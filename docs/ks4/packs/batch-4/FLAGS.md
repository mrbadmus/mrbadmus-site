# Batch 4 — science flags

Numbered per lesson. **WRONG** items are frozen text kept verbatim in the source files that must not be used as written. Each flag says what to do instead.

## 1. The Heart and Blood Vessels (`heart-blood-vessels`)

# Flags — heart-blood-vessels (8464/8461 4.2.2.2)

1. **HBV-F1** · WRONG · quiz q4 wx1: "Capillaries have the LOWEST blood pressure — that is why they can be one cell thick without bursting." · False. Pressure falls all the way round the circuit: arteries > capillaries > veins. Veins (the vena cava) have the lowest pressure; the source's own vein theory says vein pressure is low. · Correct: "Arteries have the highest blood pressure. By the time blood reaches the capillaries the pressure has already dropped a lot." · 4.2.2.2 · **Do not use q4 as written.** Its stem, options and key are right; Design may re-author it as a new item with this wx1 and HBV-F5's wx2.

2. **HBV-F2** · ROUTE · `higher` block: "Artificial pacemakers correct irregular heart rhythms. Faulty heart valves can be replaced… Artificial hearts… evaluate… drug treatment vs mechanical devices vs transplant…" · Tagged higher, so the site hides it on Combined Foundation and Triple Foundation. None of it carries "(HT only)". · Artificial pacemakers are base 4.2.2.2; valves, artificial hearts and evaluation are base 4.2.2.4. · 4.2.2.2; 4.2.2.4 · Teach pacemakers as base on all four routes here. Leave valves, artificial hearts and evaluation to coronary-heart-disease (base).

3. **HBV-F3** · GAP · Lungs absent from the frozen data. · The spec's lesson core includes "the structure and functioning of the human heart and lungs, including how lungs are adapted for gaseous exchange" — trachea, bronchi, alveoli, capillary network. No other KS4 lesson on the site covers them. · Alveoli: large surface area, thin walls, dense capillary network; O₂ diffuses into the blood, CO₂ out. · 4.2.2.2 · Teach and practise it, base. Spec text added to the source file.

4. **HBV-F4** · GAP · Natural pacemaker absent. · "The natural resting heart rate is controlled by a group of cells located in the right atrium that act as a pacemaker." · As quoted. · 4.2.2.2 · Teach it, base, next to artificial pacemakers.

5. **HBV-F5** · IMPRECISE · quiz q4 wx2: "Capillaries carry either oxygenated or deoxygenated blood depending on location — not both at once." · In a body capillary, blood enters oxygenated and leaves deoxygenated, so its oxygen content changes along the capillary. · Better: "Which blood a capillary carries is not what makes it good at exchange — thin walls and a large surface area are." · 4.2.2.2 · Use the better line if q4 is re-authored.

6. **HBV-F6** · GAP · Rate calculations for blood flow absent. · "Students should be able to use simple compound measures such as rate and carry out rate calculations for blood flow." (MS 1a, 1c). The source has no calculation. · Rate of blood flow = volume ÷ time; heart rate = beats ÷ time in minutes. · 4.2.2.2 · Teach with CFIFA worked examples (convert s ↔ min, cm³ ↔ dm³) before any practice.

7. **HBV-F7** · IMPRECISE · Theory "Structure of the Heart": "Semilunar valves — in the pulmonary artery and aorta" vs theory "Arteries": "NO valves". · These contradict each other. · The semilunar valves sit at the exits of the ventricles, where the aorta and pulmonary artery leave the heart. Arteries have no valves along their length. · — · When re-cutting the theory, place the valves at the exits of the ventricles.

8. **HBV-F8** · OFF-SPEC · "Atrioventricular (AV) valves … Semilunar valves" · "Knowledge of the names of the heart valves is not required." · Accurate, but not examinable. · 4.2.2.2 · Label "valve" only; never test the names.

9. **HBV-F9** · IMPRECISE · "CARDIAC MUSCLE — … never getting tired." · Overstated. Cardiac muscle is very resistant to fatigue. · "does not tire like other muscles" · — · Re-cut or drop (off-spec detail).

10. **HBV-F10** · IMPRECISE · quiz q3 wx3: "Valves in veins do slightly slow flow, but that's acceptable…" · Option 4 is about arteries, so this explanation answers the wrong vessel. Not false. · The point: arteries need no valves because high pressure keeps blood moving one way. · — · q3 usable as written. If Design writes its own feedback, use this point.

11. **HBV-F11** · IMPRECISE · File label "AQA 4.2.3". · AQA numbers this 4.2.2.2 in 8461 and 8464. · — · — · Badge the page 4.2.2.2.

## 2. The Water Cycle (`water-cycle`)

# Flags — water-cycle (8464/8461 4.7.2.2)

**WATER-CYCLE-F1** · ROUTE · spec reference: site `site_spec` = "4.7.3"; file name `biology-4.7.3-water-cycle.md` · 4.7.3 is "Biodiversity and the effect of human interaction on ecosystems". The water cycle is in "4.7.2.2 How materials are cycled" in both 8464 and 8461. Routes (CF CH TF TH) are correct. · AQA ref: 8464 4.7.2.2; 8461 4.7.2.2. · Spec texts · Use 4.7.2.2 on the page and in the lesson data.

**WATER-CYCLE-F2** · GAP · the spec's core statement · "The water cycle provides fresh water for plants and animals on land before draining into the seas." The source never says the water arriving on land is **fresh**, nor why (evaporation leaves dissolved salts behind). "Why water must be recycled" gives water's uses, not the cycle's importance. · Evaporation from the sea leaves salts behind → vapour → precipitation is fresh water → used by land plants and animals → drains back to the sea. · 8464/8461 4.7.2.2 ("explain the importance of the carbon and water cycles to living organisms") · Teach it explicitly; it is the answer to the spec's "explain the importance" question.

