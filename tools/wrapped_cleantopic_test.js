#!/usr/bin/env node
/* Unit test for cleanTopic() in shared/wrapped.js. Loads the function by its
   cleanTopic:start / cleanTopic:end markers, so it tests the shipped text.
   Run: node tools/wrapped_cleantopic_test.js */
const fs = require("fs"), path = require("path");
const src = fs.readFileSync(path.join(__dirname, "..", "shared", "wrapped.js"), "utf8");
const m = src.match(/\/\* cleanTopic:start[\s\S]*?\*\/([\s\S]*?)\/\* cleanTopic:end \*\//);
if (!m) { console.error("cleanTopic markers not found"); process.exit(2); }
const cleanTopic = new Function(m[1] + "; return cleanTopic;")();

const CASES = [
  /* the brief's and tricky cases */
  ["(Higher) Rate of Reaction Quiz", "Rate of Reaction"],
  ["HT Cell Division Quiz", "Cell Division"],
  ["Forces [Foundation]", "Forces"],
  ["ENERGY STORES DECK", "Energy stores"],
  ["Quiz", "Quiz"],
  ["(Higher)", "(Higher)"],
  ["Atoms - Flashcards", "Atoms"],
  ["Bonding: Homework", "Bonding"],
  ["Cell Biology (Triple)", "Cell Biology"],
  ["[Foundation] Electricity deck", "Electricity"],
  ["DNA", "DNA"],
  ["DNA QUIZ", "DNA"],
  ["  Particle   model  ", "Particle model"],
  ["Energy (higher) quiz", "Energy"],
  /* real titles from the TEST assignments table (assignments.title / .topic) */
  ["Acids and Alkalis quiz (Wk 22)", "Acids and Alkalis"],
  ["Atomic Structure (Wk 1)", "Atomic Structure"],
  ["Atomic structure key words", "Atomic structure key words"],
  ["Cell structures — flashcards", "Cell structures"],
  ["Cells and organisation — homework", "Cells and organisation"],
  ["Animal and plant cells — homework (next week)", "Animal and plant cells — homework (next week)"],
  ["Forces quiz (Wk 21)", "Forces"],
  ["Periodic Table quiz (Wk 20)", "Periodic Table"],
  ["Photosynthesis quiz (Wk 22)", "Photosynthesis"],
  ["Cell Division quiz (Wk 21)", "Cell Division"],
  ["Energy transfers · Breathing and gas exchange · Chemical reactions", "Energy transfers · Breathing and gas exchange · Chemical reactions"],
  ["Catch-up: Energy", "Catch-up: Energy"],
  ["Movement: skeleton and muscles", "Movement: skeleton and muscles"],
  ["Homeostasis", "Homeostasis"],
  ["Infection & Response (Wk 3)", "Infection & Response"],
  ["", ""],
];
let bad = 0;
for (const [i, want] of CASES) {
  const got = cleanTopic(i);
  const ok = got === want; if (!ok) { bad++; }
  console.log((ok ? "ok   " : "FAIL ") + JSON.stringify(i) + " -> " + JSON.stringify(got) + (ok ? "" : "  (wanted " + JSON.stringify(want) + ")"));
}
for (const v of [null, undefined, 5]) { if (cleanTopic(v) !== v) { bad++; console.log("FAIL non-string passthrough", v); } }
console.log(bad ? bad + " FAILED" : "all " + CASES.length + " passed");
process.exit(bad ? 1 : 0);
