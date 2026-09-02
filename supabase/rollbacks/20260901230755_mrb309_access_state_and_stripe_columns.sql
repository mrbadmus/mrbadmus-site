-- ROLLBACK for 20260901230755_mrb309_access_state_and_stripe_columns.
-- Apply by hand only. The Supabase CLI never reads this folder.
--
-- ⚠️ What reverting COSTS you. org_access_state() goes away and every
-- Night 2 module that calls it (backend consumer/access.js, the
-- family_messages_send policy, the 0011 matrix) breaks at once — so this
-- is only ever rolled back together with migrations 2–9. org_is_entitled()
-- returns to the Night 1 body, which admits a 'trialing' row with no
-- trial_end forever (the free-forever hole Night 2 closed).
-- create_family_for_parent() returns to inserting a 7-day local trial.
-- Rows carrying status 'none' violate the restored CHECK: they are moved to
-- 'trialing' with a null trial_end first, which Night 1's helper reads as
-- entitled — accept that or delete them.

drop function if exists public.profile_consumer_org(uuid);
drop function if exists public.guardian_of_child(uuid, uuid);

update public.subscriptions set status = 'trialing' where status = 'none';
alter table public.subscriptions drop constraint if exists subscriptions_status_check;
alter table public.subscriptions add constraint subscriptions_status_check check (status in
  ('trialing', 'active', 'past_due', 'canceled', 'locked', 'comped'));
alter table public.subscriptions drop constraint if exists subscriptions_billing_interval_check;
alter table public.subscriptions
  drop column if exists cancel_at_period_end,
  drop column if exists billing_interval,
  drop column if exists stripe_price_id,
  drop column if exists retry_at,
  drop column if exists last_payment_failed_at,
  drop column if exists canceled_at,
  drop column if exists locked_at;

-- Night 1 bodies: re-apply from
--   supabase/migrations/20260901214241_mrb308_subscriptions_and_entitlement.sql (org_is_entitled)
--   supabase/migrations/20260901214441_mrb308_create_family_for_parent.sql   (create_family_for_parent)
-- then:
drop function if exists public.org_access_state(uuid);
