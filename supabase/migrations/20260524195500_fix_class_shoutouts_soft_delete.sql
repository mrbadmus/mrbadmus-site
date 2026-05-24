-- =====================================================================
-- Migration:        20260524195500_fix_class_shoutouts_soft_delete.sql
-- Stage:            2C — Class shoutouts (MRB-46) — Phase 2 bugfix
-- Branch:           schools/mrb-46-phase-2-compose-ui
-- Apply target:     TEST PROJECT ONLY (qeppkiswvclkkwbxmlok)
-- DO NOT APPLY ON:  PRODUCTION (urklkrwevjtlfbwnipjn) until MRB-35
--                   (Stage 2C bundle merge) — held branch, see CLAUDE.md
-- Linear:           MRB-46 (Phase 2 — discovered while wiring soft-delete UI)
-- Author:           Drafted with Mide on 2026-05-24
-- =====================================================================
--
-- Fixes a Phase 1 RLS bug surfaced during Phase 2's soft-delete wiring:
-- the soft-delete UPDATE (`SET deleted_at = now()`) fails with
-- "new row violates row-level security policy for table class_shoutouts"
-- even when the caller is the author of the row.
--
-- ── Root cause ──────────────────────────────────────────────────────
-- PostgreSQL applies the SELECT policy's USING clause to the NEW row
-- state during UPDATE — even without RETURNING — to prevent
-- information-leak via update-into-invisibility. The Phase 1 SELECT
-- policy filters `deleted_at IS NULL`; a soft-delete sets `deleted_at`
-- to NOT NULL, so the new row state fails the SELECT USING check and
-- Postgres rejects the UPDATE.
--
-- Verified via SQL repro: `UPDATE ... SET updated_at = now()` succeeds
-- (no deleted_at change), but `UPDATE ... SET deleted_at = now()`
-- fails — same row, same auth, only the column being set differs.
--
-- ── Fix ─────────────────────────────────────────────────────────────
-- Extend the SELECT policy to allow the row's AUTHOR to see their own
-- soft-deleted rows. This lets the post-update row pass the SELECT
-- USING check (because the author is doing the UPDATE), without
-- exposing soft-deleted content to other class members or teachers.
--
-- Net effect:
--   - Teachers + active members still see only non-deleted rows.
--   - The author of a row sees that row even after they soft-delete
--     it (technically true at the RLS level; the frontend continues to
--     filter `deleted_at IS NULL` defensively, so UX is unchanged).
--   - Soft-delete UPDATEs by the author no longer trip the WITH CHECK
--     phantom-failure.
--
-- ── Design intent reaffirmed ────────────────────────────────────────
-- The original "soft-deleted hidden from EVERYONE" intent becomes
-- "hidden from everyone except the author who deleted them" — arguably
-- more correct: the author should be able to query what they deleted
-- if they care. The narrow widening is acceptable security-wise
-- because the content was originally visible to the same class anyway.
--
-- ── What did NOT change ─────────────────────────────────────────────
-- INSERT policy: unchanged. UPDATE policy: unchanged. The fix is
-- entirely on the SELECT policy.
--
-- Wrapped in a single transaction. DROP + CREATE is idempotent for
-- the policy slot.
-- =====================================================================

BEGIN;

DROP POLICY IF EXISTS class_shoutouts_select ON public.class_shoutouts;

CREATE POLICY class_shoutouts_select
  ON public.class_shoutouts FOR SELECT
  USING (
    -- Active (non-deleted) rows: visible to teachers + active members
    (deleted_at IS NULL
       AND (auth_user_teaches_class(class_id)
            OR auth_user_is_member_of_class(class_id)))
    OR
    -- Soft-deleted rows: visible to the author only (so author UPDATEs
    -- that set deleted_at pass Postgres's new-row visibility check)
    (deleted_at IS NOT NULL AND author_id = auth.uid())
  );

COMMIT;
