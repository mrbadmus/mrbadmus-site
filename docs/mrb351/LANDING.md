# MRB-351 flashcard homework — landing (27 Sep 2026, unattended)

## For the chat: what to apply, in this order

The migrations are parked on branch **`feat/mrb351-migrations`** (not on main). Apply them to
production with the files' exact bytes, in this order:

| # | file | md5 |
|---|---|---|
| 1 | `supabase/migrations/20260924180000_mrb351_flashcards_schema.sql` | `07af0b37e17ffb323baea00001889b06` |
| 2 | `supabase/migrations/20260924180100_mrb351_flashcards_functions.sql` | `0bf90094e1b51de80cfc9f0cf24c461b` |
| 3 | `supabase/migrations/20260927100000_mrb351_rollup_v2_live_results_kinds.sql` | `ab4aa701bb39659b81b246b3172a0e4f` |

Rollback runs in the reverse order, 3 → 2 → 1:

| # | file | md5 |
|---|---|---|
| 3 | `supabase/rollbacks/20260927100000_mrb351_rollup_v2_live_results_kinds_rollback.sql` | `6597512ee4606e66cfb521139b7616fa` |
| 2 | `supabase/rollbacks/20260924180100_mrb351_flashcards_functions_rollback.sql` | `eb57a5e59b014824c37fcbd75e3c4e16` |
| 1 | `supabase/rollbacks/20260924180000_mrb351_flashcards_schema_rollback.sql` | `97226103c69c5527902521b2e0e58187` ⚠️ **lossy**: it deletes every deck, card, pupil answer and flashcard submission. Read its header first. |

`supabase/MRB351-APPLY.md` on that branch is the full apply sheet. It covers the last-activity rule, stale tabs, the production FK list, and the comment-independent fingerprint query that verifies the apply. The Supabase MCP strips `--` comments, so raw `md5(prosrc)` will differ from the file even when the logic is identical. All 15 functions matched on TEST using that query.

**Edge functions.** Deploy them **after** migrations 1 and 2, from a checkout of `main`, where their source now lives:

| function | directory | imports |
|---|---|---|
| `flashcard-extract` | `supabase/functions/flashcard-extract/` | `supabase/functions/_shared/flashcards/` |
| `flashcard-answer-check` | `supabase/functions/flashcard-answer-check/` | `supabase/functions/_shared/flashcards/` |

- Command: `supabase functions deploy <name> --project-ref urklkrwevjtlfbwnipjn`.
- `verify_jwt`: true, as on TEST.
- `ANTHROPIC_API_KEY` is Mide's to set as an edge-function secret. Without it:
  - the model path answers `no_api_key`;
  - table and Q:/A: extraction still work;
  - answer checks stay "pending".

## What is live now

- **Backend `36f429e`** (mrbadmus---backend main). Proved by `/api/health` → `build: 36f429ea…`.
  - `current-assignment`'s `week_work` excludes decks.
  - The worksheet route refuses a deck (409 `flashcards_no_worksheet`).
  - Content edits to a deck through `PATCH /set-work` are refused. This closed a real half-write: a scope and question edit could have written MCQ question rows onto a deck before failing.
  - Feedback draft refuses a deck.
  - Every filter uses `quiz_type`, which exists on production. Production's CHECK does not allow `'flashcards'` there yet, so each filter is a proven no-op today.
- **Site**: see "Landing" below for the commit and the live byte proof. Until the migrations are applied, the Flashcards option does not appear anywhere and nothing else changes. This was proved on the real pages against a schema-less TEST (below).

## Reconciliation — each item, and how it was proved

