# B1 L5 · Levels of organisation · SYSTEM

Inventory of `docs/ks3/design-reference/b1/b1-05-levels-of-organisation.dc.html` (929 lines,
delivered unmodified). Method, viewports, generator vocabulary and standing law: see `README.md` in
this folder — not restated here. Cross-page value collisions: `00-delivery-drift.md`.

Measured 13 Aug 2026 in headless Chrome via `ks3_browser.py`, serving
`docs/ks3/design-reference/b1/` over HTTP, at **1280 · 1340 · 820 · 390** with
`Emulation.setDeviceMetricsOverride` (`page.set_viewport`). Every number below was read from
`getComputedStyle` / `getBoundingClientRect` in that browser, or out of the file's own source.
Where a value could not be measured it says so.

**Console: clean.** No errors or uncaught exceptions at any of the four viewports (favicon 404
filtered), on either this page or the generator's.

Where b1-01 → b1-04 have already established something true of all six pages — the header trail
carried inline, the rail's two variants, F2 (the narrow-screen top bar reading complete when nothing
was answered), the `_ds` bundle shipping the 3D Studio stylesheets, the 60-token set, the DC-runtime
settle trap, `sc-interp` wrapping every `{{ }}`, `ks3-hook-h` being inert, Design's `ks3-ladder`
single-class set, and the content living in `<script data-dc-script>` constants — this file
**confirms and cites** rather than re-deriving. Its length is spent on what is different here, and
on the four things the task asked for: the MRB-203 comparison (§3.1), the MRB-202 wording check
(§3.1.7), the `system-parts` divergence (§4.1), and drift 3's real cost (§3.3.1).

## ⚠️ This page is the one Mide rejected by name

MRB-203 cites **B1 L5 `levels-of-organisation`** as one of the two pages he compared against
Design's C1 reference and found wanting: *"no progress rail anywhere; smaller type throughout; a
flat uniform stack — the same card shape repeating down the page."* §3.1 tests all three charges
against measurement, on both pages, at all four viewports. **All three hold**, and the third is
worse than the words suggest: it is not that the stack is uniform, it is that **20 of the
generator's 21 blocks are one of five shells** while Design's page carries five bespoke instruments.

Note also that **b1-05 is a SYSTEM lesson but not the SYSTEM reference screen** —
`docs/ks3/design-coverage-manifest.md` §10.1 gives that row to b1-04, which §10.1 admits exactly one
of per family. So this page is a *second* SYSTEM realisation, and the two do not share an
instrument: b1-04's flagship is a four-specimen tuning bench, this one's is a five-stop zoom. That
is a fact about the family, recorded in §3.1.8.

---

## Content payload — line ranges for a byte-identical lift

**Never retype these.** Every string is authored and science-bearing.

| Payload | Lines |
|---|---|
| `RAIL` (5 nodes, `{id, label}`) | **356–362** |
| `RAIL_SHORT` | **364** |
| `isDone` | 366–373 |
| **`LEVELS`** — 5 levels × (tick/name/size/what/gainLabel/gain/human/alt) | **375–406** |
| `RUNGS_OF` — the 6 rung choices | **408** |
| **`HARD`** — 8 items × (id/item/answer/note) | **410–427** |
| **`CASES`** — 4 cases × (id/label/what/intact/lost/3 predicts/headline/body/principle) | **429–459** |
| `RUNGS` (page-marked r1, r2, with per-option `correction`) | **461–478** |
| `SELF_RUNGS` (r3, r4, with `fieldLabel`/`placeholder`/4 criteria) | **480–501** |
| canvas helpers `rr` / `ell` / `leafShape` | 503–531 |
| initial `state` (incl. the `startZoom` seeding) | 534–547 |
| the four zoom drawing routines `plant` / `oneLeaf` / `leafSection` / `oneCell` | **569–688** |
| `draw()` — the 900×500 design space, the 2× transform, and the **`boxes` array** (the orange "next stop is here" rectangle per stop) | **690–737** |
| `seg()` — **both branches** | **739–748** |
| `renderVals` (style strings + `hookOptions` + UI strings) | 750–924 |

Static prose: header 76–83 · hook 85–107 (the 4 hook options are **data**, at 788–792; the reveal at
**103** is static) · `#s-zoom` intro 109–112 · `#s-hard` intro 142–145 · `#s-break` head + lede
169–177 · `#s-think` **217–229 (both misconceptions are static markup, not data)** · KEY FACT
**231–235** · ladder head 237–247 and retry note 301–304 · keynote 307–310 · stretch layer 312–320 ·
endmatter 322–345.

**Authored word count (for MRB-205): ~2,630 words**, counted by the same script method b1-03 and
b1-04 used:

| Source | Words |
|---|---|
| data constants, lines 356–501 (single-quoted literal content) | **1,884** |
| of which `CASES` 429–459 | 602 |
| of which `LEVELS` 375–406 | 541 |
| of which `HARD` 410–427 | 269 |
| of which `SELF_RUNGS` 480–501 | 223 |
| of which `RUNGS` 461–478 | 214 |
| of which `RAIL` + `RAIL_SHORT` + `RUNGS_OF` | 35 |
| `renderVals` **prose** literals (4 hook options + 12 UI strings + `'Level lost: '`) | ~62 |
| the canvas label `'NEXT STOP IS HERE'` (line 734) | 4 |
| static markup 76–345, tags and `{{ }}` stripped | **683** |

⚠️ Same caveat as b1-04: a naive extraction of all single-quoted literals from `renderVals` returns
35 strings, but 13 of those are **class-name fragments** (`'is-correct'`, `' is-spent'`,
`'ks3-tally'`, `'ans-'`) and the style strings are excluded by construction. The 62 above is prose
only.

**None of these 2,630 words exists in `ks3_data/`.** The generator's `levels-of-organisation` record
is a different lesson — different big question, different hook, different misconceptions, different
ladder, different key note. §3.1.2.

---

## 1. Page skeleton

### 1.1 The spine — confirms b1-03 §1.1 and b1-04 §1.1

`<body>` holds the hydrated **`<div class="rd" data-mode="ks3" id="dc-root">`** and the logic
`<script>`; the `<x-dc>` template is removed rather than hidden. `.rd` is a DIV, not `<body>`, with
the same 8 inline declarations reproducing what `body.rd[data-mode="ks3"]` would give, and the token
block is `.rd[data-mode="ks3"]` so all tokens resolve. **All 35 `--ks3-*` tokens probed resolved to
their `shared/ks3.css` values** (§6.1).

`.rd` children, in order — **5 top-level landmarks, same set as b1-01, b1-03 and b1-04**:

| # | Element | Position | Height 1280 |
|---|---|---|---|
| 1 | `nav.ks3-nav` | static | 63.19 |
| 2 | `nav[data-rail="top"]` | **sticky, top 0, z-index 20** | 46.59 |
| 3 | `nav[data-rail="side"]` | **fixed, top 150px, left calc(50% − 632px), width 104px, z-index 20** | 0 (`display:none` <1340) |
| 4 | `main.ks3-main` | static | 8396.73 |
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
| document height | **8614** | 8568 | 8788 | **12867** |

The narrow breakpoint is `@media (max-width: 34rem)` in `shared/ks3.css`, identical to b1-01/03/04
(not re-bisected here — the padding values at 390 match those pages exactly).

**The page's own media queries are exactly two:** `min-width: 1340px` (rail swap, source line 21)
and `prefers-reduced-motion: reduce` (kills `[data-arrive]`, line 22). Enumerated by walking
`document.styleSheets` and following every `CSSImportRule`; the remaining conditions
(`print`, `(prefers-reduced-motion: no-preference)`, `(max-width: 34rem)`, `(max-width: 1023px)`,
`(max-width: 699px)`, `(max-width: 830px)`) all come from the `_ds` bundle.

⚑ **This page declares no bench grid at all**, so **drifts 1 and 2 do not touch it.** There is no
`[data-bench-grid]`, no 232/240 column and no 780/820 collapse. Its one two-column-ish layout is the
`#s-hard` choice row, which is a plain `flex-wrap` and has no breakpoint. Confirmed by source (the
page's `<style>` block, lines 14–28, contains only the `b5-arrive` keyframes, the rail rules, the
reduced-motion rule and the `input[type=range].b5-zoom` styling) and by the media enumeration above.

**No `.ks3-explainer` and no 736px `--ks3-measure` column anywhere.** Prose is capped by `ch`
measures instead: `54ch` on `#s-zoom`'s intro (measured `max-width: 683.316px`), `54ch` on
`#s-hard`'s intro, `58ch` on `#s-break`'s lede.

### 1.3 Header carries the lesson trail INLINE — confirmed

Nav markup and every resolved value match b1-01 §1.3, b1-03 §1.3 and b1-04 §1.3: `display:flex;
flex-wrap:wrap; gap:6px 0`; brand Bricolage with a 34×34 `--ks3-accent` r10 tile holding a 20×20
`#FBF3E6` chevron; 2×26 `--ks3-rule` divider at `margin 0 20px`; `ol[aria-label="Breadcrumb"]` at
body-font 17px, gap 9px, `--ks3-accent-text` 600 links; trailing `a.ks3-nav-link` "KS3".

Nav height is **63.19 at 1280, 1340 and 820**, growing to **153.97 at 390** (trail over 2 rows) —
the same pure-function-of-title-length behaviour b1-03 and b1-04 recorded. **A parity assertion must
not pin nav height to a number.** F1 (Design's inline trail vs the generator's `nav.ks3-crumbs`
inside `<main>`) reproduces exactly; measured against the generator's in §3.1.4.

### 1.4 Lesson body, document order — **11** direct children of `.ks3-lesson`

| # | Element | id | classes | margin-top | scroll-margin-top | h @1280 |
|---|---|---|---|---|---|---|
| 1 | `header` | — | `ks3-lesson-head` | — | 0 | 355.94 |
| 2 | `section` | `s-hook` | `ks3-block ks3-dark ks3-hook` | 28px | 92px | 652.73 |
| 3 | `section` | `s-zoom` | `ks3-block` | 28px | 92px | **1274.64** |
| 4 | `section` | `s-hard` | `ks3-block` | 28px | 92px | **1465.39** |
| 5 | `section` | `s-break` | `ks3-block ks3-dark ks3-practical` | 28px | 92px | 854.14 |
| 6 | `section` | `s-think` | `ks3-block ks3-misconception` | 28px | 92px | 516.31 |
| 7 | **`div`** | — | **none** — the KEY FACT box | **24px** | 0 | 127.17 |
| 8 | `section` | `s-ladder` | **`ks3-ladder`** (single class) | 28px | 92px | 1815.83 |
| 9 | `section` | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | 28px | 92px | 248 |
| 10 | `section` | — | `ks3-layer` | 34px | 0 | 254.28 |
| 11 | `div` | — | `ks3-endmatter` | 34px | 0 | 410.3 |

Three structural facts:

- **The stray unclassed KEY FACT `<div>` is here again**, at top level between `#s-think` and
  `#s-ladder`, no class, no id, `margin-top: 24px` where every neighbour uses 28 or 34, and
  anomalously indented in source (231–235). That is **b1-04's exact shape** — so across four pages
  the box has taken three positions and this is the **second vote for top-level-orphan-after-think**
  (b1-01: top-level orphan; b1-03: inside `#s-think`; b1-04 and b1-05: top-level orphan here).
  F19 now has a 2:1:1 count. Still needs one answer.
- **There is NO `p.ks3-legal`.** Measured `document.querySelector('.ks3-legal') === null`. That is
  the **second** page with the slot empty (b1-04 was the first), against b1-01's copyright and
  b1-03's safety line. F20 strengthened: absent × 2, copyright × 1, safety × 1.
- **`#s-zoom` and `#s-hard` are plain `.ks3-block`** — no modifier class at all. Their whole
  appearance beyond the block shell is inline. Neither of them maps to any registered block type.

### 1.5 Class audit and stylesheet set

The page uses **53 `ks3-*` class names, and all 53 exist in `shared/ks3.css`** (checked by string
match of `.<class>` against the sheet; **zero misses**), plus `rd`, `sc-host`, `sc-interp` and one
page-local `b5-zoom` (the range input). There is **no `ks3-hook-h`** — the hook `<h2>` carries no
class and is styled by `.ks3-hook h2`. That is the **third** independent confirmation of b1-01's
recommendation to drop the class.

⚑ **The count is 52 on load and 53 after one click.** There is no `ks3-reveal` in the resting DOM —
the hook's reveal is gated by `<sc-if value="{{ hookRevealed }}">`. Measured both ways. A parity
probe that enumerates classes on load will under-report this page by exactly one, and the missing
one is a component with its own colours.

Everything else is carried by **174 inline `style=` attributes** (b1-03: 225, b1-04: 125, b1-01:
110) plus **11 JS-built style strings** (`seg` — used for two different components; `node.chipStyle`
/ `textStyle` / `lineStyle` / `linkStyle`; `railBarStyle`; `row.style`; `c.style`; `t.style`;
`row.answerStyle`; `hardBtnStyle`; `caseLevelStyle`; plus the class-name builders `feedbackClass`
and `tallyClass`).

**Stylesheet sets differ exactly as b1-03 §1.5 recorded, and both consequences reproduce.**

| | Reference page | Generated page |
|---|---|---|
| sheets | **9** (2 inline + `_ds/…/styles.css` → 5 imports + 1 inline) | **4 link tags** |
| KS3 rules | `_ds/…/tokens/shared-ks3.css` | `/shared/ks3.css?v=41a3ad43` |
| tokens | `_ds/…/tokens/shared-tokens.css` | `/shared/tokens.css?v=8bc49b72` |
| **`shared/styles.css`** | **absent** | **present** (`?v=2da37530`) |
| **`shared/nav.css`** | **absent** | **present** (`?v=2fd4a55f`) |
| 3D Studio CSS | `_ds_bundle.css` **and** `tokens/src-styles-tokens.css` | absent |

b1-03's **F14** and **F17** both reproduce, to the same numbers, on a third page:

| | reference | generated |
|---|---|---|
| `.ks3-rung h3` | 23px / **36.8px** (1.6) | 23px / **26.45px** (1.15) |
| ladder `h2` | 36px / **57.6px** (1.6) | 36px / **43.2px** (1.2) |

---

## 2. The progress rail — same component as b1-01/03/04, **five** stages

Byte-for-byte the component b1-01 §2 specified. Confirmed by measurement, not re-derived:

- **Two variants, never both, never neither.** Bisected: at **1339** `[data-rail="side"]` is
  `display:none` and `[data-rail="top"]` is `display:block`; at **1340** the reverse. Same two
  authored rules (source lines 20–21).
