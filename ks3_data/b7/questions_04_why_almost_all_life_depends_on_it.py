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
]
