-- MRB-309 Night 2, migration 12: locked_at is stamped in ONE statement.
--
-- The webhook used to read the subscription row, ask org_access_state(),
-- and then write locked_at from what it had read. Two events landing two
-- milliseconds apart (invoice.paid and customer.subscription.created on a
-- reactivation) interleaved: one judged the row before the other's write
-- and stamped a lock onto a subscription that was, by then, healthy. The E6
-- drive caught it: a trialing family carrying a stale locked_at.
--
-- locked_at gates nothing — org_access_state() never reads it — but it is
-- what the account card shows as "access ended", so it must be right.
-- One UPDATE, state computed inside it, no read-then-write. Service role
-- only, like everything that writes subscriptions.

create or replace function public.stamp_org_lock(p_org_id uuid)
returns text
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare v_state text;
begin
  update public.subscriptions s
     set locked_at = case
           when public.org_access_state(s.org_id) = 'locked' then coalesce(s.locked_at, now())
           else null
         end
   where s.org_id = p_org_id
     and s.deleted_at is null;
  select public.org_access_state(p_org_id) into v_state;
  return v_state;
end
$fn$;

revoke all on function public.stamp_org_lock(uuid) from public, anon, authenticated;

comment on function public.stamp_org_lock(uuid) is
  'MRB-309. Sets subscriptions.locked_at atomically from org_access_state(): stamped once when locked, cleared whenever not. Returns the state.';