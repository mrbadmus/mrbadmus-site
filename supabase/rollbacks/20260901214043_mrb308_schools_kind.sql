-- ROLLBACK for MRB-308 Night 1, migration 1 of 6
-- (20260901214043_mrb308_schools_kind). Apply MANUALLY only; the CLI never
-- reads this folder.
--
-- ⚠️ APPLY LAST. This is the bottom of the MRB-308 stack. schools.kind is read
-- by org_is_entitled(), parent_owns_child(), attach_child_to_family() and
-- create_family_for_parent(), all of which are dropped by the rollbacks for
-- migrations 3, 5 and 6. Drop the column while any of them still stands and
-- the function does not fail now — it fails at execution time, on a live
-- signup, which is the worst place to find out.
--
-- Reverse order for the whole set: 6, 5, 4, 3, 2, then this one.
--
-- ⚠️ This DESTROYS the family/organisation distinction. Any consumer org
-- becomes indistinguishable from Rainford. Check first:
--   select kind, count(*) from public.schools group by kind;
-- If anything but 'school' comes back, those orgs must be dealt with before
-- this file is applied.

alter table public.schools
  drop constraint if exists schools_consumer_orgs_are_private;

alter table public.schools
  drop constraint if exists schools_kind_check;

drop index if exists public.idx_schools_kind_consumer;

alter table public.schools
  drop column if exists kind;
