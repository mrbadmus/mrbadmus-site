# The design port — 30 Sep 2026

Mide walked the pupil and teacher pages after the sharpen run: "really really
solid run, I love it". Design then redrew the screens he had called "old and
ugly". This run put her drawings onto the pages the sharpen run built, and was
not allowed to change anything the pages do. Leads, reviews and audits by
Opus 5.5; builds by Sonnet.

Design's pages: `~/Desktop/MrBadmus AI/Flashcards/` (not committed; worked from a
scratch copy). Proof folder: `~/tmp/mrb-shots/design-port/` (`MRB_SHOTS`).

| Branch | Commit | What |
|---|---|---|
| `feat/design-port-a` | `4f27e3d9e`, `49c9d73e2` | screens 01, 02, 03 |
| `feat/design-port-b` | `70a8d3277` | screen 04, item 7, item 8 (display) |
| `feat/design-port-c` | `3cc7b2bbb`, `5898cff57`, `cdd9ef81b` | screens 05, 06 |
| `feat/design-port` | `8bb81dc03` (merge), `f51abd0e6` (audit fixes) | what ships |
| backend `fix/max-score-denominator` | `f7adb90` | item 8 at its source — **pushed as a branch, NOT deployed** (see Parked) |

## The screens

| # | Design's page | Live | Files |
|---|---|---|---|
| 01 | pupil breakdown panel (question set) | teacher class page / pupil page → Breakdown | `shared/breakdown.js`, `shared/breakdown.css` |
| 02 | per-pupil flashcard sheet | Breakdown on a flashcard row | `shared/flashcard-breakdown.js`, `shared/breakdown.css` |
| 03 | flashcard progress page | `teacher/flashcards.html` | `shared/flashcard-progress.js/.css`, `teacher/flashcards.html` |
| 04 | Students, Assignments, Submission history | `teacher/class-detail.html`, `teacher/student-detail.html` (generated) | `teacher_rulings.py`, `build_teacher_port.py`, `shared/teacher-live.js` |
| 05 | "I don't know" learn step | pupil flashcard homework | `student_rulings.py`, `shared/flashcard-keyboard.js` |
| 06 | end of a pass, Done and Try again | pupil flashcard homework | `student_rulings.py`, `shared/flashcard-keyboard.js` |

**01.** One panel shell for 01 and 02: sticky header (Close · title with the
pupil under it · ‹ › with the neighbours' names; on a phone Close and ‹ › share
the top row). Stats without boxes between two hairlines. The numbered strip is
the key for the list: right = filled square, wrong = outlined square with an
accent ring, not answered = dashed. Rows split by hairlines; "Answered" /
"Correct", and "Correct" only when the answer was wrong or blank. Cut, as ruled:
the class-wide "struggled with Qn" line, the "Open Set work for …" button, the
✓/✗ disc, the topic headers and tallies (also the per-question class flag, same
family). The Reteach banner on the assignment page is untouched.

**02.** Secured is a filled chip, Got it a tinted one (they used to look the
same), Not seen dashed. Latest answer and Model answer side by side at ≥820px,
stacked on a phone. "Tries: N" and a closed History. Cut, as ruled: the All /
Not secured toggle, the "4 right · 3 nearly…" line and the status chip by the
title. They are hidden with CSS (`display:none`, so not read out), not deleted,
because drives read their text; the hidden toggle defaults to All and is never
saved, so the list cannot be stuck filtered.

**03.** Per card and Rushed columns cut; RUSHED rides in the Time cell (and in the
CSV as `2:05 (rushed)`). The Secured column is the count plus a strip with one
cell per card in the five card states, best to worst, with one legend above the
table. On a phone: Pupil (status chip under the name) and Secured, nothing
ellipsised, no sideways scroll. The strip reads each pupil's cards with the
existing `flashcard_pupil_detail` read and the SAME `cardState()` the sheet
uses: once on load (4 at a time, pupils with no sitting skipped), then only for
pupils whose row changed on the 10-second poll (measured: 20 reads for 30 pupils
on load, 0 on an idle poll, 1 when one pupil moves). Until a pupil's cards
arrive the row draws the old count-based strip, never a blank.

