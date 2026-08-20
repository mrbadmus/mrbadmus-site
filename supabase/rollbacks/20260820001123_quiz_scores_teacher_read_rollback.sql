-- Rollback for 20260820001123_quiz_scores_teacher_read.
-- Apply MANUALLY. The CLI never reads this folder.
--
-- Dropping this policy re-breaks the teacher read path: qqa_teacher_read goes
-- dead again and a teacher screen reads "no data". That is the state this
-- migration was written to end, so roll back only to undo a bad deploy.

DROP POLICY IF EXISTS quiz_scores_teacher_read ON public.quiz_scores;
