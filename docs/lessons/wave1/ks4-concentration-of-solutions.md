# concentration-of-solutions

Sources: AQA 8464 5.3.2.5 (CF CH) and 8462 4.3.2.5 (TF TH), "Concentration of solutions", read from spec-8464.txt and spec-8462.txt; same wording in both, with one (HT only) line. AQA 8462 4.3.4 "Using concentrations of solutions in mol/dm³" (chemistry only, HT only), so TH only. Rainford SOW lessons "Concentration" (calculate the mass of solute; (H) explain how mass and volume relate to concentration; key words solute, solvent, concentration, decimetre) and SEPS "Determining concentration". LEGACY page (batch 2, Ks4Ladder). 8462 4.3.5 (gas volumes) is not taught here or anywhere.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Many chemical reactions take place in solutions. The concentration of a solution can be measured in mass per given volume of solution, eg grams per dm³ (g/dm³) | Card: What concentration means; Card: cm³ and dm³; Key fact; Rung 1; Quiz Q1, Q3, Q5 | CF CH TF TH | ✓ |
| Calculate the mass of solute in a given volume of solution of known concentration in terms of mass per given volume of solution | Card: The equation (triangle:EQ_CONC); Card: Worked examples (cfifa); Rung 2; Rung 4; Quiz Q2, Q4; Dive deeper: Making up a solution | CF CH TF TH | ✓ |
| (HT only) Explain how the mass of a solute and the volume of a solution is related to the concentration of the solution | Card: Mass, volume and concentration (CH TH); Reveal: Salt solutions (CH TH); Rung 3 (Higher version) | CH TH | ✓ |
| MS 1c, MS 3b: ratios; change the subject of an equation | Card: The equation (triangle); Worked examples (rearranged for mass and for volume) | CF CH TF TH | ✓ |
| 4.3.4: the concentration of a solution can be measured in mol/dm³ | Card: Concentration in mol/dm³ (TH) | TH | ✓ |
| 4.3.4: the amount in moles or the mass of solute in a given volume can be calculated from its concentration in mol/dm³; explain how concentration in mol/dm³ relates to the mass of solute and the volume | Card: Concentration in mol/dm³ (TH): mass to moles with Mr, then ÷ volume; worked 4.0 g NaOH in 250 cm³ = 0.40 mol/dm³ | TH | ✓ |
| 4.3.4: if the volumes of two solutions that react completely are known and one concentration is known, the other can be calculated | Not taught here: it is the titration calculation (8462 4.4.2.5, the Titrations lesson). Listed as a gap for the lead to confirm. | TH | gap |
| (SOW) solute, solvent | Card: What concentration means | CF CH TF TH | ✓ |

**Gaps and mismatches.** The old generator text taught concentration in g/cm³ "at Foundation level", the dilution formula c₁V₁ = c₂V₂ and serial dilution; none of these is in 5.3.2.5 / 4.3.2.5, and they are removed. Its CH data also carried mol/dm³ and titration calculations, which are chemistry only, so they were wrong on Combined Higher; mol/dm³ is now on TH only. The 4.3.4 titration-volume line (above) is not on this page.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list. Fixes are in quiz-concentration-of-solutions.json (two old questions, identical on every route, plus three new ones, identical on every route).

**Ladder.** Ks4Ladder, one item per rung. Rungs 2, 3 and 4 are tier-split in the logic (`H ?`) under one id each. Rung 2 and Rung 4 test all-tier content on both tiers. Rung 3's Higher version (two solutions, equally concentrated) tests this lesson's own HT line and is shown on Higher routes only; kept, and flagged in case the lead wants every rung identical across tiers.

**Equation.** The record adds EQ_CONC (concentration = mass of solute ÷ volume of solution; m on top, c and V below; units g, g/dm³, dm³) and places its triangle with `triangle:EQ_CONC`. The spec gives the relation in words only ("mass per given volume of solution"); AQA writes no formula for it. The logic returns `Object.assign({}, R, {` once, so the builder adds LEAN_PROPS as it does for power.

