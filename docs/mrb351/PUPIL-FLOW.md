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

## §13. Sharpen run (29 Sep 2026) — Stage A plan

Mide's rulings of 29 Sep 2026 (A1–A5), planned by Fable 5.1 for an Opus builder. Binding; where it
contradicts §1–§12, this section wins. Line numbers are `feat/sharpen` @ `592fb4d55`.

### 13.1 Decisions

1. **The verdict caps the rating (A1).** Cap = the suggested rating: Right→Got it, Nearly→Nearly,
   Wrong / No answer→Not yet. Ratings above the cap are drawn but disabled. Enforced in ONE place,
   `Engine.rate()` (`shared/flashcard-homework.js:300-313`) — so keys 1·2·3 (`student-live.js:807-817`)
   and swipe-right (`:860-877`) obey it with no change of their own.
2. **While `Checking…` all three ratings are disabled.** A tap before the verdict cannot be capped, so
   it waits (≤4 s, `MODEL_WAIT_MS`). This overrides §11 A2's "a tap during checking rates and advances".
3. **No verdict → no cap.** Timeout, no key, old function, non-string reply: all three enabled, none
   filled (A3 as built). Reason: blocking a pupil for our outage is wrong. ⚠️ Until the chat deploys
   `flashcard-answer-check` with a key, production has no verdict for multi-word answers, so A1 bites
   only on exact / one-word / blank answers there.
