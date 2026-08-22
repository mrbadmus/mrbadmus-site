-- Rollback for 20260822100350_ks3_cards.sql
--
-- Two halves, and only one of them is destructive.
--
-- 1. `ks3_pools_ingest` goes back to its two-pool form. It is restored byte for
--    byte from 20260820220000_ks3_pools_ingest_owner_only.sql, so after this
--    runs the function is exactly what that migration left. Safe on its own,
--    and the only effect is that `ks3_pools_ingest('cards', …)` starts raising
--    'unknown pool' again.
--
-- 2. `ks3_cards` is DROPPED. Everything in it is regenerable — the table is a
--    build artefact of `export_ks3_questions.py` and Python is the source — so
--    nothing authored is lost. What IS lost is anything a later feature has
--    hung off `ks3_cards.id` by foreign key: a per-card "seen" or "starred"
--    row would go with it, and no export can bring that back.
--
--    ⚠️ SO CHECK FOR DEPENDANTS BEFORE RUNNING THE DROP:
--
--      select conrelid::regclass as referencing_table, conname
--        from pg_constraint
--       where confrelid = 'public.ks3_cards'::regclass;
--
--    An empty result means the drop costs one re-export. A non-empty result
--    means `restrict` below will refuse it, which is the intended answer — deal
--    with the dependant deliberately rather than cascading through it.
--
-- Order matters: the function references the table, so it is replaced first.

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

-- `restrict`, not `cascade` — see the note above. The policy, the two indexes
-- and the two check constraints go with the table.
drop table if exists public.ks3_cards restrict;

-- Then remove the registry row so the CLI stops considering it applied:
--   delete from supabase_migrations.schema_migrations
--    where version = '20260822100350';
