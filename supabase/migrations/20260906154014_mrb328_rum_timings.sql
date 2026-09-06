-- MRB-328 J4(a) — real-user timing, ours, and deliberately blind.
--
-- ⚠️ VERSION DRIFT BETWEEN THE TWO PROJECTS, DELIBERATELY RECONCILED HERE.
--
-- TEST took this as TWO migrations, because it was built in two passes:
--   20260906130922_mrb328_rum_timings
--   20260906131448_mrb328_rum_timings_school_from_profile
-- Production took the finished thing in ONE, and recorded it as
--   20260906154014_mrb328_rum_timings
-- which is the version this file is named for, following the MRB-326
-- precedent: the local file is named by the version PRODUCTION recorded, so a
-- future `supabase db push` does not re-apply what is already live.
--
-- The consequence to know about: TEST's schema_migrations carries two rows
-- this file does not correspond to one-for-one. The SCHEMA is identical on
-- both — the second pass only added the trigger, which is included below —
-- but a version-by-version diff of the two projects will show it, and that is
-- expected rather than a sign anything is out of step.

--
-- WHY A TABLE AT ALL, RATHER THAN A THIRD-PARTY RUM SCRIPT
--
-- Every number we have about how fast this site feels is a LOCAL measurement:
-- `teacher_perf_budget.py` drives headless Chrome against a TEST fixture over
-- a warm cache on a developer laptop on home broadband. That is a useful
-- regression gate and a terrible model of a Year 8 on a school Chromebook over
-- shared wifi. We have therefore never known what the site actually costs the
-- people using it, and every "it feels slow" has been answered with a guess.
--
-- A third-party RUM script would answer it and would also ship children's
-- browsing to a vendor. This is one table and one POST instead.
--
-- WHAT IT MAY NOT HOLD, ENFORCED RATHER THAN PROMISED
--
-- No names, no free text — not as a convention the client is trusted to keep,
-- but as CHECK constraints, because a beacon is written by JavaScript that
-- anyone can edit in a console and post whatever they like as themselves.
--   · `page` and `role` are whitelists.
--   · `conn` and `device` are whitelists.
--   · `fetches` is an array whose every element is {n, ms} with `n` matched
--     against a strict slug pattern — so a fetch label cannot become a
--     sentence, let alone a student's name.
-- The row identifies a PROFILE, which is unavoidable (RLS has to scope it) and
-- is a key, not a name.
--
-- ⚠️ There is no `path` or `url` column ON PURPOSE. A URL on this estate
-- carries `?class=<uuid>` and `?student=<uuid>`, so storing one would quietly
-- rebuild a per-child browsing log out of columns that each look innocent.
-- `page` is the coarse screen name and nothing finer.

