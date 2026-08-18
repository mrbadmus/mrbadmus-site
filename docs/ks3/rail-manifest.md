# KS3 rail manifest — what Design actually drew

⊕ **MRB-249, 18 Aug 2026.** Generated from Claude Design's delivered lesson
pages (`KS3 B*/ *.dc.html`), not written by hand. One row per lesson, recording
the rail **as Design drew it**: the ordered stop anchors from her `RAIL` const,
and the mirror map derived from her `isDone()`.

## Why this file exists

`ks3_parity.check_rail_reachable` gated whether a rail stop *on our rail* could
tick. It could not see a stop that was never put on our rail at all — and that
is exactly how the defect escaped. Across B3, B4, B5, B6, B7 and B8, **33 pages
shipped a three-stop rail where Design drew four.** Each dropped the same stop:
the synthesis section between the instrument and the ladder.

Those sections are not empty. They are 1.2–5.2 KB of teaching apiece — a drawn
equation, a summary table, a set of fact cards — and every one of them is still
in the built page, keeping its anchor, off the rail. Three separate authoring
passes reasoned that a section with no control of its own "cannot tick" and
dropped it. That reasoning contradicts **MRB-205 — Design draws, we render; the
page wins over the engine** — and it contradicts Design's own code, which says
in plain JavaScript how the stop ticks:

    if (id === 's-bench')   return s.exits;
    if (id === 's-summary') return s.exits;

The synthesis section is the *payoff* of the instrument beside it. It carries no
control because the instrument already took the student's commitment. That is a
**mirror**, it is authored as `mirrors`, and it is resolved at rail level in
`shared/ks3.js` — the same level Design resolves it at.

A gate that only checks the stops we chose to emit cannot catch a stop we chose
not to emit. This manifest is the outside reference that closes that hole:
`check_rail_matches_design` asserts the built rail equals the drawn rail, anchor
for anchor and in order, and fails a lesson that has no row here at all.

## Regenerating

`python3 ks3_rail_manifest.py --write`. It reads Design's delivered pages and
rewrites §1 below. Run it when Design delivers a new unit; never hand-edit rows.

## 1. Drawn rails

