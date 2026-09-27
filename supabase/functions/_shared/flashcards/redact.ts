// MRB-351 landing (27 Sep 2026) — a conservative, mechanical redaction pass
// over TEXT content, run before it is ever handed to the model for
// extraction. Defence in depth: the extraction prompt already tells the
// model to "ignore… ANY names of pupils or staff" (EXTRACT_SYSTEM in
// model.ts), but a prompt is an instruction the model could be talked out of
// by something inside the file itself. This runs with no model in the loop,
// so nothing in the file can switch it off.
//
// It touches ONLY the text path (pptx/docx/xlsx/csv/txt/md, read into `Unit`s
// by read_file.ts). It never touches PDFs or images — those go to the model
// as raw bytes, and a scanned register cannot be redacted by a text pass.
// `shared/flashcard-decks.js`'s upload notice tells the teacher that,
// plainly, for that reason.
//
// What it removes, from every line and every table-row-as-line (table rows
// already arrive as "| a | b |" strings inside `Unit.lines` — see
// read_file.ts's readPptx/readDocx/readXlsx):
//
//  · a roster-like block — 4 or more CONSECUTIVE short lines that are each
//    nothing but 2 or 3 capitalised words ("Amelia Hart", "Jacob Singh", …),
//    the shape of a seating plan or a class list pasted onto a slide;
//  · a shorter run of the same shape sitting directly under a heading that
//    NAMES a roster ("class list", "register", "pupils", "students",
//    "names") — a header confirms context a length threshold alone cannot;
//  · every email address, anywhere;
//  · every run of 6 or more digits, anywhere (phone numbers, admission
//    numbers, dates written as one run).
//
// It is deliberately narrow. A real question or answer is essentially never
// "exactly 2 or 3 bare capitalised words and nothing else on the line" — it
// carries a question mark, digits, lower-case function words, or is simply
// longer — so this does not consume real content. `extract_test.ts` keeps
// the fixture corpus at 100% after this pass runs.

import type { Unit } from "./read_file.ts";

const EMAIL = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g;
const LONG_DIGITS = /\d{6,}/g;
const REDACTED = "[redacted]";

// A line naming a roster, and nothing much else — "Class list", "Register",
// "Register — 10h/Ph1", "Pupils". The keyword must open the line, and
// whatever follows it must be a bare class-code-shaped token (letters,
// digits, "/") with no further words — never free-running prose. That is
// what stops an ordinary sentence that happens to use one of these words in
// passing ("Students should recall the reflex arc.") from being mistaken
// for a heading: "should recall the reflex arc." contains spaces and is not
// a bare token, so it fails to match and the sentence is left alone.
const ROSTER_HEADER = /^(class\s*list|register|pupils?|students?|names?)\b[\s:—-]*[A-Za-z0-9/]{0,24}$/i;

// "Firstname"/"Lastname"-shaped: starts with a capital, then letters, with
// an apostrophe or hyphen allowed inside ("O'Brien", "Smith-Jones") and a
// SECOND capital allowed inside too ("McCarthy", "MacDonald") — surnames
// this common are worth the small extra reach, since a real answer word
// almost never has this exact shape applied to EVERY word on the line with
// nothing else present.
const NAME_WORD = /^[A-Z][a-zA-Z]*(?:['-][a-zA-Z]+)?$/;

function scrub(s: string): string {
  return s.replace(EMAIL, REDACTED).replace(LONG_DIGITS, REDACTED);
}

// True when a line (or a "| cell | cell |" table row, read the same way) is
// nothing but 2 or 3 name-shaped words.
function looksLikeAName(line: string): boolean {
  const t = line.replace(/\|/g, " ").replace(/\s+/g, " ").trim();
  if (!t || t.length > 40) return false;
  const words = t.split(" ");
  if (words.length < 2 || words.length > 3) return false;
  return words.every((w) => NAME_WORD.test(w));
}

function isRosterHeader(line: string): boolean {
  const t = line.replace(/\|/g, " ").replace(/\s+/g, " ").trim();
  return t.length > 0 && ROSTER_HEADER.test(t);
}

// Drop runs of >=4 consecutive name-like lines. Directly under a header
// naming a roster, the threshold drops to 1 — a header is itself enough
// context to redact even a short list.
function redactLines(lines: string[]): string[] {
  const out: string[] = [];
  let run: string[] = [];
  let underHeader = false;
  const flush = () => {
    if (run.length < (underHeader ? 1 : 4)) out.push(...run);
    run = [];
  };
  for (const raw of lines) {
    const line = scrub(raw);
    if (isRosterHeader(line)) {
      flush();
      underHeader = true;
      continue;                    // the header line itself carries no card content
    }
    if (looksLikeAName(line)) {
      run.push(line);
      continue;
    }
    flush();
    underHeader = false;
    out.push(line);
  }
  flush();
  return out;
}

export function redactUnits(units: Unit[]): Unit[] {
  return units.map((u) => ({
    ...u,
    lines: redactLines(u.lines),
    notes: u.notes ? redactLines(u.notes) : u.notes,
  }));
}
