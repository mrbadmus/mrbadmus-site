# MRB-348 WS-2 — the teacher summary aggregate

22 September 2026. Rehearsed on **TEST** (`qeppkiswvclkkwbxmlok`, ref proven
out of the service-role JWT's own `ref` claim, never read off a label).
**Nothing was applied to production.**

---

## 1. What was wrong

`loadClassMatrices()` in `shared/teacher-data.js` is the universal read behind
all six generated teacher screens. Stage B fetches **every submission of every
assignment of every class the viewer touches** — no limit, no window — and the
class-card numbers are then counted in JavaScript by `pickFirstAttempts()` +
`deriveClassMetrics()`.

On the realistic TEST teacher (`mide.badmus@test-rainford.local`, 5 classes)
that is **129 rows on every screen**, of which 79 are submissions. At five
classes × forty assignments × thirty pupils — an ordinary December — it is
about **6,000 submission rows to render a page that often shows six numbers
per class**.

---

## 2. The aggregate — `public.teacher_class_summaries(uuid[])`

Migration: `supabase/migrations/20260922114500_mrb348_teacher_class_summaries.sql`
(full reasoning is in that file's header; this is the summary).

One row per class the caller may see:

| column | JS it reproduces |
|---|---|
| `active_member_count` | `loadClassMatrices` members grouping — `left_at IS NULL`, `deleted_at IS NULL`, live profile |
| `assignment_count` | non-deleted assignments of the class |
| `submissions_completed` | `deriveClassMetrics` — first attempts with `submitted_at IS NOT NULL` |
| `completion_pct` | `Math.round(handed / (members × assignments) × 100)`, NULL when the denominator is 0 |
| `class_mean` | `buildMatrix().classMean` — the mean OF the marked column means |
| `last_activity_at` | `max(submitted_at)` over the first attempts |

**First-attempt rule (MRB-38), now with two implementations that must agree:**

```
JS pickFirstAttempts()                  SQL DISTINCT ON
lower `attempts` wins                   COALESCE(attempts, 2147483647) ASC
tiebreak: earlier submitted_at          COALESCE(submitted_at,'infinity') ASC
NULL attempts is worst                  2147483647
NULL submitted_at is worst in a tie     'infinity'
```

The shape copied from `class_stars_leaderboard_for_member`, as instructed.
`s.id ASC` is appended as a deterministic tiebreak for a FULL tie (same
`attempts`, same `submitted_at`) — an anomaly neither side actually defines,
because the JS separates such rows only by PostgREST's unspecified return
order. TEST held none.

**Three predicates that are easy to conflate and are not the same:**

- `submissions_completed` uses **`submitted_at IS NOT NULL`** — the card's
  rule, from `deriveClassMetrics`.
- the **column mean** counts a cell that `cellOf` would accept:
  `completed_at IS NOT NULL OR submitted_at IS NOT NULL OR status='complete'`,
  **and** `score IS NOT NULL AND max_score > 0`. A row with `completed_at` and
  no `submitted_at` is in the mean and NOT in the count.
- **`marked`** means only *"the deadline has passed"* (`buildPapers`:
  `open = !due_at || due_at > now`). Not released, not sat, not graded. An
  assignment with no `due_at` never closes and is never marked.

**Rounding.** `round(((a::float8 / b::float8) * 100)::numeric)` — the same IEEE
double division JavaScript does, then half-away-from-zero, which equals
`Math.round` for non-negative values. Rounding the float8 directly would use
Postgres's banker's rounding and disagree on every exact `.5`; doing the
division in `numeric` would disagree wherever the double lands a hair under a
`.5`. The adversarial fixture below lands exactly on `47.5` on purpose.

### Security

`SECURITY DEFINER`, `SET search_path TO 'public'`, gated as the first
statement, in the shape of `class_teachers_for_viewer` /
`class_stars_leaderboard_for_member`. An unreadable class id is **dropped
silently**, not raised — a summary read is asked speculatively over a
remembered id list, and one stale id must not take a page down.
(`loadClassMatrices` still THROWS, deliberately: it is a page's authorisation
check.)

⚠️ **The gate is not one predicate, because the four tables' RLS is not one
predicate.** Live policies on TEST (post-WS-3 consolidation):

```
classes / class_members   operator | school+(school_admin|slt) | school+hod | school+teaches
assignments / submissions operator | school+(school_admin|slt)
                          | school + HOD OF THAT SUBJECT'S DEPARTMENT
                          | school+teaches
```

A plain HoD sees every class in the school and every member of it, but only
their own department's assignments — and therefore only their own
department's submissions. `all_work` in the function is exactly that
distinction. **This asymmetry is what the `hz_rich` (hod) row of the proof
below exercises**: eleven classes visible, most of them with their assignment
set narrowed, and both sides agreeing class by class.

The pupil arms (`student_id = auth_user_id()`) are deliberately **not**
reproduced: this is a teacher aggregate, a pupil calling it has the class
dropped by the gate. That is a narrowing of what RLS would allow them, never a
widening.

---

## 3. Proof — before vs after, as real numbers

Method: a Python replay of `loadClassMatrices`'s exact PostgREST reads, signed
in as a real user under real RLS with the anon key, with `pickFirstAttempts`,
`deriveClassMetrics` and `buildMatrix`'s `classMean` translated line for line;
then the RPC, as the same user, in the same instant; then a cell-by-cell diff.

### 3a. Every class, every reader

| reader | asked | JS-visible | RPC returned | JS rows fetched | cells compared | mismatches |
|---|---|---|---|---|---|---|
| `mide.badmus@test-rainford.local` (teacher, 5 classes) | 12 | 5 | 5 | 144 | 30 | **0** |
| `hz_amy@test.mrbadmus` (teacher, 1 class) | 12 | 1 | 1 | 6 | 6 | **0** |
| `hz_rich@test.mrbadmus` (**hod**, whole school) | 12 | 11 | 11 | 190 | 66 | **0** |

**102 of 102 values identical**, and the visibility sets matched exactly —
including the twelfth class, which is in another school and which neither path
returned to anybody.

### 3b. The realistic teacher's five classes, value by value

| class | member count | assignments | submissions completed | completion % | class mean | last activity |
|---|---|---|---|---|---|---|
| `…0001` | 5 / 5 | 5 / 5 | 15 / 15 | 60 / 60 | 78 / 78 | `2026-05-23T10:19:55.088435+00:00` both |
| `…0002` | 6 / 6 | 18 / 18 | 47 / 47 | 44 / 44 | 73 / 73 | `2026-05-25T08:00:00+00:00` both |
| `…0003` | 5 / 5 | 4 / 4 | 17 / 17 | 85 / 85 | 85 / 85 | `2026-05-22T16:19:55.088435+00:00` both |
| `…0004` | 3 / 3 | 1 / 1 | 0 / 0 | 0 / 0 | — / — | — both |
| `…0005` | 3 / 3 | 0 / 0 | 0 / 0 | — / — | — / — | — both |

(js / sql. A dash is a real NULL, and the two kinds of null are distinguished:
`…0004` has a denominator and scores 0%, `…0005` has none and returns NULL.)

⚠️ TEST drifted mid-session — another session added an assignment to `…0001`
and `…0002`, moving `assignment_count` 4→5 and 17→18 and `completion_pct`
75→60 and 46→44. **Both implementations tracked the change identically**,
which is a stronger signal than a frozen dataset would have given.

### 3c. The adversarial fixture — three-way agreement

Built on TEST on class `…0004` (clean: 3 members, 1 assignment, 0 submissions),
then **torn down by a snapshotted id list, never a predicate**, and the class
confirmed back at its exact baseline afterwards.

Three assignments (one marked, one with a future deadline, one with no
deadline) and fifteen submissions covering, deliberately:

1. a retake where the **higher** score has `attempts = 2` (first attempt must win)
2. a row with **NULL `attempts`** against one with `attempts = 1` (null is worst)
3. two rows with the **same `attempts`**, different stamps (earlier wins)
4. an **off-roster** submitter — in the column mean, not in the member count
5. `completed_at` set, **`submitted_at` NULL** — in the mean, NOT in the count
6. **submitted but ungraded** — in the count, not in the mean
7. **`max_score = 0`** — excluded from the mean entirely
8. an **in-progress** row (no stamp, status not `complete`) — no cell at all
9. a **soft-deleted** row that would otherwise have been the first attempt
10. submissions on the **upcoming** and **no-deadline** assignments — handed in, never in the mean
11. sums chosen to land the column mean on exactly **47.5**

| value | by hand | JS | SQL |
|---|---|---|---|
| `active_member_count` | 3 | 3 | 3 |
| `assignment_count` | 4 | 4 | 4 |
| `submissions_completed` | 9 | 9 | 9 |
| `completion_pct` | 75 | 75 | 75 |
| `class_mean` | 48 | 48 | 48 |
| `last_activity_at` | `2026-04-30T10:00:00+00:00` | same | same |

**0 mismatches.** The class mean is `(5+3+2+8+1) / (8×5) = 19/40 = 47.5 → 48`
— the rounding boundary, agreeing three ways.

---

## 4. Rows fetched, per screen

Measured on `mide.badmus@test-rainford.local` (5 classes, 28 assignments,
79 submissions, 22 member rows).

Per class: `…0001` 5 assignments / 15 submissions · `…0002` 18 / 47 ·
`…0003` 4 / 17 · `…0004` 1 / 0 · `…0005` 0 / 0.

| screen | today | with the scope wired | saving |
|---|---|---|---|
| `classes.html` | 129 (22 + 28 + 79) | 55 (22 + 28) + **5 RPC rows** | −74 submission rows |
| `digest.html` | 129 | 55 + **5 RPC rows** | −74 |
| `class-detail.html` `?class=…0002` | 129 | 97 (22 + 28 + 47) | −32 |
| `class-detail.html` `?class=…0004` | 129 | 50 (22 + 28 + 0) | −79 |
| `assignment.html` (one assignment of `…0002`) | 129 | 97 | −32 |
| `student-detail.html` (`…0002`) | 129 | 97 | −32 |
| `insights.html` | 129 | 129 | 0 — genuinely the broadest |

**Projected at a December load** (5 classes × 40 assignments × 30 pupils):
about 6,000 submission rows on every screen today; the summary screens would
fetch **5 rows** instead, and a single-class screen about a fifth of the rest.

Actually applied today: **only** the `total_time_seconds` drop (below). The
scope is available and OFF — see §6.

---

## 5. What was changed, and what was not

### Applied

- **`supabase/migrations/20260922114500_mrb348_teacher_class_summaries.sql`** —
  the RPC. Rehearsed on TEST. **Not applied to production.**
- **`shared/teacher-data.js`**
  - `loadClassSummaries(classIds)` — a chunked wrapper on the RPC, returning
    the **same key names `deriveClassMetrics` already produces**
    (`student_count`, `assignment_count`, `submission_count`, `completion_pct`,
    `last_activity_at`) plus `class_mean`, so it is a drop-in for the
    `classRows.forEach` metrics-fill block in `teacher-live.js`'s `base()`.
  - `loadClassMatrices(classIds, opts)` — `opts.submissionsFor`, an array of
    class ids whose submissions may be fetched. **Omitted or `null` → every
    class, which is today's behaviour byte for byte.** The filter is applied to
    the ASSIGNMENT list, so a class left out costs no rows over the wire at all.
  - `total_time_seconds` **dropped** from all three teacher-side submission
    selects.

### Verified, then deliberately NOT done

- **`id` is NOT droppable.** The task asked to drop `id` and
  `total_time_seconds` "if you confirm by grepping that nothing consumes
  them". `total_time_seconds` is genuinely unread on the teacher side (its
  only consumers are `shared/student-live.js` and `shared/student-data.js`,
  which fetch it on their own reads). **`id` is read**: `buildMatrix` in
  `shared/teacher-live.js` (~line 945) does `subId[p] = mine[p].id`, and
  `subId` is the only thing written feedback binds to
  (`buildFeedback(stEarly.subId, …)`, `mGrid.rows.map(r => r.subId)`).
  Dropping it would have silently removed the feedback control from the
  student and marking screens.

- **The academic-year window on the assignments read is a no-op, so it was not
  added.** `assignments` has **no `academic_year_id` column** (checked against
  the live schema). A class belongs to exactly one academic year
  (`classes.academic_year_id`), and the class list reaching
  `loadClassMatrices` is already year-scoped one level up by
  `loadTeacherClasses(selectedYearId)` in `base()` — which uses
  `workingAcademicYear()` from `shared/class-entry.js`, the single
  implementation, with its null-means-"I-don't-know" fallback intact. Every
  assignment of a class is therefore already inside that class's year by
  construction. The only window that *would* remove rows is a date filter on
  `due_at` / `created_at`, and that **would change rendered output** — the
  digest and the week rail read every paper of the year. Adding a filter that
  cannot remove a row, to look like a bound, is worse than not adding one.

---

## 6. The blocker — why the scope ships OFF

⚠️ **The premise "`classes.html` … does not need a single submission row" is
false as the code stands, and the reason is not in the data layer.**

All six screens share **one compiled `renderVals`**, emitted into each page by
`build_teacher_port.py`. It computes all-classes, submission-derived
aggregates **unconditionally, on every screen** — in
`teacher/class-detail.html` at lines 1572–1609 and 2057–2098:

```
totalSubs   = liveClasses.reduce((a, c) => a + c.week[0], 0)
dgMarkedSub = liveClasses.reduce((a, c) => a + this.matrixFor(c).markedSub, 0)
dgOnTime / dgLate / dgUnknown / dgMeans / digestRows / reteachRows / weakFor
```

and `classes.html` draws, per card, `weekLabel: c.week[0] + ' of ' + c.week[1]
+ ' in'` (line 1639), `pct` off the same pair (1640), `k.last` (2202), the
`state === 'live'` filter (1502, 1574) and `meanOf(k) → classMean` (1552).
Every one of those comes from `pack.submissions`.

So a submission-free pack for the summary screens would change:
`week[0]` → 0, `last` → "No activity yet", `state` → `nowork`,
`classMean` → null, and every `col*` aggregate → empty. The card that reads
"4 of 6 in · last activity 2 days ago · mean 73%" would read
"0 of 6 in · No activity yet · —".

**What the RPC gives back covers `student_count`, `assignment_count`,
`submission_count`, `completion_pct`, `class_mean` and `last_activity_at` —
six of those. It does not cover `week[0]` / `week[1]` (the current teaching
week's submitted-of-asked) nor the per-paper `colSub` / `colAsked` / `colMean`
arrays the digest sums.** Closing the gap is a bigger aggregate (a per-paper
row set, or a week-window pair on the summary), and it is a change to what
`teacher-live.js` builds — not to this file.

Which single-class screens can safely narrow is likewise decided **inside
Design's compiled template, node by node**: the values above are computed on
every screen, and whether each reaches the DOM on `class-detail` /
`assignment` / `student-detail` is a property of the template, not of the data
layer. Establishing it needs a rendered-output diff of all six pages, which is
`teacher_rulings.py` / `build_teacher_port.py` work.

**Therefore the capability ships wired but OFF**, with the default byte-for-byte
unchanged, so nothing a teacher sees can move. The wiring, when someone takes
the rendering half:

```js
// teacher-live.js, base() — the summary screens
var sums = await TD.loadClassSummaries(classIds);     // 5 rows, not 6,000
// teacher-live.js, base() — the single-class screens
packs = await TD.loadClassMatrices(classIds, { submissionsFor: [params.classId] });
```

`base()` caches per page load and each teacher screen is a full navigation, so
a per-screen scope cannot leak from one screen to the next within a session.

---

## 7. Gates

Run with `MRB_TEST_TEACHER_PASSWORD='…'`:

| gate | result |
|---|---|
| `teacher_behaviour` | **PASS** — 24 fixtures, 952 of 935 controls pressed |
| `teacher_reach` | **PASS** — 24 fixtures × 2 widths, 3144 controls hit-tested over 2010 presses |
| `teacher_picker_drive` | **PASS** — 2 widths, zero requests, zero storage keys |
| `teacher_perf_budget` | **PASS** — 4 journeys, 72 / 232 / 135 / 173 ms against a 2500 ms budget |

⚠️ `teacher_perf_budget` drives `hz_amy` and `hz_rich`, who hold one class each
with almost no work. It cannot see this defect and cannot see its fix; it was
run to prove nothing REGRESSED, not to measure a gain.

---

## 8. Open

- The migration is **rehearsed on TEST only**. Production application is Mide's,
  per CLAUDE.md's "When a migration may touch PRODUCTION".
- The rendering half (§6) — a week-window pair and a per-paper aggregate, plus
  a rendered-output diff of the six pages — is not in this workstream's files.
- `mrb348_exec_sql` / `mrb348_exec_ddl`, the temporary rehearsal RPCs WS-3
  installed on TEST, were **dropped by that workstream part-way through this
  run**. The function was already applied; every measurement after that point
  used PostgREST reads and service-role writes instead. A further DDL change on
  TEST would need that path restored.

---

## 9. Rollbacks, and the round trip rehearsed on TEST

22 September 2026, later the same day. Written so both MRB-348 aggregate
migrations can reach production with an undo beside each, per the house rule
that no migration ships without one. **Nothing was applied to production in
this run**; every statement below named `qeppkiswvclkkwbxmlok` (TEST)
explicitly, and the connector takes the project on every call, so there was no
ambient default to be wrong about.

### 9a. The two files

| rolls back | file |
|---|---|
| `20260922114500_mrb348_teacher_class_summaries` | `supabase/rollbacks/20260922114500_mrb348_teacher_class_summaries_rollback.sql` |
| `20260922231500_mrb348_teacher_class_rollup` | `supabase/rollbacks/20260922231500_mrb348_teacher_class_rollup_rollback.sql` |

Each forward migration does exactly one thing to the catalogue — 114500 creates
`teacher_class_summaries(uuid[])`; 231500 drops it and creates
`teacher_class_rollup(uuid[], timestamptz, jsonb)` — so each rollback does that
thing backwards and nothing else. **No table, no policy and no row of pupil
data is touched by either.** Rolling back 231500 recreates the older function;
rolling back 114500 then removes it. Run in that order they land on "before
either migration"; run only the first, on "exactly what 114500 left".

⚠️ **Neither file re-states GRANT or REVOKE, and that is deliberate** — it is
the opposite of the MRB-336 precedent, so it is justified in each header.
The house rule exists because `CREATE OR REPLACE` resets privileges and a
rollback that opens a hole is worse than the thing it undoes. But neither
MRB-348 migration contains a single executable GRANT or REVOKE: both rely on
the estate's default privileges. Re-stating grants would therefore leave a
*different* ACL from the one 114500 leaves. Proven below rather than argued.

### 9b. The round trip, read out of the catalogue at every step

Fingerprints are `md5(pg_proc.prosrc)` — the function body exactly as Postgres
stores it — compared against the same bytes extracted from the migration file
on disk. That is what makes "identical" a measurement and not an impression.

| step | `teacher_class_summaries` | `teacher_class_rollup` |
|---|---|---|
| 0. as found on TEST | absent | present, **body ≠ the committed file** (see 9d) |
| 1. rollback 231500 | present · `5368b2ef…` ✅ = file | absent |
| 2. forward 231500 | absent | present · `76419b38…` ✅ = file |
| 3. rollback 231500 again | present · `5368b2ef…` ✅ = file | absent |
| 4. rollback 114500 | absent | absent — **0 `teacher_class%` functions remain** |
| 5. forward 114500 | present · `5368b2ef…` ✅ = file | absent |
| 6. forward 231500 | absent | present · `76419b38…` ✅ = file |

**The equality that matters is between rows 1/3 and row 5.** Rolling back
231500 and applying 114500 forward land on the same body hash *and* the same
ACL (`=X/postgres | postgres=X | anon=X | authenticated=X | service_role=X`)
and the same `proconfig` (`search_path=public`). So "rolling back 231500 leaves
the database exactly as 114500 left it" is proven from both directions, not
assumed. Row 4 proves the second rollback reaches the state before either.

Steps 1 and 3 are byte-identical to each other, so the rollback is
deterministic and safe to run twice.

### 9c. The aggregate's output is unchanged by the round trip

The realistic teacher (`28000000-…-0001`, five classes) was read before the
round trip and again after it, with the clock **pinned** to
`2026-09-22T12:00:00Z` and a fixed week window — without pinning, `marked`
could flip between captures and the comparison would prove nothing.

All five classes returned identical values and identical `md5` of both the
`papers` and the `students` arrays. It also reproduces §3b of this document
exactly:

| class | members | assignments | handed in | completion | class mean |
|---|---|---|---|---|---|
| `2a…0001` | 5 | 5 | 15 | 60% | 78 |
| `2a…0002` | 6 | 18 | 47 | 44% | 73 |
| `2a…0003` | 5 | 4 | 17 | 85% | 85 |
| `2a…0004` | 3 | 1 | 0 | 0% | — |
| `2a…0005` | 3 | 0 | 0 | — | — |

### 9d. ⚠️ TEST was running a body that was never committed

Found, not expected, and the most useful thing in this section.

The `teacher_class_rollup` **as found on TEST** had
`pg_get_functiondef` length **9,291** characters. The committed migration's
function body alone is **11,560**. A definition cannot be shorter than the body
it contains, so TEST was demonstrably running a *different, shorter* body —
consistent with the round-three record's own pin of `70fc3ad5…`, which is not
the committed file's `76419b38…`. The migration file has exactly **one** commit
in its history, so the variant on TEST was never a committed version of it: it
was an ad-hoc or earlier paste. The gap (~2,650 characters) is the size of the
inline `⚠️` comment blocks in the committed body.

**Behaviour was identical**: the baseline captured from the variant (§9c,
before) and from the committed file (after) agree value for value and hash for
hash, across all five classes, papers and pupils included. So this is a
provenance defect, not a behavioural one — but it means **the 22 September
proof was run against a body that is not byte-identical to the file the chat is
about to apply to production.** As of step 6 above, TEST runs the committed
file, and the numbers did not move.

⚠️ The variant's source text was overwritten by step 1 and was not captured
beforehand — only its `def` hash `aca7dac6…` and length. It cannot now be
diffed line by line.

### 9e. The gate, driven rather than trusted

`teacher_class_rollup` is `SECURITY DEFINER`, so it runs as `postgres` and its
own internal gate is the *only* thing standing between a caller and every
class in the estate. There is a live hole of exactly this shape elsewhere
(teachers can press reminders on other teachers' classes), so it was driven.

Each identity below asked for **all twelve classes on TEST** — their own
alongside other teachers', other schools', and ones they have no relation to —
and what came back was parsed, not assumed. Impersonation is by
`set local request.jwt.claims`, which needs no password.

| caller | asked | returned | verdict |
|---|---|---|---|
| Sarah (plain teacher, 1 class) | 12 | **1** — only `22…0001`, the class she teaches | ✅ no leak |
| Amy (plain teacher, 1 class) | 12 | **1** — only `ee…0401`, the class she teaches | ✅ no leak |
| Tia (teacher, **another school**) | 12 | **1** — only her own school's `ee…0404` | ✅ no cross-school leak |
| Rich (**HoD** Science) | 12 | **11** — every class in *his* school, and not the other school's | ✅ correct for the scope |
| Hannah (**a pupil**, 17 submissions of her own) | 12 | **0** | ✅ student arms not reproduced |
| anon (signed out) | 12 | **0** | ✅ `EXECUTE` to `PUBLIC` is harmless |

⚠️ **The HoD row is the one that could have hidden a leak, and it is the one
worth reading twice.** A HoD sees every class in the school but only their own
department's *work*, so the function must narrow papers per class while still
returning the class. `HZ 10M Maths` really holds one assignment; Rich, HoD of
**Science**, got `papers = 0` for it while still seeing the class and its
roster. Every Science class returned its full paper count
(`10A` 18/18, `8X1` 5/5, `10X1 Biology` 4/4, `7z/Sc9` 6/6). The asymmetry is
real and it is in the right direction.

The pupil row is the other one that matters: `class_members` and
`assignment_submissions` both grant a pupil their own rows, so a naive
reproduction of RLS would have returned Hannah her own class. It returns her
nothing — a narrowing of what RLS allows, never a widening.

### 9f. What this rehearsal did NOT cover

- **`mrb348_teacher_rollup_proof.py` was not run.** It needs
  `$MRB_TEST_TEACHER_PASSWORD`, which is not on this machine. The
  SQL-level proof above is stronger for the gate question (it drives six
  identities, including a pupil and anon, where the script drives three
  teachers) but it does **not** re-run the script's JS-vs-SQL equivalence
  comparison or its adversarial fixture. §3 of this document remains the
  authority for those, with the provenance caveat of §9d.
- **Nothing was applied to production**, and no `db push` was run anywhere.
- The registry version drift is recorded in each rollback's header: TEST
  carries the rollup as `20260922175719`, the connector's own stamp, not the
  filename's `20260922231500`. Both rollbacks therefore match on the
  migration *name* as well as the version.

### 9g. Production pre-flight — READ ONLY, nothing applied

The gate in §9e was proven against **TEST's** policy set. That is not
automatically a statement about production: MRB-348 WS-3 recorded that the two
projects' policy bodies had drifted (153 policies on prod against 141 on TEST),
and the rollup's internal gate is a HAND-WRITTEN REPRODUCTION of those
policies. A gate that mirrors the wrong database is a gate that returns numbers
no reader could have computed for themselves — so production's own catalogue
was read. **Four `SELECT` statements against `pg_policies`,
`pg_proc` and `information_schema.columns`. No DDL, no DML, no `db push`,
nothing written.**

**1. The policies.** Production already carries the consolidated
`*_select_merged` policies on all four tables. Read against the gate:

| table | production grants `SELECT` to | the gate's arm | verdict |
|---|---|---|---|
| `classes` | operator · school+(school_admin\|slt) · school+hod · school+teaches · **school+member (pupil)** | operator · school+(wide\|hod\|teaches) | ✅ equal, minus the pupil arm |
| `class_members` | **self** · operator · school+(admin\|slt) · school+hod · school+teaches | counted only for a class that passed `can_see` | ✅ equal, minus the pupil arm |
| `assignments` | operator · school+(admin\|slt) · school+`is_hod_of_subject_dept` · school+teaches · **school+member, released, undeleted (pupil)** | `all_work` ∪ (hod scope ∧ `is_hod_of_subject_dept`) | ✅ equal, minus the pupil arm |
| `assignment_submissions` | **self** · operator · school+(admin\|slt) · school+`is_hod_of_subject_dept` · school+teaches | drawn only from assignments that already passed | ✅ equal, minus the pupil arm |

**The gate is equal-or-narrower than production on every table**, and every
place it is narrower is a pupil arm it deliberately does not reproduce — the
same narrowing §9e drove and confirmed. There is **no arm on which the gate is
wider than production's own RLS.** ⚠️ Note the gate additionally requires the
`hod` scope where production's `assignments` policy names only
`auth_user_is_hod_of_subject_dept(subject_id)`; if that function can ever be
true for someone without the scope, the gate is narrower there too, never
wider.

**2. The dependencies.** All eight helpers the body calls exist on production
(`auth_user_school_id`, `auth_user_operator_active`, `auth_user_has_scope`,
`auth_user_teaches_class`, `auth_user_is_hod_of_subject_dept`,
`auth_user_is_member_of_class`, `auth_user_id`, `class_school_id`).

**3. No collision.** Production holds **neither** `teacher_class_summaries` nor
`teacher_class_rollup` — consistent with neither migration having been applied
there.

**4. Every column exists.** All 25 columns the body reads were checked by name
against production's `information_schema`; **zero missing**, `is_late`
included (it is the newest, added 22 Aug 2026).

So both migrations can be applied to production as written. ⚠️ What this
pre-flight does **not** do is re-run §9e's leak drive against production's own
rows — that would mean impersonating a real teacher over real pupils' data, and
it is not needed to answer the question it was asked: whether the gate's shape
matches the policy set it will run under. It does.
