-- ════════════════════════════════════════════════════════════════════════
-- MRB-351 — FLASHCARD HOMEWORK, PART 2 OF 3: THE SERVER-SIDE FUNCTIONS.
--
-- Every function is SECURITY DEFINER, `search_path = public`, and gates the
-- caller as its FIRST statement — the shape `teacher_class_rollup` uses.
-- Nothing is trusted from the request: the class, the school, the cohort,
-- the release instant, the deadline check, every duration and the
-- completion itself are all re-derived here.
--
--   flashcard_deck_save(deck, title, cards, meta, finalise)   teacher
--   flashcard_deck_duplicate(deck)                            teacher
--   flashcard_set_work(classes, deck, mode, rule, …)          teacher
--   flashcard_edit_assignment(id, title, due, note, release)  teacher
--   flashcard_record(assignment, events)                      pupil
--   flashcard_progress(assignment)                            teacher
--   flashcard_pupil_detail(assignment, pupil)                 teacher
--   flashcard_quick_check(pupil_answer, model_answer)         pure
--
-- LONDON TIME. Nothing here formats a wall-clock time; every comparison is
-- between two timestamptz values, so there is no zone to get wrong. The
-- "Friday 3 pm" a teacher picks is converted to an instant in the browser
-- by `MRBSetWork.londonToUtcIso` — the existing, tested converter — and
-- arrives here already absolute.
--
-- REVERSIBLE: supabase/rollbacks/20260924180100_mrb351_flashcards_functions_rollback.sql
-- ════════════════════════════════════════════════════════════════════════

begin;

-- ── the no-model answer check ──────────────────────────────────────────
-- "Blank / one-word / idk-type answers are classified without a model call."
-- Returns NULL when the answer needs the model. Pure and IMMUTABLE, so the
-- edge function and this database agree on what never reaches a model.
create or replace function public.flashcard_quick_check(p_pupil text, p_model text)
returns text language sql immutable set search_path to 'public' as $$
  with n as (
    select regexp_replace(lower(coalesce(p_pupil, '')), '[^a-z0-9 ]+', ' ', 'g') as pa,
           regexp_replace(lower(coalesce(p_model, '')), '[^a-z0-9 ]+', ' ', 'g') as ma
  ), t as (
    select btrim(regexp_replace(pa, '\s+', ' ', 'g')) as pa,
           btrim(regexp_replace(ma, '\s+', ' ', 'g')) as ma
      from n
  )
  select case
    when pa = '' then 'blank'
    when pa = ma then 'match'
    when pa in ('idk', 'i dont know', 'i don t know', 'dont know', 'don t know', 'dunno',
                'no idea', 'not sure', 'no clue', 'pass', 'skip', 'x', 'xx', 'xxx', 'na', 'n a',
                'unsure', 'forgot', 'i forgot', 'i dunno', 'idek', 'not a clue',
                'no answer', 'blank', 'nk', 'dk', 'dno', 'donno', 'i dno', 'hmm', 'um', 'erm')
      then 'blank'
    -- ONE WORD: decided by whether that word is a word of the model answer.
    -- A lone function word is never an answer.
    when pa !~ ' ' and pa in ('the', 'a', 'an', 'it', 'is', 'in', 'of', 'and', 'to', 'on', 'by')
      then 'no'
    when pa !~ ' ' then
      case when (' ' || ma || ' ') like ('% ' || pa || ' %') then 'match' else 'no' end
    else null
  end
  from t
$$;

-- ── deck save ──────────────────────────────────────────────────────────
-- Replaces a deck's cards atomically, keeping the id of every card the
-- caller sent back with one (so an assignment snapshot's `card_id` keeps
-- pointing at the same card through an edit). `p_cards` is
-- [{id?, question, answer, source_ref?, confidence?, flagged?}] in order.
-- `p_finalise` marks the deck READY and refuses while any card is empty.
create or replace function public.flashcard_deck_save(
  p_deck     uuid,
  p_title    text,
  p_cards    jsonb,
  p_meta     jsonb   default '{}'::jsonb,
  p_finalise boolean default true
) returns jsonb
language plpgsql security definer set search_path to 'public' as $$
declare
  v_uid    uuid := auth.uid();
  v_school uuid := auth_user_school_id();
  v_admin  boolean := auth_user_has_scope('school_admin');
  v_deck   public.flashcard_decks;
  v_n      int;
  v_empty  int;
  v_keep   uuid[];
  c        jsonb;
  i        int := 0;
