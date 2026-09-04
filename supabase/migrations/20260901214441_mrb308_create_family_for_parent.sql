-- MRB-308 Night 1, migration 5 of 6: the family, created atomically.
--
-- "No half-created families." A family is FIVE rows that must exist together
-- or not at all: the org, its academic year, the parent's promoted profile,
-- the parent's school_admin scope, and the trial subscription. A function is
-- one transaction, so a failure anywhere rolls the whole family back.
--
-- Called by the backend with the SERVICE ROLE, after email verification.

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

  -- The 7-day trial starts here. Stripe will overwrite this row on Night 2;
  -- until then it is what org_is_entitled() reads.
  insert into public.subscriptions
    (org_id, status, trial_end, quantity)
  values
    (v_school, 'trialing', now() + interval '7 days', 0)
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

comment on function public.create_family_for_parent(uuid, text) is
  'MRB-308. Atomically creates a family org, its academic year, the parent''s '
  'promoted profile, their school_admin scope and a 7-day trial subscription. '
  'Idempotent: returns the existing family if one exists. Refuses a user who '
  'already belongs to a school-kind org. Service role only.';

-- Deliberately NOT granted to authenticated or anon. A signed-in user must
-- not be able to mint themselves an org; the backend calls this with the
-- service role after it has verified the email.
revoke all on function public.create_family_for_parent(uuid, text) from public, anon, authenticated;
