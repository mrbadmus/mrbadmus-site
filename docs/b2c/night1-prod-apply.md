# MRB-308 Night 1 — production apply and merge runbook

**Nothing in here has been run against production.** Every migration below was
applied to the TEST project (`qeppkiswvclkkwbxmlok`) and verified there. This
file is the recommended order for Mide to approve and run.

Production ref is **`urklkrwevjtlfbwnipjn`** ("mrbadmus", ends in **N**).
Anything ending `...jb` does not exist — if a tool offers it, stop.

---

## Before you start

1. **The consumer flag must be OFF on both sides.** It already is, by default:
   - backend env `CONSUMER_SIGNUP_ENABLED` is unset (absent ⇒ off)
   - the `platform_flags` row is seeded `enabled = false` by migration 4
   With either switch off, no consumer route answers and no consumer page
   renders. Applying these migrations to production therefore changes nothing
   a student, teacher or parent can see. That is the point: the schema can
   land days before the front door opens.

2. **Migration 4 rewrites the live SSO gate.** It is the only genuinely
   risky one. Read its rollback file before applying, not after.

---

## Apply order — one at a time, ref stated in words each time

Apply through `apply_migration`, BEGIN/COMMIT stripped, in exactly this order.
The order is load-bearing twice: migration 3 creates `subscriptions`, which
migration 5 inserts into; migration 4 creates `platform_flags`, which the new
hook reads.

| # | file | what it does | risk |
|---|---|---|---|
| 1 | `20260901214043_mrb308_schools_kind.sql` | adds `schools.kind` (default `school`), the privacy CHECK, one index | **none** — every existing row defaults to `school` |
| 2 | `20260901214113_mrb308_parent_role_and_child_fields.sql` | adds `parent` to the role CHECK; adds `mode`/`intensity`/`created_by`; widens `joined_via` | **none** — all widenings; no existing row can become invalid |
| 3 | `20260901214241_mrb308_subscriptions_and_entitlement.sql` | new `subscriptions` table + RLS + `org_is_entitled()` | **none** — new object, nothing reads it yet |
| 4 | `20260901214325_mrb308_consumer_flag_and_auth_hook.sql` | `platform_flags` + `consumer_signup_enabled()` + **rewrites `hook_before_user_created`** | **THE ONE TO WATCH** — see below |
| 5 | `20260901214441_mrb308_create_family_for_parent.sql` | the atomic family-creation function | **none** — new function, service-role only, nothing calls it while the flag is off |
| 6 | `20260901214558_mrb308_child_accounts.sql` | child attach/update/remove + username check | **none** — same |
| 7 | `20260901215044_mrb308_subscriptions_grants_hardening.sql` | revokes client write grants on `subscriptions`/`platform_flags` | **none** — revoking a grant nobody legitimately uses |

### After migration 4, before going further — verify the SSO gate

This is the check that matters. Run it on production and confirm all five:

```sql
WITH ev(label, e) AS (VALUES
 ('email/password  -> ALLOWED', '{"user":{"email":"x@anywhere.com","app_metadata":{"provider":"email"}}}'::jsonb),
 ('google gmail    -> 403',     '{"user":{"email":"p@gmail.com","app_metadata":{"provider":"google"}}}'::jsonb),
 ('azure gmail     -> 403',     '{"user":{"email":"s@gmail.com","app_metadata":{"provider":"azure"}}}'::jsonb),
 ('azure rainford, no invite -> 403', '{"user":{"email":"nobody@rainford.org.uk","app_metadata":{"provider":"azure"}}}'::jsonb),
 ('google, no email -> 400',    '{"user":{"email":null,"app_metadata":{"provider":"google"}}}'::jsonb))
SELECT label, coalesce(public.hook_before_user_created(e)->'error'->>'http_code','ALLOWED') FROM ev;
```

With the flag OFF (which is how it ships) the results must be exactly:
`ALLOWED, 403, 403, 403, 400`. **`google gmail` must be 403 while the flag is
off.** If it returns ALLOWED, the flag row is wrong — stop and check
`platform_flags`.

Then confirm a real seeded teacher can still be admitted: pick an unclaimed
`pending_staff` email and check the azure branch returns ALLOWED for it.

### Rainford smoke test, after all seven

- A teacher signs in (Microsoft) → lands on classes, sees their classes.
- Open `teacher/today.html` → the timetable renders as before.
- `teacher/admin.html` → loads; the new Consumer accounts card is **hidden**
  because the flag is off.
- A student signs in → their class page and assignment load.
- The leaderboard renders, and the student counts on it are unchanged.

The leaderboard is the one to look at hardest, because it is the only place
the backend change touches existing behaviour. See the caveat below.

---

## The backend

The backend changes are in the paired worktree
`~/Documents/GitHub/mrbadmus-worktrees/b2c/backend`, branch `b2c/launch`.

Deploy order is the standing rule — **backend before frontend**, because the
frontend calls routes that must already exist:

1. merge/push the backend, wait for Render to report Live
2. `python3 build_all.py` in the frontend, then push
3. smoke test

**Do NOT set `CONSUMER_SIGNUP_ENABLED` on Render.** Leave it absent. Night 4
turns it on, after Design's screens land on Night 3.

### ⚠️ The one unverified change

The leaderboard privacy exclusion (four endpoints in `server.js`) **could not
be executed against test**, because `weekly_challenges` and `weekly_scores`
do not exist on the test project — they are production-only. The change is
written to be minimal and is an *exclusion* (it drops only profiles belonging
to a non-school-kind org; profiles with `school_id IS NULL`, which is most of
the 135 students, and Rainford profiles both survive untouched).

Because it is unverified, check the leaderboard **by eye** immediately after
the backend deploys, and compare the number of students shown against the
number shown before. It should be identical: there are no consumer orgs on
production yet, so the exclusion set is empty and the filter is a no-op today.
If the count drops, revert the backend — that would mean the predicate is
inverted.

---

## Merge

The branch `b2c/launch` is clean and merge-ready in both repos. Everything is
additive: new migrations, new `/api/consumer/*` routes, a new `consumer/`
directory, one new Admin card, and two additive edits to `shared/config.js`.
The only edits to existing behaviour are the auth hook and the leaderboard
exclusion, both described above.

**Mide rules on the prod apply and the merge.** Nothing here happens without
that.
