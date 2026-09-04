# Night 4 — the live configuration checklist (MRB-321, Phase D)

Every item Mide does by hand before the flag goes on, with **current value or
MISSING** as read on 3 Sep 2026. Code drives and verifies each one; Code cannot
do any of them, because each needs a credential or a dashboard Code has no
access to.

Production ref is **`urklkrwevjtlfbwnipjn`** ("mrbadmus", ends in **N**).

Legend — **✅ verified present** · **❌ MISSING** · **⏳ Mide in progress** ·
**❓ cannot be read from here, Mide confirms**

---

## 0. Already true before Night 4 started (Code verified, nothing to do)

| item | how it was checked | value |
|---|---|---|
| Production is the right project | `select 1` + `current_database()` on `urklkrwevjtlfbwnipjn` | ✅ reachable |
| Consumer flag OFF — backend | `/api/health` returns the pre-Night-2 shape (no `stripe`/`limits`/`email` keys) | ✅ off |
| Consumer flag OFF — database | `platform_flags` table does not exist yet (Night 1 migration 4 creates it, seeded `false`) | ✅ off |
| Consumer routes not live | `GET /api/consumer/pricing` → **404** | ✅ absent |
| Consumer pages not live | `/parents/`, `/go/`, `/consumer/signup.html` → **404** | ✅ absent |
| Realtime publication exists | `select pubname from pg_publication where pubname='supabase_realtime'` → 1 row | ✅ present (Night 2 migration 4 will not need to create it) |
| `platform_operators` row for Mide | `platform_operators` joined to `profiles` | ✅ **present** — Ayo / `JellyNova13`, granted 3 Jul 2026, no `ended_at`, no `deleted_at`. Admin Accounts + Marking Queue will open. |
| Leaderboard baseline (for the regression check) | SQL | 186 score rows · **21 distinct students** · 160 live profiles · 56 with no school · 104 with a school. Current week 2026-08-28 has no scores; champion `null`. **These must be identical after the backend deploys.** |

---

## 1. Stripe — activation, then the live product

⏳ **Mide reported activation in progress, 3 Sep 2026.**

| step | value | state |
|---|---|---|
| Account activated (business details **3rd Eye Ltd**) | — | ⏳ in progress |
| Public business name **MrBadmus** | — | ⏳ |
| Statement descriptor **MRBADMUS** | — | ⏳ |
| **Managed Payments decision** | Night 2 found this account has Managed Payments ON, which forces two things: the API version pin `2026-08-26.dahlia` (already in code) and a **tax code on the product** or Checkout refuses outright | ❓ Mide's call |
| Product tax code | Night 2 set `txcd_20060058` ("Training Services – Self-study Web-based") to be able to check out at all. Whether it is right for a non-VAT-registered seller is **Mide + accountant**, not Code | ❓ open ruling |
| Live product + prices + portal config | `node scripts/stripe-setup.js --live` — **Mide supplies the `sk_live_` key on the command line; it is never written to disk** | ❌ not yet run |
| → `STRIPE_PRICE_MONTHLY` | printed by the script | ❌ |
| → `STRIPE_PRICE_ANNUAL` | printed by the script | ❌ |
| → `STRIPE_PORTAL_CONFIG` | printed by the script | ❌ |
| Live webhook endpoint | `https://mrbadmus-backend.onrender.com/api/consumer/stripe/webhook` | ❌ |
| → the **six** event types | `checkout.session.completed`, `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.paid`, `invoice.payment_failed` — **plus** `customer.subscription.trial_will_end`, which the runbooks list and which E5 (trial ending) depends on. That is **seven**; register all seven. | ❌ |
| → signing secret → `STRIPE_WEBHOOK_SECRET` | from the endpoint page | ❌ |
| Customer Portal permits | cancel at period end · update card · view invoices · switch monthly↔annual | ❌ (created by the script) |

⚠️ `scripts/stripe-setup.js` now (Night 4, Lane A) **refuses an `sk_live_` key
without `--live`**, and equally refuses `--live` with an `sk_test_` key — the
dangerous direction, which would have silently handed test ids to production.
Under `--live` it writes **no file at all** (the fs write calls are replaced
with throwers), prints a banner naming the live account, pauses ten seconds for
Ctrl-C, then prints the four ids.

---

## 2. Render environment (backend) — before the backend deploy

Code cannot read Render's environment. Every row is ❓ until Mide confirms it in
the dashboard; `/api/health` proves three of them from outside afterwards (§5).

| variable | value to set | state |
|---|---|---|
| `STRIPE_SECRET_KEY` | the **live** `sk_live_…` key | ❌ swap from test |
| `STRIPE_WEBHOOK_SECRET` | from §1 | ❌ |
| `STRIPE_PRICE_MONTHLY` | from §1 | ❌ |
| `STRIPE_PRICE_ANNUAL` | from §1 | ❌ |
| `STRIPE_PORTAL_CONFIG` | from §1 | ❌ |
| `STRIPE_API_VERSION` | **leave absent** — code defaults to `2026-08-26.dahlia`, which is what Managed Payments requires | ✅ absent is correct |
| `CONSUMER_CRON_SECRET` | a fresh random string; **must equal** `platform_settings.cron_secret` set in §4 | ❌ |
| `FRONTEND_ORIGIN` | `https://mrbadmus.com` | ❌ (worktree holds `http://localhost:8000`) |
| `RESEND_API_KEY` | already on Render per the brief — **confirm**. Absent = every email is a dry-run row and no parent ever gets one | ❓ confirm |
| `SUPABASE_ANON_KEY` | **child login 500s without it** — confirm it is set, not just the URL and service-role key | ❓ confirm |
| `ANTHROPIC_API_KEY` | already on Render for `/api/chat`; the marker uses the same key. Absent = stub marking, which would show a child a fake mark | ❓ confirm |
| `UPSTASH_REDIS_REST_URL` | shared rate limits across instances | ❌ |
| `UPSTASH_REDIS_REST_TOKEN` | ditto | ❌ |
| `MARK_PROVIDER` | leave absent | ✅ |
| `ANTHROPIC_MODEL` | leave absent (defaults `claude-sonnet-4-6`) | ✅ |
| `EXTRA_CORS_ORIGINS` | **leave absent** — production's allowlist stays byte-identical | ✅ |
| `CONSUMER_SIGNUP_ENABLED` | **still absent at this stage.** Phase E sets it | ✅ absent is correct |

