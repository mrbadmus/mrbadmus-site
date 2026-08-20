# Student assignment page — v1 handoff

**Date** 19 August 2026
**Scope** The page behind the class view's **Open the assignment** button. Fifteen multiple-choice questions, one per screen, marked on the spot.

## Files

| File | What it is |
| --- | --- |
| `MrBadmusAI Assignment.html` | Single self-contained file. Fonts, tokens, React and every state inlined. Open it offline. |
| `source/Assignment.dc.html` | Authoring source. Template + logic class. Loads the design-system bundle by relative path. |
| `source/Assignment - standalone source.dc.html` | The same source plus the bundler thumbnail. This is what compiles to the standalone file. |

One screen with three views: **Question** (`data-screen-label="Question NN"`), **Review** after handing in, and **Handed in** — the end screen. The hand-in moment is a fourth, transient view (`data-screen-label="Handing in"`, 1350ms).

---

## 1. The shape of the page

Phone, top to bottom. Everything above the question is sticky, everything below it is sticky, and the question is the only thing that scrolls.

| Band | Height at 390 | Holds |
| --- | --- | --- |
| Chrome row A | 52px | back chevron to `8r/Sc1`, the `LATE` / `HANDED IN` chip, the timer |
| Chrome row B | 45px | the marker row — every question's state, and the way to jump |
| Chrome row C | 27px | `ANSWERED 06 / 15` · `04 RIGHT` `09 LEFT` |
| Content | scrolls | topic + due line, `Question 07 of 15 · ANIMAL AND PLANT CELLS`, the question, the figure, four options |
| Action bar | 67px | **Back** · **Confirm answer** / **Next** / **Hand it in** / **Summary** |

Measured chrome total: **124px**. At desktop it is 60px — rows B and C move into a 320px rail (§6).

The two bands were split deliberately. Row B is the thing a student looks at ("how much is left"); row C is the thing they *read* ("what have I got right"). Putting the numerals inside the marker row made both harder at 21px per marker.

---

## 2. The marking moment

The single most important transition on the page, so it is specified to the value.

**A tap selects. Confirm answer marks.** Two steps, because the mark is final and a mis-tap on a 60px card should not cost a student a question. Selecting is free and reversible — tap another option as many times as you like — and the commitment is a separate, deliberate press in the thumb zone. The moment the confirm lands, the marking is immediate and total: verdict, mark and explanation, all on that screen.

While a question is unanswered and something is selected, **Confirm answer** takes the action bar's primary slot and Next demotes to a 46 × 46px chevron beside it (Back + chevron + Confirm measures 298px inside 332px of content at 360). With nothing selected the bar is Back · Next, exactly as before. Selection survives navigation and a reload — an unconfirmed draft is kept per question in `sels`, so leaving mid-thought loses nothing.

Five states, all carried by shape and mark as well as hue:

| State | Card | Key chip | Mark + word | Explanation |
| --- | --- | --- | --- | --- |
| Untouched | `--st-paper`, 1.5px `--st-rule` | outline `--st-rule-strong`, letter in `--st-caption` | none | none |
| Selected, not confirmed | `--st-paper`, **2px `--st-ink`** | filled `--st-ink`, letter `#FFFDF8` | none — no verdict has been given | none |
| Chosen, right | `--ks3-ok-tint`, 2px `--ks3-ok` | filled `--ks3-ok-text`, letter `#FFFDF8` | tick (SVG) + `RIGHT` in `--ks3-ok-text` | its own line, `--st-body` |
| Chosen, wrong | `--err-bg`, 2px `--err` | filled `--err`, letter `#FFFDF8` | rotated square + `NOT THIS ONE` in `--err` | **that distractor's** line, `--st-body` |
| The answer, unchosen | `--st-paper`, 2px `--ks3-ok` | outline 2px `--ks3-ok`, letter `--ks3-ok-text` | tick + `THE ANSWER` | its line, quieter: `--st-muted` |
| Neither | transparent, 1px `--st-rule-fact` | outline `--st-rule-fact` | none | none |

