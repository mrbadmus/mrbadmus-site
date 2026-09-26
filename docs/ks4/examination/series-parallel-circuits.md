# Examination — Series and parallel circuits (series-parallel-circuits) — AQA 8463 4.2.2 / 8464 6.2.2
Verdict: CHANGES REQUIRED
Examiner: Opus, 25 Sep 2026. Spec sources fetched: AQA-8463-SP-2016.PDF (v1.1, 30 Sep 2019) and AQA-8464-SP-2016.PDF (v1.1, 04 Oct 2019) from filestore.aqa.org.uk — text extracted, §4.2.1.1 symbol table viewed as an image; both equation-sheet PDFs in `ks4-lib.js` `EQ_BY_YEAR[2026]` downloaded and read in full (8463 sheet and 8464/8465 sheet, both headed "FOR USE IN JUNE 2026 ONLY"). Mark-scheme conventions (level descriptors, unit marks) from examiner knowledge of AQA 8463/8464 papers 2018–2024; not fetched.

Design file: `docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and Electricity/ks4-physics-6.2.2-series-parallel-circuits.dc.html` (called L13 below). The source key in `ks4-source.js` is `series-and-parallel`; the repo id is `series-parallel-circuits`.

**Numbering note.** In 8463 GCSE Physics this content is **4.2.2**. **6.2.2** is its number in 8464 Combined Science: Trilogy. The page's eyebrow "AQA Physics 6.2.2" and the key-note "AQA 6.2.2" use the 8464 number. That is the house convention for the whole pilot (chemistry uses 5.x, which is also the 8464 numbering), so I have not changed it here. It is recorded for the commander as a pilot-wide decision: a Triple pupil looking in 8463 will find no section 6.

Spec statements relied on (verbatim, 8463 4.2.2 = 8464 6.2.2):
- "For components connected in series: there is the same current through each component; the total potential difference of the power supply is shared between the components; the total resistance of two components is the sum of the resistance of each component. R_total = R1 + R2"
- "For components connected in parallel: the potential difference across each component is the same; the total current through the whole circuit is the sum of the currents through the separate components; the total resistance of two resistors is less than the resistance of the smallest individual resistor."
- "explain qualitatively why adding resistors in series increases the total resistance whilst adding resistors in parallel decreases the total resistance"; "calculate the currents, potential differences and resistances in dc series circuits"; "Students are not required to calculate the total resistance of two resistors joined in parallel."
- 8463 4.2.1.3 / 8464 6.2.1.3: "V = I R … Students should be able to recall and apply this equation." 8463 4.2.3.1 / 8464 6.2.3.1: domestic supply "about 230 V".
- 8463 RP3 / 8464 RP15 (quoted in full under flag 12 below).

