-- =====================================================================
-- Migration:        20260530140100_stage3_audit_writers.sql
-- Stage:            3 — Schools Onboarding
-- Apply target:     TEST project (qeppkiswvclkkwbxmlok) first → prod later
-- Author:           Drafted with Mide, 30 May 2026
-- =====================================================================
--
-- audit_log already exists (Stage 1) and is append-only with NO client
-- INSERT policy — writes must go through SECURITY DEFINER functions that
-- bypass RLS. This migration adds the two writers Stage 3 needs:
--
--   write_audit_event(...)  — privileged writer for service_role (Edge
--      Functions: CSV import) and internal SECURITY DEFINER callers (the
--      account-merge confirm function). NOT granted to authenticated.
--
--   log_my_event(action, payload) — safe self-logging for the frontend.
--      Forces actor_id = auth.uid() and restricts to a whitelist of
--      user-loggable actions (e.g. 'sso_login'). Granted to authenticated.
-- =====================================================================

BEGIN;

-- 1 ───────────────────────────────────────────────────────────────────
-- Privileged audit writer (service_role + internal definer callers)
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.write_audit_event(
  p_action       text,
  p_target_table text,
  p_target_id    uuid  DEFAULT NULL,
  p_payload      jsonb DEFAULT '{}'::jsonb,
  p_actor_id     uuid  DEFAULT NULL,
  p_school_id    uuid  DEFAULT NULL
) RETURNS uuid
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_actor  uuid := COALESCE(p_actor_id, auth.uid());
  v_school uuid := p_school_id;
  v_id     uuid;
BEGIN
  IF v_school IS NULL AND v_actor IS NOT NULL THEN
    SELECT school_id INTO v_school FROM public.profiles WHERE id = v_actor;
  END IF;

  INSERT INTO public.audit_log(actor_id, school_id, action, target_table, target_id, payload)
  VALUES (v_actor, v_school, p_action, p_target_table, p_target_id, COALESCE(p_payload, '{}'::jsonb))
  RETURNING id INTO v_id;

  RETURN v_id;
END;
$$;

COMMENT ON FUNCTION public.write_audit_event(text,text,uuid,jsonb,uuid,uuid) IS
  'Stage 3: privileged append-only writer into audit_log (RLS-locked). For service_role (Edge Functions) and internal SECURITY DEFINER callers (account merge). Derives school_id from the actor profile when not given. NOT granted to authenticated.';

REVOKE EXECUTE ON FUNCTION public.write_audit_event(text,text,uuid,jsonb,uuid,uuid) FROM public, anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.write_audit_event(text,text,uuid,jsonb,uuid,uuid) TO service_role;

-- 2 ───────────────────────────────────────────────────────────────────
-- Safe self-logging for the frontend (forced actor, whitelisted actions)
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.log_my_event(
  p_action  text,
  p_payload jsonb DEFAULT '{}'::jsonb
) RETURNS uuid
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_id uuid;
BEGIN
  IF auth.uid() IS NULL THEN
    RAISE EXCEPTION 'not authenticated';
  END IF;
  IF p_action NOT IN ('sso_login', 'account_claim_requested', 'account_claim_cancelled') THEN
    RAISE EXCEPTION 'action % is not user-loggable', p_action;
  END IF;

  v_id := public.write_audit_event(
    p_action       => p_action,
    p_target_table => 'auth.users',
    p_target_id    => auth.uid(),
    p_payload      => COALESCE(p_payload, '{}'::jsonb),
    p_actor_id     => auth.uid()
  );
  RETURN v_id;
END;
$$;

COMMENT ON FUNCTION public.log_my_event(text,jsonb) IS
  'Stage 3: lets an authenticated user append a small whitelist of self-events (sso_login, account_claim_requested, account_claim_cancelled) to audit_log. actor_id is forced to auth.uid().';

REVOKE EXECUTE ON FUNCTION public.log_my_event(text,jsonb) FROM public, anon;
GRANT  EXECUTE ON FUNCTION public.log_my_event(text,jsonb) TO authenticated;

COMMIT;
