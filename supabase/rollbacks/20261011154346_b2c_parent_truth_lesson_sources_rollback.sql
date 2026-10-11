-- Rollback for migrations/20261011154346_b2c_parent_truth_lesson_sources.sql.
-- ks3_lesson tag rows must go first or the narrower check cannot be added.
delete from public.question_knowledge_points where source = 'ks3_lesson';
alter table public.question_knowledge_points drop constraint question_knowledge_points_source_check;
alter table public.question_knowledge_points add constraint question_knowledge_points_source_check check (source in
  ('ks3_bank','ks4_bank','ks3_ladder','exam','ks4_lesson'));
delete from supabase_migrations.schema_migrations where version = '20261011154346';