- **Side rail geometry identical:** `fixed`, `top 150px`, `left calc(50% − 632px)` → **x 38** at
  1340, `width 104px`, `z-index 20`; `.ks3-lesson` starts at **x 190** → a 48px gutter. Height
  **416.94** for five nodes — *identical to b1-03's five-node rail*, which is a useful assertion: rail
  height is a pure function of node count.
- **Chip states identical, every colour a token.** Measured across a full drive:
  done = `--ks3-accent` #E4572E ground, `--ks3-ink` border, `--ks3-on-dark` text, holds
  `svg.ks3-mark` (`hasMark: true`, `chipTxt: ""` — the number is *replaced* by the tick);
  current-not-done = `--ks3-card` #FFFCF5 on `--ks3-ink` with `box-shadow: 0 0 0 4px
  --ks3-accent-tint` (measured `rgb(252,231,222) 0 0 0 4px`); future = `--ks3-card` on
  `--ks3-rule-strong` #C3B191 with `--ks3-ink-ghost` #9A8F86 text. Chip 32×32, r10, Bricolage
  16px/800, border 2px.
- **Label** MONO 11px/500, `letter-spacing .09em` (0.99px), uppercase, lh 1.2; current `--ks3-ink`,
  done `--ks3-ink-muted`, future `--ks3-ink-ghost`.
- **Connector** 2×20 at `margin 7px 0`; `--ks3-accent` when the node above is done, else `--ks3-rule`
  #E0D2B9. Omitted on the last node (`hasLine: i < RAIL.length - 1`).
- **Top bar** `sticky; top 0; z-index 20; background --ks3-ground; border-bottom 2px --ks3-rule;
  padding 9px 16px 10px`; inner row `flex; gap 12px; max-width 60rem; margin 0 auto`; count MONO
  15px/500 `--ks3-ink-muted`; current label 16px/700 `--ks3-ink` with ellipsis (measured **795px**
  at 1280); track `flex 0 0 96px`, height 8px, r99, `--ks3-band` ground, `2px --ks3-ink`; fill 4px
  inside the border, `--ks3-accent`.

### 2.1 Five stages, and their two label sets

`RAIL` 356–362 + `RAIL_SHORT` 364:

| # | anchor | side label (`RAIL_SHORT`) | top-bar label (`RAIL[].label`) | `done_when` (`isDone`, 366–373) |
|---|---|---|---|---|
| 1 | `#s-hook` | HOOK | Cells in a dish | `s.hookChoice !== null` |
| 2 | `#s-zoom` | ZOOM | Five stops | `Object.keys(s.seenZoom).length >= 5` |
| 3 | `#s-hard` | SORT | The awkward ones | `!!s.hardOpen` |
| 4 | `#s-break` | BREAK | Take a level out | `Object.keys(s.casePick).length >= 4` |
| 5 | `#s-ladder` | LADDER | Mastery ladder | `answers.r1 !== undefined && answers.r2 !== undefined && checked.r3 && checked.r4` |

Both label sets are authored and neither is derivable from block titles. `RAIL_SHORT` is ≤6 chars,
consistent with all three earlier pages — worth asserting, because the 104px column at MONO 11px
`.09em` is what sets the limit.

Fill maths is `(active + 1) / 5 × 100%` — measured **20 / 40 / 60 / 80 / 100 %** giving
**18.39 / 36.8 / 55.19 / 73.59 / 92** of a 92px inner track (96px less its 2px border each side).

**All five stages are reachable and I drove all five to done, in order.** Three notes, all measured:

- **Stage 2 is honest.** `seenZoom` is pre-seeded with the `startZoom` prop's stop (`{0: true}` by
  default), so one of five is banked at load; the student must visit the other four. Measured:
  ZOOM ticked only after all five stops had been visited.
- **⚑ Stage 3's `done_when` is a *button press*, not work done.** `isDone('s-hard')` is
  `!!s.hardOpen`, and `hardOpen` is set only by "Open the answers", which is itself gated on all 8
  items being placed (`hardLocked = placed < 8`, measured `disabled: true` → `false` after 8
  clicks). So the gate is real, but it is **transitively** real: the rail is watching the reveal, not
  the placements. If the button's guard were ever relaxed, the stage would tick for free. Compare
  b1-03's BENCH, which b1-03 §2 criticised for ticking on a single cheap control. Finding **F25**:
  `done_when` should be able to name the *count* (`8 of 8 placed`), the way b1-04's F21 asked for a
  threshold — not a downstream boolean.
- **Stage 4 asks for all of what is on the page.** `casePick` is keyed by case id and there are
  exactly 4 cases; `isDone` wants 4. Measured: the block's own counter read "4 of 4 explored" at the
  moment BREAK ticked. **This is the fix for b1-04's F21** — rail and instrument agree here. Worth
  recording as the pattern to prefer.
- **No stage can regress.** Nothing in this page removes a key from `seenZoom` or `casePick`, and
  `hardOpen` is one-way. Unlike b1-03's FIT, an earned stage stays earned.

### 2.2 F2 reproduced, on five stages

b1-01's F2 ("the top bar shows scroll, not completion") reproduces exactly. Driven at 1280 with
`scrollIntoView` at each anchor and **nothing answered**:

| scrolled to | count | label | fill |
|---|---|---|---|
| `#s-hook` | 1 / 5 | Cells in a dish | 20% → 18.39 / 92 |
| `#s-zoom` | 2 / 5 | Five stops | 40% → 36.8 |
| `#s-hard` | 3 / 5 | The awkward ones | 60% → 55.19 |
| `#s-break` | 4 / 5 | Take a level out | 80% → 73.59 |
| `#s-think` | 4 / 5 | Take a level out | 80% (stale) |
| `#s-ladder` | **5 / 5** | Mastery ladder | **100% → 92 / 92 (full)** |
| `#s-keynote` | 5 / 5 | Mastery ladder | 100% (stale) |

`#s-think` and `#s-keynote` are anchored but unlisted, so the `IntersectionObserver`
(`rootMargin: '-45% 0px -50% 0px'`, lines 550–556) never fires for them and the bar sits stale
through them. **A student under 1340px reads a complete progress bar having answered nothing**, and
the side rail — the variant that does read completion — is the one they cannot see. Still F2.

⚑ Worth stating against b1-04's note that "fewer stages makes it worse": **five stages makes it
slightly better but does not fix it.** Each scroll step is 20% rather than 25%, so the bar is
marginally more honest per block, and the *whole* defect is unchanged. The fix is not a stage count.

### 2.3 Anchors

