# KS3 statutory register

**Generated file — do not hand-edit.** Source of truth is `ks3_statutory.py` at the repo root; regenerate with `python3 ks3_statutory.py`.

Phase 0 of `docs/ks3/architecture.md` §10.1. Every statutory bullet of the Key stage 3 programme of study, given a permanent ID per §4.4.

**Source.** *National curriculum in England: science programmes of study*, DfE, 2014 (still in force), Key stage 3 section. Bullet text was extracted programmatically from the published HTML and **copied, never retyped**.

**Transcription fingerprint.** `sha256:3d6a2ee2a0c6785a9987c3b6d67fddd58b917377ace53bc7bc127e06627b8b9a` over the concatenated bullet corpus. Re-running the generator re-checks it.

**Independently verified, 2026-07-26.** The register was re-extracted from the live published HTML by a second, independent pass and diffed against this corpus. **All 155 bullets matched**, and the per-discipline counts (B 39 / C 36 / P 62 / WS 18) and the full heading structure were confirmed against the source. **153 of 155 are byte-identical.** The 2 exceptions differ only where the published HTML contains a double space, which this register renders as a single space:

- `KS3.C.EA.05` — published page has two spaces between "of" and "the" in "the composition of the atmosphere"
- `KS3.P.ECT.01` — published page has two spaces between "smaller" and "movement"

No word, symbol or punctuation mark differs anywhere in the corpus. Those two are whitespace artefacts of the published page, not wording, and are recorded here so the gate check is complete rather than silent.

| | Count |
|---|---|
| Biology statements | 39 |
| Chemistry statements | 36 |
| Physics statements | 62 |
| **Subject content total** | **137** |
| Working Scientifically statements | 18 |
| **All statutory statements** | **155** |

## How to read this

- **ID** — permanent (§4.4 rule 1). Once a lesson references it, it never changes meaning. If the statutory document is revised, new IDs are added and old ones marked `superseded`; they are never reused.
- **Statutory statement** — verbatim. Not paraphrased, merged or tidied. This column is what Mide checks against the source document.
- **Proposed owning unit** — ⚠️ **advisory, and NOT part of the transcription gate.** It is this register's reading of architecture.md §7, recorded so coverage becomes computable. Ownership is finally fixed at lesson grain during authoring, not here.

**The single-source rule (§4.4 rule 3).** Every subject-content statement must be owned by exactly one lesson. Zero owners is a coverage hole; two owners is duplicated content. Both are build-blocking defects.

**Working Scientifically is exempt.** WS is taught *through* content (§5.7), tagged per lesson via `ws: []` at strand grain. WS statements are listed here for audit, and are expected to be exercised many times.

**ID scheme blessed by Mide, 2026-07-26** (§11 decision 6, now closed). The §4.4 `KS3.C.PNM.02` form was adopted exactly as specified, including both details Phase 0 flagged: strand = the heading that directly owns the bullets, and `KS3.WS.<STRAND>.<nn>` for Working Scientifically.

**These 155 IDs are therefore permanent.** §4.4 rule 1 now binds: an ID never changes meaning, and a superseded ID is never reused. IDs are still minted in one place (`statement_id()`) so the register regenerates wholesale — but a re-mint is now a **breaking change**, not a routine command. Do not renumber.

---

## Biology

### Structure and function of living organisms

#### Cells and organisation

