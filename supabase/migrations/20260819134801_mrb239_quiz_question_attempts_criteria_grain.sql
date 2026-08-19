-- 20260819134801_mrb239_quiz_question_attempts_criteria_grain
--
-- MRB-239 (Mide, 19 Aug 2026) — the free-text rungs get their own grain.
--
-- `correct_answer` on a self-marked rung held "0 of 5 criteria ticked": a
-- RESULT, in a column whose every other row holds answer text. It could not
-- answer the question the per-question grain exists for, and it put a
-- computed summary in a snapshot column.
--
-- `correct_answer` now holds the SUCCESS CRITERIA THEMSELVES — the model
-- answer the student marked against, which is what that column means and
-- what the snapshot is for. Which criteria were ticked moves here.
--
-- The shape is chosen so that "19 of 24 students never tick criterion 3" is
-- a direct query rather than a reconstruction. A count can never be that.
--
-- Additive and nullable: every existing consumer and every marked-rung row
-- is unaffected.
alter table public.quiz_question_attempts
  add column if not exists criteria_met smallint[],
  add column if not exists criteria_total smallint;

comment on column public.quiz_question_attempts.criteria_met is
  'MRB-239. Self-marked (free-text) rungs only: 1-based indices of the success criteria the student ticked, indexing into the tab-separated list in correct_answer. NULL on marked (multiple-choice) rungs.';

comment on column public.quiz_question_attempts.criteria_total is
  'MRB-239. Self-marked rungs only: how many success criteria the rung offered. NULL on marked rungs. criteria_met is a subset of 1..criteria_total.';

comment on column public.quiz_question_attempts.correct_answer is
  'The model answer, as the student saw it. Marked rungs: the correct option, as "<letter>\tab<text>". Self-marked rungs (MRB-239): the success criteria, tab-separated, in the order they were shown — criteria_met indexes into this list.';
