-- Rollback for supabase/migrations/20260906044804_mrb326_timetable_slot_guard.sql
--
-- Drops the BEFORE INSERT OR UPDATE guard that refuses a second LIVE lesson in
-- one (owner, academic_year_id, weekday, period) where either row's week_cycle
-- is NULL. Apply MANUALLY only — this folder is invisible to the Supabase CLI.
--
-- ⚠️ AFTER RUNNING THIS, the NULL-cycle double-booking becomes possible again.
-- The two unique indexes are untouched by this file (this migration did not
-- create them), so equal-cycle duplicates — including the seeded-vs-manual
-- pair that started MRB-326 — are still refused by
-- `timetable_entries_teacher_slot_unique`.
--
-- Then, per supabase/rollbacks/README.md, remove the registry row:
--   delete from supabase_migrations.schema_migrations
--    where version = '20260906044804';

drop trigger if exists timetable_entries_slot_guard on public.timetable_entries;
drop function if exists public.timetable_entries_slot_guard();
