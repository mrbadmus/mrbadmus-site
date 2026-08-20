-- MRB-269 phase 4b — the teacher read path that silently failed.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`, which records its OWN
-- `supabase_migrations.schema_migrations` version. This file's timestamp is
-- that recorded version (20260820001123) so `supabase db push` treats it as
-- already applied instead of running it a second time.
--
-- `qqa_teacher_read` on quiz_question_attempts already lets a teacher read a
-- student's per-question attempts, and it reaches them by joining through
-- quiz_scores. But quiz_scores carried ONLY the two self policies
-- ("Users can view own scores" / "Users can insert own scores"), so the join
-- resolved to nothing for a teacher and the attempt policy was dead. A teacher
-- screen did not error — it read as "no data", which is the worst failure mode
-- because it looks like a class that has not worked rather than a broken read.
--
-- Measured on production, as the teacher of 8r/Sc1 against a student with two
-- quiz_scores and four attempts:
--
--   BEFORE  auth_user_teaches_class(8r/Sc1) .. true
--           quiz_scores visible ............... 0
--           attempts visible .................. 0
--   AFTER   quiz_scores visible ............... 2
--           attempts visible .................. 4
--   NEG     a student who teaches nothing ..... 0 and 0
--   CONTROL the student's own self-read ....... 2 and 4, unchanged,
--           and still 0 rows of any other student
--
-- The gate is deliberately IDENTICAL to qqa_teacher_read's: the same
-- class_members join, the same `left_at IS NULL`, the same
-- auth_user_teaches_class(). Two policies that mean "the teacher of this
-- student's class" must not drift apart.
--
-- ⚑ NOTED, NOT CHANGED: neither this policy nor qqa_teacher_read tests
-- `class_members.deleted_at`. A soft-deleted membership therefore still grants
-- a teacher read on both. Matching the existing policy was the instruction and
-- divergence would leave one stricter than the other; if that gate is wanted it
-- belongs on BOTH policies in one migration.
--
-- SELECT only. A teacher never writes a student's score.

CREATE POLICY quiz_scores_teacher_read ON public.quiz_scores
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1
      FROM public.class_members cm
      WHERE cm.student_id = quiz_scores.user_id
        AND cm.left_at IS NULL
        AND public.auth_user_teaches_class(cm.class_id)
    )
  );
