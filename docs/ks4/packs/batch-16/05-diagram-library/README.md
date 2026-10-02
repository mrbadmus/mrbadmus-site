# Batch 16 — diagram library audit

Method: grepped `figlib/physics.py`, `figlib/ks4phys.py`, `figlib/ks4elec.py`,
`figlib/charts.py`, `shared/ks4-diagrams.js`, `ks3_art/p*.py` and
`ks4_lessons/authored/batch-2/` + `batch-3/*.dc.html` for function names and
docstrings naming each lesson's subject matter, then read the matching
function's docstring (and signature, where relevant) to confirm a real match
rather than a substring collision. `ks3_art/p*.py` entries are KS3
INTERACTIVE BENCHES (sliders, drag-and-drop, scored instruments), not drawn
figures, so they are cited only as "Reusable, contingent" pedagogical
precedent, never a direct hit — and radioactivity has **no** KS3 unit at all
(AQA's radioactive-decay content starts at KS4), so lessons #1–#8 below have
no KS3 precedent to cite either way. Two authored batch-2/batch-3 lessons
already link forward to this batch's slugs (see `_extract-notes.md` note 10)
— navigation only, not a diagram.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | mass-number-isotopes | **Direct match, two of them:** `figlib/physics.py` `isotope_notation(symbol, mass, atomic, name)` — "Big AZX notation card with labelled parts" — exactly this lesson's "read protons/neutrons/electrons off the nuclear notation" content; and `figlib/ks4phys.py` `nuclide(symbol, mass, atomic, …)` — "A nuclear symbol: the element symbol, its mass number at the upper left and its atomic number at the lower left… NEVER drawn: 'mass number', 'atomic number', 'protons', 'neutrons'" — a bare, unlabelled version built for QUESTION figures (where the labels would give the answer away), as opposed to `isotope_notation()`'s labelled teaching version. The two are complementary: teach with one, question with the other. |
| 2 | nuclear-equations | **Direct match, adjacent:** `figlib/physics.py` `isotope_notation()` draws a single nuclide's AZX card and `atom_diagram(symbol, protons, neutrons)` draws the full atom — both support BUILDING a nuclear equation term by term, but neither draws a complete equation (parent → daughter + ejected particle) as one figure. **Nothing found** for a complete alpha/beta/gamma decay equation figure. |
| 3 | half-lives | **Direct match, exact name:** `figlib/physics.py` `half_life_curve(half_life_min, initial)` — "Exponential decay curve with half-life ticks" — exactly this lesson's content, parametrised for any half-life/initial-activity pair. |
| 4 | radioactive-contamination | **Reusable, contingent:** `figlib/physics.py` `radiation_penetration()` — "Alpha, beta, gamma penetration through paper/aluminium/lead" — establishes WHY contamination (ingested/inhaled source) and irradiation (external exposure) differ in risk by radiation type, but does not draw the contamination-vs-irradiation contrast itself (a person with a source ON/IN them vs a person exposed to a source AT A DISTANCE). **Nothing found** for that contrast directly. |
| 5 | background-radiation | **Reusable, contingent:** no figure draws a background-radiation SOURCES pie/bar (cosmic rays, rocks/radon, medical, nuclear industry, food) or a corrected-count-rate subtraction. `figlib/chemistry.py`'s `atmosphere_pie()` (cited in batch-14) is a proportional pie chart ENGINE that could be adapted, but draws atmospheric composition, not radiation sources — not cited as a match, only as a reusable chart TYPE. |
| 6 | uses-of-nuclear-radiation | **Nothing found anywhere searched.** No figure classifies isotopes by type/half-life against a use (smoke detectors=alpha, medical tracers=gamma/short half-life, thickness gauges=beta) anywhere in `figlib`, `ks3_art` or `shared/ks4-diagrams.js`. |
| 7 | nuclear-fission | **Reusable, contingent:** `radiation_penetration()` and `atom_diagram()` (cited above) give the component pieces (a nucleus, ejected particles) but no figure draws a chain reaction (neutron → nucleus splits → more neutrons → more splits). **Nothing found** for a chain-reaction diagram. |
| 8 | nuclear-fusion | **Nothing found anywhere searched.** No figure exists for two light nuclei merging into a heavier one (e.g. hydrogen → helium), the contrast this lesson needs against fission. |
| 9 | scalar-vector-quantities | **Nothing found anywhere searched** for a scalar-vs-vector classification figure (e.g. a quantity list sorted into two columns, or a magnitude-only vs magnitude-and-direction contrast drawing). `figlib/physics.py` `resolution_triangle()` and `figlib/ks4phys.py` `force_grid_2d()` (cited under #13) both draw vectors but assume the scalar/vector distinction has already been taught, rather than teaching it. |
| 10 | contact-noncontact-forces | **Reusable, contingent (KS3 precedent only, not confirmed by reading the function body):** `ks3_art/p4.py` `r_interaction_board` — "p4-01 `#s-bench` — five cases, and the object on the other end" — is the FIRST lesson of the KS3 forces unit and, by its position and description, is a plausible candidate for teaching contact-vs-non-contact exactly as this lesson does; named here as a candidate only, since its full body (what the five cases actually are) was not read to confirm the mechanism. **Nothing found** as a plain KS4 figure. |
| 11 | gravity | **Nothing found anywhere searched** for a dedicated weight-vs-mass or W=mg figure. `figlib/physics.py` `free_body_diagram()` (cited under #14) includes a weight arrow as PART of a larger diagram, but there is no figure built around W = mg on its own. |
| 12 | resultant-forces | **Direct match, exact name:** `figlib/physics.py` `resultant_force()` — "Single object with two horizontal forces and the resultant" — exactly this lesson's balanced/unbalanced-forces content. **Reusable, contingent:** `force_beam(whole, parts)`, `crate_forces(forces)` and `force_grid(arrows)` are general-purpose scaled-force-arrow figures that could also illustrate this lesson with different numbers. |
| 13 | resolving-forces | **Direct match, exact spec point, two of them:** `figlib/physics.py` `resolution_triangle(angle, hyp, horiz, vert, ang_label)` — "A force resolved into two perpendicular components: a right-angled triangle with the right angle marked" — and `figlib/ks4phys.py` `force_grid_2d(arrows, dot, cols, rows, …)` — "Forces drawn TO SCALE on squared paper, from one dot at a grid point… 'use vector diagrams … (scale drawings only)', **AQA 8463 §4.5.1.4**" — the function's own docstring cites the EXACT spec clause BATCH-PLAN lists for this lesson. The two figures cover the two methods AQA expects (trigonometric resolution and scale drawing on squared paper) respectively. |
| 14 | free-body-diagrams | **Direct match, same spec point, two of them:** `figlib/physics.py` `free_body_diagram()` — "Box on a surface with weight, normal reaction, thrust, friction" — a complete, captioned example; and `figlib/ks4phys.py` `free_body(obj, arrows)` — "An object… and its forces as arrows… each labelled at its TIP. All arrows are ink and the same weight, so no arrow is singled out" — a flexible BUILDER for any object/force combination, built for the same AQA 8463 §4.5.1.4 bullet `force_grid_2d()` cites (resolving-forces and free-body-diagrams share one spec point in BATCH-PLAN, and these two functions share the same KS4-specific module). |
| 15 | work-done-energy-transfer | **Nothing found anywhere searched** for a dedicated W = Fs figure (a force moving an object through a distance, with the distance marked). `figlib/physics.py` `force_beam()`/`crate_forces()` draw forces to scale but neither marks a DISTANCE moved — this lesson's genuinely missing element. |
| 16 | forces-elasticity | **Direct match, exact name:** `figlib/physics.py` `hookes_law_graph()` — "Force vs extension for a spring, linear with limit of proportionality" — exactly this lesson's RP18 content. **Reusable, contingent (KS3 precedent only):** `ks3_art/p4.py` `r_spring_plot` ("take the readings, plot them, find where it bends") is the KS3 unit's own spring-RP instrument for the identical practical. |

## Figures still needed

1. **mass-number-isotopes** — none needed; `isotope_notation()` (teaching) and `nuclide()` (questions) already cover it directly.
2. **nuclear-equations** — a complete decay-equation figure (parent nuclide → daughter nuclide + ejected particle, mass/atomic numbers balanced either side of the arrow) — the one genuinely missing figure; the component nuclide cards already exist.
3. **half-lives** — none needed; `half_life_curve()` already covers it directly.
4. **radioactive-contamination** — a contamination-vs-irradiation contrast figure (source on/in a person vs a person exposed at a distance) — the one genuinely missing figure.
5. **background-radiation** — a background-radiation-sources chart (cosmic rays, rocks/radon, medical, nuclear industry, food, by proportion) — genuinely missing; a pie/bar chart engine exists (`figlib/charts.py`, `atmosphere_pie()`-style) but no figure populates it for radiation sources.
6. **uses-of-nuclear-radiation** — a uses-by-isotope-property figure (smoke detector/alpha, medical tracer/gamma + short half-life, thickness gauge/beta — property driving the choice) — genuinely missing.
7. **nuclear-fission** — a chain-reaction diagram (neutron strikes nucleus → splits → releases more neutrons → strikes more nuclei) — genuinely missing.
8. **nuclear-fusion** — a fusion diagram (two light nuclei merging into one heavier nucleus, e.g. hydrogen isotopes → helium) — genuinely missing.
9. **scalar-vector-quantities** — a scalar-vs-vector classification figure (quantities sorted into two columns, or a magnitude-only vs magnitude-and-direction contrast) — genuinely missing.
10. **contact-noncontact-forces** — a contact-vs-non-contact classification figure — possibly already met by the KS3 `r_interaction_board` bench's underlying idea, but that bench is interactive and KS3-only; a plain KS4 figure is still missing.
11. **gravity** — a dedicated W = mg figure (mass labelled, weight arrow labelled, g stated) separate from the larger free-body diagrams — genuinely missing as its own figure.
12. **resultant-forces** — none needed; `resultant_force()` already covers it directly.
13. **resolving-forces** — none needed; `resolution_triangle()` and `force_grid_2d()` already cover both AQA-expected methods directly.
14. **free-body-diagrams** — none needed; `free_body_diagram()` and `free_body()` already cover it directly.
15. **work-done-energy-transfer** — a force-moving-an-object-through-a-marked-distance figure (W = Fs) — genuinely missing.
16. **forces-elasticity** — none needed; `hookes_law_graph()` already covers it directly.

## False near-hits

- **uses-of-nuclear-radiation / background-radiation** — grepped "tracer" across the whole repo for the medical-tracer use case; the only hit, `ks3_art/b6.py`'s `r_route_tracer`, is a Biology KS3 drug-metabolism instrument (an unrelated sense of "tracer") — ruled out by reading its docstring, not cited above.
- **scalar-vector-quantities** — grepped "scalar" across `figlib` and `ks3_art`; the only hits (`ks3_art/b3.py` line 1111, `ks3_art/p10.py` lines 696–707) are Python variable names (a "scalar" accumulator in a magnetism-field calculation and an "opt_ph IS A SET, not a scalar" comment about an authoring API) — neither is a figure about the scalar/vector PHYSICS QUANTITY distinction, and both are ruled out.
- **gravity** — `figlib/physics.py`'s `free_body_diagram()` draws a weight arrow, but only as one of four forces in a larger figure about resultant forces on a surface, not a figure built around W = mg itself — not counted as a direct match for this lesson.
