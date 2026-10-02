# Batch 11 — science flags

Numbered per lesson. **WRONG** items are frozen text kept verbatim in the source files that must not be used as written. Each flag says what to do instead.

## 1. Development of the Model of the Atom (`model-of-the-atom`)

# Flags — model-of-the-atom

**MODEL-OF-THE-ATOM-F1** · IMPRECISE · th1: "2. Thomson's plum pudding model (1897)". 1897 is when Thomson discovered the electron. He proposed the plum pudding model in about 1904. · Spec gives no dates. · Design: date the electron 1897 and the model c. 1904, or drop the dates.

**MODEL-OF-THE-ATOM-F2** · IMPRECISE · th2: "Discovery of the ELECTRON … proved atoms were not solid or indivisible." The electron showed atoms can be divided, because they contain smaller particles. The plum pudding atom is still a solid ball of positive charge. "Mostly empty space" is the scattering experiment's finding, not Thomson's. · 8464 5.1.1.3 / 8462 4.1.1.3: "Before the discovery of the electron, atoms were thought to be tiny spheres that could not be divided." · Design: "showed atoms contain smaller particles, so they can be divided".

**MODEL-OF-THE-ATOM-F3** · IMPRECISE · th2 conclusion "a tiny, dense, positively charged NUCLEUS…"; th2 "A FEW bounced STRAIGHT BACK — hit something very dense"; key_note "Thomson: plum pudding (electrons in positive mass)". The spec's conclusion says the **mass** is concentrated at the centre and the nucleus is charged; "dense" alone does not earn that mark. Back-scattered alphas were **repelled** by the positive nucleus, not stopped by hitting it. Plum pudding is a ball of positive **charge**. · 5.1.1.3: "the mass of an atom was concentrated at the centre (nucleus) and that the nucleus was charged". · Design: use the spec's words. (Same finding as batch-5 physics `development-atomic-model` C7.)

**MODEL-OF-THE-ATOM-F4** · OFF-SPEC · th3: "Rutherford → Bohr: observed line spectra of hydrogen showed electrons could only occupy specific energy levels." True, but the spec excludes it. Also th2's "electrons can jump between shells by absorbing or emitting energy" is physics 6.4.1.1, not chemistry. · 5.1.1.3: "The theoretical calculations of Bohr agreed with experimental observations." "Details of experimental work supporting the Bohr model are not required." · Design: teach the spec sentence. Keep line spectra and electron jumps out of the chemistry page's questions.

**MODEL-OF-THE-ATOM-F5** · GAP · th3: "Protons and neutrons were later identified in the nucleus." The spec gives the proton step specifically, and the neutron timing. · 5.1.1.3: "Later experiments led to the idea that the positive charge of any nucleus could be subdivided into a whole number of smaller particles, each particle having the same amount of positive charge. The name proton was given to these particles." "The experimental work of James Chadwick provided the evidence to show the existence of neutrons within the nucleus. This was about 20 years after the nucleus became an accepted scientific idea." · Design: add both as the last two steps of the timeline.

## 2. Subatomic Particles (`subatomic-particles`)

# Flags — subatomic-particles

**SUBATOMIC-PARTICLES-F1** · IMPRECISE · th1: "Every atom contains three types of subatomic particle". Hydrogen-1, the commonest atom, has one proton, one electron and **no neutron**. · 8464 5.1.1.5 / 8462 4.1.1.5. · Design: "Atoms are made of three types of particle" plus a hydrogen-1 exception, or "most atoms".

**SUBATOMIC-PARTICLES-F2** · IMPRECISE · th3 and common_mistake: "The NUCLEUS is … about 10,000 times smaller than the whole atom". The spec compares **radii**. By volume the nucleus is about 10¹² times smaller. · 5.1.1.5: "The radius of a nucleus is less than 1/10 000 of that of the atom (about 1 x 10-14 m)." · Design: "the nucleus's radius is less than 1/10 000 of the atom's".

**SUBATOMIC-PARTICLES-F3** · ROUTE · th2: "Na → Na⁺ + e⁻", "Mg → Mg²⁺ + 2e⁻", "Cl + e⁻ → Cl⁻", "O + 2e⁻ → O²⁻". These are half equations, and writing them is HT only. As written HT half equations, the non-metals are diatomic: Cl₂ + 2e⁻ → 2Cl⁻, O₂ + 4e⁻ → 2O²⁻. · 8464 5.1.1.1 / 8462 4.1.1.1: "(HT only) write balanced half equations and ionic equations where appropriate." · Design: show ion formation in words and diagrams on all routes ("loses 2 electrons → Mg²⁺: 12 p, 10 e"). Put the e⁻ equations in an HT layer, with Cl₂/O₂ written correctly.

**SUBATOMIC-PARTICLES-F4** · GAP · The source counts electrons in ions without a mass number (q1, matching). `relative-atomic-mass` counts neutrons in neutral atoms. Neither page does the spec's named skill for an **ion** given both numbers. · 5.1.1.5: "Students should be able to calculate the numbers of protons, neutrons and electrons in an atom or ion, given its atomic number and mass number." · Design: teach it here with a worked case, e.g. ²⁷₁₃Al³⁺ → 13 p, 14 n, 10 e.

**SUBATOMIC-PARTICLES-F5** · IMPRECISE · th1: electron relative mass "approximately 1/1836 — effectively 0"; key_note "mass ~0". 1/1836 is right. The spec's word is "very small", and "0" as a written answer risks the mark. · 5.1.1.5 relative-mass table: electron "Very small". · Design: label it "very small" and add 1/1836 or ≈ 1/2000 as a note.

## 3. Relative Atomic Mass, Atomic Number and Isotopes (`relative-atomic-mass`)

# Flags — relative-atomic-mass

