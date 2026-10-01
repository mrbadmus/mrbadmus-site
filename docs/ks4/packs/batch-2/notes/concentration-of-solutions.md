# concentration-of-solutions — author notes (batch-2)

## Lesson record

```python
dict(slug="concentration-of-solutions",
     source_file="concentration-of-solutions.dc.html",
     subject="chemistry", topic_id="quantitative",
     title="Concentration of Solutions",
     spec="5.3.2.5",          # 8464 5.3.2.5 / 8462 4.3.2.5; TH layer adds 8462 4.3.4
     family="Quantitative", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2",
     # s-bench is a bespoke instrument with no dc-import (heuristic would say
     # "figure"; pinned so it cannot drift). s-mol is a data-route section
     # whose only import is Ks4Choice, which the classifier cannot type.
     block_map={"s-bench": "figure", "s-mol": "check"})
```

`spec` is the data's own value, as `verify_batch_slugs` expects. The page shows the route's own number: `AQA Chemistry (8464) 5.3.2.5` on Combined, `(8462) 4.3.2.5` on Triple, plus `· 4.3.4` on TH. Both the eyebrow and the key-note spec are worked out in logic, because `SPEC_TEXT` has no batch entries.

## Family and why

**QUANTITATIVE.** The concept is one calculation, mass ÷ volume. The one thing pupils get wrong is the cm³ → dm³ conversion, and that is a calculation error, not a structural one. The flagship is a simulation that feeds straight into CFIFA, which is how the architecture defines this family.

## Activities and the demand each trains

| block | size | demand |
|---|---|---|
| Hook (Ks4Choice, ungraded): 60 g/dm³ sports drink, 250 cm³ glass | micro | **Apply**: mass from concentration × volume, before any teaching. The distractors are the classic slips (no conversion, ×4, ×250). |
| **s-bench, "The solution bench"** (flagship, new instrument) | L | **Calculate, predict-gated.** The pupil picks a mass (2/5/10/20 g) and a volume (100/200/250/500 cm³), then commits to one of four concentrations. Those are the right one plus three answers built from named errors: unconverted (÷ cm³), multiplied, and inverted (V ÷ m). Only then does the solution get made. The cylinder fills to the line and the solute grains (one dot per 0.5 g) fall from the dish and spread through the liquid, so dots per space shows the concentration. Each wrong pick gets the feedback for its own error, plus the worked line. Three solutions are needed to complete it. The log shows that different mass/volume pairs can give the same g/dm³. Reduced motion: an instant end state. Real `<button>`s with aria-pressed; the controls lock while it animates. |
| s-think (Ks4Choice, graded, spot the flaw) | micro | **Explain**: diagnose the missed conversion. |
| s-convert (Ks4Sort, 3 bins) | M | **Convert fluency**: sort volumes by their value in dm³. Every card carries the same digits (25, 250, 2500, 2.5 litres, 0.25 litres), so word shape cannot solve it; only the factor of 1000 does. Litres are included because 1 dm³ = 1 litre (frozen th1). |
| s-pour (higher): two Ks4Choice | M | **Compare and Calculate (HT explain bullet)**: two portions poured from one bottle (same concentration, different mass); then dilute the small one 50 → 200 cm³ and work out 2 g ÷ 0.200 dm³ = 10 g/dm³ from mass and volume, **not** from c₁V₁ = c₂V₂. There is a drawn figure: two beakers with equal dot spacing. |
| s-mol (triple-higher): Ks4Choice | micro | **Calculate** in mol/dm³: 4.0 g NaOH in 250 cm³ → 0.40 mol/dm³. The distractors are 16 (forgot ÷Mr), 0.0004 (no conversion) and 640 (×Mr). |
| s-calc (Ks4Cfifa) | worked pair | CFIFA, with numbers that differ by tier (below). |
| Ladder | 4 rungs | ① State (1) ② Calculate (F 2 / H 3, with a Convert choice) ③ Explain chain (F 3 / H 2) ④ Describe (4, marking points) |

### CFIFA (Foundation and Higher differ; the source FIFA appears on both)