4. **"I don't know" is a learning step (A2).** Card stays on its FRONT (question visible); the model
   answer appears in a block under the card; the answer box below it, placeholder `Now write it in your
   own words`; no rating buttons, no second "I don't know"; `‹ Back` stays. Check → normal states B/C
   with cap = min(A1 cap, Nearly). The card is appended to the end of this pass ONCE (`replayed`), comes
   round as a plain card (A1 cap only). Its replay rating is its rating for the pass; M stays deck size.
   Events: the IDK press sends today's `answer_submitted` (`I don't know`, `idk:true`) + `revealed`
   (`:269-275`, kept — it is the honest record, and make mode's made card stays "I don't know" as §12
   says); the own-words Check sends a second `answer_submitted` (`own_words:true`) + `revealed`. No
   server change.
5. **The learn-state instruction is the box's placeholder**, not a label above it: one row less with the
   keyboard up, and it is still "under the model answer" as Mide asked. Mide may overturn.
6. **End of a pass (A3).** All Got it: `10 of 10 right`, then (after the flush) `4 of 10 secured so far`,
   the line `Revise flashcards one more time` if secured < N, ONE button `Done`. Otherwise: `7 of 10
   right` + ONE button `Try again` (+ Design's ×). No line 2 there, nothing waits on the server. §11 A6's
   "this time" suffix is dropped (Mide's A3 string; the strip is hidden on the end screen so there is no
   second counter to tell it from). A8b (`tooSoon`, `loadEnd/saveEnd`, `HOUR_MS`, `:74-80, :335-340`) is
   deleted: the button is never chosen by it any more.
7. **Make mode's writing pass keeps its end screen** (`N of M right` + `Revise flashcards one more
   time` → the full review pass, `again()`). It is not a review pass: A4's "only the leftovers" would
   break make+review securing, which needs a review Got it on every card.
8. **Try again = the SAME server sitting** (no `session_finish`; `retry()` not `start()`). Reasons: the
   parked migration's rule "latest rating per card per sitting per phase" (its SQL lines 44-58) then
   makes the retry's rating the card's rating, exactly as the client counts it; a new sitting started
   seconds later could never pair for `secure` anyway (≥60 min, lines 71-75); the teacher's `sittings`
   stays "times the pupil sat down"; × still ends it (`finish()`, A13) and 10 min of silence still
   closes it server-side. Production without the migration counts any Got it ever — same under either
   choice.
9. **Try again replays only what is not Got it, in the pass's own order (A4).** `order` = the first
   pass's card order, fixed for the sitting; the retry queue = `order` minus green. Headline counts the
   whole deck (green carried in = right), so a retry opens at e.g. `7 of 10 right`.
10. **The green strip IS the bar on a retry pass.** The 8 px segments become numbered chips (1…M in
    `order`), green = Got it and a button (tap → redo, a "detour"), grey = answered not right, empty = to
    come, ring = current. One representation of one fact; first pass unchanged.
11. **Redo (detour):** tappable only from state A of the queue card. The green card opens in state A with
    its earlier answer in the box; rating it replaces its rating (A1 applies) and returns to the queue
    card without advancing. Rated below Got it → grey; it does NOT join this pass's queue (a pass always
    ends; the next Try again picks it up). `‹ Back` during a detour returns to the queue card, the green
    rating untouched.
12. **A5 — a deleted set.** Every FRESH pupil read already hides it (RLS `assignments_select_merged`
    pupil branch has `deleted_at IS NULL`, `20260922040000_mrb348_rls_consolidate.sql:647`; every route
    and RPC filters — table in 13.6). What Mide saw is a page loaded BEFORE the delete: the row stays,
    the tap fails (`flashcard_record` raises `not_your_homework`), and the overlay offers a `Try again`
    that can never succeed. Fix is client-side (13.6); no SQL, no migration.

### 13.2 Engine — `shared/flashcard-homework.js`

New fields, set in `start()` (`:184-214`): `order = passIds.slice()`, `retries = 0`, `replayed = {}`,
`detour = null`, `learn = false`, `idkNow = false`. `show()` (`:220-231`) also resets `learn`, `idkNow`.

- `RANK = {not_yet:0, nearly:1, got_it:2}`. `cap()`: not revealed → n/a; `verdict === "pending"` →
  `"none"` (nothing allowed); verdict in `VERDICTS` → `SUGGEST[verdict]`, lowered to `nearly` if
  `idkNow`; verdict `null` → `idkNow ? "nearly" : null`. `allowed(r)` = cap is null, or cap ≠ "none"
  and `RANK[r] <= RANK[cap]`. `suggestion()` (`:296-298`) returns the cap only when a verdict exists
  (post-IDK with no verdict: Got it greyed, nothing filled).
- `rate(r)` (`:300`): refuse unless `allowed(r)`. Record as today, plus `cap` in `pass[id]`. Then: if
  `detour` → `detour = null; show()` (idx unchanged); else if `idkNow && !replayed[id] &&
  passIds.indexOf(id, idx+1) < 0` → `replayed[id] = true; passIds.push(id)`; then `idx += 1` → `show()`
  or `endPass()`.
- `idk()` (`:269`): only when `!revealed && !learn`. Events as today; `learn = true; idkNow = true;
  mine = IDK_TEXT; drafts[c.id] = ""`; `revealed` stays false. `check()` in learn state: `reveal(answer,
  local, {own_words:true})`; `reveal()` sets `learn = false`.
- `current()` (`:216`): `detour ? byId[detour] : …`. `canBack()` = `!ended && (detour || idx > 0)`;
  `back()`: if `detour` → `detour = null; show()`, else as today.
- `redo(id)`: allowed when `!ended && !revealed && !learn && pass[id] && pass[id].rating === "got_it"`
  → `detour = id; show()`.
- `right()` (`:324`) and segments count over `order`. Segment `current` = the detour card if any, else
  `passIds[idx]`.
- `endPass()` (`:331`): `all = right() === order.length`. Writing pass: as today. `all`: `sessionFinish()`,
  `end = {line1, all:true, settled:false}`. Else: `end = {line1, all:false}`, `flush()`, NO
  `session_finish`.
- `retry()`: requires `ended && end && !end.all && !end.writing`. `retries += 1`; delete every `pass`
  entry whose rating ≠ got_it; `replayed = {}`, `detour = null`, `passIds = order.filter(not green)`,
  `idx = 0`, `ended = false`, `end = null`, `tok += 1`, `show()`.
- `view()` (`:374-429`) adds: `learn`, `learnAnswer` (the card's answer), `allowed:{not_yet,nearly,
  got_it}`, `cap`, `retry: retries > 0`, `chips: order.map((id,i) → {id, num:i+1, state, current,
  redo: state==="right" && !revealed && !learn && !detour})`, `canRedo`. `end`: `line1 = right + " of "
  + m + " right"`; `button ∈ done | again | retry`; `line2`/`helper` only when `end.all` (line 2 after
  settled as A8a; helper when known and `secured < n`); `buttonLabel`: Done / Revise flashcards one more
  time / Try again. `headline` unchanged (`N of M right`, M = `order.length`).
- Delete `loadEnd`, `saveEnd`, `HOUR_MS`, `tooSoon`. Header comment: update to this section.

### 13.3 Rulings — `student_rulings.py` (generates `student/class.html`; never hand-edit it)

- `hwVals()` (`:5407-5478`): add `hwLearn: !!c && v.learn`, `hwLearnAnswer: v.learnAnswer`,
  `hwPlaceholder: v.learn ? 'Now write it in your own words' : 'Your answer'`, `hwIdkOn: !v.learn`,
  `hwCardKey: c ? c.id + (v.learn ? ':learn' : '') : ''` (feeds `data-hw-card`, so
  `flashcard-keyboard.js:99-104` re-syncs the box to the engine's empty draft when the learn state
  opens), `hw{NotYet,Nearly,Got}Off: !v.allowed.X`, rate styles: `hwRateStyle(tone, on, off)` adds
  `opacity:.4;cursor:default;` when off, `hwChipsOn: v.retry`, `hwChips: v.chips.map(g → {num, id, bg,
  ring, redo, ink})`, `hwEndRetry: end.button === 'retry'`,
  `hwGone: !!this.state.hwGone` (13.6). Keep `hwEndAgain` / `hwEndDone`.
- `openHomework` (`:5364-5370`): reject handler receives the error: `hwErr: true, hwGone: err &&
  err.message === 'not_your_homework'`. Add `hwRetryPass = () => engine.retry()`, `hwGoHome = () =>
  location.replace(location.pathname + location.search)`.
- Strip bar (`:5554-5562`): wrap in `if hwChipsOff` (first pass, unchanged) and add a sibling `if
  hwChipsOn`: `<div data-hw="chips" style="display:flex;flex-wrap:wrap;gap:6px">`, each chip
  `min-width:28px;height:28px;border-radius:8px;` mono 13px, number text; green ones are `<button
  data-hw="chip-redo" data-card=id aria-label="Card N, got it. Redo it">` with `"on": "g.tap"` — the
  runtime resolves `on` by name in the loop item's scope (`shared/student-runtime.js:326-327`), so
  `hwVals()` gives each chip its own closure `tap: () => engine.redo(g.id)`; others `<span>`; the
  current one keeps the inset ring.
- Write block (`:5594-5618`): before the textarea, `if hwLearn`: `<div data-hw="learn">` with eyebrow
  `ANSWER` (`_HW_MONO`, muted) and the model answer (17px/1.45, `fx` for formulae like `hwMine`,
  `max-height:30vh;overflow:auto`). Textarea `placeholder`/`aria-label` from `hwPlaceholder`,
  `data-hw-card` from `hwCardKey`. `I don't know` link wrapped in `if hwIdkOn`.
