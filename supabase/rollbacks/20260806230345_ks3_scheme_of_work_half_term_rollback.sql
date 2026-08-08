-- Rollback for 20260806230345_ks3_scheme_of_work_half_term.sql
-- Apply MANUALLY only. The Supabase CLI never reads this folder.
--
-- ⚠️ This DROPS the column, and with it every half-term value in the table.
-- No data is recoverable from the table afterwards.
--
-- That is survivable rather than serious, and it is worth saying why: the
-- half-term placement is DERIVED, not authored. `ks3_data/half_terms.py`
-- computes it from the published default sequence, so re-applying the
-- migration and re-running `python3 ks3_seed_sow.py` reproduces every dropped
-- value byte for byte.
--
-- ⛔ That is true of the PLATFORM DEFAULT only. If a school's own half-term
-- values have been written into this table by then, they are that school's
-- data and are NOT reproducible from Python. Check before dropping:
--
--   select count(*) from public.scheme_of_work_entries
--    where key_stage = 'KS3' and half_term is not null;
--
-- (Note that school schemes live in public.scheme_of_work_overrides, which
-- this migration never touched and this rollback never touches.)

begin;

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_half_term_is_ks3_only;

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_half_term_range;

alter table public.scheme_of_work_entries
  drop column if exists half_term;

commit;
