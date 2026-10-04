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
