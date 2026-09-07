# MRB-330 — Student surfaces, and the seamlessness fixes

6 September 2026 — a **Sunday**, which is the condition the MRB-329 audit was
written on and the reason the week findings could be reproduced rather than
simulated. Work done in `main`, on top of MRB-328's report commit (`0a347c314`).

Everything below is measured. Where a claim is not measured it says so.

---

## What shipped, by the audit's finding numbers

| # | Sev | Finding | State |
|---|---|---|---|
| F1 | S1 | Work composed on first open is stamped with a past due date → LATE/MISSED | **closed** |
| F2 | S1 | The week rolls over on the year's `start_date` weekday, not a fixed day | **closed** |
| F3 | S1 | Held school shows an empty card badged OPEN with a live button | **closed** |
| F6 | S1 | Student and teacher disagree about what week it is | **week closed**, `SET` date not — §8 |
| F23 | S1 | A template shoutout reaches the child as a blank card | **closed** |
| F24 | S1 | The reminder banner is drawn and removed 12ms later | **closed** — and a second, older half of it found and closed too |
| F31 | — | No Messages surface anywhere in the staff estate | **built** |
| F25 | S3 | Deselecting a template leaves Send enabled and silently dead | **closed** |
| F13 | S4 | The "KS3" pill takes the width the breadcrumb needs | **closed** (ruled cut) |
| F12 | S2 | "LIVE RIGHT NOW · 185/185 · the rest are on their way" | **closed** (ruled cut) |
| F14 | S4 | The footer's only link points at the page you are on | **closed** (ruled cut) |
| F27 | S1 | A `school_admin` has no route into any class | **route closed by MRB-328** (verified); the "My classes" dead end is not — §7a |

---

## 1 · The week, and the late lie (F1, F2, F6)

**Ruled by Mide: the teaching week rolls on SUNDAY 00:00 UK.**

The week was "days since the academic year's `start_date`, in sevens", so it rolled
over on whatever weekday the year happened to open on. A year starting Tuesday kept
Monday in last week; a Wednesday start kept Monday *and* Tuesday. Composition is
lazy — the assignment row is written the first time somebody opens the page — and
the due date came from the *week*, not from when the row was created. On Sunday
6 September a Year 8 was therefore composed week 1's work, due the previous
Thursday, and badged LATE before she had done anything.

Sunday rather than Monday is the deliberate half of the ruling: the week has to turn
over before the weekend ends, or a child getting ahead on Sunday evening is handed
the week that has just finished with its deadline already behind her.

**The week is still named by its Monday.** A school week is Monday to Friday; every
label and range a human reads is built from that Monday. Sunday is when the *number*
changes, not what the week is called. Because of this the teacher's week bar reads
`31/08/26 · AUTUMN WEEK 1` exactly as it did before — the label did not move, the
disagreement underneath it did.

### Where the rule lives now, and what stops it drifting again

F6 was not a bug in one of these, it was the fact that there were four:

| | |
|---|---|
| backend `assignment-compose.js` `currentTeachingWeek()` | serves the work |
| `shared/teacher-live.js` `teachingWeek()` | the week bar, the digest range |
| `shared/teacher-data.js` `computeWeekWindow()` | "this week" |
| `shared/student-data.js` | its own copy of that algorithm |

`verify_week_truth.py` is new and holds all of them against the backend's, for every
day of a whole academic year, across six different year-start weekdays — 1 623
day-weeks. It fails if they ever disagree, and it fails loudly rather than silently
if the backend repo is not on the machine.

The comparison happens in **London's calendar, not UTC's**. Sunday 00:00 UK is
23:00Z on Saturday under BST, so a UTC-only rollover would turn the week over an
hour late for half the year.

### Work is never born late

Sunday alone does not close it. A class whose first opener arrives on the **Friday**
— after Thursday 18:00, inside the week they are correctly standing in — would still
get a deadline in the past, and `is_late` is `now > due_at`. `dueAtNotBornLate` gives
a composition the next occurrence of its class's due weekday that is still ahead of
it. The row keeps its own `academic_week`: the questions really are that week's
lessons, and re-keying them would make the row lie about its content. Only the
deadline moves.

### Existing assignments keep their meaning — proved, not assumed

