-- MRB-348 WS-3 — consolidate multiple permissive RLS policies.
-- A PERFORMANCE migration with NO semantic change.
--
-- ==========================================================================
-- WHAT WAS WRONG
-- ==========================================================================
-- Supabase's performance linter raises `multiple_permissive_policies` once
-- per (table, role, command) cell holding more than one PERMISSIVE policy.
-- Production reports 251 findings. Nearly every policy on this estate is
-- granted to `public`, and the linter expands `public` across the 4-5
-- concrete roles, so ONE table with 5 permissive SELECT policies is
-- reported 20 times.
--
-- Permissive policies are OR'd, and Postgres walks every branch until one
-- is true. MRB-347 made each branch cheap by hoisting the per-request auth
-- calls into InitPlans; it did not reduce the NUMBER of branches, nor fix
-- their order. This migration does both: one policy per (table, command),
-- with the cheapest branch written first.
--
-- ==========================================================================
-- THE TRANSFORM
-- ==========================================================================
-- Step 1. Every PERMISSIVE cmd='ALL' policy is expanded into four
--   per-command equivalents before anything is merged, because an ALL
--   policy also applies to SELECT and cannot be folded into a SELECT-only
--   policy without losing its write coverage:
--       SELECT  USING (qual)
--       DELETE  USING (qual)
--       UPDATE  USING (qual) WITH CHECK (with_check IF PRESENT ELSE qual)
--       INSERT  WITH CHECK (with_check IF PRESENT ELSE qual)
--
--   ⚠️ THE TRAP, and it is a silent one: that `ELSE qual` is Postgres
--   semantics, not a convenience. When an ALL/UPDATE/INSERT policy carries
--   no WITH CHECK, Postgres uses the USING expression AS the check.
--   Writing `true` there instead -- the obvious-looking default -- would
--   hand every authenticated user the right to write any row.
--
-- Step 2. Per (table, command):
--       merged USING      = OR over every policy's USING
--       merged WITH CHECK = OR over every policy's EFFECTIVE check,
--                           where effective = with_check if present else qual
--
--   ⚠️ WHY OR-ING THE TWO CLAUSES SEPARATELY IS EXACT. For an UPDATE under
--   several permissive policies, Postgres requires the OLD row to satisfy
--   at least one policy's USING and the NEW row to satisfy at least one
--   policy's WITH CHECK -- and they need NOT be the same policy. So
--   (U1 OR U2) with (C1 OR C2) is precisely the original behaviour. Had
--   Postgres instead required a single policy to satisfy both, this merge
--   would be a real widening and the transform would be unsound.
--
-- Step 3. Branches are ordered cheapest-first so the OR short-circuits:
--       0 pure column predicate   1 bare self-check   2 request-constant
--       3 school equality         4 row-dependent call   5 EXISTS (last)
--   A composite branch takes the cost of its dearest component.
--
-- Step 4. NOT TOUCHED, on purpose:
--   * RESTRICTIVE policies -- they AND rather than OR, so folding one into
--     the OR would be a security change. Any table carrying one is skipped
--     whole.
--   * policies granted to a role other than `public` -- merging across
--     differing GRANT sets changes who the policy reaches.
--   Both are listed at the foot of this file with their reasons.
--
-- ==========================================================================
-- WHY THIS FILE IS GENERATED AND PINNED, WHERE MRB-347's WAS SELF-APPLYING
-- ==========================================================================
-- MRB-347 rewrote whatever it found at apply time, because its transform
-- was idempotent and per-policy: hoisting a call it had already hoisted was
-- a no-op. THIS transform is neither. It drops policies and creates new
-- ones, and the merged expression depends on the exact set of policies
-- present. Run against a catalogue it was not generated from, a
-- self-applying version would merge the wrong set and say nothing.
--
-- So this file carries the expected qual/with_check of EVERY policy it
-- drops, and the guard block below refuses to proceed if the live
-- catalogue differs by so much as a byte. TEST and production policy sets
-- are NOT identical (141 policies on TEST, 153 on production), so this
-- matters: applied to a catalogue it does not match, this migration
-- ABORTS rather than mis-merging.
--
-- GENERATED FROM: project ref qeppkiswvclkkwbxmlok at 2026-09-22 02:05 UTC
-- Drops 97 policies across 25 tables; creates 78.
--
-- ⚠️ To land this on production, REGENERATE it against production's own
--    catalogue rather than applying this file:
--        python3 tools/rls_consolidate.py --project prod --emit \
--            --i-am-sure-production
--    The guard will otherwise abort, which is the safe direction.
--
-- REVERSIBLE: every original policy is kept in public.mrb348_policy_backup.
-- See supabase/rollbacks/ for the undo.
-- ==========================================================================

begin;

create table if not exists public.mrb348_policy_backup (
  schemaname text, tablename text, policyname text, permissive text,
  roles text, cmd text, qual text, with_check text,
  taken_at timestamptz default now()
);
revoke all on public.mrb348_policy_backup from public, anon, authenticated;

insert into public.mrb348_policy_backup
  (schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check)
select schemaname, tablename, policyname, permissive, roles::text, cmd, qual, with_check
from pg_policies
where schemaname = 'public'
  and not exists (select 1 from public.mrb348_policy_backup b
                  where b.tablename = pg_policies.tablename
                    and b.policyname = pg_policies.policyname);

