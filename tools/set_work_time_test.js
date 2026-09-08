/* set_work_time_test.js — the London ↔ UTC helpers in shared/set-work.js.
 *
 *   node tools/set_work_time_test.js
 *
 * MRB-335, RISKS B1/B8. A teacher types a WALL CLOCK and the server stores an
 * INSTANT. Between the two sit the hour that happens twice on 25 Oct 2026 and
 * the hour that never happens on 28 Mar 2027, and getting either wrong sets
 * thirty children work that opens an hour early or a day late.
 *
 * ⚠️ IT LOADS THE REAL FILE. `shared/set-work.js` is an IIFE that attaches to
 * `window` and touches `document` only inside functions, so a bare object
 * standing in for `window` is enough to reach the pure helpers. Retyping them
 * here would test a copy — which is exactly the drift a copy exists to hide.
 *
 * ⚠️ NOT A REGISTERED GATE, and that is not an oversight. `gate_registry.py`'s
 * `coverage()` scans the repo ROOT for `.py`/`.sh`; this is neither, and lives
 * in `tools/`. It is run by hand and its result is recorded in the run report.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const SRC = path.join(__dirname, "..", "shared", "set-work.js");

const sandbox = { window: {}, console, Intl, Date, Math, JSON, setTimeout, clearTimeout };
sandbox.globalThis = sandbox;
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(SRC, "utf8"), sandbox, { filename: SRC });

const SW = sandbox.window.MRBSetWork;
if (!SW || typeof SW.londonToUtcIso !== "function") {
  console.error("set_work_time_test: shared/set-work.js did not expose the helpers");
  process.exit(2);
}

let failures = 0;
function check(name, got, want) {
  const ok = got === want;
  if (!ok) { failures += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}\n           got  ${got}\n           want ${want}`);
}

/* ── London wall clock → UTC ─────────────────────────────────────────────
 *
 * BST ends 25 Oct 2026 at 02:00 BST (01:00 UTC); BST begins 28 Mar 2027 at
 * 01:00 GMT (01:00 UTC).
 *
 *  24 Oct 23:30  plain BST                      → 22:30 UTC
 *  25 Oct 00:30  still BST                      → 23:30 UTC on the 24th
 *  25 Oct 01:30  AMBIGUOUS, happens twice       → 00:30 UTC (the EARLIER,
 *                                                  i.e. 01:30 BST)
 *  25 Oct 02:30  GMT, after the change          → 02:30 UTC
 *  26 Oct 07:00  plain GMT                      → 07:00 UTC
 *  28 Mar 01:30  NONEXISTENT, inside the gap    → 01:30 UTC, which reads
 *                                                  02:30 BST — shifted
 *                                                  forward by the gap
 */
console.log("London wall clock -> UTC");
check("2026-10-24 23:30 BST", SW.londonToUtcIso("2026-10-24", "23:30"), "2026-10-24T22:30:00.000Z");
check("2026-10-25 00:30 BST", SW.londonToUtcIso("2026-10-25", "00:30"), "2026-10-24T23:30:00.000Z");
check("2026-10-25 01:30 ambiguous -> earlier", SW.londonToUtcIso("2026-10-25", "01:30"), "2026-10-25T00:30:00.000Z");
check("2026-10-25 02:30 GMT", SW.londonToUtcIso("2026-10-25", "02:30"), "2026-10-25T02:30:00.000Z");
check("2026-10-26 07:00 GMT", SW.londonToUtcIso("2026-10-26", "07:00"), "2026-10-26T07:00:00.000Z");
check("2027-03-28 01:30 gap -> forward", SW.londonToUtcIso("2027-03-28", "01:30"), "2027-03-28T01:30:00.000Z");

/* ── UTC → London wall clock ──────────────────────────────────────────── */
console.log("\nUTC -> London wall clock");
function parts(iso) { const p = SW.utcToLondonParts(iso); return p ? p.date + " " + p.time : String(p); }
check("2026-10-24T22:30Z", parts("2026-10-24T22:30:00.000Z"), "2026-10-24 23:30");
check("2026-10-24T23:30Z", parts("2026-10-24T23:30:00.000Z"), "2026-10-25 00:30");
check("2026-10-25T00:30Z (BST, 1st pass)", parts("2026-10-25T00:30:00.000Z"), "2026-10-25 01:30");
check("2026-10-25T01:30Z (GMT, 2nd pass)", parts("2026-10-25T01:30:00.000Z"), "2026-10-25 01:30");
check("2026-10-25T02:30Z", parts("2026-10-25T02:30:00.000Z"), "2026-10-25 02:30");
check("2026-10-26T07:00Z", parts("2026-10-26T07:00:00.000Z"), "2026-10-26 07:00");
check("2027-03-28T01:30Z", parts("2027-03-28T01:30:00.000Z"), "2027-03-28 02:30");

