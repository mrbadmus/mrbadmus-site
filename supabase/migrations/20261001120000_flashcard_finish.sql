-- MRB-flashcard-completion — "finished the homework" is done (Mide's
-- ruling, 1 Oct 2026; docs/experience/DESIGN-PORT-REPORT.md "Follow-up 1
-- Oct"). DONE = the pupil has reached the flashcard engine's own Done
-- screen once (a review pass where every card's LATEST rating is Got it;
-- in make mode, the writing pass first). SECURED stays separate and
-- smaller, and is never required for DONE any more.
--
-- Supersedes `flashcard_record`'s completion block from
-- `20260924180100_mrb351_flashcards_functions.sql`, which required every
-- card SECURED (two review sittings 60+ minutes apart, or a make Got it
-- plus a review Got it) before writing the submission. That is a real gap
-- between "the pupil thinks they are done" (the Done screen) and "the
-- teacher sees them in" — the live defect Mide found on 1 Oct 2026.
--
-- This is a PARKED migration (branch feat/fc-complete-migrations). It has
-- been rehearsed on TEST (qeppkiswvclkkwbxmlok) ONLY — apply → rollback →
-- apply — and is NOT applied to production (urklkrwevjtlfbwnipjn) by this
-- session. It is additive-and-safe in the sense MRB-322's postmortem
-- means by that phrase (new RLS is not involved; it only widens WHEN an
-- existing, already-RLS-safe write happens), but the standing rule still
-- applies: ship only at merge time or on Mide's explicit say.
--
-- ⚠️ ONCE APPLIED, THE CLIENT WRITE IN `shared/student-live.js`
-- (`recordFinish` / the heal in `wireLibrary`) BECOMES A NO-OP THAT FINDS
-- THE ROW ALREADY THERE. No feature detection is needed on either side:
-- both write the identical shape, and the row-exists-with-submitted_at
-- guard in both places means whichever gets there first wins and the
-- other does nothing. The client write is NOT removed by this migration —
-- it is what carries the fix on a database that does not have this
-- migration (production, today), and it is what makes TEST's own
-- `tools/flashcards_complete_live.py` prove the SAME behaviour whether or
-- not this migration is applied there.
--
-- THE WALK, IN SQL. A port of `finishedAt()` / `walkReview()` in
-- `shared/flashcard-homework.js` (1 Oct 2026, corrected 1 Oct 2026 after
-- review) — NOT the bare "every card's latest rating is Got it" version
-- that function started as. That version disagreed with `reconstruct()`
-- (what pass the pupil is actually in): a pupil who leaves a leftovers
-- round stale for over an hour gets a FRESH pass from the engine (it
-- re-asks the whole deck), and getting just the one weak card right FIRST
-- in that new pass is not the Done screen, however old Got-it ratings from
-- the abandoned round still read. So this walk is ROUND-AWARE, exactly as
-- `walkReview` is: it tracks which cards still TARGET this round
-- (`v_targets`), resets to a fresh pass when a completed-but-not-all-right
-- round goes 60+ minutes without a further rating (`v_last_at`), and
-- otherwise narrows to the leftovers and advances the round number. The
-- "I don't know" replay branch `walkReview` has is NOT ported: it needs a
-- DEVICE'S OWN localStorage record that has no server-side equivalent, and
-- `finishedAt`'s real callers (this function; `student-live.js`'s
-- `recordFinish`/heal) never have one either — an IDK replay is read here
-- as an ordinary rating, exactly as those callers read it.
--
-- `jsonb` stands in for the engine's plain JS objects (`v_latest`/
-- `v_made`/`v_done`), because plpgsql has no local hash map. The first
-- `review` row at which EVERY card in the CURRENT round's targets is
-- Got it — and, in make mode, every card already has a make-phase row —
-- is the finish; once found the loop exits (this function has no use for
-- the walk's state AFTER that point, unlike `reconstruct`, which keeps
-- walking to answer "what pass is the pupil in now").
-- `v_finish_server` resolves to `flashcard_events.server_at` exactly as
-- the client write does, for the same reason: `rated_at` is `client_at`
-- (the device's clock), and only the server's own clock may stamp
-- completion (the rule `20260821115148_assignment_submissions_progress_
-- constraints.sql` already holds the platform to).

create or replace function public.flashcard_record(p_assignment uuid, p_events jsonb default '[]'::jsonb)
returns jsonb
language plpgsql security definer set search_path to 'public' as $$
declare
  v_uid          uuid := auth.uid();
  v_a            public.assignments;
  v_sess         public.flashcard_sessions;
  v_now          timestamptz := now();
  e              jsonb;
  v_at           timestamptz;
  v_card         uuid;
  v_new_ids      uuid[] := '{}';
  v_finish       boolean := false;
  r              record;
  v_shown        timestamptz;
  v_rev          timestamptz;
  v_n            int;
  v_state        jsonb;
  v_sub          public.assignment_submissions;
  -- ⊕ 1 Oct 2026, corrected 1 Oct 2026 (review MUST-FIX) — the round-aware
  -- walkReview()/finishedAt() walk, in SQL.
  v_deck_ids     uuid[];
  v_latest       jsonb := '{}'::jsonb;
  v_made         jsonb := '{}'::jsonb;
  v_targets      uuid[];
  v_round_done   jsonb := '{}'::jsonb;
  v_n_round      int := 1;
  v_round_complete boolean := false;
  v_last_at      timestamptz;
  v_finish_at    timestamptz;
  v_finish_event uuid;
  v_finish_server timestamptz;
  v_done         boolean;
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
                 coalesce(public.flashcard_quick_check(e->>'answer', af.answer), 'pending')
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

  -- ── completion: FINISHED, not secured (⊕ 1 Oct 2026, round-aware) ────
  select count(*) into v_n from public.assignment_flashcards where assignment_id = p_assignment;
  select array_agg(id) into v_deck_ids from public.assignment_flashcards where assignment_id = p_assignment;
  v_targets := v_deck_ids;

  if v_n > 0 then
    for r in select rv.card_id, rv.rating, rv.phase, rv.event_id, rv.rated_at
               from public.flashcard_reviews rv
              where rv.assignment_id = p_assignment and rv.pupil_id = v_uid
                and rv.rating in ('got_it', 'nearly', 'not_yet')
              order by rv.rated_at, rv.id
    loop
      if coalesce(r.phase, 'review') = 'make' then
        v_made := v_made || jsonb_build_object(r.card_id::text, true);
        continue;
      end if;
      -- make mode: a review row only counts once every card has a
      -- make-phase row too (the writing pass is done) — same gate as the
      -- JS `finishedAt()`.
      continue when v_a.flashcard_mode = 'make'
        and exists (select 1 from unnest(v_deck_ids) d(id) where not (v_made ? d.id::text));

      -- a round that finished but was not all right: either the pupil is
      -- back within the hour (narrow to the leftovers, round n+1) or they
      -- went stale (a brand-new pass — walkReview's `reset()`).
      if v_round_complete then
        if v_last_at is not null and r.rated_at - v_last_at >= interval '60 minutes' then
          v_latest := '{}'::jsonb; v_targets := v_deck_ids; v_round_done := '{}'::jsonb;
          v_n_round := 1; v_round_complete := false;
        else
          select coalesce(array_agg(d.id), '{}'::uuid[]) into v_targets
            from unnest(v_deck_ids) d(id)
           where coalesce(v_latest ->> d.id::text, '') <> 'got_it';
          v_round_done := '{}'::jsonb;
          v_n_round := v_n_round + 1;
          v_round_complete := false;
        end if;
      end if;

      v_latest := v_latest || jsonb_build_object(r.card_id::text, r.rating);
      if exists (select 1 from unnest(v_targets) t(id) where t.id = r.card_id) then
        v_round_done := v_round_done || jsonb_build_object(r.card_id::text, true);
      end if;
      v_last_at := r.rated_at;

      -- the pass showing AT THIS INSTANT is all right → the Done screen.
      -- The FIRST time this happens, ever; nothing after it can un-set it.
      if not exists (select 1 from unnest(v_deck_ids) d(id)
                      where coalesce(v_latest ->> d.id::text, '') <> 'got_it') then
        v_finish_event := r.event_id;
        v_finish_at := r.rated_at;
        exit;
      end if;

      if not exists (select 1 from unnest(v_targets) t(id) where not (v_round_done ? t.id::text)) then
        v_round_complete := true;
      end if;
    end loop;
  end if;

  v_done := v_finish_at is not null;

  select * into v_sub from public.assignment_submissions
   where assignment_id = p_assignment and student_id = v_uid and deleted_at is null
   order by coalesce(attempts, 2147483647), coalesce(submitted_at, 'infinity'::timestamptz), id limit 1;

  if v_done and (v_sub.id is null or v_sub.submitted_at is null) then
    -- T is the SERVER time of the finishing rating — `flashcard_events.
    -- server_at` via its `event_id` — never the device's `rated_at` and
    -- never "now of this call" (idempotent: re-deriving the same history
    -- later must stamp the same instant). Falls back to `rated_at` only if
    -- the event row is somehow gone (never expected; `event_id` is a FK).
    select server_at into v_finish_server from public.flashcard_events where id = v_finish_event;
    v_finish_server := coalesce(v_finish_server, v_finish_at);

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
      update public.assignment_submissions set score = v_n, max_score = v_n,
             submitted_at = v_finish_server, completed_at = v_finish_server, status = 'complete',
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
