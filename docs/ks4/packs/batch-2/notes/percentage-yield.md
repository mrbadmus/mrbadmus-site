# percentage-yield — author's notes (batch-2)

## Lesson record

```python
dict(slug="percentage-yield",
     source_file="percentage-yield.dc.html",
     subject="chemistry", topic_id="quantitative",
     title="Percentage yield",
     spec="8462 4.3.3.1 (chemistry only; one HT bullet)",
     family="Quantitative",
     routes=["TF", "TH"],
     review_state="draft", batch="batch-2",
     block_map={"s-which": "check", "s-bench": "practical", "s-reasons": "check", "s-theory": "worked-example"})
```

`block_map` is needed. Without it `build_ks4.py` stops with "cannot infer a type for percentage-yield section 's-which'". With these four entries the lesson built cleanly in a scratch copy: 2 routes, zero console errors at 1280 and 360 px.

## Family and why

**QUANTITATIVE.** The calculation (% yield = actual ÷ theoretical × 100) is how the concept gets examined. On Higher it extends to a multi-step moles calculation. The lesson goes from the phenomenon (an 8.0 g gap closing to 6.2 g) to an instrument that accounts for the gap, then to CFIFA.

It is not REQUIRED PRACTICAL. AQA names no RP for 4.3.3.1. The bench only *uses* the salt preparation from Chemistry RP1 as its setting, as the examination suggests.

## Instruments and the demand each trains

| tier | block | demand |
|---|---|---|
| Flagship (L) | **The yield bench** (`#s-bench`, new). The verbatim FIFA's 8.0 g of copper sulfate goes through five drawn RP1 steps: react, filter, transfer, crystallise, dry and weigh. Before each step the pupil commits ("some is lost here" / "none is lost here"). Then the step's drawing shows a red loss label, a mass bar shrinks with an animated width (reduced motion: instant), and a running list says where each gram went. 8.0 → 6.2 g. | Explain *where* product is lost in a real separation, which is the spec's reason 2, instead of reciting "practical losses". The react step loses nothing, so "yes" is not the right answer every time. |
| Misconception (three beats) | **108%** spot-the-flaw (`#s-think`, `Ks4Choice`, graded) | Suggest why a yield is over 100%. It sits straight after the weighing step, which is where the error is born. |
| Mid (M) | **Sort the reasons** (`#s-reasons`, `Ks4Sort`): 7 cards into *lowers the yield* / *changes the rate only* / *breaks conservation of mass* | Tell the spec's three reasons apart from two named misconceptions (catalyst/powder raises yield; mass destroyed) |
| Micro | **Which working?** (`#s-which`, `Ks4Choice`, graded) | Set the fraction the right way up before the worked example reveals it |
| Equation | "Learn it · chemistry has no equation sheet". The verbatim equation, plus a `data-route="higher"` card with the moles chain | — |
| CFIFA (base) | The verbatim FIFA, with Convert = "Nothing to convert: both masses are in g." (examiner C18). Then a kg → g worked example and two write-it-out questions: 40 g / 34 g with nothing to convert, and 1.20 kg / 960 g with a conversion | Production: calculate |
| CFIFA (Higher, `data-route="higher"`) | Worked: CaCO₃ 12.0 g → 5.6 g CaO with nothing to convert (examiner-drafted). Worked: 1.00 kg CaCO₃ → 476 g CaO, converted. Questions: Haber 2.8 g N₂ → 0.51 g NH₃ with excess H₂ (limiting reactant, 1 : 2 ratio); Fe₂O₃ 16 kg → 9.8 kg Fe (convert, 1 : 2 ratio) | Multi-step theoretical yield via moles, ratio and the limiting reactant |
| Ladder | r1 verbatim q2 (Give, 1). r2: TF a kg → g calc (3.20 kg / 2600 g → 81.25%, 2 marks); TH an MgCO₃ → MgO moles calc (2.10 g → 0.80 g, 80%, 3 marks). r3 a chain with 2 red herrings, zinc sulfate context (Explain, 3). r4 a 4-mark "calculate and give two reasons" with marking points and a reject list | — |

Tier differentiation: the base % yield calculation is triple at both tiers, so its CFIFA is the same on TF and TH. TH gets the Higher CFIFA (rearrangement, ratios, two-formula chain, conversions) and a different r2.

