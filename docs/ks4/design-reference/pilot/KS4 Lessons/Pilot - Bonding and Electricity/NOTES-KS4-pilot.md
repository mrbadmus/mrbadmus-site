# NOTES — KS4 pilot (Bonding 5.2 + Electricity 6.2.1.4, 6.2.2)

**All 14 lessons are authored**, one runnable `.dc.html` per lesson, built on ten shared blocks. These pages set the KS4 standard the way B1 did for KS3: §2–§6 are written so Code can generate the other 250 lessons from them. §9 is the numbered science flags, each with its AQA source. §10 is every place the architecture did not survive a real page, and what I did instead.

Mide was asleep; every call normally asked was made and numbered here as a flag.

---

## 1. What was read, what was used

| Input | Used for |
|---|---|
| `00-KS4-Lessons-Rebuild-Architecture.md` | The brief: ten laws, anatomy, four blocks, ladder, eight families, route tags, CFIFA amendment. |
| `council_bonding_review.md` | §4's lab catalogue chose each flagship; §8's defect list became flags 1–6. |
| `KS3 P8` + `Cfifa.dc.html` | Class vocabulary (`ks3-*`), rail, ladder anatomy, CFIFA behaviour, NOTES format. |
| `04-checked-science-source` | Extracted **by script** into `ks4-source.js` so no verbatim string was retyped. All route copies are present (`quiz.TH`, `.TF`, `.CH`, `.CF`). |
| `05-diagram-library` | House style ported to `ks4-diagrams.js`: cream #F3F0E7 plates, #2E5E45 labels, #1A1A1A strokes, #2E8B7F arrows, Georgia. Circuit engine lays loops with no crossings; AQA symbol sheet only; no motor symbol; the variable-resistor arrow passes right through the body. |

Old KS4 pages were not used as structure.

---

## 2. The KS4 page template (as built)

Fixed start → family-ordered middle → fixed end. Every lesson has, in order:

1. **Chrome** (`Ks4Chrome`): brand, breadcrumb (GCSE › subject › unit › lesson), progress rail (top bar under 1340 px, side rail above). Rail nodes tick **only** when the activity is complete (`KS4.rail(list, doneFlags, active)`).
2. **Big question header**: eyebrow `AQA <Subject> <spec> · <Family>`, h1, the big question, route badges, **Route selector** (review tool; the generator renders one route per URL and drops the selector), draft flag.
3. **Hook** (`ks3-hook` + `Ks4Choice`): phenomenon or exam scenario, 50–75 words, ending in a commitment. Replies are unscored words; a shared `reveal` follows the pick.
4. **Middle**: explainer (≤150 words) → act, repeated. One flagship, one or two mids, micro-widgets.
5. **Misconception** (`ks3-misconception`, amber): placed where the error is born. Usually a `Ks4Choice` spot-the-flaw with `right-word`/`wrong-word`; in four lessons it is an amber panel that opens inside the flagship at the moment of the wrong prediction.
6. **Command words**: 3–4 `dl` cards, lesson-specific definitions.
7. **Key fact**: one per lesson, card with accent offset shadow.
8. **Exam tip**: verbatim `KS4.tip(slug)`, in its fixed slot directly above the ladder.
9. **Exam ladder** (`Ks4Ladder`).
10. **Key note** (`Ks4KeyNote`): photographable card, 6 lines, cover-and-recall.
11. **Question bank** (`Ks4QuizBank`): the route's verbatim quiz copy. See §10.1.
12. **End matter** (`Ks4End`): previous/next, connects-to, Ask Mr Badmus AI, model-limits legal line. Score vs best lives in the ladder header (localStorage `ks4-best-<slug>`).

Body text: 73–202 words of explainer per lesson (measured by script), all hooks ≤ 75 words, so every first prediction lands inside ~150 words.

**Styling rules carried from KS3:** only the ladder marks right/wrong; benches reply in words ("Yes.", "Watch what happens instead."). Amber (`--ks3-alert-*`) is only ever the wrong idea, never the pupil. No punishment: wrong predictions still advance with the correction. Motion swaps instantly under `prefers-reduced-motion`. All controls are real buttons, selects, ranges or inputs: keyboard-complete, ≥44 px targets. Phone-first grids use `repeat(auto-fit, minmax(min(Npx,100%),1fr))`.

