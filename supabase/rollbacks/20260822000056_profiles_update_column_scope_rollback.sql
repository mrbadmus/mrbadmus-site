-- Rollback for 20260822013000_profiles_update_column_scope.sql
--
-- ⚠️ THIS RE-OPENS THE PRIVILEGE-ESCALATION PATH. It restores `UPDATE` on all
-- columns to `authenticated` and `anon`, which is the state in which a student
-- can write their own `profiles.role`, flip `auth_user_has_scope('school_admin')`
-- to true, and read every profile in their school. Demonstrated, not theorised.
--
-- Apply it only to unblock a real student-facing breakage, and only for as long
-- as it takes to find which column was missing from the grant list — the fix for
-- that is one more column on the GRANT, not this file.

grant update on public.profiles to authenticated, anon;

-- The `WITH CHECK` the migration wrote is deliberately LEFT IN PLACE. Postgres
-- was already using `USING` as the check, so the clause changed no behaviour
-- when it landed and removing it would change none now. `ALTER POLICY` with
-- only a `USING` clause does not clear a `WITH CHECK` anyway — a statement here
-- that looked like it did would be a lie in a file somebody runs at 2am.
