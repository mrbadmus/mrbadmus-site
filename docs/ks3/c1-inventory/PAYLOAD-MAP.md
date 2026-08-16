# C1 · Particles and their behaviour — payload map for the rebuild

Read of Design's six approved C1 pages, frozen at `docs/ks3/design-reference/c1/`,
against the generator's current vocabulary. **This is a specification, not a build.**
No lesson module is authored here and no generator file is touched.

Method, viewports, standing law and the "new or existing?" column: `docs/ks3/b1-inventory/README.md`.
Cross-page value collisions already ruled: `docs/ks3/b1-inventory/00-delivery-drift.md`.
Design's own notes: `docs/ks3/design-reference/c1/NOTES-C1.md`.

Every line number below was read out of the frozen file named at the head of its section.
Nothing was measured in a browser for this pass — this is a source read, and where a
statement needs a rendered measurement it says so.

---

## ⚠️ C1 is a REBUILD over a unit that is already live

The live unit is `ks3_data/chemistry_c1_particles.py` (1,728 lines, six lessons inline),
built to `ks3/chemistry/particles-and-their-behaviour/` and published in
`mrbadmus_site/`. Design's six pages **supersede it**. §7 diffs the two, concretely, and
answers whether this delivery closes MRB-177.

---

## §0 · What is true of all six pages

Everything in this section is byte-identical or structurally identical across the six
frozen files, and is stated once here rather than six times below.

### 0.1 The spine

| Element | Where | Note |
|---|---|---|
| `<x-dc>` template + `<script type="text/x-dc" data-dc-script>` | every file | all authored constants live in the trailing script |
| `<div class="rd" data-mode="ks3">` | c1-01 **28**, c1-02 **30**, c1-03 **29**, c1-04 **27**, c1-05 **28**, c1-06 **28** | 8 inline declarations, same set as B1 |
| `nav.ks3-nav` + inline breadcrumb `<ol>` | c1-01 **30–44** and the same block on the other five | header trail carried INLINE — confirms B1 §1.3 |
| `nav[data-rail="top"]` | c1-01 **46–52** | sticky bar, `{{ railCountLabel }}` / `{{ railCurrentLabel }}` / `{{ railBarStyle }}` |
| `nav[data-rail="side"]` | c1-01 **54–69** | `position: fixed; top: 150px; left: calc(50% - 632px); width: 104px` |
| `main.ks3-main > div.ks3-lesson` | every file | |
| `header.ks3-lesson-head` | eyebrow / `<h1>` / `.ks3-bigq` / `.ks3-review-flag` | draft flag gated on `{{ draftVisible }}` |
| `footer.ks3-footer` with `MrBadmusAI · Key Stage 3 Science` | c1-01 **344–346** | |

Page-local `<style>` in `<helmet>`: c1-01 **14–25**, c1-02 **14–27**, c1-03 **14–26**,
c1-04 **14–24**, c1-05 **14–25**, c1-06 **14–25**. Common to all six: the `c1-arrive`
keyframe + `[data-arrive]`, the `[data-rail]` 1340px swap, and the
`prefers-reduced-motion` kill. Each file then adds its own one or two rules
(`[data-readout]`, `[data-matrix]`, `[data-ctl]`, `[data-case]`, `input[data-scrub]`).

### 0.2 The rail is on ALL SIX pages, with five stages each

Every C1 lesson declares `const RAIL = [ {id, label, short} × 5 ]`. Stage 1 is always
the hook, stage 5 is always the ladder. Both rail variants render on every page.

### 0.3 The ladder is identical in shape on all six

`RUNGS` (2 page-marked, per-option `correction`) + `SELF_RUNGS` (2 self-marked, 5
criteria each). Header strings are byte-identical across the unit:

- `<h2>Mastery ladder</h2>`
- `.ks3-ladder-sub` → `Four rungs. Two the page marks, two you mark.`
- `scoreLine` → `You got N of 4.`
- `scoreNote` → `You marked rungs 3 and 4 yourself.`
- check button → `Check my answer`
- retry button → `Retry my misses`
- retry note → `Clears the ticks on rungs 3 and 4 and keeps what you wrote.`
- tally → `All N ticked — rung met.` / `N of M ticked — not yet.`

**Rung titles are authored per lesson but follow one pattern on all six:**
`Rung 1 · Recall`, `Rung 2 · The one that catches people`, `Rung 3 · Explain`,
`Rung 4 · Take it somewhere new`.

### 0.4 The KEY FACT box

Exactly one per lesson, on all six — README.txt's convention holds. It is a **top-level
orphan `<div>`**, never nested inside a block, on all six pages. Inline style, identical
on all six:

```
margin: 28px 0 0; padding: 22px 26px; border-radius: var(--ks3-r-panel);
background: var(--ks3-card); border: 2px solid var(--ks3-ink);
box-shadow: 6px 6px 0 var(--ks3-accent);
label: mono 13px / .09em / uppercase / var(--ks3-accent-text)
body:  display 700 25px / 1.32 / -.015em / var(--ks3-ink)
```

Lines: c1-01 **165–168**, c1-02 **188–191**, c1-03 **168–171**, c1-04 **174–177**,
c1-05 **166–169**, c1-06 **176–179**.

### 0.5 Endmatter — FOUR cards on every page

`Before this lesson` · `Next in this unit` · `At GCSE this becomes` · `Ask Mr Badmus AI`.
c1-06 heads its second card **`Next unit`** (line 323), not `Next in this unit` — the
one variation. `At GCSE this becomes` is a `<p>`, never a `<ul>`. The tutor CTA is a real
`<a>` pointing at an **in-page section id** on this page, different per lesson.

### 0.6 No `p.ks3-legal` on any of the six

Six absences. F20's tally gains six on the "absent" side.

### 0.7 No figure slot and no keyword block anywhere in C1

Zero `figures[]` and zero vocabulary/keyword blocks across the six pages. Both are things
the live unit has and the new pages do not — see §7.

---

# §1 · c1-01 · The particle model · MODEL

`docs/ks3/design-reference/c1/c1-01-particle-model.dc.html` — 842 lines.

## 1.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `particle-model` | filename; **matches `ks3_data/structure.py:158` exactly** |
| title | `The particle model` | line **75**; matches structure.py:158 |
| family | `MODEL` | eyebrow line **74**, README.txt line 6 |
| eyebrow | `Particles and their behaviour · Model` | line **74** |
| big question | `Pour 50 ml of water into 50 ml of alcohol and you get 97 ml. Nothing leaked, nothing evaporated. Where did the three millilitres go?` | line **76** |
| review_state | `draft` (flag rendered) | line **78** |
| `<title>` | `The particle model · MrBadmusAI KS3` | line **12** |

## 1.2 Payload — line ranges for a byte-identical lift

**Never retype these.** Every string is authored and science-bearing.

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` — 5 × `{id, label, short}` | **351–357** | five stages, both label sets |
| `FLOOR` | **359** | `24` — the cut floor, load-bearing in Rung 2 |
| `GAP_TESTS` — 3 × `{id, label, on, off}` | **361–371** | three tests × two outcome paragraphs each |
| `RUNGS` — r1, r2, per-option `correction` | **373–390** | page-marked ladder |
| `SELF_RUNGS` — r3 (5 criteria), r4 (5 criteria) | **392–415** | self-marked ladder, `fieldLabel` + `placeholder` |
| `state` initialiser (incl. `startCuts` seeding) | 418–432 | |
| `componentDidMount` — IntersectionObserver + first draws | 433–448 | `rootMargin: '-45% 0px -50% 0px'` |
| `sizeLabel` / `sig` — the mm → µm → nm ladder | 452–464 | **engine constants, not payload** |
| `drawCut()` — 900×320 design space, 2× transform | 465–563 | ghost box, grain threshold, scale bar, progress ticks |
| `drawGap()` — 900×260 design space | 564–618 | two boxes, `GAPS EMPTY` / `GAPS FILLED IN` |
| `seg(on, dark, dis)` | 619–629 | two branches |
| `renderVals()` | 630–836 | |
| ↳ `cutNote` — **4 authored branches** | **642–651** | floor / near-floor / zero / mid |
| ↳ `gapNote` — 2 authored branches + `GAP_TESTS` lookup | **656–663** | |
| ↳ `hookOptions` — 4 options | **697–700** | |
| ↳ `cutProgress` | **708** | `floor reached` / `N of 24 possible cuts` |
| ↳ `cutGateOptions` — 4 options | **711–714** | the commit gate |
| ↳ `cutVerdict` / `cutVerdictColor` | 724–725 | `Floor` / `Yes` |
| ↳ `cutAlt` — computed aria-label | **726–727** | |
| ↳ `gapOptions` — 4 options | **745–748** | |
| ↳ `gapAlt` — computed aria-label | **756–757** | |
| ↳ `thinkOptions` — 4 options | **766–769** | |
| ↳ `markedRungs` / `selfRungs` / `scoreLine` / `onRetry` | 777–834 | shared shape, §0.3 |

Static prose: header **73–80** · hook **82–104** (h2 **84**, prompt **85**, commit **87**,
reveal **100**) · explainer **106–108** · `#s-cut` head + lede **110–118**, readout labels
**142 / 146 / 150**, button labels **155 / 156 / 157** · KEY FACT **165–168** ·
`#s-gap` **170–204** (h2 **174**, lede **177**, control caption **194**) ·
`#s-think` **206–231** (quote **211**, lede **212**, reveal paragraphs **227–228**) ·
ladder **233–301** · keynote **303–306** (body **305**) · Going further **308–316**
(body **314**) · endmatter **318–340**.

**Authored word count ≈ 1,730** (data constants 588 · `renderVals` prose 435 · static
markup, tags and `{{ }}` stripped, 707).

## 1.3 Block sequence

| # | Anchor / element | Generator block type | Status |
|---|---|---|---|
| 1 | `#s-hook` (line 82) `ks3-block ks3-dark ks3-hook` | `hook` → `r_hook` | **EXISTING.** `phenomenon.commit`/`options`/`reveal` all read since 14 Aug. |
| 2 | `section.ks3-explainer` (106) | `explainer` → `r_explainer` | **EXISTING** |
| 3 | `#s-cut` (110) `ks3-block` (light) | `check` + activity kind **`halving-bench`** | **NEW instrument.** §1.5.1 |
| 4 | orphan `<div>` (165) | `key-fact` → `r_key_fact` with `ground: "card"` | **EXISTING**, geometry differs — §1.6 |
| 5 | `#s-gap` (170) `ks3-block ks3-dark ks3-practical` | `practical` + activity kind **`gap-test-rig`** | **NEW instrument.** §1.5.2 |
| 6 | `#s-think` (206) `ks3-block ks3-misconception` | `misconception` + kind `confrontation` | **EXISTING renderer, NEW contract** — §1.6 (a) |
| 7 | `#s-ladder` (233) `ks3-ladder` | `quiz` → `r_ladder` | **EXISTING**, four string gaps — §1.6 (b) |
| 8 | `section.ks3-block ks3-dark ks3-keynote` (303) | `summary` | **EXISTING** |
| 9 | `section.ks3-layer` (308) | `stretch` layer | **EXISTING** |
| 10 | `div.ks3-endmatter` (318) | `r_endmatter` | **PARTIAL** — no "Next in this unit" card exists |

