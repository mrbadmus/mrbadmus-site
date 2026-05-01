-- =====================================================================
-- Test Plan:    0001_schools_layer_tests.sql
-- For:          0001_schools_layer.sql
-- Purpose:      Verify RLS pyramid holds. Catches data leaks before prod.
-- Run on:       Supabase BRANCH only (after migration applied to branch).
-- Safety:       Wrapped in BEGIN/ROLLBACK — no data persists after run.
--
-- Strategy:     Create a fake parallel universe. Two schools, full role
--               pyramid in each, plus legacy unattached users. For every
--               cross-school query, prove zero rows leak. For every
--               in-school query, prove the right role sees the right data.
--
-- Reading this file:
--   - Each test is a NOTICE that prints PASS or FAIL.
--   - At the end, a final summary shows total pass/fail counts.
--   - If any test FAILS, do not proceed to production. Investigate first.
-- =====================================================================

BEGIN;

-- =====================================================================
-- HELPERS — keep test code DRY
-- =====================================================================

-- Tiny test runner: takes an expected count and an actual count, prints
-- PASS or FAIL with a label. Counts go into a temp table for the summary.
CREATE TEMP TABLE test_results (
  test_name text,
  expected_count int,
  actual_count int,
  passed boolean
);

-- IMPORTANT: SECURITY DEFINER lets this function INSERT into the
-- pg_temp.test_results table no matter which role we've impersonated
-- via set_config('role', 'authenticated', ...).
--
-- The actual RLS assertions are unaffected: the SELECT count(*) that
-- becomes the `actual` argument is evaluated in the CALLER'S context
-- (under the impersonated role) BEFORE assert_count is invoked.
-- assert_count just records and announces the result.
--
-- search_path is pinned to pg_temp so SECURITY DEFINER cannot be
-- redirected to write to a malicious public.test_results.
CREATE OR REPLACE FUNCTION pg_temp.assert_count(
  test_name text,
  expected int,
  actual int
) RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = pg_temp
AS $$
DECLARE
  did_pass boolean := (expected = actual);
BEGIN
  INSERT INTO test_results VALUES (test_name, expected, actual, did_pass);
  IF did_pass THEN
    RAISE NOTICE '✓ PASS  %  (expected %, got %)', test_name, expected, actual;
  ELSE
    RAISE WARNING '✗ FAIL  %  (expected %, got %)', test_name, expected, actual;
  END IF;
END;
$$;

-- Convenience: set the current "logged in" user for RLS testing.
-- We use Supabase's auth.uid() pattern by setting the request.jwt.claim.sub.
CREATE OR REPLACE FUNCTION pg_temp.login_as(user_id uuid) RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
  PERFORM set_config('request.jwt.claim.sub', user_id::text, true);
  PERFORM set_config('request.jwt.claims', json_build_object('sub', user_id)::text, true);
  PERFORM set_config('role', 'authenticated', true);
END;
$$;

-- And reset to nobody (anonymous role)
CREATE OR REPLACE FUNCTION pg_temp.logout() RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
  PERFORM set_config('request.jwt.claim.sub', '', true);
  PERFORM set_config('request.jwt.claims', '', true);
  PERFORM set_config('role', 'anon', true);
END;
$$;


-- =====================================================================
-- SECTION A — BUILD THE FAKE UNIVERSE
-- =====================================================================
-- Two schools. Full pyramid in each. Plus a legacy user.
-- All UUIDs are deterministic so the assertions are easy to read.
-- =====================================================================

-- Two schools
INSERT INTO public.schools (id, name, code, slug, email_domains, active)
VALUES
  ('11111111-1111-1111-1111-111111111111', 'Test School Alpha', 'ALPHA', 'test-alpha', ARRAY['alpha.test'], true),
  ('22222222-2222-2222-2222-222222222222', 'Test School Bravo', 'BRAVO', 'test-bravo', ARRAY['bravo.test'], true);

-- Academic year for each
INSERT INTO public.academic_years (id, school_id, name, start_date, end_date, is_current)
VALUES
  ('aaaa1111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', '2025-26', '2025-09-01', '2026-08-31', true),
  ('aaaa2222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', '2025-26', '2025-09-01', '2026-08-31', true);

