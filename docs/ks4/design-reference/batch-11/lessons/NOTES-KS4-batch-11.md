# KS4 batch 11: 16 lessons (chemistry: atomic structure, quantitative chemistry, acids and electrolysis)

Written from `docs/ks4/packs/batch-11/` (00-BRIEF.md, FLAGS.md, 04-checked-science-source/, 05-diagram-library/README.md), main, 12 Oct 2026. The V9 prompt’s updates win over the pack. No lesson text comes from old site data: pages don’t load `ks4-source.js`; every quiz item is written into its lesson.

Before this batch: the batch 6 transpiration fix (`Design's Output/Batch 6 fix/lessons/`), batch 9 (`Design's Output/Batch 9/lessons/`) and batch 10 (`Design's Output/Batch 10/lessons/`) are all finished and waiting for download; nothing was changed in them this turn.

## Files and routes

One runnable `.dc.html` per lesson in `Batch 11/lessons/`, named `ks4-chemistry-<spec>-<slug>` with the 8464 number (8462 for transition metals). Order is the prompt’s.

1. Development of the model of the atom · `ks4-chemistry-5.1.1.3-model-of-the-atom` · CF CH TF TH
2. Subatomic particles · `ks4-chemistry-5.1.1.4-subatomic-particles` · CF CH TF TH · Higher layer (half equations)
3. Relative atomic mass, atomic number and isotopes · `ks4-chemistry-5.1.1.6-relative-atomic-mass` · CF CH TF TH · calculates
4. Electronic structure · `ks4-chemistry-5.1.1.7-electronic-structure` · CF CH TF TH
5. Group 7: the halogens · `ks4-chemistry-5.1.2.6-group-7` · CF CH TF TH · Higher layer (ionic equations)
6. Properties of transition metals · `ks4-chemistry-4.1.3.1-transition-metals` · **TF TH only**
7. Mass changes in reactions · `ks4-chemistry-5.3.1.3-mass-changes-reactions` · CF CH TF TH · calculates · Higher layer (reacting masses)
8. Chemical measurements · `ks4-chemistry-5.3.1.4-chemical-measurements` · CF CH TF TH · calculates
9. Moles · `ks4-chemistry-5.3.2.1-moles` · **CH TH only** · calculates
10. Amounts of substances in equations · `ks4-chemistry-5.3.2.2-amounts-in-equations` · **CH TH only** · calculates
11. Oxidation and reduction · `ks4-chemistry-5.4.1.4-oxidation-reduction` · CF CH TF TH · Higher layer (electrons, ionic equations)
12. Making salts and neutralisation · `ks4-chemistry-5.4.2.2-salts-neutralisation` · CF CH TF TH · RP8/RP1 · Triple layer (titration pointer)
13. The pH scale and neutralisation · `ks4-chemistry-5.4.2.4-ph-scale` · CF CH TF TH · Higher layer (×10 per unit) · Triple line (phenolphthalein)
14. Strong and weak acids · `ks4-chemistry-5.4.2.5-strong-weak-acids` · **CH TH only** · calculates
15. The process of electrolysis · `ks4-chemistry-5.4.3.1-electrolysis-principles` · CF CH TF TH · Higher layer (electrons at the electrodes)
16. Electrolysis of molten ionic compounds · `ks4-chemistry-5.4.3.2-electrolysis-molten` · CF CH TF TH · Higher layer (half equations)

Transition metals offers only TF and TH in the picker. Moles, Amounts in equations and Strong and weak acids offer only CH and TH, as monoclonal antibodies did in batch 7 (ORDER code 3 = Higher). Prev/next skip pages a route doesn’t have: on Combined Foundation, Group 7 → Mass changes, Chemical measurements → Oxidation and reduction, pH scale → Electrolysis; on Combined Higher, Group 7 → Mass changes; on Triple Foundation, Chemical measurements → Oxidation and reduction, pH scale → Electrolysis; Triple Higher gets the full order. Higher layers are hidden (not just badged) on CF and TF, and their rail entries disappear with them.

