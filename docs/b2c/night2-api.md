# B2C Night 2 — the API contract the executors build to

> ⊕ **Superseded where it disagrees with the code.** This file was written
> BEFORE any route existed and is kept as the design intent. The shipped
> contract is `API-CONTRACT.md` §v3.5 in the backend repo, written FROM the
> code afterwards, with a fifteen-row table of where the two differ (a
> `requireChildMaker` gate instead of `requireParent` on child creation;
> KS3-only unit checks; fixed term boundaries instead of Easter; feedback
> mandatory on an MB mark; extra fields on several responses). Night 3
> transcribes from `API-CONTRACT.md`, not from here.

Written before any route existed, from Design's Drop 1 const blocks
(`docs/b2c/design/drop1/…/*.dc.html`) and the seven tickets. Every response
shape below is chosen so that Night 3 can render Design's screen from it
without reshaping. Where Design's mock and a ticket disagree, the ticket
wins and the difference is noted.

Everything is under `/api/consumer/*`, behind `consumerGate` (404 when the
flag is off), unless it says otherwise. Backend module layout:

```
backend/consumer/
  access.js    orgAccess(orgId) → { state, writable, kind }   ← THE helper
  ctx.js       shared plumbing handed to every module (supabase, gates, limits, email)
  stripe.js    MRB-309
  work.js      MRB-310   (scheduler + parent controls + cron endpoints)
  chat.js      MRB-311
  checks.js    MRB-312   (unit checks)
  report.js    MRB-312   (termly report)
  marking.js   MRB-313
  email.js     MRB-314   (Resend adapter + templates + digest)
  notify.js    MRB-314   (in-app flags)
  limits.js    MRB-315   (caps + rate limiter adapter)
```

`server.js` mounts them in one block after the Night 1 consumer middlewares:
`require('./consumer')(app, ctx)`.

---

## 0. Access states and gates (MRB-309, platform-wide)

`org_access_state(org)` in SQL is the single source of truth:

| state | who | child may | parent sees |
|---|---|---|---|
| `full` | school (always); family trialing/active/comped/past_due within 7d grace; org with seat cap + period | everything | normal |
| `read_only` | family past_due beyond grace, canceled before period end, stale trial; org ≤14d past period end | view lessons and past work; **cannot submit**; chat read-only; no marking; no new work generated | "payment failed" / "cancelled, access until {date}" |
| `locked` | canceled after period end, `locked`, comped expired; org beyond 14d | same as read_only | "paused — reactivate" |
| `none` | family that never checked out | same as read_only | checkout |

Backend: `orgAccess(orgId)` in `consumer/access.js` (one RPC, 15s cache per
org, cleared by the webhook). `requireWritable(req,res,next)` uses it.
Frontend: `consumer-common.js` `guard(state)` reads `billing.state` from
`GET /api/consumer/family` (parent) or `GET /api/consumer/child/today`
(child) and disables submit/send/mark controls when not `full`.

### Gates

| middleware | admits |
|---|---|
| `consumerGate` | flag on (env + DB) |
| `requireParent` | signed-in `parent` with a family org — **no longer 402s**; attaches `req.parent = { user, profile, org, access }` |
| `requireGuardian(':id')` | `requireParent` OR organisation staff, and `guardian_of_child(actor, :id)` true; attaches `req.child` |
| `requireChild` | signed-in `student` whose org is family/organisation kind; attaches `req.child = { user, profile, org, access }` |
| `requireConsumerUser` | parent, child or org staff of a consumer org (chat) |
| `requireWritable` | after one of the above: `access.state === 'full'` else **423** `{ error:'org_locked', state, message }` |
| `requireOperator` | Night 1 |
| `requireCron` | `x-cron-secret === process.env.CONSUMER_CRON_SECRET` else 401 |

Night 1 routes change: `POST /children` needs `requireParent` only (a parent adds
children before checkout). `PATCH/DELETE /children/:id`, `/password` become
`requireGuardian`.

Common error codes: `not_found` 404 (flag off), `not_authenticated` 401,
`not_a_parent`/`not_a_guardian`/`not_a_child` 403, `no_family` 409,
`org_locked` 423, `cap_reached` 429 `{ error:'cap_reached', kind, limit, used, resets_at, message }`,
`rate_limited` 429, `quota_reached` 429 (Mr Badmus quota).

---

## 1. Family, billing (MRB-309)

### `GET /api/consumer/family` (requireParent) — extended

