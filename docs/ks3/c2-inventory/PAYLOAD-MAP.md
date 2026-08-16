# C2 · Atoms, elements and compounds — payload map

Read of the six frozen Design pages in `docs/ks3/design-reference/c2/`, taken from the
files themselves (not from `NOTES-C2.md`, which is cited only where it agrees or
disagrees). Method: `docs/ks3/b1-inventory/README.md`. Exemplar shape:
`docs/ks3/b1-inventory/b1-06-unicellular-organisms.md`.

**This is a specification, not a build.** No lesson module is authored here, and
nothing in `build_ks3.py`, `shared/ks3.css`, `shared/ks3.js`, `ks3_parity.py` or
`verify_ks3.py` is touched.

| File | Lines | Family | Rail stops | Canvases | SVGs |
|---|---|---|---|---|---|
| `c2-01-the-atom-daltons-model.dc.html` | 774 | MODEL | 5 | 1 | 0 |
| `c2-02-elements.dc.html` | 648 | CLASSIFY | 4 | 0 | 0 |
| `c2-03-compounds.dc.html` | 771 | CONTRAST | 5 | 1 | 0 |
| `c2-04-chemical-symbols.dc.html` | 601 | CLASSIFY | 5 | 0 | 0 |
| `c2-05-formulae.dc.html` | 731 | MODEL | 5 | 1 | 0 |
| `c2-06-conservation-of-mass.dc.html` | 942 | QUANTITATIVE | 5 | 1 | 2 |

Line numbers below are line numbers **in these frozen files** and are all real.

**Standing law this is written under (MRB-205 / MRB-210):** Design's approved page
is the specification; Code may add detail *inside* a component Design has drawn and
may not invent a component, block type or layout Design has not drawn; where the page
and a note disagree, the page wins.

---

## 0. Findings that decide components — read these first

### F1 ⭐ `c2-06` draws NO formula triangle. It draws a balance beam and a part–whole bar.

**This is the answer to the MRB-204-as-amended question.** Measured from the file, not
from the notes.

`c2-06` has exactly **two `<svg>` elements** in the lesson body (plus the nav chevron
and the inline `ks3-mark` tick/cross/arrow glyphs, which every page has). Both live
inside one classless `<section>` at **lines 183–240** — the section NOTES §8 calls
"the rule gets its own block, alone". Nothing else on the page is drawn.

**SVG 1 — the balance beam, lines 186–198.** `viewBox="0 0 520 210"`, `role="img"`,
`max-width: 470px`. In document order:

| Line | Element | What it draws |
|---|---|---|
| 187 | `<path d="M260 176L216 200H304Z">` fill `--ks3-ink` | the **fulcrum / stand** — a solid ink triangle apex (260,176) → base (216,200)–(304,200) |
| 188 | `<line x1=260 y1=60 x2=260 y2=178>` stroke-width 7 | the vertical post |
| 189 | `<line x1=70 y1=60 x2=450 y2=60>` stroke-width 7 | the **beam**, dead level |
| 190 | `<circle cx=260 cy=60 r=13>` fill `--ks3-accent` | the pivot |
| 191–192 | two `<line>` stroke-width 4 | the two hangers, x=70 and x=450 |
| 193–194 | two `<rect ... rx=12>` fill `--ks3-card` | the two **pans**, 120×44 |
| 195–196 | two `<text>` 27px display 800 | `before` / `after` |
| 197 | `<text x=260 y=30>` 30px display 800 | `always level` |

aria-label (line 186, verbatim): *"A balance beam, level. On the left pan: the total
mass of everything you started with. On the right pan: the total mass of everything you
ended with. The two are equal."*

Under it, line 200: `total mass of everything before = total mass of everything after`
in 26px display 800, centred; line 201, two mono lines: `everything means the gases
too` / `mass is measured in grams (g)`.

**SVG 2 — the part–whole bar with cover plates, lines 207–227.** `viewBox="0 0 470 196"`.
Same section, below a 3px ink divider (line 203) and its own eyebrow `The bar` (204) and
h2 `Cover the one you want` (205).

| Line | Element | Geometry |
|---|---|---|
| 208–209 | rect + text | **`everything before`** — x=10 y=18 **w=450** h=56 |
| 210–211 | rect + text | **`left in the flask`** — x=10 y=108 **w=296** h=56 |
| 212–213 | rect + text | **`the gas`** — x=314 y=108 **w=146** h=56 |
| 214 | dashed `<line>` y=86, `stroke-dasharray: 8 7` | separates whole from parts |
| 215–218 | `<sc-if value="{{ coverWhole }}">` | ink rect over the whole bar **+ the same label repainted in `--ks3-ink-ghost`** |
| 219–222 | `<sc-if value="{{ coverLeft }}">` | ink rect over `left in the flask` + ghost label |
| 223–226 | `<sc-if value="{{ coverGas }}">` | ink rect over `the gas` + ghost label |

296 + 8 (gap) + 146 = 450 — **the parts sum to the whole to the pixel.** That is the
teaching, and a component must preserve it rather than lay the two parts out by flex.

aria-label (line 207, verbatim): *"A bar model. One long bar is everything before the
reaction. Underneath, the same length is split into two: what is left in the flask, and
the gas. Covering one part leaves the way to work it out."*

**Verdict, stated plainly for the ruling:**

- **No formula triangle appears anywhere in C2.** No `.ks3-triangle`, no
  apex/left/right slot set, no dividing line with a product above and two factors below.
  Nothing in `c2-01`–`c2-05` draws one either (grep over all six files: the only `<svg>`
  outside the shared nav/mark set is c2-06's two).
- **The one triangular *shape* on the page is the balance's fulcrum** (line 187). It is
  the stand the beam pivots on. It carries no label, no cover, no button and no
  relationship. Reading it as a formula triangle would be a misreading.
- Design has therefore done exactly what §8 flag 14 and the 15 Aug change-log say: the
  MRB-204 cover interaction, applied to a **bar** because the relationship is a sum.
- **What this decides:** the generator's existing `formula` block renders a triangle and
  only a triangle (`r_formula`, `build_ks3.py` line 3149 → `r_formula_triangle`, line
  1562, over `_triangle_geometry`, line 1523; `TRI_W, TRI_H, TRI_PAD, TRI_DIV_Y = 260,
  216, 8, 130` at line 1520; slots hard-coded `top` / `left` /
  `right`). **A bar variant does not exist and cannot be reached from data.** See §8 and
  §10 for the exact shape it needs.

### F2 ⭐ `c2-04` carries NO coming-soon row. NOTES §7 is stale; §8 is correct.

NOTES §7 (lines 227–229) says `c2-04` links forward to `c2-05-formulae.html` "which does
not exist yet" and that the generator should render a coming-soon row. NOTES §8 (line
328) says both are now built and "the coming-soon rows this unit previously needed are
gone".

**The page agrees with §8.** `c2-04` line 298 is a plain, live link:

```html
<li><a href="c2-05-formulae.html">Formulae<svg class="ks3-mark ks3-mark-arrow" …
```

identical in shape to every other `Next in this unit` row in the unit. There is no
coming-soon markup, no disabled state, no `aria-disabled`, no muted styling, and the
`Next` link at the end of the page is the same single row. **§7's instruction is dead
and must not be implemented.** No contradiction survives on the page itself — the
contradiction is NOTES §7 against both NOTES §8 and the file, and §7 loses twice.

Every cross-lesson link in the unit, verified:

| Page | Before this lesson | Next / Connects to |
|---|---|---|
| c2-01 | `c1-01-particle-model.html` (307) | `c2-02-elements.html` (313) |
| c2-02 | `c2-01-the-atom-daltons-model.html` (289) | `c2-03-compounds.html` (295) |
| c2-03 | `c2-02-elements.html` (334) | `c2-04-chemical-symbols.html` (340) |
| c2-04 | `c2-03-compounds.html` (292) | `c2-05-formulae.html` (298) |
| c2-05 | `c2-04-chemical-symbols.html` (329) | `c2-06-conservation-of-mass.html` (335) |
| c2-06 | `c2-05-formulae.html` (453) | **`Connects to`** → `c1-03-changes-of-state.html` (459) |

`c2-06` is the only page whose second endmatter card is headed **`Connects to`** rather
than `Next in this unit` (line 457) — it is last in the unit, and NOTES §8 calls the
C1 link load-bearing. The endmatter renderer must be able to emit that heading.

### F3 ⭐ Every non-ASCII character in the unit, with the meaning-bearing ones separated

Enumerated by codepoint over all six files. **Meaning-bearing** = removing or
ASCII-folding it changes what the science says.

**Meaning-bearing — must survive the font subset and the byte-identical lift:**

| Char | Code | File(s) · lines | Context |
|---|---|---|---|
| `₂` | U+2082 | **c2-04** 84 (×2) · **c2-05** 35 occurrences, first 82 | c2-04 hook prose `NaCl, H₂O, CO₂`; c2-05 throughout — `H₂O`, `H₂O₂`, `CO₂`, `H₂SO₄`, `2CO₂`, `C₂O₄`, `C₂H₄O₂`, `2H₂O` (title 82, commit 120, mis-quote 218, reveal 234, keynote 312, stretch 321, KNOWN 374/376/380, rungs 387/395/397/399/400/406, think option 657) |
| `₃` | U+2083 | **c2-04** 350 | `{ id: 'f4', formula: 'CaCO₃', label: 'Chalk, limestone and marble', …` — **NOTES flag 13's character.** It is the whole answer to READS item f4 ("Three capitals: Ca, C and O … The small 3 is a count, not an element"), so if it fails to render the item becomes unanswerable |
| `₄` | U+2084 | **c2-05** 321, 387, 395, 397, 400 | `C₂H₄O₂` (stretch), `H₂SO₄` (rung 1), `C₂O₄` (rung 2 ×3) |
| `₆` | U+2086 | **c2-05** 321 (×2) | `C₆H₁₂O₆` — glucose, stretch layer |
| `₁` | U+2081 | **c2-05** 321, 417 (×2) | `C₆H₁₂O₆`'s subscript 1 in `H₁₂`; `Na₁Cl₁` in rung 4 — the rung's *entire* demand is that a 1 is never written, so the character is the question |
| `−` | U+2212 MINUS | **c2-06** 506, 512, 513, 521, 858 | `4.00 − 2.40` (WORKED Fine-tune), `before − the gas`, `before − left in the flask` (COVERS), `32 − 18` (rung 1 distractor), `152.00 − 149.80` (buildSteps Fine-tune). **A true minus sign, not a hyphen** — folding it to `-` changes typeset arithmetic into a hyphen |
| `°` | U+00B0 | **c2-02** 404 | `Water melts at exactly 0 °C` — a unit |
| `³` | U+00B3 | **c2-06** 302 (×2) | `<option value="cm³">cm³</option>` — the unit picker; the value AND the label |
| `ã` | U+00E3 | **c2-04** 75 | `São Paulo` in the big question — a proper noun, correctly spelled |

**Decorative / typographic — carries no science:**

| Char | Code | Where |
|---|---|---|
| `·` | U+00B7 | all six — `<title>`, eyebrows (`Atoms, elements and compounds · Model`), rung titles (`Rung 1 · Recall`), footer, card labels. 9–13 per file |
| `›` | U+203A | all six, 3× each — breadcrumb separators, `aria-hidden` |
| `—` | U+2014 EM DASH | all six, 17–26 per file — prose punctuation |
| `“` `”` | U+201C / U+201D | all six, 1× each — the `.ks3-mis-quote` on every page. The generator's misconception renderer adds its own quotes, so the authored string must be stored **without** them (b1-02's precedent) |
| `…` | U+2026 | all six, 2× each — the two `placeholder` strings on rungs 3 and 4 |

No arrow or tick characters are used as text anywhere: every tick, cross and arrow is
an inline `<svg class="ks3-mark">` path. That is why NOTES flag 13 says the subscripts
are "the one place a non-ASCII character carries meaning" — and it is right about the
*shape* of the risk, but **understates the count**: there are nine meaning-bearing
codepoints across the unit, not one, and five of them (₂ ₃ ₄ ₆ ₁) are subscripts.

### F4 The `sc-for hint-placeholder-count` on the side rail is wrong on two pages

| Page | `RAIL.length` | `hint-placeholder-count` | Line |
|---|---|---|---|
| c2-01 | 5 | 5 | 56 |
| c2-02 | 4 | 4 | 54 |
| c2-03 | 5 | 5 | 54 |
| **c2-04** | **5** | **4** ✗ | 55 |
| **c2-05** | **5** | **4** ✗ | 54 |
| c2-06 | 5 | 5 | 54 |

The hint is a Design-tool editor affordance and has no effect on the hydrated page, so
this is cosmetic — but it is the reason a reader skimming the markup could count four
stops on `c2-04`. **NOTES §7's "five in `c2-04`" is correct; the placeholder is stale.**
NOTES gives no count for `c2-05` or `c2-06`; both are measured here as **five**.

### F5 Two progress readouts disagree with their own completion test

- **c2-05** line 622: `builderProgress: … + ' of 5 real substances found'`, but the rail's
  `s-builder` ticks at `Object.keys(s.seen).length >= 3` (line 572). A student sees
  "3 of 5" and the stage is already done. Five substances are reachable (`KNOWN`,
  lines 373–383); three is the completion bar.
- **c2-06** line 773: `benchProgress: … + ' of 4 runs done'`, but `s-balance` ticks at
  `Object.keys(s.ran).length >= 3` (line 723). Four runs exist (`RUNS`, 492–501).

Both are Design's numbers, both are internally inconsistent, and neither is a science
error. **Finding for Mide, not something to improvise around** — but note that the
honest reading is that the *readout* is the promise and the *gate* is the concession,
so a generator that reads one `done_when` and one `progress_of` from data will have to
carry both numbers.

### F6 `c2-05`'s builder never marks the substance it opens on

`mark()` (c2-05 lines 560–565) is passed as the `setState` callback of `pairTabs`,
`countA` and `countB` only (625, 631, 635). The initial state is `pair:'ho', a:2, b:1`
(434–437) → key `ho:2:1` → **H₂O, which is displayed on open and is never added to
`seen`** unless the student navigates away and back. So the first of the five real
substances is free to look at and impossible to bank. A component built from data
should mark the opening state as seen at mount; that is an addition *inside* a
component Design drew, and it does not contradict the page.

---

## 1. What all six pages share — measured once, cited thereafter

### 1.1 The spine

`<body>` holds `<x-dc>` (the template) and a trailing
`<script type="text/x-dc" data-dc-script data-props="…">`. `.rd[data-mode="ks3"]` is a
`<div>` with 8 inline declarations (c2-01 line 28, and the same line on all six). Five
top-level landmarks in order:

1. `nav.ks3-nav` — brand tile + breadcrumb `<ol aria-label="Breadcrumb">` **inline in
   the nav**, + trailing `a.ks3-nav-link`. Trail is always
   `KS3 › Chemistry › Atoms, elements and compounds › <lesson title>`.
2. `nav[data-rail="top"]` — sticky, `top: 0`, `z-index: 20`. Count label / current label
   / 96px progress bar.
3. `nav[data-rail="side"]` — fixed, `top: 150px`, `left: calc(50% - 632px)`, width 104px,
   `display:none` below 1340px.