begin
  if v_uid is null or v_school is null or auth_user_role() = 'student' then
    raise exception 'not_staff' using errcode = '42501';
  end if;
  if p_cards is null or jsonb_typeof(p_cards) <> 'array' then
    raise exception 'bad_cards' using errcode = '22023';
  end if;
  v_n := jsonb_array_length(p_cards);
  if v_n > 200 then raise exception 'too_many_cards' using errcode = '22023'; end if;
  if p_title is null or char_length(btrim(p_title)) not between 1 and 120 then
    raise exception 'bad_title' using errcode = '22023';
  end if;

  select count(*) into v_empty from jsonb_array_elements(p_cards) e
   where btrim(coalesce(e->>'question', '')) = '' or btrim(coalesce(e->>'answer', '')) = '';
  if p_finalise and (v_n = 0 or v_empty > 0) then
    raise exception 'cards_incomplete' using errcode = '22023', detail = v_empty::text;
  end if;

  if p_deck is null then
    insert into public.flashcard_decks (school_id, created_by, title, source_kind,
                                        key_stage, subject, topic_id, subtopic_id,
                                        shared_with_school, status)
    values (v_school, v_uid, btrim(p_title),
            coalesce(nullif(p_meta->>'source_kind', ''), 'typed'),
            nullif(p_meta->>'key_stage', ''), nullif(p_meta->>'subject', ''),
            nullif(p_meta->>'topic_id', ''), nullif(p_meta->>'subtopic_id', ''),
            coalesce((p_meta->>'shared_with_school')::boolean, true),
            case when p_finalise then 'ready' else 'draft' end)
    returning * into v_deck;
  else
    select * into v_deck from public.flashcard_decks where id = p_deck for update;
    if not found or v_deck.deleted_at is not null
       or not (v_deck.created_by = v_uid or (v_admin and v_deck.school_id = v_school)) then
      raise exception 'not_your_deck' using errcode = '42501';
    end if;
    update public.flashcard_decks set
      title       = btrim(p_title),
      key_stage   = case when p_meta ? 'key_stage'   then nullif(p_meta->>'key_stage', '')   else key_stage end,
      subject     = case when p_meta ? 'subject'     then nullif(p_meta->>'subject', '')     else subject end,
      topic_id    = case when p_meta ? 'topic_id'    then nullif(p_meta->>'topic_id', '')    else topic_id end,
      subtopic_id = case when p_meta ? 'subtopic_id' then nullif(p_meta->>'subtopic_id', '') else subtopic_id end,
      shared_with_school = coalesce((p_meta->>'shared_with_school')::boolean, shared_with_school),
      status      = case when p_finalise then 'ready' else status end
    where id = v_deck.id
    returning * into v_deck;
  end if;

  -- ids the caller kept; anything else in the deck goes.
  select coalesce(array_agg((e->>'id')::uuid), '{}') into v_keep
    from jsonb_array_elements(p_cards) e
   where e ? 'id' and (e->>'id') ~ '^[0-9a-f-]{36}$';
  delete from public.flashcard_cards where deck_id = v_deck.id and not (id = any (v_keep));

  -- Positions are rewritten in one statement under a deferred unique, so a
  -- reorder never trips over itself half way.
  set constraints flashcard_cards_deck_id_position_key deferred;
  for c in select * from jsonb_array_elements(p_cards) loop
    if c ? 'id' and (c->>'id') ~ '^[0-9a-f-]{36}$'
       and exists (select 1 from public.flashcard_cards where id = (c->>'id')::uuid and deck_id = v_deck.id) then
      update public.flashcard_cards set
        position = i,
        question = left(btrim(coalesce(c->>'question', '')), 400),
        answer   = left(btrim(coalesce(c->>'answer', '')), 600),
        source_ref = nullif(left(c->>'source_ref', 40), ''),
        confidence = (c->>'confidence')::real,
        flagged  = coalesce((c->>'flagged')::boolean, false)
      where id = (c->>'id')::uuid;
    else
      insert into public.flashcard_cards (deck_id, position, question, answer, source_ref, confidence, flagged)
      values (v_deck.id, i, left(btrim(coalesce(c->>'question', '')), 400),
              left(btrim(coalesce(c->>'answer', '')), 600),
              nullif(left(c->>'source_ref', 40), ''), (c->>'confidence')::real,
              coalesce((c->>'flagged')::boolean, false));
    end if;
    i := i + 1;
  end loop;

  return jsonb_build_object('deck_id', v_deck.id, 'card_count', v_n,
                            'status', (select status from public.flashcard_decks where id = v_deck.id));
