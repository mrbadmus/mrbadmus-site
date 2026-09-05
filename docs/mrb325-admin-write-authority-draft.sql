-- ═══════════════════════════════════════════════════════════════════════
-- DRAFT — NOT APPLIED. Proposed migration, pending Mide's review.
-- ═══════════════════════════════════════════════════════════════════════
--
-- MRB-325 ruling 5 asked for "full teacher capability" when a school_admin
-- opens a class they do not personally teach. The frontend fix that ships
-- with this ticket (shared/teacher-live.js: mergeForeignClass) covers
-- everything the EXISTING RLS already permits for role='admin' — viewing
-- any class, its roster, its assignments, and read+write on seating plans
-- (classes, class_teachers, class_members, assignments, seating_plans and
-- room_layouts all already carry a role='admin' policy, several of them
-- FOR ALL). That required no schema change.
--
-- Three tables do NOT have an admin write path, checked against every live
-- migration rather than assumed:
--   · assignment_submissions  — marking a student's work
--   · class_shoutouts         — no admin policy of any kind, not even read
--   · submission_feedback     — admin can already SELECT; not write
--
-- This ticket's DB-write allowance was scoped to one thing only (seeding
-- school_period_times for Rainford) and explicitly banned `db push`, so
-- this file is drafted and left UNAPPLIED rather than run. It is not
-- referenced by anything and `supabase db push` will not pick it up from
-- `docs/` — move it into `supabase/migrations/` under a fresh timestamp,
-- after Mide has ruled on the shape below, to make it live.
--
-- Judgement calls a reviewer should check before approving:
--   · Is "any admin, any class in the school" the right scope for MARKING,
--     or should it require the admin to also hold a specific rostering
--     reason (cover, investigation)? The read-side precedent (classes,
--     assignments) draws no such line, so this mirrors it for consistency
--     — but marking changes a grade a real teacher will see, which the
--     read-only precedents do not.
--   · class_shoutouts currently has NO admin policy at all, including
--     read — this draft adds read+insert, matching the "full teacher
--     capability" ask. Consider whether shoutouts, being praise sent to a
--     student's own page, should stay teacher-authored only.
--   · submission_feedback's SELECT comment explicitly says written
--     feedback is "more sensitive than a submission count" and deliberately
--     stopped at read. This draft's WRITE arm reverses that stance — flag
--     for explicit confirmation, don't assume it carries over.
--
-- ═══════════════════════════════════════════════════════════════════════

-- assignment_submissions — admin write (marking), mirroring the existing
-- auth_user_role()='admin' shape used elsewhere on this table's read side.
drop policy if exists submissions_admin_write on public.assignment_submissions;
create policy submissions_admin_write on public.assignment_submissions for update
  using (
    public.auth_user_role() = 'admin'
    and exists (
      select 1 from public.classes c
      where c.id = assignment_submissions.class_id
        and c.school_id = public.auth_user_school_id()
    )
  )
  with check (
    public.auth_user_role() = 'admin'
    and exists (
      select 1 from public.classes c
      where c.id = assignment_submissions.class_id
        and c.school_id = public.auth_user_school_id()
    )
  );

-- class_shoutouts — admin read (currently absent) + insert, same
-- same-school + role='admin' shape.
drop policy if exists class_shoutouts_admin_read on public.class_shoutouts;
create policy class_shoutouts_admin_read on public.class_shoutouts for select
  using (
    public.auth_user_role() = 'admin'
    and exists (
      select 1 from public.classes c
      where c.id = class_shoutouts.class_id
        and c.school_id = public.auth_user_school_id()
    )
  );

drop policy if exists class_shoutouts_admin_insert on public.class_shoutouts;
create policy class_shoutouts_admin_insert on public.class_shoutouts for insert
  with check (
    public.auth_user_role() = 'admin'
    and exists (
      select 1 from public.classes c
      where c.id = class_shoutouts.class_id
        and c.school_id = public.auth_user_school_id()
    )
  );

-- submission_feedback — admin write. Deliberately a SEPARATE policy from
-- the teacher-authored one so it can be reviewed/dropped independently;
-- see the judgement-call note above before approving this one.
drop policy if exists submission_feedback_admin_insert on public.submission_feedback;
create policy submission_feedback_admin_insert on public.submission_feedback for insert
  with check (
    public.auth_user_role() = 'admin'
    and public.class_school_id(submission_feedback.class_id) = public.auth_user_school_id()
  );

drop policy if exists submission_feedback_admin_update on public.submission_feedback;
create policy submission_feedback_admin_update on public.submission_feedback for update
  using (
    public.auth_user_role() = 'admin'
    and public.class_school_id(submission_feedback.class_id) = public.auth_user_school_id()
  )
  with check (
    public.auth_user_role() = 'admin'
    and public.class_school_id(submission_feedback.class_id) = public.auth_user_school_id()
  );
