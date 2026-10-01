# conservation-of-mass — author's notes (batch 3)

## Lesson record

```python
dict(slug="conservation-of-mass", source_file="conservation-of-mass.dc.html",
     subject="chemistry", topic_id="quantitative",
     title="Conservation of mass and balanced equations", spec="5.3.1.1",
     family="Quantitative", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-flask": "figure", "s-write": "check"},
     withhold=[W("24 g of magnesium reacts completely with oxygen", "B3-W?")])
```

Spec: 8464 5.3.1.1 / 8462 4.3.1.1 (word-for-word identical). Eyebrow and key-note spec switch on `R.isTriple`.

## Family and why

**Quantitative.** The lesson's job is one conserved quantity: no atoms are made or lost, so total mass in = total mass out. It ends in calculation (missing mass, CFIFA) and in production (writing a balanced symbol equation). BATCH-PLAN's "QUANTITATIVE — balancing equations" is kept. Balancing as a skill already has its watch-then-do on `atoms-elements-compounds` (batch 2, coefficient steppers). So this lesson does not repeat that. It teaches *why* equations balance (atoms are conserved), how to *read* the multipliers, word → symbol → state symbols, and the missing-mass calculation.

Neighbours checked, and nothing repeated:
- `atoms-elements-compounds`: steppers, the H₂O → H₂O₂ confrontation and the diatomic confrontation.
- `relative-formula-mass`: formula unpacker, Mr balance pans and the 2Mg mass ratio.
- `percentage-yield`: yield bench.
- `using-moles-calculations`: reaction bench.

## Line-up

hook (Ks4Choice) → video → explainer → **s-flask (L, flagship)** → key fact → **s-think** (misconception) → explainer (+ Higher moles line) → **s-write (M)** → s-equation (Learn it) → s-calc (Ks4Cfifa) → command words → ladder → key note → bank → end. There is no exam-tip slot, because the subtopic has no examiner_tip.

## Instruments and the demand each one trains

| block | size | demand |
|---|---|---|
| `s-flask` "Inside the flask" | L, new instrument | **Read multipliers to count atoms, then explain conservation in terms of atoms.** Two reactions in a sealed flask on a balance: CH₄ + 2O₂ → CO₂ + 2H₂O and Ca + 2H₂O → Ca(OH)₂ + H₂. The pupil commits to an atom count on the right-hand side, and each distractor is a named multiplier error. On commit, every atom slides from its reactant molecule into its product molecule (eased, 1.5 s). The balance readout never changes. Then a verdict and the atom ledger appear. Reduced motion gives an instant swap. Real buttons; tabs are locked while an animation runs. |
| `s-write` "Word to symbol · three moves" | M, new | **Write a balanced symbol equation with state symbols** (spec 5.1.1.1, 5.2.2.2, 5.3.1.1) for marble chips + hydrochloric acid, in three predict-gated moves: (1) pick the formulae line, with three distractors (CaCl, Cl for the acid, CO); (2) pick the balancing number for HCl (1/2/4); (3) pick a state symbol for each of the five species, check, and the full equation is revealed. Wrong state symbols get a reason. |
| `s-calc` CFIFA | worked/do pair | Missing mass by conservation. Worked: one with nothing to convert (CaCO₃ 10.0 → 5.6 + 4.4 g) and one converting kg → g (Mg 1.20 kg → 2.00 kg MgO, 800 g O₂). Write-it-outs differ by tier. Foundation: ZnCO₃ (nothing to convert); CaCO₃ 0.50 kg (convert). Higher: 2NaHCO₃ with two known products (nothing to convert); blast furnace with two reactants and kg → g. |

The hook is a micro-commit: the balance reading after a spark in a sealed flask.

## Misconceptions and where each is confronted

1. **"Fewer molecules after, so less mass / not balanced"** (molecules vs atoms). Confronted in `s-think`, right after the flask has shown atoms being conserved. Three beats: the quote (2H₂ + O₂ → 2H₂O, three molecules → two); a spot-the-flaw where each option's reply says why it is wrong; then the reveal gives the correct version.
2. **Coefficient multiplies only the first atom** / coefficient applied to the whole side (examination §5). Born, and predicted, in the flask's oxygen count (3 / 4 / 6), then summarised in the key fact.
3. **Bracket subscript misread** (Ca(OH)₂). This is a flask distractor (3 H). Its full treatment is RFM's.
4. **"Mass burns away as energy" / "gases used up so mass falls."** Hook distractors. One line each, as the examination asks; the full treatment of gas mass changes belongs to 5.3.1.3.
5. **Changing formulae to balance; acid written as Cl; CO for CO₂.** `s-write` move 1.
6. **(aq) for a pure liquid.** `s-write` move 3 (water).
7. **Coefficients read as grams.** Explainer 2 ("not the number of grams").

