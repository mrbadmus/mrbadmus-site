# B1 L1 · Life processes and what living things are made of · CLASSIFY

Inventory of `docs/ks3/design-reference/b1/b1-01-life-processes.dc.html` (834 lines, delivered
unmodified). Method, viewports, generator vocabulary and standing law: see `README.md` in this
folder — not restated here. Cross-page value collisions: `00-delivery-drift.md`.

Measured 13 Aug 2026 in headless Chrome via `ks3_browser.py`, serving
`docs/ks3/design-reference/b1/` over HTTP, at **1280 · 1340 · 820 · 390** with
`Emulation.setDeviceMetricsOverride`. Every number below was read from
`getComputedStyle` / `getBoundingClientRect` in that browser, or out of the file's own source.
Where a value could not be measured it says so.

**Console: clean.** No errors or uncaught exceptions at any of the four viewports (favicon 404
filtered). The page hydrates fully — `support.js` + `_ds/…/styles.css`.

**Content payload lives in the file's `<script data-dc-script>` block** and must be lifted
**byte-identical** from these lines, not retyped: `PROCESSES` 398–406 · `SPECIMENS` 408–473 ·
`SORT_ITEMS` 475–484 · `SORT_CHOICES` 486 · `RUNGS` 488–509 · `SELF_RUNGS` 511–536 · `RAIL` 538–543
· `RAIL_SHORT` 545 · `hookOptions` 768–776 · `predictOptions` 788–791 · `madeOf` 806–810. Static
prose: header 73–75, KEY FACT 211–212, misconception 220–231, `#s-rule` 237–247, keynote 350–351,
stretch 360, endmatter 366–384, safety line 387.

---

## 1. Page skeleton

### 1.1 The spine

`<body>` holds three children: `<x-dc>` (the authored template, forced to `display:none!important`
by the runtime), the hydrated **`<div class="rd" data-mode="ks3" data-motion="on|off">`**, and the
logic `<script>`.

⚠️ **`.rd` is a DIV here, not `<body>`.** `build_ks3.py` emits `<body class="rd"
data-mode="ks3">`, so `shared/ks3.css`'s page-shell rule `body.rd[data-mode="ks3"]` **does not
match** on the reference page. Design compensates with 8 inline declarations on the div, which
resolve to exactly what the class rule would have produced: `background #FBF3E6`
(`--ks3-ground`), `color #221E1B` (`--ks3-ink`), `font-family` `--ks3-font-body`, `font-size 19px`,
`line-height 30.4px` (1.6), `min-height 100vh`, `-webkit-font-smoothing: antialiased`,
`text-wrap: pretty`. The token block itself is `.rd[data-mode="ks3"]` (no `body`), so all 60 tokens
resolve normally. **Consequence for the generator: nothing to change** — emitting `.rd` on `<body>`
reproduces the same resolved values through the class rule. Recorded because a parity probe that
reads inline styles will not find them on generator output.

`.rd` children, in order (5 top-level landmarks):

| # | Element | Position | Height 1280 |
|---|---|---|---|
| 1 | `nav.ks3-nav` | static | 63.19 |
| 2 | `nav[data-rail="top"]` | **sticky, top 0, z-index 20** | 46.59 |
| 3 | `nav[data-rail="side"]` | **fixed, top 150px, left calc(50% − 632px), width 104px, z-index 20** | 0 (display:none <1340) |
| 4 | `main.ks3-main` | static | 6951.22 |
| 5 | `footer.ks3-footer` | static | 107.59 |

### 1.2 The measure

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `.ks3-main` width | 1280 | **1320** (capped, margin 10px each side) | 820 | 390 |
| `.ks3-main` max-width | 1320px = `--ks3-page` | same | same | same |
| `.ks3-main` padding | 44px 24px 90px | 44px 24px 90px | 44px 24px 90px | **28px 16px 64px** |
| `.ks3-lesson` width | **960** | **960** | 772 | 358 |
| `.ks3-lesson` max-width | 960px = `--ks3-wide` (60rem) | same | same | same |
| `.ks3-lesson > .ks3-explainer` | 736px = `--ks3-measure` (46rem) | 736 | 736 | 358 |
| document height | 7169 | 7122 | 7201 | 10939 |

Narrow breakpoint verified by bisection: `.ks3-main` padding and `.ks3-block` padding change
between **545 (wide values) and 544 (narrow values)** — i.e. `@media (max-width: 34rem)` in
`shared/ks3.css`. The page adds **no narrow media query of its own**; its only authored query is
`@media (min-width: 1340px)` for the rail, plus `prefers-reduced-motion`.

### 1.3 Header carries the lesson trail INLINE — confirmed

`nav.ks3-nav` is `display:flex; flex-wrap:wrap; gap:6px 0; padding:14px 24px 12px; border-bottom:2px
solid --ks3-ink; background --ks3-ground`. Four children:

| Child | What | Measured |
|---|---|---|
| `a.ks3-brand` | 34×34 `--ks3-accent` rounded-10px tile + inline chevron SVG (stroke `#FBF3E6`, width 4.6) + "MrBadmusAI" | 180.97×35.19, Bricolage 22px/800, ls −0.44px, gap 10px |
| `span[aria-hidden]` | vertical divider | 2×26, `background --ks3-rule`, `margin 0 20px`, `flex 0 0 2px` |
| **`ol[aria-label="Breadcrumb"]`** | **the lesson trail, inline in the nav** | 724.44×22.09, flex wrap, gap 9px, **17px**/22.1px |
| `a.ks3-nav-link` | "KS3" | 30.63×25.59, 16px/700, `--ks3-accent-text` |

Trail items: 7 `<li>` — 4 crumbs + 3 `›` separators. Crumb links `--ks3-accent-text` 600
`text-decoration:none; white-space:nowrap`; separators `--ks3-rule-strong`; last crumb
`aria-current="page"`, `--ks3-ink-muted`, weight 500. Nav height grows as the trail wraps:
**63.19 (1280/1340) → 94.78 (820, trail on its own row) → 176.06 (390, trail over 3 rows)**.

**The generator does it differently, and this is a real divergence.** `build_ks3.py:305` emits
`<nav class="ks3-nav">` containing *brand + KS3 link only*, and `crumbs()` (`build_ks3.py:285`)
emits a **separate `<nav class="ks3-crumbs">` row inside `<main>`** — mono `--ks3-font-mono` 14px,
`gap .4rem`, `margin-bottom 24px`, `.ks3-crumb-sep` separators. So the two are not the same
component: Design's is body-font 17px inline in the nav; the generator's is mono 14px in the page
body. Finding F1 (§8).

### 1.4 Lesson body, document order (13 direct children of `.ks3-lesson`)

| # | Element | id | classes | margin-top | scroll-margin-top |
|---|---|---|---|---|---|
| 1 | `header` | — | `ks3-lesson-head` | — | — |
| 2 | `section` | `s-hook` | `ks3-block ks3-dark ks3-hook` | 28px | 92px |
| 3 | `section` | `s-seven` | `ks3-explainer` | 28px | 92px |
| 4 | `section` | `s-board` | `ks3-block` | 28px | 92px |
| 5 | **`div`** | — | **none** | **24px** | **none** |
| 6 | `section` | `s-think` | `ks3-block ks3-misconception` | 28px | 92px |
| 7 | `section` | `s-rule` | none (all inline) | 28px | 92px |
| 8 | `section` | `s-sort` | `ks3-block` | 28px | 92px |
| 9 | `section` | `s-ladder` | `ks3-ladder` | 28px | 92px |
| 10 | `section` | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | 28px | 92px |
| 11 | `section` | — | `ks3-layer` | 34px | — |
| 12 | `div` | — | `ks3-endmatter` | 34px | — |
| 13 | `p` | — | `ks3-legal` | 34px | — |

Row 5 is the KEY FACT box: **an unclassed, un-id'd `<div>` between two sections**, source lines
210–213, preceded by two blank lines at 208–209 where a `</section>` would sit. It is not a section,
carries no anchor, and is not addressable by the rail.

`class` audit: the page uses **64 class names — 59 already exist in `shared/ks3.css`**, 1
(`ks3-hook-h`) exists nowhere and is inert (that `<h2>` is styled by `.ks3-hook h2`), and 4 are
template artefacts. Everything else is carried by **110 inline `style=` attributes** plus **10
JS-built style strings** (`optStyleTab`, `lampStyle`, chip/row/line/text/badge/verdict/note builders).

---

## 2. The progress rail — NEW, and there are two of it

Nothing in the generator emits either variant. **They are not two renderings of one thing: they
carry different information.**

### 2.1 Threshold

Bisected in the browser: at **1339** `[data-rail="side"]` is `display:none` and `[data-rail="top"]`
is `display:block`; at **1340 and 1341** the reverse. Authored as two rules in the page's `<style>`
(lines 21–22):

