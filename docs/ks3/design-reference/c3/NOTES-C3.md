# C3 — Mixtures and separation · author's notes

**All seven lessons. The unit is complete.** Everything is draft and unreviewed.

Queue resolution and filename convention: `NOTES-P3.md` §0, unchanged. C3 is the
third Year-7 Chemistry unit by declaration order in `structure.py`.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `pure-or-mixture` | `KS3.C.PIS.01`, `KS3.C.PIS.02` (the mixture half) |
| `dissolving-and-solutions` | `KS3.C.PIS.02` (the dissolving half) |
| `filtration` | `KS3.C.PIS.04` |
| `evaporation-and-crystallisation` | `KS3.C.PIS.04` |
| `distillation` | `KS3.C.PIS.04` |
| `chromatography` | `KS3.C.PIS.04` |
| `proving-something-is-pure` | `KS3.C.PIS.05` |

All five PIS statements are covered. `PIS.03` (diffusion) is C1's and is not
re-covered here. PIS.04 names four techniques and gets four lessons, one each —
the alternative, a single "separating mixtures" lesson, is the thing §4.2 calls
two lessons wearing one title.

PIS.02 is split deliberately: `pure-or-mixture` teaches what a mixture **is**,
`dissolving-and-solutions` teaches the one kind of mixture the statutory
wording singles out. Teaching both in one sitting is what produces students who
think dissolving is the definition of mixing.

---

## 2. What the lessons do

- **`c3-01` (CLASSIFY)** — eight samples, verdict on each. Three of the eight
  are labelled or sold as pure and are mixtures; one is invisible and is pure.
  The flagship is deliberately **not** the C2 test-budget bench: this one is a
  grid of independent commitments, because the teaching point is the repeated
  application of one question, not the economics of evidence.
- **`c3-02` (MODEL)** — the dissolving bench, four dials, and the only lesson
  in the unit with a locked instrument: the predict-gate asks which dial changes
  *how much* dissolves before the bench opens. Salt is on the bench precisely
  because its solubility barely moves with temperature, which breaks the rule
  the student is about to over-learn.
- **`c3-03` (PROCESS)** — worked stepper, then the same five steps shuffled for
  the student to rebuild. Wrong orders are answered with **consequences on the
  bench**, never marks. The particle-scale panel is the load-bearing figure of
  the unit: it is why no filter can hold back salt.
- **`c3-04` (PROCESS)** — a parameter bench rather than a second stepper (§6's
  warning about identical lineups). Three solutes × three methods; the mass
  recovered is identical every time and only the crystals change.
- **`c3-05` (PROCESS)** — a staged run with a thermometer, and the condenser
  cooling as a **switch that can be turned off**: boil to separate, cool to
  collect, and doing one of the two gets you nothing.
- **`c3-06` (PROCESS)** — three method decisions, each with its own failure
  mode, and a forensic payoff. This is the only lesson in the unit where the
  student can produce an unreadable result and be told exactly why.
- **`c3-07` (INVESTIGATION)** — critique before construct, per §6. Four steps
  of somebody else's plan judged first, then messy melting-point data with an
  anomaly that must be reported rather than deleted.

---

## 3. New instrument kinds

### 3.1 `purity-sorter` — `c3-01` (DOM only)
`{samples: [{id, name, look, ingredients, dots, diagramLabel, pure, verdict, why}], verdicts: {}}`
Particle strips are DOM circles, not canvas. Each carries its own aria-label
naming what the diagram shows. Reusable by C8 `metals-and-non-metals` and B1
`animal-and-plant-cells`.

### 3.2 `dissolve-lab` — `c3-02` (DOM only)
`{solute, temp, stir, powder, seen: {}}` → readouts for grams, seconds and
appearance, plus a beaker diagram. **The rate/amount split is the pedagogy.** If
Code lets stirring change the grams the lesson is worthless.

### 3.3 `sequence-rebuild` — `c3-03` (DOM only)
`{steps: [{id, short, title, detail, why, tooSoon}], order: []}`. The
`tooSoon` string per step is what makes it consequence-based. Every PROCESS
lesson in the map can use this; B3 `food-tests` and C6 `making-a-pure-dry-salt`
want it unchanged.

### 3.4 `crystal-bench` — `c3-04`; 3.5 `still-run` — `c3-05`; 3.6 `chroma-run` — `c3-06`; 3.7 `melting-point-bench` — `c3-07`
All DOM. `chroma-run` positions spots by Rᶠ as a percentage of a fixed-height
lane, so a real figure can replace it without changing the payload.
`melting-point-bench` is the one to reuse for any "repeats and anomalies"
lesson — the heating-rate dial is what turns it from a data table into a
Working Scientifically instrument.

---

## 4. Science flags — numbered for review

1. **Sugar solubility figures** (`c3-02`): 190 g / 240 g / 360 g per 100 g water
   at 10 / 40 / 80 °C. Sucrose solubility is steep and the shape is right;
   confirm you are happy with these three values being quoted to three
   significant figures rather than "about 200 g".
2. **Salt solubility barely changing** — 35.8 / 36.4 / 38.1 g. Correct, and it
   is the lesson's best teaching point. Confirm you want it *foregrounded*: it
   contradicts "hot water dissolves more", which many schemes teach as a rule.
3. **Chalk given as "less than 0.01 g"** rather than 0.001 g. Calcium carbonate
   is about 0.0013 g per 100 g. Confirm the rounding.
4. **Dissolving times** in `c3-02` are computed, not measured — a base time per
   solute divided by factors for temperature, stirring and grinding. They are
   plausible and they are not data. Flagged because a student could time a real
   one and get something else.
5. **Gases becoming less soluble when warmed** (`c3-02` stretch). Correct;
   confirm the river/fish example is wanted here as well as in B9.