I was asked to re-key or compute on read, my call. **Neither was needed, and that is
a measured result rather than a preference:** for the default Thursday deadline the
new Sunday-based week produces the *same date* as the old `start_date`-based week,
for all 39 weeks of the year. No stored `due_at` is reinterpreted, no `is_late` is
recomputed, no migration was written. The two continuity proofs are tests in
`test_assignment_compose.js`.

The one place the arithmetic had to move to stay still is the consumer (B2C)
practice week, whose deadline is the Sunday that *closes* a week — and week N's own
day-7 is now the Sunday it *opens* on. `consumer/work.js` compensates with `week + 1`,
and that compensation reproduces the old date exactly, week by week. Left alone it
would have pulled every consumer deadline seven days earlier; since the Sunday
scheduler writes a week ahead, it would have been setting work already overdue.

⚠️ **The KS4 Weekly Challenge clock is untouched.** It resets Friday 10:15 and lives
in `server.js` `getWeekStart()`. The `server.js` diff is two hunks and neither is in
it. Two clocks, two products.

### Verified on TEST, on the audit's own Sunday

A fresh student, real sign-in, real browser, throwaway school with a **Tuesday**
year start — the audit's exact shape. Read back from the database, not the screen:

| | before (the audit) | after |
|---|---|---|
| `assignments.academic_week` | 1 | **2** |
| `assignments.due_at` | Thu **3** Sep 18:00 — in the past | **Thu 10 Sep 2026 18:00 London — in the future** |
| `assignment_submissions.is_late` | `true` | **`false`** |
| the bench | `MISSED` · `Overdue` · `DUE THU 3 SEP` | `ON THE BENCH NOW · DUE THU 10 SEP, 18:00` · `4 days left` |
| the completion screen | LATE, three times | `MARKED · WEEK 02` |

Running the pre-MRB-330 arithmetic against the same instant still returns week 1, so
the difference is the fix and not the fixture.

One honest qualification: the word MISSED does still appear once in the rendered
page — in the term-spine's static legend (`● DONE ● OPEN ◇ MISSED`). It is a key,
not a claim about this child. The bench itself asserts none of LATE / MISSED /
Overdue.

Screenshots: `shots/p1-03-class-after.png`, `shots/p1-09-completed-after.png`.

---

## 2 · Held state, honestly (F3)

The backend has always been unambiguous — `200` with `assignment: null`,
`reason: 'assignments_not_open_yet'` and `detail.opens_on`. Nothing on the student
page read it. A held school's child saw a card badged **OPEN**, headed "ON THE BENCH
NOW", with Questions / Draws on / Set / Due all blank, three tick-boxes, and a live
"Open the assignment →" that opened nothing *and ticked the checklist from 0/3 to
1/3*. The admin screen that turns the dial already promised, in as many words, that
students see a sentence saying no work is set. The promise was written; the reading
of it was not.

`benchOpen` now closes on the held state, which takes the badge, the docket, the
checklist and the button off the page in one condition rather than six empty
strings. The card carries the ruled line and nothing else.

⚠️ **Held is not Design's `fresh` state**, which was the obvious vehicle and the
wrong one: `fresh` also empties the work list, the shoutouts and the leaderboard,
which would take last week's completed work off the page. The ruling is explicit
that history stays. It does — held changes this week's card and nothing else.

`teacher/admin.html`'s promise now quotes the line a child actually reads, so the two
surfaces stop contradicting each other.

Verified on TEST against a school with `assignments_open_from = 2026-10-05`:

- `[data-mrb-held]` exists; its text is exactly `This week's work isn't live yet`
- the bench element has **two** children — a decorative rule and that one paragraph
- no "Open the assignment", no "ON THE BENCH NOW", no `0 / 3`, no DUE row
- **zero** assignment rows were ever written for the held class
- pressing the bench frame and all three descendants leaves the page byte-identical

Before: `../mrb329/shots/p1-14-held-school.png`. After: `shots/p1-14-held-school-after.png`.

---

## 3 · "Remind all" reaches the child (F24)

The teacher's half was already complete and well-worded — the count rose, the button
said "Reminded today". The child's half was built and then destroyed 12 milliseconds
later, every time.

The cause is one line of architecture rather than a bug in the banner.
`student-runtime.js`'s `draw()` does `host.textContent = ""` and rebuilds — a full
rebuild, deliberately, with no virtual DOM. Anything appended to the page from
*outside* the template therefore lives exactly until the next state change.
`drawReminder` appended into `<main>`, which is inside the rebuilt region.

