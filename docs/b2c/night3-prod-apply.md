# MRB-317 / MRB-318 Night 3 — production apply, merge order, and the flag-on checklist

**Nothing in here has been run against production.** Everything below was
applied to and driven on the TEST project (`qeppkiswvclkkwbxmlok`). This
extends `night1-prod-apply.md` (nine migrations) and `night2-prod-apply.md`
(twelve). Both of those must be on production before anything here.

Production ref is **`urklkrwevjtlfbwnipjn`** ("mrbadmus", ends in **N**).

**Mide rules the prod apply, the merge, and the flag. Nothing here happens
without that.**

---

## 1. What Night 3 adds

- **Pages.** `parents/` (public front door), `go/` (child login at
  mrbadmus.com/go), `org/` (organisation staff), Design's versions of every
  `consumer/` page, and Design's Admin Accounts + Marking Queue inside
  `teacher/admin.html`. All behind `CONSUMER_SIGNUP_ENABLED`; with it off every
  one renders "Not found" and makes no request. Cloudflare Pages serves the
  new directories the moment `mrbadmus_site/` carries them — no Pages setting
  changes.
- **Backend.** `consumer/org.js`, `consumer/admin.js`, `consumer/account.js`,
  `GET /api/consumer/pricing`, the email transcription, the marker's best-fit
  line. Contract: `API-CONTRACT.md` §v3.6.
- **Schema.** Two migrations (below). One reseed (the KS3 tariff).

## 2. Migrations — two, one at a time, ref stated in words

| # | file (`supabase/migrations/`) | what it does | risk |
|---|---|---|---|
| 13 | `20260902053725_mrb317_account_deletion_requests.sql` | the deletion-request ledger (30-day grace), RLS read-own-org, service-role writes | none — new table |
| 14 | `20260902053731_mrb318_classes_consumer_kind.sql` | `classes.consumer_kind` (`child` / `group` / NULL for every school class) + backfill of consumer per-child classes | none — nullable column; the backfill touches 0 rows on prod today |
| 15 | `20260902070608_mrb317_parent_update_child_pathway.sql` | `parent_update_child` gains `p_pathway` (Route on child settings); drops the seven-argument overload | **read first** — replaces a Night 1 function; the backend's PATCH sends the new argument, so backend and migration ship together |

Rollbacks of the same names in `supabase/rollbacks/`, reverse order (15 → 13).
The rollback for 14 soft-deletes group classes first — read it.

After 14, verify:
```sql
select count(*) from public.classes c join public.schools s on s.id=c.school_id
 where s.kind='school' and c.consumer_kind is not null;   -- must be 0
```

## 3. Seeds — the KS3 tariff (Mide's ruling, MRB-313)

`explain` = 4 marks, `produce` = 6. Re-run the exam-question seeder once on
production so the pool carries the new tariff (idempotent upsert on `id`):

```bash
cd mrbadmus---backend && FRONTEND_REPO=/path/to/mrbadmus-site node scripts/seed-exam-questions.js --only ks3_ladder
```
Verify: `select marks, count(*) from exam_questions where source='ks3_ladder' group by 1;` → 4: 185, 6: 185.

## 4. Gates run on TEST tonight

| gate | result |
|---|---|
| 0001 Stage 1 RLS | **37/37** (B11.1 rewritten: it asserted an EMPTY scheme of work, a Stage-1 fixture assumption; it now asserts the student sees every row — 1050/1050) |
| 0011 consumer matrix + **Section F** (deletion ledger sealed; `consumer_kind` constrained; school classes untouched) | **171/171**, 11 new Section F rows all green |
| `verify_answer_positions.py` (MRB-278) | (filled in by the morning report) |
| `build_all.py` | (filled in by the morning report) |

## 5. Render environment (backend) — every variable the flag-on needs

"Current" is what the b2c backend worktree's `.env` holds tonight (TEST
values; secrets not shown). "Prod" is what Render must hold before Night 4.

