-- =====================================================================
-- Migration:        0008_stage2_seed_empty_state_classes.sql
-- Stage:            2B — class detail page (MRB-38) — Phase 2
-- Branch:           schools/mrb-38-class-detail
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) — fake data only
-- Linear:           MRB-38 (Phase 2 — empty-state coverage)
-- =====================================================================
--
-- Adds two new KS3 classes that exercise the two empty-state branches
-- of the MRB-38 weekly Stars leaderboard:
--
--   8X2  — has a current-week assignment but ZERO submissions yet
--          → "leaderboard hides because no one is eligible"
--   9Y1  — has NO assignments at all
--          → "leaderboard hides because nothing is due this week"
--
-- Both classes are taught by Mide (28000000…0001), so they appear on
-- his MRB-20 dashboard alongside the existing 8X1 / 10A / 10Z trio.
-- Sarah's and J's dashboards are unaffected.
--
-- Both new classes set assignment_day_of_week = 1 (Monday) explicitly.
-- The four pre-existing classes stay NULL so the UI's "fall back to
-- Monday when NULL" branch (added in 0007 / MRB-38 Phase 1) is also
-- exercised.
--
-- ── Time-drift caveat (0006's populated-leaderboard fixtures) ───────
-- 0006 inserts assignments with now()-relative due_at. Because the
-- migration is idempotent (ON CONFLICT DO NOTHING), re-applying does
-- NOT refresh the timestamps. Mide first applied 0006 on 2026-05-03,
-- so its assignments are frozen at that date and will quietly drift
-- out of "this week" within a day or two of the current date.
--
-- 0008 does NOT fix that. Keeping 0008 strictly additive. If/when
-- the populated-leaderboard demos go stale during MRB-38 build, deal
-- with it separately (re-run 0006 fresh, or write a tiny UPDATE
-- migration). 0008's new assignment is dated `now() + interval '5 days'`
-- so it stays inside the current Monday-anchored week regardless of
-- when the file is read.
--
-- Note: 0008's own 8X2 assignment has the same property — its due_at
-- freezes at first-apply + 5 days. If 0008 is re-applied weeks later
-- to refresh test data, the assignment's due_at will NOT refresh.
-- Same mitigation applies (separate UPDATE migration, or fresh re-seed).
--
-- ── After this migration applies ────────────────────────────────────
-- Total classes: 4 → 6
-- Total students: 14 → 20 (6 new KS3)
-- Mide's dashboard: 3 cards → 5 cards (8X1, 10A, 10Z, 8X2, 9Y1)
-- J's dashboard:    2 cards → unchanged
-- Sarah's dashboard: 1 card → unchanged
--
-- ── Insert counts ───────────────────────────────────────────────────
--   auth.users:               +6   (3 per class, gold-standard pattern)
--   profiles:                 +6   (matched 1-to-1)
--   classes:                  +2
--   class_teachers:           +2   (Mide → each class, subject Science)
--   class_members:            +6
--   assignments:              +1   (8X2's "this week" assignment only)
--   assignment_submissions:   +0   (by design — that's the point)
--   Total: 23 new rows
--
-- ── UUID convention (extends 0006) ──────────────────────────────────
--   29000000…000E..0010 → 8X2 students (Maya, Felix, Amara)
--   29000000…0011..0013 → 9Y1 students (Ezra, Sienna, Theo)
--   2A000000…0004       → class 8X2
--   2A000000…0005       → class 9Y1
--   2B000000…0008       → class_teachers row Mide → 8X2 (Science)
--   2B000000…0009       → class_teachers row Mide → 9Y1 (Science)
--   2C000000…0401..0403 → 8X2 class_members (3 students)
--   2C000000…0501..0503 → 9Y1 class_members (3 students)
--   2D000000…0401       → 8X2's "Cells & Microscopy" assignment
--
-- ── Idempotency ─────────────────────────────────────────────────────
-- Every INSERT uses a deterministic UUID + ON CONFLICT (id) DO NOTHING.
-- Re-running this file produces the same data and never mutates rows
-- it has already inserted.
-- =====================================================================

BEGIN;

-- =====================================================================
-- 0 — Pre-flight: refuse to run unless 0006 + 0007 are in place
-- =====================================================================
-- Anchors:
--   • Class 8X1 (2A…0001) exists           → 0006 ran
--   • classes.assignment_day_of_week column → 0007 ran
-- =====================================================================

DO $$
DECLARE
  v_8x1_exists    boolean;
  v_column_exists boolean;
BEGIN
  SELECT EXISTS (
    SELECT 1 FROM public.classes
    WHERE id = '2a000000-0000-0000-0000-000000000001'
      AND name = '8X1'
  ) INTO v_8x1_exists;

  IF NOT v_8x1_exists THEN
    RAISE EXCEPTION '0006_stage2_test_seeds_expanded.sql must be applied first: class 8X1 (2A...0001) not found';
  END IF;

  SELECT EXISTS (
    SELECT 1 FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name   = 'classes'
      AND column_name  = 'assignment_day_of_week'
  ) INTO v_column_exists;

  IF NOT v_column_exists THEN
    RAISE EXCEPTION '0007_add_assignment_day_of_week.sql must be applied first: classes.assignment_day_of_week column not found';
  END IF;
END $$;


-- =====================================================================
-- 1 — auth.users (6 new KS3 students)
-- =====================================================================
-- Gold-standard pattern (matches 0006). Same password for all fixtures.
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
  -- ── 8X2 students (Y8 / KS3) ────────────────────────────────────────
  ('29000000-0000-0000-0000-00000000000e', 'maya.singh@test-rainford.local',     crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-00000000000f', 'felix.roberts@test-rainford.local',  crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000010', 'amara.okafor@test-rainford.local',   crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),

  -- ── 9Y1 students (Y9 / KS3) ────────────────────────────────────────
  ('29000000-0000-0000-0000-000000000011', 'ezra.bloom@test-rainford.local',     crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000012', 'sienna.foster@test-rainford.local',  crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('29000000-0000-0000-0000-000000000013', 'theo.nakamura@test-rainford.local',  crypt('TestPass!2026', gen_salt('bf', 10)), '{"provider":"email","providers":["email"]}'::jsonb, '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', '')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 2 — public.profiles (6 new KS3 students)
-- =====================================================================
-- KS3 students: key_stage='KS3', tier+pathway BOTH NULL (per
-- profiles_tier_only_ks4_check). exam_board='AQA' to match 0006.
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
  -- ── 8X2 students ──────────────────────────────────────────────────
  ('29000000-0000-0000-0000-00000000000e'::uuid, 'student', 'KS3', NULL, NULL, 'Maya',   'Singh'),
  ('29000000-0000-0000-0000-00000000000f'::uuid, 'student', 'KS3', NULL, NULL, 'Felix',  'Roberts'),
  ('29000000-0000-0000-0000-000000000010'::uuid, 'student', 'KS3', NULL, NULL, 'Amara',  'Okafor'),

  -- ── 9Y1 students ──────────────────────────────────────────────────
  ('29000000-0000-0000-0000-000000000011'::uuid, 'student', 'KS3', NULL, NULL, 'Ezra',   'Bloom'),
  ('29000000-0000-0000-0000-000000000012'::uuid, 'student', 'KS3', NULL, NULL, 'Sienna', 'Foster'),
  ('29000000-0000-0000-0000-000000000013'::uuid, 'student', 'KS3', NULL, NULL, 'Theo',   'Nakamura')
) AS v(id, role, key_stage, tier, science_pathway, first_name, last_name)
WHERE s.slug = 'rainford-high'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 3 — public.classes (2 new KS3 classes)
-- =====================================================================
-- Both KS3 (tier + pathway both NULL per the same check). Both anchor
-- assignment week to Monday (assignment_day_of_week = 1).
-- =====================================================================

INSERT INTO public.classes (
  id, school_id, academic_year_id, name,
  key_stage, year_group, tier, science_pathway,
  assignment_day_of_week
)
SELECT
  v.id, s.id, ay.id, v.name,
  v.key_stage, v.year_group, v.tier, v.science_pathway,
  v.assignment_day_of_week
FROM public.schools s
JOIN public.academic_years ay ON ay.school_id = s.id AND ay.name = '2025-26'
CROSS JOIN (VALUES
  ('2a000000-0000-0000-0000-000000000004'::uuid, '8X2', 'KS3', 8::smallint, NULL::text, NULL::text, 1::smallint),
  ('2a000000-0000-0000-0000-000000000005'::uuid, '9Y1', 'KS3', 9::smallint, NULL::text, NULL::text, 1::smallint)
) AS v(id, name, key_stage, year_group, tier, science_pathway, assignment_day_of_week)
WHERE s.slug = 'rainford-high'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 4 — public.class_teachers (2 rows: Mide → each class, Science)
-- =====================================================================

INSERT INTO public.class_teachers (id, class_id, teacher_id, subject_id, role)
VALUES
  ('2b000000-0000-0000-0000-000000000008',
   '2a000000-0000-0000-0000-000000000004',
   '28000000-0000-0000-0000-000000000001',
   '26000000-0000-0000-0000-000000000001',
   'subject_teacher'),
  ('2b000000-0000-0000-0000-000000000009',
   '2a000000-0000-0000-0000-000000000005',
   '28000000-0000-0000-0000-000000000001',
   '26000000-0000-0000-0000-000000000001',
   'subject_teacher')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 5 — public.class_members (6 rows: 3 + 3)
-- =====================================================================
-- ID encoding: 2C…00WWMM where WW=class index (04=8X2, 05=9Y1),
-- MM=member-within-class.
-- =====================================================================

INSERT INTO public.class_members (id, class_id, student_id, joined_via)
VALUES
  -- 8X2 (3 students)
  ('2c000000-0000-0000-0000-000000000401', '2a000000-0000-0000-0000-000000000004', '29000000-0000-0000-0000-00000000000e', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000402', '2a000000-0000-0000-0000-000000000004', '29000000-0000-0000-0000-00000000000f', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000403', '2a000000-0000-0000-0000-000000000004', '29000000-0000-0000-0000-000000000010', 'admin_added'),

  -- 9Y1 (3 students)
  ('2c000000-0000-0000-0000-000000000501', '2a000000-0000-0000-0000-000000000005', '29000000-0000-0000-0000-000000000011', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000502', '2a000000-0000-0000-0000-000000000005', '29000000-0000-0000-0000-000000000012', 'admin_added'),
  ('2c000000-0000-0000-0000-000000000503', '2a000000-0000-0000-0000-000000000005', '29000000-0000-0000-0000-000000000013', 'admin_added')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 6 — public.assignments (1 row: 8X2's "Cells & Microscopy" quick check)
-- =====================================================================
-- Due 5 days from now (lands inside the current Monday-anchored week
-- regardless of which weekday this file is read on). created_at = 7
-- days before due_at, matching 0006's convention.
--
-- 9Y1 deliberately gets ZERO assignments — that's the empty-state-B
-- coverage.
-- =====================================================================

INSERT INTO public.assignments (
  id, class_id, teacher_id, subject_id,
  topic, subtopic, title, instructions,
  quiz_type, due_at, created_at, updated_at, auto_generated
) VALUES
  ('2d000000-0000-0000-0000-000000000401',
   '2a000000-0000-0000-0000-000000000004', -- 8X2
   '28000000-0000-0000-0000-000000000001', -- Mide
   '26000000-0000-0000-0000-000000000001', -- Science
   'Cells', 'Microscopy',
   'Cells & Microscopy quick check',
   '10 questions on plant and animal cells and how to use a microscope to study them.',
   'topic_quiz',
   now() + interval '5 days',
   now() - interval '2 days',
   now() - interval '2 days',
   false)
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 7 — public.assignment_submissions: NONE
-- =====================================================================
-- 8X2 → 1 assignment, 0 submissions (empty-state A: no eligibles)
-- 9Y1 → 0 assignments, 0 submissions (empty-state B: no work due)
-- That's the entire point of this migration. No INSERT here.
-- =====================================================================


COMMIT;
