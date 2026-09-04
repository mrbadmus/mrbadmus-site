-- MRB-309 Night 2, migration 1 of 9: the access-state helper, and the columns
-- Stripe keeps in sync.
--
-- Night 1 left org_is_entitled() as a boolean. Night 2 needs THREE answers,
-- not two: full access, read-only (the child can view lessons and past work
-- but cannot submit, no new work is generated, chat is read-only, marking is
-- closed) and locked (the same for the child; the parent additionally sees a
-- reactivate path). org_access_state() is that single helper. The backend's
-- orgAccess() and the frontend's guard both read it; nothing else decides.
--
-- ⚠️ Two behaviour changes to Night 1, both deliberate:
--   1. `trialing` now requires trial_end > now(). Night 1 let a family sit on
--      a 'trialing' row forever if it never reached Stripe checkout — a free
--      account with no card. The ruling is "7-day trial, CARD REQUIRED", so
--      the trial is Stripe's trial, started at checkout.
--   2. create_family_for_parent() now inserts status 'none' with no trial_end.
--      A family that has not checked out has no entitlement. The parent can
--      still sign in, add children and reach checkout: requireParent no longer
--      answers 402 on its own — routes ask for the state they need.

alter table public.subscriptions
  drop constraint if exists subscriptions_status_check;
alter table public.subscriptions
  add constraint subscriptions_status_check check (status in
    ('none', 'trialing', 'active', 'past_due', 'canceled', 'locked', 'comped'));

alter table public.subscriptions
  add column if not exists cancel_at_period_end boolean not null default false,
  add column if not exists billing_interval     text,
  add column if not exists stripe_price_id      text,
  add column if not exists retry_at             timestamptz,
  add column if not exists last_payment_failed_at timestamptz,
  add column if not exists canceled_at          timestamptz,
  add column if not exists locked_at            timestamptz;

alter table public.subscriptions
  drop constraint if exists subscriptions_billing_interval_check;
alter table public.subscriptions
  add constraint subscriptions_billing_interval_check
  check (billing_interval is null or billing_interval in ('month', 'year'));

comment on column public.subscriptions.cancel_at_period_end is
  'Mirrors Stripe. True means the parent cancelled (or removed their last child) and access runs to current_period_end.';
comment on column public.subscriptions.retry_at is
  'Stripe''s next_payment_attempt for the open failed invoice, while past_due.';
comment on column public.subscriptions.locked_at is
  'Set by the webhook/cron when an org first reaches the locked state; cleared on reactivation.';

-- ---------------------------------------------------------------------
-- org_access_state: the ONE helper.
-- ---------------------------------------------------------------------
create or replace function public.org_access_state(p_org_id uuid)
returns text
language plpgsql
stable
security definer
set search_path to 'public'
as $fn$
declare
  v_kind text;
  s      public.subscriptions%rowtype;
begin
  if p_org_id is null then return 'locked'; end if;

  select kind into v_kind from public.schools where id = p_org_id and deleted_at is null;
  if v_kind is null then return 'locked'; end if;

  -- A real school is never gated. Rainford has no Stripe row and must not
  -- need one.
  if v_kind = 'school' then return 'full'; end if;

  select * into s from public.subscriptions where org_id = p_org_id and deleted_at is null;
  if not found then
    return case when v_kind = 'family' then 'none' else 'locked' end;
  end if;

  if v_kind = 'organisation' then
    -- Sales-led: the seat cap and the period end are set by hand from Admin.
    if s.seat_cap is not null and s.current_period_end is not null and s.current_period_end > now() then
      return 'full';
    end if;
    if s.current_period_end is not null and s.current_period_end + interval '14 days' > now() then
      return 'read_only';
    end if;
    return 'locked';
  end if;

  -- family
  if s.status = 'comped' then
    return case when s.comped_until is not null and s.comped_until > now() then 'full' else 'locked' end;
  end if;
  if s.status = 'none' then return 'none'; end if;
  if s.status = 'locked' then return 'locked'; end if;
  if s.status = 'active' then return 'full'; end if;
  if s.status = 'trialing' then
    -- Stripe moves a trial on at trial_end. A trial with no end, or one whose
    -- end has passed without Stripe telling us, is stale — read-only, never
    -- a free forever.
    return case when s.trial_end is not null and s.trial_end > now() then 'full' else 'read_only' end;
  end if;
  if s.status = 'past_due' then
    -- Dunning grace: seven days of full access past the period end, then
    -- read-only until Stripe either collects (active) or gives up (canceled).
    if s.current_period_end is not null and s.current_period_end + interval '7 days' > now() then
      return 'full';
    end if;
    return 'read_only';
  end if;
  if s.status = 'canceled' then
    -- Read-only to the end of what was paid for, then locked.
    if s.current_period_end is not null and s.current_period_end > now() then
      return 'read_only';
    end if;
    return 'locked';
  end if;
  return 'locked';
