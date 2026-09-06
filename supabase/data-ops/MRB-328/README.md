# MRB-328 J1 — BMT's lesson becomes BRB's

## The ruling

The fresh departmental sheet codes one lesson to **BMT**: `8r/Sc3`, **Wed P4**.
MRB-306 skipped it and MRB-326 flagged it, both for the same reason — there is
no `pending_staff` row for BMT, so the code can own nothing, and creating staff
needs an email only Mide can supply.

Mide ruled it on 6 Sep 2026: the slot becomes **BRB's**, who owns that class by
the standing ruling. He already teaches `8r/Sc3` twice (Mon P4, Thu P3); the
sheet's own class-summary row reads `8r/Sc3 | BRB | BMT | BRB`, so all three of
that class's lessons now sit with one teacher.

## What was written

One row in `timetable_entries` on **production**:

| field | value |
|---|---|
| class | `8r/Sc3` |
| owner | `pending_staff` BRB (unclaimed) |
| weekday / period | 3 / 4 — Wednesday P4 |
| `week_cycle` | `null` (the school runs no A/B cycle) |
| `source` | **`manual`** |

`source` is `manual`, not `seeded`, and that is the point: `seeded` means "came
from the sheet's staffing", and this row deliberately did not. It is the one
entry on the platform with no counterpart in the sheet's own columns.

## Verification

`verify_timetable_sheet.py` emits one SQL statement that set-differences the
sheet against the platform server-side. **It returned zero rows**: no lesson on
the sheet is missing from the platform, and no lesson on the platform is absent
from the sheet — with BRB's Wed P4 accounted for as `RULED_ADDITIONS`, not as a
surplus. All 13 teachers are zero-diff.

```bash
python3 verify_timetable_sheet.py \
    --sheet 'Timetable/Science TT 2026-27.xlsx' \
    --year-id <academic_year_id> > diff.sql
# then run diff.sql against prod; expect zero rows
```

The sheet carries real staff names, so it stays untracked and its path is an
argument. Only three-letter codes appear in this folder.

### The slot-guard was proved live, not merely absent

An insert passing is not on its own evidence that anything checked it. A second
insert into the same slot was attempted inside a `DO` block that traps `23505`:
it was refused, the block caught it, and the live row count at Wed P4 stayed at
**1**. So `timetable_entries_slot_guard` is running and it accepted this row on
merit.

### Two traps this check walked into first

**Resolving a code to an owner needs both directions.** An entry is owned either
by a `pending_staff` row (unclaimed) or by a `profile` (claimed, since MRB-293).
Joining only on `pending_staff_id` silently drops every claimed teacher.

**And even both directions miss BDA.** He was a real profile before the
pending-staff seeding ever ran, so no `pending_staff` row carries his code. The
first run of this check reported **21 missing lessons** — the whole of one
teacher's timetable — when nothing whatever was wrong. The query now maps
"owned by a profile no `pending_staff` row claims" to BDA, and carries a guard
that reports a row if a second such owner ever appears, because at that point
the mapping would quietly pool two teachers under one code.

The guard reports a row rather than raising. An earlier draft used `1/0`, which
Postgres constant-folds at **plan** time — so it fired on every run, healthy
ones included. A guard that always cries wolf is no better than one that sleeps.
