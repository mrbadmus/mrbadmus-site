-- ROLLBACK for 20260922114500_mrb348_teacher_class_summaries
--
-- Apply MANUALLY only -- the Supabase CLI never reads supabase/rollbacks/.
--
-- Returns the database to the state it was in before EITHER MRB-348 teacher
-- aggregate migration: no `teacher_class_summaries`, no `teacher_class_rollup`.
-- The forward migration creates exactly one function and nothing else, so this
-- file drops exactly that function and nothing else. No table, no policy, no
-- row of pupil data is touched.
--
-- ⚠️ ORDER MATTERS, AND THIS IS THE SECOND FILE OF TWO. If
-- 20260922231500 has been applied, run
-- `20260922231500_mrb348_teacher_class_rollup_rollback.sql` FIRST. That file
-- drops the rollup and recreates THIS function; this file then removes it.
-- Running this one alone against a database carrying the rollup leaves the
-- rollup standing -- which is not "before either migration", it is halfway.
-- Running it alone is otherwise harmless (`drop ... if exists`).
--
-- ⚠️ ROLLING BACK PUTS THE SIX TEACHER SCREENS BACK ON THE UNBOUNDED READ.
-- `loadClassMatrices()` falls back to fetching every submission of every
-- assignment of every class the viewer touches when the aggregate is absent.
-- That fallback was proven for real on TEST (MRB-348 round three, §4b), so
-- the screens keep WORKING; they simply get slow again, and get slower every
-- week of term. Nothing is lost and no pupil sees an error.
--
-- ⚠️ NOTHING IN THE REPO CALLS `teacher_class_summaries`. It was superseded
-- by `teacher_class_rollup` before either reached production, and the shipped
-- `shared/teacher-data.js` calls the rollup. Dropping it costs nothing; it is
-- recreated here only so that rolling back 231500 lands on a state that is
-- honestly "what 114500 left", rather than on a convenient approximation.
--
-- ⚠️ THE REGISTRY VERSION MAY NOT BE THE FILENAME'S -- see the same warning
-- in the 231500 rollback. On TEST this migration was never registered at all
-- (it was applied ad hoc and superseded the same day), so the delete below
-- found no row there. That is expected, not a failure.

begin;

drop function if exists public.teacher_class_summaries(uuid[]);

commit;

-- Step 3 of supabase/rollbacks/README.md. Matches the canonical filename
-- version OR the migration name, because the two have been seen to differ.
-- No-op when neither is present.
delete from supabase_migrations.schema_migrations
 where version = '20260922114500'
    or name    = 'mrb348_teacher_class_summaries';
