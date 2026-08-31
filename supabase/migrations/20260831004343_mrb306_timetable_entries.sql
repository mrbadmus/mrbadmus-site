-- MRB-306 WS-1 — timetable structure.
--
-- A teaching timetable: one row per teacher × weekday × period (× cycle).
-- The teacher link mirrors pending_staff_classes exactly: a CLAIMED teacher is
-- held by profile id, an UNCLAIMED one by pending_staff id, and
-- claim_pending_staff() re-points the rows on first sign-in — the same
-- mechanism, and the same moment, as the class links.
--
-- ⚠️ The brief for this work said "pending_staff EMAIL for unclaimed". It is
-- keyed on pending_staff_id instead, deliberately: the brief also required the
-- SAME mechanism as class assignments, and that mechanism
-- (pending_staff_classes) keys on the id. A FK cascades, cannot drift from the
-- pending row when an address is corrected, and claim_pending_staff() already
-- holds ps.id at the moment it needs it. The email stays reachable through
-- the FK.
--
-- Rainford runs a one-week timetable with five periods a day, so week_cycle is
-- null here; it exists because a two-week (A/B) timetable is the common other
-- shape and retro-fitting it into the unique index later would be a migration
-- against live rows.
--
-- Period CLOCK TIMES are deliberately absent. Rainford's are unknown and
-- inventing them would put a wrong time in front of a teacher; school_period_times
-- is the empty structure that will hold them, and until it is filled the UI
-- orders by period number and says "Period 1 … 5".
--
-- Applied to prod 31 Aug 2026 via MCP apply_migration, after rehearsal on TEST
-- (qeppkiswvclkkwbxmlok) where all seven constraint cases and the claim
-- round-trip were proven. This filename's version matches the version the MCP
-- recorded in schema_migrations, so `db push` will not re-apply it.

create table if not exists public.timetable_entries (
  id                uuid primary key default gen_random_uuid(),
  school_id         uuid not null references public.schools(id),
  academic_year_id  uuid not null references public.academic_years(id),
  class_id          uuid not null references public.classes(id),
  teacher_id        uuid references public.profiles(id),
  pending_staff_id  uuid references public.pending_staff(id) on delete cascade,
  weekday           smallint not null check (weekday between 1 and 5),
  period            smallint not null check (period between 1 and 20),
  week_cycle        text     check (week_cycle in ('A','B')),
  source            text not null default 'seeded'
                      check (source in ('seeded','upload','manual')),
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now(),
  deleted_at        timestamptz,
  constraint timetable_entries_one_owner check (
    (teacher_id is not null and pending_staff_id is null)
    or (teacher_id is null and pending_staff_id is not null))
);

-- A teacher stands in one room at a time. Live rows only, so a soft-deleted
-- row never blocks the slot a re-upload wants to fill.
create unique index if not exists timetable_entries_teacher_slot_unique
  on public.timetable_entries (teacher_id, academic_year_id, weekday, period, coalesce(week_cycle,''))
  where deleted_at is null and teacher_id is not null;

create unique index if not exists timetable_entries_pending_slot_unique
  on public.timetable_entries (pending_staff_id, academic_year_id, weekday, period, coalesce(week_cycle,''))
  where deleted_at is null and pending_staff_id is not null;

create index if not exists timetable_entries_teacher_day_idx
  on public.timetable_entries (teacher_id, weekday) where deleted_at is null;
create index if not exists timetable_entries_class_idx
  on public.timetable_entries (class_id) where deleted_at is null;
create index if not exists timetable_entries_pending_idx
  on public.timetable_entries (pending_staff_id) where deleted_at is null;

comment on table public.timetable_entries is
  'MRB-306: one teaching period. Owner is exactly one of teacher_id (claimed) or pending_staff_id (seeded, unclaimed); claim_pending_staff() re-points on first sign-in.';

-- ---------------------------------------------------------------------------
-- Period clock times. Structure only — no rows, and none invented.
-- ---------------------------------------------------------------------------
create table if not exists public.school_period_times (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id),
  period     smallint not null check (period between 1 and 20),
  starts_at  time,
  ends_at    time,
  label      text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint school_period_times_order check (
    starts_at is null or ends_at is null or ends_at > starts_at)
);
create unique index if not exists school_period_times_unique
  on public.school_period_times (school_id, period);

comment on table public.school_period_times is
  'MRB-306: per-school period clock times. Deliberately EMPTY — Rainford''s are unknown and are not to be invented. Until a row exists the UI labels by period number.';

-- ---------------------------------------------------------------------------
-- RLS. A teacher reads and writes only their own timetable; a school_admin
-- reads the school's. Seeded (unclaimed) rows have no authenticated owner yet,
-- so only a school_admin can see them.
--
-- Note on the RLS soft-delete gotcha (CLAUDE.md): the SELECT policy filters on
-- teacher_id, NOT on deleted_at, so a teacher soft-deleting their own row
-- leaves a post-update row the policy still admits. Re-upload is safe.
-- ---------------------------------------------------------------------------
alter table public.timetable_entries  enable row level security;
alter table public.school_period_times enable row level security;

drop policy if exists timetable_entries_own_all on public.timetable_entries;
create policy timetable_entries_own_all on public.timetable_entries for all
  using      (teacher_id = auth.uid())
  with check (teacher_id = auth.uid());

drop policy if exists timetable_entries_admin_read on public.timetable_entries;
create policy timetable_entries_admin_read on public.timetable_entries for select
  using (school_id = public.auth_user_school_id()
         and public.auth_user_has_scope('school_admin'));

drop policy if exists school_period_times_school_read on public.school_period_times;
create policy school_period_times_school_read on public.school_period_times for select
  using (school_id = public.auth_user_school_id());

drop policy if exists school_period_times_admin_write on public.school_period_times;
create policy school_period_times_admin_write on public.school_period_times for all
  using      (school_id = public.auth_user_school_id() and public.auth_user_has_scope('school_admin'))
  with check (school_id = public.auth_user_school_id() and public.auth_user_has_scope('school_admin'));