## Page order (every lesson)

Header (AQA ref, route chips, route picker) → Start here (`Ks4Guess`) → video slot → two to four teaching sections, each with a figure and an interaction → on the calculating lessons: equation block (triangle where one exists, one line otherwise), CFIFA (`Ks4Cfifa`), then Step 1 / Step 2 (/ Step 3) (`Ks4Steps`, worked then attempt) → Higher block where there is one → Think again (`Ks4Choice`) → Sort (`Ks4Sort`) → command words → key fact → exam ladder (`Ks4Practice`) → key note → practice set (`Ks4QuizBank`) → end. No examiner tips: none approved.

## Shared blocks

Copied unchanged from the batch-10 delivery (the newest) into `lessons/`: Ks4Triangle, Ks4Guess, Ks4Steps, Ks4Practice, Ks4Chain, Ks4Write, Ks4Chrome, Ks4Cfifa, Ks4Choice, Ks4Sort, Ks4KeyNote, Ks4QuizBank, Ks4End, Ks4Video, ks4-lib.js, ks4-diagrams.js, ks4-theme.css, support.js. No `_ds` inside; pages link `../../_ds/…`.

No block changes this batch. New page-level patterns (not blocks): chemical equations in the template are written with `<sub>`/`<sup>` markup and a drawn inline-SVG arrow (a two-headed one for the reversible arrow); the Higher layer is an `<sc-if value="{{ isHigher }}">` section whose rail entries carry `higher: true` and are filtered out on Foundation; two `Ks4Cfifa` blocks on one page (mass changes: base and Higher; moles: equation 1 and equation 2) with separate `on-open` handlers; a shell filler, an isotope-mix balance, a 3 × 3 displacement grid, an ion builder, a compound picker, and a route-dependent practice set (`F.H ? htBank : baseBank`).

## Rules 1–4

- **Rule 1.** Every opener is “If you had to guess, …?” with exactly two options, built on the brief’s access note: a film poster that proves you wrong; a balloon on a wall; three 10s and a 20; an empty bus; a magnet and a paperclip; a bridge from a metal you can cut with a knife; a fizzy drink on the scales; two kitchen jugs; a dozen eggs and a dozen melons; two eggs per cake; a rusty gate; salt back out of salty water; lemon juice; vinegar or battery acid; dry salt or salt water in a circuit; a positive ion between two electrodes. Titles, scenes and big questions don’t give the answer away. The wrong option’s reply is encouraging and leads into the teaching; on Subatomic particles both options lead into electrons moving, as the brief asks.
- **Rule 2.** Formula triangles where the pack gives one: n = m ÷ Mr (mass changes HT, moles, amounts in equations) and particles = n × Nₐ (moles, Nₐ a fixed cell). Both use `source: 'none'`, so the panel reads “Written out” with no chip; “Learn this one” and “Learn it” appear nowhere. Ar = [Σ(% × mass number)] ÷ 100 is a weighted sum and is shown as one bracketed line, no triangle. Mass of gas = before − after, neutrons = A − Z, electrons = protons − charge, mean/range/half-range, and 10ⁿ are subtractions, sums or powers and are shown as one line each. Percentage uncertainty (extension only, labelled off-spec) has a triangle with the × 100 as its own line.
- **Rule 3.** Every step is taught before it is tested, CFIFA on every calculation (Ks4Cfifa, Ks4Steps, and the ladder’s calc items):
  - Reacting masses (mass changes HT; amounts in equations): Ks4Cfifa teaches Step 1 (n = m ÷ Ar, with a kg → g example), Step 2 (the ratio, wanted ÷ given coefficient) and Step 3 (m = n × Mr) each alone with its own question, then Ks4Steps works all three (4.8 g Mg → 0.2 mol → 0.1 mol O₂ → 3.2 g, MgO 8.0 g; 1.2 g Mg + HCl → 0.1 g H₂) before the attempt (2.4 g Mg; 8.0 g CaCO₃ → 3.52 g CO₂). One method throughout; the pack’s 48 g : 80 g mass-ratio working appears once, as a check at the end of the worked example. On mass changes the base CFIFA (before − after, one kg → g example, one rising reading) sits on all four routes; the Higher CFIFA and Steps sit on CH TH only.
  - Moles: n = m ÷ Mr taught alone (verbatim Al example, 2.7 kg Al → 2700 g → 100 mol as its own worked step, m = n × Mr) with three questions; particles = n × Nₐ taught alone (both directions) with two questions; then two worked Ks4Steps (mass from a particle count; particles from a mass) and an attempt. Standard form is taught in a card with a pick before anything is tested.
  - Chemical measurements: Ks4Cfifa teaches the mean alone (with dm³ → cm³) and half-range alone; Ks4Steps works mean → range → ± range ÷ 2 (24.10, 24.30, 24.20 → 24.20 ± 0.10 cm³), then the attempt has an anomaly to leave out, with the reason given in the equation block.
  - Relative atomic mass: the corrected boron example, a ratio-to-percentages example (Cl 3 : 1 → 75%, 25%) and a find-the-other-abundance example before three questions; the isotope-mix balance shows Ar lean towards the commoner isotope.
  - pH ×10: worked (pH 1 vs pH 3 → 100) on both pH-scale (HT block) and strong and weak acids (Ks4Cfifa with two examples and two questions) before any pupil does one.
  - Subatomic particles: neutrons = A − Z and electrons = protons − charge are two separate subtractions in a worked card (²⁷₁₃Al³⁺ → 13 p, 14 n, 10 e), then the ion builder; no CFIFA, as the prompt says.
