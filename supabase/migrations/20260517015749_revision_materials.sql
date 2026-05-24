-- =====================================================================
-- Migration:        0007_revision_materials.sql
-- Stage:            MRB-60 — Revision Materials Library (table + RLS only)
-- Branch:           platform/revision-materials
-- Designed against: MRB-61 SPEC FROZEN (16 May 2026)
-- Apply target:     TEST project (qeppkiswvclkkwbxmlok) first.
--                   PROD apply is a separate approved step, not this file.
-- Author:           Drafted with Mide on Saturday 16 May 2026
-- =====================================================================
--
-- Creates the public-facing revision_materials table (metadata only — the
-- Storage bucket is MRB-63). Pattern B access model:
--   • SELECT: public (anon + authenticated) — marketing surface
--   • INSERT/UPDATE/DELETE: service role only (no client policies)
-- The bucket holding the file bytes will be PRIVATE; file access is gated
-- separately from metadata.
--
-- Conventions inherited from schools-layer (0001):
--   • enum-by-CHECK rather than Postgres enum types
--   • content rows use `pathway` (not `science_pathway`)
--   • `deleted_at timestamptz` soft delete
--   • single BEGIN/COMMIT transaction
--
-- Topic taxonomy is sourced from SITE_DATA in generate_site_v5.py.
-- See docs/adr/revision-materials.md for the canonical taxonomy table.
-- =====================================================================

BEGIN;

-- 1. TABLE -------------------------------------------------------------
CREATE TABLE public.revision_materials (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  title            text NOT NULL,
  description      text,
  subject          text NOT NULL CHECK (subject IN ('biology','chemistry','physics')),
  pathway          text NOT NULL CHECK (pathway IN ('combined','triple')),
  tier             text NOT NULL CHECK (tier IN ('foundation','higher')),
  paper            text NOT NULL CHECK (paper IN ('paper_1','paper_2')),
  topic            text NOT NULL,
  material_type    text NOT NULL CHECK (material_type IN ('notes','worksheet','mark_scheme','pack','other')),
  file_path        text NOT NULL,
  file_size_bytes  bigint,
  school_id        uuid REFERENCES public.schools(id),
  created_at       timestamptz NOT NULL DEFAULT now(),
  deleted_at       timestamptz,

  -- topic must be a canonical AQA slug for the given (subject, paper).
  -- Mirrors SITE_DATA in generate_site_v5.py; full table in
  -- docs/adr/revision-materials.md. Update both in lock-step.
  CONSTRAINT revision_materials_topic_check CHECK (
       (subject = 'biology'   AND paper = 'paper_1' AND topic IN ('cell-biology','organisation','infection-response','bioenergetics'))
    OR (subject = 'biology'   AND paper = 'paper_2' AND topic IN ('homeostasis','inheritance','ecology'))
    OR (subject = 'chemistry' AND paper = 'paper_1' AND topic IN ('atomic-structure','bonding','quantitative','chemical-changes','energy-changes'))
    OR (subject = 'chemistry' AND paper = 'paper_2' AND topic IN ('rates-equilibrium','organic','analysis','atmosphere','resources'))
    OR (subject = 'physics'   AND paper = 'paper_1' AND topic IN ('energy','electricity','particle-model','atomic-structure'))
    OR (subject = 'physics'   AND paper = 'paper_2' AND topic IN ('forces','waves','magnetism','space'))
  ),

  -- Physics "space" is Triple-only — block accidental Combined uploads.
  -- Content-gating: Combined students must never see Space Physics.
  CONSTRAINT revision_materials_space_triple_only_check CHECK (
    NOT (subject = 'physics' AND topic = 'space' AND pathway = 'combined')
  )
);

COMMENT ON TABLE public.revision_materials IS
  'Public revision-materials library metadata. SELECT is public; writes service-role-only. File bytes live in the PRIVATE revision-materials Storage bucket (MRB-63).';

-- Filter index for the public list page (subject/pathway/tier/paper/topic/type).
CREATE INDEX revision_materials_filter_idx
  ON public.revision_materials (subject, pathway, tier, paper, topic, material_type)
  WHERE deleted_at IS NULL;

-- Index for newest-first ordering.
CREATE INDEX revision_materials_created_at_idx
  ON public.revision_materials (created_at DESC)
  WHERE deleted_at IS NULL;


-- 2. RLS ---------------------------------------------------------------
ALTER TABLE public.revision_materials ENABLE ROW LEVEL SECURITY;

-- Public SELECT — anon + authenticated. Soft-deleted rows hidden.
CREATE POLICY revision_materials_public_read
  ON public.revision_materials
  FOR SELECT
  TO anon, authenticated
  USING (deleted_at IS NULL);

-- No INSERT/UPDATE/DELETE policies => no client can write.
-- service_role bypasses RLS, which is how legitimate writes happen.

COMMIT;


-- =====================================================================
-- POST-APPLY VERIFICATION
-- =====================================================================
-- Run supabase/tests/0007_revision_materials_tests.sql against the TEST
-- project after this migration. That file executes the acceptance
-- assertions (anon SELECT succeeds, anon INSERT denied, topic CHECK
-- rejects bad slug, space+combined CHECK rejects, valid row inserts
-- cleanly) inside BEGIN/ROLLBACK so no data persists.
--
-- Then recount all public tables to confirm exactly ONE table was added
-- and no other tables were touched:
--   SELECT count(*) FROM pg_tables WHERE schemaname='public';
--   SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename;
