# Examination — Nanoparticles (nanoparticles) — AQA 8462 4.2.4.1–4.2.4.2 (chemistry only)
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF (Version 1.1, 04 Oct 2019), downloaded from filestore.aqa.org.uk and converted to text: 4.2.4.1, 4.2.4.2 and 4.1.1.4 (atom size) quoted from that PDF. AQA-8464-SP-2016.PDF was also fetched; it has no 4.2.4 equivalent, which confirms the lesson is chemistry only.

Design file: `ks4-chemistry-5.2.3.3-nanoparticles.dc.html` (called "the page" below). Source: `src/chemistry-5.2.3.3-nanoparticles.md` and `ks4-source.js["nanoparticles"]`. Repo: `all_subtopics_chemistry_triple_foundation.py` and `all_subtopics_chemistry_triple_higher.py`, `CHEMISTRY_SUBTOPICS_ALL["bonding"]`, id `nanoparticles`. There is no CF or CH dict, which is correct.

Spec statements relied on (verbatim, 8462 v1.1):
- 4.2.4.1: "Nanoscience refers to structures that are 1–100 nm in size, of the order of a few hundred atoms. Nanoparticles, are smaller than fine particles (PM2.5), which have diameters between 100 and 2500 nm (1 x 10-7 m and 2.5 x 10-6 m). Coarse particles (PM10) have diameters between 1 x 10-5 m and 2.5 x 10-6 m. Coarse particles are often referred to as dust. As the side of cube decreases by a factor of 10 the surface area to volume ratio increases by a factor of 10. Nanoparticles may have properties different from those for the same materials in bulk because of their high surface area to volume ratio. It may also mean that smaller quantities are needed to be effective than for materials with normal particle sizes." Also: "Students should be able to compare 'nano' dimensions to typical dimensions of atoms and molecules." No (HT only) marker anywhere in 4.2.4.
- 4.2.4.2: "Nanoparticles have many applications in medicine, in electronics, in cosmetics and sun creams, as deodorants, and as catalysts … Students should consider advantages and disadvantages … given appropriate information, evaluate the use of nanoparticles for a specified purpose; explain that there are possible risks associated with the use of nanoparticles."
- 4.1.1.4: "Atoms are very small, having a radius of about 0.1 nm (1 x 10-10 m)."
- 4.2.4 heading: "Bulk and surface properties of matter including nanoparticles (chemistry only)".

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | header eyebrow | "AQA Chemistry 4.2.4 (chemistry only) · Quantitative" | 8462 4.2.4 heading | OK | Correct section, and it carries the chemistry-only label. Flag 2 is resolved by this. |
| 2 | `<title>` / h1 | "Nanoparticles" | 4.2.4 | OK | |
| 3 | `.ks3-bigq` | "Gold is yellow and unreactive. Grind it into particles a few nanometres across and it turns red and becomes a catalyst. Same atoms." | 4.2.4.1 (bulk vs nano properties) | OK | Gold nanoparticles of about 2–50 nm are red and catalytically active, which is real and well documented. "Grind" is loose, because nanogold is made chemically, not by grinding, but a rhetorical question does not assert a method. No change. |
| 4 | route badges | "Triple" + "Foundation · Higher" | 4.2.4 (chemistry only, no HT) | OK | Flag 3 is confirmed. |
| 5 | `notTriple` status line | "This whole lesson is separate-science content. Combined routes do not include it" | 4.2.4 heading | OK | Under contract §0 this is served only on TF and TH, so the line never renders in production. |
| 6 | hook `h2` + paragraph | medieval ruby glass made with a trace of gold; "particles around 25 nm across"; ring and glass have "the same kind of atom" | 4.2.4.1 | OK | Colloidal gold in ruby glass is roughly 5–60 nm, so 25 nm is representative. |
| 7 | `hookOptions[0]` | "A far bigger share of its atoms are at the surface" → "Test it with the cube splitter below." | 4.2.4.1 (high SA:V) | OK | This is the credited idea. The reply is unscored, as designed. |
| 8 | `hookOptions[1]` reply | "The particles are still gold: no new substance forms." | 4.2.4.1 "same materials" | OK | |
| 9 | `hookOptions[2]` reply | "A gold atom is the same size in a ring or in glass." | 4.2.4.1 / 4.1.1.4 | OK | |
| 10 | `hookOptions[3]` reply | "Heat cannot change one element into another." | 4.1.1 (atoms of an element) | OK | Correct at GCSE: chemical and thermal processes do not transmute elements. |
| 11 | `hookReveal` | "In a 25 nm particle, a large fraction of the atoms sit on the surface" | 4.2.4.1 | IMPRECISE | For a 25 nm gold particle (atom diameter about 0.29 nm) roughly 6 × 0.29 ÷ 25 ≈ 7% of the atoms are on the surface. That is far larger than in bulk gold (about 10⁻⁵ %), but it is not "a large fraction", and a pupil will read that as "most". The comparison is the science. → C1 |
| 12 | explainer | "Nanoscience is about structures 1 to 100 nm across: 1 nm = 1 × 10⁻⁹ m, a billionth of a metre." | 4.2.4.1 | OK | |
| 13 | explainer | "A nanoparticle holds only a few hundred atoms" | 4.2.4.1 "of the order of a few hundred atoms" | IMPRECISE / CONTRADICTS | "Only" hardens the spec's "of the order of". It also contradicts the hook's 25 nm gold particle, which contains about 5 × 10⁵ atoms. Restore the spec wording. → C2 |
| 14 | explainer | "an atom is about 0.1 nm across" | 4.1.1.4 "radius of about 0.1 nm" | WRONG | The spec gives the radius, not the diameter, as 0.1 nm. An atom is about 0.2 nm across. This is the one number the 4.2.4.1 "compare nano dimensions to atoms" statement relies on, and AQA would not credit "diameter 0.1 nm" for an atom. → C2 |
| 15 | explainer | "fine particles (PM2.5), which are 100 to 2500 nm across" | 4.2.4.1 | OK | Verbatim range. |
| 16 | explainer | "coarse particles (PM10), the dust of 2.5 × 10⁻⁶ m to 1 × 10⁻⁵ m" | 4.2.4.1 | OK | Verbatim range, and "dust" is the spec's own word. |
| 17 | explainer | "Sorting a particle means getting every size into the same unit first." | MS 1b | OK | |
| 18 | Ks4Sort `prompt` | "1 µm = 1000 nm" | MS 1b | OK | |
| 19 | Ks4Sort `done-note` | "1 µm is 1000 nm, and 1 nm is 10⁻⁹ m" | MS 1b | OK | |
| 20 | `zBins` | Coarse · PM10 / Fine · PM2.5 / Nanoparticle | 4.2.4.1 | OK | The three spec classes. |
| 21 | `zItems[0]` | dust 5 µm → coarse; why "5000 nm, inside the PM10 range of 2500 to 10 000 nm" | 4.2.4.1 | OK | 2.5 × 10⁻⁶ m to 1 × 10⁻⁵ m is 2500 to 10 000 nm. Correct bin and arithmetic. |
| 22 | `zItems[1]` | diesel soot 0.5 µm → fine; "500 nm: between 100 and 2500 nm" | 4.2.4.1 | OK | Diesel soot agglomerates reach about 0.5 µm (primary particles are smaller). The stated size decides the bin. |
| 23 | `zItems[2]` | TiO₂ in sun cream 20 nm → nano | 4.2.4.1/4.2.4.2 | OK | Sun-cream TiO₂ is typically 10–50 nm. |
| 24 | `zItems[3]` | silver in wound dressing 1 × 10⁻⁸ m → nano; "= 10 nm" | 4.2.4.1 | OK | 10⁻⁸ × 10⁹ = 10 nm. |
| 25 | `zItems[4]` | smoke 1 × 10⁻⁶ m → fine; "= 1000 nm" | 4.2.4.1 | OK | Smoke is typically 0.01–1 µm, so the value is realistic and inside 100–2500 nm. |
| 26 | `zItems[5]` | sea-salt spray 8 µm → coarse; "8000 nm" | 4.2.4.1 | OK | Sea salt sits in the coarse mode, and 8000 nm is inside 2500–10 000 nm. |
| 27 | Ks4Sort as a whole | No item sits on a boundary (100 nm or 2500 nm) | 4.2.4.1 | OK | Good design: no ambiguous edge cases. |
| 28 | cube commit `.ks3-commit` | "A cube's side shrinks from 100 nm to 10 nm, ten times smaller. What happens to its surface area to volume ratio?" | 4.2.4.1 "side of cube decreases by a factor of 10 … increases by a factor of 10" | OK | |
| 29 | `cubeOpts` + `cubeRight = cubePick === 0` | "It increases 10 times" is credited | 4.2.4.1 | OK | |
| 30 | `cubeNote` | "each time the side is divided by 10, the ratio is multiplied by 10. A 10 nm particle has 100 times the ratio of a 1000 nm grain" | 4.2.4.1 | OK | 0.6 ÷ 0.006 = 100. Correct. |
| 31 | `cubeNote` extra for pick 3 | "Volume does fall 1000 times, but surface area falls only 100 times, so the ratio rises 10 times." | 4.2.4.1, MS 5c | OK | For one cube: L³ ÷ 1000, L² ÷ 100, so the ratio is ×10. Correct. |
| 32 | `SIDES` | [1000, 100, 10, 1] nm | 4.2.4.1 | OK | Each step is ÷10. |
| 33 | `tiles` 1000 nm | SA 6 × 10⁶ nm²; V "1,000 × 10⁶" nm³; ratio 0.006 nm⁻¹ | MS 5c | OK | 6 × 1000² = 6 × 10⁶ and 1000³ = 10⁹, both correct. The volume display "1,000 × 10⁶" is not normalised standard form but is numerically correct. Style, not science. |
| 34 | `tiles` 100 nm | SA 60,000 nm²; V 1 × 10⁶ nm³; ratio 0.06 nm⁻¹ | MS 5c | OK | |
| 35 | `tiles` 10 nm | SA 600; V 1,000; ratio 0.6 | MS 5c | OK | |
| 36 | `tiles` 1 nm | SA 6; V 1; ratio 6 | MS 5c | OK | Note that a 1 nm "particle" is only a handful of atoms. It is still at the edge of the spec's 1–100 nm range. |
| 37 | tile labels | "Surface area 6L²", "Volume L³", "Ratio 6 ÷ L" | MS 5c | OK | |
| 38 | `cube(idx)` drawing | a 1000 nm cube cut into k³ cubes with k = 1, 2, 4, 8, labelled "side of each small cube: 1000/100/10/1 nm" | MS 5c | IMPRECISE | Two slices per edge give 500 nm cubes, not 100 nm. The drawing is necessarily schematic, since a true 1 nm split would be 10⁹ cubes. The visible label is acceptable on its own. |
| 39 | `cube(idx)` alt text | "A cube of side 1000 nm sliced into 8 smaller cubes, each of side 100 nm, the same total volume" (and 64 × 10 nm, 512 × 1 nm) | MS 5c | WRONG | A 1000 nm cube cut into 100 nm cubes gives 1000 cubes, not 8. With 10 nm cubes it is 10⁶, not 64, and with 1 nm cubes 10⁹, not 512. A screen-reader user is told a false count. → C3 |
| 40 | `legal` (Ks4End) | "The cube splitter draws a cube of each size sliced into smaller cubes of the same total volume." | MS 5c | IMPRECISE | This should say that the slice count is schematic, so a sighted pupil counting 8 cubes for "100 nm" is not misled. → C4 |
| 41 | `legal` | "Particles are modelled as perfect cubes, the GCSE convention; real nanoparticles are irregular … follow the same pattern." | 4.2.4.1 (cube model) | OK | This is an accurate model limitation. |
| 42 | `legal` | "Coarse (PM10) and fine (PM2.5) size ranges follow AQA 4.2.4.1." | 4.2.4.1 | OK | |
| 43 | misconception quote | "Red nanogold must be a different substance from yellow gold." | 4.2.4.1 | OK | This is the source's `common_mistake`, correctly framed as the wrong idea. |
| 44 | `thinkOptions[0]` (correct) | "Only the scale. The atoms are the same gold atoms, but far more of them sit on the surface." | 4.2.4.1 | OK | "Far more" here is comparative, so it is fine. |
| 45 | `thinkOptions[1]` reply | "The bonding inside each particle is still metallic bonding between gold atoms." | 4.2.1.5 / 4.2.4.1 | OK | |
| 46 | `thinkOptions[2]` reply | "Nanoparticles are neutral gold, like the bulk metal." | 4.2.4.1 | OK | |
| 47 | `thinkOptions[3]` reply | "The glass surrounds the particles; it is not mixed into them." | 4.2.2.7 (alloy = metal mixture) | OK | |
| 48 | `thinkReveal` | "Its different colour, reactivity and melting point come from its surface area to volume ratio, not from a change of substance." | 4.2.4.1 "properties different … because of their high surface area to volume ratio" | OK | This matches AQA's causal statement. The lowered melting point of nano-gold is real. |
| 49 | equation chip | "Derived, not on any sheet" | — (GCSE Chemistry has no equation sheet) | OK | This is accurate. SA:V = 6 ÷ L is derived, not a listed equation. |
| 50 | equation card 1 | "SA : V = 6L² ÷ L³ = 6 ÷ L"; "six faces of area L², volume L³" | MS 5c | OK | 6L²/L³ = 6/L. Correct derivation. |
| 51 | equation card 2 | "L = 6 ÷ (SA : V)" | MS 5c | OK | This is the correct rearrangement. |
| 52 | equation card 3 | "L in nm gives the ratio in nm⁻¹ … Convert every length to nm" | MS 1b | OK | |
| 53 | CFIFA worked 1 head | verbatim FIFA 1 question: cube of side 10 nm | — | OK | |
| 54 | CFIFA worked 1 C | "Nothing to convert: the side is already in nm" | — | OK | |
| 55 | CFIFA worked 1 F | "for a cube, surface area to volume ratio = 6L² ÷ L³ = 6 ÷ L" | CFIFA correction | OK | This is the formula, not rearranged for the unknown. The ratio is already the subject. |
| 56 | CFIFA worked 1 I / Fine-tune / A | "= 6 ÷ 10"; "Nothing to rearrange … unit is nm⁻¹"; "0.6 nm⁻¹" | MS 5c | OK | 6 ÷ 10 = 0.6. Correct, and it follows the CFIFA rule ("Nothing to rearrange"). |
| 57 | CFIFA worked 2 C | "0.02 µm × 1000 = 20 nm"; note "1 µm = 1000 nm" | MS 1b | OK | |
| 58 | CFIFA worked 2 F/I/A | "6 ÷ L"; "= 6 ÷ 20"; "0.3 nm⁻¹" | MS 5c | OK | 6 ÷ 20 = 0.3. |
| 59 | CFIFA worked 2 A note | "Skip the conversion and you get 6 ÷ 0.02 = 300, a thousand times too big." | MS 1b | IMPRECISE | 300 is a correct ratio in µm⁻¹ (300 µm⁻¹ = 0.3 nm⁻¹). It is only "too big" as an answer in nm⁻¹. Q2's `close` line gets this exactly right ("right for metres, wrong for the unit asked"), so as written the two notes are inconsistent. → C5 |
| 60 | CFIFA Q1 head | verbatim FIFA 3: ratio 1.2 nm⁻¹, find the side | — | OK | |
| 61 | CFIFA Q1 C | "Nothing to convert: the ratio is already in nm⁻¹, so L comes out in nm." | — | OK | |
| 62 | CFIFA Q1 F / I | "surface area to volume ratio = 6 ÷ L"; "1.2 = 6 ÷ L" | CFIFA correction | OK | The formula is un-rearranged and the values are inserted into that form, as Mide's correction requires. |
| 63 | CFIFA Q1 Fine-tune / A | "L = 6 ÷ 1.2 … unit is nm"; "L = 5 nm" | MS 5c | OK | 6 ÷ 1.2 = 5. |
| 64 | CFIFA Q1 `close` | "rearranging to L = 6 ÷ ratio happens at Fine-tune" | CFIFA correction | OK | |
| 65 | CFIFA Q2 head/C | "side of 5 × 10⁻⁸ m"; "5 × 10⁻⁸ m × 10⁹ = 50 nm" | MS 1b | OK | 5 × 10¹ = 50. |
| 66 | CFIFA Q2 F/I/A | "6 ÷ 50"; "0.12 nm⁻¹" | MS 5c | OK | 6 ÷ 50 = 0.12. |
| 67 | CFIFA Q2 `close` | "Unconverted, 6 ÷ (5 × 10⁻⁸) gives 1.2 × 10⁸, in m⁻¹: right for metres, wrong for the unit asked." | MS 1b | OK | 1.2 × 10⁸ m⁻¹ = 0.12 nm⁻¹, which is consistent. |
| 68 | CFIFA Q2 structure | Q2 is a Convert case; Q1 is not | NOTES §6 | OK | The questions give no hint of which one needs converting, as designed. |
| 69 | Uses and risks eyebrow | "AQA 4.2.4.2" | 4.2.4.2 | OK | |
| 70 | Uses paragraph | "used in medicine, electronics, cosmetics and sun creams, deodorants and as catalysts" | 4.2.4.2 | OK | This is the spec's list, verbatim in substance. |
| 71 | Uses paragraph | risks "may be absorbed through skin or lungs … long-term effects on health and the environment are not yet fully known" | 4.2.4.2 "possible risks" | OK | This is the standard creditable risk in AQA mark schemes (e.g. "may be toxic / enter cells / long-term effects unknown"). |
| 72 | Uses paragraph | "An 'evaluate' question wants a benefit, a risk and a judgement." | AQA command words ("Evaluate") | OK | |
| 73 | Ks4Write `np-eval` question | "Titanium dioxide nanoparticles are used in sun creams. Evaluate their use." [4] | 4.2.4.2 | OK | |
| 74 | `evPoints[0]` | "transparent on the skin, so the cream is not white" | 4.2.4.2 | OK | Credited in AQA mark schemes ("does not leave white marks / better coverage"). |
| 75 | `evPoints[1]` | "good protection from ultraviolet (UV) light" | 4.2.4.2 | OK | |
| 76 | `evPoints[2]` | "might pass through the skin or be breathed in … long-term effects … not fully known" | 4.2.4.2 | OK | |
| 77 | `evPoints[3]` | "Judgement: a reasoned conclusion" | Evaluate | OK | |
| 78 | `evReject[0]` | rejects "They are a different chemical so they might be dangerous." | 4.2.4.1 | OK | |
| 79 | command word "Calculate" | "Show the working. Convert, formula, insert, fine-tune, answer with a unit." | AQA command words | OK | |
| 80 | command word "Compare" | "Say how many times bigger: divide one ratio by the other." | AQA command words: "Compare – describe the similarities and/or differences between things" | IMPRECISE | This narrows the command word to a single numerical move. AQA mark schemes for this topic do credit "x times larger", but the definition itself should be AQA's. → C6 |
| 81 | command word "Evaluate" | "Benefit, risk, then a judgement with a reason." | AQA command words ("use the information supplied and knowledge to consider evidence for and against … judgement") | OK | |
| 82 | key fact | "When the side of a cube decreases by a factor of 10, its surface area to volume ratio increases by a factor of 10. That is why nanoparticles behave differently from the same material in bulk." | 4.2.4.1 | OK | Near-verbatim spec. |
| 83 | examiner tip | `K.tip` → source `examiner_tip` | 4.2.4.1 | OK | "Marks are for the SA:V ratio … never 'different substance'" is consistent with AQA mark schemes. |
| 84 | ladder r1 (TH route) | `K.find(... 'State the range of sizes')` misses on TH, so it falls to "Describe what happens to a particle's SA:V ratio as the particle gets smaller" (TH3), with command "Describe" and why "Smaller particle, larger surface area to volume ratio." | 4.2.4.1 | OK | |
| 85 | ladder r1 (TF route) | `K.find` HITS TF7 ("State the range of sizes … 1 to 100 nm") but still carries command "Describe" and why "Smaller particle, larger surface area to volume ratio." | 4.2.4.1 | CONTRADICTS | On TF the rung's `why` explains a different question from the one asked, and the command word is "Describe" on a "State" item. TF3 is the same SA:V item as TH3, so a single needle serves both routes consistently. → C7 |
| 86 | ladder r2 prompt | cube side 3 × 10⁻⁹ m; ratio in nm⁻¹ [3] | 4.2.4.1, MS 1b, 5c | OK | |
| 87 | ladder r2 `convAnswer` | "Convert m to nm: multiply by 10⁹" | MS 1b | OK | 3 × 10⁻⁹ × 10⁹ = 3 nm. |
| 88 | ladder r2 `answer`/`tol`/`unit` | 2, ±0.01, nm⁻¹ | MS 5c | OK | 6 ÷ 3 = 2. The tolerance is fine, since the answer is exact. The unit list includes the distractors nm, nm², nm³. |
| 89 | ladder r2 `right`/`wrong`/`model` | "3 nm, and 6 ÷ 3 = 2 nm⁻¹"; C/F/I/F/A lines | CFIFA correction | OK | The model's Fine-tune line ("unit nm⁻¹, because L is in nm") is consistent with the ratio already being the subject. |
| 90 | ladder r2 tariff | 3 marks | AQA practice | OK | Conversion, substitution and answer with unit. This is a reasonable 3-mark split. |
| 91 | ladder r3 links | high SA:V → greater fraction of atoms on the surface to react → smaller mass of catalyst needed | 4.2.4.1 "smaller quantities are needed to be effective" | OK | The chain order is logically correct. |
| 92 | ladder r3 herring 1 | "a different, more reactive substance" / why "same substance at a smaller size" | 4.2.4.1 | OK | |
| 93 | ladder r3 herring 2 | "atoms … smaller, so they move faster" / why "atoms are the same size" | 4.2.4.1 | OK | |
| 94 | ladder r4 question | "Silver nanoparticles are added to wound dressings because they kill bacteria. Evaluate this use." [4] | 4.2.4.2 "medicine" | OK | The antibacterial action is given in the stem, so it is "given appropriate information". |
| 95 | ladder r4 `points` | benefit (high SA:V, small amount needed); benefit (kills bacteria); risk (absorbed / released to environment, effects unknown); judgement | 4.2.4.1/4.2.4.2 | OK | These are all creditable. |
| 96 | ladder r4 `reject` | "Nanosilver is a different element."; "A benefit and a risk with no judgement cannot reach full marks." | 4.2.4.1; AQA Evaluate | OK | |
| 97 | `keyLines[0]` | "Nanoparticles are 1 to 100 nm across. 1 nm = 1 × 10⁻⁹ m. They contain a few hundred atoms." | 4.2.4.1 | IMPRECISE | Same issue as row 13. This key-note line is the one pupils memorise. → C8 |
| 98 | `keyLines[1]` | "Fine particles (PM2.5): 100 to 2500 nm. Coarse particles (PM10): 2.5 × 10⁻⁶ to 1 × 10⁻⁵ m." | 4.2.4.1 | OK | |
| 99 | `keyLines[2]` | "For a cube: SA : V = 6 ÷ L. Convert lengths to nm first." | MS 5c | OK | |
| 100 | `keyLines[3]` | "Side ÷ 10 means SA : V × 10." | 4.2.4.1 | OK | |
| 101 | `keyLines[4]` | "same substance … high SA : V gives them different properties" | 4.2.4.1 | OK | |
| 102 | `keyLines[5]` | "Uses: medicine, electronics, sun creams, deodorants, catalysts. Risks: … not yet fully known." | 4.2.4.2 | OK | "Cosmetics" is dropped from the list. That is acceptable, since the key note is a summary. |
| 103 | Ks4KeyNote `spec` | "AQA 4.2.4 (chemistry only)" | 4.2.4 | OK | |
| 104 | `bank` | `K.bank(slug, R.isTriple ? R.route : 'Triple Higher')` | contract §0 | OK | TF → TF copy (10 items), TH → TH copy (11 items). |
| 105 | Ks4End `endConnects` | "Graphene and fullerenes" → giant-covalent-structures page | 4.2.3.3 | OK | The link is correct. Graphene and fullerenes are taught in L10. |
| 106 | Ks4End `tutor-line` | "Stuck converting µm and m into nanometres?" | — | OK | |