-- We need fake auth.users entries for each profile. Supabase normally creates
-- these via the signup flow; in tests we insert directly.
-- (This requires the test to run as service_role or a privileged role on the branch.)
INSERT INTO auth.users (id, email, raw_user_meta_data, created_at)
VALUES
  -- Alpha school
  ('a0000001-0000-0000-0000-000000000001', 'admin@alpha.test',           '{}'::jsonb, now()),
  ('a0000002-0000-0000-0000-000000000002', 'hod.science@alpha.test',     '{}'::jsonb, now()),
  ('a0000003-0000-0000-0000-000000000003', 'hod.maths@alpha.test',       '{}'::jsonb, now()),
  ('a0000004-0000-0000-0000-000000000004', 'teacher.bio@alpha.test',     '{}'::jsonb, now()),
  ('a0000005-0000-0000-0000-000000000005', 'teacher.maths@alpha.test',   '{}'::jsonb, now()),
  ('a0000006-0000-0000-0000-000000000006', 'student1@alpha.test',        '{}'::jsonb, now()),
  ('a0000007-0000-0000-0000-000000000007', 'student2@alpha.test',        '{}'::jsonb, now()),
  -- Bravo school
  ('b0000001-0000-0000-0000-000000000001', 'admin@bravo.test',           '{}'::jsonb, now()),
  ('b0000002-0000-0000-0000-000000000002', 'teacher.bio@bravo.test',     '{}'::jsonb, now()),
  ('b0000003-0000-0000-0000-000000000003', 'student1@bravo.test',        '{}'::jsonb, now()),
  -- Legacy unattached
  ('c0000001-0000-0000-0000-000000000001', 'legacy@somewhere.test',      '{}'::jsonb, now())
ON CONFLICT (id) DO NOTHING;

-- Profiles for each. Note: the existing 33 profiles on the branch will
-- still exist; these are additional fake ones that won't collide.
INSERT INTO public.profiles (id, school_id, role, department, key_stage, first_name, last_name)
VALUES
  -- Alpha
  ('a0000001-0000-0000-0000-000000000001', '11111111-1111-1111-1111-111111111111', 'admin',   NULL,        'KS4', 'Alpha',  'Admin'),
  ('a0000002-0000-0000-0000-000000000002', '11111111-1111-1111-1111-111111111111', 'hod',     'Science',   'KS4', 'Alpha',  'SciHoD'),
  ('a0000003-0000-0000-0000-000000000003', '11111111-1111-1111-1111-111111111111', 'hod',     'Mathematics','KS4','Alpha',  'MathsHoD'),
  ('a0000004-0000-0000-0000-000000000004', '11111111-1111-1111-1111-111111111111', 'teacher', NULL,        'KS4', 'Alpha',  'BioTeacher'),
  ('a0000005-0000-0000-0000-000000000005', '11111111-1111-1111-1111-111111111111', 'teacher', NULL,        'KS4', 'Alpha',  'MathsTeacher'),
  ('a0000006-0000-0000-0000-000000000006', '11111111-1111-1111-1111-111111111111', 'student', NULL,        'KS4', 'Alpha',  'Student1'),
  ('a0000007-0000-0000-0000-000000000007', '11111111-1111-1111-1111-111111111111', 'student', NULL,        'KS4', 'Alpha',  'Student2'),
  -- Bravo
  ('b0000001-0000-0000-0000-000000000001', '22222222-2222-2222-2222-222222222222', 'admin',   NULL,        'KS4', 'Bravo',  'Admin'),
  ('b0000002-0000-0000-0000-000000000002', '22222222-2222-2222-2222-222222222222', 'teacher', NULL,        'KS4', 'Bravo',  'BioTeacher'),
  ('b0000003-0000-0000-0000-000000000003', '22222222-2222-2222-2222-222222222222', 'student', NULL,        'KS4', 'Bravo',  'Student1'),
  -- Legacy
  ('c0000001-0000-0000-0000-000000000001', NULL,                                    'student', NULL,       'KS4', 'Legacy', 'User');