So the fix is not a better selector or a later call: the runtime now supports
**after-draw hooks**, and the banner is one. It is redrawn after every rebuild —
state rather than a one-off insert, which is what the ruling asked for. Dismissal is
a flag for the same reason: removing the element would last until the next paint.

The same mechanism carries the held-school line, and the precedent already existed
in that file — MRB-287 carries form-field values over the rebuild for exactly this
reason.

**Measured on TEST with the audit's own MutationObserver method**, installed before
navigation:

```
+   827 ms  APPEAR
+   837 ms  DISAPPEAR     ← the render pass that used to be the end of it
+   837 ms  APPEAR        ← the after-draw hook puts it straight back
+  5091 ms  DISAPPEAR / APPEAR
+  6792 ms  DISAPPEAR / APPEAR
+  8498 ms  DISAPPEAR / APPEAR
+ 10287 ms  DISAPPEAR     ← Dismiss. Nothing follows it.
```

`data-mrb-renders` went **2 → 3 → 4 → 5** with the banner present at every mark, so
those were real rebuilds and not a still page. After Dismiss it was gone at render 5
and still gone at 6. `read_at` flipped for the dismissing child only; the other
child's stayed null.

### And a second defect, found because the first was fixed

With the banner finally surviving long enough to be used, the *other* half of the
rule turned out never to have worked either. "Opening the work counts as reading the
reminder" was implemented as

```js
var go = document.querySelector('a[href*="/student/assignment"]');
```

and **the ported class page renders no anchors at all** — every control on it is a
`<button>`, the bench's primary one included, which navigates by setting
`window.location.href`. Measured: 0 anchors, 0 selector hits, `read_at` still null
after a child had opened her work and answered it. A reminder could only ever be
cleared by pressing Dismiss, so a child who did exactly what she was asked kept
being asked.

The replacement is deliberately **not another selector**. It runs on the assignment
page, where "she opened her work" is not an event to be caught but a fact already
established by the page being there. Nothing about it can go stale when the markup
moves again — which is the real lesson: a handler keyed on markup the port had
already changed, failing silently, in a file whose gates were all green.

Evidence: `shots/p4-03-reminder-after.png`.

### The reminder, end to end — the second pass

After the mark-read fix, re-verified on a third throwaway school with a real
backend-composed assignment (15 questions from the real scheme and bank):

| step | result |
|---|---|
| teacher presses "Remind all 2" for real | 2 rows written, both `read_at = null` |
| student A sees the banner and presses the bench's primary button | lands on the assignment page — and the control is a `BUTTON`, which is exactly why the old anchor selector never fired |
| A's `read_at` after opening | **`2026-09-06T23:39:05.311+00:00`** — non-null |
| **student B, who never signed in** | **still `null`** — the write is scoped to the viewer, not a blanket update |
| A re-opens the class page | banner gone |
| Dismiss on a fresh reminder | `read_at` flips again; banner absent across three forced re-renders |

The control row is the part that matters: it rules out the fix having simply marked
everything read.

Evidence: `shots/p4-04-markread-assignment.png`, `shots/p4-05-markread-class-clean.png`.

---

## 4 · Admin → Messages (F31)

The auditor could not find a Messages surface anywhere in the staff estate. It did
not exist in the UI — but it existed as a **ruling and an RLS policy**: migration
`20260903200007`'s own comment says *"school admins read `class_shoutouts`
SCHOOL-WIDE. That read IS admin.html's 'Messages' audit surface, and Mide calls it
the safeguarding control."* So this was a missing screen, not a missing permission,
and **no migration was needed or written**.

Built into `teacher/admin.html` (hand-written; edited directly). One school-wide
list, newest first, merging both directions a teacher can write to a child:
`class_shoutouts` and `submission_feedback`. Each row carries the teacher, the
student, the class, the date and the body. Reads are batched — two table reads in
parallel, then two `.in()` resolutions — so it is not N+1, and the promise starts
before the rest of the page and is awaited after the page is revealed, leaving
admin.html's 2.7s render alone.

Two decisions worth stating:

- **Soft-deleted messages are shown, and marked as deleted.** The policies expose
  them to an admin deliberately; filtering them here would quietly undo the most
  sensitive thing that migration did. A deleted message is exactly what a
  safeguarding log must still show.