```json
{ "ok": true,
  "family": { "id", "name", "kind" },
  "parent": { "id", "name", "email" },
  "billing": {
    "state": "none|trialing|active|past_due|cancelled|locked",   // Design's billingState; 'cancelled' = canceled with period left
    "access": "full|read_only|locked|none",
    "interval": "month|year|null",
    "quantity": 2,
    "trial_end": "2026-09-09T17:00:00Z|null",
    "next_payment_at": "…|null",      // current_period_end while active/trialing
    "failed_at": "…|null", "retry_at": "…|null",   // past_due
    "access_end": "…|null",           // canceled: current_period_end; locked: locked_at
    "cancel_at_period_end": false,
    "days_left": 4,                   // trial days left, else null
    "grace_days_left": 5,             // past_due grace, else null
    "seats": [ { "child_id", "name", "year", "price_pence": 999 } ],   // graduated: first 999/7900, rest 599/4900
    "monthly_total_pence": 1598, "annual_total_pence": 12800,
    "can_checkout": true,             // state none|locked|cancelled-after-end
    "can_portal": true                // has a stripe customer
  },
  "prefs": { "digest": true, "messages_email": true, "marking_email": true },
  "children": [ …Night 1 fields…, plus:
    { "status": "active|paused|never|quiet",   // Design: paused = plan paused; never = no done item ever; quiet = nothing done in 7 days
      "streak": 6, "unread": 2, "humanLeft": 1,
      "days": [1,0,1,0,0,0,0],                  // Mon–Sun this week, done item on that day
      "scores": [ { "label": "Cells", "pct": 55 } ],   // unit-check records, oldest first, max 6
      "weak": "Health and disease: body defences", "lastActive": "2026-09-01T19:40:00Z|null",
      "work": [ { "id", "day": "Tue", "scheduled_for", "title", "sub", "kind", "source": "From Mr Badmus|Set by Funmi", "byParent": false, "mins": 20, "done": true } ],
      "position": { "cursors": { "Biology": 3, … }, "labels": { "Biology": "Cells: lesson 3" } },
      "paused": false, "mode", "intensity" } ] }
```
`messages[]` and `answers[]` per child come from their own endpoints (§3, §5);
the dashboard fetches them on opening the child.

### `POST /api/consumer/checkout` (requireParent)
Body `{ "interval": "month|year", "success_url"?, "cancel_url"? }` — URLs default
to `${FRONTEND_ORIGIN}/consumer/checkout-return.html?state=success|cancel`.
Requires ≥1 live child (else 409 `no_children`). Creates or reuses the Stripe
customer (`subscriptions.stripe_customer_id`), opens hosted Checkout in
subscription mode, `quantity = live children`, 7-day trial, card required
(`payment_method_collection: 'always'`), `client_reference_id = org_id`,
`subscription_data.metadata.org_id`. If a live subscription already exists
→ 409 `already_subscribed` with `portal: true`. Returns `{ ok, url }`.

### `POST /api/consumer/portal` (requireParent)
`{ "return_url"? }` → `{ ok, url }`. 409 `no_customer` if none.

