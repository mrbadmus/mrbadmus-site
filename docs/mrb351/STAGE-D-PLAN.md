# STAGE D PLAN — flashcards: no jumping, progress that is never lost, and a library to revise from

Planner: Fable 5.1, 29 Sep 2026. Builder: Opus. Binding; where it contradicts PUPIL-FLOW.md §1–§13, this wins.
Line numbers are `feat/sharpen-p` @ `5aa846c24` (site) unless a path says otherwise. Every claim below was read
in the file it cites; §0's numbers were MEASURED in headless Chrome against `student/class-fixture.html` in the
sharpen tree (script: this scratchpad's `measure.py`).

Reader contract: D1 = Mide's items 1, 2, 4 (one commit). D2 = item 3 (a second commit). Nothing here touches the
backend repo; every flashcard write is the RPC `flashcard_record`, and D2 adds no backend route.

---

## §0. Causes found

### Item 1 — the question box moves up when the answer box gets focus

| Fact | Where |
|---|---|
| Compact mode is keyed on FOCUS, not on a keyboard: `typing = document.activeElement === box` → `data-hw-typing="1"` | `shared/flashcard-keyboard.js:124-126` |
| Under `data-hw-typing="1"` the CSS hides everything in the strip but the headline, and forces the card to `height:max(120px,min(34% of --fc-vh, --fc-vh − 290px))!important` | `flashcard-keyboard.js:44-53` |
| `--fc-vh` is `visualViewport.height`, which on a desktop is the full window; so at 1440×900 the card goes from 352 px to 306 px and moves UP 114 px (y 313→199), the strip from 148 px to 40 px, the question text from y 364 to 234, the answer box from 680 to 515. At 1280×720: card 312→245 (y 243→129), strip 148→40. **Measured.** | measure.py, `desk1440` / `desk1280` |
| At rest the card is `flex:1 1 auto; min-height:300px` inside a body `flex:1 1 auto` of a dialog `height:min(100%,760px)`, so the card takes EVERY spare pixel: 352 px for a one-line question at 1440×900 while the answer box is 70 px. That is the "question takes so much space" half. | Design's inline styles, compiled `student/class.html` nodes 10320 / 10328 / 10332; `_CARD_FIT` `build_student_port.py:3965-3968` adds `min-height:min(300px,calc(100vh - 240px))!important` |
| Both card faces are `position:absolute;inset:0` (10334 front, 10351 back), so the stage has no content height of its own — the reason it was given `flex:1`. | compiled 10334 / 10351 |
| Every redraw re-derives compact state from `activeElement` (A10), so the jump repeats on every keystroke that redraws (`hwDraftIn` → `hwTick` when Check flips). | `flashcard-keyboard.js:152-153`, `student_rulings.py:5389-5395` |
| The phone half is by design: a 336 px keyboard leaves 508 px and the dialog is pinned to it (`flashcard-keyboard.js:98-105`). Measured at 390×844/508: dialog 760→508, card 352→173, strip 148→40. The strip collapse and the card ratio are the movement Mide sees over and above what the keyboard forces. | measure.py `phone390` |

### Item 2 — progress is only kept until the sitting closes

| Fact | Where |
|---|---|
| Every event is written to `localStorage` the moment it happens (`event()` → `save`) and flushed after 2.5 s (`FLUSH_MS`), a rating after 600 ms, a Check after 400 ms. | `shared/flashcard-homework.js:611-620, 329, 435` |
| `pagehide` → `flushAll()` → `sb.rpc(...)` — a plain fetch with NO `keepalive`; a browser may cancel it on unload. `visibilitychange` hidden → the same `flush()`. | `flashcard-homework.js:754-759, 530-533`; transport `shared/student-live.js:728-731` |
| Resume is bound to the OPEN SERVER SITTING: `open()` reads `flashcard_reviews where session_id = state.session_id`; `fresh()` throws the map away if the last rating is over 10 min old (`RESUME_MS`); no `session_id` → no read. | `flashcard-homework.js:717-729, 744-752`; `student-live.js:779-790` |
| × sends `session_finish` when anything was done (A13, `finish()`), which ends the sitting server-side (`ended_at = now`), so the next open has no `session_id` and starts at `0 of N`. S-b made a same-page reopen do the same: `if (known.ended \|\| !known.sittingOpen) start(null)`. | `flashcard-homework.js:519-522, 695-700`; `flashcard_record` sets `ended_at` on `v_finish` |
| 10 minutes of silence also closes the sitting server-side (`last_seen_at < now − 10 min` → `ended_at = last_seen_at`). | `flashcard_record`, prod body md5 `5380b3e2…` = `20260929120000_mrb351_pupil_flow.sql` |
| What IS durable on the server: one `flashcard_reviews` row per `rated` event (`card_id, rating, phase, rated_at, answer`), readable by the pupil (`flashcard_reviews_select`: `pupil_id = auth.uid()`), plus `flashcard_pupil_cards` (make-mode first answer, immutable) and `flashcard_events.answer` for review-phase text. Prod has all three columns (checked: `flashcard_events` and `flashcard_reviews` on `urklkrwevjtlfbwnipjn` carry `answer` / `answer_check`). | schema migration; prod schema query |
| A new event TYPE cannot be a pass marker without DDL: `flashcard_events_type_check` is `type = ANY('card_shown','answer_submitted','revealed','rated','session_finish','visibility')` on prod and TEST, and `flashcard_record` `continue`s on any other type (silently dropped, not an error). Extra JSON keys are dropped too — it reads named keys only. | prod/TEST constraint query; `flashcard_record` loop |
| `afterWriting` is set in three places and read nowhere. Dead. | `flashcard-homework.js:218, 241, 527` |
| Drafts (half-typed text) live only in the engine's memory (`drafts`); a reload loses them. `idkSeen`/`replayDone` are on the device (`STORE + "idk." + id`, S-c) but honoured only beside a resumed sitting. | `flashcard-homework.js:90-105, 252-263` |

### Item 4 — clicking a homework card "lifts the page"

Measured at 1440×900, 1280×720 and 390×844 on the fixture: expanding a work row (`toggleRow`, `student/class.html:661`),
opening the homework overlay and closing it leave `window.scrollY` and the row's `top` EXACTLY unchanged, with zero
scroll events — the runtime's collapse-and-restore (`shared/student-runtime.js:679-704`) nets to zero inside one
task, and the class page has `scroll-behavior:auto` (`styles.css`'s `smooth` is NOT loaded on `student/class.html`;
its three stylesheets are brand.css, student-ds.css, topbar.css). So the document does not scroll. What moves is:

| Cause | Where | Effect |
|---|---|---|
| **The dialog's entrance**: `animation:fcUp .24s both`, `@keyframes fcUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}`, on a dialog that on a phone is the whole screen (390 wide, `height:min(100%,760px)`). The scrim fades in under it (`fcIn`). student-live.js:831-844 already suppresses the replay on REBUILDS; the first open still slides. | compiled node 10320 style; `student/class.html` keyframes | the whole screen rises 14 px and fades in — "lifts the page up in a weird way", on every flashcards open. The practice deck does the same. |
| **`lockScroll`** (Stage B): `documentElement.style.overflow = body.style.overflow = "hidden"` while `state.cards \|\| state.recall`, re-applied after every draw. On a desktop with a visible scrollbar this removes ~15 px of scrollbar, the layout viewport widens, `cqw`-sized paddings and text reflow, content above the fold moves. Live page only (not on the fixture). | `shared/student-live.js:5966-5976` | a reflow on open and again on close, desktop |
| **The runtime's rebuild** empties the host (`host.textContent = ""` with `#mrb-student{min-height:100vh}`) and restores `scrollY` synchronously. Nets to zero today; it is the mechanism every other cause rides on and it costs one line to make it never clamp at all. | `student-runtime.js:677-704`; `student/class.html:56` | none measured; hardened anyway (§2.4) |
| **Question rows**: the row's button navigates (`window.location.href = w.assignmentHref`, `student_rulings.py:920-925`); `student/assignment.html` has no keyframes, no `scrollIntoView`, no `.focus()` (grep). The lift Mide sees on a question row is the row EXPANDING (same `toggleRow` → draw) plus, on the assignment page, an ordinary navigation. No additional cause found; the §2.4 fixes apply to both rows because both go through the same draw. | grep results | — |

---

## §1. Decisions (numbered; ⚑ = Mide's product call, made here so the build does not stop — he may overturn)

1. **The homework card sizes to its content.** In homework mode the stage is `flex:0 0 auto` with a JS-measured height `clamp(140px, max(front, back) content height, cap)`; cap = 46% of the dialog height on a desktop, 34% of the visual viewport under a keyboard, never more than 420 px. Reason: a one-line question does not need 352 px, and a height that depends only on content cannot change on focus. The practice deck keeps Design's `flex:1` card untouched (one component, two decks — the rule is scoped by `[data-hw="strip"]`).
2. **Compact mode exists only under a real keyboard**: `keyboardUp = innerHeight − visualViewport.height ≥ 100`. A desktop never enters it; focus changes nothing there. On a phone the only movement is the viewport pin (dialog = visual height) and the strip's non-headline lines hiding — and with decision 1 the card no longer changes ratio, so what moves is what the keyboard forces.
3. **The answer box gets the room the card gives back**: `rows="3"`, `min-height:96px` when the dialog is ≥ 700 px tall (desktop), 64 px otherwise. No other layout change.
4. **Every answer and rating is durable the moment it happens**: a `rated` / `answer_submitted` / IDK event flushes at once (`flush()`, not `flushSoon`); the device queue stays the fallback; `pagehide` and `visibilitychange:hidden` flush through a `keepalive` POST to `/rest/v1/rpc/flashcard_record` (idempotent ids make a duplicate resend harmless). Half-typed text is saved on the device per card (`STORE + "draft." + assignment`), so a reload mid-sentence keeps the words.
5. **"The current pass" is defined from the pupil's own `flashcard_reviews` rows, with no marker and no DDL.** Walk the pupil's review-phase ratings for the assignment in time order, keeping the latest rating per card. A pass ENDS at the point where (a) every card's latest rating is Got it, or (b) the pass's current round is complete (every card the round set out to ask has a rating) AND the next rating — or, at reopen, now — is ≥ 60 minutes later. The open pass = everything after the last end. Inside it, round 1 runs until every deck card has a rating; round r+1's targets are the cards not Got it when round r completed; the current round's queue = its targets without a rating in it. ⚑ **This reverses S-b**: × / reload / a dead phone / another device all land on the next card not done in the open pass. A finished-but-not-all-right pass (the Try again screen) is offered again within the hour and restarts whole after it — the hour is the secure gap, so an hour-old pass could never have paired anyway, and without a restart the eight green cards would never be asked again under `secure`. The pupil never reads "hour" or "sitting".
6. **The server sitting is untouched.** `flashcard_sessions`, the 10-minute silence, `session_finish` on × and on Done, `secure`'s two-sittings-60-minutes rule, the make+review pairing, `sittings` for the teacher — none of it moves. A pass may now span sittings; that changes no server arithmetic, because `flashcard_card_state` reads ratings per sitting per phase and never asks what a pass is.
7. **Make mode's writing pass** is reconstructed from make-phase ratings: queue = deck cards (position order) without a make rating; a card already MADE (answer stored, phone died before rating) reopens in state A with its stored answer in the box, so one Check → rate closes the hole (today's `unmade()` queue skips it forever). Then the review pass, by decision 5. `afterWriting` is deleted (dead).
8. **The IDK replay and `idkSeen` stay device-local** (S-c), now honoured beside any reconstructed pass, not only a live sitting. Another device does not replay an I-don't-know card; its own-words rating stands. Stated, accepted.
9. **Item 4: Design's `fcUp` slide is removed from the dialog** (the scrim keeps its fade), `html{scrollbar-gutter:stable}` on the class page so `lockScroll` changes no width, and `draw()` pins the host's height across the swap so the document can never clamp. ⚑ The slide is Design's motion; Mide asked for no lift.
10. ⚑ **A set enters the library when the pupil has rated every card at least once** (first pass complete), not when the teacher's rule secures it. Reason: under `secure` completion takes two sittings an hour or more apart, and revising between them is exactly what the library is for; a 12-year-old reads "all ten done" as "I have been through them all". The class page's row keeps saying what the teacher's rule says.
11. ⚑ **The answer face shows the teacher's model answer, with the pupil's own words beneath under `YOUR ANSWER`** when they wrote any (make mode: `flashcard_pupil_cards.pupil_answer`; review mode: the latest `flashcard_reviews.answer` for the card, null on older rows). Reason: the model answer is what the exam credits; the pupil's words are the memory hook; it is exactly what the homework card's back already shows (node 10351 + `hwMine`), so there is one convention, no flip-again control.
12. ⚑ **Revising in the library never counts toward secured and writes no homework row.** Flipping a card is not evidence of recall; the teacher's numbers stay honest; and no write means no pool crossing.
13. ⚑ **The entry is one button, `View your flashcards`, directly under the FLASHCARDS sidebar card** (inside `[data-bench-surface="cards"]`, after node 10207), shown only when at least one set qualifies. On a phone that card sits straight below Work (order:2 ruling); on a KS4 class the practice deck is empty and that card otherwise says only that nothing is there. Inserted by an after-draw hook (the `drawReminder` precedent), so no template, ruling or fixture text changes.
14. **The library is an overlay owned by `shared/flashcard-library.js`, appended to `document.body`** — the `set-work.js` pattern, outside the runtime that rebuilds everything. Screens: sets (newest first) → one set (tap to flip, ‹ ›, position, Shuffle). Deep links `#sets` and `#set=<assignment id>` so Back closes it.
15. **Personal names live in `flashcard_set_names` (pupil-owned, RLS), one parked migration on `feat/mrb352-migrations`; until it is applied the name is kept on the device, silently.** The row's name is the teacher's `assignments.title` until renamed; an emptied name reverts to it.
16. **Deleted and unreleased sets never reach the library**: the pupil branch of `assignments_select_merged` already requires `deleted_at IS NULL` and release, and the library filters `.is('deleted_at', null)` too. The library lists sets from the classes the pupil is CURRENTLY in (`class_members.left_at IS NULL` is what the RLS helper `auth_user_is_member_of_class` requires); a class they have left cannot be read. Stated.
17. **Pool ownership**: the library serves `assignment_flashcards` content (`question, answer`) — the homework deck, never `ks3_cards` — from exactly one read in `shared/flashcard-library.js`; `pool_ownership.py` gains that named read and refuses a second one anywhere on the site.

