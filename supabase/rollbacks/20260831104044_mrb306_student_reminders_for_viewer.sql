-- ROLLBACK for MRB-306 WS-3 (20260831104044_mrb306_student_reminders_for_viewer).
-- Apply MANUALLY only.
drop function if exists public.student_reminders_for_viewer(uuid);
