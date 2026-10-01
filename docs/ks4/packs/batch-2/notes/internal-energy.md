# internal-energy — author's notes (batch-2)

## Lesson record

```python
dict(slug="internal-energy",
     source_file="internal-energy.dc.html",
     subject="physics", topic_id="particle-model",
     title="Internal energy",
     spec="6.3.2.1",            # 8464 6.3.2.1 = 8463 4.3.2.1, base on both
     family="Model",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2")
```

## Family: MODEL, and why

One structure, particles with kinetic and potential energy, explains a whole
class of behaviour. Warming, melting, boiling, the flat sections of heating
and cooling curves, and why a cool pool out-totals hot tea all follow from it.
The flagship is the MODEL shape: a parameter instrument (energy supplied)
with a prediction at every change of regime. BATCH-PLAN's provisional
family agrees.

It deliberately differs from the pilot's `states-of-matter`
(INVESTIGATION). That pilot lesson collects messy readings to find a melting
point. This one has no data collection. Its bench is about the split of
internal energy between kinetic and potential, which `states-of-matter` never
shows.

## Line-up and the demand each part trains

| # | block | demand |
|---|---|---|
| Hook | `Ks4Choice`, unscored: you turn the flame up under boiling water. What does the thermometer do? | Commit before teaching. This is the examination's "heating always raises temperature" error. |
| Flagship (L) | **Heating bench**, a new instrument (`#s-bench`). Ice at −10 °C is heated at constant power through 4 stages: solid warming, melting at 0 °C, liquid warming, boiling at 100 °C. **Before each stage** the pupil picks one of 4 outcomes. Each outcome pairs what the temperature does with which energy of the particles increases. Then they press "Heat it". **Animated**: the particles vibrate harder, leave the lattice, wander, and escape as gas. The flame lights while heating. The thermometer moves. A stacked internal-energy bar grows in its kinetic or its potential part. The heating curve draws itself. Reduced motion jumps to the end of the stage. | Predicting, at each regime change, whether energy in raises the temperature or changes the state. Linking each outcome to kinetic or potential energy. Seeing that internal energy rises at every stage. |
| Misconception | `ks3-misconception` + `Ks4Choice` spot-the-flaw: an iceberg at −5 °C against coffee at 80 °C. "The coffee is hotter, so it has more internal energy." | Explain the flaw: average versus total. |
| Mid 1 (M) | `Ks4Sort` **Which has more internal energy?** Five pairs, two bins. Four are water pairs varying amount, temperature and state; one is the same mass in different states (ice/water at 0 °C, steam/water at 100 °C). | Compare internal energy by reasoning from particles, not temperature. Every card has the identical "X, or Y" shape, so it cannot be solved by word shape. The answers split 3/2 across the bins. |
| Mid 2 (M) | Drawn **cooling curve** (A–F) + `Ks4Sort`: each section, A to B through E to F, is placed into "Temperature falls: kinetic energy decreases" or "Temperature constant: potential energy decreases". | Interpret a cooling graph that includes changes of state (spec 4.3.2.3). The cards are letters only, so the graph must be read. |
| Command words | Determine, Explain, Describe: the three the ladder uses. | — |
| Exam tip | **Omitted.** No `examiner_tip` on any route. | — |
| Ladder | r1: verbatim q1 ("…temperature stays constant for several minutes"), Identify, 1 mark. r2: data, Determine, 3 marks. A drawn heating curve for X: the melting point, the state at 50 °C, and the average KE on D–E. r3: chain, Explain, 3 marks. Stearic acid freezes at 69 °C, with 2 red herrings. r4: 6-mark Describe, ice at −10 °C → water at 20 °C, with levels from the examination §5. | — |
| Key note | `K.keyLines(slug)`, verbatim. The examination finds it OK (C15). | — |
| Bank | `K.bank(slug, route)`, 2 verbatim items. | — |
| End | Tutor line + legal line covering the GCSE KE/PE split model, bars and time not to scale, spheres, 100 °C at normal pressure, graphs as sketches. | — |

The rail has 6 nodes: HOOK, HEAT, THINK, COMPARE, COOL, LADDER.

There is no CFIFA and no equation block, because the lesson has no
calculation (examination §5: "Equations: none to calculate in this lesson").
ΔE = m c Δθ and E = m L are named once in an explainer, as signposts to the
next lessons, both "on the equation sheet". The header keeps the
equation-sheet link, as both physics pilot lessons do.

## Misconceptions and where each is confronted