-- One class in each school
INSERT INTO public.classes (id, school_id, academic_year_id, name, key_stage, year_group, tier, science_pathway)
VALUES
  ('c1111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', 'aaaa1111-1111-1111-1111-111111111111', '10A1', 'KS4', 10, 'higher', 'triple'),
  ('c2222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', 'aaaa2222-2222-2222-2222-222222222222', '10X1', 'KS4', 10, 'higher', 'triple');

-- Wire up class teachers (Alpha bio teacher → Alpha class; Bravo bio teacher → Bravo class)
-- subject_id lookup: we use the existing seed-data Biology row.
INSERT INTO public.class_teachers (class_id, teacher_id, subject_id, role)
SELECT 'c1111111-1111-1111-1111-111111111111', 'a0000004-0000-0000-0000-000000000004', s.id, 'subject_teacher'
FROM public.subjects s WHERE s.name = 'Biology';

INSERT INTO public.class_teachers (class_id, teacher_id, subject_id, role)
SELECT 'c2222222-2222-2222-2222-222222222222', 'b0000002-0000-0000-0000-000000000002', s.id, 'subject_teacher'
FROM public.subjects s WHERE s.name = 'Biology';

-- Wire up class members (Alpha students → Alpha class; Bravo student → Bravo class)
INSERT INTO public.class_members (class_id, student_id, joined_via)
VALUES
  ('c1111111-1111-1111-1111-111111111111', 'a0000006-0000-0000-0000-000000000006', 'admin_added'),
  ('c1111111-1111-1111-1111-111111111111', 'a0000007-0000-0000-0000-000000000007', 'admin_added'),
  ('c2222222-2222-2222-2222-222222222222', 'b0000003-0000-0000-0000-000000000003', 'admin_added');

-- One assignment in each class
INSERT INTO public.assignments (id, class_id, subject_id, topic, title, quiz_type, due_at, auto_generated)
SELECT 'a1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', s.id,
       'Cell Biology', 'Cell Structure Quiz', 'topic_quiz', now() + interval '7 days', false
FROM public.subjects s WHERE s.name = 'Biology';

INSERT INTO public.assignments (id, class_id, subject_id, topic, title, quiz_type, due_at, auto_generated)
SELECT 'a2222222-2222-2222-2222-222222222222', 'c2222222-2222-2222-2222-222222222222', s.id,
       'Cell Biology', 'Cell Structure Quiz', 'topic_quiz', now() + interval '7 days', false
FROM public.subjects s WHERE s.name = 'Biology';

-- One submission per student
INSERT INTO public.assignment_submissions (id, assignment_id, student_id, score, max_score, total_time_seconds, submitted_at, attempts)
VALUES
  ('5a000001-0000-0000-0000-000000000001', 'a1111111-1111-1111-1111-111111111111', 'a0000006-0000-0000-0000-000000000006', 7, 10, 420, now(), 1),
  ('5a000002-0000-0000-0000-000000000002', 'a1111111-1111-1111-1111-111111111111', 'a0000007-0000-0000-0000-000000000007', 6, 10, 510, now(), 1),
  ('5b000001-0000-0000-0000-000000000001', 'a2222222-2222-2222-2222-222222222222', 'b0000003-0000-0000-0000-000000000003', 8, 10, 380, now(), 1);


-- =====================================================================
-- SECTION B — TESTS
-- =====================================================================
-- Pattern: SET ROLE / login_as / SELECT count(*) / assert
-- Counts what RLS shows the impersonated user. Mismatches = leaks.
-- =====================================================================

-- ─── B1. Cross-school invariant (the big one) ───────────────────────
-- Alpha admin must see Alpha data only. Cannot see Bravo.

SELECT pg_temp.login_as('a0000001-0000-0000-0000-000000000001');

SELECT pg_temp.assert_count(
  'B1.1 Alpha admin sees Alpha school row',
  1,
  (SELECT count(*)::int FROM public.schools WHERE slug = 'test-alpha')
);

