-- =====================================================================
-- MRB-138 — Public usernames: schema, generator, moderation, RPCs, guard
-- =====================================================================
-- Adds a public username to profiles + the machinery to generate, validate
-- and change it. RLS policies are UNCHANGED. The SECURITY DEFINER functions
-- deliberately bypass RLS internally so the public site can (a) check whether
-- a handle is free and (b) let a signed-in user change their own handle —
-- without exposing any other row.
--
-- Storage model: `username` is CITEXT so uniqueness is case-insensitive
-- ("frostpixel" == "FrostPixel") while the display capitalisation is preserved.
--
-- Apply order: this file → _usernames_backfill.sql → _usernames_notnull.sql
-- SAFEGUARDING: the moderation here mirrors shared/username-generator.js. Keep
-- the two in sync. This is the server-side gate (a client-only filter is
-- trivially bypassed).
-- =====================================================================

BEGIN;

CREATE EXTENSION IF NOT EXISTS citext;

-- 1 ── Columns (nullable for now; NOT NULL comes after backfill) ────────
ALTER TABLE public.profiles ADD COLUMN IF NOT EXISTS username citext;
ALTER TABLE public.profiles ADD COLUMN IF NOT EXISTS last_username_change_at timestamptz;

-- Case-insensitive uniqueness + fast lookup. NULLs coexist pre-backfill.
CREATE UNIQUE INDEX IF NOT EXISTS idx_profiles_username ON public.profiles (username);

-- 2 ── Moderation: returns a plain-English reason, or NULL if OK ─────────
-- Mirrors shared/username-generator.js. Immutable + no table reads → safe to
-- grant broadly. Normalisation maps leetspeak and strips separators so
-- "sh1t" / "s-h-i-t" / "s h i t" all collapse to "shit" before matching.
CREATE OR REPLACE FUNCTION public.username_rejection_reason(candidate text)
RETURNS text
LANGUAGE plpgsql
IMMUTABLE
SET search_path = pg_catalog, public
AS $$
DECLARE
  raw  text := btrim(coalesce(candidate, ''));
  norm text;
BEGIN
  IF raw = '' THEN RETURN 'Please enter a username.'; END IF;

  -- PII / real-name patterns run on the RAW input.
  IF position('@' in raw) > 0 THEN
    RETURN 'That looks like an email — pick a nickname instead.';
  END IF;
  IF raw ~ '(\d[ -]?){7,}' THEN
    RETURN 'That looks like a phone number — pick a nickname instead.';
  END IF;
  IF raw ~ '^[A-Z][a-z]+[ ._-]+[A-Z][a-z]+' THEN
    RETURN 'Please use a nickname, not your real name.';
  END IF;

  -- Format: start with a letter, letters/digits only, 3–20 chars.
  IF raw ~ '\s' THEN RETURN 'No spaces — try joining the words (e.g. FrostPixel).'; END IF;
  IF raw !~ '^[A-Za-z][A-Za-z0-9]*$' THEN RETURN 'Letters and numbers only — no symbols.'; END IF;
  IF char_length(raw) < 3 THEN RETURN 'Too short — use at least 3 characters.'; END IF;
  IF char_length(raw) > 20 THEN RETURN 'Too long — keep it to 20 characters or fewer.'; END IF;

  -- Normalise for banned-word matching.
  norm := regexp_replace(translate(lower(raw), '013457', 'oieast'), '[^a-z]', '', 'g');
  IF char_length(norm) < 2 THEN RETURN 'Please choose a longer nickname.'; END IF;

  -- Unambiguous offensive substrings (never inside ordinary words).
  IF norm ~ ('(fuck|shit|bitch|bastard|cunt|wank|wanker|bollock|bugger|asshole|'
           || 'arsehole|twat|slut|whore|douche|dildo|boob|penis|vagina|jizz|orgasm|'
           || 'porn|blowjob|handjob|dumbass|jackass|bullshit|dipshit|shithead|'
           || 'motherfuck|cocksuck|dickhead|knobhead|bellend|minge|tosser|piss|'
           || 'sexy|sexual|cameltoe|nigger|nigga|faggot|fagot|retard|spastic|gook|'
           || 'kike|wetback|tranny|rapist|raping|molest|pedo|paedo|hitler|nazi|kkk|'
           || 'cocaine|heroin|ganja|methhead)') THEN
    RETURN 'That username isn''t allowed — please pick something friendlier.';
  END IF;

  -- Short / ambiguous words: exact whole-handle match only (so "Peacock",
  -- "Raccoon", "Methane", "Uranus", "Essex", "Scunthorpe-safe" words pass).
  IF norm = ANY (ARRAY[
      'ass','arse','hell','damn','crap','hoe','tit','tits','nut','nuts','pee',
      'poo','poop','anal','anus','butt','cum','sex','fart','turd','meth','crack',
      'weed','kill','killer','rape','raped','rapes','murder','suicide','xxx',
      'milf','thot','std','cock','dick','prick','pussy','coon','paki','pakis',
      'chink','chinky','dyke','isis','slag','fanny','knob','shag','gash']) THEN
    RETURN 'That username isn''t allowed — please pick something friendlier.';
  END IF;

  -- Impersonation of the site / staff.
  IF norm ~ ('(mrbadmusai|mrbadmus|badmus|administrator|admin|moderator|'
           || 'staff|teacher|official|helpdesk|rainford)') THEN
    RETURN 'That name is reserved — please choose a different one.';
  END IF;
  IF norm = ANY (ARRAY['mod','support','system']) THEN
    RETURN 'That name is reserved — please choose a different one.';
  END IF;

  RETURN NULL;