Strand code `CELLS`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.CELLS.01` | cells as the fundamental unit of living organisms, including how to observe, interpret and record cell structure using a light microscope | B1 |
| `KS3.B.CELLS.02` | the functions of the cell wall, cell membrane, cytoplasm, nucleus, vacuole, mitochondria and chloroplasts | B1 |
| `KS3.B.CELLS.03` | the similarities and differences between plant and animal cells | B1 |
| `KS3.B.CELLS.04` | the role of diffusion in the movement of materials in and between cells | B1 |
| `KS3.B.CELLS.05` | the structural adaptations of some unicellular organisms | B1 |
| `KS3.B.CELLS.06` | the hierarchical organisation of multicellular organisms: from cells to tissues to organs to systems to organisms | B1 |

#### The skeletal and muscular systems

Strand code `SKEL`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.SKEL.01` | the structure and functions of the human skeleton, to include support, protection, movement and making blood cells | B2 |
| `KS3.B.SKEL.02` | biomechanics – the interaction between skeleton and muscles, including the measurement of force exerted by different muscles | B2 |
| `KS3.B.SKEL.03` | the function of muscles and examples of antagonistic muscles | B2 |

#### Nutrition and digestion

Strand code `NUT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.NUT.01` | the content of a healthy human diet: carbohydrates, lipids (fats and oils), proteins, vitamins, minerals, dietary fibre and water, and why each is needed | B3 |
| `KS3.B.NUT.02` | calculations of energy requirements in a healthy daily diet | B3 |
| `KS3.B.NUT.03` | the consequences of imbalances in the diet, including obesity, starvation and deficiency diseases | B3 |
| `KS3.B.NUT.04` | the tissues and organs of the human digestive system, including adaptations to function and how the digestive system digests food (enzymes simply as biological catalysts) | B3 |
| `KS3.B.NUT.05` | the importance of bacteria in the human digestive system | B3 |
| `KS3.B.NUT.06` | plants making carbohydrates in their leaves by photosynthesis and gaining mineral nutrients and water from the soil via their roots | B7 |

#### Gas exchange systems

Strand code `GAS`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.GAS.01` | the structure and functions of the gas exchange system in humans, including adaptations to function | B4 |
| `KS3.B.GAS.02` | the mechanism of breathing to move air in and out of the lungs, using a pressure model to explain the movement of gases, including simple measurements of lung volume | B4 |
| `KS3.B.GAS.03` | the impact of exercise, asthma and smoking on the human gas exchange system | B4 |
| `KS3.B.GAS.04` | the role of leaf stomata in gas exchange in plants | B4 |

#### Reproduction

Strand code `REP`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.REP.01` | reproduction in humans (as an example of a mammal), including the structure and function of the male and female reproductive systems, menstrual cycle (without details of hormones), gametes, fertilisation, gestation and birth, to include the effect of maternal lifestyle on the foetus through the placenta | B5 |
| `KS3.B.REP.02` | reproduction in plants, including flower structure, wind and insect pollination, fertilisation, seed and fruit formation and dispersal, including quantitative investigation of some dispersal mechanisms | B5 |

#### Health

Strand code `HLTH`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.HLTH.01` | the effects of recreational drugs (including substance misuse) on behaviour, health and life processes | B6 |

### Material cycles and energy

#### Photosynthesis

Strand code `PHOT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.PHOT.01` | the reactants in, and products of, photosynthesis, and a word summary for photosynthesis | B7 |
| `KS3.B.PHOT.02` | the dependence of almost all life on Earth on the ability of photosynthetic organisms, such as plants and algae, to use sunlight in photosynthesis to build organic molecules that are an essential energy store and to maintain levels of oxygen and carbon dioxide in the atmosphere | B7 |
| `KS3.B.PHOT.03` | the adaptations of leaves for photosynthesis | B7 |

#### Cellular respiration

Strand code `RESP`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.RESP.01` | aerobic and anaerobic respiration in living organisms, including the breakdown of organic molecules to enable all the other chemical processes necessary for life | B8 |
| `KS3.B.RESP.02` | a word summary for aerobic respiration | B8 |
| `KS3.B.RESP.03` | the process of anaerobic respiration in humans and micro-organisms, including fermentation, and a word summary for anaerobic respiration | B8 |
| `KS3.B.RESP.04` | the differences between aerobic and anaerobic respiration in terms of the reactants, the products formed and the implications for the organism | B8 |

