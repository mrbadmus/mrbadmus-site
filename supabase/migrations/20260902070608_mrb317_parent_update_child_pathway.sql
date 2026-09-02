-- MRB-317 Night 3 — a parent (or organisation staff) can change a Year 10–11
-- child's ROUTE (Combined / Triple) from the settings screen. Mide's MRB-316
-- ruling added the route question to signup AND child settings; Night 1's
-- parent_update_child accepted a tier but not a pathway, so Design's Route
-- control saved 200 and changed nothing (found by the dashboard lane's drive).
-- The old seven-argument overload is dropped so PostgREST never has two
-- candidates to choose between.
drop function if exists public.parent_update_child(uuid, text, integer, text, text, text, text);

create or replace function public.parent_update_child(
  p_child_id uuid,
  p_first_name text default null,
  p_year_group integer default null,
  p_mode text default null,
  p_intensity text default null,
  p_exam_board text default null,
  p_tier text default null,
  p_pathway text default null
) returns jsonb
language plpgsql
security definer
set search_path to 'public'
as $function$
declare
  v_parent uuid := auth.uid();
  v_ks     text;
  v_yg     int;
begin
  if v_parent is null or not public.parent_owns_child(v_parent, p_child_id) then
    raise exception 'parent_update_child: not your child';
  end if;

  if p_pathway is not null and p_pathway not in ('combined', 'triple') then
    raise exception 'parent_update_child: pathway must be combined or triple';
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
         science_pathway = case when v_ks = 'KS4' then coalesce(p_pathway, science_pathway, 'combined') else null end,
         updated_at      = now()
   where id = p_child_id;

  perform public.write_audit_event('child.updated', 'profiles', p_child_id,
            jsonb_build_object('by', v_parent), v_parent, null);

  return jsonb_build_object('ok', true);
end $function$;

revoke all on function public.parent_update_child(uuid, text, integer, text, text, text, text, text) from public, anon;
grant execute on function public.parent_update_child(uuid, text, integer, text, text, text, text, text) to authenticated;
