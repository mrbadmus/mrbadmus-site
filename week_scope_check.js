#!/usr/bin/env node
/* week_scope_check.js — x-week-truth (MRB-353 redone), 4 Oct 2026.
 *
 *   node week_scope_check.js
 *
 * Drives `shared/teacher-live.js`'s `weekScope` (and the pipeline that
 * feeds it — `buildPapers`, `assignPaperWeeks`, `buildWeeks`) directly in
 * Node, no browser and no network, against data shaped like the two real
 * classes the bug was found on: 10h/Ph1 (the live defect, seen Sun 4 Oct
 * 2026 01:04) and 8r/Sc1 (the estate's other real assignment history,
 * MRB-335's own fixture shape). Fixed clocks throughout — see CLOCKS below
 * — because the whole point of this gate is that "today" must never be an
 * input a reader can silently vary.
 *
 * WHAT IT PROVES
 *   · `started` is false ONLY on a Sunday before the week it names begins
 *     (MRB-330's roll-forward), true every other day — the fact the whole
 *     "week that has not started" branch of the rule depends on.
 *   · `lastClosed` is the most recent CLOSED, RELEASED, non-flashcard paper
 *     due at or before the end of the SELECTED week (capped at now) —
 *     scanning every paper the class has, not merely the selected week's
 *     own — which is the exact defect MRB-353's first attempt left in:
 *     asking about 10h/Ph1's week 5 (Temperature, still open) must still
 *     surface week 4's Changes of State, at every clock before Temperature
 *     itself closes, and must surface Temperature itself the moment it
 *     does (chip 0, no special case).
 *   · a flashcard set is never `lastClosed`, even when it is the newest
 *     closed thing in the class (8r/Sc1's Oct-5 flashcard set must not
 *     shadow the Oct-5 MCQ).
 *   · the week bucket rule (`papers` on the returned scope) is unchanged
 *     from `wPapers`'s own — chip 0 takes weekIdx <= 0 or null, the oldest
 *     chip takes weekIdx >= its own index, every other chip takes its own
 *     weekIdx exactly — proved by checking 8r/Sc1's pre-term-start set
 *     lands in the oldest chip's bucket.
 *   · a week object without `started`/`endMs` (an older fixture) behaves
 *     exactly as before this ruling: `started` reads true and the cutoff
 *     is simply `now`.
 *
 * WHAT IT DOES NOT PROVE: the renderVals wiring (teacher_behaviour.py's
 * fixtures below do that), or that TEST's real rows shape the same way
 * (the TEST walk in RESULT-A.md does that).
 */
"use strict";

process.env.TZ = "Europe/London";   // a UK teacher's device clock — see
                                     // teacher-live.js's own "LONDON, FOR
                                     // THE COLUMNS THAT NAME AN INSTANT".

const path = require("path");

global.window = { MRB_TEACHER_LIVE_NO_AUTORUN: true };
require(path.join(__dirname, "shared", "teacher-live.js"));
const TL = global.window.MrBadmusTeacherLive;
if (!TL || !TL.weekScope) {
  console.log("FAIL could not load window.MrBadmusTeacherLive.weekScope");
  process.exit(1);
}

let passes = 0, fails = 0;
function check(ok, what) {
  if (ok) { passes += 1; } else { fails += 1; console.log("  FAIL " + what); }
}

/* Local wall-clock constructor — London time, DST-aware via process.env.TZ
   above, so "4 Oct 2026 01:04" below means exactly what a teacher's phone
   would have said at that moment. */
function ldn(y, mo, d, h, mi) { return new Date(y, mo - 1, d, h || 0, mi || 0, 0); }

const YEAR = { start_date: "2026-09-01", end_date: "2027-08-31" };

/* A minimal `pack` — `buildPapers` reads `members.length` only for the
   roster count it stamps on each paper (irrelevant to `weekScope`, which
   never reads submissions) and `assignments` for the rows themselves. */
function scopeOf(assignments, wi, now) {
  const pack = { members: [], assignments: assignments };
  const papers = TL.buildPapers(pack, now);
  const weeks = TL.buildWeeks(YEAR, now);
  TL.assignPaperWeeks(papers, weeks, YEAR, now);
  return { scope: TL.weekScope(papers, weeks, wi, now), papers: papers, weeks: weeks };
}

