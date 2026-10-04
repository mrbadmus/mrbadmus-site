# SPEC-E / "Prompt X" — fair scores on reopened homework — apply sheet

**Nothing in here has been run against production.** Everything below was
applied to and driven on the TEST project (`qeppkiswvclkkwbxmlok`, "mrbadmus-test").

Production ref is **`urklkrwevjtlfbwnipjn`** ("mrbadmus", ends in **N**).

**Mide rules the prod apply.** This migration sits parked on branch
`feat/x-mig-reopen` until he says to apply it.

## 1. What this adds

One migration: `supabase/migrations/20261004010000_x_reopen_fair_scoring.sql`
(rollback: `supabase/rollbacks/20261004010000_x_reopen_fair_scoring_rollback.sql`).

- `assignment_submissions.answers_revealed_at` (timestamptz), `.latest_score`
  (smallint) — both nullable, additive.
- `assignment_question_attempts.first_option_letter` (text),
  `.first_is_correct` (boolean), `.first_answered_at` (timestamptz),
  `.answered_at` (timestamptz) — all nullable/defaulted, additive.
- Three trigger functions + their triggers (`mrb_attempt_resolve_correctness`,
  `mrb_attempt_track_first_answer` on `assignment_question_attempts`;
  `mrb_submission_before_write` on `assignment_submissions`).
