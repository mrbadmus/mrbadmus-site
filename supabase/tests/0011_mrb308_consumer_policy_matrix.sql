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

  -- ⊕ MRB-309: a trial is entitled only while trial_end is ahead. The
  -- Night 1 row here set status alone, which is now a stale trial.
  UPDATE public.subscriptions SET status='trialing', trial_end = now() + interval '5 days' WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family trialing (future trial_end) => entitled', 1, public.org_is_entitled(fam_a)::int);
  UPDATE public.subscriptions SET status='trialing', trial_end = NULL WHERE org_id=fam_a;
  PERFORM pg_temp.assert_count('family trialing with no trial_end => NOT entitled (MRB-309)', 0, public.org_is_entitled(fam_a)::int);

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

  -- ⚠️ This deliberately does NOT read the live value of
  -- consumer_signup_enabled, though that is the obvious thing to assert.
  -- That value is a LIVE SWITCH: anyone driving a consumer flow against this
  -- sandbox turns it on for the length of their run, and an assertion that
  -- reads it goes red for a reason that has nothing to do with the code under
  -- test. It did exactly that during the night-1 build, and a gate that cries
  -- wolf gets ignored, which is worse than not having it.
  --
  -- The guarantee worth holding is that a flag is BORN OFF — that switching
  -- consumer signup on is always a deliberate act and never a default. So a
  -- fresh row is inserted inside this rolled-back transaction and read back,
  -- which is deterministic whatever the live switch happens to be doing.
  INSERT INTO public.platform_flags (key) VALUES ('mrb308_probe_flag');
  PERFORM pg_temp.assert_count('a new platform flag is born disabled', 1,
    (SELECT count(*)::int FROM public.platform_flags
      WHERE key='mrb308_probe_flag' AND enabled = false));

  PERFORM pg_temp.assert_count('the consumer signup flag row exists at all', 1,
    (SELECT count(*)::int FROM public.platform_flags
      WHERE key='consumer_signup_enabled'));

  -- parent_owns_child, in both directions. These are here because the first
  -- version of that function never asked what the TARGET was: every clause
  -- described the parent or the org, so it answered true for a parent against
  -- themselves and for one parent against the other adult in the same family.
  -- An end-to-end drive caught it, not this file — and this file is the one
  -- that should have. Migration 20260901220658 fixed the predicate; these four
  -- rows are the matrix growing the eyes it was missing.
  PERFORM pg_temp.assert_count('parent owns their own child', 1,
    public.parent_owns_child('a0000000-0000-0000-0000-000000000001',
                             'a0000000-0000-0000-0000-000000000011')::int);

  PERFORM pg_temp.assert_count('parent does NOT own themselves', 0,
    public.parent_owns_child('a0000000-0000-0000-0000-000000000001',
                             'a0000000-0000-0000-0000-000000000001')::int);

  PERFORM pg_temp.assert_count('parent does NOT own another family''s child', 0,
    public.parent_owns_child('a0000000-0000-0000-0000-000000000001',
                             'b0000000-0000-0000-0000-000000000011')::int);

  PERFORM pg_temp.assert_count('parent B does NOT own family A''s child', 0,
    public.parent_owns_child('b0000000-0000-0000-0000-000000000001',
                             'a0000000-0000-0000-0000-000000000011')::int);
END $$;

-- =====================================================================
-- SECTION E — NIGHT 2 (MRB-309…315): access states, guardianship, chat
-- sealing, and every new table sealed the same way as the old ones.
-- =====================================================================
-- Night 1 proved the family is sealed at the schema Night 1 built. Night 2
-- added eleven tables, two helper predicates and a chat policy. Each of
-- those is a new door, and each is asserted here from the same seven
-- actors. The chat rows are the ones the ruling names: child cannot
-- message sibling, child cannot message a child in another family, parent
-- cannot message another family's child, Rainford teacher sees zero rows.

-- Fixture: the families made by the real function now start at status
-- 'none' (MRB-309: no trial until checkout). Put both on an active
-- subscription so the sealing rows below are about SEALING, not billing.
-- Section C above left family A 'active' and the council's period in the
-- past; Section E starts from a known state.
UPDATE public.subscriptions SET seat_cap = 20, current_period_end = now() + interval '300 days'
 WHERE org_id = 'cc000000-0000-0000-0000-0000000000cc';
SELECT pg_temp.assert_count('a family created by the real function starts at status none (no trial until checkout)', 1,
  (SELECT count(*)::int FROM public.subscriptions
    WHERE org_id = (SELECT id FROM fam_b_t) AND status = 'none' AND trial_end IS NULL));  -- fam_a was walked by Section C
UPDATE public.subscriptions SET status='active', current_period_end = now() + interval '20 days', quantity = 2
 WHERE org_id = (SELECT id FROM fam_a_t);
