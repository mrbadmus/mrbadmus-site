-- ROLLBACK for MRB-308 Night 1, migration 3 of 6
-- (20260901214241_mrb308_subscriptions_and_entitlement). Apply MANUALLY only.
--
-- ⚠️ Apply the rollback for migration 5 BEFORE this one.
-- create_family_for_parent() inserts into public.subscriptions, and
-- attach_child_to_family() / parent_remove_child() (migration 6) both UPDATE
-- its quantity. Dropping the table underneath any of them leaves a function
-- that only fails when a real parent uses it.
--
-- ⚠️ THIS DESTROYS BILLING STATE. Once Stripe is writing here (Night 2,
-- MRB-309) the table holds stripe_customer_id / stripe_subscription_id, which
-- are the only local link back to the Stripe objects. Take a copy first:
--   create table subscriptions_backup as select * from public.subscriptions;
--
-- The policies (subscriptions_org_admin_read, subscriptions_operator_read)
-- and the index go with the table; they need no separate statement. So do
-- the GRANTs that migration 7 (20260901215044) hardened, which is why its
-- own rollback becomes a no-op once this file has run.

drop function if exists public.org_is_entitled(uuid);

drop trigger if exists trg_subscriptions_touch on public.subscriptions;

drop function if exists public.subscriptions_touch_updated_at();

drop table if exists public.subscriptions;
