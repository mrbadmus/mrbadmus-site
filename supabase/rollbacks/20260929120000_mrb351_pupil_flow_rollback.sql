-- ════════════════════════════════════════════════════════════════════════
-- ROLLBACK for supabase/migrations/20260929120000_mrb351_pupil_flow.sql.
--
-- Restores flashcard_card_state and flashcard_record to the bodies deployed
-- before it — the bodies of 20260924180100_mrb351_flashcards_functions.sql
-- exactly as the database holds them (that file's comments stripped, which
-- is how they were applied): prosrc md5 3bea27bef4c40b1e95f978673b4470c5 and
-- e8c789dde208bc608aba4ad0cf77ce5b on TEST and production alike — then
-- drops the three columns. The column drops lose any review-phase answer
-- text recorded in the meantime; nothing else reads them.
-- ════════════════════════════════════════════════════════════════════════

begin;

create or replace function public.flashcard_card_state(p_assignment uuid, p_pupil uuid)
returns table (card_id uuid, pos int, made boolean, known boolean, secured boolean,
               last_rating text, not_yet_n int)
language sql stable security definer set search_path to 'public' as $$
  with a as (
    select completion_rule from public.assignments where id = p_assignment
  ),
  r as (
    select rv.card_id, rv.rating, rv.phase, rv.rated_at, s.started_at,
           coalesce(s.ended_at, s.last_seen_at) as s_end, s.id as sid
      from public.flashcard_reviews rv
      join public.flashcard_sessions s on s.id = rv.session_id
     where rv.assignment_id = p_assignment and rv.pupil_id = p_pupil
  ),
  per as (
    select af.id, af.position,
           exists (select 1 from public.flashcard_pupil_cards pc
                    where pc.assignment_id = p_assignment and pc.pupil_id = p_pupil
                      and pc.card_id = af.id) as made,
           exists (select 1 from r where r.card_id = af.id and r.rating = 'got_it') as known,
           (
             (exists (select 1 from r where r.card_id = af.id and r.rating = 'got_it' and r.phase = 'make')
              and exists (select 1 from r where r.card_id = af.id and r.rating = 'got_it' and r.phase = 'review'))
             or exists (select 1 from r r1 join r r2
                          on r2.card_id = r1.card_id and r2.sid <> r1.sid
                         and r2.started_at >= r1.s_end + interval '60 minutes'
                        where r1.card_id = af.id and r1.rating = 'got_it' and r1.phase = 'review'
                          and r2.rating = 'got_it' and r2.phase = 'review')
           ) as twice,
           (select r.rating from r where r.card_id = af.id order by r.rated_at desc limit 1) as last_rating,
           (select count(*) from r where r.card_id = af.id and r.rating = 'not_yet')::int as not_yet_n
      from public.assignment_flashcards af
     where af.assignment_id = p_assignment
  )
  select per.id, per.position, per.made, per.known,
         case when (select completion_rule from a) = 'quick' then per.known else per.twice end,
         per.last_rating, per.not_yet_n
    from per
$$;
revoke all on function public.flashcard_card_state(uuid, uuid) from public, anon, authenticated;

create or replace function public.flashcard_record(p_assignment uuid, p_events jsonb default '[]'::jsonb)
returns jsonb
language plpgsql security definer set search_path to 'public' as $$
declare
  v_uid      uuid := auth.uid();
  v_a        public.assignments;
  v_sess     public.flashcard_sessions;
  v_now      timestamptz := now();
  e          jsonb;
  v_at       timestamptz;
  v_card     uuid;
  v_new_ids  uuid[] := '{}';
  v_finish   boolean := false;
  r          record;
  v_shown    timestamptz;
  v_rev      timestamptz;
  v_n        int;
  v_state    jsonb;
  v_done     boolean;
  v_sub      public.assignment_submissions;
