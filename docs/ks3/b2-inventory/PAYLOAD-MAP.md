# B2 — Movement: skeleton and muscles · payload map

**What this is.** The read specification four authors build `ks3_data/b2/lesson_0N_*.py` from.
Every line number below was read out of the frozen file it names, in this repo, at the commit that
froze them. Nothing here is re-derived from `NOTES-B2.md` where the page disagrees — where they
disagree it says so, explicitly, marked **⚠ NOTES vs PAGE**.

**Source of truth.** `docs/ks3/design-reference/b2/*.dc.html`, committed unmodified.
Method, viewports, standing law: `docs/ks3/b1-inventory/README.md` — not restated here.
Design's own notes: `docs/ks3/design-reference/b2/NOTES-B2.md` (§3 the four new instruments, §6
"For Code", and the change log's fifth instrument `cover-triangle`).

**Target shape.** One `LESSON` dict per module, `architecture.md` §4.8 as amended by §4.8.1 /
§4.8.2, exemplar `ks3_data/b1/lesson_02_using_a_microscope.py`. Instrument blocks are **activities,
not block types** — `ks3_data/b1/__init__.py` `_INSTRUMENT_SEGMENTS` lifts an inline instrument
block into `activities[]` and leaves a `check` / `practical` segment behind it. B2's four
instruments must be added to that map (or authored directly as `activities[]` entries with a
`check`/`practical` block in `core`); either is legal, the second needs no `__init__.py` change.

**File sizes.** b2-01 727 lines · b2-02 896 · b2-03 823 · b2-04 1,028.

---

## The one thing to read before authoring anything

**All the science-bearing prose is in the `<script type="text/x-dc" data-dc-script>` block at the
end of each file, and NOT all of it is in a named constant.** Three pages hide authored prose
inside `renderVals()` — hook options, gate options, "think again" options, the muscle-pair
interpretation ladder, the meter ranking options, the FIFA step lines. A lift that copies only the
top-level `const` blocks loses between 240 and 900 words per lesson. Every one of those inline
literals is given its own line range below.

---
---

# 1 · `what-the-skeleton-does` — SYSTEM

`docs/ks3/design-reference/b2/b2-01-what-the-skeleton-does.dc.html` · 727 lines

## 1.1 Identity

| Field | Value | Source |
|---|---|---|
| `slug` | `what-the-skeleton-does` | `ks3_data/structure.py` line **71** — verified verbatim |
| `title` | `What the skeleton does` | structure.py line 71 · page `<h1>` line **75** |
| `family` | `SYSTEM` | structure.py line 71 |
| `unit` | `movement-skeleton-and-muscles` | structure.py line **69** |
| `discipline` | `biology` | structure.py line 69 |
| `typical_year` | `7` | structure.py line 70 |
| eyebrow | `Movement: skeleton and muscles · System` | page line **74**. Generator builds this from `unit["title"] + " · " + family_label(family)`; `family_label("SYSTEM")` → `"System"`. No authoring needed. |
| `big_question` | `A broken finger is an inconvenience. A broken rib makes every breath hurt. Same material — so what makes the difference?` | page line **76** (`p.ks3-bigq`) |
| `covers` | `KS3.B.SKEL.01` | NOTES §1 |
| `<title>` | `What the skeleton does · MrBadmusAI KS3` | page line 12 |

## 1.2 Content payload — line ranges for a byte-identical lift

**Never retype these.** Every string is authored and science-bearing.

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **348–354** | 5 nodes × `{id, label, short}` |
| **`PARTS`** | **356–433** | the flagship. 4 parts × `{id, tab, name, does, prompt, options[4], title, chain[4]×{level,text}, close}` |
| ├ `skull` | 357–375 | |
| ├ `ribs` | 376–394 | |
| ├ `femur` | 395–413 | |
| └ `marrow` | 414–432 | |
| `JOBS` | **435–440** | 4 sort categories × `{id, label}` |
| **`SORT`** | **442–455** | 6 items × `{id, text, answer, why}` — one answers "Movement and protection — both." |
| **`RUNGS`** | **457–474** | r1, r2 × `{id, title, question, options[4]×{text, correct?/correction}}` |
| **`SELF_RUNGS`** | **476–499** | r3 (5 criteria), r4 (5 criteria) × `{id, title, question, fieldLabel, placeholder, criteria[]}` |
| initial `state` | 502–514 | control defaults; `partId` seeded from `startPart` prop |
| `componentDidMount` / `componentWillUnmount` | 516–530 | IntersectionObserver, `rootMargin: '-45% 0px -50% 0px'` |
| `seg()` style helper | 532–536 | segmented-button style string |
| `renderVals()` | 538–722 | see the four prose blocks below |

**Prose living inside `renderVals()` — lift these too:**

| Payload | Lines | Holds |
|---|---|---|
| **hook options** | **583–588** (4 strings at **584–587**) | `{letter, text}` × 4 |
| hook reveal (static markup) | **100** | the paragraph inside `sc-if hookRevealed` |
| `switchProgress` format | 595 | `'N of 4 parts switched off'` |
| all-four summary (static markup) | **166** | "Four parts, four different routes, one destination…" |
| `sortProgress` format | 632 | `'N of 6 decided'` |
| **think options** | **651–656** (4 strings at **652–655**) | `{letter, text}` × 4 |
| `scoreLine` / `scoreNote` | 714–715 | `'You got N of 4.'` / `'You marked rungs 3 and 4 yourself.'` |

**Static markup prose (outside the script block):**

| What | Lines |
|---|---|
| header — eyebrow / h1 / big question / draft flag | **73–80** |
| `#s-hook` — eyebrow, h2, prompt, commit question, reveal | **82–104** (h2 84, prompt 85, commit 87, reveal 100) |
| the bridging explainer | **106–108** |
| `#s-switch` head + progress + control captions | **110–147** (eyebrow 113, h2 114) |
| all-four-switched summary band | **164–168** (copy at 166) |
| **KEY FACT box** | **171–174** (label 172, statement **173**) |
| `#s-sort` head + lede | **176–184** (eyebrow 179, h2 180, lede **184**) |
| `#s-think` — quote, lede, both reveal paragraphs | **203–228** (quote **208**, lede 209, reveals **224–225**) |
| ladder head + retry note | 230–241, **294–297** |
| keynote | **300–303** (copy at **302**) |
| stretch layer | **305–313** (copy at **311**) |
| endmatter | **315–337** (GCSE prose at **330**, tutor prompt 334) |

⚠ **No `p.ks3-legal` on this page.** The generator appends `LEGAL_LINE` unconditionally
(`build_ks3.py` line 3537) — a known standing drift, not this lesson's problem.

## 1.3 Block sequence — 11 direct children of `.ks3-lesson`