### Interactions and interdependencies

#### Relationships in an ecosystem

Strand code `ECO`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.ECO.01` | the interdependence of organisms in an ecosystem, including food webs and insect pollinated crops | B9 |
| `KS3.B.ECO.02` | the importance of plant reproduction through insect pollination in human food security | B9 |
| `KS3.B.ECO.03` | how organisms affect, and are affected by, their environment, including the accumulation of toxic materials | B9 |

### Genetics and evolution

#### Inheritance, chromosomes, DNA and genes

Strand code `INH`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.B.INH.01` | heredity as the process by which genetic information is transmitted from one generation to the next | B10 |
| `KS3.B.INH.02` | a simple model of chromosomes, genes and DNA in heredity, including the part played by Watson, Crick, Wilkins and Franklin in the development of the DNA model | B10 |
| `KS3.B.INH.03` | differences between species | B10 |
| `KS3.B.INH.04` | the variation between individuals within a species being continuous or discontinuous, to include measurement and graphical representation of variation | B10 |
| `KS3.B.INH.05` | the variation between species and between individuals of the same species meaning some organisms compete more successfully, which can drive natural selection | B11 |
| `KS3.B.INH.06` | changes in the environment which may leave individuals within a species, and some entire species, less well adapted to compete successfully and reproduce, which in turn may lead to extinction | B11 |
| `KS3.B.INH.07` | the importance of maintaining biodiversity and the use of gene banks to preserve hereditary material | B11 |

## Chemistry

### The particulate nature of matter

Strand code `PNM`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.PNM.01` | the properties of the different states of matter (solid, liquid and gas) in terms of the particle model, including gas pressure | C1 |
| `KS3.C.PNM.02` | changes of state in terms of the particle model | C1 |

### Atoms, elements and compounds

Strand code `AEC`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.AEC.01` | a simple (Dalton) atomic model | C2 |
| `KS3.C.AEC.02` | differences between atoms, elements and compounds | C2 |
| `KS3.C.AEC.03` | chemical symbols and formulae for elements and compounds | C2 |
| `KS3.C.AEC.04` | conservation of mass changes of state and chemical reactions | C2 |

### Pure and impure substances

Strand code `PIS`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.PIS.01` | the concept of a pure substance | C3 |
| `KS3.C.PIS.02` | mixtures, including dissolving | C3 |
| `KS3.C.PIS.03` | diffusion in terms of the particle model | C1 |
| `KS3.C.PIS.04` | simple techniques for separating mixtures: filtration, evaporation, distillation and chromatography | C3 |
| `KS3.C.PIS.05` | the identification of pure substances | C3 |

### Chemical reactions

Strand code `CR`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.CR.01` | chemical reactions as the rearrangement of atoms | C4 |
| `KS3.C.CR.02` | representing chemical reactions using formulae and using equations | C4 |
| `KS3.C.CR.03` | combustion, thermal decomposition, oxidation and displacement reactions | C5 |
| `KS3.C.CR.04` | defining acids and alkalis in terms of neutralisation reactions | C6 |
| `KS3.C.CR.05` | the pH scale for measuring acidity/alkalinity; and indicators | C6 |
| `KS3.C.CR.06` | reactions of acids with metals to produce a salt plus hydrogen | C6 |
| `KS3.C.CR.07` | reactions of acids with alkalis to produce a salt plus water | C6 |
| `KS3.C.CR.08` | what catalysts do | C6 |

### Energetics

