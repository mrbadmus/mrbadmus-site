-- MRB-315 Night 2, migration 8 of 9: AI usage, and the caps per org.
--
-- ai_usage_events — one row per AI call the platform pays for: tutor turn,
--   AI mark, "explain my wrong answer". Tokens and a cost estimate in pence,
--   so Admin can show spend per org.
-- org_limits — per-org overrides of the platform defaults (which live in
--   platform_settings, migration 9). `enforce` is what opts a SCHOOL in:
--   consumer orgs are always enforced; a school is never enforced unless a
--   row here says so.
-- ai_usage_counts() — the two numbers the cap middleware needs, in one read,
--   in the London calendar (a day resets at midnight London, a month on the 1st).

create table if not exists public.ai_usage_events (
  id             uuid primary key default gen_random_uuid(),
  profile_id     uuid not null references public.profiles(id),
  org_id         uuid references public.schools(id),
  kind           text not null,
  model          text,
  input_tokens   integer,
  output_tokens  integer,
  cost_pence     numeric(10,4),
  created_at     timestamptz not null default now(),
  constraint ai_usage_events_kind_check check (kind in ('tutor_turn', 'ai_mark', 'explain'))
);

create index if not exists idx_ai_usage_events_profile on public.ai_usage_events (profile_id, kind, created_at desc);
create index if not exists idx_ai_usage_events_org on public.ai_usage_events (org_id, created_at desc);

create table if not exists public.org_limits (
  org_id               uuid primary key references public.schools(id),
  tutor_turns_per_day  integer,
  ai_marks_per_month   integer,
  mb_marks_per_month   integer,
  enforce              boolean,
  note                 text,
  updated_at           timestamptz not null default now(),
  updated_by           uuid references public.profiles(id),
  constraint org_limits_nonneg check (
    (tutor_turns_per_day is null or tutor_turns_per_day >= 0) and
    (ai_marks_per_month  is null or ai_marks_per_month  >= 0) and
    (mb_marks_per_month  is null or mb_marks_per_month  >= 0))
);

create or replace function public.ai_usage_counts(p_profile uuid)
returns jsonb
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select jsonb_build_object(
    'tutor_today', (
      select count(*) from public.ai_usage_events e
       where e.profile_id = p_profile and e.kind = 'tutor_turn'
         and (e.created_at at time zone 'Europe/London')::date = (now() at time zone 'Europe/London')::date),
    'marks_month', (
      select count(*) from public.ai_usage_events e
       where e.profile_id = p_profile and e.kind = 'ai_mark'
         and (e.created_at at time zone 'Europe/London') >= date_trunc('month', now() at time zone 'Europe/London')),
    'explain_today', (
      select count(*) from public.ai_usage_events e
       where e.profile_id = p_profile and e.kind = 'explain'
         and (e.created_at at time zone 'Europe/London')::date = (now() at time zone 'Europe/London')::date)
  );
$fn$;

alter table public.ai_usage_events enable row level security;
alter table public.org_limits      enable row level security;

drop policy if exists ai_usage_events_read on public.ai_usage_events;
create policy ai_usage_events_read on public.ai_usage_events
  for select using (
    profile_id = auth.uid()
    or public.guardian_of_child(auth.uid(), profile_id)
    or public.auth_user_operator_active()
  );

drop policy if exists org_limits_read on public.org_limits;
create policy org_limits_read on public.org_limits
  for select using (
    (org_id = public.auth_user_school_id() and public.auth_user_has_scope('school_admin'))
    or public.auth_user_operator_active()
  );

revoke insert, update, delete on public.ai_usage_events from anon, authenticated;
revoke insert, update, delete on public.org_limits      from anon, authenticated;

comment on table public.ai_usage_events is
  'MRB-315. One row per paid AI call. Service role writes; the child, their guardian and operators read.';
comment on table public.org_limits is
  'MRB-315. Per-org cap overrides. enforce=true opts a school in; consumer orgs are always enforced.';