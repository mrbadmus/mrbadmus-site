-- =====================================================================
-- Migration:        20260530140000_stage3_sso_domain_hook.sql
-- Stage:            3 — Schools Onboarding (SSO + CSV import + merge)
-- Branch:           schools/stage-3-onboarding
-- Apply target:     TEST project (qeppkiswvclkkwbxmlok) first → prod later
-- Author:           Drafted with Mide, 30 May 2026
-- =====================================================================
--
-- PROVIDER-AGNOSTIC SSO gate (Microsoft Entra ID + Google behind one path).
--
-- Builds two functions:
--   1. school_id_for_email_domain(email)  — resolves a school from the
--      domain of any email, using the schools.email_domains allowlist that
--      already exists from Stage 1 (seeded with 'rainford.org.uk'). Used by
--      the auth hook AND by app/role-resolution code. Provider-neutral: it
--      only ever looks at the email address.
--   2. hook_before_user_created(event)    — the Supabase "Before User
--      Created" auth hook. Gates ONLY OAuth (azure/google) new-user
--      creation. Email/password signups (the existing public consumer flow)
--      and Admin-API-created users (the CSV importer) pass straight through.
--
-- WHY this shape: profiles.id is a hard FK to auth.users.id, so every
-- rostered student is PRE-PROVISIONED as a confirmed auth user by the CSV
-- importer. On first SSO login their verified email matches and Supabase
-- LINKS the OAuth identity to that existing user — no new user is created,
-- so the hook never fires for them. Anyone who DOES reach the OAuth branch
-- of this hook is therefore not pre-assigned → rejected (strict), unless
-- they hold a valid pending staff invitation.
--
-- AFTER APPLYING: this only CREATES the function. It must be REGISTERED as
-- the active hook by Mide in Dashboard > Authentication > Hooks (type:
-- Postgres function → public.hook_before_user_created), or via config.toml:
--   [auth.hook.before_user_created]
--   enabled = true
--   uri = "pg-functions://postgres/public/hook_before_user_created"
-- =====================================================================

BEGIN;

-- 1 ───────────────────────────────────────────────────────────────────
-- Provider-agnostic email-domain → school resolver
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.school_id_for_email_domain(p_email text)
RETURNS uuid
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT s.id
  FROM public.schools s
  WHERE COALESCE(s.active, true) = true
    AND s.deleted_at IS NULL
    AND array_length(s.email_domains, 1) IS NOT NULL
    AND lower(split_part(p_email, '@', 2)) = ANY (
      ARRAY(SELECT lower(trim(d)) FROM unnest(s.email_domains) AS d)
    )
  ORDER BY s.created_at ASC
  LIMIT 1;
$$;

COMMENT ON FUNCTION public.school_id_for_email_domain(text) IS
  'Stage 3 SSO: resolves the school whose email_domains allowlist contains the domain of p_email (case-insensitive). Provider-agnostic; operates only on the email. NULL if no active school matches.';

-- 2 ───────────────────────────────────────────────────────────────────
-- Before User Created auth hook (provider-agnostic SSO gate)
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.hook_before_user_created(event jsonb)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
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
$$;

COMMENT ON FUNCTION public.hook_before_user_created(jsonb) IS
  'Stage 3 SSO Before-User-Created auth hook. Gates ONLY OAuth (azure/google) new-user creation: rejects unknown email domains and non-pre-assigned users (strict); allows pending staff invitations. Email/password + Admin-API (CSV import) creation passes through. REGISTER in Dashboard > Authentication > Hooks or config.toml [auth.hook.before_user_created].';

-- 3 ───────────────────────────────────────────────────────────────────
-- Grants (per Supabase auth-hook contract)
-- ───────────────────────────────────────────────────────────────────────
GRANT USAGE ON SCHEMA public TO supabase_auth_admin;
GRANT EXECUTE ON FUNCTION public.hook_before_user_created(jsonb) TO supabase_auth_admin;
REVOKE EXECUTE ON FUNCTION public.hook_before_user_created(jsonb) FROM authenticated, anon, public;

-- the resolver is called by the hook (as supabase_auth_admin) and by app code.
-- Lock it down: no logged-out (anon/public) access — it should never be probed
-- from outside an authenticated/privileged context.
GRANT  EXECUTE ON FUNCTION public.school_id_for_email_domain(text)
  TO supabase_auth_admin, authenticated, service_role;
REVOKE EXECUTE ON FUNCTION public.school_id_for_email_domain(text)
  FROM anon, public;

COMMIT;

-- =====================================================================
-- END — register the hook in the Dashboard/config before SSO can gate.
-- =====================================================================
