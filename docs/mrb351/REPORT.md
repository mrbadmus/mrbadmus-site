# MRB-351 — Flashcard homework: build report

Branch `claude/flashcard-homework-feature-c2thi1`. Everything below was built and verified on **TEST**
(`qeppkiswvclkkwbxmlok`). Nothing was applied to production, and nothing was written outside TEST.

## What shipped (one paragraph)

A teacher opens **Set work**, picks **Flashcards** instead of Questions, chooses the classes, and
gets a deck in one of five ways: upload a file, paste text, type cards, or pick from **My decks** or
**Shared**. Whichever way the cards arrive, they land in the same review table before the deck can be
saved. The teacher then chooses **Pupils write the answers** or **Ready-made cards**, and **Secure** or
**Quick**, and sets the work through the existing title / release / due / note controls. Pupils see
*Flashcards · 20 cards* in their work list, and the existing bell's "New work" item fires for it. The
work opens in the class page's **existing flashcard overlay**, which is Design's one flashcard component
with a homework mode added. Every event goes through one server function that computes the timings
and writes the ordinary submission when the pupil is done. Teachers get a live progress page per
assignment and a deck library. The kind split runs through the six teacher screens and the rollup.

## Decisions taken (each is mine to take under §8; flagged ⚑ where Mide may want to flip it)

1. **Server logic lives in Postgres functions and two Supabase edge functions in this repo, not on
   Render.** The §0 rule is "put extraction where the existing API calls live unless there is a
   concrete reason not to". There are two concrete reasons. First, the Render backend's repo is not
   reachable from this build session (GitHub reports no access to `mrbadmus---backend`). Second, TEST
   has no deployed backend at all (TEST's `BACKEND_URL` is `localhost:3000`), so a Render route could
   not have been proved on TEST. This repo already owns edge functions (`roster-import`).
   - The pupil write path, completion, set work and progress are SECURITY DEFINER functions with
     internal gates, the same pattern as `teacher_class_rollup`.
   - Extraction (`flashcard-extract`) and answer checking (`flashcard-answer-check`) are edge
     functions that hold the service role.
2. **Still one assignment system.** A flashcard homework is an `assignments` row with
   `kind='flashcards'` (default `mcq_set`), `source='teacher'`, the existing release/due/note columns,
   the existing soft delete, and the existing `assignment_submissions` row on completion (score N/N,
   `status='complete'`, `is_late` stamped). `quiz_type='flashcards'`: the CHECK is widened, never
   narrowed. Because of this, the backend's bell scan picks it up with no change (teacher-set,
   released, not deleted), and so does the delete route on the class table.
