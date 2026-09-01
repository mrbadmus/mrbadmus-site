-- MRB-308 Night 1, migration 6 of 6: children, their classes, and the
-- parent's control over both.
--
-- The auth user itself is created by the backend via the Admin API. It is
-- NOT inserted here: hand-built auth.users rows are exactly how the TEST
-- fixtures ended up unable to sign in (GoTrue 500 on null token columns and
-- a missing auth.identities row). The Admin API is the only safe maker of a
-- user; this migration owns everything that happens AFTER it.

-- ---------------------------------------------------------------------
-- Ownership. One definition, used by every parent-facing function.
-- ---------------------------------------------------------------------
create or replace function public.parent_owns_child(p_parent uuid, p_child uuid)
returns boolean language sql stable security definer set search_path to 'public'
as $fn$
  select exists (
    select 1
      from public.profiles parent
      join public.schools  fam   on fam.id = parent.school_id
      join public.profiles child on child.school_id = parent.school_id
     where parent.id = p_parent
       and child.id  = p_child
       and parent.role = 'parent'
       and fam.kind = 'family'
       and fam.deleted_at is null
       and child.deleted_at is null
  );
$fn$;
grant execute on function public.parent_owns_child(uuid, uuid) to authenticated;

-- ---------------------------------------------------------------------
-- Username availability + suggestions.
-- ---------------------------------------------------------------------
-- Reuses the EXISTING validator. Recon found username already live as citext
-- NOT NULL uniquely indexed, with username_rejection_reason() enforcing
-- 3-20 chars, charset, profanity and impersonation. Nothing is reimplemented.
create or replace function public.child_username_check(candidate text)
returns jsonb language plpgsql stable security definer set search_path to 'public'
as $fn$
declare
  v_reason text;
  v_base   text;
  v_try    text;
  v_out    text[] := '{}';
  i        int := 0;
begin
  v_reason := public.username_rejection_reason(candidate);
  if v_reason is not null then
    return jsonb_build_object('ok', false, 'reason', v_reason, 'suggestions', '[]'::jsonb);
  end if;

  if public.username_available(candidate) then
    return jsonb_build_object('ok', true, 'reason', null, 'suggestions', '[]'::jsonb);
  end if;

  -- Taken. Offer alternatives, as the ruling requires. Trim the base so the
  -- suffix cannot push a 20-char name over the limit.
  v_base := left(regexp_replace(btrim(candidate), '[^A-Za-z0-9]', '', 'g'), 16);
  while array_length(v_out, 1) is distinct from 4 and i < 60 loop
    i := i + 1;
    v_try := v_base || (case when i <= 20 then i::text
                             else (10 + floor(random() * 990))::int::text end);
    if public.username_rejection_reason(v_try) is null
       and public.username_available(v_try)
       and not (v_try = any(v_out)) then
      v_out := v_out || v_try;
    end if;
  end loop;

  return jsonb_build_object(
    'ok', false,
    'reason', 'That username is taken — try another.',
    'suggestions', to_jsonb(v_out));
end $fn$;
grant execute on function public.child_username_check(text) to authenticated;

-- ---------------------------------------------------------------------
-- Attach a freshly-created auth user to the family as a child.
-- ---------------------------------------------------------------------
create or replace function public.attach_child_to_family(
  p_child_id   uuid,
  p_parent_id  uuid,
  p_first_name text,
  p_year_group int,
  p_username   text,
  p_mode       text default 'alongside_school',
  p_intensity  text default 'light',
  p_exam_board text default 'AQA',
  p_tier       text default null,
  p_pathway    text default null
)
returns jsonb
language plpgsql
security definer
set search_path to 'public'
as $fn$
declare
  v_school    uuid;
  v_year      uuid;
  v_key_stage text;
  v_tier      text;
  v_pathway   text;
  v_class     uuid;
  v_name      text;
  v_try       text;
  n           int := 1;
  v_reason    text;
