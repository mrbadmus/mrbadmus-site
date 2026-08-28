# MRB-293 — Rainford science department setup, 2026-27

A record of the production **data** writes made on 28 Aug 2026. The Supabase CLI
never reads this folder (it only reads `migrations/`), so nothing here re-applies
itself. Every statement is idempotent and safe to re-run by hand.

The **schema** half of this work is a proper migration:
`supabase/migrations/20260828203900_mrb293_pending_staff_claim_mechanism.sql`,
rolled back by the file of the same name under `supabase/rollbacks/`.

| file | what it did |
|---|---|
| `01_classes.sql` | created the 57 missing 2026-27 classes (69 total, 12 already existed) |
| `02_pending_staff.sql` | seeded the 12 teachers, keyed on email |
| `03_pending_staff_classes.sql` | their 99 class assignments (Mide's own 12 links were already live and were not touched) |
| `04_pending_staff_scopes.sql` | school_admin on claim for SPD and HTJ |
| `05_verify_pinned_table.sql` | proves the live per-class teacher map equals the pinned timetable exactly; returns zero rows when correct |

Source of truth was the **per-teacher grid** (rows 2–15) of
`26:27 Timetable/Science TT 2026-27.xlsx`, not the summary block below it —
the summary transposes 7h/Sc3 and 7h/Sc4's second teachers, carries the typo
"JSK" for JKS, and lists BMT on 8r/Sc3. Mide ruled the grid authoritative and
BMT out of scope.

Nothing here emails anybody. A seeded teacher becomes real the first time they
sign in with Microsoft.
