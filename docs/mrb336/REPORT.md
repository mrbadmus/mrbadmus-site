# MRB-336 + MRB-337 — REPORT (draft, evidence filled as lanes land)

## 1. Your seven asks → what changed → evidence

### (a) "I did not mean for only combined classes to only have the paper 1 and
### paper 2 cards, that should apply to both triple and combined … a simple fix"
It was a simple fix. `papersFor()` in `set-work-scope.js` returned `null` for
triple; it now returns `[1, 2]` for every KS4 class. The tree already stamped a
paper on every topic regardless of pathway, so nothing else had to move.
⚠️ One consequence worth knowing: `space` is triple-only and sits on Paper 2, so
a triple physics class now sees it WITH a Paper 2 chip. A combined class never
sees `space` at all — all five of its subtopics are triple-only, so the topic is
absent from the tree rather than filtered out of it.
Evidence: `test_set_work_v2.js` asserts it in both directions; `set_work_drive`
and `ks4_pool_drive` had assertions saying "triple has no papers" and those were
INVERTED, not deleted, in the house superseding style.

### (b) "It doesn't seem like I can delete works, teachers should be able to
### delete assignments and also be able to edit them"
Both, as two new routes with the access check the rest of Set work already uses.
- **Delete** is soft: the row leaves every teacher and student surface, and the
  submissions and marks stay. Pressing `Delete` turns that row's controls into
  `Delete · Cancel` in place — no dialog, no sentence — and the second press
  performs it. Automatic weekly work shows no Edit or Delete at all and the
  server refuses it (409) even if asked directly.
- **Edit** narrows at release, and the server decides, not the page. Before
  release everything is editable, because nobody has seen it. After release only
  the title and the due date, because a pupil who has started must not have the
  questions changed underneath them.
- A set given to twenty classes is twenty rows. Edit and Delete act on the ONE
  row you are looking at. There is no cascade.

### (c) "the student page should have a notification like bell icon … but I
### still like that the message appears at the top the way it does currently,
### and when they have a new unread message, this should reflect on the bell"
All three parts. The banner is untouched and still marks read when the work is
opened; the bell badge moves when it does, because both read one count.
The bell unifies FOUR kinds — `Reminder`, `Feedback`, `Shoutout`, `New work` —
which needed a new backend route, because only reminders lived in
`student_notifications`; feedback and shoutouts are separate tables.
`New work` is derived at read time from released teacher assignments rather than
written at release. Nothing runs at the instant a teacher's chosen release time
passes, so a written row would have needed a poll, and a missed tick is a
notification that never arrives for work that really was set.

### (d) "I released work for 8r1 which i set to 'release now' … but none of the
### assgt show on my student page"
Two causes, and only one of them was the one we knew about.
1. The POST was CLAMPING your release instant up to the school's go-live hold.
   All three of your sets carry `release_at = 2026-09-13 23:00:00+00` — London
   midnight on the 14th — instead of the instant you chose. That clamp is gone.
2. ⚠️ The clamp did not just DELAY your work, it RE-FILED it. The academic week
   is derived from the release instant, so all three landed in **week 3**. Today
   is teaching week **2**, and the pupil's week list filters on academic week.
   So releasing them alone would have left them invisible and this morning would
   have repeated exactly.
Both are repaired on your three rows: released, and moved to week 2. Their due
dates are untouched — you chose the 15th and 16th and a due date in a later week
is legitimate.

### (e) "it shouldn't matter when assignments go live … let's still leave 14
### september there, the point of setting work is so that students can do
### assignments even though the automatic assignments hasn't gone live yet"
Taken as the definition of what the hold is FOR, not as an exception to it.
The hold is now a COMPOSITION dial: it still governs automatic weekly work
exactly as before, and 14 September still stands. It no longer has any say over
work a teacher sets by hand.
The held-state card ("This week's work isn't live yet") only appears when there
is nothing releasable at all, so it can never sit beside live work again.

### (f) "live assignments should take over the reteach from last lesson card …
### they can see both on those cards instead of only below"
Three slots. A card is now LIVE WORK — released, not yet due, not deleted — and
each one carries its own count, its own chase chips and its own `Remind all N`
that reminds about THAT set. Two live sets fill slots A and B; the Reteach card
holds slot B only when there is no second live set; three or more adds `+N more`
to the table. The aggregated "+2 more · 0 of 6 in" is gone.
⚠️ When the only live work is the automatic weekly set — the ordinary week for
most classes — slot A is exactly the card you have now, unchanged.