**04.** One six-track grid for all three tables, cells on the text baseline. Set
column cut (hidden, not removed — `set_work`'s London-time check reads it).
Edit / Download / Delete on a quiet line under the title, next to "Quiz · N
questions" / "Flashcards · N cards", at every width. Students › Score one line
per assignment this week. "Revised after marking" under the score. Phone:
Students = Student, dot, Score; Assignments = Title, Submitted, Mean; History =
Title, Status, Score with its links on their own line.

**05.** The empty header row is gone on a homework; Close sits in the strip
beside "N of M right". The question and the model answer share one bench card,
the answer under a rule. Keyboard up: HOMEWORK tag and topic hide, question
22px, box and Check visible at 390×508 and 360×336 (the drive measures both).

**06.** At the end the strip drops its headline (the bench panel says it). Done:
the strip shows the set title; "N of N right" at 40px; "N of M secured so far";
**"Revise flashcards one more time" kept** (Mide's wording, 28 Sep) as muted
plain text so it can't be mistaken for a button; Done full width at the bottom.
Try again: numbered chips across the strip; "Tap a green card to redo it"
shows beside × **only while a green chip can really be tapped** (see Decisions).

## Items 7 and 8

**7 — class cards.** When the open set is a flashcard deck the main count is now
pupils who have started (any sitting), with "N secured" as the smaller second
fact in the slot a question set uses for its second line. No new request: the
page already read `flashcard_sessions`; it now keeps the assignment id.

**8 — "1/2" on a 4-question set.** Cause: the backend's `rescore()` writes
`max_score` = the number of questions MARKED at that moment, so a pupil who
answers 2 of 8 and finishes is stored 1/2. Shown on TEST: pupil Dev, set Q1,
`score 1, max_score 2`. The site now uses the set's own question count
everywhere it shows a question-set score: breakdown SCORE, the marking grid,
Students › Score, Submission history, the AVG SCORE tile, the class Students
AVERAGE (the matrix is rebuilt once the counts arrive), the pupil's done-bench
and Work row and the pupil's Average (from the count the class page already
loads; pupils can read their class's `assignment_questions`). Falls back to
`max_score` only when the count is unknown. **Averages change:** Dev's 1 of 8
now counts as 13%, not 50%; Ben (7 of 8 answered, 5 right) as 63%, not 71%.
The backend fix (`max_score` = the set's markable question count) is on backend
branch `fix/max-score-denominator` (`f7adb90`), 1197 backend checks green,
proved on TEST (Ella: 2 of 8 → stored `max_score 8`). **Not deployed** — the
push to backend `main` was refused by this session's permission check as a
production deploy. Until it ships, the site's display fix covers every screen,
but two SQL functions still read the stored `max_score`: the teacher class
rollup's class mean (Today / My classes) and the class-stars 75% eligibility.
Both become correct once the backend fix ships (for new submissions; stored
rows keep their old value — a backfill would be a production write, so it is
Mide's call).

## Proof

- Side by side, Design vs live, 1440 and 390, light and dark, every screen,
  real TEST data: `audit/design-XX-*.png` vs `audit/live-XX-*.png` (183 files,
  plus `base-XX-*` = origin/main on the same data). Fix round before/after:
  `fix/`. Builders' own pairs: `01/` … `06/`.
- TEST world (`world/WORLD.md`, teardown script not run): class 8d/Sc1, 6 pupils;
  question set with right, wrong, blank, late, revised and partly answered
  pupils; flashcard set with every card state on one pupil, a rushed pupil, one
  mid-set, one not started; last week's set and a scheduled one.
- Opus hand walk on TEST at 390 and 1440 (`audit/AUDIT.md` walk table): verdict
  cap, IDK learn step and replay, Try again leftovers only, green-chip redo,
  progress saved at every card and after ×, reopening homework and "revised
  after marking", week picker, ‹ › in both panels, Breakdown, Add feedback,
  Edit, Download (armed and cancelled), Delete (armed and cancelled), the
  flashcard library, top bars, Light/Dark/System: **all work**. One break found
  (the redo hint in the first pass) — fixed in `f51abd0e6`.
- Audit round 1: SEND BACK, nine must-fixes, all fixed in `f51abd0e6`.

## Baseline vs after

Baseline = origin/main `7823495ec` on TEST; after = `f51abd0e6` (the receipt
round, `prepush_gate.py --record-all`). Zero new reds.

| Check | Baseline (main) | After (port) |
|---|---|---|
| student_parity | PASS | skipped by rule (nothing it watches changed) |
| student_behaviour | PASS | PASS (one first-run red was a page clock, 06:17 vs 06:16; green in the round) |
| student_themes | PASS | PASS |
| student_switches | PASS | PASS (first after-run; not selected in the round) |
| student_bell_drive | 2 red: bell_survives_redraw, panel_survives_redraw (known, local backend up) | the same 2, nothing else |
| student_lessons_cards_check | PASS | PASS |
| teacher_behaviour | PASS | PASS |
| teacher_reach | PASS | PASS — red on the first after-run (phone header/cell misalignment from the new grid), fixed in `f51abd0e6` |
| teacher_tells | PASS | PASS |
| teacher_picker_drive | PASS | PASS |
| today_drive | PASS | PASS |
| set_work | 3 red: the inherited TEST-bank preconditions | the same 3 (a 4th seen in two runs varied between `scope_resolves_in_place` and `ks4_stays_flat`; run alone on the final tree: exactly the 3) |
| assignments_hold_drive | PASS | PASS |
| flashcard_homework_drive | PASS | PASS (+1 check: no redo hint in the first pass) |
| flashcard_engine_test | PASS | PASS |
| flashcard_progress_drive | PASS | PASS (+1 check: five-state strip) |
| flashcard_decks_drive | PASS | PASS |
| flashcard_request_shape_drive | PASS | PASS |
| mrb328_card_prefetch | PASS | PASS |
| teacher_rollup_equal | PASS | PASS |
| theme_wiring_check | PASS | PASS |
| contrast_audit / contrast_audit_interactions | ran on main (result file unreadable to this session, see below) | PASS / PASS |
| focus_audit | ran on main (same) | PASS (first after-run: a 30 s page-load timeout on `teacher/timetable.html`, a page this run does not touch) |
| brand_one_mark | ran on main (same) | PASS |
| also green in the round | | verify_ks3, import_year_drive, ks4_chrome_drive, seating_drive, consumer_flag_off, teacher_perf_budget, teacher_admin_foreign_class, teacher_admin_real, class_csv_upload, mrb328_import_picker (a and b) |
| tools/ live scripts (7) | `flashcards_sharpen_live` re-run on main: red, "We could not load your class" — the harness on this machine | the same failure; two of them are wired to a backend folder (`…/sharpen`) that no longer exists. Not counted either way; the Opus hand walk on TEST covered the same behaviours by hand |

The session's permission check refused one read of the baseline's later result
file (gates 22–25 and the live scripts); those rows say what could be shown
without it.

## Differences left, and why

- **02 stats** keep HANDED IN where Design drew Sittings — the sheet's data
  does not carry a sittings count per pupil; adding a read was not worth it in a
  styling run.
- **04 Students › Score** shows one dash per assignment for a pupil who touched
  none (Design: one dash). `flashcard_progress_drive` asserts one dash per paper
  on purpose; changing it would weaken a gate.
- **04 at 1440**, a "COMPLETE · LATE" status chip can wrap onto two lines
  inside its 150px track rather than widen the grid.
- **05** keyboard up: the progress bar hides (as it already did in Stage D);
  Design's still frame shows it. One row less above the keyboard.
- **06** the chip grid is `auto-fit` (min 28px) rather than a fixed 10 columns,
  so a deck that isn't 10 cards still fills one row; a 10-card deck fits one row
  at 360.
- **06** on the Try-again end screen the chips are drawn but not tappable (the
  engine only allows redo inside a pass); the hint is therefore not on that
  screen.
- **03** the RUSHED marker and the strip's width differ by a few pixels from
  Design; the site's top bar sits above every screen (Design drew the screens
  alone).
- **02/03** History chevron is the existing glyph, not Design's SVG.

## Decisions I made

- **Where "Tap a green card to redo it" shows.** Design put it on the Try-again
  end screen. There the chips cannot be tapped (the engine refuses a redo once a
  pass has ended), and making them tappable would change behaviour. A hint that
  promises a tap which does nothing is worse than none, so it shows beside ×
  whenever a green chip can actually be tapped — during a Try-again pass — and
  never in the first pass or on the end screen. The wording is kept.
- **Cut elements that drives read are hidden with CSS, not deleted** (02's
  toggle, verdict line and status chip; 04's Set column; 05's old header row),
  so no gate had to be weakened. Screen readers skip `display:none`.
- **The screen-03 strip reads per-card states** with an existing read rather
  than drawing three states from counts (the first build did that; sent back).
- **Item 8 fixed at both ends:** display everywhere now, backend source on a
  branch. Without the backend fix, averages built from `max_score` would stay
  inflated for anyone who left a set part-way.
- **Drive assertions changed, ruled cuts only:** `flashcard_progress_drive`
  (columns, CSV header, phone no-scroll now asserts the columns drop; one new
  five-state strip check; one selector fixed — it read the wrong label when both
  answer boxes show), `flashcard_homework_drive` (the hint must show during a
  retry pass and must NOT show in the first pass — new check).
- **The first after-run's "the class page could not load" reds in the tools/
  live scripts are the harness, not the port:** main fails identically on this
  machine (re-ran `flashcards_sharpen_live` on main: same 30 failures). Two of
  them are wired to a backend folder (`…/sharpen`) that no longer exists.

## Parked for the chat

| Item | Where | State |
|---|---|---|
| Backend `max_score` = the set's markable question count | `mrbadmus---backend` branch `fix/max-score-denominator` @ `f7adb90` | tests green, TEST-proved, not deployed (push to main refused by the session's permission check) |
| Stored rows with a short `max_score` | production | a backfill is a production write — Mide's call |
| TEST world | `~/tmp/mrb-shots/design-port/world/teardown.py` | left for Mide's own look; teardown deletes by the snapshotted id list |

## For Mide

1. Class cards for a flashcard deck (item 7) could not be seen with real data:
   the TEST world's current set is a question set. Worth a look on 8r/Sc1 when a
   deck is the open set.
2. Deploy the backend fix (one merge of `fix/max-score-denominator`), or say no.
3. The class-stars 75% rule will count a part-finished set at its true size once
   the backend fix ships.

## Follow-up 1 Oct — flashcard homework counts when it's finished

Mide used the site as a pupil (AY, Anifat) and played a flashcard set through
to the engine's own Done screen — "6 of 6 right" — and finished it. The
teacher side still said `0 of 2 in`, `NOT IN YET`, and the pupil's own row
still said `Complete homework`. On real TEST pupils reproducing the same
history (Ben and Chidi, class 8d/Sc1), the same thing happened: ten or more
Got-it ratings, no `assignment_submissions` row.

**Cause.** The only writer of that row was `flashcard_record()`'s completion
block, which required every card SECURED — Got it in two review sittings at
least 60 minutes apart, or a make Got it plus a review Got it — never just
"finished the homework". Reaching the Done screen and being "secured" are two
different, and very differently-timed, facts; the platform only wrote the
first one down once the second (much later) one happened too.

**Rule (Mide, 1 Oct 2026).** DONE = the pupil has reached the engine's own
Done screen once: a review pass where every card's latest rating is Got it;
in make mode, the writing pass first. That is done/handed in, on both the
pupil and teacher side. SECURED stays separate and smaller — the count shown
beside "done", never required for it. Late = the finishing rating reached
the server after `due_at`.

**What changed**

- `shared/flashcard-homework.js` — the round-aware walk inside `reconstruct()`
  now has a sibling, `finishedAt(rows, cards, mode)`: the FIRST point,
  cumulative over the pupil's whole history (never reset — unlike
  `reconstruct`'s own walk, which resets at every all-right to find the start
  of the next pass), where every card's latest review rating is Got it; in
  make mode, only once every card has a make-phase row too. `endPass()` flags
  `this.end.finished` when `all`; once the end screen's flush settles,
  `Api.onFinish(id)` fires exactly once. Exported on `MRBHomework`.
- `shared/student-live.js` — `wireHomework` wires `H.onFinish = recordFinish`,
  which reads the pupil's own `flashcard_reviews` (+ `event_id`), runs
  `finishedAt`, resolves the finishing rating's SERVER time from
  `flashcard_events.server_at`, and writes `assignment_submissions` in
  exactly the shape `flashcard_record` writes on secure (`score = max_score =
  n`, `status: 'complete'`, `is_late` vs `due_at`, `attempts = attempt_no =
  1`). Idempotent: a row that already has `submitted_at` is never touched —
  never downgraded, never re-stamped. `wireLibrary`'s read is widened
  (`rating, phase, event_id, id`) to run the same walk, as a HEAL, for every
  released flashcard set with no completed submission, on every class-page
  load — this is what catches AY, Anifat, Ben and Chidi. A write that fails
  (RLS/offline) breaks nothing visible and retries on the next load. The
  pupil's own row is patched in place (`fcPatchWorkRow`) so a finished set
  moves out of To do the same visit, with no reload.
- `student_rulings.py` — the done button: **"Give it another go"** (Mide's
  words, no "?"; "Revise your cards" retired). Reopening a done set starts a
  fresh revision pass; it never un-dones the row (Stage D's mid-homework
  resume is untouched — asserted, not just hoped, in the engine tests below).
  The detail line drops "· DECK SECURED" (false under the new rule, and
  secured is a teacher-side fact, not a pupil one). The Avg score tile
  excludes flashcard rows from its sum (a done deck has no `rawMax`/`score`,
  so the old fallback silently added a 0 for every finished deck). The
  score/"CORRECT" chip (`scoreText`/`scoreLabel`) is blanked for a flashcard
  row too — found LIVE during this run's own TEST proof: once a deck reaches
  "marked" the moment it is finished rather than rarely once fully secured,
  that chip, which a deck was never meant to show, read `undefined%` on
  every done deck.
- `shared/teacher-live.js` / `shared/teacher-data.js` — the My classes card's
  main count reverts from design-port-b's "started" stand-in (needed only
  because a deck wrote no submission until secured) back to `colSub` — the
  same "in" the class page's own homework card and THIS WEEK already read,
  now correct because finishing writes the submission at once. "N secured"
  is the card's smaller second fact, filled from `flashcard_progress` for the
  class's CURRENT flashcards set only (never every historical deck — bounded
  the same way the reminders-log read already is per focused class), via a
  new `loadFlashcardSecuredCounts`. The now-unused "started" plumbing
  (`flashcardStartedByAssignment` / `flashcardStartedFor` / `pack.
  flashcardStarted`) is removed — grepped first; nothing else read it.
  `reasonFor`'s "missed" count moves from `scores[i] == null` (always true
  for a deck, which has no marks) to `!row.submitted[i]` — a second,
  independent defect this same code path had.
