# C7 — Energy changes in reactions · author's notes

**Four lessons. The unit is complete.** Everything is draft and unreviewed.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `energy-and-changes-of-state` | `KS3.C.ENER.01` |
| `exothermic-reactions` | `KS3.C.ENER.02` |
| `endothermic-reactions` | `KS3.C.ENER.02` |
| `measuring-a-temperature-change` | `KS3.C.ENER.02` (as measurement) |

Two statutory statements, four lessons. `ENER.02` is one bullet naming two
opposite behaviours, and the split into a PROCESS lesson and a CONTRAST lesson
is the only way to give the endothermic case a hook of its own — otherwise it
arrives as a footnote to exothermic and stays one.

The fourth lesson owns no new content. It exists because §7 asks for an
INVESTIGATION here and because every energy figure in the unit is produced by
an apparatus that leaks, which is worth one lesson of attention.

---

## 2. Four lessons, four shapes

- **`c7-01`** — a **heating curve stepper**: one minute per tap, temperature and
  state read out together, bar trace building alongside. The two flat steps are
  the whole lesson and they have to be experienced as *waiting*, which a
  static graph cannot do.
- **`c7-02`** — a **five-beaker bench** with predict-then-run and a
  start/peak/delta readout. Four exothermic, one not — the odd one out is the
  handover to `c7-03`.
- **`c7-03`** — an **eight-item sorter**, exothermic against endothermic, with
  three deliberate pairs (melting/freezing, photosynthesis/respiration) so the
  reversal rule falls out of the sort rather than being stated.
- **`c7-04`** — a **plan critique** (five steps, sound or flawed) followed by a
  **three-dial rig builder** with eight combinations and a true value the
  student never reaches.

`c7-01` requires C1. `c7-03` cross-links to B7 and B8 for photosynthesis and
respiration, and to C5-02 for thermal decomposition.

---

## 3. Instrument kinds

`heating-curve` (`c7-01`), `temp-bench` (`c7-02`), `energy-sorter` (`c7-03`),
`plan-critique` + `rig-builder` (`c7-04`). All DOM.

`heating-curve` payload: `{curve: [{t, state, note}], minute}`. Thirteen points
from −20 °C to 120 °C with flat runs at 0 and 100. The trace bar is coloured by
whether the point repeats the previous temperature, so the flat steps show up
without any extra data. Re-pointing it at a different substance is one array.

`rig-builder` payload: `{dials: {vessel, cover, speed}, results: {key: {v, why}}}`
— a lookup keyed by the joined dial states, eight entries, each with its own
explanation. Generic three-dial apparatus chooser: any "which setup gives the
best measurement" lesson can reuse it. C10 wants nothing from it; a KS4
calorimetry lesson would.

`plan-critique` is `c3-07`'s instrument with a different plan in it.

---

## 4. Science flags

1. **−18 °C for an airless Earth and +15 °C actual**, giving 33 °C of greenhouse
   effect (`c7-04` is clean of this, but `c10-06` uses the same figures).
   Standard values. Confirm once, applies twice.
2. **Heating curve figures**: melting flat step 3 minutes, boiling flat step
   3 minutes, in a 12-minute run. The boiling step is described in the text as
   "much longer" than melting, which is true in reality (roughly 7× the energy)
   but **is not what the graph shows** — both are drawn three minutes long.
   **This is the one real inconsistency in the unit. Either the curve gets a
   longer boiling step or the text stops claiming one. Ruling wanted.**
3. **Latent heat named in the stretch only**, not in the main body. Confirm that
   is the right level.
4. **Joseph Black and Watt** (`c7-01` stretch). Historically sound. Confirm the
   nature-of-science content is wanted here.
5. **Temperature figures in `c7-02`**: magnesium 21→60, neutralisation 20→27,
   Mg + acid 20→34, hand warmer 21→50, citric + bicarbonate 20→12. Illustrative
   classroom values, not measured. Confirm you want numbers at all.
6. **Hand warmer described as crystallisation of sodium ethanoate, and flagged
   in-lesson as a change of state rather than a chemical reaction**
   (`c7-02` trial 4). Correct, and the lesson says so rather than hiding it.
   Confirm you want the honesty at KS3.
7. **Iron rusting in a disposable hand warmer** (`c7-02` use 1). Correct.
   Cross-links to C5-03.
8. **Compost heaps at 60 °C and self-igniting hay** (`c7-02` stretch). Both
   real. Confirm the hay fire is not too tangential.
9. **"There is no such thing as cold"** (`c7-03` misconception). Physically
   correct and stated flatly. Confirm you are happy with the bluntness — it is
   the strongest sentence in the unit.
10. **Ammonium nitrate cold packs reaching "near 0 °C"** (`c7-03` stretch).
    Confirm the figure.
11. **Photosynthesis called "the largest endothermic process on Earth"**
    (`c7-03` stretch). Defensible. Confirm.
12. **True value of +7.0 °C** for the neutralisation in `c7-04`, with the best
    achievable rig reading 6.8. The gap is attributed to warming the cup, lid
    and thermometer. Correct in kind; the numbers are invented. Confirm.
13. **Systematic vs random error** (`c7-04` misconception and rung 2). This is
    the most advanced idea in the unit and it is nature-of-science rather than
    chemistry. Confirm it belongs at KS3 — the argument for it is that the
    experiment cannot be honestly evaluated without it.
14. **Bomb calorimeter and food packet calories** (`c7-04` stretch). Confirm.

---

## 5. Misconception register — proposed `ENER` family

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ENER-01` | While ice is melting it has stopped absorbing heat. | `think-commit-plateau` | `think-reveal-latent` | `energy-and-changes-of-state` |
| `ENER-02` | A thermometer measures how much energy something has. | `heating-curve` | `curve-reveal` | `energy-and-changes-of-state` |
| `ENER-03` | A reaction that needs heating to start cannot be exothermic. | `think-commit-spark` | `think-reveal-balance` | `exothermic-reactions` |
| `ENER-04` | Chemical reactions create energy. | `use-3` | `use-3-reveal` | `exothermic-reactions` |
| `ENER-05` | An endothermic reaction produces cold. | `think-commit-cold` | `think-reveal-absence` | `endothermic-reactions` |
| `ENER-06` | Melting and freezing both take energy in, because both involve ice. | `rung-2` | `rung-2-feedback` | `endothermic-reactions` |
| `ENER-07` | Repeating an experiment and averaging makes the result accurate. | `think-commit-average` | `think-reveal-systematic` | `measuring-a-temperature-change` |
| `ENER-08` | Results that agree closely with each other must be correct. | `rung-2` | `rung-2-feedback` | `measuring-a-temperature-change` |

`ENER-07` and `ENER-08` are both `NOS`-shaped and both sit in an energetics
family by accident of build order. That is now eight nature-of-science entries
across five content families. **The `NOS` call is past due** — C5's notes said
the last comfortable moment was before C8, and C8 is now built.

---

## 6. For Code

- Four instruments, all DOM, no canvas, no animation loops.
- Rail stops: five in every lesson.
- SVG arrows in `c7-02`'s start→peak readout; no equations in this unit.
- `c7-01` links back to `c6-07-catalysts.html` and `c7-04` forward to
  `c8-01-metals-and-non-metals.html`. Both exist.
- No props beyond `showDraft`.
- `c7-04`'s `RIGS` lookup is keyed by `vessel|cover|speed`. If a fourth dial is
  ever added the table doubles — worth converting to a computed loss model at
  that point rather than extending the literal.
