# B1 L6 · Unicellular organisms · CONTRAST

Inventory of `docs/ks3/design-reference/b1/b1-06-unicellular-organisms.dc.html` (1,145 lines,
delivered unmodified). Method, viewports, generator vocabulary and standing law: see `README.md` in
this folder — not restated here. Cross-page value collisions: `00-delivery-drift.md`.

Measured 13 Aug 2026 in headless Chrome via `ks3_browser.py`, serving
`docs/ks3/design-reference/b1/` over HTTP, at **1280 · 1340 · 820 · 390** with
`Emulation.setDeviceMetricsOverride` (`page.set_viewport`). Every number below was read from
`getComputedStyle` / `getBoundingClientRect` in that browser, or out of the file's own source.
Where a value could not be measured it says so.

**Console: clean.** No errors or uncaught exceptions at any of the four viewports (favicon 404
filtered).

Where b1-01 → b1-05 have already established something true of all six pages — the header trail
carried inline, the rail's two variants, F2 (the narrow-screen top bar reading complete when nothing
was answered), the `_ds` bundle shipping the 3D Studio stylesheets, the 60-token set, the DC-runtime
settle trap, `sc-interp` wrapping every `{{ }}`, `ks3-hook-h` being inert, Design's `ks3-ladder`
single-class set, the content living in `<script data-dc-script>` constants, and the missing 19–28px
type tier — this file **confirms and cites** rather than re-deriving. Its length is spent on the
four things the task asked for: the "settles it" activity (§3.5), the comparison rows in both states
(§3.4), the microscope's control surface against the repo engine (§3.3), and the B1-04/B1-06 paired
contract (§4.5).

## ⚠️ This page is the CONTRAST reference screen — 18 slots inherit it

`docs/ks3/design-coverage-manifest.md` §10.1 names **this file** as the approved screen for
**CONTRAST, 18 lesson slots**, ruled by Mide on 12 Aug 2026. Unlike b1-05 (a second SYSTEM
realisation), everything on this page is family-defining by construction. The "settles it" activity
in §3.5 is the flagship, and MRB-209 §1 records Design's ruling — endorsed by chat-Claude — that it
is the shape the whole family inherits.

Two structural facts distinguish it from the four pages already inventoried, and both matter to the
cross-page rulings:

- **There is no top-level orphan KEY FACT `<div>`.** The KEY FACT box is the last child of
  `#s-compare`, inside the block. That is a **fourth position** for the box across five pages —
  F19's count is now 2 : 1 : 1 : 1, not 2 : 1 : 1. §3.4.4.
- **`p.ks3-legal` is present**, and it is a lab-safety line about pond water, not a copyright line.
  F20 becomes: absent × 2 (b1-04, b1-05), safety × 2 (b1-03, b1-06), copyright × 1 (b1-01).

---

## Content payload — line ranges for a byte-identical lift

**Never retype these.** Every string is authored and science-bearing.