**WATER-CYCLE-F3** · IMPRECISE · theory: "It is the SOLVENT for all biochemical reactions." · Overstated. · "Most reactions in cells take place in solution in water." · — · Re-cut.

**WATER-CYCLE-F4** · IMPRECISE · theory: "Soil absorption is helped by the structural effects of plant roots." · Unclear sentence. · Roots open channels in the soil so rain soaks in instead of running off. · — · Re-cut or drop.

**WATER-CYCLE-F5** · GAP · diagram · `figlib/biology.py water_cycle()` labels evaporation, condensation, precipitation, run-off only — **no transpiration**, which the lesson and both quiz items rely on. · Transpiration from leaves is a process in the cycle. · 4.7.2.2; 4.2.3.2 · The figure must add a transpiration arrow from plants (and may add groundwater).

## 3. Atmospheric Pollutants from Fuels (`atmospheric-pollutants`)

# Flags — atmospheric-pollutants (AQA 8464 5.9.3.1–5.9.3.2 / 8462 4.9.3.1–4.9.3.2)

1. **ATMOSPHERIC-POLLUTANTS-F1** · WRONG · q1 key: "CO binds irreversibly to haemoglobin — preventing red blood cells from carrying oxygen, causing suffocation even in small concentrations" · CO binding is reversible (about 200–250 times stronger than oxygen, released slowly; poisoning is treated with high-concentration oxygen). The key also leaves out the spec's answer. · Correct: CO is toxic; it is colourless and odourless, so it is not easily detected. · 8464 5.9.3.2 / 8462 4.9.3.2 · **Do not use as written.** Write a replacement item keyed on the spec statement; wx1's point ("colourless and odourless, cannot be detected without a detector") is the right teaching line.

2. **ATMOSPHERIC-POLLUTANTS-F2** · OFF-SPEC · q2 "How do catalytic converters reduce air pollution from cars?" · True science, but catalytic converters are on neither 8462 nor 8464. · — · Not usable as assessed practice on any route. Leave out of the ladder and the practice bank.

3. **ATMOSPHERIC-POLLUTANTS-F3** · OFF-SPEC · `higher` (TH, CH): "Evaluate effectiveness and limitations of pollution control: catalytic converters … electric vehicles … life cycle perspective" · 5.9.3 / 4.9.3 has no HT content; none of this is on spec. Life-cycle assessment is its own base lesson (8464 5.10.2.1). · The page has no Higher layer. · Do not render a Higher block. (CF/TF copies are already null.)

4. **ATMOSPHERIC-POLLUTANTS-F4** · WRONG · Theory 3: catalytic converters "Reduces: CO (toxic), NOₓ (acid rain, smog) and particulates" · A catalytic converter does not remove particulates; that is the particulate filter. The source's own q2 wx1 says so. · — · Re-cut: drop "and particulates" (and, as off-spec, keep catalytic converters as a one-line aside at most).

5. **ATMOSPHERIC-POLLUTANTS-F5** · GAP · Spec bullet not taught: "predict the products of combustion of a fuel given appropriate information about the composition of the fuel and the conditions in which it is used" · Nothing in the source practises it. · Carbon → CO₂ in plenty of oxygen; → CO and/or C (soot) when oxygen is limited. Hydrogen → H₂O. Sulfur in the fuel → SO₂. Any fuel burned hot in air → oxides of nitrogen (N from the air). Unburned hydrocarbons → particulates. · 8464 5.9.3.1 / 8462 4.9.3.1 (WS 1.2) · Teach it with a worked example, and include it in practice. See the source file's "Spec core missing" section.

6. **ATMOSPHERIC-POLLUTANTS-F6** · IMPRECISE · Theory 2: "Acid rain: pH typically 4–5 — 10× to 100× more acidic than normal rain." · pH 4–5 against 5.6 is about 4×–40× the H⁺ concentration. The factor-of-10-per-pH-unit idea is HT (8464 5.4.2.5). · "Acid rain has a lower pH than normal rain (about 5.6)." · 8464 5.4.2.5 (HT only) · Drop the multiplier.

7. **ATMOSPHERIC-POLLUTANTS-F7** · IMPRECISE · Theory 1: "Consciously contribute to GLOBAL DIMMING"; particulates "From incomplete combustion of fuels." · Typo ("Consciously"); and the spec's source of particulates includes unburned hydrocarbons. · "Particulates (solid particles and unburned hydrocarbons) cause global dimming and health problems." · 8464 5.9.3.1–2 · Re-cut.

8. **ATMOSPHERIC-POLLUTANTS-F8** · OFF-SPEC · Theory 1–3 and equations: acid-forming equations (H₂SO₃, H₂SO₄, HNO₃), smog and low-level ozone, aluminium ions, scrubbers, desulfurisation, catalytic converters, equation 3 (2CO + 2NO → 2CO₂ + N₂), key_note's last clause · All true and balanced; none on spec. · The spec needs: source of each pollutant, and CO toxic/undetectable; SO₂ and NOₓ → respiratory problems and acid rain; particulates → global dimming and health problems. · 8464 5.9.3 · Keep any of it as optional context only; never in Start here, the ladder or practice.

## 4. Efficiency (`efficiency`)

# Flags — efficiency

**EFFICIENCY-F1** · ROUTE · `higher` (all three copies) and theory chunk 3 "Improving Efficiency": "Describe specific ways to increase efficiency for a given device or system and justify each…" · The CF and TF `higher` copies serve HT-only content to Foundation routes. · "(HT only) Students should be able to describe ways to increase the efficiency of an intended energy transfer." Lubrication and thermal insulation, as ways of reducing unwanted energy transfers, are base (6.1.2.1). · 8464 6.1.2.2 (HT only); 8463 4.1.2.2 (HT only); 8464 6.1.2.1 · Design: teach lubrication and insulation as base; put "ways to increase efficiency" (streamlining, LEDs, regenerative braking, describe/justify) in a higher layer on CH TH only. "Evaluate cost-effectiveness" is optional enrichment beyond the HT statement.

