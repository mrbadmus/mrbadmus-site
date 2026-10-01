# particle-motion-pressure — author's notes (batch-3)

## Lesson record

```python
dict(slug="particle-motion-pressure",
     source_file="particle-motion-pressure.dc.html",
     subject="physics", topic_id="particle-model",
     title="Particle motion in gases",
     spec="6.3.3.1 (8463 4.3.3.1–4.3.3.3)",   # base 6.3.3.1 = 4.3.3.1; Triple layer 4.3.3.2; Triple Higher layer 4.3.3.3
     family="Model",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     withhold=[W("A gas is at 27°C and 100 kPa", "B3-W?")])   # all routes — see "Frozen items"
```

No `block_map` entries are needed: the build classifies every section on its
own (`s-bench` and `s-piston` → figure, `s-mark` → check, `s-equation` →
equation, `s-calc` → worked-example). Checked on the real compiler in a scratch
clone, all four routes.

## Family: MODEL, and why

One structure, molecules in constant random motion hitting the walls, explains
every behaviour the subtopic asks for: why a gas exerts a pressure, why
heating a sealed gas raises it (base), why a bigger volume lowers it (Triple),
and why a fast push warms the gas (Triple Higher). The flagship is the MODEL
shape: a parameter instrument with a prediction at every change of regime.
BATCH-PLAN's provisional family agrees.

It deliberately differs from its batch-2 neighbour `internal-energy` (also
MODEL, same topic): that bench is a heating curve with a kinetic/potential
bar; this one is a live gas with a pressure gauge and wall-hit arrows, and its
hook (an aerosol warning label) and line-up (bench → examiner sort → piston →
equation → CFIFA) share nothing with it. The batch-3 neighbours
`temperature-changes-shc` (hook: sand and sea) and `specific-latent-heat`
(hook: a steam burn) also differ.

## Line-up and the demand each part trains