**Legibility.** No body text sits on a dark fill in light mode: KS3's dark hook, bench and key-note blocks are all light cards at KS4. Dark mode (`ks4-theme.css`, OS setting or `theme` prop) remaps the `--ks3-*` tokens; every `-text` token was chosen ≥4.5:1 on ground, card and its own tint. Ink-filled controls (`.ks3-reveal-btn`, check, retry) flip to light fills in dark mode, so `--ks3-on-dark` is remapped to #16120E there. That was a real defect found in testing. Figure plates stay cream in both modes, so diagram ink never changes.

---

## 3. The shared blocks (API for the generator)

All are child DCs. Props are kebab-case in templates.

| Block | Props | Emits |
|---|---|---|
| `Ks4Choice` | `eyebrow, command, prompt, options[{text, reply, correct?}], reveal, right-word, wrong-word, figure-svg` | `on-commit(i, option)`. Graded only if any option has `correct`; verdict words, never ticks. |
| `Ks4Sort` | `eyebrow, title, prompt, bins[{id,label}], items[{text, bin, why}], done-note` | `on-done({correct})`. Tap-card-then-tap-bin; no drag; cards shuffled by hash, so no word-shape leak. |
| `Ks4Chain` | `eyebrow, title, prompt, links[] (in order), herrings[{text, why}], scored, done-note` | `on-done({correct})` on first check. |
| `Ks4Write` | `id, eyebrow, command, marks, question, points[], levels[{label,text,max}]?, reject[], figure-svg, min-words` | `on-mark({awarded, marks, set})`. Write first; the mark scheme unlocks at `min-words` (default 12). |
| `Ks4Cfifa` | `examples[{tab, head, next?, steps[{letter,label,line,note}]}], questions[{tab, id, head, close, steps[{letter,label,placeholder,line}]}]` | `on-open(openedCount, total)`. |
| `Ks4Ladder` | `slug, rungs{r1,r2,r3,r4}` (§5) | `on-done(score)`. |
| `Ks4KeyNote` | `title, spec, lines[]` | — |
| `Ks4QuizBank` | `questions` (from `KS4.bank(slug, route)`), `route-label` | — |
| `Ks4End` | `subject, prev, next, connects[], tutor-line, legal` | — |
| `Ks4Chrome` | `subject, unit, title, rv` (from `KS4.rail`) | — |

`ks4-lib.js` (`window.KS4`): `route(cmp)` → `{route, isHigher, isTriple, notHigher, notTriple, routeOptions, onRoute}`; `find(slug, route, needle)` → verbatim quiz item, falling back to the TH copy; `bank(slug, route)`; `tip(slug)`; `fifas(slug)`; `cfifa(fifa, convertLine, note)` prepends a Convert step to a verbatim FIFA; `rail`, `observe`, `load`, `save`, `fig(svg, alt)`.

---

## 4. The four new KS4 blocks

**`required-practical`** (L14 is the reference build). A panel bordered in accent with: the AQA circuit drawn from the symbol engine; the method as 5 numbered steps; **Risks** in one sentence each; then the simulation, which takes readings with ±2.5% scatter and one planted anomaly (lamp, 5th reading, ×0.6). The pupil predicts the graph from **drawn** thumbnails (A–D), not described shapes, then collects at least 4 positive and 2 negative readings. A variables `Ks4Sort` follows, then data processing through CFIFA. The practical's typical 6-marker ("describe a method") is rung 4, level-marked. Header badge: `Required practical · <name>`. **Config:** `{components{label, sym, set[], rev[], ma, Imax, shape}, trueI(c,V), anomaly{comp, n, factor}}`.

**`equation`** (L12, L13, L14). A bordered panel. Only two chips exist: **Equation sheet** (on the card of an equation printed on the AQA sheet, e.g. V = I R in L13) and **Derived, not on any sheet** (a relationship built in the lesson, e.g. SA:V = 6 ÷ L in L12). Ofqual has confirmed equation sheets for GCSE Physics and Combined Science in 2025, 2026 and 2027, and all 35 physics equations are on them, so no physics equation is ever labelled "not on the sheet". The chips **Must recall · not on the equation sheet** and **Not on the equation sheet · work it out** are retired. CFIFA's Formula line copies the equation exactly as the sheet prints it. It holds the equation with named quantities and units, the rearranged forms, and a **Units first** card naming the conversion the lesson's questions use. It always sits directly before a `Ks4Cfifa`.

