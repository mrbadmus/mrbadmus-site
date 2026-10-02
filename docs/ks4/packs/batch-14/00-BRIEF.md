# KS4 Batch 14 — Design input pack

Mide's ruling, 2 Oct 2026: **Design authors and draws every KS4 lesson from batch 4 on.** Code built this pack, will port your pages, check the science and ship them, exactly as for the pilot.

## Read first

- `docs/ks4/architecture.md` — the ten laws, the families, the CFIFA amendment, and **the two amendments of 2 Oct 2026** (Design writes the lessons; the four lesson rules).
- The pilot, as the bar and the template: `docs/ks4/design-reference/pilot/` (your delivery, unmodified) and the live pages it became.
- This file, then `FLAGS.md` (science you must not repeat), then each lesson's `04-checked-science-source/` file, then `05-diagram-library/README.md`.

## The four lesson rules (Mide, 2 Oct 2026) — apply to every lesson here

1. **Start here is a two-option guess**, framed as a guess, answerable from everyday experience on every route; the reveal is encouraging either way and leads straight into the teaching.
2. **Equations are formula triangles you can cover** — in the equation block, the equation-sheet panel and CFIFA's Formula step. A square or a ½ gets its own extra line (square-root, ×2).
3. **Teach every step before you test it.** A calculation that chains two equations gets its own "Step 1 … Step 2 …" worked example before any pupil does one; CFIFA on each step.
4. **Practice is the same size in every lesson** — same number of questions at each rung of the end practice and the exam ladder. Set the number once (at least the content-standards floor) and keep it across the batch.

Each lesson below says which calculations chain, which equations need triangles, and how many verbatim quiz items are usable; the rest of each bank is yours to write to the fixed size.

## Lessons

| # | lesson | slug | subject · topic | source file |
|---|---|---|---|---|
| 1 | Pure Substances | `pure-substances` | Chem · analysis | `04-checked-science-source/chemistry-5.8.1.1-pure-substances.md` |
| 2 | Formulations | `formulations` | Chem · analysis | `04-checked-science-source/chemistry-5.8.1.2-formulations.md` |
| 3 | Chromatography | `chromatography` | Chem · analysis | `04-checked-science-source/chemistry-5.8.1.3-chromatography.md` |
| 4 | Testing for Gases | `testing-for-gases` | Chem · analysis | `04-checked-science-source/chemistry-5.8.2.1-testing-for-gases.md` |
| 5 | Flame Tests | `flame-tests` | Chem · analysis | `04-checked-science-source/chemistry-4.8.3.1-flame-tests.md` |
| 6 | Instrumental Methods and Flame Emission Spectroscopy | `instrumental-methods` | Chem · analysis | `04-checked-science-source/chemistry-4.8.3.6-instrumental-methods.md` |
| 7 | The Composition of the Atmosphere | `composition-of-atmosphere` | Chem · atmosphere | `04-checked-science-source/chemistry-5.9.1.1-composition-of-atmosphere.md` |
| 8 | Alternative Methods of Extracting Metals | `alternative-metal-extraction` | Chem · resources | `04-checked-science-source/chemistry-5.10.1.4-alternative-metal-extraction.md` |
| 9 | Life Cycle Assessment | `life-cycle-assessment` | Chem · resources | `04-checked-science-source/chemistry-5.10.2.1-life-cycle-assessment.md` |
| 10 | Ways of Reducing the Use of Resources | `reducing-use-of-resources` | Chem · resources | `04-checked-science-source/chemistry-5.10.2.2-reducing-use-of-resources.md` |
| 11 | Corrosion and Its Prevention | `corrosion-prevention` | Chem · resources | `04-checked-science-source/chemistry-4.10.3.1-corrosion-prevention.md` |
| 12 | Alloys as Useful Materials | `alloys-useful-materials` | Chem · resources | `04-checked-science-source/chemistry-4.10.3.2-alloys-useful-materials.md` |
| 13 | Ceramics, Polymers and Composites | `ceramics-polymers-composites` | Chem · resources | `04-checked-science-source/chemistry-4.10.3.3-ceramics-polymers-composites.md` |
| 14 | The Haber Process | `haber-process` | Chem · resources | `04-checked-science-source/chemistry-4.10.4.1-haber-process.md` |
| 15 | Production and Uses of NPK Fertilisers | `npk-fertilisers` | Chem · resources | `04-checked-science-source/chemistry-4.10.4.2-npk-fertilisers.md` |

True routes, layers and families are in each lesson's entry below; they come from the AQA specification's own labels, checked by an examiner, and where they differ from what the site ships today the entry says so.

## Per lesson

### 1. Pure Substances
`pure-substances` · Chemistry / analysis · AQA 8464 5.8.1.1; 8462 4.8.1.1 · CF CH TF TH (all base)