### (g) status and the Set column were lying
Your screenshot showed three assignments as OPEN, "Set Tue 8 Sep", that no pupil
could see. Status was computed from the due date alone and never looked at the
release instant. It now reads `Scheduled` until release, `Open` between release
and due, `Closed` after; the Set column shows the release instant in London.

## 2. Deviations
## 3. Found and fixed along the way
## 4. Open on you
## 5. Gates, migrations, production

## 2. Found on the way, and fixed — things you did not ask for

**Edit had never once saved anything.** Two independent faults pointed the same
way: the sheet sent no `client_ref`, so the server refused every Save with a 400
that outlined no field; and the success test read `body.success`, which the new
route did not send. Fixing either alone still leaves Save reporting failure,
which is probably why it survived. Found by a drive, not by reading.

**"+N more" was dead on every class.** The anchor was bound to an `<if>` — control
flow, not an element — so it never reached the page. It greps as present in the
built HTML, and the helper's tolerance for a missing section turned it into a
silent no-op. That link is the only route to the third and later live sets.

**Four "Lessons in this topic" cards scroll to the top instead of opening**, on
every KS4 class page, live today. An August fix left one branch: the code
returned early on a card with no page BEFORE calling `preventDefault`, so
Design's `href="#top"` took over.

**A teacher could back-date a deadline and mark a whole class late.** `PATCH`
capped a due date in the future but never in the past, so on already-released
work a mistyped month made every unsubmitted pupil overdue at once. The
asymmetry gave it away: `release_at` has a deliberate five-minute past grace
with the reasoning written out, and `due_at` — which is what actually decides
lateness — had nothing. Before this run a deadline could not be moved at all,
so we created that surface and closed it the same day.

**The nav showed a pupil's email to anyone looking at their screen.** The chip
fell back to the whole email local part (`👤 aiden.cole`) when no first name was
set. Now it reads the real first name it was already fetching.

**Two student-read RLS policies did not exclude deleted work.** With a delete
route live, a soft-deleted assignment would have stayed readable through a
direct database read. The site's own client filtered it, so the hole would have
been silent. Both narrowed; two guards now, neither sufficient alone.

**The banner could advertise deleted or unreleased work.** The function feeding
it is `SECURITY DEFINER`, so RLS never applied, and it never joined assignments
at all. It now excludes deleted, unreleased, and — a third hole found while
fixing it — reminders pointing at another class's work entirely.

**Work set in advance would never have rung the bell.** The new-work source
windowed on when you TYPED the work rather than when it RELEASED, so a term set
in August would ring for none of it in October.

## 3. Deviations — where I did something other than what was asked

- **The prompt said add a `deleted_at` column. It already existed**, estate-wide,
  with every consumer already filtering it. The migration shrank to `deleted_by`
  plus the two RLS narrowings above.
- **The prompt's production repair was insufficient.** It said set `release_at`.
  Your three rows were also filed under the WRONG WEEK, because the clamp moved
  the release instant and the academic week is derived from it. Releasing alone
  would have left them invisible and this morning would have repeated exactly.
- **The prompt said fix status in `assignmentDueGroup` "so every consumer
  inherits it". That function has no live consumers** — its only reader is a
  retired page. The seam that actually feeds the four surfaces is `buildPapers`.
  Both were fixed.
- **`release_at` was in no database select at all**, so nothing downstream could
  have read it. That was the invisible half of the bug you reported.
- **Question positions renumber from 1, not 0** as I specified — the whole estate
  is 1-based with a uniqueness constraint to match.
- **`ks3_browser.screenshot()` resets the viewport to 1280×900**, so a drive that
  measures after a screenshot silently reads desktop numbers. Found mid-run. I
  did NOT fix it: it would shift snapshot geometry under a parity gate on merge
  day. Recorded at `ks3_browser.py:572-577` as its own unit.

## 4. Open on you

1. **Any teacher on a class can delete a colleague's set work**, as can school
   admins. Audited every time with who did it and how many pupils had submitted.
   I did not restrict it to the author, because on a co-taught class that blocks
   the cover teacher. Your call.
2. **A pupil mid-attempt when work is deleted** gets a generic failure, not a
   "your teacher withdrew this" state. Saved answers are kept. Building that
   state is design, not a bug fix.
3. **The nav bar has almost no slack between 401 and 560px.** A long name now
   truncates to `👤` there rather than overflowing — strictly better — but it is
   tight because Leaderboard and Search only collapse at 400px and below. Moving
   that threshold is a product decision.
4. **`/favicon.ico` 404s on every page.** The site has no favicon and no
   `<link rel="icon">`; CLAUDE.md pins four brand presentations and none names
   one. A brand decision.