| # | item | what was done | proof |
|---|---|---|---|
| 1 | Live results | Flashcards follow the one live-results model in `teacher-live.js` / `teacher-data.js` / `cellOf`. A finished deck is a cell the moment it is complete (on time or late). `graded=false`, so it never enters a pupil, paper or class mean or `marked_n`. An open deck is this week's work (`inWeekPaper`, `onTimeWeek`). Missing and late come only from the deadline. Last activity also counts a pupil's latest flashcard sitting, because a deck writes no submission until it is done. | `flashcard_progress_drive` 99/99 (cellOf and roster probes); the JS≡SQL proof below. |
| 2 | One rollup migration | `20260927100000`: D's v2 (live results) plus the kind split, plus last activity including `started_at` and flashcard sittings. Two things are retired: MRB-351's migration 3 (md5 `c738d1b8…`, which edited v1) and D's parked file (md5 `112d63fb…`). The rollback drops v2 only. v1 is untouched (TEST `76419b38…` = production). | `mrb348_teacher_rollup_proof.py` on TEST. Fixture mode: 104/104, plus a flashcard fixture of 51 cells and 13 assertions. That includes a flashcards-only class (mean null), sitting-only activity, an in-progress row, and week-edge papers due exactly at the window's start and end. Real classes: **1085/1085 across 3 readers, 0 mismatches, 0 excused**. Gate `teacher_rollup_equal` green on the final tree. |
| 3 | Set Work | D2's edit flow (`placeStored`, count changes at the margin, `data-sw-qid`) is main's code. The flashcards branch (`editFlash`, `flashStepValid`) sits beside it, and both share one `detailFieldsValid`. | `set_work` gate: 455 checks, only the 3 standing small-pool reds. That includes D2's edit-margin section and D3's row download. `flashcard_decks_drive` 126/126. |
| 4 | Theme | The theme run landed on main during this run. The deck library and progress page are now wired (THEME_HEAD, `theme.js`, the control). All four surfaces were measured in light and dark: the overlay, the review table, the library and the progress page. Four dark-mode defects were fixed; see Deviations. | `theme_wiring_check`: 1331 wired, 0 unwired. `contrast_audit`, full sweep over both themes and both widths: 0 failures. 8 screenshots listed below. |
| 5 | Duplicates | "Today: the all-handed-in line renders green again" was **not** on main. It is kept, once. | Exactly one copy in `teacher/today.html:300`. |

## The 12 acceptance items, re-run on the final code (TEST, real local backend)

`tools/mrb351_acceptance.py` (committed) mints its own throwaway world, signs in real roles, and calls the real SQL functions, the real `flashcard-extract` on TEST and a real local backend. Teardown is by captured id list, and residue was checked by query: 0.