- **The explanation is attached to the option, not to the page.** It appears inside the chosen card, under the option text, indented to the text column (`grid-column: 2 / -1`) and separated by a 1px rule in the state's border colour. The teaching lands where the finger is, which is why there is no feedback panel at the foot of the screen.
- **Every wrong option has its own line.** All sixteen questions carry four strings; the one a student sees is the one written against the mistake they made. The right answer's line is shown too, so the pair reads *why not that* / *why this*.
- **The two irrelevant options recede** rather than disappear: text to `--st-faint`, border to a hairline. The eye is left with two cards, not four.
- **Motion.** The card properties are on a 220ms `transition` (background, border-colour, colour) so the recede is a settle, not a flash. The tick draws in 360ms on `stroke-dashoffset`; the key chip and the wrong-mark scale in over 300ms (`mrbMark`); the explanation fades up 6px over 340ms (`mrbNote`). All of it collapses to 1ms under `prefers-reduced-motion`.
- **Once confirmed, locked.** `cursor` drops to `default` and both `select` and `confirm` return early. Back and Next still work — they navigate, they never unlock, and there is no second confirm.

---

## 3. The marker row — fifteen markers on a 390px screen

**Solved by splitting the two jobs.** A marker row has to be *readable at a glance* and *tappable to the individual question*. At 390px, 15 touch targets cannot both be 40px wide and fit; so the glance and the tap were given different objects.

**Below 720px — the strip is one control.** Fifteen markers, `flex: 1 1 0` each with a 3px gap, sit inside a 44px-tall row: **21.3px per marker at 390**, 19.6px at 360. The row is 15 buttons, but every one of them opens the same thing: a grid sheet under the chrome. So the touch minimum is met by the row, not by the marker — there is no 21px tap target anywhere.

The sheet is a `repeat(5, 1fr)` grid of **66 × 54px** cells (at 390), each carrying its numeral *and* its mark, plus the legend and a Close. Three rows at fifteen, four at sixteen to twenty. Tapping a cell jumps and closes.

**At 720px and above — the strip is direct.** Each marker becomes its own 40px-tall button and a tap jumps straight to that question. The sheet is never needed and never shown.

**At 1024px and above — the strip is gone.** The 320px rail carries the grid permanently (52px cells) with the three readings under it, so the whole set is visible without a tap at all.

Marker vocabulary, identical in the strip, the sheet, the rail and the end screen:

| | Strip | Sheet / rail |
| --- | --- | --- |
| Right | 22px tall, `--st-ink` fill, cream tick | `--st-ink` fill, cream numeral + tick |
| Wrong | 22px tall, `--err-bg`, 1.5px `--err`, `--err` diamond | `--err-bg`, 1.5px `--err`, numeral + diamond in `--err` |
| Not yet | **10px tall**, `--st-rule-soft`, no mark | dashed `--st-rule-strong`, hollow ring |
| Current | 26px tall + `0 0 0 2px var(--st-accent)` ring | + the same accent ring |
| Held on device | the ink fill gains a 45° cream hatch | ditto |

Height is doing as much work as fill: an unanswered marker is less than half the height of an answered one, so the row reads as a filling bar even in greyscale.

**It does not assume fifteen.** Every count on screen reads `total` (`WEEK 04 · 15 QUESTIONS`, `ANSWERED 06 / 15`, `All 15 questions`, `Look through all 15`, `03 OF 15`), the strip is flex so markers simply get wider or narrower, and the sheet grid rewraps. Verified at 12, 14, 15 and 16 with the `questionCount` tweak.

---

## 4. Figures

Six of the sixteen questions carry one. The topic is diagram-light; on a diagram-heavy topic most questions would, which is what `figures = Every question` shows — the remaining ten get the **figure slot**: a dashed `--st-note-bg` box at the same height, reading `FIGURE SET WITH THE QUESTION`. The slot is the specification of the space, not a placeholder pretending to be art.

| Question | Figure | Type |
| --- | --- | --- |
| 01 | Light microscope, four labelled parts | geometry + A–D label discs |
| 05 | Two mounted slides seen down the microscope, one with trapped air | two fields of view |
| 06 | The same slide at `MAG 100` and `MAG 400` | eight cells across vs two |
| 07 | Plant cell, four labelled structures | geometry + A–D label discs |
| 12 | Four specialised cells | four silhouettes + A–D |
| 15 | One cell with a scale bar reading `0.06 mm` | measurement |

