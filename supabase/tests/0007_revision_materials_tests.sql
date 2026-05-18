-- =====================================================================
-- Test Plan:    0007_revision_materials_tests.sql
-- For:          0007_revision_materials.sql
-- Purpose:      Verify the Pattern B access model + topic-taxonomy CHECK
--               constraints actually hold for the revision_materials
--               table. MRB-62 "verified" acceptance criterion.
-- Run on:       Supabase BRANCH or TEST project (after migration applied).
-- Safety:       Wrapped in BEGIN/ROLLBACK — no test data persists.
--
-- Strategy:     Five assertions per MRB-62 acceptance:
--                 T1  valid row inserts cleanly (positive control)
--                 T2  anon SELECT succeeds (no permission error, row visible)
--                 T3  anon INSERT denied (RLS)
--                 T4  topic CHECK rejects bad slug for given subject+paper
--                 T5  space+combined CHECK rejects (content-gating)
--
-- Reading this file:
--   - Each test is a NOTICE that prints PASS or FAIL.
--   - At the end, a summary + result set show pass/fail counts.
--   - If any test FAILS, do not proceed to production.
-- =====================================================================

BEGIN;

-- =====================================================================
-- HELPERS — same pattern as 0001_schools_layer_tests.sql
-- =====================================================================

CREATE TEMP TABLE test_results (
  test_name text,
  expected_count int,
  actual_count int,
  passed boolean
);

-- SECURITY DEFINER lets this function INSERT into pg_temp.test_results
-- regardless of which role the caller has set via set_config('role',...).
-- The assertion itself was already evaluated in the caller's context.
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

-- Switch the current session to the anon role (RLS will apply).
CREATE OR REPLACE FUNCTION pg_temp.as_anon() RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
  PERFORM set_config('request.jwt.claim.sub', '', true);
  PERFORM set_config('request.jwt.claims', '', true);
  PERFORM set_config('role', 'anon', true);
END;
$$;


-- =====================================================================
-- T1 — Valid row inserts cleanly (privileged session)
-- =====================================================================
-- Acts as the migration runner / service role would. If this fails the
-- table or its constraints are wrong; downstream tests would be moot.
--
-- The fixed UUIDs below (…00a1 / …00a2) are only collision-safe because
-- the ENTIRE FILE runs inside BEGIN ... ROLLBACK, so these rows never
-- persist. If you ever lift an assertion out of this transaction
-- wrapper, regenerate the UUIDs with gen_random_uuid() first — copying
-- the literals into a persistent context will collide on re-runs.

INSERT INTO public.revision_materials (
  id, title, description, subject, pathway, tier, paper, topic,
  material_type, file_path, file_size_bytes
)
VALUES (
  '00000000-0000-0000-0000-0000000000a1',
  'Cell Biology — Eukaryotes vs Prokaryotes (Foundation)',
  'Summary notes covering nucleus, organelles and bacterial structure.',
  'biology', 'combined', 'foundation', 'paper_1', 'cell-biology',
  'notes',
  'combined/foundation/biology/paper_1/cell-biology/notes/a1-eukaryotes-vs-prokaryotes.pdf',
  84211
);

-- A second valid row — Triple Higher Physics Space — used as the
-- positive control paired with T5 (space + triple is allowed).
INSERT INTO public.revision_materials (
  id, title, subject, pathway, tier, paper, topic,
  material_type, file_path
)
VALUES (
  '00000000-0000-0000-0000-0000000000a2',
  'Space Physics — Life Cycle of Stars (Triple Higher)',
  'physics', 'triple', 'higher', 'paper_2', 'space',
  'notes',
  'triple/higher/physics/paper_2/space/notes/a2-life-cycle-of-stars.pdf'
);

SELECT pg_temp.assert_count(
  'T1.1 Valid rows inserted cleanly (2 rows present)',
  2,
  (SELECT count(*)::int FROM public.revision_materials
   WHERE id IN (
     '00000000-0000-0000-0000-0000000000a1',
     '00000000-0000-0000-0000-0000000000a2'
   ))
);


