-- ROLLBACK for 20260901230828_mrb310_child_plans_and_work_items. Apply by hand only.
-- ⚠️ Drops every child's Today list, position and pause state. Migrations
-- 5 and 6 reference work_items (unit_check_attempts.work_item_id,
-- exam_answers.work_item_id) — roll those back first, or these drops fail.
drop trigger if exists trg_work_items_touch on public.work_items;
drop trigger if exists trg_child_plans_touch on public.child_plans;
drop table if exists public.work_generation_runs;
drop table if exists public.work_items;
drop table if exists public.child_plans;
-- consumer_touch_updated_at() is shared with exam_answers (migration 6);
-- drop it only if that table is already gone.
drop function if exists public.consumer_touch_updated_at();