- `_hw_rate` (`:5516-5521`): add `disabled` (parts of an `Off` expr) and `aria-disabled`; rating row
  (`:5634-5641`) passes the three `Off` names.
- End panel (`:5645-5674`): add `if hwEndRetry` → `_hw_btn("hwRetryPass", "Try again", …, "retry")`.
  Line 2 / helper / offline already gate on their own flags (engine leaves them empty on the leftovers
  screen).
- Error block (`:5675-5683`): `if hwGone` → text `Your teacher has taken this work down.` + button
  `Back to my class` (`hwGoHome`, `data-hw="gone"`); `if hwErr && !hwGone` → today's two lines.

### 13.4 Keyboard / phone layout for the learn state — `shared/flashcard-keyboard.js`

`apply()` (`:80-114`) also sets `data-hw-learn="1"` on the dialog when `[data-hw="learn"]` exists.
Add to `CSS` (`:39-49`): under `[data-hw-typing="1"][data-hw-learn="1"]` the card is
`height:max(96px,min(calc(var(--fc-vh)*.24),calc(var(--fc-vh) - 380px)))!important;max-height:
max(96px,calc(var(--fc-vh)*.24))!important` and `[data-hw="learn"] > :last-child{max-height:
calc(var(--fc-vh)*.22);overflow:auto}`. Budget at 390×844 with a 336 px keyboard (visual 508): header
56 + compact strip 40 + card 122 + ANSWER block ≈66 + box 64 + Check 52 + gaps 44 ≈ 444 ≤ 508.
At 360×740 (visual 336) it does not fit; the body already scrolls (`:94`) and the box is scrolled into
view (`:116-124`), so the ANSWER block's foot, the box and Check are visible and the question is one
flick up. **Acceptance** (drive): 390/508 — question text, ANSWER block and box inside
`[offsetTop, offsetTop+height]`, Check visible; 360/336 — ANSWER block bottom edge, box inside, Check
visible. The existing `BOXES_JS` gains the learn block's box.