// ─── 10h/Ph1 — the live defect, byte for byte ──────────────────────────
//
// "Particle Model of Matter · Changes of State" — teacher, academic_week 4,
// released Sun 20 Sep, due Mon 28 Sep 08:00Z (09:00 BST), 8 of 17 done.
// "… Temperature Changes and Specific Heat Capacity" — teacher, week 5,
// released Mon 28 Sep 14:45Z, due Mon 5 Oct 17:00Z (18:00 BST), 3 of 17.
// The two deleted "Energy" rows are not modelled: a soft-deleted
// assignment never reaches `pack.assignments` in the first place — that is
// the data layer's own job, upstream of everything `weekScope` touches —
// so "stays invisible" is proved by their simple absence here, not by a
// third input this function would have to filter.
const COS = {
  id: "cos", title: "Particle Model of Matter · Changes of State",
  source: "teacher", academic_week: 4,
  release_at: ldn(2026, 9, 20, 9, 0).toISOString(),
  due_at: "2026-09-28T08:00:00.000Z", kind: "mcq_set"
};
const TEMP = {
  id: "temp", title: "Particle Model of Matter · Temperature Changes and Specific Heat Capacity",
  source: "teacher", academic_week: 5,
  release_at: "2026-09-28T14:45:00.000Z",
  due_at: "2026-10-05T17:00:00.000Z", kind: "mcq_set"
};
const TENH = [COS, TEMP];

const CLOCKS = {
  sun: ldn(2026, 10, 4, 1, 4),    // Sun 4 Oct 2026 01:04 BST — the live defect
  wed: ldn(2026, 9, 30, 12, 0),   // Wed 30 Sep 2026 12:00 BST
  mon: ldn(2026, 10, 5, 12, 0),   // Mon 5 Oct 2026 12:00 BST — Temperature still open
  tue: ldn(2026, 10, 6, 12, 0)    // Tue 6 Oct 2026 12:00 BST — Temperature now closed
};

console.log("10h/Ph1 — chip 0 (\"this week\"), four clocks:");
Object.keys(CLOCKS).forEach(function (key) {
  const now = CLOCKS[key].getTime();
  const r = scopeOf(TENH, 0, now);
  const wantStarted = key !== "sun";
  check(r.scope.started === wantStarted,
    key + ": started === " + wantStarted + " (got " + r.scope.started + ")");
  const wantLast = (key === "tue") ? "temp" : "cos";
  const got = r.scope.lastClosed ? r.scope.lastClosed.id : null;
  check(got === wantLast,
    key + ": lastClosed === '" + wantLast + "' (got " + got + ") — " +
    (key === "tue"
      ? "Temperature has now closed and is the newer of the two"
      : "Changes of State is the newest CLOSED set" +
        (key === "mon" ? " (Temperature is due 18:00 BST, still 6h off)" : "")));
});

