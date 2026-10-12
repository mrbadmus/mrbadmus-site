-- Rollback for migrations/20261011131302_b2c_parent_truth_client_event_id.sql.
drop index if exists public.child_answers_client_event_uidx;
alter table public.child_answers drop column if exists client_event_id;
delete from supabase_migrations.schema_migrations where version = '20261011131302';