---

## §2. D1 — items 1, 2, 4 (one unit: build → gates → commit → push → verify live)

### 2.1 Engine — `shared/flashcard-homework.js` (hand-written)

**Delete**: `RESUME_MS`, `fresh()`, `afterWriting` (3 sites), `opts.newSitting`, the `known.ended || !known.sittingOpen` branch in `open()`.

**Add `MRBHomework.reconstruct(rows, cards, mode, now)`** — pure, exported, unit-tested. `rows` = the pupil's own
`flashcard_reviews` for the assignment ordered by `rated_at, id` (each `{card_id, rating, phase, rated_at}`);
`cards` = `state.cards`; returns:

```
{ stage: "make"|"review",
  pass:  {cardId: {rating, phase}},        // latest rating per card in the open pass (review) or writing pass (make)
  order: [cardId…],                        // first-rated order, then the rest by rank (see below)
  round: {n, targets:[cardId…], done:[cardId…]},   // n = 1 first pass; n ≥ 2 = retries (chips view)
  ended: null | "retry"                    // the round is complete and not all right, inside the hour → Try again screen
}
```

Algorithm (review stream `R`; `HOUR = 60*60*1000`):
1. If `mode === "make"` and some deck card has no make-phase rating: `stage = "make"`, `pass` = latest make rating per card, `order` = deck by `position`, `round = {1, targets: deck, done: rated}`; return.
2. Walk `R`. Keep `latest` (per card), `passStart`, `roundTargets` (initially the deck), `roundDone`. After each rating i: `roundDone += card` if card ∈ `roundTargets`. If every card's `latest` is `got_it` → boundary (`passStart = i+1`, reset all). Else if `roundDone ⊇ roundTargets`: the round is complete; if the next rating exists and `next.rated_at − this.rated_at ≥ HOUR` → boundary; else if the next rating exists → new round (`roundTargets` = cards whose `latest` ≠ `got_it`, `roundDone = {}` , n += 1) — a rating of a card outside the targets (a green-chip redo) updates `latest` and nothing else.
3. At the end: if the open pass is empty → `null` (a fresh pass: `start(null)` as today). If the current round is complete: not all right and `now − last.rated_at < HOUR` → `ended: "retry"`; ≥ HOUR → `null` (new pass). Otherwise the pass continues: `order` = cards in the order first rated in the open pass, then the remaining deck cards in `ranked()` order (computed by the engine from server `last`/`secured`, as today at `:195-202`); `round.targets` in `order` order.