---

## 3. Supabase production dashboard

Auth provider configuration cannot be read over SQL. ❓ = Mide reads it off the
dashboard and tells Code.

| setting | where | needed for | state |
|---|---|---|---|
| **Google provider** on, with OAuth client id + secret | Auth → Providers → Google | parent "Continue with Google". The auth hook admits an off-domain Google account **only while the flag is on** | ❓ |
| **Azure (Microsoft)** unchanged | Auth → Providers → Azure | school staff today, org staff tomorrow — **do not touch** | ❓ confirm still on |
| **Email**: password on, **Confirm email ON**, magic link on | Auth → Providers → Email | the signup verify step; org magic-link fallback | ❓ |
| **Confirm signup template** = Design's E1 | Auth → Email Templates | the one email Supabase itself sends | ❌ paste from `docs/b2c/emails/E1-supabase-confirm-signup.md` |
| Reset-password + magic-link templates say **MrBadmus**, never "MrBadmusAI" | same | brand | ❓ |
| **Site URL** `https://mrbadmus.com` | Auth → URL Configuration | every return | ❓ |
| **Redirect URLs** | Auth → URL Configuration | ❌ add all five: | |
| → `https://mrbadmus.com/consumer/verify.html` | | the signup verify return | ❌ |
| → `https://mrbadmus.com/consumer/account.html` | | the Google return | ❌ |
| → `https://mrbadmus.com/org/index.html` | | the org staff return | ❌ |
| → `https://mrbadmus.com/parents/reset-password.html` | | **the new consumer-branded reset page** (Night 4, Lane C) | ❌ |
| → `https://mrbadmus.com/reset-password.html` | | the existing school page — leave it in place | ❓ confirm present |
| **Custom SMTP** (Resend or other) | Auth → SMTP Settings | Supabase's built-in sender is capped at a handful an hour. Night 3 already hit a **429 email rate limit on TEST**. Real signups will hit it on day one | ❌ **strongly recommended before beta** |
| `platform_operators` row for Mide | SQL | Admin surfaces | ✅ present (§0) |

---

## 4. Arm the clock — last, after the backend is live

Two `platform_settings` updates on production. Until both are set, all five cron
jobs fire and do nothing, which is the safe state.

```sql
update public.platform_settings
   set value = to_jsonb('https://mrbadmus-backend.onrender.com'::text)
 where key = 'cron_target_url';

update public.platform_settings
   set value = to_jsonb('<the same secret as Render CONSUMER_CRON_SECRET>'::text)
 where key = 'cron_secret';
```

Then confirm the plumbing resolves:

```sql
select public.consumer_cron_call('/x');   -- non-NULL once armed (NULL = still unloaded)
select jobname, schedule, active from cron.job where jobname like 'consumer_%';  -- 5 rows
```

State: ❌ `platform_settings` does not exist on production yet — Night 2
migration 9 creates it. Nothing to do until Phase B has run.

---

## 5. Verify from outside — the proof the configuration took

After the backend redeploys, `/api/health` reports three modes. This is the one
check that proves §1 and §2 from outside the dashboard:

```bash
curl -s https://mrbadmus-backend.onrender.com/api/health
```

| field | must read | meaning if wrong |
|---|---|---|
| `stripe` | `configured` (live) | `missing` = no checkout at all |
| `limits` | `upstash` | `memory` = rate limits are per-instance only |
| `email` | `live` | `dry_run` = **no parent receives any email**, silently |

Current value, 3 Sep 2026 (before any deploy):
`{"status":"ok","service":"MrBadmusAI Backend","version":"2.0.0","db":"ok"}` —
none of the three fields exist yet, because the Night 2 backend is not deployed.

---

## 6. The one thing on this list that blocks beta

**❌ The consumer terms and privacy text does not exist.** There is no
`docs/b2c/legal/`, no `terms.md`, no `privacy.md`. The only privacy document on
the machine is the school-facing `MrBadmusAI_Privacy_Policy.docx`, which is the
B2B one and is not this.

Night 4 builds `/parents/terms.html` and `/parents/privacy.html` as fully-built,
fully-styled shells with an unmissable placeholder where the text goes, section
headings scaffolded from MRB-319, linked from every public footer and from the
signup checkbox. **Code deliberately did not write the legal text**: invented
terms and an invented privacy policy are worse than a visible gap, and this is
a contract with paying parents about children's data.

Consequence, stated plainly: **Phase E can run and Mide can be the first family
on a real card. The beta families should not be invited until that text lands.**
It is MRB-319, owner-side.
