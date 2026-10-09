# KS4 batch 5: 15 lessons

Written from `docs/ks4/packs/batch-5/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/, 05-diagram-library/README.md), main at 4d4864f, 4 Oct 2026. The three updates in the batch-5 prompt override the pack. No lesson text comes from old site data: these pages don't load `ks4-source.js`. Every quiz item is written into its lesson, either verbatim from the pack, re-authored as a flag allows, or new.

## Files

One runnable `.dc.html` per lesson, named `ks4-<subject>-<spec>-<slug>` as in batch 4. The spec number is the corrected AQA reference from FLAGS.

| # | Lesson | File | Routes |
|---|---|---|---|
| 1 | Land use and peat bogs | ks4-biology-4.7.3.3-land-use | CF CH TF TH |
| 2 | Metals and non-metals | ks4-chemistry-5.1.2.3-metals-non-metals | CF CH TF TH |
| 3 | Reactivity of metals | ks4-chemistry-5.4.1.1-reactivity-series | CF CH TF TH · Higher layer CH TH |
| 4 | Energy resources | ks4-physics-6.1.3-energy-resources | CF CH TF TH |
| 5 | The structure of an atom | ks4-physics-6.4.1.1-structure-of-atom | CF CH TF TH |
| 6 | Plant tissues and organs | ks4-biology-4.2.3.1-plant-tissues | CF CH TF TH |
| 7 | Waste management and pollution | ks4-biology-4.7.3.2-waste-management | CF CH TF TH |
| 8 | Using the Earth's resources | ks4-chemistry-5.10.1.1-earths-resources | CF CH TF TH |
| 9 | Development of the model of the atom | ks4-physics-6.4.1.3-development-atomic-model | CF CH TF TH |
| 10 | Global warming and ecosystems | ks4-biology-4.7.3.5-global-warming | CF CH TF TH |
| 11 | Group 0 | ks4-chemistry-5.1.2.4-group-0 | CF CH TF TH |
| 12 | Extraction of metals | ks4-chemistry-5.4.1.3-extraction-of-metals | CF CH TF TH |
| 13 | Potable water | ks4-chemistry-5.10.1.2-potable-water | CF CH TF TH · RP13 / RP8 on all four |
| 14 | Radioactive decay | ks4-physics-6.4.2.1-radioactive-decay | CF CH TF TH · Triple layer TF TH |
| 15 | Red-shift and the Big Bang | ks4-physics-4.8.2-red-shift-big-bang | TF TH only |

Shared blocks sit in the same folder so each lesson runs on its own. They are copied unchanged from the batch-4 delivery (single-chip Ks4Triangle, the triangle under Ks4Cfifa's Formula line, Ks4QuizBank at five, the nowrap fixes): Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, Ks4Chain, Ks4Write, Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, plus ks4-lib.js, ks4-diagrams.js, ks4-theme.css and support.js.

## Page order (every lesson)

Header (AQA ref, routes, route picker) → Start here (`Ks4Guess`) → video slot → teaching sections, each with its figure and one interactive (Higher / Triple layers inside them as `sc-if` on `isHigher` / `isTriple`) → equation block (`Ks4Triangle`), CFIFA (`Ks4Cfifa`) and Step 1 / Step 2 (`Ks4Steps`) where the lesson calculates → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. No examiner tip is shown: none is approved. No physics page in this batch has an equation, so no page carries the equation-sheet link or sheet panel.

## Changes to shared blocks

None. All blocks are the batch-4 copies, byte for byte.

## Rules 1–4 in this batch

- **Rule 1.** Every opener is the pack's access note as "If you had to guess, … ?" with two options and a reply to each. Titles and scenes describe the situation without the answer (e.g. "A field at the edge of town", not "Building destroys habitats").
- **Rule 2.** One triangle in the batch: concentration = mass ÷ volume (potable water), `source: 'none'`, so no chip. It appears in the equation block, under CFIFA's Formula line, and under the worked Step 2's Formula line. Chemistry has no sheet panel. "Learn this one" appears nowhere. Earth's resources' years-left division is written out as "a data step, not an AQA equation", with no triangle (the pack says none is needed): see 8.4.
- **Rule 3.** Two calculations. Potable water chains (mass by subtraction, then concentration): CFIFA on single steps, a worked `Ks4Steps`, then an attempt, all before the ladder's chained item. Earth's resources (reserves ÷ use per year): two worked CFIFA examples and two attempts before the ladder item. Every other teaching step is taught before it is tested (e.g. extraction: copper worked, then zinc and iron tagged).
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route; rung 4 is one 4- or 6-mark answer. Practice set: five questions per route.

## Quiz items

| Lesson | Verbatim | Re-authored (flag allows) | New |
|---|---|---|---|
| 1 Land use | — | q1, q2 (LAND-USE-F1, F2: explanations re-paired, opt 3 written) | 3 |
| 2 Metals/non-metals | q1 q2 | — | 3 |
| 3 Reactivity | q1 | — (q2 dropped, F1) | base: 4 · CH TH: 2 base + 2 ionic-equation |
| 4 Energy resources | q1 q2 | — | 3 |
| 5 Structure of atom | q2 | q1 (F1 wx3) | 3 |
| 6 Plant tissues | q1 q2 q3 | — | 2, incl. meristem |
| 7 Waste management | q1 | q2 (F2, F4 explanations) | 3 |
| 8 Earth's resources | q1 q2 | — | 3, incl. order of magnitude |
| 9 Dev. of atomic model | q1 q2 | — | 3, incl. sequence with protons |
| 10 Global warming | — | q1, q2 (F1, F2) | 3 |
| 11 Group 0 | q1 q2 | — | 3 |
| 12 Extraction | q1 q2 | — | 3 |
| 13 Potable water | q1 | — (q2 off-spec, F6) | 4 |
| 14 Radioactive decay | — | q1 (F1 wx1), q2 (F2 stem, wx1) | 3 |
| 15 Red-shift | q1 | — (q2 dropped, F4) | 4 |

Options are shuffled by `KS4.item()`, as before.

## Science flags

**G · Global**
- G1. Fonts: arrows (→), subscripts (₂), superscripts (²⁺, ⁻¹⁰) and Δ inside quiz and ladder text are plain characters and render in the fallback font. In page markup, arrows are inline SVG and sub/superscripts use `<sub>`/`<sup>`. Verbatim items keep their own glyphs.
- G2. All numbers in teaching models are round teaching figures, labelled on the page: waste bars (7), electricity mix of a made-up country (4), reserves and use (8), water samples (13), count-rates (14), spectra and galaxy figures (15).
- G3. Prev/next links follow subject order inside this batch; connects links into batch 4 use `../KS4 Batch 4/` paths. Code to rewire to the live order.
- G4. Drawings are mine, in the ks4-diagrams style: the figlib functions the diagram README names were not ported (they are Python). Leaf section, reactivity ladder, penetration bench, spectra and scattering figures are schematic.

**1 · Land use**
- 1.1 Conflict taught by name, both sides (F3); peat-free compost as the answer.
- 1.2 Drained peat "no longer waterlogged, so it decays" — base context per the examiner's R3, not the triple decay factors.
- 1.3 Rung 4 is a 6-mark Evaluate.

**2 · Metals and non-metals**
- 2.1 Spec definition and outer-electron link on every route (F1); "do not form positive ions" leads (F2); "most" non-metals low melting point (F3); graphite/graphene re-cut (F4); position wording from the spec (F5).
- 2.2 Element picker covers Z = 1–20. Hydrogen is described as "usually shares its electron"; its H⁺ ions in acids are not raised. B and Si are shaded non-metal.
- 2.3 Test-bench Sample A is identified as sulfur in the reply.

**3 · Reactivity of metals**
- 3.1 Tendency to form positive ions is base, every route, no "ionisation energy" (F2). Oxidation as gain of oxygen panel (F3).
- 3.2 All eight spec metals, room temperature, no steam (F4, F5); potassium re-cut (F8). K, Na, Li, Ca with acid are shown as "not done: too violent; its place comes from the water test" — my wording, not the pack's. Code to check.
- 3.3 Ladder shows K Na Li Ca Mg Al (C) Zn Fe (H) Cu Ag Au; Sn, Pb and Pt left off.
- 3.4 Hydrogen reducing oxides dropped (F7). Higher layer (CH TH): Fe + Cu²⁺, oxidised/reduced in electrons (F6).

**4 · Energy resources**
- 4.1 Reliability for every resource (F4): tides "reliable" because predictable; Sun, wind, waves weather-dependent. Geothermal re-cut (F5). No generation mechanism (F2). Sun-tracing line dropped (F1).
- 4.2 Trends chunk (F3) uses a made-up country (coal 35% → 2%, wind and solar 1% → 30%), labelled as not real data. Code may swap in real UK figures. Limits-of-science line added (F3).
- 4.3 Tidal-barrage and wave-machine impacts are my wording from the source's "disrupts marine ecosystems".

**5 · Structure of an atom**
- 5.1 "Relative mass / relative charge", no amu (F2); "less than 1/10 000" throughout (F3). Football analogy says "at least 3 km".
- 5.2 Shell capacities not taught (F4); the build figure fills 2, 8, 8 visually only.
- 5.3 Rung 2's key is 1 × 10⁻¹⁵ m (the only option under 1/10 000 of 1 × 10⁻¹⁰ m).

**6 · Plant tissues**
- 6.1 Badge 4.2.3.1 (F4). Meristem taught and practised (F1). No Higher layer, no companion cells, ATP, cohesion-tension or potometer (F2, F3). Stomata "mostly" on the lower surface (F5).
- 6.2 Guard-cell turgor mechanism left out; transpiration and translocation are a one-line pointer.

**7 · Waste management**
- 7.1 Biodiversity is the spec definition (F1); "can reduce biodiversity" (F3). Eutrophication neither taught nor drawn (F2).
- 7.2 "Acid rain falling on land and into lakes is one way" (air-pollution effect) is my wording. Code to check.

**8 · Earth's resources**
- 8.1 No Higher block, atom economy, green chemistry or LCA (F1, F2, F6, F9). Natural → agricultural/synthetic pairs taught as the Sort (F3). "About 95% less energy than extracting new aluminium" in teaching text (F8).
- 8.2 Data skills (F4): qualitative data cards; CFIFA 8 × 10⁹ ÷ 4 × 10⁷ = 200 years; 1.2 × 10⁹ ÷ 4 × 10⁷ = 30 years; attempts 200 and 300 years; ladder 6 × 10¹⁰ ÷ 2 × 10⁸ = 300 years; rung 4 compares 200 and 10 years.
- 8.3 The "Chemistry plays an important role in improving agricultural and industrial processes…" line is the spec sentence as I know it; it is not in the pack. Code to confirm against 5.10.1.1.
- 8.4 The years-left division gets no triangle, per the pack. If Mide wants one for consistency with rule 2, it is a one-object change.

**9 · Development of the atomic model**
- 9.1 Proton step in the timeline and in practice (F1). Conclusion names mass and charge (F2). Bohr limited to the spec sentence (F4).
- 9.2 No dates in my text; verbatim q2's explanation carries 1904/1909.

**10 · Global warming**
- 10.1 Land ice only (F4); consensus line (F3). No distribution data evaluation (F5).
- 10.2 The warming map is a model with invented species and four unnumbered steps.

**11 · Group 0**
- 11.1 Trend in spec words with relative atomic mass, no "London dispersion" in my text (F1, F2); verbatim q2 keeps it, as F1 allows.
- 11.2 Radon predicted from He–Xe (F3), revealed as −62 °C. Relative atomic masses 4, 20, 40, 84, 131, 222 are standard values, not in the pack.

**12 · Extraction of metals**
- 12.1 Balanced equations only (F1); the frozen ZnO equation appears nowhere, not even as a distractor. No half equations or cell detail (F2, F7). No Higher block (F6).
- 12.2 Rung 4 is the given-information item (F4): a blast furnace described as iron oxide heated with coke "almost pure carbon", no CO step (F5).

**13 · Potable water**
- 13.1 RP badged "Combined RP13 · Chemistry RP8" on all four routes, in the spec's words (F1). No flame or precipitation tests, no filtering in the RP.
- 13.2 Potable steps with reasons (F4); desalination base (F5); no health claims (F8). Sewage: screening and grit removal, sedimentation, anaerobic digestion of sludge, aerobic treatment of effluent; no chlorination (F2, F7). Relative ease taught and sorted (F3).
- 13.3 Chain values: worked 48.71 − 48.62 = 0.09 g, 0.09 ÷ 0.050 = 1.8 g/dm³; attempt 0.12 g, 4.8 g/dm³; ladder 1.5 and 0.8 g/dm³. Sample values (tap pH 7, river pH 6, sea pH 8 and 35 g/dm³) are teaching figures.

**14 · Radioactive decay**
- 14.1 Activity vs count-rate taught (F2). Four emissions, beta's origin (F3). Medical uses are a Triple layer (F4). No inverse-square law (F5); beta "up to about a metre", no amu (F6).
- 14.2 "Radiation goes out in all directions" as the reason count-rate is below activity is my wording. Code to check.

**15 · Red-shift and the Big Bang**
- 15.1 Badge 8463 4.8.2; TF TH only; no Higher layer (F1, F3). No Hubble equation, triangle or CFIFA (F2). No CMBR anywhere (F4).
- 15.2 1998 supernovae, dark mass and dark energy added (F5). Big Bang in spec words (F6); "moving away because space itself is expanding, and we are not at the centre" (F7).

## Not done / for Code

- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden.
- No examiner tips: none approved.
- Dark mode uses the existing remap; SVG plates stay cream.
