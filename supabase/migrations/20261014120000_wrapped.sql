-- MrBadmus Wrapped — the database half (14 Oct 2026)
--
-- A Spotify-Wrapped-style half-term story for pupils, and a class version for
-- teachers. Everything here is ADDITIVE: one new table, one internal gate, two
-- internal helpers and three public functions. No existing table, function,
-- policy or trigger is altered. Contract: docs/wrapped/PLAN.md section 1.
--
-- WHAT IS COUNTED, AND WHERE THE RULES ARE COPIED FROM
--   * secured cards   -> public.flashcard_card_state(assignment, pupil).secured,
--                        called, never re-implemented ("any got_it ever", MRB-354).
--   * stars           -> the class board (class_stars_board_for_member): per
--                        (class, teaching week) round(sum(score)/sum(max)*100)
--                        over COUNTED first attempts only (submitted_at <= due_at,
--                        due_at not null, score/max not null, max > 0); week =
--                        coalesce(academic_week, _mrb_week_number(year start,
--                        coalesce(release_at, created_at))); first attempt =
--                        ORDER BY coalesce(attempts, 2147483647),
--                        coalesce(submitted_at, 'infinity') LIMIT 1; ties on the
--                        class top three = whoever finished first, then pupil id.
--   * the gate        -> _wrapped_gate(): open once release_at has passed (and
--                        before close_at, if set); otherwise only the pupils and
--                        teachers named in wrapped_settings.preview_profile_ids
--                        may see it, and only when the caller asks for preview.
--
-- PRIVACY: there is no pupil parameter. wrapped_pupil always answers for
-- auth.uid(). Other pupils' numbers never leave the database: the top-band card
-- carries only the band (1/5/10 percent, or "top 3 of the class"), never a rank,
-- a group size, a name or a score.
--
-- CATCH-UP HOMEWORK (added at the commander's request): a parked column
-- assignments.recipient_ids uuid[] (NULL = whole-class homework, non-empty =
-- catch-up for those pupils only) may or may not exist where this runs. This
-- file NEVER names that column. wrapped_class() recognises "whole-class" work
-- with  (to_jsonb(a) -> 'recipient_ids') is null / 'null' / '[]'  which is true
-- whether the column is absent or NULL. Catch-up work therefore never counts in
-- the CLASS totals (handed_in, flashcards, most_secured, revisit, top3 stars,
-- opener active). wrapped_pupil() DOES count it: it is the pupil's own work.
--
-- Deploy order is safe either way: the site code calls wrapped_status and does
-- nothing if the RPC is missing.

-- ───────────────────────────────────────────────────────────────────────
-- PART 1 — the one settings row
-- ───────────────────────────────────────────────────────────────────────

create table if not exists public.wrapped_settings (
  id                   boolean primary key default true check (id),
  release_at           timestamptz not null,
  close_at             timestamptz,
  window_start         timestamptz not null,
  half_term_from       date,
  half_term_to         date,
  christmas_on         date,
  show_zero_card       boolean not null default true,
  preview_profile_ids  uuid[] not null default '{}'
);

comment on table public.wrapped_settings is
  'MrBadmus Wrapped: the single settings row. Read only by the SECURITY DEFINER wrapped_* functions; RLS on with no policies and no grants. Change a date with one UPDATE.';
comment on column public.wrapped_settings.release_at is 'When Wrapped opens for everyone. Before this, only preview_profile_ids can see it (and only with preview asked for).';
comment on column public.wrapped_settings.close_at is 'NULL = the button stays until someone sets a close date.';
comment on column public.wrapped_settings.show_zero_card is 'false hides the "Your Wrapped starts now" card for pupils with no activity.';

alter table public.wrapped_settings enable row level security;
revoke all on public.wrapped_settings from public, anon, authenticated;

insert into public.wrapped_settings
  (id, release_at, close_at, window_start, half_term_from, half_term_to, christmas_on, show_zero_card, preview_profile_ids)
values
  (true,
   timestamptz '2026-10-20 08:00:00 Europe/London',
   null,
   timestamptz '2026-09-01 00:00:00 Europe/London',
   date '2026-10-24', date '2026-11-01',
   date '2026-12-18',
   true,
   array['b0308282-5429-4050-827f-4707286a88aa'::uuid,   -- AY (pupil, 8r/Sc1)
         '74db2bf7-7c0d-47e6-9479-5cee3cda610e'::uuid])  -- Mide (teacher, 8r/Sc1)
on conflict (id) do nothing;

-- ───────────────────────────────────────────────────────────────────────
-- PART 2 — the gate (internal)
-- ───────────────────────────────────────────────────────────────────────

create or replace function public._wrapped_gate(p_preview boolean)
returns text
language sql stable security definer set search_path = public
as $$
  select coalesce((
    select case
      when now() >= s.release_at and (s.close_at is null or now() < s.close_at) then 'open'
      when coalesce(p_preview, false) and auth.uid() is not null
           and auth.uid() = any (s.preview_profile_ids) then 'preview'
      else 'closed'
    end
    from public.wrapped_settings s
    limit 1
  ), 'closed');
$$;

revoke all on function public._wrapped_gate(boolean) from public, anon, authenticated;

-- ───────────────────────────────────────────────────────────────────────
-- PART 3 — week points (internal): the class board's rule, over the window
-- ───────────────────────────────────────────────────────────────────────
-- p_class NULL = every class (the pupil's own total); not NULL = that class's
-- CURRENT members only. p_pupil NULL = everyone. p_whole_only drops catch-up
-- work (see header). Returns one row per (class, pupil, teaching week).

create or replace function public._wrapped_week_points(p_class uuid, p_pupil uuid, p_whole_only boolean)
returns table (class_id uuid, student_id uuid, wk int, pts int, tie_at timestamptz)
language sql stable security definer set search_path = public
as $$
  with s as (select window_start from public.wrapped_settings limit 1),
  a_ok as (
    select a.id, a.class_id,
           coalesce(a.academic_week::int,
                    public._mrb_week_number(ay.start_date, coalesce(a.release_at, a.created_at))) as wk,
           a.due_at
      from public.assignments a
      join public.classes c on c.id = a.class_id and c.deleted_at is null
      join public.academic_years ay on ay.id = c.academic_year_id
     where a.deleted_at is null
       and a.due_at is not null
       and (p_class is null or a.class_id = p_class)
       and (not p_whole_only
            or (to_jsonb(a) -> 'recipient_ids') is null
            or (to_jsonb(a) -> 'recipient_ids') in ('null'::jsonb, '[]'::jsonb))
  ),
  fa as (
    select distinct on (sub.assignment_id, sub.student_id)
           sub.assignment_id, sub.student_id, sub.score, sub.max_score,
           sub.submitted_at, sub.completed_at
      from public.assignment_submissions sub
      join a_ok on a_ok.id = sub.assignment_id
     where sub.deleted_at is null
       and (p_pupil is null or sub.student_id = p_pupil)
       and (p_class is null or exists (
              select 1 from public.class_members cm
               where cm.class_id = p_class and cm.student_id = sub.student_id
                 and cm.left_at is null and cm.deleted_at is null))
     order by sub.assignment_id, sub.student_id,
              coalesce(sub.attempts, 2147483647), coalesce(sub.submitted_at, 'infinity'::timestamptz)
  )
  select a_ok.class_id, fa.student_id, a_ok.wk,
         coalesce(round(sum(fa.score)::numeric / nullif(sum(fa.max_score), 0) * 100)::int, 0),
         max(coalesce(fa.completed_at, fa.submitted_at))
    from fa
    join a_ok on a_ok.id = fa.assignment_id
    cross join s
   where fa.submitted_at is not null
     and fa.submitted_at >= s.window_start and fa.submitted_at <= now()
     and fa.submitted_at <= a_ok.due_at
     and fa.score is not null and fa.max_score is not null and fa.max_score > 0
   group by a_ok.class_id, fa.student_id, a_ok.wk;
$$;

revoke all on function public._wrapped_week_points(uuid, uuid, boolean) from public, anon, authenticated;

-- ───────────────────────────────────────────────────────────────────────
-- PART 4 — wrapped_status: cheap, runs on every class page load
-- ───────────────────────────────────────────────────────────────────────

create or replace function public.wrapped_status(p_class_id uuid, p_preview boolean default false)
returns jsonb
language plpgsql stable security definer set search_path = public
as $$
declare
  v_uid   uuid := auth.uid();
  s       public.wrapped_settings%rowtype;
  v_gate  text;
  v_role  text;
  v_act   boolean;
begin
  select * into s from public.wrapped_settings limit 1;
  v_gate := public._wrapped_gate(p_preview);

  if v_uid is not null then
    if public.auth_user_is_member_of_class(p_class_id) then
      v_role := 'pupil';
    elsif public.auth_user_teaches_class(p_class_id) then
      v_role := 'teacher';
    end if;
  end if;

  if v_role is null or v_gate = 'closed' then
    return jsonb_build_object('open', false, 'preview', false, 'role', v_role,
                              'has_activity', null, 'show_zero', coalesce(s.show_zero_card, true));
  end if;

  if v_role = 'pupil' then
    v_act := exists (select 1 from public.assignment_submissions x
                      where x.student_id = v_uid and x.deleted_at is null
                        and x.submitted_at >= s.window_start and x.submitted_at <= now())
          or exists (select 1 from public.flashcard_reviews r
                      where r.pupil_id = v_uid
                        and r.rated_at >= s.window_start and r.rated_at <= now())
          or exists (select 1 from public.quiz_scores q
                      where q.user_id = v_uid
                        and q.created_at >= s.window_start and q.created_at <= now());
  end if;

  return jsonb_build_object('open', true, 'preview', v_gate = 'preview', 'role', v_role,
                            'has_activity', v_act, 'show_zero', s.show_zero_card);
end;
$$;

-- ───────────────────────────────────────────────────────────────────────
-- PART 5 — wrapped_pupil: the pupil's own story (never takes a pupil id)
-- ───────────────────────────────────────────────────────────────────────

create or replace function public.wrapped_pupil(p_class_id uuid, p_preview boolean default false)
returns jsonb
language plpgsql stable security definer set search_path = public
as $$
declare
  v_uid      uuid := auth.uid();
  s          public.wrapped_settings%rowtype;
  v_gate     text;
  v_cname    text;
  v_first    text;
  v_user     text;
  v_head     jsonb;
  v_active   boolean;
  v_cards    jsonb := '[]'::jsonb;
  v_mine     jsonb;
  v_decks    jsonb;
  v_hw       int;
  v_stars    int;
  v_sec      int;
  v_fin      int;
  v_best_src text;            -- 'homework' | 'deck' | null
  v_best     jsonb;
  v_best_deck uuid;
  v_streak   int; v_streak_cur boolean;
  v_band     jsonb;
  v_wfrom_d  date;
  v_today    date;
  v_now_wk   int;
  v_c        int;
  v_metric   text;
  v_pace     numeric;
  v_wleft    numeric;
  v_overlap  int;
  v_proj     int;
begin
  if v_uid is null or not public.auth_user_is_member_of_class(p_class_id) then
    return jsonb_build_object('state', 'not_member');
  end if;
  v_gate := public._wrapped_gate(p_preview);
  if v_gate = 'closed' then
    return jsonb_build_object('state', 'closed');
  end if;
  select * into s from public.wrapped_settings limit 1;

  select c.name into v_cname from public.classes c where c.id = p_class_id;
  select p.first_name, p.username::text into v_first, v_user from public.profiles p where p.id = v_uid;

  v_head := jsonb_build_object(
    'state', 'open', 'preview', v_gate = 'preview',
    'name', jsonb_build_object('first', v_first, 'username', v_user),
    'class', jsonb_build_object('id', p_class_id, 'name', v_cname),
    'window', jsonb_build_object('from', (s.window_start at time zone 'Europe/London')::date,
                                 'to',   (now() at time zone 'Europe/London')::date));

  v_active := exists (select 1 from public.assignment_submissions x
                       where x.student_id = v_uid and x.deleted_at is null
                         and x.submitted_at >= s.window_start and x.submitted_at <= now())
           or exists (select 1 from public.flashcard_reviews r
                       where r.pupil_id = v_uid and r.rated_at >= s.window_start and r.rated_at <= now())
           or exists (select 1 from public.quiz_scores q
                       where q.user_id = v_uid and q.created_at >= s.window_start and q.created_at <= now());

  if not v_active then
    return v_head || jsonb_build_object('zero', true, 'show_zero', s.show_zero_card);
  end if;

  v_head := v_head || jsonb_build_object('zero', false);
  v_wfrom_d := (s.window_start at time zone 'Europe/London')::date;
  v_today   := (now() at time zone 'Europe/London')::date;
  v_now_wk  := public._mrb_week_number(v_wfrom_d, now());

  -- The pupil's first-attempt hand-ins in the window, every class, once.
  select coalesce(jsonb_agg(jsonb_build_object(
           'aid', x.assignment_id, 'topic', a.topic, 'title', a.title, 'kind', a.kind,
           'cid', a.class_id, 'score', x.score, 'max', x.max_score, 'at', x.submitted_at)), '[]'::jsonb)
    into v_mine
    from (select distinct on (sub.assignment_id) sub.assignment_id, sub.score, sub.max_score, sub.submitted_at
            from public.assignment_submissions sub
           where sub.student_id = v_uid and sub.deleted_at is null
           order by sub.assignment_id, coalesce(sub.attempts, 2147483647),
                    coalesce(sub.submitted_at, 'infinity'::timestamptz)) x
    join public.assignments a on a.id = x.assignment_id and a.deleted_at is null
   where x.submitted_at is not null and x.submitted_at >= s.window_start and x.submitted_at <= now();

  -- The pupil's decks (flashcard assignments reviewed in the window) with secured counts.
  select coalesce(jsonb_agg(jsonb_build_object('aid', d.aid, 'title', d.title, 'cards', d.cards, 'sec', d.sec)), '[]'::jsonb)
    into v_decks
    from (select a.id as aid, a.title, count(*)::int as cards, (count(*) filter (where st.secured))::int as sec
            from (select distinct r.assignment_id from public.flashcard_reviews r
                   where r.pupil_id = v_uid and r.rated_at >= s.window_start and r.rated_at <= now()) fr
            join public.assignments a on a.id = fr.assignment_id and a.deleted_at is null
           cross join lateral public.flashcard_card_state(a.id, v_uid) st
           group by a.id, a.title) d;

  -- 1. opener
  v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'opener'));

  -- 2. flashcards
  select coalesce(sum((d->>'sec')::int), 0)::int,
         (count(*) filter (where (d->>'cards')::int > 0 and (d->>'sec')::int = (d->>'cards')::int))::int
    into v_sec, v_fin
    from jsonb_array_elements(v_decks) d;
  if v_sec > 0 then
    v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'flashcards', 'secured', v_sec, 'decks_finished', v_fin));
  end if;

  -- 3. homework
  select count(*)::int into v_hw
    from jsonb_to_recordset(v_mine) m(kind text) where m.kind <> 'flashcards';
  select coalesce(sum(w.pts), 0)::int into v_stars from public._wrapped_week_points(null, v_uid, false) w;
  if v_hw > 0 then
    v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'homework', 'handed_in', v_hw, 'stars', v_stars));
  end if;

  -- 4. best topic: homework >= 70, else a fully secured deck, else homework >= 50
  with t as (
    select m.topic, count(*)::int as n, round(100.0 * sum(m.score) / nullif(sum(m."max"), 0))::int as pct
      from jsonb_to_recordset(v_mine) m(topic text, kind text, score int, "max" int)
     where m.kind <> 'flashcards' and m.score is not null and m."max" > 0
     group by m.topic),
  bt as (select t.topic, t.pct from t order by t.pct desc, t.n desc, t.topic limit 1),
  bd as (select (d->>'aid')::uuid as aid, d->>'title' as title, (d->>'cards')::int as cards
           from jsonb_array_elements(v_decks) d
          where (d->>'cards')::int > 0 and (d->>'sec')::int = (d->>'cards')::int
          order by (d->>'cards')::int desc, d->>'title' limit 1)
  select case
           when (select pct from bt) >= 70 then 'homework'
           when exists (select 1 from bd) then 'deck'
           when (select pct from bt) >= 50 then 'homework'
         end,
         case
           when (select pct from bt) >= 70 or (not exists (select 1 from bd) and (select pct from bt) >= 50)
             then (select jsonb_build_object('kind', 'best_topic', 'topic', topic, 'source', 'homework', 'pct', pct) from bt)
           when exists (select 1 from bd)
             then (select jsonb_build_object('kind', 'best_topic', 'topic', title, 'source', 'deck', 'cards', cards) from bd)
         end,
         (select aid from bd)
    into v_best_src, v_best, v_best_deck;
  if v_best is not null then
    v_cards := v_cards || jsonb_build_array(v_best);
  end if;
  if v_best is null or v_best_src <> 'deck' then v_best_deck := null; end if;

  -- 5. streak: consecutive teaching weeks with any hand-in, flashcard review or quiz row
  with ev as (
    select public._mrb_week_number(v_wfrom_d, x.submitted_at) as w
      from public.assignment_submissions x
     where x.student_id = v_uid and x.deleted_at is null
       and x.submitted_at >= s.window_start and x.submitted_at <= now()
    union
    select public._mrb_week_number(v_wfrom_d, r.rated_at)
      from public.flashcard_reviews r
     where r.pupil_id = v_uid and r.rated_at >= s.window_start and r.rated_at <= now()
    union
    select public._mrb_week_number(v_wfrom_d, q.created_at)
      from public.quiz_scores q
     where q.user_id = v_uid and q.created_at >= s.window_start and q.created_at <= now()),
  isl as (select w, w - row_number() over (order by w) as g from ev),
  runs as (select count(*)::int as len, max(w) as last_w from isl group by g)
  select len, last_w >= v_now_wk - 1 into v_streak, v_streak_cur
    from runs order by len desc, last_w desc limit 1;
  if coalesce(v_streak, 0) >= 2 then
    v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'streak', 'weeks', v_streak, 'current', coalesce(v_streak_cur, false)));
  end if;

  -- 6. top band: year (honest top 1/5/10 %), else class (top 3), else personal deck
  with keys as (
    select distinct m.topic, c.school_id, c.academic_year_id as ay, c.year_group as yg, c.id as cid, c.name as cname
      from jsonb_to_recordset(v_mine) m(topic text, kind text, cid uuid, score int, "max" int)
      join public.classes c on c.id = m.cid
     where m.kind <> 'flashcards' and m.score is not null and m."max" > 0),
  ga as (
    select a.id, a.topic, c.id as cid, c.school_id, c.academic_year_id as ay, c.year_group as yg
      from public.assignments a
      join public.classes c on c.id = a.class_id and c.deleted_at is null
     where a.deleted_at is null and a.kind <> 'flashcards'
       and a.topic in (select topic from keys)
       and exists (select 1 from keys k where k.school_id = c.school_id and k.ay = c.academic_year_id and k.yg = c.year_group)),
  fs as (
    select distinct on (sub.assignment_id, sub.student_id)
           sub.assignment_id, sub.student_id, sub.score, sub.max_score, sub.submitted_at
      from public.assignment_submissions sub
      join ga on ga.id = sub.assignment_id
     where sub.deleted_at is null
     order by sub.assignment_id, sub.student_id, coalesce(sub.attempts, 2147483647),
              coalesce(sub.submitted_at, 'infinity'::timestamptz)),
  pp as (
    select ga.topic, ga.school_id, ga.ay, ga.yg, ga.cid, fs.student_id, fs.score, fs.max_score
      from fs join ga on ga.id = fs.assignment_id
     where fs.submitted_at is not null and fs.submitted_at >= s.window_start and fs.submitted_at <= now()
       and fs.score is not null and fs.max_score > 0),
  yl as (select topic, school_id, ay, yg, student_id,
                round(100.0 * sum(score) / sum(max_score))::int as pct
           from pp group by topic, school_id, ay, yg, student_id),
  ystat as (
    select y.topic, y.yg, me.pct as mypct, count(*)::int as n,
           (count(*) filter (where y.pct >= me.pct))::int as rk
      from yl y
      join yl me on me.topic = y.topic and me.school_id = y.school_id and me.ay = y.ay and me.yg = y.yg
                and me.student_id = v_uid
     group by y.topic, y.school_id, y.ay, y.yg, me.pct),
  ycand as (
    select topic, yg, mypct,
           (select min(b) from unnest(array[1, 5, 10]) b where rk <= ceil(n * b / 100.0)) as band
      from ystat where n >= 10),
  cl as (select topic, cid, student_id, round(100.0 * sum(score) / sum(max_score))::int as pct
           from pp group by topic, cid, student_id),
  cstat as (
    select c1.topic, c1.cid, me.pct as mypct, count(*)::int as n,
           (count(*) filter (where c1.pct >= me.pct))::int as rk
      from cl c1
      join cl me on me.topic = c1.topic and me.cid = c1.cid and me.student_id = v_uid
     group by c1.topic, c1.cid, me.pct),
  ccand as (select cs.topic, cs.mypct, k.cname
              from cstat cs join (select distinct topic, cid, cname from keys) k on k.topic = cs.topic and k.cid = cs.cid
             where cs.n >= 10 and cs.rk <= 3)
  select coalesce(
           (select jsonb_build_object('kind', 'top_band', 'scope', 'year', 'band', band, 'year_group', yg, 'topic', topic)
              from ycand where band is not null order by band, mypct desc, topic limit 1),
           (select jsonb_build_object('kind', 'top_band', 'scope', 'class', 'top', 3, 'class_name', cname, 'topic', topic)
              from ccand order by mypct desc, topic limit 1))
    into v_band;
  if v_band is null then
    select jsonb_build_object('kind', 'top_band', 'scope', 'personal', 'topic', d->>'title', 'cards', (d->>'cards')::int)
      into v_band
      from jsonb_array_elements(v_decks) d
     where (d->>'cards')::int > 0 and (d->>'sec')::int = (d->>'cards')::int
       and (v_best_deck is null or (d->>'aid')::uuid <> v_best_deck)
     order by (d->>'cards')::int desc, d->>'title' limit 1;
  end if;
  if v_band is not null then
    v_cards := v_cards || jsonb_build_array(v_band);
  end if;

  -- 7. forward: what December could look like at this pace
  v_metric := case when v_sec > 0 then 'cards' when v_hw > 0 then 'homework' end;
  v_c := case v_metric when 'cards' then v_sec when 'homework' then v_hw end;
  if v_metric is not null and s.christmas_on is not null and s.christmas_on > v_today then
    v_pace := v_c / greatest(1::numeric, (v_today - v_wfrom_d) / 7.0);
    v_overlap := case
      when s.half_term_from is null or s.half_term_to is null then 0
      else greatest(0, least(s.christmas_on, s.half_term_to + 1) - greatest(v_today, s.half_term_from))
    end;
    v_wleft := greatest(0, (s.christmas_on - v_today) - v_overlap) / 7.0;
    v_proj := v_c + floor(v_pace * v_wleft)::int;
    if v_proj > v_c then
      v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'forward', 'metric', v_metric, 'now', v_c, 'projected', v_proj));
    end if;
  end if;

  -- Active, but nothing countable beyond the opener (e.g. one lesson quiz in
  -- one week): no story of zeros. Same answer as a pupil with no activity.
  if jsonb_array_length(v_cards) <= 1 then
    return v_head || jsonb_build_object('zero', true, 'show_zero', s.show_zero_card);
  end if;

  return v_head || jsonb_build_object('cards', v_cards);
