-- MRB-306 — Mide's rulings 2 and 3, 3 Sep 2026. Two RLS widenings.
--
-- ⚠️ FILENAME VERSION MUST MATCH. Applied to prod via MCP `apply_migration`,
-- which records its own `schema_migrations` version — 20260903200007. A
-- mismatch makes `db push` re-apply it.
--
-- Ruling 3: `slt` reads written feedback. Mide: "A deputy who can see a
--           child's score must see the comment attached to it."
-- Ruling 2: school admins read `class_shoutouts` SCHOOL-WIDE. That read IS
--           admin.html's "Messages" audit surface, and Mide calls it the
--           safeguarding control.
--
-- ── proven before applied ───────────────────────────────────────────
-- Rehearsed on TEST and proven across 63 cases with twelve real signed-in
-- sessions. Not one case was allowed that should have been refused. Every
-- refusal was made NON-VACUOUS: school B held a parallel stack, so the same
-- session returning 0 rows on A's data returned 1 on B's, through the policy
-- under test, in the same run. That matters because the last dead policy arm
-- hid behind a refusal that passed for the wrong reason.
--
-- ⚠️ Every test actor was made admin/SLT by a `staff_scopes` ROW ONLY — no
-- fixture profile carried `role='admin'`. `auth_user_has_scope` has a
-- dual-read fallback on `profiles.role='admin'` whose own comment says it is
-- removed at the prod-gate final flip; testing through it proves nothing
-- about life afterwards.
--
-- ── the state of prod when this landed ──────────────────────────────
-- `class_shoutouts` 0 rows, `submission_feedback` 0 rows. Neither widening
-- revealed anything that already existed. 3 live `school_admin` scopes,
-- 0 live `slt` scopes.
-- ⚠️ ONE profile carries `role='admin'` with NO scope row, so the dual-read
-- fallback grants it school-wide Messages read without a grant. That is
-- pre-existing behaviour shared with 29 other admin-gated policies, not
-- something these rulings introduce — but ruling 2 extends its reach to a
-- second table. Reported to Mide: either that person needs a real
-- `staff_scopes` row (or they silently lose access when the fallback goes),
-- or their role is wrong.

-- ── ruling 3 ────────────────────────────────────────────────────────
-- The scope test is FACTORED — `(school_admin OR slt) AND same_school` —
-- rather than two parallel disjuncts, so the same-school guard cannot drift
-- between the two scopes as this is edited later.
--
-- ⚠️ `auth_user_has_scope` has NO dual-read fallback for 'slt' (only 'hod'
-- and 'school_admin'), so this arm depends entirely on `staff_scopes` rows.
alter policy submission_feedback_select on public.submission_feedback
using (
  (
    deleted_at is null
    and (
      auth_user_teaches_class(submission_class_id(submission_id))
      or submission_student_id(submission_id) = auth.uid()
      or ((auth_user_has_scope('school_admin') or auth_user_has_scope('slt'))
          and class_school_id(submission_class_id(submission_id)) = auth_user_school_id())
    )
  )
  or (
    deleted_at is not null
    and (
      teacher_id = auth.uid()
      or ((auth_user_has_scope('school_admin') or auth_user_has_scope('slt'))
          and class_school_id(submission_class_id(submission_id)) = auth_user_school_id())
    )
  )
);

-- ── ruling 2 ────────────────────────────────────────────────────────
-- ⚠️ `slt` is deliberately NOT here. Ruling 3 names FEEDBACK specifically;
-- ruling 2 names school_admin only. The resulting asymmetry is measured and
-- real — in one session a deputy reads the comment on a child's score and
-- ZERO messages — and it is reported to Mide rather than resolved in code.
--
-- ⚠️ The second arm means a school admin reads SOFT-DELETED shoutouts: a
-- teacher can post a message, delete it, and the admin still sees it while
-- the recipient sees nothing. That is the retention half of the guardrail
-- meeting the audit half. It is the most sensitive single consequence of this
-- change and was proven on TEST, not inferred.
alter policy class_shoutouts_select on public.class_shoutouts
using (
  (
    deleted_at is null
    and (
      auth_user_teaches_class(class_id)
      or auth_user_is_member_of_class(class_id)
      or (auth_user_has_scope('school_admin')
          and class_school_id(class_id) = auth_user_school_id())
    )
  )
  or (
    deleted_at is not null
    and (
      author_id = auth.uid()
      or (auth_user_has_scope('school_admin')
          and class_school_id(class_id) = auth_user_school_id())
    )
  )
);