## 2. Required changes
All `old` strings were checked with `grep -cF` and occur exactly once in `ks4-chemistry-5.2.3.3-nanoparticles.dc.html`. None contains a `\u` escape, so each one matches the file as stored.

| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| nanoparticles-C1 | `ks4-chemistry-5.2.3.3-nanoparticles.dc.html` — `hookReveal`: `a large fraction of the atoms sit on the surface` | `a far larger fraction of the atoms sit on the surface` | A 25 nm gold particle has about 7% of its atoms on the surface. What matters is how much larger this is than in bulk; "a large fraction" reads as "most". | 8462 4.2.4.1 |
| nanoparticles-C2 | same file — explainer: `A nanoparticle holds only a few hundred atoms; an atom is about 0.1 nm across.` | `Nanoparticles are of the order of a few hundred atoms; an atom has a radius of about 0.1 nm.` | (a) The spec says an atom's RADIUS is about 0.1 nm, so "0.1 nm across" is a factor of 2 wrong on the very comparison 4.2.4.1 asks pupils to make. (b) "Only a few hundred" hardens the spec's "of the order of" and contradicts the page's own 25 nm hook particle (about 5 × 10⁵ atoms). | 8462 4.1.1.4; 4.2.4.1 |
| nanoparticles-C3 | same file — `cube(idx)` alt text: `'A cube of side 1000 nm sliced into ' + (k * k * k) + ' smaller cubes, each of side '` | `'A cube of side 1000 nm sliced (drawn schematically, not to scale) into smaller cubes, each of side '` | The alt text gives false counts: 8 cubes of 100 nm (it should be 1000), 64 of 10 nm (10⁶) and 512 of 1 nm (10⁹). The rest of the expression (`+ SIDES[idx] + ' nm, the same total volume'`) is unchanged. | MS 5c |
| nanoparticles-C4 | same file — Ks4End `legal`: `The cube splitter draws a cube of each size sliced into smaller cubes of the same total volume.` | `The cube splitter draws a cube of each size sliced into smaller cubes of the same total volume; the number of slices drawn is schematic, not to scale.` | The drawing shows 2, 4 and 8 slices per edge for 100, 10 and 1 nm. The model-limits line must say this is schematic. | MS 5c |
| nanoparticles-C5 | same file — CFIFA worked 2, Answer note: `0.02 = 300, a thousand times too big.` | `0.02 = 300 per micrometre, a thousand times too big for an answer per nanometre.` | 300 µm⁻¹ is a correct value, and the error is only in the unit asked for. This brings the note into line with Q2's `close` line ("right for metres, wrong for the unit asked"). | MS 1b |
| nanoparticles-C6 | same file — command-word card: `Say how many times bigger: divide one ratio by the other.` | `Describe the similarities or differences; with ratios, say how many times bigger by dividing one by the other.` | AQA defines "Compare" as describing similarities and/or differences. The lesson-specific move is kept as a second clause. | AQA command-word glossary |
| nanoparticles-C7 | same file — ladder r1: `K.find(slug, R.route, 'State the range of sizes') \|\| ` (the trailing `\|\| ` included; in the file this is the plain two-character OR) | `` (empty string: delete it, leaving `K.find(slug, R.route, 'Describe what happens to a particle') \|\| { options: [] }`) | On TF the needle hits TF7 ("State the range of sizes") while the rung carries command "Describe" and why "Smaller particle, larger surface area to volume ratio", which answer a different question. TF3 and TH3 are the same verbatim SA:V item, so one needle gives both routes a consistent rung. | 8462 4.2.4.1 |
| nanoparticles-C8 | same file — `keyLines[0]`: `They contain a few hundred atoms.` | `They are of the order of a few hundred atoms.` | This restores the spec's "of the order of" (see C2). It is the key-note line pupils memorise. | 8462 4.2.4.1 |

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (sizes, SA:V, uses, risks) | Triple (whole lesson; `notTriple` status; TF + TH only per contract §0) | 8462 4.2.4 "(chemistry only)"; absent from 8464 | OK | — |
| SA:V calculation (cube splitter, equation, CFIFA, ladder r2) | untagged within the lesson, shown on both TF and TH ("Foundation · Higher" badge) | 4.2.4.1 carries no (HT only) marker | OK. Flag 3 is confirmed: the source's `higher` field gating SA:V as Higher is wrong, and Design is right to ignore it. | — |
| PM10 / PM2.5 ranges | untagged (both triple tiers) | 4.2.4.1, no HT marker | OK | — |
| Uses and risks / evaluate | untagged (both triple tiers) | 4.2.4.2, no HT marker | OK | — |
| Graphene item in the bank (TF9, TH10) | served on TF/TH via the bank | 4.2.3.3 is core (both courses, no HT) | OK. It is not wrong on a triple route, just slightly off-lesson (see §4). | — |
| Content that should be tagged but is not | none found | — | OK | — |

