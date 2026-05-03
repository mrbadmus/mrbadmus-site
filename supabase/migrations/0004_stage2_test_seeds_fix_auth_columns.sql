-- =====================================================================
-- Migration:        0004_stage2_test_seeds_fix_auth_columns.sql
-- Stage:            2A — incident hotfix for MRB-37 (sign-in broken on test)
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) — fake test users only
-- Linear:           MRB-37 (sub-issue of MRB-19)
-- =====================================================================
--
-- Fixes the sign-in failure for the 8 fake users seeded by 0002.
--
-- ── The bug ──────────────────────────────────────────────────────────
-- 0002 inserted into auth.users without setting six text columns:
--   confirmation_token, recovery_token, email_change_token_new,
--   email_change_token_current, phone_change_token, reauthentication_token.
-- They defaulted to NULL.
--
-- GoTrue's Go User struct types those columns as non-nullable strings.
-- When GoTrue runs SELECT * FROM auth.users WHERE email = ? during
-- signin, sql.Scan crashes on the first NULL it hits with:
--   "Scan error on column index 3, name 'confirmation_token':
--    converting NULL to string is unsupported"
--
-- The 500 surfaces to the user as "Database error querying schema".
-- Real signups never trigger this because GoTrue inserts these columns
-- as empty strings ('') itself. Only direct SQL inserts that omit them
-- leave NULLs.
--
-- ── The fix ──────────────────────────────────────────────────────────
-- UPDATE the 8 seeded users to set all six columns to '' (empty string).
-- Pure data fix, no schema or permission changes. Once applied, signin
-- works against any of the 8 test users.
--
-- ── Idempotent ───────────────────────────────────────────────────────
-- WHERE-clause guard: only updates rows where at least one of the six
-- columns is still NULL. First run sets them; subsequent runs no-op.
--
-- ── Production safety ────────────────────────────────────────────────
-- Targets only the 8 deterministic test UUIDs. Even if this migration
-- accidentally ran on prod, it would match zero rows.
-- =====================================================================

BEGIN;

-- 0 — Pre-flight: refuse to run unless 0002 + 0003 already applied.
--     Sarah's row existing proves 0002 ran; her encrypted_password being
--     non-NULL proves 0003 ran. Both gates in one query.
DO $$
DECLARE
  v_sarah_password text;
BEGIN
  SELECT encrypted_password INTO v_sarah_password
  FROM auth.users
  WHERE id = '20000000-0000-0000-0000-000000000001';

  IF v_sarah_password IS NULL THEN
    RAISE EXCEPTION '0002 + 0003 must be applied first: Sarah Whitfield (20000000-...-001) either does not exist or has no encrypted_password set';
  END IF;
END $$;

-- 1 — Set all six GoTrue token columns to '' on the 8 seeded users.
--     WHERE filter makes this strictly idempotent: subsequent runs no-op.
UPDATE auth.users
SET
  confirmation_token         = '',
  recovery_token             = '',
  email_change_token_new     = '',
  email_change_token_current = '',
  phone_change_token         = '',
  reauthentication_token     = '',
  updated_at                 = now()
WHERE id IN (
  '20000000-0000-0000-0000-000000000001', -- Sarah Whitfield (teacher)
  '21000000-0000-0000-0000-000000000001', -- Amelia Carter
  '21000000-0000-0000-0000-000000000002', -- Oliver Mensah
  '21000000-0000-0000-0000-000000000003', -- Priya Sharma
  '21000000-0000-0000-0000-000000000004', -- Jacob Reid
  '21000000-0000-0000-0000-000000000005', -- Maya Anwar
  '21000000-0000-0000-0000-000000000006', -- Ethan Brooks
  '21000000-0000-0000-0000-000000000007'  -- Sophie Lin
)
AND (
  confirmation_token         IS NULL OR
  recovery_token             IS NULL OR
  email_change_token_new     IS NULL OR
  email_change_token_current IS NULL OR
  phone_change_token         IS NULL OR
  reauthentication_token     IS NULL
);

COMMIT;

-- =====================================================================
-- VERIFICATION QUERIES (run after apply)
--
--   -- 1. Zero rows with any NULL token column among the 8 seeded users
--   SELECT count(*) FROM auth.users
--   WHERE id IN (
--     '20000000-0000-0000-0000-000000000001',
--     '21000000-0000-0000-0000-000000000001','21000000-0000-0000-0000-000000000002',
--     '21000000-0000-0000-0000-000000000003','21000000-0000-0000-0000-000000000004',
--     '21000000-0000-0000-0000-000000000005','21000000-0000-0000-0000-000000000006',
--     '21000000-0000-0000-0000-000000000007'
--   ) AND (
--     confirmation_token IS NULL OR recovery_token IS NULL OR
--     email_change_token_new IS NULL OR email_change_token_current IS NULL OR
--     phone_change_token IS NULL OR reauthentication_token IS NULL
--   );                                                  -- expect 0
--
--   -- 2. All 8 users have all six columns set to '' (empty string)
--   SELECT count(*) FROM auth.users
--   WHERE id IN (
--     '20000000-0000-0000-0000-000000000001',
--     '21000000-0000-0000-0000-000000000001','21000000-0000-0000-0000-000000000002',
--     '21000000-0000-0000-0000-000000000003','21000000-0000-0000-0000-000000000004',
--     '21000000-0000-0000-0000-000000000005','21000000-0000-0000-0000-000000000006',
--     '21000000-0000-0000-0000-000000000007'
--   )
--     AND confirmation_token         = ''
--     AND recovery_token             = ''
--     AND email_change_token_new     = ''
--     AND email_change_token_current = ''
--     AND phone_change_token         = ''
--     AND reauthentication_token     = '';              -- expect 8
--
--   -- 3. Live test: sign in via auth.html (localhost = test mode)
--   --    email:    teacher@test-rainford.local
--   --    password: TestPass!2026
-- =====================================================================