1. **"Heating always raises the temperature"** (q1's target; examination §5).
   This is born on the bench at stage 2 (0 °C) and at stage 4 (100 °C).
   Predicting "temperature rises" there opens an amber three-beat panel
   inside the bench.
   - Beat 1, the mistake: "Keep heating it and it must keep getting hotter."
   - Beat 2, why it is wrong: heating raises internal energy, not always
     temperature.
   - Beat 3, the correct version: at a melting or boiling point the energy
     goes into potential energy until the change is complete.
   It was set up first in the hook.
2. **"Hotter means more internal energy" / temperature = internal energy**
   (q2's target). Confronted by the iceberg spot-the-flaw, then practised
   in the compare sort.
3. **Internal energy = kinetic energy only** (the definition mark is lost).
   Confronted by a spot-the-flaw distractor with corrective feedback, and
   in r4's marking points.
4. **"Particles in a solid cannot move"**. Spot-the-flaw distractor.
5. **Melting or freezing "breaks the bonds inside the molecules"**
   (examination C3/C4/C12/C14/C16). The page says "forces between
   particles" throughout. Confronted by the r3 herring and the r4 reject
   list.
6. **"No energy is transferred on a flat section"** (the plateau read as
   "heater switched off"). Confronted by bench option 4 and the r3 herring.

## Route tags

**None.** 8463 4.3.2.1 / 8464 6.3.2.1 is base, with no HT and no
"Physics only" label (examination §2: "No HT or physics-only content"). The
supporting points used are all base:

- 4.3.2.3: temperature is constant during a change of state; heating and
  cooling graphs;
- 4.3.3.1: temperature related to average KE, stated for gases;
- 4.3.2.2: ΔE = m c Δθ, signpost only.

## ⚑ Net-new science-bearing items

- ⚑ Hook and reveal: at normal pressure, boiling water stays at 100 °C when heated harder; the extra energy boils it away faster (4.3.2.1, 4.3.2.3).
- ⚑ Bench stage texts and option replies. "Particles vibrate faster about fixed positions" (solid). "The energy overcomes the forces holding the particles in fixed positions, so their potential energy rises" (melting, examination C4 wording). "The energy separates the particles" (boiling).
- ⚑ The bench's schematic model: KE rises only while warming and PE only during a change of state, with bar lengths not to scale. This is stated in the legal line.
- ⚑ Explainer 2: "The temperature of a gas is related to the average kinetic energy", in the spec's own wording (4.3.3.1).
- ⚑ The iceberg/coffee spot-the-flaw and its four replies.
- ⚑ Compare sort: bath 40 °C vs mug 80 °C; ice vs water at 0 °C; water at 20 vs 60 °C; steam vs water at 100 °C; 2 kg vs 1 kg at 30 °C. Done-note.
- ⚑ The cooling-curve sketch (condensing flat at 90 °C, freezing flat at 40 °C, generic substance) and its section feedback.
- ⚑ Ladder r2: the substance X heating curve, flat at 20 °C and 80 °C, and the model answers. r3 stearic acid at 69 °C (examination §5, and the same value as the pilot `states-of-matter`). r4 levels and points (examination §5).

## Frozen items flagged and how they are handled

- **q1 keyed option**: "…to break intermolecular bonds…". This is the "bonds" imprecision (C17 is OK in substance; the wording family is C3/C4). Kept verbatim as rung 1 and in the bank, which the examination allows on all four routes. The body never uses "bonds" for forces between particles.
- **q2 wx2**: "Internal energy depends on temperature, mass AND specific heat capacity" (C23, IMPRECISE). Kept verbatim, in the bank only. q2 is not a rung, and the body never says internal energy "depends on SHC".
- **q2 wx3**: "EXTENSIVE property" (C24, not-in-spec term). Kept verbatim, in the bank only.
- **Theory 2 "THERMAL ENERGY" paragraph** (C9, borderline WRONG). Not displayed. The equations are named only as "raising the temperature, ΔE = m c Δθ".
- **Theory 1/3 "bonds" wording** (C3/C4/C12). Not displayed. Re-cut as "forces between particles".
- **matching**: replaced by the two sorts, as the pack instructs.

## New instrument / helper

- **Heating bench** (lesson-local): `partsSvg()` draws the particles, flame,
  thermometer and stacked bar, and `curve()` is a reusable temperature–time
  sketch. It is used three times: the live heating curve, the cooling
  curve, and the r2 figure. All three are built on `KS4D` primitives in
  the house style.
  - The animation is a 3.2 s interval tween per stage. Under reduced motion
    it does an instant swap with no particle jiggle.
  - Stage options are real `<button>`s with `aria-pressed`.
  - "Heat it" stays disabled until a pick is made. The pick is locked
    while heating runs.
- No `_ext` file.

## Body prose

291 words of static body prose (explainers 99 + 84 + 28, hook 28, panel 52).
Every explainer is ≤150 words before a commitment.

## Not done / for the commander

- `Ks4End` prints an empty "Connects to" heading when no link resolves. I
  listed `states-of-matter` (pilot, all routes) and `changes-in-energy`
  (same batch), so the list is never empty. `changes-of-state`,
  `temperature-changes-shc` and `specific-latent-heat` join once they ship.
- I built and drove the lesson in a scratch copy:
  - zero console errors on all 4 routes at 1280 and 360;
  - at 390 px on CF and TH, no `undefined`, `NaN` or `{{` in the text and
    no overflow, before and after driving the hook and all four bench
    stages, including the confront path.
