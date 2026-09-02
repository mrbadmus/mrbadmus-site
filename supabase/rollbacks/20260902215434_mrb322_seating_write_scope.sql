-- ROLLBACK for 20260902215434. Apply by hand only.
--
-- ⚠️ This restores the WIDER policies. It re-opens both holes: a plan can be
-- moved onto a class the writer does not teach, and any signed-in pupil can
-- create room layouts. Only run it to unblock something worse.
drop policy if exists seating_plans_author_update on public.seating_plans;
create policy seating_plans_author_update on public.seating_plans
  for update using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  ) with check (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  );

drop policy if exists room_layouts_author_insert on public.room_layouts;
create policy room_layouts_author_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and created_by = auth.uid()
  );
