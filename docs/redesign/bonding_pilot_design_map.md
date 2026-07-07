# Chemistry Bonding — Design Pilot

**Unit:** AQA 5.2 Bonding, structure and the properties of matter
**Purpose:** prove the archetype-plus-map pipeline on one unit before scaling to the whole site.

## How this document is used

1. **Design** builds each archetype below **once**, to full quality, as a runnable parametrised component (working HTML/CSS/JS, not a mockup). It also builds the shared page chrome and tokens.
2. **Code** reads those components off disk and **assembles** each Bonding page per the map in Part 2: the right archetypes, in the right number, configured to the page content, wired into `generate_site_v5.py`, output to `mrbadmus_site/`.

Design supplies taste. Code supplies assembly. Neither does the other's job.

Each archetype lists a **config** line: the data contract, i.e. what varies per page. That is what lets Code instantiate the same component differently on different pages without redesigning it.

---

## Part 1 — Archetype library (20)

### Structure and particles

**1. State Toggle Lab** — switch state or condition; the structure re-renders and a live verdict updates.
*Interaction:* pick solid / molten / in solution, lattice responds, conduction verdict shown.
*Best for:* property-depends-on-state concepts.
*Config:* particle set + charges, list of states, per-state arrangement rule, per-state verdict text.
*(This is your ionic lattice lab. Already built.)*

**2. Particle Motion Sim** — animated particles at a chosen state or temperature, showing arrangement and motion.
*Best for:* states of matter, changes of state, kinetic ideas.
*Config:* states available, particle count, motion behaviour per state, descriptor text.

**3. Dot-and-Cross Stepper** — step through electron transfer (ionic) or sharing (covalent), one move per step.
*Best for:* the bonding mechanism itself.
*Config:* species, bond type (transfer/share), ordered step sequence, final structure. Reuses your SVG dot-and-cross house style.

**4. Structure Hotspot** — tap regions of a structure to reveal how that feature explains a property.
*Best for:* structure-to-property reasoning (the core exam skill in this unit).
*Config:* base diagram (your SVGs), hotspot coordinates, reveal text per hotspot.

**5. Build-a-Structure** — assemble atoms or ions into a valid structure; resulting properties update live.
*Best for:* covalent molecules, giant structures.
*Config:* available atoms/ions, valid targets, property outputs per target.

**6. Zoom / Scale Explorer** — zoom from bulk to particle to atom; content changes per scale level.
*Best for:* nanoparticles, graphene "one atom thick", surface-area-to-volume.
*Config:* scale levels, content and visual per level.

**7. Two-State Compare** — flip between two scenarios shown with cause and effect.
*Best for:* pure vs alloy, conductor vs insulator, delocalised electrons on/off.
*Config:* state A + state B, visual and caption for each.

### Graphs and values

**8. Energy Profile Plotter** — reaction-coordinate diagram with exo/endo toggle, Ea and ΔH markers.
*Best for:* energy changes (your exo/endo page).
*Config:* type, activation energy, enthalpy sign, labels.

**9. Annotated Graph Reader** — a graph with guided callouts and questions.
*Best for:* heating/cooling curves, solubility curves.
*Config:* graph data, callout points, prompts.

**10. Slider Relationship** — drag a variable; a graph or outcome responds live with a readout.
*Best for:* size vs boiling point, concentration vs rate.
*Config:* variable, range, response function, readout text.

**11. Calculator / Value Check** — enter or compute a value; instant checked feedback.
*Best for:* Mr, surface-area-to-volume ratio, conservation of mass.
*Config:* inputs, formula, worked feedback.

### Sort, match, retrieve

**12. Categorise Bins** — tap or drag cards into two or more bins, then check.
*Best for:* classify by bond type, exo vs endo.
*Config:* items, bins, correct mapping, feedback.
*(This is your Sort-it activity.)*

**13. Sequencing / Order-it** — arrange steps into the correct order.
*Best for:* multi-stage processes.
*Config:* items, correct order.

**14. Matching Pairs** — connect terms to definitions or examples.
*Best for:* vocabulary, term-to-example links.
*Config:* left set, right set, correct pairs.

**15. Flip / Reveal Cards** — term or question on front, answer on flip.
*Best for:* retrieval practice.
*Config:* card pairs.

**16. True-False / Misconception Buster** — judge statements, reveal why.
*Best for:* targeting common exam errors.
*Config:* statements, verdicts, explanations.

**17. MCQ Check** — inline multiple choice with instant feedback and explanation.
*Best for:* quick knowledge checks anywhere.
*Config:* questions, options, correct answer, feedback.

### Prose replacement and navigation

**18. Concept Stepper** — step-through explanation, one idea per step; replaces the prose blob.
*Best for:* any page currently carrying a wall of text.
*Config:* ordered steps, each with text and optional visual.
*(This is your typed-segment stepper idea.)*

**19. Tabbed Explainer** — 2 to 4 tabs switching related sub-explanations inside one card.
*Best for:* a property set (melting / conducting / brittle) without stacking four cards.
*Config:* tab labels, content per tab.

