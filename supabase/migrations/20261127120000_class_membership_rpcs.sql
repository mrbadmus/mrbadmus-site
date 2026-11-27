-- =====================================================================
-- Class membership: add, move and remove pupils (school admins).
--
-- ONE place for the rule. Pages and the roster-import edge function call
-- these functions; nothing else writes class_members for this feature.
--
--   add_pupil_to_class(class, pupil)          → join (or re-join) a class
--   remove_pupil_from_class(class, pupil)     → soft-end the membership
--   move_pupil(pupil, from_class, to_class)   → both, in one transaction
--   class_membership_batch(ops jsonb)         → many, all-or-nothing
--   undo_membership_change(audit_ids uuid[])  → reverse a change made in
--                                               the last 15 minutes
--
-- Read helpers for the screens (SECURITY DEFINER, each with its own gate):
--   can_manage_class_membership(class)       → may this caller change it
--   membership_pupil_search(class, query)     → admin search of the school
--   membership_targets(class)                 → classes a pupil can move to
--   pupil_current_classes(pupil)              → a pupil's current classes
--   class_past_members(class)                 → who left / moved, and where
--
-- THE RULES
--   * Caller must be a school admin of the class's school: a live
--     staff_scopes row with scope='school_admin' (the same predicate as
--     auth_user_has_scope), or the legacy profiles.role='admin'. Teachers,
--     HoDs, pupils and anon get `not_admin` and nothing changes.
--     HoD is deliberately NOT admitted: staff_scopes.department cannot be
--     mapped onto KS3 or combined-science classes, which carry no subject,
--     so a department scope would not be clean.
--   * Every class must belong to the caller's school AND to the school's
--     WORKING academic year (the date rule of workingAcademicYear() in
--     shared/class-entry.js: the earliest year whose end_date is on or after
--     today+30 days, else the latest year). Never `is_current`.
--   * History is never lost. Ending a membership sets left_at AND
--     deleted_at; no row is ever deleted. Re-joining a class reopens the
--     pupil's most recent row for that class, so there is never a second
--     active row (class_members_active_unique enforces it too).
--   * Every change writes ONE audit_log row per pupil per change.
--   * Called by the edge function with the service role, the caller is the
--     `p_actor` it passes (it has already authenticated the JWT). From any
--     other role, `p_actor` is ignored and the caller is auth.uid().
-- =====================================================================

-- ── who is calling ───────────────────────────────────────────────────
create or replace function public._membership_actor(p_actor uuid)
returns uuid
language sql
stable
set search_path = public, pg_temp
as $$
  select case when coalesce(auth.role(), '') = 'service_role' then p_actor
              else auth.uid() end;
$$;

create or replace function public._membership_is_admin(p_actor uuid, p_school uuid)
returns boolean
language sql
stable
security definer
set search_path = public, pg_temp
as $$
  select p_actor is not null and p_school is not null and exists (
    select 1 from public.profiles p
     where p.id = p_actor
       and p.school_id = p_school
       and p.deleted_at is null
       and (
         p.role = 'admin'
         or exists (
           select 1 from public.staff_scopes ss
            where ss.profile_id = p_actor
              and ss.scope = 'school_admin'
              and (ss.school_id is null or ss.school_id = p_school)
              and ss.started_at <= now()
              and (ss.ended_at is null or ss.ended_at > now())
              and ss.deleted_at is null)
       ));
$$;

-- ── the school's working academic year (date rule, never is_current) ──
create or replace function public.working_academic_year_id(p_school uuid)
returns uuid
language sql
stable
security definer
set search_path = public, pg_temp
as $$
  select coalesce(
    (select ay.id from public.academic_years ay
      where ay.school_id = p_school and ay.deleted_at is null
        and ay.end_date >= (current_date + 30)
      order by ay.end_date asc limit 1),
    (select ay.id from public.academic_years ay
      where ay.school_id = p_school and ay.deleted_at is null
        and ay.end_date is not null
      order by ay.end_date desc limit 1));
