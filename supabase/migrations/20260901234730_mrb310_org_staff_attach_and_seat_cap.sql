-- MRB-310 Night 2, migration 11: a caseworker can add a pupil, and the seat
-- cap is enforced where the pupil is made.
--
-- Night 1's attach_child_to_family() admitted only a profile with
-- role = 'parent'. The ruling gives organisation staff the same controls a
-- parent has, and the E3 drive found that a council caseworker could not
-- add a pupil through the API at all. Two changes, nothing else moved:
--
--   1. The actor may be a parent of a family-kind org, OR a teacher/hod/admin
--      of an organisation-kind org. A parent in an organisation or a teacher
--      in a family are both still refused.
--   2. Organisation-kind orgs have a seat cap (set by hand from Admin). The
--      cap is enforced HERE, in the one function that makes a pupil, so no
--      route can forget it: live students >= seat_cap raises
--      'seat_cap_reached'. Families have no cap (Stripe quantity follows).

create or replace function public.attach_child_to_family(
  p_child_id uuid, p_parent_id uuid, p_first_name text, p_year_group integer, p_username text,
  p_mode text default 'alongside_school'::text, p_intensity text default 'light'::text,
  p_exam_board text default 'AQA'::text, p_tier text default null::text, p_pathway text default null::text)
returns jsonb
language plpgsql
security definer
set search_path to 'public'
as $function$
declare
  v_school    uuid;
  v_kind      text;
  v_year      uuid;
  v_key_stage text;
  v_tier      text;
  v_pathway   text;
  v_class     uuid;
  v_name      text;
  v_try       text;
  n           int := 1;
  v_reason    text;
  v_cap       int;
  v_live      int;
begin
  -- ⊕ MRB-310: a parent of a family, or staff of an organisation.
  select p.school_id, s.kind into v_school, v_kind
    from public.profiles p
    join public.schools s on s.id = p.school_id
   where p.id = p_parent_id
     and p.deleted_at is null
     and s.deleted_at is null
     and (
           (p.role = 'parent' and s.kind = 'family')
        or (p.role in ('teacher', 'hod', 'admin') and s.kind = 'organisation')
     );

  if v_school is null then
    raise exception 'attach_child_to_family: % is not a parent of a family or staff of an organisation', p_parent_id;
  end if;

  -- ⊕ MRB-310: the seat cap, enforced at the only place a pupil is made.
  if v_kind = 'organisation' then
    select sub.seat_cap into v_cap from public.subscriptions sub
     where sub.org_id = v_school and sub.deleted_at is null;
    select count(*) into v_live from public.profiles c
     where c.school_id = v_school and c.role = 'student' and c.deleted_at is null;
    if v_cap is null or v_live >= v_cap then
      raise exception 'seat_cap_reached: this organisation has % of % seats in use', v_live, coalesce(v_cap, 0)
        using errcode = 'check_violation';
    end if;
  end if;

  if p_year_group is null or p_year_group < 7 or p_year_group > 13 then
    raise exception 'attach_child_to_family: year group must be 7-13, got %', p_year_group;
  end if;

  v_reason := public.username_rejection_reason(p_username);
  if v_reason is not null then
    raise exception 'attach_child_to_family: %', v_reason;
  end if;
  if not public.username_available(p_username) then
    raise exception 'attach_child_to_family: that username is taken';
  end if;

  v_key_stage := case when p_year_group between 7 and 9 then 'KS3'
                      when p_year_group between 10 and 11 then 'KS4'
                      else 'KS5' end;

  -- ⚠️ Load-bearing. Both profiles and classes carry
  -- `(tier IS NULL AND science_pathway IS NULL) OR key_stage = 'KS4'`, and
  -- profiles.tier DEFAULTS to 'higher' with science_pathway DEFAULT
  -- 'combined'. Those defaults survive today only because key_stage is NULL
  -- and a CHECK that evaluates to NULL passes. The moment we set a real
  -- key_stage they stop being free: a KS3 child with the default tier would
  -- violate the constraint. So they are nulled explicitly off KS4.
  v_tier    := case when v_key_stage = 'KS4' then coalesce(p_tier, 'higher') else null end;
  v_pathway := case when v_key_stage = 'KS4' then coalesce(p_pathway, 'combined') else null end;

  select id into v_year from public.academic_years
   where school_id = v_school and deleted_at is null
   order by is_current desc, start_date desc nulls last limit 1;

  if v_year is null then
    raise exception 'attach_child_to_family: org % has no academic year', v_school;
  end if;

  update public.profiles
     set first_name      = coalesce(nullif(btrim(p_first_name), ''), first_name),
         username        = p_username,
         last_username_change_at = now(),
         role            = 'student',
         school_id       = v_school,
         key_stage       = v_key_stage,
         year_group      = p_year_group::text,
         tier            = v_tier,
         science_pathway = v_pathway,
         exam_board      = coalesce(p_exam_board, 'AQA'),
         mode            = p_mode,
         intensity       = p_intensity,
         created_by      = p_parent_id,
         updated_at      = now()
   where id = p_child_id;

  if not found then
    raise exception 'attach_child_to_family: no profile for child %', p_child_id;
  end if;

  -- ONE CLASS PER CHILD. Recon settled this: classes.key_stage and
  -- classes.year_group are both NOT NULL, so a shared sibling class could
  -- not state a stage or a year for siblings who differ in both. A per-child
  -- class states them truthfully and drops straight into every class-scoped
  -- surface the estate already has.
  v_name := coalesce(nullif(btrim(p_first_name), ''), p_username);
  v_try  := v_name;
  while exists (select 1 from public.classes
                 where school_id = v_school and academic_year_id = v_year and name = v_try) loop
    n := n + 1;
    v_try := v_name || ' ' || n::text;
  end loop;

  insert into public.classes
    (school_id, academic_year_id, name, key_stage, year_group, tier, science_pathway)
  values
    (v_school, v_year, v_try, v_key_stage, p_year_group::smallint, v_tier, v_pathway)
  returning id into v_class;

  insert into public.class_members (class_id, student_id, joined_via)
  values (v_class, p_child_id, 'parent_added');

  -- The parent (or caseworker) is the child's teacher, as a form tutor
  -- (subject_id NULL, which is what class_teachers_subject_required_check
  -- demands of that role). This is what makes auth_user_teaches_class()
  -- true for them and lights up the existing teacher-side surfaces with no
  -- new policy.
  insert into public.class_teachers (class_id, teacher_id, subject_id, role)
  values (v_class, p_parent_id, null, 'form_tutor');

  perform public.write_audit_event(
    p_action       => 'child.created',
    p_target_table => 'profiles',
    p_target_id    => p_child_id,
    p_payload      => jsonb_build_object('parent_id', p_parent_id, 'class_id', v_class,
                                         'username', p_username, 'year_group', p_year_group,
                                         'mode', p_mode, 'intensity', p_intensity),
    p_actor_id     => p_parent_id,
    p_school_id    => v_school);

  -- Trial quantity tracks the number of live children; Stripe reads it Night 2.
  update public.subscriptions
     set quantity = (select count(*) from public.profiles c
                      where c.school_id = v_school and c.role = 'student'
                        and c.deleted_at is null)
   where org_id = v_school;

  return jsonb_build_object('ok', true, 'child_id', p_child_id,
                            'class_id', v_class, 'class_name', v_try,
                            'key_stage', v_key_stage);
end $function$;