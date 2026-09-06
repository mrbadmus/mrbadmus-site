-- MRB-306 — `replace_timetable` RPC and its ownership check.
--
-- ⊕ RECOVERED INTO THE REPO UNDER MRB-326, 6 Sep 2026. This migration was
-- applied to BOTH projects on 31 Aug 2026 (schema_migrations version
-- 20260831144809, name mrb306_replace_timetable) but no file for it was ever
-- committed — `shared/teacher-data.js` called an RPC that git could not show
-- you. The bodies below are `pg_get_functiondef()` from production, byte for
-- byte, and the grants are production's `proacl`. Nothing here is new; a
-- `db push` against either project will see the version already registered
-- and skip it. The file exists so the repo describes the database it runs on.
--
-- What the RPC does (and the MRB-326 finding that depends on it): it retires
-- the caller's live rows for the year and inserts the supplied grid in ONE
-- transaction. It re-asserts `auth_user_teaches_class` for every class, so it
-- cannot write a class the caller does not teach — but it writes exactly the
-- grid it is given, which is why a grid drawn from a mis-scoped read (MRB-326
-- Job 1) became 24 corrupted `manual` rows under the caller's own teacher_id.

CREATE OR REPLACE FUNCTION public.auth_user_teaches_class(p_class_id uuid)
 RETURNS boolean
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  SELECT EXISTS (
    SELECT 1 FROM public.class_teachers
    WHERE class_id = p_class_id
      AND teacher_id = auth.uid()
      AND ended_at IS NULL
      AND deleted_at IS NULL
  );
$function$;

CREATE OR REPLACE FUNCTION public.replace_timetable(p_entries jsonb, p_source text DEFAULT 'manual'::text)
 RETURNS integer
 LANGUAGE plpgsql
 SET search_path TO 'public'
AS $function$
declare
  v_uid    uuid := auth.uid();
  v_year   uuid;
  v_school uuid;
  v_n      int := 0;
  r        record;
begin
  if v_uid is null then
    raise exception 'not authenticated' using errcode = '28000';
  end if;
  if p_source is null or p_source not in ('upload', 'manual') then
    raise exception 'source must be upload or manual' using errcode = '22023';
  end if;
  if jsonb_typeof(p_entries) <> 'array' then
    raise exception 'entries must be a json array' using errcode = '22023';
  end if;

  -- Every class must be one this teacher actually teaches, and they must all
  -- sit in ONE academic year — a timetable that straddled two years would
  -- make "this week" meaningless.
  for r in
    select (e->>'class_id')::uuid as class_id,
           (e->>'weekday')::smallint as weekday,
           (e->>'period')::smallint  as period
      from jsonb_array_elements(p_entries) e
  loop
    if not public.auth_user_teaches_class(r.class_id) then
      raise exception 'not your class: %', r.class_id using errcode = '42501';
    end if;
    if r.weekday is null or r.weekday < 1 or r.weekday > 5 then
      raise exception 'weekday out of range: %', r.weekday using errcode = '22023';
    end if;
    if r.period is null or r.period < 1 or r.period > 20 then
      raise exception 'period out of range: %', r.period using errcode = '22023';
    end if;

    select c.academic_year_id, c.school_id into v_year, v_school
      from public.classes c where c.id = r.class_id;
  end loop;

  -- Retire this teacher's live rows FIRST, so the per-teacher slot uniqueness
  -- cannot collide with the rows about to be written. Scoped to the year the
  -- new entries belong to; a teacher's other years are left alone.
  if v_year is not null then
    update public.timetable_entries
       set deleted_at = now(), updated_at = now()
     where teacher_id = v_uid
       and academic_year_id = v_year
       and deleted_at is null;
  end if;

  -- An EMPTY array is a legitimate payload: it means "I have no timetable",
  -- and clearing one must be possible. It retires the old rows and inserts
  -- nothing, which is why the delete above is not conditional on there being
  -- replacements.
  insert into public.timetable_entries
    (school_id, academic_year_id, class_id, teacher_id, weekday, period, source)
  select v_school, v_year, (e->>'class_id')::uuid, v_uid,
         (e->>'weekday')::smallint, (e->>'period')::smallint, p_source
    from jsonb_array_elements(p_entries) e;
  get diagnostics v_n = row_count;

  return v_n;
end;
$function$;

-- Production's grants, verbatim: the RPC is callable by signed-in users and
-- the service role only; the ownership check is callable by every role
-- because RLS policies evaluate it.
revoke all on function public.replace_timetable(jsonb, text) from public;
grant execute on function public.replace_timetable(jsonb, text) to authenticated, service_role;
grant execute on function public.auth_user_teaches_class(uuid) to anon, authenticated, service_role;
