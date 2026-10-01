# Batch 8 — diagram library audit

Method: grepped `figlib/biology.py`, `figlib/biochem.py`, `figlib/chemistry.py`,
`figlib/physics.py`, `figlib/ks4phys.py`, `figlib/charts.py`,
`shared/ks4-diagrams.js`, `ks3_art/*.py` and `ks4_lessons/authored/batch-2/`
+ `batch-3/*.dc.html` for function names and docstrings naming each lesson's
subject matter, then read the matching function/docstring to confirm it is a
real match and not a substring collision. Near-hits checked and ruled out:
`ks4_lessons/authored/batch-2/lenses.dc.html` links forward to `the-eye` and
`defects-of-the-eye` by slug (`K.hrefFor('the-eye', R)` /
`K.hrefFor('defects-of-the-eye', R)`) — a forward-reference to pages that do
not yet exist, not drawing code, same pattern as batch-6's stem-cells link.
`ks3_art/b10.py`'s `_punnett_gamete()`/`_punnett()` (Punnett-square genetics
bench) and `figlib/biology.py:60 punnett_square()` both draw genetic-cross
content for the genetic-inheritance lesson (Batch 9), not for this batch's
meiosis/sexual-reproduction content — ruled out as the wrong lesson's figure,
not a substring collision. `shared/ks4-diagrams.js` was checked in full and
remains entirely circuit-symbol and bonding/particle-model primitives —
nothing in it concerns any Batch-8 topic; listed here as checked, not cited
again below.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | homeostasis | None found anywhere searched. No generic receptor → coordination-centre → effector figure exists anywhere (figlib, ks3_art) — the closest KS3 near-hit, `ks3_art/b3.py`'s `r_system_switch`, is wired to a one-off immune-system scenario (already ruled out for an identical reason in batch-6's principles-of-organisation row) and does not concern homeostasis at all. |
| 2 | nervous-system | **Direct match:** `figlib/biology.py:517 reflex_arc()` — "Box-and-arrow diagram of a reflex arc" — covers the CNS/neurone pathway this lesson teaches (stimulus → receptor → sensory neurone → CNS → motor neurone → effector), though it is built around the reflex-specific wiring rather than voluntary-action pathways generally. |
| 3 | reflex-actions | **Direct match:** `figlib/biology.py:517 reflex_arc()` — exactly this lesson's content, a reflex arc box-and-arrow diagram. |
| 4 | reaction-time | None found anywhere searched for the ruler-drop practical itself. `figlib/charts.py:352 line_graph()` is a generic chart builder, reusable for a reaction-time-vs-condition (e.g. caffeine/distraction) bar comparison, not reaction-time-specific. |
| 5 | the-brain | None found anywhere searched. No cerebrum/cerebellum/medulla region-to-function figure exists. |
| 6 | the-eye | **Reusable KS3 instrument:** `ks3_art/p7.py:835 r_eye_camera()` — "one scene, two ways of catching it" — a KS3 interactive bench comparing the eye to a pinhole camera (aperture/pupil, lens, back surface, inverted image), drawn as a DOM instrument for a different key stage's bench, not a KS4-styled static labelled-eye figure. No `eye_anatomy()`-type figure (cornea/iris/lens/retina/ciliary muscles labelled) exists anywhere. |
| 7 | defects-of-the-eye | None found anywhere searched. No myopia/hyperopia ray-diagram or corrective-lens figure exists; `figlib/physics.py:2138 convex_lens()` is a generic optics lens figure (no eye context) — a genuine near-hit worth opening for reusable lens-ray-drawing style, not an eye-defect figure itself. |
| 8 | thermoregulation | None found anywhere searched. No vasodilation/vasoconstriction/sweating/shivering figure exists in figlib or ks3_art. |
| 9 | endocrine-system | **Direct match:** `figlib/biochem.py:329 body_glands()` — "a simple human head-and-body outline with four glands drawn as small [shapes]" — exactly this lesson's gland-location content. |
| 10 | blood-glucose-diabetes | None found anywhere searched. No insulin/glucagon negative-feedback loop or pancreas figure exists. |
| 11 | human-reproduction-hormones | **Reusable, contingent match:** `figlib/biochem.py:82 cycle_clock()` — "a circle with `days` evenly spaced ticks running clockwise... direction of time" — a generic cyclical-time figure with no existing caller anywhere in the codebase (checked), reusable for the 28-day menstrual cycle and when FSH/LH/oestrogen/progesterone peak, but not currently wired to any hormone content. |
| 12 | contraception-fertility | None found anywhere searched. No contraceptive-method classification or IVF-stages figure exists. |
| 13 | sexual-asexual-reproduction | **Sibling lesson, not drawing code for this one:** `ks4_lessons/authored/batch-2/chromosomes-mitosis.dc.html` is the sibling KS4 lesson "Chromosomes and Mitosis" and substantively contrasts mitosis (asexual: one parent, clone) against meiosis (sexual: gametes, variation) in its own activities — worth opening for content/style consistency, but it is that lesson's own delivery, not a reusable figure. `ks3_art/b5.py:3611 r_gamete_compare()` ("six features of two cells") is a KS3 sperm-vs-egg comparison-table instrument — a genuine near-hit for the gametes angle of this lesson, drawn as a DOM table for a different key stage's bench. |
| 14 | meiosis | **Partial/near match:** `figlib/biology.py:423 mitosis_stages()` — "Five-panel strip of mitosis stages" — draws MITOSIS, the two-divisions-to-four-haploid-cells process this lesson teaches is a different division entirely (meiosis), so this figure does not cover meiosis itself; useful only as a visual-style reference for a sibling cell-division strip. No `meiosis_stages()` figure exists. |
| 15 | advantages-sexual-asexual | None found anywhere searched. No variation-vs-speed comparison figure exists specific to this contrast. |
| 16 | dna-genome | **Direct match:** `figlib/biology.py:353 dna_schematic()` ("DNA as a ladder with sugar-phosphate backbone and base pairs") and `figlib/biology.py:811 dna_ladder()` ("DNA untwisted into a ladder... every rung the same width") — both cover this lesson's gene/DNA/chromosome content directly. |

