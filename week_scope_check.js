#!/usr/bin/env node
/* week_scope_check.js — the class screen's week rule, checked in Node.
 *
 *   node week_scope_check.js
 *
 * ⊕ Mide, 4 Oct 2026 (21:56): EVERY WEEK SHOWS ONLY ITS OWN HOMEWORK.
 * Nothing from any other week, ever, on any card. This drives
 * `shared/teacher-live.js`'s `weekScope` (and the pipeline that feeds it —
 * `buildPapers`, `assignPaperWeeks`, `buildWeeks`) directly, no browser and
 * no network, at fixed clocks, against data shaped like 10h/Ph1 and 8r/Sc1.
 *
 * WHAT IT PROVES
 *   · THE INVARIANT: on every chip, at every clock, `reteach` is either null
 *     or one of THAT chip's own sets (`scope.papers`). It is checked for
 *     every chip of every class at every clock, so a version that reaches
 *     into another week — the "most recent closed set" rule live on the
 *     evening of 4 Oct, which put week 4's Changes of State on weeks 5 and
 *     6 — fails here.
 *   · 10h/Ph1 at the moment Mide looked (Sun 4 Oct 21:56): week 4 →
 *     Changes of State, week 5 → Temperature (still open, 9 in — reteach
 *     does not wait for the deadline), week 6 → nothing.
 *   · a week whose own set has no hand-ins yet has NO reteach — it does not
 *     borrow another week's.
 *   · a flashcard deck is never the reteach set.
 *   · `started` is false only on a Sunday before the week it names begins.
 *   · the bucket rule is the homework card's own (the pre-term set lands in
 *     the oldest chip).
 */
"use strict";

process.env.TZ = "Europe/London";

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

function ldn(y, mo, d, h, mi) { return new Date(y, mo - 1, d, h || 0, mi || 0, 0); }

const YEAR = { start_date: "2026-09-01", end_date: "2027-08-31" };

/* `subs` maps an assignment id to how many pupils have handed it in — the
   `colSub` column `weekScope` reads off the class matrix. */
function world(assignments, subs, now) {
  const pack = { members: [], assignments: assignments };
  const papers = TL.buildPapers(pack, now);
  const weeks = TL.buildWeeks(YEAR, now);
  TL.assignPaperWeeks(papers, weeks, YEAR, now);
  const colSub = [];
  papers.forEach(function (p) { colSub[p.idx] = (subs && subs[p.id]) || 0; });
  return { papers: papers, weeks: weeks, mx: { colSub: colSub } };
}
function scopeAt(w, wi, now) { return TL.weekScope(w.papers, w.weeks, wi, now, w.mx); }
function chipOfMonday(w, ymd) {
  for (let i = 0; i < w.weeks.length; i += 1) { if (w.weeks[i].monYmd === ymd) { return i; } }
  return -1;
}
function idOf(p) { return p ? p.id : (p === undefined ? "MISSING" : null); }

/* THE INVARIANT, for every chip of a world at a clock. */
function everyChipOwnOnly(label, w, now) {
  for (let wi = 0; wi < w.weeks.length; wi += 1) {
    const s = scopeAt(w, wi, now);
    if (s.reteach === undefined) {
      check(false, label + " chip " + wi + ": weekScope gives no `reteach` — this is the " +
        "deleted \"most recent closed set\" version");
      continue;
    }
    const own = s.papers.map(function (p) { return p.id; });
    check(s.reteach === null || own.indexOf(s.reteach.id) > -1,
      label + " chip " + wi + " (" + w.weeks[wi].monYmd + "): reteach '" +
      idOf(s.reteach) + "' is not one of this week's own sets [" + own.join(", ") + "]");
    check(s.reteach === null || s.reteach.kind !== "flashcards",
      label + " chip " + wi + ": a flashcard deck is never the reteach set");
  }
}

// ─── 10h/Ph1 — production's two live sets ──────────────────────────────
const COS = {
  id: "cos", title: "Particle Model of Matter · Changes of State",
  source: "teacher", academic_week: 4,
  release_at: "2026-09-20T11:39:49.602Z",
  due_at: "2026-09-28T08:00:00.000Z", kind: "mcq_set"
};
const TEMP = {
  id: "temp", title: "Particle Model of Matter · Temperature Changes and Specific Heat Capacity",
  source: "teacher", academic_week: 5,
  release_at: "2026-09-28T14:45:17.074Z",
  due_at: "2026-10-05T17:00:00.000Z", kind: "mcq_set"
};
const TENH = [COS, TEMP];
const TENH_SUBS = { cos: 8, temp: 9 };

const CLOCKS = {
  sun0104: ldn(2026, 10, 4, 1, 4),
  sun2156: ldn(2026, 10, 4, 21, 56),   // the moment Mide reported the defect
  wed: ldn(2026, 9, 30, 12, 0),
  mon: ldn(2026, 10, 5, 12, 0),
  tue: ldn(2026, 10, 6, 12, 0)
};

