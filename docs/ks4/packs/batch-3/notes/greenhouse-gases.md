# greenhouse-gases — authoring notes (batch 3)

## Lesson record

```python
dict(slug="greenhouse-gases", source_file="greenhouse-gases.dc.html",
     subject="chemistry", topic_id="atmosphere",
     title="Greenhouse gases and climate change",
     spec="5.9.2.1–5.9.2.4 (8462 4.9.2.1–4.9.2.4)",
     family="Model", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-bench": "figure", "s-effects": "check",
                "s-reports": "check", "s-limits": "check"})
```

Every one of the four block_map ids is needed. `s-bench` has no import. `s-effects` and `s-limits` are Ks4Choice-only wrappers, which the classifier cannot type. `s-reports` is a bespoke instrument. `s-sources` (Ks4Sort → check), the command-words block (keyword), `s-ladder` and `s-keynote` classify on their own. Proven on the real compiler in a scratch clone: zero console errors at 1280 and 360 px.

## Family: MODEL, and why
One structure, the asymmetry, explains everything that follows. Short wavelengths pass through the atmosphere; long wavelengths are absorbed and re-emitted. That one model covers why Earth is warm, why more gas warms it further, and why "reflect" and "ozone" answers are wrong. MODEL's flagship is a parameter instrument with a prediction at each change of regime, and the bench is exactly that: three regimes (no gas, natural, extra). The BATCH-PLAN's provisional family (Model) is kept.

## Instruments and the demand each trains
- **Flagship (L) `#s-bench`, "Radiation bench".**
  - Three regimes, each predict-gated.
  - After the commit, rays draw on as waves: tight short-wavelength waves from the Sun reach the surface, and loose infrared waves leave it. Infrared rays are absorbed at molecules (ring and pulse), then re-emitted up or down. The thermometer animates to −18 °C, 15 °C, or above 15 °C. Reduced motion gets the final frame.
  - Once all three regimes are run, tabs let the pupil compare and replay them.
  - Demand: **explain the mechanism as interaction of short and long wavelength radiation with matter** (5.9.2.1), and predict the effect of changing the amount of gas.
- **Mid (M1) `#s-sources`: Ks4Sort, CO₂ or methane** (8 cards). Demand: **recall two human activities for each gas** (5.9.2.2). The cards defeat word shape: "natural gas" sits in both bins (a gas boiler gives CO₂, a leak gives methane), and the methane cards include no burning.
- **Micro `#s-effects`: exam-trap Choice.** Which listed effect would not earn a climate-change mark? The answer is ocean acidification, an effect of CO₂ itself (examination C14). Demand: **describe four distinct potential effects** (5.9.2.3).
- **Mid (M2) `#s-reports`: bespoke "Judge the evidence".** Two practice reports. The pupil makes three A/B judgements (data representativeness, possible bias, peer review) and answers a correlation-versus-cause item. One check gives per-row corrective notes. Demand: **evaluate the quality of evidence in a report; peer review; uncertainty and bias** (5.9.2.2, base).
- **Micro `#s-limits`: Choice.** The electric-bus swap, which is limited if the electricity comes from fossil fuels. Demand: **give reasons why actions may be limited** (5.9.2.4).
- Ladder:
  - r1: frozen q2 (methane / livestock), Give, 1 mark, at parity (9 vs 9 words).
  - r2: data, Use, 2 marks, on a T-shirt life-cycle table. It asks which stage emits most, and why "1.3 kg" is not the footprint (full life cycle).
  - r3: chain, Explain, 4 marks: short in, surface emits long, gases absorb, re-emit in all directions. Herrings: reflect, absorbs sunlight, ozone/UV.
  - r4: Evaluate, 6 marks, the examiner's cold-winter newspaper claim with a sketch temperature graph and Levels 1–3.
- No calculation, so no CFIFA; the carbon-footprint calculation is NOT-IN-SPEC (R10) and was cut. No RP: the examiner confirms none (the infrared RP is a separate physics lesson).

## Misconceptions and where each is confronted
- "Reflect" instead of absorb and re-emit: regime 2 distractor, then the three-beat panel ("Greenhouse gases reflect the heat back down to Earth.") right after that commitment. Also a rung 3 herring.
- Ozone confused with the greenhouse effect: distractors in regimes 1 and 3, and a rung 3 herring.
- Gases absorbing incoming sunlight, or wavelengths swapped: regime 2 distractors and a rung 3 herring.
- "The greenhouse effect is bad": the source common_mistake reborn as a three-beat panel after regime 3, pointing back to regime 1's −18 °C.
- "Burning natural gas gives methane", and pollutant versus greenhouse gas: `#s-sources` cards.
- "Climate change = it gets hotter", and acidification counted as a climate effect: `#s-effects` and the command-word card.
- "Carbon footprint = CO₂ from a car" and "footprint counts CO₂ only": rung 2 part 2 and a `#s-limits` distractor.
- "One cold winter disproves warming" (weather versus climate): rung 4 only. Correlation versus cause is trained in `#s-reports`, so rung 4 is not pre-answered.