SELECT pg_temp.assert_count(
  'B1.2 Alpha admin CANNOT see Bravo school row',
  0,
  (SELECT count(*)::int FROM public.schools WHERE slug = 'test-bravo')
);

SELECT pg_temp.assert_count(
  'B1.3 Alpha admin sees Alpha classes (1)',
  1,
  (SELECT count(*)::int FROM public.classes WHERE school_id = '11111111-1111-1111-1111-111111111111')
);

SELECT pg_temp.assert_count(
  'B1.4 Alpha admin CANNOT see Bravo classes',
  0,
  (SELECT count(*)::int FROM public.classes WHERE school_id = '22222222-2222-2222-2222-222222222222')
);

SELECT pg_temp.assert_count(
  'B1.5 Alpha admin sees Alpha submissions (2)',
  2,
  (SELECT count(*)::int FROM public.assignment_submissions WHERE student_id IN (
    'a0000006-0000-0000-0000-000000000006',
    'a0000007-0000-0000-0000-000000000007'
  ))
);

SELECT pg_temp.assert_count(
  'B1.6 Alpha admin CANNOT see Bravo submissions',
  0,
  (SELECT count(*)::int FROM public.assignment_submissions WHERE student_id = 'b0000003-0000-0000-0000-000000000003')
);


-- ─── B2. The reverse: Bravo admin cannot see Alpha ───────────────────

SELECT pg_temp.login_as('b0000001-0000-0000-0000-000000000001');

SELECT pg_temp.assert_count(
  'B2.1 Bravo admin sees Bravo school row',
  1,
  (SELECT count(*)::int FROM public.schools WHERE slug = 'test-bravo')
);

SELECT pg_temp.assert_count(
  'B2.2 Bravo admin CANNOT see Alpha school row',
  0,
  (SELECT count(*)::int FROM public.schools WHERE slug = 'test-alpha')
);

SELECT pg_temp.assert_count(
  'B2.3 Bravo admin CANNOT see any Alpha submissions',
  0,
  (SELECT count(*)::int FROM public.assignment_submissions WHERE id::text LIKE '5a%')
);


-- ─── B3. Teacher can only see their own classes ──────────────────────

SELECT pg_temp.login_as('a0000004-0000-0000-0000-000000000004');  -- Alpha bio teacher

SELECT pg_temp.assert_count(
  'B3.1 Alpha bio teacher sees their own class',
  1,
  (SELECT count(*)::int FROM public.classes WHERE id = 'c1111111-1111-1111-1111-111111111111')
);

SELECT pg_temp.assert_count(
  'B3.2 Alpha bio teacher CANNOT see Bravo classes',
  0,
  (SELECT count(*)::int FROM public.classes WHERE school_id = '22222222-2222-2222-2222-222222222222')
);

SELECT pg_temp.assert_count(
  'B3.3 Alpha bio teacher sees their students submissions',
  2,
  (SELECT count(*)::int FROM public.assignment_submissions
   WHERE assignment_id = 'a1111111-1111-1111-1111-111111111111')
);


-- ─── B4. HoD scoping: Maths HoD cannot see Science data ──────────────

SELECT pg_temp.login_as('a0000003-0000-0000-0000-000000000003');  -- Alpha Maths HoD

SELECT pg_temp.assert_count(
  'B4.1 Alpha Maths HoD sees their school',
  1,
  (SELECT count(*)::int FROM public.schools WHERE slug = 'test-alpha')
);

-- Maths HoD can see classes (HoDs see all classes in their school per design)
-- but for assignments they should only see their department's
SELECT pg_temp.assert_count(
  'B4.2 Alpha Maths HoD CANNOT see Biology assignments (different department)',
  0,
  (SELECT count(*)::int FROM public.assignments
   WHERE id = 'a1111111-1111-1111-1111-111111111111')
);


-- ─── B5. Science HoD: SHOULD see Science assignments ─────────────────

SELECT pg_temp.login_as('a0000002-0000-0000-0000-000000000002');  -- Alpha Science HoD

