# Student class view — v1 handoff

**Date** 19 August 2026 · supersedes the 19 August delivery
**Scope** Follow-up to your brief: Studio and Board cut (MRB-264), Class table renamed, responsive design specified, real recall questions.

## Files

| File | What it is |
| --- | --- |
| `MrBadmusAI Class View.html` | Single self-contained file. Fonts, tokens, React and both screens inlined. Open it offline; every state is reachable. |
| `source/Class View.dc.html` | Authoring source. Template + logic class. Loads the design-system bundle by relative path. |
| `source/Class View - standalone source.dc.html` | The same source plus the bundler thumbnail. This is what compiles to the standalone file. |

Two screens: **Class** (`data-screen-label="Class"`) and **Recall** (`data-screen-label="Recall"`). There is no third screen.

---

## 1. What was removed

Everything named in §1 of the brief is gone from the source, not hidden:

- Screen 2 (Studio and Board) — deleted.
- The Studio/Board nav entry. The top bar now reads **My class · Recall**.
- The 308px lit stage in the bench's right column — replaced, see §2.
- `HotspotDot`, `ToolRail`, `QualityChip`, `createPlaceholderRenderer` — no references remain. `BrandMark` is the only design-system component the page mounts.
- The `topicBench` prop (Studio / Board) — deleted.
- All specimen, labelling and stage copy. Grep the source for `specimen`, `label`, `stage`, `hotspot`: no matches outside this sentence's absence.

The word **item** survives only as *question*: the marked-work breakdown is now headed "Question by question" and reads `6 OF 8 QUESTIONS RIGHT`.

---

## 2. The right column of the bench

**Chosen: your option 1 — a preview of the work itself.** An assignment docket: a paper slip resting on the dark bench, in `--st-paper` on `--st-room-panel`, so the one bright object on the bench is the thing that is due.

Contents, all fillable from data that exists in September:

| Row | Source field |
| --- | --- |
| `QUESTIONS` | `assignment.questionCount` |
| `DRAWS ON` | `assignment.lesson.title` — the KS3 lesson the questions come from |
| `SET` | `assignment.setAt`, formatted `EEE d MMM` |
| `DUE` | `assignment.dueAt`, formatted `EEE d MMM, HH:mm` |
| Footer left | days remaining, derived |
| Footer right | `assignment.pointsAvailable` — "40 POINTS AT STAKE" |
| Footer bar | fraction of the set→due window elapsed |

