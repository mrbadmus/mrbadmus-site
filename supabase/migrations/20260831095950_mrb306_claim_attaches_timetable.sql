-- MRB-306 WS-1 — the claim also attaches the timetable.
--
-- Identical to the MRB-293 function with ONE addition: after the class links
-- are created, timetable rows seeded against this pending_staff row are
-- re-pointed at the new profile. Same mechanism, same moment, same idempotence.
--
-- A slot the teacher somehow already holds is retired (soft-deleted) rather
-- than colliding with timetable_entries_teacher_slot_unique, so the claim can
-- neither fail nor silently duplicate a period.
--
-- Proven on TEST before prod: 3 seeded rows -> 0 pending / 3 on profile, a
-- second call returns false and leaves the count at 3, and the audit payload
-- carries timetable_entries_attached.
--
-- Applied to prod 31 Aug 2026 via MCP apply_migration. This filename's version
-- matches the version the MCP recorded in schema_migrations.

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
  v_tt        int := 0;
begin
  select u.email::citext,
         u.email_confirmed_at is not null,
         coalesce(u.raw_user_meta_data, '{}'::jsonb)
    into v_email, v_confirmed, v_meta
    from auth.users u
   where u.id = p_user_id;

  if v_email is null or not v_confirmed then
    return false;
  end if;

  select * into ps
    from public.pending_staff
   where email = v_email
     and deleted_at is null
     and claimed_at is null
   order by created_at
   limit 1;

  if not found then
    return false;
  end if;

  if not exists (select 1 from public.profiles where id = p_user_id) then
    return false;
  end if;

  v_first := nullif(btrim(coalesce(v_meta->>'given_name',  v_meta->>'first_name', '')), '');
  v_last  := nullif(btrim(coalesce(v_meta->>'family_name', v_meta->>'last_name',  '')), '');
  v_full  := nullif(btrim(coalesce(v_meta->>'full_name',   v_meta->>'name',       '')), '');

  if (v_first is null or v_last is null) and v_full is not null then
    if position(',' in v_full) > 0 then
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

  -- MRB-306. The timetable attaches here, the same way the classes just did.
  update public.timetable_entries te
     set deleted_at = now(), updated_at = now()
   where te.pending_staff_id = ps.id
     and te.deleted_at is null
     and exists (
       select 1 from public.timetable_entries ex
        where ex.teacher_id       = p_user_id
          and ex.academic_year_id = te.academic_year_id
          and ex.weekday          = te.weekday
          and ex.period           = te.period
          and coalesce(ex.week_cycle,'') = coalesce(te.week_cycle,'')
          and ex.deleted_at is null);

  update public.timetable_entries
     set teacher_id       = p_user_id,
         pending_staff_id = null,
         updated_at       = now()
   where pending_staff_id = ps.id
     and deleted_at is null;
  get diagnostics v_tt = row_count;

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
                                         'class_links_created', v_links, 'scopes_granted', v_scopes,
                                         'timetable_entries_attached', v_tt),
    p_actor_id     => p_user_id,
    p_school_id    => ps.school_id);

  return true;
end
$fn$;

revoke all on function public.claim_pending_staff(uuid) from public, anon, authenticated;
