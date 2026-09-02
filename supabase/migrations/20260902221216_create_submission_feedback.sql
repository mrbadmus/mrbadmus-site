-- MRB-306 Phase 2b — teacher free-text feedback on one assignment submission.
--
-- ⚠️ FILENAME VERSION IS NOT COSMETIC. This was applied to prod via MCP
-- `apply_migration`, which records its OWN `schema_migrations` version —
-- 20260902221216. The filename must match it or `db push` re-applies the
-- whole thing. (Same trap as the MRB-84 note in CLAUDE.md.)
--
-- ── why a new table and not class_shoutouts ─────────────────────────
-- `class_shoutouts` is (id, class_id NOT NULL, author_id NOT NULL,
-- recipient_id NOT NULL, template_key, message, …). Three reasons it does not
-- fit: feedback binds to a SUBMISSION, not a class+member, so reusing it makes
-- two NOT NULL columns conditionally meaningful and needs a CHECK to express
-- "exactly one binding"; there is nowhere to keep a prior body on edit, and
-- adding one imposes that rule on shoutouts too; and `template_key` is
-- enum-constrained where feedback is free text.
--
-- ── proven, not merely rehearsed ────────────────────────────────────
-- Rehearsed on TEST (qeppkiswvclkkwbxmlok), then PROVEN there with TWELVE
-- real signed-in sessions. That mattered: the MCP runs as the service role,
-- which bypasses RLS entirely, so the six constraint probes proved the shape
-- and nothing whatever about access.

create or replace function public.submission_class_id(p_submission_id uuid)
returns uuid language sql stable security definer set search_path = public as $$
  select a.class_id
  from assignment_submissions s
  join assignments a on a.id = s.assignment_id
  where s.id = p_submission_id
$$;

create or replace function public.submission_student_id(p_submission_id uuid)
returns uuid language sql stable security definer set search_path = public as $$
  select s.student_id from assignment_submissions s where s.id = p_submission_id
$$;

create table public.submission_feedback (
  id            uuid primary key default gen_random_uuid(),
  submission_id uuid not null references public.assignment_submissions(id) on delete restrict,
  teacher_id    uuid not null references public.profiles(id) on delete restrict,
  body          text not null,
  prior_body    text,
  created_at    timestamptz not null default now(),
  edited_at     timestamptz,
  deleted_at    timestamptz,
  -- plain text, sane cap. 2000 against class_shoutouts' 500: feedback on a
  -- piece of work is a paragraph, a shoutout is a sentence.
  constraint submission_feedback_body_length_chk
    check (char_length(body) between 1 and 2000),
  constraint submission_feedback_prior_body_length_chk
    check (prior_body is null or char_length(prior_body) <= 2000),
  -- RETENTION, ENFORCED BY THE DATABASE, not by the app remembering to.
  -- An edit must leave the prior body behind, and only an edit may.
  constraint submission_feedback_edited_chk
    check ((edited_at is null) = (prior_body is null))
);

create index submission_feedback_submission_idx
  on public.submission_feedback (submission_id) where deleted_at is null;
create index submission_feedback_teacher_idx
  on public.submission_feedback (teacher_id) where deleted_at is null;

alter table public.submission_feedback enable row level security;

-- READ. Teacher of the class, the student who owns the submission, or a school
-- admin in the same school. Deleted rows: the author, or a school admin.
--
-- ⚠️ TWO THINGS HERE ARE LOAD-BEARING. BOTH WERE PROVEN ON TEST.
--
-- 1. `auth_user_has_scope('school_admin')`, NOT `auth_user_role() =
--    'school_admin'`. The first draft used the latter and it is DEAD CODE:
--    `auth_user_role()` reads `profiles.role`, whose CHECK permits only
--    student/teacher/hod/admin/parent — 'school_admin' is not a legal value of
--    that column, so the arm could never be true for anyone, in any school.
--    The symptom, measured in one request: a real admin read a child's
--    SUBMISSION and got zero rows for the FEEDBACK attached to it. Every other
--    admin-gated policy in the estate uses the scope helper.
--    ⚠️ Test it with a `staff_scopes` row, NOT with `role='admin'` —
--    `auth_user_has_scope` has a dual-read fallback its own comment says is
--    removed at the prod-gate final flip, so a test via the fallback proves
--    nothing about life after it.
--
-- 2. The trailing `deleted_at IS NOT NULL` arm. Postgres applies SELECT USING
--    to the POST-update row, so a SELECT policy filtering `deleted_at IS NULL`
--    makes the soft-delete UPDATE fail 42501 even when the UPDATE policy
--    passes. Proven by building the buggy shape, watching it 42501 in both
--    `return=representation` and `return=minimal`, then curing it with this
--    arm. Precedent: 20260524195500_fix_class_shoutouts_soft_delete.sql.
--
-- ⚠️ `slt` is DELIBERATELY ABSENT, unlike every sibling admin-read policy
-- (`submissions_admin_read`, `classes_admin_read`, … all read
-- `school_admin OR slt`). So a deputy or head of year sees a child's
-- submission and score but not the written feedback on it. That asymmetry is
-- intentional: written feedback naming a child is more sensitive than a
-- submission count, and Mide's guardrails for this feature are defaults he may
-- loosen and the build may not. One `or auth_user_has_scope('slt')` per arm
-- opens it — his call, not a bug.
create policy submission_feedback_select on public.submission_feedback
for select using (
  (
    deleted_at is null
    and (
      auth_user_teaches_class(submission_class_id(submission_id))
      or submission_student_id(submission_id) = auth.uid()
      or (auth_user_has_scope('school_admin')
          and class_school_id(submission_class_id(submission_id)) = auth_user_school_id())
    )
  )
  or (
    deleted_at is not null
    and (
      teacher_id = auth.uid()
      or (auth_user_has_scope('school_admin')
          and class_school_id(submission_class_id(submission_id)) = auth_user_school_id())
    )
  )
);

-- WRITE. Teachers of the class only, always as themselves.
-- There is deliberately NO insert path for a student: v1 is one-way. Proven on
-- TEST both as the student and with a forged `teacher_id` — 42501 each time.
create policy submission_feedback_insert on public.submission_feedback
for insert with check (
  teacher_id = auth.uid()
  and auth_user_teaches_class(submission_class_id(submission_id))
  and class_school_id(submission_class_id(submission_id)) = auth_user_school_id()
);

create policy submission_feedback_update on public.submission_feedback
for update using (
  teacher_id = auth.uid()
  and auth_user_teaches_class(submission_class_id(submission_id))
) with check (
  teacher_id = auth.uid()
  and auth_user_teaches_class(submission_class_id(submission_id))
);

-- No DELETE policy: removal is a soft delete via deleted_at.

comment on table public.submission_feedback is
  'MRB-306: teacher free-text feedback on one assignment submission. Auditable (school admins read all), one-way (no student write path), context-bound (no general inbox), attributed and retained (prior_body kept on edit, enforced by CHECK).';