- **A template-only shoutout shows its sentence**, not a blank row — which is the
  same defect as F23 and would have defeated the point of the log.

Verified on TEST with throwaway admins: reachable by clicking `Admin` in the nav,
lists both kinds, names resolved, a soft-deleted row still listed and tagged.

**A flagged risk that did not materialise.** The name-resolution reads
(`profiles`, `assignments`, `submissions`) are gated on `auth_user_role() = 'admin'`
while the two message policies use `auth_user_has_scope('school_admin')`, so an admin
who holds the scope by a `staff_scopes` row alone might have read the message and not
the name of the child it was about. Both shapes were tested — scope-only and
`role='admin'` — and their output was byte-identical, names fully resolved, confirmed
at the RLS layer with each admin's own JWT. Recorded because it was a real risk and
because the next person to touch those policies should know the two predicates differ.

Evidence: `shots/admin-messages.png`, `shots/admin-messages-admin_scope.png`,
`shots/admin-messages-deleted-admin_role.png`.

---

## 5 · Shoutouts (F23, F25)

**F23 — a template shoutout arrived blank.** `class_shoutouts` stored a
`template_key` and left `message` null; the child's card renders `message`, so the
path the composer pushes teachers towards — six templates, offered first — sent a
child their teacher's initials, their own name, "TODAY", and no words.

Fixed **at the write**, as ruled: a template send now persists the template's own
sentence alongside its key. The CHECK constraint was read on TEST before choosing
this rather than assumed — `class_shoutouts_content_chk` is an **OR**, not an XOR, so
a row carrying both columns is legal. A teacher's typed words always win; the
template sentence is only filled in when nothing was typed.

That change has three readers, and all three were followed up:

| reader | what it does now |
|---|---|
| the child's card | shows the sentence — the blank card is gone |
| the teacher's own feed | compares the two, so a template does not print its sentence twice |
| Admin → Messages | same comparison — **caught by driving the new surface**, which was rendering "Smashed a tough topic — Smashed a tough topic" |

The third is the one worth recording: it was two of this run's own changes meeting,
and only the fact that someone actually opened the page with real rows in it found it.

**F25 — Send stayed enabled with nothing to send.** The first template is
pre-selected, so pressing it *deselects* it, leaving a form with a student, no
template and no message; Send stayed enabled and the press did nothing. Send is now
genuinely disabled — the DOM property, not just styling — until a template or some
text exists, and re-enables the moment either arrives.

Verified on TEST, counting rows rather than trusting the screen: with no template and
no text the button reads `disabled = true` and pressing it leaves the row count
unchanged (1 → 1); picking a template or typing re-enables it; a template-only send
writes both columns; a free-text send writes the typed message with a null key.

Evidence: `shots/v1-shoutouts-as-child-after.png`, `shots/p2-teacher-feed.png`.

---

## 6 · The phone, and the ruled cuts

### The KS3 header (F13)

The brief called it "the truncated KS3 header pill". The audit's measurement showed
the pill was the one thing *not* truncated: at 390px it kept its full 63px while the
breadcrumbs collapsed to `Aci… › Ac…` — two ellipses that name nothing.

Removing the pill (ruled) gave that width back, and "Acids and alkalis" went from
**46px to 90px**. It still wanted 131px, so the header still read `Acids and a… ›
Acid + m…`. Two shorter ellipses is not the ruling being satisfied — the ruling was
to let the breadcrumb breathe, and a breadcrumb that names nothing has not.

So below 420px the elision is lifted and the row takes a second line. Measured after:

| crumb | rendered | needed | state |
|---|--:|--:|---|
| Acids and alkalis | **131px** | 131px | **full** |
| Acid + metal | **97px** | 97px | **full** |

Nothing is dropped, both names are readable, and the header grew from 64px to 66px —
the trail's two lines still fit inside the rail's existing minimum height.

⚠️ **`overflow: hidden` stays, and that is a finding.** Lifting it to `visible`
alongside `white-space: normal` read as the natural pairing and cost a **320px
regression**: `food-chains-and-food-webs` and `magnets-and-poles` began scrolling the
document sideways by 1px and 11px. `ks3_overflow.py` caught it. I confirmed it was
mine by reverting the rule at runtime and watching `scrollWidth` return to 320 —
worth recording, because neither overflowing element was a crumb (one was a 760px SVG
figure, the other the chat modal), so reading the symptom alone would have exonerated
the change. Wrapping buys the legibility; the clip guarantees nothing spills. Both
gates now pass at 390 and 320.

