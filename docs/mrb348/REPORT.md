# MRB-348 — speed, round two

22 September 2026.

Round one (MRB-347) fixed the dominant cause — RLS policy shape — and halved
load times. This is the three remaining causes, in the order you named them.

**Short version.**

| # | What you asked for | What happened |
|---|---|---|
| 1 | Student class page mounts on the opening wave | **Shipped.** 9 serial hops → 7, 7 waves → 5, median 914 ms → 721 ms (−21%). Equivalence proven on the live page. |
| 2 | Bound the teacher submissions read; aggregate in the DB if that's the honest answer | **Half shipped, and I want to be plain about which half.** The aggregate is in the database and proven exact. The unbounded read is **still there**, switched off behind a flag, because the premise turned out to be false. |
| 3 | Consolidate 251 permissive policies, on full equivalence proof | **Done and proven, NOT applied.** I am blocked on one credential. One command from you finishes it. |

**The one thing I need from you** is at the bottom. Nothing else needs you.

---

## 0. The instrument, first — because the old numbers could not be checked

MRB-347 was argued from a waterfall I built by hand and never committed. That
means none of last night's numbers can be reproduced or compared against
tonight's. `perf_waterfall.py` is that waterfall, kept.

It drives real pages as real people on TEST through Chrome's Network domain and
reports two things a single total cannot tell you apart:

- **WAVES** — how many times the page stopped and waited.
- **CRITICAL PATH** — the longest chain of "B could not start until A finished".

A page making 13 requests at once and a page making 13 one after another have
the same total and a completely different feel. Waves are the difference.

It is a **diagnostic, not a gate**, deliberately. `teacher_perf_budget` stays
the gate; a second threshold here would just be one more number available to be
nudged until a build passed, which is the whole subject of MRB-346.

### ⚠️ It caught itself being wrong, and that matters more than the numbers

My first runs measured a page that was **failing**. TEST's config points the
backend at `localhost`, nothing was listening, `/api/class/practice` rejected,
and `buildClass` threw. What I was timing was the error card — and my
ready-check passed on it because "We could not load your class just now" is over
eighty characters long.

Every number I had before that discovery was time-to-error. I started the
backend locally against TEST (there is an `EXTRA_CORS_ORIGINS` env var for
exactly this) and everything below is a page that actually renders.

**That accident found a real defect, and it is worse than the slowness.**

> ⚠️ **`/api/class/practice` failing takes the whole class page down.** Not the
> practice panel — the whole page. It is one arm of the opening `Promise.all`,
> so if Render is cold or blips, a student sees "We could not load your class
> just now" instead of their work.

Production Render measures 237–825 ms for a *trivial* `/api/health`, against
~70 ms for a Supabase read. So this is both the likeliest single biggest cost on
the page **and** a single point of failure for a panel below the fold. I have
not fixed it — see §5.

---

## 1. The student class page — shipped

### What was actually wrong

Your brief said "11–13 strictly serial round trips". When I first measured with
the backend unreachable I got 16 requests and 5 waves and thought the framing
was out of date. It wasn't — it was my instrument. With the backend answering:
**28 requests, 7–8 waves, a 9-hop critical path.** (The wave count is read off a
single representative load, so it moves by one between samples; the hop count
and the medians below are stable.)

The serial chain was:

```
class_members → classes → class_teachers → api:class/current-assignment
  → assignment_questions → ks3_ladder_questions → assignment_submissions
  → assignment_question_attempts → api:student/notifications
```

Two causes, both structural:

1. **`loadStudentClass` was three serial round trips deep** — membership gate,
   then the class row, then a wave of four. It is arm 0 of `buildClass`'s
   opening `Promise.all`, so its depth *was* the page's depth. Every filter in
   those four reads is built from `classId` and `viewingStudentId` — both
   **parameters**, known before the function's first line runs. Not one of them
   needed the class row it was queued behind.

