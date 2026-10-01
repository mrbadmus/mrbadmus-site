# Science review — batch 2, group chem-a

Reviewer: fresh AQA GCSE science examiner (Opus), 1 Oct 2026. I did not write or examine these lessons.

**Lessons:** atoms-elements-compounds · relative-formula-mass · using-moles-calculations · concentration-of-solutions

**Evidence read**
- For each lesson: the `.dc.html` source, both the template and all of the Component logic.
- The `batch_2.py` records and their `withhold` lists.
- The verbatim route quizzes, key notes, FIFAs and common mistakes in `shared/ks4-source-batch-2.js`.
- The examination and source pack for each lesson.
- The `K.find` / `K.bank` / `K.keyLines` behaviour in `shared/ks4-lib.js`.
- Every built route page, served from `mrbadmus_site/` on :8713. I read the page text in headless Chrome with `prefers-color-scheme: light` forced. In total: 4 + 4 + 2 + 4 = 14 pages.

**Spec basis:** AQA 8462 and 8464 v1.1 statements as quoted verbatim in the batch-2 examination files: 4.1.1.1/5.1.1.1, 4.1.1.2, 4.3.1.1, 4.3.1.2/5.3.1.2, 4.3.2.1–4.3.2.5/5.3.2.1–5.3.2.5, and 8462 4.3.4 (chemistry only, HT only). I re-checked every number on the pages myself.

Row prefixes: **S-n** = required. **A-n** = advisory.

---

## 1. atoms-elements-compounds (AQA 5.1.1.1 / 4.1.1.1 · CF CH TF TH)

### Route-by-route
| route | what renders | check |
|---|---|---|
| CF | All base content: hook, explainer, zoom (6 boxes), sort (10), think, balancer (3 equations), key fact, ladder r1–r4, key note, bank (q1, q4) | OK. Nothing HT, nothing separate-science-only. |
| CH | Same as CF, differing only in the practice-set label | OK. The spec has no HT layer to add here. Ionic and half equations are rightly absent. |
| TF / TH | Same as CF, with the eyebrow and key note reading 4.1.1.1 | OK |

- **Withheld items:** q2 (iron + sulfur, false wx3) and q3 (double-keyed balancing) are absent from all four pages, both in the bank and in the ladder. Confirmed.
- **Ladder:** r1 is frozen q1, which is clean. r2–r4 are authored.

### Checked and correct
- **Hook:** Cl is 35.5 of 58.5, which is 61 %, so "over half the mass is chlorine" is true.
- **Zoom boxes:**
  - CO₂ is 1 : 2.
  - O₂ is an element.
  - He + Ne is a mixture of elements.
  - N₂ + CO₂ has "three types of atom and two kinds of particle".
  - FeS is 1 : 1.
  - Bronze is a mixture. This is consistent with the pilot alloy ruling.
- **Sort:** all ten bins are correct.
- **Think:** every option's reply is true. "H + O → H₂O" does balance on paper, and the reply says so.
- **Worked example and balancer:** the targets are 2Mg + O₂ → 2MgO, N₂ + 3H₂ → 2NH₃ and CH₄ + 2O₂ → CO₂ + 2H₂O. The atom tally logic is right, and the gcd check rejects non-simplest multiples.
- **r2:** 2Na + Cl₂ → 2NaCl. The model and the "…ate contains oxygen" feedback are true.
- **r3:** the chain is not combined → properties kept, proportions variable → physical separation (fractional distillation). Both herrings are false, as intended.
- **r4:** the mark points are verbatim from the examiner draft.

### REQUIRED
| # | lesson · route(s) | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-1 | atoms-elements-compounds · CF CH TF TH | `data-key-fact` block (template, after the command-words block) | OLD: "Reading a particle diagram: more than one kind of particle means a mixture. One kind, with one type of atom, means an element. One kind, with different atoms combined in the same ratio in every particle, means a compound." → NEW: "Reading a particle diagram: an element has only one type of atom. A compound has atoms of two or more elements chemically combined in the same fixed ratio throughout. A mixture has two or more different substances that are not chemically combined with each other." | The OLD rule is false for giant structures. The page's own box 5 (the FeS lattice: two kinds of particle, Fe and S) is a compound, yet the rule calls it a mixture. The same goes for MgO and NaCl, which the page itself sorts as compounds. The key fact is the line pupils memorise, so it must not contradict the activity directly above it. | 4.1.1.1, 4.1.1.2 |

### ADVISORY
| # | where | point |
|---|---|---|
| A-1 | `sortItems` "Gold, Au" `why` | "Gold is listed in the periodic table: one type of atom" is weak reasoning, since the periodic table lists elements, not substances. Better: "One symbol, Au: only gold atoms." |