### 13.5 Pupil-facing strings (complete list of new/changed)

`Now write it in your own words` (placeholder) · `ANSWER` (eyebrow) · `7 of 10 right` · `10 of 10
right` · `4 of 10 secured so far` · `Revise flashcards one more time` (line, all-right screen, and the
writing-pass button) · `Done` · `Try again` · chip numbers `1`…`M` · `Your teacher has taken this work
down.` · `Back to my class`. Retired now: `right this time`. `RETIRED` lists in the test and drive gain
`"right this time"`.

### 13.6 A5 — reads and fixes

| Pupil read | Filters deleted? |
|---|---|
| work list / bench / "Revise your cards" — `shared/student-data.js:449-454` `.is('deleted_at', null)` | yes |
| class page weeks `student-live.js:2328-2330`; questions `:2548`; flashcard counts `:2681`; submissions `:3397` (ids from the filtered read + RLS) | yes |
| `/api/class/current-assignment` `server.js:1917-1966` (`auto_assignment_deleted`), `weekWorkFor` `:1674`, `readAssignmentWithQuestions` `:1248-1269`, `studentAssignment` `:8080-8089`, bell `:8837, :8977-8982` | yes |
| RPCs `student_reminders_for_viewer`, `class_stars_leaderboard_for_member`, `flashcard_record` (`deleted_at is not null → not_your_homework`, functions SQL `:508-514`) | yes |
| `student-data.js:617` (flashcard_mode), `student-live.js:4784` (kind redirect) — RLS only | add `.is("deleted_at", null)` |
| `supabase/functions/flashcard-answer-check/index.ts:57-59` batch path — no `deleted_at`/`release_at` | select both, reject as `:135-139` does (chat redeploys; report md5) |
| a page open BEFORE the delete (bfcache or a tab left open) | (a) `not_your_homework` → the taken-down state (13.3), whose button reloads the class page without the hash; (b) `window.addEventListener("pageshow", e → e.persisted && location.reload())` in `student-live.js` beside `wireHomework` |

`DELETE /api/teacher/set-work/:id` (`server.js:5871`, soft: `deleted_at`, `deleted_by`) also marks the
set's `student_notifications` read (`:5972-5976`), so the bell stops offering it. No SQL change.

### 13.7 Engine tests — add to `flashcard_engine_test.js`

10. Cap: `match` → all three enabled, Got it filled; `partial` → Got it refused (`rate("got_it")` is a
    no-op, card unchanged), Nearly filled; `no`/`blank` → only Not yet; `view().allowed` matches.
11. Checking: `modelCheck` pending → all three refused; verdict lands → cap applies; wait expires with no
    verdict → all three allowed, none filled.
12. IDK flow: `idk()` → `learn`, card not revealed, `learnAnswer` set, `canBack` true, a second `idk()`
    ignored; `check("newton")` → chip Right but cap Nearly (`allowed.got_it === false`, `suggest ===
    "nearly"`); rate Nearly → card appended once (`passIds` length M+1, `segments`/`chips` length M);
    it comes round last as a plain card (`idkNow` false, Got it allowed on Right); its replay rating is
    the pass rating; `right()` and `headline` use M. Events: `answer_submitted` ×2 for the card (`idk`
    then `own_words`).
13. IDK twice on the same card in one pass → no third showing; pass ends.
14. End screens: leftovers → `line1 "3 of 5 right"`, `button "retry"`, `line2 ""`, no `session_finish`
    sent; all right → `session_finish`, `line2` after flush, helper iff `secured < n`, `button "done"`;
    quick rule all secured → no helper. Writing pass unchanged. No `"right this time"`.
