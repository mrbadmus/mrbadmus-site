# Night 3 — backend additions the frontend builds to (MRB-317 / MRB-318)

Everything in `API-CONTRACT.md` §v3.4–v3.5 stands. This file is ONLY what
Design's nineteen surfaces need that the contract lacks, found by reading her
`const` blocks against the contract. Each addition is small and additive.
The backend executor builds these; the frontend executors build against them
at the same time. If the backend has to deviate, it writes the deviation in
`API-CONTRACT.md` §v3.6 and tells the commander, who tells the lane.

All routes: `consumerGate` first, JSON `{ error, message }` on failure,
codes as the contract. New module files: `consumer/org.js` (§C),
`consumer/admin.js` (§D), `consumer/account.js` (§B). Mounted from
`consumer/index.js` after `marking`.

---

## A. Pricing — one source, exported

`GET /api/consumer/pricing` — consumerGate, **no auth** (the public pricing
page has no session).

```json
{ "ok": true, "currency": "GBP", "trial_days": 7,
  "tiers": { "month": { "first": 999, "rest": 599 }, "year": { "first": 7900, "rest": 4900 } } }
```

Read from `ctx.stripe.TIER` — the SAME object `billingFor()` prices seats
from and `scripts/stripe-setup.js` mirrors. The pricing page and the signup
plan step compute every number from this and hold NO price constant of their
own. Cache header `Cache-Control: public, max-age=300`.

## B. Parent account — `consumer/account.js`

### B1. `PATCH /api/consumer/parent` (requireParent)
Body `{ first_name }` (1–60 chars). Writes `profiles.first_name` via service
role (the `authenticated` role has no UPDATE on profiles). → `{ ok, parent: { id, name, email } }`.
Email and password changes are NOT here: the page uses Supabase directly
(`auth.updateUser({ email })` with the confirm flow, `auth.resetPasswordForEmail`).

### B2. `GET /api/consumer/family/export` (requireParent)
A JSON bundle, `Content-Disposition: attachment; filename="mrbadmus-<family>-<date>.json"`:
```json
{ "exported_at", "family": {…}, "parent": { "id", "name", "email" },
  "children": [ { "…profile fields the contract returns…",
                  "work": [ …all work_items… ], "unit_checks": [ … ], "answers": [ …Design's answers[] shape… ],
                  "messages": [ …family_messages with this child, oldest first… ],
                  "report": { …current term's report… } } ] }
```
Nothing a child could not already see through the dashboard; no internal
emails, no Stripe ids. This is the "Download everything we hold" link.

### B3. Account deletion — soft, 30-day grace, admin-visible
Migration (commander applies): `account_deletion_requests(org_id uuid pk
references schools, requested_by uuid, requested_at timestamptz default now(),
execute_after timestamptz not null, cancelled_at timestamptz, note text)`,
RLS: parent of the org may SELECT own row; writes service-role only.

- `POST /api/consumer/family/delete-request` (requireParent) body
  `{ confirm: "DELETE" }` (exact, else 400 `confirm_required`). Upserts the
  row with `execute_after = now() + 30 days`; if a Stripe subscription is
  live, sets `cancel_at_period_end: true` on it (no refund, no immediate
  cancel — Design's "subscription is cancelled today; no further charges");
  writes `write_audit_event('account_deletion_requested','schools',org)`;
  sends the `account_deletion` email (§E). → `{ ok, execute_after }`.
  **Nothing is hard-deleted tonight.** The sweep that executes after 30 days
  is NOT built; the row and the runbook say so.
- `DELETE /api/consumer/family/delete-request` (requireParent) → sets
  `cancelled_at`, audit `account_deletion_cancelled`. → `{ ok }`.
- `GET /api/consumer/family` gains `deletion: { requested_at, execute_after } | null`.
- Admin list (§D1) shows `deletion_requested_at`.

## C. Organisation staff — `consumer/org.js`

New gate `requireOrgStaff`: signed-in `teacher|hod|admin` whose org is
`organisation`-kind → `req.staff = { user, profile, org, access }`; else 403
`not_org_staff`. Everything below is `consumerGate, requireOrgStaff`.

### C1. Groups are classes — one column
Migration (commander applies): `alter table classes add column consumer_kind
text check (consumer_kind in ('child','group'))`. The backend stamps
`consumer_kind='child'` on the per-child class right after
`attach_child_to_family` returns (service-role update, in `POST /children`
and the bulk route), and `'group'` on a group class it creates. **Every
existing reader of a child's class (`GET /family` class lookup, `classOf()`
in work.js, `consumerPracticeFor`) must exclude `consumer_kind='group'`**, so
a pupil in a group still has exactly one "own" class. A pupil is a member of
at most one group (`class_members`, `left_at` set when moved).

