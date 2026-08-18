-- MRB-239 Phase 2a — per-question grain for lesson-page quizzes, modelled on
-- assignment_question_attempts. Parent is a quiz_scores row.
CREATE TABLE public.quiz_question_attempts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  quiz_score_id uuid NOT NULL REFERENCES public.quiz_scores(id) ON DELETE CASCADE,
  question_index smallint NOT NULL,
  question_text text,
  selected_answer text,
  correct_answer text,
  is_correct boolean NOT NULL,
  time_spent_seconds integer,
  attempt_number smallint DEFAULT 1,
  created_at timestamptz DEFAULT now()
);

CREATE INDEX quiz_question_attempts_quiz_score_id_idx ON public.quiz_question_attempts(quiz_score_id);

ALTER TABLE public.quiz_question_attempts ENABLE ROW LEVEL SECURITY;

CREATE POLICY qqa_self_all ON public.quiz_question_attempts
  FOR ALL
  USING (
    EXISTS (
      SELECT 1 FROM public.quiz_scores qs
      WHERE qs.id = quiz_question_attempts.quiz_score_id
        AND qs.user_id = auth_user_id()
    )
  )
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM public.quiz_scores qs
      WHERE qs.id = quiz_question_attempts.quiz_score_id
        AND qs.user_id = auth_user_id()
    )
  );

CREATE POLICY qqa_teacher_read ON public.quiz_question_attempts
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1
      FROM public.quiz_scores qs
      JOIN public.class_members cm ON cm.student_id = qs.user_id AND cm.left_at IS NULL
      WHERE qs.id = quiz_question_attempts.quiz_score_id
        AND auth_user_teaches_class(cm.class_id)
    )
  );
