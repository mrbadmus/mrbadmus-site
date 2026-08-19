-- 20260819122539_quiz_question_attempts_rung
--
-- ⚠️ RECONSTRUCTED, 19 Aug 2026. This migration was applied to production
-- via MCP `apply_migration` earlier the same day and NO LOCAL FILE WAS
-- CHECKED IN, so `supabase_migrations.schema_migrations` carried a version
-- the repository could not account for. The file is written here to match
-- the recorded version and name exactly, so the repo can rebuild the schema
-- from scratch and `supabase db push` sees nothing outstanding.
--
-- Two more applied versions are still missing local files and are NOT
-- reconstructed here, because they are data seeds this session did not write
-- and guessing at their contents would be worse than recording the gap:
--     20260818234128  mrb238_demo_assignment_8r_sc1
--     20260818234137  mrb238_demo_assignment_questions_8r_sc1
--
-- WHAT IT DOES (MRB-262): the ladder rung a question belongs to — "recall",
-- "apply", "explain", "produce". Difficulty on a KS3 ladder is DEFINED by
-- rung, and without the column it was only recoverable from question_index
-- by assuming every ladder has the same four rungs in the same order. That
-- implicit coupling is exactly why the column is worth having.
alter table public.quiz_question_attempts
  add column if not exists rung text;

comment on column public.quiz_question_attempts.rung is
  'MRB-262. The ladder rung this question sat on — recall | apply | explain | produce. Difficulty on a KS3 ladder is defined by rung. NULL for callers that do not use rungs (e.g. KS4).';
