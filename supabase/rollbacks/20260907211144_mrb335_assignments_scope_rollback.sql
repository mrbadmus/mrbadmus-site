-- ROLLBACK for 20260907211144_mrb335_assignments_scope.sql (MRB-335).
--
-- Apply MANUALLY only — psql or the Supabase SQL Editor. The CLI never reads
-- this folder. After it succeeds, remove the registry row:
--
--   delete from supabase_migrations.schema_migrations
--    where version = '20260907211144';
--
-- ⚠️ THIS DESTROYS DATA IF ANY v2 WORK HAS BEEN SET. `set_tier`, `scope_kind`,
-- `scope_ref`, `subject` and `paper` are the only record of what a
-- teacher-chosen assignment actually was; `topic`/`subtopic` carry display
-- strings, not the tree node. Count first, and do not run this on a database
-- that answers non-zero:
--
--   select count(*) from public.assignments where scope_ref is not null;
--
-- The forward migration's backfill was a no-op on both projects (measured:
-- 0 rows), so nothing it wrote needs restoring — but a route that has since run
-- has written real rows, and they cannot be recovered from anywhere else.

alter table public.assignments drop constraint if exists assignments_paper_check;
alter table public.assignments drop constraint if exists assignments_subject_check;
alter table public.assignments drop constraint if exists assignments_scope_kind_check;
alter table public.assignments drop constraint if exists assignments_set_tier_check;

alter table public.assignments drop column if exists paper;
alter table public.assignments drop column if exists subject;
alter table public.assignments drop column if exists scope_ref;
alter table public.assignments drop column if exists scope_kind;
alter table public.assignments drop column if exists set_tier;