**RELATIVE-ATOMIC-MASS-F1** · WRONG · FIFA Insert step (frozen): "Ar = (20 × 10) + (80 × 11) ÷ 100". The outer brackets are missing. By order of operations the line evaluates to 200 + 8.8 = **208.8**, not 10.8. The next step, "(200 + 880) ÷ 100", is bracketed correctly, so the error is in the Insert line only. · Correct line: **Ar = [(20 × 10) + (80 × 11)] ÷ 100**. · 8464 5.1.1.6 / 8462 4.1.1.6; MS 1a. · Design: **do not use the Insert line as written.** Show the corrected line. Formula, Fine-tune and Answer (10.8) stand. "Bracket the whole top before ÷ 100" is worth teaching as a point, because pupils make this exact error.

**RELATIVE-ATOMIC-MASS-F2** · OFF-SPEC + ROUTE · `higher` (CH/TH only): "Use mass spectrometry data … Interpret mass spectra showing relative abundance on y-axis and mass/charge on x-axis. Understand that non-integer Ar values result from isotope mixtures." Mass spectrometry is not in GCSE: "mass spectr" appears nowhere in 8462 or 8464. The last sentence is base content. 5.1.1.6 has no HT label: calculating Ar from % abundance is required of **every** route. · 5.1.1.6: "Students should be able to calculate the relative atomic mass of an element given the percentage abundance of its isotopes." · Design: no HT layer on this page. No mass spectra. The Ar calculation goes to all four routes.

**RELATIVE-ATOMIC-MASS-F3** · IMPRECISE · th3: "Because most elements have multiple isotopes in different abundances, Ar is NOT a whole number." Many Ar values on the AQA periodic table are whole numbers (C 12, O 16, Na 23). Elements with one stable isotope (F, Na, Al) have Ar close to a whole number. · 5.1.1.6. · Design: "Ar is **often** not a whole number" (as the common_mistake and key_note already say).

**RELATIVE-ATOMIC-MASS-F4** · IMPRECISE · th1: "In the periodic table, the ATOMIC NUMBER is the SMALLER number (it cannot exceed the mass number…)". On the AQA periodic table the two numbers are **relative atomic mass** and atomic number. Mass number belongs to one isotope's symbol, ²³₁₁Na. Merging them is the confusion this lesson exists to clear up. · 5.1.1.5–5.1.1.6. · Design: show the nuclear symbol (mass number top, atomic number bottom) and the periodic-table box (Ar and atomic number) separately, and name both.

**RELATIVE-ATOMIC-MASS-F5** · IMPRECISE · q1 wx1, explaining option 1 "Same: mass number. Different: atomic number and proton count.": "If mass numbers were the same they would be identical — isotopes are DEFINED by having different mass numbers." It does not address the option's other half: a different atomic number means a different **element**. Not false. · 5.1.1.4. · Design: q1 is usable as written. If the explanation is re-cut, add "Different atomic numbers would make them different elements."

## 4. Electronic Structure (`electronic-structure`)

# Flags — electronic-structure

**ELECTRONIC-STRUCTURE-F1** · ROUTE · `higher` (CH/TH only): "Electronic configurations for all elements 1–20. Predict chemical properties from electronic structure … Explain why period number = number of shells, and group number = outer electrons." All base. Neither spec point carries an HT label, and Foundation pupils are examined on all of it. · 8464 5.1.1.7 / 8462 4.1.1.7: "represent the electronic structures of the first twenty elements … in both forms"; 5.1.2.1 / 4.1.2.1: "explain how the position of an element in the periodic table is related to the arrangement of electrons in its atoms". · Design: no HT layer. Teach all of it on all four routes.

**ELECTRONIC-STRUCTURE-F2** · IMPRECISE · th3: "Group 0: 8 outer electrons (full shell) — He: 2, Ne: 2.8, Ar: 2.8.8". The heading says 8 and the first example has 2. · 8464 5.1.2.4 / 8462 4.1.2.4: "The noble gases have eight electrons in their outer shell, except for helium, which has only two electrons." · Design: say "full outer shell: 8, except helium (2)".

**ELECTRONIC-STRUCTURE-F3** · GAP · The source gives only the number form, written with dots ("2.8.1"). The spec requires both forms, and its number form uses commas. · 5.1.1.7: "The electronic structure of an atom can be represented by numbers or by a diagram. For example, the electronic structure of sodium is 2,8,1 or [diagram]…" "represent the electronic structures of the first twenty elements … in both forms." · Design: teach the diagram form (electrons on concentric shells) alongside the numbers. Write the numbers as AQA does (2,8,1); AQA also accepts 2.8.1.

**ELECTRONIC-STRUCTURE-F4** · IMPRECISE (note; item usable) · q1 option 2 "Group 16 — add all the electrons together". Sulfur's IUPAC group number is 16, so a pupil who knows IUPAC numbering may hesitate. On the AQA periodic table (groups 1–7 and 0) the key "Group 6" is right, and the option's reasoning is wrong either way. · 5.1.2.1. · Design: q1 usable as written. Say on the page that this course numbers groups 1–7 and 0.

## 5. Group 7 — Halogens (`group-7`)

# Flags — group-7

**GROUP-7-F1** · WRONG · th2: "MELTING AND BOILING POINT INCREASE: F₂: −188°C, Cl₂: −101°C, Br₂: 59°C, I₂: 184°C." Three are boiling points; −101 °C is chlorine's **melting** point. Chlorine's boiling point is **−34 °C**. · Boiling points: F₂ −188, Cl₂ −34, Br₂ 59, I₂ 184 °C. Melting points if wanted: −220, −101, −7, 114 °C. · 8464 5.1.2.6 / 8462 4.1.2.6: "the further down the group an element is the higher its relative molecular mass, melting point and boiling point". · Design: do not reuse the series as written. Use one property, labelled.

**GROUP-7-F2** · IMPRECISE / OFF-SPEC term · th2: "Larger molecules → stronger London dispersion forces → higher boiling point." "London dispersion" is A-level. · 8464 5.2.2.4 / 8462 4.2.2.4: "The intermolecular forces increase with the size of the molecules, so larger molecules have higher melting and boiling points." · Design: say "intermolecular forces". Also say relative molecular mass increases down the group, which the spec names.