| # | block | demand |
|---|---|---|
| Hook | `Ks4Choice`, unscored: the aerosol label "Do not burn, even after use". Why must an empty can never go on a fire? | Commit before teaching. The swelling-particles option seeds the bench's first confrontation. |
| Explainer | ≤100 words: constant random motion, hits on the walls, pressure as their total push. | — |
| Flagship (L), all routes | **The gas bench** (`#s-bench`), new instrument. Sixteen molecules in a sealed can, simulated live (elastic collisions with each other and the walls), with a thermometer, a pressure gauge, and an arrow at right angles to the wall at every wall hit (longer for a harder hit). Stage 1: heat 20 °C → 300 °C — predict what happens to the molecules. Stage 2: watch the walls — predict what happens to the hits. Reveal: the molecules speed up, the gauge rises 100 → 196 kPa, and two bars show how often (×1.4) and how hard (×1.4) the walls are hit. Animated; reduced motion jumps to the end state with the molecules still. | Predict, at each regime change, what the molecules do and how that produces pressure. Builds the AQA chain: temperature → average kinetic energy → speed → more frequent, harder wall hits → pressure. |
| Mid (M), all routes | `Ks4Sort` **Mark it like an examiner** (`#s-mark`): eight lines from pupils' answers to "a sealed container of gas is heated; explain why the pressure increases", sorted into "Earns a mark" / "Earns nothing". | Apply AQA marking: which statements are creditworthy links and which are named misconceptions. Word shape checked: "walls", "faster", "collide/collision" and "molecules" each appear in both bins; "expand" appears once (the gas-volume card was reworded so the word does not predict the bin). |
| Flagship continued, Triple | **The piston bench** (`#s-piston`, `data-route="triple"`): the same gas in a cylinder with a piston, 60 cm³ at 20 °C. Pull the piston out slowly to 120 cm³ — predict the pressure. Gauge 100 → 50 kPa, bars ×0.5 / ×1.0, V label updates. | Predict and explain p–V at constant temperature with the particle model (4.3.3.2). |
| Flagship continued, Triple Higher | Inside `#s-piston`, a `data-route="triple-higher"` stage: push the piston back in fast (bicycle pump) — predict the temperature. Molecules that hit the moving piston rebound faster and turn gold; the thermometer rises ("warmer"); the gauge reads 132 kPa at 60 cm³, above the 100 kPa it read there before. | Explain why doing work on a gas raises its temperature (4.3.3.3). |
| Equation, Triple | `#s-equation` (`data-route="triple"`): pV = constant, chip **On the sheet**, with p₁V₁ = p₂V₂ and both rearrangements; a Units first card. | — |
| CFIFA, Triple | `#s-calc` (`data-route="triple"`): source FIFA verbatim behind "Nothing to convert", a second nothing-to-convert example, a convert example; two write-it-out attempts each opening with the convert decision. TF and TH numbers differ throughout (TH adds rearranging for V and Pa/kPa/m³ conversions). | Calculate pressure or volume changes. |
| Key fact | Base statement only. | — |
| Command words | Describe, Explain, Predict; Calculate is `data-route="triple"`. | — |
| Exam tip | **Omitted.** No `examiner_tip` on any route. | — |
| Ladder | r1 (all): authored ⚑ Describe, 1 mark — the motion of gas molecules (correct option is not the longest). r2: CF data rung (Predict, 2 marks; trend + predict at 80 °C); CH data rung with uneven intervals (proportional to °C? + predict at 100 °C); TF calc (0.060 → 0.024 m³, 250 kPa, nothing to convert); TH calc (0.0090 m³ → 2500 cm³, convert cm³ → m³, 360 kPa; review fix S-2/Q-PMP2). r3: CF/CH chain — the frosty-morning tyre (cooling); TF/TH chain — bigger volume at constant temperature. r4: CF/CH/TF 4-mark Explain (how molecules produce a pressure, starting from their motion); TH 6-mark levels (blocked bicycle pump), from the examination §5. | — |
| Key note | `K.keyLines(slug)` verbatim, filtered in logic: the two kelvin/absolute-zero lines never show; "Smaller V…" and "Boyle's Law: pV = constant." show on Triple only. | — |
| Bank | `K.bank(slug, route)` — q1 only once q2 is withheld. | — |
| End | Tutor line + a route-dependent legal line (16 molecules in 2D; gauge scaled to 100 kPa; slow piston keeps 20 °C on Triple; on TH the fast push loses no energy and its temperature rise is scaled to match air). | — |

Rail: CF/CH — HOOK, BENCH, MARK, LADDER. TF/TH — HOOK, BENCH, MARK, PISTON, CFIFA, LADDER (PISTON ticks after stage 4 as well on TH).

## Misconceptions and where each is confronted

1. **"Heat a gas and its molecules get bigger"** (q1 wx3; examination §5).
   Confronted on the bench, where it is born, at stage 1: an amber three-beat
   panel opens after every stage-1 reveal (it is the commonest KS3 carry-over,
   so every pupil sees it, not only those who picked it). Again in the
   examiner sort ("The molecules expand when they are heated" → no mark) and
   as an r3 red herring.
2. **"Pressure rises because the molecules collide with each other more"**
   (examination §5). Bench stage 2: picking it opens a three-beat panel that
   points at a molecule–molecule bump in the middle of the can pushing on no
   wall. Again in the sort and as red herrings on both r3 chains.
3. **"More particles"** (q1 wx1) and **"particles vibrate"** — stage-1 replies;
   "vibrate faster" is also a no-mark card.
4. **"No change in pressure, same temperature"** on expansion (Triple) —
   stage-3 reply; r3 Triple herring "molecules slow down with more room".
5. **"No heat supplied, so no temperature rise" / "only friction"** (TH;
   examination §5) — stage-4 replies; r4 TH reject list.
6. **"Pressure ∝ temperature in °C"** — the CF/CH r2 distractors (210 kPa;
   218 kPa; "it doubles from 10 °C to 50 °C") — trains the qualitative
   relation without kelvin.

## Route tags, with spec citations