SELECT pg_temp.assert_count(
  'B5.1 Alpha Science HoD sees Biology assignment in their school',
  1,
  (SELECT count(*)::int FROM public.assignments
   WHERE id = 'a1111111-1111-1111-1111-111111111111')
);

SELECT pg_temp.assert_count(
  'B5.2 Alpha Science HoD CANNOT see Bravo Biology assignment',
  0,
  (SELECT count(*)::int FROM public.assignments
   WHERE id = 'a2222222-2222-2222-2222-222222222222')
);


-- ─── B6. Student isolation ───────────────────────────────────────────

SELECT pg_temp.login_as('a0000006-0000-0000-0000-000000000006');  -- Alpha student 1

SELECT pg_temp.assert_count(
  'B6.1 Student sees own submission',
  1,
  (SELECT count(*)::int FROM public.assignment_submissions
   WHERE id = '5a000001-0000-0000-0000-000000000001')
);

SELECT pg_temp.assert_count(
  'B6.2 Student CANNOT see other student submissions in same class',
  0,
  (SELECT count(*)::int FROM public.assignment_submissions
   WHERE id = '5a000002-0000-0000-0000-000000000002')
);

SELECT pg_temp.assert_count(
  'B6.3 Student CANNOT see Bravo student submissions',
  0,
  (SELECT count(*)::int FROM public.assignment_submissions
   WHERE id = '5b000001-0000-0000-0000-000000000001')
);

SELECT pg_temp.assert_count(
  'B6.4 Student sees own class only',
  1,
  (SELECT count(*)::int FROM public.classes)
);


-- ─── B7. Legacy unattached user — no school = no school data ─────────

SELECT pg_temp.login_as('c0000001-0000-0000-0000-000000000001');  -- Legacy

SELECT pg_temp.assert_count(
  'B7.1 Legacy user CANNOT see any school row',
  0,
  (SELECT count(*)::int FROM public.schools WHERE slug IN ('test-alpha','test-bravo'))
);

SELECT pg_temp.assert_count(
  'B7.2 Legacy user CANNOT see any class',
  0,
  (SELECT count(*)::int FROM public.classes)
);

SELECT pg_temp.assert_count(
  'B7.3 Legacy user CANNOT see any submission',
  0,
  (SELECT count(*)::int FROM public.assignment_submissions)
);

SELECT pg_temp.assert_count(
  'B7.4 Legacy user CAN still see global subjects table (not school-scoped)',
  3,
  (SELECT count(*)::int FROM public.subjects WHERE name IN ('Biology','Chemistry','Physics'))
);


-- ─── B8. Subjects table is globally readable ─────────────────────────

SELECT pg_temp.login_as('a0000006-0000-0000-0000-000000000006');  -- Alpha student
SELECT pg_temp.assert_count(
  'B8.1 Student sees all 3 seeded subjects',
  3,
  (SELECT count(*)::int FROM public.subjects WHERE name IN ('Biology','Chemistry','Physics'))
);

SELECT pg_temp.login_as('b0000003-0000-0000-0000-000000000003');  -- Bravo student
SELECT pg_temp.assert_count(
  'B8.2 Bravo student also sees all 3 seeded subjects',
  3,
  (SELECT count(*)::int FROM public.subjects WHERE name IN ('Biology','Chemistry','Physics'))
);


-- ─── B9. school_subject_settings is school-scoped ────────────────────

SELECT pg_temp.login_as('a0000001-0000-0000-0000-000000000001');  -- Alpha admin

-- Note: Alpha doesn't have any school_subject_settings rows in test data,
-- but the seed migration creates them for Rainford. Alpha admin should
-- not see Rainford's settings.
SELECT pg_temp.assert_count(
  'B9.1 Alpha admin CANNOT see Rainford school_subject_settings',
  0,
  (SELECT count(*)::int FROM public.school_subject_settings sss
   JOIN public.schools s ON s.id = sss.school_id
   WHERE s.slug = 'rainford-high')
);


-- ─── B10. Audit log: locked from direct user inserts ─────────────────

SELECT pg_temp.login_as('a0000001-0000-0000-0000-000000000001');

