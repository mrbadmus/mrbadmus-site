-- MRB-317 Night 3 — account deletion is a REQUEST with a 30-day grace, not a delete.
-- Design's Parent Account: "Type DELETE to confirm … Everything is gone on {date}.
-- Sign in before then to undo it." Nothing is hard-deleted by this migration or by
-- the route that writes it; the sweep that executes a request after execute_after
-- is deliberately NOT built tonight (Mide rules the deletion path). Admin sees the row.
create table if not exists public.account_deletion_requests (
  org_id        uuid primary key references public.schools(id) on delete cascade,
  requested_by  uuid references public.profiles(id) on delete set null,
  requested_at  timestamptz not null default now(),
  execute_after timestamptz not null,
  cancelled_at  timestamptz,
  note          text
);
comment on table public.account_deletion_requests is
  'MRB-317: a parent asked for their family account to be deleted. Grace of 30 days (execute_after); cancelled_at set = withdrawn. Service-role writes only; no sweep executes it yet.';

alter table public.account_deletion_requests enable row level security;

-- The seal is the same conjunct every consumer policy carries: the caller's own org.
create policy account_deletion_requests_read_own_org
  on public.account_deletion_requests
  for select to authenticated
  using (org_id = public.auth_user_school_id());

grant select on public.account_deletion_requests to authenticated;
revoke insert, update, delete on public.account_deletion_requests from anon, authenticated;