## Route tags
**None.** All of 8464 5.9.2.1–5.9.2.4 and 8462 4.9.2.1–4.9.2.4 is base (examination §2). The pack's Higher-only `higher` field content is taught as base on all four routes: peer review and evidence (R5) and why actions are limited (R8). Eyebrow: "AQA Combined Science (8464) 5.9.2.1–5.9.2.4 · Model" on Combined and "AQA Chemistry (8462) 4.9.2.1–4.9.2.4 · Model" on Triple. Header: route chip only.

## ⚑ Net-new science-bearing items
- ⚑ The hook's "about 15 °C" average surface temperature. −18 °C is frozen text.
- ⚑ "The Sun is very hot … most of its radiation is short wavelength: visible light, with some ultraviolet." The frozen text says visible and UV.
- ⚑ Ozone absorbs some of the Sun's ultraviolet, not Earth's infrared (consistent with q1 wx2).
- ⚑ Methane comes from things that digest or rot with little air; rice paddies; natural gas is methane, and burning it gives CO₂.
- ⚑ The effects list: sea level from land ice melting and seawater expanding (C12); storms, rainfall, heat and water stress, food, species distribution (examiner §5); scale, risk and environmental implications. Acidification is an effect of CO₂, not of the temperature rise (C14).
- ⚑ The peer review, models, uncertainty, media bias and communication paragraph (5.9.2.2 wording; gap C19).
- ⚑ Reduction actions including carbon taxes and offsetting (C17), and the list of why actions are limited (examiner §5; gap C18). The electric-bus point: it only helps with low-carbon electricity (C17).
- ⚑ Practice reports A and B, and the "tested mechanism" answer to correlation versus cause.
- ⚑ T-shirt life-cycle data (example numbers, total 5.6 kg, labelled made up for practice in the legal line).
- ⚑ The rung 4 sketch temperature graph (schematic, no y values) and its marking points and levels, including weather versus climate. Rung 3 marking chain from the examiner's 4-mark Describe.

## Frozen items and source fields
- **No quiz item withheld.** Both frozen items are clean (examination §4). q1 ("Why is the greenhouse effect necessary…") stays in the bank only: it fails length parity (24 vs about 15 words), so it is not a rung.
- **Key note:** the frozen key_note is not shown verbatim. It lists N₂O (R9; the spec names three gases) and lacks the carbon-footprint definition (C23). It is replaced by six authored lines: the three spec gases, the mechanism, two activities per gas, the effects, the footprint in spec wording, and the limits. **This is a DEPARTURES §2 row.**
- Not shown: N₂O throughout (R9), cement, enteric fermentation, CO₂-equivalent, "anthropogenic" (C21), the footprint calculation (R10). The frozen footprint definition ("measured as CO₂ equivalent … individual, organisation or product", C16) is replaced by the spec's verbatim "over the full life cycle of a product, service or event".
- There is no examiner_tip, so the slot is omitted.

## New instruments and helpers
These all live inside the lesson's own Component; there is no `_ext` file:
- the radiation bench: `benchSvg`, `wave`, `head`, `ray` (a draw-on animation using pathLength and dashoffset), `mol` (CO₂/H₂O/CH₄ glyphs), `thermo`;
- the "Judge the evidence" two-report comparator (`#s-reports`): template plus state `rep`/`repChecked`/`repDone`;
- `tshirtTable` (`KS4D.table`) and `tempGraph` (the rung 4 sketch);
- `order()`, the same hash ordering as early-atmosphere.

## Adjacency with early-atmosphere
The two lessons share nothing in their hooks, flagships or line-ups:
- **early-atmosphere:** hook on Venus/Mars share bars → stepper → equation with spot-the-flaw → chain → evidence sort.
- **greenhouse-gases:** hook on −18 °C → parameter bench → source sort → effects trap → report comparator → limits choice.

The content does not overlap. Early-atmosphere ends with burial locking carbon away. Greenhouse picks up from burning it.

## Body prose
About 380 words of explainers. Counting the hook, the bench prompts and reveals, the two panels and the report cards, it is about 700 words in all, at the budget. The longest run of prose before a commitment is about 105 words (the footprint and limits explainer).

## Review fixes
| id | what I did / why not |
|---|---|
| Q-1 | All four hook options now have the reviewer's corrective replies. The reveal's last sentence is deleted. |
| Q-2 | The effects explainer's list is replaced by "Its effects reach the sea, the weather, food and wildlife." The full list still reaches the pupil in `effReveal` and the key note. |
| Q-3 | `REP[2]` replaced by the reviewer's "Report B was peer reviewed. What does that tell you?" item. It has four options, shuffled by `order()`. |
| Q-4 | The heading reads "Compare the three runs." once the tabs appear. |
| A-10 (science) | "mainly methane" is now used in the explainer and in both sort `why` lines. |
| A-1 | Eyebrow is now "Radiation bench". |
| A-2 | The "Atmosphere" label is 20 px, starting at x = 10, so it clears the incoming rays. I did not move it to x = 400, because the outgoing infrared rays sit there. |
| A-3 | Report B's Data row now includes "plus carbon dioxide records". |
| A-4 / A-5 | Not changed. A-4 follows pilot practice. A-5 (line-up overlap with early-atmosphere) is answered under EA A-4. |
