-- =====================================================================
-- Tests:   Stage 3 — Schools Onboarding (SSO gate + account merge engine)
-- Run:     against TEST only. Wrapped in a transaction that ROLLS BACK,
--          so no fixture data persists whether tests pass or fail.
-- Style:   plpgsql ASSERT per check — the script errors loudly on the first
--          failure and prints "✓ All Stage 3 tests passed." if all hold.
-- Covers:  school_id_for_email_domain, hook_before_user_created (4 branches),
--          reparent_student (collision + idempotency), and the
--          create/confirm claim round-trip. (The roster-import reconciliation
--          engine is an Edge Function, tested end-to-end via HTTP — see
--          docs/stage-3-onboarding.md.)
-- =====================================================================

BEGIN;

DO $$
DECLARE
  v_rainford uuid;
  v_old  uuid := '31000000-0000-0000-0000-0000000000a1';
  v_can  uuid := '31000000-0000-0000-0000-0000000000b1';
  v_classA uuid;
  v_classB uuid;
  v_r jsonb;
  v_xp int;
  v_active int;
BEGIN
  SELECT id INTO v_rainford FROM public.schools WHERE slug = 'rainford-high';
  ASSERT v_rainford IS NOT NULL, 'Rainford school must exist';

  -- ── SSO: domain resolver ──────────────────────────────────────────
  ASSERT public.school_id_for_email_domain('Kid@Rainford.org.uk') = v_rainford,
    'resolver: rainford domain (case-insensitive) must resolve to Rainford';
  ASSERT public.school_id_for_email_domain('kid@gmail.com') IS NULL,
    'resolver: personal domain must resolve to NULL';

  -- ── SSO: Before-User-Created hook (4 branches) ────────────────────
  ASSERT public.hook_before_user_created('{"user":{"email":"x@rainford.org.uk","app_metadata":{"provider":"email"}}}'::jsonb) = '{}'::jsonb,
    'hook: email-provider signup must pass through';
  ASSERT (public.hook_before_user_created('{"user":{"email":"x@gmail.com","app_metadata":{"provider":"google"}}}'::jsonb)->'error'->>'http_code') = '403',
    'hook: off-domain OAuth must be rejected 403';
  ASSERT (public.hook_before_user_created('{"user":{"email":"newkid@rainford.org.uk","app_metadata":{"provider":"azure"}}}'::jsonb)->'error'->>'http_code') = '403',
    'hook: on-domain OAuth with no pre-assignment must be rejected 403';
  ASSERT (public.hook_before_user_created('{"user":{"app_metadata":{"provider":"google"}}}'::jsonb)->'error'->>'http_code') = '400',
    'hook: missing email must be rejected 400';

  -- ── set up two synthetic accounts + a class collision ─────────────
  SELECT id INTO v_classA FROM public.classes WHERE school_id = v_rainford AND deleted_at IS NULL
    ORDER BY created_at LIMIT 1;
  SELECT id INTO v_classB FROM public.classes WHERE school_id = v_rainford AND deleted_at IS NULL AND id <> v_classA
    ORDER BY created_at LIMIT 1;
  ASSERT v_classA IS NOT NULL AND v_classB IS NOT NULL, 'need two Rainford classes for the merge test';

  INSERT INTO auth.users (id, email, encrypted_password, raw_app_meta_data, raw_user_meta_data, aud, role,
    email_confirmed_at, created_at, updated_at, instance_id,
    confirmation_token, recovery_token, email_change_token_new, email_change_token_current, email_change, phone_change_token, reauthentication_token)
  VALUES
   (v_old, 's3test.old@gmail.com', crypt('x', gen_salt('bf',4)), '{"provider":"email","providers":["email"]}'::jsonb,'{}'::jsonb,'authenticated','authenticated',now(),now(),now(),'00000000-0000-0000-0000-000000000000','','','','','','',''),
   (v_can, 's3test.new@rainford.org.uk', crypt('x', gen_salt('bf',4)), '{"provider":"email","providers":["email"]}'::jsonb,'{}'::jsonb,'authenticated','authenticated',now(),now(),now(),'00000000-0000-0000-0000-000000000000','','','','','','','');

  INSERT INTO public.profiles (id, first_name, school_id, role, key_stage, tier, science_pathway, total_xp, streak_days) VALUES
   (v_old, 'Old', v_rainford, 'student', 'KS4', 'higher', 'triple', 100, 5),
   (v_can, 'New', v_rainford, 'student', 'KS4', NULL, NULL, 20, 2);

  INSERT INTO public.class_members (class_id, student_id, joined_via) VALUES
   (v_classA, v_old, 'admin_added'),  -- collision class
   (v_classB, v_old, 'admin_added'),
   (v_classA, v_can, 'admin_added');  -- canonical already active in classA

  -- ── claim round-trip ──────────────────────────────────────────────
  v_r := public.create_account_claim(v_can, 's3test.old@gmail.com', 's3test_hash_0010', 30);
  ASSERT (v_r->>'matched')::boolean, 'create_account_claim must match the old account';

  v_r := public.confirm_account_claim_and_reparent('s3test_hash_0010');
  ASSERT (v_r->>'ok')::boolean, 'confirm must succeed';
  ASSERT (v_r->'counts'->>'class_members_superseded')::int = 1, 'collision membership must be superseded (1)';
  ASSERT (v_r->'counts'->>'class_members_moved')::int = 1, 'the non-colliding membership must move (1)';

  -- canonical now: XP merged, tier/pathway carried, exactly 2 active classes, no dupes
  SELECT total_xp INTO v_xp FROM public.profiles WHERE id = v_can;
  ASSERT v_xp = 120, format('canonical XP must be 120 (got %s)', v_xp);
  ASSERT (SELECT tier FROM public.profiles WHERE id = v_can) = 'higher', 'canonical tier carried from loser';
  ASSERT (SELECT science_pathway FROM public.profiles WHERE id = v_can) = 'triple', 'canonical pathway carried';
  ASSERT (SELECT deleted_at IS NOT NULL FROM public.profiles WHERE id = v_old), 'loser must be soft-deleted';
  SELECT count(DISTINCT class_id) INTO v_active FROM public.class_members
    WHERE student_id = v_can AND left_at IS NULL AND deleted_at IS NULL;
  ASSERT v_active = 2, format('canonical must have 2 active classes (got %s)', v_active);
  ASSERT (SELECT count(*) FROM (SELECT class_id, student_id FROM public.class_members
            WHERE left_at IS NULL AND deleted_at IS NULL GROUP BY 1,2 HAVING count(*) > 1) d) = 0,
    'no duplicate active memberships anywhere';

  -- ── idempotency: re-confirm + re-reparent are no-ops, XP not doubled ──
  v_r := public.confirm_account_claim_and_reparent('s3test_hash_0010');
  ASSERT (v_r->>'already_consumed')::boolean, 'second confirm must short-circuit (already_consumed)';
  PERFORM public.reparent_student(v_old, v_can);
  SELECT total_xp INTO v_xp FROM public.profiles WHERE id = v_can;
  ASSERT v_xp = 120, format('XP must stay 120 after idempotent re-run (got %s)', v_xp);

  RAISE NOTICE '✓ All Stage 3 tests passed.';
END $$;

ROLLBACK;
-- =====================================================================
-- END — transaction rolled back; no fixture data persists.
-- =====================================================================