`shared/class-entry.js` uses `.ks3-pill` as the insertion anchor for a signed-in
student's class link, and already degraded to `appendChild` when it is absent, so no
JS changed. `.ks3-nav-spacer` was kept for that reason and is now the only thing
holding that link at the right edge.

### The other ruled cuts

- **"LIVE RIGHT NOW · 185/185 · the rest are on their way"** and its three per-subject
  bars — gone, with the bar-building code and its now-unfed template keys. The slot is
  **clean**: no placeholder, as ruled. `.ks3-hub-top` is `repeat(auto-fit, minmax(...))`,
  so the empty track collapses and the hero takes the rail on its own.
- **"All of KS3"** — gone from the footer of every KS3 page. An empty links row now
  emits no `<div>` at all rather than an empty one.
- The `· N live` fragment on the subject cards (F30) was **not** in the ruled cuts and
  is deliberately left.

### Stat tiles

The audit named "stat tiles" as an alignment defect. The cause turned out to be worse
than alignment. `practiceAnswered` and `practicePct` are deliberate COULD-NOT-SOURCE
empties — the practice round writes nowhere, so neither is knowable. Passed straight
through:

| | before | after |
|---|---|---|
| the value line | `''` → **0px tall**, so the tile was 26px shorter than its three siblings and the 2×2 grid stopped lining up | `—`, the same fallback its siblings already use → **26px**, aligned |
| the progress fill | `width:` with nothing after it is an **invalid declaration**, so the fill fell back to auto width — a **full orange bar**, measured at **200px of a 200px track**, on the one reading that records nothing | `0%` → **0px** |

The full bar is the part that mattered: it read as *complete*. Both fallbacks are
written beside the three siblings that already make the same decision, so the data
stays honest about being unsourced. Visible on `shots/p1-14-held-school-after.png`:
PRACTICE now shows `—` over a faint empty rule, level with AVG SCORE beside it.

### Card edges

I could not find this one, and say so rather than inventing a fix. Mide's own
screenshots are not on this machine, so I measured instead: at 390px the student class
page has **no element exceeding the viewport** and **no card whose left and right
insets differ by more than 1px**. `ks3_overflow.py` passes at 390 and 320 across 40
built pages. If there is a specific card Mide is looking at, I need the screenshot.

---

## 7 · Redundancy on the student class page — the verdict table

The rule given: **keep only what Design draws, or what a ruling added.** Checked
against Design's own delivery in `docs/ks3/design-reference/student/`, not from memory.

| candidate | drawn by Design? | verdict |
|---|---|---|
| `WELCOME BACK, AY · YOUR CLASS` | **yes** — `Welcome back, Ayo · your class`, an eyebrow above the class name in `Class View - standalone source.dc.html`. The caps are CSS. | **keep**, unchanged |
| the SCIENCE pill | **yes** — a hero chip, bound live to `klass.pill_label`; it already drops cleanly when a class carries no subject | **keep**, unchanged |
| the YOUR TEACHER pill | **yes** — Design drew a chip *to hold a teacher's name*, with an avatar beside it | **keep — and fill** (below) |
| `Good week, AY.` | **yes** — one of the eleven values in the done-bench subtree grafted from Design's donor; `student_rulings.py` enumerates it | **keep**, unchanged |

Three of the four were already exactly what Design drew, so the honest verdict is that
this is not redundancy — it is the design.

The fourth was. **The "YOUR TEACHER" chip has been rendering the literal words "Your
teacher" over an empty avatar circle on every student's page since it was written**,
marked COULD NOT SOURCE because a student has no read policy on a teacher's `profiles`
row. That was true when it was written and has not been since:
`class_teachers_for_viewer` (migration `20260820001231`) is the SECURITY DEFINER RPC
that exists for precisely this, and the *assignment* page has been using it for weeks.
The class page simply never asked. So the chip is kept and filled — Design drew it to
hold a name, and the name is readable.

⚠️ With two teachers on a class the RPC returns names **without ids**, so there is no
way to say which one the chip means, and picking the first would put a name in front
of a child that may not be theirs. With anything other than exactly one teacher, the
old words remain.

