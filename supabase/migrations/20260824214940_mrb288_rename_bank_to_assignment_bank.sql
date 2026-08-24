-- MRB-288 phase 3 (Mide's ruling, 24 Aug 2026): the weekly-assignment pool is
-- named for its owner. "Bank" was generic, and generic invited the exact
-- cross-feed MRB-288 severs; ks3_assignment_bank states which surface owns it.
-- ks3_ladder_questions and ks3_cards keep their names.
--
-- NO compatibility view, deliberately: a missed reference must fail loudly
-- now, in the test window, not silently in September.
--
-- Applied to production 24 Aug 2026 via MCP apply_migration; this filename
-- matches the version schema_migrations recorded. Rehearsed on test
-- (qeppkiswvclkkwbxmlok) first and verified object-by-object there.

alter table public.ks3_bank_questions rename to ks3_assignment_bank;

alter table public.ks3_assignment_bank
  rename constraint ks3_bank_questions_pkey to ks3_assignment_bank_pkey;
alter table public.ks3_assignment_bank
  rename constraint ks3_bank_questions_band_check to ks3_assignment_bank_band_check;
alter index public.ks3_bank_questions_lesson_band_idx
  rename to ks3_assignment_bank_lesson_band_idx;
alter policy ks3_bank_questions_read on public.ks3_assignment_bank
  rename to ks3_assignment_bank_read;

-- The one DB object whose BODY names the table: the exporter's ingest RPC.
-- Recreated verbatim from 20260822101051 with the bank branch pointed at the
-- renamed table. CREATE OR REPLACE preserves the existing grants.
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
    insert into public.ks3_assignment_bank
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
