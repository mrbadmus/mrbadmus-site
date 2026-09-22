# MRB-348 round three — the teacher screens come off the unbounded read

22 September 2026. Rehearsed on **TEST** (`qeppkiswvclkkwbxmlok`, ref proven
out of the service-role JWT's own `ref` claim, never read off a label).
**Nothing was applied to production.**

> ## ⚠️ THE PRODUCTION MIGRATION IS A DEPENDENCY, NOT A DETAIL
>
> `supabase/migrations/20260922231500_mrb348_teacher_class_rollup.sql`
> **must be applied to production before, or in the same release as, the
> frontend push.** It creates `public.teacher_class_rollup` and drops
> `public.teacher_class_summaries`.
>
> The page has a fallback — if the function is missing the rollup call throws,
> the browser catches it and re-reads every submission exactly as it does
> today. So the ordering cannot break a teacher's screen. **That is what makes
> the ordering non-fatal; it is not a licence to skip the migration.** An
> estate running on the fallback is paying the full cost this ticket exists to
> remove, on every teacher screen, silently, with only a `console.warn` saying
> so.
>
> Round two's migration `20260922114500` has also never been applied to
> production. Apply both, in order; this one's `DROP ... IF EXISTS` is a no-op
> on a database that never took the first.

---

## 1. What was wrong, and what round two left

`loadClassMatrices()` in `shared/teacher-data.js` is the universal read behind
all six generated teacher screens. Stage B fetches **every submission of every
assignment of every class the viewer touches** — no limit, no window — and
`buildMatrix()` in `shared/teacher-live.js` counts them in the browser. 129
rows on the realistic TEST teacher today; about **6,000** at an ordinary
December, on every screen, to draw cards that show six numbers each.

Round two put `public.teacher_class_summaries(uuid[])` in the database and
proved it exact. It then **could not switch it on**, and
`docs/mrb348/teacher-aggregate.md` §6 says precisely why: six numbers do not
draw a screen. All six pages share ONE compiled `renderVals` that also
computes, unconditionally and for **every** class:

| value | where it is drawn |
|---|---|
| `week[0]` / `week[1]` | every class card: "4 of 6 in" |
| `colSub` `colAsked` `colMean` `colOnTime` `colLate` `colLateUnknown` | the digest's tiles and its per-paper class report |
| `markedSub` `markedOnTime` `markedLate` `markedLateUnknown` `markedPct` | `dgMarkedSub` / `dgOnTime` / `dgLate` / `dgUnknown` |
| `classMean` | the card's mean, `dgMeans`, `digestRows` |
| `roster[].avg` | the search pool, on every screen, across every class |
| `roster[].inWeek` | the card's "Chase Amy, Ben +3 more" |
| `roster[].flag` | `digestRows.flagN`, the chase list |
| `roster[].lastIso` | the card's "Last activity 2 days ago" |

Ship the six alone and every one of those degrades to 0 / null /
"No activity yet".

**So the aggregate had to grow to the shape the RENDER needs.** The cost of
the old read is a PRODUCT — pupils × papers. What the screens read off it is
two SUMS: a number per paper and a number per pupil. Round three returns the
two sums.

---

## 2. `public.teacher_class_rollup(uuid[], timestamptz, jsonb)`

Migration: `supabase/migrations/20260922231500_mrb348_teacher_class_rollup.sql`
(full reasoning in that file's header). One row per class the caller may see:

| column | contents |
|---|---|
| `summary` | the six numbers round two returned, unchanged and by the same rules |
| `papers` | one object per ASSIGNMENT — `sub`, `off_roster`, `on_time`, `late`, `unknown`, `marked_n`, `mean` |
| `students` | one object per ACTIVE MEMBER — `in_week`, `last_at`, `avg`, `missing_marked` |

It **supersedes and DROPS** `teacher_class_summaries`. Its six numbers are
reproduced here verbatim, so keeping both would mean two SQL implementations
of one locked rule that must agree for ever, on top of the JavaScript they
must both agree with — the exact drift that function's own header warns about.
Nothing calls it and it was never on production.

### Why each predicate is what it is

**Three predicates that are easy to conflate and are NOT the same** — round
two established them and they are unchanged:

1. **`submissions_completed`** — the class card's count, from
   `deriveClassMetrics` — is `submitted_at IS NOT NULL`. Nothing else.
2. **A CELL** — what every column and every pupil row is built from,
   `cellOf()` — exists when `completed_at IS NOT NULL OR submitted_at IS NOT
   NULL OR status = 'complete'`, and is GRADED (so counts toward a mean) only
   when `score IS NOT NULL AND max_score IS NOT NULL AND max_score > 0`. A row
   with `completed_at` and no `submitted_at` is a cell and is **not** in (1).
   A submitted-but-ungraded row is in (1), is a cell, and is in no mean.
3. **`marked`** means only *"the deadline has passed"* — `buildPapers`'
   `open = !due_at || due_at > now`. Not released, not sat, not graded. An
   assignment with no `due_at` never closes and is never marked.

**Lateness is a tri-state and the third state is the point.** `cellOf` takes
the stamp first (`is_late`, as written at completion), the comparison second
(`COALESCE(completed_at, submitted_at) > due_at`), and UNKNOWN third —
`is_late` was added on 22 Aug 2026 and nothing was backfilled, so every older
row carries NULL, and a submission with no stamp or an assignment with no
deadline cannot be judged either way. `on_time`, `late` and `unknown` come
back as three separate counts so a caller cannot quietly absorb the third into
either of the others, which is what `MRB_ONTIME_SUB` on the page is about.

**`asked` is not returned; `off_roster` is.** The page's `colAsked` is the
active roster plus anyone off it who sat THAT paper — the 24 Aug 2026 ruling
that stopped a column reading "31 of 29". The aggregate returns only the
second half, so the roster keeps being defined in exactly one place.

**`missing_marked`, not "no mark".** `mx.markedIdx.some(i =>
!row.submitted[i])` — a marked paper this pupil has no CELL for. An ungraded
submission is submitted.

**The rounding.** `round(((a::float8 / b::float8) * 100)::numeric)` — the same
IEEE double division JavaScript does, then half-away-from-zero, which equals
`Math.round` for non-negative values. Rounding the float8 directly would use
Postgres's banker's rounding and disagree on every exact `.5`; doing the
division in `numeric` would disagree wherever the double lands a hair under a
`.5`. Two exact `.5` boundaries are asserted in §3c.

**The first-attempt rule (MRB-38)** is reproduced exactly as round two wrote
it: `COALESCE(attempts, 2147483647) ASC`, `COALESCE(submitted_at, 'infinity')
ASC`, `s.id ASC` as a deterministic tiebreak for a full tie neither side
defines.

### ⚠️ The clock and the week window are the CALLER's, on purpose

`p_now` and `p_windows` exist because the page's definitions of "now" and
"this teaching week" are the BROWSER's, and this function's job is to
reproduce what that browser would have computed.

- **`p_now`** — `buildPapers` decides `marked` against one `Date.now()` taken
  in `base()`. A server `now()` a few hundred milliseconds later can flip an
  assignment whose deadline falls in that gap, and two halves of one screen
  would disagree by a paper.
- **`p_windows`** — `computeWeekWindow()` is browser-LOCAL, anchored on the
  CLASS's own day, and carries MRB-330's Sunday rule. **Four implementations
  of the teaching week already have to agree (CLAUDE.md); a fifth, in SQL,
  would be the fifth.** So the window is passed in.

⚠️ **Neither parameter is a trust boundary.** Both only re-bucket rows the
caller's own RLS already grants; a caller who lies about the clock changes
their own arithmetic and sees nothing new. The gate takes no parameters at
all.

### ⚠️ One boundary is deliberately half-open the "wrong" way

`buildMatrix` tests `p.due_at >= week.start_at && p.due_at < week.end_at` as
**strings**: `due_at` arrives from PostgREST as `…T23:00:00+00:00` and the
window from `Date.toISOString()` as `…T23:00:00.000Z`. Lexicographic order is
chronological order for those two forms everywhere EXCEPT an exact tie to the
second, where `'+'` (0x2B) sorts before `'.'` (0x2E) — so a deadline landing
exactly ON the window's start is EXCLUDED by the page and one landing exactly
on its end is INCLUDED. A Monday-anchored class's window starts at local
midnight, which is exactly where a round `due_at` falls, so this is a real
boundary. The SQL therefore reads `due_at > start AND due_at <= end`. It looks
like a typo and it is the only thing that reproduces the browser.

### Security

`SECURITY DEFINER`, `SET search_path TO 'public'`, `SET "TimeZone" TO 'UTC'`,
gated as the first statement, in the shape `class_teachers_for_viewer` and
`class_stars_leaderboard_for_member` both use. An unreadable class id is
**dropped silently**, not raised — a rollup is asked speculatively over a
remembered id list and one stale id must not take a page down.
(`loadClassMatrices` still THROWS: it is a page's authorisation check.)

The gate is not one predicate, because the four tables' RLS is not one
predicate: a plain HoD sees every class in the school and every member of it,
but only their own department's assignments — and therefore only their own
department's submissions. `all_work` is exactly that distinction, and the
`hz_rich` row of §3a is what exercises it.

---

## 3. Proof — the same method as round two (§3 there)

A Python replay of `loadClassMatrices`'s exact PostgREST reads, signed in as a
real user under real RLS **with the anon key**, with `pickFirstAttempts`,
`buildPapers`, `cellOf`, `buildMatrix`, `buildRoster` and `buildClassEntry`
translated line for line — including their string comparisons on timestamps;
then the RPC, as the same user, in the same instant, with the same clock and
windows; then a cell-by-cell diff.

`mrb348_teacher_rollup_proof.py`. The service-role key is used for nothing but
building and tearing down the fixture in §3c.

### 3a. Every class, every reader

| reader | asked | the read sees | the rollup returns | rows the read fetched | values compared | mismatches |
|---|---|---|---|---|---|---|
| `mide.badmus@test-rainford.local` (teacher, 5 classes) | 12 | 5 | 5 | 129 | 374 | **0** |
| `hz_amy@test.mrbadmus` (teacher, 1 class) | 12 | 1 | 1 | 6 | 42 | **0** |
| `hz_rich@test.mrbadmus` (**HoD**, whole school) | 12 | 11 | 11 | 175 | 592 | **0** |

**1008 of 1008 values identical**, and the visibility sets matched exactly —
including the twelfth class, which is in another school and which neither path
returned to anybody.

⚠️ The HoD row is the one that matters most. `hz_rich` sees eleven classes and
every member of them, but RLS narrows their ASSIGNMENTS to their own
department — so for most of those eleven the two sides had to agree not only
on arithmetic but on a NARROWER SET OF PAPERS, class by class. They did.

### 3b. What is compared, per class

Fifteen whole-class values, three cross-checks, seven values per PAPER and
four per PUPIL:

| | |
|---|---|
| whole class | `student_count` `assignment_count` `submission_count` `completion_pct` `last_activity_at` `classMean` `markedSub` `markedOnTime` `markedLate` `markedLateUnknown` `markedPct` `week[0]` `week[1]` `lastIso` `flagged` |
| cross-checks | SQL's own `class_mean` against the page's mean-of-marked-column-means; SQL's `active_member_count` and `assignment_count` against the page's counts |
| per paper | `sub` `asked` `mean` `on_time` `late` `unknown` `marked_n` |
| per pupil | `avg` `in_week` `last_at` `missing_marked` |

`week[0]`, `lastIso` and `flagged` are derived from the pupil rows by the same
JavaScript on both sides — they are in the table because a wrong INPUT shows
up there first, in the value a teacher actually reads on a card.

⚠️ Timestamps are compared as INSTANTS, not strings. PostgREST and `jsonb`
agree on the format today; a format difference must not be readable as a value
difference, and a value difference must not be hideable by one.

### 3c. The adversarial fixture — three ways

`mrb348_teacher_rollup_proof.py --fixture`. Built on TEST class `…0004`
(8X2 — 3 members, one pre-existing marked paper nobody sat, Monday anchor),
exercised through both paths, then **torn down by a snapshotted id list, never
a predicate** (CLAUDE.md: a predicate wipe once killed four real rows, and
`delete where title like 'mrb348%'` is exactly that shape). The class was
confirmed back at its baseline afterwards — 1 assignment, 3 members, 0 fixture
rows left behind.

Three assignments and nine submission rows, aimed at what round two's fixture
did NOT cover, because round two already proved the six summary numbers:

1. a paper due **inside the current teaching week and still open** — `week[0]`
2. **two off-roster pupils** — in the column's `asked`, not in the roster
3. `is_late` **TRUE**, **FALSE**, **NULL with a stamp after the deadline**
   (late by comparison), **NULL with a stamp before it** (on time by
   comparison) and **NULL with no stamp at all** (unknown) — every one of the
   five ways `cellOf` can decide lateness
4. a **retake with a better mark** at `attempts = 2` — the first attempt wins
5. an **in-progress row**, no stamp, not complete — **no cell at all**
6. `completed_at` with **no `submitted_at`** — a cell, and NOT a submission
   "handed in" for the card's count
7. a marked paper **nobody sat** (the class's own pre-existing one) — so
   `missing_marked` is true for every pupil and the flag then turns on
   `inWeek` alone, which is exactly Design's rule
8. sums chosen to land **two exact `.5` boundaries** — a column mean of
   19/40 = **47.5** and a pupil average of 3/8 = **37.5**

| value | by hand | JS | SQL |
|---|---|---|---|
| `student_count` | 3 | 3 | 3 |
| `assignment_count` | 4 | 4 | 4 |
| `submission_count` | 5 | 5 | 5 |
| `completion_pct` | 42 | 42 | 42 |
| `markedSub` | 5 | 5 | 5 |
| `markedOnTime` | 2 | 2 | 2 |
| `markedLate` | 2 | 2 | 2 |
| `markedLateUnknown` | 1 | 1 | 1 |
| `markedPct` | 50 | 50 | 50 |
| `classMean` | **48** | 48 | 48 |
| `week[0]` / `week[1]` | 1 / 3 | 1 / 3 | 1 / 3 |
| `flagged` | 2 | 2 | 2 |
| marked column `sub` / `asked` | 5 / 5 | 5 / 5 | 5 / 5 |
| marked column `on_time` / `late` / `unknown` | 2 / 2 / 1 | same | same |
| marked column `marked_n` / `mean` | 5 / **48** | same | same |
| pupil A `avg` / `in_week` / `missing_marked` | 63 / false / true | same | same |
| pupil B `avg` / `in_week` / `missing_marked` | **38** / true / true | same | same |
| pupil C `avg` / `in_week` / `missing_marked` | 25 / false / true | same | same |

**87 values, three ways, 0 mismatches.** `19/40 = 47.5 → 48` and
`3/8 = 37.5 → 38` are the rounding boundaries: Postgres's own `round()` on a
float8 would give 48 and 38 by luck in one direction and banker's rounding in
the other, which is why the expression casts to `numeric` only after the
double division.

⚠️ **The fixture caught one of MY errors, not the code's.** The first draft
gave the in-week paper a deadline of `window start + 1 day`, which on any day
but Monday has already passed — so the paper was in this week AND marked, and
walked into every marked-paper total. JS and SQL agreed with each other
perfectly and both disagreed with my arithmetic. That is the shape of evidence
a two-way comparison cannot give you and is the whole reason the by-hand
column exists.

---

## 4. The rendered-output diff

<!-- DIFF -->

---

## 5. Rows fetched, per screen

Measured, not projected, by `mrb348_teacher_rollup_proof.py --rows` on the
realistic TEST teacher (`mide.badmus@test-rainford.local`, 5 classes, 22
member rows, 28 assignments, 79 submissions). Same basis round two's §4 used:
the rows the three `loadClassMatrices` reads return, plus one rollup row per
class whose submissions are no longer fetched.

Per class: `…0001` 5 members / 5 assignments / 15 submissions ·
`…0002` 6 / 18 / 47 · `…0003` 5 / 4 / 17 · `…0004` 3 / 1 / 0 ·
`…0005` 3 / 0 / 0.

| screen | before | after | saving |
|---|---|---|---|
| `classes.html` | 129 | **55 + 5 rollup rows** | −74 submission rows |
| `digest.html` | 129 | **55 + 5** | −74 |
| `insights.html` | 129 | **55 + 5** | −74 |
| `class-detail.html?class=…0002` (busiest) | 129 | 97 + 4 | −28 |
| `class-detail.html?class=…0004` (quietest) | 129 | 50 + 4 | −75 |
| `assignment.html` (one paper of `…0002`) | 129 | 97 + 4 | −28 |
| `student-detail.html` (`…0002`) | 129 | 97 + 4 | −28 |
| `class-detail.html` with **no** `?class=` | 129 | 129 | **0 — by design** |

⚠️ **`insights.html` moved, and round two said it could not.** Round two's
table has insights at "129 → 129, genuinely the broadest". That was true of
the SUMMARY aggregate, which could not supply the per-paper columns the charts
read. It is not true of the rollup: the question grids the insights charts
draw come from `loadPaperQuestions`, a separate read this ticket does not
touch, and everything else on that screen is columns and pupil rows.

⚠️ **The last row is the honest one.** `load()` resolves a missing `?class=`
to the first class by code order AFTER `base()` has already run, so the id is
not knowable when the scope is decided. Guessing it would risk fetching the
wrong class's cells and drawing an empty grid on a real class, so that one
case keeps today's full read. Every link the product generates carries
`?class=`.

**Projected at a December load** (5 classes × 40 assignments × 30 pupils, the
same projection round two used): about **6,000** submission rows on every
screen today, against **150 member rows + 200 assignment rows + 5 rollup
rows** on the three summary screens — and about a fifth of the submissions on
a single-class screen. The cost stops being a product and becomes a sum.

---

## 6. The production RUM baseline

Read **read-only** from production (`urklkrwevjtlfbwnipjn`, named explicitly
on the call) so that the after-figure is comparable once this ships.

| page | samples | p50 | p75 | mean |
|---|---|---|---|---|
| `teacher-classes` | 101 | **639 ms** | 1860 | 1718 |
| `teacher-class-detail` | 51 | **1502 ms** | 3619 | 2316 |
| `teacher-assignment` | 7 | 1882 ms | 3156 | 2211 |
| `teacher-digest` | 2 | 1476 ms | 1773 | 1476 |
| `teacher-insights` | 1 | 632 ms | 632 | 632 |
| `teacher-student` | 5 | 604 ms | 1048 | 1196 |
| `teacher-today` | 48 | 1194 ms | 1967 | 1658 |
| (`student-class`, for scale) | 26 | 2556 ms | 3745 | 3899 |

⚠️ **THE AFTER-NUMBER CAN ONLY COME FROM RUM AFTER DEPLOY.** Nothing measured
on TEST is a production saving and none of the TEST figures in this report are
offered as one.

⚠️ **AND TODAY'S RUM CANNOT SHOW THIS DEFECT EITHER.** The per-resource
breakdown production has recorded so far, across every teacher page:

| resource | samples | p50 |
|---|---|---|
| `academic_years` | 41 | 862 ms |
| `profiles` | 213 | 382 ms |
| `class_teachers` | 197 | 303 ms |
| `class_members` | 167 | 271 ms |
| `assignments` | 167 | 171 ms |
| **`assignment_submissions`** | **125** | **101 ms** |

The read this ticket removes is currently the CHEAPEST thing on the page,
because the school is three weeks into an academic year and the product of
pupils and papers is still small. It grows with the term and nothing else in
that table does. So the honest claim is not "this makes teacher pages fast
today" — it is **"this stops them getting slow in December"**, and the number
that will show it is `assignment_submissions`' p50 and the `teacher-*` p75s in
`rum_timings` after the estate has a term's work in it.

---

## 7. Gates

<!-- GATES -->

---

## 8. Deviations

<!-- DEVIATIONS -->
