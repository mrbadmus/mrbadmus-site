-- ════════════════════════════════════════════════════════════════════════
-- Prompt Y2 — once secured, stays secured (Mide, 4 Oct 2026): "Once secured,
-- stays secured. It also helps with students not losing motivation."
--
-- A card that was ever rated got_it stays secured: a later lower rating —
-- ‹ Back onto it, a redo, a Revise pass after Done, a second tab — is kept
-- in flashcard_reviews (the teacher's "Later tries") but never takes it back.
-- MRB-354 counted only the LATEST rating per card per sitting per phase, so
-- ‹ Back and a wrong answer in the same sitting un-secured the card.
--
-- BASES — production's CURRENT bodies, read 4 Oct 2026 (prosrc md5):
--   flashcard_card_state  eb50f6a2648e23a26af93ab3691ddc65  ->  ec4834b787ec5c7e4b3408c9876457bb
--   flashcard_record      9f9106282729fcd97c8975983a880cb0  ->  118ade9a51a976365626b3aa67e91e56
-- Each carried forward byte for byte except one filter:
--   1 · flashcard_card_state.known reads ANY got_it of the card from
--       flashcard_reviews (was: any got_it among the latest-per-group rows).
--       `secured` is `known` (MRB-354), so both follow; `last_rating` and
--       `not_yet_n` are unchanged.
--   2 · flashcard_record's finish walk takes every got_it row, so a card's
--       secured moment is its FIRST got_it (was: groups' latest only).
-- Not changed, and why: flashcard_pupil_detail and flashcard_progress read
-- flashcard_card_state, so they follow; flashcard_store_verdict writes
-- verdicts, never ratings. The site (shared/flashcard-homework.js
-- securedInfo/securedMap) already uses this rule.
-- One transaction, two CREATE OR REPLACE, the same revoke MRB-354 carried,
-- no DROP, no data writes. Rollback: supabase/rollbacks/20261004180000_y2_secured_stays_secured_rollback.sql
-- ════════════════════════════════════════════════════════════════════════

begin;

create or replace function public.flashcard_card_state(p_assignment uuid, p_pupil uuid)
returns table (card_id uuid, pos int, made boolean, known boolean, secured boolean,
               last_rating text, not_yet_n int)
language sql stable security definer set search_path to 'public' as $$
  with a as (
    select completion_rule from public.assignments where id = p_assignment
  ),
  -- ⊕ MRB-351 pupil flow: a pupil may go ‹ Back and re-rate a card in the
  -- same sitting. Only the LATEST rating per card per sitting per phase
  -- counts here, for last_rating and not_yet_n (⊕ Y2: no longer for known —
  -- see below; a secured card stays secured). Per PHASE, not just per sitting: make mode's writing
  -- pass and its review pass share one sitting, and the make-phase Got it
  -- must survive the review pass that follows it.
  r as (
    select x.card_id, x.rating, x.phase, x.rated_at, x.started_at, x.s_end, x.sid
      from (
        select rv.card_id, rv.rating, rv.phase, rv.rated_at, s.started_at,
               coalesce(s.ended_at, s.last_seen_at) as s_end, s.id as sid,
               row_number() over (partition by rv.card_id, rv.session_id, rv.phase
                                  order by rv.rated_at desc, rv.id desc) as rn
          from public.flashcard_reviews rv
          join public.flashcard_sessions s on s.id = rv.session_id
         where rv.assignment_id = p_assignment and rv.pupil_id = p_pupil
      ) x
     where x.rn = 1
  ),
  per as (
    select af.id, af.position,
           exists (select 1 from public.flashcard_pupil_cards pc
                    where pc.assignment_id = p_assignment and pc.pupil_id = p_pupil
                      and pc.card_id = af.id) as made,
           -- ⊕ Y2 (Mide, 4 Oct 2026): "once secured, stays secured". ANY got_it
           -- this pupil ever gave the card, in any sitting or phase — read
           -- from flashcard_reviews itself, not from `r` (the latest rating per
           -- card per sitting per phase), so a later lower rating in the SAME
           -- sitting (‹ Back, a redo, a second tab) no longer takes it back.
           exists (select 1 from public.flashcard_reviews rv
                    where rv.assignment_id = p_assignment and rv.pupil_id = p_pupil
                      and rv.card_id = af.id and rv.rating = 'got_it') as known,
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
  -- ⊕ MRB-354: secured is now ONE rule — any got_it ever, any phase, any
  -- sitting (Mide, 2 Oct 2026). completion_rule's quick/secure split and
  -- `twice` (make+review, or two review sittings an hour apart) no longer
  -- decide it; `twice` is left computed above, unused, rather than removed.
  select per.id, per.position, per.made, per.known,
         per.known,
         per.last_rating, per.not_yet_n
    from per
  -- /⊕ MRB-354
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
  v_ans      text;
  -- ⊕ MRB-354: secured, one rule (Mide, 2 Oct 2026).
  v_finish_at    timestamptz;
  v_finish_event uuid;
  v_finish_server timestamptz;
  -- /⊕ MRB-354
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
    -- THE SITTING. The open one, unless it has been silent for ten minutes.
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
      -- A device clock running ahead is clamped to the server's "now".
      v_at := least(coalesce(v_at, v_now), v_now + interval '2 minutes');
      v_card := null;
      if coalesce(e->>'card', '') ~ '^[0-9a-fA-F-]{36}$' then
        select id into v_card from public.assignment_flashcards
         where id = (e->>'card')::uuid and assignment_id = p_assignment;
      end if;
      -- ⊕ MRB-351 pupil flow: a REVIEW-phase answer's text is kept on its
      -- own event, because the rating it belongs to may arrive in a later
      -- batch (the page sends the answer ahead of a model check).
      insert into public.flashcard_events (id, assignment_id, pupil_id, school_id, class_id, session_id,
                                           card_id, type, client_at, server_at, visible, phase, rating, answer)
      values ((e->>'id')::uuid, p_assignment, v_uid, v_a.school_id, v_a.class_id, v_sess.id,
              v_card, e->>'type', v_at, v_now,
              coalesce((e->>'visible')::boolean, true),
              case when e->>'phase' in ('make', 'review') then e->>'phase' end,
              case when e->>'rating' in ('got_it', 'nearly', 'not_yet') then e->>'rating' end,
              case when e->>'type' = 'answer_submitted' and e->>'phase' = 'review' and v_card is not null
                   then left(e->>'answer', 500) end)
      on conflict (id) do nothing;
      if found then
        v_new_ids := v_new_ids || (e->>'id')::uuid;
        if e->>'type' = 'session_finish' then v_finish := true; end if;
        -- the pupil's written answer rides on its own event; kept aside here
        -- because events carry no free text.
        if e->>'type' = 'answer_submitted' and v_card is not null and v_a.flashcard_mode = 'make' then
          select max(client_at) into v_shown from public.flashcard_events
           where session_id = v_sess.id and card_id = v_card and type = 'card_shown' and client_at <= v_at;
          insert into public.flashcard_pupil_cards (assignment_id, pupil_id, school_id, class_id, card_id,
                                                    session_id, event_id, pupil_answer, written_ms, answer_check)
          select p_assignment, v_uid, v_a.school_id, v_a.class_id, v_card, v_sess.id, (e->>'id')::uuid,
                 left(coalesce(e->>'answer', ''), 500),
                 case when v_shown is null then 0
                      else least(180000, public.mrb351_active_between(v_sess.id, v_shown, v_at)) end,
                 coalesce(public.flashcard_quick_check(e->>'answer', af.answer),
                          -- ⊕ MRB-353 verdict: the verdict the pupil was shown for this exact text
                          (select fv.verdict from public.flashcard_answer_verdicts fv
                            where fv.assignment_id = p_assignment and fv.pupil_id = v_uid
                              and fv.card_id = v_card and fv.answer = left(coalesce(e->>'answer', ''), 500)),
                          -- /⊕ MRB-353 verdict
                          'pending')
            from public.assignment_flashcards af where af.id = v_card
          on conflict (assignment_id, pupil_id, card_id) do nothing;   -- IMMUTABLE once written
        end if;
      end if;
    end loop;

    -- Ratings are processed after the whole batch is in, so a rating's
    -- `shown`/`revealed` partners that arrived in the same batch are seen.
    for r in select ev.* from public.flashcard_events ev
              where ev.id = any (v_new_ids) and ev.type = 'rated' and ev.card_id is not null
                and ev.rating is not null
              order by ev.client_at loop
      -- A make-phase rating only exists once the answer does.
      continue when coalesce(r.phase, 'review') = 'make' and (v_a.flashcard_mode <> 'make'
        or not exists (select 1 from public.flashcard_pupil_cards pc
                        where pc.assignment_id = p_assignment and pc.pupil_id = v_uid and pc.card_id = r.card_id));
      select max(client_at) into v_shown from public.flashcard_events
       where session_id = r.session_id and card_id = r.card_id and type = 'card_shown' and client_at <= r.client_at;
      select max(client_at) into v_rev from public.flashcard_events
       where session_id = r.session_id and card_id = r.card_id
         and type in ('revealed', 'answer_submitted') and client_at <= r.client_at
         and (v_shown is null or client_at >= v_shown);
      -- ⊕ MRB-351 pupil flow: a review rating carries the answer the pupil
      -- typed for it — the latest answer_submitted for the card since it was
      -- shown in this sitting — and the same no-model check make mode uses.
      v_ans := null;
      if coalesce(r.phase, 'review') = 'review' then
        select ev.answer into v_ans from public.flashcard_events ev
         where ev.session_id = r.session_id and ev.card_id = r.card_id and ev.type = 'answer_submitted'
           and ev.client_at <= r.client_at and (v_shown is null or ev.client_at >= v_shown)
         order by ev.client_at desc, ev.server_at desc limit 1;
      end if;
      insert into public.flashcard_reviews (session_id, assignment_id, pupil_id, school_id, class_id, card_id,
                                            event_id, rating, phase, shown_at, revealed_at, rated_at, think_ms,
                                            answer, answer_check)
      values (r.session_id, p_assignment, v_uid, v_a.school_id, v_a.class_id, r.card_id, r.id, r.rating,
              coalesce(r.phase, 'review'), v_shown, v_rev, r.client_at,
              case when v_shown is not null and v_rev is not null
                   then least(180000, public.mrb351_active_between(r.session_id, v_shown, v_rev)) end,
              v_ans,
              case when v_ans is not null then coalesce(public.flashcard_quick_check(v_ans,
                     (select af.answer from public.assignment_flashcards af where af.id = r.card_id)),
                     -- ⊕ MRB-353 verdict: the verdict the pupil was shown for this exact text
                     (select fv.verdict from public.flashcard_answer_verdicts fv
                       where fv.assignment_id = p_assignment and fv.pupil_id = v_uid
                         and fv.card_id = r.card_id and fv.answer = v_ans),
                     -- /⊕ MRB-353 verdict
                     'pending') end)
      on conflict (event_id) do nothing;
    end loop;

    update public.flashcard_sessions set last_seen_at = v_now,
           ended_at = case when v_finish then v_now else ended_at end,
           finished = finished or v_finish
     where id = v_sess.id;
    perform public.mrb351_session_refresh(v_sess.id);
  end if;

  -- ── completion ──────────────────────────────────────────────────────
  select count(*) into v_n from public.assignment_flashcards where assignment_id = p_assignment;
  -- ⊕ MRB-354: secured, one rule (Mide, 2 Oct 2026 — "a student who saw a
  -- question and answered it directly probably has that knowledge secured
  -- already"). done = every card in the deck secured by flashcard_card_state,
  -- which now flags secured from ANY got_it, any phase, any sitting; the
  -- completion_rule choice, the make+review pairing and the hour-gap rule no
  -- longer gate it. finish = the moment the LAST card became secured: per
  -- card, the earliest rated_at among its counting got_it rows (the same
  -- latest-rating-per-card-per-sitting-per-phase rows flashcard_card_state's
  -- own `r` CTE counts, reproduced here against flashcard_reviews directly);
  -- finish is the MAX of those per-card moments over the deck.
  select v_n > 0 and bool_and(cs.secured) into v_done
    from public.flashcard_card_state(p_assignment, v_uid) cs;
  if v_done then
    with cr as (
      select x.card_id, x.event_id, x.rated_at
        from (
          select rv.card_id, rv.event_id, rv.rating, rv.rated_at,
                 row_number() over (partition by rv.card_id, rv.session_id, rv.phase
                                    order by rv.rated_at desc, rv.id desc) as rn
            from public.flashcard_reviews rv
           where rv.assignment_id = p_assignment and rv.pupil_id = v_uid
        ) x
       -- ⊕ Y2 (Mide, 4 Oct 2026): every got_it counts, not only a group's
       -- latest — once secured, stays secured, so a card's moment is the
       -- FIRST time it was ever rated got_it.
       where x.rating = 'got_it'
    ),
    pc as (
      select card_id, min(rated_at) as secured_at from cr group by card_id
    )
    select cr.event_id, pc.secured_at into v_finish_event, v_finish_at
      from pc join cr on cr.card_id = pc.card_id and cr.rated_at = pc.secured_at
     order by pc.secured_at desc, cr.event_id desc limit 1;
    -- the SERVER time of the finishing rating, never the device clock and
    -- never this call's now() (re-deriving later must stamp the same instant).
    select ev.server_at into v_finish_server from public.flashcard_events ev where ev.id = v_finish_event;
    v_finish_server := coalesce(v_finish_server, least(v_finish_at, v_now));
  end if;
  -- /⊕ MRB-354

  select * into v_sub from public.assignment_submissions
   where assignment_id = p_assignment and student_id = v_uid and deleted_at is null
   order by coalesce(attempts, 2147483647), coalesce(submitted_at, 'infinity'::timestamptz), id limit 1;

  if coalesce(v_done, false) and (v_sub.id is null or v_sub.submitted_at is null) then
    -- The existing submission record, exactly as an MCQ completion writes
    -- one: score = cards secured / total, which is N/N here; on time or late
    -- by the deadline; visible to the teacher at once (23 Sep ruling).
    if v_sub.id is null then
      insert into public.assignment_submissions (assignment_id, student_id, score, max_score,
             total_time_seconds, submitted_at, completed_at, started_at, status, is_late,
             attempts, attempt_no)
      values (p_assignment, v_uid, v_n, v_n,
              (select coalesce(sum(active_ms), 0) / 1000 from public.flashcard_sessions
                where assignment_id = p_assignment and pupil_id = v_uid),
              v_finish_server, v_finish_server,
              (select min(started_at) from public.flashcard_sessions
                where assignment_id = p_assignment and pupil_id = v_uid),
              'complete', (v_a.due_at is not null and v_finish_server > v_a.due_at), 1, 1)
      on conflict (assignment_id, student_id, attempt_no) where deleted_at is null do nothing;
      select * into v_sub from public.assignment_submissions
       where assignment_id = p_assignment and student_id = v_uid and deleted_at is null
       order by coalesce(attempts, 2147483647), coalesce(submitted_at, 'infinity'::timestamptz), id limit 1;
    else
      update public.assignment_submissions set score = v_n, max_score = v_n, submitted_at = v_finish_server,
             completed_at = v_finish_server, status = 'complete',
             is_late = (v_a.due_at is not null and v_finish_server > v_a.due_at), updated_at = v_now
       where id = v_sub.id returning * into v_sub;
    end if;
  end if;

  -- ── the state the pupil's page draws from ───────────────────────────
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

commit;
