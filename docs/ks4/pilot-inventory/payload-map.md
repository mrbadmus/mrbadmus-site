# KS4 pilot — payload map

The whole-pilot summary the per-lesson files don't each repeat: the block
vocabulary as actually used across all 14 lessons, the shared components'
verified prop shapes, the family → line-up table, the route-tag inventory,
the shared assets every page loads, and the state spaces as observed. Source:
the same `reference.json` the 14 lesson files draw from, plus
`NOTES-KS4-pilot.md` (§3, §7, §8) and each `.dc.html`'s own source, read
directly. Method: `README.md` in this folder.

---

## 1. Block vocabulary, as used (not as specified)

Every `<section>`/`<div id="s-…">` across all 14 lessons, classified to the
closed KS3+KS4 vocabulary from `pilot-build-contract.md` §1 (hook, explainer,
figure, worked-example, check, keyword, practical, misconception, summary,
quiz, key-fact, rule, formula, comparison, required-practical, equation,
extended-response, exam-tip, ladder, key-note, question-bank, end, video,
chrome). Fixed-template blocks (chrome, hook, key-fact, keyword, exam-tip,
ladder, key-note, question-bank, end, video) appear once per lesson, 14 times
each, and are **not** re-tallied below — see §2 for their shared component.
The middle (family-ordered) blocks are what varies:

| Type used | Count | Lessons · section id |
|---|---|---|
| `check` | 19 | chemical-bonds#s-decider, chemical-bonds#s-sort, ionic-bonding#s-draw, ionic-bonding#s-forge, ionic-compounds#s-lens, ionic-compounds#s-deduce, covalent-bonding#s-build, metallic-bonding#s-sort, states-of-matter#s-method, states-of-matter#s-limits, states-of-matter#s-symbols, properties-small-molecules#s-model, properties-small-molecules#s-rank, polymers#s-classify, giant-covalent-structures#s-sort, metals-alloys#s-pick, nanoparticles#s-sizes, series-parallel-circuits#s-rules, resistors#s-vars |
| `worked-example` | 7 | ionic-bonding#s-watch, covalent-bonding#s-watch, polymers#s-addition, nanoparticles#s-cube, nanoparticles#s-calc (CFIFA), series-parallel-circuits#s-calc (CFIFA), resistors#s-calc (CFIFA) |
| `misconception` | 11 (explicit block) + 3 (confront inside the flagship, no block) | explicit: chemical-bonds#s-think, ionic-compounds#s-think, covalent-bonding#s-sort (carries `ks3-misconception` on the SORT section itself — a shape unique to this lesson), metallic-bonding#s-think, states-of-matter#s-think, properties-ionic-compounds#s-think, polymers#s-think, giant-covalent-structures#s-think, metals-alloys#s-think, nanoparticles#s-think, resistors#s-think. Inside-flagship (no separate section, confirmed by source: no `ks3-misconception` class anywhere on the page): ionic-bonding (gate 3 of the stepper), properties-small-molecules (first boiling-point crossing), series-parallel-circuits ("add a branch") |
| `practical` | 6 | metallic-bonding#s-bench (electron-sea workbench), states-of-matter#s-lab (heating-curve investigation), properties-ionic-compounds#s-bench (side-by-side beakers), metals-alloys#s-mixer (alloy mixer), series-parallel-circuits#s-bench (change-one-part bench), resistors#s-sim (thermistor predict) |
| `comparison` | 4 | ionic-compounds#s-models, properties-ionic-compounds#s-chain, giant-covalent-structures#s-compare, metals-alloys#s-chain |
| `equation` | 3 | nanoparticles#s-equation, series-parallel-circuits#s-equation, resistors#s-equation — every one immediately precedes its lesson's `s-calc` (CFIFA), matching NOTES §4: "It always sits directly before a `Ks4Cfifa`" |
| `extended-response` | 2 (mid-lesson) + 14 (ladder rung 4, universal) | mid-lesson: properties-ionic-compounds#s-examiner ("Be the examiner"), nanoparticles#s-evaluate (sun cream). NOTES §4 names both explicitly as the only mid-lesson uses; every OTHER lesson's `extended-response` is ladder rung 4 only |
| `required-practical` | 1 | resistors#s-rp — the only Required Practical family lesson in the pilot |