- The reminder banner (`student-live.js`) now drops a reminder whose
  assignment already has a completed submission — for a flashcard set and
  for every other kind of work alike (`student_reminders_for_viewer` itself
  has no done check; this is a site-side filter, in scope per the plan).
- **Bell link for flashcards: parked, not touched.** The bell's synthesised
  "work" item for a flashcard set points at `/student/assignment.html`, which
  is not where a deck opens (`#cards=<id>` on the class page); fixing it
  needs a backend change, which this ticket's brief does not authorise.

**Parked SQL**, branch `feat/fc-complete-migrations` (commit `e5e5556c6`,
worktree `mrbadmus-worktrees/fc-complete-migrations`, off `origin/main`):
`supabase/migrations/20261001120000_flashcard_finish.sql` — a plpgsql port of
`finishedAt()` inside `flashcard_record`'s own completion block, so the
database agrees with the client the moment this lands, with no feature
detection needed on either side (whichever writes first, the other finds the
row already there and does nothing). Rollback:
`supabase/rollbacks/20261001120000_flashcard_finish_rollback.sql`, the
current (SECURED-based) function body, copied byte-for-byte from the
migration that shipped it.
md5(migration) `9132b03534e67e2dce3738ba34b8642c`,
md5(rollback) `ea9a33ef13b4dd1075c07673799fa103`.

