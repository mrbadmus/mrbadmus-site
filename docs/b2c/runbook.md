# The B2C support runbook

Everything you actually have to do by hand once families are paying. Written
for the person on the phone, not for a developer: every step names the screen
and the button.

**Where you work.** Sign in at **mrbadmus.com/auth.html** with your own
account, then open **mrbadmus.com/consumer/admin-accounts.html**. The console
has two pages and they are linked from its own header bar: **Accounts** and
**Marking**. If either page shows "Not found", you are signed in as someone
who is not a platform operator — the console deliberately refuses to admit it
exists rather than saying "no access".

Two words that get confused, so they are separated here for good:

- **Billing state** is what Stripe thinks about the money — Trial, Active,
  Past due, Cancelled, Locked, Not started, Invoiced. It is the coloured pill
  on the Accounts list.
- **Access state** is what the family may actually *do* right now — `full`,
  `read_only`, `locked`, `none`. It is computed in the database (a function
  called `org_access_state`) and it is not the same thing. A family whose card
  failed yesterday is **Past due** on billing and still **full** on access,
  because of the seven-day grace period below. Never read the billing pill as
  a permission.

---

## 1. What every state means, and what the parent sees

The parent reads this on **Account** (mrbadmus.com/consumer/account.html —
they reach it from the dashboard's side navigation, the row labelled **Account**). The
badge at the top right of the "Your plan" card is the label in column 2.

| Stripe / our status | Badge the parent sees | Access | What the child can do | What the parent reads, and the button |
|---|---|---|---|---|
| `trialing`, trial end still ahead | **Free week** | full | Everything | "Full access. Your card is on file and nothing has been charged." A panel shows **Free week ends** *date*, a progress bar, and "Then £x a month. Cancel before *date* and nothing is charged." Button: **Manage card in Stripe** |
| `trialing`, trial end passed (Stripe never told us it ended) | **Free week** | **read_only** | Read lessons and past work; cannot hand anything in | Same card, but every write button is greyed and a banner reads **Read only just now**. This state is a fault, not a plan: it means a `customer.subscription.updated` webhook never arrived — see §11 |
| `active` | **Active** | full | Everything | "Next payment *date*. Receipts go to your email each month." Button: **Manage billing in Stripe** |
| `active`, but they pressed cancel in the Stripe portal | **Cancelled** | full | Everything, to the end of the period | "No further charges." plus "Everything works until *date*. After that, logins open but no new work is set." Button: **Resume subscription** |
| `past_due`, **inside** the 7-day grace | **Payment failed** | full | Everything | "The last payment didn't go through." plus "Your card was declined on *date*. We'll retry on *date*. Work carries on as normal until *date*. If it still fails, work stops being set and the account pauses. Nothing is deleted." Button: **Update card in Stripe** |
| `past_due`, grace expired | **Payment failed** | **read_only** | Read only; cannot hand in | Same card. Child's banner: "You can read your lessons and look back at your work, but you can't send or hand anything in at the moment. Your grown-up will know why." |
| `canceled`, still inside the paid period | **Cancelled** | **read_only** | Read only | "Everything already here stays readable, and new work, marking and messages are paused. On *date* the account pauses fully. Termly reports stay downloadable for a year." Button: **Resume subscription** |
| `canceled`, paid period over | **Paused** | **locked** | Read only; the login still works | "The subscription ended and work has stopped being set." plus "Ended *date*. Your children's logins open but show no new work. Reports, marked answers and chat history are all still here." Button: **Restart · from £x a month** |
| `comped` (our own status — a free account you granted), still in date | **Active** | full | Everything | Reads exactly like Active. There is no card to manage |
| `comped`, run out | **Paused** | locked | As Paused above | As Paused above |
| `none` — signed up, never checked out | **Not started** | `none` | Look around; cannot hand in | "Nothing has been charged. The first week is free." Button: **Start your free week** |
| Organisation (invoiced) | **Active** while the invoiced period runs, else **Paused** | full / read_only / locked | — | No button. Organisations are invoiced by hand |

**The grace period is seven days after the period end**, and it applies only
to `past_due`. Seven days is set in two places that must agree — `GRACE_DAYS`
in the backend and the same number inside `org_access_state` in the database.

**Read-only vs locked, in one line.** They are the same for the child — read,
never write. They differ for the parent: **locked** shows the way back in
(Restart / Resume), read-only does not, because the subscription has not ended
yet.

**Nothing is ever deleted by any of these states.** Reports, marked answers
and chat history survive every one of them, and the child's login keeps
working. That sentence is safe to say on the phone.

**An organisation is different in kind.** It has no Stripe subscription at
all. It is entitled by a **seat cap** and a **period end** that you set by
hand when you create it, and it goes read-only for 14 days after that period
end, then locked.

---

## 2. Refund a parent

**There is no refund button anywhere in our product, on purpose.** Refunds
happen entirely in Stripe.

1. Accounts → click the family's row → the **Billing** panel → **Open in
   Stripe ↗**. That opens their customer page in the Stripe dashboard. (If
   that link is missing, the family has no Stripe customer yet and there is
   nothing to refund.)
2. In Stripe, open the invoice or payment you are refunding.
3. Use Stripe's own **Refund** action on that payment.
4. Refunding does **not** cancel anything. If they also want to stop, do that
   separately — they cancel in the billing portal themselves, or you set the
   subscription to cancel in Stripe.

⚠️ A refund in Stripe does not write anything into our records, so nothing
about it appears on the account's Timeline. Note it somewhere yourself.

---

## 3. Extend a trial

Accounts → the family's row → **Support actions** → **Extend trial 7 days**.
The button is greyed unless the account is on trial; the hint beside it reads
"Trial ends *date*" when it is live and "Not on trial" when it is not. On
success it prints "Extended to *date*." underneath.

Behind that one button are two different things, and which one runs matters:

- If Stripe is holding a live trial, **the trial is moved at Stripe** as well
  as in our records. The parent's next charge really does move.
- If there is no Stripe subscription (a family that never checked out, or an
  organisation), it grants a **comp** instead — full access, no charge, for
  seven days.

If the account is already **paying**, the button refuses with "This account is
paying. Comp it instead if you want to give it time."

**For any length other than 7 days there is no screen.** The button is
hard-wired to 7. Press it more than once, or use §7.

---

## 4. Reset a child's password

Children have no email address, so they can never reset it themselves. Two
people can do it.

**The parent does it.** Dashboard → pick the child → **Edit** (top right of
the child's name) → scroll to the **Login** card → **Reset password**. The new
password appears on screen once, under the heading "New password · write it
down now", with the note "It won't be shown again." The old one stops working
straight away.

**You do it, over the phone.** Accounts → the family's row → the **Children**
panel → the **Reset password** button on that child's line. The new password
appears on that line as "New password for *name* (shown once):". Read it out.
Nothing stores it, so if you lose it, press the button again.

Either way it is recorded on the account's Timeline.

## 4a. Reset the *parent's* password

Two routes, both email links — you cannot set a parent's password for them.

- Signed in: **Account** → the **You** card → the **Password** row →
  **Send reset link**. The button changes to "Reset link sent".
- Signed out: **mrbadmus.com/parents/sign-in.html** → **Forgotten your
  password?**

Both land on **mrbadmus.com/parents/reset-password.html** ("Choose a new
password" → **Save new password**). That is the parent-branded page; the older
`/reset-password.html` is the school one and is not for consumer families.

---

## 5. Remove a child, and what happens to the bill

Parent's own route: Dashboard → the child → **Edit** → to the bottom →
**Remove *name* from the account** → a confirmation panel appears → **Remove**
(or **Keep *name*** to back out).

What the panel tells them, and what actually happens:

- The child's login stops working today. **Their work is not deleted** — the
  removal is a soft one, and the panel says "Their reports and marked answers
  stay in your account for a year."
- **If other children remain**: the seat count at Stripe drops to the number
  of children still on the account, with proration, so the next bill goes
  down. The panel says "Your next bill drops by £x."
- **If that was the last child**: the subscription is **not** cancelled on the
  spot. It is set to end when the paid period does — they keep what they paid
  for. The panel says "With no children left, the subscription is cancelled at
  the end of this period."

⚠️ **Adding a child back does not un-cancel it.** That is deliberate: we
cannot tell our own cancel-at-period-end from one the parent set themselves in
the portal. If they add a child back and want to keep going, they must
**Resume subscription** on Account, which sends them to the Stripe portal.

There is no operator button to remove a child.

---

## 6. Unlock an account

Accounts → the family's row → **Support actions** → **Unlock for 14 days**.
The hint reads "No charge" when it will work and "Not locked" when it will
not; the button is greyed unless the access state is genuinely **locked**. On
success: "Unlocked until *date*."

It grants a 14-day comp, and it takes effect within about fifteen seconds even
if the person is on the phone saying "try it now".

If the account is not locked the route refuses with "This account is *state*,
not locked" — read the pill first.

---

## 7. Comp an account (free access)

⚠️ **There is no Comp button on any screen.** This is the one support action
in this runbook with no user interface. What exists:

- **Up to 14 days**, on a *locked* account: use **Unlock for 14 days** (§6).
- **7 days**, on an account that is not paying: use **Extend trial 7 days**
  (§3) — on a non-trialling account that button *is* the comp path.
- **Any other length, or on a paying account**: there is no screen. It needs
  the operator API route `POST /api/consumer/admin/orgs/:id/comp` with a
  `comped_until` date, or the equivalent row change in the Supabase SQL
  editor. Ask for that to be done rather than guessing at the console.

A comped family reads as **Active** to itself and has no card to manage. When
the comp date passes the account goes straight to **Paused**.

---

## 8. Create an organisation

Accounts → **+ New organisation** (top right, beside the search box). Fill the
form and press **Create organisation**:

| Field | What to put |
|---|---|
| **Name** | The organisation's name |
| **Seat cap** | The number of pupils the invoice covers. This is a ceiling, not a count — the list shows it as "cap N seats" |
| **Period end (invoice covers to)** | The last day the invoice covers, e.g. 2027-08-31. Access is full until the end of that day, London time |
| **Contact name** | The first person who will sign in |
| **Contact email** | Required. This becomes their invitation |
| **Email domain (optional — lets staff self-claim by domain)** | e.g. `brookfield.example` |

On success it prints "Created *name* (*academic year*)." One press builds four
things — the organisation, its academic year, the entitlement, and the
invitation for the contact. If any of the last three fail, the message names
them; get that looked at before anyone signs in, because a missing one fails
later and silently.

⚠️ The **seat cap and period end are the entitlement**. There is no Stripe
subscription behind an organisation and no automatic renewal. When the period
end passes, the organisation goes read-only for 14 days and then locks — put
the renewal in your own diary.

---

## 9. Mark from your phone

Open **mrbadmus.com/consumer/admin-queue.html** (or press **Marking** in the
console header).

On a phone the left-hand **Queue** list is hidden and replaced by a single
drop-down at the top of the screen — that is the whole difference. The
drop-down carries no visible caption; it is labelled only for screen readers,
as "Pick a queued answer". Everything else is the same page and works at 390px wide.

1. Choose an answer from the drop-down.
2. The header shows the child's name, year, mode and how long ago it was sent,
   then the question and the marks.
3. **Mark it.** Most questions show a checklist — tap a point to award or
   remove it, and the score above updates. It starts from the instant mark,
   and any point where you disagree is flagged "you +1" or "you −1". A
   levels-marked question has no checklist; type the number into the box
   instead ("No point-by-point mark scheme on this question (it is
   levels-marked) — enter the score directly").
4. **Write the note.** The box is labelled "Your note to *name*" and prompts
   "Two or three lines. What they did right, then the one thing to change."
   Four one-tap starters sit under it: **Agree with instant mark**, **Name the
   term**, **Finish the sentence**, **Quote the equation**.
   ⚠️ **The note is required.** A mark with no words is refused with "Write
   the feedback — a number on its own is not marking."
5. **Send mark · N/M**. The line beneath says who it goes to: the child, and
   an email to the parents.

**Skip for now** leaves it in the queue. The queue sorts by **Oldest first**,
**Newest** or **Organisations**.

---

## 10. Someone asks to delete their account

The parent does it themselves: **Account** → to the bottom → **Delete this
account** → a red panel appears → they must type `DELETE` into "Type DELETE to
confirm" → **Delete everything**. **Keep my account** backs out.

What that actually does, today:

1. Writes a row in the deletion ledger (`account_deletion_requests`) with a
   date **30 days** ahead.
2. Tells Stripe to stop renewing the subscription at the end of the period —
   **no refund, and access is not cut off**. They keep what they paid for
   while they think about it.
3. Emails them.
4. Shows them "Account scheduled for deletion … You can undo it here at any
   point before then", with an **Undo — keep my account** button.

**Where you see it.** Accounts → the family's row → the **Billing** panel
shows a **Deletion requested** line with the date, and the **Timeline** shows
"Account deletion requested" (and "Account deletion cancelled" if they undo).
There is no filter for pending deletions on the list — you have to know to
look, or watch for the email.

⚠️ **Nothing is actually erased by any code.** There is no sweep that reads
that ledger; the 30-day promise is currently kept **by hand**. When a date
comes due, the deletion has to be carried out deliberately. Diarise every
request you see.

⚠️ **Undo does not restart the billing.** The deletion is cancelled but the
subscription is still set to stop at the period end — on purpose, because
silently reinstating a charge somebody asked to stop would be wrong. Tell them
to press **Resume subscription** on Account.

---

## 11. When the daily health digest flags something

> The digest itself is **MRB-327 §5** and is being built now; it reads a new
> route, **`GET /api/consumer/admin/health`**. This section is written against
> what is knowable today and does not describe the digest's own wording.
> The route you can already check by hand, from any browser, is
> **`https://mrbadmus-backend.onrender.com/api/health`**.

### A failed Stripe webhook

A **webhook** is Stripe telling our server that something happened — a payment
taken, a card declined, a subscription cancelled. Our records are a *mirror*
of Stripe; entitlement is computed from that mirror. So a webhook that never
arrives means **Stripe and the family's access disagree** — most visibly, a
family that has just paid can sit there looking Past due or Paused.

Stripe retries a failed webhook by itself for days, so one failure is not an
emergency. What to do:

1. **Stripe dashboard → Developers → Webhooks →** our endpoint
   (`https://mrbadmus-backend.onrender.com/api/consumer/stripe/webhook`).
2. Look at the failed event. Stripe shows the response our server gave.
3. Use Stripe's **Resend** on that event. Replaying is safe — every event is
   deduplicated on its id and each handler restates the whole subscription
   rather than nudging it, so replaying, or replaying out of order, converges
   on the right answer.
4. Then reopen the family in Accounts and check the pill and the **Timeline**
   — a delivered event shows there in words ("Payment taken", "Payment failed
   (card declined)", "Subscription changed").

If **every** event is failing rather than one, check `/api/health` first: the
`stripe` block reports whether the four pieces of Stripe configuration are
present (`configured`, `webhook_secret`, `prices`, `portal_config`). A `false`
on `webhook_secret` means our server is rejecting every webhook's signature,
and no amount of resending will help until the secret is set on Render.

Seven event types must be registered on the endpoint:
`checkout.session.completed`, `customer.subscription.created`,
`customer.subscription.updated`, `customer.subscription.deleted`,
`invoice.paid`, `invoice.payment_failed`, and
`customer.subscription.trial_will_end` (the last one is what the trial-ending
email depends on).

### A failed email

Open `https://mrbadmus-backend.onrender.com/api/health` and read the `email`
block. It has one field, `mode`, and exactly two values:

- **`resend`** — live. Emails are really being sent through Resend.
- **`dry_run`** — **nothing is being sent to anybody.** The mailer does not
  error in this mode; it writes a "sent" row in our log and returns success.
  Verification emails, the welcome email, the Sunday digest, marking emails
  and every payment-failure warning all silently go nowhere.

`dry_run` means one thing: **`RESEND_API_KEY` is not set on Render.** Set it
and redeploy; the field flips to `resend`.

(The Night 4 live checklist says this field should read `live`. It doesn't —
the two values the code emits are `resend` and `dry_run`. `resend` is the
healthy one.)

An **individual** email that failed while the mode is `resend` is a Resend
problem — a bounce, a bad address, a rate limit. Where to look next:

1. Accounts → the family → **Timeline**. Every email appears there by its
   number: **E2** welcome / child login details, **E3** digest, **E4** marked,
   **E5** trial ending, **E6** payment failed, **E7** subscription cancelled,
   **E8** new messages, plus "Deletion notice". A line reading `E6 failed`
   rather than `E6 sent` is the one you want.
2. The **Resend dashboard**, for what happened to it after it left us.
3. If the parent never confirmed their address at all, Accounts →
   **Support actions** → **Resend verification email** (hint: "E1"). It
   refuses with "That address is already confirmed" if they have.

⚠️ Supabase's own built-in sender — the one behind the confirm-signup email —
is capped at a handful an hour and will rate-limit on a busy day. That is a
separate sender from Resend and `/api/health` says nothing about it.

### Other things `/api/health` tells you

- `db` — `ok`, `error` or `unreachable`. The route deliberately answers 200
  even when the database is down, so read this field rather than the status
  code.
- `limits.backend` — `upstash` is right in production. `memory` means the
  rate limits are counted per server instance only.

---

## Two things that have no screen at all

Named here so nobody hunts for a button that does not exist:

1. **Comp for any period other than 7 or 14 days** (§7).
2. **Actually deleting an account after the 30 days** (§10) — no code does
   this; it is manual.
