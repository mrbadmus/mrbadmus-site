-- ROLLBACK for 20260908065607_mrb336_replace_assignment_questions
--
-- Apply MANUALLY only. Non-destructive: the function holds no data, and
-- dropping it cannot affect any assignment that already exists.
--
-- ⚠️ DROP THE ROUTE FIRST, OR AT THE SAME TIME. `PATCH
-- /api/teacher/set-work/:id` calls this by name for its before-release
-- question replacement; with the function gone the route answers 500
-- `questions_replace_failed` and the teacher's edit is refused — which is the
-- safe direction, but it is a live 500 rather than a clean absence.

drop function if exists public.replace_assignment_questions(uuid, jsonb);

delete from supabase_migrations.schema_migrations where version = '20260908065607';
