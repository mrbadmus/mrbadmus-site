# The `b2c/launch` worktree — orientation

⊕ This started life inside the repo root `README.md`, which was wrong: that
file is a one-line stub on `main`, and a root README announcing "you are in the
b2c/launch worktree" would have been false on `main` the moment this branch
merged. It lives here instead, where it can merge harmlessly and still be found
by anyone opening this checkout cold.

### What this branch is

**MRB-308 — B2C Launch: parents, home educators, councils.** The estate has
only ever had one kind of customer: a school with a timetable. This branch
adds two more — a family (one paying parent, their children as members) and an
organisation (a council or service, caseworkers, no timetable) — without a
second org table and without a synthetic consumer school. One column,
`schools.kind`, carries the distinction.

### The other half is in a separate worktree

The backend is a **different repository**, and it has its own worktree on a
branch of the same name:

| | path | branch |
|---|---|---|
| frontend (here) | `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/launch` | `b2c/launch` |
| backend | `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend` | `b2c/launch` |

They ship together. A change to `/api/consumer/*` that lands on one side alone
is a student- or parent-visible error, exactly as `CLAUDE.md` describes for the
main API contract.

### Running the backend: PORT 3100

The local backend for **this** worktree runs on **port 3100**, not 3000.

Main's backend already uses 3000, and the point of the split is that both can
run at the same time — you can have the live estate and the consumer build up
side by side without stopping one to look at the other. If you start this one
on 3000 it will either refuse to bind or, worse, quietly shadow the other.

### CONSUMER_SIGNUP_ENABLED is OFF, in TWO places

Consumer signup is behind **two independent switches, and both default to off.
Both must be on before any consumer surface works.**

| switch | where | guards |
|---|---|---|
| `CONSUMER_SIGNUP_ENABLED` | backend env var | the `/api/consumer/*` routes and the pages |
| `consumer_signup_enabled` | `public.platform_flags` row, on TEST | **account creation** — read by `hook_before_user_created` |

They are separate because a Postgres auth hook cannot read a backend env var.
The database needs its own copy or the SSO gate has nothing to consult. They
are ANDed rather than reconciled: **either one being off means off.**

⚠️ Flipping only the env var gets you routes that answer and a signup that is
still refused at the door with a 403. Flipping only the DB row gets you the
reverse. Flip both, or neither.

### Schema state: TEST only

All MRB-308 schema work is on the **TEST project, ref `qeppkiswvclkkwbxmlok`**.

**Nothing has been applied to production** (`urklkrwevjtlfbwnipjn`). The seven
migrations in `supabase/migrations/20260901*` were applied to TEST via
`apply_migration` and then recovered onto disk byte-for-byte from
`supabase_migrations.schema_migrations`, so the repo and the TEST database
agree exactly. Each has a hand-apply undo in `supabase/rollbacks/` under the
same filename; those are applied in **reverse order** and several of them say
so at the top, because the order is load-bearing.

### Never push from here

**Do not `git push` from this worktree. Mide pushes.** Commit freely; leave the
publishing to him.