3. **Still one flashcard component.** The pupil flow is the class page's flashcard overlay
   (MRB-284) in homework mode.
   - Design's card, flip, pips, counter, close button and bench theme draw the homework card.
   - Homework mode only adds a progress strip, the answer box, Reveal, the three ratings and a
     panel, all behind `hwOn` (`student_rulings.py`, MRB-351 section). On Design's fixture it is
     inert, and `student_behaviour` (visible text and controls identical to Design's own file) stays
     green.
   - The bell's link (`/student/assignment.html?assignment=<id>`) redirects a deck to its class page
     at `#cards=<id>`, so there is no second notification path and no second page.
4. **⚑ Secure rule, as reconciled with acceptance item 3.** §1 says: every card has Got it in two
   different sittings, the later starting ≥60 min after the earlier ended, and the make-phase rating
   counts as the first session. Acceptance 3 then expects "secures 12" within the first sitting.
   Both hold only if **the make phase is its own sitting**. So a make-phase Got it pairs with any
   review-phase Got it, and two review sittings need the 60-minute gap. That is what stops "Finish
   for now" and straight back in from counting twice. Sitting boundaries use **server** time, so a
   device clock cannot fake the gap. The consequence: a pupil who gets a card right while writing it
   and right again in review secures it the same evening. If you want make → review to need the hour
   too, it is one line in `flashcard_card_state`.
5. **Finished decks count as handed in but never enter a mean.**
   - A deck's N/N is a completion stamp, not attainment.
   - `teacher_class_rollup` (migration 3) and its JavaScript twin `cellOf` both treat a flashcard
     cell as a cell: it counts as submitted, on time or late, and toward completion and "last active".
   - It is never *graded*. On 10Z the class mean stays 85; it would have read 88.
6. **The bench stays a question-set docket.** A deck never takes the "this week's work" bench slot at
   the top of the pupil page. It stays in the work list and opens the overlay.
7. **Two extraction paths.**
   - Clean two-column tables (docx, xlsx, csv, pptx tables) and Q:/A: text are paired **exactly,
     without a model**. They cost nothing and cannot be paraphrased.
   - Everything else is one structured Claude call (`claude-sonnet-5`, vision for scans and photos).
     PDFs and images are sent whole.
   - HEIC is converted to JPEG in the browser; if the browser cannot decode it, the server says so.
8. **Answer check** is `claude-haiku-4-5`. It receives only question, model answer and pupil answer,
   numbered 0..n-1 inside the request. Blank / "idk" / one-word answers are decided in SQL
   (`flashcard_quick_check`) and never sent. It is triggered at the end of each sitting and when the
   teacher opens the progress page (fire and forget), not by a cron, which needs no secret in the
   database.
9. **Live teacher view** polls `flashcard_progress` every 10 s while the tab is visible. MCQ results
   have no live mechanism to reuse, and Realtime would add a second transport for one screen.
10. **Deck topic tags.** Subject chips only in v1. `topic_id` / `subtopic_id` exist for the curriculum
    tree, but that tree is served by the backend's `/scope`, which TEST cannot reach.
11. **academic_week** is left NULL on flashcard rows, as it already is on many teacher-set rows. The
    week is computed by the backend.
12. **Queue order** follows §4 (Not yet → Nearly → never rated → Got it). Within Got it, cards still
    unsecured come before secured ones, so a second sitting starts on the work that is left.
13. **Swipe** right = Got it, left = Not yet. Nearly stays a button. Keys are Space to turn the card
    and 1 · 2 · 3 to rate.
14. The overlay's entrance animation used to replay on every redraw, which flickered on each tap,
    practice deck included. It now plays once per opening (after-draw hook, live page).

## Migrations — apply in this order (Cowork, byte for byte)

| File | Rollback |
|---|---|
| `supabase/migrations/20260924180000_mrb351_flashcards_schema.sql` | `supabase/rollbacks/20260924180000_mrb351_flashcards_schema_rollback.sql` (⚠️ lossy, read its header) |
| `supabase/migrations/20260924180100_mrb351_flashcards_functions.sql` | `supabase/rollbacks/20260924180100_mrb351_flashcards_functions_rollback.sql` (run first when rolling back) |
| `supabase/migrations/20260924180200_mrb351_rollup_kind.sql` | `supabase/rollbacks/20260924180200_mrb351_rollup_kind_rollback.sql` |

Plus, on production:
- **Edge functions:** deploy `flashcard-extract` and `flashcard-answer-check` (the directories are
  under `supabase/functions/`; both import `../_shared/flashcards/`).
- **Secret:** set `ANTHROPIC_API_KEY` on the edge functions. Without it, the model path fails cleanly
  with `no_api_key` and answers stay "pending". Table and Q:/A: extraction still works.
- **TEST clean-up (optional):** delete the retired helper functions `mrb351-test-session` and
  `mrb351-env-probe` (both now answer 410 to everything), and the evidence table
  `public.mrb351_acceptance_log`.

RLS is in the post-MRB-348 shape: one policy per table per command, cheapest branch first, no
row-dependent SECURITY DEFINER call in any policy body. Pupil tables carry `school_id` and `class_id`
so the teacher branch is an index probe on `class_teachers`. Pupils have no INSERT/UPDATE policy on
any pupil table: `flashcard_record()` is the only write path.

## Extraction — fixture corpus score

- **13 files, 133 pairs, every shape in §2:** next-slide pptx, speaker notes, red answers, a class
  list to ignore, a docx table, an answer section, a text pdf, a scanned pdf, a phone photo, csv,
  xlsx keywords, cloze, questions-only.
- **Score: 133 / 133 = 100.0 %**, with 0 extra cards and 0 names leaked. A negative control (answers
  shifted by one card) recovers ≤ 2/20, so the scorer is not a rubber stamp.
- **How the model path was measured:** no Anthropic API key exists in this build environment or on
  TEST. So the model-path replies were produced by running the **exact** system prompt and input
  through Claude Sonnet in this session, and recorded under `tests/fixtures/flashcards/recorded/`.
  CI replays those replies on every push. **When the `ANTHROPIC_API_KEY` repo secret is set, the
  workflow also makes the real calls and scores them.** The no-model shapes (docx table, xlsx, csv)
  run for real.
- **Still to do:** the genuine Rainford pptx at live-test time.

## Acceptance (§7) — status on TEST

The server and data side ran on TEST under real roles, and the evidence is in
`public.mrb351_acceptance_log` on TEST. The page behaviour ran in headless Chromium against the
compiled pages with stubbed transports (`flashcard_homework_drive.py`, `flashcard_decks_drive.py`,
`flashcard_progress_drive.py`).

1. **Deck made and set to two classes — ✅ on TEST.** The 20-card deck was saved, then set to 10A
   and 10Z Physics as "Pupils write the answers", due Fri 2 Oct 15:00 London (14:00Z), with a note.
   - The upload itself was proved with the csv (202 → job `done`, 15 pairs, file stored at
     `school/<id>/flashcards/<deck>/<sha>.csv`) and the paste box (model path → `failed: no_api_key`
     as designed).
   - The pptx's ≥18/20 is proved by the recorded corpus (20/20), not by a live call.
2. **Pupils see the work — ✅ data side.** Pupils in both classes read the assignment, the note and
   the 20-card snapshot; a pupil in neither class reads nothing. The bell is the backend's existing
   scan of released teacher rows; its preconditions hold, but the scan itself was not run (TEST has
   no backend).
3. **Hannah's first sitting — ✅ exact.** In progress · Made 20/20 · Secured 12/20 · 1 sitting ·
   7:00 active · 3.95 s median think, all equal to the figures computed independently from the
   events. A batch re-sent twice stored 141 events for 141 sent.
4. **Hannah's second day — ✅.** Next day (TEST time shift of the first sitting) → Done, on time. The
   ordinary submission was written (20/20, complete). "Keep revising" still records (3 sittings).
   The status flipping on an open tab is covered by the progress drive's poll test.
5. **Rushing and blanks — ✅.**
   - 20 cards rated in 17.95 s gives a median think of 0.4 s, and Rushed is flagged (a flag only,
     the work still completed).
   - 10 × "idk" shows as 10 blank.
6. **Late and missing — ✅.** Completing after the deadline gives Done late (`is_late` true); pupils
   who never opened it show Missing.
7. **Snapshots are frozen — ✅.** Editing the deck (card 1's answer changed, one card removed) left
   the live assignment unchanged (20 cards, original answer). The duplicate is independent (1 card vs
   19).
8. **A colleague reuses the deck — ✅.** The colleague finds the shared deck and sets it to 8X1 as
   Ready-made / Quick. The pupil opens straight into review and completes when every card has one
   Got it. A smuggled `answer_submitted` in a review-mode deck is ignored.
9. **MCQ unchanged.** See the gates below.
10. **Rollup — ✅ exact.** The rollup for 10A (MCQ + flashcards) equals an independent recomputation.
    On 10Z the class mean is 85, where it would be 88 if the flashcard N/N were graded.
11. **Extraction score — ✅.** 133/133 recorded, CI workflow added
    (`.github/workflows/flashcards-extraction.yml`).
12. **RLS — ✅, after one leak was fixed.** The who-sees-what matrix covered 9 identities × 8 tables
    plus the bucket, and write probes.
    - **It found one leak:** pupils could read shared decks, because the school branch lacked a
      staff check. This was fixed at the source in migration 1 and re-verified.
    - After the fix, pupils see 0 decks and 0 cards and none of another pupil's rows; a pupil in 8X1
      reads no 10A snapshot; a teacher of 10A/8X1 is refused 10Z; the other school sees nothing;
      anonymous callers are refused everywhere; every direct pupil write is refused.

## Gates run here (Linux container, `MRB_CHROME` → Playwright Chromium)

See the PR description for the final list, with results.

## Not done / open

- **Push:** GitHub refused the push (403, the app is not linked for this session). The commits are
  on the local branch. Reconnect GitHub, then push, then open the PR.
- **Live model calls:** extraction and answer check need `ANTHROPIC_API_KEY` set as an edge-function
  secret, and as a repo secret for the live CI score.
- **Backend follow-up (separate repo, not reachable here):**
  - `current-assignment`'s `week_work` should filter `kind='mcq_set'`. The student page already
    ignores flashcards there, so this is tidiness, not a bug.
  - The worksheet route should refuse `kind='flashcards'`. The UI no longer offers Download on
    flashcard rows.
- **Out of scope in v1, as written in §3:** printable deck, images on cards, and AI-drafting a deck
  from a topic.
