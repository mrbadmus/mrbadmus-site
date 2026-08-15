# B1 L4 · Specialised cells · SYSTEM

Inventory of `docs/ks3/design-reference/b1/b1-04-specialised-cells.dc.html` (1,141 lines,
delivered unmodified). Method, viewports, generator vocabulary and standing law: see `README.md` in
this folder — not restated here. Cross-page value collisions: `00-delivery-drift.md`.

Measured 13 Aug 2026 in headless Chrome via `ks3_browser.py`, serving
`docs/ks3/design-reference/b1/` over HTTP, at **1280 · 1340 · 820 · 390** with
`Emulation.setDeviceMetricsOverride` (`page.set_viewport`). Every number below was read from
`getComputedStyle` / `getBoundingClientRect` in that browser, or out of the file's own source.
Where a value could not be measured it says so.

**Console: clean.** No errors or uncaught exceptions at any of the four viewports (favicon 404
filtered), on either this page or the generator's.

Where b1-01, b1-02 and b1-03 have already established something true of all six pages — the header
trail carried inline, the rail's two variants, F2 (the narrow-screen top bar reading complete when
nothing was answered), the `_ds` bundle shipping the 3D Studio stylesheets, the 60-token set, the
DC-runtime settle trap, `ks3-hook-h` being inert, Design's `ks3-ladder` single-class set, and the
content living in `<script data-dc-script>` constants — this file **confirms and cites** rather than
re-deriving. Almost all of its length is spent on what is different here.

## ⚠️ This page is the SYSTEM reference screen — MRB-203's other root cause

`docs/ks3/design-coverage-manifest.md` §10.1 names **this file**, not b1-05, as the approved
reference screen for the SYSTEM family:

| Family | Slots | Reference screen | Approved |
|---|---|---|---|
| SYSTEM | **32** | `docs/ks3/design-reference/b1/b1-04-specialised-cells.dc.html` | Mide, 12 Aug 2026 |

**b1-05 is a SYSTEM lesson but is not the family's reference screen.** §10.1 admits exactly one row
per family and this file holds it. That answers the task's item A directly: every divergence in §3.1
below is a divergence on **32 lessons**, and SYSTEM is one of the two families that had no reference
screen before Design's B1 delivery — §10.1's own note records SYSTEM + CLASSIFY as *"47 of the 183
slots, every one of which would have inherited whatever Code invented."* §3.1 is the measurement of
what Code invented.

**Content payload lives in the file's `<script data-dc-script>` block** and must be lifted
**byte-identical** from these lines, not retyped:

| Payload | Lines |
|---|---|
| `RAIL` | 384–389 |
| `RAIL_SHORT` | 391 |
| `isDone` | 393–399 |
| **`CELLS`** — 4 cells × (job/where/problem/caption/alt + 3 tuning rows + 2 sabotages × (what/3 predicts/caption/alt/3 chain links/close/closeSafe)) | **401–574** |
| `RUNGS` (page-marked r1, r2, with per-option `correction`) | 576–593 |
| `SELF_RUNGS` (r3, r4, with `fieldLabel`/`placeholder`/4 criteria) | 595–616 |
| canvas helpers `rr` / `ell` / `mito` / `arrow` | 618–663 |
| the four cell drawing routines `red` / `root` / `sperm` / `nerve` | 702–935 |
| `paint` / `drawAll` | 937–965 |
| `seg()` — **both branches** | 967–976 |
| `renderVals` (style strings + `hookOptions` + UI strings) | 978–1136 |

Static prose: header 74–76 · hook 84–87 · `#s-tuned` intro 107–109 · `#s-break` head 155–160 ·
`#s-rule` 213–241 (all four problem cards are **static markup**, not data) · `#s-think` 250–255 ·
KEY FACT 261–262 · ladder head 268–269 and retry note 331 · keynote 336–337 · stretch layer 342+346 ·
endmatter 352–371.

**Authored word count (for MRB-205): ~3,840 words**, counted with a script over the source by the
same method b1-03 used (data constants + render literals + static markup):

| Source | Words |
|---|---|
| data constants, lines 384–616 (single-quoted literal content) | **2,958** |
| of which `CELLS` 401–574 | 2,384 |
| of which `RUNGS` 576–593 | 277 |
| of which `SELF_RUNGS` 595–616 | 274 |
| `renderVals` **prose** literals (4 hook options + 8 short UI strings) | ~58 |
| static markup 73–379, tags and `{{ }}` stripped | **824** |

⚠️ One counting caveat, stated because b1-03's figure is quoted elsewhere: a naive extraction of all
single-quoted literals from `renderVals` returns ~250 tokens, but the great majority of those are
inline **CSS fragments** (`'display:grid;place-items:center;…'`), not prose. The 58 above is the
prose only. Almost all 3,840 words are science-bearing and **none of it exists in `ks3_data/`** —
`ks3_data/biology_b1_cells.py`'s `specialised-cells` record is a different lesson with different
content (§3.1.2).

---

## 1. Page skeleton

### 1.1 The spine — confirms b1-03 §1.1

`<body>` holds two children: the hydrated **`<div class="rd" data-mode="ks3" id="dc-root">`** and
the logic `<script>`. As on b1-03, the `<x-dc>` template is removed rather than hidden.

