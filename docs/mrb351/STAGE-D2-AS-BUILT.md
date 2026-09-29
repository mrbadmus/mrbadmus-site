# Stage D2 as built — "Your flashcards" (the library)

Builder: Opus 5.5, 29 Sep 2026. Spec: `docs/mrb351/STAGE-D-PLAN.md` §3 (on `feat/sharpen-d1`).
Branch `feat/sharpen-d2`, based on `5aa846c24`. Every ⚑ decision in §1 took the plan's default.

## What a pupil gets

- On the class page, directly under the FLASHCARDS card, ONE button **View your flashcards** — only when at
  least one flashcard homework has had every card rated at least once (decision 10). No qualifying set, no
  button (that is the empty state: nothing to open, nothing shown).
- Tap → **Your flashcards**: the sets, newest first. Each row is the set's name and `N CARDS`; the class name
  is added only when the sets span more than one class.
- Tap a set → one card at a time. Tap the card (or Space/Enter) to flip: the model answer, and under it
  **YOUR ANSWER** when the pupil wrote one (make mode's first answer wins; otherwise their latest review
  answer). `‹` / `›` and the arrow keys move and wrap; `3 / 10` is the only position marker; **Shuffle**
  toggles a new order and back.
- Tap the name in the header to rename it in place (Enter or leaving the box saves, Escape cancels). A blank
  name, or the teacher's own title, goes back to the teacher's title.
- `#sets` and `#set=<id>` are real addresses: Back steps set → list → class page; × and Escape step out of
  every entry the library pushed, so Back afterwards goes where it went before.
- Nothing in the library writes a rating, an event or a submission (decision 12). The only write is the name.

## Files

| file | what |
|---|---|
| `shared/flashcard-library.js` (new) | the overlay, appended to `<body>` outside the runtime; the one serving read of the deck |
| `shared/flashcard-library.css` (new) | Design's overlay materials: `--pg-*` column, `--b-*` card, `fcIn`-style fade, no slide |
| `shared/student-live.js` | DEPS += the library; `wireLibrary()` after the paint (R1 + R2, identity columns only) |
| `build_student_port.py` | `STAMPED_DEPS` += both files |
| `pool_ownership.py` | check 1b `check_library()` + the summary line |
| `gate_registry.py` | watches for `pool_ownership` and `flashcard_homework_drive` |
| `flashcard_homework_drive.py` | `run_library()` at 390 (mobile) and 1440; `--library` runs only it |
| `tools/flashcards_library_live.py` (new) | the TEST live proof (§3.6) |
| generated | `student/class.html`, `class-fixture.html`, `assignment*.html` (stamp map only) and their `mrbadmus_site/` copies |

Migration (branch `feat/mrb352-migrations` only):
`supabase/migrations/20261001090000_mrb352_flashcard_set_names.sql` md5 `78b7acafcce70621f9de75d8bec113ac`,
`supabase/rollbacks/20261001090000_mrb352_flashcard_set_names_rollback.sql` md5 `f3a487b980b6af21fd71183e1123b960`.
Rehearsed on TEST (`qeppkiswvclkkwbxmlok`): apply → verified (RLS on, 4 policies, 1 trigger, anon has no
select) → rollback → verified absent → apply → verified; left applied. Production untouched (read-only check:
the table is absent and `mrb351_touch_updated_at` exists, so the migration will apply at merge).

## Deviations

- Deviation: the plan puts the live proof in `--library` on D1's `tools/flashcards_stage_d_live.py`, which is
  being written in parallel in the other worktree → wrote `tools/flashcards_library_live.py`, its own
  throwaway world (teacher + pupil minted per run, as every other `flashcards_*_live.py` does) rather than the
  mrb326 pupils → no merge conflict, and no standing account's data is touched.
- Deviation: the plan's body-scroll lock copies `lockScroll` (html AND body `overflow:hidden`) → the library
  locks the ROOT only → measured in Chrome on the class page: `overflow:hidden` on html+body makes `<body>` a
  clipped scroller and `window.scrollY` reads 0, so the page behind jumps to the top. With the root alone
  scrollY holds (1440 live run: 553 → 553). **Finding for D1 / item 4:** Stage B's `lockScroll` in
  `student-live.js` does exactly html+body, so on the LIVE page opening the homework overlay or the practice
  round sends the page behind to the top while it is open. The fixture never loads `lockScroll`, which is why
  §0's fixture measurements show zero movement.
- Deviation: R2 does not reuse the class page's own card-count read → one paged identity read covering every
  set the pupil has rated in (sets can come from other classes, which the class page's read does not cover).
  R1 and R2 are both paged (1,000-row PostgREST page; a year of ratings can pass it).
- Deviation: the library stylesheet is injected by `flashcard-library.js` itself (stamped through
  `__MRB_ASSET_V__`) rather than a `<link>` in the generated template → no template or ruling change, and the
  sheet only loads on a page that loads the library.
- Deviation: `Flip the card` is the card's `aria-describedby` hint, not its `aria-label` → an aria-label on the
  card button would replace the question text for a screen reader.
- Deviation (unspecified detail): closing the library resets the set view; the next open of any set starts at
  card 1, face up, in the teacher's order. Tapping the scrim outside the column closes. Escape inside the
  rename box cancels the rename only.
- Deviation (unspecified detail): renaming to exactly the teacher's title is stored as "no personal name"
  (the row is deleted), so a later retitle by the teacher still shows.
- Deviation: degrade mode was proved on the fixture (stub answering `42P01`) AND on the real class page against
  TEST, by wrapping `fetch` in the page so every `flashcard_set_names` request answers exactly as PostgREST
  does for a missing table (404 `PGRST205`) → no DDL from a tool; the real client code path.
- Deviation: the migration was rehearsed with the connector's `execute_sql` and the file's exact text, not
  `apply_migration` → `apply_migration` records its own `schema_migrations` version (memory: migration version
  drift); nothing was recorded in TEST's `schema_migrations`.
- Deviation: `PUPIL-FLOW.md` §14 (D2 half) not written → D1 is writing §14 in parallel; this file is the D2
  as-built, to fold in at merge.
- Deviation: `pool_ownership` check 1b sweeps every `shared/*.js` and root `*.html` (not a named list) plus
  the backend's `server.js`; its `watches` gained `shared/*.js` to match. Proved to bite: a temporary
  `select('id, question')` in `teacher-data.js` turned it red, then reverted.
- Deviation: pushing `feat/mrb352-migrations` needed `MRB_BACKEND_DIR` (the `figures_mirror` gate) and an SSH
  keepalive (the first attempt died with 141 after the gates passed) — both known traps; the push went through.

## Not run

- `student_controls_drive.py` (wired run) was not run; the button is a plain `<button>` that opens the overlay.