**GROUP-7-F3** · GAP · The source covers halogens with metals (salts, −1 halide ions) but not with non-metals. · 5.1.2.6: "Students should be able to describe the nature of the compounds formed when chlorine, bromine and iodine react with metals and non-metals." · Design: with metals, ionic compounds containing halide ions (−1). With non-metals, covalent molecular compounds, e.g. H₂ + Cl₂ → 2HCl (hydrogen chloride).

**GROUP-7-F4** · IMPRECISE (frozen) · q2 wx1, explaining option 1 "Fluorine has fewer electrons, making it less stable and more reactive": "Fewer electrons in an outer shell means the atom needs to GAIN electrons — but that doesn't directly explain why fluorine attracts electrons more strongly. The distance from the nucleus is the key factor." The first sentence suggests fluorine has fewer **outer** electrons than chlorine. Both have 7. Fluorine has fewer electrons only in total. · 5.1.2.6 (seven outer electrons). · Design: **do not use q2 as written.** Use it with wx1 replaced by: "Fluorine and chlorine both have 7 outer electrons. Fewer electrons in total is not the reason — fluorine's outer shell is closer to the nucleus, so it attracts an incoming electron more strongly."

**GROUP-7-F5** · ROUTE · `higher` (CH/TH only): "…lower electron affinity → less reactive. Astatine predicted to be solid, dark coloured and least reactive halogen. Displacement reactions as reactivity evidence." The astatine prediction and displacement-as-evidence are **base** ("predict properties from given trends down the group"). "Electron affinity" is A-level. This page's real HT layer is not in the source. · 8464 5.4.1.4 / 8462 4.4.1.4 (HT only): "write ionic equations for displacement reactions; identify … which species are oxidised and which are reduced"; 5.1.1.1 / 4.1.1.1 (HT only) half equations. · Design: astatine on all routes. HT layer: Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂, with chlorine reduced (gains electrons) and bromide oxidised (loses electrons). It links to `oxidation-reduction` in this batch.

## 6. Properties of Transition Metals (`transition-metals`)

# Flags — transition-metals

**TRANSITION-METALS-F1** · WRONG (frozen) · q2 wx2, explaining option 2 "Platinum — the most effective transition metal catalyst": "Platinum is used in catalytic converters for car exhaust and in the Contact process — not the Haber process." The present-day Contact process uses **vanadium(V) oxide**, which this lesson's own th2 states. Platinum was the early Contact catalyst and has long been replaced. The Contact process is not in 8462 anyway. · 8462 4.1.3.2; 4.10.4.1 ("a catalyst of iron"). · Design: **do not use q2 as written.** Use it with wx2 replaced by: "Platinum is a catalyst in catalytic converters for car exhausts — the Haber process uses iron."

**TRANSITION-METALS-F2** · OFF-SPEC + ROUTE · `higher` (TH only): "Write balanced ionic equations … Explain variable oxidation states in terms of d-electron configuration — … 3d and 4s subshells. Calculate the oxidation state of a transition metal from a compound formula. Evaluate the use of specific transition metals as catalysts with reference to their variable oxidation states." This is A-level. 8462 4.1.3 carries no HT label and no sub-shells. · 8462 4.1.3 "(chemistry only)", no HT. · Design: no HT layer. TF and TH get the same page.

**TRANSITION-METALS-F3** · GAP · (a) th1's comparison table covers water and oxygen but not **halogens**, which the spec lists. (b) The spec's exemplar metals are Cr, Mn, Fe, Co, Ni, Cu, and Mn is missing from th1's list. Zn is included, but Zn forms only Zn²⁺ and colourless compounds, so it shows none of the typical properties. · 8462 4.1.3.1: "describe the difference compared with Group 1 in melting points, densities, strength, hardness and reactivity with oxygen, water and halogens … exemplify … by reference to Cr, Mn, Fe, Co, Ni, Cu"; 4.1.3.2: "exemplify … by reference to compounds of Cr, Mn, Fe, Co, Ni, Cu". · Design: add a halogens row (Group 1 burn vigorously in chlorine to form white chlorides; hot iron wool reacts less vigorously, giving orange-brown iron(III) chloride). Build the examples and colours on the six metals, e.g. Cu²⁺ blue, Fe²⁺ green, Fe³⁺ orange-brown, Ni²⁺ green, Co²⁺ pink, manganate(VII) purple, dichromate orange. Do not use zinc as a typical transition metal.

**TRANSITION-METALS-F4** · IMPRECISE · th2: "Manganese: Mn²⁺, Mn⁴⁺, Mn⁷⁺ (in permanganate)." Mn²⁺ is a real ion. Manganese is +4 in MnO₂ and +7 inside the MnO₄⁻ ion, but free Mn⁴⁺ and Mn⁷⁺ ions do not exist. "Oxidation state" is not GCSE language. · 8462 4.1.3.2: "Many transition elements have ions with different charges". · Design: show "ions with different charges" with Fe²⁺/Fe³⁺ and Cu⁺/Cu²⁺. Present manganate(VII) only as a coloured compound.

## 7. Mass Changes in Reactions (`mass-changes-reactions`)

# Flags — mass-changes-reactions

**MCR-F1** · WRONG · th1, under "WHEN MASS APPEARS TO DECREASE": "Mg ribbon burning — ash (MgO) seems lighter than the ribbon, but this is because oxygen from AIR was added. Without accounting for the oxygen, mass appears lost." · Contradicts itself and th1's own increase section. · The oxide is heavier than the metal (spec's own example). A falling crucible reading is MgO smoke escaping when the lid is lifted, not oxygen. · 8464 5.3.1.3 / 8462 4.3.1.3 · Delete it from the decrease list; Mg burning is the INCREASE example only.

