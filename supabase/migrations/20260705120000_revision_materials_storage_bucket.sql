-- =====================================================================
-- Migration:        20260705120000_revision_materials_storage_bucket.sql
-- Stage:            MRB-63 — Revision Materials Library (storage bucket)
-- Branch:           platform/revision-materials
-- Designed against: MRB-61 SPEC FROZEN (16 May 2026) + ADR
--                   docs/adr/revision-materials.md (storage decision).
-- Follows:          20260517015749_revision_materials.sql (table + RLS).
-- =====================================================================
--
-- Creates the PRIVATE Storage bucket that holds the file bytes for the
-- revision-materials library, plus the RLS read policy that implements
-- Pattern B gating:
--
--   • Table metadata (revision_materials) SELECT is PUBLIC — marketing
--     surface, anyone can browse the list.
--   • The bucket is PRIVATE. Only authenticated users may read objects,
--     which is what lets a logged-in session mint a short-lived signed
--     URL. Anon has NO storage policy => cannot read or deep-link files.
--   • Writes (uploads) are service-role only. service_role bypasses RLS;
--     no INSERT/UPDATE/DELETE policy is granted to clients.
--
-- Object key convention (locked in the ADR):
--   {pathway}/{tier}/{subject}/{paper}/{topic}/{material_type}/{uuid}-{slug}.{ext}
--
-- NB: no seed/placeholder rows are inserted. The table is left empty;
-- Mide registers real materials via the documented upload workflow.
-- =====================================================================

BEGIN;

-- 1. PRIVATE BUCKET ----------------------------------------------------
INSERT INTO storage.buckets (id, name, public)
VALUES ('revision-materials', 'revision-materials', false)
ON CONFLICT (id) DO NOTHING;

-- 2. STORAGE RLS -------------------------------------------------------
-- Authenticated users may read objects in this bucket. This grant is what
-- permits signed-URL creation from an authenticated session. Anon gets no
-- policy => the raw bytes are never reachable by a logged-out visitor,
-- even with a leaked object key.
CREATE POLICY "revision_materials_auth_read"
  ON storage.objects
  FOR SELECT
  TO authenticated
  USING (bucket_id = 'revision-materials');

-- No INSERT/UPDATE/DELETE policies => clients cannot write. Uploads happen
-- via the service role (Supabase dashboard / admin), which bypasses RLS.

COMMIT;

-- =====================================================================
-- POST-APPLY VERIFICATION (read-only; do NOT test with a live insert)
-- =====================================================================
--   SELECT id, name, public FROM storage.buckets WHERE id='revision-materials';
--   SELECT policyname, roles, cmd FROM pg_policies
--     WHERE schemaname='storage' AND tablename='objects'
--       AND policyname='revision_materials_auth_read';
-- =====================================================================
