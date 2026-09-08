# MRB-336 + MRB-337 — PLAN

Daytime run, 8 Sep 2026. Site worktree `feat/set-work-v21` off `44dadd96c`;
backend worktree `feat/set-work-v21` off `6f4b3fa`.

## The seven things Mide asked for

| # | His words | Where it lands |
|---|---|---|
| 1 | papers on triple too, "a simple fix" | `papersFor` — one line, plus three gates |
| 2 | delete and edit assignments | `DELETE`/`PATCH /api/teacher/set-work/:id` + row controls |
| 3 | a bell with unread messages, banner stays | `GET /api/student/notifications` + bell on every student surface |
| 4 | released work did not reach the pupil | remove the POST clamp; move his three rows by hand |
| 5 | the hold should not govern teacher work | same; hold keeps governing auto composition only |
| 6 | live assignments take over the reteach card | slots A/B in the week view |
| 7 | look through the student pages and fix everything | the sweep lane |

## Order

1. **Recon → RISKS.md + PLAN.md** ← this commit
2. **Backend** — papers; clamp removal; `deleted_by` migration on TEST; DELETE;
   PATCH; notifications route; `test_set_work_v2.js` blocks
3. **Site** — sheet (hold line out, Edit mode, Delete controls); class page
   slots A/B; status + Set column; consumers; bell on every student surface
4. **Sweep** — student surfaces at 390/1280, before and after
5. **Drives** — `set_work_drive`, `student_bell_drive`, `assignments_hold_drive`,
   `set_work_scope_check`, `ks4_pool_drive`
6. **Reviews** — backend diff, UI diff, cold RISKS audit by a fresh reader
7. **Receipts** — `prepush_gate.py --record-all` once, on the final tree
8. **Merge** — backend first (health, 401s), prod migration, release the three
   rows, then site, live stamp proof, prod re-reads
9. **REPORT.md + mide-live-check.md**

## Rulings taken in this plan

- **The hold is a composition dial, not a visibility dial.** It keeps its whole
  meaning for automatic work and loses it entirely for work a teacher set by
  hand. Mide's sentence — "the point of setting work is so that students can do
  assignments even though the automatic assignments hasn't gone live yet" — is
  the definition, not an exception to it. 14 September stays.
- **A card is live work, not a week's work.** Slot A and slot B each show ONE
  assignment with ITS OWN count, ITS OWN chase list and ITS OWN reminder. The
  aggregate "+2 more · 0 of 6 in" goes. When the only live work is the automatic
  weekly set, slot A is exactly today's card and nothing has changed.
- **Status is release_at and due_at, and nothing else.** `Scheduled` before
  release, `Open` between, `Closed` after. The SET column is the release
  instant, in London. This is what made his screenshot say OPEN about work no
  pupil could see.
- **Edit narrows at release.** Before release everything is editable, because
  nobody has seen it. After release, `title` and `due_at` only — a pupil who has
  started must not have the questions changed underneath them.
- **Delete is soft and keeps the marks.** The row leaves every surface; the
  submissions and the points stay.
- **The bell unifies three tables and the banner keeps its job.** Reminders,
  feedback and shoutouts reach one panel; the top banner is untouched and still
  marks read, and the badge moves when it does.

## Not in this run, and why

- The student's `academic_week` filing (RISKS C1) — a real inconsistency between
  the teacher's due-date week window and the student's academic-week list. Both
  are correct for today's data. Changing the filing rule would move live work.
  Recorded for Mide.
- KS3 lesson pages — single-owner generator files, out of the sweep by §2.6.
