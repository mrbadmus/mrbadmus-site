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

### The checked-in file IS what was proven

The function was applied to TEST through the Supabase connector with an
explicit `project_id`, and the connector takes the SQL inline — so the
executable text and the file could in principle drift, and everything below
would then be a proof about something that is not in the repo. They do not:
with SQL comments stripped and whitespace collapsed, the file's body and
`pg_proc.prosrc` on TEST are the same 6,521 characters and the same md5
`6ebd8c32b1dd96b5dd6d6ef0af31eb27`. `teacher_class_summaries` is gone from
TEST's catalogue (`count = 0`).

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

§6 of round two's write-up is explicit that which values reach the DOM is a
property of Design's compiled template **node by node**, not of the data
layer — so the only thing that establishes "nothing a teacher sees has moved"
is a diff of what actually renders. `teacher_behaviour` and `teacher_reach`
cannot do it: they drive `teacher_fixtures/*-fixture.html`, which have no
network and never load `shared/teacher-live.js` at all. Their own `watches`
lists in `gate_registry.py` say so in as many words.

So `mrb348_teacher_equiv.py` (new) signs in as real people on TEST, serves
`mrbadmus_site/` over a local static server, drives the six real pages and
compares **visible text, the control set and the address**, `--capture old`
against `--capture new`. It is EXCLUDED from the gate registry rather than
registered, for the same reason its student sibling is: a two-tree comparison
cannot run against one tree, and a gate comparing a capture against itself
would be green for ever.

**Eleven cases, two readers.** Reader A `mide.badmus@test-rainford.local`
(5 classes, 28 assignments, 79 submissions); reader B `hz_rich@test.mrbadmus`
(`staff_scopes.scope = 'hod'`, Science).

| case | url | what it is for | chars |
|---|---|---|---|
| `classes` | `classes.html` | the card grid — `week[0]`, `last`, `state`, the mean | 637 |
| `digest` | `digest.html` | the all-class tiles — `dgMarkedSub` / `dgOnTime` / `dgLate` / `dgUnknown` / `dgMeans` | 557 |
| `digest-class` | `digest.html?class=10A` | the single-class report — the per-paper columns, paper by paper | 1492 |
| `insights` | `insights.html` | the charts screen | 460 |
| `class` | `class-detail.html?class=10A` | the busiest class, in focus | 2146 |
| `class-fallback` | `class-detail.html` (no parameter) | the path that keeps the OLD full read | 1670 |
| `student` | `student-detail.html?class=10A&student=…` | 17 submissions, the richest history on the seed | 1774 |
| `marking` | `assignment.html?class=10A&paper=1` | a CLOSED paper — 3/6 in, mean 80%, the on-time split | 317 |
| `marking-grid` | `assignment.html?class=10A&paper=0` | the fifteen-question breakdown and the six-pupil grid | 742 |
| `hod-classes` | `classes.html` (reader B) | a standing that is not an ordinary teacher's | 292 |
| `hod-digest` | `digest.html` (reader B) | the same, through the digest | 397 |

### Result

**Eleven of eleven identical** — the same visible text to the character, the
same control set, the same address:

```
  ✅ every case renders the same visible text, the same controls, and the same address.
```

⚠️ **THE MARKING SCREEN NEEDED TWO CASES, and the reason is a property of the
seed.** Of 10A's eighteen assignments, every one that has submissions has ZERO
`assignment_questions` rows, and the only one with a question list (fifteen)
has zero submissions. No single paper exercises both halves of that screen, so
`marking` carries the submission aggregate and `marking-grid` carries the
question grid.

⚠️ **AND THE HARNESS HAD TO BE MADE HONEST FIRST — twice.** Both findings are
recorded in its own docstring, because both would otherwise be re-derived:

1. **Mounted is not finished.** A readiness probe that only asked whether the
   mount host had content captured THREE DIFFERENT PAGES from one URL on one
   unchanged tree — the first paint before `load()` had resolved the paper
   list, a mid state, and the finished screen. Readiness is now QUIESCENCE:
   the snapshot must come back identical eight times at 500 ms.
2. **Another session was mutating TEST mid-capture.** An assignment titled
   `mrb336muczfmg5 FOREIGN TITLE` appeared on 10A and vanished again — a
   throwaway row from a different gate's fixture. It carries no `due_at`, and
   `buildPapers` sorts `due_at DESC NULLS FIRST`, so while it existed it took
   index 0 and shifted every paper down one: `?paper=1` rendered the wrong
   paper, **stably**, for a 425-character diff that read exactly like a
   regression. Every case now carries a `require` naming the identity it is
   about (a class code, a person, a paper title — never a computed value) and
   reloads until that target is on screen.