Option 2 (drop the column) was rejected because the docket earns its place; option 3 (the lesson's opening image) was rejected because it makes the bench depend on lesson art existing per topic.

Empty state (`classState = Fresh class`): the docket stays, every row is an em dash, the flag reads `BENCH CLEAR`, the footer reads `No deadline`. The panel never disappears, so the bench does not change shape when nothing is set.

### The bench, otherwise

- Primary CTA **Open the assignment** → `/class/8r-sc1/assignments/:id`. **This is an existing platform page and is not designed here.** In the prototype the click ticks task one, which is what opening it does to this page's state on return. The same route is behind the expanded work row's primary button for open and retake rows.
- Tasks: **Open it · Answer the eight questions · Hand it in**. Tappable, 40px rows, `N / 3 DONE` meter against them, unchanged in mechanism.
- The blurb ("Eight questions, set from this week's lessons…") is **dropped below 720px** — it restates the tasks, and on a phone the tasks and the CTA matter more than the sentence.

---

## 3. The Lessons card

Was "Specimens in this class". Now **Lessons in this topic**, pointing at the live KS3 lesson pages for the current topic. Four rows, each a link to `/ks3/biology/cells-and-microscopy/lesson-:n`:

| | |
| --- | --- |
| `01` | Life processes and cells — `READ · 4 RUNGS DONE` |
| `02` | Using a microscope — `THIS WEEK · SET IN THE ASSIGNMENT` (accent border + `--st-chip-tint`) |
| `03` | Animal and plant cells — `NOT OPENED` |
| `04` | Specialised cells — `NOT OPENED` |

The 52×44 hatched thumbnail is gone: it stood in for a specimen render. A 34px mono lesson numeral replaces it, so nothing on the card is a placeholder waiting on art.

---

## 4. Recall — real questions

Six questions per round, drawn from **rungs 1 and 2** of the authored KS3 lessons, across the topics the class has covered. Each distractor carries the feedback written against it in the lesson; that feedback now renders after **Check**, in a panel to the left of the button row, edged `--st-ok-room` when right and `--st-ember` when not.

The six in the prototype (`Component.questions`), with the answer marked:

1. **Cells & microscopy** — An eyepiece lens of 10 and an objective lens of 40 are used together. What is the total magnification? → **B: 400, because the two lens powers are multiplied together**
2. **Cell parts** — Which structure would you find in a plant cell but never in an animal cell? → **A: A chloroplast, where light is absorbed for photosynthesis**
3. **Cells & microscopy** — What is the job of the cell membrane? → **B: To control which substances enter and leave the cell**
4. **Digestion** — Why does the body use enzymes to digest food? → **A: They break large food molecules into small ones the body can absorb**
5. **Movement & joints** — Why do muscles have to work in pairs across a joint? → **B: A muscle can only pull, so a second muscle pulls the bone back**
6. **Gas exchange** — Alveoli are covered in a dense network of capillaries. Why does that matter? → **B: It gives oxygen a very short distance to diffuse into the blood**

### What the real length changed

- **The 40px question survives, with a wider measure.** `26ch` put question 1 on four lines; it is now `min(30ch, 100%)`, which holds the longest of the six to three lines at desktop. The type scale is `clamp(25px, 3.1cqw, 40px)` — 40px at 1290px and above, 25px at 390px, where question 1 runs to five lines and still clears the options.
- **The 2×2 option grid becomes a single column below 1024px.** Full-sentence options in a 450px cell already wrap to two lines; in a 340px cell they wrap to three and the grid stops reading as a grid. Single column is the rule for tablet and phone, 2×2 for desktop only.
- Options are top-aligned (`align-items:flex-start`), not centred, so a two-line option does not push its key chip off the first line.
- No question, option or feedback string exceeds the panel at 360px. Longest measured line: question 1 at five lines, 372px stage inner width.

Round mechanics are unchanged: pip row, two-step check-then-next, streak, round-score card, unlimited rounds.

---

## 5. Leaderboard

Renamed everywhere: section eyebrow, the empty state ("The leaderboard starts when the first work is marked"), the recall card's copy ("Recall counts for 20 of the 100 points on the leaderboard"), the round-complete note, and the pinned row's gap text. Section anchor is `#board`; `data-screen-label="Leaderboard"`.

The component is otherwise untouched — leader card, chaser rows, pinned self row, movement marks, legend footer, week chips, top-5/top-10 toggle.

Legend, unchanged and still visible: **ON TIME · 40 · SCORE · 40 · RECALL · 20**, `RESETS EVERY MONDAY 00:00`. As before: **the split shown in the bars is an approximation for drawing only** (`onTime = round(pts × 0.4)` capped at 40, `recall = round(pts × 0.19)` capped at 20, score is the remainder). Real per-component values come from the API. Do not ship the approximation.

---

## 6. Responsive specification

**Primary target 390px. Then 360px. Then tablet. Then desktop.**

### How it is built

Two mechanisms, deliberately split:

1. **Container queries for everything continuous.** The page root carries `container-type: inline-size`; every size, gap, padding and font size is a `clamp(min, Ncqw, max)` literal in the element's own style. Nothing continuous is computed in JavaScript, so it is correct before the script runs and correct at every width in between, not only at the breakpoints.
2. **Ten measured switches for everything discrete.** A width measurement on the root feeds ten values that cannot be interpolated. That is the whole list; there are no others.

| Switch | Desktop ≥1024 | Tablet 720–1023 | Phone <720 |
| --- | --- | --- | --- |
| `benchCols` | `1fr` + `minmax(300px,440px)` | one column | one column |
| `docketOrder` | 3 (right) | 1 (above the copy) | 1 (above the copy) |
| `statsBasis` | `340px`, beside the title | `100%`, own row | `100%`, own row |
| `railDisplay` / `railAlign` | `grid` / `start` | `flex` column / `stretch` | `flex` column / `stretch` |
| `spineCols` | `repeat(12, 46px)` | `repeat(12, 46px)` | `repeat(6, minmax(40px,1fr))` |
| `rowCols` | `46px 20px 1fr auto` | `46px 20px 1fr auto` | `18px 1fr auto` |
| `chaseCols` | `30px 34px 1fr 62px 22px` | same | `24px 30px 1fr 52px 16px` |
| `boardCols` | leader + chasers side by side | stacked | stacked |
| `recallCols` | `1fr` + `356px` | one column | one column |
| `optCols` | `1fr 1fr` | one column | one column |
| `ghostRight` | `-14px` (bleeds) | `12px` (inset) | `12px` (inset) |

Measurement: a synchronous read in `componentDidMount`, so the first paint is already at the right breakpoint; then `resize`, `orientationchange` and `visualViewport` listeners, plus a 250ms settle poll for the first six seconds to catch font load and scrollbar arrival. A `ResizeObserver` on a `container-type` element did **not** deliver reliably in testing — do not reintroduce it as the only source.

### The bench when it cannot be two columns

Below 1024px the bench becomes one column and the docket moves **above** the copy. Order on a phone: docket → eyebrow → headline → tasks → CTA row. The facts a student opens the page for (how many questions, when it is due) are the first thing under the fold-free header; the button that acts on them is still one screen down, not three. The blurb is dropped (§2).

### The term spine when twelve bars do not fit

**Two rows of six, not a scroller and not a compressed bar.** Twelve 46px bars plus gaps need 662px; 390px offers 362px. Compressing to 26px bars fits but breaks the 40px touch minimum, and a scroller breaks the spine's only job, which is seeing the whole term at once. Six per row at `minmax(40px,1fr)` keeps both: the whole term visible, every bar tappable, and the split falls on the half-term. Bar height is `clamp(42px, 3.6cqw, 50px)`.

### The leaderboard when the two columns do not fit

Stacked, leader card first at full width, then chaser rows, then the pinned self row, then the legend. The chaser grid drops to `24px 30px 1fr 52px 16px` with `gap: 8px` — the name column still resolves to 188px at 390px, which holds every roster name without truncation (verified against the longest, `Hafsah I.`). The ghost `01` numeral moves inside the card rather than bleeding off it, so it is never a half-glyph at the edge.

### The work-row grid at 390px

**It does not survive.** `46px 20px 1fr auto` needs 114px of fixed columns before the title, and the `auto` column carries score, status word, hint and caret. At 390px it becomes `18px 1fr auto`:

- The week number leaves the grid and joins a mono meta line under the title: `W04 · DUE THU 18:00`.
- The one-line brief (`8 questions · draws on this week's lessons`) is dropped; it reappears in the expanded panel's detail line.
- The status word and the hint (`READ FEEDBACK`) are dropped from the row; the caret carries the affordance and the expanded header carries the detail.
- The score stays, at `clamp(22px, 2cqw, 27px)`.
- Row height is 64px at 390px, comfortably over the 40px minimum.

**The inline feedback panel inside it:** unchanged in structure, tightened in padding to `clamp(13px,1.4cqw,18px)` and inset to `margin: 0 clamp(4px,1.2cqw,16px) 20px` so it reads as nested rather than full-bleed. Note rows keep the 30px `MB` avatar beside the text. Question chips wrap. The footer's two buttons stay on one row at 390px (`Open the lesson` + `Close` = 232px); the `MARKS ARE FINAL…` footnote is dropped below 720px.

### Which sidebar cards move, and where

Only one card is promoted. Phone order:

1. Bench
2. Term spine
3. **Recall card** — moved above the work list. It is the one action always available, it needs no assignment to be set, and on a phone it should not be four screens down.
4. Work list
5. Lessons in this topic
6. Shoutouts
7. Leaderboard

Desktop placement is different, and deliberately so. The rail is a two-column grid whose row heights are set by the taller column, so a short column leaves a visible band of nothing. Balancing it:

| Card | Desktop cell |
| --- | --- |
| Work list | col 1, rows 1–2 |
| Shoutouts | col 1, row 3 — **under the work list**, not in the sidebar |
| Lessons in this topic | col 2, row 1 |
| Recall card | col 2, row 2 |

Column 1 measures 774px against the sidebar's 565px, so the leftover whitespace falls at the foot of the sidebar where it reads as ordinary column white, rather than as a 331px band across the page above the leaderboard. Shoutouts is the card to move because it is the least urgent and the most tolerant of being read last.

Implemented with `order` on the four children of one container, which is a CSS grid at desktop (explicit `grid-column` / `grid-row`) and a flex column below it. The two placement systems coexist on every child — `order` is inert in the grid because every cell is explicit, and `grid-column` / `grid-row` are inert in the flex column. No markup is duplicated between layouts, and the phone order above is unaffected by the desktop rebalance.

### Type scale at small widths

Every size is one `clamp`. Phone value is the 390px result.

| | Desktop | 390px |
| --- | --- | --- |
| Page title `8r/Sc1` | 76px | **40px** |
| Bench headline | 46px | **27px** |
| Recall question | 40px | **25px** |
| Leader name | 40px | 26px |
| Leader points | 62px | 38px |
| Round score | 96px | 56px |
| Reading values | 34px | 26px |
| Work-row title | 18px | 16.5px |
| Body / options | 16.5 / 16px | 15 / 14.5px |
| Mono eyebrows and captions | 9.5–11.5px | unchanged |

Mono labels are not scaled. They are already at the floor and they are what the layout is measured against.

### Chrome at small widths

- Header 56px (from 64px). The `PROD` chip, the name "Ayo", and the Settings and Sign out links leave the bar; the avatar becomes a button opening a 186px sheet with **Settings** and **Sign out**, 44px rows. Brand chevron and wordmark stay, wordmark at 16px.
- Breadcrumb bar 44px. Right-hand note shortens from `AUTUMN TERM · WEEK 04 / 12` to `WK 04 / 12`.
- Page padding `clamp(14px, 3cqw, 44px)`: 44px desktop, 14px at both 390 and 360.

### Touch targets

40px minimum, everywhere, at every width: nav items, avatar, bench tasks, week bars, work rows, work tabs, leaderboard week chips, the top-5/10 toggle, recall options (62px), and every button. The account sheet's rows are 44px.

### 360px

Same layout as 390px throughout — no further breakpoint. Every clamp bottoms out at or before 360px, so nothing shrinks further and nothing overflows. Verified: no horizontal scroll at 360px on either screen. This is the defect class the open KS3 overflow ticket describes, so it is worth re-checking against the real font load on device.

### The `layout` prop

A tweak, `Auto / Phone 360 / Phone 390 / Tablet 820 / Desktop 1460`, pins the root to that width and centres it with hairline edges. It drives the container queries and the switches together, so a reviewer sees the true 390px design without resizing a window. `Auto` is the shipping behaviour.

---

## 7. Tokens

Design-system bundle at `_ds/mrbadmusai-design-system-…/`, linked in the helmet: `src-styles-tokens.css`, `shared-tokens.css`, `shared-ks3.css`, `fonts.css`, `_ds_bundle.css`, `styles.css`.

The root carries **`class="rd" data-mode="ks3"`** — both hooks, or every `--ks3-*` value is inert.

### Corrections in this build

**Ink.** `--st-ink` is redefined on the design root as `var(--ks3-ink)` = **#221E1B**, the locked KS3 value. The studio package's own `--st-ink` is #1A1714; that is the older value and it is not used anywhere on this page.

**The green — and this needs correcting in the brief's favour.** `#12A150` is **not new to the KS3 system**. It is already `--ks3-ok` in `tokens/shared-tokens.css`, ruled there as *"3.0:1 — NEVER body text"* and reserved for the ladder's correctness marks, with `--ks3-ok-text: #0A6B36` for anything at body size. So there is nothing to amend for the cream surfaces: this page now uses `var(--ks3-ok)` by name, and only ever as a graphic — the 3px on-time meter, the 5px chaser bars, the 16px legend swatch. No green text anywhere.

**One genuine amendment, please rule on it.** There is no green in the `--st-*` dark-room family, and `--ks3-ok` at #12A150 measures 2.3:1 on `--st-room-panel` #1E1913, under the 3:1 graphic threshold. The bench and the leader card need one:

```
--st-ok-room: #55B36A;   /* dark-room success green. 6.6:1 on --st-room-panel.
                            Graphic only: bar segments, the recall tick, a 3px panel edge.
                            The dark-surface counterpart of --ks3-ok, as --st-ember is of --ks3-accent. */
```

Declared on the design root, not in the token files. It wants adding to `src-styles-tokens.css` beside `--st-ember` before this ships.

**Accent.** `--ks3-accent-text` #A93411 for every button fill and every orange under 24px; `--ks3-accent-hover` #7F2408 for hover; `--ks3-accent` #E4572E for graphics only — hatch strips, rings, the open-status dot, bar segments. `a` and `a:hover` are defined in the helmet against those two.

**Type.** Bricolage Grotesque 600 display, Instrument Sans UI and body, DM Mono uppercase eyebrows and numerals. Self-hosted, inlined in the standalone file.

### The glyph trap — still binding

The latin subsets do not carry `→` (U+2192), `✓` (U+2713) or `✕` (U+2715). Every arrow, tick and cross on this page is inline SVG: the chevron in each CTA, the back chevron, the task tick, the correct-answer tick, the question-chip ticks, the two filter-clear crosses, the leaderboard movement triangles. The missed-work mark is a rotated bordered square, not a glyph.

`×` was also avoided in copy: recall question 1 reads "An eyepiece lens of 10 and an objective lens of 40" rather than using the multiplication sign, so no science notation depends on a character outside the subset. If U+00D7 is confirmed present in the shipped subsets, the question can be rewritten to standard notation.

### Breadcrumb

`MY CLASSES › 8r/Sc1 › OVERVIEW` implied a list. It is now two crumbs: **`8r/Sc1 › OVERVIEW`**, with the brand mark as the route home. A student has one class, so there is no list crumb to click. On Recall it reads `8r/Sc1 › RECALL`.

### Brand mark

`MrBadmusDS.BrandMark` — the orange double chevron — plus the "MrBadmusAI" wordmark in Bricolage 600, as on KS3 lesson pages. Designed to your reading that student surfaces are the student's own product surface. If Mide reads the plain-white-text rule as covering these too, it is one component swap in the header.

---

## 8. State and data

`Component.state`

| Key | Meaning |
| --- | --- |
| `view` | `'class'` \| `'recall'` |
| `w` | measured root width, px — the only source for the ten switches |
| `menu` | account sheet open |
| `tab` | `'all'` \| `'todo'` \| `'marked'` |
| `week` | 1–12 or `null` — term-spine filter |
| `open` | id of the expanded work row, or `null` — one at a time |
| `bench` | `{t1,t2,t3}` task ticks |
| `boardWeek` | 1–4 or `'term'` |
| `boardSize` | 5 or 10 |
| `qi`, `pick`, `checked`, `right`, `streak` | recall round |

Props: `layout`, `classState` (Work set / Fresh class), `hideScores`, `showSpine`.

Work item shape: `{ id, week, title, brief, status, score?, late?, retake?, detail, notes?[], items?[] }` with `status` in `open | marked | pending | missed`. `items` is an array of 1/0 per question.

Filters compose: tab then week. When they empty the list, the empty state offers **Clear filters**, and the term spine offers **SHOW ALL 12 WEEKS** whenever a week is picked — both were the filter-trap fix and both survive.

Status is carried by **shape**, never hue alone: filled disc marked, hollow ring pending, ringed disc open, rotated square missed. Identical in the spine, the rows and the legend.

---

## 9. Every interaction

**Class.** Nav My class / Recall · avatar sheet · breadcrumb to class root · four readings (static) · week bar tap to filter, tap again or SHOW ALL 12 WEEKS to clear · three work tabs · bench task ticks with meter · **Open the assignment** (routes out; ticks task one) · Practise recall · docket (static) · work row expand and collapse, one at a time, with per-row primary and Close · Clear filters · lesson rows link out · leaderboard week chips W01–W04 and TERM · SHOW TOP 10 / SHOW TOP 5.

**Recall.** Back to 8r/Sc1 · pick an option · **Check** reveals the answer and that distractor's feedback · **Next question** · Skip, which breaks the streak · round-complete card at six · Another round · Back to class · Open the assignment instead.

**Empty states.** `classState = Fresh class` empties the work list, the shoutouts, the leaderboard and the docket, and swaps the bench to "No work set yet" with recall as the only action. `hideScores` replaces every percentage with its status word; the leaderboard is unaffected, by design — it is a different permission.

---

## 10. Do not ship

1. **The leaderboard bar split is drawn from an approximation.** Wire the real per-component values before this goes near a student.
2. **`--st-ok-room: #55B36A` is not in the token files yet.** §7. It needs a ruling and a line in `src-styles-tokens.css`.
3. **`Open the assignment` routes to a page that is not designed here.** Confirm the route and the return behaviour — this page assumes it comes back with task one ticked.
4. **Recall questions are six hardcoded examples.** The API needs to serve rungs 1–2 across the topics a class has covered, with the per-distractor feedback strings.
5. **360px is verified in a desktop browser, not on a device.** The open KS3 overflow defect is the reason to re-check on a real Year 7 phone with the real font load.
