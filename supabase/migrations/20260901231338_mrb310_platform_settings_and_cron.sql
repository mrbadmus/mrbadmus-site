-- MRB-310 Night 2, migration 9 of 9: platform settings, and the clock.
--
-- platform_settings — small operator-editable values: the consumer cap
--   defaults, and where the cron should call. Service role only.
--
-- The scheduler. compose_assignment() and the work generator are JavaScript
-- in the backend, so the database cannot generate a week itself; what it can
-- do is be the CLOCK. pg_cron fires, consumer_cron_call() POSTs to the
-- backend with a shared secret through pg_net, and the backend does the work.
--
-- ⚠️ BST/GMT is handled the way this estate handles it — by hand. pg_cron
-- runs in UTC. Sunday 18:00 London is 17:00 UTC in summer and 18:00 UTC in
-- winter, so BOTH are scheduled and the backend keeps only the one where it
-- is 18:xx in Europe/London. Every cron endpoint is idempotent (the weekly
-- one on work_generation_runs, the emails on email_log.dedupe_key), so the
-- extra firing costs one refused request. The same pattern serves 09:00
-- London for the daily tick.
--
-- Until cron_target_url is set, consumer_cron_call() is a no-op — the job
-- exists, fires, and does nothing. That is the state on TEST tonight and on
-- production until Mide sets the URL and secret from the SQL editor.

create table if not exists public.platform_settings (
  key         text primary key,
  value       jsonb not null,
  note        text,
  updated_at  timestamptz not null default now(),
  updated_by  uuid references public.profiles(id)
);

alter table public.platform_settings enable row level security;

drop policy if exists platform_settings_operator_read on public.platform_settings;
create policy platform_settings_operator_read on public.platform_settings
  for select using (public.auth_user_operator_active());

revoke insert, update, delete on public.platform_settings from anon, authenticated;

insert into public.platform_settings (key, value, note) values
  ('consumer_limits',
   '{"tutor_turns_per_day": 60, "ai_marks_per_month": 40, "mb_marks_per_month": 2, "explain_per_day": 60}'::jsonb,
   'MRB-315 defaults. Per-org overrides in org_limits.'),
  ('cron_target_url', 'null'::jsonb,
   'Base URL of the backend, e.g. "https://mrbadmus-backend.onrender.com". NULL = the cron does nothing.'),
  ('cron_secret', 'null'::jsonb,
   'Shared secret the backend expects in x-cron-secret. Must equal CONSUMER_CRON_SECRET on Render.')
on conflict (key) do nothing;

-- ---------------------------------------------------------------------
-- The clock.
-- ---------------------------------------------------------------------
create extension if not exists pg_cron with schema pg_catalog;
create extension if not exists pg_net with schema extensions;
grant usage on schema cron to postgres;

create or replace function public.consumer_cron_call(p_path text)
returns bigint
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare
  v_url    text;
  v_secret text;
  v_id     bigint;
begin
  select value #>> '{}' into v_url    from public.platform_settings where key = 'cron_target_url';
  select value #>> '{}' into v_secret from public.platform_settings where key = 'cron_secret';
  if v_url is null or v_url = '' or v_url = 'null' or v_secret is null or v_secret = 'null' then
    return null;   -- not configured: deliberately a no-op
  end if;
  select net.http_post(
    url     := rtrim(v_url, '/') || p_path,
    headers := jsonb_build_object('content-type', 'application/json', 'x-cron-secret', v_secret),
    body    := jsonb_build_object('fired_at', now(), 'path', p_path),
    timeout_milliseconds := 120000
  ) into v_id;
  return v_id;
end
$fn$;

revoke all on function public.consumer_cron_call(text) from public, anon, authenticated;

-- Sunday 18:00 Europe/London, both clock settings.
select cron.schedule('consumer_weekly_utc17', '0 17 * * 0', $$select public.consumer_cron_call('/api/consumer/cron/weekly')$$);
select cron.schedule('consumer_weekly_utc18', '0 18 * * 0', $$select public.consumer_cron_call('/api/consumer/cron/weekly')$$);
-- 09:00 Europe/London daily: trial-ending reminders, lock sweeps.
select cron.schedule('consumer_daily_utc08',  '0 8 * * *',  $$select public.consumer_cron_call('/api/consumer/cron/daily')$$);
select cron.schedule('consumer_daily_utc09',  '0 9 * * *',  $$select public.consumer_cron_call('/api/consumer/cron/daily')$$);
-- Hourly: the new-messages batch.
select cron.schedule('consumer_hourly',       '5 * * * *',  $$select public.consumer_cron_call('/api/consumer/cron/hourly')$$);

comment on table public.platform_settings is
  'MRB-310/315. Operator-editable platform values. Service role writes; operators read.';
comment on function public.consumer_cron_call(text) is
  'MRB-310. Called by pg_cron. POSTs to the backend at platform_settings.cron_target_url with the shared secret. No-op until configured.';