The audit read the empty chip as **F22**, a TEST artefact from a missing migration.
That reading was wrong, and it is worth recording: applying the migration would not
have filled it, because the class page never called the RPC. The empty pill was live
on production too.

---

## 7a · A school_admin's route into a class (F27) — verified, and the audit half-corrected

The audit reported that a `school_admin` is told "You are not teaching any classes
this year", lists nothing, and has **no route from the UI into any class** — every
admin screen in that audit was reached by pasting a class UUID into the address bar.

That is now half wrong, and the half that is wrong matters most. **MRB-328 J3 built
the route**: `teacher/admin.html` links each staff row to
`/teacher/classes.html?teacher=<id>`, which draws THAT person's class cards and
heads the page with their name, and each card opens class-detail through the
existing acting-as-admin path.

Verified on TEST with two throwaway admins who teach nothing — one holding
`school_admin` by a `staff_scopes` row with `profiles.role = 'teacher'`, one holding
both. **Two clicks, no typed URLs:**

> `/teacher/today.html` → **Admin** in the nav → `/teacher/admin.html` → the
> **9b/Sc7** row → `class-detail.html?class=…`, rendering the full roster, the
> "ACTING AS ADMIN" marker and live controls.

The Teachers rows work the same way. `profiles.role = 'admin'` made no observable
difference; the `staff_scopes` row alone suffices.

**The half that is still true:** `/teacher/classes.html` reached directly — which is
what the "My classes" tab in the nav does — still answers a question the admin did
not ask. It renders one bare sentence, *"You are not teaching any classes this
year."*, with no nav and no way back except the browser's Back button. So the block
is gone but the dead end is not, and an admin who takes the obvious tab still meets
it. Screenshot: `shots/p3-03-classes-after.png`. Not fixed here — it is a change to
a generated page's empty state and its scope, and it wants its own ruling on what an
admin should see there.

---

## 8 · Open items, and what I did not close

### Left deliberately, with the reason

**The teacher's "SET" date still disagrees with the student's (F6, second half).**
The student's docket shows `created_at` — when the work was actually set. The
teacher's rail shows `due_at − 7 days`. On a class verified in this run the same
assignment reads `SET Sun 6 Sep` to the child and `SET Fri 4 Sep` to the teacher.

I did not change it, because the teacher's side is a **ruling** (24 August 2026) and
its reasoning is sound and written down: `created_at` is the row's insert stamp, and
a term composed in one batch gives every assignment in it the same `created_at`,
which collapses the whole twelve-week rail onto a single range — "it fails silently
and it fails on exactly the data the platform actually has." Overturning that to
match the student would reintroduce the defect it was made to fix.

So this is a product question rather than a bug: **what does "SET" mean?** One of the
two surfaces should change, and which one is Mide's call. Whichever way it goes, the
week fix has made the gap smaller — both now agree about the week, and only the label
inside it differs.

**The empty subject chip — a new finding, and the fix is one word with a trap.**
The audit read the small empty pill in the student hero as **F22**, a TEST artefact
from a missing migration. That reading is wrong and the correction matters: it is the
**subject** chip, rendering as an 18×14 bordered box whenever a class carries no
`pill_label`. It was live on production too, and applying the F22 migration would not
have touched it.

P6 already ruled on exactly this shape — "an empty chip is not nothing, it is a small
bordered box with nothing in it, which is worse than either state" — and built the
`drop` flag for it. `classSize` and `envBadge` carry that flag; `subjectLabel` does
not. So the fix is the word `"drop"` on one binding.

⚠️ **I did not make it, and this is why.** `build_student_port.py` states an invariant
in a comment: *"no two drops share a parent's child list."* I measured the paths
rather than trusting it — `classSize` and `subjectLabel` are children **0 and 2 of the
same parent**. Adding the flag falsifies the stated invariant, and whether it is
actually safe depends on the removal order of the two drops, which is currently
accidental rather than designed. That is a change that wants its own run, its own
reasoning, and a gate — not a one-word edit at the end of a long night.

**F30 — "58 lessons · 58 live" on the hub's subject cards.** Not in the ruled cuts,
deliberately left.

**F15, F16, F32, and the set-work branch's findings** (F7, F17, F18, F19, F25's
sibling, F29) were not in this run's scope and are untouched.

**Two boundaries on the new mark-read, found by verifying it and left as they are.**

