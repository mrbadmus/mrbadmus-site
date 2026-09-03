-- ROLLBACK for 20260903200144. Apply by hand only.
--
-- ⚠️ This puts COVER BACK INSIDE SEATING and re-opens the pupil read. After
-- running it: every pupil in the school can list every room layout again, and
-- an ACTIVE cover teacher can read, create and edit the seating plan for the
-- class they are covering — a named list of children handed to someone the
-- ruling of 3 Sep 2026 says should not have it.
--
-- It exists because a rollback that only half-restores is worse than none, and
-- because the estate's rule is that every forward migration has an undo. It is
-- not a thing to run to "unstick" a deploy. Nothing in the seating page needs
-- it: the page was rewritten alongside the forward migration and does not read
-- or write anything these wider policies would newly allow.
--
-- Order matters and is the exact reverse of the forward file: the helper the
-- old policies depend on has to exist BEFORE the policies that call it, and
-- the helper this migration introduced can only be dropped once nothing
-- references it.

-- ── 1 · bring back the cover-aware helper ───────────────────────────────
create or replace function public.auth_user_teaches_class_now(p_class_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.class_teachers
     where class_id  = p_class_id
       and teacher_id = auth.uid()
       and deleted_at is null
       and (started_at is null or started_at <= now())
       and (ended_at   is null or ended_at   >  now())
  );
$$;

comment on function public.auth_user_teaches_class_now(uuid) is
  'MRB-322. Interval-aware sibling of auth_user_teaches_class: true while the '
  'caller''s class_teachers row has started and has not yet ended, so ACTIVE '
  'cover counts and expired cover does not.';

-- ── 2 · room_layouts, back to the whole school ──────────────────────────
drop policy if exists room_layouts_staff_read on public.room_layouts;
create policy room_layouts_school_read on public.room_layouts
  for select using (school_id = public.auth_user_school_id());

drop policy if exists room_layouts_staff_insert on public.room_layouts;
create policy room_layouts_author_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and created_by = auth.uid()
    and public.auth_user_role() in ('teacher', 'hod', 'admin')
  );

create policy room_layouts_admin_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and public.auth_user_role() = 'admin'
  );

drop policy if exists room_layouts_staff_update on public.room_layouts;
create policy room_layouts_author_update on public.room_layouts
  for update using (
    school_id = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  ) with check (
    school_id = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  );

-- ── 3 · seating_plans, back to the two-policy cover-aware shape ─────────
drop policy if exists seating_plans_staff_read on public.seating_plans;
create policy seating_plans_teacher_read on public.seating_plans
  for select using (
    public.auth_user_teaches_class_now(class_id)
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

create policy seating_plans_admin_read on public.seating_plans
  for select using (
    public.auth_user_role() = 'admin'
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

drop policy if exists seating_plans_staff_insert on public.seating_plans;
create policy seating_plans_author_insert on public.seating_plans
  for insert with check (
    created_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and public.auth_user_teaches_class_now(class_id)
  );

create policy seating_plans_admin_insert on public.seating_plans
  for insert with check (
    public.auth_user_role() = 'admin'
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

drop policy if exists seating_plans_staff_update on public.seating_plans;
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

-- ── 4 · retire the helper this migration introduced ─────────────────────
-- Last, once nothing references it.
drop function if exists public.auth_user_is_subject_teacher_of_class(uuid);
