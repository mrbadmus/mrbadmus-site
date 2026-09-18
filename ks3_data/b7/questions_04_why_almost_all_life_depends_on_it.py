"""B7 lesson 04 — Why almost all life depends on it: twelve questions (MRB-269).

This lesson makes one claim in three parts — a producer is the way energy
enters a chain, the oxygen in the air is biological waste, and photosynthesis
is the living world's one route for taking carbon back out — and then argues
it from a plate of six foods. The bank probes all three jobs and the two
chains that carry the argument. The easier band holds what the jobs rest on:
where the atmosphere's oxygen came from, who does the sea's photosynthesis,
what a mushroom actually is, and what photosynthesis does to carbon dioxide.
The standard band works the instrument's own findings — that the step count
changes while the destination does not, that most of what a cow eats is
respired away, that "lungs of the planet" is wrong on both counts, and that
the bee adds no sugar. The harder band takes it somewhere new: the vent
communities behind the word *almost*, the ripening bacteria that look like
producers and are not, the sequence of the Great Oxidation run the wrong way
round, and a sealed jar where one organism has to do two of the three jobs at
once.

The distractors are built from the lesson's two declared misconceptions and
from the errors it corrects in passing. PLANT-07 ("trees are the lungs of the
planet") supplies the seaweed and zooplankton options in e02, the whole option
set of s03, and the sea-has-no-plants option in s01. PLANT-08 ("plants make
oxygen for us to breathe") supplies the deliberate-release option in e01 and
the "nothing is wrong" option in h03. Four errors the lesson corrects while
passing supply the rest: that the released oxygen comes out of the carbon
dioxide rather than out of split water (e01, e04), that minerals or soil carry
energy (e03, s04), that each organism in a chain adds energy of its own (s01,
s02), and that a decomposer sits outside a food chain rather than at the end
of one (e03, h02).

`figure` is None throughout — this lesson declares no figures at all, so there
is nothing a question could legitimately point at.
"""