**Closed-vocabulary types NOT used in the pilot's middle sections:** `figure`
(diagrams are mounted through `KS4.fig()` INSIDE other blocks, e.g. a
`figureSvg` prop on `check`/`worked-example`/`equation` blocks, never as a
standalone section — confirmed: no lesson has a bare section whose sole
content is a figure), `summary`, `quiz` (the Question bank is the type
`question-bank`, not `quiz` — `quiz` as KS3 defined it does not appear),
`rule`, `formula` (subsumed into `equation` at KS4), `keyword` beyond the one
fixed command-words `<dl>` per lesson.

**Every lesson's middle also has 2–3 `ks3-explainer` prose sections** (no id,
class `ks3-explainer`) threading the instruments together — 73–202 words each
per NOTES §2, confirmed against `words` in `reference.json`.

## 2. Component prop shapes, as used (verified against the pages)

`NOTES-KS4-pilot.md` §3's table, cross-checked directly against every
`Ks4*.dc.html`'s own `data-props` attribute and template. Confirmed
byte-consistent with NOTES; no drift found between the documented API and
what a lesson actually passes.

| Block | Props (kebab-case in templates) | Emits | Verified against |
|---|---|---|---|
| `Ks4Choice` | `eyebrow, command, prompt, options[{text, reply, correct?}], reveal, right-word, wrong-word, figure-svg` | `on-commit(i, option)` | `Ks4Choice.dc.html` L20–L39; reveal `<p>` carries **no distinguishing class**, only the `[data-arrive]` wrapper on its parent `<div>` — a real gap against KS3's `.ks3-reveal`, noted because it affects any parity/measurement tooling that assumes a `.ks3-reveal` class exists at KS4 |
| `Ks4Sort` | `eyebrow, title, prompt, bins[{id,label}], items[{text,bin,why}], done-note` | `on-done({correct})` | tap-card-then-tap-bin, no drag. Every card, every bin AND the "Check the sort" button are all real `<button>`s (`Ks4Sort.dc.html` L26/L33/L36/L44), so its total button count is `items + bins + 1`. Confirmed for chemical-bonds: 8 items + 3 bins + 1 check = 12, matching `sort_button_count: 12` in `reference.json`. ⚠️ Its OWN check button also carries `class="ks3-reveal-btn"` — the same collision-prone class the Question bank's "load more" uses (see method note 3); the two never collide with each other in practice only because they sit in different, non-overlapping DOM subtrees when scoped correctly |
| `Ks4Chain` | `eyebrow, title, prompt, links[] (in order), herrings[{text,why}], scored, done-note` | `on-done({correct})` on first check | |
| `Ks4Write` | `id, eyebrow, command, marks, question, points[], levels[{label,text,max}]?, reject[], figure-svg, min-words` | `on-mark({awarded,marks,set})` | present as ladder rung 4 on all 14 lessons (`ladder_write_present: true` in every lesson's interaction pass) |
| `Ks4Cfifa` | `examples[{tab,head,next?,steps[{letter,label,line,note}]}], questions[{tab,id,head,close,steps[{letter,label,placeholder,line}]}]` | `on-open(openedCount,total)` | only on L12/L13/L14 (the three `equation` lessons) |
| `Ks4Ladder` | `slug, rungs{r1,r2,r3,r4}` | `on-done(score)` | `.ks3-rung` × 4 confirmed on every lesson (`rungCount: 4` uniformly in reference.json); feedback class is `ks3-feedback is-correct`/`is-wrong` (`Ks4Ladder.dc.html` L215) |
| `Ks4KeyNote` | `title, spec, lines[]` | — | `lineCount: 6` on **every one of the 14 lessons**, confirmed — the "6 lines" in NOTES §2 is not a typical case, it is universal in this pilot |
| `Ks4QuizBank` | `questions` (from `KS4.bank(slug,route)`), `route-label` | — | ⚠️ **paginates behind its own `.ks3-reveal-btn` ("Show N more"), `state.shown` starts at **4**.** That class name COLLIDES with `#s-sort`'s "Show what settles each one" button. A naive `document.querySelector('.ks3-reveal-btn')` finds the SORT's button first (disabled until the sort is complete) and looks exhausted after zero clicks — this is exactly what `measure_design.py`'s first draft did, undercounting every chemistry lesson's bank at a flat 4. Fixed by scoping the click to the bank's own root (found via its "Practice set" eyebrow). See §4 below for the corrected per-lesson counts |
| `Ks4End` | `subject, prev, next, connects[], tutor-line, legal` | — | |
| `Ks4Chrome` | `subject, unit, title, rv` (from `KS4.rail`) | — | ⚠️ **The top progress bar is NOT width-driven.** `Ks4Chrome.dc.html`'s `Component.state = {scrolled:false}`; `showTop` in the render is literally `this.state.scrolled`, flipped by a `scroll` listener testing `window.scrollY > 140`. Below 1340px the side rail is CSS-hidden (`[data-rail="side"]{display:none}`) and the top bar starts hidden too (state default `false`), so **at the top of a narrow page, neither rail is visible** — confirmed identically on all 14 lessons at 820/390/360, `rail.topVisible: false` at scrollY=0, `rail_after_scroll.topVisible: true` after `scrollTo(0,300)` |

## 3. The eight families → block line-ups (this pilot's 14)

| Family | Lessons | Flagship shape used |
|---|---|---|
| CLASSIFY | L1 chemical-bonds, L9 polymers | Decision instrument (bond decider; structure decider) |
| PROCESS | L2 ionic-bonding, L4 covalent-bonding | Worked stepper with gated predictions, then pupil builds the same sequence |
| MODEL | L3 ionic-compounds, L5 metallic-bonding, L8 properties-small-molecules | Parameter instrument with predictions at each regime change (lattice lens; electron-sea workbench; two-forces model) |
| CONTRAST | L7 properties-ionic-compounds, L10 giant-covalent-structures, L11 metals-alloys | Predict-gated A/B or mixer instrument, then linked-comparison `Ks4Chain` |
| INVESTIGATION | L6 states-of-matter | Critique-a-flawed-method sort, after a messy-data lab sim |
| QUANTITATIVE | L12 nanoparticles | Simulation (cube splitter) feeding straight into `equation` → `Ks4Cfifa` |
| SYSTEM | L13 series-parallel-circuits | Break/change-one-part bench, predict the knock-on |
| REQUIRED PRACTICAL | L14 resistors | `required-practical` block, then the practical's own misconception and variables |

Confirms NOTES §7's closing line: **no two lessons in the same family share a
line-up** — CONTRAST alone uses three different flagship shapes (beakers,
A/B-plus-table, mixer) across its three lessons.

## 4. Question bank — corrected per-lesson counts (Triple Higher, fully expanded)

| Lesson | Bank items (TH) | "Load more" clicks needed |
|---|---|---|
| chemical-bonds | 12 | 2 |
| ionic-bonding | 12 | 2 |
| ionic-compounds | 12 | 2 |
| covalent-bonding | 12 | 2 |
| metallic-bonding | 12 | 2 |
| states-of-matter | 12 | 2 |
| properties-ionic-compounds | 12 | 2 |
| properties-small-molecules | 12 | 2 |
| polymers | 12 | 2 |
| giant-covalent-structures | 12 | 2 |
| metals-alloys | 12 | 2 |
| nanoparticles | 11 | 2 |
| series-parallel-circuits | 2 | 0 |
| resistors | 2 | 0 |

Matches NOTES §9 flag 4 (nanoparticles: 11 TH) and flag 14 (physics quizzes
are thin: 2 questions, one route copy) exactly.

## 5. Route-tag inventory (NOTES §8, cross-checked against `reference.json`'s section-count-by-route)

| Content | Tag | AQA source | Confirmed in reference.json |
|---|---|---|---|
| Limitations of the particle model (states-of-matter `#s-limits`) | `higher` | 8462/8464 5.2.2.1 (HT only) | 16 sections TH/CH vs 15 CF/TF |
| Addition polymerisation (polymers `#s-addition`) | `triple` | 8462 4.7.3.1 | 14 sections TH/TF vs 13 CF/CH |
| Thermosoftening/thermosetting polymers (same section) | `triple` | 8462 4.10.4.3 | (folded into the same `#s-addition` delta above) |
| Named alloys and their uses (metals-alloys `#s-pick`) | `triple` | 8462 4.10.4.2 | 15 sections TH/TF vs 14 CF/CH |
| Nanoparticles, whole lesson | `triple` | 8462 4.2.4 | Design's review page renders all 4 routes identically (17 sections every route) — the tag applies at the **URL-build level** (2 of 4 URLs exist per `pilot-build-contract.md` §0), not as an in-page conditional; see the nanoparticles lesson file |
| Graphene, fullerenes, nanotubes (giant-covalent-structures `#s-sort`) | `base` | 5.2.3.3 (no HT marker) | untagged, all 4 routes identical (15 sections every route) |
| Covalent dot-and-cross drawing | `base` | 5.2.1.4 | untagged, all 4 routes identical (15 sections every route) |
| Everything else in the pilot | `base` | — | 8 of 14 lessons show byte-identical section counts across all 4 routes |

## 6. Shared assets every lesson loads

From every `.dc.html`'s `<helmet>`, confirmed identical across all 14 files:

- `../../_ds/mrbadmusai-design-system-…/styles.css` — the design-system bundle (fonts, base tokens)
- `ks4-theme.css` — dark-mode token remap (`prefers-color-scheme` / `theme` prop)
- `ks4-source.js` — the verbatim-text data module (quiz per route, tips, key notes, FIFAs, equations, RPs)
- `ks4-lib.js` — `window.KS4`: `route()`, `find()`, `bank()`, `tip()`, `fifas()`, `cfifa()`, `rail`, `observe`, `load`, `save`, `fig()`
- `ks4-diagrams.js` — pure SVG-string diagram functions
- One page-local `<style>` block (small, animation keyframes + reduced-motion overrides + narrow-width fixes)
- `support.js` (the DC/React/Babel runtime — **does not ship**; compile-time only, per `pilot-build-contract.md` §1)

Fonts confirmed via computed style across all 14: **Bricolage Grotesque** (headings, 800), **Instrument Sans** (body, 400/600/700), **DM Mono** (eyebrows, badges, mono labels) — no lesson deviates.

## 7. State spaces, as observed (NOTES §7, cross-checked)

Every lesson's NOTES §7 line-up is reproduced verbatim in each per-lesson
file's opening section. What the browser pass adds beyond NOTES' own prose:

- **Ladder is uniformly 4 rungs, uniformly ~200–450 words**, `hasCommandWords: true` on all 14 — the command-word vocabulary (Recall/Apply/Explain/Produce plus lesson-specific Compare/Evaluate/Deduce/Calculate) is present in every ladder's rendered text, not just its data.
- **Key note is uniformly 6 lines** on all 14 lessons (see §2 above).
- **`swaps_instantly` under reduced motion is `true` on all 14 lessons** for the shared `[data-arrive]` hook-reveal mechanism — the one universal animated instrument every lesson has, and the one this run could cheaply prove per-lesson rather than assert once. The lesson-specific instruments (electron-sea drift, particle heating-curve, alloy mixer push) were **not** individually proven to swap instantly by this run — screenshots at 1280/360 exist for visual spot-check, but no per-instrument reduced-motion assertion was scripted for anything beyond the shared hook mechanism. Flagged as a real gap, not silently assumed clean.
- **Keyboard: 0 `tabindex="-1"` controls found on any of the 14 lessons** — 57–76 focusable controls per lesson, every one a native interactive element.
- **Console: 0 errors on all 14 lessons, at all 5 widths, on the default route.** No lesson's other-3-routes pass (1280 only) logged an error either.
- **Overflow: 0 instances at any width (1280/1340/820/390/360) on any lesson's default-route sweep.**

## 8. Known measurement limitations (see also README §"Limitations")

- The Write rung's min-words unlock (interaction step 6 in every lesson file) is **not reliably measured** — by the time it runs, rung 1 is already answered+disabled, so the generic `#s-ladder button` click target can land on rung 2/3's own controls instead of rung 4's *Check my answer*. Not evidence either way about the real unlock behaviour.
- Dark-mode computed styles were captured only for the FIXED (always-present) component set, on a fresh mount — the reveal panel and chosen-option styles (state-dependent) were captured in light mode only, inside the interactions pass, which runs after the dark-mode pass has already reset to light.
- Per-instrument reduced-motion proof (beyond the shared hook mechanism) was not scripted individually — see §7 above.
