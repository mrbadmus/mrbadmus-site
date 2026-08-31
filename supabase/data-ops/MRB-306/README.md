# MRB-306 WS-1 — timetable seed (31 Aug 2026)

The 2026-27 science timetable, seeded from the school's own grid into
`public.timetable_entries`.

## Source

`26:27 Timetable/Science TT 2026-27.xlsx` (repo root; the folder name has a
colon on disk, not a slash). Rows 2–15 are the per-teacher grid; columns B–AE
are `Day:Period`, five teaching periods a day plus a `Reg` column.

`parse_timetable.py` is the exact parser used. Re-running it reproduces the
204 rows deterministically.

## What was seeded, and what was not

| | count |
|---|---|
| Cells with content in the grid | 385 |
| **Seeded** | **204** |
| Skipped: the `Reg` column (registration, never a lesson) | 56 |
| Skipped: `[BRACKETED]` non-teaching (PPA, MAN, INTER, LLEAD, ECT, MENTOR, COVER, BLANK, form groups) | 89 |
| Skipped: Y12/13 classes (ruled out) | 31 |
| Skipped: `EMC/*` enrichment slots | 4 |
| Skipped: teacher BMT (ruled out) | 1 |

204 + 56 + 89 + 31 + 4 + 1 = 385, so every cell in the grid is accounted for
in exactly one category.

Every skipped cell was inspected by value, not by assumption — the full
distinct-value list was reviewed to confirm no real KS3/KS4 lesson was dropped.

## Verification (both directions)

The seed was dry-run before insertion: 204 rows in, 204 classes resolved,
0 unresolved, 0 rows with both owners set, 13 teachers, 69 distinct classes.

After insertion the per-teacher and per-weekday counts were read back from the
database and compared against an INDEPENDENT recount from the spreadsheet.
They match exactly:

| code | entries | classes | Mon | Tue | Wed | Thu | Fri |
|---|---|---|---|---|---|---|---|
| BDA | 21 | 12 | 5 | 4 | 5 | 4 | 3 |
| BLF | 14 | 8 | 2 | 4 | 3 | 2 | 3 |
| BRB | 17 | 9 | 4 | 3 | 4 | 3 | 3 |
| ELV | 12 | 8 | 4 | 2 | 4 | 2 | 0 |
| FNL | 17 | 10 | 4 | 3 | 3 | 2 | 5 |
| HRS | 17 | 8 | 4 | 4 | 3 | 3 | 3 |
| HTJ | 13 | 6 | 1 | 4 | 2 | 4 | 2 |
| JKS | 12 | 8 | 3 | 2 | 3 | 2 | 2 |
| MKB | 16 | 8 | 4 | 3 | 2 | 4 | 3 |
| RNN | 18 | 10 | 4 | 4 | 4 | 3 | 3 |
| SPD | 16 | 9 | 4 | 2 | 4 | 3 | 3 |
| SRE | 18 | 8 | 5 | 4 | 0 | 5 | 4 |
| WKN | 13 | 7 | 0 | 4 | 2 | 4 | 3 |
| **total** | **204** | 69 | | | | | |

The three zeroes are real, not gaps: ELV has no Friday teaching, SRE no
Wednesday, WKN no Monday — all `[BLANK]` blocks in the source grid.

## Ownership

Mide (`BDA`) is the only CLAIMED teacher, so his 21 entries attach directly to
his live profile. The other 183 attach to `pending_staff` rows and move to a
real profile on first Microsoft sign-in, via `claim_pending_staff()` — the same
mechanism, and the same moment, as the class links.

## Nothing existing was touched

The seed only INSERTS into a table created in the same run. No class,
class_teacher, pending_staff, profile, student or submission row was modified.
