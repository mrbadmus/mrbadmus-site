-- Rollback for 20261004010000_x_reopen_fair_scoring.sql
-- Manual apply only (the CLI never reads this folder). Reverses, in order:
-- grants → triggers → functions → columns. Run as one statement block (or
-- paste the whole file) so a mid-way failure leaves the LEAST inconsistent
-- state — half-reverted is still "triggers gone, columns still there",
-- which is safe (no trigger left pointing at a dropped function).

-- 1. restore the grants PART 5 revoked
grant insert, update on public.assignment_question_attempts to authenticated;
grant update (answers_revealed_at, latest_score) on public.assignment_submissions to authenticated;

-- 2. drop the triggers
drop trigger if exists trg_submission_before_write on public.assignment_submissions;
drop trigger if exists trg_20_attempt_track_first_answer on public.assignment_question_attempts;
drop trigger if exists trg_10_attempt_resolve_correctness on public.assignment_question_attempts;

-- 3. drop the functions
drop function if exists public.mrb_submission_before_write();
drop function if exists public.mrb_attempt_track_first_answer();
drop function if exists public.mrb_attempt_resolve_correctness();

-- 4. drop the columns (irreversibly discards any first_*/revealed/latest
--    data accumulated since the migration was applied — this is the one
--    genuinely destructive step; confirm that is wanted before running it)
alter table public.assignment_question_attempts
  drop column if exists first_option_letter,
  drop column if exists first_is_correct,
  drop column if exists first_answered_at,
  drop column if exists answered_at;

alter table public.assignment_submissions
  drop column if exists answers_revealed_at,
  drop column if exists latest_score;

-- Verification after rollback:
--   select count(*) from information_schema.columns
--    where table_name in ('assignment_submissions','assignment_question_attempts')
--      and column_name in ('answers_revealed_at','latest_score','first_option_letter',
--                           'first_is_correct','first_answered_at','answered_at');
--   -- expect 0
--   select count(*) from pg_trigger where tgname like 'trg_%attempt%' or tgname = 'trg_submission_before_write';
--   -- expect 0
