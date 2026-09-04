-- ════════════════════════════════════════════════════════════════════════
-- MRB-322 follow-up — two write policies were wider than the ruling.
--
-- Both were found by a cold read of the diff, after the first migration had
-- already been applied to production. Both are closed here rather than by
-- editing the original, because the original is applied and a migration that
-- has run is history.
-- ════════════════════════════════════════════════════════════════════════

-- 1 · A plan could be re-pointed at a class you do not teach.
--
-- INSERT required auth_user_teaches_class_now(class_id). UPDATE constrained
-- school and authorship but said nothing about class_id at all, so the author
-- of a plan for their own class could move it onto ANY class in the school:
--
--     update seating_plans set class_id = '<someone else's class>' where id = ...
--
-- Both clauses passed. The teacher of that other class would then open a plan
-- on their own register holding a different class's pupil ids — and the
-- original author, who can no longer READ the row, could go on blind-writing
-- and soft-deleting it. The ruling was "write: author plus admins" for THAT
-- class's plan.
drop policy if exists seating_plans_author_update on public.seating_plans;
create policy seating_plans_author_update on public.seating_plans
  for update using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  ) with check (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
    and (public.auth_user_role() = 'admin'
         or public.auth_user_teaches_class_now(class_id))
  );

-- 2 · Anyone with a session could create a room layout — pupils included.
--
-- `auth_user_school_id()` reads profiles.school_id, which a student has just
-- as much as a teacher, and the insert asked for nothing beyond that and
-- `created_by = auth.uid()`. So a pupil could POST rows that every teacher in
-- the school then sees in the room picker and cannot remove, because retiring
-- a layout is author-or-admin only. The plans table had been gated on
-- class_teachers from the start; this one was simply missed.
--
-- The role set is the one the backend already gates /api/teacher/* on.
drop policy if exists room_layouts_author_insert on public.room_layouts;
create policy room_layouts_author_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and created_by = auth.uid()
    and public.auth_user_role() in ('teacher', 'hod', 'admin')
  );