```css
[data-rail="side"] { display: none; }
@media (min-width: 1340px) { [data-rail="side"] { display: block; } [data-rail="top"] { display: none; } }
```

There is never a viewport with both, and never one with neither.

### 2.2 Variant A — the side rail (≥1340 only)

| Property | Measured (1340) | Token? |
|---|---|---|
| `position` / `top` / `left` / `width` / `z-index` | `fixed` / `150px` / `calc(50% − 632px)` → **38px** / `104px` / `20` | all bare |
| `ol` | flex column, `align-items:center`, no list style | — |
| node `<li>` | 32–45.55 wide × 90.19 tall (56.19 for the last, no connector) | — |
| chip | **32×32**, `border-radius 10px`, Bricolage **16px/800**, `border 2px` | bare |
| chip — done | `background --ks3-accent`, `border --ks3-ink`, `color --ks3-on-dark`, holds `svg.ks3-mark` | tokens |
| chip — current, not done | `background --ks3-card`, `border --ks3-ink`, `color --ks3-ink`, **`box-shadow: 0 0 0 4px --ks3-accent-tint`** | tokens |
| chip — future | `background --ks3-card`, `border --ks3-rule-strong` (#C3B191), `color --ks3-ink-ghost` (#9A8F86) | tokens |
| label | MONO **11px/500**, `letter-spacing .09em` (0.99px), uppercase, centred, lh 1.2 | bare |
| label colour | current `--ks3-ink` · done `--ks3-ink-muted` · future `--ks3-ink-ghost` | tokens |
| connector | `2×20`, `margin 7px 0`; `--ks3-accent` when the node above is done, else `--ks3-rule` | tokens |
| link | flex column, `gap 7px`, `padding 2px 0`, `text-decoration:none`, `color:inherit` | — |

Geometry at 1340: rail occupies x 38–142; `.ks3-lesson` starts at x 190 → a 48px gutter. It stays
in the gutter at wider viewports because `.ks3-main` caps at 1320px (checked arithmetically against
the measured `left` formula; not separately measured above 1341).

**4 stages** (`RAIL`, lines 538–543 + `RAIL_SHORT` 545):

| # | anchor | side label (`RAIL_SHORT`) | top-bar label (`RAIL[].label`) |
|---|---|---|---|
| 1 | `#s-hook` | HOOK | The flame |
| 2 | `#s-board` | TESTS | Run the tests |
| 3 | `#s-sort` | SORT | Sort all eight |
| 4 | `#s-ladder` | LADDER | Mastery ladder |

Two label sets, one per variant. Both are authored, neither is derivable from the block titles.

### 2.3 Variant B — the sticky top bar (<1340)

`position:sticky; top:0; z-index:20; background --ks3-ground; border-bottom 2px solid --ks3-rule;
padding 9px 16px 10px`. Inner row `display:flex; gap:12px; max-width:60rem (960px); margin:0 auto`:

| Part | Measured | Token? |
|---|---|---|
| count | MONO 15px/500, `--ks3-ink-muted`, 45×24, `flex 0 0 auto` — text `"1 / 4"` | bare size |
| current label | 16px/700, `--ks3-ink`, `flex 1 1 auto`, `overflow:hidden; text-overflow:ellipsis; white-space:nowrap` — 795 wide at 1280, 623 at 820, **193 at 390** | bare |
| track | `flex 0 0 96px`, height **8px**, `border-radius 99px`, `background --ks3-band`, `border 2px solid --ks3-ink`, `overflow:hidden` | tokens + bare |
| fill | height 100% (**4px** inside the border), `background --ks3-accent`, `width = (active+1)/4 × 100%` → measured **23px of 92px** at stage 1 | token |

### 2.4 Completion vs scroll — the two variants disagree

Driven in the browser (`scrollIntoView` at each of the 4 anchors, then measured):

| | drives what | mechanism |
|---|---|---|
| **top bar** | count `n / 4`, current label, fill width | **scroll only** — `state.active` from an `IntersectionObserver`, `rootMargin: '-45% 0px -50% 0px'` (lines 574–584) |
| **side rail** | ✓ mark + accent chip + accent connector | **completion** — `isDone(id, state)`, lines 547–553 |
| **side rail** | 4px `--ks3-accent-tint` ring + ink border + ink label | **scroll** — same `active` index |

So the top bar shows **no completion at all**: it reads `4 / 4` with a full accent bar for a
student who has scrolled to the bottom and answered nothing. Measured: scrolling to `#s-ladder`
without interacting gives `topCount: "4 / 4"`, fill 100%, while side-rail marks stay `[false ×4]`.
This contradicts `README.txt`'s standing convention — *"Progress rail ticks only on completed
activities, right or wrong"* — for the variant that every student under 1340px gets. Finding F2.

Completion predicates as authored:

```js
s-hook   → s.hookChoice !== null
s-board  → Object.keys(s.predictions).length > 0 && Object.keys(s.tapped).length >= 7
s-sort   → Object.keys(s.sort).length >= 8
s-ladder → s.answers.r1 !== null && s.answers.r2 !== null && s.checked.r3 && s.checked.r4
```

⚠️ **Stage 2 can never complete.** `s.tapped` is keyed by *specimen id* (4 possible keys), not by
test, so `>= 7` is unreachable. Measured: prediction set + all seven lamps tapped on Candle flame →
`sideMarks: [true, false, true, false]`. Stage 2's chip stays a grey `2`. Finding F3.

Dead code: `railFillHeight` (line 730) is computed and never returned — the side rail has no
continuous fill, only per-node connectors.

### 2.5 Anchors

**8 elements carry `scroll-margin-top: 92px`** — every `<section>` with an id (`s-hook`, `s-seven`,
`s-board`, `s-think`, `s-rule`, `s-sort`, `s-ladder`, `s-keynote`), authored individually as an
inline style on each. The rail references only 4 of the 8. The KEY FACT div, `.ks3-layer`,
`.ks3-endmatter` and `.ks3-legal` carry none. Value confirmed by driving it: clicking the side
rail's SORT link puts `#s-sort` at **top: 91.94px** with `location.hash = "#s-sort"`; at 1280 the
same landing leaves `#s-sort` at 91.53px with the 46.59px sticky bar occupying 0–46.59 — a 44.94px
clearance. `scroll-behavior` resolves to `auto` (no smooth scroll authored).

### 2.6 What the generator needs to emit it

```python
"rail": [                                     # NEW field, §5 gap G2
  {"anchor": "s-hook",   "short": "HOOK",   "label": "The flame",
   "done_when": "committed"},
  {"anchor": "s-board",  "short": "TESTS",  "label": "Run the tests",
   "done_when": "all_tests_run"},
  {"anchor": "s-sort",   "short": "SORT",   "label": "Sort all eight",
   "done_when": "all_sorted"},
  {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
   "done_when": "ladder_complete"},
]
```

Per stage: an anchor id that must match a section actually emitted, a ≤6-char mono `short`, a
sentence-case `label`, and a completion predicate naming a state the block already owns. Stage
count is `len(rail)`; the fill maths is `(active+1)/len(rail)`. Anchors and `scroll-margin-top: 92px`
must be emitted on **every** id-bearing section, not only rail stages, or a hash link from
elsewhere lands under the sticky bar.

---

## 3. Every block in document order

`GEN?` — **E** the generator has this block type · **E★** existing type, but this page uses it in a
shape the renderer cannot produce · **N** new. Component names in the last column are
`ks3_parity.COMPONENTS` entries (60 registered) that would gate it.

| # | Block | GEN? | States | Gating components |
|---|---|---|---|---|
| 1 | `header.ks3-lesson-head` — eyebrow "Cells and organisation · Classify", h1, `.ks3-bigq`, `.ks3-review-flag` | **E** (`build_ks3.py:1042`) | draft flag present / absent (`review_state != frozen`) | lesson title (row 1) · big question (row 2) · eyebrow (row 6) · draft badge |
| 2 | `#s-hook` — ink-dark 2-col: prose column (eyebrow "Start here", `h2.ks3-hook-h`, `.ks3-hook-prompt`) + **animated candle art** + **motion toggle**; then `.ks3-hook-commit` with `.ks3-commit` question, 3 `.ks3-option`s, gated `.ks3-reveal` | **E★** | option resting / chosen (border+badge → `--ks3-alert`); reveal hidden / shown; motion on / off; art animating / frozen | hook is ink-dark, accent shadow · dark-block option resting/CHOSEN (+badges) · standard block shell |
| 3 | `#s-seven` — explainer prose + **7 initial pills** (MRS GREN) | **E★** | none | body prose (row 4) |
| 4 | `#s-board` — **the CLASSIFY flagship** (see §3.1) | **N** | 4 specimens × (predict-open → board-open → complete) | activity option resting/CHOSEN (+badges) for the predict gate; everything else unregistered |
| 5 | **KEY FACT box** — `--ks3-band` ground, `2px --ks3-ink`, `box-shadow 5px 5px 0 --ks3-accent`, MONO 13px label + Bricolage 22px/700 statement | **N** | static, one state | none |
| 6 | `#s-think` — misconception: `.ks3-mis-head` (badge + eyebrow), `.ks3-mis-quote`, a prose line, **two mono-numeral scorecards** | **E★** | static | misconception is amber |
| 7 | `#s-rule` — **statement panel**: band ground, `3px --ks3-ink`, eyebrow, `clamp(30px,4.2vw,46px)` display statement `max-width 20ch`, 3 cards, closing 20px prose `max-width 46rem` | **N** | static | none (closest: standard block shell) |
| 8 | `#s-sort` — **the 3-way sorter** (see §3.2) | **N** | per-row unset / set; whole activity locked / unlocked; evidence hidden / shown | none |
| 9 | `#s-ladder` — `.ks3-ladder`, head + score, 2 page-marked rungs, 2 self-marked rungs, `.ks3-retry-wrap` | **E** (`build_ks3.py:882`) | option resting / correct / wrong / spent; feedback correct / wrong; ticks 0..4; tally not-yet / met; retry | ladder shell · ladder heading · ladder option ×6 states+badges · ladder feedback CORRECT/WRONG · page-marked rung is accent · self-marked rung is violet · R8 answer box · R8 check-my-answer button |
| 10 | `#s-keynote` — ink-dark, accent-yellow shadow, `p.ks3-eyebrow` + one paragraph | **E** | static | key note is ink-dark · key note type drops to 700 |
| 11 | `.ks3-layer` — "Going further" violet stretch layer | **E** (`r_layer`) | static (populated / omitted when empty) | stretch layer is violet |
| 12 | `.ks3-endmatter` — 4 cards: "Before this lesson" (**prose**), "Connects to" (2 links + arrow marks), "At GCSE this becomes" (**prose**), `.ks3-tutor` (**live `<a href="#s-board">`**) | **E★** | static | tutor card is accent · tutor text is large-bold |
| 13 | `p.ks3-legal` — **lesson-specific safety line** | **E★** | static | none |

Totals: **6 blocks the generator can already produce (E)**, **5 it produces in the wrong shape
(E★)**, **4 it cannot produce at all (N)** — counting the KEY FACT box, the board, the statement
panel and the sorter. Two of the four rail stages sit inside N blocks.

### 3.1 `#s-board` — "Run the seven tests", the CLASSIFY decision instrument

This is the lesson's flagship and the family's *"decision instrument (commit a prediction, watch
resolution)"* (§6). Real mechanics, driven in the browser:

**What the student manipulates.** Three nested affordances.

1. **Specimen tabs** — 4 pill buttons (`Candle flame · Oak seed · Robot vacuum · Yeast in dough`),
   `border-radius 999px`, 17px/700, `padding 11px 17px`, `min-height 44px`. On-state is an
   **ink fill**: `background --ks3-ink`, `border --ks3-ink`, `color --ks3-on-dark`. Off:
   `--ks3-card` on `--ks3-option-border`. `aria-pressed` carries the state;
   `transition: transform .14s` is declared but nothing changes `transform`.
2. **The prediction gate** — inside the inset panel, above a 2px `--ks3-rule` divider: *"Before you
   test it — alive, or not alive?"* (21px/700) and **2 `.ks3-option` buttons** (A Alive / B Not
   alive) in a `repeat(auto-fit, minmax(220px, 1fr))` grid. Choosing one **removes the gate
   entirely** (`predictionOpen: !prediction`) and opens the board. Measured: the whole prediction
   `<div>` disappears from the DOM — the student cannot see or change what they predicted
   afterwards. Finding F4.
3. **The lamp board** — **7 buttons, one per life process**, in
   `repeat(auto-fit, minmax(230px, 1fr))`, `gap 11px`. Each is a full-width 2-row button:
   row 1 = 28×28 Bricolage-15px/800 initial badge + process name (18px/700) + verdict word
   (16px/700, `margin-left:auto`); row 2 = the note (16px/1.45 `--ks3-ink-body`),
   `display:none` until tapped.

**Item counts.** 4 specimens × 7 processes = **28 authored verdict+note pairs** (lines 408–473),
plus per specimen a `verdictHead`, `verdictBody`, `cells` boolean, `cellsAnswer`, `cellsNote`.
Processes are MRS GREN with keys `M R S G Rp E N` — note **two initials read "R"** (Respiration,
Reproduction) and the key `Rp` disambiguates.

**Feedback, and when.** Tap → that lamp resolves, immediately and irreversibly:

| Lamp state | background | border | badge | verdict word | word colour |
|---|---|---|---|---|---|
| untapped | `--ks3-card` | `--ks3-option-border` | `--ks3-band` | "Tap to test" | `--ks3-accent-text` |
| tapped, process present | `--ks3-alert-tint` | **`--ks3-ink`** | `--ks3-alert` | "Yes" | `--ks3-alert-text` |
| tapped, process absent | `--ks3-row-dim` | `--ks3-option-border` | `--ks3-band` | "No" | `--ks3-ink-muted` |

Re-tapping is a **no-op** (`if (cur.indexOf(p.key) >= 0) return;`) — verified: state and computed
styles identical before and after. There is no reset per specimen.

Live readouts: instruction flips `"Tap each test to run it." → "All seven tested."`; tally is MONO
24px `"N of 7 lit"` where **N counts only the Yes lamps** (measured: M yes + R no → `"1 of 7 lit"`;
all seven on the flame → `"6 of 7 lit"`).

**Resolution.** When all 7 are tapped, an ink-dark panel appears inside the card
(`data-reveal="1"`, `background --ks3-ink`, `border-radius --ks3-r-panel`, `padding 22px 24px`):
Bricolage 26px/800 headline, 19px/1.6 `--ks3-on-dark-body` body, then a divided row
(`border-top 2px --ks3-dark-panel`) labelled **"The eighth test"** (MONO 15px, `.08em`, uppercase,
`--ks3-on-dark-muted`) with the cells answer in **20px/700 `--ks3-alert`** and the cells note in
18px `--ks3-on-dark-body`. This is where the lesson's actual rule lands.

**Does it mark correctness? No — and this is the R3-relevant answer.** The prediction is never
scored: choosing "Alive" for the candle flame produces the same UI as choosing "Not alive". The
lamps report the *specimen's* property, not the student's judgement. The verdict headline states
the truth ("Six of seven — and still not alive.") without ever referring to what was predicted. So
R3 is respected in the letter, and Law 4 (predict-before-reveal) is respected as a gate — but the
reveal never answers the prediction right or wrong "in tone tokens", which Law 4's second clause
asks for. Finding F5.