**`.rd` is a DIV here, not `<body>`** — b1-01 §1.1 recorded this and resolved it ("nothing to
change"); confirmed identically. The same 8 inline declarations on the div reproduce what
`body.rd[data-mode="ks3"]` in `shared/ks3.css` would give (`background var(--ks3-ground)`,
`color var(--ks3-ink)`, `font-family var(--ks3-font-body)`, `font-size 19px`, `line-height 1.6`,
`min-height 100vh`, `-webkit-font-smoothing: antialiased`, `text-wrap: pretty`), and the token block
is `.rd[data-mode="ks3"]` so all tokens resolve. Every one of the 37 `--ks3-*` tokens probed
resolved to its `shared/ks3.css` value (spot table in §6.1).

`.rd` children, in order — **5 top-level landmarks, same set as b1-01 and b1-03**:

| # | Element | Position | Height 1280 |
|---|---|---|---|
| 1 | `nav.ks3-nav` | static | 63.19 |
| 2 | `nav[data-rail="top"]` | **sticky, top 0, z-index 20** | 46.59 |
| 3 | `nav[data-rail="side"]` | **fixed, top 150px, left calc(50% − 632px), width 104px, z-index 20** | 0 (`display:none` <1340) |
| 4 | `main.ks3-main` | static | — |
| 5 | `footer.ks3-footer` | static | 75.59 |

### 1.2 The measure

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `.ks3-main` width | 1280 | **1320** (capped, margin 10px each side) | 820 | 390 |
| `.ks3-main` max-width | 1320px = `--ks3-page` | same | same | same |
| `.ks3-main` padding | 44px 24px 90px | 44px 24px 90px | 44px 24px 90px | **28px 16px 64px** |
| `.ks3-lesson` width | **960** | **960** | 772 | 358 |
| `.ks3-lesson` max-width | 960px = `--ks3-wide` (60rem) | same | same | same |
| `nav.ks3-nav` height | 63.19 | 63.19 | **63.19** | **153.97** |
| document height | 8477 | 8430 | 8585 | 13302 |

Narrow breakpoint verified by bisection: `.ks3-main` padding and `.ks3-block` padding change between
**545 (wide: 44px 24px 90px / 32px) and 544 (narrow: 28px 16px 64px / 22px 18px)** —
`@media (max-width: 34rem)` in `shared/ks3.css`, identical to b1-01 and b1-03.

**The page's own media queries are exactly three** (plus the `print` block the `_ds` bundle ships):
`max-width: 780px` (bench grid), `min-width: 1340px` (rail swap) and `prefers-reduced-motion: reduce`
(kills `[data-arrive]`). Enumerated from `document.styleSheets`, inline sheets only.

This page carries **no `.ks3-explainer`** — there is no 736px `--ks3-measure` column anywhere in it,
exactly as b1-03. Prose is capped by `ch` measures instead: `54ch` on `#s-tuned`'s intro, `58ch` on
`#s-break`'s lede, `24ch` on the `#s-rule` statement and `56ch` on its sub-line.

### 1.3 Header carries the lesson trail INLINE — confirmed; wraps latest of the three

Nav markup and every resolved value match b1-01 §1.3 and b1-03 §1.3 exactly: `display:flex;
flex-wrap:wrap; gap:6px 0; padding:14px 24px 12px; border-bottom:2px solid --ks3-ink;
background --ks3-ground`; brand Bricolage 22px/800 with a 34×34 `--ks3-accent` r10 tile; 2×26
`--ks3-rule` divider at `margin 0 20px`; `ol[aria-label="Breadcrumb"]` at body-font **17px/22.1px,
gap 9px**; trailing `a.ks3-nav-link` "KS3".

The `<ol>` measures **469.61px** — the shortest of the three pages inventoried (b1-03: 512.67,
b1-01: 724.44) — so the nav stays **63.19px at 1280, 1340 *and* 820**, growing only at 390
(**153.97**, trail over 2 rows). This confirms b1-03's rule and strengthens it: **nav height is a
pure function of the lesson title's length, and a parity assertion must not pin it to a number.**

F1 (Design's inline trail vs the generator's `nav.ks3-crumbs` inside `<main>`) reproduces exactly;
measured against the generator's in §3.1.4.

### 1.4 Lesson body, document order — **11** direct children of `.ks3-lesson`

| # | Element | id | classes | margin-top | scroll-margin-top |
|---|---|---|---|---|---|
| 1 | `header` | — | `ks3-lesson-head` | — | — |
| 2 | `section` | `s-hook` | `ks3-block ks3-dark ks3-hook` | 28px | 92px |
| 3 | `section` | `s-tuned` | `ks3-block` | 28px | 92px |
| 4 | `section` | `s-break` | `ks3-block ks3-dark ks3-practical` | 28px | 92px |
| 5 | `section` | `s-rule` | **none** (all inline) | 28px | 92px |
| 6 | `section` | `s-think` | `ks3-block ks3-misconception` | 28px | 92px |
| 7 | **`div`** | — | **none** — the KEY FACT box | **24px** | 0 |
| 8 | `section` | `s-ladder` | **`ks3-ladder`** (single class) | 28px | 92px |
| 9 | `section` | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | 28px | 92px |
| 10 | `section` | — | `ks3-layer` | 34px | — |
| 11 | `div` | — | `ks3-endmatter` | 34px | — |

Three structural facts worth stating plainly:

- **The stray unclassed `<div>` is back.** b1-03 §1.4 recorded that b1-01 had a stray top-level
  `<div>` (its KEY FACT box) and that b1-03 had none, having moved its two KEY FACTs *inside*
  `#s-think`. b1-04 reverts to b1-01's shape: **one KEY FACT box, at top level, between `#s-think`
  and `#s-ladder`, with no class, no id, `margin-top: 24px`** (every neighbouring block uses 28px) —
  and in the source it sits at lines 259–263 with anomalous indentation, two levels deeper than its
  siblings. So across three pages the KEY FACT box has taken **three different structural
  positions**. Finding F19; the generator needs one.
- **There is NO `p.ks3-legal`.** Measured `document.querySelector('.ks3-legal') === null`. b1-03
  ended on a lesson-specific *safety* line; b1-01 and the generator end on a copyright line; this
  page ends on the endmatter and nothing else. That is a **third** answer to the same slot, and it
  makes b1-03's gap G11 ("only one can occupy the slot") sharper: the slot is not even always
  occupied. Finding F20.
- **Every id-bearing block is a `<section>` with an anchor**, and `#s-rule` again carries no class at
  all — its whole appearance is inline (`background: var(--ks3-band)`, `border: 3px solid
  var(--ks3-ink)`, `border-radius: var(--ks3-r-block)`, `padding: 34px 32px`).

### 1.5 Class audit and stylesheet set

The page uses **49 `ks3-*` class names, and all 49 exist in `shared/ks3.css`** (checked by string
match of `.<class>` against the sheet; zero misses). There is **no `ks3-hook-h`** — this page's hook
`<h2>` carries no class at all and is styled by `.ks3-hook h2`. That is now the *second* independent
confirmation of b1-01's recommendation ("`ks3-hook-h` is an inert class. Drop it"): b1-03 and b1-04
both dropped it.

Non-`ks3-*` classes: `rd`, `sc-host`, `sc-interp`. The `sc-interp` gotcha b1-03 §1.5 recorded holds
and **bit this measurement run**: the DC runtime wraps every `{{ }}` interpolation in a
`<span class="sc-interp">`, so `button.querySelector('span')` on a cell button returns the wrapper,
not the author's span. The correct probe is `button.children[n]`. A parity probe that walks
descendant spans positionally will read the wrong element on the reference page and the right one on
generator output.

Everything else is carried by **125 inline `style=` attributes** (b1-03: 225, b1-01: 110) plus
**11 JS-built style strings** (`seg` — used for two different components, see §3.3 —
`node.chipStyle/textStyle/lineStyle/linkStyle`, `railBarStyle`, `c.tagStyle`, `t.dialStyle`,
`link.style`, plus the class-name builders `feedbackClass` and `tallyClass`).

**Stylesheet sets differ exactly as b1-03 §1.5 recorded, and both consequences reproduce.**
Enumerated by walking `document.styleSheets` and following every `CSSImportRule`:

| | Reference page | Generated page |
|---|---|---|
| sheets | 9 (2 inline + `_ds/…/styles.css` → 5 imports + 1 inline) | **4 link tags** |
| KS3 rules | `_ds/…/tokens/shared-ks3.css` | `/shared/ks3.css?v=41a3ad43` |
| tokens | `_ds/…/tokens/shared-tokens.css` | `/shared/tokens.css?v=8bc49b72` |
| **`shared/styles.css`** | **absent** | **present** (`?v=2da37530`) |
| **`shared/nav.css`** | **absent** | **present** (`?v=2fd4a55f`) |
| 3D Studio CSS | `_ds_bundle.css` **and** `tokens/src-styles-tokens.css` | absent |

b1-03's **F14** reproduces to the same numbers on this page — the absent `shared/styles.css` means
KS3 headings with no explicit line-height inherit 1.6 on the reference page and 1.15 on the
generated one:

| | reference | generated |
|---|---|---|
| `.ks3-rung h3` | 23px / **36.8px** (1.6) | 23px / **26.45px** (1.15) |

b1-03's **F17** reproduces too: `class="ks3-ladder"` alone misses `.ks3-block h2`, so the ladder
heading is 36px / **57.6px (1.6)** here against the generator's 36px / **43.2px (1.2)**. Both
findings are therefore confirmed on a second family's reference screen and are not b1-03 artefacts.

---

## 2. The progress rail — same component as b1-01/b1-03, **four** stages

Byte-for-byte the component b1-01 §2 specified, at a different stage count. Confirmed by
measurement, not re-derived:

- **Two variants, never both, never neither.** Bisected: at **1339** `[data-rail="side"]` is
  `display:none` and `[data-rail="top"]` is `display:block`; at **1340** and **1341** the reverse.
  Same two authored rules (source lines 22–23).
- **Side rail geometry identical:** `fixed`, `top 150px`, `left calc(50% − 632px)` → **x 38** at
  1340, `width 104px`, `z-index 20`; `.ks3-lesson` starts at x 190 → a 48px gutter. Height
  **326.75** for four nodes (b1-03: 416.94 for five).
- **Chip states identical, every colour a token:** done = `--ks3-accent` #E4572E ground, `--ks3-ink`
  border, `--ks3-on-dark` text, holds `svg.ks3-mark` (measured `hasMark: true`, `chipTxt: ""` — the
  number is *replaced* by the tick); current-not-done = `--ks3-card` on `--ks3-ink` with
  `box-shadow: 0 0 0 4px --ks3-accent-tint`; future = `--ks3-card` on `--ks3-rule-strong` with
  `--ks3-ink-ghost` text. Chip 32×32, r10, Bricolage 16px/800, border 2px.
- **Label** MONO 11px/500, `letter-spacing .09em` (0.99px), uppercase, lh 1.2; current `--ks3-ink`,
  done `--ks3-ink-muted`, future `--ks3-ink-ghost`.
- **Connector** 2×20 at `margin 7px 0`; `--ks3-accent` when the node above is done, else `--ks3-rule`
  (#E0D2B9). Omitted on the last node (`hasLine: i < RAIL.length - 1`).
- **Top bar** `sticky; top 0; z-index 20; background --ks3-ground; border-bottom 2px --ks3-rule;
  padding 9px 16px 10px`; inner row `flex; gap 12px; max-width 60rem; margin 0 auto`; count MONO
  15px/500 `--ks3-ink-muted`; current label 16px/700 `--ks3-ink` with
  `overflow:hidden; text-overflow:ellipsis; white-space:nowrap` (measured **795px** at 1280); track
  `flex 0 0 96px`, height 8px, r99, `--ks3-band` ground, `2px --ks3-ink`; fill 4px inside the border,
  `--ks3-accent`.

### 2.1 Four stages, and their two label sets

`RAIL` 384–389 + `RAIL_SHORT` 391:

| # | anchor | side label (`RAIL_SHORT`) | top-bar label (`RAIL[].label`) | `done_when` (`isDone`, 393–399) |
|---|---|---|---|---|
| 1 | `#s-hook` | HOOK | The trade | `s.hookChoice !== null` |
| 2 | `#s-tuned` | TUNED | Same seven parts | `Object.keys(s.seen).length >= 4` |
| 3 | `#s-break` | BREAK | Break it on purpose | `Object.keys(s.predict).length >= 4` |
| 4 | `#s-ladder` | LADDER | Mastery ladder | `answers.r1 !== undefined && answers.r2 !== undefined && checked.r3 && checked.r4` |

Both label sets are authored and neither is derivable from block titles. Fill maths is
`(active + 1) / 4 × 100%` — measured **23 / 46 / 69 / 92 of a 96px track** (the track's inner width
is 92px after its 2px border, so stage 4 is a full bar).

**All four stages are reachable and I drove all four to done.** Three notes, all measured:

- **Stage 2 is the most honest `done_when` in the B1 inventory so far.** `seen` starts pre-seeded
  with the `startCell` prop's cell, so one of four is already banked at load; the student must then
  visit the other three. Measured: after clicking cells 2, 3 and 4, TUNED ticked. Unlike b1-03's
  BENCH — which ticked on a single gate click and credited the richest instrument on the page by its
  cheapest control — this stage cannot be earned without touching the instrument itself.
- **Stage 3 asks for half of what is on the page.** `predict` is keyed `cellId + ':' + sabotageId`
  and there are **8 sabotages** (4 cells × 2), but `isDone` wants only **4 keys**. Measured by
  driving one prediction per cell: the progress line read "1 of 8" → "4 of 8 sabotages run" and BREAK
  ticked at 4. So the block's own counter and the rail's threshold disagree about what "done" is —
  the student sees *4 of 8* beside a ticked stage. That is not a bug, but it is an authored decision
  the generator must be told (`done_when` needs a threshold, not just a name). Finding F21.
- **Stage 3 cannot regress.** Unlike b1-03's FIT (whose "Strip it back out" *deleted* a key and could
  un-tick an earned stage), nothing here removes a key from `predict`. Once answered, a sabotage
  stays answered; there is no reset except the page reload.

### 2.2 F2 reproduced, on four stages, and one stage worse than b1-03

b1-01's F2 ("the top bar shows scroll, not completion") reproduces exactly. Driven at 1280 with
`scrollIntoView` at each anchor and **nothing answered**:

| scrolled to | count | label | fill |
|---|---|---|---|
| `#s-hook` | 1 / 4 | The trade | 23 / 96 |
| `#s-tuned` | 2 / 4 | Same seven parts | 46 / 96 |
| `#s-break` | 3 / 4 | Break it on purpose | 69 / 96 |
| `#s-rule` | 3 / 4 | Break it on purpose | 69 / 96 |
| `#s-think` | 3 / 4 | Break it on purpose | 69 / 96 |
| `#s-ladder` | **4 / 4** | Mastery ladder | **92 / 96 (full)** |
| `#s-keynote` | 4 / 4 | Mastery ladder | 92 / 96 |

`#s-rule`, `#s-think` and `#s-keynote` are anchored but unlisted, so the `IntersectionObserver`
(`rootMargin: '-45% 0px -50% 0px'`, lines 676–686) never fires for them and the bar sits stale
through them. A student under 1340px reads a **complete progress bar having answered nothing**, and
the side rail — the variant that does read completion — is the one they cannot see. Still Finding F2,
now on the reference screen for 32 more lessons. **Fewer stages makes it worse:** four stages means
each scroll step is 25% of the bar, so scrolling past two blocks reads as half the lesson done.

### 2.3 Anchors

**All 8 id-bearing sections carry `scroll-margin-top: 92px`**, authored individually as an inline
style on each (`s-hook`, `s-tuned`, `s-break`, `s-rule`, `s-think`, `s-ladder`, `s-keynote` — and
`#dc-root`, the runtime's own wrapper, carries 0). The rail references **4 of the 7 lesson
anchors**. The KEY FACT div, `.ks3-layer` and `.ks3-endmatter` carry no anchor.

Verified by driving: clicking the side rail's BREAK link at 1340 puts `#s-break` at **top: 92.11px**
with `location.hash = "#s-break"`. `scroll-behavior` resolves to `auto` (no smooth scroll authored).

### 2.4 What the generator needs to emit it

Identical shape to b1-01 §2.6 and b1-03 §2.4, four entries, **plus a threshold** (§2.1's F21):

```python
"rail": [                                     # NEW field, §5 gap G1
  {"anchor": "s-hook",   "short": "HOOK",   "label": "The trade",
   "done_when": "committed"},
  {"anchor": "s-tuned",  "short": "TUNED",  "label": "Same seven parts",
   "done_when": "all_specimens_seen"},        # 4 of 4
  {"anchor": "s-break",  "short": "BREAK",  "label": "Break it on purpose",
   "done_when": "predictions_made", "threshold": 4},   # of 8 available
  {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
   "done_when": "ladder_complete"},
]
```

`short` is ≤6 chars on all three pages measured (HOOK/BENCH/WALL/BUILD/LADDER, TESTS/SORT,
TUNED/BREAK) — worth asserting rather than assuming, because the 104px rail column at MONO 11px
`.09em` is what sets the limit. `scroll-margin-top: 92px` must be emitted on **every** id-bearing
section, not only rail stages.

---

## 3. Every block in document order

`GEN?` — **E** the generator has this block type · **E★** existing type, but this page uses it in a
shape the renderer cannot produce · **N** new. Component names in the last column are
`ks3_parity.COMPONENTS` entries (60 registered) that would gate it.

| # | Block | GEN? | States | Gating components |
|---|---|---|---|---|
| 1 | `header.ks3-lesson-head` — eyebrow "Cells and organisation · System", h1, `.ks3-bigq`, `.ks3-review-flag` | **E** | draft flag present / absent (`showDraft` prop) | lesson title · big question · eyebrow · draft badge |
| 2 | `#s-hook` — ink-dark: eyebrow, h2, prompt, `.ks3-hook-commit` with `.ks3-commit`, 4 `.ks3-option`s, gated `.ks3-reveal` | **E★** | option resting / chosen (border → `--ks3-alert`); reveal hidden / shown | hook is ink-dark, accent shadow · dark-block option resting/CHOSEN |
| 3 | `#s-tuned` — **the SYSTEM flagship**, a light bench: 4 full-width option rows + live canvas + tuning readout (§3.2) | **N** | 4 cells × 3 tuning rows × 6 dial kinds | **none registered** |
| 4 | `#s-break` — **the sabotage-and-consequence practical** (§3.4) | **N** | 4 cells × 2 sabotages × (unpredicted / predicted) × dark canvas + 3-link chain | `sim canvas` gates `practical` today and there is no `.ks3-sim` here |
| 5 | `#s-rule` — statement panel: `--ks3-band`, `3px --ks3-ink`, eyebrow, `clamp(28px,3.9vw,44px)` statement at `24ch`, sub-line at `56ch`, **4 cream problem cards** | **N** | static | none (closest: standard block shell) |
| 6 | `#s-think` — misconception carrying **two** quote/answer pairs split by an `--ks3-alert-border` rule | **E★** | static | misconception is amber |
| 7 | **unclassed `<div>`** — one KEY FACT box, top-level, `mt 24px` | **N** | static | none |
| 8 | `#s-ladder` — `class="ks3-ladder"`, head + score, 2 page-marked rungs, 2 self-marked rungs, `.ks3-retry-wrap` | **E** | option resting / correct / wrong / spent; feedback correct / wrong; ticks 0..4; tally not-yet / met; retry | ladder shell · ladder heading · ladder option ×6 states+badges · ladder feedback CORRECT/WRONG · page-marked rung is accent · self-marked rung is violet · R8 answer box · R8 check-my-answer button |
| 9 | `#s-keynote` — ink-dark, alert-yellow shadow, **`p.ks3-eyebrow`** + one paragraph | **E★** | static | key note is ink-dark · key note type drops to 700 |
| 10 | `.ks3-layer` — "Going further" violet stretch layer, **one bare `<p>`** | **E★** | static | stretch layer is violet |
| 11 | `.ks3-endmatter` — **4 cards**: "Before this lesson" (1 link) · "Connects to" (2 links) · "At GCSE this becomes" (**prose**) · `.ks3-tutor` (**live `<a href="#s-rule">`**) | **E★** | static | tutor card is accent · tutor text is large-bold |
| — | `p.ks3-legal` | — | **ABSENT** | — |

Totals: **2 blocks the generator can already produce (E)**, **5 it produces in the wrong shape
(E★)**, **4 it cannot produce at all (N)**. Two of the four rail stages sit inside N blocks.

---

### 3.1 ⭐ The generator's SYSTEM output versus Design's SYSTEM drawing, component by component

This is the point of measuring this page. MRB-203's finding was that the parity gate reported green
over 116 assertions while B1 shipped with no progress rail and a flat uniform stack, because the gate
cannot see an unregistered component — and SYSTEM is one of the two families that had **no reference
screen at all** when the generator's SYSTEM pages were written. So this comparison is the direct
answer to *"has the generator drifted from Design's SYSTEM drawing, or was it never at it?"*

Generated page measured at the same four viewports from
`mrbadmus_site/ks3/biology/cells-and-organisation/specialised-cells.html` (build already run),
served over HTTP from `mrbadmus_site/`. Console clean at all four.

#### 3.1.1 The verdict first

**"Never at it", and further away than MODEL was.** The two pages agree on everything
`shared/ks3.css` owns and agree on almost nothing else — and unlike b1-03, where at least the
subject matter matched, **these two pages teach different lessons.** Design's b1-04 is *"the same
seven parts, tuned"* across four cells with a sabotage-and-consequence engine. The generator's page
is *"shape is its job"* built around **diffusion**, with a chemistry-borrowed diffusion sim and a
`system-parts` dependency graph. They share a title, a slug and a red blood cell; they do not share a
big question, a hook, a misconception, a ladder or a key note.

| Layer | Agreement |
|---|---|
| Tokens / palette | identical |
| Block shells (`.ks3-block`, `.ks3-dark`, `.ks3-hook`, `.ks3-misconception`, `.ks3-practical`, `.ks3-ladder`, `.ks3-keynote`, `.ks3-layer-body`, `.ks3-endmatter > section`, `.ks3-tutor`, `.ks3-rung`, `.ks3-answer`, `.ks3-check-btn`, `.ks3-option`, `.ks3-footer`) | **identical to the pixel** — §3.1.3 |
| Page shell (`.ks3-main` padding/max-width, `.ks3-lesson` 960px, h1 74px/69.56/−2.59px, narrow query at 34rem) | identical |
| Document structure | **11 blocks vs 20; no shared block sequence** |
| The flagship instrument | **absent from the generator** |
| The lesson's actual content | **different lesson** |
| Chrome (rail, brand, crumbs, keynote heading, ladder/rung type, endmatter, tutor, legal) | **eight divergences, §3.1.4** |

#### 3.1.2 Structure: 11 blocks against 20

| | Design (11 children of `.ks3-lesson`) | Generator (20 children) |
|---|---|---|
| 1 | `header.ks3-lesson-head` | `header.ks3-lesson-head` |
| 2 | `#s-hook` (hook **+ commit + 4 options + gated reveal in one dark block**) | `.ks3-hook` (prose only, ends on a `.ks3-commit` `<p>` with no buttons) |
| 3 | `#s-tuned` — the flagship | `.ks3-check` `which-has-no-nucleus` |
| 4 | `#s-break` — the sabotage engine | `.ks3-explainer` |
| 5 | `#s-rule` | `.ks3-figure.ks3-figure-pending` |
| 6 | `#s-think` (2 quote/answer pairs) | `.ks3-misconception` `no-nucleus-reveal` |
| 7 | KEY FACT `<div>` | `.ks3-check` `how-does-oxygen-get-in` |
| 8 | `#s-ladder` | `.ks3-practical` `membrane-diffusion-lab` (holds `ks3-sim data-sim="diffusion"`) |
| 9 | `#s-keynote` | `.ks3-explainer` |
| 10 | `.ks3-layer` | `.ks3-figure.ks3-figure-pending` |
| 11 | `.ks3-endmatter` | `.ks3-practical` `knock-out-the-shape` (holds `ks3-sim data-sim="system-parts"`) |
| 12 | — | `.ks3-figure.ks3-figure-pending` |
| 13 | — | `.ks3-keywords` (**4 flip cards**) |
| 14 | — | `.ks3-check` `shape-job-cards` (**6 more flip cards**) |
| 15 | — | `.ks3-check` `design-a-cell` (criteria button) |
| 16 | — | `.ks3-ladder` |
| 17 | — | `.ks3-keynote` |
| 18 | — | `.ks3-layer.ks3-stretch` (holds a nested explainer + check) |
| 19 | — | `.ks3-endmatter` |
| 20 | — | `p.ks3-legal` |

Generator block-type census, measured: `check` 5 · `explainer` 3 · `figure` 3 · `practical` 2 ·
`hook` 1 · `misconception` 1 · `keywords` 1 · `ladder` 1 · `keynote` 1 · `layer` 1 · `endmatter` 1 ·
`legal` 1.

Consequences that are facts, not readings:

- **No block on the generated page carries an `id` or a `scroll-margin-top`.** Measured `smt: 0px`
  across all 20 children; the only 12 `id`s on the page are form-control ids (`ks3-sim-part-2`,
  `ks3-ans-specialised-cells-explain`, `ks3-crit-…`). The rail has nothing to anchor to even once it
  exists — `rail[].anchor` requires emitting section ids first.
- **`[data-rail]` count is 0** and `[data-bench-grid]` count is 0, at all four viewports.
- **The generator's hook does not commit.** Design's `#s-hook` ends with 4 `.ks3-option`s and a gated
  reveal *inside the dark block*; the generator's `.ks3-hook` ends with a `.ks3-commit` paragraph and
  the commit moves to a separate light `.ks3-check`. Same divergence b1-03 recorded, on a second
  family.
- **Three `ks3-figure-pending` slots vs one live canvas.** Design carries no `<figure>` at all: its
  diagrams are two live canvases (1800×1120 and 1800×840) drawn from data by 234 lines of routine.
  The generator carries three dashed "Diagram coming soon" placeholders (`3px dashed
  --ks3-rule-strong` #C3B191, `--ks3-inset` ground, `padding 52px 24px`, r24 — measured) and no cell
  drawing at all. On the SYSTEM reference screen the system is drawn; on the generator's SYSTEM page
  it is a to-do, three times.
- **10 flip cards vs 0.** Measured on the reference page: `document.querySelectorAll('[aria-expanded]').length === 0`
  and no `.ks3-cards` / `.ks3-card-btn`. **Neither of the two reference screens inventoried so far
  contains a flip card**, which means R4's ambiguous clause (*"one tap flips one card"* — at most one
  open, or one card per tap?) still cannot be arbitrated from Design's delivery. b1-03 §3.1.6 flagged
  it; this page adds a second family's silence. Ambiguity for Design, §8(a).

#### 3.1.3 Where they agree — the shells, to the pixel

Measured at 1280 on both. Every row below is identical on the two pages.

| Shell | ground | border | radius | shadow | padding |
|---|---|---|---|---|---|
| `.ks3-block` | `--ks3-card` #FFFCF5 | 2px `--ks3-ink` | 28px | `5px 5px 0 #221E1B` | 30px |
| `.ks3-dark.ks3-hook` | `--ks3-ink` #221E1B | none | 30px | `6px 6px 0 #E4572E` | 32px |
| `.ks3-dark.ks3-practical` | `--ks3-ink` | none | 30px | **`6px 6px 0 #2F5CE0`** | 32px |
| `.ks3-dark.ks3-keynote` | `--ks3-ink` | none | 30px | `6px 6px 0 #FFC53D` | 32px |
| `.ks3-misconception` | `--ks3-alert-tint` #FFF3D4 | 2px `--ks3-ink` | 28px | `5px 5px 0 #221E1B` | 30px |
| `.ks3-ladder` | `--ks3-card` | 3px `--ks3-ink` | 30px | `6px 6px 0 #12A150` | 32px |
| `.ks3-layer-body` | `--ks3-stretch-tint` #F0EAFC | 2px `--ks3-stretch` #6B3FD4 | 26px | none | 26px 28px |
| `.ks3-endmatter > section` | `--ks3-card` | 2px `--ks3-ink` | 22px | none | 22px |
| `.ks3-tutor` | `--ks3-accent` | 2px `--ks3-ink` | 22px | none | 22px |
| `.ks3-rung` | — | border-left 4px `--ks3-accent` | — | — | 0 0 0 22px |
| `.ks3-rung-self` | — | border-left 4px `--ks3-stretch` | — | — | 0 0 0 22px |
| `.ks3-answer` | `--ks3-card` | 2px `--ks3-option-border` | 16px | — | 16px 18px, min-height 136px |
| `.ks3-check-btn` | `--ks3-band` | 2px `--ks3-ink` | 14px | — | 13px 20px |
| `.ks3-option` (light) | `--ks3-ground` | 2px `--ks3-option-border` | 16px | — | 16px 18px, min-height 44px |
| `.ks3-ladder .ks3-option` | `--ks3-ground` | 2px `--ks3-option-border` | **15px** | — | **15px 17px** |
| `.ks3-footer` | `--ks3-card` | border-top 2px `--ks3-ink` | — | — | 24px |
| `.ks3-endmatter` grid | — | — | — | — | 3 × 309.328px, gap 16px |

That list is the substance of *"where Design drew the screen, the build is right."* The list below is
what the registry could not see.

#### 3.1.4 Where they diverge — chrome, eight items measured

| # | Component | Design (b1-04) | Generator | Verdict |
|---|---|---|---|---|
| D1 | **Progress rail** | 2 variants, 4 stages, threshold 1340 | **absent** (0 `[data-rail]`) | new component, §7.1 |
| D2 | **Nav brand mark** | 34×34 `--ks3-accent` r10 tile with a `#FBF3E6` chevron 20×20 inside, then wordmark. `a` measured 180.97×35.19 | **bare `#E4572E` chevron SVG 30×30, no tile** (measured `.ks3-brand span` absent), then wordmark. `a` 176.97×35.19 | ⚑ **Design diverges from MRB-197's own ruling**, which says "a single bold `#E4572E` chevron + wordmark" — the generator's version. b1-03's F15, reproduced identically on a second page, so it is Design's settled house style, not a slip. For Design |
| D3 | **Breadcrumb** | body-font 17px/22.1, gap 9px, `--ks3-accent-text` 600 links, **inline in `nav.ks3-nav`** behind a 2px divider; `<ol>` 469.61px | `nav.ks3-crumbs` **inside `<main>`**, MONO 14px `--ks3-ink-muted`, gap 6.4px, `margin 0 0 24px`, full-width (1232px at 1280), `.ks3-crumb-sep` | b1-01's F1, unchanged |
| D4 | **Keynote heading** | `<p class="ks3-eyebrow">Key note</p>` → Bricolage 30px/**700** UPPERCASE **`--ks3-alert` #FFC53D** (caught by `.ks3-keynote p`) | `<h2>Key note</h2>` → Bricolage 30px/**800** sentence case **`--ks3-on-dark` #FBF3E6** | b1-03's F16, reproduced exactly. Two reference screens now agree with each other and disagree with the build |
| D5 | **Ladder `h2` line-height** | `class="ks3-ladder"` alone → `.ks3-block h2` misses → **36px / 57.6px (1.6)** | `class="ks3-block ks3-ladder"` → **36px / 43.2px (1.2)** | b1-03's F17, reproduced. 14.4px per line |
| D6 | **Rung `h3` line-height** | 23px / **36.8px (1.6)** | 23px / **26.45px (1.15)** | b1-03's F14 (`shared/styles.css`), reproduced |
| D7 | **Tutor CTA** | `<a class="ks3-tutor-cta" href="#s-rule">Ask about this lesson</a>`, 18px/600; heading "Ask Mr Badmus AI"; line "Not sure which problem a cell is solving?" | `<span class="ks3-tutor-cta">Start a question →</span>`, **no href**, 16px/700; heading "Stuck? Ask Mr Badmus AI"; generic line | b1-01's F12, unchanged. Design's anchor again points into its own page (b1-03 pointed at `#s-bench`; this one at `#s-rule`) |
| D8 | **Legal line** | **absent entirely** | fixed copyright/provenance line, 15px `--ks3-ink-muted`, `border-top 1px --ks3-rule`, `padding 16px 0 0` | **new**, and it makes b1-03's G11 a three-way: copyright (generator) vs safety (b1-03) vs nothing (b1-04). Needs a ruling, §8(c) |

**Endmatter is the one chrome item that now agrees.** Both pages carry **4 cards** with the same
grid, and the generator does render a "Connects to" card here — so b1-03's D7 ("`references` is
unrendered; only 3 cards") does **not** reproduce on this lesson. The generator's version of the
third card renders `ks4_links` as **links** where Design writes **prose** ("Cell differentiation,
exchange surfaces and surface area to volume ratio, and active transport at the root hair."), which
is the surviving half of D7. The generator's "Connects to" card additionally carries a **`<p>` of
platform self-explanation** — *"Diffusion is owned by C1 (§7.4 ordering: the particle idea is taught
in chemistry first)…"* — rendered to the student. That is a §8.10 copy-rule breach on a live page
(no platform self-explanation on student pages). Finding F22, and it is a defect in the current
build regardless of the rebuild.

#### 3.1.5 The flagship: Design's two canvases versus the generator's two sims

| | Design | Generator |
|---|---|---|
| Instruments | **`#s-tuned`** (light) + **`#s-break`** (dark) | `membrane-diffusion-lab` + `knock-out-the-shape`, both dark `.ks3-practical` |
| Canvas 1 | `<canvas width="1800" height="1120">` at **638×396.97 CSS** at 1280 → ~2.82 device px per CSS px, drawn via `ctx.setTransform(2,0,0,2,0,0)` over a fixed 900×560 diagram space scaled to fit | `<canvas width="560" height="220">` at **896×354.42 CSS** → **0.625 device px per CSS px** |
| Consequence | crisp at 1× and 2× | **upscaled ~1.6× and soft at 1×**; measurably not retina |
| Canvas 2 | `<canvas width="1800" height="840">`, rendered on a `--ks3-dark-panel` ground with `dark=true` passed to the same routines — the drawing has a **dark palette variant built in** (`ink = '#C6B9A7'`, grounds `#241A18`/`#241E17`/`#1A1611`/`#100D0A`) | same 560×220 sim canvas, second instance |
| Frame | `2px --ks3-ink`, `--ks3-r-card` 22px, cream, with a MONO 14px caption strip **inside** the frame on `--ks3-band` behind a `2px --ks3-rule` top border (dark variant: `2px --ks3-on-dark-muted` frame, `--ks3-dark-panel` caption strip) | `2px --ks3-on-dark-muted` #C6B9A7, r20, caption *outside* the frame at body size |
| Content | four real cells drawn from data — biconcave discs folding through a capillary; a root hair pushing between 13 soil particles with water/mineral arrows; a sperm head/midpiece/tail with 4 mitochondria; a nerve soma with 5 dendrites, a segmented myelin sheath and branched terminals — **each with a sabotaged variant** (sphere / nucleus-restored / stubbed hair / no mitochondria / no tail / limp tail / bare axon / 3-cell relay) | an abstract dependency graph of 6 named part nodes, and a two-population diffusion animation |
| Controls | 4 full-width cell rows + 2 dark sabotage segments + 3 predict options = 9 controls; 13 `[aria-pressed]` on the page | one `data-controls="part"` / `data-controls="temperature"` selector each, built by JS |
| Locked state | **none** — no veil, no blur, no disabled control anywhere on this page (measured: 0 `disabled` attributes outside the answered ladder) | **R5 exactly**: canvas `filter: blur(2px) saturate(0.65)`, an 85%-alpha `--ks3-card` veil carrying "Make your prediction first — then the lab runs.", controls collapsed, caption readable |
| Gating | the *content* is gated instead: `chainOpen = answered`, so the broken canvas and the consequence chain **do not exist in the DOM** until the prediction is made | the instrument exists and is veiled |

Two things follow. First, **Design gates by absence and the generator gates by veil.** These are
different answers to R5's "predict before you see". Design's is stricter (there is nothing to peek
at) but gives the student no preview of what they are predicting about; the generator's R5 veil is
the more legible affordance. **The page wins** — Code renders Design's absence-gate — but the R5
component must not be deleted from the registry when the bench replaces the sim, because PROCESS and
INVESTIGATION still use it. Second, **§10.2's `practical` row maps to `sim canvas` + `sim live figure
is mono`, and neither exists in Design's practical block.** `#s-break` is a `ks3-practical` whose
canvas is not a `.ks3-sim` at all. So §10.2's `practical` row is stale against **both** reference
screens now measured, not just b1-03's.

---

### 3.2 `#s-tuned` — "Nothing new was added. Something was turned up, and something was turned down."

The SYSTEM flagship, and the largest new component on this page. The SYSTEM spine asks for parts
that only mean anything in relation to a whole; this realises it as **one bench, four specimens, and
a three-row tuning readout that never changes its shape**.

**Layout.** `[data-bench-grid="1"]`, `display: grid; gap: 22px; align-items: start`, with the column
template supplied by the page's own `<style>` at line 20 (§3.3.1). Measured:

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `grid-template-columns` | `232px 642px` | `232px 642px` | `232px 454px` | **`318px`** (collapsed) |
| grid box | 896 × 1243.81 | 896 × 1243.81 | 708 × 1349.38 | 318 × 2134.67 |
| canvas CSS box | 638 × 396.97 | 638 × 396.97 | 450 × 280 | 314 × 195.38 |
| readout box | 642 × 780.45 | same | 454 × 980.59 | 318 × 1516.33 |

**The control column** is a `<ul>` at `flex column, gap 8px` holding **four full-width option rows** —
the `seg(on, false)` component that drift 4 ruled is not a segmented control. Fully specified in
§3.3.

**The canvas frame:** `border-radius var(--ks3-r-card)` 22px, `2px solid var(--ks3-ink)`,
`background var(--ks3-card)`, `overflow: hidden`, with the caption **inside** the frame —
`padding 11px 16px`, `border-top 2px solid var(--ks3-rule)`, `background var(--ks3-band)`, MONO 14px
`--ks3-ink-muted`. Caption text is `CELLS[].caption`; `aria-label` is `CELLS[].alt` and the canvas
carries `role="img"`.

**The tuning readout** — `margin-top 16px`, `padding 22px 24px`, `--ks3-r-panel` 20px,
`background --ks3-inset` #F7EFE1, `2px solid --ks3-ink`:

| Element | Measured |
|---|---|
| "Its job" label | MONO 14px/500, `letter-spacing .07em`, uppercase, `--ks3-ink-muted` |
| `cellJob` | 21px/700, lh 1.4 |
| `cellWhere` | 18px, lh 1.6, `--ks3-ink-body` |
| tuning rows (3) | `flex, gap 12px, align-items flex-start`, `padding 14px 16px`, `--ks3-r-panel` 20px, `background --ks3-card`, `2px solid --ks3-rule-strong` #C3B191 |
| dial chip | `flex: 0 0 74px` (measured 74 × 33.19), `padding 5px 0`, `border-radius 8px`, MONO 12px/500 `.08em`, `2px solid --ks3-ink`, `color --ks3-ink` |
| `t.part` | 18px/700 |
| `t.why` | 18px, lh 1.55, `--ks3-ink-body` |
| "The problem it solves:" | `margin-top 18px`, `padding-top 16px`, `border-top 2px --ks3-rule`, 19px/1.6, the label in `--ks3-font-display` |

**The dial is the one genuinely new semantic device on the page.** Six authored values, each with a
token ground, measured live on two cells:

| Dial | Ground token | Measured | Meaning in the content |
|---|---|---|---|
| `GONE` | `--ks3-alert-tint` | #FFF3D4 | a part the cell destroyed (red blood cell's nucleus) |
| `NONE` | `--ks3-alert-tint` | #FFF3D4 | a part never built (root hair's chloroplasts) |
| `HALF` | `--ks3-alert-tint` | #FFF3D4 | a part deliberately incomplete (sperm nucleus) |
| `MORE` | `--ks3-accent-tint` | #FCE7DE | turned up (mitochondria) |
| `EXTRA` | `--ks3-accent-tint` | #FCE7DE | a structure added (nerve's fatty sheath) |
| `SHAPE` | `--ks3-band` | #F4E9D8 | the whole cell reshaped |

R2 is satisfied and then some — **every state carries a word, and the word is the state**. But note
the collapse: six dials map to **three** grounds, so the tint alone does not identify the dial. That
is correct (the tint means *lost / gained / reshaped*) but it must be specified as a three-value
`polarity` derived from a six-value `dial`, not as six colours. §7.2.

**One asymmetry, measured.** `EXTRA` is used once, for the nerve cell's fatty sheath, and its `part`
field reads `'Fatty sheath'` with **no number** — where every other tuning row names a numbered part
from last lesson (`'Nucleus (3)'`, `'Mitochondria (4)'`, `'Chloroplasts (7)'`, `'Whole cell'`). So
the page's own claim — *"Nothing on the parts list is new"* (`#s-think`, line 251) — is contradicted
by one row of its own instrument, which adds a structure that is not on the seven-part list. **This
is science/editorial and it is Mide's call, not Code's** (§8(b)). It is not a rendering problem: both
sentences are authored, both are lifted byte-identical, and the generator will reproduce the tension
exactly as delivered.

---

### 3.3 ⭐ The full-width option row — drift 4's third variant, specified

`00-delivery-drift.md` ruled that this page's `seg()` light branch is **not a segmented control**:
it is a full-width option row and it needs its own registry component. This is that specification,
and it answers the task's item B including its "check rather than assume" clause.

Source, lines 973–975:

```js
'width:100%;text-align:left;cursor:pointer;font:inherit;padding:12px 14px;min-height:56px;' +
'border-radius:var(--ks3-r-option);border:2px solid ' +
  (on ? 'var(--ks3-accent)' : 'var(--ks3-option-border)') +
';background:' + (on ? 'var(--ks3-accent-tint)' : 'var(--ks3-ground)') +
';color:var(--ks3-ink);'
```

#### 3.3.1 What it is used for

**Exactly one thing: the four cell-picker rows in `#s-tuned`'s control column.** Nothing else on the
page calls `seg(x, false)`. The dark branch `seg(x, true)` is called for the two sabotage tabs in
`#s-break` and *is* a segmented control (§3.4).

#### 3.3.2 Geometry at all four viewports

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| width | **232** | 232 | 232 | **318** |
| height | 72.05 | 72.05 | 72.05 | 72.05 |
| padding | 12px 14px | 12px 14px | 12px 14px | 12px 14px |
| min-height | 56px | 56px | 56px | 56px |
| border-radius | 16px (`--ks3-r-option`) | 16 | 16 | 16 |
| border width | 2px | 2px | 2px | 2px |
| text-align | left | left | left | left |
| display | `inline-block` | same | same | same |
| list gap | 8px | 8px | 8px | 8px |

Width is **not** a property of the component — it is `width:100%` inside the bench grid's control
column, so it is 232px wherever the grid is two-column and the full collapsed width at 390. Height is
72.05 at every viewport because the two-line content exceeds the 56px floor; **56px is a floor that
this page's content never touches**, which matters for the registry (a ±1px assertion on height will
be measuring the content, not the component).

#### 3.3.3 Every state, measured

| State | ground | border | name | tag |
|---|---|---|---|---|
| **resting** | `--ks3-ground` #FBF3E6 | `2px --ks3-option-border` #DDCFB6 | `--ks3-ink` 17px/700 lh 1.25 | `--ks3-ink-muted` #5F564F |
| **chosen** (`aria-pressed="true"`) | `--ks3-accent-tint` #FCE7DE | `2px --ks3-accent` #E4572E | unchanged | **`--ks3-accent-text` #A93411** |
| spent | **does not exist** | — | — | — |
| disabled | **does not exist** — measured `disabled: false` on all four, `opacity: 1`, `cursor: pointer` in both states | — | — | — |
| focus ring | see below | — | — | — |

Internal composition, measured through `sc-interp` wrappers via `button.children[n]`:

- child 0 — the cell name: `display:block; font-size:17px; font-weight:700; line-height:1.25`
  (21.25px).
- child 1 — the tag: `display:block; margin-top:2px`, MONO **13px/500**, `letter-spacing .04em`
  (0.52px), `text-transform: uppercase`, colour **carries the state** (`--ks3-accent-text` when
  chosen, `--ks3-ink-muted` otherwise). Content: "In your blood" · "In a plant root" · "A sex cell" ·
  "In your nervous system".

**Truth of state is `aria-pressed`**, measured flipping `['true','false','false','false']` →
`['false','true','false','false']` on a click. Exactly one row is pressed at any time — this is a
single-select radio group wearing button clothes, with no `role="radiogroup"` and no arrow-key
handling. Accessibility note, §8(a).

**Focus ring: measured, and it took a real key event.** `getComputedStyle` after a programmatic
`.focus()` reports `outline-style: none`, because Chrome does not match `:focus-visible` for scripted
focus — which is a trap for any parity probe. Driving a genuine `Input.dispatchKeyEvent` Tab through
CDP instead gives `element.matches(':focus-visible') === true` and:

```
outline: rgb(228, 87, 46) solid 3px;   /* --ks3-accent */
outline-offset: 2px;
```

Identical to b1-03's measurement of the KS3 focus ring, and the option row adds no override of its
own. Note that a `:focus-visible` **rule** search over `document.styleSheets` returns zero hits — the
declaration is not reachable by rule enumeration through the `_ds` bundle, so the ring must be probed
by behaviour, never by reading the cascade.

#### 3.3.4 Is it just the generator's `.ks3-option` under a different name?

Checked rather than assumed, by measuring `.ks3-option` on the generated page at 1280:

| Property | Design's option row (`seg(x,false)`) | Generator's `.ks3-option` | Same? |
|---|---|---|---|
| ground, resting | `--ks3-ground` #FBF3E6 | `--ks3-ground` #FBF3E6 | ✔ |
| border, resting | `2px --ks3-option-border` #DDCFB6 | `2px --ks3-option-border` #DDCFB6 | ✔ |
| ground, chosen | `--ks3-accent-tint` #FCE7DE | `--ks3-accent-tint` #FCE7DE | ✔ |
| border, chosen | `2px --ks3-accent` #E4572E | `2px --ks3-accent` #E4572E | ✔ |
| border-radius | `--ks3-r-option` 16px | `--ks3-r-option` 16px | ✔ |
| width / text-align | 100% / left | 100% / left | ✔ |
| state carrier | `aria-pressed` | `aria-pressed` | ✔ |
| **padding** | **12px 14px** | **16px 18px** | ✗ |
| **min-height** | **56px** | **44px** (`--ks3-tap`) | ✗ |
| **display** | `inline-block`, no gap | `flex`, `gap: 14px`, `align-items: center` | ✗ |
| **font** | `font: inherit` → 19px/400, overridden per child (17/700 + 13 MONO) | 18px/600 on the button, `.ks3-opt-label` 18px/600 | ✗ |
| **leading mark** | none | `.ks3-opt-mark` 28×28, r9, `--ks3-band` ground, 15px/800, `flex: 0 0 28px` | ✗ |
| resting height at 1280 | 72.05 | 64.00 | ✗ |

**The honest answer is: it is the generator's option button, re-clothed — and that is the cheaper
finding, but it is still a distinct registered component.** The entire colour system is identical in
both states: four token values, same four, same roles. What differs is (a) box metrics — 12/14 vs
16/18 padding and a 56px vs 44px floor, which the ±1px registry cannot treat as the same component —
and (b) internal composition: two stacked lines with a state-carrying MONO tag, instead of one flex
row with a letter chip and a single label.

The practical consequence for the rebuild is small and worth stating: **do not build a new component
from scratch.** Register it as a **variant of the existing option button** — `.ks3-option` plus a
modifier that sets `padding: 12px 14px; min-height: 56px; display: block` and swaps the
`.ks3-opt-mark` + `.ks3-opt-label` pair for a `name` + `tag` pair. Every colour, radius, border and
state rule is inherited unchanged. One new component row in `ks3_parity.COMPONENTS` (two, if resting
and chosen are registered separately, which §10.2's `check` row precedent suggests they are), not a
new family of them.

And it is **categorically not** the segmented control drift 4 ruled from b1-06 (17px/700,
`11px 17px`, 44px, `--ks3-r-control` 14px, auto width). Nothing about the two is shared except the
helper's name and its colour tokens. Generating one from the other would produce the wrong control in
both places, exactly as drift 4 said.

#### 3.3.5 Drift 1 and drift 2 on this page, confirmed against measurement

- **Drift 1 (bench control column).** Source line 20 declares `minmax(0, 232px)`; measured
  `232px 642px` at 1280 and 1340. **232px is what this page renders**, and drift 1's ruled value is
  232px, so applying the ruling is a no-op here and moves b1-03 by 8px. Confirmed, no contradiction.
  Note that this page *also* carries the separate options-grid `repeat(auto-fit, minmax(232px, 1fr))`
  at line 217 (`#s-rule`'s card grid), which drift 1 correctly identified as a second component —
  measured **3 columns of 287.328px at 1280**, not the 4 the source's four cards might suggest.
- **Drift 2 (collapse breakpoint).** Source line 21 declares `max-width: 780px`; bisected live:
  **781 → `232px 415px` (two columns), 780 → `668px` (one column)**. So 780 is real on this page and
  **at 820 this page still renders a two-column bench** (`232px 454px`, canvas squeezed to 450px
  CSS). ⚑ **Adopting drift 2's ruled 820px is therefore a visible change to this approved page**, not
  only to b1-06 — at 800px it would go from a 232px control column beside a ~470px canvas to a full
  318px-wide stacked layout. Drift 2 argued exactly this as the kinder outcome and it holds up
  against measurement: at 820 the canvas here is 450 × 280 CSS, drawn from an 1800 × 1120 buffer.
  Nothing I measured contradicts the ruling; I record only that its cost lands on this page too.

---

### 3.4 `#s-break` — "Take the adaptation away", the sabotage-and-consequence engine

Design's dark `ks3-practical` (`--ks3-ink` ground, `6px 6px 0 --ks3-blue` #2F5CE0 shadow, r30,
padding 32px) and the second new instrument. It is where SYSTEM earns its name: break one part, and
follow the failure **outward through three scales**.

**Head row:** `flex, align-items flex-end, justify-content space-between, gap 20px, flex-wrap wrap`
carrying eyebrow + `<h2>` on the left (34px, lh 1.12, `letter-spacing −.03em` → measured −1.02px,
`--ks3-on-dark`) and the progress line on the right (MONO 15px/500 `--ks3-on-dark-muted`, reading
`"N of 8 sabotages run"`). Lede at 19px/1.65 `--ks3-on-dark-body`, `max-width 58ch`, with the current
cell name in `<strong style="color: var(--ks3-on-dark)">`.

**The sabotage tabs — this is a real segmented control**, `seg(on, true)`, and drift 4's note that
*"the dark branch is byte-identical in all four pages"* is confirmed by measurement here:

| State | ground | border | colour | geometry |
|---|---|---|---|---|
| on | `--ks3-alert` #FFC53D | `2px --ks3-alert` | `--ks3-ink` | `padding 11px 17px`, `min-height 44px`, r14 = `--ks3-r-control`, 17px/700 |
| off | `transparent` | `2px --ks3-on-dark-muted` #C6B9A7 | `--ks3-on-dark` #FBF3E6 | identical |

Widths are content-driven (measured 168.64 and 213.78 at 1280) in a `flex, gap 9px, flex-wrap wrap`
row. **Two tabs per cell, always** — every one of the four cells has exactly 2 sabotages.

**The sabotage panel:** `--ks3-dark-panel` #3E3730, `padding 22px 24px`, `--ks3-r-panel` 20px, MONO
14px `.07em` uppercase `--ks3-on-dark-muted` label ("The sabotage") over `sab.what` at 21px/1.5/700
`--ks3-on-dark`.

**The predict gate** is a `.ks3-commit` + `.ks3-options` pair using the **standard dark-block
`.ks3-option`** — measured 896 × 64.8, `padding 16px 18px`, `min-height 44px`, r16, `2px
--ks3-on-dark-muted`, ground `--ks3-dark-panel`, 18px/600 `--ks3-on-dark`, `gap 14px`, in a
`flex column, gap 11px` list. So the predict gate needs **no new component** — it is the registered
dark option, and its 3 options come from `sab.predict`.

**On answering, three things happen at once** (measured):

1. `predictOpen` goes false → **the gate leaves the DOM entirely**. b1-01's **F4 reproduces**: the
   student cannot see or revise what they predicted…
2. …except that this page **fixes F4 halfway**: `yourPickLine` renders `"You said: " + sab.predict[picked]`
   as a MONO 15px `--ks3-on-dark-muted` line above the chain. Measured: *"You said: It has less
   surface, and it can no longer fold through narrow vessels"*. The choice is **echoed but not
   revisable and not marked** — there is no `correct` field on any predict option, so R3 is respected.
   This is the first partial answer to F4 in the B1 inventory and the generator should carry it.
3. `chainOpen` goes true → the broken canvas, the chain and the close panel arrive inside a
   `[data-arrive="1"]` wrapper (0.34s `b4-arrive` translate-6px + fade, killed under
   `prefers-reduced-motion`).

**The consequence chain** — an `<ol>` at `flex column, gap 12px`, three rows, measured at 1280:

| Row | ground | border | padding | radius |
|---|---|---|---|---|
| 1 ("The cell") | **`--ks3-band` #F4E9D8** | **`2px --ks3-ink`** | 18px 20px | `--ks3-r-panel` 20px |
| 2 (the middle scale) | `--ks3-ground` #FBF3E6 | `2px --ks3-rule-strong` #C3B191 | 18px 20px | 20px |
| 3 ("The whole body" / "The outcome") | `--ks3-ground` | `2px --ks3-rule-strong` | 18px 20px | 20px |

Each row: a MONO 13px/500 `.08em` uppercase `--ks3-ink-muted` scale label, then 19px/1.55
`--ks3-ink` text. **The rows are light-on-dark islands** — cream panels inside an ink block — which
is why they carry `--ks3-ink` text rather than `--ks3-on-dark`. Row 1 is emphasised by ground and
border, and the emphasis is **positional (`i === 0`), not semantic**: it always means "the cell",
because every chain in the data starts at the cell.

**The close panel:** `padding 18px 20px`, `--ks3-r-panel`, `--ks3-dark-panel` ground, 19px/1.6
`--ks3-on-dark-body`.

**⚑ The `namedConditions` prop is a content switch, and it is Mide's.** Every sabotage carries
**two** closing paragraphs, `close` and `closeSafe`, selected by
`safe = this.props.namedConditions === false`. Three of the eight pairs differ:

| Cell · sabotage | `close` names | `closeSafe` says instead |
|---|---|---|
| red · sphere | **hereditary spherocytosis** | "There are real inherited conditions in which red cells come out round and stiff…" |
| nerve · sheath | **multiple sclerosis** | "Speed here is not a bonus; it is the difference between catching yourself as you trip and hitting the floor." |
| the other six | — | identical strings |

Default is `namedConditions: true`, i.e. **the named-condition text ships by default**. This is a
real editorial/safeguarding decision that §4.8 has no field for, it is not Code's to take, and the
generator cannot express it today. Gap G9, §8(b).

**The broken canvas, measured** (a first probe indexed `#s-break`'s canvases from 1 when the section
holds only one — the cell canvas lives in `#s-tuned` — and was re-run):

| Property | Value |
|---|---|
| buffer | **1800 × 840** |
| CSS box at 1280 | **892 × 416.27** (frame 896 inner, less its 4px border) |
| device px per CSS px | **2.018** → crisp at 1× and 2×, matching `#s-tuned`'s canvas |
| frame | `2px solid --ks3-on-dark-muted` #C6B9A7, `--ks3-r-card` 22px, `overflow: hidden` |
| caption strip | inside the frame: `--ks3-dark-panel` #3E3730 ground, `border-top 2px --ks3-on-dark-muted`, `padding 11px 16px`, MONO 14px `--ks3-on-dark-muted` |

So the dark canvas is the light one's exact twin — same frame geometry, same inside-the-frame caption
strip, same 2× buffer discipline — with every colour swapped to its on-dark counterpart. **One
component with a ground variant**, not two components.

---

### 3.5 `#s-rule` — the statement panel, and drift 3

An unclassed `<section>` whose whole appearance is inline: `background var(--ks3-band)`,
`border 3px solid var(--ks3-ink)`, `border-radius var(--ks3-r-block)` 28px, `padding 34px 32px`,
`margin 28px 0 0`.

| Part | Measured |
|---|---|
| eyebrow | `.ks3-eyebrow` overridden to `color: var(--ks3-accent-text)`; text "What settles it" |
| statement | `--ks3-font-display` 800, `font-size: clamp(28px, 3.9vw, 44px)`, lh 1.08, `letter-spacing −.03em`, `max-width 24ch` |
| sub-line | 19px/1.6, `max-width 56ch`, `--ks3-ink-body` |
| card grid | `repeat(auto-fit, minmax(232px, 1fr))`, gap 14px |
| card | `--ks3-card`, `2px --ks3-ink`, `--ks3-r-card` 22px, `padding 20px 22px` |
| card label | MONO 14px/500 `.07em` uppercase `--ks3-accent-text` — "Problem 1".."Problem 4" |
| card title | display 800, 23px, lh 1.2, `−.02em` |
| card body | 18px/1.55 `--ks3-ink-body` |
| card footer | MONO 15px/500 `--ks3-ink-muted` — the example cells |

**Statement type, measured across the four viewports** (drift 3's ruled value is this page's own
declaration, so this is the ruling's reference measurement):

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| computed font-size | **44px** (capped) | 44px | **31.98px** (3.9vw) | **28px** (floored) |
| line-height | 47.52 | 47.52 | 34.54 | 30.24 |
| rendered box width | 678.25 | 678.25 | 501.53 | 288 (clipped by the 288px column) |

Drift 3 ruled `clamp(28px, 3.9vw, 44px)` and this page is one of the two that already declare it.
**Confirmed, no contradiction.** Its consequence for b1-05 (30px → 44px) is unchanged by anything
measured here.

**The four problem cards are static markup, not data** (lines 217–242). That matters for §7: this is
the one substantial content payload on the page that is *not* in the `<script>` block, so a
byte-identical lift must take it from the markup.

**Card grid measured at four viewports:** 3 columns of 287.328px at 1280 and 1340 (four cards →
3 + 1, the fourth alone on row 2), 2 × 344px at 820, 1 × 288px at 390. ⚑ **A four-card grid that
renders 3-up leaves an orphan card at every desktop width.** With drift 1's other declaration
(240px) it would still be 3-up at 1280. Whether Design intends the 3+1 or wants 2×2 is **not
determinable from the delivery** — it is one number (`minmax`) and it is Design's call. §8(a).

---

### 3.6 `#s-think` — one misconception block, two misconceptions

`.ks3-block ks3-misconception`: `--ks3-alert-tint` #FFF3D4, `2px --ks3-ink`, r28, `5px 5px 0
#221E1B`, padding 30px. Shape confirmed identical to b1-03 §3.6, with **two quote/answer pairs
inside one block**, separated by an inline divider: `margin-top 22px; padding-top 20px; border-top
2px solid var(--ks3-alert-border)` (#D9821A).

One measured detail the generator must not lose: **the two quotes render at different sizes.** The
first `.ks3-mis-quote` measures **19px/700** and the second **22px/700**, because
`shared/ks3.css` sizes the first-of-type differently from a subsequent one inside a nested `<div>`.
Both are Instrument Sans 700 `--ks3-ink`; the first carries `margin-top: 15px`, the second is reset
to `margin-top: 0` inline. Whether the 19/22 split is intended is **not determinable** — it falls out
of CSS specificity rather than being authored. §8(a).

The two misconceptions:

1. *"Specialised cells are made of different parts from ordinary cells."* — the CELL-family
   misconception this lesson exists to kill.
2. *"A red blood cell is not really a cell, then."* — the misconception this lesson's **own hook
   creates**, answered in the same block. See §4.4 on the B1-04/B1-06 contract.

### 3.7 The KEY FACT box, specified to generate

One box, top-level, unclassed, `margin-top: 24px`, measured at 1280:

| Property | Value | Token |
|---|---|---|
| ground | #F4E9D8 | **`--ks3-band`** — drift 5 confirmed, this page is one of the five |
| border | 2px solid #221E1B | `--ks3-ink` |
| radius | 20px | `--ks3-r-panel` |
| shadow | `5px 5px 0 #E4572E` | **`--ks3-accent`** |
| padding | 18px 22px | new |
| box | 960 × 127.17 (1280) · 772 × 127.17 (820) · 358 × 186.55 (390) | full lesson width |
| label | "Key fact", MONO 13px/500, `letter-spacing .09em` (1.17px), uppercase, `--ks3-accent-text` #A93411 | |
| body | display 700, 22px, lh 1.35, `−.015em`, `--ks3-ink` | |

Drift 5 noted that `--ks3-band` is also the ground a **chosen-wrong** ladder option takes, and that
the KEY FACT box must therefore never grow anything that reads as a mark. Confirmed safe here: no
badge, no icon, no border colour in common — the wrong option takes `2px --ks3-ink` with no shadow,
the KEY FACT takes `2px --ks3-ink` **with a 5px accent shadow**, and the shadow is the discriminator.
Worth pinning as an assertion.

**Because the box is full lesson width and unclassed, it sits *outside* every block shell** — it is a
sibling of the sections, not a child of one. b1-03 put its two inside `#s-think`; b1-01 put its one at
top level. Finding F19 needs one answer.

### 3.8 The ladder, the stretch layer and the endmatter

**`#s-ladder`** is `class="ks3-ladder"` (single class, hence F17's 57.6px heading) with the standard
4-rung shape: 2 page-marked rungs from `RUNGS`, 2 self-marked from `SELF_RUNGS`, `.ks3-retry-wrap`.
Every state measured and every one matches the registered components exactly:

| State | ground | border | text |
|---|---|---|---|
| resting | `--ks3-ground` #FBF3E6 | `2px --ks3-option-border` #DDCFB6 | `--ks3-ink` 18px/600 |
| CHOSEN-CORRECT (`.is-correct`) | **#E4F7EB** | `2px #12A150` | `--ks3-ink` |
| CHOSEN-WRONG (`.is-wrong`) | **`--ks3-band` #F4E9D8** | `2px --ks3-ink` | `--ks3-ink` |
| SPENT (`.is-spent`) | **`--ks3-row-dim` #FBF6EC** | `2px #EBDFCB` | **#6E655D** |
| all answered | `disabled`, `cursor: default` | | |

Feedback: `.ks3-feedback.is-wrong` = `--ks3-band` on `2px --ks3-ink`, r15, `padding 14px 18px`, 19px,
opening on the word "Not this one." followed by the chosen option's `correction`;
`.ks3-feedback.is-correct` = #E4F7EB on `2px #12A150`, text "Correct." with no trailing prose
(`feedbackText` is `''` on a right answer). Ticks: 4 per self-rung; tally
`"0 of 4 ticked — not yet."` on `--ks3-band` `--ks3-ink-body`, flipping to
`"All 4 ticked — rung met."` on #E4F7EB #0A6B36 with `.is-met`. Score line
`"You got N of 4."` + `"You marked rungs 3 and 4 yourself."`.

**Retry, measured:** `onRetry` sets `{answers:{}, checked:{}, ticks:{}}` — score returns to
"You got 0 of 4.", both feedback paragraphs and both tick lists leave the DOM, and **the textarea's
value survives** (measured `''` because I never typed, but `text` is deliberately not cleared and the
retry note says so: *"Clears the ticks on rungs 3 and 4 and keeps what you wrote."*). ⚠️ The note
under-describes what the button does: it also **clears rungs 1 and 2 entirely**, re-enabling both
page-marked rungs and discarding their marks. The button is labelled "Retry my misses" and it in fact
retries the hits as well. Finding F23 — a copy/behaviour mismatch, and under standing law *the page
wins*, so the generator reproduces both the button's behaviour and its inaccurate note. Flagged for
Design rather than fixed.

**`.ks3-layer`** — one bare `<p>` in a `.ks3-layer-body` (`--ks3-stretch-tint` #F0EAFC, `2px
--ks3-stretch` #6B3FD4, r26, `padding 26px 28px`). The generator's equivalent nests two blocks inside
it (b1-03's D10, reproduced).

**`.ks3-endmatter`** — 4 cards, `3 × 309.328px` grid, gap 16px; heads "Before this lesson" ·
"Connects to" · "At GCSE this becomes" · "Ask Mr Badmus AI". Third card is **prose**. Tutor CTA is a
live `<a href="#s-rule">` at 18px/600, r12, `--ks3-card` on `--ks3-accent-text`.

---

## 4. Interactive behaviours

Eleven, each with its trigger. All measured live unless marked.

| # | Behaviour | Trigger | Effect |
|---|---|---|---|
| B1 | **Hook commit** | click one of 4 `.ks3-option` | `hookChoice` set; option border → `--ks3-alert`; `.ks3-reveal` arrives (`--ks3-dark-panel`, `2px --ks3-alert`, r18, `padding 18px 20px`, `mt 18px`, `b4-arrive` animation); rail stage 1 ticks. **Never marked** — R3 respected, no `correct` field exists |
| B2 | **Cell select** | click one of 4 option rows | `cell` set, `seen[id]` set; canvas repaints; the whole readout (job/where/3 tuning rows/problem) swaps; `#s-break`'s tabs, sabotage, predict and chain all swap with it |
| B3 | **Rail stage 2** | 4 distinct cells seen | TUNED chip → accent + tick |
| B4 | **Sabotage select** | click one of 2 dark segments | `sab[cellId]` set; the sabotage panel text swaps; if that (cell, sabotage) pair was already predicted, its chain returns; otherwise the predict gate returns |
| B5 | **Predict** | click one of 3 dark `.ks3-option` | `predict[cell:sab]` set; gate leaves the DOM; broken canvas + "You said:" + 3-row chain + close panel arrive under `[data-arrive]`; progress counter increments |
| B6 | **Rail stage 3** | 4 distinct (cell, sabotage) predictions | BREAK chip → accent + tick, while the block's own counter still reads "4 of 8" (F21) |
| B7 | **Ladder mark** | click a `.ks3-option` in rung 1 or 2 | chosen → `.is-correct` or `.is-wrong`, the true answer always → `.is-correct`, the rest → `.is-spent`, all four `disabled`; feedback paragraph arrives with `role="status"`; score recomputes. **First click locks** (`if (a[r.id] !== undefined) return null`) |
| B8 | **Self-mark** | click "Check my answer" | 4 criteria checkboxes + tally arrive; tally recomputes on each toggle; a rung scores only at 4 of 4 |
| B9 | **Retry** | click "Retry my misses" | clears `answers`, `checked`, `ticks`; keeps `text` (F23) |
| B10 | **Rail navigation** | click a side-rail link | `location.hash` set, target lands at **top 92.11px**, `scroll-behavior: auto` |
| B11 | **Rail progress (scroll)** | `IntersectionObserver` `rootMargin: '-45% 0px -50% 0px'` on the 4 rail sections | sets `active`; drives the top bar's count, label and fill — **not** completion (F2) |

**Two behaviours the page does *not* have**, both worth recording because their absence is a design
statement: **no locked/veiled instrument** (§3.1.5) and **no revision of any answer** except the
ladder's retry. Once a cell's sabotage is predicted, that prediction is permanent for the session.

**Settle trap:** as b1-02 recorded, the DC runtime hydrates asynchronously and repaints canvases on
`document.fonts.ready`. Every measurement above used `settle ≥ 0.35s` after each click; probes that
read immediately will catch the pre-hydration DOM.

---

## 5. Schema gaps against `docs/ks3/architecture.md` §4.8

§4.8 is authoritative: *"Fields not listed here do not exist without an amendment to this document."*

### 5.1 Already covered by §4.8

`slug` · `title` · `discipline` · `unit` · `family` (SYSTEM) · `big_question` · `phenomenon` (the
hook prose) · `misconceptions` (both of `#s-think`'s) · `ladder` (all four rungs, criteria, retry) ·
`key_note` · `review_state` (drives `.ks3-review-flag`) · `requires` (the "Before this lesson" card) ·
`references` (the "Connects to" card) · `ks4_links` (the "At GCSE" card) · `stretch` (the layer).

### 5.2 Gaps — 13, of which 9 are new to this page

| # | Gap | Needed by | New here? |
|---|---|---|---|
| **G1** | `rail` — a list of `{anchor, short, label, done_when}` **plus a `threshold`** for count-based stages | §2.4 | shared (b1-01), **threshold is new** |
| **G2** | `anchor` / `scroll-margin-top` on every block — §4.8 has no per-block id | §2.3 | shared (b1-01/b1-03) |
| **G3** | `key_fact` — a first-class field, with a **position** (inside a block, or a top-level sibling) | §3.7, F19 | shared, position clause new |
| **G4** | `statement` block — the `#s-rule` panel: eyebrow + display statement + sub-line + N cards of `{label, title, body, examples}` | §3.5 | shared (b1-03), **card shape differs** |
| **G5** | **`system_bench`** — the `#s-tuned` instrument: a list of specimens, each `{id, name, tag, job, where, problem, caption, alt, tuning: [{dial, part, why}]}` | §3.2 | **new** |
| **G6** | **`dial`** vocabulary — a six-value enum (`GONE`/`NONE`/`HALF`/`MORE`/`EXTRA`/`SHAPE`) collapsing to a three-value polarity for colour | §3.2 | **new** |
| **G7** | **`sabotage`** — per specimen, a list of `{id, label, what, predict: [3], caption, alt, chain: [{scale, text}], close, closeSafe}` | §3.4 | **new** |
| **G8** | **`chain`** — the three-scale consequence ladder, with row 1 emphasised positionally | §3.4 | **new** |
| **G9** | **`named_conditions`** — the editorial switch selecting `close` vs `closeSafe` | §3.4 | **new**, and it is Mide's, §8(b) |
| **G10** | **`drawing`** — §4.8's `figures` carries `{id, kind, caption, status}` for a *pending slot*; this page needs a **live canvas kind** with a data-driven routine, a light and a dark palette variant, and a sabotaged state per specimen | §3.1.5 | **new** |
| **G11** | **`legal`** — three answers now exist for one slot (copyright / lesson safety line / nothing) | §1.4, D8 | shared (b1-03), **third value new** |
| **G12** | `tutor_prompt` + `tutor_anchor` — Design authors both the tutor card's line and an in-page href | §3.8 | shared (b1-01 F12) |
| **G13** | **`hook_options`** — the hook's 4 unmarked commitment options and its gated reveal text | §4 B1 | **new** (b1-03's hook options were in the same shape but its gap list folded them into `phenomenon`) |

**`activities` cannot carry G5–G8.** §5.5's activity families describe marked or self-marked tasks;
the bench and the sabotage engine are neither. They are instruments, and §4.8 has no field for an
instrument with its own content payload.

---

## 6. Measurements

Every number in this file was read from the browser. This section is the subset that a parity
assertion would pin, split by whether it traces to a token.

### 6.1 Traces to a token

All 37 `--ks3-*` custom properties probed on `.rd[data-mode="ks3"]` resolved to their
`shared/ks3.css` values. Spot-check of the ones this page's new components depend on:

| Token | Value | Used by |
|---|---|---|
| `--ks3-ground` | #FBF3E6 | option row resting, chain rows 2–3 |
| `--ks3-card` | #FFFCF5 | canvas frame, tuning rows, `#s-rule` cards |
| `--ks3-band` | #F4E9D8 | KEY FACT, chain row 1, caption strip, SHAPE dial |
| `--ks3-inset` | #F7EFE1 | tuning readout |
| `--ks3-ink` | #221E1B | every 2–3px border, dark grounds |
| `--ks3-ink-body` | #3B342E | body prose |
| `--ks3-ink-muted` | #5F564F | MONO captions, resting tag |
| `--ks3-ink-ghost` | #9A8F86 | future rail chip |
| `--ks3-accent` | #E4572E | chosen border, done chip, KEY FACT shadow |
| `--ks3-accent-text` | #A93411 | chosen tag, card labels, KEY FACT label |
| `--ks3-accent-tint` | #FCE7DE | chosen ground, MORE/EXTRA dial |
| `--ks3-alert` | #FFC53D | sabotage tab on, hook reveal border |
| `--ks3-alert-tint` | #FFF3D4 | GONE/NONE/HALF dial, misconception ground |
| `--ks3-alert-border` | #D9821A | `#s-think`'s internal divider |
| `--ks3-on-dark` / `-body` / `-muted` | #FBF3E6 / #E7DECE / #C6B9A7 | dark blocks |
| `--ks3-dark-panel` | #3E3730 | sabotage panel, close panel, dark options |
| `--ks3-rule` / `-strong` | #E0D2B9 / #C3B191 | caption borders, tuning row borders |
| `--ks3-option-border` | #DDCFB6 | option row resting border |
| `--ks3-blue` | #2F5CE0 | `#s-break`'s shadow |
| `--ks3-stretch` / `-tint` | #6B3FD4 / #F0EAFC | layer |
| `--ks3-row-dim` | #FBF6EC | SPENT option |
| `--ks3-r-block/card/panel/option/control` | 28 / 22 / 20 / 16 / 14 px | all |
| `--ks3-tap` | 44px | ladder options, sabotage tabs |
| `--ks3-page` / `--ks3-wide` | 1320px / 60rem | page shell |

### 6.2 New measurements — px values not expressed as a token

| Value | Where | Note |
|---|---|---|
| `232px` control column | bench grid | drift 1's ruled value |
| `780px` collapse | bench grid | drift 2 rules 820 against it |
| `1340px` | rail swap | shared across all pages |
| `92px` scroll-margin | all 7 anchors | shared |
| `104px` rail width, `150px` rail top, `calc(50% − 632px)` | side rail | shared |
| `96px / 8px / 99px` track, `2px` border | top bar | shared |
| `32px / 10px` rail chip | side rail | shared |
| **`12px 14px` padding, `56px` min-height** | **option row** | **new — the whole of drift 4's third variant** |
| `17px/700 lh 1.25` + `13px MONO .04em` | option row children | new |
| `74px` dial chip, `8px` radius, `12px/.08em` | tuning dial | new |
| `14px 16px` padding, `12px` gap | tuning row | new |
| `18px 20px` padding, `12px` gap | chain rows | new |
| `18px 22px` padding, `5px 5px 0` shadow | KEY FACT | new |
| `34px 32px` padding, `3px` border | `#s-rule` | new |
| `minmax(232px, 1fr)`, `14px` gap | `#s-rule` card grid | new, and 3-up (§3.5) |
| `24ch / 56ch / 54ch / 58ch` | prose measures | new |
| `1800×1120` and `1800×840` buffers, 900×560 design space, `setTransform(2,…)` | canvases | new |
| `0.34s` `b4-arrive`, translateY 6px | arrival animation | new |
| `24px` margin-top | KEY FACT only | **anomalous** — every sibling uses 28px or 34px |

### 6.3 Not measured

1. **The `railLabels` prop's effect.** It is declared in `data-props` (boolean, default true,
   section "Progress rail") and **never read anywhere in the script** — grep of the whole file finds
   it only in the props declaration. It is a dead prop. Whether Design intended a labels-off rail
   variant is unknown and cannot be tested. §8(a).
2. **`startCell` values other than `red`.** The prop is an enum of the four cell ids and I did not
   override the `data-props` payload; the seeding logic at lines 668–669 was read from source.

---

## 7. How to generate each new component from data

Four new components, in descending cost.

### 7.1 The progress rail

Identical to b1-01 §2.6 and b1-03 §2.4. Requires G1 and G2. Emit the two `<nav>` variants, the two
media rules, and `scroll-margin-top: 92px` on every id-bearing section. `done_when` must support a
threshold (F21).

### 7.2 `system_bench` — `#s-tuned`

```python
{"type": "system-bench",
 "specimens": [
   {"id": "red", "name": "Red blood cell", "tag": "In your blood",
    "job": "...", "where": "...", "problem": "...",
    "caption": "...", "alt": "...",
    "drawing": "red",                      # names a routine, G10
    "tuning": [{"dial": "GONE", "part": "Nucleus (3)", "why": "..."}, ...]},
   ...
 ],
 "start": "red"}                            # the `startCell` prop
```

Renders: the `[data-bench-grid]` two-column shell; a `<ul>` of **option rows** (§7.3) in the control
column; the framed canvas with its inside caption; the readout with N tuning rows. `dial` drives the
chip's word and, via a three-value polarity map, its ground. **Nothing here can be derived** — every
string is authored and every one is science-bearing.

### 7.3 The full-width option row

Per §3.3.4, register it as a **variant of `.ks3-option`**, not a new component:

```css
.ks3-option--row {          /* name is Code's to choose; behaviour is not */
  display: block;
  padding: 12px 14px;
  min-height: 56px;
}
.ks3-option--row .ks3-opt-name { display:block; font-size:17px; font-weight:700; line-height:1.25; }
.ks3-option--row .ks3-opt-tag  { display:block; margin-top:2px;
  font-family: var(--ks3-font-mono); font-size:13px; font-weight:500;
  letter-spacing:.04em; text-transform:uppercase; color: var(--ks3-ink-muted); }
.ks3-option--row[aria-pressed="true"] .ks3-opt-tag { color: var(--ks3-accent-text); }
```

Ground, border, radius and both chosen-state colours inherit from `.ks3-option` unchanged. Data
shape: `{name, tag}` per row plus `aria-pressed` from the bench's current specimen. **Two registry
rows** (resting, chosen) by the precedent §10.2 sets for `check`.

### 7.4 `sabotage` — `#s-break`

```python
{"type": "sabotage",
 "specimen": "red",                         # keyed to the bench's specimens
 "options": [
   {"id": "sphere", "label": "Make it a sphere",
    "what": "...",
    "predict": ["...", "...", "..."],        # 3, never marked (R3)
    "caption": "...", "alt": "...",
    "chain": [{"scale": "The cell", "text": "..."},
              {"scale": "The vessel", "text": "..."},
              {"scale": "The whole body", "text": "..."}],
    "close": "...", "close_safe": "..."},    # G9 selects between them
   ...
 ]}
```

Renders: the head row with its live counter; the dark segmented control (the **existing** dark
segment, drift 4's ruled geometry); the sabotage panel; the predict gate built from the **existing**
dark `.ks3-option`; and, once answered, the dark canvas, the "You said:" echo, the 3-row chain and
the close panel inside `[data-arrive]`. Row 1 of the chain takes the emphasised treatment
positionally. Two new registry rows: `chain row is emphasised` and `chain row is plain`.

### 7.5 The two smaller ones

**KEY FACT box** (G3): `--ks3-band` ground, `2px --ks3-ink`, `--ks3-r-panel`, `5px 5px 0
--ks3-accent`, `padding 18px 22px`, MONO 13px `.09em` `--ks3-accent-text` label + display-700 22px
body. Needs a **position** field until F19 is answered.

**Statement panel** (G4): `--ks3-band`, `3px --ks3-ink`, `--ks3-r-block`, `padding 34px 32px`,
`clamp(28px, 3.9vw, 44px)` display statement at 24ch, 19px sub-line at 56ch, then N cards in
`repeat(auto-fit, minmax(232px, 1fr))` gap 14px. b1-03's version of this block took 2 cards at
`minmax(280px)`; this one takes 4 at `minmax(232px)`. **One `minmax` value must be ruled** the way
drift 1 ruled the bench column — it is the same class of hand-authoring residue and it is not in
`00-delivery-drift.md`. Finding F24.

---

## 8. Ambiguities and findings

Separated by whose call each is.

### (a) Ambiguity for Design — 6

| # | Question |
|---|---|
| A1 | **The 3+1 card grid.** `#s-rule`'s four problem cards render 3-up at every desktop width, orphaning the fourth. Is that intended, or should the `minmax` give 2×2? (§3.5) |
| A2 | **`#s-think`'s two quote sizes.** The first `.ks3-mis-quote` is 19px, the second 22px, and the difference falls out of CSS specificity rather than being authored. Which is right? (§3.6) |
| A3 | **The KEY FACT box's home.** Three pages, three structural positions (top-level orphan / inside the misconception / top-level orphan again), and a 24px margin where every sibling uses 28. (§3.7, F19) |
| A4 | **`railLabels`** is a declared prop that nothing reads. Was a labels-off rail intended? (§6.3) |
| A5 | **The statement panel's `minmax`** — 232px here, 280px on b1-03. One value needed. (F24) |
| A6 | **R4's flip-card clause** still cannot be arbitrated: neither reference screen inventoried so far contains a flip card. (§3.1.2) |
| A7 | **"Retry my misses"** clears rungs 1 and 2 as well as the self-marked ones. Copy or behaviour? (F23) |
| A8 | **The nav brand mark.** Design's 34×34 accent tile with an inverted cream chevron, on both reference screens now, against MRB-197's ruled bare chevron. Design's house style has diverged from Design's own rule. (D2) |

### (b) Science or content — Mide's, and only Mide's — 3

| # | Question |
|---|---|
| S1 | **`namedConditions` ships true.** The default text names **hereditary spherocytosis** and **multiple sclerosis** to Year 7–9 students, with a `closeSafe` alternative already written for both. Which ships? (§3.4, G9) |
| S2 | **The nerve cell's `EXTRA` fatty sheath contradicts the page's own key fact.** `#s-think` and the KEY FACT box both say no specialised cell has a new part; the bench's nerve row adds one that is not on the seven-part list. Both are authored; the tension is in the delivery. (§3.2) |
| S3 | **The B1-04 / B1-06 paired contract (§4.4 below).** Whether the hook's four-part claim is safe to ship without B1-06 in the same release is a content judgement, not a build one. |

### (c) Code's to decide — 3

| # | Decision |
|---|---|
| C1 | **Register the option row as a `.ks3-option` variant**, not a new component (§3.3.4). Cheapest correct answer; nothing about the page changes. |
| C2 | **`done_when` gets a `threshold`** so stage 3's "4 of 8" is expressible (F21). |
| C3 | **The legal slot** needs one rule that admits "absent" as a value (G11, D8). Recommendation: make the field optional and emit nothing when unset, which reproduces all three delivered behaviours. |

### Findings raised on this page

| # | Finding |
|---|---|
| **F19** | The KEY FACT box has taken three structural positions across three pages, and here carries an anomalous 24px margin-top. |
| **F20** | b1-04 has **no legal line at all**, making the slot three-valued. |
| **F21** | Rail stage 3 ticks at 4 of 8 while the block's own counter reads "4 of 8 sabotages run" — a visible disagreement between rail and instrument. |
| **F22** | ⚠️ **Live-site defect, independent of the rebuild.** The generated page's "Connects to" endmatter card renders platform self-explanation to the student: *"Diffusion is owned by C1 (§7.4 ordering: the particle idea is taught in chemistry first)…"* That breaches the §8.10 copy rule and it is shipping today. |
| **F23** | "Retry my misses" also clears the rungs the student got right; its own note says otherwise. |
| **F24** | The statement panel's card `minmax` differs between b1-03 (280px) and b1-04 (232px) — a sixth drift, not in `00-delivery-drift.md`. |

### Findings confirmed from earlier pages

F1 (breadcrumb), F2 (rail top bar shows scroll not completion — **worse at 4 stages**),
F4 (predict gate leaves the DOM — **partially fixed here by the "You said:" echo**),
F12 (tutor CTA is a live anchor with an authored line), F14 (`shared/styles.css` absent → rung `h3`
36.8 vs 26.45), F15 (nav brand tile), F16 (keynote heading element/weight/colour), F17 (ladder `h2`
57.6 vs 43.2). All eight reproduce on a second family's reference screen.

---

## 4.4 ⭐ The B1-04 / B1-06 paired contract (CELL-08)

*(Numbered out of sequence deliberately — this belongs with the content, and it is the one thing in
this file that the register cannot express.)*

MRB-209 §3 records that this page's hook asserts a four-part claim about the red blood cell, and that
B1-06 resolves the apparent contradiction with a bacterium. **The two lessons must change together or
the contradiction returns silently.** Here is this page's half of the fingerprint, verbatim.

**Line 84** — the sentence that carries the contract:

```html
<h2>Last lesson: no nucleus, no instructions, no repair, no dividing.</h2>
```

**Line 85**, which ratifies it and cannot be separated from it:

```html
<p class="ks3-hook-prompt">All still true. And yet: a red blood cell starts out with a nucleus, in the marrow inside your bones, and as it matures it pushes that nucleus out and destroys it. It can then never repair itself and never divide, and it lasts about a hundred and twenty days. Your body does this deliberately, two million times a second.</p>
```

**Precisely which sentence carries the contract:** the `<h2>` at **line 84**. It is the one that
generalises — *no nucleus ⇒ no instructions ⇒ no repair ⇒ no dividing* — as a rule, with no
qualifier. Line 85's "All still true" is what promotes it from a recap into an assertion the lesson
stands behind. Everything downstream depends on it: `#s-think`'s second misconception (line 254–255,
*"A red blood cell is not really a cell, then."*), ladder rung 2's correct option (line 590,
*"…which is why it cannot repair itself and lasts about 120 days"*), and the stretch layer's two
million cells a second (line 346).

**Why B1-06 must move with it.** `CELL-08` in `docs/ks3/misconception-register.md:179` is
*"A single-celled organism is just a simpler version of one of our cells — the same parts, doing
less"*, confronted by `more-not-fewer` and owned by `unicellular-organisms` — B1-06. A bacterium has
**no nucleus and divides perfectly well**, roughly every twenty minutes. Read against line 84 as a
general rule, B1-06 teaches the student that B1-04 was wrong. Read as a claim about *this* cell —
a human cell that had a nucleus and destroyed it — both are true, and the pair is one of the better
teaching moments in the unit.

**What the register cannot express, and why this is recorded here.** The misconception register keys
on `{id, statement, elicited_by, confronted_by, owner}`. It has no way to say *"lesson A asserts a
rule that lesson B qualifies, and the qualification is the point."* There is no field for a
cross-lesson claim/qualification pair, so nothing in the build would notice if B1-04 shipped without
B1-06, or if either lesson's wording were edited independently. Until that field exists, **the
verbatim quote above is the fingerprint**: if line 84's wording changes, B1-06's bacterium passage
must be re-read against it, and vice versa. Whether the pair is safe to ship split is S3 — Mide's.

---

## Provenance

Measured 13 August 2026 on branch `feat/ks3-b1`, in headless Chrome via `ks3_browser.py`
(`Emulation.setDeviceMetricsOverride`), against:

- `docs/ks3/design-reference/b1/b1-04-specialised-cells.dc.html` (1,141 lines, unmodified), served
  over HTTP from `docs/ks3/design-reference/b1/`;
- `mrbadmus_site/ks3/biology/cells-and-organisation/specialised-cells.html` (70 lines, build already
  run), served over HTTP from `mrbadmus_site/`.

Sources read: `docs/ks3/design-coverage-manifest.md` §10.1–10.2, `docs/ks3/architecture.md` §4.8,
`docs/ks3/misconception-register.md`, `shared/ks3.css`, and this folder's `README.md`,
`00-delivery-drift.md` and `b1-03-animal-and-plant-cells.md`.

**All five ruled drifts confirmed against this page's source and its rendered output:** drift 1
(232px, line 20) · drift 2 (780px, line 21 — bisected live at 780/781; the ruled 820 changes this
page, §3.3.5) · drift 3 (`clamp(28px, 3.9vw, 44px)`, line 214) · drift 4 (the light `seg()` branch,
lines 973–975, is the cell-picker row and not a segmented control, §3.3) · drift 5 (`--ks3-band`,
line 260). **No measurement contradicts any of the five rulings.**