-- =====================================================================
-- T2 — Anon SELECT succeeds (no permission error, rows visible)
-- =====================================================================
-- Public marketing surface: anonymous browsers must be able to read
-- the metadata. Soft-deleted rows must be hidden by the policy USING
-- clause — included here because it is part of the same policy
-- expression, not scope-creep.

SELECT pg_temp.as_anon();

-- ─── T2.0 — Role-swap precondition (integrity backstop) ───────────────
-- This guard protects BOTH T2 AND T3. Every assertion below this point
-- (T2.1, T2.2, AND the T3 anon-INSERT-denied test further down) assumes
-- the set_config('role','anon',true) swap actually landed. If for any
-- reason it silently no-ops (typo, wrapper that pins the role, future
-- Postgres change), T2/T3 would pass for the wrong reason — the
-- privileged session can SELECT the rows too, and any INSERT exception
-- could masquerade as RLS denial. Fail loudly here instead.
-- Do NOT remove this check thinking it only concerns T2; T3 depends on
-- the same role swap (it never re-asserts the role before its DO block).
SELECT pg_temp.assert_count(
  'T2.0 Role swap landed (current_user = anon)',
  1,
  (SELECT count(*)::int WHERE current_user = 'anon')
);

SELECT pg_temp.assert_count(
  'T2.1 Anon SELECT returns both inserted rows',
  2,
  (SELECT count(*)::int FROM public.revision_materials
   WHERE id IN (
     '00000000-0000-0000-0000-0000000000a1',
     '00000000-0000-0000-0000-0000000000a2'
   ))
);

-- Reset back so we can soft-delete the row as a privileged session.
RESET ROLE;

UPDATE public.revision_materials
   SET deleted_at = now()
 WHERE id = '00000000-0000-0000-0000-0000000000a1';

SELECT pg_temp.as_anon();

SELECT pg_temp.assert_count(
  'T2.2 Anon SELECT hides soft-deleted row (policy USING deleted_at IS NULL)',
  1,
  (SELECT count(*)::int FROM public.revision_materials
   WHERE id IN (
     '00000000-0000-0000-0000-0000000000a1',
     '00000000-0000-0000-0000-0000000000a2'
   ))
);


-- =====================================================================
-- T3 — Anon INSERT denied (RLS — no INSERT policy)
-- =====================================================================
-- FAIL-CLOSED. This is the linchpin of Pattern B: the entire security
-- model rests on "anon cannot write." A false green here would ship a
-- security hole. We accept ONLY the specific RLS-denial condition as a
-- PASS; any other exception type, and the "no exception at all" path,
-- both record a distinct, visible FAIL — with the actual SQLSTATE and
-- message captured so the failure mode is diagnosable.
--
-- The correct denial path on Postgres 14+ for "RLS blocks INSERT
-- because no permissive INSERT policy matches" is SQLSTATE 42501
-- (condition: insufficient_privilege), message: "new row violates
-- row-level security policy for table ...".

DO $$
DECLARE
  v_sqlstate text;
  v_message  text;
BEGIN
  BEGIN
    INSERT INTO public.revision_materials (
      title, subject, pathway, tier, paper, topic, material_type, file_path
    )
    VALUES (
      'Anon injection attempt',
      'biology', 'combined', 'foundation', 'paper_1', 'cell-biology',
      'notes',
      'should-never-land.pdf'
    );
    -- Reached here ⇒ INSERT succeeded ⇒ anon WROTE ⇒ security hole.
    -- Record as a hard FAIL, never as a pass.
    PERFORM pg_temp.assert_count(
      'T3.1 Anon INSERT denied by RLS (SQLSTATE 42501)', 0, 1);
  EXCEPTION
    WHEN insufficient_privilege THEN
      -- Correct denial path — RLS rejected the write. PASS.
      PERFORM pg_temp.assert_count(
        'T3.1 Anon INSERT denied by RLS (SQLSTATE 42501)', 0, 0);
    WHEN OTHERS THEN
      -- Wrong failure mode (e.g. CHECK violation, FK error, permission
      -- error on a different object). Do NOT silently pass — record a
      -- FAIL and surface the actual SQLSTATE + message so we can tell
      -- exactly why this happened.
      GET STACKED DIAGNOSTICS
        v_sqlstate = RETURNED_SQLSTATE,
        v_message  = MESSAGE_TEXT;
      RAISE WARNING
        'T3.1 wrong failure mode — SQLSTATE=%, MESSAGE=%',
        v_sqlstate, v_message;
      PERFORM pg_temp.assert_count(
        'T3.1 Anon INSERT denied by RLS (SQLSTATE 42501)', 0, 1);
  END;
