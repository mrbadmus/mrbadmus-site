-- ROLLBACK for MRB-308 Night 1, migration 5 of 6
-- (20260901214441_mrb308_create_family_for_parent). Apply MANUALLY only.
--
-- Safe on its own: nothing in the estate calls this function except the
-- backend's parent-signup route, which is itself behind CONSUMER_SIGNUP_ENABLED.
-- It was never granted to authenticated or anon.
--
-- ⚠️ Dropping the function does NOT unwind the families it already made. Each
-- one is five rows — a schools row, an academic_years row, the promoted
-- profile, a staff_scopes row and a subscriptions row — and they stay exactly
-- where they are. To find them:
--   select id, name, code, created_at from public.schools
--    where kind = 'family' and deleted_at is null order by created_at;
-- Unwinding a family is a deliberate, separate act. It is not scripted here,
-- because deleting a parent's account and their children's work by running a
-- rollback file is not something that should be one command away.

drop function if exists public.create_family_for_parent(uuid, text);
