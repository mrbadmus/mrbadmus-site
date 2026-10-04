# Batch 4 — science log (running)

Every science decision made while porting Design's batch 4, with the source line.
Design's lesson files stay byte-identical on disk (`docs/ks4/design-reference/batch-4/`,
`MD5SUMS`). Changes are NAMED rulings in `ks4_batch_rulings.py` (`SCIENCE`), applied at
compile time, each failing loud if its target text moves. "Pack" = `docs/ks4/packs/batch-4/`
(`FLAGS.md`, `04-checked-science-source/`).

## Stage 2a — efficiency, infrared-black-bodies, thermal-conductivity, uses-em-waves, periodic-table, development-periodic-table, atmospheric-pollutants

### Mide's rulings (TASK-AA.md)

| Ruling | Decision | What changed | Source |
|---|---|---|---|
| 5.2 infrared glow colours | Applied as B4-IRB-GLOW-1..4 | Slider stops now 500, 700, 1000, 1500, 2500, 3500, 5500 °C (a 700 °C stop added, because none of Design's six stops could honestly read "dull red"). Labels: 500 no visible glow; 700 dull red; 1000 orange; 1500 yellow-white; 2500 white; 3500 white (peak nearly visible); 5500 Sun. Default stop is now 1000 °C. Planck function, peak formula (2898 µm·K ÷ T) and every peak value untouched. Design's glow panel has no colour swatches (words only), so there were no swatches to change. | Mide, 4 Oct; FLAGS IRB-F1/F2 |
| G1 biology no chip | No effect in 2a (no biology equation page in this stage) | — | Mide |
| G2 fonts / subscripts | None of these 7 lessons contains a Unicode subscript, Δ, θ or arrow (chemistry text is written out in words; the two `<sub>` formulas are real tags). Nothing to convert. Needed in 2b (blood: one `₂`; transport: Δ and →). | grep of the 7 files | Mide |
| 12.2 arsenic beside the gap below silicon | Kept as drawn. Correct history: after zinc the next known element by weight was arsenic, which behaves like phosphorus. | none | Mide |
| 12.3 no Newlands octaves table | None drawn or added. | none | Mide |
| 13.3 UV lamp reason | Kept: "a coating inside the lamp absorbs the ultraviolet and gives out visible light" (fluorescence). Correct. | none | Mide |

### Numbered flags

**Efficiency (NOTES §4; FLAGS EFFICIENCY-F1..F3)** — no change.
- F1: lubrication and insulation base; "ways to increase efficiency" (lubricate, streamline, insulate, swap component, regenerative braking) is a CH/TH-only block. Verified in the built pages (shows on CH TH, absent on CF TF).
- F2: LED preset is 40% (realistic), filament lamp 10%.
- F3: "× 100" is a conversion line, never a triangle. Both equation chips read "On the sheet"; no "Learn this one".
- Every number recomputed, all correct: 7000÷20000 = 0.35; 1800÷2500 = 0.72 (1800÷2.5 = 720 is the flagged wrong way); 0.40×60 = 24 W; 900÷1200 = 0.75 (900÷1.2 = 750); 0.90×5000 = 4500 J (90×5000 = 450 000); worked 0.80×2000 = 1600, 2000−1600 = 400 J; attempt 0.35×60 000 = 21 000, 60 000−21 000 = 39 000 J; ladder 3÷60 = 0.05, 0.65×4000 = 2600 J; rung 4 6÷40 = 0.15, 3÷8 = 0.375, wasted 34 W and 5 W; think-again 150÷200 = 0.75 (150÷50 = 3, 200÷150 = 1.33); quiz 0.6×500 = 300 → waste 200 (500÷0.6 = 833); LED 1 J/s vs bulb 90 J/s → 89; 0.85×2000 = 1700 (170 000, 2353, 300); Sankey 5÷20 = 0.25 (4, 0.33, 15).

**Infrared (NOTES §5; IRB-F1..F8)**
- F1/F2/F3: Design's text is already re-cut (peak stays in the infrared until about 3500 °C; "hotter: more at every wavelength, distribution shifts to shorter wavelengths"; q1 re-authored with correct wx3). Verified.
- F4: one Sun figure ("about 5500 °C", peak 0.50 µm visible). Kept.
- F5: balance + Earth's temperature in the TH-only layer; "reflection of radiation into space". Verified.
- F6: no RP block; matt black recalled as a bridge. F7: no star colours / telescopes. F8: spec label "4.6.3.1–4.6.3.2 · Physics only". Verified.
- Numbers: peaks 2898÷T(K): 700 °C → 3.0 µm, 1000 → 2.3, 1500 → 1.6, 2500 → 1.0, 3500 → 0.77 (just infrared), 5500 → 0.50 (visible). All match the displayed text.
- B4-IRB-CHIP: Design's renderVals returns a fresh object, so the one route chip had no words/menu. Fixed by passing `routeWords` / `routeSwitchOptions`. `port_lesson` now fails loudly if a lesson neither spreads the route helper nor passes them (biodiversity has the same pattern: needed in 2b).
- Pre-existing, left: at 500 °C the peak (3.7 µm) is off the right edge of the 0–3 µm axis; the dashed peak line is clipped. Design's drawing; the peak text is right.

**Thermal conductivity (NOTES §9; TC-F1..F7)**
- F1: all four routes, RP2 layer on TF TH only (shown by `isTriple`). F2: no shielding. F3: no higher layer, no U-values, no equation. F4: RP2 compares the temperature drop over a fixed time (fair test); the quiz replacement is TF TH only. F5: thickness part in RP2. F6: spec wording, no definition, no unit. F7: cavity insulation gives both reasons. All verified in the page.
- **B4-TC-VERDICT (new error found).** The wall model says stone conducts 3× better than the block and "thick" is 3× "thin". When a change cancels (stone-thick ↔ block-thin) the verdict read "the material conducts about three times better but the wall is a third as thick, or the reverse", which describes a ninefold change, not a cancel. Replaced with "One change raises the rate threefold and the other lowers it threefold, so they cancel out."
- Quiz: 4 base + 1 route item = 5 on every route.

**Uses of EM waves (NOTES §13; UEM-F1..F6)**
- F1: microwaves absorbed by water molecules, outer layers, inside by conduction (CH TH layer). F5: all six spec pairs present, sun tanning linked to UV risk. F6: "transfers energy to the thermal store". F3: base = wave ↔ use; reasons CH TH only. Verified.
- F4/F2 — **soft point, pack allows it.** The CH TH quiz keeps q1 ("microwaves pass through the ionosphere; radio waves reflect off it") and q2 (UV sterilises medical equipment by damaging DNA). The pack says both are usable on CH TH. Neither the ionosphere nor UV sterilisation is on the spec, and "radio waves reflect off the ionosphere" is true only of long/medium/short-wave radio, not FM or TV. Left as the pack ruled; flagged for Mide because an examiner might prefer the "pass through the atmosphere" wording in the key.
- Cosmetic, left: in the satellite figure the word "satellite" and the "microwaves pass through the atmosphere" label cross the arrows.

**Periodic table (NOTES §8; PERIODIC-TABLE-F1..F6)**
- F1: transition metals dropped. Design kept a one-line pointer ("have their own lesson on the Triple route"). **B4-PT-F1** shows that pointer on TF TH only (it is a pointer to a page Combined pupils cannot reach).
- F2: Group 1 and 7 trends on every route in spec language, no "ionisation energy". F3: Group 0 "unreactive all the way down". F5: "period = occupied shells". F6: q1 usable. All verified.
- Builder checked: z = 1–20 gives the right shells (2.8.8.2 for Ca) and groups; neon outer 8; 2.8.2 → Period 3 Group 2; 2.8.5 → Period 3 Group 5.

**Development of the periodic table (NOTES §12; DEVELOPMENT-PERIODIC-TABLE-F1..F3)**
- F1: q1 re-authored (no wrong wx3). F2: isotope step taught on every route (Te 52 p / 127.6; I 53 p / 126.9; Ar 18 p / 39.9; K 19 p / 39.1 — all correct). Verified.
- **B4-DPT-F3.** "Argon and potassium, found later, show the same thing" implied potassium was found later; potassium was known from 1807, argon from 1894. Re-cut to "Argon, found later, and potassium show the same thing."

**Atmospheric pollutants (NOTES §3; ATMOSPHERIC-POLLUTANTS-F1..F8)**
- F1: q1 replaced with CO "toxic, colourless, odourless". F3: no Higher layer. F4/F6/F7/F8: converters, pH multiplier, smog, acid equations left out; particulates "solid particles and unburned hydrocarbons". F5: predict-the-products taught, worked, practised (4 cases checked against `expect()`).
- **B4-AP-STOVE.** A wrong reply said a camping stove "is not hot enough" for oxides of nitrogen (a flame does make some). Re-cut: oxides of nitrogen are linked to the high temperatures in engines; here the danger is the oxygen running out.
- **B4-AP-F2.** A quiz distractor named "The catalytic converter" (off-spec, F2/F8: never in practice). Replaced with "The engine oil".
- Accepted simplification, as Design flagged (NOTES 3.2): the predictor treats "CO and soot" as arriving together under limited oxygen; the pack says "CO and/or C". A pupil who ticks only CO is shown "Here is the full set", not marked as a wrong idea.
- Equations balanced: S + O₂ → SO₂; N₂ + O₂ → 2NO.

### Rules 1–4 (structural, all 26 pages)
- Rule 1: each hook has exactly two options and a guess line beginning "If you had to guess, …" with its own question (7 of 7).
- Rule 2: efficiency shows two triangles on every route, both "On the sheet" (rendered text count = 2), none "Learn this one". Other 6 lessons have no equation.
- Rule 3: efficiency has a worked Steps then an attempt Steps before the ladder.
- Rule 4: ladder 2·2·2·1 in the source of every lesson (13 of 13 checked), no "Shape:" alert on any page, before or after clicking every control; five quiz questions on every page (26 of 26).

### Not changed, decided
- review_state stays `draft` for every lesson until Mide says.
- `ks4_science_rulings` (the pilot's 101-row table) is not used for batch 4; its `--batch` check reports 0 rows by design.


## Stage 2b — heart-blood-vessels, water-cycle, transport-in-cells, blood, coronary-heart-disease, biodiversity

### Mide's rulings

| Ruling | Decision | What changed |
|---|---|---|
| G1 biology equations | Applied as drawn: `source: 'none'`. Rendered check on all 24 pages: no "On the sheet" chip, "Written out" appears (heart 2, transport 3). | none |
| G2 subscripts | Display-time conversion in a batch-4-only asset, `shared/ks4-ext-batch-4.js` (source `ks4_lessons/batch4_ext.js`, named by `EXT_SRC` in `batch_4.py`). It turns a run of U+2080..2089 into `<sub>2</sub>` in the live DOM and keeps the runtime's own text node as the first fragment, so in-place patching still works. Proved on blood: a wrong answer to "Which substance does plasma NOT transport?" shows CO<sub>2</sub>, no raw subscript left, and it survives "Retry my misses". Authored text and the shared runtime are untouched. | new asset only |
| G2 Δ and → | Left as the pilot leaves them (system fallback font). Δ appears in transport's `% change` triangle, → in transport and heart text. Not clean to subset without touching shared fonts. | none |
| 2.2 snow runoff | Fine, kept (water cycle, step 7). | none |
| 11.2 biodiversity sort | **B4-BIO-SORT-1..3.** The three hedgerow / breeding-programme / field-margin cards are gone. One bin would be a degenerate sort, so the bins are now the three threats (Waste, Deforestation, Global warming) and the six cards are examples of each, worded from Design's own "Human activity" section. Title, prompt and done-note re-cut to match. The quiz and rung 1 still name hedgerows, breeding programmes and field margins as wrong options for "which reduces biodiversity" (correct, and consistent with the sibling lesson); left. | `biodiversity` |

### Numbered flags

**1 Heart and blood vessels (HBV-F1..F11)** — all verified as drawn, no change. Pacemakers (natural and artificial) base on all routes (F2, F4); lungs taught and practised (F3); valves unnamed and at the exits of the ventricles (F7, F8); pressure falls arteries > capillaries > veins (F1); q4 re-authored with the pack's own wx (F5); q3 kept (F10); badge 4.2.2.2 (F11). Cardiac "never tires" not used (F9).
- Numbers recomputed, all correct: 6.0 ÷ 1.5 = 4.0 dm³/min; 21 beats ÷ 0.25 min = 84 bpm (21 ÷ 15 = 1.4 is the flagged wrong way); 1500 cm³ = 1.5 dm³, 1.5 ÷ 0.30 = 5.0 dm³/min; 36 ÷ 0.5 = 72 (36 ÷ 30 = 1.2); 2400 cm³ = 2.4 dm³, 2.4 ÷ 4.0 = 0.60 dm³/min (600 cm³/min in the wrong unit); ladder 18 ÷ 0.25 = 72; 900 cm³ = 0.90 dm³, 0.90 ÷ 0.20 = 4.5 dm³/min.

**2 Water cycle (WATER-CYCLE-F1..F5)** — all verified, no change. 4.7.2.2 (F1); fresh water taught as its own section and in practice (F2); "most reactions in cells take place in solution" not claimed as "the solvent for all" (F3); roots sentence dropped (F4); transpiration, groundwater and "salt stays here" are in the figure and the walk-through (F5). Cloud = droplets, not vapour (correct). No numbers.

**6 Transport in cells (TRANSPORT-IN-CELLS-F1..F10)** — all verified, no change. Urea diffusion ends at the blood plasma (F1); no Higher layer, % change, isotonic reading and SA:V on every route (F2); route-aware label "Required practical 3" on TF TH, "2" on CF CH, in the chip, the RP heading and the key note (F3); q3 re-authored on "less energy" (F4); energy "from respiration", no carrier proteins (F5); crossing at 0 % read as "same concentration as the cell contents", never "water potential" (F6); SA:V three-step worked then attempt before the ladder (F7); gills and leaves (F8); rate of water uptake (F9); "partially permeable" used in the text (F10). The verbatim quiz items still say "ATP" and "selectively permeable", which F10 allows.
- Numbers recomputed, all correct: (3.4 − 4.0) ÷ 4.0 × 100 = −15 %; 2800 mg = 2.80 g, 0.30 ÷ 2.50 × 100 = +12 %; 0.60 g ÷ 120 min = 0.005 g/min; (2.8 − 3.2) ÷ 3.2 × 100 = −12.5 %; 0.90 g ÷ 90 min = 0.01 g/min (0.6 g/h if left in hours); ladder (2.3 − 2.0) ÷ 2.0 × 100 = +15 %; SA:V 1 cm 6 : 1, 2 cm 24 ÷ 8 = 3 : 1, 3 cm 54 ÷ 27 = 2 : 1, 4 cm 96 ÷ 64 = 1.5 : 1. The graph's points (0.2, +10) and (0.4, −2) cross zero at about 0.37 mol/dm³, as labelled.

**7 Blood (BLD-F1..F7)** — all verified. Three white-cell functions including antitoxins (F1); recognition from a drawn smear (F2); biconcave line re-cut to "large surface area for oxygen" (F3); no spleen, fibrin or memory cells in the teaching (F4, F6); badge 4.2.2.3 (F7). q1 kept with its original wx3 (F5 says usable).
- Accepted as the pack ruled: the verbatim platelet item's key says "trigger fibrin mesh formation" (F6 says fibrin is context only). The keyed idea is "blood clotting", so any pupil who knows only that is right.
- The one `₂` (plasma-carbon dioxide explanation, which also says "bicarbonate", F6 context) is shown as CO<sub>2</sub> by the ext asset.

**10 Coronary heart disease (CHD-F1..F8)** — all verified, no change. All base on all four routes (F1); faulty valves (F2), artificial hearts and heart-and-lungs transplant (F3), bypass left out (F4); "risk rises with age because fatty material has longer to build up" (F5); menopause line dropped (F6); three-patient choice and a 6-mark Evaluate item (F7); badge 4.2.2.4 (F8). No numbers.

**11 Biodiversity (BIODIVERSITY-F1..F9)** — all verified. Spec definition only, with plants and microorganisms counting (F1, F2, F3); q2 (Svalbard) and the genetic-diversity question not used (F4, F6); no Higher layer (F5); stability taught as the spec's three dependencies (F7); pollinator figure not used (F8); threats kept to a short overview with a pointer to the sibling lessons (F9).
- Food-web models re-derived: Species-poor (5): removing rabbit loses the fox; removing grass loses all four consumers. Species-rich (10): removing grass loses nothing; removing oak loses only the caterpillar. Titles "5 species" and "10 species" match.
- The route chip is correct on all four routes (biodiversity builds its own return object but spreads the route helper).

### Rules 1–4, stage 2b
- Rule 1: every hook has two options and a "If you had to guess, …?" line.
- Rule 2: biology equations (heart rate, rate of blood flow, % change in mass, rate of water uptake, SA:V) carry no chip and read "Written out".
- Rule 3: SA:V is a worked Steps (2 cm cube) then an attempt Steps (3 cm cube) before the ladder. Heart rate / blood flow are two-step CFIFA, not chains.
- Rule 4: ladder 2·2·2·1 in all six; five quiz questions on every route; no "Shape:" alert after pressing every enabled control.

### Open items
- None. Two points that were flagged are **lane-ruled: they stand as the pack ruled**: the CH TH ionosphere and UV-sterilisation quiz items (uses-em-waves; pack UEM-F3/F4 allow them on CH TH) and the predictor's "CO and soot together" simplification (atmospheric-pollutants; Design NOTES 3.2, pack F5 "CO and/or C").
- `review_state` is `examiner-reviewed` on all 13 lessons, so no page shows the "Draft" banner. (Not yet frozen by this log; the freeze file is stamped separately.)
- Fixed after review: Ks4Steps / Ks4Cfifa line inputs clipped their placeholders at phone width ("anything to co…"). The batch-4 stylesheet only (`EXTRA_CSS` in `ks4_lessons/batch_4.py`, appended to `shared/ks4-lesson-batch-4.css`) now tightens the line card and badge at 520px and below and sets the hint to 11px (10px at 380px and below). Measured on all 50 pages at 360 and 390: no placeholder is wider than its input. No shared asset changed.
- Cosmetic, Design's layout, left: the satellite and cycle figures have labels that cross arrows; at 500 °C the infrared peak is off the axis.
