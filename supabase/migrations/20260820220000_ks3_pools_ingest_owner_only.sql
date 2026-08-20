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
  end if;

  raise exception 'ks3_pools_ingest: unknown pool %', pool;
end;
$$;

revoke all on function public.ks3_pools_ingest(text, jsonb) from public;
grant execute on function public.ks3_pools_ingest(text, jsonb) to authenticated;