4. `main.ks3-main > div.ks3-lesson`
5. `footer.ks3-footer` — `MrBadmusAI · Key Stage 3 Science`

Brand mark is Claude Design's KS3 mark: 34×34 `--ks3-accent` r10 tile holding a 20×20
`#FBF3E6` chevron, then the wordmark. Correct per the project's KS3 brand rule.

### 1.2 The page-local `<style>` block

Identical on all six (c2-01 lines 14–25 is the superset):

```
html, body { margin:0; padding:0; background:#FBF3E6; }
a / a:hover → --ks3-accent-text / --ks3-accent-hover
@keyframes c2-arrive  (translateY(6px) + opacity)
[data-arrive] { animation: c2-arrive .34s ease-out both; }
[data-rail="side"] { display:none; }
@media (min-width:1340px) { side shown, top hidden }
@media (prefers-reduced-motion: reduce) { [data-arrive] { animation:none !important } }
```

Two pages add one rule each:

- **c2-01** lines 23–24: `[data-obsrow] { display:grid; grid-template-columns: minmax(0,1fr) minmax(0,150px); gap:14px; align-items:center; }` and `@media (max-width:620px)` collapsing it to one column.
- **c2-04** line 23: `[data-symgrid] { display:grid; grid-template-columns: repeat(auto-fit, minmax(min(210px,100%),1fr)); gap:14px; }`

**No animation loop anywhere in the unit.** No `requestAnimationFrame`, no `tick()`. The
only motion is the `c2-arrive` entry animation, which `prefers-reduced-motion` kills.
NOTES §7 is correct on this.

### 1.3 The ladder — byte-identical markup on all six

