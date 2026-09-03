-- ════════════════════════════════════════════════════════════════════════
-- MRB-322 follow-up, part 3 — "admin" on the seating tables now means the
-- school_admin SCOPE, not profiles.role = 'admin'.
--
-- Ruled by Mide, 3 September 2026. Explicitly authorised for production.
--
-- WHY. Seating was the only surface in the estate still reading
-- `auth_user_role() = 'admin'`. On production that string names exactly one
-- person — an account holding no staff scopes at all, and therefore unable
-- to read a class or a register, so the seating powers it was granted were
-- powers over rows it could never navigate to. Meanwhile the three people
-- who actually administer the school are `role = 'teacher'` carrying the
-- `school_admin` SCOPE, and seating gave them nothing.
--
-- The rest of the estate — assignment_questions, timetable_entries,
-- pending-staff claim, student notifications — has used
-- `auth_user_has_scope('school_admin')` since MRB-293. Seating now says the
-- same thing in the same words.
--
-- ⚠️ NOBODY LOSES ACCESS. `auth_user_has_scope()` still carries its M1
-- dual-read fallback:
--
--     or (p_scope = 'school_admin' and exists (
--           select 1 from public.profiles p
--            where p.id = auth.uid() and p.role = 'admin'))
--
-- so `has_scope('school_admin')` is a strict SUPERSET of
-- `auth_user_role() = 'admin'`. This migration only widens, and it widens
-- onto the seam the estate will retire that fallback through — when the
-- final advisory flip removes it, seating retires with everything else
-- rather than being the one table left behind holding a role string.
--
-- WHAT DOES NOT CHANGE. The school seal is untouched. Every policy keeps
-- `school_id = auth_user_school_id()` / `class_school_id(class_id) =
-- auth_user_school_id()` as a conjunct OUTSIDE the admin branch, so a
-- school_admin reaches their own school's rows and no further. The teacher
-- branches — authorship on room_layouts, live subject_teacher on
-- seating_plans — are copied across byte for byte. A teacher without the
-- scope sees exactly what they saw before this ran.
-- ════════════════════════════════════════════════════════════════════════

-- ── 1 · room_layouts ────────────────────────────────────────────────────
--
-- READ. The old `auth_user_role() in ('teacher','admin')` becomes an
-- explicit two-branch disjunction. Written out rather than left as an array
-- membership test because the two halves are no longer the same kind of
-- claim: one reads a column on profiles, the other reads a live row in
-- staff_scopes.
drop policy if exists room_layouts_staff_read on public.room_layouts;
create policy room_layouts_staff_read on public.room_layouts
  for select using (
    school_id = public.auth_user_school_id()
    and (public.auth_user_role() = 'teacher'
         or public.auth_user_has_scope('school_admin'))
  );

-- INSERT. `created_by = auth.uid()` stays outside the branch, so a layout is
-- always authored by whoever made it — the school_admin included.
drop policy if exists room_layouts_staff_insert on public.room_layouts;
create policy room_layouts_staff_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and created_by = auth.uid()
    and (public.auth_user_role() = 'teacher'
         or public.auth_user_has_scope('school_admin'))
  );

-- UPDATE, which is also how a layout is retired — soft delete only.
--
-- ⚠️ Still no `deleted_at is null` in USING, and still deliberate: Postgres
-- applies the SELECT policy to a row's POST-update state, so a policy that
-- hid retired rows would make the retirement itself fail with 42501
-- (CLAUDE.md, MRB-46 Phase 2). Filtering retired rows is the client's job.
--
-- This is the branch that gives a school_admin something they did not have:
-- a plain teacher may only edit a layout they authored, a school_admin may
-- edit any layout in their school. That is the ruling's "edit any layout".
drop policy if exists room_layouts_staff_update on public.room_layouts;
create policy room_layouts_staff_update on public.room_layouts
  for update using (
    school_id = public.auth_user_school_id()
    and ((created_by = auth.uid() and public.auth_user_role() = 'teacher')
         or public.auth_user_has_scope('school_admin'))
  ) with check (
    school_id = public.auth_user_school_id()
    and ((created_by = auth.uid() and public.auth_user_role() = 'teacher')
         or public.auth_user_has_scope('school_admin'))
  );

-- No DELETE policy at all: a saved plan points at a layout, so a hard delete
-- would orphan it.

-- ── 2 · seating_plans ───────────────────────────────────────────────────
--
-- READ. A school_admin reads every plan in their school; a teacher reads the
-- plans of classes they currently subject-teach, and the staff conjunct that
-- 20260903203226 added stays exactly where it was.
drop policy if exists seating_plans_staff_read on public.seating_plans;
create policy seating_plans_staff_read on public.seating_plans
  for select using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_has_scope('school_admin')
         or (public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );

-- INSERT. This is the ruling's "create a plan for any class": a school_admin
-- is not required to teach the class, only to be in its school.
drop policy if exists seating_plans_staff_insert on public.seating_plans;
create policy seating_plans_staff_insert on public.seating_plans
  for insert with check (
    created_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_has_scope('school_admin')
         or (public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );

-- UPDATE, which is also the soft delete.
--
-- The teacher branch still says "you authored it AND you still teach it":
-- authoring a plan in September does not license writing to it after you
-- have handed the class over in January.
--
-- ⚠️ WITH CHECK repeats the whole scope, class_id included, and that is the
-- load-bearing half. class_school_id(class_id) and the helper are both
-- re-evaluated against the POST-update row, so `set class_id = <a class you
-- do not teach>` fails. Restated here rather than inherited.
drop policy if exists seating_plans_staff_update on public.seating_plans;
create policy seating_plans_staff_update on public.seating_plans
  for update using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_has_scope('school_admin')
         or (created_by = auth.uid()
             and public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  ) with check (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (public.auth_user_has_scope('school_admin')
         or (created_by = auth.uid()
             and public.auth_user_role() = 'teacher'
             and public.auth_user_is_subject_teacher_of_class(class_id)))
  );

-- No DELETE policy: soft delete only.
