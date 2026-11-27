-- membership_rpc_check.sql — proves the class-membership functions on TEST.
-- ONE DO block that ends by raising its own report, so every write it makes
-- is rolled back. Run on TEST only (qeppkiswvclkkwbxmlok). Fixtures: the
-- 7z/Sc9 throwaways (f326…). The report's last line must read "ALL PASS".
do $check$
declare
  admin_id   uuid := 'f3260000-0000-0000-0000-000000000002';
  teacher_id uuid := 'f3260000-0000-0000-0000-000000000001';
  pupil_a    uuid := 'f3260000-0000-0000-0000-000000000011';
  pupil_b    uuid := 'f3260000-0000-0000-0000-000000000012';
  c1 uuid := 'f3260000-0000-0000-0000-000000000101';   -- 7z/Sc9  (a, b)
  c2 uuid := 'f3260000-0000-0000-0000-000000000102';   -- 7z/Sc9b (b)
  r jsonb; n int; rep text := ''; fails int := 0; aud uuid[];
  rows_before int; rows_after int; snap text; snap2 text;
begin
  select count(*) into rows_before from class_members where student_id in (pupil_a, pupil_b);
  select string_agg(id::text || coalesce(left_at::text, '') || coalesce(deleted_at::text, ''), ',' order by id)
    into snap from class_members where student_id in (pupil_a, pupil_b);

  -- ── 1. anon: no EXECUTE at all ──
  perform set_config('request.jwt.claims', '{"role":"anon"}', true);
  set local role anon;
  begin
    perform public.move_pupil(pupil_a, c1, c2, admin_id);
    rep := rep || E'FAIL anon executed move_pupil\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   anon: no execute on move_pupil\n';
  end;
  begin
    perform public.class_membership_batch('[{"op":"remove"}]'::jsonb, admin_id, 'admin');
    rep := rep || E'FAIL anon executed batch\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   anon: no execute on batch\n';
  end;
  reset role;

  -- ── 2. pupil: refused, and naming the admin as p_actor changes nothing ──
  perform set_config('request.jwt.claims',
    json_build_object('sub', pupil_a, 'role', 'authenticated')::text, true);
  set local role authenticated;
  begin
    perform public.move_pupil(pupil_a, c1, c2, admin_id);
    rep := rep || E'FAIL pupil moved themselves\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   pupil: move refused (actor spoof ignored)\n';
  end;
  begin
    perform public._membership_join(c2, pupil_a, 'admin_added', null);
    rep := rep || E'FAIL pupil called an internal\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   pupil: internals not executable\n';
  end;
  begin
    perform 1 from public.membership_pupil_search(c1, 'Pu');
    rep := rep || E'FAIL pupil searched the school\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   pupil: search refused\n';
  end;
  if public.can_manage_class_membership(c1) then
    rep := rep || E'FAIL pupil can_manage true\n'; fails := fails + 1;
  else rep := rep || E'ok   pupil: can_manage false\n'; end if;
  select count(*) into n from public.class_past_members(c1);
  rep := rep || format(E'%s   pupil: past members hidden (%s rows)\n', case when n = 0 then 'ok' else 'FAIL' end, n);
  if n <> 0 then fails := fails + 1; end if;
  reset role;

  -- ── 3. teacher of c1: refused every write ──
  perform set_config('request.jwt.claims',
    json_build_object('sub', teacher_id, 'role', 'authenticated')::text, true);
  set local role authenticated;
  begin
    perform public.remove_pupil_from_class(c1, pupil_a, admin_id);
    rep := rep || E'FAIL teacher removed a pupil\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   teacher: remove refused\n';
  end;
  begin
    perform public.add_pupil_to_class(c2, pupil_a, null);
    rep := rep || E'FAIL teacher added a pupil\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   teacher: add refused\n';
  end;
  if public.can_manage_class_membership(c1) then
    rep := rep || E'FAIL teacher can_manage true\n'; fails := fails + 1;
  else rep := rep || E'ok   teacher: can_manage false\n'; end if;
  reset role;

  select string_agg(id::text || coalesce(left_at::text, '') || coalesce(deleted_at::text, ''), ',' order by id)
    into snap2 from class_members where student_id in (pupil_a, pupil_b);
  if snap2 is distinct from snap then
    rep := rep || E'FAIL refused calls changed class_members\n'; fails := fails + 1;
  else rep := rep || E'ok   refused calls changed nothing\n'; end if;

  -- ── 4. admin: move, history, move back, remove, batch, undo ──
  perform set_config('request.jwt.claims',
    json_build_object('sub', admin_id, 'role', 'authenticated')::text, true);
  set local role authenticated;
  if public.can_manage_class_membership(c1) then rep := rep || E'ok   admin: can_manage true\n';
  else rep := rep || E'FAIL admin can_manage false\n'; fails := fails + 1; end if;

  r := public.move_pupil(pupil_a, c1, c2, null);
  select count(*) into n from class_members where student_id = pupil_a and class_id = c2 and left_at is null and deleted_at is null;
  rep := rep || format(E'%s   admin: move a c1→c2 (%s)\n', case when n = 1 then 'ok' else 'FAIL' end, r->'results'->0->>'outcome');
  if n <> 1 then fails := fails + 1; end if;
  select count(*) into n from class_members where student_id = pupil_a and class_id = c1
     and left_at is not null and deleted_at is not null;
  rep := rep || format(E'%s   old row soft-ended, not deleted\n', case when n >= 1 then 'ok' else 'FAIL' end);
  if n < 1 then fails := fails + 1; end if;
  select count(*) into n from public.class_past_members(c1) p where p.student_id = pupil_a and p.moved_to_class_id = c2;
  rep := rep || format(E'%s   c1 history says "moved to 7z/Sc9b"\n', case when n = 1 then 'ok' else 'FAIL' end);
  if n <> 1 then fails := fails + 1; end if;

  -- move back: reuses the old c1 row, no duplicate
  select count(*) into rows_after from class_members where student_id = pupil_a and class_id = c1;
  r := public.move_pupil(pupil_a, c2, c1, null);
  select count(*) into n from class_members where student_id = pupil_a and class_id = c1;
  rep := rep || format(E'%s   move back reuses the row (%s → %s rows, outcome %s)\n',
    case when n = rows_after then 'ok' else 'FAIL' end, rows_after, n, r->'results'->0->>'to_class_id');
  if n <> rows_after then fails := fails + 1; end if;
  select count(*) into n from public.class_past_members(c1) p where p.student_id = pupil_a;
  rep := rep || format(E'%s   back in c1 → not listed as past\n', case when n = 0 then 'ok' else 'FAIL' end);
  if n <> 0 then fails := fails + 1; end if;

  -- add when already a member: no-op, no audit
  r := public.add_pupil_to_class(c1, pupil_a, null);
  rep := rep || format(E'%s   add existing member → already\n',
    case when r->'results'->0->>'outcome' = 'already' then 'ok' else 'FAIL' end);
  if r->'results'->0->>'outcome' <> 'already' then fails := fails + 1; end if;

  -- batch remove both, then undo restores both with original joined_at
  r := public.class_membership_batch(jsonb_build_array(
         jsonb_build_object('op', 'remove', 'class_id', c1, 'student_id', pupil_a),
         jsonb_build_object('op', 'remove', 'class_id', c1, 'student_id', pupil_b)), null, 'admin');
  select count(*) into n from class_members where class_id = c1 and student_id in (pupil_a, pupil_b)
     and left_at is null and deleted_at is null;
  rep := rep || format(E'%s   batch remove 2 (active left %s)\n', case when n = 0 then 'ok' else 'FAIL' end, n);
  if n <> 0 then fails := fails + 1; end if;
  select array_agg(x::text::uuid) into aud from jsonb_array_elements_text(r->'audit_ids') x;
  select count(*) into n from audit_log where id = any(aud) and action = 'class_member.remove'
     and actor_id = admin_id and payload ? 'from_class';
  rep := rep || format(E'%s   audit: %s rows, who/what/which class\n', case when n = 2 then 'ok' else 'FAIL' end, n);
  if n <> 2 then fails := fails + 1; end if;
  perform public.undo_membership_change(aud, null);
  select count(*) into n from class_members where class_id = c1 and student_id in (pupil_a, pupil_b)
     and left_at is null and deleted_at is null;
  rep := rep || format(E'%s   undo restores both (%s)\n', case when n = 2 then 'ok' else 'FAIL' end, n);
  if n <> 2 then fails := fails + 1; end if;
  begin
    perform public.undo_membership_change(aud, null);
    rep := rep || E'FAIL undo ran twice\n'; fails := fails + 1;
  exception when invalid_parameter_value then rep := rep || E'ok   second undo refused\n';
  end;

  -- batch is all-or-nothing: second op invalid → first not applied
  begin
    perform public.class_membership_batch(jsonb_build_array(
         jsonb_build_object('op', 'remove', 'class_id', c1, 'student_id', pupil_a),
         jsonb_build_object('op', 'move', 'class_id', c1, 'to_class_id', c1, 'student_id', pupil_b)), null, 'admin');
    rep := rep || E'FAIL bad batch accepted\n'; fails := fails + 1;
  exception when invalid_parameter_value then null;
  end;
  select count(*) into n from class_members where class_id = c1 and student_id = pupil_a
     and left_at is null and deleted_at is null;
  rep := rep || format(E'%s   bad batch rolled back whole\n', case when n = 1 then 'ok' else 'FAIL' end);
  if n <> 1 then fails := fails + 1; end if;

  -- a class in another school is refused
  begin
    perform public.add_pupil_to_class('6d6197fb-15eb-422a-81e5-274af1b98158', pupil_a, null);
    rep := rep || E'FAIL other school accepted\n'; fails := fails + 1;
  exception when insufficient_privilege then rep := rep || E'ok   other school refused\n';
  end;
  -- one active row per (class, pupil), always
  select count(*) into n from (select class_id, student_id from class_members
     where left_at is null and deleted_at is null group by 1, 2 having count(*) > 1) d;
  rep := rep || format(E'%s   no duplicate active rows (%s)\n', case when n = 0 then 'ok' else 'FAIL' end, n);
  if n <> 0 then fails := fails + 1; end if;
  select count(*) into n from public.membership_targets(c1);
  rep := rep || format(E'%s   targets listed (%s)\n', case when n > 0 then 'ok' else 'FAIL' end, n);
  if n = 0 then fails := fails + 1; end if;
  reset role;

  raise exception 'REPORT%', E'\n' || rep || case when fails = 0 then 'ALL PASS' else fails || ' FAILED' end;
end
$check$;