⚠️ **What this diff does NOT prove.** `hz_rich` renders ONE class, not eleven.
He holds the `hod` scope, but `loadTeacherClasses` is deliberately
SELF-FILTERED to the viewer's own `class_teachers` rows (MRB-325 ruling 1, the
Today/My-classes leak fix), so the page never asks about the rest of the
school. The wide cross-department read is real and is proven in §3a, where the
same user was asked about all twelve class ids directly and RLS answered for
eleven — with the aggregate agreeing on every one. These two rows prove the
RENDER under a non-ordinary standing; §3a proves the READ. They answer
different questions and neither substitutes for the other.


### ⚠️ What this diff could NOT see

Stated plainly, because a diff that cannot observe a value is not evidence
about that value.

- **One viewport.** Every case was driven at the harness's default desktop
  width. It says nothing about 390 or 360 — `teacher_reach` is the gate that
  holds those, it passed, and it drives fixtures whose data is baked in, so
  neither instrument observes this change at a phone width. Nothing here is
  width-dependent (no value moved; only where it was computed), but that is an
  argument, not a measurement.
- **Two readers, not every standing.** A `school_admin` acting on a colleague's
  class (`?teacher=`), an SLT member, and an operator are not driven. §3a's
  proof covers what each may READ — the gate's arms are the same for all of
  them — but not what each RENDERS.
- **Visible text, controls and address — not pixels and not the console.**
  `innerText` of the mount host, the tag+label of every control, and
  `location.search`. A purely visual change (colour, position) or a console
  error would not fail it. `teacher_behaviour` holds the console on the
  fixtures and passed.
- **One instant.** Each capture is one moment of TEST's data. The teaching
  week did not roll and no deadline passed mid-run; a value that only differs
  at a boundary — the `>` / `<=` week edge in §2, say — is proven in §3c's
  fixture, not here.
- **It cannot see rows.** Identical output is exactly what this ticket wants,
  which means the diff is evidence of SAFETY and none at all of the saving.
  The saving is §5's row table.

---

## 4b. The fallback, proven by breaking it for real

The page must survive the case where the frontend has shipped and the
migration has not. That was checked by **renaming the function out of TEST's
catalogue** — not by editing the page, not by a stub:

```sql
ALTER FUNCTION public.teacher_class_rollup(uuid[], timestamptz, jsonb)
  RENAME TO teacher_class_rollup_mrb348_hidden;
```

With the function genuinely absent, `--capture fallback` drove the same eleven
cases. **All eleven render identically to the PRE-CHANGE tree** — the same
visible text, the same controls, the same address:

```
  comparing OLD (before MRB-348 round three) with FALLBACK
  ✅ every case renders the same visible text, the same controls, and the same address.
```

⚠️ **That result is only possible if the fallback actually fired.** Had the
catch swallowed the failure without re-reading, every class but the one in
focus would have had an empty matrix: `0 of N in`, "No activity yet", no mean,
no chase names. The diff would have been enormous. Byte-identical to the
pre-change tree is the signature of the full submissions read having happened.

**TEST was restored immediately afterwards and the restoration was verified,
not assumed**: the function is back under its own name, `pg_proc.prosrc` still
hashes to `70fc3ad5b2da5a604827a01c052c67ca`, the normalised body still
matches the checked-in migration (`6ebd8c32b1dd96b5dd6d6ef0af31eb27`), and a
search for `%mrb348_hidden%` returns **0 rows**. `--compare` (old vs new) was
then re-run and still passes, which also rules out the world having drifted
between the three captures.

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

## 5b. The waterfall — waves and critical path

`perf_waterfall.py`, four teacher journeys, five runs each, medians, on TEST
with a local static server. BEFORE is a hardlinked copy of `mrbadmus_site`
carrying `shared/teacher-{data,live}.js` from `757a7966b~1`, the last commit
before round three; AFTER is the built tree.

| journey | mount ms (before → after) | waves | hops | pre-mount requests |
|---|---|---|---|---|
| `teacher-classes` | 460 → 362 / 394 | 3 → 3 | 4 → 4 | 22 → 22 |
| `teacher-digest` | 344 → 505 / 333 | 3 → 2–3 | 3 → 3 | 20 → 19–20 |
| `teacher-insights` | 532 → 691 / 564 | 5 → 4 | 5 → 5 | 26 → 25–26 |
| `teacher-class-detail` | 584 → 710 / 659 | 7 → 6 | 7 → 7 | 38 → 38 |