`<section id="s-ladder" class="ks3-ladder">` with head (`h2 Mastery ladder`, sub *"Four
rungs. Two the page marks, two you mark."*), `.ks3-ladder-score` (`{{ scoreLine }}` /
`{{ scoreNote }}`), `.ks3-rungs` holding a `markedRungs` loop then a `selfRungs` loop, and
a `.ks3-retry-wrap` (`Retry my misses` / *"Clears the ticks on rungs 3 and 4 and keeps
what you wrote."*).

Line ranges: c2-01 **218–286** · c2-02 **200–268** · c2-03 **245–313** · c2-04 **203–271**
· c2-05 **240–308** · c2-06 **364–432**.

Scoring is identical on all six: `score` counts the two marked rungs correct plus each
self-rung whose ticks are all set; `scoreLine` is always `'You got ' + score + ' of 4.'`
and `scoreNote` is always `'You marked rungs 3 and 4 yourself.'`. `onRetry` clears
`answers`, `checked` and `ticks` and keeps `text`.

**Existing.** Generator block type `quiz` → `r_ladder`.

### 1.4 The keynote, the layer, the endmatter

- **Keynote** — `<section class="ks3-block ks3-dark ks3-keynote">`, eyebrow `Key note`,
  one `<p>`. **No `id`, not a rail stop, on all six.** Existing: block type `summary`
  (reads `lesson["key_note"]`).
- **Going further layer** — `<section class="ks3-layer">` → `.ks3-layer-head`
  (`Going further` eyebrow + `.ks3-layer-rule`) → `.ks3-layer-body` → exactly one `<p>` on
  all six. Existing: `r_layer`.
- **Endmatter** — `<div class="ks3-endmatter">` with four `<section>`s: *Before this
  lesson* (link list), *Next in this unit* / *Connects to* (link list), *At GCSE this
  becomes* (prose), `.ks3-tutor` (h2 *Ask Mr Badmus AI*, one prompt `<p>`, an
  `a.ks3-tutor-cta` **pointing at an in-page anchor**, label always `Ask about this
  lesson`). Tutor anchors: c2-01 `#s-model` · c2-02 `#s-think` · c2-03 `#s-think` ·
  c2-04 `#s-sort` · c2-05 `#s-think` · c2-06 `#s-balance`.

### 1.5 `p.ks3-legal` — present on two pages, safety not copyright

- **c2-03** line 354: *"Heating iron and sulfur produces a small amount of hydrogen
  sulfide, which smells of rotten eggs and is toxic. This one belongs in a fume cupboard,
  done by a teacher."*
- **c2-06** line 473: *"Burning magnesium is dangerously bright. Never look straight at
  it, and never seal a flask that is being heated."*

Absent on c2-01, c2-02, c2-04, c2-05. Existing: `lesson["safety_note"]` →
`<p class="ks3-legal ks3-safety">` (`build_ks3.py` 3534–3536). Note the generator adds
`ks3-safety`, which Design does not emit — a class-set parity probe will see one extra.

### 1.6 The KEY FACT box — same position, same ground, all six

A **top-level classless `<div>`** immediately after the flagship instrument block:
`margin: 28px 0 0; padding: 22px 26px; border-radius: var(--ks3-r-panel); background:
var(--ks3-card); border: 2px solid var(--ks3-ink); box-shadow: 6px 6px 0
var(--ks3-accent);` with a mono `Key fact` label in `--ks3-accent-text` and a 25px
display-700 statement.

Lines: c2-01 **163–166** · c2-02 **168–171** · c2-03 **186–189** · c2-04 **143–146** ·
c2-05 **174–177** · c2-06 **332–335**.

**Existing**, and this is the good news: `r_key_fact` emits exactly this
(`.ks3-keyfact[data-ground="card"]`, `shared/ks3.css` 2430–2455). The authored records
need `ground: "card"` — the renderer's default is `band`. **Six for six on `card` is a
new majority against B1's 5:1 band split; worth recording as the C2 half of drift 5.**

Statements, verbatim:

| Page | Line | Text |
|---|---|---|
| c2-01 | 165 | An atom is the smallest particle of an element. There are about a hundred kinds, and no chemical reaction turns one kind into another. |
| c2-02 | 170 | An element is made of one kind of atom, and cannot be broken down into anything simpler by chemistry. Nothing about how it looks will tell you. |
| c2-03 | 188 | A mixture can be any proportion and can be separated again. A compound is one fixed proportion, joined in a reaction, and behaves like neither element that made it. |
| c2-04 | 145 | One capital letter starts one element. CO is carbon and oxygen; Co is cobalt. The case of the second letter is not a style choice. |
| c2-05 | 176 | A formula says which elements are present and how many atoms of each. Change one of those numbers and you have not changed the amount — you have changed the substance. |
| c2-06 | 334 | Atoms are rearranged in a reaction, never created or destroyed. If the mass appears to change, a gas has come in from the air or escaped into it. |

### 1.7 The explainer

One `<section class="ks3-explainer">` on every page, immediately after the hook, holding
exactly one `<p>`: c2-01 **106–108** · c2-02 **104–106** · c2-03 **104–106** ·
c2-04 **105–107** · c2-05 **104–106** · c2-06 **104–106**.

**Existing** (`r_explainer`), with one drift: the generator emits
`<section class="ks3-block ks3-explainer">` and Design emits `<section
class="ks3-explainer">`. `.ks3-explainer` resets `background`, `border`, `padding` and
`box-shadow`, so the rendering is identical — but the class set differs by one, which a
class-audit parity assertion will catch. Same drift B1 recorded; not new.

### 1.8 The hook

`<section id="s-hook" class="ks3-block ks3-dark ks3-hook">` on all six: eyebrow `Start
here`, `<h2>`, `.ks3-hook-prompt`, then `.ks3-hook-commit` holding `.ks3-commit`, a
`ul.ks3-options` loop of four lettered `.ks3-option` buttons, and an
`<sc-if value="{{ hookRevealed }}">`-gated `.ks3-reveal` with `data-arrive="1"`.

**Existing** (`r_hook` reads `phenomenon.commit` / `.options` / `.reveal`). **No page in
C2 carries hook media** — no `figures`, no `tiles`, no art column, and therefore no
Motion toggle, which is correct because nothing in the unit animates.

### 1.9 The misconception block

`<section id="s-think" class="ks3-block ks3-misconception">` on all six:
`.ks3-mis-head` (`!` badge + `Think again` eyebrow), `.ks3-mis-quote` **in curly quotes**,
a `max-width: 54ch` framing paragraph, a `ul.ks3-options` of four lettered options
capped at `max-width: 34rem`, and a `thinkOpen`-gated reveal panel of **two** `<p>`s on
all six (c2-01 212–213 · c2-02 194–195 · c2-03 239–240 · c2-04 197–198 · c2-05 234–235
· c2-06 358–359).

**Existing** (`misconception` block → `r_activity` with the `predict` generic shell), with
one gap: the generator's reveal is a single `data-reveal` div taking one string, and
every C2 reveal is **two paragraphs**. See §10, gap N7.

### 1.10 The rail component

Identical `renderVals().rail` closure on all six, differing only in the `done` test.
It emits per node: `href`, `label` (= `RAIL[i].short`), `num`, `done`, `showNum`,
`hasLine`, and four computed style strings (`linkStyle`, `chipStyle`, `textStyle`,
`lineStyle`). `railCountLabel` = `(active+1) + ' / ' + RAIL.length`; `railCurrentLabel`
= `RAIL[active].label`; `railBarStyle` width = `((active+1)/RAIL.length)*100 + '%'`.

`active` is driven by one `IntersectionObserver` with
`rootMargin: '-45% 0px -50% 0px'`, observing every `RAIL[i].id`. Every rail id resolves
to a real section on all six pages (checked: c2-01 s-hook/s-model/s-scale/s-think/
s-ladder; c2-02 s-hook/s-bench/s-think/s-ladder; c2-03 s-hook/s-bench/s-sort/s-think/
s-ladder; c2-04 s-hook/s-sort/s-read/s-think/s-ladder; c2-05 s-hook/s-builder/s-limit/
s-think/s-ladder; c2-06 s-hook/s-balance/s-build/s-think/s-ladder).

**Two rail nodes per page carry both a `label` and a `short` and neither is derivable
from the block title** — both must be authored, as §4.8.1 A already requires.

### 1.11 Props declared in `data-props`

| Page | Prop | Editor | Range / default | Section label |
|---|---|---|---|---|
| all six | `showDraft` | boolean | default `true` | Lesson state |
| c2-01 | `startZoom` | int | 0–4, default 0 | How small |
| c2-02 | **`testBudget`** | int | **4–24, default 8** | The test bench |
| c2-03 | `startHeated` | boolean | default `false` | The bench |
| c2-04 | — | — | — | — |
| c2-05 | — | — | — | — |
| c2-06 | `startSealed` | boolean | default `false` | The balance bench |

`showDraft` gated the `.ks3-review-flag` under-review marker in the lesson head on all
six. ⊕ **MRB-221, 16 Aug 2026 — that marker is revoked and the build no longer emits it,
so `showDraft` is a Design preview switch with no student-facing meaning. Do not wire it.**
(This is a record of what Design drew, kept as measured; the literal marker wording is not
reproduced, because MRB-221 requires the string to return zero hits across the docs.) `testBudget` is NOTES §7's teaching dial and **is the
pedagogy of c2-02** — a generator that drops it turns the lesson into a click-through.

---

## 2. `c2-01` · The atom: Dalton's model · MODEL

### 2.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `the-atom-daltons-model` | ✅ matches `ks3_data/structure.py` line 167 exactly |
| title | `The atom: Dalton's model` | ✅ matches structure.py line 167; page `<h1>` line 75 |
| discipline / unit | `chemistry` / `atoms-elements-and-compounds` | structure.py 165 |
| family | `MODEL` | ✅ structure.py 167; page eyebrow line 74 `… · Model` |
| eyebrow | `Atoms, elements and compounds · Model` | line 74 |
| big question | *People tried to turn lead into gold for fifteen hundred years and never once managed it. What would have to be true for that to be impossible?* | line 76 |
| `<title>` | `The atom: Dalton's model · MrBadmusAI KS3` | line 12 |
| statutory | `KS3.C.AEC.01` | NOTES §1 |

### 2.2 Payload — line ranges for a byte-identical lift

**Never retype these.** Script block: **335–772**.

| Payload | Lines | Holds |
|---|---|---|
| `data-props` (JSON in the attribute) | **335** | `showDraft` bool default true; `startZoom` int 0–4 default 0 |
| **`RAIL`** | **336–342** | 5 × `{id, label, short}` |
| **`CLAIMS`** | **344–348** | 3 × `{id, text}` — Dalton's three claims, full sentences |
| **`OBS`** | **350–363** | 4 × `{id, text, needs:[claimId], fail}` — the four pre-Dalton observations and, for each, the sentence that replaces it when a claim it needs is off |
| **`ZOOM`** | **365–376** | 5 × `{scale, label, note}` — the magnification ladder from 1 cm to 0.0000001 mm |
| **`RUNGS`** | **378–395** | r1, r2 — 4 options each, `correct` on one and `correction` on the other three |
| **`SELF_RUNGS`** | **397–420** | r3, r4 — `{id, title, question, fieldLabel, placeholder, criteria[5]}` |
| `class Component` | 422–770 | |
| ↳ `state` | 423–436 | `hookChoice, gate, off{}, touched, zoom, seenZoom{0:true}, thinkChoice, answers, text, checked, ticks, active` |
| ↳ `componentDidMount` | 438–451 | IntersectionObserver + `this.draw()` |
| ↳ `componentDidUpdate` / `componentWillUnmount` | 453–454 | redraw / disconnect |
| ↳ **`draw()`** | **456–567** | the 900×310 design space, `setTransform(2,…)`, `#100D0A` ground, a clipped viewport `rect(60,34,W-120,H-88)`, **five per-zoom drawings** (z0 wire 475–481 · z1 grains 482–493 · z2 scratches 494–512 · z3 "past the reach of any light microscope" 513–525 · z4 atom lattice 526–545), the bezel 548–550, the two corner captions 552–559, and the **zoom ladder bar strip** 561–566 |
| ↳ `seg(on, dark, dis)` | 569–578 | the shared control-button style string, dark and light branches |
| ↳ `renderVals` | 580–769 | |
| ↳ **`modelNote`** three branches | **594–602** | all-on / nothing-broken / n-broken prose |
| ↳ **`hookOptions`** | **635–639** | 4 lettered option strings |
| ↳ `modelProgress` | 647 | `'All three claims on'` / `n + ' switched off'` |
| ↳ `claims` view (style strings) | 655–669 | `ON`/`OFF` chip, row style, toggle |
| ↳ `observations` view | 670–680 | swaps `o.text` → `o.fail`, verdict `explained` / `no longer explained` |
| ↳ zoom view (`zoomProgress`, `zoomScale`, `zoomNote`, **`zoomAlt`**) | 683–696 | `zoomAlt` at **687** is a composed aria-label |
| ↳ **`thinkOptions`** | **698–702** | 4 lettered option strings |
| ↳ ladder views | 710–762 | `markedRungs`, `selfRungs`, `scoreLine`, `scoreNote` |
| ↳ `onRetry` | 763–767 | |

Static prose: header **73–80** · hook **82–104** (reveal at **100** is static; the four
hook options are data at 635–639) · `#s-model` head + lede **111–118**, gate prompt
**122**, the two mono section labels **138** and **148** · KEY FACT **163–166** ·
`#s-scale` head + lede **168–176**, button labels `Back out` / `Ten times closer`
**182–183** · `#s-think` **191–197** with the mis-quote at **196** and the two-paragraph
reveal at **212–213** · ladder head **219–228** and retry note **284** · keynote
**288–291** · layer **293–301** · endmatter **303–325**.

### 2.3 Block sequence

11 direct children of `.ks3-lesson`.

| # | Line | Element / id | Classes | Generator block type | Status |
|---|---|---|---|---|---|
| 1 | 73 | `header` | `ks3-lesson-head` | — (page furniture) | EXISTING |
| 2 | 82 | `section#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` | **EXISTING** — `r_hook` |
| 3 | 106 | `section` | `ks3-explainer` | `explainer` | **EXISTING** — `r_explainer` (1 extra class, §1.7) |
| 4 | 110 | `section#s-model` | `ks3-block` (light) | `check` shell + activity kind **`claim-switch`** | **NEW kind** |
| 5 | 163 | `div` | none, fully inline | `key-fact`, `ground: "card"` | **EXISTING** — `r_key_fact` |
| 6 | 168 | `section#s-scale` | `ks3-block ks3-dark ks3-practical` | `practical` shell + activity kind **`scale-zoom`** (canvas) | **NEW kind** |
| 7 | 191 | `section#s-think` | `ks3-block ks3-misconception` | `misconception` | **EXISTING** (2-paragraph reveal gap, §10 N7) |
| 8 | 218 | `section#s-ladder` | `ks3-ladder` | `quiz` | **EXISTING** — `r_ladder` |
| 9 | 288 | `section` | `ks3-block ks3-dark ks3-keynote` | `summary` | **EXISTING** |
| 10 | 293 | `section` | `ks3-layer` | stretch layer | **EXISTING** — `r_layer` |
| 11 | 303 | `div` | `ks3-endmatter` | endmatter | **EXISTING** |

⚠️ **`#s-model` is a light `.ks3-block`, not a practical.** Same trap `ks3_data/b1/__init__.py`
records for `system-bench` and `zoom-ladder` — mapping it to `practical` paints the whole
instrument on ink and resolves its text tokens wrong. Map to **`check`**.
⚠️ **`#s-scale` IS dark practical.** Map to `practical`.

### 2.4 Rail — 5 stages

| # | anchor | short | long label | `done_when` (source line 606–614) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | Lead into gold | `hookChoice !== null` → `committed` |
| 2 | `s-model` | `MODEL` | Switch a claim off | **`touched >= 2`** — two claim toggles, in any direction. NOT "all three off" |
| 3 | `s-scale` | `SCALE` | How small | `Object.keys(seenZoom).length >= 5` — every zoom level visited |
| 4 | `s-think` | `THINK` | One copper atom | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | Mastery ladder | `r1 && r2 answered && checked.r3 && checked.r4` |

Note stage 2: `touched` increments on **every** claim button press including switching
one back on, so two presses of the same claim tick the stage. That is Design's rule as
written; a component must not tighten it silently.

Note stage 3: `seenZoom` seeds `{0: true}` at mount (line 429) and only `onZoomIn` adds
to it (line 694) — `onZoomOut` does not. So the stage requires reaching level 4 by
stepping in, which is exactly right, and `startZoom` > 0 would make it unreachable
without first backing out and climbing again. Flag, do not fix.

### 2.5 Instruments

#### `claim-switch` — `#s-model`, DOM only, NEW

**Controls**
- A **commit gate** (lines 120–134), `<sc-if value="{{ gateOpen }}">` where
  `gateOpen: s.gate === null` (648). Panel: `--ks3-inset`, 2px ink, `--ks3-r-panel`,
  prompt in `.ks3-commit` coloured `--ks3-accent-text` (122): *"Commit first. Which claim
  do you think the other two could not manage without?"*. Options are **the three claim
  texts themselves**, lettered A–C (`gateOptions`, 649–653). The instrument body is
  `<sc-if value="{{ modelOpen }}">` = `s.gate !== null` (654). **Once opened, the gate
  panel disappears** — it is gated by absence, not by disabling.
- **Three claim toggle buttons** (140–145). Each is a full-width `<button>` with
  `aria-pressed="{{ c.on }}"`, an `ON`/`OFF` chip (`flex: 0 0 52px`, mono 13px) and the
  claim text left-aligned. `on` = `!s.off[c.id]`. On: `--ks3-card` ground, 2px
  `--ks3-ink`, `--ks3-ink` text, ink chip with `--ks3-on-dark` label. Off:
  `--ks3-row-dim` ground, 2px `--ks3-rule`, `--ks3-ink-faint` text, `--ks3-band` chip
  with `--ks3-ink-muted` label. `--ks3-r-option`, `min-height: var(--ks3-tap)`.

**Readouts**
- `modelProgress` (line 116), mono 15px `--ks3-ink-muted`, top-right of the head row.
- **Four observation rows** (150–155), `[data-obsrow]` grid `minmax(0,1fr)
  minmax(0,150px)`, collapsing to one column under 620px. Each row: the observation
  text at 18px on the left, a right-aligned mono uppercase verdict on the right.
  - alive: `o.text`, verdict `explained`, `--ks3-card` ground, 2px `--ks3-option-border`,
    verdict `--ks3-ink-muted`
  - dead (`o.needs.some(n => s.off[n])`): **`o.fail` replaces the text**, verdict
    `no longer explained`, `--ks3-band` ground, 2px `--ks3-ink`, verdict
    `--ks3-accent-text`
- `modelNote` panel (158), `--ks3-band`, 2px ink, `--ks3-r-panel`, 19px. Three branches
  (594–602).

**Payload shape as actually authored** — NOTES §3.1 predicted
`{claims, observations, off}`. The file adds a gate:

```
{
  gate:   { prompt: str, options_from: "claims" },   # the 3 claim texts, lettered
  claims: [ { id, text } ],                          # 3, lines 344–348
  observations: [ { id, text, needs: [claimId], fail } ],  # 4, lines 350–363
  progress: { none: "All three claims on", some: "{n} switched off" },
  note:   { all_on: str, none_broken: str, some_broken: "…{off}…{broken}…" },
  verdicts: { alive: "explained", dead: "no longer explained" },
  # runtime: off:{}, touched:int
}
```

DOM/CSS: no `ks3-*` class on any part of it except `.ks3-eyebrow`, `.ks3-commit` and
`.ks3-options`/`.ks3-option` for the gate. Everything else is inline-styled. Canvas: none.

#### `scale-zoom` — `#s-scale`, ONE CANVAS, NEW (and NOT the existing `zoom-ladder`)

**Controls** — two buttons only (182–183): `Back out` (`disabled` when `z === 0`) and
`Ten times closer` (`disabled` when `z === 4`). Both take `seg(false, true, dis)` — the
**dark** branch, so they are outline buttons on ink with `--ks3-on-dark-muted` borders.

**Readouts**
- `zoomProgress` (174), mono 15px `--ks3-on-dark-muted`: `'(z+1) of 5 steps'`.
- `zoomScale` (184), mono 17px **`--ks3-alert`**, inside the control strip.
- `zoomNote` (188), 19px `--ks3-on-dark-body`, below the frame.
- `zoomAlt` (687) — composed aria-label: `'A magnified view of copper at ' + scale + ': '
  + label.toLowerCase() + '.'`

**The canvas** — `width="1800" height="620"`, drawn in a **900 × 310 design space** with
`setTransform(2,0,0,2,0,0)`. Ground `#100D0A`. Content clipped to `rect(60, 34, 780, 222)`.
Five drawings, one per `ZOOM` index — a wire bar, a grain field, a scratch field, a
"past the reach of any light microscope" caption card, and a hexagonally-offset atom
lattice (`step = 62`, `r = 25`, plus a highlight arc). Palette is **hard-coded hex, not
tokens**: `#B7692F`, `#D98A4A`, `#8A4A1E`, `#A85F2A`, `#7A4520`, `#5A3212`, `#5C5249`,
`#FFC53D`, `#C6B9A7`, `#3E3730`. Two mono corner captions at y=24 (label upper-cased
left, scale right), and a 5-segment progress strip at `y = H-42` filled `#FFC53D` up to
and including `z`.

**Payload:** `{ levels: [ {scale, label, note} ] × 5, start: int, drawings: [5 keys] }`.

**Why this is not `zoom-ladder`.** The generator has a `zoom-ladder` activity kind
(`r_zoom_ladder`, `build_ks3.py` line 1877, with `ZOOM_DRAWINGS` at 1874;
`ks3-zoom-block`, `data-zoomblock`). It is
B1's plant→cell ladder: a **slider and a tick row**, an authored `next_box` orange dashed
rectangle per level, and a validated `ZOOM_DRAWINGS = {"plant", "plant-shoot",
"one-leaf", "leaf-section", "one-cell"}` set that would **raise** on any C2 drawing name.
c2-01's instrument has two step buttons and no ticks, no next-box, and five drawings that
do not exist. It is a **different instrument that happens to share the word zoom**.

---

## 3. `c2-02` · Elements · CLASSIFY

### 3.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `elements` | ✅ matches structure.py line 168 |
| title | `Elements` | ✅ structure.py 168; `<h1>` line 73 |
| family | `CLASSIFY` | ✅ structure.py 168; eyebrow line 72 |
| eyebrow | `Atoms, elements and compounds · Classify` | line 72 |
| big question | *Everything there has ever been is built from about a hundred kinds of atom. So how do you tell whether the thing in front of you is one of them?* | line 74 |
| `<title>` | `Elements · MrBadmusAI KS3` | line 12 |
| statutory | `KS3.C.AEC.02` (element half) | NOTES §1 |

### 3.2 Payload — line ranges

Script block: **317–646**.

| Payload | Lines | Holds |
|---|---|---|
| `data-props` | **317** | `showDraft`; **`testBudget` int 4–24 default 8** |
| **`RAIL`** | **318–323** | **4** × `{id, label, short}` |
| **`TESTS`** | **325–330** | 4 × `{id, label}` — `look` / `conduct` / `table` / `break` |
| **`SAMPLES`** | **332–387** | **6** × `{id, tab, name, look, element, name2, results{4 keys}, why}` — the single biggest payload in the unit |
| ↳ s1 copper | 333–341 | element |
| ↳ s2 water | 342–350 | not an element — compound |
| ↳ s3 sulfur | 351–359 | element |
| ↳ s4 **brass** | 360–368 | not an element — mixture (`ATOM-03`) |
| ↳ s5 air | 369–377 | not an element — mixture |
| ↳ s6 sodium | 378–386 | element (`ATOM-05`) |
| **`RUNGS`** | **389–406** | r1, r2 |
| **`SELF_RUNGS`** | **408–431** | r3, r4 × 5 criteria |
| `class Component` | 433–644 | |
| ↳ `state` | 434–446 | `hookChoice, sampleId:'s1', ran{}, used:0, verdicts{}, thinkChoice, …` |
| ↳ `componentDidMount` / `WillUnmount` | 448–462 | observer only — **no `draw()`, no canvas** |
| ↳ `seg(on, dis)` | 464–468 | light branch only |
| ↳ `renderVals` | 470–643 | |
| ↳ **`hookOptions`** | **515–519** | 4 lettered options |
| ↳ **`budgetLabel`** | **527** | `'{left} of {budget} tests left · {n} of 6 decided'` |
| ↳ `sampleTabs` | 528–533 | tab label gains `' ·'` when decided |
| ↳ `testButtons` | 536–549 | disable rule + spend |
| ↳ `results` | 551–553 | filtered to the tests actually run |
| ↳ **`verdictButtons`** | **554–557** | `It is an element` / `It is not an element` |
| ↳ **`thinkOptions`** | **572–576** | 4 lettered options |
| ↳ ladder views | 584–636 | |

Static prose: header **71–78** · hook **80–102** (reveal **98**) · `#s-bench` head + lede
**109–116** · the sample panel's labels **125–126**, results-row chrome **136–141**,
`Your verdict on this sample` **146** · the all-decided close **163** · KEY FACT
**168–171** · `#s-think` **173–179**, mis-quote **178**, reveal **194–195** · ladder
**200–268** · keynote **270–273** · layer **275–283** · endmatter **285–307**.

### 3.3 Block sequence

10 direct children — **the only page in the unit with no `ks3-practical` and no canvas.**

| # | Line | Element / id | Classes | Block type | Status |
|---|---|---|---|---|---|
| 1 | 71 | `header` | `ks3-lesson-head` | — | EXISTING |
| 2 | 80 | `section#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` | EXISTING |
| 3 | 104 | `section` | `ks3-explainer` | `explainer` | EXISTING |
| 4 | 108 | `section#s-bench` | `ks3-block` (light) | `check` + kind **`test-budget-bench`** | **NEW kind** |
| 5 | 168 | `div` | none | `key-fact` ground `card` | EXISTING |
| 6 | 173 | `section#s-think` | `ks3-block ks3-misconception` | `misconception` | EXISTING |
| 7 | 200 | `section#s-ladder` | `ks3-ladder` | `quiz` | EXISTING |
| 8 | 270 | `section` | `ks3-block ks3-dark ks3-keynote` | `summary` | EXISTING |
| 9 | 275 | `section` | `ks3-layer` | layer | EXISTING |
| 10 | 285 | `div` | `ks3-endmatter` | endmatter | EXISTING |

### 3.4 Rail — 4 stages (the only four-stop page in C2)

| # | anchor | short | long label | `done_when` (488–494) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | On the list or not | `hookChoice !== null` |
| 2 | `s-bench` | `TESTS` | Six samples | `Object.keys(verdicts).length >= 6` — a verdict on **every** sample |
| 3 | `s-think` | `THINK` | Brass | `thinkChoice !== null` |
| 4 | `s-ladder` | `LADDER` | Mastery ladder | ladder complete |

NOTES §7's "four in `c2-02`" is correct.

### 3.5 Instrument — `test-budget-bench`, DOM only, NEW

**Controls**

1. **Six sample tabs** (119–121), `seg(pressed, false)`, labelled `Sample 1`…`Sample 6`.
   A decided sample's tab label gains a **trailing ` ·`** (line 529) — the only "done"
   affordance, and it is a middot appended to the string, not a mark element.
2. **Four test buttons** (129–131) per sample, labels from `TESTS`.
   `disabled = ran[t.id] || left <= 0 || decided` (539). Pressing spends one from the
   global budget: `used + 1` (546), guarded against double-spend at 543.
   **The budget is global, not per-sample.**
3. **Two verdict buttons** (148–150): `It is an element` / `It is not an element`.
   `disabled = decided` — one shot per sample, locked at 563.

**Readouts**

- `budgetLabel` (114), mono 15px **`--ks3-accent-text`**, top-right of the head row:
  `'{left} of {budget} tests left · {n} of 6 decided'`.
- Sample panel (124–159): `--ks3-inset`, 2px ink, `--ks3-r-panel`, `padding: 22px 24px`.
  Mono uppercase `sampleName` at 14px, then `sampleLook` at 20px.
- **Results list** (134–143), `hasResults` gated, `data-arrive="1"`: one `<li>` per test
  actually run, `--ks3-card` on 2px `--ks3-rule`, `border-radius: 14px` (a bare px, not a
  token), mono uppercase test label + 18px result prose.
- **Verdict panel** (152–157), `verdictOpen` gated: **ink ground, `--ks3-on-dark`
  text**, `--ks3-r-panel`, 24px display-800 `verdictName` (= `sample.name2`, which is the
  reveal of what the sample actually was) + 18px `verdictWhy` in `--ks3-on-dark-body`.
  **This is the only place a sample is named**, and it fires on the student's verdict
  regardless of whether that verdict was right — the instrument never marks.
- **All-decided close** (161–165): `--ks3-band`, 2px ink, one 19px paragraph (163) —
  the lesson's punchline about shine, colour and conducting.

**Payload shape as actually authored** — NOTES §3.2 is accurate and the file adds `tab`
and `name2`:

```
{
  budget: int,                       # prop-driven, default 8, range 4–24
  tests:   [ { id, label } ],        # 4, lines 325–330
  samples: [ { id, tab, name, look, element: bool, name2, results: {testId: str}, why } ],  # 6, 332–387
  verdicts_labels: ["It is an element", "It is not an element"],
  progress: "{left} of {budget} tests left · {n} of 6 decided",
  close: str,                        # line 163
  # runtime: sampleId, ran:{sampleId:{testId:true}}, used:int, verdicts:{sampleId:'yes'|'no'}
}
```

Note `element: bool` is authored on every sample and **read by nothing** in
`renderVals` — the verdict panel keys off `name2`/`why`, not off `element`. It is a
correctness field waiting for a marker. An orphan-key sweep will flag it; keep it.

DOM/CSS: `.ks3-eyebrow`, `.ks3-options`/`.ks3-option` (hook + think only), everything
else inline. No canvas. No `ks3-*` class on the bench at all.

---

## 4. `c2-03` · Compounds · CONTRAST

### 4.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `compounds` | ✅ matches structure.py line 169 |
| title | `Compounds` | ✅ structure.py 169; `<h1>` line 73 |
| family | `CONTRAST` | ✅ structure.py 169; eyebrow line 72 |
| eyebrow | `Atoms, elements and compounds · Contrast` | line 72 |
| big question | *Iron and sulfur in a dish. Same two elements before and after heating — and afterwards the magnet is useless. What changed?* | line 74 |
| `<title>` | `Compounds · MrBadmusAI KS3` | line 12 |
| safety note | line 354 (`p.ks3-legal`) | |

### 4.2 Payload — line ranges

Script block: **364–769**.

| Payload | Lines | Holds |
|---|---|---|
| `data-props` | **364** | `showDraft`; `startHeated` bool default false |
| **`RAIL`** | **365–371** | 5 × `{id, label, short}` |
| **`TESTS`** | **373–394** | **4** × `{id, name, before, after, settles: bool, verdict}` — `look` (375–378, settles **false**) / `magnet` (379–383) / `ratio` (384–388, the 7 g : 4 g pair) / `acid` (389–393) |
| **`SORT`** | **396–405** | 4 × `{id, text, answer, why}` — sea water / carbon dioxide / **steel** (NOTES flag 9) / sugar |
| **`RUNGS`** | **407–424** | r1, r2 (r2 is the 7 g + 8 g leftover question) |
| **`SELF_RUNGS`** | **426–449** | r3, r4 × 5 criteria |
| `class Component` | 451–767 | |
| ↳ `state` | 452–466 | `hookChoice, gate, heated, ratio:1, testId:'look', seenTests:{look:true}, sortPick{}, …` |
| ↳ `componentDidMount` | 468–481 | observer + `draw()` |
| ↳ **`draw()`** | **486–567** | the dish canvas — see §4.5 |
| ↳ `seg(on, dark, dis)` | 569–578 | both branches |
| ↳ `renderVals` | 580–766 | |
| ↳ **`hookOptions`** | **622–626** | 4 lettered options |
| ↳ **`gateOptions`** | **635–639** | 4 lettered options — the proportion gate (`ATOM-06`) |
| ↳ `benchProgress` | 646 | `'{n} of 4 tests run'` |
| ↳ **`stateTabs`** | **647–649** | `Stirred together` / `Heated until it glows` |
| ↳ **`ratioTabs`** | **654** | `['Mostly sulfur','Half and half','Mostly iron']` |
| ↳ **`dishAlt`** | **660–662** | two composed aria-labels (heated / not) |
| ↳ **`dishNote`** | **663–665** | two 18px caption strings |
| ↳ `testTabs` / `testName` / `testBefore` / `testAfter` / `testVerdictWord` / `testVerdict` | 666–674 | `testVerdictWord` = `'Settles it.'` / `'Settles nothing.'` (673) |
| ↳ `sortProgress` / `sortItems` | 676–693 | option labels `['Mixture','Compound']` at **684** |
| ↳ **`thinkOptions`** | **695–699** | 4 lettered options |
| ↳ ladder views | 707–759 | |

Static prose: header **71–78** · hook **80–102** (reveal **98**) · `#s-bench` head + lede
**109–116**, gate prompt **120**, control group labels **138** and **146**, the
before/after card labels **172** and **176** · KEY FACT **186–189** · `#s-sort` head +
lede **192–199** · `#s-think` **218–224**, mis-quote **223**, reveal **239–240** · ladder
**245–313** · keynote **315–318** · layer **320–328** · endmatter **330–352** · legal **354**.

### 4.3 Block sequence

12 direct children.

| # | Line | Element / id | Classes | Block type | Status |
|---|---|---|---|---|---|
| 1 | 71 | `header` | `ks3-lesson-head` | — | EXISTING |
| 2 | 80 | `section#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` | EXISTING |
| 3 | 104 | `section` | `ks3-explainer` | `explainer` | EXISTING |
| 4 | 108 | `section#s-bench` | `ks3-block ks3-dark ks3-practical` | `practical` + kind **`mixture-compound-dish`** | **NEW kind** |
| 5 | 186 | `div` | none | `key-fact` ground `card` | EXISTING |
| 6 | 191 | `section#s-sort` | `ks3-block` **+ inline `background: var(--ks3-inset)`** | `check` + kind **`verdict-cards`** | **NEW kind** (see §4.6) |
| 7 | 218 | `section#s-think` | `ks3-block ks3-misconception` | `misconception` | EXISTING |
| 8 | 245 | `section#s-ladder` | `ks3-ladder` | `quiz` | EXISTING |
| 9 | 315 | `section` | `ks3-block ks3-dark ks3-keynote` | `summary` | EXISTING |
| 10 | 320 | `section` | `ks3-layer` | layer | EXISTING |
| 11 | 330 | `div` | `ks3-endmatter` | endmatter | EXISTING |
| 12 | 354 | `p` | `ks3-legal` | `safety_note` | EXISTING (extra `ks3-safety` class, §1.5) |

⚠️ **`.ks3-block` + inline `--ks3-inset`** is a ground override the generator has no way
to express. `.ks3-block` is `--ks3-card` (`ks3.css` 296). Three sections in the unit do
this (c2-03 #s-sort, c2-04 #s-read, c2-05 #s-limit, c2-06 #s-build — four, in fact). See
§10 gap N8.

### 4.4 Rail — 5 stages

| # | anchor | short | long label | `done_when` (594–601) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | The magnet stops | `hookChoice !== null` |
| 2 | `s-bench` | `BENCH` | Four tests, two states | `Object.keys(seenTests).length >= 4` — all four tests opened. `seenTests` seeds `{look: true}` at mount (458), so three taps finish it |
| 3 | `s-sort` | `SORT` | Four substances | `Object.keys(sortPick).length >= 4` |
| 4 | `s-think` | `THINK` | Still in there | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | Mastery ladder | ladder complete |

NOTES §7's "five in `c2-03`" is correct.

### 4.5 Instrument — `mixture-compound-dish`, ONE CANVAS + DOM, NEW

**Gate** (118–132), `gateOpen: s.gate === null` (634). Prompt at 120: *"Commit first. In
the mixture you can use any amounts you like. What about after heating?"* — four lettered
options (635–639). The whole bench body is `<sc-if value="{{ benchOpen }}">` =
`s.gate !== null` (645). **Gated by absence.**

**Controls** — three groups, all `seg(on, dark=true, dis)`, i.e. the dark branch:

1. **`stateTabs`** (140–142) — `Stirred together` / `Heated until it glows`. Two-way.
2. **`ratioTabs`** (148–150) — `Mostly sulfur` / `Half and half` / `Mostly iron`,
   **`disabled = s.heated`** (655) and the click handler re-checks `if (!this.state.heated)`
   (657). ⭐ **This disable IS the lesson** (NOTES §3.3): a compound's proportion is not
   adjustable. Group label at 146: `How much of each`.
3. **`testTabs`** (163–165) — the four `TESTS` names; each click records into `seenTests`.

**The canvas** — `width="1700" height="560"`, drawn in an **850 × 280 design space** at
`setTransform(2,…)`. Ground `#100D0A`. Everything is clipped to an **ellipse**
`ellipse(W/2, H/2+10, 330, 96)` — the dish — which is then re-stroked at `lineWidth: 4`
in `#5C5249` (548–552). Palette: `iron = '#9AA0A6'`, `sulfur = '#E9C445'`, dish interior
`#1A1713` cold / `#2A2622` heated. **Hard-coded hex, not tokens.**

- **Not heated** (506–524): 120 particles at pseudo-random positions from a hand-rolled
  LCG (`n = (n*1103515245 + 12345) % 2147483648`, three draws per particle), coloured
  iron if `k < frac` where `frac = [0.3, 0.5, 0.7][s.ratio]`. Iron r=9, sulfur r=7, both
  stroked `rgba(0,0,0,0.45)`. **The ratio control changes the mix in the drawing** — that
  is the point of it existing.
- **Heated** (525–545): a strict **5 × 17 lattice** at `x = W/2 - 290 + col*36,
  y = H/2 - 58 + row*34`. Each cell is one iron circle (r=9) plus one sulfur circle
  (r=7) offset `+17` in x, joined by a 3px `#6E655D` stub from `x+8` to `x+11`.
  **One-to-one, regular, repeating** — NOTES flag 8's diagram, and the flag is right that
  it is the visual most in need of an examiner's eye.
- Corner captions (554–565): mono 15px. Top-left `#FFC53D`: `BEFORE HEATING · A MIXTURE`
  / `AFTER HEATING · IRON SULFIDE`. Top-right `#C6B9A7`: `two kinds of particle, side by
  side` / `every iron atom joined to one sulfur atom`. Bottom-left, a two-swatch legend
  drawn as text: `iron` at x=24 in the iron colour and `sulfur` at x=80 in the sulfur
  colour.

**Readouts**
- `benchProgress` (114) mono 15px `--ks3-on-dark-muted`.
- `dishNote` (158) — 18px 700 `--ks3-on-dark`, in a `--ks3-dark-panel` strip under the
  canvas.
- **The test result card** (168–181) — this is the CONTRAST spine. `--ks3-ground` on ink,
  `--ks3-r-panel`. Mono `testName`, then a **two-up auto-fit grid**
  `repeat(auto-fit, minmax(min(240px,100%),1fr))`: `Before heating` on `--ks3-inset` with
  a 2px `--ks3-rule`, `After heating` on `--ks3-card` with a 2px `--ks3-ink` and an
  **`--ks3-accent-text`** caption. Then the verdict line (180): a display-font
  `<strong>` reading `Settles it.` or `Settles nothing.` followed by the prose.

**Payload shape as actually authored** — NOTES §3.3 predicted `{heated, ratio, test,
tests}`. The file adds the gate, the ratio labels, both alt texts and both dish notes:

```
{
  gate:  { prompt: str, options: [4 × str] },
  states: [ {id: false, label: "Stirred together"}, {id: true, label: "Heated until it glows"} ],
  ratios: ["Mostly sulfur", "Half and half", "Mostly iron"],   # index 1 default; disabled when heated
  ratio_fracs: [0.30, 0.50, 0.70],                              # drawing only
  tests: [ { id, name, before, after, settles: bool, verdict } ],  # 4, lines 373–394
  dish_alt:  { mixed: str, heated: str },     # lines 660–662
  dish_note: { mixed: str, heated: str },     # lines 663–665
  captions:  { left: {mixed, heated}, right: {mixed, heated} },   # canvas, 557–560
  verdict_words: { settles: "Settles it.", not: "Settles nothing." },
  progress: "{n} of 4 tests run",
  start_heated: bool
}
```

#### `verdict-cards` — `#s-sort`, DOM only, NEW

A column of four cards (202–214). Each: 20px/22px padding, `--ks3-card`,
`--ks3-r-panel`, border 2px `--ks3-option-border` → **2px `--ks3-ink` once decided**
(682–683). Inside: a 19px 600 statement, then two buttons `Mixture` / `Compound`
(`seg(on, false, open)`), then an `it.open`-gated `data-arrive` paragraph reading a
display-font `<strong>{{ it.answer }}</strong>` + `{{ it.why }}`.

**One shot per card**, locked at 688. Progress readout `sortProgress` at 197,
`'{n} of 4 decided'`.

Payload: `{ items: [ {id, text, answer, why} ] × 4, options: ["Mixture","Compound"],
progress: "{n} of 4 decided" }`.

⚠️ **This is the same shape as `c2-04`'s `#s-read` and structurally near-identical to
`c2-04`'s `#s-sort`.** Build it once — see §10, gap N3.

---

## 5. `c2-04` · Chemical symbols · CLASSIFY

### 5.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `chemical-symbols` | ✅ matches structure.py line 170 |
| title | `Chemical symbols` | ✅ structure.py 170; `<h1>` line 74 |
| family | `CLASSIFY` | ✅ structure.py 170; eyebrow line 73 |
| eyebrow | `Atoms, elements and compounds · Classify` | line 73 |
| big question | *A chemist in Lagos, one in Osaka and one in São Paulo write the same thing for salt. None of them writes "salt".* | line 75 — contains `ã` (F3) and **straight ASCII double quotes** around *salt* |
| `<title>` | `Chemical symbols · MrBadmusAI KS3` | line 12 |

### 5.2 Payload — line ranges

Script block: **320–599**. **The only page in the unit with no props beyond `showDraft`
and no canvas.**

| Payload | Lines | Holds |
|---|---|---|
| `data-props` | **320** | `showDraft` only |
| **`RAIL`** | **321–327** | **5** × `{id, label, short}` |
| **`ORIGINS`** | **329** | `['First letter', 'First two letters', 'From an older name']` — the three sort buckets |
| **`SYMBOLS`** | **331–341** | **9** × `{id, symbol, name, origin: 0|1|2, why}` — H, C, Ca, Cl, Mg, Na, Fe, Pb, Au (NOTES flags 11 and 12 live in `Mg` 336 and `Cl` 335) |
| **`READS`** | **343–352** | **4** × `{id, formula, label, answer, options[4], why}` — `NaCl` (344) / `CO` (346) / `Co` (348) / **`CaCO₃`** (350) |
| **`RUNGS`** | **354–371** | r1 (MgO), r2 (Co-for-CO) |
| **`SELF_RUNGS`** | **373–396** | r3, r4 × 5 criteria |
| `class Component` | 398–597 | |
| ↳ `state` | 399–409 | `hookChoice, symPick{}, readPick{}, thinkChoice, …` |
| ↳ `componentDidMount` / `WillUnmount` | 411–425 | observer only |
| ↳ `seg(on, dis)` | 427–431 | **light branch, and a smaller one**: `font-size: 15px; padding: 9px 13px` (the only page with a shrunk control) |
| ↳ `renderVals` | 433–596 | |
| ↳ **`hookOptions`** | **474–478** | 4 lettered options |
| ↳ `sortProgress` | 486 | `'{n} of 9 placed'` |
| ↳ `symbols` view | 487–503 | per-card style + the three `ORIGINS` buttons |
| ↳ `allSorted` | 504 | `>= 9` |
| ↳ `readProgress` | 506 | `'{n} of 4 read'` |
| ↳ `reads` view | 507–523 | per-card style + the four count buttons |
| ↳ **`thinkOptions`** | **525–529** | 4 lettered options |
| ↳ ladder views | 537–589 | |

Static prose: header **72–79** · hook **81–103** (prompt **84** carries `H₂O`/`CO₂`;
reveal **99**) · `#s-sort` head + lede **110–117** · the all-sorted close **138** ·
KEY FACT **143–146** · `#s-read` head + lede **149–156** · `#s-think` **176–182**,
mis-quote **181**, reveal **197–198** · ladder **203–271** · keynote **273–276** ·
layer **278–286** · endmatter **288–310**.

### 5.3 Block sequence

11 direct children.

| # | Line | Element / id | Classes | Block type | Status |
|---|---|---|---|---|---|
| 1 | 72 | `header` | `ks3-lesson-head` | — | EXISTING |
| 2 | 81 | `section#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` | EXISTING |
| 3 | 105 | `section` | `ks3-explainer` | `explainer` | EXISTING |
| 4 | 109 | `section#s-sort` | `ks3-block` (light) | `check` + kind **`origin-grid`** | **NEW kind** |
| 5 | 143 | `div` | none | `key-fact` ground `card` | EXISTING |
| 6 | 148 | `section#s-read` | `ks3-block` + inline `--ks3-inset` | `check` + kind **`verdict-cards`** (same as c2-03 §4.6) | **NEW kind, shared** |
| 7 | 176 | `section#s-think` | `ks3-block ks3-misconception` | `misconception` | EXISTING |
| 8 | 203 | `section#s-ladder` | `ks3-ladder` | `quiz` | EXISTING |
| 9 | 273 | `section` | `ks3-block ks3-dark ks3-keynote` | `summary` | EXISTING |
| 10 | 278 | `section` | `ks3-layer` | layer | EXISTING |
| 11 | 288 | `div` | `ks3-endmatter` | endmatter | EXISTING |

**No coming-soon row anywhere on the page** — see F2.

### 5.4 Rail — 5 stages

| # | anchor | short | long label | `done_when` (446–453) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | Why symbols | `hookChoice !== null` |
| 2 | `s-sort` | `SORT` | Nine symbols | `Object.keys(symPick).length >= 9` |
| 3 | `s-read` | `READ` | Read four labels | `Object.keys(readPick).length >= 4` |
| 4 | `s-think` | `THINK` | CO and Co | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | Mastery ladder | ladder complete |

NOTES §7's "five in `c2-04`" is correct; the `hint-placeholder-count="4"` at line 55 is
stale (F4).

### 5.5 Instruments

NOTES §3 says *"`c2-04` needs no instrument: it is two commit-and-reveal grids."* That is
true as a description and **false as a build instruction** — neither grid exists in the
generator today.

#### `origin-grid` — `#s-sort`, DOM only, NEW

A **CSS grid**, `[data-symgrid]` (page style line 23):
`repeat(auto-fit, minmax(min(210px,100%),1fr))`, `gap: 14px`.

Per card (121–132): `--ks3-card`, `--ks3-r-panel`, `padding: 18px 20px`, border 2px
`--ks3-option-border` → 2px `--ks3-ink` when open (492–493). Contents:

- the **symbol** at `font-size: 42px`, display 800, `line-height: 1`, `letter-spacing: -.02em`
- the **name** at 19px 600
- three buttons, one per `ORIGINS` bucket, `seg(pressed, open)`
- an `sy.open`-gated `data-arrive` paragraph at **17px** (the smallest reveal in the unit)
  in `--ks3-ink-body`

One shot per card (498). `sortProgress` at 115 reads `'{n} of 9 placed'`. An
`allSorted`-gated close panel at 136–140 on `--ks3-band` with a 2px ink border (138).

Payload: `{ buckets: ["First letter","First two letters","From an older name"],
items: [ {id, symbol, name, origin: int, why} ] × 9, progress: "{n} of 9 placed",
close: str }`.

⚠️ `origin` is authored on every symbol and **read by nothing** — the card reveals `why`
on any pick. Same shape as c2-02's unused `element` flag. Keep it; flag it in the sweep.

#### `verdict-cards` (second instance) — `#s-read`, DOM only, NEW

Structurally the same component as c2-03's `#s-sort` (§4.6) with three differences:

1. the card's headline is a **mono 26px 500 formula** (`{{ r.formula }}`, line 161), not
   a prose statement, with an 18px `--ks3-ink-body` label under it (162);
2. there are **four** options per card (`['One','Two','Three','Four']`, authored per item
   in `READS`), not two;
3. the reveal is 18px, matching c2-03.

Everything else — `--ks3-card`, `--ks3-r-panel`, `padding: 20px 22px`, the
`option-border` → `ink` border swap, the display-font `<strong>{{ answer }}</strong>` +
`{{ why }}` reveal, the one-shot lock, the `'{n} of 4 read'` progress — is identical.

**One component, two instances, with the headline typed (`prose` | `formula`) and the
options authored per item.** See §10, gap N3.

---

## 6. `c2-05` · Formulae · MODEL

### 6.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `formulae` | ✅ matches structure.py line 171 |
| title | `Formulae` | ✅ structure.py 171; `<h1>` line 73 |
| family | `MODEL` | ✅ structure.py 171; eyebrow line 72 |
| eyebrow | `Atoms, elements and compounds · Model` | line 72 |
| big question | *One of these bottles is drinking water. The other bleaches hair and has been used as rocket fuel. The difference is one atom.* | line 74 |
| `<title>` | `Formulae · MrBadmusAI KS3` | line 12 |

### 6.2 Payload — line ranges

Script block: **357–729**.

| Payload | Lines | Holds |
|---|---|---|
| `data-props` | **357** | `showDraft` only |
| **`RAIL`** | **358–364** | 5 × `{id, label, short}` |
| **`PAIRS`** | **366–370** | 3 × `{id, a, b, aName, bName}` — `ho` / `co` / `nacl` |
| comment | 372 | `// Known substances, keyed pair:countA:countB` |
| **`KNOWN`** | **373–383** | **5** entries keyed `pair:a:b` |
| ↳ `ho:2:1` H₂O | 374–375 | `{name, note, atoms[3], bonds[2]}` |
| ↳ `ho:2:2` H₂O₂ | 376–377 | `{name, note, atoms[4], bonds[3]}` |
| ↳ `co:1:1` CO | 378–379 | `{name, note, atoms[2], bonds[1]}` |
| ↳ `co:1:2` CO₂ | 380–381 | `{name, note, atoms[3], bonds[2]}` |
| ↳ `nacl:1:1` NaCl | 382 | `{name, note, giant: true}` — **no `atoms`, no `bonds`** |
| **`RUNGS`** | **385–402** | r1 (H₂SO₄ atom count), r2 (2CO₂ vs C₂O₄) |
| **`SELF_RUNGS`** | **404–427** | r3, r4 (`Na₁Cl₁`, NOTES flag 17) × 5 criteria |
| **`COLOURS`** | **429** | `{H:'#F4E9D8', O:'#8FB7FF', C:'#C6B9A7', Na:'#FFC53D', Cl:'#7FB3A8'}` — atom palette, hex not tokens |
| `class Component` | 431–727 | |
| ↳ `state` | 432–446 | `hookChoice, gate, pair:'ho', a:2, b:1, seen{}, limitChoice, thinkChoice, …` |
| ↳ `componentDidMount` | 448–461 | observer + `draw()` |
| ↳ `key()` | 466 | `pair + ':' + a + ':' + b` |
| ↳ **`draw()`** | **468–540** | 850 × 260 design space; **three branches** — not-found 483–490, giant 492–514, molecule 516–539 |
| ↳ `seg(on)` | 542–546 | dark branch only, **no `dis` parameter** — nothing in this instrument disables |
| ↳ `renderVals` | 548–726 | |
| ↳ `mark()` | 560–565 | records a `KNOWN` key into `seen` — see F6 |
| ↳ **`hookOptions`** | **598–602** | 4 lettered options |
| ↳ **`gateOptions`** | **611–615** | 4 lettered options (`ATOM-09`) |
| ↳ `builderProgress` | **622** | `'{n} of 5 real substances found'` (see F5) |
| ↳ `pairTabs` / `countA` / `countB` | 623–636 | counts are `[1,2,3]` for both |
| ↳ **`molAlt`** | **638–640** | composed aria-label, three-way |
| ↳ **`builtName`** / **`builtNote`** | **641–642** | the not-a-substance name is **composed** at 641 |
| ↳ **`limitOptions`** | **644–647** | **3** lettered options (the only 3-option commit in the unit) |
| ↳ **`thinkOptions`** | **655–659** | 4 lettered options |
| ↳ ladder views | 667–719 | |

Static prose: header **71–78** · hook **80–102** (h2 **82** carries `H₂O`/`H₂O₂`; reveal
**98**) · `#s-builder` head + lede **109–116**, gate prompt **120**, the three control
group labels **138**, **146** (`{{ firstLabel }}`), **154** (`{{ secondLabel }}`) ·
KEY FACT **174–177** · `#s-limit` **179–211** — eyebrow **180**, h2 **181**, lede **182**,
**the two contrast cards 185–192** (molecule card 185–188; giant card 189–192, **ink
ground**), the commit prompt **196**, the `limitOpen` reveal **208** · `#s-think`
**213–219**, mis-quote **218**, reveal **234–235** · ladder **240–308** · keynote
**310–313** · layer **315–323** (glucose/ethanoic acid, NOTES flag 16) · endmatter
**325–347**.

### 6.3 Block sequence

11 direct children.

| # | Line | Element / id | Classes | Block type | Status |
|---|---|---|---|---|---|
| 1 | 71 | `header` | `ks3-lesson-head` | — | EXISTING |
| 2 | 80 | `section#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` | EXISTING |
| 3 | 104 | `section` | `ks3-explainer` | `explainer` | EXISTING |
| 4 | 108 | `section#s-builder` | `ks3-block ks3-dark ks3-practical` | `practical` + kind **`formula-builder`** | **NEW kind** |
| 5 | 174 | `div` | none | `key-fact` ground `card` | EXISTING |
| 6 | 179 | `section#s-limit` | `ks3-block` + inline `--ks3-inset` | `check` + kind **`model-limit`** | **NEW kind** |
| 7 | 213 | `section#s-think` | `ks3-block ks3-misconception` | `misconception` | EXISTING |
| 8 | 240 | `section#s-ladder` | `ks3-ladder` | `quiz` | EXISTING |
| 9 | 310 | `section` | `ks3-block ks3-dark ks3-keynote` | `summary` | EXISTING |
| 10 | 315 | `section` | `ks3-layer` | layer | EXISTING |
| 11 | 325 | `div` | `ks3-endmatter` | endmatter | EXISTING |

**No `formula` block, no triangle, no FIFA, no worked example.** MODEL with no
calculation — the MRB-204 four-part ruling does not engage on this page at all.

### 6.4 Rail — 5 stages

| # | anchor | short | long label | `done_when` (570–577) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | One atom apart | `hookChoice !== null` |
| 2 | `s-builder` | `BUILD` | Build a formula | **`Object.keys(seen).length >= 3`** — three of the five real substances, despite the readout promising five (F5), and the opening H₂O never banks itself (F6) |
| 3 | `s-limit` | `LIMIT` | Where it runs out | `limitChoice !== null` |
| 4 | `s-think` | `THINK` | Big and small numbers | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | Mastery ladder | ladder complete |

NOTES gives no count for c2-05. **Measured: five.**

### 6.5 Instruments

#### `formula-builder` — `#s-builder`, ONE CANVAS + DOM, NEW

**Gate** (118–132), `gateOpen: s.gate === null`. Prompt at 120: *"Commit first. If you
change the 2 in H₂O to a 3, what have you got?"* — four options (611–615). Body gated by
`builderOpen` = `s.gate !== null` (621). Gated by absence.

**Controls** — three groups, all `seg(on)` (dark branch, `--ks3-alert` when pressed):

1. **`pairTabs`** (140–142), group label `Two elements` (138). Labels are composed:
   `p.a + ' and ' + p.b` → `H and O` / `C and O` / `Na and Cl` (624).
2. **`countA`** (148–150), group label is **dynamic**: `{{ firstLabel }}` = `pair.aName`
   (627), e.g. `Hydrogen atoms`. Buttons `1` / `2` / `3`.
3. **`countB`** (156–158), group label `{{ secondLabel }}` = `pair.bName` (628).
   Buttons `1` / `2` / `3`.

Search space is 3 pairs × 3 × 3 = **27 combinations, of which 5 are substances**. That
"most of it is not a substance" is NOTES §8's stated teaching and it is why the not-found
branch must exist.

**The canvas** — `width="1700" height="520"`, **850 × 260** design space at
`setTransform(2,…)`, ground `#100D0A`, `textAlign: 'center'`, `cx = W/2, cy = H/2 + 6`.

- **Not found** (483–490): two centred mono lines in `#6E655D` — `no substance with this
  formula` (17px) and `not every combination of atoms is a substance` (15px). Returns
  early.
- **Giant** (492–514): a **4 × 12 checkerboard**, `step = 58`, origin
  `cx-320, cy-82`. `isNa = (row+col) % 2 === 0`; Na circles r=19 in `COLOURS.Na`, Cl
  circles r=23 in `COLOURS.Cl`, each stroked `#100D0A` 2px and **labelled `Na` / `Cl`
  in 13px Bricolage Grotesque 800**. Footer caption `a repeating stack, going on in every
  direction` in `#C6B9A7` mono 15px at `H-18`.
- **Molecule** (516–539): bonds first — `#5C5249`, `lineWidth: 7`, one line per
  `bonds[[i,j]]` between `atoms[i]` and `atoms[j]` offset from `(cx,cy)`. Then atoms:
  circle at `at.r`, filled `COLOURS[at.s]` (fallback `#C6B9A7`), stroked `#100D0A` 2.5px,
  labelled `at.s` in **16px Bricolage Grotesque 800** at `y + 6`. Footer caption
  `one particle`.

**Readouts**
- `builderProgress` (114), mono 15px `--ks3-on-dark-muted`.
- Under the canvas, on `--ks3-dark-panel`: `builtName` (166) at **30px display 800**, and
  `builtNote` (167) at 18px `--ks3-on-dark-body`.
- The not-a-substance name is composed at 641:
  `pair.a + (a>1 ? a : '') + pair.b + (b>1 ? b : '') + ' — not a substance'`.
  ⚠️ **It composes with ASCII digits, not subscripts** — `H3O2 — not a substance`, not
  `H₃O₂`. Every authored name in `KNOWN` uses proper subscripts. That is Design's page as
  written and the page wins; a generator must reproduce the ASCII composition, and if
  Mide wants subscripts it is a content change, not a build decision.
- `molAlt` (638–640), three-way composed aria-label.

**Payload shape as actually authored** — NOTES §8 predicted
`{pairs, a, b, known:{key:{name,note,atoms,bonds,giant}}}`. Accurate, plus:

```
{
  gate:   { prompt: str, options: [4 × str] },
  pairs:  [ { id, a, b, aName, bName } ],        # 3, lines 366–370
  counts: [1, 2, 3],                              # both axes
  start:  { pair: "ho", a: 2, b: 1 },
  known:  { "pair:a:b": { name, note, atoms: [{s,x,y,r}], bonds: [[i,j]], giant: bool } },  # 5, 373–383
  colours: { H, O, C, Na, Cl },                   # line 429
  not_found: { name_suffix: " — not a substance", note: str,  # line 642
               canvas_lines: [str, str] },        # lines 486, 488
  captions: { molecule: "one particle",           # line 539
              giant: "a repeating stack, going on in every direction" },  # line 512
  progress: "{n} of 5 real substances found",
  done_at: 3
}
```

#### `model-limit` — `#s-limit`, DOM only, NEW

The MODEL family's *where it breaks* step, as a **two-card contrast + a commit + a
reveal** — not a comparison table.

- Head: eyebrow `Where the model runs out` (180), h2 (181), 54ch lede (182).
- **Two cards** in an auto-fit grid `repeat(auto-fit, minmax(min(280px,100%),1fr))`,
  `gap: 16px` (184):
  - **light card** (185–188): `--ks3-card`, 2px ink, `--ks3-r-panel`,
    `padding: 22px 24px`. Mono caption `A molecule · CO₂` in `--ks3-ink-muted`, 18px prose.
  - **ink card** (189–192): `background: var(--ks3-ink); color: var(--ks3-on-dark)`,
    **no border**. Mono caption `A giant structure · NaCl` in **`--ks3-alert`**, 18px
    prose in `--ks3-on-dark-body`.
  The light/dark asymmetry is the argument, not decoration.
- **Commit** (195–206): a 19px 700 prompt *"So what does the formula for salt tell you?"*
  and a `ul.ks3-options` capped at `34rem` with **three** lettered options.
- **Reveal** (207–209): `limitOpen`-gated, `data-arrive`, on `--ks3-band` with a 2px ink
  border, 19px. Ungated by the answer — commitment, never marking.

Payload: `{ eyebrow, title, lede, cards: [ {caption, text, ground: "card"|"ink"} ] × 2,
commit: str, options: [3 × str], reveal: str }`.

---

## 7. `c2-06` · Conservation of mass · QUANTITATIVE

### 7.1 Identity

| Field | Value | Source |
|---|---|---|
| slug | `conservation-of-mass` | ✅ matches structure.py line 172 |
| title | `Conservation of mass` | ✅ structure.py 172; `<h1>` line 73 |
| family | `QUANTITATIVE` | ✅ structure.py 172; eyebrow line 72 `… · Quantitative` |
| eyebrow | `Atoms, elements and compounds · Quantitative` | line 72 |
| big question | *A candle burns down to nothing. A nail rusts and gets heavier. One of those looks like mass being destroyed and one like mass being made. Neither is.* | line 74 |
| `<title>` | `Conservation of mass · MrBadmusAI KS3` | line 12 |
| safety note | line 473 (`p.ks3-legal`) | |

### 7.2 Payload — line ranges

Script block: **483–940**. The largest of the six.

| Payload | Lines | Holds |
|---|---|---|
| `data-props` | **483** | `showDraft`; `startSealed` bool default false |
| **`RAIL`** | **484–490** | 5 × `{id, label, short}` |
| **`RUNS`** | **492–501** | **4** entries keyed `reaction:vessel`, each `{before, after, gas: 'in'|'out'|'none', note}` |
| ↳ `marble:open` | 493–494 | 152.00 → 149.80, gas `out` |
| ↳ `marble:sealed` | 495–496 | 152.00 → 152.00, gas `none` |
| ↳ `magnesium:open` | 497–498 | **2.40 → 4.00**, gas `in` |
| ↳ `magnesium:sealed` | 499–500 | **152.00 → 152.00**, gas `none` ⚠️ see F7 below |
| **`WORKED`** | **503–508** | **4** × `{letter, label, line, note}` — F/I/F/A, `Formula` / `Insert` / **`Fine-tune`** / `Answer`, on the magnesium reaction |
| **`COVERS`** | **510–514** | **3** × `{result, sentence}` keyed `whole` / `left` / `gas` — the bar's cover payload |
| **`RUNGS`** | **516–533** | r1 (18 g + 32 g sealed), r2 (rusting nail) |
| **`SELF_RUNGS`** | **535–558** | r3 (candle), r4 (sealed bag of steel wool) × 5 criteria |
| `class Component` | 560–938 | |
| ↳ `state` | 561–581 | `hookChoice, gate, rxn:'marble', vessel, ran{}, showAfter, workedStep:0, cover:'gas', formPick, insertPick, ansText, ansUnit, buildOpen, thinkChoice, …` |
| ↳ `componentDidMount` | 583–596 | observer + `draw()` |
| ↳ `runKey()` / `run()` | 601–602 | |
| ↳ **`draw()`** | **604–691** | 850 × 280 design space; the balance body 620–630, the flask 632–650, the bung 652–655, the gas plume 657–670, the **digital display** 672–690 |
| ↳ `seg(on, dis)` | 693–697 | dark branch |
| ↳ **`segLight(on, dis)`** | **699–703** | light branch, **`text-align: left`** — the only left-aligned control style in the unit, for the stacked FIFA pick buttons |
| ↳ `renderVals` | 705–937 | |
| ↳ `gasMass` | 710 | `152.00 - 149.80` computed, **not authored** |
| ↳ **`hookOptions`** | **749–753** | 4 lettered options |
| ↳ **`gateOptions`** | **762–766** | 4 lettered options |
| ↳ `benchProgress` | **773** | `'{n} of 4 runs done'` (see F5) |
| ↳ **`rxnTabs`** | **774–777** | `Marble chips and acid` / `Burning magnesium` |
| ↳ **`vesselTabs`** | **781–784** | `Open flask` / `Sealed flask` |
| ↳ **`benchAlt`** | **789–790** | composed aria-label |
| ↳ `runLabel` / `runStyle` / `onRun` / `benchStatus` | 792–796 | `Start the reaction` / `Reaction finished`; two status strings at 796 |
| ↳ `beforeLabel` / `afterLabel` / `benchNote` | 797–799 | `afterLabel` is `'—'` until run (798) |
| ↳ **`coverWhole/Left/Gas`, `coverTabs`, `coverResult`, `coverSentence`** | **801–815** | the bar instrument's whole surface |
| ↳ `workedProgress` / `workedSteps` / `workedBtnLabel` / `onWorked` | 817–824 | staged reveal, `slice(0, workedStep)` |
| ↳ **`formPicks`** | **826–829** | 3 candidate rule statements |
| ↳ **`insertPicks`** | **835–838** | 3 candidate insertions |
| ↳ answer field + unit select wiring | 844–850 | `buildBtnLocked` at 849 is the four-way gate |
| ↳ `buildProgress` | 851–852 | `'{n} of 3 lines committed'` / `'Opened'` |
| ↳ **`buildSteps`** | **855–859** | 4 × `{letter, label, line, note}` — the marble version of F/I/F/A |
| ↳ **`buildClose`** | **864** | composed: `'You wrote {x} {unit}. The worked answer is 2.20 g.'` |
| ↳ **`thinkOptions`** | **866–870** | 4 lettered options |
| ↳ ladder views | 878–930 | |

Static prose: header **71–78** · hook **80–102** (reveal **98**) · `#s-balance` head +
lede **109–116**, gate prompt **120**, control group labels **138** and **146**, the three
readout tile labels **165**, **169**, **173**, and ⭐ **the third tile's literal body at
174**: `not measured — you work it out` · **the rule section 183–240** (see §7.5) ·
worked example **242–266**, head **245–246**, the done-note **264** · `#s-build`
**268–330**, eyebrow **269**, h2 **270**, lede **271**, the three step labels **275**,
**284**, **293**, the two visually-hidden `<label>`s **295** and **297**, the unit
`<option>` set **299–304**, button label `Show the four steps` **310**, the reveal head
**316** · KEY FACT **332–335** · `#s-think` **337–343**, mis-quote **342**, reveal
**358–359** · ladder **364–432** · keynote **434–437** · layer **439–447** (phlogiston,
NOTES flag 19) · endmatter **449–471** · legal **473**.

### F7 ⚠️ `magnesium:sealed` reuses the marble masses

`RUNS['magnesium:sealed']` (line 499) is `before: 152.00, after: 152.00` — the
**marble** numbers. `magnesium:open` (497) is `2.40 → 4.00`. So switching from open to
sealed on the magnesium reaction jumps the balance readout from 2.40 g to 152.00 g with
no explanation, and the sealed note (500) talks about magnesium while the display shows
the marble apparatus mass.

It is arguably defensible — a sealed flask weighs the whole apparatus and 152.00 g is a
plausible flask-plus-contents mass — and the note never quotes the number. But it is
**undocumented in NOTES, unmentioned in flag 18** (which covers 2.40/4.00 and
152.00/149.80 and says nothing about the fourth run), and it is the one place in the unit
where two runs share a number for no stated reason. **Finding for Mide.** Do not
"fix" it silently: the masses cross the examiner gate.

### 7.3 Block sequence

13 direct children — the longest stack in the unit.

| # | Line | Element / id | Classes | Block type | Status |
|---|---|---|---|---|---|
| 1 | 71 | `header` | `ks3-lesson-head` | — | EXISTING |
| 2 | 80 | `section#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` | EXISTING |
| 3 | 104 | `section` | `ks3-explainer` | `explainer` | EXISTING |
| 4 | 108 | `section#s-balance` | `ks3-block ks3-dark ks3-practical` | `practical` + kind **`balance-bench`** | **NEW kind** |
| 5 | **183** | `section` | **none — fully inline** (`--ks3-band`, **3px** ink, `--ks3-r-block`, `padding: 32px`) | `formula` **with a NEW `shape: "bar"`** | ⭐ **EXISTING SHELL, NEW DRAWING** |
| 6 | 242 | `section` | `ks3-block ks3-worked` | `worked-example` + kind **`worked-example`** staged | **EXISTING, with gaps** (§7.7) |
| 7 | 268 | `section#s-build` | `ks3-block` + inline `--ks3-inset` | `check` + kind **`fifa-construct`** | **EXISTING kind, wrong field shape** (§7.8) |
| 8 | 332 | `div` | none | `key-fact` ground `card` | EXISTING |
| 9 | 337 | `section#s-think` | `ks3-block ks3-misconception` | `misconception` | EXISTING |
| 10 | 364 | `section#s-ladder` | `ks3-ladder` | `quiz` | EXISTING |
| 11 | 434 | `section` | `ks3-block ks3-dark ks3-keynote` | `summary` | EXISTING |
| 12 | 439 | `section` | `ks3-layer` | layer | EXISTING |
| 13 | 449 | `div` | `ks3-endmatter` | endmatter | EXISTING |
| — | 473 | `p` | `ks3-legal` | `safety_note` | EXISTING |

⚠️ **Blocks 5 and 6 carry no `id` and are not rail stops.** The rule and the worked
example are read, not done — consistent with MRB-208's "the rail carries only sections
that require the student to do something".

### 7.4 Rail — 5 stages

| # | anchor | short | long label | `done_when` (721–728) |
|---|---|---|---|---|
| 1 | `s-hook` | `HOOK` | Where the wax went | `hookChoice !== null` |
| 2 | `s-balance` | `BALANCE` | Open and sealed | **`Object.keys(ran).length >= 3`** — three of the four run keys, though the readout says 4 (F5) |
| 3 | `s-build` | `STEPS` | Your own four steps | `s.buildOpen` — i.e. the student pressed `Show the four steps`, which itself requires all three lines committed (849) |
| 4 | `s-think` | `THINK` | Burning and mass | `thinkChoice !== null` |
| 5 | `s-ladder` | `LADDER` | Mastery ladder | ladder complete |

NOTES gives no count for c2-06. **Measured: five.** Note there is **no rail stop for the
rule/bar section and none for the worked example** — the QUANTITATIVE four-part sequence
occupies three page sections and one rail stage.

### 7.5 ⭐ The rule section, 183–240 — the whole MRB-204 question in one block

One classless `<section>` holding **two drawings and one instrument**, split by a 3px ink
rule at line 203.

**Upper half — part 1 and part 2 of the four-part treatment.**
- eyebrow `The rule` in `--ks3-accent-text`, **centred** (184)
- the **balance-beam SVG** (186–198) — full geometry in F1
- the statement (200), 26px display 800, centred:
  `total mass of everything before = total mass of everything after`
- two mono support lines (201), `line-height: 1.9`, separated by `<br>`:
  `everything means the gases too` / `mass is measured in grams (g)`

**Lower half — the `cover-triangle` shape, drawn as a BAR.**
- eyebrow `The bar`, h2 `Cover the one you want` (204–205)
- a wrapping flex row, `gap: 30px 44px`, `justify-content: center` (206):
  - **left, `flex: 1 1 300px; min-width: 280px; max-width: 470px`**: the bar SVG
    (207–227) with its three `sc-if` cover plates
  - **right, `flex: 1 1 300px; min-width: 260px`** (228–237):
    - three cover buttons (230–232). Style (810–811) is **its own**, not `seg` and not
      `segLight`: 17px 700, `padding: 11px 18px`, `min-height: 44px`, **2px `--ks3-ink`
      border always**, ground swaps `--ks3-card` → `--ks3-ink` with `--ks3-on-dark` text
      when pressed. Labels: `Cover the gas` / `Cover what is left` / `Cover the whole`.
    - `{{ coverResult }}` (234) at **28px display 800** — the arrangement that falls out
    - `{{ coverSentence }}` (235) at 19px — one sentence naming the operation
    - a static closing line (236) at 18px `--ks3-ink-body`: *"Two parts side by side make
      the whole. Cover the part you want and take the other one away from the whole."*

**Behaviour: three-way radio, always exactly one covered, default `gas`** (state line 569:
`cover: 'gas'`). Clicking the pressed button does **not** uncover — `onClick` sets, never
toggles (812). Compare the existing triangle, whose JS *does* toggle off
(`shared/ks3.js` 4975: `if (on) { tri.removeAttribute("data-covered"); }`). **Opposite
interaction contract.**

The covered label is repainted in `--ks3-ink-ghost` on top of the ink plate (217, 221,
225) — NOTES' *"the covered label stays faintly visible underneath"*. The existing
triangle's cover is a plain opaque `--ks3-ink` rect with **no ghost text**
(`ks3.css` 3011). **Second behavioural difference.**

`COVERS` payload verbatim (510–514):

| key | `result` | `sentence` |
|---|---|---|
| `whole` | `before = left in the flask + the gas` | Cover the whole bar and you are left with the two parts side by side — add them. |
| `left` | `left in the flask = before − the gas` | Cover the left part and you are left with the whole bar and the gas — take the gas away from the whole. |
| `gas` | `the gas = before − left in the flask` | Cover the gas and you are left with the whole bar and what stayed behind — take one away from the other. This is the one an open flask asks you for. |

### 7.6 Instrument — `balance-bench`, ONE CANVAS + DOM, NEW

**Gate** (118–132), `gateOpen: s.gate === null`. Prompt at 120: *"Commit first. Marble
chips react with acid in an open flask, fizzing hard. What does the balance do?"* — four
options (762–766). Body gated by `benchOpen` (772). Gated by absence.

**Controls**
1. **`rxnTabs`** (140–142), group label `Reaction` (138): `Marble chips and acid` /
   `Burning magnesium`. Changing it **resets `showAfter` to false** (779).
2. **`vesselTabs`** (148–150), group label `Vessel` (146): `Open flask` / `Sealed flask`.
   Also resets `showAfter` (786).
3. **The run button** (158), inside the canvas footer strip. Its own style (793–794):
   18px 700, `padding: 13px 22px`, 2px `--ks3-ink`, ground `--ks3-alert`, `opacity: .55`
   when spent. Label `Start the reaction` → `Reaction finished`, `disabled` once run.

**The canvas** — `width="1700" height="560"`, **850 × 280** design space at
`setTransform(2,…)`, ground `#100D0A`. `cx = 300, base = 214`.

- **Balance body** (620–630): a trapezium `(cx±150, base)` → `(cx±132, base+34)` in
  `#3E3730`, plus a `#5C5249` pan strip `fillRect(cx-128, base-10, 256, 12)`.
- **Flask** (632–650): a stroked conical outline in `#C6B9A7` at `lineWidth: 4`, filled
  with a liquid trapezium coloured by reaction — `rgba(143,183,255,0.35)` for marble,
  `rgba(255,197,61,0.28)` for magnesium.
- **Bung** (652–655): only when `vessel === 'sealed'` — a `#8A7A62`
  `fillRect(cx-28, base-132, 56, 16)`. **The vessel control changes the picture**, which
  is the p3-01 ramp-height lesson applied here.
- **Gas plume** (657–670): only when the run is done and `gas !== 'none'`. Seven
  shrinking circles rising from the neck, `#8FB7FF` when gas is leaving and `#FFC53D`
  when oxygen is joining, plus a mono label at `(cx+44, base-168)`:
  `gas leaving the flask` / `oxygen joining from the air`.
- **The digital display** (672–690): a `#221E1B` rect at `(570, 96)` sized 236 × 86,
  stroked `#5C5249`. Inside: a 12px mono `BEFORE` / `AFTER` tag in `#C6B9A7`, the mass at
  **34px mono in `#FFC53D`** via `.toFixed(2)`, a small `g` at x+150, and below the box
  `sealed flask` / `open flask`.

**Readouts — three tiles** (163–176), an auto-fit grid
`repeat(auto-fit, minmax(min(200px,100%),1fr))`, `gap: 12px`, each on `--ks3-dark-panel`:

| Tile | Label | Body |
|---|---|---|
| 1 | `Mass before` | `{{ beforeLabel }}` — 25px mono `--ks3-on-dark` |
| 2 | `Mass after` | `{{ afterLabel }}` — 25px mono **`--ks3-alert`**; reads `—` until run |
| 3 | `Where it went` | ⭐ **static literal**: `not measured — you work it out` — 19px 700 `--ks3-on-dark` |

Tile 3 never changes and takes no data. NOTES §8 is explicit that this mirrors the light
gates in `p3-01`; it is the QUANTITATIVE family's refusal-to-tell tile and must be
emitted as a real tile, not as prose.

Then `benchStatus` beside the run button (159) and `benchNote` (178) — a full-width
`--ks3-ground` panel on the ink block, 19px, carrying `RUNS[key].note` once run.

**Payload shape as actually authored** — NOTES §8 predicted
`{reaction, vessel, before_g, after_g, gas, ran}`. The file is richer:

```
{
  gate: { prompt: str, options: [4 × str] },
  reactions: [ {id: "marble", label: "Marble chips and acid"},
               {id: "magnesium", label: "Burning magnesium"} ],
  vessels:   [ {id: "open", label: "Open flask"}, {id: "sealed", label: "Sealed flask"} ],
  runs: { "rxn:vessel": { before: float, after: float, gas: "in"|"out"|"none", note: str } },  # 4, 492–501
  liquid_colours: { marble: "rgba(143,183,255,0.35)", magnesium: "rgba(255,197,61,0.28)" },
  gas_labels: { out: "gas leaving the flask", in: "oxygen joining from the air" },
  tiles: [ {label: "Mass before"}, {label: "Mass after"},
           {label: "Where it went", body: "not measured — you work it out"} ],
  run_labels: { idle: "Start the reaction", done: "Reaction finished" },
  status:     { idle: str, done: str },       # line 796
  idle_note:  str,                            # line 799
  decimals: 2,
  start_sealed: bool,
  progress: "{n} of 4 runs done",
  done_at: 3
}
```

### 7.7 The worked example, 242–266 — MRB-204 part 3

`<section class="ks3-block ks3-worked">`, **no id**. Head: eyebrow `Worked example · one
step at a time` (245), h2 carrying the numbers (246), and `workedProgress` top-right —
`'Step {n} of 4'` (817).

Each revealed step (251–260) is a flex row: a **38 × 38 `--ks3-accent-text` chip with
`--ks3-ground` text**, `border-radius: 11px`, display 800 20px, holding the letter; then a
mono uppercase label, a **26px display-800 line**, and an 18px `--ks3-ink-body` note. Row
ground `--ks3-inset`, 2px `--ks3-option-border`, `--ks3-r-panel`.

Reveal is `WORKED.slice(0, s.workedStep)` (818) — steps are **added to the list**, not
unhidden in place. Button (263) is `.ks3-reveal-btn` with labels `Show the first step` →
`Show the next step` → `All four shown`, disabled at 4. On completion a sibling span
appears (264): *"Now the same four steps on the other reaction."*

`WORKED`, verbatim (503–508):

| Letter | Label | Line | Note |
|---|---|---|---|
| F | Formula | `total mass before = total mass after` | Nothing is created and nothing is destroyed. Everything has to be counted, including the gas. |
| I | Insert | `2.40 g + mass of oxygen = 4.00 g` | The magnesium was weighed; the oxygen came from the air and was not. |
| F | **Fine-tune** | `mass of oxygen = 4.00 − 2.40` | Cover the part you want on the bar. Rearranged so the unknown is on its own, with both masses in grams. |
| A | Answer | `1.60 g of oxygen joined from the air` | The powder is heavier than the metal because it contains something that was not on the balance to start with. |

**Against the generator.** `r_fifa(staged=True)` (`build_ks3.py` line 2598) emits
`.ks3-fifa ks3-fifa-staged[data-stepper]` with one `<p class="ks3-fifa-step" hidden
data-step="i"><strong>letter · name</strong> line<span class="ks3-fifa-note">…</span></p>`
per step and one `[data-step-next]` button; `wireStepper` (`shared/ks3.js` line 4888)
unhides them one at a time and calls `markStage(sec, true)` at the end. The step **model
matches** (`{letter, name, line, note}` is §4.8.2's list shape, and `Fine-tune` is exactly
why that amendment exists). Three gaps, all inside the drawn component:

1. **No letter chip.** The generator concatenates `letter · name` into a `<strong>`;
   Design draws a 38px accent-text square with the bare letter and a separate mono label.
2. **No progress readout.** `'Step {n} of 4'` has nowhere to live.
3. **No done-note.** The *"Now the same four steps on the other reaction."* span (264) has
   no field.

Button labels are already configurable (`buttons.first` / `.next` / `.done`).

### 7.8 `#s-build`, 268–330 — MRB-204 part 4

`<section id="s-build" class="ks3-block">` + inline `--ks3-inset`. Eyebrow `Your turn ·
the same four steps` (269), h2 with the marble numbers (270), 52ch lede (271).

**Three commitment panels**, each `--ks3-card` on 2px `--ks3-option-border`,
`--ks3-r-panel`, `padding: 20px 22px`:

1. **`Step 1 · The rule`** (274–281) — a **vertical stack** of three
   `segLight`-styled buttons (mono 500, left-aligned), one per candidate rule
   (`formPicks`, 826–829). Radio, `disabled` once `buildOpen`.
2. **`Step 2 · Insert`** (283–290) — same shape, three candidate insertions
   (`insertPicks`, 835–838).
3. **`Steps 3 and 4 · Work it out, then answer`** (292–306) — a **free-text numeric input
   plus a unit `<select>`**:
   - `<input type="text" inputMode="decimal" id="c2ans" placeholder="0.00">`, mono 22px,
     `width: 8.5rem`, `min-height: 44px`, `--ks3-r-option`, 2px `--ks3-option-border`
   - `<select id="c2unit" class="ks3-sim-units">` with options
     `choose a unit` / `g` / `kg` / **`cm³`** / `N`
   - both `<label>`s are **visually hidden** via `position: absolute; left: -9999px`
     (295, 297) — a pattern the generator does not have a helper for

⭐ **`class="ks3-sim-units"` is a repo class** (`shared/ks3.css` 1227, applied by
`shared/ks3.js` 1072). Design reached into the shipped stylesheet for this one control.
It is the only place in C2 that does so.

**Gate** (309–312): the button is `disabled` unless *all four* of `formPick`, `insertPick`,
non-empty `ansText` and non-empty `ansUnit` are set (849). Progress span reads
`'{n} of 3 lines committed'` → `'Opened'` (851–852).

**Reveal** (314–329): `buildOpen`-gated, `data-arrive`, **ink ground** with
`--ks3-on-dark`. Head (316) mono uppercase in `--ks3-alert`: `The open flask, done four
ways`. Then four steps in the same F/I/F/A shape as the worked example but on ink —
34px `--ks3-alert` chips with `--ks3-ink` letters, 25px display lines, `--ks3-on-dark-body`
notes, separated by `2px solid var(--ks3-dark-rule)` top borders from the second row
(862). Then `buildClose` (327), composed at 864:
`'You wrote {ansText} {ansUnit}. The worked answer is 2.20 g.'`

**Against the generator.** `r_fifa_construct` (`build_ks3.py` line 1444,
`.ks3-construct`) is the registered `fifa-construct` kind and it renders **four free-text
`<input>`s, one per letter**, plus a Check button, a model `<ol>` and a success-criteria
tick list. It asserts `len(fields) == len(model) == len(success)` and that the letters
match the paired stepper's letters in order.

Design's page is a **different mechanism**: two multiple-choice ladders and one
number+unit pair, three commitments, no tick list, no success criteria, an ink-ground
model reveal, and a closing line that quotes back what the student typed. The existing
assertions would **raise** on it (there are 3 commitments and 4 model lines, and there
are no success criteria at all). See §10, gap N6.

Note the same defect the generator already fixed for B1 exists here: `<input value="{{
ansValue }}">` at line 296 sets an attribute, and the DC runtime re-renders on every
state change — a generator port must not emit a `value` attribute.

---

## 8. The `cover-triangle` kind, and its BAR variant

The 15 Aug change-log names `cover-triangle` as "the one to build once" across `p3-01`,
one other lesson and `c2-06`. **In C2 only `c2-06` uses it, and only as a bar.**

### 8.1 What already exists

| Piece | Where | Notes |
|---|---|---|
| `formula` block type | `BLOCK_RENDERERS` (`build_ks3.py` ~3243), `r_formula` (3149) | statement + optional `triangle`; **MRB-204 part 1 is satisfied** |
| `r_formula_triangle` | `build_ks3.py` line 1562 (geometry helper `_triangle_geometry` at 1523) | draws the triangle in SVG with clipped covers |
| geometry constants | `TRI_W, TRI_H, TRI_PAD, TRI_DIV_Y = 260, 216, 8, 130` (line 1520) | **hard-coded triangle** |
| slots | `top` / `left` / `right`, literal in the loops | |
| CSS | `.ks3-triangle`, `.ks3-tri-svg`, `.ks3-tri-path`, `.ks3-tri-div`, `.ks3-tri-label`, `.ks3-tri-cover`, `.ks3-tri-btns`, `.ks3-tri-note`, `.ks3-tri-close` — `ks3.css` 2991–3027 | `.ks3-tri-cover` is opaque ink, `opacity: 0/1` |
| JS | `shared/ks3.js` 4968–4982, `[data-triangle]` / `.ks3-tri-btn` / `data-cover` / `data-covered` | **toggles off** on a second press |

### 8.2 What c2-06 needs that none of it provides

| # | Need | Why the triangle path cannot serve it |
|---|---|---|
| B1 | **Shape `bar`** | Geometry is a hard-coded 260 × 216 triangle path with a divider line. There is no branch, no `shape` key, and no second geometry function |
| B2 | **Slots `whole` / `left` / `right-part`**, arranged as one bar over two | The renderer's loops are literally `for key in ("top","left","right")`. `top` is *above* the divider (the numerator); on a bar the whole is above and the parts are below and **must sum in width** |
| B3 | **Part widths that encode the proportion** | 450 = 296 + 8 + 146. A triangle has no widths to author. The bar's widths must be authored or derived, and they are the arithmetic |
| B4 | **A ghost label under the plate** | `.ks3-tri-cover` is a plain rect. The bar repaints the label in `--ks3-ink-ghost` on top (lines 217/221/225) |
| B5 | **Radio, not toggle** | `ks3.js` 4975 removes `data-covered` on re-press. c2-06 never uncovers (812) and **starts covered** (`cover: 'gas'`, 569) |
| B6 | **A `result` line in display type** | The triangle emits only `.ks3-tri-note` prose. The bar emits **28px display 800 `coverResult`** *and* a 19px `coverSentence`. Two fields per cover, not one |
| B7 | **A second drawing above it** | The balance beam (186–198) shares the section with the bar. The `formula` block renders one statement and at most one triangle |
| B8 | **Two mono support lines** under the statement | `everything means the gases too` / `mass is measured in grams (g)` (line 201) — no field |
| B9 | **A static closing sentence** beside the buttons | line 236 — the `close` field exists on the triangle but renders centred under it, not in the right-hand column |

### 8.3 The payload the amended kind needs

Design's change-log shape is `{shape, cells:[{id,label,slot}], covered, results:{id:{result,sentence}}}`.
Measured against the page, the honest shape is:

```python
"formula": {
    "eyebrow":   "The rule",
    "statement": "total mass of everything before = total mass of everything after",
    "support":   ["everything means the gases too",
                  "mass is measured in grams (g)"],
    "figure": {                       # part 2, drawn — NOT necessarily a triangle
        "shape": "balance",           # "triangle" | "balance" | "bar"
        "aria_label": "A balance beam, level. …",
        "pans": {"left": "before", "right": "after"},
        "caption": "always level",
    },
    "cover": {                        # the cover-triangle kind, bar variant
        "shape":   "bar",
        "eyebrow": "The bar",
        "heading": "Cover the one you want",
        "aria_label": "A bar model. One long bar is everything before …",
        "whole":  {"id": "whole", "label": "everything before",
                   "button": "Cover the whole"},
        "parts": [{"id": "left", "label": "left in the flask",
                   "button": "Cover what is left", "weight": 296},
                  {"id": "gas",  "label": "the gas",
                   "button": "Cover the gas",      "weight": 146}],
        "covered": "gas",             # the default, and it is never none
        "mode":    "radio",           # vs the triangle's "toggle"
        "results": {"whole": {"result": "before = left in the flask + the gas",
                              "sentence": "Cover the whole bar and you are left …"},
                    "left":  {...}, "gas": {...}},
        "close": "Two parts side by side make the whole. Cover the part you want "
                 "and take the other one away from the whole.",
    },
}
```

**The ruling that is still Mide's to make** (NOTES flag 14, restated in the change-log and
unchanged): is "drawn as a triangle" shorthand for *drawn, in whatever shape the
relationship has*? Everything above assumes yes and is buildable either way — if the
answer is "triangles are literal", `c2-06` has to be redrawn and this whole section is
void. **The page as frozen contains no triangle, so a build cannot proceed on the literal
reading without a redraw from Design.** This is the one place in C2 where the answer
changes what gets built, and it is a real product decision, not an implementation detail.

---

## 9. Cross-cutting mechanics the generator has to learn

### 9.1 Gating by absence, seven times

Every gate in C2 is `<sc-if value="{{ gateOpen }}">` where `gateOpen: s.gate === null`,
and the instrument body is `<sc-if value="{{ xOpen }}">` where `xOpen: s.gate !== null`.
**The gate panel disappears once answered** — it is not disabled, not dimmed, not
collapsed. Instances: c2-01 `#s-model` (120/136), c2-03 `#s-bench` (118/134), c2-05
`#s-builder` (118/134), c2-06 `#s-balance` (118/134). Plus the four hook reveals and six
misconception reveals, which are the ordinary Law 4 shape.

The generator's Law 4 wiring (`shared/ks3.js` ~752–780) unhides a `[data-reveal]` and
leaves the options in place. **The instrument gate is the opposite: the options go and
the instrument arrives.** A new state, not a variant of the existing one.

### 9.2 One-shot locking, five instances

c2-02 verdicts (563), c2-03 sort (688), c2-04 symbols (498) and reads (518), and the
ladder's marked rungs (all six). Every one is `if (state[x] !== undefined) return null;`
inside the updater — belt and braces on top of the `disabled` attribute.

### 9.3 Composed strings that a data record must be able to express

Not a single one of these is a plain authored string:

| Page | Line | Composition |
|---|---|---|
| c2-01 | 600–601 | `'Switching off ' + n + (n===1 ? ' claim leaves ' : ' claims leaves ') + broken + ' of the four observations…'` — **an inline plural** |
| c2-01 | 687 | `zoomAlt` = `'A magnified view of copper at ' + scale + ': ' + label.toLowerCase() + '.'` |
| c2-02 | 527 | `budgetLabel` = `left + ' of ' + budget + ' tests left · ' + n + ' of 6 decided'` |
| c2-02 | 529 | tab label + `' ·'` when decided |
| c2-03 | 660–662 | `dishAlt`, two-way |
| c2-05 | 638–640 | `molAlt`, three-way |
| c2-05 | 641 | `builtName` for a non-substance, **assembled from symbols and ASCII digits** |
| c2-06 | 789–790 | `benchAlt`, composed from vessel + a `.toFixed(2)` mass + before/after |
| c2-06 | 864 | `buildClose` quotes the student's own input back |
| all six | rail | `railCountLabel`, `railBarStyle` |
| all six | ladder | `tallyText` = `'All {n} ticked — rung met.'` / `'{met} of {n} ticked — not yet.'` |

An inventory that stores only flat strings loses all of these. Every one needs either a
format template with named slots or a small set of renderer-side rules.

### 9.4 Every canvas is hard-coded hex, never a token

`#100D0A` (ground, all four canvases), `#5C5249`, `#C6B9A7`, `#FFC53D`, `#3E3730`,
`#221E1B`, `#6E655D`, plus per-instrument palettes (`#B7692F`/`#D98A4A`/`#8A4A1E`/
`#A85F2A`/`#7A4520`/`#5A3212` for copper; `#9AA0A6`/`#E9C445` for iron and sulfur;
`COLOURS` at c2-05 line 429; `#8FB7FF`/`#8A7A62` for c2-06). A canvas cannot read a CSS
custom property without `getComputedStyle`, so this is a legitimate constraint rather than
drift — but it means **a token-drift gate must exempt canvas literals**, and the values
must be lifted as data rather than retyped.

Two canvas fonts are named as strings: `"DM Mono", ui-monospace, monospace` and
`"Bricolage Grotesque", system-ui, sans-serif`.

### 9.5 Canvas geometry, all four

| Page | Attribute size | Design space | Transform | Aspect |
|---|---|---|---|---|
| c2-01 `#s-scale` | 1800 × 620 | 900 × 310 | `setTransform(2,0,0,2,0,0)` | exact |
| c2-03 `#s-bench` | 1700 × 560 | **850 × 280** | `setTransform(2,…)` | exact |
| c2-05 `#s-builder` | 1700 × **520** | **850 × 260** | `setTransform(2,…)` | exact |
| c2-06 `#s-balance` | 1700 × 560 | **850 × 280** | `setTransform(2,…)` | exact |

All four are `<canvas … ref="{{ xRef }}" role="img" aria-label="{{ xAlt }}"
style="display:block; width:100%; height:auto;">` inside a wrapper with
`border-radius: var(--ks3-r-card); border: 2px solid var(--ks3-on-dark-muted);
overflow: hidden`, with a `--ks3-dark-panel` footer strip carrying the controls or the
caption. **That wrapper is one component**, used four times.

None of them carries `class="ks3-sim"`, so the registered `sim canvas` component that
gates `practical` has nothing to gate here — the same divergence b1-04, b1-05 and b1-06
recorded.

### 9.6 Redraw discipline

All four canvas pages implement `componentDidUpdate() { this.draw(); }` — **every state
change redraws**, including a ladder tick. There is no dirty check and no rAF. NOTES §8's
"c2-06's bench redraws on control changes only" is **not quite what the code does**: it
redraws on every render. Harmless (the draws are cheap and there is no animation) but
worth stating so a port does not inherit a claim the source does not make.

---

## 10. What no existing generator component covers

The complete list. "EXISTING" means `build_ks3.py` can render it from data today.

### 10.1 Existing and reusable, unchanged

`hook` · `explainer` · `key-fact` (needs `ground: "card"` on all six) · `misconception`
shell · `quiz` (the ladder, byte-identical on all six) · `summary` (keynote) ·
`r_layer` (Going further) · endmatter · `safety_note` · the rail component · the
`.ks3-option` / `.ks3-options` lettered option list · `.ks3-reveal` + `data-arrive`.

### 10.2 New activity kinds — six, none of which exists

| Kind | Lesson(s) | Shell | Canvas | One-line demand |
|---|---|---|---|---|
| **`claim-switch`** | c2-01 `#s-model` | `check` (light) | no | 3 toggles + 4 dependency rows whose text is replaced by a failure sentence |
| **`scale-zoom`** | c2-01 `#s-scale` | `practical` (dark) | **yes** | 2 step buttons over 5 authored drawings + a segment strip |
| **`test-budget-bench`** | c2-02 `#s-bench` | `check` (light) | no | 6 samples × 4 tests against **one global budget**, one verdict each |
| **`mixture-compound-dish`** | c2-03 `#s-bench` | `practical` (dark) | **yes** | 2 states × 3 proportions (proportion **disabled when heated**) × 4 before/after tests |
| **`formula-builder`** | c2-05 `#s-builder` | `practical` (dark) | **yes** | 3 pairs × 3 × 3 counts → 5 known substances, 22 "not a substance" |
| **`balance-bench`** | c2-06 `#s-balance` | `practical` (dark) | **yes** | 2 reactions × 2 vessels, a run button, three tiles of which one never measures |

Plus **two shared shapes** that appear more than once and should be built once:

| Kind | Instances | Demand |
|---|---|---|
| **`verdict-cards`** | c2-03 `#s-sort` (2 options, prose headline), c2-04 `#s-read` (4 options, **mono formula** headline) | a column of one-shot commit-and-reveal cards |
| **`origin-grid`** | c2-04 `#s-sort` (9 cards, 3 buckets, auto-fit grid, 42px symbol headline) | the same contract laid out as a grid with a display headline |

`verdict-cards` and `origin-grid` differ only in layout (column vs auto-fit grid) and
headline type (prose / mono formula / display symbol). **One kind with `layout` and
`headline` keys is the honest reading**; two kinds is also defensible. It is a code
decision, not a Design one.

And **one more**:

| Kind | Instance | Demand |
|---|---|---|
| **`model-limit`** | c2-05 `#s-limit` | two contrast cards, one light and one **ink**, then a 3-option commit and an ungated reveal |

### 10.3 Gaps in components that DO exist

| # | Gap | Where | Detail |
|---|---|---|---|
| **N1** ⭐ | **`formula` has no `shape: "bar"`** | c2-06 rule section | §8. Triangle geometry is hard-coded (`TRI_* = 260, 216, 8, 130`), slots are literally `top`/`left`/`right`, the cover is a plain opaque rect, and the JS toggles off. The bar needs its own geometry, part weights that sum, ghost labels, radio semantics, a default cover, and a two-field result per cover |
| **N2** ⭐ | **`formula` renders one drawing** | c2-06 rule section | The section holds a **balance beam AND a bar**, plus two mono support lines under the statement. Three drawn/typed elements in one block; the renderer has room for one |
| **N3** | **No commit-and-reveal card set** | c2-03 `#s-sort`, c2-04 `#s-sort`, c2-04 `#s-read` | Three instances, one shape. The nearest existing kinds — `sort-rows` (`ks3-sort`, chips into named columns) and `sort-task` (`ks3-hard`) — are neither: these are per-card multiple choice with a per-card written answer |
| **N4** | **Instrument gates are absence-gated** | 4 instruments | §9.1. Existing Law 4 unhides a reveal and leaves the options; C2 removes the gate and swaps in the instrument |
| **N5** | **`worked-example` stepper has no letter chip, no progress readout, no done-note** | c2-06 242–266 | §7.7. `r_fifa(staged=True)` renders `letter · name` in a `<strong>`; Design draws a 38px accent square, a mono label, a 26px display line and a note, plus `Step {n} of 4` and a closing span |
| **N6** ⭐ | **`fifa-construct` is the wrong mechanism** | c2-06 `#s-build` | §7.8. Existing: 4 free-text inputs + Check + model `<ol>` + success ticks, with a hard assertion that fields == model == success. Design: 2 multiple-choice ladders (3 options each) + 1 number field + 1 unit `<select>` + a 4-step ink reveal + a line quoting the student's input. The existing assertions would raise |
| **N7** | **A misconception reveal is one string** | all six `#s-think` | Every C2 reveal is **two paragraphs**. `r_activity` emits `<div class="ks3-reveal" hidden data-reveal>%s</div>` from `a["reveal"]` — one string |
| **N8** | **No ground override on `.ks3-block`** | c2-03 `#s-sort`, c2-04 `#s-read`, c2-05 `#s-limit`, c2-06 `#s-build` | Four light blocks carry inline `background: var(--ks3-inset)`. `.ks3-block` is `--ks3-card` and there is no `ground` on the activity shells (only on `key-fact`, `rule` and `comparison`) |
| **N9** | **No 3-option commit** | c2-05 `#s-limit` | Every other commit in KS3 is four options. `r_activity_options` takes a list, so this is free — recorded so it is not "corrected" to four |
| **N10** | **No visually-hidden label helper** | c2-06 295, 297 | `position: absolute; left: -9999px` on two `<label>`s. No `.ks3-sr-only` in `shared/ks3.css` |
| **N11** | **No number + unit answer pair** | c2-06 292–306 | Text input with `inputMode="decimal"` beside a `select.ks3-sim-units` offering `g` / `kg` / `cm³` / `N`. The class exists; the pairing has no renderer |
| **N12** | **The dark-canvas frame is unnamed** | 4 canvases | §9.5. One wrapper shape used four times; no component, no class, no CSS |
| **N13** | **`Connects to` endmatter heading** | c2-06 457 | The second endmatter card is `Connects to` on the unit's last lesson, `Next in this unit` on the other five |
| **N14** | **A stage needs both a `done_when` and a `progress` string, and they may disagree** | c2-05, c2-06 | F5. `'of 5'` with `done_at: 3`, `'of 4'` with `done_at: 3` |
| **N15** | **The `testBudget` prop has nowhere to live** | c2-02 | A per-lesson teaching dial (4–24, default 8). §4.8 has no prop concept. Dropping it removes the lesson's pedagogy |
| **N16** | **`ORIGINS` / `element` / `origin` are authored and unread** | c2-02 `SAMPLES[].element`, c2-04 `SYMBOLS[].origin` | Correctness data with no marker behind it. An orphan-key sweep will flag both; they are Design's intent, not slips — keep them and say so |

### 10.4 Not a gap, but must be carried

- **All nine meaning-bearing non-ASCII codepoints** (F3), including U+2212 MINUS in five
  places and five distinct subscripts. Font-subset check required before build.
- **The `.ks3-mis-quote` curly quotes are page-level**; the authored statement must be
  stored **without** them (the renderer adds them) — b1-02's precedent.
- **`c2-05`'s not-a-substance name uses ASCII digits** (line 641) while every authored
  name uses subscripts. Reproduce as written; changing it is Mide's call.
- **`c2-01`'s `touched >= 2` and `c2-03`'s pre-seeded `seenTests`** are lenient completion
  rules. Reproduce; do not tighten.

---

## 11. Findings requiring a decision, consolidated

| # | Finding | Whose call |
|---|---|---|
| **F1 / N1** | c2-06 draws a **balance beam and a part–whole bar and no triangle anywhere**. NOTES flag 14's ruling is still open and now blocks the component | **Mide** — product/pedagogy |
| **F2** | NOTES §7's coming-soon instruction for c2-04 is dead; the page carries a live link | resolved here — do not implement §7 |
| **F3** | Nine meaning-bearing non-ASCII codepoints, not one. `₃` in `CaCO₃` is flag 13's; there are eight more | Code — font-subset verification |
| **F4** | `hint-placeholder-count` is 4 on c2-04 and c2-05, both of which have 5 rail stops | cosmetic; recorded |
| **F5** | Two progress readouts promise more than their `done_when` requires (c2-05 5 vs 3, c2-06 4 vs 3) | **Mide** — is the readout or the gate the intent? |
| **F6** | c2-05's builder never banks the substance it opens on | Code may fix inside the drawn component; state it |
| **F7** | `magnesium:sealed` reuses the marble masses (152.00 → 152.00) with no note explaining it | **Mide** — science/content accuracy |
| **N16** | `SAMPLES[].element` and `SYMBOLS[].origin` are authored and read by nothing | recorded; keep the data |
| §9.6 | NOTES says c2-06 "redraws on control changes only"; the code redraws on every render | recorded; harmless |

---

*Measured 16 Aug 2026 from the frozen files in `docs/ks3/design-reference/c2/`. Every
line number cited is a line number in those files and was read, not inferred. No lesson
module was authored and no generator file was modified.*