### C2. `GET /api/consumer/org`
```json
{ "ok": true,
  "org": { "id", "name", "kind": "organisation", "seat_cap": 40, "seats_used": 31, "period_end": "2027-08-31", "contact_name", "contact_email", "access", "state" },
  "staff": { "id", "name": "Ms Okafor" },
  "staff_list": [ { "id", "name", "role": "Caseworker|Admin", "groups": "7B, 9X", "pending": false } ],
  "groups": [ { "id", "name": "7B", "year": 7, "unit": "Cells and organisation|null", "intensity": "light|steady|full", "count": 9, "done": "6/9" } ],
  "pupils": [ { "id", "name", "initial", "username", "year", "group": "7B|null", "group_id", "mode", "intensity", "paused",
                "days": [1,0,1,0,0,0,0], "last": 45, "streak": 1, "lastActive": "…iso|null", "active": "Today|Yesterday|9 days ago|Never",
                "flag": "Not started|Quiet|null", "scores": [ { "label", "pct" } ], "weak": "…|null", "humanUsed": 1, "humanLeft": 1, "unread": 0 } ] }
```
`pupils[]` is the SAME per-child enrichment `enrichFamily()` gives a parent
(export `enrichChildren(orgId, children)` from work.js and reuse it; do not
re-derive streaks). `done` on a group = done/set items this week across its
members. `staff_list` = live `profiles` with role teacher/hod/admin in the
org + unclaimed `pending_staff` rows (`pending: true`). `seats_used` = live
children. `period_end` = `subscriptions.current_period_end`.