All six are inline SVG on `--st-paper`, `--st-ink` strokes, `--st-crumb-bg` / `--st-num-well` fills, `--st-accent` leader lines and label rings. **No green and no red inside a figure** — those two hues mean right and wrong on this page and nothing else. They are schematic stand-ins for the lesson's own figures; the frame, the cap and the caption row are the part that ships.

### A figure and four options on a 390px screen

They do not both fit at every combination, and the figure is what gives.

- The figure is capped at `clamp(132px, 34cqw, 232px)` — **132px at 390**, 232px from 682px up — inside a `--st-paper` frame with a caption row. Block height at 390: **184–193px**.
- `preserveAspectRatio="xMidYMid meet"` means the cap letterboxes the drawing rather than squashing it, so one cap serves six different aspect ratios.
- Measured at 390 with letter options (Q01, Q07): the first option starts **355px** below the chrome and the fourth ends at **622px**. On a 390 × 844 phone the scrollable window is 653px, so **the figure and all four options are on screen at once**.
- With full-sentence options and a figure (Q05 unanswered), the four options need 295px and the fourth lands ~6px under the fold. Three are always in view; the fourth is one thumb-flick away and the sticky action bar never moves.
- **Tap the figure and it takes the screen**: the cap becomes `min(72vh, 620px)` in place, caption switches to `TAP TO SHRINK`. In place rather than as an overlay, so the chrome, the timer and the marker row stay put and nothing has to be dismissed.
- On an iPhone SE (667px) two options are visible under the figure. That is the floor; it is not a broken state, it is a scroll.

---

## 5. The states

Reachable three ways: the `scenario` tweak, a URL hash on the standalone file, or simply playing the page.

| State | Hash | What is different |
| --- | --- | --- |
| First open | `#first` | Q01, fifteen 10px markers, `ANSWERED 00 / 15`, `15 LEFT`, clock from 00:00 |
| Mid-way | `#midway` | six answered (four right), on Q07, 06:12 on the clock |
| Returning after leaving | `#returning` | identical facts to mid-way, **plus** the arrival animation (§7) |
| All answered, not handed in | `#all` | `NONE LEFT` in accent, **Hand it in** replaces Next, no late chip |
| Handing in | — | the stamp, 1350ms, then the end screen |
| Handed in | `#done` | end screen, `HANDED IN` chip, timer frozen and labelled `TOTAL` |
| Opened after the due date | `#late` | `LATE` chip in the chrome, `· 2 DAYS LATE` on the due line in `--err`; nine answered, everything still works |
| Handed in late | `#donelate` | end screen with the `LATE` chip and `Marked · handed in late` |
| Live, saved | `#live` | reads `localStorage` — the real shipping behaviour |

A student who answered all fifteen and never pressed hand in **shows no late chip** (`All answered`). Late is a fact about the clock, not about the button.

---

## 6. Responsive specification

**Primary target 390px. Then 360px. Then tablet. Then desktop.** Same method as the class view, deliberately.

1. **Container queries for everything continuous.** The design root carries `container-type: inline-size`; every size, gap, padding and font size is a `clamp(min, Ncqw, max)` literal in the element's own inline style. Correct before the script runs, and correct at every width in between.
2. **Eight measured switches for everything discrete.** A width read on the root feeds eight values that cannot be interpolated. That is the whole list.

| Switch | Desktop ≥1024 | Tablet 720–1023 | Phone <720 |
| --- | --- | --- | --- |
| `shellDisplay` / `shellCols` | `grid`, `1fr` + `320px` | `block`, one column | `block`, one column |
| `optCols` | `1fr 1fr` | one column | one column |
| `showStrip` | hidden — the rail's grid replaces it | strip in the chrome | strip in the chrome |
| `showReadout` | hidden — in the rail | 27px row | 27px row |
| `rail` | 320px, `position: sticky; top: 78px` | none | none |
| `markerHit` + action | grid cells, 52px, jump | 40px, tap jumps | **44px, tap opens the sheet** |
| `wrongCols` (end screen) | two columns | one | one |
| header title + `BrandMark` | shown | shown | dropped |

Measurement is the class view's, unchanged: a synchronous read in `componentDidMount` so the first paint is already at the right breakpoint, then `resize`, `orientationchange` and `visualViewport` listeners plus a 250ms settle poll for six seconds. No `ResizeObserver` — it did not deliver reliably on a `container-type` element.