## Misconceptions and where each is confronted

1. **"The mass was destroyed in the reaction."** Hook option B, then the r3 red herring.
2. **Yield over 100% accepted without comment.** `#s-think`, straight after the weighing step on the bench. The three beats are the quote, the replies, and the reveal (wet or impure product).
3. **"A catalyst increases the yield."** It is a distractor in `#s-think`, a card in the sort ("changes the rate only"), an r3 red herring and an r4 reject. The frozen th3 claim "sufficient time, temperature, catalyst" is **not** reproduced anywhere (examiner C11).
4. **Inverting the fraction / giving the loss as the yield / forgetting × 100.** `#s-which`, CFIFA close lines, r2 `wrong` text, r4 reject.
5. **HT: forgetting the mole ratio.** Close line on Higher Q2 ("175%"). Using the excess reactant: Higher Q1 close names nitrogen as the limiting reactant.

## Route tags

The whole lesson ships only on TF and TH (8462 4.3.3 "(chemistry only)"; there is no section in 8464), so nothing is tagged `triple`.

| element | tag | citation |
|---|---|---|
| Higher equation card (moles chain) | `higher` | 8462 4.3.3.1 "(HT only) calculate the theoretical mass of a product from a given mass of reactant and the balanced equation" |
| `#s-theory`: explainer plus Higher CFIFA | `higher` | 8462 4.3.3.1 HT; 4.3.2.4 limiting reactants (HT only) |
| r2 TH variant, chosen by `R.isHigher` in logic | higher | as above |
| Key-note Higher line, added by `R.isHigher` in logic | higher | as above |

The frozen `common_mistake` carries the HT moles method on TF (examiner R8). It is not displayed on any route. The moles method appears only inside `data-route="higher"` elements.

## ⚑ Net-new science-bearing items

- ⚑ Bench step losses: 0.5 g on the filter paper, 0.3 g on the flask walls, 0.8 g still dissolved, 0.2 g on the drying paper. These are model values that add up to the verbatim FIFA's 8.0 → 6.2 g. The *kinds* of loss trace to spec 4.3.3.1, "some of the product may be lost when it is separated from the reaction mixture". The legal line says the masses are a model.
- ⚑ The bench's react step: excess copper oxide makes all the acid react, and no copper sulfate is lost at that step. Source: RP1 method (8462 Appendix RP1).
- ⚑ 108% → wet or impure product. Source: examination §5, examiner-drafted 1-mark item.
- ⚑ Sort cards: "grinding a solid reactant into a fine powder" changes the rate only (8462 4.6.1.2 surface area); "a catalyst" changes the rate only (4.6.1.4).
- ⚑ The why-yield-matters explainer re-cuts th2/th3 (cost, waste, sustainability, Haber about 15% per pass, recycled to about 98%). The Haber figures are context only, as the examination says, and are never used as a rung.
- ⚑ Every new calculation was checked by hand:
  - CFIFA: 1900 ÷ 2500 = 76%; 34 ÷ 40 = 85%; 960 ÷ 1200 = 80%.
  - Higher CFIFA: CaCO₃ 12.0 g → 6.72 g, 83.3% (examiner-drafted); 1000 g → 560 g, 85%; N₂ 0.10 mol → NH₃ 0.20 mol = 3.4 g, 15%; Fe₂O₃ 100 mol → Fe 200 mol = 11 200 g, 87.5%.
  - Ladder: r2 TF 2600 ÷ 3200 = 81.25%; r2 TH 2.10 ÷ 84 = 0.025 mol → 1.00 g, 80%; r4 9.0 ÷ 12.0 = 75%.
  - Mr values: CaCO₃ 100, CaO 56, N₂ 28, NH₃ 17, Fe₂O₃ 160, MgCO₃ 84, MgO 40.
- ⚑ The r3 chain, the r4 marking points and the reject list are written from the spec's three reasons and AQA mark-scheme conventions (examination §5).

## Frozen items flagged wrong, and how they are handled

