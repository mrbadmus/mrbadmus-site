-- Rollback for 20260906145023_mrb331_release_gates_student_reads.sql (MRB-331).
-- Apply by hand. Restores both policies to their pre-MRB-331 text, which is
-- 20260501212106_schools_layer.sql for the assignments policy and
-- 20260820091413_soft_delete_ends_access_the_other_two.sql for the questions
-- policy — NOT 20260818231201, which the later migration replaced.
--
-- ⚠️ THIS RELEASES EVERY HELD ASSIGNMENT IMMEDIATELY. Any teacher-set work
-- scheduled for a future date becomes readable by its class the moment this
-- runs. Check what is pending first:
--
--   select count(*) from assignments
--    where release_at > now() and deleted_at is null;

drop policy if exists assignments_student_read on public.assignments;
create policy assignments_student_read on public.assignments
  for select
  using (
    class_school_id(class_id) = auth_user_school_id()
    and auth_user_is_member_of_class(class_id)
  );

drop policy if exists aq_student_read on public.assignment_questions;
create policy aq_student_read on public.assignment_questions
  for select
  using (
    exists (
      select 1
      from assignments a
      join class_members cm
        on cm.class_id = a.class_id
       and cm.left_at is null
       and cm.deleted_at is null
      where a.id = assignment_questions.assignment_id
        and cm.student_id = auth_user_id()
    )
  );