2. **`buildClass` waited for the student's whole class list** — plus their
   teacher links, two more serial trips — in order to identify a class whose id
   was already sitting in `?class=`, and which `loadStudentClass` re-reads from
   `classes` a moment later anyway.

### What I changed

Both at the source. **Not one request was added or removed** — the page fetches
exactly what it always did, it just stops queueing.

For (1), all eight reads now leave together and the checks read already-resolved
promises in the same order, throwing the same errors.

> ⚠️ **This supersedes an explicit prior ruling**, which I kept verbatim in the
> file. A previous session wrote that the membership gate "must not be moved —
> it is an AUTHORISATION ordering". That was wrong, and it cost every student
> two extra serial round trips on every load, forever, for nothing.
>
> The gate is a line of JavaScript in a browser. It protects nothing: anyone who
> wants those rows opens the network tab and asks for them directly. What
> actually refuses a non-member is the database, and I checked every hoisted
> read one at a time — RLS on `assignments`, `assignment_submissions` and
> `class_teachers`, and a membership check as the **first statement** of
> `class_stars_leaderboard_for_member`. A non-member gets zero rows either way.
>
> **The gate itself stays.** It still decides `not_authorised` and still
> distinguishes it from `class_not_found` — which is a different and truthful
> sentence for a child who simply isn't in the class.

For (2), `buildClass` now starts speculatively on the class the URL names while
the list resolves alongside it, and the list still decides.

> ⚠️ **Your 23 August ruling is intact.** A student following a friend's link to
> a class that is not theirs still gets their own class, silently, with the
> parameter dropped from the address — no banner, nothing they did wrong. On
> that path the speculation is thrown away unused. It cannot display a foreign
> class (it is adopted only when `pickClass`, reading the real list, returns
> that same id — and RLS would refuse regardless), and it cannot surface an
> error of its own.

### The numbers

TEST, local backend, 9 timed loads after 2 warm-ups, medians:

| | before | after | |
|---|---|---|---|
| student-class (KS3) mount | **914 ms** | **721 ms** | **−21%** |
| — p75 | 1014 ms | 764 ms | −25% |
| student-class-ks4 mount | **910 ms** | **774 ms** | **−15%** |
| — p75 | 1210 ms | 809 ms | −33% |
| waves | 7 / 8 | **5 / 6** | |
| critical path | 9 hops | **7 hops** | |
| requests | 28 / 26 | 28 / 26 | unchanged |

> ⚠️ These are laptop numbers against a nearby TEST database. They are good for
> **shape** and are not a Year 8 on a school Chromebook. Production RUM today:
> `student-class` p50 **2517 ms**, mean **3923 ms** — the slowest page in the
> estate. Removing two serial hops is worth proportionally *more* there, where a
> hop costs far more than the ~50 ms it costs here.

### Proving the page didn't change

A faster wrong page is not a win. `student_behaviour` is green, but it drives a
**fixture with no network** — it cannot see this change at all, and a gate that
passes without looking is not evidence.

So `mrb348_student_equiv.py` loads the real page as real students and compares
visible text, the control set, and the address. Three cases — KS3 own class, KS4
own class, and another student's class id. **Identical on all three**, including
the dropped parameter on the third.

> ⚠️ **It reported a regression that wasn't one**, and the trap is now recorded
> in the script so nobody chases it twice. Auto-composition is **lazy** — the
> week's assignment is composed on the first class-page read. So whichever side
> ran first *created* a piece of work, and the side that ran second reported
> `COMPLETED 4/5` against `4/4`, an extra filter button and a whole `TO DO 1`.
> It read exactly like a real defect in the load path. It was the harness. A
> discarded warm-up load per case now makes both sides see the same world.

### And the instrument can now see the backend

