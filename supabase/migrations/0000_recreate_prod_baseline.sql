-- =====================================================================
-- Pre-Test Scaffolding: 0000_recreate_prod_baseline.sql
-- For:    Stage 1 testing on the empty test project (qeppkiswvclkkwbxmlok)
-- Why:    The test project is empty. The real migration assumes production's
--         starting shape exists. This file recreates that shape, faithfully,
--         before the real migration runs.
-- DO NOT: Apply this to production. It is scaffolding, not a migration.
-- Drop on completion: this exists only for the test session.
-- =====================================================================
--
-- This file recreates the EXACT pre-migration state of production:
--   - public.profiles with the 21 columns recon found
--   - public.schools with the 6 columns recon found
--   - The 3 existing RLS policies on profiles
--   - RLS enabled on both tables (matching production)
--   - 5 fake legacy profile rows (simulating the 33 in production)
--
-- After this file runs, the test project should respond to a recon query
-- exactly like production did.
-- =====================================================================

BEGIN;

-- =====================================================================
-- 1 — auth.users fake rows
-- =====================================================================
-- profiles.id has a FK to auth.users.id, so we need users first.
-- These IDs are deterministic so we can reference them later.
-- =====================================================================

INSERT INTO auth.users (
  id, email, raw_user_meta_data, aud, role,
  email_confirmed_at, created_at, updated_at,
  instance_id
) VALUES
  ('11111111-aaaa-aaaa-aaaa-111111111111', 'legacy1@example.test', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000'),
  ('22222222-aaaa-aaaa-aaaa-222222222222', 'legacy2@example.test', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000'),
  ('33333333-aaaa-aaaa-aaaa-333333333333', 'legacy3@example.test', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000'),
  ('44444444-aaaa-aaaa-aaaa-444444444444', 'legacy4@example.test', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000'),
  ('55555555-aaaa-aaaa-aaaa-555555555555', 'legacy5@example.test', '{}'::jsonb, 'authenticated', 'authenticated', now(), now(), now(), '00000000-0000-0000-0000-000000000000')
ON CONFLICT (id) DO NOTHING;


-- =====================================================================
-- 2 — public.schools (matches production recon Query 2)
-- =====================================================================
CREATE TABLE public.schools (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at    timestamptz DEFAULT now(),
  name          text NOT NULL,
  code          text NOT NULL,
  admin_user_id uuid,
  active        boolean DEFAULT true
);

ALTER TABLE public.schools ENABLE ROW LEVEL SECURITY;
-- Note: production has RLS enabled but no policies on schools yet.


-- =====================================================================
-- 3 — public.profiles (matches production recon Query 1)
-- =====================================================================
-- 21 columns, exact shape, exact defaults.
-- =====================================================================

CREATE TABLE public.profiles (
  id              uuid PRIMARY KEY REFERENCES auth.users(id),
  created_at      timestamptz DEFAULT now(),
  updated_at      timestamptz DEFAULT now(),
  first_name      text,
  last_name       text,
  avatar_url      text,
  school_name     text,
  year_group      text,
  teacher_name    text,
  school_code     text,
  exam_board      text DEFAULT 'AQA'::text,
  science_pathway text DEFAULT 'combined'::text,
  tier            text DEFAULT 'higher'::text,
  target_grade    smallint,
  strengths       text[],
  weaknesses      text[],
  recent_results  text,
  personal_note   text,
  total_xp        integer DEFAULT 0,
  streak_days     smallint DEFAULT 0,
  last_active     timestamptz DEFAULT now()
);

ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- The 3 RLS policies that exist on production (recon Query 4)
CREATE POLICY "Users can insert own profile" ON public.profiles
  FOR INSERT WITH CHECK (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON public.profiles
  FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can view own profile" ON public.profiles
  FOR SELECT USING (auth.uid() = id);


-- =====================================================================
-- 4 — Seed 5 fake legacy profiles (stand-ins for the 33 in production)
-- =====================================================================
-- These will get key_stage='KS4' backfilled by the real migration,
-- proving the backfill logic works.
-- =====================================================================

INSERT INTO public.profiles (
  id, first_name, last_name, school_name, year_group, teacher_name,
  exam_board, science_pathway, tier, total_xp
) VALUES
  ('11111111-aaaa-aaaa-aaaa-111111111111', 'Legacy', 'One',   'Old Free Text School A', '10', 'Mr Old', 'AQA', 'combined', 'higher', 100),
  ('22222222-aaaa-aaaa-aaaa-222222222222', 'Legacy', 'Two',   'Old Free Text School A', '11', 'Ms Old', 'AQA', 'triple',   'higher', 250),
  ('33333333-aaaa-aaaa-aaaa-333333333333', 'Legacy', 'Three', 'Old Free Text School B', '10', NULL,     'AQA', 'combined', 'foundation', 50),
  ('44444444-aaaa-aaaa-aaaa-444444444444', 'Legacy', 'Four',  NULL,                      '11', NULL,     'AQA', 'combined', 'higher', 0),
  ('55555555-aaaa-aaaa-aaaa-555555555555', 'Legacy', 'Five',  'Old Free Text School C', '10', 'Mrs X',  'AQA', 'triple',   'higher', 175);


COMMIT;

-- =====================================================================
-- Verification queries (run after this file completes):
--
--   SELECT count(*) FROM public.profiles;     -- should return 5
--   SELECT count(*) FROM public.schools;      -- should return 0
--   SELECT count(*) FROM pg_policies WHERE tablename = 'profiles';  -- 3
--
-- Once verified, run 0001_schools_layer.sql, then 0001_schools_layer_tests.sql.
-- =====================================================================