begin
  select p.school_id into v_school
    from public.profiles p
    join public.schools s on s.id = p.school_id
   where p.id = p_parent_id and p.role = 'parent' and s.kind in ('family','organisation');

  if v_school is null then
    raise exception 'attach_child_to_family: % is not a parent of a consumer org', p_parent_id;
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

  -- The parent is the child's teacher, as a form tutor (subject_id NULL,
  -- which is what class_teachers_subject_required_check demands of that
  -- role). This is what makes auth_user_teaches_class() true for the parent
  -- and lights up the existing teacher-side surfaces with no new policy.
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
end $fn$;

revoke all on function public.attach_child_to_family(uuid,uuid,text,int,text,text,text,text,text,text) from public, anon, authenticated;

-- ---------------------------------------------------------------------
-- Edit a child. Parent-callable.
-- ---------------------------------------------------------------------
create or replace function public.parent_update_child(
  p_child_id   uuid,
  p_first_name text default null,
  p_year_group int  default null,
  p_mode       text default null,
  p_intensity  text default null,
  p_exam_board text default null,
  p_tier       text default null
)
returns jsonb language plpgsql security definer set search_path to 'public'
as $fn$
declare
  v_parent uuid := auth.uid();
  v_ks     text;
  v_yg     int;
begin
  if v_parent is null or not public.parent_owns_child(v_parent, p_child_id) then
    raise exception 'parent_update_child: not your child';
  end if;

  select coalesce(p_year_group, nullif(year_group,'')::int) into v_yg
    from public.profiles where id = p_child_id;

  if v_yg is not null and (v_yg < 7 or v_yg > 13) then
    raise exception 'parent_update_child: year group must be 7-13';
  end if;

  v_ks := case when v_yg between 7 and 9 then 'KS3'
               when v_yg between 10 and 11 then 'KS4'
               else 'KS5' end;

  update public.profiles
     set first_name      = coalesce(nullif(btrim(p_first_name),''), first_name),
         year_group      = coalesce(v_yg::text, year_group),
         key_stage       = coalesce(v_ks, key_stage),
         mode            = coalesce(p_mode, mode),
         intensity       = coalesce(p_intensity, intensity),
         exam_board      = coalesce(p_exam_board, exam_board),
         tier            = case when v_ks = 'KS4' then coalesce(p_tier, tier, 'higher') else null end,
         science_pathway = case when v_ks = 'KS4' then coalesce(science_pathway, 'combined') else null end,
         updated_at      = now()
   where id = p_child_id;

  perform public.write_audit_event('child.updated', 'profiles', p_child_id,
            jsonb_build_object('by', v_parent), v_parent, null);

  return jsonb_build_object('ok', true);
end $fn$;
grant execute on function public.parent_update_child(uuid,text,int,text,text,text,text) to authenticated;

-- ---------------------------------------------------------------------
-- Remove a child. SOFT, retaining attempts.
-- ---------------------------------------------------------------------
create or replace function public.parent_remove_child(p_child_id uuid)
returns jsonb language plpgsql security definer set search_path to 'public'
as $fn$
declare
  v_parent uuid := auth.uid();
  v_school uuid;
begin
  if v_parent is null or not public.parent_owns_child(v_parent, p_child_id) then
    raise exception 'parent_remove_child: not your child';
  end if;

  select school_id into v_school from public.profiles where id = p_child_id;

  -- Membership ends; the rows stay. assignment_question_attempts and
  -- assignment_submissions are DELIBERATELY untouched — the ruling is
  -- "soft, retaining attempts", so a child re-added later, or a parent
  -- querying past work, still finds the history.
  update public.class_members
     set left_at = coalesce(left_at, now()), deleted_at = coalesce(deleted_at, now())
   where student_id = p_child_id and deleted_at is null;

  update public.profiles set deleted_at = now(), updated_at = now()
   where id = p_child_id and deleted_at is null;

  update public.subscriptions
     set quantity = (select count(*) from public.profiles c
                      where c.school_id = v_school and c.role = 'student'
                        and c.deleted_at is null)
   where org_id = v_school;

  perform public.write_audit_event('child.removed', 'profiles', p_child_id,
            jsonb_build_object('by', v_parent), v_parent, v_school);

  return jsonb_build_object('ok', true);
end $fn$;
grant execute on function public.parent_remove_child(uuid) to authenticated;
