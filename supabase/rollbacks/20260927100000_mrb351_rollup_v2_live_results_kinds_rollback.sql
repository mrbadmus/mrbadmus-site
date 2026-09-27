-- ROLLBACK for 20260927100000_mrb351_rollup_v2_live_results_kinds.sql
--
-- Apply MANUALLY only -- the Supabase CLI never reads supabase/rollbacks/.
--
-- Drops public.teacher_class_rollup_v2 and nothing else. The forward
-- migration only CREATE OR REPLACEs that one function; it does not touch
-- public.teacher_class_rollup (v1), any table, column or policy. So the
-- rollback is the single inverse of that one CREATE.
--
-- ROLLBACK ORDER (this migration is the LAST of the three that must land
-- together for the flashcard kind split to be meaningful; roll back in the
-- REVERSE of apply order):
--   1. THIS FILE                                                (v2 dropped)
--   2. supabase/rollbacks/20260924180100_mrb351_flashcards_functions_rollback.sql
--   3. supabase/rollbacks/20260924180000_mrb351_flashcards_schema_rollback.sql
--      (⚠️ LOSSY — read its own header before running it)
--
-- ⚠️ ROLLING BACK PUTS THE SIX TEACHER SCREENS BACK ON THE FULL SUBMISSIONS
-- READ, NOT ON A BROKEN PAGE. `loadClassSummaries` in shared/teacher-
-- data.js calls `teacher_class_rollup_v2` and falls back to the full
-- per-class submissions read on any error, INCLUDING PGRST202/42883 (the
-- function does not exist) -- exactly the state every class was already in
-- before this migration was ever applied. Nothing is lost and no pupil
-- sees an error; the six screens simply stop showing LIVE results for a
-- class that is not the one focused on, and go back to the old
-- deadline-gated `marked` reading (and, if migrations 1-2 are also rolled
-- back, lose flashcard homework entirely) until the JS side is rolled back
-- too (it is not this file's job -- see shared/teacher-live.js /
-- teacher-data.js).
--
-- ⚠️ THE REGISTRY VERSION MAY NOT BE THE FILENAME'S, per the precedent set
-- by 20260922231500's own rollback and by 20260924010000's: the MCP
-- connector has been observed stamping `schema_migrations` with its own
-- timestamp rather than the file's. The delete at the end matches on the
-- name as well as the canonical version for that reason, and is a no-op if
-- neither matches.

begin;

drop function if exists public.teacher_class_rollup_v2(uuid[], timestamptz, jsonb);

commit;

-- Step 3 of supabase/rollbacks/README.md.
delete from supabase_migrations.schema_migrations
 where version = '20260927100000'
    or name    = 'mrb351_rollup_v2_live_results_kinds';