**MCR-F2** · ROUTE · th2 "Predicting Mass Changes" (moles) and the FIFA (4.8 g Mg → 8.0 g MgO) · Unbadged on all four routes. · Calculating masses from a balanced equation, and moles, are HT only. · 8464 5.3.2.1–5.3.2.2 / 8462 4.3.2.1–4.3.2.2 (HT only) · HT-badge th2 and the FIFA; CH TH only. Give CF TF a base CFIFA: mass of gas = mass before − mass after (5.3.1.1), or the 5.3.1.2 check that 2 × 24 + 32 = 2 × 40.

**MCR-F3** · GAP · th1–th3 · Spec asks pupils to "explain these changes in terms of the particle model"; the data only says "gas molecules leave the container". · Gas particles move freely and spread out of an open vessel, taking their mass with them; oxygen particles from the air bond to metal atoms and become part of the solid. · 8464 5.3.1.3 / 8462 4.3.1.3 · Teach the particle explanation for both directions.

**MCR-F4** · IMPRECISE · q2 wx1: "Humidity can contribute, but the primary reason is oxygen being ABSORBED from the air. The reaction is 4Fe + 3O₂ → 2Fe₂O₃" · Rust is hydrated iron(III) oxide; water is required and adds mass too. The equation is for anhydrous iron(III) oxide. · Both air and water are needed for iron to rust. · 8462 4.10.3.1 (chemistry only) · q2 stays usable (key correct, base reasoning). Do not repeat "4Fe + 3O₂ → 2Fe₂O₃" as the rusting equation in teaching text.

**MCR-F5** · IMPRECISE · FIFA F step: "2 × Mr(Mg) : 2 × Mr(MgO) = 48 : 80" · Mg is an element: Ar, not Mr. Numbers correct. · 8464 5.3.1.2 · Frozen; show as is. In Design's own text write Ar(Mg).

## 8. Chemical Measurements (`chemical-measurements`)

# Flags — chemical-measurements

**CM-F1** · GAP · whole file · The spec's own demand is missing: "use the range of a set of measurements about the mean as a measure of uncertainty" and "represent the distribution of results and make estimations of uncertainty". · Uncertainty = ± half the range about the mean (e.g. 24.10, 24.30, 24.20 cm³ → 24.20 ± 0.10 cm³). · 8464 5.3.1.4 / 8462 4.3.1.4; WS 3.4 · Make mean ± half-range the lesson's core and its CFIFA flagship (written from the spec into the source file).

**CM-F2** · OFF-SPEC · equations "% uncertainty = (uncertainty ÷ measured value) × 100"; th2; key_note; FIFA; q1 · Percentage uncertainty is not in 8462 or 8464 (A-level content). Arithmetic all correct. · See CM-F1. · — · Keep only as a labelled extension. Never put it in the place of the core calculation. q1 usable as an extension item only.

**CM-F3** · WRONG · q2 (stem "a burette or measuring cylinder"), option 1 "From the top of the meniscus — this gives the largest volume reading" and wx1 "Reading from the TOP of the meniscus gives an overestimate"; also common_mistake "Reading from the top overestimates the volume" · True for a measuring cylinder; false for a burette, whose scale reads downward, so the top of the meniscus gives the smaller reading. · Read the bottom of the meniscus at eye level on both; the direction of the error depends on which way the scale runs. · AT 1 · **q2: do not use as written.** Re-cut the common_mistake to the cylinder only, or explain both directions.

**CM-F4** · IMPRECISE · th1/key_note "PRECISION — how reproducible/consistent measurements are"; th3 "Repeat and average for reliability"; q1 wx1 "precision depends on the uncertainty relative to the measurement" · Mixes precision, reproducibility and % uncertainty; "reliability" is not an AQA term. · AQA: accurate = close to the true value; precise = cluster closely; repeatable = same investigator, same conditions; reproducible = different investigators, different equipment. · WS 3.7 · Use AQA's four definitions word for word.

**CM-F5** · IMPRECISE · key_note "Burette: ±0.05 cm³ — most precise for volumes" · A pipette delivers its one fixed volume with the smaller uncertainty; a burette titre carries two readings (±0.10 cm³). · — · Say: pipette for one fixed volume, burette for a variable volume.

## 9. Moles (`moles`)

# Flags — moles

**MOL-F1** · IMPRECISE · q2 option 2 "30100 g — multiplying particle count by Mr" with wx2 "The Mr gives mass PER MOLE — 3.01 × 10²³ is only 0.5 mol, not 1 mol." · wx2 explains option 1's error (taking 1 mol), not option 2's; and option 2's figure does not follow its own stated error (3.01 × 10²³ × 100 = 3.01 × 10²⁵ g, not 30100). · The key (50 g) and the other two explanations are right. · 8464 5.3.2.1 · q2 usable; any per-option feedback Design writes for option 2 should address "particle count × Mr".

**MOL-F2** · IMPRECISE · th2 "What mass of NaOH contains 3.01 × 10²³ molecules?" · NaOH is ionic; it has formula units, not molecules. Arithmetic ✓. · Moles apply to "atoms, molecules, ions, electrons, formulae". · 8464 5.3.2.1 · Re-cut: "formula units".

**MOL-F3** · IMPRECISE · th1 "This number is chosen because: 1 mole of carbon-12 atoms has a mass of exactly 12 grams." · The pre-2019 definition; no longer exact. Not needed. · "The mass of one mole of a substance in grams is numerically equal to its relative formula mass." · 8464 5.3.2.1 · Re-cut to the spec sentence.

**MOL-F4** · ROUTE · th3 / key_note / equation 4 "% mass = (Ar × number of atoms ÷ Mr) × 100" · Base content (8464 5.3.1.2), on an HT-only page. · Its Foundation home is `relative-formula-mass` (CF CH TF TH). · 8464 5.3.1.2 · Treat it as a recap here, not new HT content; link to relative-formula-mass.

**MOL-F5** · IMPRECISE · CFIFA Convert line "matching the g/mol basis of Ar" · Ar is a relative mass with no unit. · Corrected line written into the source file. · 8464 5.3.1.2 · Use the corrected line.

