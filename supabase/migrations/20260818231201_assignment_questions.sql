-- MRB-239 Phase 2b — an assignment stores question REFERENCES, never text and
-- never a seed. Text resolves from live content at render time; the historical
-- record is preserved by assignment_question_attempts, which snapshots what the
-- student actually saw. source_ref is the lesson's stable path
-- (<discipline>/<unit-slug>/<lesson-slug>), resolvable without a uuid.
CREATE TABLE public.assignment_questions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  assignment_id uuid NOT NULL REFERENCES public.assignments(id) ON DELETE CASCADE,
  position smallint NOT NULL,
  source_ref text NOT NULL,
  rung text NOT NULL CHECK (rung IN ('recall', 'apply', 'explain', 'produce')),
  created_at timestamptz DEFAULT now(),
  UNIQUE (assignment_id, position)
);

CREATE INDEX assignment_questions_assignment_id_idx ON public.assignment_questions(assignment_id);

ALTER TABLE public.assignment_questions ENABLE ROW LEVEL SECURITY;

CREATE POLICY aq_student_read ON public.assignment_questions
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1
      FROM public.assignments a
      JOIN public.class_members cm ON cm.class_id = a.class_id AND cm.left_at IS NULL
      WHERE a.id = assignment_questions.assignment_id
        AND cm.student_id = auth_user_id()
    )
  );

CREATE POLICY aq_teacher_all ON public.assignment_questions
  FOR ALL
  USING (
    EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_questions.assignment_id
        AND auth_user_teaches_class(a.class_id)
        AND class_school_id(a.class_id) = auth_user_school_id()
    )
  )
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_questions.assignment_id
        AND auth_user_teaches_class(a.class_id)
        AND class_school_id(a.class_id) = auth_user_school_id()
    )
  );

CREATE POLICY aq_admin_read ON public.assignment_questions
  FOR SELECT
  USING (
    (auth_user_has_scope('school_admin') OR auth_user_has_scope('slt'))
    AND EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_questions.assignment_id
        AND class_school_id(a.class_id) = auth_user_school_id()
    )
  );

CREATE POLICY aq_operator_read ON public.assignment_questions
  FOR SELECT
  USING (auth_user_operator_active());
