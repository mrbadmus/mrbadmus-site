-- =====================================================================
-- Test Plan:    0011_mrb308_consumer_policy_matrix.sql
-- For:          MRB-308 (B2C Launch, Night 1)
-- Purpose:      Prove a family is SEALED. Every family from every other
--               family, from Rainford, and from anonymous.
-- Run on:       TEST project. Wrapped in BEGIN/ROLLBACK — nothing persists.
--
-- Why this file exists as well as 0001:
--   0001 proves the school pyramid. This proves the thing the school
--   pyramid was never asked about: that adding `parent` and two new org
--   kinds did not open a door sideways. The locked ruling is "every family
--   is sealed from every other family", and a ruling that is not asserted
--   is a ruling that drifts.
--
-- Reading this file: each row of the final result is one assertion.
-- Failures sort to the top.
-- =====================================================================

BEGIN;

CREATE TEMP TABLE test_results (
  test_name text, expected_count int, actual_count int, passed boolean
);
GRANT SELECT, INSERT ON test_results TO anon, authenticated;

CREATE OR REPLACE FUNCTION pg_temp.assert_count(test_name text, expected int, actual int)
RETURNS void LANGUAGE plpgsql SECURITY DEFINER SET search_path = pg_temp AS $$
DECLARE did_pass boolean := (expected = actual);
BEGIN
  INSERT INTO test_results VALUES (test_name, expected, actual, did_pass);
END; $$;

CREATE OR REPLACE FUNCTION pg_temp.login_as(user_id uuid) RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
  PERFORM set_config('request.jwt.claim.sub', user_id::text, true);
  PERFORM set_config('request.jwt.claims', json_build_object('sub', user_id)::text, true);
  PERFORM set_config('role', 'authenticated', true);
END; $$;

CREATE OR REPLACE FUNCTION pg_temp.logout() RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
  PERFORM set_config('request.jwt.claim.sub', '', true);
  PERFORM set_config('request.jwt.claims', '', true);
  PERFORM set_config('role', 'anon', true);
END; $$;

-- =====================================================================
-- SECTION A — BUILD TWO FAMILIES, ONE ORGANISATION, AND BORROW RAINFORD
-- =====================================================================
-- The auth users are inserted directly here (a test fixture, rolled back).
-- Production never does this: real users come from the Admin API, because
-- hand-built auth.users rows cannot actually sign in.

INSERT INTO auth.users (id, instance_id, aud, role, email, email_confirmed_at,
                        raw_app_meta_data, raw_user_meta_data, created_at, updated_at)
VALUES
 ('a0000000-0000-0000-0000-000000000001','00000000-0000-0000-0000-000000000000','authenticated','authenticated','parentA@gmail.com',    now(),'{"provider":"google"}','{}',now(),now()),
 ('a0000000-0000-0000-0000-000000000011','00000000-0000-0000-0000-000000000000','authenticated','authenticated','ca1@children.mrbadmus.internal',now(),'{"provider":"email"}','{}',now(),now()),
 ('a0000000-0000-0000-0000-000000000012','00000000-0000-0000-0000-000000000000','authenticated','authenticated','ca2@children.mrbadmus.internal',now(),'{"provider":"email"}','{}',now(),now()),
 ('b0000000-0000-0000-0000-000000000001','00000000-0000-0000-0000-000000000000','authenticated','authenticated','parentB@gmail.com',    now(),'{"provider":"google"}','{}',now(),now()),
 ('b0000000-0000-0000-0000-000000000011','00000000-0000-0000-0000-000000000000','authenticated','authenticated','cb1@children.mrbadmus.internal',now(),'{"provider":"email"}','{}',now(),now()),
 ('c0000000-0000-0000-0000-000000000001','00000000-0000-0000-0000-000000000000','authenticated','authenticated','caseworker@council.gov.uk',now(),'{"provider":"email"}','{}',now(),now()),
 ('c0000000-0000-0000-0000-000000000011','00000000-0000-0000-0000-000000000000','authenticated','authenticated','pc1@children.mrbadmus.internal',now(),'{"provider":"email"}','{}',now(),now());