| element | tag | citation |
|---|---|---|
| Gas bench (motion, temperature ↔ average KE, pressure from wall collisions, qualitative p–T at constant V) | base | 8464 6.3.3.1 = 8463 4.3.3.1 |
| Triple explainer (compressed/expanded by pressure changes; **net force at right angles** to the wall) | `triple` | 8463 4.3.3.2 (physics only, no HT) |
| Piston bench, stage 3 (p–V at constant T, particle explanation) | `triple` | 8463 4.3.3.2 |
| Piston bench, stage 4 (work done on a gas raises its temperature; bicycle pump) | `triple-higher` | 8463 4.3.3.3 (physics only, HT only) |
| Equation pV = constant, CFIFA | `triple` | 8463 4.3.3.2; Appendix A sheet eq 12, no HT mark |
| Command word Calculate | `triple` | 8463 4.3.3.2 |
| r2/r3 Triple variants (by `R.isTriple`), r4 6-marker (by TH) | logic | 4.3.3.2; 4.3.3.3 |

pV = constant is **not** taught as Higher (it is Foundation-tier Triple
content) and is never shown on Combined. Kelvin, absolute zero and
p/T = constant appear nowhere on the page (NOT-IN-SPEC, examination R9/R10).

## Equations

pV = constant — chip **On the sheet** (printed on the June 2026 8463 sheet,
eq 12; Triple only). The `equations` field's other two lines (p ÷ T,
T(K) = T(°C) + 273) are never rendered (examination C16).

## ⚑ Net-new science-bearing items

- ⚑ Hook option set and reveal (pressure rises on heating; sealed can cannot vent).
- ⚑ Bench copy: stage asks, replies, the two "why" lines, the two three-beat panels.
- ⚑ The bench model's numbers: 196 kPa at 300 °C from 100 kPa at 20 °C (= 100 × 573/293, correct for an ideal gas at constant volume; the page never states the ratio or kelvin); hits ×1.4 and push per hit ×1.4 (both ∝ speed ∝ √T(K): √(573/293) = 1.40); 100 → 50 kPa for 60 → 120 cm³; 132 kPa at 60 cm³ after a fast push from 120 cm³ at 50 kPa (adiabatic air, γ = 1.4: 50 × 2^1.4 = 132; temperature ≈ 114 °C, shown only as "warmer").
- ⚑ Examiner sort: eight cards and their credit/no-credit rulings (credit: KE up, faster, more frequent wall hits, bigger force per hit — all examination §5 marking points).
- ⚑ Triple explainer wording of 4.3.3.2.
- ⚑ CFIFA: TF second example (frozen theory example re-cut, 100 kPa 2 m³ → 0.5 m³ = 400 kPa), TF convert example (bubble 250 kPa × 4.0 cm³ ÷ 100 kPa = 10 cm³), TH examples (150 × 0.80 ÷ 120 = 1.0 m³; 100 × 60 ÷ 240 = 25 cm³ = 2.5 × 10⁻⁵ m³), attempts (TF 120 × 0.40 ÷ 0.60 = 80 kPa; 100 × 3.0 ÷ 75 = 4.0 m³; TH 2400 × 0.050 ÷ 100 = 1.2 m³; 100 × 45 ÷ 150 = 30 cm³). All rechecked.
- ⚑ Ladder r1 (authored at parity), r2 all four (CF table 92/99/105/112 kPa at 0/20/40/60 °C → 119 kPa at 80 °C; CH table 95/105/109 kPa at 10/40/50 °C → 126 kPa at 100 °C — both generated from p ∝ (θ + 273) and rounded; TF 250 kPa; TH 360 kPa), r3 both chains, r4 4-mark points and the TH 6-mark levels (examination §5 descriptor, worded as levels).
- ⚑ Key fact.

## Frozen items flagged wrong, and how they are handled

