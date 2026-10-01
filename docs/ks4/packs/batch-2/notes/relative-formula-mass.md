# relative-formula-mass — lesson notes (batch-2, draft)

## Lesson record

```python
dict(slug="relative-formula-mass",
     source_file="relative-formula-mass.dc.html",
     subject="chemistry", topic_id="quantitative",
     title="Relative Formula Mass",
     spec="5.3.1.2", family="Quantitative", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2")
```

Spec: 8464 5.3.1.2 / 8462 4.3.1.2 (base). The HT layer is 4.3.2.2 (reacting masses from equations, HT only). The eyebrow and key-note chip read `5.3.1.2` on Combined routes and `4.3.1.2` on Triple routes.

## Family: QUANTITATIVE, and why

The concept is a calculation: Mr is a sum, and percentage by mass and reacting masses follow from it. The flagship makes the count-and-add visible, then feeds straight into CFIFA.

The line-up differs from the pilot's QUANTITATIVE lesson (nanoparticles). Here it is: hook, unpacker with an in-instrument confront, pans, a Higher layer, the equation block, CFIFA, the ladder. Nanoparticles has a size sort, a cube splitter, a spot-the-flaw and an evaluate Write.

## Instruments and the demand each one trains

| scale | instrument | demand |
|---|---|---|
| L (flagship) | **Formula unpacker** (`#s-unpack`). Four formulas in rising difficulty: CO₂, C₂H₅OH, Mg(OH)₂ and Al₂(SO₄)₃. The pupil first commits to how many atoms of a target element are present. The distractors are the named counting errors: the subscript applied to the wrong atom; the H in OH missed; the bracket multiplier applied to H only, or to O twice; 4 + 3 instead of 3 × 4. Only after the commit does the formula unpack, animated. Atoms pop out in sequence, with bracketed groups drawn as boxed copies. Each atom's Ar grows a bar segment along one fixed 0–350 scale until it reaches Mr. A tally (element · n × Ar = …, then Mr = …) follows. | Count atoms in a formula and sum Ar (the 4.3.1.2 skill), with the bracket rule made visible. |
| M | **Load the pans** (`#s-pans`). Two balanced equations: 2Mg + O₂ → 2MgO, and CH₄ + 2O₂ → CO₂ + 2H₂O. The pupil predicts which pan is heavier, then types both totals, then presses "Load the pans". The formula-unit blocks drop onto the reactant pan, which dips; the products drop onto the other pan and the beam returns level. Feedback names the specific error for common wrong totals: a coefficient ignored, O₂ counted as 16, Mr(2H₂O) given as 18 or 36. | Show that the totals of Mr × coefficient on the two sides are equal (base 4.3.1.2), by producing the totals. |
| micro, **Higher** | Inside `#s-pans`, a `data-route="higher"` card: the 48 : 32 : 80 mass ratio (from th3), then a graded `Ks4Choice`, "6 g of Mg → ? g MgO". The distractors are 6 g (oxygen's mass forgotten), 5 g (the coefficient missed on MgO) and 20 g (the wrong scale). | Apply the HT reacting-mass ratio. |
| CFIFA | Worked examples: (1) the **verbatim** source FIFA (H₂SO₄ = 98) with "Nothing to convert: Ar values have no units." in front; (2) % Mg in MgO = 60 %, nothing to convert; (3) the mass of Mg in 2.0 kg of MgO, converting kg → g, = 1200 g, the examination's suggested convert example; (4) on Higher only, the th3 reacting-mass example, 12 g Mg → 20 g MgO. Write-it-out attempts differ by tier, and each opens with the convert decision. **Foundation:** % Ca in CaCO₃ = 40 %; the mass of Ca in 0.50 kg of CaCO₃ = 200 g (kg → g). **Higher:** % N in NH₄NO₃ = 35 %; the MgO from 3.0 kg of Mg, in grams = 5000 g (kg → g, HT method). | Watch then do (Law 5); tiers really differ (content standards §2). |
| micro | Hook `Ks4Choice` (unscored): H₂O (3 atoms) against O₂ (2 atoms). | Commitment; confronts "more atoms means more mass". |

## Misconceptions and where each is confronted

1. **Brackets: multiplying only the atom next to the subscript.** Confronted head-on inside the flagship at Mg(OH)₂, where an amber three-beat panel is always shown. The beats are: the quote; why it is wrong (the bracket's 2 belongs to the whole group; counting it on H gives 42, not 58); and the verbatim `common_mistake` as the correct version (Ca(OH)₂ = 74). It is also confronted in rung 4 ((NH₄)₂SO₄ given as 114).
2. **A coefficient changes Mr** (2H₂O treated as Mr 36, or 2MgO as Mr 80). Confronted in the explainer before the pans, in the pans' error feedback, and in a rung 3 herring.
3. **Diatomic Mr** (O₂ taken as 16). Confronted in the pans feedback.
4. **More atoms means more mass.** Confronted by the hook.
5. **Percentage by mass ignores the number of atoms** (H in water as 1/18). Confronted in the % explainer, the closing note of Higher Q1, and the rung 4 reject list.
6. **Mass lost or made in a reaction.** Confronted in the Higher choice's 6 g reply and a rung 3 herring.

## Route tags (spec-cited)

| content | tag | citation |
|---|---|---|
| Mr = sum of Ar; brackets; totals on each side of a balanced equation are equal | base | 4.3.1.2 (no HT marker) |
| Percentage by mass of an element in a compound | **base**, taught to every route | 4.3.1.2: "calculate the percentage by mass…". The examination's R5 says the old copies withheld this from CF/TF. |
| Reacting masses: the 48 g : 32 g : 80 g ratio, scaling from a given mass | **higher** (`data-route="higher"` on the pans card and on the "mass ratio" equation card; `R.isHigher` selects the 4th worked example, the Higher CFIFA questions and the Higher r2) | 4.3.2.2 (HT only); examination R4 |
| Key-note clause "Mr is used to calculate mass ratios in reactions." | Shown on CH/TH. On CF/TF the line is swapped in logic for "The Mr totals on each side of a balanced equation are equal.", per examination C12. | 4.3.2.2 vs 4.3.1.2 |
| Empirical and molecular formula (frozen `higher` field) | **not taught.** Empirical formula belongs to `using-moles-calculations`; molecular formula is not in the spec (examination R6/R7). | 4.3.2.3; — |
| Carbon-12 | not taught | examination R8 |

## ⚑ Net-new science-bearing items

- ⚑ Hook text, options and reveal (H₂O 18 against O₂ 32).
- ⚑ The Ar list shown (H 1, C 12, N 14, O 16, Mg 24, Al 27, S 32, Ca 40), which matches the AQA data sheet. Al = 27 is added, per examination C5.
- ⚑ The four unpacker formulas and their counts. Mr values: CO₂ 44, C₂H₅OH 46, Mg(OH)₂ 58, Al₂(SO₄)₃ 342. The wrong-count replies and the confront's 42 (24 + 16 + 2) are also new.
- ⚑ The pans' totals (80 = 80 for both equations) and the feedback lines.
- ⚑ The Higher micro: 6 g Mg → 10 g MgO. Distractor arithmetic: 6 g; 5 g = 6 ÷ 48 × 40; 20 g.
- ⚑ Every CFIFA example and question except the verbatim H₂SO₄ FIFA. Values: 60 %; 1200 g; 40 %; 200 g; 35 %; 5000 g (3000 ÷ 48 = 62.5, × 80). The 12 g → 20 g Higher example uses th3's own numbers.
- ⚑ The equation cards. "% by mass = (Ar × number of atoms of that element) ÷ Mr × 100" and "mass ratio = ratio of (number in front × Mr)" are written from the spec. The Mr card shows the verbatim `equations[0]`.
- ⚑ Ladder r2. **Foundation:** % C in CO₂ = 27.3 % (3 s.f.), tolerance ±0.06. **Higher:** the CaO from 0.50 kg of CaCO₃ = 280 g (Mr 100 → 56), kg → g, tolerance ±1.
- ⚑ The r3 chain (atoms conserved → same atoms on each side → same Ar sum = 80).
- ⚑ Rung 4: (NH₄)₂SO₄, the student's 114 against the correct 132, and % N = 21.2 %. The marking points and rejects are new.
- ⚑ The command-word definitions and the key fact (% by mass, with MgO 60 % as the example).

## Frozen items flagged wrong, and how they are handled

- **q2 (Mg(NO₃)₂, all routes).** wx1 contradicts itself ("1 N, NOT 2 — wait:"). It is kept verbatim in the practice bank, never a rung and never quoted. The bracket skill it tests is trained by the unpacker, by CFIFA and by rung 4 instead.
- **q1 (CaCO₃).** wx1 is imprecise (C19) but not false. It is used as **rung 1**, command "Calculate", 1 mark. It is the only clean verbatim item, and its needle `'relative formula mass of calcium carbonate'` exists in all four route copies. The examination suggested q1 as an apply item. The pilot's rung 1 is always a verbatim MCQ, and a 1-mark MCQ calculation is an AQA-style recall-tier item, so it sits at rung 1 and rung 2 is a fresh CFIFA calculation.

## Other

- **Exam tip slot:** omitted. The subtopic has no `examiner_tip`.
- **New instruments or helpers:** the unpacker and the pans are built inside the lesson's own Component logic, with namespaced `rfm-*` keyframes in the helmet. No `_ext` file. Reduced motion shows the end state instantly: the resting inline state is the final layout.
- **Connects:** `atoms-elements-compounds` and `using-moles-calculations` via `KS4.hrefFor`, with nulls filtered out.
- **Body prose:** hook 31 words; explainers 105, 59 and 52 words; Higher card 63 words. Total 310 words. Every block is at most 150 words before a commitment.
- **Self-check:** I rendered the lesson on all four routes in headless Chrome, on the pilot runtime with a scratch source file. Results: 0 console errors, no `undefined`/`NaN`/`{{`, and scrollWidth of 390 at 390 px. A drive confirmed the unpacker's confront appears at Mg(OH)₂ only, the pans' error feedback fires, the key note swaps line 4 on CF/TF only, and the Higher CFIFA tab appears on CH/TH only. The standalone runtime does not strip `data-route`, so the HT card shows on every route there; the build's `apply_route_layers` handles it. `build_ks4.py --batch batch-2` was not run, because no batch-2 module is registered.
- One harness note: `ks3_browser.Page.goto` timed out waiting for `loadEventFired` on this page under `support.js`, although `document.readyState` was `complete` within 2 s. I drove it with `Page.navigate` and a fixed wait instead. The cause is in the test harness, not the lesson.

## Review fixes (1 Oct 2026)

From `review/science-chem-a.md` (no required rows; A-2…A-4) and `review/quality-b.md` (Q-1…Q-4, A-1…A-3):

- **Science A-2.** Pan 1 hints corrected. A reactant total of 64 now gets "O₂ has two O atoms: Mᵣ 32, not 16." A total of 40 now gets "2Mg is two magnesium atoms (48), and O₂ is 32: 48 + 32 = 80."
- **Science A-3.** Not applied: it is a frozen-text fix (q1 wx1) for Mide's list. q1 stays as rung 1.
- **Science A-4.** No change: noted so the Foundation % items are not later duplicated onto Higher.
- **Q-1.** Eyebrows are now `The formula unpacker` and `Load the pans`. `upStep` and `panStep` are deleted.
- **Q-2.** The confront panel's verbatim `common_mistake` paragraph is deleted, along with `cmText`. The panel keeps its three beats: the quote, why it is wrong (42, not 58), and the tally beside it as the correct count.
- **Q-3.** Key fact is now the reviewer's bracket-rule text word for word ("A number after a bracket multiplies everything inside it: Mg(OH)₂ is one Mg, two O and two H, Mᵣ = 58. Mᵣ has no units.").
- **Q-4.** Added the route chip, copied from `using-moles-calculations.dc.html`. Eyebrow is now `AQA Chemistry ({{ specCode }}) {{ specRef }} · Quantitative`, with 8464 on Combined and 8462 on Triple.
- **Quality A-1.** Not applied. q1 (CaCO₃) is the only clean verbatim quiz item. q2 is withheld for its self-contradicting wx1, and the H₂SO₄ item is a FIFA, not a quiz item. Repeating Mᵣ(CaCO₃) after CFIFA Q1 is accepted.
- **Quality A-2.** Not applied. The bar's "Mᵣ = 342" label is the moment the animation lands, and the tally line adds the sum it came from, so I judged both worth keeping.
- **Quality A-3.** Not applied. The subscript glyphs come from Georgia's own Unicode subscript digits, which is the pilot diagram engine's convention (`ks4-diagrams.js` `T()`). Changing it needs a shared helper.
- **"State" → "Give".** Nothing to change: no chip on this lesson read "State".
- **Validation.** Re-run in scratch on all four routes: 0 console errors, no undefined/NaN/`{{`, scrollWidth 390. The new 64 hint fires. The key fact and eyebrows are as above.