**EFFICIENCY-F2** · IMPRECISE · theory chunk 2: "EXAMPLE — LED bulb (efficient): Input: 100 J / Useful light: 90 J / Wasted heat: 10 J / Efficiency = … 90%" (also matching pair "0.90 (90%)") · Real white LEDs transfer roughly 30–50% of their input to light; 90% teaches a false fact. · Keep the contrast with a filament lamp (≈ 5–10%) using a realistic LED figure, e.g. 40 J of 100 J → 40%. · — · Design: re-cut the theory example. Quiz q2 (LED 10 J/s of 11 J/s) is an idealised device with correct arithmetic — usable as written.

**EFFICIENCY-F3** · IMPRECISE · equations[2]: "efficiency (%) = (useful output ÷ total input) × 100" · Not an AQA equation and on neither sheet; it is the decimal → percentage conversion. · Spec: "Students may be required to calculate or use efficiency values as a decimal or as a percentage." · 8464 6.1.2.2; 8463 4.1.2.2 (MS 3b, c) · Design: no formula triangle for it; teach "× 100 for a percentage" (and "÷ 100 before using a % in the equation") as its own line in CFIFA.

## 5. Infrared Emission, Absorption and Black Bodies (`infrared-black-bodies`)

# Flags — infrared-black-bodies

**IRB-F1** · WRONG · theory chunk 2: "Very hot iron (1000°C): orange-white — peak moves into visible range." · At 1000 °C (1273 K) the emission peak is ≈ 2.3 µm, still in the infrared. The object glows brighter because more of the visible band is emitted, not because the peak is visible. The peak reaches the visible only near 4000 K and above (the Sun, ≈ 5800 K). · "the intensity and wavelength distribution of any emission depends on the temperature of the body" · 8463 4.6.3.2 · Design: re-cut — "as it gets hotter it emits more at every wavelength and a bigger share at shorter wavelengths, so the glow goes red → orange → yellow-white; the peak is still in the infrared".

