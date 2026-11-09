# Widening `self_ticks` for a child's level pick

**Why.** `POST /api/consumer/child/self-ticks` now takes `level`, the value of the level a
child picked, and keeps it in `child_answers.self_ticks` as one entry of 100 + value, beside the
page's positions. The column's CHECK, `child_answers_self_ticks_range`, allows only 1–20 and 20
entries, so the database refuses that entry.

**Until this is applied.** Nothing breaks and nothing is lost: the route catches the refusal
(23514), saves the ticks without the level, logs one line and answers `level: null`. The parent
reads "Ticked N of M" and no level, as they do today.

**Apply: TEST first, production at merge time** (CLAUDE.md, "When a migration may touch
PRODUCTION"). It takes a brief lock and rewrites nothing. Rehearsed on TEST inside a transaction
and rolled back, 9 Nov 2026; TEST and production are both still at the old CHECK.

```sql
alter table public.child_answers drop constraint child_answers_self_ticks_range;
alter table public.child_answers add constraint child_answers_self_ticks_range
  check (self_ticks is null or (cardinality(self_ticks) <= 21 and 1 <= all(self_ticks) and 109 >= all(self_ticks)));
```

The route itself allows a tick only from 1 to 20 and a level only from 0 to 9, so 21–99 can't be
written through it. Rollback: put the 1–20 and 20-entry CHECK back after removing any entry of 100
or more from `self_ticks`.

After applying, record it as a migration file under `supabase/migrations/`, named by the version
production records.