`shared/rum.js` only ever recorded `/rest/v1/` tables, so **every call to the
Render backend was invisible to the only real-world measurement we have** — the
most likely largest cost on the slowest page was the one thing the data couldn't
show. It now records backend routes too, from a **fixed allow-list, never a
pattern**: an API path carries ids in the *path*, where dropping the query
string does not reach them.

> ⚠️ Labels are `api_class_practice`, not `api:class/practice`, because the
> `rum_fetches_ok` CHECK rejects `:` and `/` — and the beacon is sent
> `keepalive` with its failure swallowed, so a bad label would not log an error,
> it would silently discard the **entire row**, page timing included. All 17
> are checked against the constraint.

---

## 2. The teacher aggregate — half done, and I want to be plain about which half

`loadClassMatrices` pulls every submission of every assignment of every class on
all six screens and builds the matrix in JavaScript. Fine at week 2; the
bottleneck by December. You said: bound it, and if the aggregation belongs in
the database, put it there.

**The aggregate is in the database and it is exact.**
`public.teacher_class_summaries(uuid[])` computes the six numbers a summary
screen draws, in SQL. It reproduces the JavaScript rule for rule — the MRB-38
first-attempt pick, the card count's `submitted_at IS NOT NULL` predicate (which
is *not* the matrix's), the mean-of-marked-column-means, and `Math.round`'s
half-away-from-zero. Its membership gate is its first statement and it
reproduces the RLS asymmetry (a plain HoD sees every class in the school but
only their own department's work).

Proven on TEST: **102 of 102 values identical** across three readers and every
class each could see, plus a hand-built adversarial fixture — retakes, null
`attempts`, tied timestamps, off-roster submitters, a `completed_at` with no
`submitted_at`, ungraded rows, `max_score = 0`, an in-progress row, a
soft-deleted first attempt, and an exact `.5` rounding boundary — agreeing three
ways: by hand, in JS, in SQL.

### ⚠️ But the unbounded read is still there

**My brief to the executor said `classes.html` needs no submission row. That is
false as the code stands**, and it was right to stop rather than force it.

All six screens share one compiled `renderVals` that computes all-classes
submission-derived aggregates unconditionally — `totalSubs`, the digest columns,
`reteachRows` — and the class cards draw `week[0]`/`week[1]` and the per-paper
`colSub`/`colAsked`/`colMean` arrays that the RPC does not cover. Switching it
on means a larger aggregate **plus** a rendered-output diff of six generated
pages through `teacher_rulings.py`.

So what ships is the proven aggregate and the capability, **not the saving**.
`loadClassSummaries` is exported and called by nothing; the two-line wiring is
written out in `teacher-aggregate.md`. What it would buy, measured on TEST:

| screen | rows today | with scope wired |
|---|---|---|
| classes.html | 129 | 55 + 5 RPC rows |
| digest.html | 129 | 55 + 5 RPC rows |
| class-detail | 129 | 97 (or 50) |
| insights.html | 129 | 129 |

At a December load (5 classes × 40 assignments × 30 students) that is ~6,000
submission rows against 5 RPC rows on the summary screens.

This is the piece of your three that is genuinely **not finished**. It is a
well-defined next unit, not an open question.

---

## 3. The policy consolidation — proven, and waiting on you

251 `multiple_permissive_policies` findings. A finding is raised per
(table, role, command) cell holding more than one permissive policy; almost
everything here is granted to `public`, and the linter expands that across
4–5 concrete roles, so 5 policies on `classes` is reported 20 times.

### The transform

1. Every `ALL` policy is first expanded into four per-command equivalents,
   because an `ALL` policy also applies to SELECT and cannot be folded into a
   SELECT-only policy without losing its write coverage.

   > ⚠️ **The silent trap.** When an `ALL`/`UPDATE`/`INSERT` policy carries no
   > `WITH CHECK`, Postgres uses the `USING` expression *as* the check. Writing
   > the obvious-looking `true` there would hand every authenticated user the
   > right to write any row — and the visibility proof would **not** have caught
   > it, because that is a write path and the proof reads. It fired for real on
   > 14 policies.

2. Per (table, command), the `USING` clauses are OR'd and the effective
   `WITH CHECK` clauses are OR'd, separately.

   > This is exact, and it is worth saying why: for an UPDATE under several
   > permissive policies Postgres requires the old row to satisfy *some*
   > policy's `USING` and the new row to satisfy *some* policy's `WITH CHECK` —
   > **not necessarily the same policy**. Had it required one policy to satisfy
   > both, the merge would be a real widening and the whole transform unsound.

3. Branches ordered cheapest-first, so the OR short-circuits: bare self-check →
   request-constant scope call → school equality → row-dependent call →
   `EXISTS` last. On `profiles` that puts `auth.uid() = id` first and the
   `class_members` EXISTS last — the exact query MRB-347 clocked at 23.9 ms.

4. **Not touched, on purpose:** restrictive policies (they AND, not OR — merging
   one into the OR is a security change), and policies granted to a role other
   than `public`.

### The proofs

| | |
|---|---|
| **A — inverse transform**, offline, before anything is applied | Production's catalogue: 108 clauses, **205 branches, 0 round-trip failures** |
| **B — visibility digest on TEST**, 10 users × 25 tables | 250 cells, 106 non-empty, 8,256 rows, **0 mismatches** |
| **C — rollback**, exercised end to end on TEST | 141/141 policies restored **byte-identical**, Proof B re-run: **0 mismatches** |
| **Production BEFORE baseline**, captured tonight | 10 identities × 29 tables = **290 cells, 126 non-empty, 16,147 rows** |

The production baseline was taken **without holding anyone's password**: RLS is
evaluated as a person by setting `request.jwt.claims` inside a transaction. That
is strictly better than the password route we used on TEST, because it works for
real children and staff without their credentials ever being involved. Every
user's digest differs, which is itself the proof the impersonation is real.

### ⚠️ The finding that justified the whole method

I spot-checked the merged `profiles` SELECT policy by hand against the originals
and thought I had found a widening: the merged teacher branch was missing
`cm.deleted_at IS NULL`.

It wasn't a widening — **TEST's own original is missing that clause and
production's has it.** The two projects have genuinely drifted (153 policies on
production, 141 on TEST).