Strand code `ENER`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.ENER.01` | energy changes on changes of state (qualitative) | C7 |
| `KS3.C.ENER.02` | exothermic and endothermic chemical reactions (qualitative) | C7 |

### The periodic table

Strand code `PT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.PT.01` | the varying physical and chemical properties of different elements | C8 |
| `KS3.C.PT.02` | the principles underpinning the Mendeleev periodic table | C8 |
| `KS3.C.PT.03` | the periodic table: periods and groups; metals and non-metals | C8 |
| `KS3.C.PT.04` | how patterns in reactions can be predicted with reference to the periodic table | C8 |
| `KS3.C.PT.05` | the properties of metals and non-metals | C8 |
| `KS3.C.PT.06` | the chemical properties of metal and non-metal oxides with respect to acidity | C8 |

### Materials

Strand code `MATS`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.MATS.01` | the order of metals and carbon in the reactivity series | C9 |
| `KS3.C.MATS.02` | the use of carbon in obtaining metals from metal oxides | C9 |
| `KS3.C.MATS.03` | properties of ceramics, polymers and composites (qualitative) | C9 |

### Earth and atmosphere

Strand code `EA`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.C.EA.01` | the composition of the Earth | C10 |
| `KS3.C.EA.02` | the structure of the Earth | C10 |
| `KS3.C.EA.03` | the rock cycle and the formation of igneous, sedimentary and metamorphic rocks | C10 |
| `KS3.C.EA.04` | Earth as a source of limited resources and the efficacy of recycling | C10 |
| `KS3.C.EA.05` | the composition of the atmosphere | C10 |
| `KS3.C.EA.06` | the production of carbon dioxide by human activity and the impact on climate | C10 |

## Physics

### Energy

#### Calculation of fuel uses and costs in the domestic context

Strand code `FUEL`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.FUEL.01` | comparing energy values of different foods (from labels) (kJ) | P2 |
| `KS3.P.FUEL.02` | comparing power ratings of appliances in watts (W, kW) | P2 |
| `KS3.P.FUEL.03` | comparing amounts of energy transferred (J, kJ, kW hour) | P2 |
| `KS3.P.FUEL.04` | domestic fuel bills, fuel use and costs | P2 |
| `KS3.P.FUEL.05` | fuels and energy resources | P2 |

#### Energy changes and transfers

Strand code `ECT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.ECT.01` | simple machines give bigger force but at the expense of smaller movement (and vice versa): product of force and displacement unchanged | P1 |
| `KS3.P.ECT.02` | heating and thermal equilibrium: temperature difference between 2 objects leading to energy transfer from the hotter to the cooler one, through contact (conduction) or radiation; such transfers tending to reduce the temperature difference; use of insulators | P1 |
| `KS3.P.ECT.03` | other processes that involve energy transfer: changing motion, dropping an object, completing an electrical circuit, stretching a spring, metabolism of food, burning fuels | P1 |

#### Changes in systems

Strand code `CIS`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.CIS.01` | energy as a quantity that can be quantified and calculated; the total energy has the same value before and after a change | P1 |
| `KS3.P.CIS.02` | comparing the starting with the final conditions of a system and describing increases and decreases in the amounts of energy associated with movements, temperatures, changes in positions in a field, in elastic distortions and in chemical compositions | P1 |
| `KS3.P.CIS.03` | using physical processes and mechanisms, rather than energy, to explain the intermediate steps that bring about such changes | P1 |

### Motion and forces

#### Describing motion

Strand code `MOT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.MOT.01` | speed and the quantitative relationship between average speed, distance and time (speed = distance ÷ time) | P3 |
| `KS3.P.MOT.02` | the representation of a journey on a distance-time graph | P3 |
| `KS3.P.MOT.03` | relative motion: trains and cars passing one another | P3 |

#### Forces

Strand code `FORCES`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.FORCES.01` | forces as pushes or pulls, arising from the interaction between 2 objects | P4 |
| `KS3.P.FORCES.02` | using force arrows in diagrams, adding forces in 1 dimension, balanced and unbalanced forces | P4 |
| `KS3.P.FORCES.03` | moment as the turning effect of a force | P4 |
| `KS3.P.FORCES.04` | forces: associated with deforming objects; stretching and squashing – springs; with rubbing and friction between surfaces, with pushing things out of the way; resistance to motion of air and water | P4 |
| `KS3.P.FORCES.05` | forces measured in newtons, measurements of stretch or compression as force is changed | P4 |
| `KS3.P.FORCES.06` | force-extension linear relation; Hooke’s Law as a special case | P4 |
| `KS3.P.FORCES.07` | work done and energy changes on deformation | P4 |
| `KS3.P.FORCES.08` | non-contact forces: gravity forces acting at a distance on Earth and in space, forces between magnets, and forces due to static electricity | P4 |

