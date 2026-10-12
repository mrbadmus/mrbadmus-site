-- B2C parent truth, part 3 (11 Oct 2026). Additive (widens a check).
-- Lesson pages now record KS3 answers that are not ladder rungs (Start-here
-- guesses, predictions, "your turn" calculations), so their knowledge-point
-- tags need their own source. Apply AFTER 20261011131302.
-- Rollback: supabase/rollbacks/20261011154346_b2c_parent_truth_lesson_sources_rollback.sql

alter table public.question_knowledge_points drop constraint question_knowledge_points_source_check;
alter table public.question_knowledge_points add constraint question_knowledge_points_source_check check (source in
  ('ks3_bank','ks4_bank','ks3_ladder','ks3_lesson','exam','ks4_lesson'));
