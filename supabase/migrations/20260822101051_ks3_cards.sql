-- The KS3 flashcard deck, mirrored out of the Python source of truth.
--
-- The third pool, and it is the same arrangement as the first two: the cards
-- are written in `ks3_data/<unit>/lesson_*.py`, `export_ks3_questions.py` is
-- the only writer, and a gate (`--verify`) asserts the table still matches
-- Python. This table is a BUILD ARTEFACT. Nothing here authors a card and
-- nothing here may be hand-edited in the database.
--
-- WHY IT HAS TO EXIST. The deck is built from the lessons a class has actually
-- covered, so it is assembled at runtime in the browser, and the browser cannot
-- read Python. There is no other path from `LESSON["vocabulary"]` to a card in
-- front of a child.
--
-- ── TWO KINDS SHIP, AND A THIRD IS A SLOT WITH NO ROWS IN IT ──────────────
--
--   definition  573 rows, one per `LESSON["vocabulary"]` entry, in all 107
--               lessons. front `Define: <term>`, back the authored definition.
--   equation      9 rows, one per authored word equation, across 7 lessons.
--               front `Complete the word equation: <left>`, back the right-hand
--               side, with the parts in their own columns so the surface can
--               draw the row properly.
--
--   key_fact      0 rows. THE CHECK CONSTRAINT ACCEPTS IT AND THE EXPORTER
--               EMITS NONE, deliberately. `key_facts[].text` and `key_note` are
--               STATEMENTS: they are a back with no front. The obvious front,
--               `big_question`, is unusable at card size — a median of 148
--               characters and 87 of the 107 lessons over 120 — so shipping key
--               facts would mean WRITING a science prompt for every lesson.
--               That is Mide's gate, not an export's. The slot is here so that
--               the day those fronts are authored, this migration does not have
--               to move.
--
-- ── THE ARROW IS NEVER A CHARACTER ────────────────────────────────────────
--
-- `equation_arrow` holds the WORD the drawn arrow means — 'gives', 'makes' —
-- which is what the lesson pages author and what the equation component uses as
-- its accessible name. The arrow itself is an SVG drawn by the client; the
-- shipped font subsets carry no U+2192. There is deliberately no column a typed
-- arrow could go in, and the exporter refuses any part containing one.
--
-- `equation_arrow` is NULL for two of the three authored shapes (c5-03's
-- rusting equation and b3-06's three enzyme equations author no arrow word).
-- Null means "draw it, do not read it" — not "there is no arrow".

create table if not exists public.ks3_cards (
  -- '<lesson_slug>#def#<term>' / '<lesson_slug>#eq#<left-hand side>'.
  --
  -- ⚠️ ANCHORED ON THE FRONT, NEVER ON POSITION. Insert a new term at the top
  -- of a lesson's vocabulary and a positional id would make every id below it
  -- name a different card, sliding any per-card state a student has built up
  -- onto the wrong questions. Anchored on the front, reordering moves nothing
  -- and rewriting a definition moves nothing; the id changes only when the
  -- question does.
  id                       text primary key,
  unit_code                text     not null,      -- 'B4'
  lesson_slug              text     not null,      -- 'alveoli-built-for-exchange'
  kind                     text     not null
    check (kind in ('definition', 'equation', 'key_fact')),
  card_position            smallint not null,      -- order within the lesson
  -- The UNIT's title, verbatim from ks3_data/structure.py — 'Breathing and gas
  -- exchange'. Design shows it on both faces and her sample values are unit
  -- titles uppercased; uppercasing is presentation and is done by the surface,
  -- because it is reversible there and is not here.
  topic                    text     not null,
  front                    text     not null,
  back                     text     not null,
  -- The vocabulary entry's `note`: extra teaching detail, and NOT part of the
  -- definition. Its own column rather than appended to `back`, because a
  -- student self-marks by comparing what they said to what is on the back, and
  -- three extra sentences make a card they knew read as one they half-knew.
  back_note                text,
  equation_left            text,
  equation_arrow           text,                   -- a WORD, or null. Never a glyph.
  equation_right           text,
  equation_condition       text,
  equation_condition_over  text,
  equation_condition_under text,
  created_at               timestamptz default now(),
  updated_at               timestamptz default now(),

  -- An equation card is nothing without its two sides, and no other kind may
  -- carry them. Without this an equation row could ship with an empty row to
  -- draw and the page would render a card with a front and no answer.
  constraint ks3_cards_equation_parts check (
    case when kind = 'equation'
         then equation_left is not null and equation_right is not null
         else equation_left is null and equation_arrow is null
              and equation_right is null and equation_condition is null
              and equation_condition_over is null
              and equation_condition_under is null
    end),

  -- The one thing a mirror of a drawn arrow must never become.
  constraint ks3_cards_no_typed_arrow check (
    front not like '%→%' and back not like '%→%'
    and coalesce(equation_left, '') not like '%→%'
    and coalesce(equation_right, '') not like '%→%'
    and coalesce(equation_arrow, '') not like '%→%')
);

-- The deck is drawn per lesson, in card order, for the lessons a class has
-- covered — which is exactly this index.
create index if not exists ks3_cards_lesson_idx
  on public.ks3_cards (lesson_slug, card_position);

create index if not exists ks3_cards_unit_kind_idx
  on public.ks3_cards (unit_code, kind);

alter table public.ks3_cards enable row level security;

-- Reference content, the same for every student. Readable by anyone signed in;
-- only the service role and `ks3_pools_ingest` write. Identical in shape to
-- ks3_ladder_questions_read.
drop policy if exists ks3_cards_read on public.ks3_cards;
create policy ks3_cards_read on public.ks3_cards
  for select to authenticated using (true);


-- ── the ingest helper gains a third branch ────────────────────────────────
--
-- Re-emitted whole rather than patched, because `create or replace function`
-- takes the whole body. The bank and ladder branches are unchanged, byte for
-- byte, from 20260820220000_ks3_pools_ingest_owner_only.sql; the original
-- header comment is reproduced below because it is the security argument and
-- it still applies.
--
-- A single, tightly-guarded way to refresh the KS3 question pools from the
-- Python source, without a service-role key on the machine doing the export.
--
-- The pools are a BUILD ARTEFACT of `export_ks3_questions.py`. Applying ~1 MB of
-- generated upserts through an MCP round-trip is slow and fragile; this takes
-- the same rows as one jsonb payload over PostgREST instead. The whole export
-- now applies in about two seconds.
--
-- ⚠️ SECURITY DEFINER, so the guard is the whole safety story. It is NOT open to
-- `authenticated` at large — an ordinary student holding a valid JWT must not be
-- able to rewrite the question bank. It checks the caller's email against the
-- one account that owns the content. Anything else raises.
--
-- If Mide would rather this did not exist, removing it is one statement, and
-- the only cost is that a pool refresh goes back to ~28 SQL round trips.
-- Nothing else depends on it: the site build does not call it, the backend does
-- not call it, and no page does.
create or replace function public.ks3_pools_ingest(pool text, payload jsonb)
returns integer
language plpgsql
security definer
set search_path = public
as $$
declare
  n integer;
begin
  if coalesce(auth.jwt() ->> 'email', '') <> 'midebolabadmus@gmail.com' then
    raise exception 'ks3_pools_ingest: not permitted';
  end if;

  if pool = 'bank' then
    insert into public.ks3_bank_questions
      (id, unit_code, lesson_slug, band, bank_position, text, figure, options)
    select r.id, r.unit_code, r.lesson_slug, r.band, r.bank_position, r.text,
           r.figure, r.options
      from jsonb_to_recordset(payload) as r(
        id text, unit_code text, lesson_slug text, band text,
        bank_position smallint, text text, figure text, options jsonb)
    on conflict (id) do update set
      unit_code = excluded.unit_code, lesson_slug = excluded.lesson_slug,
      band = excluded.band, bank_position = excluded.bank_position,
      text = excluded.text, figure = excluded.figure,
      options = excluded.options, updated_at = now();
    get diagnostics n = row_count;
    return n;

  elsif pool = 'ladder' then
    insert into public.ks3_ladder_questions
      (question_ref, unit_code, lesson_slug, rung, text, answer_letter, options)
    select r.question_ref, r.unit_code, r.lesson_slug, r.rung, r.text,
           r.answer_letter, r.options
      from jsonb_to_recordset(payload) as r(
        question_ref text, unit_code text, lesson_slug text, rung text,
        text text, answer_letter text, options jsonb)
    on conflict (question_ref) do update set
      unit_code = excluded.unit_code, lesson_slug = excluded.lesson_slug,
      rung = excluded.rung, text = excluded.text,
      answer_letter = excluded.answer_letter, options = excluded.options,
      updated_at = now();
    get diagnostics n = row_count;
    return n;

  elsif pool = 'cards' then
    insert into public.ks3_cards
      (id, unit_code, lesson_slug, kind, card_position, topic, front, back,
       back_note, equation_left, equation_arrow, equation_right,
       equation_condition, equation_condition_over, equation_condition_under)
    select r.id, r.unit_code, r.lesson_slug, r.kind, r.card_position, r.topic,
           r.front, r.back, r.back_note, r.equation_left, r.equation_arrow,
           r.equation_right, r.equation_condition, r.equation_condition_over,
           r.equation_condition_under
      from jsonb_to_recordset(payload) as r(
        id text, unit_code text, lesson_slug text, kind text,
        card_position smallint, topic text, front text, back text,
        back_note text, equation_left text, equation_arrow text,
        equation_right text, equation_condition text,
        equation_condition_over text, equation_condition_under text)
    on conflict (id) do update set
      unit_code = excluded.unit_code, lesson_slug = excluded.lesson_slug,
      kind = excluded.kind, card_position = excluded.card_position,
      topic = excluded.topic, front = excluded.front, back = excluded.back,
      back_note = excluded.back_note,
      equation_left = excluded.equation_left,
      equation_arrow = excluded.equation_arrow,
      equation_right = excluded.equation_right,
      equation_condition = excluded.equation_condition,
      equation_condition_over = excluded.equation_condition_over,
      equation_condition_under = excluded.equation_condition_under,
      updated_at = now();
    get diagnostics n = row_count;
    return n;
  end if;

  raise exception 'ks3_pools_ingest: unknown pool %', pool;
end;
$$;

revoke all on function public.ks3_pools_ingest(text, jsonb) from public;
grant execute on function public.ks3_pools_ingest(text, jsonb) to authenticated;