| variable | needed for | current (worktree .env) | prod before flag-on |
|---|---|---|---|
| `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE_KEY` / `SUPABASE_ANON_KEY` | everything; **anon key is required for child login** | present (TEST project) | present on Render already for the first two; **check `SUPABASE_ANON_KEY` is set** (child login 500s without it) |
| `CONSUMER_SIGNUP_ENABLED` | the front door (backend half) | `false` | **leave absent until Night 4**, then `true` |
| `STRIPE_SECRET_KEY` | checkout, portal, quantity sync, extend-trial | present (`sk_test_…`) | **live key** — Mide swaps at launch |
| `STRIPE_WEBHOOK_SECRET` | webhook signature | present | from the dashboard endpoint `https://mrbadmus-backend.onrender.com/api/consumer/stripe/webhook` |
| `STRIPE_PRICE_MONTHLY` / `STRIPE_PRICE_ANNUAL` / `STRIPE_PORTAL_CONFIG` | checkout, portal | present (test-mode ids) | re-run `scripts/stripe-setup.js` against the LIVE key (it refuses non-`sk_test_` by default — flip deliberately) and paste the three ids |
| `STRIPE_API_VERSION` | optional; code defaults to `2026-08-26.dahlia` | missing (default used) | leave absent |
| `CONSUMER_CRON_SECRET` | the three cron routes | present | random; must equal `platform_settings.cron_secret` |
| `FRONTEND_ORIGIN` | return URLs, every email link (`/go`, `/consumer/…`) | `http://localhost:8000` | `https://mrbadmus.com` |
| `RESEND_API_KEY` | real email; absent = dry-run rows | **missing** | **required for launch** — E2–E8 and the deletion email; domain `mrbadmus.com` verified in Resend |
| `ANTHROPIC_API_KEY` | AI marking (absent = stub marker, flagged `provider:'stub'`) | **missing locally** | already on Render for `/api/chat`; the marker uses the same key |
| `MARK_PROVIDER` | force `stub` | missing | leave absent |
| `UPSTASH_REDIS_REST_URL` / `_TOKEN` | shared rate limits across instances | **missing** | optional on one Render instance; Night 2 open item 6 says "before launch" |
| `ANTHROPIC_MODEL` | model for chat + marking | missing (default `claude-sonnet-4-6`) | leave absent |
| `EXTRA_CORS_ORIGINS` | comma-separated extra CORS origins for local static servers (Night 3) | unset | **leave absent** — production's allowlist stays byte-identical |

## 6. Supabase dashboard (production project) — settings the flag-on needs

| setting | where | needed for | state |
|---|---|---|---|
| **Google provider** enabled with the OAuth client id/secret | Authentication → Providers → Google | parent "Continue with Google" | check — the hook admits an off-domain Google account only while `consumer_signup_enabled` is on |
| **Azure (Microsoft) provider** enabled | Authentication → Providers → Azure | org staff Microsoft sign-in | already used by school staff — confirm still on |
| **Email provider**: email+password on, **Confirm email ON**, magic link ("Email OTP / magic link") on | Authentication → Providers → Email | parent signup verify step; org magic-link fallback | check |
| **Site URL** `https://mrbadmus.com`; **Redirect URLs** include `https://mrbadmus.com/consumer/verify.html`, `https://mrbadmus.com/org/index.html`, `https://mrbadmus.com/reset-password.html`, `https://mrbadmus.com/consumer/account.html` | Authentication → URL Configuration | the verify return, Google return, org return, password reset | **missing until added** |
| **Confirm signup email template** = Design's E1 (`docs/b2c/emails/E1-supabase-confirm-signup.md`) | Authentication → Email Templates → Confirm signup | the one email Supabase sends | **missing until pasted** (Night 2 open item 5) |
| **Reset password** and **Magic link** templates — brand as "MrBadmus" | same | parent reset; org magic link | check wording carries no "MrBadmusAI" |
| **Custom SMTP** (Resend SMTP or another) | Authentication → SMTP Settings | Supabase's built-in sender is rate-limited to a handful an hour — real signups will hit it | **missing until configured** |
| `platform_flags.consumer_signup_enabled` | SQL editor | the DB half of the front door | `false`; flip on Night 4 |
| `platform_settings.cron_target_url` + `cron_secret` | SQL editor (Night 2 runbook) | the Sunday scheduler + digests | null on prod until armed |
| **Realtime**: `family_messages` in the `supabase_realtime` publication | migration 4 (Night 2) | live chat | applied by Night 2's migration |
| **`platform_operators`** row for Mide | SQL | Admin Accounts + Marking Queue (a non-operator gets 404) | check Mide's profile has a live row |

