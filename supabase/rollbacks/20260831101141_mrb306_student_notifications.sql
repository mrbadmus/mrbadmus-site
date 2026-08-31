-- ROLLBACK for MRB-306 WS-3 (20260831101141_mrb306_student_notifications).
-- Apply MANUALLY only. Drop the RPC first — it reads this table.
--   drop function if exists public.student_reminders_for_viewer(uuid);
drop table if exists public.student_notifications;
