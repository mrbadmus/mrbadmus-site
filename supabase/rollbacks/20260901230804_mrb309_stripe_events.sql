-- ROLLBACK for 20260901230804_mrb309_stripe_events. Apply by hand only.
-- ⚠️ Drops the webhook's idempotency ledger. With it gone, a replayed Stripe
-- event is applied twice; the audit trail of every billing transition is
-- lost with the table.
drop table if exists public.stripe_events;
