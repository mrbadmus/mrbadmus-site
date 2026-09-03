-- ROLLBACK for 20260903214546_mrb322_seating_admin_is_scope.sql
--
-- Restores all six seating policies to the state 20260903203226 left them
-- in: the admin branch reads `auth_user_role() = 'admin'` again, and
-- room_layouts' staff test goes back to the `in ('teacher','admin')` array.
--
-- ⚠️ This is a NARROWING. `auth_user_has_scope('school_admin')` is a strict
-- superset of `auth_user_role() = 'admin'` (the M1 dual-read fallback), so
-- applying this rollback TAKES seating away from every teacher who holds the
-- school_admin scope but is not `role = 'admin'` — on production that is
-- Ayomide, James and Richard. Any plan or layout they authored survives; they
-- simply stop being able to reach rows outside the classes they teach.
--
-- Nothing else is touched. The anon revokes from 20260903203226 are NOT
-- reinstated — they never should have been granted, and this migration did
-- not change them.
--
-- Apply by hand. The Supabase CLI never reads this folder.

-- ── room_layouts ────────────────────────────────────────────────────────
drop policy if exists room_layouts_staff_read on public.room_layouts;
create policy room_layouts_staff_read on public.room_layouts
  for select using (
    school_id = public.auth_user_school_id()
    and public.auth_user_role() in ('teacher', 'admin')
  );

drop policy if exists room_layouts_staff_insert on public.room_layouts;
create policy room_layouts_staff_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and created_by = auth.uid()
    and public.auth_user_role() in ('teacher', 'admin')
  );

drop policy if exists room_layouts_staff_update on public.room_layouts;
create policy room_layouts_staff_update on public.room_layouts
  for update using (
    school_id = public.auth_user_school_id()
    and ((created_by = auth.uid() and public.auth_user_role() = 'teacher')
         or public.auth_user_role() = 'admin')
  ) with check (
    school_id = public.auth_user_school_id()
    and ((created_by = auth.uid() and public.auth_user_role() = 'teacher')
         or public.auth_user_role() = 'admin')
  );

-- ── seating_plans ───────────────────────────────────────────────────────
drop policy if exists seating_plans_staff_read on public.seating_plans;
create policy seating_plans_staff_read on public.seating_plans
  for select using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or (public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );

drop policy if exists seating_plans_staff_insert on public.seating_plans;
create policy seating_plans_staff_insert on public.seating_plans
  for insert with check (
    created_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or (public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );

drop policy if exists seating_plans_staff_update on public.seating_plans;
create policy seating_plans_staff_update on public.seating_plans
  for update using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or (created_by = auth.uid()
             and public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  ) with check (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or (created_by = auth.uid()
             and public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );
