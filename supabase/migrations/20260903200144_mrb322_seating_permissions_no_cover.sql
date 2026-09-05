-- ════════════════════════════════════════════════════════════════════════
-- MRB-322 follow-up — seating permissions, ruled 3 Sep 2026.
--
-- COVER IS REMOVED FROM SEATING ENTIRELY. Not narrowed, not time-boxed:
-- removed. A cover teacher is staff, so they still read the room layouts —
-- desk geometry, no children. They do not read, create, edit or retire a
-- seating plan, because a seating plan is a named list of children and
-- standing in a room for a fortnight is not the same as being given that
-- list. Whether cover should ever see one is a safeguarding question with
-- an owner, and the owner is not this migration.
--
-- Three things change:
--
--   1 · the helper.  auth_user_teaches_class_now() counted ANY live
--       class_teachers row, cover included, and is dropped. Its replacement
--       asks the one question seating actually wants asked.
--   2 · room_layouts. The read was the whole school, which includes every
--       pupil in it. Now staff only.
--   3 · seating_plans. Read and write both go through the new helper, so
--       cover — active or expired — is outside all four verbs.
--
-- Every policy below is rewritten whole rather than patched, because a
-- permission you have to assemble out of three migrations to read is a
-- permission nobody will read.
-- ════════════════════════════════════════════════════════════════════════

-- ── 1 · the helper ──────────────────────────────────────────────────────
--
-- "Subject teacher or co-teacher" is one row shape, not two: co-teaching is
-- two `subject_teacher` rows on the same class, and there is no separate
-- co-teacher role to check for. So the test is role = 'subject_teacher',
-- and the two roles that are NOT it are excluded on purpose:
--
--   cover_teacher  the ruling. Cover does not see the children's names.
--   form_tutor     a pastoral attachment to a form, not a teaching one to
--                  this class's lessons. A form tutor who also teaches the
--                  class has a subject_teacher row as well and passes on
--                  that one.
--
-- `ended_at is null` is deliberately the SAME liveness test the estate's
-- auth_user_teaches_class() uses, and that alignment is the point. Anyone
-- who can read a seating plan can therefore also read the class and its
-- register through the existing policies — so the page never has to render
-- a plan whose names it cannot resolve. Diverging here is exactly what
-- produced the cover seam this migration removes.
create or replace function public.auth_user_is_subject_teacher_of_class(p_class_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.class_teachers
     where class_id   = p_class_id
       and teacher_id = auth.uid()
       and role       = 'subject_teacher'
       and ended_at   is null
       and deleted_at is null
  );
$$;

comment on function public.auth_user_is_subject_teacher_of_class(uuid) is
  'MRB-322, ruled 3 Sep 2026. True when the caller holds a live '
  'subject_teacher row on this class — which covers co-teaching, since a '
  'co-teacher is a second subject_teacher row. cover_teacher and form_tutor '
  'rows do not count: a seating plan is a named list of children. Seating '
  'is the only caller.';

-- ════════════════════════════════════════════════════════════════════════
-- 2 · room_layouts — staff read, staff author, author-or-admin edit
-- ════════════════════════════════════════════════════════════════════════

-- READ. Was `school_id = auth_user_school_id()` and nothing else, and
-- auth_user_school_id() resolves for a pupil just as well as for a teacher,
-- so every child in the school could list every room layout in it. Nothing
-- student-facing has ever asked for one.
drop policy if exists room_layouts_school_read on public.room_layouts;
drop policy if exists room_layouts_staff_read  on public.room_layouts;
create policy room_layouts_staff_read on public.room_layouts
  for select using (
    school_id = public.auth_user_school_id()
    and public.auth_user_role() in ('teacher', 'admin')
  );

-- INSERT. One policy, not two: the previous pair let an admin insert a row
-- with someone else's uuid in created_by, because only the teacher branch
-- carried `created_by = auth.uid()`. An admin creating a layout is its
-- author like anyone else.
drop policy if exists room_layouts_author_insert on public.room_layouts;
drop policy if exists room_layouts_admin_insert  on public.room_layouts;
drop policy if exists room_layouts_staff_insert  on public.room_layouts;
create policy room_layouts_staff_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and created_by = auth.uid()
    and public.auth_user_role() in ('teacher', 'admin')
  );

-- UPDATE, which is also how a layout is retired — soft delete only.
--
-- ⚠️ No `deleted_at is null` in USING, and that is deliberate. Postgres
-- applies the SELECT policy to a row's POST-update state, so a policy that
-- hid retired rows would make the retirement itself fail with 42501
-- (CLAUDE.md, MRB-46 Phase 2). Filtering retired rows is the client's job.
--
-- The author branch now carries role = 'teacher' as well as authorship.
-- Authorship alone was load-bearing on an INSERT policy that had already
-- been shown to let the wrong people write, and a permission should not
-- depend on another policy having held.
drop policy if exists room_layouts_author_update on public.room_layouts;
drop policy if exists room_layouts_staff_update  on public.room_layouts;
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

-- No DELETE policy at all: a saved plan points at a layout, so a hard delete
-- would orphan it.

-- ════════════════════════════════════════════════════════════════════════
-- 3 · seating_plans — the class's own teachers, and school admins
-- ════════════════════════════════════════════════════════════════════════

-- READ. Two policies became one, because two SELECT policies OR together
-- and reading a permission that is spread across two rows of pg_policies is
-- how the cover branch survived a review in the first place.
--
-- The teacher branch here is the helper alone, with no profiles.role conjunct.
--
-- ⚠️ SUPERSEDED by 20260903203226, which adds that conjunct. The reasoning
-- below was "a pupil cannot acquire a subject_teacher row, since every INSERT
-- policy on class_teachers is staff-gated". Every RLS policy is — but the
-- roster-import edge function runs on the service role, where RLS does not
-- apply, and takes the teacher id straight from its request body. Left here
-- as written, because the shape of the mistake is worth keeping: the check
-- was real, it was just not a check on the only door.
drop policy if exists seating_plans_teacher_read on public.seating_plans;
drop policy if exists seating_plans_admin_read   on public.seating_plans;
drop policy if exists seating_plans_staff_read   on public.seating_plans;
create policy seating_plans_staff_read on public.seating_plans
  for select using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or public.auth_user_is_subject_teacher_of_class(class_id))
  );

-- INSERT. `created_by = auth.uid()` is outside the branch, so it binds the
-- admin too: a plan is always authored by whoever made it.
drop policy if exists seating_plans_author_insert on public.seating_plans;
drop policy if exists seating_plans_admin_insert  on public.seating_plans;
drop policy if exists seating_plans_staff_insert  on public.seating_plans;
create policy seating_plans_staff_insert on public.seating_plans
  for insert with check (
    created_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_role() = 'admin'
         or public.auth_user_is_subject_teacher_of_class(class_id))
  );

-- UPDATE, which is also the soft delete.
--
-- The author branch says "and STILL teaches it": authoring a plan in
-- September does not license writing to it after you have handed the class
-- over in January.
--
-- WITH CHECK repeats the whole scope, class_id included, and that is the
-- load-bearing half. Both class_school_id(class_id) and the helper are
-- re-evaluated against the POST-update row, so `set class_id = <a class you
-- do not teach>` fails — which is the shape of the hole the previous
-- migration closed, restated here rather than inherited.
drop policy if exists seating_plans_author_update on public.seating_plans;
drop policy if exists seating_plans_staff_update  on public.seating_plans;
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

-- No DELETE policy: soft delete only.

-- ── 4 · retire the cover-aware helper ───────────────────────────────────
-- Last, and only once nothing references it. Seating was its only caller;
-- it was added by 20260902214105 for the cover reading that has now been
-- ruled away, so it goes with the ruling rather than being left about as a
-- loaded gun with a plausible name.
drop function if exists public.auth_user_teaches_class_now(uuid);
