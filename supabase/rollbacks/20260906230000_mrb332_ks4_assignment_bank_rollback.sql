-- Rollback for 20260906230000_mrb332_ks4_assignment_bank.sql
--
-- Apply MANUALLY. The Supabase CLI never reads this folder.
--
-- ⚠️ THIS DROPS EVERY KS4 ASSIGNMENT QUESTION. That is safe in the sense that
-- the questions are a BUILD ARTEFACT — `ks4_data/questions/**.py` in the site
-- repo is the source, and `python3 export_ks4_questions.py` rebuilds the
-- table from it. It is NOT safe if anything has been hand-edited in the
-- database, which is forbidden precisely so that this rollback stays cheap.
--
-- What it does NOT undo, because it never touched them: rows in
-- `assignment_questions` that reference these ids. A KS4 assignment already
-- set would keep its `source_ref` values and find nothing behind them. If
-- KS4 assignments exist, delete or re-point those first — check with:
--
--     select count(*) from public.assignment_questions aq
--       join public.assignments a on a.id = aq.assignment_id
--      where a.key_stage = 'KS4';

drop policy if exists ks4_assignment_bank_read on public.ks4_assignment_bank;

drop index if exists public.ks4_assignment_bank_subject_idx;
drop index if exists public.ks4_assignment_bank_serving_idx;

drop table if exists public.ks4_assignment_bank;