15. Try again: `retry()` → `retries 1`, headline `"3 of 5 right"` at open, `chips` = 3 green
    (`redo:true`) + 2 todo, queue = the 2 leftovers in first-pass order, `pass` keeps only green; a
    green chip `redo(id)` → detour card in state A with its earlier draft; rating it Not yet → replaces
    (headline `2 of 5`), chip grey, queue unchanged, back on the queue card; `back()` during a detour
    returns without a rating; finishing the queue all right → all-right screen; a second retry replays
    only the still-grey ones. Sessions: exactly ONE `session_finish` across pass + retries.
16. Old test 7's "hour later → Revise is the button" becomes "all right, secured < n → Done + helper";
    remove the `end.` localStorage assertion.

### 13.8 Drive — `flashcard_homework_drive.py` (both viewports)

`STATE_JS` (`:152-201`) adds `disabled` per rating button, `learn` text, `chips` (count / green / grey),
`gone`. In the make-mode run after card 1 (`:346`): a `partial` verdict shows Got it disabled (screenshot
`C-nearly-capped`); a `no` verdict (`"water"`) shows only Not yet enabled (`C-wrong-capped`); an IDK card:
`A2-learn` (keyboard up, `BOXES` incl. the learn block), `C-idk-capped` (Right verdict, Got it disabled,
Nearly filled), the card comes round again before the pass ends (`A-idk-replay`). Review-mode run: rate
two of five Not yet → `End-try-again` (`Try again`, no line 2, no `session_finish` in `__FC_FAKE__`),
click → `Retry-strip` (3 green chips, queue of 2, headline `3 of 5 right`), tap a green chip → `Redo`,
rate it Not yet → chip grey; finish → `End-all-right-done` (`Done`, line 2, ONE `session_finish`). A
`not_your_homework` rejection from the fake transport → `Gone` screen text + `Back to my class`. `RETIRED`
+= `"right this time"`. `no_retired` at every new screen.

### 13.9 TEST live proof — `tools/flashcards_sharpen_live.py` (new, from `tools/mrb351_pupil_flow_live.py`)

Reuse its `build/teardown/open_deck/wait_for` (import the module). 390×844, `mobile:true`, visual 508,
review mode, 6 cards. TEST's function returns no verdict for multi-word answers (no key), so: Right =
`newton`, Wrong = one wrong word, No answer = typed `dunno` (blank → Not yet only), IDK = the flow; for
ONE card set `window.MRBHomework.modelCheck = () => Promise.resolve("partial")` in the page (real page,
real DB, only that verdict stubbed) → Nearly cap, screenshot named `…-nearly-stubbed`. Required shots
to `$MRB_SHOTS/flashcards-sharpen/` (fallback `ks3_browser.gate_tmp()`): `01-wrong-capped`,
`02-nearly-stubbed-capped`, `03-right-open`, `04-idk-learn-keyboard`, `05-idk-checked-capped`,
`06-idk-replay`, `07-end-try-again`, `08-retry-strip`, `09-redo-green`, `10-end-done`. Assert from the
DB (service role, ids snapshotted): ONE `flashcard_sessions` row for the whole pass + retry, ended;
`flashcard_reviews` holds both ratings for a re-rated card; then delete the assignment via
`DELETE /api/teacher/set-work/:id` as the throwaway teacher WITHOUT reloading the pupil page, tap the
row → `11-taken-down`, tap `Back to my class` → the row is gone (`12-after-delete`). Tear down.

### 13.10 Build list, in order (one commit on `feat/sharpen`; the merge/push call is the commander's)

