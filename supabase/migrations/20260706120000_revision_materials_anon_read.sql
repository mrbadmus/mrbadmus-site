-- =====================================================================
-- Migration:        20260706120000_revision_materials_anon_read.sql
-- Stage:            MRB-64/66 follow-up — open revision materials to
--                   logged-out visitors for PREVIEW.
-- Follows:          20260705120000_revision_materials_storage_bucket.sql
-- Applied on prod:  via MCP apply_migration on 2026-07-06 (project
--                   urklkrwevjtlfbwnipjn). Checked in for history parity;
--                   idempotent, so a later `supabase db push` is safe.
-- =====================================================================
--
-- Product change: the Revision Materials page now shows an "Open" button
-- alongside "Download". Open must work for everyone (marketing surface),
-- so anon needs SELECT on the bucket to mint a short-lived signed URL.
--
-- The original bucket migration granted read only to `authenticated` and
-- deliberately left anon with no policy. That decision is superseded here.
-- Download remains a UI-level sign-up nudge (see revision.html) — this
-- policy makes file bytes reachable by anyone, which is the accepted
-- trade-off (an opened PDF can be saved from the browser anyway).
--
-- Scope: this one bucket only. No other bucket, table, or role is touched.
-- =====================================================================

BEGIN;

DROP POLICY IF EXISTS "revision_materials_anon_read" ON storage.objects;

CREATE POLICY "revision_materials_anon_read"
  ON storage.objects
  FOR SELECT
  TO anon
  USING (bucket_id = 'revision-materials');

COMMIT;

-- =====================================================================
-- ROLLBACK (manual): DROP POLICY IF EXISTS "revision_materials_anon_read"
--   ON storage.objects;  -- reverts to sign-in-required file access.
-- POST-APPLY VERIFICATION (read-only):
--   SELECT policyname, roles, cmd FROM pg_policies
--     WHERE schemaname='storage' AND tablename='objects'
--       AND policyname='revision_materials_anon_read';
-- =====================================================================
