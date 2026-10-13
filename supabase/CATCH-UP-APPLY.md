# Catch-up migration — apply sheet

Branch: `feat/catch-up-migration` · built 14 Oct 2026 · **apply only after Mide says yes.**

| file | what |
|---|---|
| `supabase/migrations/20261014120000_catch_up_recipients.sql` | the migration (additive) |
| `supabase/rollbacks/20261014120000_catch_up_recipients_rollback.sql` | manual undo |

## What it does

1. `assignments.recipient_ids uuid[]` — NULL = whole class (every existing
   row stays NULL); a non-empty array = a catch-up for those pupils only.
   CHECK: 1..60 entries.
2. Restrictive SELECT policy `assignments_catch_up_audience` — a class member
   sees a catch-up only if named in it. No existing policy is rewritten.
   It also hides the catch-up's `assignment_questions` (their pupil branch
   reads `assignments` under RLS).
3. One line, `AND a.recipient_ids IS NULL`, added to three SECURITY DEFINER
   functions so a catch-up never counts in a class figure:
   `class_stars_board_for_member`, `class_stars_leaderboard_for_member`,
   `teacher_class_rollup_v2`. The bodies are production's own, byte-for-byte,
   plus that line.

The site and backend shipped BEFORE this work either way: they probe for the
column, and without it nothing is a catch-up and the Catch-up option is hidden.

## Before applying — production must still hold the bodies this was built from

```sql
select proname, md5(prosrc) from pg_proc
 where pronamespace = 'public'::regnamespace
   and proname in ('class_stars_board_for_member',
                   'class_stars_leaderboard_for_member',
                   'teacher_class_rollup_v2')
 order by 1;
```

Expected (production on 14 Oct 2026):

| function | md5 before |
|---|---|
| class_stars_board_for_member | `c309e0419062699c0962e1ccf5d2e279` |
| class_stars_leaderboard_for_member | `8f5bd0c5d902f6496e36b8bc7acb841b` |
| teacher_class_rollup_v2 | `e33f558df97f6a89e42bd31d778de4d3` |

**If any differs, STOP.** Someone changed that function since; this file
would silently revert their change. Regenerate the migration from the new
body (`gen_mig.py` approach: production body + the one line, anchor matched
exactly once).

## Apply

Production ref `urklkrwevjtlfbwnipjn` — state it before the write. Apply the
migration file's full text (MCP `apply_migration`, name
`catch_up_recipients`, or the SQL editor).

## After applying — verify

```sql
select proname, md5(prosrc) from pg_proc
 where pronamespace = 'public'::regnamespace
   and proname in ('class_stars_board_for_member',
                   'class_stars_leaderboard_for_member',
                   'teacher_class_rollup_v2')
 order by 1;
select policyname, permissive from pg_policies
 where tablename = 'assignments' and policyname = 'assignments_catch_up_audience';
select count(*) filter (where recipient_ids is not null) as catch_ups,
       count(*) as all_rows
  from assignments;
```

| function | md5 after |
|---|---|
| class_stars_board_for_member | `45a942329c57c7c60d46e21896b75bb1` |
| class_stars_leaderboard_for_member | `68d3e80f4445483b634b4a7c9eb05221` |
| teacher_class_rollup_v2 | `2d776cb168442801d3761b57b9b9bb50` |

Policy row: `RESTRICTIVE`. `catch_ups` = 0.

(These were measured on TEST after applying there on 14 Oct 2026: identical
md5s — the connector kept the comments.)

**Then restart the Render backend** (Manual Deploy → "Restart service" is
enough). The backend's `catchUpSupported()` probe caches "absent" from the
moment it first runs; a restart makes it look again. Until then teachers
won't see the Catch-up option. The pages need no redeploy — they probe on
every load.

## Classmate proof (optional, read-only — everything rolls back)

The proof run on TEST, 8X1, 14 Oct 2026: a `DO` block inserts a catch-up for
one pupil, switches `role authenticated` + `request.jwt.claims` to each
viewer, counts, then `RAISE EXCEPTION` so the whole transaction is undone.
Result: **recipient 1 assignment / 1 question · classmate 0 / 0 · teacher
1 / 1.** The same block is in `docs/catch-up/REPORT.md` on the site branch.

## ⚠️ Ordering hazards

- `feat/x-mig-pupil-class` (stars functions) and `feat/mrb351-migrations`'
  `20260927100000_mrb351_rollup_v2_live_results_kinds.sql` are ALREADY live
  on production (bodies match by md5). **Never re-run either after this
  migration** — each would quietly remove the catch-up line, and catch-ups
  would start counting in class figures again.
- A future migration that redefines any of the three functions must keep
  `AND a.recipient_ids IS NULL`.

## Rollback

`supabase/rollbacks/20261014120000_catch_up_recipients_rollback.sql`, by hand.
It soft-deletes every catch-up FIRST (`deleted_at = now()`): without the
column a catch-up would look like class homework and appear to the whole
class. Then it restores the three functions to the "before" bodies above and
drops the policy, the constraint and the column.

TEST: applied 14 Oct 2026 as version `20261013235431` (the connector stamps
its own version). TEST's stars-leaderboard and rollup v2 were older than
production's; applying brought both up to production's bodies plus the line.