1. *A broken assignment keeps the reminder unread.* `markRemindersReadOnOpen` runs
   after the mount, so an assignment that cannot render — one with no questions, which
   throws in `buildAssignment` — aborts before it. The child sees "This week's work is
   not ready yet" and stays on the chase list. That is arguably the RIGHT answer: a
   child who could not get her work should still be chased. Recorded because it is a
   real condition under which "opening the work" does not clear the reminder.
2. *No `keepalive` on the write.* Unlike the per-answer save path, `markRemindersRead`
   is a plain update, so a child who opens the assignment and instantly navigates away
   may not be marked read. The failure mode is benign and is exactly what that
   function's own comment already calls the honest outcome — the line appears once
   more on the class page. Making it keepalive means leaving the Supabase SDK for a
   raw fetch, which is a bigger change than the defect warrants tonight.

### Found while verifying, not fixed

**The shoutout "Remove" control does not soft-delete.** Four attempts across three
Remove buttons: no confirm dialog, no console error, and **zero** rows changed
`deleted_at`. Found while verifying Messages, outside this run's scope, and unfixed —
but it is adjacent to the safeguarding story and it fails in the worst direction: a
teacher who believes they have taken a message back has not. The soft-deleted state
in the Messages screenshots had to be produced with a service-role write instead.

**An assignment can be composed with zero questions and still present as work.** On a
throwaway Year 9 class with no bank rows for its scheme, composition wrote a row with
no questions; the bench then showed `QUESTIONS` and `DRAWS ON` blank, with the
checklist and "Open the assignment" live — the F3 shape, arriving by a different road.
It is a seeding artefact here rather than something a real class would hit today, but
it is the same family and worth a look when the empty-week work lands.

### Open on Mide

- **What "SET" means**, above.
- **The `slt` asymmetry in Messages.** `submission_feedback` is readable school-wide by
  `school_admin` *and* `slt`; `class_shoutouts` only by `school_admin`. That split is a
  ruling from the migration, not an oversight, so the surface tells an `slt` viewer
  that the shoutouts they can see are their own classes' rather than the school's.
  Worth confirming it is still what you want now the log exists.

---

## 9 · How this was verified

- **TEST project `qeppkiswvclkkwbxmlok` only.** Production was never written to and
  never read as an authenticated user. No migration was written or applied anywhere;
  `supabase db push` was never invoked. Two of the fixes turned out to need no schema
  change at all, and that was established by reading the constraints rather than
  assuming: `class_shoutouts_content_chk` is an OR, and the Messages RLS already
  existed and already said what it was for.
- **Real sign-ins.** Every persona typed an email and password into `auth.html` and
  pressed Sign In. No injected sessions. Each seeded account proved a real password
  grant before anything relied on it — the known GoTrue-500 trap on seeded TEST users
  did not bite.
- **Counts come from the record.** Every number here was read back from
  `assignments`, `assignment_submissions`, `student_notifications`, `class_shoutouts`
  or `submission_feedback`. Where the screen and the record disagreed, the
  disagreement is the finding.
- **The phone was a phone** — 390×844, DPR 2, `mobile: true`, touch emulation on, set
  before navigating. Screenshots taken with `Page.captureScreenshot` directly, because
  `ks3_browser.screenshot()` re-issues the metrics with `mobile: false`.
- **The clock was not faked.** The week work was verified on Sunday 6 September, which
  is the day the audit found the defect on.

### Throwaways, and their destruction

Three suffixes across three verification passes — `mrb330-86fe84`, `mrb330b-44d626`,
`mrb330c-…` — each tagging every row it created so teardown could find all of it and
touch nothing else. No invented name could be mistaken for a real pupil, and no real
child's data was read or written at any point.

All three tore down to **zero**, verified by re-querying every table and by an orphan
sweep, independently of the script that did the deleting.

### Gates

Run green during the work: `verify_ks3` (full), `student_parity`,
`student_behaviour`, `teacher_behaviour`, `leaderboard_behaviour`, `ks3_overflow` at
both 390 and 320, the new `verify_week_truth`, and the backend's
`test_assignment_compose` (42 passing).

The push itself is gated by `prepush_gate.py`, which runs every fast gate and
requires a receipt for every slow one **against the exact tree being pushed** — so
the whole set is recorded once more on the final commit, after this report is in it.
Nothing shipped on a receipt for an earlier tree; the run was restarted each time a
byte changed, which is the point of keying a receipt on the tree.