#### Pressure in fluids

Strand code `PRES`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.PRES.01` | atmospheric pressure, decreases with increase of height as weight of air above decreases with height | P5 |
| `KS3.P.PRES.02` | pressure in liquids, increasing with depth; upthrust effects, floating and sinking | P5 |
| `KS3.P.PRES.03` | pressure measured by ratio of force over area – acting normal to any surface | P5 |

#### Balanced forces

Strand code `BAL`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.BAL.01` | opposing forces and equilibrium: weight held by stretched spring or supported on a compressed surface | P4 |

#### Forces and motion

Strand code `FMOT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.FMOT.01` | forces being needed to cause objects to stop or start moving, or to change their speed or direction of motion (qualitative only) | P4 |
| `KS3.P.FMOT.02` | change depending on direction of force and its size | P4 |

### Waves

#### Observed waves

Strand code `OBW`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.OBW.01` | waves on water as undulations which travel through water with transverse motion; these waves can be reflected, and add or cancel – superposition | P6 |

#### Sound waves

Strand code `SND`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.SND.01` | frequencies of sound waves, measured in hertz (Hz); echoes, reflection and absorption of sound | P6 |
| `KS3.P.SND.02` | sound needs a medium to travel, the speed of sound in air, in water, in solids | P6 |
| `KS3.P.SND.03` | sound produced by vibrations of objects, in loudspeakers, detected by their effects on microphone diaphragm and the ear drum; sound waves are longitudinal | P6 |
| `KS3.P.SND.04` | the auditory range of humans and animals | P6 |

#### Energy and waves

Strand code `EAW`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.EAW.01` | pressure waves transferring energy; use for cleaning and physiotherapy by ultrasound; waves transferring information for conversion to electrical signals by microphone | P6 |

#### Light waves

Strand code `LGT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.LGT.01` | the similarities and differences between light waves and waves in matter | P7 |
| `KS3.P.LGT.02` | light waves travelling through a vacuum; speed of light | P7 |
| `KS3.P.LGT.03` | the transmission of light through materials: absorption, diffuse scattering and specular reflection at a surface | P7 |
| `KS3.P.LGT.04` | use of ray model to explain imaging in mirrors, the pinhole camera, the refraction of light and action of convex lens in focusing (qualitative); the human eye | P7 |
| `KS3.P.LGT.05` | light transferring energy from source to absorber, leading to chemical and electrical effects; photosensitive material in the retina and in cameras | P7 |
| `KS3.P.LGT.06` | colours and the different frequencies of light, white light and prisms (qualitative only); differential colour effects in absorption and diffuse reflection | P7 |

### Electricity and electromagnetism

#### Current electricity

Strand code `CUR`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.CUR.01` | electric current, measured in amperes, in circuits, series and parallel circuits, currents add where branches meet and current as flow of charge | P8 |
| `KS3.P.CUR.02` | potential difference, measured in volts, battery and bulb ratings; resistance, measured in ohms, as the ratio of potential difference (p.d.) to current | P8 |
| `KS3.P.CUR.03` | differences in resistance between conducting and insulating components (quantitative) | P8 |

#### Static electricity

