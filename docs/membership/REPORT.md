# Class membership — report (27 Nov 2026)

## What a school admin can now do

On a class page, a **Pupils** button (admins only):

- **Add a pupil**: type a name or admission number, tap **Add**.
- **Not on MrBadmus yet?** Add them by school email and name. They are
  created the same way the CSV import creates them, and their Microsoft
  sign-in links to that account the first time they sign in.
- **Move** a pupil: pick the class (same year group listed first), confirm.
  One action.
- **Remove** a pupil: one tap, a plain confirm, then **Undo** for 20 seconds.
- **Several at once**: tick pupils (or Select all), then Move or Remove.
- **Left this class**: who left or moved, when, and where to, with the work
  they did in this class.

On a pupil's page, a **Classes** button: their current classes, with Move
and Remove for an admin.

**Add pupils (CSV)** gains **Make the class match this file**. The preview
lists, by name, who will be added, who will move in from another class
(same year group and same science), and who will be removed. Nothing happens
until the admin presses **Make it match**. If any row in the file can't be
read as a pupil, nobody is removed.

Teachers see the result but can't change membership. A teacher of a class
with pupils who have left gets a read-only **Left this class** button.

## The rules, and where they live

All writes go through database functions in
`supabase/migrations/20261127120000_class_membership_rpcs.sql`:
`add_pupil_to_class`, `remove_pupil_from_class`, `move_pupil`,
`class_membership_batch`, `undo_membership_change`. Each one:

- checks the caller is a school admin of the class's school;
- checks every class is in that school's current academic year;
- does the whole change in one transaction;
- writes one `audit_log` row per pupil per change.

Other rules:

- **History is never lost.** Leaving sets `left_at` and `deleted_at`; no row
  is ever deleted. Submissions, scores and flashcards stay with the work.
- **No duplicates.** Re-joining a class reopens that pupil's existing row.
  Undo puts an old stint's dates back exactly.
- **No "missing" for work set before a pupil joined.** This applies to the
  roster flag, Today's chase list, the pupil page, and the database roll-up
  (`20261127120100_rollup_missing_respects_joined_at.sql`).
- **Leaving drops a pupil out of the current class view.** They leave the
  current and future weeks, missing lists, reminders and the class
  leaderboard, because all of those already read only current members.

Head of department scope is **not** admitted. `staff_scopes.department`
can't be mapped onto KS3 or combined-science classes, which carry no subject,
so it wasn't clean. **Admins only.**

## Proof

| check | result |
|---|---|
| `tools/membership_rpc_check.sql` on TEST (anon, pupil, teacher refused; move, move back, undo, batch all-or-nothing, audit, no duplicates) | ALL PASS |
| `tools/class_membership_drive.js` on TEST (admin, both teachers, moved pupil; 390 px + 1280 px; light + dark) | ALL PASS |
| Independent reviewer walk (admin, teacher of each class, moved pupil, anon, break attempts) | Every permission scenario passed. It found 3 defects and 2 risks, all fixed and re-verified (below) |

Reviewer findings fixed:

1. The built copy of the panel script was stale. Rebuilt.
2. Undoing a move back overwrote the earlier stint's dates. Undo now restores
   them exactly. Regression check added.
3. The pupil page showed "MISSING" for work set before joining. It now reads
   "Before joining", via `teacher_rulings.py`.
4. "Add by email" with another school's pupil is now refused.
5. In "match" mode, a skipped row now holds all removals.

Found by the second walk and fixed:

6. After a move on a pupil's page, the page re-opens on a class the pupil is
   still in, and the Undo stays on screen for the rest of its window.
7. A closed sheet left an invisible layer over the page that blocked every
   click. The existing "Add pupils (CSV)" sheet had the same bug, so it's
   fixed in both.

## Gates (cloud session, on the clean tree)

- **Pass:** ks4_pilot_check, ks4_batch_check, knowledge_points_check,
  contrast_audit, teacher_tells, gate_coverage, week_scope_check,
  test_isolation, theme_wiring_check, brand_one_mark, lean_check, plus 21
  other fast gates.
- **Could not run here:** pool_ownership, set_work_unit, seating_tells,
  figures_mirror, curriculum_tree_mirror and knowledge_points_mirror need
  the backend repo. frozen_window_guard and export_ks3_questions_verify need
  production credentials. 3d_isolation needs the 3D Studio build. The slow
  drives need `MRB_THROWAWAY_PASSWORD` and the local backend. The pre-push
  hook runs all of these on Mide's Mac.

## Deviations

- The CSV import's name-based path (`teacher/import.html`, which creates
  classes) still writes `class_members` directly. It is open to teachers
  today; routing it through admin-only functions would have taken that
  away. → Left as it is. Only the by-class path (the class page) now goes
  through the functions.
- Teachers can still write `class_members` directly under the existing row
  rules. → Not changed: the brief said RLS stays exactly as strict as it is,
  and tightening it might break joining by class code. Flagged here for a
  later decision.
- Several gates can't run in a cloud session. → Listed above.
- One of my commits (9fbbff29) swept in 825 KS4 lesson pages that a gate
  was rewriting at that moment. → Restored to the starting commit two commits
  later; the branch's KS4 pages are byte-identical to `b0b005d0`. Nothing
  reached `main` or production.
- The edge function deployed to TEST is a bundled copy of the committed
  `index.ts` (same code, comments stripped). → Production should deploy the
  committed file itself.