**State scope.** `predictions` and `tapped` are both keyed by specimen id, so all four instruments
hold independent progress. Verified: complete the flame, switch to Oak seed (prediction gate
returns, fresh lamps), switch back (flame's 7 lamps and verdict panel intact).

### 3.2 `#s-sort` — "Living, once living, never living"

The family's *"classification drills at rising stakes"*. **8 rows × 3 categories.**

- Rows are `<li>`, `padding 15px 18px`, `border-radius --ks3-r-option`, `background --ks3-card`,
  stacked in a flex column with `gap 10px`. Row border is **`--ks3-rule` before an answer and
  `--ks3-option-border` after** — a 2-shade "this row is answered" signal, nothing more.
- Each row: item name (`flex 1 1 190px`, 19px/700) + 3 chips
  (`Living · Once living · Never living`), 16px/700, `padding 9px 14px`, `min-height 44px`,
  `border-radius --ks3-r-control`. Chosen chip: `background --ks3-accent-tint`,
  `border --ks3-accent`. Unchosen: `--ks3-ground` on `--ks3-option-border`.
- **Choices are freely changeable** until the reveal — verified by re-clicking a row from
  "Never living" to "Once living"; the counter does not double-count.
- `.ks3-reveal-btn` "Show what settles each one" + MONO 15px progress `"N of 8 sorted"` →
  `"All eight sorted"`. **Locked state**: `disabled` attribute present, `opacity .45`,
  `cursor default` — clicking it while locked does nothing (verified). At 8/8 the attribute is
  removed, `opacity 1`, `cursor pointer`.
- Pressing it reveals, on **all eight rows at once**, a divided line
  (`border-top 2px --ks3-rule; padding-top 12px; 18px/1.55 --ks3-ink-body`) reading
  **`<strong>Answer</strong> — evidence`** where the bold word is the *correct* category in
  Bricolage 800.

**Correctness marking: none.** Measured with a deliberately wrong row (Yeast in bread dough →
"Once living"): after the reveal its chip is `--ks3-accent-tint`/`--ks3-accent` — pixel-identical
to a correct row's chip — while the evidence line says "Living — Single cells, feeding on sugar…".
No ✓/✗, no colour change, no count of how many were right. R3 is obeyed. Whether a student is
expected to self-mark by reading each line is **not stated anywhere on the page**. Finding F6.

Also measured: the evidence `<p>` carries `data-reveal="1"` but **not** `class="ks3-reveal"`, so
`animation-name` resolves to `none` — the `.ks3-reveal[data-reveal]` 220ms reveal animation in
`shared/ks3.css` does not fire here. The hook's reveal, which does carry the class, resolves to
`animation-name: ks3-reveal`. Finding F7 (trivial, Code can take it).

---

## 4. Interactive behaviours

All 12 driven in the browser with a 450ms settle after each click (the DC runtime re-renders
asynchronously — measuring in the immediately following `Runtime.evaluate` reads pre-render values
and will produce false "state does not paint" results).

| # | Trigger | What changes | Notes |
|---|---|---|---|
| 1 | Click a motion pill (On/Off) | `.rd[data-motion]` flips; `[data-motion="off"] [data-anim]` kills all 5 animations (`animation-name: none`, duration 0s) | On-pill: `--ks3-alert` fill, `--ks3-ink` text; Off-pill: transparent, `2px --ks3-on-dark-muted`, `--ks3-on-dark-body`. 15px/700, `padding 7px 14px`, `min-height 34px`, pill radius |
| 2 | OS `prefers-reduced-motion: reduce` | Flame/soot `animation-name: none` via the page's own query; **`data-motion` stays `"on"`** | Set at mount only (`componentDidMount`); a later OS change does not re-sync the toggle. CSS still wins |
| 3 | Click a hook option | `aria-pressed="true"` → border `--ks3-alert`, badge `--ks3-alert`/`--ks3-ink`; `.ks3-reveal` appears (dark variant: `--ks3-dark-panel`, `2px --ks3-alert`, radius 18px, `ks3-reveal` animation) | **Re-choosable** — no lock, no correctness. Rail stage 1 ticks |
| 4 | Click a specimen tab | Panel name/blurb swap; that specimen's own prediction/lamps/verdict restore | Independent state per specimen |
| 5 | Click a prediction option | Prediction block removed from DOM; lamp board + instruction + tally appear | Irreversible; unrecorded |
| 6 | Tap a lamp | Lamp resolves (§3.1 table), note row `display:none → block`, tally recount | Re-tap = no-op |
| 7 | Seventh lamp | Instruction → "All seven tested."; verdict panel appears | Per specimen |
| 8 | Click a sort chip | Chip → accent tint/accent; row border → `--ks3-option-border`; counter increments | Changeable; no marking |
| 9 | Click "Show what settles each one" | Locked: nothing. Unlocked: evidence line on all 8 rows | `sortRevealed` is one-way |
| 10 | Click a ladder option | Chosen wrong → `.is-wrong` (`--ks3-band` on `--ks3-ink`, badge ink/on-dark, drawn ✗ `M6.5 6.5l11 11M17.5 6.5l-11 11`); correct → `.is-correct` (`--ks3-ok-tint` on `--ks3-ok`, badge `--ks3-ok`/white, drawn ✓ `M5 12.5l4.6 4.5L19 7`); others → `.is-spent` (`--ks3-row-dim`, `--ks3-option-spent`, `--ks3-ink-faint`); **all 4 `disabled`**; `.ks3-feedback is-wrong\|is-correct` appears with the option's `correction`; score line updates | Second click on the same rung: no change (verified). Letters A–D replaced by the drawn mark on the marked options only |
| 11 | Type in a rung textarea, then "Check my answer" | Criteria `<ul class="ks3-ticks">` appears with 4 real checkboxes and `.ks3-tally` "0 of 4 ticked — not yet." (`--ks3-band`, `--ks3-ink-body`); ticking all 4 → `.ks3-tally.is-met` "All 4 ticked — rung met." (`--ks3-ok-tint`, `--ks3-ok-text`) and score +1 | ⚠️ **Two defects, measured.** (a) The typed answer is **lost on the next re-render** — `<textarea value="{{ rung.value }}">` sets an attribute a textarea does not read, so pressing Check empties the box while `state.text` still holds the string. (b) Check works with an **empty** textarea, and ticking all four then scores the rung. Findings F8, F9 |
| 12 | Click "Retry my misses" | `answers`, `checked`, `ticks` all reset; options re-enabled, feedback gone, score back to "You got 0 of 4." | ⚠️ It clears **correct** answers too, so it is a full ladder reset, not "my misses" — and its own note says "keeps what you wrote", which it cannot honour after F8. Finding F10 |

Score line: `"You got N of 4."` + `"You marked rungs 3 and 4 yourself."` — matches §5.8.1's ruling
(all four rungs count). Measured 0 → 1 (r2 correct) → 2 (r3 all ticked).

Keyboard/focus (real `Tab` via `Input.dispatchKeyEvent`): **every control gets the R15 ring** —
`outline: 3px solid #E4572E`, `outline-offset: 2px`, from `[data-mode="ks3"] :focus-visible`, and
it reaches Design's inline-styled buttons too (`.rd` carries `data-mode`). Tab order: brand → 3
crumb links → nav KS3 → motion On → motion Off → hook options → … The **top rail contains no
focusable element**, so under 1340px there is no keyboard route to a section; the side rail's 4
anchors provide one above it. Finding F11.

---

## 5. Schema gaps against §4.8

§4.8 is authoritative — *"Fields not listed here do not exist without an amendment to this
document."* Existing coverage first, then the gaps.

### 5.1 Already covered

| Page content | §4.8 field |
|---|---|
| h1, breadcrumb tail, eyebrow left half | `title`, `unit`, `discipline` |
| eyebrow right half "Classify" | `family` |
| `.ks3-bigq` | `big_question` |
| draft flag | `review_state` |
| hook eyebrow/heading/prompt/commit question | `phenomenon` (`{kind,title,prompt,commit}` as authored today) |
| `.ks3-mis-quote` | `misconceptions[].statement` |
| keynote paragraph | `key_note` |
| block order + types | `core[]` |
| "Going further" | `stretch[]` |
| ladder rungs, options, corrections, criteria | `ladder{recall,apply,explain,produce}` — `q`/`options`/`answer`/`feedback` for the marked pair, `q`/`success` for the self-marked pair. Design's per-option `correction` maps 1:1 onto the existing `feedback` dict keyed by option index |
| "Connects to" links | `references` / `requires` |
| candle art *existence* | `figures[]` — but see G12 |

Not surfaced on the page at all: `covers`, `touches`, `beyond_statutory`, `threads`,
`typical_year`, `typical_minutes`, `assumes`, `ws`, `vocabulary` (this lesson renders no keyword
block — the MRS GREN pills are not vocabulary cards).

### 5.2 Gaps — 13

| # | What the page needs | §4.8 today | Proposed field + shape | Sits inside |
|---|---|---|---|---|
| G1 | KEY FACT box, one per lesson, positioned mid-page | nothing (`key_note` is the end-of-lesson revision card and renders in the dark keynote block) | **block type `key-fact`** in `core`: `{"type": "key-fact", "text": "…"}`; text ≤ ~140 chars, may contain `<em>` | `core[]` — needs a §5.1.1 vocabulary amendment; MRB-203's registry fails the build otherwise |
| G2 | 4 progress-rail stages, two label sets, completion predicates | nothing | **`rail: [{anchor, short, label, done_when}]`** (§2.6) | top level |
| G3 | The seven-tests board: 7 processes × 4 specimens, 28 verdict+note pairs, 4 verdict panels | `activities[].kind` has no such kind; existing `classify` kind is a single prompt + flat `options` | **`activities[] {kind: "test-board", tests: [{key, initial, name}], specimens: [{id, name, blurb, results: {key: [bool, note]}, verdict_head, verdict_body, extra_label, extra_answer, extra_note}]}` | `activities[]` |
| G4 | The 3-way sorter: 8 items, 3 categories, per-item evidence | `classify` kind cannot express rows × categories | **`activities[] {kind: "sort-rows", categories: [str], items: [{id, name, answer, evidence}], reveal_label: str}` | `activities[]` |
| G5 | `#s-rule` statement panel: display statement + 3 cards + closing prose | nothing; not an `explainer` (band ground, 3px border, display type, card grid) | **block type `rule`**: `{"type": "rule", "eyebrow": "What settles it", "statement": "…", "cards": [{"term": "…", "gloss": "…"}], "close": "…"}` | `core[]` — §5.1.1 amendment. CLASSIFY's spine already demands it: *"Ends with the rule stated in the student's words"* |
| G6 | MRS GREN initial pills (7) | `explainer` renders prose only | **`{"type": "explainer", "text": "…", "pills": [{"initial": "M", "label": "Movement"}]}` | the `explainer` block record |
| G7 | Two mono-numeral scorecards in the misconception | `misconception` activity has `prompt`/`reveal`/`targets` only; `cards` is the flip-card component, which this is not | **`scorecards: [{figure: "6 of 7", title: "Candle flame — not alive", note: "…"}]`** | the `misconception` activity record |
| G8 | Tutor card copy "Stuck on why a flame isn't alive?" + CTA label + `href="#s-board"` | generator hard-codes generic copy and a non-interactive `<span>` (deliberately, `build_ks3.py:1013`) | **`tutor: {"prompt": "…", "cta": "…", "anchor": "s-board"}`** — but see F12 before adopting | top level |
| G9 | "At GCSE this becomes" as **prose** | `ks4_links` is a list of KS4 slugs (empty for this lesson) | **`ks4_becomes: "…"`** — prose sentence, rendered when `ks4_links` is empty | top level |
| G10 | "Before this lesson → Nothing — this is where the unit starts." | `requires: []` and the generator omits an empty card | **`before_this: "…"`** — prose used only when `requires` is empty | top level |
| G11 | `.ks3-legal` = "Never light a candle to test this at home without an adult with you." | `LEGAL_LINE` is a fixed copyright/provenance line | **`safety_note: "…"`** — and a ruling on whether both lines render | top level |
| G12 | The candle: an animated CSS/DOM illustration (2 flame layers, 3 soot motes, candle body, 2 `@keyframes`) | `figures[].kind` enum is `schematic \| graph \| photo \| apparatus` — none fits, and a figure record carries no code binding | **`figures[].kind += "css-art"`** plus **`art: "<registered-art-id>"`**, e.g. `{"id": "b1-candle-flame", "kind": "css-art", "art": "candle-flame", "caption": "…", "status": "final"}`; and the hook block needs `{"type": "hook", "art": "b1-candle-flame"}` to place it | `figures[]` (§4.10) + the `hook` block record |
| G13 | Motion toggle | nothing | No field. Emit it iff the lesson renders any `[data-anim]` art — derivable from G12. Code decision, stated here so it is not mistaken for a gap |

Two of these (G1, G5) are new **block types**, which under MRB-203 cannot be rendered until the
registry knows them; four (G3, G4, G6, G7) are new shapes **inside** existing records, which still
need §4.8/§5.5 amended because the activity record's sub-shape is only loosely specified today.

---

## 6. Measurements

`--ks3-*` tokens in play: **60 resolvable on `.rd[data-mode="ks3"]`** (plus `--ks3-hue` and
`--ks3-season`, which are scoped to index-page selectors and empty here). Enumerated with
`getComputedStyle(rd).getPropertyValue('--ks3-…')` after walking every `@import`ed sheet. The
bundled `_ds/…/tokens/shared-ks3.css` is **byte-identical** to the repo's `shared/ks3.css`; the
bundled `shared-tokens.css` differs from `shared/tokens.css` **only** in `@font-face` URL rewrites
(`/shared/fonts/…` → `../fonts/…`). So the page and the generator share one palette.

⚠️ `_ds/…/_ds_bundle.css` (35KB, loaded last through `styles.css`) is the **3D Studio** stylesheet
(`--st-*` tokens, `#root`, `st-ping`), not a KS3 bundle. It carries a bare
`button { background:none; border:none; padding:0 }` reset, harmlessly outranked by every
`.ks3-*` class rule here. Finding F13.

### 6.1 Shell and type

| Property | 1280 | 1340 | 820 | 390 | Token or new |
|---|---|---|---|---|---|
| root font-size / line-height | 19px / 30.4px | = | = | = | bare (matches `body.rd` rule) |
| `.ks3-main` padding | 44px 24px 90px | = | = | 28px 16px 64px | bare (ks3.css) |
| `.ks3-main` max-width | 1320px | = | = | = | `--ks3-page` |
| `.ks3-lesson` max-width | 960px | = | = | = | `--ks3-wide` |
| `.ks3-explainer` max-width | 736px | = | = | = | `--ks3-measure` |
| `nav.ks3-nav` padding / border-bottom | 14px 24px 12px / 2px `--ks3-ink` | = | = | = | bare / token |
| nav height | 63.19 | 63.19 | 94.78 | 176.06 | measured |
| `.ks3-brand` | Bricolage 22px/800, ls −0.44px, gap 10px, tile 34×34 r10 `--ks3-accent` | = | = | = | tokens + bare |
| breadcrumb `<ol>` | 17px / 22.1px, gap 9px | = | = | = | bare |
| h1 (`clamp(44px, 6vw, 74px)`, lh .94, ls −.035em) | **74px** / 69.56 | 74px | **49.2px** / 46.25 | **44px** / 41.36 | bare |
| `.ks3-bigq` | 25px/600, lh 1.35, `--ks3-accent-text`, max-width 24ch = 406px | = | = | 358 (clamped by column) | token colour |
| `.ks3-eyebrow` | 13px/700, ls .16em = 2.08px, uppercase, `--ks3-ink-muted` | = | = | = | token colour |
| `.ks3-lesson-head` | border-bottom 3px `--ks3-ink`, padding-bottom 28px | = | = | = | token |
| `.ks3-review-flag` | 16px/700 `--ks3-accent-text`, `--ks3-accent-tint` ground, 2px `--ks3-accent`, r999, 10px 17px, 313.41×49.59 | = | = | = | tokens |
| `.ks3-footer` | 16px `--ks3-ink-muted`, `--ks3-card` ground, border-top 2px `--ks3-ink`, padding 24px, centred, h 107.59 | = | = | = | tokens |
| `.ks3-legal` | 15px/22.5 `--ks3-ink-muted`, border-top **1px** `--ks3-rule`, padding-top 16px, margin-top 34px | = | = | = | tokens |

### 6.2 Block shells

| Block | radius | border | shadow | padding 1280 | padding 390 | ground |
|---|---|---|---|---|---|---|
| `.ks3-block` (`#s-board`, `#s-sort`) | 28px `--ks3-r-block` | 2px `--ks3-ink` | `5px 5px 0 --ks3-ink` (`--ks3-shadow-block`) | 30px | 22px 18px | `--ks3-card` |
| `.ks3-dark.ks3-hook` | 30px `--ks3-r-dark` | none | **`6px 6px 0 --ks3-accent`** | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-dark.ks3-keynote` | 30px | none | **`6px 6px 0 --ks3-alert`** | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-misconception` | 28px | 2px `--ks3-ink` | `5px 5px 0 --ks3-ink` | 30px | 22px 18px | **`--ks3-alert-tint`** |
| `#s-rule` (inline) | 28px `--ks3-r-block` | **3px `--ks3-ink`** | none | **34px 32px** | 34px 32px (no narrow rule) | **`--ks3-band`** |
| KEY FACT div (inline) | **20px `--ks3-r-panel`** | 2px `--ks3-ink` | **`5px 5px 0 --ks3-accent`** | **18px 22px** | 18px 22px | **`--ks3-band`** ✔ agrees with drift 5 |
| `.ks3-ladder` | 30px | **3px `--ks3-ink`** | **`6px 6px 0 --ks3-ok`** | 32px | 22px 18px | `--ks3-card` |
| `.ks3-layer-body` | **26px** | 2px `--ks3-stretch` | none | **26px 28px** | = | `--ks3-stretch-tint` |
| `.ks3-endmatter > section` | 22px `--ks3-r-card` | 2px `--ks3-ink` | none | 22px | = | `--ks3-card` (`.ks3-tutor`: `--ks3-accent`) |

Block spacing: `margin-top 28px` between sections, **24px** above the KEY FACT div, **34px** above
`.ks3-layer` / `.ks3-endmatter` / `.ks3-legal`.

### 6.3 Grids

| Grid | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `#s-hook > div` (`minmax(0,1.35fr) minmax(0,1fr)`, gap 34px) | 495.19 + 366.81 | = | 387.19 + 286.81 | **165.44 + 122.56 — never collapses** |
| hook options (`.ks3-options` flex column, gap 11px) | 896 | 896 | 708 | 322 |
| prediction options (`auto-fit, minmax(220px,1fr)`) | 416.5 ×2 | = | 322.5 ×2 | **266 ×1** |
| lamp grid (`auto-fit, minmax(230px,1fr)`, gap 11px) | 3 cols | 3 | 2 | 1 |
| misconception cards (`auto-fit, minmax(232px,1fr)`, gap 14px) | 441 ×2 | = | 347 ×2 | 318 ×1 |
| `#s-rule` cards (`auto-fit, minmax(220px,1fr)`, gap 14px) | 287.33 ×3 | = | 224.66 ×3 | 288 ×1 |
| MRS GREN pills / specimen tabs | flex wrap, gap 10px | = | = | wraps to 3 / 4 rows |
| sort rows | flex column, gap 10px; row inner flex wrap gap 14px; chips gap 8px | = | = | name and chips on separate lines |
| ladder options (`.ks3-ladder .ks3-options`) | 280.66 ×3 | = | ×3 | **296 ×1** (narrow rule) |
| `.ks3-endmatter` (`auto-fit, minmax(250px,1fr)`, gap 16px) | 309.33 ×3 | = | 378 ×2 | 358 ×1 |

### 6.4 Controls

| Control | size | radius | border | resting ground | chosen ground |
|---|---|---|---|---|---|
| `.ks3-option` (light) | 18px/600, `padding 16px 18px`, `min-height 44px` (`--ks3-tap`), gap 14px | `--ks3-r-option` 16px | 2px `--ks3-option-border` | `--ks3-ground` | `--ks3-accent-tint` + `--ks3-accent` border; badge → `--ks3-accent`/`--ks3-on-dark` |
| `.ks3-option` (on `.ks3-dark`) | same | 16px | 2px `--ks3-on-dark-muted` | `--ks3-dark-panel` | same panel, border → **`--ks3-alert`**; badge → `--ks3-alert`/`--ks3-ink` |
| `.ks3-opt-mark` | 28×28, r9, 15px/800 | — | — | `--ks3-band`/`--ks3-ink-muted` (dark: `--ks3-on-dark-muted`/`--ks3-ink`) | — |
| specimen tab | 17px/700, `11px 17px`, 44px, w 113–157 | **999px** | 2px | `--ks3-card`/`--ks3-option-border` | `--ks3-ink` fill (see drift 4: this is b1-03's inverted treatment, on a pill not `--ks3-r-control`) |
| lamp button | 18px/700 name, 16px/700 verdict, 16px/1.45 note, `padding 14px 16px`, 44px min, gap 8px | `--ks3-r-option` | 2px | `--ks3-card`/`--ks3-option-border` | §3.1 table |
| sort chip | 16px/700, `9px 14px`, 44px, w 78/117/121 | `--ks3-r-control` 14px | 2px | `--ks3-ground`/`--ks3-option-border` | `--ks3-accent-tint`/`--ks3-accent` |
| motion pill | 15px/700, `7px 14px`, **min-height 34px** (< `--ks3-tap`) | 999px | 2px | transparent/`--ks3-on-dark-muted` | `--ks3-alert` fill |
| `.ks3-reveal-btn` | 17px/700, `14px 22px`, 44px, `--ks3-ink` fill, `--ks3-on-dark` text | 14px | 2px `--ks3-ink` | — | locked: `opacity .45; cursor:default` |
| `.ks3-check-btn` | 17px/700, `13px 20px`, 44px, `--ks3-band` ground, 2px `--ks3-ink` | 14px | — | — | — |
| `.ks3-retry` | 18px/700, `14px 24px`, 44px, `--ks3-ink` fill | 14px | 2px | — | — |
| `.ks3-answer` | 19px/1.6, `16px 18px`, **min-height 136px**, w 864 | 16px | 2px `--ks3-option-border` | `--ks3-card` | — |
| `.ks3-tutor-cta` | 18px/600 `--ks3-accent-text` on `--ks3-card`, `10px 17px`, gap 6px | **12px** | — | — | — |

### 6.5 Type inventory (resolved)

| Role | family | size | weight | line-height | ls | colour |
|---|---|---|---|---|---|---|
| h1 | DISPLAY | 74 / 49.2 / 44 | 800 | .94 | −.035em | `--ks3-ink` |
| `.ks3-hook-h` (`.ks3-hook h2`) | DISPLAY | 38 (30 ≤544) | 800 | 39.9 | −1.14px | `--ks3-on-dark` |
| `.ks3-block h2` | DISPLAY | 30 | 800 | 36 | −.75px | `--ks3-ink` |
| `.ks3-ladder h2` | DISPLAY | 36 | 800 | 57.6 | −1.08px | `--ks3-ink` |
| `.ks3-rung h3` | DISPLAY | 23 | 800 | 36.8 | normal | `--ks3-accent-text` |
| `#s-rule` statement | DISPLAY | **46 / 46 / 34.44 / 30** (`clamp(30px,4.2vw,46px)`) | 800 | 1.06 | −.03em | `--ks3-ink` |
| KEY FACT statement | DISPLAY | 22 | 700 | 29.7 | −.015em | `--ks3-ink` |
| verdict headline | DISPLAY | 26 | 800 | 31.2 | −.02em | `--ks3-on-dark` |
| `.ks3-keynote p` + its eyebrow | DISPLAY | 30 (24 ≤544) | 700 | 39 | −.02em | `--ks3-on-dark` / `--ks3-alert` |
| `.ks3-endmatter h2` | DISPLAY | 21 | 800 | 26.25 | −.01em | `--ks3-ink` |
| body | BODY | 19 | 400 | 30.4 | — | `--ks3-ink` |
| `.ks3-explainer p` | BODY | 20 | 400 | 35 (1.75) | — | `--ks3-ink` |
| `#s-rule` closing prose | BODY | 20 | 400 | 34 (1.7) | — | `--ks3-ink` |
| `.ks3-commit` | BODY | 22 | 700 | 29.7 | — | `--ks3-on-dark-body` |
| prediction question | BODY | 21 | 700 | 33.6 | — | `--ks3-ink` |
| `.ks3-rung-q` | BODY | 21 | 600 | 29.4 | — | `--ks3-ink` |
| `.ks3-score` | BODY | 22 | 700 | 35.2 | — | `--ks3-ink` |
| card title / `.ks3-hook-prompt` | BODY | 18 / 19 | 700 / 400 | 28.8 / 31.35 | — | `--ks3-ink` / `--ks3-on-dark-body` |
| card body | BODY | 17 | 400 | 25.5 | — | `--ks3-ink-body` |
| `.ks3-ladder-sub` / `.ks3-score-note` / `.ks3-retry-note` / `.ks3-answer-label` | BODY | 18 / 16 / 16 / 16 | 400/400/400/700 | 28.8 / 25.6 | — | `--ks3-ink-muted` |
| scorecard numeral | MONO | 32 | 500 | 32 | — | `--ks3-ink` |
| lamp tally | MONO | 24 | 500 | — | — | `--ks3-ink` |
| specimen name caption | MONO | 15 | 500 | 24 | .06em | `--ks3-ink-muted` |
| "The eighth test" | MONO | 15 | 500 | — | .08em | `--ks3-on-dark-muted` |
| rail count / sort progress | MONO | 15 | 500 | 24 | — | `--ks3-ink-muted` |
| KEY FACT label | MONO | 13 | 500 | 20.8 | .09em | `--ks3-accent-text` |
| rail node label | MONO | 11 | 500 | 13.2 | .09em | state-dependent |

### 6.6 The candle art (measured geometry)

Frame: 366.81×**226** at 1280 (286.81 at 820, **122.56 at 390** — the frame narrows, the art does
not), `background #17130F` (**bare hex, no token**), `border 2px --ks3-dark-panel`,
`border-radius 22px`, `overflow:hidden`, `display:grid; place-items:end center`.

| Layer | size | offset | fill | animation |
|---|---|---|---|---|
| outer flame | 46×92 | `bottom 86px` | `linear-gradient(180deg,#FFC53D,#E4572E 62%,#A93411)` | `b1-flicker 1.7s ease-in-out infinite alternate` |
| inner flame | 20×42 | `bottom 90px` | `#FFF3D4` | `b1-flicker 1.15s …` |
| wick | 3×12 | `bottom 78px` | `#2A211B` | — |
| candle body | 74×78 | flow | `linear-gradient(90deg,#E7DECE,#FFFCF5 38%,#C6B9A7)` | — |
| soot ×3 | 5 / 4 / 3 px circles | `left 46/55/50%`, `bottom 128/132/140px` | `#6E6259` | `b1-soot 3.1s / 2.4s+.7s delay / 3.8s+1.4s delay linear infinite` |

Border radii on the flames are authored as two-axis percentages
(`50% 50% 46% 46% / 66% 66% 34% 34%` and `… / 70% 70% 30% 30%`). Nine of the eleven colours here
are **bare hex that happen to equal token values** (`#FFC53D` = `--ks3-alert`, `#E4572E` =
`--ks3-accent`, `#A93411` = `--ks3-accent-text`, `#FFF3D4` = `--ks3-alert-tint`, `#E7DECE` =
`--ks3-on-dark-body`, `#FFFCF5` = `--ks3-card`, `#C6B9A7` = `--ks3-on-dark-muted`); `#17130F`,
`#2A211B` and `#6E6259` match nothing in the palette and are genuinely new values.

---

## 7. New components — how to generate each

Seven components, in page order. Each states its data, markup, CSS, states and parity assertions.
Anything marked "assert" is a new `ks3_parity.COMPONENTS` entry.

### 7.1 `rail` — progress rail, both variants

- **Data:** §2.6's `rail` list + the four `done_when` predicates, which must resolve against state
  the blocks already own.
- **Markup:** two `<nav aria-label="Lesson progress">` siblings after `nav.ks3-nav`, one
  `data-rail="top"`, one `data-rail="side"`; side = `<ol><li><a href="#anchor"><span chip><span
  label></a><span connector></li>…`, the connector omitted on the last node; top = one flex row of
  count / label / track+fill.
- **CSS:** move the two authored rules into `shared/ks3.css` verbatim (`[data-rail="side"]{display:none}`
  + the `min-width:1340px` swap) and replace the JS style strings with classes:
  `.ks3-rail-chip`, `.ks3-rail-chip.is-done`, `.is-current`, `.ks3-rail-label`,
  `.ks3-rail-line.is-done`, `.ks3-railbar`, `.ks3-railbar-fill`. Every colour listed in §2.2 is
  already a token; the bare values needing a home are `104px`, `150px`, `632px`, `32px`, `20px`,
  `96px`, `8px`, `11px`, `.09em`.
- **States:** chip done / current / future (3) × label done / current / future (3) × connector done /
  not (2); top bar: count, label, fill width.
- **Assert:** (a) exactly one rail visible at each of 1280/1340; (b) side rail hidden at 1339,
  shown at 1340; (c) done chip is `--ks3-accent` ground + holds an `svg.ks3-mark`, never a typed ✓;
  (d) current chip carries `0 0 0 4px --ks3-accent-tint`; (e) future chip label is
  `--ks3-ink-ghost`; (f) side rail's right edge never overlaps `.ks3-lesson`'s left edge;
  (g) every rail `href` resolves to an element that exists and carries `scroll-margin-top: 92px`.

### 7.2 `key-fact` — the KEY FACT box

- **Data:** `{"type": "key-fact", "text": "…"}` (G1). One per lesson — assert at most one.
- **Markup:** `<div class="ks3-keyfact"><p class="ks3-keyfact-label">Key fact</p><p
  class="ks3-keyfact-body">…</p></div>` as a direct child of `.ks3-lesson`. Label text is fixed
  chrome, not data.
- **CSS:** `background var(--ks3-band); border: 2px solid var(--ks3-ink); border-radius:
  var(--ks3-r-panel); box-shadow: 5px 5px 0 var(--ks3-accent); padding: 18px 22px; margin-top:
  24px`; label MONO 13px/500 `.09em` uppercase `--ks3-accent-text`; body DISPLAY 22px/700 lh 1.35
  ls −.015em `--ks3-ink`.
- **States:** one.
- **Assert:** ground is `--ks3-band` (drift 5); the box carries **no badge, no letter, no mark** —
  `--ks3-band` is also the chosen-wrong ladder ground (MRB-202), so anything mark-like here reads
  as a verdict; shadow is accent, not ink (that is what distinguishes it from a `.ks3-block`).

### 7.3 `test-board` — the seven-tests instrument

- **Data:** G3. Validation the generator should enforce: `len(tests) >= 1`, every specimen supplies
  a result for **every** test key, `initial` may repeat but `key` may not, ≥2 specimens (the
  instrument's whole argument is comparison).
- **Markup:** `<section class="ks3-block" data-activity="…" data-board>` → eyebrow, `<h2>`, prompt
  `<p>`, `<ul class="ks3-tabs">` of `aria-pressed` buttons, then
  `<div class="ks3-board-panel">` holding: MONO name, blurb, the predict gate
  (`<ul class="ks3-options">` of 2 `.ks3-option`s behind a `border-top`), and the lamp grid
  `<ul class="ks3-lamps">` of `<button class="ks3-lamp">` with badge / name / verdict / note spans,
  then the verdict `<div class="ks3-board-verdict">`.
- **CSS:** panel `--ks3-inset` ground, `2px --ks3-ink`, `--ks3-r-panel`, 24px; dividers `2px
  --ks3-rule`; lamps per §6.4 with `.is-yes` / `.is-no`; verdict `--ks3-ink` ground,
  `--ks3-r-panel`, `22px 24px`, and its footer row `border-top 2px --ks3-dark-panel`.
- **States:** tab on/off (2); gate open/answered (2); lamp off/yes/no (3); board
  incomplete/complete (2); note hidden/shown (2). Full matrix per specimen: 4 × (2 × 3⁷).
- **Assert:** (a) a lamp's resolved state carries a **word** ("Yes"/"No"/"Tap to test") as well as
  colour (R2); (b) the lamp board is absent from the DOM until a prediction exists (Law 4);
  (c) tapping the same lamp twice does not change state; (d) the verdict panel appears only when
  every test is tapped; (e) no element in this block carries a ✓/✗ mark (R3 — only the ladder
  marks); (f) `--ks3-alert-tint` lamps sit on `--ks3-ink` borders, at 44px min-height.

### 7.4 `sort-rows` — the 3-way sorter

- **Data:** G4. Validate: every `answer` ∈ `categories`; ≥2 categories; evidence non-empty for
  every item.
- **Markup:** `<section class="ks3-block" data-activity="…" data-sort>` → eyebrow, `<h2>`, prompt,
  `<ul class="ks3-sortrows">` of `<li class="ks3-sortrow">` each holding a name span + a chip span
  of `aria-pressed` buttons + (after reveal) `<p class="ks3-sort-evidence" data-reveal>`; footer
  = `.ks3-reveal-btn` + MONO counter.
- **CSS:** row `--ks3-card`, `--ks3-r-option`, `15px 18px`, `2px --ks3-rule` →
  `.is-answered { border-color: var(--ks3-option-border) }`; chips per §6.4; evidence `border-top
  2px --ks3-rule; padding-top 12px; 18px/1.55 --ks3-ink-body`, its lead word DISPLAY 800.
- **States:** row unanswered/answered (2); chip chosen/not (2); button locked/unlocked (2);
  evidence hidden/shown (1-way).
- **Assert:** (a) the reveal button carries `disabled` until every row is answered, and the
  disabled state changes **more than opacity** — it must also read as locked in the counter text;
  (b) no chip differs by whether the choice was right (R3); (c) the evidence lead word equals the
  item's `answer` exactly; (d) counter text switches to a words form ("All eight sorted") at
  completion; (e) if the evidence is to animate, it needs `class="ks3-reveal"`, not `data-reveal`
  alone (F7).

### 7.5 `rule` — the statement panel

- **Data:** G5.
- **Markup:** `<section class="ks3-rule" id="s-rule"><p class="ks3-eyebrow">…</p><p
  class="ks3-rule-statement">…</p><ul class="ks3-rule-cards">…</ul><p class="ks3-rule-close">…</p>`.
- **CSS:** `background var(--ks3-band); border: 3px solid var(--ks3-ink); border-radius:
  var(--ks3-r-block); padding: 34px 32px`; statement DISPLAY 800 `clamp(28px, 3.9vw, 44px)`
  (**the ruled value from drift 3, not this page's `clamp(30px, 4.2vw, 46px)`**) lh 1.06 ls −.03em
  `max-width 20ch`; cards `auto-fit minmax(220px,1fr)` gap 14px, `--ks3-card` on
  `2px --ks3-option-border`, `--ks3-r-card`, `17px 19px`; close 20px/1.7 `max-width 46rem`.
- **States:** one.
- **Assert:** eyebrow takes `--ks3-accent-text` (not the default `--ks3-ink-muted`); border is
  3px, distinguishing it from a `.ks3-block`; statement clamp is the ruled one; card borders are
  `--ks3-option-border`, not `--ks3-ink` (that is what separates these from misconception cards).

### 7.6 `scorecards` — mono-numeral comparison pair

- **Data:** G7 — `[{figure, title, note}]`, 2–3 entries.
- **Markup:** `<ul class="ks3-scorecards"><li><p class="ks3-scorecard-fig">6 of 7</p><p
  class="ks3-scorecard-title">…</p><p class="ks3-scorecard-note">…</p></li>…`.
- **CSS:** grid `auto-fit minmax(232px,1fr)` gap 14px; card `--ks3-card` on `2px --ks3-ink`,
  `--ks3-r-card`, `18px 20px`; figure MONO 32px/500 lh 1; title 18px/700; note 17px/1.5
  `--ks3-ink-body`.
- **States:** one.
- **Assert:** the figure is MONO (it is a live-number role, §6.5) and the card sits on the amber
  misconception ground without becoming a mark.

### 7.7 `explainer.pills` — the initial-pill row

- **Data:** G6 — `pills: [{initial, label}]`, 2–8 entries.
- **Markup:** `<ul class="ks3-pills"><li><span class="ks3-pill-badge"
  aria-hidden="true">M</span><span class="ks3-pill-label">Movement</span></li>…`.
- **CSS:** flex wrap gap 10px; `<li>` `--ks3-card` on `2px --ks3-option-border`,
  `border-radius 999px`, `padding 9px 15px 9px 9px`, gap 9px; badge 26×26 r8 `--ks3-band`
  DISPLAY 15px/800 `--ks3-accent-text`; label 17px/600.
- **States:** one — this row is decorative reference, not a control. It must not be given
  `aria-pressed`, a cursor or a hover.
- **Assert:** the initial is duplicated in the label's first letter (so a screen reader reading
  only the label loses nothing) and the badge is `aria-hidden`.

Plus two the generator must **acquire rather than generate**:

- **`candle-flame` art (G12)** — 6 positioned elements + 2 `@keyframes` + 3 non-palette colours.
  A generator can only emit this from a **registered named art component** keyed by figure id. It is
  not derivable from any data shape. Recommend `shared/ks3-art.css` holding one block per art id and
  `build_ks3.py` emitting `<div class="ks3-art ks3-art--candle-flame" aria-hidden="true">` with the
  fixed inner spans. **Assert:** every `[data-anim]` element stops under both `[data-motion="off"]`
  and `prefers-reduced-motion: reduce`.
- **Motion toggle (G13)** — 2 pills on the dark ground, `min-height 34px`. Emit only in a block
  containing art. **Assert:** toggling sets `data-motion` on the `.rd` root and freezes every
  `[data-anim]`; both pills carry `aria-pressed`.

---

## 8. Ambiguities and findings

**(a) Needs Design.**

- **F1 — Two different breadcrumbs.** Design's trail is body-font 17px inline in `nav.ks3-nav`
  behind a 2px divider; the generator's is `nav.ks3-crumbs`, MONO 14px, a separate row inside
  `<main>`, and `.ks3-crumbs` is a shipped, tested class. Both are drawn; they cannot both be right.
  Not resolved here. Note the consequence either way: the inline trail is what pushes the nav to
  94.78px at 820 and 176.06px at 390, and the sticky rail sits directly under it.
- **F2 — The top rail shows scroll, not completion.** `README.txt` says the rail "ticks only on
  completed activities". The <1340 variant has no tick at all and reads 4/4 with a full accent bar
  for a student who answered nothing — measured. Does the top bar need completion (a fraction of
  *done* stages) or is progress-through-page intended for narrow screens?
- **F5 — Law 4's second clause.** The prediction gates the reveal, but the reveal never answers the
  prediction right or wrong, and the prediction is erased from the DOM once made. Law 4 asks that
  "the reveal answers the prediction right/wrong in tone tokens". Is the deliberate silence the
  design (so that only the ladder marks, R3), or a gap?
- **F6 — The sorter reveals answers without marking.** A wrong row is visually identical to a right
  one after the reveal; there is no self-mark, no count, and no instruction telling the student to
  compare. Eight items is a lot to self-mark unaided. Intended?
- **F12 — The tutor CTA is a live in-page anchor.** Design's card is
  `<a class="ks3-tutor-cta" href="#s-board">Ask about this lesson</a>` under the line "Stuck on why
  a flame isn't alive?". `build_ks3.py:1013` deliberately renders a `<span>` instead, with a
  comment recording that the previous `<a href="#ks3-tutor">` pointed at an element no KS3 page
  contains and that §8.8 means a KS3 student can reach no tutor today. Design's version resolves
  that by pointing the tutor card at **the lesson's own board activity** — which scrolls, does not
  ask anybody anything, and still reads as a tutor. The page wins under standing law, so this needs
  Design's word rather than Code's.
- **Drift 4 note.** This page's specimen tabs are a fifth `seg()`-shaped control: b1-06's geometry
  (17px, `11px 17px`, 44px) but on `border-radius: 999px` and with b1-03's **inverted ink
  on-state**. `00-delivery-drift.md` ruled the segmented control on b1-06's variant and flagged
  b1-03's inversion as Design's call; this page is evidence that the inversion is not a one-off.

**(b) Needs Mide (science / content).**

- **The approved page and the authored data teach different lessons.** `ks3_data/biology_b1_cells.py`
  L1 opens on "Three dishes on the bench" (seed / growing crystal / yeast) with
  `big_question: "What makes something alive?"`, and its ladder asks about the crystal. Design's
  approved page opens on a **candle flame**, asks *"A candle flame moves, grows, feeds and makes
  waste. So what stops it being alive?"*, and its ladder asks about a robot vacuum and a Mars
  probe. Under standing law the approved page wins, so the build re-authors the record from the page
  — which means **~1,900 words of new content** (counted from the file: 1,098 in the data constants,
  139 in the logic tail, 642 of static prose), nearly all of it science-bearing: 28 specimen verdict
  notes, 8 sort evidence lines, 4 ladder questions with 8 distractor corrections, 8 success
  criteria. It arrives at once and needs the examiner gate. Two specific claims worth Mide's eye because the page teaches
  them as settled: the candle flame is credited with **six of seven** processes including
  reproduction ("touch a second wick to it") and excretion; and coal is filed as **"Once living"**
  with the gloss "No cells left, but it was part of living things."
- **`covers` is `["KS3.B.CELLS.01a"]` today.** Whether the candle framing still owns that statement,
  and nothing more, is a curriculum judgement.

**(c) Code's call — recorded, not asked.**

- **F3 — Rail stage 2 can never tick** (`Object.keys(s.tapped).length >= 7` over a specimen-keyed
  map). Intent is unambiguous from `README.txt`; the predicate is wrong. Code fixes it. Which rule
  replaces it — *any one specimen fully tested* vs *all four* — is a real choice; recommend **any
  one**, because the block's own completion signal ("All seven tested.") fires per specimen.
- **F4** — the prediction disappears once made. Keeping it visible (disabled, chosen state
  retained) is an addition *inside* a component Design drew and contradicts nothing on the page.
  Recommend it; state it in the build report.
- **F7** — the sort evidence has `data-reveal` without `class="ks3-reveal"`, so the reveal
  animation does not fire. Add the class.
- **F8 — the self-marked answer is lost.** `<textarea value="{{…}}">` sets an attribute textareas
  ignore; pressing "Check my answer" re-renders and empties the box while state keeps the string.
  Measured. The generator's own `_rung_self` emits `<textarea … rows="5">` with no `value`, so this
  defect does not survive the port — but §5.8.1's *"keeps the written answer"* must be tested, not
  assumed.
- **F9 — "Check my answer" works on an empty box.** Measured: r4 checked with no text reveals all
  four criteria and ticking them scores the rung. §5.8.1 point 1 says the rung renders a textarea
  "and nothing else" before the button, precisely so that a written artefact exists before marking.
  Recommend gating Check on non-empty text; that is an addition inside Design's component and
  contradicts nothing drawn.
- **F10 — "Retry my misses" resets everything**, correct answers included (score 2 → 0, measured).
  §5.8.1 point 6 says it clears ticks and keeps the answer. Recommend retrying only unmet rungs.
- **F11 — no keyboard route to sections under 1340px.** The top rail holds only spans. Adding
  anchors to it is an addition inside a drawn component; alternatively leave it, since the
  breadcrumb and normal document order remain tab-navigable. Recommend adding them.
- **F13 — the shipped `_ds` bundle is the 3D Studio stylesheet**, not a KS3 one, loaded last and
  carrying a global `button` reset. It affects nothing here (every `.ks3-*` class rule outranks it),
  and the generator loads no such bundle. Recorded so nobody treats `_ds_bundle.css` as KS3 design
  intent.
- **The hook's 2-column grid never collapses.** `minmax(0,1.35fr) minmax(0,1fr)` holds at 390,
  giving a **165px prose column and a 122px candle** — the prompt paragraph grows to 345px tall.
  `shared/ks3.css`'s narrow query at 34rem does not touch it and the page adds no query of its own.
  Not in `00-delivery-drift.md` because it is a single-page fact, not a cross-page collision.
  The kind fix is a `max-width: 34rem` single-column rule for the hook split; that changes an
  approved page's narrow layout, so it is stated here as a finding and left for the build report.
- **`ks3-hook-h` is an inert class** (styled by `.ks3-hook h2`). Drop it.
- **Class-set note:** Design's ladder is `class="ks3-ladder"`; the generator emits
  `class="ks3-block ks3-ladder"`. Both resolve to the same painted shell (3px ink, 30px radius,
  `6px 6px 0 --ks3-ok`) because `.ks3-ladder` follows `.ks3-block` in the stylesheet — verified by
  measurement on this page for the single-class case only. Worth a parity assertion rather than a
  change.

**Could not measure.** Rail geometry above 1341px (checked arithmetically from the measured
`left: calc(50% − 632px)` and the 1320px cap, not by device-metrics override). `:hover` states
(`.ks3-option:hover { transform: translateX(3px) }` and the `transition: transform .14s` on the
specimen tabs) — CDP mouse-move hover was not driven; the rules are read from source, not measured.
The `320px` viewport was out of scope. No `print` stylesheet exists to measure.