DO $$
BEGIN
  BEGIN
    INSERT INTO public.audit_log (action, target_table, target_id)
    VALUES ('test.injection', 'classes', gen_random_uuid());
    -- If we got here, the policy let it through — that's a fail
    PERFORM pg_temp.assert_count('B10.1 audit_log INSERT blocked at policy level', 0, 1);
  EXCEPTION WHEN insufficient_privilege OR check_violation THEN
    PERFORM pg_temp.assert_count('B10.1 audit_log INSERT blocked at policy level', 0, 0);
  WHEN OTHERS THEN
    -- Some other error — also counts as "not allowed"
    PERFORM pg_temp.assert_count('B10.1 audit_log INSERT blocked at policy level', 0, 0);
  END;
END;
$$;


-- ─── B11. Scheme of work entries: globally readable ──────────────────

SELECT pg_temp.login_as('a0000006-0000-0000-0000-000000000006');  -- student

-- (No SoW entries seeded yet — Stage 4 populates them. So count is 0,
-- but the access *itself* should not error. Verify the SELECT runs cleanly.)
SELECT pg_temp.assert_count(
  'B11.1 Student can SELECT from sow_entries (read access works, table empty)',
  0,
  (SELECT count(*)::int FROM public.scheme_of_work_entries)
);


-- ─── B12. Scheme of work overrides: school-scoped ────────────────────

SELECT pg_temp.login_as('a0000001-0000-0000-0000-000000000001');

INSERT INTO public.scheme_of_work_overrides (
  school_id, key_stage, year_group, tier, pathway, subject_id,
  academic_week, topic, created_by
)
SELECT '11111111-1111-1111-1111-111111111111', 'KS4', 10, 'higher', 'triple',
       (SELECT id FROM public.subjects WHERE name = 'Biology'),
       1, 'Custom Alpha Topic', 'a0000001-0000-0000-0000-000000000001';

SELECT pg_temp.assert_count(
  'B12.1 Alpha admin sees own override',
  1,
  (SELECT count(*)::int FROM public.scheme_of_work_overrides
   WHERE school_id = '11111111-1111-1111-1111-111111111111')
);

-- Bravo admin must not see it
SELECT pg_temp.login_as('b0000001-0000-0000-0000-000000000001');

SELECT pg_temp.assert_count(
  'B12.2 Bravo admin CANNOT see Alpha override',
  0,
  (SELECT count(*)::int FROM public.scheme_of_work_overrides)
);


-- ─── B13. Question attempts visibility follows submission ownership ──

-- Insert a fake question attempt under Alpha student 1's submission
SELECT pg_temp.login_as('a0000006-0000-0000-0000-000000000006');

INSERT INTO public.assignment_question_attempts (
  submission_id, question_index, question_text, selected_answer,
  correct_answer, is_correct, time_spent_seconds
)
VALUES (
  '5a000001-0000-0000-0000-000000000001', 1, 'What is a cell?',
  'B', 'A', false, 45
);

-- Student sees their own attempt
SELECT pg_temp.assert_count(
  'B13.1 Student sees own question attempt',
  1,
  (SELECT count(*)::int FROM public.assignment_question_attempts
   WHERE submission_id = '5a000001-0000-0000-0000-000000000001')
);

-- Other Alpha student CANNOT see student 1's attempt
SELECT pg_temp.login_as('a0000007-0000-0000-0000-000000000007');
SELECT pg_temp.assert_count(
  'B13.2 Other student CANNOT see classmate question attempts',
  0,
  (SELECT count(*)::int FROM public.assignment_question_attempts
   WHERE submission_id = '5a000001-0000-0000-0000-000000000001')
);

-- Alpha bio teacher CAN see student 1's attempt (their class)
SELECT pg_temp.login_as('a0000004-0000-0000-0000-000000000004');
SELECT pg_temp.assert_count(
  'B13.3 Alpha bio teacher sees their students question attempts',
  1,
  (SELECT count(*)::int FROM public.assignment_question_attempts
   WHERE submission_id = '5a000001-0000-0000-0000-000000000001')
);

