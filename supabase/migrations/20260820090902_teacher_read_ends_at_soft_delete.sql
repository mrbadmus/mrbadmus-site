-- MRB-270 phase 4 — removal from a class ENDS the teacher's read.
--
-- ⚠️ APPLIED VIA MCP `apply_migration`; this file's timestamp is the version it
-- recorded (20260820090902) so `supabase db push` will not re-run it.
--
-- RULED (Mide, 20 Aug 2026). Both teacher-read policies tested
-- `cm.left_at IS NULL` and neither tested `cm.deleted_at IS NULL`, so a
-- membership that had been SOFT-DELETED still granted the teacher sight of
-- that student's scores and every per-question attempt behind them.
--
-- The two columns are not the same thing and both have to hold:
--   left_at    — the student left the class in the ordinary way
--   deleted_at — the membership row itself was removed
-- A row soft-deleted without left_at being set — which is exactly what a
-- mistaken enrolment corrected by a teacher looks like — passed the old test
-- completely.
--
-- The DPA with the school is still open and the defensible position is the
-- narrow one: removal from a class ends the read. Nothing here widens any
-- policy; both are strictly tightened, and student self-read is untouched.
--
-- ── PROVED, on an isolated fixture that was removed afterwards ─────────────
--
-- Its own school, so nothing could touch 8r/Sc1 or any real class: one class,
-- one teacher, an ACTIVE member, and a member soft-deleted with left_at still
-- NULL. Counts read as each identity in turn, RLS on:
--
--   identity               active: score/attempt/profile   removed: same three
--   TEACHER of the class            1  1  1                      0  0  0
--   ACTIVE student, self            1  1  1                      0  0  0
--   REMOVED student, self           0  0  0                      1  1  1
--   unrelated student               0  0  0                      0  0  0
--   ANONYMOUS (no jwt)              0  0  0                      0  0  0
--
-- And the fix demonstrably BIT, rather than the row being blocked for some
-- other reason. Both predicates evaluated side by side as the teacher:
--
--   Active Student    old: true   new: true
--   Removed Student   old: TRUE   new: false     ← the leak, and its close
--
-- The old predicate was evaluated as a plain expression rather than by
-- re-instating the old policy: re-opening a hole on production to photograph
-- it is not worth the window.
--
-- ⊕ The two OTHER policies carrying the identical bug are closed in
-- 20260820091500, deliberately in their own migration so the record keeps
-- what was ruled separate from what was found by sweeping.

drop policy if exists quiz_scores_teacher_read on public.quiz_scores;

create policy quiz_scores_teacher_read on public.quiz_scores
  for select
  using (
    exists (
      select 1
        from public.class_members cm
       where cm.student_id = quiz_scores.user_id
         and cm.left_at is null
         and cm.deleted_at is null
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
         and cm.deleted_at is null
       where qs.id = quiz_question_attempts.quiz_score_id
         and public.auth_user_teaches_class(cm.class_id)
    )
  );
