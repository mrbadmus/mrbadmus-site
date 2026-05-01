-- =====================================================================
-- Migration:        0001_schools_layer.sql  (v2 — corrected section order)
-- Stage:            1 — Schools Layer Foundation
-- Branch:           schools/stage-1-schema-rls
-- Designed against: stage-1-design-v2.md
-- Apply target:     Test project first → production after green tests
-- Author:           Drafted with Mide on Friday 1 May 2026
-- =====================================================================
--
-- This migration builds the foundation for the schools layer of MrBadmusAI.
-- It creates 13 new tables, extends 2 existing tables, and adds RLS policies
-- enforcing the role pyramid: student → teacher → HoD → admin, with strict
-- cross-school isolation.
--
-- v2 NOTE — section ordering change vs v1:
--   v1 placed helper functions first (Section 1). PostgreSQL validates
--   LANGUAGE sql function bodies AT CREATE TIME, so the helpers failed
--   because they referenced columns/tables not yet created.
--
--   v2 reorders to: extend tables → new tables → helpers → RLS → policies →
--   profiles policies → seeds → indexes. All content is identical to v1;
--   only the order is changed. The helpers are still LANGUAGE sql (preserves
--   inlining performance for RLS calls).
--
-- Wrapped in a single transaction. If any step fails, the whole migration
-- rolls back atomically.
-- =====================================================================

BEGIN;

-- SECTION 1 — EXTEND EXISTING TABLES (design doc §2.1, §3)
-- =====================================================================

-- 1.1 ───────────────────────────────────────────────────────────────────
-- Extend `schools` (currently 0 rows, no policies)
-- ───────────────────────────────────────────────────────────────────────
ALTER TABLE public.schools
  ADD COLUMN IF NOT EXISTS slug text UNIQUE,
  ADD COLUMN IF NOT EXISTS email_domains text[] DEFAULT '{}',
  ADD COLUMN IF NOT EXISTS subdomain text UNIQUE,
  ADD COLUMN IF NOT EXISTS show_on_public_leaderboard boolean DEFAULT true,
  ADD COLUMN IF NOT EXISTS key_stages_supported text[] DEFAULT ARRAY['KS3','KS4'],
  ADD COLUMN IF NOT EXISTS departments text[] DEFAULT ARRAY['Science'],
  ADD COLUMN IF NOT EXISTS updated_at timestamptz DEFAULT now(),
  ADD COLUMN IF NOT EXISTS deleted_at timestamptz;


-- 1.2 ───────────────────────────────────────────────────────────────────
-- Extend `profiles` (33 existing rows — handle with care)
-- ───────────────────────────────────────────────────────────────────────

-- Add new columns. All nullable for backward-compatibility with existing rows.
ALTER TABLE public.profiles
  ADD COLUMN IF NOT EXISTS school_id uuid REFERENCES public.schools(id),
  ADD COLUMN IF NOT EXISTS role text DEFAULT 'student',
  ADD COLUMN IF NOT EXISTS department text,
  ADD COLUMN IF NOT EXISTS key_stage text,
  ADD COLUMN IF NOT EXISTS deleted_at timestamptz;