## 10. Amounts of Substances in Equations (`amounts-in-equations`)

# Flags — amounts-in-equations

**AIE-F1** · WRONG · th3 "Atom economy = (Mr of desired products ÷ Mr of ALL products) × 100"; key_note "Atom economy = (Mr desired ÷ Mr all products) × 100"; equations[2] "atom economy = (Mr desired products ÷ Mr all products) × 100" · Not AQA's formula. A products denominator gives the same number only when every product is counted with its coefficient (conservation, 4.3.1.2); as worded it invites dropping coefficients. It is also off-topic here (chemistry only, with its own page). · AQA: atom economy = (Mr of desired product from equation ÷ sum of Mr of all reactants from equation) × 100. · 8462 4.3.3.2 (chemistry only) · **Do not use equations[2] or the atom-economy text.** Leave atom economy off this page; link to `atom-economy` (TF TH).

**AIE-F2** · ROUTE / OFF-SPEC · th3 yield text; key_note "% yield = (actual ÷ theoretical) × 100"; equations[1]; q2 (80 %) · Percentage yield is 8462 4.3.3.1 (chemistry only) and is not in 8464, so it is off-spec on Combined Higher, where this page also runs. It has its own page, `percentage-yield` (TF TH). Science correct. · — · 8462 4.3.3.1 (chemistry only) · Recommended: leave out and link. If kept, TH only and triple-badged; q2 then usable on TH only.

**AIE-F3** · IMPRECISE · th2: the method lists "Step 1: Write the balanced equation … Step 5: Convert moles back to mass", but the worked example numbers four steps with different meanings ("Step 1: 2 mol Mg → 2 mol MgO (ratio 1:1)"). · Two numberings for one method. · — · — · Re-cut to one numbered method, used identically in the example and around the FIFA.

**AIE-F4** · GAP · whole file · Spec bullet "calculate the masses of substances shown in a balanced symbol equation" is not taught as such. · e.g. 2Mg + O₂ → 2MgO reads as 48 g + 32 g → 80 g. · 8464 5.3.2.2 (HT only) · Teach it before the reacting-mass chain.

**AIE-F5** · IMPRECISE · q2 option 2 "5% — % yield = (5 ÷ 25) × 100 (using the difference)" · The option's own working gives 20 %, which is option 3. Key and explanations right. · — · 8462 4.3.3.1 · Only matters if q2 is kept (TH, AIE-F2).

## 11. Oxidation and Reduction (`oxidation-reduction`)

# Flags — oxidation-reduction

**OXR-F1** · ROUTE · key_note "Oxidation: gain O / lose electrons. Reduction: lose O / gain electrons. OIL RIG…" and equations "Oxidation = gain of oxygen / loss of electrons", "Reduction = loss of oxygen / gain of electrons", "OIL RIG: …" — shown on CF TF unbadged; th2 is introduced only as "At a more advanced level" · The electron definition is HT only. · Base: oxidation = gain of oxygen, reduction = loss of oxygen. HT: oxidation = loss of electrons, reduction = gain of electrons. · 8464 5.4.1.1, 5.4.1.3 (base); 8464 5.4.1.4 (HT only) · Split every mixed line: the oxygen half on all routes, the electron half (and th2, OIL RIG, q2) HT-badged on CH TH only.

**OXR-F2** · OFF-SPEC · oxidising agent / reducing agent — th2 tail, th3, common_mistake ("agents do the opposite of what they're called"), key_note, `higher` ("Identify oxidising agents… and reducing agents"), q1 ("what is the reducing agent?") · Correct chemistry, not AQA GCSE content: "reducing agent" is nowhere in 8462/8464; "oxidising agent" appears only undefined in the alcohols section. · The spec's demand is "identify the substances which are oxidised or reduced" (oxygen, base; electrons, HT). · 8464 5.4.1.3, 5.4.1.4 · Drop the agent terms. **q1: do not use as written** (off-spec term; its oxidised/reduced reasoning should be rebuilt by Design as an on-spec item).

**OXR-F3** · WRONG · th1 "Mg + O₂ → MgO" (also in the matching, which is replaced anyway) · Unbalanced. · 2Mg + O₂ → 2MgO. · 8464 5.3.1.1 · Re-cut with the balanced equation.

**OXR-F4** · WRONG · th2 "Cl + e⁻ → Cl⁻" and "Na + Cl → Na⁺ + Cl⁻" · Chlorine exists as Cl₂ molecules; the half equation for a single atom is not what AQA credits. · Cl₂ + 2e⁻ → 2Cl⁻; 2Na + Cl₂ → 2NaCl. Better on-spec HT example: displacement ionic equation Mg + Cu²⁺ → Mg²⁺ + Cu (Mg oxidised, Cu²⁺ reduced). · 8464 5.4.1.4 (HT only) · Re-cut with Cl₂, or use the displacement example.

**OXR-F5** · IMPRECISE / OFF-SPEC · th3 "Carbon in the blast furnace: reduces iron oxide — carbon is the REDUCING AGENT (it gets oxidised to CO₂)"; also potassium manganate(VII), hydrogen peroxide · Extraction details are "not required"; in the blast furnace CO is the main reductant. · On-spec: carbon reduces a metal oxide, e.g. 2CuO + C → 2Cu + CO₂ (CuO loses oxygen: reduced; carbon gains oxygen: oxidised). · 8464 5.4.1.3 · Use the carbon + metal-oxide example; drop the blast furnace and the extra agents.

**OXR-F6** · GAP · quiz · No usable frozen item on CF TF (q1 off-spec, q2 HT). The HT layer also misses 5.4.2.1 (HT): metals + acids as redox, and writing displacement ionic equations (5.4.1.4). · — · 8464 5.4.1.3; 5.4.1.4; 5.4.2.1 (HT only) · Design writes oxygen-based "which is oxidised, which is reduced?" items for every route, and an ionic-equation item for CH TH.

## 12. Making Salts and Neutralisation (`salts-neutralisation`)

# Flags — salts-neutralisation