### The three gates that ship red, and why

No gate was weakened. Three carry a `GATE-OVERRIDE`, named in the commit message,
and none of the three is red because of anything in this ticket:

| gate | why it is red |
|---|---|
| `3d_parity` | Pre-existing and long-standing — the same three failures (`--st-ok-room`, and two 1.5px-vs-1px borders) that MRB-323 through MRB-328 each overrode. MRB-330 changed **zero** files under `3d-studio/` or `mrbadmus_site/3d/`. |
| `pool_ownership` | It hardcodes the SIBLING backend checkout, which is currently sitting on **another session's** `feat/mrb332-ks4-pool` branch, where `bankFor()` was rewritten. It is reading a branch nobody has shipped, not the code being pushed. My worktree on `main` still has the `bankFor` it expects. |
| `teacher_admin_foreign_class` | `admin_view_drive.py` defines `NOW = "2026-08-30T00:00:00+00:00"` — a hardcoded instant that was genuinely *now* when it was written and stopped being now on 31 August. It is that fixture's live paper's `due_at`, and the Remind control only draws when children owe **this week's** paper, so the fixture quietly stopped making the button the gate then reports as missing. |

The third deserves the proof rather than the assertion, because it is the one that
could plausibly have been mine. It is not: on any **non-Sunday** the MRB-330 week
code is behaviourally identical to what it replaced — `getDay() === 0` is false, so
both changed branches are no-ops — and today is a Monday. Computed both ways, the
window is `Mon 7 Sep → Mon 14 Sep` under the old code and the new one, byte for
byte, and the fixture's paper (due **Sun 30 Aug**) is outside both.

I attempted the repair — making `NOW` track the clock, which is restoring the
fixture's original property rather than weakening an assertion — and it perturbed a
second, unrelated check on the same drive. So it is reverted and written up instead:
it wants its own run, with that drive's fixture semantics properly understood, rather
than a tuned guess at the end of a long night.

⚠️ **`verify_week_truth` is registered with `needs_env=MRB_BACKEND`, deliberately**,
and `pool_ownership` is the argument for it. A gate that silently compares against
whatever branch somebody left checked out in a sibling repo proves nothing about what
a child is actually served. The new gate refuses to guess and must be told which
backend is authoritative; it was run, and passed, against the backend this run is
pushing.

`ks3_overflow` earned its keep: it caught a 320px regression I introduced while
fixing the breadcrumb, and I confirmed the regression was mine before fixing it
rather than assuming it was pre-existing.

---

## 10 · Deviations

**Deviation:** the brief named "the truncated KS3 header pill" → at 390px the pill was
the one element *not* truncated → I removed it as ruled and then found the breadcrumb
still did not fit, so I also let it wrap below 420px. Going beyond the literal
instruction was the only way to satisfy it: the ruling was to let the breadcrumb
breathe, and two shorter ellipses is not breathing.

**Deviation:** the brief asked for the alignment defects in Mide's screenshots,
naming "card edges" → those screenshots are not on this machine → I measured instead
and fixed what measurement found (the header, and the stat tiles, where the real
defect was a full progress bar on an unrecorded metric). **I could not find a card-edge
defect**: no element exceeds the viewport at 390px and no card's insets differ by more
than 1px. If there is a specific card, I need the screenshot.

**Deviation:** the brief said "re-key or compute on read — your call" for existing
assignments → **neither was needed**, and I proved it rather than choosing: every
Thursday deadline of the year is byte-identical under the new arithmetic, so nothing
stored is reinterpreted. The proof is a test, not an assertion.

**Deviation:** I found the empty subject chip and did **not** fix it, though the fix is
one word. `build_student_port.py` states an invariant that the fix would falsify, and
I measured that the two bindings really do share a parent. Recorded in §8 rather than
shipped unverified at the end of a long run.

**Deviation:** the shoutout **Remove** control does not soft-delete — four attempts,
no confirm dialog, no console error, zero rows changed. Found while verifying
Messages, outside this run's scope, unfixed. It is adjacent to the safeguarding story
and worth a look: **a teacher who thinks they have removed a shoutout has not.**

**Deviation:** the backend change was made in a git worktree on `main` rather than in
the main backend checkout, because another session was actively working that checkout
on a feature branch. Nothing of theirs was touched.
