-- =====================================================================
-- MRB-138 — Rollback for the usernames migration set
-- =====================================================================
-- Manual undo only (the Supabase CLI never reads supabase/rollbacks/).
-- Reverses, in dependency order, everything added by:
--   20260724120000_usernames_schema.sql
--   20260724120100_usernames_backfill.sql   (data only — nothing to undo)
--   20260724120200_usernames_notnull.sql
-- =====================================================================

BEGIN;

DROP TRIGGER IF EXISTS trg_profiles_username_guard ON public.profiles;

DROP FUNCTION IF EXISTS public.set_username(text);
DROP FUNCTION IF EXISTS public.username_available(text);
DROP FUNCTION IF EXISTS public.profiles_username_guard();
DROP FUNCTION IF EXISTS public.assign_unique_username();
DROP FUNCTION IF EXISTS public.generate_username();
DROP FUNCTION IF EXISTS public.username_rejection_reason(text);

DROP INDEX IF EXISTS public.idx_profiles_username;

ALTER TABLE public.profiles DROP COLUMN IF EXISTS last_username_change_at;
ALTER TABLE public.profiles DROP COLUMN IF EXISTS username;

COMMIT;