- **Frozen items still served that should be withheld:** none.
- **Only Mide can rule:** none.

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-1).

---

## 2. relative-formula-mass (AQA 5.3.1.2 / 4.3.1.2 · CF CH TF TH)

### Route-by-route
| route | what renders | check |
|---|---|---|
| CF / TF | <ul><li>Unpacker (CO₂, C₂H₅OH, Mg(OH)₂, Al₂(SO₄)₃).</li><li>Pans (2Mg + O₂; CH₄ + 2O₂), described as "totals balance", which is base.</li><li>% by mass explainer and "Learn it" card, which is base. This is correctly shown to Foundation, as the examination's R5 required.</li><li>CFIFA: H₂SO₄ FIFA, then %Mg in MgO, then 2.0 kg MgO → 1200 g Mg.</li><li>Questions: %Ca in CaCO₃ = 40 %; 0.50 kg CaCO₃ → 200 g Ca.</li><li>Ladder: r1 is q1 (CaCO₃ = 100); r2 is %C in CO₂ = 27.3 %; r3 is the totals chain; r4 is (NH₄)₂SO₄ Mr 132, %N 21.2 %.</li><li>Key note line 4 is rewritten to "The Mr totals on each side of a balanced equation are equal."</li></ul> | OK. The reacting-masses block, the mass-ratio card and the Higher CFIFA tab are all absent, which is correct because 4.3.2.2 is HT. |
| CH / TH | <ul><li>Everything above, plus a HIGHER-badged reacting-mass panel: 6 g Mg → 10 g MgO.</li><li>A mass-ratio "Learn it" card.</li><li>A Higher CFIFA tab: 12 g → 20 g.</li><li>Questions: %N in NH₄NO₃ = 35 %; 3.0 kg Mg → 5000 g MgO.</li><li>r2: 0.50 kg CaCO₃ → 280 g CaO.</li><li>Frozen key-note line "Mr is used to calculate mass ratios in reactions".</li></ul> | OK |

- **Withheld item:** q2, Mg(NO₃)₂ with the self-contradicting wx1, is absent everywhere. Confirmed.
- **Arithmetic re-checked:**
  - 2 × 24 + 32 = 80 = 2 × 40.
  - 16 + 64 = 80 = 44 + 36.
  - Mg(OH)₂ = 58; the bracket-error value is 42.
  - Al₂(SO₄)₃ has 12 O and Mr 342.
  - 6 ÷ 48 × 80 = 10.
  - 12 ÷ 44 = 27.27 %.
  - 500 ÷ 100 × 56 = 280.
  - 3000 ÷ 48 × 80 = 5000.
  - NH₄NO₃ = 80, so N = 35 %.
  - (NH₄)₂SO₄ = 132, so N = 21.2 %; the student's wrong value is 114.
- **Distractor feedback:** every option of the 6 g panel is true.

### REQUIRED
None.

### ADVISORY
| # | where | point |
|---|---|---|
| A-2 | `PANS[0].hint.l` keys 64 and 40 | A reactant total of 64 comes from 2 × 24 + 16, which is taking O₂ as 16. The 64 hint ("O₂ is one molecule here") diagnoses a different error. A total of 40 comes from 24 + 16, which is both one Mg and O as 16. Suggested replacements: 64 → "O₂ has two O atoms: Mᵣ 32, not 16." and 40 → "2Mg is two magnesium atoms (48), and O₂ is 32: 48 + 32 = 80." |
| A-3 | frozen q1 wx1, served on the r1 rung and in the bank on all routes | "CaCO₃ has only ONE oxygen — but…" reads as a false statement. The examination rated it IMPRECISE and usable, and I agree it is not worth withholding. Put it on Mide's list of frozen-text fixes. |
| A-4 | `cfQuestions` Higher | On H routes the Foundation % items (CaCO₃) are replaced, not added to. This is fine, because % by mass is still practised in Q1 (NH₄NO₃) and in the examples. No change needed. Noted only so a later editor does not "restore" the CF items onto H as duplicates. |

- **Frozen items still served that should be withheld:** none.
- **Only Mide can rule:** none.

**Verdict: SCIENCE PASS.**

---

## 3. using-moles-calculations (AQA 5.3.2.3–5.3.2.4 / 4.3.2.3–4.3.2.4, HT only · CH TH)