### C3. Groups
- `POST /api/consumer/org/groups` `{ name, year_group, unit_code?|topic?, intensity? }` → creates the class (`consumer_kind='group'`, the org's academic year, `key_stage` from year) → `{ ok, group }`. 400 `name_required|year_group_invalid`, 409 `group_exists`.
- `PATCH /api/consumer/org/groups/:id` `{ name?, year_group?, unit_code?|topic?, intensity? }` → renames; when `unit_code`/`topic` or `intensity` is given, applies it to EVERY current member server-side through the same functions the guardian routes use (`position`, `intensity`) → `{ ok, group, applied: n }`.
- `POST /api/consumer/org/groups/:id/members` `{ add: [child_id], remove: [child_id] }` → moves pupils (adding to one group leaves any other) → `{ ok, count }`. 404 for a child not in the org.
- `DELETE /api/consumer/org/groups/:id` → soft-deletes the class; members keep their own class → `{ ok }`.

### C4. Set work at org scope — ONE route, loop on the server
`POST /api/consumer/org/work` (+writable)
```json
{ "target": "all" | { "group_id": "…" } | { "child_id": "…" },
  "kind": "lesson|practice|exam", "lesson_slug"?, "unit_code"?|"topic"?, "question_id"?, "scheduled_for"?, "note"? }
```
Resolves the pupil set (all live pupils / the group's members / the one
pupil — 404 if not the org's), then calls the SAME internal function the
guardian `POST /children/:id/work` route uses, once per pupil, `set_by =
staff id`. → `{ ok, set: n, skipped: [ { child_id, reason } ] }`. Never N
client calls.

### C5. Bulk add pupils — seat cap enforced before the first insert
`POST /api/consumer/org/pupils/bulk` (+writable)
`{ pupils: [ { first_name, year_group, group: "7B"|null, mode?, intensity? } ] }` (1–200 rows).
First: `seats_free = seat_cap − live children`. If `pupils.length >
seats_free` → **409 `seat_cap_reached`** `{ error, seat_cap, seats_used,
seats_free, message: "Only <n> seats free. Add seats from Account, or remove leavers first." }` and NOTHING is created.
Then per row: username from `generate_username()` (the estate's generator),
password = three words + number (e.g. `comet-saturn-42`, ≥ 8 chars), create
exactly as `POST /children` does (auth user, `attach_child_to_family`, stamp
`consumer_kind`, seed plan, NO email — an org pupil has no parent), add to
the named group (create the group if the name is new, `year_group` from the
row). A row that fails is reported, not fatal.
→ `{ ok, created: [ { child_id, first_name, year_group, group, username, password } ], failed: [ { row, error } ] }`.
**The passwords are returned ONCE, here, for the login slips, and are never
stored or logged.**

### C6. Org account
- `GET /api/consumer/org/export` → CSV (`text/csv`, attachment): pupil name, username, year, group, mode, streak, last active, unit-check average, sessions done this term. No passwords, no internal emails.
- Existing `POST /children/:id/password` (guardian) already lets staff reset a pupil's password; it returns `{ ok }` — **change it to also return `{ password }` ONLY when the caller supplied none** (body `{}` → generated, returned once; body `{ password }` → set, not echoed). Design shows the new password once on both the parent and the org pupil page.
- Chat per pupil: existing `/chat/*` (an org staff member is a valid counterparty — `requireConsumerUser`). Report per pupil: existing `/children/:id/report` (staff are guardians). Digest: existing weekly digest already goes to org staff.

### C7. Org sign-in
No new route. `/org/sign-in.html` uses Supabase `signInWithOAuth({ provider: 'azure' })` (the hook admits an on-domain Microsoft account with a `pending_staff` row) and `signInWithOtp({ email })` as the magic-link fallback (passes the hook; `claim_pending_staff` keys on email). Email+password (Design's form) is `signInWithPassword` for a staff member who already has one. After sign-in the page calls `GET /api/consumer/org`; 403 `not_org_staff` → Design's error string.

## D. Admin — `consumer/admin.js` (all `requireOperator`)

### D1. `GET /api/consumer/admin/accounts?filter=all|trialing|active|past_due|cancelled|locked|orgs&q=`
```json
{ "ok": true,
  "stats": { "families", "in_trial", "children", "organisations", "pupils", "family_mrr_pence", "past_due" },
  "accounts": [ { "id", "name", "kind": "family|organisation", "email": "parent or contact email|null",
                  "billing": "trialing|active|past_due|cancelled|locked|none|invoiced",
                  "kids": [ { "id", "name", "year", "mode": "School|Home", "active": "today|yesterday|3 days ago|never" } ],
                  "kids_label": "Amara Y9, Leo Y7" | "31 pupils",
                  "mrr_pence": 1598, "mrr_label": "£15.98" | "£186.00 eq." , "since": "…iso", "last_active": "…iso|null",
                  "cycle": "Monthly|Annual (£79)|Annual · 40 seats", "next": "…iso|null", "next_label": "8 Sep|Retry 11 Sep",
                  "card": null, "failures": 2, "stripe_customer_id": "cus_…|null",
                  "seat_cap", "seats_used", "deletion_requested_at": "…|null", "trial_end", "locked_at" } ] }
```
`failures` = count of `stripe_events` rows of type `invoice.payment_failed`
resolved to the org. `card` is `null` tonight (reading the payment method is
a Stripe call per account; the page shows "—"); `stripe_customer_id` is
what the "Open in Stripe" link needs (`https://dashboard.stripe.com/test/customers/<id>` on TEST — the page builds the URL from `/api/health`'s `stripe` mode, or simply from `MrBadmusConfig.environment`). Org MRR is the organisation's annual value ÷ 12 when a `subscriptions.quantity`×price exists, else 0 — labelled "eq.".

### D2. `GET /api/consumer/admin/accounts/:id`
The D1 row plus `timeline: [ { when: "…iso", what: "Account created" } ]`
merged and sorted newest-first from: `audit_log` where `school_id = org`
(every operator action below writes one), `stripe_events` resolved to the
org (type → words: "Payment failed (card declined)", "Subscription cancelled", …),
`email_log` for the org ("E3 Sunday digest sent", "E6 sent" — map type → E-number: welcome E2, digest E3, mb_marked E4, trial_ending E5, payment_failed E6, subscription_cancelled E7, new_messages E8), plus children added (`profiles.created_at` where `created_by` is the parent).

### D3. Support actions — each writes `write_audit_event` so D2 shows it
| route | body | does |
|---|---|---|
| `POST /admin/orgs/:id/extend-trial` | `{ days: 7 }` | If a live Stripe subscription is `trialing`: `stripe.subscriptions.update(id, { trial_end: current + days })` and mirror; else the existing comp path (`status='comped'`, `comped_until = greatest(trial_end, now) + days`). → `{ ok, trial_end }`. 409 `not_on_trial` when neither applies. |
| `POST /admin/children/:id/password` | `{}` | Operator resets any consumer child's password to a generated one, returned ONCE → `{ ok, password }`. 404 if not a consumer child. |
| `POST /admin/orgs/:id/resend-verification` | — | Anon client `auth.resend({ type: 'signup', email })` for the family's parent. 409 `already_verified` when `email_confirmed_at` is set. → `{ ok }` |
| `POST /admin/orgs/:id/human-marks` | `{ add: 2 }` | `org_limits.mb_marks_per_month = coalesce(current, platform default 2) + add`, note "goodwill <date>". → `{ ok, limits }`. (This persists past the month — say so in the response `note`.) |
| `POST /admin/orgs/:id/unlock` | — | Only when `org_access_state` is `locked`: comp for 14 days (`comped_until = now + 14d`, status `comped`), invalidate access. 409 `not_locked` otherwise. → `{ ok, comped_until }` |
| `POST /admin/orgs` | `{ name, seat_cap, period_end: "YYYY-MM-DD", contact_name, contact_email, email_domain? }` | **Create an organisation from Admin** — no SQL: `schools` row (`kind='organisation'`, `email_domains=[email_domain]` when given, `code` generated), its `academic_years` row (1 Sep–31 Aug of the current year), `subscriptions` row (`status='active'`, `seat_cap`, `current_period_end = period_end`, `quantity=0`), a `pending_staff` row for the contact (`profile_role='admin'`) so the first Microsoft or magic-link sign-in claims it. Audit `organisation_created`. → `{ ok, org }`. 400 `name_required|seat_cap_invalid|period_end_invalid|contact_email_invalid`. Replicates exactly what `night2-drive.js` step 16 did by SQL. |

### D4. Marking queue rows — four fields more
`GET /admin/mb-queue` rows gain: `child.mode` ("School|Home"), `child.board`
("AQA · Combined · Higher" or "KS3"), `parent_names: ["Funmi"]` (guardians who
will be emailed), `prev_count` (this child's other exam answers), and `org_kind`.
`sent_at` stays; the page computes age.

## E. Emails (MRB-314 follow-through) — `consumer/email.js`
Transcribe Design's `Emails.dc.html` into the existing templates, keeping the
node-list renderer (one list → html + text): E2 → `child_login_details` AND
`welcome` (E2 is the post-checkout welcome: username, never the password,
login URL **mrbadmus.com/go**, the first week's facts, "Free week ends"), E3 →
`digest`, E4 → `mb_marked`, E5 → `trial_ending` (itemised per-child rows),
E6 → `payment_failed` (grace dates: failed on, retry on, grace end). E1 is
Supabase's confirm-signup email: keep NO template; write her E1 text to
`docs/b2c/emails/E1-supabase-confirm-signup.md` for Mide to paste into the
dashboard. E7 (`subscription_cancelled`) and E8 (`new_messages`) were NOT
delivered — keep the Night 2 placeholders, rewritten only where they said
"MrBadmusAI" or pointed at retired paths. New `account_deletion` (B3): plain,
one CTA "Undo — sign in", 30-day date. Every link: dashboard →
`/consumer/overview.html`, account → `/consumer/account.html`, child login →
`/go`, marked answer → `/consumer/overview.html?child=<id>&view=answers`.
600px, hex colours, one CTA, plain-text part, subject + preview as hers,
wordmark "MrBadmus". Re-run `scripts/email-preview.js`; `grep -c "AI"` on the
rendered output must be 0 for the wordmark (a word like "detail" is fine —
grep `MrBadmusAI` and ` AI ` separately).

## F. Frontend seam additions (frontend lanes, in consumer-common.js — Edit only)
- `boot({ public: true })`: on the enabled path removes `meta[name=robots]`; still `notFound()` when off; never loads the Supabase SDK unless `requireSession` or the page asks (`sessionOptional: true` loads it and passes `session|null`).
- `MrBadmusConsumer.pricing()` — memoised `GET /api/consumer/pricing`, with `price(tiers, interval, n)` returning `{ first, rest, total_pence }`.
- `MrBadmusConsumer.childLoginUrl` = `'/go/'`.
- Nothing else shared changes shape.

## G. Marker prompt (MRB-313) — one line
In `markingSystemPrompt`, when the item has NO level descriptors (the KS3
ladder items): "There are no level descriptors. Place the answer by BEST FIT
against the scheme points: the score reflects how much of the scheme the
answer meets overall, not a one-to-one count of ticks." KS3 `explain` = 4
marks, `produce` = 6 (reseeded on TEST tonight).