## 7. Stripe dashboard (live mode)

- Product + two prices + portal configuration from `scripts/stripe-setup.js` (live key).
- Webhook endpoint → `https://mrbadmus-backend.onrender.com/api/consumer/stripe/webhook`, events: `checkout.session.completed`, `customer.subscription.created`, `.updated`, `.deleted`, `invoice.paid`, `invoice.payment_failed`, `customer.subscription.trial_will_end`.
- Tax code ruling (Night 2 open item 1) and the VAT question — still on Mide.
- The Customer Portal must allow: cancel at period end, card update, invoices, monthly↔annual switch (as `stripe-setup.js` configures).

## 8. Deploy order

1. Migrations 13 → 14 on production (§2), verify after 14.
2. Seeder re-run (§3).
3. Render env (§5) — everything except `CONSUMER_SIGNUP_ENABLED`.
4. Backend: merge `b2c/launch`, push, wait "Live", read `/api/health` (`stripe`, `limits`, `email` modes).
5. Frontend: `python3 build_all.py`, commit, push; confirm `https://mrbadmus.com/go/`, `/parents/`, `/org/sign-in.html` all answer "Not found" (flag off) with no console requests.
6. Supabase dashboard (§6): providers, redirect URLs, E1 template, SMTP.
7. Rainford smoke (teacher landing, today, admin with the consumer card hidden, student class page, leaderboard count unchanged).
8. Arm the clock (Night 2 runbook §platform_settings) — last.
9. Leave the flag off. **Night 4 turns it on in three places**: `shared/config.js` PROD (`CONSUMER_SIGNUP_ENABLED: true`, rebuild, push), Render `CONSUMER_SIGNUP_ENABLED=true` (redeploy), `update platform_flags set enabled=true where key='consumer_signup_enabled'`.

## 9. Open items found by the drives (on Mide)

- **No sign-out on any child surface** — Design's child header has none. A child on a shared family laptop cannot sign out; one link is the fix if you want it.
- **A child cannot see a past unit check's breakdown** — the only route that returns one is guardian-only, so Design's "See the breakdown" on the already-taken card is dropped. A `GET /child/unit-checks` route would restore it.
- **`GET /api/consumer/family` takes 5–10 s on TEST** with two children (`enrichFamily`); the dashboard's first paint waits on it. The MRB-292 shape again; not fixed tonight.
- **`/reset-password.html` is the school-brand page** ("MrBadmusAI", Fraunces); a consumer parent resetting a password lands on it. Works; wrong brand.
- **Usernames cannot contain hyphens** (platform charset since before Night 1) but Design's examples (`amara-rockets`) and her E2 copy do. The pages accept letters and digits only and the placeholder says so; her example strings are a Design change or a charset ruling.
- **No privacy notice page exists** on the estate; the Account page's "Privacy notice" row is omitted until one does (consumer T&Cs / privacy are on your owner-side list).
- **Exam picker has no pagination** — 370 KS3 questions on one screen; Design drew none.

## 10. Deliberately unbuilt (on Mide)

- The sweep that executes an `account_deletion_requests` row after 30 days.
- A Public Organisations page (Design did not deliver one).
- The organisation DPA PDF (the account page offers "Request a copy" by email).
- Card brand/last-4 on Admin Accounts (a Stripe read per account; shows "—").
- E7 (cancelled) and E8 (new-messages) copy — Night 2 placeholders until Design delivers.