UPDATE public.profiles SET first_name='ParentA' WHERE id='a0000000-0000-0000-0000-000000000001';
UPDATE public.profiles SET first_name='ParentB' WHERE id='b0000000-0000-0000-0000-000000000001';

-- Families made by the REAL function, so the matrix tests what ships.
SELECT public.create_family_for_parent('a0000000-0000-0000-0000-000000000001','Family Alpha') AS id
  INTO TEMP fam_a_t;
SELECT public.create_family_for_parent('b0000000-0000-0000-0000-000000000001','Family Bravo') AS id
  INTO TEMP fam_b_t;

SELECT public.attach_child_to_family('a0000000-0000-0000-0000-000000000011','a0000000-0000-0000-0000-000000000001','Ada',   8, 'MatrixAdaOne',  'home_education','full','AQA');
SELECT public.attach_child_to_family('a0000000-0000-0000-0000-000000000012','a0000000-0000-0000-0000-000000000001','Bea',  10, 'MatrixBeaTwo',  'alongside_school','light','AQA','higher','triple');
SELECT public.attach_child_to_family('b0000000-0000-0000-0000-000000000011','b0000000-0000-0000-0000-000000000001','Cal',   9, 'MatrixCalThree','alongside_school','steady','AQA');

-- An organisation-kind org (a council). Staff are caseworkers: ordinary
-- teachers by role, with no school_admin scope, so they must NOT see billing.
INSERT INTO public.schools (id, name, code, kind, show_on_public_leaderboard, email_domains, departments)
VALUES ('cc000000-0000-0000-0000-0000000000cc','Test Council','COUNCILTEST','organisation', false, '{}', ARRAY['Science']);

INSERT INTO public.academic_years (id, school_id, name, start_date, end_date, is_current)
VALUES ('cc000000-0000-0000-0000-00000000ac01','cc000000-0000-0000-0000-0000000000cc','2026-27','2026-09-01','2027-08-31',true);

UPDATE public.profiles SET role='teacher', school_id='cc000000-0000-0000-0000-0000000000cc', first_name='Case'
 WHERE id='c0000000-0000-0000-0000-000000000001';

INSERT INTO public.classes (id, school_id, academic_year_id, name, key_stage, year_group)
VALUES ('cc000000-0000-0000-0000-00000000c101','cc000000-0000-0000-0000-0000000000cc','cc000000-0000-0000-0000-00000000ac01','Pupil One','KS3',8);

UPDATE public.profiles SET role='student', school_id='cc000000-0000-0000-0000-0000000000cc',
       key_stage='KS3', year_group='8', tier=NULL, science_pathway=NULL, first_name='Pip'
 WHERE id='c0000000-0000-0000-0000-000000000011';

INSERT INTO public.class_members (class_id, student_id, joined_via)
VALUES ('cc000000-0000-0000-0000-00000000c101','c0000000-0000-0000-0000-000000000011','admin_added');
INSERT INTO public.class_teachers (class_id, teacher_id, subject_id, role)
VALUES ('cc000000-0000-0000-0000-00000000c101','c0000000-0000-0000-0000-000000000001',NULL,'form_tutor');

INSERT INTO public.subscriptions (org_id, status, seat_cap, current_period_end)
VALUES ('cc000000-0000-0000-0000-0000000000cc','active', 20, now() + interval '300 days');

-- =====================================================================
-- SECTION B — THE MATRIX
-- =====================================================================
DO $$
DECLARE
  fam_a uuid; fam_b uuid;
  r_teacher uuid; r_student uuid;
  pa uuid := 'a0000000-0000-0000-0000-000000000001';
  pb uuid := 'b0000000-0000-0000-0000-000000000001';
  ca1 uuid := 'a0000000-0000-0000-0000-000000000011';
  sc uuid := 'c0000000-0000-0000-0000-000000000001';
  cc uuid := 'cc000000-0000-0000-0000-0000000000cc';
