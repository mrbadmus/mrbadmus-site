# MrBadmus B2C — design manifest

Convention: one `.dc.html` per surface. Copy and mock data live in `const` blocks at the top of each file's logic; interactive state comes through template holes. Every consumer surface loads the KS3 design system (`_ds/…/styles.css`) with `class="rd" data-mode="ks3"` on the root. Brand mark = `MrBadmusDS.BrandMark` (orange chevron) + "MrBadmus" wordmark, Bricolage 800. No "AI" anywhere on these surfaces.

**Responsive.** Phone-first at 390. Parent surfaces gain a desktop layout at ≥960px: Dashboard swaps the tab bar for a left sidebar (nav, children, billing note) and lays child detail out in two columns; Account goes two-column; Signup gets a step rail. Child surfaces and the report stay single-column at any width.

Ticks, crosses and arrows are inline SVG (`.ks3-mark`), never typed characters — the shipped font subsets don't carry them.

## Drop 1 — parent + child

| File | What it is | Data it expects |
|---|---|---|
| `Parent Signup.dc.html` | Account → verify → add child (name, year, board/tier for Y10–11 only, mode, username check + suggestion, password) → "where is your child up to?" unit picker → children list → plan (monthly/annual, live maths) → Stripe hand-off → return screen with first week's work and login hand-over. Tweak `startStep` jumps to any step. | `PRICE`, `UNITS[year]` (half-term → units, subject), username availability check, `trialEnd`, generated first-week sessions per child. |
| `Parent Dashboard.dc.html` | Overview (one card per child), child detail (the three parent questions: doing the work / getting better / nudge), this week's work with "From Mr Badmus" / "Set by {parent}" labels and parent-removable items, set work, pause/resume, chat (unread state), marked answers list + detail (instant mark, points hit, examiner note, Mr Badmus's mark when landed), child settings (intensity, name, year, board, tier, mode, reset password shown once, remove child). Bottom tab bar Home / Messages / Account. Tweaks: `billingState` (banners + locked screen), `scenario` (normal / quiet-week / no-children). | `PARENT`, `CHILDREN[]` with `status` (active/paused/never/quiet), `days[7]`, `scores[]`, `work[]`, `messages[]`, `answers[]`, `humanLeft`, billing state + dates. |
| `Parent Account.dc.html` | Plan card with one treatment per billing state (trialing, active, past_due, cancelled, locked), children on the plan with per-seat price, link out to Stripe portal (we design the surround only), parent details, digest / marking email toggles, data download, cancel pointer, delete account (type DELETE, 30-day grace). Tweaks: `billingState`, `annual`. | Subscription state, next/failed/retry/access-end dates, seats, parent profile, notification prefs. |
| `Termly Report.dc.html` | The printable report (A4 via `doc-page`, flowing). Header strip, four stats, summary, units covered with unit-check %, progress chart, strengths / next steps, extended-writing log (MB = human-marked), teacher's note signed Mide Badmus. Print button hidden at print. | `REPORT` — child, term, sessions, minutes, units[], answers[], strengths[], nextSteps[], teacherNote. |
| `Child Login.dc.html` | Username + password, show/hide, two error strings, no reset path (points to the grown-up). | Username → password map. |
| `Child Today.dc.html` | Today screen: greeting, streak + personal best, unread-message card from parent, today's items labelled "From Mr Badmus" / "Set by {parent}", later this week, links to exam questions and unit check. Chat screen child side. Tweak `scenario`: normal / nothing-today / no-new-work (locked account, no meta-text). | `CHILD`, `PARENT.name`, `ITEMS[]` with `by: 'mb'|'parent'`, `LATER[]`, `MESSAGES[]`. |
| `Child Exam Questions.dc.html` | Pick (filters, done state), write (ks3 answer box, word count), marking interstitial, result (score, mark-scheme points hit/missed, examiner's note), "Send to Mr Badmus" with remaining count, quota-used state, sent state, human-marked result when it lands. Tweak `quotaLeft` 2/1/0. | `QUESTIONS[]` with `scheme[]`, marking service response (`hits[]`, `feedback`), human mark (`score`, `date`, `feedback`), monthly quota + reset date. |
| `Child Unit Check.dc.html` | Start (unit, count, minutes, lessons, rules), timed run (progress bar, MCQ via `.ks3-option`, short answer, skip/back, hand in, time-out), result (%, personal best, breakdown per sub-topic, weak area with a note, question-by-question review). Tweak `alreadyTaken` shows the previous score and turns start into a practice run. | `UNIT`, `QS[]` (choice or short with `accept[]`), previous attempt. |

### Empty / edge states covered
No children yet (dashboard). Child hasn't logged in (dashboard card + detail). No work done this week (`scenario: quiet-week`). Chat with no messages (both sides). Marking quota used up (child + parent copy). Unit check already taken. Account locked (dashboard locked screen, account card, child `no-new-work`). Also: username taken, first payment/trial banner, past-due grace, cancelled-until-date, remove-last-child billing consequence, time ran out on a unit check.

### Decisions I made that aren't in the brief — flag if wrong
- **Board, route (Combined / Triple) and tier only appear for Year 10–11.** KS3 has no tier and the system says it must not grow one. Y7–9 skip all three questions.
- **Child password is shown in plain text at creation and on reset**, once, because the parent has to hand it over. Never emailed.
- **Human-mark quota is per child per calendar month**, shown as "1 of 2 left", reset date named.
- **Pause freezes the streak** rather than breaking it. Locked account resets streaks but not progress.
- **Unit check retake is "practice"**: the first attempt is the record; later runs show in the child's own history only.
- **Report is A4** (UK councils). Header/footer are in-flow rather than repeating per page — repeating slots fought the streaming renderer.
- **Removing the last child cancels at period end** rather than immediately.
- Trial banner shows on every dashboard screen; past-due and cancelled banners likewise. The locked state replaces the dashboard rather than banner-ing it.

## Drop 2 — public site

| File | What it is |
|---|---|
| `Public Home.dc.html` | Hero with a real marked answer as the product glimpse; the three parent questions; how a week runs; who marks it (Mide's credentials); routes to home ed and pricing. |
| `Public How It Works.dc.html` | Five steps (who does what, when) with an example card each; accordion FAQs. |
| `Public Pricing.dc.html` | Live calculator: cycle × number of children, saving shown on annual; what's included; tutor comparison; money FAQs. |
| `Public Home Education.dc.html` | Three pillars (coverage, rigour, evidence); browsable scheme of work by year; the termly report; LA-facing FAQs. |
| `Public Organisations.dc.html` | Councils, alternative provision, tutoring centres; what an organisation account adds; contact form (name, work email, organisation, type, pupils). No price anywhere. |
| `Public Sign In.dc.html` | Chooser (child / parent), parent form with Google and reset, link to organisation sign in. |

Shared nav across all four content pages; nav links collapse under 900px (CTA and Sign in stay). No "AI" on any public page; the FAQ answers the question honestly when asked.

## Drop 3 — emails, organisations, admin

| File | What it is |
|---|---|
| `Emails.dc.html` | E1 verify, E2 welcome (login username, never the password), E3 Sunday digest (per-child strip, weak spot, not-started state), E4 marked by Mr Badmus, E5 trial ending (itemised first charge), E6 payment failed (grace dates), E7 cancelled (access-until date, kept data, resume), E8 new messages batched (max one an hour, quiet 9pm–7am). Subject + preview text on each. 600px, hex colours (no CSS vars in email), one CTA. |
| `Org Sign In.dc.html` | Staff sign in. Wordmark only. |
| `Org Dashboard.dc.html` | Pupils table with search, group and needs-attention filters; pupil detail (week, checks, answers, reset password, set work); groups (shared year/unit/intensity); set work to everyone / group / pupil; messages (pupil–caseworker threads, reply); bulk add pupils against the seat cap; organisation account (seat cap, one annual invoice, staff, DPA, export). Sidebar on desktop, select-nav on mobile. Wordmark only, no chevron. |
| `Admin Marking Queue.dc.html` | Mr Badmus's queue sorted oldest / newest / organisations, age turns ember past 48h; marking pane starts from the instant mark, each scheme point toggles, note with snippets, send (needs a note). Dark room tokens, wordmark only. |
| `Admin Accounts.dc.html` | Stats strip; every account filtered by billing state or organisation; detail with children/pupils, billing, support actions (extend trial, reset password, resend E1, add human marks, unlock 14 days), timeline. Wordmark only. |

### Decisions in Drops 2–3 — flag if wrong
- **Organisations are invoiced annually against a seat cap**, BACS, no cards, no trial. No organisation price appears anywhere public (ruled).
- **Pupil–staff messaging is on for organisations**, same as families, logged. No parent invites in v1; the Sunday digest goes to the caseworker (ruled).
- **Staff surfaces (Org and Admin) carry the plain wordmark only**, no chevron (ruled).
- **Human-mark quota applies per pupil in organisations too**, and staff can send on the pupil's behalf.
- **Admin surfaces use the dark-room tokens** so they are never mistaken for a customer screen.
- **Marking requires a written note** (10+ characters) before sending; the score alone isn't enough.
- Emails carry no password ever; E2 says so.
