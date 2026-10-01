# changes-in-energy — author's notes (batch-2)

## Lesson record

```python
dict(slug="changes-in-energy",
     source_file="changes-in-energy.dc.html",
     subject="physics", topic_id="energy",
     title="Changes in energy",
     spec="6.1.1.2",            # 8464 6.1.1.2 = 8463 4.1.1.2, base on both
     family="Quantitative",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2")
```

## Family: QUANTITATIVE, and why

The idea is carried by three equations. The thing pupils get wrong is
arithmetic structure: which quantity is squared, and which unit goes in.
The flagship is a simulation that produces numbers, and those numbers feed
straight into CFIFA, as the family requires. BATCH-PLAN's provisional
family agrees.

## Line-up and the demand each part trains

| # | block | demand |
|---|---|---|
| Hook | `Ks4Choice`: the same car at twice the speed. How much more energy must the brakes transfer? (unscored) | Commit to a factor before any teaching. The reveal is ×4. |
| Flagship (L) | **Store bench**, new instrument (`#s-bench`). Four changes: Ep with h doubled (×2), Ee with e doubled (×4), Ek with v tripled (×9), Ek with m doubled (×2). Each change: predict the factor (3 options, every distractor a named error) → "Fill the store" → the scene moves (shelf rises, spring stretches, velocity arrow grows, second block fades in) and the after bar grows from the before value. Two working lines follow. | Predicting how a store scales with each variable. This trains *which quantity is squared*, the error the examination lists first. The tripled speed blocks rote "doubling gives ×4". The doubled mass straight after it shows the contrast. |
| Mid (M) | `Ks4Sort` **Units first**: 8 exam values sorted into "Insert as it is" or "Convert first" (g, km/h, cm, kJ against kg, m, N/m, m/s). | The C of CFIFA: deciding whether to convert. The examination names this as "the commonest lost mark on Ee". Cards carry only quantity = value + unit, so knowing SI units is the demand. |
| `equation` | Three cards, each chipped **Equation sheet**, with quantities, units and rearranged forms. Ee card: "Valid up to the limit of proportionality"; e can be a compression. Ep card: "The question always gives g." | — |
| Micro (misconception) | `Ks4Choice` **spot-the-flaw**: Ep = 20 × 9.8 × 3.0 for a box of *weight* 20 N. | Identify the error: weight used as mass, so g is counted twice. |
| CFIFA | `Ks4Cfifa`: worked examples are verbatim FIFA 1 (Ek) and verbatim FIFA 2 (Ep), each with "Nothing to convert", then one convert example. **Foundation:** 15 cm → 0.15 m, Ee = 0.45 J. **Higher:** 250 g → 0.25 kg, Ep → Ek chain, v = 7.9 m/s. Two write-it-out questions, different per tier. **F:** Ep 4.0 kg × 12 m (nothing to convert); Ek 600 g at 15 m/s (convert). **H:** v from Ek = 300 000 J, m = 1500 kg (rearrange); k from 0.90 J at 6.0 cm (convert + rearrange). | Watch then do, convert first, rearrange at Higher (content standards §2). |
| Command words | Calculate, Explain, Describe: the three the ladder uses. | — |
| Exam tip | **Omitted.** No subtopic has an `examiner_tip` on any route (checked all four `all_subtopics_physics*.py`). | — |
| Ladder | r1 verbatim q2 (spring k = 400 N/m, 1 mark, Calculate). r2 calc, 3 marks. **F:** 300 g at 4.0 m/s → 2.4 J (g→kg). **H:** 800 kg, 90 kJ → v = 15 m/s (kJ→J, rearrange). r3 chain, falling ball, Ep → Ek, with 2 red herrings. r4 6-mark Describe, bungee jump, levels from the examination §5. | — |
| Key note | `K.keyLines(slug)`, verbatim. | — |
| Bank | `K.bank(slug, route)`, 2 verbatim items. | — |
| End | Tutor line plus a legal line: g = 9.8, no dissipation on the bench, spring within the limit of proportionality, bars to scale only within a change. | — |

The rail has 6 nodes: HOOK, BENCH, UNITS, FLAW, CFIFA, LADDER.

## Misconceptions and where each is confronted

1. **"Twice the speed (or stretch), twice the energy" / forgetting to square.**
   This is born on the bench at change 2 (e doubled) and change 3 (v tripled).
   Picking the unsquared factor opens an amber three-beat panel inside the bench.
   - Beat 1, the mistake as a pupil says it: "Twice as much speed, twice as much energy."
   - Beat 2, why it is wrong: speed and extension are squared, so the factor is squared too.
   - Beat 3, the correct version: 2 × 2 = 4, 3 × 3 = 9; square v or e first.
   The ×6 option at change 3 confronts "squaring = doubling" (v² = 2v), which the examination lists.
