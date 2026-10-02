# KS4 Batch 16 — Design input pack

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
| 1 | Mass Number, Atomic Number and Isotopes | `mass-number-isotopes` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.1.2-mass-number-isotopes.md` |
| 2 | Nuclear Equations | `nuclear-equations` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.2.2-nuclear-equations.md` |
| 3 | Half-Lives and Radioactive Decay | `half-lives` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.2.3-half-lives.md` |
| 4 | Radioactive Contamination | `radioactive-contamination` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.2.4-radioactive-contamination.md` |
| 5 | Background Radiation | `background-radiation` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.3-background-radiation.md` |
| 6 | Uses of Nuclear Radiation | `uses-of-nuclear-radiation` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.4-uses-of-nuclear-radiation.md` |
| 7 | Nuclear Fission | `nuclear-fission` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.5.1-nuclear-fission.md` |
| 8 | Nuclear Fusion | `nuclear-fusion` | Phys · atomic-structure | `04-checked-science-source/physics-6.4.5.2-nuclear-fusion.md` |
| 9 | Scalar and Vector Quantities | `scalar-vector-quantities` | Phys · forces | `04-checked-science-source/physics-6.5.1.1-scalar-vector-quantities.md` |
| 10 | Contact and Non-Contact Forces | `contact-noncontact-forces` | Phys · forces | `04-checked-science-source/physics-6.5.1.2-contact-noncontact-forces.md` |
| 11 | Gravity | `gravity` | Phys · forces | `04-checked-science-source/physics-6.5.1.3-gravity.md` |
| 12 | Resultant Forces | `resultant-forces` | Phys · forces | `04-checked-science-source/physics-6.5.1.4-resultant-forces.md` |
| 13 | Resolving Forces and Vector Diagrams | `resolving-forces` | Phys · forces | `04-checked-science-source/physics-6.5.1-resolving-forces.md` |
| 14 | Free Body Diagrams | `free-body-diagrams` | Phys · forces | `04-checked-science-source/physics-6.5.1-free-body-diagrams.md` |
| 15 | Work Done and Energy Transfer | `work-done-energy-transfer` | Phys · forces | `04-checked-science-source/physics-6.5.2-work-done-energy-transfer.md` |
| 16 | Forces and Elasticity | `forces-elasticity` | Phys · forces | `04-checked-science-source/physics-6.5.3-forces-elasticity.md` |

True routes, layers and families are in each lesson's entry below; they come from the AQA specification's own labels, checked by an examiner, and where they differ from what the site ships today the entry says so.

## Per lesson

### 1. Mass Number, Atomic Number and Isotopes
`mass-number-isotopes` · Physics / atomic structure · AQA refs (8464 6.4.1.2; 8463 4.4.1.2) · true routes CF CH TF TH

**Family:** MODEL (BATCH-PLAN said CLASSIFY) — one structure, the notation ᴬ_Z X, gives every count (p, n, e) and decides isotope / different element / ion; the isotope sort follows from the model rather than standing alone.

**Flagship (a suggestion, not a spec):** a nuclide card where the pupil changes protons or neutrons and sees A, Z, the element and "isotope of…" update.

**Route layers:** none — all base.

**Required practical:** none.

**Calculations:**
- Particle counts from notation: protons = Z; neutrons = A − Z; electrons = Z (neutral atom). **Chains equations? no.** Units: none (counts) — Convert step is always "nothing to convert". Base.

**Equations that need formula triangles (rule 2):** neutrons = A − Z — Learn it (not on either sheet). An addition relationship (A = Z + N), not a product, so a cover-triangle does not apply as drawn; if Design wants the same visual, A on top, Z | N below, covering by subtraction.

**Misconceptions to confront:**
- "Mass number is the number of neutrons." → A = protons + neutrons (6.4.1.2).
- "Different mass number means a different element." → The atomic number (protons) decides the element (6.4.1.2).
- "Neutrons = A + Z." → Neutrons = A − Z.
- "An ion is an isotope." → Ions differ in electrons; isotopes differ in neutrons; A and Z are unchanged by losing outer electrons (6.4.1.2).
- "Isotopes are a different substance chemically." → Same protons and electrons, same element.

**"Start here" access note (rule 1):** two coins that look the same but one is heavier — still the same coin? (same identity, different mass).

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1, q2). None unusable. The bank must be topped up by Design to the batch's fixed size.

**Diagrams:** see `05-diagram-library/README.md` (#1). Must draw: ᴬ_Z X notation with A top-left, Z bottom-left (theory 1's glyph is garbled — F1); `isotope_notation()` to teach, `nuclide()` in questions; an isotope trio (¹²C, ¹³C, ¹⁴C) showing neutrons only change.

**Examiner tip:** none approved.

---

### 2. Nuclear Equations
`nuclear-equations` · Physics / atomic structure · AQA refs (8464 6.4.2.2; 8463 4.4.2.2) · true routes CF CH TF TH

**Family:** QUANTITATIVE — the spec limits the skill to "balancing the atomic numbers and mass numbers"; it is an arithmetic balance, done every time.

**Flagship (a suggestion, not a spec):** a balance where the pupil fills the daughter's A and Z and both rows (top, bottom) must sum equal before the equation locks.

**Route layers:** none — all base.

**Required practical:** none.

**Calculations:**
- α decay: daughter A = parent A − 4, Z = parent Z − 2. **Chains equations? no.** Units: none. Base.
- β decay: daughter A = parent A, Z = parent Z + 1. **Chains equations? no.** Units: none. Base. Needs its own worked example (only α is worked in the source — F2; use ¹⁴₆C → ¹⁴₇N + ⁰₋₁e).
- γ: no change. Base.

**Equations that need formula triangles (rule 2):** none — the change rules are additions/subtractions, not products. Not on either sheet (Learn it).

**Misconceptions to confront:**
- "β decay lowers the mass number like α." → β: mass unchanged, charge +1 (6.4.2.2).
- "Subtract 2 from the top number for α." → α takes 4 off A and 2 off Z (6.4.2.2).
- "The −1 on the β symbol means Z goes down." → Z goes up by 1, so the bottom row balances: Z = (Z+1) + (−1).
- "γ makes a new element." → γ changes neither mass nor charge (6.4.2.2).
- "I must name the new element." → Not required; only balancing is (6.4.2.2).

**"Start here" access note (rule 1):** a scales/balance — if 4 is taken off one side, must it reappear on the other for the totals to match?

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1, q2). None unusable. Never set "name the daughter element" (F1). The bank must be topped up by Design to the batch's fixed size.

**Diagrams:** see `05-diagram-library/README.md` (#2). Must draw: a complete decay-equation figure (parent → daughter + particle, A and Z balanced either side) for α and for β — genuinely missing; build from `nuclide()` cards.

**Examiner tip:** none approved.

---

### 3. Half-Lives and Radioactive Decay
`half-lives` · Physics / atomic structure · AQA refs (8464 6.4.2.3; 8463 4.4.2.3, 4.4.3.2) · true routes CF CH TF TH

**Family:** QUANTITATIVE — determining a half-life from data or a graph, and finding what remains, carries the concept; randomness is the explanation behind it.

**Flagship (a suggestion, not a spec):** a large sample of nuclei decaying at random with a live activity–time curve; the pupil marks each halving and finds it takes the same time.

**Route layers:**
- Higher: "calculate the net decline, expressed as a ratio, in a radioactive emission after a given number of half-lives" — 8464 6.4.2.3 (HT only) / 8463 4.4.2.3 (HT only). This is (½)ⁿ and the FIFA's Step 2 as written.
- Triple: "explain why the hazards associated with radioactive material differ according to the half-life involved" — 8463 4.4.3.2 (physics only); choosing isotopes for uses — 8463 4.4.3.3 (physics only); background subtraction — 8463 4.4.3.1 (physics only). The source's `higher` field is this triple content, not HT (F2).

**Required practical:** none.

**Calculations:**
- Remaining activity after a time: n = t ÷ T½, then halve n times (base) / N = N₀ × (½)ⁿ (HT). **Chains equations? yes** — Step 1 n = total time ÷ half-life; Step 2 halve n times (HT: × (½)ⁿ). Units: t and T½ in the SAME unit (convert min ↔ h ↔ days if they differ; SI never needed). Base (Step 2 as a ratio is HT).
- Determine the half-life from data or a graph. **Chains equations? yes** (from data) — Step 1 count the halvings (800 → 100 = 3); Step 2 T½ = t ÷ n. From a graph: read the time for the value to halve (one step). Units: as given. Base.
- Net decline as a ratio: fraction remaining (½)ⁿ; fraction decayed 1 − (½)ⁿ. **Chains equations? no.** Units: none. HT (F6).
- Both chained calculations need a Step 1 / Step 2 worked example before pupils try one (F4). CFIFA's conversion example: mixed units (e.g. T½ = 15 min, t = 1 h).

**Equations that need formula triangles (rule 2):**
- n = t ÷ T½ — Learn it (not on either sheet). Triangle: t on top; n | T½ below.
- N = N₀ × (½)ⁿ — Learn it, HT. Triangle: N on top; N₀ | (½)ⁿ below. The power (½)ⁿ is its own line (work it out first, or halve n times).

**Misconceptions to confront:**
- "After two half-lives it's all gone." → Each half-life halves what is left: ½ then ¼ (6.4.2.3).
- "Halve from the original each time." → Halve the current value.
- "Heating it up speeds decay / changes the half-life." → Half-life is fixed for an isotope; decay is random and unaffected.
- "We can say which atom decays next." → Decay is random; only the large-sample proportion is predictable (6.4.2.3).
- "A short half-life means it's safer forever / a long one is more dangerous right now." → Short = high activity briefly; long = low activity for a long time (8463 4.4.3.2, triple).

**"Start here" access note (rule 1):** a full bag of popcorn kernels popping at random — can you tell which kernel pops next, or roughly how many will have popped in a minute?

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1 Apply, q2 Explain). None unusable; q1 wx3 imprecise (F5). The bank must be topped up by Design to the batch's fixed size, with HT ratio items tagged Higher and half-life-choice items tagged Triple.

**Diagrams:** see `05-diagram-library/README.md` (#3). Must draw: a decay curve with successive halvings marked at equal time steps — `half_life_curve()` covers it.

**Examiner tip:** none approved.

---

### 4. Radioactive Contamination
`radioactive-contamination` · Physics / atomic structure · AQA refs (8464 6.4.2.4; 8463 4.4.2.4) · true routes CF CH TF TH

**Family:** CONTRAST — the spec's demand is "compare the hazards associated with contamination and irradiation": two situations, one discriminating difference (does the source stay with you?).

**Flagship (a suggestion, not a spec):** one source, two scenes — dust on/in the body vs standing near a sealed source — where the pupil moves the person away and predicts whether exposure stops, for α, β and γ.

**Route layers:** none — all base.

**Required practical:** none.

**Calculations:** none.

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Food zapped with radiation becomes radioactive." → "The irradiated object does not become radioactive." (6.4.2.4)
- "Contamination and irradiation are the same thing." → Contamination = radioactive atoms on/in you, decaying; irradiation = exposure, stops when you leave (6.4.2.4).
- "Alpha is harmless because paper stops it." → Inside the body α is the most hazardous — highly ionising, all energy deposited locally (6.4.2.4, 6.4.2.1).
- "A lead apron stops everything." → Lead reduces γ; distance, time and shielding together reduce dose.
- "Research on radiation harm can be kept private." → Findings must be published and peer reviewed (6.4.2.4, WS 1.6).

**"Start here" access note (rule 1):** standing near a bonfire vs getting the ash on your clothes — which one stops when you walk away?

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1, q2 — q2 is X-rays, an irradiation context but not a radioactive source, F2). None unusable. The bank must be topped up by Design to the batch's fixed size, including an "irradiated object is not radioactive" item.

**Diagrams:** see `05-diagram-library/README.md` (#4). Must draw: a contamination-vs-irradiation contrast (source on/in a person vs person at a distance from a source) — genuinely missing; `radiation_penetration()` supports the hazard-by-type strand.

**Examiner tip:** none approved.

---

### 5. Background Radiation
`background-radiation` · Physics / atomic structure · AQA refs (8463 4.4.3.1; no 8464 equivalent) · true routes TF TH

**Family:** CLASSIFY (BATCH-PLAN said QUANTITATIVE) — the only calculation is one subtraction; the spec's demand is sorting sources (natural / man-made) and judging how location and occupation change the dose.

**Flagship (a suggestion, not a spec):** a UK-dose bar or pie the pupil rebuilds by dragging sources into natural / man-made, then sees the total change for a pilot, a radiographer and a Cornwall householder.

**Route layers:**
- Whole page: "Hazards and uses of radioactive emissions and of background radiation (physics only)" — 8463 4.4.3 / 4.4.3.1. No HT layer: the source's `higher` field is not HT and must show on TF too (F2).

**Required practical:** none.

**Calculations:**
- Corrected count rate = measured count rate − background count rate. **Chains equations? no.** Units: both rates in the same unit (counts/min or counts/s). Triple base.
- Dose units: 1000 mSv = 1 Sv. **Chains equations? no.** Convert mSv ↔ Sv. Triple base.

**Equations that need formula triangles (rule 2):** corrected = measured − background — Learn it (not on the 8463 sheet); a subtraction, so no cover-triangle.

**Misconceptions to confront:**
- "Background only exists near power stations." → It is around us all the time, mostly natural (8463 4.4.3.1).
- "Add the background on." → Subtract it from the measured count rate.
- "The detector reading is the source's activity." → It is a count rate; activity is decays per second in the source (8463 4.4.2.1).
- "Everyone gets the same dose." → Dose depends on location and occupation (8463 4.4.3.1).
- "Medical X-rays and fallout are the biggest part." → Radon is about half of the UK average.

**"Start here" access note (rule 1):** is there any radiation in your bedroom right now, with nothing radioactive in it — yes or no? (Granite worktops, bananas and flights are everyday hooks.)

**Practice (rule 4):** TF and TH: 1 verbatim item usable (q2; prefer corrected wording, F4). q1 not usable as written (F1 — "corrected activity" must read "corrected count rate"). The bank must be topped up by Design to the batch's fixed size. Do not test recall of the unit "sievert" (spec).

**Diagrams:** see `05-diagram-library/README.md` (#5). Must draw: a UK background-sources chart (radon ≈ 50 %, ground/buildings ≈ 13–15 %, cosmic ≈ 10–12 %, food ≈ 10 %, medical ≈ 15 %, other man-made < 1 %) — genuinely missing; a pie/bar engine exists.

**Examiner tip:** none approved.

---

### 6. Uses of Nuclear Radiation
`uses-of-nuclear-radiation` · Physics / atomic structure · AQA refs (8463 4.4.3.3, 4.4.3.2; base supporting 8464 6.4.2.1) · true routes TF TH

**Family:** CLASSIFY — choose the radiation type and half-life for a use, and say why; the spec adds evaluating perceived risk from data.

**Flagship (a suggestion, not a spec):** a decision instrument for medical jobs (tracer in an organ, external beam, internal thyroid treatment): pick type and half-life, see whether it reaches the detector/tissue and what dose remains.

**Route layers:**
- Whole page: medical uses "for exploration of internal organs, and for control or destruction of unwanted tissue"; "evaluate the perceived risks…" — 8463 4.4.3.3 (physics only); half-life choice — 8463 4.4.3.2 (physics only). No HT layer: the source's `higher` field is not HT and must show on TF too (F1).
- Industrial uses (smoke detectors, gauges) are base applications of 8464 6.4.2.1, already taught in batch 5's `radioactive-decay` — review only here (F5).

**Required practical:** none.

**Calculations:** none on this page (activity remaining belongs to `half-lives`).

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Tracers use alpha because it's the strongest." → α would not leave the body and would do the most damage inside; tracers emit γ (8463 4.4.3.3).
- "A long half-life tracer is better — it lasts longer." → Short half-life: activity falls quickly, lower dose (8463 4.4.3.2).
- "Gamma is the most ionising." → γ is the least ionising, most penetrating (6.4.2.1).
- "Any radiation use is too risky." → Risk is judged against data and benefit (8463 4.4.3.3).
- "The patient becomes radioactive after radiotherapy beams." → An irradiated object does not become radioactive (6.4.2.4).

**"Start here" access note (rule 1):** a doctor wants to see inside you without cutting — should what they send in come out the other side, or stay in?

**Practice (rule 4):** TF and TH: 2 verbatim items usable (q1 smoke detector — review; q2 tracer). None unusable. The bank must be topped up by Design to the batch's fixed size, weighted to medical uses and a risk-from-data item (F2).

**Diagrams:** see `05-diagram-library/README.md` (#6). Must draw: a uses-by-property figure (tracer/γ + short half-life; external beams crossing at a tumour; internal thyroid source) — genuinely missing; industrial row optional.

**Examiner tip:** none approved.

---

### 7. Nuclear Fission
`nuclear-fission` · Physics / atomic-structure · AQA refs (8464 —; 8463 4.4.4.1) · true routes TF TH

**Family:** PROCESS — the spec is a sequence (neutron absorbed → nucleus splits → 2–3 neutrons + gamma + KE → chain reaction), and asks pupils to draw/interpret it.

**Flagship (a suggestion, not a spec):** a chain-reaction stepper where the pupil adds or removes control rods and watches the neutron count per generation steady, grow or die.

**Route layers:**
- Whole page: "4.4.4 Nuclear fission and fusion (physics only)" — 8463 4.4.4.1. No HT layer: the source's `higher` field is not HT (NUCLEAR-FISSION-F4) — controlled vs uncontrolled chain reaction is TF core.
- Base cross-reference: nuclear power advantages/disadvantages — 8464 6.1.3 / 8463 4.1.3.

**Required practical:** none.

**Calculations:** none in the spec. (Balancing the fission equation's mass and atomic numbers is 8463 4.4.2.2 practice, not a CFIFA calculation; chains equations? no.) E = mc² is off-spec — do not teach as a calculation.

**Equations that need formula triangles (rule 2):** none. ("E = mc²" in `equations` is off-spec and on neither sheet — no triangle, no chip.)

**Misconceptions to confront:**
- "The nucleus just splits on its own." → Spontaneous fission is rare; it usually absorbs a neutron first (4.4.4.1).
- "Fission is the same as alpha decay." → Fission gives two roughly equal nuclei plus 2–3 neutrons and gamma rays (4.4.4.1).
- "Control rods slow the neutrons down." → Control rods absorb neutrons; the moderator slows them.
- "A chain reaction always means an explosion." → In a reactor it is controlled; only an uncontrolled one is a weapon (4.4.4.1).
- "The energy comes from breaking chemical bonds." → It is nuclear; all the fission products move off with kinetic energy (4.4.4.1).

**"Start here" access note (rule 1):** a row of dominoes where one knocks over two — does the toppling die out or spread?

**Practice (rule 4):** TF TH: 2 verbatim items usable — q1 as a spec rung; q2 as a stretch item only (mass defect is beyond 4.4.4.1, NUCLEAR-FISSION-F3). None unusable. The bank must be topped up by Design to the batch's fixed size, including items on gamma rays/KE of products and on reading a chain-reaction diagram.

**Diagrams:** see `05-diagram-library/README.md` (#7). Must draw: a fission event (neutron in → two daughter nuclei + 2–3 neutrons + gamma) and a chain-reaction diagram — spec skill "draw/interpret diagrams", nothing in the library.

**Examiner tip:** none approved.

---

### 8. Nuclear Fusion
`nuclear-fusion` · Physics / atomic-structure · AQA refs (8464 —; 8463 4.4.4.2) · true routes TF TH

**Family:** CONTRAST — the spec is two sentences, and their teaching weight is the contrast with fission (join vs split, light vs heavy nuclei, both convert mass to energy).

**Flagship (a suggestion, not a spec):** a side-by-side fission | fusion board where the pupil drags nuclei together or apart and sorts the shared and different features.

**Route layers:**
- Whole page: "4.4.4 Nuclear fission and fusion (physics only)" — 8463 4.4.4.2. No HT layer: the source's `higher` field is not HT and its content is off-spec (NUCLEAR-FUSION-F4).
- Fusion in stars: 8463 4.8.1.2 (physics only) — same routes.

**Required practical:** none.

**Calculations:** none in the spec. Chains equations? no. (Checking the D-T equation balances is 8463 4.4.2.2 practice.)

**Equations that need formula triangles (rule 2):** none. The D-T reaction in `equations` is a nuclear equation, not a formula.

**Misconceptions to confront:**
- "Fusion splits atoms." → Fusion joins two light nuclei into a heavier one (4.4.4.2).
- "Nuclear power stations use fusion." → Every working power station uses fission; fusion is still experimental.
- "The energy appears from nowhere." → Some of the mass is converted into energy of radiation (4.4.4.2).
- "Fusion gives more energy per reaction than fission." → Per reaction fission gives more (≈ 200 MeV vs ≈ 18 MeV); per kilogram of fuel fusion gives more.

**"Start here" access note (rule 1):** the Sun shines for billions of years — is it burning like a fire, or doing something else?

**Practice (rule 4):** TF TH: 1 verbatim item usable — q1, as a stretch item only (off-spec). q2 not usable (NUCLEAR-FUSION-F2, wrong wrong_explanation). The bank must be topped up by Design to the batch's fixed size, from the two spec sentences and the fission contrast.

**Diagrams:** see `05-diagram-library/README.md` (#8). Must draw: two light nuclei (e.g. ²H + ³H) joining into one heavier nucleus, beside a fission event for contrast — nothing in the library.

**Examiner tip:** none approved.

---

### 9. Scalar and Vector Quantities
`scalar-vector-quantities` · Physics / forces · AQA refs (8464 6.5.1.1; 8463 4.5.1.1) · true routes CF CH TF TH

**Family:** CLASSIFY — the spec is a two-way sort (magnitude only vs magnitude + direction) applied to named quantities, plus the arrow convention.

**Flagship (a suggestion, not a spec):** a sorter where each quantity card is dropped into Scalar or Vector, and vector cards then grow an arrow whose length the pupil sets.

**Route layers:**
- Higher: right-angle resultant by scale drawing (Pythagoras only as a check) — "8464 6.5.1.4 (HT only)" / "8463 4.5.1.4 (HT only)", "scale drawings only". Currently written into the base text (SCALAR-VECTOR-QUANTITIES-F1).
- Higher: motion in a circle — constant speed, changing velocity — "8464 6.5.4.1.3 (HT only)" / "8463 4.5.6.1.3 (HT only)".

**Required practical:** none.

**Calculations:**
- Resultant of two forces in a line (add same way, subtract opposite ways) — no equation; chains equations? no; no units to convert (all N); base (8464 6.5.1.4).
- HT: resultant of two perpendicular forces — scale drawing; Resultant² = F₁² + F₂² as a check; chains equations? no, but the square root is its own line; no units to convert; HT.

**Equations that need formula triangles (rule 2):** none. "Resultant² = F₁² + F₂²" is not a spec equation and is on neither sheet — no chip, and not a product, so no triangle; if shown (HT only), the square-root step is its own line.

**Misconceptions to confront:**
- "Speed and velocity are the same thing." → Velocity is speed in a given direction (6.5.4.1.3).
- "Run a lap and you've been displaced 400 m." → Displacement is start-to-finish in a straight line; a full lap is 0 m (6.5.4.1.1).
- "8 N one way and 3 N the other makes 11 N." → Forces in a line in opposite directions subtract (6.5.1.4).
- "Weight is in kg, so it's a scalar like mass." → Weight is a force in newtons, a vector (6.5.1.3).
- "A longer arrow is just drawn bigger." → Arrow length represents the magnitude (6.5.1.1).

**"Start here" access note (rule 1):** someone tells you "the shop is 200 m away" — is that enough to find it, or do you need to know which way?

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1, q2). None unusable. The bank must be topped up by Design to the batch's fixed size.

**Diagrams:** see `05-diagram-library/README.md` (#9). Must draw: a scalar-vs-vector contrast (e.g. distance along a curved path vs straight-line displacement arrow) — nothing in the library; HT layer can reuse `force_grid_2d()` for scale drawing.

**Examiner tip:** none approved.

---

### 10. Contact and Non-Contact Forces
`contact-noncontact-forces` · Physics / forces · AQA refs (8464 6.5.1.2; 8463 4.5.1.2) · true routes CF CH TF TH

**Family:** CLASSIFY (BATCH-PLAN said CONTRAST) — the spec says "All forces between objects are either" contact or non-contact and then names examples of each: a two-way sort of named forces. Its second strand — each interaction produces a force on each object — rides on the sort.

**Flagship (a suggestion, not a spec):** scenes (book on table, magnet and paperclip, skydiver, Earth and Moon) where the pupil tags each force contact / non-contact and sees its interaction partner on the other object.

**Route layers:** none — all base. (Upthrust, if kept as an example, is a term from "8463 4.5.5.1.2 (HT only)" (physics only) and must explain itself; static-charge detail is "8463 4.2.5.1" (physics only).)

**Required practical:** none.

**Calculations:** none.

**Equations that need formula triangles (rule 2):** none.

**Misconceptions to confront:**
- "Gravity needs air to work / stops in space." → Gravitational force is non-contact; objects are physically separated (6.5.1.2).
- "Friction holds the book up." → The normal contact force from the table holds it up; friction acts along surfaces.
- "Weight and the normal force are a Newton's third law pair." → They act on the same object; the pair of the book's weight is the book's pull on the Earth (6.5.4.2.3).
- "A magnet has to touch to pull." → Magnetic force is non-contact (6.5.1.2).
- "Air resistance is non-contact — you can't see the air touching." → Air resistance is a contact force (6.5.1.2).

**"Start here" access note (rule 1):** a fridge magnet pulls a paperclip across a small gap — does it need to touch it to pull?

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1, q2). None unusable. The bank must be topped up by Design to the batch's fixed size.

**Diagrams:** see `05-diagram-library/README.md` (#10). Must draw: a contact-vs-non-contact figure with the force on EACH object of an interacting pair, as arrows (spec: "The forces to be represented as vectors"). KS3 `r_interaction_board` is a candidate precedent only.

**Examiner tip:** none approved.

---

### 11. Gravity
`gravity` · Physics / forces · AQA refs (8464 6.5.1.3; 8463 4.5.1.3) · true routes CF CH TF TH

**Family:** QUANTITATIVE — the spec's core is W = mg, "recall and apply", with W ∝ m.

**Flagship (a suggestion, not a spec):** a "same mass, different worlds" newtonmeter: one mass hung on Earth, Moon and Mars, the pupil predicting each reading with W = mg.

**Route layers:** none — all base. (Orbit/free-fall context in theory 3 belongs to "8463 4.8.1.3" (physics only); keep to a line or cut.)

**Required practical:** none.

**Calculations:**
- W = mg (find W) — chains equations? no; Convert: g → kg (e.g. 450 g → 0.45 kg); base.
- Rearranged m = W ÷ g (find m) and g = W ÷ m — chains equations? no; Convert: g → kg / kN → N; base.
- Weight on another world from a weight on Earth — **chains equations? yes**: Step 1 m = W_Earth ÷ g_Earth; Step 2 W_new = m × g_new. Needs its own "Step 1 … Step 2 …" worked example before any pupil does one (rule 3). Convert: none if both given in N and N/kg. Base.
- Frozen FIFA: 12 kg on Earth → 117.6 N (Convert: nothing to convert — examined ✓). The second worked example must carry a g → kg conversion.

**Equations that need formula triangles (rule 2):** W = mg — On the sheet (8464 and 8463 June 2026). Triangle: top W; bottom m × g. No square, no ½.

**Misconceptions to confront:**
- "My weight is 60 kg." → Weight is a force, in newtons (6.5.1.3).
- "On the Moon my mass goes down." → Mass stays the same; weight depends on g where you are (6.5.1.3).
- "There's no gravity in space, so astronauts are weightless." → Gravity still acts in orbit; they are in free fall.
- "Twice the mass doesn't mean twice the weight." → Weight is directly proportional to mass, W ∝ m (6.5.1.3).
- "g means grams." → Here g is gravitational field strength, in N/kg; grams must be converted to kg first.
- "Weight acts from the bottom of the object." → It acts at the centre of mass (6.5.1.3).

**"Start here" access note (rule 1):** an astronaut stands on bathroom scales on the Moon — would they read more or less than on Earth?

**Practice (rule 4):** all four routes: 2 verbatim items usable (q1, q2). None unusable (q1's "50 kg" distractor is internally inconsistent but harmless — GRAVITY-F3). The bank must be topped up by Design to the batch's fixed size, including a W ∝ m item and a centre-of-mass item.

**Diagrams:** see `05-diagram-library/README.md` (#11). Must draw: a mass with its weight arrow from the centre of mass, labelled m, W and g; the same object on Earth and Moon — nothing dedicated in the library.

**Examiner tip:** none approved.

---

### 12. Resultant Forces
`resultant-forces` · Physics / Forces · AQA refs (8464 6.5.1.4; 8463 4.5.1.4; supporting 6.5.4.2.1 / 4.5.6.2.1, 6.5.4.1.5 / 4.5.6.1.5) · true routes CF CH TF TH

- **Family:** MODEL — one idea (the resultant) predicts every motion: zero → still or steady; non-zero → speeds up, slows down or turns.
- **Flagship (a suggestion, not a spec):** Change two opposing forces on a cart and predict, before it runs, whether it stays still, cruises, speeds up or slows down.
- **Route layers:**
  - Free body diagrams; resultant of two forces at an angle by scale drawing — 8464 6.5.1.4 (HT only) / 8463 4.5.1.4 (HT only) → CH TH.
  - Resultant perpendicular to motion changes direction (circle, qualitative) — 8464 6.5.4.1.3 (HT only) → CH TH (one line; detail lives on `motion-in-a-circle`).
- **Required practical:** none.
- **Calculations:**
  - Resultant of two forces in a straight line: add (same direction) / subtract (opposite), direction of the larger. Chains equations? no. Units: none to convert (all N). Base.
  - HT: resultant of two forces at an angle, scale drawing only. Chains? no. Convert = the scale (N → cm, measured cm → N). Higher.
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "Zero resultant means it's not moving." — Newton's First Law: zero resultant also means steady velocity (6.5.4.2.1).
  - "A moving car must have a bigger forward force." — at steady speed resistive forces balance the driving force (6.5.4.2.1).
  - "At terminal velocity there's no air resistance / gravity has switched off." — weight = air resistance, resultant zero (6.5.4.1.5).
  - "The skydiver runs out of energy and stops speeding up." — the forces balance; weight is still there (6.5.4.1.5).
  - "Forces at an angle just add up." — at an angle you need a vector (scale) diagram (6.5.1.4 HT).
- **"Start here" access note (rule 1):** two people pull a rope in a tug of war, equally hard: does the rope move or stay put?
- **Practice (rule 4):** frozen q1, q2 usable on all four routes (2). None unusable. Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` (#12). Must draw: two forces on one object with the resultant arrow (`resultant_force()`); balanced/unbalanced pairs for book, car, skydiver; HT: a to-scale tip-to-tail diagram.
- **Examiner tip:** none approved.

---

### 13. Resolving Forces and Vector Diagrams
`resolving-forces` · Physics / Forces · AQA refs (8464 6.5.1.4 (HT only); 8463 4.5.1.4 (HT only)) · true routes CH TH (site ships TH; moving under the route-flag PR)

- **Family:** PROCESS — changed from BATCH-PLAN's QUANTITATIVE: AQA says "scale drawings only", so there is no equation for a FIFA flagship to carry; the skill is a fixed drawing sequence (scale → tip-to-tail → measure → convert back).
- **Flagship (a suggestion, not a spec):** A to-scale drawing stepper on squared paper: pupils predict the resultant's length and angle, then draw and measure it.
- **Route layers:** whole page is higher — 8464 6.5.1.4 (HT only) / 8463 4.5.1.4 (HT only). No physics-only layer.
- **Required practical:** none.
- **Calculations:**
  - Resultant of two forces at an angle, by scale drawing (magnitude and direction). Chains equations? no. Convert: the scale (N → cm to draw; measured cm → N to answer); angle by protractor. Higher.
  - Resolving one force into two perpendicular components, by scale drawing. Chains? no. Convert: as above. Higher.
  - Equilibrium: three forces drawn tip-to-tail close into a triangle; find an unknown force by drawing. Chains? no. Higher.
  - No trigonometry, Pythagoras or arctan (off-spec, flags F1, F2).
- **Equations that need formula triangles (rule 2):** none (no equation on spec or on either sheet).
- **Misconceptions to confront:**
  - "Two forces at an angle just add up." — their resultant is found by a vector diagram (6.5.1.4 HT).
  - "Components are extra forces on top of the original." — "the two component forces together have the same effect as the single force" (6.5.1.4 HT).
  - "A closed triangle means the forces are equal." — it means the resultant is zero: equilibrium (6.5.1.4 HT).
  - "The resultant goes from the last arrow back to the first." — it goes from the tail of the first to the tip of the last.
  - "I don't need to say my scale." — the answer only means something converted back by the stated scale.
- **"Start here" access note (rule 1):** pulling a sledge with a rope that slopes up: is some of your pull lifting the sledge, or is all of it pulling it forwards?
- **Practice (rule 4):** frozen q2 usable on CH TH (1). q1 not usable (RESOLVING-FORCES-F4). The FIFA's method is off-spec (F2). Design tops the bank up to the batch's fixed size with scale-drawing items.
- **Diagrams:** see `05-diagram-library/README.md` (#13). Must draw: forces to scale on squared paper (`force_grid_2d()`, AQA 4.5.1.4 "scale drawings only"); a resolution triangle with right angle marked (`resolution_triangle()` — drop any trig labels); parallelogram of forces; closed triangle of three forces.
- **Examiner tip:** none approved.

---

### 14. Free Body Diagrams
`free-body-diagrams` · Physics / Forces · AQA refs (8464 6.5.1.4 (HT only); 8463 4.5.1.4 (HT only); supporting 6.5.1.2–3, 6.5.4.2.1–2, 6.5.4.1.5) · true routes CH TH (site ships TH; moving under the route-flag PR)

- **Family:** MODEL — one diagram (every force on one object) predicts the motion: balanced → still or steady, unbalanced → accelerates.
- **Flagship (a suggestion, not a spec):** Pupils build the FBD for a moving scene (car, skydiver, box on a slope) and predict from it whether the object speeds up, slows down or stays steady.
- **Route layers:** whole page is higher — 8464 6.5.1.4 (HT only) / 8463 4.5.1.4 (HT only). Upthrust, if named — 8463 4.5.5.1.2 (physics only)(HT only) → TH.
- **Required practical:** none.
- **Calculations:** None required (spec: "describe qualitatively"). Reading the resultant off an FBD uses the straight-line add/subtract from `resultant-forces` — chains? no; convert: none. No trig (flag F1).
- **Equations that need formula triangles (rule 2):** none.
- **Misconceptions to confront:**
  - "The book pushes down on the table, so that goes on the book's diagram." — an FBD shows only forces acting ON the object (6.5.1.4 HT).
  - "A moving object must have an arrow pointing the way it's going." — at constant velocity the forces balance (6.5.4.2.1).
  - "At terminal velocity there's no air resistance." — drag equals weight (6.5.4.1.5).
  - "Normal force always points straight up." — it is perpendicular to the surface.
  - "Weight acts from the bottom / where it touches the floor." — weight acts at the centre of mass (6.5.1.3).
- **"Start here" access note (rule 1):** a book lying still on a table: is just one force acting on it, or more than one?
- **Practice (rule 4):** frozen q2 usable on CH TH (1). q1 not usable (FREE-BODY-DIAGRAMS-F1, F2). Design tops the bank up to the batch's fixed size.
- **Diagrams:** see `05-diagram-library/README.md` (#14). Must draw: `free_body_diagram()` (box: weight, normal, thrust, friction); `free_body()` builder for book, car, skydiver (two stages), box on a slope (qualitative — no W sin θ labels).
- **Examiner tip:** none approved.

---

### 15. Work Done and Energy Transfer
`work-done-energy-transfer` · Physics / Forces · AQA refs (8464 6.5.2; 8463 4.5.2; supporting 6.5.1.3 / 4.5.1.3, 6.1.1.2 / 4.1.1.2) · true routes CF CH TF TH

- **Family:** QUANTITATIVE — W = Fs carries the concept (force, distance along its line, energy transferred).
- **Flagship (a suggestion, not a spec):** Push a crate with a set force over a set distance and watch the joules transferred tick up — then turn the force sideways to the motion and see the count stop.
- **Route layers:** none — all base (6.5.2 has no HT or physics-only content).
- **Required practical:** none.
- **Calculations:**
  - W = Fs, and F = W ÷ s, s = W ÷ F. Chains equations? no. Convert: cm → m, km → m, kN → N, kJ → J (e.g. 250 cm → 2.5 m). Base.
  - Lifting: chains equations? **yes** — Step 1 weight = mg; Step 2 work done = weight × height (= Ep gained). Convert: g → kg, cm → m. Base. Needs its own "Step 1 … Step 2 …" worked example (frozen th3 example: 5 kg, 2 m → 49 N → 98 J).
  - 1 N m = 1 J (unit conversion). Chains? no. Base.
- **Equations that need formula triangles (rule 2):** W = Fs — On the sheet (8464 and 8463 June 2026) — W on top / F × s on the bottom. Supporting W = mg — On the sheet — W top / m × g bottom.
- **Misconceptions to confront:**
  - "Holding a heavy bag still is hard work, so work is done." — no displacement, no work (6.5.2).
  - "Gravity does work on a bag I carry along a corridor." — force ⟂ motion: no distance along its line of action (6.5.2).
  - "Use the total distance, whatever direction." — distance along the line of action of the force (6.5.2).
  - "Friction turns the energy into movement." — work against friction raises the temperature (6.5.2).
  - "W in W = Fs is weight." — it is work done, in joules.
  - "s = W × F." — rearrange: s = W ÷ F.
- **"Start here" access note (rule 1):** pushing a heavy trolley across a car park versus pushing against a wall that doesn't move: which leaves you having done more work?
- **Practice (rule 4):** frozen q1, q2 usable on all four routes (2). None unusable. Design tops the bank up to the batch's fixed size, including one cm → m item, one lifting chain, one N m ↔ J item.
- **Diagrams:** see `05-diagram-library/README.md` (#15). Must draw: a force arrow pushing an object with the distance moved marked along the force's line (missing from figlib); force at right angles to motion (bag carried horizontally).
- **Examiner tip:** none approved.

---

### 16. Forces and Elasticity
`forces-elasticity` · Physics / Forces · AQA refs (8464 6.5.3; 8463 4.5.3; supporting 6.1.1.2 / 4.1.1.2, 6.5.1.3 / 4.5.1.3) · true routes CF CH TF TH

- **Family:** REQUIRED PRACTICAL — changed from BATCH-PLAN's QUANTITATIVE: the spring RP is this lesson's own spec point (RP18 / RP6) and it carries F = ke, gradient = k and the limit of proportionality; the CFIFA work sits inside its data processing.
- **Flagship (a suggestion, not a spec):** Hang masses on a simulated spring, record lengths, plot F against e, find k from the gradient and spot where the line stops being straight.
- **Route layers:** none — all base (6.5.3 has no HT or physics-only content; Ee = ½ke² is base per Mide's ruling).
- **Required practical:** Combined RP18 (8464 6.5.3) on CF CH; Physics RP6 (8463 4.5.3) on TF TH — "investigate the relationship between force and extension for a spring." Same practical.
- **Calculations:**
  - F = ke, k = F/e, e = F/k. Chains equations? no. Convert: cm → m, mm → m; find e = stretched length − natural length first. Base.
  - Spring constant from RP data: chains? **yes** — Step 1 force = weight of masses, W = mg (Convert g → kg); Step 2 k = F/e (Convert cm → m) or k = gradient. Base.
  - Ee = ½ke². Chains? no (k, e given). Convert: cm → m before squaring. Base.
  - Ee from a force and extension: chains? **yes** — Step 1 k = F/e; Step 2 Ee = ½ke². Base.
  - Ee → speed: chains? **yes** — Step 1 Ee = ½ke²; Step 2 Ek = ½mv² → v. Base.
- **Equations that need formula triangles (rule 2):**
  - F = ke — On the sheet (8464 and 8463 June 2026) — F top / k × e bottom.
  - Ee = ½ke² — On the sheet (both) — Ee top / ½ × k × e² bottom. Extra lines: to find k, k = 2Ee ÷ e²; to find e, e² = 2Ee ÷ k, then square-root (own line).
  - W = mg (RP force) — On the sheet (both) — W top / m × g bottom.
- **Misconceptions to confront:**
  - "Extension is the spring's length." — extension is the increase from natural length (6.5.3).
  - "It's proportional until it breaks / until the elastic limit." — until the limit of proportionality (6.5.3).
  - "Once it bends, it's permanently stretched." — non-linear ≠ inelastic; inelastic means it does not return to its original length (6.5.3).
  - "You can stretch something with one push." — a stationary object needs more than one force to change shape (6.5.3).
  - "The masses are the force." — the force is their weight, W = mg, in newtons (6.5.1.3).
  - "Double the extension, double the stored energy." — Ee ∝ e²: double e, four times Ee (6.5.3).
- **"Start here" access note (rule 1):** hanging a second, identical weight on a spring: does it stretch about twice as far, or only a little bit more?
- **Practice (rule 4):** frozen q1 usable on all four routes (1). q2 not usable (FORCES-ELASTICITY-F3). Design tops the bank up to the batch's fixed size, including an Ee item and a graph-reading (limit of proportionality) item.
- **Diagrams:** see `05-diagram-library/README.md` (#16). Must draw: `hookes_law_graph()` (F vs e, linear then curving, limit of proportionality marked); RP set-up (clamp, spring, ruler, pointer, mass hanger); natural length vs stretched length with e marked.
- **Examiner tip:** none approved.
