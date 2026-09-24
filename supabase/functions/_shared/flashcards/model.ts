// MRB-351 — the ONE Claude call per extraction, and the answer-check call.
//
// Extraction: Sonnet-class (vision when the file is a scan or a photo), one
// request, structured output against EXTRACT_SCHEMA. Answer check:
// Haiku-class, one request per sitting's batch, structured output against
// CHECK_SCHEMA, and the ONLY things in it are question, model answer and the
// pupil's answer — no name, no id, no class, not even our own row ids (items
// are numbered 0..n-1 inside the request and mapped back here).

import Anthropic from "npm:@anthropic-ai/sdk@0.128.0";
import type { Extraction } from "./pairs.ts";
import type { Readable } from "./read_file.ts";
import { render } from "./read_file.ts";

export const EXTRACT_MODEL = "claude-sonnet-5";
export const CHECK_MODEL = "claude-haiku-4-5";

export const EXTRACT_SYSTEM = `You turn a teacher's revision material into flashcards for GCSE and KS3 science pupils.

You are given one file: slides, a document, a worksheet, a spreadsheet, a scan or a photo. Find every question–answer pair in it and return them in the order they appear.

The shapes teachers actually produce, and what to do with each:
- A two-column table (question | answer, or keyword | definition): each row is a card. A keyword row becomes a card whose question is the keyword itself and whose answer is the definition.
- "Q:" / "A:" lines, or "Question 3" / "Answer 3": pair them.
- Numbered questions with an answer section later ("Answers", "Mark scheme", a second list numbered the same way): pair question n with answer n.
- A question on one slide and its answer on the NEXT slide ("Question 4" then "Answer 4", or a slide that repeats the question and adds the answer): pair them; the answer slide is not a card of its own.
- The answer on the same slide or line, marked in red, green, blue, bold or a highlight. In the text you are given, coloured runs are wrapped like [red]…[/red] and bold runs like **…**; the marked part is the answer and the rest is the question. Remove the markers.
- Answers in the speaker notes ("[speaker notes]" after a slide): the slide text is the question, the note is the answer. Drop leading "Answer:" labels.
- Cloze sentences with a gap ("Plants make glucose by ______."): make a card whose question is the sentence with the gap kept as "___", and whose answer is the missing word or words (use a word bank if one is given).
- A list of questions with no answers anywhere: return each question in unpaired_questions. Never invent an answer.
- An answer you cannot place with a question: return it in unpaired_answers.

Rules:
- Copy the teacher's wording. Fix only obvious extraction damage (a word split across a line break, stray numbering, bullet characters). Do not paraphrase, shorten, add to, or "improve" either side.
- Keep chemical formulae exactly as written in plain characters (H2O, CO2, H2SO4); units and symbols as written.
- Ignore everything that is not revision content: titles, learning objectives, instructions to pupils, dates, slide numbers, "Do Now", seating plans, class lists, and ANY names of pupils or staff. Never put a person's name in a card, and never repeat names anywhere in your output.
- source_ref says where the card came from in a few words, e.g. "slide 7", "slides 7–8", "page 2", "row 5", or null.
- confidence is 0 to 1: 1 when the pairing is explicit in the file; lower when you had to infer which answer belongs to which question, when the file is hard to read, or when the answer looks incomplete.
- A question is at most 400 characters and an answer at most 600.`;

export const EXTRACT_SCHEMA = {
  type: "object",
  additionalProperties: false,
  required: ["cards", "unpaired_questions", "unpaired_answers"],
  properties: {
    cards: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        required: ["question", "answer", "source_ref", "confidence"],
        properties: {
          question: { type: "string" },
          answer: { type: "string" },
          source_ref: { type: ["string", "null"] },
          confidence: { type: "number" },
        },
      },
    },
    unpaired_questions: {
      type: "array",
      items: {
        type: "object", additionalProperties: false, required: ["question", "source_ref"],
        properties: { question: { type: "string" }, source_ref: { type: ["string", "null"] } },
      },
    },
    unpaired_answers: {
      type: "array",
      items: {
        type: "object", additionalProperties: false, required: ["answer", "source_ref"],
        properties: { answer: { type: "string" }, source_ref: { type: ["string", "null"] } },
      },
    },
  },
} as const;

export type Usage = { model: string; input_tokens: number; output_tokens: number };

function b64(bytes: Uint8Array): string {
  let s = "";
  const CH = 0x8000;
  for (let i = 0; i < bytes.length; i += CH) s += String.fromCharCode(...bytes.subarray(i, i + CH));
  return btoa(s);
}