- **Rule 4.** Ladder 2 · 2 · 2 · 1 on every page and route; rung 4 is one 4- or 6-mark answer (6 on lessons 1, 5, 6, 7, 8, 10, 12, 14, 16; 4 elsewhere). Practice set: five per route on every page. Banks differ by route only where a verbatim item is HT-only: mass changes, oxidation and reduction, pH scale, electrolysis principles and electrolysis molten swap one or two items between CF/TF and CH/TH; the ladder is the same on all routes everywhere.

## Quiz items (practice set, five per route)

“Rebuilt” = same stem, options and key, with FLAGS’ corrected explanations. Options are shuffled by `KS4.item()`.

- 1 Model of the atom: q1 q2 verbatim + 3 new (plum pudding description; Chadwick and the 20 years; Bohr’s change).
- 2 Subatomic particles: q1 q2 verbatim + 3 new (²⁷₁₃Al³⁺ counts; neutrons in ⁵⁶₂₆Fe; radius statement).
- 3 Relative atomic mass: q1 rebuilt (wx1 extended per F5), q2 verbatim + 3 new (the missing bracket; neutrons in Cl-37; what the top number in a periodic-table box is).
- 4 Electronic structure: q1 q2 verbatim + 3 new (calcium 2,8,8,2; helium in Group 0; lowest level first).
- 5 Group 7: q1 q3 verbatim, q2 rebuilt (wx1 replaced per F4) + 2 new (boiling-point trend; HCl covalent).
- 6 Transition metals: q1 verbatim, q2 rebuilt (wx2 replaced per F1) + 3 new (coloured compounds; Fe²⁺/Fe³⁺; halogens row).
- 7 Mass changes: q1 q2 verbatim + 3 new on CF TF (before − after; sealed flask; particle explanation); CH TH swap the particle item for a 2 : 1 ratio item.
- 8 Chemical measurements: 5 new (mean ± half range; anomaly; precise; why repeats; apparatus). q1 not used in the core (CM-F2; its calculation is the extension); q2 not used (CM-F3).
- 9 Moles: q1 verbatim, q2 rebuilt (wx2 rewritten to address “particle count × Mr”, MOL-F1) + 3 new (kg → g; mass → particles chain; atoms in a mole of water).
- 10 Amounts in equations: q1 verbatim + 4 new (masses in an equation; three-step Mg → MgO; Mr(H₂) = 2; method order). q2 not used (AIE-F2).
- 11 Oxidation and reduction: CF TF 5 new oxygen-based; CH TH q2 verbatim + 3 of those + a displacement ionic-equation item. q1 not used (OXR-F2).
- 12 Salts: q2 verbatim + 4 new (why excess, replacing q1 per SN-F5; name the salt; RP order; carbonate in excess).
- 13 pH scale: CF TF q2 verbatim + 4 new (UI colour; ionic equation; probe vs UI; the curve); CH TH q1 q2 verbatim + 3 of those.
- 14 Strong and weak acids: q1 q2 verbatim + 3 new (pH 1 vs 4; a weak acid; excess magnesium).
- 15 Electrolysis principles: CF TF 5 new (why molten or dissolved, replacing q1 per EP-F2; which ion where; electrolyte; what carries the current; cathode); CH TH q2 verbatim + 4 of those.
- 16 Electrolysis molten: q1 q2 verbatim + 3 new on CF TF (predict both products for KI; anode observation; the general rule); CH TH swap the rule item for a complete-the-half-equation item.