5. **The teacher chip renders its own label as its value** on a class with other
   than exactly one teacher, because the underlying read returns names without
   ids. Ambiguous, and yours.
6. **The parent digest and termly report still count minutes a child spent on
   work since deleted.** Ruled deliberately: the minutes are a fact about what
   the child did, and retracting them because a teacher tidied a duplicate is the
   worse error. Say if you disagree — it is one join in each.
7. **The scheme of work is untouched** and still governs automatic weekly work.
   14 September still stands.

## 5. Gates

**42 green.** 24 slow gates hold receipts bound to tree `ebcb1a427c9c`; every
fast gate ran at push time. `set_work` — the gate for this ticket — passed
**304 checks, 0 failed**.

⚠️ `set_work` had never been receipted before today, and not because anyone
skipped it: the registry runs the drive with no `--shots` flag, so recording it
writes PNGs into the repo and dirties the tree, and a dirty tree refuses
receipts. It had been skipping on a missing credential that turned out not to be
one — the fixture creates its own accounts and re-asserts whatever password it
is handed. Its screenshots are now committed, so the receipt is real.

**1 red, carried under an explicit override**, written into the commit message
so `git log` still says it in a year: `teacher_admin_foreign_class`, 3 checks in
C7 REMINDERS. Proven pre-existing by REPRODUCTION, not assertion — the merge
base's `teacher/`, `mrbadmus_site/teacher/` and `teacher_fixtures/` were checked
out into the worktree, the gate re-run, the identical three failures produced,
and the files restored.

**5 skipped, each named with its reason.** Two of them —
`student_controls_drive` and `export_ks3_questions_verify` — default to YOUR
production account, and this run was not permitted to use it. That gate is the
one that catches dead controls, so its questions were asked by hand instead and
written up in `sweep-after.md`; the bell was pressed on all seven surfaces, 48
presses, 48 opens. The three `3d_*` gates cannot run because `3d-studio/dist` is
gitignored and was never built here; nothing in this run touched `3d-studio/`.

⚠️ One flaky check found and NOT tuned: `set_work_drive.py:5279` reads
`!primary.disabled` after a fixed 0.3s sleep, and fails about one run in four
while the very next check proves the button was pressable. Recorded rather than
quietly adjusted.

## 6. Production, in order (all times UK, 8 Sep 2026)

1. **Backend** merged and pushed (`6f4b3fa..7490ca9`). Proved BEHAVIOURALLY, not
   by status code: the three new routes answered **404 before** the deploy and
   **401 after**, 45 seconds later. `/api/health` cannot say which build Render
   is serving, and a 404 read as "not built" misled a lane earlier today.
2. **Four migrations**, one at a time, each verified before the next.
   - `20260908065322` — `deleted_by`, `student_message_reads` + RLS, and both
     student-read policies narrowed. Re-read after: the ONLY difference from the
     production text is the added `deleted_at IS NULL`.
   - `20260908065607` — `replace_assignment_questions`. ACL after: postgres +
     service_role only.
   - `20260908072557` — `search_path`. ACL re-checked and STILL clean.
   - `20260908112533` — `student_reminders_for_viewer`. ACL after byte-identical
     to before, `anon` never granted, and all three new guards live.
   ⚠️ `CREATE OR REPLACE` RESETS A FUNCTION'S PRIVILEGES. On the last one, which
   is SECURITY DEFINER, leaving them at the default would have made it callable
   by `anon`. Both migrations restate their grants and both were verified after
   applying rather than trusted.
3. **Your three rows repaired** — released at 18:42, moved to academic_week 2,
   `due_at` untouched. Exactly 3 rows, guarded by id + `source='teacher'` +
   not-deleted. Read before, read after.
4. **Site** merged and pushed (`44dadd96c..5195bb5d1`).
5. **Live proof.** The page map first, then the assets with a cache-busting
   nonce, compared with `cmp` and not `grep`: `student-bell.js` (33,993 bytes),
   `nav.js` (15,676), `nav.css` (16,039) — all byte-identical to the committed
   build. ⚠️ Never fetch a stamped URL BEFORE its deploy lands: `_headers` marks
   assets immutable and a pre-deploy fetch pins the stale bytes for a year.
6. **Production re-reads.** 0 soft-deleted assignments · your 3 rows released and
   in week 2 · Rainford's `assignments_open_from` still **2026-09-14**, exactly
   as you asked.

⚠️ **These two documents were committed AFTER the receipts.** Receipts bind to
the git tree, so any tracked byte — documentation included — invalidates them.
The receipts attest the CODE tree that shipped; this file lands on top, the same
order last night's run used. Nothing about the shipped code changed.
