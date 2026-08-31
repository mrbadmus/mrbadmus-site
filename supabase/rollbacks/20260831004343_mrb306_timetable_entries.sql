-- ROLLBACK for MRB-306 WS-1 (20260831004343_mrb306_timetable_entries).
-- Apply MANUALLY only. The CLI never reads this folder.
--
-- Order matters: claim_pending_staff() references timetable_entries, so the
-- function must be reverted to its MRB-293 form BEFORE the table is dropped.
-- Run 20260831095950_mrb306_claim_attaches_timetable's rollback first.
--
-- This DESTROYS the 204 seeded timetable rows. They are reproducible from
-- supabase/data-ops/MRB-306/01_seed_timetable.sql and the source spreadsheet.

drop table if exists public.timetable_entries;
drop table if exists public.school_period_times;
