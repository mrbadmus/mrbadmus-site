-- Rollback for 20260726180000_ks3_scheme_of_work_overrides.sql
-- Apply MANUALLY only. The Supabase CLI never reads this folder.
--
-- ⚠️ This drops the only thing stopping duplicate KS3 override rows. Any
-- duplicates created afterwards will be silently accepted, and re-applying the
-- forward migration will then FAIL on the unique index — with a school's real
-- scheme of work as the thing you have to pick a winner from. Check before you
-- reverse, and check again before you re-apply:
--
--   select school_id, year_group, subject_id, academic_week, count(*)
--     from public.scheme_of_work_overrides
--    where key_stage = 'KS3'
--    group by 1, 2, 3, 4
--   having count(*) > 1;
--
-- Unlike its companion rollback, this one deletes nothing and cannot fail on
-- existing data: it only drops constraints. There is no exam_board column on
-- this table, so there is no NOT NULL to restore.

begin;

drop index if exists public.scheme_of_work_overrides_ks3_unique;

alter table public.scheme_of_work_overrides
  drop constraint if exists scheme_of_work_overrides_ks3_subtopic_is_slug;

alter table public.scheme_of_work_overrides
  drop constraint if exists scheme_of_work_overrides_ks3_no_tier_or_pathway;

commit;