-- --------------------------------------------------------------------------
-- GUARD. Abort unless every policy this migration drops is present with
-- exactly the expression it was generated against. This is what makes a
-- catalogue-pinned migration safe to attempt on an environment that may
-- have drifted.
-- --------------------------------------------------------------------------
do $guard$
declare expected record; live record; n int := 0;
begin
  for expected in
    select * from (values
      ($mrb348$academic_years$mrb348$, $mrb348$academic_years_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$academic_years$mrb348$, $mrb348$academic_years_member_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(school_id = ( SELECT auth_user_school_id() AS auth_user_school_id))$mrb348$, null),
      ($mrb348$assignment_question_attempts$mrb348$, $mrb348$attempts_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (EXISTS ( SELECT 1
   FROM (assignment_submissions s
     JOIN assignments a ON ((a.id = s.assignment_id)))
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))$mrb348$, null),
      ($mrb348$assignment_question_attempts$mrb348$, $mrb348$attempts_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM (assignment_submissions s
     JOIN assignments a ON ((a.id = s.assignment_id)))
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(a.subject_id))))$mrb348$, null),
      ($mrb348$assignment_question_attempts$mrb348$, $mrb348$attempts_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$assignment_question_attempts$mrb348$, $mrb348$attempts_self_all$mrb348$, $mrb348$ALL$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM assignment_submissions s
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (s.student_id = ( SELECT auth_user_id() AS auth_user_id)))))$mrb348$, null),
      ($mrb348$assignment_question_attempts$mrb348$, $mrb348$attempts_teacher_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM (assignment_submissions s
     JOIN assignments a ON ((a.id = s.assignment_id)))
  WHERE ((s.id = assignment_question_attempts.submission_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))$mrb348$, null),
      ($mrb348$assignment_questions$mrb348$, $mrb348$aq_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))$mrb348$, null),
      ($mrb348$assignment_questions$mrb348$, $mrb348$aq_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$assignment_questions$mrb348$, $mrb348$aq_student_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM (assignments a
     JOIN class_members cm ON (((cm.class_id = a.class_id) AND (cm.left_at IS NULL) AND (cm.deleted_at IS NULL))))
  WHERE ((a.id = assignment_questions.assignment_id) AND (cm.student_id = ( SELECT auth_user_id() AS auth_user_id)) AND ((a.release_at IS NULL) OR (a.release_at <= now())) AND (a.deleted_at IS NULL))))$mrb348$, null),
      ($mrb348$assignment_questions$mrb348$, $mrb348$aq_teacher_all$mrb348$, $mrb348$ALL$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))$mrb348$),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))$mrb348$, null),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_admin_write$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))$mrb348$),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(a.subject_id))))$mrb348$, null),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_self_all$mrb348$, $mrb348$ALL$mrb348$, $mrb348$(student_id = ( SELECT auth_user_id() AS auth_user_id))$mrb348$, null),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_teacher_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))$mrb348$, null),
      ($mrb348$assignment_submissions$mrb348$, $mrb348$submissions_teacher_update$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$(EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)))$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id))$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_student_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_member_of_class(class_id) AND ((release_at IS NULL) OR (release_at <= now())) AND (deleted_at IS NULL))$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_teacher_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id))$mrb348$, null),
      ($mrb348$assignments$mrb348$, $mrb348$assignments_teacher_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id))$mrb348$, null),
      ($mrb348$audit_log$mrb348$, $mrb348$audit_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)))$mrb348$, null),
      ($mrb348$audit_log$mrb348$, $mrb348$audit_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$audit_log$mrb348$, $mrb348$audit_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_self_insert$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$((student_id = ( SELECT auth_user_id() AS auth_user_id)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_self_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(student_id = ( SELECT auth_user_id() AS auth_user_id))$mrb348$, null),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_staff_insert$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR auth_user_teaches_class(class_id)))$mrb348$),
      ($mrb348$class_members$mrb348$, $mrb348$class_members_teacher_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(auth_user_teaches_class(class_id) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_shoutouts$mrb348$, $mrb348$class_shoutouts_admin_insert$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid)) AND (recipient_id IN ( SELECT cm.student_id
   FROM class_members cm
  WHERE ((cm.class_id = class_shoutouts.class_id) AND (cm.left_at IS NULL) AND (cm.deleted_at IS NULL)))))$mrb348$),
      ($mrb348$class_shoutouts$mrb348$, $mrb348$class_shoutouts_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_shoutouts$mrb348$, $mrb348$class_shoutouts_admin_update$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid)))$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid)))$mrb348$),
      ($mrb348$class_shoutouts$mrb348$, $mrb348$class_shoutouts_insert$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$(auth_user_teaches_class(class_id) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid)) AND (recipient_id IN ( SELECT cm.student_id
   FROM class_members cm
  WHERE ((cm.class_id = class_shoutouts.class_id) AND (cm.left_at IS NULL) AND (cm.deleted_at IS NULL)))))$mrb348$),
      ($mrb348$class_shoutouts$mrb348$, $mrb348$class_shoutouts_select$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(((deleted_at IS NULL) AND (auth_user_teaches_class(class_id) OR auth_user_is_member_of_class(class_id) OR (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))) OR ((deleted_at IS NOT NULL) AND ((author_id = ( SELECT auth.uid() AS uid)) OR (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))$mrb348$, null),
      ($mrb348$class_shoutouts$mrb348$, $mrb348$class_shoutouts_update$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$((author_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(class_id))$mrb348$, $mrb348$((author_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(class_id))$mrb348$),
      ($mrb348$class_teachers$mrb348$, $mrb348$class_teachers_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_teachers$mrb348$, $mrb348$class_teachers_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_teachers$mrb348$, $mrb348$class_teachers_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, null),
      ($mrb348$class_teachers$mrb348$, $mrb348$class_teachers_hod_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$(( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((subject_id IS NULL) OR auth_user_is_hod_of_subject_dept(subject_id)))$mrb348$, null),
      ($mrb348$class_teachers$mrb348$, $mrb348$class_teachers_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$class_teachers$mrb348$, $mrb348$class_teachers_self_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(teacher_id = ( SELECT auth_user_id() AS auth_user_id))$mrb348$, null),
      ($mrb348$classes$mrb348$, $mrb348$classes_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)))$mrb348$, null),
      ($mrb348$classes$mrb348$, $mrb348$classes_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$),
      ($mrb348$classes$mrb348$, $mrb348$classes_hod_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$classes$mrb348$, $mrb348$classes_hod_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope))$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope))$mrb348$),
      ($mrb348$classes$mrb348$, $mrb348$classes_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$classes$mrb348$, $mrb348$classes_student_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_member_of_class(id))$mrb348$, null),
      ($mrb348$classes$mrb348$, $mrb348$classes_teacher_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(id))$mrb348$, null),
      ($mrb348$classes$mrb348$, $mrb348$classes_teacher_update$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(id))$mrb348$, null),
      ($mrb348$family_messages$mrb348$, $mrb348$family_messages_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$family_messages$mrb348$, $mrb348$family_messages_party_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((deleted_at IS NULL) AND (org_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((sender_id = ( SELECT auth.uid() AS uid)) OR (recipient_id = ( SELECT auth.uid() AS uid))))$mrb348$, null),
      ($mrb348$pending_staff$mrb348$, $mrb348$pending_staff_admin_all$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$),
      ($mrb348$pending_staff$mrb348$, $mrb348$pending_staff_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$platform_flags$mrb348$, $mrb348$platform_flags_operator_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$),
      ($mrb348$platform_flags$mrb348$, $mrb348$platform_flags_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$true$mrb348$, null),
      ($mrb348$platform_operator_activations$mrb348$, $mrb348$operator_activations_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator)$mrb348$, null),
      ($mrb348$platform_operator_activations$mrb348$, $mrb348$operator_activations_operator_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator)$mrb348$, $mrb348$( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator)$mrb348$),
      ($mrb348$platform_operators$mrb348$, $mrb348$platform_operators_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator)$mrb348$, null),
      ($mrb348$platform_operators$mrb348$, $mrb348$platform_operators_operator_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator)$mrb348$, $mrb348$( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator)$mrb348$),
      ($mrb348$profiles$mrb348$, $mrb348$Users can view own profile$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(( SELECT auth.uid() AS uid) = id)$mrb348$, null),
      ($mrb348$profiles$mrb348$, $mrb348$profiles_admin_read_school$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)))$mrb348$, null),
      ($mrb348$profiles$mrb348$, $mrb348$profiles_hod_read_dept$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (((department IS NOT NULL) AND auth_user_is_hod_of_dept(department)) OR (role = 'student'::text)))$mrb348$, null),
      ($mrb348$profiles$mrb348$, $mrb348$profiles_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$profiles$mrb348$, $mrb348$profiles_teacher_read_students$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (role = 'student'::text) AND (EXISTS ( SELECT 1
   FROM class_members cm
  WHERE ((cm.student_id = profiles.id) AND auth_user_teaches_class(cm.class_id) AND (cm.left_at IS NULL)))))$mrb348$, null),
      ($mrb348$scheme_of_work_overrides$mrb348$, $mrb348$sow_overrides_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$scheme_of_work_overrides$mrb348$, $mrb348$sow_overrides_hod_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id))$mrb348$, null),
      ($mrb348$scheme_of_work_overrides$mrb348$, $mrb348$sow_overrides_member_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(school_id = ( SELECT auth_user_school_id() AS auth_user_school_id))$mrb348$, null),
      ($mrb348$school_period_times$mrb348$, $mrb348$school_period_times_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$),
      ($mrb348$school_period_times$mrb348$, $mrb348$school_period_times_school_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(school_id = ( SELECT auth_user_school_id() AS auth_user_school_id))$mrb348$, null),
      ($mrb348$school_subject_settings$mrb348$, $mrb348$sss_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$school_subject_settings$mrb348$, $mrb348$sss_hod_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id))$mrb348$, null),
      ($mrb348$school_subject_settings$mrb348$, $mrb348$sss_member_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(school_id = ( SELECT auth_user_school_id() AS auth_user_school_id))$mrb348$, null),
      ($mrb348$schools$mrb348$, $mrb348$schools_member_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(id = ( SELECT auth_user_school_id() AS auth_user_school_id))$mrb348$, null),
      ($mrb348$schools$mrb348$, $mrb348$schools_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$staff_scopes$mrb348$, $mrb348$staff_scopes_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$staff_scopes$mrb348$, $mrb348$staff_scopes_school_admin_write$mrb348$, $mrb348$ALL$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$),
      ($mrb348$staff_scopes$mrb348$, $mrb348$staff_scopes_school_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)))$mrb348$, null),
      ($mrb348$staff_scopes$mrb348$, $mrb348$staff_scopes_self_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(profile_id = ( SELECT auth.uid() AS uid))$mrb348$, null),
      ($mrb348$student_notifications$mrb348$, $mrb348$student_notifications_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$student_notifications$mrb348$, $mrb348$student_notifications_admin_send$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (sent_by = ( SELECT auth.uid() AS uid)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$),
      ($mrb348$student_notifications$mrb348$, $mrb348$student_notifications_student_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$(student_id = ( SELECT auth.uid() AS uid))$mrb348$, null),
      ($mrb348$student_notifications$mrb348$, $mrb348$student_notifications_teacher_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$auth_user_teaches_class(class_id)$mrb348$, null),
      ($mrb348$student_notifications$mrb348$, $mrb348$student_notifications_teacher_send$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$((sent_by = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(class_id))$mrb348$),
      ($mrb348$submission_feedback$mrb348$, $mrb348$submission_feedback_admin_insert$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (teacher_id = ( SELECT auth.uid() AS uid)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$),
      ($mrb348$submission_feedback$mrb348$, $mrb348$submission_feedback_admin_update$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (teacher_id = ( SELECT auth.uid() AS uid)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$, $mrb348$(( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (teacher_id = ( SELECT auth.uid() AS uid)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$),
      ($mrb348$submission_feedback$mrb348$, $mrb348$submission_feedback_insert$mrb348$, $mrb348$INSERT$mrb348$, null, $mrb348$((teacher_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(submission_class_id(submission_id)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id)))$mrb348$),
      ($mrb348$submission_feedback$mrb348$, $mrb348$submission_feedback_update$mrb348$, $mrb348$UPDATE$mrb348$, $mrb348$((teacher_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(submission_class_id(submission_id)))$mrb348$, $mrb348$((teacher_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(submission_class_id(submission_id)))$mrb348$),
      ($mrb348$subscriptions$mrb348$, $mrb348$subscriptions_operator_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$( SELECT auth_user_operator_active() AS auth_user_operator_active)$mrb348$, null),
      ($mrb348$subscriptions$mrb348$, $mrb348$subscriptions_org_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((org_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$timetable_entries$mrb348$, $mrb348$timetable_entries_admin_read$mrb348$, $mrb348$SELECT$mrb348$, $mrb348$((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope))$mrb348$, null),
      ($mrb348$timetable_entries$mrb348$, $mrb348$timetable_entries_own_all$mrb348$, $mrb348$ALL$mrb348$, $mrb348$(teacher_id = ( SELECT auth.uid() AS uid))$mrb348$, $mrb348$(teacher_id = ( SELECT auth.uid() AS uid))$mrb348$)
    ) as t(tablename, policyname, cmd, qual, with_check)
  loop
    select pg_policies.qual, pg_policies.with_check, pg_policies.cmd,
           pg_policies.permissive, pg_policies.roles::text as roles
      into live
    from pg_policies
    where schemaname = 'public'
      and tablename = expected.tablename
      and policyname = expected.policyname;

    if not found then
      raise exception 'MRB-348 aborted: policy %.% not found. This migration is pinned to the catalogue it was generated from -- regenerate it with tools/rls_consolidate.py against THIS database.', expected.tablename, expected.policyname;
    end if;
    if live.permissive <> 'PERMISSIVE' then
      raise exception 'MRB-348 aborted: %.% is RESTRICTIVE here but was PERMISSIVE when generated. Restrictive policies AND rather than OR and must never be merged.',
        expected.tablename, expected.policyname;
    end if;
    if live.roles <> '{public}' then
      raise exception 'MRB-348 aborted: %.% is granted to % here, not {public}.',
        expected.tablename, expected.policyname, live.roles;
    end if;
    if live.cmd is distinct from expected.cmd
       or live.qual is distinct from expected.qual
       or live.with_check is distinct from expected.with_check then
      raise exception 'MRB-348 aborted: %.% has drifted from the catalogue this migration was generated against. Regenerate rather than forcing.',
        expected.tablename, expected.policyname;
    end if;
    n := n + 1;
  end loop;
  if n <> 97 then
    raise exception 'MRB-348 aborted: guard matched % policies, expected %', n, 97;
  end if;
  raise notice 'MRB-348 guard: % policies verified byte-identical', n;
end $guard$;

-- --------------------------------------------------------------------------
-- THE MERGE, table by table.
-- --------------------------------------------------------------------------

-- ---- academic_years ----------------------------------------------------
--   2 policies -> 4
--     - academic_years_admin_write
--     - academic_years_member_read
drop policy "academic_years_admin_write" on public.academic_years;
drop policy "academic_years_member_read" on public.academic_years;

-- SELECT: academic_years_admin_write, academic_years_member_read
--   branch order (cost: policy)
--     3: academic_years_admin_write
--     3: academic_years_member_read
create policy "academic_years_select_merged" on public.academic_years
  as permissive for select to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR ((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)))
  )
;

-- INSERT: academic_years_admin_write
--   branch order (cost: policy)
--     3: academic_years_admin_write
create policy "academic_years_insert_merged" on public.academic_years
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- UPDATE: academic_years_admin_write
--   branch order (cost: policy)
--     3: academic_years_admin_write
create policy "academic_years_update_merged" on public.academic_years
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- DELETE: academic_years_admin_write
--   branch order (cost: policy)
--     3: academic_years_admin_write
create policy "academic_years_delete_merged" on public.academic_years
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- ---- assignment_question_attempts --------------------------------------
--   5 policies -> 4
--     - attempts_admin_read
--     - attempts_hod_read
--     - attempts_operator_read
--     - attempts_self_all
--     - attempts_teacher_read
drop policy "attempts_admin_read" on public.assignment_question_attempts;
drop policy "attempts_hod_read" on public.assignment_question_attempts;
drop policy "attempts_operator_read" on public.assignment_question_attempts;
drop policy "attempts_self_all" on public.assignment_question_attempts;
drop policy "attempts_teacher_read" on public.assignment_question_attempts;

-- SELECT: attempts_admin_read, attempts_hod_read, attempts_operator_read, attempts_self_all, attempts_teacher_read
--   branch order (cost: policy)
--     2: attempts_operator_read
--     5: attempts_admin_read
--     5: attempts_hod_read
--     5: attempts_self_all
--     5: attempts_teacher_read
create policy "assignment_question_attempts_select_merged" on public.assignment_question_attempts
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (EXISTS ( SELECT 1
   FROM (assignment_submissions s
     JOIN assignments a ON ((a.id = s.assignment_id)))
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))))
    OR ((EXISTS ( SELECT 1
   FROM (assignment_submissions s
     JOIN assignments a ON ((a.id = s.assignment_id)))
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(a.subject_id)))))
    OR ((EXISTS ( SELECT 1
   FROM assignment_submissions s
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (s.student_id = ( SELECT auth_user_id() AS auth_user_id))))))
    OR ((EXISTS ( SELECT 1
   FROM (assignment_submissions s
     JOIN assignments a ON ((a.id = s.assignment_id)))
  WHERE ((s.id = assignment_question_attempts.submission_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- INSERT: attempts_self_all
--   branch order (cost: policy)
--     5: attempts_self_all
create policy "assignment_question_attempts_insert_merged" on public.assignment_question_attempts
  as permissive for insert to public
  with check (
    ((EXISTS ( SELECT 1
   FROM assignment_submissions s
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (s.student_id = ( SELECT auth_user_id() AS auth_user_id))))))
  )
;

-- UPDATE: attempts_self_all
--   branch order (cost: policy)
--     5: attempts_self_all
create policy "assignment_question_attempts_update_merged" on public.assignment_question_attempts
  as permissive for update to public
  using (
    ((EXISTS ( SELECT 1
   FROM assignment_submissions s
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (s.student_id = ( SELECT auth_user_id() AS auth_user_id))))))
  )
  with check (
    ((EXISTS ( SELECT 1
   FROM assignment_submissions s
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (s.student_id = ( SELECT auth_user_id() AS auth_user_id))))))
  )
;

-- DELETE: attempts_self_all
--   branch order (cost: policy)
--     5: attempts_self_all
create policy "assignment_question_attempts_delete_merged" on public.assignment_question_attempts
  as permissive for delete to public
  using (
    ((EXISTS ( SELECT 1
   FROM assignment_submissions s
  WHERE ((s.id = assignment_question_attempts.submission_id) AND (s.student_id = ( SELECT auth_user_id() AS auth_user_id))))))
  )
;

-- ---- assignment_questions ----------------------------------------------
--   4 policies -> 4
--     - aq_admin_read
--     - aq_operator_read
--     - aq_student_read
--     - aq_teacher_all
drop policy "aq_admin_read" on public.assignment_questions;
drop policy "aq_operator_read" on public.assignment_questions;
drop policy "aq_student_read" on public.assignment_questions;
drop policy "aq_teacher_all" on public.assignment_questions;

-- SELECT: aq_admin_read, aq_operator_read, aq_student_read, aq_teacher_all
--   branch order (cost: policy)
--     2: aq_operator_read
--     5: aq_admin_read
--     5: aq_student_read
--     5: aq_teacher_all
create policy "assignment_questions_select_merged" on public.assignment_questions
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))))
    OR ((EXISTS ( SELECT 1
   FROM (assignments a
     JOIN class_members cm ON (((cm.class_id = a.class_id) AND (cm.left_at IS NULL) AND (cm.deleted_at IS NULL))))
  WHERE ((a.id = assignment_questions.assignment_id) AND (cm.student_id = ( SELECT auth_user_id() AS auth_user_id)) AND ((a.release_at IS NULL) OR (a.release_at <= now())) AND (a.deleted_at IS NULL)))))
    OR ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- INSERT: aq_teacher_all
--   branch order (cost: policy)
--     5: aq_teacher_all
create policy "assignment_questions_insert_merged" on public.assignment_questions
  as permissive for insert to public
  with check (
    ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- UPDATE: aq_teacher_all
--   branch order (cost: policy)
--     5: aq_teacher_all
create policy "assignment_questions_update_merged" on public.assignment_questions
  as permissive for update to public
  using (
    ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
  with check (
    ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- DELETE: aq_teacher_all
--   branch order (cost: policy)
--     5: aq_teacher_all
create policy "assignment_questions_delete_merged" on public.assignment_questions
  as permissive for delete to public
  using (
    ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_questions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- ---- assignment_submissions --------------------------------------------
--   7 policies -> 4
--     - submissions_admin_read
--     - submissions_admin_write
--     - submissions_hod_read
--     - submissions_operator_read
--     - submissions_self_all
--     - submissions_teacher_read
--     - submissions_teacher_update
drop policy "submissions_admin_read" on public.assignment_submissions;
drop policy "submissions_admin_write" on public.assignment_submissions;
drop policy "submissions_hod_read" on public.assignment_submissions;
drop policy "submissions_operator_read" on public.assignment_submissions;
drop policy "submissions_self_all" on public.assignment_submissions;
drop policy "submissions_teacher_read" on public.assignment_submissions;
drop policy "submissions_teacher_update" on public.assignment_submissions;

-- SELECT: submissions_admin_read, submissions_hod_read, submissions_operator_read, submissions_self_all, submissions_teacher_read
--   branch order (cost: policy)
--     1: submissions_self_all
--     2: submissions_operator_read
--     5: submissions_admin_read
--     5: submissions_hod_read
--     5: submissions_teacher_read
create policy "assignment_submissions_select_merged" on public.assignment_submissions
  as permissive for select to public
  using (
    ((student_id = ( SELECT auth_user_id() AS auth_user_id)))
    OR (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))))
    OR ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(a.subject_id)))))
    OR ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- INSERT: submissions_self_all