| # | File | Change |
|---|---|---|
| 1 | `shared/flashcard-homework.js` | 13.2 |
| 2 | `flashcard_engine_test.js` | 13.7 (run: `node flashcard_engine_test.js`) |
| 3 | `student_rulings.py` | 13.3 |
| 4 | `shared/flashcard-keyboard.js` | 13.4 |
| 5 | `shared/student-live.js` | `hwGone` wiring is in rulings; add `pageshow` reload, `.is("deleted_at", null)` at `:4784` |
| 6 | `shared/student-data.js:617` | `.is('deleted_at', null)` |
| 7 | `supabase/functions/flashcard-answer-check/index.ts:57-59` | batch path filters; NOT deployed here — md5 in the report |
| 8 | `flashcard_homework_drive.py` | 13.8 |
| 9 | `tools/flashcards_sharpen_live.py` | 13.9; add to `gate_registry.py` only if the existing live tool is (it is not — keep it a tool) |
| 10 | `python3 build_all.py`; gates `flashcard_engine_test`, `flashcard_homework_drive`, `student_behaviour`, `student_themes`, `brand_one_mark`; then 13.9 against TEST; §12-style as-built note appended here |

### 13.11 As built (Sharpen Stage A, 29 Sep 2026)

Everything in 13.10 was built on `feat/sharpen`, one commit. Where it differs from 13.1–13.9 it says so
under *Deviations*.

- **A1 — the verdict caps the rating.** `Engine.cap()` / `allowed()` / `rate()` in
  `shared/flashcard-homework.js`: Right → up to Got it, Nearly → up to Nearly, Wrong / No answer → Not yet
  only; `"none"` while Checking… (all three refused); no verdict → no cap. Ratings above the cap are drawn
  faded (`opacity:.4`), `disabled` and `aria-disabled="true"` (`_hw_rate` in `student_rulings.py`); keys
  1·2·3 and the swipe go through `rate()` and obey it with no change of their own (the drive presses key 3
  above the cap and nothing happens).
- **A2 — "I don't know" is a learning step.** The card stays on its question; an `ANSWER` block (the model
  answer, formula-rendered on a Chemistry deck) sits under it; the box's placeholder is `Now write it in
  your own words`; no second I don't know; ‹ Back stays. The own-words Check is capped at Nearly, and the
  card comes round once more at the end of the pass as a plain card (A1 cap only), with an empty box.
  Events: the press sends `answer_submitted` "I don't know" (`idk:true`) + `revealed`; the own words send
  `answer_submitted` (`own_words:true`) + `revealed`. No server change.
- **A3 — end of a pass.** All right: `N of N right`, then (after the flush) `K of N secured so far`, the
  line `Revise flashcards one more time` while K < N, ONE button `Done`; the sitting ends
  (`session_finish`). Otherwise `M of N right` + ONE button `Try again`, nothing waits on the server, the
  sitting stays open. Make mode's writing pass keeps `Revise flashcards one more time` → its review pass.
  `loadEnd` / `saveEnd` / `HOUR_MS` / `tooSoon` are deleted; `right this time` is retired (engine test,
  drive `RETIRED`).
- **A4 — Try again replays only the leftovers**, in the pass's own order, in the SAME server sitting. The
  bar becomes numbered chips (green = Got it and a button, grey, to come, ring = current); a green chip
  opens that card as a detour in state A with its earlier answer; re-rating replaces its rating and
  returns to the queue's card; below Got it it turns grey and waits for the next Try again. Proven on TEST:
  ONE `flashcard_sessions` row, ended, for a pass and two Try agains; `flashcard_reviews` holds
  `got_it, nearly, got_it` for the redone card.
- **A5 — a deleted set.** `not_your_homework` → `Your teacher has taken this work down.` + `Back to my
  class` (reloads the class page without the fragment; the row is gone). `.is('deleted_at', null)` on
  `student-data.js`'s `flashcard_mode` read and `student-live.js`'s kind read; `pageshow` with `persisted`
  reloads the class page; the edge function's batch path refuses a deleted or unreleased set as the sync
  path does. **`supabase/functions/flashcard-answer-check/index.ts` md5 `6cc6e1f0341c0a87c69a904b099b8acb`
  — NOT deployed anywhere.**
- **Keyboard** (`shared/flashcard-keyboard.js`): `data-hw-learn="1"` and the 13.4 rules. At 390×844 with
  the keyboard up the question, the ANSWER block, the box and Check are all on screen; at 360×740 (visual
  404, and 336) the ANSWER block's foot, the box and Check are.
- **Proof.** `node flashcard_engine_test.js` 128/128 (tests 10–16 of 13.7 plus the deleted-set cases);
  `flashcard_homework_drive.py` both phones, every screen of 13.8; `tools/flashcards_sharpen_live.py` on
  TEST, the twelve shots of 13.9 in `$MRB_SHOTS/flashcards-sharpen/`, throwaway world torn down by
  snapshotted ids.

**Deviations**

- Deviation: the end panel's Try again is `data-hw="retry-pass"`, not `retry` → the load-error screen
  already has a `data-hw="retry"` Try again → one name, one control.
- Deviation: the rulings also add `hwChipsOff` (13.3 named only `hwChipsOn`) → the first-pass bar needs
  its own condition to step aside on a retry.
- Deviation: a Try again's leftover cards open with an EMPTY box, and so does an I-don't-know replay →
  13.2 kept every draft, which put the pupil's wrong answer (or the own-words answer copied from the
  screen a minute earlier) back in the box to send again. A redo of a green card still keeps its answer,
  as 13.1.11 says.
- Deviation: reopening a deck the page already holds now asks the server first (an empty
  `flashcard_record` call), and a `not_your_homework` from any flush puts the engine in `error:"gone"`
  → 13.6 (a) covered only the first open, but a class page that has already opened the deck once holds
  its engine, so tapping the row after the delete would have started a new pass on a deleted set with no
  server call at all. Offline, the device carries on as before.
- Deviation: the keyboard module scrolls the Check row (not only the box) into view, and again when the
  visual viewport's height changes while typing → at 360 the learn state's Check sat under the keyboard.
- Deviation: the writing pass's end screen shows its button at once and no line 2 → 13.2 gives line 2 to
  the all-right screen only; nothing on that screen needs the server.
- Deviation: the batch path's release check applies to a teacher caller too (13.6 said "reject as the
  sync path does") → before release there are no pupil answers to check, so it changes nothing.
- Deviation (proof rig only): the live proof runs the TEST backend locally with
  `EXTRA_CORS_ORIGINS=http://127.0.0.1:5612`; the backend worktree was at `c7fcf31` (one commit past
  `ac03385`, "C5: pupils can always reopen their homework"), not this run's.