$$;

-- ── a class the caller may change, or an exception ──────────────────
create or replace function public._membership_class(p_actor uuid, p_class uuid)
returns public.classes
language plpgsql
stable
security definer
set search_path = public, pg_temp
as $$
declare
  c public.classes;
begin
  select * into c from public.classes where id = p_class and deleted_at is null;
  if not found then
    raise exception 'class_not_found' using errcode = 'P0002';
  end if;
  if not public._membership_is_admin(p_actor, c.school_id) then
    raise exception 'not_admin' using errcode = '42501';
  end if;
  if c.consumer_kind is not null then
    raise exception 'class_not_school' using errcode = '22023';
  end if;
  if c.academic_year_id is distinct from public.working_academic_year_id(c.school_id) then
    raise exception 'class_wrong_year' using errcode = '22023';
  end if;
  return c;
end;
$$;

create or replace function public._membership_pupil(p_school uuid, p_student uuid)
returns public.profiles
language plpgsql
stable
security definer
set search_path = public, pg_temp
as $$
declare
  p public.profiles;
begin
  select * into p from public.profiles where id = p_student;
  if not found or p.deleted_at is not null then
    raise exception 'pupil_not_found' using errcode = 'P0002';
  end if;
  if p.role is distinct from 'student' or p.school_id is distinct from p_school then
    raise exception 'pupil_not_in_school' using errcode = '22023';
  end if;
  return p;
end;
$$;

-- ── the two primitive writes ─────────────────────────────────────────
-- Join: reopen the most recent row for (class, pupil) if there is one,
-- else insert. Returns (row id, previous joined_at or null, 'added' |
-- 'rejoined' | 'already').
create or replace function public._membership_join(
  p_class uuid, p_student uuid, p_via text, p_joined_at timestamptz default null)
returns table (member_id uuid, outcome text, prev_left_at timestamptz)
language plpgsql
security definer
set search_path = public, pg_temp
as $$
#variable_conflict use_column
declare
  v_id uuid;
  v_left timestamptz;
begin
  select cm.id into v_id from public.class_members cm
   where cm.class_id = p_class and cm.student_id = p_student
     and cm.left_at is null and cm.deleted_at is null
   for update;
  if found then
    return query select v_id, 'already'::text, null::timestamptz; return;
  end if;

  select cm.id, cm.left_at into v_id, v_left from public.class_members cm
   where cm.class_id = p_class and cm.student_id = p_student
   order by coalesce(cm.left_at, cm.deleted_at, cm.joined_at) desc nulls last, cm.created_at desc
   limit 1
   for update;
  if found then
    update public.class_members
       set left_at = null, deleted_at = null,
           joined_at = coalesce(p_joined_at, now()),
           updated_at = now()
     where id = v_id;
    return query select v_id, 'rejoined'::text, v_left; return;
  end if;

  insert into public.class_members (class_id, student_id, joined_via, joined_at)
  values (p_class, p_student, p_via, coalesce(p_joined_at, now()))
  returning id into v_id;
  return query select v_id, 'added'::text, null::timestamptz;
end;
$$;

-- Leave: soft-end the active row. Returns its id and joined_at, or nothing.
create or replace function public._membership_leave(p_class uuid, p_student uuid, p_at timestamptz)
returns table (member_id uuid, joined_at timestamptz)
language sql
security definer
set search_path = public, pg_temp
as $$
  update public.class_members cm
     set left_at = p_at, deleted_at = p_at, updated_at = now()
   where cm.class_id = p_class and cm.student_id = p_student
     and cm.left_at is null and cm.deleted_at is null
  returning cm.id, cm.joined_at;
$$;

create or replace function public._membership_name(p public.profiles)
returns text language sql immutable as $$
  select nullif(btrim(coalesce(p.first_name, '') || ' ' || coalesce(p.last_name, '')), '');
$$;