-- The shape validator for `fetches`, as a constraint rather than a hope: each
-- element must be an object with a slug `n` and a bounded numeric `ms`.
--
-- It is a FUNCTION rather than an inline CHECK because Postgres refuses a
-- subquery inside a check constraint ("cannot use subquery in check
-- constraint") and walking a jsonb array needs one. Marked immutable so a
-- constraint may call it; it reads nothing but its argument.
create or replace function public.rum_fetches_ok(v jsonb)
returns boolean
language sql
immutable
set search_path to ''
as $$
  select jsonb_typeof(v) = 'array'
     and jsonb_array_length(v) <= 40
     and not exists (
       select 1 from jsonb_array_elements(v) e
       where jsonb_typeof(e) <> 'object'
          or not (e ? 'n') or not (e ? 'ms')
          or jsonb_typeof(e->'n')  <> 'string'
          or jsonb_typeof(e->'ms') <> 'number'
          or (e->>'n') !~ '^[a-z][a-z0-9_-]{0,39}$'
          or (e->>'ms')::numeric < 0
          or (e->>'ms')::numeric > 600000
     );
$$;

create table if not exists public.rum_timings (
  id          uuid primary key default gen_random_uuid(),
  profile_id  uuid not null references public.profiles(id) on delete cascade,
  school_id   uuid          references public.schools(id),

  page        text not null check (page in (
                'teacher-classes','teacher-class-detail','teacher-student',
                'teacher-today','teacher-timetable','teacher-admin',
                'teacher-import','teacher-assignment','teacher-digest',
                'teacher-insights','teacher-seating',
                'student-class','student-assignment')),
  role        text not null check (role in ('teacher','student')),

  -- Total ms from navigation start to the page being usable — the moment the
  -- skeleton is replaced, which is what MRB-292 made observable.
  ttoi_ms     integer not null check (ttoi_ms >= 0 and ttoi_ms < 600000),

  -- [{"n":"classes","ms":412}, ...]. Named fetches only; see the pattern check.
  fetches     jsonb not null default '[]'::jsonb
                constraint rum_timings_fetches_shape
                check (public.rum_fetches_ok(fetches)),

  conn        text check (conn   in ('slow-2g','2g','3g','4g','unknown')),
  device      text check (device in ('low','mid','high','unknown')),

  -- Which BUILD produced the timing. Without it, a week of rows spanning three
  -- deploys averages into a number that describes no version of the site.
  build       text check (build ~ '^[a-f0-9]{8}$'),

  created_at  timestamptz not null default now()
);

create index if not exists rum_timings_school_created_idx
  on public.rum_timings (school_id, created_at desc);
create index if not exists rum_timings_page_created_idx
  on public.rum_timings (page, created_at desc);

alter table public.rum_timings enable row level security;

-- INSERT: only ever as yourself. A beacon cannot be written on behalf of
-- another user, so one noisy client can only ever distort its own rows.
drop policy if exists rum_timings_insert_self on public.rum_timings;
create policy rum_timings_insert_self on public.rum_timings
  for insert to authenticated
  with check (profile_id = auth.uid());

-- SELECT: school admins, for their own school only.
--
-- ⚠️ The `school_id = auth_user_school_id()` conjunct IS the seal, exactly as
-- in the B2C work: without it a school admin at one school reads another
-- school's rows, and this table will eventually carry more than one school.
drop policy if exists rum_timings_read_admin on public.rum_timings;
create policy rum_timings_read_admin on public.rum_timings
  for select to authenticated
  using (
    school_id is not null
    and school_id = public.auth_user_school_id()
    and exists (
      select 1 from public.staff_scopes s
      where s.profile_id = auth.uid()
        and s.scope in ('school_admin','slt')
        and s.deleted_at is null
        and s.started_at <= now()
        and (s.ended_at is null or s.ended_at > now())
    )
  );

-- No UPDATE and no DELETE policy: a timing is a fact about a moment, and
-- nothing on the estate has any business editing one. Retention is a
-- scheduled job's concern, running as service-role, not a user's.

comment on table public.rum_timings is
  'MRB-328: real-user page timings. No names, no URLs, no free text — every '
  'text column is whitelisted or slug-checked. Insert-self, school-admin read.';


-- ── Second pass ────────────────────────────────────────────────────────

--
-- The first cut had the beacon send school_id from the client. Two things were
-- wrong with that.
--
-- It is usually NOT THERE. school_id lives on the profile row, not in the JWT's
-- user_metadata, so the column would have arrived null on most loads — and the
-- admin read policy requires it non-null. The table would have filled up with
-- rows no admin could ever read, and nothing would have looked broken until
-- someone finally asked for the numbers and got an empty result. That is the
-- failure mode this whole ticket exists to stop having.
--
-- And it let a client assert its own school, which is a thing a client should
-- never be able to say about itself.
--
-- SECURITY DEFINER because the inserting user cannot necessarily read the
-- profiles row the lookup needs; the function reads exactly one column of one
-- row, keyed by the profile_id the INSERT policy has already pinned to
-- auth.uid(), so it cannot be steered at another user's record.
create or replace function public.rum_timings_fill_school()
returns trigger
language plpgsql
security definer
set search_path to ''
as $$
begin
  select p.school_id into new.school_id
    from public.profiles p
   where p.id = new.profile_id;
  return new;
end;
$$;

drop trigger if exists rum_timings_fill_school on public.rum_timings;
create trigger rum_timings_fill_school
  before insert on public.rum_timings
  for each row execute function public.rum_timings_fill_school();
