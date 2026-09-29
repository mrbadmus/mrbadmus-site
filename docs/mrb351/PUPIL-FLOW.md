# PUPIL-FLOW — Stage A plan (flashcard sitting, pupil side)

Phone run, 28 Sep 2026. Plan by Fable 5.1; reviewed by Fable 5.1 (see §11);
built by Opus 5.5. Updated to what was built at the end of the run (§12).

Written for the builder (implement exactly this) and for Mide (read it straight
through). Every claim about today's behaviour cites the file and line it came
from, as of `origin/main` when the run began.

## 0. What is wrong today, and why (grounded)

| Mide saw | Cause in code |
|---|---|
| "0 of 10 secured" never moves | `shared/flashcard-homework.js:236-250` — the headline is `secured` (server-computed), and under rule `secure` a card is secured only by `got_it` in two sittings 60 min apart (`flashcard_card_state`, functions migration lines 381-419). Nothing counts what happened *this* sitting. |
| End screen "00 / 10 SECURED · FOR NOW · Go again" | `student_rulings.py:5430-5432` (`hwBig`, `hwPanelEyebrow`), panel markup `5570-5592`. |
| No Back | The engine has no previous-card path: `rate()` at `flashcard-homework.js:176-204` always advances; the review queue is `shift()`ed away. |
| Keyboard covers the box | Overlay is `position:fixed;inset:0`, dialog `height:min(100%,760px)`, body `flex:1`, card `min-height:300px`, faces `position:absolute;inset:0` (rulings `student_rulings.py:5536-5554`). iOS Safari and Android Chrome (108+) shrink only `visualViewport`, not the layout viewport, so the fixed dialog keeps its height and the textarea sits under the keyboard. Nothing listens to `visualViewport`. |
| "Get every card right once more, later on" | Literal at `flashcard-homework.js:241`. |
| Nobody types in review | `check()` refuses unless phase is make (`:155`); review uses `flip()` (`:166-174`) — Reveal with nothing typed. |

## 1. Decisions (binding for the builder; Mide may overturn any)

1. **A sitting is one pass through all N cards.** Wrong cards do not loop round within a sitting. The next sitting starts with the cards not yet secured (existing `rank()` order, `flashcard-homework.js:112-124`, kept). Reason: "3 of 10 right" then stays honest and a sitting always ends.
2. **Headline = right this sitting, out of N**: `3 of 10 right`. "Right" = the card's current rating this sitting is Got it (auto-accepted or tapped). Back + re-rate moves it up or down.
3. **One word for the second fact: "secured"**, in both rules. Under rule `quick` the SQL already returns `known` as `secured` (`flashcard_card_state` last select), so no wording fork.
4. **Reveal only after a real answer or "I don't know".** "I don't know" reveals the model answer and rates Not yet automatically.
5. **Auto-rate with override, one tap per card.** Verdict pre-selects a rating; Next accepts it; tapping a different rating advances with that rating instead.
6. **Model check timeout 4 s.** After that (or when the key is missing / function not deployed) the chip reads "Compare it yourself", no pre-selection, the pupil taps a rating as today. A verdict landing after 4 s is ignored.
7. **Remove "Finish for now" and the pip row in homework mode.** × ends the sitting (already: `student_rulings.py:5372-5376`); the bar replaces the pips. The practice deck keeps both.
8. **Make mode = two passes in the first sitting**: the writing pass, an end screen, then the review pass (button on that end screen starts it). Server already pairs a make `got_it` with any later review `got_it` (functions lines 397-399), so cards secure during that second pass and the number moves.
9. **No schema change is required to ship Stage A.** One function-only migration is parked (see §8) to make replaced ratings count correctly and to keep review-phase typed answers. The site needs no feature detection for it.
10. Helper line "Revise flashcards one more time" shows only in the review pass, only while `secured < N`, and hides while typing (compact mode).

## 2. The sitting, card by card (both modes)

The overlay chrome is Design's (header node 10321, body 10328, card 10332/10333). Homework mode changes only what is under the header and under the card, as today (`student_rulings.py:5481-5621`).

