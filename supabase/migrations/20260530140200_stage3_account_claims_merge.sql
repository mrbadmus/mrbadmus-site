-- =====================================================================
-- Migration:        20260530140200_stage3_account_claims_merge.sql
-- Stage:            3 — Schools Onboarding (account reconciliation / merge)
-- Apply target:     TEST project (qeppkiswvclkkwbxmlok) first → prod later
-- Author:           Drafted with Mide, 30 May 2026
-- Depends on:       20260530140100_stage3_audit_writers.sql (write_audit_event)
-- =====================================================================
--
-- BRANCH B (chosen from the Step-1 prod audit: 57% of existing accounts are
-- on personal email domains). Self-service "claim a previous account":
--
--   1. Student signs in via school SSO (canonical account).
--   2. On the student settings page they enter their OLD personal email.
--   3. The account-claim Edge Function emails a single-use, time-limited
--      verification link to that personal address (proof of control).
--   4. On confirmation, confirm_account_claim_and_reparent() idempotently
--      reparents the old profile's data onto the canonical account, soft-
--      deletes the old profile, and writes an audit_log entry.
--
-- This migration provides the table + the three SECURITY DEFINER functions
-- the Edge Function calls. The token itself is generated/emailed by the Edge
-- Function; only its SHA-256 hash is ever stored here.
--
-- IDEMPOTENT BY DESIGN: reparent_student() can be re-run with the same
-- (old, canonical) pair and will move nothing the second time. XP counters
-- are summed once then zeroed on the loser, so re-runs never double-count.
-- =====================================================================

BEGIN;

