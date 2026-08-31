-- MRB-306 WS-3 — the student's unread reminders, with the sender's name.
--
-- WHY AN RPC AND NOT A JOIN. A student can read ONLY their own profile row
-- ("Users can view own profile": auth.uid() = id). There is no policy that
-- lets a student read a TEACHER's profile, so selecting
-- `sent_by:profiles(display_name)` from the class page returns null — silently,
-- with no error — and the reminder would read as though nobody sent it.
--
-- This is the same problem `class_teachers_for_viewer` already solves, and it
-- is solved the same way: SECURITY DEFINER, gated on membership, returning
-- only the display name. It establishes no new exposure — a class member can
-- already see their teachers' names through that function — and it keeps the
-- student page to ONE call instead of a read plus a name lookup.
--
-- The COALESCE chain is copied from that function deliberately, so the two
-- cannot render the same teacher's name two different ways.
--
-- Applied to prod 31 Aug 2026 via MCP apply_migration after rehearsal on TEST,
-- where it was confirmed to FAIL CLOSED: a non-member and a nonexistent class
-- both return an empty list rather than an error or another student's rows.

create or replace function public.student_reminders_for_viewer(p_class_id uuid)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $fn$
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
$fn$;

revoke all on function public.student_reminders_for_viewer(uuid) from public, anon;
grant execute on function public.student_reminders_for_viewer(uuid) to authenticated;