**Header (one row, Design's):** `FLASHCARDS · 8r/Sc1` · `3 / 10` · ×. `3 / 10` is the card position (`stackPos`, `hwVals` `:5440`), unpadded in homework mode. Nothing else.

**Strip (under the header):**
- Line 1, bold: `2 of 10 right` (headline; `hwProgress`).
- Bar: fills `right / N` (`hwPct`).
- Line 2, quiet, rule `secure` only, review pass only: `4 secured`.
- Line 3, only when review pass and `secured < N`: `Revise flashcards one more time`.
- Teacher's note box: unchanged (before the first rating only, `:5427`).
- `SAVED ON THIS PHONE` offline marker: unchanged.
No "Made x / y", no "YOUR DECK IS READY" line (it becomes the make-pass end screen, §4).

**State A — question + input** (`hwWriting`): card front = question (tag `HOMEWORK`, topic = title, as today). Under the card:
- textarea, placeholder `Your answer` (aria-label same), rows 2, min-height 64px.
- Row: `Back` (outlined, only when a previous card exists this sitting) · `Check` (filled, disabled until a non-space character, as today `:152`).
- Link-style button under the row: `I don't know`.
Same in make and review phases and in both modes.

**State B — checking** (`hwChecking`): on Check, the card flips to the back at once (model answer + `YOUR ANSWER` block, `:5608-5620`) and a chip above the rating row reads `Checking…`. The local check (§3) may resolve this instantly.

**State C — revealed with verdict** (`hwRating`): chip reads one of `Right` / `Nearly` / `Not quite` / `No answer` / `Compare it yourself`. Rating row (three buttons, as today) with the suggested one filled and the other two outlined: Right→Got it, Nearly→Nearly, Not quite and No answer→Not yet. A `Next` button under the row (only when a suggestion exists). `Back` also here.

**State D — rated:** the engine records the rating and shows the next card in State A. If it was the last card, the end screen (§4).

**Back** from A or C: shows the previous card (this sitting) in State A with the pupil's earlier text prefilled. Re-checking sends fresh `answer_submitted`/`revealed`/`rated` events; the latest `rated` for that card in this sitting is the current one (§5).

Keyboard shortcuts (`student-live.js:758-771`): Space/Enter no longer reveals (typing is required); `1·2·3` rate when revealed, unchanged; swipe (`:814-831`) unchanged.

## 3. The per-card check

1. **Local check first, instantly** — a JS port of `flashcard_quick_check` (functions migration lines 34-60) placed in `shared/flashcard-homework.js` as `MRBHomework.quickCheck(pupil, model)`: normalise (lower, strip non `[a-z0-9 ]`, collapse spaces); blank or an "idk" phrase → `blank`; equal → `match`; one word: function word → `no`, else `match` if it is a word of the model answer, else `no`; multi-word → `null`. One addition: if the normalised model answer is a whole-word substring of the pupil's answer → `match`. Same list of idk phrases, copied verbatim, so SQL and JS agree.
2. **Model check when local says `null`** — `POST /functions/v1/flashcard-answer-check` with `{assignment_id, card_id, pupil_answer}` (new sync mode in `supabase/functions/flashcard-answer-check/index.ts`). The function verifies the caller as today (`:36-57`), loads that one card from `assignment_flashcards`, calls `checkWithModel([item], key)` (`_shared/flashcards/model.ts:174-197`) and returns `200 {verdict}`. No key → `200 {skipped:"no_key"}` as today `:59-60`. No pupil identifier reaches the model (same prompt builder). If a `flashcard_pupil_cards` row for (pupil, card) is still `pending` with the same text, write the verdict onto it so the end-of-sitting background run does not pay twice. The existing `{assignment_id, session_id?}` batch mode is untouched.
3. **Client timeout 4 s** (`AbortController`). Timeout, network error, `skipped`, non-JSON or an old deployment without the sync mode → `Compare it yourself`, manual rating. That is the whole degrade story for the function: feature-detect by response shape (`typeof r.verdict === "string"`).
4. Auto-rate vs pupil: §2 State C. Every rating goes through the same `rated` event; the event carries `via: "auto"|"tap"` (extra JSON key; `flashcard_record` reads named keys only, lines 523-533).

## 4. End of a sitting, and coming back

**End screen** (replaces the FOR NOW panel, `student_rulings.py:5570-5592`), three lines and one button:
- `7 of 10 right this sitting`
- `4 of 10 secured so far`
- Button: `Done` when `secured == N` (closes the overlay); otherwise `Revise flashcards one more time` (starts a new pass now; in make mode after the writing pass this is the review pass of the same sitting; otherwise it is a new sitting — the engine sends `session_finish` first, exactly as `endPass` does today `:208-215`).
No eyebrow, no big padded number, no "FOR NOW", no "Go again", no "Keep revising".

**Server-side sitting** (unchanged, functions lines 496-507, 574-577): the open `flashcard_sessions` row; ended by `session_finish` (× or the end-screen button) or 10 minutes of silence. Secured needs two review sittings 60 min apart, or make + review (lines 397-409).

**Coming back later (next day):** a new sitting; headline starts at `0 of 10 right`; `secured` carries over; queue starts with unsecured cards.

**Resume mid-sitting (reload within 10 min, `state.session_id` non-null):** on open, `student-live.js` reads the pupil's own rows `select card_id, rating, rated_at from flashcard_reviews where session_id = <id> order by rated_at` (RLS allows own rows) and hands the engine `{card_id: latest rating}`; those cards count as done this sitting and the pass continues from the first card without a rating. No migration needed. If the read fails, start a fresh pass (today's behaviour).

