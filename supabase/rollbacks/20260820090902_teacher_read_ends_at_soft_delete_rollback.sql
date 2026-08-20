-- Rollback for 20260820090902_teacher_read_ends_at_soft_delete.
-- Apply MANUALLY. The CLI never reads this folder.
--
-- ⚠️ THIS RE-OPENS A READ THAT WAS RULED CLOSED. Dropping `deleted_at IS NULL`
-- puts a teacher back in sight of the scores and per-question attempts of a
-- student who has been removed from their class. The DPA with the school is
-- still open and that is the position the ruling rejected.
--
-- There is no honest reason to run this. It exists because a migration without
-- a stated undo is a migration nobody can reason about, not because rolling
-- back is a thing to do. If a deploy genuinely must run against the pre-4
-- policy set, run it and roll forward the moment it is unblocked.

drop policy if exists quiz_scores_teacher_read on public.quiz_scores;

create policy quiz_scores_teacher_read on public.quiz_scores
  for select
  using (
    exists (
      select 1
        from public.class_members cm
       where cm.student_id = quiz_scores.user_id
         and cm.left_at is null
         and public.auth_user_teaches_class(cm.class_id)
    )
  );

drop policy if exists qqa_teacher_read on public.quiz_question_attempts;

create policy qqa_teacher_read on public.quiz_question_attempts
  for select
  using (
    exists (
      select 1
        from public.quiz_scores qs
        join public.class_members cm
          on cm.student_id = qs.user_id
         and cm.left_at is null
       where qs.id = quiz_question_attempts.quiz_score_id
         and public.auth_user_teaches_class(cm.class_id)
    )
  );
