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

## Landing (done)

- **Backend** `36f429e` on mrbadmus---backend main. `/api/health` reported `build: 36f429ea7291…` within a minute of the push.
- **Site** `78edceb11` on main, a fast-forward pushed through `hooks/pre-push`: 29 gates fresh, 24 on unchanged receipts, and `set_work` under the override above. Verified live **by bytes**: every page below and every stamped asset below, fetched from mrbadmus.com with a nonce, is byte-identical to the committed build.
  - Pages: `teacher/class-detail`, `teacher/decks`, `teacher/flashcards`, `teacher/today`, `teacher/classes`, `student/class`, `student/assignment`.
  - Assets, each md5[:8] equal to its stamp: `flashcard-decks.css?v=cb9045ef`, `flashcard-decks.js?v=3acf513a`, `flashcard-progress.css?v=abf53d2e`, `flashcard-progress.js?v=d789beed`, `set-work.css?v=0410163d`, `set-work.js?v=adc79707`, `student-ds.css?v=a95e6c87`, `student-live.js?v=79338c4d`, `teacher-admin-nav.js?v=7582ce57`, `teacher-data.js?v=8743d7e1`, `teacher-live.js?v=123910f9`, `theme.js?v=6fd6f722`.
- **Production is unchanged underneath.** Read-only, with the public anon key: `GET /rest/v1/flashcard_decks` → 404 `PGRST205`. That is exactly the answer the capability probe caches as "not switched on", so the feature stays hidden until the chat applies the migrations.
- **Migrations** parked on `origin/feat/mrb351-migrations` `e0b39085f`: one commit on main holding the six files and `supabase/MRB351-APPLY.md`, md5s as in the first table. Its push re-ran `teacher_rollup_equal` against TEST: green.

---

## Set from class (M) — 27 Sep 2026

Written for Mide and the chat. Mide could upload a deck on production but could not set it to a class. This section says what was wrong, what changed, and how each change was proved. Production credentials were not on this machine, so every live proof ran on **TEST**. Mide does the final production click in 8r/Sc1.

### Edge function — the chat deploys `flashcard-extract` to production

| file | md5 |
|---|---|
| `supabase/functions/flashcard-extract/index.ts` | `fc844d3272c9fe3a1f3c095b4ffa651d` |
| `supabase/functions/_shared/flashcards/pipeline.ts` | `fa85e30cc6cce58561a4ae62e3024264` |
| `supabase/functions/_shared/flashcards/extract_test.ts` (test only, not deployed) | `157a3a2c9fb94de3dd299eab5523fe68` |
| `supabase/functions/_shared/flashcards/redact.ts`, `redact_test.ts` | **deleted** |

`flashcard-answer-check` is unchanged, so it needs no redeploy.

### 1. The blocker: no Flashcards choice when Set work opens from a class page

**Cause.** `probeFcCapability()` in `shared/set-work.js` only asked `window.MrBadmusAdminScope`. The class page lazy-loads that module, so it is often not there yet when Set work opens. With the module missing, the sheet read "no", and the choice stayed hidden for as long as the page stayed open.

**Fix.** The sheet now gets its own answer:

- If the nav module is on the page, the sheet uses that module's cached probe, so the nav link and the sheet always agree.
- If it is not, the sheet runs the same one-row GET of `flashcard_decks` itself. It follows the same rules: it never uses `head:true`, it treats only a missing table as "no", and it uses the same sessionStorage key for a "no".
- If the answer is unknown, the sheet asks again while it is open. When an answer arrives, only the type choice is redrawn (`syncTypeChoice`), so the scroll position is kept.

**Proof.**
- `tools/mrb351_set_from_class_live.py` on TEST reproduced production's condition: `MrBadmusAdminScope` was removed before pressing the class page's own Set work button. The choice appeared **0.3 s** after the press, from the sheet's own probe.
- Stubbed drive `flashcard_decks_drive` §5c: the same case passes, and Flashcards goes to Deck while Questions goes back to Classes.

### 2. Questions and Flashcards side by side, at the top of the sheet

The type choice is now its own block, `[data-sw=type]`. It is the first child of the sheet body, above every panel. It shows on the step the sheet opens on and on the step after (Topic or Deck), for new sets only. The two chips are equal, full-size options, using the same chip style as the Tier and Subject chips.

- **Choosing Flashcards** goes straight to the Deck step when a class is already ticked (always true from a class page). With no class ticked yet, the sheet stays on Classes, and Next goes to Deck.
- **Choosing Questions** returns to the Classes step, which is where the Questions flow starts. The Questions flow itself is unchanged.

**Proof.** Live TEST: "it is the first thing on the sheet", and choosing Flashcards goes straight to Deck. Drive checks that the chips are equal width (±1 px). Screenshot `01-class-setwork-type-1280.png`.

### 2b. A wider sheet

From 1100 px wide, the sheet is `min(88vw, 1400px)`: **1126 px at 1280, 1267 px at 1440, and 1400 px at 1920**. The height is unchanged.

- The class list and the topic tree go two columns.
- Chip rows stay on one line.
- The question list on the Detail step stays one column.

Below 1100 px nothing changes, and phones stay exactly as they were (390 px wide).

**Proof.** Live TEST at 1280, 1440, 1920 and 390, in light and dark: all 8 combinations have no sideways scroll. Screenshots are `10-sheet-*` and `11-sheet-topic-*`.

### 3. "Set to a class" in the deck library

