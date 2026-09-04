-- ROLLBACK for 20260901215044_mrb308_subscriptions_grants_hardening.
-- Apply by hand only. The Supabase CLI never reads this folder.
--
-- ⚠️ Restoring these grants does NOT by itself make subscriptions writable by
-- a client: RLS still has no INSERT/UPDATE/DELETE policy on the table, so
-- writes stay denied. This rollback only returns the table to resting on that
-- single mechanism. There is very little reason to run it.

grant insert, update, delete on public.subscriptions to anon, authenticated;
grant insert, update, delete on public.platform_flags to anon;