**20. Labelled Diagram Builder** — drag labels onto a diagram, check placement.
*Best for:* exam diagram literacy.
*Config:* base diagram (your SVGs), label set, correct positions.

---

## Part 2 — Chemistry Bonding page map

Deliberately varied. Interactive count in brackets. "Static" means a house-style SVG you already have, no interactive needed.

**1. Chemical bonds: the three types** — 5.2.1.1 — Foundation base — **(2)**
Categorise Bins (classify examples: metal + non-metal to ionic, etc.) + Concept Stepper (how to decide bond type).
*Why:* a decision-rule page. Sorting plus guided logic beats prose.

**2. Ionic bonding** — 5.2.1.2 — Foundation base — **(1)**
Dot-and-Cross Stepper (Na + Cl to NaCl transfer). Static: your ionic dot-and-cross SVGs alongside.
*Why:* the mechanism is the whole point, so step it.

**3. Ionic compounds / giant ionic lattice** — 5.2.1.3 — Higher flag — **(1)**
State Toggle Lab (already built). Properties as static cards (as in your screenshot).
*Why:* one strong lab carries the page; the property cards read fine static. A restraint example.

**4. Covalent bonding** — 5.2.1.4 — Foundation base — **(1 to 2)**
Dot-and-Cross Stepper (H₂, Cl₂, H₂O, CH₄, NH₃) + optional Build-a-Structure.
*Why:* sharing mechanism first; build is a nice extension, not required.

**5. Metallic bonding** — 5.2.1.5 — Foundation base — **(1)**
Two-State Compare (delocalised electrons on/off to conduction and malleability). Static: your metallic_bonding SVG.
*Why:* the sea-of-electrons idea lands best as a compare.

**6. The three states of matter** — 5.2.2.1 — Foundation base — **(2)**
Particle Motion Sim + Annotated Graph Reader (heating/cooling curve).
*Why:* motion and the curve are both core and both visual. A genuinely rich page.

**7. State symbols** — 5.2.2.2 — Foundation base — **(0 to 1)**
Optional MCQ Check or Matching Pairs. Otherwise static.
*Why:* a small factual page. A quick check is plenty, or leave it clean. The near-zero example.

**8. Properties of small molecules** — 5.2.2.4 — Foundation base — **(1)**
Tabbed Explainer (low melting point / no conduction) or Two-State Compare vs giant structures. Static: simple_molecular SVG.
*Why:* the contrast with giant structures is the learning.

**9. Polymers** — 5.2.2.5 — Foundation base — **(0 to 1)**
Optional Structure Hotspot on the chain. Static: polymer SVG.
*Why:* mostly a labelled structure. Keep it light.

**10. Giant covalent: diamond, graphite, silica** — 5.2.2.6 / 5.2.3.1 / 5.2.3.2 — Foundation base — **(2)**
Structure Hotspot (structure to property) + Two-State Compare (diamond hard/insulator vs graphite soft/conductor). Static: diamond, graphite, silicon_dioxide SVGs.
*Why:* property-from-structure is the examined skill; the hotspot nails it.

**11. Graphene and fullerenes** — 5.2.3.3 — Triple / Higher flag — **(1)**
Zoom / Scale Explorer (one atom thick; C₆₀; nanotube). Static: graphene, fullerene, nanotube SVGs.
*Why:* scale is the wow factor. Zoom communicates "one atom thick" in a way text cannot.

**12. Properties of metals and alloys** — 5.2.2.7 — Foundation base — **(1)**
Two-State Compare (pure metal layers slide vs alloy layers blocked).
*Why:* the sliding-layers mechanism is best animated as a compare.

**13. Metals as conductors** — 5.2.2.8 — Foundation base — **(0 to 1)**
Optional Two-State Compare (electrons carrying charge). May fold into page 5.
*Why:* likely a short page; possibly merged.

**14. Nanoparticles** — 5.2.4 — Higher / Triple flag — **(2)**
Zoom / Scale Explorer + Calculator / Value Check (surface-area-to-volume ratio).
*Why:* scale and the SA:V calculation are both examinable.

---

## Part 3 — What I need you to confirm

1. **Exact page split.** This map follows the AQA subtopics confirmed by your diagram library. Your generator may merge or split some: Properties of ionic compounds (5.2.2.3) likely lives on page 3; Metals as conductors (page 13) may fold into Metallic bonding (page 5). Confirm the real page list and I lock the map to it.
2. **Tier flags.** I have marked the obvious Higher / Triple pages. Confirm against your `higher` and `triple_only` fields.
3. **Static diagram palette.** Your SVG libraries use the older house style (sage, salmon, Georgia serif). The new redesign is cream, white cards, burnt-orange, Fraunces. During the Design library phase we should refresh the SVG palette to the new tokens so static diagrams and interactives do not clash on the same page.

## Part 4 — Next steps

1. You confirm Part 3.
2. **Design** builds the archetypes flagged in this map (not all 20 for the pilot, only the ones Bonding actually uses: roughly 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 18, 19). Plus chrome and tokens.
3. **Code** assembles the 14 pages per this map, wires the generator, outputs to `mrbadmus_site/`.
4. We review the real pages, confirm the pattern holds, then scale the same audit to the next unit.