### Sticky, and why it is safe

Both the chrome and the action bar are `position: sticky` **inside** the `container-type: inline-size` root. Verified: at `scrollY 217` the header sits at `top: 0` and the action bar's bottom edge is on the viewport bottom. `position: fixed` would **not** be safe there — layout containment makes the root a containing block for fixed descendants — which is why the enlarged figure expands in place and the marker sheet is `position: absolute; top: 100%` on the header rather than an overlay.

### Type scale at small widths

Every size is one `clamp`. The 390 column is the phone value.

| | Desktop | 390px |
| --- | --- | --- |
| Question | 32px | **23px** |
| Option text | 16.5px | **15px** |
| Explanation | 15px | **13.5px** |
| End-screen title | 50px | 30px |
| End-screen score | 92px | 52px |
| Wrong-card question | 17px | 15.5px |
| Clock | 14.5px | 13px |
| Header assignment title | 18px | dropped |
| Mono eyebrows, captions, markers | 9–11.5px | unchanged |

### Touch targets

40px minimum at every width: back chevron 44px, marker row 44px (40px at ≥720), sheet cells 54px, rail cells 52px, options 60px minimum, action-bar buttons 46px, the quiet Next chevron 46 × 46px, the end screen's jump rows 44px and its buttons 48px.

### 360px

