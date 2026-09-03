-- MRB-308 Night 1, migration 3 of 6: subscriptions + the entitlement helper.
--
-- One row per org. Stripe fills this table on Night 2 (MRB-309); tonight it
-- is written only by hand from Admin (comp / extend trial / seat cap) and
-- read by org_is_entitled().

create table if not exists public.subscriptions (
  org_id                 uuid primary key references public.schools(id),
  stripe_customer_id     text unique,
  stripe_subscription_id text unique,
  status                 text not null default 'trialing',
  trial_end              timestamptz,
  current_period_end     timestamptz,
  quantity               integer not null default 1,
  seat_cap               integer,
  comped_until           timestamptz,
  created_at             timestamptz not null default now(),
  updated_at             timestamptz not null default now(),
  deleted_at             timestamptz,

  constraint subscriptions_status_check check (status in
    ('trialing', 'active', 'past_due', 'canceled', 'locked', 'comped')),
  constraint subscriptions_quantity_check check (quantity >= 0),
  constraint subscriptions_seat_cap_check check (seat_cap is null or seat_cap >= 0)
);

comment on table public.subscriptions is
  'MRB-308. One row per org, keyed on schools.id. Written by the service role '
  '(Stripe webhook, MRB-309) and by platform operators from Admin. Never by '
  'a parent: there are deliberately no INSERT/UPDATE/DELETE policies here, so '
  'RLS denies every write from an ordinary session.';

create index if not exists idx_subscriptions_status
  on public.subscriptions (status) where deleted_at is null;

alter table public.subscriptions enable row level security;

-- READ: the parent of the family (they hold school_admin scoped to it), or
-- organisation staff with the same scope. Paired with the org_id conjunct,
-- exactly as every other scope grant in the estate is.
drop policy if exists subscriptions_org_admin_read on public.subscriptions;
create policy subscriptions_org_admin_read on public.subscriptions
  for select using (
    org_id = public.auth_user_school_id()
    and public.auth_user_has_scope('school_admin')
  );

-- READ: platform operators (Mide) see every org's billing state, for Admin.
drop policy if exists subscriptions_operator_read on public.subscriptions;
create policy subscriptions_operator_read on public.subscriptions
  for select using (public.auth_user_operator_active());

-- ⚠️ NO write policies, deliberately. RLS default-denies, so INSERT/UPDATE/
-- DELETE are impossible for anon and authenticated alike. The service role
-- bypasses RLS and is the only writer. A parent must never be able to grant
-- themselves entitlement by writing their own row.

create or replace function public.subscriptions_touch_updated_at()
returns trigger language plpgsql as $fn$
begin
  new.updated_at := now();
  return new;
end $fn$;

drop trigger if exists trg_subscriptions_touch on public.subscriptions;
create trigger trg_subscriptions_touch
  before update on public.subscriptions
  for each row execute function public.subscriptions_touch_updated_at();

-- ---------------------------------------------------------------------
-- The entitlement helper.
-- ---------------------------------------------------------------------
-- STABLE + SECURITY DEFINER so it can read subscriptions from inside a
-- policy or an app gate without the caller needing read access to the row.
create or replace function public.org_is_entitled(p_org_id uuid)
returns boolean
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select case
    -- No org named: not entitled. Never fail open.
    when p_org_id is null then false

    -- A real school is entitled unconditionally. Rainford does not pay
    -- through Stripe and must never be gated by a subscriptions row it
    -- does not have. This is the clause that keeps the B2B estate whole.
    when (select s.kind from public.schools s where s.id = p_org_id) = 'school'
      then true

    when (select s.kind from public.schools s where s.id = p_org_id) = 'family'
      then exists (
        select 1 from public.subscriptions sub
        where sub.org_id = p_org_id
          and sub.deleted_at is null
          and (
                sub.status in ('trialing', 'active')
             or (sub.status = 'comped'
                 and sub.comped_until is not null
                 and sub.comped_until > now())
             -- Dunning grace: a failed card does not lock a child out of
             -- their work the same day. Seven days past the period end.
             or (sub.status = 'past_due'
                 and sub.current_period_end is not null
                 and sub.current_period_end + interval '7 days' > now())
          )
      )

    when (select s.kind from public.schools s where s.id = p_org_id) = 'organisation'
      then exists (
        select 1 from public.subscriptions sub
        where sub.org_id = p_org_id
          and sub.deleted_at is null
          and sub.seat_cap is not null
          and sub.current_period_end is not null
          and sub.current_period_end > now()
      )

    -- Unknown org, or an org kind we have not taught this function about.
    else false
  end;
$fn$;

comment on function public.org_is_entitled(uuid) is
  'MRB-308. school => always true (Rainford is not gated on Stripe). '
  'family => trialing/active, or comped within comped_until, or past_due '
  'within a 7-day grace of current_period_end. organisation => a seat cap is '
  'set and current_period_end is in the future. Anything else, including a '
  'missing row, is FALSE — this fails closed by design.';

grant execute on function public.org_is_entitled(uuid) to authenticated, anon;