UPDATE public.subscriptions SET status='active', current_period_end = now() + interval '20 days', quantity = 1
 WHERE org_id = (SELECT id FROM fam_b_t);

-- Rows in the new tables, one per family, so cross-family reads have
-- something to fail to see.
INSERT INTO public.child_plans (child_id, org_id, cursors)
VALUES ('a0000000-0000-0000-0000-000000000011', (SELECT id FROM fam_a_t), '{"Biology":1}'),
       ('b0000000-0000-0000-0000-000000000011', (SELECT id FROM fam_b_t), '{"Biology":1}');
INSERT INTO public.work_items (id, org_id, child_id, week_start, scheduled_for, kind, title, ref)
VALUES ('a0000000-0000-0000-0000-0000000000f1', (SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000011', '2026-09-07', '2026-09-08', 'lesson', 'Matrix lesson A', '{}'),
       ('b0000000-0000-0000-0000-0000000000f1', (SELECT id FROM fam_b_t), 'b0000000-0000-0000-0000-000000000011', '2026-09-07', '2026-09-08', 'lesson', 'Matrix lesson B', '{}');
INSERT INTO public.exam_questions (id, key_stage, subject, topic, marks, text, scheme, source)
VALUES ('zz-matrix-q', 'KS3', 'Biology', 'Matrix', 4, 'Matrix question', '[{"text":"a point"}]', 'code_seed');
INSERT INTO public.exam_answers (id, org_id, child_id, question_id, answer, ai_score, ai_max)
VALUES ('a0000000-0000-0000-0000-0000000000e1', (SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000011', 'zz-matrix-q', 'an answer', 2, 4),
       ('b0000000-0000-0000-0000-0000000000e1', (SELECT id FROM fam_b_t), 'b0000000-0000-0000-0000-000000000011', 'zz-matrix-q', 'an answer', 2, 4);
INSERT INTO public.unit_check_attempts (org_id, child_id, unit_code, key_stage, question_ids, count, time_limit_s)
VALUES ((SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000011', 'B1', 'KS3', '{x}', 10, 900),
       ((SELECT id FROM fam_b_t), 'b0000000-0000-0000-0000-000000000011', 'B1', 'KS3', '{x}', 10, 900);
INSERT INTO public.consumer_notifications (org_id, recipient_id, kind, title)
VALUES ((SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000011', 'matrix', 'for child A1'),
       ((SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000001', 'matrix', 'for parent A');
INSERT INTO public.email_log (type, org_id, recipient_id, recipient_email, status)
VALUES ('matrix', (SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000001', 'parentA@gmail.com', 'dry_run');
INSERT INTO public.stripe_events (id, type, org_id) VALUES ('evt_matrix', 'matrix', (SELECT id FROM fam_a_t));
INSERT INTO public.ai_usage_events (profile_id, org_id, kind)
VALUES ('a0000000-0000-0000-0000-000000000011', (SELECT id FROM fam_a_t), 'tutor_turn'),
       ('b0000000-0000-0000-0000-000000000011', (SELECT id FROM fam_b_t), 'tutor_turn');
INSERT INTO public.org_limits (org_id, tutor_turns_per_day) VALUES ((SELECT id FROM fam_a_t), 10), ((SELECT id FROM fam_b_t), 10);
INSERT INTO public.parent_prefs (profile_id) VALUES ('a0000000-0000-0000-0000-000000000001'), ('b0000000-0000-0000-0000-000000000001');
-- A parent→child message in each family, and a staff→pupil one, as the
-- service role would write them (inserted as postgres; the policy rows
-- below are the ones inserted AS the actors).
INSERT INTO public.family_messages (id, org_id, sender_id, recipient_id, body)
VALUES ('a0000000-0000-0000-0000-0000000000d1', (SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000011', 'hello A1 from PA'),
       ('b0000000-0000-0000-0000-0000000000d2', (SELECT id FROM fam_b_t), 'b0000000-0000-0000-0000-000000000001', 'b0000000-0000-0000-0000-000000000011', 'hello B1 from PB'),
       ('c0000000-0000-0000-0000-0000000000d3', 'cc000000-0000-0000-0000-0000000000cc', 'c0000000-0000-0000-0000-000000000001', 'c0000000-0000-0000-0000-000000000011', 'hello pupil from staff');

DO $$
DECLARE
  fam_a uuid; fam_b uuid;
  r_teacher uuid; r_student uuid;
  pa  uuid := 'a0000000-0000-0000-0000-000000000001';
  pb  uuid := 'b0000000-0000-0000-0000-000000000001';
  ca1 uuid := 'a0000000-0000-0000-0000-000000000011';
  ca2 uuid := 'a0000000-0000-0000-0000-000000000012';
  cb1 uuid := 'b0000000-0000-0000-0000-000000000011';
  sc  uuid := 'c0000000-0000-0000-0000-000000000001';
  pc1 uuid := 'c0000000-0000-0000-0000-000000000011';
  cc  uuid := 'cc000000-0000-0000-0000-0000000000cc';
  n int;
BEGIN
  SELECT id INTO fam_a FROM fam_a_t;
  SELECT id INTO fam_b FROM fam_b_t;
  SELECT id INTO r_teacher FROM public.profiles
    WHERE role='teacher' AND school_id=(SELECT id FROM public.schools WHERE code='RHS') LIMIT 1;
  SELECT id INTO r_student FROM public.profiles
    WHERE role='student' AND school_id=(SELECT id FROM public.schools WHERE code='RHS') LIMIT 1;

  -- ---------- C1. org_access_state truth table (as postgres) ----------
  PERFORM pg_temp.assert_count('state: school is full', 1,
    (public.org_access_state((SELECT id FROM public.schools WHERE code='RHS')) = 'full')::int);
  PERFORM pg_temp.assert_count('state: unknown org is locked', 1,
    (public.org_access_state('00000000-0000-0000-0000-00000000dead') = 'locked')::int);
  PERFORM pg_temp.assert_count('state: null org is locked', 1,
    (public.org_access_state(NULL) = 'locked')::int);
  PERFORM pg_temp.assert_count('state: organisation with seat cap + period is full', 1,
    (public.org_access_state(cc) = 'full')::int);
  -- family B walks the state machine
  UPDATE public.subscriptions SET status='none', trial_end=NULL, current_period_end=NULL, comped_until=NULL WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: none → none', 1, (public.org_access_state(fam_b)='none')::int);
  UPDATE public.subscriptions SET status='trialing', trial_end=now()+interval '5 days' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: trialing with future trial_end → full', 1, (public.org_access_state(fam_b)='full')::int);
  UPDATE public.subscriptions SET status='trialing', trial_end=now()-interval '1 day' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: trialing with past trial_end → read_only (no free forever)', 1, (public.org_access_state(fam_b)='read_only')::int);
  UPDATE public.subscriptions SET status='trialing', trial_end=NULL WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: trialing with no trial_end → read_only', 1, (public.org_access_state(fam_b)='read_only')::int);
  UPDATE public.subscriptions SET status='active', current_period_end=now()+interval '20 days' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: active → full', 1, (public.org_access_state(fam_b)='full')::int);
  UPDATE public.subscriptions SET status='past_due', current_period_end=now()-interval '3 days' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: past_due inside 7-day grace → full', 1, (public.org_access_state(fam_b)='full')::int);
  UPDATE public.subscriptions SET status='past_due', current_period_end=now()-interval '8 days' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: past_due beyond grace → read_only', 1, (public.org_access_state(fam_b)='read_only')::int);
  UPDATE public.subscriptions SET status='canceled', current_period_end=now()+interval '10 days' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: canceled with period left → read_only', 1, (public.org_access_state(fam_b)='read_only')::int);
  UPDATE public.subscriptions SET status='canceled', current_period_end=now()-interval '1 day' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: canceled after period end → locked', 1, (public.org_access_state(fam_b)='locked')::int);
  UPDATE public.subscriptions SET status='locked' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: locked → locked', 1, (public.org_access_state(fam_b)='locked')::int);
  UPDATE public.subscriptions SET status='comped', comped_until=now()+interval '30 days' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: comped in date → full', 1, (public.org_access_state(fam_b)='full')::int);
  UPDATE public.subscriptions SET status='comped', comped_until=now()-interval '1 day' WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('state: comped expired → locked', 1, (public.org_access_state(fam_b)='locked')::int);
  PERFORM pg_temp.assert_count('org_is_entitled is exactly state=full (locked → false)', 0, public.org_is_entitled(fam_b)::int);
  UPDATE public.subscriptions SET status='active', current_period_end=now()+interval '20 days', comped_until=NULL WHERE org_id=fam_b;
  PERFORM pg_temp.assert_count('org_is_entitled is exactly state=full (active → true)', 1, public.org_is_entitled(fam_b)::int);
  UPDATE public.subscriptions SET current_period_end=now()-interval '3 days' WHERE org_id=cc;
  PERFORM pg_temp.assert_count('state: organisation 3 days past period → read_only', 1, (public.org_access_state(cc)='read_only')::int);
  UPDATE public.subscriptions SET current_period_end=now()-interval '20 days' WHERE org_id=cc;
  PERFORM pg_temp.assert_count('state: organisation 20 days past period → locked', 1, (public.org_access_state(cc)='locked')::int);
  UPDATE public.subscriptions SET current_period_end=now()+interval '300 days' WHERE org_id=cc;

  -- ---------- C2. guardian_of_child ----------
  PERFORM pg_temp.assert_count('guardian: PA of A1', 1, public.guardian_of_child(pa, ca1)::int);
  PERFORM pg_temp.assert_count('guardian: PA of B1 (other family) no', 0, public.guardian_of_child(pa, cb1)::int);
  PERFORM pg_temp.assert_count('guardian: PB of A1 no', 0, public.guardian_of_child(pb, ca1)::int);
  PERFORM pg_temp.assert_count('guardian: A1 of A2 (sibling) no', 0, public.guardian_of_child(ca1, ca2)::int);
  PERFORM pg_temp.assert_count('guardian: council staff of pupil', 1, public.guardian_of_child(sc, pc1)::int);
  PERFORM pg_temp.assert_count('guardian: council staff of A1 no', 0, public.guardian_of_child(sc, ca1)::int);
  PERFORM pg_temp.assert_count('guardian: Rainford teacher of Rainford student no (school kind)', 0, public.guardian_of_child(r_teacher, r_student)::int);
  PERFORM pg_temp.assert_count('guardian: pupil of self no', 0, public.guardian_of_child(pc1, pc1)::int);

  -- ---------- C3. family_message_allowed — the rule ----------
  PERFORM pg_temp.assert_count('chat rule: PA → A1', 1, public.family_message_allowed(pa, ca1)::int);
  PERFORM pg_temp.assert_count('chat rule: A1 → PA', 1, public.family_message_allowed(ca1, pa)::int);
  PERFORM pg_temp.assert_count('chat rule: A1 → A2 sibling NO', 0, public.family_message_allowed(ca1, ca2)::int);
  PERFORM pg_temp.assert_count('chat rule: A1 → B1 other family NO', 0, public.family_message_allowed(ca1, cb1)::int);
  PERFORM pg_temp.assert_count('chat rule: PA → B1 other family child NO', 0, public.family_message_allowed(pa, cb1)::int);
  PERFORM pg_temp.assert_count('chat rule: PB → A1 NO', 0, public.family_message_allowed(pb, ca1)::int);
  PERFORM pg_temp.assert_count('chat rule: PA → PB adult to adult NO', 0, public.family_message_allowed(pa, pb)::int);
  PERFORM pg_temp.assert_count('chat rule: staff → pupil', 1, public.family_message_allowed(sc, pc1)::int);
  PERFORM pg_temp.assert_count('chat rule: pupil → staff', 1, public.family_message_allowed(pc1, sc)::int);
  PERFORM pg_temp.assert_count('chat rule: pupil → A1 NO', 0, public.family_message_allowed(pc1, ca1)::int);
  PERFORM pg_temp.assert_count('chat rule: Rainford teacher → Rainford student NO (school kind)', 0, public.family_message_allowed(r_teacher, r_student)::int);

  -- ---------- C4. chat, as the actors, through RLS ----------
  PERFORM pg_temp.login_as(ca1);
  PERFORM pg_temp.assert_count('A1 sees exactly the 1 message addressed to them', 1,
    (SELECT count(*)::int FROM public.family_messages));
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_a, ca1, pa, 'hi mum');
    PERFORM pg_temp.assert_count('A1 → PA insert allowed', 1, 1);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('A1 → PA insert allowed', 1, 0);
  END;
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_a, ca1, ca2, 'hi sis');
    PERFORM pg_temp.assert_count('A1 → A2 (sibling) insert REFUSED', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('A1 → A2 (sibling) insert REFUSED', 1, 1);
  END;
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_a, ca1, cb1, 'hi stranger');
    PERFORM pg_temp.assert_count('A1 → B1 (other family) insert REFUSED', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('A1 → B1 (other family) insert REFUSED', 1, 1);
  END;
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_a, pa, ca1, 'forged as PA');
    PERFORM pg_temp.assert_count('A1 cannot insert as PA (sender must be self)', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('A1 cannot insert as PA (sender must be self)', 1, 1);
  END;
  BEGIN
    UPDATE public.family_messages SET body='edited' WHERE sender_id = ca1;
    PERFORM pg_temp.assert_count('A1 UPDATE of a message is refused (no edit path)', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('A1 UPDATE of a message is refused (no edit path)', 1, 1);
  END;
  SELECT public.family_messages_mark_read(pa) INTO n;
  PERFORM pg_temp.assert_count('A1 marks PA''s 1 message read via RPC', 1, n);
  PERFORM pg_temp.assert_count('A1 cannot soft-delete PA''s message', 0,
    public.family_message_delete('a0000000-0000-0000-0000-0000000000d1')::int);

  PERFORM pg_temp.login_as(pa);
  PERFORM pg_temp.assert_count('PA sees the 2 messages in their thread with A1', 2,
    (SELECT count(*)::int FROM public.family_messages));
  PERFORM pg_temp.assert_count('PA sees 0 of family B messages', 0,
    (SELECT count(*)::int FROM public.family_messages WHERE org_id = fam_b));
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_b, pa, cb1, 'hi other child');
    PERFORM pg_temp.assert_count('PA → B1 (other family child) insert REFUSED', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA → B1 (other family child) insert REFUSED', 1, 1);
  END;
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_a, pa, cb1, 'hi other child, my org id');
    PERFORM pg_temp.assert_count('PA → B1 with own org_id still REFUSED', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA → B1 with own org_id still REFUSED', 1, 1);
  END;

  PERFORM pg_temp.login_as(pb);
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_b, pb, ca1, 'hi A1');
    PERFORM pg_temp.assert_count('PB → A1 insert REFUSED', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PB → A1 insert REFUSED', 1, 1);
  END;

  PERFORM pg_temp.login_as(sc);
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (cc, sc, pc1, 'well done this week');
    PERFORM pg_temp.assert_count('council staff → pupil insert allowed', 1, 1);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('council staff → pupil insert allowed', 1, 0);
  END;
  PERFORM pg_temp.login_as(pc1);
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (cc, pc1, sc, 'thanks');
    PERFORM pg_temp.assert_count('pupil → staff insert allowed', 1, 1);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('pupil → staff insert allowed', 1, 0);
  END;
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (cc, pc1, ca1, 'hi');
    PERFORM pg_temp.assert_count('pupil → family child insert REFUSED', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('pupil → family child insert REFUSED', 1, 1);
  END;

  PERFORM pg_temp.login_as(r_teacher);
  PERFORM pg_temp.assert_count('Rainford teacher sees 0 family_messages', 0,
    (SELECT count(*)::int FROM public.family_messages));
  PERFORM pg_temp.login_as(r_student);
  PERFORM pg_temp.assert_count('Rainford student sees 0 family_messages', 0,
    (SELECT count(*)::int FROM public.family_messages));
  PERFORM pg_temp.logout();
  PERFORM pg_temp.assert_count('anon sees 0 family_messages', 0,
    (SELECT count(*)::int FROM public.family_messages));

  -- locked org: read stays, send closes
  PERFORM set_config('role','postgres',true);
  UPDATE public.subscriptions SET status='locked' WHERE org_id=fam_a;
  PERFORM pg_temp.login_as(pa);
  PERFORM pg_temp.assert_count('locked family: PA still reads their thread', 2,
    (SELECT count(*)::int FROM public.family_messages));
  BEGIN
    INSERT INTO public.family_messages (org_id, sender_id, recipient_id, body) VALUES (fam_a, pa, ca1, 'while locked');
    PERFORM pg_temp.assert_count('locked family: PA send REFUSED at policy', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('locked family: PA send REFUSED at policy', 1, 1);
  END;
  PERFORM set_config('role','postgres',true);
  UPDATE public.subscriptions SET status='active' WHERE org_id=fam_a;

  -- ---------- C5. every new table, sealed ----------
  PERFORM pg_temp.login_as(pa);
  PERFORM pg_temp.assert_count('PA sees A1''s 1 work item', 1, (SELECT count(*)::int FROM public.work_items));
  PERFORM pg_temp.assert_count('PA sees 0 of B1''s work items', 0, (SELECT count(*)::int FROM public.work_items WHERE child_id=cb1));
  PERFORM pg_temp.assert_count('PA sees A1''s plan', 1, (SELECT count(*)::int FROM public.child_plans));
  PERFORM pg_temp.assert_count('PA sees A1''s 1 exam answer', 1, (SELECT count(*)::int FROM public.exam_answers));
  PERFORM pg_temp.assert_count('PA sees A1''s 1 unit check', 1, (SELECT count(*)::int FROM public.unit_check_attempts));
  PERFORM pg_temp.assert_count('PA sees only their own notification (not A1''s)', 1, (SELECT count(*)::int FROM public.consumer_notifications));
  PERFORM pg_temp.assert_count('PA sees 0 email_log rows', 0, (SELECT count(*)::int FROM public.email_log));
  PERFORM pg_temp.assert_count('PA sees 0 stripe_events', 0, (SELECT count(*)::int FROM public.stripe_events));
  PERFORM pg_temp.assert_count('PA sees 0 platform_settings', 0, (SELECT count(*)::int FROM public.platform_settings));
  PERFORM pg_temp.assert_count('PA sees A1''s 1 usage event', 1, (SELECT count(*)::int FROM public.ai_usage_events));
  PERFORM pg_temp.assert_count('PA sees own org_limits row only', 1, (SELECT count(*)::int FROM public.org_limits));
  PERFORM pg_temp.assert_count('PA sees own prefs only', 1, (SELECT count(*)::int FROM public.parent_prefs));
  PERFORM pg_temp.assert_count('PA reads the exam question pool', 1, (SELECT count(*)::int FROM public.exam_questions WHERE id='zz-matrix-q'));
  BEGIN
    INSERT INTO public.work_items (org_id, child_id, week_start, scheduled_for, kind, title) VALUES (fam_a, ca1, '2026-09-07', '2026-09-08', 'lesson', 'forged');
    PERFORM pg_temp.assert_count('PA INSERT into work_items refused (service role only)', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA INSERT into work_items refused (service role only)', 1, 1);
  END;
  BEGIN
    UPDATE public.child_plans SET paused_at = now() WHERE child_id = ca1;
    PERFORM pg_temp.assert_count('PA UPDATE of child_plans refused (service role only)', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA UPDATE of child_plans refused (service role only)', 1, 1);
  END;
  BEGIN
    UPDATE public.exam_answers SET mb_score = 6 WHERE child_id = ca1;
    PERFORM pg_temp.assert_count('PA cannot mark an answer (service role only)', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('PA cannot mark an answer (service role only)', 1, 1);
  END;

  PERFORM pg_temp.login_as(ca1);
  PERFORM pg_temp.assert_count('A1 sees own 1 work item', 1, (SELECT count(*)::int FROM public.work_items));
  PERFORM pg_temp.assert_count('A1 sees own 1 notification', 1, (SELECT count(*)::int FROM public.consumer_notifications));
  PERFORM pg_temp.assert_count('A1 sees 0 parent_prefs', 0, (SELECT count(*)::int FROM public.parent_prefs));
  PERFORM pg_temp.assert_count('A1 sees 0 org_limits', 0, (SELECT count(*)::int FROM public.org_limits));
  BEGIN
    UPDATE public.work_items SET status='done' WHERE child_id = ca1;
    PERFORM pg_temp.assert_count('A1 cannot mark own item done directly (goes through the backend)', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('A1 cannot mark own item done directly (goes through the backend)', 1, 1);
  END;

  PERFORM pg_temp.login_as(ca2);
  PERFORM pg_temp.assert_count('A2 sees 0 of sibling A1''s work items', 0, (SELECT count(*)::int FROM public.work_items));
  PERFORM pg_temp.assert_count('A2 sees 0 of sibling A1''s answers', 0, (SELECT count(*)::int FROM public.exam_answers));

  PERFORM pg_temp.login_as(pb);
  PERFORM pg_temp.assert_count('PB sees 0 of family A work items', 0, (SELECT count(*)::int FROM public.work_items WHERE org_id=fam_a));
  PERFORM pg_temp.assert_count('PB sees 0 of family A answers', 0, (SELECT count(*)::int FROM public.exam_answers WHERE org_id=fam_a));

  PERFORM pg_temp.login_as(sc);
  PERFORM pg_temp.assert_count('council staff sees 0 family work items', 0, (SELECT count(*)::int FROM public.work_items));
  PERFORM pg_temp.login_as(r_teacher);
  PERFORM pg_temp.assert_count('Rainford teacher sees 0 work items', 0, (SELECT count(*)::int FROM public.work_items));
  PERFORM pg_temp.assert_count('Rainford teacher sees 0 exam answers', 0, (SELECT count(*)::int FROM public.exam_answers));
  PERFORM pg_temp.assert_count('Rainford teacher sees 0 unit checks', 0, (SELECT count(*)::int FROM public.unit_check_attempts));
  PERFORM pg_temp.logout();
  PERFORM pg_temp.assert_count('anon sees 0 exam questions', 0, (SELECT count(*)::int FROM public.exam_questions));
  PERFORM pg_temp.assert_count('anon sees 0 work items', 0, (SELECT count(*)::int FROM public.work_items));

  -- ---------- C6. structural ----------
  PERFORM set_config('role','postgres',true);
  PERFORM pg_temp.assert_count('family_messages is in the realtime publication', 1,
    (SELECT count(*)::int FROM pg_publication_tables WHERE pubname='supabase_realtime' AND tablename='family_messages'));
  PERFORM pg_temp.assert_count('five consumer cron jobs are scheduled', 5,
    (SELECT count(*)::int FROM cron.job WHERE jobname LIKE 'consumer_%'));
  PERFORM pg_temp.assert_count('consumer_cron_call is a no-op while unconfigured', 1,
    (public.consumer_cron_call('/x') IS NULL)::int);
  PERFORM pg_temp.assert_count('the cap defaults row exists', 1,
    (SELECT count(*)::int FROM public.platform_settings WHERE key='consumer_limits'));
  PERFORM pg_temp.assert_count('mb_quota_used counts only sent_to_mb this month', 0, public.mb_quota_used(ca1));
  PERFORM pg_temp.assert_count('ai_usage_counts sees A1''s tutor turn today', 1,
    ((public.ai_usage_counts(ca1)->>'tutor_today')::int));
END $$;

-- =====================================================================
-- SECTION F — NIGHT 3 (MRB-317/318): the deletion-request ledger is sealed
-- like every other family table, and a group class is tellable apart.
-- =====================================================================
-- Night 3 added one table (account_deletion_requests) and one column
-- (classes.consumer_kind). The table is read by the parent who asked and
-- by nobody else; it is written by the service role only — a parent who
-- could write their own execute_after could shorten their own grace.
INSERT INTO public.account_deletion_requests (org_id, requested_by, execute_after)
VALUES ((SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000001', now() + interval '30 days');

DO $$
DECLARE
  fam_a uuid; fam_b uuid; r_teacher uuid;
  pa  uuid := 'a0000000-0000-0000-0000-000000000001';
  pb  uuid := 'b0000000-0000-0000-0000-000000000001';
  ca1 uuid := 'a0000000-0000-0000-0000-000000000011';
  sc  uuid := 'c0000000-0000-0000-0000-000000000001';
BEGIN
  SELECT id INTO fam_a FROM fam_a_t;
  SELECT id INTO fam_b FROM fam_b_t;
  SELECT id INTO r_teacher FROM public.profiles
    WHERE role='teacher' AND school_id=(SELECT id FROM public.schools WHERE code='RHS') LIMIT 1;

  PERFORM pg_temp.login_as(pa);
  PERFORM pg_temp.assert_count('F: PA sees own family''s deletion request', 1,
    (SELECT count(*)::int FROM public.account_deletion_requests));
  BEGIN
    UPDATE public.account_deletion_requests SET execute_after = now() WHERE org_id = fam_a;
    PERFORM pg_temp.assert_count('F: PA cannot shorten own grace (service role writes only)', 1,
      (SELECT count(*)::int FROM public.account_deletion_requests WHERE org_id = fam_a AND execute_after > now() + interval '29 days'));
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('F: PA cannot shorten own grace (service role writes only)', 1, 1);
  END;
  BEGIN
    INSERT INTO public.account_deletion_requests (org_id, requested_by, execute_after) VALUES (fam_b, pa, now());
    PERFORM pg_temp.assert_count('F: PA cannot file a request against family B', 1, 0);
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('F: PA cannot file a request against family B', 1, 1);
  END;

  PERFORM pg_temp.login_as(ca1);
  PERFORM pg_temp.assert_count('F: child A1 sees the family''s request (same org, read-only)', 1,
    (SELECT count(*)::int FROM public.account_deletion_requests));
  PERFORM pg_temp.login_as(pb);
  PERFORM pg_temp.assert_count('F: PB sees 0 of family A''s deletion request', 0,
    (SELECT count(*)::int FROM public.account_deletion_requests));
  PERFORM pg_temp.login_as(sc);
  PERFORM pg_temp.assert_count('F: council staff sees 0 family deletion requests', 0,
    (SELECT count(*)::int FROM public.account_deletion_requests));
  PERFORM pg_temp.login_as(r_teacher);
  PERFORM pg_temp.assert_count('F: Rainford teacher sees 0 deletion requests', 0,
    (SELECT count(*)::int FROM public.account_deletion_requests));
  PERFORM pg_temp.logout();
  PERFORM pg_temp.assert_count('F: anon sees 0 deletion requests', 0,
    (SELECT count(*)::int FROM public.account_deletion_requests));

  -- classes.consumer_kind: present, constrained, and NULL on every school class
  PERFORM set_config('role','postgres',true);
  PERFORM pg_temp.assert_count('F: classes.consumer_kind exists', 1,
    (SELECT count(*)::int FROM information_schema.columns WHERE table_schema='public' AND table_name='classes' AND column_name='consumer_kind'));
  PERFORM pg_temp.assert_count('F: every school-kind class has NULL consumer_kind', 0,
    (SELECT count(*)::int FROM public.classes c JOIN public.schools s ON s.id=c.school_id WHERE s.kind='school' AND c.consumer_kind IS NOT NULL));
  BEGIN
    UPDATE public.classes SET consumer_kind = 'caseload' WHERE id = (SELECT id FROM public.classes LIMIT 1);
    PERFORM pg_temp.assert_count('F: consumer_kind refuses a value outside child|group', 1, 0);
  EXCEPTION WHEN check_violation THEN
    PERFORM pg_temp.assert_count('F: consumer_kind refuses a value outside child|group', 1, 1);
  END;
END $$;

-- =====================================================================
-- SECTION F2 — NIGHT 4 (MRB-321): a sibling's paper, and the terms stamp
-- =====================================================================
-- A1 added GET /api/consumer/child/unit-checks, whose ONLY scope is
-- `child_id = the calling child`. This section states, at the database, what
-- that route is and is not relying on: whether RLS alone would keep two
-- siblings apart, and whether a parent or a child can move their own terms
-- acceptance.
--
-- A second sitting, for the OTHER child in family A, so "my sibling's paper"
-- is a real row rather than a hypothesis.
INSERT INTO public.unit_check_attempts (org_id, child_id, unit_code, key_stage, question_ids, count, time_limit_s)
VALUES ((SELECT id FROM fam_a_t), 'a0000000-0000-0000-0000-000000000012', 'B2', 'KS3', '{y}', 10, 900);

DO $$
DECLARE
  pa  uuid := 'a0000000-0000-0000-0000-000000000001';
  ca1 uuid := 'a0000000-0000-0000-0000-000000000011';
  ca2 uuid := 'a0000000-0000-0000-0000-000000000012';
  cb1 uuid := 'b0000000-0000-0000-0000-000000000011';
  n   int;
BEGIN
  -- ── the cross-family seal, which IS the database's ──────────────────
  PERFORM pg_temp.login_as(cb1);
  PERFORM pg_temp.assert_count('F2: child B1 sees 0 of family A''s unit-check attempts', 0,
    (SELECT count(*)::int FROM public.unit_check_attempts
      WHERE child_id IN (ca1, ca2)));
  PERFORM pg_temp.assert_count('F2: child B1 sees exactly their own one attempt', 1,
    (SELECT count(*)::int FROM public.unit_check_attempts));

  -- ── the sibling seal, which turns out to be BOTH layers ─────────────
  -- MEASURED, not assumed. The Night 4 route was written on the assumption
  -- that RLS here is ORG-scoped — a parent must see every child's sittings,
  -- and a parent and a child share an org — which would have made the
  -- route's own `.eq('child_id', profile.id)` the only thing keeping two
  -- siblings apart. It is not: the policy is own-row-OR-guardian, so a child
  -- sees exactly their own and a parent sees both. The route's equality is
  -- therefore a SECOND belt that agrees with the database rather than the
  -- only one. Asserted here so that a future widening of the policy to the
  -- org — which would be a perfectly reasonable-looking change — fails a
  -- gate instead of quietly making a sibling's paper readable.
  PERFORM pg_temp.login_as(ca1);
  SELECT count(*)::int INTO n FROM public.unit_check_attempts;
  PERFORM pg_temp.assert_count(
    'F2: child A1 sees ONLY their own attempt, not their sibling''s — RLS is child-scoped, and GET /child/unit-checks agrees with it',
    1, n);

  PERFORM pg_temp.login_as(pa);
  PERFORM pg_temp.assert_count('F2: parent A sees both children''s attempts', 2,
    (SELECT count(*)::int FROM public.unit_check_attempts));
  PERFORM pg_temp.logout();
  PERFORM pg_temp.assert_count('F2: anon sees 0 unit-check attempts', 0,
    (SELECT count(*)::int FROM public.unit_check_attempts));

  -- ── A5: the terms stamp ─────────────────────────────────────────────
  PERFORM set_config('role','postgres',true);
  PERFORM pg_temp.assert_count('F2: profiles.terms_accepted_at exists and is nullable', 1,
    (SELECT count(*)::int FROM information_schema.columns
      WHERE table_schema='public' AND table_name='profiles'
        AND column_name='terms_accepted_at' AND is_nullable='YES' AND column_default IS NULL));
  -- No DEFAULT and no back-fill: a profile created by the real functions
  -- inside this transaction comes out NULL. Scoped to THIS plan's own
  -- fixtures rather than the whole table, because the TEST project also
  -- carries live rows from the lane drives, and a live parent who has
  -- genuinely accepted the terms is not a failure of this assertion.
  PERFORM pg_temp.assert_count('F2: a profile made by the real functions starts NULL — no DEFAULT, no back-fill', 0,
    (SELECT count(*)::int FROM public.profiles
      WHERE terms_accepted_at IS NOT NULL
        AND id IN (pa, ca1, ca2, cb1, 'b0000000-0000-0000-0000-000000000001'::uuid)));

  -- Only the service role writes it. A parent who could set their own
  -- acceptance date could set it to any date they liked, which would make
  -- the column worth nothing as evidence.
  PERFORM pg_temp.login_as(pa);
  BEGIN
    UPDATE public.profiles SET terms_accepted_at = now() WHERE id = pa;
    PERFORM pg_temp.assert_count('F2: parent cannot stamp their own terms acceptance', 0,
      (SELECT count(*)::int FROM public.profiles WHERE id = pa AND terms_accepted_at IS NOT NULL));
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('F2: parent cannot stamp their own terms acceptance', 0, 0);
  END;
  PERFORM pg_temp.login_as(ca1);
  BEGIN
    UPDATE public.profiles SET terms_accepted_at = now() WHERE id = pa;
    PERFORM pg_temp.assert_count('F2: a child cannot stamp their parent''s terms acceptance', 0,
      (SELECT count(*)::int FROM public.profiles WHERE id = pa AND terms_accepted_at IS NOT NULL));
  EXCEPTION WHEN OTHERS THEN
    PERFORM pg_temp.assert_count('F2: a child cannot stamp their parent''s terms acceptance', 0, 0);
  END;
  PERFORM pg_temp.logout();
END $$;

-- =====================================================================
-- RESULTS
-- =====================================================================
SELECT CASE WHEN passed THEN 'PASS' ELSE 'FAIL' END AS status,
       test_name, expected_count AS expected, actual_count AS actual
FROM test_results ORDER BY passed ASC, test_name ASC;

ROLLBACK;