## 4. Verbatim layer (the repo's four files)
| route | field | finding | change id if any |
|---|---|---|---|
| CF, CH | (whole dict) | Absent from `all_subtopics_chemistry.py` and `all_subtopics_chemistry_higher.py`. This is correct for chemistry-only 4.2.4. | — |
| TF, TH | `quiz` | Identical in content to `ks4-source.js` (the only differences are tuple vs list and int vs string keys in `wrong_explanations`, which are serialisation only). TF has 10 items and TH has 11 (flag 4). | — |
| TF | `quiz` TF1–TF10 | Every correct option and every `wrong_explanations` entry was checked against 4.2.4 and 4.2.3.3, and nothing is wrong. Nothing on the TF copy is HT (4.2.4 has no HT content). TF7 "1 to 100 nm" matches the spec. TF7's "mm are a million times larger" is right (1 mm = 10⁶ nm). TF8's "antibacterial agent" is not in the spec list but falls under medicine, so it is creditable. | — |
| TH | `quiz` TH1–TH11 | Every item was checked. TH5 wrong-explanation 3 ("Catalysts provide an alternative pathway") agrees with 8462 4.6.1.4. TH8 ("halving L doubles the ratio") is correct because the ratio is 6/L. TH11 is correct: 6/2 = 3 nm⁻¹ and 6/20 = 0.3 nm⁻¹. TH10's "fourth outer electron … delocalised" agrees with 4.2.3.2/4.2.3.3. | — |
| TF, TH | `quiz` TF9 / TH10 | These graphene items are 4.2.3.3 content inside a 4.2.4 bank. The science is correct and they are kept verbatim. They are noted only because this lesson's page no longer teaches graphene (it moved to L10). | — |
| TF, TH | `examiner_tip` | Identical to source. OK against 4.2.4.1. | — |
| TF, TH | `spec` | `"5.2.3.3"` is wrong. This is 8462 **4.2.4** (5.2.3.3 is graphene and fullerenes). The page already shows 4.2.4. The generator should display 4.2.4 and never this field, and the frozen py is not edited (flag 2). | — (generator display rule, not a page change) |
| TF, TH | `summary` / `key_note` / `theory` / `matching` | These mix in graphene and fullerenes (5.2.3.3). They are not served by the ported page, which uses Design's own `keyLines`. The science itself is correct. Theory's "a few hundred to a few thousand atoms" is looser than the spec, but it is not served. | — |
| TF | `fifas` | The repo's TF copy has DIFFERENT, unitless FIFAs ("sides of length 2 → 3", "1 → 6", "3 → 2"). The arithmetic is correct: 24/8, 6/1, 54/27. `ks4-source.js` carries only the TH FIFAs, so the page serves the nm-based TH FIFAs on TF as well. That is correct, since SA:V is not HT. It is recorded so the port does not "restore" the TF FIFAs. | — |
| TH | `higher` | This field ("Calculate surface area to volume ratio … Evaluate uses …") implies HT gating. That is wrong per 4.2.4.1, and Design ignores it correctly (flag 3). It is not served. | — |
| TF, TH | `triple_only` | `null`. Harmless, because the dicts exist only in the triple files. | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 2 (spec number) | The page must show **8462 4.2.4** (4.2.4.1 sizes and SA:V, 4.2.4.2 uses and risks). It already does, in the eyebrow, key note and evaluate eyebrow. The `5.2.3.3` in the filename and the py `spec` field is wrong, because 5.2.3.3/4.2.3.3 is graphene and fullerenes. Keep the site slug `nanoparticles` (its URL already exists). The design filename may keep the pilot slug, since it is not shown to pupils, but no generated text may print 5.2.3.3 for this lesson. | 8462 4.2.4 heading; 4.2.3.3 |
| 3 (SA:V gated Higher) | Confirmed: **not HT**. 4.2.4.1 carries no (HT only) marker, so the whole lesson (SA:V included) is Triple at both tiers. Design renders it that way. | 8462 4.2.4.1 |
| 4 (11 TH / 10 TF) | Confirmed and kept verbatim. The TF copy contains nothing HT. The only route issue is ladder r1's needle picking TF7 on TF, which C7 fixes. | 8462 4.2.4 |
| 5 (PM10/PM2.5 added) | Added correctly. All six sort items are in the right bins: dust 5 µm → coarse (2500–10 000 nm); soot 0.5 µm → fine; TiO₂ 20 nm → nano; Ag 1 × 10⁻⁸ m = 10 nm → nano; smoke 1 × 10⁻⁶ m = 1000 nm → fine; sea salt 8 µm → coarse. The sizes are physically realistic (diesel soot agglomerates reach about 0.5 µm, smoke is 0.01–1 µm, sea salt is coarse-mode), and none sits on a boundary. | 8462 4.2.4.1 |
| 16 (option order) | This is not a science matter. Re-ordering changes no text and no credited answer, and AQA papers do not fix option order. The science is neutral, so Mide or the build decides. | — |
| 18 (new science) | Verified. See §6. Five fixes (C1, C2, C5, C7, C8) touch new or re-cut text. Every new number is correct. | — |