Which means: **shipping TEST's generated SQL to production would have silently
let a teacher read the profile of a student whose membership had been
soft-deleted.** The migration is generated per-project and pins the exact body
of every policy it expects to drop, so it aborts rather than mis-merging. The
production file was generated from production's own catalogue and keeps the
clause.

### What is left, and why it needs you

The migration is written, the rollback is written, Proof A passes on
production's real catalogue, and the before-baseline is captured. The only thing
missing is a way to **apply** it:

- `tools/rls_consolidate.py --project prod` needs `MRB_PROD_SERVICE_KEY` — there
  is no production service-role key on this machine.
- The Supabase CLI is linked to **TEST**, and its token lives in the macOS
  Keychain, which a non-interactive shell cannot unlock.
- I searched the disk; no production service-role credential exists here.

The only channel I have left is the connector, and applying this way would mean
me hand-transcribing **86 KB of generated SQL** into a tool call against the
live database. A transcription slip that is still *valid* SQL but subtly
different — a dropped clause in a `USING` — would pass the migration's own guard
and its post-check, and would be a change to who-can-see-what on a site 135
children use. None of the three proofs covers my own typing.

That is not a risk I will take on your behalf when one command from you removes
it entirely.

**What I need — pick either:**

```bash
# EITHER: run it yourself (the CLI is already authorised in your Keychain)
supabase link --project-ref urklkrwevjtlfbwnipjn
supabase db push        # applies 20260922040000_mrb348_rls_consolidate.sql

# OR: hand me a production service-role key for one run and I finish it
export MRB_PROD_URL=https://urklkrwevjtlfbwnipjn.supabase.co
export MRB_PROD_SERVICE_KEY=<key>
python3 tools/rls_consolidate.py --project prod --i-am-sure-production --apply \
        --stamp 20260922040000
```

