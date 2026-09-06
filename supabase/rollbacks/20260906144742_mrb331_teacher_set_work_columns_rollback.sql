-- Rollback for 20260906144742_mrb331_teacher_set_work_columns.sql (MRB-331).
-- Apply by hand. The Supabase CLI never reads this folder.
--
-- ⚠️ ORDER MATTERS. The unique index must be widened back BEFORE `source` is
-- dropped, because the index's predicate names that column. Doing it the other
-- way round leaves the estate with no per-class-per-week guard at all.
--
-- ⚠️ THIS IS LOSSY IF ANY TEACHER HAS SET WORK. Dropping `source` cannot
-- distinguish a teacher-set row from an auto one afterwards, and dropping
-- `release_at` releases every held assignment immediately. Check first:
--
--   select count(*) from assignments
--    where source = 'teacher' and set_by is not null and deleted_at is null;
--
-- A non-zero answer means real teacher-set work exists. Widening the unique
-- index below will then FAIL if any class holds both an auto and a teacher-set
-- assignment in one week — which is exactly what the feature creates. Resolve
-- by soft-deleting the teacher-set rows first, deliberately, or do not roll
-- back this far.

drop index if exists public.assignments_class_week_uniq;
create unique index if not exists assignments_class_week_uniq
  on public.assignments (class_id, academic_week)
  where deleted_at is null and academic_week is not null;

drop index if exists public.assignments_class_release_idx;

alter table public.assignments
  drop constraint if exists assignments_source_agrees_with_auto_generated;
alter table public.assignments
  drop constraint if exists assignments_source_check;

alter table public.assignments drop column if exists source;
alter table public.assignments drop column if exists set_by;
alter table public.assignments drop column if exists release_at;

alter table public.classes drop column if exists auto_assignments;