// The user turn: the file itself (pdf/image) or its structured text.
// deno-lint-ignore no-explicit-any
export function extractContent(r: Readable, fileName: string): any[] {
  const label = `File name: ${fileName.replace(/[^\w .()-]/g, "_").slice(0, 120)}`;
  if (r.kind === "pdf") {
    return [
      { type: "document", source: { type: "base64", media_type: "application/pdf", data: b64(r.data) } },
      { type: "text", text: `${label}\nExtract the flashcards from this PDF.` },
    ];
  }
  if (r.kind === "image") {
    return [
      { type: "image", source: { type: "base64", media_type: r.mediaType, data: b64(r.data) } },
      { type: "text", text: `${label}\nThis is a photo or scan of a sheet. Extract the flashcards from it.` },
    ];
  }
  return [{ type: "text", text: `${label}\n\n<file>\n${render(r.units)}\n</file>\n\nExtract the flashcards from this file.` }];
}

export async function extractWithModel(r: Readable, fileName: string, apiKey: string):
    Promise<{ result: Extraction; usage: Usage }> {
  const client = new Anthropic({ apiKey });
  const msg = await client.messages.create({
    model: EXTRACT_MODEL,
    max_tokens: 16000,
    system: EXTRACT_SYSTEM,
    output_config: { effort: "medium", format: { type: "json_schema", schema: EXTRACT_SCHEMA } },
    messages: [{ role: "user", content: extractContent(r, fileName) }],
  // deno-lint-ignore no-explicit-any
  } as any);
  // deno-lint-ignore no-explicit-any
  const m = msg as any;
  if (m.stop_reason === "refusal") throw new Error("model_refused");
  if (m.stop_reason === "max_tokens") throw new Error("model_truncated");
  // deno-lint-ignore no-explicit-any
  const text = (m.content as any[]).filter((b) => b.type === "text").map((b) => b.text).join("");
  const parsed = JSON.parse(text);
  return {
    result: { method: "model", cards: parsed.cards ?? [], unpaired_questions: parsed.unpaired_questions ?? [],
              unpaired_answers: parsed.unpaired_answers ?? [] },
    usage: { model: EXTRACT_MODEL, input_tokens: m.usage?.input_tokens ?? 0, output_tokens: m.usage?.output_tokens ?? 0 },
  };
}

// ── answer check ──────────────────────────────────────────────────────
export const CHECK_SYSTEM = `You compare a school pupil's flashcard answer with the teacher's model answer.

For each item decide:
- "match": the pupil's answer gives the key content of the model answer. Spelling mistakes, different wording, missing units the question did not ask for, or extra correct detail still count as a match.
- "partial": some of the key content is there, but something important is missing or only half right.
- "no": wrong, irrelevant, or does not answer the question.
- "blank": empty, "I don't know", a guess with no content, random letters, or a joke.

Judge science content only. Return one verdict per item, with its index.`;

export const CHECK_SCHEMA = {
  type: "object", additionalProperties: false, required: ["verdicts"],
  properties: {
    verdicts: {
      type: "array",
      items: {
        type: "object", additionalProperties: false, required: ["i", "verdict"],
        properties: { i: { type: "integer" }, verdict: { type: "string", enum: ["match", "partial", "no", "blank"] } },
      },
    },
  },
} as const;

export type CheckItem = { question: string; model_answer: string; pupil_answer: string };

export async function checkWithModel(items: CheckItem[], apiKey: string):
    Promise<{ verdicts: (string | null)[]; usage: Usage }> {
  const client = new Anthropic({ apiKey });
  const body = items.map((it, i) =>
    `<item i="${i}">\n<question>${it.question}</question>\n<model_answer>${it.model_answer}</model_answer>\n<pupil_answer>${it.pupil_answer}</pupil_answer>\n</item>`,
  ).join("\n");
  const msg = await client.messages.create({
    model: CHECK_MODEL,
    max_tokens: 4000,
    system: CHECK_SYSTEM,
    output_config: { format: { type: "json_schema", schema: CHECK_SCHEMA } },
    messages: [{ role: "user", content: body }],
  // deno-lint-ignore no-explicit-any
  } as any);
  // deno-lint-ignore no-explicit-any
  const m = msg as any;
  // deno-lint-ignore no-explicit-any
  const text = (m.content as any[]).filter((b) => b.type === "text").map((b) => b.text).join("");
  const parsed = JSON.parse(text);
  const out: (string | null)[] = items.map(() => null);
  for (const v of parsed.verdicts ?? []) {
    if (Number.isInteger(v.i) && v.i >= 0 && v.i < out.length &&
        ["match", "partial", "no", "blank"].includes(v.verdict)) out[v.i] = v.verdict;
  }
  return { verdicts: out, usage: { model: CHECK_MODEL, input_tokens: m.usage?.input_tokens ?? 0, output_tokens: m.usage?.output_tokens ?? 0 } };
}
