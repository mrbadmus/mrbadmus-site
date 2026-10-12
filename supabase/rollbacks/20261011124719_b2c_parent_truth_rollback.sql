-- Rollback for migrations/20261011124719_b2c_parent_truth.sql.
-- Drops the four new tables (and so every row recorded in them) and puts the
-- ai_usage_events kind check back to the five kinds it held on 11 Oct 2026.
-- lesson_mark usage rows must go first or the narrower check cannot be added.
-- Rehearsed on TEST (qeppkiswvclkkwbxmlok) on 11 Oct 2026.

delete from public.ai_usage_events where kind = 'lesson_mark';
alter table public.ai_usage_events drop constraint ai_usage_events_kind_check;
alter table public.ai_usage_events add constraint ai_usage_events_kind_check check (kind = any (array[
  'tutor_turn','ai_mark','explain','flashcard_extract','flashcard_answer_check']::text[]));

drop table if exists public.child_tutor_questions;
drop table if exists public.child_answers;
drop table if exists public.question_knowledge_points;
drop table if exists public.knowledge_points;

delete from supabase_migrations.schema_migrations where version = '20261011124719';
