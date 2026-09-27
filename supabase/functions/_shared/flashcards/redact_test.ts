// MRB-351 landing (27 Sep 2026) — direct unit tests for the redaction pass,
// independent of the pptx fixture (see extract_test.ts's own redaction test
// for the end-to-end proof through `extract()`).
//   deno test --allow-read --allow-env --allow-net supabase/functions/_shared/flashcards/

import { assert, assertEquals } from "jsr:@std/assert@1";
import { redactUnits } from "./redact.ts";
import type { Unit } from "./read_file.ts";

function unit(lines: string[]): Unit {
  return { ref: "slide 1", lines };
}

Deno.test("redact: a run of >=4 short 'Firstname Lastname' lines is dropped", () => {
  const out = redactUnits([unit([
    "10h/Ph1 — seating & groups",
    "Amelia Hart", "Jacob Singh", "Olivia Brennan", "Noah Kowalski", "Isla McCarthy", "Leo Adeyemi",
  ])]);
  assertEquals(out[0].lines, ["10h/Ph1 — seating & groups"]);
});

Deno.test("redact: a run of only 3 name-like lines is kept (below the threshold, no header)", () => {
  const out = redactUnits([unit(["Amelia Hart", "Jacob Singh", "Olivia Brennan", "What is a cell?"])]);
  assertEquals(out[0].lines, ["Amelia Hart", "Jacob Singh", "Olivia Brennan", "What is a cell?"]);
});

Deno.test("redact: a header naming a roster drops even a short run under it", () => {
  const out = redactUnits([unit(["Class list", "Amelia Hart", "Jacob Singh", "What is a cell?"])]);
  assertEquals(out[0].lines, ["What is a cell?"]);
});

Deno.test("redact: 'Register' as a heading works the same way", () => {
  const out = redactUnits([unit(["Register — 10h/Ph1", "Amelia Hart", "The basic unit of life"])]);
  assertEquals(out[0].lines, ["The basic unit of life"]);
});

Deno.test("redact: real Q/A content is never touched", () => {
  const lines = [
    "What is the speed of light in a vacuum?", "300 000 000 m/s",
    "Name the part of the electromagnetic spectrum with the longest wavelength.", "Radio waves",
    "Which electromagnetic waves are used to cook food?", "Microwaves",
    "Which electromagnetic waves are used in remote controls?", "Infrared",
  ];
  const out = redactUnits([unit(lines)]);
  assertEquals(out[0].lines, lines);
});

Deno.test("redact: an ordinary sentence using the word 'students' in passing is not a header", () => {
  const out = redactUnits([unit(["Students should recall the reflex arc.", "Sodium Chloride", "Isaac Newton"])]);
  assertEquals(out[0].lines, ["Students should recall the reflex arc.", "Sodium Chloride", "Isaac Newton"]);
});

Deno.test("redact: email addresses and long digit runs are scrubbed wherever they appear", () => {
  const out = redactUnits([unit([
    "Email your teacher at amelia.hart@rainford.sch.uk with questions.",
    "The admission number is 20261234567.",
  ])]);
  assert(!out[0].lines[0].includes("@"));
  assert(out[0].lines[0].includes("[redacted]"));
  assert(!/\d{6,}/.test(out[0].lines[1]));
});

Deno.test("redact: table rows carried as '| a | b |' lines are read the same way as plain lines", () => {
  const out = redactUnits([unit([
    "| Amelia | Hart |", "| Jacob | Singh |", "| Olivia | Brennan |", "| Noah | Kowalski |",
    "| What is a cell? | The basic unit of life |",
  ])]);
  assertEquals(out[0].lines, ["| What is a cell? | The basic unit of life |"]);
});
