# Examination — Properties of small molecules (properties-small-molecules) — AQA 8462 4.2.2.4 / 8464 5.2.2.4
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF (filestore.aqa.org.uk, v1.1 04 Oct 2019), read as text. 8464 5.2.2.4 is word-for-word the same as 8462 4.2.2.4. Also used: 8462 4.1.2.6 (Group 7), 4.2.1.4 (limitations of representations), 4.4.2.4 (acids give H⁺(aq)); 8464 5.7.1.3 (alkane boiling points).

Spec statement relied on throughout (8462 4.2.2.4 = 8464 5.2.2.4): *"Substances that consist of small molecules are usually gases or liquids that have relatively low melting points and boiling points. These substances have only weak forces between the molecules (intermolecular forces). It is these intermolecular forces that are overcome, not the covalent bonds, when the substance melts or boils. The intermolecular forces increase with the size of the molecules, so larger molecules have higher melting and boiling points. These substances do not conduct electricity because the molecules do not have an overall electric charge. Students should be able to use the idea that intermolecular forces are weak compared with covalent bonds to explain the bulk properties of molecular substances."*

Design file: `ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html` (below: "the page").

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | eyebrow (l.37) | "AQA Chemistry 5.2.2.4 · Model" | 8464 5.2.2.4 / 8462 4.2.2.4 | OK | Combined number; 8462 equivalent is 4.2.2.4. Same numbering convention as the rest of the pilot. |
| 2 | `.ks3-bigq` (l.39) | Chlorine gas, bromine liquid, iodine solid; each a pair of atoms held by one covalent bond | 4.1.2.6 ("molecules made of pairs of atoms"); 4.2.2.4 | OK | Room-temperature states match data (Cl₂ bp −34, Br₂ mp −7/bp 59, I₂ mp 114). Single bond X–X correct. |
| 3 | route badges (l.41–42) | "Combined · Triple", "Foundation · Higher" | 5.2.2.4 in 8464; no HT marker | OK | Whole lesson is base content on all four routes. |
| 4 | hook h2 + para (l.54–55) | Water boils at 100 °C | data | OK | |
| 5 | hook para | Splitting water needs "an electric current running through it for minutes, or a temperature of thousands of degrees" | context (4.4.3 electrolysis) | OK | Thermal dissociation of water becomes significant above ~2000 °C; electrolysis collects gas over minutes. Qualitative and true. |
| 6 | hook para | "Both processes start with the same H₂O molecules." | 4.2.2.4 | OK | |
| 7 | `hookOptions[0]` | "Whole water molecules, spread far apart" / reply "Test that on the model below." | 4.2.2.4 | OK | Correct idea; unscored reply, no verdict leak. |
| 8 | `hookOptions[1]` | "Hydrogen and oxygen gases" / "Then boiling would be the same process as splitting water. Is it?" | 4.2.2.4 | OK | Challenges the covalent-bonds-break misconception. |
| 9 | `hookOptions[2]` | Dissolved air / "A little air comes out at first, but the big bubbles keep coming long after." | general | OK | True: dissolved air leaves early as small bubbles. |
| 10 | `hookOptions[3]` | Empty bubble / "The bubble pushes the water aside, so something fills it." | general | OK | |
| 11 | `hookReveal` | "Steam is H₂O molecules, far apart and moving fast. Boiling pulls whole molecules away from each other. The O–H bonds inside each molecule are untouched…" | 4.2.2.4 ("intermolecular forces that are overcome, not the covalent bonds"); 4.2.2.1 (gas model) | OK | |
| 12 | explainer 1 (l.64) | "A small molecule is a fixed group of atoms joined by strong covalent bonds: H₂O, CH₄, Cl₂." | 4.2.1.4; 4.2.2.4 | OK | |
| 13 | explainer 1 | "Between one molecule and the next there are only weak intermolecular forces." | 4.2.2.4 ("only weak forces between the molecules") | OK | Spec wording. |
| 14 | explainer 1 | "two kinds of attraction… only the weak one decides when it melts or boils" | 4.2.2.4 | OK | |
| 15 | `MOL[0]` water | mp 0, bp 100 | data book | OK | |
| 16 | `MOL[1]` methane | mp −182, bp −161 | data book (mp −182.5, bp −161.5) | OK | Rounded; −161 matches the verbatim quiz Q1. |
| 17 | `MOL[2]` chlorine | mp −101, bp −34 | data book (−101.5 / −34.0) | OK | |
| 18 | `MOL[3]` bromine | mp −7, bp 59 | data book (−7.2 / 58.8) | OK | |
| 19 | `MOL[4]` iodine | mp 114, bp 184 | data book (113.7 / 184.3) | OK | |
| 20 | `MOL[].r` drawing radii | Cl 19, Br 23, I 28 (rising); CH₄ drawn smaller overall than Cl₂ | 4.2.2.4 (size) | OK | Order right. Real covalent radii Cl:Br:I = 1 : 1.15 : 1.34, drawn 1 : 1.21 : 1.47. So the drawing is qualitative (see #45). |
| 21 | `molecule()` water geometry | two H at ±0.9 rad about O (~103°) | 4.2.1.4 | OK | Bent shape; bond angle not examined. |
| 22 | `molecule()` methane | C with 4 H at 90° in 2D | 4.2.1.4 (2D representations) | OK | 2D projection; acceptable representation. |
| 23 | `molecule()` diatomics | two atoms joined by one thick line | 4.2.1.4 ("line to represent a single bond") | OK | |
| 24 | `model()` state logic | `T < mp` solid; `T < bp` liquid; else gas | 4.2.2.1 ("predict the states… given appropriate data") | OK | The boundaries are right (at mp it melts; at bp it boils). |
| 25 | `model()` dotted lines | intermolecular forces drawn dotted between near neighbours in solid/liquid, none in gas | 4.2.2.4 | OK | Caveat carried in `legal`. At GCSE, gas = forces overcome is the credited model. |
| 26 | `model()` gas | molecules drawn whole, bonds intact | 4.2.2.4 | OK | Core teaching point, shown correctly. |
| 27 | `model()` alt text (s/l/g) | "solid, molecules held in place by intermolecular forces" / "liquid, molecules close and moving past each other" / "gas, whole molecules far apart; the covalent bonds inside are intact" | 4.2.2.1; 4.2.2.4 | OK | |
| 28 | `modelNote` solid | "intermolecular forces (dotted) hold every molecule in place. The thick lines are covalent bonds." | 4.2.2.4 | OK | |
| 29 | `modelNote` liquid | "some intermolecular forces have been overcome; molecules slide past each other" | 4.2.2.1 / 4.2.2.4 | OK | Standard GCSE description. |
| 30 | `modelNote` gas | "every intermolecular force has been overcome. Each molecule is still whole." | 4.2.2.4 | OK | |
| 31 | `dataLine` | "<name> · melts X °C · boils Y °C" with minus sign | data | OK | |
| 32 | slider range | −270 to 220 °C | data | OK | Covers every mp and bp (lowest −182, highest 184). |
| 33 | default temp 20 °C per molecule | water liquid, CH₄ gas, Cl₂ gas, Br₂ liquid, I₂ solid | data | OK | Matches the big question. |
| 34 | `gatePrompt` | "You have just passed the boiling point of X. What has come apart?" | 4.2.2.4 | OK | |
| 35 | `gateOpts[0]` (credited) | "Whole molecules separate from each other" | 4.2.2.4 | OK | Only index 0 gets "Yes." |
| 36 | `gateOpts[1]` | "The covalent bonds inside the molecules break" → confront | 4.2.2.4 ("not the covalent bonds") | OK | Correctly treated as wrong. |
| 37 | `gateOpts[2]` | "Both…" → confront | 4.2.2.4 | OK | Correctly treated as wrong. |
| 38 | confront quote | "When it boils, the covalent bonds break." | 4.2.2.4 | OK | Named misconception, matches source common_mistake. |
| 39 | confront body | Molecules above bp still whole; "If the bonds broke, steam would be hydrogen and oxygen, and it would never condense back to water." | 4.2.2.4 | OK | H₂ + O₂ do not condense to water on cooling; the reasoning holds. |
| 40 | confront body | "A low boiling point tells you the forces between molecules are weak; it tells you nothing about the covalent bonds." | 4.2.2.4 | OK | Agrees with verbatim CH10/TH10. |
| 41 | `gateWord` | "Yes." / "The model disagrees." | house style | OK | Words, not ticks. |
| 42 | `gateReply` | "Only the weak intermolecular forces were overcome. Now try the other molecules: the bigger the molecule, the hotter you have to go." | 4.2.2.4 | CONTRADICTS | Default first molecule is water (bp 100). The next tab is methane: bigger, and drawn bigger (r 18 vs 17, five atoms against three), yet it boils at −161. Straight after the gate, the instrument disproves its own rule. Water's high bp comes from hydrogen bonding, which is not GCSE content, and verbatim Q1 attributes it only to "stronger intermolecular forces". Scope the rule to the halogens. → C2, C3 |
| 43 | explainer 2 (l.107) | "The bigger the molecule, the stronger the intermolecular forces… more energy it takes to separate them." | 4.2.2.4 ("increase with the size of the molecules") | OK | Spec statement. |
| 44 | explainer 2 | "That is the whole pattern down Group 7" | 4.1.2.6 ("further down the group… higher its relative molecular mass, melting point and boiling point") | OK | |
| 45 | explainer 2 | "…it is why most small-molecule substances are gases or liquids at room temperature while a few large ones are solids" | 4.2.2.4 ("usually gases or liquids") | OK | Acceptable. The weakness of the forces is the main reason, and size explains the solids. |
| 46 | explainer 2 | "Small molecules also never conduct electricity: a molecule has no overall charge, and there are no free electrons or ions." | 4.2.2.4 ("do not conduct electricity because the molecules do not have an overall electric charge"); 4.4.2.4 ("Acids produce hydrogen ions (H⁺) in aqueous solutions") | IMPRECISE | "Never" is false for a solution: HCl is a small molecule and hydrochloric acid conducts. The source's own theory notes this, and pupils electrolyse acids in 4.4.3. Also, "small molecules" do not conduct; the substance does not. Use the spec's unqualified "do not conduct". → C1 |
| 47 | explainer 2 | reason "no overall charge… no free electrons or ions" | 4.2.2.4 | OK | Spec reason plus the accepted mark-scheme alternative. |
| 48 | Rank prompt (l.113) | "The molecules are drawn to scale." | 4.2.2.4 | IMPRECISE | Radii are exaggerated by ~10–15% for I₂ (see #20). The order is right but "to scale" overclaims. → C4 |
| 49 | `rankSvg` alt | "…molecules drawn to scale, getting larger from left to right" | — | IMPRECISE | Same claim as #48. → C5 |
| 50 | `RANK` / `correct` | CH₄ < Cl₂ < Br₂ < I₂ (indices 1,2,3,4) | data; 4.2.2.4 | OK | bp −161 < −34 < 59 < 184. Water excluded from the ranking, which is correct. |
| 51 | `rankText` right | "CH₄ −161 °C, Cl₂ −34 °C, Br₂ 59 °C, I₂ 184 °C. Each molecule is larger than the last, so the intermolecular forces are stronger and more energy is needed…" | 4.2.2.4 | OK | Mr 16 < 71 < 160 < 254. |
| 52 | `rankText` wrong | "Size is the clue: the larger the molecule, the stronger the forces between molecules and the higher the boiling point." | 4.2.2.4 | OK | |
| 53 | Command word "Explain" | "Name the weak forces between molecules. Say the covalent bonds do not break." | AQA command words (explain = reasons/causes) | OK | Lesson-specific application; fine. |
| 54 | Command word "Suggest" | "Use the size pattern on a substance you have not met." | AQA ("apply knowledge… to a novel situation") | OK | |
| 55 | Command word "Use the data" | "Quote the numbers from the question in your answer." | AQA ("answer must be based on the information given") | OK | |
| 56 | Key fact | "Melting or boiling… overcomes the weak forces between molecules. The strong covalent bonds inside each molecule stay intact." | 4.2.2.4 | OK | |
| 57 | Examiner tip (`K.tip`) | verbatim: never write "the bonds break"; say weak IMFs overcome, covalent bonds intact | 4.2.2.4 | OK | Same text in all four repo files. |
| 58 | r1 (`K.find` 'State what is overcome when a simple molecular substance boils') | Verbatim Q4, present in CF4/CH4/TF4/TH4. `KS4.find` matches the route's own copy, so the TH fallback is never needed. | 4.2.2.4 | OK | Credited option: "The weak intermolecular forces between the molecules". |
| 59 | r1 `why` | "The weak intermolecular forces between molecules." | 4.2.2.4 | OK | |
| 60 | r1 wrong replies (verbatim) | covalent not broken / no ionic / no metallic bonds | 4.2.2.4 | OK | |
| 61 | r2 prompt | alkanes are small molecules that get larger from top to bottom | 8464 5.7.1.3 (bp vs molecular size); 4.2.2.4 | OK | |
| 62 | r2 table | pentane C₅H₁₂ 36; hexane C₆H₁₄ ?; heptane C₇H₁₆ 98 | data book (36.1, 68.7, 98.4) | OK | Formulae follow CₙH₂ₙ₊₂. |
| 63 | r2 part 1 | options −20 / 69 / 150 °C; answer 69 | 4.2.2.4; WS 3.5 (interpolate) | OK | 69 is the only option between 36 and 98, and it is the true value. |
| 64 | r2 part 2 | "The state of hexane at 25 °C": answer liquid | 4.2.2.1 ("predict the states… given appropriate data") | IMPRECISE | The data give no melting point, so solid and liquid cannot be told apart "using the data", yet the model answer says "it is above its melting point". AQA state-prediction items always give both mp and bp. Add hexane's mp (−95 °C, data book −95.3) to the part label. → C6 |
| 65 | r2 `right` | "Hexane is between the other two in size, so its boiling point is between theirs." | 4.2.2.4 | OK | |
| 66 | r2 `wrong` | "…Its boiling point must fall between 36 and 98 °C." | 4.2.2.4 | OK | |
| 67 | r2 `model[0]` | "Boiling point about 69 °C… hexane is between the two in size." | 4.2.2.4 | OK | |
| 68 | r2 `model[1]` | "At 25 °C hexane is below its boiling point, and it is above its melting point, so it is a liquid." | 4.2.2.1 | OK | Only after C6. Before C6 the melting point is unstated. |
| 69 | r3 link 1 | "Iodine molecules are larger than chlorine molecules." | 4.2.2.4 | OK | |
| 70 | r3 link 2 | "So the intermolecular forces between iodine molecules are stronger." | 4.2.2.4 | OK | |
| 71 | r3 link 3 | "More energy is needed to overcome them, so iodine's melting point is above room temperature." | 4.2.2.1 / 4.2.2.4 | OK | mp 114 °C. |
| 72 | r3 herring 1 | stronger I–I covalent bond / why "Melting does not break covalent bonds, so their strength does not set the melting point." | 4.2.2.4 | OK | Also true in fact: I–I is weaker than Cl–Cl, so the herring is doubly wrong. |
| 73 | r3 herring 2 | "Iodine is made of ions" / why "two non-metal atoms sharing a pair: a small molecule, no ions" | 4.2.1.4 | OK | |
| 74 | r3 command/marks | Explain, 3 | AQA | OK | The three links match three creditable points. |
| 75 | r4 question | "Methane, CH₄, boils at −161 °C and does not conduct electricity. Explain both properties." 4 marks | 4.2.2.4 | OK | |
| 76 | r4 point 1 | small molecules with weak IMFs between them | 4.2.2.4 | OK | |
| 77 | r4 point 2 | little energy to overcome weak forces → low bp | 4.2.2.4 | OK | |
| 78 | r4 point 3 | strong covalent bonds not broken on boiling | 4.2.2.4 | OK | AQA credits it as a separate point in 4/6-mark structure items. |
| 79 | r4 point 4 | no overall charge, no free electrons or ions → cannot conduct | 4.2.2.4 | OK | |
| 80 | r4 reject | "The covalent bonds are weak." / "The bonds break when it boils." | 4.2.2.4; AQA MS convention (reject "bonds break" for simple molecular) | OK | |
| 81 | key note line 1 | "Small molecules: a fixed number of atoms joined by strong covalent bonds." | 4.2.1.4 | OK | |
| 82 | key note line 2 | "Between molecules there are only weak intermolecular forces." | 4.2.2.4 | OK | |
| 83 | key note line 3 | "Melting and boiling overcome the intermolecular forces. The covalent bonds stay intact." | 4.2.2.4 | OK | |
| 84 | key note line 4 | "…low melting and boiling points: mostly gases or liquids at room temperature." | 4.2.2.4 ("usually") | OK | |
| 85 | key note line 5 | "Bigger molecules, stronger intermolecular forces, higher melting and boiling points." | 4.2.2.4 | OK | Spec statement. |
| 86 | key note line 6 | "They do not conduct: molecules have no overall charge." | 4.2.2.4 | OK | Spec wording, unqualified. The explainer should match it (C1). |
| 87 | Ks4KeyNote `spec` | "AQA 5.2.2.4" | 8464 | OK | |
| 88 | `tutor-line` | "Mixing up bonds and intermolecular forces?" | — | OK | |
| 89 | `legal` sentence 1 | "Melting and boiling points are rounded data-book values." | data | OK | Every value checked (#15–19, #62). |
| 90 | `legal` sentence 2 | "…intermolecular forces are not bonds and do not join particular pairs of molecules." | 4.2.2.4 | OK | A correct model limitation. |
| 91 | `legal` sentence 3 | "Iodine sublimes when heated gently in an open tube, but at atmospheric pressure it does melt at 114 °C." | data (triple point 113.5 °C, 12.1 kPa) | OK | True. Its vapour pressure near mp explains the open-tube sublimation. |
| 92 | `legal` (missing) | Nothing warns that water does not follow the size rule the page teaches | 4.2.2.4 | IMPRECISE | Water is on the bench beside larger methane (see #42). Add one sentence. → C3 |
| 93 | `endPrev`/`endNext`/`endConnects` | ionic compounds ← → polymers; covalent bonding, states of matter | spec order 4.2.2.3 → 4.2.2.5 | OK | |
| 94 | RAIL labels | "Inside a steam bubble", "The two-forces model", "Rank it", "Exam ladder" | — | OK | |
| 95 | `done` flags | model done when gate answered and ≥3 molecules taken past bp | — | OK | No science claim. |
| 96 | title/h1/Ks4Chrome unit | "Properties of small molecules" / "Bonding, structure and properties" | 4.2.2.4 | OK | |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| properties-small-molecules-C1 | `ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html` — `Small molecules also never conduct electricity:` | `Small-molecule substances also do not conduct electricity:` | "Never" is false: HCl(aq) and other acids made from small molecules conduct (4.4.2.4, 4.4.3), and the source's own theory says so. The spec says "do not conduct" of the *substances*. | 8462 4.2.2.4; 4.4.2.4 |
| properties-small-molecules-C2 | same file — `Now try the other molecules: the bigger the molecule, the hotter you have to go.` | `Now try the other molecules: for chlorine, bromine and iodine, the bigger the molecule, the hotter you have to go.` | Water is the default first molecule and methane is the next tab. Methane is bigger and boils 261 °C lower, so the unscoped rule contradicts the bench. The halogens obey the rule (4.1.2.6) and are the lesson's ranking set. | 8462 4.2.2.4; 4.1.2.6 |
| properties-small-molecules-C3 | same file — `but at atmospheric pressure it does melt at 114 °C.` | `but at atmospheric pressure it does melt at 114 °C. Water boils far higher than its small size suggests: its molecules have an extra, stronger kind of intermolecular force, which GCSE does not require.` | This is the model-limits line. The bench shows water (small, bp 100) beside methane (larger, bp −161) with no explanation. Hydrogen bonding is outside the spec, so name it only as "stronger intermolecular force", which agrees with verbatim Q1's credited answer. | 8462 4.2.2.4 |
| properties-small-molecules-C4 | same file — `The molecules are drawn to scale.` | `The molecules are drawn roughly to scale.` | Drawn radii exaggerate the real Cl:Br:I size ratio (1 : 1.21 : 1.47 against 1 : 1.15 : 1.34). The order is right but "to scale" is an overclaim. | 8462 4.2.1.4 (limitations of representations) |
| properties-small-molecules-C5 | same file — `molecules drawn to scale, getting larger` | `molecules drawn roughly to scale, getting larger` | As C4 (alt text). | 8462 4.2.1.4 |
| properties-small-molecules-C6 | same file — `label: 'The state of hexane at 25 °C'` | `label: 'The state of hexane at 25 °C (it melts at −95 °C)'` | "Use the data" cannot decide solid against liquid without a melting point, and the model answer cites one the pupil was never given. Hexane mp is −95.3 °C (data book). The file stores these as literal `\u` escapes in a JS string, so keep the escapes. | 8462 4.2.2.1 ("predict the states of substances… given appropriate data") |

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (small molecules: IMFs vs covalent bonds, size trend, non-conduction) | base (all four routes; badges "Combined · Triple", "Foundation · Higher") | 8462 4.2.2.4 / 8464 5.2.2.4, no HT marker, not "chemistry only" | OK | — |
| Two-forces model incl. state prediction from mp/bp | base | 4.2.2.1 (predict states from data), no HT marker | OK | — |
| Rank it (halogens) | base | 4.2.2.4 + 4.1.2.6, both base | OK | — |
| Ladder r2 alkane data | base | 8464 5.7.1.3 base; also used as unfamiliar-data application of 4.2.2.4 | OK | — |
| Anything that should be tagged Higher or Triple and is not | — | no HT or chemistry-only statement in 4.2.2.4 | none found | — |
| "More electrons → stronger IMFs" (verbatim CH6, TH6, TH11 and the source theory) | untagged, bank only | not a spec statement (spec: "size of the molecules") | OK as served | — (not taught in the body. True, and creditworthy as "larger molecules") |

## 4. Verbatim layer (the repo's four files)
The repo quizzes in `all_subtopics_chemistry*.py` were compared field by field with `ks4-source.js` and are identical on every route (CF 10, CH 10, TF 12, TH 12 items). `examiner_tip`, `key_note`, `higher: null`, `triple_only: null`, `fifas: []`, `rp: null` are the same in all four files.

| route | field | finding | change id if any |
|---|---|---|---|
| all | quiz Q1 (CF1/CH1/TF1/TH1) water vs methane | Credited answer is "stronger intermolecular forces" in water. True, and correctly avoids hydrogen bonding (not in spec). Wrong-explanation 1 ("water has 2 and methane has 4" covalent bonds) is correct. | — |
| all | quiz Q2 no conduction | "no free electrons or ions" credited. The spec's reason is "no overall electric charge", and AQA mark schemes also accept "no delocalised electrons / no ions". OK. | — |
| all | quiz Q3, Q4, Q5 | Correct against 4.2.2.4 and 4.2.1.4. Q4 is the r1 item. | — |
| CF, TF | quiz 6–10 (high/low mp; conduct?; name force; identify CO₂; bonds break?) | All correct. CO₂ is a simple molecule; NaCl, Cu and diamond are correctly rejected. | — |
| CH, TH | quiz 6 (larger molecules) | "more electrons, giving stronger IMFs" goes beyond the spec's wording but is true. Base content, so serving it on Higher copies only is harmless. | — |
| CH, TH | quiz 7, 8, 9, 10 | Correct (4.2.2.4). The 9 deduction, "low mp + non-conducting in any state → simple molecular", is standard AQA. | — |
| TF | quiz 11 "two reasons" | "no free electrons and no free ions" credited. Acceptable. | — |
| TF | quiz 12 | "Gases or liquids (with some low-melting solids)" matches "usually gases or liquids". | — |
| TH | quiz 11 Cl₂ vs I₂ | Correct. It duplicates the r3 chain, which is fine. | — |
| TH | quiz 12 limitation of a single-molecule drawing | Matches 8462 4.2.1.4 ("describe the limitations of using… diagrams to represent molecules"). That is base content, not HT, but serving it on TH only does no harm. | — |
| all | option order / length | Every item has the credited option at index 0 (neutralised by `KS4.item`'s hash sort). In CH7, CH9, TH11 and TH12 it is also clearly the longest option, which is a residual tell. That is outside the science remit and is not changed here (flag 16). | — |
| all | route-gating errors | None: no HT-only or chemistry-only content is served on a route that should not see it. | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 16 (option order) | Keep the hash re-order ON. Order carries no science, and index-0-always is a tell that AQA papers do not have. Reordering changes no text, so the verbatim rule is not breached. The longest-option tell stays on CH7/CH9/TH11/TH12; recorded, not fixed (outside science remit). | — |
| 17 (data values) | All confirmed as rounded data-book values: H₂O 0/100; CH₄ −182/−161 (−182.5/−161.5); Cl₂ −101/−34 (−101.5/−34.0); Br₂ −7/59 (−7.2/58.8); I₂ 114/184 (113.7/184.3); pentane 36 (36.1), hexane 69 (68.7), heptane 98 (98.4). Rank order CH₄ < Cl₂ < Br₂ < I₂ is correct. The slider state logic uses these values correctly. Water is on the bench but not in the ranking, which is right. The bench's generalisation after water was not right: fixed by C2 and C3. The added hexane mp −95 °C (C6) is data book −95.3. The hardness-vs-carbon data is not in this lesson. | 4.2.2.1; 4.2.2.4 |
| 18 (new science) | Hook, gate, confront, rank, r2, r3 and r4 all verified (section 6). Required: C2 and C3 (water against the size rule) and C6 (r2 missing mp). | 4.2.2.4 |

## 6. New science introduced by Design (flag 18) — verified?
- Hook (steam bubble, four options + reveal): **verified correct.**
- Two-forces bench (five molecules, state from mp/bp, dotted IMFs vanish, bonds persist): **verified correct** on values and state logic. The rule stated after the gate conflicts with water against methane on the same bench. **C2 + C3.**
- Gate (credited "whole molecules separate") + amber confront ("covalent bonds break"): **verified correct.**
- Rank it (CH₄ < Cl₂ < Br₂ < I₂, reveal text): **verified correct.** The "drawn to scale" wording is overclaimed: **C4 + C5.**
- Explainer 2: correct apart from "never conduct": **C1.**
- Ladder r2 (alkane data; hexane ≈ 69 °C; liquid at 25 °C): the estimate is **verified correct** (true value 68.7 °C). The state part lacks the melting point its own model answer relies on: **C6.**
- Ladder r3 (Cl₂ gas vs I₂ solid chain + two herrings): **verified correct.** The order is causal, and both herrings are wrong for the reasons given.
- Ladder r4 (methane, 4 marks, four points, two rejects): **verified correct.** It is AQA-creditable as written.
- Key note (6 lines), key fact, command words, `legal` line: **verified correct.** The `legal` line gets the water sentence (C3).
