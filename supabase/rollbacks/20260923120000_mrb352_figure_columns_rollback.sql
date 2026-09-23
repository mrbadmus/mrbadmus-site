-- Rollback for 20260923120000_mrb352_figure_columns.sql (MRB-352).
-- Apply by hand. The Supabase CLI never reads this folder.
--
-- ⚠️ LOSSY IF ANY ROW HAS BEEN GIVEN A FIGURE. Dropping either column
-- discards every value already written to it. Check first:
--
--   select count(*) from public.ks4_assignment_bank  where figure is not null;
--   select count(*) from public.ks3_ladder_questions where figure is not null;
--
-- A non-zero answer means real figure ids exist and will be lost. That is
-- expected and safe on TEST during rehearsal (Python — the source of truth —
-- still has them, and a forward re-run of the migration plus the exporter
-- restores the column and its values from scratch). It is NOT safe to run
-- against a project where the figure feature has actually shipped to
-- students without first confirming that is really what is wanted.
--
-- No CHECK, no FK, no index, no default was added by the forward migration,
-- so there is nothing else to undo — just the two columns.

alter table public.ks4_assignment_bank  drop column if exists figure;
alter table public.ks3_ladder_questions drop column if exists figure;
