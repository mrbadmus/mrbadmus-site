-- Rollback for 20261014120000_wrapped.sql. Manual apply only.
-- Removes everything Wrapped added: three public functions, two internal
-- helpers, the gate, and the settings table. Nothing else was touched by the
-- migration, so nothing else needs restoring.
-- Safe to run when the site is live: the site code does nothing if the
-- wrapped_status RPC is missing.

drop function if exists public.wrapped_class(uuid, boolean);
drop function if exists public.wrapped_pupil(uuid, boolean);
drop function if exists public.wrapped_status(uuid, boolean);
drop function if exists public._wrapped_week_points(uuid, uuid, boolean);
drop function if exists public._wrapped_gate(boolean);
drop table if exists public.wrapped_settings;

-- Registry line. The version is the migration file's own; if Supabase minted a
-- different one when the migration was applied (apply_migration does), delete
-- that row instead: select version from supabase_migrations.schema_migrations where name = 'wrapped';
delete from supabase_migrations.schema_migrations where version = '20261014120000';