## 1. Checked items
| # | Where (element / constant name / template line) | Claim as written | Spec section | Verdict (OK / WRONG / IMPRECISE / CONTRADICTS) | Note |
|---|---|---|---|---|---|
| 1 | header eyebrow l.36 | "AQA Physics 6.2.2 · System" | 8463 4.2.2 / 8464 6.2.2 | OK (convention) | This is the 8464 number. See the numbering note above. |
| 2 | header badges l.40–41 | "Combined · Triple", "Foundation · Higher" | 8463 4.2.2 / 8464 6.2.2 (no HT marker, no "physics only") | OK | Base content on all four routes. |
| 3 | big question l.38 | "Change one resistor in a circuit and every reading can move." | 4.2.2 | OK | This is framing. Step 3 of the bench shows the case where a reading does *not* move. |
| 4 | equation-sheet link, `K.route` → `eqSheetHref` | Triple → 8463 PDF; Combined → 8464/8465 PDF | flag 22 | OK | Both URLs return HTTP 200 application/pdf. Both are headed "FOR USE IN JUNE 2026 ONLY". |
| 5 | fallback `eqSheetLabel` in `renderVals` | "GCSE Physics (8463) · June 2026" | — | OK | Matches the PDF header. |
| 6 | hook h2 l.57 | "A 4 Ω resistor and an 8 Ω resistor, one 12 V battery." | 4.2.2 | OK | — |
| 7 | `hookFig` (`fig(CFG[0], false)`) | series loop: ammeter, R₁ 4 Ω, R₂ 8 Ω; battery 12 V; switch open; voltmeter across R₁ | 4.2.1.1, 4.2.2 | OK (see #50 for symbol drawing) | Meters are placed correctly: the ammeter is in series and the voltmeter is in parallel with R₁. |
| 8 | hook prompt | "The two resistors are in series. Which one has the bigger potential difference across it?" | 4.2.2 | OK | — |
| 9 | `hookOptions[0]` "The 8 Ω resistor" / reply | "Check it against the bench below." | 4.2.2 | OK | This is the correct answer. The hook is ungraded by design (no `correct` flag). |
| 10 | `hookOptions[1]` 4 Ω / reply | "Tempting: it lets current through more easily. But both carry the same current." | 4.2.2 "same current through each component" | OK | — |
| 11 | `hookOptions[2]` equal / reply | "Equal shares would need equal resistances." | 4.2.2 | OK | — |
| 12 | `hookOptions[3]` full 12 V / reply | "That is true in parallel, not in series." | 4.2.2 | OK | — |
| 13 | `hookReveal` | "same current … 1 A here … 4 V across the 4 Ω and 8 V across the 8 Ω, adding up to … 12 V" | 4.2.2, 4.2.1.3 | OK | Recomputed: R = 12 Ω, I = 12/12 = 1 A, V₁ = 4 V, V₂ = 8 V, and 4 + 8 = 12 V. ✓ |
| 14 | explainer l.67 | "In a series circuit there is one loop. The same current passes through every component" | 4.2.2; 4.2.1.2 "A current has the same value at any point in a single closed loop." | OK | — |
| 15 | explainer l.67 | "the battery's potential difference is shared between them: bigger resistance, bigger share" | 4.2.2 | OK | Follows from V = IR with a common I. |
| 16 | explainer l.67 | "Resistances add: R_total = R₁ + R₂" | 4.2.2 | OK | — |
| 17 | explainer l.67 | "each branch is connected straight across the battery, so every branch has the full potential difference, and the branch currents add up to the current from the battery" | 4.2.2 parallel bullets | OK | This is exact for simple parallel branches with an ideal cell, as the `legal` line states. |
| 18 | `CFG` / `read()` | series: I = V/ΣR, V₁ = I·R₁; parallel: I = ΣV/Rᵢ, V₁ = V | 4.2.2, 4.2.1.3 | OK | The physics model is correct for an ideal source. No parallel total-resistance formula is used, which satisfies flag 15. |
| 19 | bench change 1 `whyI` | "Total resistance rises from 12 Ω to 24 Ω … half the current: 0.5 A." | 4.2.2 | OK | 4 + 20 = 24 Ω; 12/24 = 0.5 A. ✓ Direction: down ✓ |
| 20 | bench change 1 `whyV` | "V = I R = 0.5 × 4 = 2 V." | 4.2.1.3 | OK | It was 4 V, so it goes down. ✓ |
| 21 | bench change 2 `whyI` | "3 A through R₁ and 1.5 A through R₂, 4.5 A in total." | 4.2.2 | OK | 12/4 = 3 A, 12/8 = 1.5 A, total 4.5 A (was 1 A, so up). ✓ |
| 22 | bench change 2 `whyV` | "R₁ is now connected straight across the battery, so it has the whole 12 V." | 4.2.2 | OK | 4 V → 12 V, so up. ✓ |
| 23 | bench change 3 `whyI` | "The new branch takes its own 1 A … total rises to 5.5 A." | 4.2.2 | OK | 12/12 = 1 A; 4.5 + 1 = 5.5 A. ✓ |
| 24 | bench change 3 `whyV` | "Every branch is across the battery, so R₁ still has 12 V." | 4.2.2 | OK | Stays the same. ✓ |
| 25 | bench change 4 `whyI` | "The broken branch carries nothing; the others still carry 3 A and 1 A. The total falls to 4 A." | 4.2.2 | OK | 3 + 1 = 4 A (was 5.5 A, so down). ✓ |
| 26 | bench change 4 `whyV` | "R₁ is still across the battery: 12 V, and its lamp would stay lit." | 4.2.2 | IMPRECISE | There is no lamp in this circuit. R₁ is a resistor, so "its lamp" names a component that does not exist. → C2 |
| 27 | bench change 4 figure, `fig()` | the broken R₂ branch is drawn as an open **switch** labelled "R₂ removed" | 4.2.1.1 | IMPRECISE | The title says the branch *breaks*, but the label says *removed*, and the symbol is a switch. A switch in a branch is a real component on the AQA sheet, so the label should say what it stands for. → C3 |
| 28 | `truth` / `dir()` | the direction verdicts computed from `read()` | — | OK | I checked all eight verdicts against #19–#25. |
| 29 | confront quote l.103 | "Adding another resistor always adds resistance, so the current must fall." | 4.2.2 | OK | Correctly presented as the misconception. |
| 30 | confront body l.104 | "True in series, false in parallel … More current for the same p.d. means less total resistance. Two resistors in parallel always resist less than the smaller one on its own." | 4.2.2 "explain qualitatively … parallel decreases"; "less than … the smallest individual resistor" | OK | This is qualitative only, which satisfies flag 15. |
| 31 | confront placement `st === 3` | opens at "add a branch" | — | OK | This is where the error is born. |
| 32 | Sort `done-note` l.111 | "In series, current is shared by nothing and p.d. is shared out. In parallel, p.d. is shared by nothing and current is shared out." | 4.2.2 | OK | The phrasing is unusual but correct. |
| 33 | `rItems[0]` → s | "The current is the same through every component." / "One loop, one current." | 4.2.2 | OK | — |
| 34 | `rItems[1]` → s | "The battery's p.d. is shared between the components." / "The shares add up to the supply p.d." | 4.2.2 | OK | — |
| 35 | `rItems[2]` → s | "R_total = R₁ + R₂" / "Resistances in series add." | 4.2.2 | OK | — |
| 36 | `rItems[3]` → p | "Every branch has the same p.d. as the battery." / "Each branch connects straight across the supply." | 4.2.2 | OK | — |
| 37 | `rItems[4]` → p | "The currents in the branches add up to the total current." / "Charge splits at a junction and rejoins." | 4.2.2 | OK | — |
| 38 | `rItems[5]` → p | "The total resistance is less than the smallest resistance." / "Each extra branch is an extra path." | 4.2.2 | OK | — |
| 39 | `rItems[6]` → s | "If one component breaks, everything stops." / "There is only one path." | 4.2.2 "describe the difference between series and parallel circuits" | OK | — |
| 40 | equation card 1 chip | "Equation sheet" on V = I R | 2026 sheets | OK | V = I R is on both June 2026 sheets: "potential difference = current × resistance  V = I R". |
| 41 | equation card 1 text | "V = I R … potential difference (V, volts) = current (I, amperes) × resistance (R, ohms) · I = V ÷ R · R = V ÷ I" | 4.2.1.3 | OK | Units match the spec. |
| 42 | equation card 2 | "R_total = R₁ + R₂" with **no chip** | 4.2.2; 2026 sheets | IMPRECISE | This is **not on either 2026 sheet** (I read both in full; there is no resistance-sum line). It is an equation printed in the spec at 4.2.2, so pupils must learn it. The ruling is to add the chip "Not on the sheet · learn it". → C1 (flag 21) |
| 43 | equation card 2 text | "for resistors in series only. In parallel, say the total is less than the smallest; you are not asked to calculate it." | 4.2.2 last sentence | OK | Flag 15. |
| 44 | equation card 3 "Units first" | "Current must be in amperes. 1 mA = 0.001 A: divide a milliamp reading by 1000" | 4.2.1.3 (I in A) | OK | — |
| 45 | CFIFA ex.1 head `F[0].question` | "R₁ = 3 Ω and R₂ = 7 Ω in series with a 20 V battery. Find the current and pd across each resistor." | 4.2.2 | OK | Verbatim source. |
| 46 | CFIFA ex.1 C/F/I | "Nothing to convert …" / "R_total = R₁ + R₂; V = I R" / "R_total = 3 + 7 = 10 Ω; 20 = I × 10" | 4.2.2 | OK | The Formula line matches the sheet form ("V = I R") and follows the CFIFA correction. |
| 47 | CFIFA ex.1 F/A | "I = 20 ÷ 10 = 2 A; V₁ = 2 × 3 = 6 V; V₂ = 2 × 7 = 14 V … (check: 6 + 14 = 20 V)" | 4.2.2 | OK | Recomputed. ✓ |
| 48 | CFIFA ex.2 (new) | 6.0 V, 250 mA, R₁ = 8.0 Ω → 0.25 A; R_total = 24 Ω; R₂ = 16 Ω | 4.2.2 "equivalent resistance" | OK | 6.0/0.25 = 24; 24 − 8.0 = 16 Ω. ✓ |
| 49 | CFIFA ex.2 Answer note | "Unconverted, 6.0 ÷ 250 gives 0.024 Ω, and R₂ would come out negative" | — | OK | 0.024 − 8.0 < 0. ✓ |
| 50 | circuit engine symbols used on this page (`ks4-diagrams.js` `SYM`) | resistor, ammeter, voltmeter, battery, switch | 4.2.1.1 symbol table | IMPRECISE (battery, switch) | Resistor, ammeter and voltmeter match AQA. The **battery** leads stop about 9–13 px short of the plates, the two cells are not joined, and there is no dashed link, so the loop is drawn visibly open. The **switch** contacts are filled dots, which on a circuit diagram read as junctions; AQA draws hollow circles. The fixes are recorded once, in `resistors.md` C10–C12, because the engine is shared. |
| 51 | CFIFA Q1 (new) | 5.0 Ω + 15 Ω, 10 V → 20 Ω, 0.50 A, V₂ = 7.5 V; close "V₁ = 2.5 V, 2.5 + 7.5 = 10 V" | 4.2.2 | OK | Recomputed. ✓ |
| 52 | CFIFA Q2 (new) | 400 mA, 12 Ω + 18 Ω → 0.40 A; 30 Ω; V = 12 V; close "400 × 30 gives 12 000 V" | 4.2.2 | OK | Recomputed. ✓ The Fine-tune line says "Nothing to rearrange", which follows the CFIFA correction. |
| 53 | command word "Calculate" | "Show every line. The unit earns its own mark." | AQA command-word glossary ("Calculate: students should use numbers given in the question to work out the answer") | IMPRECISE | This is not a general rule of AQA marking. Most AQA physics calculations print the unit on the answer line, so no mark is available for it. A separate unit mark is given only when the pupil has to supply the unit. → C4 |
| 54 | command word "Determine" | "Use the circuit diagram or the data to work it out." | AQA glossary ("use given data or information to obtain an answer") | OK | — |
| 55 | command word "Explain" | "Say what changes and why, using current, p.d. and resistance." | AQA glossary | OK | — |
| 56 | key fact l.153 | "Series: same current, p.d. shared, R_total = R₁ + R₂. Parallel: same p.d., currents add, total resistance less than the smallest branch." | 4.2.2 | OK | — |
| 57 | examiner tip l.161 (draft) | verbatim in §5, flag 11 | — | not approved (flag 11) | There is no factual error. See §5. |
| 58 | Ladder r1 `K.find(slug, route, 'pd across each lamp')` | "Two lamps are connected in parallel across a 6 V battery. What is the pd across each lamp?" (correct: "6 V each — every branch …") | 4.2.2 | OK | Verbatim. The needle matches the one TH item, and every route falls back to TH, so the result is the same on all four. |
| 59 | r1 `why` | "Each branch is connected across the battery, so each lamp has the full 6 V." | 4.2.2 | OK | — |
| 60 | r1 wrong explanations (verbatim) | "Pd splitting happens in SERIES…", "Parallel circuits never increase voltage beyond the supply.", "…only the branch CURRENT changes with resistance." | 4.2.2 | OK | — |
| 61 | r2 prompt (new) | 6.0 Ω + 9.0 Ω, 800 mA → battery p.d. | 4.2.2 | OK | — |
| 62 | r2 `convAnswer: 1` | "Convert mA to A: divide by 1000" | 4.2.1.3 | OK | — |
| 63 | r2 `answer: 12, tol: 0.05, unit: 'V'` | 0.80 × 15 = 12 V | 4.2.2 | OK | Recomputed: 0.80 × 15 = 12.0. The tolerance is absolute (`Ks4Ladder` l.209–210), so it accepts 12 and 12.0. Unit V ✓. The distractor units A, Ω and W are all plausible. |
| 64 | r2 `right` / `wrong` / `model` | "0.80 A × 15 Ω = 12 V."; model C/F/I/F/A lines | 4.2.2 | OK | — |
| 65 | r3 links (order) | new branch = another path at full p.d. → total current up at the same p.d. → R = V ÷ I, so the total is lower, "less than either resistor alone" | 4.2.2 "explain qualitatively … parallel decreases" | OK | The chain order is logical and uses only qualitative reasoning. |
| 66 | r3 herring 1 | "Resistances always add, so the total resistance increases." / "That is the rule for series only." | 4.2.2 | OK | — |
| 67 | r3 herring 2 | "The current splits, so each resistor gets less p.d." / "In parallel each branch keeps the full p.d." | 4.2.2 | OK | — |
| 68 | r4 question (new, 6 marks) | "The lights in a house are wired in parallel. Explain why this is better than wiring them in series. Refer to the potential difference, the current, and what happens when one lamp fails." | 4.2.2; 4.2.3.1 | OK | This is a standard AQA-style extended question. |
| 69 | r4 levels | L3 5–6 "detailed … each linked … contrasted with series"; L2 3–4; L1 1–2; 0 | AQA level-of-response convention | OK | These match AQA's three-level, 6-mark structure. |
| 70 | r4 point 1 | "In parallel, every lamp has the full mains p.d. (230 V) across it." | 4.2.3.1 "about 230 V" | OK | — |
| 71 | r4 point 2 | "In series the p.d. would be shared, so each lamp would get only part of it and be dim." | 4.2.2 | OK | — |
| 72 | r4 point 3 | "Each lamp is on its own branch, so it can be switched on and off independently." | 4.2.2 | OK | This assumes a switch on each branch, which is how AQA mark schemes credit "independent". |
| 73 | r4 point 4 | "If one lamp fails in parallel, the other branches are still complete, so the other lamps stay on." | 4.2.2 | OK | — |
| 74 | r4 point 5 | "In series, one failure breaks the only path, so every lamp goes out." | 4.2.2 | OK | — |
| 75 | r4 point 6 | "Adding lamps in parallel does not dim the others; the total current rises instead." | 4.2.2 | OK | This is true for an ideal supply. |
| 76 | r4 reject | "'In parallel the current is the same everywhere.' That is series." | 4.2.2 | OK | — |
| 77 | keyLines[0] | "Series: one path. The same current through every component." | 4.2.2 | OK | — |
| 78 | keyLines[1] | "Series: the supply p.d. is shared. Bigger resistance, bigger share." | 4.2.2 | OK | — |
| 79 | keyLines[2] | "Series: R_total = R₁ + R₂." | 4.2.2 | OK | — |
| 80 | keyLines[3] | "Parallel: every branch has the same p.d. as the supply. Branch currents add up to the total." | 4.2.2 | OK | — |
| 81 | keyLines[4] | "Parallel: total resistance is less than the smallest branch resistance. Adding a branch lowers it." | 4.2.2 | OK | — |
| 82 | keyLines[5] | "V = I R. Convert mA to A first." | 4.2.1.3 | OK | — |
| 83 | Ks4End `legal` | "The bench treats the battery as having no internal resistance and every resistor as fixed … Real meters and cells give slightly lower readings. Circuit symbols follow the AQA symbol sheet." | 4.2.1.1 | OK | "Follow the AQA symbol sheet" becomes true once the engine fixes in `resistors.md` C10–C12 land. |
| 84 | Ks4End `endPrev` | "Nanoparticles" (L12) | 8462 4.2.4 (chemistry only) | route issue | This links a Combined pupil to a Triple-only lesson. See §3. |
| 85 | Ks4QuizBank `K.bank(slug, route)` | 2 verbatim TH items on every route | — | OK | See §4. |

## 2. Required changes
| id | where (Design file + the exact `old` string, verbatim, unique in the file) | new string (verbatim) | why | spec section |
|---|---|---|---|---|
| series-parallel-circuits-C1 | `ks4-physics-6.2.2-series-parallel-circuits.dc.html`: `<p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">R<sub>total</sub> = R₁ + R₂</p>` | `<span style="display: inline-block; margin-bottom: 8px; font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; border: 2px solid var(--ks3-ink);">Not on the sheet · learn it</span><p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">R<sub>total</sub> = R₁ + R₂</p>` | Flag 21, as ruled. R_total = R₁ + R₂ is printed in the spec but is absent from both June 2026 equation sheets, which I read in full. The chip copies the style of the "Equation sheet" chip on card 1. | 8463 4.2.2 / 8464 6.2.2; AQA 8463 and 8464/8465 equation sheets, June 2026 |
| series-parallel-circuits-C2 | same file: `'R₁ is still across the battery: 12 V, and its lamp would stay lit.'` | `'R₁ is still across the battery, so it still has the full 12 V and still carries 3 A.'` | There is no lamp in the circuit. The new text states the reading the pupil has just predicted. | 4.2.2 |
| series-parallel-circuits-C3 | same file: `name: 'R₂ removed'` | `name: 'R₂ branch broken'` | The step title is "The R₂ branch breaks.", but the drawn symbol is an open switch labelled "removed". The label should match the event and say what the open symbol stands for. | 4.2.1.1, 4.2.2 |
| series-parallel-circuits-C4 | same file: `Show every line. The unit earns its own mark.` | `Show every line. If the answer line does not print the unit, give it: it can carry a mark.` | As written, this states a marking rule AQA does not apply. The unit is usually printed on the answer line, and it earns a mark only when the pupil must supply it. | AQA command-word glossary; AQA 8463 mark-scheme convention |
| series-parallel-circuits-C5 | frozen/served `rp` field, `id: 'series-parallel-circuits'`, in each of `all_subtopics_physics.py`, `all_subtopics_physics_higher.py`, `all_subtopics_physics_triple_foundation.py`, `all_subtopics_physics_triple_higher.py` (once per file): `RP15 (Physics) — Construct series and parallel circuits; measure I and V at different points to verify rules.` | `RP15 (Combined Science) / RP3 (Physics) — Use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits, including the length of a wire at constant temperature and combinations of resistors in series and parallel.` | Flag 12. The source describes a practical that does not exist. AQA's RP is about *resistance*: the length of a wire, and resistors in series and parallel. It also mislabels the Combined number as "Physics". Apply this as a ruling on the GENERATED route copy (the port serves `rp` verbatim), not as a hand edit of the frozen py. | 8464 6.2.1.3 RP15 and 8463 4.2.1.3 RP3: "Use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits. This should include: the length of a wire at constant temperature; combinations of resistors in series and parallel." |

Circuit-engine changes that also affect this page are recorded once, in `resistors.md` (C10 cell, C11 battery, C12 switch).

## 3. Route tags
| content | Design's tag | spec label | verdict | change id if any |
|---|---|---|---|---|
| Whole lesson (series and parallel rules, V = IR, R_total, qualitative parallel R) | base, all four routes | 8463 4.2.2 / 8464 6.2.2: no (HT), not "physics only" | OK | — |
| Parallel total-resistance calculation | absent | 4.2.2: "not required to calculate" | OK (correctly absent) | — |
| Mains 230 V in r4 | base | 8464 6.2.3.1 / 8463 4.2.3.1: base | OK | — |
| `higher` / `triple_only` fields in all four py files | null / null | base | OK | — |
| `endPrev` → Nanoparticles | served on all routes | 8462 4.2.4 is chemistry only; the lesson is TF/TH only | WRONG ROUTE (navigation, not science) | The port should make `endPrev` route-dependent: on CF/CH, point to the previous lesson that exists on Combined (metals-alloys). There is no string change in Design's file. |

## 4. Verbatim layer (the repo's four files)
| route | field | finding | change id if any |
|---|---|---|---|
| CF CH TF TH | `quiz` | 2 items, byte-identical in all four files (flag 14). Item 1 (parallel lamps, 6 V) is correct. Item 2 (household wiring) is correct: "full mains voltage … independently". Its wrong-explanation "safety comes from fuses, not lower current" is correct. Nothing is route-inappropriate. | — |
| CF CH TF TH | `fifas` | 1 FIFA (3 Ω + 7 Ω, 20 V). The numbers are correct. On the page it is restructured to the CFIFA rule (Formula as on the sheet), as recorded in NOTES "CFIFA correction". | — |
| CF CH TF TH | `key_note` | "Series: same I, pd splits, R adds. Parallel: same pd, I splits, total R less than smallest. Household = parallel — full voltage, independent. Series break = all stop. Parallel break = others continue." Correct. (The page uses its own `keyLines`.) | — |
| CF CH TF TH | `examiner_tip` | null. The page carries a draft (flag 11). | — |
| CF CH TF TH | `rp` | WRONG: it describes a non-existent "verify the rules" practical and mislabels RP15 as Physics. | C5 |
| CF CH TF TH | `equations` | "Series: R_total = R₁ + R₂ + R₃" etc. These are correct generalisations of the spec. The spec states only two-resistor forms, and three in series is fine. Not served on the page. | — |
| — | `ks4-source.js` theory "SECOMPARISON:" | A typo in the source's theory text. It is not served by the page, so no action. | — |

## 5. Flags decided (from NOTES §9 that touch this lesson)
| flag | decision | spec section |
|---|---|---|
| 11 | NOT approved (Mide's call). Draft text, verbatim: "Before you calculate anything, say which arrangement you are looking at. In series use one current for every component and add the resistances; in parallel use one p.d. for every branch and add the currents. Mixing the two rules is the commonest lost mark." Factual check: both rules are correct. "The commonest lost mark" is an unsupported claim, since no examiner report is cited; it is not a science error. | 8463 4.2.2 |
| 12 | Confirmed. The source misdescribes the practical. The corrected RP text is C5. L13 is correctly *not* built as RP15/RP3, and that practical is still unbuilt in the pilot. | 8464 RP15 / 8463 RP3 (quoted in C5) |
| 13 | Applies here too: RP15 is the 8464 number, and in 8463 the same practical is RP3. C5 names both. | 8463 §8.2.3, 8464 RP15 |
| 14 | Confirmed: 2 quiz items, identical on all four routes. Ladder rungs 2–4 are all new and are examined in §6. | — |
| 15 | Confirmed: there is no parallel-resistance calculation anywhere on the page, bench, CFIFA or ladder. The bench computes branch currents with I = V/R per branch, which is series-style V = IR applied to one component and is permitted. | 4.2.2 "not required to calculate the total resistance of two resistors joined in parallel" |
| 21 | Confirmed against both June 2026 sheets: R_total = R₁ + R₂ is NOT on either. Chip "Not on the sheet · learn it" added (C1). V = I R IS on both sheets, so its "Equation sheet" chip is correct. Note: NOTES §4 says "no physics equation is ever labelled not on the sheet". That holds for the 35 equations in 8463 Appendix/equation list (I counted 35 lines on the 8463 sheet), but R_total = R₁ + R₂ is a spec-printed relationship outside that list, so the ruling stands. | 8463 4.2.2; AQA 8463 equation sheet, June 2026 |
| 22 | Both `EQ_BY_YEAR[2026]` URLs resolve (HTTP 200, application/pdf, 740 921 and 341 050 bytes). Both PDFs are headed "FOR USE IN JUNE 2026 ONLY" even though their filenames contain "2025". **NOTES "Equation sheet link" paragraph is stale**: it says "Both current PDFs say 'for use in June 2025 only'", and they now say June 2026. For this academic year (exams June 2027), AQA has confirmed sheets for 2027, but I found no June 2027 PDF published yet. Add `EQ_BY_YEAR[2027]` and move `EQ_YEAR` when it appears. | AQA news "formulae and equation sheets for 2025–2027" |

## 6. New science introduced by Design (flag 18) — verified?
- Hook scenario (4 Ω + 8 Ω, 12 V; 1 A, 4 V / 8 V): **verified**.
- Bench, 4 changes (the 8 meter-direction verdicts and all `whyI`/`whyV` numbers): **verified**, apart from the wording defects C2 and C3.
- Rules sort, 7 items: **verified**.
- CFIFA worked 2 (6.0 V, 250 mA, R₁ 8.0 Ω → R₂ = 16 Ω): **verified**.
- CFIFA Q1 (5.0 Ω + 15 Ω, 10 V → 0.50 A, 7.5 V): **verified**.
- CFIFA Q2 (400 mA, 12 Ω + 18 Ω → 12 V): **verified**.
- Ladder r2 (800 mA, 6.0 Ω + 9.0 Ω → 12 V, tol 0.05 absolute, unit V): **verified**.
- Ladder r3 chain and herrings: **verified**.
- Ladder r4 6-mark household wiring (levels, 6 points, 1 reject): **verified**. It is AQA-creditable as written.
- Draft examiner tip: factually correct, **not approved** (flag 11).
