-- MRB-310 Night 2, migration 10: the KS4 scheme needs more than 39 weeks.
--
-- scheme_of_work_entries.academic_week carries CHECK (1..39): a teaching
-- ORDER within one (year, subject) block, and 39 is the English school year.
-- KS3 fits (ks3_seed_sow.py asserts it). The KS4 default sequence generated
-- tonight from the four all_subtopics_* modules does not: a Triple Higher
-- Chemistry year needs 48 slots, and five of the twelve tier×pathway blocks
-- overflow when split across Year 10 and Year 11. 46 of 865 KS4 rows were
-- dropped by the first seed run because of this ceiling.
--
-- KS4 rows may run to 52; KS3 keeps 39, so the KS3 generator's assertion
-- still means what it says.

alter table public.scheme_of_work_entries
  drop constraint if exists scheme_of_work_entries_academic_week_check;

alter table public.scheme_of_work_entries
  add constraint scheme_of_work_entries_academic_week_check
  check (
    academic_week >= 1
    and academic_week <= case when key_stage = 'KS4' then 52 else 39 end
  );

comment on constraint scheme_of_work_entries_academic_week_check on public.scheme_of_work_entries is
  'MRB-310: 1..39 at KS3 (one school year of teaching order); 1..52 at KS4, where the AQA subtopic sequence for one year of a Triple Higher science runs to 48 slots.';