console.log("10h/Ph1 — every chip shows only its own week:");
Object.keys(CLOCKS).forEach(function (key) {
  const now = CLOCKS[key].getTime();
  const w = world(TENH, TENH_SUBS, now);
  everyChipOwnOnly("10h/Ph1 @" + key, w, now);
  const c4 = chipOfMonday(w, "2026-09-21"), c5 = chipOfMonday(w, "2026-09-28");
  check(idOf(scopeAt(w, c4, now).reteach) === "cos",
    key + ": week 4 reteach is its own Changes of State (got " + idOf(scopeAt(w, c4, now).reteach) + ")");
  check(idOf(scopeAt(w, c5, now).reteach) === "temp",
    key + ": week 5 reteach is its own Temperature set, open or not (got " +
    idOf(scopeAt(w, c5, now).reteach) + ")");
  const c6 = chipOfMonday(w, "2026-10-05");
  if (c6 > -1) {
    const s6 = scopeAt(w, c6, now);
    check(s6.papers.length === 0 && s6.reteach === null,
      key + ": week 6 has nothing set and no reteach (got " + idOf(s6.reteach) +
      ", " + s6.papers.length + " set(s))");
  }
});

(function () {
  const now = CLOCKS.sun2156.getTime();
  const w = world(TENH, TENH_SUBS, now);
  const s0 = scopeAt(w, 0, now);
  check(s0.started === false, "Sun 21:56: week 6 has not started (got " + s0.started + ")");
  const mon = CLOCKS.mon.getTime();
  check(scopeAt(world(TENH, TENH_SUBS, mon), 0, mon).started === true,
    "Mon 5 Oct 12:00: week 6 has started");
})();

// A week whose own set has nobody in yet does NOT borrow another week's.
(function () {
  const now = CLOCKS.wed.getTime();
  const w = world(TENH, { cos: 8, temp: 0 }, now);
  const c5 = chipOfMonday(w, "2026-09-28");
  const s5 = scopeAt(w, c5, now);
  check(s5.papers.length === 1 && s5.reteach === null,
    "week 5 with Temperature set but nobody in: reteach is null, never Changes of State (got " +
    idOf(s5.reteach) + ")");
})();

// ─── 8r/Sc1 — several sets in a week, flashcards, the oldest bucket ────
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
  { id: "old", title: "Old set, before term start", source: "teacher",
    release_at: "2026-08-18T09:00:00.000Z", due_at: "2026-08-25T17:00:00.000Z",
    kind: "mcq_set" }
];
const SC1_SUBS = { auto1: 2, t1: 1, t2: 1, t3: 1, fc1: 2, mcq1: 2, fc2: 1, old: 0 };

console.log("8r/Sc1 — several sets a week, flashcards, the oldest chip:");
Object.keys(CLOCKS).forEach(function (key) {
  const now = CLOCKS[key].getTime();
  const w = world(SC1, SC1_SUBS, now);
  everyChipOwnOnly("8r/Sc1 @" + key, w, now);
});
(function () {
  const now = CLOCKS.sun2156.getTime();
  const w = world(SC1, SC1_SUBS, now);
  const c5 = chipOfMonday(w, "2026-09-28");
  check(idOf(scopeAt(w, c5, now).reteach) === "mcq1",
    "8r/Sc1 week 5: the MCQ, never a flashcard deck (got " + idOf(scopeAt(w, c5, now).reteach) + ")");
  const c2 = chipOfMonday(w, "2026-09-07");
  const r2 = idOf(scopeAt(w, c2, now).reteach);
  check(["t1", "t2", "t3"].indexOf(r2) > -1,
    "8r/Sc1 week 2: one of week 2's own three sets (got " + r2 + ")");
  const oldest = w.weeks.length - 1;
  const so = scopeAt(w, oldest, now);
  check(so.papers.some(function (p) { return p.id === "old"; }),
    "8r/Sc1: the pre-term set lands in the oldest chip's bucket");
  check(idOf(so.reteach) === "auto1",
    "8r/Sc1 oldest chip: the auto set (the pre-term set has nobody in) (got " + idOf(so.reteach) + ")");
})();

// ─── a class with exactly one set, nobody in ───────────────────────────
(function () {
  const ONE = [{ id: "one", title: "The only set", source: "teacher", academic_week: 3,
    release_at: "2026-09-14T07:00:00.000Z", due_at: "2026-09-22T17:00:00.000Z", kind: "mcq_set" }];
  const now = CLOCKS.sun2156.getTime();
  const w = world(ONE, { one: 0 }, now);
  everyChipOwnOnly("one-set class", w, now);
  for (let wi = 0; wi < w.weeks.length; wi += 1) {
    check(scopeAt(w, wi, now).reteach === null,
      "one-set class chip " + wi + ": nobody in, so no reteach anywhere");
  }
})();

console.log((fails ? "FAIL" : "PASS") + " — " + passes + " passed, " + fails + " failed");
console.log(passes + " passed, " + fails + " failed");
process.exit(fails ? 1 : 0);
