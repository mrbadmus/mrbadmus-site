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
]