Same layout as 390 throughout — no further breakpoint. Markers become 19.6px, page padding stays 14px, every clamp is already at its floor. **Verified: no horizontal overflow at either 360 or 390** (root `scrollWidth` equals `clientWidth`; no descendant crosses the root's edges).

### The `layout` tweak

`Auto / Phone 360 / Phone 390 / Tablet 820 / Desktop 1460` pins the root to that width and centres it with hairline edges, driving the container queries and the switches together. `Auto` is the shipping behaviour.

---

## 7. Leaving and coming back

No banner, no sentence, no toast. The evidence is the state itself:

1. It **opens on the question they left off at** — not Q01, and not the next unanswered one either.
2. The marker row is already marked, and on a return those marks **arrive**: a 340ms scale-in per marker, staggered 40ms left to right (`mrbMark`). Under a second, and it makes the restore visible instead of asserted.
3. The clock is already at 06:12 and continues from there.
4. Row C already reads `ANSWERED 06 / 15 · 04 RIGHT · 09 LEFT`.

The stagger is cancelled by the first interaction (`resumed: false`), so it happens once per return and never again.

Persistence in the prototype is `localStorage` under `mrbadmusai.assignment.8rSc1.a5.v1` — `{answers, held, idx, elapsed, view, handedAt, late}`, written on every answer, every jump, every hand-in and every tenth clock tick. Only the `Live, saved` scenario reads or writes it, so a reviewer flipping between states never overwrites their own run. Wrapped in `try/catch`: in private mode the page works and forgets.

---

## 8. Connection loss

The design assumption is **local-first**: the tap marks the answer, the explanation appears, and the network is not in that path. So what changes offline is *not* whether the answer lands — it is whether it has been sent.

- A 5px **45° accent hatch** appears above the chrome — the class view's "on the bench" texture, reused as "in transit".
- A row under the readout: `OFFLINE · 03 HELD ON THIS DEVICE`, with a hatched swatch beside it, on `--st-chip-tint`.
- Answers made offline get **the same mark, hatched**: `--st-ink` fill overlaid with a 45° cream hatch. The mark still lands — that is the point — and its texture says not yet sent. It is legible in the sheet legend as `ON THIS DEVICE`.
- On reconnect the held marks **drain one at a time**, 130ms apart, and the row reads `BACK ONLINE · 03 SENT` for a beat before it goes.

Driven by the real `online` / `offline` events as well as the `offline` tweak, so pulling the network on a device shows it.

---

## 9. Hand in

**Cosmetic by design, and drawn that way.** No confirm, no warning, no count-down of consequences.

- The button appears **only when nothing is blank**, on every question, in the action bar. Before that, the last question offers `NEXT UNANSWERED` instead, which jumps to the first blank.
- Pressing it stamps: the content area is replaced by a dark `--st-room-panel` frame with the hatch strip, and a cream stamp block rotates in over 440ms (`mrbStamp`: scale 1.55 → 1, −9° → −2.5°) with a ring expanding behind it (`mrbRing`). Under it, in mono: `15 / 15 ANSWERED · 18:44 ON THE CLOCK`.
- 1350ms later the end screen. The action bar is gone throughout — there is nothing to press and nothing to undo.

---

## 10. The end screen

The revision artefact. Score, time, and every wrong answer with its explanation.

- **Dark panel** — the same object as the class view's bench and leader card, so the reward reads as continuous: `12 / 15` in Bricolage at 52px (92px desktop), `80%` in `--st-ember` beside it, then the whole marker row again in its dark variant (cream fill + ink tick for right, `--st-ember` outline + diamond for wrong) — **every marker still jumps**. Under it: `RIGHT 12 · WRONG 03 · TIME TAKEN 18:44`.
- **Where it went wrong** — one card per wrong answer, two columns at desktop, one below 1024. Each carries the question, `YOU CHOSE` in the wrong palette with that distractor's explanation, `THE ANSWER` in the ok palette with its explanation, and a 44px `LOOK AT QUESTION 03` row that jumps into review. Full marks gets `NOTHING WRONG` in a dashed box instead.
- **Look through all 15** returns to Q01 in review: everything marked, everything locked, `Summary` in the action bar to come back. Reachable for as long as the assignment exists.

---

## 11. Tokens

Design-system bundle at `_ds/mrbadmusai-design-system-…/`, linked in the helmet: `src-styles-tokens.css`, `shared-tokens.css`, `shared-ks3.css`, `fonts.css`, `_ds_bundle.css`, `styles.css`. The root carries **`class="rd" data-mode="ks3"`** — both hooks, or every `--ks3-*` value is inert. `--st-ink` is redefined on the root as `var(--ks3-ink)` = **#221E1B**, as in the class view.

| Job | Token | Value |
| --- | --- | --- |
| Ground, paper | `--st-ground`, `--st-paper` | #FBF3E6, #FFFDF8 |
| Ink | `--ks3-ink` | #221E1B |
| Every button fill, every orange under 24px | `--ks3-accent-text` | #A93411 |
| Button hover, link hover | `--ks3-accent-hover` | #7F2408 |
| Graphics only — hatch, rings, the current-marker ring, the 24px+ `80%` | `--st-accent` / `--st-ember` | #E4572E / #F2946E |
| Right — mark, 2px card border, tint wash | `--ks3-ok` | #12A150 |
| Right — the words `RIGHT` / `THE ANSWER`, **and the key-chip fill behind the 11px letter** | `--ks3-ok-text` | #0A6B36 |
| Right — card wash | `--ks3-ok-tint` | #E4F7EB |
| Wrong — mark, border, chip fill, the words | `--err` / `--err-bg` / `--err-border` | #A83824 / #FBE4DE / #E0897B |

R1 both ways: `--ks3-ok` never sits behind small text, so the 11px letter in the right-answer chip sits on `--ks3-ok-text` (#0A6B36, cream on it measures 6.5:1) while the tick, the 2px border and the wash stay on `--ks3-ok`. Same rule the orange already follows — every button fill is `--ks3-accent-text`.

`--st-ok-room` is **not** needed here: the one dark surface (the end panel, the hand-in stamp) marks right with a cream fill and an ink tick, not with green. The class view's request for that token still stands on its own account.

**Type.** Bricolage Grotesque 600 for questions, scores and the assignment title; Instrument Sans for options, explanations and buttons; DM Mono uppercase for every eyebrow, count, clock and marker numeral. Self-hosted, inlined in the standalone file.

**The glyph trap — still binding.** Every tick, cross, chevron and arrow is inline SVG: the option tick, the marker ticks, the hand-in chip tick, the stamp icon, the back and next chevrons, the sheet's close cross. Wrong is a **rotated bordered square**, never a glyph. `×` (U+00D7) is avoided in copy too: question 02 reads "An eyepiece lens of 10 and an objective lens of 40", question 06 says "a total magnification of 100", and the figure captions read `MAG 100` / `MAG 400`.

---

## 12. State and data

`Component.state`

| Key | Meaning |
| --- | --- |
| `w` | measured root width, px — the only source for the eight switches |
| `idx` | current question, 0-based |
| `answers` | `{ [questionIndex]: optionIndex }` — presence means confirmed and locked |
| `sels` | `{ [questionIndex]: optionIndex }` — selected but not yet confirmed; free to change |
| `held` | `{ [questionIndex]: 1 }` — answered while offline, not yet sent |
| `elapsed`, `paused` | the clock, in seconds |
| `view` | `'q'` \| `'done'` |
| `handing`, `handedAt` | the stamp, and the timestamp string |
| `sheet`, `zoom` | marker sheet open, figure enlarged |
| `resumed` | run the arrival stagger once |
| `net` | `'sent'` while draining held answers |
| `scn`, `live`, `late`, `realOff` | scenario, whether it persists, past due, real network state |

Question shape: `{ t: topic, q: text, o: [4 strings], f: [4 strings], a: answerIndex, g: figureKey | null }`. `f[i]` is the line for option `i` — for the answer it is the "Right. …" line, for a distractor it is that misconception.

Tweaks: `layout`, `scenario`, `offline`, `figures` (Six of them / Every question / None), `questionCount` (12–16).

### The timer

Counts up in a 1s interval. Pauses at **60,000ms** with no `pointerdown`, `keydown`, `wheel`, `touchstart` or `scroll`; any of those resumes it and resets the idle clock. It does not run on the end screen, during the stamp, or after hand-in. Paused reads as a hollow ring plus `PAUSED` and the numerals drop to `--st-muted`; after hand-in the label becomes `TOTAL`. **Their own total only** — no per-question clock exists in the data model, and no class figure is shown.

---

## 13. Every interaction

Back to `8r/Sc1` · tap an option to select it, and again to change your mind · **Confirm answer**, once, ever · read the explanation · Back · Next · tap the marker row to open the sheet (phone) or a marker to jump (tablet up) · tap a sheet cell to jump · Close the sheet · tap a figure to enlarge it, tap again to shrink · `NEXT UNANSWERED` from the last question · **Hand it in** when nothing is blank · the stamp · the end screen · tap any end-screen marker to jump to that question · `LOOK AT QUESTION NN` on a wrong card · **Look through all 15** · `Summary` back from review · Back to `8r/Sc1` · Open lesson 02 · go offline and answer anyway · come back online and watch it drain.

---

## 14. Continuity with the class view

- The route in is the class view's **Open the assignment** (and the expanded work row's primary button for open and retake rows) → `/class/8r-sc1/assignments/:id`. **That wiring is the one thing still open**: v1 ticks task one and stays put. In the prototype, back goes through history, falling back to `Class View.dc.html`.
- Same chrome pattern as v1's Recall screen — a slim bar with a back chevron to `8r/Sc1` — so a student recognises the room. `BrandMark` + `8r/Sc1` at 720px and up, chevron + `8r/Sc1` below.
- **v1 says eight questions and this is fifteen.** The class view's docket (`QUESTIONS 8`), its bench task (`Answer the eight questions`) and its blurb all need the real count from `assignment.questionCount`. Say the word and I will change it — I have not touched an approved file.

---

## 15. Do not ship

1. **The sixteen questions are authored examples.** The API needs to serve rungs 1–2 from the class's scheme of work with the per-distractor feedback strings — four per question, one per option, no generic fallbacks. A question without all four is not shippable: the whole design rests on them.
2. **The six figures are schematic stand-ins.** Real lesson art replaces them. The frame, the `clamp(132px, 34cqw, 232px)` cap, `preserveAspectRatio="meet"`, the caption row and the enlarge tap are the specification; the drawings are not.
3. **The date strings are fixed** (`DUE THU 18 SEP, 18:00`, `17 SEP, 20:41`, `20 SEP, 19:07`, `2 DAYS LATE`). Late, and the hand-in stamp, must come from the server clock, not the device's.
4. **`localStorage` is the stand-in for continuous save.** The rule is cross-device: the server holds `answers`, `idx` and `elapsed`, and the device is a cache. The drain animation in §8 assumes a queue that survives a reload.
5. **360px is verified in a desktop browser, not on a device.** Same open KS3 overflow defect as v1 — re-check on a real Year 7 phone with the real font load.
