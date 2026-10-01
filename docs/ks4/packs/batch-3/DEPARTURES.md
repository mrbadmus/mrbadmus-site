# DEPARTURES — KS4 Batch 3 (13 Code-authored lessons)

Batch 3 has no Design original: Code wrote every lesson from the AQA spec, the
examination files and the review rounds, so there is no Design-vs-built diff
to register. A "departure" here is instead any of three things: (1) a frozen
quiz item (verbatim source data) withheld from the page because the
examination found it wrong, ambiguous or wrong for its route; (2) a frozen
source field — an `rp` practical number, a key-note line, a theory
paragraph — that is not shown on the page because it is wrong, imprecise or
out of its spec; (3) a change the two review rounds (science examiner +
quality reviewer, both fresh Opus readers, 1 Oct 2026; a second commit pass,
`2ddea6225`, re-checked every REQUIRED row) required to what was first
authored, plus the handful of advisories the commander or the author applied
anyway because they touched what a pupil is told. The frozen Python data
itself (`ks4_lessons/batch_3.py`, `shared/ks4-source-batch-3.js`) is never
edited for any of this — withholding happens at the serving layer
(`K.bank`/`K.find` plus `batch_3.py`'s `withhold` list), and every
pupil-facing fix is a change to the lesson's own authored template or logic,
not to the frozen record.

Sources: `ks4_lessons/batch_3.py` (withhold entries B3-W1…B3-W9, with needles
and routes); `docs/ks4/packs/batch-3/review/science-phys-a.md`,
`science-phys-b.md`, `science-chem-bio.md`, `quality-a.md` and `quality-b.md`
(REQUIRED rows and applied advisories, both review rounds — round-2 sections
re-check the round-1 fixes rather than opening new ones, and the quality
reviews have not had a second round appended as of this write-up);
`docs/ks4/packs/batch-3/notes/<slug>.md` ("Review fixes" tables, and the
frozen items each lesson's author lists as not shown); and
`docs/ks4/packs/batch-3/examination/<slug>.md`.

---

## 1. Withheld frozen quiz items — 9 rows

Every row is a `withhold` entry in `ks4_lessons/batch_3.py` (dep ids
B3-W1…B3-W9). The item stays verbatim in the practice bank's source data on
every route it would otherwise serve; `K.bank`/`K.find` never return it as a
rung, in the body, or on the named routes at all.

| id | lesson | routes | the question | why | citation |
|---|---|---|---|---|---|
| B3-W1 | temperature-changes-shc | all | "A 2 kg iron block (c = 450 J/kg°C) cools from 200°C to 50°C…" | option 4's label states false arithmetic (ΔE = m × c, not c × Δθ, = 900 J) and wx3 misdiagnoses the error as a missing mass | 6.3.2.2 |
| B3-W2 | sound-waves-hearing | TH | "…used for foetal scanning rather than X-rays" (q2) | wx2 says X-rays penetrate soft tissue *less* well than bone — reversed (X-rays pass through soft tissue more easily, which is why bone shows up); the item is also 4.6.1.5 content taught on a 4.6.1.4 page | 6.6.2.2; 8463 4.6.1.5 |
| B3-W3 | microscopy | all | "What is the maximum magnification of a light microscope?" (q1) | wx2 states a false equipment fact — "×200 is a common low-power objective" — when real school objectives are ×4/×10/×40, and total magnification (eyepiece × objective) is itself examined RP1 content | RP1 |
| B3-W4 | microscopy | all | "An image is 45 mm wide. The actual size is 0.009 mm" (q2) | wx3 says "45 minus 0.009 is not how you calculate magnification!" for the ×4500 distractor, but 45 − 0.009 ≠ 4500; the distractor actually comes from rounding 0.009 to 0.01, which the feedback never names | 4.1.1.5 |
| B3-W5 | conservation-of-mass | all | "24 g of magnesium reacts completely with oxygen…" (q2) | the distractor "64 g — double the mass of magnesium" is arithmetically false (double of 24 g is 48 g, not 64 g), and its wx is mismatched — it answers the 40 g error, not the 64 g one | 5.3.1.1 |
| B3-W6 | atom-economy | TF, TH | "Why do addition reactions always have an atom economy of 100%?" (q2) | option 4 is correct in substance under AQA's own formula (desired Mr ÷ Σ reactant Mr = 1 for a single-product addition reaction), and the item's own wx3 concedes the statement is true — two defensible answers | 8462 4.3.3.2 |
| B3-W7 | types-of-em-waves | all | "Which EM wave has the highest frequency?" (q1) | wx3 teaches the microwave-resonance myth — that ovens are tuned to water's resonant frequency; they run at 2.45 GHz, nowhere near any resonance of water | 6.6.2.1; 6.6.2.4 |
| B3-W8 | particle-motion-pressure | all | "A gas is at 27°C and 100 kPa. It is heated to 327°C at constant volume…" (q2) | requires the kelvin scale and p ∝ T; neither is examinable in AQA physics 8463 or 8464 at any tier (whole-text search found no "kelvin" and no "absolute zero" in 8463) | — (not in either spec) |
| B3-W9 | atom-economy | TF, TH | "A reaction produces 80 g of desired product and 20 g of waste product…" (q1) | atom economy is defined from the balanced equation, not from collected masses the stem conflates the two; option 4's feedback ("calculated incorrectly") names no misconception | 4.3.3.2 |

---

## 2. Frozen source text not shown on the page — 36 rows

Wrong theory claims, a wrong `rp` number, key-note lines replaced or dropped,
and content tagged to the wrong route, that are deliberately not displayed
(ordinary not-in-spec scope cuts — SEM/TEM description, toluidine blue,
Miller–Urey, "green chemistry", cement production, banded iron, isotopes,
the ozone/UV story — are not listed here; this table is content that could
mislead if it had been shown, or that was shown on the wrong route, not
ordinary scoping).

| lesson | field | what | why |
|---|---|---|---|
| temperature-changes-shc | theory 3 | "Cast iron pans (low SHC): heat up quickly — responsive. Ceramic: heat up more slowly but retain heat longer." | IMPRECISE, NOT-IN-SPEC; a cast-iron pan's behaviour is dominated by its large mass, not SHC alone |
| temperature-changes-shc | theory 3 | "Higher SHC = … heats up and cools down more slowly" | IMPRECISE; only true for the same mass and the same rate of energy transfer — every comparison on the page keeps both explicit instead |
| sound-waves-hearing | theory 1; common_mistake | "Sound travels faster in denser media (unlike EM waves…)" | WRONG; density is not the reason (lead ≈1200 m/s is slower than aluminium ≈6400 m/s); re-cut as "closer together and more strongly linked" |
| sound-waves-hearing | equations | "d = v × t / 2" | not an AQA equation; AQA's is s = v t, with the halving as a method step |
| sound-waves-hearing | key_note | ultrasound/SONAR lines ("Ultrasound uses: medical…", "d = vt/2…") | 4.6.1.5 content on a 4.6.1.4 page; only the human-range and speed-ordering lines are kept verbatim |
| microscopy | key_note | "Resolution = sharpness. Magnification = size increase." | IMPRECISE; a mark scheme does not credit "sharpness" — replaced with the distinguish-two-points definition |
| microscopy | th1 | "Staining kills cells — so stained specimens cannot be living." | IMPRECISE; some stains are used on living cells; not used |
| conservation-of-mass | th3 | "OR: 2 moles H₂ + 1 mole O₂ → 2 moles H₂O" | WRONG ROUTE as written — HT content (5.3.2.2) shown as base; tagged Higher instead and withheld from CF/TF |
| conservation-of-mass | `higher` field | atom economy formula; "addition reactions have 100% atom economy" | WRONG ROUTE and WRONG LESSON; chemistry-only content served to Combined Higher; cut entirely, not shown on any route |
| atom-economy | `equations[0]` | atom economy = (Mr desired ÷ Σ Mr all **products**) × 100 | numerically valid (mass is conserved) but not AQA's printed form; the page shows AQA's reactants-denominator form instead |
| atom-economy | common_mistake | "…uses the relative formula masses of the PRODUCTS … not the reactants." | WRONG; directly contradicts AQA's formula, whose denominator *is* the reactants; never shown |
| atom-economy | key_note | line 1 (products-denominator form) | IMPRECISE; replaced with an authored AQA-form line |
| atom-economy | th2 | "EXAMPLE 1 — high atom economy" (45.9%) / "EXAMPLE 3 — low" (56%) | WRONG; the labels contradict each other (45.9% is the lowest value, not the highest); labels not reproduced |
| waves-detection-exploration | theory 1 | "P-waves are refracted … → core is DENSER than mantle" | IMPRECISE; refraction shows a boundary and gives the core's size, not density on its own; not displayed |
| waves-detection-exploration | theory 1 | shadow-zone definitions ("regions … that receive neither P nor S") | IMPRECISE; conflates the separate P-wave and S-wave shadow zones; the bench draws the two zones separately instead |
| waves-detection-exploration | equations | "d = v × t / 2" | not an AQA equation; the card shows s = v t, with halving as a method step |
| mixtures | `rp` | "RP1 — Investigate paper chromatography…" | WRONG number (it is 8464 RP12 / 8462 RP6) and wrong lesson (owned by `chromatography`); no RP block shown |
| mixtures | key_note | "Chromatography: dissolved substances — Rf = …" | Rf belongs to `chromatography`; shown as "Chromatography: dissolved substances." with no Rf line |
| mixtures | th2 | "Heat solution to saturate it, then allow to COOL SLOWLY" | IMPRECISE; heating evaporates water, it does not saturate the solution; re-cut as "evaporate some of the water" |
| mixtures | th3 | "lower boiling point substances rise higher and condense at the top … collected at different heights" | true of the industrial crude-oil column, false of the lab method, where fractions are collected one after another from one outlet as the thermometer reading rises; not used for the lab method |
| early-atmosphere | key_note (whole field) | O₂ from "cyanobacteria"; omits fossil fuels | the organism word is wrong for AQA ("algae") and a whole spec statement (fossil-fuel formation) is missing; replaced by six authored lines |
| early-atmosphere | th2 | "cyanobacteria (blue-green bacteria) evolved — the first photosynthetic organisms" | IMPRECISE; AQA's word is "algae", and anoxygenic photosynthetic bacteria predate cyanobacteria; re-cut |
| early-atmosphere | th3 | "As Earth cooled below 100°C, water vapour CONDENSED…" | IMPRECISE; 100°C is today's sea-level boiling point, not a spec figure; re-cut to spec wording |
| early-atmosphere | `higher` field | evidence-evaluation half | WRONG ROUTE; base spec content (5.9.1.2 "evaluate different theories") withheld from Foundation; taught as base on all four routes instead |
| specific-latent-heat | theory 3 | "This is why ponds freeze from the surface DOWN…" | IMPRECISE, NOT-IN-SPEC; the causal chain is muddled (density of water near 4°C, not latent heat, is the real reason); not displayed |
| specific-latent-heat | theory 1 | Lv > Lf "because fully separating particles" | NOT-IN-SPEC; not displayed |
| greenhouse-gases | key_note (whole field) | lists N₂O among the three named gases; no carbon-footprint definition | the spec names three gases, not four, and the footprint definition is a whole missing spec statement; replaced by six authored lines |
| greenhouse-gases | th3 | footprint definition: "total amount of greenhouse gases (measured as CO₂ equivalent)…" | IMPRECISE; drops the mark-bearing phrase "over the full life cycle of a product, service or event"; re-cut to the spec's own wording |
| greenhouse-gases | `higher` field | peer review/evidence evaluation; why actions are limited | WRONG ROUTE; both are base spec statements (5.9.2.2, 5.9.2.4) withheld from Foundation; taught as base on all four routes instead |
| types-of-em-waves | theory 2 | "RADIO WAVES: λ = 0.1 m to 10⁴ m; f = 30 MHz to 3 kHz"; "MICROWAVES: λ = 1 mm to 0.1 m; f = 300 MHz to 300 GHz" | WRONG; both bands are self-contradictory under c = fλ, and not in the spec; numbers dropped |
| types-of-em-waves | theory 1; common_mistake | "Energy INCREASES (∝ frequency)"; "more energy per photon" | NOT-IN-SPEC, IMPRECISE; photon energy is beyond GCSE; not taught |
| types-of-em-waves | theory 3 | "All are produced by changes in energy levels of electrons OR by oscillating charges." | IMPRECISE; contradicts the page's own gamma-from-nucleus line; not shown |
| types-of-em-waves | equations | "c = f × λ" | AQA's symbol is v, not c; rendered as v = f λ |
| particle-motion-pressure | theory 1–3; common_mistake; `variables` | kelvin scale, absolute zero, p ÷ T = constant | NOT-IN-SPEC at any tier (no "kelvin" anywhere in 8463); none of it is shown — the bench and ladder use only the qualitative p–T relation |
| particle-motion-pressure | `higher` field | "pV = constant … Absolute zero (0 K) …" | WRONG TAG; pV is Foundation-tier Triple content, not Higher, and is never shown on Combined; not rendered as a Higher block |
| particle-motion-pressure | `equations` field | "p ÷ T = constant"; "T(K) = T(°C) + 273" | NOT-IN-SPEC; only "pV = constant" is rendered, Triple only |

---

## 3. Changed after review, by lesson

Required rows from both review rounds (`S-n` = science examiner, `Q-n`/`A-n`
= quality reviewer, round 1; `S-A n` = science advisory, round 1), plus a
second commit pass (`2ddea6225`) that re-checked every REQUIRED row and
found none still open, and applied advisories that changed science or
pupil-facing wording. Pure layout/cosmetic advisories are omitted. "Old →
new" is short; full text is in the review files and the lesson's notes file.

### temperature-changes-shc
| id | where | old → new | reason |
|---|---|---|---|
| Q-SHC1 (REQUIRED) | `offVerdictText` | now ends "Record the highest temperature." | the number it names was repeated a line below, in "Process your data" |
| S-A1 | CFIFA H Question 2 | added "Assume all the energy heats the block." to the head | makes the (otherwise unstated) assumption explicit |
| S-A2 | RP step 5 | "Record the energy supplied (the joulemeter reading, or E = V × I × t) and the highest temperature…" | names the joulemeter alternative explicitly |
| A-SHC1 | before the ladder | added a Key fact card: ΔE = m c Δθ, Δθ = final − initial, the SHC definition | — |
| A-SHC2 | explainer | removed "Aluminium's is 900 J/kg °C." | the ranking lead already gives it where it is used |
| A-SHC3 | the sim | the unlagged run no longer hides the lagged result | the off-question verdict, the processing panel, the comparison and the unlagged line now stay visible together |
| A-SHC4 | the ranking instrument | the placed 1st–4th slots stay visible and locked after the reveal | "Take back" now shows only before heating |
| A-SHC5 | the graph | "lagged"/"no lagging" labels moved mid-graph | clear of the 11–12 min crosses |

### sound-waves-hearing
| id | where | old → new | reason |
|---|---|---|---|
| A-4 | key note | "Speed: solid > liquid > gas." → "Speed: **usually** solid > liquid > gas." | matches the explainer's corrected "usually" (examination C5) |
| A-6 | key fact | "…only works from 20 Hz to 20 kHz." → "…**In a human ear**, the conversion only works from about 20 Hz to 20 kHz." | — |
| A-SW1 | hook reveal | cut "Below, you find out how the ear does it, and where its range ends." | a signpost that told the pupil nothing they needed |
| A-SW2 | tone buttons | added `aria-label="<tone>: heard"` / `"<tone>: not heard"` | accessibility |

### microscopy
| id | where | old → new | reason |
|---|---|---|---|
| science A-3 | `#s-think` "×3.3" reply | → "That divides the wrong way, real ÷ image, and still mixes µm with mm. Magnification is image ÷ real." | names the actual error |
| quality Q-1 | `hookOptions[0].reply` | → "More magnification alone gives a bigger blur, not more detail. Resolve it, below, tests this." | — |
| quality Q-2 | `#s-rp` | Variables paragraph deleted; step 2 and Risks shortened | trimmed to examined content only |
| quality Q-3 | drawing title / `drawAlt` | → "Onion epidermis cells, seen at ×400" | — |
| quality A-1 | convert-first CFIFA example | chloroplast 5 µm / 25 mm / ×5000 → 4 µm / 30 mm / ×7500 | the old numbers mirrored `eukaryotes-prokaryotes`'s example |
| quality A-2 | key-note line | "Magnification = size increase." → "Magnification = how many times bigger the image is than the real object." | — |
| quality A-3 | unit-ladder card | split onto two lines (mm → µm / µm → nm) | no longer wraps mid-arrow |

### conservation-of-mass
| id | where | old → new | reason |
|---|---|---|---|
| S-2 (commander ruling: science numbers over quality's) | `rungs.r2` (CH, TH) | 0.40 kg CH₄ / 1.10 kg CO₂ / 0.90 kg H₂O, answer **1600 g**, tol 5 → 0.16 kg / 0.44 kg / 0.36 kg, answer **640 g**, tol 2 | the engine's calc-rung parser reads "1,600" as 1; the new set stays stoichiometric (160 + 640 = 440 + 360). Quality's own fix (Q-1) proposed 0.040/0.11/0.09 kg, answer 160 g — the commander chose the science reviewer's 640 g set instead; see §4 |
| Q-2a | Foundation CFIFA Question 2 | 0.50 kg CaCO₃ → 280 g CaO (220 g) → 0.84 kg MgCO₃ → 400 g MgO (**440 g**) | duplicated `relative-formula-mass`'s live rung 2 |
| Q-2b | worked example 1 | 10.0 g → 5.6 g CaO (4.4 g) → 25.0 g → 14.0 g CaO (**11.0 g**) | shared 5.6 g CaO with `percentage-yield`'s live worked example; the answer also repeated F Q1/H Q1's 4.4 g |

### atom-economy
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | `rungs.r3` | marks 2 → **3** | a three-link chain |
| Q-2 | `row()` unit dividers | full-height line → short ticks at the top and bottom of the bar | the dividers were cutting through the centred labels |
| Q-3 | CFIFA worked example 2 | Iron (Fe₂O₃ + 3CO, 45.9%, repeating the strip) → **Copper: 2CuO + C → 2Cu + CO₂**, 127 ÷ 171 × 100 = **74.3%** | the strip's Iron tab printed the same working |
| A-7 | ethanol CFIFA tab | unchanged — the frozen Formula step stays verbatim, with a reconciling AQA-reactants note underneath | accepted under the frozen-text policy |

S-3 (withholding frozen q1 as well as q2, so the practice-bank section is
hidden rather than shown empty) was **applied by the author ahead of
review** and is recorded under "Considered, not changed" (§4), because it is
a standing engine behaviour, not a lesson-specific text fix.

### waves-detection-exploration
| id | where | old → new | reason |
|---|---|---|---|
| A-7 | hook | "…which part of it is solid and which is liquid." → "…that part of it is liquid." | matches 4.6.1.5 (the core's outer part is liquid; nothing in spec asks which part is solid) |
| A-8 | bench figure | the P-wave path to 150° now enters the core at 44° (was 47°) | so the two core-crossing paths no longer cross |
| A-WD1 | bench step 4 | earlier S paths dimmed, their ✕ marks removed; station badges dimmed to 35% | the moved shadow edge and the 78° tick now stand out |
| A-WD2 | hook reveal | cut "Below, you read them yourself." | signpost |

### mixtures
| id | where | old → new | reason |
|---|---|---|---|
| science S-1 (REQUIRED) | `ROUNDS` sand round, Simple-distillation reply | → "Distilling off all the water would leave the sand behind, but it takes a long time and a lot of energy. A filter catches insoluble sand in seconds." | names the real reason filtration wins |
| science A-4 | key-note line | "Fractional distillation: liquids with different boiling points." → "…liquids **whose boiling points are close together**." | — |
| quality Q-1 | desk order | blue ink → water, sand, copper sulfate, **muddy pond water (new round)**, ethanol / same ink → dyes; six rounds | answers were in button order, and the last round could be solved by elimination |
| quality A-1 | second explainer | cut to new content only: bead column; fractions collected one after another | — |
| quality A-2 | last round's reveal | cut the `chromatography`-lesson signpost | — |

A-5 (withholding q2, the Rf item, from the bank) was **declined** by the
commander and is recorded under §4.

### early-atmosphere
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | first explainer | cut to its first sentence, "AQA examines one theory…" | — |
| Q-2 | rung 2 part (b) | replaced with a graph-reading part on how O₂ changed after 2.7 billion years; command chip Suggest → Describe; command-words block's Suggest card → Give | matches the new rung's command word |
| A-9 (science) | hook heading | "Venus and Mars still have the kind of air Earth started with" → "Venus and Mars **may** still have…" | spec wording ("one theory suggests…") |
| A-1 | rung 3 oceans herring | given its own feedback, no longer repeating clock stage 6; Explain command card made generic | — |
| A-2 | equation block | eyebrow → "Equation"; chip → "Learn it · no chemistry equation sheet" | — |

### specific-latent-heat
| id | where | old → new | reason |
|---|---|---|---|
| S-1 / Q-SLH2 (REQUIRED) | H "Convert first" Answer note | → "Converting only L gives 45.2 ÷ 2 260 000 = 0.00002 kg (0.02 g): a thousand times too small." | the old note mislabelled the error |
| Q-SLH3 (REQUIRED) | F "Convert first" | Lf = 334 000 J/kg so only the mass converts; Answer note "Left in grams, 250 × 334 000 = 83 500 000 J: a thousand times too big." | — |
| Q-SLH1 (REQUIRED) | ledger plate title/legend | title anchored to the right edge; legend stacked (condensing row, cooling row) | nothing clips or overlaps at 390 px |
| Q-SLH4 (REQUIRED) | explainer 2; logger step 1 | "Run it backwards on a cooling graph…" deleted; eyebrow → "Energy from a flat section"; logger step 1 replaced with "Which section of the graph does E = m L describe?" | the freezing-point = melting-point misconception is no longer confronted on this page (covered by `internal-energy`) |
| Q-SLH5 (REQUIRED) | `curve()` | tick labels 24 px, every 20 °C / 2 min; left margin widened | the rotated axis title no longer overlaps the numbers |
| A-SLH1 | the confrontation text | "…bonds between them form…" → "…are held by the forces between them…" | matches batch-2 `internal-energy`'s "forces between particles" wording |
| A-SLH2 | r2-H prompt | dropped "in kilograms" | the unit is now the pupil's own choice |
| A-SLH3 | hook reveal | cut "The ledger below counts both." | — |
| A-SLH5 | before the ladder | added a Key fact card: E = m L at constant temperature, ΔE = m c Δθ when temperature changes | — |

### greenhouse-gases
| id | where | old → new | reason |
|---|---|---|---|
| Q-1 | hook options | all four now carry corrective replies; reveal's last sentence deleted | — |
| Q-2 | effects explainer | the full list → "Its effects reach the sea, the weather, food and wildlife." | the full list is still in `effReveal` and the key note (round-2 advisory A-12 offered restoring one short list; not required) |
| Q-3 | `REP[2]` | replaced with "Report B was peer reviewed. What does that tell you?" (four options, shuffled) | — |
| Q-4 | tabs heading | "Compare the three runs." once all three regimes are run | — |
| A-10 (science) | explainer and both sort `why` lines | "mainly methane" used consistently | — |
| A-1 | eyebrow | → "Radiation bench" | — |
| A-3 | Report B's Data row | added "plus carbon dioxide records" | supports the correlation-versus-cause item |

### types-of-em-waves
| id | where | old → new | reason |
|---|---|---|---|
| science A-1 | explainer | "wavelength (the length of one complete wave)" → "wavelength (the distance from a point on one wave to the same point on the next wave)" | the spec's own definition (8463 4.6.1.2 / 8464 6.6.1.2), the wording mark schemes credit |
| science A-2 | CH/TH `cfQuestions` hi Question 2 close | "…gives 330 000 m: an aerial bigger than a city." → "…gives 330 000 m: a wavelength of 330 km for a phone signal." | — |
| quality A-EM1 | `p1Reveal` | cut "From radio waves to gamma rays, each group's wavelength is shorter than the last." | the figure's heading already says it |

Not changed: science A-3 (frozen q2 wx3, photon energy — no action asked, kept as harmless feedback); quality A-EM2 and A-EM3 (both marked acceptable by the reviewer).

### particle-motion-pressure
| id | where | old → new | reason |
|---|---|---|---|
| S-2 / Q-PMP2 (REQUIRED) | TH rung 2 | rewritten to 0.0090 m³ at 100 kPa squeezed to 2500 cm³ (convert cm³ → m³); answer **360 kPa**, tol 1 | every numeric ladder answer now < 1000, clearing the parser limit (see §4) |
| Q-PMP1 (REQUIRED) | hook options | every wrong option now carries a corrective reply; the shared reveal reworded so it repeats no reply | — |
| S-A9 | Triple explainer | → "the same **average speed**" | — |
| S-A10 | TH Question 1 | → "the volume the gas would occupy at 100 kPa" | — |
| A-PMP1 | bench, TH stage 3 | the fast-push verdict and bars now hide once the push starts | — |
| A-PMP2 | bench, the "bump into each other" confrontation | the empty verdict line is no longer drawn | — |

### power
| id | where | old → new | reason |
|---|---|---|---|
| S-3 / Q-PW2 (REQUIRED) | Higher rung 2 | rewritten to 1.2 kW for 150 s; answer **180 kJ**, tol 1 | every numeric ladder answer now < 1000, clearing the parser limit (see §4) |
| Q-PW1 (REQUIRED) | hook options | every wrong option now carries a corrective reply; the shared reveal reworded | — |
| S-A11 | equation block | added an Ep = m g h card, chip "On the sheet" | the source FIFA and Higher Question 1 both use it |

---

## 3a. Shared-block engine fixes (Mide's approval, 2 Oct 2026)

Every page of this batch (13 lessons, all routes) changes because two shared blocks compiled into every KS4 page were fixed — see `ks4_rulings.py` R16/R17 and `docs/ks4/design-reference/pilot/DEPARTURES-PILOT.md` ("Shared blocks — ladder number parse and sort completion"). Science content, lesson logic and freeze hashes are unchanged.

- **R16 (Ks4Ladder Apply rung):** a typed number with space or comma thousands separators ("63 000", "63,000") is now read as 63000, not 63; a single decimal comma ("6,3") still reads 6.3.
- **R17 (Ks4Sort):** the block now reports completion when the sort is checked, so the lesson's rail stop ticks. Lessons in this batch that use Ks4Sort: sound-waves-hearing, atom-economy, waves-detection-exploration, early-atmosphere, greenhouse-gases, particle-motion-pressure, power.

---

## 4. Considered, not changed

**The June 2026 equation-sheet labelling rule, applied across the batch.**
Every physics equation this batch teaches — ΔE = m c Δθ, E = P t, E = m L,
P = E/t, P = W/t, Ep = m g h, and pV = constant — is chipped **"On the
sheet"** rather than "Learn it", under the batch-2 ruling: the June 2026
equation sheets (both 8463 and 8464/8465, headed "FOR USE IN JUNE 2026
ONLY") print every one of them, even where the spec itself lists an equation
as **recall** (E = P t, P = E/t, P = W/t are all spec recall-list items; Ep =
m g h is recall; pV = constant carries no HT mark and sits on the 8463 sheet
list only). This follows the same precedent as the pilot's `resistors-C9`
(V = I R, also a recall equation, chipped "On the sheet" because the 2026
sheet prints it) and batch 2's `changes-in-energy` ruling on Ek and Ep.
`KS4.EQ_YEAR` is the switch for when AQA stops publishing the full sheet; the
`power` examination's own verdict flagged that the spec and the 2026 sheet
disagree for every equation in that lesson, and the batch stayed consistent
with the pilot's rule rather than the spec's recall/sheet split.

**Sound q1 (the SONAR item) kept in `sound-waves-hearing`'s bank, overruled
advisory A-5.** The science reviewer (round 1, confirmed round 2) recommended
withholding it on this slug, since it tests 4.6.1.5 content ("divide the
echo time by 2 in SONAR calculations") that this 4.6.1.4 page does not
teach, even though the item is scientifically correct. The reviewer named it
the commander's call rather than a science defect. The commander declined:
the item stays in the frozen bank, unused as a rung either way — it is not
served to the pupil on this page regardless, so withholding it would change
nothing a pupil sees, only the bank's own listing.

**Mixtures' Rf question (q2) kept in the bank, overruled advisory A-5.** The
science reviewer flagged withholding it, since Rf and chromatography's
mechanism belong to the (not-yet-written) `chromatography` lesson rather
than to `mixtures`. The commander ruled to keep it in the bank — not a rung,
and not previewed on the page — rather than mint a new withhold row, closing
the question for this run.

**Conservation-of-mass Higher rung 2 uses the science reviewer's numbers
(640 g), not the quality reviewer's (160 g).** Both reviewers caught the
same defect independently — the keyed answer, 1600 g, trips the engine's
calc-rung parser, which reads "1,600" or "1 600" as 1 — and each proposed a
different stoichiometric fix under 1000: quality's Q-1 scaled the reaction
down to 0.040 kg methane / 110 g CO₂ / 90 g H₂O, answer 160 g; science's S-2
scaled it to 0.16 kg / 0.44 kg / 0.36 kg, answer 640 g. The commander ruled
for the science reviewer's set (640 g), recorded in §3 above; quality's 160 g
set was not shipped.

**Atom-economy's practice section hidden rather than shown empty, because
both frozen items are withheld.** With q1 (B3-W9) and q2 (B3-W6) both
withheld on TF and TH, the lesson's practice bank is empty on every route it
ships on. The author's fix (quality review row S-3) changed the bank's
render guard from `sc-if value="{{ ready }}"` to `sc-if value="{{ bankOn }}"`
(`bankOn = ready && bank.length > 0`), so the section — including its
heading — is not rendered at all, and no rung or body text refers to it.
This is a standing engine behaviour applied ahead of formal review rather
than a lesson-specific text fix, which is why it sits here rather than in
§3's atom-economy table.

**The ladder's number-parser limit — answers rewritten below 1000, not
fixed at the source.** `Ks4Ladder`'s calc-rung grader parses a typed answer
with `parseFloat(s.replace(',', '.'))`, so "1,600" reads as 1 and "1 600"
reads as 1600 only if there is no comma at all — either way, a pupil who
writes a correct answer in normal exam form (with a thousands separator) is
marked wrong. This is a shared pilot-block defect, inherited from the
engine, and is **not fixed in this batch**. The batch's workaround, applied
wherever the examination's own typical numbers would have produced an answer
≥ 1000, is to choose different, still-stoichiometric numbers that keep every
calc-rung answer under 1000: `conservation-of-mass` CH/TH rung 2 (640 g, not
1600 g — see above), `particle-motion-pressure` TH rung 2 (360 kPa, not a
four-figure value), and `power` Higher rung 2 (180 kJ, not a four-figure
value). `temperature-changes-shc`'s r2 answers (770 J; 18.7 °C) were chosen
below 1000 for the same reason from first authoring, noted in that lesson's
own "Engine note" rather than as a review fix.

---

Row counts: §1 (withheld quiz items) **9**; §2 (frozen source text not
shown) **36**; §3 (changed after review) **13 lessons**, 68 rows in all
(S-/Q-/A- ids, both review rounds, both science and quality reviewers);
§4 (considered, not changed) **6** items.

> Quality round 2 (both groups): SHIP ×13, no new required rows. One commander edit after round 2: specific-latent-heat prompt "does E = m L describe" set with non-breaking spaces (quality A2-SLH1).