UNIT = "B7"
LESSON = "why-almost-all-life-depends-on-it"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-04-e01",
        "band": "easier",
        "text": "The atmosphere is about a fifth oxygen. Where did all of "
                "that oxygen come from?",
        "options": [
            {"text": "From carbon dioxide, split apart by plants to release "
                     "the oxygen locked inside it.",
             "correct": False,
             "why": "The oxygen a plant releases comes from splitting water, "
                    "not carbon dioxide. The atoms of the carbon dioxide end "
                    "up in the glucose the plant builds."},
            {"text": "It was part of the atmosphere from the moment the Earth "
                     "first formed.",
             "correct": False,
             "why": "There was no oxygen worth mentioning for the first two "
                    "billion years of Earth's history. Every molecule of it "
                    "in the air today is biological in origin."},
            {"text": "Photosynthesis released it over billions of years, as "
                     "the waste from splitting water.",
             "correct": True},
            {"text": "Plants release it deliberately, to keep the air "
                     "breathable for the animals around them.",
             "correct": False,
             "why": "Nothing in biology is done for another organism's "
                    "benefit. Oxygen is waste — what is left over when a "
                    "plant splits water to build glucose."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e02",
        "band": "easier",
        "text": "Roughly half of the world's photosynthesis happens in the "
                "sea. Which organisms are doing it?",
        "options": [
            {"text": "Phytoplankton — microscopic algae with chlorophyll, "
                     "drifting in the sunlit surface water.",
             "correct": True},
            {"text": "Zooplankton — the tiny drifting animals that fill the "
                     "surface water in enormous numbers.",
             "correct": False,
             "why": "Zooplankton are animals, and they eat phytoplankton. "
                    "Being small and drifting does not make an organism a "
                    "producer; having chlorophyll and building sugar does."},
            {"text": "Seaweed, rooted on the sea floor around the edges of "
                     "every continent.",
             "correct": False,
             "why": "Seaweeds are photosynthetic, but they are stuck in "
                    "shallow water near coasts. The bulk of the sea's "
                    "production is done by algae too small to see."},
            {"text": "Bacteria around deep-sea vents, where hot water carries "
                     "dissolved chemicals out of the rock.",
             "correct": False,
             "why": "Those bacteria build sugars from chemical energy rather "
                    "than light — that is chemosynthesis, and it is a rare "
                    "exception, not half the planet's photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e03",
        "band": "easier",
        "text": "The mushroom you see is only part of the organism. What is "
                "the rest of it, and what is it doing?",
        "options": [
            {"text": "A root system pulling minerals and water out of the "
                     "soil, the way a plant's roots do.",
             "correct": False,
             "why": "Fungi have no roots, and minerals carry no energy — to a "
                    "fungus or to anything else. The threads are digesting "
                    "dead plant material that a leaf built."},
            {"text": "A green underground stem that photosynthesises in the "
                     "dark and feeds the mushroom above it.",
             "correct": False,
             "why": "Nothing photosynthesises in the dark, and fungi have no "
                    "chlorophyll anywhere. Everything a fungus lives on was "
                    "built by something else, some time ago."},
            {"text": "Nothing — the mushroom is the whole organism, which is "
                     "why it can appear overnight.",
             "correct": False,
             "why": "It appears overnight because it is only the fruiting "
                    "body. The organism itself has been feeding in the "
                    "compost or dead wood for a long time already."},
            {"text": "A network of threads through compost or dead wood, "
                     "digesting dead material from the outside in.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e04",
        "band": "easier",
        "text": "Respiration, decay and burning all put carbon dioxide into "
                "the air. What is photosynthesis doing about it?",
        "options": [
            {"text": "It breaks the carbon dioxide apart and destroys the "
                     "carbon that was inside it.",
             "correct": False,
             "why": "No reaction destroys atoms. The carbon is built into "
                    "organic molecules and locked into wood, roots and ocean "
                    "sediment — moved, not destroyed."},
            {"text": "It takes carbon dioxide back out, locking the carbon "
                     "into wood, roots and ocean sediment.",
             "correct": True},
            {"text": "Nothing — once carbon dioxide is in the air there is no "
                     "way of removing it again.",
             "correct": False,
             "why": "Taking it back out is the third of the three jobs. "
                    "Photosynthesis is the living world's one route out of "
                    "the atmosphere, and it is why carbon dioxide can fall."},
            {"text": "It swaps the carbon dioxide for oxygen, atom for atom, "
                     "so that the air stays balanced.",
             "correct": False,
             "why": "The oxygen released comes from splitting water, not from "
                    "the carbon dioxide. The carbon and its oxygen atoms both "
                    "go into the sugar the plant builds."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-04-s01",
        "band": "standard",
        "text": "Bread is two steps back to a producer; salmon is four. What "
                "does that difference between them tell you?",
        "options": [
            {"text": "Salmon is further from photosynthesis, so part of its "
                     "energy must have come from somewhere else.",
             "correct": False,
             "why": "No chain on the plate has a second source. All six "
                    "arrive at a producer capturing sunlight, however many "
                    "steps it takes them to get there."},
            {"text": "Only how many organisms handled the molecules on the "
                     "way — both chains still end at photosynthesis.",
             "correct": True},
            {"text": "Salmon must store more energy, because four organisms "
                     "have each added some of their own to it.",
             "correct": False,
             "why": "Nothing in a chain adds energy. Each organism spends "
                    "most of what it eats on staying alive and passes on what "
                    "is left, so a longer chain delivers less."},
            {"text": "Bread depends on photosynthesis and salmon does not, "
                     "because there are no plants out in the sea.",
             "correct": False,
             "why": "There are producers in the sea — phytoplankton, "
                    "microscopic algae that photosynthesise exactly as a leaf "
                    "does. The salmon's chain ends with them."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s02",
        "band": "standard",
        "text": "A farmer can sell a field as wheat for bread, or feed the "
                "crop to cattle and sell beef. Which choice feeds more "
                "people, and why?",
        "options": [
            {"text": "The beef — meat carries far more energy per gram than "
                     "bread does.",
             "correct": False,
             "why": "Per gram, perhaps — but the field yields far fewer "
                    "grams. Around ten kilograms of grass go into every "
                    "kilogram of cow."},
            {"text": "Neither — the energy from the field is simply passed "
                     "along the chain either way.",
             "correct": False,
             "why": "Passed along is not passed on intact. Most of what the "
                    "cow eats is released again by respiration, to keep the "
                    "cow itself alive."},
            {"text": "The beef — the cow's own respiration adds energy to "
                     "what the grass supplied.",
             "correct": False,
             "why": "Respiration releases stored energy; it never creates "
                    "any. A cow adds nothing to the chain — it spends what "
                    "the grass captured from sunlight."},
            {"text": "The wheat — most of what a cow eats is respired away "
                     "rather than passed on.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s03",
        "band": "standard",
        "text": "Someone argues that rainforests must be protected because "
                "they are the lungs of the planet, supplying the world's "
                "oxygen. What is wrong with the argument?",
        "options": [
            {"text": "Half of all photosynthesis is in the sea, and a forest "
                     "consumes much of what it makes.",
             "correct": True},
            {"text": "Nothing is wrong — trees are the only organisms on "
                     "Earth putting oxygen into the air.",
             "correct": False,
             "why": "Plants, algae and some bacteria all photosynthesise, and "
                    "the sea's producers match every forest and grassland on "
                    "land put together."},
            {"text": "Forests only respire, so a forest takes oxygen out of "
                     "the air and never puts any back.",
             "correct": False,
             "why": "That overcorrects. A forest does release oxygen — it "
                    "also consumes much of what it produces, which makes it "
                    "closer to balanced than to a supply."},
            {"text": "Forests deal with carbon dioxide rather than oxygen, "
                     "and the two gases are unconnected.",
             "correct": False,
             "why": "Photosynthesis does both at once: the same reaction "
                    "takes carbon dioxide in and releases oxygen. Rainforests "
                    "are worth protecting, just not as an oxygen supply."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s04",
        "band": "standard",
        "text": "Honey is almost pure sugar, and a bee is an animal. So "
                "where was that sugar actually built?",
        "options": [
            {"text": "In the bee's body, which is what makes honey an animal "
                     "product rather than a plant one.",
             "correct": False,
             "why": "Bees evaporate the water off nectar and add enzymes. "
                    "They add no sugar at all — every gram of it was already "
                    "made when they found it."},
            {"text": "In pollen grains, which bees collect and press together "
                     "into a sugary paste.",
             "correct": False,
             "why": "Bees collect nectar to make honey, not pollen — and "
                    "pollen is a plant product too. Either way the sugar was "
                    "built in a leaf."},
            {"text": "In the plant, by photosynthesis, and put into nectar — "
                     "the bee only took the water out.",
             "correct": True},
            {"text": "In the soil the flower grew in, then drawn up the stem "
                     "and concentrated in the nectar.",
             "correct": False,
             "why": "Soil supplies water and minerals, never sugar, and "
                    "minerals carry no energy. The sugar in nectar is glucose "
                    "the plant made from carbon dioxide."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-04-h01",
        "band": "harder",
        "text": "Two and a half kilometres down, where no light has ever "
                "reached, tube worms two metres long live around hot water "
                "pouring out of the sea floor. Why is that community the "
                "exception the word almost is protecting?",
        "options": [
            {"text": "The worms carry chlorophyll and photosynthesise using "
                     "the glow given off by the hot water.",
             "correct": False,
             "why": "No light reaches that depth at all, and nothing there "
                    "photosynthesises. Energy enters the chain through "
                    "bacteria using chemical reactions instead."},
            {"text": "The community lives on dead material sinking down from "
                     "the sunlit water far above it.",
             "correct": False,
             "why": "That describes most deep-sea life, which does still "
                    "depend on photosynthesis. Vent communities are different "
                    "because their chains start somewhere else entirely."},
            {"text": "Bacteria at the base of those chains build sugars using "
                     "chemical energy instead of light.",
             "correct": True},
            {"text": "The worms need no energy source at all, because the hot "
                     "water is enough to keep them alive.",
             "correct": False,
             "why": "Heat is not food. Every organism needs organic molecules "
                    "built by something, and at a vent those molecules are "
                    "built by chemosynthetic bacteria."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h02",
        "band": "harder",
        "text": "The bacteria that ripen a cheese are living on the protein "
                "and fat in the milk. Where does that put them in the chain?",
        "options": [
            {"text": "One step further along the same chain — the molecules "
                     "they feed on were built in a grass leaf.",
             "correct": True},
            {"text": "Outside it — bacteria are decomposers, and a decomposer "
                     "is not part of any food chain.",
             "correct": False,
             "why": "Nothing that feeds on something else is outside a chain. "
                    "A decomposer sits at the end of one, in exactly the same "
                    "way the mushroom does."},
            {"text": "At the very start of it — bacteria are the smallest "
                     "organisms, so everything else sits above them.",
             "correct": False,
             "why": "Position in a chain is about where the molecules came "
                    "from, not about size. Phytoplankton are microscopic and "
                    "they are producers; these bacteria are not."},
            {"text": "They are producers themselves, because some bacteria "
                     "photosynthesise, so a bacterium can start a chain.",
             "correct": False,
             "why": "Some bacteria do photosynthesise — but not these ones. "
                    "These are living on sugars, proteins and fats a grass "
                    "plant built and a cow passed on."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h03",
        "band": "harder",
        "text": "A student writes: photosynthesis evolved to supply the "
                "oxygen that animals need to breathe. Using what this lesson "
                "says about the first two billion years, what is wrong with "
                "that sentence?",
        "options": [
            {"text": "Nothing is wrong — supplying breathable air is exactly "
                     "what photosynthesis is for.",
             "correct": False,
             "why": "Oxygen is a waste product, left over from splitting "
                    "water to build glucose. Nothing in biology is done for "
                    "another organism's benefit."},
            {"text": "Oxygen was always in the air anyway, so nothing ever "
                     "had to evolve to supply it.",
             "correct": False,
             "why": "There was no oxygen worth mentioning for the first two "
                    "billion years. It was supplied — by bacteria — just not "
                    "for anyone's benefit."},
            {"text": "The early oxygen came out of the sea itself rather than "
                     "out of anything that was alive.",
             "correct": False,
             "why": "It came out of living things that happened to live in "
                    "the sea. The origin of every oxygen molecule in the air "
                    "is biological, not geological."},
            {"text": "It runs backwards: oxygen built up as waste first, and "
                     "breathing animals came later.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h04",
        "band": "harder",
        "text": "A sealed glass jar of pond water, algae and a few tiny "
                "animals sits on a windowsill and stays alive for months, "
                "with nothing added but light. What are the algae supplying?",
        "options": [
            {"text": "Only the oxygen — the animals must be finding their "
                     "food somewhere else inside the jar.",
             "correct": False,
             "why": "There is nowhere else. In a sealed jar the only organic "
                    "molecules are the ones the algae built, so the food is "
                    "coming from them as well."},
            {"text": "Both the food and the oxygen — every organic molecule "
                     "and every breath in the jar came from them.",
             "correct": True},
            {"text": "Only the food — the oxygen was sealed in at the start "
                     "and there is enough of it to last months.",
             "correct": False,
             "why": "The animals and the algae both respire continuously and "
                    "would use it up. It is being replaced, which is the "
                    "second of photosynthesis's three jobs."},
            {"text": "Neither — the light coming through the glass supplies "
                     "the animals with energy directly.",
             "correct": False,
             "why": "An animal has no way of capturing light energy. Only a "
                    "photosynthetic organism can, which is why everything "
                    "else has to eat something."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-04-e05",
        "band": "easier",
        "text": "Almost all sea life lives in a thin layer near the surface "
                "of the ocean. Why?",
        "options": [
            {"text": "Because the water below that layer is far too cold for "
                     "anything to live in.",
             "correct": False,
             "why": "Life is found at every depth, including the sea floor. "
                    "What runs out with depth is the light the producers "
                    "need."},
            {"text": "Because the pressure below a hundred metres would crush "
                     "any living thing.",
             "correct": False,
             "why": "Animals live at depths of kilometres. What thins out "
                    "near the surface is the light rather than the "
                    "pressure."},
            {"text": "Because below about a hundred metres there is not "
                     "enough light for the producers.",
             "correct": True},
            {"text": "Because the sea floor holds no minerals for sea plants "
                     "to root in.",
             "correct": False,
             "why": "Minerals are not what a producer builds its food from, "
                    "and phytoplankton root in nothing at all. It is the "
                    "light that runs out."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e06",
        "band": "easier",
        "text": "Which group of living things can carry out photosynthesis?",
        "options": [
            {"text": "Plants, algae and some kinds of bacteria.",
             "correct": True},
            {"text": "Plants only, since chlorophyll is found nowhere else.",
             "correct": False,
             "why": "Algae in the sea photosynthesise with chlorophyll "
                    "exactly as a leaf does, and so do some bacteria. Plants "
                    "are not the whole group."},
            {"text": "Plants and fungi, since both grow rooted in one place.",
             "correct": False,
             "why": "Fungi have no chlorophyll and cannot photosynthesise at "
                    "all. They feed on material that something else built."},
            {"text": "Any organism small enough to drift in sunlit water.",
             "correct": False,
             "why": "Zooplankton are tiny and drift in sunlit water, and they "
                    "are animals that eat. What counts is chlorophyll and "
                    "building sugar."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e07",
        "band": "easier",
        "text": "What is an organic molecule?",
        "options": [
            {"text": "Any molecule found in the soil or in water that was "
                     "not made by people in a factory.",
             "correct": False,
             "why": "Where a molecule is found does not decide it. An organic "
                    "molecule is one built around carbon by a living thing."},
            {"text": "A molecule that carries energy but contains no carbon "
                     "at all.",
             "correct": False,
             "why": "Carbon is what they are all built around — sugars, "
                    "starches, proteins and fats."},
            {"text": "Any molecule that is dissolved in the water inside a "
                     "living cell.",
             "correct": False,
             "why": "Minerals dissolve in a cell's water and are not organic. "
                    "The word means built around carbon by a living thing."},
            {"text": "A molecule built around carbon by a living thing — a "
                     "sugar, a starch, a protein, a fat.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e08",
        "band": "easier",
        "text": "Three things photosynthesis does for everything else. Which "
                "list names all three?",
        "options": [
            {"text": "It supplies energy to food chains, it makes the "
                     "minerals in the soil, and it warms the atmosphere up.",
             "correct": False,
             "why": "Minerals come from rock rather than from this reaction, "
                    "and it warms nothing. The third job is taking carbon "
                    "dioxide back out of the air."},
            {"text": "It is the way energy enters food chains, it released "
                     "the oxygen in the air, and it takes carbon dioxide back "
                     "out.",
             "correct": True},
            {"text": "It supplies food to food chains, it removes the oxygen "
                     "animals do not need, and it adds carbon dioxide.",
             "correct": False,
             "why": "Those two gases are the wrong way round. Photosynthesis "
                    "releases oxygen and takes carbon dioxide out of the "
                    "air."},
            {"text": "It supplies food to food chains, it makes the rain "
                     "fall, and it keeps the level of oxygen steady.",
             "correct": False,
             "why": "Making rain is not one of the three. The third is taking "
                    "carbon dioxide back out of the atmosphere."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e09",
        "band": "easier",
        "text": "A slice of bread is two steps back to a producer. What is "
                "the wheat grain in the middle of that chain?",
        "options": [
            {"text": "A fruit the plant grows in order to attract the "
                     "animals that will eat it and carry its seeds away for "
                     "it later.",
             "correct": False,
             "why": "Wheat is pollinated by the wind and spreads no fruit. "
                    "The grain is a seed, packed with starch for the "
                    "seedling rather than for an animal."},
            {"text": "A store of the minerals the plant has drawn up out of "
                     "the soil.",
             "correct": False,
             "why": "Minerals are taken up in tiny amounts and carry no "
                    "energy. A grain is mostly starch, built from glucose "
                    "the leaves made."},
            {"text": "A seed — a store of starch the plant packed for its "
                     "own seedling, which we intercept.",
             "correct": True},
            {"text": "A swollen piece of the root, filled with the sugar "
                     "that the plant itself had no immediate use for.",
             "correct": False,
             "why": "A grain grows on the ear, at the top of the plant. It "
                    "is a seed, and what is packed into it is starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e10",
        "band": "easier",
        "text": "Which of these builds its own food out of carbon dioxide and "
                "water?",
        "options": [
            {"text": "Grass growing in a field.", "correct": True},
            {"text": "A mushroom growing on a log.",
             "correct": False,
             "why": "Fungi have no chlorophyll and cannot photosynthesise. A "
                    "mushroom digests material that something else built."},
            {"text": "A bee visiting a flower.",
             "correct": False,
             "why": "A bee collects nectar the plant made and adds no sugar "
                    "of its own. It is feeding rather than building."},
            {"text": "A cow grazing in a field.",
             "correct": False,
             "why": "Everything in a cow was built from what it ate. Only the "
                    "grass builds food out of carbon dioxide and water."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e11",
        "band": "easier",
        "text": "Burning coal releases carbon dioxide that was taken out of "
                "the air hundreds of millions of years ago. What took it out?",
        "options": [
            {"text": "Volcanoes, which drew the gas back down into the rock.",
             "correct": False,
             "why": "Volcanoes put carbon dioxide into the air rather than "
                    "taking it out. Coal formed from plants, and plants took "
                    "the gas out by photosynthesis."},
            {"text": "The oceans, which dissolved the gas and turned it into "
                     "coal.",
             "correct": False,
             "why": "Coal is the remains of plants rather than of sea water. "
                    "The carbon in it was taken from the air by "
                    "photosynthesis."},
            {"text": "Nothing did — the carbon in coal has been in the rock "
                     "since the Earth formed.",
             "correct": False,
             "why": "Coal is made of the remains of living things. Every "
                    "carbon atom in it was once carbon dioxide, built into a "
                    "plant."},
            {"text": "Photosynthesis, in the plants that those coal seams "
                     "formed from.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e12",
        "band": "easier",
        "text": "Plants photosynthesise. Do they respire as well, and if so, "
                "when?",
        "options": [
            {"text": "No — respiration is what animals do, and photosynthesis "
                     "is the plant version of it.",
             "correct": False,
             "why": "Every living thing respires, plants included. "
                    "Photosynthesis is a different reaction, running in the "
                    "opposite direction."},
            {"text": "Yes — plants respire all the time, day and night.",
             "correct": True},
            {"text": "Yes, but only at night, once photosynthesis has "
                     "stopped.",
             "correct": False,
             "why": "Respiration does not pause in the light. It runs day and "
                    "night, while photosynthesis runs only while there is "
                    "light."},
            {"text": "Yes, but only when a plant is short of light and has to "
                     "live off its store.",
             "correct": False,
             "why": "A plant respires whether it is well lit or not — that is "
                    "how it uses the energy in its store, at any hour of the "
                    "day."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e13",
        "band": "easier",
        "text": "A decomposer feeds on dead material. Where does that put it "
                "in a food chain?",
        "options": [
            {"text": "At the end of one, feeding on what the organisms before "
                     "it built.",
             "correct": True},
            {"text": "Outside every chain, since dead material is no longer "
                     "part of one.",
             "correct": False,
             "why": "The molecules are the same whether the organism is alive "
                    "or dead. A decomposer sits at the end of a chain, not "
                    "out of it."},
            {"text": "At the start of one, because it puts minerals back into "
                     "the soil.",
             "correct": False,
             "why": "Returning minerals is real and does not make an organism "
                    "a producer. A producer builds its own food; a decomposer "
                    "feeds on what was built."},
            {"text": "In the middle of one, between the producer and the "
                     "animal that eats it.",
             "correct": False,
             "why": "Decomposers feed on whatever has died, plant or animal, "
                    "so they sit at the end rather than in the middle."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-04-s05",
        "band": "standard",
        "text": "A farmed salmon is fed pellets made from smaller fish and "
                "from crops such as rapeseed. Does that change where its "
                "chain ends?",
        "options": [
            {"text": "Yes — a farmed fish is fed by people, so its chain "
                     "begins at the factory that makes the pellets.",
             "correct": False,
             "why": "A factory presses and mixes; it builds no organic "
                    "molecules of its own. Both ingredients trace back to "
                    "producers."},
            {"text": "Yes — the crop part of the pellet ends at a producer, "
                     "but the fish part does not.",
             "correct": False,
             "why": "The smaller fish ate other organisms, and that chain "
                    "runs back to phytoplankton. Both halves of the pellet "
                    "end at a producer."},
            {"text": "No — the crop ends at a plant and the fish meal ends at "
                     "phytoplankton, so both run back to photosynthesis.",
             "correct": True},
            {"text": "No — because pellets carry no energy of their own, so "
                     "nothing about the chain has changed.",
             "correct": False,
             "why": "Pellets carry plenty of energy; that is why they are "
                    "fed. What matters is that the energy came from producers "
                    "either way."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s06",
        "band": "standard",
        "text": "A student says eating meat is wasteful because energy is "
                "destroyed at every step of a food chain. Correct that "
                "sentence.",
        "options": [
            {"text": "Energy is not destroyed — most of it is released by "
                     "respiration and passes to the surroundings instead of "
                     "being passed on.",
             "correct": True},
            {"text": "Energy is not destroyed and none of it is lost either, "
                     "so a chain wastes nothing at all.",
             "correct": False,
             "why": "Very little of what a cow eats reaches the person who "
                    "eats the cow. It is not destroyed, but it is certainly "
                    "not all passed on."},
            {"text": "Energy is destroyed, and that is why a longer chain "
                     "delivers less at the end of it.",
             "correct": False,
             "why": "Energy is never destroyed. It is transferred to the "
                    "surroundings by respiration, which is why less is left "
                    "for the next organism."},
            {"text": "Energy is destroyed only when an organism dies without "
                     "being eaten, so nothing is wasted while a chain is "
                     "working.",
             "correct": False,
             "why": "Nothing destroys energy at any point. Even a body that "
                    "nothing eats is worked through by decomposers."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s07",
        "band": "standard",
        "text": "A fungus eats no living organism at all. Why is it still not "
                "a producer?",
        "options": [
            {"text": "Because it grows in the dark under the soil, and a "
                     "producer has to live somewhere that the light can "
                     "reach.",
             "correct": False,
             "why": "Where an organism lives is not the test. What settles it "
                    "is whether it builds its own organic molecules."},
            {"text": "Because it has no roots with which to take up raw "
                     "materials.",
             "correct": False,
             "why": "Roots are not the test either. Phytoplankton have none "
                    "and are producers, because they build sugar from carbon "
                    "dioxide."},
            {"text": "Because it has no green colour anywhere in it, and "
                     "only green organisms are counted as producers.",
             "correct": False,
             "why": "Colour is not the test — some photosynthetic bacteria "
                    "are not green. What matters is building your own food."},
            {"text": "Because it feeds on molecules that something else "
                     "built, instead of building its own.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s08",
        "band": "standard",
        "text": "Why is it wrong to say that plants make oxygen for us, but "
                "right to say that we depend on the oxygen plants make?",
        "options": [
            {"text": "Both sentences are wrong, since the oxygen in the air "
                     "was never made by living things.",
             "correct": False,
             "why": "All of it was. Every molecule of oxygen in the "
                    "atmosphere was released by a photosynthetic organism."},
            {"text": "Because oxygen is waste from building glucose, and "
                     "depending on something is not the same as being given "
                     "it.",
             "correct": True},
            {"text": "Because the oxygen is made for other plants rather than "
                     "for animals.",
             "correct": False,
             "why": "It is not made for anyone at all. Oxygen is what is left "
                    "over when a plant splits water to build glucose."},
            {"text": "Because plants make the oxygen and we make the carbon "
                     "dioxide, so both sentences describe a fair exchange.",
             "correct": False,
             "why": "The exchange is real and neither side is doing it for "
                    "the other. The word that has to go is for."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s09",
        "band": "standard",
        "text": "A young growing forest takes carbon dioxide out of the air. "
                "A mature forest of the same size takes out far less. "
                "Explain.",
        "options": [
            {"text": "A mature forest's leaves are much older, so the "
                     "chlorophyll in them no longer absorbs light properly.",
             "correct": False,
             "why": "Its leaves are new each year and work perfectly well. "
                    "What has changed is the balance between growth and "
                    "decay."},
            {"text": "A mature forest has stopped photosynthesising, since "
                     "only young trees do it.",
             "correct": False,
             "why": "A mature forest photosynthesises enormously. It also "
                    "respires and decays at about the same rate, which is the "
                    "point."},
            {"text": "In a mature forest, new growth locks up as much carbon "
                     "as respiration and decay return.",
             "correct": True},
            {"text": "A mature forest is shaded by its own canopy, so almost "
                     "no light reaches any of the leaves lower down inside "
                     "it.",
             "correct": False,
             "why": "The canopy is the part in full sunlight. The difference "
                    "is that a mature forest is no longer piling up new "
                    "wood."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s10",
        "band": "standard",
        "text": "A student argues that since photosynthesis puts oxygen into "
                "the air and respiration takes it out, the amount in the "
                "atmosphere can never have changed. What is wrong with that?",
        "options": [
            {"text": "The two have not balanced over the Earth's history — "
                     "oxygen built up from almost none to about a fifth of "
                     "the air.",
             "correct": True},
            {"text": "Nothing is wrong with it, which is why the level of "
                     "oxygen has stayed at about a fifth ever since the "
                     "Earth formed.",
             "correct": False,
             "why": "There was no oxygen worth mentioning for the first two "
                    "billion years. It built up, so the two clearly have not "
                    "cancelled."},
            {"text": "Respiration does not use oxygen, so there is nothing "
                     "for photosynthesis to balance against.",
             "correct": False,
             "why": "Respiration uses oxygen — that is why you breathe. The "
                    "point is that the two have not balanced over billions of "
                    "years."},
            {"text": "Only animals respire, so plants are adding oxygen with "
                     "nothing taking it away again.",
             "correct": False,
             "why": "Plants respire too, day and night. What settles the "
                    "argument is that the level rose over billions of "
                    "years."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s11",
        "band": "standard",
        "text": "A student says that because plants respire too, a plant must "
                "use up all the oxygen it makes and so cannot supply any. "
                "What is wrong?",
        "options": [
            {"text": "Plants respire only during the night, so the whole of "
                     "the oxygen they make during the day is left over.",
             "correct": False,
             "why": "Plants respire day and night. The reason there is a "
                    "surplus is that in the light photosynthesis runs much "
                    "faster than respiration."},
            {"text": "Plants do not respire at all, which is why they need no "
                     "oxygen of their own.",
             "correct": False,
             "why": "Every living thing respires. What leaves a surplus is "
                    "that in the light a plant photosynthesises far faster "
                    "than it respires."},
            {"text": "The student is right, and the oxygen in the air must "
                     "have come out of the rocks and the oceans instead of "
                     "from plants.",
             "correct": False,
             "why": "All of it came from photosynthetic organisms. A plant in "
                    "the light releases far more oxygen than its own "
                    "respiration uses."},
            {"text": "In the light a plant photosynthesises much faster than "
                     "it respires, so oxygen is left over.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s12",
        "band": "standard",
        "text": "A student writes that the Sun feeds every living thing. "
                "Rewrite that so it is accurate.",
        "options": [
            {"text": "The Sun feeds the producers directly, and they pass "
                     "the food they are given on along the rest of the "
                     "chain.",
             "correct": False,
             "why": "Nothing is given to a producer. It builds its own food "
                    "out of carbon dioxide and water, using the energy in "
                    "sunlight."},
            {"text": "The Sun supplies energy producers store in molecules "
                     "that everything else eats.",
             "correct": True},
            {"text": "The Sun feeds animals directly through their skin and "
                     "feeds the plants through their leaves.",
             "correct": False,
             "why": "No animal can capture light energy. Only a "
                    "photosynthetic organism can, which is why everything "
                    "else has to eat."},
            {"text": "The Sun supplies the carbon that every living thing is "
                     "built from.",
             "correct": False,
             "why": "The carbon comes from carbon dioxide in the air. What "
                    "the Sun supplies is energy, not matter."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s13",
        "band": "standard",
        "text": "Antarctic krill feed on phytoplankton under the sea ice, and "
                "whales feed on krill. In a year when the ice stays late and "
                "little light reaches the water, krill numbers fall. Explain "
                "the link.",
        "options": [
            {"text": "The ice keeps the krill away from the surface where "
                     "they feed, so they starve in the deeper water below "
                     "it.",
             "correct": False,
             "why": "Krill can move; their food cannot be made. Less light "
                    "means less photosynthesis, so less food enters the "
                    "chain."},
            {"text": "The cold slows the krill down, so the whales catch far "
                     "more of them.",
             "correct": False,
             "why": "The whales' feeding is not what has changed. Less light "
                    "reaching the water means the producers build less, and "
                    "the chain has less to pass on."},
            {"text": "Less light means the phytoplankton photosynthesise "
                     "less, so less food enters the chain.",
             "correct": True},
            {"text": "The ice takes the dissolved oxygen out of the water "
                     "underneath it, so the krill cannot respire.",
             "correct": False,
             "why": "Ice does not strip the oxygen out of the sea. The link "
                    "that matters here is light, photosynthesis and food."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-04-h05",
        "band": "harder",
        "text": "A field grows 12 000 kg of grass in a season. Taking around "
                "ten kilograms of grass for every kilogram of cow, roughly "
                "how much cow could that field produce?",
        "options": [
            {"text": "About 120 000 kg, since ten kilograms of grass go into "
                     "every kilogram of cow.",
             "correct": False,
             "why": "You have multiplied where you should have divided. Ten "
                    "kilograms of grass make one of cow, so the answer is "
                    "smaller than the crop, not larger."},
            {"text": "About 1200 kg, since 12 000 divided by ten is 1200.",
             "correct": True},
            {"text": "About 12 000 kg, since all of the grass ends up as cow "
                     "in the end.",
             "correct": False,
             "why": "Most of what a cow eats is respired away to keep the cow "
                    "alive, which is exactly what the ten-to-one figure "
                    "records."},
            {"text": "About 10 kg, since ten kilograms of grass make one "
                     "kilogram of cow.",
             "correct": False,
             "why": "The ten to one is a ratio rather than a total. Divide "
                    "the whole crop by ten and the field yields about 1200 "
                    "kg."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h06",
        "band": "harder",
        "text": "Suppose all the world's phytoplankton died. Which of "
                "photosynthesis's three jobs would be affected?",
        "options": [
            {"text": "Only the first, since the chains in the sea would "
                     "empty while the air itself stayed exactly as it is at "
                     "the moment.",
             "correct": False,
             "why": "The sea's producers do about half of the world's "
                    "photosynthesis, so the oxygen and the carbon dioxide "
                    "would both be affected as well."},
            {"text": "Only the second, since their oxygen would stop "
                     "reaching the atmosphere.",
             "correct": False,
             "why": "That is one of the three. The chains above them would "
                    "empty too, and half the world's carbon dioxide removal "
                    "would stop."},
            {"text": "None of them, since the land plants would simply "
                     "photosynthesise more to make up the difference.",
             "correct": False,
             "why": "Land plants cannot spread out over the ocean. Roughly "
                    "half of the world's photosynthesis would simply be "
                    "gone."},
            {"text": "All three — the sea's chains empty, less oxygen added, "
                     "less carbon dioxide removed.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h07",
        "band": "harder",
        "text": "Someone argues that because roughly half of photosynthesis "
                "happens in the sea, felling a rainforest is only half as bad "
                "as people say. What is wrong with the reasoning?",
        "options": [
            {"text": "It treats oxygen as the only thing a forest does, and "
                     "the carbon a forest holds is released when it is "
                     "cleared.",
             "correct": True},
            {"text": "Nothing is wrong with it, since the oxygen figure is "
                     "roughly right and supplying oxygen is what a forest "
                     "is for.",
             "correct": False,
             "why": "The oxygen figure is roughly right and it is not the "
                    "whole account. Clearing a forest releases the carbon in "
                    "the wood and empties the chains living there."},
            {"text": "It is wrong because the sea does almost no "
                     "photosynthesis at all.",
             "correct": False,
             "why": "The sea does roughly half of it. What the argument "
                    "leaves out is everything a forest does besides "
                    "oxygen."},
            {"text": "It is wrong because a mature forest produces far more "
                     "oxygen than the whole ocean does.",
             "correct": False,
             "why": "A mature forest consumes much of what it produces. Its "
                    "value lies in the carbon it stores and the life it "
                    "holds."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h08",
        "band": "harder",
        "text": "Deep caves where no light has ever reached hold whole "
                "communities living on bat droppings and leaf litter washed "
                "in from outside. Are those chains an exception, like the "
                "deep-sea vents?",
        "options": [
            {"text": "Yes — no light reaches a cave, so nothing living in one "
                     "can depend on photosynthesis.",
             "correct": False,
             "why": "The material arriving does the depending for them. Every "
                    "scrap of it was built by a plant outside, in the light."},
            {"text": "Yes — the organisms there build their own food out of "
                     "the rock, as vent bacteria do.",
             "correct": False,
             "why": "Vent bacteria use energy from chemical reactions. A cave "
                    "community is living on material carried in from a lit "
                    "world."},
            {"text": "No — everything they live on was built by "
                     "photosynthesis outside the cave and carried in.",
             "correct": True},
            {"text": "No — because a faint light does reach a cave, and the "
                     "organisms there are able to use it.",
             "correct": False,
             "why": "There is genuinely no light deep in a cave. What makes "
                    "it not an exception is the food arriving from outside."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h09",
        "band": "harder",
        "text": "A sealed jar of pond water, algae and small animals lives "
                "for months on a windowsill. An identical jar is put in a "
                "dark cupboard. Predict what happens, and explain it.",
        "options": [
            {"text": "Only the animals die, and the algae live on the "
                     "minerals in the water.",
             "correct": False,
             "why": "Minerals supply no energy. Without light the algae "
                    "cannot build anything and go the same way as the "
                    "animals."},
            {"text": "Everything dies — nothing captures energy, so no food "
                     "is built and no oxygen replaced.",
             "correct": True},
            {"text": "Everything survives, because a sealed jar holds on to "
                     "all of its own food and all of its oxygen.",
             "correct": False,
             "why": "Both are being spent all the time by respiration. In the "
                    "light they are replaced; in the dark they are not."},
            {"text": "Only the algae die, and the animals live on for months "
                     "on the food and oxygen already dissolved in the water.",
             "correct": False,
             "why": "The animals were eating the algae and breathing the "
                    "oxygen the algae released. Both supplies stop at the "
                    "same time."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h10",
        "band": "harder",
        "text": "The middle of a compost heap gets warm. What is happening in "
                "there, and which way is the carbon moving?",
        "options": [
            {"text": "Decomposers respire as they feed, and the carbon "
                     "returns to the air as carbon dioxide.",
             "correct": True},
            {"text": "The heap is photosynthesising in the dark inside it, "
                     "and the carbon in it is being locked away into new "
                     "material.",
             "correct": False,
             "why": "Nothing photosynthesises without light, and there is no "
                    "chlorophyll left in a compost heap. What is going on is "
                    "decay."},
            {"text": "The rotting material is burning slowly, and the heat "
                     "destroys its carbon.",
             "correct": False,
             "why": "No reaction destroys carbon. The heap is warm because "
                    "organisms in it are respiring, and the carbon leaves as "
                    "carbon dioxide."},
            {"text": "The heap is drawing carbon dioxide out of the air "
                     "around it, which is why compost improves a soil.",
             "correct": False,
             "why": "Compost does feed a soil, and it is releasing carbon "
                    "dioxide rather than taking any in. Decomposers respire "
                    "like everything else."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h11",
        "band": "harder",
        "text": "Someone says that because photosynthesis takes carbon "
                "dioxide out of the air, planting trees can simply undo the "
                "burning of fossil fuels. What is the strongest objection?",
        "options": [
            {"text": "Trees take in no carbon dioxide at all until they are "
                     "fully grown.",
             "correct": False,
             "why": "A young growing tree is exactly the one locking carbon "
                    "into new wood. The objection is about how much, and for "
                    "how long."},
            {"text": "Trees release all their carbon again every autumn, when "
                     "their leaves fall.",
             "correct": False,
             "why": "Some returns through the leaf litter, and the trunk "
                    "holds the rest for as long as the tree stands. The real "
                    "difficulty is scale and timescale."},
            {"text": "Photosynthesis cannot remove carbon dioxide from the "
                     "air at all — only the oceans and the rocks can do "
                     "that.",
             "correct": False,
             "why": "Photosynthesis is the living world's route out of the "
                    "atmosphere. The problem is the rate, not whether it "
                    "happens."},
            {"text": "A tree holds its carbon only while it stands, and "
                     "fossil fuels return carbon that was locked away over "
                     "millions of years.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h12",
        "band": "harder",
        "text": "Many crops cannot be grown without bees to pollinate them. "
                "Someone argues that this makes bees producers, since without "
                "them there would be no food. What is wrong with that?",
        "options": [
            {"text": "Bees do build sugar, since they turn nectar into honey "
                     "inside their own bodies.",
             "correct": False,
             "why": "Bees evaporate water off nectar and add enzymes; they "
                    "add no sugar. Every gram of it was built in a leaf."},
            {"text": "Nothing is wrong with it — anything that a food chain "
                     "could not manage without counts as a producer.",
             "correct": False,
             "why": "Being essential is not what the word means. A producer "
                    "is an organism that builds its own organic molecules."},
            {"text": "Producer describes what an organism builds, not how "
                     "important it is — and a bee feeds on sugar a plant "
                     "made.",
             "correct": True},
            {"text": "Bees are decomposers rather than producers, since they "
                     "feed on the remains of flowers.",
             "correct": False,
             "why": "Nectar is a living plant's product rather than dead "
                    "material. Either way, a bee feeds on something a plant "
                    "built."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h13",
        "band": "harder",
        "text": "A spacecraft must carry a crew for three years with no "
                "resupply. An engineer proposes tanks of algae under lamps "
                "instead of stored food and oxygen. Which jobs would the "
                "algae do, and what must still be supplied?",
        "options": [
            {"text": "Food and oxygen — the crew must still supply light "
                     "energy, carbon dioxide and water.",
             "correct": True},
            {"text": "Food only, since oxygen cannot be released into "
                     "anything unless there is already an atmosphere around "
                     "the tanks.",
             "correct": False,
             "why": "Oxygen is released into whatever the algae are sealed "
                    "in. Both jobs are done; what has to be supplied is "
                    "energy and raw materials."},
            {"text": "Oxygen only, since algae are far too small to be worth "
                     "eating.",
             "correct": False,
             "why": "Algae feed enormous numbers of animals in the sea, and "
                    "they are grown as food. They would supply both."},
            {"text": "Neither, since a closed system cannot work without a "
                     "bed of soil for the algae to root themselves in.",
             "correct": False,
             "why": "Algae drift and have no roots at all. What a closed "
                    "system does need is a supply of light energy and raw "
                    "materials."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-04-e14",
        "band": "easier",
        "text": "Photosynthesis is the way energy enters almost every food "
                "chain. If it stopped completely, what would happen?",
        "options": [
            {"text": "Every chain above the producers would empty from the "
                     "bottom up, because nothing new would be entering them.",
             "correct": True},
            {"text": "Nothing would change straight away, because animals "
                     "store enough energy to keep every chain going "
                     "indefinitely.",
             "correct": False,
             "why": "Animals hold only a short-term store. Without new "
                    "energy entering, that store runs out and every chain "
                    "above the producers fails."},
            {"text": "Only the chains in the sea would be affected, since "
                     "land plants would keep working exactly as before.",
             "correct": False,
             "why": "Land plants capture sunlight in exactly the same way as "
                    "the sea's algae. Losing job one would stop energy "
                    "entering on land as well as at sea."},
            {"text": "Decomposers would take over as the new producers, since "
                     "they already feed at the end of every chain.",
             "correct": False,
             "why": "A decomposer feeds on what a producer already built; it "
                    "cannot start building organic molecules of its own, so "
                    "it cannot replace the job producers do."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e15",
        "band": "easier",
        "text": "Photosynthesis releases oxygen into the air. If every "
                "photosynthetic organism vanished overnight, what would "
                "happen to the oxygen level?",
        "options": [
            {"text": "It would stay exactly where it is, since the oxygen "
                     "already in the atmosphere cannot be used up.",
             "correct": False,
             "why": "Every respiring organism keeps drawing on that oxygen. "
                    "With nothing left to add fresh oxygen, the level would "
                    "fall rather than hold steady."},
            {"text": "It would fall over time, because nothing would be "
                     "adding fresh oxygen while respiration kept using it "
                     "up.",
             "correct": True},
            {"text": "It would rise at first, because decomposers would "
                     "suddenly have far more dead material to work through.",
             "correct": False,
             "why": "Decomposers respire like every other organism, using "
                    "oxygen rather than releasing it. More dead material "
                    "means more oxygen used, not more supplied."},
            {"text": "It would fall immediately to zero, since almost every "
                     "oxygen molecule in the air is used within a single "
                     "day.",
             "correct": False,
             "why": "The atmosphere holds an enormous reserve of oxygen "
                    "built up over billions of years. Losing the supply "
                    "would lower the level gradually, not empty it in a "
                    "day."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e16",
        "band": "easier",
        "text": "Photosynthesis takes carbon dioxide back out of the air. If "
                "that stopped completely, what would happen to the level of "
                "carbon dioxide over time?",
        "options": [
            {"text": "It would stay level, since respiration and decay would "
                     "also slow down to match.",
             "correct": False,
             "why": "Respiration and decay do not slow down just because "
                    "photosynthesis has stopped; they would keep adding "
                    "carbon dioxide with nothing removing it."},
            {"text": "It would fall, because burning and decay would use up "
                     "the carbon dioxide that is already there.",
             "correct": False,
             "why": "Burning and decay release carbon dioxide, they do not "
                    "remove it. Nothing would be left to take it back out."},
            {"text": "It would only ever rise, since respiration, decay and "
                     "burning would all keep adding it with nothing taking "
                     "it out.",
             "correct": True},
            {"text": "It would rise for a while and then reverse on its own, "
                     "once the level got high enough.",
             "correct": False,
             "why": "Nothing about a higher level makes carbon dioxide "
                    "remove itself. Without the living world's one route "
                    "out, there is no mechanism to reverse the rise."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e17",
        "band": "easier",
        "text": "A dairy herd is fed silage rather than fresh grass through "
                "the winter months. What is silage?",
        "options": [
            {"text": "A mineral supplement added to a cow's water, meant to "
                     "replace nutrients missing from winter grass rather "
                     "than to supply any energy of its own.",
             "correct": False,
             "why": "Silage is a feed in its own right rather than a mineral "
                    "additive, and it supplies energy rather than minerals."},
            {"text": "Dried hay that has been baked to remove all of its "
                     "water content before storage.",
             "correct": False,
             "why": "Silage is preserved wet rather than dried; it is "
                    "fermented and stored sealed away from air, not baked."},
            {"text": "A manufactured feed pellet with no connection to "
                     "anything the field itself grew.",
             "correct": False,
             "why": "Silage is made from the farm's own grass rather than "
                    "manufactured elsewhere, so the energy in it still "
                    "traces back to that field's photosynthesis."},
            {"text": "Preserved grass, cut and stored so that a herd can "
                     "still be fed once fresh grass has stopped growing.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e18",
        "band": "easier",
        "text": "A cow's rumen contains bacteria that break the grass down "
                "before any of it reaches the cow's own tissues. Where do "
                "those bacteria sit in the grass-to-steak chain?",
        "options": [
            {"text": "Between the grass and the cow, one extra step feeding "
                     "on the same photosynthesis before the cow's tissues "
                     "do.",
             "correct": True},
            {"text": "Before the grass, since bacteria are decomposers and "
                     "every chain has to start with one.",
             "correct": False,
             "why": "A producer capturing sunlight starts a chain, not a "
                    "decomposer. The grass comes first; the bacteria act on "
                    "it afterwards."},
            {"text": "Outside the chain entirely, since they live inside the "
                     "cow rather than out in the field.",
             "correct": False,
             "why": "Where an organism lives does not remove it from a "
                    "chain. Feeding on the grass's molecules puts the "
                    "bacteria inside the chain, wherever they live."},
            {"text": "After the cow, since the bacteria only appear once the "
                     "steak has already been eaten.",
             "correct": False,
             "why": "The bacteria are at work in the rumen before the cow's "
                    "own body absorbs anything, not afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e19",
        "band": "easier",
        "text": "Zooplankton drift in the sunlit surface water and feed on "
                "phytoplankton. Where does that put zooplankton in a food "
                "chain?",
        "options": [
            {"text": "At the very start of the chain, since they are as "
                     "small as the producers they live alongside.",
             "correct": False,
             "why": "Size does not decide a chain's starting point. Feeding "
                    "on phytoplankton rather than building their own food "
                    "puts zooplankton after the producer, not at the "
                    "start."},
            {"text": "One step after the producer, as the first animal to "
                     "feed on what the phytoplankton built.",
             "correct": True},
            {"text": "In the same position as phytoplankton, since both "
                     "drift in the same surface water.",
             "correct": False,
             "why": "Sharing a habitat does not make two organisms the same "
                    "kind. Phytoplankton build their own food; zooplankton "
                    "eat it, which puts them a step further along."},
            {"text": "Outside any chain, because a drifting animal is too "
                     "small to count as a proper link in a chain like this "
                     "one.",
             "correct": False,
             "why": "Size has no bearing on whether an organism belongs to a "
                    "chain. Zooplankton feed on phytoplankton, which makes "
                    "them a genuine link."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e20",
        "band": "easier",
        "text": "A food chain is drawn as a single line, but a real animal's "
                "diet is more like a web. What does a food web show that a "
                "single chain does not?",
        "options": [
            {"text": "It shows that a chain can be any length at all, "
                     "whereas a web is fixed at exactly three links.",
             "correct": False,
             "why": "A web is not a fixed length; the branching between "
                    "organisms is the point of a web, not a rule about link "
                    "count."},
            {"text": "It shows a series of chains laid end to end, one after "
                     "another, rather than side by side.",
             "correct": False,
             "why": "End to end is still just one long chain. A web's "
                    "branching connections, not its length, is what a "
                    "single chain leaves out."},
            {"text": "It shows that one organism can feed on, or be fed on "
                     "by, several different organisms at once.",
             "correct": True},
            {"text": "It replaces producers with decomposers as the "
                     "organism every chain starts from, since a web is built "
                     "the opposite way round from a chain.",
             "correct": False,
             "why": "A web still starts with producers, exactly as a chain "
                    "does. What changes is the number of connections drawn "
                    "between organisms, not which kind starts it."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e21",
        "band": "easier",
        "text": "The ocean dissolves carbon dioxide straight out of the air "
                "on a large scale. Why is that described as a non-biological "
                "removal?",
        "options": [
            {"text": "Because the ocean takes out more carbon dioxide each "
                     "year than every plant on Earth put together.",
             "correct": False,
             "why": "How much is removed is not what the word is about. It is "
                    "about whether a living thing is doing the removing."},
            {"text": "Because carbon dioxide dissolved in seawater is a "
                     "different gas from the one plants take in.",
             "correct": False,
             "why": "It is the same gas either way. Non-biological describes "
                    "the process, not the substance being removed."},
            {"text": "Because it happens in the parts of the ocean where "
                     "nothing is living.",
             "correct": False,
             "why": "It happens right across the ocean surface, living or "
                    "not. The word describes the mechanism, not the place."},
            {"text": "Because a gas dissolving in water is a physical "
                     "process, with no living thing doing it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e22",
        "band": "easier",
        "text": "Over very long timescales, the slow weathering of certain "
                "rocks also removes carbon dioxide from the atmosphere. What "
                "is that process called?",
        "options": [
            {"text": "Silicate weathering.", "correct": True},
            {"text": "Photosynthetic weathering, since it uses the same "
                     "chemistry as building glucose from carbon dioxide.",
             "correct": False,
             "why": "Weathering is a chemical reaction between rock and "
                    "rainwater; it shares no chemistry with photosynthesis "
                    "despite both removing the same gas."},
            {"text": "Biological decay, since minerals in rock are broken "
                     "down the same way dead material is.",
             "correct": False,
             "why": "Rock is not living material, and nothing decays it the "
                    "way a decomposer breaks down dead tissue. Weathering is "
                    "a chemical reaction with rainwater, not decay."},
            {"text": "Ocean acidification, since dissolved carbon dioxide "
                     "reacts with the rock beneath the sea floor.",
             "correct": False,
             "why": "Ocean acidification is a consequence of dissolved "
                    "carbon dioxide, not the name for rock removing it from "
                    "the air."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e23",
        "band": "easier",
        "text": "Food chains are built from producers and consumers. What "
                "does it mean to call an organism a consumer?",
        "options": [
            {"text": "It sits at the very end of a chain, because nothing "
                     "else feeds on it once it has eaten.",
             "correct": False,
             "why": "Plenty of consumers are eaten by something else further "
                    "along. The word is about how an organism gets its food, "
                    "not where it sits."},
            {"text": "It gets its food by eating other organisms, and never "
                     "builds any of its own.",
             "correct": True},
            {"text": "It uses up oxygen when it respires, which a producer "
                     "does not have to do.",
             "correct": False,
             "why": "Producers respire and use oxygen too, exactly as "
                    "consumers do. What marks a consumer out is that it eats "
                    "to get its food."},
            {"text": "It eats only plants, which is what separates it from a "
                     "producer further up the chain.",
             "correct": False,
             "why": "An organism that eats only plants is a herbivore, and "
                    "one that eats animals is a consumer just the same. The "
                    "test is eating rather than building."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e24",
        "band": "easier",
        "text": "Some bacteria photosynthesise and some carry out "
                "chemosynthesis instead. What is the key difference between "
                "the two?",
        "options": [
            {"text": "Photosynthetic bacteria build glucose to store energy "
                     "for themselves, and chemosynthetic bacteria are "
                     "sometimes described as building oxygen for other "
                     "organisms to use instead.",
             "correct": False,
             "why": "Both processes build organic molecules such as "
                    "glucose. The difference between them is the energy "
                    "source, not the product."},
            {"text": "Photosynthetic bacteria live on land and "
                     "chemosynthetic bacteria live only in the sea.",
             "correct": False,
             "why": "Photosynthetic bacteria are found in the sea as well "
                    "as on land. The difference is the source of energy "
                    "each one uses, not where it lives."},
            {"text": "Photosynthetic bacteria use light energy and "
                     "chemosynthetic bacteria use energy from chemical "
                     "reactions.",
             "correct": True},
            {"text": "Photosynthetic bacteria are producers and "
                     "chemosynthetic bacteria are decomposers instead.",
             "correct": False,
             "why": "Chemosynthetic bacteria also build their own organic "
                    "molecules from raw materials, which makes them "
                    "producers too, just powered a different way."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e25",
        "band": "easier",
        "text": "Earthworms feed on dead leaves and other decaying plant "
                "material in the soil. Does that make an earthworm a "
                "producer?",
        "options": [
            {"text": "Yes — anything that feeds only on plant material "
                     "rather than on another animal counts as a producer.",
             "correct": False,
             "why": "What a producer eats is not the test, because a "
                    "producer eats nothing at all. It is whether the "
                    "organism builds its own organic molecules."},
            {"text": "Yes — earthworms are essential for healthy soil, and a "
                     "producer is defined as an organism the ecosystem "
                     "cannot do without.",
             "correct": False,
             "why": "Being essential is not what the word producer means. A "
                    "producer is defined by building its own food, not by "
                    "how important it is."},
            {"text": "It depends on the leaf, since some leaves still "
                     "contain enough sugar to count as a food source the "
                     "earthworm builds itself.",
             "correct": False,
             "why": "Eating a store of sugar built by something else is "
                    "still feeding, whatever kind of leaf it came from. It "
                    "is never the same as building the sugar yourself."},
            {"text": "No — an earthworm feeds on material a plant already "
                     "built, rather than building any of its own.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e26",
        "band": "easier",
        "text": "Milk on its own is not cheese. Something feeds on the "
                "protein and fat in it and turns it into cheese. What is "
                "that something?",
        "options": [
            {"text": "Bacteria, which mature the milk as they feed on it.",
             "correct": True},
            {"text": "Sunlight, which changes the chemical structure of the "
                     "milk as it curdles.",
             "correct": False,
             "why": "Cheese making happens away from sunlight, in a dairy "
                    "or a cave. What matures the milk is a living organism "
                    "feeding on it, not light."},
            {"text": "The cow itself, continuing to add enzymes to the milk "
                     "after it has left the udder.",
             "correct": False,
             "why": "Once milk has left the cow it takes no further part in "
                    "the process. What acts on it afterwards is a separate "
                    "organism, bacteria, feeding on it."},
            {"text": "Yeast, in the same way that it turns dough into "
                     "bread.",
             "correct": False,
             "why": "Yeast ferments sugars in dough or in brewing; the "
                    "organism that matures a cheese is bacteria feeding on "
                    "its protein and fat."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e27",
        "band": "easier",
        "text": "A fungus has no mouth and no gut, yet it still gets "
                "nutrients out of a piece of dead wood. How does it "
                "actually feed?",
        "options": [
            {"text": "It absorbs whole pieces of wood through its cell "
                     "walls and breaks them down once they are inside.",
             "correct": False,
             "why": "The wood is broken down before it ever crosses the "
                    "fungus's cell walls, not afterwards inside a cell."},
            {"text": "It digests the wood on the outside first, then "
                     "absorbs the smaller molecules that are released.",
             "correct": True},
            {"text": "It waits for the wood to rot on its own, then simply "
                     "absorbs whatever water is left in it once the rotting "
                     "is complete.",
             "correct": False,
             "why": "The fungus itself is what does the rotting, releasing "
                    "digestive substances onto the wood rather than waiting "
                    "for it to decay unaided."},
            {"text": "It photosynthesises using whatever light reaches the "
                     "log, and needs the wood only for support.",
             "correct": False,
             "why": "Fungi have no chlorophyll and cannot photosynthesise. "
                    "Every nutrient a fungus gets comes from digesting "
                    "material something else built."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e28",
        "band": "easier",
        "text": "A mushroom grows on a log from a tree that died years ago, "
                "feeding on wood that was built by photosynthesis long "
                "before. What does that show about a food chain?",
        "options": [
            {"text": "That a chain breaks down completely once too much "
                     "time has passed between its links.",
             "correct": False,
             "why": "Nothing about the mushroom's chain breaks down with "
                    "time; the molecules stay usable however long ago they "
                    "were built."},
            {"text": "That decomposers are the only organisms whose chains "
                     "can stretch back over several years.",
             "correct": False,
             "why": "Any stored organic material can sit for a long time "
                    "before being eaten, not only the material decomposers "
                    "feed on."},
            {"text": "That the energy in a chain does not have to reach a "
                     "consumer immediately — it can be stored for a long "
                     "time first.",
             "correct": True},
            {"text": "That the mushroom must be photosynthesising slowly in "
                     "the dark to build up its own reserves over time, the "
                     "way a plant does in low light.",
             "correct": False,
             "why": "Fungi have no chlorophyll and cannot photosynthesise "
                    "in the dark or otherwise. The stored energy was built "
                    "by a plant, not by the fungus itself."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e29",
        "band": "easier",
        "text": "In the salmon chain, phytoplankton are eaten by "
                "zooplankton, which are eaten by small fish and shrimp-like "
                "animals, which the salmon then hunts. What comes "
                "immediately before 'small fish and shrimp-like animals' in "
                "that chain?",
        "options": [
            {"text": "A salmon fillet, since the chain always starts from "
                     "what is on the plate.",
             "correct": False,
             "why": "The salmon fillet is the very first link, at the "
                    "opposite end of the chain from the one asked about "
                    "here."},
            {"text": "Phytoplankton, since they are the producer at the "
                     "base of the whole chain.",
             "correct": False,
             "why": "Phytoplankton sit at the far end of the chain, two "
                    "links further back than the one asked about here."},
            {"text": "Sunlight falling on the top hundred metres of ocean, "
                     "since that is where the chain truly begins.",
             "correct": False,
             "why": "Sunlight is the energy source rather than a link in "
                    "the chain itself, and it sits even further back than "
                    "the producer."},
            {"text": "Zooplankton, the tiny drifting animals that the small "
                     "fish and shrimp-like animals feed on.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-e30",
        "band": "easier",
        "text": "A food chain is written grass to cow to human, with an arrow "
                "between each pair. What does each arrow mean?",
        "options": [
            {"text": "Is eaten by — the arrow always points the way the "
                     "energy travels.",
             "correct": True},
            {"text": "Lives alongside — the arrow joins organisms that share "
                     "the same habitat.",
             "correct": False,
             "why": "Sharing a habitat is not what a chain records. Each "
                    "arrow shows food, and the energy in it, moving from one "
                    "organism to the next."},
            {"text": "Eats — the arrow points from the feeder to whatever it "
                     "happens to be feeding on.",
             "correct": False,
             "why": "That is the arrow drawn backwards. It runs from the one "
                    "being eaten to the one doing the eating, the way the "
                    "energy goes."},
            {"text": "Turns into — the arrow shows one organism changing into "
                     "the next one along.",
             "correct": False,
             "why": "No organism turns into the next one. The arrow shows the "
                    "energy and the molecules passing along as one is eaten "
                    "by another."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-04-s14",
        "band": "standard",
        "text": "Photosynthesis lets energy enter food chains, and it also "
                "puts oxygen into the air. Losing either would be disastrous, "
                "but in different ways. Which is the more immediate threat to "
                "every existing food chain?",
        "options": [
            {"text": "Losing the energy route, because every organism above a "
                     "producer would run out of energy directly and "
                     "immediately.",
             "correct": True},
            {"text": "Losing the oxygen supply, because every animal would "
                     "suffocate within seconds without a fresh supply of "
                     "oxygen.",
             "correct": False,
             "why": "The atmosphere holds a vast reserve of oxygen built up "
                    "over billions of years; losing the supply would lower "
                    "that level only gradually, not within seconds."},
            {"text": "Neither is more immediate, since both are carried out "
                     "by the same organisms at exactly the same rate.",
             "correct": False,
             "why": "The two stop for the same reason, but their effects run "
                    "on different timescales — an energy shortage bites "
                    "straight away, while an oxygen shortage would take far "
                    "longer to be felt."},
            {"text": "Losing the oxygen supply, because oxygen is needed to "
                     "build the very cells that make up a producer.",
             "correct": False,
             "why": "Producers use carbon dioxide and water to build "
                    "glucose; the oxygen released is a waste product of "
                    "that process rather than something the producer needs "
                    "first."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s15",
        "band": "standard",
        "text": "A supermarket labels its lettuce 'carbon neutral', on the "
                "grounds that the plants took carbon dioxide out of the air "
                "while they were growing. What is missing from that "
                "reasoning?",
        "options": [
            {"text": "Nothing is missing — a growing crop takes carbon "
                     "dioxide out of the air, so any vegetable is carbon "
                     "neutral.",
             "correct": False,
             "why": "Taking carbon in is only half the story. What matters is "
                    "whether that carbon then stays out of the air, and here "
                    "it does not."},
            {"text": "The carbon returns to the air when the lettuce is eaten "
                     "and respired, and growing and moving it released more.",
             "correct": True},
            {"text": "Lettuce is almost entirely water, so it took no carbon "
                     "dioxide out of the air in the first place.",
             "correct": False,
             "why": "Lettuce is mostly water, but the dry matter in it is "
                    "still built from carbon that came out of the air. The "
                    "gap is what happens to that carbon afterwards."},
            {"text": "A growing plant releases carbon dioxide rather than "
                     "absorbing it, so the label has the direction backwards.",
             "correct": False,
             "why": "A plant in the light takes far more carbon dioxide in "
                    "than it gives out, so that part of the label is right. "
                    "What it leaves out is the carbon going back."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s16",
        "band": "standard",
        "text": "A dairy farmer feeds her herd silage through the winter "
                "instead of fresh grass from the field. Does switching to "
                "silage change where the energy in the winter's milk "
                "originally came from?",
        "options": [
            {"text": "Yes — silage is a manufactured product, so its energy "
                     "comes from the factory that produced it rather than "
                     "from a field.",
             "correct": False,
             "why": "Silage is made from the farm's own cut grass rather "
                    "than manufactured elsewhere. Its energy still comes "
                    "from that grass's photosynthesis."},
            {"text": "Yes — because the grass is stored for months, its "
                     "stored sugars are converted into a completely "
                     "different kind of energy while it waits.",
             "correct": False,
             "why": "Preserving grass changes it chemically only a little; "
                    "the energy in it still originated as sugar built by "
                    "photosynthesis months earlier."},
            {"text": "No — the silage is preserved grass, so the chain "
                     "still traces back to photosynthesis in that same "
                     "field earlier in the year.",
             "correct": True},
            {"text": "No — because a cow's rumen bacteria replace the "
                     "grass's energy with fresh energy of their own before "
                     "the cow's own tissues ever use any of it.",
             "correct": False,
             "why": "Rumen bacteria break the grass down; they do not add "
                    "fresh energy of their own. The energy the cow gets was "
                    "already captured by the grass's own photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s17",
        "band": "standard",
        "text": "One large field of grass feeds both a beef herd, for "
                "steak, and a dairy herd, for cheese. What do the steak "
                "chain and the cheese chain have in common?",
        "options": [
            {"text": "Nothing significant — one traces back to a beef herd "
                     "and the other to a dairy herd, which are different "
                     "animals entirely.",
             "correct": False,
             "why": "Which herd is involved does not change where the "
                    "underlying energy came from. Both herds are eating "
                    "grass grown by the same photosynthesis."},
            {"text": "Only that both involve a cow, since steak and cheese "
                     "are otherwise built from completely different "
                     "molecules.",
             "correct": False,
             "why": "Sharing the same animal is real, but the deeper point "
                    "is that both animals are drawing on energy captured by "
                    "exactly the same field's photosynthesis."},
            {"text": "They must have different origins, since one chain has "
                     "an extra bacterial step that the other does not.",
             "correct": False,
             "why": "An extra step changes how many organisms handle the "
                    "energy, not where that energy originally came from. "
                    "Both chains still end at the same field."},
            {"text": "Both trace back to the very same photosynthesis, in "
                     "the same field, just carried there by two different "
                     "animals.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s18",
        "band": "standard",
        "text": "An animal takes food into its body and digests it inside a "
                "gut. A fungus has no gut at all. How does its way of "
                "feeding compare?",
        "options": [
            {"text": "A fungus digests its food outside its own body "
                     "first, then absorbs the smaller molecules that are "
                     "released.",
             "correct": True},
            {"text": "A fungus digests its food inside its cells in exactly "
                     "the same way an animal's gut does, just on a smaller "
                     "scale.",
             "correct": False,
             "why": "A fungus has no internal gut at all. Digestion happens "
                    "outside the fungus, on the material it is feeding on, "
                    "before anything is absorbed."},
            {"text": "A fungus needs no digestion at all, since dead "
                     "material has already broken itself down by the time a "
                     "fungus reaches it.",
             "correct": False,
             "why": "The fungus itself is what breaks the material down, "
                    "releasing digestive substances onto it rather than "
                    "waiting for it to decay unaided."},
            {"text": "A fungus photosynthesises its own food rather than "
                     "digesting anything, which is why it needs no gut.",
             "correct": False,
             "why": "Fungi have no chlorophyll and cannot photosynthesise. "
                    "Every fungus depends on digesting material something "
                    "else already built."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s19",
        "band": "standard",
        "text": "A student says a food web is just several separate food "
                "chains added together, and shows nothing that a single "
                "chain does not already show. Evaluate that claim.",
        "options": [
            {"text": "The student is right — a web is only chains placed "
                     "side by side, with no new connections between them.",
             "correct": False,
             "why": "A web's whole point is the connections between chains, "
                    "such as one producer feeding several different "
                    "consumers. Placing chains side by side would not draw "
                    "those connections in."},
            {"text": "Mostly wrong — a web shows that one organism can "
                     "belong to several chains at once, so losing it "
                     "affects more than a single line of feeding.",
             "correct": True},
            {"text": "Completely wrong — a web replaces every producer in "
                     "the chains it is built from with a different kind of "
                     "organism.",
             "correct": False,
             "why": "A web is built from the very same producers and "
                    "consumers as its component chains; drawing the "
                    "connections between them does not change what kind of "
                    "organism starts each one."},
            {"text": "The student is right, because a web can always be "
                     "split back into the exact same chains it started from "
                     "with nothing lost.",
             "correct": False,
             "why": "Splitting a web back into separate chains loses the "
                    "shared connections between them, which is precisely "
                    "the extra information a web shows."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s20",
        "band": "standard",
        "text": "Deep-sea vent communities running on chemosynthesis were "
                "found in 1977. Why did that discovery matter to biologists "
                "at the time, beyond just describing one unusual "
                "ecosystem?",
        "options": [
            {"text": "It proved that sunlight is not needed for any "
                     "chemical reaction to happen anywhere on Earth.",
             "correct": False,
             "why": "Countless chemical reactions run without sunlight "
                    "already; the discovery was specifically about a living "
                    "system building its own food without it."},
            {"text": "It showed that tube worms are actually a kind of "
                     "plant, since they grow so close to the vents.",
             "correct": False,
             "why": "Tube worms are animals. The discovery was about the "
                    "bacteria at the base of the chain, not about "
                    "reclassifying the worms themselves."},
            {"text": "It overturned the assumption that sunlight was the "
                     "only way energy could enter a living system.",
             "correct": True},
            {"text": "It proved that photosynthesis had stopped working "
                     "properly in deep water, forcing organisms to adapt.",
             "correct": False,
             "why": "Photosynthesis cannot happen in deep water regardless "
                    "of vents, because no light reaches that depth. The "
                    "discovery was about an alternative energy source, not "
                    "a failure of photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s21",
        "band": "standard",
        "text": "Some scientists searching for life on a moon with a frozen "
                "ocean and no daylight take chemosynthesis seriously as a "
                "reason life might exist there. Why?",
        "options": [
            {"text": "Because chemosynthesis proves that sunlight can pass "
                     "through solid ice without being blocked.",
             "correct": False,
             "why": "Chemosynthesis has nothing to do with light passing "
                    "through ice; its whole point is an energy source that "
                    "does not depend on light reaching anywhere at all."},
            {"text": "Because a frozen ocean is assumed to contain the same "
                     "chlorophyll that plants and algae use on Earth.",
             "correct": False,
             "why": "Chlorophyll is what photosynthetic organisms use to "
                    "capture light, which by definition is not available in "
                    "a moon with no daylight."},
            {"text": "Because chemosynthetic bacteria need extreme cold to "
                     "build their sugars, which an icy moon would supply in "
                     "more than enough quantity to spare.",
             "correct": False,
             "why": "The vent communities chemosynthesis was found in are "
                    "hot, not cold. What matters for an icy moon is the "
                    "absence of light, not the temperature."},
            {"text": "Because chemosynthesis shows that a living system can "
                     "build its own food using chemical energy rather than "
                     "light.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s22",
        "band": "standard",
        "text": "A student argues that since zooplankton drift in the same "
                "sunlit water as phytoplankton, they must photosynthesise a "
                "little as well. Correct that.",
        "options": [
            {"text": "They do not — zooplankton are animals with no "
                     "chlorophyll, and they get their energy by eating "
                     "phytoplankton instead.",
             "correct": True},
            {"text": "They are partly right — zooplankton photosynthesise "
                     "weakly, on top of the food they also eat.",
             "correct": False,
             "why": "Zooplankton have no chlorophyll at all, so they cannot "
                    "photosynthesise even weakly. Every bit of their energy "
                    "comes from feeding."},
            {"text": "They are completely right, since anything living in "
                     "sunlit water is automatically capturing some of that "
                     "light for its own use, the same way a plant leaf "
                     "does.",
             "correct": False,
             "why": "Living in lit water is not enough on its own; "
                    "capturing light energy requires chlorophyll, which "
                    "zooplankton do not have."},
            {"text": "The student has it backwards — phytoplankton are the "
                     "ones that eat zooplankton, not the other way round.",
             "correct": False,
             "why": "Phytoplankton are producers that build their own food; "
                    "it is zooplankton that feed on phytoplankton, not the "
                    "reverse."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s23",
        "band": "standard",
        "text": "The ocean dissolving carbon dioxide and rock slowly "
                "weathering both remove carbon dioxide from the air, exactly "
                "as photosynthesis does. So why is photosynthesis described "
                "as 'the only large-scale biological process' that removes "
                "it, rather than simply 'the only process'?",
        "options": [
            {"text": "Because the ocean and rock weathering only remove "
                     "carbon dioxide in small, local amounts that barely "
                     "register.",
             "correct": False,
             "why": "The ocean removes carbon dioxide on a scale comparable "
                    "to the whole land biosphere, far from a small, local "
                    "amount."},
            {"text": "Because those two processes are chemical and "
                     "geological rather than carried out by a living "
                     "thing.",
             "correct": True},
            {"text": "Because the ocean and rock weathering both happen far "
                     "too slowly to be worth naming at all.",
             "correct": False,
             "why": "Rock weathering is genuinely slow, but the ocean "
                    "dissolves carbon dioxide continuously and on a large "
                    "scale; both are worth naming precisely because they "
                    "matter."},
            {"text": "Because 'the only process' would have been factually "
                     "correct, and the word biological was added purely for "
                     "style.",
             "correct": False,
             "why": "The word biological is doing real work — without it "
                    "the sentence would be false, since two genuine "
                    "non-biological removal routes exist."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s24",
        "band": "standard",
        "text": "Phytoplankton in the open ocean are microscopic and "
                "individually short-lived, yet they support whales weighing "
                "tens of tonnes. Explain how that is possible.",
        "options": [
            {"text": "Each phytoplankton cell stores far more energy than its "
                     "size suggests, enough on its own to feed a large "
                     "animal.",
             "correct": False,
             "why": "A microscopic cell holds a microscopic amount of energy. "
                    "What makes the supply large is the number of cells, not "
                    "the size of any one of them."},
            {"text": "A whale takes most of its energy from the seawater it "
                     "filters rather than from the organisms in it.",
             "correct": False,
             "why": "Seawater itself carries no food energy. Everything a "
                    "whale lives on was built by an organism, and traced back "
                    "far enough that means phytoplankton."},
            {"text": "There are enormous numbers of them and they reproduce "
                     "very fast, so the total food built each year is huge.",
             "correct": True},
            {"text": "Phytoplankton grow much larger in cold water, reaching "
                     "the size of a small fish near the poles.",
             "correct": False,
             "why": "Phytoplankton stay microscopic wherever they live. Cold "
                    "polar water supports huge numbers of them, which is a "
                    "different thing from large ones."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s25",
        "band": "standard",
        "text": "A salmon feed pellet is made from ground-up smaller fish "
                "and from crops such as rapeseed. Tracing both ingredients "
                "back, what two kinds of producer lie behind that one "
                "pellet?",
        "options": [
            {"text": "Two different kinds of algae, one marine and one "
                     "freshwater, since fish always eat algae directly.",
             "correct": False,
             "why": "The smaller fish in the pellet themselves eat other "
                    "organisms rather than only algae, and rapeseed is a "
                    "land crop rather than any kind of algae."},
            {"text": "A single producer, since both ingredients are "
                     "eventually ground into the same pellet and become one "
                     "thing.",
             "correct": False,
             "why": "Being mixed into one pellet does not merge their "
                    "origins. The crop and the fish meal each trace back "
                    "through separate chains to separate producers."},
            {"text": "Only phytoplankton, since every ingredient in a "
                     "fish-based pellet ultimately comes from the sea.",
             "correct": False,
             "why": "The rapeseed in the pellet is a land crop, grown in a "
                    "field rather than in the sea, so it traces back to a "
                    "land producer, not phytoplankton."},
            {"text": "Phytoplankton, behind the fish meal, and the rapeseed "
                     "plant itself, behind the crop.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s26",
        "band": "standard",
        "text": "Estimates of how much of the world's photosynthesis happens "
                "in the sea are usually given as 'roughly half' rather than "
                "as an exact figure such as 48.3%. Why is the rounder claim "
                "the more honest one?",
        "options": [
            {"text": "Because the true split varies between different "
                     "studies and with the season, so a single exact figure "
                     "would overstate how precisely it is known.",
             "correct": True},
            {"text": "Because scientists have never attempted to measure "
                     "how much photosynthesis happens in the sea at all.",
             "correct": False,
             "why": "The estimate has been measured by real studies; the "
                    "point is that those studies vary, not that no "
                    "measurement exists."},
            {"text": "Because an exact figure would be too difficult for a "
                     "student to remember, regardless of how accurate it "
                     "is.",
             "correct": False,
             "why": "Ease of remembering has nothing to do with why the "
                    "lesson hedges. The reason is that the true figure "
                    "genuinely shifts between studies and seasons."},
            {"text": "Because the sea's share of photosynthesis is "
                     "shrinking so quickly that any figure would be out of "
                     "date within a year.",
             "correct": False,
             "why": "There is no evidence of such a rapid decline. The hedge "
                    "is about measurement uncertainty between studies, not "
                    "about a changing trend."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s27",
        "band": "standard",
        "text": "If a mature rainforest is not, in fact, supplying the "
                "planet's oxygen, which job of photosynthesis still makes it "
                "worth protecting?",
        "options": [
            {"text": "Letting energy into food chains, since a forest is the "
                     "only place on Earth where energy enters a food chain, "
                     "unlike anywhere out at sea, which the claim leaves out "
                     "entirely.",
             "correct": False,
             "why": "Energy enters food chains at sea just as much as on "
                    "land, so that is not something only a forest provides."},
            {"text": "Taking carbon dioxide back out of the air, since "
                     "felling it releases the carbon its wood has locked "
                     "away, and leaving it standing keeps that carbon out of "
                     "the air.",
             "correct": True},
            {"text": "Putting oxygen into the air, since a mature forest "
                     "releases far more oxygen than it consumes, unlike any "
                     "other ecosystem.",
             "correct": False,
             "why": "A mature forest is close to balanced, consuming much "
                    "of what it produces, which is exactly why it is not a "
                    "net oxygen supply."},
            {"text": "None of them, since a forest's value has nothing to do "
                     "with what photosynthesis does for everything else.",
             "correct": False,
             "why": "A forest's carbon-locking value comes directly from "
                    "taking carbon dioxide out of the air and holding it in "
                    "growing wood."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s28",
        "band": "standard",
        "text": "A cow's own digestive system cannot break down the tough "
                "plant fibre in grass on its own. What do the bacteria "
                "living in its rumen do that lets the cow use the grass "
                "anyway?",
        "options": [
            {"text": "They photosynthesise a small extra supply of glucose "
                     "for the cow to use alongside the grass.",
             "correct": False,
             "why": "Bacteria in a rumen have no chlorophyll and no light "
                    "to use even if they did; they feed on the grass rather "
                    "than building anything of their own."},
            {"text": "They filter out the tough fibre completely, so that "
                     "only the digestible parts of the grass ever reach the "
                     "cow.",
             "correct": False,
             "why": "The bacteria are not a filter that removes material; "
                    "they actively break the tough fibre down chemically "
                    "into forms the cow's own body can use."},
            {"text": "They break down the tough plant fibre chemically, "
                     "releasing molecules the cow's own body is then able "
                     "to absorb and use.",
             "correct": True},
            {"text": "They replace the cow's own stomach lining, allowing "
                     "the cow to digest grass in the same way it would "
                     "digest meat, rather than doing a separate chemical job "
                     "alongside it.",
             "correct": False,
             "why": "Nothing about the bacteria replaces any part of the "
                    "cow's body. They live alongside the cow's own "
                    "digestive system, doing a chemical job it cannot do "
                    "alone."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s29",
        "band": "standard",
        "text": "A student suggests calling fungi 'recyclers' instead of "
                "'decomposers', arguing that it sounds less like they are "
                "eating something and more like they are helping. Evaluate "
                "that renaming.",
        "options": [
            {"text": "It is a real improvement, since a recycler and a "
                     "decomposer carry out completely different biological "
                     "processes.",
             "correct": False,
             "why": "Renaming does not change what is happening "
                    "biologically. Whatever the word used, the fungus is "
                    "still feeding on material something else built."},
            {"text": "It solves the problem, because 'recycler' correctly "
                     "describes an organism that builds its own organic "
                     "molecules, which is exactly what the old label got "
                     "wrong in the first place.",
             "correct": False,
             "why": "Building your own organic molecules is what a "
                    "producer does. A fungus feeding on dead material fits "
                    "neither the old label's problem nor the new one's "
                    "claim any differently."},
            {"text": "It changes what students believe fungi are doing, "
                     "since 'recycler' removes any suggestion that energy "
                     "passes through the chain at all.",
             "correct": False,
             "why": "Whichever word is used, the underlying biology stays "
                    "exactly the same — a fungus absorbs molecules "
                    "something else built, and that energy still passes "
                    "along the chain."},
            {"text": "It changes only the word, not the biology — a fungus "
                     "still gets its energy from material something else "
                     "built, whatever it is called.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-s30",
        "band": "standard",
        "text": "A student argues that because bread reaches a producer in "
                "fewer steps than cheese does, a bread field must always "
                "supply more total energy to people than a dairy farm of "
                "any size. What is wrong with that argument?",
        "options": [
            {"text": "Step count is about efficiency per step, not about "
                     "total amount — a large enough dairy farm could still "
                     "supply more energy overall than a tiny wheat field.",
             "correct": True},
            {"text": "Nothing is wrong with it, since fewer steps always "
                     "means more total energy reaches the final food, no "
                     "matter the size of the land involved or how the two "
                     "farms happen to compare.",
             "correct": False,
             "why": "Fewer steps means less is lost at each stage, but the "
                    "total amount produced still depends on how much land "
                    "and how much grass or wheat is grown, not on step "
                    "count alone."},
            {"text": "The argument is wrong because cheese and bread "
                     "actually reach a producer in exactly the same number "
                     "of steps.",
             "correct": False,
             "why": "Cheese's chain has one extra step, through the cow "
                    "and the bacteria that mature it, compared with bread's "
                    "more direct route to the wheat plant."},
            {"text": "The argument is wrong because dairy farms produce no "
                     "energy for people at all, only wheat fields do.",
             "correct": False,
             "why": "Cheese and milk both supply real energy to people; a "
                    "dairy farm's output is not zero, it is simply passed "
                    "through more steps than bread's is."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-04-h14",
        "band": "harder",
        "text": "Suppose jobs one and three both stopped completely — no "
                "new energy entering food chains, and no more carbon "
                "dioxide being taken back out of the air. Which outcome "
                "best describes what would follow over the following "
                "centuries?",
        "options": [
            {"text": "Existing food chains would empty as their stored "
                     "energy ran out, while carbon dioxide in the "
                     "atmosphere climbed without anything pulling it back "
                     "down.",
             "correct": True},
            {"text": "Food chains would carry on exactly as before, since "
                     "animals do not depend on new energy entering once a "
                     "chain already exists.",
             "correct": False,
             "why": "Every organism above a producer is spending energy "
                    "that has to keep being replaced; without new energy "
                    "entering, stored supplies would run out and the chains "
                    "above the producers would collapse."},
            {"text": "Carbon dioxide levels would fall, since burning and "
                     "decay would also stop once photosynthesis stopped.",
             "correct": False,
             "why": "Burning and decay do not depend on photosynthesis "
                    "continuing; they would keep adding carbon dioxide with "
                    "nothing left to remove it."},
            {"text": "Nothing serious would happen for many centuries, "
                     "since the atmosphere itself holds enough stored energy "
                     "to support every food chain on Earth indefinitely, "
                     "however jobs one and three behave.",
             "correct": False,
             "why": "The atmosphere itself stores no food energy at all; "
                    "every joule reaching a food chain has to come from an "
                    "organism capturing it fresh."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h15",
        "band": "harder",
        "text": "A campaigner claims that if humans stopped burning fossil "
                "fuels tomorrow, atmospheric carbon dioxide would fall back "
                "to pre-industrial levels within about a decade, because "
                "photosynthesis and the ocean would simply mop it up. What "
                "is the strongest objection to that timescale?",
        "options": [
            {"text": "There is no objection — photosynthesis and the ocean "
                     "genuinely do remove carbon dioxide fast enough to "
                     "clear a century of emissions within ten years.",
             "correct": False,
             "why": "Those removal processes run over decades to millions "
                    "of years depending on the route; none of them clears "
                    "an accumulated surplus that quickly."},
            {"text": "The removal routes run on very different timescales "
                     "from the emissions did, so clearing what has built up "
                     "would take far longer than a decade.",
             "correct": True},
            {"text": "The objection is that photosynthesis and the ocean "
                     "have stopped removing carbon dioxide altogether since "
                     "industrial emissions began.",
             "correct": False,
             "why": "Both routes are still actively removing carbon "
                    "dioxide; the issue is that they cannot keep pace with "
                    "how quickly it has been added, not that they have "
                    "stopped working."},
            {"text": "The objection is that stopping fossil fuel burning "
                     "would itself release even more carbon dioxide than "
                     "continuing to burn it.",
             "correct": False,
             "why": "Burning fossil fuels is what releases the carbon "
                    "dioxide in the first place; stopping it prevents "
                    "further emissions rather than causing extra ones."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h16",
        "band": "harder",
        "text": "A headline reads: 'Chemosynthetic bacteria near a deep-sea "
                "vent prove that life anywhere in the universe can exist "
                "without photosynthesis.' What is the overreach in that "
                "claim?",
        "options": [
            {"text": "The claim is not an overreach — one confirmed "
                     "exception is enough to rule photosynthesis out as "
                     "necessary anywhere.",
             "correct": False,
             "why": "Showing that life can survive on Earth without "
                    "photosynthesis in one setting does not establish what "
                    "is possible on a completely different world with "
                    "different chemistry and conditions."},
            {"text": "The claim understates the finding — vent bacteria "
                     "suggest that photosynthesis has failed to evolve "
                     "successfully on this planet, and every living thing "
                     "here depends on chemosynthesis instead.",
             "correct": False,
             "why": "Photosynthesis clearly did evolve on Earth and "
                    "supplies almost every other food chain on the planet; "
                    "the vent bacteria are the rare exception, not evidence "
                    "that it never happened."},
            {"text": "It generalises from one Earth ecosystem to every "
                     "possible world, when the finding only shows one "
                     "alternative energy route is possible here.",
             "correct": True},
            {"text": "There is no overreach, because chemosynthesis and "
                     "photosynthesis are actually the same process under a "
                     "different name.",
             "correct": False,
             "why": "The two use different energy sources entirely — light "
                    "for one, chemical reactions for the other — and are "
                    "genuinely different processes."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h17",
        "band": "harder",
        "text": "A dairy herd needs about 8 kg of grass-equivalent silage "
                "to produce 1 kg of milk, and about 12 kg of milk to make "
                "1 kg of hard cheese. Roughly how much silage did a field "
                "need to grow to supply a herd producing 500 kg of cheese "
                "in a season?",
        "options": [
            {"text": "About 6 000 kg, from multiplying 500 kg of cheese by "
                     "12 kg of milk per kilogram of cheese only.",
             "correct": False,
             "why": "This stops after converting cheese to milk and never "
                    "converts that milk back to the silage that produced "
                    "it, missing the second step of the chain."},
            {"text": "About 4 000 kg, from multiplying 500 kg of cheese "
                     "directly by the 8 kg silage-to-milk figure.",
             "correct": False,
             "why": "8 kg of silage makes a kilogram of milk, not a "
                    "kilogram of cheese; the milk-to-cheese step has to be "
                    "included as well."},
            {"text": "About 62.5 kg, from dividing 500 kg of cheese by the "
                     "two ratios rather than multiplying by them.",
             "correct": False,
             "why": "Both figures given are amounts of input needed per "
                    "kilogram of output, so they have to be multiplied "
                    "through the chain, not divided."},
            {"text": "About 48 000 kg, from converting cheese to milk and "
                     "then milk to silage in two steps.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h18",
        "band": "harder",
        "text": "A student's ecosystem diagram draws an arrow from 'soil' "
                "to 'trees', labelled 'energy', to show what decomposers "
                "return to the forest. Evaluate whether that label is "
                "accurate.",
        "options": [
            {"text": "It is wrong — decomposers return minerals to the "
                     "soil, and minerals carry no energy, so the arrow "
                     "should not be labelled energy.",
             "correct": True},
            {"text": "It is accurate, since the whole reason decomposers "
                     "matter is that they recharge the soil with the energy "
                     "plants need to grow.",
             "correct": False,
             "why": "What decomposers return to the soil is minerals, "
                    "which trees take up as raw materials; the energy a "
                    "tree runs on comes from its own photosynthesis, not "
                    "from the soil."},
            {"text": "It is accurate, but only because decomposers are "
                     "themselves a kind of producer that generates new "
                     "energy as they feed.",
             "correct": False,
             "why": "A decomposer builds no organic molecules of its own; "
                    "it feeds on what a producer already built, which makes "
                    "it the opposite of a producer."},
            {"text": "It is wrong, but only because the arrow is pointing "
                     "in the wrong direction — it should run from the trees "
                     "to the soil instead.",
             "correct": False,
             "why": "Reversing the arrow's direction would not fix the "
                    "real problem, which is that minerals rather than "
                    "energy are what actually pass from soil to a growing "
                    "tree."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h19",
        "band": "harder",
        "text": "One hectare of wheat yields 8000 kg of grain, eaten "
                "directly as bread. A second hectare of pasture, converted "
                "through cattle at the usual ten-kilograms-of-grass-per-"
                "kilogram-of-cow ratio, yields about 900 kg of beef. "
                "Roughly how many times more food, by mass, does the wheat "
                "hectare deliver directly to people?",
        "options": [
            {"text": "About twice as much, since converting through an "
                     "animal always halves the usable yield exactly.",
             "correct": False,
             "why": "The ten-to-one conversion loses far more than half; "
                    "the actual ratio between the two hectares here works "
                    "out much larger than two."},
            {"text": "Roughly nine times as much, from dividing the wheat "
                     "yield by the beef yield.",
             "correct": True},
            {"text": "About the same amount, since both hectares started "
                     "with the same field's worth of sunlight falling on "
                     "them.",
             "correct": False,
             "why": "Starting with the same sunlight does not guarantee "
                    "the same food yield once one hectare's energy passes "
                    "through an extra animal, losing most of it to "
                    "respiration along the way."},
            {"text": "Roughly ninety times as much, since the ten-to-one "
                     "ratio should be applied twice over for a fair "
                     "comparison.",
             "correct": False,
             "why": "The ten-to-one ratio has already been used once to "
                    "reach the 900 kg beef figure; applying it a second "
                    "time double-counts the conversion loss."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h20",
        "band": "harder",
        "text": "A textbook says vent bacteria are not 'life as we know it' "
                "because they do not depend on sunlight. Evaluate that "
                "description, using what the bacteria are actually made "
                "of.",
        "options": [
            {"text": "The description is fair, since an organism that gets "
                     "its energy differently must also be built from "
                     "entirely different chemistry.",
             "correct": False,
             "why": "Nothing about a different energy source implies "
                    "different underlying chemistry; the vent bacteria are "
                    "still built from cells, proteins and DNA exactly as "
                    "sunlight-powered organisms are."},
            {"text": "The description is fair, because 'life as we know "
                     "it' is defined specifically by an organism's ability "
                     "to use sunlight.",
             "correct": False,
             "why": "'Life as we know it' generally refers to the shared "
                    "biochemistry of cells, proteins and DNA, not to which "
                    "particular energy source an organism happens to use."},
            {"text": "The description is misleading, since the bacteria "
                     "are built from the same cells, proteins and DNA as "
                     "every other organism — only their energy source "
                     "differs.",
             "correct": True},
            {"text": "The description is misleading, but only because the "
                     "bacteria are technically plants rather than "
                     "bacteria.",
             "correct": False,
             "why": "They are genuinely bacteria, not plants, and "
                    "reclassifying them would not be what makes the "
                    "original description misleading."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h21",
        "band": "harder",
        "text": "The slow weathering of rock removes roughly 0.3 billion "
                "tonnes of carbon from the atmosphere each year worldwide; "
                "gross photosynthesis removes roughly 120 billion tonnes of "
                "carbon each year, before respiration returns most of it. "
                "Roughly how many times faster is photosynthesis's gross "
                "removal than weathering's?",
        "options": [
            {"text": "About 4 times faster, from rounding both figures to "
                     "the nearest whole number first.",
             "correct": False,
             "why": "Rounding both figures first throws away the "
                    "information the calculation needs; dividing the real "
                    "figures gives a much larger ratio than 4."},
            {"text": "About 40 times faster, from dividing 120 by 3 rather "
                     "than by 0.3.",
             "correct": False,
             "why": "The weathering figure is 0.3 billion tonnes, not 3; "
                    "using the wrong figure understates the true ratio by a "
                    "factor of ten."},
            {"text": "About 120 times faster, treating the weathering "
                     "figure as if it were 1 billion tonnes.",
             "correct": False,
             "why": "The weathering figure given is 0.3 billion tonnes, "
                    "not 1; substituting a rounder number changes the "
                    "answer."},
            {"text": "About 400 times faster, from dividing 120 by 0.3.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h22",
        "band": "harder",
        "text": "The build-up of oxygen was poisonous to almost everything "
                "alive at the time. A student concludes from this that "
                "photosynthesis 'cannot be called beneficial overall'. "
                "Evaluate that conclusion.",
        "options": [
            {"text": "It does not follow — the same build-up also made "
                     "possible every oxygen-breathing organism alive today, "
                     "you included.",
             "correct": True},
            {"text": "The conclusion is correct, since an event that was "
                     "harmful to any organism at the time can never be "
                     "called beneficial afterwards.",
             "correct": False,
             "why": "An event's long-term consequences are not fixed by "
                    "its immediate effects; the same oxygen build-up that "
                    "harmed early life also enabled the evolution of "
                    "everything that breathes today."},
            {"text": "The conclusion is correct, but only because "
                     "photosynthesis has since stopped producing oxygen as "
                     "a waste product.",
             "correct": False,
             "why": "Photosynthesis still releases oxygen as a waste "
                    "product in exactly the same way; nothing about the "
                    "process itself has changed since then."},
            {"text": "The conclusion does not follow, but only because the "
                     "poisoning never actually happened and is an "
                     "exaggeration.",
             "correct": False,
             "why": "The harm to anaerobic life at the time is well "
                    "supported; the flaw in the student's reasoning is the "
                    "leap to 'not beneficial overall', not a doubt about "
                    "whether the event occurred."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h23",
        "band": "harder",
        "text": "A campaign poster reads: 'Without bees, there would be no "
                "food at all.' Evaluate that claim using what you know about "
                "how bread and salmon are produced.",
        "options": [
            {"text": "The claim is entirely fair, since bread and salmon "
                     "both depend on bees pollinating the plants somewhere "
                     "in their chain.",
             "correct": False,
             "why": "Wheat is pollinated by the wind rather than by bees, "
                    "and salmon's chain runs through phytoplankton and "
                    "zooplankton in the sea, with no bee involved at all."},
            {"text": "The claim overreaches — wheat is wind-pollinated and "
                     "salmon's chain runs entirely through the sea, so "
                     "neither depends on bees at all.",
             "correct": True},
            {"text": "The claim understates the case, since bees are also "
                     "needed to pollinate the phytoplankton that a salmon's "
                     "whole chain in the sea ultimately depends on.",
             "correct": False,
             "why": "Phytoplankton are microscopic algae that reproduce "
                    "without any pollination at all, by anything, bees "
                    "included."},
            {"text": "The claim is fair for bread but not for salmon, "
                     "since wheat needs bees to be pollinated before it can "
                     "produce grain.",
             "correct": False,
             "why": "Wheat is pollinated by the wind rather than by bees, "
                    "so bread does not depend on bees either."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h24",
        "band": "harder",
        "text": "The ocean dissolving carbon dioxide and photosynthesis "
                "locking carbon into wood are both described as 'removing' "
                "carbon dioxide from the air. Explain the important "
                "difference between what happens to the carbon afterwards "
                "in each case.",
        "options": [
            {"text": "There is no real difference — once carbon leaves the "
                     "atmosphere by either route it can never return to "
                     "the air again.",
             "correct": False,
             "why": "Dissolved carbon dioxide can outgas back into the "
                    "atmosphere from the ocean, and wood can decay or burn "
                    "and release its carbon again too; neither route is "
                    "guaranteed to be permanent."},
            {"text": "Dissolved carbon dioxide is permanently locked away, "
                     "while carbon in wood is released again the moment a "
                     "tree drops a single leaf.",
             "correct": False,
             "why": "Dissolved carbon dioxide can exchange back out of the "
                    "ocean into the air, and a tree's trunk holds most of "
                    "its locked carbon for as long as the tree stands, not "
                    "just until one leaf falls."},
            {"text": "Carbon locked in wood is held in a solid structure "
                     "that only releases it again through decay or "
                     "burning, while dissolved carbon dioxide can also "
                     "exchange back out of the ocean into the air.",
             "correct": True},
            {"text": "Both are chemically identical outcomes, since carbon "
                     "dioxide dissolved in water and carbon dioxide locked "
                     "in wood are the same molecule either way.",
             "correct": False,
             "why": "While the carbon atom itself is the same, dissolved "
                    "carbon dioxide stays as a gas in solution able to "
                    "exchange with the air, whereas carbon in wood is bound "
                    "into a solid structure that behaves very differently."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h25",
        "band": "harder",
        "text": "A colony of chemosynthetic bacteria at a vent builds 40 "
                "units of sugar an hour. A tube worm living on them "
                "respires away 85% of what it obtains from the bacteria "
                "just to survive the heat and pressure. Roughly how many "
                "units per hour end up as new worm tissue, if tissue growth "
                "is what's left after respiration?",
        "options": [
            {"text": "34 units, from taking 85% of the 40 units as what "
                     "remains.",
             "correct": False,
             "why": "85% is the fraction respired away, not the fraction "
                    "remaining; taking 85% of the total as the leftover has "
                    "the calculation backwards."},
            {"text": "40 units, since none of the sugar built by the "
                     "bacteria is ever lost between the bacteria and the "
                     "worm.",
             "correct": False,
             "why": "The worm respires away 85% of what it obtains just to "
                    "survive, so it cannot be passing on the whole 40 units "
                    "unchanged."},
            {"text": "8.5 units, from moving the decimal point of 85% "
                     "directly onto the 40 units instead of working out a "
                     "true percentage of it.",
             "correct": False,
             "why": "This treats 85% as if it meant 8.5, which is not what "
                    "the percentage states; 85% respired leaves 15% for "
                    "growth, not a tenth as much."},
            {"text": "6 units, from taking the 15% of the 40 units that is "
                     "left once respiration has used the rest.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h26",
        "band": "harder",
        "text": "A mature forest is close to oxygen-neutral, releasing "
                "about as much oxygen as it consumes. A student concludes "
                "that felling it therefore has no effect on atmospheric "
                "oxygen at all, only on carbon dioxide. What is wrong with "
                "that conclusion?",
        "options": [
            {"text": "Being balanced while standing says nothing about "
                     "what happens when it is felled — burning the timber "
                     "consumes oxygen in one large, one-off event.",
             "correct": True},
            {"text": "Nothing is wrong with it, since a forest that "
                     "consumes what it produces cannot possibly affect the "
                     "atmosphere either way, standing or felled.",
             "correct": False,
             "why": "The balance holds while a forest is standing and "
                    "growing; burning its timber afterwards is a separate, "
                    "one-off event that consumes oxygen rather than "
                    "continuing the balance."},
            {"text": "The conclusion is wrong because a mature forest is "
                     "not actually oxygen-neutral at all, and produces a "
                     "large surplus every year.",
             "correct": False,
             "why": "The near-balance of a mature forest is the correct "
                    "description; the flaw in the student's reasoning is "
                    "elsewhere, in ignoring what felling itself does."},
            {"text": "The conclusion is wrong because felling a forest "
                     "instantly converts every tree in it into carbon "
                     "dioxide with no oxygen involved at all.",
             "correct": False,
             "why": "Burning released wood genuinely uses oxygen as well "
                    "as releasing carbon dioxide; the felling event is not "
                    "oxygen-free."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h27",
        "band": "harder",
        "text": "As global temperatures rise, the weathering of rock — rock "
                "reacting with rainwater to remove carbon dioxide — actually "
                "speeds up rather than slows down, acting as a natural brake "
                "on warming over very long timescales. A student concludes "
                "this makes weathering fast enough to cancel out carbon "
                "dioxide from burning fossil fuels within a human lifetime. "
                "What is the flaw?",
        "options": [
            {"text": "There is no flaw — a faster weathering rate at "
                     "higher temperatures is exactly fast enough to offset "
                     "several decades of emissions within a single human "
                     "lifetime.",
             "correct": False,
             "why": "Even a sped-up weathering rate operates over hundreds "
                    "of thousands to millions of years, nowhere close to "
                    "matching emissions released over a human lifetime."},
            {"text": "The brake genuinely exists, but it acts over "
                     "hundreds of thousands to millions of years — far too "
                     "slowly to offset emissions happening over decades.",
             "correct": True},
            {"text": "The flaw is that the weathering of rock actually slows "
                     "down as temperatures rise, the opposite of what the "
                     "student assumes.",
             "correct": False,
             "why": "The given fact is that weathering speeds up with "
                    "warming, which is correct; the student's error is "
                    "about the timescale, not the direction of the "
                    "effect."},
            {"text": "The flaw is that the weathering of rock has nothing to "
                     "do with carbon dioxide, and only affects the rocks it "
                     "reacts with.",
             "correct": False,
             "why": "Carbon dioxide dissolved in rainwater is precisely what "
                    "this weathering removes from the air as it reacts with "
                    "rock."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h28",
        "band": "harder",
        "text": "A student argues that because the ocean's dissolving of "
                "carbon dioxide is non-biological, it must be permanent, "
                "unlike wood which eventually decays and releases its "
                "carbon again. Evaluate that argument.",
        "options": [
            {"text": "It is correct — anything non-biological is fixed in "
                     "place forever, while anything biological is always "
                     "temporary.",
             "correct": False,
             "why": "Being non-biological does not make a process "
                    "permanent; dissolved carbon dioxide is simply a gas in "
                    "solution, free to move back out of the water under the "
                    "right conditions."},
            {"text": "It is correct, because wood is the only material "
                     "anywhere that ever releases carbon back into the "
                     "air.",
             "correct": False,
             "why": "The ocean can also return dissolved carbon dioxide to "
                    "the atmosphere, so wood is not the only route by which "
                    "stored carbon gets released again."},
            {"text": "It is wrong — dissolved carbon dioxide can also "
                     "exchange back out of the ocean into the air, so "
                     "'non-biological' does not automatically mean "
                     "permanent.",
             "correct": True},
            {"text": "It is wrong, but only because wood itself never "
                     "actually decays or burns once it has locked its "
                     "carbon away.",
             "correct": False,
             "why": "Wood absolutely can decay or burn, releasing its "
                    "locked carbon again; that is precisely the timescale "
                    "difference the rest of the lesson relies on."},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h29",
        "band": "harder",
        "text": "A bee starts with 120 g of nectar that is 20% sugar by "
                "mass — so 24 g of sugar and 96 g of water. It evaporates "
                "water off the nectar, without adding or removing any "
                "sugar, until the mixture is 80% sugar by mass, which is "
                "honey. Roughly what mass of honey does that 24 g of sugar "
                "end up in?",
        "options": [
            {"text": "96 g, since the honey should weigh the same as the "
                     "water that was originally there.",
             "correct": False,
             "why": "The water is what gets evaporated away; the final "
                    "mass depends on the sugar staying at 80% of a smaller "
                    "total, not on matching the original water mass."},
            {"text": "120 g, since evaporating water off a nectar sample "
                     "does not change its total mass, however long the bee "
                     "spends fanning it dry.",
             "correct": False,
             "why": "Evaporating water removes mass from the mixture; the "
                    "honey left behind weighs less than the nectar the bee "
                    "started with."},
            {"text": "19.2 g, from taking 80% of the original 24 g of sugar "
                     "as the final mass.",
             "correct": False,
             "why": "The sugar itself is never reduced, since the bee adds "
                    "no sugar and removes none; 80% is the sugar's share of "
                    "the final honey, not a fraction taken off the sugar "
                    "itself."},
            {"text": "About 30 g, since 24 g of unchanged sugar making up "
                     "80% of the final mass means the final mass is 24 "
                     "divided by 0.8.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-04-h30",
        "band": "harder",
        "text": "A fallen tree holds 500 kg of carbon, built up over 60 "
                "years of growth. Fungi and bacteria decompose it "
                "completely over the following 15 years, releasing that "
                "carbon back into the air at a roughly steady rate. "
                "Roughly what mass of carbon does the decomposition "
                "release per year?",
        "options": [
            {"text": "About 33 kg a year, from dividing the 500 kg by the "
                     "15 years it takes to decompose.",
             "correct": True},
            {"text": "About 8 kg a year, from dividing the 500 kg by the "
                     "60 years the tree spent growing instead of the years "
                     "it takes to decompose.",
             "correct": False,
             "why": "The growing period tells you how long the carbon "
                    "took to build up, not how quickly it is released again "
                    "once decomposition begins."},
            {"text": "500 kg a year, since all of a fallen tree's carbon "
                     "is released within the very first year of decay.",
             "correct": False,
             "why": "The question states the decomposition happens over "
                    "15 years at a roughly steady rate, not all in the "
                    "first year."},
            {"text": "About 133 kg a year, from dividing the 500 kg by the "
                     "difference between the two time periods given.",
             "correct": False,
             "why": "Subtracting the two time periods produces a number "
                    "with no meaning here; the rate is the total carbon "
                    "divided by the time decomposition actually takes, 15 "
                    "years."},
        ],
        "figure": None,
    },
]