--   branch order (cost: policy)
--     1: submissions_self_all
create policy "assignment_submissions_insert_merged" on public.assignment_submissions
  as permissive for insert to public
  with check (
    ((student_id = ( SELECT auth_user_id() AS auth_user_id)))
  )
;

-- UPDATE: submissions_admin_write, submissions_self_all, submissions_teacher_update
--   branch order (cost: policy)
--     1: submissions_self_all
--     5: submissions_admin_write
--     5: submissions_teacher_update
create policy "assignment_submissions_update_merged" on public.assignment_submissions
  as permissive for update to public
  using (
    ((student_id = ( SELECT auth_user_id() AS auth_user_id)))
    OR ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))))
    OR ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
  with check (
    ((student_id = ( SELECT auth_user_id() AS auth_user_id)))
    OR ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))))
    OR ((EXISTS ( SELECT 1
   FROM assignments a
  WHERE ((a.id = assignment_submissions.assignment_id) AND auth_user_teaches_class(a.class_id) AND (class_school_id(a.class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))))
  )
;

-- DELETE: submissions_self_all
--   branch order (cost: policy)
--     1: submissions_self_all
create policy "assignment_submissions_delete_merged" on public.assignment_submissions
  as permissive for delete to public
  using (
    ((student_id = ( SELECT auth_user_id() AS auth_user_id)))
  )
;

-- ---- assignments -------------------------------------------------------
--   7 policies -> 4
--     - assignments_admin_read
--     - assignments_admin_write
--     - assignments_hod_read
--     - assignments_operator_read
--     - assignments_student_read
--     - assignments_teacher_read
--     - assignments_teacher_write
drop policy "assignments_admin_read" on public.assignments;
drop policy "assignments_admin_write" on public.assignments;
drop policy "assignments_hod_read" on public.assignments;
drop policy "assignments_operator_read" on public.assignments;
drop policy "assignments_student_read" on public.assignments;
drop policy "assignments_teacher_read" on public.assignments;
drop policy "assignments_teacher_write" on public.assignments;

-- SELECT: assignments_admin_read, assignments_admin_write, assignments_hod_read, assignments_operator_read, assignments_student_read, assignments_teacher_read, assignments_teacher_write
--   branch order (cost: policy)
--     2: assignments_operator_read
--     4: assignments_admin_read
--     4: assignments_admin_write
--     4: assignments_hod_read
--     4: assignments_student_read
--     4: assignments_teacher_read
--     4: assignments_teacher_write
create policy "assignments_select_merged" on public.assignments
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope))))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_member_of_class(class_id) AND ((release_at IS NULL) OR (release_at <= now())) AND (deleted_at IS NULL)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id)))
  )
