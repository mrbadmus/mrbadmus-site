-- ROLLBACK for 20260901231304_mrb315_ai_usage_and_limits. Apply by hand only.
-- ⚠️ Drops the usage ledger: the caps have nothing to count, and the
-- backend's aiCap middleware fails CLOSED (429) when its RPC is missing.
-- Roll the backend back with it.
drop function if exists public.ai_usage_counts(uuid);
drop table if exists public.org_limits;
drop table if exists public.ai_usage_events;
