/* student_challenge_rows_test.js — Unit C: the pupil class page's rows for a
 * teacher-set WEEKLY CHALLENGE (`weeklyChallengeRows` in shared/student-live.js),
 * and the guards that keep one out of every question-set sum.
 *
 *   node tools/student_challenge_rows_test.js
 *
 * Loads the REAL file. `shared/student-live.js` is one big IIFE that touches
 * the DOM only inside functions, and hands the pure helper out through
 * `window.__MRB_WC_ROWS__`; a bare sandbox is enough to reach it.
 *
 * Pins brief 3(b) and 3(c): a row is "Weekly challenge: Physics", links to
 * /weekly-challenge.html?subject=physics, is open until due_at (or played),
 * then closed -- never missed, never late, never marked -- and carries no
 * questions, bar, reopen button or score. The source guards for 3(a) (kept out
 * of `cards`, never the bench) are asserted on the file text, because they are
 * three lines of a function that cannot run without a database.
 *
 * Not a registered gate (lives in tools/); run by hand, recorded in the run
 * report.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const SRC = path.join(__dirname, "..", "shared", "student-live.js");
const text = fs.readFileSync(SRC, "utf8");

const sandbox = {
  window: {}, document: { addEventListener() {}, readyState: "loading" },
  location: { search: "", hash: "", pathname: "/student/class.html", href: "" },
  console, Intl, Date, Math, JSON, Promise, setTimeout, clearTimeout,
  navigator: { userAgent: "node" }, localStorage: { getItem() { return null; } }
};
sandbox.window = sandbox;
sandbox.globalThis = sandbox;
vm.createContext(sandbox);
try { vm.runInContext(text, sandbox, { filename: SRC }); }
catch (e) { /* the page's own start-up may need a browser; the helper is set first */ }

const rows = sandbox.__MRB_WC_ROWS__;
let failures = 0;
function check(name, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  if (!ok) { failures += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}${ok ? "" : `\n           got  ${JSON.stringify(got)}\n           want ${JSON.stringify(want)}`}`);
}
if (typeof rows !== "function") {
  console.error("student_challenge_rows_test: shared/student-live.js did not expose weeklyChallengeRows");
  process.exit(2);
}

const NOW = Date.parse("2026-10-21T12:00:00Z");
const ctx = {
  weeks: {}, currentWeek: 8, weekOf: function () { return 1; }, serverNow: NOW,
  fmtDue: function (iso) { return "due:" + iso; }
};
const card = function (over) {
  return Object.assign({ id: "w1", title: "Weekly challenge: Physics", kind: "weekly_challenge",
                         subject_name: "Physics", due_at: "2026-10-23T09:15:00Z" }, over || {});
};

console.log("open (not played, before due_at)");
let r = rows([card()], [], ctx)[0];
check("title is the teacher-visible one", r.title, "Weekly challenge: Physics");
check("links to the challenge page with the subject", r.assignmentHref, "/weekly-challenge.html?subject=physics");
check("status open, not played", [r.status, r.played, r.wc], ["open", false, true]);
check("detail is the due phrase", r.detail, "due:2026-10-23T09:15:00Z");
check("no questions: no brief, no lessons, no qtotal/answered/score", [r.brief, r.lessons, r.qtotal, r.answered, r.score, r.rawScore, r.late, r.reopen], ["", [], undefined, undefined, undefined, undefined, undefined, undefined]);
check("lands in the current teaching week", r.week, 8);

console.log("\nplayed (week_work says done)");
r = rows([card()], [{ id: "w1", challenge: { subject: "physics", week_start: "2026-10-16", done: true } }], ctx)[0];
check("closed + played", [r.status, r.played], ["closed", true]);
check("the deadline still shown once played (the panel is never empty)", r.detail, "due:2026-10-23T09:15:00Z");
check("still links to the page", r.assignmentHref, "/weekly-challenge.html?subject=physics");

console.log("\npast due_at, not played");
const late = Object.assign({}, ctx, { serverNow: Date.parse("2026-10-23T09:16:00Z") });
r = rows([card()], [{ id: "w1", challenge: { subject: "physics", done: false } }], late)[0];
check("closed, not played", [r.status, r.played], ["closed", false]);
check("never missed / late / marked / pending", ["missed", "marked", "pending"].indexOf(r.status) === -1 && r.late === undefined, true);

console.log("\nsubject sources");
check("week_work subject wins", rows([card({ subject_name: "Biology" })], [{ id: "w1", challenge: { subject: "chemistry" } }], ctx)[0].assignmentHref, "/weekly-challenge.html?subject=chemistry");
check("else the assignment's subject", rows([card({ subject_name: "Biology" })], [], ctx)[0].assignmentHref, "/weekly-challenge.html?subject=biology");
check("else the title", rows([card({ subject_name: null, title: "Weekly challenge: Chemistry" })], undefined, ctx)[0].assignmentHref, "/weekly-challenge.html?subject=chemistry");
check("an unknown subject links to the bare page", rows([card({ subject_name: "Science", title: "Weekly challenge" })], [], ctx)[0].assignmentHref, "/weekly-challenge.html");

console.log("\nthe row's own week beats the current week");
check("academic_week from the data layer", rows([card()], [], Object.assign({}, ctx, { weeks: { w1: 5 } }))[0].week, 5);
check("no week anywhere -> weekOf", rows([card()], [], Object.assign({}, ctx, { currentWeek: null }))[0].week, 1);

console.log("\nthe guards (3a): kept out of every question-set sum");
const has = function (s) { return text.indexOf(s) > -1; };
check("kind is split out of `cards` once", has('var cards = allCards.filter(function (c) { return !(c && c.kind === "weekly_challenge"); });'), true);
check("the week_work bench pick refuses a challenge row", has("if (w.challenge) { return false; }"), true);
check("the data layer names the kind", fs.readFileSync(path.join(__dirname, "..", "shared", "student-data.js"), "utf8").indexOf("'weekly_challenge'") > -1, true);

console.log(failures ? `\n${failures} FAILED` : "\nall passed");
process.exit(failures ? 1 : 0);
