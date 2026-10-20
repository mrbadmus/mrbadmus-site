-- Rollback for 20261021120000_wrapped_opens.sql. Manual apply only.
-- Drops the two functions and the table (the recorded counts go with it).
-- Safe with the site live: wrapped.js swallows a missing wrapped_mark.
drop function if exists public.wrapped_open_stats();
drop function if exists public.wrapped_mark(uuid, text);
drop table if exists public.wrapped_opens;
-- Registry: apply_migration mints its own version; delete by name if so.
-- select version from supabase_migrations.schema_migrations where name = 'wrapped_opens';
delete from supabase_migrations.schema_migrations where version = '20261021120000';