**Audit of the ladder, worked examples and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 cm³ to dm³ | ok |
| Rung 2 Foundation: 4.0 g in 200 cm³ | ok (20 g/dm³) |
| Rung 2 Higher: 60 g/dm³, 350 cm³ | ok (21 g) |
| Rung 3 Foundation chain: 18 ÷ 600 slip | Fault: links 1 (the rule) and 2 (the conversion and the slip) could be read in either order. Fix (logic_edits): link 2 now starts "So the 600 cm³ must be divided by 1000 to give 0.6 dm³. The student divided by 600 instead." Link 3 uses that 0.6. One forced order. |
| Rung 3 Higher chain: 6.0 g in 150 cm³ against 10 g in 250 cm³ | ok (both 40 g/dm³). One forced order: convert, then calculate both, then conclude. |
| Rung 4 Foundation: make 250 cm³ at 20 g/dm³ | ok (5.0 g) |
| Rung 4 Higher: make 200 cm³ at 35 g/dm³ | ok (7.0 g) |
| CFIFA Foundation example 1: 12 g in 0.40 dm³ | ok (30 g/dm³) |
| CFIFA example 2 (old fifa): 15 g NaOH in 500 cm³ | ok (30 g/dm³) |
| CFIFA Foundation example 3: 50 g/dm³, 200 cm³ | ok (10 g) |
| CFIFA Higher example 1: 8.0 g at 16 g/dm³ | ok (0.50 dm³) |
| CFIFA Higher example 3: 40 g/dm³, 150 cm³ | ok (6.0 g) |
| CFIFA Foundation Q1, Q2 | ok (36 g/dm³; 40 g/dm³) |
| CFIFA Higher Q1, Q2 | ok (10 g; 0.25 dm³ = 250 cm³) |
| Quiz Q1 25 g glucose | Answer ok (50 g/dm³). Fault: "dissolved in 500 cm³ of water". Concentration uses the volume of solution, and the spec says so. Fix: "25 g of glucose is dissolved in water to make 500 cm³ of solution. What is the concentration in g/dm³?" Options kept; feedback rewritten plainly. NEW ID. |
| Quiz Q2 80 g/dm³, 250 cm³ (kept) | ok (20 g) |
| Quiz Q3 250 cm³ in dm³ (new) | ok |
| Quiz Q4 40 g/dm³, 0.5 dm³ (new) | ok (20 g) |
| Quiz Q5 Highest concentration (new) | ok (100, 20, 25, 20 g/dm³) |

**Removed or moved.**
- Removed: the solution bench animation (now the cm³ and dm³ card and the worked examples); the Think again on 5.0 ÷ 250 (now an Easy mistake); the Convert-first Sort (now the cm³ and dm³ card); the Higher pour and dilute choices (now Mass, volume and concentration and the Salt solutions reveal, CH TH); the TH mol/dm³ choice (now the Concentration in mol/dm³ card, TH); the equations panel (now The equation card and its triangle); the Key note; the video; the command words (now Dive deeper).
- Not kept: `benchFig` (animation-driven, and its div has `max-width: 420px`, so it is not the builder's figure div); `pourFig` (static and correct, but passed as `figure-svg` to a Ks4Choice, not drawn in a figure div, so the builder cannot place it; see Figures wanted).
- Moved to Dive deeper: volume of solution, not of water; making up a solution (from Rung 4's mark points); command words.
- Key changes: none beyond the new id below (Q1's options are unchanged, but their keys hash the new stem).
- New id (stem changed): Quiz Q1.
- Rung prompts reworded, position kept (id kept): concentration-of-solutions#r3 (Foundation links only).

**Words.** Old Design page prose about 580 (old generator theory 329). New knowledge + key fact + Dive deeper about 546.

**Fixes after the examiner and blind checks (13 Nov).** EX = EXAMINER.md item; BLIND = blind pass. Where this list and the tables above disagree, this list is current.
- EX SHOULD 1: "Volume of solution, not of water" and "Making up a solution" moved from Dive deeper into Key knowledge, just before Easy mistakes, so Rung 4's mark points are taught in Key knowledge. Same text.
- EX SHOULD 2: practice Q2 (kept) wrong_explanations rewritten without dashes, every route. Stem and options unchanged.
- EX SHOULD 3: the TH card "Concentration in mol/dm³" adds the reverse direction of 4.3.4: amount (mol) = concentration (mol/dm³) × volume of solution (dm³), then × Mr for the mass.
