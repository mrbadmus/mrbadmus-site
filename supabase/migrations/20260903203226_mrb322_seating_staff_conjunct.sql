-- ════════════════════════════════════════════════════════════════════════
-- MRB-322 follow-up, part 2 — the staff conjunct the previous migration
-- reasoned its way out of, and a default grant nobody asked for.
--
-- Found by a cold read of 20260903200144 whose brief was "find a signed-in
-- pupil or cover teacher a path to any seating row". It could not find one
-- through RLS. It found one through the door beside it.
-- ════════════════════════════════════════════════════════════════════════

-- ── 1 · seating_plans: the teacher branch now checks that you are staff ──
--
-- 20260903200144 left `profiles.role` out of the teacher branch on purpose,
-- and said why:
--
--     "Holding a live subject_teacher row IS the staff test — a pupil cannot
--      acquire one, since every INSERT policy on class_teachers is staff-gated"
--
-- Every RLS insert policy on class_teachers is indeed staff-gated. That was
-- the wrong thing to check. `supabase/functions/roster-import/index.ts` runs
-- on the SERVICE ROLE — RLS does not apply to it at all — and it inserts
-- `class_teachers { role: 'subject_teacher', teacher_id: <from the request
-- body> }` without ever comparing that id to the caller, to the school, or to
-- the target's role. So a staff caller can hand a live subject_teacher row to
-- any uuid in the profiles table, a pupil's included, and under the old
-- policy that pupil then read a named list of children.
--
-- The premise was false, so the conclusion goes. The ruling's own words are
-- "a TEACHER who is a subject teacher or co-teacher of that class", and this
-- is that sentence written out.
--
-- ⚠️ This does NOT fix roster-import, which is a much wider hole than
-- seating — it lets one teacher attach ANY teacher to a class they invent —
-- and it belongs to whoever owns that function. This narrows seating so that
-- seating does not depend on it. Written up for Mide.
--
-- The role set matches room_layouts' ('teacher','admin') so that "staff"
-- means one thing across both seating tables rather than two.
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

-- ── 2 · take the anon grants off both tables ────────────────────────────
--
-- `anon` holds SELECT/INSERT/UPDATE/DELETE/TRUNCATE on both seating tables.
-- Nothing granted them deliberately; it is the project-wide default that
-- fires on every new table. RLS already refuses anon on all four verbs —
-- `auth.uid()` is null, so every policy evaluates false — so this changes no
-- behaviour today. It is removed anyway, because the seating surface is
-- staff-only by ruling and a table-level grant to the signed-out role is a
-- second thing that has to keep being true.
revoke all on public.room_layouts  from anon;
revoke all on public.seating_plans from anon;
