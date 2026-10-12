-- Rollback for baselines/20261013_prod_parent_truth_bundle.sql (PRODUCTION).
--
-- ⚠️ IRREVERSIBLE FOR ITS DATA: drops both tables, and so every answer and
-- every tutor question/reply recorded for every consumer child since the
-- bundle was applied. Take the family export first if any of it is wanted.
--
-- Nothing else is touched (the bundle altered nothing else). The backend
-- probes child_answers: with the table gone it records nothing, the lesson
-- answer route answers 204 and the parent's activity route 503 not_ready —
-- exactly as before the bundle.

begin;
drop table if exists public.child_tutor_questions;
drop table if exists public.child_answers;
commit;
