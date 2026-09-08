-- ROLLBACK for 20260907235438_mrb335_classes_tier_write_seal.sql (MRB-335).
--
-- Apply MANUALLY only. Then:
--   delete from supabase_migrations.schema_migrations where version = '20260907235438';
--
-- ⚠️ THIS RE-OPENS A WRITE HOLE, and it is the one this migration was written
-- to close. `classes_staff_write` is `FOR ALL` to every teacher, hod and admin
-- in the school, and the frontend holds a client with the teacher's own JWT —
-- so with this trigger gone, any teacher can PATCH `/rest/v1/classes` and move
-- a class's `tier`, `science_pathway` or `science_subject` with no scope check
-- and no audit row. A Foundation Combined class flipped to Higher Triple is
-- served the full specification, and the only symptom is a child meeting
-- questions three years above them in work that looks entirely normal.
--
-- Do not run this to make a write succeed. If a legitimate writer is being
-- refused, the answer is to give that writer `school_admin`, or to route the
-- write through `POST /api/admin/class-tier`, which the trigger permits.

drop trigger if exists classes_guard_tier_columns on public.classes;
drop function if exists public.classes_guard_tier_columns();