end
$fn$;

comment on function public.org_access_state(uuid) is
  'MRB-309. full | read_only | locked | none. The single source of truth for what an org may do. org_is_entitled() is exactly (org_access_state() = ''full'').';

-- org_is_entitled keeps its signature (requireParent and Night 1 callers read
-- it) but is now defined ON TOP of the state, so the two can never disagree.
create or replace function public.org_is_entitled(p_org_id uuid)
returns boolean
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select public.org_access_state(p_org_id) = 'full';
$fn$;

-- A family that has not checked out has no trial yet. The 7 days are
-- Stripe's, and they start when a card is on file.
create or replace function public.create_family_for_parent(
  p_user_id     uuid,
  p_family_name text default null
)
returns uuid
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare
  v_email      text;
  v_confirmed  boolean;
  v_first      text;
  v_existing   uuid;
  v_school     uuid;
  v_year       uuid;
  v_y          int;
  v_year_name  text;
  v_name       text;
  v_code       text;
begin
  if p_user_id is null then
    raise exception 'create_family_for_parent: no user id given';
  end if;

  select u.email, u.email_confirmed_at is not null
    into v_email, v_confirmed
    from auth.users u where u.id = p_user_id;

  if v_email is null then
    raise exception 'create_family_for_parent: no such auth user %', p_user_id;
  end if;

  -- The ruling is explicit: email verification before the family is usable.
  if not v_confirmed then
    raise exception 'create_family_for_parent: email not verified for %', p_user_id;
  end if;

  -- IDEMPOTENT. Verification links get clicked twice, and a retried request
  -- must not mint a second family. If this parent already has one, hand back
  -- the same id rather than creating another.
  select p.school_id into v_existing
    from public.profiles p
    join public.schools s on s.id = p.school_id
   where p.id = p_user_id and s.kind = 'family' and s.deleted_at is null;

  if v_existing is not null then
    return v_existing;
  end if;

  -- Refuse to convert someone who already belongs to a real school. A
  -- Rainford teacher signing up as a parent on their work email would
  -- otherwise have their staff profile silently repointed at a family org,
  -- losing every class link they hold.
  if exists (
    select 1 from public.profiles p
     join public.schools s on s.id = p.school_id
    where p.id = p_user_id and s.kind = 'school'
  ) then
    raise exception 'create_family_for_parent: % already belongs to a school; a family needs a separate account', p_user_id;
  end if;

  select nullif(btrim(coalesce(first_name, '')), '') into v_first
    from public.profiles where id = p_user_id;

  v_name := nullif(btrim(coalesce(p_family_name, '')), '');
  if v_name is null then
    v_name := coalesce(v_first || '''s family', 'Family ' || substr(p_user_id::text, 1, 8));
  end if;

  -- No unique index on schools.code, but a colliding code would still be
  -- confusing in Admin, so make it wide enough not to.
  v_code := 'FAM-' || upper(substr(replace(p_user_id::text, '-', ''), 1, 10));

  -- The academic year. classes.academic_year_id is NOT NULL and
  -- academic_years.school_id is NOT NULL, so a family that cannot make a
  -- class is a family that cannot hold a child. English academic year:
  -- September to 31 August, which is what workingAcademicYear()'s 30-day
  -- lookahead expects to find.
  v_y := case when extract(month from now()) >= 9
              then extract(year from now())::int
              else extract(year from now())::int - 1 end;
  v_year_name := v_y::text || '-' || right((v_y + 1)::text, 2);

  insert into public.schools
    (name, code, kind, show_on_public_leaderboard,
     email_domains, key_stages_supported, departments, active)
  values
    (v_name, v_code, 'family',
     -- Not negotiable, and also enforced by schools_consumer_orgs_are_private:
     -- a family is never on the public leaderboard.
     false,
     '{}',                      -- no SSO domain: a family is not domain-keyed
     array['KS3','KS4'],
     array['Science'],
     true)
  returning id into v_school;

  insert into public.academic_years
    (school_id, name, start_date, end_date, is_current)
  values
    (v_school, v_year_name,
     make_date(v_y, 9, 1), make_date(v_y + 1, 8, 31), true)
  returning id into v_year;

  -- role and school_id move together: profiles_staff_school_guard raises if a
  -- non-student profile is left without a school_id, so this cannot be split.
  update public.profiles
     set role       = 'parent',
         school_id  = v_school,
         updated_at = now()
   where id = p_user_id;

  -- This row, not the role string, is what makes the parent an admin — and
  -- only of this org. Every scope grant in the estate is conjoined with
  -- school_id = auth_user_school_id(), so it reaches nothing else.
  insert into public.staff_scopes
    (profile_id, scope, school_id, department, granted_by, reason)
  values
    (p_user_id, 'school_admin', v_school, null, p_user_id,
     'MRB-308: parent is admin of their own family org');

  -- ⊕ MRB-309: no trial until checkout. The 7 days are Stripe's and start
  -- when a card is on file. 'none' means "never subscribed" — the parent can
  -- sign in, add children and reach checkout; nothing else is open.
  insert into public.subscriptions
    (org_id, status, trial_end, quantity)
  values
    (v_school, 'none', null, 0)
  on conflict (org_id) do nothing;

  perform public.write_audit_event(
    p_action       => 'family.created',
    p_target_table => 'schools',
    p_target_id    => v_school,
    p_payload      => jsonb_build_object('parent_id', p_user_id,
                                         'family_name', v_name,
                                         'academic_year', v_year_name),
    p_actor_id     => p_user_id,
    p_school_id    => v_school);

  return v_school;
end
$fn$;

-- ---------------------------------------------------------------------
-- guardian_of_child: a parent of the child, or staff of the child's
-- organisation-kind org. Organisation staff hold the same controls a parent
-- does (pause, intensity, position, add/remove work, report), so every
-- consumer route that says "the parent" means this.
-- ---------------------------------------------------------------------
create or replace function public.guardian_of_child(p_actor uuid, p_child uuid)
returns boolean
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select public.parent_owns_child(p_actor, p_child)
      or exists (
        select 1
          from public.profiles actor
          join public.schools  org   on org.id = actor.school_id
          join public.profiles child on child.school_id = actor.school_id
         where actor.id = p_actor
           and child.id = p_child
           and p_actor <> p_child
           and actor.role in ('teacher', 'hod', 'admin')
           and child.role = 'student'
           and org.kind = 'organisation'
           and org.deleted_at is null
           and actor.deleted_at is null
           and child.deleted_at is null
      );
$fn$;

-- Does this profile belong to a consumer-kind org (family or organisation)?
-- Used by the backend to decide whether the access-state gate applies at all,
-- so Rainford's routes pay nothing for it.
create or replace function public.profile_consumer_org(p_profile uuid)
returns uuid
language sql
stable
security definer
set search_path to 'public'
as $fn$
  select p.school_id
    from public.profiles p
    join public.schools s on s.id = p.school_id
   where p.id = p_profile
     and s.kind in ('family', 'organisation')
     and s.deleted_at is null;
$fn$;