⚠️ **Deviation — the apply/rollback/apply rehearsal on TEST could NOT be
run.** The brief asked for it via something other than `supabase db push`;
the only other apply path this session had access to was a service-role key
(TEST ref `qeppkiswvclkkwbxmlok`, confirmed from the key's own payload),
which can read and write ROWS through PostgREST but cannot execute DDL —
there is no SQL endpoint, and `CREATE OR REPLACE FUNCTION` is not a table
write. The session had no Supabase CLI Personal Access Token and no database
password, and the `supabase-test` MCP needed an OAuth step this unattended
session could not perform. So the rollback's byte-exactness against the
LIVE function (not just the migration file, per memory "Migration body
provenance") is unverified too. **Needs a credentialed follow-up**: apply →
confirm `md5(pg_get_functiondef('public.flashcard_record(uuid,jsonb)'
::regprocedure))` matches the migration's own body → rehearse the rollback →
re-apply, all on TEST only, never production.

**A second, independent write path proves the SAME behaviour without this
migration**: the client write (`recordFinish`/the heal) already ran, for
real, against production-shaped RLS, on TEST — see the live proof below.

**Deviation — `tools/mrb351_acceptance.py` items 5/6 left unchanged.** The
plan that preceded this build flagged items 5 and 6 (rows ~600-662) as
breaking once the parked migration lands: item 5's rushed deck finishes on a
WRITING pass alone under the old rule's `quick`-rule reading (`secured =
known`), which the new make-mode rule (writing pass + an all-right review
pass) would read as not finished. Since the migration is not applied to
TEST, `flashcard_record`'s SQL is byte-identical to before this run, and
these items still pass, unedited, against what is actually deployed. Editing
them now, blind, to anticipate a migration this session could not verify
would risk shipping an unverified test change; left for whoever applies the
migration to rewrite alongside it, per the original plan's wording.

**Proof**

- `node flashcard_engine_test.js` — **186 passed, 0 failed**, including five
  new sections for `finishedAt`/`onFinish`: agreement with `endPass().all`
  including "done on round 2" (a Try-again screen then an all-right retry);
  make mode's writing-pass gate (a pure check: review-all-right rows alone
  do NOT finish a make-mode set); the hour-gap reset moves `reconstruct` to a
  new pass but never un-finishes a pupil (`finishedAt` is cumulative, never
  reset); the documented `‹ Back` + "I don't know" divergence (finishes one
  replay early — accepted, not "fixed"); `onFinish` fires exactly once, never
  on a Try-again screen.
- `flashcard_homework_drive.py`, `flashcard_progress_drive.py`,
  `teacher_reach.py`, `teacher_behaviour.py`, `student_behaviour.py`,
  `today_drive.py`, `mrb328_card_prefetch_drive.py`,
  `mrb348_teacher_rollup_proof.py` — all eight, run sequentially (one Chrome
  at a time, per the gate-receipt round's own rule), **all green, 0 FAILs**.
  None needed an assertion change: all eight key on the submission row or on
  surfaces this ticket did not touch, so the fix is additive from their
  point of view.
- **`tools/flashcards_complete_live.py` (new), on TEST** — a throwaway
  teacher and three pupils, real decks, the real backend (design-port
  worktree, a free port), the real class page served locally, real RLS.
  **24 of 25 checks green** on the final run:
  - (a) a pupil finishes a REVIEW set all-Got-it in one sitting →
    `assignment_submissions` written at Done (score/max 5/5, on time); the
    TEACHER's own `flashcard_progress` RPC reads them `done`; the pupil's
    own data layer shows the row `marked`, `COMPLETED …`, no "secured"
    wording; reopening starts a FRESH pass (`0 of 5 right` again); finishing
    a second time never moves `completed_at` (idempotent, same row id).
  - (b) make mode: the writing pass, then the review pass all-Got-it → Done,
    same write (score/max 3/3).
  - (c) **HEAL, on the EXISTING design-port throwaway world** (class 8d/Sc1,
    pupils Ben and Chidi, the exact two TEST pupils WORLD.md recorded as
    reproducing Mide's bug): loading the real class page as each of them —
    no deck opened, nothing else done — writes the row. Ben: `completed_at
    2026-09-30T19:56:32Z, is_late false`; Chidi: `2026-09-30T21:13:49Z,
    is_late true` — matching WORLD.md's own hand-walked prediction
    ("done 19:56:38, on time" / "done 21:13:49, late") to the second.
  - (d) a pupil one card into a three-card set is NOT done (no submission)
    and reopening resumes on the next undone card — Stage D unchanged.
  - (e) a reminder on the unfinished set still shows; the same pupil's
    reminder on the now-finished set is hidden.
  - The one red: a scripted click on the collapsed work-list row never
    revealed the "Give it another go" button text in headless Chrome,
    across several selector attempts (including switching the week-select
    to "All weeks" first, which was itself a real harness bug this run found
    and fixed — the row's own teaching week differed from "this week"). The
    row's DATA is independently confirmed correct (`status: 'marked'`,
    `detail: 'COMPLETED …'`, `fc: true`) and `student_behaviour.py` (above)
    already drives this exact template's primaryLabel logic byte-for-byte
    against Design's own file; this is recorded as a harness gap, not a
    reproduced defect.
  - Screenshots: `~/tmp/mrb-shots/design-port/fc-complete/shots/fc-complete/`
    — `a-00-teacher-progress-done.png` (teacher), `a-01-done.png`,
    `a-02-give-it-another-go.png`, `b-01-make-done.png`, `d-01-resume.png`,
    `e-01-reminder-shows.png`, `e-02-reminder-hidden.png`,
    `c-ben-after-heal.png`, `c-chidi-after-heal.png` (pupil). Throwaway rows
    torn down by the snapshotted id list each run; confirmed no orphans
    after the final run (`schools` like `FC Complete%` → `[]`).

**Decisions I made**

- **My classes card: "N secured" costs a bounded extra read.** Sharpen B4
  deliberately never fetches `flashcard_progress` for My classes (every
  historical deck, every class, would be expensive). Mide's ruling asked for
  "N secured" there anyway, so the read is narrowed instead of widened back
  to that cost: one `flashcard_progress` call per class whose CURRENT set is
  a flashcards deck, never per historical deck, never for a class with no
  flashcards work open. A failed count costs that one card's second line,
  never the page.
- **The Avg score tile and the score/CORRECT chip both exclude flashcard
  rows**, rather than inventing a mark for a thing that has never been one.
  The chip fix was found live, mid-proof, on real TEST data — not predicted
  by the plan — and is in scope for the same reason the Avg-tile one was:
  both are "a deck reaching `marked` far sooner now breaks a display that
  assumed `marked` was rare for a deck."
- **`reasonFor`'s missed-count fix rides along.** It is the same `w.scores[i]
  == null` vs `!row.submitted[i]` confusion as the Avg tile, on the exact
  code path this ticket already had open, and it also quietly fixes a
  submitted-but-not-yet-marked MCQ row being counted "missed" — a latent bug
  with nothing to do with flashcards.
- **The migration's rehearsal gap is reported, not hidden or faked.** No
  `--db`-style confirmation exists for this session to fabricate; the client
  write stands on its own TEST proof instead, and the migration stays
  genuinely parked until someone with a DB credential can run the three-step
  rehearsal.
- **`mrb351_acceptance.py` items 5/6 are left alone, on purpose**, for the
  reason given above — they are correct against what TEST actually runs
  today.

**For Mide**

1. The parked migration needs a session with a Supabase Personal Access
   Token or a DB password to actually rehearse (apply → confirm the live
   `prosrc` md5 → rollback → re-apply) before it can be merged with
   confidence. This session proved the ruling live without it, via the
   client write.
2. The flashcard bell link (opens `/student/assignment.html` instead of the
   class page's `#cards=` overlay) is a real dead end for a pupil clicking
   it from the bell panel, and needs the backend team.
3. Known, accepted divergence: a pupil who uses ‹ Back to rate an
   "I don't know" card Got it before its scheduled replay comes round is
   recorded as finished one replay earlier than the screen shows them. They
   are one tap from Done either way; not fixed, per the engine's own
   comment.

### Review pass, 1 Oct 2026 — one must-fix, three should-fixes, all closed

Opus 5.5 reviewed commit `bfd266295` and sent it back. Fixed in commit
`c1adc96bf` (after rebasing `fix/flashcard-completion` onto `origin/main`
`64a0cb303`, which carries this same design port — the rebase replayed
clean, no generated-file conflicts, `build_all.py` reproduced byte-identical
output).

**MUST-FIX — `finishedAt()` disagreed with `reconstruct()` about which pass
a pupil is in.** `finishedAt` walked the pupil's whole history cumulatively
and never reset. `reconstruct()` DOES reset: a leftovers ("Try again") round
left stale for 60+ minutes gets a fresh pass (the engine re-asks the whole
deck, weak card first — `rankedIds`). The reviewer's repro: sitting 1 rates
c0–c3 Got it, c4 Not yet (leftovers); a day later the pupil gets c4 (ranked
first in the new pass) right; `reconstruct` correctly shows 1 of 5 rated,
not ended — but the old `finishedAt`, never resetting, saw every card's
all-time-latest rating as Got it and called the pupil done, one card into a
pass they had not finished. That would have stamped `completed_at`
permanently wrong (too early — a genuinely late finish could read "on
time") via the heal, on the very next class-page load, for any real pupil
who ever left a deck mid-leftovers for an hour.

**Fix:** factored the round-aware walk out of `reconstruct()`'s step 2 into
one shared `walkReview()` (`latest`/`targets`/`done`/`complete`/`n`/
`lastAt`, the hour-gap reset, the round advance) — both functions now call
it, so they cannot drift apart again by being maintained separately.
`finishedAt` takes `walkReview`'s `firstFinish`: the first row, anywhere in
history, at which the pass showing AT THAT INSTANT was all Got it. The
IDK-replay branch is carried into the shared walker (and so into
`finishedAt` too, for symmetry), though real callers never pass `idk` (it is
a device-local record with no server equivalent) so it is inert for them in
practice — documented in the function's own comment rather than left
implicit.

New engine test 33 (the reviewer's own `scratchpad/div.js` repro, as a
pure-data test): null after the leftovers screen; null after one card of
the fresh pass (**the exact case that was wrong**); a hit at that pass's
own last card. `node scratchpad/div.js` confirms the same sequence directly
against the fixed module. `node flashcard_engine_test.js`: **191/191**
(186 + the 5 finishedAt/onFinish sections already in commit `bfd266295`,
+ test 33).

**Parked SQL** (`feat/fc-complete-migrations`, commit `bbd68a144`): the
same round-aware walk, ported into `flashcard_record`'s completion block —
`v_targets`/`v_round_done`/`v_n_round`/`v_round_complete`/`v_last_at`
mirroring the JS locals, the same hour-gap reset and round-advance. The
IDK-replay branch is NOT ported (no server-side device record exists, and
`finishedAt`'s real callers never pass one anyway — same reasoning as the
JS). Still parked, still unrehearsed on TEST — this session has no
Supabase PAT and no DB password, so there is still no way to execute DDL
here; unchanged limitation from commit `bfd266295`, reported again rather
than silently repeated.
md5(migration) `bce3e7164bcd1a4e9bdcec7a96ad1156` (was
`9132b03534e67e2dce3738ba34b8642c`). md5(rollback)
`ea9a33ef13b4dd1075c07673799fa103` (unchanged — the rollback restores the
PRE-this-ticket body, which this fix does not touch).

**Should-fix 1 — the Avg score tile's own caption contradicted its
number.** `avgMarks` (the earlier fix) excludes flashcard rows from the
average; the caption underneath it still read `marked.length`, every
marked row including decks — "63% · 2 MARKED" for an average that was
really one set's score. Same filter, same reasoning, now on the caption
too (`student_rulings.py`). Left alone, flagged for Mide: the row word and
filter tab both still say "Marked" for a finished deck, which is a product
wording decision, not this same caption-contradicts-its-number bug.

**Should-fix 2 — the heal's reads had no `pupil_id` filter, and the write
had no membership check.** RLS already restricts a real pupil to their own
`flashcard_reviews`/`flashcard_sessions` rows, but nothing stopped a
staff/admin account's OWN uid, under a broader read policy, from pulling
rows it should not and then writing a submission naming itself as the
pupil (`submissions_self_all` only checks `student_id = auth_user_id()` —
it cannot tell "a real pupil" from "any signed-in account using its own
id this way"). Added `.eq("pupil_id", uid)` to both reads
(`shared/student-live.js`), and a new `pupilMemberOfAssignmentClass`
check inside `writeFinishedSubmission` itself — the write refuses unless
`uid` is a `class_members` row (not left, not deleted) for the
assignment's own class. One extra read, per WRITE only (never per heal
check, since writes are rare).

**Should-fix 3 — the heal read flashcard_sessions unconditionally.** Every
class-page load used to read sessions/`server_at` for every deck a pupil
had ever rated, regardless of whether anything needed finishing. Restructured
so the (cheap) `assignments`/`assignment_submissions` reads run first,
`finishedAt` is computed from data already in hand, and the session read
only fires for the resulting (usually empty) "needs a write" list — zero
extra requests for a pupil whose decks are already recorded or none
finished.

**Should-fix 4 (the harness) — the "Give it another go" check tapped the
wrong element.** The row's own header IS the toggle button
(`student_rulings.py` "PROD N4": node 161, `<button onClick=
{{r.toggle}}>`, which that ruling also gives `aria-expanded`). The first
build's probe searched `button,[role="button"],div` for the first element
whose text started with the title — which could, and did, land on an
outer wrapper sorting earlier in document order than the real button.
Scoped the tap to `button[aria-expanded]` instead.

**Proof, after the fixes, rebase and rebuild:**
- `node flashcard_engine_test.js`: **191 passed, 0 failed**.
- `node scratchpad/div.js` (the reviewer's repro): confirms the fixed
  sequence directly (`null`, `null`, `null`, then "reconstruct now: stage
  review pass size 1 ended null" — the pupil correctly read as 1 of 5
  rated, not finished).
- `flashcard_homework_drive.py`, `flashcard_progress_drive.py`,
  `student_behaviour.py`, `teacher_reach.py`, `today_drive.py`: **all
  green, 0 FAILs**, each run sequentially post-rebase.
- `teacher_behaviour.py`: one run hit a transient `chrome closed the
  websocket mid-frame` (the known CDP flake CLAUDE.md names); retried
  once, green — **1061 of 994 controls pressed, 0 FAILs**.
- `tools/flashcards_complete_live.py` on TEST, post-rebase and post-fix:
  **25 of 25 checks green** — every check from the first pass PLUS the
  previously-red "Give it another go" tap, now passing (`{'label':
  "Give it another go", 'context': "Give it another go"}`). The heal
  re-ran against the same real TEST pupils Ben and Chidi and reproduced
  the identical `completed_at`/`is_late` from the first pass byte for
  byte, confirming the write is stable across repeated runs, not just
  idempotent within one. No orphaned throwaway rows after the run.

Commit: `c1adc96bf` (`fix/flashcard-completion`, rebased onto
`origin/main` `64a0cb303`). Parked SQL: `bbd68a144`
(`feat/fc-complete-migrations`).

---

## Sweep fixes, 1 Oct

An Opus code review of the sweep-fix WIP (`f928cd136..3fe37f1a2`,
`docs/.../sweep/REVIEW.md`) sent it back: seven must-fixes, two of which
made the underlying defect worse rather than fixing it, and one of which
(C1) reversed a quoted Mide ruling on this run's own say-so. This round
applies the review's findings. No browser was used by the review; every
item below was then driven for real on TEST against the design-port
throwaway world (`docs/.../world/WORLD.md`, class `8d/Sc1`) to prove the
fix reaches the screen, not just the diff.

### 1. B1 — scheduled work was hidden from the whole class page

**What Mide would have seen (the sweep's own fix, before this round):** he
sets a flashcard pack for next week, and it vanishes — not just from "N of
M in", but from the Assignments table, the "N assignments" header and the
Reteach card's own rail, because the first fix filtered `wPapers` itself,
and everything on the class page reads `wPapers`.

**What changed (`teacher_rulings.py`, the `const openP` tuple and the
`wTally`/`wAllClosed` tuple just below it):** `wPapers` is restored to
every state. A new `wReleased` (`wPapers` minus `state === 'scheduled'`)
is the source for `wIdxs` — and therefore `wTally`, `wSub`/`wAsk`/`wMean`,
the chase list and `weekScore` — and for `wAllClosed`. The Assignments
table, the header count, the "Nothing open…" line and `openP`/"+N more"
all keep reading `wPapers`, untouched.

**Proof (TEST, class-detail.html, `8d/Sc1`):** the Assignments table still
lists "Animal and plant cells — homework (next week)" with `STATUS
SCHEDULED`, and the header reads "5 ASSIGNMENTS · 6 THIS TERM" (`wPapers`,
includes it). Every roster row reads "N of **4** in" (`wReleased` — the
scheduled set excluded from the denominator); before this fix it would
have excluded the scheduled set from the TABLE instead, making a
teacher's own next-week homework disappear.
Screenshots: `sweep/fix/b1-class-detail-1440.png`, `-390.png`.

### 2. B5 — the digest zeroed on the path most classes take, and mixed two units on one screen

**What Mide would have seen:** a head-of-department's ON TIME and MEAN
tiles reading "—"/zero on any class the digest reaches via the database
rollup (`teacher_class_rollup_v2`) rather than the full read — which is
most classes, on a real roster, most of the time — because only
`buildMatrix` ever computed `inWeekPaper`, and `matrixFromRollup` read it
back as `undefined`.

**What changed (`shared/teacher-live.js`):** the "this week" predicate is
now `computeInWeekPaper(papers, week)`, one function above `finishMatrix`,
called identically by `buildMatrix` (replacing its inline block,
byte-for-byte the same rule) and by `matrixFromRollup` (new). **Units:**
the whole-school Submissions tile is relabelled "Pupils in" —
`totalSubs` is a PUPIL count (`c.week[0]`), while On time counts
SUBMISSION CELLS, so the two were sitting side by side under one word
("Submissions") answering different questions; relabelling was chosen
over recounting because `totalSubs`/`c.week[0]` feeds other screens'
vocabulary unchanged (`teacher_rulings.py`).

**Proof (TEST, digest.html, no class filter — the rollup path):**
`window.__MRB_DATA__.MATRIX['6d6...'].partial === true` (confirms the
rollup path, not `buildMatrix`) with `inWeekPaper` keys `['1','2','3','4']`
— populated, not `undefined`. On screen: "PUPILS IN 6 · Across 1 active
class" beside "ON TIME 64% · 4 late of **11 submissions** with results" —
nonzero, and the two tiles no longer share one noun.
Screenshot: `sweep/fix/b5-digest-1440.png`.

### 3. C3 — the Edit sheet's TOPIC line, and why the first fix never painted

**What Mide would have seen:** opening Edit on a released set still reads
"TOPIC: Sweep respiration set" — the set's own title, not its topic — on
every edit, because the first fix set `S.roScope` inside `loadScope()`'s
async callback but nothing ever repainted `els.roScope.textContent` from
it, and `syncStep()` (the only thing that paints it) had already run,
synchronously, before `/scope` answered. It also read only
`S.scopes[0]`, so a multi-topic set would have shown just its first topic
even once repainted.

**What changed (`shared/set-work.js`, `loadScope()`):** the block moved to
AFTER `placeStored()` (which is what splits a multi-topic set's stored
questions across `S.scopes`), now maps `scopeName()` over **every** scope
and joins the results with " · ", and repaints
`els.roScope.textContent` directly rather than waiting for a `syncStep()`
nothing calls again.

**Proof (TEST, class-detail.html → `MRBSetWork.edit()` on the real
Q1 set, `scope_kind:'topic', scope_ref:'B1'`):**
`[data-sw="ro-scope"]`.textContent reads "Cells and organisation" — the
real KS3 topic name from the real `/scope` tree — not "Cells and
organisation — homework" (the title). Screenshot:
`sweep/fix/c3-edit-topic-1440.png`.

### 4. C9 bench title — the first fix was dead code

**What Mide would have seen:** a three-topic auto set's bench still reads
just its first topic ("Energy transfers"), because the first fix read
`current.questions[].topic`, a field `/api/class/current-assignment`
never returns (confirmed read-only against the backend,
`readAssignmentWithQuestions`, server.js ~1234–1249) — so `caTopics` was
always empty and the fallback to `ca.topic` fired every time, silently.

**What changed (`shared/student-live.js`, the `benchWork` block):** for
`ca.source === 'auto'`, the topic list is read off `ca.title.split(' · ')`
instead — the composer's own separator (`server.js` ~2240,
`topics.join(' · ')`, read-only, confirmed), the same one
`scopeName()` uses for a "Topic · Subtopic" name. A teacher-set title is
used whole, as before.

**Proof (TEST, student/class.html, pupil Farah — her real auto set spans
three topics):** `window.__MRB_DATA__.benchDoneTitle === 'Mixed topics'`.
Screenshots: `sweep/fix/c9-a4-bench-done-390.png`,
`a4-bench-compact-scrolled-390.png`.

### 5. C9 aria — the flip button was hidden while focused

**What Mide would have seen:** nothing (a screen-reader-only defect) — a
pupil using a screen reader loses the only control on a flipped flashcard,
because `faces[0]` IS the flip `<button>` itself (template node 10334),
and the first fix set `aria-hidden="true"` on it while it still had focus.

**What changed (`shared/student-live.js`, `syncFlipAria`):** only
`faces[1]` (the back `<div>`, no focusable elements) is toggled; `faces[0]`
is never touched. The front face is never hidden while unflipped either
way, so no drive assertion needed to change.

### 6. C6 — HANDED IN stopped contradicting the chip, then started repeating it

**What Mide would have seen:** the per-pupil sheet's HANDED IN tile read
"In progress" — the exact word the status chip immediately above it
already shows — for every pupil who hadn't handed in, trading the
original bug (HANDED IN said "Not yet" while the row pill said "Missing"
for the same pupil) for a different one (a label repeating its own
neighbour, against the standing no-redundant-text rule). Separately, "Done
late" was a green pill wearing the exact colours of "Missing" (the first
fix's own over-correction for a green pill with a stray red square).

**What changed:** `shared/flashcard-breakdown.js` — HANDED IN now reads
"—" for every state that isn't done/done_late (TIME's own convention,
right beside it), instead of repeating the chip. `shared/
flashcard-progress.css` — `.fp-st-late` keeps the green/ok tone (it IS
done) and only its DOT changes to the site's late-dot shape (a square, in
the warn/orange tone, matching `student-detail.html`'s `stDot`) —
distinct from both "Missing" (orange pill) and plain "Done" (round green
dot). `flashcard_progress_drive.py:915`'s assertion updated:
`"In progress"` → `"—"` (old-before-either-fix value: `"Not yet"`).

**Proof (TEST, flashcards.html, Dev Patel — genuinely Missing on F1):**
HANDED IN tile reads "—"; the row pill is an orange "Missing" chip with a
square dot, "Done late" rows are green with a square orange dot, "Done"
rows are green with a round dot. `flashcard_progress_drive.py`: 0 FAILs.
Screenshots: `sweep/fix/c6-flashcards-table-1440.png`,
`c6-breakdown-sheet-1440.png`.

### 7. C1 — reverted; put to Mide

**What Mide would have seen:** with two live sets open, "Reteach from the
last set" stays on screen (it used to cede its slot to the second set,
MRB-336 §4.1) — which sounds like a pure improvement, except the ruling it
overturns quotes Mide's own words ("live assignments should take over the
reteach from last lesson card"), and the justification for overturning it
was this run's own gloss on a finding, not a quoted instruction from him.
Separately, `currentSet()` was changed to pick the open paper due
soonest rather than the first in the list, which disagreed with the class
page's own lead card (newest release) the moment two sets were open.

**What changed:** both reverted, byte for byte. `teacher_rulings.py`:
the `showReteach: true` override tuple removed; MRB-336 §4.1's
`showReteach: wCards.length < 2` stands. `shared/teacher-live.js`:
`currentSet()` back to "the first open paper, in `papers`' own order".

**Put to Mide (his calls, not this run's):**
- Should Reteach keep its slot even behind two live assignment cards, and
  if so, which of the (at most two) live cards gives way?
- With two sets open, which one should lead — the class page's own first
  card (`wOrder`, newest *release*) or "My classes"' `currentSet()`
  (currently the first *open* paper in list order, which is closed-set-
  aware but not due-aware)? They can presently show different sets for
  the same situation.

### 8. A1 — should-fix: rounding and scope

**What changed (`shared/student-live.js`, `weekOf()`):** `Math.floor` →
`Math.round`, matching `weeksBetween()` in `shared/teacher-live.js`
byte-for-byte (its own comment explains why: a floor divides 6.99 weeks
down to 6 across a clock change). The release-instant/teaching-week
fallback is now gated on `card.kind === 'flashcards'`, matching the
teacher side's own scope (`assignPaperWeeks()`); every other row keeps
its original `due_at − 7-day-block` fallback unchanged.

### 9. A4 — should-fix: the done bench reading as two things

**What Mide would have seen:** a done bench showing two full-size
headings and two full-size buttons — the done card's own ("Mixed topics" /
"See your answers") and the injected next-step box's (also a full
headline + a filled pill button) — reading as two things of equal weight
rather than one done thing with an optional next step.

**What changed (`shared/student-live.js`, `drawBenchNext`):** on
`benchDone`, the injected box is compact — one line of text (no `<h2>`)
and one underlined link-style action, never a second filled button. An
empty bench (no done card of its own yet) keeps the original full
presentation, since the box IS the bench's one thing to say there.

**Proof (TEST, Farah — a done auto set + a missed set to nudge about):**
the bench frame holds exactly one `<h2>` ("Mixed topics", the done card's
own) and the injected box reads "Using a microscope — homework (last
week) · Was due Wed 23 Sep, 20:55" + one underlined "Finish it" link — no
second heading, no second filled button. The dead PRACTICE "—" tile (a
pre-existing defect, not touched by A4) is still on screen awaiting
Mide's ruling (see below). Screenshot:
`sweep/fix/a4-bench-compact-scrolled-390.png`.