**IRB-F2** · WRONG · quiz q1 wx3: "White hot means the peak has moved to visible wavelengths with broad-spectrum emission — cool objects emit IR (invisible) then progress through red, orange, yellow to white as temperature rises." (and the key's gloss "from infrared through red to shorter visible wavelengths approaching white") · White-hot metal (≈ 1300–1500 °C) peaks at ≈ 1.6–1.8 µm, infrared. It looks white because all visible wavelengths are now emitted strongly enough to mix. The key's first clause ("peak emission shifts to shorter wavelengths") is right. · as IRB-F1 · 8463 4.6.3.2 · **Do not use q1 as written.** Write a replacement on the same stem in which the feedback says the peak moves to shorter wavelengths without claiming it enters the visible.

**IRB-F3** · IMPRECISE · theory chunk 1 and common_mistake: "Hotter objects emit MORE radiation and at SHORTER wavelengths" · Read literally, it says a hotter object swaps long wavelengths for short. It emits more at every wavelength, with the distribution (and its peak) shifted to shorter wavelengths. · "The hotter the body, the more infrared radiation it radiates in a given time." "…the intensity and wavelength distribution of any emission depends on the temperature" · 8463 4.6.3.1–4.6.3.2 · Design: use the spec's two-part wording; draw the curves (two or three temperatures, one inside the other).

**IRB-F4** · IMPRECISE · theory chunk 3: "Yellow stars (like the Sun, ~5500 K)" against chunk 2: "The Sun (~5500°C surface)" · The Sun's surface is ≈ 5800 K ≈ 5500 °C; the two lines disagree by 273 K. · — · — · Design: one figure, "about 5800 K (5500 °C)".

**IRB-F5** · ROUTE · theory chunk 1 "EMISSION vs ABSORPTION RATES: If emission rate > absorption rate → object cools…"; chunk 3 "EARTH'S TEMPERATURE…"; `higher` (TH) · The absorb/emit balance and Earth's temperature are HT only, but are taught as base. Conversely, the `higher` field's first line ("black body radiation curves — how peak wavelength depends on temperature") is not HT. · "(HT only) A body at constant temperature is absorbing radiation at the same rate as it is emitting radiation… (HT only) The temperature of the Earth depends on… the rates of absorption and emission of radiation, reflection of radiation into space." · 8463 4.6.3.2 (physics only) (HT only) · Design: balance + Earth's temperature in a TH-only layer; curves in the TF/TH base of the page; say "reflection of radiation into space", not "albedo".

**IRB-F6** · ROUTE · `rp` field absent; BATCH-PLAN's "Rainford's IR RP" family suggestion · The IR-surfaces practical is base: RP21 (8464 6.6.2.2) = RP10 (8463 4.6.2.2), on all four routes. Its spec home is "Properties of electromagnetic waves 1". If it lived here, Combined pupils (who never see this physics-only page) would lose a base RP. · "Required practical activity 21: investigate how the amount of infrared radiation absorbed or radiated by a surface depends on the nature of that surface." · 8464 6.6.2.2; 8463 4.6.2.2 · Settled: the RP belongs on `properties-em-waves-1` (CF CH TF TH), as the route audit recommends, and goes in the route-flag PR. This page recalls its result (matt black is the best emitter and absorber) as a bridge only, with no RP block.

**IRB-F7** · OFF-SPEC · theory chunk 3: star colours ("Red stars (~3000 K)… Blue-white stars (~30,000 K)"), "Hubble detects visible light; James Webb Space Telescope detects infrared", chunk 2 "depends ONLY on temperature — not on the material" · Correct physics (Hubble also sees near-UV and near-IR), but none of it is examinable. · — · 8463 4.6.3; 4.8 · Design: optional context only. Never in practice or ladder items.

**IRB-F8** · ROUTE · spec field "6.6.5 (physics only)" · No such section. The content is 8463 4.6.3.1–4.6.3.2 "Black body radiation (physics only)"; 8464 has no equivalent. Routes TF TH are right. · — · 8463 4.6.3 · Correct the spec field to 8463 4.6.3.1–4.6.3.2 in the route-flag PR.

## 6. Diffusion, Osmosis and Active Transport (`transport-in-cells`)

# Flags — transport-in-cells (8464/8461 4.1.3.1–4.1.3.3)

**TRANSPORT-IN-CELLS-F1** · WRONG · theory "Diffusion": "Urea diffuses from liver cells (where it is made) → into blood → into kidney tubules → excreted in urine" · Urea does not diffuse into the kidney tubules; it enters the nephron by filtration of the blood. · The diffusion step is liver cells → blood plasma. The spec's own example stops there: "the waste product urea from cells into the blood plasma for excretion in the kidney". · 8464/8461 4.1.3.1; 8461 4.5.3.3 (biology only) "filtration of the blood" · Re-cut: end the diffusion chain at "into the blood plasma".

**TRANSPORT-IN-CELLS-F2** · ROUTE · `higher` field (served on CH/TH only; `null` on CF/TF): "% change = (change in mass ÷ original mass) × 100 … isotonic point … surface area to volume ratios … why large organisms need exchange systems" · None of it is HT. 4.1.3 carries no "(HT only)" label. Foundation pupils currently never see the SA:V calculation or the isotonic-point reading. · All base: % change and graphs (4.1.3.2, MS 1c, 4a–4d); SA:V (4.1.3.1, MS 1c, 5c). · 8464/8461 4.1.3.1–2 · Teach all of it on every route. No Higher layer in this lesson.

**TRANSPORT-IN-CELLS-F3** · ROUTE · `rp`: "RP2 — Investigate osmosis …" · "RP2" is the Combined number only. In 8461, RP2 is antiseptics/antibiotics (culturing microorganisms); osmosis is **RP3**. · Combined Trilogy Required practical activity 2 = Biology Required practical activity 3, same practical. · 8464 4.1.3.2; 8461 4.1.3.2 · Label route-aware: "Required practical 2" on CF/CH, "Required practical 3" on TF/TH (or "RP2 Combined / RP3 Biology").

**TRANSPORT-IN-CELLS-F4** · IMPRECISE · quiz q3 key: "No oxygen → aerobic respiration stops → no ATP produced → no energy for active transport" (stem: "Why does active transport stop if oxygen is removed…") · "No ATP produced" contradicts on-spec content: anaerobic respiration still transfers energy, just much less. The stem's "stop" overstates. · Credit-worthy chain: less oxygen → less aerobic respiration → less energy transferred → less active transport. · 8464/8461 4.1.3.3; 4.4.2.1 · **Do not use as written.** Design may write a replacement on the same idea with "less energy" and "slows / stops".

**TRANSPORT-IN-CELLS-F5** · IMPRECISE · theory "Active Transport": "ENERGY from ATP (produced by aerobic respiration)" and "active transport STOPS immediately if respiration is blocked (… or by removing oxygen)" · Energy comes from respiration, aerobic and anaerobic; removing oxygen greatly reduces active transport rather than stopping it instantly. "ATP" and "carrier proteins" are not spec words. · Spec: "This requires energy from respiration." · 4.1.3.3; 4.4.2.1 · Re-cut: lead with "energy from respiration"; ATP/carrier proteins as an aside if at all.

**TRANSPORT-IN-CELLS-F6** · IMPRECISE · `higher`: "The isotonic point … is where the external solution concentration matches the cell's water potential" · Compares a concentration with a water potential; "water potential" is A-level (also in theory "Osmosis"). · Where the line crosses 0 % change in mass, there is no net movement of water: the solution has the same concentration as the cell contents. · 4.1.3.2 · Use the corrected wording; never "water potential".

**TRANSPORT-IN-CELLS-F7** · GAP · SA:V calculation · The spec requires pupils to "calculate and compare surface area to volume ratios"; the source has no worked example. It is a three-step chain (SA, then V, then the ratio). · e.g. 1 cm cube: SA = 6 × 1 × 1 = 6 cm², V = 1 cm³, SA:V = 6 : 1; 2 cm cube: 24 cm², 8 cm³, 3 : 1; 3 cm cube: 54 cm², 27 cm³, 2 : 1 — the ratio falls as size rises. · 8464/8461 4.1.3.1 (MS 1c, 5c) · Design writes a "Step 1 … Step 2 … Step 3 …" worked example before any pupil attempt (rule 3), on every route.

**TRANSPORT-IN-CELLS-F8** · GAP · Exchange surfaces named by the spec · Gills in fish and leaves in plants are missing; theory covers alveoli, villi, root hairs only. · Gills: many filaments/lamellae (large SA), thin, good blood supply, water flows over (ventilated). Leaves: flat, thin, stomata, air spaces in spongy mesophyll. · 4.1.3.1 · Include both.

**TRANSPORT-IN-CELLS-F9** · GAP · "use simple compound measures of rate of water uptake" · Not in the source. · e.g. rate = change in mass ÷ time (g/min). · 4.1.3.2 (MS 1a, 1c) · Teach with the RP data.

**TRANSPORT-IN-CELLS-F10** · IMPRECISE · theory "Diffusion" and "Osmosis" (minor, re-cuttable): "high water potential"; "Plant wilts" placed after plasmolysis; alveoli "highly folded"; q2 wx2 "selectively permeable"; q4 wx3 answers a bursting question that cannot arise in a concentrated solution · Off-spec terms or loose chains. · Spec word: partially permeable. Wilting follows loss of turgor (flaccid cells); plasmolysis is the extreme. Lung SA comes from many alveoli. · 4.1.3.1–2 · Re-cut theory. q2 and q4 remain usable as written.

## 7. Blood (`blood`)

# Flags — blood (8464/8461 4.2.2.3)

1. **BLD-F1** · GAP · White-blood-cell functions list phagocytosis and antibodies only. · The spec lists three: "phagocytosis, antibody production, antitoxin production." · Some white blood cells produce antitoxins, which neutralise the toxins released by bacteria. · 4.3.1.6 (functions required by 4.2.2.3) · Teach all three, base. Spec text added to the source file.

2. **BLD-F2** · GAP · Recognition from images. · "Students should be able to recognise different types of blood cells in a photograph or diagram, and explain how they are adapted to their functions." The source has no image work and gives adaptations for red cells only. · Red cell: biconcave, no nucleus. White cell: larger, has a nucleus; phagocytes engulf. Platelets: small fragments. · 4.2.2.3 · Include image-recognition teaching and practice items.

3. **BLD-F3** · IMPRECISE · "BICONCAVE DISC SHAPE — increases surface area for oxygen absorption and releases carbon dioxide." · Garbled, and suggests red cells are the CO₂ carriers. At GCSE, plasma carries CO₂ (as the source's own plasma theory says). · "Biconcave shape gives a large surface area for oxygen to diffuse in and out." · 4.2.2.3 · Re-cut this line.

4. **BLD-F4** · IMPRECISE · "…before being broken down in the spleen." · Old red cells are removed by the spleen **and the liver**. · — · — · Say "spleen and liver", or drop it (off-spec).

5. **BLD-F5** · IMPRECISE · quiz q1 wx3: "…this is a result of their biconcave shape and flexibility, not the absence of a nucleus." · Losing the nucleus does help flexibility. The option is wrong only because it is not the main, examined reason. · "The main reason is more room for haemoglobin." · — · q1 usable as written. Softer wording if Design writes its own feedback.

6. **BLD-F6** · OFF-SPEC · "connective tissue", "~270 million haemoglobin molecules", "MEMORY LYMPHOCYTES", the fibrin/scab sequence, "bicarbonate". · All accurate, beyond the spec. · Spec words: blood is "a tissue"; on re-infection "white blood cells respond quickly to produce the correct antibodies". · 4.2.2.3; 4.3.1.7 · Use as context only. Don't build practice on them.

7. **BLD-F7** · IMPRECISE · File label "AQA 4.2.3.2". · AQA numbers this 4.2.2.3. · — · — · Badge the page 4.2.2.3.

## 8. The Periodic Table (`periodic-table`)

# Flags — periodic-table (AQA 8464 5.1.2.1 / 8462 4.1.2.1)

1. **PERIODIC-TABLE-F1** · ROUTE · Theory 3 "Transition Metals" (whole chunk) · Chemistry-only content (8462 4.1.3.1–4.1.3.2); not in 8464. The site ships it to Combined Foundation and Combined Higher. A separate Triple lesson, `transition-metals` (TF TH), already teaches it. · Transition metals are Triple only. · 8462 4.1.3 (chemistry only) · Drop it from this lesson, or show it as a Triple-only layer (TF TH) with nothing from it in Combined practice.

2. **PERIODIC-TABLE-F2** · ROUTE · `higher` (TH, CH): "Group 1 reactivity increases down (outer electron further from nucleus, weaker attraction, lower ionisation energy). Group 7 reactivity decreases down … Predict properties of unknown elements from position." · This is base content, not HT; the CF/TF copies are null, so Foundation pupils lose it. "Ionisation energy" is A-level. · Base on all routes: going down Group 1 the outer electron is further from the nucleus, so it is lost more easily → more reactive; going down Group 7 the outer shell is further from the nucleus, so an electron is gained less easily → less reactive. · 8464 5.1.2.1, 5.1.2.5, 5.1.2.6 / 8462 4.1.2.1, 4.1.2.5, 4.1.2.6 · Teach on every route in spec language; no Higher block; never use "ionisation energy".

3. **PERIODIC-TABLE-F3** · IMPRECISE · Theory 2: "NON-METALS become LESS REACTIVE going down" · The spec states this trend for Group 7 only; Group 0 is unreactive throughout. · "Group 7 elements become less reactive going down the group." · 8464 5.1.2.4, 5.1.2.6 · Re-cut.

4. **PERIODIC-TABLE-F4** · IMPRECISE · Theory 3 examples: "iron (Fe), copper (Cu), zinc (Zn), titanium (Ti) …" · Zinc is usually not classed as a transition element (Zn²⁺ only; colourless compounds). · Use the spec's six: Cr, Mn, Fe, Co, Ni, Cu. · 8462 4.1.3.1 · Applies only if the Triple layer is kept (F1).

5. **PERIODIC-TABLE-F5** · IMPRECISE · Theory 1: "each period represents a new electron shell being filled" · True for Periods 1–3 (all GCSE uses), not beyond. · "The period number is the number of occupied shells." · 8464 5.1.1.7 · Re-cut.

6. **PERIODIC-TABLE-F6** · IMPRECISE · q1 wx2, shown for option "2.2 — two shells and two outer electrons": "Period 3 means 3 SHELLS, not 3 electrons in the outer shell. …" · The text answers the "2.8.3" error, not "2.2". It is still true, and "Period 3 means 3 shells" rules out 2.2. · — · Usable as written; no action.

## 9. Thermal Conductivity and Reducing Unwanted Energy Transfers (`thermal-conductivity`)

# Flags — thermal-conductivity

**TC-F1** · ROUTE · page routes "Triple Foundation, Triple Higher"; spec field "6.1.3 (physics only)" · The content is base: it sits in 8464 6.1.2.1 as well as 8463 4.1.2.1, with no physics-only label. Only RP2 is physics-only. 6.1.3 is "National and global energy resources", a different lesson. · "The higher the thermal conductivity of a material the higher the rate of energy transfer by conduction across the material. Students should be able to describe how the rate of cooling of a building is affected by the thickness and thermal conductivity of its walls." · 8464 6.1.2.1; 8463 4.1.2.1 · Approved move: page → CF CH TF TH, RP2 as a TF TH layer; spec field → 8464 6.1.2.1 / 8463 4.1.2.1. Design writes the page for all four routes.

**TC-F2** · WRONG · theory chunk 2: "4. ELECTROMAGNETIC SHIELDING: Reduces energy loss from electrical components." · Shielding blocks electromagnetic interference. It is not a way of reducing unwanted energy transfers and is on no GCSE spec. · Spec's examples: "lubrication and the use of thermal insulation" · 8464 6.1.2.1 · Design: drop it.

**TC-F3** · WRONG · `higher` (TH): "Calculate rate of energy transfer through a material. Evaluate different insulation methods quantitatively using U-values or thermal conductivity data. Explain why double-glazing is more effective with wider gaps." · 6.1.2.1/4.1.2.1 has no HT statement. There is no conduction equation and no U-values in the spec. "Wider gaps are better" is false beyond ≈ 15–20 mm: convection currents form in the gap and the insulation gets worse. · — · 8464 6.1.2.1; 8463 4.1.2.1 · Do not use. No higher layer on this page.

**TC-F4** · WRONG · quiz q2 wx1: "Final temperature alone doesn't account for starting conditions or time — rate of cooling (gradient) is a fairer comparison." · In RP2 the starting temperature and the time are both controlled, so the temperature after 10 minutes (or the drop over a fixed time) is a fair comparison. AQA's own RP2 method compares exactly that. Option 2's real error is "higher temperature = better conductor": a higher final temperature means a better insulator. The feedback teaches a false method rule. · RP2: "investigate the effectiveness of different materials as thermal insulators" · 8463 4.1.2.1 RP2 (physics only) · **Do not use q2 as written.** A replacement belongs to the TF TH RP2 layer only.

**TC-F5** · GAP · theory chunk 3 / `rp`: material type is the only independent variable · RP2 has a second half the source omits. · "…and the factors that may affect the thermal insulation properties of a material." · 8463 4.1.2.1 RP2 · Design: the RP2 layer also covers one factor, e.g. thickness (number of layers of one material) as the IV, everything else controlled.

**TC-F6** · IMPRECISE · theory chunk 1: insulators transfer energy "only by vibration between tightly packed or sparse particles"; key_note: "Thermal conductivity: rate of energy transfer by conduction." · Gases conduct by occasional collisions of widely spaced particles, not vibration, which is why air is so poor. Thermal conductivity is a property of a material; a higher value gives a higher rate. · "The higher the thermal conductivity of a material the higher the rate of energy transfer by conduction" · 8464 6.1.2.1 · Design: re-cut in the spec's own words. Do not teach a definition (spec: not required) or the W/m·K unit and k × A × ΔT ÷ d (off-spec, context at most).

**TC-F7** · IMPRECISE · theory chunk 2: "Cavity wall insulation (fibreglass or foam) — reduces conduction through walls" · Cavity insulation traps air in small pockets, so it also stops convection currents in the cavity. AQA credits both "trapped air is a poor conductor" and "reduces convection". · — · 8464 6.1.2.1 · Design: give both reasons.

## 10. Coronary Heart Disease (`coronary-heart-disease`)

# Flags — coronary-heart-disease (8464/8461 4.2.2.4)

1. **CHD-F1** · ROUTE · `higher` block (all of it): statins, stents, bypass, transplant recap; "Artificial hearts provide temporary support. Faulty valves can be replaced with biological or mechanical alternatives. Each treatment has risks … and benefits to evaluate." · Hidden on Combined Foundation and Triple Foundation. 4.2.2.4 has no "(HT only)" label. · Everything in it is base. · 4.2.2.4 · Teach it on all four routes.

2. **CHD-F2** · GAP · Faulty valves are absent from the theory. · "In some people heart valves may become faulty, preventing the valve from opening fully, or the heart valve might develop a leak. Students should understand the consequences of faulty valves." · A valve that won't open fully lets less blood through; a leaking valve lets blood flow back. Less oxygenated blood reaches the body, so the patient is tired and breathless. Replaced with biological or mechanical valves. · 4.2.2.4 · Teach and practise, base. Spec text added to the source file.

3. **CHD-F3** · GAP · Artificial hearts, and "heart and lungs" transplant, are missing from the theory. · "a donor heart, or heart and lungs can be transplanted. Artificial hearts are occasionally used to keep patients alive whilst waiting for a heart transplant, or to allow the heart to rest as an aid to recovery." · As quoted. · 4.2.2.4 · Teach both uses of an artificial heart, base.

4. **CHD-F4** · OFF-SPEC · Bypass surgery (theory, common_mistake, q2 option 3). · Accurate, but not in 4.2.2.4. The spec's contrast is drugs (statins) vs mechanical devices (stents, valves, artificial hearts) vs transplant. · — · 4.2.2.4 · Keep as context. Don't make stent-vs-bypass the lesson's central contrast. q2 is still usable: bypass is only a wrong option there.

5. **CHD-F5** · IMPRECISE · "AGE — risk increases with age as arteries gradually narrow." · Contradicts q1 wx3 ("Arteries don't naturally narrow with age"), which is the correct one. · "Risk rises with age because fatty material has longer to build up." · 4.2.2.4 · Re-cut the theory line.

6. **CHD-F6** · IMPRECISE · "(though risk equalises after menopause)" · Overstated. Women's risk rises after the menopause. · "rises after the menopause" · — · Re-cut or drop (off-spec).

7. **CHD-F7** · GAP · Evaluation is thin. · The spec's first statement is "evaluate the advantages and disadvantages of treating cardiovascular diseases by drugs, mechanical devices or transplant". The source gives a few risks and no structured weighing. · Statins: no surgery, but taken long term, side effects, slow to act. Stents: quick recovery, but surgery risk and the artery can narrow again. Transplant: for heart failure, but rejection, donor shortage and immunosuppressants for life. Artificial heart: temporary, risk of clots and infection. · 4.2.2.4 · Include a 6-mark "Evaluate" item in the ladder.

8. **CHD-F8** · IMPRECISE · File label "AQA 4.2.3.3". · AQA numbers this 4.2.2.4. · — · — · Badge the page 4.2.2.4.

## 11. Biodiversity (`biodiversity`)

# Flags — biodiversity (8464/8461 4.7.3.1)

**BIODIVERSITY-F1** · WRONG · theory "What is Biodiversity?": "BIODIVERSITY is the variety of life on Earth. It has two components: SPECIES DIVERSITY — the number of DIFFERENT SPECIES in an area AND the relative abundance of each species. GENETIC DIVERSITY — the variety of ALLELES …" · Not AQA's definition. Relative abundance and genetic diversity are A-level framings, and "two components" is wrong even in general (biodiversity is usually described at genetic, species and ecosystem levels). A pupil who writes "variety of life" without "different species" risks the mark. · "Biodiversity is the variety of all the different species of organisms on earth, or within an ecosystem." · 8464/8461 4.7.3.1 · Re-cut theory to the spec definition. Genetic variation may appear only as a link to 4.6.2.1, not as part of the definition.

**BIODIVERSITY-F2** · WRONG · common_mistake: "Biodiversity is NOT just about the NUMBER of species — it also includes the RELATIVE ABUNDANCE of each species. An ecosystem with 100 species but 99% of the biomass belonging to just one species has LOW biodiversity in practice." · Contradicts the AQA definition (variety of species — 100 species is high biodiversity), and mixes biomass with abundance. · As F1. · 4.7.3.1 · Do not use. Replace with a spec misconception, e.g. "biodiversity = how many animals live there" (it is the variety of different species, plants and microorganisms included).

**BIODIVERSITY-F3** · WRONG · key_note: "Biodiversity = species diversity + genetic diversity." · As F1. The rest of the key_note is fine. · As F1. · 4.7.3.1 · Do not use the first clause.

**BIODIVERSITY-F4** · WRONG · quiz q2 wx2: "Seed banks like the Svalbard Global Seed Vault store seeds of wild plant species AND crop varieties — not food crops only." · Svalbard is the backup vault for the world's crop genebanks (crop varieties and crop wild relatives). It is the counter-example to the claim. Also: seed banks are not in 8464 or 8461 (off-spec), and distractor 2 ("grow plants for replanting…") is half-true, as wx1 concedes. · The wild-species example is Kew's Millennium Seed Bank. · — (off-spec) · **q2: do not use as written**, on any route.

**BIODIVERSITY-F5** · ROUTE · `higher` field (CH/TH only; `null` on CF/TF): "The impact of environmental change on biodiversity … evaluate conservation strategies … International agreements (e.g. Convention on Biological Diversity)" · No HT content. Threats are base (4.7.3.2–4.7.3.5); evaluating conservation is base in 4.7.3.6 (WS 1.4, 1.5); the CBD is off-spec. The genuine HT, biology-only point (8461 4.7.2.4, environmental change and species distribution) is a different lesson (`environmental-change`, TH) and is not what this text says. · — · 4.7.3.1–6; 8461 4.7.2.4 · No Higher layer in this lesson. Show nothing as HT.

**BIODIVERSITY-F6** · OFF-SPEC · quiz q1: "Why is high genetic diversity within a species important?" · Correct science (on-spec via 4.6.2.1 variation, 4.6.2.3 inbreeding), but it tests genetic diversity, which AQA does not include in biodiversity, and it reinforces F1. · — · 4.7.3.1 · Not a rung for this lesson. Extension only, if used at all.

**BIODIVERSITY-F7** · GAP · the spec's stability statement · Source says "more species = more connections = more resilience. If one species declines, others can take over its role." Correct in substance but not the mark-scheme mechanism. · "A great biodiversity ensures the stability of ecosystems by reducing the dependence of one species on another for food, shelter and the maintenance of the physical environment." Supporting interdependence: "If one species is removed it can affect the whole community." · 4.7.3.1; 4.7.1.1 · Teach the spec's three dependencies by name.

**BIODIVERSITY-F8** · IMPRECISE · theory: "approximately 75% of the world's food crops depend on animal pollinators" · Overstated. The FAO/IPBES figure is that about 75 % of leading food crop **types benefit** to some degree from animal pollination; about a third of crop production by volume. · "About three-quarters of the main food crops benefit from pollinators." · — · Re-cut, or drop the number.

**BIODIVERSITY-F9** · GAP · scope · Most of the theory (threats; seven conservation measures) is the content of 4.7.3.2–4.7.3.5 and 4.7.3.6, each a separate lesson (`waste-management`, `land-use`, `deforestation`, `global-warming`, `maintaining-biodiversity`). Invasive species, overexploitation, seed banks and legislation are off-spec; sustainable fishing is 8461 4.7.5.3 (biology only). · 4.7.3.1 asks for: definition; stability; humans rely on it; human activities reduce it; measures only recent. Plus WS 1.4 (how waste, deforestation and global warming affect biodiversity). · 4.7.3.1–6 · Keep threats and measures to a short overview linking to the sibling lessons; do not duplicate them. Minor: CITES is an international agreement, not a law.

## 12. Development of the Periodic Table (`development-periodic-table`)

# Flags — development-periodic-table (AQA 8464 5.1.2.2 / 8462 4.1.2.2)

1. **DEVELOPMENT-PERIODIC-TABLE-F1** · WRONG · q1 wx3: "Not leaving gaps was a problem for Mendeleev too initially — but the bigger issue for Newlands was that his pattern broke down after the first 16 elements." · Mendeleev's defining step was leaving gaps; he never had a no-gaps problem. The option it explains ("Newlands did not leave gaps — but neither did he need to") is half-true: no gaps was itself a reason Newlands was rejected (the source's own theory 1 and key_note say so). · Mendeleev left gaps for undiscovered elements; Newlands did not. · 8464 5.1.2.2 / 8462 4.1.2.2 · **Do not use as written.**

2. **DEVELOPMENT-PERIODIC-TABLE-F2** · GAP · Spec step missing from the source: "Knowledge of isotopes made it possible to explain why the order based on atomic weights was not always correct." · The source credits Moseley/atomic number and never mentions isotopes. · Relative atomic mass is the abundance-weighted mean mass of an element's isotopes, so an element with fewer protons can have the higher Ar if its heavier isotopes are common: argon (18 protons, Ar 39.9) comes before potassium (19, Ar 39.1); tellurium (52, Ar 127.6) before iodine (53, Ar 126.9). · 8464 5.1.2.2; 5.1.1.5–5.1.1.6 · Teach as its own step on every route; include in practice. See the source file's "Spec core missing" section. Moseley may stay as context.

3. **DEVELOPMENT-PERIODIC-TABLE-F3** · IMPRECISE · common_mistake: "Mendeleev's arrangement had a few inconsistencies because Ar and atomic number don't always match perfectly (e.g. argon and potassium)." · Argon was unknown in 1869 (discovered 1894), so it was never in Mendeleev's table. His own swap was tellurium and iodine. · "Mendeleev swapped some pairs, e.g. tellurium and iodine, to keep groups right; argon and potassium, found later, show the same problem — isotopes explain both." · 8464 5.1.2.2 · Re-cut.

## 13. Uses and Applications of Electromagnetic Waves (`uses-em-waves`)

# Flags — uses-em-waves

**UEM-F1** · WRONG · theory chunk 1: "MICROWAVE OVENS: microwave frequency matches water molecules' resonance → absorbed → food heats from inside." · 2.45 GHz is not a resonance of water. Microwaves are absorbed by water molecules in the food (dielectric heating), mostly within the outer few centimetres; the centre heats by conduction. "Heats from inside" is a popular myth. · "microwaves – … cooking food"; HT "brief explanations why each type… is suitable" · 8464 6.6.2.4; 8463 4.6.2.4 · Design: re-cut — "microwaves are absorbed by the water molecules in food, transferring energy to its thermal store" (the reason is HT).

**UEM-F2** · OFF-SPEC · `higher` (CH/TH): "Explain how optical fibres work using total internal reflection." and "Evaluate the hazards and benefits of each type in context (e.g. X-rays vs MRI vs ultrasound for medical imaging)." · Total internal reflection is in neither 8463 nor 8464. Ultrasound is not an EM wave and is "Waves for detection and exploration (physics only) (HT only)", so a CH comparison using it is off-route. · — · 8463 4.6.1.5 · Design: do not use the TIR clause. Ultrasound only as a TH-only aside, if at all. The hazard/benefit evaluation stays, from 6.6.2.3 ("draw conclusions from given data about the risks and consequences of exposure to radiation").

**UEM-F3** · ROUTE · theory glosses giving reasons ("pass through soft tissue, absorbed by bone", "pass through the atmosphere and ionosphere", "ionising types minimised"); quiz q1 and q2 · The use list is base, but the "why it suits" explanations are HT only. Both quiz items ask why, so they are HT items served to all four routes. · "(HT only) Students should be able to give brief explanations why each type of electromagnetic wave is suitable for the practical application." · 8464 6.6.2.4 (HT only); 8463 4.6.2.4 (HT only) · Design: base = wave ↔ use (CF CH TF TH); reasons in the higher layer (CH TH). q1, q2 usable on CH TH only; CF TF need their own use-matching items.

**UEM-F4** · IMPRECISE · theory chunk 1: radio "travel long distances, reflect off ionosphere"; common_mistake "radio waves for BROADCAST (reflect off ionosphere)"; q1 wx2 "reflects (most) radio waves" · Only long/medium/short-wave radio (below ≈ 30 MHz) reflects off the ionosphere; FM radio and TV pass through it and are line-of-sight. The ionosphere is not in the spec. · — · 8464 6.6.2.4 · Design: for satellites, use the creditable HT reason "microwaves pass through the atmosphere". q1 stays usable on CH TH (its keyed point is right for the radio bands that reflect).

**UEM-F5** · GAP · theory and key_note omit the spec's "ultraviolet – … sun tanning" (and key_note omits IR "cooking food") · The spec list is the examinable core; every item on it should appear. · "ultraviolet – energy efficient lamps, sun tanning"; "infrared – electrical heaters, cooking food, infrared cameras" · 8464 6.6.2.4 · Design: include all six spec pairs verbatim as the base core; link sun tanning to UV's hazard (premature skin ageing, skin cancer — 6.6.2.3).

**UEM-F6** · IMPRECISE · theory chunk 3: "ST ERILISATION"; chunk 2: IR "absorbed by surfaces, converted to heat" · Typo; "converted to heat" → "transfers energy to the thermal energy store". · — · — · Design: re-cut.
