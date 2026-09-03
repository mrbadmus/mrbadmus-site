-- MRB-309 Night 2, migration 2 of 9: the Stripe event ledger.
--
-- Stripe delivers every event at least once and retries for days. The
-- webhook is idempotent on the event id: it INSERTs here first, and a
-- conflict means "already handled — answer 200 and do nothing". The row is
-- also the audit trail Mide reads when a family says their card was charged
-- and the site still shows them locked.
--
-- Service role only. A parent must never be able to write an event, and
-- there is nothing in here a parent needs to read.

create table if not exists public.stripe_events (
  id             text primary key,                 -- evt_...
  type           text not null,                    -- customer.subscription.updated, ...
  org_id         uuid references public.schools(id),
  stripe_created timestamptz,
  received_at    timestamptz not null default now(),
  processed_at   timestamptz,
  outcome        text,                             -- applied | ignored | error
  error          text,
  payload        jsonb,
  constraint stripe_events_outcome_check check (outcome is null or outcome in ('applied', 'ignored', 'error'))
);

create index if not exists idx_stripe_events_org on public.stripe_events (org_id, received_at desc);
create index if not exists idx_stripe_events_type on public.stripe_events (type, received_at desc);

alter table public.stripe_events enable row level security;

-- Operators read the ledger from Admin. Nobody else reads it, nobody writes
-- it from a session: no other policies, and the grants say so twice.
drop policy if exists stripe_events_operator_read on public.stripe_events;
create policy stripe_events_operator_read on public.stripe_events
  for select using (public.auth_user_operator_active());

revoke insert, update, delete on public.stripe_events from anon, authenticated;

comment on table public.stripe_events is
  'MRB-309. One row per Stripe webhook event, keyed on the event id. The webhook inserts first and treats a conflict as already-processed. Service role only.';