END;
$$;

-- Drop back to privileged role for the remaining CHECK-constraint tests
-- (those are constraint checks, not RLS — running them as service role
-- isolates the failure mode to CHECK rather than RLS denial).
RESET ROLE;


-- =====================================================================
-- T4 — Topic CHECK rejects bad slug for given subject+paper
-- =====================================================================
-- 'homeostasis' is a valid biology topic — but only on paper_2. Trying
-- to file it under paper_1 must violate revision_materials_topic_check.

DO $$
BEGIN
  BEGIN
    INSERT INTO public.revision_materials (
      title, subject, pathway, tier, paper, topic, material_type, file_path
    )
    VALUES (
      'Mis-tagged: homeostasis under biology paper_1',
      'biology', 'combined', 'foundation', 'paper_1', 'homeostasis',
      'notes',
      'should-never-land.pdf'
    );
    PERFORM pg_temp.assert_count('T4.1 Topic CHECK rejects valid-slug-wrong-paper (biology p1 + homeostasis)', 0, 1);
  EXCEPTION WHEN check_violation THEN
    PERFORM pg_temp.assert_count('T4.1 Topic CHECK rejects valid-slug-wrong-paper (biology p1 + homeostasis)', 0, 0);
  END;
END;
$$;

-- Also: a slug that doesn't exist anywhere in the taxonomy.
DO $$
BEGIN
  BEGIN
    INSERT INTO public.revision_materials (
      title, subject, pathway, tier, paper, topic, material_type, file_path
    )
    VALUES (
      'Mis-tagged: nonsense slug',
      'biology', 'combined', 'foundation', 'paper_1', 'made-up-topic',
      'notes',
      'should-never-land.pdf'
    );
    PERFORM pg_temp.assert_count('T4.2 Topic CHECK rejects fully-invalid slug', 0, 1);
  EXCEPTION WHEN check_violation THEN
    PERFORM pg_temp.assert_count('T4.2 Topic CHECK rejects fully-invalid slug', 0, 0);
  END;
END;
$$;


-- =====================================================================
-- T5 — space + combined CHECK rejects (content-gating)
-- =====================================================================
-- Space Physics is Triple-only. Combined students must never see it.
-- The dedicated space-triple-only CHECK must reject this.

DO $$
BEGIN
  BEGIN
    INSERT INTO public.revision_materials (
      title, subject, pathway, tier, paper, topic, material_type, file_path
    )
    VALUES (
      'Mis-pathway: space under Combined',
      'physics', 'combined', 'higher', 'paper_2', 'space',
      'notes',
      'should-never-land.pdf'
    );
    PERFORM pg_temp.assert_count('T5.1 Space+Combined CHECK rejects (content gating)', 0, 1);
  EXCEPTION WHEN check_violation THEN
    PERFORM pg_temp.assert_count('T5.1 Space+Combined CHECK rejects (content gating)', 0, 0);
  END;
END;
$$;


-- =====================================================================
-- SECTION C — SUMMARY
-- =====================================================================
-- RESET ROLE was already done above; this is a belt-and-braces reset
-- before we read the temp table for the summary.

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
  RAISE NOTICE '  MRB-62 revision_materials TEST SUMMARY';
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
    RAISE NOTICE '  ✓ All assertions passed. Pattern B + taxonomy CHECKs hold.';
  END IF;
END;
$$;

-- Final result set — authoritative output, sorted so failures float up.
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
