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
| `drafted` | 1 |
| `drawn` | 3 |
| `final` | 1 |
| `needed` | 15 |
| **Total** | **20** |

`needed` = declared by a lesson, not yet drawn. A lesson may ship with figures at `needed` — it is not a build blocker — but the need is then counted here rather than invisible.

## Figures

| Unit | Lesson | Figure ID | Kind | Status | Caption |
|---|---|---|---|---|---|
| B1 | `animal-and-plant-cells` | `b1-cell-bench` | css-art | `drafted` | The cell bench drawing: a leaf cell and a cheek cell, each as a textbook drawing and as a ×400 field of view. |
| B1 | `life-processes` | `b1-candle-flame` | css-art | `final` | A burning candle: a flickering flame above the wick, with soot rising from it. |
| B1 | `using-a-microscope` | `b1-onion-epidermis-x100` | micrograph | `needed` | Onion epidermis, ×100. Cells countable, edges sharp. |
| B1 | `using-a-microscope` | `b1-onion-epidermis-x400` | micrograph | `needed` | The same spot, ×400. One cell wall crossing an empty grey field. |
| B10 | `how-we-worked-out-dna` | `b10-base-pairs` | diagram | `drawn` | A always with T, C always with G — and the reason is width. A and G are the big bases, C and T the small ones, so every rung is one big and one small and every rung comes out the same length. Two big bases would bulge; two small ones would pinch. |
| B3 | `absorption-and-the-small-intestine` | `b3-villus-labelled` | diagram | `needed` | A single villus, labelled: the wall one cell thick, the capillary network running through it, and the microvilli on the outer surface of each covering cell. |
| B3 | `the-digestive-system` | `b3-gut-labelled` | diagram | `needed` | The human digestive system, labelled: mouth, oesophagus, stomach, small intestine, large intestine, rectum and anus, with the pancreas, liver and gall bladder shown feeding into the small intestine without food passing through them. |
| B4 | `the-gas-exchange-system` | `b4-gas-exchange-labelled` | diagram | `needed` | The human gas exchange system, labelled: nose and mouth, trachea, bronchi, bronchioles and alveoli, with the ribs, intercostal muscles and diaphragm drawn around the lungs rather than as part of the airway. |
| B5 | `fertilisation-seeds-and-fruit` | `b5-pollen-tube` | diagram | `needed` | A pollen grain on the stigma, the pollen tube extending down through the style, and the male gamete nucleus reaching an ovule inside the ovary. |
| B5 | `flowers-and-pollination` | `b5-flower-parts-labelled` | diagram | `needed` | A generalised flower cut in half and labelled: sepal and petal on the outside, the anther and filament together as the stamen, the stigma, style, ovary and ovules together as the carpel, and the nectary at the base. |
| B5 | `flowers-and-pollination` | `b5-wind-vs-insect` | diagram | `needed` | An insect-pollinated flower and a wind-pollinated flower side by side, showing petals, nectary, the position of the anthers, the texture of the stigma and the grains of pollen for each. |
| B5 | `gametes-and-fertilisation` | `b5-gametes-labelled` | diagram | `needed` | A sperm cell and an egg cell drawn to the same scale and labelled: the sperm’s head, mitochondria and tail, and the egg’s nucleus, cytoplasm, food store and outer layer, with each cell’s diameter given — about 0.005 mm and about 0.1 mm. |
| B5 | `gestation-placenta-and-birth` | `b5-placenta-exchange` | diagram | `needed` | The placenta drawn as an exchange surface: the mother's blood on one side, the foetus's blood on the other in the folded finger-like projections, the two brought within a fraction of a millimetre and never joined, with the umbilical cord carrying the foetus's own blood to and from it. Arrows labelled for direction — oxygen and glucose crossing in, carbon dioxide and urea crossing out. |
| B5 | `human-reproductive-systems` | `b5-female-system-labelled` | diagram | `needed` | The female reproductive system, labelled: the ovaries, the oviducts, the uterus, the cervix and the vagina. |
| B5 | `human-reproductive-systems` | `b5-male-system-labelled` | diagram | `needed` | The male reproductive system, labelled: the testes, the sperm duct, the glands that add fluid, the urethra and the penis. |
| B5 | `lifestyle-and-the-developing-foetus` | `b5-what-crosses` | diagram | `needed` | What crosses the placenta and what does not: small soluble molecules — oxygen, glucose, alcohol, nicotine, carbon monoxide, caffeine — diffusing across the exchange surface, with large molecules such as insulin shown too big to pass and antibodies shown carried across using energy. The two blood supplies are drawn separately and never mixing. |
| B5 | `seed-dispersal` | `b5-dispersal-specimens` | diagram | `needed` | The eight specimens drawn to scale from their structures and left unlabelled by method: dandelion, sycamore key, poppy capsule, blackberry, goosegrass, burdock burr, coconut and gorse pod. |
| B5 | `the-menstrual-cycle` | `b5-cycle-timeline` | diagram | `needed` | One cycle drawn as a timeline for each of the three lengths, 21, 28 and 35 days: the bleeding window at the start, the building phase, release a fortnight before the end, and the fortnight in which the lining is held ready — with the release marker landing on a different day in each of the three. |
| B9 | `disturbing-a-food-web` | `b9-oak-wood-web` | diagram | `drawn` | The wood, before anything is taken out of it. Count the arrows into and out of each organism before you choose one to remove — the ones with a single line are not always the ones that matter least. |
| B9 | `food-chains-and-food-webs` | `b9-oak-wood-web-thread` | diagram | `drawn` | One oak wood. Every arrow points the way the energy travels, from the eaten to the eater. The numbered orange chain is one route through it — the same four steps the bench above climbs. |
