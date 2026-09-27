# MRB-351 (flashcard homework) — migrations apply order

Stream B of the MRB-351 landing (27 Sep 2026). This is the migrations-only
worktree; the site (`shared/*.js`, `teacher/*`, `student/*`) and the backend
routes are separate streams and land separately. See `docs/mrb351/REPORT.md`
(on `origin/claude/flashcard-homework-feature-c2thi1`) for the full feature
build, and `docs/experience/REPORT.md`'s "The parked migration" section on
`origin/main` for why `teacher_class_rollup_v2` exists at all.

⊕ 27 Sep 2026, same day — an Opus review of this branch (before it shipped)
found three things wrong and one flake. All four are fixed here; see
"The Opus review fixes" below. Migration 3 and its rollback both changed;
migrations 1/2 did not.

## Apply, in this order

| # | file | md5 |
|---|---|---|
| 1 | `supabase/migrations/20260924180000_mrb351_flashcards_schema.sql` | `07af0b37e17ffb323baea00001889b06` |
| 2 | `supabase/migrations/20260924180100_mrb351_flashcards_functions.sql` | `0bf90094e1b51de80cfc9f0cf24c461b` |
| 3 | `supabase/migrations/20260927100000_mrb351_rollup_v2_live_results_kinds.sql` | `ab4aa701bb39659b81b246b3172a0e4f` |

md5s above are `md5 -q` of the files as committed on `feat/mrb351-migrations`
after stream J (27 Sep 2026, corrected pass). Migrations 1 and 2 are
byte-identical to the first landing session (same md5s as before). Migration
3's `in_week`/`on_time_week` window-boundary OPERATORS are unchanged from
`1077b3e6e` — the `> week_start AND <= week_end` pair was correct all along
(see "The stream J fixes" below) — so its only real difference from
`1077b3e6e` is the two `LAST_ACTIVE_RULE.md` → `supabase/MRB351-APPLY.md`
doc-pointer edits. Its md5 nonetheless differs from every value recorded
earlier in this document (`db60ff77…`, and the two below) because NONE of
those were actually the hash of this file's literal bytes — see the note in
"TEST rehearsal, stream J" about what `execute_sql` was really sent each
time.

Migrations 1 and 2 are the flashcard schema and server-side functions,
brought onto this branch byte-identical to the flashcard-homework branch
(`claude/flashcard-homework-feature-c2thi1`, commit `22b442dde`) — nothing in
either file was changed. Migration 3 is new for this landing: it supersedes
BOTH `20260924180200_mrb351_rollup_kind.sql` (which is **not** carried onto
this branch — it edited `teacher_class_rollup` v1 in place, and v1 must stay
exactly as production has it) and the parked
`20260924010000_rollup_live_results.sql` on `feat/rollup-live-results`
(commit `b734f03ba`, md5 `112d63fbb9440bd8faca02c0efffff41`) — Mide's 23 Sep
2026 "results are live" ruling with NO flashcard awareness. Migration 3 is
that live-results `teacher_class_rollup_v2` PLUS the flashcard kind split
folded in: a flashcard cell counts as a cell everywhere (sub/on_time/late/
unknown/off_roster/submissions_completed/last_activity_at/in_week/
missing_marked) but is never graded (never in marked_n/mean/class_mean/avg),
PLUS the two `last_at` fixes from the Opus review (below). Full reasoning is
in migration 3's own header comment.

