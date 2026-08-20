-- Rollback for 20260820091500_soft_delete_ends_access_the_other_two.
-- Apply MANUALLY. The CLI never reads this folder.
--
-- ⚠️ Same warning as 20260820090902's rollback, and one of these is worse:
-- restoring `profiles_teacher_read_students` puts a teacher back in sight of
-- the NAME of a student removed from their class. That is personal data.

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
         and public.auth_user_teaches_class(cm.class_id)
         and cm.left_at is null
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
       where a.id = assignment_questions.assignment_id
         and cm.student_id = public.auth_user_id()
    )
  );