6. **Filter paper described as a fibre tangle, not a sieve** (`c3-03` stretch),
   with the claim that it retains particles smaller than its widest gap.
   Correct, and unusual for KS3. Confirm it stays.
7. **Reverse osmosis desalination at 3–4 kWh per cubic metre** (`c3-03`,
   `c3-05`). Modern seawater RO plants are around this. Confirm, or give a
   figure you will defend.
8. **Copper sulfate turning white on over-heating** (`c3-04`) — loss of water of
   crystallisation. Correct. Confirm you want water of crystallisation named in
   the stretch layer a year early.
9. **Naica gypsum crystals "metres long", grown over hundreds of thousands of
   years at 58 °C** (`c3-04` stretch). The largest are around 11–12 m. Confirm
   the vagueness is acceptable or give the number.
10. **Salt water boiling at "just over 100 °C", creeping up as it concentrates**
    (`c3-05`). Correct and rarely said at KS3. Confirm.
11. **Ethanol/water distillation described as giving "mostly ethanol"** and
    needing a fractionating column to do better. Correct — a single still cannot
    reach pure ethanol. Confirm the honesty is wanted rather than the usual KS3
    simplification.
12. **"Steam off boiling sea water tastes salty"** (`c3-05` misconception). The
    confrontation distinguishes vapour from carried droplets, and blames the
    method. This is the sharpest thing in the unit and the one I would most want
    checked.
13. **The Rᶠ subscript** in `c3-06` uses `<sub>`, not a Unicode subscript —
    deliberately, after C2 flag 13. Confirm that convention for the whole course.
14. **Melting point of the unknown given as 53 °C** with batch 2 melting 45–52.
    The numbers are constructed to be readable, not taken from a real substance.
    Confirm a nameless "compound P" is acceptable, or name one.
15. **Fast heating making a range read narrower** (`c3-07`). Real and the right
    way round — thermometer lag. Confirm the size of the effect as modelled
    (55% of the range collapsed, +1.5 °C on the end point) is defensible.

---

## 5. Misconception register — proposed `MIX` family

`MIX` is opened by `c3-01`. Same request as `ATOM`: **rule on the family before
the IDs are referenced elsewhere.**

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `MIX-01` | Pure means clean, natural or with nothing added. | `hook-two-labels` | `think-again-juice` | `pure-or-mixture` |
| `MIX-02` | If it looks the same all the way through, it is pure. | `sample-ring` | `sorter-reveal` | `pure-or-mixture`, `proving-something-is-pure` |
| `MIX-03` | Dissolving destroys the solute, or turns it into liquid. | `hook-balance` | `think-again-melting` | `dissolving-and-solutions` |
| `MIX-04` | Stirring harder makes more dissolve. | `gate-which-dial` | `dissolve-lab` | `dissolving-and-solutions` |
| `MIX-05` | Dissolving is melting. | `think-commit-melting` | `think-reveal-melting` | `dissolving-and-solutions` |
| `MIX-06` | Filtered water is clean water. | `think-commit-pond` | `think-reveal-pond` | `filtration` |
| `MIX-07` | A fine enough filter would separate salt from water. | `rung-2-filter` | `particle-panels` | `filtration` |
| `MIX-08` | Evaporated water is gone — destroyed. | `think-commit-water` | `think-reveal-water` | `evaporation-and-crystallisation` |
| `MIX-09` | Faster evaporation gives more product. | `bench-boil-run` | `bench-summary` | `evaporation-and-crystallisation` |
| `MIX-10` | Boiling carries dissolved salt over with the steam. | `think-commit-spray` | `think-reveal-droplets` | `distillation` |
| `MIX-11` | The dye or colour is made by the paper or the solvent. | `hook-black-ink` | `chroma-run` | `chromatography` |
| `MIX-12` | The spot that travels furthest is the one there is most of. | `think-commit-furthest` | `think-reveal-tug` | `chromatography` |
| `MIX-13` | One measurement is enough if it is the right answer. | `think-commit-one-run` | `melting-point-bench` | `proving-something-is-pure` |

`MIX-08` **is `PART-05` in a third costume** — "the puddle dried up", "the mass
went down when it burned", and now "the water evaporated so it is gone". Minted
separately because the confrontation is different (a cold surface, not a sealed
bag), and it should carry a cross-reference rather than pretend to be new.

`MIX-02` is the spine of the unit and it is confronted three times: by the gold
ring and the milk in `c3-01`, by the clear filtrate in `c3-03`, and by the
melting range in `c3-07`.

---

## 6. For Code

- Seven instruments, all DOM. No canvas anywhere in the unit and no animation
  loops, so `prefers-reduced-motion` has nothing to degrade beyond the shared
  arrive transition.
- Rail stops: five in `c3-01`, `c3-03`, `c3-04`, `c3-05` and `c3-07`, six in
  `c3-02`, four in `c3-06`.
- `c3-01` links back to `c2-06-conservation-of-mass.html`; `c3-07` links forward
  to `c4-01-chemical-vs-physical-change.html`. Both exist.
- One declared figure at `needed`: `c3-distillation-apparatus` in `c3-05`,
  rendered as an honest `.ks3-figure-slot` placeholder. The other three
  techniques are taught by instrument and declare no figure — if apparatus
  diagrams are wanted for filtration, crystallisation and chromatography as
  well, say so and I will declare three more.
- Tweakable props: `showParticles` and `revealIngredients` on `c3-01`,
  `demoMode` and `showSolubilityNumbers` on `c3-02`, `requirePourPrediction` on
  `c3-03`, `showTimings` on `c3-04`, `showThermometer` on `c3-05`. `demoMode`
  is the front-of-class dial: it opens the bench without the predict-gate, and
  it should never be the default in a student build.