## 1.4 Rail

Five stages, all anchors resolve to real section ids on the page.

| # | anchor | short | label | `done_when` (page's own predicate, line 668–675) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `50 + 50 = 97` | `hookChoice !== null` — a commitment made |
| 2 | `s-cut` | `CUT` | `Keep cutting` | `reachedFloor` — 24 cuts reached at least once (sticky; undo does not untick) |
| 3 | `s-gap` | `GAP` | `What is in the gap` | `gapTest !== null` — one of the three tests run |
| 4 | `s-think` | `THINK` | `A sharper knife` | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | `r1 && r2 answered && r3 && r4 checked` |

## 1.5 Instruments

### 1.5.1 Halving bench — `#s-cut`, canvas

- **Gate** (lines 120–134): a 4-option commit inside an inset panel, shown while
  `cutGate === null`; the bench markup does not exist until a gate option is pressed.
- **Canvas**: `<canvas width="1800" height="640" role="img" aria-label="{{ cutAlt }}">`
  (line 138). Design space **900 × 320**, `setTransform(2,0,0,2,0,0)`, `clearRect` first.
- **Readouts**, `[data-readout]` 3-col grid → 1-col under 620px (page style line 23–24):
  `Cuts made` · `Edge of the piece` · `Still sugar?` (labels 142 / 146 / 150).
- **Controls**, three buttons in a flex row (154–158): `Cut it in half` (disabled at
  floor) · `Undo a cut` (disabled at 0) · `Cut ten more times` (disabled at floor).
- **Note panel** (161): `--ks3-band`, 2px ink, holding `{{ cutNote }}`.
- **Payload the generator would need**

```
floor: 24
size_ladder:  engine — 1 cm / 2^n, formatted mm ≥0.1cm, µm ≥1e-4cm, else nm
gate:    { commit: "...", options: [4 strings] }
readouts: [{label, source}] × 3
buttons:  [{label, action, disabled_when}] × 3
notes:   { at_floor, near_floor, at_start, mid }   # 4 authored strings
alt:     computed from n and the grain threshold
```

- **Canvas-vs-DOM**: canvas. The grain threshold is `n >= FLOOR - 4`; below it the piece
  is a solid block, at and above it the piece resolves into `2^(24−n)` particles across
  and the canvas prints `ONE PARTICLE` or `N PARTICLES LEFT` (line 531).

### 1.5.2 Gap test rig — `#s-gap`, canvas, dark ground

- **Controls**: a 4-option `ul.ks3-options` (179–188) picking what is in the gap, then a
  three-button row of tests (196–199) using the **dark** `seg()` branch.
- **Canvas**: `1800 × 520`, design space **900 × 260**, no `clearRect` (opaque fill).
  Two boxes side by side; the right one packs solid when the answer is not "Nothing at all".
- **Readout**: none numeric. `{{ gapNote }}` under the frame (202) resolves to
  `GAP_TESTS[i].on` when the gap is empty and `.off` when it is filled.
- **Payload**

```
options: [4 strings]           # index 3 ("Nothing at all") is the one that survives
tests:   [{id, label, on, off}] × 3
notes:   { no_test_correct, no_test_wrong }
```

- The `filled` discriminator is `gapChoice !== null && gapChoice !== 3` — **positional**.
  A port must carry the correct index explicitly, not rely on option order.

### 1.5.3 The `#s-think` commit

Not in NOTES §2, but it is an interactive mechanism: quote (211) → lede (212) → 4 options
(214–223) → gated two-paragraph reveal (225–230). It is a rail stop. See §1.6 (a).

## 1.6 What no existing generator component covers

**(a) `confrontation` must become a rail stop that asks for something.**
`build_ks3.py`'s own comment above `ACTIVITY_KIND_RENDERERS` states: *"`#s-think` is a
rail stop on none of the six lessons, because MRB-208 ruled the rail carries only
sections that require the student to do something, and a confrontation asks for nothing."*
**C1 contradicts this on all six pages.** Every C1 `#s-think` carries four options and a
reveal gated behind them, and every C1 rail lists `s-think` as a stage. The fix is the one
the same comment already predicts — `data-stage-done` must be emitted on the basis of
whether the payload carries a commitment, not on the kind's name.

**(b) The ladder's authored strings the generator cannot express.** Four gaps, all
present on all six lessons:

1. **Rung titles.** `LADDER_RUNGS` is the fixed tuple `recall / apply / explain / produce`,
   rendered `2 · Apply` and `4 · Produce`. Design writes `Rung 2 · The one that catches
   people` and `Rung 4 · Take it somewhere new`, and prefixes the word `Rung `.
2. **`fieldLabel`.** `_rung_self` hardcodes `Write your answer`. Design authors
   `Your explanation` / `Your reply` / `Your answer` per rung.
3. **`placeholder`.** `_rung_self` emits no `placeholder`. Design authors one per self-rung
   (`Both liquids are made of…`).
4. **Retry note.** `shared/ks3.js:309` writes *"Reopens only the rungs you missed, and puts
   your cursor on the first one."*; Design's C1 says *"Clears the ticks on rungs 3 and 4 and
   keeps what you wrote."* **The engine's behaviour is better than Design's** — Design's
   `onRetry` (830–834) also clears `r1` and `r2`, which its own note does not say. The
   engine string is engine-owned and should win; this is a finding for Design, not a port task.

**(c) The KEY FACT box's geometry.** `r_key_fact` can already emit `data-ground="card"`,
so the ground is covered. The numbers are not:

| Property | `shared/ks3.css:2430` | Design C1 (all six) |
|---|---|---|
| `margin-top` | 24px | **28px** |
| `padding` | 18px 22px | **22px 26px** |
| `box-shadow` | 5px 5px 0 accent | **6px 6px 0 accent** |
| body `font-size` | 22px | **25px** |
| body `line-height` | 1.35 | **1.32** |

**⚑ Drift 5 is reopened.** The ruling was `--ks3-band` on a 5:1 count. C1 is
`--ks3-card` × 6, so the tally is now **band × 5, card × 7** and the majority has flipped.
Ruling needed before the port, not during it.

**(d) `seg()` — drift 4 is reopened, in both branches.** Drift 4 ruled the segmented
control at **17px / `11px 17px`** on b1-06's variant, on the basis that it is the only
b1 light branch matching the dark branch's geometry. C1 uses **16px / `11px 16px`** in
*both* branches, on all six pages (c1-01 **619–629**, c1-02 605–610, c1-03 614–619,
c1-04 609–620, c1-05 559–564, c1-06 470–474). C1 is internally consistent and 1px smaller
than the ruling in every dimension. Six pages against one — needs re-ruling.

**(e) `halving-bench` and `gap-test-rig` have no renderer.** Neither is in
`ACTIVITY_KIND_RENDERERS`, neither maps to a `SIM_ARIA` kind, and the `sim` path is closed
to both: `r_sim` refuses any `kind` not in `SIM_ARIA` and any control not in
`SIM_CONTROLS` (`temperature, volume, particles, medium, specimen, magnification, focus,
part, centre, motion`). `cut`, `undo`, `cut-ten` and the three gap tests are none of those.

**(f) The endmatter has no "Next in this unit" card.** `lesson_page` builds exactly three
cards — `Before this lesson`, `Connects to`, `At GCSE this becomes` — plus the tutor.
Design's C1 draws a forward link on every page. `references` renders under "Connects to",
which is the wrong heading and the wrong semantic.

**(g) c1-01 needs `before_this`.** Its first card reads *"Nothing — this is where the unit
starts"* and links to `../ks3/index.html`. The schema key exists (§4.8.1 D) and
`r_endmatter` drops an empty card without it.

**(h) The tutor CTA is a live in-page link, not a span.** `r_endmatter` deliberately emits
a `<span>` because `#ks3-tutor` does not exist. Design's C1 emits
`<a class="ks3-tutor-cta" href="#s-gap">Ask about this lesson</a>` — a working link that
scrolls the student back up to the bench. That is arguably worse than an inert span: it
promises a tutor and delivers a scroll. **Finding for Mide**, and either way the per-lesson
anchor and the per-lesson tutor paragraph (line 337) are authored strings that need a home.

**(i) `done_when` is authored and read by nothing.** `build_ks3.py:3417` serialises it into
`data-rail-stages`; `shared/ks3.js`'s `doneByDom` never looks at it, using `data-stage-done`
and then heuristics. Every `done_when` string in every KS3 lesson module is currently inert.
C1 needs five real predicates per lesson, so this has to be closed for the rebuild.

**(j) `3 · Explain` vs `Rung 3 · Explain` — the count-word helper.** `_count_word` and the
derived `ladder-sub` already produce Design's exact sentence; no gap. Recorded so the port
does not re-derive it.

**⚑ Science / content, for Mide only**

1. **The particle count label may be one dimension short.** At `n = 20` the canvas draws a
   16 × 16 face and prints `256 PARTICLES LEFT` (line 531). A cube of sugar 16 particles on
   an edge holds 16³ = 4,096. The drawing is a cross-section, so the face count is
   defensible; the words `PARTICLES LEFT` read as the whole piece.
2. **`FLOOR = 24` and "0.6 nm" check out.** 1 cm / 2²⁴ = 0.596 nm, and `sizeLabel(24)`
   returns `0.6 nm`. NOTES §3 flag 1 is correct. Whether 0.6 nm is "about the width of a
   sucrose molecule" is yours.
3. **The deliberate line** — *"you can cut a particle, you just don't get sugar"* — is
   carried in the reveal at line 227 and in Rung 2's key (line 385). NOTES §3 flag 2 holds.

---

# §2 · c1-02 · Solids, liquids and gases · CONTRAST

`c1-02-solids-liquids-and-gases.dc.html` — 809 lines.

## 2.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `solids-liquids-and-gases` | **matches structure.py:159** |
| title | `Solids, liquids and gases` | line **77** |
| family | `CONTRAST` | line **76** |
| eyebrow | `Particles and their behaviour · Contrast` | line **76** |
| big question | `Ice, water and steam are the same substance and the same particles. So what exactly is different about them?` | line **78** |

