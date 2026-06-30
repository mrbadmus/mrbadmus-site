-- =====================================================================
-- Migration:        20260530140400_stage3_import_helpers.sql
-- Stage:            3 — Schools Onboarding (CSV import support)
-- Apply target:     TEST project (qeppkiswvclkkwbxmlok) first → prod later
-- Author:           Drafted with Mide, 30 May 2026
-- =====================================================================
--
-- The roster-import Edge Function reconciles in TypeScript using the
-- service role (which bypasses RLS for profiles/classes/class_members).
-- The ONE thing PostgREST cannot do for it is look up an existing
-- auth.users id by email (the auth schema is not exposed over REST), so
-- this migration adds a single privileged helper for that.
-- =====================================================================

BEGIN;

CREATE OR REPLACE FUNCTION public.user_id_for_email(p_email text)
RETURNS uuid
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public, auth
AS $$
  SELECT id FROM auth.users
  WHERE lower(email) = lower(trim(p_email))
  LIMIT 1;
$$;

COMMENT ON FUNCTION public.user_id_for_email(text) IS
  'Stage 3 CSV import: resolves an existing auth.users id by email (case-insensitive). service_role only — used by the roster-import Edge Function to find-or-create student accounts idempotently.';

REVOKE EXECUTE ON FUNCTION public.user_id_for_email(text) FROM public, anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.user_id_for_email(text) TO service_role;

COMMIT;