### Route-by-route
| route | what renders | check |
|---|---|---|
| CH | <ul><li>Hook: 2.4 g Mg + 3.65 g HCl, so HCl is limiting.</li><li>Bench: Mix A gives HCl limiting; Mix B gives Mg limiting.</li><li>Sort: six mixes.</li><li>Balancing-from-masses explainer.</li><li>Think: 2Fe + 3Cl₂ → 2FeCl₃.</li><li>Equations: n = m ÷ Mr; masses → moles → ÷ smallest.</li><li>CFIFA: Mg + 2HCl from masses; 4Na + O₂ → 2Na₂O with kg conversion; FIFA limiting.</li><li>Questions: N₂ + 3H₂ → 2NH₃; H₂/O₂ tank → 2700 g.</li><li>Ladder: definition; 3.6 g Mg + 3.2 g O₂ → 6.0 g; excess-acid chain; Al/Cl₂ 2 : 3 : 2, then 8.9 g.</li><li>Four authored key lines.</li><li>Bank: Na/Cl₂ item only.</li></ul> | OK. No mol/dm³ anywhere: the s-solution panel, the c = n ÷ V card and the c key line are all absent. The withheld KOH q1 is absent from the bank on CH. `K.find` is not used by any rung, so the TH fallback inside `find()` cannot leak the withheld item. |
| TH | The CH content, plus the TRIPLE-badged "Moles in solution · 4.3.4" panel: 25.0 cm³ of 0.100 mol/dm³ gives 0.00250 mol HCl against 0.00200 mol Mg, so HCl is limiting. Also the c = n ÷ V card, key line 5, and the KOH q1 in the bank. | OK. 4.3.4 is chemistry only and HT only, so TH is its correct and only route. |

- **4.3.2.3 is now taught.** The spec point the source pack lacked has two worked examples, two "do" items and r4(a).
- **Arithmetic re-checked:**
  - Bench and sort: every one of the six sort verdicts is correct.
  - Fe/Cl₂: 1 : 1.5 : 1 doubles to 2 : 3 : 2, with 6 Cl on each side.
  - Mg/HCl moles: 0.20 / 0.40 / 0.20 / 0.20.
  - Na/O₂: 40 / 10 / 20, so 4 : 1 : 2.
  - N₂/H₂: 0.10 / 0.30 / 0.20; the Mr(H₂) = 1 error gives 1 : 6 : 2, which does not balance.
  - H₂/O₂ tank: 200 / 75 mol, so O₂ is limiting; 150 mol H₂O is 2700 g; 50 mol H₂ is left over.
  - r2: 0.15 / 0.10 mol, so Mg is limiting and the answer is 6.0 g.
  - r4: 0.20 / 0.30 / 0.20 gives 2 : 3 : 2. Then 0.10 / 0.10 mol, so Cl₂ is limiting. 0.0667 mol × 133.5 = 8.9 g.
  - TH panel: 0.100 × 0.0250 = 0.00250 mol.
- **Feedback:** every distractor reply is true.

### REQUIRED
None.

### ADVISORY
| # | where | point |
|---|---|---|
| A-5 | frozen CH/TH bank item "A student mixes 0.1 mol Na with 0.05 mol Cl₂ … Which is the limiting reactant?" (key "Neither") | The page itself teaches AQA's definition: "the limiting reactant is the one completely used up" (r1, key fact, key line 1). In a stoichiometric mix both reactants are completely used up, so a pupil applying the page's definition would not choose "Neither". The bench handles the same case well, saying "both are used up and neither is in excess". The source examination (C21) judged the key defensible, and I do not think it is outright false. However, it sits in tension with the lesson's own definition. **Recommend withholding it on CH and TH** (a new B2-W row). On CH that leaves the bank empty, so the CH bank would need an authored replacement. This is not a conflict between AQA sources, so it is the commander's call, not Mide's. |
| A-6 | r4 `points[4]`–`[5]` | Rounding to 0.067 mol mid-calculation and then multiplying gives 8.94. The stated 8.9 g is right, but better practice is "0.10 × 2 ÷ 3 = 0.0667 mol" and "0.0667 × 133.5 = 8.9 g". |
| A-7 | `eyebrowLine` (CH) and the key note `keySpec` (CH) | "AQA Chemistry (8464)". 8464 is Combined Science: Trilogy, not a Chemistry specification. Write "AQA Combined Science (8464) 5.3.2.3–5.3.2.4". The same label appears in concentration-of-solutions; see A-9. |
| A-8 | r1 `command: 'State'` | "State" is not in AQA's science command-word list. Use "Give" (or "Define"). The same applies to concentration-of-solutions r1. |

- **Frozen items still served that should be withheld:** possibly the Na/Cl₂ "Neither" item, as advisory (A-5).
- **Only Mide can rule:** none.

**Verdict: SCIENCE PASS.**

---