Strand code `STAT`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.STAT.01` | separation of positive or negative charges when objects are rubbed together: transfer of electrons, forces between charged objects | P9 |
| `KS3.P.STAT.02` | the idea of electric field, forces acting across the space between objects not in contact | P9 |

#### Magnetism

Strand code `MAG`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.MAG.01` | magnetic poles, attraction and repulsion | P10 |
| `KS3.P.MAG.02` | magnetic fields by plotting with compass, representation by field lines | P10 |
| `KS3.P.MAG.03` | Earth’s magnetism, compass and navigation | P10 |
| `KS3.P.MAG.04` | the magnetic effect of a current, electromagnets, DC motors (principles only) | P10 |

### Matter

#### Physical changes

Strand code `PHYC`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.PHYC.01` | conservation of material and of mass, and reversibility, in melting, freezing, evaporation, sublimation, condensation, dissolving | C1 |
| `KS3.P.PHYC.02` | similarities and differences, including density differences, between solids, liquids and gases | P11 |
| `KS3.P.PHYC.03` | Brownian motion in gases | P11 |
| `KS3.P.PHYC.04` | diffusion in liquids and gases driven by differences in concentration | C1 |
| `KS3.P.PHYC.05` | the difference between chemical and physical changes | C4 |

#### Particle model

Strand code `PMOD`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.PMOD.01` | the differences in arrangements, in motion and in closeness of particles explaining changes of state, shape and density; the anomaly of ice-water transition | P11 |
| `KS3.P.PMOD.02` | atoms and molecules as particles | C2 |

#### Energy in matter