## 2.2 Payload — line ranges

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` — 5 stages | **338–344** | |
| `STATES` | **346** | `['solid','liquid','gas']` |
| `MATRIX` — 6 × `{key, label, solid, liquid, gas}` | **348–355** | the contrast table, 24 authored cells |
| `RUNGS` | **357–374** | |
| `SELF_RUNGS` | **376–399** | |
| `state` initialiser (incl. `startState` prop) | 402–417 | |
| `componentDidMount` — IO + reduced-motion probe + `seed()` + `loop()` | 418–435 | |
| `seed()` — 48 particles, random x/y/vx/vy/phase | 441–447 | engine |
| `draw()` — 900 × 310 design space, three state routines | 454–604 | solid 511–532, liquid 533–564, gas 565–590 |
| ↳ **fixed-size reference particle** | **592–597** | NOTES §3 flag 3 — must not be removed |
| `seg(on, dis)` | 605–610 | |
| `renderVals()` | 611–803 | |
| ↳ `benchNote` — **8 authored branches** | **623–640** | squash × 2, trails × 3, resting × 3 |
| ↳ `hookOptions` — 4 | **674–677** | |
| ↳ `benchProgress` | **685** | |
| ↳ `gateOptions` — 4 | **688–691** | |
| ↳ `benchAlt` — computed, 3 branches | **699–702** | |
| ↳ `stateButtons` / motion / trails / squash labels | 703–719 | `Freeze the motion` / `Start the motion`, `Hide the paths` / `Show the paths` |
| ↳ `matrixRows` — highlight rule | **722–730** | |
| ↳ `thinkOptions` — 4 | **733–736** | |

Static prose: header **75–82** · hook **84–106** (h2 **86**, prompt **87**, commit **89**,
reveal **102**) · explainer **108–110** · `#s-bench` **112–157** (eyebrow **115**, h2 **116**,
gate commit **123**, group captions **141** `State` / **147** `Instruments`, squash button
label **151**) · `#s-matrix` **159–186** (eyebrow **160**, h2 **161**, lede **162**, four
`<th>` **167–170**, footnote **185**) · KEY FACT **188–191** · `#s-think` **193–218**
(quote **198**, lede **199**, reveal **214–215**) · ladder **220–288** · keynote **290–293** ·
Going further **295–303** · endmatter **305–327**.

**Authored word count ≈ 1,570** (data 480 · `renderVals` prose 424 · static 666).

## 2.3 Block sequence

| # | Anchor | Block type | Status |
|---|---|---|---|
| 1 | `#s-hook` (84) | `hook` | EXISTING |
| 2 | `.ks3-explainer` (108) | `explainer` | EXISTING |
| 3 | `#s-bench` (112) light | `check` + kind **`state-bench`** | **NEW** — §2.5.1 |
| 4 | `#s-matrix` (159) light | `check` + kind **`state-matrix`** | **NEW** — §2.5.2. `comparison` is the nearest existing and is the wrong shape. |
| 5 | orphan `<div>` (188) | `key-fact` `ground: "card"` | EXISTING, §1.6 (c) |
| 6 | `#s-think` (193) | `misconception` + `confrontation` | EXISTING renderer, §1.6 (a) |
| 7 | `#s-ladder` (220) | `quiz` | EXISTING, §1.6 (b) |
| 8 | keynote (290) | `summary` | EXISTING |
| 9 | layer (295) | `stretch` | EXISTING |
| 10 | endmatter (305) | `r_endmatter` | PARTIAL, §1.6 (f) |

**This is the only C1 lesson with no dark `practical` block.** Its only dark grounds are
the hook and the keynote.

## 2.4 Rail

| # | anchor | short | label | `done_when` (645–652) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `The long bridge` | `hookChoice !== null` |
| 2 | `s-bench` | `BENCH` | `State bench` | `Object.keys(seen).length >= 3` |
| 3 | `s-matrix` | `TABLE` | `The contrast` | **`Object.keys(seen).length >= 3`** — the same predicate as stage 2 |
| 4 | `s-think` | `THINK` | `Softening particles` | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete |

**⚑ Finding.** Stage 3 ticks on stage 2's state. `#s-matrix` demands nothing of the
student, so under MRB-208 it should not be a rail stop at all — or the matrix needs its own
demand. Same defect shape as c1-05 stage 4 (§5.4). **Design's call.**

## 2.5 Instruments

### 2.5.1 State bench — `#s-bench`, canvas

- **Gate** (121–135): 4-option commit, `gateOpen = gate === null`. Answering it also
  seeds `seen.solid = true` (line 695) — so the gate is both the commitment and the first
  state observation.
- **Canvas**: `1800 × 620`, design space **900 × 310**, animated via `requestAnimationFrame`
  (`loop()` 448–453). **No `clearRect`** — the opaque `fillRect(0,0,W,H)` covers it.
- **Controls**, two labelled groups:
  - `State` (141–146): three segmented buttons, `Solid` / `Liquid` / `Gas`. Selecting one
    resets `squash` to false and records the state as seen.
  - `Instruments` (147–152): `Freeze the motion` / `Start the motion` toggle ·
    `Hide the paths` / `Show the paths` toggle · `Try to squash it` toggle.
- **Readouts**: none numeric. `benchProgress` in the section head (118) and
  `{{ benchNote }}` in a band panel below (155).
- **Payload**

```
states: ["solid","liquid","gas"]
gate:   { commit, options: [4] }
controls: motion(toggle, labels ×2) · trails(toggle, labels ×2) · squash(toggle, 1 label)
notes:  { squash: {gas, other},
          trails: {solid, liquid, gas},
          rest:   {solid, liquid, gas} }        # 8 authored strings
alt:    3 computed branches
reference_particle: true          # NOTES §3 flag 3 — non-negotiable
```

- **Canvas-vs-DOM**: canvas. Squash drops the lid by 92px for a gas and 8px for a solid or
  liquid (line 470) and prints one of two mono banners (491).
- **⚑ Finding.** `benchProgress` (line 614) computes `Object.keys(seen).length + (seen[st] ? 0 : 1)`,
  which counts the *current* state as seen before it is chosen. On load, with the gate
  unanswered and the bench not yet rendered, the section head reads **"1 of 3 states seen"**.
  Same family as B1's F2.

### 2.5.2 Contrast matrix — `#s-matrix`, DOM

Not in NOTES §2 at all, and it is an instrument: the row highlight is live and driven by
the bench.

- **Structure**: `div[overflow-x:auto]` → `table[data-matrix]` → `thead` with four `<th>`
  (`Property` / `Solid` / `Liquid` / `Gas`) → `tbody` with six rows, each `<th scope="row">`
  plus three `<td>`.
- **Page-local CSS** (lines 23–26): `border-collapse: collapse`, 2px ink borders, mono
  uppercase 13px column heads, and a 700px breakpoint dropping to 16px / `9px 10px`.
- **Highlight rule** (line 723): `squash` → the `squash` row; else `trails` → the
  `movement` row; else the `arrangement` row. Lit rows take `--ks3-accent-tint` on both
  the row and its `<th>`.
- **Payload**

```
columns: ["Property","Solid","Liquid","Gas"]
rows: [{key, label, solid, liquid, gas}] × 6
highlight_from: state-bench   # squash → squash, trails → movement, else arrangement
footnote: "The highlighted row is the one your current bench setting is showing."
```

- **⚑ Finding.** Three of the six rows — `shape`, `volume`, `pour` — can never be
  highlighted by any bench setting. And the footnote (185) refers to a bench the student
  cannot see until the gate above is answered.

## 2.6 What no existing generator component covers

- **`state-bench` has no renderer, and the `particle-states` sim is not it.** `SIM_ARIA`'s
  `particle-states` is *"a box of particles that responds to a **temperature slider**"*
  with `SIM_CONTROLS` of `temperature / volume / particles / medium`. Design's bench has
  **no temperature control at all** — it has three named state buttons, a motion toggle, a
  path toggle and a squash toggle. Rendering it as `particle-states` would give the student
  a slider Design did not draw and hide three controls Design did. That is the MRB-205
  failure exactly.
- **`state-matrix` has no renderer.** `r_comparison` is B1-06's shape (a fixed two-column
  "one against the other" table with a dark header row); this is a 4-column property matrix
  with a live-highlighted row keyed off another block's state. **Cross-block state is a new
  capability** — no existing KS3 component reads another block's state.
- **Two toggles need paired labels.** `motion` and `trails` each carry two authored strings
  swapped by state. Nothing in the schema holds a label pair.
- Plus §1.6 (a) (b) (c) (d) (f) (i), all of which recur here.

**⚑ Science / content, for Mide**
The `#s-think` reveal (215) argues *"If melting made particles smaller you would expect
water to be less dense than ice, and it is the other way round."* The observation is right
(water is denser than ice) but the conditional reads backwards on a first pass — smaller
particles in the liquid would make water **more** dense, which is what happens, so the
sentence appears to offer the observed fact as the refutation of its own antecedent.
Worth a read before it goes to students.

---

# §3 · c1-03 · Changes of state · PROCESS

`c1-03-changes-of-state.dc.html` — 842 lines.

## 3.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `changes-of-state` | **matches structure.py:160** |
| title | `Changes of state` | line **76** |
| family | `PROCESS` | line **75** |
| eyebrow | `Particles and their behaviour · Process` | line **75** |
| big question | `Put ice on a hot ring and the temperature climbs. Then, for eight full minutes, it stops climbing — while the flame is still on. Where is that energy going?` | line **77** |

## 3.2 Payload — line ranges

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **347–353** | |
| comment | 355 | *"x = energy put in (0-100), T = temperature. Two plateaus"* |
| `KEYS` — 6 breakpoints | **356** | `[[0,-20],[12,0],[26,0],[60,100],[92,100],[100,120]]` |
| `SORTS` — 4 × `{id, text, answer, right, wrong}` | **358–371** | the melt/dissolve sorter, 12 authored strings |
| `RUNGS` | **373–390** | |
| `SELF_RUNGS` | **392–415** | |
| `state` (incl. `startScrub`) | 418–432 | carries **`thinkSeen`, which nothing reads or writes** |
| `tempAt(x)` — piecewise interpolation over `KEYS` | 451–458 | engine |
| `phaseAt(x)` — 5 bands | **459–466** | `ice <12 · melting <26 · water <60 · boiling <92 · steam` |
| `draw()` — 900 × 330; graph left, flask right | 467–613 | graph 481–545, flask 546–612 |
| `seg(on, dis)` | 614–619 | |
| `renderVals()` | 620–836 | |
| ↳ **`PHASE`** — 5 × `{label, color, note}` | **633–644** | **the five plateau paragraphs — the science core of the lesson** |
| ↳ `hookOptions` — 4 | **680–683** | |
| ↳ `curveProgress` | **691** | `N of 2 plateaus visited` |
| ↳ `gateOptions` — 4 | **694–697** | |
| ↳ `scrubText` (aria-valuetext) | **706** | |
| ↳ `curveAlt` | **720** | |
| ↳ `jumps` — 3 × `{label, v}` | **722–724** | `Jump to melting` 19 · `Jump to boiling` 76 · `Back to the start` 0 |
| ↳ `bubbleOptions` — 4 | **740–743** | |
| ↳ **`bubbleVerdict`** — 3 authored branches | **750–754** | per-answer response |
| ↳ `sortCards` | 756–774 | |

