# Batch 16 — science flags

Numbered per lesson. **WRONG** items are frozen text kept verbatim in the source files that must not be used as written. Each flag says what to do instead.

## 1. Mass Number, Atomic Number and Isotopes (`mass-number-isotopes`)

# Flags — mass-number-isotopes (batch 16)

1. **MASS-NUMBER-ISOTOPES-F1** · IMPRECISE · theory 1: "NUCLEAR NOTATION:\n₍Z₎A X" · The notation glyph is garbled (Z appears before A, on the same line). · Mass number A top-left, atomic number Z bottom-left of the symbol: ᴬ_Z X, e.g. ²³₁₁Na (the spec's own example). · 8464 6.4.1.2 / 8463 4.4.1.2 · Draw the notation properly (figlib `isotope_notation()` to teach, `nuclide()` in questions); never reproduce the theory string.
2. **MASS-NUMBER-ISOTOPES-F2** · IMPRECISE · theory 3: "POSITIVE ION (CATION): loses electrons" · The spec says **outer** electrons. · "Atoms turn into positive ions if they lose one or more outer electron(s)." · 8464 6.4.1.2 · Use the spec wording.
3. **MASS-NUMBER-ISOTOPES-F3** · OFF-SPEC · theory 3 negative ions, "CATION"/"ANION"; theory 2 "Physical properties differ slightly" · True, but chemistry content (ionic bonding; isotope properties), not in either physics spec. · Physics needs only positive ions and isotope notation. · 8464 5.2.1.2 (chemistry) · Keep to one line or leave out; never test negative ions or cation/anion on this page.

## 2. Nuclear Equations (`nuclear-equations`)

# Flags — nuclear-equations (batch 16)

1. **NUCLEAR-EQUATIONS-F1** · OFF-SPEC · theory 3 "EXAM STRATEGY: … Use the periodic table to identify the daughter element from its new atomic number."; FIFA I step "Z=86 is radon (Rn)" (verbatim, keep) · The spec says naming the daughter element is not required. · "This is limited to balancing the atomic numbers and mass numbers. The identification of daughter elements from such decays is not required." · 8464 6.4.2.2 / 8463 4.4.2.2 · Keep the FIFA verbatim but present the symbol as given; never ask a pupil to name or look up a daughter element. q1 is fine (options differ in A and Z).
2. **NUCLEAR-EQUATIONS-F2** · GAP · the only worked example is α decay · Rule 3: β balancing (Z goes UP, the −1 on ⁰₋₁e) is a different step and must be modelled before pupils do one. · β: A unchanged, Z + 1; ¹⁴₆C → ¹⁴₇N + ⁰₋₁e (the spec's example). · 8464 6.4.2.2 · Add a β worked example from theory 2's C-14 equation. CFIFA's unit-conversion example cannot apply here (A and Z have no units).

## 3. Half-Lives and Radioactive Decay (`half-lives`)

# Flags — half-lives (batch 16)

1. **HALF-LIVES-F1** · ROUTE · equation "After n half-lives: fraction remaining = (½)ⁿ"; theory 2 "After n half-lives: (½)ⁿ remains"; FIFA F steps "remaining = initial × (½)ⁿ", "960 × (½)⁴ = 960 × 1/16" · Expressing the decline as a ratio/fraction is the spec's only HT statement here. · Base: determine half-life from data or a graph, and find what is left by halving step by step (960 → 480 → 240 → 120 → 60). HT: "calculate the net decline, expressed as a ratio, … after a given number of half-lives". · 8464 6.4.2.3 (HT only) / 8463 4.4.2.3 (HT only) · Teach halving on every route; tag (½)ⁿ and the ratio as Higher. The FIFA stays verbatim; on Foundation its Step 2 is shown as halving.
2. **HALF-LIVES-F2** · ROUTE · theory 3 (tracers, cancer treatment, nuclear waste; background radiation), `higher` ("Compare the suitability of different isotopes…"), key_note and common_mistake background clauses · This is physics-only content, not HT; the `higher` field holds no HT point except the ratio. · 8463 4.4.3.2 "explain why the hazards associated with radioactive material differ according to the half-life involved" (physics only); 4.4.3.1 background (physics only); 4.4.3.3 medical uses (physics only). · 8463 4.4.3.1–4.4.3.3 · Tag these as Triple (TF and TH), not Higher; keep background subtraction for the triple layer (it is taught in full on `background-radiation`).
3. **HALF-LIVES-F3** · IMPRECISE · theory 2 "Iodine-131: half-life ~8 days (medical uses — short enough to leave the body)" · Half-life governs how fast the activity falls, not how fast the substance leaves the body. · "short, so its activity soon falls to a low level". · 8463 4.4.3.2 · Re-cut the line.
4. **HALF-LIVES-F4** · GAP · FIFA chains two steps in one F step ("Number of half-lives = total time ÷ half-life; remaining = initial × (½)ⁿ") · Rule 3: a chained calculation needs its own Step 1 / Step 2 worked example; "determine the half-life from given information" (the reverse chain: count halvings, then T½ = t ÷ n) is never worked at all. · Step 1 n = t ÷ T½; Step 2 halve n times (HT: × (½)ⁿ). Reverse: Step 1 count halvings 800 → 100 = 3; Step 2 T½ = 6 h ÷ 3 = 2 h. · 8464 6.4.2.3 · Design writes both as Step 1 / Step 2 worked examples before any pupil attempt. CFIFA's conversion example: use mixed units (e.g. T½ = 15 min, t = 1 h → 60 min).
5. **HALF-LIVES-F5** · IMPRECISE · q1 wx3 "Radioactive sources never fully reach zero — activity halves each half-life but never reaches exactly zero (exponential decay)." · A real sample has a finite number of nuclei and eventually all decay; "never zero" is the smooth-curve idealisation. · "Only 3 half-lives have passed, so ⅛ of the activity (80 Bq) remains." · 8464 6.4.2.3 · q1 is usable; prefer this wording for wx3.
6. **HALF-LIVES-F6** · FOR MIDE · spec phrase "net decline, expressed as a ratio" · Whether AQA credits the fraction remaining (e.g. 1/8, 1 : 8) or the fraction decayed (7/8) as "net decline". · Best reading: teach both — fraction left = (½)ⁿ, fraction decayed = 1 − (½)ⁿ — and word every question to name which it wants. · 8464 6.4.2.3 (HT only) · Design writes HT items that say "what fraction remains" or "what fraction has decayed", never bare "net decline", until Mide rules.
7. **HALF-LIVES-F7** · IMPRECISE · CFIFA Convert "…so the hours cancel before any seconds conversion would be needed." · Implies seconds might be needed; they never are — n = t ÷ T½ only needs both times in the same unit. · Corrected Convert line written into the source (`[NEW — examiner-corrected]`). · CFIFA amendment · Use the corrected line.

## 4. Radioactive Contamination (`radioactive-contamination`)

# Flags — radioactive-contamination (batch 16)

1. **RADIOACTIVE-CONTAMINATION-F1** · GAP · whole source · Two spec sentences are missing: "The irradiated object does not become radioactive" (the most-examined point in this section) and the peer-review statement. · Both quoted in the source under "Spec core missing from the frozen data". · 8464 6.4.2.4 / 8463 4.4.2.4 · Teach both; add a practice item on "is the irradiated object now radioactive?".
2. **RADIOACTIVE-CONTAMINATION-F2** · IMPRECISE · theory 1 "Example: standing near a radioactive source; medical X-ray; radiotherapy"; matching "Medical X-ray — brief external exposure"; q2 (radiographer, X-rays) · The spec defines irradiation as exposure to **nuclear** radiation; an X-ray comes from a machine, not a radioactive source. · Use a γ source (standing near one; γ-sterilised syringes; radiotherapy). · 8464 6.4.2.4; X-rays are 6.6.2.4 · Replace X-ray examples in teaching. q2 is scientifically right and usable as an irradiation item; add a nuclear-source item alongside it.
3. **RADIOACTIVE-CONTAMINATION-F3** · OFF-SPEC · theory 3 "DISTANCE — intensity follows inverse square law; doubling distance reduces dose by ¾." · Not on the GCSE spec; true only for γ from a point source; α and β are limited by their range in air. (Batch 5 flagged the same line in `radioactive-decay`.) · "Further from the source → lower dose; α and β have a short range in air." · 8464 6.4.2.1 · Do not teach the inverse-square law.

## 5. Background Radiation (`background-radiation`)

# Flags — background-radiation (batch 16)

1. **BACKGROUND-RADIATION-F1** · WRONG · q1 stem "Background count rate is 20 counts/min. With a source present, the detector reads 320 counts/min. What is the corrected activity of the source?" (and wx1 "overestimate the source activity") · A detector reading is a **count rate**, not the source's activity; the spec defines the two separately and a detector catches only a fraction of the decays. · "What is the corrected count rate due to the source?" — key 300 counts/min stands. · 8463 4.4.2.1 · **Do not use as written.** Usable with "corrected activity" → "corrected count rate" in the stem and wx1.
2. **BACKGROUND-RADIATION-F2** · ROUTE · `higher` "Calculate corrected count rates by subtracting background. Evaluate the significance … Discuss the health implications of radon…" (TF copy null) · 4.4.3.1 carries no HT label, so none of this is Higher. · All of it is physics-only base: TF and TH. · 8463 4.4.3.1 · Teach on both Triple routes.
3. **BACKGROUND-RADIATION-F3** · GAP · theory 1 artificial sources; theory 3 dose · Missing from the spec: "nuclear accidents" as a man-made source, and "1000 millisieverts (mSv) = 1 sievert (Sv)". Also "Students will not need to recall the unit of radiation dose." · Add both statements. · 8463 4.4.3.1 · Teach both; give "sievert" in any question rather than asking for it.
4. **BACKGROUND-RADIATION-F4** · IMPRECISE · q2 key "…giving the true activity of the source alone"; q2 wx2 "Geiger counters don't need resetting to zero" · "Activity" should be "count rate"; counters ARE reset to zero before each count — the point is that measuring background is not calibration. · Key: "…the count rate due to the source alone"; wx2: "Measuring background is not calibrating the counter — it gives a value to subtract." · 8463 4.4.2.1 · q2 usable; prefer the corrected wording.

## 6. Uses of Nuclear Radiation (`uses-of-nuclear-radiation`)

# Flags — uses-of-nuclear-radiation (batch 16)

1. **USES-OF-NUCLEAR-RADIATION-F1** · ROUTE · `higher` "Evaluate the choice of radiation type … Calculate the activity remaining after a given time using half-life. Explain why specific half-lives are chosen…" (TF copy null) · No HT statement exists in 4.4.3.2–4.4.3.3; evaluating choices is physics-only base. "Activity remaining" belongs to `half-lives` (base by halving; the ratio is HT there). · Evaluating type and half-life choices is TF and TH. · 8463 4.4.3.2, 4.4.3.3 · Teach on both Triple routes; leave the calculation to `half-lives`.
2. **USES-OF-NUCLEAR-RADIATION-F2** · GAP · whole source · Spec bullet "evaluate the perceived risks of using nuclear radiations in relation to given data and consequences" has no content or item. · e.g. dose from a scan vs annual background, benefit of diagnosis vs small added cancer risk. · 8463 4.4.3.3 · Add a data-based risk-evaluation task.
3. **USES-OF-NUCLEAR-RADIATION-F3** · GAP · theory 1 "control or destruction of unwanted tissue" given only as external γ beams · Internal treatment is the other standard context: I-131 taken up by the thyroid, or an implanted source. · 8463 4.4.3.3 · Add internal treatment and why its radiation type and half-life suit it.
4. **USES-OF-NUCLEAR-RADIATION-F4** · IMPRECISE · theory 2 "absorbed by the sheet but not by surrounding air"; theory 2 pipeline "Gamma source moved through underground pipe … Crack or fault → more gamma escapes"; theory 3 "can pass through a few mm of material. Absorbed by aluminium"; key_note/matching "absorbed proportional to thickness" · β is partly absorbed by the sheet and over ~1 m of air; leaks are found with a γ-emitting tracer in the fluid that collects in the soil, not by a source in the pipe; β is stopped by a few mm of aluminium; absorption increases with thickness, it is not proportional. · As stated. · 8463 4.4.2.1 · Re-cut these lines.
5. **USES-OF-NUCLEAR-RADIATION-F5** · ROUTE · theory 2 industrial uses (thickness gauges, smoke detectors, pipelines), q1 · Industrial uses are base applications of 6.4.2.1 and already taught in batch 5's `radioactive-decay`; this page's own spec is medical. · 8463 4.4.3.3 names medicine only. · 8464 6.4.2.1; 8463 4.4.3.3 · Lead with medical uses; industrial uses as quick review only. q1 usable.

## 7. Nuclear Fission (`nuclear-fission`)

# Flags — nuclear-fission (8463 4.4.4.1)

1. **NUCLEAR-FISSION-F1** · IMPRECISE · theory 1: "FISSILABLE MATERIALS:" · Not a word. · The term is **fissile** (uranium-235, plutonium-239). · — · Use "fissile" in the re-cut theory.

2. **NUCLEAR-FISSION-F2** · GAP · theory 1: "Produces TWO SMALLER NUCLEI (fission fragments) + 2–3 NEUTRONS + ENERGY." · Four spec statements are missing: fragments are "roughly equal in size"; the nucleus emits "two or three neutrons plus gamma rays"; "All of the fission products have kinetic energy"; "Spontaneous fission is rare." Also no diagram, though the spec requires pupils to "draw/interpret diagrams representing nuclear fission and how a chain reaction may occur". · Quoted in the source's new "Spec core missing" section. · 8463 4.4.4.1 · Teach all four; draw the fission event and the chain reaction.

3. **NUCLEAR-FISSION-F3** · OFF-SPEC · theory 1 "The 'missing mass' is converted to energy: E = mc²"; "~200 MeV"; theory 2 "CRITICAL MASS"; `equations` "E = mc²  (mass-energy equivalence)"; quiz q2 (key: "'mass defect' is converted to energy via E = mc²") · Correct physics, but beyond 8463 4.4.4.1, which says only "Energy is released by the fission reaction". E = mc² is on no AQA GCSE sheet or recall list; critical mass and MeV are not in 8463. · Spec: energy is released; all fission products have kinetic energy. (Mass → energy is stated only for fusion, 4.4.4.2.) · 8463 4.4.4.1 · Do not show E = mc² as a lesson equation; cut or reduce critical mass to context; use q2 only as a stretch item, not a spec rung.

4. **NUCLEAR-FISSION-F4** · ROUTE · `higher`: "Explain the chain reaction quantitatively … Explain critical mass. Describe the difference between controlled (reactor) and uncontrolled (weapon) chain reactions …" (TF copy: null) · 4.4.4 has no "(HT only)" label anywhere. Controlled vs uncontrolled chain reaction is spec core for **both** TF and TH, yet the TF copy drops it; critical mass and the "quantitative" chain reaction are off-spec on any route. · Whole page is "(physics only)", no HT layer. · 8463 4.4.4 · Teach controlled/uncontrolled to TF and TH alike; no HT layer on this page.

## 8. Nuclear Fusion (`nuclear-fusion`)

# Flags — nuclear-fusion (8463 4.4.4.2)

1. **NUCLEAR-FUSION-F1** · WRONG · theory 2: "TEMPERATURE: ~100 million °C (ten times hotter than the Sun's core for practical fusion reactors)." · The Sun's core is about 15 million °C, so 100 million °C is about six to seven times hotter, not ten. · ~100 million °C ≈ 6–7 × the Sun's core temperature. · — (off-spec context) · Theory is re-cuttable: correct the ratio or cut it.

2. **NUCLEAR-FUSION-F2** · WRONG · quiz q2, wrong option "Fusion produces more energy per reaction than fission — so fewer reactions are needed" with wx2 "Individual fusion reactions do release large amounts of energy, but individual fission reactions also release large amounts — the comparison isn't straightforward per reaction." · The per-reaction comparison is straightforward and the option is simply false; the wx dodges it. The key is also imprecise ("fuel from seawater": only deuterium; tritium is bred from lithium), and the whole item is beyond 4.4.4.2. · One fission ≈ 200 MeV; one D-T fusion ≈ 17.6 MeV — fission releases more per reaction. Per kilogram of fuel, fusion releases more. · — · **Do not use q2 as written.**

3. **NUCLEAR-FUSION-F3** · OFF-SPEC · theory 2–3 (Coulomb barrier, plasma, confinement, JET/ITER/NIF, advantages and challenges, "JET … record fusion energy output 2022", "ITER costs ~€20 billion", "2040s–2050s"); quiz q1 · 8463 4.4.4.2 is two sentences: "Nuclear fusion is the joining of two light nuclei to form a heavier nucleus. In this process some of the mass may be converted into the energy of radiation." Everything else is beyond it, and the dated figures are already stale (JET's final record was 69 MJ in Oct 2023; ITER's cost estimate is well above €20 bn). · — · 8463 4.4.4.2 · Cut dated figures. Keep at most one line on why fusion is hard. Use q1 only as a stretch item, not a spec rung.

4. **NUCLEAR-FUSION-F4** · ROUTE · `higher`: "Explain why extremely high temperatures are needed … Describe the specific plasma confinement methods … Evaluate the advantages of fusion over fission …" · Labelled as HT, but 4.4.4 has no HT label, and this content is not in the spec on any route. · No HT layer on this page. · 8463 4.4.4 · Do not build an HT layer from this field.

5. **NUCLEAR-FUSION-F5** · IMPRECISE · theory 1: "Four protons → helium-4 nucleus (two protons + two neutrons) + energy." · The net reaction also emits two positrons and two neutrinos; as written, charge is not conserved (4+ → 2+). · "Hydrogen nuclei fuse, in several steps, to form helium." · 8463 4.8.1.2 · Use the step-free wording.

## 9. Scalar and Vector Quantities (`scalar-vector-quantities`)

# Flags — scalar-vector-quantities (8464 6.5.1.1; 8463 4.5.1.1)

1. **SCALAR-VECTOR-QUANTITIES-F1** · ROUTE · theory 3 "Two forces at RIGHT ANGLES: use Pythagoras … Scale drawings can also be used …"; key_note "right angles = Pythagoras"; `equations` "Resultant² = F₁² + F₂²  (for perpendicular vectors)"; common_mistake "A car travelling in a circle at constant SPEED has changing VELOCITY" · All are HT-only spec content, but the page has no `higher` field and ships them on all four routes, including Foundation. · Resultant of two non-parallel forces: "(HT only) … determine the resultant of two forces, to include both magnitude and direction (scale drawings only)" (8464 6.5.1.4 / 8463 4.5.1.4). Circular motion: "(HT only) … motion in a circle involves constant speed but changing velocity" (8464 6.5.4.1.3 / 8463 4.5.6.1.3). · as quoted · Put both in an HT layer (CH, TH). Foundation keeps only forces in a line.

2. **SCALAR-VECTOR-QUANTITIES-F2** · IMPRECISE · theory 3: "3 N up + 4 N right → resultant = √(9 + 16) = 5 N (at an angle)." and `equations` "Resultant² = F₁² + F₂²" · Arithmetic correct, but (a) the spec method is a scale drawing, with Pythagoras only a check AQA normally also credits; (b) a vector answer needs a direction, and "at an angle" gives none (here 53° from the vertical / 37° above the horizontal). The equation is not a spec equation and is on neither June 2026 sheet. · Resultant 5 N at 37° above the 4 N force, found by scale drawing. · 8464 6.5.1.4 (HT only) · HT layer: teach scale drawing first; if Pythagoras is shown, show it as a check, give the direction, and give it no "On the sheet"/"Learn it" chip.

## 10. Contact and Non-Contact Forces (`contact-noncontact-forces`)

# Flags — contact-noncontact-forces (8464 6.5.1.2; 8463 4.5.1.2)

1. **CONTACT-NONCONTACT-FORCES-F1** · IMPRECISE · theory 3: "Example: charged balloon sticks to a wall (different charges attract)." · The wall is uncharged; the balloon induces an opposite charge on the wall's surface. As written it tells pupils the wall carries a different charge. Static charge itself is physics only. · Two charged objects attract (unlike charges) or repel (like charges) without touching. · 8463 4.2.5.1 · Use the two-charged-objects example for base; drop the wall.

2. **CONTACT-NONCONTACT-FORCES-F2** · IMPRECISE · theory 3 "All three non-contact forces can attract or repel (except gravity — gravity is always attractive)."; common_mistake "normal force is a REACTION from the surface" · The first sentence contradicts itself. The second, beside theory 1's Newton's-third-law sentence, invites the commonest error: calling weight and normal contact force a third-law pair. They act on the same object. · "Electrostatic and magnetic forces can attract or repel. Gravity only attracts." The third-law partner of the book's weight is the book's pull on the Earth. · 8464 6.5.1.2; 6.5.4.2.3 · Use the corrected sentences; confront the N3 trap explicitly.

3. **CONTACT-NONCONTACT-FORCES-F3** · ROUTE (minor) · theory 2 "UPTHRUST — upward force from a fluid on a submerged object"; key_note; quiz q2 option 4 "Upthrust on a submarine …" · The term upthrust is defined only in 8463 4.5.5.1.2 "(HT only)" (physics only). Classifying it as contact is correct. · — · 8463 4.5.5.1.2 · Fine on all routes as a self-explaining example; q2 stays usable on all four routes.

4. **CONTACT-NONCONTACT-FORCES-F4** · IMPRECISE · theory 2 "COMPRESSION — a pushing force through a solid. A compressed spring."; theory 3 "Three fundamental non-contact forces at GCSE" · Compression is not one of AQA's named forces (the force is the spring's push); "fundamental" is wrong (electrostatic and magnetic are one interaction). · "AQA names three non-contact forces: gravitational, electrostatic, magnetic." · 8464 6.5.1.2 · Cut "compression" and "fundamental".

## 11. Gravity (`gravity`)

# Flags — gravity (8464 6.5.1.3; 8463 4.5.1.3)

1. **GRAVITY-F1** · IMPRECISE · theory 2 "In deep space (no gravity): W = 0 N" and "Mass: measured with a balance (compares gravitational force on both sides — same anywhere)." · Gravity never falls to exactly zero. And only a two-pan balance compares; a school top-pan balance measures a force and is calibrated for Earth's g, so it would read low on the Moon. · "Far from any planet or star, g is almost zero, so weight is almost zero." "A two-pan balance compares masses, so it reads the same anywhere." · 8464 6.5.1.3 · Use the corrected lines, or cut both.

2. **GRAVITY-F2** · GAP · (absent) · Two base spec lines are missing from the frozen data: the centre of mass, and W ∝ m with the ∝ symbol. · "The weight of an object may be considered to act at a single point referred to as the object's 'centre of mass'." "The weight of an object and the mass of an object are directly proportional." (MS 3a: recognise and use ∝.) Quoted in the source's new "Spec core missing" section. · 8464 6.5.1.3; 8463 4.5.1.3 · Teach both; draw the weight arrow from the centre of mass; add one practice item on each.

3. **GRAVITY-F3** · IMPRECISE (minor) · quiz q1 option 3 "50 kg — mass on the Moon is 1/6 of Earth mass" · The distractor's own reasoning does not give its number: 1/6 of 80 kg is 13.3 kg. wx2 ("Mass NEVER changes …") is correct and aligned. · — · — · q1 remains usable as written on all routes.

## 12. Resultant Forces (`resultant-forces`)

# Flags — resultant-forces

**RESULTANT-FORCES-F1** · OFF-SPEC · th1: "FORCES AT RIGHT ANGLES: use Pythagoras; direction from trigonometry or scale drawing."
- Wrong: AQA asks for the resultant of two forces at an angle only at Higher, and only by "scale drawings only". Pythagoras and trigonometry are not GCSE requirements here, and the line sits in base theory.
- Correct science: base = "calculate the resultant of two forces that act in a straight line". HT = vector diagram (scale drawing) for two forces at an angle, magnitude and direction.
- Spec: 8464 6.5.1.4 / 8463 4.5.1.4.
- Design: base teaches straight-line resultants only. Any angled resultant goes in the HT layer (CH TH) as a scale drawing; no Pythagoras or trig.

**RESULTANT-FORCES-F2** · ROUTE · th2 "Free Body Diagrams" (whole chunk), th3 "SCALE DRAWING METHOD", th3 "Resultant force perpendicular to motion → object CHANGES DIRECTION".
- Wrong: shown to every route as base. FBDs and scale drawings are "(HT only)" in 6.5.1.4; the perpendicular/circle idea is "(HT only)" in 6.5.4.1.3.
- Correct science: content is right; layer is higher.
- Spec: 8464 6.5.1.4 (HT only); 8464 6.5.4.1.3 (HT only); 8463 4.5.1.4, 4.5.6.1.3.
- Design: put these in the HT layer (CH TH), or leave the detail to the `free-body-diagrams` and `resolving-forces` pages and link. Simple force-arrow pictures (book, car, skydiver) used only to show balanced vs unbalanced are fine on base.

**RESULTANT-FORCES-F3** · IMPRECISE · `higher`: "centripetal force is always directed towards the centre."
- Wrong: AQA does not name or require centripetal force. The spec line is qualitative: constant speed, changing velocity.
- Correct science: "(HT only) …explain qualitatively, with examples, that motion in a circle involves constant speed but changing velocity."
- Spec: 8464 6.5.4.1.3 / 8463 4.5.6.1.3.
- Design: drop "centripetal"; keep the changing-velocity idea at most as a one-line link to `motion-in-a-circle`.

## 13. Resolving Forces and Vector Diagrams (`resolving-forces`)

# Flags — resolving-forces

**RESOLVING-FORCES-F1** · OFF-SPEC · th1 "Horizontal component: Fx = F cos θ / Vertical component: Fy = F sin θ" (+ the 50 N at 37° example), th2 "METHOD 3 — COMPONENT METHOD", `equations` (all three), `common_mistake`, key_note "Fx = F cosθ, Fy = F sinθ… R = √(Fx²+Fy²)", `higher` "using trigonometry".
- Wrong: AQA requires resolution and resultants by vector diagram, "(scale drawings only)". No trigonometric or Pythagoras equation is on the spec or on either June 2026 sheet. The physics is correct; it is beyond the course.
- Correct science: "(HT only) A single force can be resolved into two components acting at right angles to each other. The two component forces together have the same effect as the single force." "(HT only) …use vector diagrams to illustrate resolution of forces, equilibrium situations and determine the resultant of two forces, to include both magnitude and direction (scale drawings only)."
- Spec: 8464 6.5.1.4 (HT only) / 8463 4.5.1.4 (HT only).
- Design: teach resolution by drawing — the force to scale at its angle, then drop the horizontal and vertical sides and measure them. No sin/cos, no √, no arctan, no formula triangle. The 50 N at 37° numbers work as a drawing (≈ 40 N and 30 N measured).

**RESOLVING-FORCES-F2** · OFF-SPEC · the frozen FIFA: "R = √(3² + 4²) = √(9+16) = √25 = 5 N; θ = arctan(4/3) = 53° north of east".
- Wrong: method is Pythagoras + arctan. Answer (5 N at 53° north of east) is correct.
- Correct science: scale drawing. 1 cm = 1 N; 3 cm east, then 4 cm north from its tip; resultant from start to finish measures 5.0 cm → 5 N; protractor ≈ 53° north of east.
- Spec: 8464 6.5.1.4 (HT only).
- Design: do not use the four FIFA steps as the taught method. Use the same question as the first scale-drawing worked example (corrected Convert line in source: the scale). Second worked example: a scale that is not 1:1 (e.g. 1 cm = 10 N) so the convert-back step is real.

**RESOLVING-FORCES-F3** · WRONG · th3: "Scale drawings introduce measurement errors — component method is more precise. For GCSE, scale drawings are acceptable for force problems."
- Wrong: for AQA GCSE scale drawing is the required method, not an accepted fallback; the line tells pupils the taught method is second-best.
- Correct science: "(scale drawings only)". Reduce error with a large scale, sharp pencil, careful protractor.
- Spec: 8464 6.5.1.4 (HT only).
- Design: do not use; replace with the accuracy advice.

**RESOLVING-FORCES-F4** · OFF-SPEC · q1: "A 13 N force acts at 67.4° to the horizontal. What are the horizontal and vertical components? (sin67.4° = 0.923, cos67.4° = 0.385)".
- Wrong: needs trigonometry. Key, distractors and wrong_explanations are internally correct and aligned.
- Correct science: as F1.
- Spec: 8464 6.5.1.4 (HT only).
- Design: **do not use as written** on any route. A scale-drawing replacement (draw 13 N at 67.4° on squared paper, read 5 N and 12 N) is a Design top-up item.

**RESOLVING-FORCES-F5** · IMPRECISE · th1: "Essential for inclined plane problems, projectile problems, force equilibrium."
- Wrong: projectiles are not in AQA GCSE physics.
- Correct science: equilibrium situations (6.5.1.4).
- Spec: 8464 6.5.1.4.
- Design: drop "projectile problems".

**RESOLVING-FORCES-F6** · ROUTE · header "Appears on routes: Triple Higher".
- Wrong: 8464 6.5.1.4 carries the same (HT only) text as 8463 4.5.1.4.
- Correct: true routes CH TH. Approved; moving under the route-flag PR.
- Design: author for CH TH.

## 14. Free Body Diagrams (`free-body-diagrams`)

# Flags — free-body-diagrams

**FREE-BODY-DIAGRAMS-F1** · OFF-SPEC · th3 "Resolving Forces from Free Body Diagrams" (whole chunk: "Fx = F cos θ… Component of weight along slope: W sin θ… Normal contact force = W cos θ"), th2 "use scale drawing or trigonometry", `equations` (both), key_note "Resolve angled forces: Fx = F cosθ, Fy = F sinθ", `higher` "Resolve forces into perpendicular components… or components".
- Wrong: AQA asks for FBDs "qualitatively" and for resolution by "scale drawings only". Trigonometric components and slope resolution are A-level.
- Correct science: "(HT only) …use free body diagrams to describe qualitatively examples where several forces lead to a resultant force on an object, including balanced forces when the resultant force is zero."
- Spec: 8464 6.5.1.4 (HT only) / 8463 4.5.1.4 (HT only).
- Design: no trig, no formula triangles. A slope FBD is fine qualitatively (weight straight down, normal force perpendicular to the slope, friction up the slope). Resolution belongs on `resolving-forces`, by scale drawing.

**FREE-BODY-DIAGRAMS-F2** · WRONG · q1 option 4: "3.33 N — Fy = F ÷ θ = 10 ÷ 30 = 0.33 N".
- Wrong: the option's value (3.33 N) contradicts its own working (10 ÷ 30 = 0.33). Also the whole item (vertical component of 10 N at 30° by sin) is off-spec (F1).
- Correct science: n/a — item is off-spec.
- Spec: 8464 6.5.1.4.
- Design: **do not use q1 as written** on any route.

**FREE-BODY-DIAGRAMS-F3** · IMPRECISE · q2 wx1: "At terminal velocity, acceleration = 0 which means forces are BALANCED — but this means the skydiver continues at the same speed, not that they've stopped."
- Wrong: option 1 says "still accelerating", not "stopped"; the second clause answers an error the option does not make.
- Correct science: key and other explanations correct (6.5.4.1.5).
- Design: q2 usable; if the explanation is re-cut, end it after "BALANCED, so the speed stays the same".

**FREE-BODY-DIAGRAMS-F4** · ROUTE · header "Appears on routes: Triple Higher"; th1 "UPTHRUST: upward, in a fluid".
- Wrong: 8464 6.5.1.4 carries the same (HT only) FBD text, so Combined Higher has it. Upthrust as a topic is 8463 4.5.5.1.2 (physics only)(HT only).
- Correct: true routes CH TH (approved; moving under the route-flag PR). Upthrust may appear in a list of force names on CH, but any explanation of it is a TH layer.
- Design: author for CH TH; keep upthrust to a name on an arrow.

## 15. Work Done and Energy Transfer (`work-done-energy-transfer`)

# Flags — work-done-energy-transfer

**WORK-DONE-ENERGY-TRANSFER-F1** · OFF-SPEC · th2 "P = W ÷ t = F × s ÷ t = F × v / Power also equals force × speed"; key_note "P = Fv (force × speed for constant motion)".
- Wrong: P = Fv is not in 8464 or 8463 and is on neither June 2026 sheet. The algebra is right.
- Correct science: P = W/t is the spec's link (8464 6.1.1.4).
- Spec: 8464 6.5.2, 6.1.1.4 / 8463 4.5.2, 4.1.1.4.
- Design: keep P = W/t as a link; drop P = Fv.

**WORK-DONE-ENERGY-TRANSFER-F2** · IMPRECISE · th3 "Friction always acts OPPOSITE to motion — it always does NEGATIVE work on moving objects".
- Wrong: signed work is not GCSE and confuses "work done against friction".
- Correct science: "Work done against the frictional forces acting on an object causes a rise in the temperature of the object."
- Spec: 8464 6.5.2 / 8463 4.5.2.
- Design: use the spec sentence.

**WORK-DONE-ENERGY-TRANSFER-F3** · IMPRECISE · th2 "Pushing a box along the floor: work done against friction → kinetic energy of box + thermal energy (friction)."
- Wrong: work done against friction goes to the thermal store (temperature rise), not to the kinetic store. Pushing at steady speed adds nothing to the kinetic store.
- Correct science: as F2.
- Design: "work done against friction → thermal store; the box and floor warm up".

**WORK-DONE-ENERGY-TRANSFER-F4** · IMPRECISE · th3 "Lifting: W = F × h (where F = weight = mg…) Combined with W = mg: W = mgh".
- Wrong: W stands for work and for weight in the same line.
- Correct science: weight = mg (6.5.1.3); work done = weight × height = mgh = Ep gained (6.1.1.2).
- Design: write the two steps in words. This is a chained calculation (rule 3) — see brief.

**WORK-DONE-ENERGY-TRANSFER-F5** · GAP · spec lines not practised: "convert between newton-metres and joules"; "rise in the temperature of the object".
- Correct science: 1 J = 1 N m; friction → temperature rise.
- Spec: 8464 6.5.2 / 8463 4.5.2.
- Design: one item each in the top-up bank.

## 16. Forces and Elasticity (`forces-elasticity`)

# Flags — forces-elasticity

**FORCES-ELASTICITY-F1** · WRONG · th1 "Within the ELASTIC LIMIT, extension is DIRECTLY PROPORTIONAL to the applied force"; th2 "BEYOND THE ELASTIC LIMIT: Graph curves — no longer proportional"; key_note "Elastic limit: beyond this, Hooke's Law breaks down — graph curves"; matching row 3.
- Wrong: proportionality ends at the **limit of proportionality**, not the elastic limit. They are different points; AQA uses only "limit of proportionality" and marks the two apart.
- Correct science: "The extension of an elastic object, such as a spring, is directly proportional to the force applied, provided that the limit of proportionality is not exceeded." Beyond it the graph is non-linear. Inelastic deformation (does not return to its original length) is a separate idea.
- Spec: 8464 6.5.3 / 8463 4.5.3; 6.1.1.2 ("assuming the limit of proportionality has not been exceeded").
- Design: use "limit of proportionality" for where the straight line ends; keep "elastic vs inelastic deformation" for whether the spring returns to its length. Do not use the term "elastic limit" as the end of proportionality.

**FORCES-ELASTICITY-F2** · IMPRECISE · rp "RP18 (Physics) — Investigate force–extension relationship for a spring"; th2 "REQUIRED PRACTICAL (RP18)"; key_note "RP18".
- Wrong: RP18 is the Combined Science number. In GCSE Physics 8463 it is Required practical activity 6.
- Correct: 8464 RP18 (CF CH) / 8463 RP6 (TF TH). Same practical, same AT 1 and 2.
- Spec: 8464 6.5.3, 10.2.18; 8463 4.5.3, 8.2.6.
- Design: label by route (RP18 on Combined, RP6 on Physics). The frozen rp data is otherwise correct; add that the force is the weight of the hung masses (W = mg, g given).

**FORCES-ELASTICITY-F3** · WRONG · q2 option 4 (index 3, marked false): "The rubber band needs forces from both sides to stay in equilibrium while stretching"; wx3: "Equilibrium (resultant = 0) IS the right idea here".
- Wrong: option 4 is a correct reason (spec: more than one force for a stationary object), and its own explanation says so. Two defensible answers. Also wx1 calls the single-force → acceleration idea "Newton's First Law" (it is the Second Law); wx2 says "A single force CAN stretch an elastic material" and calls the support's pull a "Newton's Third Law" second force (a Third-Law pair acts on a different object).
- Correct science: "to change the shape of an object (by stretching, bending or compressing), more than one force has to be applied – this is limited to stationary objects only." One unbalanced force accelerates the object (Newton's Second Law).
- Spec: 8464 6.5.3 / 8463 4.5.3; 8464 6.5.4.2.2.
- Design: **do not use q2 as written.** A replacement item on the same idea is a top-up item.

**FORCES-ELASTICITY-F4** · GAP · `equations` lists only "F = k × e"; variables omit Ee; compression and linear/non-linear not stated.
- Wrong: Ee = ½ke² is taught in th3 and is base (Mide's ruling), on both June 2026 sheets, but is not in the equations list. The spec's "also applies to the compression…" and "linear and non-linear relationship" lines are absent.
- Correct science: see the "Spec core missing" section added to the source.
- Spec: 8464 6.5.3 / 8463 4.5.3.
- Design: equation block carries F = ke and Ee = ½ke², both "On the sheet"; teach e as extension or compression.

**FORCES-ELASTICITY-F5** · IMPRECISE · th3 "Two equal and opposite forces are needed to stretch, compress or bend an object."
- Wrong: the spec says "more than one force". Bending a ruler held at both ends and pressed in the middle uses three.
- Design: "more than one force"; two equal and opposite is the stretching/squashing case.
