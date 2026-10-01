# using-moles-calculations — author notes (batch-2)

## Lesson record

```python
dict(slug="using-moles-calculations",
     source_file="using-moles-calculations.dc.html",
     subject="chemistry", topic_id="quantitative",
     title="Using Moles — Calculations and Limiting Reactants",
     spec="5.3.2.3–5.3.2.4",  # 8464 5.3.2.3–5.3.2.4 / 8462 4.3.2.3–4.3.2.4 (HT only); TH layer touches 8462 4.3.4
     family="Quantitative", routes=["CH", "TH"],
     review_state="draft", batch="batch-2",
     # s-bench: bespoke instrument, no dc-import. s-solution: data-route
     # section whose only import is Ks4Choice (the classifier cannot type it).
     block_map={"s-bench": "figure", "s-solution": "check"})
```

The whole lesson is HT only, so it ships on CH and TH and nothing in it carries a `higher` tag. The eyebrow and key-note spec are worked out in logic: `(8464) 5.3.2.3–5.3.2.4` on CH, `(8462) 4.3.2.3–4.3.2.4` on TH, and the key note on TH adds 4.3.4.

## Family and why

**QUANTITATIVE.** Both spec points are calculations that carry the concept:

- 4.3.2.3: masses → moles → whole-number ratio = balancing numbers.
- 4.3.2.4: moles compared with the equation ratio decide the limiting reactant and the amount of product.

The flagship is a simulation that feeds straight into CFIFA.

## Activities and the demand each trains

