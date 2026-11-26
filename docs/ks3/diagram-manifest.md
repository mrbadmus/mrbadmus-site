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
| `drawn` | 220 |
| `final` | 1 |
| `needed` | 3 |
| `retired` | 6 |
| **Total** | **231** |

`needed` = declared by a lesson, not yet drawn. A lesson may ship with figures at `needed` — it is not a build blocker — but the need is then counted here rather than invisible.

## Figures

| Unit | Lesson | Figure ID | Kind | Status | Caption |
|---|---|---|---|---|---|
| B1 | `animal-and-plant-cells` | `b1-cell-bench` | css-art | `drafted` | The cell bench drawing: a leaf cell and a cheek cell, each as a textbook drawing and as a ×400 field of view. |
| B1 | `animal-and-plant-cells` | `b1-cell-pair` | diagram | `drawn` | The plant cell has every part the animal cell has, plus three more. |
| B1 | `levels-of-organisation` | `b1-levels` | diagram | `drawn` | Each level is made of the level before it. |
| B1 | `life-processes` | `b1-candle-flame` | css-art | `final` | A burning candle: a flickering flame above the wick, with soot rising from it. |
| B1 | `specialised-cells` | `b1-diffusion` | diagram | `drawn` | Particles diffuse from a high concentration to a low concentration. |
| B1 | `specialised-cells` | `b1-specialised-cells` | diagram | `drawn` | The same basic parts, with a different shape or amount for each job. Not to scale. |
| B1 | `unicellular-organisms` | `b1-cell-sizes` | diagram | `drawn` | Lengths drawn to scale. |
| B1 | `unicellular-organisms` | `b1-unicellular` | diagram | `drawn` | Each one is a whole organism in a single cell. Not to scale. |
| B1 | `using-a-microscope` | `b1-biological-drawing` | diagram | `drawn` | Single lines, ruled labels and the magnification. No shading. |
| B1 | `using-a-microscope` | `b1-field-of-view` | diagram | `drawn` | Width of slide you can see with a ×10 eyepiece, to scale. |
| B1 | `using-a-microscope` | `b1-light-microscope` | diagram | `drawn` | Light goes up from the lamp, through the slide and the lenses, to your eye. |
| B1 | `using-a-microscope` | `b1-magnification-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| B1 | `using-a-microscope` | `b1-onion-epidermis-x100` | micrograph | `needed` | Onion epidermis, ×100. Cells countable, edges sharp. |
| B1 | `using-a-microscope` | `b1-onion-epidermis-x400` | micrograph | `needed` | The same spot, ×400. One cell wall crossing an empty grey field. |
| B10 | `chromosomes-genes-and-dna` | `b10-double-helix` | diagram | `drawn` | DNA is two strands twisted into a double helix, joined by pairs of bases. |
| B10 | `chromosomes-genes-and-dna` | `b10-nested-scale` | diagram | `drawn` | One molecule, five magnifications. Each frame is a callout of the frame above it, and the orange strand you can trace from the top of the column to the bottom never stops being the same strand. Orange is DNA wherever it appears; ink and grey are everything that is not DNA. The gene in panel 04 is a marked length of the strand that was coiled in panel 03 — a section of it, not a separate object sitting on it. Nothing is swapped for anything else on the way down: a chromosome, a gene and DNA are not three things sitting side by side in the nucleus, they are one thing at three magnifications. Count the marks in panel 02 — there are 46, in 23 pairs — and the orange one is the member of one pair that the rest of the column follows. |
| B10 | `chromosomes-genes-and-dna` | `b10-nucleus-to-base` | diagram | `drawn` | One DNA molecule, from the nucleus down to its bases. |
| B10 | `how-we-worked-out-dna` | `b10-base-ladder` | diagram | `drawn` | A big base always pairs with a small one. |
| B10 | `how-we-worked-out-dna` | `b10-base-pairs` | diagram | `drawn` | The reason is width. Every rung is one big and one small and every rung comes out the same length. Two big bases would bulge; two small ones would pinch — and twisting the ladder up into the shape you already know does not change it, because that width has become the width of the spiral. |
| B10 | `passing-it-on-heredity` | `b10-punnett-pp` | diagram | `drawn` | Each parent has two versions and passes one, so there are four ways the pair can land — and the grid is all four. Three of them contain at least one P, and P beats p, so three of the four flower purple. The fourth got p from both parents. That is where three to one comes from, and it is why a white plant can appear from two purple ones. |
| B10 | `passing-it-on-heredity` | `b10-punnett-pp-cross` | diagram | `drawn` | One of the four squares is pp. The chance of white is 1 in 4. |
| B10 | `passing-it-on-heredity` | `b10-punnett-pp-pp` | diagram | `drawn` | Two of the four squares are pp, so the chance of white is 1 in 2. |
| B10 | `variation-continuous-and-discontinuous` | `b10-blood-group-bars` | diagram | `drawn` | Blood groups of sixty students. The bars have gaps, because the groups are separate. |
| B10 | `variation-continuous-and-discontinuous` | `b10-height-bars-lean` | diagram | `drawn` | Heights of sixty students, in 5 cm ranges. |
| B10 | `variation-continuous-and-discontinuous` | `b10-height-bars-touching` | diagram | `drawn` | Height, in centimetres, for sixty students. The bars touch — there is no gap between one range and the next. |
| B10 | `what-makes-a-species` | `b10-speciation` | diagram | `drawn` | Split, change on each side, and the two groups can no longer interbreed. |
| B11 | `natural-selection` | `b11-moth-barks` | diagram | `drawn` | The same two moths on two kinds of bark. |
| B11 | `natural-selection` | `b11-moth-pair` | diagram | `drawn` | Neither moth changed. The bark did. Being found is the whole of the disadvantage. |
| B11 | `natural-selection` | `b11-selection-steps` | diagram | `drawn` | Natural selection in peppered moths on sooty bark. |
| B3 | `absorption-and-the-small-intestine` | `b3-villus-labelled` | diagram | `drawn` | Each frame is drawn from a callout of the frame before it, so the folding is one thing at three sizes rather than three separate facts: the tube is ridged, every ridge is covered in villi, and every cell of every villus is covered in microvilli. The panel underneath shows why it is worth doing. Count the cells across the wall of the villus — there is one. On the far side of that single cell is a capillary, which is why a glucose molecule in the gut is in the bloodstream a moment later. |
| B3 | `absorption-and-the-small-intestine` | `b3-villus-lean` | diagram | `drawn` | Every villus has a thin wall and a capillary close behind it. |
| B3 | `absorption-and-the-small-intestine` | `b3-visking` | diagram | `drawn` | Glucose passes through the tubing. Starch does not. |
| B3 | `energy-in-food-and-what-you-need` | `b3-burning-food` | diagram | `drawn` | The burning food heats the water. A bigger temperature rise means more energy. |
| B3 | `energy-in-food-and-what-you-need` | `b3-day-intake` | diagram | `drawn` | The day's food falls 2480 kJ short of the 9500 kJ needed. |
| B3 | `energy-in-food-and-what-you-need` | `b3-energy-needs` | diagram | `drawn` | Daily energy needs, rounded. The rower needs over four times as much as the 4-year-old. |
| B3 | `energy-in-food-and-what-you-need` | `b3-share-of-day` | diagram | `drawn` | The chocolate bar is about 11% of the day's need. |
| B3 | `enzymes-in-digestion` | `b3-enzyme-breakdown` | diagram | `drawn` | Each enzyme breaks one kind of large molecule into small ones. |
| B3 | `enzymes-in-digestion` | `b3-enzyme-cycle` | diagram | `drawn` | The enzyme is the same at the end as at the start. |
| B3 | `food-tests` | `b3-food-test-colours` | diagram | `drawn` | Each test finds one nutrient. The right-hand tubes show a positive result. |
| B3 | `the-digestive-system` | `b3-digestion-timing` | diagram | `drawn` | Hours spent in each organ, to scale. |
| B3 | `the-digestive-system` | `b3-gut-body` | diagram | `drawn` | Food passes through the mouth, oesophagus, stomach, small intestine, large intestine, rectum and anus. |
| B3 | `the-digestive-system` | `b3-gut-labelled` | diagram | `drawn` | One tube, from 01 at the top to 07 at the bottom, with the orange line running down the middle of it the whole way. The small intestine is the long narrow coiled run; the large intestine below it is visibly wider and shorter. Stop 05 — pancreas, liver and gall bladder — sits inside the dashed boundary, with ducts leading out of it into the tube. That is the distinction the bench’s own stop 05 rests on: those three send juices in, and food never passes through them. Put a finger on 01 and follow the orange line down: it does not stop, branch or start again anywhere between there and 07, and it never once goes into the dashed boundary. |
| B4 | `how-breathing-works` | `b4-bell-jar-model` | diagram | `drawn` | Pull the sheet down and the balloons inflate. |
| B4 | `how-breathing-works` | `b4-lung-volume-bottle` | diagram | `drawn` | The air you breathe out pushes water out of the bottle. |
| B4 | `stomata-and-gas-exchange-in-plants` | `b4-gas-exchange-bars` | diagram | `drawn` | Respiration, photosynthesis, and what a sensor outside the leaf actually measures, in bright light. |
| B4 | `stomata-and-gas-exchange-in-plants` | `b4-guard-cells-two-state` | diagram | `drawn` | Nothing opens the pore but the shape of the two cells beside it. Water moves into the pair and each cell bows away from its partner — the wall along the inside is thick and stiff while the outer wall stretches, so the cell can only curve, and curving pulls the gap open. Water moves out, the cells go limp and straighten, and the two inner walls meet: no gap left. The pair is drawn the same length and the same thickness in both states, so the only thing that has changed is the bend. And the slice underneath says where the pores are: every one of them is in the underside of the leaf, and the top surface has none. |
| B4 | `the-gas-exchange-system` | `b4-gas-exchange-labelled` | diagram | `drawn` | The route in runs 01 to 05 and stops there: gas exchange happens at the sacs and nowhere earlier along the tubes. Each lung is drawn full of branching — four divisions, each branch narrower than the last — because a lung is not a hollow bag. The circled cluster is magnified on the right, where one capillary crosses the sacs and the wall between air and blood is a single cell thick. The ribs, the muscles between them and the diaphragm are drawn outside the lungs: 06 is the only part of this figure that is not the airway. |
| B5 | `fertilisation-seeds-and-fruit` | `b5-pollen-tube` | diagram | `drawn` | The grain lands at 01 and the two nuclei fuse at 03, and the drawing puts the whole length of the style between them: pollination is delivery, fertilisation is fusion, and they are not the same event. The three ovules are drawn inside the ovary wall; on the right the three seeds are inside the fruit wall, in the same three places. Ovule to seed and ovary to fruit are then one fact about containment rather than two labels to memorise. Nothing moves out of anything — check it: put one finger on the top ovule on the left and one on the top seed on the right, and nothing has travelled. It changed where it already was, and the ovary swelled around it. The tube has a distance to grow and takes time to grow it, which is why 01 and 03 are two events and not one. |
| B5 | `flowers-and-pollination` | `b5-flower-parts-labelled` | diagram | `drawn` | Nine parts, drawn twice. On the left, inside the dashed line, the anthers stand where a visiting insect must brush past them and the stigma is a small sticky knob in the same enclosed space. On the right the dashed line encloses only the floret: the anthers hang outside it on long thin filaments and the stigmas are large, feathery and open to the air. A table can tell a student that anthers are “held inside” or “dangling outside”; only a drawing can let them check it. Both drawings carry the same numbers for the same parts, so anything that differs between them is a position and not a different part: find 01, 02 and 03 on each side, and look at where the dashed line leaves them. |
| B5 | `flowers-and-pollination` | `b5-wind-vs-insect` | diagram | `retired` | An insect-pollinated flower and a wind-pollinated flower side by side, showing petals, nectary, the position of the anthers, the texture of the stigma and the grains of pollen for each. |
| B5 | `gametes-and-fertilisation` | `b5-egg-sperm-scale` | diagram | `drawn` | Relative diameter, to scale. |
| B5 | `gametes-and-fertilisation` | `b5-gametes-journey` | diagram | `drawn` | The whole process on one tract, numbered in the order it happens. The solid orange line is one journey — the egg, and then the embryo it becomes — running from the ovary at 01 to the uterus lining at 05. The dashed line is the sperm’s route in, and the two meet at 03 in the oviduct. The cells drawn between 03 and 04 are the same embryo dividing while it is still travelling: by the time it reaches 05 it is a ball of cells and it is in a different organ, five or six days later. Find 03, then find 05: they are marked with different days, they sit in different organs, and the orange route runs the whole way between them. Fertilisation and implantation are two events, not one. |
| B5 | `gametes-and-fertilisation` | `b5-gametes-labelled` | diagram | `retired` | A sperm cell and an egg cell drawn to the same scale and labelled: the sperm’s head, mitochondria and tail, and the egg’s nucleus, cytoplasm, food store and outer layer, with each cell’s diameter given — about 0.005 mm and about 0.1 mm. |
| B5 | `gestation-placenta-and-birth` | `b5-placenta-exchange` | diagram | `drawn` | Two circulations, brought within a fraction of a millimetre of each other across an enormous surface, and never joined. Trace the blue: the baby's blood leaves along the cord, loops inside a villus, and returns along the cord — a closed circuit. Trace the orange: the mother's blood arrives through the uterus wall, fills the space around and between the villi, and leaves the way it came. Between them, everywhere, is placenta tissue one cell thick. Only substances cross it, and they cross by diffusion, from wherever there is more of them to wherever there is less. Both bloods are red in life; the two colours here say only whose is whose. Follow either one as far as it goes and you never arrive in the other: every villus reaches into the mother's blood and her blood reaches back between them, yet the tissue outline runs unbroken around every villus and along the plate. Substances cross that wall; blood never does. |
| B5 | `human-reproductive-systems` | `b5-female-system-labelled` | diagram | `retired` | The female reproductive system, labelled: the ovaries, the oviducts, the uterus, the cervix and the vagina. |
| B5 | `human-reproductive-systems` | `b5-male-system-labelled` | diagram | `retired` | The male reproductive system, labelled: the testes, the sperm duct, the glands that add fluid, the urethra and the penis. |
| B5 | `human-reproductive-systems` | `b5-reproductive-systems` | diagram | `drawn` | The nine structures the lesson asks a student to place, each drawn where the body puts it. Two things are true here that a name-to-job list cannot show: the testes sit below the dashed line, outside the body cavity, and the orange ring is in the oviduct — fertilisation happens there and not in the uterus. The dashed link between 01 and 05 is the only pairing that runs across the two systems; both make gametes. Everything with a filled badge has no counterpart on the other side, which is why the systems are not mirror images. Count the filled badges: there are three, and all three are on the female side. |
| B5 | `lifestyle-and-the-developing-foetus` | `b5-what-crosses` | diagram | `retired` | What crosses the placenta and what does not: small soluble molecules — oxygen, glucose, alcohol, nicotine, carbon monoxide, caffeine — diffusing across the exchange surface, with large molecules such as insulin shown too big to pass and antibodies shown carried across using energy. The two blood supplies are drawn separately and never mixing. |
| B5 | `seed-dispersal` | `b5-dispersal-specimens` | diagram | `drawn` | Eight fruits and seeds on one ground line at one scale, smallest first, numbered and named — and nothing else. The hooks, the hairs, the ring of holes under the rim, the flesh around a hard pip, the off-centre wing, the fibrous layer full of voids: all of it is drawn, none of it is captioned with a method. The scale is real, which is why the coconut is that size and the goosegrass is that size, and why one of them was never going to be moved by wind. The goosegrass detail is magnified four times and says so on the drawing. Measure any of them against the bar under the ground line: the coconut is 250 mm across, husk and all, the goosegrass pair is 9 mm, and both are drawn against that same bar. Then work out, from what is drawn and from nothing else, how each one gets away from the plant it grew on. |
| B5 | `the-menstrual-cycle` | `b5-cycle-timeline` | diagram | `retired` | One cycle drawn as a timeline for each of the three lengths, 21, 28 and 35 days: the bleeding window at the start, the building phase, release a fortnight before the end, and the fortnight in which the lining is held ready — with the release marker landing on a different day in each of the three. |
| B7 | `leaves-built-for-the-job` | `b7-leaf-section` | diagram | `drawn` | The whole slice is less than half a millimetre from top to bottom. Two of its features are claims you can check by looking: the palisade cells are the layer nearest the light, and they hold most of the chloroplasts — count them against the spongy cells below. The only break in either surface is the one pore, and it is underneath. Follow the arrow to see why that still works: carbon dioxide goes in through the pore, up through the air spaces, and into a palisade cell, without anything having to carry it. |
| B7 | `the-photosynthesis-reaction` | `b7-word-summary` | diagram | `drawn` | The word summary for photosynthesis. |
| B7 | `why-almost-all-life-depends-on-it` | `b7-food-chain-grass` | diagram | `drawn` | A food chain starts with a producer. |
| B8 | `aerobic-respiration` | `b8-word-aerobic` | diagram | `drawn` | The word summary for aerobic respiration. |
| B8 | `anaerobic-respiration-in-humans` | `b8-word-anaerobic` | diagram | `drawn` | The word summary for anaerobic respiration in humans. |
| B8 | `fermentation` | `b8-word-fermentation` | diagram | `drawn` | The word summary for fermentation. |
| B8 | `fermentation` | `b8-yeast-limewater` | diagram | `drawn` | Yeast and sugar solution, with a delivery tube into limewater. |
| B9 | `disturbing-a-food-web` | `b9-oak-wood-web` | diagram | `drawn` | The wood, before anything is taken out of it. Count the arrows into and out of each organism before you choose one to remove — the ones with a single line are not always the ones that matter least. |
| B9 | `food-chains-and-food-webs` | `b9-oak-wood-web-thread` | diagram | `drawn` | One oak wood.  The numbered orange chain is one route through it — the same four steps the bench above climbs. |
| B9 | `predator-and-prey` | `b9-predator-prey-cycle` | diagram | `drawn` | The fox line is still going up while the rabbit line is already coming down, and it does not turn over until years later. That gap is the whole idea: foxes cannot become more foxes the moment there is more to eat — breeding takes time — so the fox peak always follows the rabbit peak rather than arriving with it. Look at when each peak happens, not how high it is: the two are counted on their own scales. |
| C1 | `changes-of-state` | `c1-heating-curve` | graph | `drawn` | The temperature stays flat while the water melts and while it boils. |
| C1 | `diffusion` | `c1-brownian` | diagram | `drawn` | Air particles hit the speck unevenly, so it moves in a random path. |
| C1 | `diffusion` | `c1-spreading` | diagram | `drawn` | The particles spread from a high concentration to a low concentration. |
| C1 | `gas-pressure` | `c1-wall-hits` | diagram | `drawn` | In half the space, the particles hit the walls more often. |
| C1 | `particle-model` | `c1-mixing` | diagram | `drawn` | The small particles fit into gaps between the big ones. |
| C1 | `solids-liquids-and-gases` | `c1-expansion` | diagram | `drawn` | Heating moves the particles slightly further apart. The particles do not grow. |
| C1 | `solids-liquids-and-gases` | `c1-particle-states` | diagram | `drawn` | One substance, three states. Compare the particles inside each box with the reference particle underneath it. |
| C1 | `solids-liquids-and-gases` | `c1-three-states` | diagram | `drawn` | The same particles in each state, arranged and moving differently. |
| C2 | `chemical-symbols` | `c2-co-and-co` | diagram | `drawn` | CO is two elements joined. Co is one element. |
| C2 | `compounds` | `c2-ecm-particles` | diagram | `drawn` | Look at the kinds of atom, and which ones are joined. |
| C2 | `compounds` | `c2-iron-sulfur` | diagram | `drawn` | Mixed, iron and sulfur are separate. In iron sulfide, they are joined. |
| C2 | `conservation-of-mass` | `c2-carbon-burns` | diagram | `drawn` | The same atoms before and after, so the same mass. |
| C2 | `conservation-of-mass` | `c2-open-sealed` | diagram | `drawn` | Open, the gas escapes and the mass falls. Sealed, it stays the same. |
| C2 | `conservation-of-mass` | `c2-word-magnesium` | diagram | `drawn` | The word equation for burning magnesium. |
| C2 | `elements` | `c2-element-particles` | diagram | `drawn` | Copper and oxygen each have one kind of atom. Water has two. |
| C2 | `formulae` | `c2-ammonia` | diagram | `drawn` | Count the atoms of each element. |
| C2 | `formulae` | `c2-big-small` | diagram | `drawn` | The big number counts molecules. The small numbers count atoms. |
| C2 | `formulae` | `c2-molecules` | diagram | `drawn` | Each formula counts the atoms in one molecule. |
| C2 | `formulae` | `c2-salt-lattice` | diagram | `drawn` | Salt has no separate molecules. NaCl gives the ratio. |
| C2 | `the-atom-daltons-model` | `c2-lead-gold-atoms` | diagram | `drawn` | Lead is only lead atoms. Gold is only gold atoms. |
| C3 | `distillation` | `c3-distillation-apparatus` | diagram | `needed` | Distillation apparatus: round-bottomed flask over a Bunsen with anti-bumping granules, thermometer bulb level with the side arm, Liebig condenser with cold water entering at the bottom and leaving at the top, and a beaker collecting the distillate. The apparatus is open to the air at the collecting end. |
| C3 | `filtration` | `particle-panels` | diagram | `drawn` | A grain of sand is a lump of many millions of particles stuck together, thousands of times wider than the gaps between the paper's fibres. A dissolved salt particle is on its own, and it is smaller than the gap by more than the gap is smaller than the grain. There is no filter paper that stops one and passes the other. |
| C4 | `chemical-vs-physical-change` | `c4-change-particles` | diagram | `drawn` | Melting moves the same particles. A reaction joins the atoms up in new particles. |
| C4 | `reactions-rearrange-atoms` | `c4-methane-steps` | diagram | `drawn` | Every atom in the products was in the methane or the oxygen. |
| C4 | `reactions-rearrange-atoms` | `c4-water-steps` | diagram | `drawn` | The same 6 atoms all the way through. Only the joins change. |
| C4 | `word-equations` | `c4-word-magnesium` | diagram | `drawn` | Oxygen from the air is a reactant, so it goes on the left. |
| C4 | `word-equations` | `c4-word-marble` | diagram | `drawn` | Two reactants on the left, three products on the right. |
| C5 | `combustion` | `c5-fire-triangle` | diagram | `drawn` | The fire triangle: fuel, oxygen and heat. |
| C5 | `combustion` | `c5-word-complete` | diagram | `drawn` | With plenty of oxygen, methane gives carbon dioxide and water. |
| C5 | `combustion` | `c5-word-incomplete` | diagram | `drawn` | With too little oxygen, some carbon becomes carbon monoxide and some is left as soot. |
| C5 | `displacement` | `reactivity-series` | diagram | `drawn` | Nobody was told this order. It was assembled by doing what you are about to do — putting metals into each other's solutions and recording which way the swap went. The bench below covers four of these twelve; the same method extended down the list produces the rest of it. |
| C5 | `oxidation` | `c5-rust-tubes` | diagram | `drawn` | Only the tubes with both air and water rust. |
| C5 | `oxidation` | `c5-word-magnesium` | diagram | `drawn` | Magnesium gains oxygen from the air. |
| C5 | `oxidation` | `c5-word-metal-oxygen` | diagram | `drawn` | A metal gains oxygen and becomes a metal oxide. |
| C5 | `oxidation` | `c5-word-rust` | diagram | `drawn` | Rust is hydrated iron oxide. |
| C5 | `thermal-decomposition` | `c5-gas-tests` | diagram | `drawn` | Oxygen relights a glowing splint. Hydrogen pops. Carbon dioxide turns limewater milky. |
| C5 | `thermal-decomposition` | `c5-heating-carbonate` | diagram | `drawn` | The gas turns limewater milky, so it is carbon dioxide. |
| C5 | `thermal-decomposition` | `c5-word-carbonate-heat` | diagram | `drawn` | One reactant breaks down into two products. Heating goes on all the time. |
| C6 | `acid-plus-metal` | `c6-squeaky-pop` | diagram | `drawn` | Collect the gas, close the tube, then test it away from the reaction. |
| C6 | `acid-plus-metal` | `c6-word-metal-acid` | diagram | `drawn` | Every reactive metal gives a salt and hydrogen with an acid. |
| C6 | `acids-and-alkalis` | `c6-ph-scale-acids` | diagram | `drawn` | Below 7 is acidic, 7 is neutral and above 7 is alkaline. |
| C6 | `acids-and-carbonates` | `c6-limewater-test` | diagram | `drawn` | The end of the delivery tube must be under the limewater. |
| C6 | `acids-and-carbonates` | `c6-word-carbonate-acid` | diagram | `drawn` | Every metal carbonate gives a salt, water and carbon dioxide with an acid. |
| C6 | `making-a-pure-dry-salt` | `c6-salt-steps` | diagram | `drawn` | Excess, filter, evaporate, then cool slowly. |
| C6 | `making-a-pure-dry-salt` | `c6-word-copper-sulfate` | diagram | `drawn` | Copper oxide neutralises sulfuric acid, making copper sulfate and water. |
| C6 | `neutralisation` | `c6-neutral-curve` | graph | `drawn` | The pH jumps past 7 when the last of the acid is used up. |
| C6 | `neutralisation` | `c6-word-hcl-naoh` | diagram | `drawn` | Sodium from the alkali and chloride from the acid make sodium chloride. |
| C6 | `neutralisation` | `c6-word-neutral` | diagram | `drawn` | The general word equation for neutralisation. |
| C6 | `the-ph-scale-and-indicators` | `c6-cabbage-colours` | diagram | `drawn` | Red cabbage indicator in acid, neutral and alkaline solutions. |
| C6 | `the-ph-scale-and-indicators` | `c6-ph-scale-colours` | diagram | `drawn` | Match the colour to the chart, then read the pH number. |
| C6 | `the-ph-scale-and-indicators` | `ph-scale` | diagram | `drawn` | Fifteen whole numbers, one colour each. The reds and oranges are acid, green is neutral, and the blues and purples are alkali. The numbers matter more than the colours: colour-blind chemists use a pH meter and get the same answer. |
| C7 | `endothermic-reactions` | `c7-endo-thermometers` | diagram | `drawn` | The temperature of the mixture falls, so the reaction is endothermic. |
| C7 | `endothermic-reactions` | `c7-exo-endo-arrows` | diagram | `drawn` | The arrows show which way the energy moves. |
| C7 | `exothermic-reactions` | `c7-exo-arrows` | diagram | `drawn` | In an exothermic reaction, energy goes out of the chemicals. |
| C7 | `exothermic-reactions` | `c7-exo-thermometers` | diagram | `drawn` | The temperature of the mixture rises, so the reaction is exothermic. |
| C7 | `measuring-a-temperature-change` | `c7-cup-rig` | diagram | `drawn` | The cup and lid cut down the heat that escapes. |
| C7 | `measuring-a-temperature-change` | `c7-tc-table` | diagram | `drawn` | Final means the highest or lowest temperature reached. |
| C7 | `measuring-a-temperature-change` | `c7-tc-thermometers` | diagram | `drawn` | Read the start temperature, then the highest temperature reached. |
| P1 | `conservation-of-energy` | `p1-pendulum-stores` | diagram | `drawn` | The bars change. The total stays at 120 J. |
| P1 | `energy-transfers-before-and-after` | `p1-sankey-winch` | diagram | `drawn` | The width of each arrow shows the energy. 100 J in = 70 J + 30 J out. |
| P1 | `simple-machines` | `p1-lever-trade` | diagram | `drawn` | Small force, big distance. Big force, small distance. |
| P1 | `simple-machines` | `p1-triangle-wfd` | diagram | `drawn` | Cover the one you want to find. |
| P10 | `electromagnets` | `p10-electromagnet-nail` | diagram | `drawn` | Close the switch, and the iron core picks up the clips. |
| P10 | `how-a-motor-works` | `p10-motor-arrows-marked` | diagram | `drawn` | The coil from this lesson's bench, with its two force arrows marked. |
| P10 | `magnetic-fields` | `p10-bar-field-lines` | diagram | `drawn` | Each small circle is a plotting compass. Its needle points along the field line. |
| P10 | `magnetic-fields` | `p10-horseshoe-field-gap` | diagram | `drawn` | The gap between a horseshoe magnet's two poles. |
| P10 | `magnetic-fields` | `p10-two-magnets-nn` | diagram | `drawn` | No field lines pass through the neutral point. |
| P10 | `magnets-and-poles` | `p10-pole-pairs-three` | diagram | `drawn` | The arrows show which way each magnet is pushed or pulled. |
| P10 | `magnets-and-poles` | `p10-steel-test-three` | diagram | `drawn` | The small letters show the poles the magnet makes in the steel. |
| P10 | `the-earth-is-a-magnet` | `p10-earth-field-model` | diagram | `drawn` | The magnet's S end is under the Arctic, so the compass N end points north. |
| P12 | `mass-vs-weight` | `p12-weight-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P2 | `calculating-energy-transferred` | `p2-energy-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P2 | `energy-in-food` | `p2-food-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P2 | `fuels-and-energy-resources` | `p2-fossil-fuels` | diagram | `drawn` | Coal formed from plants. Oil and gas formed from tiny sea organisms. |
| P2 | `power-ratings-in-watts` | `p2-power-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P3 | `distance-time-graphs` | `p3-dt-curve` | diagram | `drawn` | A line that gets steeper, then less steep. |
| P3 | `distance-time-graphs` | `p3-dt-journey` | diagram | `drawn` | A walk, a wait, then a run. |
| P3 | `speed` | `p3-speed-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P4 | `drawing-and-adding-forces` | `p4-resultant-beam-recap` | diagram | `drawn` | The same beam as earlier in this lesson. |
| P4 | `drawing-and-adding-forces` | `p4-sledge-arrows` | diagram | `drawn` | The 40 N pull and the 25 N pull, drawn to the same scale. |
| P4 | `friction` | `p4-crate-steady` | diagram | `drawn` | A crate sliding along a floor at a steady speed. |
| P4 | `moments` | `p4-moment-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P4 | `moments` | `p4-moments-seesaw` | diagram | `drawn` | A seesaw balanced on its pivot. |
| P4 | `moments` | `p4-moments-seesaw-find` | diagram | `drawn` | Find the distance marked with a question mark. |
| P4 | `what-a-force-is` | `p4-force-pair-wall` | diagram | `drawn` | The skater and the wall push on each other. |
| P4 | `what-a-force-is` | `p4-newtonmeter-reading` | diagram | `drawn` | The pointer reads 3 N, so the shoe pulls down with 3 N. |
| P6 | `echoes-reflection-and-absorption` | `p6-echo-boundary` | diagram | `drawn` | Reflected, absorbed and transmitted: usually some of each. |
| P6 | `echoes-reflection-and-absorption` | `p6-echo-cliff` | diagram | `drawn` | The shout travels to the cliff and back again. |
| P6 | `frequency-pitch-and-loudness` | `p6-05-count` | diagram | `drawn` | Each second holds 200 vibrations. Three seconds hold 600. |
| P6 | `frequency-pitch-and-loudness` | `p6-05-rate` | diagram | `drawn` | Share the vibrations out over 30 seconds. Each second gets 500. |
| P6 | `frequency-pitch-and-loudness` | `p6-05-traces` | diagram | `drawn` | Taller waves sound louder. More waves across the screen sound higher. |
| P6 | `frequency-pitch-and-loudness` | `p6-05-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P6 | `hearing-and-auditory-range` | `p6-ear-parts` | diagram | `drawn` | Sound goes in through the ear canal. The auditory nerve carries impulses to the brain. |
| P6 | `hearing-and-auditory-range` | `p6-ear-range-animals` | diagram | `drawn` | Each animal hears a different range of frequencies. |
| P6 | `hearing-and-auditory-range` | `p6-ear-range-human` | diagram | `drawn` | Each mark on the scale is ten times the one before. |
| P6 | `how-sound-is-made` | `p6-03-chain` | diagram | `drawn` | Every sound follows these four steps. |
| P6 | `sound-is-longitudinal` | `p6-04-graph` | diagram | `drawn` | Each peak sits under a compression. Each dip sits under a rarefaction. |
| P6 | `sound-is-longitudinal` | `p6-04-sound` | diagram | `drawn` | Longitudinal: each layer of air moves back and forth along the direction of travel. |
| P6 | `sound-is-longitudinal` | `p6-04-transverse` | diagram | `drawn` | Transverse: each coil moves across the direction of travel. |
| P6 | `sound-needs-a-medium` | `p6-medium-bell-jar` | diagram | `drawn` | The hammer beats in both jars. Only the jar with air in it lets the sound out. |
| P6 | `sound-needs-a-medium` | `p6-medium-rail` | diagram | `drawn` | The same blow reaches the listener through the steel and through the air. |
| P6 | `sound-needs-a-medium` | `p6-medium-speed-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P6 | `transverse-waves-and-superposition` | `p6-02-superpose` | diagram | `drawn` | Crest on crest adds. Crest on trough of the same size cancels. |
| P6 | `transverse-waves-and-superposition` | `p6-02-transverse` | diagram | `drawn` | The surface moves up and down. The wave travels across. |
| P6 | `ultrasound-at-work` | `p6-ultra-probe` | diagram | `drawn` | The pulse goes down to the crack and back up to the probe. |
| P6 | `waves-on-water` | `p6-01-motion` | diagram | `drawn` | Follow the dot. It only goes up and down while the wave passes. |
| P6 | `waves-on-water` | `p6-01-parts` | diagram | `drawn` | The parts of a wave. |
| P7 | `colour-and-the-spectrum` | `p7-prism` | diagram | `drawn` | Red is bent the least. Violet is bent the most. |
| P7 | `colour-and-the-spectrum` | `p7-prism-two` | diagram | `drawn` | The second prism puts the colours back into white light. |
| P7 | `light-travels` | `p7-light-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P7 | `light-travels` | `p7-shadow` | diagram | `drawn` | Straight rays leave a sharp-edged shadow behind the card. |
| P7 | `light-travels` | `p7-trip-sat` | diagram | `drawn` | Find the time marked with a question mark. |
| P7 | `light-travels` | `p7-trip-sun` | diagram | `drawn` | Find the distance marked with a question mark. |
| P7 | `reflection-mirrors-and-scattering` | `p7-reflect-find` | diagram | `drawn` | Find i and r. Both are measured from the normal. |
| P7 | `reflection-mirrors-and-scattering` | `p7-reflect-law` | diagram | `drawn` | Both angles are measured from the normal, and they are equal. |
| P7 | `reflection-mirrors-and-scattering` | `p7-surfaces` | diagram | `drawn` | Each ray obeys the law of reflection on both surfaces. |
| P7 | `refraction` | `p7-block-angle` | diagram | `drawn` | Towards the normal going in. Away from the normal coming out. |
| P7 | `refraction` | `p7-block-straight` | diagram | `drawn` | Along the normal: a change of speed, but no change of direction. |
| P7 | `refraction` | `p7-straw` | diagram | `drawn` | The eye traces the light back in a straight line. |
| P7 | `why-things-look-coloured` | `p7-colour-green` | diagram | `drawn` | No light is reflected to the eye. |
| P7 | `why-things-look-coloured` | `p7-colour-white` | diagram | `drawn` | Only the reflected red light reaches the eye. |
| P7 | `why-things-look-coloured` | `p7-filter-red` | diagram | `drawn` | The filter absorbs green and blue. Only red gets through. |
| P7 | `why-things-look-coloured` | `p7-filter-two` | diagram | `drawn` | The red filter lets through only red. The green filter absorbs red. |
| P8 | `building-and-measuring-a-circuit` | `p8-build-ammeter-across` | diagram | `drawn` | The ammeter bridges the lamp, so the lamp goes out. |
| P8 | `building-and-measuring-a-circuit` | `p8-build-correct` | diagram | `drawn` | The ammeter is in the loop. The voltmeter is across the lamp. |
| P8 | `building-and-measuring-a-circuit` | `p8-build-symbols` | diagram | `drawn` | Each component has one standard symbol. |
| P8 | `building-and-measuring-a-circuit` | `p8-build-voltmeter-loop` | diagram | `drawn` | The voltmeter reads 3.00 V, but no current flows. |
| P8 | `conductors-and-insulators` | `p8-cond-cable` | diagram | `drawn` | Copper inside to carry the current. Plastic outside to keep it in. |
| P8 | `conductors-and-insulators` | `p8-cond-circuit` | diagram | `drawn` | The ammeter is in the loop. The voltmeter is across the pencil lead. |
| P8 | `conductors-and-insulators` | `p8-cond-electrons` | diagram | `drawn` | Free electrons can carry charge through a metal. Plastic has none. |
| P8 | `conductors-and-insulators` | `p8-cond-tester` | diagram | `drawn` | The lamp lights only when the material conducts. |
| P8 | `conductors-and-insulators` | `p8-cond-triangle` | diagram | `drawn` | Cover R. V sits over I, so you divide. |
| P8 | `conductors-and-insulators` | `p8-resistance-chart-recap` | diagram | `drawn` | The same chart as earlier in this lesson. |
| P8 | `current-and-circuits` | `p8-l1-drawn` | diagram | `drawn` | Straight lines, square corners and the right symbols. |
| P8 | `current-and-circuits` | `p8-l1-open` | diagram | `drawn` | An open switch leaves a gap, so no current flows. |
| P8 | `current-and-circuits` | `p8-l1-symbols-supply` | diagram | `drawn` | The symbols for parts that supply, join and switch. |
| P8 | `current-and-circuits` | `p8-l1-symbols-use` | diagram | `drawn` | The symbols for parts that use and measure. |
| P8 | `current-and-circuits` | `p8-l1-two-ammeters` | diagram | `drawn` | Before the lamp and after it, the current is the same. |
| P8 | `current-and-circuits` | `p8-lamp-symbol` | diagram | `drawn` | One of the eight symbols from this lesson's key, shown on its own. |
| P8 | `current-at-a-junction` | `p8-l3-find` | diagram | `drawn` | Find the reading marked with a question mark. |
| P8 | `current-at-a-junction` | `p8-l3-find-ma` | diagram | `drawn` | Change milliamps to amps before you subtract. |
| P8 | `current-at-a-junction` | `p8-l3-junction` | diagram | `drawn` | 0.30 A + 0.20 A = 0.50 A in the main wire, on both sides. |
| P8 | `potential-difference` | `p8-l4-find` | diagram | `drawn` | Find the reading marked with a question mark. |
| P8 | `potential-difference` | `p8-l4-find-mv` | diagram | `drawn` | Change millivolts to volts before you subtract. |
| P8 | `potential-difference` | `p8-l4-meters` | diagram | `drawn` | The ammeter is in the loop. The voltmeter is across the lamp. |
| P8 | `potential-difference` | `p8-l4-parallel` | diagram | `drawn` | Each branch gets the battery's full p.d. |
| P8 | `potential-difference` | `p8-l4-series` | diagram | `drawn` | 2.0 V + 4.0 V = 6.0 V. |
| P8 | `resistance` | `p8-res-circuit-lamp` | diagram | `drawn` | The ammeter reads in milliamps, so convert first. |
| P8 | `resistance` | `p8-res-circuit-resistor` | diagram | `drawn` | The ammeter is in the loop. The voltmeter is across the resistor. |
| P8 | `resistance` | `p8-res-collisions` | diagram | `drawn` | Every bump makes it harder for the electrons to flow, and heats the wire. |
| P8 | `resistance` | `p8-res-triangle` | diagram | `drawn` | Cover the one you want. Side by side means multiply. One over the other means divide. |
| P8 | `resistance` | `p8-res-wires` | diagram | `drawn` | A longer wire or a thinner wire has more resistance. |
| P8 | `series-and-parallel` | `p8-l2-parallel` | diagram | `drawn` | Two paths. The full p.d. on each branch, and the currents add up. |
| P8 | `series-and-parallel` | `p8-l2-series` | diagram | `drawn` | One path. The same current everywhere, and the p.d. shared. |
| P9 | `charging-by-rubbing` | `p9-rub-rod-duster` | diagram | `drawn` | Two electrons move from the duster to the rod. The protons stay where they are. |
| P9 | `electric-fields` | `p9-field-arrows-two` | diagram | `drawn` | Each arrow shows the push on a small positive charge at that point. |
| P9 | `electric-fields` | `p9-field-cancel-mid` | diagram | `drawn` | Each big charge pushes the test charge away from itself. |
| P9 | `electric-fields` | `p9-field-point-marked` | diagram | `drawn` | One point on a field map, marked. |
| P9 | `forces-between-charges` | `p9-charge-matrix-grid` | diagram | `drawn` | The same grid as earlier in this lesson. |
| P9 | `forces-between-charges` | `p9-induction-wall` | diagram | `drawn` | The wall's electrons move a little way back. The surface is left slightly positive. |
| P9 | `forces-between-charges` | `p9-pairs-three` | diagram | `drawn` | The arrows show the force on each ball. |