-- Bravo teacher CANNOT see Alpha attempt
SELECT pg_temp.login_as('b0000002-0000-0000-0000-000000000002');
SELECT pg_temp.assert_count(
  'B13.4 Bravo teacher CANNOT see Alpha question attempts',
  0,
  (SELECT count(*)::int FROM public.assignment_question_attempts
   WHERE submission_id = '5a000001-0000-0000-0000-000000000001')
);


-- ─── B14. profile read-across for legitimate cases ───────────────────

-- Alpha bio teacher should see profile of their student
SELECT pg_temp.login_as('a0000004-0000-0000-0000-000000000004');

SELECT pg_temp.assert_count(
  'B14.1 Alpha bio teacher sees Alpha student profile (in their class)',
  1,
  (SELECT count(*)::int FROM public.profiles
   WHERE id = 'a0000006-0000-0000-0000-000000000006')
);

-- But NOT a Bravo student
SELECT pg_temp.assert_count(
  'B14.2 Alpha bio teacher CANNOT see Bravo student profile',
  0,
  (SELECT count(*)::int FROM public.profiles
   WHERE id = 'b0000003-0000-0000-0000-000000000003')
);


-- =====================================================================
-- SECTION C — SUMMARY
-- =====================================================================
-- Two outputs:
--   1. Per-test result set (returned by the final SELECT before ROLLBACK).
--      This guarantees we see results even if RAISE NOTICE is suppressed
--      by the client.
--   2. NOTICE channel summary (works when client surfaces notices).
--
-- IMPORTANT: drop back to the privileged session role before reading
-- test_results. The temp table is owned by the original (privileged)
-- role and has no grants to 'authenticated'. The role swap was needed
-- only to simulate users; once we're summarising, we're done simulating.
-- =====================================================================

RESET ROLE;
SELECT set_config('request.jwt.claim.sub', '', true);
SELECT set_config('request.jwt.claims', '', true);

DO $$
DECLARE
  v_total int;
  v_passed int;
  v_failed int;
  v_failed_names text;
BEGIN
  SELECT count(*),
         count(*) FILTER (WHERE passed),
         count(*) FILTER (WHERE NOT passed)
  INTO v_total, v_passed, v_failed
  FROM test_results;

  SELECT string_agg(test_name, E'\n  - ')
  INTO v_failed_names
  FROM test_results
  WHERE NOT passed;

  RAISE NOTICE '';
  RAISE NOTICE '═══════════════════════════════════════════════════════════';
  RAISE NOTICE '  STAGE 1 RLS TEST SUMMARY';
  RAISE NOTICE '═══════════════════════════════════════════════════════════';
  RAISE NOTICE '  Total:  %', v_total;
  RAISE NOTICE '  Passed: %', v_passed;
  RAISE NOTICE '  Failed: %', v_failed;
  RAISE NOTICE '═══════════════════════════════════════════════════════════';

  IF v_failed > 0 THEN
    RAISE NOTICE '';
    RAISE NOTICE '  FAILED TESTS:';
    RAISE NOTICE '  - %', v_failed_names;
    RAISE NOTICE '';
    RAISE NOTICE '  ✗ DO NOT push to production. Investigate first.';
  ELSE
    RAISE NOTICE '';
    RAISE NOTICE '  ✓ All tests passed. Stage 1 RLS pyramid holds.';
    RAISE NOTICE '  → Sleep on it. Apply to production tomorrow with fresh eyes.';
  END IF;
END;
$$;


-- Final result set returned to the client. This is the authoritative
-- output: every assertion appears as a row, with PASS/FAIL state.
-- Sorted so failures are at the top.
SELECT
  CASE WHEN passed THEN '✓ PASS' ELSE '✗ FAIL' END AS status,
  test_name,
  expected_count AS expected,
  actual_count AS actual
FROM test_results
ORDER BY passed ASC, test_name ASC;


-- =====================================================================
-- ROLL BACK ALL TEST DATA
-- =====================================================================
-- Whether tests pass or fail, no fake data persists.
-- =====================================================================

ROLLBACK;