**SN-F1** · WRONG · `rp`: "RP3 (Chemistry) — Prepare a sample of a pure, dry hydrated copper sulfate salt starting from copper oxide and sulfuric acid using add-excess-solid method." · The number is wrong. Chemistry RP3 is electrolysis of aqueous solutions. · Making a soluble salt is **Combined RP8** (8464 5.4.2.3) and **Chemistry RP1** (8462 4.4.2.3), common to both: "preparation of a pure, dry sample of a soluble salt from an insoluble oxide or carbonate, using a Bunsen burner to heat dilute acid and a water bath or electric heater to evaporate the solution." The method in the field is correct. · 8464 5.4.2.3; 8462 4.4.2.3, §8.2.1 · Frozen text stays; do not show "RP3". Label the practical "Combined RP8 · Chemistry RP1" on all four routes.

**SN-F2** · ROUTE · th1 "METHOD 2 — Titration (for soluble salts from soluble starting materials) …"; th3 titration procedure (pipette, burette, phenolphthalein, concordant titres, repeat without indicator); key_note "Soluble salt from two soluble reactants: titration to find volumes, then repeat without indicator." · Served on all four routes. Titration is chemistry only, and AQA's soluble-salt statement asks only for the insoluble-solid method. · "The volumes of acid and alkali solutions that react with each other can be measured by titration using a suitable indicator." · 8462 4.4.2.5 (chemistry only) · Triple layer on TF TH only, linked to the `titrations` lesson (TF TH). CF CH: the excess-solid method only.

**SN-F3** · OFF-SPEC · th2 "Making Insoluble Salts — Precipitation" (whole chunk); key_note "Insoluble salt: mix two solutions, precipitate forms, filter/wash/dry."; equations "BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq)" · Preparing an insoluble salt by precipitation is in neither 8464 nor 8462. AQA meets BaCl₂ and AgNO₃ precipitates only as ion tests, chemistry only, and with acid present. The chemistry is correct. · "Sulfate ions in solution produce a white precipitate with barium chloride solution in the presence of dilute hydrochloric acid." "Halide ions in solution produce precipitates with silver nitrate solution in the presence of dilute nitric acid." · 8462 4.8.3.4–4.8.3.5 (chemistry only) · Do not teach or test as core. If kept at all, one line of triple context pointing to the ion-tests lesson.

**SN-F4** · IMPRECISE · th1 step 3 "EVAPORATE the filtrate to crystallise the salt, or leave to crystallise slowly." · Read as "evaporate to dryness", which spits and drives the water of crystallisation out of hydrated copper sulfate (blue → white). · RP: "a water bath or electric heater to evaporate the solution". Heat until crystals start to form at the edge, then leave to cool and crystallise; pat dry between filter papers. · 8464 5.4.2.3 RP8; 8462 RP1 · Re-cut the step.

**SN-F5** · WRONG · q1 wx2: "You cannot add more solid than the acid can react with — excess produces the same yield." · The first clause is false: adding more solid than the acid can react with is exactly what "excess" means, and it is the method. · "The solid is added to the acid until no more reacts and the excess solid is filtered off." The acid limits how much salt forms; once it is used up, extra solid makes no more salt. · 8464 5.4.2.3 · q1 **do not use as written**. Design writes a replacement "why add excess?" item (key: so all the acid reacts / none is left to contaminate the salt).

**SN-F6** · IMPRECISE (minor) · q2 wx2: "This is a precipitation ionic equation — it describes salt formation, not neutralisation." · NaCl is soluble; Na⁺ and Cl⁻ do not precipitate when they meet in solution. · Na⁺ and Cl⁻ are spectator ions in neutralisation; only H⁺ and OH⁻ react. · 8464 5.4.2.4 · q2 usable verbatim on all four routes.

**SN-F7** · GAP (minor) · th3 "NEUTRALISATION is the reaction between an ACID and a BASE (or alkali) to form a SALT and WATER." · Omits carbonates, which Method 1 uses. Fizzing stopping, with solid left over, is how a pupil knows the carbonate is in excess. Naming the salt from the acid is in the sibling `reactions-of-acids`. · "… and by metal carbonates to produce salts, water and carbon dioxide." "hydrochloric acid produces chlorides, nitric acid produces nitrates, sulfuric acid produces sulfates" · 8464 5.4.2.2 · Add the carbonate line, and "add until no more fizzes and some solid is left" for the carbonate version of the method.

## 13. The pH Scale and Neutralisation (`ph-scale`)

# Flags — ph-scale

**PH-F1** · ROUTE · th1 "The pH SCALE measures the CONCENTRATION of hydrogen ions (H⁺) …" and "The pH scale is LOGARITHMIC — each unit change represents a 10× change in H⁺ concentration: pH 3 has 10× more H⁺ than pH 4. pH 3 has 100× more H⁺ than pH 5."; th2 "The MORE H⁺ ions in solution → LOWER pH"; key_note "pH scale is logarithmic — each unit = 10× change in H⁺."; q1 (pH 2 vs pH 4, 100×) · Served on all four routes. The factor of 10, and describing acidity by H⁺ concentration, are HT only. The science is correct. · "As the pH decreases by one unit, the hydrogen ion concentration of the solution increases by a factor of 10." "describe neutrality and relative acidity in terms of the effect on hydrogen ion concentration and the numerical value of pH (whole numbers only)" · 8464 5.4.2.5 / 8462 4.4.2.6 (HT only) · HT layer on CH TH; q1 on **CH TH only**. Base routes: acids < 7, alkalis > 7, lower pH = more acidic. This content is the core of `strong-weak-acids` (CH TH); teach it there, and here only as a link or an HT layer.

**PH-F2** · IMPRECISE · th1 "pH 0–6: ACIDIC … pH 8–14: ALKALINE"; key_note "pH 0–6: acidic. pH 7: neutral. pH 8–14: alkaline." · Leaves 6–7 and 7–8 unassigned; pH 6.5 is acidic. · "Aqueous solutions of acids have pH values of less than 7 and aqueous solutions of alkalis have pH values greater than 7." · 8464 5.4.2.4 · Use "below 7 / exactly 7 / above 7" everywhere, including any scale figure.