**`extended-response`** = `Ks4Write`. Mark scheme hidden until the pupil has written `min-words`. Point-marked (4-markers) or level-marked (6-markers: the pupil picks a level, which awards its top mark, then ticks indicative content). A **Do not accept** list is mined from the verbatim wrong-answer explanations. On the ladder it is rung 4; mid-lesson it appears once (L12 evaluate).

**`lesson-video`** = `Ks4Video`, one slot per lesson directly after the hook section. It appears only once the pupil has committed to the hook, and only if `KS4.VIDEOS[slug]` has a `src`, so the phenomenon always comes first. It is optional and never gates: no rail node, no score. It shows a poster frame with a play button (eyebrow "Watch the explanation", "Optional · <duration>"), then a native player with an English captions track (`.vtt`) and a folded **Read the transcript**. **Config:** `{ src, poster, captions, title, duration, transcript: [paragraphs] }`. The empty state renders nothing (all 14 lessons today).

**`exam-tip`**. Fixed slot directly above the ladder, text verbatim from source. Where the source has no tip (both physics lessons) the slot carries a drafted tip with a **Draft · awaiting approval** chip. See flag 11.

---

## 5. The exam ladder

Four rungs, one point each, **scored out of 4**. Each shows its command word and tariff chips.

| Rung | Form | Config | Scores when |
|---|---|---|---|
| 1 Recall | a verbatim quiz item (`KS4.find`), 1 mark | `{...item, command, marks:1, why}` | right option picked |
| 2 Apply | `kind:'calc'` (C choice + number + unit select), `'text'` (a typed formula), or `'data'` (one select per part, with a drawn data table) | `calc: convOptions, convAnswer, answer, tol, unit, units[]`; `text: accept[]`; `data: parts[{label, options, answer}]`; all: `prompt, figureSvg, right, wrong, model[]` | everything right on first check. Calc needs the right conversion **and** the unit. |
| 3 Explain | `Ks4Chain` with red herrings | `links[], herrings[{text, why}]` | chain right on first check |
| 4 Produce | `Ks4Write`, 4 or 6 marks | `question, points[], levels[]?, reject[]` | self-award ≥ half the marks |

**Retry my misses** resets only unscored rungs and keeps writing. The best score persists; the header shows the change against it. Multiple choice is only ever rung 1.

---

## 6. CFIFA

The one implementation is `Ks4Cfifa.dc.html`: worked examples revealed one step at a time behind **Nothing to convert / Convert first** tabs, then **Question 1 / Question 2** with no hint of which needs converting. Attempts are write-it-out: five inputs, *Check your working* once all five are filled, then the model lines with *I had this* self-ticks. Old FIFA steps are kept word for word by `KS4.cfifa()`, which puts a Convert line in front. Apply rungs use the same C-first logic in a lighter form (choose the conversion, then number and unit).

| Lesson | Worked 1 (nothing to convert) | Worked 2 (convert) | Q1 / Q2 |
|---|---|---|---|
| L12 nanoparticles | verbatim FIFA 1 (10 nm) | 0.02 µm → 20 nm (new) | verbatim FIFA 3 (rearrange) / 5 × 10⁻⁸ m → 50 nm (new) |
| L13 series & parallel | verbatim FIFA (3 Ω + 7 Ω, 20 V) | 250 mA → 0.25 A (new) | 5 Ω + 15 Ω, 10 V / 400 mA → 0.40 A (new) |
| L14 I–V | 4.0 V, 0.40 A (new) | 180 mA → 0.18 A (new) | 6.0 V, 0.25 A / 35 mA → 0.035 A (new) |

Every Convert-case answer note names the size of the error the unconverted number would give.

---

## 7. Lessons: family, line-up, instruments

State spaces are what a port must reproduce.