;

-- INSERT: assignments_admin_write, assignments_teacher_write
--   branch order (cost: policy)
--     4: assignments_admin_write
--     4: assignments_teacher_write
create policy "assignments_insert_merged" on public.assignments
  as permissive for insert to public
  with check (
    (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id)))
  )
;

-- UPDATE: assignments_admin_write, assignments_teacher_write
--   branch order (cost: policy)
--     4: assignments_admin_write
--     4: assignments_teacher_write
create policy "assignments_update_merged" on public.assignments
  as permissive for update to public
  using (
    (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id)))
  )
  with check (
    (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id)))
  )
;

-- DELETE: assignments_admin_write, assignments_teacher_write
--   branch order (cost: policy)
--     4: assignments_admin_write
--     4: assignments_teacher_write
create policy "assignments_delete_merged" on public.assignments
  as permissive for delete to public
  using (
    (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(class_id)))
  )
;

-- ---- audit_log ---------------------------------------------------------
--   3 policies -> 1
--     - audit_admin_read
--     - audit_hod_read
--     - audit_operator_read
drop policy "audit_admin_read" on public.audit_log;
drop policy "audit_hod_read" on public.audit_log;
drop policy "audit_operator_read" on public.audit_log;

-- SELECT: audit_admin_read, audit_hod_read, audit_operator_read
--   branch order (cost: policy)
--     2: audit_operator_read
--     3: audit_admin_read
--     3: audit_hod_read
create policy "audit_log_select_merged" on public.audit_log
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope))))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
  )