Static prose: header **74–81** · hook **83–105** (h2 **85**, prompt **86**, commit **88**,
reveal **101**) · explainer **107–109** · `#s-curve` **111–166** (eyebrow **114**, h2 **115**,
lede **119**, gate commit **123**, scrub label **141**, readout labels **145 / 149 / 153**,
static `50.0 g` **154**) · KEY FACT **168–171** · `#s-bubble` **173–196** (eyebrow **174**,
h2 **175**, lede **176**, **static** reveal paragraphs **192–193** including *"Steam is
invisible"*) · `#s-think` **198–227** (quote **203**, lede **204**, card buttons **211 / 212**,
gated summary **223–224**) · ladder **229–297** · keynote **299–302** · Going further
**304–312** · endmatter **314–336**.

**Authored word count ≈ 1,813** — the second-largest lesson in the unit.

## 3.3 Block sequence

| # | Anchor | Block type | Status |
|---|---|---|---|
| 1 | `#s-hook` (83) | `hook` | EXISTING |
| 2 | `.ks3-explainer` (107) | `explainer` | EXISTING |
| 3 | `#s-curve` (111) light | `check` + kind **`heating-bench`** | **NEW** — §3.5.1 |
| 4 | orphan `<div>` (168) | `key-fact` `ground: "card"` | EXISTING |
| 5 | `#s-bubble` (173) dark | `practical` + kind **`keyed-commit`** | **NEW** — §3.5.2 |
| 6 | `#s-think` (198) | `misconception` + kind **`sort-cards`** | **NEW instrument inside an existing shell** — §3.5.3 |
| 7 | `#s-ladder` (229) | `quiz` | EXISTING |
| 8 | keynote (299) | `summary` | EXISTING |
| 9 | layer (304) | `stretch` | EXISTING |
| 10 | endmatter (314) | `r_endmatter` | PARTIAL |

## 3.4 Rail

| # | anchor | short | label | `done_when` (651–658) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `Sealed bag` | `hookChoice !== null` |
| 2 | `s-curve` | `CURVE` | `Heating bench` | `seenPlateau.melting && seenPlateau.boiling` — **both** plateaus visited |
| 3 | `s-bubble` | `BUBBLE` | `In the bubble` | `bubbleChoice !== null` |
| 4 | `s-think` | `THINK` | `Melt or dissolve` | `sortsAnswered >= 4` — all four cards sorted |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete |

This is the strongest rail in the unit: every predicate names state the section itself owns.

## 3.5 Instruments

### 3.5.1 Heating bench — `#s-curve`, canvas + range input

- **Gate** (121–135): 4-option commit on what the temperature will do.
- **Canvas**: `1800 × 660`, design space **900 × 330**, `clearRect` then opaque fill.
  Left half is the heating curve (`gx 62, gy 40, gw 470, gh H−110`), right half is a
  sealed flask (`fx 596, fy 44, fw 250, fh H−120`) drawn per phase.
- **Controls**:
  - `<input id="scrub" data-scrub type="range" min=0 max=100 step=1>` with a per-value
    `aria-valuetext` (line 142). Page CSS gives it `width:100%; height:44px;
    accent-color: var(--ks3-accent)`.
  - Three jump buttons (157–161): `Jump to melting` (19) · `Jump to boiling` (76) ·
    `Back to the start` (0). Pressed state is `|x − v| < 3`.
- **Readouts** (143–156): `Temperature` (`−N °C` / `N °C`) · `What is in the flask`
  (`{{ phaseLabel }}`, coloured by phase) · `Mass in the flask` — **hard-coded `50.0 g`
  in the markup**, deliberately never a variable.
- **Payload**

```
keys:   [[0,-20],[12,0],[26,0],[60,100],[92,100],[100,120]]
phases: { ice, melting, water, boiling, steam } × {label, color, note}
gate:   { commit, options: [4] }
jumps:  [{label, value}] × 3
mass:   "50.0 g"                 # constant, and the point
progress: "N of 2 plateaus visited"
alt / aria-valuetext: computed from T and phase
```

- **Canvas-vs-DOM**: canvas. The flask has four distinct particle routines
  (ice 570–572, melting 573–585, water 586–590, boiling 591–601, steam 602–605) with two
  mono banners: `ORDER BREAKING DOWN` and `BREAKING AWAY COMPLETELY`.

### 3.5.2 Bubble commit — `#s-bubble`, DOM, dark ground

Four options (178–187), then a gated dark panel. The panel's **first** paragraph is
computed (`{{ bubbleVerdict }}`, three authored branches keyed on the answer index) and its
**second and third** paragraphs are static markup (192–193). Payload:

```
options: [4]
answer_index: 2                      # "Water that has turned into a gas"
responses: { correct, index_3_special_case, other }
reveal: [2 static paragraphs]        # incl. "Steam is invisible"
```

The nearest existing shape is the generic `predict` (prompt / options / reveal), which
carries **one** reveal string. A per-answer response is new.

### 3.5.3 Melt-or-dissolve sorter — inside `#s-think`, DOM

Not in NOTES §2; NOTES §1 names it as PART-06's confrontation.

- **Structure** (206–219): `display: grid; grid-template-columns: repeat(auto-fit,
  minmax(260px, 1fr)); gap: 12px`. Each card is a div with a bold 18px statement, two
  segmented buttons (`Melting` / `Dissolving`), and a per-answer note revealed on choice.
- **Card border** (767–768): `--ks3-accent` when right, `--ks3-ink` when wrong,
  `--ks3-option-border` when unanswered. Note colour: `--ks3-ink` right,
  `--ks3-accent-text` wrong.
- **Gated summary** (221–226) once all four are sorted: two static paragraphs.
- **Payload**

```
buttons: ["Melting","Dissolving"]
cards: [{id, text, answer, right, wrong}] × 4
summary: [2 static paragraphs]
done_when: all four answered
```

- The nearest existing kind is `sort-rows` / `sort-pairs`. Both are the wrong shape: this
  is a per-card binary verdict with two authored feedback strings each, and a gated
  whole-set summary.

## 3.6 What no existing generator component covers

- `heating-bench`, `keyed-commit` and `sort-cards` — three new kinds, none in
  `ACTIVITY_KIND_RENDERERS`, none reachable via `r_sim`.
- **A range input is a new control class.** No KS3 component emits `<input type="range">`
  with `aria-valuetext`. `r_sim` builds sliders, but only from `SIM_CONTROLS` names and
  only inside a `SIM_ARIA` kind.
- **A hard-coded readout.** `Mass in the flask · 50.0 g` is markup, not state, and that is
  the whole confrontation of PART-05. The port must not turn it into a variable.
- **Per-answer response strings** (§3.5.2) — the reveal is currently one string.
- Plus §1.6 (a) (b) (c) (d) (f) (i).

**⚑ Science / content, for Mide only — three items, one of them substantive**

1. **The drawn plateau ratio is 2.29 : 1, and the page's own words say seven.**
   `KEYS` gives melting 12→26 = **14 units** and boiling 60→92 = **32 units**, a ratio of
   **2.29 : 1**. The `PHASE.boiling` note (line 641) says *"far longer than the melting one
   … about seven times as much energy"*, and the real figure is right (L_f 334 kJ/kg vs
   L_v 2260 kJ/kg ≈ 6.8 : 1). **NOTES §3 flag 4 asserts the drawn ratio "is real (about 7:1
   for water)". It is not — the canvas under-draws it by a factor of about three.** The
   science in the prose is correct; the picture contradicts it. Either `KEYS` moves (boiling
   would need to run 60 → ~155 on a rescaled axis) or the prose changes. **Mide's call.**
2. **NOTES §3 flag 4 also names the wrong rung.** It says *"Rung 4's answer depends on
   students having seen it"*. Rung 4 (405–414) is the wet-towel evaporation question and
   does not touch the plateau ratio. **Rung 2** (383–389) is the plateau rung.
3. **Eight minutes or six?** The big question (77) says the climb stops *"for eight full
   minutes"*; Rung 2 (383) says *"For six minutes the thermometer stays at 0 °C"*.
   Technically two different set-ups, but a student will read them as one.

**⚑ Code finding.** `state.thinkSeen` (line 429) is initialised and never read or written.
Dead state; do not carry it into the module.

---

# §4 · c1-04 · Gas pressure · MODEL

`c1-04-gas-pressure.dc.html` — 820 lines.

## 4.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `gas-pressure` | **matches structure.py:161** |
| title | `Gas pressure` | line **74** |
| family | `MODEL` | line **73** |
| eyebrow | `Particles and their behaviour · Model` | line **73** |
| big question | `An empty aerosol can carries a warning: do not put it on a fire, it may explode. It is empty. What is there to explode?` | line **75** |

## 4.2 Payload — line ranges

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **347–353** | |
| `TEMPS` — 3 × `{label, v}` | **355** | `Cold 0.55 · Warm 1 · Hot 1.75` |
| `VOLS` — 3 × `{label, v}` | **356** | `Large 1 · Half size 0.62 · Quarter size 0.4` |
| `COUNTS` — 3 × `{label, v}` | **357** | `12 · 24 · 48` |
| `PREDICTIONS` — 3 × `{id, question, options[3], answer, note}` | **359–369** | the prediction stack |
| `RUNGS` | **371–388** | |
| `SELF_RUNGS` | **390–413** | |
| `state` (incl. `startTemp` prop) | 416–432 | |
| `componentDidMount` — IO, reduced probe, `hits/flashes/bumps` arrays | 433–452 | |
| `seed()` — 48 particles with unit direction vectors | 458–465 | engine |
| `step()` — **the physics** | **472–504** | wall bounce → `hits.push(now)`; 1-second rolling window (501); pair-distance bump detection (492–500) |
| `draw()` — 900 × 340 | 505–608 | box 515–531, flashes 533–541, bumps 543–551, particles 553–564, reference particle 566–577, readout 579–606 |
| `seg(on, dis)` | 609–614 | light |
| `segDark(on)` | 615–620 | dark, amber |
| `renderVals()` | 621–814 | |
| ↳ `benchNote` — **6 authored branches** | **631–644** | marks · smaller box · hot · cold · more particles · resting |
| ↳ `hookOptions` — 4 | **680–683** | |
| ↳ `benchProgress` | **691** | `N of 3 controls tried` |
| ↳ `gateOptions` — 4 | **694–697** | |
| ↳ `benchAlt` — computed | **705–706** | |
| ↳ `marksLabel` pair | **720** | |
| ↳ `predictions` incl. the wrong-answer fallback string | **725–741** (fallback **738**) | |
| ↳ `thinkOptions` — 4 | **744–747** | |