## Route tags

| element | tag | citation |
|---|---|---|
| Explainer 2, the moles sentence ("2 moles of H₂ react with 1 mole of O₂…") | `higher` | 8464 5.3.2.2 / 8462 4.3.2.2 (HT only): "chemical equations can be interpreted in terms of moles" (examination R6) |
| Rung 2 and CFIFA write-it-outs | chosen in logic by `R.isHigher` (Foundation vs Higher numbers) | content standards §2 |

Everything else is base (5.3.1.1, 5.1.1.1, 5.2.2.2). The pack's `higher` field (theoretical yield, atom economy) is **not shown on any route**. It is cut per examination R7/R8: it is chemistry-only content that was being served to Combined Higher, and it belongs to other lessons.

## Frozen items

- **q2 "24 g of magnesium reacts completely with oxygen…" — WITHHOLD on all routes.** The distractor "64 g — double the mass of magnesium" is false (double is 48 g), and its wx2 is mismatched (examination C19/C20). Needle: `24 g of magnesium reacts completely with oxygen`. The subtraction skill it tested is trained by the authored rung 2 and the CFIFA.
- q1 ("Why must chemical equations be balanced?") is correct, but it **fails option-length parity**: the key is 17 words against 5–10. It is not used as rung 1; it stays in the bank. Rung 1 is authored at parity ⚑.
- q3 (4Fe + 3O₂ → 2Fe₂O₃) is correct. It stays in the bank and is not a rung, because rung 2 must differ by tier.
- The key note is shown verbatim, via `K.keyLines`.
- The frozen th3 Mg + 2HCl state-symbol example is deliberately **not** shown in the body, because it is the rung-4 answer. The body uses CaCO₃ + HCl instead.

## ⚑ Net-new science-bearing items

- ⚑ Hook: CH₄ + 2O₂ in a sealed flask; the reading is unchanged; the reply wordings.
- ⚑ Flask: reaction 2, Ca + 2H₂O → Ca(OH)₂ + H₂ (from the pack's matching pairs); atom counts and ledgers; the distractor replies.
- ⚑ Key fact: multipliers vs subscripts (spec 5.3.1.1 wording).
- ⚑ Think-again options, replies and reveal.
- ⚑ s-write: CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂(g), and every distractor and reason.
- ⚑ CFIFA: all four write-it-out questions and both worked examples. Mass data were checked against the Mr ratios:
  - CaCO₃ 100:56:44;
  - 2Mg+O₂ 48:32:80;
  - ZnCO₃ ≈125:81:44;
  - 2NaHCO₃ 168:106:18:44;
  - Fe₂O₃+3CO 160+84 = 112+132.
- ⚑ Rung 1 (authored, State). Rung 2 Foundation: CuCO₃ 6.2 → 4.0 + 2.2 g. Rung 2 Higher: CH₄ 400 g + O₂ 1600 g → 1100 + 900 g, kg → g.
- ⚑ Rung 3 chain and herrings.
- ⚑ Rung 4 marking points: the examination's 3-mark "Write" item plus one explain mark (4 marks).

## New instrument / helper

`flaskSvg()` (in the lesson's own logic) draws atoms with `KS4D.circ`/`KS4D.T` on the cream plate, with fixed element fills and per-atom start→end interpolation. No shared file was added.

## Section ids needing block_map

`s-flask` → `figure`; `s-write` → `check`.

## Body prose

About 260 words: hook 47, explainers about 150 including the Higher line, plus headings and prompts. This is well inside the ~700-word limit.

## Self-check

Done in a scratch APFS clone, with a temporary `ks4_lessons/batch_3.py` for my two lessons only:
- `build_ks4.py --batch batch-3` passed: 6 pages, zero console errors at 1280 and 360.
- No "undefined", "NaN" or "{{" on any route.
- No horizontal scroll at 390 or 1280.
- The withheld item is absent.
- Flask, think, write and calc were driven by click.
- 390 px screenshots of the instruments were checked.

The clone was deleted afterwards.