**Two AFTER figures are given per journey because two identical runs of the
SAME tree differed by up to 170 ms.** At TEST's data size the mount time is
dominated by laptop and network noise, and quoting one of those numbers as a
result would be quoting the noise. **The honest reading is that the waterfall
shows NO time change on TEST beyond its own spread.**

What it does show, and what is stable across runs, is the SHAPE:

```
 BEFORE  teacher-classes   class_members → assignment_submissions → schools → rum_timings
 AFTER   teacher-classes   assignments → rpc:teacher_class_rollup → schools → rum_timings

 BEFORE  teacher-digest    assignments → assignment_submissions → rum_timings
 AFTER   teacher-digest    assignments → rpc:teacher_class_rollup → rum_timings
```

The unbounded submissions read has **left the critical path** on the three
summary journeys and been replaced by a fixed-size RPC. The request count is
unchanged — one read became one read — and `teacher-class-detail` loses a wave
(7 → 6) because its non-focused classes no longer contribute a submissions
request of their own. What changed is the number of ROWS on the wire, which is
§5's table, and a row count is not something a waterfall measures.

⚠️ **THIS IS A TEST MEASUREMENT AND IT IS NOT A PRODUCTION SAVING.** It is a
laptop, a nearby sandbox database with 79 submission rows in it, and a warm
cache. Every number in this section describes shape, not a teacher's morning.
The production figure can only come from `rum_timings` after this ships — see
§6.

⚠️ **The first BEFORE run was invalid and is not in the table above**, for a
reason worth recording: both trees serve the same asset URLs, cache-bust stamp
included, so serving them on the same port let Chrome answer the second run
out of the first run's cache. The tell was `rpc:teacher_class_rollup`
appearing in the critical path of a run that was supposed to predate it. The
before run now uses its own port and therefore its own origin and cache
(`$MRB348_PORT`, documented in `perf_waterfall.py`). ⚠️ A second trap on the
same attempt: round three landed in THREE commits, so `HEAD~1` still contains
the change — the base is the commit before the WIP one.

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

## 6b. What changed, file by file

| file | what |
|---|---|
| `supabase/migrations/20260922231500_mrb348_teacher_class_rollup.sql` | **new.** `teacher_class_rollup`; drops `teacher_class_summaries`. TEST only. |
| `shared/teacher-data.js` | `loadClassSummaries(classIds, opts)` rewritten onto the rollup, returning `{metrics, papers, students}` per class. `loadClassMatrices`'s `submissionsFor` is unchanged — round two added it and it now has callers. |
| `shared/teacher-live.js` | `finishMatrix()` (the marked totals, in ONE place), `matrixFromRollup()`, `buildRoster` honouring a partial row, `buildClassEntry(…, roll)`, the per-screen scope + the fallback in `base()`, `focus` set by `load()` **and** by the mount, and `yearOfClass` no longer fetching submissions. |
| `mrb348_teacher_rollup_proof.py` | **new.** The three-reader proof, the adversarial fixture, and `--rows`. Registered as the gate `teacher_rollup_equal`. |
| `mrb348_teacher_equiv.py` | **new.** The rendered-output diff, eleven cases. `EXCLUDED` (two-tree). |
| `perf_waterfall.py` | `$MRB348_SERVE_DIR`, so a BEFORE tree can be measured without reverting the repo. |
| `gate_registry.py` | one GATES row, one EXCLUDED row. |
| the generated pages | `?v=` cache-bust stamps only — `teacher-data.js` `2b828519 → 3fef17de`, `teacher-live.js` `b8fa3a37 → 94834e17`. No ruling and no template changed. |

⚠️ **`teacher_rulings.py` and `build_teacher_port.py` are untouched.** Every
value this ticket moves is computed in the data layer and read by Design's
compiled `renderVals` exactly as before; the six generated pages differ from
their previous build only in the two asset stamps above.

---

## 7. Gates

`prepush_gate.py --record-all`, with `$MRB_TEST_TEACHER_PASSWORD` and
`$MRB_TEST_STUDENT_PASSWORD` set. **Eleven of twelve affected slow gates PASS;
one is RED and it is the inherited one.**