;

-- ---- class_members -----------------------------------------------------
--   7 policies -> 2
--     - class_members_admin_read
--     - class_members_hod_read
--     - class_members_operator_read
--     - class_members_self_insert
--     - class_members_self_read
--     - class_members_staff_insert
--     - class_members_teacher_read
drop policy "class_members_admin_read" on public.class_members;
drop policy "class_members_hod_read" on public.class_members;
drop policy "class_members_operator_read" on public.class_members;
drop policy "class_members_self_insert" on public.class_members;
drop policy "class_members_self_read" on public.class_members;
drop policy "class_members_staff_insert" on public.class_members;
drop policy "class_members_teacher_read" on public.class_members;

-- SELECT: class_members_admin_read, class_members_hod_read, class_members_operator_read, class_members_self_read, class_members_teacher_read
--   branch order (cost: policy)
--     1: class_members_self_read
--     2: class_members_operator_read
--     4: class_members_admin_read
--     4: class_members_hod_read
--     4: class_members_teacher_read
create policy "class_members_select_merged" on public.class_members
  as permissive for select to public
  using (
    ((student_id = ( SELECT auth_user_id() AS auth_user_id)))
    OR (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((auth_user_teaches_class(class_id) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
  )
;

-- INSERT: class_members_self_insert, class_members_staff_insert
--   branch order (cost: policy)
--     4: class_members_self_insert
--     4: class_members_staff_insert
create policy "class_members_insert_merged" on public.class_members
  as permissive for insert to public
  with check (
    (((student_id = ( SELECT auth_user_id() AS auth_user_id)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR auth_user_teaches_class(class_id))))
  )
;

-- ---- class_shoutouts ---------------------------------------------------
--   6 policies -> 3
--     - class_shoutouts_admin_insert
--     - class_shoutouts_admin_read
--     - class_shoutouts_admin_update
--     - class_shoutouts_insert
--     - class_shoutouts_select
--     - class_shoutouts_update
drop policy "class_shoutouts_admin_insert" on public.class_shoutouts;
drop policy "class_shoutouts_admin_read" on public.class_shoutouts;
drop policy "class_shoutouts_admin_update" on public.class_shoutouts;
drop policy "class_shoutouts_insert" on public.class_shoutouts;
drop policy "class_shoutouts_select" on public.class_shoutouts;
drop policy "class_shoutouts_update" on public.class_shoutouts;

-- SELECT: class_shoutouts_admin_read, class_shoutouts_select
--   branch order (cost: policy)
--     4: class_shoutouts_admin_read
--     4: class_shoutouts_select
create policy "class_shoutouts_select_merged" on public.class_shoutouts
  as permissive for select to public
  using (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((((deleted_at IS NULL) AND (auth_user_teaches_class(class_id) OR auth_user_is_member_of_class(class_id) OR (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))) OR ((deleted_at IS NOT NULL) AND ((author_id = ( SELECT auth.uid() AS uid)) OR (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)))))))
  )
;

-- INSERT: class_shoutouts_admin_insert, class_shoutouts_insert
--   branch order (cost: policy)
--     4: class_shoutouts_admin_insert
--     4: class_shoutouts_insert
create policy "class_shoutouts_insert_merged" on public.class_shoutouts
  as permissive for insert to public
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid)) AND (recipient_id IN ( SELECT cm.student_id
   FROM class_members cm
  WHERE ((cm.class_id = class_shoutouts.class_id) AND (cm.left_at IS NULL) AND (cm.deleted_at IS NULL))))))
    OR ((auth_user_teaches_class(class_id) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid)) AND (recipient_id IN ( SELECT cm.student_id
   FROM class_members cm
  WHERE ((cm.class_id = class_shoutouts.class_id) AND (cm.left_at IS NULL) AND (cm.deleted_at IS NULL))))))
  )
;

-- UPDATE: class_shoutouts_admin_update, class_shoutouts_update
--   branch order (cost: policy)
--     4: class_shoutouts_admin_update
--     4: class_shoutouts_update
create policy "class_shoutouts_update_merged" on public.class_shoutouts
  as permissive for update to public
  using (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid))))
    OR (((author_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(class_id)))
  )
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (author_id = ( SELECT auth.uid() AS uid))))
    OR (((author_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(class_id)))
  )
;

-- ---- class_teachers ----------------------------------------------------
--   6 policies -> 4
--     - class_teachers_admin_read
--     - class_teachers_admin_write
--     - class_teachers_hod_read
--     - class_teachers_hod_write
--     - class_teachers_operator_read
--     - class_teachers_self_read
drop policy "class_teachers_admin_read" on public.class_teachers;
drop policy "class_teachers_admin_write" on public.class_teachers;
drop policy "class_teachers_hod_read" on public.class_teachers;
drop policy "class_teachers_hod_write" on public.class_teachers;
drop policy "class_teachers_operator_read" on public.class_teachers;
drop policy "class_teachers_self_read" on public.class_teachers;

-- SELECT: class_teachers_admin_read, class_teachers_admin_write, class_teachers_hod_read, class_teachers_hod_write, class_teachers_operator_read, class_teachers_self_read
--   branch order (cost: policy)
--     1: class_teachers_self_read
--     2: class_teachers_operator_read
--     4: class_teachers_admin_read
--     4: class_teachers_admin_write
--     4: class_teachers_hod_read
--     4: class_teachers_hod_write
create policy "class_teachers_select_merged" on public.class_teachers
  as permissive for select to public
  using (
    ((teacher_id = ( SELECT auth_user_id() AS auth_user_id)))
    OR (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((subject_id IS NULL) OR auth_user_is_hod_of_subject_dept(subject_id))))
  )
;

-- INSERT: class_teachers_admin_write, class_teachers_hod_write
--   branch order (cost: policy)
--     4: class_teachers_admin_write
--     4: class_teachers_hod_write
create policy "class_teachers_insert_merged" on public.class_teachers
  as permissive for insert to public
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((subject_id IS NULL) OR auth_user_is_hod_of_subject_dept(subject_id))))
  )
;

-- UPDATE: class_teachers_admin_write, class_teachers_hod_write
--   branch order (cost: policy)
--     4: class_teachers_admin_write
--     4: class_teachers_hod_write
create policy "class_teachers_update_merged" on public.class_teachers
  as permissive for update to public
  using (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((subject_id IS NULL) OR auth_user_is_hod_of_subject_dept(subject_id))))
  )
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((subject_id IS NULL) OR auth_user_is_hod_of_subject_dept(subject_id))))
  )
;

-- DELETE: class_teachers_admin_write, class_teachers_hod_write
--   branch order (cost: policy)
--     4: class_teachers_admin_write
--     4: class_teachers_hod_write
create policy "class_teachers_delete_merged" on public.class_teachers
  as permissive for delete to public
  using (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR ((( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((subject_id IS NULL) OR auth_user_is_hod_of_subject_dept(subject_id))))
  )
;

-- ---- classes -----------------------------------------------------------
--   8 policies -> 4
--     - classes_admin_read
--     - classes_admin_write
--     - classes_hod_read
--     - classes_hod_write
--     - classes_operator_read
--     - classes_student_read
--     - classes_teacher_read
--     - classes_teacher_update
drop policy "classes_admin_read" on public.classes;
drop policy "classes_admin_write" on public.classes;
drop policy "classes_hod_read" on public.classes;
drop policy "classes_hod_write" on public.classes;
drop policy "classes_operator_read" on public.classes;
drop policy "classes_student_read" on public.classes;
drop policy "classes_teacher_read" on public.classes;
drop policy "classes_teacher_update" on public.classes;

-- SELECT: classes_admin_read, classes_admin_write, classes_hod_read, classes_hod_write, classes_operator_read, classes_student_read, classes_teacher_read
--   branch order (cost: policy)
--     2: classes_operator_read
--     3: classes_admin_read
--     3: classes_admin_write
--     3: classes_hod_read
--     3: classes_hod_write
--     4: classes_student_read
--     4: classes_teacher_read
create policy "classes_select_merged" on public.classes
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope))))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_member_of_class(id)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(id)))
  )