- In 13.9, the I-don't-know card's own words (`vector`) are decided by the local check, so no stub was
  needed there; the one stubbed verdict is card 3's Nearly, as planned.

**After the Fable review (sent back once on `529d11898`; all taken)**

- M-1: a card met with "I don't know" and not yet rated this pass reopens in the learn state (after
  ‹ Back then forward, or a reload), so its Nearly cap and its replay still apply (`idkSeen`, reset by
  Try again). Engine test 12b.
- M-2: mid-pass (first pass and Try again) the strip is the headline and the bar / chips only — no
  `N secured`, no helper line. The end screen keeps both. (This retires §1's strip lines 2–3.)
- S-a: a to-come segment / chip has a 1px `--pg-rule-strong` edge (dark mode made `--pg-band` all but
  vanish); a green chip's digit is `--pg-card` (the dark theme's `--on-accent` was white on light green).
  Drive shot `Retry-strip-dark`.
- S-b: reopening after × mid-pass starts a new pass (`!sittingOpen`), not the old one across a closed
  sitting. Engine test 12d.
- S-c: `idkSeen` and which replays are done are kept on the device (`mrbadmusai.fchw.v1.idk.<id>`), read
  only alongside a resumed sitting, so a reload mid-learn keeps the cap and the replay. Engine test 12c.
- S-d: the `pageshow` reload fires only when the fragment is `#cards=` or the overlay is open, not on
  every back-swipe.
- Left as ruled by the commander: the chip still says `Right` after I don't know while Got it is greyed;
  the Done screen's wording.

**Still for someone else**
- The chat deploys `flashcard-answer-check` (md5 above) with a key; until then A1 bites on production only
  for exact / one-word / blank answers (13.1.3).
- Mide: the answer box above the keyboard on a real iPhone (Safari) and Android (Chrome), learn state
  included.

## §14. Stage D as built — D1 (Mide's items 1, 2, 4)