## 6. New science introduced by Design (flag 18) — verified?
- Hook (ruby glass, gold 25 nm) and hook reveal: the science is correct. The reveal's "a large fraction" is overstated → C1.
- Explainer (sizes, atom size, PM ranges): the ranges are verbatim-correct. The atom size is wrong (0.1 nm is the radius) → C2.
- Size sort (6 items, conversions): all correct.
- Cube splitter (SIDES, tiles, commit, notes): all numbers are correct (SA 6L², V L³, ratio 6/L, ×10 per ÷10, 100× from 1000 nm to 10 nm). The drawing and alt-text counts are schematic or wrong → C3, C4.
- Spot-the-flaw (same substance): correct.
- Equation card (6L²/L³ = 6/L; L = 6/ratio; units): correct. The "Derived, not on any sheet" chip is accurate.
- CFIFA worked 2 (0.02 µm → 20 nm → 0.3 nm⁻¹): correct. The error note is imprecise → C5.
- CFIFA Q2 (5 × 10⁻⁸ m → 50 nm → 0.12 nm⁻¹; unconverted 1.2 × 10⁸ m⁻¹): correct.
- CFIFA restructure of verbatim FIFA 1 and FIFA 3 to Mide's rule (Formula un-rearranged; rearrangement at Fine-tune): done correctly, and the numbers are unchanged.
- Evaluate `Ks4Write` (TiO₂ sun cream, 4 marks): the points and reject list are creditable.
- Ladder r2 (3 × 10⁻⁹ m → 3 nm → 2 nm⁻¹, tol 0.01): correct.
- Ladder r3 (catalyst chain + 2 herrings): correct.
- Ladder r4 (silver dressing evaluate, 4 marks): correct.
- Key-note lines: correct, except line 1's "contain a few hundred atoms" → C8.
- Command words: "Compare" is narrower than AQA's definition → C6.