**PH-F3** · IMPRECISE · th1 "Hydrochloric acid (conc.): pH ~0–1" (and matching "pH 4 — … black coffee or tomato juice") · Concentrated HCl (~12 mol/dm³) is below pH 0. pH ~0–1 is dilute bench acid. Black coffee is ≈ 5. · — · — · Write "dilute hydrochloric acid: pH ~1". The matching is replaced anyway.

**PH-F4** · OFF-SPEC · th2 litmus and phenolphthalein; key_note "Phenolphthalein: colourless in acid, pink in alkali."; th3 "WHY SUCH A SHARP CHANGE NEAR THE END POINT: …" · The base spec names universal indicator (or a wide range indicator) and the pH probe only. Phenolphthalein is a titration indicator (chemistry only). Explaining the steep part of the curve needs the log scale and is beyond GCSE. th3 also mixes "end point" with "equivalence point". The pH-change curve itself is the spec's AT 3 opportunity and is fine on all routes. · "describe the use of universal indicator or a wide range indicator to measure the approximate pH of a solution"; AT 3 "investigate pH changes when a strong acid neutralises a strong alkali" · 8464 5.4.2.4; 8462 4.4.2.5 (chemistry only) · Core is UI (match the colour to a chart, approximate pH) and pH probe. Keep the curve as data to read. Drop the "why" paragraph. Litmus only as KS3 recall.

**PH-F5** · GAP · The neutralisation ionic equation is absent from this file. · It is in this lesson's own spec clause, and the data places it only in `salts-neutralisation`. · "In neutralisation reactions between an acid and an alkali, hydrogen ions react with hydroxide ions to produce water." H⁺(aq) + OH⁻(aq) → H₂O(l) · 8464 5.4.2.4 / 8462 4.4.2.4 · Teach it here on all four routes. Added to the source file under "Spec core missing".

**PH-F6** · IMPRECISE (minor) · q2 wx3: "Unless you add enormous amounts of water, the pH approaches 7 gradually but never quite reaches it — you are diluting, not neutralising." · "Unless …" implies enough water would reach 7; diluting an acid never reaches or passes 7. Key and alignment correct. · — · 8464 5.4.2.4 · q2 usable verbatim on all four routes.

## 14. Strong and Weak Acids (`strong-weak-acids`)

# Flags — strong-weak-acids

**SWA-F1** · WRONG · th3 "But: if EXCESS acid is used, both eventually produce the SAME amount of H₂. Why: both have the same TOTAL number of acid molecules — weak acid eventually fully reacts." and "Weak acid: effervescence slower — same total CO₂ ultimately produced." · The condition is backwards. With excess acid, the metal is the limiting reactant, so equal H₂ follows trivially and the stated reason is irrelevant. · Equal volumes of the two acids at the same concentration, with **excess magnesium** (or excess carbonate), give the same total H₂ (or CO₂): the acid is limiting, both contain the same amount of acid, and the weak acid keeps ionising as its H⁺ ions are used up. It just takes longer. · 8464 5.4.2.5 / 8462 4.4.2.6 (HT only) · Theory is re-cuttable: rewrite with "excess magnesium / excess carbonate, equal volumes, same concentration".

**SWA-F2** · OFF-SPEC · th2 "EFFECT OF DILUTION on weak acids: Adding water → equilibrium shifts RIGHT (more ionisation) → slightly more H⁺. Weak acids become relatively more ionised on dilution." · A-level. "Slightly more H⁺" is misleading: the H⁺ **concentration** falls and the pH rises on dilution; only the fraction ionised rises. · Spec asks only for dilute/concentrated "in terms of amount of substance". · 8464 5.4.2.5 · Drop the paragraph.

**SWA-F3** · GAP · The spec's own statement on the factor of 10 per pH unit, and relative acidity from whole-number pH (MS 2h), are not in this file. In the data they sit in `ph-scale`, served on all four routes (PH-F1). · "As the pH decreases by one unit, the hydrogen ion concentration of the solution increases by a factor of 10." "describe neutrality and relative acidity in terms of the effect on hydrogen ion concentration and the numerical value of pH (whole numbers only)." · 8464 5.4.2.5 / 8462 4.4.2.6 (HT only) · Teach it here, with a worked example (th2's own numbers: pH 1 vs pH 3 → 10 × 10 = 100 times the H⁺ concentration). Added to the source file under "Spec core missing".

**SWA-F4** · IMPRECISE (minor) · th1 "dissociate into H⁺ and the conjugate base"; q1 wx3 "(monoprotic)"; HF as an example · A-level vocabulary. HF is not one of AQA's examples (ethanoic, citric, carbonic). · — · 8464 5.4.2.5 · Say "H⁺ ions and negative ions". q1 is usable verbatim (bracketed term). Lead with the spec's named acids.

## 15. The Process of Electrolysis (`electrolysis-principles`)

# Flags — electrolysis-principles

**EP-F1** · ROUTE · th2 "At the cathode: cations GAIN electrons → REDUCED …", "At the anode: anions LOSE electrons → OXIDISED …", "Oxidation at the Anode (OA). Reduction at the Cathode (RC). Memory: AN OX, A RED CAT"; common_mistake and key_note (same); q2 "During electrolysis, where does oxidation take place?" · Served on all four routes. Electron gain/loss at the electrodes, and naming it reduction/oxidation, are HT only. Base routes learn only which ions move where and that they are discharged as elements. · Base: "Positively charged ions move to the negative electrode (the cathode), and negatively charged ions move to the positive electrode (the anode). Ions are discharged at the electrodes producing elements." HT: "at the cathode … positively charged ions gain electrons and so the reactions are reductions. At the anode … negatively charged ions lose electrons and so the reactions are oxidations." · 8464 5.4.3.1, 5.4.3.5 (HT only); 5.4.1.4 (HT only) · HT layer on CH TH; q2 on **CH TH only**. CF TF: ions move to the oppositely charged electrode and are discharged.

