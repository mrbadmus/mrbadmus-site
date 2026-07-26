-- ROLLBACK for 20260726074443_drop_stale_weekly_challenge_constraint.sql
-- Apply manually only. Never run via `supabase db push`.
--
-- Restores the stale UNIQUE (week_start, subject, tier) constraint.
--
-- ⚠️  RESTORING THIS RE-BREAKS THE WEEKLY CHALLENGE. It reinstates the
-- 6-track ceiling on a 12-track system: only one pathway per
-- (week_start, subject, tier) can exist, and students on the losing pathway
-- get "No challenge available. Check back soon!" for the whole week.
-- This file exists for completeness of the migration pair, not because
-- rolling back is ever expected to be the right move.
--
-- This will FAIL if any (week_start, subject, tier) slot currently holds more
-- than one pathway — which is exactly what the forward migration enables.
-- Check first:
--   SELECT week_start, subject, tier, count(DISTINCT pathway)
--   FROM weekly_challenges
--   GROUP BY 1,2,3 HAVING count(DISTINCT pathway) > 1;
-- Any rows returned must be resolved (by Mide, deliberately) before this runs.

ALTER TABLE public.weekly_challenges
  ADD CONSTRAINT weekly_challenges_week_subject_tier_key
  UNIQUE (week_start, subject, tier);