-- Remove the AQA default on exam_board (per design doc §3 / Mide's feedback).
-- New users get NULL; their effective board is read from school_subject_settings.
-- Existing 33 rows keep whatever value they currently have — we don't touch them.
ALTER TABLE public.profiles ALTER COLUMN exam_board DROP DEFAULT;

-- Backfill key_stage = 'KS4' for the 33 existing rows (design doc §6.1).
-- This must happen BEFORE we add the CHECK constraint, otherwise rows with
-- non-NULL tier and NULL key_stage would fail the constraint.
UPDATE public.profiles SET key_stage = 'KS4' WHERE key_stage IS NULL;

-- Now add the CHECK constraints (design doc §3).
-- 1. role must be one of the valid options
ALTER TABLE public.profiles
  ADD CONSTRAINT profiles_role_check
  CHECK (role IN ('student', 'teacher', 'hod', 'admin'));

-- 2. key_stage must be one of the valid options if set
ALTER TABLE public.profiles
  ADD CONSTRAINT profiles_key_stage_check
  CHECK (key_stage IS NULL OR key_stage IN ('KS3', 'KS4', 'KS5'));

-- 3. tier and science_pathway only valid when key_stage = 'KS4'
ALTER TABLE public.profiles
  ADD CONSTRAINT profiles_tier_only_ks4_check
  CHECK (
    (tier IS NULL AND science_pathway IS NULL)
    OR key_stage = 'KS4'
  );

-- 4. department required when role = 'hod'
ALTER TABLE public.profiles
  ADD CONSTRAINT profiles_hod_needs_department_check
  CHECK (
    role <> 'hod' OR department IS NOT NULL
  );

-- 5. school_id required for staff roles (students can be unattached legacy)
ALTER TABLE public.profiles
  ADD CONSTRAINT profiles_staff_needs_school_check
  CHECK (
    role = 'student' OR school_id IS NOT NULL
  );


-- =====================================================================
-- SECTION 2 — NEW TABLES (design doc §2.2 through §2.14)
-- =====================================================================

-- 2.1 ───────────────────────────────────────────────────────────────────
-- subjects (global lookup) — design doc §2.3
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.subjects (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text UNIQUE NOT NULL,
  department text NOT NULL,
  display_order smallint,
  active boolean DEFAULT true,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);


-- 2.2 ───────────────────────────────────────────────────────────────────
-- academic_years — design doc §2.2
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.academic_years (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id uuid NOT NULL REFERENCES public.schools(id),
  name text NOT NULL,
  start_date date,
  end_date date,
  is_current boolean DEFAULT false,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  UNIQUE (school_id, name)
);


-- 2.3 ───────────────────────────────────────────────────────────────────
-- school_subject_settings — design doc §2.4
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.school_subject_settings (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id uuid NOT NULL REFERENCES public.schools(id),
  subject_id uuid NOT NULL REFERENCES public.subjects(id),
  exam_board text NOT NULL CHECK (exam_board IN (
    'AQA', 'Edexcel', 'OCR', 'WJEC', 'CCEA', 'Eduqas', 'CIE', 'SQA'
  )),
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  UNIQUE (school_id, subject_id)
);


-- 2.4 ───────────────────────────────────────────────────────────────────
-- scheme_of_work_entries (global) — design doc §2.8
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.scheme_of_work_entries (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  key_stage text NOT NULL CHECK (key_stage IN ('KS3','KS4','KS5')),
  year_group smallint NOT NULL CHECK (year_group BETWEEN 7 AND 13),
  tier text CHECK (tier IS NULL OR tier IN ('foundation','higher')),
  pathway text CHECK (pathway IS NULL OR pathway IN ('combined','triple')),
  subject_id uuid NOT NULL REFERENCES public.subjects(id),
  exam_board text NOT NULL CHECK (exam_board IN (
    'AQA','Edexcel','OCR','WJEC','CCEA','Eduqas','CIE','SQA'
  )),
  academic_week smallint NOT NULL CHECK (academic_week BETWEEN 1 AND 39),
  topic text NOT NULL,
  subtopic text,
  notes text,
  active boolean DEFAULT true,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  UNIQUE (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week)
);


-- 2.5 ───────────────────────────────────────────────────────────────────
-- scheme_of_work_overrides (per-school) — design doc §2.9
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.scheme_of_work_overrides (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id uuid NOT NULL REFERENCES public.schools(id),
  key_stage text NOT NULL CHECK (key_stage IN ('KS3','KS4','KS5')),
  year_group smallint NOT NULL CHECK (year_group BETWEEN 7 AND 13),
  tier text CHECK (tier IS NULL OR tier IN ('foundation','higher')),
  pathway text CHECK (pathway IS NULL OR pathway IN ('combined','triple')),
  subject_id uuid NOT NULL REFERENCES public.subjects(id),
  academic_week smallint NOT NULL CHECK (academic_week BETWEEN 1 AND 39),
  topic text NOT NULL,
  subtopic text,
  notes text,
  created_by uuid REFERENCES public.profiles(id),
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  UNIQUE (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week)
);


-- 2.6 ───────────────────────────────────────────────────────────────────
-- classes — design doc §2.5
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.classes (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id uuid NOT NULL REFERENCES public.schools(id),
  academic_year_id uuid NOT NULL REFERENCES public.academic_years(id),
  name text NOT NULL,
  key_stage text NOT NULL CHECK (key_stage IN ('KS3','KS4','KS5')),
  year_group smallint NOT NULL CHECK (year_group BETWEEN 7 AND 13),
  tier text CHECK (tier IS NULL OR tier IN ('foundation','higher')),
  science_pathway text CHECK (science_pathway IS NULL OR science_pathway IN ('combined','triple')),
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  UNIQUE (school_id, academic_year_id, name),
  CONSTRAINT classes_tier_only_ks4_check
    CHECK ((tier IS NULL AND science_pathway IS NULL) OR key_stage = 'KS4')
);


-- 2.7 ───────────────────────────────────────────────────────────────────
-- class_members (students in classes) — design doc §2.6
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.class_members (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  class_id uuid NOT NULL REFERENCES public.classes(id),
  student_id uuid NOT NULL REFERENCES public.profiles(id),
  joined_via text NOT NULL CHECK (joined_via IN (
    'code','csv_import','sims_sync','admin_added'
  )),
  joined_at timestamptz DEFAULT now(),
  left_at timestamptz,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz
);

-- A student can only have one *active* membership per class at a time.
-- Historic rows (with left_at set) are allowed to coexist for audit history.
CREATE UNIQUE INDEX class_members_active_unique
  ON public.class_members (class_id, student_id)
  WHERE left_at IS NULL AND deleted_at IS NULL;


-- 2.8 ───────────────────────────────────────────────────────────────────
-- class_teachers (teachers in classes, with subject) — design doc §2.7
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.class_teachers (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  class_id uuid NOT NULL REFERENCES public.classes(id),
  teacher_id uuid NOT NULL REFERENCES public.profiles(id),
  subject_id uuid REFERENCES public.subjects(id),
  role text NOT NULL CHECK (role IN ('subject_teacher','form_tutor','cover_teacher')),
  started_at timestamptz DEFAULT now(),
  ended_at timestamptz,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  -- subject_id required for subject_teacher role; NULL for form_tutor
  CONSTRAINT class_teachers_subject_required_check CHECK (
    (role = 'form_tutor' AND subject_id IS NULL)
    OR (role IN ('subject_teacher','cover_teacher') AND subject_id IS NOT NULL)
  )
);

-- A teacher can only have one *active* assignment per (class, subject, role).
CREATE UNIQUE INDEX class_teachers_active_unique
  ON public.class_teachers (class_id, teacher_id, subject_id, role)
  WHERE ended_at IS NULL AND deleted_at IS NULL;


-- 2.9 ───────────────────────────────────────────────────────────────────
-- assignments — design doc §2.10
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE public.assignments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  class_id uuid NOT NULL REFERENCES public.classes(id),
  teacher_id uuid REFERENCES public.profiles(id),
  subject_id uuid NOT NULL REFERENCES public.subjects(id),
  topic text NOT NULL,
  subtopic text,
  title text NOT NULL,
  instructions text,
  quiz_type text NOT NULL CHECK (quiz_type IN (
    'topic_quiz','subtopic_quiz','weekly_challenge'
  )),
  due_at timestamptz,
  auto_generated boolean DEFAULT true,
  source_sow_entry_id uuid REFERENCES public.scheme_of_work_entries(id),
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz
);


-- 2.10 ──────────────────────────────────────────────────────────────────
-- assignment_submissions — design doc §2.11
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE public.assignment_submissions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  assignment_id uuid NOT NULL REFERENCES public.assignments(id),
  student_id uuid NOT NULL REFERENCES public.profiles(id),
  score smallint,
  max_score smallint,
  total_time_seconds integer,
  submitted_at timestamptz,
  attempts smallint DEFAULT 0,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz
);


-- 2.11 ──────────────────────────────────────────────────────────────────
-- assignment_question_attempts — design doc §2.12
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE public.assignment_question_attempts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  submission_id uuid NOT NULL REFERENCES public.assignment_submissions(id),
  question_index smallint NOT NULL,
  question_text text,        -- denormalised snapshot (correctness, not speed)
  selected_answer text,
  correct_answer text,       -- denormalised snapshot (correctness, not speed)
  is_correct boolean NOT NULL,
  time_spent_seconds integer,
  attempt_number smallint DEFAULT 1,
  created_at timestamptz DEFAULT now()
);


-- 2.12 ──────────────────────────────────────────────────────────────────
-- school_invitations — design doc §2.13
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE public.school_invitations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id uuid NOT NULL REFERENCES public.schools(id),
  email text NOT NULL,
  role text NOT NULL CHECK (role IN ('teacher','hod','admin')),
  department text,
  token text UNIQUE NOT NULL,
  expires_at timestamptz NOT NULL,
  accepted_at timestamptz,
  invited_by uuid REFERENCES public.profiles(id),
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  deleted_at timestamptz,
  CONSTRAINT invitations_hod_needs_dept_check CHECK (
    role <> 'hod' OR department IS NOT NULL
  )
);


-- 2.13 ──────────────────────────────────────────────────────────────────
-- audit_log (append-only) — design doc §2.14
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE public.audit_log (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  actor_id uuid REFERENCES public.profiles(id),
  school_id uuid REFERENCES public.schools(id),
  action text NOT NULL,
  target_table text NOT NULL,
  target_id uuid,
  payload jsonb,
  created_at timestamptz DEFAULT now()
);


-- =====================================================================
-- =====================================================================
-- SECTION 3 — HELPER FUNCTIONS (design doc §4.1)
-- =====================================================================
-- These small functions are used by every RLS policy. Marked STABLE so
-- Postgres caches results within a query — without this, RLS becomes
-- painfully slow.
-- =====================================================================

-- Returns the school_id of the currently logged-in user.
-- NULL for legacy unattached users (they pass through but RLS denies them
-- access to school-scoped data).
CREATE OR REPLACE FUNCTION public.auth_user_school_id()
RETURNS uuid
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT school_id FROM public.profiles WHERE id = auth.uid();
$$;

-- Returns the user's role: 'student', 'teacher', 'hod', or 'admin'.
CREATE OR REPLACE FUNCTION public.auth_user_role()
RETURNS text
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT role FROM public.profiles WHERE id = auth.uid();
$$;

-- Returns the user's department, e.g. 'Science'. NULL for non-HoD roles.
CREATE OR REPLACE FUNCTION public.auth_user_department()
RETURNS text
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT department FROM public.profiles WHERE id = auth.uid();
$$;

-- Wrapper around auth.uid() for consistency across policies.
CREATE OR REPLACE FUNCTION public.auth_user_id()
RETURNS uuid
LANGUAGE sql
STABLE
AS $$
  SELECT auth.uid();
$$;

-- Returns the school_id of a given class. Used by tables that don't carry
-- school_id directly (assignments, submissions, attempts).
CREATE OR REPLACE FUNCTION public.class_school_id(p_class_id uuid)
RETURNS uuid
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT school_id FROM public.classes WHERE id = p_class_id;
$$;

-- True if the logged-in teacher has an active row in class_teachers
-- (i.e. ended_at IS NULL) for the given class.
CREATE OR REPLACE FUNCTION public.auth_user_teaches_class(p_class_id uuid)
RETURNS boolean
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.class_teachers
    WHERE class_id = p_class_id
      AND teacher_id = auth.uid()
      AND ended_at IS NULL
      AND deleted_at IS NULL
  );
$$;

-- True if the logged-in student is in class_members for the given class
-- with no left_at timestamp.
CREATE OR REPLACE FUNCTION public.auth_user_is_member_of_class(p_class_id uuid)
RETURNS boolean
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.class_members
    WHERE class_id = p_class_id
      AND student_id = auth.uid()
      AND left_at IS NULL
      AND deleted_at IS NULL
  );
$$;

-- True if the user is HoD AND their department matches the given subject's
-- department. Used by RLS on subject-scoped tables.
CREATE OR REPLACE FUNCTION public.auth_user_is_hod_of_subject_dept(p_subject_id uuid)
RETURNS boolean
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.subjects s
    WHERE s.id = p_subject_id
      AND s.department = public.auth_user_department()
      AND public.auth_user_role() = 'hod'
  );
$$;


-- =====================================================================
-- SECTION 4 — ENABLE RLS ON ALL NEW TABLES (design doc §4)
-- =====================================================================
-- Default-deny: enable RLS first, then add specific permit policies.
-- Any table without policies will simply return zero rows for non-superusers.
-- =====================================================================

ALTER TABLE public.subjects                       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.academic_years                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.school_subject_settings        ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.scheme_of_work_entries         ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.scheme_of_work_overrides       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.classes                        ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.class_members                  ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.class_teachers                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.assignments                    ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.assignment_submissions         ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.assignment_question_attempts   ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.school_invitations             ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.audit_log                      ENABLE ROW LEVEL SECURITY;


-- =====================================================================
-- SECTION 5 — RLS POLICIES (design doc §4.2)
-- =====================================================================
-- Naming convention: <table>_<who>_<action>
-- Every policy traces back to a line in design doc §4.2.
-- =====================================================================

-- 5.1 ───────────────────────────────────────────────────────────────────
-- schools
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY schools_member_read ON public.schools
  FOR SELECT USING (id = public.auth_user_school_id());

CREATE POLICY schools_admin_update ON public.schools
  FOR UPDATE USING (
    id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

-- INSERT/DELETE on schools: locked. Stage 6 onboarding will add insert via
-- a SECURITY DEFINER function, not via direct policy.


-- 5.2 ───────────────────────────────────────────────────────────────────
-- academic_years
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY academic_years_member_read ON public.academic_years
  FOR SELECT USING (school_id = public.auth_user_school_id());

CREATE POLICY academic_years_admin_write ON public.academic_years
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );


-- 5.3 ───────────────────────────────────────────────────────────────────
-- subjects (global)
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY subjects_authenticated_read ON public.subjects
  FOR SELECT TO authenticated USING (true);

-- INSERT/UPDATE: locked. Platform admin (you) inserts manually.


-- 5.4 ───────────────────────────────────────────────────────────────────
-- school_subject_settings
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY sss_member_read ON public.school_subject_settings
  FOR SELECT USING (school_id = public.auth_user_school_id());

CREATE POLICY sss_admin_write ON public.school_subject_settings
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

CREATE POLICY sss_hod_write ON public.school_subject_settings
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'hod'
    AND public.auth_user_is_hod_of_subject_dept(subject_id)
  );


-- 5.5 ───────────────────────────────────────────────────────────────────
-- scheme_of_work_entries (global read)
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY sow_entries_authenticated_read ON public.scheme_of_work_entries
  FOR SELECT TO authenticated USING (true);

-- INSERT/UPDATE: locked. Platform admin only.


-- 5.6 ───────────────────────────────────────────────────────────────────
-- scheme_of_work_overrides
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY sow_overrides_member_read ON public.scheme_of_work_overrides
  FOR SELECT USING (school_id = public.auth_user_school_id());

CREATE POLICY sow_overrides_admin_write ON public.scheme_of_work_overrides
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

CREATE POLICY sow_overrides_hod_write ON public.scheme_of_work_overrides
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'hod'
    AND public.auth_user_is_hod_of_subject_dept(subject_id)
  );


-- 5.7 ───────────────────────────────────────────────────────────────────
-- classes
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY classes_student_read ON public.classes
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_is_member_of_class(id)
  );

CREATE POLICY classes_teacher_read ON public.classes
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_teaches_class(id)
  );

CREATE POLICY classes_hod_read ON public.classes
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'hod'
  );

CREATE POLICY classes_admin_read ON public.classes
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

CREATE POLICY classes_staff_write ON public.classes
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() IN ('teacher','hod','admin')
  );


-- 5.8 ───────────────────────────────────────────────────────────────────
-- class_members
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY class_members_self_read ON public.class_members
  FOR SELECT USING (student_id = public.auth_user_id());

CREATE POLICY class_members_teacher_read ON public.class_members
  FOR SELECT USING (
    public.auth_user_teaches_class(class_id)
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

CREATE POLICY class_members_hod_read ON public.class_members
  FOR SELECT USING (
    public.auth_user_role() = 'hod'
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

CREATE POLICY class_members_admin_read ON public.class_members
  FOR SELECT USING (
    public.auth_user_role() = 'admin'
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

-- Students self-insert via Stage 3 join code flow
CREATE POLICY class_members_self_insert ON public.class_members
  FOR INSERT WITH CHECK (
    student_id = public.auth_user_id()
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

-- Teachers/admins can add students to classes they teach/manage
CREATE POLICY class_members_staff_insert ON public.class_members
  FOR INSERT WITH CHECK (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND (
      public.auth_user_role() = 'admin'
      OR public.auth_user_teaches_class(class_id)
    )
  );

-- Teachers/admins can update (mostly to set left_at)
CREATE POLICY class_members_staff_update ON public.class_members
  FOR UPDATE USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND (
      public.auth_user_role() = 'admin'
      OR public.auth_user_teaches_class(class_id)
    )
  );


-- 5.9 ───────────────────────────────────────────────────────────────────
-- class_teachers
-- ───────────────────────────────────────────────────────────────────────
CREATE POLICY class_teachers_self_read ON public.class_teachers
  FOR SELECT USING (teacher_id = public.auth_user_id());

CREATE POLICY class_teachers_hod_read ON public.class_teachers
  FOR SELECT USING (
    public.auth_user_role() = 'hod'
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

CREATE POLICY class_teachers_admin_read ON public.class_teachers
  FOR SELECT USING (
    public.auth_user_role() = 'admin'
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

CREATE POLICY class_teachers_admin_write ON public.class_teachers
  FOR ALL USING (
    public.auth_user_role() = 'admin'
    AND public.class_school_id(class_id) = public.auth_user_school_id()
  );

CREATE POLICY class_teachers_hod_write ON public.class_teachers
  FOR ALL USING (
    public.auth_user_role() = 'hod'
    AND public.class_school_id(class_id) = public.auth_user_school_id()
    AND (subject_id IS NULL OR public.auth_user_is_hod_of_subject_dept(subject_id))
  );


-- 5.10 ──────────────────────────────────────────────────────────────────
-- assignments — uses class_school_id() since no school_id on table
-- ──────────────────────────────────────────────────────────────────────
CREATE POLICY assignments_student_read ON public.assignments
  FOR SELECT USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND public.auth_user_is_member_of_class(class_id)
  );

CREATE POLICY assignments_teacher_read ON public.assignments
  FOR SELECT USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND public.auth_user_teaches_class(class_id)
  );

CREATE POLICY assignments_hod_read ON public.assignments
  FOR SELECT USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND public.auth_user_role() = 'hod'
    AND public.auth_user_is_hod_of_subject_dept(subject_id)
  );

CREATE POLICY assignments_admin_read ON public.assignments
  FOR SELECT USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

CREATE POLICY assignments_teacher_write ON public.assignments
  FOR ALL USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND public.auth_user_teaches_class(class_id)
  );

CREATE POLICY assignments_admin_write ON public.assignments
  FOR ALL USING (
    public.class_school_id(class_id) = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );


-- 5.11 ──────────────────────────────────────────────────────────────────
-- assignment_submissions
-- ──────────────────────────────────────────────────────────────────────
CREATE POLICY submissions_self_all ON public.assignment_submissions
  FOR ALL USING (student_id = public.auth_user_id());

CREATE POLICY submissions_teacher_read ON public.assignment_submissions
  FOR SELECT USING (
    EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_id
        AND public.auth_user_teaches_class(a.class_id)
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  );

CREATE POLICY submissions_teacher_update ON public.assignment_submissions
  FOR UPDATE USING (
    EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_id
        AND public.auth_user_teaches_class(a.class_id)
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  );

CREATE POLICY submissions_hod_read ON public.assignment_submissions
  FOR SELECT USING (
    public.auth_user_role() = 'hod'
    AND EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_id
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
        AND public.auth_user_is_hod_of_subject_dept(a.subject_id)
    )
  );

CREATE POLICY submissions_admin_read ON public.assignment_submissions
  FOR SELECT USING (
    public.auth_user_role() = 'admin'
    AND EXISTS (
      SELECT 1 FROM public.assignments a
      WHERE a.id = assignment_id
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  );


-- 5.12 ──────────────────────────────────────────────────────────────────
-- assignment_question_attempts — visibility follows submission
-- ──────────────────────────────────────────────────────────────────────
CREATE POLICY attempts_self_all ON public.assignment_question_attempts
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.assignment_submissions s
      WHERE s.id = submission_id
        AND s.student_id = public.auth_user_id()
    )
  );

CREATE POLICY attempts_teacher_read ON public.assignment_question_attempts
  FOR SELECT USING (
    EXISTS (
      SELECT 1
      FROM public.assignment_submissions s
      JOIN public.assignments a ON a.id = s.assignment_id
      WHERE s.id = submission_id
        AND public.auth_user_teaches_class(a.class_id)
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  );

CREATE POLICY attempts_hod_read ON public.assignment_question_attempts
  FOR SELECT USING (
    public.auth_user_role() = 'hod'
    AND EXISTS (
      SELECT 1
      FROM public.assignment_submissions s
      JOIN public.assignments a ON a.id = s.assignment_id
      WHERE s.id = submission_id
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
        AND public.auth_user_is_hod_of_subject_dept(a.subject_id)
    )
  );

CREATE POLICY attempts_admin_read ON public.assignment_question_attempts
  FOR SELECT USING (
    public.auth_user_role() = 'admin'
    AND EXISTS (
      SELECT 1
      FROM public.assignment_submissions s
      JOIN public.assignments a ON a.id = s.assignment_id
      WHERE s.id = submission_id
        AND public.class_school_id(a.class_id) = public.auth_user_school_id()
    )
  );


-- 5.13 ──────────────────────────────────────────────────────────────────
-- school_invitations
-- ──────────────────────────────────────────────────────────────────────
CREATE POLICY invitations_admin_all ON public.school_invitations
  FOR ALL USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

-- Special: invited person reads own invitation by token (no auth required
-- pre-signup, but Stage 6 will add a public RPC for this — for now, only
-- authenticated users with matching email can read their own).
CREATE POLICY invitations_invitee_read ON public.school_invitations
  FOR SELECT TO authenticated USING (
    email = (SELECT email FROM auth.users WHERE id = auth.uid())
    AND accepted_at IS NULL
    AND expires_at > now()
  );


-- 5.14 ──────────────────────────────────────────────────────────────────
-- audit_log (append-only)
-- ──────────────────────────────────────────────────────────────────────
CREATE POLICY audit_admin_read ON public.audit_log
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );

CREATE POLICY audit_hod_read ON public.audit_log
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'hod'
  );

-- INSERT: locked at policy level. Triggers will use SECURITY DEFINER
-- functions to insert, bypassing RLS. No user can insert directly.
-- UPDATE/DELETE: nothing — append-only by design.


-- =====================================================================
-- SECTION 6 — EXTEND EXISTING `profiles` POLICIES (design doc §4.2)
-- =====================================================================
-- The existing profiles policies (Users can view/insert/update own profile)
-- need extending so teachers can read their students, HoDs can read their
-- department's profiles, and admins can read their school.
-- We DON'T drop the existing policies — we add alongside them.
-- =====================================================================

-- Teachers can read profiles of students in classes they teach
CREATE POLICY profiles_teacher_read_students ON public.profiles
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND role = 'student'
    AND EXISTS (
      SELECT 1 FROM public.class_members cm
      WHERE cm.student_id = profiles.id
        AND public.auth_user_teaches_class(cm.class_id)
        AND cm.left_at IS NULL
    )
  );

-- HoDs can read profiles of teachers in their department + students in their dept's classes
CREATE POLICY profiles_hod_read_dept ON public.profiles
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'hod'
    AND (
      department = public.auth_user_department()
      OR role = 'student'
    )
  );

-- Admins can read all profiles in their school
CREATE POLICY profiles_admin_read_school ON public.profiles
  FOR SELECT USING (
    school_id = public.auth_user_school_id()
    AND public.auth_user_role() = 'admin'
  );


-- =====================================================================
-- SECTION 7 — SEEDS (design doc §6.1)
-- =====================================================================

-- 7.1 ───────────────────────────────────────────────────────────────────
-- subjects: Biology, Chemistry, Physics
-- ───────────────────────────────────────────────────────────────────────
INSERT INTO public.subjects (name, department, display_order, active)
VALUES
  ('Biology',   'Science', 1, true),
  ('Chemistry', 'Science', 2, true),
  ('Physics',   'Science', 3, true);


-- 7.2 ───────────────────────────────────────────────────────────────────
-- Rainford High School (the pilot school)
-- ───────────────────────────────────────────────────────────────────────
INSERT INTO public.schools (
  name, code, slug, email_domains,
  show_on_public_leaderboard,
  key_stages_supported, departments,
  active
)
VALUES (
  'Rainford High School',
  'RHS',
  'rainford-high',
  ARRAY['rainford.org.uk'],  -- single domain for both staff and students
  true,
  ARRAY['KS3','KS4'],
  ARRAY['Science'],
  true
);


-- 7.3 ───────────────────────────────────────────────────────────────────
-- Rainford 2025-26 academic year (current)
-- ───────────────────────────────────────────────────────────────────────
INSERT INTO public.academic_years (school_id, name, start_date, end_date, is_current)
SELECT id, '2025-26', '2025-09-01'::date, '2026-08-31'::date, true
FROM public.schools WHERE slug = 'rainford-high';


-- 7.4 ───────────────────────────────────────────────────────────────────
-- Rainford × {Biology, Chemistry, Physics} → AQA
-- ───────────────────────────────────────────────────────────────────────
INSERT INTO public.school_subject_settings (school_id, subject_id, exam_board)
SELECT
  (SELECT id FROM public.schools WHERE slug = 'rainford-high'),
  s.id,
  'AQA'
FROM public.subjects s
WHERE s.name IN ('Biology','Chemistry','Physics');


-- =====================================================================
-- SECTION 8 — INDEXES FOR RLS PERFORMANCE
-- =====================================================================
-- RLS policies hit these columns hard. Indexes keep things fast at scale.
-- =====================================================================

CREATE INDEX idx_profiles_school_id          ON public.profiles(school_id);
CREATE INDEX idx_profiles_role               ON public.profiles(role);
CREATE INDEX idx_classes_school_id           ON public.classes(school_id);
CREATE INDEX idx_class_members_student_id    ON public.class_members(student_id);
CREATE INDEX idx_class_members_class_id      ON public.class_members(class_id);
CREATE INDEX idx_class_teachers_teacher_id   ON public.class_teachers(teacher_id);
CREATE INDEX idx_class_teachers_class_id     ON public.class_teachers(class_id);
CREATE INDEX idx_assignments_class_id        ON public.assignments(class_id);
CREATE INDEX idx_assignments_subject_id      ON public.assignments(subject_id);
CREATE INDEX idx_submissions_assignment_id   ON public.assignment_submissions(assignment_id);
CREATE INDEX idx_submissions_student_id      ON public.assignment_submissions(student_id);
CREATE INDEX idx_attempts_submission_id      ON public.assignment_question_attempts(submission_id);
CREATE INDEX idx_audit_log_school_id         ON public.audit_log(school_id);
CREATE INDEX idx_audit_log_actor_id          ON public.audit_log(actor_id);
CREATE INDEX idx_sow_lookup                  ON public.scheme_of_work_entries(
  key_stage, year_group, subject_id, exam_board, academic_week
);


COMMIT;

-- =====================================================================
-- END OF MIGRATION (v2)
-- v1 had a section-ordering bug. v2 reorders sections so columns/tables
-- referenced by helper functions exist before the helpers are created.
-- All content otherwise identical.
-- =====================================================================