end;
$$;

-- ───────────────────────────────────────────────────────────────────────
-- PART 6 — wrapped_class: the teacher's class story (never names a pupil
-- except the first name of the top three)
-- ───────────────────────────────────────────────────────────────────────

create or replace function public.wrapped_class(p_class_id uuid, p_preview boolean default false)
returns jsonb
language plpgsql stable security definer set search_path = public
as $$
declare
  s        public.wrapped_settings%rowtype;
  v_uid    uuid := auth.uid();
  v_gate   text;
  v_cname  text;
  v_yg     int;
  v_cards  jsonb := '[]'::jsonb;
  v_pupils int; v_active int; v_hw int;
  v_sec    int; v_decks int;
  v_ms     jsonb; v_rv jsonb; v_top jsonb;
begin
  if v_uid is null or not public.auth_user_teaches_class(p_class_id) then
    return jsonb_build_object('state', 'not_teacher');
  end if;
  v_gate := public._wrapped_gate(p_preview);
  if v_gate = 'closed' then
    return jsonb_build_object('state', 'closed');
  end if;
  select * into s from public.wrapped_settings limit 1;
  select c.name, c.year_group into v_cname, v_yg from public.classes c where c.id = p_class_id;

  -- Whole-class work in the window (catch-up work is left out on purpose),
  -- current members, and each member's first-attempt hand-ins on that work.

  with mem as (
    select cm.student_id from public.class_members cm
      join public.profiles p on p.id = cm.student_id and p.deleted_at is null
     where cm.class_id = p_class_id and cm.left_at is null and cm.deleted_at is null),
  a_ok as (
    select a.id, a.kind, a.topic, a.title from public.assignments a
     where a.class_id = p_class_id and a.deleted_at is null
       and ((to_jsonb(a) -> 'recipient_ids') is null
            or (to_jsonb(a) -> 'recipient_ids') in ('null'::jsonb, '[]'::jsonb))),
  fa as (
    select distinct on (sub.assignment_id, sub.student_id)
           sub.assignment_id, sub.student_id, sub.score, sub.max_score, sub.submitted_at
      from public.assignment_submissions sub
      join a_ok on a_ok.id = sub.assignment_id
      join mem on mem.student_id = sub.student_id
     where sub.deleted_at is null
     order by sub.assignment_id, sub.student_id, coalesce(sub.attempts, 2147483647),
              coalesce(sub.submitted_at, 'infinity'::timestamptz)),
  hi as (
    select fa.*, a_ok.kind, a_ok.topic from fa join a_ok on a_ok.id = fa.assignment_id
     where fa.submitted_at is not null and fa.submitted_at >= s.window_start and fa.submitted_at <= now()),
  rv as (
    select distinct r.pupil_id, r.assignment_id from public.flashcard_reviews r
      join a_ok on a_ok.id = r.assignment_id and a_ok.kind = 'flashcards'
      join mem on mem.student_id = r.pupil_id
     where r.rated_at >= s.window_start and r.rated_at <= now())
  select (select count(*) from mem)::int,
         (select count(*) from (select student_id from hi union select pupil_id from rv) z)::int,
         (select count(*) from hi where kind <> 'flashcards')::int
    into v_pupils, v_active, v_hw;

  v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'opener', 'pupils', v_pupils, 'active', v_active));
  if v_hw > 0 then
    v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'homework', 'handed_in', v_hw));
  end if;

  -- flashcards: secured cards across members, decks started, and the most secured deck
  with mem as (
    select cm.student_id from public.class_members cm
      join public.profiles p on p.id = cm.student_id and p.deleted_at is null
     where cm.class_id = p_class_id and cm.left_at is null and cm.deleted_at is null),
  a_ok as (
    select a.id, a.title from public.assignments a
     where a.class_id = p_class_id and a.deleted_at is null and a.kind = 'flashcards'
       and ((to_jsonb(a) -> 'recipient_ids') is null
            or (to_jsonb(a) -> 'recipient_ids') in ('null'::jsonb, '[]'::jsonb))),
  pairs as (
    select distinct r.assignment_id, r.pupil_id from public.flashcard_reviews r
      join a_ok on a_ok.id = r.assignment_id
      join mem on mem.student_id = r.pupil_id
     where r.rated_at >= s.window_start and r.rated_at <= now()),
  st as (
    select p.assignment_id, p.pupil_id, count(*)::int as cards, (count(*) filter (where cs.secured))::int as sec
      from pairs p
     cross join lateral public.flashcard_card_state(p.assignment_id, p.pupil_id) cs
     group by p.assignment_id, p.pupil_id),
  per_deck as (
    select st.assignment_id, a_ok.title, sum(st.sec)::int as sec, sum(st.cards)::int as cards
      from st join a_ok on a_ok.id = st.assignment_id group by st.assignment_id, a_ok.title)
  select (select coalesce(sum(sec), 0) from per_deck)::int,
         (select count(*) from per_deck)::int,
         (select jsonb_build_object('kind', 'most_secured', 'topic', title, 'pct', round(100.0 * sec / cards)::int)
            from per_deck where sec > 0 and cards > 0
           order by sec::numeric / cards desc, sec desc, title limit 1)
    into v_sec, v_decks, v_ms;
  if v_sec > 0 then
    v_cards := v_cards || jsonb_build_array(jsonb_build_object('kind', 'flashcards', 'secured', v_sec, 'decks', v_decks));
  end if;
  if v_ms is not null then
    v_cards := v_cards || jsonb_build_array(v_ms);
  end if;

  -- revisit: the lowest-scoring homework topic with at least 3 hand-ins
  with mem as (
    select cm.student_id from public.class_members cm
      join public.profiles p on p.id = cm.student_id and p.deleted_at is null
     where cm.class_id = p_class_id and cm.left_at is null and cm.deleted_at is null),
  a_ok as (
    select a.id, a.topic from public.assignments a
     where a.class_id = p_class_id and a.deleted_at is null and a.kind <> 'flashcards'
       and ((to_jsonb(a) -> 'recipient_ids') is null
            or (to_jsonb(a) -> 'recipient_ids') in ('null'::jsonb, '[]'::jsonb))),
  fa as (
    select distinct on (sub.assignment_id, sub.student_id)
           sub.assignment_id, sub.score, sub.max_score, sub.submitted_at
      from public.assignment_submissions sub
      join a_ok on a_ok.id = sub.assignment_id
      join mem on mem.student_id = sub.student_id
     where sub.deleted_at is null
     order by sub.assignment_id, sub.student_id, coalesce(sub.attempts, 2147483647),
              coalesce(sub.submitted_at, 'infinity'::timestamptz))
  select jsonb_build_object('kind', 'revisit', 'topic', t.topic, 'pct', t.pct)
    into v_rv
    from (select a_ok.topic, count(*) as n, round(100.0 * sum(fa.score) / sum(fa.max_score))::int as pct
            from fa join a_ok on a_ok.id = fa.assignment_id
           where fa.submitted_at is not null and fa.submitted_at >= s.window_start and fa.submitted_at <= now()
             and fa.score is not null and fa.max_score > 0
           group by a_ok.topic having count(*) >= 3) t
   order by t.pct, t.topic limit 1;
  if v_rv is not null then
    v_cards := v_cards || jsonb_build_array(v_rv);
  end if;

  -- top3: stars, first name only (surname initial only if two of the three share a first name)
  with w as (
    select wp.student_id, sum(wp.pts)::int as stars, max(wp.tie_at) as tie_at
      from public._wrapped_week_points(p_class_id, null, true) wp group by wp.student_id),
  r as (
    select w.student_id, w.stars, p.first_name, p.last_name,
           row_number() over (order by w.stars desc, w.tie_at asc nulls last, w.student_id) as rn
      from w join public.profiles p on p.id = w.student_id and p.deleted_at is null
     where w.stars > 0),
  t3 as (select * from r where rn <= 3)
  select jsonb_build_object('kind', 'top3', 'pupils', jsonb_agg(
           jsonb_build_object(
             'first_name', case when (select count(*) from t3 x where lower(x.first_name) = lower(t3.first_name)) > 1
                                then trim(coalesce(t3.first_name, '') || ' ' || coalesce(upper(substring(t3.last_name from 1 for 1)) || '.', ''))
                                else coalesce(t3.first_name, '') end,
             'stars', t3.stars) order by t3.rn))
    into v_top
    from t3 having count(*) > 0;
  if v_top is not null then
    v_cards := v_cards || jsonb_build_array(v_top);
  end if;

  return jsonb_build_object('state', 'open', 'preview', v_gate = 'preview',
           'class', jsonb_build_object('id', p_class_id, 'name', v_cname, 'year_group', v_yg),
           'cards', v_cards);
end;
$$;

-- ───────────────────────────────────────────────────────────────────────
-- PART 7 — grants. The three public functions are callable by signed-in users
-- only; the helpers and the table are not reachable by them at all.
-- ───────────────────────────────────────────────────────────────────────

revoke all on function public.wrapped_status(uuid, boolean) from public, anon;
revoke all on function public.wrapped_pupil(uuid, boolean)  from public, anon;
revoke all on function public.wrapped_class(uuid, boolean)  from public, anon;
grant execute on function public.wrapped_status(uuid, boolean) to authenticated;
grant execute on function public.wrapped_pupil(uuid, boolean)  to authenticated;
grant execute on function public.wrapped_class(uuid, boolean)  to authenticated;