- **Family:** CONTRAST. One discriminating difference: a pure substance melts at one sharp temperature, a mixture melts over a range (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** heat two samples side by side and watch the thermometers. One sits flat at a single temperature, the other creeps across a range below it.
- **Route layers:** none. 5.8.1.1 has no HT or chemistry-only statement. The `higher` field is not a layer (PS-F3).
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Pure means natural, so pure orange juice is pure." In chemistry pure means a single element or compound (5.8.1.1).
  - "Mixing two pure chemicals still gives something pure." A mixture is not a single substance (5.8.1.1).
  - "An impure sample just melts at a different temperature." It melts over a range, not at a specific temperature (5.8.1.1).
  - "An impurity always raises the boiling point." The spec fact is "specific temperature vs range" (PS-F1).
- **"Start here" access note (rule 1):** "pure" on a juice carton vs "pure" in a lab: same word, different meaning?
- **Practice (rule 4):** q1 and q2 usable verbatim on all four routes (2). None unusable. Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md`. Must draw: heating curves, pure (flat plateau) overlaid on impure (sloped range). `heating_curve()` draws only the pure one.
- **Examiner tip:** none approved.

---

### 2. Formulations
`formulations` · Chemistry / analysis · AQA 8464 5.8.1.2; 8462 4.8.1.2 · CF CH TF TH (all base)

- **Family:** CLASSIFY. The spec's one skill is "identify formulations given appropriate information": formulation or not, and why (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a shelf of product labels. The pupil sorts each one into formulation, mixture or pure substance, then changes one ingredient's amount and sees the product fail.
- **Route layers:** none. 5.8.1.2 has no HT or chemistry-only statement. The `higher` field is not a layer (FO-F1). Flame tests in th3 are chemistry only (FO-F2).
- **Required practical:** none.
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Any mixture is a formulation." It must be designed as a useful product, in carefully measured quantities (5.8.1.2).
  - "A pure chemical like ethanol is a formulation." A formulation is a mixture (5.8.1.2, 5.8.1.1).
  - "The extra ingredients are just filler; only the active one matters." Each chemical has a particular purpose (5.8.1.2).
  - "Alloys aren't formulations, they're metals." Alloys are on the spec's list (5.8.1.2).
- **"Start here" access note (rule 1):** squash made by a recipe vs a puddle of muddy water. Which one was designed?
- **Practice (rule 4):** q1 and q2 usable verbatim on all four routes (2). None unusable. Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md`. No figure exists and none is required. A labelled product-ingredient card set is Design's call.
- **Examiner tip:** none approved.

---

### 3. Chromatography
`chromatography` · Chemistry / analysis · AQA 8464 5.8.1.3; 8462 4.8.1.3 · CF CH TF TH (all base, RP on all four)

- **Family:** REQUIRED PRACTICAL. RP12/RP6 is the lesson: run the practical, measure, calculate Rf, identify against references (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a simulated chromatogram. The pupil places the baseline and the solvent level, runs it, measures from the origin to the spot centre, then matches the unknown's Rf to the references.
- **Route layers:** none. 5.8.1.3 has no HT or chemistry-only statement. The `higher` field is not a layer (CH-F6).
- **Required practical:** Combined **RP12** (8464 5.8.1.3, §10.2.12); Chemistry **RP6** (8462 4.8.1.3, §8.2.6). On CF CH TF TH. Not "RP1" as the source says (CH-F1).
- **Calculations:**
  - Rf = distance moved by substance ÷ distance moved by solvent. **Chains equations? no.** (Reading the two distances off the chromatogram, from the origin to the spot centre, is a measuring step to teach first.) Convert: both distances must be in the same unit (mm ↔ cm). Rf has no unit; answer to the data's significant figures. Base.
  - Rearranged: distance moved by substance = Rf × distance moved by solvent. Chains? no. Base.
  - CFIFA: worked example 1 is the frozen FIFA (7.2 ÷ 9.6, nothing to convert). Worked example 2 needs a real conversion, e.g. spot 36 mm, solvent front 8.0 cm.
- **Equations that need formula triangles (rule 2):** Rf = distance moved by substance ÷ distance moved by solvent — **Learn it** (no chemistry equation sheet). Triangle: top = distance moved by substance; bottom = Rf × distance moved by solvent.
- **Misconceptions to confront:**
  - "Measure to the top of the spot." Measure from the origin to the centre of the spot (5.8.1.3).
  - "Rf of 1.6 is fine." Rf is between 0 and 1; you divided the wrong way (5.8.1.3).
  - "One spot means it's pure." Only one spot in every solvent shows it is pure (5.8.1.3).
  - "A mixture always shows one spot per substance." Spots may separate depending on the solvent (5.8.1.3).
  - "Draw the start line in pen." Ink dissolves and runs; use pencil (RP12/RP6).
  - "Put the spots in the solvent." The solvent must be below the line, or the spots dissolve into it (RP12/RP6).
- **"Start here" access note (rule 1):** a wet felt-tip mark on a paper towel spreads into colours. Is that ink one colour or several?
- **Practice (rule 4):** q2 usable verbatim on all four routes (1). q1 is **not usable** (CH-F2, CH-F3). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md`. Must draw: the chromatography set-up with an unknown beside references (`figlib/chemistry.py` `chromatography()`), marked origin, spot centre and solvent front distances.
- **Examiner tip:** none approved.

---

### 4. Testing for Gases
`testing-for-gases` · Chemistry / analysis · AQA 8464 5.8.2.1–5.8.2.4; 8462 4.8.2.1–4.8.2.4 · CF CH TF TH (all base)

- **Family:** CLASSIFY. Four gases, four tests: result → gas, and gas → test (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** four unlabelled tubes of gas. The pupil picks a test (lit splint, glowing splint, limewater, damp litmus), sees the result, and names each gas.
- **Route layers:** none. 5.8.2 has no HT or chemistry-only statement. The `higher` field is not a layer (TG-F3).
- **Required practical:** none of its own. (The tests are used to identify the products in Combined RP9 / Chemistry RP3, electrolysis. Chemistry RP7's AT 8 names "gas tests", 8462 §8.2.7.)
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none. Chemical equations only: CO₂ + Ca(OH)₂ → CaCO₃ + H₂O; 2H₂ + O₂ → 2H₂O (not the unbalanced form in th1, TG-F1).
- **Misconceptions to confront:**
  - "Use a glowing splint for hydrogen." Hydrogen: burning splint → pop. Oxygen: glowing splint → relights (5.8.2.1, 5.8.2.2).
  - "Hydrogen puts the splint out." It burns rapidly with a pop (5.8.2.1).
  - "Any liquid goes cloudy with CO₂." Only limewater, calcium hydroxide solution (5.8.2.3).
  - "Chlorine turns litmus red." The mark is bleached, turns white (5.8.2.4).
  - "Dry litmus works." The paper must be damp (5.8.2.4).
- **"Start here" access note (rule 1):** blow on a glowing barbecue ember: does it flare up or go out?
- **Practice (rule 4):** q1 and q2 usable verbatim on all four routes (2). None unusable. Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md`. Must draw: the four tests (`figlib/chemistry.py` `ion_tests()` gas rows cover H₂, O₂, Cl₂), plus a CO₂-through-limewater figure, which is missing.
- **Examiner tip:** none approved.

---

### 5. Flame Tests
`flame-tests` · Chemistry / analysis · AQA — (not in 8464); 8462 4.8.3.1 (chemistry only) · TF TH (whole lesson triple, no HT layer)

- **Family:** CLASSIFY. Colour → ion is a fast decision with one complication (masking). The RP7 part is a single method step, not the lesson's demand (BATCH-PLAN kept).
- **Flagship (a suggestion, not a spec):** a Bunsen and a wire loop. The pupil tests unknown salts and names each ion, then tests a sodium + potassium mixture and sees the yellow hide the lilac.
- **Route layers:**
  - triple: the whole lesson. 8462 4.8.3 "(chemistry only)", 4.8.3.1.
  - Not a layer: the `higher` field and th2's electron explanation are off-spec (FT-F3).
- **Required practical:** **Chemistry RP7** (8462 4.8.3.5, §8.2.7): identify the ions in unknown single ionic compounds, 4.8.3.1–4.8.3.5. Chemistry only, TF TH. No Combined number. This lesson carries its flame-test part. The source's "RP Chemistry 4" is wrong (FT-F1).
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Sodium is red." Sodium is yellow; lithium is crimson (4.8.3.1).
  - "Potassium is purple." The spec word is lilac (4.8.3.1).
  - "Copper is blue." The flame is green; blue is the copper(II) hydroxide precipitate (4.8.3.1, 4.8.3.2).
  - "A mixture shows both colours." Some colours can be masked (4.8.3.1).
  - "Lithium and calcium are the same red." Crimson vs orange-red (4.8.3.1).
- **"Start here" access note (rule 1):** fireworks and street lights are different colours. Could the metal inside decide the colour?
- **Practice (rule 4):** q1 and q2 usable verbatim on TF and TH (2). None unusable. Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md`. Must draw: the flame-colour reference for the five ions (`figlib/chemistry.py` `flame_tests()`), and the wire-loop-in-Bunsen method.
- **Examiner tip:** none approved.

---

### 6. Instrumental Methods and Flame Emission Spectroscopy
`instrumental-methods` · Chemistry / analysis · AQA 8462 4.8.3.6–4.8.3.7 (chemistry only; no 8464 counterpart) · true routes: TF TH (triple layer, no HT)

**Family:** CONTRAST — the spec asks for the advantages of instrumental methods over the chemical tests, and FES is the instrumental twin of the flame test (`flame-tests`, same batch); kept from BATCH-PLAN.

**Flagship (a suggestion, not a spec):** The same unknown solution in a flame test and in a spectroscope side by side: the eye sees one masked colour, the spectrum shows two sets of lines the pupil matches against a reference set.

**Route layers:**
- Whole lesson: "4.8.3 Identification of ions by chemical and spectroscopic means (chemistry only)" — 8462 4.8.3.6, 4.8.3.7. Same content on TF and TH. No Higher block (the source's `higher` is off-spec — F1).

**Required practical:** none. (Chem 8462 RP7 is the chemical ion tests, a different lesson; AT 8 hand-held spectroscope is an optional opportunity, not an RP.)

**Calculations:** None. (Concentration is read by comparing line brightness with standards — a data reading, not a calculation.)

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "A machine just does the same as a flame test." → The output is a line spectrum that identifies the ions and measures their concentration (4.8.3.7).
- "If I can see the colour, I don't need the instrument." → In a mixture some flame colours are masked; the spectrum still shows each ion's lines (4.8.3.1; 4.8.3.7).
- "One line at the right wavelength proves the metal." → Match the sample's lines against the whole reference set (4.8.3.7).
- "A brighter line means a hotter flame." → Conditions are kept the same; a brighter line means more of that ion, read against standards (4.8.3.7).
- "Instruments are better because they're more expensive." → The spec's advantages are accurate, sensitive and rapid (4.8.3.6).

**"Start here" access note (rule 1):** Everyone has struggled to tell two close shades of a colour apart by eye — would a machine or a person be better at it?

**Practice (rule 4):** 2 frozen quiz items usable on TF and TH (q1, q2). None unusable. The bank must be topped up by Design to the batch's fixed size, centred on reading a sample spectrum against a reference set, including a two-ion mixture (F3), and on stating the three spec advantages (F5).

**Diagrams:** `05-diagram-library/README.md` row 6 — `flame_tests()` covers the flame-test side. Must draw: a line-spectrum figure (sample strip beside reference strips for Li, Na, K, Ca, Cu, lines at given wavelengths, varying brightness); a simple flame → spectroscope → detector schematic.

**Examiner tip:** none approved.

---

### 7. The Composition of the Atmosphere
`composition-of-atmosphere` · Chemistry / atmosphere · AQA 8464 5.9.1.1; 8462 4.9.1.1 · true routes: CF CH TF TH (all base)

**Family:** CLASSIFY — the demand is placing each gas at its share of today's air (about four-fifths, about one-fifth, small amounts) and moving between fractions and percentages; kept from BATCH-PLAN. Distinct from `early-atmosphere` (how it changed, batch 3) and `greenhouse-gases` (why CO₂ is rising, batch 3): this lesson is TODAY's air only.

**Flagship (a suggestion, not a spec):** A 100-particle box of air the pupil fills gas by gas, predicting how many of each before the true count (80 N₂, 20 O₂, a handful of the rest) drops in.

**Route layers:**
- None. 5.9.1.1 / 4.9.1.1 has no HT and no chemistry-only content. The source's `higher` is off-spec (F2): no Higher block.

**Required practical:** none.

**Calculations:**
- Volume of a gas in a sample of air: volume = fraction (or % ÷ 100) × total volume (e.g. ¹⁄₅ × 500 cm³ = 100 cm³ oxygen). Chains equations? no. Convert: dm³ ↔ cm³ (1 dm³ = 1000 cm³) when the sample and answer units differ; % → fraction. Base (MS 1c). One worked example before practice.
- Fraction ↔ percentage ↔ ratio (⁴⁄₅ = 80%; N₂ : O₂ ≈ 4 : 1). Chains? no. Base (MS 1c).

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Air is mostly oxygen — that's what we breathe." → About four-fifths nitrogen, one-fifth oxygen (5.9.1.1).
- "Carbon dioxide is a big part of the air." → It is a small proportion, about 0.04% (5.9.1.1).
- "Today's air is changing fast, so the proportions are new." → They have been much the same for 200 million years (5.9.1.1).
- "Air is just nitrogen and oxygen." → There are small proportions of other gases, including CO₂, water vapour and noble gases (5.9.1.1).
- "Argon has been there since the Earth formed." → Wrong in the source (F1); argon is simply an unreactive noble gas — don't teach the origin claim.

**"Start here" access note (rule 1):** Everyone breathes air to get oxygen — is the air mostly oxygen, or mostly something else?

**Practice (rule 4):** 2 frozen quiz items usable on all four routes (q1, q2). None unusable. q2 (photosynthesis removes CO₂) leans on `early-atmosphere`'s point — don't add more of that. The bank must be topped up by Design to the batch's fixed size, with fraction/percentage and volume-of-gas items (F5).

**Diagrams:** `05-diagram-library/README.md` row 7 — `atmosphere_pie()` covers it directly. Must draw: nothing new beyond the pie (or a 100-square grid for the fractions work).

**Examiner tip:** none approved.

---

### 8. Alternative Methods of Extracting Metals
`alternative-metal-extraction` · Chemistry / resources · AQA 8464 5.10.1.4 (HT only); 8462 4.10.1.4 (HT only) · true routes: CH TH (whole lesson higher)

**Family:** CONTRAST — phytomining vs bioleaching (and both vs traditional mining), converging on one shared last step; kept from BATCH-PLAN. Distinct from `extraction-of-metals` (carbon reduction, batch 5) and `earths-resources` (finite vs renewable, batch 5).

**Flagship (a suggestion, not a spec):** Two pipelines from the same low-grade copper ore — plants → burn → ash → acid, and bacteria → leachate — that merge at "solution of copper compounds", where the pupil chooses scrap iron or electrolysis to finish.

**Route layers:**
- Whole lesson: 8464 5.10.1.4 (HT only); 8462 4.10.1.4 (HT only). Layer = higher on CH and TH (no chemistry-only label, so not triple-higher). Site ships CH TH — correct.
- The displacement ionic equation draws on 8464 5.4.1.4 (HT only) — consistent with the route.

**Required practical:** none.

**Calculations:** None.

**Equations that need formula triangles (rule 2):** none. (Cu²⁺(aq) + Fe(s) → Cu(s) + Fe²⁺(aq) is a chemical equation, not a triangle. The second frozen equation is unbalanced — F1, do not use.)

**Misconceptions to confront:**
- "The plants turn the metal into pure metal." → The plants absorb metal compounds; burning them gives ash containing metal compounds, which still has to be processed (5.10.1.4).
- "Bacteria eat the metal." → Bacteria produce leachate solutions containing metal compounds (5.10.1.4).
- "Once it's in solution you just boil off the water." → That gives copper compounds; copper metal needs displacement with scrap iron or electrolysis (5.10.1.4).
- "Iron can take copper's place because it's heavier." → Iron is more reactive than copper, so it displaces it (5.4.1.2).
- "Biological methods are just better." → They are slow; their gain is using low-grade ores without digging, moving and dumping large amounts of rock — evaluate both sides (5.10.1.4).

**"Start here" access note (rule 1):** Everyone knows plants pull water and food up from the soil through their roots — could a plant pull up metal too?

**Practice (rule 4):** 2 frozen quiz items usable on CH and TH (q1, q2). None unusable (the WRONG item is an equation, not a quiz item). The bank must be topped up by Design to the batch's fixed size, including a given-information evaluation item (F4).

**Diagrams:** `05-diagram-library/README.md` row 8 — only `reactivity_series()` exists (context). Must draw: phytomining sequence (grow → harvest → burn → ash → dissolve in acid); bioleaching sequence (bacteria on ore heap → leachate); the shared finish (scrap iron in copper solution → copper; or electrolysis).

**Examiner tip:** none approved.

---

### 9. Life Cycle Assessment
`life-cycle-assessment` · Chemistry / resources · AQA 8464 5.10.2.1; 8462 4.10.2.1 · true routes: CF CH TF TH (all base)

**Family:** INVESTIGATION — the spec skill is interpreting and judging LCA data, including spotting that pollutant effects need value judgements and that selective LCAs can be misused; kept from BATCH-PLAN. Distinct from `reducing-use-of-resources` (what end users do) and `earths-resources` (finite vs renewable).

**Flagship (a suggestion, not a spec):** A plastic-bag vs paper-bag LCA table the pupil fills stage by stage from data cards, then sees the verdict flip when a "company" leaves one stage out.

**Route layers:**
- None. 5.10.2.1 / 4.10.2.1 has no HT and no chemistry-only content. Comparative LCA is base on all four routes; the source's `higher` is not a Higher layer (F2). Green chemistry and atom economy are cut (F3).

**Required practical:** none.

**Calculations:**
- Total impact of a product from its stage values: total = sum of stage values (incl. transport). Chains? no. Convert: kJ ↔ MJ, g ↔ kg (CO₂, waste) so every stage is in the same unit before adding. Base (MS 1a, 1d).
- Impact per use = total ÷ number of uses, to compare a reusable bag with a single-use one. **Chains? yes** — Step 1 total the stages; Step 2 divide by the number of uses. Needs its own "Step 1 … Step 2 …" worked example first. Convert as above. Base (MS 1c, 2a).
- How many times larger / percentage difference between two products' values. Chains? no. Base (MS 1c).

**Equations that need formula triangles (rule 2):** none (data steps, not AQA equations).

**Misconceptions to confront:**
- "Paper is natural, so a paper bag is always greener." → Compare every stage, incl. manufacture and transport; paper can score worse (5.10.2.1).
- "An LCA is just maths, so it's objective." → Allocating values to pollutant effects needs value judgements; LCA is not purely objective (5.10.2.1).
- "If an advert quotes an LCA, it must be true." → Selective or abbreviated LCAs can be misused to reach pre-determined conclusions (5.10.2.1).
- "LCA only looks at what happens when you throw it away." → It covers extraction, manufacture and packaging, use, and disposal, with transport at each stage (5.10.2.1).
- "Everything in an LCA can be measured." → Water, resources, energy and some wastes are fairly easily quantified; pollutant effects are not (5.10.2.1).

**"Start here" access note (rule 1):** Everyone has been asked "paper or plastic?" at a till — if you had to guess, which bag is better for the planet?

**Practice (rule 4):** 1 frozen quiz item usable on all four routes (q2). Not usable: q1 (F1, do not use as written). The bank must be topped up by Design to the batch's fixed size, centred on plastic-vs-paper data items (F4).

**Diagrams:** `05-diagram-library/README.md` row 9 — `life_cycle_assessment()` covers the four-stage strip directly. Must draw: a two-row comparative LCA table/strip (plastic vs paper) with transport arrows between stages.

**Examiner tip:** none approved.

---

### 10. Ways of Reducing the Use of Resources
`reducing-use-of-resources` · Chemistry / resources · AQA 8464 5.10.2.2; 8462 4.10.2.2 · true routes: CF CH TF TH (all base)

**Family:** CLASSIFY — the demand is placing a way of saving a material at reduce / reuse / recycle and knowing why that rank, then judging options from given data; kept from BATCH-PLAN. Distinct from `life-cycle-assessment` (a whole-life audit of one product) and `earths-resources` (finite vs renewable).

**Flagship (a suggestion, not a spec):** A glass bottle and an aluminium can each sent down reduce → reuse → recycle, with an energy meter showing what each choice saves against making new from ore or sand.

**Route layers:**
- None. 5.10.2.2 / 4.10.2.2 has no HT and no chemistry-only content. The source's `higher` is not a Higher layer (F2): data evaluation is base on all four routes.

**Required practical:** none.

**Calculations:**
- Percentage energy saved by recycling: % saved = (energy from ore − energy from scrap) ÷ energy from ore × 100. **Chains? yes** — Step 1 energy saved = difference; Step 2 percentage of the original. Needs a "Step 1 … Step 2 …" worked example first. Convert: kJ ↔ MJ, or per-tonne ↔ per-kg, so both energies are in the same unit. Base (MS 1c).

**Equations that need formula triangles (rule 2):** none (a percentage, not an AQA equation).

**Misconceptions to confront:**
- "Recycling is the best thing you can do." → Reducing use comes first, then reuse, then recycling (5.10.2.2; UK waste hierarchy).
- "Recycling costs no energy." → Melting and recasting still need energy, but far less than extracting from ore (5.10.2.2).
- "Recycled aluminium saves energy because it's lighter." → Recycled metal is already aluminium, so the electrolysis of aluminium oxide in molten cryolite is avoided (5.4.3.3).
- "All recycled stuff gets sorted perfectly." → How much separation is needed depends on the material and the properties wanted — some scrap steel just goes into blast-furnace iron (5.10.2.2).
- "Only metals and plastics come from limited resources." → So do glass, building materials and clay ceramics (5.10.2.2).

**"Start here" access note (rule 1):** Everyone has finished a glass bottle — is it better for the planet to use it again or put it in the recycling?

**Practice (rule 4):** 1 frozen quiz item usable on all four routes (q2). Not usable: q1 (F1, do not use as written). The bank must be topped up by Design to the batch's fixed size, including the scrap-steel point (F3) and a given-data evaluation (F4).

**Diagrams:** `05-diagram-library/README.md` row 10 — `life_cycle_assessment()` is adjacent only. Must draw: a reduce > reuse > recycle hierarchy; a glass-bottle loop (reuse → crush and melt → new glass product); scrap steel joining blast-furnace iron.

**Examiner tip:** none approved.

---

### 11. Corrosion and Its Prevention
`corrosion-prevention` · Chemistry / resources · AQA 8462 4.10.3.1 (no 8464 equivalent) · TF TH (chemistry only)

- **Family:** CONTRAST. The spec's two mechanisms are barrier vs sacrificial, and galvanising is both. BATCH-PLAN's suggestion kept.
- **Flagship (a suggestion, not a spec):** scratch two coated nails, one tin-plated and one zinc-plated, and see which one the rust attacks.
- **Route layers:**
  - Triple-higher: 8462 4.4.1.4 (HT only). Rusting as iron losing electrons; zinc loses electrons in preference to iron (CP-F3). No other HT layer. The `higher` field is off-spec (CP-F4).
- **Required practical:** none. The rusting tubes are a spec "describe experiments" requirement (4.10.3.1) on both routes, not an RP (CP-F2).
- **Calculations:** none.
- **Equations that need formula triangles (rule 2):** none. The rusting symbol equation is a chemical equation, not a formula.
- **Misconceptions to confront:**
  - "Iron rusts in damp air or in any water." It needs both oxygen and water; boiled water under oil gives no rust (4.10.3.1).
  - "Aluminium doesn't corrode because it's unreactive." It is more reactive than iron, and its oxide layer protects it (4.10.3.1).
  - "Touching a more reactive metal makes iron rust faster." The more reactive metal corrodes instead (4.10.3.1; CP-F1).
  - "Galvanising is just a coat of zinc paint." It also protects sacrificially when scratched, because zinc is more reactive (4.10.3.1).
  - "Tin plating protects like zinc." Tin is less reactive, so once it is scratched the iron rusts faster.
- **"Start here" access note (rule 1):** a bike left out in the rain vs one kept in a dry shed: which goes rusty?
- **Practice (rule 4):** q1 and q2 usable verbatim on TF and TH (2 per route). None unusable. Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` (#11, nothing exists). Must draw: the three rusting tubes; barrier vs sacrificial (zinc block on a hull or pipe); a scratched tin coat vs a scratched zinc coat.
- **Examiner tip:** none approved.

---

### 12. Alloys as Useful Materials
`alloys-useful-materials` · Chemistry / resources · AQA 8462 4.10.3.2 (no 8464 equivalent; mechanism recap from 8464 5.2.2.7 / 8462 4.2.2.7) · TF TH (chemistry only)

- **Family:** CLASSIFY, as alloy → composition → property → use. Kept from BATCH-PLAN. The pilot `metals-alloys` already sorts uses into three bins and owns the distorted-layers mechanism, so this lesson classifies by **composition and property**, the 4.10.3.2 list, and closes on evaluating an unfamiliar alloy from data.
- **Flagship (a suggestion, not a spec):** a composition dial. Slide the carbon in steel (or the gold in a ring) and watch hardness, brittleness or carat change.
- **Route layers:** none. 4.10.3.2 has no HT statement, and the `higher` field is not a layer (AL-F3).
- **Required practical:** none.
- **Calculations:**
  - Gold percentage from carats: % gold = carats ÷ 24 × 100, and back. **Chains equations? no.** No units to convert (CFIFA Convert: "nothing to convert"). Base (triple). Spec anchors: 24 ct = 100 %, 18 ct = 75 %.
  - Percentage composition of an alloy from given masses: % = mass of metal ÷ total mass × 100. **Chains? no.** Convert step: masses must share a unit (g with kg). Base (triple).
- **Equations that need formula triangles (rule 2):** both Learn it (chemistry has no sheet).
  - % gold = carats ÷ 24 × 100 → triangle top: carats; bottom: (% ÷ 100) × 24. The ÷100 step is its own line.
  - % by mass = part ÷ whole × 100 → top: part; bottom: whole × (% ÷ 100).
- **Misconceptions to confront:**
  - "18 carat means 18 % gold." Carats are out of 24, so 18 ct = 75 % (4.10.3.2).
  - "An alloy is a compound." It is a mixture, not chemically combined in fixed ratios.
  - "More carbon always makes steel better." High carbon steel is strong but brittle; low carbon steel is softer and easier to shape (4.10.3.2).
  - "Stainless steel has no carbon." Chromium and nickel give the corrosion resistance; the carbon is still there (AL-F2).
  - "Aluminium alloys are used in planes because they're the strongest." They are chosen for low density (4.10.3.2).
  - "Bronze and brass are the same." Bronze is copper + tin; brass is copper + zinc (4.10.3.2).
- **"Start here" access note (rule 1):** are most metal things around you (cutlery, coins, keys) pure metals or mixtures of metals? Do not reuse the pilot's carat opener.
- **Practice (rule 4):** q2 usable verbatim on TF and TH (1 per route). q1 not usable (AL-F1). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` (#12). `metallic(cols, rows, {alloy:[…]})` covers the recap. Must draw: a composition → use table/strip for steel (low C, high C, stainless), bronze, brass, gold (24/18/9 ct), aluminium alloy.
- **Examiner tip:** none approved.

---

### 13. Ceramics, Polymers and Composites
`ceramics-polymers-composites` · Chemistry / resources · AQA 8462 4.10.3.3 (no 8464 equivalent) · TF TH (chemistry only)

- **Family:** CONTRAST. The spec's one "explain in terms of structure" demand is thermosetting vs thermosoftening, and LDPE vs HDPE and soda-lime vs borosilicate are contrasts of the same shape. BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** heat two polymer chain models side by side. The one with no cross-links slumps; the cross-linked one holds and finally chars.
- **Route layers:** none. 4.10.3.3 has no HT statement, and the `higher` field is not a layer (CPC-F4).
- **Required practical:** none.
- **Calculations:** quantitative comparison of material properties from a given table (4.10.3.3, e.g. strength ÷ density). **Chains equations? no.** Convert step: put values in the same unit before comparing (g/cm³ with kg/m³). Base (triple). No equation is named in the spec.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Thermosetting plastics melt and then set." They do not melt; cross-links hold the chains (4.10.3.3).
  - "LDPE and HDPE are made from different stuff." Both are made from ethene, under different conditions (4.10.3.3; CPC-F2).
  - "Cross-links are just strong intermolecular forces." They are bonds between chains; thermosoftening polymers have only weak forces between chains.
  - "Borosilicate glass is used because it's stronger." It melts at a higher temperature than soda-lime glass (4.10.3.3).
  - "A composite is better at everything." Matrix and reinforcement each bring a property; it is better in at least one (CPC-F5).
  - "In reinforced concrete the concrete is the reinforcement." The steel is the reinforcement; the concrete is the matrix (4.10.3.3).
- **"Start here" access note (rule 1):** a plastic drinks bottle vs a saucepan handle: which one would go soft in a hot oven?
- **Practice (rule 4):** q2 usable verbatim on TF and TH (1 per route). q1 not usable (CPC-F1). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` (#13, nothing exists). Must draw: thermosoftening (separate chains) vs thermosetting (cross-linked network); LDPE (branched) vs HDPE (unbranched) packing; a composite cross-section, matrix + fibres (CFRP or reinforced concrete).
- **Examiner tip:** none approved.

---

### 14. The Haber Process
`haber-process` · Chemistry / resources · AQA 8462 4.10.4.1 (no 8464 equivalent; uses 8462 4.6.1.4, 4.6.2.1–4.6.2.7) · TF TH (chemistry only, with a large TH layer)

- **Family:** SYSTEM. One plant: reactor, condenser and recycle loop, with three conditions you can change, each pulling rate and yield in different directions. BATCH-PLAN kept. On TF the system is shown and named; the "change one" play is TH.
- **Flagship (a suggestion, not a spec):** a plant with temperature and pressure dials. Turn one and two meters, rate and % ammonia, move in opposite directions (TH). TF sees the gases loop round.
- **Route layers:**
  - Triple-higher: 8462 4.10.4.1 "(HT only)". Interpret graphs of conditions vs rate; apply dynamic equilibrium to Haber; explain the trade-off between rate and position of equilibrium; relate conditions to the cost of raw materials and energy. With 8462 4.6.2.4–4.6.2.7 (HT only): Le Chatelier, temperature, pressure. The catalyst leaving the position unchanged sits here too (HB-F1).
- **Required practical:** none.
- **Calculations:** none required by 4.10.4.1. TH reads values off a % ammonia vs pressure graph (MS 1a, 1c). The FIFA is an "explain" scaffold, not a calculation; its CFIFA Convert line is "nothing to convert" (examined ✓). The `higher` atom-economy line is not HT and is trivially 100 % (HB-F6).
- **Equations that need formula triangles (rule 2):** none. N₂ + 3H₂ ⇌ 2NH₃ is a chemical equation.
- **Misconceptions to confront:**
  - "The iron catalyst makes more ammonia." It only makes equilibrium arrive faster; the yield is unchanged (TH; HB-F2).
  - "450 °C is used because hot gives the most ammonia." The forward reaction is exothermic, so lower temperature gives more; 450 °C is for rate (4.6.2.6, HT).
  - "They'd use 1000 atm if they could afford it, so pressure lowers yield." Higher pressure raises yield (2 molecules vs 4); cost and safety limit it (4.6.2.7, HT).
  - "Rate and yield are the same thing." Rate is how fast; yield is how much at equilibrium (4.10.4.1 HT trade-off).
  - "The hydrogen comes from the air too." Nitrogen comes from air, hydrogen from natural gas (4.10.4.1).
  - "The ammonia is recycled." The unreacted nitrogen and hydrogen are recycled; the ammonia is liquefied and removed (4.10.4.1).
- **"Start here" access note (rule 1):** can the nitrogen in the air we breathe be turned into plant food: yes or no?
- **Practice (rule 4):** TF: 0 usable (q1 and q2 are HT reasoning, HB-F1). TH: q1, q2 usable verbatim (2). Design authors the TF items and tops the bank up to the batch's fixed size on both routes.
- **Diagrams:** see `05-diagram-library/README.md` (#14, nothing exists). Must draw: the plant flow (N₂ + H₂ in → reactor with iron at 450 °C / 200 atm → condenser → liquid NH₃ out; recycle loop); TH: % ammonia vs pressure at several temperatures (HB-F5).
- **Examiner tip:** none approved.

---

### 15. Production and Uses of NPK Fertilisers
`npk-fertilisers` · Chemistry / resources · AQA 8462 4.10.4.2 (no 8464 equivalent; uses 8462 4.10.4.1, 4.8.1.2, 4.3.1.2) · TF TH (chemistry only)

- **Family:** PROCESS. The spec's core is the integrated route: mined rock and Haber ammonia → acids → soluble salts → blended formulation. BATCH-PLAN kept.
- **Flagship (a suggestion, not a spec):** a flow board. Drag raw materials (air, natural gas, phosphate rock, potash) through the linked plants until a bag of N, P and K fills.
- **Route layers:** none. 4.10.4.2 has no HT statement, and the `higher` field is off-spec or base (NPK-F4).
- **Required practical:** none. "Prepare an ammonium salt" is an AT 4 skills opportunity (4.10.4.2), not an RP.
- **Calculations:**
  - Percentage by mass of N (or P, K) in a fertiliser salt: Step 1 Mr from Ar values; Step 2 % = (Ar × number of atoms) ÷ Mr × 100. **Chains equations? yes**, Step 1 Mr then Step 2 %. It needs its own "Step 1 … Step 2 …" worked example first (e.g. NH₄NO₃: Mr 80 → 35 % N). Convert step: nothing to convert. Base (triple).
- **Equations that need formula triangles (rule 2):** % by mass = part ÷ whole × 100 (Learn it; chemistry has no sheet) → triangle top: mass of element (Ar × n); bottom: Mr × (% ÷ 100). The ÷100 step is its own line.
- **Misconceptions to confront:**
  - "Fertiliser is just nitrogen." NPK contains compounds of all three elements (4.10.4.2).
  - "Phosphate rock can go straight on the field." It is insoluble and must be treated with acid first (4.10.4.2).
  - "All three nutrients are made in factories." Potassium salts and phosphate rock are mined (4.10.4.2).
  - "Phosphate rock + any acid gives the same thing." Nitric acid → phosphoric acid + calcium nitrate; sulfuric → single superphosphate; phosphoric → triple superphosphate (4.10.4.2; NPK-F1).
  - "Making it in the lab and in industry is the same, just bigger." Industry is continuous, concentrated and uses the reaction's own heat (4.10.4.2; NPK-F1).
  - "Ammonium fertiliser causes acid rain." Acid rain comes from SO₂ and NOₓ from burning fuels (4.9.3; NPK-F2).
- **"Start here" access note (rule 1):** a field that grows wheat every year with nothing added: bigger or smaller harvests over time?
- **Practice (rule 4):** q1 usable verbatim on TF and TH (1 per route). q2 not usable as a core rung (off-spec, NPK-F3). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` (#15, nothing exists). Must draw: the integrated-process flow (air + natural gas → Haber ammonia → + nitric/sulfuric/phosphoric acid → ammonium salts; phosphate rock + acid → soluble phosphates; mined potassium salts → blend → NPK bag).
- **Examiner tip:** none approved.
