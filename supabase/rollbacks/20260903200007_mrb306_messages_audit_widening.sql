-- Rollback for 20260903200007_mrb306_messages_audit_widening.
-- MANUAL ONLY. The CLI never reads this folder.
--
-- ⚠️ This NARROWS read access back. It destroys no data, but it removes the
-- Messages audit surface that Mide named the safeguarding control — school
-- admins stop being able to read shoutouts school-wide, and SLT stops being
-- able to read written feedback. Do not run it to "tidy up"; run it only if
-- the widening is being deliberately withdrawn.
--
-- Restores each policy to its immediately-prior form:
--   · submission_feedback_select — school_admin only, no slt
--   · class_shoutouts_select     — teacher/member only, no school_admin

alter policy submission_feedback_select on public.submission_feedback
using (
  (
    deleted_at is null
    and (
      auth_user_teaches_class(submission_class_id(submission_id))
      or submission_student_id(submission_id) = auth.uid()
      or (auth_user_has_scope('school_admin')
          and class_school_id(submission_class_id(submission_id)) = auth_user_school_id())
    )
  )
  or (
    deleted_at is not null
    and (
      teacher_id = auth.uid()
      or (auth_user_has_scope('school_admin')
          and class_school_id(submission_class_id(submission_id)) = auth_user_school_id())
    )
  )
);

alter policy class_shoutouts_select on public.class_shoutouts
using (
  ((deleted_at is null) and (auth_user_teaches_class(class_id)
                             or auth_user_is_member_of_class(class_id)))
  or ((deleted_at is not null) and (author_id = auth.uid()))
);