### `POST /api/consumer/stripe/webhook` — raw body, NOT behind consumerGate
Signature verified with `STRIPE_WEBHOOK_SECRET`. Inserts `stripe_events`
first (conflict → 200 `{ ok, duplicate: true }`). Handles:
`checkout.session.completed`, `customer.subscription.created|updated|deleted`,
`invoice.paid`, `invoice.payment_failed`, `customer.subscription.trial_will_end` (logged only).
Stripe status → ours: trialing→trialing, active→active, past_due|unpaid→past_due,
canceled|incomplete_expired→canceled, incomplete→(ignore), paused→canceled.
Writes: status, stripe_subscription_id, stripe_customer_id, trial_end,
current_period_end, quantity, cancel_at_period_end, billing_interval,
stripe_price_id, retry_at (from the invoice's next_payment_attempt),
last_payment_failed_at, canceled_at; `locked_at` when the state computes to
locked. Sends: payment_failed, subscription_cancelled emails (§6). Returns 200 always
after the ledger row exists (errors recorded in `outcome='error'`).

### Quantity sync
`syncSubscriptionQuantity(orgId)` in stripe.js — called by `POST /children`
and `DELETE /children/:id`. Live children count → Stripe subscription
quantity (`proration_behavior: 'create_prorations'`). Count 0 →
`cancel_at_period_end: true`. No Stripe subscription → no-op.

### Organisation-kind orgs never touch Stripe. `checkout`/`portal` → 409 `organisation`.

---

## 2. Automatic work (MRB-310)

### Term week and position
`currentTeachingWeek(academic_year, now)` (existing, backend) gives the term
week. SOW `academic_week` at KS3 is a per-(year, subject) teaching ORDER
(1..n), not a calendar, so a child's position is a cursor per subject in
`child_plans.cursors = { Biology: w, Chemistry: w, Physics: w }`, seeded at
onboarding to the term week for all three, or — when the parent picks a
unit — to that unit's first week for its subject and the term week for the
others.

### Generation (Sunday 18:00 London, `POST /api/consumer/cron/weekly`)
For every child in a family/organisation org where `orgAccess = full` and
`child_plans.paused_at is null`, for `week_start = next Monday`:
skip if `work_generation_runs(child, week)` exists. Otherwise, by intensity:

| intensity | lessons | practice | exam / unit check | sessions |
|---|---|---|---|---|
| light (alongside default) | 1 (subject with the lowest cursor; ties Bio→Chem→Phys) | 1 | — | 2 |
| steady | 2 | 1 | — | 3 |
| full (home-ed default) | 3 (one per science) | 1 | 1 exam item, replaced by a unit check on any week a unit ends | 5 |

Each lesson = the SOW row at that subject's cursor: `title = "{topic}: lesson {n}"`,
`sub = lesson title`, `ref = { lesson_slug, unit_code, subject, href }`, 20 min;
cursor then advances by 1. Practice = an `assignments` row composed by
`composeFromBank(currentSlugs, earlierSlugs, byLesson, 'standard', 10)` for
the child's class (`auto_generated`, `academic_week = week`), `ref = { assignment_id }`,
10 min. Exam = one `exam_questions` row the child has not answered, matching
key stage/subject of this week's lessons, `ref = { question_id }`, 15 min.
Unit check when a lesson generated this week is the LAST row of its topic:
`ref = { unit_code, subject, unit_name }`, 15 min, Friday.
Days: Tue, Thu, Sat for lessons/practice/exam in light/steady; Mon–Fri for full.
KS4 (Y10–11): SOW rows are seeded for KS4 from the generator's subtopic order
(4 blocks: tier × pathway, 'AQA'); there is no KS4 bank so no practice item;
exam items come from KS4 `exam_questions`.
Locked / read_only / none orgs: nothing generated, run row written with
`note='not_entitled'` so the week is not retried.

### Child: `GET /api/consumer/child/today` (requireChild)
```json
{ "ok": true,
  "child": { "name", "streak", "best": "78%|null", "bestUnit": "Health and disease|null" },
  "parent": { "id", "name": "Mum", "initial": "M" },      // first parent/staff thread partner
  "access": "full|read_only|locked|none",
  "items": [ { "id", "title", "sub", "mins": "20", "done": false, "by": "mb|parent", "byName": "Funmi", "href": "/ks3/…|/consumer/exam.html?q=…|…", "kind", "scheduled_for" } ],   // this week, not removed
  "later": [ { "day": "Thu", "title", "tag": "Mr Badmus|Funmi", "id" } ],   // future-dated this week
  "messages": [ { "id", "who": "you|parent", "text", "time", "unread": true } ],   // latest 20 with the parent
  "unread": 1,
  "flashcards": [ { "lesson_slug", "title" } ],  // child_flashcard_queue
  "notifications": [ { "id", "kind", "title", "body", "ref", "created_at" } ] }
```
`POST /api/consumer/child/work/:id/done` (requireChild, requireWritable) → `{ ok, streak }`.
Practice items are marked done automatically when `/api/assignment/complete`
completes the referenced assignment; unit checks and exams when their attempt lands.

### Parent controls (requireGuardian on `:id`)
- `POST /children/:id/pause` `{ "paused": true|false }` → `{ ok, paused, paused_at }`
- `POST /children/:id/intensity` `{ "intensity": "light|steady|full" }`
- `POST /children/:id/position` `{ "unit_code": "B3" }` or `{ "cursors": {…} }` → `{ ok, cursors, labels }`
- `GET  /children/:id/work?week=2026-09-07` → `{ ok, week_start, items:[…as dashboard…] }`
- `POST /children/:id/work` `{ "kind": "lesson|practice|exam", "lesson_slug"?, "unit_code"?, "question_id"?, "scheduled_for"?, "note"? }` → creates a work item with `set_by = parent id`; practice composes an assignment from the unit/lesson; returns `{ ok, item }`
- `DELETE /children/:id/work/:item` → soft remove (`status='removed'`), only items not done
- `GET  /children/:id/picker` → `{ units: [ { unit_code, subject, name, lessons: [ { slug, title, week } ] } ] }` for the child's key stage
- `POST /children/:id/generate` `{ "week_start"? }` — on-demand generation for one child (idempotent); used by the drive and by onboarding "start now"

### Cron (requireCron; also behind consumerGate)
- `POST /api/consumer/cron/weekly` `{ force?: true }` — checks it is 18:xx Europe/London unless `force`; generates; then sends digests (§6). Returns counts.
- `POST /api/consumer/cron/daily` — 09:xx London: trial-ending emails (trial_end in 36–60h), lock sweep (`locked_at` stamp).
- `POST /api/consumer/cron/hourly` — new-messages batch emails.

Streak: consecutive days ending today or yesterday with ≥1 done item, where
days inside a pause window are skipped (frozen), computed on read.

---

## 3. Chat (MRB-311) — requireConsumerUser
- `GET /api/consumer/chat/threads` → `{ ok, threads: [ { with: { id, name, role, initial }, last: { text, time, mine }, unread } ] }`
  parent: one per child; child: one per parent/staff; org staff: one per pupil.
- `GET /api/consumer/chat/messages?with=<id>&before=<iso>&limit=50` → `{ ok, messages: [ { id, who: "you|them", sender_id, text, time, read_at, created_at } ] }`
- `POST /api/consumer/chat/send` `{ to, text }` (requireWritable) → inserts via `callerClient(req)` so the RLS policy is the enforcement → `{ ok, message }`; policy refusal → 403 `not_allowed`.
- `POST /api/consumer/chat/read` `{ with }` → `{ ok, marked }`
- `DELETE /api/consumer/chat/messages/:id` → sender only → `{ ok }`
Realtime: clients subscribe to `postgres_changes` on `family_messages` with their own JWT.

---

## 4. Unit checks (MRB-312)
- `GET /api/consumer/child/unit-check?unit=B3` (requireChild) → `{ ok, unit: { code, name, subject, year, count: 10, minutes: 15, lessons: 6 }, previous: { date, pct, is_record } | null, access }`
- `POST /api/consumer/child/unit-check/start` `{ unit_code, work_item_id? }` (requireWritable) → `{ ok, attempt_id, time_limit_s: 900, qs: [ { id, topic, text, options: [4 strings] } ] }` — 10 bank questions, band standard, spread across the unit's lessons, deterministic per attempt; answers never sent.
- `POST /api/consumer/child/unit-check/submit` `{ attempt_id, answers: [ { id, chosen } ], elapsed_s }` → `{ ok, score, max, pct, breakdown: [ { topic, got, of } ], weakest, weak_note, is_record, flashcards_seeded: n }`
- `GET /api/consumer/children/:id/unit-checks` (requireGuardian) → `{ ok, attempts: [...] }`

## 5. Termly report (MRB-312)
`GET /api/consumer/children/:id/report?term=autumn-2026` (requireGuardian; also operator) → `{ ok, report: REPORT }` exactly Design's shape:
```
REPORT = { child: { name, surname, year, ks, mode: 'school|home', dates }, term, produced, ref,
           sessions: { done, set }, minutes, streakBest, checksAvg,
           units: [ { name, subject, lessons: '6/6', check: '55%|—', status: 'Complete|Continues in spring|In progress' } ],
           summary, progressNote, strengths: [], nextSteps: [], answers: [ { date, q, mark: '4/6 MB' } ],
           teacherNote: '' }
```
Terms: autumn = 1 Sep–19 Dec, spring = 1 Jan–Easter, summer = Easter–31 Aug (calendar rules in report.js).
`POST /api/consumer/admin/children/:id/report-note` `{ term, note }` (requireOperator).

## 6. Exam questions and marking (MRB-313)
- `GET /api/consumer/child/exam-questions` (requireChild) → `{ ok, questions: [ { id, topic, subject, marks, text, stem, done: null|'ai'|'human', scheme: [strings], answer, hits: [idx], feedback, human: { score, date, feedback } | null, waiting: bool, answer_id } ], quotaLeft, quotaTotal, resetDate: '1 October', access }`
  Pool: the child's key stage (and tier/pathway at KS4), all subjects.
- `POST /api/consumer/mark` `{ question_id, answer, work_item_id? }` (requireChild, requireWritable, aiCap('ai_mark')) → `{ ok, answer_id, score, max, hits: [idx], feedback, verdict }`
  Claude with the scheme in the prompt; `MARK_PROVIDER=stub` when no ANTHROPIC key (keyword overlap, flagged in response as `provider:'stub'`).
- `POST /api/consumer/exam-answers/:id/send-to-mb` (requireChild, requireWritable) → 429 `quota_reached` or `{ ok, quotaLeft }`; notifies nothing yet.
- `GET /api/consumer/admin/mb-queue` (requireOperator) → `{ ok, pending: [ { id, child: { id, name, year }, org, question: { text, marks, scheme }, answer, ai: { score, max, hits, feedback }, sent_at } ] }`
- `POST /api/consumer/admin/exam-answers/:id/mb-mark` `{ score, feedback }` → writes, in-app flags to child and parent, marking email to parent.
- `GET /api/consumer/children/:id/answers` (requireGuardian) → Design's `answers[]`: `{ id, date, marks, topic, question, answer, aiScore: '4/6', points: [ { n, ok, text } ], aiFeedback, human, humanScore, humanDate, humanFeedback, waiting }`.

## 7. Email (MRB-314) — `consumer/email.js`
`sendEmail({ type, org_id, to: { profile_id | email }, subject, html, text, dedupe_key })`.
Refuses any recipient whose profile role is `student` or address ends
`@children.mrbadmus.internal` → logs `skipped`. `RESEND_API_KEY` absent → logs
`dry_run` with the rendered subject (never sends). Types: `welcome`,
`child_login_details`, `trial_ending`, `payment_failed`, `subscription_cancelled`,
`mb_marked`, `new_messages`, `digest`. Wordmark "MrBadmus", no "AI" anywhere, plain-text part always.
- Digest: Sunday after generation, per parent (all children) and per org staff member (their pupils).
- `POST /api/consumer/prefs` (requireParent) `{ digest?, messages_email?, marking_email? }`.
- `GET /api/consumer/admin/emails?limit=` (requireOperator).

## 8. Caps and rate limits (MRB-315) — `consumer/limits.js`
- `aiCap(kind)` middleware: for users in a consumer org (or a school with `org_limits.enforce`), reads `ai_usage_counts`, compares with `org_limits` ?? `platform_settings.consumer_limits`; 429 `cap_reached` with `resets_at` (midnight/1st, London) and a friendly message. Applied to `/api/chat` (`tutor_turn`), `/api/explain-wrong-answer` (`explain`), `/api/consumer/mark` (`ai_mark`). On success records `ai_usage_events` with tokens and a cost estimate (Sonnet: £2.4/M in, £12/M out at 1.25 $/£ — constants, labelled estimate).
- Rate limiter: `makeLimiter({ name, windowMs, max, key: 'ip|user' })` → Upstash REST when `UPSTASH_REDIS_REST_URL`+`TOKEN` set, else in-memory sliding window (`limiter.backend` reported on `/api/health`). Applied: `/api/consumer/*` 300/15min per IP and 120/15min per user; AI routes 60/hr per user; `/api/consumer/child/login` 10/15min per IP (existing) + per username; `/api/consumer/family/ensure` 20/hr per IP.
- Admin: `GET /api/consumer/admin/usage?month=` → per org `{ org, kind, tutor_turns, ai_marks, explains, input_tokens, output_tokens, cost_pence_estimate, limits, enforce }`; `POST /api/consumer/admin/orgs/:id/limits` `{ tutor_turns_per_day?, ai_marks_per_month?, mb_marks_per_month?, enforce? }`.

---

## Frontend scaffolds (Night 2, functional only)
`consumer/` gains: `checkout-return.html`, `account.html` (billing card, portal button, prefs),
`child.html` (parent's child view: work list with labels, pause/intensity/position/add/remove, chat panel, answers list, unit-check history, report link),
`today.html` (child Today: items with labels, done buttons, later, chat panel),
`exam.html` (child exam questions + AI mark + send to Mr Badmus),
`unit-check.html`, `report.html` (print CSS). `overview.html` links to them.
`teacher/admin.html` gains: Mr Badmus queue, usage table, emails log, report-note — under the Consumer card, hidden when the flag is off.