**All 7 lesson sections carry `scroll-margin-top: 92px`**, authored individually as an inline style
on each (`s-hook`, `s-zoom`, `s-hard`, `s-break`, `s-think`, `s-ladder`, `s-keynote`). The rail
references **5 of the 7**. `#dc-root` (the runtime's wrapper) and the four form-control ids
(`zoom`, `ans-r3`, `ans-r4`, and the criteria checkboxes) carry 0. The KEY FACT div, `.ks3-layer`
and `.ks3-endmatter` carry no anchor.

Full id list measured: `dc-root`, `s-hook`, `s-zoom`, **`zoom`** (the range input), `s-hard`,
`s-break`, `s-think`, `s-ladder`, `ans-r3`, `ans-r4`, `s-keynote`. ⚑ Note `id="zoom"` is a bare,
un-namespaced id on a form control inside a lesson — the generator's convention is
`ks3-<thing>-<slug>-<field>`. A collision is a real risk once two instruments share a page.
Finding **F26**.

### 2.4 What the generator needs to emit it

Identical shape to b1-01 §2.6, b1-03 §2.4 and b1-04 §2.4, five entries:

```python
"rail": [                                     # NEW field, §5 gap G1
  {"anchor": "s-hook",   "short": "HOOK",   "label": "Cells in a dish",
   "done_when": "committed"},
  {"anchor": "s-zoom",   "short": "ZOOM",   "label": "Five stops",
   "done_when": "all_stops_seen", "threshold": 5},
  {"anchor": "s-hard",   "short": "SORT",   "label": "The awkward ones",
   "done_when": "answers_opened"},            # ⚑ F25 — prefer "all_placed", threshold 8
  {"anchor": "s-break",  "short": "BREAK",  "label": "Take a level out",
   "done_when": "all_cases_explored", "threshold": 4},
  {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
   "done_when": "ladder_complete"},
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
| 1 | `header.ks3-lesson-head` — eyebrow "Cells and organisation · System", h1, `.ks3-bigq`, `.ks3-review-flag` | **E** | draft flag present / absent (`showDraft` prop) | lesson title · big question · eyebrow · draft badge |
| 2 | `#s-hook` — ink-dark: eyebrow, h2, prompt, `.ks3-hook-commit` with `.ks3-commit`, 4 `.ks3-option`s, gated `.ks3-reveal` | **E★** | option resting / chosen (border → `--ks3-alert`); reveal hidden / shown | hook is ink-dark, accent shadow · dark-block option resting/CHOSEN |
| 3 | `#s-zoom` — **the ZOOM instrument**: 1800×1000 canvas, a 5-stop range slider, 5 segment ticks, a 5-field readout panel (§3.3) | **N** | 5 stops × (canvas frame + orange next-stop box + readout) | **none registered** |
| 4 | `#s-hard` — **the SORT instrument**: 8 rows × 6 choices, unmarked until a gated reveal marks all 8 at once (§3.4) | **N** | row unplaced / placed / (after reveal) right / wrong; button locked / live | **none registered**; ⚑ and it marks (§3.4.2) |
| 5 | `#s-break` — the **case-and-consequence practical**: 4 dark tabs, predict gate, cream reveal island (§3.5) | **E★** | 4 cases × (unpredicted / predicted) | `sim canvas` gates `practical` today and there is no `.ks3-sim` here |
| 6 | `#s-think` — misconception carrying **two** quote/answer pairs split by an `--ks3-alert-border` rule | **E★** | static | misconception is amber |
| 7 | **unclassed `<div>`** — one KEY FACT box, top-level, `mt 24px` | **N** | static | none |
| 8 | `#s-ladder` — `class="ks3-ladder"`, head + score, 2 page-marked rungs, 2 self-marked rungs, `.ks3-retry-wrap` | **E** | option resting / correct / wrong / spent; feedback correct / wrong; ticks 0..4; tally not-yet / met; retry | ladder shell · ladder heading · ladder option ×6 states+badges · ladder feedback CORRECT/WRONG · page-marked rung is accent · self-marked rung is violet · R8 answer box · R8 check-my-answer button |
| 9 | `#s-keynote` — ink-dark, alert-yellow shadow, **`p.ks3-eyebrow`** + one paragraph | **E★** | static | key note is ink-dark · key note type drops to 700 |
| 10 | `.ks3-layer` — "Going further" violet stretch layer, **one bare `<p>`** | **E★** | static | stretch layer is violet |
| 11 | `.ks3-endmatter` — **4 cards**: "Before this lesson" (1 link) · "Connects to" (2 links) · "At GCSE this becomes" (**prose**) · `.ks3-tutor` (**live `<a href="#s-hard">`**) | **E★** | static | tutor card is accent · tutor text is large-bold |
| — | `p.ks3-legal` | — | **ABSENT** | — |

Totals: **2 blocks the generator can already produce (E)**, **6 it produces in the wrong shape
(E★)**, **3 it cannot produce at all (N)**. Two of the five rail stages sit inside N blocks.

---

### 3.1 ⭐ Design's approved page versus the generator's current output, component by component

This is the point of measuring this page: it is the one MRB-203 names. Generated page measured at
the same four viewports from
`mrbadmus_site/ks3/biology/cells-and-organisation/levels-of-organisation.html` (71 lines, build
already run), served over HTTP from `mrbadmus_site/`. Console clean at all four.

#### 3.1.1 Mide's three charges, tested

| Charge | Verdict | Measured evidence |
|---|---|---|
| **"No progress rail anywhere"** | **TRUE, exactly.** | `document.querySelectorAll('[data-rail]').length === 0` at 1280, 1340, 820 and 390. Not hidden, not broken — absent. And **no block on the generated page carries an `id` or a `scroll-margin-top`**: measured `smt: "0px"` on all 21 children, and the only 11 ids on the page are form-control ids (`ks3-sim-part-1`, `ks3-ans-…`, `ks3-crit-…`). There is nothing for a rail to anchor to even once the rail exists. |
| **"Smaller type throughout"** | **TRUE, but not the way it sounds — and this is the important correction.** | Every shared component's type is **identical to the pixel**: `h1` 74px/69.56/−2.59px on both; hook `h2` 38px/39.9 on both; `.ks3-option` 18px/600 on both; body prose 19px/1.6 on both. The generator is not rendering the same things smaller. What it is missing is a **whole tier of body-level display type that only exists inside Design's instruments**: 30px live level name, 26px case headline, 22px display KEY FACT, 21px "what we did", 20px "gain" line, 20px hard-row item. Measured on the generated page: **there is no type between 19px and 28px anywhere**, and every size above 19px is a heading (`h2` 28/30/36/38, `h1` 74). Design's page has five distinct sizes in that band. The type *scale* is intact; the type *surfaces* are gone with the components they live in. |
| **"A flat uniform stack — the same card shape repeating"** | **TRUE, and stronger than stated.** | 21 children, and **20 of them are one of five shells**: `.ks3-block.ks3-check` ×4, `.ks3-block.ks3-explainer` ×2, `.ks3-figure.ks3-figure-pending` ×3, `.ks3-block.ks3-misconception` ×2, `.ks3-block.ks3-dark.ks3-practical` ×2, plus one each of hook / keywords / ladder / keynote / layer / endmatter / legal. Four consecutive `ks3-check` blocks render the identical 30px-padded cream card with an `h2` and 3 options. Design's 11 children include **five shapes that appear once each** (`#s-zoom`, `#s-hard`, `#s-break`, the KEY FACT div, the ladder) and no block type repeats except `.ks3-block` as a bare shell twice. |

#### 3.1.2 They are not the same lesson

| | Design (b1-05) | Generator |
|---|---|---|
| Big question | *"A dish of living stomach cells cannot digest a sandwich. Your stomach can. What is the difference?"* | *"How do you get from one cell to a whole animal?"* |
| Hook | stomach cells grown in a dish; a sandwich sits there | pulling cooked steak apart with two forks |
| Instruments | five-stop plant zoom · eight-item sorter · four-case removal | a `system-parts` dependency graph |
| Worked-through example | a **plant** (whole plant → shoot → leaf → palisade layer → palisade cell) | a **human** (muscle cell → muscle tissue → stomach → digestive system) |
| Misconceptions | *"An organ is just a bigger tissue"* · *"Blood can't be a tissue — it's a liquid"* | *"The levels are just about size"* · *"Blood is not a tissue, because a tissue is solid"* |
| Ladder r1 | Blood — which level? (4 options) | What is a tissue? (4 options) |
| Key note | *"Cells, tissues, organs, organ systems, organism. Each rung can do something the rung below it cannot…"* | *"…It is about what works with what, never about size — a pea-sized gland is an organ and a leg bone is a tissue."* |

They share a title, a slug, a family and the blood-is-a-tissue misconception. **Every one of Design's
2,630 words is new content**, and the generator's ~1,900 words are a different lesson that will be
displaced, not ported. This is the same situation b1-04 §3.1.1 recorded and it is Mide's call
whether any of the generator's current wording survives (§8(b)).

#### 3.1.3 Structure: 11 blocks against 21

| | Design (11 children) | Generator (21 children) |
|---|---|---|
| 1 | `header.ks3-lesson-head` | `header.ks3-lesson-head` |
| 2 | `#s-hook` (hook **+ commit + 4 options + gated reveal in one dark block**) | `.ks3-hook` (prose only, ends on a `.ks3-commit` `<p>` with **no buttons**) |
| 3 | `#s-zoom` — the ZOOM instrument | `.ks3-check` `smallest-piece` |
| 4 | `#s-hard` — the SORT instrument | `.ks3-explainer` |
| 5 | `#s-break` | `.ks3-figure.ks3-figure-pending` |
| 6 | `#s-think` (2 quote/answer pairs) | `.ks3-keywords` (**3 flip cards**) |
| 7 | KEY FACT `<div>` | `.ks3-check` `size-trap` |
| 8 | `#s-ladder` | `.ks3-misconception` `not-about-size` |
| 9 | `#s-keynote` | `.ks3-practical` `level-sorter` |
| 10 | `.ks3-layer` | `.ks3-check` `blood-check` |
| 11 | `.ks3-endmatter` | `.ks3-misconception` `blood-is-a-tissue` |
| 12 | — | `.ks3-figure.ks3-figure-pending` |
| 13 | — | `.ks3-practical` `break-the-chain` (holds `ks3-sim data-sim="system-parts"`) |
| 14 | — | `.ks3-explainer` |
| 15 | — | `.ks3-figure.ks3-figure-pending` |
| 16 | — | `.ks3-check` `plant-ladder` (criteria button) |
| 17 | — | `.ks3-ladder` |
| 18 | — | `.ks3-keynote` |
| 19 | — | `.ks3-layer.ks3-stretch` (holds a nested explainer + check) |
| 20 | — | `.ks3-endmatter` |
| 21 | — | `p.ks3-legal` |

Generator block-type census, measured: `check` 4 · `figure` 3 · `explainer` 2 · `misconception` 2 ·
`practical` 2 · `hook` 1 · `keywords` 1 · `ladder` 1 · `keynote` 1 · `layer` 1 · `endmatter` 1 ·
`legal` 1.

Consequences that are facts, not readings:

- **The generator's hook does not commit.** Design's `#s-hook` ends with 4 `.ks3-option`s and a
  gated reveal *inside the dark block*; the generator's `.ks3-hook` ends with a `.ks3-commit`
  paragraph and the commit moves to a separate light `.ks3-check` (`smallest-piece`). Same
  divergence b1-03 and b1-04 recorded — now on a third family instance.
- **Three `ks3-figure-pending` slots vs one live canvas.** Design carries no `<figure>` at all: its
  diagram is one live 1800×1000 canvas drawn from data by **120 lines of routine** (569–688) plus
  a 48-line `draw()`. The generator carries three dashed "Diagram coming soon" placeholders
  (measured `3px dashed --ks3-rule-strong` #C3B191, `--ks3-inset` #F7EFE1 ground, `padding 52px
  24px`, r24) and no plant drawing at all. **On this lesson the levels are drawn; on the generator's
  version they are a to-do, three times.**
- **7 flip cards vs 0.** Measured on the reference page:
  `document.querySelectorAll('[aria-expanded]').length === 0`, and no `.ks3-cards` /
  `.ks3-card-btn`. **Three reference screens inventoried, three with no flip card at all.** R4's
  ambiguous clause (*"one tap flips one card"* — at most one open, or one card per tap?) still
  cannot be arbitrated from Design's delivery. b1-03 §3.1.6 flagged it, b1-04 added a second
  silence, this is the third. §8(a).
- **The generator's endmatter has 3 cards, not 4** — heads measured `["Before this lesson", "At GCSE
  this becomes", "Stuck? Ask Mr Badmus AI"]`. **b1-03's D7 reproduces here** (it did not on b1-04):
  `references` is unrendered and there is no "Connects to" card. Design has all four, and writes the
  third as prose where the generator renders `ks4_links` as two links.

#### 3.1.4 Where they diverge — chrome, eight items measured

| # | Component | Design (b1-05) | Generator | Verdict |
|---|---|---|---|---|
| D1 | **Progress rail** | 2 variants, 5 stages, threshold 1340 | **absent** (0 `[data-rail]`, 0 `scroll-margin-top`) | new component, §7.1 |
| D2 | **Nav brand mark** | 34×34 `--ks3-accent` r10 tile with a `#FBF3E6` chevron 20×20 inside, then wordmark | **bare `#E4572E` chevron SVG 30×30, no tile** (measured `.ks3-brand span` absent); `a` 176.97×35.19 | ⚑ **Design diverges from MRB-197's own ruling**, which specifies the generator's version. Third page, identical markup — settled house style, not a slip. For Design |
| D3 | **Breadcrumb** | body-font 17px, gap 9px, `--ks3-accent-text` 600 links, **inline in `nav.ks3-nav`** behind a 2px divider | `nav.ks3-crumbs` **inside `<main>`**, MONO 14px `--ks3-ink-muted`, `margin 0 0 24px`, full-width (**1232px** at 1280) | b1-01's F1, unchanged |
| D4 | **Keynote heading** | `<p class="ks3-eyebrow">Key note</p>` → Bricolage **30px / 700 / UPPERCASE / `--ks3-alert` #FFC53D** | `<h2>Key note</h2>` → Bricolage **30px / 800 / sentence case / `--ks3-on-dark` #FBF3E6** | b1-03's F16, reproduced exactly. **Three reference screens now agree with each other and disagree with the build** |
| D5 | **Ladder `h2` line-height** | `class="ks3-ladder"` alone → `.ks3-block h2` misses → **36px / 57.6px (1.6)** | `class="ks3-block ks3-ladder"` → **36px / 43.2px (1.2)** | b1-03's F17, third confirmation |
| D6 | **Rung `h3` line-height** | 23px / **36.8px (1.6)** | 23px / **26.45px (1.15)** | b1-03's F14 (`shared/styles.css` absent), third confirmation |
| D7 | **Tutor CTA** | `<a class="ks3-tutor-cta" href="#s-hard">Ask about this lesson</a>`, 18px/600, `--ks3-card` on `--ks3-accent-text`, r12; heading "Ask Mr Badmus AI"; line *"Stuck on which rung something belongs to?"* | `<span class="ks3-tutor-cta">Start a question →</span>`, **no href**, 16px/700; heading "Stuck? Ask Mr Badmus AI"; generic line | b1-01's F12, unchanged. Design's anchor again points into its own page (b1-03: `#s-bench`; b1-04: `#s-rule`; b1-05: `#s-hard`) — **three for three**, so `tutor_anchor` is a real authored field, not a one-off |
| D8 | **Legal line** | **absent entirely** | fixed copyright/provenance line, 15px `--ks3-ink-muted`, `border-top 1px --ks3-rule` | second page with the slot empty. §8(c) |

#### 3.1.5 Where they agree — the shells, to the pixel

Measured at 1280 on both. Every row identical on the two pages.

| Shell | ground | border | radius | shadow | padding |
|---|---|---|---|---|---|
| `.ks3-block` | `--ks3-card` #FFFCF5 | 2px `--ks3-ink` | 28px | `5px 5px 0 #221E1B` | 30px |
| `.ks3-dark.ks3-hook` | `--ks3-ink` #221E1B | none | 30px | `6px 6px 0 #E4572E` | 32px |
| `.ks3-dark.ks3-practical` | `--ks3-ink` | none | 30px | **`6px 6px 0 #2F5CE0`** | 32px |
| `.ks3-dark.ks3-keynote` | `--ks3-ink` | none | 30px | `6px 6px 0 #FFC53D` | 32px |
| `.ks3-misconception` | `--ks3-alert-tint` #FFF3D4 | 2px `--ks3-ink` | 28px | `5px 5px 0 #221E1B` | 30px |
| `.ks3-ladder` | `--ks3-card` | 3px `--ks3-ink` | 30px | `6px 6px 0 #12A150` | 32px |
| `.ks3-layer-body` | `--ks3-stretch-tint` #F0EAFC | 2px `--ks3-stretch` #6B3FD4 | 26px | none | 26px 28px |
| `.ks3-endmatter` grid | — | — | — | — | 3 × 309.328px, gap 16px |
| `.ks3-tutor` | `--ks3-accent` | 2px `--ks3-ink` | 22px | none | 22px |
| `.ks3-option` (light) | `--ks3-ground` #FBF3E6 | 2px `--ks3-option-border` #DDCFB6 | 16px | — | 16px 18px, min-height 44px |
| `.ks3-option` (dark block) | `--ks3-dark-panel` #3E3730 | 2px `--ks3-on-dark-muted` #C6B9A7 | 16px | — | 16px 18px, 18px/600 `--ks3-on-dark` |
| `.ks3-ladder .ks3-option` | `--ks3-ground` | 2px `--ks3-option-border` | **15px** | — | **15px 17px** |
| `.ks3-footer` | `--ks3-card` | border-top 2px `--ks3-ink` | — | — | 24px |
| `h1` | — | — | — | — | 74px / 69.56px / −2.59px, Bricolage |

**That list is the substance of "where Design drew the screen, the build is right."** It is also the
answer to why the parity gate went green over 116 assertions while this page shipped: everything the
gate could see agreed, and everything it could not see was missing.

#### 3.1.6 ⭐ Component by component: what the rebuild must change

Ordered by cost. "Delete" means the generator's version is displaced by Design's, not that the
component leaves the registry.

| # | Component | Now | Must become |
|---|---|---|---|
| 1 | **Progress rail** | absent | 2 variants, 5 stages, `RAIL_SHORT` + `RAIL[].label`, `isDone` per stage, `min-width: 1340px` swap, `scroll-margin-top: 92px` on all 7 sections. §7.1 |
| 2 | **Section anchors** | none (`smt: 0px` × 21) | `id` + `scroll-margin-top: 92px` on every lesson section. Prerequisite for #1 |
| 3 | **The ZOOM instrument** | 3 × "Diagram coming soon" | one live 1800×1000 canvas + range slider + 5 segment ticks + 5-field readout. §7.2 |
| 4 | **The SORT instrument** | one `.ks3-practical` with 4 `.ks3-option`s and a prose reveal listing all 8 answers | 8 rows × 6 choices, per-row state, gated all-at-once reveal that marks each row. §7.3 |
| 5 | **The removal cases** | one `system-parts` sim + one `.ks3-option` triple + one prose reveal | 4 dark segment tabs, per-case predict gate, per-case cream reveal island with chip / headline / body / principle. §7.4 |
| 6 | **Hook commits inside the dark block** | prose hook, then a separate light `.ks3-check` | 4 dark `.ks3-option`s + gated `.ks3-reveal` inside `#s-hook`; delete the `smallest-piece` check |
| 7 | **KEY FACT box** | absent | one top-level unclassed div, `--ks3-band` / `2px --ks3-ink` / r20 / `5px 5px 0 --ks3-accent` / `18px 22px`, `mt 24px`. §7.5 |
| 8 | **Misconceptions** | 2 blocks, each with a hidden `[data-reveal]` | **1 block, 2 quote/answer pairs**, both open, split by a `2px --ks3-alert-border` rule |
| 9 | **Ladder class** | `class="ks3-block ks3-ladder"` | `class="ks3-ladder"` (D5) — or rule the other way; one value needed |
| 10 | **Keynote heading** | `<h2>` 800 sentence-case on-dark | `<p class="ks3-eyebrow">` 700 uppercase `--ks3-alert` (D4) |
| 11 | **Tutor CTA** | `<span>`, no href, 16/700 | `<a href="#s-hard">`, 18/600 (D7) |
| 12 | **Endmatter** | 3 cards, `ks4_links` as links | 4 cards incl. "Connects to"; third card is **prose** (D7/§3.1.3) |
| 13 | **Stretch layer** | nested explainer + check inside `.ks3-layer-body` | one bare `<p>` |
| 14 | **Flip cards** | 7 (3 keyword + 4 criteria-list) | **0** — Design uses none |
| 15 | **Figure placeholders** | 3 | **0** |
| 16 | **Legal line** | present | absent (D8) |
| 17 | **Nav brand** | bare chevron (MRB-197's rule) | Design's tile — ⚑ **unresolved**, D2, §8(a) |

**16 changes plus one unresolved.** Note that #1, #2, #6, #8, #10, #11, #12, #13, #15 and #16 are
all *chrome and shape* — they cost nothing but the generator learning to emit them. The expensive
items are #3, #4 and #5, and they are the three that carry the lesson.

#### 3.1.7 ⭐ MRB-202's original symptom, on this page

Mide's P0 was raised against **this lesson's** question *"What is the smallest piece you could pull
off and still call it muscle?"*, where the correct option B rendered in the accent and read as wrong.
The MRB-202 investigation concluded it is the `ks3-check` commit block behaving per R3.

**Confirmed on the live generated page**, driven at 1280. The question is at line 29 of
`mrbadmus_site/ks3/biology/cells-and-organisation/levels-of-organisation.html`,
`data-activity="smallest-piece"`, heading *"Commit before you read on. What is the smallest piece
you could pull off and still call it muscle?"*, options A / B / C with B = *"One single muscle
cell"*.

| | resting | after clicking **B** (the intended answer) | after clicking **C** (wrong) |
|---|---|---|---|
| button ground | `--ks3-ground` #FBF3E6 | **unchanged** #FBF3E6 | unchanged |
| button border | `2px --ks3-option-border` #DDCFB6 | **unchanged** #DDCFB6 | unchanged |
| `.ks3-opt-mark` badge | `--ks3-band` #F4E9D8 ground, `--ks3-ink-muted` #5F564F glyph | **`--ks3-accent` #E4572E ground, `--ks3-on-dark` #FBF3E6 glyph** | identical accent badge on C |
| drawn mark (✓/✕) | none | **none** | none |
| reveal | hidden | `--ks3-accent-tint` #FCE7DE on `2px --ks3-accent`, r18, 18px 20px, 19px | identical |

So the state carrier is **the badge alone**, it is **`--ks3-accent`**, and it is **identical whether
the student was right or wrong** — R3 rendered faithfully, exactly as MRB-202 concluded. The reason
it reads as a mark is that the accent badge sits directly above an accent-bordered reveal panel that
opens with **"One muscle cell."** — a correction. The student sees an orange badge on their answer
and a correction underneath, and infers the orange means "wrong".

**Now the check the task asked for: does Design's approved page defer, or does it correct?**

Design's nearest equivalent is `#s-hook`'s commit. Driven twice from a clean load:

- **Question**, line 90: *"Nothing is missing from the dish. So what has the stomach got?"*
- **Options** (data, 788–792): A *"More cells"* · B *"The cells arranged into layers that work
  together"* · C *"Different kinds of cell"* · D *"Nothing — the dish just needs more time"*
- **Reveal**, line 103, quoted verbatim:

  > **Keep it.** The five levels below are not five sizes of the same thing — each one can do
  > something the level under it cannot, and that is the only reason the ladder exists.

**It defers.** "Keep it" is the deferral wording the investigation predicted, and it is confirmed on
this page. The chosen option's treatment also differs from the generator's, measured after a click:

| | Design's chosen hook option | Generator's chosen `ks3-check` option |
|---|---|---|
| button ground | `--ks3-dark-panel` #3E3730 (**unchanged**) | `--ks3-ground` #FBF3E6 (**unchanged**) |
| button border | `--ks3-on-dark-muted` #C6B9A7 → **`--ks3-alert` #FFC53D** | #DDCFB6 (**unchanged**) |
| `.ks3-opt-mark` badge | #C6B9A7 → **`--ks3-alert` #FFC53D**, glyph stays `--ks3-ink` | #F4E9D8 → **`--ks3-accent` #E4572E**, glyph → `--ks3-on-dark` |
| drawn mark | none | none |
| reveal that follows | `2px --ks3-alert` on `--ks3-dark-panel`, text **"Keep it."** | `2px --ks3-accent` on `--ks3-accent-tint`, text **"One muscle cell."** |

So Design's chosen state uses **two** carriers (border + badge) and they are both `--ks3-alert`;
the generator's uses **one** (badge) and it is `--ks3-accent`. There is no accent anywhere on
Design's chosen option and no drawn mark on either. Accent and alert are different families, and
Design's alert pair does not sit under a correction — it sits under a deferral, in the same colour.
**That colour coherence is the substance of the fix**: the state mark and the reveal border are the
same token, so the pair reads as one gesture rather than as a verdict plus an answer.

⚑ **But there is a real finding, and it is significant.** The reveal is a **single static string
gated only on `hookChoice !== null`** — there is no per-option reveal and no branching. I drove the
page twice from clean loads: clicking **D**, *"Nothing — the dish just needs more time"* — which the
lesson exists to refute — produces **byte-identical** text to clicking **B**. A student who has just
said the dish only needs more time is told, in bold, **"Keep it."**

That is deferral applied where deferral is wrong. R3 forbids *marking*; it does not require
*endorsing*. Under standing law the page wins and Code renders it as delivered — but this is
**Design's call and Mide's**, not Code's, and it is the second half of MRB-202's story:

- the generator's failure mode is **"looks marked, isn't"**;
- Design's failure mode is **"reads endorsed, shouldn't be"**.

Neither is a rendering defect. Finding **F27**, §8(a) for the wording and §8(b) for whether "Keep
it" is safe on a flatly wrong option.

#### 3.1.8 Two SYSTEM realisations that share no instrument

b1-04 and b1-05 are both SYSTEM, and neither instrument appears on the other page:

| | b1-04 (the §10.1 reference screen) | b1-05 |
|---|---|---|
| Flagship | 4-specimen tuning bench + sabotage engine | 5-stop zoom + 8-item sorter + 4-case removal |
| Canvases | 2 (1800×1120 light, 1800×840 dark) | **1** (1800×1000 light) |
| Bench grid | yes, `232px 1fr` | **none** |
| Segmented control uses | 2 dark tabs | **4 dark tabs + 53 light segments** |
| Locked/veiled state | none | **none** |
| Gating style | by absence (`chainOpen = answered`) | **by absence** (`casePredictOpen = !answered`) |
| Rail stages | 4 | 5 |
| KEY FACT position | top-level orphan | top-level orphan |
| Legal line | absent | absent |

⚑ **Consequence for MRB-203's registry.** §10.1 admits one reference screen per family, and SYSTEM
covers **32 lesson slots**. If b1-04 is the family's screen, then b1-05's three instruments are not
"the SYSTEM shape" — they are three more components that any SYSTEM lesson may or may not use. The
registry cannot express "the family's screen plus a per-lesson instrument set" today. That is
**Design's structural question**, not Code's: does SYSTEM have one drawn shape or a palette?
Finding **F28**, §8(a). It is the same question in a different key for CLASSIFY, MODEL and
CONTRAST once their second lessons land.

The two pages **do** agree on the deferral gate (both hide the commit rather than veiling it), the
absence of a legal line, and the KEY FACT box's position — so those three are settling, and §8(c)
should record them as ruled by repetition.

---

### 3.2 `#s-hook` — the commit that stays in the dark block

`.ks3-block ks3-dark ks3-hook`: `--ks3-ink` #221E1B ground, no border, r30, `6px 6px 0 #E4572E`,
padding 32px, measured 960 × 652.73 at 1280.

| Part | Measured |
|---|---|
| `h2` (no class) | 38px / 39.9px, `--ks3-on-dark` #FBF3E6 |
| `.ks3-hook-prompt` | inherited body 19px |
| `.ks3-commit` | 22px, `--ks3-on-dark-body` #E7DECE |
| `.ks3-options` | 4 `.ks3-option`, 896 × 64.8 each, `padding 16px 18px`, `min-height 44px`, r16, `2px --ks3-on-dark-muted` #C6B9A7 on `--ks3-dark-panel` #3E3730, 18px/600 `--ks3-on-dark`, `display flex`, `gap 14px` |
| `.ks3-opt-mark` | 28 × 28, r9, `--ks3-on-dark-muted` #C6B9A7 ground, 15px/800, `--ks3-ink` glyph |
| **chosen** | border → `--ks3-alert` #FFC53D **and** badge ground → `--ks3-alert` #FFC53D with the glyph staying `--ks3-ink`; **button ground, radius, padding and size unchanged** (measured `rgb(62,55,48)` in both states); `aria-pressed="true"` |
| `.ks3-reveal` | `--ks3-dark-panel` ground, `2px --ks3-alert`, r18, `padding 18px 20px`, `margin-top 18px`, 19px `--ks3-on-dark`, arrives under `[data-arrive="1"]` |

**No new component.** Every value above is the registered dark-block option and the registered dark
hook. The only thing the generator cannot do is *put them there* — its hook block has
`hasOptions: 0`.

---

### 3.3 `#s-zoom` — "From a whole plant to one cell, without leaving the leaf"

The largest new component on this page: one instrument that renders **five different diagrams from
one canvas routine**, with a 5-field readout that never changes shape.

`.ks3-block` (plain), 960 × 1274.64 at 1280, `padding 30px`, `--ks3-card`, `2px --ks3-ink`, r28,
`5px 5px 0 #221E1B`. `h2` 30px / 36px.

**The canvas frame** (a straight reuse of b1-04's, which is the useful finding — one component with
a ground variant, already specified):

| Property | Measured @1280 |
|---|---|
| buffer | **1800 × 1000** |
| CSS box | **892 × 495.55** |
| device px per CSS px | **2.018** — crisp at 1× and 2×, matching b1-04's discipline |
| design space | 900 × 500, via `ctx.setTransform(2,0,0,2,0,0)` then `scale(k,k)` with `k = min(W/900, H/500)` |
| frame | `2px solid --ks3-ink`, `--ks3-r-card` 22px, `--ks3-card` ground, `overflow: hidden` |
| caption strip | **inside the frame**: `--ks3-band` #F4E9D8 ground, `border-top 2px --ks3-rule` #E0D2B9, `padding 14px 18px 18px` |
| a11y | `role="img"`, `aria-label="{{ zoomAlt }}"` from `LEVELS[].alt` |

**Two things live in the caption strip that b1-04's does not have**, and both are new:

1. **A two-value caption row** — `flex, baseline, space-between, gap 16px, wrap`: `zoomStepLabel`
   (MONO 14px/500 `.07em` uppercase `--ks3-ink-muted`, reading `"Stop N of 5"`) on the left and
   `zoomSize` (MONO **17px**/500 `--ks3-ink`, e.g. *"about 50 micrometres — 0.05 mm"*) on the right.
   The scale readout is the second-largest mono on the page and it is the only place the physical
   size appears. New component.
2. **A custom range input** — `input[type="range"].b5-zoom`, `min 0 max 4 step 1`, measured
   **856 × 40** at 1280, with an author-styled track (`height 10px`, r99, `--ks3-band` ground, `2px
   --ks3-ink`) and thumb (`30 × 30`, `border-radius 50%`, `--ks3-accent` ground, **`3px solid
   --ks3-ink`**, `margin-top −12px`), declared twice — `::-webkit-slider-*` and `::-moz-range-*`
   (lines 23–27). Its `<label for="zoom">` is `position: absolute; left: -9999px` — visually hidden,
   correctly present for a screen reader. ⚑ **This is the only range input in the whole KS3
   delivery** and it is the only place a page-local CSS class (`b5-zoom`) is required, because
   pseudo-elements cannot be set from an inline `style=`. The generator must emit it as real CSS,
   not as an inline attribute. Finding **F29**.

**The five segment ticks** are `seg(i === s.zoom, false)` — the light branch, §3.6. Widths are
content-driven (measured 105.55 / 136.39 / 78.11 / 80.08 / 59.8 for Organism / Organ system / Organ
/ Tissue / Cell), height **47.59**, in a `flex, gap 7px, wrap` row.

**The readout panel** — `margin-top 18px`, `padding 24px`, `--ks3-r-panel` 20px,
`background --ks3-inset` #F7EFE1, `2px solid --ks3-ink`; measured **896 × 330.47** at 1280:

| Field | Source | Measured |
|---|---|---|
| `levelName` | `LEVELS[].name` | **`--ks3-font-display` 800, `font-size: 30px`, lh 1.15 → 34.5px, `letter-spacing −.025em` → −0.75px** |
| `levelWhat` | `LEVELS[].what` | 19px / 30.4px, `--ks3-ink-body` #3B342E |
| divider | — | `margin-top 18px; padding-top 16px; border-top 2px --ks3-rule` |
| `levelGainLabel` | `LEVELS[].gainLabel` | MONO 14px/500, `letter-spacing .07em` → 0.98px, uppercase, **`--ks3-accent-text` #A93411** |
| `levelGain` | `LEVELS[].gain` | **20px / 31px / 600** — the only 20px/600 body type in the delivery |
| `levelHuman` | `LEVELS[].human` | 18px / 28.8px `--ks3-ink-body`, prefixed by a display-font `<strong>In you:</strong>` |

**`gainLabel` is authored per level and is not derivable.** It changes with the rung — *"What it can
do that an organ system cannot"* / *"…that a single organ cannot"* / *"…that a single tissue
cannot"* / *"…that a single cell cannot"* / *"…that its own parts cannot"*. That five-string ladder
**is the lesson**, and no template can generate it. §7.2.

**The orange "next stop" box** is a per-stop rectangle in the `boxes` array (lines 713–719), drawn
in design-space coordinates with `setLineDash([11,8])`, `lineWidth 4`, `strokeStyle '#E4572E'`, a
176×26 r8 accent tab above it, and the literal label **`NEXT STOP IS HERE`** in
`500 14px "DM Mono"` at `#FBF3E6`. `boxes[4]` is `null` — the last stop has no box, because there is
no stop below the cell. That null is semantic, not an omission.

⚠️ **The four drawing routines hard-code eleven hex colours that are not KS3 tokens**:
`#EFE3C9` (soil), `#8A6A3C` (root), `#5E7A3A` (stem), `#5E9440` / `#2F5326` (leaf fill/stroke),
`#3E6B2C` (midrib), `#EFE6D2` (epidermis), `#EFF3E4` (cell fill), `#4F7C3B` (chloroplast),
`#D9C48D` (cell wall), `#F5ECD8` / `#A2603A` (cytoplasm/membrane), `#E4EDE9` / `#9AB0A6` (vacuole),
`#7C6AA6` / `#453A69` (nucleus). Only `#221E1B`, `#C3B191`, `#E4572E`, `#FBF3E6` and `#FFFCF5`
resolve to tokens. **These are subject illustration colours, not system colours** — the same
category as b1-04's cell drawings — and the generator needs somewhere to put them. Finding **F30**;
they must not be forced into the `--ks3-*` namespace and they must not be invented per lesson.

#### 3.3.1 ⭐ Drift 3, measured — and the ruling is aimed at the wrong element

`00-delivery-drift.md` drift 3 lists b1-05 line 132 as a **statement** at `font-size: 30px` with no
clamp, and rules it to `clamp(28px, 3.9vw, 44px)`, flagging that as *"a visible change to an
approved page"*.

**Line 132 is `{{ levelName }}`.** It is not a statement panel. **b1-05 has no `#s-rule` and no
statement panel of any kind** — measured, the page's 11 children contain no unclassed
`--ks3-band` / `3px --ks3-ink` section, and the string "What settles it" does not appear. The
element the ruling would change is the **live heading of an instrument's readout**, which:

- sits inside a `2px`-bordered `--ks3-inset` panel, above four more fields;
- **changes text five times** as the student drags the slider;
- is structurally the counterpart of b1-04's `cellJob` (**21px/700**) and its `#s-tuned` readout, not
  of b1-04's `#s-rule` statement (44px display).

So the closest true analogue on the reference screen is **21px**, and the ruling would take this
element to **44px** — more than twice it.

**Here is the number Mide asked for.** Measured at all four viewports, first as authored, then with
`clamp(28px, 3.9vw, 44px)` applied live to the same element and re-measured:

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| **as authored** font-size | 30px | 30px | 30px | 30px |
| line-height | 34.5px | 34.5px | 34.5px | 34.5px (**2 lines**, box 69) |
| readout panel height | **330.47** | 330.47 | 330.47 | 600.33 |
| `#s-zoom` height | 1274.64 | 1274.64 | 1206.20 | 1463.55 |
| document height | 8614 | 8568 | 8788 | 12867 |
| **with the ruled clamp** font-size | **44px** | **44px** | **31.98px** | **28px** |
| line-height | 50.6px | 50.6px | 36.78px | 32.2px (2 lines, box 64.38) |
| readout panel height | **346.56** | **346.56** | 332.75 | 595.70 |
| `#s-zoom` height | 1290.73 | 1290.73 | 1208.48 | 1458.92 |
| document height | 8630 | 8584 | 8790 | 12862 |
| **Δ panel** | **+16.09px** | **+16.09px** | +2.28px | **−4.63px** |
| **Δ document** | **+16px** | **+16px** | +2px | **−5px** |

**The layout cost is small and safe.** Nothing wraps that did not already wrap. I measured every one
of the five level names at 44px with `measureText` in the page's own resolved Bricolage 800:

| Level name | @28px | @30px (authored) | @31.98px | @44px |
|---|---|---|---|---|
| Organism — the whole plant | 378.0 | 404.0 | 429.5 | **582.0** |
| Organ system — the shoot | 353.9 | 378.3 | 402.4 | 545.9 |
| Organ — one leaf | 226.3 | 241.9 | 257.2 | 348.9 |
| Tissue — the palisade layer | 364.9 | 390.0 | 414.7 | 562.1 |
| Cell — one palisade cell | 311.3 | 332.7 | 353.8 | 479.6 |

The available column is **844px at 1280 and 1340**, so all five stay on one line at 44px (widest is
582). At 820 the column is 656px and the widest at 31.98px is 429.5 — one line. At 390 the column is
**266px** and every name already wraps to 2 lines at 30px; the clamp's floor of 28px makes them
**smaller**, and the page gets 5px shorter.

**Nothing else on the page depends on the statement's current height.** Checked: the readout panel
is `padding`-driven with no fixed height; `#s-zoom` has no `min-height`; the canvas is
`width:100%; height:auto` with its own aspect ratio and sits *above* the panel; the rail's
`scroll-margin-top` is a constant; no `position: sticky` or `top` on the page is computed from it.
The +16px propagates to the document height and stops.

**⚖️ My finding, for Mide, stated as a finding and not a decision.**

The ruling's *layout* cost is negligible — 16px at desktop, −5px on a phone. Its *semantic* cost is
the real question, and drift 3 could not have seen it because it read the line as a statement:

- Applying it makes **an instrument's live readout heading the largest body-level type on the
  page** — 44px, larger than `#s-break`'s case headline (26px), larger than the KEY FACT (22px),
  and 8px off the ladder's `h2` (36px). The thing the eye lands on becomes *"Organism — the whole
  plant"*, a caption, rather than the key fact or the ladder.
- b1-04's structurally equivalent readout heading is **21px**.
- MRB-203's finding — *"Code's B1 pages ran smaller than Design's screens and the new block types
  never opted into the display scale"* — is about **Code's** output. This element is **Design's**,
  it is already on the display scale (Bricolage 800, `−.025em`), and it is 30px because it is a
  caption, not because anyone forgot.

So the honest reading is that **b1-05 is not a fourth data point for the statement role at all** —
it is the same kind of exclusion drift 3 already made for b1-02's formula statement. Removing it
leaves three genuine statements (46 / 44 / 40 at the cap) and `clamp(28px, 3.9vw, 44px)` remains
correct as the modal and median — **the ruling stands, unchanged, for the statement role**; it
simply should not be applied to line 132.

Three ways forward, all Mide's, none taken here:

| Option | Effect on b1-05 |
|---|---|
| **(a)** Rule line 132 out of drift 3 as a different role (a *readout heading*) and leave it at 30px | no visible change to an approved page; drift 3's ruled statement clamp unaffected |
| **(b)** Apply the ruled clamp as written | +16px at desktop, −5px at 390, and a 44px caption outranks the key fact |
| **(c)** Give readout headings their own ruled value, taking b1-04's `cellJob` (21px) and this (30px) as its two data points | a sixth drift, and it moves b1-05 *down* to 21px or b1-04 *up* to 30px |

**Recorded as F31.** I have not changed anything. Everything above was measured by setting the
property live in the browser and restoring it.

---

### 3.4 `#s-hard` — "Eight things that get put on the wrong rung"

The second new instrument, and the tallest block on the page after the ladder: `.ks3-block` (plain),
960 × **1465.39** at 1280, growing to **2035.53** once the answers are open.

**The row.** `<ul>` at `flex column, gap 11px`; each `<li>` is `padding 18px 20px`,
`--ks3-r-panel` 20px, measured 896 × 130.59:

| Row state | ground | border |
|---|---|---|
| **before reveal** (placed or not — identical) | `--ks3-card` #FFFCF5 | `2px --ks3-rule-strong` #C3B191 |
| **after reveal, right** | **`--ks3-inset` #F7EFE1** | **`2px --ks3-ink` #221E1B** |
| **after reveal, wrong** | **`--ks3-alert-tint` #FFF3D4** | **`2px --ks3-alert-border` #D9821A** |

Row content: `HARD[].item` at **20px / 700**; then a `flex, gap 7px, wrap` row of **6** choice
buttons (`RUNGS_OF`); then, once open, `HARD[].answer + '.'` in a display-font `<strong>` followed by
`HARD[].note`, at 18px / 27.9px `--ks3-ink-body`, `margin-top 12px`, inside `[data-arrive="1"]`.

**The gate.** `button.ks3-reveal-btn` "Open the answers", `--ks3-ink` ground, `2px --ks3-ink`,
`padding 14px 22px`, 17px, `--ks3-r-control` 14px, beside a MONO 15px/500 `--ks3-ink-muted` counter
reading `"N of 8 placed"`. Measured `disabled: true` with `opacity: 0.45; cursor: default` until all
8 are placed, then `disabled: false; opacity: 1; cursor: pointer`. ⚑ The disabled *appearance* is an
**authored inline style** (`hardBtnStyle`), not a `:disabled` rule — a parity probe that looks for
`button:disabled { opacity }` in the cascade will find nothing.

**48 choice buttons + 1 gate = 49 buttons in one block** (measured
`sec.querySelectorAll('button').length === 49`). That is more interactive controls than any other
block in the B1 delivery.

#### 3.4.1 The counter is broken and the label is a lie

⚑ Measured: with **zero** items placed, the counter reads **"0 of 8 placed"** and the button is
disabled — correct. But `placed` is computed as `HARD.filter(h => s.hard[h.id]).length`, and
`s.hard[id]` is set to the *label string* of the chosen rung. One of the six labels is
`'Not on the ladder'` — a truthy string — so that is fine. **The bug is elsewhere and I could not
reproduce a failure**: every path I drove incremented correctly and the button unlocked at exactly 8.
Recording as *measured correct*, with the note that the filter is truthiness-based rather than
`!== undefined`, so any future rung label that is the empty string would silently never count.
Not a defect today. No finding raised.

#### 3.4.2 ⚑ This activity marks correctness — and R3 needs re-reading against it

Driven at 1280: I placed all 8, deliberately putting row 0 ("Blood") on the correct rung and rows
1–7 on wrong ones, then pressed "Open the answers". Measured immediately after:

```
row 0 (correct):  background rgb(247,239,225)  border 2px solid rgb(34,30,27)
rows 1–7 (wrong): background rgb(255,243,212)  border 2px solid rgb(217,130,26)
```

That is `--ks3-inset` + `--ks3-ink` for right, `--ks3-alert-tint` + `--ks3-alert-border` for wrong,
applied to **eight rows at once**, plus the correct rung named in bold in every row. **This is an
activity that marks.**

Whether it breaks R3 depends on which half of R3 is load-bearing, and the two halves disagree here:

- *"Activity buttons never mark correctness"* — **satisfied.** The buttons do not change. Measured:
  the chosen choice button keeps its `seg(on)` accent-tint treatment before and after the reveal;
  the mark is on the **row container**, which is not a button.
- *"green and red must not appear on an activity button"* — **satisfied**, and comfortably: the
  marking palette is `--ks3-inset` / `--ks3-alert-tint` / `--ks3-alert-border`. There is no
  `--ks3-ok` #12A150 and no `--ks3-danger` anywhere in the block. Measured: the ladder's green
  (#12A150 / #E4F7EB) appears nowhere on this page outside `#s-ladder`.

So Design has found a third state that is neither "never marked" nor "marked green/red": **a
deferred, self-service, amber-and-neutral mark, on the row rather than the control, opened by the
student's own deliberate action after committing to all eight.** That is a genuinely good answer to
R10 (per-option feedback on activities), which has been flagged for Mide and unruled since
2026-08-09.

⚑ **It is also a rule the parity gate will now fail.** MRB-202 promoted R3 from a proxy to a direct
runtime assertion: *"presses every activity option and requires identical resolved colours and no
marking colour."* On this page, pressing every activity option and then opening the answers produces
**two different resolved grounds on sibling rows**. If the gate walks up from the pressed button to
its effective background — which layer D explicitly does, *"walking up the tree for the effective
background"* — it will see #F7EFE1 on one row and #FFF3D4 on another and it will fire. Finding
**F32**: R3's runtime assertion must be scoped to the control, or `#s-hard` must be registered as an
exception, **before** this page is built. This is a build-blocking interaction between two ruled
things and it is §8(c) — Code's to fix in the gate, not by changing the page.

---

### 3.5 `#s-break` — "Keep every cell alive. Remove the organisation."

Design's dark `ks3-practical`: `--ks3-ink` ground, `6px 6px 0 --ks3-blue` #2F5CE0, r30, padding 32px,
measured 960 × 854.14 at 1280.

**Head row:** `flex, align-items flex-end, space-between, gap 20px, wrap` — eyebrow + `<h2>` on the
left (**34px / 38.08px, `letter-spacing −.03em` → −1.02px, `--ks3-on-dark`**) and the progress line
on the right (MONO 15px/500 `--ks3-on-dark-muted`, reading `"N of 4 explored"`). Lede 19px / 1.65
`--ks3-on-dark-body`, `max-width 58ch`. **Identical head geometry to b1-04's `#s-break`** — one
component, confirmed twice.

**The case tabs are a real segmented control**, `seg(on, true)`, and drift 4's claim that *"the dark
branch is byte-identical in all four pages"* is confirmed by measurement here:

| State | ground | border | colour | geometry |
|---|---|---|---|---|
| on | `--ks3-alert` #FFC53D | `2px --ks3-alert` | `--ks3-ink` | `padding 11px 17px`, `min-height 44px`, r14 = `--ks3-r-control`, 17px/700, measured height **53.19** |
| off | `transparent` | `2px --ks3-on-dark-muted` #C6B9A7 | `--ks3-on-dark` #FBF3E6 | identical |

**Four tabs, not two** (b1-04 has two). Widths content-driven: 220.69 / 292.55 / 215.70 / 215.89 in a
`flex, gap 9px, wrap` row.

**The "what we did" panel:** `--ks3-dark-panel` #3E3730, `padding 22px 24px`, `--ks3-r-panel` 20px,
`margin-top 20px`, MONO 14px `.07em` uppercase `--ks3-on-dark-muted` label ("What we did") over
`kase.what` at **21px / 1.5 / 700** `--ks3-on-dark`, then `kase.intact` at 18px / 1.6
`--ks3-on-dark-body`. The second field is new against b1-04 — it names what is *still intact*, which
is the whole rhetorical move of the block ("nothing is killed, only the arrangement is gone").

**The predict gate** is a `.ks3-commit` + `.ks3-options` pair using the **standard dark-block
`.ks3-option`** — measured 896 × 64.8, `padding 16px 18px`, `min-height 44px`, r16,
`2px --ks3-on-dark-muted`, ground `--ks3-dark-panel`, 18px/600 `--ks3-on-dark`, `gap 14px`. **No new
component**; 3 options from `kase.predict`, and no `correct` field on any of them, so R3 holds.

**On answering, two things happen** (measured): `casePredictOpen` goes false → the gate **leaves the
DOM entirely** (measured `sec.querySelector('.ks3-option') === null`), and `caseOpen` goes true → a
cream reveal island arrives under `[data-arrive="1"]`.

⚑ **b1-01's F4 reproduces in full, and this page does NOT have b1-04's partial fix.** b1-04 added a
`yourPickLine` — *"You said: …"* — echoing the choice above the chain. Measured here:
`s.innerText.includes('You said') === false`. The student's prediction leaves the DOM with no echo,
no mark and no way to revise it. So the "You said" echo exists on **one** of the two SYSTEM pages.
One value needed. Finding **F33**.

**The reveal island** — a cream panel inside the ink block, `margin-top 22px`, `padding 24px`,
`--ks3-r-panel` 20px, `background --ks3-ground` #FBF3E6, `color --ks3-ink`:

| Part | Measured |
|---|---|
| level chip | `caseLevelStyle`, an **inline-block pill**: `padding 6px 13px`, `border-radius 999px`, `2px solid --ks3-ink`, `background --ks3-alert-tint` #FFF3D4, MONO 14px/500 `.07em` (0.98px) uppercase `--ks3-ink`. Text `"Level lost: " + kase.lost` |
| headline | `kase.headline`, **`--ks3-font-display` 800, 26px / 30.68px, `−.025em` → −0.65px** |
| body | `kase.body`, 19px / 30.4px `--ks3-ink-body` |
| principle | `margin-top 18px; padding-top 16px; border-top 2px --ks3-rule`, 19px, opening with a display-font `<strong>The principle:</strong>` |

**The pill is a new component** — a rounded-999px, ink-bordered, alert-tint status chip. Nothing
else in the delivery uses `border-radius: 999px` on a text element (the rail's track uses it on a
bar). Two registry rows: the chip and the cream-island-inside-a-dark-block.

**Design gates by absence here too**, exactly as b1-04 §3.1.5 recorded, and there is **no veil, no
blur and no disabled control anywhere on this page** (measured: the only `disabled` attributes are
the ladder's answered options and `#s-hard`'s locked gate). The generator's version of the same
teaching beat uses the **R5 veil** — measured on the generated page: canvas `filter: blur(2px)
saturate(0.65)`, an 85%-alpha `--ks3-card` cover reading *"Make your prediction first — then the lab
runs."*, and `.ks3-sim-controls` at `display: none`. Two different answers to "predict before you
see". **The page wins** — but R5 must not leave the registry, because PROCESS and INVESTIGATION
still use it.

---

### 3.6 ⭐ `seg()`'s light branch — drift 4, and its cost on this page

Source, lines 745–747:

```js
'cursor:pointer;font:inherit;font-size:16px;font-weight:700;padding:9px 13px;min-height:44px;' +
'border-radius:var(--ks3-r-control);border:2px solid ' +
  (on ? 'var(--ks3-accent)' : 'var(--ks3-option-border)') +
';background:' + (on ? 'var(--ks3-accent-tint)' : 'var(--ks3-ground)') +
';color:var(--ks3-ink);'
```

Measured at 1280 (identical at 1340, 820 and 390 — this control has no responsive behaviour):

| State | ground | border | type | geometry |
|---|---|---|---|---|
| **resting** | `--ks3-ground` #FBF3E6 | `2px --ks3-option-border` #DDCFB6 | 16px / 700 `--ks3-ink` | `padding 9px 13px`, `min-height 44px`, `--ks3-r-control` 14px, height **47.59**, width content-driven |
| **chosen** (`aria-pressed="true"`) | `--ks3-accent-tint` #FCE7DE | `2px --ks3-accent` #E4572E | unchanged | unchanged |
| spent / disabled | **do not exist** | — | — | — |

**Used 53 times on this page** — 5 zoom ticks + 8 rows × 6 rung choices — which makes b1-05 by a
wide margin the heaviest user of the light segment in the delivery. Truth of state is
`aria-pressed`. In `#s-hard` the groups are **independent single-selects, one per row**, with no
`role="radiogroup"` and no arrow-key handling; the same accessibility note b1-04 §3.3.3 raised
applies eight times over. §8(a).

**Focus ring: measured, and it took a real key event.** After a scripted `.focus()`,
`getComputedStyle` reports `outline: rgb(34,30,27) none 3px` and `element.matches(':focus-visible')
=== false` — Chrome does not match `:focus-visible` for programmatic focus, which is a trap for any
parity probe. Driving a genuine `Input.dispatchKeyEvent` Tab through CDP instead lands on the
"Organ system" tick with `:focus-visible === true` and:

```
outline: rgb(228, 87, 46) solid 3px;   /* --ks3-accent */
outline-offset: 2px;
```

Identical to b1-03's and b1-04's measurement of the KS3 focus ring; the segment adds no override.

#### 3.6.1 Drift 4's ruled value, and what adopting it costs here

Drift 4 rules **b1-06's** light branch (17px / `11px 17px` / 44px / `r-control`) on the ground that
it is the only one whose geometry matches its own dark branch. **That reasoning is confirmed on this
page by direct measurement**: this page's own dark branch is 17px / `11px 17px` / 44px / r14 and
measures **53.19px tall** (the case tabs, §3.5), against the light branch's **47.59px**. The same
helper produces two controls **5.6px different in height** on one page. Drift 4's argument is
correct and this page is the clearest evidence for it.

**The cost of adopting it, measured.** I applied the ruled declaration to all six choice buttons in
`#s-hard`'s first row, live in the browser, re-measured, and restored the authored value in the same
evaluation:

| | 1280 | 820 | 390 |
|---|---|---|---|
| choice-row inner width | 852 | **664** | 274 |
| **authored** button height | 47.59 | 47.59 | 47.59 |
| authored button widths | 59.8 · 80.08 · 78.11 · 136.39 · 105.55 · 161.11 | same | same |
| authored rows of buttons | **1** | **1** | **3** |
| authored row height | 130.59 | 130.59 | 239.78 |
| authored `#s-hard` height | 1465.39 | 1465.39 | 2490.06 |
| **ruled** button height | **53.19** | 53.19 | 53.19 |
| ruled button widths | 69.66 · 91.2 · 89.11 · 151.05 · 118.27 · 177.31 | same | same |
| ruled rows of buttons | 1 | **2** ⚑ | **4** ⚑ |
| ruled row height | 136.19 | **196.38** | **316.75** |
| ruled `#s-hard` height | 1470.98 | **1531.17** | **2567.03** |
| **Δ section** | **+5.59px** | **+65.78px** | **+76.97px** |
| **Δ document** | +6px | **+66px** | **+77px** |

⚑ **The wrap is real, and it happens at 820.** The six buttons total 621.04px of width plus 35px of
gap = 656.04 in a 664px row — **8px of headroom**. At the ruled size they total 696.60 + 35 = 731.60
and the sixth ("Not on the ladder") drops to a second line, on **every one of the eight rows**. The
same thing costs a fourth line at 390.

At 1280 the ruling is free (+5.59px). At the width a school laptop actually renders, it costs 66px
and turns eight one-line control rows into eight two-line ones.

**The ruling is still right** — a control must not change size when it changes ground, and this
page's own 5.6px mismatch is the clearest evidence for that in the delivery. But its cost lands
almost entirely on this page and almost entirely below 1280, and Mide should see the 820 column
before it is applied.

---

### 3.7 `#s-think` — one misconception block, two misconceptions

`.ks3-block ks3-misconception`: `--ks3-alert-tint` #FFF3D4, `2px --ks3-ink`, r28, `5px 5px 0
#221E1B`, padding 30px, 960 × 516.31. Shape confirmed identical to b1-03 §3.6 and b1-04 §3.6, with
**two quote/answer pairs inside one block**, separated by an inline divider:
`margin-top 22px; padding-top 20px; border-top 2px solid var(--ks3-alert-border)` (#D9821A).

**The 19/22 split reproduces exactly.** The first `.ks3-mis-quote` measures **19px / 700**
(`margin-top 15px`) and the second **22px / 700** (`margin-top: 0` inline), for the same
CSS-specificity reason b1-04 §3.6 identified — the second is inside a nested `<div>` so
`:first-of-type` no longer applies. **Third page, same split, still not authored.** b1-04 flagged it
as A2; this confirms it is systematic rather than a one-page accident, which makes it more likely to
be a stylesheet defect than a design choice. §8(a).

The two misconceptions, both **static markup** (217–229), not data:

1. *"An organ is just a bigger tissue."* — the CELL-family misconception this lesson exists to kill.
2. *"Blood can't be a tissue — it's a liquid."* — which the generator's page also carries, in
   different words, and which ladder rung 1 tests.

### 3.8 The KEY FACT box

One box, top-level, unclassed, `margin-top: 24px`, measured at 1280:

| Property | Value | Token |
|---|---|---|
| ground | #F4E9D8 | **`--ks3-band`** — **drift 5 confirmed**, this page is one of the five |
| border | 2px solid #221E1B | `--ks3-ink` |
| radius | 20px | `--ks3-r-panel` |
| shadow | `5px 5px 0 #E4572E` | **`--ks3-accent`** |
| padding | 18px 22px | new |
| box | 960 × 127.17 | full lesson width |
| label | "Key fact", MONO 13px/500, `letter-spacing .09em` (1.17px), uppercase, `--ks3-accent-text` #A93411 | |
| body | display 700, **22px / 29.7px**, `−.015em` (−0.33px), `--ks3-ink` | |

**Byte-identical to b1-04's box on every measured property including the 24px margin.** Two pages
now agree exactly, which is the strongest evidence yet for F19's answer. Drift 5's caution holds:
no badge, no icon, and the 5px accent shadow is what distinguishes it from a chosen-wrong ladder
option (same `--ks3-band` ground, same `2px --ks3-ink` border, **no shadow**). Worth pinning as an
assertion.

### 3.9 The ladder, the stretch layer and the endmatter

**`#s-ladder`** is `class="ks3-ladder"` (single class, hence D5's 57.6px heading), 960 × 1815.83,
`--ks3-card` on `3px --ks3-ink`, r30, `6px 6px 0 #12A150`, padding 32px, with the standard 4-rung
shape: 2 page-marked rungs from `RUNGS`, 2 self-marked from `SELF_RUNGS`, `.ks3-retry-wrap`. Every
state driven and measured; every one matches the registered components exactly:

| State | ground | border | text | mark |
|---|---|---|---|---|
| resting | `--ks3-ground` #FBF3E6 | `2px --ks3-option-border` #DDCFB6 | `--ks3-ink` | letter |
| CHOSEN-CORRECT (`.is-correct`) | **#E4F7EB** = `--ks3-ok-tint` | `2px #12A150` = `--ks3-ok` | `--ks3-ink` | drawn ✓ |
| CHOSEN-WRONG (`.is-wrong`) | **`--ks3-band` #F4E9D8** | `2px --ks3-ink` | `--ks3-ink` | drawn ✕ |
| SPENT (`.is-spent`) | **`--ks3-row-dim` #FBF6EC** | `2px #EBDFCB` | **#6E655D** | none |
| all answered | `disabled: true` | | | |

Ladder options are r15 / `padding 15px 17px` — the ladder-specific override, not the 16px/`16px 18px`
of a plain option. Feedback measured on a wrong answer: `.ks3-feedback.is-wrong` = `--ks3-band` on
`2px --ks3-ink`, r15, `padding 14px 18px`, 19px, reading *"Not this one."* followed by that option's
authored `correction`. On a right answer `feedbackText` is `''` — "Correct." with no trailing prose.
Ticks: 4 per self-rung; tally `"0 of 4 ticked — not yet."` on `--ks3-band` `--ks3-ink-body`,
flipping to `"All 4 ticked — rung met."` with `.is-met`. Score `"You got N of 4."` +
`"You marked rungs 3 and 4 yourself."`

**F23 reproduces.** `onRetry` is `{answers:{}, checked:{}, ticks:{}}` — it clears rungs 1 and 2 as
well as the self-marked ones — while the note says *"Clears the ticks on rungs 3 and 4 and keeps
what you wrote."* Same copy/behaviour mismatch b1-04 raised. Second page, identical wording and
identical behaviour, so it is systematic. Under standing law the page wins and the generator
reproduces both.

**`.ks3-layer`** — one bare `<p>` in a `.ks3-layer-body` (`--ks3-stretch-tint` #F0EAFC,
`2px --ks3-stretch` #6B3FD4, r26, `padding 26px 28px`). The generator's equivalent nests two blocks
inside it (b1-03's D10, reproduced a third time).

**`.ks3-endmatter`** — 4 cards, `3 × 309.328px` grid, gap 16px; heads "Before this lesson" ·
"Connects to" · "At GCSE this becomes" · "Ask Mr Badmus AI". Third card is **prose**
(`thirdIsProse: true`). Tutor CTA is a live `<a href="#s-hard">` at 18px/600, r12, `--ks3-card` on
`--ks3-accent-text`.

---

## 4. Interactive behaviours

Eleven, each with its trigger. All measured live unless marked.

| # | Behaviour | Trigger | Effect |
|---|---|---|---|
| B1 | **Hook commit** | click one of 4 dark `.ks3-option` | `hookChoice` set; option border → `--ks3-alert`; `.ks3-reveal` arrives under `[data-arrive]`; rail stage 1 ticks. **Never marked** (R3) and **never branched** (F27) |
| B2 | **Zoom by slider** | drag `input#zoom` | `zoom` set, `seenZoom[v]` set; canvas repaints to a different routine; all 5 readout fields swap; caption + size swap; the tick row's pressed state moves |
| B3 | **Zoom by tick** | click one of 5 segments | identical to B2 |
| B4 | **Rail stage 2** | 5 distinct stops seen | ZOOM chip → accent + tick |
| B5 | **Place an item** | click one of 6 choices in one of 8 rows | `hard[id]` set to the label string; that row's pressed state moves; counter increments; the gate unlocks at 8. **Freely revisable** — the page says so: *"change your mind as often as you like, nothing is marked"* |
| B6 | **Open the answers** | click the (unlocked) gate | `hardOpen` true; all 8 rows restyle right/wrong **at once**; 8 answer paragraphs arrive under `[data-arrive]`; rail stage 3 ticks. **One-way** — no close, no retry |
| B7 | **Case select** | click one of 4 dark segments | `caseId` set; the "what we did" panel swaps; if that case was already predicted its reveal returns, otherwise the predict gate returns |
| B8 | **Predict** | click one of 3 dark `.ks3-option` | `casePick[caseId]` set; gate leaves the DOM (**F4, no echo — F33**); cream island arrives; counter increments |
| B9 | **Rail stage 4** | 4 distinct cases predicted | BREAK chip → accent + tick, and the block's own counter agrees ("4 of 4 explored") |
| B10 | **Ladder mark / self-mark / retry** | as b1-04 B7–B9 | identical; **first click locks** (`if (st.answers[r.id] !== null && !== undefined) return null`) |
| B11 | **Rail navigation and progress** | click a side-rail link; scroll | `location.hash` set, `scroll-behavior: auto`; `IntersectionObserver` `rootMargin: '-45% 0px -50% 0px'` on the 5 rail sections drives the top bar's count, label and fill — **not** completion (F2) |

**Two behaviours the page does *not* have**, both design statements: **no locked/veiled instrument**
(§3.5) and **no revision of a prediction or a hook choice** once made. `#s-hard`'s placements are the
one thing on the page that is freely revisable, and the page says so in words.

**Settle trap:** as b1-02 recorded, the DC runtime hydrates asynchronously and repaints the canvas
on `document.fonts.ready` (line 562). Every measurement above used ≥0.35s settle after each click,
and the `#s-break` drive used 0.5s per step. Probes that read immediately catch the pre-hydration
DOM.

---

### 4.1 ⭐ `wireSystemParts` versus Design's approved page

The task asks whether the repo's `system-parts` instrument (built under MRB-198, `shared/ks3.js`
lines 2246–2570+) matches what Design drew. **Measured answer: Design's approved b1-05 does not
contain a `system-parts` instrument, or a dependency graph, or a part selector, in any form.**

Measured on the reference page: no `<select>` anywhere; no `[data-parts]`; no `.ks3-sim`; one canvas
and it draws a plant. Measured on the generated page: one `.ks3-sim[data-sim="system-parts"]` with
an 8-part payload, inside `.ks3-practical[data-activity="break-the-chain"]`.

So this is not a divergence between two implementations of one component. **It is one component that
Design replaced with a different one.** Here is the comparison, precisely, without reconciling.

#### 4.1.1 The parts list and the `needs` edges

The generated page's `data-parts` (line 49 of the generated file), 8 parts:

| id | name | job | needs | `one_of_many` |
|---|---|---|---|---|
| `muscle-cell` | Muscle cell | Shortens when it is told to | — | **true** |
| `gland-cell` | Gland cell | Makes acid and digestive juice | — | **true** |
| `muscle-tissue` | Muscle tissue | Squeezes and churns the food | `muscle-cell` | — |
| `gland-tissue` | Glandular tissue | Releases the juice into the stomach | `gland-cell` | — |
| `lining` | Lining tissue | Protects the stomach from its own acid | — | — |
| `stomach` | Stomach (organ) | Breaks food down, physically and chemically | `muscle-tissue`, `gland-tissue`, `lining` | — |
| `digestive` | Digestive system | Gets food into the blood | `stomach` | — |
| `organism` | The organism | Stays supplied with everything it needs | `digestive` | — |

Design's `#s-break` has **no parts and no edges**. Its four cases are authored prose:

| case | what is removed | level lost |
|---|---|---|
| `dish` | every cell separated from every other | **Tissue and above** |
| `nomuscle` | the stomach's muscle tissue only | (not stated as a level) |
| `leafcells` | a leaf's cells shuffled | — |
| `detached` | a leaf cut off the plant | — |

Only **one** of the four (`nomuscle`) is the same experiment as the sim's headline case.

#### 4.1.2 MRB-198's asserted cascade — verified, and it holds

MRB-198's audit asserts that switching off muscle tissue must stop the stomach, then the digestive
system, then the organism, in order, and that the readout must also carry what still works. I drove
the generated sim after unveiling it (answering the predict gate first, then setting the `<select>`
and dispatching `change`, 3.2s settle per part to let all waves land). Verbatim readouts:

> **muscle-tissue** — "The muscle tissue is off. Its job — squeezes and churns the food — is not
> being done. Stopped, in the order the failure spread: **Stomach (organ), then Digestive system,
> then The organism.** Still working: Muscle cell, Gland cell, Glandular tissue, Lining tissue."

> **muscle-cell** — "The muscle cell is off. Its job — shortens when it is told to — is not being
> done. **Almost nothing else happens: it is one of thousands doing that job, and the rest cover for
> it. Everything else still works.**"

> **stomach** — "…Stopped, in the order the failure spread: Digestive system, then The organism.
> Still working: Muscle cell, Gland cell, Muscle tissue, Glandular tissue, Lining tissue."

> **lining** — "…Stopped, in the order the failure spread: Stomach (organ), then Digestive system,
> then The organism. Still working: Muscle cell, Gland cell, Muscle tissue, Glandular tissue."

> **digestive** — "…Stopped, in the order the failure spread: The organism. Still working: Muscle
> cell, Gland cell, Muscle tissue, Glandular tissue, Lining tissue, Stomach (organ)."

**Every one of MRB-198's assertions is satisfied.** The cascade order is exactly
stomach → digestive → organism; `one_of_many` absorbs at wave 0 for both cell-level parts and the
readout says so in the lesson's own language; and the "Still working:" clause is present on every
non-absorbed case and correctly excludes the stopped set. The animation is wave-by-wave at
`WAVE_MS = 550` with a travelling dashed edge, and `REDUCED` jumps to the end state (R6). **The
instrument is correct and does what its audit says.**

#### 4.1.3 Where the two diverge — and it is not a preference

| | `wireSystemParts` (repo) | Design's `#s-break` (approved) |
|---|---|---|
| Model | a **derived** dependency graph — rows from longest-chain-up, cascade from `needs` closure | **four authored cases**, each a hand-written chain of prose |
| Scale coverage | 5 levels, one worked chain (human digestive) | 4 cases spanning **both** a human stomach and a plant leaf |
| `one_of_many` | a data flag that absorbs the failure at wave 0 | ⚑ **no equivalent, and the *opposite* teaching point**: case `dish` removes *every* cell's arrangement at once, and case `nomuscle` removes a whole tissue. The sim's best moment — "switch off one cell and almost nothing happens" — has **no counterpart on the approved page** |
| Failure direction | strictly **upward** (a part stops → its dependents stop) | **upward and sideways**: `leafcells` fails because *arrangement* is lost with no part missing at all, which the graph cannot represent |
| Readout | one generated sentence, `job` + ordered stops + still-working list | four authored fields per case: level-lost chip, 26px headline, body, and a `principle` line |
| Marking | never | never (R3 respected on both) |
| Gating | **R5 veil** — blur + 85% cover + hidden controls | **absence** — the whole reveal is out of the DOM until predicted |
| Control | one `<select>` "Switch one part off" (R15: a selector, never a slider) | four segmented tabs |
| Canvas | 560×220 buffer at **896×354.42 CSS → 0.625 device px per CSS px** (upscaled ~1.6×, measurably not retina) | no canvas in this block at all |

**Three divergences are load-bearing and none of them is a matter of taste:**

1. **`one_of_many` has no home on the approved page.** It is the single most valuable idea in the
   sim — a redundant part fails and the system absorbs it — and Design's four cases never make that
   point. Under standing law Code **may add** behaviour inside a component Design has drawn, but
   `one_of_many` is not inside anything Design drew here; it belongs to a component Design replaced.
   **It cannot be carried across without inventing a fifth case**, which the law forbids.
   This is a real content loss and it is **Mide's call**, not Code's. §8(b).
2. **`leafcells` cannot be expressed as a graph.** Nothing is removed; the parts are shuffled. A
   `needs`-closure model has no way to say "every part present, arrangement gone". So the engine
   cannot be retargeted at Design's content even if we wanted to.
3. **The canvas resolution.** Design's one canvas runs a **1800×1000 buffer at 892 CSS px
   (2.018×)**; the sim runs **560×220 at 896 CSS px (0.625×)**. If any part of `wireSystemParts`
   survives into another lesson, that ratio is a defect on its own and worth fixing where it lives.
   Finding **F34**, independent of this rebuild.

**Recommendation, stated as a finding rather than taken:** `wireSystemParts` is correct, audited and
used by at least one other lesson's data shape. It should not be deleted from `shared/ks3.js` on
account of this page. But **on this page it is displaced**, and the `system-parts` sim kind, the
`data-parts` payload and its 8 authored `job` strings all leave this lesson with it.

---

## 5. Schema gaps against `docs/ks3/architecture.md` §4.8

§4.8 is authoritative: *"Fields not listed here do not exist without an amendment to this
document."*

### 5.1 Already covered by §4.8

`slug` · `title` · `discipline` · `unit` · `family` (SYSTEM) · `big_question` · `phenomenon` (the
hook prose) · `misconceptions` (both of `#s-think`'s) · `ladder` (all four rungs, criteria, retry) ·
`key_note` · `review_state` (drives `.ks3-review-flag`) · `requires` ("Before this lesson") ·
`references` ("Connects to") · `ks4_links` ("At GCSE") · `stretch` (the layer).

### 5.2 Gaps — 12, of which 5 are new to this page

| # | Gap | Needed by | New here? |
|---|---|---|---|
| **G1** | `rail` — `{anchor, short, label, done_when}` **plus `threshold`** | §2.4 | shared (b1-01); threshold shared with b1-04 |
| **G2** | `anchor` / `scroll-margin-top` on every block — §4.8 has no per-block id | §2.3 | shared |
| **G3** | `key_fact` — first-class, with a **position** | §3.8 | shared; **b1-04 and b1-05 now agree on the position**, so F19 has a majority |
| **G4** | **`zoom_ladder`** — the `#s-zoom` instrument: an ordered list of levels, each `{tick, name, size, what, gain_label, gain, human, alt, drawing, next_box}` | §3.3 | **new** |
| **G5** | **`drawing`** — §4.8's `figures` carries `{id, kind, caption, status}` for a *pending slot*; this page needs a **live canvas kind** with a named routine per level, a design-space box, and a per-level `next_box` rectangle | §3.3 | **new** (b1-04 raised the live-canvas half; the per-step `boxes` array is new) |
| **G6** | **`illustration_palette`** — the 15 non-token hex values the drawing routines use | §3.3, F30 | **new** |
| **G7** | **`sort_task`** — the `#s-hard` instrument: `{choices: [6], items: [{id, item, answer, note}], gate_label, counter_template}`, with the marking rule | §3.4 | **new** |
| **G8** | **`removal_cases`** — the `#s-break` instrument: a list of `{id, label, what, intact, lost, predict: [3], headline, body, principle}` | §3.5 | **new** |
| **G9** | `legal` — three answers for one slot (copyright / safety line / **nothing, ×2**) | §1.4, D8 | shared (b1-03), value settling toward absent |
| **G10** | `tutor_prompt` + `tutor_anchor` — Design authors both the line and an in-page href, on **three of three** pages | §3.9 | shared (b1-01 F12), now strongly evidenced |
| **G11** | `hook_options` — 4 unmarked commitment options + **one** gated reveal | §3.2, F27 | shared (b1-04), and the single-reveal shape is confirmed |
| **G12** | `slider_control` — the `b5-zoom` range input needs real CSS (pseudo-elements are unreachable from inline styles) | §3.3, F29 | **new** |

**`activities` cannot carry G4, G7 or G8.** §5.5's activity families describe marked or self-marked
tasks. The zoom is neither; the sorter is a fourth thing (deferred self-service marking, §3.4.2);
the removal cases are a predict-then-read instrument. §4.8 has no field for an instrument with its
own content payload — the same conclusion b1-04 §5.2 reached, now from three more directions.

---

## 6. Measurements

### 6.1 Traces to a token

All **35** `--ks3-*` custom properties probed on `.rd[data-mode="ks3"]` resolved to their
`shared/ks3.css` values, exactly:

| Token | Value | Used by |
|---|---|---|
| `--ks3-ground` | #FBF3E6 | seg resting, `#s-break`'s cream island, page ground |
| `--ks3-card` | #FFFCF5 | canvas frame, `#s-hard` rows, rail chips |
| `--ks3-band` | #F4E9D8 | KEY FACT, caption strip, slider track, ladder wrong |
| `--ks3-inset` | #F7EFE1 | zoom readout panel, **`#s-hard` right row** |
| `--ks3-ink` | #221E1B | every 2–3px border, dark grounds, slider thumb border |
| `--ks3-ink-body` | #3B342E | body prose, answer notes |
| `--ks3-ink-muted` | #5F564F | MONO captions, counters |
| `--ks3-ink-ghost` | #9A8F86 | future rail chip |
| `--ks3-accent` | #E4572E | chosen seg border, done chip, KEY FACT shadow, slider thumb, next-stop box |
| `--ks3-accent-text` | #A93411 | gain label, KEY FACT label, tutor CTA |
| `--ks3-accent-tint` | #FCE7DE | chosen seg ground, current-chip halo |
| `--ks3-alert` | #FFC53D | dark tab on, hook chosen border, hook reveal border, keynote shadow |
| `--ks3-alert-tint` | #FFF3D4 | misconception ground, **`#s-hard` wrong row**, level-lost pill |
| `--ks3-alert-border` | #D9821A | `#s-think` divider, **`#s-hard` wrong row border** |
| `--ks3-on-dark` / `-body` / `-muted` | #FBF3E6 / #E7DECE / #C6B9A7 | dark blocks |
| `--ks3-dark-panel` | #3E3730 | "what we did" panel, dark options, hook reveal |
| `--ks3-rule` / `-strong` | #E0D2B9 / #C3B191 | caption borders, `#s-hard` resting row border |
| `--ks3-option-border` | #DDCFB6 | seg resting border, ladder option |
| `--ks3-blue` | #2F5CE0 | `#s-break`'s shadow |
| `--ks3-stretch` / `-tint` | #6B3FD4 / #F0EAFC | layer |
| `--ks3-row-dim` | #FBF6EC | SPENT ladder option |
| `--ks3-ok` / `-tint` | #12A150 / #E4F7EB | ladder correct, ladder shadow — **and nowhere else on the page** |
| `--ks3-r-block/card/panel/option/control` | 28 / 22 / 20 / 16 / 14 px | all |
| `--ks3-tap` | 44px | segs, options |
| `--ks3-page` / `--ks3-wide` | 1320px / 60rem | page shell |

### 6.2 New measurements — px values not expressed as a token

| Value | Where | Note |
|---|---|---|
| `1340px` | rail swap | shared across all pages |
| `92px` scroll-margin | all 7 anchors | shared |
| `104px` rail width, `150px` top, `calc(50% − 632px)` | side rail | shared; measured **x 38** at 1340, 48px gutter |
| `416.94` rail height (5 nodes) | side rail | **identical to b1-03's 5-node rail** — assertable |
| `96 / 8 / 99px` track, `92px` inner | top bar | shared |
| `20 / 40 / 60 / 80 / 100 %` | top-bar fill | 5-stage arithmetic |
| **`1800 × 1000` buffer, 900×500 design space, `setTransform(2,…)`, k = min(W/900,H/500)** | zoom canvas | new; **2.018 device px per CSS px** |
| **`14px 18px 18px` caption strip padding** | zoom frame | new (b1-04's is `11px 16px`) — ⚑ a sixth drift candidate |
| **MONO `17px`** | `zoomSize` | new; the largest mono in the delivery |
| **`10px` track / `30×30` thumb / `3px` thumb border / `40px` input height / `−12px` thumb margin** | `b5-zoom` | new, and the only range input in KS3 |
| **`24px` panel padding, `18px` margin-top** | zoom readout | new (b1-04's readout is `22px 24px` / `16px`) — ⚑ same drift candidate |
| **`30px` / lh 1.15 / `−.025em`** | `levelName` | **drift 3's disputed element, §3.3.1** |
| **`20px` / lh 1.55 / 600** | `levelGain` | new |
| **`18px 20px` padding, `11px` gap, r20** | `#s-hard` rows | new |
| **`20px`/700 item, `7px` chip gap** | `#s-hard` | new |
| **`14px 22px` padding, 17px, r14, opacity .45** | "Open the answers" | new |
| **`16px` / `9px 13px` / 47.59 height** | light seg | drift 4's third variant |
| **`26px` / lh 1.18 / `−.025em`** | case headline | new |
| **`6px 13px`, `border-radius 999px`** | level-lost pill | new — the only 999px text chip |
| **`24px` padding, r20** | `#s-break` cream island | new |
| `18px 22px` padding, `5px 5px 0` shadow, `24px` margin-top | KEY FACT | **identical to b1-04** |
| `54ch / 58ch` | prose measures | new |
| `0.34s` `b5-arrive`, translateY 6px | arrival animation | **`b5-` prefix, not `b4-`** — the keyframe name is per-page and must be generated, not copied |
| **15 non-token hex values** | drawing routines | F30 |

### 6.3 Not measured

1. **The `railLabels` prop.** Declared in `data-props` (boolean, default true, section "Progress
   rail") and **never read anywhere in the script** — a grep of the whole file finds it only in the
   declaration. Dead on this page exactly as on b1-04. Whether a labels-off rail was intended is
   unknown and untestable. §8(a).
2. **`startZoom: 'cell'`.** The prop is an enum (`organism` | `cell`) and I did not override the
   `data-props` payload; the seeding at lines 536–537 was read from source, not driven.
3. **`prefers-reduced-motion: reduce`.** The rule (line 22) was read from source and enumerated from
   `document.styleSheets`, but I did not run the page under the emulated media feature. The
   `[data-arrive]` animations on the hook reveal, the eight answer paragraphs and the case island
   are therefore verified as *authored*, not as *suppressed*.
4. **The canvas pixels.** I measured the buffer, the CSS box, the transform and the design space,
   and read all four drawing routines from source, but I did not screenshot or pixel-diff the five
   drawings. Whether the `boxes` rectangles actually land on the feature they point at is a visual
   check I did not run.
5. **`WAVE_MS` timing on the generated sim.** I settled 3.2s per part, which is comfortably past the
   4 × 550ms the deepest cascade needs, so the readouts in §4.1.2 are end-state readouts. I did not
   measure the intermediate waves.

Everything else flagged as unmeasured in the first pass has since been measured: drift 4's wrap cost
at all three widths (§3.6.1), Design's chosen-badge colour (§3.1.7), and all 53 `ks3-*` classes
against `shared/ks3.css` (§1.5, zero misses).

---

## 7. How to generate each new component from data

Four new components plus two small ones, in descending cost.

### 7.1 The progress rail

Identical to b1-01 §2.6 / b1-03 §2.4 / b1-04 §7.1. Requires G1 and G2. Emit the two `<nav>`
variants, the two media rules, and `scroll-margin-top: 92px` on **every** id-bearing section.
`done_when` must support a threshold, and §2.1's F25 argues it must name the *work*, not a
downstream flag.

### 7.2 `zoom_ladder` — `#s-zoom`

```python
{"type": "zoom-ladder",
 "levels": [                                   # ordered top → bottom, 5 here
   {"tick": "Organism", "name": "Organism — the whole plant",
    "size": "about 30 cm tall",
    "what": "...",
    "gain_label": "What it can do that an organ system cannot",   # authored per level
    "gain": "...",
    "human": "You. Roughly thirty trillion cells, and one thing.",
    "alt": "...",
    "drawing": "plant",                        # names a routine, G5
    "next_box": [180, 56, 540, 306]},          # design-space rect, null on the last
   ...
 ],
 "start": "organism",                          # the `startZoom` prop
 "slider": True}
```

Renders: the framed canvas with its two-value caption row; the `b5-zoom` range input **with real
CSS** (G12); the segment tick row; the 5-field readout panel. `next_box` drives the dashed accent
rectangle and its `NEXT STOP IS HERE` tab; `null` suppresses both. **Nothing here can be derived** —
`gain_label` in particular changes with the rung and *is* the lesson.

### 7.3 `sort_task` — `#s-hard`

```python
{"type": "sort-task",
 "choices": ["Cell", "Tissue", "Organ", "Organ system", "Organism", "Not on the ladder"],
 "items": [{"id": "blood", "item": "Blood", "answer": "Tissue", "note": "..."}, ...],   # 8
 "gate_label": "Open the answers",
 "counter": "{n} of {total} placed",
 "marks_on_reveal": True}                      # ⚑ see F32 before building
```

Renders: a `flex column, gap 11px` list of rows; per row the item at 20px/700 and a wrapping row of
light segments; the gate button with its authored disabled style; on reveal, all rows restyle at
once and each grows its answer paragraph. **Three new registry rows**: row resting, row right, row
wrong. **F32 must be answered first** — R3's runtime assertion currently fails this component.

### 7.4 `removal_cases` — `#s-break`

```python
{"type": "removal-cases",
 "cases": [
   {"id": "dish", "label": "Stomach cells in a dish",
    "what": "...", "intact": "...", "lost": "Tissue and above",
    "predict": ["...", "...", "..."],          # 3, never marked (R3)
    "headline": "They keep working. Nothing gets digested.",
    "body": "...", "principle": "..."},
   ...
 ]}
```

Renders: the head row with its live counter; the dark segmented control (the **existing** dark
segment, drift 4's ruled geometry); the "what we did" panel with its two fields; the predict gate
built from the **existing** dark `.ks3-option`; and, once answered, the cream island with pill,
headline, body and principle inside `[data-arrive]`. **Two new registry rows**: the 999px level-lost
pill, and the cream-island-inside-a-dark-block. `lost` is optional — only one of the four cases
states a level, and the pill still renders (`"Level lost: undefined"` would be wrong; the generator
must omit the pill when `lost` is unset). ⚠️ **That omission behaviour is not in the delivery** —
all four cases here carry `lost`. It is Code's decision, §8(c).

### 7.5 The two smaller ones

**KEY FACT box** (G3): `--ks3-band` ground, `2px --ks3-ink`, `--ks3-r-panel` 20px, `5px 5px 0
--ks3-accent`, `padding 18px 22px`, `margin-top 24px`, MONO 13px `.09em` `--ks3-accent-text` label +
display-700 22px/1.35 body, at full lesson width, as a **top-level sibling after the misconception
block**. Two pages now specify this identically; it is ready to build.

**The light segment** (drift 4): one component, one geometry, both grounds. Register resting and
chosen as two rows. Adopt the ruled 17px/`11px 17px` only after §6.3(4) is measured.

---

## 8. Ambiguities and findings

Separated by whose call each is.

### (a) Ambiguity for Design — 8

| # | Question |
|---|---|
| A1 | **⭐ The hook reveal does not branch.** One static string, gated on *any* choice, opening with **"Keep it."** — including for *"Nothing — the dish just needs more time"*. Is one reveal intended for four options, or should it branch? (§3.1.7, F27) |
| A2 | **⭐ Does SYSTEM have one drawn shape or a palette of instruments?** b1-04 and b1-05 are both SYSTEM and share no instrument. §10.1 admits one reference screen per family and 32 slots inherit it. (§3.1.8, F28) |
| A3 | **`#s-hard` marks correctness on an activity.** Deferred, amber, on the row not the button, opened by the student — a fourth state R3 does not describe and R10 has not ruled. Intended? (§3.4.2) |
| A4 | **`#s-think`'s two quote sizes.** 19px then 22px, on three of three pages, falling out of CSS specificity rather than authorship. Which is right? (§3.7) |
| A5 | **`railLabels`** is a declared prop nothing reads, on two pages now. Was a labels-off rail intended? (§6.3) |
| A6 | **R4's flip-card clause** still cannot be arbitrated: **three** reference screens, zero flip cards. (§3.1.3) |
| A7 | **The nav brand mark.** Design's 34×34 accent tile with an inverted cream chevron, on three reference screens now, against MRB-197's ruled bare chevron. (D2) |
| A8 | **The zoom readout panel's metrics differ from b1-04's tuning readout** — `24px` / `mt 18px` here against `22px 24px` / `mt 16px` there, and the caption strip is `14px 18px 18px` against `11px 16px`. A sixth drift, not in `00-delivery-drift.md`, and one value is needed. |
| A9 | **⭐ Drift 4's ruled segment costs 66px and a line-wrap at 820.** The ruling is right on its own terms (this page's own light/dark mismatch is the evidence for it) but its cost is concentrated here and below 1280: at 820 all eight `#s-hard` rows go from one line of six controls to two. Accept the taller layout, or ask Design for a narrower sixth label ("Not on the ladder" is 177.31px at the ruled size)? (§3.6.1) |

### (b) Science or content — Mide's, and only Mide's — 4

| # | Question |
|---|---|
| S1 | **⭐ Drift 3's ruling, applied to line 132.** The element is an instrument's live readout heading, not a statement panel; b1-05 has no statement panel. The ruled clamp costs **+16px** at 1280/1340, **+2px** at 820 and **−5px** at 390, and makes a 44px caption the largest body-level type on the page, above a 22px key fact. Three options in §3.3.1. (F31) |
| S2 | **⭐ `one_of_many` has no home on Design's page.** The generator's best teaching moment — switch off one cell and the tissue absorbs it — has no counterpart in Design's four cases, and Code may not invent a fifth. Is that loss acceptable? (§4.1.3) |
| S3 | **Is "Keep it." safe on a wrong answer?** A student who has just said the dish needs more time is told to keep that. (§3.1.7) |
| S4 | **Does any of the generator's current lesson survive?** The two pages teach different lessons with different examples (plant vs human), different misconceptions and a different big question. Design's 2,630 words displace ~1,900 words of examiner-unreviewed draft. (§3.1.2) |

### (c) Code's to decide — 5

| # | Decision |
|---|---|
| C1 | **⭐ R3's runtime assertion must be scoped before this page builds.** MRB-202 made R3 a direct assertion that presses every activity option and requires identical resolved colours. `#s-hard` will fail it legitimately. Scope the assertion to the control, or register `#s-hard` as a declared exception with its own contrast pairs. **Build-blocking.** (F32) |
| C2 | **`done_when` gets a `threshold`** (b1-04 C2) **and should name the work, not a downstream flag** — `#s-hard`'s stage watches `hardOpen`, not the 8 placements. (F25) |
| C3 | **The legal slot** needs one rule admitting "absent" as a value. Two of four pages are now absent; recommendation unchanged from b1-04 C3 — make the field optional and emit nothing when unset. (G9) |
| C4 | **The `next_box` and `lost` fields are optional and their omission is meaningful.** `boxes[4] === null` suppresses the next-stop rectangle; a case with no `lost` must suppress the pill rather than render "undefined". Neither omission appears in the delivery for `lost`; Code chooses and states it. (§7.4) |
| C5 | **Illustration colours need a home outside the `--ks3-*` namespace** (G6, F30). They are subject artwork, not system colour, and must not be re-invented per lesson. |

### Findings raised on this page

| # | Finding |
|---|---|
| **F25** | Rail stage 3's `done_when` watches a button (`hardOpen`), not the work (8 placements). Transitively correct today, brittle by construction. |
| **F26** | `id="zoom"` is a bare, un-namespaced form-control id inside a lesson, against the generator's `ks3-<thing>-<slug>-<field>` convention. Collision risk once two instruments share a page. |
| **F27** | ⭐ The hook's reveal is a single unbranched string opening **"Keep it."**, served identically to a student who chose the option the lesson exists to refute. Verified by two clean-load drives. |
| **F28** | ⭐ b1-04 and b1-05 are both SYSTEM and share **no instrument**. §10.1's one-screen-per-family model cannot express a family with a palette, and 32 slots depend on which it is. |
| **F29** | The `b5-zoom` range input needs **real CSS** — its track and thumb are pseudo-elements, unreachable from an inline `style=`. It is the only such element in KS3 and the only reason this page carries a page-local class. |
| **F30** | The four drawing routines hard-code **15 hex values that are not KS3 tokens** (plant greens, soil, cell wall, vacuole, nucleus). Subject artwork with no home in the schema. |
| **F31** | ⭐ **Drift 3's b1-05 row points at the wrong element.** Line 132 is `{{ levelName }}`, an instrument readout heading; b1-05 has no statement panel at all. Cost of applying the ruling measured at all four viewports (+16 / +16 / +2 / −5 px). The ruling stands for the statement role; b1-05 is an exclusion, not a data point. |
| **F32** | ⭐ **Build-blocking.** `#s-hard` marks correctness on eight sibling rows. MRB-202's R3 runtime assertion — press every activity option, require identical resolved colours, walk up for the effective background — will fire on it. Scope the assertion or register the exception first. |
| **F33** | `#s-break`'s predict gate leaves the DOM with **no "You said:" echo**. b1-04 added that echo; this page has none. F4 half-fixed on one SYSTEM page and unfixed on the other; one value needed. |
| **F34** | `wireSystemParts`' canvas runs a 560×220 buffer at 896 CSS px — **0.625 device px per CSS px**, upscaled ~1.6× and soft at 1×, against Design's 2.018×. A defect wherever that sim survives, independent of this rebuild. |

### Findings confirmed from earlier pages

F1 (breadcrumb) · **F2** (rail top bar shows scroll not completion — reproduced on five stages) ·
**F4** (predict gate leaves the DOM — and here **without** b1-04's partial fix, F33) ·
F12 (tutor CTA is a live anchor with an authored line — **three of three**, and the anchor points
into the page each time) · F14 (`shared/styles.css` absent → rung `h3` 36.8 vs 26.45) ·
F15 (nav brand tile) · F16 (keynote heading element/weight/colour) · F17 (ladder `h2` 57.6 vs 43.2) ·
F19 (KEY FACT box position — **b1-04 and b1-05 agree exactly, including the 24px margin**, giving it
a 2:1:1 majority) · F20 (no legal line — **second page**) · F23 ("Retry my misses" clears the hits
too — second page, identical copy and behaviour, so it is systematic).

**b1-03's D7 reproduces here and did not on b1-04**: the generator renders only 3 endmatter cards
and drops "Connects to" on this lesson.

### Drift rulings, checked against this page

| Drift | Ruled | This page |
|---|---|---|
| 1 — bench column 232px | 232px | **N/A** — no bench grid on this page |
| 2 — collapse 820px | 820px | **N/A** — no bench grid, no `max-width` query of its own |
| 3 — statement `clamp(28px, 3.9vw, 44px)` | as ruled | ⚑ **the b1-05 row is aimed at a readout heading, not a statement.** Cost measured; the ruling stands for the statement role and should exclude line 132. **F31** |
| 4 — `seg()` light branch, b1-06's variant | b1-06's | **Confirmed, and this page is the best evidence for it** — its own dark branch is 53.19px tall against its light branch's 47.59px, the exact mismatch drift 4 objects to. ⚑ Cost measured: 53 controls; **+5.59px at 1280, +65.78px at 820, +76.97px at 390**, because the six choice buttons wrap to a second line at 820 on all eight rows (§3.6.1) |
| 5 — KEY FACT ground `--ks3-band` | `--ks3-band` | **Confirmed** — measured #F4E9D8, source line 232. One of the five |

---

## Provenance

Measured 13 August 2026 on branch `feat/ks3-b1`, in headless Chrome via `ks3_browser.py`
(`Emulation.setDeviceMetricsOverride`), against:

- `docs/ks3/design-reference/b1/b1-05-levels-of-organisation.dc.html` (929 lines, unmodified),
  served over HTTP from `docs/ks3/design-reference/b1/`;
- `mrbadmus_site/ks3/biology/cells-and-organisation/levels-of-organisation.html` (71 lines, build
  already run), served over HTTP from `mrbadmus_site/`.

Sources read: `docs/ks3/architecture.md` §4.8 and its MRB-183 / MRB-202 amendment entries,
`shared/ks3.js` `wireSystemParts` (lines 2246–2570), and this folder's `README.md`,
`00-delivery-drift.md` and `b1-04-specialised-cells.md`.

Nothing on either page was modified. The drift-3 what-if measurements in §3.3.1 were taken by setting
`style.fontSize` live in the browser, reading the result, and restoring the authored value in the
same evaluation.