### Parked (unchanged by this round)

- **A1's SQL fix** — `flashcard_set_work()` still never stamps
  `academic_week`; the site-side fallback this round tightened is the
  interim, not a replacement for the migration (`feat/mrb352-migrations`,
  per the phone/sharpen runs).
- **B4's backfill** — `max_score = count(assignment_questions)` on
  existing mcq submission rows; the backend fix (design-port) does not
  repair rows written before it landed.

### Mide's calls (not this run's to make)

- **C2** — the Set work sheet says "Not set yet" for topics the automatic
  set already covered this week (`server.js` `teacherSetHistory` is
  `source='teacher'` only, deliberately — a product ruling, not a bug).
- **C7** — the pupil class-page Leaderboard is permanently empty by
  design (`shared/student-live.js` sets `roster=[]` on purpose, pending
  Mide's ruling); a dead section under the no-redundant-text rule until
  he rules on it.
- **C8** — "Revise after marking" shows the pupil the answer, then lets
  them pick it; no code defect, a product question about whether that is
  the intended design.
- **The PRACTICE tile** — `practiceAnswered` reads `""` always; nothing
  ever writes it. A4 made the bench reachable again from a done state but
  did not touch this dead tile, per the should-fix's own instruction to
  park it for Mide.
- **"Marked" for a done deck** — the row word and filter tab call a
  finished flashcard deck "Marked", which is not a mark; a wording
  decision, flagged in the fc-complete section above, still open.
- **C1's two questions** — see item 7 above.
- **The "Back to today" link** — class-detail.html's "Back to today"
  shows even when the teacher arrived from My classes (C9 small item);
  cosmetic, not touched this round.

**Proof, this round, in full:** `node flashcard_engine_test.js` — 191/191.
`python3 teacher_tells.py` — 6/6 live pages clean. `python3
theme_wiring_check.py` — 1331 wired, 0 not wired. `python3
gate_registry.py --check` — clean. `python3 flashcard_progress_drive.py`
— all checks green (incl. the updated HANDED-IN assertion), twice
(before and after the final `build_all.py`). Live TEST screenshots for
every must-fix and A4, in `sweep/fix/`, against the design-port throwaway
world — read-only, no new writes.