**EP-F2** · WRONG · q1 option 3 "Electrolysis only works on liquids — all solids resist decomposition." with wx3 "Some solids are electrolysed — e.g. electrolysis of a metal anode in electroplating. The issue specifically with NaCl solid is fixed ions." · The wx is false. No solid is ever the electrolyte; in electroplating the electrolyte is an aqueous solution and the metal anode is an electrode. The distractor's first clause is nearly true (electrolytes are molten or dissolved), so a pupil who picked it is corrected with a falsehood. · "When an ionic compound is melted or dissolved in water, the ions are free to move … These liquids and solutions are able to conduct electricity and are called electrolytes." · 8464 5.4.3.1 · q1 **do not use as written**. Design writes a replacement "why must it be molten or dissolved?" item.

**EP-F3** · OFF-SPEC · th1 "Electroplate metals …", "Purify metals (e.g. copper refining)", "Manufacture chemicals (e.g. chlorine and sodium hydroxide from brine)"; th3 "REACTIVE ELECTRODES (e.g. copper in electroplating) …" · Correct chemistry, but in neither 8464 nor 8462 (brine and copper refining were legacy-spec content). · — · — · Context at most; never test it, never let it outweigh the spec's uses (extracting reactive metals, 5.4.3.3).

**EP-F4** · IMPRECISE (minor) · th2 "→ solid metal or hydrogen gas deposited." · A gas is produced (given off), not deposited. · — · 8464 5.4.3.4 · Re-cut: "metal coats the cathode, or hydrogen gas bubbles off".

**EP-F5** · ROUTE (minor) · `higher` (served CH TH): "Understand that current is carried by ions in solution and by electrons in external circuit." · Correct, but not HT: it is the base idea that ions move to the electrodes. The rest of the field (half equations, oxidation at anode) is correctly HT. · — · 8464 5.4.3.1 · Teach this sentence on all four routes.

## 16. Electrolysis of Molten Ionic Compounds (`electrolysis-molten`)

# Flags — electrolysis-molten

**EM-F1** · WRONG · `rp`: "RP4 (Chemistry) — Carry out electrolysis of lead(II) bromide. Observe products at each electrode. Safety: work in fume cupboard — bromine is toxic." · Not an AQA required practical on any route. Chemistry RP4 is temperature changes in reacting solutions. The only electrolysis RP is **aqueous**: Combined RP9 (8464 5.4.3.4) = Chemistry RP3 (8462 4.4.3.4), taught in `electrolysis-aqueous`. Molten lead bromide is a teacher demonstration in a fume cupboard. · RP9/RP3: "investigate what happens when aqueous solutions are electrolysed using inert electrodes." 5.4.3.2 skills column: "A safer alternative for practical work is anhydrous zinc chloride." · 8464 5.4.3.2, 5.4.3.4; 8462 4.4.3.2, §8.2.3–8.2.4 · Frozen text stays. Required practical: **none**. Present PbBr₂ as a demonstration (its observations and fume-cupboard safety are correct) with no RP badge, and mention zinc chloride as the safer alternative. Remove the RP flag BATCH-PLAN gives this row.

**EM-F2** · ROUTE · th1 half equations "Na⁺ + e⁻ → Na", "2Cl⁻ → Cl₂ + 2e⁻", "Pb²⁺ + 2e⁻ → Pb", "2Br⁻ → Br₂ + 2e⁻"; equations "Cathode: Na⁺ + e⁻ → Na", "Anode: 2Cl⁻ → Cl₂ + 2e⁻"; common_mistake "This is reduction — metal ions GAIN electrons … This is oxidation — non-metal ions LOSE electrons."; key_note "metal ion + electrons → metal … non-metal ions lose electrons" · Served on all four routes. All correct, but HT only. · "(HT only) Throughout Section 4.4.3 Higher Tier students should be able to write half equations for the reactions occurring at the electrodes …" · 8464 5.4.3.1 (HT para), 5.4.3.5 (HT only) · HT layer on CH TH. CF TF: compound → which product at which electrode, and the word equations / overall symbol equations (2NaCl → 2Na + Cl₂; PbBr₂ → Pb + Br₂). Keep the overall equations on all routes.

**EM-F3** · ROUTE · `higher` (served CH TH): "Explain product prediction from ion identity." and "Justify why reactive metals above carbon cannot be extracted by carbon reduction — electrolysis of molten compound is the only option." · Both are base, so CF TF lose them. The second belongs to `electrolysis-extraction`. Only the half-equation sentence is HT. · "Students should be able to predict the products of the electrolysis of binary ionic compounds in the molten state." "Electrolysis is used if the metal is too reactive to be extracted by reduction with carbon or if the metal reacts with carbon." · 8464 5.4.3.2, 5.4.3.3 · Teach prediction on all four routes; link to `electrolysis-extraction` for the carbon reason.

**EM-F4** · IMPRECISE · q2 wx3: "Lead bromide is ionic in BOTH solid and molten states — Na⁺ and Cl⁻ (or Pb²⁺ and Br⁻) ions exist in the solid too. They just can't move." · Names sodium chloride's ions first in a lead bromide item (copied from the NaCl item). Not false, but a pupil may read it as lead bromide containing Na⁺. · — · 8464 5.4.3.1 · q2 usable verbatim on all four routes. Design's own text names only Pb²⁺ and Br⁻.

**EM-F5** · IMPRECISE (minor) · q1 wx3: "Electrolysis is done in an enclosed container — calcium doesn't react with air at this stage. The product is pure calcium metal." · The "enclosed container" claim is not a general fact. The real reason is that electrolysis discharges the electrolyte's own ions: Ca²⁺ at the cathode. · — · 8464 5.4.3.2 · q1 usable verbatim on all four routes. The key's word "reduced" is HT framing; the answer (calcium) is base.