## Science flags

**G · Global**
- G1. Formulas in the templates use real `<sub>`/`<sup>` markup (H₂O, Cl₂, Pb²⁺, Br⁻, CH₃COOH, ²⁷₁₃Al³⁺ as a stacked nuclear symbol); chemical arrows in templates are drawn inline SVG, never typed. JS-built text (quiz, ladder, sort, key note, figures) uses Unicode sub/superscripts; figures render them in the figure serif. Verbatim items keep their typed arrows (G2 as before).
- G2. Live-site pointers (Atoms, elements and compounds; Relative formula mass; Using moles in calculations; Conservation of mass; Titrations; Percentage yield; Atom economy) are written as `/ks4/<slug>` in `FILE`. Code to re-point to the live URLs; batch-2/3 `endConnects` that forward-link to `moles`, `amounts-in-equations`, `mass-changes-reactions` and `salts-neutralisation` now have targets.
- G3. Links to earlier batches use `../../KS4 Batch 4/…` and `../../KS4 Batch 5/…` (periodic table, Group 0, metals and non-metals, reactivity series, extraction of metals, and the two physics atom lessons).
- G4. One job per spec point; siblings get a pointer: alpha scattering as an investigation → physics Development of the atomic model (from lesson 1); counting p/n/e → Subatomic particles (from Relative atomic mass); Group 0 → its own lesson (from Electronic structure); electron-transfer redox → Oxidation and reduction (from Group 7, electrolysis); the law itself → Conservation of mass (from Mass changes); % by mass → Relative formula mass and limiting reactants → Using moles in calculations (from Moles); yield and atom economy → their own lessons (from Amounts in equations); titration method → Titrations (from Salts, pH scale); extraction reasons → Extraction of metals (from both electrolysis lessons); strong/weak and the ×10 → Strong and weak acids (from pH scale).
- G5. Every figure is mine, in the ks4-diagrams style (D.atom is reused for shells); nothing was ported from `figlib` or `ks3_art`. The diagram README’s “still needed” list is covered: weighted-mean balance, transition-metal contrast and colour strip, apparatus with meniscus close-ups, one-mole piles, coefficient bars, electron-transfer pair, RP sequence, full vs partial ionisation, plus the cell and crucible.
- G6. Made-up teaching data, labelled on each page: balance readings, titres and temperature rises, the hook circuit, the pH curve shape, the 2 × 2 beaker set.
- G7. Off-spec detail in the sources left out: line spectra and electron jumps (F4), mass spectrometry (RAM-F2), London dispersion (G7-F2), electron affinity (G7-F5), 3d/4s and oxidation-state calculations (TM-F2), Mn⁴⁺/Mn⁷⁺ ions (TM-F4), percentage uncertainty as core (CM-F2), the pre-2019 mole definition (MOL-F3), yield and atom economy (AIE-F1, F2), oxidising/reducing agents and the blast furnace (OXR-F2, F5), precipitation as a preparation (SN-F3), litmus and the “why sharp” paragraph (PH-F4), dilution shifting the weak-acid equilibrium and conjugate base (SWA-F2, F4), electroplating, refining and brine (EP-F3), AN OX / RED CAT mnemonic not used.
- G8. Every balanced equation and half equation was checked for atoms and charge: 2Mg + O₂ → 2MgO; CuO + H₂ → Cu + H₂O; 2CuO + C → 2Cu + CO₂; 2Fe₂O₃ + 3C → 4Fe + 3CO₂; Fe₂O₃ + 3CO → 2Fe + 3CO₂; Mg + 2HCl → MgCl₂ + H₂; H₂ + Cl₂ → 2HCl; Cl₂ + 2NaBr → 2NaCl + Br₂ (and KI forms); Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂; Br₂ + 2I⁻ → 2Br⁻ + I₂; Mg + Cu²⁺ → Mg²⁺ + Cu; Mg + 2H⁺ → Mg²⁺ + H₂; Zn + Cu²⁺ → Zn²⁺ + Cu; CuO + H₂SO₄ → CuSO₄ + H₂O; H⁺ + OH⁻ → H₂O; 2NaCl → 2Na + Cl₂; PbBr₂ → Pb + Br₂; Na → Na⁺ + e⁻; Mg → Mg²⁺ + 2e⁻; Cl₂ + 2e⁻ → 2Cl⁻; O₂ + 4e⁻ → 2O²⁻; Pb²⁺ + 2e⁻ → Pb; 2Br⁻ → Br₂ + 2e⁻; Na⁺ + e⁻ → Na; 2Cl⁻ → Cl₂ + 2e⁻; Zn²⁺ + 2e⁻ → Zn; HCl → H⁺ + Cl⁻; CH₃COOH ⇌ CH₃COO⁻ + H⁺.