## 4. concentration-of-solutions (AQA 5.3.2.5 / 4.3.2.5, with 8462 4.3.4 on TH · CF CH TF TH)

### Route-by-route
| route | what renders | check |
|---|---|---|
| CF / TF | <ul><li>Hook: 60 g/dm³ × 0.25 dm³ = 15 g.</li><li>Explainer: g/dm³ only. The g/cm³ unit was correctly dropped.</li><li>Bench: 4 masses × 4 volumes. The dot density is proportional to concentration, and the four options are always distinct.</li><li>Think: 5.0 g in 250 cm³ = 20 g/dm³.</li><li>Convert sort.</li><li>Equations: three g/dm³ forms plus ÷1000.</li><li>CFIFA: 12 g / 0.40 dm³; FIFA 15 g / 500 cm³; 50 g/dm³ × 0.2 dm³.</li><li>Questions: 30 g/dm³ and 40 g/dm³.</li><li>Ladder: ÷1000; 4.0 g / 200 cm³ = 20 g/dm³; the 18 g / 600 cm³ error chain; making 250 cm³ of 20 g/dm³.</li><li>Four key lines.</li><li>Bank: glucose q1.</li></ul> | OK. The HT "explain the relationship" layer (s-pour, dilution, the Explain card, the dilution key line) is absent. No c₁V₁ = c₂V₂, no serial dilution, no mol/dm³. |
| CH | The CF content, plus the HIGHER-badged s-pour block: same bottle means same concentration; dilution 2 g / 0.200 dm³ = 10 g/dm³. Higher CFIFA: volume 0.50 dm³; mass 6.0 g. Higher questions: 10 g; 250 cm³. Higher rungs: 60 × 0.350 = 21 g; A vs B 50 / 25 g/dm³; making 200 cm³ of 35 g/dm³ = 7.0 g. Dilution key line. | OK. No mol/dm³ and no titration, as R8/R9 required. The "standard unit" claim is not present. |
| TH | The CH content, plus the "HIGHER · TRIPLE" s-mol panel: 4.0 g NaOH in 250 cm³ is 0.10 mol, giving 0.40 mol/dm³. Also the c = n ÷ V card and the mol/dm³ key line. | OK |

- **Withheld item:** q2 (80 g/dm³, with the wrong distractor arithmetic and the false wx2) is absent everywhere. Confirmed.
- **Feedback:** every distractor reply in the hook, think, pour, dilute and mol panels is arithmetically and scientifically true. For example, 16 mol/dm³ is the g/dm³ value, and 640 comes from × Mr instead of ÷.

### REQUIRED
None.

### ADVISORY
| # | where | point |
|---|---|---|
| A-9 | `eyebrowLine` / `keySpec` on CF and CH | "AQA Chemistry (8464)" mislabels the Combined specification, as in A-7. Write "AQA Combined Science (8464) 5.3.2.5". |
| A-10 | r4 Foundation and Higher `points[2]` ("Transfer the solution to a … volumetric flask…") | A volumetric flask is not named in 4.3.2.5. The source examination flagged this 4-mark item as an AT 1 practical-context extension. On CF/TF, a pupil who writes "make up to 250 cm³ of solution with distilled water" in a measuring cylinder would, I believe, still be credited at Combined Foundation. As written, the self-marking point withholds the mark. Suggest: "Transfer to a 250 cm³ volumetric flask (or make the total volume of solution up to 250 cm³), rinsing the beaker into it." I am not certain how AQA would credit this, so it is advisory, not required. |
| A-11 | r1 `command: 'State'` | Use "Give", as in A-8. |

- **Frozen items still served that should be withheld:** none. The glucose q1 "dissolved in 500 cm³ of water" wording is imprecise (examination C20) but has no effect on the key, and it remains usable.
- **Only Mide can rule:** none.

**Verdict: SCIENCE PASS.**

---

## Summary
| lesson | REQUIRED | ADVISORY | verdict |
|---|---|---|---|
| atoms-elements-compounds | S-1 | A-1 | **SCIENCE PASS AFTER REQUIRED CHANGES** |
| relative-formula-mass | none | A-2, A-3, A-4 | **SCIENCE PASS** |
| using-moles-calculations | none | A-5 to A-8 | **SCIENCE PASS** |
| concentration-of-solutions | none | A-9 to A-11 | **SCIENCE PASS** |

- **Withholds:** all four lessons' `withhold` entries take effect in `shared/ks4-source-batch-2.js` on every route. No withheld item reaches a rung.
- **Route layers:** every `data-route` layer (`higher`, `triple`, `triple-higher`) renders only on its correct routes in the built pages.
- **Only Mide can rule:** nothing in this group.
