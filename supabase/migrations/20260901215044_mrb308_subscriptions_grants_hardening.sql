-- MRB-308 Night 1, migration 7: harden subscriptions at the GRANT layer too.
--
-- Found while writing the policy matrix. `subscriptions` had RLS enabled with
-- no INSERT/UPDATE/DELETE policies, so writes were already denied — but the
-- table-level GRANTs still handed anon and authenticated INSERT, UPDATE and
-- DELETE. That left the billing table resting on exactly one mechanism.
--
-- `profiles` is already hardened this way (UPDATE is revoked from anon and
-- authenticated there, which is why profile writes go through SECURITY
-- DEFINER functions), so this follows an existing house pattern rather than
-- inventing one.
--
-- The ruling is "only the service role writes". After this it is true at two
-- independent layers: a policy gap and a grant would BOTH have to regress
-- before a parent could touch their own entitlement.

revoke insert, update, delete on public.subscriptions from anon, authenticated;

-- platform_flags: same reasoning. The operator-write policy is the intended
-- gate, but the flag that decides whether consumer signup exists at all
-- should not be one policy edit away from being writable by any session.
revoke insert, update, delete on public.platform_flags from anon;

-- service_role keeps everything (it bypasses RLS anyway); this is belt and
-- braces for the client-facing roles only.
grant select on public.subscriptions to anon, authenticated;
grant select on public.platform_flags to anon, authenticated;