**1 · Model of the atom**
- 1.1 Dates: electron 1897, plum pudding about 1904, nucleus 1911, neutrons 1932 (F1); the timeline text uses the spec’s words for each step.
- 1.2 “Showed atoms contain smaller particles, so they can be divided” (F2); plum pudding is a ball of positive charge; back-scattered alphas were repelled; the conclusion is “mass concentrated at the centre, nucleus charged” (F3).
- 1.3 Bohr taught as the spec sentence only; no line spectra, no electron jumps (F4). Protons from subdividing the nuclear charge and Chadwick’s neutrons about 20 years later are the last two timeline steps (F5).
- 1.4 Built as a PROCESS (chain of models); scattering is one evidence card with a three-row observation → conclusion classifier.

**2 · Subatomic particles**
- 2.1 “Atoms are made of three types of particle” with the hydrogen-1 exception (F1). “The radius of a nucleus is less than 1/10 000 of that of the atom” (F2).
- 2.2 Ion formation in words and counts on all routes; the e⁻ half equations are a Higher block with Cl₂ and O₂ written correctly (F3).
- 2.3 ²⁷₁₃Al³⁺ → 13 p, 14 n, 10 e is the worked case, then the builder covers Na, Mg²⁺, Cl⁻, O²⁻, Al³⁺ (F4).
- 2.4 Electron mass “very small (about 1/2000 of a proton)” (F5).

**3 · Relative atomic mass**
- 3.1 The FIFA’s Insert line is shown corrected, [(20 × 10) + (80 × 11)] ÷ 100, with a note that the unbracketed line equals 208.8; the bracket is also the Think again and a bank item (F1).
- 3.2 No HT layer; no mass spectra; the Ar calculation on all four routes (F2). “Often not a whole number”, with C 12, O 16, Na 23 as whole-number examples (F3).
- 3.3 The nuclear symbol and the periodic-table box are drawn side by side and named differently (F4). q1’s wx1 extended with “different atomic numbers would make them different elements” (F5).
- 3.4 Ladder calc items accept ±0.15 on Ar to allow for rounding.