## 5. Events and Back

Event log stays append-only and idempotent (`flashcard-homework.js:265-307`, `flashcard_record` lines 509-533). Back produces no event of its own; re-answering sends `card_shown`, `answer_submitted` (with `answer`), `revealed`, `rated` again. **Current rating per card per sitting = latest `rated` by client time.**
- Client: engine keeps `sitting[cardId] = {rating, mine, verdict}`; `right = count(rating == got_it)`.
- Server today: `last_rating` is already latest-by-time (line 411) but `known` = any `got_it` ever (line 396) and `twice` pairs any `got_it` (397-409), so a Got it later changed to Not yet still counts. Fixed by the parked migration (§8). Until applied, production is slightly generous, never blocked.
- Make-mode `flashcard_pupil_cards` is immutable on first write (line 548): the teacher keeps the pupil's first written answer. Later re-answers exist only as events (and in `flashcard_reviews.answer` once §8 lands).

## 6. Keyboard spec

New hand-written file `shared/flashcard-keyboard.js` (loaded by `student-live.js` like `flashcard-homework.js`; add to `STAMPED_DEPS`, `build_student_port.py:225-231`).

- `vv()` returns `{height, offsetTop}` from `window.visualViewport`.
- On `visualViewport` `resize` and `scroll`, and after every draw (`window.__MRB_AFTER_DRAW__`, `student-live.js:778-788`): set on the overlay root `style.top = offsetTop px`, `style.height = height px` (instead of `inset:0`), and on the dialog `--fc-vh: <height>px` with `height: min(var(--fc-vh), 760px)`. The body node (10328) gets `overflow-y:auto` so it scrolls inside the visual viewport.
- **Compact mode** while the textarea has focus: dialog gets `data-hw-typing="1"`. In that state: strip shows line 1 only (bar, secured, helper, note hidden); card container `min-height:120px; flex:0 0 auto; max-height:34%` of `--fc-vh`; question text steps down to 18px; `I don't know` stays; header stays.
- After the state flips, `textarea.scrollIntoView({block:"nearest"})` and a second call 300 ms later (iOS animates the keyboard).
- On blur, remove the attribute; on overlay close, restore `inset:0`.
- Acceptance: with a 336 px keyboard on 390×844 (visual height 508), the question text's and the textarea's bounding boxes are both inside `[offsetTop, offsetTop+508]`, and Check is visible.

## 7. What the teacher sees (data only; Stage C draws it)

