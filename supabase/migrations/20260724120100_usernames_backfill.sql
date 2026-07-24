-- =====================================================================
-- MRB-138 — Backfill: assign a generated handle to every existing user
-- =====================================================================
-- Every profile with a NULL username gets a unique generated handle. Because
-- assign_unique_username() checks the current table on each call, handles
-- assigned earlier in the loop are automatically avoided later — collision
-- retry is inherent. Idempotent: re-running only fills rows still NULL.
--
-- Apply AFTER _usernames_schema.sql, BEFORE _usernames_notnull.sql.
-- =====================================================================

BEGIN;

DO $$
DECLARE
  r         record;
  cand      text;
  filled    int := 0;
BEGIN
  FOR r IN SELECT id FROM public.profiles WHERE username IS NULL LOOP
    cand := public.assign_unique_username();
    UPDATE public.profiles SET username = cand WHERE id = r.id;
    filled := filled + 1;
  END LOOP;
  RAISE NOTICE 'usernames backfill: % row(s) assigned', filled;
END;
$$;

COMMIT;

-- Verify:
--   SELECT count(*) FROM public.profiles WHERE username IS NULL;   -- 0
--   SELECT count(*) FROM (SELECT username FROM public.profiles GROUP BY username HAVING count(*) > 1) d;  -- 0 (no dupes)
--   SELECT id, first_name, username FROM public.profiles ORDER BY created_at LIMIT 10;
