-- =====================================================================
-- MRB-138 — Enforce username NOT NULL (after backfill)
-- =====================================================================
-- Safe because:
--   • _usernames_backfill.sql filled every existing row, AND
--   • the BEFORE INSERT guard trigger (trg_profiles_username_guard) fills
--     username on every new insert path before the constraint is checked
--     (auth signup trigger, roster import, account-claims merge).
--
-- Apply AFTER _usernames_backfill.sql. Guarded so it errors loudly rather
-- than half-applying if any NULL remains.
-- =====================================================================

BEGIN;

DO $$
DECLARE
  remaining int;
BEGIN
  SELECT count(*) INTO remaining FROM public.profiles WHERE username IS NULL;
  IF remaining > 0 THEN
    RAISE EXCEPTION 'Refusing to set NOT NULL: % profile(s) still have a NULL username. Run the backfill first.', remaining;
  END IF;
END;
$$;

ALTER TABLE public.profiles ALTER COLUMN username SET NOT NULL;

COMMIT;

-- Verify:
--   SELECT is_nullable FROM information_schema.columns
--    WHERE table_name = 'profiles' AND column_name = 'username';   -- NO