END;
$$;

-- 3 ── Generator (server-side; mirrors the JS pools) ────────────────────
CREATE OR REPLACE FUNCTION public.generate_username()
RETURNS text
LANGUAGE plpgsql
VOLATILE
SET search_path = pg_catalog, public
AS $$
DECLARE
  adjs text[] := ARRAY[
    'Frost','Void','Crimson','Shadow','Ember','Storm','Onyx','Blaze',
    'Lunar','Velvet','Mint','Pearl','Dusk','Coral','Amber','Silk',
    'Falcon','Otter','Comet','Fox','Raven','Tiger','Wolf','Koi',
    'Mango','Waffle','Pixel','Noodle','Bolt','Jelly','Turbo','Cosmo'];
  nouns text[] := ARRAY[
    'Pixel','Pulse','Rift','Byte','Wave','Spark','Drift','Quest',
    'Dash','Echo','Orbit','Glide','Flare','Ripple','Nova','Prism',
    'Beam','Trail','Loop','Harbor','Meadow','Summit','River','Cove'];
  a text;
  n text;
BEGIN
  a := adjs[1 + floor(random() * array_length(adjs, 1))::int];
  n := nouns[1 + floor(random() * array_length(nouns, 1))::int];
  -- Always append 2 digits: keeps length <= 20 and widens the space for backfill.
  RETURN a || n || (10 + floor(random() * 90))::int::text;
END;
$$;

-- Loops the generator until it finds a free handle (collision retry).
CREATE OR REPLACE FUNCTION public.assign_unique_username()
RETURNS text
LANGUAGE plpgsql
VOLATILE
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  cand  text;
  tries int := 0;
BEGIN
  LOOP
    cand := public.generate_username();
    EXIT WHEN NOT EXISTS (SELECT 1 FROM public.profiles WHERE username = cand::citext);
    tries := tries + 1;
    IF tries > 60 THEN
      -- Vanishingly unlikely; widen with an extra digit and take it.
      cand := cand || floor(random() * 10)::int::text;
      EXIT;
    END IF;
  END LOOP;
  RETURN cand;
END;
$$;

-- 4 ── Guard trigger: fills/sanitises username on EVERY write path ───────
-- INSERT: if no username was supplied, adopt the signup-chosen handle from
--   auth metadata when it is clean + free, otherwise generate one. A supplied
--   handle that fails moderation is replaced (never blocks account creation).
-- UPDATE: a changed username is validated server-side (rejects bad direct writes).
CREATE OR REPLACE FUNCTION public.profiles_username_guard()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  meta_username text;
  reason        text;