| block | size | demand |
|---|---|---|
| Hook (Ks4Choice, ungraded) | micro | **Predict.** 2.4 g Mg + 3.65 g HCl (the source FIFA's own numbers): which runs out? The options are the three wrong ideas (smaller mass; equal moles so both together; gas escaping stops it) and the right reason. The reveal is the verbatim th2 working. |
| **s-bench, "The reaction bench"** (flagship, new instrument) | L | **Determine, predict-gated, animated.** Counters of 0.01 mol, with HCl always in pairs so every step is whole. Mix A (0.08 Mg / 0.12 HCl) is the "fewer moles" trap: Mg has fewer moles but HCl runs out. Mix B (0.06 / 0.16): Mg limiting. "Your mix" has −/+ steppers. The pupil commits to "Mg runs out / HCl runs out / both together", then watches the reaction step by step: one Mg and two HCl slide to the arrow and become one MgCl₂ and one H₂, until one reactant is gone. The readout gives reactions, mol and g of H₂, and the excess left over. Feedback is computed from the numbers; the trap pick gets "Fewer moles is not the test." first. Reduced motion: an instant end state. Real buttons; the controls lock during the run. Done when Mix A and Mix B have both been run. |
| s-sort (Ks4Sort, 2 bins) | M | **Determine at speed.** Six mixes, four in mol and two in g (needing ÷Ar or ÷Mr first). Each must be placed under "Mg limiting" or "HCl limiting". The bins are balanced 3/3, and one card is the fewer-moles trap. No word-shape solving: every card is the same template with different numbers. |
| s-think (Ks4Choice, graded, spot the flaw) | micro | **Balance.** The ratio 1 : 1.5 : 1 for Fe + Cl₂ → FeCl₃, where the misconception is "round 1.5 to 2". Every distractor is a named slip: round up, round down, or leave a fractional coefficient. |
| s-solution (triple) | micro | **Determine in solution.** n = c × V for 25.0 cm³ of 0.100 mol/dm³ HCl against 0.00200 mol Mg. The distractors are fewer-moles, no cm³ conversion (2.5 mol), and "close enough". |
| s-calc (Ks4Cfifa) | worked pair | Balancing and limiting reactant in one CFIFA (below). |
| Ladder | 4 rungs | ① State (1) ② Calculate (3, with a Convert choice) ③ Explain chain (3) ④ Calculate / determine (6, six marking points) |

### CFIFA

**Worked examples:**
1. **Balance, nothing to convert.** The examiner's checked Mg + HCl example: 0.20 / 0.40 / 0.20 / 0.20 → 1 : 2 : 1 : 1, with a mass check.
2. **Balance, convert first.** The examiner's checked Na / O₂ example in kg → g: 40 / 10 / 20 → 4Na + O₂ → 2Na₂O, with a mass check.
3. **Limiting reactant.** The source FIFA, its four steps verbatim, with "Nothing to convert: masses are already in grams." in front (the examiner's own C24 wording).

**Write-it-out:**
- **Q1 (nothing to convert) ⚑.** N₂ 2.8 g, H₂ 0.6 g, NH₃ 3.4 g → 0.10 / 0.30 / 0.20 → N₂ + 3H₂ → 2NH₃. The mass check closes: 2.8 + 0.6 = 3.4. The closing line names the Mr(H₂) = 1 slip.
- **Q2 (convert kg → g) ⚑.** 2H₂ + O₂ → 2H₂O with 0.40 kg H₂ and 2.4 kg O₂: H₂ 200 mol, O₂ 75 mol. 200 mol of H₂ needs 100 mol of O₂, so O₂ is limiting. That gives 150 mol of H₂O = 2700 g (2.7 kg). Check: O₂ 2400 g + H₂ used 300 g = 2700 g. The close: hydrogen has the smaller mass yet is in excess, with 50 mol left over.

The lesson ships on Higher only, so there is no Foundation/Higher split in numbers. Every example is at Higher demand: unit conversion, a two-step chain, and ratio handling.

### Ladder

- **r1 (authored ⚑).** State what is meant by the limiting reactant. The key uses the spec's own words, "completely used up". The distractors are smallest mass, fewest moles, and "left over" (that is the excess). The replies point back to the hook and to Mix A.
  - It is authored rather than `K.find`, because the bank has two items: q1 is wrong on CH, and the examiner says q2 should not be rung 1 or 2. There is no `K.find` in r1, so `check_rung1_fallback` has no needles.
- **r2 ⚑.** 2Mg + O₂ → 2MgO with 3.6 g Mg and 3.2 g O₂. That is 0.15 mol and 0.10 mol, and Mg needs only 0.075 mol of O₂, so Mg is limiting. n(MgO) = 0.15 mol, mass 6.0 g. Mass check: 3.6 + 2.4 = 6.0 ✓. The Convert choice is "nothing to convert". The unit options include mol and g/mol.
- **r3.** The examiner-drafted 3-mark "Explain why an excess of acid is used", built as a chain with two herrings: "the excess limits", and "excess makes more than the equation allows".
- **r4 ⚑ (6 marks).** This follows the examiner's steer: "determine the balanced equation, then the limiting reactant".
  - (a) Al 5.4 g, Cl₂ 21.3 g, AlCl₃ 26.7 g → 0.20 / 0.30 / 0.20 → 2Al + 3Cl₂ → 2AlCl₃ (mass check 26.7 ✓).
  - (b) 2.7 g Al and 7.1 g Cl₂ → 0.10 / 0.10. Al needs 0.15 mol of Cl₂, so Cl₂ is limiting. n(AlCl₃) = 0.10 × 2 ÷ 3 = 0.067 mol, which is 8.9 g (exactly 26.7 ÷ 3).
  - Six marking points, one mark each, and two "do not accept" lines (a fractional coefficient; limiting judged by mass).

## Misconceptions and where each is confronted

1. **"The limiting reactant is the one with the smaller mass" (this is the pack's own common_mistake).**
   - The hook: Mg is the smaller mass and is in excess.
   - The CFIFA Q2 close; the r1 distractor; the r4 reject line.
2. **"…the one with fewer moles."** Mix A on the bench is where it is born and confronted: the predict trap, then "Fewer moles is not the test", the computed reason, and the correct conclusion, which together are the three beats. Also the s-sort trap card, the s-solution distractor, and the r1 distractor.
3. **"The reactant in excess limits the product."** The r1 "left over" distractor and the r3 herring.
4. **"Equal moles means both run out together" (ignoring the ratio).** The hook option and the bench's "both together" option (correct only for an exactly matched "Your mix").
5. **Using masses directly as balancing numbers.** The balancing explainer, and the CFIFA working (masses → moles every time).
6. **Rounding 1.5 to 2, or not dividing by the smallest.** s-think (three beats: the quote, why it is wrong, and the correct version via doubling); the r4 reject line.
7. **Mr(H) = 1 for H₂, and likewise O₂ and Cl₂.** The balancing explainer; the CFIFA Q1 close; the Mr notes in the worked examples.
8. **Ignoring the coefficient when converting moles of product.** The source FIFA (n(H₂) = n(HCl) ÷ 2), CFIFA Q2 (×2), and r4 (× 2 ÷ 3).
9. **TH only: no cm³ → dm³ conversion in n = c × V.** The s-solution distractor "2.5 mol".

## Route tags (every one)

| element | tag | citation |
|---|---|---|
| `#s-solution` section (mol/dm³, n = c × V, a limiting reactant in solution) | `triple` (CH/TH lesson, so TH only) | 8462 4.3.4 "Using concentrations of solutions in mol/dm³ (chemistry only) (HT only)"; absent from 8464. On this lesson `triple` means TH, as the commander directed. |
| equation card c = n ÷ V | `triple` | 8462 4.3.4 |

In logic: the key-note line "c (mol/dm³) = n ÷ V" shows on Triple only; the eyebrow and key-note spec switch 8464/8462.

Everything else is `higher` by virtue of the lesson: 4.3.2.3 and 4.3.2.4 are both "(HT only)" in 8464 and 8462, so no inline tag is needed.

## ⚑ Net-new science-bearing items

- Hook option replies.
- The explainer re-cut: the limiting/excess definitions follow the spec 4.3.2.4 wording, and "chemists often use an excess…" is spec text. The balancing explainer follows spec 4.3.2.3.
- The bench model, its computed feedback, and the legal line.
- The s-sort cards (the arithmetic of all six was checked).
- The s-think Fe/Cl₂ ratio item.
- The s-solution explainer (from verbatim th1 numbers: 100 cm³ × 2 mol/dm³ = 0.2 mol) and its item: n(HCl) = 0.00250, needed 0.00400.
- CFIFA Q1 and Q2; ladder r1, r2 and r4 (r3 is examiner-drafted).
- The command-word cards, the key fact, and the key-note re-wording (see below).
- The two balancing worked examples are the examiner's own checked examples (examination §5), used as given.

## Frozen items flagged wrong, and how they are handled

- **q1** ("0.3 mol KOH in 300 cm³ of water", mol/dm³). This is chemistry-only HT content (8462 4.3.4), so it is **wrong for CH**.
  - It is **kept verbatim in the practice bank** (`K.bank` serves it on both routes; the brief says frozen items stay untouched in the bank). It is **never a ladder rung or body item on CH.**
  - It is not used as a rung on TH either. The r2 slot is a CFIFA input rung, so the page trains production, and q1's "of water" wording (C18) is imprecise.
- **q2** (0.1 mol Na + 0.05 mol Cl₂, "Neither"). The route is right, but it is a stoichiometric boundary case, and the option 1 text versus wx1 mismatch is IMPRECISE (C22).
  - **Kept verbatim in the bank. Not a rung,** per the examiner. The idea it tests ("both used up exactly") is reachable honestly on the bench's "Your mix".
- **Not displayed:**
  - The th3 heading "Using Moles to Balance Equations" over empirical/molecular formula (C7): **wrong; not displayed**. 4.3.2.3 is taught new, from the examiner's worked examples.
  - Molecular formula (R6 / C9): **NOT-IN-SPEC; cut**. Empirical formula is not taught as a term (R5).
  - Matching item 4 (C17, self-contradicting) and the rest of the matching: **replaced** by s-sort.
  - th1's mol/dm³ and titration content (R1/R2): mol/dm³ is kept **TH-only** (`triple`). The titration worked calculation is **left to `titrations`**, which the examiner names as its home, and is linked from connects where that page exists. C4's sig-fig note therefore does not arise here.
- **Key note re-worded.** "…whichever runs out first limits yield" became "…limits the amount of product" (C12: "yield" is chemistry-only, 4.3.3.1; the spec wording is used). The molecular-formula clause is cut. The empirical clause is re-aimed at balancing: "masses → moles → divide by the smallest → simplest whole-number ratio". "c (mol/dm³) = n ÷ V (V in dm³)" is kept verbatim, on Triple only.

## Budget check (the examiner's note to the commander)

With th1 tagged TH-only, the CH page still has:
- one flagship (the bench);
- two mid-size activities (s-sort, plus the s-think confrontation);
- the 4.3.2.3 teaching added through two worked examples, Q1 and r4;
- about 220 words of body prose.

## New instruments and helpers

- **The reaction bench** (`benchSvg`, `token`, `load`, `finish`, tick-driven step animation). It is a vertical layout, so the 16 px labels stay legible at 390 px, built from KS4D primitives (`svg`, `T`, `arrow`, `C.*`) inside this lesson's Component.
- No `_ext` file.
- This lesson has no `triple-higher` tags, so it does not need the `'isHigher && isTriple'` runtime shim that `concentration-of-solutions` carries (see that lesson's notes for the engine bug).

## Body prose word count

About 255 words: the hook paragraph (38), the limiting-reactant explainer (79), the balancing explainer (62), the s-solution paragraph (47, TH only), and the big question (32).

## Self-check done

- **Template:** tags balanced; every `{{ }}` root exists in `renderVals`; all dc-imports are registered blocks with their declared props.
- **Logic:** run in Node with the real `ks4-lib.js` and `ks4-diagrams.js` and a source record from `build_source_record`, on CH and TH, with and without reduced motion. Mix A, Mix B and "Your mix" were all driven through their animations. No `undefined` or `NaN`.
- **Scratch build:** a clone of the worktree with a temporary batch module; `build_ks4.py --batch` gave zero console errors at 1280 and 360.
- **Headless Chrome:** checked at 390 (light) and 1280 (dark). There is no horizontal scroll, and the `#s-solution` route layer appears on TH and not on CH.