- **Foundation worked examples:**
  - Nothing to convert: 12 g in 0.40 dm³ → 30 g/dm³ ⚑ (the examiner's suggested example).
  - **The source FIFA verbatim** (15 g NaOH, 500 cm³ → 30 g/dm³), with Convert `500 cm³ ÷ 1000 = 0.5 dm³` in front.
  - Mass from c × V: 50 g/dm³, 200 cm³ → 10 g (frozen th2 example 2).
- **Higher worked examples:**
  - Nothing to convert, rearranged: 8.0 g, 16 g/dm³ → 0.50 dm³ (frozen th2 example 3).
  - The source FIFA.
  - Convert, then rearrange: 40 g/dm³, 150 cm³ → 6.0 g ⚑.
- **Foundation write-it-out:**
  - Q1: 9.0 g in 0.30 dm³ → 30 g/dm³ (nothing to convert) ⚑.
  - Q2: 6.0 g in 150 cm³ → 40 g/dm³ (convert; examiner-drafted).
- **Higher write-it-out:**
  - Q1: mass of NaCl in 250 cm³ of 40 g/dm³ → 10 g (convert; examiner-drafted).
  - Q2: volume for 3.0 g at 12 g/dm³ → 0.25 dm³ = 250 cm³ (nothing to convert going in; dm³ → cm³ at the end) ⚑.

### Ladder

- **r1 (authored ⚑).** State how to convert cm³ → dm³. The distractors are ×1000 (the wrong way), ÷100 (the cm → m length confusion) and ÷10 (cm → dm as a length; this is frozen q1 wx3's error).
  - It is authored rather than `K.find`, because the bank has only two items. q2 is barred from rungs (§ frozen items), and q1 is an apply-level calculation, not recall. With no `K.find` in r1, `check_rung1_fallback` has no needles to warn on.
- **r2.**
  - Foundation: 4.0 g in 200 cm³ → 20 g/dm³ ⚑ (2 marks).
  - Higher: KNO₃, 60 g/dm³ × 0.350 dm³ = 21 g ⚑ (3 marks).
- **r3.**
  - Foundation: an explain chain diagnosing 18 ÷ 600 = 0.03, then the correct 30 g/dm³ ⚑ (3 marks).
  - Higher: the examiner-drafted A vs B (5 g in 100 vs 200 cm³), which is the HT explain bullet (2 marks).
  - Each has two red herrings tied to named misconceptions.
- **r4.** Describe how to make 250 cm³ of 20 g/dm³ NaCl (Foundation) or 200 cm³ of 35 g/dm³ KCl (Higher, 7.0 g ⚑). It has four marking points (examiner-drafted shape) and one "do not accept" (using the concentration as the mass).

## Misconceptions and where each is confronted

1. **Not converting cm³ → dm³ (the frozen common_mistake).**
   - Born at the first calculation, so it is confronted at the bench's predict gate (the unconverted option and its 1000× feedback).
   - Then again, three beats, in s-think: the quote, why it is wrong, and the correct line.
   - Drilled in s-convert; caught in r2's Convert choice and in r3 (Foundation).
2. **Converting the wrong way (×1000).** Covered by r1's distractor, the r2 conv option, the r3 herring, and the hook's 15 000 g option.
3. **Inverting the formula (V ÷ m).** Covered by the bench's inverted option, and s-think option C.
4. **Multiplying instead of dividing.** Covered by the bench's multiplied option, s-think option B, and the hook's 240 g option.
5. **"A larger volume of the same solution is more concentrated" (amount vs concentration). HT.** s-pour, first choice; the quote is in the mis-quote line.
6. **"Diluting removes solute" / "adding water changes nothing" / "more water, stronger". HT.** s-pour, second choice. Each distractor is one of these.
7. **TH: g/dm³ vs mol/dm³, and ×Mr vs ÷Mr.** s-mol distractors.
8. **Volume of solvent vs volume of solution (C5/C20).** All new text says "to make … of solution". It is deliberately **not** made a scored distractor, because the frozen bank q1 itself says "500 cm³ of water". Marking that wording wrong on the same page would contradict a verbatim item.

## Route tags (every one)

| element | tag | citation |
|---|---|---|
| `#s-pour` section (amount vs concentration; dilution reasoning from mass and volume) | `higher` | 8464 5.3.2.5 / 8462 4.3.2.5: "(HT only) explain how the mass of a solute and the volume of a solution is related to the concentration of the solution" |
| "Explain" command-word card | `higher` | same HT bullet |
| `#s-mol` section (mol/dm³, n ÷ V, ÷Mr) | `triple-higher` | 8462 4.3.4 "Using concentrations of solutions in mol/dm³ (chemistry only) (HT only)"; absent from 8464 |
| equation card c = n ÷ V | `triple-higher` | 8462 4.3.4 |

These differ by route in logic, with no badge: CFIFA examples and questions (Foundation vs Higher, per content standards §2), ladder r2/r3/r4 (`R.isHigher`), key-note lines (the dilution line is Higher only; the mol/dm³ line is TH only), and the eyebrow and key-note spec (8464 vs 8462; `· 4.3.4` on TH).

## ⚑ Net-new science-bearing items

- The hook: 60 g/dm³ × 0.25 dm³ = 15 g, and its replies.
- The bench's computed options and feedback strings, the legal line, and the "one dot per 0.5 g" model.
- The s-think item and its reveal.
- The s-convert cards. All are ÷1000, and litre = dm³ comes from frozen th1.
- The s-pour figure and both choices: 40 g/dm³ × 0.050 = 2 g; × 0.200 = 8 g; 2 ÷ 0.200 = 10 g/dm³.
- The s-mol explainer and its item (examiner-drafted numbers; the conversion "÷Mr" comes from the frozen `higher` field, c = m ÷ (Mr × V)).
- CFIFA items marked ⚑ above.
- Ladder r1, r2 (both tiers), r3 (Foundation), and r4 (Higher numbers). r4 Foundation and r3 Higher use examiner-drafted numbers.
- Command-word definitions, the key fact, and key-note lines 4–6 (rearrangements from the frozen `equations`; dilution from the frozen key_note; mol/dm³ from 4.3.4).
- **The volumetric flask (r4 points 3–4; legal line) is an extension, per the examiner** (AT 1 practical context, not named in 4.3.2.5).

## Frozen items flagged wrong, and how they are handled

- **q2** ("80 g/dm³ … 250 cm³"): distractor 3's working gives 2000, not 320 (C26), and wx2 teaches a false relationship (C25). **Kept verbatim in the practice bank (`K.bank`), never a ladder rung or body item on any route.**
- **q1** ("… 500 cm³ of water"): wording imprecise (C20); numbers right. **Kept verbatim in the bank.** It is not a rung, for the reasons under r1.
- **Not displayed (theory re-cut):**
  - th1: g/cm³ (R7 / C2, NOT-IN-SPEC) and "at Foundation level".
  - th3: c₁V₁ = c₂V₂ (R5) and serial dilution (R6). These are not taught anywhere on the page.
  - The key-note's "c₁V₁ = c₂V₂" is cut.
  - The `higher` field's "mol/dm³ is the standard unit in Higher-level calculations" (C12, wrong for CH) is not shown.
  - The `higher` field's titration sentence (R9) is left to `titrations`; it is linked in connects where that page exists.
- **Matching is replaced** by s-convert. Its c₁V₁ item (C19) is not carried.

## Key note

The source key_note is used sentence by sentence where the examiner passed it: lines 1–3 verbatim, and the dilution sentence on Higher routes only. c₁V₁ = c₂V₂ is cut. Two lines are added: the frozen equations' rearrangements, and, on TH only, mol/dm³.

## mol/dm³ ownership (examiner's note for the commander)

**This lesson owns the mol/dm³ explanation (8462 4.3.4) on TH:** the definition, n ÷ V, and the link from g to mol via Mr. `using-moles-calculations` (TH layer) applies c × V to a limiting-reactant problem and links back here. The titration calculation is left to `titrations`. Both lessons link to it through `K.hrefFor`, filtered to null-safe.

## New instruments and helpers

- **The solution bench** (`benchSvg`, `answers()`, the tick-driven fill and drop animation). It is built inside this lesson's Component, from KS4D primitives (`svg`, `line`, `T`, `circ`, `C.*`). It is a measuring cylinder with 100–500 cm³ graduations, a dashed red target line, a dish of grains, and dissolved dots.
- **`pourSvg`**: two beakers with equal dot density.
- No `_ext` file.
- **Engine shim (please read): `'isHigher && isTriple': TH` in `renderVals`.**
  - `build_ks4.apply_route_layers` wraps a `data-route="triple-higher"` element in `sc-if` with the expression `isHigher && isTriple`.
  - `shared/ks4-runtime.js`'s `lookup()` does plain key lookup only, so that wrapper is always false. Without the shim, triple-higher content never renders on any route. This was verified in a scratch build: TH showed no `#s-mol` until the shim was added.
  - The real fix belongs in the engine: `ROUTE_LAYER_EXPR["triple-higher"] = "isTH"`, since `KS4.route()` already returns `isTH`. The shim is harmless after that fix and can be deleted then.

## Body prose word count

About 200 words. That is the hook paragraph (38), the explainer (77), the s-mol paragraph (52, TH only), and the big question (30). Instrument copy, choices and ladder are excluded.

## Self-check done

- **Template:** tags balanced; every `{{ }}` root exists in `renderVals`; the dc-imports are all registered blocks with their declared props.
- **Logic:** run in Node with the real `shared/ks4-lib.js` and `shared/ks4-diagrams.js` and a source record from `build_source_record`, on all four routes, with and without reduced motion. Every bench option was driven through its animation. No `undefined` or `NaN` anywhere.
- **Scratch build** (APFS clone of the worktree, a temporary `ks4_lessons/batch_mytest.py`; the real worktree untouched): `build_ks4.py --batch` gave zero console errors at 1280 and 360.
- **Headless Chrome:** checked at 390 and 1280, light and dark. There is no horizontal scroll at 390. Route layers are present or absent correctly on CF, CH and TH, with badges.

## Review fixes (quality-b, science-chem-a)

- **Q-1 (required).** Title in sentence case, "Concentration of solutions", in `<title>`, `<h1>`, the Ks4Chrome title and the Ks4KeyNote title.
- **Q-2 (required).** `madeLines` now leaves out the solution just made while its verdict is showing, and `hasMade` counts only earlier ones. The result no longer appears twice.
- **Q-3 (required).** Higher r3 is now 3 marks and at least as hard as Foundation r3. A is 6.0 g in 150 cm³ and B is 10 g in 250 cm³: convert both, both are 40 g/dm³, so they are equally concentrated. Two new red herrings (more salt; less water). ⚑ The arithmetic was checked.
- **Common_mistake caps text: not applicable.** This lesson never prints `common_mistake`.
- **quality-b A-1.** "Give the unit" is folded into the Calculate card.
- **quality-b A-2.** Foundation Q1 is now 9.0 g in 0.25 dm³ = 36 g/dm³, and the close line now says 250.
- **quality-b A-3.** The explainer's conversion example is now 500 cm³ = 0.500 dm³, so it no longer repeats the hook's 250 cm³ line.
- **science A-9.** On CF/CH the eyebrow reads "AQA Combined Science (8464) 5.3.2.5 · Quantitative". The keySpec "AQA 5.3.2.5 (8464)" carries no subject label, so it is unchanged.
- **science A-11.** r1's command word is now "Give", with the prompt "Give the step that converts a volume in cm³ into dm³."
- **science A-10.** In r4 (Foundation and Higher), the transfer point now accepts a volumetric flask "(or another container where the volume can be measured)". The make-up point now reads "until the total volume of solution is 250 cm³ / 200 cm³, then mix". The legal line still names the volumetric flask, as the accurate method.
- **Engine shim removed.** The `'isHigher && isTriple'` key is deleted (the engine now uses reserved flags). The "Engine shim" paragraph above is now historical.
- **Scratch rebuild (fixed engine), with zero console errors.** Route sections showed as follows:
  - `#s-mol` and the c = n ÷ V card show on TH only, badged "Higher · Triple".
  - `#s-pour` shows on CH and TH.
  - CF and TF show neither.
  - No horizontal scroll at 390.
