-- MRB-336 — the class-page BANNER stops advertising work that is gone.
--
-- ⚠️ THIS FUNCTION IS SECURITY DEFINER, SO RLS DOES NOT APPLY TO IT. That is
-- the whole reason it needs changing. `assignments_student_read` was narrowed
-- at 20260908065322 so a soft-deleted assignment is invisible to a pupil at the
-- database — but this function reads `student_notifications` alone, joins
-- `assignments` nowhere, and runs as its owner. The narrowed policy never had a
-- chance to fire, so the banner went on saying "your teacher reminded you about
-- X" for work a teacher had deleted, with a link that lands on a 404.
--
-- Its only protection until now was the mark-read sweep in
-- `DELETE /api/teacher/set-work/:id`, which is explicitly best-effort: it logs
-- and carries on rather than failing the delete, because a stale bell is not
-- worth refusing a teacher's correction over. That is the right call for that
-- route, and it is exactly why it cannot be the only guard. **Both stay.** Two
-- guards, neither sufficient alone, is the same shape already agreed for
-- `deleted_at` on the read side.
--
-- THREE CONDITIONS ARE ADDED, and they are the three the BELL already applies
-- in `GET /api/student/notifications`. The banner and the bell are fed by
-- different code and must not disagree about which reminders are real:
--
--   1. `a.deleted_at is null` — the finding. Deleted work is gone from both.
--
--   2. `a.release_at is null or a.release_at <= now()` — the release gate. A
--      teacher can plant a reminder against work set for LATER; the banner
--      would announce it and the link would 404, because `studentAssignment`
--      refuses an unreleased row. A pupil must not learn that work exists
--      before it is released.
--
--   3. `a.class_id = sn.class_id` — the reminder's assignment must belong to
--      the reminder's class. ⚠️ `student_notifications_teacher_send` is
--      WITH CHECK (sent_by = auth.uid() AND auth_user_teaches_class(class_id)):
--      it constrains the CLASS and says NOTHING about `assignment_id`, so a
--      teacher may write a reminder naming a class they teach that carries any
--      assignment uuid on the estate — another class's, another school's. This
--      is the same hole that was closed on the bell's title read; closing it
--      here too is what keeps the two surfaces telling one story.
--
-- ⚠️ AN `inner join` AND NOT A `left join`. A reminder whose assignment cannot
-- be resolved at all — a dangling id — produces NO ROW, rather than a banner
-- entry with a null link. No assignment means no reminder, never a reminder
-- pointing at nothing.
--
-- Everything else is byte-identical to the previous definition: the membership
-- guard, the `student_id = auth.uid()` filter, the unread filter, the sender
-- fallback chain and the returned shape. A caller cannot tell this version from
-- the last one except by the rows it declines to return.
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
      join public.assignments a
        on a.id = sn.assignment_id
       and a.deleted_at is null
       and a.class_id = sn.class_id
       and (a.release_at is null or a.release_at <= now())
      left join public.profiles p on p.id = sn.sent_by
     where sn.class_id   = p_class_id
       and sn.student_id = auth.uid()
       and sn.read_at is null
  ) r;

  return jsonb_build_object('reminders', v_rows);
end;
$function$;

-- ⚠️ CREATE OR REPLACE RESETS A FUNCTION'S PRIVILEGES TO THE DEFAULT, so the
-- original grants are re-stated. Omitting them would leave this SECURITY
-- DEFINER function callable by `anon` — an unauthenticated caller reaching a
-- function that runs as its owner. `auth.uid()` would be NULL and it would
-- return nothing, but a hole that happens to be empty is still a hole.
revoke all on function public.student_reminders_for_viewer(uuid) from public;
revoke all on function public.student_reminders_for_viewer(uuid) from anon;
grant execute on function public.student_reminders_for_viewer(uuid) to authenticated;
grant execute on function public.student_reminders_for_viewer(uuid) to service_role;
