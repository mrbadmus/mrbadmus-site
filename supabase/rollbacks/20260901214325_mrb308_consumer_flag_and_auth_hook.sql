-- ROLLBACK for MRB-308 Night 1, migration 4 of 6
-- (20260901214325_mrb308_consumer_flag_and_auth_hook). Apply MANUALLY only.
--
-- ======================================================================
-- ⚠️⚠️  READ THIS BEFORE YOU RUN ANYTHING IN THIS FILE.  ⚠️⚠️
--
-- THIS FILE TOUCHES THE LIVE SSO GATE. hook_before_user_created is what
-- every Google and Microsoft sign-in passes through. Get the order wrong and
-- you do not get an error in this window — you get every new Rainford
-- Microsoft signup failing at the door until somebody notices.
--
-- 1. REVERTING THE HOOK IS NOT A `DROP`. There is no earlier definition to
--    fall back to: `create or replace` overwrote it in place. The version
--    that must be restored is the MRB-293 one, installed by
--      supabase/migrations/20260828204639_mrb293_hook_admits_pending_staff.sql
--    and it is reproduced verbatim below so this file can stand alone. If you
--    ever edit it, take the body from that migration, never from memory.
--
-- 2. NEVER DROP platform_flags FIRST. The CURRENT hook calls
--    consumer_signup_enabled(), which reads public.platform_flags. Drop the
--    table (or the function) while the current hook is still registered and
--    the hook raises at execution time — which breaks ALL Google AND Azure
--    signup, not just consumer signup, because the raise happens before any
--    branch returns.
--
-- THE SAFE ORDER, and the order the statements appear in below:
--    (a) restore the MRB-293 hook   — it references neither the function nor
--                                     the table, so once it is in place
--                                     nothing depends on them
--    (b) drop consumer_signup_enabled()
--    (c) drop platform_flags
--
-- After (a), an off-domain Google signup is refused with the 403 again, so
-- no parent can create an account. That is the point of the rollback.
-- ======================================================================

-- (a) Restore the MRB-293 hook. Verbatim from migration 20260828204639.
CREATE OR REPLACE FUNCTION public.hook_before_user_created(event jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
DECLARE
  v_email    text := lower(nullif(trim(event->'user'->>'email'), ''));
  v_provider text := COALESCE(event->'user'->'app_metadata'->>'provider', 'email');
  v_school   uuid;
BEGIN
  -- Non-OAuth creation passes through untouched. This covers BOTH the
  -- existing public email/password signup AND the CSV importer, which uses
  -- the Admin API (provider 'email'). Gating those would deadlock onboarding.
  IF v_provider NOT IN ('azure', 'google') THEN
    RETURN '{}'::jsonb;
  END IF;

  -- From here: a brand-new OAuth (school SSO) user is about to be created.
  -- Pre-provisioned students/staff already exist and LINK rather than create,
  -- so they never reach this branch.

  IF v_email IS NULL THEN
    RETURN jsonb_build_object('error', jsonb_build_object(
      'http_code', 400,
      'message', 'No email address was returned by your sign-in provider. Please try again.'
    ));
  END IF;

  v_school := public.school_id_for_email_domain(v_email);

  IF v_school IS NULL THEN
    RETURN jsonb_build_object('error', jsonb_build_object(
      'http_code', 403,
      'message', format(
        'The email domain "@%s" is not recognised for any MrBadmusAI school. Please sign in with your school email, or ask your teacher.',
        split_part(v_email, '@', 2))
    ));
  END IF;

  -- On-domain, but no pre-existing account. Allowed ONLY if a valid pending
  -- staff invitation exists for this email; otherwise rejected (strict).
  IF EXISTS (
    SELECT 1 FROM public.school_invitations si
    WHERE lower(si.email) = v_email
      AND si.school_id = v_school
      AND si.accepted_at IS NULL
      AND si.deleted_at IS NULL
      AND si.expires_at > now()
  ) THEN
    RETURN '{}'::jsonb;
  END IF;

  -- MRB-293: seeded staff awaiting their first sign-in are admitted the same way.
  IF EXISTS (
    SELECT 1 FROM public.pending_staff ps
    WHERE ps.email = v_email::citext
      AND ps.school_id = v_school
      AND ps.claimed_at IS NULL
      AND ps.deleted_at IS NULL
  ) THEN
    RETURN '{}'::jsonb;
  END IF;

  RETURN jsonb_build_object('error', jsonb_build_object(
    'http_code', 403,
    'message', format(
      'We could not find a MrBadmusAI account for %s. Ask your teacher to add you to a class, then sign in again.',
      v_email)
  ));
END;
$function$;

-- (b) Now nothing references it.
drop function if exists public.consumer_signup_enabled();

-- (c) And now nothing references this. The policies (platform_flags_read,
-- platform_flags_operator_write) and the consumer_signup_enabled row go with
-- the table.
drop table if exists public.platform_flags;
