-- MRB-310 Night 2, migration 3 of 9: the child's plan, and the work it produces.
--
-- Three tables.
--
-- child_plans     — one row per consumer child: paused or not, and WHERE they
--                   are in the default scheme of work. Position is a cursor
--                   per subject (the SOW's academic_week, which at KS3 is a
--                   per-(year, subject) teaching order, not a calendar). A
--                   light-mode child advances one subject a week; a full-mode
--                   child advances all three. Seeded at onboarding from the
--                   "where are they up to" picker, defaulting to the term week.
-- work_items      — what appears on the child's Today screen. Every item
--                   carries set_by: the literal 'mrbadmus' for the scheduler,
--                   or the profile id of the parent / caseworker who set it.
-- work_generation_runs — the idempotency ledger: one row per (child, week).
--                   The scheduler never generates twice for the same week.
--
-- Reads: the child (own rows), their guardian (guardian_of_child), operators.
-- Writes: service role only. Every parent control is a backend route that
-- checks guardian_of_child() and then writes with the service role.

create table if not exists public.child_plans (
  child_id          uuid primary key references public.profiles(id),
  org_id            uuid not null references public.schools(id),
  paused_at         timestamptz,
  paused_by         uuid references public.profiles(id),
  pause_log         jsonb not null default '[]'::jsonb,   -- [{"from": ts, "to": ts|null}]
  cursors           jsonb not null default '{}'::jsonb,   -- {"Biology": 3, "Chemistry": 3, "Physics": 3}
  position_set_by   text,                                  -- 'term_week' | 'picker' | profile id
  position_set_at   timestamptz,
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now()
);

create index if not exists idx_child_plans_org on public.child_plans (org_id);

create table if not exists public.work_items (
  id             uuid primary key default gen_random_uuid(),
  org_id         uuid not null references public.schools(id),
  child_id       uuid not null references public.profiles(id),
  week_start     date not null,                 -- the Monday
  scheduled_for  date not null,
  position       smallint not null default 0,
  kind           text not null,
  title          text not null,
  sub            text,
  minutes        smallint not null default 20,
  ref            jsonb not null default '{}'::jsonb,
  set_by         text not null default 'mrbadmus',
  status         text not null default 'set',
  done_at        timestamptz,
  removed_at     timestamptz,
  removed_by     uuid references public.profiles(id),
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now(),
  constraint work_items_kind_check   check (kind in ('lesson', 'practice', 'exam', 'unit_check', 'flashcards')),
  constraint work_items_status_check check (status in ('set', 'done', 'removed')),
  constraint work_items_minutes_check check (minutes between 5 and 60),
  constraint work_items_set_by_check check (set_by = 'mrbadmus' or set_by ~* '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
);

create index if not exists idx_work_items_child_week on public.work_items (child_id, week_start, position);
create index if not exists idx_work_items_org on public.work_items (org_id, week_start);
create index if not exists idx_work_items_ref_assignment on public.work_items ((ref->>'assignment_id')) where kind = 'practice';

create table if not exists public.work_generation_runs (
  child_id      uuid not null references public.profiles(id),
  week_start    date not null,
  generated_at  timestamptz not null default now(),
  items         smallint not null default 0,
  note          text,
  primary key (child_id, week_start)
);

-- ---------------------------------------------------------------------
-- RLS — the same three readers on every consumer table.
-- ---------------------------------------------------------------------
alter table public.child_plans           enable row level security;
alter table public.work_items            enable row level security;
alter table public.work_generation_runs  enable row level security;

drop policy if exists child_plans_read on public.child_plans;
create policy child_plans_read on public.child_plans
  for select using (
    child_id = auth.uid()
    or public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

drop policy if exists work_items_read on public.work_items;
create policy work_items_read on public.work_items
  for select using (
    child_id = auth.uid()
    or public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

drop policy if exists work_generation_runs_read on public.work_generation_runs;
create policy work_generation_runs_read on public.work_generation_runs
  for select using (
    public.guardian_of_child(auth.uid(), child_id)
    or public.auth_user_operator_active()
  );

revoke insert, update, delete on public.child_plans          from anon, authenticated;
revoke insert, update, delete on public.work_items           from anon, authenticated;
revoke insert, update, delete on public.work_generation_runs from anon, authenticated;

create or replace function public.consumer_touch_updated_at()
returns trigger language plpgsql as $fn$
begin
  new.updated_at := now();
  return new;
end $fn$;

drop trigger if exists trg_child_plans_touch on public.child_plans;
create trigger trg_child_plans_touch before update on public.child_plans
  for each row execute function public.consumer_touch_updated_at();

drop trigger if exists trg_work_items_touch on public.work_items;
create trigger trg_work_items_touch before update on public.work_items
  for each row execute function public.consumer_touch_updated_at();

comment on table public.child_plans is
  'MRB-310. Per consumer child: pause state and per-subject SOW cursors. Service role writes.';
comment on table public.work_items is
  'MRB-310. The child''s Today list. set_by is ''mrbadmus'' or the guardian''s profile id, so the screen can label it. Service role writes.';
comment on table public.work_generation_runs is
  'MRB-310. One row per (child, week): the scheduler is idempotent on it.';