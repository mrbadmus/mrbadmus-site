-- ROLLBACK for 20260903203226. Apply by hand only.
--
-- ⚠️ This drops the `profiles.role = 'teacher'` conjunct from the seating_plans
-- teacher branch. After running it, anyone holding a live `subject_teacher` row
-- on a class reads and writes that class's seating plans REGARDLESS of what
-- their profile says they are — and `supabase/functions/roster-import/index.ts`
-- hands out that row on the service role, taking the teacher id from its
-- request body without checking it against the caller, the school, or the
-- target's role. So restoring this puts a pupil one service-role call away from
-- a named list of children.
--
-- It also puts the `anon` grants back on both tables. RLS still refuses anon on
-- every verb, so that half changes no behaviour; it is restored only so this
-- file actually returns the database to the state 20260903203226 found.
--
-- Do not run this to unstick a deploy. Nothing in the seating page depends on
-- the wider policies.

drop policy if exists seating_plans_staff_read on public.seating_plans;
create policy seating_plans_staff_read on public.seating_plans
  for select using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or public.auth_user_is_subject_teacher_of_class(class_id))
  );

drop policy if exists seating_plans_staff_insert on public.seating_plans;
create policy seating_plans_staff_insert on public.seating_plans
  for insert with check (
    created_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or public.auth_user_is_subject_teacher_of_class(class_id))
  );

drop policy if exists seating_plans_staff_update on public.seating_plans;
create policy seating_plans_staff_update on public.seating_plans
  for update using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or (created_by = auth.uid()
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  ) with check (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or (created_by = auth.uid()
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );

-- The Supabase default grant these tables were created with.
grant all on public.room_layouts  to anon;
grant all on public.seating_plans to anon;