**`start(resume)`** takes that object (or null). With it: `stage`, `pass`, `order`, `retries = round.n − 1`, `passIds`:
- round 1: `done = round.done` in `order` order, then `order` minus done; `idx = done.length` (so `‹ Back` reaches the done cards, as the current resume does at `:264`);
- round ≥ 2: `passIds = round.targets − round.done` in `order` order, `idx = 0`, `baseLen = passIds.length` (the chips view, exactly `retry()`'s shape at `:493-516`);
- `ended: "retry"`: `passIds` empty; call `endPass()` so the Try again screen shows (its `end.right/m` come from `pass`/`order`).
- Make writing pass: for a card with `c.made && !pass[c.id]`, `drafts[c.id] = c.mine` (decision 7).
- `idkSeen`/`replayDone` (S-c) are loaded whenever a resume object is present (drop the `RESUME_MS` age test; keep the `at` write).
- Drafts: `drafts` is loaded from `STORE + "draft." + id` in `start()` (both fresh and resumed) and saved on every `setDraft` (debounced 300 ms) and cleared for a card when it is rated. A Try again still empties the leftovers' drafts (the 13.11 deviation).

**`open(assignmentId)`**: always reads `state = t(id, queued)` first (flushing the device queue), then `Api.resumeRead(assignmentId)` (own rows, whole assignment), then `new Engine(id, state, {resume: reconstruct(rows, state.cards, state.mode, Date.now())})`. For a KNOWN engine (same page): after `t(id, [])` merges, if `known.pending.length === 0` rebuild the pass from the server exactly as a first open (another device may have moved it; the server holds everything this device did); if `pending.length > 0` (offline) keep the in-memory pass and `Api.active = known`. A known engine whose pass `end.all` is true always rebuilds (the server will answer "new pass"). The `not_your_homework` path is unchanged.

**Flush timing**: `rate()`, `check()`, `idk()` → `this.flush()` immediately (was `flushSoon(600/400/400)`); `card_shown` keeps `FLUSH_MS`. `flush()`'s in-flight guard already serialises; nothing else changes.

**Keepalive**: new `Api.transportKeepalive` (injected like `transport`). `visibility()` when hidden and the `pagehide` handler call `flushBeacon()`: if `pending.length` and `transportKeepalive` exists → send `pending.slice(0, 60)` through it and do NOT remove them from the queue (the reply is not awaited; ids are idempotent; the next `open()` resends and the server `on conflict do nothing`s). Otherwise fall back to `flush()` as today.

**`view()`** adds nothing new for D1 except that `retry` (chips) is true when `retries > 0`, which reconstruction now sets. Header comment: replace the S-b paragraph with decision 5, in the pupil's words.

### 2.2 Live wiring — `shared/student-live.js` (hand-written)

- `H.resumeRead = (assignmentId) => sb.from("flashcard_reviews").select("card_id, rating, phase, rated_at, id").eq("assignment_id", assignmentId).order("rated_at", {ascending:true}).order("id", {ascending:true})` → rows (RLS = own rows; the current largest per-pupil count on TEST is 0 and a year's worth is tens of rows). Replace `:779-790`.
- `H.transportKeepalive = (id, events) => sb.auth.getSession().then(s => fetch(C.SUPABASE_URL + "/rest/v1/rpc/flashcard_record", {method:"POST", keepalive:true, headers:{apikey, Authorization:"Bearer …", "Content-Type":"application/json", Prefer:"return=minimal"}, body: JSON.stringify({p_assignment:id, p_events:events})}))` — the shape `onSessionEnd` already uses at `:741-746`. Bodies ≤ 60 events stay well under the 64 KB keepalive budget.
- `lockScroll` (`:5966-5976`): unchanged in logic; the width change is removed by CSS (2.4).

### 2.3 Layout — `shared/flashcard-keyboard.js` (hand-written; keeps its name, header rewritten to "the homework card's size and the phone keyboard")

- `keyboardUp()` = `root.innerHeight − vv().height ≥ 100`. `typing = box focused && keyboardUp()`. Desktop never sets `data-hw-typing`.
- **Card fit, every draw and every viewport change, homework mode only** (`p.strip` exists): measure `front = 10334.scrollHeight`, `back = 10351.scrollHeight` (absolute faces measure their content regardless of the stage's height); `cap = typing ? max(120, .34*vv) : min(420, .46*dialogHeight)`; `h = clamp(140, max(front, back), cap)`; set `p.dialog.style.setProperty("--hw-card-h", h + "px")` and `data-hw-fit="1"` on the dialog. Inject CSS (mirrors `_CARD_FIT`'s specificity, both `!important`):
  `.rd[data-mode="ks3"] [data-mrb-dialog="flashcards"][data-hw-fit] [data-card-fit]{flex:0 0 auto!important;min-height:0!important;height:var(--hw-card-h)!important}` plus `[data-hw-fit] [data-hw="answer"]{min-height:64px}` and `@media (min-height:700px){[data-hw-fit][data-hw-fit] [data-hw="answer"]{min-height:96px}}`. Remove the old typing-mode card rules (`:47-49`, `:56-58`); keep the strip/body/padding compact rules for the phone; the learn state keeps `data-hw-learn` and its ANSWER-block scroll cap (`:59-60`), and under a keyboard the learn cap is `.24*vv` for the card.
- The measurement runs BEFORE student-live's text-shrink loop (`:859-871`) because this module registers its hook at load and the loop registers inside `wireHomework`; the loop then only shrinks text that still overflows at the cap. Guard against oscillation: measure with the faces' inline `font-size` cleared first.
- `reveal()`/`scrollBox()` unchanged; `restore()` unchanged.

### 2.4 Item 4 — three small edits

- `student_rulings.py` `STYLE_EDIT["class view"]`: `10320: [("animation:fcUp .24s both;", "")]` (the scrim's `fcIn` fade stays on 10319). student-live.js `:835-844` becomes a no-op for the dialog and is left in place for the scrim.
- `build_student_port.py`: the class-view emitted CSS gains `html{scrollbar-gutter:stable}` beside `_CARD_FIT` (`:4336`); `lockScroll` then removes no width. (Generated page — never hand-edit `student/class.html`.)
- `shared/student-runtime.js` `draw()` (`:677-704`): before `host.textContent = ""` set `host.style.minHeight = host.offsetHeight + "px"`; after `host.appendChild(frag)` and the scroll restore, clear it. The document can no longer clamp during a rebuild in any browser.

### 2.5 Rulings — `student_rulings.py` (generates `student/class.html`; never hand-edit it)

- Textarea (`:5686-5696`): `"rows": "3"`; drop `min-height:64px` from the inline style (the module's CSS owns it now).
- 2.4's STYLE_EDIT. Nothing else — the strip, the states, the end screens are as built.

### 2.6 SQL

**None for D1.** Decision 5 needs no marker; prod already carries `flashcard_events.answer` and `flashcard_reviews.answer/answer_check`. Note for the report: TEST's `flashcard_record` / `flashcard_card_state` bodies differ from prod's today (prod md5 `5380b3e2…` / `2ed66c5f…` = the pupil_flow migration file; TEST `8cc69d21…` / `50abdc35…`). Before the live proof the builder prints both md5s; if TEST is ahead of prod the proof still stands because nothing in D1 depends on either body beyond what prod has.

### 2.7 Degrade

- Old function bodies / no `answer` column: irrelevant — D1 reads `flashcard_reviews` rows, which every deployed body writes.
- `resumeRead` fails (RLS, network): `reconstruct` gets `null` → a fresh pass, today's behaviour; the device queue still flushes first.
- No `fetch keepalive` (old browser): `flushBeacon` falls back to `flush()`.
- Offline: answers queue on the device (`SAVED ON THIS PHONE` as today); reopening on the same device flushes them before reading; another device sees only what reached the server — stated in the report.

### 2.8 Pupil-facing strings

No new strings. Unchanged: `N of M right`, `Try again`, `Done`, `Revise flashcards one more time`, `K of N secured so far`, `SAVED ON THIS PHONE`, `Your answer`, `Now write it in your own words`, `‹ Back`, `I don't know`, `Check`. `RETIRED` lists unchanged.

### 2.9 Tests

**`flashcard_engine_test.js`** (fast gate `flashcard_engine_test`). Extend the stand-in `server()` with `S.reviews()` → rows built from its `rated` events in arrival order (`rated_at` = the event's `at`, make-phase rows only once the card is made), and set `H.resumeRead = (id) => Promise.resolve(S.reviews())` in `fresh()`. Replace test 5 and 12d; add:

17. `reconstruct` table (pure): (a) 3 rated of 5 (got, not_yet, got) → round 1, `done` 3 in rated order, `pass` counts 2 right, `ended null`; (b) 5 rated, 2 not right, last 5 min ago → `ended "retry"`, round 1 complete; (c) same but last rating 61 min ago → `null` (new pass); (d) round 2 begun 5 min after round 1 completed: targets = the 2 leftovers, one re-rated got_it → `round.n 2`, `done` 1, pass right = 4; (e) a green-chip redo inside round 2 (rating for a non-target) changes `pass` and not `round`; (f) all got_it at some point, then 1 later rating → open pass = that 1 rating, round 1; (g) make mode: 3 of 5 make ratings → `stage "make"`, `done` 3; all 5 make ratings + 0 review → review round 1 empty done; (h) a card rated twice inside round 1 (the IDK replay) counts once toward cover; (i) empty rows → `null`.
18. Reopen after × mid-pass (replaces 12d): 2 rated, `finish()`, `close()`, `open("A")` → `headline "1 of 5 right"`, `pos 3`, segments right/answered/todo/todo/todo, `canBack`; `session_finish` WAS sent (A13 kept).
19. Dead phone: `H._reset()` + `localStorage.clear()` (a new device) with the same `S` → `open("A")` lands at `pos 3` with the same headline; drafts absent.
20. Offline then reload: `S.fail = true`, answer card 3, `S.fail = false`, `H._reset()` WITHOUT clearing localStorage → `open("A")` flushes the queue first, then lands at `pos 4` with card 3 counted.
21. Try again screen survives reopen: 5 rated, 2 leftover, `open("A")` again within the hour → `phase "end"`, `end.button "retry"`, `end.line1 "3 of 5 right"`; tap `retry()` → queue of 2 in first-pass order, 3 green chips. With the stand-in clock moved 61 min → `open("A")` → `0 of 5 right`, 5 todo.
22. Mid-retry reopen: retry started, 1 of 2 redone (got_it) → reopen → chips view, `retries 1`, queue = the remaining 1, headline `4 of 5 right`.
23. All right → Done → reopen → new pass at `0 of 5 right` (and `session_finish` sent once).
24. Make mode: writing pass, 2 made+rated, card 3 made (answer_submitted sent) and not rated → reopen → card 3 in state A with its stored answer in the box; Check → rate → card 4; writing complete → review pass at `0 of 5`.
25. Flush timing: a `rated` event reaches the transport before the next macrotask (no 600 ms wait); `visibility()` hidden with `transportKeepalive` set → the keepalive stand-in receives the pending batch and `pending` is unchanged; a following `flush()` sends the same ids and the stand-in dedupes by id.
26. `draft.` persistence: `setDraft("half")`, `H._reset()`, `open("A")` → `view().draft === "half"` for that card; after rating the key is gone.
27. `RETIRED` unchanged; `afterWriting` absent from the source (string check).

**`flashcard_homework_drive.py`** (slow gate; fixture, fake transport). Add:
- **Desktop runs** at 1440×900 and 1280×720 (`mobile:false`, no fake keyboard): open the homework; record `getBoundingClientRect()` of header (10321), strip, card, question text (10340), textarea, Check; `focus()` the textarea; record again; type one character (a redraw); record; blur; record. Assert every `top` and `height` identical (±0) across all four snapshots, `data-hw-typing` never set, textarea height ≥ 96 px, card height ≤ 420 px and card height < half the dialog's; front text not clipped (`10334.scrollHeight ≤ clientHeight + 1`). Screenshot `D-desk-1440-focus`.
- **Phone runs** (390/508, 360/404) keep every existing assertion (`boxes`, learn state) and add: with the keyboard up the card's height ≤ 34% of the visual height and ≥ 120 px; with the keyboard down the card's height equals its content height (±2 px) and the strip is full height.
- **Item 4**: at 1440 and 390, scroll the page so the first work row sits mid-screen; record `scrollY`, the row's `top`, `document.documentElement.clientWidth`; click the row; open the homework via `__MRB_OPEN_HW__`; close it via ×; assert all three unchanged (±1) at each step and no `scroll` event fired (a listener installed before the click); assert the dialog's computed `animation-name` is `none` and the overlay's is `fcIn`.
- **Resume on the fixture**: rate 3 of 5, click ×, click the row again → `progress "N of 5 right"` (N = greens), `pos` card 4, `‹ Back` present; reload the page (`page.goto` again — the fake transport is re-created empty, so instead set `window.__FC_FAKE__` to replay its stored events into `reviews`) → same landing. Keep `RETIRED` and `no_retired` at every new screen.
- `gate_registry.py`: no new watches for D1 (all files already watched); update the `why` text.

**`student_behaviour.py`**: no change expected — every D1 change is behind `hwOn` or is CSS/animation. Run it; if the `fcUp` STYLE_EDIT shows up in a visible-text or control comparison it will not (animation is not text). `student_themes`, `brand_one_mark`: run.

**TEST live proof — `tools/flashcards_stage_d_live.py`** (new; imports `mrb351_acceptance`, `mrb351_pupil_flow_live` (`build/teardown/open_deck/wait_for/session_js`), `flashcard_homework_drive` (`Phone`, `STATE_JS`, `check`), `ks3_browser`). TEST only (`jwt_ref` guard); throwaway world; teardown by snapshotted ids. Review-mode deck of 10 cards. Serves the sharpen tree on 5612 with the TEST backend as `flashcards_sharpen_live.py` does. Steps, with shots to `$MRB_SHOTS/flashcards-stage-d/`:
1. 390×844 mobile, fresh profile A: open; answer 3 cards (right, wrong, right) → headline `2 of 10 right`; wait until `MRBHomework.active.pending.length === 0`; tap × → `01-closed`. Reopen via the row (`__MRB_OPEN_HW__`) → card 4, `2 of 10 right`, segments right/answered/right, `‹ Back` present → `02-reopen-card-4`. DB: `flashcard_reviews` has 3 rows; `flashcard_sessions` has 1 row, ended.
2. Answer card 4 (right); wait for `pending === 0`; **kill Chrome with SIGKILL** (`os.killpg(browser.proc.pid, SIGKILL)` via a new `Browser.kill()` helper in `ks3_browser.py`; no `pagehide`, no `beforeunload`). Start a NEW `Browser()` (fresh profile = another device) with the same pupil session → open → card 5, `3 of 10 right` → `03-other-device-card-5`.
3. In that browser: `Network.emulateNetworkConditions offline:true`; answer card 5 (right) → strip shows `SAVED ON THIS PHONE` → `04-offline-saved`; go online; `page.goto` the class page again (a reload) → the queue flushes first; open → card 6, `4 of 10 right` → `05-after-offline-reload`. DB: 5 review rows.
4. Finish cards 6–10 with 2 wrong → Try again screen `7 of 10 right` → `06-try-again`; × ; reopen → the same Try again screen → `07-try-again-again`; tap → chips, queue of 3 → `08-retry-queue`; answer 1 right; × ; reopen → chips, queue of 2, `8 of 10 right` → `09-mid-retry-reopen`. Then shift every `flashcard_reviews.rated_at` and the session's times back 61 minutes via the service role (as `mrb351_acceptance` does for the hour) → reopen → `0 of 10 right`, 10 todo → `10-new-pass-after-hour`.
5. 1440×900 (`mobile:false`), same pupil: real class page, scroll to the work list, click the flashcards row: `scrollY`, row `top`, `clientWidth` unchanged (±1); open the deck; focus the box: the six rects unchanged; `data-hw-typing` absent → `11-desk-no-jump`; × → page unchanged.
6. DB assertions (service role): `flashcard_reviews` row count = ratings made; every `answer` for a review rating present; `flashcard_sessions` count = the number of × / hour boundaries (report the number; do not assert an exact figure beyond ≥ 3); `assignment_submissions` absent (nothing secured under `secure`). Teardown.

### 2.10 D1 build order

1. `shared/flashcard-homework.js` (2.1) → `node flashcard_engine_test.js` green.
2. `shared/flashcard-keyboard.js` (2.3), `shared/student-runtime.js`, `build_student_port.py`, `student_rulings.py` (2.4, 2.5), `shared/student-live.js` (2.2).
3. `python3 build_all.py`; `flashcard_homework_drive.py` (2.9) green at four sizes; `student_behaviour`, `student_themes`, `brand_one_mark`, `pool_ownership` green.
4. `tools/flashcards_stage_d_live.py` on TEST, all 11 shots; md5s of TEST vs prod function bodies in the report.
5. PUPIL-FLOW.md §14 "Stage D as built" (D1 half); commit; push per CLAUDE.md; verify live by md5 of `student/class.html`, `student-live.js`, `flashcard-homework.js`, `flashcard-keyboard.js`, `student-runtime.js`.

---

## §3. D2 — item 3: the flashcard library

### 3.1 What a set is

One `assignments` row with `quiz_type='flashcards'` the pupil can read, plus its frozen `assignment_flashcards`
(`position, question, answer`), plus the pupil's own words per card (decision 11), plus the pupil's personal name
(3.4). A set QUALIFIES when `count(distinct card_id in the pupil's flashcard_reviews for it) === count(assignment_flashcards)`
(decision 10). Newest first = `assignments.created_at desc` (fallback `release_at`).

### 3.2 Reads (all through the pupil's Supabase client; RLS does the scoping)

On the class page after first paint (in `student-live.js`, off the critical path, after `__MRB_MOUNT__`):
- R1 `flashcard_reviews.select("assignment_id, card_id")` — own rows, no filter (RLS = `pupil_id = auth.uid()`); dedupe client-side → `ratedCards[assignment_id] = Set`.
- R2 `assignment_flashcards.select("assignment_id").in("assignment_id", ids from R1)` → counts. (The class page already does this read for the class's decks at `:2790-2795`; reuse its result for ids it covers.)
- `libraryReady = some id: ratedCards[id].size === count[id] && count[id] > 0`. Publish `window.__MRB_LIBRARY_READY__ = [ids]` and call `MRBFlashcardLibrary.offer()`.

On library open (in `shared/flashcard-library.js`):
- R3 `assignments.select("id, title, class_id, subject_id, created_at, release_at, subject:subject_id(name), class:class_id(name)").in("id", readyIds).eq("quiz_type","flashcards").is("deleted_at", null).order("created_at", {ascending:false})`.
- R4 `flashcard_set_names.select("assignment_id, name")` (own rows) — probed once; error code `42P01` / `PGRST205` → device mode (3.4).
On a set open:
- R5 **the one serving read**: `assignment_flashcards.select("id, position, question, answer").eq("assignment_id", id).order("position")`.
- R6 `flashcard_pupil_cards.select("card_id, pupil_answer").eq("assignment_id", id)` (own rows).
- R7 `flashcard_reviews.select("card_id, answer, rated_at").eq("assignment_id", id).not("answer","is",null).order("rated_at",{ascending:false})` → latest non-null per card. R6 wins over R7 for a card (make mode's first answer is the one the teacher keeps).

### 3.3 The overlay — `shared/flashcard-library.js` + `shared/flashcard-library.css` (new, hand-written; `STAMPED_DEPS` in `build_student_port.py:225-236` gains both; `student-live.js` dep list `:92-101` gains the script)

Structure: one `<div data-mrb-library role="dialog" aria-modal="true" aria-label="Your flashcards">` appended to
`document.body`, `position:fixed;inset:0;z-index:50` with the same scrim as Design's overlay (`rgba(59,42,32,.62)`,
`fcIn` fade, no slide), a 390 px-wide column (`max-width:100%; height:min(100%,760px)`) in `--pg-*` tokens with the
card in the pupil's bench tokens (`--b-*`) — the same materials as Design's flashcard component, so light/dark and the
six bench themes follow for free. Body scroll is locked the same way as `lockScroll` while open (with 2.4's
`scrollbar-gutter`), Escape closes, Tab is trapped (copy `set-work.js:1337, 1462-1484`), nothing calls `focus()`
after a state change except the dialog itself on open (`preventScroll`), and the DOM is patched in place (list built
once per load; flipping toggles an attribute).

**Screen 1 — sets** (`#sets`): header `Your flashcards` (Bricolage 700 19px, the overlay header style of 10321) ·
×. Rows (buttons, 56 px min): name (Instrument Sans 600 17px) and, on one quiet mono line, `10 CARDS` plus the class
name ONLY when the sets span more than one class. No dates, no subject words, no explanation. Empty state cannot
occur (the button exists only when a set qualifies); if the list read fails: one line `Your flashcards did not load.`
and a `Try again` button.

**Screen 2 — a set** (`#set=<id>`): header: `‹` (back to sets) · the name as a `<button data-lib="name">` (tapping
it turns it into an `<input maxlength="60">` with the current name selected; Enter or blur saves; Escape cancels;
blank → the teacher's title) · ×. Under it Design's card stage at the library's own fixed height (`clamp(220px,
46% of the column, 380px)`): front = `QUESTION` eyebrow (mono 10px, `--b-ember`) + the question (Bricolage 700,
Design's 29px stepping down to 18px with the same fit loop as `student-live.js:859-871`); back = `ANSWER` eyebrow +
the model answer (21px/1.45 600) and, when present, the `YOUR ANSWER` block exactly as node 10353/`hwMine` draw it.
Tap the card (or Space/Enter) to flip; formulae through `window.MRBFormulae` when the set's subject is chemistry
(the `hwChem` rule). Under the card one row: `‹` · `3 / 10` (mono, Design's `stackPos` style) · `›`; a second row:
`Shuffle` (outlined toggle; `aria-pressed`). Arrow keys move; the position wraps. No ratings, no writes (decision 12).
Pip row: none (the counter carries position — one representation of one fact).

Strings (complete): `Your flashcards` · `View your flashcards` (the class-page button) · `10 CARDS` (`N CARDS`) ·
`QUESTION` · `ANSWER` · `YOUR ANSWER` · `Shuffle` · `Your flashcards did not load.` · `Try again` · aria: `Close`,
`Back to your sets`, `Previous card`, `Next card`, `Rename this set`, `Flip the card`.

**The button on the class page**: `MRBFlashcardLibrary.offer()` registers an `__MRB_AFTER_DRAW__` hook that, when
`__MRB_LIBRARY_READY__` is non-empty, appends (idempotently, keyed by `data-mrb-library-open`) after node 10207 inside
`[data-bench-surface="cards"]`: `<button type="button" data-mrb-library-open data-port-action="flashcard-library"
style="margin-top:10px;width:100%;min-height:48px;border-radius:14px;border:1.5px solid var(--st-rule);
background:var(--st-paper);color:var(--st-body);font:600 15px var(--st-ui)">View your flashcards</button>`. Tapping
it sets `location.hash = "#sets"`; the module listens to `hashchange` (like `openFromHash`, `student-live.js:793-800`)
so a direct link and Back both work; closing replaces the state to drop the fragment (`:851-855`). The hook runs on
the fixture too but `__MRB_LIBRARY_READY__` is never set there, so `student_behaviour`'s text comparison sees nothing.

### 3.4 Personal names — one parked migration + rollback (branch `feat/mrb352-migrations`)

`supabase/migrations/20261001090000_mrb352_flashcard_set_names.sql`:

```sql
-- MRB-352 Stage D — a pupil's own name for a completed flashcard set (the library).
-- Pupil-owned rows only. Nothing else reads it. REVERSIBLE: rollbacks/20261001090000_…_rollback.sql
begin;

create table if not exists public.flashcard_set_names (
  pupil_id       uuid not null references public.profiles(id) on delete cascade,
  assignment_id  uuid not null references public.assignments(id) on delete cascade,
  name           text not null check (char_length(btrim(name)) between 1 and 60),
  updated_at     timestamptz not null default now(),
  primary key (pupil_id, assignment_id)
);

drop trigger if exists flashcard_set_names_touch on public.flashcard_set_names;
create trigger flashcard_set_names_touch before update on public.flashcard_set_names
  for each row execute function public.mrb351_touch_updated_at();

alter table public.flashcard_set_names enable row level security;

-- The pupil's own rows, and only for a set they can see (the assignments policy
-- decides that: released, live, a class they are in).
drop policy if exists flashcard_set_names_select on public.flashcard_set_names;
create policy flashcard_set_names_select on public.flashcard_set_names for select using (
  pupil_id = (select auth.uid())
);
drop policy if exists flashcard_set_names_insert on public.flashcard_set_names;
create policy flashcard_set_names_insert on public.flashcard_set_names for insert with check (
  pupil_id = (select auth.uid())
  and exists (select 1 from public.assignments a where a.id = flashcard_set_names.assignment_id)
);
drop policy if exists flashcard_set_names_update on public.flashcard_set_names;
create policy flashcard_set_names_update on public.flashcard_set_names for update
  using (pupil_id = (select auth.uid()))
  with check (pupil_id = (select auth.uid()));
drop policy if exists flashcard_set_names_delete on public.flashcard_set_names;
create policy flashcard_set_names_delete on public.flashcard_set_names for delete using (
  pupil_id = (select auth.uid())
);

revoke all on public.flashcard_set_names from anon;
grant select, insert, update, delete on public.flashcard_set_names to authenticated;

commit;
```

`supabase/rollbacks/20261001090000_mrb352_flashcard_set_names_rollback.sql`:

```sql
begin;
drop table if exists public.flashcard_set_names;
commit;
```

Client: upsert `{pupil_id: uid, assignment_id, name}` `onConflict: "pupil_id,assignment_id"`; blank → `delete`.
**Degrade** (decision 15): R4's probe fails with `42P01`/`PGRST205` → `deviceMode`: names in
`localStorage["mrbadmusai.fcset.v1.names"]` (`{assignment_id: name}`), no text tells the pupil; when a later load
finds the table, device names not on the server are written up once and the local key cleared. Rehearse the
migration on TEST before the live proof; production is the chat's, at merge time (CLAUDE.md).

### 3.5 Gates

- **`pool_ownership.py`**: new §1b `check_library()`: `shared/flashcard-library.js` has EXACTLY one `from("assignment_flashcards").select(…)` whose select names `question`/`answer`; `shared/student-live.js`'s `assignment_flashcards` reads name identity columns only (`assignment_id`); `server.js` and every other `shared/*.js` never read `assignment_flashcards` content; and the library file never names `ks3_cards`, `ks3_ladder_questions` or either bank. Print the new line in `main()`'s summary: `homework deck (library) ← assignment_flashcards (flashcard-library.js, one serving read)`. `watches` += the two new files.
- **`flashcard_homework_drive.py`** (fixture; fake data): a `--library` section: install `__MRB_LIBRARY_READY__ = [AID]` and a fake `sb` for R3–R7 (a small in-page stub like `__FC_FAKE__`), redraw → the button exists inside `[data-bench-surface="cards"]`, once, and survives a redraw; tap → `#sets`, list of 1 with the teacher's title and `5 CARDS`, no class name; open → front = card 1's question, tap → back = model answer + `YOUR ANSWER` when the stub has one, `›` → card 2, `‹` wraps, Shuffle reorders (assert the set of fronts is the deck and the order differs from position with the stub seeded), rename → Enter → header shows the new name, blank → title again, Escape closes, Back button (history) closes; at 390 and 1440, light and dark (`html[data-theme="dark"]`) shots `L-sets`, `L-card-front`, `L-card-back`, `L-rename`, `L-dark`. `scrollY` unchanged across open/close. `gate_registry.py`: `watches` += `shared/flashcard-library.js`, `shared/flashcard-library.css`.
- **`student_controls_drive.py`** (wired run): no change needed; the new button must report as "did something" (opens the overlay). Mention in the report if the wired sweep was run.
- **`student_themes`**: the button sits inside `[data-bench-surface="cards"]` (skipped by the sweep); the overlay is outside the mount and unwatched — the drive's dark shot is the proof. Run it anyway.
- **`gate_watches_check`**: no docs paths in any `watches`.

### 3.6 TEST live proof — extend `tools/flashcards_stage_d_live.py` with `--library`

Same world (10-card review deck), after §2.9's step 4 the set qualifies (every card rated once): reload the class
page → `View your flashcards` under the FLASHCARDS card → `12-library-button` (390) → tap → one set named with the
teacher's title, `10 CARDS` → `13-sets` → open → front/back with `YOUR ANSWER` from the real `flashcard_reviews.answer`
→ `14-card-back` → rename to `My forces set` → DB: `flashcard_set_names` row (TEST has the migration) → reload →
the name persists → `15-renamed`. Delete the set as the throwaway teacher (`DELETE /api/teacher/set-work/:id`) →
reload → the button is gone (no qualifying set) → `16-after-delete`. Device mode (no table) is proved on the
FIXTURE drive by making the stub answer `42P01` — never by DDL from a tool. 1440 shots of `13`/`14`. Teardown (add
`flashcard_set_names` by `assignment_id` to `pf.teardown`'s order, first).

### 3.7 D2 build order

1. Migration + rollback on `feat/mrb352-migrations` (rehearse on TEST: `supabase db push` or MCP with the file's exact text; md5 in the report).
2. `shared/flashcard-library.js` / `.css`; `student-live.js` R1/R2 + dep; `build_student_port.py` `STAMPED_DEPS`.
3. `pool_ownership.py`, `flashcard_homework_drive.py --library`, `gate_registry.py`.
4. `python3 build_all.py`; gates; TEST live proof 12–16; PUPIL-FLOW.md §14 (D2 half); commit; push; verify live by md5 (`flashcard-library.js`, `.css`, `student-live.js`, `class.html`).

---

## §4. Build order across D1/D2 and file-conflict notes

Two commits on `feat/sharpen-p`, D1 then D2. Files touched:

| File | D1 | D2 | Conflict risk |
|---|---|---|---|
| `shared/flashcard-homework.js` | heavy (2.1) | — | **HIGH** — the Stage A/C6 builder is amending this file now; rebase onto their latest before starting; `reconstruct` is a new pure block, `open()`/`start()` are rewrites of `:212-267, 689-731` |
| `shared/flashcard-keyboard.js` | rewrite of `:43-60, 92-132` | — | medium (C6 touched it) |
| `shared/student-live.js` | `:779-790` replaced; `H.transportKeepalive` added beside `:757` | R1/R2 after mount; dep list `:92-101` | medium — add, do not reorder |
| `student_rulings.py` | STYLE_EDIT 10320; textarea rows | — | low (two lines) |
| `build_student_port.py` | CSS rule beside `_CARD_FIT` | `STAMPED_DEPS` | low |
| `shared/student-runtime.js` | `draw()` pin | — | low; touches every generated page — run `student_behaviour`, `teacher_*` drives that watch it (`gate_registry`'s `watches` select them) |
| `shared/student-ds.css` | — (the gutter rule is emitted by the port, not here) | — | none |
| `shared/flashcard-library.js`, `.css` | — | new | none |
| `flashcard_engine_test.js`, `flashcard_homework_drive.py`, `pool_ownership.py`, `gate_registry.py` | yes | yes | low |
| `tools/flashcards_stage_d_live.py`, `ks3_browser.py` (`Browser.kill()`) | new / +1 method | +`--library` | none |
| `supabase/migrations|rollbacks/20261001090000_…` | — | on `feat/mrb352-migrations` only | none |
| `docs/mrb351/PUPIL-FLOW.md` §14 | as-built | as-built | none |

Backend repo: untouched. `API-CONTRACT.md`: untouched (no route changes; the library reads tables under RLS).
Generated pages (`student/class.html`, `student/class-fixture.html`) come from `build_all.py` — never hand-edit.
The `student-runtime.js` change invalidates the receipts of every gate watching it; budget for a longer pre-push run
(and the SSH keepalive noted in memory).

---

## §5. What Fable's review must check

1. **§0's measurements reproduce** on the sharpen tree (`measure.py`): the 114 px card move at 1440, the 148→40 strip, zero scroll events on the row click. If the row click DOES scroll on the reviewer's machine, §2.4 still covers it (the host pin) — but say so.
2. **Decision 5 is complete**: walk `reconstruct` by hand through §2.9's cases 17a–17i; especially (b)/(c) (the hour), (d)/(e) (round 2 vs a redo), (h) (the IDK double rating does not open a round), and make mode (g). Confirm no server rule changed: `flashcard_card_state`'s per-sitting-per-phase latest rating is untouched, `secure` still needs two sittings.
3. **× still sends `session_finish`** (A13) and Done still does; the teacher's `sittings` is unaffected; `onSessionEnd` still fires the answer-check batch.
4. **Keepalive correctness**: pending events are NOT removed after a beacon; the next `open()` resends them; `flashcard_record` `on conflict (id) do nothing` makes that safe; batch ≤ 60 events.
5. **Desktop never compacts**: the threshold is on `innerHeight − visualViewport.height`, not on focus; the card height depends only on content; the drive's four snapshots are byte-equal.
6. **Practice deck untouched**: every new CSS rule and the height measurement are scoped by `[data-hw="strip"]` / `data-hw-fit`; `_CARD_FIT` still governs the practice card; `student_behaviour` green.
7. **Item 4**: `fcUp` gone from the dialog, `fcIn` kept on the scrim; `scrollbar-gutter:stable` on the class page only; the runtime pin clears its inline style after the append (no permanent min-height).
8. **Library reads are pupil-safe**: R1–R7 all go through RLS as the pupil; no service role, no backend; `assignment_flashcards` content is read in exactly one place (`pool_ownership` red otherwise); deleted/unreleased sets cannot appear (the policy line quoted in decision 16).
9. **Names**: the migration's RLS lets a pupil write only `pupil_id = auth.uid()` and only for a visible assignment; `anon` revoked; rollback drops the table; device mode has no visible text; the one-shot upload happens once.
10. **No redundant text**: the button appears only when it opens something; the sets list says name + count (+ class only when it disambiguates); the card shows one counter; no helper sentences anywhere in the library.
11. **Strings** in §2.8 / §3.3 are the complete list; `RETIRED` words absent on every drive screen.
12. **The six ⚑ calls** are surfaced to Mide in the report verbatim (decisions 5, 9, 10, 11, 12, 13).

---

## §6. As built (D1) — 29 Sep 2026, Opus 5.5, `feat/sharpen-d1`

Items 1, 2 and 4 are built as §2 says, with the deviations below. Every ⚑ in §1 took the plan's default.

**Engine** (`shared/flashcard-homework.js`): `RESUME_MS`, `fresh()`, `afterWriting`, `opts.newSitting` and the S-b
branch are gone. `MRBHomework.reconstruct(rows, cards, mode, now, idk)` is pure and exported; `open()` always sends
the device queue first, then reads the pupil's own `flashcard_reviews` for the whole assignment and starts the engine
from `reconstruct`. A same-page reopen drains the queue (up to 3 sends) and, if the server now has everything,
rebuilds from the server; offline it keeps the pass in memory. `check()`, `idk()` and `rate()` flush at once;
`visibilitychange:hidden` and `pagehide` go through `flushBeacon()` → `transportKeepalive` (≤ 60 events, queue left
intact). Half-typed text is kept per card under `mrbadmusai.fchw.v1.draft.<assignment>` (300 ms debounce, written at
once on rate/Check/close/pagehide, the key removed when empty).

**Layout** (`shared/flashcard-keyboard.js`): compact mode needs `innerHeight − visualViewport.height ≥ 100`; the
homework card is `data-hw-fit` with `--hw-card-h` = its taller face's content height (faces measured by letting them go
to `height:auto` for one synchronous read), floor 140 px at rest / 120 px under a keyboard, cap
`min(420, 46% dialog)` at rest / 34% of the visual height under a keyboard (24%, floor 96, in the learn state).

**Item 4**: `fcUp` removed from node 10320 (STYLE_EDIT); `html{scrollbar-gutter:stable}` on the class view;
`draw()` pins the host's min-height across the swap and restores it after.

**Measured results** — engine test 167/167; `flashcard_homework_drive.py` all green at 390/844, 360/740, 1440/900,
1280/720 and the item-4 runs at 1440 and 390; TEST live proof `tools/flashcards_stage_d_live.py` all green (29
checks). Function bodies before the live proof: TEST `flashcard_record` `8cc69d21…`, `flashcard_card_state`
`50abdc35…`; prod `5380b3e2…` / `2ed66c5f…` — TEST is ahead, as §2.6 said, and nothing in D1 depends on the
difference.

### Deviations

- Deviation: §0 found the document does not scroll on the fixture, and it doesn't. On the LIVE page it did:
  `lockScroll` set `overflow:hidden` on BOTH html and body, and because this page's html and body are both
  viewport-tall with the content overflowing them, the body then clipped its own overflow, the document shrank to
  one screen (scrollHeight 1395 → 900) and the browser clamped `scrollY` to 0. Measured on TEST at 1440: scrollY
  316 → 0 on open and still 0 after close. That is the lift Mide saw on every homework card. → `lockScroll` now hides
  the root only (html alone, or body alone, keeps scrollY 316; both give 0 — probed all three). → The plan said
  "unchanged in logic"; the logic was the cause. The live proof's step 5 caught it and now passes; the drive gains a
  static check that the body is never set hidden.
- Deviation: the plan's live step 4 expected a reopen an hour after a MID-RETRY round to start a new pass. Decision
  5's own algorithm (step 3) only ages out a round that is COMPLETE; an unfinished round carries on however long the
  pupil is away, which is what Mide asked for ("they come back to what they've done"). → Kept the algorithm; the live
  step now proves both: an hour-old mid-retry round still shows its chips and queue of 2, then the round is finished
  (9 of 10, Try again), aged an hour again, and the reopen is a new pass at `0 of 10 right`.
- Deviation: an "I don't know" replay is rated AFTER its round's cover is complete, so the plain walk would read the
  replay as the first rating of round 2. → `reconstruct` takes this device's I-don't-know record and absorbs a
  replay's rating (card seen, rated once in the round, within the hour) into the round it belongs to (test 17h′). On
  another device, which has no record, it reads as round 2 begun — the pupil lands in the chips view one tap earlier
  than Try again would have put them. Stated, accepted.
- Deviation: dropping `RESUME_MS` would let a stale I-don't-know record from an earlier pass apply to a later one. →
  The record now carries its round number `n` and is honoured only for the same round and when written no earlier
  than 5 minutes before the open pass's first rating.
- Deviation: decision 3's 64/96 px box is keyed on a JS-set `data-hw-tall` (dialog ≥ 700 px AND no keyboard) rather
  than `@media (min-height:700px)`, because a phone is 844 tall with or without its keyboard and the media query
  cannot tell; the 360×740 drive failed on Check being pushed under a 404 px keyboard until the box went back to 64 px
  there. With `rows="3"` the box is `height:64px` when not tall, `auto` + `min-height:96px` when tall.
- Deviation: the card's floor under a keyboard is 120 px (the plan's own drive bound), not 140, so a one-line
  question gives the box the room.
- Deviation: the keyboard module runs the same shrink-to-fit loop as student-live.js right after sizing the card,
  instead of relying on hook order (the fixture has no student-live loop at all). student-live's loop then finds
  nothing to do. Inline font sizes are not cleared first: every draw rebuilds the faces, so they start at Design's
  size anyway.
- Deviation: the keepalive keeps the access token to hand (`getSession` at wiring + `onAuthStateChange`), because a
  `pagehide` cannot wait on `getSession()`'s promise; it falls back to `getSession` if none is cached.
- Deviation (adjacent defect): the teacher's note showed again on a pass reopened part-way (`!e.acted` is per visit).
  → `hwNoteOn` also needs `pos === 1 && !retry`. The drive asserts the note is gone on the reopened card 4.
- Deviation: a same-page reopen after Done still rebuilds from the server even offline-with-pending; offline it falls
  back to `start(null)`, a new pass, exactly as the server will say.
- Deviation: `scrollbar-gutter` cannot be SEEN in headless Chrome (`ks3_browser` launches with `--hide-scrollbars`);
  the drive and the live proof assert the computed `scrollbar-gutter: stable` instead, and the width assertions pass
  trivially there.

### Review corrections (Fable, GO with corrections — amended into the D1 commit)

- **Android resizes-content.** The class view's viewport meta carries `interactive-widget=resizes-content`, so
  Android Chrome shrinks the LAYOUT viewport with the keyboard and `innerHeight − visualViewport.height` read 0:
  compact mode never came on there. `keyboardUp()` now measures against the tallest layout height seen while the box
  was NOT focused (per width). Drive `run_resizes_content` (360/404, 390/336) proves compact mode, the box and Check
  inside what the keyboard leaves, and the strip back on keyboard down. A desktop still never compacts.
- `reconstruct` gates the device's I-don't-know record on the same round `n` and age as `start()` (engine 17h″).
- The dialog body (node 10328) is `overscroll-behavior:contain` (STYLE_EDIT), so a scroll that reaches its end does
  not carry on into the class page behind.
- On a tall desktop dialog (`data-hw-tall`, mouse-and-keyboard only via `@media (hover:hover) and (pointer:fine)`)
  the write block and answer box grow into the room the card gave back, up to 200px. The rect snapshots at rest,
  focused, typing and blurred are still identical (1440: box 200px; 1280: 200px). The drive asserts `data-hw-tall`
  present at 1280×720 and absent at 1366×660 (dialog 660px: box 64px).
- Accepted edges, stated: (a) ‹ Back from a card after its round's cover is complete but before an I-don't-know
  replay is rated re-rates a card already counted; on reopen the replay may then read as round 2 on another device.
  (b) Offline events that land AFTER another device has moved the pass on carry their original device times, so
  they sort into the middle of the other device's ratings and can re-cut round boundaries (a round may read as
  complete or not differently). Both only change where the chips view starts; no rating is lost and the server's
  arithmetic is untouched.
