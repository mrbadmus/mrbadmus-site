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
| `final` | 1 |
| `needed` | 4 |
| **Total** | **6** |

`needed` = declared by a lesson, not yet drawn. A lesson may ship with figures at `needed` — it is not a build blocker — but the need is then counted here rather than invisible.

## Figures

| Unit | Lesson | Figure ID | Kind | Status | Caption |
|---|---|---|---|---|---|
| B1 | `animal-and-plant-cells` | `b1-cell-bench` | css-art | `drafted` | The cell bench drawing: a leaf cell and a cheek cell, each as a textbook drawing and as a ×400 field of view. |
| B1 | `life-processes` | `b1-candle-flame` | css-art | `final` | A burning candle: a flickering flame above the wick, with soot rising from it. |
| B1 | `using-a-microscope` | `b1-onion-epidermis-x100` | micrograph | `needed` | Onion epidermis, ×100. Cells countable, edges sharp. |
| B1 | `using-a-microscope` | `b1-onion-epidermis-x400` | micrograph | `needed` | The same spot, ×400. One cell wall crossing an empty grey field. |
| B3 | `absorption-and-the-small-intestine` | `b3-villus-labelled` | diagram | `needed` | A single villus, labelled: the wall one cell thick, the capillary network running through it, and the microvilli on the outer surface of each covering cell. |
| B3 | `the-digestive-system` | `b3-gut-labelled` | diagram | `needed` | The human digestive system, labelled: mouth, oesophagus, stomach, small intestine, large intestine, rectum and anus, with the pancreas, liver and gall bladder shown feeding into the small intestine without food passing through them. |
