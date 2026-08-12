# KS3 diagram manifest

**Generated file — do not hand-edit.** Produced by `build_ks3.py` from the `figures` field on each lesson record. Regenerate with `python3 build_ks3.py`.

architecture.md §4.10, added on Mide's ruling of 2026-07-26 (§11 conflict 1h, ADOPT). MRB-103 caught this gap: the lesson record had nowhere to declare a diagram, so a missing asset could only be discovered at build time. Every figure a lesson declares appears here as a tracked sourcing task.

## ⚠️ Schematic, not photographic

A **Platform Backlog ticket already exists for real-life photography across all subjects.** The KS3 diagram need recorded here is **related but distinct**.

- These are **schematic** assets: particle arrangements, ray diagrams, circuit diagrams, field lines, labelled biological structures.
- A photograph does **not** substitute for one. A photograph of a beaker does not do the job of a particle diagram.
- **Do not merge the two sourcing efforts.** Satisfying the photography ticket will not satisfy this manifest, and vice versa.

MRB-103 also flagged an **anatomical/structural diagram gap** (cells, organs) and put it on the critical path. That gap is real and lands in Biology B1; it is one of the reasons C1 rather than B1 is the vertical slice (§11 conflict 1a).

## Status counts

| Status | Figures |
|---|---|
| `needed` | 27 |
| **Total** | **27** |

`needed` = declared by a lesson, not yet drawn. A lesson may ship with figures at `needed` — it is not a build blocker — but the need is then counted here rather than invisible.

## Figures

| Unit | Lesson | Figure ID | Kind | Status | Caption |
|---|---|---|---|---|---|
| B1 | `animal-and-plant-cells` | `b1-animal-cell-labelled` | schematic | `needed` | An animal cell with the membrane, cytoplasm, nucleus and mitochondria labelled. |
| B1 | `animal-and-plant-cells` | `b1-cheek-onion-micrograph` | micrograph | `needed` | Cheek cells and onion cells side by side at the same magnification. |
| B1 | `animal-and-plant-cells` | `b1-plant-cell-labelled` | schematic | `needed` | A plant cell with all seven parts labelled, drawn beside an animal cell at the same scale. |
| B1 | `levels-of-organisation` | `b1-organisation-ladder` | schematic | `needed` | One example carried up all five levels: muscle cell → muscle tissue → stomach → digestive system → human. |
| B1 | `levels-of-organisation` | `b1-plant-organisation` | schematic | `needed` | The same five levels in a plant: palisade cell → palisade tissue → leaf → shoot system → whole plant. |
| B1 | `levels-of-organisation` | `b1-stomach-wall-layers` | micrograph | `needed` | A section through the stomach wall showing three different tissue layers stacked on each other. |
| B1 | `life-processes` | `b1-everything-is-cells` | micrograph | `needed` | Three specimens at the same magnification — a leaf, human skin and pond water — each one made of cells. |
| B1 | `life-processes` | `b1-three-dishes` | apparatus | `needed` | Three dishes side by side: a dry seed, a crystal growing in salty water, and yeast frothing in sugar water. |
| B1 | `specialised-cells` | `b1-diffusion-distance` | schematic | `needed` | A small cell and a large cell side by side, with the distance from the surface to the centre marked on each. |
| B1 | `specialised-cells` | `b1-red-blood-cell-section` | schematic | `needed` | A red blood cell face on and in section, with the dip in the middle marked and arrows showing oxygen crossing the membrane. |
| B1 | `specialised-cells` | `b1-specialised-cells-set` | schematic | `needed` | Six specialised cells drawn to the same scale, each labelled with the one feature that fits its job: red blood cell, nerve cell, sperm cell, root hair cell, palisade cell, muscle fibre. |
| B1 | `unicellular-organisms` | `b1-pond-water-micrograph` | micrograph | `needed` | A field of pond water at ×100 with a Euglena, an Amoeba and a Paramecium in view at once. |
| B1 | `unicellular-organisms` | `b1-unicellular-adaptations` | schematic | `needed` | Euglena, Amoeba, Paramecium and a bacterium drawn to the same scale, each labelled with its structural adaptations. |
| B1 | `using-a-microscope` | `b1-bubbles-vs-cells` | micrograph | `needed` | The same onion slide twice: a field full of air bubbles with thick dark rims, and a field of onion cells packed in a brick-wall pattern. |
| B1 | `using-a-microscope` | `b1-drawing-standards` | schematic | `needed` | Two drawings of the same onion cells: one shaded, in biro, with crossing label lines; one in sharp pencil with straight ruled labels and no shading. |
| B1 | `using-a-microscope` | `b1-microscope-labelled` | schematic | `needed` | A light microscope with the eyepiece, objective lenses, stage, clips, light source and both focus wheels labelled. |
| C1 | `changes-of-state` | `c1-sealed-bag` | apparatus | `needed` | Sealed bag with ice on a balance, before and after. |
| C1 | `changes-of-state` | `c1-state-change-map` | schematic | `needed` | The six changes of state as arrows between solid, liquid and gas. |
| C1 | `diffusion` | `c1-bromine-jars` | apparatus | `needed` | Two gas jars, bromine below air, before and after the cover slip is removed. |
| C1 | `diffusion` | `c1-diffusion-gradient` | schematic | `needed` | Particles spreading from a region of high concentration to low, shown at three times. |
| C1 | `gas-pressure` | `c1-gas-pressure-collisions` | schematic | `needed` | Gas particles colliding with the walls of a container, with one collision arrowed. |
| C1 | `gas-pressure` | `c1-vacuum-marshmallow` | apparatus | `needed` | Marshmallow in a bell jar, before and after pumping. |
| C1 | `particle-model` | `c1-mixing-volumes` | apparatus | `needed` | Two measuring cylinders, before and after mixing. |
| C1 | `particle-model` | `c1-particles-three-states` | schematic | `needed` | Particles drawn as circles in a solid, a liquid and a gas. |
| C1 | `solids-liquids-and-gases` | `c1-arrangement-compare` | schematic | `needed` | Particle arrangement, movement and spacing in the three states, side by side. |
| C1 | `testing-the-model` | `c1-ice-water-density` | graph | `needed` | Density of water against temperature, showing the maximum at 4 °C. |
| C1 | `testing-the-model` | `c1-model-scorecard` | schematic | `needed` | A scorecard of observations against whether the simple particle model explains them. |
