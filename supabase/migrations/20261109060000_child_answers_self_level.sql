-- A child's level pick (blind run 2, 9 Nov 2026). ADDITIVE ONLY. TEST first;
-- production at merge time only (CLAUDE.md, "When a migration may touch PRODUCTION").
--
--   child_answers.self_level   the VALUE of the level a child picked for their
--                              own written answer, 0–9. Never a mark.
--
-- self_ticks holds the page's positions, and a rung's scheme is its indicative
-- points, so the level couldn't be read back: a parent saw "Ticked 4 of 6" and no
-- pick. The backend probes the column, so it can deploy ahead of this file: until
-- then the level is dropped and the ticks still save.
--
-- Rollback: supabase/rollbacks/20261109060000_child_answers_self_level_rollback.sql

alter table public.child_answers add column if not exists self_level smallint check (self_level between 0 and 9);
comment on column public.child_answers.self_level is
  'The level a child picked for their OWN written answer, by value. Never a mark: no parent total reads it.';