**4 · Electronic structure**
- 4.1 No HT layer; everything on all four routes (F1). “Full outer shell: 8, except helium (2)” (F2).
- 4.2 Both forms taught: numbers with commas (2,8,1; dots accepted) and the shell diagram, which the filler draws for any of nine elements after the pupil has committed to the number form (F3). The page says groups are numbered 1–7 and 0 (F4).

**5 · Group 7**
- 5.1 Boiling points only in the chart: −188, −34, 59, 184 °C (F1). “Intermolecular forces increase with the size of the molecules”; relative molecular mass named (F2).
- 5.2 With non-metals, covalent molecular compounds: H₂ + Cl₂ → 2HCl (F3). q2 used with the replacement wx1 (F4).
- 5.3 Astatine prediction on all routes; the HT layer is the ionic equation Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂ with chlorine reduced and bromide oxidised, linking to Oxidation and reduction (F5).

**6 · Transition metals**
- 6.1 q2 used with the replacement wx2: platinum in catalytic converters; the Haber process uses iron (F1). No HT layer; TF and TH get the same page (F2).
- 6.2 A halogens row (sodium burns in chlorine to white sodium chloride; hot iron wool reacts less vigorously, orange-brown iron(III) chloride); the six spec metals; zinc never used as typical (F3).
- 6.3 “Ions with different charges” with Fe²⁺/Fe³⁺ and Cu⁺/Cu²⁺; manganate(VII) and dichromate appear only as coloured compounds; “oxidation state” not used (F4).

**7 · Mass changes**
- 7.1 Magnesium burning is the increase example only; it never appears under decrease (F1).
- 7.2 The moles prediction and the pack’s FIFA numbers are a Higher block on CH TH, taught by the three-step method; CF TF get the base CFIFA (before − after) (F2).
- 7.3 The particle explanation for both directions is taught in the cards and demanded in the 6-mark rung (F3).
- 7.4 q2 used verbatim; the rusting equation is not repeated in teaching text (F4). Design’s own text writes Ar(Mg) (F5).

**8 · Chemical measurements**
- 8.1 Mean ± half the range is the lesson’s core and its Step 1/2/3 (F1). Percentage uncertainty is a dashed, labelled extension block with the verbatim FIFA; never tested in the core (F2).
- 8.2 Meniscus: read the bottom at eye level on both; the direction of the error depends on which way the scale runs; the figure shows a cylinder scale running up and a burette scale running down (F3).
- 8.3 WS 3.7’s four definitions word for word; “reliability” not used (F4). Pipette for one fixed volume, burette for a variable volume (F5).

**9 · Moles**
- 9.1 q2 rebuilt with a new wx2 addressing “particle count × Mr” (F1). “Formula units” for NaOH and NaCl (F2). The spec sentence for the mass of a mole; no carbon-12 definition (F3).
- 9.2 % by mass is a pointer to Relative formula mass, not taught (F4). The corrected Convert line of the verbatim FIFA is used (F5).

**10 · Amounts in equations**
- 10.1 Atom economy and percentage yield left off the page and linked; the wrong atom-economy formula never appears; q2 not used (F1, F2).
- 10.2 One numbered method (Step 1 moles of given, Step 2 ratio, Step 3 mass of wanted) used identically in the CFIFA, the worked example, the attempt, the Sort and the ladder (F3).
- 10.3 Masses in a balanced equation taught before the chain: 48 g + 32 g → 80 g, with a pick on N₂ + 3H₂ → 2NH₃ (F4). F5 moot (q2 not used).