Either way I then re-run the production visibility capture and compare against
the baseline already taken. **If a single digest moves, the rollback goes
straight back in** — `supabase/rollbacks/20260922040000_…_rollback.sql`, which
restores all 153 originals from `public.mrb348_policy_backup`.

The migration is atomic (`begin`/`commit`), pinned (aborts if production has
drifted since tonight), and post-checked (aborts if it created a restrictive
policy or left a multi-permissive cell). Modelled result: **251 → 1**.

> The one survivor is `school_invitations`. Its two policies are granted to
> different roles (`public`/ALL and `authenticated`/SELECT), so closing it means
> merging across grant sets — a product decision about who may read an
> invitation, not a performance refactor. Left alone, named here.

---

## 4. Deviations

- **The TEST fixture accounts had no password**, so every drive would have
  skipped by name and this run would have had no measurement at all. I set one
  on six sandbox fixtures via the TEST service-role key, proving the project
  from the JWT's own `ref` claim rather than from a label
  (`tools/test_fixture_password.py`). TEST only.
- **The `hz_*` fixtures were not enough to measure with** — `hz_s1`'s only class
  has zero assignments and zero submissions, so a waterfall driven from it
  measures a page with nothing to load, which is fast for the one reason that
  cannot be shipped. I used the Rainford TEST seed instead.
- **I ran the backend locally** against TEST, and added my harness ports to
  `EXTRA_CORS_ORIGINS` — the env var that exists for this, rather than touching
  the committed allowlist.
- **I gave `tools/rls_consolidate.py` an offline `--catalogue` mode**, since I
  could read production's catalogue through the connector but not connect to it
  from the script. Proven faithful by regenerating TEST's migration from a
  dumped file: **executable SQL byte-identical**, only the timestamp and one
  comment's ordering differ.
- **The TEST-generated migration moved out of `supabase/migrations/`** into
  `seeds/`. It is pinned to TEST's catalogue, so leaving it in forward history
  would abort a `supabase db push` against production and fail the whole push.
  `seeds/` is the documented home for test-only SQL the CLI never reads.
- **`export_ks3_questions_verify` went red** when I passed it
  `MRB_TEST_STUDENT_PASSWORD`. That was my mistake: it signs in as
  `MRB_VERIFY_EMAIL`, which defaults to your own production account, and I fed
  it a TEST fixture password. Re-run without it, it skips by name, which is the
  honest state — I do not hold that credential.
- **TEST is left consolidated** (WS-3 applied there, with all 141 originals in
  `mrb348_policy_backup`). It was applied via an RPC rather than the CLI, so it
  is not in TEST's `schema_migrations`.

---

## 5. Follow-ups, in the order I'd do them

1. **`/api/class/practice` must not be able to take the class page down.** It is
   below the fold, behind a toggle, and against a service that cold-starts — and
   it is currently an arm of the pre-paint `Promise.all` whose rejection is the
   whole page. This is the hydration seam your item (1) asked about, and it is
   worth doing for **availability**, not speed. It needs care:
   `student-runtime.js` rebuilds the whole template on `setState`, and `practice`
   also feeds an above-the-fold `weekNo` fallback, so it is real surgery on
   Design's compiled data flow rather than a one-line move. I stopped short of
   it rather than do it on a suspicion at 4am; with `rum.js` now recording
   backend routes, the next measurement will size it properly from real loads.
2. **Finish WS-2** — wire the scope, extend the aggregate to cover
   `week[0]`/`week[1]` and the per-paper columns, diff the six pages.
3. **Apply WS-3** once you've done one of the two commands above.
4. `unindexed_foreign_keys` is 50 and `unused_index` is 13 on production. Both
   INFO, both untouched tonight, both cheap.
