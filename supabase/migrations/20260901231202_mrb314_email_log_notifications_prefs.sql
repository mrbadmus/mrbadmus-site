-- MRB-314 Night 2, migration 7 of 9: every email logged, in-app flags, and
-- the parent's notification preferences.
--
-- email_log — one row per send attempt: type, org, recipient, the Resend id,
--   and a dedupe key so a cron that fires twice cannot send twice. Never a
--   child: the backend refuses any recipient whose profile is a student or
--   whose address is on the internal children domain, and logs 'skipped'.
-- consumer_notifications — the in-app flag ("Mr Badmus has marked your
--   answer", "new messages") for a parent or a child.
-- parent_prefs — digest and message/marking emails can be switched off;
--   billing emails cannot (they are the DMCC reminder).

create table if not exists public.email_log (
  id               uuid primary key default gen_random_uuid(),
  type             text not null,
  org_id           uuid references public.schools(id),
  recipient_id     uuid references public.profiles(id),
  recipient_email  text not null,
  subject          text,
  resend_id        text,
  status           text not null,
  error            text,
  dedupe_key       text,
  created_at       timestamptz not null default now(),
  constraint email_log_status_check check (status in ('sent', 'dry_run', 'failed', 'skipped'))
);

create unique index if not exists uq_email_log_dedupe on public.email_log (dedupe_key) where dedupe_key is not null;
create index if not exists idx_email_log_org on public.email_log (org_id, created_at desc);
create index if not exists idx_email_log_type on public.email_log (type, created_at desc);

create table if not exists public.consumer_notifications (
  id             uuid primary key default gen_random_uuid(),
  org_id         uuid not null references public.schools(id),
  recipient_id   uuid not null references public.profiles(id),
  kind           text not null,
  title          text not null,
  body           text,
  ref            jsonb not null default '{}'::jsonb,
  created_at     timestamptz not null default now(),
  read_at        timestamptz
);

create index if not exists idx_consumer_notifications_unread on public.consumer_notifications (recipient_id, created_at desc) where read_at is null;

create table if not exists public.parent_prefs (
  profile_id       uuid primary key references public.profiles(id),
  digest           boolean not null default true,
  messages_email   boolean not null default true,
  marking_email    boolean not null default true,
  updated_at       timestamptz not null default now()
);

alter table public.email_log              enable row level security;
alter table public.consumer_notifications enable row level security;
alter table public.parent_prefs           enable row level security;

drop policy if exists email_log_operator_read on public.email_log;
create policy email_log_operator_read on public.email_log
  for select using (public.auth_user_operator_active());

drop policy if exists consumer_notifications_own_read on public.consumer_notifications;
create policy consumer_notifications_own_read on public.consumer_notifications
  for select using (recipient_id = auth.uid() or public.auth_user_operator_active());

drop policy if exists parent_prefs_own_read on public.parent_prefs;
create policy parent_prefs_own_read on public.parent_prefs
  for select using (profile_id = auth.uid() or public.auth_user_operator_active());

revoke insert, update, delete on public.email_log              from anon, authenticated;
revoke insert, update, delete on public.consumer_notifications from anon, authenticated;
revoke insert, update, delete on public.parent_prefs           from anon, authenticated;

-- A recipient marks their own notifications read.
create or replace function public.consumer_notifications_mark_read(p_ids uuid[] default null)
returns integer
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare n integer;
begin
  update public.consumer_notifications
     set read_at = now()
   where recipient_id = auth.uid()
     and read_at is null
     and (p_ids is null or id = any(p_ids));
  get diagnostics n = row_count;
  return n;
end
$fn$;

revoke all on function public.consumer_notifications_mark_read(uuid[]) from public;
grant execute on function public.consumer_notifications_mark_read(uuid[]) to authenticated;

comment on table public.email_log is
  'MRB-314. Every outgoing email: type, org, recipient, Resend id, outcome. dedupe_key makes a repeated cron a no-op. Never a child.';
comment on table public.consumer_notifications is
  'MRB-314. In-app flags for parents and children. Read by the recipient; written by the service role.';
comment on table public.parent_prefs is
  'MRB-314. Digest and non-billing email switches. Billing emails are not optional.';