-- ── one operation, already inside a transaction ──────────────────────
-- p_op: {op: add|remove|move, student_id, class_id, to_class_id}
-- (for move, class_id is the FROM class). Returns a result object.
create or replace function public._membership_apply(
  p_actor uuid, p_op jsonb, p_batch uuid, p_source text)
returns jsonb
language plpgsql
security definer
set search_path = public, pg_temp
as $$
declare
  v_op     text := lower(coalesce(p_op->>'op', ''));
  v_pupil  uuid := nullif(p_op->>'student_id', '')::uuid;
  v_from   uuid := nullif(p_op->>'class_id', '')::uuid;
  v_to     uuid := nullif(p_op->>'to_class_id', '')::uuid;
  v_via    text := coalesce(nullif(p_op->>'via', ''), 'admin_added');
  c_from   public.classes;
  c_to     public.classes;
  pp       public.profiles;
  v_now    timestamptz := now();
  j        record;
  l        record;
  v_audit  uuid;
  v_member uuid;
  v_outcome text;
  v_action text;
  v_payload jsonb;
begin
  if v_pupil is null then raise exception 'pupil_not_found' using errcode = 'P0002'; end if;
  if v_via not in ('admin_added', 'csv_import') then v_via := 'admin_added'; end if;

  if v_op = 'add' then
    c_to := public._membership_class(p_actor, v_from);
    pp := public._membership_pupil(c_to.school_id, v_pupil);
    select * into j from public._membership_join(c_to.id, v_pupil, v_via);
    v_member := j.member_id; v_outcome := j.outcome;
    if j.outcome = 'already' then
      return jsonb_build_object('op', 'add', 'student_id', v_pupil, 'class_id', c_to.id,
                                'outcome', 'already');
    end if;
    v_action := 'class_member.add';
    v_payload := jsonb_build_object(
      'student_id', v_pupil, 'student_name', public._membership_name(pp),
      'to_class', jsonb_build_object('id', c_to.id, 'name', c_to.name),
      'outcome', j.outcome, 'member_id', j.member_id);

  elsif v_op = 'remove' then
    c_from := public._membership_class(p_actor, v_from);
    pp := public._membership_pupil(c_from.school_id, v_pupil);
    select * into l from public._membership_leave(c_from.id, v_pupil, v_now);
    v_member := l.member_id; v_outcome := 'removed';
    if l.member_id is null then
      return jsonb_build_object('op', 'remove', 'student_id', v_pupil, 'class_id', c_from.id,
                                'outcome', 'not_member');
    end if;
    v_action := 'class_member.remove';
    v_payload := jsonb_build_object(
      'student_id', v_pupil, 'student_name', public._membership_name(pp),
      'from_class', jsonb_build_object('id', c_from.id, 'name', c_from.name),
      'member_id', l.member_id, 'prev_joined_at', l.joined_at, 'left_at', v_now);

  elsif v_op = 'move' then
    if v_from is null or v_to is null or v_from = v_to then
      raise exception 'move_needs_two_classes' using errcode = '22023';
    end if;
    c_from := public._membership_class(p_actor, v_from);
    c_to   := public._membership_class(p_actor, v_to);
    if c_from.school_id is distinct from c_to.school_id then
      raise exception 'classes_not_same_school' using errcode = '22023';
    end if;
    pp := public._membership_pupil(c_from.school_id, v_pupil);
    select * into l from public._membership_leave(c_from.id, v_pupil, v_now);
    if l.member_id is null then
      raise exception 'not_member' using errcode = '22023';
    end if;
    select * into j from public._membership_join(c_to.id, v_pupil, v_via);
    v_member := l.member_id; v_outcome := 'moved';
    v_action := 'class_member.move';
    v_payload := jsonb_build_object(
      'student_id', v_pupil, 'student_name', public._membership_name(pp),
      'from_class', jsonb_build_object('id', c_from.id, 'name', c_from.name),
      'to_class',   jsonb_build_object('id', c_to.id,   'name', c_to.name),
      'member_id', l.member_id, 'prev_joined_at', l.joined_at, 'left_at', v_now,
      'to_member_id', j.member_id, 'to_outcome', j.outcome);
  else
    raise exception 'unknown_op' using errcode = '22023';
  end if;

  v_payload := v_payload || jsonb_build_object('source', p_source, 'batch_id', p_batch);
  insert into public.audit_log (actor_id, school_id, action, target_table, target_id, payload)
  values (p_actor, coalesce(c_from.school_id, c_to.school_id), v_action, 'class_members',
          v_member, v_payload)
  returning id into v_audit;

  return jsonb_build_object('op', v_op, 'student_id', v_pupil,
                            'class_id', coalesce(c_from.id, c_to.id),
                            'to_class_id', c_to.id,
                            'outcome', v_outcome,
                            'audit_id', v_audit);