No new data needed. `flashcard_progress` returns `made / known / secured / sittings / answers{match,partial,no,blank,pending} / rushed / status`; `flashcard_pupil_detail` returns per-card `mine`, `check`, `ratings[]`. Breakdown (`shared/flashcard-progress.js`) and the live-results cell (`shared/teacher-live.js:860-866, 1128-1138`) stay consistent because both read `flashcard_card_state`. After §8, `known`/`secured` mean "current rating per sitting", and `ratings[]` may show a card rated twice in one sitting — the drawer already lists every rating in time order. The teacher word is `secured`.

## 8. Data/SQL — one parked migration, safe to ship the site first

Branch `feat/mrb351-pupil-flow-migrations`, files `supabase/migrations/20260929120000_mrb351_pupil_flow.sql` and `supabase/rollbacks/20260929120000_mrb351_pupil_flow_rollback.sql`. Function-replace plus two nullable columns; nothing the site reads changes shape.

1. `alter table flashcard_reviews add column answer text check (char_length(answer) <= 500), add column answer_check text check (answer_check in ('match','partial','no','blank','pending'))` — nullable, no backfill.
2. `flashcard_card_state`: in CTE `r`, keep only the latest rating per `(card_id, session_id)`. Everything downstream (`known`, `twice`, `last_rating`, `not_yet_n`) reads the filtered `r`.
3. `flashcard_record`: in review phase, the matching `answer_submitted` (latest before the rating, same card, same session) writes `flashcard_reviews.answer` and `answer_check = coalesce(flashcard_quick_check(answer, model), 'pending')`. Make-mode `flashcard_pupil_cards` logic unchanged.
4. Rollback: the current bodies of both functions from `origin/feat/mrb351-migrations:supabase/migrations/20260924180100_mrb351_flashcards_functions.sql` and `alter table flashcard_reviews drop column answer, drop column answer_check`.

Degrade on production until applied: the site sends the same events it will send afterwards; the server ignores the text in review phase and counts any Got it ever. No probe, no branch in the site. Edge function: the chat deploys `flashcard-answer-check` after the site; until then every model check falls back to "Compare it yourself" (§3.3).

## 9. Proof plan

Runs against **TEST** (`qeppkiswvclkkwbxmlok`).

1. **Engine tests (Node, no browser):** quickCheck table (SQL parity cases), right-this-sitting count, Back replaces a rating, resume from `{card: rating}`, make-mode two passes, end-screen text.
2. **Drive (gate `flashcard_homework_drive`, rewritten):** headless Chrome, `Emulation.setDeviceMetricsOverride` 390×844 `mobile:true`, then the keyboard simulated by re-issuing device metrics with the visual height reduced (390×508), so `visualViewport` genuinely shrinks. Assert §6 acceptance at each state; both modes; 390 and 360. Assert no text from the retired set ("FOR NOW", "Go again", "Made ", "later on", "Finish for now").
3. **Two sittings on TEST against the real database:** pupil sitting 1 in the real page; then shift that sitting back 61 minutes via service role (as `tools/mrb351_acceptance.py` did); sitting 2 → secured rises, `assignment_submissions` row appears, teacher's `flashcard_progress` shows Done. Screenshot every screen into `$MRB_SHOTS/pupil-flow/`.
4. Existing gates must stay green: `student_behaviour`, `flashcard_progress_drive`, `teacher_rollup_equal`.

## 10. Build list, in order

