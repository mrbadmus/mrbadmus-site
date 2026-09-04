-- ROLLBACK for 20260901231121_mrb313_exam_questions_and_answers. Apply by hand only.
-- ⚠️ Drops every child's written answer and every mark, AI or Mr Badmus's,
-- and the question pool with its schemes (the code_seed set is reproducible
-- from scripts/seed-exam-questions.js in the backend repo; the answers are not).
drop trigger if exists trg_exam_answers_touch on public.exam_answers;
drop function if exists public.mb_quota_used(uuid);
drop table if exists public.exam_answers;
drop table if exists public.exam_questions;
