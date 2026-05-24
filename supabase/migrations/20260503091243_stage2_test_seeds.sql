-- =====================================================================
-- Migration:        0002_stage2_test_seeds.sql
-- Stage:            2A — test fixtures for /teacher/* dashboard build
-- Branch:           schools/stage-1-schema-rls (Stage 2 work continues here)
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) — fake data only
-- Linear:           MRB-18
-- =====================================================================
--
-- Seeds the test project with the smallest realistic universe needed to
-- build and demo the MRB-20 "My classes" list page:
--
--   - 1 teacher (Sarah Whitfield)
--   - 1 class:  10X1 Biology — Y10, KS4, Higher tier, Triple pathway
--   - 7 students (Amelia, Oliver, Priya, Jacob, Maya, Ethan, Sophie)
--   - 4 weekly Biology topic quizzes covering the past 4 weeks
--   - 22 submissions with patchy completion (6 / 5 / 7 / 4 students/week)
--
-- All entities attach to Rainford High School and the 2025-26 academic
-- year — both already seeded by 0001_schools_layer.sql.
--
-- Idempotent: every INSERT uses ON CONFLICT (id) DO NOTHING with
-- deterministic UUIDs, so re-running this file produces the same data.
--
-- UUID convention (visually distinct from the baseline xxxxxxxx-aaaa
-- legacy pattern, so collisions are impossible at a glance):
--
--   2000…0001            → teacher (Sarah Whitfield)
--   2100…0001 — 0007     → 7 students
--   2200…0001            → class (10X1 Biology)
--   2300…0001            → class_teachers row (teacher → class)
--   2400…0001 — 0007     → class_members rows (student → class)
--   2500…0001 — 0004     → 4 weekly assignments
--   2600…WWSS            → submissions, last 4 hex digits encode
--                           WW = week (01..04), SS = student# (01..07)
--                           e.g. 2600…0301 = wk3 student1
-- =====================================================================

BEGIN;

-- =====================================================================
-- 0 — Pre-flight: refuse to run unless Stage 1 is in place
-- =====================================================================
-- Protects against accidental application before the schema exists.
-- =====================================================================

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM public.schools WHERE slug = 'rainford-high') THEN
    RAISE EXCEPTION 'Stage 1 not applied: Rainford High School (slug=rainford-high) not found';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM public.subjects WHERE name = 'Biology') THEN
    RAISE EXCEPTION 'Stage 1 not applied: Biology subject not found';
  END IF;
  IF NOT EXISTS (
    SELECT 1
    FROM public.academic_years ay
    JOIN public.schools s ON s.id = ay.school_id
    WHERE s.slug = 'rainford-high' AND ay.name = '2025-26'
  ) THEN
    RAISE EXCEPTION 'Stage 1 not applied: 2025-26 academic year for Rainford not found';
  END IF;
END $$;


-- =====================================================================
-- 1 — auth.users (teacher + 7 students)
-- =====================================================================
-- profiles.id has a hard FK to auth.users.id, so users must come first.
-- Form matches 0000_recreate_prod_baseline.sql (full Supabase auth shape).
--
-- All seven GoTrue text columns (confirmation_token, recovery_token,
-- email_change_token_new, email_change_token_current, email_change,
-- phone_change_token, reauthentication_token) are set to '' explicitly.
-- NULL on any of these breaks signin: GoTrue's User struct types them
-- as non-nullable Go strings and sql.Scan errors with "converting NULL
-- to string is unsupported". Real Supabase signups always insert these
-- as ''; direct SQL inserts must too. See MRB-37 for the incident
-- that surfaced this.
-- =====================================================================

INSERT INTO auth.users (
  id, email, raw_user_meta_data, aud, role,
  email_confirmed_at, created_at, updated_at, instance_id,
  confirmation_token, recovery_token, email_change_token_new, email_change_token_current,
  email_change, phone_change_token, reauthentication_token
) VALUES
  ('20000000-0000-0000-0000-000000000001', 'teacher@test-rainford.local',  '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000001', 'student1@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000002', 'student2@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000003', 'student3@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000004', 'student4@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000005', 'student5@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000006', 'student6@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', ''),
  ('21000000-0000-0000-0000-000000000007', 'student7@test-rainford.local', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000', '', '', '', '', '', '', '')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 2 — public.profiles (teacher + 7 students)
-- =====================================================================
-- Teacher: role=teacher, KS4 (matches the class), no department.
--   department is required only for role='hod' per
--   profiles_hod_needs_department_check, so leaving it NULL is correct.
-- Students: role=student, KS4, Higher, Triple — matches the class shape.
-- All bound to Rainford via slug lookup so the file stays portable.
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
  ('20000000-0000-0000-0000-000000000001'::uuid, 'teacher', 'KS4', NULL,     NULL,     'Sarah',  'Whitfield'),
  ('21000000-0000-0000-0000-000000000001'::uuid, 'student', 'KS4', 'higher', 'triple', 'Amelia', 'Carter'),
  ('21000000-0000-0000-0000-000000000002'::uuid, 'student', 'KS4', 'higher', 'triple', 'Oliver', 'Mensah'),
  ('21000000-0000-0000-0000-000000000003'::uuid, 'student', 'KS4', 'higher', 'triple', 'Priya',  'Sharma'),
  ('21000000-0000-0000-0000-000000000004'::uuid, 'student', 'KS4', 'higher', 'triple', 'Jacob',  'Reid'),
  ('21000000-0000-0000-0000-000000000005'::uuid, 'student', 'KS4', 'higher', 'triple', 'Maya',   'Anwar'),
  ('21000000-0000-0000-0000-000000000006'::uuid, 'student', 'KS4', 'higher', 'triple', 'Ethan',  'Brooks'),
  ('21000000-0000-0000-0000-000000000007'::uuid, 'student', 'KS4', 'higher', 'triple', 'Sophie', 'Lin')
) AS v(id, role, key_stage, tier, science_pathway, first_name, last_name)
WHERE s.slug = 'rainford-high'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 3 — public.classes (10X1 Biology)
-- =====================================================================
-- Y10, KS4, Higher tier, Triple pathway. Looks up Rainford and the
-- 2025-26 academic year by their natural keys.
-- =====================================================================

INSERT INTO public.classes (
  id, school_id, academic_year_id, name,
  key_stage, year_group, tier, science_pathway
)
SELECT
  '22000000-0000-0000-0000-000000000001'::uuid,
  s.id, ay.id, '10X1 Biology',
  'KS4', 10, 'higher', 'triple'
FROM public.schools s
JOIN public.academic_years ay ON ay.school_id = s.id AND ay.name = '2025-26'
WHERE s.slug = 'rainford-high'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 4 — public.class_teachers (Sarah Whitfield → 10X1 Biology, Biology)
-- =====================================================================
-- role='subject_teacher' requires non-NULL subject_id per
-- class_teachers_subject_required_check.
-- =====================================================================

INSERT INTO public.class_teachers (
  id, class_id, teacher_id, subject_id, role
)
SELECT
  '23000000-0000-0000-0000-000000000001'::uuid,
  '22000000-0000-0000-0000-000000000001'::uuid,
  '20000000-0000-0000-0000-000000000001'::uuid,
  s.id,
  'subject_teacher'
FROM public.subjects s
WHERE s.name = 'Biology'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 5 — public.class_members (7 students → 10X1 Biology)
-- =====================================================================
-- joined_via='admin_added' for all (typical for fixture data).
-- =====================================================================

INSERT INTO public.class_members (
  id, class_id, student_id, joined_via
) VALUES
  ('24000000-0000-0000-0000-000000000001', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000001', 'admin_added'),
  ('24000000-0000-0000-0000-000000000002', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000002', 'admin_added'),
  ('24000000-0000-0000-0000-000000000003', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000003', 'admin_added'),
  ('24000000-0000-0000-0000-000000000004', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000004', 'admin_added'),
  ('24000000-0000-0000-0000-000000000005', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000005', 'admin_added'),
  ('24000000-0000-0000-0000-000000000006', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000006', 'admin_added'),
  ('24000000-0000-0000-0000-000000000007', '22000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000007', 'admin_added')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 6 — public.assignments (4 weekly Biology topic quizzes)
-- =====================================================================
-- All quiz_type='topic_quiz', auto_generated=false (teacher-set, not
-- generated from a scheme_of_work_entries row). max_score=10 lives on
-- each submission, not on the assignment itself.
-- due_at is anchored relative to now() so the file remains valid over time.
-- =====================================================================

INSERT INTO public.assignments (
  id, class_id, teacher_id, subject_id,
  topic, subtopic, title, instructions,
  quiz_type, due_at, auto_generated
)
SELECT
  v.id,
  '22000000-0000-0000-0000-000000000001'::uuid,
  '20000000-0000-0000-0000-000000000001'::uuid,
  s.id,
  v.topic, v.subtopic, v.title, v.instructions,
  'topic_quiz', v.due_at, false
FROM public.subjects s
CROSS JOIN (VALUES
  ('25000000-0000-0000-0000-000000000001'::uuid,
    'Cell Biology',           'Cell structure and transport',
    'Cell Biology Quiz — Week 1',
    '10 questions on cell structure, microscopy, and transport across membranes.',
    now() - interval '21 days'),
  ('25000000-0000-0000-0000-000000000002'::uuid,
    'Organisation',           'Animal organisation',
    'Organisation Quiz — Week 2',
    '10 questions on the digestive system, the heart, and circulation.',
    now() - interval '14 days'),
  ('25000000-0000-0000-0000-000000000003'::uuid,
    'Infection and response', 'Communicable diseases',
    'Infection & Response Quiz — Week 3',
    '10 questions on pathogens, the immune system, and antibiotics.',
    now() - interval '7 days'),
  ('25000000-0000-0000-0000-000000000004'::uuid,
    'Bioenergetics',          'Photosynthesis',
    'Bioenergetics Quiz — Week 4',
    '10 questions on photosynthesis, limiting factors, and respiration.',
    now())
) AS v(id, topic, subtopic, title, instructions, due_at)
WHERE s.name = 'Biology'
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 7 — public.assignment_submissions (22 rows, patchy completion)
-- =====================================================================
-- Per-week pattern (= 6 + 5 + 7 + 4 = 22):
--   W1 (6/7): all but Sophie
--   W2 (5/7): all but Ethan + Sophie; Jacob bombed first try (attempts=2)
--   W3 (7/7): everyone
--   W4 (4/7): Amelia, Oliver, Priya, Maya — Jacob, Ethan, Sophie miss
--
-- Submission UUID encoding: 26000000-0000-0000-0000-00000000WWSS
--   WW = week (01..04), SS = student# (01..07)
--
-- max_score=10 throughout. total_time_seconds correlates inversely with
-- score (strong=fast, weak=slow). attempts=1 except Jacob W2 (=2).
-- submitted_at clusters in the 24h window before each due_at.
-- =====================================================================

INSERT INTO public.assignment_submissions (
  id, assignment_id, student_id,
  score, max_score, total_time_seconds, submitted_at, attempts
) VALUES
  -- ── Week 1 — Cell Biology (due now-21d) — 6/7 ─────────────────────
  ('26000000-0000-0000-0000-000000000101', '25000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000001',  9, 10, 320, now() - interval '21 days 18 hours', 1),  -- Amelia
  ('26000000-0000-0000-0000-000000000102', '25000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000002',  8, 10, 280, now() - interval '21 days 14 hours', 1),  -- Oliver
  ('26000000-0000-0000-0000-000000000103', '25000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000003',  8, 10, 340, now() - interval '21 days 8 hours',  1),  -- Priya
  ('26000000-0000-0000-0000-000000000104', '25000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000004',  7, 10, 480, now() - interval '21 days 4 hours',  1),  -- Jacob
  ('26000000-0000-0000-0000-000000000105', '25000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000005',  6, 10, 510, now() - interval '21 days 2 hours',  1),  -- Maya
  ('26000000-0000-0000-0000-000000000106', '25000000-0000-0000-0000-000000000001', '21000000-0000-0000-0000-000000000006',  5, 10, 620, now() - interval '21 days 1 hour',   1),  -- Ethan
  -- (Sophie absent)

  -- ── Week 2 — Organisation (due now-14d) — 5/7 ────────────────────
  ('26000000-0000-0000-0000-000000000201', '25000000-0000-0000-0000-000000000002', '21000000-0000-0000-0000-000000000001', 10, 10, 240, now() - interval '14 days 16 hours', 1),  -- Amelia
  ('26000000-0000-0000-0000-000000000202', '25000000-0000-0000-0000-000000000002', '21000000-0000-0000-0000-000000000002',  9, 10, 260, now() - interval '14 days 12 hours', 1),  -- Oliver
  ('26000000-0000-0000-0000-000000000203', '25000000-0000-0000-0000-000000000002', '21000000-0000-0000-0000-000000000003',  7, 10, 440, now() - interval '14 days 6 hours',  1),  -- Priya
  ('26000000-0000-0000-0000-000000000204', '25000000-0000-0000-0000-000000000002', '21000000-0000-0000-0000-000000000004',  5, 10, 580, now() - interval '14 days 3 hours',  2),  -- Jacob (2 attempts)
  ('26000000-0000-0000-0000-000000000205', '25000000-0000-0000-0000-000000000002', '21000000-0000-0000-0000-000000000005',  7, 10, 470, now() - interval '14 days 1 hour',   1),  -- Maya
  -- (Ethan, Sophie absent)

  -- ── Week 3 — Infection & Response (due now-7d) — 7/7 ─────────────
  ('26000000-0000-0000-0000-000000000301', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000001',  9, 10, 350, now() - interval '7 days 19 hours', 1),  -- Amelia
  ('26000000-0000-0000-0000-000000000302', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000002',  9, 10, 290, now() - interval '7 days 16 hours', 1),  -- Oliver
  ('26000000-0000-0000-0000-000000000303', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000003',  8, 10, 420, now() - interval '7 days 10 hours', 1),  -- Priya
  ('26000000-0000-0000-0000-000000000304', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000004',  7, 10, 510, now() - interval '7 days 6 hours',  1),  -- Jacob
  ('26000000-0000-0000-0000-000000000305', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000005',  6, 10, 540, now() - interval '7 days 4 hours',  1),  -- Maya
  ('26000000-0000-0000-0000-000000000306', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000006',  6, 10, 590, now() - interval '7 days 2 hours',  1),  -- Ethan
  ('26000000-0000-0000-0000-000000000307', '25000000-0000-0000-0000-000000000003', '21000000-0000-0000-0000-000000000007',  4, 10, 700, now() - interval '7 days 1 hour',   1),  -- Sophie

  -- ── Week 4 — Bioenergetics (due now) — 4/7 ───────────────────────
  ('26000000-0000-0000-0000-000000000401', '25000000-0000-0000-0000-000000000004', '21000000-0000-0000-0000-000000000001', 10, 10, 280, now() - interval '1 day 8 hours',  1),  -- Amelia
  ('26000000-0000-0000-0000-000000000402', '25000000-0000-0000-0000-000000000004', '21000000-0000-0000-0000-000000000002',  9, 10, 320, now() - interval '1 day 4 hours',  1),  -- Oliver
  ('26000000-0000-0000-0000-000000000403', '25000000-0000-0000-0000-000000000004', '21000000-0000-0000-0000-000000000003',  8, 10, 410, now() - interval '16 hours',       1),  -- Priya
  ('26000000-0000-0000-0000-000000000405', '25000000-0000-0000-0000-000000000004', '21000000-0000-0000-0000-000000000005',  6, 10, 600, now() - interval '4 hours',        1)   -- Maya
  -- (Jacob, Ethan, Sophie absent)
ON CONFLICT (id) DO NOTHING;


COMMIT;

-- =====================================================================
-- END OF SEED FILE
-- =====================================================================
-- VERIFICATION QUERIES (run after apply)
--
--   -- 8 fake new + 5 legacy = 13 total profiles
--   SELECT count(*) FROM public.profiles;               -- expect 13
--
--   -- One class, one teacher row, seven members
--   SELECT count(*) FROM public.classes;                -- expect 1
--   SELECT count(*) FROM public.class_teachers;         -- expect 1
--   SELECT count(*) FROM public.class_members;          -- expect 7
--
--   -- Four assignments, twenty-two submissions
--   SELECT count(*) FROM public.assignments;            -- expect 4
--   SELECT count(*) FROM public.assignment_submissions; -- expect 22
--
--   -- Per-week submission counts (in due_at order)
--   SELECT a.title, count(*) AS submitted
--   FROM public.assignment_submissions sub
--   JOIN public.assignments a ON a.id = sub.assignment_id
--   GROUP BY a.title, a.due_at
--   ORDER BY a.due_at;                                  -- 6, 5, 7, 4
-- =====================================================================
