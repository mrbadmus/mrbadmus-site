-- Rollback for 20260820140008_assignment_question_attempts_identity_and_letters.
-- Apply by hand only. The Supabase CLI never reads this folder.
--
-- ⚠️ RESTORING THE NOT NULL ON is_correct CAN FAIL, and that is the point: if
-- any row has been written with a null is_correct — a self-marked or written
-- response, which is the whole reason the constraint was dropped — this
-- statement refuses. Do not "fix" it by setting those rows false. False is a
-- claim that the student got it wrong; null is the truth, which is that the
-- platform never knew. If you genuinely need the constraint back, delete the
-- null rows deliberately and say so.
alter table public.assignment_question_attempts
  drop column if exists question_ref,
  drop column if exists selected_option_letter,
  drop column if exists correct_option_letter,
  drop column if exists rung,
  drop column if exists criteria_met,
  drop column if exists criteria_total;

alter table public.assignment_question_attempts
  alter column is_correct set not null;