end $$;

-- ── deck duplicate ─────────────────────────────────────────────────────
-- "Colleagues can duplicate and edit their copy." The copy is the caller's,
-- in the caller's school, sharing nothing with the original but its text.
create or replace function public.flashcard_deck_duplicate(p_deck uuid)
returns uuid
language plpgsql security definer set search_path to 'public' as $$
declare
  v_uid    uuid := auth.uid();
  v_school uuid := auth_user_school_id();
  v_src    public.flashcard_decks;
  v_new    uuid;
begin
  if v_uid is null or v_school is null or auth_user_role() = 'student' then
    raise exception 'not_staff' using errcode = '42501';
  end if;
  select * into v_src from public.flashcard_decks where id = p_deck;
  if not found or not (
       v_src.created_by = v_uid
       or (v_src.deleted_at is null and v_src.school_id = v_school
           and (v_src.shared_with_school or auth_user_has_scope('school_admin')))) then
    raise exception 'deck_not_visible' using errcode = '42501';
  end if;
  insert into public.flashcard_decks (school_id, created_by, title, key_stage, subject, topic_id,
                                      subtopic_id, source_kind, source_file_path, source_file_name,
                                      source_file_sha256, status, shared_with_school, duplicated_from)
  values (v_school, v_uid, left(v_src.title, 113) || ' (copy)', v_src.key_stage, v_src.subject,
          v_src.topic_id, v_src.subtopic_id, v_src.source_kind,
          case when v_src.school_id = v_school then v_src.source_file_path end,
          v_src.source_file_name, v_src.source_file_sha256, v_src.status, true, v_src.id)
  returning id into v_new;
  insert into public.flashcard_cards (deck_id, position, question, answer, source_ref, confidence, flagged)
  select v_new, position, question, answer, source_ref, confidence, flagged
    from public.flashcard_cards where deck_id = v_src.id order by position;
  return v_new;
end $$;

