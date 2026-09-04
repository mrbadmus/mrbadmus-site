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

### Night 2 (MRB-309…315) — what landed on this side

Night 2 is the billing, the weekly scheduler, chat, unit checks, the termly
report, exam marking, email and the caps. Most of it is backend; what it left
in **this** worktree is:

**Eleven more migrations**, all applied to TEST and recovered onto disk the
same way the Night 1 seven were:

```
supabase/migrations/20260901230755_mrb309_access_state_and_stripe_columns.sql
supabase/migrations/20260901230804_mrb309_stripe_events.sql
supabase/migrations/20260901230828_mrb310_child_plans_and_work_items.sql
supabase/migrations/20260901230851_mrb311_family_messages.sql
supabase/migrations/20260901231055_mrb312_unit_checks_and_report_notes.sql
supabase/migrations/20260901231121_mrb313_exam_questions_and_answers.sql
supabase/migrations/20260901231202_mrb314_email_log_notifications_prefs.sql
supabase/migrations/20260901231304_mrb315_ai_usage_and_limits.sql
supabase/migrations/20260901231338_mrb310_platform_settings_and_cron.sql
supabase/migrations/20260901234536_mrb310_ks4_scheme_week_ceiling.sql
supabase/migrations/20260901234730_mrb310_org_staff_attach_and_seat_cap.sql
supabase/migrations/20260902001003_mrb309_stamp_org_lock.sql
```

⊕ The paragraph above that says *"the seven migrations in
`supabase/migrations/20260901*`"* is Night 1's count and is now stale — there
are **twenty**, nine from Night 1 and eleven from Night 2. Everything else it
says still holds: TEST only, nothing on production, each with a hand-apply undo
in `supabase/rollbacks/` applied in **reverse order**.

**Two seeds.**

- `supabase/seeds/20260902001000_ks4_default_sequence.sql` — the KS4 scheme of
  work, four blocks (tier × pathway, board `AQA`), generated by
  `ks4_seed_sow.py` from the KS4 generator's own subtopic order. This is what
  gives a Year 10 or 11 child a position and a weekly lesson; without it the
  scheduler has nothing to point at above KS3.
- **`exam_questions` is seeded from the BACKEND**, not from here:
  `node scripts/seed-exam-questions.js` in the backend worktree, which reads
  the frontend repo's `shared/exam-content/*.js` for the `bonding_v2` items.
  There is no seed file for it in `supabase/seeds/`.

**Two Python scripts, both one-shot generators rather than build steps** — they
are NOT wired into `build_all.py` and must be run by hand when their source
changes:

- `ks4_seed_sow.py` — writes the KS4 seed above.
- `export_ks3_extended.py` — exports KS3 content the backend cannot reach
  (the backend has no access to `ks3_data/`).

**The policy matrix grew a Section E.**
`supabase/tests/0011_mrb308_consumer_policy_matrix.sql` now runs five sections;
the new one reads:

> `SECTION E — NIGHT 2 (MRB-309…315): access states, guardianship, chat
> sealing, and every new table sealed the same way as the old ones.`

Night 1 proved the family is sealed at the schema Night 1 built. Section E
proves the same of what Night 2 added: the access states, `guardian_of_child()`,
the chat send policy (including that a **locked** family's parent is refused at
the policy, not merely at the 423), and every new table —
`work_items`, `child_plans`, `family_messages`, `unit_check_attempts`,
`exam_answers`, `email_log`, `consumer_notifications`, `ai_usage_events` —
driven as a member of the *other* family and as a Rainford teacher, and refused
both times.

**The consumer pages** now under `consumer/`:

```
consumer/signup.html            consumer/verify.html
consumer/overview.html          consumer/add-child.html
consumer/child.html             consumer/account.html
consumer/checkout-return.html
consumer/child-login.html       consumer/today.html
consumer/exam.html              consumer/unit-check.html
consumer/report.html
consumer/consumer-common.js     consumer/consumer.css
```

`consumer-common.js` holds the shared plumbing — the API base, the session, and
`guard(access, who)`, which returns `{ state, writable, title, message }` for a
page to disable its submit, send and mark controls with. It takes either a bare
state word or a whole response object; ⚠️ on the family payload **both**
`billing.state` and `billing.access` exist and only `access` is the permission,
so it reads `access` first. An access word it has never seen refuses rather
than admits. `who` picks the parent or the child wording.

That is a courtesy layer only: **the backend refuses the same writes with 423
`org_locked`, and the RLS policies refuse them again underneath that.** Never
treat the frontend guard as the enforcement.

### Night 3 (MRB-317 / MRB-318) — what landed on this side

Design's nineteen surfaces compiled onto the Night 1–2 plumbing. Three new
page trees, each behind `CONSUMER_SIGNUP_ENABLED` exactly like `consumer/`, and
each copied and round-tripped by `generate_site_v5.py` (they are on its
safety-net list — a file added to one of them that the build has not seen is a
loud abort, not a silent deletion):

```
parents/   the public front door — index, how-it-works, pricing, home-education, sign-in
go/        the child's login at mrbadmus.com/go
org/       organisation staff — sign-in, index (the dashboard)
consumer/  Design's parent + child app (signup, verify, checkout-return, overview,
           account, report, today, exam, unit-check); add-child, child and
           child-login RETIRED
teacher/admin.html   Design's Admin Accounts + Marking Queue inside the consumer card
```

**Design system:** nothing from her `_ds/` bundle is vendored. Her token files
are byte-identical to `shared/tokens.css` and `shared/ks3.css` apart from font
URL prefixes, so every consumer page loads those two plus `consumer/consumer.css`
with `class="rd" data-mode="ks3"` on the root. The admin dark-room `--st-*`
tokens are inlined in `teacher/admin.html`.

**Three more migrations**, applied to TEST and recovered onto disk the same way:

```
supabase/migrations/20260902053725_mrb317_account_deletion_requests.sql
supabase/migrations/20260902053731_mrb318_classes_consumer_kind.sql
supabase/migrations/20260902070608_mrb317_parent_update_child_pathway.sql
```

**Gate 0011 grew a Section F** (the deletion ledger is sealed; `consumer_kind`
is constrained and NULL on every school class). **Gate 0001's B11.1 was
rewritten**: it asserted an EMPTY scheme of work, a Stage-1 fixture assumption
that had silently become a test of the seed; it now asserts a student sees every
row.

**Two commander harnesses** for the built tree: `night3_selfreview.py`
(flag-off zero-request sweep, Rainford regression, cold greps) and
`night3_flagon_smoke.py` (real sessions over `mrbadmus_site/` with the flag
turned on for that browser only, by a setter on `window.MrBadmusConfig`).
Both serve on a port the backend's CORS allowlist knows (5500), or one named in
`EXTRA_CORS_ORIGINS` on the backend instance.

**The flag is off in all three places** (`shared/config.js` both blocks, the
backend `.env`, the `platform_flags` row). Turning it on for a drive means the
DB row AND `CONSUMER_SIGNUP_ENABLED=true` on the backend's command line — never
edit `.env` — AND either the config block or the browser-side setter.

The runbook is `docs/b2c/night3-prod-apply.md`; the executor contract for the
backend additions is `docs/b2c/night3-api.md` (superseded where it disagrees
with `API-CONTRACT.md` §v3.6).
