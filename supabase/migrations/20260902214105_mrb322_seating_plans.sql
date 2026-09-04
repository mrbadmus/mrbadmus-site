-- ════════════════════════════════════════════════════════════════════════
-- MRB-322 — seating plans
--
--   room_layouts   the shape of a room: where the desks are, how many seats
--                  each has, which wall the board is on. One room may hold
--                  several layouts (the room gets rearranged; two teachers
--                  disagree about it), so the room code is NOT unique.
--   seating_plans  a class placed onto one of those layouts.
--
-- ── Why room_code is a CHECK and not a `rooms` table ──────────────────
-- The room list is fixed and nobody types a room name — not a teacher, not
-- an admin. The UI is a dropdown, and this CHECK is what makes that true at
-- the database rather than merely true in the markup. A lookup table would
-- buy extensibility this feature has no use for yet; when a second school
-- arrives the CHECK becomes a school-scoped `rooms` table and this comment
-- is the note that says so.
-- ════════════════════════════════════════════════════════════════════════

-- ── The cover-aware "does this person teach this class RIGHT NOW" test ──
--
-- ⚠️ This is deliberately NOT `auth_user_teaches_class()`. That helper asks
-- `ended_at IS NULL`, which reads a teacher as attached only while their
-- stint has no end date at all. Cover is booked the other way round: a cover
-- teacher gets a row with `started_at = now` and `ended_at = the day the
-- absence ends`, and under the old test that person is invisible for the
-- whole time they are actually standing in the room.
--
-- MRB-322 was ruled to give ACTIVE cover teacher visibility and expired
-- cover none, so it needs the interval read: started, and not yet ended.
-- The existing helper is left exactly as it is — it backs policies across
-- the whole estate and changing it here would move all of them at once.
-- That divergence is written up for Mide rather than fixed in passing.
create or replace function public.auth_user_teaches_class_now(p_class_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.class_teachers
     where class_id  = p_class_id
       and teacher_id = auth.uid()
       and deleted_at is null
       and (started_at is null or started_at <= now())
       and (ended_at   is null or ended_at   >  now())
  );
$$;

comment on function public.auth_user_teaches_class_now(uuid) is
  'MRB-322. Interval-aware sibling of auth_user_teaches_class: true while the '
  'caller''s class_teachers row has started and has not yet ended, so ACTIVE '
  'cover counts and expired cover does not.';

-- ── updated_at ───────────────────────────────────────────────────────
-- The estate keeps one touch function per feature (consumer_, subscriptions_,
-- platform_flags_) rather than one shared one; this follows that.
create or replace function public.seating_touch_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

-- ════════════════════════════════════════════════════════════════════════
-- room_layouts
-- ════════════════════════════════════════════════════════════════════════
create table if not exists public.room_layouts (
  id          uuid primary key default gen_random_uuid(),
  school_id   uuid not null references public.schools(id),
  room_code   text not null,
  name        text,
  layout      jsonb not null,
  source      text not null,
  created_by  uuid not null references public.profiles(id),
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  deleted_at  timestamptz,

  constraint room_layouts_room_code_check check (room_code in
    ('S01','S02a','S02b','S02c','S04','S08a','S08b','S08c','S09a','S09b','S010')),

  constraint room_layouts_source_check check (source in ('photo','template','manual')),

  -- Structural floor for the JSONB. The canvas validates far more strictly
  -- than this before it will draw; the point of repeating the desk cap and
  -- the front-wall vocabulary here is that a room layout can arrive from a
  -- vision model, and a model's output should not be trusted by the only
  -- component that happens to be looking at it.
  constraint room_layouts_layout_shape_check check (
    jsonb_typeof(layout) = 'object'
    and jsonb_typeof(layout -> 'desks') = 'array'
    and jsonb_array_length(layout -> 'desks') <= 60
    and (layout ->> 'front') in ('top','right','bottom','left')
  )
);

create index if not exists room_layouts_school_room_idx
  on public.room_layouts (school_id, room_code) where deleted_at is null;
create index if not exists room_layouts_author_idx
  on public.room_layouts (created_by) where deleted_at is null;

