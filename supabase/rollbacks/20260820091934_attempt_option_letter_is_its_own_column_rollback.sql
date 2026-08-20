-- Rollback for 20260820091934_attempt_option_letter_is_its_own_column.
-- Apply MANUALLY. The CLI never reads this folder.
--
-- ⚠️ THIS DESTROYS DATA, and unusually for a rollback it destroys data the
-- forward migration did not create: every letter recorded since it landed.
-- There is nowhere else for those values to go — `selected_answer` now holds
-- the option TEXT alone, so dropping the columns loses which option was chosen
-- wherever two distractors do not differ in their first characters.
--
-- Only run this to unblock a deploy that must run the pre-phase-5 backend, and
-- prefer leaving the columns in place: they are nullable and additive, and a
-- backend that does not know about them simply writes null.

alter table public.quiz_question_attempts
  drop column if exists selected_option_letter,
  drop column if exists correct_option_letter;

comment on column public.quiz_question_attempts.selected_answer is NULL;
comment on column public.quiz_question_attempts.correct_answer is NULL;