| item | examination | handling |
|---|---|---|
| q2 · needle **"A gas is at 27°C and 100 kPa"** | NOT-IN-SPEC on every route (kelvin, p ∝ T; C27). Also C28: its 1200 kPa distractor's own working gives 1211. | **Withhold on all four routes** (commander: engine `withhold`). Never used as a rung. |
| q1 ("Why does the pressure inside a tyre increase…") | OK, base, all routes. | Kept in the bank. **Not a rung**: its key (20 words) is ≥4 words longer than its longest distractor (15), so it fails option-length parity; r1 is authored instead. |
| FIFA (200 kPa, 3 m³ → 1 m³) | OK, Triple only. | Verbatim behind "Nothing to convert", inside `data-route="triple"`. |
| `higher` field | WRONG TAG (C18). | Not rendered. Its pV sentence → the Triple layer; its kinetic-theory sentence → base bench; absolute zero dropped. |
| `equations` field, lines 2–3 | NOT-IN-SPEC (C16). | Not rendered; only pV = constant shows, Triple only. |
| `key_note` lines 5–6 (kelvin, absolute zero) | NOT-IN-SPEC (C20). | Filtered out in logic; lines 3–4 shown on Triple only. Text of the shown lines unchanged. |
| theory 1–3 kelvin/p ∝ T passages; `common_mistake` kelvin half; `variables` T in kelvin | NOT-IN-SPEC (C3, C7, C11, C19, C21). | Not used. The common_mistake's collision half ("RATE and FORCE of collisions") is what the bench and sort teach. |
| theory 2 heating chain out of order (C6); tyres (C12); bike pump as pV (C17) | IMPRECISE. | Re-cut: the bench uses the corrected chain; the bike pump appears only as 4.3.3.3 (work done). |

## New instruments / helpers

- **Gas bench** and **piston bench**: one 2D hard-disc gas model in the lesson's own logic (`newGas`, `stepGas`, `setT`, `ke`, `pressure`, `place`), drawn with `KS4D` primitives (cream plate, house strokes). Animation runs only while the bench is on screen (an IntersectionObserver on `#s-bench`/`#s-piston`) or while a reveal is playing; `prefers-reduced-motion` gets still molecules and an instant end state. All controls are real `<button>`s. No `_ext` file.

## Body prose

Hook + explainers, measured on the built page: 130 words (CF/CH), 201 words
(TH). Longest run before a commitment: ~100 words.

## Self-check

Built with `build_ks4.py --batch batch-3` in an APFS scratch clone (a scratch
`batch_3.py` holding only this lesson and `power`): compile clean, the build's
own zero-console-error check at 1280 and 360 px passed. Driven in headless
Chrome on all four routes at 390 px, motion on and reduced: every bench stage,
the piston stages (TF, TH), CFIFA, ladder render; no `undefined`/`NaN`/`{{`/
`null` text, no sideways scroll, zero console errors (other than the
CORS-blocked health ping every localhost page makes).

## Review fixes

Reviews: `docs/ks4/packs/batch-3/review/science-phys-a.md` §3, `quality-a.md` (particle-motion-pressure).

| row | what I did / why not |
|---|---|
| S-2 / Q-PMP2 (REQUIRED) | TH r2 rewritten to the quality reviewer's item: a 0.0090 m³ balloon at 100 kPa squeezed to 2500 cm³; convert cm³ → m³ (÷ 1 000 000); answer 360, unit kPa. Every numeric ladder answer is now < 1000. Driven in a scratch build: typing 360 + kPa grades Correct. |
| Q-PMP1 (REQUIRED) | Every wrong hook option now has a corrective reply ("Molecules do not change size when they are heated." / "Even a can holding only air would burst…" / "The metal is not what changes most: the gas pushing on it is."). The swell reply deliberately stops short of "they move faster", which bench stage 1 asks. The shared reveal was reworded so it no longer repeats any reply. |
| S-A9 | Applied: Triple explainer now says the molecules keep "the same average speed". |
| S-A10 | Applied: TH Question 1 now asks for "the volume the gas would occupy at 100 kPa". |
| A-PMP1 | Applied: on TH the stage-3 verdict and bars hide once the fast push starts (`p3Show`). |
| A-PMP2 | Applied: when the "bump into each other" confrontation opens, the empty verdict line is not drawn (`bShowVerdict`). |
| S-A8 | Not changed: the frozen key-note line "Boyle's Law: pV = constant." is not wrong, and the equation card states the conditions. |
| A-PMP3 | Not changed: the equation-sheet link is part of the brief's fixed lesson head on every physics page; Combined pupils use the same sheet across the topic. |
