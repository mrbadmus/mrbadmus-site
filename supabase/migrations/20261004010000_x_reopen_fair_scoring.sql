-- SPEC E / "Prompt X" — fair scores on reopened homework (Mide's option A, 4 Oct 2026)
--
-- Pupils can reopen marked homework ("marked" is never a lock" — Sharpen C5,
-- 29 Sep 2026). This migration makes sure that once a pupil has been SHOWN
-- THE CORRECT ANSWERS, the score the TEACHER sees counts only answers given
-- BEFORE that reveal — entirely in the database, so it holds regardless of
-- which route (the live backend, the legacy /api/assignment-submit, or any
-- future caller) writes the row, and regardless of what a client sends.
--
-- Everything here is ADDITIVE (new nullable columns, new triggers) and is
-- gated so it can sit parked on a branch for days without being safe to run
-- against a server that doesn't know about it yet — see the frontend
-- probe-and-fallback notes in RESULT-E.md for the other half of that safety.
--
-- ───────────────────────────────────────────────────────────────────────
-- PART 0 — new columns
-- ───────────────────────────────────────────────────────────────────────

alter table public.assignment_submissions
  add column if not exists answers_revealed_at timestamptz,
  add column if not exists latest_score smallint;

comment on column public.assignment_submissions.answers_revealed_at is
  'Stamped by trg_submissions_before_write the first time this attempt becomes complete. The DB clock, never a client value. Immutable once set — see the trigger function body.';
comment on column public.assignment_submissions.latest_score is
  'count(is_correct) right now, for every markable question — "if I marked it today". NULL for a non-MCQ submission (e.g. a flashcard deck), which this feature does not touch. `score` stays the COUNTED (pre-reveal) figure every existing reader already expects.';

alter table public.assignment_question_attempts
  add column if not exists first_option_letter text,
  add column if not exists first_is_correct boolean,
  add column if not exists first_answered_at timestamptz default now(),
  add column if not exists answered_at timestamptz default now();

comment on column public.assignment_question_attempts.first_option_letter is
  'The letter this question was FIRST answered with. Immutable after insert — a revision can never change it.';
comment on column public.assignment_question_attempts.first_is_correct is
  'Whether the FIRST answer was correct, computed server-side from the question bank where the bank row can still be resolved (never trusted from the browser for a markable/band question). Immutable after insert.';
comment on column public.assignment_question_attempts.first_answered_at is
  'When this question was FIRST answered. Immutable after insert — note this is NOT the same column as `created_at`, which upsert leaves alone too, kept so the two can diverge safely if that ever changes.';
comment on column public.assignment_question_attempts.answered_at is
  'When the CURRENTLY STORED answer to this question was given — advances on a genuine revision (the selected letter changed), stays put on a no-op upsert of the same letter.';

-- ───────────────────────────────────────────────────────────────────────
-- PART 1 — one-time backfill, BEFORE any trigger exists to interfere
-- ───────────────────────────────────────────────────────────────────────
--
-- ⚠️ Honest limit, stated once here and again in RESULT-E.md: an answer that
-- was already overwritten by a revision BEFORE this migration ran cannot be
-- recovered. Its `first_is_correct`/`first_option_letter` below are backfilled
-- from whatever is CURRENTLY stored — which, for an already-revised row, is
-- the LATEST answer wearing the FIRST answer's name. `first_answered_at` is
-- still correct in every case (upsert never touches `created_at`). On
-- production as of 29 Sep 2026 this affects exactly one submission
-- (5d00390b…, found already flagged "revised" by the existing heuristic);
-- TEST's own count is checked and reported in RESULT-E.md.

update public.assignment_question_attempts
set first_option_letter = selected_option_letter,
    first_is_correct = is_correct,
    first_answered_at = created_at,
    answered_at = created_at
where first_answered_at is null or first_answered_at = answered_at; -- idempotent: a second run touches nothing new

update public.assignment_submissions
set answers_revealed_at = coalesce(completed_at, submitted_at)
where status = 'complete' and answers_revealed_at is null;

-- latest_score = count(is_correct) today, for every submission that belongs
-- to an MCQ-composed assignment (at least one markable `assignment_questions`
-- row). A flashcard/self-marked-only submission keeps latest_score NULL —
-- the gate every trigger below also uses, so backfill and triggers agree.
--
-- ⚠️ THE 2-SECOND SLACK IS THE SAME ONE server.js's `isRevised()` ALREADY
-- USES (`REVISED_SLACK_MS`), applied here for the SAME documented reason:
-- MRB-292's in-flight-answer race ("the last answer POSTed 240ms after
-- completed_at", one completion in four on production) means an answer's
-- `created_at`/`first_answered_at` can legitimately land a few hundred ms
-- AFTER `completed_at`/`answers_revealed_at` even though the pupil gave it
-- BEFORE the reveal — the drain and the completion race each other, and the
-- completion can win. A strict `<=` would exclude that answer from the
-- counted score purely because of request ordering, which is the opposite
-- of fair and is exactly the failure mode `REVISED_SLACK_MS` already exists
-- to absorb on the "was this revised" side. (TEST's own data separately
-- surfaced a FAR larger, unrelated gap on one fixture row — see RESULT-E.md
-- — which is a seeded-timestamp artifact, not this race, and is not fixed
-- by this slack.)
with mcq_assignments as (
  select distinct assignment_id from public.assignment_questions where band is not null
),
counts as (
  select submission_id,
         count(*) filter (where is_correct) as latest,
         count(*) filter (
           where first_is_correct
             and (s.answers_revealed_at is null
                  or a.first_answered_at <= s.answers_revealed_at + interval '2 seconds')
         ) as counted
  from public.assignment_question_attempts a
  join public.assignment_submissions s on s.id = a.submission_id
  group by submission_id
)
update public.assignment_submissions s
set latest_score = c.latest,
    score = c.counted
from counts c
where s.id = c.submission_id
  and s.assignment_id in (select assignment_id from mcq_assignments);

-- ───────────────────────────────────────────────────────────────────────
-- PART 2 — server-side correctness, from the question bank, where resolvable
-- ───────────────────────────────────────────────────────────────────────
--
-- `assignment_questions` carries no answer key of its own (see RESULT-E.md
-- §"why a trigger can resolve this") — a question's correctness lives in
-- `ks3_assignment_bank.options[i].correct` or `ks4_assignment_bank.
-- correct_index`, keyed by `source_ref` = the bank row's own `id`, and which
-- bank to read is decided by `assignments.key_stage` (verified on TEST: 100%
-- of sampled assignment_questions rows resolve to the bank matching their
-- class's key stage, zero cross-matches). Both banks serve options in
-- AUTHORED order with no shuffle (`normaliseKs4BankRow`, `readAssignment-
-- WithQuestions` in server.js) — letter 'ABCD'[i] IS array index i, which is
-- what makes a trigger-side join safe to do at all.
--
-- When the bank row can no longer be resolved (a retired question — ids are
-- never reused, so this can only mean "withdrawn after this assignment was
-- composed") this function changes nothing: the client-sent value is kept,
-- exactly as before this migration. That is the one case named in SPEC-E as
-- "if it can't be done reliably" — everything else resolves.

create or replace function public.mrb_attempt_resolve_correctness()
returns trigger
language plpgsql
security definer
set search_path = public
as $fn$
declare
  v_assignment_id uuid;
  v_key_stage text;
  v_band text;
  v_letter text := upper(nullif(trim(new.selected_option_letter), ''));
  v_idx int;
  v_computed boolean;
  v_correct_letter text;
  v_correct_text text;
begin
  if v_letter is null then
    return new;  -- nothing chosen yet; nothing to verify
  end if;

  select s.assignment_id into v_assignment_id
  from public.assignment_submissions s
  where s.id = new.submission_id;

  if v_assignment_id is null then
    return new;  -- orphaned attempt row; leave whatever the caller sent
  end if;

  select a.key_stage into v_key_stage
  from public.assignments a where a.id = v_assignment_id;

  select aq.band into v_band
  from public.assignment_questions aq
  where aq.assignment_id = v_assignment_id and aq.source_ref = new.question_ref
  limit 1;

  -- Only markable (band IS NOT NULL) MCQ rows are verified. A self-marked
  -- ladder rung (band NULL, rung NOT NULL) is untouched — "must not count
  -- against the student" already means its is_correct is never set to a
  -- real value, and this function must not be the thing that sets one.
  if v_band is null then
    return new;
  end if;

  v_idx := ascii(v_letter) - ascii('A');
  if v_idx < 0 or v_idx > 25 then
    return new;  -- not a real letter; nothing to verify against
  end if;

  if v_key_stage = 'KS4' then
    select (v_idx = k.correct_index),
           substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k.correct_index + 1, 1),
           k.options[k.correct_index + 1]
    into v_computed, v_correct_letter, v_correct_text
    from public.ks4_assignment_bank k
    where k.id = new.question_ref;
  elsif v_key_stage = 'KS3' then
    -- One pass over the exploded options array: whether the SELECTED index
    -- is the correct one, plus the letter and text of whichever option
    -- actually carries `correct: true`. No GROUP BY — a bare aggregate with
    -- no matching bank row still returns one row of NULLs, which is exactly
    -- "could not resolve" for the caller below.
    select bool_or(case when (t.ord - 1) = v_idx then (t.opt ->> 'correct')::boolean end),
           max(case when (t.opt ->> 'correct')::boolean
                    then substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ', (t.ord - 1)::int + 1, 1) end),
           max(case when (t.opt ->> 'correct')::boolean then t.opt ->> 'text' end)
    into v_computed, v_correct_letter, v_correct_text
    from public.ks3_assignment_bank k
    cross join lateral jsonb_array_elements(k.options) with ordinality as t(opt, ord)
    where k.id = new.question_ref;
  end if;

  if v_computed is not null then
    new.is_correct := v_computed;
    if v_correct_letter is not null then
      new.correct_option_letter := v_correct_letter;
    end if;
    if v_correct_text is not null then
      new.correct_answer := v_correct_text;
    end if;
  end if;
  -- else: bank row not found (retired question) — leave the client's
  -- is_correct/correct_answer/correct_option_letter exactly as sent, which
  -- is today's behaviour, unchanged.

  return new;
end;
$fn$;

-- ───────────────────────────────────────────────────────────────────────
-- PART 3 — first_*/answered_at bookkeeping (always immutable once set)
-- ───────────────────────────────────────────────────────────────────────

create or replace function public.mrb_attempt_track_first_answer()
returns trigger
language plpgsql
security definer
set search_path = public
as $fn$
begin
  if tg_op = 'INSERT' then
    new.first_option_letter := new.selected_option_letter;
    new.first_is_correct := new.is_correct;
    new.first_answered_at := now();
    new.answered_at := now();
  elsif tg_op = 'UPDATE' then
    -- Immutable, whatever the client sends: a revision cannot rewrite history.
    new.first_option_letter := old.first_option_letter;
    new.first_is_correct := old.first_is_correct;
    new.first_answered_at := coalesce(old.first_answered_at, old.created_at, now());
    if new.selected_option_letter is distinct from old.selected_option_letter then
      new.answered_at := now();
    else
      new.answered_at := old.answered_at;
    end if;
  end if;
  return new;
end;
$fn$;

-- Correctness resolves first (it can change `is_correct`), THEN the first-
-- answer bookkeeping captures whatever `is_correct` ended up being — trigger
-- order follows name order within the same event, hence the "10_"/"20_"
-- prefixes rather than relying on creation order (which Postgres does NOT
-- guarantee is alphabetical unless named to force it).
drop trigger if exists trg_10_attempt_resolve_correctness on public.assignment_question_attempts;
create trigger trg_10_attempt_resolve_correctness
  before insert or update on public.assignment_question_attempts
  for each row execute function public.mrb_attempt_resolve_correctness();

drop trigger if exists trg_20_attempt_track_first_answer on public.assignment_question_attempts;
create trigger trg_20_attempt_track_first_answer
  before insert or update on public.assignment_question_attempts
  for each row execute function public.mrb_attempt_track_first_answer();

-- ───────────────────────────────────────────────────────────────────────
-- PART 4 — the submission's own score, derived, never trusted
-- ───────────────────────────────────────────────────────────────────────
--
-- ⚠️ GATED ON "is this assignment MCQ-composed at all" (at least one
-- `assignment_questions` row with band IS NOT NULL). Without that gate this
-- would zero out every flashcard-deck submission: `writeFinishedSubmission`
-- in shared/student-live.js writes `assignment_submissions` DIRECTLY from
-- the pupil's own browser (RLS `assignment_submissions_update_merged`/
-- `_insert_merged`, no backend involved at all) with `score = max_score =
-- <cards rated>` and there are never any `assignment_question_attempts` rows
-- for a flashcard deck to derive a score from. That write path is real,
-- live since 1 Oct 2026, and is the one legitimate case SPEC-E's own
-- investigation note flagged to check before closing anything. This
-- migration does not touch it: a submission with zero markable
-- `assignment_questions` rows keeps whatever score it was written with,
-- exactly as today.

create or replace function public.mrb_submission_before_write()
returns trigger
language plpgsql
security definer
set search_path = public
as $fn$
declare
  v_is_mcq boolean;
  v_counted smallint;
  v_latest smallint;
begin
  -- 1. answers_revealed_at: the DB clock, stamped once, on the transition
  --    into 'complete', and immutable forever after. A client (or a
  --    well-meaning backfill) cannot set it directly — see PART 1 above,
  --    which runs BEFORE this trigger exists for exactly that reason.
  if tg_op = 'INSERT' then
    new.answers_revealed_at := case when new.status = 'complete' then now() else null end;
  else
    if old.answers_revealed_at is not null then
      new.answers_revealed_at := old.answers_revealed_at;
    elsif new.status = 'complete' and old.status is distinct from 'complete' then
      new.answers_revealed_at := now();
    else
      new.answers_revealed_at := old.answers_revealed_at;
    end if;
  end if;

  select exists(
    select 1 from public.assignment_questions
    where assignment_id = new.assignment_id and band is not null
  ) into v_is_mcq;

  if not v_is_mcq then
    return new;  -- flashcards / self-marked-only: score is not this trigger's business
  end if;

  if tg_op = 'INSERT' then
    -- A brand-new submission row is opened with score 0 (W1: created by the
    -- first answer, which lands in assignment_question_attempts a moment
    -- later in the same request) — nothing to derive yet.
    new.latest_score := 0;
    -- score is left as whatever the caller supplied (openAttempt always
    -- supplies 0); the UPDATE branch below is what makes it authoritative
    -- from here on.
  else
    -- the same 2-second slack as the backfill CTE above and as server.js's
    -- `isRevised()` REVISED_SLACK_MS — see that comment for why.
    select count(*) filter (where is_correct),
           count(*) filter (
             where first_is_correct
               and (new.answers_revealed_at is null
                    or first_answered_at <= new.answers_revealed_at + interval '2 seconds')
           )
    into v_latest, v_counted
    from public.assignment_question_attempts
    where submission_id = new.id;

    new.latest_score := coalesce(v_latest, 0);
    new.score := coalesce(v_counted, 0);
  end if;

  return new;
end;
$fn$;

drop trigger if exists trg_submission_before_write on public.assignment_submissions;
create trigger trg_submission_before_write
  before insert or update on public.assignment_submissions
  for each row execute function public.mrb_submission_before_write();

-- ───────────────────────────────────────────────────────────────────────
-- PART 5 — close the hole: no legitimate browser path writes attempts rows
-- ───────────────────────────────────────────────────────────────────────
--
-- Checked (grep across shared/*.js): every INSERT/UPDATE of
-- `assignment_question_attempts` in the whole frontend estate goes through
-- the backend's service-role key (/api/assignment/answer et al). Nothing in
-- shared/student-live.js, shared/student-data.js, shared/teacher-live.js,
-- shared/teacher-data.js or shared/breakdown.js ever calls
-- `.insert(`/`.update(`/`.upsert(` on this table — every call site there is
-- a `.select(`. `service_role` bypasses RLS/grants entirely, so this REVOKE
-- cannot touch the real write path; it only removes the PostgREST route a
-- pupil's own browser session could otherwise use to set `is_correct`
-- directly (the hole SPEC-E's investigation flagged).
--
-- `assignment_submissions` gets NO table-wide REVOKE: `writeFinishedSubmission`'s
-- flashcard-completion write is a real, legitimate `authenticated`-role
-- INSERT/UPDATE of `score`/`max_score`/`status`/etc. on that table, so
-- removing the table's blanket UPDATE grant would break it, and re-granting
-- it column-by-column would mean enumerating every column every legitimate
-- writer needs (the flashcard path AND every staff path) — a much larger,
-- riskier change than this unit's scope, not attempted here.
--
-- ⚠️ THE COLUMN-LEVEL REVOKE BELOW IS A NO-OP TODAY, AND IS KEPT ANYWAY AS
-- DEFENCE IN DEPTH. Checked on TEST: Supabase's default schema carries a
-- blanket `GRANT ALL ON assignment_submissions TO authenticated` with no
-- column list, and PostgreSQL's ACL model does not let a column-level REVOKE
-- override an existing TABLE-level grant that already covers that column —
-- `has_column_privilege('authenticated', 'assignment_submissions',
-- 'answers_revealed_at', 'UPDATE')` still returns true after this statement
-- runs. The real protection for `answers_revealed_at`/`latest_score` is
-- PART 4's trigger: it recomputes both from server-held state on every
-- UPDATE regardless of what a client sent, so a pupil's own PostgREST call
-- CAN submit any value for these two columns but the row that is actually
-- stored ignores it every time. "The triggers above already make them
-- derived" (SPEC-E item 5) is true and is doing the real work here; this
-- REVOKE would only start mattering if the table's blanket grant is ever
-- narrowed, and costs nothing to have in place now for that day.

revoke insert, update on public.assignment_question_attempts from authenticated;

revoke update (answers_revealed_at, latest_score) on public.assignment_submissions from authenticated;
