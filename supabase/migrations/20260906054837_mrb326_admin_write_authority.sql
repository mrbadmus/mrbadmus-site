-- ═══════════════════════════════════════════════════════════════════════
-- MRB-326 — admin write authority on a class the admin does not teach.
-- ═══════════════════════════════════════════════════════════════════════
--
-- MRB-325 ruling 5 let a school_admin OPEN a colleague's class. It stopped
-- there: every read policy on the estate already had an admin arm, and no
-- write policy did. So an admin could see a foreign class in full and then
-- be refused by RLS on every single thing they tried to do in it — mark,
-- comment, praise, chase. "Opens but cannot act" is what shipped, and this
-- migration is the half that was missing.
--
-- Four tables, seven policies. Each is a SEPARATE, NAMED policy sitting
-- alongside the teacher-facing one rather than a widening of it, so any one
-- of them can be reviewed, disabled or dropped on its own without touching
-- what a classroom teacher can do. `supabase/rollbacks/` drops all seven.
--
-- ── The condition, and why it is this one ──────────────────────────────
--
--   public.auth_user_has_scope('school_admin')  AND  <same school>
--
-- NOT `auth_user_role() = 'admin'`, which is what the MRB-325 draft in
-- `docs/` used. The admin concept on this platform is the SCOPE — MRB-322's
-- "seating_admin_is_scope" ruling — and `auth_user_has_scope` already
-- dual-reads `profiles.role = 'admin'` as its M1 fallback, so the scope
-- function is a superset of the role test and nothing that worked before
-- stops working. Every recent policy on the estate (seating_plans,
-- room_layouts, submission_feedback_select, student_notifications_admin_read)
-- is written this way; these follow it.
--
-- ⚠️ `slt` IS DELIBERATELY EXCLUDED. Several READ policies grant
-- `school_admin OR slt`. None of these do. SLT is an oversight role — it
-- looks at the school — and nothing in ruling 5 asks for a member of SLT to
-- be able to change a mark or write to a child's page.
--
-- ── What each policy KEEPS from its teacher-facing twin ────────────────
--
-- The draft dropped these; dropping them would have made the admin policy
-- MORE permissive than the teacher one, which is not what "full teacher
-- capability" means:
--
--   · `author_id = auth.uid()`  (shoutouts) and `teacher_id = auth.uid()`
--     (feedback) and `sent_by = auth.uid()` (notifications) — you write as
--     yourself. An admin must not be able to post under a colleague's name,
--     and the pages already show "You" vs "Another teacher" off exactly
--     these columns.
--   · the recipient-is-a-current-member subquery on shoutouts — praise goes
--     to a child in the class, admin or not.
--
-- ── One correction the draft could not have known ─────────────────────
--
-- `assignment_submissions` HAS NO `class_id` COLUMN. The draft wrote
-- `assignment_submissions.class_id`; that would have failed to apply. Every
-- existing policy on the table reaches the class through `assignments`, and
-- so does this one.
--
-- ── One table the draft did not name ──────────────────────────────────
--
-- `student_notifications` — the class screen's "Remind" control, through
-- `sendReminders()`. Its insert policy is `sent_by = auth.uid() AND
-- auth_user_teaches_class(class_id)`, so it blocked an admin exactly like
-- the other three. Found by auditing the control rather than the draft.
--
-- ── Judgement calls, carried forward from the draft for the record ─────
--
--   · MARKING changes a grade a real teacher will see, which the read-only
--     admin precedents do not. Scoped here to any school_admin, any class
--     in their own school — the same line every read policy draws — rather
--     than requiring a rostered reason (cover, investigation), because
--     there is no such concept in the schema to hang it on.
--   · `submission_feedback`'s SELECT comment says written feedback is "more
--     sensitive than a submission count" and deliberately stopped at read.
--     This reverses that stance for WRITE. It is a separate named policy so
--     that reversal can be undone by itself.
--
-- Retention is untouched: `submission_feedback_edited_chk` still forces an
-- edit to carry `prior_body`, and neither table has a DELETE policy for
-- anyone, so "remove" stays a soft delete for an admin exactly as it is for
-- a teacher.
-- ═══════════════════════════════════════════════════════════════════════

-- ── assignment_submissions — marking ──────────────────────────────────
drop policy if exists submissions_admin_write on public.assignment_submissions;
create policy submissions_admin_write on public.assignment_submissions for update
  using (
    public.auth_user_has_scope('school_admin')
    and exists (
      select 1 from public.assignments a
      where a.id = assignment_submissions.assignment_id
        and public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  )
  with check (
    public.auth_user_has_scope('school_admin')
    and exists (
      select 1 from public.assignments a
      where a.id = assignment_submissions.assignment_id
        and public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  );

-- ── class_shoutouts — read, post, and remove your own ─────────────────
--
-- ⚠️ The READ policy may already be redundant. On the TEST project
-- `class_shoutouts_select` has grown a `school_admin` arm; the migration
-- that did it is not in this repo, so it was applied ad hoc and production
-- may well still carry the narrow version from 20260524104500. A second
-- permissive SELECT policy simply ORs in, so this is correct either way and
-- costs nothing where it is redundant.
drop policy if exists class_shoutouts_admin_read on public.class_shoutouts;
create policy class_shoutouts_admin_read on public.class_shoutouts for select
  using (
    public.auth_user_has_scope('school_admin')
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

drop policy if exists class_shoutouts_admin_insert on public.class_shoutouts;
create policy class_shoutouts_admin_insert on public.class_shoutouts for insert
  with check (
    public.auth_user_has_scope('school_admin')
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and author_id = auth.uid()
    and recipient_id in (
      select cm.student_id from public.class_members cm
      where cm.class_id = class_shoutouts.class_id
        and cm.left_at is null
        and cm.deleted_at is null
    )
  );

-- The "Remove" control. `author_id = auth.uid()` is kept: an admin removes
-- what an admin wrote, and a colleague's praise is not theirs to retract.
drop policy if exists class_shoutouts_admin_update on public.class_shoutouts;
create policy class_shoutouts_admin_update on public.class_shoutouts for update
  using (
    public.auth_user_has_scope('school_admin')
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and author_id = auth.uid()
  )
  with check (
    public.auth_user_has_scope('school_admin')
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and author_id = auth.uid()
  );

-- ── submission_feedback — write and edit your own ─────────────────────
drop policy if exists submission_feedback_admin_insert on public.submission_feedback;
create policy submission_feedback_admin_insert on public.submission_feedback for insert
  with check (
    public.auth_user_has_scope('school_admin')
    and teacher_id = auth.uid()
    and public.class_school_id(public.submission_class_id(submission_id))
        = public.auth_user_school_id()
  );

drop policy if exists submission_feedback_admin_update on public.submission_feedback;
create policy submission_feedback_admin_update on public.submission_feedback for update
  using (
    public.auth_user_has_scope('school_admin')
    and teacher_id = auth.uid()
    and public.class_school_id(public.submission_class_id(submission_id))
        = public.auth_user_school_id()
  )
  with check (
    public.auth_user_has_scope('school_admin')
    and teacher_id = auth.uid()
    and public.class_school_id(public.submission_class_id(submission_id))
        = public.auth_user_school_id()
  );

-- ── student_notifications — the Remind control ────────────────────────
drop policy if exists student_notifications_admin_send on public.student_notifications;
create policy student_notifications_admin_send on public.student_notifications for insert
  with check (
    public.auth_user_has_scope('school_admin')
    and sent_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );
