-- =====================================================================
-- Migration:        0006_stage2_test_seeds_expanded.sql
-- Stage:            2A — extended test fixtures for /teacher/* dashboard
-- Branch:           schools/stage-2a-test-seeds-expanded
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) — fake data only
-- Linear:           MRB-39 (blocks MRB-20 + MRB-38)
-- =====================================================================
--
-- Extends 0002's seed (Sarah / 10X1 Biology / Triple) with the two
-- remaining MRB-20 dashboard modes — KS3 and KS4 Combined — plus a
-- second KS4 Triple class so we can verify the multi-class case.
--
-- After this migration applies, the test project will hold:
--
--   ── Pre-existing (from 0002) ────────────────────────────────────
--   1 teacher  (Sarah Whitfield)
--   1 class    (10X1 Biology — KS4 / Higher / Triple)
--   7 students, 4 assignments, 22 submissions
--
--   ── Added by this migration ─────────────────────────────────────
--   2 teachers (Mide Badmus, J Okonkwo)
--   3 classes:
--     8X1         — KS3   / Y8  / no tier or pathway   — Science
--     10A         — KS4   / Y10 / Higher / Combined    — Bio+Chem+Phys
--     10Z Physics — KS4   / Y10 / Higher / Triple      — Physics only
--   13 students  (5 KS3-only, 6 KS4-Combined, 2 KS4-Triple)
--                10Z's 5 students = 3 reused from 10A + 2 new
--   1 subjects row "Science" (KS3 sciences are not split per AQA — adding
--                this row lets KS3 class_teachers and assignments satisfy
--                the existing schema constraints without DDL changes)
--   7 class_teachers rows
--   16 class_members rows (5 + 6 + 5)
--   20 assignments        (4 + 12 + 4)
--   65 assignment_submissions
--      8X1 ~70%  (14/20)
--      10A ~50%  (36/72)
--      10Z ~75%  (15/20)
--
-- ── Expected dashboard view per teacher (MRB-20 verification) ────
--   Sign in as Sarah → 1 card  (10X1 Biology — pre-existing)
--   Sign in as Mide  → 3 cards (8X1, 10A, 10Z Physics)
--   Sign in as J     → 2 cards (8X1, 10A)
--
-- ── Why the "Science" row ────────────────────────────────────────
-- KS3 in real schools is a single subject called "Science" (split
-- happens at KS4). The schema enforces non-NULL subject_id on every
-- 'subject_teacher' row (class_teachers_subject_required_check) and
-- on every assignment. Adding a "Science" subject row lets the data
-- model reflect reality without DDL or constraint changes. The
-- MRB-20 dashboard pill is derived from key_stage, so the user-
-- visible label stays "Science" regardless of how the data tags it.
-- display_order=0 places it before Biology/Chemistry/Physics in any
-- alphabetical-by-display_order list.
--
-- ── auth.users gold-standard pattern (lessons from MRB-37) ───────
-- Every auth.users row inserted below sets ALL of:
--   encrypted_password = crypt('TestPass!2026', gen_salt('bf', 10))
--   raw_app_meta_data  = '{"provider":"email","providers":["email"]}'
--   confirmation_token         = ''   } seven text columns that
--   recovery_token             = ''   } GoTrue's User struct
--   email_change_token_new     = ''   } types as non-nullable Go
--   email_change_token_current = ''   } strings — leaving any of
--   email_change               = ''   } them NULL crashes signin
--   phone_change_token         = ''   } with "Database error
--   reauthentication_token     = ''   } querying schema"
-- 0002 missed all of these and required hotfixes 0003/0004/0005 to
-- restore signin. This migration bakes them in from the start.
--
-- ── Idempotency ──────────────────────────────────────────────────
-- Every INSERT uses a deterministic UUID + ON CONFLICT (id) DO
-- NOTHING. Re-running this file produces the same data and never
-- mutates rows it has already inserted.
--
-- ── UUID convention (extends 0002's xN…) ─────────────────────────
--   26000000-0000-0000-0000-000000000001 → "Science" subjects row
--   28000000-0000-0000-0000-000000000001 → Mide Badmus     (teacher)
--   28000000-0000-0000-0000-000000000002 → J Okonkwo       (teacher)
--   29000000-0000-0000-0000-000000000001..0005 → 5 KS3 students (8X1)
--   29000000-0000-0000-0000-000000000006..000B → 6 KS4 Combined students (10A)
--   29000000-0000-0000-0000-00000000000C..000D → 2 KS4 Triple-only students (10Z)
--   2A000000-0000-0000-0000-000000000001 → class 8X1
--   2A000000-0000-0000-0000-000000000002 → class 10A
--   2A000000-0000-0000-0000-000000000003 → class 10Z Physics
--   2B000000-0000-0000-0000-000000000001..0007 → class_teachers rows
--   2C000000-0000-0000-0000-00000000WWMM → class_members
--                                            WW=class index (01..03)
--                                            MM=member index within class
--   2D000000-0000-0000-0000-00000000WWAA → assignments
--                                            WW=class index, AA=assignment#
--                                            (10A's AA goes 01..0C in hex)
--   2E000000-0000-0000-0000-000000WWAASS → assignment_submissions
--                                            WW=class, AA=assignment, SS=student
-- =====================================================================

BEGIN;

-- =====================================================================
-- 0 — Pre-flight: refuse to run unless 0002 + 0004 + 0005 are in place
-- =====================================================================
-- Sarah's profile existing proves 0002 ran. Her auth.users row having
-- confirmation_token = '' (not NULL) proves 0004 ran. email_change = ''
-- proves 0005 ran. encrypted_password being non-NULL proves 0003 ran.
-- All four gates in one query — fail loud and early if anything is
-- missing rather than producing partial state mid-migration.
-- =====================================================================

DO $$
DECLARE
  v_sarah_profile_exists boolean;
  v_sarah_confirmation   text;
  v_sarah_email_change   text;
  v_sarah_password       text;
BEGIN
  SELECT EXISTS (
    SELECT 1 FROM public.profiles
    WHERE id = '20000000-0000-0000-0000-000000000001'
      AND first_name = 'Sarah'
  ) INTO v_sarah_profile_exists;

  IF NOT v_sarah_profile_exists THEN
    RAISE EXCEPTION '0002_stage2_test_seeds.sql must be applied first: Sarah Whitfield profile (20000000-...-001) not found';
  END IF;

  SELECT confirmation_token, email_change, encrypted_password
  INTO v_sarah_confirmation, v_sarah_email_change, v_sarah_password
  FROM auth.users
  WHERE id = '20000000-0000-0000-0000-000000000001';

  IF v_sarah_password IS NULL OR v_sarah_password = '' THEN
    RAISE EXCEPTION '0003_stage2_test_passwords.sql must be applied first: Sarah has no encrypted_password';
  END IF;

  IF v_sarah_confirmation IS NULL THEN
    RAISE EXCEPTION '0004_stage2_test_seeds_fix_auth_columns.sql must be applied first: Sarah.confirmation_token is NULL';
  END IF;

  IF v_sarah_email_change IS NULL THEN
    RAISE EXCEPTION '0005_stage2_test_seeds_fix_email_change.sql must be applied first: Sarah.email_change is NULL';
  END IF;
END $$;


-- =====================================================================
-- 1 — public.subjects: add the "Science" row for KS3
-- =====================================================================
-- See header comment for rationale. department='Science' matches the
-- existing Bio/Chem/Phys rows. display_order=0 sorts it first.
-- =====================================================================

INSERT INTO public.subjects (id, name, department, display_order, active)
VALUES (
  '26000000-0000-0000-0000-000000000001',
  'Science', 'Science', 0, true
)
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 2 — auth.users (2 teachers + 13 students = 15 rows)
-- =====================================================================
-- GOLD-STANDARD INSERT — every column GoTrue cares about is set
-- explicitly. Easy to verify by scanning the column list:
--   encrypted_password           — bcrypt cost-10 via crypt()
--   raw_app_meta_data            — provider=email shape
--   raw_user_meta_data           — empty jsonb (matches 0002)
--   six text token columns       — all ''
--   email_change                 — ''
-- Without ALL of these set, signin breaks on Scan errors (see header).
-- =====================================================================

INSERT INTO auth.users (
  id, email,
  encrypted_password,
  raw_app_meta_data, raw_user_meta_data,
  aud, role,
  email_confirmed_at, created_at, updated_at, instance_id,
  confirmation_token, recovery_token,
  email_change_token_new, email_change_token_current, email_change,
  phone_change_token, reauthentication_token
) VALUES
  -- ── Teachers ─────────────────────────────────────────────────────
  ('28000000-0000-0000-0000-000000000001', 'mide.badmus@test-rainford.local',
    crypt('TestPass!2026', gen_salt('bf', 10)),
    '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb,
    'authenticated', 'authenticated',
    now(), now(), now(), '00000000-0000-0000-0000-000000000000',
    '', '', '', '', '', '', ''),
  ('28000000-0000-0000-0000-000000000002', 'j.okonkwo@test-rainford.local',
    crypt('TestPass!2026', gen_salt('bf', 10)),
    '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb,
    'authenticated', 'authenticated',
    now(), now(), now(), '00000000-0000-0000-0000-000000000000',
    '', '', '', '', '', '', ''),

  -- ── 8X1 students (KS3 / Y8) ──────────────────────────────────────
  ('29000000-0000-0000-0000-000000000001', 'aiden.cole@test-rainford.local',     crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000002', 'lily.edwards@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000003', 'marcus.bennett@test-rainford.local', crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000004', 'zara.hassan@test-rainford.local',    crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000005', 'tom.wright@test-rainford.local',     crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),

  -- ── 10A students (KS4 / Y10 / Higher / Combined) ─────────────────
  ('29000000-0000-0000-0000-000000000006', 'hannah.patel@test-rainford.local',  crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000007', 'joel.murphy@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000008', 'naomi.silva@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000009', 'daniel.park@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-00000000000a', 'olivia.chen@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-00000000000b', 'ben.khan@test-rainford.local',      crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),

  -- ── 10Z unique students (KS4 / Y10 / Higher / Triple) ────────────
  ('29000000-0000-0000-0000-00000000000c', 'isla.reeves@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-00000000000d', 'connor.walsh@test-rainford.local',  crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', '')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 3 — public.profiles (2 teachers + 13 students)
-- =====================================================================
-- Teachers: role='teacher', key_stage='KS4' (matches Sarah's pattern),
--   tier/pathway NULL.
-- KS3 students: key_stage='KS3', tier/pathway BOTH NULL — required by
--   profiles_tier_only_ks4_check.
-- KS4 Combined students: KS4 / higher / combined.
-- KS4 Triple-only students: KS4 / higher / triple.
-- The 3 students reused between 10A and 10Z take their primary class's
--   pathway (combined) — this is realistic (a kid registered as Combined
--   who happens to attend a Triple-only Physics enrichment session).
-- =====================================================================

INSERT INTO public.profiles (
  id, school_id, role, key_stage, tier, science_pathway,
  first_name, last_name, exam_board
)
SELECT
  v.id, s.id, v.role, v.key_stage, v.tier, v.science_pathway,
  v.first_name, v.last_name, 'AQA'
FROM public.schools s
CROSS JOIN (VALUES
  -- ── Teachers ───────────────────────────────────────────────────
  ('28000000-0000-0000-0000-000000000001'::uuid, 'teacher', 'KS4', NULL,     NULL,        'Mide',   'Badmus'),
  ('28000000-0000-0000-0000-000000000002'::uuid, 'teacher', 'KS4', NULL,     NULL,        'J',      'Okonkwo'),

  -- ── 8X1 students (KS3 — tier/pathway MUST be NULL) ─────────────
  ('29000000-0000-0000-0000-000000000001'::uuid, 'student', 'KS3', NULL,     NULL,        'Aiden',  'Cole'),
  ('29000000-0000-0000-0000-000000000002'::uuid, 'student', 'KS3', NULL,     NULL,        'Lily',   'Edwards'),
  ('29000000-0000-0000-0000-000000000003'::uuid, 'student', 'KS3', NULL,     NULL,        'Marcus', 'Bennett'),
  ('29000000-0000-0000-0000-000000000004'::uuid, 'student', 'KS3', NULL,     NULL,        'Zara',   'Hassan'),
  ('29000000-0000-0000-0000-000000000005'::uuid, 'student', 'KS3', NULL,     NULL,        'Tom',    'Wright'),

  -- ── 10A students (KS4 / Higher / Combined) ────────────────────
  ('29000000-0000-0000-0000-000000000006'::uuid, 'student', 'KS4', 'higher', 'combined',  'Hannah', 'Patel'),
  ('29000000-0000-0000-0000-000000000007'::uuid, 'student', 'KS4', 'higher', 'combined',  'Joel',   'Murphy'),
  ('29000000-0000-0000-0000-000000000008'::uuid, 'student', 'KS4', 'higher', 'combined',  'Naomi',  'Silva'),
  ('29000000-0000-0000-0000-000000000009'::uuid, 'student', 'KS4', 'higher', 'combined',  'Daniel', 'Park'),
  ('29000000-0000-0000-0000-00000000000a'::uuid, 'student', 'KS4', 'higher', 'combined',  'Olivia', 'Chen'),
  ('29000000-0000-0000-0000-00000000000b'::uuid, 'student', 'KS4', 'higher', 'combined',  'Ben',    'Khan'),

  -- ── 10Z unique students (KS4 / Higher / Triple) ───────────────
  ('29000000-0000-0000-0000-00000000000c'::uuid, 'student', 'KS4', 'higher', 'triple',    'Isla',   'Reeves'),
  ('29000000-0000-0000-0000-00000000000d'::uuid, 'student', 'KS4', 'higher', 'triple',    'Connor', 'Walsh')
) AS v(id, role, key_stage, tier, science_pathway, first_name, last_name)
WHERE s.slug = 'rainford-high'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 4 — public.classes (3 new classes)
-- =====================================================================
-- 8X1: KS3, no tier or pathway (constraint: tier+pathway must both be
--      NULL unless KS4).
-- 10A: KS4 / Higher / Combined.
-- 10Z Physics: KS4 / Higher / Triple.
-- All bound to Rainford + the 2025-26 academic year.
-- =====================================================================

INSERT INTO public.classes (
  id, school_id, academic_year_id, name,
  key_stage, year_group, tier, science_pathway
)
SELECT
  v.id, s.id, ay.id, v.name,
  v.key_stage, v.year_group, v.tier, v.science_pathway
FROM public.schools s
JOIN public.academic_years ay ON ay.school_id = s.id AND ay.name = '2025-26'
CROSS JOIN (VALUES
  ('2a000000-0000-0000-0000-000000000001'::uuid, '8X1',          'KS3', 8::smallint,  NULL::text,     NULL::text),
  ('2a000000-0000-0000-0000-000000000002'::uuid, '10A',          'KS4', 10::smallint, 'higher'::text, 'combined'::text),
  ('2a000000-0000-0000-0000-000000000003'::uuid, '10Z Physics',  'KS4', 10::smallint, 'higher'::text, 'triple'::text)
) AS v(id, name, key_stage, year_group, tier, science_pathway)
WHERE s.slug = 'rainford-high'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 5 — public.class_teachers (7 rows)
-- =====================================================================
-- All seven rows use role='subject_teacher' which requires non-NULL
-- subject_id per class_teachers_subject_required_check.
--
--   8X1   — 2 rows: Mide + J, both teaching Science
--   10A   — 4 rows: Mide(Phys), Mide(Chem), J(Bio), J(Chem)
--   10Z   — 1 row : Mide teaching Physics
--
-- Subject lookups by name keep this portable; "Science" uses its
-- deterministic UUID since this migration created it.
-- =====================================================================

-- 5a — 8X1 (Science) — both teachers
INSERT INTO public.class_teachers (id, class_id, teacher_id, subject_id, role)
VALUES
  ('2b000000-0000-0000-0000-000000000001',
   '2a000000-0000-0000-0000-000000000001',
   '28000000-0000-0000-0000-000000000001',
   '26000000-0000-0000-0000-000000000001',
   'subject_teacher'),
  ('2b000000-0000-0000-0000-000000000002',
   '2a000000-0000-0000-0000-000000000001',
   '28000000-0000-0000-0000-000000000002',
   '26000000-0000-0000-0000-000000000001',
   'subject_teacher')
ON CONFLICT (id) DO NOTHING;

-- 5b — 10A (Bio + Chem + Phys split between Mide and J)
INSERT INTO public.class_teachers (id, class_id, teacher_id, subject_id, role)
SELECT
  v.id,
  '2a000000-0000-0000-0000-000000000002'::uuid,
  v.teacher_id,
  s.id,
  'subject_teacher'
FROM public.subjects s
CROSS JOIN (VALUES
  ('2b000000-0000-0000-0000-000000000003'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Physics'),    -- Mide → Phys
  ('2b000000-0000-0000-0000-000000000004'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Chemistry'),  -- Mide → Chem
  ('2b000000-0000-0000-0000-000000000005'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Biology'),    -- J    → Bio
  ('2b000000-0000-0000-0000-000000000006'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Chemistry')   -- J    → Chem
) AS v(id, teacher_id, subject_name)
WHERE s.name = v.subject_name
ON CONFLICT (id) DO NOTHING;

-- 5c — 10Z Physics (Mide only)
INSERT INTO public.class_teachers (id, class_id, teacher_id, subject_id, role)
SELECT
  '2b000000-0000-0000-0000-000000000007'::uuid,
  '2a000000-0000-0000-0000-000000000003'::uuid,
  '28000000-0000-0000-0000-000000000001'::uuid,
  s.id,
  'subject_teacher'
FROM public.subjects s
WHERE s.name = 'Physics'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 6 — public.class_members (16 rows: 5 + 6 + 5)
-- =====================================================================
-- 10Z's 5 members = 3 reused from 10A (Hannah, Joel, Naomi) +
--                   2 unique new students (Isla, Connor)
-- joined_via='admin_added' for all (typical for fixture data).
--
-- ID encoding: 2C…00WWMM where WW=class index (01..03), MM=member-
-- within-class (01..06). Member ordering is preserved across submissions
-- below (e.g. 10Z student #4 = Isla, used in 2E…0304XX submission IDs).
-- =====================================================================

INSERT INTO public.class_members (id, class_id, student_id, joined_via)
VALUES
  -- 8X1 (5 students)
  ('2c000000-0000-0000-0000-000000000101', '2a000000-0000-0000-0000-000000000001', '29000000-0000-0000-0000-000000000001', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000102', '2a000000-0000-0000-0000-000000000001', '29000000-0000-0000-0000-000000000002', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000103', '2a000000-0000-0000-0000-000000000001', '29000000-0000-0000-0000-000000000003', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000104', '2a000000-0000-0000-0000-000000000001', '29000000-0000-0000-0000-000000000004', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000105', '2a000000-0000-0000-0000-000000000001', '29000000-0000-0000-0000-000000000005', 'admin_added'),

  -- 10A (6 students)
  ('2c000000-0000-0000-0000-000000000201', '2a000000-0000-0000-0000-000000000002', '29000000-0000-0000-0000-000000000006', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000202', '2a000000-0000-0000-0000-000000000002', '29000000-0000-0000-0000-000000000007', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000203', '2a000000-0000-0000-0000-000000000002', '29000000-0000-0000-0000-000000000008', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000204', '2a000000-0000-0000-0000-000000000002', '29000000-0000-0000-0000-000000000009', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000205', '2a000000-0000-0000-0000-000000000002', '29000000-0000-0000-0000-00000000000a', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000206', '2a000000-0000-0000-0000-000000000002', '29000000-0000-0000-0000-00000000000b', 'admin_added'),

  -- 10Z Physics (5 students = 3 from 10A + 2 unique)
  ('2c000000-0000-0000-0000-000000000301', '2a000000-0000-0000-0000-000000000003', '29000000-0000-0000-0000-000000000006', 'admin_added'),  -- Hannah (also 10A)
  ('2c000000-0000-0000-0000-000000000302', '2a000000-0000-0000-0000-000000000003', '29000000-0000-0000-0000-000000000007', 'admin_added'),  -- Joel   (also 10A)
  ('2c000000-0000-0000-0000-000000000303', '2a000000-0000-0000-0000-000000000003', '29000000-0000-0000-0000-000000000008', 'admin_added'),  -- Naomi  (also 10A)
  ('2c000000-0000-0000-0000-000000000304', '2a000000-0000-0000-0000-000000000003', '29000000-0000-0000-0000-00000000000c', 'admin_added'),  -- Isla   (10Z only)
  ('2c000000-0000-0000-0000-000000000305', '2a000000-0000-0000-0000-000000000003', '29000000-0000-0000-0000-00000000000d', 'admin_added')   -- Connor (10Z only)
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 7 — public.assignments (20 rows: 4 + 12 + 4)
-- =====================================================================
-- All weekly across the past 4 weeks. due_at anchored to now() so the
-- file ages gracefully. created_at = due_at - 7 days (audit-friendly:
-- looks like work spread across a month, not all at once).
-- =====================================================================

-- 7a — 8X1: 4 weekly Science assignments (Mide and J share ownership)
INSERT INTO public.assignments (
  id, class_id, teacher_id, subject_id,
  topic, subtopic, title, instructions,
  quiz_type, due_at, created_at, updated_at, auto_generated
) VALUES
  ('2d000000-0000-0000-0000-000000000101',
   '2a000000-0000-0000-0000-000000000001',
   '28000000-0000-0000-0000-000000000002', -- J
   '26000000-0000-0000-0000-000000000001', -- Science
   'Cells',     'Cell structure',
   'Science Quiz — Cells (Wk 1)',
   '10 questions on plant and animal cell parts and their jobs.',
   'topic_quiz', now() - interval '21 days', now() - interval '28 days', now() - interval '28 days', false),
  ('2d000000-0000-0000-0000-000000000102',
   '2a000000-0000-0000-0000-000000000001',
   '28000000-0000-0000-0000-000000000001', -- Mide
   '26000000-0000-0000-0000-000000000001',
   'Forces',    'Contact and non-contact forces',
   'Science Quiz — Forces (Wk 2)',
   '10 questions on push, pull, gravity, friction.',
   'topic_quiz', now() - interval '14 days', now() - interval '21 days', now() - interval '21 days', false),
  ('2d000000-0000-0000-0000-000000000103',
   '2a000000-0000-0000-0000-000000000001',
   '28000000-0000-0000-0000-000000000001', -- Mide
   '26000000-0000-0000-0000-000000000001',
   'Particles', 'States of matter',
   'Science Quiz — Particles (Wk 3)',
   '10 questions on solids, liquids, gases, and changes of state.',
   'topic_quiz', now() - interval '7 days',  now() - interval '14 days', now() - interval '14 days', false),
  ('2d000000-0000-0000-0000-000000000104',
   '2a000000-0000-0000-0000-000000000001',
   '28000000-0000-0000-0000-000000000002', -- J
   '26000000-0000-0000-0000-000000000001',
   'Reactions', 'Chemical vs physical change',
   'Science Quiz — Reactions (Wk 4)',
   '10 questions on identifying chemical reactions vs physical changes.',
   'topic_quiz', now(),                     now() - interval '7 days',  now() - interval '7 days',  false)
ON CONFLICT (id) DO NOTHING;

-- 7b — 10A: 12 assignments (4 weeks × 3 subjects). Bio→J, Phys→Mide,
--      Chem alternates Mide/J across weeks.
INSERT INTO public.assignments (
  id, class_id, teacher_id, subject_id,
  topic, subtopic, title, instructions,
  quiz_type, due_at, created_at, updated_at, auto_generated
)
SELECT
  v.id,
  '2a000000-0000-0000-0000-000000000002'::uuid,
  v.teacher_id,
  s.id,
  v.topic, v.subtopic, v.title, v.instructions,
  'topic_quiz', v.due_at, v.due_at - interval '7 days', v.due_at - interval '7 days', false
FROM public.subjects s
CROSS JOIN (VALUES
  -- Biology (J owns all four)
  ('2d000000-0000-0000-0000-000000000201'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Biology',
    'Cell Biology', 'Cell transport',          'Bio Quiz — Cell Transport (Wk 1)',
    '10 questions on diffusion, osmosis and active transport.',
    now() - interval '21 days'),
  ('2d000000-0000-0000-0000-000000000202'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Biology',
    'Bioenergetics', 'Photosynthesis',         'Bio Quiz — Photosynthesis (Wk 2)',
    '10 questions on photosynthesis and limiting factors.',
    now() - interval '14 days'),
  ('2d000000-0000-0000-0000-000000000203'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Biology',
    'Infection and response', 'Pathogens',     'Bio Quiz — Communicable Diseases (Wk 3)',
    '10 questions on viral, bacterial and fungal pathogens.',
    now() - interval '7 days'),
  ('2d000000-0000-0000-0000-000000000204'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Biology',
    'Homeostasis', 'Hormonal coordination',    'Bio Quiz — Hormonal Coordination (Wk 4)',
    '10 questions on the endocrine system and blood glucose regulation.',
    now()),

  -- Chemistry (Mide and J alternate weeks)
  ('2d000000-0000-0000-0000-000000000205'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Chemistry',
    'Atomic structure', 'Atoms and elements',  'Chem Quiz — Atomic Structure (Wk 1)',
    '10 questions on protons, neutrons, electrons and isotopes.',
    now() - interval '21 days'),
  ('2d000000-0000-0000-0000-000000000206'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Chemistry',
    'Bonding', 'Ionic and covalent bonding',   'Chem Quiz — Bonding (Wk 2)',
    '10 questions on ionic, covalent and metallic bonding.',
    now() - interval '14 days'),
  ('2d000000-0000-0000-0000-000000000207'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Chemistry',
    'Quantitative chemistry', 'Moles',         'Chem Quiz — Quantitative (Wk 3)',
    '10 questions on relative formula mass, moles, and concentrations.',
    now() - interval '7 days'),
  ('2d000000-0000-0000-0000-000000000208'::uuid, '28000000-0000-0000-0000-000000000002'::uuid, 'Chemistry',
    'Energy changes', 'Exothermic / endothermic', 'Chem Quiz — Energy Changes (Wk 4)',
    '10 questions on energy changes during reactions.',
    now()),

  -- Physics (Mide owns all four)
  ('2d000000-0000-0000-0000-000000000209'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Physics',
    'Energy', 'Energy stores and transfers',   'Phys Quiz — Energy Stores (Wk 1)',
    '10 questions on kinetic, potential, thermal energy and transfers.',
    now() - interval '21 days'),
  ('2d000000-0000-0000-0000-00000000020a'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Physics',
    'Electricity', 'Series and parallel circuits', 'Phys Quiz — Electricity (Wk 2)',
    '10 questions on current, voltage, resistance in circuits.',
    now() - interval '14 days'),
  ('2d000000-0000-0000-0000-00000000020b'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Physics',
    'Particle model', 'Density and changes of state', 'Phys Quiz — Particle Model (Wk 3)',
    '10 questions on density, internal energy and specific heat capacity.',
    now() - interval '7 days'),
  ('2d000000-0000-0000-0000-00000000020c'::uuid, '28000000-0000-0000-0000-000000000001'::uuid, 'Physics',
    'Atomic structure', 'Radioactive decay',   'Phys Quiz — Atomic Structure (Wk 4)',
    '10 questions on alpha, beta and gamma radiation and half-life.',
    now())
) AS v(id, teacher_id, subject_name, topic, subtopic, title, instructions, due_at)
WHERE s.name = v.subject_name
ON CONFLICT (id) DO NOTHING;

-- 7c — 10Z Physics: 4 weekly assignments, all Mide
INSERT INTO public.assignments (
  id, class_id, teacher_id, subject_id,
  topic, subtopic, title, instructions,
  quiz_type, due_at, created_at, updated_at, auto_generated
)
SELECT
  v.id,
  '2a000000-0000-0000-0000-000000000003'::uuid,
  '28000000-0000-0000-0000-000000000001'::uuid,
  s.id,
  v.topic, v.subtopic, v.title, v.instructions,
  'topic_quiz', v.due_at, v.due_at - interval '7 days', v.due_at - interval '7 days', false
FROM public.subjects s
CROSS JOIN (VALUES
  ('2d000000-0000-0000-0000-000000000301'::uuid,
    'Forces', 'Forces and motion',           'Triple Phys Quiz — Forces & Motion (Wk 1)',
    '10 questions on Newton''s laws, momentum and forces in equilibrium.',
    now() - interval '21 days'),
  ('2d000000-0000-0000-0000-000000000302'::uuid,
    'Magnetism', 'Electromagnetism',         'Triple Phys Quiz — Magnetism (Wk 2)',
    '10 questions on magnetic fields, motors and transformers.',
    now() - interval '14 days'),
  ('2d000000-0000-0000-0000-000000000303'::uuid,
    'Space physics', 'Solar system and orbits', 'Triple Phys Quiz — Space (Wk 3)',
    '10 questions on solar system structure, life cycle of stars, red shift.',
    now() - interval '7 days'),
  ('2d000000-0000-0000-0000-000000000304'::uuid,
    'Waves', 'Properties of waves',          'Triple Phys Quiz — Waves (Wk 4)',
    '10 questions on transverse / longitudinal waves and the EM spectrum.',
    now())
) AS v(id, topic, subtopic, title, instructions, due_at)
WHERE s.name = 'Physics'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 8 — public.assignment_submissions (65 rows: 14 + 36 + 15)
-- =====================================================================
-- ID encoding: 2E…000000WWAASS where
--   WW = class index   (01=8X1, 02=10A, 03=10Z)
--   AA = assignment#   (within the class — 10A's run 01..0C in hex)
--   SS = student#      (member-within-class index, see section 6)
--
-- Score / time conventions:
--   * max_score = 10 throughout
--   * score and total_time_seconds inversely correlated — strong
--     students answer faster and score higher
--   * attempts = 1 except where noted (Daniel Chem Wk2 = 2 attempts)
--
-- Punctuality:
--   * "on-time"  → submitted_at ≤ due_at
--   * "late"     → submitted_at  > due_at  (i.e. timestamp closer to now)
--
-- Per-class summary baked into the data below:
--
--   ┌──── 8X1 (5 students × 4 = 20; submitted 14 = ~70%) ─────────────┐
--   │ Aiden  4/4  90%  fully on-time   (top 8X1 contender)             │
--   │ Lily   4/4  80%  3 on-time, 1 late                               │
--   │ Marcus 3/4  60%  1 on-time, 2 late                               │
--   │ Zara   2/4  55%  1 on-time, 1 late                               │
--   │ Tom    1/4  50%  1 on-time                                       │
--   │ → MRB-38 8X1 leaderboard eligibles (all-completed): only Aiden,  │
--   │   Lily.  Aiden 1st (4 on-time), Lily 2nd (3 on-time).            │
--   └──────────────────────────────────────────────────────────────────┘
--
--   ┌──── 10A (6 students × 12 = 72; submitted 36 = ~50%) ────────────┐
--   │ Hannah 12/12  ~84%  fully on-time   (perfect attender)           │
--   │ Joel    9/12  ~73%  mix on-time/late                             │
--   │ Naomi   6/12  ~58%  mix                                          │
--   │ Daniel  5/12  ~50%  three lates incl. one 2-attempt              │
--   │ Olivia  3/12  ~47%  on-time but only Bio/Chem first half         │
--   │ Ben     1/12  ~40%  one Bio Wk1 late                             │
--   │ → 10A leaderboard eligibles: only Hannah (no other student       │
--   │   submitted all 12). Mide-vs-J RLS check still works on this set.│
--   └──────────────────────────────────────────────────────────────────┘
--
--   ┌──── 10Z (5 students × 4 = 20; submitted 15 = ~75%) ─────────────┐
--   │ Hannah 4/4  95%  4 on-time   → 1st  (rank by on-time, then %)   │
--   │ Joel   4/4  85%  4 on-time   → 2nd                              │
--   │ Isla   4/4 100%  3 on-time + 1 late (Wk3) → 3rd (DESPITE 100%) │
--   │ Connor 2/4  75%  ineligible (incomplete)                         │
--   │ Naomi  1/4  60%  ineligible                                      │
--   │ → MRB-38 verification: Isla 100% but ranks below Joel 85%        │
--   │   because Isla missed a deadline. Proves the on-time-DESC        │
--   │   primary sort works.                                            │
--   └──────────────────────────────────────────────────────────────────┘
-- =====================================================================

INSERT INTO public.assignment_submissions (
  id, assignment_id, student_id,
  score, max_score, total_time_seconds, submitted_at, attempts,
  created_at, updated_at
) VALUES
  -- ════════════════════════════════════════════════════════════════
  -- 8X1 — 14 submissions
  -- ════════════════════════════════════════════════════════════════
  -- Wk 1 (due now-21d) — 5/5 (all)
  ('2e000000-0000-0000-0000-000000010101', '2d000000-0000-0000-0000-000000000101', '29000000-0000-0000-0000-000000000001',  9, 10, 320, now() - interval '21 days 18 hours', 1, now() - interval '21 days 18 hours', now() - interval '21 days 18 hours'),  -- Aiden  on-time
  ('2e000000-0000-0000-0000-000000010102', '2d000000-0000-0000-0000-000000000101', '29000000-0000-0000-0000-000000000002',  8, 10, 280, now() - interval '21 days 14 hours', 1, now() - interval '21 days 14 hours', now() - interval '21 days 14 hours'),  -- Lily   on-time
  ('2e000000-0000-0000-0000-000000010103', '2d000000-0000-0000-0000-000000000101', '29000000-0000-0000-0000-000000000003',  6, 10, 380, now() - interval '21 days 8 hours',  1, now() - interval '21 days 8 hours',  now() - interval '21 days 8 hours'),   -- Marcus on-time
  ('2e000000-0000-0000-0000-000000010104', '2d000000-0000-0000-0000-000000000101', '29000000-0000-0000-0000-000000000004',  4, 10, 480, now() - interval '21 days 4 hours',  1, now() - interval '21 days 4 hours',  now() - interval '21 days 4 hours'),   -- Zara   on-time
  ('2e000000-0000-0000-0000-000000010105', '2d000000-0000-0000-0000-000000000101', '29000000-0000-0000-0000-000000000005',  5, 10, 520, now() - interval '21 days 2 hours',  1, now() - interval '21 days 2 hours',  now() - interval '21 days 2 hours'),   -- Tom    on-time

  -- Wk 2 (due now-14d) — 3/5 (Aiden, Lily, Marcus)
  ('2e000000-0000-0000-0000-000000010201', '2d000000-0000-0000-0000-000000000102', '29000000-0000-0000-0000-000000000001', 10, 10, 280, now() - interval '14 days 16 hours', 1, now() - interval '14 days 16 hours', now() - interval '14 days 16 hours'),  -- Aiden  on-time
  ('2e000000-0000-0000-0000-000000010202', '2d000000-0000-0000-0000-000000000102', '29000000-0000-0000-0000-000000000002',  7, 10, 320, now() - interval '14 days 12 hours', 1, now() - interval '14 days 12 hours', now() - interval '14 days 12 hours'),  -- Lily   on-time
  ('2e000000-0000-0000-0000-000000010203', '2d000000-0000-0000-0000-000000000102', '29000000-0000-0000-0000-000000000003',  5, 10, 420, now() - interval '13 days 18 hours', 1, now() - interval '13 days 18 hours', now() - interval '13 days 18 hours'),  -- Marcus LATE

  -- Wk 3 (due now-7d) — 4/5 (Aiden, Lily, Marcus, Zara)
  ('2e000000-0000-0000-0000-000000010301', '2d000000-0000-0000-0000-000000000103', '29000000-0000-0000-0000-000000000001',  8, 10, 300, now() - interval '7 days 8 hours',   1, now() - interval '7 days 8 hours',   now() - interval '7 days 8 hours'),    -- Aiden  on-time
  ('2e000000-0000-0000-0000-000000010302', '2d000000-0000-0000-0000-000000000103', '29000000-0000-0000-0000-000000000002',  9, 10, 260, now() - interval '7 days 6 hours',   1, now() - interval '7 days 6 hours',   now() - interval '7 days 6 hours'),    -- Lily   on-time
  ('2e000000-0000-0000-0000-000000010303', '2d000000-0000-0000-0000-000000000103', '29000000-0000-0000-0000-000000000003',  7, 10, 360, now() - interval '6 days 18 hours',  1, now() - interval '6 days 18 hours',  now() - interval '6 days 18 hours'),   -- Marcus LATE
  ('2e000000-0000-0000-0000-000000010304', '2d000000-0000-0000-0000-000000000103', '29000000-0000-0000-0000-000000000004',  7, 10, 400, now() - interval '5 days 12 hours',  1, now() - interval '5 days 12 hours',  now() - interval '5 days 12 hours'),   -- Zara   LATE

  -- Wk 4 (due now) — 2/5 (Aiden, Lily)
  ('2e000000-0000-0000-0000-000000010401', '2d000000-0000-0000-0000-000000000104', '29000000-0000-0000-0000-000000000001',  9, 10, 290, now() - interval '2 hours',          1, now() - interval '2 hours',          now() - interval '2 hours'),           -- Aiden  on-time
  ('2e000000-0000-0000-0000-000000010402', '2d000000-0000-0000-0000-000000000104', '29000000-0000-0000-0000-000000000002',  8, 10, 320, now() - interval '1 hour',           1, now() - interval '1 hour',           now() - interval '1 hour'),            -- Lily   on-time

  -- ════════════════════════════════════════════════════════════════
  -- 10A — 36 submissions (Bio→01..04, Chem→05..08, Phys→09..0c)
  -- ════════════════════════════════════════════════════════════════
  -- Bio Wk1 (due now-21d) — 6/6 (all)
  ('2e000000-0000-0000-0000-000000020101', '2d000000-0000-0000-0000-000000000201', '29000000-0000-0000-0000-000000000006',  9, 10, 220, now() - interval '21 days 8 hours',  1, now() - interval '21 days 8 hours',  now() - interval '21 days 8 hours'),   -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020102', '2d000000-0000-0000-0000-000000000201', '29000000-0000-0000-0000-000000000007',  8, 10, 280, now() - interval '21 days 6 hours',  1, now() - interval '21 days 6 hours',  now() - interval '21 days 6 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000020103', '2d000000-0000-0000-0000-000000000201', '29000000-0000-0000-0000-000000000008',  7, 10, 350, now() - interval '21 days 4 hours',  1, now() - interval '21 days 4 hours',  now() - interval '21 days 4 hours'),   -- Naomi  on-time
  ('2e000000-0000-0000-0000-000000020104', '2d000000-0000-0000-0000-000000000201', '29000000-0000-0000-0000-000000000009',  6, 10, 400, now() - interval '20 days 18 hours', 1, now() - interval '20 days 18 hours', now() - interval '20 days 18 hours'),  -- Daniel LATE
  ('2e000000-0000-0000-0000-000000020105', '2d000000-0000-0000-0000-000000000201', '29000000-0000-0000-0000-00000000000a',  5, 10, 450, now() - interval '21 days 2 hours',  1, now() - interval '21 days 2 hours',  now() - interval '21 days 2 hours'),   -- Olivia on-time
  ('2e000000-0000-0000-0000-000000020106', '2d000000-0000-0000-0000-000000000201', '29000000-0000-0000-0000-00000000000b',  4, 10, 550, now() - interval '20 days 10 hours', 1, now() - interval '20 days 10 hours', now() - interval '20 days 10 hours'),  -- Ben    LATE

  -- Bio Wk2 (due now-14d) — 5/6 (no Ben)
  ('2e000000-0000-0000-0000-000000020201', '2d000000-0000-0000-0000-000000000202', '29000000-0000-0000-0000-000000000006', 10, 10, 200, now() - interval '14 days 10 hours', 1, now() - interval '14 days 10 hours', now() - interval '14 days 10 hours'),  -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020202', '2d000000-0000-0000-0000-000000000202', '29000000-0000-0000-0000-000000000007',  8, 10, 280, now() - interval '14 days 6 hours',  1, now() - interval '14 days 6 hours',  now() - interval '14 days 6 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000020203', '2d000000-0000-0000-0000-000000000202', '29000000-0000-0000-0000-000000000008',  7, 10, 380, now() - interval '13 days 18 hours', 1, now() - interval '13 days 18 hours', now() - interval '13 days 18 hours'),  -- Naomi  LATE
  ('2e000000-0000-0000-0000-000000020204', '2d000000-0000-0000-0000-000000000202', '29000000-0000-0000-0000-000000000009',  6, 10, 420, now() - interval '14 days 1 hour',   1, now() - interval '14 days 1 hour',   now() - interval '14 days 1 hour'),    -- Daniel on-time
  ('2e000000-0000-0000-0000-000000020205', '2d000000-0000-0000-0000-000000000202', '29000000-0000-0000-0000-00000000000a',  5, 10, 480, now() - interval '14 days 1 hour',   1, now() - interval '14 days 1 hour',   now() - interval '14 days 1 hour'),    -- Olivia on-time

  -- Bio Wk3 (due now-7d) — 3/6 (Hannah, Joel, Naomi)
  ('2e000000-0000-0000-0000-000000020301', '2d000000-0000-0000-0000-000000000203', '29000000-0000-0000-0000-000000000006',  9, 10, 240, now() - interval '7 days 8 hours',   1, now() - interval '7 days 8 hours',   now() - interval '7 days 8 hours'),    -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020302', '2d000000-0000-0000-0000-000000000203', '29000000-0000-0000-0000-000000000007',  7, 10, 320, now() - interval '6 days 12 hours',  1, now() - interval '6 days 12 hours',  now() - interval '6 days 12 hours'),   -- Joel   LATE
  ('2e000000-0000-0000-0000-000000020303', '2d000000-0000-0000-0000-000000000203', '29000000-0000-0000-0000-000000000008',  6, 10, 400, now() - interval '7 days 1 hour',    1, now() - interval '7 days 1 hour',    now() - interval '7 days 1 hour'),     -- Naomi  on-time

  -- Bio Wk4 (due now) — 2/6 (Hannah, Joel)
  ('2e000000-0000-0000-0000-000000020401', '2d000000-0000-0000-0000-000000000204', '29000000-0000-0000-0000-000000000006',  9, 10, 220, now() - interval '1 hour',           1, now() - interval '1 hour',           now() - interval '1 hour'),            -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020402', '2d000000-0000-0000-0000-000000000204', '29000000-0000-0000-0000-000000000007',  8, 10, 290, now() - interval '2 hours',          1, now() - interval '2 hours',          now() - interval '2 hours'),           -- Joel   on-time

  -- Chem Wk1 (due now-21d) — 5/6 (no Ben)
  ('2e000000-0000-0000-0000-000000020501', '2d000000-0000-0000-0000-000000000205', '29000000-0000-0000-0000-000000000006',  8, 10, 260, now() - interval '21 days 8 hours',  1, now() - interval '21 days 8 hours',  now() - interval '21 days 8 hours'),   -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020502', '2d000000-0000-0000-0000-000000000205', '29000000-0000-0000-0000-000000000007',  7, 10, 320, now() - interval '21 days 4 hours',  1, now() - interval '21 days 4 hours',  now() - interval '21 days 4 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000020503', '2d000000-0000-0000-0000-000000000205', '29000000-0000-0000-0000-000000000008',  6, 10, 400, now() - interval '21 days 2 hours',  1, now() - interval '21 days 2 hours',  now() - interval '21 days 2 hours'),   -- Naomi  on-time
  ('2e000000-0000-0000-0000-000000020504', '2d000000-0000-0000-0000-000000000205', '29000000-0000-0000-0000-000000000009',  5, 10, 480, now() - interval '20 days 12 hours', 1, now() - interval '20 days 12 hours', now() - interval '20 days 12 hours'),  -- Daniel LATE
  ('2e000000-0000-0000-0000-000000020505', '2d000000-0000-0000-0000-000000000205', '29000000-0000-0000-0000-00000000000a',  4, 10, 520, now() - interval '21 days 1 hour',   1, now() - interval '21 days 1 hour',   now() - interval '21 days 1 hour'),    -- Olivia on-time

  -- Chem Wk2 (due now-14d) — 3/6 (Hannah, Joel, Daniel)
  ('2e000000-0000-0000-0000-000000020601', '2d000000-0000-0000-0000-000000000206', '29000000-0000-0000-0000-000000000006',  9, 10, 240, now() - interval '14 days 6 hours',  1, now() - interval '14 days 6 hours',  now() - interval '14 days 6 hours'),   -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020602', '2d000000-0000-0000-0000-000000000206', '29000000-0000-0000-0000-000000000007',  7, 10, 340, now() - interval '14 days 3 hours',  1, now() - interval '14 days 3 hours',  now() - interval '14 days 3 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000020604', '2d000000-0000-0000-0000-000000000206', '29000000-0000-0000-0000-000000000009',  4, 10, 500, now() - interval '13 days 18 hours', 2, now() - interval '13 days 18 hours', now() - interval '13 days 18 hours'),  -- Daniel LATE, 2 attempts

  -- Chem Wk3 (due now-7d) — 2/6 (Hannah, Joel)
  ('2e000000-0000-0000-0000-000000020701', '2d000000-0000-0000-0000-000000000207', '29000000-0000-0000-0000-000000000006',  8, 10, 250, now() - interval '7 days 8 hours',   1, now() - interval '7 days 8 hours',   now() - interval '7 days 8 hours'),    -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020702', '2d000000-0000-0000-0000-000000000207', '29000000-0000-0000-0000-000000000007',  8, 10, 300, now() - interval '7 days 4 hours',   1, now() - interval '7 days 4 hours',   now() - interval '7 days 4 hours'),    -- Joel   on-time

  -- Chem Wk4 (due now) — 2/6 (Hannah, Naomi)
  ('2e000000-0000-0000-0000-000000020801', '2d000000-0000-0000-0000-000000000208', '29000000-0000-0000-0000-000000000006',  9, 10, 220, now() - interval '1 hour',           1, now() - interval '1 hour',           now() - interval '1 hour'),            -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020803', '2d000000-0000-0000-0000-000000000208', '29000000-0000-0000-0000-000000000008',  5, 10, 480, now() - interval '30 minutes',       1, now() - interval '30 minutes',       now() - interval '30 minutes'),        -- Naomi  on-time

  -- Phys Wk1 (due now-21d) — 4/6 (Hannah, Joel, Naomi, Daniel)
  ('2e000000-0000-0000-0000-000000020901', '2d000000-0000-0000-0000-000000000209', '29000000-0000-0000-0000-000000000006',  7, 10, 280, now() - interval '21 days 8 hours',  1, now() - interval '21 days 8 hours',  now() - interval '21 days 8 hours'),   -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020902', '2d000000-0000-0000-0000-000000000209', '29000000-0000-0000-0000-000000000007',  6, 10, 340, now() - interval '21 days 6 hours',  1, now() - interval '21 days 6 hours',  now() - interval '21 days 6 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000020903', '2d000000-0000-0000-0000-000000000209', '29000000-0000-0000-0000-000000000008',  5, 10, 420, now() - interval '21 days 2 hours',  1, now() - interval '21 days 2 hours',  now() - interval '21 days 2 hours'),   -- Naomi  on-time
  ('2e000000-0000-0000-0000-000000020904', '2d000000-0000-0000-0000-000000000209', '29000000-0000-0000-0000-000000000009',  4, 10, 500, now() - interval '20 days 18 hours', 1, now() - interval '20 days 18 hours', now() - interval '20 days 18 hours'),  -- Daniel LATE

  -- Phys Wk2 (due now-14d) — 2/6 (Hannah, Joel)
  ('2e000000-0000-0000-0000-000000020a01', '2d000000-0000-0000-0000-00000000020a', '29000000-0000-0000-0000-000000000006',  8, 10, 260, now() - interval '14 days 8 hours',  1, now() - interval '14 days 8 hours',  now() - interval '14 days 8 hours'),   -- Hannah on-time
  ('2e000000-0000-0000-0000-000000020a02', '2d000000-0000-0000-0000-00000000020a', '29000000-0000-0000-0000-000000000007',  7, 10, 320, now() - interval '14 days 4 hours',  1, now() - interval '14 days 4 hours',  now() - interval '14 days 4 hours'),   -- Joel   on-time

  -- Phys Wk3 (due now-7d) — 1/6 (Hannah only)
  ('2e000000-0000-0000-0000-000000020b01', '2d000000-0000-0000-0000-00000000020b', '29000000-0000-0000-0000-000000000006',  7, 10, 290, now() - interval '7 days 4 hours',   1, now() - interval '7 days 4 hours',   now() - interval '7 days 4 hours'),    -- Hannah on-time

  -- Phys Wk4 (due now) — 1/6 (Hannah only)
  ('2e000000-0000-0000-0000-000000020c01', '2d000000-0000-0000-0000-00000000020c', '29000000-0000-0000-0000-000000000006',  8, 10, 250, now() - interval '1 hour',           1, now() - interval '1 hour',           now() - interval '1 hour'),            -- Hannah on-time

  -- ════════════════════════════════════════════════════════════════
  -- 10Z Physics — 15 submissions
  -- (member#: 01=Hannah, 02=Joel, 03=Naomi, 04=Isla, 05=Connor)
  -- ════════════════════════════════════════════════════════════════
  -- Wk 1 (due now-21d) — 5/5 (all)
  ('2e000000-0000-0000-0000-000000030101', '2d000000-0000-0000-0000-000000000301', '29000000-0000-0000-0000-000000000006',  9, 10, 200, now() - interval '21 days 12 hours', 1, now() - interval '21 days 12 hours', now() - interval '21 days 12 hours'),  -- Hannah on-time
  ('2e000000-0000-0000-0000-000000030102', '2d000000-0000-0000-0000-000000000301', '29000000-0000-0000-0000-000000000007',  8, 10, 250, now() - interval '21 days 8 hours',  1, now() - interval '21 days 8 hours',  now() - interval '21 days 8 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000030103', '2d000000-0000-0000-0000-000000000301', '29000000-0000-0000-0000-000000000008',  6, 10, 410, now() - interval '21 days 4 hours',  1, now() - interval '21 days 4 hours',  now() - interval '21 days 4 hours'),   -- Naomi  on-time
  ('2e000000-0000-0000-0000-000000030104', '2d000000-0000-0000-0000-000000000301', '29000000-0000-0000-0000-00000000000c', 10, 10, 150, now() - interval '21 days 16 hours', 1, now() - interval '21 days 16 hours', now() - interval '21 days 16 hours'),  -- Isla   on-time
  ('2e000000-0000-0000-0000-000000030105', '2d000000-0000-0000-0000-000000000301', '29000000-0000-0000-0000-00000000000d',  7, 10, 400, now() - interval '21 days 2 hours',  1, now() - interval '21 days 2 hours',  now() - interval '21 days 2 hours'),   -- Connor on-time

  -- Wk 2 (due now-14d) — 4/5 (no Naomi)
  ('2e000000-0000-0000-0000-000000030201', '2d000000-0000-0000-0000-000000000302', '29000000-0000-0000-0000-000000000006', 10, 10, 220, now() - interval '14 days 10 hours', 1, now() - interval '14 days 10 hours', now() - interval '14 days 10 hours'),  -- Hannah on-time
  ('2e000000-0000-0000-0000-000000030202', '2d000000-0000-0000-0000-000000000302', '29000000-0000-0000-0000-000000000007',  9, 10, 240, now() - interval '14 days 6 hours',  1, now() - interval '14 days 6 hours',  now() - interval '14 days 6 hours'),   -- Joel   on-time
  ('2e000000-0000-0000-0000-000000030204', '2d000000-0000-0000-0000-000000000302', '29000000-0000-0000-0000-00000000000c', 10, 10, 160, now() - interval '14 days 14 hours', 1, now() - interval '14 days 14 hours', now() - interval '14 days 14 hours'),  -- Isla   on-time
  ('2e000000-0000-0000-0000-000000030205', '2d000000-0000-0000-0000-000000000302', '29000000-0000-0000-0000-00000000000d',  8, 10, 380, now() - interval '14 days 1 hour',   1, now() - interval '14 days 1 hour',   now() - interval '14 days 1 hour'),    -- Connor on-time

  -- Wk 3 (due now-7d) — 3/5 (Hannah, Joel, Isla — Isla LATE)
  ('2e000000-0000-0000-0000-000000030301', '2d000000-0000-0000-0000-000000000303', '29000000-0000-0000-0000-000000000006',  9, 10, 180, now() - interval '7 days 8 hours',   1, now() - interval '7 days 8 hours',   now() - interval '7 days 8 hours'),    -- Hannah on-time
  ('2e000000-0000-0000-0000-000000030302', '2d000000-0000-0000-0000-000000000303', '29000000-0000-0000-0000-000000000007',  8, 10, 280, now() - interval '7 days 4 hours',   1, now() - interval '7 days 4 hours',   now() - interval '7 days 4 hours'),    -- Joel   on-time
  ('2e000000-0000-0000-0000-000000030304', '2d000000-0000-0000-0000-000000000303', '29000000-0000-0000-0000-00000000000c', 10, 10, 140, now() - interval '6 days 6 hours',   1, now() - interval '6 days 6 hours',   now() - interval '6 days 6 hours'),    -- Isla   LATE

  -- Wk 4 (due now) — 3/5 (Hannah, Joel, Isla)
  ('2e000000-0000-0000-0000-000000030401', '2d000000-0000-0000-0000-000000000304', '29000000-0000-0000-0000-000000000006', 10, 10, 200, now() - interval '1 hour',           1, now() - interval '1 hour',           now() - interval '1 hour'),            -- Hannah on-time
  ('2e000000-0000-0000-0000-000000030402', '2d000000-0000-0000-0000-000000000304', '29000000-0000-0000-0000-000000000007',  9, 10, 230, now() - interval '2 hours',          1, now() - interval '2 hours',          now() - interval '2 hours'),           -- Joel   on-time
  ('2e000000-0000-0000-0000-000000030404', '2d000000-0000-0000-0000-000000000304', '29000000-0000-0000-0000-00000000000c', 10, 10, 150, now() - interval '30 minutes',       1, now() - interval '30 minutes',       now() - interval '30 minutes')         -- Isla   on-time
ON CONFLICT (id) DO NOTHING;


COMMIT;

-- =====================================================================
-- END OF SEED FILE
-- =====================================================================
-- VERIFICATION QUERIES (run after apply)
--
--   -- 1. Counts: previous totals + this migration's additions
--   SELECT count(*) FROM public.subjects;                  -- expect 4   (Bio,Chem,Phys + Science)
--   SELECT count(*) FROM public.profiles;                  -- expect 28  (13 prior + 15 new)
--   SELECT count(*) FROM auth.users;                       -- expect 28  (same)
--   SELECT count(*) FROM public.classes;                   -- expect 4   (1 prior + 3 new)
--   SELECT count(*) FROM public.class_teachers;            -- expect 8   (1 + 7)
--   SELECT count(*) FROM public.class_members;             -- expect 23  (7 + 16)
--   SELECT count(*) FROM public.assignments;               -- expect 24  (4 + 20)
--   SELECT count(*) FROM public.assignment_submissions;    -- expect 87  (22 + 65)
--
--   -- 2. New "Science" subject row exists with display_order 0
--   SELECT id, name, department, display_order, active
--   FROM public.subjects
--   WHERE id = '26000000-0000-0000-0000-000000000001';     -- expect 1 row, display_order=0
--
--   -- 3. Per-class submission counts
--   SELECT c.name,
--          (SELECT count(*) FROM class_members  WHERE class_id = c.id AND left_at IS NULL) AS students,
--          (SELECT count(*) FROM assignments    WHERE class_id = c.id AND deleted_at IS NULL) AS assigns,
--          (SELECT count(*) FROM assignment_submissions sub
--             JOIN assignments a ON a.id = sub.assignment_id
--             WHERE a.class_id = c.id AND sub.submitted_at IS NOT NULL AND sub.deleted_at IS NULL) AS subs
--   FROM public.classes c
--   ORDER BY c.name;
--   --   expect:
--   --     10A           students=6, assigns=12, subs=36   (50%)
--   --     10X1 Biology  students=7, assigns=4,  subs=22   (78% — pre-existing)
--   --     10Z Physics   students=5, assigns=4,  subs=15   (75%)
--   --     8X1           students=5, assigns=4,  subs=14   (70%)
--
--   -- 4. Mide-as-teacher card-count check (RLS — anon role won't work,
--   --    run as Mide via Studio impersonate, or just trust the 7 rows)
--   SELECT class_id, subject_id FROM public.class_teachers
--   WHERE teacher_id = '28000000-0000-0000-0000-000000000001'
--     AND ended_at IS NULL AND deleted_at IS NULL;
--   --   expect: 4 class_teachers rows for Mide (10A Phys, 10A Chem,
--   --           10Z Phys, 8X1 Science) → 3 cards on the dashboard
--   --           because the two 10A rows collapse to one card.
--
--   -- 5. J-as-teacher card-count check
--   SELECT class_id, subject_id FROM public.class_teachers
--   WHERE teacher_id = '28000000-0000-0000-0000-000000000002'
--     AND ended_at IS NULL AND deleted_at IS NULL;
--   --   expect: 3 class_teachers rows for J (10A Bio, 10A Chem,
--   --           8X1 Science) → 2 cards on the dashboard
--   --           because the two 10A rows collapse to one card.
--
--   -- 6. 10Z leaderboard tiebreak preview (Stars eligibility = all 4 done)
--   SELECT
--     p.first_name,
--     count(*) AS submitted,
--     sum(CASE WHEN sub.submitted_at <= a.due_at THEN 1 ELSE 0 END) AS on_time,
--     round(100.0 * sum(sub.score) / sum(sub.max_score), 1) AS score_pct,
--     sum(sub.total_time_seconds) AS total_seconds
--   FROM public.assignment_submissions sub
--   JOIN public.assignments a ON a.id = sub.assignment_id
--   JOIN public.profiles p     ON p.id = sub.student_id
--   WHERE a.class_id = '2a000000-0000-0000-0000-000000000003'
--     AND sub.submitted_at IS NOT NULL
--     AND sub.deleted_at IS NULL
--   GROUP BY p.first_name
--   HAVING count(*) = (SELECT count(*) FROM assignments
--                       WHERE class_id = '2a000000-0000-0000-0000-000000000003'
--                         AND deleted_at IS NULL)
--   ORDER BY on_time DESC, score_pct DESC, total_seconds ASC, p.first_name ASC;
--   --   expect ranking:
--   --     Hannah  4 on-time  95%   800s
--   --     Joel    4 on-time  85%  1000s
--   --     Isla    3 on-time 100%   600s   ← perfect score, ranks 3rd because of one late
--
--   -- 7. Live test: sign in via auth.html (localhost = test mode)
--   --    All passwords: TestPass!2026
--   --    teacher@test-rainford.local       (Sarah)
--   --    mide.badmus@test-rainford.local   (Mide)
--   --    j.okonkwo@test-rainford.local     (J)
-- =====================================================================