drop trigger if exists room_layouts_touch_updated_at on public.room_layouts;
create trigger room_layouts_touch_updated_at
  before update on public.room_layouts
  for each row execute function public.seating_touch_updated_at();

alter table public.room_layouts enable row level security;

-- read: the school.
-- Ruled as "read: school" and implemented literally. A layout row carries desk
-- geometry, a room code and an author uuid — no student data of any kind — so
-- the wide read costs nothing today. Noted for Mide because "school" does
-- include students, and no student-facing surface asks for it.
create policy room_layouts_school_read on public.room_layouts
  for select using (school_id = public.auth_user_school_id());

-- write: the author, or a school admin. Split per verb rather than FOR ALL so
-- that INSERT gets a WITH CHECK: FOR ALL's USING clause does not constrain an
-- insert, and without this a teacher could stamp another school's id onto a row.
create policy room_layouts_author_insert on public.room_layouts
  for insert with check (
    school_id  = public.auth_user_school_id()
    and created_by = auth.uid()
  );

create policy room_layouts_admin_insert on public.room_layouts
  for insert with check (
    school_id = public.auth_user_school_id()
    and public.auth_user_role() = 'admin'
  );

-- ⚠️ No `deleted_at is null` in any USING clause here, and that is deliberate.
-- Postgres applies the SELECT USING to the row's POST-update state, so a policy
-- that hid soft-deleted rows would make the soft delete itself fail with 42501
-- (CLAUDE.md, MRB-46 Phase 2). Filtering deleted rows is the client's job.
create policy room_layouts_author_update on public.room_layouts
  for update using (
    school_id = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  ) with check (
    school_id = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  );

-- No DELETE policy at all: layouts are retired with deleted_at, never removed,
-- because a saved seating plan points at one and a hard delete would orphan it.

-- ════════════════════════════════════════════════════════════════════════
-- seating_plans
-- ════════════════════════════════════════════════════════════════════════
create table if not exists public.seating_plans (
  id              uuid primary key default gen_random_uuid(),
  class_id        uuid not null references public.classes(id),
  room_layout_id  uuid not null references public.room_layouts(id),
  name            text,
  assignments     jsonb not null default '{}'::jsonb,
  created_by      uuid not null references public.profiles(id),
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now(),
  deleted_at      timestamptz,

  constraint seating_plans_assignments_shape_check
    check (jsonb_typeof(assignments) = 'object')
);

create index if not exists seating_plans_class_idx
  on public.seating_plans (class_id) where deleted_at is null;
create index if not exists seating_plans_layout_idx
  on public.seating_plans (room_layout_id) where deleted_at is null;

drop trigger if exists seating_plans_touch_updated_at on public.seating_plans;
create trigger seating_plans_touch_updated_at
  before update on public.seating_plans
  for each row execute function public.seating_touch_updated_at();

alter table public.seating_plans enable row level security;

-- read: someone who teaches this class right now — subject teacher, co-teacher
-- or ACTIVE cover, all three being just `class_teachers` rows — or a school
-- admin. A teacher who does not teach the class gets nothing, which is the
-- whole point: a seating plan is a named list of children.
create policy seating_plans_teacher_read on public.seating_plans
  for select using (
    public.auth_user_teaches_class_now(class_id)
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

create policy seating_plans_admin_read on public.seating_plans
  for select using (
    public.auth_user_role() = 'admin'
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

-- write: the author (who must also actually teach the class), or a school admin.
create policy seating_plans_author_insert on public.seating_plans
  for insert with check (
    created_by = auth.uid()
    and public.class_school_id(class_id) = public.auth_user_school_id()
    and public.auth_user_teaches_class_now(class_id)
  );

create policy seating_plans_admin_insert on public.seating_plans
  for insert with check (
    public.auth_user_role() = 'admin'
    and public.class_school_id(class_id) = public.auth_user_school_id()
  );

create policy seating_plans_author_update on public.seating_plans
  for update using (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  ) with check (
    public.class_school_id(class_id) = public.auth_user_school_id()
    and (created_by = auth.uid() or public.auth_user_role() = 'admin')
  );

-- No DELETE policy: soft delete only.