/* ── round trip ───────────────────────────────────────────────────────────
 * Every unambiguous case must survive both directions unchanged. The two
 * that cannot are stated rather than skipped: the ambiguous hour returns the
 * SAME wall clock (both instants read 01:30), and the gap hour returns the
 * shifted one. */
console.log("\nround trip (wall -> UTC -> wall)");
[["2026-10-24", "23:30"], ["2026-10-25", "00:30"], ["2026-10-25", "02:30"],
 ["2026-10-26", "07:00"], ["2026-06-15", "18:00"], ["2027-01-04", "07:00"]
].forEach(function (c) {
  check(c[0] + " " + c[1], parts(SW.londonToUtcIso(c[0], c[1])), c[0] + " " + c[1]);
});
check("2026-10-25 01:30 ambiguous returns its own clock",
      parts(SW.londonToUtcIso("2026-10-25", "01:30")), "2026-10-25 01:30");
check("2027-03-28 01:30 gap returns the shifted clock",
      parts(SW.londonToUtcIso("2027-03-28", "01:30")), "2027-03-28 02:30");

/* ── offsets ────────────────────────────────────────────────────────────── */
console.log("\noffset minutes east of UTC");
check("2026-06-15 (BST)", SW.londonOffsetMinutesAt(Date.parse("2026-06-15T12:00:00Z")), 60);
check("2027-01-04 (GMT)", SW.londonOffsetMinutesAt(Date.parse("2027-01-04T12:00:00Z")), 0);
check("2026-10-25T00:59Z (still BST)", SW.londonOffsetMinutesAt(Date.parse("2026-10-25T00:59:00Z")), 60);
check("2026-10-25T01:00Z (GMT)", SW.londonOffsetMinutesAt(Date.parse("2026-10-25T01:00:00Z")), 0);

/* ── the hold line's date label ─────────────────────────────────────────── */
console.log("\nhold line date label");
check("14 Sep 2026", SW.londonDateLabel("2026-09-14T00:00:00.000Z"), "14 Sep 2026");
check("1 Jan 2027", SW.londonDateLabel("2027-01-01T09:00:00.000Z"), "1 Jan 2027");
/* 23:30 UTC on 13 Sep is already the 14th in BST. The label must be the day a
   teacher in London would say, not the day the instant is in UTC. */
check("13 Sep 23:30Z is 14 Sep in London",
      SW.londonDateLabel("2026-09-13T23:30:00.000Z"), "14 Sep 2026");

/* ── the school hold is LONDON midnight ────────────────────────────────────
 * MRB-335 item 4. `schools.assignments_open_from` is a DATE, and
 * `Date.parse("2026-09-14")` reads it as 00:00 UTC — which in BST is 01:00 on
 * the morning of the 14th. Work released at 00:30 London on the day a school
 * opens was therefore judged to be BEFORE the hold, one hour wide, five months
 * of the year, and only ever at night. `holdMs()` converts the DATE the same
 * way the release and due fields are converted, so the sheet and the server
 * cannot disagree about the same midnight. */
console.log("\nschool hold — London midnight on its own date");
check("14 Sep 2026 (BST) is 23:00Z on the 13th",
      SW.londonToUtcIso("2026-09-14", "00:00"), "2026-09-13T23:00:00.000Z");
check("…so 00:30 London on the 14th is NOT before it",
      Date.parse(SW.londonToUtcIso("2026-09-14", "00:30")) >=
      Date.parse(SW.londonToUtcIso("2026-09-14", "00:00")), true);
check("…and naive UTC midnight would have said it WAS",
      Date.parse("2026-09-14") > Date.parse(SW.londonToUtcIso("2026-09-14", "00:30")), true);
check("4 Jan 2027 (GMT) is 00:00Z on the day itself",
      SW.londonToUtcIso("2027-01-04", "00:00"), "2027-01-04T00:00:00.000Z");
check("in GMT the naive read agrees",
      Date.parse("2027-01-04"), Date.parse(SW.londonToUtcIso("2027-01-04", "00:00")));

console.log(failures ? `\n${failures} FAILED` : "\nall checks passed");
process.exit(failures ? 1 : 0);
