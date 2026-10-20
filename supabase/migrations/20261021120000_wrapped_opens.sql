-- MrBadmus Wrapped — open counts (21 Oct 2026)
--
-- One table and two functions, all additive. Counts how many people opened the
-- Wrapped story, reached its last card, and shared. Nothing here changes any
-- existing table, function or policy.
--
--   * wrapped_opens        one row per (profile, class). RLS on, NO policies,
--                          every grant revoked: nobody reads it through the API.
--   * wrapped_mark(class, event)
--                          SECURITY DEFINER, EXECUTE for authenticated only.
--                          Records for auth.uid() and nobody else (there is no
--                          profile parameter). Silent no-op when: not signed in,
--                          not a member or teacher of that class, the Wrapped
--                          gate is not 'open' (so preview opens before release
--                          never count), or the event is unknown.
--                          Events: 'open' (opens + 1), 'end', 'share'.
--   * wrapped_open_stats() read-only totals plus per-class counts; no pupil
--                          names. EXECUTE revoked from everyone but the
--                          service role (and the table owner).
--
-- Role and membership come from the same helpers wrapped_status uses
-- (auth_user_is_member_of_class, then auth_user_teaches_class); the release
-- gate is _wrapped_gate(false), i.e. wrapped_settings.release_at / close_at.

create table if not exists public.wrapped_opens (
  profile_id       uuid        not null references public.profiles (id) on delete cascade,
  class_id         uuid        not null references public.classes (id) on delete cascade,
  role             text        not null check (role in ('pupil', 'teacher')),
  first_opened_at  timestamptz not null default now(),
  last_opened_at   timestamptz not null default now(),
  opens            integer     not null default 0,
  reached_end      boolean     not null default false,
  shared           boolean     not null default false,
  primary key (profile_id, class_id)
);

alter table public.wrapped_opens enable row level security;
revoke all on table public.wrapped_opens from public, anon, authenticated;

create or replace function public.wrapped_mark(p_class_id uuid, p_event text)
returns void
language plpgsql volatile security definer set search_path = public
as $$
declare
  v_uid  uuid := auth.uid();
  v_role text;
begin
  if v_uid is null or p_class_id is null or p_event is null then return; end if;
  if p_event not in ('open', 'end', 'share') then return; end if;
  -- p_preview is false on purpose: a preview gate never counts.
  if public._wrapped_gate(false) <> 'open' then return; end if;

  if public.auth_user_is_member_of_class(p_class_id) then
    v_role := 'pupil';
  elsif public.auth_user_teaches_class(p_class_id) then
    v_role := 'teacher';
  else
    return;
  end if;

  insert into public.wrapped_opens as w (profile_id, class_id, role, opens, reached_end, shared)
  values (v_uid, p_class_id, v_role,
          case when p_event = 'open' then 1 else 0 end,
          p_event = 'end', p_event = 'share')
  on conflict (profile_id, class_id) do update
    set role           = excluded.role,
        opens          = w.opens + case when p_event = 'open' then 1 else 0 end,
        last_opened_at = case when p_event = 'open' then now() else w.last_opened_at end,
        reached_end    = w.reached_end or p_event = 'end',
        shared         = w.shared or p_event = 'share';
end;
$$;

revoke all on function public.wrapped_mark(uuid, text) from public, anon;
grant execute on function public.wrapped_mark(uuid, text) to authenticated;

create or replace function public.wrapped_open_stats()
returns jsonb
language sql stable security definer set search_path = public
as $$
  select jsonb_build_object(
    'pupils_opened',    (select count(distinct profile_id) from public.wrapped_opens where role = 'pupil' and opens > 0),
    'teachers_opened',  (select count(distinct profile_id) from public.wrapped_opens where role = 'teacher' and opens > 0),
    'reached_end',      (select count(distinct profile_id) from public.wrapped_opens where reached_end),
    'shared',           (select count(distinct profile_id) from public.wrapped_opens where shared),
    'by_class',         coalesce((
      select jsonb_agg(jsonb_build_object(
               'class_name',      c.name,
               'pupils_opened',   x.pupils,
               'teachers_opened', x.teachers,
               'reached_end',     x.ended,
               'shared',          x.shared,
               'opens',           x.opens) order by c.name)
        from (select class_id,
                     count(*) filter (where role = 'pupil' and opens > 0)   as pupils,
                     count(*) filter (where role = 'teacher' and opens > 0) as teachers,
                     count(*) filter (where reached_end)                    as ended,
                     count(*) filter (where shared)                         as shared,
                     sum(opens)::int                                        as opens
                from public.wrapped_opens group by class_id) x
        join public.classes c on c.id = x.class_id), '[]'::jsonb)
  );
$$;

revoke all on function public.wrapped_open_stats() from public, anon, authenticated;
