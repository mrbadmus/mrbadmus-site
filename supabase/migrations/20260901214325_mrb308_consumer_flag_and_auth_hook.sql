-- MRB-308 Night 1, migration 4 of 6: the consumer flag, and the auth-hook fix.
--
-- WHY THIS MIGRATION EXISTS AT ALL (it was not in the ticket).
--
-- Recon found that hook_before_user_created gates provider IN ('azure',
-- 'google'). A parent signing up with Google today hits
-- school_id_for_email_domain('...@gmail.com') => NULL and is refused with a
-- 403: "The email domain @gmail.com is not recognised for any MrBadmusAI
-- school." Google parent signup is a locked ruling, so the hook had to move
-- or Night 1 would have shipped a front door that cannot be opened.
--
-- A Postgres auth hook cannot read a backend env var, so the flag needs a
-- form the DATABASE can see. Rather than let CONSUMER_SIGNUP_ENABLED drift
-- across three homes, the two gates are ANDed: the backend env var guards
-- the /api/consumer/* routes and the pages, this row guards ACCOUNT CREATION.
-- Either one being off means off. Both default off.

create table if not exists public.platform_flags (
  key         text primary key,
  enabled     boolean not null default false,
  note        text,
  updated_at  timestamptz not null default now(),
  updated_by  uuid references public.profiles(id)
);

alter table public.platform_flags enable row level security;

-- Anyone signed in may READ a flag (the frontend needs to know whether to
-- show a consumer entry point). Only platform operators may write one.
drop policy if exists platform_flags_read on public.platform_flags;
create policy platform_flags_read on public.platform_flags
  for select using (true);

drop policy if exists platform_flags_operator_write on public.platform_flags;
create policy platform_flags_operator_write on public.platform_flags
  for all using (public.auth_user_operator_active())
          with check (public.auth_user_operator_active());

insert into public.platform_flags (key, enabled, note)
values ('consumer_signup_enabled', false,
        'MRB-308. OFF until launch. When false, hook_before_user_created '
        'refuses consumer Google signups, every /api/consumer/* route 404s, '
        'and no consumer page is reachable. Flip with the backend env var '
        'CONSUMER_SIGNUP_ENABLED, never alone.')
on conflict (key) do nothing;

create or replace function public.consumer_signup_enabled()
returns boolean language sql stable security definer set search_path to 'public'
as $fn$
  select coalesce((select enabled from public.platform_flags
                   where key = 'consumer_signup_enabled'), false);
$fn$;

grant execute on function public.consumer_signup_enabled() to authenticated, anon;

-- ---------------------------------------------------------------------
-- The hook. Every existing branch is preserved verbatim; ONE branch is
-- added. Rainford's azure SSO path is byte-for-byte what it was.
-- ---------------------------------------------------------------------
create or replace function public.hook_before_user_created(event jsonb)
returns jsonb
language plpgsql
security definer
set search_path to 'public'
as $function$
DECLARE
  v_email    text := lower(nullif(trim(event->'user'->>'email'), ''));
  v_provider text := COALESCE(event->'user'->'app_metadata'->>'provider', 'email');
  v_school   uuid;
BEGIN
  -- Non-OAuth creation passes through untouched. This covers BOTH the
  -- existing public email/password signup AND the CSV importer, which uses
  -- the Admin API (provider 'email'). Gating those would deadlock onboarding.
  -- ⊕ MRB-308: it also covers parent email/password signup and the child
  -- accounts the parent creates, which are made via the Admin API.
  IF v_provider NOT IN ('azure', 'google') THEN
    RETURN '{}'::jsonb;
  END IF;

  -- From here: a brand-new OAuth user is about to be created.
  -- Pre-provisioned students/staff already exist and LINK rather than create,
  -- so they never reach this branch.

  IF v_email IS NULL THEN
    RETURN jsonb_build_object('error', jsonb_build_object(
      'http_code', 400,
      'message', 'No email address was returned by your sign-in provider. Please try again.'
    ));
  END IF;

  v_school := public.school_id_for_email_domain(v_email);

  IF v_school IS NULL THEN
    -- ⊕ MRB-308. An off-domain GOOGLE signup is how a parent joins. Admit it
    -- only while consumer signup is switched on, and only for Google:
    -- `azure` is school SSO and stays strict, because an off-domain Microsoft
    -- account reaching here means a school account that has gone astray, not
    -- a customer.
    IF v_provider = 'google' AND public.consumer_signup_enabled() THEN
      RETURN '{}'::jsonb;
    END IF;

    RETURN jsonb_build_object('error', jsonb_build_object(
      'http_code', 403,
      'message', format(
        'The email domain "@%s" is not recognised for any MrBadmusAI school. Please sign in with your school email, or ask your teacher.',
        split_part(v_email, '@', 2))
    ));
  END IF;

  -- On-domain, but no pre-existing account. Allowed ONLY if a valid pending
  -- staff invitation exists for this email; otherwise rejected (strict).
  IF EXISTS (
    SELECT 1 FROM public.school_invitations si
    WHERE lower(si.email) = v_email
      AND si.school_id = v_school
      AND si.accepted_at IS NULL
      AND si.deleted_at IS NULL
      AND si.expires_at > now()
  ) THEN
    RETURN '{}'::jsonb;
  END IF;

  -- MRB-293: seeded staff awaiting their first sign-in are admitted the same way.
  IF EXISTS (
    SELECT 1 FROM public.pending_staff ps
    WHERE ps.email = v_email::citext
      AND ps.school_id = v_school
      AND ps.claimed_at IS NULL
      AND ps.deleted_at IS NULL
  ) THEN
    RETURN '{}'::jsonb;
  END IF;

  RETURN jsonb_build_object('error', jsonb_build_object(
    'http_code', 403,
    'message', format(
      'We could not find a MrBadmusAI account for %s. Ask your teacher to add you to a class, then sign in again.',
      v_email)
  ));
END;
$function$;
