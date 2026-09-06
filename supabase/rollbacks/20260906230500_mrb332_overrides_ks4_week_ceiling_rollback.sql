-- Rollback for 20260906230500_mrb332_overrides_ks4_week_ceiling.sql
--
-- Apply MANUALLY. The Supabase CLI never reads this folder.
--
-- ⚠️ This restores the flat 1..39 ceiling on scheme_of_work_overrides. It
-- will FAIL if any override row already sits above week 39 — which is
-- exactly the row set the forward migration exists to allow. Check first,
-- and delete or renumber before rolling back:
--
--     select school_id, key_stage, year_group, subject_id, count(*)
--       from public.scheme_of_work_overrides
--      where academic_week > 39
--      group by 1,2,3,4;

alter table public.scheme_of_work_overrides
  drop constraint if exists scheme_of_work_overrides_academic_week_check;

alter table public.scheme_of_work_overrides
  add constraint scheme_of_work_overrides_academic_week_check
  check (academic_week between 1 and 39);
