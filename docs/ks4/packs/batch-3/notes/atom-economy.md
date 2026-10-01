# atom-economy — author's notes (batch 3)

## Lesson record

```python
dict(slug="atom-economy", source_file="atom-economy.dc.html",
     subject="chemistry", topic_id="quantitative", title="Atom economy",
     spec="8462 4.3.3.2", family="Quantitative", routes=["TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-strip": "figure", "s-brine": "check", "s-route": "comparison"},
     withhold=[W("Why do addition reactions always have an atom economy of 100%?", "B3-W?")])
```

Spec: 8462 4.3.3.2, chemistry only. The second bullet (choosing a reaction pathway) is HT. The topic is absent from 8464. The eyebrow is fixed at "AQA Chemistry (8462) 4.3.3.2 · Quantitative" because the lesson ships only on Triple routes.

## Family and why

**Quantitative.** A calculation carries the concept. The flagship is a scale model of that calculation (bar length = Mr), and it feeds straight into CFIFA.

## Line-up

hook → video → explainer → **s-equation** (Learn it; placed before the flagship so the formula is printed once and the strip can use it) → **s-strip (L)** → **s-think** → **s-brine (M)** → explainer (why it matters; versus % yield) → **s-route (Higher; M2)** → s-calc → command words → ladder → key note → bank → end.

This differs from `percentage-yield` (yield bench plus a sort), `relative-formula-mass` (unpacker plus pans) and `conservation-of-mass` (flask plus writer). The subtopic has no examiner tip, so there is no tip slot.

## Instruments and the demand each one trains

| block | size | demand |
|---|---|---|
| `s-strip` "The mass strip" | L, new | **Judge and calculate the useful share of the reactants' mass, from the balanced equation.** Three reactions: ethene hydration (100%), lime (56%) and iron (45.9%). Each runs in three steps. (1) The reactant bars are drawn to scale with Mr, and the product row is an empty dashed outline of the same length (conservation). (2) The pupil commits to a band: 100%, more than half, or less than half. (3) On commit, the product bars drop out of the reactant row, desired product first, and a red marker lands at the share. The working line follows, in AQA's reactant form. It is animated, with an instant swap under reduced motion, and the tabs lock while it runs. The three reactions are ranked by their numbers, not labelled "high" or "low" (fixes examination C5). |
| `s-brine` "One equation, three products" | M, new | **The numerator is the desired product, counted with its coefficient.** 2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂. The pupil commits to which product gives the lowest atom economy, with a fourth option for "one equation has one atom economy". Then they view each product's strip and working: NaOH 52.3%, Cl₂ 46.4%, H₂ 1.3%. |
| `s-route` "Choose a route" | M, **Higher** | **Weigh pathway factors** (spec HT bullet). Fermentation and hydration are set out side by side (an HTML grid with role=table). A Ks4Sort then asks which route each row favours. The done-note says rows are not votes, explains the effect of by-product usefulness, and calls for a justified conclusion. It feeds the Higher rung-4 6-marker, which refers back to this table instead of printing the data a second time. |
| `s-calc` CFIFA | worked/do | Worked 1 is the source's ethanol FIFA, verbatim, with "Nothing to convert" in front and a note on the Formula step giving AQA's reactant denominator, 28 + 18 = 46. Worked 2 is iron, Fe₂O₃ + 3CO, where the coefficients count. Write-it-outs differ by tier. Foundation: 2H₂O → 2H₂ + O₂ (11.1%) and Mg + 2HCl (97.9%). Higher: 2NH₄Cl + Ca(OH)₂ (18.8%) and CH₄ + H₂O → CO + 3H₂ (17.6%). Higher needs the coefficient on both sides of the fraction. |

## Misconceptions and where confronted

1. **Coefficient on the desired product forgotten** (examination §5). Confronted in `s-think` right after the flagship's iron run. Three beats: the quote (2NaCl → 2Na + Cl₂ with Mr(Na) = 23 → 19.7%); a spot-the-flaw whose options are no error, the coefficient (key), dividing by the waste, and the fraction inverted (509%); then the reveal: 46 ÷ 117 × 100 = 39.3%.
2. **Atom economy confused with percentage yield or completion.** Confronted in:
   - the hook (the "every molecule reacts" distractor);
   - explainer 2;
   - the rung 1 distractors;
   - the rung 3 herring.
3. **"Fermentation makes two ethanols, so it is more efficient."** Hook distractor (coefficient seduction).
4. **"A renewable raw material means a higher atom economy."** Hook distractor.
5. **Higher only: choosing a pathway on atom economy alone.** Confronted in the `s-route` intro and done-note, and in rung 4's reject line.

## Route tags

| element | tag | citation |
|---|---|---|
| `s-route` section | `higher` (TH only, since the lesson is TF/TH) | 8462 4.3.3.2, second bullet "(HT only) explain why a particular reaction pathway is chosen…" (examination R5) |
| s-brine closing line (usefulness of by-products) | `higher` | same bullet |
| "Evaluate" command-word card | `higher` | same |
| Rung 4: TH gets the 6-mark Evaluate; TF gets a 4-mark Calculate/Give | logic, `R.isHigher` | same |
| Rung 2 and CFIFA numbers | logic, `R.isHigher` | content standards §2 |

The calculation, why it matters, addition = 100%, and the comparison with yield are all base triple (TF and TH), per examination R1–R4 and R6. The pack's `higher` lines that carry triple content are taught on TF as well.

## Frozen items flagged and how handled