// The exact regression: picking WEEK 5's OWN chip (Temperature's week)
// before Temperature has closed must still surface Changes of State — the
// defect MRB-353's first attempt left in, because it searched only the
// selected week's own papers and week 5's own paper had nothing closed in
// it yet.
(function () {
  const now = CLOCKS.wed.getTime();
  const r = scopeOf(TENH, 0, now);
  const topWeek = r.weeks[0].weekOfYear;
  const wiOfWeek5 = topWeek - 5;   // the chip showing TEMP's own week
  const wiOfWeek4 = topWeek - 4;   // the chip showing COS's own week
  check(wiOfWeek5 >= 0 && wiOfWeek5 < r.weeks.length,
    "week 5's own chip (wi=" + wiOfWeek5 + ") exists on the bar at the Wed clock");
  if (wiOfWeek5 >= 0 && wiOfWeek5 < r.weeks.length) {
    const r5 = TL.weekScope(r.papers, r.weeks, wiOfWeek5, now);
    check(r5.lastClosed && r5.lastClosed.id === "cos",
      "picking week 5's own chip (Temperature, still open) surfaces " +
      "Changes of State as the last CLOSED set — got " +
      (r5.lastClosed ? r5.lastClosed.id : null) +
      " (this is the live defect: it used to read 'Nothing to reteach yet')");
  }
  check(wiOfWeek4 >= 0 && wiOfWeek4 < r.weeks.length,
    "week 4's own chip (wi=" + wiOfWeek4 + ") exists on the bar at the Wed clock");
  if (wiOfWeek4 >= 0 && wiOfWeek4 < r.weeks.length) {
    // ⊕ Corrected per Mide's own ruling (commander relay, 4 Oct 2026) — the
    // cutoff is LITERAL, no grace day. Changes of State is due 28 Sep
    // 09:00 BST, which is AFTER week 4's own end (the following Monday,
    // 28 Sep 00:00 BST): it has not closed BY week 4, so week 4's own chip
    // reads "Nothing to reteach yet". This is item 1 of the bug report —
    // "week 4 reteach showed week 4's own set" — and this IS the defect,
    // not a fact to preserve. An earlier version of this check asserted
    // the opposite from a misreading of that exact line.
    const r4 = TL.weekScope(r.papers, r.weeks, wiOfWeek4, now);
    check(r4.lastClosed === null,
      "picking week 4's own chip (Changes of State due 09:00 BST THE " +
      "MORNING AFTER week 4 ends) resolves to null — \"Nothing to " +
      "reteach yet\", not its own set — got " +
      (r4.lastClosed ? r4.lastClosed.id : null));
  }
})();

// A clock before either set exists at all: nothing to reteach.
(function () {
  const now = ldn(2026, 9, 1, 9, 0).getTime();
  const r = scopeOf(TENH, 0, now);
  check(r.scope.lastClosed === null,
    "before either set has even been released, lastClosed is null " +
    "(\"Nothing to reteach yet\") — got " +
    (r.scope.lastClosed ? r.scope.lastClosed.id : null));
})();

// ─── 8r/Sc1 — flashcards never shadow an MCQ, and the oldest bucket ────
const SC1 = [
  { id: "auto1", title: "Week 1 auto set", source: "auto", academic_week: 1,
    release_at: null, due_at: "2026-09-03T17:00:00.000Z", kind: "mcq_set" },
  { id: "t1", title: "Teacher set A", source: "teacher",
    release_at: "2026-09-08T18:42:00.000Z", due_at: "2026-09-15T17:00:00.000Z", kind: "mcq_set" },
  { id: "t2", title: "Teacher set B", source: "teacher",
    release_at: "2026-09-08T18:42:00.000Z", due_at: "2026-09-15T17:00:00.000Z", kind: "mcq_set" },
  { id: "t3", title: "Teacher set C", source: "teacher",
    release_at: "2026-09-08T18:42:00.000Z", due_at: "2026-09-16T06:00:00.000Z", kind: "mcq_set" },
  { id: "fc1", title: "Flashcards — due with the MCQ", source: "teacher",
    release_at: "2026-09-28T00:00:00.000Z", due_at: "2026-10-05T00:00:00.000Z",
    kind: "flashcards" },
  { id: "mcq1", title: "MCQ — due Mon 5 Oct", source: "teacher",
    release_at: "2026-09-28T17:21:00.000Z", due_at: "2026-10-05T17:00:00.000Z",
    kind: "mcq_set" },
  { id: "fc2", title: "Flashcards — due Fri 9 Oct", source: "teacher",
    release_at: "2026-09-28T00:00:00.000Z", due_at: "2026-10-09T17:00:00.000Z",
    kind: "flashcards" },
  { id: "fc3", title: "Flashcards — due Sat 10 Oct", source: "teacher",
    release_at: "2026-09-28T00:00:00.000Z", due_at: "2026-10-10T17:00:00.000Z",
    kind: "flashcards" },
  { id: "old", title: "Old set, before term start", source: "teacher",
    release_at: "2026-08-18T09:00:00.000Z", due_at: "2026-08-25T17:00:00.000Z",
    kind: "mcq_set" }
];

