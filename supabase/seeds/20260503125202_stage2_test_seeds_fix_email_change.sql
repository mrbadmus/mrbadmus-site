-- =====================================================================
-- Migration:        0005_stage2_test_seeds_fix_email_change.sql
-- Stage:            2A — second hotfix for MRB-37 (sign-in still broken)
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) — fake test users only
-- Linear:           MRB-37 (sub-issue of MRB-19)
-- =====================================================================
--
-- Follow-up to 0004. After 0004 set six text token columns to '',
-- GoTrue's signin Scan moved on and choked on a seventh column we
-- missed: email_change.
--
-- ── The bug (cont'd from 0004) ───────────────────────────────────────
-- New error after 0004 applied:
--   "Scan error on column index 8, name 'email_change':
--    converting NULL to string is unsupported"
--
-- email_change is the new email a user is in the process of changing TO
-- (set when a user requests an email change, cleared on confirmation).
-- GoTrue's User struct types it as a non-nullable Go string. Real
-- signups insert it as ''; our 0002 INSERT omitted it, leaving NULL.
--
-- ── Why we missed it in 0004 ─────────────────────────────────────────
-- 0004's column list was drafted from the original error message
-- (confirmation_token) plus the obvious sibling token columns. We
-- treated email_change_token_new / email_change_token_current as
-- "the email-change-related text columns" and overlooked email_change
-- itself, which is a sibling of those two but stores the actual new
-- email (not a token).
--
-- Confirmed via prod comparison: 0 of 33 working prod users have
-- email_change = NULL; all 8 of our test users did. Single-column gap.
--
-- ── The fix ──────────────────────────────────────────────────────────
-- UPDATE the 8 seeded users to set email_change to '' (empty string).
-- Pure data fix, single column.
--
-- ── Idempotent ───────────────────────────────────────────────────────
-- WHERE-clause guard: only updates rows where email_change is still
-- NULL. First run sets it; subsequent runs no-op.
--
-- ── Production safety ────────────────────────────────────────────────
-- Targets only the 8 deterministic test UUIDs. Even if this migration
-- accidentally ran on prod, it would match zero rows.
-- =====================================================================

BEGIN;

-- 0 — Pre-flight: refuse to run unless 0004 already applied.
--     0004 set Sarah's confirmation_token to ''. Sarah existing proves
--     0002 ran; her confirmation_token being '' (not NULL, not anything
--     else) proves 0004 ran. Both gates in one query.
DO $$
DECLARE
  v_sarah_confirmation_token text;
BEGIN
  SELECT confirmation_token INTO v_sarah_confirmation_token
  FROM auth.users
  WHERE id = '20000000-0000-0000-0000-000000000001';

  IF v_sarah_confirmation_token IS NULL OR v_sarah_confirmation_token <> '' THEN
    RAISE EXCEPTION '0004 must be applied first: Sarah Whitfield (20000000-...-001) does not have confirmation_token = '''' (got %)', coalesce(v_sarah_confirmation_token, 'NULL');
  END IF;
END $$;

-- 1 — Set email_change to '' on the 8 seeded users.
--     WHERE filter makes this strictly idempotent: subsequent runs no-op.
UPDATE auth.users
SET
  email_change = '',
  updated_at   = now()
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
AND email_change IS NULL;

COMMIT;

-- =====================================================================
-- VERIFICATION QUERIES (run after apply)
--
--   -- 1. Zero rows with email_change still NULL on the 8 seeded users
--   SELECT count(*) FROM auth.users
--   WHERE id IN (
--     '20000000-0000-0000-0000-000000000001',
--     '21000000-0000-0000-0000-000000000001','21000000-0000-0000-0000-000000000002',
--     '21000000-0000-0000-0000-000000000003','21000000-0000-0000-0000-000000000004',
--     '21000000-0000-0000-0000-000000000005','21000000-0000-0000-0000-000000000006',
--     '21000000-0000-0000-0000-000000000007'
--   ) AND email_change IS NULL;                          -- expect 0
--
--   -- 2. All 8 users have email_change = '' (empty string)
--   SELECT count(*) FROM auth.users
--   WHERE id IN (
--     '20000000-0000-0000-0000-000000000001',
--     '21000000-0000-0000-0000-000000000001','21000000-0000-0000-0000-000000000002',
--     '21000000-0000-0000-0000-000000000003','21000000-0000-0000-0000-000000000004',
--     '21000000-0000-0000-0000-000000000005','21000000-0000-0000-0000-000000000006',
--     '21000000-0000-0000-0000-000000000007'
--   ) AND email_change = '';                             -- expect 8
--
--   -- 3. Live test: sign in via auth.html (localhost = test mode)
--   --    email:    teacher@test-rainford.local
--   --    password: TestPass!2026
-- =====================================================================