Migration 3 must apply strictly after 1 and 2 — it reads `assignments.kind`
(migration 1) and `flashcard_sessions` (migration 1's schema, populated by
migration 2's `flashcard_record`).

## Rollback, in reverse order

| # | file | md5 |
|---|---|---|
| 1 | `supabase/rollbacks/20260927100000_mrb351_rollup_v2_live_results_kinds_rollback.sql` | `6597512ee4606e66cfb521139b7616fa` (unchanged) |
| 2 | `supabase/rollbacks/20260924180100_mrb351_flashcards_functions_rollback.sql` | `eb57a5e59b014824c37fcbd75e3c4e16` (was `44bfc929784c2fc00a761db3de82fa99` — added its own `schema_migrations` delete) |
| 3 | `supabase/rollbacks/20260924180000_mrb351_flashcards_schema_rollback.sql` (⚠️ LOSSY — read its own header before running it; it hard-deletes every flashcard deck, card, assignment and pupil event) | `97226103c69c5527902521b2e0e58187` (was `4a6c6287053658523186dd09334c97bb` — expanded LOSSY header, the production FK sweep note, and its own `schema_migrations` delete) |

Apply by hand only — the Supabase CLI never reads `supabase/rollbacks/`.

## The Opus review fixes (27 Sep 2026, same day, before this branch shipped)

1. **`last_at` was cells-only, and the JS had already moved on.** Stream I
   (25 Sep 2026, experience run item 7, `feat/mrb351-landing` commit
   `c2fde3a12`) changed `buildRoster`'s `lastIso` to read `activity[]`
   instead of `stamp[]`: a pupil mid-way through an open paper
   (`started_at` set, no `completed_at` yet) has no cell at all
   (`cellOf` returns null for one) and was invisible to the old rule. D's
   v2 — and this migration's own first draft — still computed `last_at` as
   `MAX(c.stamp)` over `cells` only. Fixed with a new `activity` CTE: for
   every first attempt, activity is the cell's own stamp when it IS one, or
   `started_at` when it is not (yet) one. `first_attempts` grew one column
   (`s.started_at`) to support this. The proof script's `activity_at()`
   mirrors it line for line.
2. **A flashcard sitting wrote no activity at all.** A deck writes no
   `assignment_submissions` row until every card is secured (MRB-351 §1),
   so a pupil several sittings into an unfinished deck had NO activity
   signal whatsoever — worse than the MCQ case, because there is no
   eventual "in progress" row to fall back to either. Fixed with a new
   `flashcard_activity` CTE folding in
   `MAX(flashcard_sessions.last_seen_at)` over the class's own non-deleted,
   released flashcard assignments, combined with source 1 via `GREATEST()`.
   The exact rule (for the site stream's JS twin) is written up in full
   under "The last-activity rule" below — it also answers "can a teacher's
   RLS read `flashcard_sessions` for their class" (yes, confirmed both from
   the migration file and from TEST's live `pg_policies`). ⚠️ A standalone
   `LAST_ACTIVE_RULE.md` was named here and in code comments in the first
   landing session but never actually written; stream J (27 Sep 2026)
   inlined the rule into this document instead and repointed every comment
   that named the missing file (`teacher-live.js`, `teacher-data.js`
   already pointed here; this migration and the proof script named the
   phantom file until now).
3. **Rollback 1 could FK-fail on real data.** `submission_feedback.
   submission_id -> assignment_submissions(id) ON DELETE RESTRICT` and
   `assignment_question_attempts.submission_id -> assignment_submissions(id)`
   (defaults to RESTRICT, no ON DELETE clause) both hard-fail the rollback's
   `DELETE FROM assignment_submissions` the moment a single feedback row or
   attempt row references a flashcard submission. Checked against
   `pg_constraint` on TEST for every FK into `assignment_submissions`/
   `assignments` — these were the only two rollback 1 did not already
   handle (the four `flashcard_*` tables' own FKs into `assignments` are
   moot because rollback 1 drops those tables outright, before deleting any
   `assignments` row). Fixed: rollback 1 now deletes matching
   `submission_feedback` and `assignment_question_attempts` rows first.
   ⊕ Re-swept read-only against PRODUCTION too (stream J, 27 Sep 2026): the
   only FK production adds beyond that pair is `assignment_questions.
   assignment_id -> assignments(id) ON DELETE CASCADE`, harmless in practice
   (flashcard assignments have no `assignment_questions` rows — that table
   is the MCQ/ladder question-bank link) but real, and now named in
   rollback 1's own header rather than left implicit. Rollback 1's LOSSY
   header now lists every table and row class it deletes or drops, not just
   the three it originally named. Rollbacks 1 and 2 now also delete their
   own `supabase_migrations.schema_migrations` row by version-or-name, the
   same pattern rollback 3 already used — neither did before this pass, so
   a full rollback left two of the three migrations still "applied" as far
   as the CLI's own bookkeeping was concerned.
4. **The MCQ fixture was day-of-week sensitive.** Its "marked" paper's
   `due_at` was `now - 3 days`, and whether that landed inside or outside
   the CURRENT teaching week's 7-day window depended on where "now" sat in
   the week when the fixture happened to run — true by luck on 24 Sep 2026,
   false on 27 Sep, with no code change in between. Fixed: `due_at` is now
   `now - 8 days`, which is provably outside the window on ANY day
   (`window = [start, start+7d)`, `now` always inside it, so
   `now - 8d < start - 1d < start` for every possible position of `now`).
   The dependent submission timestamps (p0/p1/p2/o1 on that paper) shifted
   by the same +5 days to keep their relative gaps — and the
   is_late-by-comparison results for p2/o1 — unchanged. The by-hand
   `week0`/`flagged`/`p0.in_week` values were recomputed for the new,
   permanent placement rather than re-guessed. Fixture mode is now green on
   every run, with nothing excused.

The proof script also gained three new fixture assertions the review asked
for, all green: an in-progress MCQ row's `started_at` showing as `last_at`
(the mrb348r3 class), a flashcard sitting outranking an existing MCQ
completion for the same pupil in the same class (same class, a 5th
"flashcard probe" assignment, inert on every other hand value), and a pupil
whose ONLY activity signal in a class is a flashcard sitting
(`fixture_flashcards()`'s `p_missing`).

## The stream J fixes (27 Sep 2026, second pass, before this branch merges)

A second review of this same branch, before it merges, checked one
correctness question, found it already answered correctly, then found a
fixture bug the checking itself surfaced, plus two documentation gaps.
Migration 3 changed only in comments (the window-boundary OPERATORS did not
move — see item 1; the diff against `1077b3e6e` for `in_week`/`on_time_week`
is nil); the two schema/functions rollbacks changed (not migrations 1/2
themselves); this document and the proof script changed.

1. **The week-window boundary was checked, and confirmed correct as it
   stood.** A first pass of this review misread `buildMatrix`'s literal
   `>=`/`<` operators as the target and proposed moving the SQL to
   `[week_start, week_end)` to match them syntactically. That was wrong: the
   two operators are not the two sides' real agreement. `p.due_at >=
   pack.week.start_at && p.due_at < pack.week.end_at` compares raw ISO
   STRINGS in the browser, and PostgREST's `…+00:00` vs
   `Date.toISOString()`'s `…000Z` tie the OPPOSITE way at an exact instant
   match ('+' 0x2B sorts before '.' 0x2E) — so the page's actual, effective
   boundary is `(week_start, week_end]`: a due date tied to the window's
   start reads as NOT this week (it belongs to the week that is ending), one
   tied to its end reads as IN this week. That is exactly what
   `c.due_at > cls.week_start AND c.due_at <= cls.week_end` already computed,
   and it is also the sensible reading on its own terms — a deadline at the
   stroke of the week's end is that week's work, not next week's. **No SQL
   change was needed**; the diff against `1077b3e6e` for `in_week`/
   `on_time_week` is nil. Four new fixture assertions pin the boundary
   directly rather than leaving it to a comment: a paper due exactly at
   `week_start` (NOT in week) and exactly at `week_end` (in week), for both
   an MCQ paper and a flashcard deck, each built, asserted and torn down in
   isolation against class `mrb348r3`'s existing clean pupil. The proof
   script's own `in_win` now parses `due_at`/`start_at`/`end_at` into real
   instants before comparing (via a new `parse_iso()` helper) rather than
   comparing the raw strings the JS does — asserting `(start, end]`
   EXPLICITLY, on real instants, is what actually proves the SQL matches the
   browser's effective behaviour, rather than mirroring a format-dependent
   string tie that happens to land the same way on this one pair of ISO
   shapes.

   **SQL and the live page both use `(week_start, week_end]`.** The JS gets
   there through a string comparison of two different ISO formats, which is
   fragile — a future change to either format (or a browser/runtime that
   formats `toISOString()` differently) could silently move the boundary out
   from under it with no code change and no test failure on the JS side.
   Hardening `shared/teacher-live.js` to compare parsed instants directly,
   with the same explicit `(start, end]` rule, is a real follow-up — but it
   is a site-stream change to a file this migrations-only worktree does not
   touch, and is not part of this landing.
2. **The new fixture that PROVED item 1 had a day-of-week bug of its own.**
   Two of the four boundary-test papers relied on being naturally `closed`
   (`due_at <= now`) to stop the "open paper is in-week regardless of due
   date" branch (item 5's ruling) from swallowing the due-date test they
   exist to isolate. That relies on `now` sitting inside
   `[week_start, week_end)` — true most days, false on a SUNDAY, because
   MRB-330 moves the computed window forward to the day ahead ("Sunday
   belongs to the week that is coming"), leaving `now` BEFORE `week_start`.
   This session ran on a Sunday (27 Sep 2026), so the "start"-boundary
   papers were never closed, the open-bypass fired regardless of the fix
   being tested, and both assertions read `in_week = True` when the (correct)
   SQL and the (correct) test both wanted `False`. Exactly the trap the Opus
   review's fix #4 hit on a different paper, in a different session. Fixed
   by giving ALL FOUR boundary papers a far-future `release_at`
   (`marked = False`), not only the "end" pair, so `in_week` can only come
   from the due-date window test being proved, on any day of the week,
   forever. Full account in "TEST rehearsal, stream J" below.
3. **Rollbacks 1 and 2 never deleted their own `schema_migrations` row.**
   Rollback 3 always has (`delete from supabase_migrations.schema_migrations
   where version = … or name = …`); rollbacks 1 and 2 did not, so a full
   3→2→1 rollback left two of the three migrations still recorded as
   applied. Both now delete their own row, same pattern, same
   version-or-name match (the MCP connector has been observed stamping its
   own timestamp rather than the file's — see rollback 3's own comment).
4. **The `LAST_ACTIVE_RULE.md` this document, the migration and the proof
   script all pointed to was never actually written.** The site worktree's
   `teacher-live.js`/`teacher-data.js` already point at "the last-activity
   rule in `supabase/MRB351-APPLY.md`" — correct, once this section below
   existed. Every other pointer (this file's fix #3 above, the migration's
   `activity`/`flashcard_activity` CTE comments, the proof script's own
   comments) named the phantom standalone file; all repointed here.

## The last-activity rule

A pupil's `last_at` (what every class-summary card and the class-detail page
show as "last active") is the LATEST of two sources, taken with `GREATEST()`
(NULL-safe: either side missing is simply ignored, both missing is `NULL`,
"no activity yet"):

1. **Every first-attempt MCQ/topic-quiz row's own activity instant** — the
   cell's completion stamp (`COALESCE(completed_at, submitted_at)`) when the
   row IS a cell (`completed_at`/`submitted_at` is set, or `status =
   'complete'`); otherwise its `started_at`, so a pupil mid-way through an
   open paper still shows as active even though `cellOf` returns nothing
   for them yet. One row per (class, pupil) — `MAX()` over every
   assignment's first attempt.
2. **`MAX(flashcard_sessions.last_seen_at)`**, over every flashcard
   assignment in the SAME class that is both non-deleted and released
   (`release_at IS NULL OR release_at <= now`) — a flashcard SITTING is
   activity in its own right, even before the deck is finished. A deck
   writes NO `assignment_submissions` row until every card is secured, so
   without this second source a pupil several sittings into an unfinished
   deck would have no `first_attempts` row and no activity signal at all —
   worse than the MCQ in-progress case, which at least has an eventual
   "in progress" row to fall back to.

The SQL twin is `teacher_class_rollup_v2`'s `activity` CTE (source 1) and
`flashcard_activity` CTE (source 2), combined via `GREATEST(act_last.
last_activity_at, fc_last.last_activity_at)` in `per_student`
(`20260927100000_mrb351_rollup_v2_live_results_kinds.sql`). The JS twin is
`buildMatrix`'s `row.activity` (source 1, `shared/teacher-live.js`) and
`pack.flashcardLastActive[sid]` (source 2, computed in
`shared/teacher-data.js`'s `loadClassMatrices`, from the SAME
non-deleted/released scoping the SQL uses), combined the same way in
`matrixFromRollup`/the roster build. `mrb348_teacher_rollup_proof.py`
mirrors both in `activity_at()` (source 1) and the `flashcard_last_seen`
loop in `js_values()` (source 2).

A teacher's RLS can read `flashcard_sessions` for their own class — confirmed
both from the migration's own policies and from TEST's live `pg_policies` —
so this is a normal authenticated read, not something routed through the
`SECURITY DEFINER` rollup only.

### Stale tabs

A teacher's tab that probed for the `kind` column or `teacher_class_rollup_v2`
BEFORE this migration set landed caches that probe's negative result — the
site's "does this backend support Flashcards yet" check has a client-side
`sessionStorage` TTL, so **Flashcards can stay hidden in an already-open tab
for up to 10 minutes after the apply**, or until the teacher opens a NEW tab
(which probes fresh). This is expected, not a rollout failure: do not chase a
report of "I don't see Flashcards yet" from a tab that has been open since
before the migrations landed without first asking the teacher to reload.

## What this migration does NOT touch

`public.teacher_class_rollup` (v1, `20260922231500`) is never edited by
anything on this branch. Rehearsed on TEST: after the full forward-rollback-
forward cycle below, `md5(prosrc)` of v1 is `76419b38e96c77271ff4ee035a713ffb`
on TEST, matching production's `76419b…` exactly (confirmed by a read-only
production `SELECT md5(prosrc) FROM pg_proc WHERE proname =
'teacher_class_rollup'`, in the first landing session; not re-run this
session since TEST's own v1 body was already re-confirmed unchanged).

Nothing on `origin/main`'s SITE code calls `teacher_class_rollup` (v1)
directly — only `teacher_class_rollup_v2`, via `shared/teacher-data.js`'s
`loadClassSummaries` (`sb.rpc('teacher_class_rollup_v2', ...)`, one call
site, with a fallback to the full submissions read on any error). v1 is kept
only because a live production migration is never allowed to drop a function
that might still be called from an in-flight request or an older deployed
bundle, per the standing "sits beside, never replaces" pattern.

## Edge functions (land via the site branch, not this one)

`supabase/functions/flashcard-extract` and
`supabase/functions/flashcard-answer-check`, both importing
`supabase/functions/_shared/flashcards/`, are part of the flashcard-homework
feature build but are not present in this migrations-only worktree — they
live on `main` via the site stream's branch (the site worktree in this
landing is `feat/mrb351-landing`).

**Deploy AFTER migrations 1 and 2** (they read `assignments.kind`/
`flashcard_decks` etc.), not before, and not bundled with migration 3
(migration 3 is a SQL-only rollup change with no edge-function dependency).

**verify_jwt.** Both functions are live on TEST with `verify_jwt: true`
(confirmed via `list_edge_functions` on `qeppkiswvclkkwbxmlok`, 27 Sep 2026 —
`flashcard-extract` id `85ff1ed7-e74b-4054-a3f0-4e505493c0c4`,
`flashcard-answer-check` id `2c97afb8-78f5-4ab4-998f-eefc16e3d38e`, both
`"verify_jwt":true`). `supabase functions deploy` defaults to
`verify_jwt: true` unless `--no-verify-jwt` is passed, so deploying with NO
extra flag reproduces TEST's setting exactly — do not add
`--no-verify-jwt`.

**Command form**, from a `main` checkout of the SITE repo (not this
migrations worktree — the functions do not exist here):

```
supabase functions deploy flashcard-extract --project-ref urklkrwevjtlfbwnipjn
supabase functions deploy flashcard-answer-check --project-ref urklkrwevjtlfbwnipjn
```

**`ANTHROPIC_API_KEY` is Mide's to set, as an edge-function secret, never
written to any file, migration, `.env`, or committed anywhere in either
repo.** He sets it himself, once, after these two functions are live on
production:

```
supabase secrets set ANTHROPIC_API_KEY=... --project-ref urklkrwevjtlfbwnipjn
```

Without it, the model-marking path (`flashcard-answer-check`'s free-text
grading) answers `no_api_key` rather than a mark — a soft-fail, not an
error — and the non-model paths keep working regardless: table extraction
and Q:/A: pairing in `flashcard-extract` need no model call at all, so a
teacher can build and assign a deck from a table or a Q:/A: paste before the
key is ever set.

## TEST rehearsal, 27 Sep 2026 (Opus review session — superseded by stream J below)

⊕ This section's own `teacher_class_rollup_v2` md5 (`bd503c56…`) is now STALE
— stream J's window-boundary fix changed the function's text again after
this rehearsal ran. Kept here as the record of what the Opus review pass
proved; "TEST rehearsal, stream J" below is the current state.

- Applied the fixed migration 3 directly (`CREATE OR REPLACE`, idempotent)
  over the already-forward state from the first landing session; proved
  both fixtures and real-classes mode green; then did a FULL
  forward → rollback → forward cycle to prove the fixed rollback 1 (with
  the new FK-safety deletes) round-trips cleanly and the rebuilt schema is
  identical:
  - Rollback (3 → 2 → 1): the new `submission_feedback`/
    `assignment_question_attempts` deletes in rollback 1 ran cleanly (0 rows
    matched — TEST held 0 flashcard assignments at rollback time, so this
    proves the SQL is valid and ready, not that it was exercised against
    real referencing rows). Confirmed clean afterwards: no
    `assignments.kind`, no `flashcard*`/`mrb351_*` tables or functions, v1's
    `md5(prosrc)` still `76419b…`.
  - Forward again (1 → 2 → 3): confirmed shape (columns, tables, functions).
    `teacher_class_rollup_v2`'s `md5(prosrc)` is `bd503c56e9b144e33e14183d87e0766f`
    (this is the FIXED body — different from the pre-review value, as
    expected, since the function's text genuinely changed).
- `mrb348_teacher_rollup_proof.py` (extended for the kind split AND the two
  `last_at` fixes, with the mrb348r3 fixture's day-sensitivity removed and
  three new assertions added): **fixture mode 104/104 (mrb348r3 class) +
  51 generic cells/13 flashcard-specific assertions
  (`fixture_flashcards()`) — 0 mismatches, 0 excused, both fully green.**
  Real-classes mode across three readers (a 5-class teacher, a 1-class
  teacher, an HOD): **1043/1043, 0 mismatches.**
- TEST left in the FORWARD state, no residue: zero `mrb351%`/`mrb348r3%`
  leftover rows, zero flashcard assignments, zero `flashcard_sessions` rows,
  zero throwaway classes. `schema_migrations` carries exactly one row per
  migration (the three above), duplicates from BOTH rounds of the
  round-trip rehearsal cleaned up.

## TEST rehearsal, stream J, 27 Sep 2026 (corrected pass — current)

Full cycle, exact committed file bytes, via the Supabase MCP's `execute_sql`
(no CLI, no `apply_migration` — this session's brief named `execute_sql` and
`list_edge_functions` only), each forward step followed by a manual
`insert into supabase_migrations.schema_migrations` matching the file's own
version/name, exactly mirroring what `supabase db push` would record.

⚠️ **Every `md5(prosrc)` recorded anywhere earlier in this document for `v2`
(`db60ff77…`, `bd503c56…`, `55547774…`) is now known to be the hash of
whatever text a PREVIOUS `execute_sql` call happened to send, not necessarily
the literal migration file's bytes** — an earlier pass in this same session
re-typed the function body with its comments stripped, and it is now clear
at least one prior session did too, since the two "exact file, comments
included" applies below (window-operators reverted, then again after the
boundary-expectation correction) land on the SAME hash both times
(`e33f558d…`), and it differs from every value that came before it. The
lesson: a "record the md5(prosrc)" step is only meaningful when the text sent
to `execute_sql` is provably the file's own bytes (e.g. `awk` from `CREATE OR
REPLACE FUNCTION` to the closing `;`, piped straight into the call) — never
retyped from memory or "cleaned up" en route.

- **First revert (window-boundary operators back to `>` / `<=`, exact
  `1077b3e6e` text) applied with comments STRIPPED** (an artefact of typing
  the body out rather than piping the file) — landed on `bd503c56…`,
  coincidentally the SAME hash the prior session's own (also
  comment-light) apply had produced. Caught by inspecting `length(prosrc)`/
  `left(prosrc, 300)` on TEST and finding no comments in the stored body
  where the committed file has many.
- **Re-applied a second time, this time piping the file's own
  `CREATE OR REPLACE FUNCTION … ;` block verbatim** (`awk
  '/^CREATE OR REPLACE FUNCTION public.teacher_class_rollup_v2/,0'`) —
  `teacher_class_rollup_v2` `md5(prosrc)`: **`e33f558df97f6a89e42bd31d778de4d3`**.
  This is the first md5 in this document's history that is provably the hash
  of the committed file's own function body, comments included.
  `teacher_class_rollup` (v1) `md5(prosrc)`: **`76419b38e96c77271ff4ee035a713ffb`**
  — untouched throughout, matches production.
- **Coordinator caught a mis-ruling on the boundary direction** (see "The
  stream J fixes" item 1): the operators were reverted to exactly
  `1077b3e6e`'s `> week_start AND <= week_end`, and the proof's fixture
  expectations were flipped to match (`week_start` → NOT in week,
  `week_end` → in week). Re-running `--fixture` then surfaced a SECOND,
  independent bug in the fixture itself, unrelated to the SQL: two of the
  four boundary papers (the "start" pair) relied on `due_at <= now` making
  them naturally `closed`, which is only true when `now` is inside
  `[week_start, week_end)` — false on a SUNDAY (MRB-330: "Sunday belongs to
  the week that is coming" moves the computed window to the day AHEAD, so
  `now` sits BEFORE `week_start`). This session ran on a Sunday
  (27 Sep 2026), so the "start" papers were never closed, `marked AND NOT
  closed` was true regardless of the due-date test, and the open-bypass
  (item 5's ruling) swallowed the very boundary being tested — read
  `in_week = True` on both sides for a paper that should have been
  isolated to the due-date branch. Exactly the day-of-week trap the Opus
  review's fix #4 hit on a different paper. Fixed by giving ALL FOUR
  boundary papers a far-future `release_at` (`marked = False`), not only
  the "end" pair, removing the open-bypass from the equation entirely so
  `in_week` can only come from the due-date window test, on any day of the
  week.
- **`mrb348_teacher_rollup_proof.py --fixture`**: **mrb348r3 class —
  PASS, 104/104**, including the four corrected boundary assertions
  (`boundary end mcq` → in week, `boundary start mcq` → NOT in week,
  `boundary end fc` → in week, `boundary start fc` → NOT in week; all eight
  individual JS/SQL checks OK). `fixture_flashcards()` — **PASS, 51 generic
  cells + 13 flashcard-specific assertions**. Both fixtures torn down by
  their own snapshotted id lists: "0 fixture rows left behind" / class row
  count `0` after teardown.
- **`mrb348_teacher_rollup_proof.py`** (default, real-classes mode), the
  same three readers (5-class teacher, 1-class teacher, HOD): **1085 values
  compared, 0 mismatches** across all three.
- **TEST left FORWARD, 0 residue**, query-verified after the run: zero
  `assignments` titled `mrb348r3%`, zero `flashcard_sessions` rows, zero
  decks/classes left over from either fixture, `schema_migrations` holding
  exactly the three rows above and nothing duplicated.

## Verifying the apply — compare function bodies without comments

The Supabase MCP connector strips `--` comment lines from SQL it sends, so a
function applied through it has a different raw `md5(prosrc)` from the file
even when the logic is identical (TEST shows exactly this). Verify with the
comment- and whitespace-independent fingerprint instead. Run on the target
project after migrations 1–3:

```sql
select proname,
       md5(regexp_replace(regexp_replace(prosrc, '--[^\n]*', '', 'g'), '\s+', '', 'g')) as norm
  from pg_proc p join pg_namespace n on n.oid = p.pronamespace
 where n.nspname = 'public'
   and (proname like 'flashcard%' or proname like 'mrb351%' or proname = 'teacher_class_rollup_v2')
 order by 1;
```

Every row must equal this table, computed from the committed files (and equal
on TEST, 27 Sep 2026, all 15):

| function | norm |
|---|---|
| `flashcard_card_state` | `f072d908603a97cd12fdbaec414a66d1` |
| `flashcard_deck_duplicate` | `b6a673ba494e40f9e9d9b663685a249d` |
| `flashcard_deck_save` | `95ae87f37824c00bb42a2af37dad4bd3` |
| `flashcard_edit_assignment` | `5993f52636cd0e2ee071295cd303169f` |
| `flashcard_progress` | `2a7d33f329548c430af4213200aa849f` |
| `flashcard_pupil_detail` | `e1751dd5d7c5508df9983a2fd24cc905` |
| `flashcard_quick_check` | `da5faa5d97c30df324fdc7dd149ce47d` |
| `flashcard_record` | `27c38c1d17cc56761f19da52268c0e45` |
| `flashcard_set_work` | `1869c6d581e31ebd2627d34240b06a16` |
| `mrb351_active_between` | `9b4c1d4a24a024dc2eb217aecfc6a926` |
| `mrb351_deck_card_count` | `4456f8352ea5dbbf0dcf16539b0a0a7e` |
| `mrb351_session_refresh` | `e17219b5b6a9f445a9c593a0ffb1d117` |
| `mrb351_teacher_gate` | `0bedcdd0af9672e66740169259c779d4` |
| `mrb351_touch_updated_at` | `fa6e76dbdc52fe3c022e152185807dba` |
| `teacher_class_rollup_v2` | `e2735f6dba20e07949692d989c066dfc` |