## Figures still needed

1. **homeostasis** — a general, reusable receptor → coordination centre (CNS/endocrine) → effector feedback-loop figure, distinct from `r_system_switch`'s one-off wiring, since no such figure exists anywhere in the estate.
2. **nervous-system** — (contingent on reusing `reflex_arc()`) a CNS-and-neurones overview figure: sensory/relay/motor neurones, synapse, and the voluntary pathway alongside the reflex pathway already drawn.
3. **reflex-actions** — none needed; `reflex_arc()` already covers this lesson directly.
4. **reaction-time** — a labelled ruler-drop set-up figure (ruler held vertically, thumb/finger at 0 cm, distance fallen) matching this lesson's one FIFA and its ruler-drop method (currently inside `theory`, not a dedicated `rp` field — see extraction notes).
5. **the-brain** — a labelled brain-regions figure (cerebrum, cerebellum, medulla) each paired with its function, plus a one-line note on MRI/CT/PET scanning and the limits of studying brain damage.
6. **the-eye** — a labelled eye-anatomy figure (cornea, iris, pupil, lens, ciliary muscles, retina, optic nerve), distinct from `r_eye_camera()`'s eye-vs-camera comparison instrument.
7. **defects-of-the-eye** — (contingent on reusing `convex_lens()`'s ray-drawing style) a short-sight vs long-sight ray-diagram pair, each with its corrective lens (concave/convex) shown bringing the image back onto the retina.
8. **thermoregulation** — a too-hot vs too-cold two-branch figure: vasodilation/sweating/hair flat vs vasoconstriction/shivering/hair raised, each effector response labelled.
9. **endocrine-system** — none needed for gland location; `body_glands()` already covers it. A hormonal-vs-nervous contrast figure (speed, duration, how the signal travels) is still needed.
10. **blood-glucose-diabetes** — an insulin/glucagon negative-feedback loop figure centred on the pancreas, liver and blood glucose level, plus a Type 1 vs Type 2 diabetes contrast (no insulin produced vs insulin resistance).
11. **human-reproduction-hormones** — (contingent on reusing `cycle_clock()`) a 28-day menstrual-cycle figure with FSH, LH, oestrogen and progesterone levels marked at the days they peak, and ovulation/menstruation marked on the circle.
12. **contraception-fertility** — a method-classification figure: hormonal (pill, injection, implant, patch) vs barrier (condom, diaphragm) vs surgical (sterilisation) vs natural, each with how it prevents pregnancy, plus an IVF-stages flowchart.
13. **sexual-asexual-reproduction** — a gametes-vs-no-gametes contrast figure: sexual (two parents, fusion of gametes, genetic variation) vs asexual (one parent, mitosis, genetically identical clones).
14. **meiosis** — a two-divisions-to-four-haploid-cells figure (the one genuinely missing figure for this lesson — `mitosis_stages()` draws the wrong division), showing chromosome number halving from 46 to 23 across two divisions.
15. **advantages-sexual-asexual** — a variation-vs-speed balance figure: sexual reproduction's genetic variation (survival advantage) against asexual reproduction's speed and reliability in stable environments.
16. **dna-genome** — none needed; `dna_schematic()`/`dna_ladder()` already cover the DNA structure. A gene → protein → characteristic figure (the MODEL this lesson is built around) is still needed, distinct from the structural ladder figures.