| # | File | Kind | Change |
|---|---|---|---|
| 1 | `shared/flashcard-homework.js` | hand-written | states A-D, `sitting` map, `right`, Back, `quickCheck`, verdict/auto-rate, `resume(map)`, one-pass sittings, make two-pass, `view()` returns the new strings |
| 2 | `shared/flashcard-keyboard.js` | new, hand-written | §6 |
| 3 | `student_rulings.py` | rulings → generates `student/class.html` | strip, controls, chip, Back/Next/I don't know, end screen, hide pips in hw mode, compact-mode attributes; **never edit `student/class.html`** |
| 4 | `build_student_port.py` | hand-written | add `flashcard-keyboard.js` to `STAMPED_DEPS` |
| 5 | `shared/student-live.js` | hand-written | load keyboard module, sync check call with 4 s timeout, resume read, drop Space-reveal |
| 6 | `supabase/functions/flashcard-answer-check/index.ts` | hand-written | sync `{card_id, pupil_answer}` mode |
| 7 | `flashcard_homework_drive.py`, `ks3_browser.py`, `gate_registry.py` | hand-written | §9.2; add the new file to `watches` |
| 8 | engine test + live two-sitting script | new | §9.1, §9.3 |
| 9 | migration + rollback on `feat/mrb351-pupil-flow-migrations` | new | §8 |
| 10 | `python3 build_all.py`, gates, commit, push | | one unit per CLAUDE.md |

## 11. Review — SENT BACK once; these amendments OVERRIDE §1–§10

A Fable 5.1 reviewer read §1–§10 as a Year 8 pupil and as Mide and sent the plan
back. Every code claim checked out except one (A9). The commander adopted all
thirteen required changes; where an amendment and an earlier section disagree,
the amendment wins.

