-- TEST ONLY (qeppkiswvclkkwbxmlok). Removes everything
-- class_membership_drive_seed.sql made, plus the accounts the drive's own
-- "add by email" / CSV runs create (emails cb_*@throwaway.test only).
-- By id, never by a broad predicate.
do $teardown$
declare
  ids uuid[] := array(
    select id from auth.users
     where id::text like 'cb000000-%'
        or (email like 'cb\_%@throwaway.test' escape '\'));
  cls uuid[] := array['cb000000-0000-0000-0000-0000000000c1','cb000000-0000-0000-0000-0000000000c2']::uuid[];
begin
  delete from public.audit_log
   where actor_id = any(ids)
      or (payload->>'student_id')::text = any(ids::text[]);
  delete from public.assignment_submissions where student_id = any(ids)
      or assignment_id in (select id from public.assignments where class_id = any(cls));
  delete from public.student_notifications where student_id = any(ids) or class_id = any(cls);
  delete from public.assignments where class_id = any(cls);
  delete from public.class_members where student_id = any(ids) or class_id = any(cls);
  delete from public.class_teachers where class_id = any(cls) or teacher_id = any(ids);
  delete from public.classes where id = any(cls);
  delete from public.staff_scopes where profile_id = any(ids);
  delete from public.profiles where id = any(ids);
  delete from auth.identities where user_id = any(ids);
  delete from auth.users where id = any(ids);
end
$teardown$;