| slug | design page | stops | mirrors |
|---|---|---|---|
| `life-processes` | `b1-01-life-processes` | s-hook s-board s-sort s-ladder | — |
| `using-a-microscope` | `b1-02-using-a-microscope` | s-hook s-method s-worked s-yours s-lab s-ladder | — |
| `animal-and-plant-cells` | `b1-03-animal-and-plant-cells` | s-hook s-bench s-wall s-fit s-ladder | — |
| `specialised-cells` | `b1-04-specialised-cells` | s-hook s-tuned s-break s-ladder | — |
| `levels-of-organisation` | `b1-05-levels-of-organisation` | s-hook s-zoom s-hard s-break s-ladder | — |
| `unicellular-organisms` | `b1-06-unicellular-organisms` | s-hook s-scope s-settle s-ladder | — |
| `variation-continuous-and-discontinuous` | `b10-01-variation-continuous-and-discontinuous` | s-hook s-bench s-two s-ladder | s-two=s-bench |
| `chromosomes-genes-and-dna` | `b10-02-chromosomes-genes-and-dna` | s-hook s-bench s-model s-ladder | s-model=s-bench |
| `how-we-worked-out-dna` | `b10-03-how-we-worked-out-dna` | s-hook s-bench s-who s-ladder | s-who=s-bench |
| `passing-it-on-heredity` | `b10-04-passing-it-on-heredity` | s-hook s-bench s-steps s-ladder | s-steps=s-bench |
| `what-makes-a-species` | `b10-05-what-makes-a-species` | s-hook s-bench s-test s-ladder | s-test=s-bench |
| `variation-and-competitive-success` | `b11-01-variation-and-competitive-success` | s-hook s-bench s-three s-ladder | s-three=s-bench |
| `natural-selection` | `b11-02-natural-selection` | s-hook s-bench s-steps s-ladder | s-steps=s-bench |
| `when-the-environment-changes-extinction` | `b11-03-when-the-environment-changes-extinction` | s-hook s-bench s-risk s-ladder | s-risk=s-bench |
| `biodiversity-and-gene-banks` | `b11-04-biodiversity-and-gene-banks` | s-hook s-bench s-banks s-ladder | s-banks=s-bench |
| `what-the-skeleton-does` | `b2-01-what-the-skeleton-does` | s-hook s-switch s-sort s-think s-ladder | — |
| `joints` | `b2-02-joints` | s-hook s-bench s-cases s-think s-ladder | — |
| `antagonistic-muscle-pairs` | `b2-03-antagonistic-muscle-pairs` | s-hook s-bench s-pairs s-think s-ladder | — |
| `biomechanics-forces-in-the-body` | `b2-04-biomechanics-forces-in-the-body` | s-hook s-bench s-build s-meters s-think s-ladder | — |
| `a-balanced-diet` | `b3-01-a-balanced-diet` | s-hook s-plate s-nutrients s-ladder | s-nutrients=s-plate |
| `food-tests` | `b3-02-food-tests` | s-hook s-bench s-limits s-ladder | s-limits=s-bench |
| `energy-in-food-and-what-you-need` | `b3-03-energy-in-food-and-what-you-need` | s-hook s-ledger s-maths s-ladder | s-maths=s-ledger |
| `when-diet-goes-wrong` | `b3-04-when-diet-goes-wrong` | s-hook s-three s-cases s-ladder | s-three=s-hook |
| `the-digestive-system` | `b3-05-the-digestive-system` | s-hook s-journey s-two s-ladder | s-two=s-journey |
| `enzymes-in-digestion` | `b3-06-enzymes-in-digestion` | s-hook s-bench s-three s-ladder | s-three=s-bench |
| `absorption-and-the-small-intestine` | `b3-07-absorption-and-the-small-intestine` | s-hook s-fold s-four s-ladder | s-four=s-fold |
| `bacteria-in-the-gut` | `b3-08-bacteria-in-the-gut` | s-hook s-jobs s-deal s-ladder | s-deal=s-hook |
| `the-gas-exchange-system` | `b4-01-the-gas-exchange-system` | s-hook s-air s-parts s-ladder | s-parts=s-air |
| `how-breathing-works` | `b4-02-how-breathing-works` | s-hook s-model s-limits s-ladder | s-limits=s-model |
| `alveoli-built-for-exchange` | `b4-03-alveoli-built-for-exchange` | s-hook s-gradient s-built s-ladder | s-built=s-gradient |
| `exercise-asthma-and-smoking` | `b4-04-exercise-asthma-and-smoking` | s-hook s-bench s-smoke s-ladder | s-smoke=s-bench |
| `stomata-and-gas-exchange-in-plants` | `b4-05-stomata-and-gas-exchange-in-plants` | s-hook s-ledger s-stomata s-ladder | s-stomata=s-ledger |
| `human-reproductive-systems` | `b5-01-human-reproductive-systems` | s-hook s-jobs s-pair s-ladder | s-pair=s-jobs |
| `gametes-and-fertilisation` | `b5-02-gametes-and-fertilisation` | s-hook s-compare s-fert s-ladder | s-fert=s-compare |
| `the-menstrual-cycle` | `b5-03-the-menstrual-cycle` | s-hook s-dial s-events s-ladder | s-events=s-dial |
| `gestation-placenta-and-birth` | `b5-04-gestation-placenta-and-birth` | s-hook s-cross s-stages s-ladder | s-stages=s-cross |
| `lifestyle-and-the-developing-foetus` | `b5-05-lifestyle-and-the-developing-foetus` | s-hook s-cross s-windows s-ladder | s-windows=s-cross |
| `flowers-and-pollination` | `b5-06-flowers-and-pollination` | s-hook s-parts s-designs s-ladder | s-designs=s-parts |
| `fertilisation-seeds-and-fruit` | `b5-07-fertilisation-seeds-and-fruit` | s-hook s-becomes s-steps s-ladder | s-steps=s-becomes |
| `seed-dispersal` | `b5-08-seed-dispersal` | s-hook s-sort s-methods s-ladder | s-methods=s-sort |
| `what-drugs-do-to-the-body` | `b6-01-what-drugs-do-to-the-body` | s-hook s-dose s-classes s-ladder | s-classes=s-dose |
| `alcohol-and-smoking` | `b6-02-alcohol-and-smoking` | s-hook s-clock s-years s-ladder | s-years=s-clock |
| `substance-misuse-and-decisions` | `b6-03-substance-misuse-and-decisions` | s-hook s-claims s-four s-ladder | s-four=s-claims |
| `the-photosynthesis-reaction` | `b7-01-the-photosynthesis-reaction` | s-hook s-bench s-summary s-ladder | s-summary=s-bench |
| `leaves-built-for-the-job` | `b7-02-leaves-built-for-the-job` | s-hook s-tuner s-features s-ladder | s-features=s-tuner |
| `testing-a-leaf-for-starch` | `b7-03-testing-a-leaf-for-starch` | s-hook s-bench s-method s-ladder | s-method=s-bench |
| `why-almost-all-life-depends-on-it` | `b7-04-why-almost-all-life-depends-on-it` | s-hook s-trace s-jobs s-ladder | s-jobs=s-trace |
| `aerobic-respiration` | `b8-01-aerobic-respiration` | s-hook s-bench s-summary s-ladder | s-summary=s-bench |
| `why-every-cell-respires` | `b8-02-why-every-cell-respires` | s-hook s-bench s-jobs s-ladder | s-jobs=s-bench |
| `anaerobic-respiration-in-humans` | `b8-03-anaerobic-respiration-in-humans` | s-hook s-bench s-equation s-ladder | s-equation=s-bench |
| `fermentation` | `b8-04-fermentation` | s-hook s-bench s-two s-ladder | s-two=s-bench |
| `aerobic-vs-anaerobic` | `b8-05-aerobic-vs-anaerobic` | s-hook s-bench s-table s-ladder | s-table=s-bench |
| `food-chains-and-food-webs` | `b9-01-food-chains-and-food-webs` | s-hook s-bench s-roles s-ladder | s-roles=s-bench |
| `predator-and-prey` | `b9-02-predator-and-prey` | s-hook s-bench s-cycle s-ladder | s-cycle=s-bench |
| `disturbing-a-food-web` | `b9-03-disturbing-a-food-web` | s-hook s-bench s-rules s-ladder | s-rules=s-bench |
| `pollinators-and-food-security` | `b9-04-pollinators-and-food-security` | s-hook s-bench s-who s-ladder | s-who=s-bench |
| `toxic-build-up-in-a-food-chain` | `b9-05-toxic-build-up-in-a-food-chain` | s-hook s-bench s-two s-ladder | s-two=s-bench |
| `sampling-an-ecosystem` | `b9-06-sampling-an-ecosystem` | s-hook s-bench s-rules s-ladder | s-rules=s-bench |
| `particle-model` | `c1-01-particle-model` | s-hook s-cut s-gap s-think s-ladder | — |
| `solids-liquids-and-gases` | `c1-02-solids-liquids-and-gases` | s-hook s-bench s-matrix s-think s-ladder | s-matrix=s-bench |
| `changes-of-state` | `c1-03-changes-of-state` | s-hook s-curve s-bubble s-think s-ladder | — |
| `gas-pressure` | `c1-04-gas-pressure` | s-hook s-bench s-predict s-think s-ladder | — |
| `diffusion` | `c1-05-diffusion` | s-hook s-walk s-think s-scale s-ladder | s-scale=s-think |
| `testing-the-model` | `c1-06-testing-the-model` | s-hook s-bench s-verdict s-history s-ladder | — |
| `the-atom-daltons-model` | `c2-01-the-atom-daltons-model` | s-hook s-model s-scale s-think s-ladder | — |
| `elements` | `c2-02-elements` | s-hook s-bench s-think s-ladder | — |
| `compounds` | `c2-03-compounds` | s-hook s-bench s-sort s-think s-ladder | — |
| `chemical-symbols` | `c2-04-chemical-symbols` | s-hook s-sort s-read s-think s-ladder | — |
| `formulae` | `c2-05-formulae` | s-hook s-builder s-limit s-think s-ladder | — |
| `conservation-of-mass` | `c2-06-conservation-of-mass` | s-hook s-balance s-build s-think s-ladder | — |