1. **Chemical bonds · Classify.** Hook (Na vs H with Cl) → **Bond decider** flagship (13-element tray; pair → predict ionic/covalent/metallic → chamber draws dot-and-cross, formula or electron sea; verdict names the specific wrong idea) → spot-the-flaw (ice melting ≠ weak bonds) → 8-card `Ks4Sort` → ladder (data table P/Q/R).
2. **Ionic bonding · Process.** Hook (Na in Cl₂) → **Call-each-step** stepper, Na+Cl then Mg+O. Three gates: who loses, what charge, what holds them. The confront "the bond is the transfer" opens at gate 3. → **Draw it yourself** dot-and-cross builder (Li+F, K+Cl, Ca+O, Mg+S; electrons-moved stepper, two charge selects; verdict per marking point) → **Formula forge** (Al₂O₃ worked, then Li₂S and Ca₃N₂; live charge meter; simplest-ratio check).
3. **Ionic compounds · Model.** Hook (cubic crystals) → **Lattice lens** (predict neighbour count, then 3 views: layer, 4 in-plane, +2 above and below = 6) → spot-the-flaw (NaCl is not a molecule) → **Deduce the formula** from drawn lattices (MgO, CaF₂, Li₂O, typed) → **Model limitations** sort against three drawn representations → ladder r4 evaluates a ball-and-stick model.
4. **Covalent bonding · Process.** Hook (H₂) → worked water in 3 steps with a bond-count gate → **Shared-pair builder** (HCl, Cl₂, O₂, N₂, NH₃, CH₄, CO₂; ± pairs per bond; per-atom "n of 8" chips; the correct build reveals the dot-and-cross) → weak-bond misconception sort.
5. **Metallic bonding · Model.** Hook (gold leaf) → spot-the-flaw ("bonded between atoms"), before the bench → **Electron-sea workbench**: battery (drift towards +), heat (vibration spreading), hammer (layer slides one place); predict each first → property-to-model sort.
6. **States of matter · Investigation.** Exam-scenario hook (stearic acid, water bath) → **Heating-curve investigation**: 21 readings at 30 s, scatter ±0.5 °C, anomaly at 2:00; synced particle view; pupil identifies the anomaly and reads MP (69 ± 1.5 °C) → spot-the-flaw (melting is physical) → **Critique the method** sort → **Higher**: limits of the model (verbatim TH7 as a check) → state-symbol sort (molten ≠ aq).
7. **Properties of ionic compounds · Contrast.** Hook (probes in salt) → **Side-by-side beakers**: solid (fixed lattice, bulb off) against molten or solution (ions drift to opposite electrodes, bulb lit); predict each → spot-the-flaw (electrons flow) → linked-comparison `Ks4Chain` → **Be the examiner** (mark a 1/3 answer) → ladder r4 6-mark banker №1.
8. **Properties of small molecules · Model.** Hook (steam bubble) → **Two-forces model**: 5 molecules × temperature slider; solid, liquid or gas from mp/bp; dotted forces vanish, thick bonds persist. First crossing of a bp is gated, and a wrong call opens the amber confront → **Rank it** (CH₄ < Cl₂ < Br₂ < I₂, molecules drawn to scale).
9. **Polymers · Classify.** Hook (ethene vs bag) → **Structure decider**: 8 drawn diagrams in two rounds; wrong "giant covalent" on a polymer gets a targeted trap reply → spot-the-flaw (polymer ≠ giant covalent) → **Triple**: addition-polymerisation chain builder (predict atoms lost; verbatim equation; thermosoftening and thermosetting).
10. **Giant covalent structures · Contrast.** Hook (drill bit and pencil) → **Diamond/graphite A/B**: per structure, predict bonds per atom (then highlight one atom's bonds), conductivity, hardness and melting point; the comparison table fills as you go → spot-the-flaw (graphite ≠ metal) → graphene/C₆₀/nanotube sort (**core**, untagged) → ladder r4 6-mark banker №2.
11. **Metals and alloys · Contrast.** Hook (24 vs 18 carat) → **Alloy mixer**: 0–4 larger atoms distort the layers; predict, then push (pure slides one place, alloy jams) → spot-the-flaw (metals must melt) → `Ks4Chain` banker №3 → **Triple**: engineer's pick (steel, aluminium alloy, bronze or brass).
12. **Nanoparticles · Quantitative (Triple).** Hook (ruby glass) → coarse/fine/nano size sort (unit conversion required) → **Cube splitter** (predict ×10; 1000→1 nm; SA, V and ratio tiles) → spot-the-flaw (same substance) → `equation` → CFIFA → evaluate `Ks4Write` (sun cream).
13. **Series and parallel · System.** Exam hook with drawn circuit → **Change one part** bench: 4 successive changes (R₂ → 20 Ω; rewire in parallel; add a branch; break a branch); predict both meters, then close the switch. The confront opens at "add a branch" → rules sort → `equation` → CFIFA → ladder r4 6-mark (household wiring).
14. **Resistors and I–V · Required practical.** Hook (bulb switch-on surge) → `required-practical` block (§4) → thermistor predict on a drawn circuit (the misconception) → variables sort → `equation` → CFIFA → ladder r4 6-mark method.

Two lessons in the same family never share a line-up: the Contrast lessons use beakers, A/B plus table, and a mixer.

---

## 8. Route tags: source of truth

Tags come from the AQA spec's HT and "chemistry only" labels only, not from the old pages' `higher` fields.

| Content | Tag | AQA source |
|---|---|---|
| Limitations of the particle model | `higher` | 8462/8464 5.2.2.1 (HT only) |
| Addition polymerisation | `triple` | 8462 4.7.3.1 (chemistry only) |
| Thermosoftening / thermosetting polymers | `triple` | 8462 4.10.4.3 (chemistry only) |
| Named alloys and their uses | `triple` | 8462 4.10.4.2 (chemistry only) |
| Nanoparticles, whole lesson | `triple` | 8462 4.2.4 (chemistry only) |
| Graphene, fullerenes, nanotubes | `base` | 5.2.3.3 (no HT marker) |
| Covalent dot-and-cross drawing | `base` | 5.2.1.4 (no HT marker) |
| Everything else in the pilot | `base` | — |

Badges: **Higher** (stretch tokens), **Triple** (blue tokens), **Higher · Triple** (both borders, one pill: not needed in this unit), **Required practical** (accent). Tagged blocks render inline, where the content belongs, wrapped in `sc-if isHigher/isTriple`, with a coloured border and the badge. The header adds "Contains Higher" or "Contains Triple". Key-note lines that carry tagged content are sliced off for routes without it.

---

## 9. Science flags

Each flag carries its AQA source. Verbatim items stay verbatim; Code fixes through DEPARTURES.

1. **Graphene and fullerenes are core, not Higher** (council defect 4). AQA 5.2.3.3 has no HT marker. They are taught untagged in L10; the Foundation quiz copies already test them (TF5–7).
2. **Nanoparticles spec number.** The pilot slug says 5.2.3.3, but nanoparticles are 8462 **4.2.4** (chemistry only); 5.2.3.3 is graphene and fullerenes. The page shows 4.2.4; the filename keeps the pilot slug so Code's mapping still resolves. Code to pick the permanent slug.
3. **Nanoparticles source gates the SA:V calculation as Higher.** 4.2.4.1 has no HT marker: it is Triple, both tiers. Rendered so.
4. **Nanoparticles quiz has 11 questions (TH), 10 (TF).** Kept verbatim.
5. **PM10 / PM2.5 and size ranges were missing from the source.** Added from 4.2.4.1 as new explainer text and a sort (sizes: dust 5 µm, soot 0.5 µm, TiO₂ 20 nm, Ag 10 nm, smoke 1 µm, sea salt 8 µm).
6. **Covalent source `higher` field treats dot-and-cross drawing as HT.** 5.2.1.4 lists the eight molecules as base content. It also mentions electronegativity and bond polarity, which are not in the GCSE spec: dropped.
7. **Addition polymerisation in Combined quiz copies.** CF/CH polymer copies include items such as "State the type of bond in a monomer that allows addition polymerisation" (CF9). That content is chemistry-only (4.7.3.1). Kept verbatim; Code to remove from Combined copies. PVC and nylon items (TH7) go beyond 5.2.2.5 as well.
8. **States of matter:** the TH copy's limitation items (TH7, TH11) are HT-only content. Code to confirm the CH copy carries them and the CF/TF copies do not.
9. **Charge size vs melting point** (MgO vs NaCl; TH5, TH7, TH10 in properties of ionic compounds) is not a 5.2.2.3 statement. Kept verbatim in the bank; not taught in the body.
10. **5.2.2.2 and 5.2.2.8 have no slots.** Folded into states of matter and metals and alloys.
11. **No examiner tip exists for either physics lesson** in the checked source. A tip was drafted in the fixed slot, chipped *Draft · awaiting approval*. Mide to approve or replace.
12. **Series-and-parallel source mis-describes RP15.** It gives "construct series and parallel circuits; measure I and V to verify rules". AQA Combined RP15 (Physics RP3) is *resistance*: length of wire, and resistors in series and parallel. L13 is not built as that practical; the RP remains unbuilt in this pilot.
13. **I–V practical numbering:** "RP16" is the Combined (8464) number; in Physics 8463 it is RP4. The badge names the practical, not a number.
14. **Physics quizzes are thin:** 2 questions, one route copy. The ladder's rungs 2–4 are therefore all new content.
15. **Parallel resistance is qualitative at GCSE** (6.2.2: explain, do not calculate). No parallel-resistance calculation appears anywhere.
16. **Option order.** In the source the correct option is always first and usually longest (council defect 6). `ks4-lib.js` re-orders options by a stable hash; no text is changed. If "verbatim" is meant to include order, turn the sort off in `KS4.item`.
17. **Data values used** (data-book, rounded): mp/bp in °C of H₂O 0/100, CH₄ −182/−161 (the −161 is the source's), Cl₂ −101/−34, Br₂ −7/59, I₂ 114/184; stearic acid mp 69; NaCl 801; tungsten >3400; iron bp ~2860. Alkane bp: pentane 36, hexane 69, heptane 98. Hardness vs carbon in iron (70/120/155/220) is **illustrative** and needs Code's check or a relabel as "model data".
18. **New worked examples and questions** (§6 table, the ladders, Be-the-Examiner in L7) are new science. All need the examiner pass.
19. **Metallic-bonding source key note mentions alloys**, which belong to 5.2.2.7. Moved there.
21. **R_total = R₁ + R₂ (L13) is not one of the 35 sheet equations.** It is a series rule. Its card carries no chip; only V = I R is chipped **Equation sheet**. Mide to confirm whether it gets a chip and which wording.
22. **Equation-sheet URLs are year-stamped.** The current AQA PDFs say "for use in June 2026 only". `KS4.EQ_BY_YEAR` holds one entry per year, and `EQ_YEAR` picks it. Each summer, add the new pair and move the year.
20. **Filament-lamp resistance.** 6.2.1.4 says only that "resistance increases as the temperature of the filament increases". The pages say no more; the ion-vibration story is deliberately absent.

---

## 10. Where the architecture met a real page

1. **Verbatim quizzes needed a home the anatomy did not have.** The ladder uses one item (rung 1), which leaves 9–11 verbatim questions per route, and they are the site's best teaching. They sit in a **Question bank** after the key note, inside the end matter, route-specific and unscored against the ladder. Retry-my-misses stays ladder-only.
2. **"Apply, units required" does not fit most bonding lessons.** Chemistry 5.2 has almost no calculations. Rung 2 became *deduce or use data*, where tariff and command word matter, not units: `kind:'text'` for formula deduction and `kind:'data'` for drawn tables. Units are enforced wherever a quantity exists (L12–L14).
3. **Self-marked rung scoring.** KS3's "all criteria ticked" is too harsh for 6-markers, so rung 4 scores at ≥ half the tariff (a level pick awards the top of that level).
4. **The council's "Teach me / Labs / Test me" chooser was not built.** The progress rail does the same job with fewer controls.
5. **Misconception placement.** Where the error is born inside an instrument (L2 gate 3, L8 first boiling, L13 add a branch), the confrontation is an amber panel **inside** the flagship, not a separate block.
6. **The route selector is a review affordance.** The generator should render a single route per URL and drop the control.
7. **"No text on dark fills" retired KS3's dark hook, bench and key-note blocks.** KS4 benches are light cards with cream figure plates.
8. **Physics exam tips** — see flag 11.
9. **The ladder's data rung uses option buttons, not `<select>`.** Native selects cannot wrap, so long options (metallic bonding, metals and alloys) pushed the page to 434–474 px at 390 px. The rung now uses the same wrapping pick-buttons as the Convert step, at every width. This is fixed once in `Ks4Ladder`.
10. **Comparison tables are rows of cards, not `<table>`.** Two reasons. A 3-column table cannot fit at 360 px. And an `<sc-for>` inside `<tbody>` is moved out of the table by the HTML parser, which is why L10 logged `{{ r.label }}`, `{{ r.d }}` and `{{ r.g }}` as unresolved. L10's diamond/graphite comparison now puts the row label above two labelled cells that wrap under 480 px (ARIA table roles kept).
11. **Circuit benches draw the switch that the button names.** In L13 an AQA open switch sits beside the battery. It closes when **Close the switch** is pressed, and it is drawn closed in the Before circuit.
12. **Heat source drawn.** In L6 the particle view has a flame under the container. It is lit and flickering while heating; before the start it shows as a dashed, unlit outline (static with reduced motion). The alt text says which.
13. **Video after the commitment.** See `lesson-video` in §4. Putting it after the hook's first prediction keeps "phenomenon first" and makes watching a choice, not a gate.

---

## 11. Build notes for Code

- `ks4-source.js` is generated; never hand-edit it. Regenerate from the source folder and diff.
- All animation reads `prefers-reduced-motion` once on mount and swaps to the end state. Timed simulations (L6) use wall-clock time, not tick counts, so throttled tabs still finish.
- Diagrams are SVG strings from `ks4-diagrams.js`, mounted through `KS4.fig(svg, alt)` with `role="img"` and a state-specific `aria-label`.
- Parity checks at 1280 / 1340 / 820 / 390 px. The side rail appears at ≥1340 px.


## CFIFA correction (Mide, 25 Sep 2026)

- **Formula** is written exactly as it appears on the equation sheet (e.g. `V = I R`), never pre-rearranged.
- **Insert** puts the given values into that form (e.g. `4.0 = 0.40 × R`).
- **Fine-tune** is where the equation is rearranged for the unknown and worked out. Where the unknown is already the subject, the line says "Nothing to rearrange".
- Applied to L12, L13, L14. The verbatim source FIFAs for L12 (FIFA 1, FIFA 3) and L13 (series FIFA) rearranged inside the Formula step; they are now restructured to this rule on Mide's instruction, so they are no longer word for word.
- L14: "Must recall · not on the equation sheet" chip removed. V = I R is on the sheet.
- `.ks3-commit` prompts now render in `--ks3-ink` (amber was unreadable on light grounds; ink flips in dark mode).

## Equation sheet link (every physics lesson)

Under the route selector (URLs now the June 2026 PDFs, see flag 22): **View the full equation sheet**, opens AQA's PDF in a new tab. Combined routes link the Combined Science Trilogy/Synergy sheet (8464/8465); Triple routes link the GCSE Physics sheet (8463). URLs live once in `ks4-lib.js` (`KS4.EQ`); `KS4.route()` returns `eqSheetHref` / `eqSheetLabel`. Both current PDFs say "for use in June 2025 only", so check the URLs each exam year.

## Review fixes (25 Sep 2026)

1. Equation chips: removed "Must recall · not on the equation sheet" from L13; V = I R is now chipped **Equation sheet**. L12's chip is now **Derived, not on any sheet**. §4 and flag 21.
2. `KS4.EQ` now points at the June 2026 PDFs through `EQ_BY_YEAR` / `EQ_YEAR`. Flag 22.
3. Ladder data rung: selects replaced by wrapping buttons. §10.9.
4. L10 table rebuilt as card rows; the unresolved-hole warnings are gone. §10.10.
5. L13 bench: switch drawn, open to closed. §10.11.
6. `Ks4Video` slot added to all 14 lessons, empty for now. §4, §10.13.
7. L6: flame under the particle container. §10.12.
