-- ROLLBACK for 20260908112533_mrb336_student_reminders_exclude_deleted
--
-- Apply MANUALLY only. Restores `student_reminders_for_viewer` to its
-- pre-MRB-336 definition, transcribed verbatim from `pg_get_functiondef` before
-- the migration ran.
--
-- ⚠️ RUNNING THIS RE-OPENS THE BANNER. With the join gone, the class page will
-- again advertise reminders whose assignment has been soft-deleted, whose
-- assignment has not been released yet, or whose assignment belongs to another
-- class entirely — each with a link that lands on a 404. The only thing left
-- standing between a pupil and that is the best-effort mark-read sweep in
-- `DELETE /api/teacher/set-work/:id`, which logs rather than fails, and which
-- covers only the first of the three cases. Do not run this to "simplify" the
-- function.

create or replace function public.student_reminders_for_viewer(p_class_id uuid)
returns jsonb
language plpgsql
stable security definer
set search_path to 'public'
as $function$
declare
  v_rows jsonb;
begin
  -- Only a member of the class, and only ever their OWN reminders.
  if not public.auth_user_is_member_of_class(p_class_id) then
    return jsonb_build_object('reminders', '[]'::jsonb);
  end if;

  select coalesce(
           jsonb_agg(
             jsonb_build_object(
               'id',            r.id,
               'assignment_id', r.assignment_id,
               'created_at',    r.created_at,
               'sender',        r.sender)
             order by r.created_at desc),
           '[]'::jsonb)
    into v_rows
  from (
    select sn.id, sn.assignment_id, sn.created_at,
           coalesce(
             nullif(btrim(p.display_name), ''),
             nullif(btrim(coalesce(p.first_name,'') || ' ' || coalesce(p.last_name,'')), ''),
             'Your teacher')                       as sender
      from public.student_notifications sn
      left join public.profiles p on p.id = sn.sent_by
     where sn.class_id   = p_class_id
       and sn.student_id = auth.uid()
       and sn.read_at is null
  ) r;

  return jsonb_build_object('reminders', v_rows);
end;
$function$;

-- ⚠️ RE-STATED, because CREATE OR REPLACE resets a function's privileges and a
-- rollback that opens a hole is worse than the thing it is rolling back. This
-- is SECURITY DEFINER: left at the default it would be callable by `anon`.
revoke all on function public.student_reminders_for_viewer(uuid) from public;
revoke all on function public.student_reminders_for_viewer(uuid) from anon;
grant execute on function public.student_reminders_for_viewer(uuid) to authenticated;
grant execute on function public.student_reminders_for_viewer(uuid) to service_role;

delete from supabase_migrations.schema_migrations where version = '20260908112533';