Static prose: header **72–79** · hook **81–103** (h2 **83**, prompt **84**, commit **86**,
reveal **99**) · explainer **105–107** · `#s-bench` **109–172** (eyebrow **112**, h2 **113**,
gate commit **120**, three control-group captions **140 / 148 / 156**, the grey-bumps
caption **166**) · KEY FACT **174–177** · `#s-predict` **179–199** (eyebrow **180**,
h2 **181**, lede **182**) · `#s-think` **201–227** (quote **206**, lede **207**, three-paragraph
reveal **222–224**) · ladder **229–297** · keynote **299–302** · Going further **304–312** ·
endmatter **314–336**.

**Authored word count ≈ 1,693.**

## 4.3 Block sequence

| # | Anchor | Block type | Status |
|---|---|---|---|
| 1 | `#s-hook` (81) | `hook` | EXISTING |
| 2 | `.ks3-explainer` (105) | `explainer` | EXISTING |
| 3 | `#s-bench` (109) light | `check` + kind **`collision-counter`** | **NEW** — §4.5.1 |
| 4 | orphan `<div>` (174) | `key-fact` `ground: "card"` | EXISTING |
| 5 | `#s-predict` (179) dark | `practical` + kind **`prediction-stack`** | **NEW** — §4.5.2 |
| 6 | `#s-think` (201) | `misconception` + `confrontation` | EXISTING renderer |
| 7 | `#s-ladder` (229) | `quiz` | EXISTING |
| 8 | keynote (299) | `summary` | EXISTING |
| 9 | layer (304) | `stretch` | EXISTING |
| 10 | endmatter (314) | `r_endmatter` | PARTIAL |

## 4.4 Rail

| # | anchor | short | label | `done_when` (651–658) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `The empty can` | `hookChoice !== null` |
| 2 | `s-bench` | `COUNT` | `Collision counter` | `touched >= 3` |
| 3 | `s-predict` | `PREDICT` | `Three predictions` | all 3 predictions answered |
| 4 | `s-think` | `THINK` | `Swelling particles` | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete |

**⚑ Finding.** `touched` is set by `Math.max(prev.touched, N)` where N is 1 for temperature,
2 for volume and 3 for count (709 / 713 / 717). Pressing **only** a particle-count button
sets `touched = 3`, ticks the stage, and makes the head read *"all controls tried"* when
one was. The predicate wants a set, not a maximum.

## 4.5 Instruments

### 4.5.1 Collision counter — `#s-bench`, canvas

- **Gate** (118–132): 4-option commit on what causes pressure.
- **Canvas**: `1800 × 680`, design space **900 × 340**, animated, no `clearRect`.
- **Controls**, three captioned groups in a `[data-ctl]` grid
  (`repeat(auto-fit, minmax(230px, 1fr))`, page CSS line 23):
  - `Temperature` → `Cold` / `Warm` / `Hot`
  - `Size of the container` → `Large` / `Half size` / `Quarter size`
  - `How many particles` → `12` / `24` / `48`
  - plus a full-width toggle `Show/Hide particle-to-particle bumps` (165) with a
    17px muted caption beside it (166) — **NOTES §3 flag 7's confrontation, in words**.
- **Readouts — drawn on the canvas, not in the DOM** (579–606):
  `WALL HITS PER SECOND` + a 58px Bricolage number · `PRESSURE` + a 220×22 bar filled to
  `min(1, hits/170)` · three mono status lines `TEMPERATURE / CONTAINER / PARTICLES`.
- **Reference particle**, fixed radius 9, drawn bottom-left with
  `ONE PARTICLE — SAME SIZE AT EVERY SETTING` (566–577).
- **Payload**

```
temps:  [{label, speed_multiplier}] × 3
vols:   [{label, scale}] × 3
counts: [{label, n}] × 3
gate:   { commit, options: [4] }
bumps:  { on_label, off_label, caption, threshold: 0.0022 }
notes:  6 authored branches
readouts: wall_hits_per_second (live) · pressure_bar (hits/170) · 3 status lines
alt:    computed from temp/vol/count
```

- **Canvas-vs-DOM**: canvas, including the readouts. **NOTES §3 flag 6 holds** — pressure
  is reported as a count and a bar, never in pascals.
- **The counting is real**, not a formula: `step()` pushes a timestamp on every wall
  collision and shifts entries older than 1000 ms (line 501), so the number on screen is an
  actual count of the last second. `flashes` last 420 ms (502). Reduced-motion scales speed
  by 0.35 (474) rather than stopping — so the count still runs.

### 4.5.2 Prediction stack — `#s-predict`, DOM, dark ground

- **Structure** (184–198): a vertical flex column of three panels, each with a bold
  18px question, three `segDark` buttons (`Goes up` / `Stays the same` / `Goes down`),
  and a note revealed on answer.
- **Panel border** (732–733): `--ks3-alert` when right, `--ks3-on-dark-muted` otherwise.
- **Note** (738): the authored `note` when right; a **single shared fallback** when wrong —
  *"Not quite — go back to the bench and try it before reading on. Change only the one
  thing the question changes."*
- **Payload**

```
options: ["Goes up","Stays the same","Goes down"]     # shared by all three
predictions: [{id, question, answer_index, note}] × 3
wrong_note: 1 shared string
done_when: all three answered
```

- Nearest existing kind: generic `predict`. Wrong shape — this is three predictions in one
  block, each with its own answer and note, on a shared option set.

## 4.6 What no existing generator component covers

- **`collision-counter` is not `gas-pressure`.** `SIM_ARIA`'s `gas-pressure` is *"gas
  particles bouncing inside a box with a **movable wall**"* with a readout *"in words"*.
  Design draws three three-way segmented groups, a bumps toggle, a live 1-second rolling
  count, a pressure bar and a fixed-size reference particle. `SIM_CONTROLS` has
  `temperature / volume / particles`, which is three of the four names — but `r_sim` builds
  them as sliders, and there is no name for the bumps toggle, no canvas readout, and no
  reference particle. Porting onto `gas-pressure` would drop the bumps toggle, which is
  PART-08's entire confrontation.
- **`prediction-stack` has no renderer.**
- **A canvas-drawn readout is new.** Every KS3 instrument to date writes its readout into
  `.ks3-sim-readout` in the DOM. Design draws it inside the canvas — which means it is
  **invisible to a screen reader except through `aria-label`**, and the label
  (705–706) reports temperature, container and particle count but **not the wall-hit
  number**. That is the one number the lesson is about. **Finding: the aria-label needs the
  count, and the port should add it** (an addition inside a drawn component, per standing law).
- Plus §1.6 (a) (b) (c) (d) (f) (i).

---

# §5 · c1-05 · Diffusion · MODEL

`c1-05-diffusion.dc.html` — 744 lines.

## 5.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `diffusion` | **matches structure.py:162** |
| title | `Diffusion` | line **75** |
| family | `MODEL` | line **74** |
| eyebrow | `Particles and their behaviour · Model` | line **74** |
| big question | `Someone opens a bottle of perfume at the far end of a sealed, still room with no draught at all. Two minutes later you can smell it. What carried it to you?` | line **76** |

## 5.2 Payload — line ranges

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **332–338** | |
| `SCALE_CARDS` — 3 × `{distance, time, text}` | **340–347** | the scale panel, 9 authored strings |
| `RUNGS` | **349–366** | |
| `SELF_RUNGS` | **368–391** | |
| `state` (incl. `startWarm` prop) | 394–410 | |
| `reset()` — 130 particles seeded in the left strip | **433–442** | `x 0.04–0.17, y 0.18–0.82`; zeroes `crossR` / `crossL` / `frames` |
| `step()` — the random walk | **449–476** | isotropic step, reflecting walls, side-crossing counters (460–464), trail capture (465–468), evenness test (470–474) |
| `draw()` — 900 × 320 | 477–557 | tank 487–489, divider 491–499, trace 501–510, particles 512–523, half counts 529–535, **concentration profile 537–556** |
| `seg(on, dis)` | 559–564 | |
| `renderVals()` | 565–738 | |
| ↳ `walkNote` — **4 authored branches** | **575–584** | not started · tracing · even · spreading |
| ↳ `hookOptions` — 4 | **618–621** | |
| ↳ `walkProgress` | **629** | `not started` / `spreading` / `evened out` |
| ↳ `gateOptions` — 4 | **632–635** | |
| ↳ `walkAlt` — computed | **643–644** | |
| ↳ control labels (`Pause`/`Continue`/`Start the run`, trace pair, warm pair) | 649–662 | |
| ↳ `thinkOptions` — 4 | **666–669** | |
| ↳ `scaleCards` | **677** | passed straight through |

Static prose: header **73–80** · hook **82–104** (h2 **84**, prompt **85**, commit **87**,
reveal **100**) · explainer **106–108** · `#s-walk` **110–164** (eyebrow **113**, h2 **114**,
lede **118**, gate commit **122**, readout labels **142 / 146 / 150**, reset button
label **156**) · KEY FACT **166–169** · `#s-think` **171–196** (quote **176**, lede **177**,
reveal **192–193** — *the crossing-counter argument*) · `#s-scale` **198–212** (eyebrow **199**,
h2 **200**, lede **201**, closing paragraph **211**) · ladder **214–282** ·
keynote **284–287** · Going further **289–297** (the Brown / Einstein / Perrin paragraph
**295**) · endmatter **299–321**.

**Authored word count ≈ 1,592.**

## 5.3 Block sequence

| # | Anchor | Block type | Status |
|---|---|---|---|
| 1 | `#s-hook` (82) | `hook` | EXISTING |
| 2 | `.ks3-explainer` (106) | `explainer` | EXISTING |
| 3 | `#s-walk` (110) light | `check` + kind **`random-walk-bench`** | **NEW** — §5.5.1 |
| 4 | orphan `<div>` (166) | `key-fact` `ground: "card"` | EXISTING |
| 5 | `#s-think` (171) | `misconception` + `confrontation` | EXISTING renderer |
| 6 | `#s-scale` (198) dark | `practical` + kind **`scale-cards`** | **NEW** — §5.5.2 |
| 7 | `#s-ladder` (214) | `quiz` | EXISTING |
| 8 | keynote (284) | `summary` | EXISTING |
| 9 | layer (289) | `stretch` | EXISTING |
| 10 | endmatter (299) | `r_endmatter` | PARTIAL |

**c1-05 is the only C1 lesson where `#s-think` sits BEFORE the dark practical block.**
Every other lesson runs `practical → think`.

## 5.4 Rail

| # | anchor | short | label | `done_when` (589–596) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `The still room` | `hookChoice !== null` |
| 2 | `s-walk` | `WALK` | `Random walk` | `even` — the tank has evened out |
| 3 | `s-think` | `THINK` | `Wanting to spread` | `thinkChoice !== null` |
| 4 | `s-scale` | `SCALE` | `Distance and time` | **`thinkChoice !== null`** — stage 3's predicate |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete |

**⚑ Finding, the clearest instance in the unit.** Stage 4 ticks on stage 3's state.
`#s-scale` is three static cards and two paragraphs; it demands nothing at all, so under
MRB-208 it is not a rail stop. Either it needs a demand or it comes off the rail. **Design's
call** — same question as c1-02 stage 3 (§2.4).

## 5.5 Instruments

### 5.5.1 Random-walk bench — `#s-walk`, canvas

- **Gate** (120–134): 4-option commit on what the particles do once the tank is even.
- **Canvas**: `1800 × 640`, design space **900 × 320**, animated, no `clearRect`. The tank
  is `bx 56, by 44, bw W−112, bh H−118` on `#F3F6F5`; a dashed divider marks the midline.
- **Controls**, four buttons (154–159): `Start the run` / `Pause` / `Continue` ·
  `Put the drop back` · `Follow one particle` / `Stop following one particle` ·
  `Warm the water` / `Cool the water`.
- **Readouts**, `[data-readout]` 3-col grid: `Crossings left to right` ·
  `Crossings right to left` · `Spread out?` (`Yes` / `Not yet`).
- **Second readout, drawn on the canvas**: `LEFT HALF: n` / `RIGHT HALF: n` above the tank
  (534–535) and an 18-bin **concentration profile** below it labelled
  `HOW CROWDED, ALONG THE TANK` (537–556).
- **Payload**

```
particles: 130, seeded x 0.04–0.17 / y 0.18–0.82
step:      { cool: 0.0055, warm: 0.011 }        # y step ×1.5
even_test: |right − n/2| < 0.09n, sampled every 20 frames
gate:      { commit, options: [4] }
controls:  run(3 labels) · reset(1) · trace(2) · warm(2)
readouts:  crossR · crossL · even  +  half counts  +  18-bin profile
notes:     4 authored branches
progress:  not started / spreading / evened out
```

- **Canvas-vs-DOM**: hybrid — three DOM readouts, two canvas readouts.
- **NOTES §3 flag 8 verified.** `crossR` / `crossL` are instance fields cleared **only** by
  `reset()` (439–440), never when `even` flips. The counters keep climbing. ✓
- **⚑ Code finding.** Because the counters are instance fields and `renderVals` runs only
  on `setState`, and `step()` calls `setState` at most every 20 frames and usually every 40
  (line 473), the two DOM counters **update in visible jumps roughly twice a second**
  rather than continuously. The port has to choose a cadence deliberately.

### 5.5.2 Scale cards — `#s-scale`, DOM, dark ground, static

