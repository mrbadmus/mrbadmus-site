-- Rollback for 20260902221216_create_submission_feedback.
-- MANUAL ONLY. The CLI never reads this folder.
--
-- ⚠️ This DESTROYS every piece of written feedback a teacher has left,
-- including rows they soft-deleted and the prior bodies kept on edit. There is
-- no other copy. Read the table before running it:
--     select count(*) from public.submission_feedback;
-- If that is not 0, this is data loss and needs Mide's explicit say-so.
--
-- The two helpers are dropped last because the policies depend on them. They
-- are used by nothing else — check before assuming that is still true:
--     select polname from pg_policy where pg_get_expr(polqual, polrelid)
--       like '%submission_class_id%';

drop policy if exists submission_feedback_update on public.submission_feedback;
drop policy if exists submission_feedback_insert on public.submission_feedback;
drop policy if exists submission_feedback_select on public.submission_feedback;

drop table if exists public.submission_feedback;

drop function if exists public.submission_student_id(uuid);
drop function if exists public.submission_class_id(uuid);