(function () {
  // Tue 6 Oct 2026 12:00 BST — the Sep sets and the Oct-5 MCQ have all
  // closed (18:00 BST Monday is behind us); the Oct-5 flashcard set closed
  // at the SAME due instant but must not be picked; the Oct 9/10 flashcard
  // sets and the old August set have not and never will outrank it.
  const now = ldn(2026, 10, 6, 12, 0).getTime();
  const r = scopeOf(SC1, 0, now);
  check(r.scope.lastClosed && r.scope.lastClosed.id === "mcq1",
    "8r/Sc1 at Tue 6 Oct: lastClosed is the MCQ due Mon 5 Oct, not the " +
    "flashcard set that closed at the same instant — got " +
    (r.scope.lastClosed ? r.scope.lastClosed.id : null));
})();

(function () {
  // A clock between the Sep-15/16 sets closing and the Oct work existing
  // at all: the week-1 auto set is still the newest closed thing, every
  // Sep teacher set outranks it by due date, so this also proves ordering
  // across THREE same-day-released papers with two different due dates.
  const now = ldn(2026, 9, 20, 12, 0).getTime();
  const r = scopeOf(SC1, 0, now);
  check(r.scope.lastClosed && r.scope.lastClosed.id === "t3",
    "8r/Sc1 at 20 Sep: lastClosed is 'Teacher set C' (due 16 Sep, the " +
    "latest of the three Sep releases) — got " +
    (r.scope.lastClosed ? r.scope.lastClosed.id : null));
})();

(function () {
  // The pre-term-start set must land in the OLDEST chip's bucket, not
  // vanish and not duplicate into a chip of its own — the same "two end
  // chips are buckets" rule `wPapers` has always applied.
  const now = ldn(2026, 10, 6, 12, 0).getTime();
  const r = scopeOf(SC1, 0, now);
  const oldestWi = r.weeks.length - 1;
  const oldest = TL.weekScope(r.papers, r.weeks, oldestWi, now);
  const ids = oldest.papers.map(function (p) { return p.id; });
  check(ids.indexOf("old") >= 0,
    "the pre-term-start set lands in the oldest chip's bucket (wi=" +
    oldestWi + ") — bucket holds [" + ids.join(", ") + "]");
})();

(function () {
  // Flashcards still bucket normally (`closed`/`live`/`scheduled` are not
  // kind-filtered) even though they can never be `lastClosed`. `fc1` has no
  // `academic_week`, so (like `mcq1`, due the same day) it buckets by its
  // own due_at-7 derivation rather than into chip 0 — found its own weekIdx
  // first, same as a real caller would via `wPapers`.
  const now = ldn(2026, 10, 6, 12, 0).getTime();
  const r = scopeOf(SC1, 0, now);
  const fc1 = r.papers.filter(function (p) { return p.id === "fc1"; })[0];
  const topWeek = r.weeks[0].weekOfYear;
  const wiOfFc1 = topWeek - fc1.weekOfYear;
  const there = TL.weekScope(r.papers, r.weeks, wiOfFc1, now);
  const closedIds = there.closed.map(function (p) { return p.id; });
  check(closedIds.indexOf("fc1") >= 0,
    "a closed flashcard set still appears in its own week's `closed` " +
    "(wi=" + wiOfFc1 + ") — it is only `lastClosed` that excludes it " +
    "— got [" + closedIds.join(", ") + "]");
})();

// ─── a fixture-shaped week object, lacking `started`/`endMs` ───────────
(function () {
  const now = CLOCKS.sun.getTime();
  const bareWeeks = [{ idx: 0, weekOfYear: 1, term: "Autumn", label: "This week",
    range: "04/10/26", now: true, monYmd: "2026-10-05", friYmd: "2026-10-09" }];
  const papers = TL.buildPapers({ members: [], assignments: TENH }, now);
  papers.forEach(function (p) { p.weekIdx = 0; });   // force both into chip 0
  const r = TL.weekScope(papers, bareWeeks, 0, now);
  check(r.started === true,
    "a week object with no `started` key reads as started=true (old " +
    "fixtures keep their green behaviour) — got " + r.started);
  check(r.weekEndMs === null,
    "a week object with no `endMs` key reads as unbounded — got " + r.weekEndMs);
  check(r.lastClosed && r.lastClosed.id === "cos",
    "and the cutoff is simply `now`, same as before this ruling — got " +
    (r.lastClosed ? r.lastClosed.id : null));
})();

console.log("\n" + passes + " passed, " + fails + " failed");
process.exit(fails ? 1 : 0);