-- ── set work ───────────────────────────────────────────────────────────
-- One assignment per class, atomically, each with its own frozen snapshot.
-- The same caller standing Set work v2 checks: teaches the class (or is the
-- school's admin), class in the caller's school. The same release/deadline
-- rules: release not more than 5 minutes in the past, deadline after
-- release and within 365 days. Replays by `p_client_ref` for 24 hours, so a
-- double tap on a slow phone never sets the work twice.
create or replace function public.flashcard_set_work(
  p_class_ids  uuid[],
  p_deck       uuid,
  p_mode       text,
  p_rule       text,
  p_title      text,
  p_release_at timestamptz,
  p_due_at     timestamptz,
  p_note       text default null,
  p_client_ref text default null
) returns jsonb
language plpgsql security definer set search_path to 'public' as $$
declare
  v_uid     uuid := auth.uid();
  v_school  uuid := auth_user_school_id();
  v_admin   boolean := auth_user_has_scope('school_admin');
  v_deck    public.flashcard_decks;
  v_release timestamptz := coalesce(p_release_at, now());
  v_note    text := nullif(btrim(coalesce(p_note, '')), '');
  v_title   text := btrim(coalesce(p_title, ''));
  v_cls     public.classes;
  v_subject uuid;
  v_ids     uuid[] := '{}';
  v_cid     uuid;
  v_aid     uuid;
  v_prior   jsonb;
  v_n       int;
begin
  if v_uid is null or v_school is null or auth_user_role() = 'student' then
    raise exception 'not_staff' using errcode = '42501';
  end if;

  if p_client_ref is not null then
    select payload into v_prior from public.audit_log
     where actor_id = v_uid and action = 'assignment.flashcards.set'
       and payload->>'client_ref' = p_client_ref and created_at > now() - interval '24 hours'
     order by created_at desc limit 1;
    if v_prior is not null then
      return jsonb_build_object('replayed', true, 'assignment_ids', v_prior->'assignment_ids',
                                'release_at', v_prior->'release_at');
    end if;
  end if;

  if p_class_ids is null or array_length(p_class_ids, 1) is null then
    raise exception 'no_classes' using errcode = '22023';
  end if;
  if array_length(p_class_ids, 1) > 20 then
    raise exception 'too_many_classes' using errcode = '22023';
  end if;
  if p_mode not in ('make', 'review') then raise exception 'bad_mode' using errcode = '22023'; end if;
  if p_rule not in ('secure', 'quick') then raise exception 'bad_rule' using errcode = '22023'; end if;
  if char_length(v_title) not between 1 and 120 then raise exception 'bad_title' using errcode = '22023'; end if;
  if v_note is not null and char_length(v_note) > 300 then raise exception 'bad_note' using errcode = '22023'; end if;
  if v_release < now() - interval '5 minutes' then raise exception 'release_past' using errcode = '22023'; end if;
  if p_due_at is null or p_due_at <= v_release then raise exception 'due_before_release' using errcode = '22023'; end if;
  if p_due_at > now() + interval '365 days' then raise exception 'due_too_far' using errcode = '22023'; end if;

  select * into v_deck from public.flashcard_decks where id = p_deck;
  if not found or v_deck.deleted_at is not null or not (
       v_deck.created_by = v_uid
       or (v_deck.school_id = v_school and (v_deck.shared_with_school or v_admin))) then
    raise exception 'deck_not_visible' using errcode = '42501';
  end if;
  if v_deck.status <> 'ready' then raise exception 'deck_not_ready' using errcode = '22023'; end if;
  select count(*) into v_n from public.flashcard_cards
   where deck_id = v_deck.id and btrim(question) <> '' and btrim(answer) <> '';
  if v_n = 0 or v_n <> v_deck.card_count then raise exception 'deck_not_ready' using errcode = '22023'; end if;

  select id into v_subject from public.subjects
   where lower(name) = coalesce(v_deck.subject, 'science') limit 1;
  if v_subject is null then
    select id into v_subject from public.subjects where lower(name) = 'science' limit 1;
  end if;

  foreach v_cid in array (select array_agg(distinct x) from unnest(p_class_ids) x) loop
    select * into v_cls from public.classes where id = v_cid and deleted_at is null;
    if not found or v_cls.school_id <> v_school
       or not (v_admin or coalesce(auth_user_teaches_class(v_cls.id), false)) then
      raise exception 'class_not_yours' using errcode = '42501', detail = v_cid::text;
    end if;

    insert into public.assignments (
      class_id, school_id, teacher_id, set_by, subject_id, subject, topic, title,
      quiz_type, source, auto_generated, key_stage, year_group,
      release_at, due_at, teacher_note,
      kind, deck_id, flashcard_mode, completion_rule)
    values (
      v_cls.id, v_cls.school_id, v_uid, v_uid, v_subject, v_deck.subject,
      coalesce(v_deck.topic_id, left(v_deck.title, 120)), v_title,
      'flashcards', 'teacher', false, v_cls.key_stage, v_cls.year_group,
      v_release, p_due_at, v_note,
      'flashcards', v_deck.id, p_mode, p_rule)
    returning id into v_aid;

    insert into public.assignment_flashcards (assignment_id, card_id, position, question, answer)
    select v_aid, c.id, row_number() over (order by c.position) - 1, c.question, c.answer
      from public.flashcard_cards c where c.deck_id = v_deck.id order by c.position;

    v_ids := v_ids || v_aid;
  end loop;

  insert into public.audit_log (actor_id, school_id, action, target_table, target_id, payload)
  values (v_uid, v_school, 'assignment.flashcards.set', 'flashcard_decks', v_deck.id,
          jsonb_build_object('client_ref', p_client_ref, 'assignment_ids', to_jsonb(v_ids),
                             'release_at', v_release, 'due_at', p_due_at, 'mode', p_mode,
                             'rule', p_rule, 'cards', v_n));

  return jsonb_build_object('success', true, 'assignment_ids', to_jsonb(v_ids),
                            'release_at', v_release, 'cards', v_n);
end $$;

-- ── edit a flashcard assignment ────────────────────────────────────────
-- The v2.1 edit rules: once released, only the title, the deadline and the
-- note move; before release the release time may move too. The deck and
-- the mode never move — the snapshot is the snapshot.
create or replace function public.flashcard_edit_assignment(
  p_id uuid, p_title text, p_due_at timestamptz, p_note text, p_release_at timestamptz default null
) returns jsonb
language plpgsql security definer set search_path to 'public' as $$
declare
  v_uid   uuid := auth.uid();
  v_a     public.assignments;
  v_rel   timestamptz;
  v_note  text := nullif(btrim(coalesce(p_note, '')), '');
begin
  select * into v_a from public.assignments where id = p_id and deleted_at is null for update;
  if not found or v_a.kind <> 'flashcards'
     or class_school_id(v_a.class_id) is distinct from auth_user_school_id()
     or auth_user_school_id() is null
     or not coalesce(auth_user_teaches_class(v_a.class_id) or auth_user_has_scope('school_admin'), false) then
    raise exception 'not_yours' using errcode = '42501';
  end if;
  v_rel := case when v_a.release_at is not null and v_a.release_at > now() and p_release_at is not null
                then p_release_at else v_a.release_at end;
  if v_rel is distinct from v_a.release_at and v_rel < now() - interval '5 minutes' then
    raise exception 'release_past' using errcode = '22023';
  end if;
  if p_due_at is null or p_due_at <= coalesce(v_rel, v_a.created_at) then
    raise exception 'due_before_release' using errcode = '22023';
  end if;
  if char_length(btrim(coalesce(p_title, ''))) not between 1 and 120 then
    raise exception 'bad_title' using errcode = '22023';
  end if;
  if v_note is not null and char_length(v_note) > 300 then raise exception 'bad_note' using errcode = '22023'; end if;
  update public.assignments set title = btrim(p_title), due_at = p_due_at, teacher_note = v_note,
                                release_at = v_rel, updated_at = now()
   where id = p_id;
  -- A deadline that moves re-judges lateness for work finished before the
  -- move is ever seen by nobody: `is_late` is stamped at completion and is
  -- the historical fact. That is the existing rule for MCQ sets too.
  return jsonb_build_object('ok', true);
end $$;

-- ════════════════════════════════════════════════════════════════════════
-- THE PUPIL SIDE
-- ════════════════════════════════════════════════════════════════════════

-- Per-card standing for one pupil: made? known? secured? The ONE definition
-- of completion — `flashcard_record` and `flashcard_progress` both read it.
--
-- ⚠️ SECURE, AS RULED: every card has `got_it` in TWO DIFFERENT SITTINGS,
-- the later starting at least 60 minutes after the earlier ended. "The
-- make-phase rating counts as the first session": writing an answer and
-- judging it against the model answer is its own sitting, so a make-phase
-- `got_it` pairs with ANY later review-phase `got_it` without the 60-minute
-- gap. Two REVIEW sittings need the gap, which is what stops "Finish for
-- now" and straight back in from counting twice. Sitting boundaries are
-- SERVER times (`started_at`, `ended_at`, `last_seen_at`), never the
-- device clock, so the gap cannot be manufactured by changing the clock.
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

-- Recompute one sitting's figures from its raw events. ACTIVE TIME is the
-- sum of the gaps between consecutive events, each capped at 180 s, where
-- a gap counts only if the tab was VISIBLE at its start (a `visibility`
-- event carries the new state; every other event carries the state it was
-- sent in). Durations use the device's own clock — it is the only clock
-- that saw the card — and only ever as DIFFERENCES within one sitting.
create or replace function public.mrb351_session_refresh(p_session uuid)
returns void
language plpgsql security definer set search_path to 'public' as $$
declare
  v_s public.flashcard_sessions;
begin
  select * into v_s from public.flashcard_sessions where id = p_session;
  if not found then return; end if;
  with ev as (
    select e.client_at, e.visible,
           lead(e.client_at) over (order by e.client_at, e.server_at, e.id) as next_at
      from public.flashcard_events e where e.session_id = p_session
  )
  update public.flashcard_sessions s set
    active_ms = coalesce((select sum(least(180000, greatest(0,
                   (extract(epoch from (ev.next_at - ev.client_at)) * 1000)::bigint)))
                   from ev where ev.visible and ev.next_at is not null), 0)::int,
    cards_seen = (select count(distinct card_id) from public.flashcard_events
                   where session_id = p_session and type = 'card_shown' and card_id is not null),
    cards_rated = (select count(*) from public.flashcard_reviews where session_id = p_session),
    cards_made = (select count(*) from public.flashcard_pupil_cards where session_id = p_session),
    median_think_ms = (select percentile_disc(0.5) within group (order by think_ms)
                         from public.flashcard_reviews where session_id = p_session and think_ms is not null),
    median_write_ms = (select percentile_disc(0.5) within group (order by written_ms)
                         from public.flashcard_pupil_cards where session_id = p_session)
  where s.id = p_session;
  -- RUSHED — a flag, never a block: a median think under 1.5 s over ten or
  -- more ratings, or a make-phase median writing time under 4 s over five
  -- or more written cards.
  update public.flashcard_sessions set rushed =
      (cards_rated >= 10 and coalesce(median_think_ms, 999999) < 1500)
      or (cards_made >= 5 and coalesce(median_write_ms, 999999) < 4000)
   where id = p_session;
end $$;
revoke all on function public.mrb351_session_refresh(uuid) from public, anon, authenticated;

-- Active milliseconds between two events of one sitting (same rule as above).
create or replace function public.mrb351_active_between(p_session uuid, p_from timestamptz, p_to timestamptz)
returns integer
language sql stable security definer set search_path to 'public' as $$
  with ev as (
    select e.client_at, e.visible,
           lead(e.client_at) over (order by e.client_at, e.server_at, e.id) as next_at
      from public.flashcard_events e where e.session_id = p_session
  )
  select coalesce(sum(least(180000, greatest(0,
           (extract(epoch from (least(ev.next_at, p_to) - ev.client_at)) * 1000)::bigint))), 0)::int
    from ev
   where ev.visible and ev.next_at is not null
     and ev.client_at >= p_from and ev.client_at < p_to
$$;
revoke all on function public.mrb351_active_between(uuid, timestamptz, timestamptz) from public, anon, authenticated;

-- ── flashcard_record: the ONE pupil write path ─────────────────────────
-- `p_events` is [{id, type, card?, at, visible?, phase?, rating?, answer?}],
-- `at` in epoch milliseconds or ISO. Idempotent by `id`: a batch sent twice
-- over a flaky connection inserts nothing the second time and changes no
-- figure. Called with '[]' it only returns the pupil's state (resume).
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

  -- ── completion ──────────────────────────────────────────────────────
  select count(*) into v_n from public.assignment_flashcards where assignment_id = p_assignment;
  select v_n > 0 and bool_and(cs.secured and (v_a.flashcard_mode <> 'make' or cs.made))
    into v_done from public.flashcard_card_state(p_assignment, v_uid) cs;

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

-- ════════════════════════════════════════════════════════════════════════
-- THE TEACHER SIDE
-- ════════════════════════════════════════════════════════════════════════

-- Who may read an assignment's flashcard progress: a teacher of the class,
-- or the school's admin/SLT, or an active platform operator. Returns the
-- assignment, or raises.
create or replace function public.mrb351_teacher_gate(p_assignment uuid)
returns public.assignments
language plpgsql stable security definer set search_path to 'public' as $$
declare v_a public.assignments;
begin
  select * into v_a from public.assignments where id = p_assignment and kind = 'flashcards';
  if not found then raise exception 'not_found' using errcode = '42501'; end if;
  if not coalesce(auth_user_operator_active()
          or (class_school_id(v_a.class_id) = auth_user_school_id()
              and (auth_user_teaches_class(v_a.class_id)
                   or auth_user_has_scope('school_admin') or auth_user_has_scope('slt'))), false) then
    raise exception 'not_found' using errcode = '42501';
  end if;
  return v_a;
end $$;
revoke all on function public.mrb351_teacher_gate(uuid) from public, anon, authenticated;

-- One row per ACTIVE pupil of the class, every figure the table shows, plus
-- the class strip above it. `p_now` is the caller's clock for the Missing
-- rule, for the same reason `teacher_class_rollup` takes one.
create or replace function public.flashcard_progress(p_assignment uuid, p_now timestamptz default null)
returns jsonb
language plpgsql stable security definer set search_path to 'public' as $$
declare
  v_a   public.assignments;
  v_now timestamptz := coalesce(p_now, now());
  v_n   int;
  v_out jsonb;
begin
  v_a := public.mrb351_teacher_gate(p_assignment);
  select count(*) into v_n from public.assignment_flashcards where assignment_id = p_assignment;

  with pupils as (
    select distinct cm.student_id as pid, p.first_name, p.last_name, p.display_name
      from public.class_members cm join public.profiles p on p.id = cm.student_id
     where cm.class_id = v_a.class_id and cm.left_at is null and cm.deleted_at is null
       and p.deleted_at is null
  ),
  sub as (
    select distinct on (s.student_id) s.student_id, s.submitted_at, s.completed_at, s.is_late
      from public.assignment_submissions s
     where s.assignment_id = p_assignment and s.deleted_at is null
     order by s.student_id, coalesce(s.attempts, 2147483647),
              coalesce(s.submitted_at, 'infinity'::timestamptz), s.id
  ),
  sess as (
    select s.pupil_id, count(*)::int as sittings, sum(s.active_ms)::bigint as active_ms,
           bool_or(s.rushed) as rushed, max(s.last_seen_at) as last_seen
      from public.flashcard_sessions s where s.assignment_id = p_assignment group by s.pupil_id
  ),
  think as (
    select rv.pupil_id, percentile_disc(0.5) within group (order by rv.think_ms) as med_think
      from public.flashcard_reviews rv
     where rv.assignment_id = p_assignment and rv.think_ms is not null group by rv.pupil_id
  ),
  ans as (
    select pc.pupil_id,
           count(*) filter (where answer_check = 'match')::int   as a_match,
           count(*) filter (where answer_check = 'partial')::int as a_partial,
           count(*) filter (where answer_check = 'no')::int      as a_no,
           count(*) filter (where answer_check = 'blank')::int   as a_blank,
           count(*) filter (where answer_check = 'pending')::int as a_pending,
           percentile_disc(0.5) within group (order by written_ms) as med_write
      from public.flashcard_pupil_cards pc where pc.assignment_id = p_assignment group by pc.pupil_id
  ),
  standing as (
    select pu.pid,
           (select count(*) filter (where made)    from public.flashcard_card_state(p_assignment, pu.pid))::int as made,
           (select count(*) filter (where known)   from public.flashcard_card_state(p_assignment, pu.pid))::int as known,
           (select count(*) filter (where secured) from public.flashcard_card_state(p_assignment, pu.pid))::int as secured
      from pupils pu
  ),
  prow as (
    select pu.pid, pu.first_name, pu.last_name, pu.display_name,
           st.made, st.known, st.secured,
           coalesce(se.sittings, 0) as sittings, coalesce(se.active_ms, 0) as active_ms,
           th.med_think, an.med_write, coalesce(se.rushed, false) as rushed, se.last_seen,
           an.a_match, an.a_partial, an.a_no, an.a_blank, an.a_pending,
           sb.submitted_at, sb.is_late,
           case
             when sb.submitted_at is not null and coalesce(sb.is_late, false) then 'done_late'
             when sb.submitted_at is not null then 'done'
             when v_a.due_at is not null and v_a.due_at <= v_now then 'missing'
             when se.sittings is null then 'not_started'
             else 'in_progress'
           end as status
      from pupils pu
      join standing st on st.pid = pu.pid
      left join sess  se on se.pupil_id = pu.pid
      left join think th on th.pupil_id = pu.pid
      left join ans   an on an.pupil_id = pu.pid
      left join sub   sb on sb.student_id = pu.pid
  ),
  reteach as (
    select af.id, af.position, af.question, af.answer, count(*)::int as not_yet
      from public.flashcard_reviews rv
      join public.assignment_flashcards af on af.id = rv.card_id
     where rv.assignment_id = p_assignment and rv.rating = 'not_yet'
       and rv.pupil_id in (select pid from pupils)
     group by af.id, af.position, af.question, af.answer
     order by count(*) desc, af.position
     limit 5
  )
  select jsonb_build_object(
    'assignment', jsonb_build_object('id', v_a.id, 'title', v_a.title, 'class_id', v_a.class_id,
                    'mode', v_a.flashcard_mode, 'rule', v_a.completion_rule, 'due_at', v_a.due_at,
                    'release_at', v_a.release_at, 'note', v_a.teacher_note, 'deck_id', v_a.deck_id,
                    'class_name', (select name from public.classes where id = v_a.class_id)),
    'n', v_n,
    'now', v_now,
    'class', jsonb_build_object(
      'pupils', (select count(*) from prow),
      'done', (select count(*) from prow where status in ('done', 'done_late')),
      'completion_pct', case when (select count(*) from prow) = 0 then null
        else round(((select count(*) from prow where status in ('done', 'done_late'))::float8
                    / (select count(*) from prow)::float8 * 100)::numeric)::int end,
      'avg_sittings', (select round(avg(sittings)::numeric, 1) from prow where sittings > 0),
      'reteach', coalesce((select jsonb_agg(jsonb_build_object('card_id', id, 'position', position,
                   'question', question, 'answer', answer, 'not_yet', not_yet)
                   order by not_yet desc, position) from reteach), '[]'::jsonb)),
    'pupils', coalesce((select jsonb_agg(jsonb_build_object(
        'pupil_id', pid, 'first_name', first_name, 'last_name', last_name, 'display_name', display_name,
        'status', status, 'made', made, 'known', known, 'secured', secured,
        'sittings', sittings, 'active_ms', active_ms, 'median_think_ms', med_think,
        'median_write_ms', med_write, 'rushed', rushed, 'last_active', last_seen,
        'answers', jsonb_build_object('match', coalesce(a_match, 0), 'partial', coalesce(a_partial, 0),
                    'no', coalesce(a_no, 0), 'blank', coalesce(a_blank, 0), 'pending', coalesce(a_pending, 0)),
        'completed_at', submitted_at) order by last_name, first_name, pid) from prow), '[]'::jsonb)
  ) into v_out;
  return v_out;
end $$;

-- The drawer: every card with the pupil's answer, their rating history,
-- and their sittings as a timeline. Read-only.
create or replace function public.flashcard_pupil_detail(p_assignment uuid, p_pupil uuid)
returns jsonb
language plpgsql stable security definer set search_path to 'public' as $$
declare
  v_a public.assignments;
begin
  v_a := public.mrb351_teacher_gate(p_assignment);
  if not exists (select 1 from public.class_members cm
                  where cm.class_id = v_a.class_id and cm.student_id = p_pupil) then
    raise exception 'not_found' using errcode = '42501';
  end if;
  return jsonb_build_object(
    'pupil', (select jsonb_build_object('id', p.id, 'first_name', p.first_name,
                                        'last_name', p.last_name, 'display_name', p.display_name)
                from public.profiles p where p.id = p_pupil),
    'cards', coalesce((select jsonb_agg(jsonb_build_object(
        'id', af.id, 'position', af.position, 'question', af.question, 'answer', af.answer,
        'mine', pc.pupil_answer, 'check', pc.answer_check, 'written_ms', pc.written_ms,
        'secured', cs.secured, 'known', cs.known,
        'ratings', coalesce((select jsonb_agg(jsonb_build_object('rating', rv.rating, 'phase', rv.phase,
                     'at', rv.rated_at, 'think_ms', rv.think_ms, 'session_id', rv.session_id)
                     order by rv.rated_at)
                     from public.flashcard_reviews rv
                    where rv.assignment_id = p_assignment and rv.pupil_id = p_pupil
                      and rv.card_id = af.id), '[]'::jsonb)
      ) order by af.position)
      from public.assignment_flashcards af
      join public.flashcard_card_state(p_assignment, p_pupil) cs on cs.card_id = af.id
      left join public.flashcard_pupil_cards pc
        on pc.assignment_id = p_assignment and pc.pupil_id = p_pupil and pc.card_id = af.id
     where af.assignment_id = p_assignment), '[]'::jsonb),
    'sessions', coalesce((select jsonb_agg(jsonb_build_object(
        'id', s.id, 'started_at', s.started_at, 'ended_at', coalesce(s.ended_at, s.last_seen_at),
        'open', s.ended_at is null, 'active_ms', s.active_ms, 'cards_seen', s.cards_seen,
        'cards_rated', s.cards_rated, 'cards_made', s.cards_made,
        'median_think_ms', s.median_think_ms, 'rushed', s.rushed) order by s.started_at)
      from public.flashcard_sessions s
     where s.assignment_id = p_assignment and s.pupil_id = p_pupil), '[]'::jsonb)
  );
end $$;

-- ── grants ─────────────────────────────────────────────────────────────
revoke all on function public.flashcard_deck_save(uuid, text, jsonb, jsonb, boolean) from public, anon;
revoke all on function public.flashcard_deck_duplicate(uuid) from public, anon;
revoke all on function public.flashcard_set_work(uuid[], uuid, text, text, text, timestamptz, timestamptz, text, text) from public, anon;
revoke all on function public.flashcard_edit_assignment(uuid, text, timestamptz, text, timestamptz) from public, anon;
revoke all on function public.flashcard_record(uuid, jsonb) from public, anon;
revoke all on function public.flashcard_progress(uuid, timestamptz) from public, anon;
revoke all on function public.flashcard_pupil_detail(uuid, uuid) from public, anon;
grant execute on function public.flashcard_deck_save(uuid, text, jsonb, jsonb, boolean) to authenticated;
grant execute on function public.flashcard_deck_duplicate(uuid) to authenticated;
grant execute on function public.flashcard_set_work(uuid[], uuid, text, text, text, timestamptz, timestamptz, text, text) to authenticated;
grant execute on function public.flashcard_edit_assignment(uuid, text, timestamptz, text, timestamptz) to authenticated;
grant execute on function public.flashcard_record(uuid, jsonb) to authenticated;
grant execute on function public.flashcard_progress(uuid, timestamptz) to authenticated;
grant execute on function public.flashcard_pupil_detail(uuid, uuid) to authenticated;
grant execute on function public.flashcard_quick_check(text, text) to authenticated, service_role;

commit;