;

-- INSERT: classes_admin_write, classes_hod_write
--   branch order (cost: policy)
--     3: classes_admin_write
--     3: classes_hod_write
create policy "classes_insert_merged" on public.classes
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
  )
;

-- UPDATE: classes_admin_write, classes_hod_write, classes_teacher_update
--   branch order (cost: policy)
--     3: classes_admin_write
--     3: classes_hod_write
--     4: classes_teacher_update
create policy "classes_update_merged" on public.classes
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(id)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_teaches_class(id)))
  )
;

-- DELETE: classes_admin_write, classes_hod_write
--   branch order (cost: policy)
--     3: classes_admin_write
--     3: classes_hod_write
create policy "classes_delete_merged" on public.classes
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope)))
  )
;

-- ---- family_messages ---------------------------------------------------
--   2 policies -> 1
--     - family_messages_operator_read
--     - family_messages_party_read
drop policy "family_messages_operator_read" on public.family_messages;
drop policy "family_messages_party_read" on public.family_messages;

-- SELECT: family_messages_operator_read, family_messages_party_read
--   branch order (cost: policy)
--     2: family_messages_operator_read
--     3: family_messages_party_read
create policy "family_messages_select_merged" on public.family_messages
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((deleted_at IS NULL) AND (org_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ((sender_id = ( SELECT auth.uid() AS uid)) OR (recipient_id = ( SELECT auth.uid() AS uid)))))
  )
;

-- ---- pending_staff -----------------------------------------------------
--   2 policies -> 4
--     - pending_staff_admin_all
--     - pending_staff_operator_read
drop policy "pending_staff_admin_all" on public.pending_staff;
drop policy "pending_staff_operator_read" on public.pending_staff;

-- SELECT: pending_staff_admin_all, pending_staff_operator_read
--   branch order (cost: policy)
--     2: pending_staff_operator_read
--     3: pending_staff_admin_all
create policy "pending_staff_select_merged" on public.pending_staff
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- INSERT: pending_staff_admin_all
--   branch order (cost: policy)
--     3: pending_staff_admin_all
create policy "pending_staff_insert_merged" on public.pending_staff
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- UPDATE: pending_staff_admin_all
--   branch order (cost: policy)
--     3: pending_staff_admin_all
create policy "pending_staff_update_merged" on public.pending_staff
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- DELETE: pending_staff_admin_all
--   branch order (cost: policy)
--     3: pending_staff_admin_all
create policy "pending_staff_delete_merged" on public.pending_staff
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- ---- platform_flags ----------------------------------------------------
--   2 policies -> 4
--     - platform_flags_operator_write
--     - platform_flags_read
drop policy "platform_flags_operator_write" on public.platform_flags;
drop policy "platform_flags_read" on public.platform_flags;

-- SELECT: platform_flags_operator_write, platform_flags_read
--   branch order (cost: policy)
--     0: platform_flags_read
--     2: platform_flags_operator_write
create policy "platform_flags_select_merged" on public.platform_flags
  as permissive for select to public
  using (
    (true)
    OR (( SELECT auth_user_operator_active() AS auth_user_operator_active))
  )
;

-- INSERT: platform_flags_operator_write
--   branch order (cost: policy)
--     2: platform_flags_operator_write
create policy "platform_flags_insert_merged" on public.platform_flags
  as permissive for insert to public
  with check (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
  )
;

-- UPDATE: platform_flags_operator_write
--   branch order (cost: policy)
--     2: platform_flags_operator_write
create policy "platform_flags_update_merged" on public.platform_flags
  as permissive for update to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
  )
  with check (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
  )
;

-- DELETE: platform_flags_operator_write
--   branch order (cost: policy)
--     2: platform_flags_operator_write
create policy "platform_flags_delete_merged" on public.platform_flags
  as permissive for delete to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
  )
;

-- ---- platform_operator_activations -------------------------------------
--   2 policies -> 4
--     - operator_activations_operator_read
--     - operator_activations_operator_write
drop policy "operator_activations_operator_read" on public.platform_operator_activations;
drop policy "operator_activations_operator_write" on public.platform_operator_activations;

