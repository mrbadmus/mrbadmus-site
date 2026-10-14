-- Rollback for migrations/20261011170510_b2c_parent_truth_answer_key.sql.
alter table public.question_knowledge_points drop column if exists answer_key;
delete from supabase_migrations.schema_migrations where version = '20261011170510';
