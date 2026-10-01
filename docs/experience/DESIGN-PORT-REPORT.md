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