- **q1** ("A reaction has a theoretical yield of 20 g but only 14 g is obtained…"), TF and TH. Distractor index 1, "43% — (14 ÷ 20) × 3 = 42%", contradicts itself (examiner C21). It is kept **verbatim** in the practice bank (`K.bank`) and is **never a ladder rung** on either route. Rung 1 is q2, which the examiner marks clean.
- **th3 "catalyst" advice** (C11, WRONG). Not reproduced. The lesson teaches the opposite at three points.
- **th2 "100% … impossible in practice"** (C8). Not reproduced. The page says a pure, dry product can never be *more* than 100%.
- **th1 reason 4, "impure reactants"** (C4). Not taught. The taught set is the spec's three reasons.
- **Key note** (C14, C15). It is used verbatim **except** for two of the examiner's corrections:
  - "Always less than 100% in practice." → "Usually less than 100% in practice."
  - "impurities" is dropped from the reasons list.

  Mide or the next examiner should confirm both, or log them in DEPARTURES.
- The frozen matching activity is replaced by the sort.

## New instrument and helpers

- **The yield bench**, built inside the lesson's own Component: the `STAGES` table and `stageSvg(k, shown)`. It draws the RP1 apparatus in the house figure style through `KS4D` primitives (beaker, filter funnel, conical flask, evaporating basin, crystals, balance). There is no shared `_ext` file.
- Local `steps5` / `q5` helpers build the five-line CFIFA rows.

## Word count

About 330 words of body prose in the template, from the hook to the equation (instrument strings excluded). Hook paragraph: 42 words before its commitment.

## Checks run

- A node harness confirmed that every `{{ }}` resolves on TF and TH, tags are balanced, every `dc-import` prop is declared by its block or used by a pilot lesson, and no `undefined`/`NaN` text appears. It drove the whole bench to 6.2 g.
- A scratch-copy `build_ks4.py --batch` run built the lesson with zero console errors.
- Headless-Chrome drive at 390 px: no horizontal scroll; Higher badges appear only on TH (2 on TH, 0 on TF); the bench completes. Light and dark screenshots were reviewed.

## Review fixes (science-chem-b.md, quality-b.md)

- **S-1 (required):** the r4 reason marking points now accept any two of the three spec reasons: "First reason, any one of: …" and "Second reason: a different one of those three."
- **Q-1:** the bench's closing box now reads "Theoretical yield 8.0 g · actual yield 6.2 g. Nothing was destroyed." (the 6.2 g repetition is gone).
- **Q-2:** "Chemistry-only spec point." is dropped from the key note. The key note therefore carries three examiner/reviewer edits to the frozen text (C14, C15, Q-2).
- **Q-3:** r1 is now an authored "Give" MCQ at length parity, using the reviewer's wording. Each distractor names a misconception: atoms destroyed, catalyst, rounding. The frozen q2 now lives in the bank only.
- **Q-4:** the base write-it-out questions now differ by tier. TF keeps 40 g / 34 g and 1.20 kg / 960 g. TH gets rearrangement questions instead:
  - 72% of 45 g → 32.4 g, nothing to convert;
  - 85% of 2.40 kg → 2040 g, convert kg → g.

  I changed the reviewer's suggested numbers because they reproduced 34 g / 40 g and 1900 g / 2500 g, which already appear in the TF questions and the worked example.
- **Q-5:** the hard-coded pills are replaced by the route chip, in the same markup as using-moles-calculations. The eyebrow now reads "AQA Chemistry (8462) 4.3.3.1 · Quantitative". The fallback `R` carries `routeWords` and `routeSwitchOptions`.
- **A-1 (science):** the sort's done-note now says "never the maximum mass of product".
- **A-2 (science):** the Higher worked answer now reads "83.3% (83%)".
- **Quality A-2:** stage names lose their numbers ("Dry and weigh", not "5 · Dry and weigh"), so they no longer repeat "n of 5 steps run".
- **Quality A-1 (binary bench commit) and A-3 (moving `#s-which` after the worked example):** not done. Both are structural changes to the flagship's flow, not cheap fixes. Left for the next pass.
- **Validated in a scratch copy:**
  - `build_ks4.py --batch batch-2`: 52 pages, zero console errors.
  - Headless-Chrome check: the route chip reads "Triple science · Foundation tier" on TF and "… Higher tier" on TH; CFIFA Q1 differs by tier; no undefined/NaN text.