| gate | result |
|---|---|
| `verify_ks3` | **PASS** |
| `today_drive` | **PASS** |
| `teacher_behaviour` | **PASS** |
| `teacher_reach` | **PASS** |
| `teacher_picker_drive` | **PASS** |
| `ks4_chrome_drive` | **PASS** |
| `assignments_hold_drive` | **PASS** |
| `consumer_flag_off` | **PASS** |
| `teacher_perf_budget` | **PASS** |
| `mrb328_card_prefetch` | **PASS** |
| `teacher_rollup_equal` (new) | **PASS** |
| `teacher_admin_foreign_class` | ❌ **RED — INHERITED** |

Every fast gate ran and passed, including `gate_watches_check` (52 gates, each
watching its own script, none watching `docs/**`) and `gate_coverage` (every
root script classified — the two new ones are `teacher_rollup_equal` in GATES
and `mrb348_teacher_equiv.py` in EXCLUDED).

### The red, in full

```
FAIL  teacher_admin_foreign_class (exit 1)
  ❌ teacher_admin_foreign_class_drive: 3 check(s) failed
     · C7. REMINDERS — the control is drawn on the foreign class
     · …labelled for the children who actually owe the paper
     · …and pressing it UPSERTS student_notifications
```

**These are the same three checks CLAUDE.md names as the standing inherited
red** ("the inherited red (`teacher_admin_foreign_class`, C7 REMINDERS × 3) is
still inherited and still red"). Its other nine checks — D4 and D5, the whole
admin-scope fallback — pass. It is about a REMINDERS control on a foreign
class, a surface round three does not touch: this ticket changes where the
class-card numbers are counted, and adds no control, removes none, and writes
nothing to `student_notifications`. **It has not been weakened, re-run until
green, or overridden.** A push would still need its `GATE-OVERRIDE:` line, the
same one it has needed since before this work started.

### Skipped, by name

Nine gates were **SKIPPED BY RULE** — nothing this branch's commits changed
falls in their `watches`, which is MRB-346's selection working as designed and
is printed rather than silently absent: `student_parity`,
`student_behaviour`, `student_themes`, `import_year_drive`,
`leaderboard_behaviour`, `ks3_instrument_liveness`, `student_switches`,
`student_controls_drive`, `seating_drive`, `mrb328_import_picker`.

Five were skipped for a **missing precondition**, each named: `set_work`,
`ks4_pool_drive` (no `$MRB_SET_WORK_PASSWORD`), `teacher_admin_real`,
`class_csv_upload`, `mrb328_import_picker_real`, `student_bell_drive` (no
`$MRB_THROWAWAY_PASSWORD`), and `3d_parity` / `3d_render_check`
(`3d-studio/dist` does not exist).

### ⚠️ `teacher_perf_budget` passed, and it could not have failed for this

It drives `hz_amy` and `hz_rich`, who hold one class each with almost no work.
It **cannot see this defect and cannot see its fix**. It is reported here to
show nothing REGRESSED, and it is not a measurement of the gain. It is also
recorded as FLAKY; it passed first time, so there was nothing to re-run.

---

## 8. Deviations

**Deviation: the brief's two-line wiring would have rendered zeroes → I
replaced the aggregate instead of calling the one that existed → because six
numbers cannot draw a screen.** The brief said to wire `loadClassSummaries`
and `submissionsFor` into `base()` in the shape written at the end of round
two's §6, and separately to "extend the aggregate". Doing the first with the
existing RPC would have set `week[0]` to 0, `last` to "No activity yet",
`classMean` to null and every `col*` array to empty on every class card. So
`loadClassSummaries` keeps its name and its place and now calls a NEW, larger
function; the two-line shape survives as `loadClassSummaries(ids, {now,
windows})` plus `submissionsFor`.

**Deviation: the new migration DROPS `teacher_class_summaries` → rather than
leaving it beside the rollup → because its six numbers are reproduced verbatim
and two SQL implementations of one locked rule is the drift its own header
warns about.** Nothing calls it and it was never on production, so dropping it
costs nothing. Both migrations must be applied to production, in order.

**Deviation: the exec seam was not restored.** `docs/mrb348/rls-consolidation.md`
§8 says `mrb348_exec_sql` / `mrb348_exec_ddl` were dropped and would need
re-applying for further DDL on TEST. They were not needed: the claude.ai
Supabase connector takes an explicit `project_id` on **every** call, so there
is no ambient project to be wrong about (CLAUDE.md item 8's own reasoning), and
the DDL went through it. The ref was still proven out of the service-role JWT
before any fixture write. No arbitrary-SQL function was created on TEST and
none needs dropping.

**Deviation: `class-detail.html` with no `?class=` keeps the OLD full read →
rather than guessing the class → because `load()` resolves it to `CLASSES[0]`
AFTER `base()` has already decided the scope.** Guessing would risk fetching
the wrong class's cells and drawing an empty grid on a real class. Every link
the product generates carries `?class=`; `class-fallback` in the rendered diff
is the case that proves the path is unchanged.

**Deviation (adjacent fix, in passing): `yearOfClass` was fetching a class's
entire submission history to read one field.** It exists to answer "which
academic year is this class in", and doubles as the authorisation check — but
the authorisation happens in Stage A, which `submissionsFor` does not touch. It
now passes `{ submissionsFor: [] }`.

**Finding, not a deviation: round two's "insights.html — 129 → 129, genuinely
the broadest" is no longer true.** That was a true statement about the SUMMARY
aggregate, which could not supply the per-paper columns the charts read. The
rollup can, and the question grids the charts draw come from
`loadPaperQuestions`, a separate read this ticket does not touch. Insights is
now on the narrow path and its rendered output is identical.

**Finding: `hz_rich`'s HoD reach is real at the database and invisible on the
page.** The brief expected the HoD row to exercise a wide cross-department
read through the render. It does not: `loadTeacherClasses` is deliberately
SELF-FILTERED to the viewer's own `class_teachers` rows (MRB-325 ruling 1, the
Today/My-classes leak fix), so `classes.html` shows him ONE class. The wide
read is proven in §3a instead, where the same user was asked about all twelve
class ids directly and RLS answered for eleven, with the aggregate agreeing on
every one. Both are reported rather than one standing in for the other.

**Finding, flagged and not acted on: `mide.badmus` holds SIX `class_teachers`
rows for FIVE classes** — 10A appears twice. Every current consumer dedupes by
class id and the rollup groups from `classes` joined to the asked id list, not
from `class_teachers`, so nothing double-counts today. It is written down
because an aggregate that ever grouped by the link table would.

**Deviation: the fallback was proven by changing a SHARED database for about
four minutes → rather than by a local stub → because a stub would have proved
the wrong thing.** Renaming `teacher_class_rollup` out of TEST's catalogue is
the only way to put PostgREST's real answer to a missing function in front of
the page; a hand-written `throw` in a copy of `teacher-data.js` proves that a
`throw` is caught and nothing else. ⚠️ **The cost is named: for the length of
that drive, any other session driving a teacher page on TEST also took the
fallback path.** That is harmless — the fallback renders the identical page,
which is the whole finding — but it is a change to a project other people are
using, so it was kept short and the restoration was verified from `pg_proc`
rather than assumed (§4b).

**Deviation: the first BEFORE waterfall measured the wrong code, twice over.**
Round three landed in three commits, so `HEAD~1` still contained the change;
and both trees serve the same asset URLs with the same cache-bust stamp, so
running them on one port let Chrome answer the second run from the first run's
cache. Both traps are written into `perf_waterfall.py` and the tell is
recorded: `rpc:teacher_class_rollup` in the critical path of a run that was
supposed to predate it.

**Not a deviation, but it must not be buried: `teacher_admin_foreign_class` is
RED and it is the inherited red** (C7 REMINDERS × 3). It was not weakened, not
re-run until green, and not overridden. §7 carries the output.

**Named consequence, checked rather than assumed: `cache.packs` is exposed and
its `submissions` are now empty for any class the screen is not focused on.**
`base()` publishes `packs` on the cache. Nothing reads it — not
`teacher-live.js`, not `teacher_rulings.py`, not `build_teacher_port.py`
(grepped, zero hits) — and everything that USED to read a pack's submissions
now reads the matrix instead. A future consumer that reached for
`cache.packs[id].submissions` would get an empty list for five classes out of
six and no error, which is why it is written down here and in
`loadClassMatrices`'s own note rather than left to be discovered.

**Finding: TEST's fixtures cannot be driven by two sessions at once.** The
rendered diff caught a throwaway assignment from another gate's fixture
appearing on 10A mid-capture and vanishing again — see §4. Nothing was wrong
with either session; the hazard is structural, and the harness now pins each
case to an identity so it cannot silently measure a different world.

**My own arithmetic was the only thing the fixture caught.** Its first draft
gave the in-week paper a deadline of `window start + 1 day`, which on any day
but Monday has already passed — so the paper was in this week AND marked and
walked into every marked-paper total. JS and SQL agreed with each other
exactly and both disagreed with me. Fixed by moving the deadline to an hour
before the window closes.
