# MRB-293 — Rainford science department setup, 2026-27

A record of the production **data** writes made on 28 Aug 2026. The Supabase CLI
never reads this folder (it only reads `migrations/`), so nothing here re-applies
itself. Every statement is idempotent and safe to re-run by hand.

The **schema** half of this work is two proper migrations, each with a rollback
of the same name under `supabase/rollbacks/`:

- `20260828203900_mrb293_pending_staff_claim_mechanism.sql` — the store, the
  claim function, and the trigger wiring.
- `20260828204639_mrb293_hook_admits_pending_staff.sql` — see **the gate**, below.

⚠️ **Roll back in the reverse order they were applied**: the hook one FIRST. The
live `hook_before_user_created` references `public.pending_staff`, which the other
file drops.

## The gate — the thing that would have made all of this do nothing

`public.hook_before_user_created` is the Supabase Before-User-Created auth hook.
It gates OAuth sign-ups strictly: an on-domain address with no pre-existing
account is refused **unless** it holds a live `school_invitations` row. There
are none, and there never were — the table is empty.

So a seeded teacher pressing "Login with Microsoft" would have been turned away
at the door with

> We could not find a MrBadmusAI account for r.spedding@rainford.org.uk.

and the claim would never have fired, because the auth user is never created.
Verified by calling the hook directly with each of the twelve addresses before
the change: all twelve refused, 403.

The second migration adds one branch: a live, UNCLAIMED `pending_staff` row for
the same school admits, exactly as a `school_invitations` row already did.
After it, all twelve are admitted and everything else is refused as before —
an unknown domain, an on-domain address nobody seeded, and an already-claimed
row all still 403; email/password sign-up still passes straight through.

**Whether that hook is actually registered is a Dashboard setting** (Authentication
→ Hooks) that cannot be read from SQL, so this run could not tell whether it was
live. The change is correct either way: if the hook is registered it was a
blocker and now is not; if it is not registered, the function simply is not
called.

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