| Payload | Lines |
|---|---|
| `RAIL` (4 nodes, `{id, label}`) | **427–432** |
| `RAIL_SHORT` | **434** |
| `isDone` | 436–442 |
| `OBJS` — 3 objectives × (id/label/total/fov/**dof**) | **445–449** (comment at 444) |
| **`POND`** — 7 organisms × (kind/x/y/depth/len/seed) | **451–460** |
| `BACTERIA` — the 54-element LCG generator | **462–475** |
| `CENTRES` — 3 pan targets × (id/label/x/y) | **477–481** |
| **`RESOLVE`** — 3 prose notes keyed by total magnification | **483–487** |
| **`COMPARE`** — 7 rows × (name/uni/multi) | **489–497** |
| **`CASES`** — 4 cases × (id/label/desc/4 features × (text/settles/why)/verdictLabel/answer/why) | **499–552** |
| **`RUNGS`** — r1, r2, with per-option `correction` | **554–571** |
| **`SELF_RUNGS`** — r3 (5 criteria), r4 (4 criteria) | **573–595** |
| canvas helpers `rr` / `ell` | 597–614 |
| initial `state` (incl. `startMount` / `motionDefault` seeding) | 616–634 |
| lifecycle — `componentDidMount`, `tick`, `objDef`, `focusDepth` | 636–670 |
| the four organism routines `amoeba` / `paramecium` / `euglena` / `cheekCell` | **673–802** |
| `draw()` — the 900×560 design space, the 2× transform, the circular clip and the two-stroke bezel | **804–885** |
| `seg()` — **both branches** | **887–896** |
| `renderVals` (style strings + UI strings) | 898–1140 |

Static prose: header **87–94** · hook **96–118** (the 4 hook options are **data**, at 958–962; the
reveal at **114** is static) · `#s-scope` head + lede **120–128**, its eight control captions and
readout labels at 150 / 158 / 167 / 176 / 185 / 195 / 199 / 203, the "What you can resolve:" label at
**208** · `#s-compare` **215–244** (statement **217**, dark header row **220–224**, KEY FACT
**240–243**) · `#s-settle` **246–290** (eyebrow / h2 / instructions **247–249**, button label **279**)
· `#s-think` **292–304** (**both misconceptions are static markup, not data**) · ladder head 306–316
and retry note **370–373** · keynote **376–379** · stretch layer **381–389** · endmatter **391–414** ·
legal line **416**.

**Authored word count (for MRB-205): ~2,490 words**, counted by the same script method b1-03, b1-04
and b1-05 used:

| Source | Words |
|---|---|
| data constants, lines 427–595 (single-quoted literal content) | **1,538** |
| of which `CASES` 499–552 | 704 |
| of which `SELF_RUNGS` 573–595 | 317 |
| of which `RUNGS` 554–571 | 238 |
| of which `COMPARE` 489–497 | 160 |
| of which `RESOLVE` 483–487 | 81 |
| of which `OBJS` + `POND` + `BACTERIA` + `CENTRES` | 20 |
| of which `RAIL` + `RAIL_SHORT` | 18 |
| `renderVals` **prose** literals (4 hook options + 4 gate options + 2 mount notes + 2 captions + 2 alt texts + 16 UI strings) | **241** |
| static markup 87–416, tags and `{{ }}` stripped | **711** |

⚠️ Same caveat as b1-04 and b1-05: a naive extraction of all single-quoted literals from
`renderVals` returns 35 strings, but five of those are **style-string fragments**
(`';border:2px solid '`, `'0 0 0 4px var(--ks3-accent-tint)'`,
`'; border-top: 2px solid var(--ks3-rule);'`, `'; border: 2px solid '`, and the 16px choice-button
declaration block). The 241 above is prose only, 30 strings.

**None of these 2,490 words exists in `ks3_data/`.** The generator's `unicellular-organisms` record
(`ks3_data/biology_b1_cells.py`, from line 2000) is a different lesson — different big question
(*"How can one single cell be a whole living thing?"* against Design's *"Two single cells, the same
size. One is a whole animal. One is a piece of you. What tells them apart?"*), a 16-block stack of
`hook · check · explainer · misconception · practical · figure · check · misconception · figure ·
keyword · check · check · quiz · summary · explainer · check`, and no `key_note`, no `tutor_anchor`,
no `rail`. §3.1.

---

## 1. Page skeleton

### 1.1 The spine — confirms b1-03 §1.1, b1-04 §1.1 and b1-05 §1.1

`<body>` holds the hydrated **`<div class="rd" data-mode="ks3" id="dc-root">`** and the logic
`<script>`; the `<x-dc>` template is removed rather than hidden. `.rd` is a DIV, not `<body>`, with
the same 8 inline declarations reproducing what `body.rd[data-mode="ks3"]` would give (line 42), and
the token block is `.rd[data-mode="ks3"]` so all tokens resolve. **All 36 `--ks3-*` tokens probed
resolved to their `shared/ks3.css` / `shared/tokens.css` values** (§6.1), including the `--ks3-ok`
family that b1-03's F14 story turns on.

`.rd` children, in order — **5 top-level landmarks, the same set as b1-01, b1-03, b1-04 and b1-05**:

| # | Element | Position | Height 1280 |
|---|---|---|---|
| 1 | `nav.ks3-nav` | static | 63.19 |
| 2 | `nav[data-rail="top"]` | **sticky, top 0, z-index 20** | 46.59 |
| 3 | `nav[data-rail="side"]` | **fixed, top 150px, left calc(50% − 632px), width 104px, z-index 20** | 0 (`display:none` <1340) |
| 4 | `main.ks3-main` | static | 7646.66 |
| 5 | `footer.ks3-footer` | static | 107.59 |

### 1.2 The measure

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `.ks3-main` width | 1280 | **1320** (capped) | 820 | 390 |
| `.ks3-main` max-width | 1320px = `--ks3-page` | same | same | same |
| `.ks3-main` padding | 44px 24px 90px | 44px 24px 90px | 44px 24px 90px | **28px 16px 64px** |
| `.ks3-lesson` width | **960** | **960** | 772 | 358 |
| `.ks3-lesson` max-width | 960px = `--ks3-wide` (60rem) | same | same | same |
| `nav.ks3-nav` height | 63.19 | 63.19 | **63.19** | **153.97** |
| document height | **7864** | 7817 | 8527 | **12381** |

The narrow breakpoint is `@media (max-width: 34rem)` in `shared/ks3.css`, identical to
b1-01/03/04/05 (not re-bisected — the padding values at 390 match those pages exactly).

**The page's own media queries are exactly four**, enumerated by walking `document.styleSheets` and
following every `CSSImportRule`:

| Condition | Source line | What it does |
|---|---|---|
| `max-width: 820px` | 21 | collapses `[data-bench-grid]` to one column — **⚑ matches nothing, §1.6** |
| `max-width: 820px` | 26–30 | the comparison rows' stacked variant, §3.4.2 |
| `min-width: 1340px` | 32 | the rail swap |
| `prefers-reduced-motion: reduce` | 33 | kills `[data-arrive]` |

The remaining conditions (`print`, `(prefers-reduced-motion: no-preference)`, `(max-width: 34rem)`,
`(max-width: 1023px)` ×3, `(max-width: 699px)` ×7, `(max-width: 830px)`) all come from the `_ds`
bundle.

**No `.ks3-explainer` and no 736px `--ks3-measure` column anywhere.** Prose is capped by `ch`
measures instead: `58ch` on `#s-scope`'s lede, `54ch` on `#s-settle`'s instruction paragraph, `26ch`
on `#s-compare`'s statement (measured `max-width: 671.837px` at 1280).

### 1.3 Header carries the lesson trail INLINE — confirmed

Nav markup and every resolved value match b1-01 §1.3 and b1-03/04/05 §1.3: `display:flex;
flex-wrap:wrap; gap:6px 0`; brand Bricolage with a 34×34 `--ks3-accent` r10 tile holding a 20×20
`#FBF3E6` chevron; 2×26 `--ks3-rule` divider at `margin 0 20px`; `ol[aria-label="Breadcrumb"]` at
body-font 17px, gap 9px, `--ks3-accent-text` 600 links; trailing `a.ks3-nav-link` "KS3".

Nav height is **63.19 at 1280, 1340 and 820**, growing to **153.97 at 390** (trail over 2 rows) —
the same pure-function-of-title-length behaviour b1-03, b1-04 and b1-05 recorded. **A parity
assertion must not pin nav height to a number.** F1 (Design's inline trail vs the generator's
`nav.ks3-crumbs` inside `<main>`) reproduces exactly — fifth page, unchanged.

### 1.4 Lesson body, document order — **11** direct children of `.ks3-lesson`

| # | Element | id | classes | margin-top | scroll-margin-top | h @1280 |
|---|---|---|---|---|---|---|
| 1 | `header` | — | `ks3-lesson-head` | — | 0 | 355.94 |
| 2 | `section` | `s-hook` | `ks3-block ks3-dark ks3-hook` | 28px | 92px | 612.84 |
| 3 | `section` | `s-scope` | `ks3-block ks3-dark ks3-practical` | 28px | 92px | 594.72 (gate closed) → **1506.06** (open, ×4 pond) |
| 4 | **`section`** | `s-compare` | **none** — fully inline-styled | 28px | 92px | **1024.36** |
| 5 | `section` | `s-settle` | `ks3-block` | 28px | 92px | **1097.03** → 1545.30 (one case revealed) |
| 6 | `section` | `s-think` | `ks3-block ks3-misconception` | 28px | 92px | 577.09 |
| 7 | `section` | `s-ladder` | **`ks3-ladder`** (single class) | 28px | 92px | 1961.59 |
| 8 | `section` | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | 28px | 92px | 287 |
| 9 | `section` | — | `ks3-layer` | 34px | 0 | 254.28 |
| 10 | `div` | — | `ks3-endmatter` | 34px | 0 | 410.3 |
| 11 | **`p`** | — | **`ks3-legal`** | 34px | 0 | 39.5 |

Four structural facts:

- **`#s-compare` is a `<section>` with no class at all** — no `.ks3-block`, no modifier. Its whole
  appearance is 20 inline declarations: `background: var(--ks3-band)`, `border: 3px solid
  var(--ks3-ink)`, `border-radius: var(--ks3-r-block)`, `padding: 34px 32px`, `margin: 28px 0 0`.
  Measured 960 × 1024.36. **It maps to no registered block type**, and the KEY FACT box lives inside
  it. §3.4.
- **The KEY FACT box has moved inside a block for the second time** (b1-03 put it inside
  `#s-think`), and this is its **fourth distinct position** across five pages. F19 restated in §3.4.4.
- **`p.ks3-legal` is present** and carries lab safety, not copyright: *"Pond water is not sterile.
  Keep it away from your mouth and cuts, seal slides with a coverslip, and wash your hands before you
  leave the lab."* 15px `--ks3-ink-muted`, `border-top 1px --ks3-rule`, `padding 16px 0 0`.
- **`#s-scope` is `.ks3-practical` and carries no `.ks3-sim`.** Measured
  `document.querySelectorAll('.ks3-sim').length === 0`. Same divergence b1-04 and b1-05 recorded:
  the registered `sim canvas` component gates `practical` today, and there is nothing here for it to
  gate.

### 1.5 Class audit and stylesheet set

The page uses **51 `ks3-*` class names on load** — 54 total counting `rd`, `sc-host`, `sc-interp` —
and **55 total after one hook click**, when `ks3-reveal` enters the DOM. That is b1-05's ⚑ again:
**a parity probe that enumerates classes on load under-reports this page by one**, and the missing
one is a component with its own colours.

Across all reachable states the page uses **60 distinct `ks3-*` names, and all 60 exist in
`shared/ks3.css` — zero misses** (checked by string match of `.<class>`). There is **no
`ks3-hook-h`**: the hook `<h2>` carries no class and is styled by `.ks3-hook h2`. Fourth independent
confirmation of b1-01's recommendation to drop the class.

⚠️ **Measurement caveat.** The DOM enumeration walks `e.className.split` and therefore silently skips
**SVG elements**, whose `className` is an `SVGAnimatedString`. `ks3-mark` and `ks3-mark-arrow` are
present in the static markup (lines 74, 328–329, 340–341, 395, 401–402) and were confirmed from
source, not from the DOM walk. Any parity probe built the same way will have the same blind spot.

Everything else is carried by **125 inline `style=` attributes** (b1-03: 225, b1-04: 125, b1-05: 174,
b1-01: 110) plus **13 JS-built style strings** (`seg` — used for four different control groups;
`node.chipStyle` / `textStyle` / `lineStyle` / `linkStyle`; `railBarStyle`; `row.style`; `t.style`
×4 groups; `f.style`; `c.style`; `f.whyStyle`; `settleBtnStyle`; plus the class-name builders
`feedbackClass` and `tallyClass`).

**Stylesheet sets differ exactly as b1-03 §1.5 recorded, and both consequences reproduce.**

| | Reference page | Generated page |
|---|---|---|
| sheets | **4 entries** (2 inline + `_ds/…/styles.css` → imports + 1 inline) | 4 link tags |
| KS3 rules | `_ds/…/tokens/shared-ks3.css` | `/shared/ks3.css?v=…` |
| **`shared/styles.css`** | **absent** | present |
| **`shared/nav.css`** | **absent** | present |
| 3D Studio CSS | `_ds_bundle.css` **and** `tokens/src-styles-tokens.css` | absent |

`shared/ks3.css` and the `_ds` bundle's `tokens/shared-ks3.css` are **byte-identical** (verified by
`diff`, exit 0). That is the design-delivery shape already recorded: the bundle re-ships the repo's
own KS3 CSS, and the real design lives in the page's inline styles.

b1-03's **F14** and **F17** both reproduce, to the same numbers, on a fifth page:

| | reference | generated (b1-05's, the nearest built page) |
|---|---|---|
| `.ks3-rung h3` | 23px / **36.8px** (1.6) | 23px / 26.45px (1.15) |
| ladder `h2` | 36px / **57.6px** (1.6) | 36px / 43.2px (1.2) |

### 1.6 ⚑ FINDING F30 — `[data-bench-grid]` matches nothing on this page

Measured: **`document.querySelectorAll('[data-bench-grid]').length === 0`**, at all four viewports.

Lines 20–21 declare the bench grid and its collapse:

```css
[data-bench-grid] { grid-template-columns: minmax(0, 232px) minmax(0, 1fr); }
@media (max-width: 820px) { [data-bench-grid] { grid-template-columns: minmax(0, 1fr); } }
```

**Neither selector matches an element.** The page's only two-column-ish layout is
`[data-compare-grid]` (8 matches), which is a `flex-wrap` row with its own threshold, and the
microscope's control cluster, which is a plain `display:flex; flex-wrap:wrap`. Design carried the
bench-grid boilerplate forward from b1-03/b1-04 and did not use it.

**This changes the evidence under drifts 1 and 2 in `00-delivery-drift.md`, and it must be recorded
rather than quietly absorbed.**

| Drift | Stated count | Live count once dead CSS is excluded |
|---|---|---|
| 1 — control column 232 / 240 | 232 × 2 (b1-04, b1-06), 240 × 1 (b1-03) | **232 × 1 live, 240 × 1 live, 232 × 1 dead** — a 1 : 1 tie |
| 2 — collapse 780 / 820 | 780 × 2, 820 × 1 (b1-06) | **780 × 2 live, 820 × 0 live** on this selector |

- **Drift 1's majority is gone.** It was 2 : 1 for 232px; among declarations that style a real
  element it is 1 : 1. The ruling ("majority, and nothing else distinguishes them") no longer rests
  on a majority. The tie-break the file offers as secondary — that both are on the 8px step and the
  difference carries no semantic content — still holds, so **232px is still a defensible answer**,
  but it is now a coin-toss with a reason rather than a count. **Flagged for Mide, §8(b)/(c); not
  resolved here.**
- **Drift 2's ruling is unaffected, and its stated basis was already the right one.** The file rules
  820px *against* the count on the grounds that "820px is already a ruled threshold on that page,
  for a different component" — the comparison rows. That is exactly right, and it is now the *only*
  reason: b1-06's `[data-bench-grid]` 820 is inert, so the count among live bench-grid declarations
  is 780 × 2, 820 × 0. The one-threshold-per-page argument survives intact — **b1-06 does have a
  live 820px threshold** (§3.4.2), and it is the most recently considered narrow-width decision in
  the delivery. **The ruling stands; one sentence of its evidence needs correcting.**

Everything else in `00-delivery-drift.md` checks out against measurement:

| Drift | Ruling | Checked here |
|---|---|---|
| 3 — statement type | `clamp(28px, 3.9vw, 44px)` | b1-06 line 217 is `clamp(26px, 3.6vw, 40px)`, measured **40px @1280/1340, 29.52px @820, 26px @390**. It is a real statement (the `#s-compare` display line), so it is one of the four occurrences the corrected drift 3 counts. ✔ evidence reproduces |
| 4 — `seg()` light branch | b1-06's variant | Source 893–895 and measured: 17px / 700 / `11px 17px` / `min-height 44px` / `--ks3-r-control` 14px, accent + accent-tint on, option-border + ground off. **The dark branch (889–891) is the same geometry with `--ks3-alert`** — measured on the mount tabs: `background rgb(255,197,61)`, `color rgb(34,30,27)` on; `transparent` on `--ks3-on-dark-muted` off. ✔ the "one helper, one geometry, two grounds" argument reproduces exactly |
| 5 — KEY FACT ground | `var(--ks3-band)` | b1-06 line 240 is `var(--ks3-card)`, measured `rgb(255,252,245)`. **This page is the outlier, confirmed.** §3.4.4 records why the outlier is not arbitrary here and why that does not change the ruling |

---

## 2. The progress rail — same component as b1-01/03/04/05, **four** stages

Byte-for-byte the component b1-01 §2 specified. Confirmed by measurement, not re-derived:

- **Two variants, never both, never neither.** Bisected: at **1339** `[data-rail="side"]` is
  `display:none` and `[data-rail="top"]` is `display:block`; at **1340** the reverse. Same two
  authored rules (source lines 31–32).
- **Side rail geometry identical:** `fixed`, `top 150px`, `left calc(50% − 632px)` → **x 38** at
  1340, `width 104px`, `z-index 20`; `.ks3-lesson` starts at **x 190** → a 48px gutter. Height
  **326.75** for four nodes. Against b1-05's 416.94 for five, that is **90.19px per node** —
  confirming b1-05's assertion that rail height is a pure function of node count, and giving the
  step: `h = 32 + (n−1) × 90.19` to within a rounding.
- **Chip states identical, every colour a token.** Measured across a full drive:
  done = `--ks3-accent` #E4572E ground, `--ks3-ink` border, `--ks3-on-dark` text, holds
  `svg.ks3-mark` (`hasMark: true`, `chipTxt: ""` — the number is *replaced* by the tick);
  current-not-done = `--ks3-card` #FFFCF5 on `--ks3-ink` with `box-shadow: 0 0 0 4px
  --ks3-accent-tint` (measured `rgb(252,231,222) 0 0 0 4px`); future = `--ks3-card` on
  `--ks3-rule-strong` #C3B191 with `--ks3-ink-ghost` #9A8F86 text. Chip 32×32, r10, Bricolage
  16px/800, border 2px.
- **Label** MONO 11px/500, `letter-spacing .09em` (0.99px), uppercase, lh 1.2; current `--ks3-ink`,
  done `--ks3-ink-muted`, future `--ks3-ink-ghost`.
- **Connector** 2×20 at `margin 7px 0`; `--ks3-accent` when the node above is done, else `--ks3-rule`.
  Omitted on the last node (`hasLine: i < RAIL.length - 1`).
- **Top bar** `sticky; top 0; z-index 20; background --ks3-ground; border-bottom 2px --ks3-rule;
  padding 9px 16px 10px`; inner row `flex; gap 12px; max-width 60rem; margin 0 auto`; count MONO
  15px/500 `--ks3-ink-muted`; current label 16px/700 `--ks3-ink` with ellipsis (measured **795px**
  at 1280); track `flex 0 0 96px`, height 8px, r99, `--ks3-band` ground, `2px --ks3-ink`, inner
  **92px**; fill `--ks3-accent`.

### 2.1 Four stages, and their two label sets

`RAIL` 427–432 + `RAIL_SHORT` 434:

| # | anchor | side label (`RAIL_SHORT`) | top-bar label (`RAIL[].label`) | `done_when` (`isDone`, 436–442) |
|---|---|---|---|---|
| 1 | `#s-hook` | HOOK | What settles it | `s.hookChoice !== null` |
| 2 | `#s-scope` | SCOPE | Two slides | `!!s.seenScope['pond:400'] && !!s.seenScope['cheek:400']` |
| 3 | `#s-settle` | SETTLE | Four mystery cells | `Object.keys(s.caseOpen).length >= 4` |
| 4 | `#s-ladder` | LADDER | Mastery ladder | `answers.r1 !== null && answers.r2 !== null && checked.r3 && checked.r4` |

Both label sets are authored and neither is derivable from block titles. `RAIL_SHORT` is ≤6 chars,
consistent with all four earlier pages — worth asserting, because the 104px column at MONO 11px
`.09em` is what sets the limit.

Fill maths is `(active + 1) / 4 × 100%` — measured **25 / 50 / 75 / 100 %** giving **23 / 46 / 69 /
92** of the 92px inner track.

**All four stages are reachable and I drove all four to done, in order.** Four notes, all measured:

- **Stage 2 is honest and is the best `done_when` in the delivery so far.** It names two specific
  states — `pond:400` *and* `cheek:400` — not a count and not a downstream boolean. Driven: after
  ×40 objective on pond it read `1 of 2 mounts seen at ×400` and SCOPE stayed grey; after switching
  the mount to cheek it read `2 of 2` and SCOPE ticked. The block's own counter and the rail agree
  exactly, which is the pattern b1-05 §2.1 asked for.
- **Stage 3 is honest.** `caseOpen` is keyed by case id, there are exactly 4 cases, and each key can
  only be set by a reveal whose own guard requires all four features marked. Driven: SETTLE ticked
  only after the fourth case was revealed.
- **⚑ Stage 4 ticks for a button press, twice over.** `checked.r3` and `checked.r4` are set by
  pressing **"Check my answer"** — with an empty textarea and zero criteria ticked. Driven at 1340:
  after answering r1 correctly, r2 **wrongly**, and pressing both check buttons without ticking
  anything, the LADDER chip went **done** while the score read *"You got 1 of 4."* and both tallies
  read *"0 of 5 ticked — not yet."* / *"0 of 4 ticked — not yet."* This is b1-05's **F25** in a new
  place: `done_when` cannot name a threshold, so it watches the cheapest available boolean. Finding
  **F31**.
- **⚑ Stage 4 can regress, and it is the first stage in the delivery that can.** `onRetry`
  (1134–1138) resets `answers`, `checked` and `ticks`. Driven: after all four stages were done,
  pressing "Retry my misses" put LADDER back to a grey `4` chip and the score back to *"You got 0 of
  4."* b1-05 §2.1 recorded "no stage can regress" as a property of that page; **it is not a property
  of the family.** The generator's rail model must decide whether a stage is monotonic or live.
  Finding **F32**, §8(c) — Code can decide, because Design's page is unambiguous about what happens;
  what is undecided is only whether the generator's `done_when` vocabulary needs a `monotonic` flag.

### 2.2 F2 reproduced, on four stages

b1-01's F2 ("the top bar shows scroll, not completion") reproduces exactly. Driven at 1280 with
`scrollIntoView` at each anchor and **nothing answered**:

| scrolled to | count | label | fill style | fill px |
|---|---|---|---|---|
| `#s-hook` | 1 / 4 | What settles it | `width: 25%` | 23 / 92 |
| `#s-scope` | 2 / 4 | Two slides | `width: 50%` | 46 |
| `#s-compare` | 2 / 4 | Two slides | 50% (**stale**) | 46 |
| `#s-settle` | 3 / 4 | Four mystery cells | `width: 75%` | 69 |
| `#s-think` | 3 / 4 | Four mystery cells | 75% (**stale**) | 69 |
| `#s-ladder` | **4 / 4** | Mastery ladder | **`width: 100%`** | **92 / 92 (full)** |
| `#s-keynote` | 4 / 4 | Mastery ladder | 100% (stale) | 92 |

`#s-compare`, `#s-think` and `#s-keynote` are anchored but unlisted, so the `IntersectionObserver`
(`rootMargin: '-45% 0px -50% 0px'`, lines 638–644) never fires for them and the bar sits stale
through them. **A student under 1340px reads a complete progress bar having answered nothing**, and
the side rail — the variant that does read completion — is the one they cannot see. Still F2.

⚑ Against b1-05's note that five stages makes it "slightly better", **four makes it slightly worse**:
each scroll step is 25%, so the bar reaches 100% three sections before the end of the page, and it
does so while *three* unlisted anchored sections sit downstream of the last listed one. The defect is
unchanged in kind. **The fix is not a stage count.**

### 2.3 Anchors

**All 7 lesson sections carry `scroll-margin-top: 92px`**, authored individually as an inline style
on each (`s-hook`, `s-scope`, `s-compare`, `s-settle`, `s-think`, `s-ladder`, `s-keynote`). The rail
references **4 of the 7**. `#dc-root` and the form-control ids carry 0. `.ks3-layer`,
`.ks3-endmatter` and `p.ks3-legal` carry no anchor.

Full id list measured **at load**: `dc-root`, `s-hook`, `s-scope`, `s-compare`, `s-settle`,
`s-think`, `s-ladder`, `ans-r3`, `ans-r4`, `s-keynote` — **10**. An eleventh, **`b6focus`** (the
focus range input, line 189), exists only once the gate has been answered and `scopeOpen` is true.

⚑ Note the contrast with b1-05's **F26**: that page has a bare `id="zoom"` on a form control;
this one uses `id="b6focus"` and `id="ans-r3"` / `ans-r4`. So the delivery carries **three different
id conventions for form controls** — bare (`zoom`), lesson-prefixed (`b6focus`), and role-prefixed
(`ans-r3`). The generator's convention is `ks3-<thing>-<slug>-<field>`, which matches none of them.
F26 stands, with a second data point.

### 2.4 What the generator needs to emit it

Identical shape to b1-01 §2.6 and b1-03/04/05 §2.4, four entries:

```python
"rail": [                                     # NEW field, §5 gap G1
  {"anchor": "s-hook",    "short": "HOOK",   "label": "What settles it",
   "done_when": "committed"},
  {"anchor": "s-scope",   "short": "SCOPE",  "label": "Two slides",
   "done_when": "states_seen",                # ⭐ names states, not a count
   "states": ["pond:400", "cheek:400"]},
  {"anchor": "s-settle",  "short": "SETTLE", "label": "Four mystery cells",
   "done_when": "all_cases_revealed", "threshold": 4},
  {"anchor": "s-ladder",  "short": "LADDER", "label": "Mastery ladder",
   "done_when": "ladder_complete"},           # ⚑ F31 — currently a button press
]
```

`scroll-margin-top: 92px` must be emitted on **every** id-bearing section, not only rail stages.

---

## 3. Every block in document order

`GEN?` — **E** the generator has this block type · **E★** existing type, but this page uses it in a
shape the renderer cannot produce · **N** new. Component names in the last column are
`ks3_parity.COMPONENTS` entries (60 registered) that would gate it.

| # | Block | GEN? | States | Gating components |
|---|---|---|---|---|
| 1 | `header.ks3-lesson-head` — eyebrow "Cells and organisation · Contrast", h1, `.ks3-bigq`, `.ks3-review-flag` | **E** | draft flag present / absent (`showDraft` prop) | lesson title · big question · eyebrow · draft badge |
| 2 | `#s-hook` — ink-dark: eyebrow, h2, prompt, `.ks3-hook-commit` with `.ks3-commit`, 4 `.ks3-option`s, gated `.ks3-reveal` | **E★** | option resting / chosen (border + badge → `--ks3-alert`); reveal hidden / shown | hook is ink-dark, accent shadow · dark-block option resting/CHOSEN |
| 3 | `#s-scope` — **the microscope bench**: a commit gate, 4 dark control groups, an 1800×1120 canvas, a fine-focus slider, a 3-panel readout, 3 prose notes (§3.3) | **N** (engine exists, control surface does not) | gate closed / open · 2 mounts × 3 objectives × 3 centres × motion on/off × 101 focus steps | `sim canvas` gates `practical` today and there is **no `.ks3-sim` here** |
| 4 | `#s-compare` — **the comparison table**: unclassed band section, display statement, dark header row, 7 data rows, KEY FACT box (§3.4) | **N** | wide (3 columns) / narrow (stacked, captioned) | **none registered** |
| 5 | `#s-settle` — **the "settles it" activity**: 4 case tabs, a case panel, 4 feature rows × 2 marks, a gated reveal (§3.5) | **N** | 4 cases × 4 features × (unmarked / SETTLES IT / SETTLES NOTHING) × (pre-reveal / post-reveal) | **none registered** |
| 6 | `#s-think` — misconception carrying **two** quote/answer pairs split by an `--ks3-alert-border` rule | **E★** | static, both open | misconception is amber |
| 7 | `#s-ladder` — `class="ks3-ladder"`, head + score, 2 page-marked rungs, 2 self-marked rungs, `.ks3-retry-wrap` | **E** | option resting / correct / wrong / spent; feedback correct / wrong; ticks 0..5 and 0..4; tally not-yet / met; retry | ladder shell · ladder heading · ladder option ×6 states+badges · ladder feedback CORRECT/WRONG · page-marked rung is accent · self-marked rung is violet · R8 answer box · R8 check-my-answer button |
| 8 | `#s-keynote` — ink-dark, alert-yellow shadow, **`p.ks3-eyebrow`** + one paragraph | **E★** | static | key note is ink-dark · key note type drops to 700 |
| 9 | `.ks3-layer` — "Going further" violet stretch layer, **one bare `<p>`** (Euglena) | **E★** | static | stretch layer is violet |
| 10 | `.ks3-endmatter` — **4 cards**: "Before this lesson" (1 link) · "Connects to" (2 links) · "At GCSE this becomes" (**prose**) · `.ks3-tutor` (**live `<a href="#s-settle">`**) | **E★** | static | tutor card is accent · tutor text is large-bold |
| 11 | `p.ks3-legal` — **lab safety**, not copyright | **E★** | static | — |

Totals: **2 blocks the generator can already produce (E)**, **6 it produces in the wrong shape
(E★)**, **3 it cannot produce at all (N)**. Three of the four rail stages sit inside N blocks.

### 3.1 Against the generator's current record — in brief

The full component-by-component comparison against a built page was done on b1-05 §3.1 and its
conclusions (D1–D8, the shells agreeing to the pixel, F14/F16/F17) reproduce here; they are not
re-derived. What is specific to this lesson:

| | Design (b1-06) | Generator (`ks3_data/biology_b1_cells.py`, from line 2000) |
|---|---|---|
| Big question | *"Two single cells, the same size. One is a whole animal. One is a piece of you. What tells them apart?"* | *"How can one single cell be a whole living thing?"* |
| Blocks | 11 children, **3 of them one-off instruments** | 16 blocks: `hook · check · explainer · misconception · practical · figure · check · misconception · figure · keyword · check · check · quiz · summary · explainer · check` |
| Sim | inline microscope, 2 mounts, 4 control groups | `{"kind": "microscope", …}` inside a `practical` |
| Comparison | a 7-row two-column table with two states | a `figure` (`b1-unicellular-adaptations`, `kind: schematic`) — a pending placeholder |
| The discrimination skill | `#s-settle`, 16 marked judgements across 4 cases | one `check` (*"What does unicellular mean?"*) with distractor corrections |
| `key_note` | present, authored (line 378) | **present** in the record but a different sentence |
| `tutor_anchor` | `#s-settle` — sixth authored anchor across five pages | **field does not exist** |
| `rail` | 4 stages, two label sets | **field does not exist** |
| `references` | "Connects to" carries 2 links | `[]` — the card cannot render |

The generator's record shares a title, a slug, a family and the `unicellular` / `multicellular`
vocabulary. **Every one of Design's 2,490 words is new content**, and whether any of the generator's
current wording survives is Mide's call (§8(b)).

**D7 confirmed for a sixth time:** Design's tutor CTA is
`<a class="ks3-tutor-cta" href="#s-settle">Ask about this lesson</a>`, 18px/600, `--ks3-card` on
`--ks3-accent-text`, r12, `padding 10px 17px`; heading *"Ask Mr Badmus AI"*; line *"Not sure which
fact settles it?"* Design's anchor points into its own page on **every page inventoried** —
`#s-bench`, `#s-rule`, `#s-hard`, `#s-settle`. `tutor_anchor` is a real authored field, not a
one-off.

**D4 confirmed:** keynote heading is `<p class="ks3-eyebrow">Key note</p>` rendering Bricolage
**30px / 700 / UPPERCASE / `--ks3-alert` #FFC53D**, and the keynote body is also 30px / 700
Bricolage — the two are the same size, which is the family's treatment and not a slip.

### 3.2 `#s-hook` — the commit that stays in the dark block

`.ks3-block ks3-dark ks3-hook`: `--ks3-ink` #221E1B ground, no border, r30, `6px 6px 0 #E4572E`,
padding 32px, measured 960 × 612.84 at 1280.

| Part | Measured |
|---|---|
| `h2` (no class) | 38px / 39.9px, `--ks3-on-dark` #FBF3E6 |
| `.ks3-hook-prompt` | inherited body 19px |
| `.ks3-commit` | 22px, `--ks3-on-dark-body` #E7DECE |
| `.ks3-options` | 4 `.ks3-option`, `padding 16px 18px`, `min-height 44px`, r16, `2px --ks3-on-dark-muted` #C6B9A7 on `--ks3-dark-panel` #3E3730, 18px/600 `--ks3-on-dark`, `display flex`, `gap 14px` |
| `.ks3-opt-mark` | 28 × 28, r9, `--ks3-on-dark-muted` ground, 15px/800, `--ks3-ink` glyph |
| **chosen** | border → `--ks3-alert` #FFC53D **and** badge ground → `--ks3-alert` with the glyph staying `--ks3-ink`; **button ground, radius, padding and size unchanged** (measured `rgb(62,55,48)` in both states); `aria-pressed="true"`; **no drawn mark** |
| `.ks3-reveal` | `--ks3-dark-panel` ground, `2px --ks3-alert`, r18, `padding 18px 20px`, 19px `--ks3-on-dark`, arrives under `[data-arrive="1"]` |

**No new component.** Every value above is the registered dark-block option and the registered dark
hook. The only thing the generator cannot do is *put them there* — its hook block has no options.

**On MRB-202 / R3, and b1-05's F27.** This page has the same single-static-reveal structure: the
reveal is gated only on `hookChoice !== null` (line 112) and there is no per-option branching. Driven
twice from clean loads, clicking **A** and clicking **D** produce byte-identical reveal text. But the
wording here does **not** endorse:

> Three of those four are true of a Paramecium and settle nothing. Telling which fact does the work
> is the whole of this lesson.

Options (data, 958–962): A *"It can move on its own"* · B *"It has more structures inside it"* ·
C *"It carries out all seven life processes by itself"* · D *"It lives in water instead of inside a
body"*. The reveal tells every student that three of the four settle nothing, **without saying which
three**. So it defers *and* refuses to endorse, which is the wording b1-05's F27 asked for. ⭐
**This is the pattern the family should inherit**, and it is worth putting in front of Design as the
answer to F27 rather than leaving F27 open: b1-05's *"Keep it."* endorses a flatly wrong option;
b1-06's reveal does not endorse anything. Recorded in §8(a).

### 3.3 ⭐ `#s-scope` — the microscope bench, and what the repo engine is missing

`.ks3-block ks3-dark ks3-practical`: `--ks3-ink` ground, no border, r30, **`6px 6px 0 #2F5CE0`**,
padding 32px. Measured 960 × 594.72 with the gate closed, **1506.06** at ×4 pond once open, 1485.28
at ×400.

**The physics is settled and is NOT re-derived here.** MRB-210 reconciled one engine against this
page on Mide's ruled depth table — `0.100 / 0.040 / 0.008 mm` at `×40 / ×100 / ×400`, which is this
page's own `OBJS` (lines 445–449) — and that table now governs all of KS3. `shared/ks3.js` carries
it as `OBJ_DOF_MM`, with `FOCUS_MIN_MM = -0.09`, `FOCUS_SPAN_MM = 0.18` and `SHARP_FRACTION = 0.6`,
all of which match this page's `focusDepth()` (line 670) and its `Math.abs(fd - p.depth) < o.dof *
0.6` sharpness test (line 910) exactly. The three MRB-210 reconciliations are confirmed present in
the repo engine: the cheek smear is one layer, the 54 bacteria are on this page's own deterministic
LCG (`n = (n * 1103515245 + 12345) % 2147483648`, lines 462–475) and are excluded from the in-focus
readout, and the seven pond organisms carry this page's authored depths.

#### 3.3.1 The commit gate

Before the instrument appears, `gateOpen: s.gate === null` shows a commit (line 132):

> Commit first. At which magnification will you first be able to tell one pond organism from another?

Four dark `.ks3-option`s (data 971–975): A *"×40 — the lowest power"* · B *"×100"* ·
C *"×400 — the highest"* · D *"You never can with a school microscope"*. Measured resting:
`--ks3-dark-panel` #3E3730 on `2px --ks3-on-dark-muted` #C6B9A7, r16, `16px 18px`, `min-height 44px`,
18px/600, badge 28×28 r9.

**Gating is by absence, both ways.** `gateOpen` and `scopeOpen` are complementary
(`s.gate === null` / `s.gate !== null`), so answering the gate **removes the question** and reveals
the bench in one step. Measured: after a click, `document.querySelector('#s-scope .ks3-commit')` is
`null`. Same "hide, don't veil" discipline b1-04 and b1-05 recorded — third page, settling.

⚑ The gate is a **prediction with no marked answer and no reveal at all**. The student commits and
the question vanishes; nothing ever tells them whether ×400 was right. The instrument itself is the
answer (`RESOLVE[100]` says outlines let you tell one kind from another). That is R3-clean, but it
means the gate's four options are the only place in the delivery where a commit produces *no*
response of any kind. **Ambiguity for Design, §8(a): is the silence deliberate?**

#### 3.3.2 The control surface as drawn, against the repo engine

Four control groups, each a MONO 14px/500 `.07em` uppercase `--ks3-on-dark-muted` caption over a
`flex; gap 9px; wrap` row of `seg(on, true)` buttons (17px / 700 / `11px 17px` / 44px / r14; on =
`--ks3-alert` ground and border with `--ks3-ink` text; off = `transparent` on `--ks3-on-dark-muted`
with `--ks3-on-dark` text).

| # | Group caption | Buttons | Repo engine equivalent? |
|---|---|---|---|
| 1 | **Mount** | `Pond water` · `Cheek cells` | ⚠️ **Partial.** The engine renders one specimen per `sim` payload and classifies it by name (`specimenKind()` — `pond` / `cheek` / `onion` / `bubbles`). It has no concept of **two mounts on one instrument** and no tab to swap between them. |
| 2 | **Objective** | `×4` · `×10` · `×40` | ✅ **Yes.** `OBJECTIVES` / `OBJ_DOF_MM`, index-matched, plus MRB-198's non-parfocal `OBJ_FOCUS_SHIFT = [0, 10, 22]` which Design's page does not have (Mide ruled 13 Aug that it stays). |
| 3 | **Move the slide to** | `The blob` · `The slipper` · `The green spindle` | ❌ **No.** `shared/ks3.js` line ~1406 says so in as many words: *"Design's page holds the cast still and gives the student a `centre` control to pan to each one. This engine has no centre control, so the organisms SWIM."* |
| 4 | **Movement** | one toggle: `Swimming` / `Held still` | ❌ **No.** The engine's motion is unconditional (subject only to R6 reduced-motion, which draws the settled frame). There is no student-facing on/off. |

Plus the **fine-focus wheel**, inside the canvas frame's caption strip: `input[type="range"].b6-focus`,
`min 0 max 100 step 1 value 50`, measured **856 × 40** at 1280, with an author-styled track (10px,
r99, `--ks3-dark-panel` ground, `2px --ks3-on-dark-muted`) and thumb (28 × 28, 50%, `--ks3-alert`
ground, **`3px solid --ks3-ink`**, `margin-top −11px`), declared twice — `::-webkit-slider-*` and
`::-moz-range-*` (lines 34–38). Its `<label for="b6focus">` is `position: absolute; left: -9999px` —
visually hidden, correctly present for a screen reader. ✅ The repo engine has a focus wheel.

⚑ **This is the second range input in the delivery** (b1-05's `b5-zoom` was the first) and the second
place a page-local CSS class is required, because pseudo-elements cannot be set from an inline
`style=`. b1-05's **F29** — "the generator must emit it as real CSS, not as an inline attribute" —
now has two instances and is therefore a rule, not a special case.

#### 3.3.3 What the two missing controls need

**The centring / pan control.** Data: `CENTRES` (477–481), 3 entries × `{id, label, x, y}` where
`x, y` are millimetres on the slide and are **copies of the first three `POND` entries' positions**.
`draw()` uses it at line 820: `ctr = pond ? (CENTRES.find(k => k.id === state.centre) || CENTRES[1])
: {x: 0, y: 0}`, and every organism is placed at `cx + (p.x − ctr.x) * pxPerMm`. So panning is a
pure translation of the field, applied only on the pond mount.

- `centreOffered: pond` (line 995) — **the group disappears entirely on the cheek mount.** Measured:
  four control groups on pond, three on cheek.
- Driven: clicking "The blob" pans the amoeba to the centre and leaves the readout reading
  **"the slipper"**, because the focus wheel is still at 50 (depth 0.000, the paramecium's plane) and
  the amoeba sits at −0.045. ⭐ **That is the pedagogy**: centring and focusing are two separate
  operations, and the instrument makes the student do both. The engine, which swims the organisms
  instead, cannot teach that.
- What the generator needs: a `centres` list on the sim payload, `[{id, label, x, y}]`, and a
  `centre_offered_on` mount filter. The labels (*"The blob"*, *"The slipper"*, *"The green spindle"*)
  are authored teaching language — they are how the lesson refers to an organism the student cannot
  yet name — and must not be derived from `kind`.

**The motion toggle.** State `motion: this.props.motionDefault !== false` (line 625), label
`s.motion ? 'Swimming' : 'Held still'`, and `moving()` (660) gates both the animation loop and every
per-organism detail that depends on `t`. With motion off the cilia stop waving, the contractile
vacuoles freeze mid-cycle and the euglena stops bending — the drawing is still complete, just still.

- Measured off-state: `aria-pressed="false"`, `transparent` on `--ks3-on-dark-muted`.
- ⚑ It doubles as a **reduced-motion escape hatch that the student controls**, on top of the
  `prefers-reduced-motion` media query. R6 says reduced motion must be a complete experience; this
  control says the student may *choose* stillness even when the OS has not asked for it. The repo
  engine honours R6 but gives the student no choice.
- What the generator needs: `motion_toggle: true` plus `motion_default` on the sim payload, and the
  two authored labels. **The labels are content** — *"Swimming"* / *"Held still"* is a Paramecium
  vocabulary choice, not a generic on/off.

#### 3.3.4 The canvas and the readouts

| Property | Measured @1280 |
|---|---|
| buffer | **1800 × 1120** |
| CSS box | **892 × 555.02** |
| device px per CSS px | **2.018** — crisp at 1× and 2× |
| design space | 900 × 560, via `ctx.setTransform(2,0,0,2,0,0)` |
| field | a circular clip of radius `min(W,H) × 0.45`, on `#100D0A`; pond ground `#E9EFE5`, cheek `#EBE4D6` |
| bezel | two strokes — `lineWidth 11` `#100D0A`, then `lineWidth 3` `#4A4038` |
| frame | `--ks3-r-card` 22px, `2px solid --ks3-on-dark-muted`, `overflow: hidden` |
| caption strip | **inside the frame**: `--ks3-dark-panel` ground, `border-top 2px --ks3-on-dark-muted`, `padding 14px 18px 16px`, holding the "Fine focus" caption, the focus readout and the slider |
| a11y | `role="img"`, `aria-label="{{ scopeAlt }}"` — two authored strings, 1018–1020 |

**Three readout panels**, in a `grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap
12px`, each `--ks3-dark-panel` / `--ks3-r-panel` 20px / `padding 15px 17px`, MONO 13px `.07em`
uppercase `--ks3-on-dark-muted` label over a value:

| Panel | Value type | Measured |
|---|---|---|
| Total magnification | MONO **25px** / 500 `--ks3-on-dark` | `×40` / `×100` / `×400` |
| Field of view | MONO **25px** / 500 | `4.50 mm` / `1.80 mm` / `0.45 mm` — `o.fov.toFixed(2)` |
| In focus | **body 19px / 700** `--ks3-on-dark` | `the blob, the slipper, the green spindle` / `the slipper` / `nothing sharp` / `the whole smear` |

Plus a fourth readout in the caption strip: `focusLabel`, MONO **16px** `--ks3-alert`, reading
`between layers` or `sharp: <names>`.

**Focus sweep driven at ×400 on pond**, 7 positions — the discrimination the lesson depends on:

| slider | depth (mm) | In focus |
|---|---|---|
| 0 | −0.090 | nothing sharp |
| 25 | −0.045 | the blob |
| 44 | −0.011 | nothing sharp |
| 50 | 0.000 | the slipper |
| 56 | +0.011 | the green spindle |
| 75 | +0.045 | nothing sharp |
| 100 | +0.090 | nothing sharp |

At ×400 the sharp window is `0.6 × 0.008 = 0.0048 mm`, i.e. **±2.7 slider units** — the student
cannot hold two organisms sharp at once, which is the point. At ×4 (`0.6 × 0.100 = 0.060 mm`,
±33 units) all three are sharp simultaneously, measured at slider 50.

**Three authored prose notes** below the instrument, all live-switched:

- `resolveNote` (`RESOLVE`, 483–487) — on `--ks3-ground` inside the dark block, `padding 17px 19px`,
  `--ks3-r-panel`, 19px `--ks3-ink`, prefixed by a display-font `<strong>What you can resolve:</strong>`.
  **⭐ This is the only cream-on-dark inset in the delivery** and it is where the lesson's answer to
  its own gate lives.
- `mountNote` — 18px `--ks3-on-dark-body`, two strings (1012–1014). The pond one carries the bacteria
  fact; `shared/ks3.js` already ships it as `BACTERIA_NOTE`.
- `scopeCaption` — MONO 15px `--ks3-on-dark-muted`, two strings (1015–1017). ⭐ **The pond caption is
  the page telling the truth about its own model**: *"Real ones swim out of the field in seconds.
  These are held for you, and the slide moves when you ask it to."* That sentence **is the
  justification for the centre control and against the engine's swimming**, and it is exactly the
  kind of sentence §8.10 permits — it is about the specimen, not about the platform's build order.

⚑ **FINDING F33 — the page wins over the engine on motion, in words.** Standing law: *"Where the page
teaches one thing in words and the engine does another, the page wins."* Line 1016 states in student-
facing prose that the organisms are held still and the slide moves on request. The repo engine does
the opposite — it swims them and has no slide. This is not a preference to be reconciled; the
approved page contains a sentence the engine contradicts. §8(c) — Code's, because the resolution is
already ruled.

### 3.4 ⭐ `#s-compare` — the comparison rows, both states (MRB-210)

An unclassed `<section>` (line 215) styled entirely inline: `background: var(--ks3-band)` #F4E9D8,
`border: 3px solid var(--ks3-ink)`, `border-radius: var(--ks3-r-block)` 28px, `padding: 34px 32px`.
Measured 960 × 1024.36 at 1280. **It is the only band-ground block in the delivery.**

Its parts, in order:

1. `p.ks3-eyebrow` with an inline `color: var(--ks3-accent-text)` override — "Side by side".
2. **The statement**, line 217: `--ks3-font-display` 800, `clamp(26px, 3.6vw, 40px)`, `line-height
   1.1`, `letter-spacing -.03em`, `max-width: 26ch`. Measured **40px / 44px / −1.2px** at 1280 and
   1340 (671.83 × 88), **29.52px** at 820, **26px** at 390. This is drift 3's fourth statement.
3. **The table** — a `--ks3-card` box with `2px --ks3-ink`, `--ks3-r-card` 22px, `overflow: hidden`,
   holding 1 header row + 7 data rows.
4. **The KEY FACT box**, §3.4.4.

#### 3.4.1 The row mechanism, at the root and not in a query

Design fixed the rows at the root under MRB-210. Source lines 22–24:

```css
[data-compare-grid] { display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: flex-start; }
[data-compare-grid] > [data-compare-label] { flex: 0 0 118px; }
[data-compare-grid] > [data-compare-cell]  { flex: 1 1 250px; min-width: 0; }
```

All three verified by `getComputedStyle`: `display: flex`, `flex-wrap: wrap`, `gap: 10px 14px`,
label `flex: 0 0 118px`, cell `flex: 1 1 250px`, `min-width: 0px`. **Every declaration MRB-210
records is present in the delivered file and resolves as stated.**

Row chrome, measured on a data row: `padding: 15px 14px`, `border-top: 2px solid --ks3-rule`
#E0D2B9, `align-items: start`, and a zebra from `renderVals` line 1024 — `i % 2 ? var(--ks3-inset)
: var(--ks3-card)`, measured `rgb(255,252,245)` / `rgb(247,239,225)` alternating across the 7 rows.
Label MONO 14px/500 `.04em` uppercase `--ks3-ink-muted`; `uni` cell 18px/1.5 `--ks3-ink`; `multi`
cell 18px/1.5 **`--ks3-ink-body`** — the multicellular column is deliberately one step quieter.

#### 3.4.2 The narrow state, and its threshold

Lines 26–30, `@media (max-width: 820px)`:

```css
[data-compare-grid] > [data-compare-label] { flex: 1 1 100%; }
[data-compare-head] { display: none; }
[data-compare-cap] { display: block; margin: 0 0 3px; font-family: var(--ks3-font-mono);
                     font-size: 12px; font-weight: 500; letter-spacing: .07em;
                     text-transform: uppercase; color: var(--ks3-accent-text); }
```

**Bisected: at 821 the dark header row is `display: flex`; at 820 it is `display: none`.** The
threshold is exact and it is a viewport query, measured by device-metrics override as the README
requires.

Every stacked cell then grows its own caption, so no sentence is orphaned from its subject. Measured
at 820: `[data-compare-cap]` computed **MONO 12px / 500 / 0.84px letter-spacing / uppercase /
`--ks3-accent-text` #A93411 / `margin 0 0 3px`** — every declaration as authored. The two caption
strings are `Paramecium` and `One of your cheek cells`, hard-coded once per cell in the row template
(lines 229 and 233) and **duplicating the header row's two labels** (222–223).

#### 3.4.3 ⚑ MRB-210's numbers, verified — three of five do not reproduce

The task asked for every number to be checked. Here is the check, honestly.

| MRB-210's claim | Verdict | Measured |
|---|---|---|
| `scrollWidth === clientWidth` | ✅ **Reproduces, everywhere** | section 954 = 954 @1280 · 954 = 954 @1340 · 766 = 766 @820 · **352 = 352 @390**; table 886/886, 698/698, 284/284; `document.documentElement` 1280/1280 … 390/390. **No horizontal overflow at any viewport or container width tested.** |
| the wide layout is unchanged at **118 + 315 + 315** | ⚠️ **Shape yes, number no** | At 1280 and 1340 the real page measures **118 + 356 + 356** (row content 858 = 118 + 356 + 356 + 2 × 14 gap). 315 corresponds to a `.ks3-lesson` of **878px**, which no ruled viewport produces — confirmed by a container sweep: 846 → 299, **878 → 315**, 926 → 339. So the figure was taken in a probe container, not at the reference width. |
| cells go from **26 × 297px** slivers … | ❌ **Not verifiable** | That is the *pre-fix* geometry. The delivered file at `docs/ks3/design-reference/b1/` **already carries the fix** (lines 22–30). There is no pre-fix copy in the repo, so the before-numbers cannot be reproduced against the provenance anchor. |
| … to **211 × 81px** readable blocks at a 360px container | ⚠️ **Shape yes, number no** | At `.ks3-lesson: 360px` the cells measure **258 × 81** and **258 × 54**. 258 is the exact row content width for a 360px lesson (360 − 6 border − 64 padding − 4 border − 28 padding). 211 corresponds to a **313px** lesson. The **81px height reproduces exactly**, which is the number that carries the claim. |
| section height **3330px → 2366px** | ⚠️ **Neither reproduces** | Before: not verifiable (above). After, at `.ks3-lesson: 360px`: **2151.75**. At the 390 viewport: **2232.36**. At 820: 1328.52. At 1280/1340: 1024.36. |

**Reading.** Every *structural* claim reproduces: root-level flex, the three declarations verbatim,
the 820px header/caption swap, no horizontal overflow at any width, and cells that go from side-by-
side slivers to full-width stacked blocks whose height collapses to ~81px. What does not reproduce
is the **pixel arithmetic**, and the cause is legible: MRB-210's numbers were taken by shrinking a
*container* (which Design's own note calls the correct method for container-driven wrapping) rather
than by overriding device metrics, and the container it shrank was not `.ks3-lesson`. The
container-sweep column above shows exactly which container width produces each quoted figure.

**Nothing here contradicts the fix or the ruling.** But **layer-C assertions must not be written from
MRB-210's numbers** — they would fail on the delivered page. §3.4.5 gives the assertions to write
instead.

#### 3.4.4 The KEY FACT box — inside the block, and on `--ks3-card`

Lines 240–243, the last child of `#s-compare`. Measured at 1280:

| Property | Measured | Token |
|---|---|---|
| background | `rgb(255,252,245)` | **`--ks3-card`** ⚑ drift 5's outlier |
| border | `2px solid rgb(34,30,27)` | `--ks3-ink` |
| radius | 20px | `--ks3-r-panel` |
| shadow | `rgb(228,87,46) 5px 5px 0` | `--ks3-accent` |
| padding | `18px 22px` | new |
| margin | `24px 0 0` | new |
| height | **127.17** (216.23 at 390) | — |
| eyebrow | MONO 13px / 500 / 1.17px (`.09em`) / uppercase / `--ks3-accent-text` | tokens |
| body | Bricolage **22px** / 29.7px (1.35) / **700** / −0.33px (`-.015em`) / `--ks3-ink` | tokens |

**Drift 5 confirmed: b1-06 is the outlier, and I can now say why.** Every other page puts the KEY
FACT box at top level on the page's `--ks3-ground`, where `--ks3-band` gives it a lift. This page
puts it **inside a `--ks3-band` section**, where `--ks3-band` would make it invisible — band on band.
`--ks3-card` is the only light ground that separates from `--ks3-band` at all.

So the outlier is **not** hand-authoring drift; it is a consequence of a different placement.

⚖️ **This does not overturn drift 5's ruling and should not.** `var(--ks3-band)` is right for the box
as a top-level component, 5 : 1, and the generator needs one value for that. But it means the
generator must be able to emit the box **on a non-default ground when it is nested in a band block**,
or the CONTRAST family loses its key fact into its own background. Recorded as **F34** and as a
schema consequence in §5 (G12). **Correction offered to `00-delivery-drift.md`, not taken here** —
that file is another agent's, and this is a reason, not a re-ruling.

⚑ **F19 restated.** Across five pages the KEY FACT box has taken **four** positions: top-level orphan
(b1-01, b1-04, b1-05 — 3), inside `#s-think` (b1-03), inside `#s-compare` (b1-06). It is not a
position the generator can guess; it is authored. `key_fact` needs a placement field, not just a
string.

#### 3.4.5 The layer-C assertions the coverage manifest needs, concretely

Both states must register. These are written from what the delivered page actually measures, at
viewports the harness can set, and every one was verified above:

```python
# ── C: comparison table, WIDE (assert at 1280 and 1340) ──────────────────
("compare-row-is-flex-wrap",        '[data-compare-grid]', 'display',   'flex'),
("compare-row-wraps",               '[data-compare-grid]', 'flex-wrap', 'wrap'),
("compare-row-gap",                 '[data-compare-grid]', 'gap',       '10px 14px'),
("compare-label-fixed-118",         '[data-compare-grid] > [data-compare-label]', 'flex', '0 0 118px'),
("compare-cell-basis-250",          '[data-compare-grid] > [data-compare-cell]',  'flex', '1 1 250px'),
("compare-cell-min-width-zero",     '[data-compare-grid] > [data-compare-cell]',  'min-width', '0px'),
("compare-head-visible-wide",       '[data-compare-head]',  'display',  'flex'),
("compare-cap-hidden-wide",         '[data-compare-cap]',   'display',  'none'),
# geometry: assert the RELATION, never the pixel — the pixel is a function of page width
("compare-cells-equal-width",       lambda: cell0.width == cell1.width),
("compare-cells-side-by-side",      lambda: cell0.top == cell1.top),
("compare-no-h-overflow",           lambda: section.scrollWidth == section.clientWidth),

# ── C: comparison table, NARROW (assert at 820 and 390) ──────────────────
("compare-label-full-width",        '[data-compare-grid] > [data-compare-label]', 'flex', '1 1 100%'),
("compare-head-hidden-narrow",      '[data-compare-head]',  'display',  'none'),
("compare-cap-visible-narrow",      '[data-compare-cap]',   'display',  'block'),
("compare-cap-is-mono-12",          '[data-compare-cap]',   'font-family', VAR('--ks3-font-mono')),
("compare-cap-is-accent-text",      '[data-compare-cap]',   'color',    '#A93411'),
("compare-cap-tracking",            '[data-compare-cap]',   'letter-spacing', '0.84px'),
("compare-cells-stacked",           lambda: cell0.top < cell1.top),
("compare-cells-full-width",        lambda: cell0.width == row.clientWidth - 28),
("compare-no-h-overflow-narrow",    lambda: section.scrollWidth == section.clientWidth),
("compare-every-cell-captioned",    lambda: all(cell.querySelector('[data-compare-cap]') for cell in cells)),

# ── C: the threshold itself (bisect, do not assume) ─────────────────────
("compare-head-visible-at-821",     viewport(821), '[data-compare-head]', 'display', 'flex'),
("compare-head-hidden-at-820",      viewport(820), '[data-compare-head]', 'display', 'none'),
```

Two rules behind that list, both learned from §3.4.3:

1. **Assert declarations and relations, never absolute pixel widths.** `118px` is authored and may be
   asserted; `356` and `258` are derived from page width and will change with any container the
   component is dropped into.
2. **The threshold must be bisected, not assumed.** One assertion at 820 proves nothing about where
   the query fires; a 821/820 pair proves it exactly.

### 3.5 ⭐⭐ `#s-settle` — "Does that settle it?", the CONTRAST flagship

`.ks3-block` (plain), measured 960 × **1097.03** at 1280 resting, **1545.30** with one case revealed.
`--ks3-card`, `2px --ks3-ink`, r28, `5px 5px 0 #221E1B`, padding 30px. `h2` 30px.

This activity exists nowhere in the generator, and **18 CONTRAST slots plus the CLASSIFY-adjacent
work inherit it**. Specified exhaustively below.

#### 3.5.1 The teaching claim, in the page's own words

Line 249, the instruction, verbatim:

> Every fact below each cell is true. Most of them settle nothing, because they are true of
> single-celled organisms *and* of cells inside a body. Mark only the ones that decide it.

That sentence is the activity's specification. Three consequences the data honours exactly:

- **Every fact is true.** There are no false statements to eliminate. The judgement is
  *discrimination*, not truth-testing — which is why the activity cannot be modelled as a quiz.
- **Most settle nothing.** Measured across the data: **16 features, 6 discriminators, 10 non-
  discriminators.** Marking everything "settles it" is wrong 10 times out of 16; marking everything
  "settles nothing" is wrong 6 times.
- **The discriminating fact is never the most interesting one.** Confirmed on all four cases —
  §3.5.2.

#### 3.5.2 The data shape — `CASES`, lines 499–552

```python
{
  "id": "c1",                       # stable; keys `marks` and `caseOpen`
  "label": "Mystery cell 1",        # panel heading; tab label is label.replace("Mystery cell ", "Cell ")
  "desc":  "About 0.05 mm long. It is green, and it swims using one long whip at the front.",
  "features": [                     # exactly 4 on every case
    {"text": "It can swim.", "settles": False,
     "why": "A sperm cell swims. So does a white blood cell, through tissue. …"},
    …
  ],
  "verdictLabel": "It is an organism",              # MONO eyebrow on the reveal
  "answer":       "Euglena — a single-celled organism.",   # 27px display line
  "why":          "Green, so it makes its own food; a flagellum, so it can go and find light. …"
}
```

The four cases, with the discriminator count and the trap each carries:

| Case | Cell | Facts that settle it | Facts that settle nothing | The trap |
|---|---|---|---|---|
| c1 | **Euglena** | 1 of 4 — *"It is green, and makes its own food from light."* | swims · has mitochondria · is only 0.05 mm long | Swimming is listed first and is the vivid one. Size is planted as a decoy and refuted in its own `why`: *"Your cheek cell is 0.06 mm and a Paramecium is 0.25 mm — the bigger one is the organism here, and that is a coincidence."* |
| c2 | **Sperm cell** | **2 of 4** — *"It never feeds."* and *"It carries half a set of chromosomes."* | has a tail and swims · is packed with mitochondria | ⭐ **The pattern-breaker.** Its own `why` says so: *"Two facts settled it, and neither was the swimming. Some cases have more than one discriminator; the skill is spotting which facts qualify, not counting them."* This is what stops the activity degrading into "find the one". |
| c3 | **Bacterium** | **2 of 4** — *"It divides on its own, over and over."* and *"Its DNA sits in a loose loop in the cytoplasm."* | has no nucleus · is very small (0.002 mm) | The absent nucleus is the headline fact and settles nothing, because a red blood cell has none either. §4.5. |
| c4 | **Amoeba** | **2 of 4** — *"Nothing else feeds it and nothing else positions it."* and *"It has a vacuole that keeps filling with water and squeezing it out."* | changes shape as it moves · flows around another cell and engulfs it | ⭐ **The hardest, and the one the task named.** Both vivid facts settle nothing because a white blood cell does both — the `why` on the engulfing fact says *"This is the hardest one… Behaviour is not evidence."* The verdict line says it outright: *"The two most vivid facts — shape-changing and engulfing — are the two that settle nothing… The quiet facts did the work."* |

**Distribution: 1 / 2 / 2 / 2 discriminators.** A student who learns "there is one" from case 1 is
corrected on case 2 by the reveal itself, in a sentence written for that purpose.

#### 3.5.3 Every control, every state — measured

**(a) The four case tabs** — `flex; gap 9px; wrap`, `seg(on, false)` (the light branch, drift 4's
ruled value):

| State | Measured |
|---|---|
| on | `--ks3-accent-tint` #FCE7DE ground, `2px --ks3-accent` #E4572E, `--ks3-ink` text, `aria-pressed="true"` |
| off | `--ks3-ground` #FBF3E6 ground, `2px --ks3-option-border` #DDCFB6, `--ks3-ink` text |
| both | 17px / 700 / `padding 11px 17px` / `min-height 44px` / `--ks3-r-control` 14px; measured 79.44–83.47 × 53.19 |

Labels are derived: `k.label.replace('Mystery cell ', 'Cell ')` → `Cell 1` … `Cell 4`. **The tabs
carry no completion state at all** — a revealed case looks identical to an untouched one.
Finding **F35**, §3.5.7.

**(b) The case panel** — `--ks3-inset` #F7EFE1, `2px --ks3-ink`, `--ks3-r-panel` 20px, `padding 22px
24px`. Label MONO 14px `.07em` uppercase `--ks3-ink-muted` (*"Mystery cell 1"*); description
**21px / 30.45px / 700** `--ks3-ink`.

**(c) The four feature rows** — a `flex-direction: column; gap: 11px` list. Each row is `padding 18px
20px`, `--ks3-r-panel` 20px, and takes one of **three grounds**:

| Row state | ground | border | when |
|---|---|---|---|
| unrevealed | `--ks3-card` #FFFCF5 | `2px --ks3-rule-strong` #C3B191 | before the reveal, regardless of marking |
| revealed, **settles it** | `--ks3-band` #F4E9D8 | `2px --ks3-ink` #221E1B | after the reveal |
| revealed, **settles nothing** | `--ks3-row-dim` #FBF6EC | `2px --ks3-rule` #E0D2B9 | after the reveal |

⭐ **The row ground carries the truth, not the student's mark.** Verified by driving the same case
twice — once marking every row "Settles it", once marking c4 correctly. The row grounds were
byte-identical in both runs. **R3 is respected: nothing on this page marks the student's answer
right or wrong.**

Row height 130.09 unrevealed → 197.88 revealed (the `why` paragraph is 4 lines at 960).

**(d) The two choice buttons per row**, `flex; gap 9px; wrap`, built inline at 1051–1054 rather than
by `seg()`:

| State | Measured |
|---|---|
| resting | `--ks3-ground` on `2px --ks3-option-border`, `--ks3-ink`, `opacity 1`, `cursor pointer` |
| picked | **`--ks3-accent-tint` on `2px --ks3-accent`**, `--ks3-ink`, `opacity 1`, `aria-pressed="true"` |
| after reveal, picked | unchanged — accent tint, accent border, `opacity 1`, `cursor default`, `disabled` |
| after reveal, not picked | `--ks3-ground` on `--ks3-option-border`, **`opacity: .5`**, `cursor default`, `disabled` |
| geometry, all states | 16px / 700 / `padding 10px 16px` / `min-height 44px` / `--ks3-r-control` 14px |

⚑ **This is a fifth `seg`-like control that is not `seg()`.** It is 16px/`10px 16px` where the
segmented control is 17px/`11px 17px`, and it uses `--ks3-r-control` like the segment. Drift 4
resolved four variants; this is a fifth, deliberately smaller because two of them sit inside a row.
**It needs its own registry entry** — `settle-choice` — exactly as drift 4 concluded for b1-04's
option row. §8(c).

Labels: `Settles it` and `Settles nothing`, from a hard-coded 2-element list (1045–1046). They are
**not** per-case data — the same two words on all 16 rows.

**(e) The reveal button** — `button.ks3-reveal-btn`, label *"Show what settles it"*. Measured
`--ks3-ink` ground, `--ks3-on-dark` text, `2px --ks3-ink`, r14, `padding 14px 22px`, 17px/700,
`min-height 44px`.

| State | `disabled` | `opacity` | `cursor` | when |
|---|---|---|---|---|
| locked | `true` | **0.45** | `default` | `markedCount < 4` |
| live | `false` | 1 | `pointer` | all 4 marked, not yet revealed |
| spent | `true` | **0.45** | `default` | after the reveal |

**(f) The progress counter** — MONO 15px `--ks3-ink-muted` beside the button. Reads
`"N of 4 marked"` while marking and **`"Opened"`** afterwards.

**(g) The reveal panel** — `[data-arrive="1"]`, `margin-top 20px`, `padding 24px`, `--ks3-r-panel`
20px, **`--ks3-ink` ground with `--ks3-on-dark` text** — the only ink-dark panel that is not a whole
block. Three parts:

| Part | Measured |
|---|---|
| `caseVerdictLabel` | MONO 14px / 500 / 1.12px (`.08em`) / uppercase / **`--ks3-alert`** #FFC53D |
| `caseAnswer` | Bricolage **27px** / 31.86px (1.18) / 800 / −0.675px / `--ks3-on-dark` |
| `caseWhy` | 19px / 30.4px / `--ks3-on-dark-body` #E7DECE |

Panel height 185.03 for c4.

**(h) The per-feature `why` line**, revealed with the panel: `margin 12px 0 0`, **18px / 27.9px**,
opening with a display-font `<strong>` reading exactly `Settles it.` or `Settles nothing.`

#### 3.5.4 Driven in the browser — what actually happens

Every row below was driven from a clean load at 1280, with a ≥850 ms settle (see §4.4).

| Action | Result |
|---|---|
| **Reveal early, nothing marked** | Button is `disabled`; the click is a no-op. `caseOpen` stays false, counter stays `"0 of 4 marked"`. **Belt and braces**: `onSettle` (1071–1075) re-checks the mark count inside the state updater and returns `null` if short, so even a programmatic click cannot open it. |
| **Mark one** | Counter `"1 of 4 marked"`; button still `disabled`, `opacity 0.45`. Picked button → accent tint + accent border, `aria-pressed="true"`. |
| **Change your mind** | Clicking the other choice on the same row moves the mark; counter **stays at 1**. `marks[caseId][i]` is a single value, so a row is marked-or-not, never both. |
| **Mark all four** | Counter `"4 of 4 marked"`; button `disabled: false`, `opacity 1`, `cursor pointer`. |
| **Mark everything "Settles it"** | Allowed. The reveal opens normally, all four rows show their `why`, and **three of the four rows show `--ks3-row-dim` with a `Settles nothing.` opener directly under a mark the student gave as "Settles it"**. Nothing says "you got 3 wrong". |
| **Reveal** | `caseOpen[id] = true`. All 4 rows re-ground by truth, all 8 choice buttons `disabled`, the 4 unpicked ones drop to `opacity .5`, the 4 `why` lines arrive, the ink panel arrives, the counter changes to `"Opened"`, the button greys to 0.45. |
| **Click a choice after the reveal** | No-op, twice over: the buttons are `disabled: true`, **and** the `onClick` updater's first line is `if (st.caseOpen[kase.id]) return null;`. Verified — marks did not move. |
| **Switch to another case** | Fully independent. Case 2 opened at `"0 of 4 marked"`, all 8 buttons `aria-pressed="false"`, no reveal. |
| **Switch back to a revealed case** | State persists: reveal still open, counter `"Opened"`. |
| **Rail** | SETTLE ticks only when all four cases have been revealed. |

**Marking correctly changes exactly one thing, and it is invisible.** `agreed = revealed && ((pick
=== 'yes') === f.settles)` (line 1038) feeds only `whyStyle`'s colour (1065):

| | agreed | disagreed |
|---|---|---|
| `why` text colour | `--ks3-ink` **#221E1B** | `--ks3-ink-body` **#3B342E** |

Measured on both runs. **That is the whole difference** — two near-identical dark greys, ΔL* of
roughly 6, on 18px body text. It is not perceptible, and it is certainly not a mark.

⚑ **FINDING F36 — `agreed` is computed and then effectively discarded.** Two readings, and they lead
opposite ways, which is why this is flagged and not resolved:

- **It is R3 done properly.** R3 says only the mastery ladder may mark correctness. Computing
  agreement and then rendering it at a strength below perception is *technically* a mark that cannot
  be read, which is arguably the most conservative possible reading of R3 — the intent is legible in
  the code and nothing on screen judges the student.
- **Or it is a bug.** Two greys 6 ΔL* apart is what a half-finished styling decision looks like. If
  Design meant the student's agreement to register at all, this does not do it; if Design meant it
  not to register, the `agreed` computation should not exist.

**Design's call (§8(a)), not Code's**, and the generator must be told which — because "emit
`--ks3-ink` vs `--ks3-ink-body` on a paragraph" is a data-driven decision the renderer cannot infer.

#### 3.5.5 ⭐ Why this activity is not a `check`, a `quiz` or a `misconception`

It matters, because the temptation to map it onto an existing block type is strong and every mapping
loses the lesson.

| Existing type | Why it fails |
|---|---|
| `check` | A check is one question, one commit, one reveal. This is **four independent judgements per case, gated collectively**, and the student must make all four before seeing any. |
| `quiz` | A quiz marks. This does not mark, cannot mark, and must not mark (R3). Its answers are not right/wrong, they are settles/doesn't-settle — a different predicate. |
| `misconception` | A misconception block confronts one stated belief. This confronts **a habit of reasoning** — reaching for the vivid fact — and it does so by making the student commit ten times to facts that go nowhere. |
| `practical` | No apparatus, no method, no observation. |

**It is a new block type.** §7.3 specifies it.

#### 3.5.6 What the generator needs to emit it

```python
{"type": "settles-it",                       # NEW block type — §5 gap G7
 "id": "s-settle",
 "eyebrow": "Your turn · four mystery cells",
 "heading": "Does that settle it?",
 "instruction": "Every fact below each cell is true. Most of them settle nothing, …",
 "choice_labels": ["Settles it", "Settles nothing"],   # authored; the same on every row
 "reveal_label": "Show what settles it",
 "progress_format": "{n} of {total} marked",           # and "Opened" once revealed
 "cases": [
   {"id": "c1",
    "label": "Mystery cell 1",
    "tab_label": "Cell 1",                   # ⚑ authored, NOT derived — see below
    "description": "About 0.05 mm long. It is green, and it swims using one long whip at the front.",
    "features": [                            # exactly 4; the renderer must not accept 3 or 5
      {"text": "It can swim.", "settles": False,
       "why": "A sperm cell swims. So does a white blood cell, through tissue. …"},
      …
    ],
    "verdict_label": "It is an organism",
    "answer": "Euglena — a single-celled organism.",
    "why": "Green, so it makes its own food; a flagellum, so it can go and find light. …"},
   …                                          # exactly 4 cases
 ]}
```

Six things the generator must get right, each of which the page fixes:

1. **`tab_label` is authored, not derived.** Design derives it with
   `label.replace('Mystery cell ', 'Cell ')` — a string surgery that only works because every label
   begins with that exact phrase. A generator that reproduces the `.replace` will silently emit
   `"Mystery cell 1"` as a tab the moment a lesson names its cases anything else. **Emit two fields.**
2. **`settles` is a boolean per feature, and the count per case is free.** The renderer must never
   assume one discriminator. c2, c3 and c4 all have two; the family's teaching point (c2's `why`)
   depends on the count varying.
3. **The reveal is gated on *all* features marked, not on a threshold.** `markedCount <
   kase.features.length`. The guard is enforced twice — the `disabled` attribute and a re-check
   inside the state updater — and both must be emitted, because `disabled` alone is bypassable.
4. **Marks are per-case and never cleared.** `marks[caseId][featureIndex]`, `caseOpen[caseId]`. There
   is no retry and no reset on this block.
5. **Nothing may mark correctness.** The row ground is a function of `settles` only; the choice
   buttons carry only "you picked this". R3.
6. **The `why` strings open with a fixed word**, `f.settles ? 'Settles it.' : 'Settles nothing.'`,
   rendered as a display-font `<strong>` and **not** part of the authored `why`. The authored string
   begins after it. Getting this wrong duplicates the phrase.

#### 3.5.7 ⚑ Two smaller findings on this block

**F35 — the case tabs carry no completion state.** Four cases must all be revealed for the rail to
tick, and the tabs are the only navigation between them, but a revealed tab and an untouched tab are
pixel-identical. Measured on all four. A student who has done c1 and c3 has nothing to tell them c2
and c4 remain. The rail's SETTLE chip is the only feedback, and under 1340px the rail is the top bar,
which shows scroll (F2). **Design's, §8(a)** — adding a tick to a tab is a visual decision, and it
sits close enough to "marking" that Code should not invent it.

**F37 — the reveal is the only place the cell is named.** `caseAnswer` (*"Euglena — a single-celled
organism."*) is the first time the organism is named; the panel calls it "Mystery cell 1" throughout.
That is deliberate and good. It is recorded because a generator that renders `label` as a heading
*and* `answer` as an accessible name would spoil the activity — **`answer` must not leak into
`aria-label`, `title`, or the tab.**

### 3.6 `#s-think` — one misconception block, two misconceptions

`.ks3-block ks3-misconception`: `--ks3-alert-tint` #FFF3D4 ground, `2px --ks3-ink`, r28, `5px 5px 0
#221E1B`, padding 30px, measured 960 × 577.09.

- `.ks3-mis-head` with `.ks3-mis-badge` — 32×32, r10, `--ks3-ink` ground, **`--ks3-alert` glyph**,
  19px — and `p.ks3-eyebrow` "Think again".
- `.ks3-mis-quote` ×2 — 19px / 30.4px / **700** `--ks3-ink`, body font, curly quotes authored in the
  string.
- The splitter: `margin-top 22px; padding-top 20px; border-top: 2px solid var(--ks3-alert-border)`
  #D9821A. Same construction as b1-05's two-misconception block.
- **Both are open. `document.querySelectorAll('#s-think [data-reveal]').length === 0`.** No gating,
  no flip.

Misconception 1 is the paired-contract half — §4.5. Misconception 2 (*"One cell means simple."*) is
the one the register knows: `CELL-08`, `confronted_by: more-not-fewer`, owner `unicellular-organisms`
(`docs/ks3/misconception-register.md:179`).

### 3.7 The ladder, the stretch layer and the endmatter

**Ladder** — `class="ks3-ladder"` alone (D5, fifth confirmation): `--ks3-card`, `3px --ks3-ink`, r30,
`6px 6px 0 #12A150`, padding 32px, 960 × 1961.59. `h2` **36px / 57.6px (1.6)**; `.ks3-rung h3`
**23px / 36.8px (1.6)** — F17 and F14 both reproduce. Sub-line *"Four rungs. Two the page marks, two
you mark."* Score `"You got N of 4."` + `"You marked rungs 3 and 4 yourself."`

Driven at 1340 with a 2.2 s settle, all six option states measured and **all six are the registered
component**:

| State | ground | border | badge | drawn mark |
|---|---|---|---|---|
| `is-correct` | `--ks3-ok-tint` #E4F7EB | `--ks3-ok` #12A150 | `--ks3-ok` ground, `#FFFFFF` glyph | ✔ tick path |
| `is-wrong` | `--ks3-band` #F4E9D8 | `--ks3-ink` #221E1B | `--ks3-ink` ground, `--ks3-on-dark` glyph | ✔ cross path |
| `is-spent` | `--ks3-row-dim` #FBF6EC | `--ks3-option-spent` #EBDFCB | `--ks3-band` ground, `--ks3-ink-ghost` glyph | — letter |
| feedback correct | `--ks3-ok-tint` | `--ks3-ok` | — | ✔ |
| feedback wrong | `--ks3-band` | `--ks3-ink` | — | ✔ |
| resting | `--ks3-ground` | `--ks3-option-border` | `--ks3-band` | letter |

Ladder option geometry: r **15px**, `padding 15px 17px`, `min-height 44px`, 18px; `.ks3-options` is
`grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap 11px`. **MRB-202's chosen-wrong
`--ks3-band` ground is present and correct on Design's own page**, so the reference and the fixed
build agree.

Self-rungs: 5 criteria on r3, 4 on r4 — **the count varies per rung and is authored.** Tally reads
`"N of M ticked — not yet."` → `"All M ticked — rung met."` with `class="ks3-tally is-met"`. Score
reached `"You got 3 of 4."` with r1 right, r2 wrong, both self-rungs fully ticked.

**Retry** clears `answers`, `checked` and `ticks` but **not** `text` — matching its own note,
*"Clears the ticks on rungs 3 and 4 and keeps what you wrote."* Verified: the `.ks3-ticks` lists
disappear (`length 0`), the r1 options return to a bare `ks3-option` class and re-enable, the score
returns to 0, and the textarea retains its value. See F32 for the rail consequence.

**Stretch layer** — `.ks3-layer` → `.ks3-layer-body` `--ks3-stretch-tint` #F0EAFC on `2px
--ks3-stretch` #6B3FD4, r26, `padding 26px 28px`, holding **one bare `<p>`** (Euglena and the
kingdoms). Same shape as b1-05.

**Endmatter** — 4 cards, `grid` `309.328 / 309.328 / 309.344`, gap 16px; heads
`["Before this lesson", "Connects to", "At GCSE this becomes", "Ask Mr Badmus AI"]`. The third is
**prose**, not links. `.ks3-tutor` is `--ks3-accent` on `2px --ks3-ink`, r22, padding 22px.

---

## 4. Interactive behaviours

Eleven, all driven in the browser.

| # | Trigger | Effect | State key |
|---|---|---|---|
| 1 | Click a hook option | `aria-pressed`; border + badge → `--ks3-alert`; the static reveal appears; HOOK ticks | `hookChoice` |
| 2 | Click a gate option | The commit **disappears** and the whole bench appears | `gate` |
| 3 | Click a mount tab | Swaps specimen, redraws, drops the centre group on cheek, swaps `mountNote` / `scopeCaption` / `scopeAlt`; banks `<mount>:400` if the objective is ×40 | `mount`, `seenScope` |
| 4 | Click an objective tab | Changes `total` / `fov` / `dof`; redraws; swaps `resolveNote`; banks `<mount>:400` at ×40 | `obj`, `seenScope` |
| 5 | Click a centre tab (pond only) | Pans the field by translating every organism's position | `centre` |
| 6 | Click the movement toggle | Freezes / resumes the rAF loop and every `t`-dependent detail | `motion` |
| 7 | Drag the focus wheel | Redraws blur per organism; re-computes `inFocus` and `focusLabel` | `focus` |
| 8 | Click a case tab | Swaps the whole activity to that case's marks and reveal state | `caseId` |
| 9 | Click a feature choice | Sets that row's mark; no-op after the reveal | `marks` |
| 10 | Click "Show what settles it" | Grounds all 4 rows by truth, disables all 8 buttons, opens the `why` lines and the ink panel | `caseOpen` |
| 11 | Ladder: option / check / retry | The registered R2–R8 behaviours | `answers`, `text`, `checked`, `ticks` |

### 4.1 Gating style — by absence, three times

Every gate on this page **removes** the thing it hides rather than veiling it:

| Gate | Mechanism |
|---|---|
| Hook reveal | `<sc-if value="{{ hookRevealed }}">` — not in the DOM until `hookChoice !== null` |
| Scope bench | `gateOpen: s.gate === null` / `scopeOpen: s.gate !== null` — complementary, so the commit leaves as the bench arrives |
| Settle reveal | `<sc-if value="{{ caseOpen }}">` |
| Ladder criteria | `<sc-if value="{{ rung.checked }}">` |

**Fourth page in a row.** b1-04, b1-05 and b1-06 all gate by absence; §8(c) should now record it as
ruled by repetition, not left open.

### 4.2 Reduced motion

`@media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } }` (line 33),
plus `this.reduced` (line 649) consumed by `moving()` (660), which kills the rAF loop and every
`t`-dependent detail. **Not measured under an actual reduced-motion emulation** — `ks3_browser.py`
has no CDP hook for `Emulation.setEmulatedMedia` in its current API, and adding one was out of scope
for a read-only inventory. Recorded in §6.3.

### 4.3 The `record()` closure — a correctness note

`record(mount, obj)` is defined inside `renderVals` (928–933) and invoked from the tab handlers
*after* `setState`. It reads the other axis from `this.state`, which is safe **only because each
handler changes one axis and reads the other**. Driven every path: ×40 then swap mount, swap mount
then ×40, and both in the reverse order — `seenScope` reached `2 of 2` on every one. No defect
found; recorded because a generator that re-orders those two statements would introduce one.

### 4.4 ⚑ The settle trap, third and worst instance

b1-02 recorded that 450 ms is not enough; b1-03 added `animation: … both`. **This page needs more
than 900 ms.** A ladder-option read taken 900 ms after the click returned
`background: rgb(251,243,230)` (`--ks3-ground`) and `border-color: rgb(221,207,182)` on an element
whose class was already `ks3-option is-correct` — i.e. the class had landed and the paint had not.
The same read at **2.0 s** returned `--ks3-ok-tint` on `--ks3-ok`, correctly. The cause is
`animation: ks3-pop .35s both` on `.ks3-option.is-correct` layered on top of the DC runtime's async
re-render.

**That produced a false finding in this run** — "Design's reference page renders ladder states with
no ground" — which survived one probe and was killed by the second. It is recorded here because the
class of error matters: **on this page, read the class name and the computed style in the same probe
and disbelieve any disagreement between them.** A build-run probe must settle ≥ 2 s after any click
that changes an option's state, or assert on `className` and re-read style separately.

### 4.5 ⭐ The B1-04 / B1-06 paired contract (CELL-08) — this page's half

b1-04 §4.4 quotes its half verbatim: the `<h2>` at its line 84, *"Last lesson: no nucleus, no
instructions, no repair, no dividing."*, ratified by line 85's *"All still true."*

**This page's half, `#s-think`'s first misconception, verbatim with its line numbers.**

**Line 297** — the belief being confronted:

```html
<p class="ks3-mis-quote">“No nucleus means no instructions — so a bacterium cannot divide.”</p>
```

**Line 298** — the resolution, and the sentence the contract actually depends on:

```html
<p>Two lessons ago that was exactly right, about a red blood cell. It is wrong here, and the difference is worth being precise about. A red blood cell <em>had</em> a nucleus and destroyed it, and the DNA went with it. A bacterium never had one: its DNA is there, in a loose loop in the cytoplasm, with no membrane around it. Instructions present, container absent. That is why a bacterium can divide every twenty minutes and a red blood cell can never divide again.</p>
```

**Precisely which sentences the contract depends on.** Four, and no others:

1. **Line 297's quote** — it *states* B1-04's rule as a student would over-generalise it. Remove it
   and the contradiction is never named.
2. **Line 298, sentence 1**: *"Two lessons ago that was exactly right, about a red blood cell."* This
   is the explicit back-reference. It is the only string in the whole delivery that points at B1-04
   by position, and **it will be wrong if the unit is ever re-ordered** — "two lessons ago" is
   B1-04 only while B1-05 sits between them. Finding **F38**.
3. **Line 298, sentences 3–4**: *"A red blood cell **had** a nucleus and destroyed it, and the DNA
   went with it. A bacterium never had one: its DNA is there, in a loose loop in the cytoplasm, with
   no membrane around it."* This is the resolution — **never had one / destroyed its own**. It is
   what makes both lessons true at once, and the `<em>` on *had* is load-bearing typography, not
   decoration.
4. **Line 298, final sentence**: *"That is why a bacterium can divide every twenty minutes and a red
   blood cell can never divide again."* This is what discharges B1-04's fourth clause (*no
   dividing*) explicitly. Without it the resolution is about DNA and leaves the dividing claim
   dangling.

**Three more places on this page restate the pair, and all three must move with it:**

| Where | Line | String |
|---|---|---|
| `CASES` c3, feature 1 `why` | 530 | *"A red blood cell has no nucleus either, and that is a part of you. Missing a nucleus settles nothing on its own."* |
| `CASES` c3, feature 2 `why` | 531 | *"A red blood cell can never divide again. A cell that makes more of itself unaided is reproducing…"* |
| `RUNGS` r2 | 564–569 | The whole rung: the question *"A red blood cell has no nucleus and can never divide. A bacterium has no nucleus and divides every twenty minutes. What explains the difference?"*, the correct option *"The bacterium still has its DNA, loose in the cytoplasm; the red blood cell lost its DNA with its nucleus"*, and the distractor correction *"That is the red blood cell. The bacterium never had a nucleus at any point."* |

So the contract's fingerprint on this side is **five strings across three blocks**, not one.

**Why the register cannot express it.** MRB-209 §3 and b1-04 §4.4 establish this and it is confirmed
here: `docs/ks3/misconception-register.md` keys on `{id, statement, elicited_by, confronted_by,
owner}`. `CELL-08` (line 179) is *"A single-celled organism is just a simpler version of one of our
cells — the same parts, doing less"* — which is `#s-think`'s **second** misconception, not the first.
**The register does not know the bacterium/red-blood-cell pair exists at all.** There is no id for
it, no owner, and no field that could say "lesson A asserts a rule that lesson B qualifies."

⚑ **That is worse than b1-04 recorded.** b1-04 said the register has no field for a cross-lesson
claim/qualification pair. Measured here: the pair is not merely unexpressible, **it is unregistered** —
`#s-think`'s first misconception has no register entry of any kind, while its second does. So a
build-time check over the register would report this block as fully accounted for.

**Until that field exists, the quoted strings above are the only fingerprint.** If b1-04's line 84
changes, lines 297, 298, 530, 531 and 564–569 must be re-read against it, and vice versa. Whether
the pair is safe to ship split is **Mide's** (§8(b)).

---

## 5. Schema gaps against `docs/ks3/architecture.md` §4.8

§4.8 is authoritative: *"Fields not listed here do not exist without an amendment to this document."*

### 5.1 Already covered by §4.8

`slug`, `title`, `discipline`, `unit`, `family`, `covers`, `touches`, `threads`, `typical_year`,
`typical_minutes`, `requires`, `assumes`, `references`, `ks4_links`, `big_question`, `phenomenon`,
`misconceptions`, `vocabulary`, `figures`, `core`, `stretch`, `support`, `activities`, `ladder`,
`key_note`, `ws`, `review_state`.

The ladder maps cleanly: `RUNGS` → two page-marked rungs with per-option `correction`; `SELF_RUNGS`
→ two self-marked rungs with `fieldLabel` / `placeholder` / a **variable-length** criteria list.

### 5.2 Gaps — 13, of which 6 are new to this page

| # | Gap | Needed by | New here? |
|---|---|---|---|
| G1 | **`rail`** — `[{anchor, short, label, done_when, threshold?, states?}]` | §2 | no (b1-01) |
| G2 | **`tutor_anchor`** — the in-page href on the tutor CTA | §3.1 | no (b1-01); **sixth authored instance** |
| G3 | **`legal`** — the block-level line, and its *kind* (safety vs copyright vs absent) | §1.4 | no (b1-01); this page is the second safety line |
| G4 | **`key_fact`** — the box's string | §3.4.4 | no (b1-01) |
| G5 | **`key_fact_placement`** — top-level / inside-block / inside-which-block | §3.4.4 | **⊕ NEW** — four positions across five pages |
| G6 | **`key_fact_ground`** — the box needs a non-default ground when nested in a band block | §3.4.4 | **⊕ NEW** |
| G7 | **`settles-it` block type** — the whole payload in §3.5.6 | §3.5 | **⊕ NEW** |
| G8 | **`comparison` block type** — `{statement, columns: [{caption}], rows: [{name, cells}], key_fact}` | §3.4 | **⊕ NEW** |
| G9 | **sim `mounts`** — more than one specimen on one instrument, with per-mount notes, captions and alt text | §3.3.2 | **⊕ NEW** |
| G10 | **sim `centres`** — `[{id, label, x, y}]` + `centre_offered_on` | §3.3.3 | **⊕ NEW** |
| G11 | **sim `motion_toggle` / `motion_default`** + the two authored labels | §3.3.3 | **⊕ NEW** |
| G12 | **`misconceptions[].pairs_with`** — a cross-lesson claim/qualification edge | §4.5 | no (b1-04 raised it); **strengthened: the pair is unregistered, not merely unexpressible** |
| G13 | **block-level `id`** — every section needs a stable anchor id, independent of the rail | §2.3 | no (b1-05) |

Note that `showDraft`, `railLabels`, `startMount` and `motionDefault` are **DC props**, not lesson
data — they are the design-tool's preview controls (line 426). `startMount` and `motionDefault`
nonetheless imply G9 and G11: Design gave itself a switch for each, which is how a payload field
looks before it is one.

---

## 6. Measurements

### 6.1 Traces to a token

All 36 probed resolved on `.rd[data-mode="ks3"]`:

`--ks3-ground` #FBF3E6 · `--ks3-card` #FFFCF5 · `--ks3-band` #F4E9D8 · `--ks3-inset` #F7EFE1 ·
`--ks3-row-dim` #FBF6EC · `--ks3-ink` #221E1B · `--ks3-ink-body` #3B342E · `--ks3-ink-muted` #5F564F ·
`--ks3-ink-ghost` #9A8F86 · `--ks3-ink-faint` #6E655D · `--ks3-rule` #E0D2B9 · `--ks3-rule-strong`
#C3B191 · `--ks3-accent` #E4572E · `--ks3-accent-text` #A93411 · `--ks3-accent-tint` #FCE7DE ·
`--ks3-accent-hover` #7F2408 · `--ks3-alert` #FFC53D · `--ks3-alert-tint` #FFF3D4 ·
`--ks3-alert-border` #D9821A · `--ks3-on-dark` #FBF3E6 · `--ks3-on-dark-body` #E7DECE ·
`--ks3-on-dark-muted` #C6B9A7 · `--ks3-dark-panel` #3E3730 · `--ks3-option-border` #DDCFB6 ·
`--ks3-option-spent` #EBDFCB · `--ks3-stretch` #6B3FD4 · `--ks3-stretch-tint` #F0EAFC · `--ks3-ok`
#12A150 · `--ks3-ok-text` #0A6B36 · `--ks3-ok-tint` #E4F7EB · `--ks3-r-card` 22px · `--ks3-r-block`
28px · `--ks3-r-panel` 20px · `--ks3-r-control` 14px · `--ks3-r-option` 16px · `--ks3-page` 1320px ·
`--ks3-wide` 60rem · `--ks3-measure` 46rem · the three font stacks.

Every colour on this page resolves to one of those. **No hard-coded hex in any inline `style=`** —
checked by reading all 125 attributes; the only literal colours in the file are inside `draw()`, on
the canvas (`#100D0A`, `#E9EFE5`, `#EBE4D6`, `#4A4038`, and the organism palette `#6E6152`,
`#8A7BB0`, `#4B4070`, `#F2FAFB`, `#8FAAB8`, `#E0D2B4`, `#8A7A62`, `#7A6A50`, `#DCC9A6`, `#8A6A3C`,
`#CEE0BC`, `#3E6B2C`, `#4F7C3B`, `#C2372B`, `#EFE7D6`, `#A99C86`, `#7C6E5C`), which is a **drawing
palette and not a UI palette** — the same status b1-03 and b1-04 gave theirs.

### 6.2 New measurements — px values not expressed as a token

| Value | Where | Note |
|---|---|---|
| **118px** | comparison label column | MRB-210's, authored |
| **250px** | comparison cell flex-basis | MRB-210's, authored |
| **10px 14px** | comparison row gap | authored |
| **15px 14px** | comparison row padding | authored |
| **820px** | comparison narrow threshold | drift 2's ruled value, live here |
| **1340px** | rail swap | family-wide |
| **92px** | `scroll-margin-top` | family-wide |
| **104px / 150px / calc(50% − 632px)** | side rail | family-wide |
| **96px / 8px** | top-bar track | family-wide |
| **1800 × 1120** | canvas buffer | shared with b1-04's dark canvas |
| **900 × 560** | canvas design space | new |
| **0.45** | field-radius fraction of `min(W,H)` | new |
| **11 / 3** | bezel stroke widths | new |
| **160px** | readout panel `minmax` | new |
| **25px** | readout value MONO | new — and the only 25px in the delivery besides `.ks3-bigq` |
| **27px** | case answer display | new |
| **21px** | case description | new |
| **22px** | KEY FACT display / `.ks3-commit` | shared with b1-05 |
| **26ch / 54ch / 58ch** | prose measures | authored per block |
| **28 × 28 / −11px / 10px** | focus thumb, offset, track | new |
| **10px 16px / 16px** | settle choice button | ⚑ the fifth `seg`-like control |
| **11px 17px / 17px / 44px** | `seg()` both branches | drift 4's ruled value |
| **0.45 / 0.5** | disabled-button and unpicked-choice opacities | new |
| **3px** | `#s-compare` and `.ks3-ladder` border | shared |
| **34px 32px** | `#s-compare` padding | new |
| **18px 22px / 24px 0 0** | KEY FACT padding / margin | new |
| **18px 20px** | settle row padding | new |

**The 19–28px tier b1-05 §3.1.1 identified is here in force: 27 · 25 · 23 · 22 · 21**, five distinct
sizes between the 19px body and the 28px smallest heading, every one of them inside an instrument.
The generated pages have **nothing** in that band. This is the fifth page to confirm it.

### 6.3 Not measured

- **`prefers-reduced-motion: reduce`** was not emulated. The rule exists (line 33) and `moving()`
  consumes `matchMedia` (649, 660), both read from source. `ks3_browser.py` exposes no
  `Emulation.setEmulatedMedia` in its current API and adding one was out of scope.
- **The pre-fix comparison grid.** Not in the repo; MRB-210's before-numbers cannot be verified
  against the provenance anchor. §3.4.3.
- **Canvas pixel output.** No image diffing was done — the canvas was measured for buffer size, CSS
  box, device-pixel ratio and readout consequences only. The drawing routines (673–885) were read,
  not rendered-and-compared.
- **Print styles.** The `_ds` bundle carries a `print` block; not exercised.
- **Keyboard traversal and focus order.** Not driven. Every control is a real `<button>` or
  `<input>`, and the focus slider has a correctly associated visually-hidden `<label>`, but tab
  order, focus rings and `aria-pressed` announcement were not tested.
- **The 1340px side rail at 390 and 820.** Not applicable — it is `display: none` below 1340.
- **A built page for this lesson.** `mrbadmus_site/ks3/biology/cells-and-organisation/` has no
  `unicellular-organisms.html` from the current data in a state worth diffing; the generator
  comparison in §3.1 was made against the **record**, not a rendered page.

---

## 7. How to generate each new component from data

### 7.1 The progress rail

§2.4. Identical to b1-01 §2.6 with four entries. The one thing this page adds to the specification is
`done_when: "states_seen"` with an explicit `states` list — the best-formed gate in the delivery, and
the shape the other pages' gates should be migrated to.

### 7.2 `comparison` — `#s-compare` (G8)

```python
{"type": "comparison",
 "id": "s-compare",
 "eyebrow": "Side by side",
 "eyebrow_tone": "accent-text",             # ⚑ an inline override on this page
 "statement": "The same seven processes. One cell does all of them; one does one.",
 "ground": "band",                          # ⚑ this block is --ks3-band, not --ks3-card
 "columns": [
   {"caption": "Paramecium",              "tone": "alert"},     # header-row colour
   {"caption": "One of your cheek cells", "tone": "on-dark"}
 ],
 "rows": [
   {"name": "Movement",
    "cells": ["Beats hundreds of cilia and swims, reversing when it hits something.",
              "Does not move. It is held in a sheet by the cells around it."]},
   …                                        # 7 rows
 ],
 "row_tones": ["ink", "ink-body"],          # column 2 is one step quieter
 "key_fact": {"eyebrow": "Key fact",
              "text": "One cell doing all seven life processes is an organism. One cell doing one job is part of one.",
              "ground": "card"}             # G6 — card, because the block is band
}
```

Renderer requirements, every one measured:

- Root-level `flex-wrap`, `flex: 0 0 118px` on the label, `flex: 1 1 250px; min-width: 0` on cells.
  **Not a grid.** A grid cannot produce the 820px stack without a second query.
- One `@media (max-width: 820px)` emitting all three narrow declarations together — the label to
  `1 1 100%`, the header row to `display: none`, and the caption to `display: block`.
- **Every cell emits its caption element unconditionally**, hidden by CSS at wide widths. Emitting it
  conditionally would need JS and would break at a container width the query does not know about.
- The captions **are** the column captions — one authored string used twice per column. Do not
  author them twice.
- Zebra from the row index: `i % 2 ? --ks3-inset : --ks3-card`, `border-top: 2px --ks3-rule` on every
  row including the first data row (which sits under the dark header).
- The number of columns is 2 on this page; the flex basis maths only works for 2. **Assert 2**, or
  make the basis a function of the count.

### 7.3 `settles-it` — `#s-settle` (G7)

Payload in §3.5.6. Renderer requirements beyond it:

- **Three row grounds, keyed only on `settles` and `revealed`** — never on the student's mark.
- **Two guards on the reveal**: the `disabled` attribute *and* a re-check inside the state updater.
- **Marks disabled after the reveal**, with unpicked choices at `opacity: .5` and picked choices
  unchanged.
- The `why` opener (`Settles it.` / `Settles nothing.`) is generated from the boolean, in
  `--ks3-font-display`, and is **not** part of the authored string.
- Per-case state: `marks[case][feature]`, `caseOpen[case]`. Switching tabs must not clear either.
- The progress string switches from `"N of M marked"` to `"Opened"`, not to `"M of M marked"`.
- ⚑ **Unresolved before this can be generated**: whether the `agreed` colour distinction (F36) is
  intended. The renderer needs a rule, and only Design can give it.

### 7.4 The microscope's three missing controls (G9, G10, G11)

The engine exists and the physics is settled. What the payload needs:

```python
"sim": {"kind": "microscope",
        "mounts": [                                   # G9
          {"id": "pond", "label": "Pond water", "specimen": "pond water",
           "note": "The dots scattered between them are bacteria, …",
           "caption": "Real ones swim out of the field in seconds. …",
           "alt": "A microscope field of pond water containing …",
           "organisms": [{"kind": "amoeba", "x": -0.90, "y": 0.30,
                          "depth": -0.045, "len": 0.30, "seed": 0.4}, …]},
          {"id": "cheek", "label": "Cheek cells", "specimen": "cheek cells",
           "note": "One layer, one shape, no movement. …",
           "caption": "Stained, so the nuclei show. …",
           "alt": "A microscope field of flat, still cheek cells …"}
        ],
        "start_mount": "pond",
        "centres": [{"id": "amoeba", "label": "The blob", "x": -0.90, "y": 0.30},
                    {"id": "paramecium", "label": "The slipper", "x": 0.15, "y": -0.10},
                    {"id": "euglena", "label": "The green spindle", "x": 0.58, "y": 0.46}],
        "centre_offered_on": ["pond"],                # G10
        "motion_toggle": True, "motion_default": True,
        "motion_labels": ["Swimming", "Held still"],  # G11
        "resolve_notes": {40: "Specks, and one or two shapes. …",
                          100: "Outlines. …",
                          400: "Structures. …"}}
```

`OBJS`' `total` / `fov` / `dof` are **engine constants** under MRB-210, not payload — that is already
ruled and `shared/ks3.js` holds them.

The centre control's arrival forces one engine decision, and it is Code's (§8(c)): **the organisms
must stop swimming when a centre control is present**, because line 1016 says they are held still and
the page wins. F33.

### 7.5 The KEY FACT box, nested (G5, G6)

```python
"key_fact": {"text": "…", "placement": "inside:s-compare", "ground": "card"}
```

Default `placement: "top-level"` and `ground: "band"` (drift 5's ruling). `inside:<id>` appends it as
the last child of the named block and the generator must pick a ground that separates from that
block's own — which is the whole reason G6 exists.

---

## 8. Ambiguities and findings

### (a) Ambiguity for Design — 7

1. **F36 — is the `agreed` colour distinction intended?** `--ks3-ink` vs `--ks3-ink-body` on the
   `why` paragraph is the only trace of whether the student agreed with the page, and it is below
   perception. Either strengthen it (and say how far it may go without becoming a mark under R3) or
   remove the computation. The generator needs one answer. §3.5.4.
2. **F35 — should a revealed case tab show it is done?** Four cases must all be revealed, and the
   tabs are the only navigation, but they carry no state. §3.5.7.
3. **The scope gate has no response of any kind.** A student commits to a magnification and the
   question vanishes with no reveal, no deferral and no wording. Every other commit on the page and
   in the delivery produces *something*. Deliberate? §3.3.1.
4. **D2 — nav brand.** Design's 34×34 accent tile with an inset chevron, against MRB-197's ruled bare
   chevron. Fifth page, identical markup — settled house style, not a slip, and still unresolved
   between the two documents.
5. **R4's flip-card clause is now unarbitrable from Design's delivery.** Measured:
   `document.querySelectorAll('[aria-expanded]').length === 0`, no `.ks3-cards`, no `.ks3-card-btn`.
   **Five reference screens, zero flip cards.** R4's ambiguous *"one tap flips one card"* cannot be
   settled from a delivery that never uses the component. Either R4's clause is dead or Design
   intends flip cards somewhere not yet drawn.
6. **F37's corollary.** The reveal is the only place a mystery cell is named. Confirm that the name
   must never appear in a tab, `aria-label` or `title` — the activity depends on it.
7. **⭐ b1-05's F27 has an answer on this page, and Design should ratify it.** b1-05's hook reveal
   says *"Keep it."* to a flatly wrong option; this page's says *"Three of those four are true of a
   Paramecium and settle nothing"* — deferring without endorsing, and without saying which three.
   That is the wording F27 asked for. Proposed as the family pattern; Design's to confirm. §3.2.

### (b) Science or content — Mide's, and only Mide's — 5

1. **Is the B1-04 / B1-06 pair safe to ship split?** b1-04 asserts *no nucleus ⇒ no instructions ⇒ no
   repair ⇒ no dividing* as a rule; this page qualifies it with a bacterium. Shipped apart, in either
   order, a student is taught something false. §4.5.
2. **Is *"Two lessons ago"* (line 298) safe as a permanent string?** It is true only while B1-05 sits
   between them. F38.
3. **c4's second discriminator.** *"It has a vacuole that keeps filling with water and squeezing it
   out"* settles it because *"Your body holds the fluid around its cells steady, so no cell of yours
   needs to bail out."* Examiner check: is that true without qualification at KS3?
4. **c2's second discriminator.** *"Half a set is only useful if it is going to be added to another
   half. Nothing that lives on its own has half its instructions."* Examiner check against haploid
   single-celled organisms.
5. **Drift 1's ruling now rests on a 1 : 1 tie among live declarations** (§1.6). 232px is still
   defensible on the "8px, no semantics" ground, but the majority argument is gone and Mide may want
   to rule it directly.

### (c) Code's to decide — 6

1. **F33 — the organisms stop swimming when a centre control is present.** The page says so in
   student-facing prose (line 1016) and standing law says the page wins. Code implements it; no round
   trip. §3.3.3.
2. **The settle choice button is a new registry entry** (`settle-choice`, 16px / `10px 16px` /
   `--ks3-r-control`), separate from `seg()`. Same conclusion drift 4 reached for b1-04's option row.
3. **F32 — whether `done_when` needs a `monotonic` flag.** The ladder stage regresses on retry here
   and no stage regresses on b1-05. Both behaviours are unambiguous on their pages; only the
   generator's vocabulary is undecided.
4. **Layer-C assertions for the comparison rows must be written from measurement, not from MRB-210's
   quoted pixels** (§3.4.5). Three of five do not reproduce on the delivered page.
5. **Probe settle on this page is ≥ 2 s after any option-state click** (§4.4), or assert `className`
   and computed style in separate reads.
6. **Ruled by repetition, and §8(c) should now record them as settled:** gating by absence (four
   pages), `ks3-hook-h` being inert (four pages), `tutor_anchor` being a real authored field (six
   instances), `RAIL_SHORT` ≤ 6 characters (five pages), and `scroll-margin-top: 92px` on every
   anchored section (five pages).

### Findings raised on this page

| # | Finding |
|---|---|
| **F30** | `[data-bench-grid]` matches nothing on b1-06 — drift 1 loses its majority, drift 2 keeps its ruling but loses one line of evidence. §1.6 |
| **F31** | The LADDER rail stage ticks on two button presses, with an empty textarea and zero criteria ticked. b1-05's F25 in a new place. §2.1 |
| **F32** | The LADDER stage regresses on "Retry my misses" — the first regressing stage in the delivery. §2.1 |
| **F33** | The page's own caption says the organisms are held still and the slide moves; the repo engine swims them. The page wins. §3.3.3 |
| **F34** | The KEY FACT box is `--ks3-card` here **because** it is nested in a `--ks3-band` block. Drift 5's outlier has a reason, and it implies a `ground` field. §3.4.4 |
| **F35** | The four case tabs carry no completion state, and the rail is the only feedback. §3.5.7 |
| **F36** | `agreed` is computed and rendered as a 6-ΔL* text-colour difference — R3-safe or unfinished, and only Design can say which. §3.5.4 |
| **F37** | The reveal is the only place a mystery cell is named; `answer` must not leak into any label. §3.5.7 |
| **F38** | *"Two lessons ago"* hard-codes the unit's teaching order into a student-facing sentence. §4.5 |

### Findings confirmed from earlier pages

| # | Origin | Status here |
|---|---|---|
| F1 | b1-01 | Inline trail vs `nav.ks3-crumbs` — reproduces, fifth page |
| F2 | b1-01 | Top bar reads 4/4 with nothing answered — reproduces, and four stages is marginally worse than five |
| F12 | b1-01 | Tutor CTA is an `<a>` with an in-page href — sixth instance, `#s-settle` |
| F14 | b1-03 | `.ks3-rung h3` 36.8px vs 26.45px — reproduces |
| F16 | b1-03 | Keynote heading is a 700 uppercase alert eyebrow — reproduces |
| F17 | b1-03 | Ladder `h2` 57.6px vs 43.2px — reproduces |
| F19 | b1-01 | KEY FACT placement — **fourth position**, count now 3 : 1 : 1 |
| F20 | b1-01 | Legal line — absent × 2, safety × 2, copyright × 1 |
| F25 | b1-05 | `done_when` watches a downstream boolean — reproduces as F31 |
| F26 | b1-05 | Form-control id conventions — **three different ones** across the delivery |
| F27 | b1-05 | Static hook reveal with no branching — reproduces structurally, but the wording here does not endorse. §3.2 |
| F29 | b1-05 | A range input needs real CSS, not an inline attribute — **second instance, now a rule** |

### Drift rulings, checked against this page

| Drift | Ruling | Verdict |
|---|---|---|
| 1 | 232px control column | ⚑ **Evidence corrected.** b1-06's declaration is dead CSS; the live count is 1 : 1. Ruling defensible, majority gone. §1.6 |
| 2 | 820px collapse | ✅ **Stands.** Its stated basis — 820 already ruled on this page for the comparison rows — is verified live and bisected exactly. One line of its evidence (b1-06's bench-grid 820) should be struck. |
| 3 | `clamp(28px, 3.9vw, 44px)` statement | ✅ **Evidence reproduces.** b1-06 line 217 is a real statement at `clamp(26px, 3.6vw, 40px)`, measured 40 / 29.52 / 26. It is one of the four the corrected drift 3 counts. |
| 4 | b1-06's `seg()` light branch | ✅ **Confirmed by measurement.** Both branches share 17px / `11px 17px` / 44px / `--ks3-r-control`, differing only in colour — the property the ruling turns on. |
| 5 | `var(--ks3-band)` KEY FACT | ✅ **Outlier confirmed, and explained.** `--ks3-card` here is forced by nesting in a band block, not drift. Ruling unchanged; a `ground` field is now required. F34 |

---

## Provenance

Measured 13 August 2026 on branch `feat/ks3-b1`, in headless Chrome via `ks3_browser.py`
(`Emulation.setDeviceMetricsOverride`), against
`docs/ks3/design-reference/b1/b1-06-unicellular-organisms.dc.html` (1,145 lines, unmodified), served
over HTTP from `docs/ks3/design-reference/b1/`.

Seven probe passes: skeleton and comparison rows at four viewports; the "settles it" activity driven
through eleven paths across three clean loads; the microscope driven through both mounts, three
objectives, three centres, the motion toggle and a seven-point focus sweep; the rail driven to all
four stages done at 1340 and F2-scrolled at 1280; the ladder driven through correct, wrong and retry
with a 2.2 s settle; a container sweep at 360 / 400 / 846 / 878 / 926 for MRB-210's figures; and a
matched-rule probe walking `document.styleSheets` to attribute computed values to their source.

Console clean at every viewport on every pass. Scratch scripts were written to the session
scratchpad, not to the repo. **No file in the repository was modified except this one.**