-- 1 ───────────────────────────────────────────────────────────────────
-- account_claims
-- ───────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS public.account_claims (
  id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  claimant_id    uuid NOT NULL REFERENCES public.profiles(id),   -- canonical (new SSO) account
  claimant_email text NOT NULL,                                  -- school email (informational)
  old_email      text NOT NULL,                                  -- personal email being claimed
  old_profile_id uuid REFERENCES public.profiles(id),            -- resolved loser profile
  token_hash     text NOT NULL,                                  -- SHA-256 of single-use token
  status         text NOT NULL DEFAULT 'pending'
                 CHECK (status IN ('pending','verified','consumed','expired','cancelled')),
  expires_at     timestamptz NOT NULL,
  verified_at    timestamptz,
  consumed_at    timestamptz,
  created_at     timestamptz DEFAULT now(),
  updated_at     timestamptz DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS account_claims_token_hash_key
  ON public.account_claims(token_hash);
CREATE INDEX IF NOT EXISTS idx_account_claims_claimant
  ON public.account_claims(claimant_id);
CREATE INDEX IF NOT EXISTS idx_account_claims_old_profile
  ON public.account_claims(old_profile_id);
-- at most one PENDING claim per (claimant, old_email)
CREATE UNIQUE INDEX IF NOT EXISTS account_claims_pending_unique
  ON public.account_claims(claimant_id, lower(old_email))
  WHERE status = 'pending';

ALTER TABLE public.account_claims ENABLE ROW LEVEL SECURITY;

-- claimant may read their own claims (to show status); ALL writes go through
-- the SECURITY DEFINER functions / service_role. No client INSERT/UPDATE.
CREATE POLICY account_claims_self_read ON public.account_claims
  FOR SELECT USING (claimant_id = auth.uid());

-- 2 ───────────────────────────────────────────────────────────────────
-- reparent_student(old, canonical) — idempotent data move
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.reparent_student(p_old uuid, p_canonical uuid)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_cm_superseded int := 0;
  v_cm_moved      int := 0;
  v_cm_relinked   int := 0;
  v_subs          int := 0;
  v_shout         int := 0;
  v_ws_present    boolean := false;
  v_ws_col        text;
  v_ws_moved      int := 0;
BEGIN
  IF p_old IS NULL OR p_canonical IS NULL OR p_old = p_canonical THEN
    RAISE EXCEPTION 'reparent_student: invalid args (old=%, canonical=%)', p_old, p_canonical;
  END IF;

  -- (1) class_members: close colliding ACTIVE memberships on the OLD account
  -- (where the canonical account is already an active member of that class),
  -- so the class_members_active_unique partial index is never violated.
  UPDATE public.class_members om
     SET left_at = now(), updated_at = now()
   WHERE om.student_id = p_old
     AND om.left_at IS NULL AND om.deleted_at IS NULL
     AND EXISTS (
       SELECT 1 FROM public.class_members cm
        WHERE cm.class_id = om.class_id
          AND cm.student_id = p_canonical
          AND cm.left_at IS NULL AND cm.deleted_at IS NULL
     );
  GET DIAGNOSTICS v_cm_superseded = ROW_COUNT;

  -- move remaining ACTIVE memberships (no active collision possible now)
  UPDATE public.class_members
     SET student_id = p_canonical, updated_at = now()
   WHERE student_id = p_old AND left_at IS NULL AND deleted_at IS NULL;
  GET DIAGNOSTICS v_cm_moved = ROW_COUNT;

  -- relink any remaining historic/closed memberships (not under the active
  -- partial unique index, so always safe) so history follows the student
  UPDATE public.class_members
     SET student_id = p_canonical, updated_at = now()
   WHERE student_id = p_old;
  GET DIAGNOSTICS v_cm_relinked = ROW_COUNT;

  -- (2) assignment_submissions (no unique on (assignment, student))
  UPDATE public.assignment_submissions
     SET student_id = p_canonical, updated_at = now()
   WHERE student_id = p_old;
  GET DIAGNOSTICS v_subs = ROW_COUNT;

  -- (3) class_shoutouts received. author_id is always staff, so leave it.
  UPDATE public.class_shoutouts
     SET recipient_id = p_canonical, updated_at = now()
   WHERE recipient_id = p_old;
  GET DIAGNOSTICS v_shout = ROW_COUNT;

  -- (4) profile-field carryover: fill canonical NULLs from the loser; merge
  -- counters. key_stage is copied alongside tier/pathway to satisfy the
  -- profiles_tier_only_ks4_check constraint.
  UPDATE public.profiles c
     SET key_stage       = COALESCE(c.key_stage, o.key_stage),
         science_pathway = COALESCE(c.science_pathway, o.science_pathway),
         tier            = COALESCE(c.tier, o.tier),
         target_grade    = COALESCE(c.target_grade, o.target_grade),
         year_group      = COALESCE(c.year_group, o.year_group),
         strengths       = COALESCE(c.strengths, o.strengths),
         weaknesses      = COALESCE(c.weaknesses, o.weaknesses),
         school_name     = COALESCE(c.school_name, o.school_name),
         total_xp        = COALESCE(c.total_xp, 0) + COALESCE(o.total_xp, 0),
         streak_days     = GREATEST(COALESCE(c.streak_days, 0), COALESCE(o.streak_days, 0)),
         updated_at      = now()
    FROM public.profiles o
   WHERE c.id = p_canonical AND o.id = p_old;

  -- zero the loser's counters so a re-run never double-counts XP (idempotency)
  UPDATE public.profiles
     SET total_xp = 0, streak_days = 0, updated_at = now()
   WHERE id = p_old;

  -- (5) PROD-only consumer table weekly_scores (absent in TEST). Guarded +
  -- dynamic so the same function is correct on test and prod. Detects the
  -- owner column name automatically.
  IF to_regclass('public.weekly_scores') IS NOT NULL THEN
    v_ws_present := true;
    SELECT column_name INTO v_ws_col
      FROM information_schema.columns
     WHERE table_schema = 'public' AND table_name = 'weekly_scores'
       AND column_name IN ('student_id','user_id','profile_id')
     ORDER BY CASE column_name WHEN 'student_id' THEN 1 WHEN 'profile_id' THEN 2 ELSE 3 END
     LIMIT 1;
    IF v_ws_col IS NOT NULL THEN
      EXECUTE format('UPDATE public.weekly_scores SET %I = $1 WHERE %I = $2', v_ws_col, v_ws_col)
        USING p_canonical, p_old;
      GET DIAGNOSTICS v_ws_moved = ROW_COUNT;
    END IF;
  END IF;

  RETURN jsonb_build_object(
    'old', p_old,
    'canonical', p_canonical,
    'class_members_superseded', v_cm_superseded,
    'class_members_moved', v_cm_moved,
    'class_members_relinked', v_cm_relinked,
    'submissions_moved', v_subs,
    'shoutouts_moved', v_shout,
    'weekly_scores_present', v_ws_present,
    'weekly_scores_column', v_ws_col,
    'weekly_scores_moved', v_ws_moved
  );
END;
$$;

COMMENT ON FUNCTION public.reparent_student(uuid,uuid) IS
  'Stage 3: idempotently moves a student''s data (class_members [collision-aware], assignment_submissions, class_shoutouts received, profile-field/XP carryover, and prod weekly_scores when present) from old profile to canonical. Re-running is a no-op. Does NOT touch audit_log.actor_id (history is preserved).';

REVOKE EXECUTE ON FUNCTION public.reparent_student(uuid,uuid) FROM public, anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.reparent_student(uuid,uuid) TO service_role;

-- 3 ───────────────────────────────────────────────────────────────────
-- create_account_claim(...) — called by the Edge Function (service_role)
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.create_account_claim(
  p_claimant_id uuid,
  p_old_email   text,
  p_token_hash  text,
  p_ttl_minutes int DEFAULT 30
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_old            uuid;
  v_claimant_email text;
  v_claim_id       uuid;
BEGIN
  IF p_claimant_id IS NULL THEN
    RAISE EXCEPTION 'claimant required';
  END IF;

  -- resolve the loser profile by personal email (email lives in auth.users)
  SELECT p.id INTO v_old
    FROM public.profiles p
    JOIN auth.users u ON u.id = p.id
   WHERE lower(u.email) = lower(trim(p_old_email))
     AND p.deleted_at IS NULL
   LIMIT 1;

  SELECT u.email INTO v_claimant_email FROM auth.users u WHERE u.id = p_claimant_id;

  -- anti-enumeration: behave identically whether or not a match exists
  IF v_old IS NULL OR v_old = p_claimant_id THEN
    RETURN jsonb_build_object('matched', false);
  END IF;

  INSERT INTO public.account_claims(
    claimant_id, claimant_email, old_email, old_profile_id, token_hash, status, expires_at
  )
  VALUES (
    p_claimant_id, COALESCE(v_claimant_email, ''), lower(trim(p_old_email)),
    v_old, p_token_hash, 'pending', now() + make_interval(mins => p_ttl_minutes)
  )
  ON CONFLICT (claimant_id, lower(old_email)) WHERE (status = 'pending')
  DO UPDATE SET token_hash = EXCLUDED.token_hash,
                expires_at = EXCLUDED.expires_at,
                old_profile_id = EXCLUDED.old_profile_id,
                updated_at = now()
  RETURNING id INTO v_claim_id;

  PERFORM public.write_audit_event(
    p_action       => 'account_claim_requested',
    p_target_table => 'account_claims',
    p_target_id    => v_claim_id,
    p_payload      => jsonb_build_object('old_email', lower(trim(p_old_email)), 'old_profile_id', v_old),
    p_actor_id     => p_claimant_id
  );

  RETURN jsonb_build_object('matched', true, 'claim_id', v_claim_id);
END;
$$;

COMMENT ON FUNCTION public.create_account_claim(uuid,text,text,int) IS
  'Stage 3: resolves the loser profile by old_email, stores a pending single-use claim (token hash only) for the canonical claimant, logs account_claim_requested. Anti-enumeration: returns matched=false (no row, no email) when no eligible old account exists. service_role only.';

REVOKE EXECUTE ON FUNCTION public.create_account_claim(uuid,text,text,int) FROM public, anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.create_account_claim(uuid,text,text,int) TO service_role;

-- 4 ───────────────────────────────────────────────────────────────────
-- confirm_account_claim_and_reparent(token_hash) — called after the student
-- clicks the email link. Validates, reparents, soft-deletes loser, audits.
-- ───────────────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.confirm_account_claim_and_reparent(p_token_hash text)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  v_claim  public.account_claims%ROWTYPE;
  v_counts jsonb;
BEGIN
  SELECT * INTO v_claim FROM public.account_claims WHERE token_hash = p_token_hash;

  IF NOT FOUND THEN
    RETURN jsonb_build_object('ok', false, 'reason', 'invalid_token');
  END IF;

  -- idempotent: a consumed claim returns success without re-running anything
  IF v_claim.status = 'consumed' THEN
    RETURN jsonb_build_object('ok', true, 'already_consumed', true, 'claim_id', v_claim.id);
  END IF;

  IF v_claim.status = 'cancelled' THEN
    RETURN jsonb_build_object('ok', false, 'reason', 'cancelled');
  END IF;

  IF v_claim.expires_at <= now() THEN
    UPDATE public.account_claims SET status = 'expired', updated_at = now()
     WHERE id = v_claim.id AND status = 'pending';
    RETURN jsonb_build_object('ok', false, 'reason', 'expired');
  END IF;

  IF v_claim.old_profile_id IS NULL THEN
    RETURN jsonb_build_object('ok', false, 'reason', 'no_old_profile');
  END IF;

  IF v_claim.old_profile_id = v_claim.claimant_id THEN
    UPDATE public.account_claims SET status = 'cancelled', updated_at = now() WHERE id = v_claim.id;
    RETURN jsonb_build_object('ok', false, 'reason', 'self_claim');
  END IF;

  -- reparent (idempotent), then soft-delete loser, then consume the claim
  v_counts := public.reparent_student(v_claim.old_profile_id, v_claim.claimant_id);

  UPDATE public.profiles SET deleted_at = now(), updated_at = now()
   WHERE id = v_claim.old_profile_id AND deleted_at IS NULL;

  UPDATE public.account_claims
     SET status = 'consumed',
         verified_at = COALESCE(verified_at, now()),
         consumed_at = now(),
         updated_at = now()
   WHERE id = v_claim.id;

  PERFORM public.write_audit_event(
    p_action       => 'account_merge_confirmed',
    p_target_table => 'profiles',
    p_target_id    => v_claim.old_profile_id,
    p_payload      => jsonb_build_object(
                        'canonical_id', v_claim.claimant_id,
                        'old_email', v_claim.old_email,
                        'counts', v_counts),
    p_actor_id     => v_claim.claimant_id
  );

  RETURN jsonb_build_object('ok', true, 'claim_id', v_claim.id, 'counts', v_counts);
END;
$$;

COMMENT ON FUNCTION public.confirm_account_claim_and_reparent(text) IS
  'Stage 3: validates a single-use claim by token hash (pending + not expired), reparents the loser onto the canonical account, soft-deletes the loser, consumes the claim, and writes account_merge_confirmed to audit_log. Idempotent: a consumed token returns success without re-running. service_role only.';

REVOKE EXECUTE ON FUNCTION public.confirm_account_claim_and_reparent(text) FROM public, anon, authenticated;
GRANT  EXECUTE ON FUNCTION public.confirm_account_claim_and_reparent(text) TO service_role;

COMMIT;
