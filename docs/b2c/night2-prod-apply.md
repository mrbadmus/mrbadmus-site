# MRB-309…315 Night 2 — production apply and merge runbook

**Nothing in here has been run against production.** Every migration below
was applied to the TEST project (`qeppkiswvclkkwbxmlok`) and verified there.
This extends `night1-prod-apply.md`; Night 1's nine migrations must already be
on production before any of these.

Production ref is **`urklkrwevjtlfbwnipjn`** ("mrbadmus", ends in **N**).

---

## Before you start

1. **The consumer flag stays OFF in all three places** — `shared/config.js`
   (both environments), the backend env `CONSUMER_SIGNUP_ENABLED` (absent on
   Render), and the `platform_flags` row. Every Night 2 route is behind
   `consumerGate` except the Stripe webhook, which answers 400 to anything
   without a valid signature. The cron jobs are scheduled but call a URL that
   is NULL until you set it, so they fire and do nothing.

2. **Two migrations change Night 1 behaviour, deliberately.** Migration 1
   makes a `trialing` row entitled only while `trial_end` is ahead (Night 1
   admitted a trial with no end forever), and makes `create_family_for_parent`
   start a family at status `none` — no trial until Stripe checkout with a
   card. No production family exists yet, so no row is affected.

3. **Migration 9 installs two extensions** (`pg_cron`, `pg_net`) and schedules
   five jobs. Both are Supabase-supported; neither touches an existing table.

---

## Apply order — one at a time, ref stated in words each time

Apply through `apply_migration`, BEGIN/COMMIT stripped, in exactly this order.
The order is load-bearing: 3 defines `consumer_touch_updated_at()` and
`work_items`, which 5 and 6 reference; 1 defines `guardian_of_child()` and
`org_access_state()`, which every later policy calls.

| # | file (`supabase/migrations/`) | what it does | risk |
|---|---|---|---|
| 1 | `20260901230755_mrb309_access_state_and_stripe_columns.sql` | `org_access_state()`; `org_is_entitled()` redefined on top of it; Stripe columns on `subscriptions`; status `none`; `create_family_for_parent` starts at `none`; `guardian_of_child()`, `profile_consumer_org()` | **read first** — replaces two Night 1 functions |
| 2 | `20260901230804_mrb309_stripe_events.sql` | webhook idempotency ledger | none |
| 3 | `20260901230828_mrb310_child_plans_and_work_items.sql` | `child_plans`, `work_items`, `work_generation_runs` | none |
| 4 | `20260901230851_mrb311_family_messages.sql` | chat table, `family_message_allowed()`, RLS, two RPCs, joins the realtime publication | none — **verify the publication exists first** (see below) |
| 5 | `20260901231055_mrb312_unit_checks_and_report_notes.sql` | `unit_check_attempts`, `report_notes`, `child_flashcard_queue` | none |
| 6 | `20260901231121_mrb313_exam_questions_and_answers.sql` | `exam_questions`, `exam_answers`, `mb_quota_used()` | none |
| 7 | `20260901231202_mrb314_email_log_notifications_prefs.sql` | `email_log`, `consumer_notifications`, `parent_prefs` | none |
| 8 | `20260901231304_mrb315_ai_usage_and_limits.sql` | `ai_usage_events`, `org_limits`, `ai_usage_counts()` | none |
| 9 | `20260901231338_mrb310_platform_settings_and_cron.sql` | `platform_settings` + defaults; `pg_cron`, `pg_net`; `consumer_cron_call()`; five jobs | **installs extensions** |
| 10 | `20260901234536_mrb310_ks4_scheme_week_ceiling.sql` | `scheme_of_work_entries.academic_week` CHECK: 1..52 at KS4 (KS3 stays 1..39) | none — widening; needed before the KS4 seed |
| 11 | `20260901234730_mrb310_org_staff_attach_and_seat_cap.sql` | `attach_child_to_family()` admits organisation staff and enforces the seat cap | **read first** — replaces a Night 1 function |
| 12 | `20260902001003_mrb309_stamp_org_lock.sql` | `stamp_org_lock()` — `locked_at` maintained in one statement (a webhook race left it stale) | none — new function, service role only |

⚠️ **Three OLDER migrations were missing from the TEST project and were
applied there tonight to match production** — `20260820140008` (attempt
letters), `20260820212314` (one assignment per class per week),
`20260821115157` (submission/attempt uniqueness). Production already has
all three; nothing to do there. They are noted so that the TEST ledger's
extra rows do not read as Night 2 work.

Each has a rollback of the same name in `supabase/rollbacks/`. Roll back in
reverse order (12→1); 5 and 6 reference `work_items`, so 3 cannot be rolled
back before them.

### Before migration 4 — the realtime publication

```sql
select pubname from pg_publication where pubname = 'supabase_realtime';
```
Production should already have it (Supabase creates it). The migration
creates it if absent, which is safe, but you want to know which happened.

### After migration 1 — the state helper, five cases