Plan and deviations: `docs/mrb351/STAGE-D-PLAN.md` §2 and §6. This section only records what now overrides the
sections above. D1 and D2 were built on the pupil lane's old tip and replayed onto main after Stage C and its
re-audit fixes (30 Sep 2026); none of Stage C's changes touched a Stage D source file, so §14 and §15 hold on main
exactly as written, and every generated page was rebuilt with `build_all.py` after the replay.

- **Where a reopened deck lands (overrides S-b and §4's resume).** Worked out from the pupil's own
  `flashcard_reviews` for the whole assignment by `MRBHomework.reconstruct`, not from the server's open sitting.
  × / a reload / a phone that died / another device / offline-then-reload all land on the next card not done, with
  the pass's count. A finished round that is not all right shows Try again for an hour, then a new pass; an
  unfinished round keeps its place however long the pupil is away; all right ends the pass.
- **Nothing is lost.** Every answer and rating is sent at once; the device queue stays the fallback; a hidden or
  closing page sends the queue on a `keepalive` request and keeps it queued (ids are idempotent). Half-typed text is
  kept on the device per card.
- **The server did not change.** `flashcard_sessions`, the 10-minute silence, `session_finish` on × and Done, the
  `secure` rule, `sittings` for the teacher — untouched. No SQL.
- **The homework card sizes to its content** (140–420 px, under half the dialog) and compact mode needs a real
  keyboard: on a desktop focusing the answer box moves nothing. The answer box is three rows, 96 px on a tall dialog.
- **Nothing lifts.** The dialog's `fcUp` slide is gone (the scrim still fades); the class page keeps its scrollbar's
  room; the runtime pins the host's height across a redraw; and the scroll lock hides the root only — hiding html AND
  body clamped the live page to the top on every open.
- **Proof:** `flashcard_engine_test.js` 17–27, `flashcard_homework_drive.py` (desktop 1440/1280, phones 390/360,
  item 4 at 1440/390, fixture resume), `tools/flashcards_stage_d_live.py` on TEST (11 shots).

- **One scroll lock.** D1 and D2 found the same html+body clamp independently. `lockScroll` in `student-live.js`
  (homework overlay, practice round) and the library's `html[data-mrb-library-open]` both hide the ROOT only.

## §15. Stage D as built — D2 (Mide's item 3: "Your flashcards")

Full as-built, migration md5s and deviations: `docs/mrb351/STAGE-D2-AS-BUILT.md` (kept). What now holds:

- **The entry.** One button, `View your flashcards`, directly under the FLASHCARDS card on the class page — only
  when at least one flashcard homework has had every card rated at least once (decision 10). No qualifying set,
  no button.
- **The library** (`shared/flashcard-library.js` + `.css`, an overlay appended to `<body>`, outside the runtime):
  the sets newest first (name + `N CARDS`, the class only when sets span classes) → one card at a time, tap or
  Space/Enter to flip; the back is the model answer and, when the pupil wrote one, `YOUR ANSWER` (make mode's
  first answer wins, else the latest review answer). `‹` `›` and arrows wrap; `3 / 10` is the one position
  marker; Shuffle toggles. `#sets` / `#set=<id>` are real addresses, so Back steps set → list → class page.
- **Names.** Tap the name (a muted pencil marks it) to rename; blank or the teacher's own title reverts to the
  teacher's title. Stored in `flashcard_set_names` (pupil-owned RLS; the UPDATE check also requires a visible
  assignment) — a parked migration on `feat/mrb352-migrations`, applied on TEST only. Until production has it, names
  stay on the device, silently, and are uploaded once when the table appears.
- **Nothing counts.** Revising in the library writes no rating, event or submission (decision 12); the only write
  is the name.
- **Pool ownership.** `assignment_flashcards` content (`question, answer`) is read in exactly one place,
  `flashcard-library.js`; `pool_ownership` check 1b sweeps every `shared/*.js`, root `*.html` and the backend's
  `server.js` for a second.
- **Parked.** The qualifying read (R1) pulls every one of the pupil's `flashcard_reviews` rows on each class-page
  load (paged, capped); a per-set RPC/view needs DDL and is parked.
- **Proof:** `flashcard_homework_drive.py --library` (390 and 1440, light and dark, degrade mode via a `42P01`
  stub), `tools/flashcards_library_live.py` and `tools/flashcard_set_names_rls.py` on TEST.
