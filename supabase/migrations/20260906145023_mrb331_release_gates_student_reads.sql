-- MRB-331 — an unreleased assignment does not exist, as far as a student is
-- concerned, and the database is where that is said.
--
-- ⚠️ VERSION IS LOAD-BEARING, AND IT IS NOT THE ONE THIS FILE WAS FIRST GIVEN.
-- MCP `apply_migration` records its OWN `schema_migrations` version rather
-- than reading a filename. TEST recorded 20260906145023; the file was written
-- as ...145530 and renamed to match. Read the version back after applying and
-- rename, every time — a mismatch makes `supabase db push` re-apply the whole
-- file on the next run.
--
-- The brief's rule is "nothing reaches a student before the hold". The backend
-- could enforce that in `/api/class/current-assignment` alone, and it would
-- work for every read that goes through the backend. It would not cover a read
-- that does not: `shared/student-live.js` and `shared/student-data.js` hold
-- direct PostgREST reads of `assignments`, and the student's work list is one
-- of them. A backend-only check would leave that list showing next Monday's
-- title today — silently, and looking completely normal.
--
-- So the release lives in RLS, and the backend check is a second layer rather
-- than the only one.
--
-- ⚠️ `release_at IS NULL` MUST STAY VISIBLE. Every assignment that exists
-- today has a NULL release, including the two pre-term ones on Rainford's
-- 8r/Sc1 that MRB-324 went out of its way not to retract. A policy that
-- required a non-null stamp would retract them the moment it applied.

drop policy if exists assignments_student_read on public.assignments;
create policy assignments_student_read on public.assignments
  for select
  using (
    class_school_id(class_id) = auth_user_school_id()
    and auth_user_is_member_of_class(class_id)
    and (release_at is null or release_at <= now())
  );

-- The questions go with it. Without this a student who knew an assignment id
-- could read next week's questions out of `assignment_questions` while the
-- assignment row itself stayed invisible — the paper without its cover.
drop policy if exists aq_student_read on public.assignment_questions;
create policy aq_student_read on public.assignment_questions
  for select
  using (
    exists (
      select 1
      from assignments a
      join class_members cm
        on cm.class_id = a.class_id
       and cm.left_at is null
       and cm.deleted_at is null
      where a.id = assignment_questions.assignment_id
        and cm.student_id = auth_user_id()
        and (a.release_at is null or a.release_at <= now())
    )
  );

-- ⚠️ TEACHERS, HODS, ADMINS AND OPERATORS ARE DELIBERATELY UNTOUCHED.
-- A teacher must see work they have scheduled for next Monday — that is the
-- entire point of being able to set it in advance — so no release clause goes
-- on `assignments_teacher_read`, `assignments_teacher_write`,
-- `assignments_hod_read`, `assignments_admin_read`, `assignments_admin_write`,
-- `assignments_operator_read`, `aq_teacher_all`, `aq_admin_read` or
-- `aq_operator_read`.
--
-- ⚠️ `cm.deleted_at is null` IS CARRIED FORWARD, not newly added. It arrived in
-- 20260820091413 ("soft delete ends access, the other two") and rewriting this
-- policy without it would silently restore a soft-deleted member's read.
