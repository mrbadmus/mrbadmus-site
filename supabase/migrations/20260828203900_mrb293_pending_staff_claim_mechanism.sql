-- MRB-293 — pending-staff claim mechanism.
--
-- A member of staff is seeded here BEFORE they have an account. The first time
-- they sign in with a verified email that matches a seeded row (case-insensitively),
-- their profile is promoted to staff, their class links are created and their
-- admin scopes are applied. Identity keys on EMAIL only — never on name, because
-- Microsoft directory names are unreliable and a name mismatch would strand a
-- teacher in an empty dashboard.

create table if not exists public.pending_staff (
  id                 uuid primary key default gen_random_uuid(),
  school_id          uuid not null references public.schools(id),
  email              citext not null,
  first_name         text,
  last_name          text,
  staff_code         text,
  profile_role       text not null default 'teacher'
                       check (profile_role in ('teacher','hod','admin')),
  granted_by         uuid not null references public.profiles(id),
  reason             text,
  claimed_at         timestamptz,
  claimed_profile_id uuid references public.profiles(id),
  created_at         timestamptz not null default now(),
  updated_at         timestamptz not null default now(),
  deleted_at         timestamptz
);

-- One live pending row per person. The claim looks a person up by email alone,
-- so the email must be unique across live rows, not merely per school.
create unique index if not exists pending_staff_live_email_unique
  on public.pending_staff (email) where deleted_at is null;
create index if not exists pending_staff_unclaimed_idx
  on public.pending_staff (email) where deleted_at is null and claimed_at is null;

create table if not exists public.pending_staff_scopes (
  id               uuid primary key default gen_random_uuid(),
  pending_staff_id uuid not null references public.pending_staff(id) on delete cascade,
  scope            text not null check (scope in ('hod','slt','school_admin')),
  department       text,
  created_at       timestamptz not null default now(),
  constraint pending_staff_scopes_hod_needs_department check (scope <> 'hod' or department is not null),
  constraint pending_staff_scopes_dept_only_for_hod   check (scope =  'hod' or department is null)
);
create unique index if not exists pending_staff_scopes_unique
  on public.pending_staff_scopes (pending_staff_id, scope, coalesce(department,''));

create table if not exists public.pending_staff_classes (
  id               uuid primary key default gen_random_uuid(),
  pending_staff_id uuid not null references public.pending_staff(id) on delete cascade,
  class_id         uuid not null references public.classes(id),
  subject_id       uuid references public.subjects(id),
  role             text not null default 'subject_teacher'
                     check (role in ('subject_teacher','form_tutor','cover_teacher')),
  created_at       timestamptz not null default now(),
  -- mirrors class_teachers_subject_required_check
  constraint pending_staff_classes_subject_required check (
    (role = 'form_tutor' and subject_id is null)
    or (role in ('subject_teacher','cover_teacher') and subject_id is not null))
);
create unique index if not exists pending_staff_classes_unique
  on public.pending_staff_classes (pending_staff_id, class_id, subject_id, role);

alter table public.pending_staff         enable row level security;
alter table public.pending_staff_scopes  enable row level security;
alter table public.pending_staff_classes enable row level security;

-- Visible only to a school_admin of the same school, and to platform operators.
-- No student or ordinary-teacher path reads these tables at all.
drop policy if exists pending_staff_admin_all on public.pending_staff;
create policy pending_staff_admin_all on public.pending_staff for all
  using      (school_id = public.auth_user_school_id() and public.auth_user_has_scope('school_admin'))
  with check (school_id = public.auth_user_school_id() and public.auth_user_has_scope('school_admin'));

drop policy if exists pending_staff_operator_read on public.pending_staff;
create policy pending_staff_operator_read on public.pending_staff for select
  using (public.auth_user_operator_active());

drop policy if exists pending_staff_scopes_admin_all on public.pending_staff_scopes;
create policy pending_staff_scopes_admin_all on public.pending_staff_scopes for all
  using (exists (select 1 from public.pending_staff ps where ps.id = pending_staff_id
                   and ps.school_id = public.auth_user_school_id()
                   and public.auth_user_has_scope('school_admin')))
  with check (exists (select 1 from public.pending_staff ps where ps.id = pending_staff_id
                   and ps.school_id = public.auth_user_school_id()
                   and public.auth_user_has_scope('school_admin')));

drop policy if exists pending_staff_classes_admin_all on public.pending_staff_classes;
create policy pending_staff_classes_admin_all on public.pending_staff_classes for all
  using (exists (select 1 from public.pending_staff ps where ps.id = pending_staff_id
                   and ps.school_id = public.auth_user_school_id()
                   and public.auth_user_has_scope('school_admin')))
  with check (exists (select 1 from public.pending_staff ps where ps.id = pending_staff_id
                   and ps.school_id = public.auth_user_school_id()
                   and public.auth_user_has_scope('school_admin')));

-- ---------------------------------------------------------------------------
-- The claim itself. Idempotent, and safe to call on every sign-in.
-- ---------------------------------------------------------------------------
create or replace function public.claim_pending_staff(p_user_id uuid)
returns boolean
language plpgsql
security definer
set search_path = public
as $fn$
declare
  v_email     citext;
  v_confirmed boolean;
  v_meta      jsonb;
  ps          public.pending_staff%rowtype;
  v_first     text;
  v_last      text;
  v_full      text;
  v_links     int := 0;
  v_scopes    int := 0;