-- SELECT: operator_activations_operator_read, operator_activations_operator_write
--   branch order (cost: policy)
--     2: operator_activations_operator_read
--     2: operator_activations_operator_write
create policy "platform_operator_activations_select_merged" on public.platform_operator_activations
  as permissive for select to public
  using (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
    OR (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- INSERT: operator_activations_operator_write
--   branch order (cost: policy)
--     2: operator_activations_operator_write
create policy "platform_operator_activations_insert_merged" on public.platform_operator_activations
  as permissive for insert to public
  with check (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- UPDATE: operator_activations_operator_write
--   branch order (cost: policy)
--     2: operator_activations_operator_write
create policy "platform_operator_activations_update_merged" on public.platform_operator_activations
  as permissive for update to public
  using (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
  with check (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- DELETE: operator_activations_operator_write
--   branch order (cost: policy)
--     2: operator_activations_operator_write
create policy "platform_operator_activations_delete_merged" on public.platform_operator_activations
  as permissive for delete to public
  using (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- ---- platform_operators ------------------------------------------------
--   2 policies -> 4
--     - platform_operators_operator_read
--     - platform_operators_operator_write
drop policy "platform_operators_operator_read" on public.platform_operators;
drop policy "platform_operators_operator_write" on public.platform_operators;

-- SELECT: platform_operators_operator_read, platform_operators_operator_write
--   branch order (cost: policy)
--     2: platform_operators_operator_read
--     2: platform_operators_operator_write
create policy "platform_operators_select_merged" on public.platform_operators
  as permissive for select to public
  using (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
    OR (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- INSERT: platform_operators_operator_write
--   branch order (cost: policy)
--     2: platform_operators_operator_write
create policy "platform_operators_insert_merged" on public.platform_operators
  as permissive for insert to public
  with check (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- UPDATE: platform_operators_operator_write
--   branch order (cost: policy)
--     2: platform_operators_operator_write
create policy "platform_operators_update_merged" on public.platform_operators
  as permissive for update to public
  using (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
  with check (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- DELETE: platform_operators_operator_write
--   branch order (cost: policy)
--     2: platform_operators_operator_write
create policy "platform_operators_delete_merged" on public.platform_operators
  as permissive for delete to public
  using (
    (( SELECT auth_user_is_platform_operator() AS auth_user_is_platform_operator))
  )
;

-- ---- profiles ----------------------------------------------------------
--   5 policies -> 1
--     - Users can view own profile
--     - profiles_admin_read_school
--     - profiles_hod_read_dept
--     - profiles_operator_read
--     - profiles_teacher_read_students
drop policy "Users can view own profile" on public.profiles;
drop policy "profiles_admin_read_school" on public.profiles;
drop policy "profiles_hod_read_dept" on public.profiles;
drop policy "profiles_operator_read" on public.profiles;
drop policy "profiles_teacher_read_students" on public.profiles;

-- SELECT: Users can view own profile, profiles_admin_read_school, profiles_hod_read_dept, profiles_operator_read, profiles_teacher_read_students
--   branch order (cost: policy)
--     1: Users can view own profile
--     2: profiles_operator_read
--     3: profiles_admin_read_school
--     4: profiles_hod_read_dept
--     5: profiles_teacher_read_students
create policy "profiles_select_merged" on public.profiles
  as permissive for select to public
  using (
    ((( SELECT auth.uid() AS uid) = id))
    OR (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope))))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('hod'::text) AS auth_user_has_scope) AND (((department IS NOT NULL) AND auth_user_is_hod_of_dept(department)) OR (role = 'student'::text))))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (role = 'student'::text) AND (EXISTS ( SELECT 1
   FROM class_members cm
  WHERE ((cm.student_id = profiles.id) AND auth_user_teaches_class(cm.class_id) AND (cm.left_at IS NULL))))))
  )
;

-- ---- scheme_of_work_overrides ------------------------------------------
--   3 policies -> 4
--     - sow_overrides_admin_write
--     - sow_overrides_hod_write
--     - sow_overrides_member_read
drop policy "sow_overrides_admin_write" on public.scheme_of_work_overrides;
drop policy "sow_overrides_hod_write" on public.scheme_of_work_overrides;
drop policy "sow_overrides_member_read" on public.scheme_of_work_overrides;

-- SELECT: sow_overrides_admin_write, sow_overrides_hod_write, sow_overrides_member_read
--   branch order (cost: policy)
--     3: sow_overrides_admin_write
--     3: sow_overrides_member_read
--     4: sow_overrides_hod_write
create policy "scheme_of_work_overrides_select_merged" on public.scheme_of_work_overrides
  as permissive for select to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR ((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- INSERT: sow_overrides_admin_write, sow_overrides_hod_write
--   branch order (cost: policy)
--     3: sow_overrides_admin_write
--     4: sow_overrides_hod_write
create policy "scheme_of_work_overrides_insert_merged" on public.scheme_of_work_overrides
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- UPDATE: sow_overrides_admin_write, sow_overrides_hod_write
--   branch order (cost: policy)
--     3: sow_overrides_admin_write
--     4: sow_overrides_hod_write
create policy "scheme_of_work_overrides_update_merged" on public.scheme_of_work_overrides
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- DELETE: sow_overrides_admin_write, sow_overrides_hod_write
--   branch order (cost: policy)
--     3: sow_overrides_admin_write
--     4: sow_overrides_hod_write
create policy "scheme_of_work_overrides_delete_merged" on public.scheme_of_work_overrides
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- ---- school_period_times -----------------------------------------------
--   2 policies -> 4
--     - school_period_times_admin_write
--     - school_period_times_school_read
drop policy "school_period_times_admin_write" on public.school_period_times;
drop policy "school_period_times_school_read" on public.school_period_times;

-- SELECT: school_period_times_admin_write, school_period_times_school_read
--   branch order (cost: policy)
--     3: school_period_times_admin_write
--     3: school_period_times_school_read
create policy "school_period_times_select_merged" on public.school_period_times
  as permissive for select to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR ((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)))
  )
;

-- INSERT: school_period_times_admin_write
--   branch order (cost: policy)
--     3: school_period_times_admin_write
create policy "school_period_times_insert_merged" on public.school_period_times
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- UPDATE: school_period_times_admin_write
--   branch order (cost: policy)
--     3: school_period_times_admin_write
create policy "school_period_times_update_merged" on public.school_period_times
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- DELETE: school_period_times_admin_write
--   branch order (cost: policy)
--     3: school_period_times_admin_write
create policy "school_period_times_delete_merged" on public.school_period_times
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- ---- school_subject_settings -------------------------------------------
--   3 policies -> 4
--     - sss_admin_write
--     - sss_hod_write
--     - sss_member_read
drop policy "sss_admin_write" on public.school_subject_settings;
drop policy "sss_hod_write" on public.school_subject_settings;
drop policy "sss_member_read" on public.school_subject_settings;

-- SELECT: sss_admin_write, sss_hod_write, sss_member_read
--   branch order (cost: policy)
--     3: sss_admin_write
--     3: sss_member_read
--     4: sss_hod_write
create policy "school_subject_settings_select_merged" on public.school_subject_settings
  as permissive for select to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR ((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- INSERT: sss_admin_write, sss_hod_write
--   branch order (cost: policy)
--     3: sss_admin_write
--     4: sss_hod_write
create policy "school_subject_settings_insert_merged" on public.school_subject_settings
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- UPDATE: sss_admin_write, sss_hod_write
--   branch order (cost: policy)
--     3: sss_admin_write
--     4: sss_hod_write
create policy "school_subject_settings_update_merged" on public.school_subject_settings
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- DELETE: sss_admin_write, sss_hod_write
--   branch order (cost: policy)
--     3: sss_admin_write
--     4: sss_hod_write
create policy "school_subject_settings_delete_merged" on public.school_subject_settings
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND auth_user_is_hod_of_subject_dept(subject_id)))
  )
;

-- ---- schools -----------------------------------------------------------
--   2 policies -> 1
--     - schools_member_read
--     - schools_operator_read
drop policy "schools_member_read" on public.schools;
drop policy "schools_operator_read" on public.schools;

-- SELECT: schools_member_read, schools_operator_read
--   branch order (cost: policy)
--     2: schools_operator_read
--     3: schools_member_read
create policy "schools_select_merged" on public.schools
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR ((id = ( SELECT auth_user_school_id() AS auth_user_school_id)))
  )
;

-- ---- staff_scopes ------------------------------------------------------
--   4 policies -> 4
--     - staff_scopes_operator_read
--     - staff_scopes_school_admin_write
--     - staff_scopes_school_read
--     - staff_scopes_self_read
drop policy "staff_scopes_operator_read" on public.staff_scopes;
drop policy "staff_scopes_school_admin_write" on public.staff_scopes;
drop policy "staff_scopes_school_read" on public.staff_scopes;
drop policy "staff_scopes_self_read" on public.staff_scopes;

-- SELECT: staff_scopes_operator_read, staff_scopes_school_admin_write, staff_scopes_school_read, staff_scopes_self_read
--   branch order (cost: policy)
--     1: staff_scopes_self_read
--     2: staff_scopes_operator_read
--     3: staff_scopes_school_admin_write
--     3: staff_scopes_school_read
create policy "staff_scopes_select_merged" on public.staff_scopes
  as permissive for select to public
  using (
    ((profile_id = ( SELECT auth.uid() AS uid)))
    OR (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND (( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) OR ( SELECT auth_user_has_scope('slt'::text) AS auth_user_has_scope))))
  )
;

