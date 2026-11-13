# transformers

Sources: AQA spec 4.7.3.4 (physics only, HT only) and 4.2.4.3 The National Grid, read from the 8463 PDF. Rainford KS4 Physics Unit 7 lesson "Transformers". Route: TH only. The old data's spec field says "6.7.3.4"; the real AQA 8463 number is 4.7.3.4, and there is no 6.7.3 in the Combined spec (8464 section 6.7 stops at 6.7.2.3).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| A basic transformer consists of a primary coil and a secondary coil wound on an iron core | Card: What a transformer is (fig:transformer); Rung 4 | TH | ✓ |
| Iron is used as it is easily magnetised | Card: What a transformer is; Rung 1 | TH | ✓ |
| Knowledge of laminations and eddy currents is not required | Not taught anywhere on the page | TH | ✓ |
| The ratio of the p.d.s across the coils depends on the ratio of the number of turns on each coil | Card: The p.d.s and the turns | TH | ✓ |
| Vp / Vs = np / ns; apply (on the Physics equation sheet); p.d. in volts | Card: The p.d.s and the turns; Worked examples (Step 1); Rung 2 | TH | ✓ |
| Step-up: Vs > Vp. Step-down: Vs < Vp | Reveal: Step-up and step-down; Start here; Rung 1 | TH | ✓ |
| If transformers were 100% efficient, the electrical power output would equal the electrical power input | Card: Power in and power out | TH | ✓ |
| Vs × Is = Vp × Ip; Vs × Is is the power output (secondary), Vp × Ip the power input (primary), in watts; apply (on the sheet) | Card: Power in and power out; Worked examples (Step 2, Current from the supply); Rung 2 | TH | ✓ |
| Explain how an alternating current in one coil inducing a current in another is used in transformers | Card: How it works; Key fact; Rung 3; Rung 4 | TH | ✓ |
| Explain how the ratio of the p.d.s depends on the ratio of the turns | Card: The p.d.s and the turns; Reveal: Step-up and step-down; Dive deeper: A quick check | TH | ✓ |
| Calculate the current drawn from the input supply to provide a particular power output | Worked examples: Current from the supply; Rung 2 (second calc) | TH | ✓ |
| Apply the equations to the currents and power transfer, and relate these to the advantages of transmission at high p.d. | Card: Why the National Grid uses a high p.d.; Rung 3; Rung 4 | TH | ✓ |
| 4.2.4.3: step-up transformers increase the p.d. from the power station to the transmission cables; step-down transformers decrease it, to a much lower value, for domestic use; the National Grid is an efficient way to transfer energy | Card: Why the National Grid uses a high p.d. | TH | ✓ |
| Maths: rearrangement and unit conversion (MS 1c, 3b, 3c) | Worked examples (kV to V in Step 1; rearrangement noted on every Fine-tune line); Rung 2 (kV to V, mA to A) | TH | ✓ |

**Triangles.** No formula triangle. Vp / Vs = np / ns and Vs × Is = Vp × Ip each have four quantities, so neither fits a three-cell triangle. Both are in `equations` with `source: "sheet"` and no top/bottom, and no `triangle:` slot is placed. The three CFIFA examples carry `"eq": "null"`: `lean_ks4._example_js` writes an eq name it does not find in `equations` straight into the JS, so this becomes `eq: null` and the Formula step draws no triangle. Do not change it to Python `None`, which would print `eq: None` into the page's JS.

**Gaps and mismatches.** The old page had no example of the current drawn from the supply, no unit conversion and no rearrangement for Vp/Vs. It wrote the turns equation upside down from AQA's form (Vs/Vp = Ns/Np, capital N); the record uses AQA's Vp / Vs = np / ns. It never said "iron is used as it is easily magnetised".

**Removed or moved.** Removed: eddy currents, laminated cores, "soft iron", flux leakage (the spec says laminations and eddy currents are not required). Removed: "magnetic flux", "emf", "Faraday's law", "mutual induction". Removed: the grid voltage chain (25 kV, 400 kV, 33 kV, 11 kV) as a list to learn; 25 kV and 400 kV appear only as numbers in a worked example. Removed: "~95–99% efficient". Moved to Dive deeper: a quick turns-ratio check; real transformers are not 100% efficient. Removed: the matching activity. Quiz: Q1 "Why can't transformers work with direct current (DC)?": **question wording kept exactly (the draft's rewording is undone), so its quiz ID is unchanged**; marked "fixed" because the options and feedback were rewritten: its right option rested on "constant magnetic flux", "emf" and "Faraday's law" and was the longest option. The stem itself is accurate and has none of those words. Q2 "Why does the National Grid transmit electricity at very high voltages?": **question wording kept exactly, ID unchanged**; marked "fixed": the credited option was visibly the longest, with dash tails, "power wasted as heat" and "P_loss = I²R" in code style. It now reads "The current is smaller, so cables heat less". Q3, Q4 and Q5: new.