end;
$$;

-- ── the public writers ───────────────────────────────────────────────
create or replace function public.class_membership_batch(
  p_ops jsonb, p_actor uuid default null, p_source text default 'admin')
returns jsonb
language plpgsql
security definer
set search_path = public, pg_temp
as $$
declare
  v_actor uuid := public._membership_actor(p_actor);
  v_batch uuid := gen_random_uuid();
  v_out   jsonb := '[]'::jsonb;
  v_op    jsonb;
begin
  if v_actor is null then raise exception 'not_admin' using errcode = '42501'; end if;
  if p_ops is null or jsonb_typeof(p_ops) <> 'array' or jsonb_array_length(p_ops) = 0 then
    raise exception 'no_ops' using errcode = '22023';
  end if;
  if jsonb_array_length(p_ops) > 500 then
    raise exception 'too_many_ops' using errcode = '22023';
  end if;
  if p_source not in ('admin', 'csv', 'csv_match', 'pupil_page') then p_source := 'admin'; end if;
  for v_op in select * from jsonb_array_elements(p_ops) loop
    v_out := v_out || jsonb_build_array(public._membership_apply(v_actor, v_op, v_batch, p_source));
  end loop;
  return jsonb_build_object('ok', true, 'batch_id', v_batch, 'results', v_out,
    'audit_ids', coalesce((select jsonb_agg(r->'audit_id') from jsonb_array_elements(v_out) r
                            where r ? 'audit_id'), '[]'::jsonb));
end;
$$;

create or replace function public.add_pupil_to_class(
  p_class_id uuid, p_student_id uuid, p_actor uuid default null)
returns jsonb language sql security definer set search_path = public, pg_temp as $$
  select public.class_membership_batch(
    jsonb_build_array(jsonb_build_object('op', 'add', 'class_id', p_class_id, 'student_id', p_student_id)),
    p_actor, 'admin');
$$;

create or replace function public.remove_pupil_from_class(
  p_class_id uuid, p_student_id uuid, p_actor uuid default null)
returns jsonb language sql security definer set search_path = public, pg_temp as $$
  select public.class_membership_batch(
    jsonb_build_array(jsonb_build_object('op', 'remove', 'class_id', p_class_id, 'student_id', p_student_id)),
    p_actor, 'admin');
$$;

create or replace function public.move_pupil(
  p_student_id uuid, p_from_class_id uuid, p_to_class_id uuid, p_actor uuid default null)
returns jsonb language sql security definer set search_path = public, pg_temp as $$
  select public.class_membership_batch(
    jsonb_build_array(jsonb_build_object('op', 'move', 'class_id', p_from_class_id,
                                         'to_class_id', p_to_class_id, 'student_id', p_student_id)),
    p_actor, 'admin');
$$;

-- ── undo: reverse this caller's own changes from the last 15 minutes ──
create or replace function public.undo_membership_change(
  p_audit_ids uuid[], p_actor uuid default null)
returns jsonb
language plpgsql
security definer
set search_path = public, pg_temp
as $$
declare
  v_actor uuid := public._membership_actor(p_actor);
  a       record;
  v_pupil uuid;
  v_from  uuid;
  v_to    uuid;
  v_n     int := 0;
  v_at    timestamptz := now();
