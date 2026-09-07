-- Rollback for MRB-328 J4(a) rum_timings (prod version 20260906154014).
--
-- Drops the trigger first, then the table: the trigger depends on the
-- table, and dropping in the other order leaves a function referring to
-- something gone.
--
-- ⚠️ It DESTROYS collected timings. That is the intent — the data is
-- diagnostic, reproducible by browsing, and worth nothing beside leaving a
-- half-created table behind.

drop trigger  if exists rum_timings_fill_school on public.rum_timings;
drop function if exists public.rum_timings_fill_school();
drop policy   if exists rum_timings_read_admin  on public.rum_timings;
drop policy   if exists rum_timings_insert_self on public.rum_timings;
drop index    if exists public.rum_timings_page_created_idx;
drop index    if exists public.rum_timings_school_created_idx;
drop table    if exists public.rum_timings;
drop function if exists public.rum_fetches_ok(jsonb);
