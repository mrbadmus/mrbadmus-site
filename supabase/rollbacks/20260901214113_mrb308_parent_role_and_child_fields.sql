-- ROLLBACK for MRB-308 Night 1, migration 2 of 6
-- (20260901214113_mrb308_parent_role_and_child_fields). Apply MANUALLY only.
--
-- ⚠️ THIS FAILS, LOUDLY, IF ANY PARENT OR PARENT-ADDED ROW EXISTS — and that
-- is the intended behaviour. Narrowing a CHECK is validated against every
-- existing row, so a single profile with role = 'parent' makes the first
-- statement below raise 23514, and a single class_members row with
-- joined_via = 'parent_added' makes the second one raise. Nothing is half
-- applied; Postgres validates before it commits.
--
-- Check what stands in the way first:
--   select count(*) from public.profiles where role = 'parent';
--   select count(*) from public.class_members where joined_via = 'parent_added';
--   select count(*) from public.profiles
--    where mode is not null or intensity is not null or created_by is not null;
-- Every one of those must be 0. If they are not, the families have to be
-- removed before this file can be applied — this rollback deliberately does
-- not delete anyone's children to make itself pass.
--
-- Apply the rollback for migration 6 BEFORE this one: attach_child_to_family()
-- and parent_update_child() both write profiles.mode / intensity / created_by,
-- and would break at execution time once the columns are gone.

alter table public.profiles
  drop constraint if exists profiles_role_check;

alter table public.profiles
  add constraint profiles_role_check
  check (role in ('student', 'teacher', 'hod', 'admin'));

alter table public.class_members
  drop constraint if exists class_members_joined_via_check;

alter table public.class_members
  add constraint class_members_joined_via_check
  check (joined_via in ('code', 'csv_import', 'sims_sync', 'admin_added'));

alter table public.profiles
  drop constraint if exists profiles_mode_check;

alter table public.profiles
  drop constraint if exists profiles_intensity_check;

-- created_by carries an FK to profiles(id); dropping the column drops it too.
alter table public.profiles
  drop column if exists mode,
  drop column if exists intensity,
  drop column if exists created_by;
