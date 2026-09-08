# MRB-336 + MRB-337 — RISKS

Seeded from the prompt's §12, extended by recon on 8 Sep 2026. Each risk gets a
letter, a statement, and how it is closed. A risk with no closer is a finding.

## A. Corrections to the prompt's own assumptions (found in recon, before any code)

**A1. `assignments.deleted_at` ALREADY EXISTS, and every consumer already filters it.**
The prompt's §5 asks for a migration adding `deleted_at`. It is already there
(TEST `information_schema` read, 8 Sep), it is `timestamptz null`, and the whole
estate already carries `.is('deleted_at', null)` — 30+ call sites in `server.js`,
5 in the site's data layer, plus the RLS policies `assignments_student_read` and
`aq_student_read`. Two consumers were found NOT filtering it and are fixed in
this run (see D1).
→ The migration reduces to `deleted_by uuid` + the partial index. Adding
`deleted_at` again would be a no-op at best and a column-type fight at worst.
⚠️ This is the good kind of surprise, but it inverts the §5 risk: the danger is
no longer "a consumer forgets to exclude deleted rows", it is "a consumer that
already excludes them is assumed to need editing and gets edited wrongly".

**A2. Releasing Mide's three rows needs `academic_week` moved too, not just
`release_at`.** The prompt's §3.2 production step says set `release_at = now()`.
That alone leaves all three rows STILL invisible to every pupil.
Read from production, 8 Sep: all three carry `academic_week = 3`. Today is
teaching week **2** (`currentTeachingWeek` run against the real year row,
start 2026-09-01, week zero 2026-08-30). The student's week list
(`weekWorkFor`, server.js:1446) filters `.eq('academic_week', week)` with
`week` = the CURRENT teaching week. A week-3 row is not in week 2's list at any
`release_at`.
The rows were filed under week 3 because the POST derives the academic week
from the RELEASE instant, and the clamp had already moved that instant to
13 Sep 23:00Z — which is week 3. The clamp did not just delay the work, it
re-filed it.
→ The production step sets `release_at = now()` AND `academic_week = 2`, which
is exactly what the POST's own rule would have produced with no clamp. `due_at`
is NOT moved: the teacher chose 15/16 Sep and a due date in a later week is
legitimate. Read before, read after, three rows only.

**A3. Feedback and shoutouts do NOT live in `student_notifications`.** That table
is reminders only — `kind text not null default 'reminder' check (kind in
('reminder'))`. `submission_feedback` and `class_shoutouts` are separate tables
with their own RLS.
→ §7's second branch applies: the bell is served by a backend route that unifies
the three, not by a direct client read of one table. A client-side three-table
join under RLS would also be three round trips on a phone.

## B. The hold (§3.2)

- **B1. Removing the clamp cannot retract work already seen.** The clamp resolves
  at SET time and stores an instant; nothing re-applies it at read time. So
  removing it changes only rows written after the deploy. The three existing rows
  are moved by hand (A2), deliberately and by id.
- **B2. The student side needs no change at all.** Traced end to end: the only
  student-side hold read is server.js:1728, inside the auto-compose path, AFTER
  the "already composed?" branch. It governs CREATION only. Teacher rows are
  served by `weekWorkFor` and gated on `release_at`, never on the hold.
  → The drive must PROVE this rather than assume it: held school + teacher row
  released now → pupil sees it; auto row → still held.
- **B3. The held card must not sit beside live teacher work.** Already true by
  construction (`benchHeldLine` requires `held && !benchWork`), but it is now
  load-bearing rather than incidental, so the drive asserts it.
- **B4. `resolveReleaseAt`'s hold argument becomes dead at its only call site.**
  A clamp that no production caller reaches is the "gate that stopped watching"
  shape. → The call site passes `null` with a ⊕ MRB-336 note, and the function
  keeps its unit tests as arithmetic tests; the auto path never used it.
- **B5. `Later` may now be in the past where the clamp used to rescue it.**
  Validation is unchanged (≥ now − 5 min), so a teacher choosing a past time gets
  a 400 rather than a silent shove forward. That is the intended reading: the
  clamp was hiding a validation result.

## C. Cards and status (§4)

- **C1. Two different week filters already disagree.** The teacher's week view
  selects by `due_at` inside the week window; the student's list selects by
  `academic_week`. Mide's three rows are week 3 with due dates in week 3, so they
  agree today — but a set released in week 2 and due in week 3 lands in the
  student's week 2 and the teacher's week 3. → §4.1 defines a card by
  `release_at ≤ now < due_at`, which removes the teacher side's dependence on the
  week window. Recorded, not silently reconciled: the student's academic_week
  filing is untouched by this run.
- **C2. Status computed in device time.** `assignmentDueGroup` compares ISO
  strings against `nowIso`; the SET/DUE columns must render in London. → One
  formatter, London-pinned, no `toLocaleString` with a timeZone on the server
  (it crashes Render — MRB-335).
- **C3. Slot B flapping.** At the instant a second set releases, slot B changes
  from Reteach to that set. Acceptable and intended; the drive pins it at both
  sides of the boundary so it is a ruling, not a surprise.
- **C4. Remind on card A must remind about set A.** The per-card reminder carries
  that card's assignment id. The current aggregate card has one reminder for the
  whole week. → Drive asserts the id written into `student_notifications`.
- **C5. Scheduled rows count as set but are not cards.** "N assignments · N this
  term" counts them; the three card slots do not show them.

## D. Delete and edit (§5, §6)

- **D1. Two consumers do not filter deleted rows.** Found in recon; fixed and
  listed in the report with file:line.
- **D2. Delete after submissions.** Submissions and points are kept; the row
  leaves every teacher and student surface. A deleted set's marks are not
  retracted from a leaderboard total.
- **D3. Edit replacing questions after a pupil started.** Refused: after release
  only `title` and `due_at` change. Before release nobody can have started,
  because nobody can see it.
- **D4. Double-tap delete / crafted id.** Idempotent (already deleted → 200, same
  shape); auto rows 409; another class's id refused by `setWorkAccess`.
- **D5. Notifications for deleted work.** Unread rows for the assignment are
  marked read at delete; the bell and the banner never advertise deleted work.
- **D6. Multi-class sets are N rows and Edit/Delete act on ONE.** No cascade.
  Stated on the sheet? No — stated in the report; the sheet says nothing, because
  a teacher looking at one class's row is acting on one class's row.

## E. Bell (§7)

- **E1. RLS leak across pupils.** The route reads as the caller, never
  service-role, and the drive proves pupil A cannot read pupil B's rows.
- **E2. Badge counting read rows.** Badge = unread only; the banner's existing
  mark-read path must move the badge.
- **E3. 390px.** The bell must not break the 46rem column; KS4's dark header has
  its own spacing. Both measured.
- **E4. No polling loop.** Load + `visibilitychange` only.

## F. Process

- **F1. Two sessions today.** The content session (MRB-338) is in its own
  worktree. Pathspec commits only; different ports; receipts recorded once on the
  final tree, last.
- **F2. Receipts bind to the tree.** Slow gates run once, at the end, after the
  last byte.
- **F3. Disk.** 2.8 GB at start. Checked before each gate wave; ≥ 700 MB.
- **F4. Never `pkill -f`.** It kills the other lane's browser.