Every ready deck with cards now has a **Set to a class** button (the primary style). It opens the same Set work sheet on Flashcards, with that deck chosen, on the Classes step. The deck is already chosen, so Next goes straight to Detail; Back still leads to the Deck step if the teacher wants a different deck. The page has no compiled class list, so the button reads the teacher's own classes once (`loadTeacherClasses(null, {metrics:false})`) and passes them to `MRBSetWork.open({deck, classes})`. The colleague toggle now reads **"Share with colleagues"** / **"Stop sharing with colleagues"**.

**Proof.** Live TEST: the library row opens the sheet on Flashcards, the teacher's class is listed, Next goes straight to Detail, and the save is confirmed by a service-role read. Screenshots `07`–`09`. The stubbed drive checks the exact `flashcard_set_work` payload.

### 4. Upload friction removed

- The upload warning is deleted.
- The pre-model redaction is deleted: `redact.ts` is gone, and `pipeline.ts` now sends text straight to the model.
- Staff-only access and the answer-check escaping are untouched.
- The "no names leaked" test is replaced by two tests. Both prove that `300 000 000 m/s` and `31536000` survive extraction exactly: one goes through the model call, the other through the no-model table path.
- **Addition beyond the brief:** the cached-upload reply now carries the deck's `subject`, so item 5 can draw its title correctly.

**Proof.** `deno test` in `_shared/flashcards`: 14 passed, 0 failed.

### 5. Formula subscripts only on Chemistry decks

Everywhere else, flashcard text is shown exactly as typed:

- **Deck component:** `draw` and `hasFormula` take the deck's subject. The editor's preview follows the subject chips.
- **Set work:** the deck summary title.
- **Teacher progress page:** one read of `assignments → subjects(name)`.
- **Pupil overlay:** the runtime's `fx` node draws plain text when the card carries `plain`. `hwVals` sets `plain` unless the assignment's subject is Chemistry. The page gets each assignment's subject from `window.__MRB_FC_SUBJECT__`, built from the work list's `subject_name`. That name comes from `flashcard_set_work`'s `subject_id`, which it takes from the deck's own subject; an untagged deck gets "Science".

**Proof.**
- `flashcard_decks_drive`: an untagged deck shows no subscript, and Chemistry does.
- `flashcard_homework_drive` and `flashcard_progress_drive` pass, with Chemistry data.
- `student_behaviour` is unchanged.

### Live TEST proof

`tools/mrb351_set_from_class_live.py` scored **27/27**. It used the throwaway world from `mrb331_fixture`, a real backend at `origin/main` 36f429e, and the built site. The pupil saw the deck in the work list, and the overlay opened on card 1 of 10. Teardown deleted rows by captured ids only, and a fresh query found **zero residue**. Screenshots are in `$MRB_SHOTS/set-from-class/`.

### Decisions I made

- **The Today page:** it has no Set work button, by an existing ruling (`teacher/today.html:645`), so "from Today" had no entry point to change. The type choice lives in the one sheet, so every entry point gets it: class page, Classes screen and deck library.
- **The probe:** I chose "run the same GET itself" over "load `teacher-admin-nav.js`". Loading that module would boot its nav injection on the class page as a side effect.
- **"Returns to the normal flow"** is read as going back to the Classes step, the start of the Questions flow.
- **TEST uses the fixture's class** (8a/Sc1), because 8r/Sc1 exists only on production.
- **Pupil subject:** comes from the work list's `subject_name`, not from a new read or any database change.

### Landing (Set from class)

- **Commit:** main `3953495f4`, pushed 28 Sep 2026 about 00:30.
- **Live check:** `class-detail`, `decks` and `student/class` on mrbadmus.com carry the committed stamps (`set-work.js?v=2ed11396`, `set-work.css?v=91d649e0`, `flashcard-decks.js?v=2610cf68`, `student-runtime.js?v=262db1e1`, `student-live.js?v=7ef9b8c5`). All seven changed assets match the committed build's md5 byte for byte, including `flashcard-progress.js?v=66f7cf7d` and `flashcard-decks.css?v=3da3c46d`.
- **Gates** (affected only, `--record-all`):
  - Every run gate is green, apart from the two overrides below.
  - Skipped by rule, with nothing on this branch in their watches: `student_parity`, `flashcard_request_shape_drive`, `today_drive`, `import_year_drive`, `ks4_pool_drive`, `ks3_instrument_liveness`, `student_switches`, `seating_drive`, `assignments_hold_drive`, `class_csv_upload`, `mrb328_import_picker`, `mrb328_import_picker_real`, `teacher_rollup_equal`, `ks4_parity`.
  - Skipped for a missing precondition: `student_controls_drive` (no production credential) and `3d_*` (no studio build).
- **Standing overrides** (in the commit message):
  - `set_work`: 455 checks, 3 red. These are the standing TEST small-pool reds.
  - `figures_mirror`: `build_figures.py --mirror` reads the main backend checkout by a hard-coded path, and that checkout has no `figures.json`.
- **Production is not yet proved.** No production credentials were set, so the 8r/Sc1 journey is Mide's click:
  1. Open 8r/Sc1 → Set work.
  2. Check the Flashcards choice is at the top.
  3. Choose Flashcards and pick "(Higher) Rate of Reaction Quiz" under My decks.
  4. Next → keep the due date → Set work.
  5. As the pupil, the deck is in the work list; pressing it opens the cards.
- **The edge function (item 4)** is committed but not deployed. The chat deploys `flashcard-extract` using the md5s above. Until then, production still redacts uploads and still returns the cached-upload reply without `subject`; the page copes with both.
