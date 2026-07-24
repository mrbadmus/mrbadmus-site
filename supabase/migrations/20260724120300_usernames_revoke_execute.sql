-- Revoke EXECUTE on the username helper/trigger functions from client roles.
--
-- Why: generate_username(), assign_unique_username() and profiles_username_guard()
-- are internal. assign_unique_username() and profiles_username_guard() run only as
-- row triggers on public.profiles; generate_username() is a SECURITY DEFINER helper
-- they call. None is meant to be invoked directly by a signed-in browser client, yet
-- PostgreSQL grants EXECUTE to anon/authenticated by default for public-schema
-- functions. The Supabase database linter flags that as a warning. Revoking EXECUTE
-- from the client roles quiets the advisory without changing behaviour (the trigger
-- path still runs as the table owner via SECURITY DEFINER). Additive and safe:
-- REVOKE of a grant that is not present is a no-op, so this is idempotent.

BEGIN;

REVOKE EXECUTE ON FUNCTION public.generate_username()       FROM anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.assign_unique_username()  FROM anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.profiles_username_guard() FROM anon, authenticated;

-- profiles_username_guard also carried a PUBLIC execute grant (generate_username and
-- assign_unique_username were already revoked from PUBLIC in 20260724120000_usernames_schema.sql).
-- Without this, anon/authenticated keep EXECUTE via PUBLIC membership and the advisory is
-- NOT quieted for this function — verified on prod 2026-07-24 with has_function_privilege().
REVOKE EXECUTE ON FUNCTION public.profiles_username_guard() FROM PUBLIC;

COMMIT;

-- Verify (proacl for these three should no longer list anon/authenticated with EXECUTE):
--   SELECT n.nspname, p.proname, p.proacl
--   FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
--   WHERE p.proname IN ('generate_username','assign_unique_username','profiles_username_guard');
