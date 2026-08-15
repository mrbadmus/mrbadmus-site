# B1 L3 · Animal and plant cells · MODEL

Inventory of `docs/ks3/design-reference/b1/b1-03-animal-and-plant-cells.dc.html` (1,265 lines,
delivered unmodified). Method, viewports, generator vocabulary and standing law: see `README.md` in
this folder — not restated here. Cross-page value collisions: `00-delivery-drift.md`.

Measured 13 Aug 2026 in headless Chrome via `ks3_browser.py`, serving
`docs/ks3/design-reference/b1/` over HTTP, at **1280 · 1340 · 820 · 390** with
`Emulation.setDeviceMetricsOverride` (`page.set_viewport`). Every number below was read from
`getComputedStyle` / `getBoundingClientRect` in that browser, or out of the file's own source.
Where a value could not be measured it says so.

**Console: clean.** No errors or uncaught exceptions at any of the four viewports (favicon 404
filtered), on either this page or the generator's.

## ⚠️ This page is not just another lesson — it is the MODEL reference screen

`docs/ks3/design-coverage-manifest.md` §10.1 names **this file** as the approved reference screen
for the MODEL family, at **50 slots** — the largest family in the curriculum, and more than a
quarter of all 183:

| Family | Slots | Reference screen | Approved |
|---|---|---|---|
| MODEL | **50** | `docs/ks3/design-reference/b1/b1-03-animal-and-plant-cells.dc.html` | Mide, 12 Aug 2026 |

So every divergence recorded in §3.1 below is a divergence on 50 lessons, not one. §10.1 also
carries a **numeric inconsistency worth one line**: §10.1 says MODEL has 50 slots, while
`design-coverage-manifest.md` line 75 says **49** (Biology 8, Chemistry 17, Physics 24 = 49). One
of the two is wrong. Code cannot tell which; it is not load-bearing for this inventory.

**Content payload lives in the file's `<script data-dc-script>` block** and must be lifted
**byte-identical** from these lines, not retyped: `RAIL` 493–499 · `RAIL_SHORT` 501 · `isDone`
503–510 · `PARTS` 515–559 · `CHLORO`/`MITO_LEAF`/`MITO_CHEEK` 561–566 · `SORT` 568–579 ·
`CONSEQUENCE` 581–589 · `FIT` 591–624 · `RUNGS` 626–643 · `SELF_RUNGS` 645–666 · the canvas
drawing routines 668–931 · `renderVals` string literals 1049–1259. Static prose: header 74–76,
hook 84–115, bench intro 139–141, `#s-rule` 226–249, `#s-wall` 254–256 + 281–282, `#s-fit` 290–295,
`#s-think` 352–367, keynote 443–444, stretch 453, endmatter 458–479, safety line 482.

**Authored word count (for MRB-205):** ~1,984 words inside the data constants and `renderVals`
literals, plus 954 in static markup — **~2,938 words**, counted with a script over the source. Of
the 1,984, 505 are the seven parts' `job`/`detail`/`scopeNote` triples, 360 the four FIT cells,
478 the four ladder rungs and their eight criteria, 239 the sorter and its consequence lines. Almost
all of it is science-bearing and none of it exists in `ks3_data/`.

---

## 1. Page skeleton

### 1.1 The spine — confirms b1-01 §1.1

`<body>` holds two children: the hydrated **`<div class="rd" data-mode="ks3">`** and the logic
`<script>` (the `<x-dc>` template is removed rather than hidden on this page — measured
`bodyKids: [div.rd, script]`, where b1-01 kept an `<x-dc>` at `display:none`).

⚠️ **`.rd` is a DIV here, not `<body>`** — the same divergence b1-01 §1.1 recorded and resolved
("nothing to change"). Confirmed identically: 8 inline declarations on the div reproduce what
`body.rd[data-mode="ks3"]` in `shared/ks3.css` would give (`background var(--ks3-ground)`,
`color var(--ks3-ink)`, `font-family var(--ks3-font-body)`, `font-size 19px`, `line-height 1.6`,
`min-height 100vh`, `-webkit-font-smoothing: antialiased`, `text-wrap: pretty`), and the token block
is `.rd[data-mode="ks3"]` so all 60 tokens resolve. **One new consequence**, and it is not cosmetic
— see §1.5.

`.rd` children, in order (5 top-level landmarks — same set as b1-01):

| # | Element | Position | Height 1280 |
|---|---|---|---|
| 1 | `nav.ks3-nav` | static | 63.19 |
| 2 | `nav[data-rail="top"]` | **sticky, top 0, z-index 20** | 46.59 |
| 3 | `nav[data-rail="side"]` | **fixed, top 150px, left calc(50% − 632px), width 104px, z-index 20** | 0 (`display:none` <1340) |
| 4 | `main.ks3-main` | static | 8999.31 |
| 5 | `footer.ks3-footer` | static | 107.59 |

### 1.2 The measure

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `.ks3-main` width | 1280 | **1320** (capped, margin 10px each side) | 820 | 390 |
| `.ks3-main` max-width | 1320px = `--ks3-page` | same | same | same |
| `.ks3-main` padding | 44px 24px 90px | 44px 24px 90px | 44px 24px 90px | **28px 16px 64px** |
| `.ks3-lesson` width | **960** | **960** | 772 | 358 |
| `.ks3-lesson` max-width | 960px = `--ks3-wide` (60rem) | same | same | same |
| `nav.ks3-nav` height | 63.19 | 63.19 | **63.19** | **153.97** |
| document height | 9217 | 9170 | 9525 | 14571 |

Narrow breakpoint verified by bisection: `.ks3-main` padding and `.ks3-block` padding change
between **545 (wide) and 544 (narrow)** — `@media (max-width: 34rem)` in `shared/ks3.css`,
identical to b1-01. The page's own queries are exactly three: `max-width: 780px` (bench grid),
`min-width: 1340px` (rail swap) and `prefers-reduced-motion: reduce` (kills `[data-arrive]`).

This page carries **no `.ks3-explainer`** — there is no 736px `--ks3-measure` column anywhere in it.
Every block runs the full 960px. The MODEL spine's *"prose orbits it"* is realised by making prose
a paragraph inside an instrument block, capped by `ch` measures (`54ch` on `#s-bench` and `#s-wall`,
`58ch` on `#s-fit`, `26ch` on the `#s-rule` statement) rather than by a shared measure column.

### 1.3 Header carries the lesson trail INLINE — confirmed, and it wraps *later* here

The nav markup and every resolved value match b1-01 §1.3 exactly: `display:flex; flex-wrap:wrap;
gap:6px 0; padding:14px 24px 12px; border-bottom:2px solid --ks3-ink; background --ks3-ground`;
brand 180.97×35.19 Bricolage 22px/800 ls −0.44px with a 34×34 `--ks3-accent` r10 tile; 2×26
`--ks3-rule` divider at `margin 0 20px`; `ol[aria-label="Breadcrumb"]` at body-font **17px/22.1px,
gap 9px**; trailing `a.ks3-nav-link` "KS3". Crumb links `--ks3-accent-text` 600, separators
`--ks3-rule-strong`, last crumb `aria-current="page"` `--ks3-ink-muted` 500.