```sql
select public.org_access_state(id) from public.schools where code = 'RHS';  -- must be 'full'
select public.org_is_entitled(id)  from public.schools where code = 'RHS';  -- must be true
select public.org_access_state(null);                                        -- 'locked'
select public.org_access_state('00000000-0000-0000-0000-00000000dead');      -- 'locked'
select count(*) from public.subscriptions where status = 'none';             -- 0 today; that is fine
```
If Rainford is anything but `full`, stop.

### After migration 9 — the clock is armed but unloaded

```sql
select jobname, schedule, active from cron.job where jobname like 'consumer_%';  -- 5 rows
select key, value from public.platform_settings;                                 -- cron_target_url and cron_secret are null
select public.consumer_cron_call('/x');                                          -- returns NULL (no-op)
```

### Seeds (data, not migrations — apply after 9)

| seed | what | how |
|---|---|---|
| `exam_questions` | the question pool (`code_seed` 15 KS4 authored by Code — **review before launch**; `bonding_v2`; `ks3_ladder`) | `node scripts/seed-exam-questions.js` in the backend with production env, once |
| `supabase/seeds/20260902001000_ks4_default_sequence.sql` | KS4 default sequence rows in `scheme_of_work_entries` (tier × pathway, AQA) | SQL editor, once; idempotent |

Neither is needed for the schema to be healthy; both are needed before a
family sees work.

### Rainford smoke test, after all nine

Same as Night 1 (teacher signs in, today, admin with the Consumer card hidden,
student class page, leaderboard count unchanged). Nothing on Night 2 touches
a school-kind path: `org_access_state` short-circuits on `kind='school'`, the
cap middleware skips schools unless `org_limits.enforce` is set, and the
rate limiters are mounted on `/api/consumer/*` only (the AI-route limiter is
60/hour per user on `/api/chat` — that is the one change a school user could
meet, and it is above the existing 60/hour per IP).

---

## Render environment (backend), before the backend deploy

| var | value | needed for |
|---|---|---|
| `STRIPE_SECRET_KEY` | **live** key (Mide swaps at launch; test key until then) | checkout, portal, quantity sync |
| `STRIPE_API_VERSION` | optional; defaults to `2026-08-26.dahlia` in code — the account's Managed Payments rejects the SDK's older default, and the webhook object shape differs | everything Stripe |
| `STRIPE_WEBHOOK_SECRET` | from the Stripe dashboard webhook endpoint pointing at `https://mrbadmus-backend.onrender.com/api/consumer/stripe/webhook` | signature verification |
| `STRIPE_PRICE_MONTHLY`, `STRIPE_PRICE_ANNUAL`, `STRIPE_PORTAL_CONFIG` | from `node scripts/stripe-setup.js` run against the live account | checkout, portal |
| `CONSUMER_CRON_SECRET` | random; **must equal** `platform_settings.cron_secret` | cron endpoints |
| `FRONTEND_ORIGIN` | `https://mrbadmus.com` | return URLs, email links |
| `RESEND_API_KEY` | from Resend (domain `mrbadmus.com` verified) | real sends; absent = dry-run rows only |
| `ANTHROPIC_API_KEY` | already on Render | AI marking (absent = stub marker) |
| `UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN` | optional; absent = in-memory limiter | shared rate limits |
| `CONSUMER_SIGNUP_ENABLED` | **leave absent** | the front door |

Then, in the SQL editor on production, to arm the clock:
```sql
update public.platform_settings set value = to_jsonb('https://mrbadmus-backend.onrender.com'::text) where key = 'cron_target_url';
update public.platform_settings set value = to_jsonb('<the same secret as CONSUMER_CRON_SECRET>'::text) where key = 'cron_secret';
```
Do this LAST, after the backend is live. Until then every firing is a no-op.

⚠️ **Two Stripe rulings for Mide before live mode.** (1) The product carries
tax code `txcd_20060058` ("Training Services – Self-study Web-based"):
this account has Managed Payments on and Checkout refuses a product with no
tax code, so one had to be set to check out at all. Whether that code is
right for a non-VAT-registered seller is Mide's and the accountant's call.
(2) `scripts/stripe-setup.js` must be re-run against the LIVE account to
create the product, prices and portal configuration there; it refuses to run
on a non-`sk_test_` key by default — flip that guard deliberately.

Stripe dashboard: register the webhook endpoint for the events
`checkout.session.completed`, `customer.subscription.created`, `.updated`,
`.deleted`, `invoice.paid`, `invoice.payment_failed`,
`customer.subscription.trial_will_end`.

---

## Deploy order

1. Migrations 1→9 on production, verifying after 1, 4 and 9 as above.
2. Seeds (exam questions, KS4 sequence).
3. Backend: merge `b2c/launch`, push, wait for Render "Live". `/api/health`
   now reports `stripe`, `limits` and `email` modes — read it.
4. `python3 build_all.py`, push the frontend.
5. Arm the clock (the two `platform_settings` updates).
6. Rainford smoke test.
7. Leave the flag off. Night 4 turns it on.

**Mide rules on the prod apply and the merge.** Nothing here happens without
that.
