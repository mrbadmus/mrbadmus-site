-- =====================================================================
-- Migration:        20260629195630_add_profiles_external_student_id.sql
-- Stage:            3 — Schools Onboarding (CSV import: store external ID)
-- Apply target:     PROD project (urklkrwevjtlfbwnipjn)
-- Author:           Drafted with Mide, 29 Jun 2026
-- =====================================================================
--
-- Rainford's Synergy MIS exports a per-student "Admission Number" — a
-- stable internal identifier. We STORE it on the profile so future
-- Synergy data merges have a durable anchor. This migration is
-- STORE-ONLY: identity reconciliation in the roster-import Edge Function
-- stays keyed on EMAIL. The external id is written, never used to match.
--
-- Column:  profiles.external_student_id text, nullable. NULL for every
--          existing / non-imported user — no backfill, constraint-safe.
--
-- Uniqueness: a PARTIAL unique index scoped to (school_id,
--          external_student_id). The same Synergy id cannot duplicate
--          WITHIN a school, but:
--            - NULLs are allowed for all legacy / SSO-only users;
--            - the same id value may legitimately recur ACROSS schools
--              (Synergy ids are unique per-school, not globally).
--
-- Interplay: touches none of the 5 existing profiles CHECK constraints
--          (role / key_stage / tier-only-ks4 / hod-needs-dept /
--          staff-needs-school). The Edge Function writes via service_role
--          (bypasses RLS), so no RLS policy change is required.
-- =====================================================================

BEGIN;

ALTER TABLE public.profiles
  ADD COLUMN IF NOT EXISTS external_student_id text;

COMMENT ON COLUMN public.profiles.external_student_id IS
  'Stage 3 CSV import: external MIS student identifier (e.g. Synergy Admission Number). Store-only anchor for future data merges; never used for identity matching (reconciliation stays on email). Unique per school via uq_profiles_external_student_id.';

CREATE UNIQUE INDEX IF NOT EXISTS uq_profiles_external_student_id
  ON public.profiles (school_id, external_student_id)
  WHERE external_student_id IS NOT NULL;

COMMIT;