| # | result | observed |
|---|---|---|
| 1 | ✅ | A 20-card deck was saved and set to two classes. csv upload → extraction job `done`, 15 pairs. Paste box → model path → `failed: no_api_key`, as designed. (Set to 10A + 8X1 rather than 10A + 10Z, because the fixture's teacher teaches that pair.) |
| 2 | ✅ | A pupil in the class reads the 20-card snapshot and the note; a pupil in neither class is refused (`not_your_homework`). **Real backend:** the bell shows New work for the deck, `week_work` excludes it, the worksheet refuses it with 409, and delete soft-deletes it and clears the bell. |
| 3 | ✅ | First sitting: made 20/20, secured 12/20, 1 sitting. A batch re-sent twice stores its events once. |
| 4 | ✅ | A second review sitting, genuinely 60 minutes later (server timestamps backdated), secures the rest: Done, on time; the ordinary submission is written (20/20, complete). |
| 5 | ✅ | 20 cards rated fast → Rushed is flagged and the work still completes. 10 × "idk" → 10 blank. |
| 6 | ✅ | Completing after the deadline → Done late (`is_late` true). A pupil who never opened it → Missing. |
| 7 | ✅ | Editing the deck (an answer changed, a card removed) leaves the set work's snapshot at 20 cards with the original answer. |
| 8 | ✅ | A colleague duplicates and reuses the shared deck (an independent copy). The pupil opens straight into review. A smuggled `answer_submitted` in review mode writes 0 rows. |
| 9 | ✅ | MCQ unchanged: the full gate sweep on the final tree (below). |
| 10 | ✅ | Rollup exact: 1085/1085, 0 mismatches (above). |
| 11 | ✅ | `deno test`: 21/21. Recorded corpus 133/133 = 100%; the negative control still fails. |
| 12 | ✅ | `tools/mrb351_rls_matrix.py`: 9 identities × 8 tables = 72 cells, plus the `teacher-uploads` bucket, plus 6 write probes: **0 unexpected**. Every direct pupil write is refused; `flashcard_record` for another pupil's work is refused; a teacher setting to a class they don't teach is refused; a smuggled review answer is ignored. |

## The no-schema proof (production's shape, on real pages)

`tools/mrb351_noschema_live.py` rolls nothing itself. It was run on a TEST rolled back to production's shape (no `assignments.kind`, no flashcard tables, v1 `76419b38…`). It boots the real backend, signs in a real teacher and pupil, and walks the same journey on this branch's build and on an `origin/main` build. That journey is:

- Today, timetable, classes, two class-detail pages, digest, insights and student-detail;
- the Set work sheet, with a real MCQ set through the real route;
- the pupil class page, the bell, and `student/assignment.html`.

Result: 56 checks, 55 green.

- **Request shape:** equal to main on every page, and no request names `kind`, `flashcard_mode`, `completion_rule`, `deck_id` or a flashcard table.
- **Console:** errors equal to main's on all 13 pages.
- **Capability probe:** it fires, and its 404 is cached once per browser session.
- **Feature hidden:** no "Flashcard decks" link and no Flashcards chip.
- **The one red:** the accepted deck-redirect read on the pupil assignment page (see Decisions). It is now excused by exact shape and page.

`--expect-schema` on the forward TEST gave 9/9: the probe answers 200, the link and the chip appear, and the library lists decks.

## Gates on the final tree

`prepush_gate.py --record-all` on the final tree: 31 passed, 3 skipped for a missing precondition, 1 skipped by rule, and 1 red.

- **Skipped for a precondition:** `3d_*` (no studio build) and `student_controls_drive` (needs `MRB_DRIVE_PASSWORD`, never set).
- **Skipped by rule:** `ks4_pool_drive`.
- **Red:** `set_work`, 3 of 455. These are the standing small-pool checks, overridden on the push exactly as on main's recent Set work landings.

Green includes:

- `teacher_rollup_equal`, `student_bell_drive`, `teacher_perf_budget`, `focus_audit`;
- `teacher_admin_real`, `teacher_admin_foreign_class`, `ks4_parity`;
- every flashcard drive;
- `student_behaviour`, `teacher_behaviour`, `teacher_reach`;
- all fast gates, including `theme_wiring_check` and `contrast_audit`.

Theme screenshots (not committed; in `~/tmp/mrb351-theme-shots/`): `review-table-{light,dark}.png`, `deck-library-{light,dark}.png`, `progress-page-{light,dark}.png`, `pupil-overlay-{light,dark}.png`.

## TEST housekeeping (done)

- The retired helpers `mrb351-test-session` and `mrb351-env-probe` are deleted from TEST. Both were already two-line stubs answering 410. Their evidence was the table below.
- `public.mrb351_acceptance_log` (39 rows) was saved to the session's evidence folder, then dropped. What it recorded (24 Sep): the original run's items 1–8, 10 and 12. That included Hannah's first sitting at made 20 / secured 12 / 1 sitting / 7:00 active, 141 events stored for 141 sent, 10Z's class mean 85 (88 if decks were graded), and the RLS leak found and fixed at source. All of it is superseded by the re-run above.
- TEST is left **forward** (all three migrations, v2 fingerprint `e2735f6d…`), with 0 throwaway residue. `flashcard-extract` and `flashcard-answer-check` are at v2 (hardened, below).

## Decisions I made

1. **Degrade-safety reads `quiz_type`, never `kind`.** The site and backend derive the kind from `quiz_type='flashcards'`. That column exists on production, and the `assignments_flashcard_shape` CHECK makes the derivation exact once the migrations are in. The extra flashcard columns and `flashcard_sessions` are read only when a deck row exists. On production the only new request is `quiz_type` added to an existing select, plus the capability probe below.
2. **One lazy capability probe for teachers.** It is a GET of `flashcard_decks?limit=1`, not a HEAD: postgrest-js turns a bodiless 404 into a fake 204, which is why two earlier fixes were wrong. It fails closed and waits up to 15 s for the client. A "no" is remembered only for a missing-table answer, for 10 minutes in sessionStorage; a network error, an expired session or a 5xx is "not known yet" and gets asked again. So on production each teacher tab session logs one expected 404, the same kind of expected miss as the existing v2 fallback. After the apply, a tab that already probed shows Flashcards within 10 minutes, or at once in a new tab.
3. **One accepted request difference.** The pupil assignment page asks `assignments?select=quiz_type,class_id&id=eq.<id>`, in parallel with `current-assignment`, to send a deck's link to its class page. Main never asks this. It answers 200, adds no serial wait, and nobody sees it.
4. **Kept the edge-function decision** (extraction and answer check on Supabase, not Render). No concrete problem was found. They were hardened:
   - extraction is staff only (it used to refuse only `student`, so a parent account could reach it);
   - the pupil answer is escaped inside the prompt;
   - roster-like blocks, emails and 6+-digit runs are redacted from **text** before any model call. The class-list fixture's names are proved absent; the corpus is still 133/133.
5. **The week window stays `(start, end]`.** The final audit asked for `[start, end)`. On inspection, the live page compares timestamp **strings** in two ISO formats, and in effect it uses `(start, end]`, the same as D's proven v2. The SQL keeps matching the live page. Hardening the JS to compare parsed instants is a follow-up.
6. **Backend landed first** as `36f429e`, replayed onto a backend main that had moved (`7cce2d0`) rather than force-pushed. Its unit suites were re-run there: worksheet 705, set-work 157, compose 109, feedback-draft 42, all passing.
7. The flashcard-sessions read under RLS has no HoD branch, so a HoD who does not teach a class sees "No activity yet" on the JS roster for a pupil whose only activity is a sitting, while the SQL summary shows it. This is narrow. Left as a note.
8. `flashcard_set_work` does not stamp `academic_week`, so the pupil's "WEEK NN" label is blank on a deck, which the page handles. Decks also ignore the school's assignment hold. Both are left for Mide.

## For Mide

- **Before you set `ANTHROPIC_API_KEY`:** text uploads are redacted, but **photos and scanned PDFs cannot be**, and they are sent to the model as they are. The upload step now says "Don't upload anything with pupils' names on it — class lists, registers or marked work. Photos and scans are sent as they are." Whether that is enough is your call.
- **Science flag:** `shared/formulae.js` renders `N2` and `F2` as N₂ / F₂ on flashcards. On a KS4 deck, "N2" can mean Newton's second law and "F2" the second filial generation. CLAUDE.md records this exact reason for keeping KS4 unwired. Rule on whether teacher decks should subscript.
- **Deck secure rule** (MRB-351 decision 4): a make-phase Got it pairs with a review Got it on the same evening. If make → review should also need the hour, that is one line in `flashcard_card_state`.

## Deviations

- Deviation: the first no-schema proof passed vacuously (the probe never fired) → found by checking that the probe count was 0 → proved the probe both ways on real pages (`--expect-schema` 9/9; no-schema, probe fires once) → a proof that cannot show a positive is not a proof.
- Deviation: my own first probe fix (read the status) was also wrong, because postgrest-js fakes a 204 for a bodiless HEAD 404 → a later stream replaced HEAD with a one-row GET and proved it live → the drive stubs now answer the way the real library does.
- Deviation: the Opus final audit's week-boundary finding was applied, then reverted → the live JS's effective rule is `(start, end]` → the SQL matches the live page (Decision 5).
- Deviation: the theme pass fixed four dark-mode contrast defects its new coverage measured for the first time. One of them, Set Work's disabled Next/Save (opacity 0.45 → a flat muted style), also changes the existing Questions path → a small visible change beyond "exactly as today", taken because it failed AA in the dark theme that is now live.
- Deviation: two parallel agents both rolled TEST forward at once → verified afterwards: no duplicate policies, triggers or overloads, one row per migration, all 15 fingerprints exact. The migrations use `drop … if exists` and re-apply cleanly.
- Deviation: agents stalled three times on the stream watchdog → the small critical fixes were done directly, and fresh agents were started for the rest.