| # | Section | Lines | Generator block / activity kind |
|---|---|---|---|
| 1 | `header.ks3-lesson-head` | 73–80 | generator-emitted from identity fields |
| 2 | `#s-hook` `.ks3-block.ks3-dark.ks3-hook` | 82–104 | **`hook`** → `phenomenon` with `commit` + `options` + `reveal` (the b1-02 shape, §4.8.2) |
| 3 | `section.ks3-explainer` | 106–108 | **`explainer`** |
| 4 | `#s-switch` `.ks3-block` (light) | 110–169 | **NEW** — activity kind `system-switch`, on a **`check`** segment (light ground, per `_INSTRUMENT_SEGMENTS`' measured rule) |
| 5 | KEY FACT `<div>` (orphan, no id, no class) | 171–174 | **`key-fact`** with `ground: "card"` |
| 6 | `#s-sort` `.ks3-block`, `background: var(--ks3-inset)` | 176–201 | **NEW** — activity kind `job-sort` (see §1.6); **not** `sort-task`, **not** `sort-rows` |
| 7 | `#s-think` `.ks3-block.ks3-misconception` | 203–228 | **`misconception`**, kind `predict` (generic shell) — but see §1.6 note 3, the reveal is **two** paragraphs |
| 8 | `#s-ladder` `.ks3-ladder` | 230–298 | **`quiz`** → `r_ladder`. Two marked rungs + two self-marked. Shape identical to B1. |
| 9 | keynote `.ks3-block.ks3-dark.ks3-keynote` | 300–303 | **`summary`** → `key_note` |
| 10 | `section.ks3-layer` | 305–313 | `stretch` layer (`r_layer`) |
| 11 | `div.ks3-endmatter` | 315–337 | `r_endmatter` — **card 2 is headed "Next in this unit"**, see §1.6 note 5 |

## 1.4 Rail — 5 stops (matches NOTES §6)

Rail source: **lines 348–354**. Tick conditions: **lines 555–562**.

| # | anchor | `short` | `label` | ticks when (page's own condition) | proposed `done_when` |
|---|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `Two broken bones` | `hookChoice !== null` | `committed` |
| 2 | `s-switch` | `SWITCH` | `Switch a part off` | `Object.keys(opened).length >= 4` — all four parts *switched off*, not merely predicted | `all_parts_opened` |
| 3 | `s-sort` | `SORT` | `Which job is this` | `Object.keys(sortPick).length >= 6` | `all_items_decided` |
| 4 | `s-think` | `THINK` | `Living or dead` | `thinkChoice !== null` | `committed` |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | `r1 && r2 answered && r3 && r4 checked` | `ladder_complete` |

⚠ **`s-think` is a rail stop, and the generator's standing convention says it must not be.**
`build_ks3.py`'s `ACTIVITY_KIND_RENDERERS` comment (~line 2705) records MRB-208's ruling that the
rail carries "only sections that require the student to do something", concludes *"`#s-think` is a
rail stop on none of the six lessons"*, and therefore emits `confrontation` **without**
`data-stage-done`. **All four B2 pages put `#s-think` in the rail** and tick it on a commitment.
Design's `#s-think` *does* ask for a commitment (four options, gated reveal) — it is a `predict`,
not a B1-style `confrontation`. This is a real divergence and it is Mide's or the commander's call,
not an author's. Building it as drawn needs the section to emit `data-stage-done`.

⚠ **`done_when` is documentation only.** `build_ks3.py` line 3417 puts it in the
`data-rail-stages` JSON and **nothing reads it** — `shared/ks3.js` `doneByDom()` (line 5033)
decides completion from `data-stage-done` on the section, falling back to DOM heuristics. An
instrument that has a completion contract must set `data-stage-done` itself.

## 1.5 Instrument — `system-switch` (DOM-only, **no canvas**)

Markup **110–169**. Payload `PARTS` **356–433**. Logic 595–630.

**Controls**
- Four part tabs (`partTabs`, 596–599; markup 119–123). `seg()` styling, `aria-pressed`.
- Four prediction options per part (`partOptions`, 603–611; markup 132–141). `disabled` once the
  part is opened; a second click on an opened part is a no-op (guard at 608).
- *Switch this part off* button (`onSwitch`, 616–619; markup 145). `disabled` until a prediction is
  committed **and** re-disabled once opened (`switchLocked`, 612). Label flips to `Switched off`.
- Hint line beside the button (`switchHint`, 615): `Commit to a prediction first.` → `Ready.` →
  `Now try another part.`

**Readouts**
- `partName` (mono uppercase) + `partDoes` (20px prose) in an inset panel, markup 125–128.
- Progress counter `N of 4 parts switched off` (595; markup 116).
- The chain, revealed on switch-off: an ink-dark panel (markup 150–161) with `chainTitle` in
  alert-coloured mono caps, then one row per step. **Each row is a `[data-chainrow]` grid:
  `minmax(0,104px) minmax(0,1fr)`, gap 16px, collapsing to one column below 620px** (page-local
  CSS, lines 23–24). Left cell is the level chip; right cell is the step text.
- Level chip colour is data-driven: `Cell` → `var(--ks3-alert)`, everything else →
  `var(--ks3-on-dark-muted)` (625–627). Ground `var(--ks3-dark-panel)`.
- `chainClose` under a 2px `--ks3-dark-rule` (markup 160).
- All-four summary band, `--ks3-band` on 2px ink (markup 164–168), gated on `allSwitched`.

**Payload as actually authored** (⚠ NOTES vs PAGE — NOTES §3.1 gives
`{parts:[{id,name,does,prompt,options[4],chain:[{level,text}],close}], predicted:{}, opened:{}}`;
the page's `PARTS` entries carry **two more authored fields**):

```
PARTS[] = { id, tab, name, does, prompt, options[4], title, chain[4]{level,text}, close }
```
`tab` is the short tab caption (`The marrow inside`) and `name` is the long panel caption
(`The marrow inside the bones`) — they differ on 3 of 4 parts. `title` is the chain panel heading
(`Marrow switched off`). NOTES lists neither. Runtime state is
`{partId, predict:{}, opened:{}}`.

**The chains do not all climb.** Design's §3.1 note is confirmed by the data: skull is
Cell→Tissue→Organ→Organism, ribs is Organ→Organ→Tissue→Cell, femur is Tissue→Organ→Organism→**Cell**,
marrow is Cell→Tissue→Organ→**Cell**. The level chips are a rendering of the data, never a claim
about direction.

**`showLevels` prop** (declared in `data-props`, line 347; read at 623) blanks the level string.
⚠ **Defect: the chip `<span>` still renders** — an empty pill with `padding:5px 11px` and a
`--ks3-dark-panel` background, plus a 104px grid column holding nothing. If the generator supports
the prop it should omit the chip and collapse the grid.

## 1.6 What no existing generator component covers

1. **`system-switch` is new.** It is *close* to `sabotage` (`build_ks3.py` 2170–2255) — both are
   commit-then-chain — but three things do not map:
   - `sabotage` renders `<ol class="ks3-chain">` of `{scale, text}` with **no per-link chip
     styling** and no level colour rule; b2-01 needs a levelled chip whose colour is a function of
     the level string.
   - `sabotage` is **cast-coupled**: `_drawing_for()` (2258–2268) *raises* unless the sabotage's
     specimen is declared by a `system-bench` on the same page. b2-01 has no bench and no cells.
   - `sabotage` paints a `<canvas data-drawing>` per panel from the `CELL_DRAWINGS` set. b2-01 is
     deliberately drawing-free (NOTES flag 17: no anatomical diagrams anywhere in the unit).
   - `sabotage` renders the `practical` ink-dark shell; b2-01's `#s-switch` is a **light**
     `.ks3-block` with an ink-dark panel *inside* it only after the reveal.
2. **The per-item sorter is new.** `#s-sort` reveals **each row the instant that row is decided**
   (`open = pick !== undefined`, 635). Both existing sorters gate the whole set behind one button:
   `sort-rows` (1330–1399, `[data-sort-reveal]`) and `sort-task` (1958–2013, `[data-hard-reveal]`).
   Neither can produce a per-row immediate reveal, and `sort-task` additionally *validates* that
   every item's `answer` is one of the offered `choices` (1981–1986) — which b2-01 violates by
   design: item `i4` answers `Movement and protection — both.`, a string that is not one of the
   four `JOBS` labels. Proposed kind: **`job-sort`**, payload
   `{categories[]{id,label}, items[]{id,text,answer,why}, counter}`.
3. **A two-paragraph misconception reveal.** `#s-think`'s reveal is two `<p>`s (224, 225). The
   generic `predict` shell carries one `reveal`. Either `reveal` becomes rich/multi-paragraph or
   the record needs `reveal[]`.
4. **KEY FACT geometry differs from the shipped component.** Design draws
   `padding: 22px 26px` · `background: var(--ks3-card)` · `border-radius: var(--ks3-r-panel)` ·
   `box-shadow: 6px 6px 0 var(--ks3-accent)` · body **25px/1.32** · `margin-top: 28px`.
   `shared/ks3.css` `.ks3-keyfact` (2430–2457) is `padding: 18px 22px` · band ·
   `box-shadow: 5px 5px 0` · body **22px/1.35** · `margin-top: 24px`. The ground is authorable
   (`ground: "card"`, line 2438); **the shadow offset, the type size and the padding are not**.
   This is a CSS finding for the commander, identical on all four pages.
5. **Endmatter card 2 is "Next in this unit".** `r_endmatter` (3307–3349) is called with the fixed
   headings `Before this lesson` / `Connects to` / `At GCSE this becomes` (3527–3530). Design's
   B2 pages head the middle card **"Next in this unit"** and point forward. Either the heading
   becomes authorable or B2 renders a card Design did not draw.
6. **The `[data-chainrow]` 620px breakpoint** is page-local CSS (lines 23–24) with no equivalent in
   `shared/ks3.css`.

---
---

# 2 · `joints` — MODEL

`docs/ks3/design-reference/b2/b2-02-joints.dc.html` · 896 lines

## 2.1 Identity

| Field | Value | Source |
|---|---|---|
| `slug` | `joints` | `ks3_data/structure.py` line **72** — verified verbatim |
| `title` | `Joints` | structure.py line 72 · page `<h1>` line **80** |
| `family` | `MODEL` | structure.py line 72 |
| eyebrow | `Movement: skeleton and muscles · Model` | page line **79** |
| `big_question` | `Shoulders dislocate all the time. Elbows almost never do. What is the shoulder buying with that risk?` | page line **81** |
| `covers` | `KS3.B.SKEL.01` (the *movement* clause) — NOTES §1 records this lesson **has no statement of its own**; it is a `structure.py` slot | NOTES §1 |
| `<title>` | `Joints · MrBadmusAI KS3` | page line 12 |

## 2.2 Content payload — line ranges for a byte-identical lift

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **367–373** | 5 nodes × `{id, label, short}` |
| **`JOINTS`** | **375–412** | the flagship. 4 joints × `{id, tab, name, bend[2], twist, axes, angleLabel, where, hold, trade, twistYes, twistNo}` |
| ├ `hinge` | 376–384 | `bend: [0,145]`, `twist: false`, `axes: '1'` |
| ├ `ball` | 385–393 | `bend: [0,180]`, `twist: true`, `axes: '3'` |
| ├ `pivot` | 394–402 | `bend: [0,0]`, `twist: true`, `axes: '1 — a turn'` |
| └ `fixed` | 403–411 | `bend: [0,0]`, `twist: false`, `axes: '0'` |
| **`CASES`** | **414–427** | 4 cases × `{id, text, options[5], answer, why}`. `k4` (thumb) answers `None of these.` |
| **`RUNGS`** | **429–446** | r1, r2 |
| **`SELF_RUNGS`** | **448–471** | r3 (5 criteria), r4 (5 criteria) |
| initial `state` | 474–488 | incl. **`angles: { hinge: 20, ball: 40, pivot: 0, fixed: 0 }`** (478) — the per-joint starting angles are authored data |
| lifecycle | 490–512 | IO + `reduced` motion probe + `draw()` + `tick()` |
| `joint()` | 514 | current-joint lookup |
| `tick()` — the twist animation loop | 516–528 | `this.tw += dt * 1.1` |
| **`draw()`** — the whole canvas routine | **530–688** | see §2.5 |
| `seg(on, dark)` | 690–699 | two-branch button style (dark branch is new relative to b2-01) |
| `renderVals()` | 701–891 | |

**Prose living inside `renderVals()`:**

| Payload | Lines | Holds |
|---|---|---|
| **hook options** | **744–749** (4 strings at **745–748**) | |
| **gate options** (the commit that unlocks the bench) | **757–762** (4 strings at **758–761**) | |
| **`benchAlt`** — the aria-label template | **774–776** | matches NOTES §3.2's quoted example exactly, at the default hinge/20° |
| `benchProgress` format | 768 | `'N of 4 joints tried'` |
| `twistLabel` / `twistNote` fallback | 788, 790 | `Try to twist it` / `Twisting` / **`Press it and watch what happens.`** (the only twist-note string not in `JOINTS`) |
| `caseProgress` format | 800 | `'N of 4 decided'` |
| **think options** | **820–825** (4 strings at **821–824**) | |
| `scoreLine` / `scoreNote` | 883–884 | |

**Canvas string literals** (authored, inside `draw()`): `'range of movement: 0 to ' + j.bend[1] + ' degrees'` at **564**; `'range of bending: none'` at **569**; the joint-name chip uses `j.name.toUpperCase()` at 665.

**Static markup prose:**

| What | Lines |
|---|---|
| header | **78–85** |
| `#s-hook` | **87–109** (h2 89, prompt 90, commit 92, reveal **105**) |
| explainer | **111–113** (copy at **112**) |
| `#s-bench` head, lede, commit prompt | **115–139** (h2 119, lede **123**, commit **127**) |
| bench readout captions | 153, **166**, **170**, **174**, 179 (`Directions it moves in` / `Where you have one` / `What holds it together` / `The trade:`) |
| **KEY FACT box** | **184–187** (statement **186**) |
| `#s-cases` head + lede | **189–197** (h2 193, lede **197**) |
| all-cases closing band | **215–219** (copy at **217**) |
| `#s-think` — quote, lede, two reveal paragraphs | **222–247** (quote **227**, lede 228, reveals **243–244**) |
| ladder head + retry note | 249–259, **313–316** |
| keynote | **319–322** (copy at **321**) |
| stretch layer | **324–332** (copy at **330**) |
| endmatter | **334–356** (GCSE prose **349**, tutor prompt 353) |

## 2.3 Block sequence — 11 direct children of `.ks3-lesson`

| # | Section | Lines | Generator block / activity kind |
|---|---|---|---|
| 1 | `header.ks3-lesson-head` | 78–85 | generator-emitted |
| 2 | `#s-hook` `.ks3-block.ks3-dark.ks3-hook` | 87–109 | **`hook`** |
| 3 | `section.ks3-explainer` | 111–113 | **`explainer`** |
| 4 | `#s-bench` `.ks3-block.ks3-dark.ks3-practical` | 115–182 | **NEW** — activity kind `joint-bench`, on a **`practical`** segment (ink-dark, matching `_INSTRUMENT_SEGMENTS`' measured rule for a dark block) |
| 5 | KEY FACT `<div>` (orphan) | 184–187 | **`key-fact`**, `ground: "card"` |
| 6 | `#s-cases` `.ks3-block`, inset ground | 189–220 | **NEW** — same `job-sort` shape as b2-01 §1.6 note 2, **plus a closing band gated on all-decided** |
| 7 | `#s-think` `.ks3-block.ks3-misconception` | 222–247 | **`misconception`**, kind `predict`, two-paragraph reveal |
| 8 | `#s-ladder` `.ks3-ladder` | 249–317 | **`quiz`** |
| 9 | keynote | 319–322 | **`summary`** |
| 10 | `section.ks3-layer` | 324–332 | `stretch` |
| 11 | `div.ks3-endmatter` | 334–356 | `r_endmatter`, card 2 = "Next in this unit" |

No `p.ks3-legal`.

## 2.4 Rail — 5 stops (matches NOTES §6)

Rail source **367–373**; tick conditions **716–723**.

| # | anchor | `short` | `label` | ticks when | proposed `done_when` |
|---|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `Range or stability` | `hookChoice !== null` | `committed` |
| 2 | `s-bench` | `BENCH` | `Drive the joint` | `Object.keys(tried).length >= 4` — `tried` is keyed by **joint id**, set by a tab click (771), a slider move (785) or a twist press (793). Four distinct joints must be touched. | `all_joints_tried` |
| 3 | `s-cases` | `CASES` | `Four places` | `Object.keys(casePick).length >= 4` | `all_cases_decided` |
| 4 | `s-think` | `THINK` | `Tendon or ligament` | `thinkChoice !== null` | `committed` |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete | `ladder_complete` |

Same ⚠ on `s-think` as §1.4.

## 2.5 Instrument — `joint-bench` (**canvas required**)

Markup **115–182**. Payload `JOINTS` **375–412**. Draw routine **530–688**. Animation loop 516–528.

**Commit gate.** ⚠ NOTES vs PAGE — NOTES §3.2 lists three controls and no gate. The page gates the
whole bench behind a four-option commitment: `gateOpen: s.gate === null` (756), `benchOpen:
s.gate !== null` (767). The gate block (markup 125–139) **disappears** when answered and the bench
appears in its place — gating by absence, the same idiom B1 used three times. The gate's four
options are at **757–762**; the prompt at **127** ("Commit first. Your knee and your shoulder are
both joints. How do they compare?"). This is `BODY-05`'s elicitation in NOTES §5.

**Controls**
- Joint tabs ×4 (`jointTabs`, 769–772; markup 143–147). Dark `seg()` branch:
  `--ks3-alert` fill when pressed, transparent + `--ks3-on-dark-muted` border when not.
- Bend slider (`markup 156`), `class="b2-slider"`, `id="b2angle"`, `step="1"`,
  `min="{{ angleMin }}"` = `j.bend[0]`, `max="{{ angleMax }}"` = **`j.bend[1] || 1`** (779 — the
  `|| 1` avoids `min === max`), bound to **both `onChange` and `onInput`** (NOTES §6 confirmed).
  `disabled` when `j.bend[1] === 0` (782) — pivot and fixed, exactly as NOTES says.
  Slider chrome is page-local CSS at **lines 23–29** (`-webkit-`/`-moz-` track and thumb,
  28px alert thumb on a 3px ink ring, greyed thumb when disabled).
- *Try to twist it* toggle (`onTwist`, 791–794; markup 158). Label flips to `Twisting`.

**Readouts**
- `angleLabel` = the joint's own `angleLabel` (`Bend the joint` / `Swing the limb` /
  **`This joint does not bend`**), markup 153.
- `angleValueLabel` = `'20°'` or the literal `'locked'` when `bend[1] === 0` (781), markup 154.
- Three dark-panel tiles (markup 164–177): `axesLabel` (mono 27px), `whereLabel`, `holdLabel`.
- `twistNote` (markup 159), three-way: `j.twistYes` when twisting · `Press it and watch what
  happens.` when it *can* twist but is not · `j.twistNo` when it cannot.
- `tradeNote` on a cream panel with a display-type `The trade:` lead-in (markup 179).

**Canvas.** `<canvas width="1800" height="740">` (markup 150) drawn in a **900 × 370 design space
at a 2× transform** (534, 537). Ink ground `#100D0A`. Pivot at `px = 470, py = 250`; upper bone
250px, lower bone 235px (542–543).
- **Allowed sweep** (549–564): a filled arc of radius `lowerLen * 0.86` from 0 to `-bend[1]`,
  `rgba(143,183,255,0.13)` fill, `rgba(143,183,255,0.5)` 2px dashed `[6,6]` stroke, with the mono
  caption `range of movement: 0 to N degrees` at `(px-250, py+92)`. When `bend[1] === 0` the sweep
  is replaced by the caption `range of bending: none` (565–570).
- **Bones** (572–596): three-pass stroke — 26px `#F4E9D8`, 3px `#100D0A` centre line, 20px
  `#F4E9D8` — giving an outlined bar.
- **The joint** (599–625): a filled circle, radius **27 for `ball`, 20 otherwise**, fill
  `#5C5249` for `fixed` and `#FFC53D` otherwise. `hinge` adds two 4px `#8FB7FF` vertical bars at
  ±20px (the groove). `fixed` adds a seven-stroke `#C6B9A7` jagged seam (620–624).
- **Twist indicator** (628–661), drawn on the moving bone at 0.62 of its length, rotated with it:
  a 20 × 42 ellipse. Twist-capable and twisting → solid `#FFC53D` ring with an 8px orbiting dot
  driven by `Math.sin/cos(this.tw)`. Twist-capable, idle → 3px `#6E655D` dashed `[5,5]` ring.
  **Twist-refused → dashed grey ring PLUS a 5px `#C6B9A7` drawn cross** (652–659). NOTES §3.2's
  "the refusal is drawn (a dashed ring with a drawn cross) **and** written out" — confirmed.
- **Name chip** (663–687): a hand-drawn rounded rect at (24, 24), `#221E1B` fill, `#FFC53D` 2px
  stroke, `j.name.toUpperCase()` in 14px DM Mono.
- **Reduced motion** (492, 546, 642): `prefers-reduced-motion` freezes the orbit at
  `Math.sin(1.2)` / `Math.cos(1.2)` and stops the rAF advancing `this.tw`. The ring still draws
  solid; only the motion stops.

**aria-label** (`benchAlt`, 774–776) is composed, not authored:
`'A two-bone model of a ' + name.toLowerCase() + '. The moving bone is set at ' + angle + ' degrees
within a range of 0 to ' + bend[1] + ' degrees, and the joint ' + (twist ? 'can be turned about its
long axis.' : 'cannot be turned about its long axis at all.')`

**Payload as actually authored** (⚠ NOTES vs PAGE — NOTES §3.2 gives the *runtime state*
`{joint, bend_deg, bend_range, twist_allowed, twisting}`; the *authored* payload is):

```
JOINTS[] = { id, tab, name, bend[2], twist, axes, angleLabel, where, hold, trade,
             twistYes, twistNo }
start_angles = { hinge: 20, ball: 40, pivot: 0, fixed: 0 }      # line 478
gate = { prompt, options[4] }                                    # lines 127, 757–762
```

## 2.6 What no existing generator component covers

1. **`joint-bench` is new, and it is the only B2 instrument whose drawing is genuinely
   parametric.** The nearest shipped canvas engines are the microscope (`_microscope_payload`,
   832–1049) and the four `CELL_DRAWINGS` — a fixed enum of cell portraits. A two-bone linkage
   whose sweep, joint glyph, seam and twist verdict are all functions of `bend[]`/`twist` is not in
   `shared/ks3.js`.
2. **The `b2-slider` control.** No `shared/ks3.css` rule styles `input[type=range]` for KS3 today;
   the 28px alert thumb / 10px dark track chrome is page-local (lines 23–29 here, 23–27 in b2-04).
   It must move into `shared/ks3.css` or the sliders render as browser default on both pages.
3. **The disabled-slider state is meaningful, not decorative.** For `pivot` and `fixed` the slider
   is disabled *and* the value reads `locked` *and* the label reads `This joint does not bend`.
   Three coordinated readouts; a generic range control gives none of them.
4. **A five-option per-item sorter with an "off-model" answer.** `#s-cases` offers
   `['Hinge','Ball and socket','Pivot','Fixed','None of these']` and case `k4` answers
   `None of these.` — the MODEL family's whole point. `sort-task` would refuse this payload at
   build time (1981–1986) unless `None of these` is a declared choice, which it is here; but
   `sort-task` still cannot do the per-row immediate reveal or the closing band.
5. **The closing band gated on all-decided** (markup 215–219) — a `sc-if allCases` panel on
   `--ks3-band`. `sort-task`/`sort-rows` have no equivalent slot. Same shape as b2-01's
   `allSwitched` band, so one slot (`close_all`) serves both.
6. KEY FACT geometry drift, endmatter heading — as §1.6 notes 4 and 5.

---
---

# 3 · `antagonistic-muscle-pairs` — SYSTEM

`docs/ks3/design-reference/b2/b2-03-antagonistic-muscle-pairs.dc.html` · 823 lines

## 3.1 Identity

| Field | Value | Source |
|---|---|---|
| `slug` | `antagonistic-muscle-pairs` | `ks3_data/structure.py` line **73** — verified verbatim |
| `title` | `Antagonistic muscle pairs` | structure.py line 73 · page `<h1>` line **73** |
| `family` | `SYSTEM` | structure.py line 73 |
| eyebrow | `Movement: skeleton and muscles · System` | page line **72** |
| `big_question` | `Every muscle you own can do exactly one thing. So how does an arm come back?` | page line **74** |
| `covers` | `KS3.B.SKEL.03` | NOTES §1 |
| `<title>` | `Antagonistic muscle pairs · MrBadmusAI KS3` | page line 12 |

## 3.2 Content payload — line ranges for a byte-identical lift

**This page has the least of its prose in named constants and the most inside `renderVals()`.
Read the second table as carefully as the first.**

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **359–365** | 5 nodes |
| **`MOVES`** | **367–380** | 4 movements × `{id, text, options[4], answer, why}`. `m4` is the eccentric-contraction case (NOTES flag 13). |
| **`RUNGS`** | **382–399** | r1, r2 |
| **`SELF_RUNGS`** | **401–424** | r3 (5 criteria), r4 (5 criteria) |
| initial `state` | 427–440 | `mode: 'none'`, `dead: {biceps:false, triceps:false}` |
| lifecycle | 442–464 | `this.angle = 10` is the **starting elbow angle** (443) — authored, not in a const |
| `acting()` | 466–472 | which muscle is actually pulling once the kill switches apply |
| **`target()`** | **474–480** | the mechanism: both → hold; biceps → **135**; triceps → **6**; neither → **6** |
| **`tick()`** | **482–497** | one rAF loop mutating `this.angle`; rate **90 °/s pulled, 55 °/s falling** (490) |
| `band()` — the muscle-belly draw helper | 499–514 | |
| **`draw()`** | **516–599** | see §3.5 |
| `seg(on, dark)` | 601–610 | identical to b2-02's |
| `renderVals()` | 612–819 | |

**Prose living inside `renderVals()` — this is where the lesson's science lives:**

| Payload | Lines | Holds |
|---|---|---|
| **`note` — the seven-branch interpretation ladder** | **623–638** | the single most important authored block on this page. Seven mutually exclusive strings: biceps-dead (625), triceps-dead (627), both-dead (629), both-pulling (631), biceps-pulling (633), triceps-pulling (635), **neither (637 — the gravity line NOTES flag 15 names)** |
| **hook options** | **671–676** (4 strings at **672–675**) | |
| **gate options** | **684–689** (4 strings at **685–688**) | `BODY-09`'s elicitation |
| **`modeTabs`** | **696–704** (labels at **697–700**) | `Biceps` / `Triceps` / `Both` / `Neither` |
| **`killTabs`** | **705–714** (labels at **706–707**) | `Biceps off` / `Triceps off` |
| **`benchAlt`** — aria-label template | **716–718** | |
| **`benchStatus`** — four-branch status line | **719–722** | |
| `bicepsState` / `tricepsState` | 724–725 | `switched off` / `contracted` / `relaxed` |
| `benchProgress` format | 695 | `'N of 4 settings tried'` |
| `moveProgress` format | 728 | `'N of 4 decided'` |
| **think options** | **747–752** (4 strings at **748–751**) | |
| `scoreLine` / `scoreNote` | 810–811 | |

**Canvas string literals** (inside `draw()`, authored): the two muscle labels at **584** and
**586** — `'BICEPS · IN FRONT'` / `'TRICEPS · BEHIND'` each suffixed
`' — SWITCHED OFF'` / `' — PULLING'` / `' — RELAXED'`.

**Static markup prose:**

| What | Lines |
|---|---|
| header | **71–78** |
| `#s-hook` | **80–102** (h2 82, prompt 83, commit 85, reveal **98**) |
| explainer | **104–106** (copy at **105**) |
| `#s-bench` head, lede, commit prompt | **108–132** (h2 112, lede **116**, commit **120**) |
| bench control captions | **138** (`Contract`), **146** (`Switch a muscle off`) |
| bench readout captions | **164** (`Elbow angle`), **168** (`Biceps · in front`), **172** (`Triceps · behind`), 177 (`What this tells you:`) |
| **KEY FACT box** | **182–185** (statement **184**) |
| `#s-pairs` head + lede | **187–195** (h2 191, lede **195**) |
| `#s-think` — quote, lede, two reveal paragraphs | **214–239** (quote **219**, lede 220, reveals **235–236**) |
| ladder head + retry note | 241–251, **305–308** |
| keynote | **311–314** (copy at **313**) |
| stretch layer | **316–324** (copy at **322** — the co-contraction extension, NOTES flag 14) |
| endmatter | **326–348** (GCSE prose **341**, tutor prompt 345) |

## 3.3 Block sequence — 11 direct children of `.ks3-lesson`

| # | Section | Lines | Generator block / activity kind |
|---|---|---|---|
| 1 | `header.ks3-lesson-head` | 71–78 | generator-emitted |
| 2 | `#s-hook` `.ks3-block.ks3-dark.ks3-hook` | 80–102 | **`hook`** |
| 3 | `section.ks3-explainer` | 104–106 | **`explainer`** |
| 4 | `#s-bench` `.ks3-block.ks3-dark.ks3-practical` | 108–180 | **NEW** — activity kind `muscle-pair`, on a **`practical`** segment |
| 5 | KEY FACT `<div>` (orphan) | 182–185 | **`key-fact`**, `ground: "card"` |
| 6 | `#s-pairs` `.ks3-block`, inset ground | 187–212 | **NEW** — `job-sort` shape again; **no** closing band on this one |
| 7 | `#s-think` `.ks3-block.ks3-misconception` | 214–239 | **`misconception`**, kind `predict`, two-paragraph reveal |
| 8 | `#s-ladder` `.ks3-ladder` | 241–309 | **`quiz`** |
| 9 | keynote | 311–314 | **`summary`** |
| 10 | `section.ks3-layer` | 316–324 | `stretch` |
| 11 | `div.ks3-endmatter` | 326–348 | `r_endmatter`, card 2 = "Next in this unit" |

No `p.ks3-legal`.

## 3.4 Rail — 5 stops (matches NOTES §6)

Rail source **359–365**; tick conditions **643–650**.

| # | anchor | `short` | `label` | ticks when | proposed `done_when` |
|---|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `Only ever a pull` | `hookChoice !== null` | `committed` |
| 2 | `s-bench` | `BENCH` | `Two muscles, one elbow` | `Object.keys(tried).length >= 4` | `four_settings_tried` |
| 3 | `s-pairs` | `PAIRS` | `Four movements` | `Object.keys(movePick).length >= 4` | `all_moves_decided` |
| 4 | `s-think` | `THINK` | `Relax or stretch` | `thinkChoice !== null` | `committed` |
| 5 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete | `ladder_complete` |

⚠ **Stage 2's counter is over a mixed key space.** `tried` takes keys from **two** namespaces:
mode ids `biceps` / `triceps` / `both` / `none` (703) **and** kill ids `off-biceps` / `off-triceps`
(712). The label reads `N of 4 settings tried`, but 4 keys is reachable as 2 modes + 2 kills, or
4 modes + 0 kills. The counter is honest about "settings touched" and dishonest about "all four
contraction modes tried". An author reproducing it should reproduce the behaviour and flag it;
tightening it to the four modes would contradict the drawn label. Same ⚠ on `s-think` as §1.4.

## 3.5 Instrument — `muscle-pair` (**canvas required, animated**)

Markup **108–180**. Mechanism 466–497. Draw 499–599. Copy 623–638, 671–726.

**Commit gate** — same idiom as b2-02: gate options 684–689, prompt at **120**, `gateOpen`/
`benchOpen` at 683/694. The gate disappears when answered.

**Controls**
- `Contract` — four exclusive mode tabs (696–704; markup 137–143).
- `Switch a muscle off` — two independent toggles (705–714; markup 145–152). Both may be on.

**Readouts**
- `benchStatus` under the canvas (719–722; markup 158) — four branches.
- Three dark tiles (markup 162–175): live `angleLabel` (`Math.round(this.angle) + '°'`, 723) in
  mono 27px alert; `bicepsState`; `tricepsState`.
- `benchNote` on a cream panel with a display-type `What this tells you:` lead (markup 177), driven
  by the seven-branch ladder at 623–638.

**Mechanism** (this is the teaching, not chrome):
```
acting()  bi  = (mode === 'biceps'  || mode === 'both') && !dead.biceps
          tri = (mode === 'triceps' || mode === 'both') && !dead.triceps
target()  bi && tri → this.angle   (the joint LOCKS wherever it is)
          bi        → 135
          tri       → 6
          neither   → 6            (falls under gravity)
tick()    rate = (!bi && !tri) ? 55 : 90 °/s     — falling is SLOWER than pulling
```
NOTES §3.3's "gravity straightens a hanging arm for free" is implemented as the 55-vs-90 rate
difference, and the student meets it by pressing **Neither**. Do not flatten the two rates.

**Canvas.** `<canvas width="1800" height="740">` (markup 156), 900 × 370 design space at 2×
(520, 523). Ink ground `#100D0A`. Shoulder `(380, 70)`, elbow `(380, 232)`, forearm 168px
(529–533). **0° is the forearm hanging straight down**, opening towards +x (531–532).
- **Muscles are drawn behind the bones** (551–559) as quadratic-curve bellies via `band()`
  (499–514). Insertions: biceps 46px along the forearm, triceps 30px behind the elbow (552–553).
  Origins ±16px at the shoulder (554–555).
  **Thickness encodes contraction**: biceps 34 when pulling else 20; triceps 30 else 18 (558–559).
  **Colour encodes state**: `#4A4038` dead · `#FFC53D` pulling · `#8A7A62` relaxed (556–557).
- **Bones** (535–549, 561–562): black casing + `#F4E9D8` core, 22px upper / 20px forearm.
- **Elbow** `#C6B9A7` r15; **hand** `#F4E9D8` r16 (565–578).
- **Labels** at (600, 44) and (40, 44), colour `#6E655D` when dead else `#FFC53D` (581–586).
- **Angle arc** `#8FB7FF` r58 at the elbow with the rounded degree readout at
  `(el.x+34, el.y+84)` (589–597).
- **Reduced motion**: `this.reduced` is probed at 444 but — ⚠ — the tick loop **does not check
  it**. b2-02 gates its animation on `!this.reduced` (522); b2-03 does not. The arm animates under
  `prefers-reduced-motion: reduce`. This is a defect on Design's page, not a design choice; a
  reduced-motion build should snap to `target()` instead of easing. Say so if you fix it.

**Payload as actually authored** (⚠ NOTES vs PAGE — NOTES §3.3 gives runtime state
`{mode, dead:{biceps,triceps}, angle_deg}`. The **authored** payload is not a list at all — it is
seven interpretation strings, four status strings, three state words, two mode-tab label sets and
two canvas label stems, all inline in `renderVals()` and `draw()`):

```
muscle_pair = {
  gate:        { prompt, options[4] },
  modes:       [{id, label}] × 4,
  kills:       [{id, label}] × 2,
  status:      { both, biceps, triceps, none },          # 719–722
  states:      { dead, contracted, relaxed },            # 724–725
  notes:       { biceps_dead, triceps_dead, both_dead,
                 both, biceps, triceps, none },          # 623–638
  canvas_labels: { biceps, triceps, off, pulling, relaxed },   # 584–586
  start_angle: 10,                                       # 443
  targets:     { biceps: 135, triceps: 6, none: 6 },     # 476–479
  rates:       { pull: 90, fall: 55 },                   # 490
  alt:         <template>                                # 716–718
}
```

## 3.6 What no existing generator component covers

1. **`muscle-pair` is new and is the only B2 instrument with a continuous physical state.** It is
   not `sabotage` (no chain, no cells, no canvas enum), not `system-bench` (which validates
   `specimens[].drawing ∈ CELL_DRAWINGS` and `specimens[].tuning`, 2101–2113), and not any generic
   kind. The 7 × interpretation ladder alone has no slot anywhere in the current vocabulary.
2. **Two independent toggle groups in one instrument** — an exclusive 4-tab group *and* a
   non-exclusive 2-toggle group, whose product decides the readout. No shipped instrument has this
   control topology.
3. **A rAF-driven readout.** `angleLabel` (723) reads `this.angle`, an *instance field* mutated by
   the animation loop, not state. `renderVals()` is only recomputed when a control changes
   (NOTES §6), so the degree tile updates on interaction, while the canvas updates every frame.
   Whatever `shared/ks3.js` does here must keep that split or the page repaints 60×/s.
4. **Reduced-motion gap** (see above) — a defect to fix inside the drawn component, stated.
5. `job-sort` per-item sorter — as §1.6 note 2.
6. KEY FACT geometry drift, endmatter heading — as §1.6 notes 4 and 5.

---
---

# 4 · `biomechanics-forces-in-the-body` — QUANTITATIVE

`docs/ks3/design-reference/b2/b2-04-biomechanics-forces-in-the-body.dc.html` · 1,028 lines

## 4.1 Identity

| Field | Value | Source |
|---|---|---|
| `slug` | `biomechanics-forces-in-the-body` | `ks3_data/structure.py` line **74** — verified verbatim |
| `title` | `Biomechanics: forces in the body` | structure.py line 74 · page `<h1>` line **78** |
| `family` | `QUANTITATIVE` | structure.py line 74 |
| eyebrow | `Movement: skeleton and muscles · Quantitative` | page line **77** |
| `big_question` | `Holding a 2 kg dumbbell, your biceps pulls with about 160 newtons. Why is it working eight times harder than the weight it is holding?` | page line **79** |
| `covers` | `KS3.B.SKEL.02` | NOTES §1 |
| `<title>` | `Biomechanics: forces in the body · MrBadmusAI KS3` | page line 12 |
| ownership | structure.py line 74 has **no `owned_by` marker** — this is an owned B2 slot. NOTES flag 1 is the open ruling, and it is Mide's. Design taught it as *turning effect = force × distance from the joint*; the word **moment** appears nowhere on the page (verified). | |

## 4.2 Content payload — line ranges for a byte-identical lift

| Payload | Lines | Holds |
|---|---|---|
| `RAIL` | **517–524** | **6** nodes |
| **`G`** | **526** | `const G = 10;   // N/kg, the KS3 convention` — NOTES flag 2 |
| **`WORKED`** | **528–533** | the FIFA worked example. 4 steps × `{letter, label, line, note}`. Letters **F · I · F · A**; labels **Formula · Insert · Fine-tune · Answer** (the round-2 rename NOTES change-log item 1 records). |
| **`COVERS`** | **535–539** | the cover-triangle results. `{T: {result, sentence}, F: {…}, d: {…}}` |
| **`METERS`** | **541–545** | 3 rows × `{name, readings, mean}` — 305 N / 203 N / 1422 N (NOTES flag 16) |
| **`RUNGS`** | **547–564** | r1 (a calculation), r2 |
| **`SELF_RUNGS`** | **566–589** | r3 (5 criteria), r4 (5 criteria, incl. the 50 N / 5 N m / 30 N m arithmetic) |
| initial `state` | 592–614 | `load` seeded from `startLoad`; **`ins: 4`, `hand: 32`, `cover: 'F'`** are authored defaults |
| lifecycle | 616–632 | IO + `draw()` only — **no animation loop** (NOTES §6 confirmed) |
| **`muscleForce()`** | **634–637** | `(load × G × hand/100) / (ins/100)` |
| `arrow()` helper | 639–657 | |
| **`draw()`** | **659–764** | see §4.5 |
| `seg(on, dark, dis)` | 766–775 | three-argument variant |
| `renderVals()` | 777–1023 | |

**Prose living inside `renderVals()`:**

| Payload | Lines | Holds |
|---|---|---|
| **hook options** | **823–828** (4 strings at **824–827**) | |
| **gate options** | **836–841** (4 strings at **837–840**) | `BODY-10`'s elicitation |
| `benchProgress` | 847 | `Meter fitted` / `Meter not fitted yet` |
| `handTabs` | 854–857 | the two hand distances `[32, 16]`, label `'N cm'` |
| **`benchAlt`** | **859–861** | aria-label template |
| **`muscleTile`** | **864** | `'not measured — you work it out'` until the meter is fitted |
| **`meterLabel` / `meterNote`** | **866, 868–870** | `Fit a force meter to the tendon` → `Meter reading shown`; the two-branch note |
| **`coverTabs`** | **876–880** (labels at **877–879**) | ⚠ button order on the page is **Cover F, Cover T, Cover d** and the default cover is **`F`** (601) |
| `workedProgress` / `workedBtnLabel` | 889, 894 | `'Step N of 4'`; `Show the first step` / `Show the next step` / `All four shown` |
| `buildHead` | **898** | `'Your rig: N kg at N cm, muscle at N cm.'` |
| **`formPicks`** | **899–903** (3 strings at **900–902**) | step 1 distractors |
| **`insertPicks`** | **908–912** (3 templates at **909–911**) | step 2 distractors, **computed from the student's own rig** |
| **`buildSteps`** | **928–933** (4 objects at **929–932**) | the student's rig, done four ways — a second full FIFA set, distinct from `WORKED` |
| **`buildClose`** | **937** | `'You wrote X Y. The worked answer is N N. Fit the force meter on the rig and it reads the same.'` |
| `buildProgress` | 924–925 | `'N of 3 lines committed'` / `'Opened'` |
| **`rankOptions`** | **940–944** (3 strings at **941–943**) | |
| `meterProgress` | 939 | `Not ranked yet` / `Ranked` |
| **think options** | **952–957** (4 strings at **953–956**) | |
| `scoreLine` / `scoreNote` | 1015–1016 | |

**Canvas string literals** (inside `draw()`): `'ELBOW'` at **724**; `'muscle'` and the computed
`'N N'` force label at **740–741**; `'THE FOREARM RIG · SIDE VIEW'` at **763**.

**Static markup prose:**

| What | Lines |
|---|---|
| header | **76–83** |
| `#s-hook` | **85–107** (h2 87, prompt **88**, commit 90, reveal **103**) |
| explainer | **109–111** (copy at **110**) |
| `#s-bench` head, lede, commit prompt | **113–137** (h2 117, lede **121**, commit **125**) |
| bench control captions | **144** (`Mass in the hand`), **151** (`Muscle attached at`), **157** (`Hand distance`) |
| bench readout captions | **172**, **176**, **180**, **184** (`Weight of the load` / `Load, from the elbow` / `Muscle, from the elbow` / `Force in the muscle`) |
| **the triangle section** — eyebrow, heading, SVG letters, the three prose lines | **197–234** (eyebrow 198, heading **199**, SVG `T`/`F`/`×`/`d` at **204–207**, `Two things side by side…` at **229**, the T/F/d unit legend at **230**, **`Nothing moving: F₁ × d₁ = F₂ × d₂` at 231**) |
| worked-example head | **236–243** (eyebrow 239, h2 **240**) |
| worked-example footer copy | **258** (`Now the same four steps on your own rig.`) |
| `#s-build` head + lede | **262–265** (eyebrow 263, lede **265**) |
| `#s-build` step captions and prompts | **269–270**, **279–280**, **289–290** |
| unit `<select>` options | **296–301** (`choose a unit`, `N`, `kg`, `m`, `N m`) |
| `#s-build` reveal heading | **313** (`Your rig, done four ways`) |
| **KEY FACT box** | **329–332** (statement **331**) |
| `#s-meters` head + lede | **334–342** (h2 338, lede **342**) |
| meter card captions | **363** (`mean of three`) |
| meters closing band | **367** |
| `#s-think` — quote, lede, two reveal paragraphs | **372–397** (quote **377**, lede 378, reveals **393–394**) |
| ladder head + retry note | 399–409, **463–466** |
| keynote | **469–472** (copy at **471**) |
| stretch layer | **474–482** (copy at **480** — the Achilles/sprinter extension) |
| endmatter | **484–504** (**card 2 is headed `Taught in full in` and carries PROSE, not links**, 491–494; GCSE prose **497**; tutor prompt 501) |
| **`p.ks3-legal`** | **506** | `Weight in newtons is taken as mass in kilograms × 10 N/kg throughout.` |

## 4.3 Block sequence — 15 direct children of `.ks3-lesson`

| # | Section | Lines | Generator block / activity kind |
|---|---|---|---|
| 1 | `header.ks3-lesson-head` | 76–83 | generator-emitted |
| 2 | `#s-hook` `.ks3-block.ks3-dark.ks3-hook` | 85–107 | **`hook`** |
| 3 | `section.ks3-explainer` | 109–111 | **`explainer`** |
| 4 | `#s-bench` `.ks3-block.ks3-dark.ks3-practical` | 113–195 | **NEW** — activity kind `arm-lever`, on a **`practical`** segment |
| 5 | the triangle `<section>` — **no id, no class**, inline `--ks3-band` on a 3px ink border, `--ks3-r-block` radius, 32px padding | 197–234 | **`formula`** with `triangle` → `r_formula` (3149–3169) + `r_formula_triangle` (1562–1631). **Partially covered** — see §4.6 note 2 |
| 6 | `section.ks3-block.ks3-worked` — **no id** | 236–260 | **`worked-example`** activity, `kind: "worked-example"`, `staged: True`, `fifa: WORKED` → `r_fifa(staged=True)` (2598–2646). **Partially covered** — see §4.6 note 3 |
| 7 | `#s-build` `.ks3-block`, inset ground | 262–327 | **NEW** — activity kind `lever-steps`. **Not** `fifa-construct` — see §4.6 note 4 |
| 8 | KEY FACT `<div>` (orphan) | 329–332 | **`key-fact`**, `ground: "card"` |
| 9 | `#s-meters` `.ks3-block` (default ground) | 334–370 | **NEW** — activity kind `meter-compare`; the statutory "measurement of force exerted by different muscles" |
| 10 | `#s-think` `.ks3-block.ks3-misconception` | 372–397 | **`misconception`**, kind `predict`, two-paragraph reveal |
| 11 | `#s-ladder` `.ks3-ladder` | 399–467 | **`quiz`** |
| 12 | keynote | 469–472 | **`summary`** |
| 13 | `section.ks3-layer` | 474–482 | `stretch` |
| 14 | `div.ks3-endmatter` | 484–504 | `r_endmatter` — card 2 is **`Taught in full in`** and is **prose**, not a list |
| 15 | `p.ks3-legal` | 506 | the g = 10 N/kg convention line |

⚠ Blocks 5 and 6 carry **no `id`**, so they are not rail targets and take no anchor. Block 6 does
carry `scroll-margin-top: 92px` anyway. The generator's `_id_attr` (3225–3235) emits nothing
without an `anchor`, which is correct here.

## 4.4 Rail — 6 stops (matches NOTES §6: "the extra one is the force-meter comparison the statutory statement asks for")

Rail source **517–524**; tick conditions **794–802**.

| # | anchor | `short` | `label` | ticks when | proposed `done_when` |
|---|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | `Eight times harder` | `hookChoice !== null` | `committed` |
| 2 | `s-bench` | `RIG` | `The forearm rig` | `Object.keys(touched).length >= 2 && meterShown` — **two of the three controls moved AND the meter fitted** | `rig_measured` |
| 3 | `s-build` | `STEPS` | `Your own four steps` | `buildOpen` | `steps_opened` |
| 4 | `s-meters` | `METERS` | `Three force meters` | `rankChoice !== null` | `ranked` |
| 5 | `s-think` | `THINK` | `What levers buy` | `thinkChoice !== null` | `committed` |
| 6 | `s-ladder` | `LADDER` | `Mastery ladder` | ladder complete | `ladder_complete` |

`touched` keys are `load` / `ins` / `hand`, set at 850, 853, 856. Same ⚠ on `s-think` as §1.4.
Note the worked example (block 6) and the triangle (block 5) are **deliberately not rail stops** —
they demand nothing the rail can record.

## 4.5 Instruments

### 4.5.1 `arm-lever` (**canvas required, static — no animation**)

Markup **113–195**. Force law **634–637**. Draw **659–764**. Copy 823–871.

**Commit gate** — options 836–841, prompt at **125** ("You move the load from 32 cm out to 16 cm —
half the distance. What happens to the force the muscle needs?"). Same disappear-on-answer idiom.

**Controls** (all three exactly as NOTES §3.4 says)
- `Mass in the hand` — range `min=0.5 max=5 step=0.5`, `id="b2load"`, bound to **`onChange` and
  `onInput`** (markup 147).
- `Muscle attached at` — range `min=3 max=6 step=0.5`, `id="b2ins"`, both events (markup 154).
- `Hand distance` — two tabs, **32 cm / 16 cm** (854–857; markup 158–162).
- *Fit a force meter to the tendon* — one-way button, `disabled` once fitted (865, 871;
  markup 190).

**Readouts** — four dark tiles (markup 170–187):
`weightLabel` (`W = load × 10`, mono 25px) · `handLabel` · `insLabel` ·
**`muscleTile`, which reads `not measured — you work it out` until the meter is fitted (864)** and
only then shows `F.toFixed(0) + ' N'`.
NOTES §3.4's design note is load-bearing: *"If Code makes the meter reading available before the
calculation, the lesson is gone."* The tile is the gate.
`meterNote` beside the button, two branches (868–870).

**Canvas.** `<canvas width="1800" height="700">` (markup 167), **900 × 350** design space at 2×
(663, 666). Ink ground `#100D0A`. **Scale 17 px per cm** (671). Elbow at `(150, 190)`;
`handX = 150 + hand × 17`; `insX = 150 + ins × 17` (672–674). Everything is a function of state,
which is why NOTES calls it "a static drawing driven by two sliders".
- Upper arm: vertical, 128px, black casing + `#F4E9D8` core (677–689).
- Muscle: a `#FFC53D` 15px quadratic curve from `(el.x+16, el.y-118)` to `(insX, el.y-12)`
  (691–697) — **the curve moves with the insertion slider**.
- Forearm: horizontal to `handX`, same two-pass treatment (699–711).
- Elbow: `#C6B9A7` r16 with the mono caption `ELBOW` below (713–724).
- Load: a hand circle at `handX`, then a `#8FB7FF` block whose **width `34 + load × 7` and height
  `26 + load × 3` both grow with the mass** (726–737).
- **Two force arrows** (740–741) via `arrow()` (639–657): the muscle arrow at `insX` pointing up,
  labelled `muscle`; the load arrow at `handX + 46` pointing down, labelled with the computed
  weight in N. The muscle arrow is **never labelled with its magnitude** — same gate as the tile.
- **Two dimension lines** (744–758) via a local `dim()` closure: `--` the muscle distance at
  `y + 92` in `#FFC53D`, the load distance at `y + 132` in `#8FB7FF`, each with end ticks and a
  centred mono caption.
- Corner caption `THE FOREARM RIG · SIDE VIEW` (760–763).

**aria-label** (`benchAlt`, 859–861) is composed from the three live values.

**Payload as authored** (⚠ NOTES vs PAGE — NOTES §3.4's
`{load_kg, d_muscle_cm, d_load_cm, g: 10, meter_fitted}` is the runtime state; the authored payload
is the ranges, the tab set, the two tile strings, the two meter strings and the gate):

```
arm_lever = {
  gate:   { prompt, options[4] },
  load:   { min: 0.5, max: 5, step: 0.5, default: 2, label: 'Mass in the hand' },
  ins:    { min: 3,   max: 6, step: 0.5, default: 4, label: 'Muscle attached at' },
  hand:   { options: [32, 16], default: 32, label: 'Hand distance' },
  g:      10,
  tiles:  { weight, load_distance, muscle_distance, muscle_force },
  unmeasured: 'not measured — you work it out',
  meter:  { label, label_done, note, note_done },
  alt:    <template>
}
```

### 4.5.2 `cover-triangle` (DOM/SVG, **no canvas**)

Markup **197–234**. Payload `COVERS` **535–539**. Logic 873–887.

**Controls** — three buttons (876–885; markup 222–226), in the page's own order
**`Cover F`, `Cover T`, `Cover d`**, `aria-pressed`, ink fill when pressed. Default cover is
**`F`** (state line 601) — the page loads with F already covered, which is the arrangement the
lesson actually needs.

**Readouts**
- The SVG (markup 201–220), `viewBox="0 0 300 214"`, `role="img"` with the aria-label
  *"A formula triangle: turning effect on top, force and distance from the joint underneath,
  multiplied together."* (line 201).
  Triangle path `M150 8L290 200H10Z`; divider `line x1=66 y1=120 x2=234 y2=120`;
  letters `T` (150, 100), `F` (106, 182), `×` (150, 178), `d` (196, 182) — **all four are literal
  `<text>` elements, not data**.
- Three cover plates, each a `sc-if` on `coverTop`/`coverLeft`/`coverRight` (873–875):
  `rect` + a **ghost letter in `--ks3-ink-ghost` on top of the plate**, so the covered quantity
  stays faintly visible (markup 208–219). NOTES change-log confirms this is deliberate.
- `coverResult` in display 800/30px (markup 227) — e.g. `T = F × d`.
- `coverSentence` in 19px prose (markup 228).
- Three fixed prose lines below (markup 229, 230, 231): the multiply/divide rule, the T/F/d unit
  legend (mono, `<br>`-separated), and **`Nothing moving: F₁ × d₁ = F₂ × d₂`** in display 700/21px.
  NOTES change-log records the last one was reworded from a fourth arrangement into a condition.
- **Reduced motion:** nothing animates; the plate simply appears (NOTES). Confirmed — no
  transition or animation on the covers.

**Payload as authored** (⚠ NOTES vs PAGE — the change-log's
`{shape, cells:[{id,label,slot}], covered, results:{id:{result,sentence}}}` describes an
instrument more general than the page. The page has **no `cells` array and no `shape` field**;
the three cells and their slots are hard-coded SVG text at 204–207):

```
COVERS = { T: {result, sentence}, F: {result, sentence}, d: {result, sentence} }
buttons  = ['Cover F', 'Cover T', 'Cover d']     # in that order
default  = 'F'
```

## 4.6 What no existing generator component covers

1. **`arm-lever` is new.** No shipped engine draws a scaled side-view linkage with force arrows and
   dimension lines. It is the cheapest of the three canvas instruments to build (static, no rAF)
   and the most important to get right, because the whole lesson turns on the muscle-force tile
   staying blank.
2. **The formula triangle is COVERED but not fully.** `r_formula` + `r_formula_triangle` already
   exist and are the *corrected* geometry (derived 260 × 216 covers, clipped to the path —
   1523–1559 explains why Design's authored rects overhang). Adopt the generator's version. Three
   real gaps:
   - **No `result` slot.** `r_formula_triangle` gives each cell a `label`, a `button` and one
     `text` note (1589–1606). Design shows **two** things per cover: the arrangement
     (`T = F × d`) in display 800/30px, and a sentence in prose. Folding them into one `text`
     loses the display-type line, which is the thing a student reads. Needs
     `top/left/right: {label, button, result, text}`.
   - **`close` is one paragraph** (1608–1609). Design has **three** distinct trailing blocks:
     the multiply/divide rule (229), the mono unit legend with `<br>`s (230), and the
     balanced-condition line in display type (231). Needs `close[]` or three named slots
     (`rule`, `units`, `condition`).
   - **Button order and default.** The generator emits buttons in fixed `top, left, right` order
     (1597–1601) and pre-presses none. Design ships `F, T, d` with `F` already covered.
3. **The FIFA badge treatment is new.** NOTES change-log item 1 makes the badges the point:
   *"FIFA is now visible as FIFA."* Design draws each step as a **card** — 38px rounded-square
   badge in `--ks3-accent-text` on `--ks3-ground`, mono uppercase label, display 800/26px line,
   prose note — inside an inset panel with a 2px option border (markup 246–253).
   `r_fifa` (2598–2646) emits `<p class="ks3-fifa-step"><strong>letter · name</strong> line
   <span class="ks3-fifa-note">…` — one paragraph, no badge, no card, no per-step ground.
   `shared/ks3.css` has `.ks3-fifa` (819–830) and a `.ks3-fifa-letter` badge (3037) but the badge
   belongs to `fifa-construct`'s **fields**, not to the worked example's steps. The staged
   mechanics (`data-stepper`, 4889) are right and reusable; the **drawing is not**.
4. **`#s-build` is new, and `fifa-construct` is the wrong shape for it.** `r_fifa_construct`
   (1444–1517) is *n* free-text fields + a model reveal + criteria ticks, and it **hard-asserts
   `len(fields) == len(model) == len(success)`** (1464–1469) and that the field letters match the
   stepper's letters in order (1471–1480). Design's `#s-build` is:
   - Step 1 · Formula → **three multiple-choice lines** (899–907), one correct
   - Step 2 · Insert → **three multiple-choice lines computed from the student's own rig values**
     (908–916) — the distractors are generated, not authored
   - Steps 3 and 4 → **a free-text number field + a `<select>` unit picker** (markup 291–302),
     with a visually-hidden label each
   - a reveal button gated on **all three lines committed** (922–923), then a 4-step ink-dark FIFA
     panel built from the student's rig (928–936), closing with `buildClose` (937) which quotes
     back what the student wrote
   Nothing in that maps onto `fifa-construct`. Proposed kind **`lever-steps`**, and it needs the
   engine to compute `insertPicks` and `buildSteps` from live control values — the first B2
   instrument whose *option text* is a function of another instrument's state.
5. **`#s-meters` is new.** A three-option ranking commitment, then a reveal of three structured
   cards (`name` / `readings` mono / `mean` display 800/30px / the fixed caption `mean of three`)
   and a closing `--ks3-band` band. `reveal-cards` is in `GENERIC_ACTIVITY_KINDS` — meaning the
   claim is that prompt/options/reveal *is* its drawn component — which is exactly the MRB-205
   failure here: Design drew a card grid with four typed fields per card. Proposed kind
   **`meter-compare`**, payload `{prompt, options[3], rows[]{name, readings, mean}, mean_label,
   close}`.
6. **Endmatter card 2 is `Taught in full in` and carries PROSE.** `r_endmatter` (3307–3319)
   renders `<h2>heading</h2><ul>items</ul>` and **skips any card with no items** — a prose-only
   card cannot be expressed. This is the editorial half of NOTES flag 1 (the P4 ownership pointer)
   and it will not render without a change. `before_this` / `ks4_becomes` (3520–3525) already show
   the pattern for prose-in-a-card; this needs a third.
7. **The `b2-slider` chrome** (page-local CSS 23–27) — same finding as §2.6 note 2.
8. **`p.ks3-legal` collision.** Design's legal line is the g-convention note; the generator appends
   `LEGAL_LINE` (the copyright line) unconditionally at 3537 and puts `safety_note` *above* it
   (3534–3536). The convention note is not a safety note. Either `safety_note` widens or a
   `convention_note` slot is added; shipping it through `safety_note` would put "Weight in newtons
   is taken as…" under a class named `ks3-safety`.
9. KEY FACT geometry drift — as §1.6 note 4.

---
---

# CROSS-LESSON

## C1 · The unit spine — identical on all four pages

Every page has the same five top-level landmarks and the same shell:

- `nav.ks3-nav` with the KS3 brand tile + inline breadcrumb (b2-01 30–44, b2-02 35–49,
  b2-03 28–42, b2-04 33–47). Four crumbs, the third being the unit index (`index.html`), the
  fourth `aria-current="page"`.
- `nav[data-rail="top"]` sticky, `z-index: 20` — count / label / 96px bar.
- `nav[data-rail="side"]` fixed, `top: 150px`, `left: calc(50% - 632px)`, width 104px,
  `display: none` below **1340px** (page-local CSS line 20–21 on all four).
- `main.ks3-main > div.ks3-lesson`.
- `footer.ks3-footer` — `MrBadmusAI · Key Stage 3 Science`.

Page-local CSS shared by all four (lines 14–22): the `b2-arrive` keyframe
(`translateY(6px)` + fade, .34s, `[data-arrive]`), the 1340px rail swap, and the
`prefers-reduced-motion` kill for `[data-arrive]`. **The arrive animation is the unit's one
shared motion primitive and it is correctly reduced-motion-gated on every page.**

Every reveal panel in the unit carries `data-arrive="1"`.

## C2 · The mastery ladder is byte-for-byte the same instrument on all four pages

Markup: b2-01 **230–298** · b2-02 **249–317** · b2-03 **241–309** · b2-04 **399–467**.
Logic: b2-01 663–720 · b2-02 832–889 · b2-03 759–816 · b2-04 964–1021.

Four rungs every time — **two page-marked (`RUNGS`), two self-marked (`SELF_RUNGS`)**, sub-heading
`Four rungs. Two the page marks, two you mark.`, score line `You got N of 4.`, note
`You marked rungs 3 and 4 yourself.`, retry button `Retry my misses` with the note
`Clears the ticks on rungs 3 and 4 and keeps what you wrote.`
Feedback words are `Correct.` / `Not this one.` on every page.
Every self-rung has **five** criteria on every page (8 self-rungs × 5 = 40 criteria across B2).
`r_ladder` (2989) already renders this shape — no new work, but the `correction` strings on wrong
options are science-bearing and must be lifted verbatim.

## C3 · The KEY FACT box — position and treatment

**One per lesson**, always a **top-level orphan `<div>`** with no id and no class, always
`background: var(--ks3-card)` → `ground: "card"`, always `box-shadow: 6px 6px 0 var(--ks3-accent)`,
label `Key fact` in mono `--ks3-accent-text`, statement in display 700/25px/1.32.

| Lesson | Lines | Sits between |
|---|---|---|
| b2-01 | **171–174** | `#s-switch` → `#s-sort` |
| b2-02 | **184–187** | `#s-bench` → `#s-cases` |
| b2-03 | **182–185** | `#s-bench` → `#s-pairs` |
| b2-04 | **329–332** | `#s-build` → `#s-meters` |

In b2-01/02/03 it lands **immediately after the flagship instrument**; in b2-04 it lands after the
student's own calculation, not after the rig. That is the QUANTITATIVE pattern: state the law once
the student has used it.

The four-way `card` ground is a *unit-wide* choice and differs from the shipped
`.ks3-keyfact` default (`band`) — authorable via `ground`. The 6px shadow, 25px body and
`22px 26px` padding are **not** authorable and are the same CSS finding on all four pages.

## C4 · The FIFA badge treatment

Only b2-04 carries a formula, so only b2-04 carries FIFA — but it carries it **twice**, and the two
are drawn differently:

| | Lines | Badge | Ground |
|---|---|---|---|
| worked example (`WORKED`) | markup **245–254**, data **528–533** | 38px rounded square, `--ks3-accent-text` fill, `--ks3-ground` letter, display 800/20px | inset card, 2px `--ks3-option-border` |
| student's own steps (`buildSteps`) | markup **314–323**, data **928–936** | 34px rounded square, `--ks3-alert` fill, `--ks3-ink` letter, display 800/18px | ink-dark panel, rows separated by `--ks3-dark-rule` |

Letters and labels are identical in both: **F Formula · I Insert · F Fine-tune · A Answer**.
Anyone building the badge must build both variants — light-on-inset and alert-on-ink. This is the
pattern NOTES says matches `b1-02`, and it is also the pattern the P3 unit will reuse, so it is
worth building once as a modifier rather than twice.

## C5 · `cover-triangle` appears **once** in B2, not more

⚠ **NOTES vs PAGE, and it matters for scheduling.** The change-log calls `cover-triangle` a
*"shared shape across all three lessons that use it, and the one to build once."* Those three
lessons are **not** three B2 lessons — B2 has exactly one formula and one triangle, in **b2-04**
(markup 197–234, data 535–539). b2-01, b2-02 and b2-03 contain no triangle, no `COVERS` constant
and no formula block; verified by reading all four script blocks. The other two instances live in
the P3 delivery (`p3-01` and one other), which is a different unit's inventory.

## C6 · The commit-gate idiom — three of four pages

b2-02 (`#s-bench`, 125–139), b2-03 (`#s-bench`, 118–132) and b2-04 (`#s-bench`, 123–137) all gate
the flagship instrument behind a four-option commitment that **disappears** when answered
(`gateOpen: s.gate === null` / `benchOpen: s.gate !== null`). b2-01 gates differently: the
prediction is **per part**, inside the instrument, and it stays visible but disabled after the
switch-off. Both are "gating by absence or by disable", the idiom B1's inventory named; they are
not the same component and must not be merged.

## C7 · The per-item sorter appears on three pages and is the unit's highest-reuse new component

| Lesson | Section | Lines | Items | Options per item | Closing band |
|---|---|---|---|---|---|
| b2-01 | `#s-sort` | 176–201 | 6 (`SORT`, 442–455) | 4 shared `JOBS` | no |
| b2-02 | `#s-cases` | 189–220 | 4 (`CASES`, 414–427) | 5, per item | **yes** (215–219) |
| b2-03 | `#s-pairs` | 187–212 | 4 (`MOVES`, 367–380) | 4, per item | no |

(b2-01 *does* have an all-done band at 164–168, but it belongs to `#s-switch`, not to the sorter.)

All three share: an inset-ground `.ks3-block`, a right-aligned mono progress counter
(`N of M decided`), a max-54ch lede, a column of cards at gap 14px, a per-card option row, and a
**per-card immediate reveal** on `<strong>answer</strong> why`. Cards go from
`--ks3-option-border` to `--ks3-ink` when decided, and unchosen options dim to `opacity: .5` on
all three — but by two different routes: b2-02 and b2-03 append it inline (810, 738), b2-01 gets it
from `seg()`'s own disabled branch (535, called at 642). Same pixels, different style strings; a
byte-comparison of the three will not match.

**One component, three payload widths.** Recommended shape:
```
job-sort = { lede, counter, categories?[]{id,label},          # shared set (b2-01) OR
             items[]{ id, text, options[]?, answer, why },    # per-item set (b2-02/03)
             close_all? }
```
Building this once covers 14 of the unit's authored items and is the single biggest win in B2.

## C8 · What the unit needs from the generator, ranked

| # | Thing | Lessons | Existing? |
|---|---|---|---|
| 1 | `job-sort` — per-item sorter with immediate reveal | b2-01, b2-02, b2-03 | **NEW** (`sort-task`/`sort-rows` both gate the whole set) |
| 2 | `system-switch` — DOM-only, levelled consequence chain | b2-01 | **NEW** (nearest is `sabotage`, cast-coupled to a bench + canvas) |
| 3 | `joint-bench` — parametric two-bone canvas | b2-02 | **NEW** |
| 4 | `muscle-pair` — animated antagonist canvas | b2-03 | **NEW** |
| 5 | `arm-lever` — static scaled-lever canvas | b2-04 | **NEW** |
| 6 | `lever-steps` — pick-a-line ×2 + number + unit, then a rig-computed FIFA reveal | b2-04 | **NEW** |
| 7 | `meter-compare` — rank, then three structured readings cards | b2-04 | **NEW** |
| 8 | FIFA step **badge** drawing, two grounds | b2-04 | drawing NEW, `data-stepper` mechanics exist |
| 9 | triangle `result` slot + three-part `close` + button order/default | b2-04 | component exists, **payload widens** |
| 10 | `misconception` reveal as two paragraphs | all four | one-paragraph today |
| 11 | endmatter card 2 as `Next in this unit` (b2-01/02/03) and as **prose** `Taught in full in` (b2-04) | all four | headings fixed, prose card impossible |
| 12 | `b2-slider` range chrome in `shared/ks3.css` | b2-02, b2-04 | page-local today |
| 13 | KEY FACT 6px shadow / 25px body / 22px 26px padding | all four | 5px / 22px / 18px 22px today |
| 14 | `#s-think` as a **rail stop** with a completion contract | all four | ruled the other way under MRB-208 — **needs a ruling** |
| 15 | a convention-note slot distinct from `safety_note` | b2-04 | none |

## C9 · Open questions this document does not resolve

- **NOTES flag 1** (b2-04 ownership vs Physics P4) is Mide's ruling and blocks the freeze. Nothing
  in the code depends on it — NOTES §6 confirms and the page confirms: no shared component, no
  import, the word *moment* absent.
- **The `#s-think` rail stop** (§1.4 ⚠) contradicts a standing generator ruling on all four pages.
- **NOTES §5's `BODY` misconception family** must be ruled before any `BODY-01`…`BODY-11` id is
  written into a lesson record — NOTES §5 asks for this explicitly and ids are permanent. The
  `elicited_by` / `confronted_by` names in that table (`hook-two-breaks`, `switch-off-chains`,
  `bench-gate-knee-shoulder`, `ladder-r2`, …) are **conceptual, not DOM ids** — none of them
  appears in any of the four files. Authors must map them onto real activity ids.
- **b2-03's reduced-motion gap** (§3.5) — a defect on the approved page. Fixing it is an addition
  inside a drawn component; state it in the build report.
- **NOTES flags 2–17** are science/content and are Mide's alone.