**11 · Oxidation and reduction**
- 11.1 Oxygen definitions on all routes; electron definitions, OIL RIG, the ionic equation and q2 in a Higher block on CH TH; the header reads 5.4.1.1, 5.4.1.3 (+ 5.4.1.4 Higher) (F1).
- 11.2 Oxidising and reducing agents never appear; q1 not used (F2). 2Mg + O₂ → 2MgO (F3). Chlorine never as a single atom; the HT example is Mg + Cu²⁺ → Mg²⁺ + Cu, plus Mg + 2H⁺ → Mg²⁺ + H₂ as the metals-and-acids line (F4).
- 11.3 Carbon reducing a metal oxide is 2CuO + C → 2Cu + CO₂ (and 2Fe₂O₃ + 3C → 4Fe + 3CO₂ in the bank); no blast furnace, manganate or peroxide (F5). Oxygen-based items on every route; an ionic-equation item on CH TH (F6).

**12 · Salts**
- 12.1 Labelled “Combined RP8 · Chemistry RP1” everywhere; “RP3” never shown (F1).
- 12.2 Titration is a Triple-only block that points to Titrations; CF CH see the excess-solid method only (F2). Precipitation not taught (F3).
- 12.3 The last step is “heat on a water bath until crystals start to form, leave to cool, pat dry”; boiling dry is the Think again (F4).
- 12.4 q1 replaced by a “why excess?” item keyed to all the acid reacting (F5). q2 verbatim (F6). Carbonates: salt + water + carbon dioxide; “add until the fizzing stops and solid is left” (F7).

**13 · pH scale**
- 13.1 The ×10 factor and q1 are a Higher block on CH TH; base routes get below 7 / 7 / above 7 and “lower pH, more acidic”; the full treatment is pointed to Strong and weak acids (F1).
- 13.2 “Below 7 / exactly 7 / above 7” everywhere including the chart (F2). “Dilute hydrochloric acid about 1”, coffee about 5 (F3).
- 13.3 Core is universal indicator and the probe; the curve is shown as data to read; no “why sharp” paragraph; litmus only in a distractor; phenolphthalein one Triple line (F4).
- 13.4 H⁺(aq) + OH⁻(aq) → H₂O(l) taught on all four routes (F5). q2 verbatim (F6).

**14 · Strong and weak acids**
- 14.1 Reactions with magnesium re-cut to “equal volumes, same concentration, excess magnesium: same total hydrogen, slower” (F1).
- 14.2 Dilution of weak acids not taught (F2). The ×10 statement is taught with the pack’s own numbers (pH 1 vs 3 → 100) in CFIFA (F3).
- 14.3 “H⁺ ions and negative ions”; HF not used; the spec’s named acids lead (F4). q1 verbatim.

**15 · Electrolysis principles**
- 15.1 Electron gain/loss, reduction/oxidation and q2 are a Higher block on CH TH; CF TF learn which ions move where and that they are discharged as elements (F1).
- 15.2 q1 replaced by a “why molten or dissolved?” item (F2). Electroplating, refining and brine not mentioned; extraction of reactive metals is the one use, pointed to its lesson (F3).
- 15.3 “Metal coats the cathode, or gas bubbles off” wording; nothing “deposited” as a gas (F4). “Ions carry the charge in the liquid; electrons in the wires” on all routes (F5).

**16 · Electrolysis molten**
- 16.1 No RP badge; lead bromide is a teacher demonstration in a fume cupboard with zinc chloride named as the safer alternative; the aqueous RP is named as Combined RP9 = Chemistry RP3 and left to its lesson (F1).
- 16.2 Half equations are a Higher block on CH TH; CF TF get the products and the overall equations 2NaCl → 2Na + Cl₂ and PbBr₂ → Pb + Br₂ (F2). Prediction taught on all four routes; the carbon reason is a pointer to Extraction of metals (F3).
- 16.3 Design’s own text names only Pb²⁺ and Br⁻ for lead bromide; q2 verbatim (F4). q1 verbatim; its “reduced” is HT framing but the answer is base (F5).

## Not done / for Code

- Videos: `KS4.VIDEOS` is empty, so the slot stays hidden.
- No examiner tips: none approved.
- Live-lesson pointers are `/ks4/<slug>` placeholders (G2).
- Dark mode uses the existing remap; SVG plates stay cream.