begin
  if v_uid is null then raise exception 'not_signed_in' using errcode = '42501'; end if;
  select * into v_a from public.assignments where id = p_assignment;
  if not found or v_a.kind <> 'flashcards' or v_a.deleted_at is not null
     or (v_a.release_at is not null and v_a.release_at > v_now)
     or not exists (select 1 from public.class_members cm
                     where cm.class_id = v_a.class_id and cm.student_id = v_uid
                       and cm.left_at is null and cm.deleted_at is null) then
    raise exception 'not_your_homework' using errcode = '42501';
  end if;
  if p_events is null or jsonb_typeof(p_events) <> 'array' then p_events := '[]'::jsonb; end if;
  if jsonb_array_length(p_events) > 500 then raise exception 'batch_too_big' using errcode = '22023'; end if;

  if jsonb_array_length(p_events) > 0 then
    select * into v_sess from public.flashcard_sessions
     where assignment_id = p_assignment and pupil_id = v_uid and ended_at is null
     order by started_at desc limit 1 for update;
    if found and v_sess.last_seen_at < v_now - interval '10 minutes' then
      update public.flashcard_sessions set ended_at = last_seen_at where id = v_sess.id;
      perform public.mrb351_session_refresh(v_sess.id);
      v_sess := null;
    end if;
    if v_sess.id is null then
      insert into public.flashcard_sessions (assignment_id, pupil_id, school_id, class_id,
                                             started_at, last_seen_at)
      values (p_assignment, v_uid, v_a.school_id, v_a.class_id, v_now, v_now)
      returning * into v_sess;
    end if;

    for e in select * from jsonb_array_elements(p_events) loop
      continue when coalesce(e->>'id', '') !~ '^[0-9a-fA-F-]{36}$';
      continue when coalesce(e->>'type', '') not in
        ('card_shown', 'answer_submitted', 'revealed', 'rated', 'session_finish', 'visibility');
      v_at := case when (e->>'at') ~ '^\d{12,14}$' then to_timestamp((e->>'at')::bigint / 1000.0)
                   else (e->>'at')::timestamptz end;
      v_at := least(coalesce(v_at, v_now), v_now + interval '2 minutes');
      v_card := null;
      if coalesce(e->>'card', '') ~ '^[0-9a-fA-F-]{36}$' then
        select id into v_card from public.assignment_flashcards
         where id = (e->>'card')::uuid and assignment_id = p_assignment;
      end if;
      insert into public.flashcard_events (id, assignment_id, pupil_id, school_id, class_id, session_id,
                                           card_id, type, client_at, server_at, visible, phase, rating)
      values ((e->>'id')::uuid, p_assignment, v_uid, v_a.school_id, v_a.class_id, v_sess.id,
              v_card, e->>'type', v_at, v_now,
              coalesce((e->>'visible')::boolean, true),
              case when e->>'phase' in ('make', 'review') then e->>'phase' end,
              case when e->>'rating' in ('got_it', 'nearly', 'not_yet') then e->>'rating' end)
      on conflict (id) do nothing;
      if found then
        v_new_ids := v_new_ids || (e->>'id')::uuid;
        if e->>'type' = 'session_finish' then v_finish := true; end if;
        if e->>'type' = 'answer_submitted' and v_card is not null and v_a.flashcard_mode = 'make' then
          select max(client_at) into v_shown from public.flashcard_events
           where session_id = v_sess.id and card_id = v_card and type = 'card_shown' and client_at <= v_at;
          insert into public.flashcard_pupil_cards (assignment_id, pupil_id, school_id, class_id, card_id,
                                                    session_id, event_id, pupil_answer, written_ms, answer_check)
          select p_assignment, v_uid, v_a.school_id, v_a.class_id, v_card, v_sess.id, (e->>'id')::uuid,
                 left(coalesce(e->>'answer', ''), 500),
                 case when v_shown is null then 0
                      else least(180000, public.mrb351_active_between(v_sess.id, v_shown, v_at)) end,
                 coalesce(public.flashcard_quick_check(e->>'answer', af.answer), 'pending')
            from public.assignment_flashcards af where af.id = v_card
          on conflict (assignment_id, pupil_id, card_id) do nothing;
        end if;
      end if;
    end loop;

    for r in select ev.* from public.flashcard_events ev
              where ev.id = any (v_new_ids) and ev.type = 'rated' and ev.card_id is not null
                and ev.rating is not null
              order by ev.client_at loop
      continue when coalesce(r.phase, 'review') = 'make' and (v_a.flashcard_mode <> 'make'
        or not exists (select 1 from public.flashcard_pupil_cards pc
                        where pc.assignment_id = p_assignment and pc.pupil_id = v_uid and pc.card_id = r.card_id));
      select max(client_at) into v_shown from public.flashcard_events
       where session_id = r.session_id and card_id = r.card_id and type = 'card_shown' and client_at <= r.client_at;
      select max(client_at) into v_rev from public.flashcard_events
       where session_id = r.session_id and card_id = r.card_id
         and type in ('revealed', 'answer_submitted') and client_at <= r.client_at
         and (v_shown is null or client_at >= v_shown);
      insert into public.flashcard_reviews (session_id, assignment_id, pupil_id, school_id, class_id, card_id,
                                            event_id, rating, phase, shown_at, revealed_at, rated_at, think_ms)
      values (r.session_id, p_assignment, v_uid, v_a.school_id, v_a.class_id, r.card_id, r.id, r.rating,
              coalesce(r.phase, 'review'), v_shown, v_rev, r.client_at,
              case when v_shown is not null and v_rev is not null
                   then least(180000, public.mrb351_active_between(r.session_id, v_shown, v_rev)) end)
      on conflict (event_id) do nothing;
    end loop;

    update public.flashcard_sessions set last_seen_at = v_now,
           ended_at = case when v_finish then v_now else ended_at end,
           finished = finished or v_finish
     where id = v_sess.id;
    perform public.mrb351_session_refresh(v_sess.id);
  end if;

  select count(*) into v_n from public.assignment_flashcards where assignment_id = p_assignment;
  select v_n > 0 and bool_and(cs.secured and (v_a.flashcard_mode <> 'make' or cs.made))
    into v_done from public.flashcard_card_state(p_assignment, v_uid) cs;

  select * into v_sub from public.assignment_submissions
   where assignment_id = p_assignment and student_id = v_uid and deleted_at is null
   order by coalesce(attempts, 2147483647), coalesce(submitted_at, 'infinity'::timestamptz), id limit 1;

  if coalesce(v_done, false) and (v_sub.id is null or v_sub.submitted_at is null) then
    if v_sub.id is null then
      insert into public.assignment_submissions (assignment_id, student_id, score, max_score,
             total_time_seconds, submitted_at, completed_at, started_at, status, is_late,
             attempts, attempt_no)
      values (p_assignment, v_uid, v_n, v_n,
              (select coalesce(sum(active_ms), 0) / 1000 from public.flashcard_sessions
                where assignment_id = p_assignment and pupil_id = v_uid),
              v_now, v_now,
              (select min(started_at) from public.flashcard_sessions
                where assignment_id = p_assignment and pupil_id = v_uid),
              'complete', (v_a.due_at is not null and v_now > v_a.due_at), 1, 1)
      on conflict (assignment_id, student_id, attempt_no) where deleted_at is null do nothing;
      select * into v_sub from public.assignment_submissions
       where assignment_id = p_assignment and student_id = v_uid and deleted_at is null
       order by coalesce(attempts, 2147483647), coalesce(submitted_at, 'infinity'::timestamptz), id limit 1;
    else
      update public.assignment_submissions set score = v_n, max_score = v_n, submitted_at = v_now,
             completed_at = v_now, status = 'complete',
             is_late = (v_a.due_at is not null and v_now > v_a.due_at), updated_at = v_now
       where id = v_sub.id returning * into v_sub;
    end if;
  end if;

  select jsonb_build_object(
    'assignment_id', v_a.id, 'title', v_a.title, 'mode', v_a.flashcard_mode,
    'rule', v_a.completion_rule, 'due_at', v_a.due_at, 'note', v_a.teacher_note,
    'n', v_n,
    'made',    (select count(*) filter (where made) from public.flashcard_card_state(p_assignment, v_uid)),
    'known',   (select count(*) filter (where known) from public.flashcard_card_state(p_assignment, v_uid)),
    'secured', (select count(*) filter (where secured) from public.flashcard_card_state(p_assignment, v_uid)),
    'complete', v_sub.submitted_at is not null,
    'completed_at', v_sub.completed_at, 'is_late', v_sub.is_late,
    'session_id', (select id from public.flashcard_sessions where assignment_id = p_assignment
                     and pupil_id = v_uid and ended_at is null order by started_at desc limit 1),
    'sittings', (select count(*) from public.flashcard_sessions where assignment_id = p_assignment and pupil_id = v_uid),
    'cards', coalesce((
      select jsonb_agg(jsonb_build_object(
               'id', af.id, 'position', af.position, 'question', af.question, 'answer', af.answer,
               'made', cs.made, 'known', cs.known, 'secured', cs.secured, 'last', cs.last_rating,
               'mine', pc.pupil_answer) order by af.position)
        from public.assignment_flashcards af
        join public.flashcard_card_state(p_assignment, v_uid) cs on cs.card_id = af.id
        left join public.flashcard_pupil_cards pc
          on pc.assignment_id = p_assignment and pc.pupil_id = v_uid and pc.card_id = af.id
       where af.assignment_id = p_assignment), '[]'::jsonb)
  ) into v_state;
  return v_state;
end $$;

alter table public.flashcard_reviews drop column if exists answer, drop column if exists answer_check;
alter table public.flashcard_events drop column if exists answer;

commit;