-- INSERT: staff_scopes_school_admin_write
--   branch order (cost: policy)
--     3: staff_scopes_school_admin_write
create policy "staff_scopes_insert_merged" on public.staff_scopes
  as permissive for insert to public
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- UPDATE: staff_scopes_school_admin_write
--   branch order (cost: policy)
--     3: staff_scopes_school_admin_write
create policy "staff_scopes_update_merged" on public.staff_scopes
  as permissive for update to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
  with check (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- DELETE: staff_scopes_school_admin_write
--   branch order (cost: policy)
--     3: staff_scopes_school_admin_write
create policy "staff_scopes_delete_merged" on public.staff_scopes
  as permissive for delete to public
  using (
    (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- ---- student_notifications ---------------------------------------------
--   5 policies -> 2
--     - student_notifications_admin_read
--     - student_notifications_admin_send
--     - student_notifications_student_read
--     - student_notifications_teacher_read
--     - student_notifications_teacher_send
drop policy "student_notifications_admin_read" on public.student_notifications;
drop policy "student_notifications_admin_send" on public.student_notifications;
drop policy "student_notifications_student_read" on public.student_notifications;
drop policy "student_notifications_teacher_read" on public.student_notifications;
drop policy "student_notifications_teacher_send" on public.student_notifications;

-- SELECT: student_notifications_admin_read, student_notifications_student_read, student_notifications_teacher_read
--   branch order (cost: policy)
--     1: student_notifications_student_read
--     4: student_notifications_admin_read
--     4: student_notifications_teacher_read
create policy "student_notifications_select_merged" on public.student_notifications
  as permissive for select to public
  using (
    ((student_id = ( SELECT auth.uid() AS uid)))
    OR (((class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
    OR (auth_user_teaches_class(class_id))
  )
;

-- INSERT: student_notifications_admin_send, student_notifications_teacher_send
--   branch order (cost: policy)
--     4: student_notifications_admin_send
--     4: student_notifications_teacher_send
create policy "student_notifications_insert_merged" on public.student_notifications
  as permissive for insert to public
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (sent_by = ( SELECT auth.uid() AS uid)) AND (class_school_id(class_id) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR (((sent_by = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(class_id)))
  )
;

-- ---- submission_feedback -----------------------------------------------
--   4 policies -> 2
--     - submission_feedback_admin_insert
--     - submission_feedback_admin_update
--     - submission_feedback_insert
--     - submission_feedback_update
drop policy "submission_feedback_admin_insert" on public.submission_feedback;
drop policy "submission_feedback_admin_update" on public.submission_feedback;
drop policy "submission_feedback_insert" on public.submission_feedback;
drop policy "submission_feedback_update" on public.submission_feedback;

-- INSERT: submission_feedback_admin_insert, submission_feedback_insert
--   branch order (cost: policy)
--     4: submission_feedback_admin_insert
--     4: submission_feedback_insert
create policy "submission_feedback_insert_merged" on public.submission_feedback
  as permissive for insert to public
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (teacher_id = ( SELECT auth.uid() AS uid)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR (((teacher_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(submission_class_id(submission_id)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
  )
;

-- UPDATE: submission_feedback_admin_update, submission_feedback_update
--   branch order (cost: policy)
--     4: submission_feedback_admin_update
--     4: submission_feedback_update
create policy "submission_feedback_update_merged" on public.submission_feedback
  as permissive for update to public
  using (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (teacher_id = ( SELECT auth.uid() AS uid)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR (((teacher_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(submission_class_id(submission_id))))
  )
  with check (
    ((( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope) AND (teacher_id = ( SELECT auth.uid() AS uid)) AND (class_school_id(submission_class_id(submission_id)) = ( SELECT auth_user_school_id() AS auth_user_school_id))))
    OR (((teacher_id = ( SELECT auth.uid() AS uid)) AND auth_user_teaches_class(submission_class_id(submission_id))))
  )
;

-- ---- subscriptions -----------------------------------------------------
--   2 policies -> 1
--     - subscriptions_operator_read
--     - subscriptions_org_admin_read
drop policy "subscriptions_operator_read" on public.subscriptions;
drop policy "subscriptions_org_admin_read" on public.subscriptions;

-- SELECT: subscriptions_operator_read, subscriptions_org_admin_read
--   branch order (cost: policy)
--     2: subscriptions_operator_read
--     3: subscriptions_org_admin_read
create policy "subscriptions_select_merged" on public.subscriptions
  as permissive for select to public
  using (
    (( SELECT auth_user_operator_active() AS auth_user_operator_active))
    OR (((org_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- ---- timetable_entries -------------------------------------------------
--   2 policies -> 4
--     - timetable_entries_admin_read
--     - timetable_entries_own_all
drop policy "timetable_entries_admin_read" on public.timetable_entries;
drop policy "timetable_entries_own_all" on public.timetable_entries;

-- SELECT: timetable_entries_admin_read, timetable_entries_own_all
--   branch order (cost: policy)
--     1: timetable_entries_own_all
--     3: timetable_entries_admin_read
create policy "timetable_entries_select_merged" on public.timetable_entries
  as permissive for select to public
  using (
    ((teacher_id = ( SELECT auth.uid() AS uid)))
    OR (((school_id = ( SELECT auth_user_school_id() AS auth_user_school_id)) AND ( SELECT auth_user_has_scope('school_admin'::text) AS auth_user_has_scope)))
  )
;

-- INSERT: timetable_entries_own_all
--   branch order (cost: policy)
--     1: timetable_entries_own_all
create policy "timetable_entries_insert_merged" on public.timetable_entries
  as permissive for insert to public
  with check (
    ((teacher_id = ( SELECT auth.uid() AS uid)))
  )
;

-- UPDATE: timetable_entries_own_all
--   branch order (cost: policy)
--     1: timetable_entries_own_all
create policy "timetable_entries_update_merged" on public.timetable_entries
  as permissive for update to public
  using (
    ((teacher_id = ( SELECT auth.uid() AS uid)))
  )
  with check (
    ((teacher_id = ( SELECT auth.uid() AS uid)))
  )
;

-- DELETE: timetable_entries_own_all
--   branch order (cost: policy)
--     1: timetable_entries_own_all
create policy "timetable_entries_delete_merged" on public.timetable_entries
  as permissive for delete to public
  using (
    ((teacher_id = ( SELECT auth.uid() AS uid)))
  )
;

-- --------------------------------------------------------------------------
-- POST-CONDITIONS
-- --------------------------------------------------------------------------
do $post$
declare n_restrictive int; n_multi int;
begin
  select count(*) into n_restrictive
  from pg_policies where schemaname='public' and permissive <> 'PERMISSIVE';
  if n_restrictive > 0 then
    raise exception 'MRB-348 aborted: % restrictive policies present after merge; this migration must never create one', n_restrictive;
  end if;

  -- every table this migration touched must now hold exactly one PUBLIC
  -- permissive policy per command it covers
  select count(*) into n_multi from (
    select tablename, cmd from pg_policies
    where schemaname='public' and roles::text='{public}'
      and tablename in ($mrb348$academic_years$mrb348$, $mrb348$assignment_question_attempts$mrb348$, $mrb348$assignment_questions$mrb348$, $mrb348$assignment_submissions$mrb348$, $mrb348$assignments$mrb348$, $mrb348$audit_log$mrb348$, $mrb348$class_members$mrb348$, $mrb348$class_shoutouts$mrb348$, $mrb348$class_teachers$mrb348$, $mrb348$classes$mrb348$, $mrb348$family_messages$mrb348$, $mrb348$pending_staff$mrb348$, $mrb348$platform_flags$mrb348$, $mrb348$platform_operator_activations$mrb348$, $mrb348$platform_operators$mrb348$, $mrb348$profiles$mrb348$, $mrb348$scheme_of_work_overrides$mrb348$, $mrb348$school_period_times$mrb348$, $mrb348$school_subject_settings$mrb348$, $mrb348$schools$mrb348$, $mrb348$staff_scopes$mrb348$, $mrb348$student_notifications$mrb348$, $mrb348$submission_feedback$mrb348$, $mrb348$subscriptions$mrb348$, $mrb348$timetable_entries$mrb348$)
    group by tablename, cmd having count(*) > 1
  ) d;
  if n_multi > 0 then
    raise exception 'MRB-348: % (table,cmd) cells still hold multiple public policies', n_multi;
  end if;
  raise notice 'MRB-348: merge complete, 0 restrictive, 0 multi-permissive public cells';
end $post$;

commit;

-- ==========================================================================
-- LEFT ALONE, AND WHY
-- ==========================================================================
--   account_deletion_requests.account_deletion_requests_read_own_org
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   ks3_assignment_bank.ks3_assignment_bank_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   ks3_cards.ks3_cards_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   ks3_ladder_questions.ks3_ladder_questions_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   ks4_assignment_bank.ks4_assignment_bank_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   revision_materials.revision_materials_public_read
--       granted to {anon,authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   rum_timings.rum_timings_insert_self
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   rum_timings.rum_timings_read_admin
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   scheme_of_work_entries.sow_entries_authenticated_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   school_invitations.invitations_invitee_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
--   subjects.subjects_authenticated_read
--       granted to {authenticated}, not {public}; merging across differing GRANT sets would change who the policy reaches
