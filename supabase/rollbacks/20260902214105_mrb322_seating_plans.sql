-- ════════════════════════════════════════════════════════════════════════
-- ROLLBACK for 20260902214105_mrb322_seating_plans
--
-- Apply by hand only. The CLI never reads this folder.
--
-- ⚠️ This DROPS both tables and every seating plan in them. A seating plan is
-- a teacher's afternoon of work, so read the counts before running it:
--
--     select count(*) from public.seating_plans where deleted_at is null;
--     select count(*) from public.room_layouts  where deleted_at is null;
--
-- `auth_user_teaches_class_now()` is dropped LAST and only after the policies
-- that depend on it are gone with their tables. Nothing outside MRB-322 uses
-- it — the estate's own `auth_user_teaches_class()` is a different function and
-- is deliberately left alone here, as it was by the forward migration.
-- ════════════════════════════════════════════════════════════════════════

drop table if exists public.seating_plans;
drop table if exists public.room_layouts;

drop function if exists public.auth_user_teaches_class_now(uuid);
drop function if exists public.seating_touch_updated_at();
