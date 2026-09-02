-- ROLLBACK for 20260901231055_mrb312_unit_checks_and_report_notes. Apply by hand only.
-- ⚠️ Drops every unit-check record, every report note and the flashcard queue.
drop table if exists public.child_flashcard_queue;
drop table if exists public.report_notes;
drop table if exists public.unit_check_attempts;