begin
  select u.email::citext,
         u.email_confirmed_at is not null,
         coalesce(u.raw_user_meta_data, '{}'::jsonb)
    into v_email, v_confirmed, v_meta
    from auth.users u
   where u.id = p_user_id;

  -- Only a verified identity may claim.
  if v_email is null or not v_confirmed then
    return false;
  end if;

  select * into ps
    from public.pending_staff
   where email = v_email          -- citext: exact address, case-insensitive
     and deleted_at is null
     and claimed_at is null
   order by created_at
   limit 1;

  if not found then
    return false;                 -- any other sign-in proceeds exactly as today
  end if;

  -- The profile must already exist (handle_new_user creates it).
  if not exists (select 1 from public.profiles where id = p_user_id) then
    return false;
  end if;

  -- Names come from the Microsoft identity; the seeded names are only a fallback.
  -- Microsoft supplies full_name far more reliably than given_name/family_name.
  v_first := nullif(btrim(coalesce(v_meta->>'given_name',  v_meta->>'first_name', '')), '');
  v_last  := nullif(btrim(coalesce(v_meta->>'family_name', v_meta->>'last_name',  '')), '');
  v_full  := nullif(btrim(coalesce(v_meta->>'full_name',   v_meta->>'name',       '')), '');

  if (v_first is null or v_last is null) and v_full is not null then
    if position(',' in v_full) > 0 then
      -- directory form "Surname, Firstname"
      v_last  := coalesce(v_last,  nullif(btrim(split_part(v_full, ',', 1)), ''));
      v_first := coalesce(v_first, nullif(btrim(split_part(v_full, ',', 2)), ''));
    elsif position(' ' in v_full) > 0 then
      v_first := coalesce(v_first, nullif(btrim(split_part(v_full, ' ', 1)), ''));
      v_last  := coalesce(v_last,  nullif(btrim(substring(v_full from position(' ' in v_full) + 1)), ''));
    else
      v_first := coalesce(v_first, v_full);
    end if;
  end if;

  v_first := coalesce(v_first, ps.first_name);
  v_last  := coalesce(v_last,  ps.last_name);

  -- Promote. role and school_id move together: profiles_staff_school_guard
  -- rejects a staff profile with no school.
  update public.profiles
     set role       = ps.profile_role,
         school_id  = ps.school_id,
         first_name = v_first,
         last_name  = v_last,
         updated_at = now()
   where id = p_user_id;

  insert into public.class_teachers (class_id, teacher_id, subject_id, role)
  select psc.class_id, p_user_id, psc.subject_id, psc.role
    from public.pending_staff_classes psc
   where psc.pending_staff_id = ps.id
     and not exists (
       select 1 from public.class_teachers ct
        where ct.class_id   = psc.class_id
          and ct.teacher_id = p_user_id
          and ct.subject_id is not distinct from psc.subject_id
          and ct.role       = psc.role
          and ct.ended_at is null and ct.deleted_at is null);
  get diagnostics v_links = row_count;

  insert into public.staff_scopes (profile_id, scope, school_id, department, granted_by, reason)
  select p_user_id, pss.scope, ps.school_id, pss.department, ps.granted_by,
         coalesce(ps.reason, 'Seeded staff scope, applied on first sign-in')
    from public.pending_staff_scopes pss
   where pss.pending_staff_id = ps.id
     and not exists (
       select 1 from public.staff_scopes ss
        where ss.profile_id = p_user_id
          and ss.scope      = pss.scope
          and ss.school_id  = ps.school_id
          and coalesce(ss.department,'') = coalesce(pss.department,'')
          and ss.ended_at is null and ss.deleted_at is null);
  get diagnostics v_scopes = row_count;

  update public.pending_staff
     set claimed_at         = now(),
         claimed_profile_id = p_user_id,
         updated_at         = now()
   where id = ps.id;

  perform public.write_audit_event(
    p_action       => 'pending_staff.claimed',
    p_target_table => 'pending_staff',
    p_target_id    => ps.id,
    p_payload      => jsonb_build_object('staff_code', ps.staff_code, 'role', ps.profile_role,
                                         'class_links_created', v_links, 'scopes_granted', v_scopes),
    p_actor_id     => p_user_id,
    p_school_id    => ps.school_id);

  return true;
end
$fn$;

revoke all on function public.claim_pending_staff(uuid) from public, anon, authenticated;

-- ---------------------------------------------------------------------------
-- Wiring. The claim must win over the 'student' default that handle_new_user
-- leaves behind, and must never be able to break a sign-in: if it raises, the
-- person still signs in with an ordinary profile and the pending row stays
-- unclaimed for the next attempt.
-- ---------------------------------------------------------------------------
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
as $fn$
BEGIN
  INSERT INTO public.profiles (id)
  VALUES (NEW.id)
  ON CONFLICT (id) DO NOTHING;

  BEGIN
    PERFORM public.claim_pending_staff(NEW.id);
  EXCEPTION WHEN OTHERS THEN
    RAISE WARNING 'claim_pending_staff failed for %: %', NEW.id, SQLERRM;
  END;

  RETURN NEW;
END;
$fn$;

-- Covers a seeded person who already had an account, and one whose email is
-- verified after the row was created. Idempotent, so re-firing is harmless.
create or replace function public.handle_user_signin_claim()
returns trigger
language plpgsql
security definer
as $fn$
BEGIN
  BEGIN
    PERFORM public.claim_pending_staff(NEW.id);
  EXCEPTION WHEN OTHERS THEN
    RAISE WARNING 'claim_pending_staff failed for %: %', NEW.id, SQLERRM;
  END;
  RETURN NEW;
END;
$fn$;

drop trigger if exists on_auth_user_signin_claim on auth.users;
create trigger on_auth_user_signin_claim
  after update on auth.users
  for each row
  when (old.last_sign_in_at    is distinct from new.last_sign_in_at
     or old.email_confirmed_at is distinct from new.email_confirmed_at)
  execute function public.handle_user_signin_claim();