**What differs is only the wrap point,** because this lesson's title is shorter: the `<ol>` measures
512.67px wide (b1-01's was 724.44), so it still fits beside the brand at 820 and the nav stays
**63.19px at 1280, 1340 *and* 820**, growing only at 390 (**153.97**, trail over 2 rows). b1-01
measured 94.78 at 820 and 176.06 at 390. **So nav height is a function of the lesson title's
length** — a parity assertion must not pin it to a number.

F1 (two different breadcrumbs) reproduces exactly; the generator's `nav.ks3-crumbs` is measured
against Design's in §3.1.

### 1.4 Lesson body, document order (12 direct children of `.ks3-lesson`)

| # | Element | id | classes | margin-top | scroll-margin-top |
|---|---|---|---|---|---|
| 1 | `header` | — | `ks3-lesson-head` | — | — |
| 2 | `section` | `s-hook` | `ks3-block ks3-dark ks3-hook` | 28px | 92px |
| 3 | `section` | `s-bench` | `ks3-block` | 28px | 92px |
| 4 | `section` | `s-rule` | **none** (all inline) | 28px | 92px |
| 5 | `section` | `s-wall` | `ks3-block` | 28px | 92px |
| 6 | `section` | `s-fit` | `ks3-block ks3-dark ks3-practical` | 28px | 92px |
| 7 | `section` | `s-think` | `ks3-block ks3-misconception` | 28px | 92px |
| 8 | `section` | `s-ladder` | **`ks3-ladder`** (single class) | 28px | 92px |
| 9 | `section` | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | 28px | 92px |
| 10 | `section` | — | `ks3-layer` | 34px | — |
| 11 | `div` | — | `ks3-endmatter` | 34px | — |
| 12 | `p` | — | `ks3-legal` | 34px | — |

Two structural differences from b1-01 worth stating:

- **Every id-bearing block is a `<section>` with an anchor.** b1-01 had a stray unclassed `<div>`
  (its KEY FACT box) sitting at top level between two sections; this page has none. The KEY FACT
  boxes here live **inside `#s-think`** (§3.6).
- **`#s-fit` is the first `ks3-practical` in the B1 inventory.** Shadow `6px 6px 0
  var(--ks3-blue)` (#2F5CE0), eyebrow `var(--ks3-blue-light)` (#8FB7FF) — `shared/ks3.css:254,257`.
  b1-01 and b1-02 never exercised it.

### 1.5 Class audit, and a stylesheet-set divergence that is *not* cosmetic

The page uses **51 `ks3-*` class names, and all 51 exist in `shared/ks3.css`.** There is no inert
class here — notably **no `ks3-hook-h`**: this page's hook `<h2>` carries no class at all and is
styled by `.ks3-hook h2`. That independently confirms b1-01's recommendation ("`ks3-hook-h` is an
inert class. Drop it") — Design already dropped it one lesson later.

Non-`ks3-*` classes found: `sc-interp` only. The DC runtime wraps **every** `{{ }}` interpolation in
a `<span class="sc-interp">`, which shifts `querySelectorAll('span')` indices inside any
interpolated control. The generator emits bare text nodes. A parity probe that walks child spans
positionally will read the wrong element on the reference page and the right one on generator output.

Everything else is carried by **225 inline `style=` attributes** (b1-01: 110) plus **13 JS-built
style strings** (`seg`, `node.chipStyle/textStyle/lineStyle/linkStyle`, `railBarStyle`, `p.style`,
`p.numStyle`, `p.tagStyle`, `readoutStyle`, `readoutNumStyle`, `readoutWhereStyle`,
`readoutScopeStyle`, `row.style`, `c.style`, `row.answerStyle`, `f.style`, `f.wordStyle`,
`verdictBadgeStyle`, `clearStyle`, plus the dead `runBtnStyle`). This is a much more
inline-carried page than L1 — consistent with `project_design_delivery_shape`.

#### ⚑ The reference page and the generated page do not load the same stylesheets — and it changes measurements

Enumerated by walking `document.styleSheets` and following every `CSSImportRule`:

| | Reference page | Generated page |
|---|---|---|
| sheets | 9 (2 inline + `_ds/…/styles.css` → 5 imports + 1 inline) | 4 link tags |
| KS3 rules | `_ds/…/tokens/shared-ks3.css` | `/shared/ks3.css?v=41a3ad43` |
| tokens | `_ds/…/tokens/shared-tokens.css` | `/shared/tokens.css?v=8bc49b72` |
| **`shared/styles.css`** | **absent** | **present** |
| **`shared/nav.css`** | **absent** | **present** |
| 3D Studio CSS | `_ds_bundle.css` **and** `tokens/src-styles-tokens.css` | absent |

`diff` of the bundled `shared-ks3.css` against the repo's `shared/ks3.css` is **empty — byte
identical**, confirming b1-01 §6. And b1-01's F13 holds but understates it: the bundle ships **two**
3D Studio files, not one — `_ds_bundle.css` (35KB, `--st-*`, `#root`, `st-ping`) and
`tokens/src-styles-tokens.css` (3.5KB, the `--st-*` token block, header comment "3D Studio tokens").
Neither is KS3 design intent.

The load-bearing half is the *absence* of `shared/styles.css` on the reference page. That sheet
carries, at line 20:

```css
h1, h2, h3, .brand {
  font-family: var(--font-serif);
  font-optical-sizing: auto;
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: var(--lh-title);   /* --lh-title: 1.15  (shared/tokens.css:166) */
}
```

`shared/ks3.css`'s `[data-mode="ks3"] h1, h2, h3` (specificity 0,1,1) overrides the family and the
weight, but **sets no `line-height` and no `letter-spacing`**. So on the generated page every KS3
heading with no explicit line-height inherits `1.15` from the KS4 sheet; on the reference page it
inherits `1.6` from the page shell. Measured on `.ks3-rung h3` (23px, no line-height rule anywhere
in ks3.css):

| | reference | generated |
|---|---|---|
| `.ks3-rung h3` line-height | **36.8px** (1.6) | **26.45px** (1.15) |

That is a 10.35px per-line divergence on all eight rung headings of every KS3 lesson, invisible to
any probe that only ever loads one of the two sheet sets. Finding F14.

---

## 2. The progress rail — same component as b1-01, **five** stages

The rail is byte-for-byte the same component b1-01 §2 specified, at a different stage count.
Confirmed, not re-derived:

- **Two variants, never both, never neither.** Bisected: at **1339** `[data-rail="side"]` is
  `display:none` and `[data-rail="top"]` is `display:block`; at **1340** and **1341** the reverse.
  Authored as the same two rules (source lines 22–23) b1-01 carried.
- **Side rail geometry identical:** `fixed`, `top 150px`, `left calc(50% − 632px)` → **x 38** at
  1340, `width 104px`, `z-index 20`; `.ks3-lesson` starts at x 190 → a 48px gutter. Height 416.94
  for five nodes (b1-01: 4 nodes).
- **Chip states identical** and every colour is a token: done = `--ks3-accent` ground, `--ks3-ink`
  border, `--ks3-on-dark` text, holds `svg.ks3-mark` (measured `hasMark: true`, `chipTxt: ""` — the
  number is *replaced* by the drawn tick, not accompanied by it); current-not-done = `--ks3-card` on
  `--ks3-ink` with `box-shadow: 0 0 0 4px --ks3-accent-tint`; future = `--ks3-card` on
  `--ks3-rule-strong` with `--ks3-ink-ghost` text. Chip 32×32, r10, Bricolage 16px/800, border 2px.
- **Label** MONO 11px/500, `letter-spacing .09em` (0.99px), uppercase, lh 1.2; current `--ks3-ink`,
  done `--ks3-ink-muted`, future `--ks3-ink-ghost`.
- **Connector** 2×20 at `margin 7px 0`; `--ks3-accent` when the node above is done, else
  `--ks3-rule`. Omitted on the last node (`hasLine: i < RAIL.length - 1`).
- **Top bar** `sticky; top 0; z-index 20; background --ks3-ground; border-bottom 2px --ks3-rule;
  padding 9px 16px 10px`; inner row `flex; gap 12px; max-width 60rem; margin 0 auto`; count MONO
  15px/500 `--ks3-ink-muted`; current label 16px/700 `--ks3-ink` with
  `overflow:hidden; text-overflow:ellipsis; white-space:nowrap` (measured **795px** at 1280,
  **623** at 820, **193** at 390); track `flex 0 0 96px`, height 8px, r99, `--ks3-band` ground,
  `2px --ks3-ink`; fill 4px inside the border, `--ks3-accent`.

### 2.1 Five stages, and their two label sets

`RAIL` 493–499 + `RAIL_SHORT` 501:

| # | anchor | side label (`RAIL_SHORT`) | top-bar label (`RAIL[].label`) | `done_when` (`isDone`, 503–510) |
|---|---|---|---|---|
| 1 | `#s-hook` | HOOK | The parts list | `s.hookChoice !== null` |
| 2 | `#s-bench` | BENCH | The bench | `s.gate !== null` |
| 3 | `#s-wall` | WALL | Wall or membrane | `!!s.sortOpen` |
| 4 | `#s-fit` | BUILD | Fit the cell | `Object.keys(s.fitRan).length >= 4` |
| 5 | `#s-ladder` | LADDER | Mastery ladder | `answers.r1 !== null && answers.r2 !== null && checked.r3 && checked.r4` |

Both label sets are authored and neither is derivable from the block titles. Fill maths is
`(active + 1) / 5 × 100%` — measured 18.39 / 36.8 / 55.19 / 73.59 / **92 of a 96px track**.

**All five stages are reachable, and I drove all five to done.** b1-01's F3 (an unreachable stage)
does not reproduce. Three notes:

- **Stage 2 ticks on the *gate*, not on the instrument.** One click on any of four gate options
  ticks BENCH, and the student has then touched no part button, no specimen tab and no view tab. The
  richest instrument on the page is credited by its cheapest control.
- **Stage 4 is the most expensive stage in the B1 inventory** — all four FIT cells must be run.
  Measured: "Strip it back out" *deletes* `fitRan[spec.id]`, so it can un-tick a stage that was
  already earned (progress went "2 of 4 cells run" → "1 of 4" on one click).
- **Stage 2 becomes unreachable if `showScopeView` is false.** `gateOpen = scopeAvailable &&
  s.gate === null`; with the prop off, the gate never renders, `s.gate` stays `null`, BENCH never
  ticks. Read from source at lines 1102 and 505; **not measured** (the prop defaults to `true` and I
  did not override the `data-props` payload).

### 2.2 F2 reproduced, on five stages

b1-01's F2 ("the top bar shows scroll, not completion") reproduces exactly and one stage worse.
Driven at 1280 with `scrollIntoView` at each anchor and **nothing answered**:

| scrolled to | count | label | fill |
|---|---|---|---|
| `#s-hook` | 1 / 5 | The parts list | 18.39 / 96 |
| `#s-bench` | 2 / 5 | The bench | 36.8 / 96 |
| `#s-wall` | 3 / 5 | Wall or membrane | 55.19 / 96 |
| `#s-fit` | 4 / 5 | Fit the cell | 73.59 / 96 |
| `#s-ladder` | **5 / 5** | Mastery ladder | **92 / 96 (full)** |
| `#s-keynote` | 5 / 5 | Mastery ladder | 92 / 96 |

`#s-keynote` is not a rail stage, so the `IntersectionObserver`
(`rootMargin: '-45% 0px -50% 0px'`, lines 720–730) never fires for it and the bar stays pinned at
5/5 for the whole tail of the page. So a student under 1340px reads a complete progress bar having
answered nothing, and the side rail — which does read completion — is the variant they cannot see.
Still Finding F2, now on the reference screen for 50 lessons.

### 2.3 Anchors

**All 8 id-bearing sections carry `scroll-margin-top: 92px`**, authored individually as an inline
style on each (`s-hook`, `s-bench`, `s-rule`, `s-wall`, `s-fit`, `s-think`, `s-ladder`,
`s-keynote`). The rail references **5 of the 8** — `s-rule`, `s-think` and `s-keynote` are anchored
but unlisted. `.ks3-layer`, `.ks3-endmatter` and `.ks3-legal` carry none.

Verified by driving: clicking the side rail's WALL link at 1340 puts `#s-wall` at
**top: 92.48px** with `location.hash = "#s-wall"`. `scroll-behavior` resolves to `auto` (no smooth
scroll authored). The 92px clears the 46.59px sticky bar with a 45.4px margin under 1340, and clears
nothing in particular at 1340+ where the bar is hidden — the same single value serves both, as
b1-01 recorded.

### 2.4 What the generator needs to emit it

Identical shape to b1-01 §2.6, five entries:

```python
"rail": [                                     # NEW field, §5 gap G1
  {"anchor": "s-hook",   "short": "HOOK",   "label": "The parts list",
   "done_when": "committed"},
  {"anchor": "s-bench",  "short": "BENCH",  "label": "The bench",
   "done_when": "gate_answered"},
  {"anchor": "s-wall",   "short": "WALL",   "label": "Wall or membrane",
   "done_when": "answers_opened"},
  {"anchor": "s-fit",    "short": "BUILD",  "label": "Fit the cell",
   "done_when": "all_specimens_run"},
  {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
   "done_when": "ladder_complete"},
]
```

`short` is ≤6 chars on both pages (HOOK/BENCH/WALL/BUILD/LADDER, TESTS/SORT) — worth asserting
rather than assuming, because the 104px rail column at MONO 11px `.09em` is what sets the limit.
`scroll-margin-top: 92px` must be emitted on **every** id-bearing section, not only rail stages.

---

## 3. Every block in document order

`GEN?` — **E** the generator has this block type · **E★** existing type, but this page uses it in a
shape the renderer cannot produce · **N** new. Component names in the last column are
`ks3_parity.COMPONENTS` entries (60 registered) that would gate it.

| # | Block | GEN? | States | Gating components |
|---|---|---|---|---|
| 1 | `header.ks3-lesson-head` — eyebrow "Cells and organisation · Model", h1, `.ks3-bigq`, `.ks3-review-flag` | **E** | draft flag present / absent (`showDraft` prop) | lesson title (row 1) · big question (row 2) · eyebrow (row 6) · draft badge |
| 2 | `#s-hook` — ink-dark: eyebrow, h2, prompt, **7 numbered dark part tiles**, then `.ks3-hook-commit` with `.ks3-commit`, 4 `.ks3-option`s, gated `.ks3-reveal` | **E★** | option resting / chosen (border → `--ks3-alert`); reveal hidden / shown | hook is ink-dark, accent shadow · dark-block option resting/CHOSEN (+badges) |
| 3 | `#s-bench` — **the MODEL flagship** (§3.2) | **N** | 2 specimens × 2 views × 2 stains × 7 parts × gate open/closed | activity option resting/CHOSEN (+badges) for the gate; **everything else unregistered** |
| 4 | `#s-rule` — statement panel: `--ks3-band`, `3px --ks3-ink`, eyebrow, `clamp(28px,3.9vw,44px)` statement at `26ch`, MONO sub-line, **2 cream cards each holding a chip list** | **N** | static | none (closest: standard block shell) |
| 5 | `#s-wall` — **the 2-way sorter that marks** (§3.4) | **N** | per-row unset / set; locked / unlocked; answers open; **per-row right / wrong** | none |
| 6 | `#s-fit` — **the build-and-run practical** (§3.5) | **N** | 4 specimens × 2⁷ installs × (unrun / fails / waste / works) | sim canvas + system-parts canvas gate `practical` today, and neither exists here |
| 7 | `#s-think` — misconception carrying **two statements and two KEY FACT boxes** (§3.6) | **E★** | static | misconception is amber |
| 8 | `#s-ladder` — `class="ks3-ladder"`, head + score, 2 page-marked rungs, 2 self-marked rungs, `.ks3-retry-wrap` | **E** | option resting / correct / wrong / spent; feedback correct / wrong; ticks 0..4; tally not-yet / met; retry | ladder shell · ladder heading · ladder option ×6 states+badges · ladder feedback CORRECT/WRONG · page-marked rung is accent · self-marked rung is violet · R8 answer box · R8 check-my-answer button |
| 9 | `#s-keynote` — ink-dark, alert-yellow shadow, **`p.ks3-eyebrow`** + one paragraph | **E★** | static | key note is ink-dark · key note type drops to 700 |
| 10 | `.ks3-layer` — "Going further" violet stretch layer, **one bare `<p>`** | **E★** | static | stretch layer is violet |
| 11 | `.ks3-endmatter` — **4 cards**: "Before this lesson" (1 link), "Connects to" (2 links), "At GCSE this becomes" (**prose**), `.ks3-tutor` (**live `<a href="#s-bench">`**) | **E★** | static | tutor card is accent · tutor text is large-bold |
| 12 | `p.ks3-legal` — **lesson-specific safety line, no copyright line** | **E★** | static | none |

Totals: **2 blocks the generator can already produce (E)**, **6 it produces in the wrong shape
(E★)**, **4 it cannot produce at all (N)**. Three of the five rail stages sit inside N blocks.

---

### 3.1 ⭐ The generator's MODEL output versus Design's MODEL drawing, component by component

This is the point of measuring this page. MRB-203's finding was that the parity gate reported green
over 116 assertions while B1 shipped with no progress rail and a flat uniform stack, because the
gate cannot see an unregistered component. b1-03 is the family reference for 50 slots, so this
comparison is the most direct available answer to *"has the generator drifted from Design's current
MODEL drawing, or was it never at it?"*

Generated page measured at the same four viewports from
`mrbadmus_site/ks3/biology/cells-and-organisation/animal-and-plant-cells.html` (build already run),
served over HTTP from `mrbadmus_site/`. Console clean at all four.

#### 3.1.1 The verdict first

**The answer is "never at it", not "drifted".** The two pages agree almost perfectly on the values
`shared/ks3.css` owns and disagree on almost everything the *page* owns. Every block shell that
exists on both sides is pixel-identical; the page's structure, its instrument, its rhythm and its
chrome are different documents.

| Layer | Agreement |
|---|---|
| Tokens / palette | identical (bundled `shared-ks3.css` is byte-identical to `shared/ks3.css`) |
| Block shells (`.ks3-block`, `.ks3-dark`, `.ks3-hook`, `.ks3-misconception`, `.ks3-practical`, `.ks3-ladder`, `.ks3-keynote`, `.ks3-layer-body`, `.ks3-endmatter > section`, `.ks3-tutor`) | **identical to the pixel** — see the table in §3.1.3 |
| Page shell (`.ks3-main` padding/max-width, `.ks3-lesson` 960px, h1 clamp, narrow query at 34rem) | identical |
| Focus ring | identical (`3px solid #E4572E`, offset 2px) |
| Document structure | **12 blocks vs 20; no shared block sequence** |
| The flagship instrument | **absent from the generator** |
| Chrome (rail, brand, crumbs, keynote heading, endmatter, legal, tutor) | **six divergences, §3.1.4** |

#### 3.1.2 Structure: 12 blocks against 20

| | Design (12 children of `.ks3-lesson`) | Generator (20 children) |
|---|---|---|
| 1 | `header.ks3-lesson-head` | `header.ks3-lesson-head` |
| 2 | `#s-hook` (hook **+ commit + reveal in one block**) | `.ks3-hook` (hook prose only, ends on a `.ks3-commit` `<p>` with no buttons) |
| 3 | `#s-bench` — the flagship | `.ks3-check` `whats-holding-it-up` |
| 4 | `#s-rule` | `.ks3-explainer` |
| 5 | `#s-wall` | `.ks3-figure.ks3-figure-pending` |
| 6 | `#s-fit` | `.ks3-misconception` `wall-or-membrane` |
| 7 | `#s-think` (2 statements, 2 KEY FACTs) | `.ks3-explainer` |
| 8 | `#s-ladder` | `.ks3-figure.ks3-figure-pending` |
| 9 | `#s-keynote` | `.ks3-practical` `cell-parts-lab` (holds `ks3-sim data-sim="system-parts"`) |
| 10 | `.ks3-layer` | `.ks3-check` `plant-extras` |
| 11 | `.ks3-endmatter` | `.ks3-misconception` `not-all-green` |
| 12 | `p.ks3-legal` | `.ks3-figure.ks3-figure-pending` |
| 13 | — | `.ks3-keywords` (**7 flip cards**) |
| 14 | — | `.ks3-check` `part-job-cards` (**7 more flip cards**) |
| 15 | — | `.ks3-check` `compare-two-cells` (criteria button) |
| 16 | — | `.ks3-ladder` |
| 17 | — | `.ks3-keynote` |
| 18 | — | `.ks3-layer.ks3-stretch` (holds a nested explainer + check) |
| 19 | — | `.ks3-endmatter` |
| 20 | — | `p.ks3-legal` |

Consequences that are facts, not readings:

- **No block on the generated page carries an `id` or a `scroll-margin-top`.** Measured: `smt: 0`
  across every `<section>` and `<div>`; the only `id`s on the page are form-control ids
  (`ks3-sim-part-1`, `ks3-ans-…`, `ks3-crit-…`). So the rail has nothing to anchor to even once it
  exists — `rail[].anchor` requires emitting section ids first.
- **`[data-rail]` count is 0** and `[data-bench-grid]` count is 0. Neither selector appears anywhere
  in `shared/ks3.css` either (verified).
- **The generator's hook does not commit.** Design's `#s-hook` ends with 4 `.ks3-option` buttons and
  a gated reveal *inside the dark block*; the generator's `.ks3-hook` ends with a `.ks3-commit`
  paragraph and the commit itself moves to a separate light `.ks3-check` block. Law 1 and Law 4 are
  both satisfied either way; the shapes are not the same shape.
- **Three `ks3-figure-pending` slots vs one canvas.** Design carries no `<figure>` at all: its
  diagram is a live 1800×1120 `<canvas>` inside the flagship. The generator carries three dashed
  "Diagram coming soon" placeholders (`3px dashed --ks3-rule-strong`, `--ks3-inset`, `padding 52px
  24px`, r24 — measured) and no cell drawing. On the MODEL reference screen, the model is drawn;
  on the generator's MODEL page, the model is a to-do.

#### 3.1.3 Where they agree — the shells, to the pixel

Measured at 1280 on both. Identical rows omit a "delta" column because there is none.

| Shell | ground | border | radius | shadow | padding | agree? |
|---|---|---|---|---|---|---|
| `.ks3-block` | `--ks3-card` #FFFCF5 | 2px `--ks3-ink` | 28px | `5px 5px 0 #221E1B` | 30px | ✔ |
| `.ks3-dark.ks3-hook` | `--ks3-ink` | none | 30px | `6px 6px 0 #E4572E` | 32px | ✔ |
| `.ks3-dark.ks3-practical` | `--ks3-ink` | none | 30px | **`6px 6px 0 #2F5CE0`** | 32px | ✔ |
| `.ks3-dark.ks3-keynote` | `--ks3-ink` | none | 30px | `6px 6px 0 #FFC53D` | 32px | ✔ |
| `.ks3-misconception` | `--ks3-alert-tint` #FFF3D4 | 2px `--ks3-ink` | 28px | `5px 5px 0 #221E1B` | 30px | ✔ |
| `.ks3-ladder` | `--ks3-card` | 3px `--ks3-ink` | 30px | `6px 6px 0 #12A150` | 32px | ✔ |
| `.ks3-layer-body` | `--ks3-stretch-tint` #F0EAFC | 2px `--ks3-stretch` | 26px | none | 26px 28px | ✔ |
| `.ks3-endmatter > section` | `--ks3-card` | 2px `--ks3-ink` | 22px | none | 22px | ✔ |
| `.ks3-tutor` | `--ks3-accent` | 2px `--ks3-ink` | 22px | none | 22px | ✔ |
| `.ks3-legal` | — | border-top **1px** `--ks3-rule` | — | — | 16px 0 0 | ✔ |
| `.ks3-rung` | — | border-left 4px `--ks3-accent` | — | — | 0 0 0 22px | ✔ |
| `.ks3-rung-self` | — | border-left 4px `--ks3-stretch` | — | — | 0 0 0 22px | ✔ |
| `.ks3-answer` | `--ks3-card` | 2px `--ks3-option-border` | 16px | — | 16px 18px, min-height 136px | ✔ |
| `.ks3-check-btn` | `--ks3-band` | 2px `--ks3-ink` | 14px | — | 13px 20px | ✔ |
| `.ks3-option` (light) | `--ks3-ground` | 2px `--ks3-option-border` | 16px | — | 16px 18px, min-height 44px | ✔ |
| `.ks3-ladder .ks3-option` | `--ks3-ground` | 2px `--ks3-option-border` | **15px** | — | **15px 17px** | ✔ |
| `.ks3-footer` | `--ks3-card` | border-top 2px `--ks3-ink` | — | 24px | — | ✔ |

That list is the substance of "where Design drew the screen, the build is right" — the shells came
from Design's artifacts and they are exact. The list below is what the registry could not see.

#### 3.1.4 Where they diverge — chrome, ten items measured

| # | Component | Design (b1-03) | Generator | Verdict |
|---|---|---|---|---|
| D1 | **Progress rail** | 2 variants, 5 stages, threshold 1340 | **absent** (0 `[data-rail]`) | new component, §7.1 |
| D2 | **Nav brand mark** | 34×34 `--ks3-accent` rounded-10px tile with a `#FBF3E6` chevron 20×20 inside, then wordmark. `a` 180.97×35.19 | **bare `#E4572E` chevron SVG 30×30, no tile** (measured: `.ks3-brand span` absent), then wordmark. `a` 176.97×35.19 | ⚑ **Design diverges from MRB-197's own ruling**, which says "a single bold `#E4572E` chevron + wordmark" — the generator's version. Design's tile inverts it (cream stroke on accent). Finding F15, for Design |
| D3 | **Breadcrumb** | body-font 17px/22.1, gap 9px, `--ks3-accent-text` 600 links, **inline in `nav.ks3-nav`** behind a 2px divider | `nav.ks3-crumbs` **inside `<main>`**, MONO 14px/400 `--ks3-ink-muted`, gap 6.4px, `margin 0 0 24px`, `.ks3-crumb-sep` | b1-01's F1, unchanged |
| D4 | **Keynote heading** | `<p class="ks3-eyebrow">Key note</p>` → Bricolage 30px/**700** uppercase **`--ks3-alert` #FFC53D** (caught by `.ks3-keynote p`) | `<h2>Key note</h2>` → Bricolage 30px/**800** sentence case **`--ks3-on-dark` #FBF3E6** | different element, weight and colour. Finding F16 |
| D5 | **Ladder `h2` line-height** | `class="ks3-ladder"` alone → `.ks3-block h2` misses → **36px / 57.6px (1.6)** | `class="ks3-block ks3-ladder"` → `.ks3-block h2` hits → **36px / 43.2px (1.2)** | ⚑ b1-01 §8 said the two class sets "resolve to the same painted shell". The **shell** is identical (verified above); the **type is not**. 14.4px per line. Finding F17 |
| D6 | **Rung `h3` line-height** | 23px / **36.8px (1.6)** | 23px / **26.45px (1.15)** | caused by `shared/styles.css` (§1.5). Finding F14 |
| D7 | **Endmatter cards** | **4**: Before this lesson (1 link) · Connects to (2 links) · At GCSE this becomes (**prose**) · tutor | **3**: Before this lesson (1 link) · At GCSE this becomes (**link list**) · tutor. No "Connects to" | `references` is unrendered; `ks4_links` renders as links where Design writes prose. Gaps G10, and `references` needs a card |
| D8 | **Tutor CTA** | `<a class="ks3-tutor-cta" href="#s-bench">Ask about this lesson</a>`, 18px/600, r12, `--ks3-card` on `--ks3-accent-text`; heading "Ask Mr Badmus AI"; line "Still not sure which parts are the plant's?" | `<span class="ks3-tutor-cta">Start a question →</span>`, **no href**, 16px/700; heading "Stuck? Ask Mr Badmus AI"; generic line | b1-01's F12, unchanged. Design's anchor points at its own flagship |
| D9 | **Legal line** | lesson-specific **safety** line ("A cheek cell sample is your own only… Methylene blue stains skin, clothes and benches") | fixed **copyright/provenance** line | both are 15px/22.5 `--ks3-ink-muted` on a 1px `--ks3-rule` top border, and **only one can occupy the slot**. Gap G11 needs a ruling, not just a field |
| D10 | **Stretch layer** | `class="ks3-layer"`, body = one bare `<p>` 19px/32.3 | `class="ks3-layer ks3-stretch"`, body = **2 nested blocks** (`.ks3-explainer` + `.ks3-check`) | shell identical; contents are a different composition |

#### 3.1.5 The flagship: Design's canvas bench versus the generator's `system-parts` sim

Both pages put a cell-parts instrument on the page. They are not the same instrument, and the
difference is measurable rather than editorial.

| | Design `#s-bench` | Generator `.ks3-sim[data-sim="system-parts"]` |
|---|---|---|
| Block | `ks3-block` (light, `--ks3-card`) | inside `ks3-block ks3-dark ks3-practical` |
| Drawing | `<canvas width="1800" height="1120">` displayed at **630×398 CSS** → ~2.86 device px per CSS px, drawn via `ctx.setTransform(2,0,0,2,0,0)` over a 900×560 diagram space | `<canvas width="560" height="220">` displayed at **896×354 CSS** → **0.625 device px per CSS px** |
| Consequence | crisp at 1× and at 2× | **upscaled 1.6× and soft at 1×**; measurably not retina |
| Frame | `2px --ks3-ink`, `--ks3-r-card` 22px, cream, with a MONO caption strip inside the frame on `--ks3-band` behind a `2px --ks3-rule` top border | `2px --ks3-on-dark-muted`, r20, `--ks3-inset`, caption *outside* the frame at 17px body |
| Content | two real specimens drawn from data: rounded-rect leaf cell with wall/inner wall/vacuole/13 chloroplasts/4 mitochondria/nucleus with nucleolus; blob cheek cell with 8 mitochondria; a ×400 field view with a circular aperture clip and 25 tiled cells (leaf) or 5 blobs (cheek); optional methylene-blue stain | an abstract dependency graph of 7 named part nodes |
| Controls | 4 specimen/view tabs + 1 conditional stain button + 7 part buttons (16 controls total when the stain is offered) | one `data-controls="part"` selector, built by JS (`.ks3-sim-controls` measured empty in HTML, `n: 1`) |
| Locked state | the **"Down a school microscope" tab** is `disabled`, `opacity .45`, `cursor default` until the gate is answered; the canvas itself is never veiled | **R5 exactly**: canvas `filter: blur(2px) saturate(0.65)`, an 85%-alpha `--ks3-card` veil (`.ks3-sim-cover`, r20, padding 16px) carrying "Make your prediction first — then the lab runs.", controls collapsed to 0×0, caption fully readable |
| Marking | none (§4) | none |

Two things follow. First, **the generator's R5 lock is better than the reference screen's** — a
blurred-and-veiled canvas with a readable caption is what R5 asks for, and Design's page gates a
*view tab* at 45% opacity instead. Code should not "fix" Design's page to match (the page wins), but
the R5 component must not be deleted when the bench replaces the sim. Second, **`practical` currently
maps to `sim canvas` + `sim live figure is mono` in §10.2, and neither component exists in Design's
practical block.** `#s-fit` is a `ks3-practical` with no canvas at all. So §10.2's `practical` row is
already stale against the approved MODEL screen.

#### 3.1.6 Flip cards — the task's item D, answered

**Design's MODEL reference screen contains no flip cards.** Measured on the reference page:
`document.querySelectorAll('[aria-expanded]').length === 0` and
`document.querySelectorAll('.ks3-cards, .ks3-card-btn').length === 0`. There is no `keyword` block,
no `.ks3-keywords`, and no card that opens.

So "cream vocabulary cards two-up" describes **`#s-rule`'s two static cards**, and the phrase is
literally accurate about them: `--ks3-card` #FFFCF5 ground (cream), `2px --ks3-ink`,
`--ks3-r-card` 22px, `padding 20px 22px`, in `repeat(auto-fit, minmax(280px, 1fr))` gap 16px inside
an 890px inner width → **exactly 2 up at 1280 (437 + 437)**, 2 up at 820 (343 + 343), 1 up at 390
(288). They hold a MONO 14px `.07em` label ("In both · 4" `--ks3-ink-muted`; "Plant only · 3"
`--ks3-accent-text`), a wrapped chip list, and an 18px/1.55 `--ks3-ink-body` close paragraph. They
carry **no `aria-expanded`, no cursor, no hover, no dog-ear.** They are reference, not affordance.

The generator's flip cards, measured for the comparison (14 of them, in two `.ks3-cards` sets):

| Property | Value |
|---|---|
| grid | `repeat(auto-fit, minmax(268px, 1fr))`, gap 16px → **3 up at 1280** (309.33 each), 3 up at 1340, 2 up at 820 (378), 1 up at 390 (322) |
| card resting | `--ks3-card`, `2px --ks3-option-border`, r22, `padding 22px`, `min-height 150px`, `box-shadow 4px 4px 0 #E0D2B9` (`--ks3-shadow-card`) |
| dog-ear | `::after`, `content ""`, absolute top/right 0, `border-top: 26px solid var(--ks3-accent)` + `border-left: 26px solid transparent`, `border-top-right-radius: var(--ks3-r-panel)` |
| front | Bricolage 27px/800 |
| hint | "Say it, then tap →" 16px/700 `--ks3-accent-text`, arrow is an inline `svg.ks3-mark` |
| open | `aria-expanded="true"`, back's `hidden` attribute removed, ground → `--ks3-accent-tint`, border → `--ks3-accent`, **dog-ear `border-top-color: transparent`** (`shared/ks3.css:469`), hint `display:none` |
| truth of state | **`aria-expanded`** — measured `false` → `true` → `false` across tap, and the `hidden` attribute tracks it |
| narrow | `.ks3-cards { grid-template-columns: 1fr }` and `.ks3-card-btn { min-height: 0 }` at 34rem — card drops to 125.78px tall at 390 |

R4's three clauses check out on the generator: the dog-ear **is** the only affordance, it **is**
removed on open (via colour, not width — a probe that reads `::after` width will see 26px both
ways), and there is no hover reveal and no auto flip. The fourth clause, *"one tap flips one
card"*, is ambiguous, and the generator reads it as "a tap affects only the card tapped": measured
two cards open simultaneously (`['true','true','false']`). Whether R4 also means *at most one open
at a time* cannot be settled from Design's delivery, because **the MODEL reference screen has no
flip card to arbitrate it.** Ambiguity for Design, §8(a).

---

### 3.2 `#s-bench` — "One cell, two organisms, two ways of looking", the MODEL instrument

The MODEL spine (`architecture.md` 991–995) asks for a *"flagship parameter instrument with
predict-gates at each regime change → property blocks each anchored back to the model"*. This is it,
and it is the single largest new component in the B1 inventory.

**What the student manipulates.** Four affordances in three groups.

1. **Specimen tabs** — 2 buttons (`Cheek cell · Leaf cell`), styled by `seg(on, false)`:
   17px/700, `padding 11px 17px`, `min-height 44px`, `border-radius var(--ks3-r-control)` 14px,
   `2px` border. **On-state is an ink fill**: `background --ks3-ink`, `border --ks3-ink`,
   `color --ks3-on-dark`. Off: `--ks3-card` on `--ks3-option-border`. `aria-pressed` carries it.
2. **View tabs** — 2 buttons (`The textbook drawing · Down a school microscope`), same `seg()`.
   The scope tab is `disabled` with `opacity:.45; cursor:default` **until the gate is answered**
   (measured both states).
3. **The stain button** — 1 button, and it **materialises and vanishes**: `stainOffered = scope &&
   specimen === 'cheek'`. Measured: 11 `[aria-pressed]` buttons on leaf+scope, **12** on
   cheek+scope, with a third MONO control label "Stain" appearing beside "Specimen" and "Looking at
   it". Label carries the state in words — "Add methylene blue" → "Methylene blue — on".
4. **The part list** — 7 full-width buttons in a `flex column, gap 8px` inside the 240px control
   column. Each is `min-height 56px`, `padding 11px 13px`, `--ks3-r-option` 16px, gap 11px, with a
   32×32 r10 Bricolage-16px/800 number tile, a 17px/700 lh 1.25 name, and a MONO 13px `.04em`
   uppercase tag underneath.

**Part-button states — three, all measured, all carrying a word:**

| State | ground | border | number tile | name | tag text | tag colour |
|---|---|---|---|---|---|---|
| present, in both | `--ks3-ground` | `--ks3-option-border` | `--ks3-band` / `--ks3-ink-muted` | `--ks3-ink` | "In both" | `--ks3-ink-muted` |
| present, plant only | `--ks3-ground` | `--ks3-option-border` | `--ks3-band` / `--ks3-ink-muted` | `--ks3-ink` | "Plant only" | `--ks3-accent-text` |
| absent from this specimen | **`--ks3-row-dim`** #FBF6EC | `--ks3-option-border` | `--ks3-band` / **`--ks3-ink-ghost`** | **`--ks3-ink-faint`** | **"Not in an animal cell"** | `--ks3-ink-ghost` |
| selected (any of the above) | `--ks3-accent-tint` | `--ks3-accent` | `--ks3-accent` / `--ks3-on-dark` | unchanged | unchanged | unchanged |

R2 is satisfied — every state carries a word as well as a tone. Note the **asymmetry in the
absent-part guard**: switching to Cheek resets `part` to `nucleus` if the current part is
wall/vacuole/chloroplasts (line 1090), but a part that is absent **can still be selected** while on
Cheek. Measured: clicking Chloroplasts on Cheek gives `aria-pressed="true"` with the full
accent-tint/accent selected treatment, and the readout switches to its absent variant. That is
better behaviour than the guard, not worse — the readout then teaches *"An animal cell does not have
it, and that is not a fault"* — but the two paths disagree about whether an absent part is
selectable.

**The predict gate.** An inset panel above the grid: `--ks3-inset` #F7EFE1, `2px --ks3-ink`,
`--ks3-r-panel` 20px, `padding 20px 22px`, `margin-top 20px`, `data-arrive="1"`. Question 20px/700
lh 1.6. Four `.ks3-option`s in a `repeat(auto-fit, minmax(180px, 1fr))` grid gap 11px → **4 up at
1280/1340** (203.75 each), 3 up at 820, 1 up at 390.

Answering it does three things at once, measured: the gate **leaves the DOM entirely**, `view` is
**force-switched to `'scope'`**, and the scope tab loses `disabled`. Two consequences:

- b1-01's **F4 reproduces** — the student cannot see or revise what they predicted. Worse here,
  because the gate's own answer (5 of 7) is delivered only obliquely, in the tally line.
- **The gate is never marked** (R3 respected): choosing A "All seven" and C "Three of them" produce
  identical UI, and `gateOptions` carries no `correct` field at all. What answers it is the tally
  changing to `7 parts in this cell · 5 of them visible at ×400`. Whether a student connects the two
  is not stated on the page.

**The readout panel** — `margin-top 16px`, `padding 22px 24px`, `--ks3-r-panel`:

| State | ground | border |
|---|---|---|
| part present in this specimen | `--ks3-inset` | `2px --ks3-ink` |
| part absent | `--ks3-row-dim` | `2px --ks3-rule-strong` |

Head row (`flex, gap 12px, wrap`): a 36×36 r11 `--ks3-accent` / `--ks3-on-dark` Bricolage-18px/800
number tile; the part name in Bricolage **25px/800 ls −.02em**; then a pill —
`padding 5px 11px`, r999, `2px --ks3-ink`, MONO 14px `.06em` uppercase — reading **"In both cells"**
(`--ks3-band`), **"Plant cells only"** (`--ks3-accent-tint`) or **"Not in this cell at all"**
(`--ks3-band`). Then `job` 20px/600 lh 1.55 and `detail` 18px/1.6 `--ks3-ink-body`.

**The scope note** is a fourth paragraph that exists only when `scope && present`, and it is the
one place in the instrument that takes a tone:

| `part.visible` | ground | border | lead word (Bricolage) |
|---|---|---|---|
| `true` | `--ks3-card` | `2px --ks3-rule-strong` | "You can see this one." |
| `false` | **`--ks3-alert-tint`** | **`2px --ks3-alert-border`** | "You cannot see this one." |

Measured both, on Chloroplasts and on Mitochondria. `padding 15px 17px`, `--ks3-r-panel`,
18px/1.55 `--ks3-ink-body`, animated with `b3-arrive`.

**The caption and the tally** are authored per combination, not derived. Caption (MONO 14px,
`--ks3-ink-muted`, on `--ks3-band` inside the frame behind `2px --ks3-rule`, `padding 11px 16px`) has
**4 variants**; the tally line (MONO 16px `--ks3-ink-muted`) has **5**, all measured:

| specimen · view · stain | caption | tally |
|---|---|---|
| leaf · diagram | "Leaf cell, drawn as a slice through the middle. A real cell is a box, not a rectangle." | "7 parts in this cell · 4 shared with you · 3 the plant's own" |
| leaf · scope | "Leaf tissue, ×400. Real slides are crowded — you never get one cell on its own." | "7 parts in this cell · 5 of them visible at ×400" |
| cheek · diagram | "Cheek cell, drawn flattened. In your mouth it is a soft, irregular bag." | "4 parts in this cell · every one of them is in a leaf cell too" |
| cheek · scope · unstained | "Cheek cells, ×400. Unstained: almost nothing to see." | "4 parts in this cell · 2 of them visible at ×400 — and only once it is stained" |
| cheek · scope · stained | "Cheek cells, ×400. Stained with methylene blue." | "4 parts in this cell · 2 of them visible at ×400" |

`canvasAlt` likewise has **4 authored variants**, one per specimen × view, each a full sentence
describing the drawing. That is R6-grade alt text and it must survive the port verbatim.

**State scope.** `specimen`, `view`, `stain` and `part` are all single scalars on the component —
unlike b1-01's board, which kept independent state per specimen. Switching specimen therefore
carries the current part across (measured: Chloroplasts selected on Cheek stays selected when you
return to Leaf), and switching away and back does not reset the view or the stain.

### 3.3 The bench grid — the task's item B, measured

`[data-bench-grid]` is declared at source line 20 and collapsed at line 21:

```css
[data-bench-grid] { grid-template-columns: minmax(0, 240px) minmax(0, 1fr); }
@media (max-width: 780px) { [data-bench-grid] { grid-template-columns: minmax(0, 1fr); } }
```

**As delivered** (`gap 22px`, `align-items: start`), bisected:

| viewport | resolved columns | canvas CSS width | `#s-bench` height |
|---|---|---|---|
| 1280 | `240px 634px` | 630 | 1356.59 |
| 1340 | `240px 634px` | 630 | 1356.59 |
| 900 | `240px 526px` | 522 | 1390.78 |
| 820 | `240px 446px` | 442 | 1476.38 |
| 800 | `240px 426px` | 422 | 1463.92 |
| **781** | `240px 407px` | 403 | 1503.30 |
| **780** | `668px` (single) | 664 | **2149.23** |
| 390 | `318px` (single) | 314 | — |

So the two columns survive to 781 and collapse at 780, exactly as authored.

#### Applying drift 1 (232px) to this page

Injected `[data-bench-grid] { grid-template-columns: minmax(0,232px) minmax(0,1fr) }` and
re-measured:

| viewport | columns | canvas | `#s-bench` height | longest name wraps? | longest tag wraps? |
|---|---|---|---|---|---|
| 1280 | `232px 642px` | 638 (+8) | 1361.56 (+4.97) | no | no |
| 900 | `232px 534px` | 530 (+8) | 1395.75 (+4.97) | no | no |
| 820 | `232px 454px` | 450 (+8) | 1481.36 (+4.98) | no | no |
| 800 | `232px 434px` | 430 (+8) | 1468.91 (+4.99) | no | no |

**Verdict: drift 1 is safe on b1-03.** The 8px comes off the control column and goes onto the
canvas; the block grows ~5px taller because the canvas keeps its 900:560 aspect ratio. No part
button changes height (every one stays 70.05px), no name wraps to a second line, no tag wraps. The
longest strings in the column are "Cell membrane"/"Mitochondria"/"Chloroplasts" (names) and "Not in
an animal cell" (tag), and all clear 232 − 26 (padding) − 32 (tile) − 11 (gap) = 163px of text
width. **No reason to reopen the ruling.**

#### Applying drift 2 (820px) to this page

Injected a `max-width: 820px` collapse on top of the 232px column:

| viewport | columns | canvas | `#s-bench` height | vs as-delivered |
|---|---|---|---|---|
| 821 | `232px 455px` | 451 | 1481.97 | — |
| **820** | `708px` (single) | **704** | **2114.33** | **+637.95px taller** |
| 800 | `688px` | 684 | 2101.89 | +637.97 |
| 781 | `669px` | 665 | 2149.86 | +646.56 |

**Verdict: drift 2 is also safe on b1-03, and it is a large visible change in the 781–820 band.**
Nothing wraps, nothing overflows, no control loses its 44px tap target. What happens is that between
781 and 820 the bench block becomes **43% taller** and the cell drawing goes from 442px wide to
704px wide — which is the "kinder at 800px" outcome `00-delivery-drift.md` argued for, quantified.
The trade is a page that is ~640px longer in that band. At 820 specifically, the document grows from
9525 to roughly 10163 (arithmetic from the block delta; the whole-document height was not
re-measured under the patch).

**Neither ruling is reopened by this page.** Both apply cleanly. Drift 2's cost is bigger than the
drift document implies, because b1-03's canvas is aspect-ratio-locked and doubles the block's
height when it goes full width — so the ruling should be applied knowing that, not as a
one-number change.

One thing the rulings do **not** cover: this page's bench grid has **`gap: 22px`** and
**`align-items: start`** inline (line 186), and b1-04/b1-06's gaps were not measured here. If the
generator owns `[data-bench-grid]` it owns those two too, and they need the same reconciliation.

### 3.4 `#s-wall` — "Wall or membrane?", the sorter that marks

Five statements, two categories. `<ul>` is `flex column, gap 11px, margin-top 20px`.

- **Row** `padding 18px 20px`, `--ks3-r-panel` 20px. Statement 19px/600 lh 1.5.
- **Chips** — 2 per row (`Cell wall · Cell membrane`), `flex, gap 9px, wrap`, 16px/700,
  `padding 10px 16px`, `min-height 44px`, `--ks3-r-control` 14px. Chosen `--ks3-accent-tint` on
  `2px --ks3-accent`; unchosen `--ks3-ground` on `2px --ks3-option-border`. `aria-pressed` carries it.
- **Footer** `flex, gap 16px, wrap, margin-top 20px`: `.ks3-reveal-btn` "Open the answers" (17px/700,
  `padding 14px 22px`, 44px, r14, `--ks3-ink` fill, `--ks3-on-dark` text) plus a MONO 15px
  `--ks3-ink-muted` progress line **"N of 5 sent"**.
- **Locked state**, measured at 4/5: `disabled` attribute present, `opacity .45`,
  `cursor: default`. Clicking it while locked is a verified no-op (no `[data-arrive]` answer
  appeared). At 5/5 the attribute is gone, `opacity 1`, `cursor pointer`.

**Pressing it reveals per-row evidence AND marks each row right or wrong.** This is the sharpest
finding on the page. Measured with rows 2, 4 and 5 deliberately wrong:

| Row state after reveal | ground | border | any word or mark? |
|---|---|---|---|
| chosen category **correct** | `--ks3-inset` #F7EFE1 | `2px --ks3-ink` | **none** |
| chosen category **wrong** | **`--ks3-alert-tint` #FFF3D4** | **`2px --ks3-alert-border` #D9821A** | **none** |
| before reveal | `--ks3-card` | `2px --ks3-rule-strong` | — |

The chips themselves are byte-identical in both cases (`--ks3-accent-tint` on `--ks3-accent`,
measured on a correct and a wrong row) — so the *button* obeys R3 while the *row it sits in* does
not. And the row wash is the **only** signal: the evidence line reads
`<strong>Cell wall.</strong> …` (Bricolage 800 18px, `--ks3-ink-body`) — the correct answer and its
reason — and never refers to what the student chose. Three rules are in tension at once:

- **R2** — "Colour is never the only signal… Every state survives being printed in greyscale."
  Right and wrong here differ **only** by ground and border colour.
- **R3** — "Activity buttons never mark correctness. Green and red must not appear on an activity
  button." The button doesn't; the row does, in amber.
- **`README.txt`** — "Amber is reserved for misconceptions." This is not a misconception block.

Also measured: **choices stay changeable after the reveal, and the row re-marks live.** Flipping
row 1 from "Cell wall" to "Cell membrane" turned it from `--ks3-inset` to `--ks3-alert-tint`
immediately. A student can therefore chase the colour to "all five pale" without reading a word of
the evidence — which is the exact failure mode R3 exists to prevent. Finding F18.

Beneath the rows, an ink panel (`data-arrive`, `--ks3-ink`, `--ks3-r-panel`, `padding 22px 24px`)
with a Bricolage 26px/800 headline "The wall is the box. The membrane is the door." and a 19px/1.6
`--ks3-on-dark-body` paragraph. Same shape as b1-01's board verdict.

### 3.5 `#s-fit` — "Fit the cell to the job", the build-and-run practical

Four real cells, seven installable parts, three verdict outcomes. The block is `ks3-block ks3-dark
ks3-practical`.

- **Head row** `flex, align-items: flex-end, space-between, gap 20px, wrap`: eyebrow "Build it"
  (`--ks3-blue-light`), `h2` **34px/800 lh 1.12 ls −.03em** `--ks3-on-dark` (an inline size, not
  `.ks3-block h2`'s 30px), and a right-aligned MONO 15px `--ks3-on-dark-muted` progress line
  **"N of 4 cells run"**.
- **Specimen tabs** — 4 buttons via `seg(on, **true**)`, the *dark* branch: 17px/700,
  `11px 17px`, 44px, `--ks3-r-control`; on = `--ks3-alert` fill with `--ks3-ink` text and
  `--ks3-alert` border; off = transparent on `2px --ks3-on-dark-muted` with `--ks3-on-dark` text.
  This is the only use of `seg(_, true)` on the page.
- **The job panel** — `--ks3-dark-panel` #3E3730, `--ks3-r-panel`, `padding 22px 24px`: MONO 14px
  `.07em` "The job" (`--ks3-on-dark-muted`), then `job` 21px/700 lh 1.5 `--ks3-on-dark` and `where`
  18px/1.6 `--ks3-on-dark-body`.
- **Install row** — "Install the parts" 18px/700, then 7 pill buttons `flex wrap gap 10px`:
  17px/700, `padding 11px 17px`, **`min-height 48px`**, `border-radius 999px`, with a 24×24 r7
  Bricolage-14px/800 inline-grid number and `margin-right 9px`. Off = transparent on
  `2px --ks3-on-dark-muted`, number `--ks3-dark-panel`/`--ks3-on-dark-muted`. On =
  **`--ks3-alert` fill**, `--ks3-ink` text, number `--ks3-ink`/`--ks3-alert` (inverted).
- **Run row** — `flex gap 16px wrap`: "Run this cell" / "Run it again" (18px/700, `13px 22px`,
  48px, r14, `--ks3-ground` fill on a `--ks3-ground` border, `--ks3-ink` text); "Strip it back out"
  (16px/700, `10px 16px`, 44px, r14, transparent on `2px --ks3-on-dark-muted`,
  `--ks3-on-dark-body`); and a MONO 15px hint **"Install something first"** → **"N of 7
  installed"**.

⚠️ **The Run button is `disabled` while looking fully enabled.** Measured with nothing installed:
`disabled === true`, `opacity: 1`, `cursor: pointer`. The markup at line 321 hardcodes the enabled
style; `renderVals` computes a `runBtnStyle` at line 1227 that *does* carry
`opacity:.4;cursor:default` — and **nothing in the template ever references it**. Dead code, exactly
like b1-01's unused `railFillHeight`. The lock is announced only in the hint text, and the same page
gives `#s-wall`'s reveal button a proper `opacity .45; cursor default`. Finding F19; Code's call.

**The verdict panel** appears on Run, `--ks3-ground` on `--ks3-ink` text (a light panel inside the
dark block), `--ks3-r-panel`, `padding 24px`, `data-arrive`. Three outcomes, all driven:

| `status` | badge text | badge ground | headline (Bricolage 27px/800 lh 1.18 ls −.025em) |
|---|---|---|---|
| `fails` (any needed part missing) | "Fails" | `--ks3-alert-tint` | "It does not survive. One part short." / "… N parts short." |
| `waste` (nothing missing, something extra) | "Alive, but wasteful" | `--ks3-band` | "It lives — but you built something it will never switch on." |
| `works` | "Alive" | `--ks3-accent-tint` | "It works. Exactly the parts the job needs, and nothing spare." |

Badge is MONO 14px `.08em` uppercase, `padding 6px 13px`, r999, `2px --ks3-ink`, `--ks3-ink` text.
Every outcome carries a **word**, so R2 holds here even though the tone changes.

**Findings cards** (`flex column, gap 10px`, `margin-top 18px`), one per missing or extra part:

| kind | ground | border | lead word | word colour |
|---|---|---|---|---|
| missing | `--ks3-alert-tint` | `2px --ks3-alert-border` | "Missing — " | `--ks3-alert-text` |
| installed, never used | `--ks3-inset` | `2px --ks3-rule-strong` | "Installed, never used — " | `--ks3-accent-text` |

`padding 16px 18px`, `--ks3-r-panel`; part name 17px/700 `--ks3-ink`; note 18px/1.55
`--ks3-ink-body`. The missing note comes from the shared `CONSEQUENCE` map (7 entries); the extra
note from `spec.waste[id]` with a fallback string "This cell has no job that needs it."

Then a closing note behind `border-top 2px --ks3-rule; padding-top 16px`, 19px/1.6 `--ks3-ink`.

⚠️ **The closing note is unconditional, so a failed build is told the answer.** Measured: running a
palisade cell with only 4 of 7 parts produced the "Fails · 3 parts short" verdict *and* the note
"All seven. A palisade cell is a plant cell with nothing left out…". The note is `spec.note`, not a
per-status string. Finding F20 — this one has a content dimension and is flagged for Mide as well as
Design.

Also measured, and correct: editing the install set after a run **removes** the verdict
(`fitRan[spec.id]` deleted on every part toggle), and "Strip it back out" clears the set, removes
the verdict, re-disables Run, and decrements the "N of 4 cells run" counter.

### 3.6 `#s-think` — one misconception block carrying two misconceptions and **two** KEY FACT boxes

`.ks3-block ks3-misconception`: `--ks3-alert-tint`, `2px --ks3-ink`, r28, `5px 5px 0 --ks3-ink`,
`padding 30px`. Head is `.ks3-mis-head` (`flex, gap 12px`): a 32×32 r10 `--ks3-ink` badge with a
Bricolage-19px/800 `--ks3-alert` "!", then `.ks3-eyebrow` "Think again" in `--ks3-alert-text`.

The block then holds **two complete misconception statements**, the second wrapped in an unclassed
`<div>` with `margin-top 22px; padding-top 20px; border-top: 2px solid var(--ks3-alert-border)`.

⚠️ **README.txt: "One KEY FACT box per lesson."** This page has **two**, both measured, both
identical in every resolved value:

```
background: var(--ks3-band)        #F4E9D8
border: 2px solid var(--ks3-ink)
border-radius: var(--ks3-r-panel)  20px
box-shadow: 5px 5px 0 var(--ks3-accent)
padding: 18px 22px
margin-top: 24px
```

The first is a direct child of `#s-think`; the second is nested inside that unclassed `<div>`.
Finding F21 — the MODEL reference screen breaks its own delivery convention, and b1-01 §7.2's
assertion *"One per lesson — assert at most one"* would fail the build on this page.

⚠️ **A second nesting consequence, purely mechanical.** `shared/ks3.css:319` is
`.ks3-misconception > p { font-size: 19px; line-height: 1.6 }` — specificity (0,1,1) — and
`.ks3-mis-quote` (line 312) is (0,1,0). So the **direct-child** quote loses its own size and the
**nested** one keeps it:

| | measured |
|---|---|
| first `.ks3-mis-quote` (direct child of `#s-think`) | 19px / 30.4px (1.6) / 700 |
| second `.ks3-mis-quote` (inside the wrapper div) | **22px / 30.8px (1.4) / 700** |

Two quotes with the same class render at two sizes, from wrapper nesting alone. Finding F22; Code's
call (the fix is a specificity bump on `.ks3-mis-quote`, and it changes b1-01 and b1-02's quotes to
22px as well, so it needs stating in the build report).

### 3.7 The KEY FACT box, specified to generate — the task's item C

Everything below was measured on this page at all four viewports; nothing varies with viewport
except the box's own width.

**Geometry**

| Property | Value | Token? |
|---|---|---|
| `background` | `#F4E9D8` | **`--ks3-band`** ✔ agrees with drift 5 |
| `border` | `2px solid #221E1B` | `--ks3-ink` |
| `border-radius` | `20px` | `--ks3-r-panel` |
| `box-shadow` | `5px 5px 0 #E4572E` | `--ks3-accent` |
| `padding` | `18px 22px` | bare |
| `margin` | `24px 0 0` | bare |
| width | 896 (1280/1340) · 708 (820) · 318 (390) | fills its parent block's content box |
| height | 97.48 · 97.48 · 127.17 · 156.86 | content-driven |

**Type — two roles, both fixed**

| Part | family | size | weight | line-height | letter-spacing | colour |
|---|---|---|---|---|---|---|
| eyebrow "Key fact" | MONO `--ks3-font-mono` (DM Mono) | 13px | 500 | 20.8px (1.6) | **1.17px = .09em** | `--ks3-accent-text` #A93411 |
| statement | DISPLAY `--ks3-font-display` (Bricolage Grotesque) | 22px | **700** (not 800) | 29.7px (1.35) | **−0.33px = −.015em** | `--ks3-ink` #221E1B |

`text-transform: uppercase` on the eyebrow, `margin: 0`; statement `margin: 7px 0 0`.

**The eyebrow text is chrome, not data.** Both boxes read exactly "Key fact"; the only authored
value is the statement.

**The ground.** `--ks3-band`, matching five of the six pages and the ruled value. Note again that
`--ks3-band` is also the ground a **chosen-wrong** ladder option takes (MRB-202) — measured on this
page's rung 2, `is-wrong` = `--ks3-band` on `2px --ks3-ink` with an ink/on-dark ✗ badge. The KEY FACT
box's distinguishing marks are the **accent** shadow (a wrong option has none) and the absence of
any badge, letter or mark. Nothing inside a KEY FACT box may ever read as a verdict.

**States: one.** No hover, no focus, no `aria-*`, no interactivity, not focusable, and no
`data-arrive` (it is present at load, not revealed).

**Placement.** Both instances sit **inside** `#s-think`, not at `.ks3-lesson` top level as b1-01's
did, and carry no id and no `scroll-margin-top`. So placement must be expressible as a block inside
a misconception activity, not only as a `core[]` sibling — see G2.

**Statement lengths measured:** 68 and 96 characters. b1-01's was 62. A ≤~140-char budget holds.

### 3.8 The stretch layer, the endmatter and the safety line

- **`.ks3-layer`** — `.ks3-layer-head` is `flex, gap 14px, margin-bottom 16px` with the eyebrow
  "Going further" and a `.ks3-layer-rule` hairline (2px tall, `--ks3-stretch-rule` #D8CBF5, 813.73
  wide at 1280). Body `--ks3-stretch-tint` on `2px --ks3-stretch`, r26, `padding 26px 28px`, holding
  **one bare `<p>`** at 19px / 32.3px (1.7).
- **`.ks3-endmatter`** — `repeat(auto-fit, minmax(250px, 1fr))`, gap 16px, at the full 960px →
  **3 columns for 4 cards** at 1280/1340 (309.33 each, the fourth wrapping), 2 at 820 (378), 1 at
  390. Card `h2` Bricolage 21px/800 lh 1.25 ls −.01em. Links 18px/600 `--ks3-accent-text` with an
  inline `svg.ks3-mark.ks3-mark-arrow`. Prose 18px/1.5 `--ks3-ink-body`.
- **`p.ks3-legal`** — 15px / 22.5px `--ks3-ink-muted`, `border-top: 1px solid --ks3-rule`,
  `padding-top 16px`, `margin-top 34px`. On this page it is a **safety line about methylene blue and
  cheek swabs**, and there is no copyright line anywhere on the page.

---

## 4. Interactive behaviours

All 18 driven in the browser. **The DC-runtime settle trap applies and this page adds a second
edge:** b1-01 recorded that a 450ms settle is needed because the runtime re-renders
asynchronously. On this page every revealed element also runs
`animation: b3-arrive .34s ease-out **both**`, and `both` means the 0% keyframe (`opacity: 0`)
holds before the animation starts. Measured: one read taken ~450ms after a click returned
`opacity: 0` on a freshly revealed scope note that was fully opaque on the next read. **Settle must
exceed the runtime re-render plus 340ms**, or a real element measures as invisible.

| # | Trigger | What changes | Notes |
|---|---|---|---|
| 1 | Click a hook option | `aria-pressed="true"`; border → `--ks3-alert`, badge → `--ks3-alert`/`--ks3-ink`, ground stays `--ks3-dark-panel`; `.ks3-reveal` appears (`--ks3-dark-panel`, `2px --ks3-alert`, r18) | **Re-choosable** (measured: choosing D moves the state off B), never disabled, never marked. Rail stage 1 ticks |
| 2 | Click a specimen tab | Canvas redraws; part tags/greys swap; readout, caption, tally and `canvasAlt` all change; a plant-only part selected on Cheek is preserved | Guard at line 1090 resets `part` to `nucleus` only when switching *to* Cheek from a plant-only part |
| 3 | Click a gate option | Gate `<div>` **removed from the DOM**; `view` force-switched to `'scope'`; scope tab loses `disabled` | Irreversible, unrecorded, unmarked. Rail stage 2 ticks |
| 4 | Click a view tab | Canvas swaps drawing mode; scope note appears/disappears; caption + tally change; stain control appears iff specimen is Cheek | Scope tab is a no-op while `gate === null` (verified: `disabled` + an early `return` in `onClick`) |
| 5 | Click the stain button | `seg()` on-state (ink fill); label "Add methylene blue" → "Methylene blue — on"; nucleus redraws `#4A3C7A` at α .92 instead of `#DCD2BE` at α .6; caption and tally change | Control exists only on cheek+scope; measured 11 → 12 `[aria-pressed]` buttons |
| 6 | Click a part button | That button → `--ks3-accent-tint`/`--ks3-accent` with an accent number tile; readout head/pill/job/detail/scope-note all swap; the canvas marker ring + numbered bubble move | Marker is dashed and `#8F857B` when the part is invisible at ×400, solid `--ks3-accent` otherwise |
| 7 | Click a sorter chip | Chip → `--ks3-accent-tint`/`--ks3-accent`; "N of 5 sent" increments; row border stays `--ks3-rule-strong` until the reveal | Freely changeable; re-clicking does not double-count |
| 8 | Click "Open the answers" while locked | **Nothing** (verified: `disabled`, and `onOpenSort` re-checks the count) | `opacity .45`, `cursor default` |
| 9 | Click "Open the answers" at 5/5 | Evidence line on all five rows at once **and** every row washes right (`--ks3-inset`/ink) or wrong (`--ks3-alert-tint`/`--ks3-alert-border`) | One-way (`sortOpen` never resets). Rail stage 3 ticks. **§3.4** |
| 10 | Change a chip after the reveal | Chips update and **the row re-marks live** (measured `--ks3-inset` → `--ks3-alert-tint`) | The evidence line does not change — it always states the correct answer |
| 11 | Click a FIT specimen tab | Job panel, install set, verdict and hint all swap to that specimen's state | `fit` and `fitRan` are keyed by specimen id, so all four builds are independent |
| 12 | Toggle a FIT part | Pill → `--ks3-alert` fill with inverted number; hint recount; **any existing verdict is removed** | Correct: `fitRan[spec.id]` is deleted on every toggle |
| 13 | Click "Run this cell" | Verdict panel appears with badge, headline, per-part findings and the closing note; "N of 4 cells run" increments; button label → "Run it again" | Disabled at 0 installed but visually unlocked — **F19** |
| 14 | Click "Strip it back out" | Install set emptied, verdict removed, Run re-disabled, **"N of 4 cells run" decremented** | Can un-earn rail stage 4 |
| 15 | Click a ladder option | Chosen wrong → `.is-wrong` (`--ks3-band` on `2px --ks3-ink`, badge ink/on-dark, drawn ✗ `M6.5 6.5l11 11M17.5 6.5l-11 11`); correct → `.is-correct` (`--ks3-ok-tint` on `--ks3-ok`, badge `--ks3-ok`/white, drawn ✓ `M5 12.5l4.6 4.5L19 7`); others → `.is-spent` (`--ks3-row-dim`, `--ks3-option-spent`, `--ks3-ink-faint`, letter kept); **all 4 `disabled`**; `.ks3-feedback` appears | Second click on the same rung: no change (score held at 1 of 4). Letters are replaced by the drawn mark **only** on the marked options |
| 16 | Type in a rung textarea, then "Check my answer" | `.ks3-ticks` appears with 4 real checkboxes (`.ks3-tick-num` MONO 15px `--ks3-ok-text`) and `.ks3-tally` "0 of 4 ticked — not yet." (`--ks3-band` on `2px --ks3-rule-strong`, `--ks3-ink-body`, r13); ticking all 4 → `.ks3-tally.is-met` "All 4 ticked — rung met." (`--ks3-ok-tint` on `--ks3-ok`, `--ks3-ok-text`) and score +1 | ⚠️ **b1-01's F8 and F9 both reproduce.** (a) Typed "TYPED-PROBE-STRING", pressed Check, measured `textarea.value === ""` — the answer is **lost on re-render**. Note the mechanism differs slightly from b1-01: the runtime **strips** the `value="{{ }}"` attribute rather than leaving it (`getAttribute('value') === null`), so the box simply re-renders empty. (b) Check on an **empty** box opens all four criteria, and ticking them scores the rung |
| 17 | Click "Retry my misses" | `answers`, `checked` and `ticks` all reset; every option re-enabled; feedback and criteria gone; score 3 of 4 → **0 of 4**; rail stage 5 un-ticks | ⚠️ **b1-01's F10 reproduces.** It clears correct answers too, and its own note says "keeps what you wrote", which it cannot honour after F8 |
| 18 | `prefers-reduced-motion: reduce` | `[data-arrive] { animation: none !important }` via the page's own query (line 24) | **There is no motion toggle on this page** — `.rd` carries no `data-motion` attribute and there are **0 `[data-anim]` elements** (measured). b1-01's toggle and its G13 do not apply here. Not separately measured under an emulated media feature; read from source |

**Score line** reads `"You got N of 4."` + `"You marked rungs 3 and 4 yourself."` Measured
0 → 1 (r1 correct) → 1 (r2 wrong) → 2 (r3 met) → **3** (r4 met). All four rungs count, so R8's
"the score reads out of 4" holds.

**Reveal animation.** Every revealed element on this page animates with **`b3-arrive`** (0.34s
ease-out both, `translateY(6px)` + opacity), including the hook reveal, which carries **both**
`class="ks3-reveal"` and `data-arrive="1"`. Measured `animationName: "b3-arrive"` — the shipped
`.ks3-reveal[data-reveal]` animation in `shared/ks3.css` never fires here because the attribute is
`data-arrive`, not `data-reveal`. Only two `@keyframes` exist on the page: `b3-arrive` and
`sc-shine` (from the DC runtime bundle). b1-01's F7 (a reveal that silently doesn't animate) does
**not** reproduce — this page is internally consistent, it just uses its own animation name and its
own attribute. The generator's `data-reveal` + `.ks3-reveal` pair produces the shipped animation.

**Keyboard and focus** (real `Tab` via `Input.dispatchKeyEvent`, 14 stops): **every control gets the
R15 ring** — `outline: 3px solid rgb(228, 87, 46)`, `outline-offset: 2px`, from
`[data-mode="ks3"] :focus-visible` — and it reaches Design's inline-styled buttons because `.rd`
carries `data-mode`. Order: brand → 3 crumb links → nav KS3 → 4 hook options → Cheek → Leaf → The
textbook drawing → 2 gate options → … The disabled scope tab is skipped. **The top rail contains 0
focusable elements; the side rail contains 5** — so under 1340px there is still no keyboard route to
a section. b1-01's F11, unchanged.

---

## 5. Schema gaps against §4.8

§4.8 (`docs/ks3/architecture.md` 449–492) is authoritative — *"Fields not listed here do not exist
without an amendment to this document."* Existing coverage first, then the gaps.

### 5.1 Already covered

| Page content | §4.8 field |
|---|---|
| h1, breadcrumb tail | `title`, `unit`, `discipline` |
| eyebrow "Cells and organisation · Model" | `unit` + `family` |
| `.ks3-bigq` | `big_question` |
| draft flag | `review_state` |
| hook eyebrow / heading / prompt / commit question + 4 options | `phenomenon` (`{kind,title,prompt,commit}`) |
| both `.ks3-mis-quote` statements | `misconceptions[].statement` — but see G8 |
| keynote paragraph | `key_note` |
| block order + types | `core[]` |
| "Going further" paragraph | `stretch[]` |
| the four rungs, options, per-option corrections, success criteria | `ladder{recall,apply,explain,produce}`. Design's per-option `correction` maps 1:1 onto the existing `feedback` dict keyed by option index |
| "Before this lesson → Using a microscope" | `requires: ["using-a-microscope"]` — **b1-01's G10 (`before_this` prose) is not needed on this page**; the card is a real link |
| "Connects to → Specialised cells, Unicellular organisms" | `references` — the field exists; the **rendering** does not (D7) |
| the seven cell parts as vocabulary | `vocabulary[{term,definition,note}]` covers term/definition, but not the page's `where`/`visible`/`scopeNote`/`mark` — see G4 |

Not surfaced on the page at all: `covers`, `touches`, `beyond_statutory`, `threads`,
`typical_year`, `typical_minutes`, `assumes`, `ws`, `support`. **`figures` is empty on this page and
that is a statement, not an omission** (§4.10: *"legitimately is, for lessons carried entirely by
interactives"*) — but see G9, because the canvas has to come from somewhere.

### 5.2 Gaps — 14, of which 7 are new to this page

| # | What the page needs | §4.8 today | Proposed field + shape | New here? |
|---|---|---|---|---|
| G1 | 5 rail stages, two label sets, completion predicates | nothing | **`rail: [{anchor, short, label, done_when}]`** (§2.4) | carried from b1-01 G2, unchanged |
| G2 | **Two** KEY FACT boxes, one nested inside a misconception activity | nothing | **block type `key-fact`** `{"type": "key-fact", "text": "…"}` — but the record must be a **list**, and it must be legal **inside** a `misconception` activity as well as in `core[]`. b1-01 G1 assumed one, at top level; F21 shows both assumptions are wrong | carried, **amended** |
| G3 | `#s-rule` statement panel: display statement at 26ch, a MONO sub-line, and 2 cream cards each holding a **chip list** | nothing | **block type `rule`** `{"type": "rule", "eyebrow": "…", "statement": "…", "sub": "…", "cards": [{"label": "In both · 4", "label_tone": "muted\|accent", "chips": ["1 · Cell membrane", …], "chip_tone": "inset\|accent-tint", "close": "…"}]}`. b1-01's G5 had `{term, gloss}` cards and no sub-line | carried, **amended** |
| G4 | The bench: 7 parts × (job, detail, visible, scopeNote, where) + per-specimen marker geometry + 4 alt texts + 4 captions + 5 tally lines | `activities[].kind` has nothing comparable | **`activities[] {kind: "cell-bench", parts: [{id, num, name, where, job, detail, visible, scope_note, mark: {specimen: [{x,y,r}]}}], specimens: [{id, label, alt: {view: str}, caption: {view: str}, tally: {view: str}}], gate: {q, options}, views: [{id, label}], extras: [{id, label_off, label_on, when}]}` | **NEW** |
| G5 | The 2-way sorter: 5 statements, 2 categories, per-row evidence, per-row right/wrong wash | `classify` cannot express rows × categories | **`activities[] {kind: "sort-pairs", categories: [{id, label}], rows: [{id, text, answer, note}], reveal_label, reveal_panel: {headline, body}, mark_rows: bool}` — `mark_rows` must be an explicit field, because whether an activity marks is an R3 decision, not a rendering detail | **NEW** |
| G6 | The build-and-run practical: 4 specimens × 7 parts, needs/waste sets, 7 consequence lines, 3 verdict statuses | `practical` maps to `sim canvas` + `sim live figure is mono` in §10.2, and this block has no canvas | **`activities[] {kind: "fit-parts", parts: [ref to G4's part ids], specimens: [{id, label, kind, job, where, needs: [id], waste: {id: note}, note}], consequence: {id: note}, verdicts: {fails, waste, works}}` | **NEW** |
| G7 | The hook's 7 numbered dark part tiles | `phenomenon` renders prose only | **`phenomenon.tiles: [{num, label}]`** — 2–8 entries. Related to b1-01's G6 (`explainer.pills`) but a different component: numbered not initialled, on the ink ground not cream, `--ks3-r-option`-family radius 14px not a pill | **NEW** |
| G8 | **Two misconceptions rendered inside one `#s-think` block**, divided by a `2px --ks3-alert-border` rule, the second carrying its own KEY FACT | `misconceptions` is a list, and the generator emits **one block per entry** (measured: two separate `.ks3-misconception` sections) | a `group` or `render_as` discriminator on `misconceptions`, or a `misconception` block that takes a list. Needs Design's word on which is intended before a field is chosen | **NEW** |
| G9 | The cell drawing: 260 lines of `<canvas>` 2D code, 4 alt texts, 28 non-palette colours, per-part marker anchors in a 900×560 diagram space | `figures[].kind` enum is `schematic \| graph \| photo \| apparatus`; a figure record carries no code binding | **`figures[].kind += "canvas-art"`** plus **`art: "<registered-art-id>"`**, e.g. `{"id": "b1-cell-bench", "kind": "canvas-art", "art": "cell-bench", "caption": "…", "status": "final"}`. b1-01's G12 proposed `css-art` for a CSS/DOM illustration; this is a different mechanism and needs its own kind | carried, **amended** |
| G10 | "At GCSE this becomes" as **prose** | `ks4_links` is a list of KS4 slugs, and the generator renders it as a link list | **`ks4_becomes: "…"`** — prose sentence. Also needs a **`references` endmatter card** ("Connects to"), which the generator does not emit at all | carried from b1-01 G9, **extended** |
| G11 | `.ks3-legal` = a lesson-specific safety line, **with no copyright line anywhere on the page** | `LEGAL_LINE` is a fixed copyright/provenance line | **`safety_note: "…"`**, **and a ruling on which line occupies the slot** — Design's page shows only the safety line, so "render both" contradicts the approved page | carried from b1-01 G11 |
| G12 | Tutor copy "Still not sure which parts are the plant's?" + CTA label + `href="#s-bench"` | generator hard-codes generic copy and a non-interactive `<span>` (deliberately, `build_ks3.py:1013`) | **`tutor: {"prompt": "…", "cta": "…", "anchor": "s-bench"}`** — but F12 (b1-01) is still unresolved | carried from b1-01 G8 |
| G13 | Keynote heading is a `p.ks3-eyebrow`, not an `h2` (D4) | the generator emits `<h2>Key note</h2>` | No field. A rendering ruling: which element the keynote's label is. Recorded so it is not mistaken for a gap | **NEW** |
| G14 | Design's page declares **four editor props** in `data-props` (line 492): `showDraft`, `railLabels`, `startSpecimen` (`leaf\|cheek`), `showScopeView` | nothing | `showDraft` maps to `review_state`. `startSpecimen` is a real authoring choice (**`activities[].start`**). `railLabels` and `showScopeView` are Design's preview switches with no student-facing meaning — and `showScopeView: false` makes rail stage 2 unreachable (§2.1). Recommend: keep `start`, drop the other three, state it | **NEW** |

**Four of these are new activity kinds or block types** (G3's `rule`, G4, G5, G6), which under
MRB-203 cannot be rendered until `ks3_parity.COMPONENTS` and §10.2 know them, and none of them can
be expressed by bending an existing kind. **G2's amendment is the one that will bite silently**: a
`key-fact` field typed as a scalar will pass review and then fail on this page.

---

## 6. Measurements

`--ks3-*` tokens in play: **60 resolvable on `.rd[data-mode="ks3"]`** (62 declared, of which
`--ks3-hue` and `--ks3-season` are scoped to index-page selectors and resolve empty here).
Enumerated by walking `document.styleSheets` and following every `CSSImportRule`. Identical to
b1-01's set — confirmed, not re-derived.

### 6.1 Shell and type

| Property | 1280 | 1340 | 820 | 390 | Token or new |
|---|---|---|---|---|---|
| root font-size / line-height | 19px / 30.4px | = | = | = | bare (matches `body.rd` rule) |
| `.ks3-main` padding | 44px 24px 90px | = | = | 28px 16px 64px | bare (ks3.css) |
| `.ks3-main` max-width | 1320px | = | = | = | `--ks3-page` |
| `.ks3-lesson` max-width | 960px | = | = | = | `--ks3-wide` |
| `nav.ks3-nav` padding / border-bottom | 14px 24px 12px / 2px `--ks3-ink` | = | = | = | bare / token |
| nav height | 63.19 | 63.19 | **63.19** | **153.97** | measured (title-length dependent, §1.3) |
| `.ks3-brand` | Bricolage 22px/800, ls −0.44px, gap 10px, tile 34×34 r10 `--ks3-accent` | = | = | = | tokens + bare |
| breadcrumb `<ol>` | 17px / 22.1px, gap 9px, w 512.67 | = | = | w 342, h 53.19 | bare |
| h1 (`clamp(44px, 6vw, 74px)`, lh .94, ls −.035em) | **74px** / 69.56 | 74px | **49.2px** / 46.25 | **44px** / 41.36 | bare |
| `.ks3-bigq` | 25px/600, lh 1.35 (33.75), `--ks3-accent-text`, max-width 24ch = 406px | = | = | 358 (column-clamped) | token colour |
| `.ks3-eyebrow` | 13px/700, ls .16em = 2.08px, uppercase | = | = | = | token colours (5 variants, §6.5) |
| `.ks3-lesson-head` | border-bottom 3px `--ks3-ink`, padding-bottom 28px, h 322.19 | = | = | = | token |
| `.ks3-review-flag` | 16px/700 `--ks3-accent-text` on `--ks3-accent-tint`, 2px `--ks3-accent`, r999, 10px 17px, 313.41×49.59 | = | = | = | tokens |
| `.ks3-footer` | 16px `--ks3-ink-muted`, `--ks3-card`, border-top 2px `--ks3-ink`, padding 24px, h 107.59 | = | = | = | tokens |
| `.ks3-legal` | 15px/22.5 `--ks3-ink-muted`, border-top **1px** `--ks3-rule`, padding-top 16px, margin-top 34px | = | = | = | tokens |

### 6.2 Block shells

| Block | radius | border | shadow | padding 1280 | padding 390 | ground |
|---|---|---|---|---|---|---|
| `.ks3-block` (`#s-bench`, `#s-wall`) | 28px `--ks3-r-block` | 2px `--ks3-ink` | `5px 5px 0 --ks3-ink` (`--ks3-shadow-block`) | 30px | 22px 18px | `--ks3-card` |
| `.ks3-dark.ks3-hook` | 30px `--ks3-r-dark` | none | `6px 6px 0 --ks3-accent` | 32px | 22px 18px | `--ks3-ink` |
| **`.ks3-dark.ks3-practical`** (`#s-fit`) | 30px | none | **`6px 6px 0 --ks3-blue`** #2F5CE0 | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-dark.ks3-keynote` | 30px | none | `6px 6px 0 --ks3-alert` | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-misconception` | 28px | 2px `--ks3-ink` | `5px 5px 0 --ks3-ink` | 30px | 22px 18px | `--ks3-alert-tint` |
| `#s-rule` (inline) | 28px `--ks3-r-block` | **3px `--ks3-ink`** | none | **34px 32px** | 34px 32px (no narrow rule) | **`--ks3-band`** |
| KEY FACT div ×2 (inline) | **20px `--ks3-r-panel`** | 2px `--ks3-ink` | **`5px 5px 0 --ks3-accent`** | **18px 22px** | 18px 22px | **`--ks3-band`** ✔ drift 5 |
| `.ks3-ladder` | 30px | **3px `--ks3-ink`** | **`6px 6px 0 --ks3-ok`** | 32px | 22px 18px | `--ks3-card` |
| `.ks3-layer-body` | **26px** | 2px `--ks3-stretch` | none | **26px 28px** | = | `--ks3-stretch-tint` |
| `.ks3-endmatter > section` | 22px `--ks3-r-card` | 2px `--ks3-ink` | none | 22px | = | `--ks3-card` (`.ks3-tutor`: `--ks3-accent`) |
| bench gate panel (inline) | 20px | 2px `--ks3-ink` | none | 20px 22px | = | `--ks3-inset` |
| bench readout (inline) | 20px | 2px `--ks3-ink` / `--ks3-rule-strong` | none | 22px 24px | = | `--ks3-inset` / `--ks3-row-dim` |
| bench scope note (inline) | 20px | 2px `--ks3-rule-strong` / `--ks3-alert-border` | none | 15px 17px | = | `--ks3-card` / `--ks3-alert-tint` |
| canvas frame (inline) | 22px `--ks3-r-card` | 2px `--ks3-ink` | none | 0 | = | `--ks3-card`; caption strip `--ks3-band` behind `border-top 2px --ks3-rule`, `11px 16px` |
| `#s-rule` card (inline) | 22px | 2px `--ks3-ink` | none | 20px 22px | = | `--ks3-card` |
| `#s-wall` row (inline) | 20px | 2px `--ks3-rule-strong` → `--ks3-ink` / `--ks3-alert-border` | none | 18px 20px | = | `--ks3-card` → `--ks3-inset` / `--ks3-alert-tint` |
| `#s-wall` reveal panel (inline) | 20px | none | none | 22px 24px | = | `--ks3-ink` |
| `#s-fit` job panel (inline) | 20px | none | none | 22px 24px | = | `--ks3-dark-panel` |
| `#s-fit` verdict panel (inline) | 20px | none | none | 24px | = | `--ks3-ground` |
| `#s-fit` finding card (inline) | 20px | 2px `--ks3-alert-border` / `--ks3-rule-strong` | none | 16px 18px | = | `--ks3-alert-tint` / `--ks3-inset` |
| hook reveal | **18px** | 2px `--ks3-alert` | none | 18px 20px | = | `--ks3-dark-panel` |
| hook part tile (inline) | **14px** | none | none | 12px 14px | = | `--ks3-dark-panel` |

Block spacing: `margin-top 28px` between all nine sections, **24px** above each KEY FACT div,
**34px** above `.ks3-layer` / `.ks3-endmatter` / `.ks3-legal`. `.ks3-rungs` gap 28px.

### 6.3 Grids

| Grid | declared | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|---|
| hook part tiles | `auto-fit, minmax(158px, 1fr)`, gap 10px | 5 cols × 171.19 (7 items → 2 rows) | = | 4 × 169.5 | 1 × 322 |
| hook options | `.ks3-options` flex column, gap 11px | 896 | 896 | 708 | 322 |
| bench control row | flex wrap, gap `22px 34px` | 2 groups (3 when the stain is offered) | = | = | wraps |
| bench gate options | `auto-fit, minmax(180px, 1fr)`, gap 11px | 4 × 203.75 | = | 3 × 212.67 | 1 × 270 |
| **`[data-bench-grid]`** | `minmax(0, 240px) minmax(0, 1fr)`, gap 22px, `align-items: start`; collapse `≤780px` | **240 + 634** | 240 + 634 | **240 + 446** | 1 × 318 |
| bench part list | flex column, gap 8px | 240 | 240 | 240 | 318 |
| `#s-rule` cards | `auto-fit, minmax(280px, 1fr)`, gap 16px | **2 × 437** | 2 × 437 | 2 × 343 | 1 × 288 |
| `#s-rule` chip list | flex wrap, gap 8px | 389 | = | = | wraps to 1 per row |
| `#s-wall` rows | flex column, gap 11px | 896 | 896 | 708 | 318 |
| `#s-wall` chip row | flex wrap, gap 9px | 852 | = | = | wraps |
| `#s-fit` tabs | flex wrap, gap 9px | 4 in 1 row | = | = | 4 rows |
| `#s-fit` part pills | flex wrap, gap 10px | 7 over 2 rows | = | 2 rows | 7 rows |
| ladder options | `auto-fit, minmax(250px, 1fr)`, gap 11px | 3 × 280.66 | = | 2 × 332.5 | **1 × 296** |
| `.ks3-endmatter` | `auto-fit, minmax(250px, 1fr)`, gap 16px | 3 × 309.33 (4 cards) | = | 2 × 378 | 1 × 358 |

### 6.4 Controls

| Control | size | radius | border | resting ground | chosen ground |
|---|---|---|---|---|---|
| `.ks3-option` (light) | 18px/600, `padding 16px 18px`, `min-height 44px` (`--ks3-tap`), gap 14px | `--ks3-r-option` 16px | 2px `--ks3-option-border` | `--ks3-ground` | `--ks3-accent-tint` + `--ks3-accent` border |
| `.ks3-option` (on `.ks3-dark`) | same | 16px | 2px `--ks3-on-dark-muted` | `--ks3-dark-panel` | same panel, border → **`--ks3-alert`**; badge → `--ks3-alert`/`--ks3-ink` |
| `.ks3-opt-mark` (light / dark) | 28×28, r9, 15px/800 | — | — | `--ks3-band`/`--ks3-ink-muted` (dark: `--ks3-on-dark-muted`/`--ks3-ink`) | — |
| `.ks3-ladder .ks3-option` | 18px/600, **`15px 17px`**, 44px; mark **27×27** | **15px** | 2px | `--ks3-ground` | §4 row 15 |
| `seg()` light (specimen / view / stain) | 17px/700, `11px 17px`, 44px | `--ks3-r-control` 14px | 2px | `--ks3-card`/`--ks3-option-border` | **`--ks3-ink` fill / `--ks3-on-dark` text — the inverted on-state, drift 4** |
| `seg()` dark (`#s-fit` tabs) | 17px/700, `11px 17px`, 44px | `--ks3-r-control` | 2px | transparent/`--ks3-on-dark-muted` | `--ks3-alert` fill / `--ks3-ink` text |
| bench part button | name 17px/700 lh 1.25, tag MONO 13px `.04em`; `padding 11px 13px`, **`min-height 56px`**, gap 11px; tile 32×32 r10 | `--ks3-r-option` | 2px | `--ks3-ground` / `--ks3-row-dim` when absent | `--ks3-accent-tint`/`--ks3-accent` |
| sorter chip | 16px/700, `10px 16px`, 44px, w 99.25/152.77 | `--ks3-r-control` | 2px | `--ks3-ground`/`--ks3-option-border` | `--ks3-accent-tint`/`--ks3-accent` |
| `#s-fit` part pill | 17px/700, `11px 17px`, **48px**; number 24×24 r7, `margin-right 9px` | **999px** | 2px | transparent/`--ks3-on-dark-muted` | `--ks3-alert` fill, number `--ks3-ink`/`--ks3-alert` |
| `#s-fit` Run | 18px/700, `13px 22px`, **48px** | `--ks3-r-control` | 2px `--ks3-ground` | `--ks3-ground` fill | **locked: `disabled` but `opacity 1`, `cursor pointer` — F19** |
| `#s-fit` Strip it back out | 16px/700, `10px 16px`, 44px | `--ks3-r-control` | 2px `--ks3-on-dark-muted` | transparent, `--ks3-on-dark-body` | — |
| `.ks3-reveal-btn` | 17px/700, `14px 22px`, 44px, `--ks3-ink` fill, `--ks3-on-dark` text | 14px | 2px `--ks3-ink` | — | **locked: `opacity .45; cursor default`** |
| `.ks3-check-btn` | 17px/700, `13px 20px`, 44px, `--ks3-band`, 2px `--ks3-ink`, `margin-top 14px` | 14px | — | — | — |
| `.ks3-retry` | 18px/700, `14px 24px`, 44px, `--ks3-ink` fill | 14px | 2px | — | — |
| `.ks3-answer` | 19px/1.6, `16px 18px`, **min-height 136px**, w 864 | 16px | 2px `--ks3-option-border` | `--ks3-card` | — |
| `.ks3-tally` | 17px/700, `11px 16px`, r13 | — | 2px `--ks3-rule-strong` → `--ks3-ok` | `--ks3-band`/`--ks3-ink-body` | met: `--ks3-ok-tint`/`--ks3-ok-text` |
| `.ks3-tutor-cta` | 18px/600 `--ks3-accent-text` on `--ks3-card`, `10px 17px` | **12px** | — | — | — |
| readout `where` pill | MONO 14px `.06em` uppercase, `5px 11px`, r999, 2px `--ks3-ink` | 999px | 2px | `--ks3-band` / `--ks3-accent-tint` | — |
| verdict badge | MONO 14px `.08em` uppercase, `6px 13px`, r999, 2px `--ks3-ink` | 999px | 2px | `--ks3-alert-tint` / `--ks3-band` / `--ks3-accent-tint` | — |
| `#s-rule` chip | 17px/700, `8px 14px`, r999, 2px `--ks3-ink` | 999px | 2px | `--ks3-inset` / `--ks3-accent-tint` | not a control |

### 6.5 Type inventory (resolved at 1280)

| Role | family | size | weight | line-height | letter-spacing | colour |
|---|---|---|---|---|---|---|
| h1 | DISPLAY | 74 / 49.2 / 44 | 800 | .94 (69.56) | −.035em (−2.59px) | `--ks3-ink` |
| `.ks3-hook h2` (unclassed) | DISPLAY | 38 (30 ≤544) | 800 | 39.9 (1.05) | −1.14px | `--ks3-on-dark` |
| `.ks3-block h2` (`#s-bench`, `#s-wall`) | DISPLAY | 30 | 800 | 36 (1.2) | −.75px | `--ks3-ink` |
| `#s-fit h2` (inline) | DISPLAY | **34** | 800 | 38.08 (1.12) | −1.02px (−.03em) | `--ks3-on-dark` |
| `.ks3-ladder h2` | DISPLAY | 36 | 800 | **57.6 (1.6)** | −1.08px | `--ks3-ink` |
| `.ks3-rung h3` / `.ks3-rung-self h3` | DISPLAY | 23 | 800 | **36.8 (1.6)** | normal | `--ks3-accent-text` / `--ks3-stretch-text` |
| `#s-rule` statement | DISPLAY | **44 / 44 / 31.98 / 28** (`clamp(28px,3.9vw,44px)`) | 800 | 1.08 (47.52) | −.03em (−1.32px) | `--ks3-ink`, `max-width 26ch` = 734.77px |
| **KEY FACT statement** | DISPLAY | 22 | **700** | 1.35 (29.7) | −.015em (−.33px) | `--ks3-ink` |
| `#s-wall` reveal headline | DISPLAY | 26 | 800 | 31.2 (1.2) | −.02em | `--ks3-on-dark` |
| `#s-fit` verdict headline | DISPLAY | 27 | 800 | 31.86 (1.18) | −.025em | `--ks3-ink` |
| bench readout name | DISPLAY | 25 | 800 | 40 (1.6) | −.5px (−.02em) | `--ks3-ink` |
| sorter answer lead word / finding lead word | DISPLAY | 18 / 17 | 700 | 27.9 / 27.2 | — | `--ks3-ink-body` / `--ks3-alert-text` or `--ks3-accent-text` |
| `.ks3-keynote p` **and its `.ks3-eyebrow`** | DISPLAY | 30 (24 ≤544) | 700 | 39 (1.3) | −.02em (−.6px) | `--ks3-on-dark` / **`--ks3-alert`** |
| `.ks3-endmatter h2` | DISPLAY | 21 | 800 | 26.25 (1.25) | −.01em | `--ks3-ink` |
| hook part-tile number / `#s-rule` card chips | DISPLAY / BODY | 15 / 17 | 800 / 700 | 24 / 27.2 | — | `--ks3-ink` |
| body | BODY | 19 | 400 | 30.4 (1.6) | — | `--ks3-ink` |
| `.ks3-hook-prompt` / `#s-fit` intro | BODY | 19 | 400 | 31.35 (1.65) | — | `--ks3-on-dark-body` |
| `#s-bench` / `#s-wall` intro | BODY | 19 | 400 | 30.4 (1.6) | — | `--ks3-ink`, `max-width 54ch` |
| `.ks3-commit` | BODY | 22 | 700 | 29.7 (1.35) | — | `--ks3-on-dark-body` |
| gate question | BODY | 20 | 700 | 32 (1.6) | — | `--ks3-ink` |
| bench readout `job` | BODY | 20 | 600 | 31 (1.55) | — | `--ks3-ink` |
| readout `detail` / scope note / sorter evidence / rule-card close / finding note | BODY | 18 | 400 | 27.9 (1.55) | — | `--ks3-ink-body` |
| `#s-fit` job | BODY | 21 | 700 | 31.5 (1.5) | — | `--ks3-on-dark` |
| `#s-fit` where | BODY | 18 | 400 | 28.8 (1.6) | — | `--ks3-on-dark-body` |
| `#s-wall` row statement | BODY | 19 | 600 | 28.5 (1.5) | — | `--ks3-ink` |
| `.ks3-mis-quote` direct child / nested | BODY | **19 / 22** | 700 | 30.4 / 30.8 | — | `--ks3-ink` — **F22** |
| `.ks3-rung-q` | BODY | 21 | 600 | 29.4 (1.4) | — | `--ks3-ink` |
| `.ks3-score` / `.ks3-score-note` / `.ks3-ladder-sub` | BODY | 22 / 16 / 18 | 700/400/400 | 35.2 / 25.6 / 28.8 | — | `--ks3-ink` / `--ks3-ink-muted` |
| `.ks3-feedback` / `.ks3-feedback-word` | BODY | 19 | 400 / 700 | — | — | `--ks3-ink` |
| `.ks3-tick` label / `.ks3-answer-label` | BODY | 19 / 16 | 400 / 700 | — | — | `--ks3-ink` / `--ks3-ink-muted` |
| hook part-tile label / bench part name | BODY | 17 | 700 | 27.2 / 21.25 (1.25) | — | `--ks3-on-dark` / `--ks3-ink` |
| `.ks3-legal` | BODY | 15 | 400 | 22.5 | — | `--ks3-ink-muted` |
| bench tally | MONO | **16** | 500 | 25.6 | normal | `--ks3-ink-muted` |
| rail count · sorter progress · `#s-fit` progress · run hint · `#s-rule` sub-line | MONO | 15 | 500 | 24 | normal | `--ks3-ink-muted` / `--ks3-on-dark-muted` |
| `.ks3-tick-num` | MONO | 15 | 500 | — | — | `--ks3-ok-text` |
| bench control labels · `#s-rule` card labels | MONO | 14 | 500 | 22.4 | .07em (0.98px) | `--ks3-ink-muted` / `--ks3-accent-text` |
| canvas caption | MONO | 14 | 500 | 22.4 | **normal** | `--ks3-ink-muted` |
| readout `where` pill | MONO | 14 | 500 | 22.4 | .06em (0.84px) | `--ks3-ink` |
| verdict badge | MONO | 14 | 500 | 22.4 | .08em | `--ks3-ink` |
| **KEY FACT label** | MONO | 13 | 500 | 20.8 | .09em (1.17px) | `--ks3-accent-text` |
| bench part tag | MONO | 13 | 500 | 20.8 | .04em (0.52px) | `--ks3-ink-muted` / `--ks3-accent-text` / `--ks3-ink-ghost` |
| rail node label | MONO | 11 | 500 | 13.2 | .09em (0.99px) | state-dependent |

`.ks3-eyebrow` takes **five different colours** on this page, all tokens:
`--ks3-ink-muted` (header, `#s-bench`, `#s-wall`), `--ks3-alert` (`#s-hook`),
`--ks3-blue-light` (`#s-fit`, from `.ks3-practical .ks3-eyebrow`), `--ks3-alert-text`
(`#s-think`, from `.ks3-misconception .ks3-eyebrow`), `--ks3-accent-text` (`#s-rule`, inline).
The keynote's eyebrow is a sixth case and is not eyebrow-sized at all (30px display, above).

### 6.6 The canvas instrument (measured geometry and every colour)

| Property | Value |
|---|---|
| element | `<canvas width="1800" height="1120" role="img" aria-label="…">` |
| CSS size | `display:block; width:100%; height:auto` → **630 × 398.22** at 1280, 522 at 900, **442** at 820, 314 at 390 |
| device pixels per CSS pixel | ~2.86 at 1280 (1800/630) |
| drawing space | `CVW 900 × CVH 560`, entered via `ctx.setTransform(2, 0, 0, 2, 0, 0)` |
| redraw triggers | `componentDidMount`, `componentDidUpdate`, `document.fonts.ready`, and the `canvasRef` callback |
| font used on canvas | `'800 21px "Bricolage Grotesque", system-ui, sans-serif'` for the marker bubble numeral |
| diagram mode | `#FFFCF5` field; leaf = 4 nested rounded rects (wall 664×444 r34, inner 624×404 r26, vacuole 428×208 r72) + 13 rotated chloroplast ellipses with 3 grana strokes each + 4 mitochondria + a nucleus with nucleolus; cheek = 2 nested `blob()` paths (150-segment sinusoidally perturbed ellipse, `rx 298 ry 168`) + 8 mitochondria + a nucleus |
| scope mode | `#100D0A` ground, a **circular aperture** `arc(450, 280, 250)` used as a clip, an `11px #100D0A` + `3px #4A4038` ring drawn over it, and the specimen tiled at `k = 0.52`: leaf = a 5×5 grid of scaled cells, cheek = 5 blobs at authored offsets; `ctx.filter = 'blur(0.7px)'` on chloroplasts and `'blur(1.1px)'` on nuclei |
| stain | changes the scope nucleus from `#DCD2BE` at `globalAlpha .6` to `#4A3C7A` at `.92` |
| part marker | rings at `r + 5` around every anchor for the selected part, `lineWidth 4` on the first and `2.4` at `globalAlpha .6` on the rest; **`setLineDash([7,6])` and hue `#8F857B` when the part is invisible at ×400**, solid `--ks3-accent` otherwise; then a 19px filled bubble with the part number in `--ks3-ground` |
| marker anchors | authored per part per specimen in `PARTS[].mark` — 33 `{x, y, r}` triples across the seven parts |

**Colours.** 32 hex literals appear in the logic block. **Four resolve to a token**
(`#221E1B` = `--ks3-ink`, `#FFFCF5` = `--ks3-card`, `#E4572E` = `--ks3-accent`,
`#FBF3E6` = `--ks3-ground`) and **28 are genuinely new values with no `--ks3-*` equivalent**,
checked against the resolved token table:

```
#100D0A #2F5326 #3E3260 #453A69 #4A3C7A #4A4038 #4F7C3B #5C8544 #6E9C52 #7C6AA6
#8B4523 #8F857B #9AB0A6 #9C8DC0 #A2603A #B0A48E #C96C3C #CFB98A #D9C48D #DCD2BE
#E3EDE2 #E4EDE9 #E8EFDF #EBE4D6 #EDF2E1 #EFE8DA #F5ECD8 #F6E2D2
```

These are a **specimen palette** — cellulose tans, chlorophyll greens, mitochondrial oranges, a
purple nucleus, a methylene-blue stain, and two field-of-view creams. They are not KS3 UI colours
and should not become `--ks3-*` tokens; they belong to the art component (§7.7).

---

## 7. New components — how to generate each

Eight components. Three are carried from b1-01 with amendments; **five are new to the registry.**
Each states its data, markup, CSS, states and parity assertions. Anything marked "assert" is a new
`ks3_parity.COMPONENTS` entry.

### 7.0 Three carried from b1-01, with amendments

- **`rail` (b1-01 §7.1)** — unchanged in every value; five stages instead of four. The only new
  assertion this page adds: **`short` is ≤6 characters**, because the 104px rail column at MONO 11px
  `.09em` sets that limit and nothing else enforces it.
- **`key-fact` (b1-01 §7.2)** — every measured value confirms b1-01's spec exactly (§3.7). **Two
  amendments:** (a) *drop* b1-01's "assert at most one per lesson" — this page has two, and it is the
  family reference; (b) the box must be renderable **inside** a misconception block, not only as a
  `.ks3-lesson` child. Markup stays
  `<div class="ks3-keyfact"><p class="ks3-keyfact-label">Key fact</p><p class="ks3-keyfact-body">…</p></div>`.
- **`rule` (b1-01 §7.5)** — the panel shell is identical (`--ks3-band`, `3px --ks3-ink`,
  `--ks3-r-block`, `34px 32px`, eyebrow in `--ks3-accent-text`) and this page's statement **already
  uses the ruled `clamp(28px, 3.9vw, 44px)`** from drift 3, so drift 3 needs no adjustment here.
  Two amendments: `max-width` is **26ch** (b1-01 said 20ch — needs one value, and this is the
  reference screen); and the panel takes a **MONO 15px `--ks3-ink-muted` sub-line** below the
  statement that b1-01's spec has no slot for. Its cards are a separate component — §7.5.

### 7.1 `cell-bench` — the MODEL flagship

- **Data:** G4. Validation the generator should enforce: every part supplies `job`, `detail`,
  `visible` and `scope_note`; every specimen supplies a `caption`, an `alt` and a `tally` for
  **every** view; every part's `mark` covers at least one specimen; ≥2 specimens and ≥2 views (the
  instrument's whole argument is comparison); the gate's options carry **no** `correct` key.
- **Markup:** `<section class="ks3-block" id="…" data-activity="…" data-bench>` → eyebrow, `<h2>`,
  intro `<p>` at 54ch; a `<div class="ks3-bench-controls">` of labelled groups (each a MONO 14px
  `.07em` label over a `flex gap 9px` button row); the gate
  `<div class="ks3-bench-gate" data-reveal>`; then
  `<div class="ks3-bench-grid" data-bench-grid>` holding
  `<ul class="ks3-bench-parts">` of `<button class="ks3-bench-part" aria-pressed>` and a right
  column of `<figure class="ks3-bench-frame">` (canvas + caption), `<div class="ks3-bench-readout">`
  and the MONO tally `<p>`.
- **CSS:** move `[data-bench-grid]`'s two rules into `shared/ks3.css` with the **ruled** values —
  `grid-template-columns: minmax(0, 232px) minmax(0, 1fr)` and a `max-width: 820px` collapse (drift
  1 and 2, both verified safe on this page in §3.3) — plus `gap: 22px; align-items: start`.
  Classes for every state in §3.2: `.ks3-bench-part`, `.is-selected`, `.is-absent`;
  `.ks3-bench-readout`, `.is-absent`; `.ks3-bench-where`, `.is-both`, `.is-plant`, `.is-absent`;
  `.ks3-bench-scope`, `.is-visible`, `.is-hidden`. Bare values needing a home: `240→232px`, `56px`
  (part min-height), `36px`/`11px` (readout tile), `.04em`, `.06em`, `.07em`, `1800×1120`.
- **States:** specimens (n) × views (n) × extras (2ⁿ) × parts (n) × gate (2). For b1-03 that is
  2 × 2 × 2 × 7 × 2 = 112 renderings of the readout alone, plus 4 canvas modes.
- **Assert:** (a) every part state carries a **word** as well as a tone (R2) — "In both" / "Plant
  only" / "Not in an animal cell"; (b) the gate is absent from the DOM once answered **and** no
  element in the block ever carries a ✓/✗ or a green/red (R3 — only the ladder marks);
  (c) the scope-locked view control is `disabled` **and** visually distinct; (d) `canvasAlt` is a
  full sentence, present and different for every specimen × view combination; (e) the canvas's
  attribute size is at least 2× its maximum CSS width at the widest viewport; (f) selecting an
  absent part still resolves to a readout rather than an empty panel; (g) the caption strip sits
  **inside** the frame, on `--ks3-band` behind a `2px --ks3-rule` top border.

### 7.2 `sort-pairs` — the 2-way sorter, and the R3 decision inside it

- **Data:** G5. Validate: every `row.answer` ∈ `categories`; ≥2 categories; `note` non-empty on
  every row; `reveal_panel` present.
- **Markup:** `<section class="ks3-block" id="…" data-activity="…" data-sort>` → eyebrow, `<h2>`,
  intro; `<ul class="ks3-sortrows">` of `<li class="ks3-sortrow">` each holding a statement `<p>`, a
  `<div class="ks3-sortchips">` of `aria-pressed` buttons, and (after the reveal) a
  `<p class="ks3-sort-evidence" data-reveal>`; footer = `.ks3-reveal-btn` + a MONO counter; then
  `<div class="ks3-sort-panel" data-reveal>`.
- **CSS:** row `--ks3-card` on `2px --ks3-rule-strong`, `--ks3-r-panel`, `18px 20px`; chips per
  §6.4; evidence 18px/1.55 `--ks3-ink-body` with a DISPLAY-800 lead word; panel `--ks3-ink`,
  `--ks3-r-panel`, `22px 24px`.
- **States:** row unanswered / answered / (after reveal) right / wrong; chip chosen / not; button
  locked / unlocked; panel hidden / shown.
- **Assert:** (a) the locked button carries `disabled` **and** `opacity .45` **and** a counter that
  says how many remain; (b) the chips are byte-identical whether the choice was right or wrong
  (measured true on this page, and it is the half of R3 the page keeps); (c) the evidence lead word
  equals the row's `answer` exactly; (d) **if `mark_rows` is true, every marked row also carries a
  word or a drawn mark** — this is the assertion that would have caught F18, and it is the reason
  `mark_rows` must be a field rather than a hard-coded behaviour.

### 7.3 `fit-parts` — the build-and-run practical

- **Data:** G6. Validate: every `specimen.needs` ⊆ the part id set; every id in `waste` is **not** in
  `needs`; `consequence` covers every part id; the three verdict strings exist; ≥2 specimens.
- **Markup:** `<section class="ks3-block ks3-dark ks3-practical" id="…" data-activity="…" data-fit>`
  → a head row (eyebrow, `<h2>`, MONO progress), intro at 58ch, `<ul class="ks3-fit-tabs">`,
  `<div class="ks3-fit-job">`, "Install the parts" label, `<ul class="ks3-fit-parts">` of pill
  buttons, a run row (Run / Strip / MONO hint), then `<div class="ks3-fit-verdict" data-reveal>`
  holding a badge, a headline, `<ul class="ks3-fit-findings">` and a closing `<p>`.
- **CSS:** the dark `seg()` for tabs; pills at `min-height 48px` on `border-radius 999px`;
  `.ks3-fit-verdict` a **light** panel (`--ks3-ground`) inside the dark block;
  `.ks3-fit-badge.is-fails|.is-waste|.is-works`; `.ks3-fit-finding.is-missing|.is-extra`.
- **States:** specimens (n) × 2ⁿ installs × 4 run states (unrun / fails / waste / works), and the
  verdict is removed on any install change.
- **Assert:** (a) the Run button's disabled state is **visible** — `opacity` < 1 or a distinct
  ground — because F19 is a rendered-in-the-reference defect and the assertion is what stops it
  being ported; (b) each verdict carries its word (R2); (c) a `fails` verdict does **not** render the
  specimen's closing note (F20 — this contradicts the approved page, so it must be flagged to Design
  before it is asserted); (d) "Strip it back out" is idempotent and the progress counter never goes
  negative; (e) `consequence` text is shared across specimens and `waste` text is per specimen.

### 7.4 `phenomenon.tiles` — the numbered part-tile row

- **Data:** G7 — `tiles: [{num, label}]`, 2–8 entries.
- **Markup:** `<ul class="ks3-tiles"><li><span class="ks3-tile-num" aria-hidden="true">1</span><span
  class="ks3-tile-label">Cell membrane</span></li>…`
- **CSS:** `display:grid; grid-template-columns: repeat(auto-fit, minmax(158px, 1fr)); gap: 10px;
  margin: 24px 0 0`; `<li>` `--ks3-dark-panel`, `border-radius 14px`, `padding 12px 14px`,
  `flex; align-items:center; gap:10px`; number 26×26 r8 `--ks3-on-dark-muted` ground with
  `--ks3-ink` DISPLAY 15px/800; label 17px/700 `--ks3-on-dark`.
- **States:** one — this row is decorative reference, not a control. No `aria-pressed`, no cursor,
  no hover.
- **Assert:** the numbers match the part ids the flagship uses (so tile 5 and bench part 5 are the
  same part), the number span is `aria-hidden`, and the tiles are **not** focusable.

### 7.5 `rule-cards` — the cream two-up card with a chip list

Separated from `rule` (§7.0) because b1-01's card is `{term, gloss}` and this one is a labelled chip
inventory. Both are cream cards inside the same panel; only one shape can be the component, and this
is the one the family reference draws.

- **Data:** part of G3 — `cards: [{label, label_tone, chips: [str], chip_tone, close}]`, 2–3 entries.
- **Markup:** `<ul class="ks3-rule-cards"><li><p class="ks3-rule-card-label">In both · 4</p><ul
  class="ks3-rule-chips"><li>1 · Cell membrane</li>…</ul><p class="ks3-rule-card-close">…</p></li>…`
- **CSS:** grid `repeat(auto-fit, minmax(280px, 1fr))` gap 16px, `margin-top 26px`; card
  `--ks3-card` on `2px --ks3-ink`, `--ks3-r-card`, `20px 22px`; label MONO 14px `.07em` uppercase in
  `--ks3-ink-muted` or `--ks3-accent-text`; chips `flex wrap gap 8px`, `padding 8px 14px`, r999,
  `2px --ks3-ink`, 17px/700, ground `--ks3-inset` or `--ks3-accent-tint`; close 18px/1.55
  `--ks3-ink-body`.
- **States:** two label tones × two chip tones. The tone is authored, not derived — "Plant only"
  takes accent because it is the lesson's point, not because it is second.
- **Assert:** card borders are `--ks3-ink` (this is what separates them from a `.ks3-option`, whose
  border is `--ks3-option-border`); the chips carry **no** `aria-pressed`, cursor or hover; the
  label's chip count matches `len(chips)`; `minmax(280px, 1fr)` at the 890px inner width yields
  exactly 2 columns.

### 7.6 `misconception` group — two statements in one block

- **Data:** G8, once Design has ruled on the shape.
- **Markup:** the existing `.ks3-misconception` shell, with the second and subsequent statements
  each wrapped in `<div class="ks3-mis-next">`.
- **CSS:** `.ks3-mis-next { margin-top: 22px; padding-top: 20px; border-top: 2px solid
  var(--ks3-alert-border); }` — and **a specificity fix on `.ks3-mis-quote`** so nesting stops
  changing its size (F22). Recommend `.ks3-misconception .ks3-mis-quote { font-size: 22px;
  line-height: 1.4 }` replacing the `>` rule's reach, which makes every B1 quote 22px.
- **States:** one, ×n statements.
- **Assert:** exactly one `.ks3-mis-head` per block; every `.ks3-mis-quote` in the document resolves
  to the same font-size regardless of nesting depth.

### 7.7 `cell-bench` art — acquire, do not generate

The canvas is 260 lines of imperative 2D drawing (`rr`, `ell`, `blob`, `mito`, `nucleus`,
`leafBody`, `cheekBody`, `drawDiagram`, `drawScope`, `drawMarker`, `draw`), 28 non-palette colours,
two `ctx.filter` blur values, a clip-and-tile field view, and 33 authored marker anchors in a
900×560 space. **No data shape produces it.** It must be a **registered named art component** keyed
by figure id, exactly as b1-01 concluded for its candle — but by a different mechanism, so it needs
its own `figures[].kind` (`canvas-art`, G9) rather than reusing `css-art`.

Recommend `shared/ks3-art/cell-bench.js` exporting `draw(ctx, {specimen, view, stain, part})` with
the colour table as module constants, and `build_ks3.py` emitting
`<canvas class="ks3-art ks3-art--cell-bench" width="1800" height="1120" role="img"
aria-label="{{alt}}">` plus a data attribute naming the art id. **Assert:** the canvas is redrawn on
`document.fonts.ready` (the marker numeral is set in Bricolage and will draw in a fallback face
otherwise — Design's page handles this explicitly at line 732); the attribute size is ≥2× the
maximum CSS width; and `role="img"` plus a non-empty `aria-label` are present for every state, because
R6 requires the written readout to carry the entire result and there is no motion here to fall back on.

---

## 8. Ambiguities and findings

Confirmed against `00-delivery-drift.md`, as required — **this page is a party to all five drifts
and contradicts none of them:**

| Drift | Ruled | What b1-03 measures | Contradiction? |
|---|---|---|---|
| 1 — bench grid column | 232px | declares **240px**; patched to 232px it costs 8px of control column, gains 8px of canvas, adds ~5px of block height, wraps nothing (§3.3) | **no** |
| 2 — bench grid collapse | 820px (against the count) | declares **780px**; patched to 820px the bench block is **+637.95px taller at 820** and the canvas goes 442 → 704px. Large, visible, not breaking (§3.3) | **no** — but the cost is bigger than the drift document implies, because this page's canvas is aspect-locked |
| 3 — statement type | `clamp(28px, 3.9vw, 44px)` | **already declares exactly that** (line 227) and resolves to 44 / 44 / 31.98 / 28 | **no** — this page is one of the two the ruling was drawn from |
| 4 — `seg()` light branch | b1-06's accent-tint variant | declares the **inverted ink-fill** on-state, and uses it on **three** controls (specimen tabs, view tabs, stain) plus the dark branch on a fourth (`#s-fit` tabs). Geometry is identical to b1-06's (17px, `11px 17px`, 44px, `--ks3-r-control`) — only the on-state colour differs | **no**, but see F23 |
| 5 — KEY FACT ground | `var(--ks3-band)` | measured `#F4E9D8` = `--ks3-band` on **both** boxes | **no** |

**(a) Needs Design.**

- **F15 — the brand mark.** Design's KS3 nav puts the chevron **inside a 34×34 `--ks3-accent`
  rounded-10px tile** with a `#FBF3E6` stroke; MRB-197's ruling and the generator both emit a bare
  `#E4572E` chevron with no tile. Measured on both. Both are drawn; they cannot both be right, and
  this is the mark on 50 lessons.
- **F16 — the keynote label.** Design: `p.ks3-eyebrow` → Bricolage 30px/700 uppercase
  `--ks3-alert`. Generator: `h2` → Bricolage 30px/800 sentence case `--ks3-on-dark`. Which element
  is the keynote's label, and is it yellow?
- **F18 — the sorter marks in amber, with colour as the only signal.** Measured: after the reveal a
  wrong row is `--ks3-alert-tint` on `2px --ks3-alert-border` and a right row is `--ks3-inset` on
  `2px --ks3-ink`, with **no word and no mark** distinguishing them, and the chips identical. This
  sits against R2 ("every state survives being printed in greyscale"), R3 ("only the mastery ladder
  marks right and wrong") and `README.txt` ("Amber is reserved for misconceptions") at once. It is
  also gameable: choices stay changeable after the reveal and the row re-marks live, so a student can
  chase the pale ground without reading the evidence. Does the sorter mark, and if so what word does
  a marked row carry?
- **F21 — two KEY FACT boxes.** `README.txt` says one per lesson; the MODEL reference screen has
  two, both inside `#s-think`. Is the convention wrong, or the page?
- **F23 — amber outside a misconception, in four places.** Beyond F18: the bench's "You cannot see
  this one" note (`--ks3-alert-tint` / `--ks3-alert-border`), `#s-fit`'s "Missing —" findings (same
  pair), and `#s-fit`'s "Fails" badge (`--ks3-alert-tint`). Each is legible and each carries a word,
  so none breaks R2 — but `README.txt`'s "amber is reserved for misconceptions" is either a
  narrower rule than the pages follow, or four uses need a different tone.
- **F20 — the failed build is told the answer.** `spec.note` renders under every verdict, so a
  palisade cell run with 4 of 7 parts gets "Fails · 3 parts short" *and* "All seven. A palisade cell
  is a plant cell with nothing left out…" (measured). Intended, or should the note be gated on
  `works`?
- **Flip cards, and R4's fourth clause.** The MODEL reference screen has **no flip card** (measured:
  0 `aria-expanded`, 0 `.ks3-cards`), so it cannot arbitrate whether *"one tap flips one card"* means
  "a tap affects only the card tapped" (the generator's reading — two cards open simultaneously,
  measured) or "at most one card is open at a time". Also: the generator's MODEL page renders **14
  flip cards in two sets**, and Design's renders none. Is the `keyword` block part of the MODEL
  rhythm at all?
- **b1-01's F1, F2, F4, F11 and F12 all reproduce here unchanged** and are not restated: two
  different breadcrumbs; the narrow top bar reading 5/5 with nothing answered; a prediction erased
  once made; no keyboard route to a section under 1340px; a tutor CTA that is a live in-page anchor
  on Design's page and a dead `<span>` on the generator's.

**(b) Needs Mide (science / content).**

- **The approved page and the authored data teach different lessons, again.**
  `mrbadmus_site/…/animal-and-plant-cells.html` (built from `ks3_data/`) opens on *"Onion cells on
  the left, cheek cells on the right, both at ×400"* with the big question *"What is inside a cell,
  and what is each part for?"*; Design's page opens on *"You and an oak tree run off the same parts
  list"* with *"What does a plant cell have that you do not — and what do you have that a plant does
  not?"*. Under standing law the approved page wins, which means **~2,938 words of new content**
  (counted in §0), nearly all science-bearing: 7 parts × job/detail/scope-note, 5 sorter evidence
  lines, 7 consequence lines, 4 FIT cells with their waste notes, 4 rungs with 6 distractor
  corrections and 8 success criteria. It arrives at once and needs the examiner gate.
- **Four specific claims the page teaches as settled**, worth an examiner's eye because the
  instrument is built on them: (1) **five of the seven parts are visible in a leaf cell at ×400**
  (wall, cytoplasm, nucleus, vacuole, chloroplasts) and **two are not** (membrane, mitochondria) —
  this is the gate's answer and the tally's number; (2) **two of the four are visible in a cheek
  cell at ×400, and only once stained**; (3) *"The single line you see at the edge of a cheek cell is
  not the membrane; it is just where the cell stops"*; (4) a **root hair cell has a large vacuole**
  and is credited with six of the seven parts. Rung 4 also asks a student to conclude "plant-like but
  not proved" about a walled, vacuolated, chloroplast-free pond cell — the criterion *"a wall on its
  own is not proof, because things that are not plants have walls too"* reaches beyond KS3's usual
  ground.
- **`covers` for this lesson** is whatever `ks3_data/biology_b1_cells.py` currently declares;
  whether the "one parts list, three extras" framing still owns exactly those statements is a
  curriculum judgement.

**(c) Code's call — recorded, not asked.**

- **F14 — `shared/styles.css` leaks KS4 heading rules onto every KS3 page.**
  `h1, h2, h3, .brand { letter-spacing: -0.01em; line-height: var(--lh-title) /* 1.15 */ }` at
  `styles.css:20` wins wherever `shared/ks3.css` sets no line-height, because
  `[data-mode="ks3"] h1, h2, h3` sets only family and weight. Measured on `.ks3-rung h3`: **26.45px
  generated vs 36.8px on the reference.** The reference page cannot see it because it never loads
  `styles.css`. Fix: give `[data-mode="ks3"] h1, h2, h3` an explicit `line-height` and
  `letter-spacing`, or stop emitting `styles.css` on KS3 pages. The second is cleaner and is a
  bigger change; recommend the first, and add a parity assertion that pins each heading's resolved
  line-height.
- **F17 — `ks3-ladder` versus `ks3-block ks3-ladder` is not cosmetic after all.** b1-01 §8 recorded
  that both class sets "resolve to the same painted shell … worth a parity assertion rather than a
  change". The shell is confirmed identical here (3px ink, 30px radius, `6px 6px 0 --ks3-ok`, 32px
  padding), but `.ks3-block h2 { line-height: 1.2 }` only matches the two-class form, so the ladder
  heading is **36px/57.6px on Design's page and 36px/43.2px on the generator's**. One of the two is
  the ladder heading. Design's single-class form is the approved page, so under standing law the
  page wins and the generator should drop `ks3-block` from the ladder — which is also what makes
  `.ks3-ladder`'s own rules the single source. Recommend it, and state it in the build report
  because it changes the KS4-facing ladder too.
- **F19 — `#s-fit`'s Run button is `disabled` and looks enabled.** Measured `disabled: true,
  opacity: 1, cursor: pointer`, while `runBtnStyle` (line 1227) computes the correct
  `opacity:.4;cursor:default` and is never referenced by the template. Dead code, same species as
  b1-01's unused `railFillHeight`. The same page renders `#s-wall`'s locked button properly. Code
  fixes it; §7.3 asserts it.
- **F22 — `.ks3-mis-quote` changes size with nesting.** `.ks3-misconception > p` (0,1,1) beats
  `.ks3-mis-quote` (0,1,0), so the direct-child quote renders 19px and a nested one renders 22px
  (measured, both on this page). Fix the specificity. It moves b1-01's and b1-02's quotes to 22px
  too, so it belongs in the build report.
- **F2's fix is now a five-stage decision.** The narrow top bar reads a full accent bar at
  `#s-ladder` **and stays there for `#s-keynote`, `.ks3-layer`, `.ks3-endmatter` and the legal
  line** — a quarter of the page's scroll height showing "complete". Whatever ruling F2 gets,
  the fix should also give the observer something to report for the tail.
- **The `sc-interp` wrapper.** The DC runtime wraps every interpolation in a
  `<span class="sc-interp">`, shifting positional child-span indices. A parity probe must select by
  class or by attribute, never by `querySelectorAll('span')[n]`. This cost me two mis-read
  measurements before I noticed; recording it so the next run doesn't pay it.
- **The `b3-arrive` settle floor.** `animation: b3-arrive .34s ease-out **both**` means a
  freshly revealed element measures `opacity: 0` for up to 340ms after the runtime finishes
  re-rendering. A 450ms settle is **not** enough on this page; measured a real element at
  `opacity: 0` and then `1`. Use ≥800ms, or read `getAnimations()` and wait.
- **`_ds` ships two 3D Studio stylesheets, not one.** b1-01's F13 named `_ds_bundle.css`;
  `tokens/src-styles-tokens.css` is the second (`--st-*` token block, "3D Studio tokens — values
  lifted verbatim from the frozen reference"). Neither is KS3 design intent, both are loaded on
  every reference page, and the generator loads neither. Recorded so nobody treats either as a KS3
  source.
- **§10.2's `practical` row is stale against this page.** It gates `practical` on `sim canvas` and
  `sim live figure is mono`; Design's `#s-fit` is a `ks3-practical` with **no canvas and no live
  mono figure**. The row needs the `fit-parts` components added, or `practical` splits into two
  block types.
- **§10.1 says MODEL has 50 slots; `design-coverage-manifest.md:75` says 49.** One line is wrong.
  Not load-bearing here; flagged so it is fixed by whoever owns the count.
- **`ks3-hook-h` is already gone.** b1-01 recommended dropping the inert class; this page's hook
  `<h2>` carries no class at all. Nothing to do — recorded so the recommendation is not re-litigated.

**Could not measure.**

- **Rail stage 2's unreachability under `showScopeView: false`** — read from source lines 1102 and
  505; the prop defaults to `true` and I did not rewrite the `data-props` payload to test it.
- **`prefers-reduced-motion: reduce`** — the page's own query at line 24 is read from source; I did
  not drive `Emulation.setEmulatedMedia`. b1-01 measured the equivalent rule firing, and this page's
  is simpler (one selector, `animation: none !important`).
- **`:hover`** — `.ks3-option:hover { transform: translateX(3px) }` and `.ks3-card-btn:hover
  { transform: translate(-2px,-2px) }` are read from `shared/ks3.css`; CDP mouse-move hover was not
  driven on either page.
- **Rail geometry above 1341px** — checked arithmetically from the measured
  `left: calc(50% − 632px)` and the 1320px `--ks3-page` cap, not by device-metrics override, exactly
  as b1-01 did.
- **Document height at 820 under drift 2's collapse** — the `#s-bench` delta (+637.95px) was
  measured directly; the resulting whole-document height is arithmetic.
- **The 320px viewport** was out of scope, and **no `print` stylesheet exists** on either page to
  measure.
