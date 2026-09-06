#!/usr/bin/env python3
"""MRB-328 J1 — re-verify every teacher's platform timetable against the sheet.

Re-run of the MRB-326 verification, repeated because J1 added one entry that
is NOT in the sheet's staffing: the sheet's single BMT-coded lesson
(8r/Sc3, Wed P4) is now owned by BRB under Mide's standing ruling that BRB
owns that class. That row is expected as a RULED ADDITION — it must show up
as a surplus of exactly one against BRB's sheet count, and nowhere else.

The sheet carries real staff names, so it stays untracked and its path is an
argument. Only three-letter staff codes appear in this file or its output.

It emits a single SQL statement that does the set difference SERVER-SIDE, so
the comparison never depends on transcribing 200 rows out of the database by
hand. Run it against prod and expect zero rows back.

  python3 verify_timetable_sheet.py --sheet 'Timetable/Science TT 2026-27.xlsx' \
      --year-id <academic_year_id> > diff.sql

RESOLVING A STAFF CODE TO AN OWNER is the one subtle part, and it caught this
run out. An entry is owned EITHER by a pending_staff row (unclaimed) OR by a
profile (claimed, since MRB-293), so the query has to look both ways —
`ps.id = te.pending_staff_id OR ps.claimed_profile_id = te.teacher_id`.
That still misses BDA: he was a real profile before the pending_staff seeding
ever ran, so no pending_staff row carries his code and nothing maps his 21
entries back to "BDA". Left unhandled that reads as 21 missing lessons — the
whole of one teacher's timetable — when nothing at all is wrong. The query
below therefore treats "owned by a profile no pending_staff row claims" as
BDA, which is true while he is the only such owner; the emitted SQL asserts
that uniqueness rather than assuming it.
"""
import argparse, json, re, sys
from collections import defaultdict

import openpyxl

# A teaching cell is "<class> $<CODE> (#room)". Everything else on the grid is
# non-teaching: [PPA]/[MAN]/[COVER]/[INTER]/[BLANK]/registration groups, and
# EMC/<slot> enrichment. MRB-306 excluded all of them and so does this.
CELL = re.compile(r'^([0-9]{1,2}[A-Za-z]{1,2}/[A-Za-z]{2}[0-9]?)\s+\$([A-Z]{3})')
SIXTH_FORM = re.compile(r'^1[23]')          # Y12/13 sets have no platform class
RULED_ADDITIONS = {("BRB", "8r/Sc3", 3, 4)}  # J1: the sheet's BMT lesson

# BMT holds no timetable: there is no pending_staff row for the code, so it can
# own nothing. Its single teaching cell is the one RULED_ADDITIONS re-attributes
# to BRB, so the code is dropped here and re-enters as BRB's — counting it under
# both would show as one missing and one surplus that cancel out invisibly.
NO_PLATFORM_STAFF = {"BMT"}


def read_sheet(path):
    ws = openpyxl.load_workbook(path, data_only=True)["Sheet1"]
    header = {c.column: str(c.value or "") for c in ws[1]}
    days = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5}
    out = set()
    for row in ws.iter_rows(min_row=2, max_row=15):
        code = str(row[0].value or "").strip()
        if not code:
            continue
        for cell in row[1:]:
            head = header.get(cell.column, "")
            if ":" not in head:
                continue
            day, period = head.split(":", 1)
            if period == "Reg" or day not in days:
                continue          # registration is not a lesson
            m = CELL.match(str(cell.value or "").strip())
            if not m:
                continue          # [BRACKETED] non-teaching, EMC/*, blank
            klass, owner = m.group(1), m.group(2)
            if SIXTH_FORM.match(klass):
                continue          # Y12/13: no platform class exists
            if owner in NO_PLATFORM_STAFF:
                continue          # re-enters via RULED_ADDITIONS, owned by BRB
            out.add((owner, klass, days[day], int(period)))
    return out


def emit_sql(sheet_path, year_id):
    rows = read_sheet(sheet_path) | RULED_ADDITIONS
    vals = ",".join(f"('{c}','{k}',{w},{p})" for c, k, w, p in sorted(rows))
    return f"""-- MRB-328 J1: sheet vs platform, expecting ZERO rows back.
with expected(code,cls,weekday,period) as (values {vals}),
-- Guard the BDA assumption. It reports a ROW rather than raising: an earlier
-- draft used 1/0, which Postgres constant-folds at PLAN time, so it fired on
-- every run including the healthy ones. A guard that always cries wolf is no
-- better than one that never does.
guard as (
  select count(distinct te.teacher_id)::int as owners
  from timetable_entries te
  where te.deleted_at is null and te.academic_year_id = '{year_id}'
    and te.teacher_id is not null
    and not exists (select 1 from pending_staff ps
                     where ps.claimed_profile_id = te.teacher_id)
  having count(distinct te.teacher_id) > 1),
platform as (
  select coalesce(ps.staff_code, 'BDA') as code, c.name as cls,
         te.weekday, te.period
  from timetable_entries te
  join classes c on c.id = te.class_id
  left join pending_staff ps
    on ps.id = te.pending_staff_id or ps.claimed_profile_id = te.teacher_id
  where te.deleted_at is null and te.academic_year_id = '{year_id}')
select 'MISSING' as kind, * from (select * from expected
                                  except select * from platform) a
union all
select 'SURPLUS', * from (select * from platform
                          except select * from expected) b
union all
-- Its own branch, so it is evaluated in the healthy case too. Hanging it off
-- SURPLUS would skip it exactly when a silent second owner could slip through.
select 'GUARD: >1 unseeded owner, BDA mapping unsafe', '', '', owners, 0
  from guard
order by 1,2,4,5;
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--year-id", required=True)
    a = ap.parse_args()
    print(emit_sql(a.sheet, a.year_id))
    return 0


if __name__ == "__main__":
    sys.exit(main())