BEGIN
  IF TG_OP = 'INSERT' THEN
    IF NEW.username IS NULL THEN
      SELECT raw_user_meta_data ->> 'username' INTO meta_username
        FROM auth.users WHERE id = NEW.id;
      IF meta_username IS NOT NULL
         AND public.username_rejection_reason(meta_username) IS NULL
         AND NOT EXISTS (SELECT 1 FROM public.profiles WHERE username = meta_username::citext) THEN
        NEW.username := meta_username;
      ELSE
        NEW.username := public.assign_unique_username();
      END IF;
    ELSIF public.username_rejection_reason(NEW.username::text) IS NOT NULL THEN
      NEW.username := public.assign_unique_username();
    END IF;

  ELSIF TG_OP = 'UPDATE' THEN
    IF NEW.username IS DISTINCT FROM OLD.username THEN
      IF NEW.username IS NULL THEN
        RAISE EXCEPTION 'Username cannot be blank.';
      END IF;
      reason := public.username_rejection_reason(NEW.username::text);
      IF reason IS NOT NULL THEN
        RAISE EXCEPTION '%', reason;
      END IF;
    END IF;
  END IF;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_profiles_username_guard ON public.profiles;
CREATE TRIGGER trg_profiles_username_guard
  BEFORE INSERT OR UPDATE ON public.profiles
  FOR EACH ROW EXECUTE FUNCTION public.profiles_username_guard();

-- 5 ── RPCs for the frontend ────────────────────────────────────────────
-- Availability check (used live at signup + in settings). Boolean only.
CREATE OR REPLACE FUNCTION public.username_available(candidate text)
RETURNS boolean
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT candidate IS NOT NULL
     AND NOT EXISTS (SELECT 1 FROM public.profiles WHERE username = candidate::citext);
$$;

-- Authoritative change: moderation + school-impersonation + 30-day lock +
-- availability, atomically, for the signed-in user only.
CREATE OR REPLACE FUNCTION public.set_username(candidate text)
RETURNS jsonb
LANGUAGE plpgsql
VOLATILE
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  uid      uuid := auth.uid();
  reason   text;
  sch      text;
  sch_norm text;
  lastc    timestamptz;
  cand     text := btrim(coalesce(candidate, ''));
BEGIN
  IF uid IS NULL THEN
    RETURN jsonb_build_object('ok', false, 'error', 'You need to be signed in.');
  END IF;

  reason := public.username_rejection_reason(cand);
  IF reason IS NOT NULL THEN
    RETURN jsonb_build_object('ok', false, 'error', reason);
  END IF;

  SELECT school_name, last_username_change_at INTO sch, lastc
    FROM public.profiles WHERE id = uid;

  -- Block a student impersonating their own school.
  IF sch IS NOT NULL THEN
    sch_norm := regexp_replace(lower(sch), '[^a-z]', '', 'g');
    IF char_length(sch_norm) >= 4
       AND position(sch_norm in regexp_replace(translate(lower(cand), '013457', 'oieast'), '[^a-z]', '', 'g')) > 0 THEN
      RETURN jsonb_build_object('ok', false, 'error', 'That name is reserved — please choose a different one.');
    END IF;
  END IF;

  -- 30-day lock.
  IF lastc IS NOT NULL AND lastc > now() - interval '30 days' THEN
    RETURN jsonb_build_object(
      'ok', false,
      'error', 'You can change your username again on '
             || to_char((lastc + interval '30 days')::date, 'DD Mon YYYY') || '.');
  END IF;

  -- Availability (defensive; the unique index is the true guarantee).
  IF EXISTS (SELECT 1 FROM public.profiles WHERE username = cand::citext AND id <> uid) THEN
    RETURN jsonb_build_object('ok', false, 'error', 'That username is taken — try another.');
  END IF;

  UPDATE public.profiles
     SET username = cand, last_username_change_at = now()
   WHERE id = uid;

  RETURN jsonb_build_object('ok', true, 'username', cand);
EXCEPTION
  WHEN unique_violation THEN
    RETURN jsonb_build_object('ok', false, 'error', 'That username is taken — try another.');
END;
$$;

-- 6 ── Grants ───────────────────────────────────────────────────────────
REVOKE ALL ON FUNCTION public.generate_username()        FROM public;
REVOKE ALL ON FUNCTION public.assign_unique_username()   FROM public;
GRANT  EXECUTE ON FUNCTION public.username_rejection_reason(text) TO anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.username_available(text)        TO anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.set_username(text)              TO authenticated;

COMMIT;

-- Verify:
--   SELECT public.username_rejection_reason('FrostPixel');   -- NULL (ok)
--   SELECT public.username_rejection_reason('sh1t');         -- friendlier msg
--   SELECT public.username_available('FrostPixel99');        -- true
--   SELECT public.generate_username();                       -- e.g. MangoWave42
