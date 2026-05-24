-- =====================================================================
-- Migration:        0003_stage2_test_passwords.sql
-- Stage:            2A — Phase B testing prep (Gap 1 from MRB-19)
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) — fake test users only
-- Linear:           MRB-19
-- =====================================================================
--
-- Sets a known plaintext password on the 8 fake users seeded by
-- 0002_stage2_test_seeds.sql, so they can sign in via auth.html during
-- Phase B testing of the /teacher/* auth gate.
--
-- ── Password ─────────────────────────────────────────────────────────
--   Plaintext:  TestPass!2026
--   Stored as:  bcrypt hash via pgcrypto's crypt() with cost factor 10
--               (matches GoTrue's default, accepted by Supabase auth)
--
-- All 8 users (Sarah Whitfield + 7 students) get the same password —
-- fine for testing convenience: fake accounts in a sandbox project.
--
-- ── Why pgcrypto? ────────────────────────────────────────────────────
-- Supabase auth (GoTrue) expects bcrypt cost-10 in encrypted_password.
-- pgcrypto's crypt(plain, gen_salt('bf', 10)) produces exactly that
-- format. pgcrypto is enabled by default in every Supabase project,
-- so no CREATE EXTENSION needed.
--
-- ── Why also raw_app_meta_data? ──────────────────────────────────────
-- 0002 inserted these users without raw_app_meta_data. GoTrue's normal
-- signup flow sets it to {"provider":"email","providers":["email"]} and
-- some signin code paths reference it. Setting it defensively here
-- matches a real-signup row's shape and avoids any chance of a
-- "missing provider" failure mode during signin.
--
-- ── Idempotent ───────────────────────────────────────────────────────
-- First run sets encrypted_password + raw_app_meta_data on rows that
-- don't have them yet. Subsequent runs no-op (the WHERE clause filters
-- to NULL/empty passwords only). To rotate the password later, do it
-- manually via Supabase Studio or write a follow-up migration — don't
-- re-run this file expecting different behaviour.
-- =====================================================================

BEGIN;

-- 0 — Pre-flight: refuse to run unless 0002 seeded users are present.
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM auth.users WHERE id = '20000000-0000-0000-0000-000000000001'
  ) THEN
    RAISE EXCEPTION '0002_stage2_test_seeds.sql must be applied first: Sarah Whitfield (20000000-...-001) not found in auth.users';
  END IF;
END $$;

-- 1 — Set bcrypt password + raw_app_meta_data for all 8 test users.
--     WHERE filter makes this strictly idempotent: subsequent runs no-op.
UPDATE auth.users
SET
  encrypted_password = crypt('TestPass!2026', gen_salt('bf', 10)),
  raw_app_meta_data  = '{"provider":"email","providers":["email"]}'::jsonb,
  updated_at         = now()
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
AND (encrypted_password IS NULL OR encrypted_password = '');

COMMIT;

-- =====================================================================
-- VERIFICATION QUERIES (run after apply)
--
--   -- 1. Eight rows now have a non-NULL encrypted_password
--   SELECT count(*) FROM auth.users
--   WHERE encrypted_password IS NOT NULL
--     AND id IN (
--       '20000000-0000-0000-0000-000000000001',
--       '21000000-0000-0000-0000-000000000001','21000000-0000-0000-0000-000000000002',
--       '21000000-0000-0000-0000-000000000003','21000000-0000-0000-0000-000000000004',
--       '21000000-0000-0000-0000-000000000005','21000000-0000-0000-0000-000000000006',
--       '21000000-0000-0000-0000-000000000007'
--     );                                                -- expect 8
--
--   -- 2. The hash actually validates against 'TestPass!2026'.
--   --    crypt(plain, existing_hash) re-hashes plain using the same
--   --    salt extracted from existing_hash — equal only if the plain
--   --    text is what was originally hashed.
--   SELECT count(*) FROM auth.users
--   WHERE id IN (
--     '20000000-0000-0000-0000-000000000001',
--     '21000000-0000-0000-0000-000000000001','21000000-0000-0000-0000-000000000002',
--     '21000000-0000-0000-0000-000000000003','21000000-0000-0000-0000-000000000004',
--     '21000000-0000-0000-0000-000000000005','21000000-0000-0000-0000-000000000006',
--     '21000000-0000-0000-0000-000000000007'
--   ) AND encrypted_password = crypt('TestPass!2026', encrypted_password);
--                                                       -- expect 8
--
--   -- 3. Live test: sign in via auth.html (localhost = test mode)
--   --    email:    teacher@test-rainford.local
--   --    password: TestPass!2026
-- =====================================================================
