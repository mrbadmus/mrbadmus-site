-- ROLLBACK for mrb310_ks4_scheme_week_ceiling. Apply by hand only.
-- ⚠️ Restoring the 39-week ceiling FAILS while any KS4 row sits above week
-- 39 — delete the KS4 default sequence first (it is regenerable from
-- ks4_seed_sow.py), or the ALTER is refused by the rows it would invalidate.
delete from public.scheme_of_work_entries where key_stage = 'KS4' and academic_week > 39;
alter table public.scheme_of_work_entries drop constraint if exists scheme_of_work_entries_academic_week_check;
alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_academic_week_check check (academic_week >= 1 and academic_week <= 39);
