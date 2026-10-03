-- ⚠️⚠️⚠️ TEST ONLY — NEVER RUN THIS ON PRODUCTION (urklkrwevjtlfbwnipjn). ⚠️⚠️⚠️
--
-- Running it on production would DROP A REAL PRODUCTION CONSTRAINT:
-- `schools_admin_user_id_fkey` existed on production long before the B2C
-- repair migration that this file undoes. That migration was a no-op on
-- production; this rollback is NOT. It exists only so the TEST rehearsal
-- (apply → verify → roll back → verify → re-apply) can be repeated.
--
-- Undoes: 20261003212731_b2c_repair_schools_admin_user_id_fkey.sql (TEST only).
-- After running it, delete the registry row on TEST:
--   DELETE FROM supabase_migrations.schema_migrations WHERE version = '20261003212731';
ALTER TABLE public.schools DROP CONSTRAINT IF EXISTS schools_admin_user_id_fkey;

NOTIFY pgrst, 'reload schema';