2. **Units not converted** (g, cm, kJ, km/h). Units sort, then every CFIFA convert step. The unconverted answer is named in each close/note (4500 J, 67 500 J, 0.05 N/m).
3. **Weight used as mass in mgh / g counted twice.** Spot-the-flaw, right after the equation block, where Ep = mgh is first written.
4. **"Energy is used up as it falls."** Ladder r3 herring, with corrective why. r4 reject list.
5. **v ∝ h** ("twice the height, twice the speed"). Ladder r3 herring.
6. **Ee beyond the limit of proportionality** (examination C10). Corrected on the Ee equation card. The frozen theory's "elastic limit" wording is not displayed.

## Route tags

**None.** Every point in 8463 4.1.1.2 / 8464 6.1.1.2 is base. The spec
section carries no HT and no "Physics only" label (examination §2: "No HT
content in 4.1.1.2; no physics-only content").

- **Ee = ½ke² is BASE, not HT.** `findings-for-mide.md` item 3 says
  "Ee = ½ke² HT-only". The brief §3 carries that list in, but this lesson
  does not apply it. The examination read the spec text, and 4.1.1.2 says
  "Students should be able to apply this equation which is given on the
  Physics equation sheet", with no HT marker. I also read both June 2026
  equation-sheet PDFs (the `EQ_BY_YEAR[2026]` URLs). Their key reads
  "HT = Higher Tier only equations". Ee carries no HT mark on either sheet;
  only Vp Ip = Vs Is, p = m v and F = B I l are marked HT on the
  Combined sheet. The findings item concerned an HT *question* on
  `forces-elasticity` and is not a spec ruling. Ee is taught on all four
  routes.
- Tier differences are **numbers only**, chosen in logic by `R.isHigher`
  (content standards §2): the convert worked example, both CFIFA questions
  and ladder r2. Rearranging and the Ep→Ek chain appear at Higher. No base
  content is hidden from Foundation.

## Equation-sheet chips: a deviation from the brief

The commander's brief said "Ek = ½mv², Ep = mgh learn-it". The examination
§5 also says so, from 8463 Appendix A's recall list, but its examiner did
**not** re-read the June 2026 sheets. I downloaded and read both
(`pdftotext`). Each prints all three: "kinetic energy = 0.5 × mass ×
(speed)²", "elastic potential energy = 0.5 × spring constant ×
(extension)²", and "gravitational potential energy = mass × gravitational
field strength × height". The 8464/8465 sheet and the 8463 sheet are both
headed "FOR USE IN JUNE 2026 ONLY". This matches the pilot's ruled
precedent: V = I R is a recall equation in Appendix A, but it carries the
**Equation sheet** chip in L13/L14 (DEPARTURES `resistors-C9`) because it
is on the 2026 sheet. So all three cards carry **Equation sheet**, and no
card says "Learn it".

Two things for Mide's review:
- the spec still lists Ek and Ep as recall equations;
- `KS4.EQ_YEAR` must move when AQA publishes the June 2027 sheets. AQA has
  confirmed sheets for 2025–2027.

## ⚑ Net-new science-bearing items

- ⚑ Hook: brakes transfer the car's kinetic energy away and get hot (8464 6.5.6.3.4 / 8463 4.5.6.3.4). The worked numbers come from the frozen theory example: 1000 kg at 20 m/s = 200 000 J; at 10 m/s, 50 000 J.
- ⚑ Bench values, all from frozen examples or simple variants: 2 kg at 1.5 m → 29.4 J, and at 3.0 m → 58.8 J (theory 2). k = 200 N/m at 0.05 m → 0.25 J, and at 0.10 m → 1.0 J (theory 3). 70 kg at 6 m/s → 1260 J (FIFA 1); at 2 m/s → 140 J; 140 kg at 6 m/s → 2520 J.
- ⚑ The bench option replies and the squaring confrontation.
- ⚑ Units sort: 72 km/h ÷ 3.6 = 20 m/s and 500 g → 0.5 kg (both from the frozen common_mistake). 15 cm, 3.6 kJ, 2.5 m, 40 N/m, 1.2 kg, 12 m/s.
- ⚑ Equation cards: the rearranged forms; "The question always gives g" (4.1.1.2); "Valid up to the limit of proportionality" and compression (4.1.1.2, 4.5.3).
- ⚑ Spot-the-flaw: W = mg (4.5.1.3). Ep = (20 ÷ 9.8) × 9.8 × 3.0 = 60 J = weight × height.
- ⚑ CFIFA convert examples and all four questions. Every number was recomputed: 0.45 J; 7.84 J → v = 7.92 → 7.9 m/s; 470.4 J; 67.5 J; v = 20 m/s; k = 500 N/m.
- ⚑ Ladder r2 (2.4 J; 15 m/s), r3 chain and herrings (conservation of energy, 4.1.2.1), r4 bungee levels and points (examination §5, examiner-drafted).

## Frozen items flagged and how they are handled

- **q1** ("An 800 kg car…"): the key is correct. The "16,000 J" option label and wx3 misdiagnose the error, and wx1 reads as an instruction (examination C21/C23/C24). It is kept verbatim in the bank and is **not** used as a rung. The ladder uses q2 for r1. The examination says q1 is usable on all routes, but q2's feedback is clean.
- **Theory 3, "Only valid within the ELASTIC LIMIT"** (C10, WRONG). This is re-cuttable theory and is not displayed. The Ee card says "limit of proportionality".
- **Theory 2, "heavier objects store more GPE"** (C7). Not displayed. The page says "mass".
- **key_note line 6, "All three equations need mass in kg and distance in m"** (C14, minor imprecision: Ee has no mass). Kept verbatim, because the brief makes the key note verbatim via `K.keyLines`. This is flagged for a DEPARTURES ruling if Mide wants it changed.
- **matching**: replaced by the units sort, as the pack instructs.
- **rp**: none. Correct: the examination says this is an AT 1 opportunity, not an RP. No RP block.

## New instrument / helper

- **Store bench** (lesson-local, in the Component logic): `scene()`, `bars()`
  and `benchSvg()` draw on `KS4D` (`svg`, `line`, `circ`, `T`, `arrow`) in
  the house style, with cream plate and Georgia labels. The animation is a
  1.1 s interval tween. Under reduced motion it
  swaps instantly. Prediction buttons are real `<button>`s with
  `aria-pressed`, and "Fill the store" stays disabled until a pick is made.
- No `_ext` file.

## Body prose

205 words of static body prose (explainers 81 + 38, hook 29, misconception
panel 57). Every explainer is ≤150 words before a commitment. Under the
~700 budget.

## Not done / for the commander

- `Ks4End` always prints its "Connects to" heading, even when the list is
  empty (a block behaviour, which is outside my files). I listed
  `internal-energy` (same batch, so `hrefFor` resolves),
  `forces-elasticity` and `work-done-energy-transfer`. The last two drop
  out until they ship.
- I built and drove both lessons in a **scratch copy** of the worktree
  (`build_ks4.py --batch batch-cetest`, a throwaway module):
  - zero console errors on 8 pages at 1280 and 360;
  - at 390 px, no `undefined`, `NaN` or `{{` in the text and no horizontal
    overflow, on CF and TH, before and after driving the hook and all four
    bench changes.
  The scratch copy has been deleted.

## Review fixes (1 Oct 2026)

| row | what I did / why not |
|---|---|
| S-1 | Nothing in the lesson. The engine withholds frozen q1 (B2-W10). Rung 1 was already the spring item. |
| S-2 | r4 point 6 now reads "…by air resistance. The total energy stays the same." The false causal "so" is gone. |
| Q-CE1 / Q-X1 | Replaced the static pills with the `ks3-route-switch` route chip (`{{ routeWords }}`, `{{ routeSwitchOptions }}`), copied from using-moles-calculations. Added both keys to the fallback `R`. |
| Q-CE2 | Deleted the explainer sentence that said which quantities are squared. The bench now asks first. |
| Q-CE3 | **Not applied, by commander ruling.** "Equation sheet" stays on Ek, Ep and Ee, because the June 2026 sheets print all three (as in pilot resistors-C9). The CFIFA placeholder "as on the equation sheet" stays for the same reason. |
| Q-CE4 | Rounds 1 and 2 now ask only "What happens to the energy in the … store?". Round 4 drops "at the same 6 m/s", which the h2 already says. |
| Q-EN3 pattern (contradicted replies) | All four hook replies set to `''`. The reveal states the answer at once, so "Hold that" and "Check it" were false. |
| A-3 | Applied. r4 point 4 now reads "Once the cord pulls up harder than her weight, she slows down…". |
| A-CE3 | Applied. The Foundation convert example's Insert line is now `Ee = ½ × 40 × 0.15²`, and Fine-tune squares it. |
| A-CE4 | Applied in part. The after-bar value label is removed, because the working line under the figure repeats it. The before-bar label stays: it is the only number on screen before the pupil commits. |
| A-1 | Not applied. A "Spec: recall this" line under an "Equation sheet" chip contradicts the ruling's message for this exam year. |
| A-2 | Not applied. The key note is frozen and served verbatim. This needs a DEPARTURES ruling. |
| A-CE1 | Not applied. A key fact card would repeat the key note (no-redundant-text rule). |
| A-CE2 | Not applied. The commander confirmed the spring item for rung 1. |

Validated in a scratch copy (`build_ks4.py --batch`, throwaway module): zero console errors on all 8 pages at 1280 and 360. At 390 px on CF and TH, the route chip reads the right words, there is no `undefined`, `NaN` or `{{`, and no overflow before or after driving the hook and all four bench changes. The scratch copy has been deleted.