begin
  if v_actor is null then raise exception 'not_admin' using errcode = '42501'; end if;
  if p_audit_ids is null or array_length(p_audit_ids, 1) is null then
    raise exception 'no_ops' using errcode = '22023';
  end if;
  -- newest first, so a batch unwinds in reverse order
  for a in
    select al.* from public.audit_log al
     where al.id = any(p_audit_ids)
     order by al.created_at desc, al.id desc
     for update
  loop
    if a.actor_id is distinct from v_actor
       or a.action not in ('class_member.add', 'class_member.remove', 'class_member.move')
       or a.created_at < now() - interval '15 minutes'
       or exists (select 1 from public.audit_log u
                   where u.action = 'class_member.undo' and u.payload->>'undoes' = a.id::text) then
      raise exception 'undo_expired' using errcode = '22023';
    end if;
    v_pupil := (a.payload->>'student_id')::uuid;
    v_from  := nullif(a.payload#>>'{from_class,id}', '')::uuid;
    v_to    := nullif(a.payload#>>'{to_class,id}', '')::uuid;
    -- the caller must still be an admin of these classes, in the working year
    if v_from is not null then perform public._membership_class(v_actor, v_from); end if;
    if v_to   is not null then perform public._membership_class(v_actor, v_to);   end if;

    if a.action = 'class_member.add'
       or (a.action = 'class_member.move' and a.payload->>'to_outcome' is distinct from 'already') then
      perform public._membership_leave(v_to, v_pupil, v_at);
    end if;
    if a.action in ('class_member.remove', 'class_member.move') then
      perform public._membership_join(v_from, v_pupil, 'admin_added',
                                      (a.payload->>'prev_joined_at')::timestamptz);
    end if;

    insert into public.audit_log (actor_id, school_id, action, target_table, target_id, payload)
    values (v_actor, a.school_id, 'class_member.undo', 'class_members', a.target_id,
            jsonb_build_object('undoes', a.id, 'undone_action', a.action,
                               'student_id', v_pupil,
                               'student_name', a.payload->>'student_name',
                               'from_class', a.payload->'from_class',
                               'to_class', a.payload->'to_class'));
    v_n := v_n + 1;
  end loop;
  if v_n <> coalesce(array_length(p_audit_ids, 1), 0) then
    raise exception 'undo_expired' using errcode = '22023';
  end if;
  return jsonb_build_object('ok', true, 'undone', v_n);
end;
$$;

-- ── reads for the screens ────────────────────────────────────────────
create or replace function public.can_manage_class_membership(p_class_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public, pg_temp
as $$
  select exists (
    select 1 from public.classes c
     where c.id = p_class_id and c.deleted_at is null and c.consumer_kind is null
       and c.academic_year_id = public.working_academic_year_id(c.school_id)
       and public._membership_is_admin(auth.uid(), c.school_id));
$$;

-- Admin search of the school's pupils by name or admission number.
create or replace function public.membership_pupil_search(p_class_id uuid, p_query text)
returns table (student_id uuid, first_name text, last_name text, admission_no text,
               in_class boolean, classes jsonb)
language plpgsql
stable
security definer
set search_path = public, pg_temp
as $$
#variable_conflict use_column
declare
  c public.classes;
  q text := btrim(coalesce(p_query, ''));
  v_year uuid;
begin
  c := public._membership_class(auth.uid(), p_class_id);
  if length(q) < 2 then return; end if;
  v_year := c.academic_year_id;
  return query
  select p.id, p.first_name, p.last_name, p.external_student_id,
         exists (select 1 from public.class_members m
                  where m.class_id = c.id and m.student_id = p.id
                    and m.left_at is null and m.deleted_at is null),
         coalesce((select jsonb_agg(jsonb_build_object('id', k.id, 'name', k.name) order by k.name)
                     from public.class_members m join public.classes k on k.id = m.class_id
                    where m.student_id = p.id and m.left_at is null and m.deleted_at is null
                      and k.deleted_at is null and k.academic_year_id = v_year), '[]'::jsonb)
    from public.profiles p
   where p.school_id = c.school_id and p.role = 'student' and p.deleted_at is null
     and (   (coalesce(p.first_name, '') || ' ' || coalesce(p.last_name, '')) ilike '%' || q || '%'
          or (coalesce(p.last_name, '') || ' ' || coalesce(p.first_name, '')) ilike '%' || q || '%'
          or p.external_student_id ilike q || '%')
   order by p.last_name nulls last, p.first_name
   limit 20;
end;
$$;

-- Classes a pupil in p_class_id can be moved to: the school's working-year
-- classes, same year group first.
create or replace function public.membership_targets(p_class_id uuid)
returns table (class_id uuid, name text, year_group smallint, same_year boolean, pupils int)
language plpgsql
stable
security definer
set search_path = public, pg_temp
as $$
#variable_conflict use_column
declare
  c public.classes;
begin
  c := public._membership_class(auth.uid(), p_class_id);
  return query
  select k.id, k.name, k.year_group, (k.year_group = c.year_group),
         (select count(*)::int from public.class_members m
           where m.class_id = k.id and m.left_at is null and m.deleted_at is null)
    from public.classes k
   where k.school_id = c.school_id and k.academic_year_id = c.academic_year_id
     and k.deleted_at is null and k.consumer_kind is null and k.id <> c.id
   order by (k.year_group = c.year_group) desc, k.year_group, k.name;
end;
$$;

-- A pupil's CURRENT classes (working year). Visible to the school's admins
-- and SLT, and to a teacher of any of the pupil's current classes.
create or replace function public.pupil_current_classes(p_student_id uuid)
returns table (class_id uuid, name text, year_group smallint, joined_at timestamptz,
               can_manage boolean)
language plpgsql
stable
security definer
set search_path = public, pg_temp
as $$
#variable_conflict use_column
declare
  v_school uuid;
  v_year   uuid;
  v_me     uuid := auth.uid();
begin
  select p.school_id into v_school from public.profiles p
   where p.id = p_student_id and p.role = 'student' and p.deleted_at is null;
  if v_school is null or v_me is null then return; end if;
  v_year := public.working_academic_year_id(v_school);
  if not (
       public._membership_is_admin(v_me, v_school)
    or (public.auth_user_school_id() = v_school and public.auth_user_has_scope('slt'))
    or exists (select 1 from public.class_members m
                where m.student_id = p_student_id and m.left_at is null and m.deleted_at is null
                  and public.auth_user_teaches_class(m.class_id))
  ) then
    return;
  end if;
  return query
  select k.id, k.name, k.year_group, m.joined_at, public._membership_is_admin(v_me, v_school)
    from public.class_members m join public.classes k on k.id = m.class_id
   where m.student_id = p_student_id and m.left_at is null and m.deleted_at is null
     and k.deleted_at is null and k.academic_year_id = v_year
   order by k.name;
end;
$$;

-- Who has left this class, when, and where they went. For the class's own
-- teachers and the school's admins / SLT / HoDs. Only pupils NOT currently
-- back in the class are listed.
create or replace function public.class_past_members(p_class_id uuid)
returns table (student_id uuid, first_name text, last_name text,
               joined_at timestamptz, left_at timestamptz,
               moved_to_class_id uuid, moved_to_name text,
               done int, avg_pct int)
language plpgsql
stable
security definer
set search_path = public, pg_temp
as $$
#variable_conflict use_column
declare
  v_school uuid;
begin
  select c.school_id into v_school from public.classes c
   where c.id = p_class_id and c.deleted_at is null;
  if v_school is null then return; end if;
  if not (
       public.auth_user_teaches_class(p_class_id)
    or (public.auth_user_school_id() = v_school
        and (public.auth_user_has_scope('school_admin') or public.auth_user_has_scope('slt')
             or public.auth_user_has_scope('hod')))
  ) then
    return;
  end if;
  return query
  with ended as (
    select distinct on (m.student_id) m.student_id, m.joined_at, m.left_at
      from public.class_members m
     where m.class_id = p_class_id and m.left_at is not null
       and not exists (select 1 from public.class_members a
                        where a.class_id = p_class_id and a.student_id = m.student_id
                          and a.left_at is null and a.deleted_at is null)
     order by m.student_id, m.left_at desc
  ),
  moved as (
    select distinct on (e.student_id) e.student_id,
           (al.payload#>>'{to_class,id}')::uuid as to_id, al.payload#>>'{to_class,name}' as to_name
      from ended e
      join public.audit_log al
        on al.action = 'class_member.move'
       and al.payload->>'student_id' = e.student_id::text
       and al.payload#>>'{from_class,id}' = p_class_id::text
       and al.payload->>'left_at' is not null
       and abs(extract(epoch from ((al.payload->>'left_at')::timestamptz - e.left_at))) < 1
     order by e.student_id, al.created_at desc
  ),
  work as (
    select fa.student_id,
           count(*)::int as done,
           case when sum(fa.max_score) filter (where fa.max_score > 0 and a.kind is distinct from 'flashcards') > 0
                then round(100.0 * sum(fa.score) filter (where fa.max_score > 0 and a.kind is distinct from 'flashcards')
                           / sum(fa.max_score) filter (where fa.max_score > 0 and a.kind is distinct from 'flashcards'))::int
           end as avg_pct
      from (select distinct on (s.assignment_id, s.student_id) s.*
              from public.assignment_submissions s
              join ended e on e.student_id = s.student_id
             where s.deleted_at is null
               and (s.completed_at is not null or s.submitted_at is not null or s.status = 'complete')
             order by s.assignment_id, s.student_id,
                      coalesce(s.attempts, 2147483647), coalesce(s.submitted_at, 'infinity'::timestamptz), s.id) fa
      join public.assignments a on a.id = fa.assignment_id
     where a.class_id = p_class_id and a.deleted_at is null
     group by fa.student_id
  )
  select e.student_id, p.first_name, p.last_name, e.joined_at, e.left_at,
         mv.to_id, mv.to_name, coalesce(w.done, 0), w.avg_pct
    from ended e
    join public.profiles p on p.id = e.student_id
    left join moved mv on mv.student_id = e.student_id
    left join work w on w.student_id = e.student_id
   order by e.left_at desc;
end;
$$;

-- ── who may call what ────────────────────────────────────────────────
-- Internals: nobody but the owner. Public: signed-in users and the service
-- role; every one refuses a non-admin inside. Never anon.
do $$
declare f text;
begin
  foreach f in array array[
    'public._membership_actor(uuid)',
    'public._membership_is_admin(uuid, uuid)',
    'public._membership_class(uuid, uuid)',
    'public._membership_pupil(uuid, uuid)',
    'public._membership_join(uuid, uuid, text, timestamptz)',
    'public._membership_leave(uuid, uuid, timestamptz)',
    'public._membership_name(public.profiles)',
    'public._membership_apply(uuid, jsonb, uuid, text)',
    'public.working_academic_year_id(uuid)'
  ] loop
    execute format('revoke all on function %s from public, anon, authenticated', f);
    execute format('grant execute on function %s to service_role', f);
  end loop;
  foreach f in array array[
    'public.class_membership_batch(jsonb, uuid, text)',
    'public.add_pupil_to_class(uuid, uuid, uuid)',
    'public.remove_pupil_from_class(uuid, uuid, uuid)',
    'public.move_pupil(uuid, uuid, uuid, uuid)',
    'public.undo_membership_change(uuid[], uuid)',
    'public.can_manage_class_membership(uuid)',
    'public.membership_pupil_search(uuid, text)',
    'public.membership_targets(uuid)',
    'public.pupil_current_classes(uuid)',
    'public.class_past_members(uuid)'
  ] loop
    execute format('revoke all on function %s from public, anon', f);
    execute format('grant execute on function %s to authenticated, service_role', f);
  end loop;
end $$;
