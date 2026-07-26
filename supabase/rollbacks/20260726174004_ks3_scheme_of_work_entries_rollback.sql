-- Rollback for 20260726174004_ks3_scheme_of_work_entries.sql
-- Apply MANUALLY only. The Supabase CLI never reads this folder.
--
-- ⚠️ This restores exam_board NOT NULL. If any KS3 rows exist they have
-- exam_board IS NULL and the ALTER will fail. Delete or migrate those rows
-- first — deliberately not done automatically here, because silently deleting
-- a school's scheme of work is exactly the kind of thing a rollback should
-- make someone decide on purpose.
--
--   select count(*) from public.scheme_of_work_entries where key_stage = 'KS3';

begin;

drop index if exists public.scheme_of_work_entries_ks3_unique;

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_ks3_subtopic_is_slug;

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_ks3_no_tier_or_pathway;

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_ks3_has_no_board;

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_exam_board_check;

alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_exam_board_check
  check (exam_board in (
    'AQA', 'Edexcel', 'OCR', 'WJEC', 'CCEA', 'Eduqas', 'CIE', 'SQA'
  ));

alter table public.scheme_of_work_entries
  alter column exam_board set not null;

commit;
