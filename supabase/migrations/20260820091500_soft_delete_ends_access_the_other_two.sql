-- MRB-270 phase 4, the ADJACENT half.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820091500) so `supabase db push` will not re-run it.
--
-- Not ruled by name. Found by sweeping every policy whose USING clause reads
-- `class_members`, after 20260820090902 closed the two that were: the same
-- predicate bug sat on two more, and fixing two of four would have left the
-- database saying two different things about what a soft-deleted membership
-- means.
--
--   profiles_teacher_read_students — a teacher still read the NAME of a
--       student removed from their class. If anything this is the MORE
--       DPA-sensitive of the pair the ruling named: personal data, not
--       attainment.
--
--   aq_student_read — the mirror, in the student direction: a student whose
--       membership had been soft-deleted still read that class's assignment
--       questions.
--
-- Both are strict tightenings; nothing is widened. Measured before applying:
-- exactly ONE soft-deleted membership existed in the whole database and it was
-- phase 4's own test fixture, so no live access changed. Verified after: all
-- four class_members-reading policies now test `deleted_at IS NULL`, and the
-- teacher's read of a removed student's PROFILE is 0 where it was 1.

drop policy if exists profiles_teacher_read_students on public.profiles;

create policy profiles_teacher_read_students on public.profiles
  for select
  using (
    school_id = public.auth_user_school_id()
    and role = 'student'
    and exists (
      select 1
        from public.class_members cm
       where cm.student_id = profiles.id
         and cm.left_at is null
         and cm.deleted_at is null
         and public.auth_user_teaches_class(cm.class_id)
    )
  );

drop policy if exists aq_student_read on public.assignment_questions;

create policy aq_student_read on public.assignment_questions
  for select
  using (
    exists (
      select 1
        from public.assignments a
        join public.class_members cm
          on cm.class_id = a.class_id
         and cm.left_at is null
         and cm.deleted_at is null
       where a.id = assignment_questions.assignment_id
         and cm.student_id = public.auth_user_id()
    )
  );