- **A1. No `Next` button in State C.** Tapping the filled (suggested) rating is the tap that advances; tapping another rating advances with that one. Filled = chosen for you.
- **A2. Rating row visible from State B.** While `Checking…`, the three ratings are showing with none filled. A tap during checking rates and advances; a verdict landing after a tap is ignored.
- **A3. Chip words: `Right` / `Nearly` / `Wrong` / `No answer`.** No `Not quite`. When there is no verdict (timeout, no key, old function) there is **no chip at all** — `Compare it yourself` is deleted everywhere.
- **A4. `I don't know`** reveals the model answer and lands in State C with chip `No answer` and `Not yet` filled; the pupil still taps to go on.
- **A5. One counter per fact.** Homework mode blanks the header position (`stackPos: ''`). The bar becomes N per-card segments (right = green, answered not right = grey, to come = empty, current = outlined), so it carries position. Headline `2 of 10 right` stays.
- **A6. Pupil words.** The pupil never reads "sitting". End screen line 1: `7 of 10 right this time`. Line 2: `4 of 10 secured so far`. ("secured" is Mide's word and stays; flagged to him that `locked in` is the alternative.)
- **A7. The headline counts per PASS.** The client map is `pass`, emptied at each `start()`/`again()`. Make mode's review pass opens at `0 of 10 right`. The server sitting keeps every event.
- **A8. End screen honesty.** (a) Line 2 is blank until the `session_finish` flush resolves, then fills with the server number; offline → `SAVED ON THIS PHONE` in its place, never a stale number. (b) Rule `secure`, review phase (not make's second pass), and under 60 minutes since this assignment's previous sitting ended (engine stores `Date.now()` per assignment in localStorage at `session_finish`): another pass now cannot secure anything, so the button is `Done`, and the quiet line `Revise flashcards one more time` shows above it (meaning: later). Otherwise the button is `Revise flashcards one more time` while `secured < N`, `Done` when all are secured. *(Commander's refinement: the helper line stays on the `Done` case so the pupil still knows there is more to do.)*
- **A9. Keyboard CSS must beat `_CARD_FIT`.** The built card is `min(300px, calc(100vh - 240px)) !important` (`build_student_port.py:3912`), not a plain 300px. Compact-mode sizes must be `!important` under `[data-hw-typing="1"]`.
- **A10. The overlay is rebuilt on every state change** (`student-live.js:773-776`), so an attribute set on focus is wiped by the next keystroke's redraw. The keyboard module re-derives compact state in `__MRB_AFTER_DRAW__` from `document.activeElement` (and restores focus/caret if the redraw replaced the textarea), and re-applies `top`/`height` there.
- **A11. The drive must not shrink the layout viewport.** Keep device metrics at 390×844 `mobile:true` and inject a fake `window.visualViewport` (`Page.addScriptToEvaluateOnNewDocument`; `{width, height:508, offsetTop, addEventListener}`), dispatch `resize`, then assert the §6 boxes. A second run at 360×740 with height 404. Manual check on a real iPhone Safari and Android Chrome is listed for Mide in the report.
- **A12. Local check = SQL, exactly.** Drop the JS-only substring rule; SQL and JS must agree case for case, or the teacher sees `pending` for an answer the pupil was told was `Right`.
- **A13. × after one checked card must end the sitting.** Confirm `acted` counts a Check in the review phase so `hwClose` still sends `session_finish`.

Optional suggestions adopted: `‹ Back` is a small text link, not a third big button; the viewport meta gains `interactive-widget=resizes-content` for Android Chrome; the sync model check flushes `answer_submitted` first so the background batch does not pay twice. Not adopted: blanking `8r/Sc1` in the header (it is Design's chrome and tells a pupil with two classes which one).

## 12. As built

Stage A, 28 Sep 2026. Everything in §10 was built; where it differs from §1–§11 it says so here.

- **Engine** `shared/flashcard-homework.js`: states A–D, the per-PASS map (A7), `‹ Back`, `I don't know`
  (sends `answer_submitted` with the text `I don't know` and `idk: true`, so a make-mode card is made and the
  teacher sees what was pressed), `quickCheck` = SQL case for case on 74 cases (A12), model check with a 4 s
  wait, `resume(map)`, make's two passes, the A8 end screen. Every `rated` event carries `via: auto|tap`.
- **Keyboard** `shared/flashcard-keyboard.js`: §6 + A9/A10. It injects its own `!important` compact rules.
  It also puts the right text in the answer box when `‹ Back` changes the card under a box that stays on
  screen (the runtime would otherwise carry the old card's text over). Compact-mode card height is
  `max(120px, min(34% of --fc-vh, --fc-vh − 290px))`, so at 360×740 with a 404 px keyboard Check still fits.
- **Layout choices**: `‹ Back` and `I don't know` sit as small links on Check's row, not under it (one row
  less, which is what lets 404 px fit). With no verdict, no rating is filled (none of today's two-filled
  look). The strip is hidden on the end screen (its numbers would repeat the screen's — the no-redundant-text
  rule).
- **Edge function**: sync mode added (pupils only, own class, after release); batch mode untouched. NOT
  deployed anywhere: TEST still runs the old version, which answers the sync body with `{skipped:"no_key"}`
  (TEST has no ANTHROPIC_API_KEY), so the live proof covers the no-verdict fallback against the real
  deployment and the fixture drive covers a verdict.
- **Migration** (branch `feat/mrb351-pupil-flow-migrations`, parked): two deviations from §8. (1) "latest
  rating per card per sitting" is per sitting **per phase** — otherwise make mode's writing-pass Got it is
  erased by its own review pass in the same sitting and nothing secures. (2) `flashcard_events` also gains a
  nullable `answer`: the page flushes a review answer ahead of the model check, so its rating can arrive in a
  later batch, and events carried no text. Rollback restores the byte-exact deployed bodies.
- **Proof**: `flashcard_engine_test.js` (fast gate), `flashcard_homework_drive.py` (rewritten per §9.2/A11),
  `tools/mrb351_pupil_flow_live.py` (two sittings on TEST, run once with production's function bodies and once
  with the migration applied: after sitting 1, 4 of 5 secured vs 3 of 5 — the replaced Got it).
- **For Mide**: check on a real iPhone (Safari) and Android (Chrome) that the answer box stays above the
  keyboard; a headless browser cannot raise a real keyboard.

### After Stage A

- Stage B (6344e304b) retitled the overlay header "Flashcards" (was "FLASHCARDS · class") and stops the class page scrolling beneath an open overlay. The homework-mode counter stays blank (A5).
- Still for the chat: apply the migration on `feat/mrb351-pupil-flow-migrations` (md5s in `docs/experience/PHONE-REPORT.md`) and deploy `flashcard-answer-check` (md5 `94f7c9d5b4d1cefdcaf8f2bfef0079a6`). TEST currently has the migration applied.
- Still for Mide: check the answer box stays above the keyboard on a real iPhone (Safari) and Android phone (Chrome).
