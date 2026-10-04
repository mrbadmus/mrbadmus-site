# KS4 batch 4: 13 lessons (Part 2 of the brief)

Written from `docs/ks4/packs/batch-4/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/), main at e417fb1, 4 Oct 2026. No lesson text comes from old site data: these pages don't load `ks4-source.js`. Every quiz item is written into the lesson, either verbatim from the pack or new.

## Files

One runnable `.dc.html` per lesson, named like the pilot (`ks4-<subject>-<spec>-<slug>`). The spec number is the corrected AQA reference from FLAGS, not the site's.

| # | Lesson | File | Routes |
|---|---|---|---|
| 1 | The heart and blood vessels | ks4-biology-4.2.2.2-heart-blood-vessels | CF CH TF TH |
| 2 | The water cycle | ks4-biology-4.7.2.2-water-cycle | CF CH TF TH |
| 3 | Atmospheric pollutants from fuels | ks4-chemistry-5.9.3.1-atmospheric-pollutants | CF CH TF TH |
| 4 | Efficiency | ks4-physics-6.1.2.2-efficiency | CF CH TF TH · Higher layer CH TH |
| 5 | Infrared, black bodies | ks4-physics-4.6.3-infrared-black-bodies | TF TH · Higher layer TH |
| 6 | Diffusion, osmosis, active transport | ks4-biology-4.1.3-transport-in-cells | CF CH TF TH · RP2 (CF CH) / RP3 (TF TH) |
| 7 | Blood | ks4-biology-4.2.2.3-blood | CF CH TF TH |
| 8 | The periodic table | ks4-chemistry-5.1.2.1-periodic-table | CF CH TF TH |
| 9 | Thermal conductivity | ks4-physics-6.1.2.1-thermal-conductivity | CF CH TF TH · RP2 layer TF TH |
| 10 | Coronary heart disease | ks4-biology-4.2.2.4-coronary-heart-disease | CF CH TF TH |
| 11 | Biodiversity | ks4-biology-4.7.3.1-biodiversity | CF CH TF TH |
| 12 | Development of the periodic table | ks4-chemistry-5.1.2.2-development-periodic-table | CF CH TF TH |
| 13 | Uses of EM waves | ks4-physics-6.6.2.4-uses-em-waves | CF CH TF TH · Higher layer CH TH |

Shared blocks are in the same folder so each lesson runs on its own: the four Part 1 blocks (Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, with Ks4Chain and Ks4Write), and the pilot blocks Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, plus ks4-lib.js, ks4-diagrams.js, ks4-theme.css and support.js.

## Page order (every lesson)

Header (AQA ref, routes, route picker; equation-sheet link and sheet panel on physics pages with equations) → Start here (`Ks4Guess`) → video slot → teaching sections, each with its figure and one interactive → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → equation block (`Ks4Triangle`) and CFIFA (`Ks4Cfifa`) / Step 1 … Step 2 (`Ks4Steps`) where the lesson calculates → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. Route layers are `sc-if` blocks on `isHigher` / `isTriple`. No examiner tip is shown: none is approved for this batch.

## Changes to shared blocks in this delivery

1. **Ks4Triangle, the 4 Oct correction.** It has one chip, "On the sheet", shown for any `source` except `'none'`. Nothing renders "Learn this one". `source` now takes `'sheet'` (default) or `'none'`. Part 1's copy, demos and notes are updated to match.
2. **Ks4Cfifa** (pilot file, one addition): an example can carry `eq` and `find`, and the triangle (compact) then appears under its Formula line. Rule 2 needs it in CFIFA's Formula step.
3. **Ks4QuizBank**: fixed at five questions, "Show more" removed, heading "Five questions on this lesson" (the Part 1 rule, now in the file).
4. **Ks4Steps, Ks4Guess**: two `white-space: nowrap` fixes (the "Step 2" badge and the "Or this" tag wrapped at some widths). Applied to the Part 1 copies too.

## Rules 1–4 in this batch

- **Rule 1.** Every opener is the pack's access note, framed as "If you had to guess, … ?" with two options and a friendly reply to each.
- **Rule 2.** Triangles in the equation block, in CFIFA's Formula step, and (physics) in the sheet panel under the equation-sheet link. Efficiency: both equations, "On the sheet". Biology (heart rate, rate of blood flow, % change in mass, rate of water uptake, SA:V): `source: 'none'`, so no chip. See flag G1.
- **Rule 3.** Chained calculations: efficiency (useful, then wasted) and SA:V (surface area, volume, ratio, three steps). Each has a worked `Ks4Steps` then a `Ks4Steps` attempt before the ladder. The ladder's SA:V item comes after both. Heart: the optional chained "volume per minute" calculation was not added, so no chain there.
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route; rung 4 is one 4- or 6-mark answer. The practice set is five questions per route.

## Verbatim quiz items used

| Lesson | Verbatim | Re-authored (allowed by flag) | New |
|---|---|---|---|
| 1 Heart | q1 q2 q3 | q4 with HBV-F1 wx1 and HBV-F5 wx2 | pacemaker |
| 2 Water cycle | q1 q2 | — | fresh water (F2), clouds, precipitation |
| 3 Pollutants | — | — | 5 (q1 WRONG, q2 off-spec); includes predict-the-products |
| 4 Efficiency | q1 q2 | — | 3 |
| 5 Infrared | q2 | q1 on the same stem, option 4 and wx3 rewritten (IRB-F2) | 3 |
| 6 Transport | q1 q2 q4 q5 | q3 with "less energy" (F4) | — |
| 7 Blood | q1–q4 | — | antitoxins |
| 8 Periodic table | q1 q2 | — | 3 |
| 9 Thermal cond. | q1 | — | 3 base + 1 route-dependent (TF TH: RP2 item replacing q2; CF CH: cavity insulation) |
| 10 CHD | q1 q2 q3 | — | faulty valve, artificial hearts |
| 11 Biodiversity | — | — | 5 (q1 off-spec, q2 WRONG) |
| 12 Dev. of PT | q2 | — | 4, including isotopes (F2) |
| 13 EM uses | q1 q2 on CH TH only | — | CF TF: 5 base use items; CH TH: q1 q2 + 3 base |

Options are shuffled by `KS4.item()`, as in the pilot. The pilot FIFA (efficiency engine; % change potato) is used verbatim as CFIFA example 1, with the pack's own Convert line.

## Science flags

**G · Global**
- G1. Biology equations are on no equation sheet, so they carry no chip (`source: 'none'`), and the line above them reads "Written out". Showing "On the sheet" would be false. If Mide wants a chip on biology too, that's a one-word change.
- G2. Fonts. `→` (U+2192) appears inside verbatim quiz text (transport q4) and verbatim FIFA-style lines. Subscripts (₂) appear in a verbatim blood wrong-answer explanation. Δ appears in the % change triangle. None of these are in the house fonts' latin subsets, so they render in the fallback font. Arrows written by me are drawn as SVG; subscripts in the template use `<sub>`.
- G3. Relative values in teaching models (Sankey presets, wall model, black-body curves, RP graph, Te/I masses) are flagged per lesson below. None are exam data.

**1 · Heart and blood vessels**
- 1.1 Badge 4.2.2.2 (HBV-F11). Valves unnamed (F8) and placed at the exits of the ventricles (F7).
- 1.2 Lungs taught and practised (F3); natural and artificial pacemakers both base (F2, F4).
- 1.3 Rate calculations (F6): three CFIFA examples (nothing to convert; s → min; cm³ → dm³), two attempts, two ladder items. Values: 6.0 dm³ ÷ 1.5 min = 4.0 dm³/min; 21 ÷ 0.25 = 84 bpm; 1.5 ÷ 0.30 = 5.0; 36 ÷ 0.5 = 72; 2.4 ÷ 4.0 = 0.60; 18 ÷ 0.25 = 72; 0.90 ÷ 0.20 = 4.5.
- 1.4 "Pressure falls all the way round: arteries > capillaries > veins" (from HBV-F1).
- 1.5 Heart diagram drawn as you face the patient; schematic.

**2 · Water cycle**
- 2.1 Badge 4.7.2.2 (F1). Fresh-water importance taught as its own section and in practice (F2). Diagram includes transpiration, groundwater and "salt stays here" (F5).
- 2.2 "Follow a drop" flagship: snow on the hilltop melts into runoff (step 7). Code to confirm that's acceptable wording.

**3 · Atmospheric pollutants**
- 3.1 No Higher block (F3). Catalytic converters, acid-forming equations, smog and the pH multiplier are left out entirely (F2, F4, F6, F8).
- 3.2 Predict-the-products (F5) is taught with a worked example and a four-case predictor that uses F5's rules exactly: plenty of O₂ gives CO₂ + H₂O; limited O₂ adds CO and particulates; S gives SO₂; high temperature gives NOₓ. The predictor treats "CO and soot" as arriving together under limited oxygen; the pack says "CO and/or C".
- 3.3 New q1 replacement keyed on "toxic, colourless, odourless, not easily detected" (F1).

**4 · Efficiency**
- 4.1 Higher layer (ways to increase efficiency) on CH TH only; lubrication and insulation base (F1).
- 4.2 Sankey presets: filament lamp 10%, LED 40% (F2's realistic figure), motor 75% (source example). Teaching values, not data.
- 4.3 "× 100" is a conversion line, never a triangle (F3).
- 4.4 Chained example: 0.80 × 2000 = 1600 J, 2000 − 1600 = 400 J. Attempt: 0.35 × 60 000 = 21 000 J, 60 000 − 21 000 = 39 000 J. CFIFA: 1800 ÷ 2500 = 0.72; 0.40 × 60 = 24 W; 900 ÷ 1200 = 0.75; 0.90 × 5000 = 4500 J. Ladder: 3 ÷ 60 = 0.05; 0.65 × 4000 = 2600 J. Rung 4: 6 ÷ 40 = 0.15, 3 ÷ 8 = 0.375.
- 4.5 The rung-2 efficiency item expects the unit "no unit": `Ks4Practice` offers it as a unit choice.

**5 · Infrared, black bodies**
- 5.1 Route picker limited to Triple Foundation / Triple Higher. Balance and Earth sections are TH only; curves are base for the page (F5). "Reflection of radiation into space", never albedo.
- 5.2 Curves are Planck curves for a black body at 500, 1000, 1500, 2500, 3500 and 5500 °C, scaled to the hottest shown. Peak = 2898 µm·K ÷ T (1000 °C: 2.3 µm, IR; 5500 °C: 0.50 µm, visible), consistent with F1/F2/F4. Glow words: 1000 °C dull red, 1500 °C orange, 2500 °C yellow-white. Code to check those colour bands.
- 5.3 No RP block; the matt-black result is recalled as a bridge (F6). Star colours and telescopes left out (F7).

**6 · Transport in cells**
- 6.1 All base on every route, including % change, the zero-crossing reading and SA:V (F2). RP label route-aware (F3).
- 6.2 Wording: "no net movement of water: same concentration as the cell contents"; never "water potential" (F6). Energy "from respiration"; no ATP or carrier proteins in my text (F5). The verbatim quiz items still say "ATP" and "selectively permeable" (F10 says they stay usable).
- 6.3 Gills and leaves added (F8); rate of water uptake taught (F9): 0.60 ÷ 120 = 0.005 g/min; 0.90 ÷ 90 = 0.01 g/min.
- 6.4 SA:V three-step worked (2 cm: 24, 8, 3 : 1) and attempt (3 cm: 54, 27, 2 : 1) (F7). Ladder: 4 cm gives 96 ÷ 64 = 1.5 : 1.
- 6.5 RP graph values are typical class results (crossing ≈ 0.37 mol/dm³). Not data.
- 6.6 Diffusion definition, its factors and the active transport examples are the spec's own wording.

**7 · Blood**
- 7.1 Badge 4.2.2.3 (F7). Three white-cell functions, antitoxins included (F1). Recognition from a drawn smear (F2): the smear is a drawing, not a micrograph. A real stained photograph would be better if one is licensed.
- 7.2 Biconcave line re-cut to F3's wording. Spleen, fibrin and memory cells left out (F4, F6).

**8 · Periodic table**
- 8.1 Transition metals dropped, with a pointer to the Triple lesson (F1). Group 1 and 7 explanations on every route, in spec language, with no "ionisation energy" (F2). Group 0 "unreactive throughout" (F3). "Occupied shells" (F5).
- 8.2 Builder covers Z = 1–20; hydrogen is drawn on its own above the table, as on the AQA sheet.

**9 · Thermal conductivity**
- 9.1 Written for all four routes; RP2 layer TF TH only (F1). No Higher layer, no U-values, no conduction equation (F3, F6). EM shielding dropped (F2).
- 9.2 Cavity insulation gives both reasons, poor conductor and no convection (F7). RP2 includes a thickness part (F5) and uses the fair temperature-drop comparison (F4).
- 9.3 The wall model uses relative rates only: stone 3 × the conductivity of the insulating block; thick = 3 × thin. Not data.
- 9.4 Opener: spoons in soup, the pack's access note. Part 1's Demo 2 used the same scene as a format demo.

**10 · Coronary heart disease**
- 10.1 Badge 4.2.2.4 (F8). Everything base (F1). Faulty valves, heart-and-lungs transplant and artificial hearts taught (F2, F3). Bypass left out (F4). Age line re-cut (F5); menopause line dropped (F6).
- 10.2 Evaluation: pros and cons from F7; a three-patient choice activity; a 6-mark Evaluate item at rung 4.
- 10.3 Risk factors (4.2.2.6) appear as one short line. The causal-versus-correlation point is not taught here.

**11 · Biodiversity**
- 11.1 Spec definition only; no relative abundance or genetic diversity (F1–F3, F6). Stability taught with the spec's three dependencies (F7). No Higher layer (F5).
- 11.2 Threats and measures kept to a short overview with pointers to sibling lessons (F9). The sort includes hedgerows, breeding programmes and field margins as "helps maintain", which strays into `maintaining-biodiversity`. Code may want to cut it to the three threats.
- 11.3 Pollinator figure not used (F8).
- 11.4 The food webs are invented models (5 and 10 species).

**12 · Development of the periodic table**
- 12.1 Isotope step taught and practised (F2), with Te 52 p / 127.6 and I 53 p / 126.9; Ar/K mentioned as found later (F3). No-gaps wording from F1.
- 12.2 The "Gap" step names arsenic (As) beside the gap below silicon. That's standard history, but it isn't in the pack. Code to confirm or blank it.
- 12.3 The brief's "Newlands' octaves beside Mendeleev's table" figure is only partly drawn: Mendeleev fragments (Te/I swap, gap below Si) and the Te/I comparison are drawn, but there is no octaves table. Flagging rather than inventing an octave layout.

**13 · Uses of EM waves**
- 13.1 Base core = the six spec pairs, verbatim, sun tanning included (F5). Reasons are in the CH TH layer only (F3). No total internal reflection, no ultrasound (F2).
- 13.2 Microwave cooking re-cut per F1. The satellite reason is "pass through the atmosphere" (F4); the verbatim q1 key still says "ionosphere" (F4 allows it on CH TH).
- 13.3 The ultraviolet lamp reason (a coating absorbs UV and gives out visible light) is my own wording, not the pack's. Code to check.
- 13.4 Rung 3 uses UV and ionising hazards (8464 6.6.2.3, base) so the ladder stays base on CF TF.

## Not done / for Code

- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden, as in the pilot.
- Prev/next links point at sibling batch-4 files where a natural order exists; Code to rewire to the live order.
- Dark mode uses the pilot's remap; SVG plates stay cream, as in the pilot.