Strand code `EIM`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.EIM.01` | changes with temperature in motion and spacing of particles | P11 |
| `KS3.P.EIM.02` | internal energy stored in materials | P11 |

### Space physics

Strand code `SPACE`.

| ID | Statutory statement (verbatim) | Proposed owning unit |
|---|---|---|
| `KS3.P.SPACE.01` | gravity force, weight = mass x gravitational field strength (g), on Earth g=10 N/kg, different on other planets and stars; gravity forces between Earth and Moon, and between Earth and sun (qualitative only) | P12 |
| `KS3.P.SPACE.02` | our sun as a star, other stars in our galaxy, other galaxies | P12 |
| `KS3.P.SPACE.03` | the seasons and the Earth’s tilt, day length at different times of year, in different hemispheres | P12 |
| `KS3.P.SPACE.04` | the light year as a unit of astronomical distance | P12 |

## Working scientifically

Taught through the content across all three disciplines (§5.7). Audit-only — exempt from the exactly-once rule.

### Scientific attitudes

Strand code `ATT`. Tag as `ws: ["scientific-attitudes"]`.

| ID | Statutory statement (verbatim) |
|---|---|
| `KS3.WS.ATT.01` | pay attention to objectivity and concern for accuracy, precision, repeatability and reproducibility |
| `KS3.WS.ATT.02` | understand that scientific methods and theories develop as earlier explanations are modified to take account of new evidence and ideas, together with the importance of publishing results and peer review |
| `KS3.WS.ATT.03` | evaluate risks |

### Experimental skills and investigations

Strand code `EXP`. Tag as `ws: ["experimental-skills-and-investigations"]`.

| ID | Statutory statement (verbatim) |
|---|---|
| `KS3.WS.EXP.01` | ask questions and develop a line of enquiry based on observations of the real world, alongside prior knowledge and experience |
| `KS3.WS.EXP.02` | make predictions using scientific knowledge and understanding |
| `KS3.WS.EXP.03` | select, plan and carry out the most appropriate types of scientific enquiries to test predictions, including identifying independent, dependent and control variables |
| `KS3.WS.EXP.04` | use appropriate techniques, apparatus, and materials during fieldwork and laboratory work, paying attention to health and safety |
| `KS3.WS.EXP.05` | make and record observations and measurements using a range of methods for different investigations; and evaluate the reliability of methods and suggest possible improvements |
| `KS3.WS.EXP.06` | apply sampling techniques |

### Analysis and evaluation

Strand code `ANA`. Tag as `ws: ["analysis-and-evaluation"]`.

| ID | Statutory statement (verbatim) |
|---|---|
| `KS3.WS.ANA.01` | apply mathematical concepts and calculate results |
| `KS3.WS.ANA.02` | present observations and data using appropriate methods, including tables and graphs |
| `KS3.WS.ANA.03` | interpret observations and data, including identifying patterns and using observations, measurements and data to draw conclusions |
| `KS3.WS.ANA.04` | present reasoned explanations, including explaining data in relation to predictions and hypotheses |
| `KS3.WS.ANA.05` | evaluate data, showing awareness of potential sources of random and systematic error |
| `KS3.WS.ANA.06` | identify further questions arising from their results |

### Measurement

Strand code `MEA`. Tag as `ws: ["measurement"]`.

| ID | Statutory statement (verbatim) |
|---|---|
| `KS3.WS.MEA.01` | understand and use SI units and IUPAC (International Union of Pure and Applied Chemistry) chemical nomenclature |
| `KS3.WS.MEA.02` | use and derive simple equations and carry out appropriate calculations |
| `KS3.WS.MEA.03` | undertake basic data analysis including simple statistical techniques |

---

## Appendix — coverage audit (advisory)

Statutory *supply* per unit (statements this register proposes it owns) against authoring *demand* (lessons architecture.md §7 gives it).

| Unit | Statements | §7 lessons | Statements per lesson |
|---|---|---|---|
| B1 | 6 | 8 | 0.75 ⚠️ |
| B2 | 3 | 4 | 0.75 ⚠️ |
| B3 | 5 | 8 | 0.62 ⚠️ |
| B4 | 4 | 5 | 0.80 ⚠️ |
| B5 | 2 | 8 | 0.25 ⚠️ |
| B6 | 1 | 3 | 0.33 ⚠️ |
| B7 | 4 | 4 | 1.00 |
| B8 | 4 | 5 | 0.80 ⚠️ |
| B9 | 3 | 6 | 0.50 ⚠️ |
| B10 | 4 | 5 | 0.80 ⚠️ |
| B11 | 3 | 4 | 0.75 ⚠️ |
| C1 | 5 | 6 | 0.83 ⚠️ |
| C2 | 5 | 6 | 0.83 ⚠️ |
| C3 | 4 | 7 | 0.57 ⚠️ |
| C4 | 3 | 5 | 0.60 ⚠️ |
| C5 | 1 | 5 | 0.20 ⚠️ |
| C6 | 5 | 7 | 0.71 ⚠️ |
| C7 | 2 | 4 | 0.50 ⚠️ |
| C8 | 6 | 5 | 1.20 |
| C9 | 3 | 4 | 0.75 ⚠️ |
| C10 | 6 | 6 | 1.00 |
| P1 | 6 | 8 | 0.75 ⚠️ |
| P2 | 5 | 5 | 1.00 |
| P3 | 3 | 3 | 1.00 |
| P4 | 11 | 9 | 1.22 |
| P5 | 3 | 4 | 0.75 ⚠️ |
| P6 | 6 | 9 | 0.67 ⚠️ |
| P7 | 6 | 7 | 0.86 ⚠️ |
| P8 | 3 | 7 | 0.43 ⚠️ |
| P9 | 2 | 3 | 0.67 ⚠️ |
| P10 | 4 | 5 | 0.80 ⚠️ |
| P11 | 5 | 4 | 1.25 |
| P12 | 4 | 6 | 0.67 ⚠️ |
| **Total** | **137** | **185** | **0.74** |

**26 of 33 units are marked ⚠️** — §7 gives them more lessons than there are statutory statements for those lessons to own.

This is the register's principal finding and it is recorded as open decision **§11.11**. There are 137 subject-content statements and 185 lessons in §7, so under §4.4 rule 3 (exactly one owner) at least 48 lessons must own nothing — which §10.2 forbids (`covers` non-empty). The two rules cannot both hold as written.