Not in NOTES §2. Three cards in
`repeat(auto-fit, minmax(240px, 1fr))` (202–210), each: a mono uppercase
`--ks3-alert` distance label, a 28px display time, and a 17px body paragraph. Closed by a
static paragraph (211) carrying the inverse-square-ish rule (*"Double the distance and
diffusion takes four times as long"*).

```
cards: [{distance, time, text}] × 3
closing: 1 static paragraph
interactive: false
```

Nearest existing shape: `r_cards` (reveal-cards). Wrong — these are not flip cards, there
is nothing to reveal, and R4's declaration ask (`verify_ks3.py` §5.1.2(a)) would fire on a
block that asks for nothing. It is a **static three-up panel** and needs its own component.

**⚑ Note.** `--ks3-alert` (amber) is used here for a non-misconception label on dark ground
(line 205). The dark segmented control has used amber since B1 (drift 4 records the dark
branch as byte-identical across four b1 pages), so amber-on-dark is established for
*controls*; this is amber for *body labelling*, which is new. README.txt's *"Amber is
reserved for misconceptions"* is about blocks, not controls — but this instance is neither.
Flagged, not resolved.

## 5.6 What no existing generator component covers

- **`random-walk-bench` is not `diffusion`.** `SIM_ARIA`'s `diffusion` is *"two groups of
  particles, **orange starting on the left and blue starting on the right**"* with a
  readout *"in words"*. Design draws **one** group of 130 purple particles released on the
  left into still water, a single traced particle, a warm/cool toggle, a pause/continue
  transport, a reset, and an 18-bin concentration histogram. Only the crossing counters are
  shared. Porting onto `diffusion` would replace the lesson's instrument with a different
  one.
- **A transport control (`run` / `pause` / `continue` / `reset`) is new.** No KS3 instrument
  has a play head.
- **A "follow one" trace is new**, and its trail cap (900 points, line 467) is an
  authored-ish engine constant.
- **A histogram readout is new.**
- **`scale-cards` has no renderer** and must not be forced into `reveal-cards`.
- Plus §1.6 (a) (b) (c) (d) (f) (i), and the §5.4 rail question.

---

# §6 · c1-06 · Testing the model · INVESTIGATION

`c1-06-testing-the-model.dc.html` — 666 lines. **No canvas anywhere on this page.**

## 6.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `testing-the-model` | **matches structure.py:163** |
| title | `Testing the model: does it explain everything?` | line **75**; **matches structure.py:163 in full** |
| family | `INVESTIGATION` | line **74** |
| eyebrow | `Particles and their behaviour · Investigation` | line **74** |
| big question | `You have spent five lessons being shown how well the particle model works. Here are seven things it has to account for. Three of them it cannot. What should be done about that?` | line **76** |

⚠️ `README.txt` line 11 abbreviates the title to `Testing the model`, and the endmatter
link on c1-05 (line 309) uses the same short form. The page's own `<h1>` carries the full
title and matches `structure.py`. **The full title is the title.**

## 6.2 Payload — line ranges

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **348–354** | |
| **`CASES`** — 7 × `{id, tag, text, ok, verdict}` | **356–371** | the evidence bench — **the largest single payload in C1** |
| **`HISTORY`** — 5 × `{year, who, label, claim, body, broke}` | **373–394** | the model timeline, 25 authored strings |
| `RUNGS` | **396–413** | |
| `SELF_RUNGS` | **415–438** | |
| `state` | 441–453 | `history: 1` — the timeline opens on **Dalton**, not Democritus |
| `componentDidMount` — IO only | 454–467 | no draw loop, no canvas |
| `seg(on)` | 470–474 | one-arg, no disabled branch |
| `renderVals()` | 475–660 | |
| ↳ **`VERDICTS`** — 4 × `{text, reply}` | **490–499** | **authored inside `renderVals`, not at module scope** |
| ↳ `hookOptions` — 4 | **533–536** | |
| ↳ `benchProgress` | **544** | `N of 7 judged` / `all seven judged` |
| ↳ `cases` mapping incl. `verdictLabel` pair | 545–565 | `The model handles this` / `The model cannot do this` |
| ↳ **`tally`** | **567** | `Four explained, three not — and you called N of the seven before opening the verdict.` |
| ↳ `verdictOptions` / `verdictResponse` | 569–575 | |
| ↳ `historySteps` + `historyLabel/Claim/Body/Broke` | 577–587 | |
| ↳ `thinkOptions` — 4 | **590–593** | |

Static prose: header **73–80** · hook **82–104** (h2 **84**, prompt **85**, commit **87**,
reveal **100**) · explainer **106–108** · `#s-bench` **110–149** (eyebrow **113**, h2 **114**,
lede **118**, buttons **129 / 130**, **the shared-cause paragraph 146**) · `#s-verdict`
**151–174** (eyebrow **152**, h2 **153**, lede **154**, **two static reveal paragraphs
170–171**) · KEY FACT **176–179** · `#s-history` **181–201** (eyebrow **182**, h2 **183**,
lede **184**, `What broke it:` label **199**) · `#s-think` **203–228** (quote **208**,
lede **209**, reveal **224–225**) · ladder **230–298** · keynote **300–303** ·
Going further **305–313** (the over-correction paragraph **311**) · endmatter **315–337**.

**Authored word count ≈ 2,327 — the largest lesson in the unit** (data 1,186 ·
`renderVals` prose 261 · static 880).

## 6.3 Block sequence

| # | Anchor | Block type | Status |
|---|---|---|---|
| 1 | `#s-hook` (82) | `hook` | EXISTING |
| 2 | `.ks3-explainer` (106) | `explainer` | EXISTING |
| 3 | `#s-bench` (110) light | `check` + kind **`evidence-bench`** | **NEW** — §6.5.1 |
| 4 | `#s-verdict` (151) dark | `practical` + kind **`keyed-commit`** | **NEW** (same kind as c1-03 §3.5.2) — §6.5.2 |
| 5 | orphan `<div>` (176) | `key-fact` `ground: "card"` | EXISTING |
| 6 | `#s-history` (181) light | `check` + kind **`model-timeline`** | **NEW** — §6.5.3 |
| 7 | `#s-think` (203) | `misconception` + `confrontation` | EXISTING renderer |
| 8 | `#s-ladder` (230) | `quiz` | EXISTING |
| 9 | keynote (300) | `summary` | EXISTING |
| 10 | layer (305) | `stretch` | EXISTING |
| 11 | endmatter (315) | `r_endmatter` | PARTIAL; second card is headed **`Next unit`** |

**Two structural firsts for the unit:** the KEY FACT box sits at position 5, *after* the
dark practical block rather than straight after the flagship instrument; and this is the
only lesson with **three** anchored non-hook, non-think, non-ladder sections.

## 6.4 Rail

| # | anchor | short | label | `done_when` (504–511) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `Ice floats` | `hookChoice !== null` |
| 2 | `s-bench` | `EVIDENCE` | `Evidence bench` | all 7 cases judged |
| 3 | `s-verdict` | `VERDICT` | `The verdict` | `verdictChoice !== null` |
| 4 | `s-history` | `HISTORY` | `Five models` | **`history !== 1`** |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete |

**⚑ Finding.** The timeline opens on index 1 (Dalton), so stage 4 ticks the moment any
*other* entry is selected — and **unticks** if the student reads all five and returns to
Dalton. The predicate wants "has visited more than the default", which is a set, not an
inequality. Same class of defect as c1-04 stage 2 (§4.4).

## 6.5 Instruments

### 6.5.1 Evidence bench — `#s-bench`, DOM only

**No gate.** This is the only flagship instrument in C1 that is open from the start.

- **Structure** (120–141): a vertical flex column of seven panels. Each panel is a
  `[data-case]` grid — `minmax(0,1fr) auto`, collapsing to one column at 720px (page CSS
  line 23–24) — with a mono uppercase `tag`, a bold 19px `text`, and two buttons
  `Explains it` / `Cannot`.
- **Verdict**, revealed on answer (133–138): a panel with a `6px` left border —
  `--ks3-rule-strong` on `--ks3-inset` when the model handles it, `--ks3-accent` on
  `--ks3-band` when it fails — a mono label (`The model handles this` / `The model cannot
  do this`) and the authored verdict paragraph.
- **Tally**, revealed when all seven are judged (143–148): the computed `tally` line in
  24px display type, followed by the **static** shared-cause paragraph.
- **Payload**

```
cases: [{id, tag, text, ok, verdict}] × 7          # 4 ok, 3 fail
buttons: ["Explains it", "Cannot"]
verdict_labels: { ok, fail }
tally: "Four explained, three not — and you called N of the seven before opening the verdict."
shared_cause: 1 static paragraph                   # "identical featureless spheres"
done_when: all seven judged
```

- **⚑ NOTES §3 flag 9 is slightly off.** It says *"The tally text says so"* about the shared
  cause. The tally (567) is the count line only; the shared cause is the **static
  paragraph at 146**. The claim is on the page, in the same panel — just not in the string
  NOTES names. Matters because it decides whether the sentence lives in data or in markup.

### 6.5.2 Verdict commit — `#s-verdict`, DOM, dark ground

Four options (156–165) each carrying its own `reply`, then a gated dark panel whose
**first** paragraph is `{{ verdictResponse }}` (the chosen option's reply) and whose
**second and third** paragraphs are static (170–171).

```
options: [{text, reply}] × 4
answer_index: 1            # "Keep using it where it works, and record exactly where it fails"
reveal: [2 static paragraphs]
```

Structurally identical to c1-03's bubble commit (§3.5.2) but with the reply attached
per-option rather than branched in code — so **`keyed-commit` should take the c1-06 shape**
(reply on the option) and c1-03 should be expressed in it.

### 6.5.3 Model timeline — `#s-history`, DOM

- **Structure** (186–200): a wrapping flex row of five buttons, each a two-line stack
  (mono 12px `year` over 16px/700 `who`), then one detail card below.
- **Button style** (579–581): `text-align:left; padding:10px 14px; min-height:44px;
  border-radius: var(--ks3-r-control)` — a **third** control geometry in the unit, neither
  the light segment nor the dark one.
- **Detail card** (195–200): mono accent-text `label` · 26px display `claim` ·
  19px `body` · a rule-topped 18px muted line prefixed by the static bold
  `What broke it:` and carrying `broke`.
- **Payload**

```
steps: [{year, who, label, claim, body, broke}] × 5
default_index: 1                     # Dalton
broke_label: "What broke it:"        # static
done_when: has visited more than the default   # ← see §6.4 finding
```

- **NOTES §3 flag 10 verified**: Bohr's `broke` reads *"Nothing yet, for chemistry."* (393).

## 6.6 What no existing generator component covers

- **`evidence-bench` has no renderer.** The nearest existing kinds are `test-board`
  (`r_test_board`) and `removal-cases` (`r_removal_cases`). Both are the wrong shape: this
  is seven binary judgements each with one authored verdict and a two-tone verdict panel,
  plus a whole-set tally that counts how many the student called correctly **before**
  opening the verdicts. The "you called N of seven" scoring is genuinely new — it scores a
  commitment the page explicitly says it is not marking (line 118).
- **`model-timeline` has no renderer**, and its button is a third control geometry (§6.5.3)
  that needs registering rather than folding into `seg()`.
- **`keyed-commit` has no renderer** (shared with c1-03).
- **`VERDICTS` lives inside `renderVals`, not at module scope.** A byte-identical lift must
  reach lines **490–499**, which a naive "constants are at the top of the script" extraction
  would miss. Same for c1-03's `PHASE` (633–644) and c1-04's fallback note (738).
- **The endmatter's second card is headed `Next unit`**, not `Next in this unit` — a
  per-lesson heading override on top of the missing card itself (§1.6 f).
- Plus §1.6 (a) (b) (c) (d) (i).

**⚑ Science / content, for Mide**
NOTES §3 flag 9 says the three failures *"all fail because the model has identical
featureless spheres with no bonds"*. `CASES` k3 (ice floating) is attributed to particles
needing *"a shape, that hold each other at arm's length in a fixed pattern"*; k5 (diamond
vs graphite) to *"particles that can bond"*; k6 (rubber) to *"long tangled chains"*. Three
different repairs, presented as one shared cause. The static paragraph at 146 makes the
unifying claim carefully (*"different from each other, or … joined together in some
particular way"*), so it holds — but it is the sentence the whole C1 → C2 bridge rests on
and is worth reading as an examiner.

---

# §7 · WHAT CHANGES FOR A STUDENT

Design's C1 against `ks3_data/chemistry_c1_particles.py` (1,728 lines) and the built pages
in `ks3/chemistry/particles-and-their-behaviour/`.

## 7.1 Slugs and titles — nothing moves

| # | Live slug | Live title | Design slug | Design title | Verdict |
|---|---|---|---|---|---|
| 1 | `particle-model` | The particle model | `particle-model` | The particle model | **identical** |
| 2 | `solids-liquids-and-gases` | Solids, liquids and gases | same | same | **identical** |
| 3 | `changes-of-state` | Changes of state | same | same | **identical** |
| 4 | `gas-pressure` | Gas pressure | same | same | **identical** |
| 5 | `diffusion` | Diffusion | same | same | **identical** |
| 6 | `testing-the-model` | Testing the model: does it explain everything? | same | same | **identical** |

All six also match `ks3_data/structure.py:156–164`. **No slug breaks, no URL changes, no
`requires` edge repointing, no scheme-of-work row moves.** Families are unchanged too
(MODEL / CONTRAST / PROCESS / MODEL / MODEL / INVESTIGATION).

## 7.2 What a student GAINS

**(a) A progress rail. Verified absent on the live unit.** `grep -c 'data-rail'` returns
**0** on all six built pages; `ks3-railbar` returns 0; no `rail` key exists in any of the
six live lesson dicts. Design's C1 puts five stages on every page, in both variants.

**(b) A KEY FACT box.** `grep -c 'ks3-keyfact'` returns **0** on all six built pages. The
live unit has `key_note` (which renders as the dark keynote) but no key-fact box. Design
adds one per lesson.

**(c) Bespoke instruments in place of a shared three-slider lab.** The live unit renders
seven `particle-states` / `gas-pressure` / `diffusion` sim frames across five lessons
(L1 0 · L2 1 · L3 1 · L4 2 · L5 2 · L6 1), all built from the same four `SIM_CONTROLS`
sliders. Design draws **ten distinct mechanisms** plus a live matrix:

| Lesson | Live | Design |
|---|---|---|
| L1 | no instrument at all | halving bench (canvas) + gap test rig (canvas) |
| L2 | 1 × `particle-states` slider lab | state bench (canvas, 6 controls) + live contrast matrix |
| L3 | 1 × `particle-states` slider lab | heating bench (canvas, scrub + 3 jumps) + melt/dissolve sorter |
| L4 | 2 × `gas-pressure` slider labs | collision counter (canvas, 10 controls) + prediction stack |
| L5 | 2 × `diffusion` slider labs | random-walk bench (canvas, transport + trace + warm) |
| L6 | 1 × `diffusion` slider lab (reused from L5) | evidence bench (7 cases) + verdict commit + model timeline |

**L1 gains the most: it currently has no interactive instrument at all.**

**(d) A hook that ends in a commitment on every lesson.** The live records carry
`phenomenon.commit` but no `options` and no `reveal`, so the live hook asks a question and
stops. Design authors four options and a gated reveal on all six.

**(e) An answered "Think again" on every lesson.** The live `misconception` blocks are the
three-beat prose format MRB-177 introduced. Design keeps the confrontation and adds a
four-option commitment before the reveal, so the student states the wrong idea's fate
before reading it.

**(f) Eleven "Diagram coming soon" placeholders disappear.** `ks3-figure-pending` count on
the built pages: L1 2 · L2 1 · L3 2 · L4 2 · L5 2 · L6 2 = **11**. Design's C1 declares no
figures at all, because the canvases do the work the figures were promising.

**(g) Per-lesson self-rung scaffolding.** Design authors `fieldLabel` and `placeholder` on
all twelve self-marked rungs. The live pages emit the engine's fixed `Write your answer`
and no placeholder.

## 7.3 What a student LOSES

**(a) The keyword / vocabulary block, on all six lessons.** Every live lesson carries a
`keyword` block and a populated `vocabulary` list. **Design's C1 has neither on any page.**
Terms are taught inside the blocks that use them. This is the single biggest deletion and
it is a **product decision, not a port detail** — the live pages give a student a
definitions panel to revise from and the new ones do not.

**(b) Block count roughly halves.** Live `core` lengths: 14 · 13 · 17 · 14 · 13 · 15 = **86
blocks**. Design's: 10 · 10 · 10 · 10 · 10 · 11 = **61 sections**, of which the ladder,
keynote, stretch and endmatter are four. The teaching surface goes from ~10 content blocks
per lesson to ~5, each much larger.

**(c) The worked-example / do-it-yourself pair on L3.** `changes-of-state` currently
carries `mass-fifa` (`worked-example`) + `mass-fifa-do` (`construct`) — a Law 5 pair, and
the only FIFA-style working in the unit. `grep -c 'ks3-worked'` confirms it is live on the
built page. **Design's c1-03 has no worked example and no arithmetic.** MRB-177 §5.1.2(b)
was ruled specifically to protect this pair's budget exemption; dropping the pair makes that
amendment moot for C1.

**(d) `reveal-cards` grids, on all six.** Live: `word-check`, `state-cards`,
`state-change-cards`, `pressure-cards`, `word-flip`. Design has none. MRB-177's other
amendment — §5.1.2(a), the declare-then-tap rule, enforced by `verify_ks3.py:722–751` —
therefore has nothing to enforce in C1 after the rebuild.

**(e) The safety/legal line.** The generator emits `LEGAL_LINE` unconditionally, so the
live pages carry it. Design's C1 pages have none. (In practice the port would keep it —
it is a repo standing element, not a Design one — but it is a difference in the frozen
delivery.)

**(f) The "Connects to" endmatter card**, in exchange for a "Next in this unit" card that
the generator cannot currently emit.

## 7.4 Do the big question, hook and ladder differ? — yes, on all six

**Every big question is rewritten.** Not one survives.

| # | Live big question | Design big question |
|---|---|---|
| 1 | What is everything made of? | Pour 50 ml of water into 50 ml of alcohol and you get 97 ml… Where did the three millilitres go? |
| 2 | Why does a solid keep its shape but a liquid doesn't? | Ice, water and steam are the same substance and the same particles. So what exactly is different about them? |
| 3 | Where does the ice go when it melts? | Put ice on a hot ring and the temperature climbs. Then, for eight full minutes, it stops climbing… Where is that energy going? |
| 4 | What is actually pushing on the inside of a balloon? | An empty aerosol can carries a warning… It is empty. What is there to explode? |
| 5 | How does a smell get across the room with no wind? | Someone opens a bottle of perfume at the far end of a sealed, still room… What carried it to you? |
| 6 | Is the particle model true, or just useful? | You have spent five lessons being shown how well the particle model works. Here are seven things it has to account for. Three of them it cannot. What should be done about that? |

The pattern is consistent: the live questions are abstract and open; Design's are a
specific scenario with a number in it that the lesson then has to settle.

**Every hook is a different phenomenon.**

| # | Live hook | Design hook |
|---|---|---|
| 1 | Half a glass of water, half a glass of alcohol (50 + 50 = 97 cm³) | **Same phenomenon**, retold in ml and promoted to the big question |
| 2 | The same stuff, three ways (ice / water / steam) | A steel girder on a hot day |
| 3 | The sealed bag | **Same phenomenon** (seal it in the bag first) |
| 4 | The marshmallow in the vacuum jar | Nothing in it, and it still bursts (the aerosol can) |
| 5 | Perfume at the front of the lab | No draught, no fan, no one waving (the still room, with a candle as the control) |
| 6 | The one that doesn't fit (ice floats) | Ice floats — **same phenomenon** |

Three of six keep the phenomenon and rewrite it; three change it outright.

**Every ladder is rewritten, and the rung names change.** The live ladders use the
generator's fixed `Recall / Apply / Explain / Produce`. Design uses
`Rung 1 · Recall`, `Rung 2 · The one that catches people`, `Rung 3 · Explain`,
`Rung 4 · Take it somewhere new` on all six. Rung 2's whole framing changes from "apply it"
to "here is the trap", and every question, distractor and correction is new.

**Misconception coverage is unchanged.** PART-01 to PART-13 are all elicited and confronted
in both versions, and the lesson each one lands in is the same in both. NOTES §1's table
agrees with the live `misconceptions` lists lesson for lesson. **Nothing in the register
needs to move.**

## 7.5 Does this delivery close MRB-177?

MRB-177's own record, in the header of `chemistry_c1_particles.py` **lines 37–86**, lists
four structural defects and two content-standard rules.

| MRB-177 item | Does Design's C1 satisfy it? |
|---|---|
| **1. Seventeen activities never placed in any composition** | **Yes, structurally — by making it impossible.** Design's pages have no `activities[]` / `core[]` split at all: every mechanism is a section in document order. There is nothing to orphan. |
| **2. Five declared figures never placed** | **Moot.** Design declares zero figures. The defect cannot recur; the affordance is also gone (§7.3 f). |
| **3. Hooks not paid off where the student is still holding them** | **Yes, and more strictly.** Every hook's reveal is *in the hook block*, gated on the student's own commitment — zero blocks of distance, against MRB-177's fix of one. |
| **4. The five `simulation` activities had no motion, so Law 9 was unsatisfied** | **Yes.** Five of the six lessons carry an animated canvas (c1-06 is DOM-only and deliberately so — it is a judgement lesson, not a phenomenon lesson). All animation respects `prefers-reduced-motion`, and c1-04 scales speed rather than stopping so the count still runs. |
| **Distractor length parity** | **Not verified here.** Needs a read of all 24 ladder option sets plus the 30 commit sets. Design's sets look balanced on inspection but this was not measured. **Open.** |
| **Three-beat misconception format** (mistake in the student's words first, then why it is wrong, then the correct version) | **Yes on all six.** `.ks3-mis-quote` states the wrong idea verbatim, the lede names it as the sensible objection, the four options make the student commit, and the gated reveal gives why-wrong then correct-version. It is a **four**-beat format — the commitment is added. |

**Answer: yes, this delivery closes MRB-177's four structural defects, and closes them at
the level of shape rather than by fixing instances.** Two qualifications Mide should see
before the ticket is closed:

1. **Distractor length parity is unverified** and is the one MRB-177 item that could still
   be failing silently.
2. **MRB-177 also produced two standing amendments to `architecture.md` §5.1.2** — the
   reveal-cards declaration rule (a) and the worked-example budget exemption (b), both
   ruled by Mide on 7 Aug 2026 and both enforced in `verify_ks3.py`. **Design's C1 uses
   neither reveal-cards nor worked examples**, so after the rebuild both amendments apply
   to zero C1 blocks. They stay live for the rest of KS3; they simply stop describing this
   unit. That is not a defect, but it means "MRB-177 is closed" and "MRB-177's rulings are
   exercised by C1" stop being the same statement.

---

# §8 · Where NOTES-C1.md and the pages disagree

Reported, not resolved.

| # | NOTES says | The pages say |
|---|---|---|
| 1 | §2 headline: *"Nine controls across six benches."* | The §2 table lists **eight** instruments across **six lessons**. Counting control *groups* on the pages gives **eighteen**. Counting bespoke mechanisms gives **ten**, plus c1-02's live matrix = **eleven**. No reading of the pages produces "nine controls across six benches". |
| 2 | §2 omits four instruments | The melt/dissolve sorter (c1-03), the prediction stack (c1-04), the verdict commit (c1-06) and the contrast matrix (c1-02) are all mechanisms with payloads. Three of the four are named in NOTES §1 as misconception confrontations, so they were not forgotten — just not counted as instruments. The scale cards (c1-05) are static and correctly excluded. |
| 3 | §2, c1-01 halving bench measures *"edge length, piece count, floor at 24"* | The three readouts are `Cuts made`, `Edge of the piece`, `Still sugar?`. The third is a verdict, not a count. |
| 4 | §3 flag 4: *"the boiling plateau is drawn much longer than the melting one. That ratio is real (about 7:1)"* | `KEYS` draws **2.29 : 1**. The prose in `PHASE.boiling` says seven times, and seven is the right number. **The picture contradicts the words.** §3.6. |
| 5 | §3 flag 4: *"Rung 4's answer depends on students having seen it"* | c1-03's Rung 4 is the wet-towel evaporation question. **Rung 2** is the plateau rung. |
| 6 | §3 flag 9: *"The tally text says so"* | The tally is the count line (567). The shared-cause claim is the **static paragraph at 146**. |
| 7 | §2 implies all instruments are canvas (*"All canvas work is drawn at 2×…"*) | c1-06's two instruments are **pure DOM**; the page has no canvas at all. The 2× claim is otherwise exact — all six canvases are `1800 × 2H` against a `900 × H` design space with `setTransform(2,0,0,2,0,0)`, and every one carries `role="img"` and a state-bound `aria-label`. |
| 8 | README.txt: *"Progress rail ticks only on completed activities"* | True of the **side** rail. The **top bar** is position-driven (`(active + 1) / 5`), so it reads `5 / 5` at the foot of a page on which nothing was answered. This is B1's drift **F2**, reproduced on all six C1 pages. |
| 9 | README.txt: *"Amber is reserved for misconceptions"* | Holds for blocks. Amber is also the dark segmented control's on-state (established since B1, drift 4) and — new in C1 — the scale-card distance label on c1-05 (line 205), which is neither a control nor a misconception. |

---

# §9 · The complete new-component list

Everything the generator cannot render today, gathered. **Ten new activity kinds, one new
block-level capability, one new control geometry, and six schema keys.**

### New activity kinds — none exist in `ACTIVITY_KIND_RENDERERS`

| Kind | Lesson | Canvas? | Nearest existing thing, and why it is wrong |
|---|---|---|---|
| `halving-bench` | c1-01 | yes | none |
| `gap-test-rig` | c1-01 | yes | none |
| `state-bench` | c1-02 | yes | `particle-states` sim — slider-driven, no state buttons, no squash |
| `state-matrix` | c1-02 | no | `comparison` — 2-column, no live highlight, no cross-block state |
| `heating-bench` | c1-03 | yes | none; needs a range input, which no KS3 component emits |
| `sort-cards` | c1-03 | no | `sort-rows` / `sort-pairs` — no per-card twin feedback, no gated set summary |
| `keyed-commit` | c1-03, c1-06 | no | generic `predict` — carries one reveal string, not a per-option reply |
| `collision-counter` | c1-04 | yes | `gas-pressure` sim — no bumps toggle, no canvas readout, no reference particle |
| `prediction-stack` | c1-04 | no | generic `predict` — one prediction per block, not three |
| `random-walk-bench` | c1-05 | yes | `diffusion` sim — two groups not one, no transport, no trace, no histogram |
| `scale-cards` | c1-05 | no | `reveal-cards` — nothing to reveal; would trip `verify_ks3.py` §5.1.2(a) |
| `evidence-bench` | c1-06 | no | `test-board` / `removal-cases` — no called-it-before-the-verdict scoring |
| `model-timeline` | c1-06 | no | none |

(Thirteen rows, ten distinct kinds — `keyed-commit` is shared.)

### New capabilities

1. **`confrontation` must be able to declare a completion contract.** `#s-think` is a rail
   stop on all six C1 pages and carries a commitment. `ACTIVITY_KIND_RENDERERS` currently
   omits `data-stage-done` for it on the strength of B1's payloads. The attribute must key
   off the payload, exactly as the file's own comment already argues.
2. **Cross-block state.** c1-02's matrix highlight is driven by the bench's controls. No
   KS3 component reads another block's state today.
3. **Range inputs and transport controls.** `<input type="range" aria-valuetext>` (c1-03)
   and run/pause/continue/reset (c1-05).
4. **Canvas-drawn readouts** (c1-04, c1-05) — with the accessibility consequence in §4.6.
5. **A "Next in this unit" endmatter card** (all six), with a per-lesson heading override
   for c1-06's `Next unit`.
6. **Real `done_when` predicates.** The field is authored, serialised, and read by nothing.
   C1 needs 30 of them.

### New schema keys, per lesson

`rail[].done_when` (make live) · `ladder.<rung>.title` (override the fixed name) ·
`ladder.<rung>.field_label` · `ladder.<rung>.placeholder` · `before_this` (c1-01) ·
`tutor.anchor` + `tutor.prompt` (all six) · `next_in_unit` (all six).

### One control geometry to re-rule

C1's `seg()` is **16px / `11px 16px`** in both light and dark branches on all six pages.
Drift 4 ruled **17px / `11px 17px`**. Six pages against one — see §1.6 (d). And drift 5's
KEY FACT ground flips from 5:1 to 5:7 — see §1.6 (c). **Both need Mide or Design before the
port, not during it.**

---

## Provenance

Source: `docs/ks3/design-reference/c1/*.dc.html`, committed unmodified, read 16 Aug 2026.
Generator vocabulary read from `build_ks3.py` (`BLOCK_RENDERERS` 3243, `ACTIVITY_SHELLS`
2675, `ACTIVITY_KIND_RENDERERS` 2721, `GENERIC_ACTIVITY_KINDS` 2772, `SIM_ARIA` 782,
`SIM_CONTROLS` 749, `r_rail` 3377, `r_ladder` 2989, `r_key_fact` 3067),
`shared/ks3.js` (`CONTROL_LABELS` 659, `doneByDom` 5033, ladder strings 295–360),
`shared/ks3.css` (`.ks3-keyfact` 2430, `.ks3-reveal` 638).
Live unit read from `ks3_data/chemistry_c1_particles.py` and the built pages in
`ks3/chemistry/particles-and-their-behaviour/`.
Word counts are script-derived from the ranges named in each §x.2 table.
