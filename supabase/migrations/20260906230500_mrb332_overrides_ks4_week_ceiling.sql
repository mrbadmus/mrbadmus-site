-- MRB-332 — a school's own KS4 sequence needs more than 39 weeks.
--
-- `scheme_of_work_overrides.academic_week` carries CHECK (1..39): a teaching
-- ORDER within one (year, subject) block, where 39 is the English school
-- year. MRB-310 already widened the GLOBAL table (`scheme_of_work_entries`)
-- to 52 at KS4, because the AQA subtopic sequence for one year of a Triple
-- Higher science runs to 48 slots. The per-school table was left at 39, and
-- nothing had exercised it: there were no KS4 override rows anywhere.
--
-- Rainford's own KS4 scheme of work exercises it. Measured from the school's
-- spreadsheet, its longest single year is Year 11 Biology at 55 lessons:
--
--     Year 9   Biology 19   Chemistry 20   Physics 17
--     Year 10  Biology 46   Chemistry 48   Physics 47
--     Year 11  Biology 55   Chemistry 45   Physics 46
--
-- (Rainford begins KS4 in Year 9, which is why there are three year groups
-- and not two. `year_group` already allows 7..13, so that part needs
-- nothing.)
--
-- ⚠️ 55 IS ALSO PAST THE GLOBAL TABLE'S 52. The two tables are widened to
-- different numbers on purpose and the difference is not an oversight:
--   · 52 on `scheme_of_work_entries` is what the AQA DEFAULT sequence needs,
--     and that sequence is generated from the site's own curriculum data, so
--     its ceiling is knowable and fixed.
--   · A REAL SCHOOL's sequence is not knowable in advance. It counts taught
--     lessons — tests, review lessons, required practicals split over two
--     periods — not spec points, so it is always longer than the spec order
--     and the next school will differ again.
-- 60 is chosen as the school ceiling: it clears Rainford's 55 with headroom
-- and still refuses a number that could only be a parsing error.
--
-- KS3 keeps 39, so `ks3_seed_sow.py`'s assertion still means what it says.

alter table public.scheme_of_work_overrides
  drop constraint if exists scheme_of_work_overrides_academic_week_check;

alter table public.scheme_of_work_overrides
  add constraint scheme_of_work_overrides_academic_week_check
  check (
    academic_week >= 1
    and academic_week <= case when key_stage = 'KS3' then 39 else 60 end
  );

comment on constraint scheme_of_work_overrides_academic_week_check
  on public.scheme_of_work_overrides is
  'MRB-332: 1..39 at KS3 (one school year of teaching order); 1..60 above it, '
  'where a school''s own KS4 sequence counts taught lessons rather than spec '
  'points — Rainford''s Year 11 Biology runs to 55. The global table''s KS4 '
  'ceiling is 52 and is deliberately lower: it holds the generated AQA '
  'default, whose length is knowable.';