BEGIN
  SELECT id INTO fam_a FROM fam_a_t;
  SELECT id INTO fam_b FROM fam_b_t;
  SELECT id INTO r_teacher FROM public.profiles
    WHERE role='teacher' AND school_id=(SELECT id FROM public.schools WHERE code='RHS') LIMIT 1;
  SELECT id INTO r_student FROM public.profiles
    WHERE role='student' AND school_id=(SELECT id FROM public.schools WHERE code='RHS') LIMIT 1;

  -- ---------- PARENT A, inside their own family ----------
  PERFORM pg_temp.login_as(pa);
  PERFORM pg_temp.assert_count('PA sees exactly 1 school (own family)', 1,
    (SELECT count(*)::int FROM public.schools));
  PERFORM pg_temp.assert_count('PA sees own 3 profiles (self + 2 children)', 3,
    (SELECT count(*)::int FROM public.profiles));
  PERFORM pg_temp.assert_count('PA sees own 2 classes', 2,
    (SELECT count(*)::int FROM public.classes));
  PERFORM pg_temp.assert_count('PA sees own 2 class_members', 2,
    (SELECT count(*)::int FROM public.class_members));
  PERFORM pg_temp.assert_count('PA sees own 1 subscription', 1,
    (SELECT count(*)::int FROM public.subscriptions));

  -- ---------- PARENT A, reaching for family B ----------
  PERFORM pg_temp.assert_count('PA sees 0 of family B profiles', 0,
    (SELECT count(*)::int FROM public.profiles WHERE school_id = fam_b));
  PERFORM pg_temp.assert_count('PA sees 0 of family B classes', 0,
    (SELECT count(*)::int FROM public.classes WHERE school_id = fam_b));
  PERFORM pg_temp.assert_count('PA sees 0 of family B subscription', 0,
    (SELECT count(*)::int FROM public.subscriptions WHERE org_id = fam_b));
  PERFORM pg_temp.assert_count('PA sees 0 of family B school row', 0,
    (SELECT count(*)::int FROM public.schools WHERE id = fam_b));
  PERFORM pg_temp.assert_count('PA sees 0 Rainford profiles', 0,
    (SELECT count(*)::int FROM public.profiles p JOIN public.schools s ON s.id=p.school_id WHERE s.code='RHS'));
  PERFORM pg_temp.assert_count('PA sees 0 council profiles', 0,
    (SELECT count(*)::int FROM public.profiles WHERE school_id = cc));

  -- ---------- PARENT A cannot write billing ----------
  BEGIN
    UPDATE public.subscriptions SET status='active', comped_until = now() + interval '10 years'
     WHERE org_id = fam_a;
    PERFORM pg_temp.assert_count('PA UPDATE of own subscription is refused', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA UPDATE of own subscription is refused', 1, 1);
  END;
  BEGIN
    INSERT INTO public.subscriptions (org_id, status) VALUES (fam_b, 'active');
    PERFORM pg_temp.assert_count('PA INSERT of a subscription is refused', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA INSERT of a subscription is refused', 1, 1);
  END;

  -- ---------- PARENT B ----------
  PERFORM pg_temp.login_as(pb);
  PERFORM pg_temp.assert_count('PB sees own 2 profiles (self + 1 child)', 2,
    (SELECT count(*)::int FROM public.profiles));
  PERFORM pg_temp.assert_count('PB sees own 1 class', 1,
    (SELECT count(*)::int FROM public.classes));
  PERFORM pg_temp.assert_count('PB sees 0 of family A profiles', 0,
    (SELECT count(*)::int FROM public.profiles WHERE school_id = fam_a));
  PERFORM pg_temp.assert_count('PB sees 0 of family A subscription', 0,
    (SELECT count(*)::int FROM public.subscriptions WHERE org_id = fam_a));

  -- ---------- CHILD in family A ----------
  PERFORM pg_temp.login_as(ca1);
  PERFORM pg_temp.assert_count('Child sees only self in profiles (not sibling, not parent)', 1,
    (SELECT count(*)::int FROM public.profiles));
  PERFORM pg_temp.assert_count('Child sees only own 1 class', 1,
    (SELECT count(*)::int FROM public.classes));
  PERFORM pg_temp.assert_count('Child sees 0 subscriptions (not an admin)', 0,
    (SELECT count(*)::int FROM public.subscriptions));
  PERFORM pg_temp.assert_count('Child sees own family school row only', 1,
    (SELECT count(*)::int FROM public.schools));
  PERFORM pg_temp.assert_count('Child sees 0 of family B anything', 0,
    (SELECT count(*)::int FROM public.profiles WHERE school_id = fam_b));

  -- ---------- ORGANISATION STAFF ----------
  PERFORM pg_temp.login_as(sc);
  PERFORM pg_temp.assert_count('Org staff sees self + taught pupil', 2,
    (SELECT count(*)::int FROM public.profiles));
  PERFORM pg_temp.assert_count('Org staff sees 0 subscriptions (no school_admin scope)', 0,
    (SELECT count(*)::int FROM public.subscriptions));
  PERFORM pg_temp.assert_count('Org staff sees 0 family A profiles', 0,
    (SELECT count(*)::int FROM public.profiles WHERE school_id = fam_a));

  -- ---------- RAINFORD TEACHER — must not see consumers ----------
  IF r_teacher IS NOT NULL THEN
    PERFORM pg_temp.login_as(r_teacher);
    PERFORM pg_temp.assert_count('Rainford teacher sees 0 family A profiles', 0,
      (SELECT count(*)::int FROM public.profiles WHERE school_id = fam_a));
    PERFORM pg_temp.assert_count('Rainford teacher sees 0 family classes', 0,
      (SELECT count(*)::int FROM public.classes WHERE school_id IN (fam_a, fam_b)));
    PERFORM pg_temp.assert_count('Rainford teacher sees 0 subscriptions', 0,
      (SELECT count(*)::int FROM public.subscriptions));
    PERFORM pg_temp.assert_count('Rainford teacher sees 0 consumer school rows', 0,
      (SELECT count(*)::int FROM public.schools WHERE kind <> 'school'));
  END IF;

  -- ---------- RAINFORD STUDENT ----------
  IF r_student IS NOT NULL THEN
    PERFORM pg_temp.login_as(r_student);
    PERFORM pg_temp.assert_count('Rainford student sees 0 family profiles', 0,
      (SELECT count(*)::int FROM public.profiles WHERE school_id IN (fam_a, fam_b)));
    PERFORM pg_temp.assert_count('Rainford student sees 0 subscriptions', 0,
      (SELECT count(*)::int FROM public.subscriptions));
  END IF;

  -- ---------- ANONYMOUS ----------
  PERFORM pg_temp.logout();
  PERFORM pg_temp.assert_count('Anon sees 0 schools', 0, (SELECT count(*)::int FROM public.schools));
  PERFORM pg_temp.assert_count('Anon sees 0 profiles', 0, (SELECT count(*)::int FROM public.profiles));
  PERFORM pg_temp.assert_count('Anon sees 0 classes', 0, (SELECT count(*)::int FROM public.classes));
  PERFORM pg_temp.assert_count('Anon sees 0 subscriptions', 0, (SELECT count(*)::int FROM public.subscriptions));
  PERFORM pg_temp.assert_count('Anon sees 0 class_members', 0, (SELECT count(*)::int FROM public.class_members));

  PERFORM set_config('role','postgres',true);
END $$;

-- =====================================================================
-- SECTION C — ENTITLEMENT TRUTH TABLE
-- =====================================================================
DO $$
DECLARE fam_a uuid; cc uuid := 'cc000000-0000-0000-0000-0000000000cc';
BEGIN
  SELECT id INTO fam_a FROM fam_a_t;

  PERFORM pg_temp.assert_count('school kind is entitled with no subscription row', 1,
    (SELECT public.org_is_entitled(id)::int FROM public.schools WHERE code='RHS'));

  UPDATE public.subscriptions SET status='trialing' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family trialing => entitled', 1, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='active' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family active => entitled', 1, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='canceled' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family canceled => NOT entitled', 0, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='locked' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family locked => NOT entitled', 0, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='comped', comped_until = now() + interval '30 days' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family comped, future => entitled', 1, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='comped', comped_until = now() - interval '1 day' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family comped, expired => NOT entitled', 0, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='past_due', comped_until=NULL,
         current_period_end = now() - interval '2 days' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family past_due inside 7-day grace => entitled', 1, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET current_period_end = now() - interval '8 days' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family past_due beyond grace => NOT entitled', 0, public.org_is_entitled(fam_a)::int);

  UPDATE public.subscriptions SET status='active' WHERE org_id=fam_a;
  UPDATE public.subscriptions SET deleted_at = now() WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family with soft-deleted subscription => NOT entitled', 0, public.org_is_entitled(fam_a)::int);
  UPDATE public.subscriptions SET deleted_at = NULL WHERE org_id=fam_a;

  PERFORM pg_temp.assert_count('organisation with seat cap + future period => entitled', 1, public.org_is_entitled(cc)::int);
  UPDATE public.subscriptions SET seat_cap = NULL WHERE org_id=cc;
  PERFORM pg_temp.assert_count('organisation with no seat cap => NOT entitled', 0, public.org_is_entitled(cc)::int);
  UPDATE public.subscriptions SET seat_cap = 20, current_period_end = now() - interval '1 day' WHERE org_id=cc;
  PERFORM pg_temp.assert_count('organisation with expired period => NOT entitled', 0, public.org_is_entitled(cc)::int);
END $$;

-- =====================================================================
-- SECTION D — STRUCTURAL GUARANTEES
-- =====================================================================
DO $$
DECLARE fam_a uuid;
BEGIN
  SELECT id INTO fam_a FROM fam_a_t;

  PERFORM pg_temp.assert_count('family org is off the public leaderboard', 1,
    (SELECT count(*)::int FROM public.schools WHERE id=fam_a AND show_on_public_leaderboard = false));

  BEGIN
    INSERT INTO public.schools (name, code, kind, show_on_public_leaderboard)
    VALUES ('Leaky family','LEAK','family', true);
    PERFORM pg_temp.assert_count('a public-facing family org cannot be created', 1, 0);
  EXCEPTION WHEN check_violation THEN
    PERFORM pg_temp.assert_count('a public-facing family org cannot be created', 1, 1);
  END;

  PERFORM pg_temp.assert_count('parent holds school_admin in own family only', 1,
    (SELECT count(*)::int FROM public.staff_scopes
      WHERE profile_id='a0000000-0000-0000-0000-000000000001' AND scope='school_admin' AND school_id=fam_a));

  PERFORM pg_temp.assert_count('KS3 child carries no tier and no pathway', 1,
    (SELECT count(*)::int FROM public.profiles
      WHERE username='MatrixAdaOne' AND tier IS NULL AND science_pathway IS NULL AND key_stage='KS3'));

  PERFORM pg_temp.assert_count('KS4 child carries tier and pathway', 1,
    (SELECT count(*)::int FROM public.profiles
      WHERE username='MatrixBeaTwo' AND tier='higher' AND science_pathway='triple' AND key_stage='KS4'));

  PERFORM pg_temp.assert_count('each child has exactly one class', 2,
    (SELECT count(*)::int FROM public.classes WHERE school_id=fam_a));

  PERFORM pg_temp.assert_count('consumer signup flag is OFF by default', 1,
    (SELECT count(*)::int FROM public.platform_flags
      WHERE key='consumer_signup_enabled' AND enabled = false));
END $$;

-- =====================================================================
-- RESULTS
-- =====================================================================
SELECT CASE WHEN passed THEN 'PASS' ELSE 'FAIL' END AS status,
       test_name, expected_count AS expected, actual_count AS actual
FROM test_results ORDER BY passed ASC, test_name ASC;

ROLLBACK;
