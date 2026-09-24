// MRB-351 — the extraction tests. Run:  deno test --allow-read --allow-env --allow-net supabase/functions/_shared/flashcards/
//
// Three layers:
//   1. the file reader keeps what pairing depends on (slide order, speaker
//      notes, red/bold answers, tables as cells, docx page breaks);
//   2. the no-model rules pair exactly the shapes they claim, and refuse the
//      rest;
//   3. the whole corpus through `extract()` scores ≥ 90% of pairs recovered
//      and leaks no pupil name. The model path REPLAYS the recorded replies in
//      tests/fixtures/flashcards/recorded/ unless FLASHCARD_LIVE=1 and an
//      ANTHROPIC_API_KEY are set, in which case it makes the real calls.

import { assert, assertEquals } from "jsr:@std/assert@1";
import { readFile, render } from "./read_file.ts";
import { linePairs, tablePairs } from "./pairs.ts";
import { extract } from "./pipeline.ts";
import { scoreFixture, type Expected } from "./score.ts";

const DIR = new URL("../../../../tests/fixtures/flashcards/", import.meta.url);
const bytes = (n: string) => Deno.readFileSync(new URL(n, DIR));
const EXPECTED: Record<string, Expected> = JSON.parse(new TextDecoder().decode(bytes("expected.json")));

Deno.test("pptx: 41 slides in order, next-slide answers present", () => {
  const r = readFile("rainford_forces_next_slide.pptx", bytes("rainford_forces_next_slide.pptx"));
  assert(r.kind === "text");
  assertEquals(r.units.length, 41);
  assertEquals(r.units[1].ref, "slide 2");
  assert(r.units[1].lines.some((l) => l.includes("What is the unit of force?")));
  assert(r.units[2].lines.some((l) => l.includes("The newton (N)")));
});

Deno.test("pptx: speaker notes are read and slide furniture is not", () => {
  const r = readFile("cells_speaker_notes.pptx", bytes("cells_speaker_notes.pptx"));
  assert(r.kind === "text");
  assertEquals(r.units.length, 8);
  assert(r.units[0].notes?.[0].startsWith("Answer: It contains genetic material"));
  assert(render(r.units).includes("[speaker notes]"));
});

Deno.test("pptx: a red answer on the same line is marked, the question is not", () => {
  const r = readFile("acids_red_answers.pptx", bytes("acids_red_answers.pptx"));
  assert(r.kind === "text");
  const line = r.units[0].lines.find((l) => l.includes("sulfuric"))!;
  assert(line.includes("[red]H2SO4[/red]"), line);
  assert(!line.includes("[red]7"), line);
});

Deno.test("docx: a page break splits the questions from the answers", () => {
  const r = readFile("atoms_answers_at_end.docx", bytes("atoms_answers_at_end.docx"));
  assert(r.kind === "text");
  assertEquals(r.units.map((u) => u.ref), ["page 1", "page 2"]);
  assert(r.units[1].lines.includes("# Answers"));
});

Deno.test("no-model rules: tables and Q/A lines pair exactly; other shapes are refused", () => {
  for (const [name, n] of [["energy_two_column_table.docx", 12], ["waves_keywords.xlsx", 10], ["chemistry_basics.csv", 15]] as const) {
    const r = readFile(name, bytes(name));
    assert(r.kind === "text");
    const t = tablePairs(r.units);
    assert(t, name);
    assertEquals(t!.cards.length, n, name);
  }
  const qa = readFile("x.txt", new TextEncoder().encode("Q: What is a cell?\nA: The basic unit of life\nQ: What is an organ?\nA: A group of tissues\nworking together\nQ: What is a tissue?\nA: A group of similar cells"));
  assert(qa.kind === "text");
  const lp = linePairs(qa.units)!;
  assertEquals(lp.cards.length, 3);
  assertEquals(lp.cards[1].answer, "A group of tissues working together");
  for (const name of ["photosynthesis_cloze.txt", "enzymes_questions_only.md", "atoms_answers_at_end.docx",
                      "em_spectrum_with_class_list.pptx", "rainford_forces_next_slide.pptx"]) {
    const r = readFile(name, bytes(name));
    assert(r.kind === "text");
    assertEquals(tablePairs(r.units) ?? linePairs(r.units), null, name);
  }
});

Deno.test("limits: 25 MB and unknown types are refused", () => {
  let code = "";
  try { readFile("x.exe", new Uint8Array(4)); } catch (e) { code = (e as { code: string }).code; }
  assertEquals(code, "unsupported_type");
  try { readFile("x.pdf", new Uint8Array(25 * 1024 * 1024 + 1)); } catch (e) { code = (e as { code: string }).code; }
  assertEquals(code, "too_big");
});

Deno.test("corpus: ≥ 90% of pairs recovered, no pupil name leaks", async () => {
  const live = Deno.env.get("FLASHCARD_LIVE") === "1" && !!Deno.env.get("ANTHROPIC_API_KEY");
  let expected = 0, recovered = 0;
  const lines: string[] = [];
  for (const [name, exp] of Object.entries(EXPECTED)) {
    const res = await extract(name, bytes(name), live ? { apiKey: Deno.env.get("ANTHROPIC_API_KEY")! } : {
      model: () => {
        const rec = JSON.parse(new TextDecoder().decode(bytes(`recorded/${name}.json`)));
        return Promise.resolve({ result: { method: "model", ...rec }, usage: { model: "recorded", input_tokens: 0, output_tokens: 0 } });
      },
    });
    const s = scoreFixture(exp, res.rows);
    expected += s.expected; recovered += s.recovered;
    lines.push(`${name.padEnd(38)} ${res.method.padEnd(6)} ${String(s.recovered).padStart(3)}/${String(s.expected).padEnd(3)} extra ${s.extra}` +
      (s.misses.length ? `  missed: ${s.misses.slice(0, 3).join(" | ")}` : "") + (s.leaked.length ? `  LEAKED ${s.leaked}` : ""));
    assertEquals(s.leaked, [], `${name} leaked a name`);
  }
  const pct = recovered / expected;
  console.log(`\n${live ? "LIVE" : "RECORDED"} corpus score: ${recovered}/${expected} = ${(pct * 100).toFixed(1)}%\n` + lines.join("\n"));
  assert(pct >= 0.9, `corpus score ${(pct * 100).toFixed(1)}% is under 90%`);
});

Deno.test("the scorer is not a rubber stamp: answers shifted by one card recover almost nothing", () => {
  const exp = EXPECTED["rainford_forces_next_slide.pptx"];
  const rec = JSON.parse(new TextDecoder().decode(bytes("recorded/rainford_forces_next_slide.pptx.json")));
  const cards = rec.cards as { question: string; answer: string }[];
  const shifted = cards.map((c, i) => ({ question: c.question, answer: cards[(i + 1) % cards.length].answer }));
  const s = scoreFixture(exp, shifted);
  assert(s.recovered <= 2, `shifted answers still scored ${s.recovered}/20`);
  const invented = scoreFixture(EXPECTED["enzymes_questions_only.md"],
    EXPECTED["enzymes_questions_only.md"].pairs.map((p) => ({ question: p.q, answer: "an invented answer" })));
  assertEquals(invented.recovered, 0);
});
