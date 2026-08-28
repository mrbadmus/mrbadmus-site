-- Rollback for 20260828204639_mrb293_hook_admits_pending_staff. Apply MANUALLY.
-- Restores hook_before_user_created to its pre-MRB-293 body, verified byte-identical
-- to what production ran before the change (prosrc md5 c06841d83b3259124324822ca49bcc7b).
--
-- ⚠️ ORDER MATTERS. This file must be applied BEFORE
-- rollbacks/20260828203900_mrb293_pending_staff_claim_mechanism.sql, which drops
-- public.pending_staff. The hook below no longer references that table; the CURRENT
-- hook does. Dropping the table first would leave the live SSO gate raising at
-- execution time — every Microsoft sign-in would fail until this file was applied.
--
-- After this, seeded staff who have not yet claimed can no longer sign in at all
-- (if the hook is registered): they hold no school_invitations row.
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

  RETURN jsonb_build_object('error', jsonb_build_object(
    'http_code', 403,
    'message', format(
      'We could not find a MrBadmusAI account for %s. Ask your teacher to add you to a class, then sign in again.',
      v_email)
  ));
END;
$function$;

GRANT EXECUTE ON FUNCTION public.hook_before_user_created(jsonb) TO supabase_auth_admin;
REVOKE EXECUTE ON FUNCTION public.hook_before_user_created(jsonb) FROM authenticated, anon, public;