- **q2 "Why do addition reactions always have an atom economy of 100%?" — WITHHOLD on TF and TH.** It has two creditable answers (examination C27). Needle: `Why do addition reactions always have an atom economy of 100%?`
- **q1 "A reaction produces 80 g of desired product…"** It stays in the bank and **is not a rung**: the stem conflates collected masses with equation masses (C20), and option 4 has no named misconception (C24). All four rungs are authored.
- **`equations[0]` (products denominator): not displayed.** The equation block shows AQA's reactant form, with "sum of Mr(reactants) = sum of Mr(products)" as a second Learn-it card (4.3.1.2), as the examination §4 asks.
- **`common_mistake` (tells pupils NOT to use the reactants): not shown anywhere** (C15 WRONG). Its correction runs through the lesson: the coefficient think-again and the reactant-form working on every line.
- **`key_note` line 1** (products form) is replaced by an authored AQA-form line ⚑ (C16). Lines 2–5 are verbatim, via `K.keyLines(slug).slice(1)`.
- **th1 formula** (C2) and **th2 "high" / "low" labels** (C5) are not reproduced.
- **th3 "COMPARING ROUTES"** is re-taught with the full factor list, Higher only (C14).
- "Green chemistry", "substitution/elimination" and "pharmaceutical manufacturers" are cut (not in spec).
- The FIFA steps are verbatim. Their labels are slightly off (C18), but they are kept, with a note added to step 2.

## ⚑ Net-new science-bearing items

- ⚑ Hook (two factories), options and reveal. "Almost half" means 88/180 = 48.9%.
- ⚑ The strip's three reactions, the band replies and the working lines (100%, 56%, 45.9% checked).
- ⚑ The brine numbers: 153 total; 52.3%, 46.4%, 1.3%.
- ⚑ The Higher line on by-product usefulness.
- ⚑ The NaCl/Na think-again: 39.3%, 19.7%, 509%, and 23/71 for the "waste" option.
- ⚑ The fermentation vs hydration table: about 30 °C vs 300 °C and 60–70 atm; renewable vs finite; slow batches vs fast continuous; dilute (distil) vs pure; CO₂ vs none. These are from the examination's indicative content. "In batches" and "continuous" are standard textbook facts; the examiner should confirm them.
- ⚑ All CFIFA write-it-outs; every Mr total was checked equal on both sides.
- ⚑ Rung 1, authored at parity.
- ⚑ Rung 2. Foundation: CuCO₃ + H₂SO₄, 159.5/221.5 = 72.0%. Higher: TiCl₄ + 2Mg, 48/238 = 20.2%.
- ⚑ Rung 3 chain.
- ⚑ Rung 4 Foundation: 2Fe₂O₃ + 3C, 224/356 = 62.9%.
- ⚑ Rung 4 Higher: levels and indicative content, from examination §5.
- ⚑ Key-note line 1.

## Deviation from the brief

The brief asks for a CFIFA worked example with a unit to convert. The examination (§5, which overrides the brief) says atom economy has no unit conversion and forbids inventing one. Both worked examples and all write-it-outs therefore open with "Nothing to convert: Mr values have no units". The Convert *decision* is still trained:
- every write-it-out starts with it;
- the rung-2 Convert options include two plausible wrong conversions.

## New instrument / helper

`row()` and `stripSvg()` are in the lesson logic, drawn with `KS4D.T`/`KS4D.line` on the cream plate. No shared file was added.

## Section ids needing block_map

- `s-strip` → `figure`
- `s-brine` → `check`
- `s-route` → `comparison`

## Body prose

About 230 words on TF and about 290 on TH.

## Self-check

The build passed in a scratch clone: zero console errors on TF and TH at 1280 and 360. No undefined, NaN or "{{" text, and no horizontal scroll. The withheld item is absent. The strip, brine and route were driven and screenshotted at 390 px, in light and dark.

During the self-check I replaced the first version of the route table, a `<table>` with `sc-for` inside `<tbody>`. It rendered no rows, because the HTML parser foster-parents the loop out of `<tbody>`. The current version is a div grid with ARIA table roles. Future authors should avoid `sc-for` inside `<table>`.

## Review fixes

| id | where | old → new | reason |
|---|---|---|---|
| S-3 | practice-bank section | `sc-if value="{{ ready }}"` → `sc-if value="{{ bankOn }}"` (`bankOn = ready && bank.length > 0`) | The engine now withholds q1 (B3-W9) as well as q2 (B3-W6), so the bank is empty on TF and TH. The block, including its heading, is not rendered, so there is no "0 of 0". No rung or text refers to the bank. |
| A-7 | ethanol CFIFA tab | unchanged: the frozen Formula step stays verbatim, with the reconciling AQA-reactants note under it | accepted under the frozen policy |
| Q-1 | `rungs.r3` | marks 2 → **3** | three-link chain |
| Q-2 | `row()` unit dividers | full-height line → short ticks at the top and bottom of the bar | the dividers were cutting through the centred labels (2F\|e, 2Na\|Cl) |
| Q-3 | CFIFA worked example 2 | Iron (Fe₂O₃ + 3CO, 45.9%, repeating the strip) → **Copper: 2CuO + C → 2Cu + CO₂**, (2 × 63.5) ÷ (2 × 79.5 + 12) × 100 = 127 ÷ 171 × 100 = **74.3%** ✓ (products 127 + 44 = 171) | the strip's Iron tab printed the same working |

Validated in a scratch clone with q1 and q2 withheld:
- the build passed;
- the bank block is absent;
- no "0 of 0", undefined or NaN;
- no horizontal scroll at 390 px;
- r3 shows 3 marks.