- A one-time backfill of the new attempt/submission columns from existing
  data, run BEFORE the triggers are created (so the backfill cannot be
  blocked by the triggers' own immutability rules).
- `REVOKE INSERT, UPDATE ON assignment_question_attempts FROM authenticated`
  (closes a real hole — see below) and a column-level `REVOKE UPDATE
  (answers_revealed_at, latest_score) ON assignment_submissions FROM
  authenticated` (kept as defence in depth; see the migration's own comment
  for why it is a no-op today under Supabase's blanket table grant).

No existing column is dropped, renamed or retyped. `score`/`max_score` keep
their names; only what WRITES `score` changes (the new trigger, not the
backend's `rescore()`, has the final word on it for an MCQ-composed
assignment).

## 2. Deploy-order safety

The frontend (`feat/x-reopen`) and backend (`feat/x-reopen`, backend repo)
branches both probe for the new columns before selecting them (PostgREST
400s a WHOLE select on one unknown column) and fall back to pre-migration
behaviour when they are absent. So:

- **Migration first, code later**: every reader on main keeps working
  exactly as today (nobody selects the new columns yet) — AND every MCQ
  submission's `score` immediately becomes the fairer, counted figure,
  because that is a property of the TRIGGER, not of any application code.
- **Code first, migration later**: every probe reports "not supported",
  `isRevised()` uses the old heuristic, `latest_score` is never read. No
  400, no behaviour change, no outage.
- **Both at once**: the intended end state — truthful labels, `latest_score`
  visible in the raw API payload, score fairness live.

There is no unsafe ordering.

## 3. Correctness is resolved from the question bank

`assignment_questions` carries no answer key of its own — only `source_ref`
(the bank row's own `id`) and `band`. The trigger resolves `is_correct` by
joining `source_ref` to `ks3_assignment_bank` or `ks4_assignment_bank`,
chosen by `assignments.key_stage`. Verified on TEST before writing the
trigger: of ~150 sampled `assignment_questions` rows, 100% resolved to the
bank matching their class's key stage, zero cross-matches (see the
migration's PART 2 comment). When a bank row can no longer be resolved (a
retired question), the trigger changes nothing — the client-sent value is
kept exactly as before this migration.

## 4. What this closes, and what it deliberately does not

- **Closed**: a pupil's browser can no longer INSERT/UPDATE
  `assignment_question_attempts` at all (checked: no legitimate frontend
  code path in `shared/*.js` ever writes that table — every write goes
  through the backend's service-role key).
- **Closed by the trigger, not by a grant**: `score`/`latest_score`/
  `answers_revealed_at` on `assignment_submissions` are DERIVED — whatever
  a client (or the backend's own `rescore()`) writes to them is overridden
  before the row is stored, for every MCQ-composed submission. Proved live
  on TEST by impersonating the real pupil role (see §6) and sending `score:
  999` directly: the stored row came back `0`.
- **NOT closed**: there is no table-level REVOKE narrowing
  `assignment_submissions` itself, because a REAL, LIVE feature
  (`writeFinishedSubmission` in `shared/student-live.js` — flashcard
  homework completion, shipped 1 Oct 2026) legitimately writes `score`/
  `max_score`/`status`/etc. to that table directly from the pupil's own
  browser, with NO backend involved. Narrowing the grant would need
  enumerating every column every legitimate writer needs across both the
  pupil and staff paths — out of this ticket's scope, and not attempted.

## 5. Backfill — what changed, and the one honest limit

Run as one-time, idempotent SQL before any trigger existed (so it could not
be blocked by them). On TEST (117 submissions, 14 complete, 1 demonstrable
"revised" row at `34d4cd62…` plus the 6 flagged by the pre-existing
heuristic):

- Every complete MCQ submission's `score`/`latest_score` were recomputed.
  For every row that was never genuinely revised, the two came out equal to
  each other and to the PRE-backfill `score` — zero visible change.
- **One row changed materially**: `65e2615a-9fbe-42e0-a86f-ee9cdb1f4e53`
  went from `score=5` to `score=0`. Investigated: its `completed_at` (23 Sep)
  predates its attempts' `created_at` (30 Sep) by a week — an impossible
  ordering for a real pupil (you cannot complete a set before answering its
  questions), and a clear TEST-fixture artefact (a seeded/backdated
  `completed_at` with real-time attempt rows), not a live defect. Flagged
  here rather than silently left; **this exact row should be checked by
  hand before (if ever) treating TEST row counts as a baseline for anything
  else.**
- **Unrecoverable, as SPEC-E's own investigation anticipated**: for a
  submission already revised BEFORE this migration ran, the backfilled
  `first_option_letter`/`first_is_correct` necessarily carry the LATEST
  (already-overwritten) answer, because that is all the pre-migration data
  ever recorded under that row. `first_answered_at` is correct in every
  case regardless (upsert never touches `created_at`). On TEST this affects
  whichever of the pre-existing "revised" rows are genuine (not the
  backdated-fixture one above) — a handful out of 14 complete rows; the
  investigation's own prod figure was exactly one submission
  (`5d00390b…`).

## 6. Proof on TEST — the central scenario, live

Two throwaway assignments (one KS3, one KS4), soft-deleted after use
(`deleted_at`) because this session's SQL connector declined every `DELETE`
it was asked to run unattended — see §7.

**KS3** (class `6d6197fb-…`, real bank question `b8-02-s32`, correct = A):

1. Answered WRONG (B), with a spoofed `is_correct: true` sent as if from the
   browser → stored row: `is_correct: false`, `correct_option_letter: 'A'`,
   `correct_answer` the bank's real text — the server ignored the spoof.
2. `rescore()`-equivalent UPDATE tried to set `score: 1` → stored `score: 0`.
3. Marked complete → `answers_revealed_at` stamped by the DB.
4. >2s later, revised to the CORRECT answer (A), with a SECOND spoof
   (`is_correct: false`, `correct_option_letter: 'Z'`) → stored row:
   `is_correct: true`, `correct_option_letter: 'A'` — spoof ignored again;
   `first_option_letter`/`first_is_correct` unchanged (`B`/`false`);
   `answered_at` advanced past the reveal.
5. `rescore()`-equivalent UPDATE → **`score: 0` (unchanged), `latest_score: 1`
   (risen)** — THE CENTRAL PROOF.
6. A second, previously-blank question (`b8-02-e01`) answered CORRECTLY
   after the reveal → `score` stayed `0`, `latest_score` became `2` — proves
   the "answer a previously blank question after hand-in" path too.

**KS4** (class `2a000000-…`, real bank question
`ks4-eukaryotes-prokaryotes-h01`, correct = C): same spoof-defeat proof
repeated for the other bank/branch of the trigger — `is_correct`/
`correct_option_letter`/`correct_answer` all correctly resolved to C/`×6000`
against a spoofed A/`×6`.

**RLS impersonation** (as the real pupil `f3260000-…-000011`, via
`request.jwt.claims` + `set local role authenticated`, no password needed):

- `UPDATE assignment_question_attempts SET is_correct = true …` →
  **`permission denied for table assignment_question_attempts`** (the REVOKE
  works).
- `UPDATE assignment_submissions SET score = 999, latest_score = 999 …` →
  the grant allows the WRITE (RLS passes, the pupil owns the row) but the
  row returned by the same statement reads **`score: 0, latest_score: 2`**
  — the trigger overrode it before storage.
- `UPDATE assignment_submissions SET answers_revealed_at = '2099-01-01' …`
  → stored value unchanged, still the real reveal instant.

**Flashcard safety** (real live submission `0c7d54f6…` on flashcard
assignment `1df990b3…`, wrapped in `BEGIN…ROLLBACK` so nothing persisted):
`UPDATE … SET score = 7, max_score = 7` → returned **`score: 7, max_score: 7,
latest_score: NULL`** — passed through untouched, because the assignment has
zero markable `assignment_questions` rows. No regression to the live
flashcard-homework feature.

## 7. Rollback

`supabase/rollbacks/20261004010000_x_reopen_fair_scoring_rollback.sql`
reverses grants → triggers → functions → columns, in that order, and is
proved correct BY INSPECTION rather than by running it on TEST: this
session's SQL connector declined every `DROP TRIGGER`/`DROP FUNCTION`/
`DELETE` statement it was asked to run unattended ("destructive statements
may require the user to confirm"), with no interactive channel available to
confirm them. A future session with interactive confirmation (or Mide
running it by hand) should execute the rollback on TEST once before trusting
it on production, per the standing rule.

**Known TEST residue from this same restriction** — six rows this session
could not physically delete, all provably unreachable by any real app code
(their parent rows are soft-deleted, `deleted_at` set):

```sql
-- assignment_questions (3 rows, KS3 Q1/Q2 + KS4 Q1 of the throwaway sets)
delete from assignment_questions where id in (
  'c284eeee-aa63-4020-a202-8c411dc3a477', '69748fb2-6fd9-403d-a18d-18a2918d6309',
  'd6629bf5-3ad4-4005-972b-9cccb91f1343');
-- assignment_question_attempts (3 rows, same sets)
delete from assignment_question_attempts where id in (
  'ef7134ef-e4ce-43db-9ef2-5a4ac6696ea5', '7a11b69f-2b40-43b1-b89d-4ecea10745ea',
  'a31c9fe9-f422-4cce-8378-3c89bc461924');
-- then the two soft-deleted parent assignments and their submissions can be
-- hard-deleted too, if wanted (not required — deleted_at already hides them):
delete from assignment_submissions where id in (
  'c05304c9-f1d0-4120-b9d7-df731d3b05ae', 'abc083f9-637d-4d9e-8712-5ebba7bfb554');
delete from assignments where id in (
  'd03bef5b-69b0-42a9-838c-b5b0ed7669d1', '9b491d09-121b-485d-aec6-7f38a42f9bdb');
```

## 8. Verification queries (run after applying to production)

```sql
-- 1. the columns exist
select column_name from information_schema.columns
 where table_name in ('assignment_submissions','assignment_question_attempts')
   and column_name in ('answers_revealed_at','latest_score','first_option_letter',
                        'first_is_correct','first_answered_at','answered_at');
-- expect 6 rows

-- 2. the triggers exist and are enabled
select tgname, tgenabled from pg_trigger
 where tgname in ('trg_10_attempt_resolve_correctness','trg_20_attempt_track_first_answer',
                   'trg_submission_before_write');
-- expect 3 rows, tgenabled = 'O'

-- 3. the hole is closed
select has_table_privilege('authenticated','assignment_question_attempts','INSERT') as can_insert,
       has_table_privilege('authenticated','assignment_question_attempts','UPDATE') as can_update;
-- expect false, false

-- 4. no complete MCQ submission is left with a NULL score
select count(*) from assignment_submissions s
 where s.status = 'complete' and s.score is null
   and exists (select 1 from assignment_questions aq
                where aq.assignment_id = s.assignment_id and aq.band is not null);
-- expect 0
```

## 9. Fingerprints and the step after applying (added by the commander, 4 Oct 2026)

| file | md5 (file bytes) |
|---|---|
| `supabase/migrations/20261004010000_x_reopen_fair_scoring.sql` | `a2f85b26a5ed478112f4d13de2a214c2` |
| `supabase/rollbacks/20261004010000_x_reopen_fair_scoring_rollback.sql` | `ea08fe5cfced11b274890ef71b358b4d` |

Production pre-check (read-only, 4 Oct 2026): neither `assignment_submissions`
nor `assignment_question_attempts` carries ANY non-internal trigger, and none of
`mrb_attempt_resolve_correctness` / `mrb_attempt_track_first_answer` /
`mrb_submission_before_write` exists — this migration creates, it does not
replace, so there is no production body to rebuild from.

Production replay (read-only, 4 Oct 2026): the correctness trigger's rule was
run as a SELECT over every one of production's 168 answered
`assignment_question_attempts` rows — 168/168 agree with the stored
`is_correct`, 0 unresolved. Applying this changes no existing mark.

**After applying: restart the Render service** (Manual Deploy → "Restart" or
redeploy the same commit). `server.js`'s `revealColumnsSupported()` caches a
definite "columns absent" for the life of the process, so until a restart the
backend keeps the old "revised" heuristic and does not return `latest_score`.
The TEACHER's score is fair the moment the SQL lands regardless — the trigger
computes it — the restart only switches on the truthful "Changed after answers
shown" label and the "Now X / Y" line. `shared/breakdown.js` probes per page
load and needs nothing.
