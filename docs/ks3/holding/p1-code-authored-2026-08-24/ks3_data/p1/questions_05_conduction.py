"""P1 lesson 05 — Conduction: twelve questions.

These probe the mechanism rather than the vocabulary: what actually moves
along a rod, why a metal beats a non-metal, and what your hand is really
reporting when it says a handrail is cold. The distractors are built from
ENER-13 — metal is colder than wood because it feels colder — and from the
two habits the relay is aimed at: believing the hot particles travel, and
believing that conduction is just a property a material has with no mechanism
behind it.

No figures. Three of each answer index.
"""

UNIT = "P1"
LESSON = "conduction"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-05-e01",
        "band": "easier",
        "text": "Which of these is the best conductor?",
        "options": [
            {"text": "Wood",
             "correct": False,
             "why": "Wood is full of tiny pockets of trapped air, and air is "
                    "about the worst there is."},
            {"text": "Copper",
             "correct": True},
            {"text": "Glass",
             "correct": False,
             "why": "Glass is a solid whose particles touch, so it conducts a "
                    "little — and it has no free electrons, so only a little."},
            {"text": "Plastic",
             "correct": False,
             "why": "Plastic is used for kettle handles for exactly the "
                    "opposite reason."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e02",
        "band": "easier",
        "text": "In conduction through a solid, what travels along?",
        "options": [
            {"text": "The hot particles, from one end to the other",
             "correct": False,
             "why": "In a solid the particles are locked to their neighbours. "
                    "They vibrate harder about the same place."},
            {"text": "Heat, which is a fluid that flows through the material",
             "correct": False,
             "why": "There is no such fluid. That idea was called caloric and "
                    "careful weighing killed it two hundred years ago."},
            {"text": "The vibration, handed from particle to particle",
             "correct": True},
            {"text": "Nothing — the whole rod warms at the same instant",
             "correct": False,
             "why": "The far end of a spoon gets hot long after the near end "
                    "does, which is what the wax blobs show."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e03",
        "band": "easier",
        "text": "Why is a saucepan handle usually made of wood or plastic?",
        "options": [
            {"text": "Because those materials are lighter than metal",
             "correct": False,
             "why": "Weight is a small convenience. Something much more "
                    "important is being avoided."},
            {"text": "Because they do not rust in a hot kitchen",
             "correct": False,
             "why": "Stainless steel does not rust either, and it still makes "
                    "a poor handle."},
            {"text": "Because they are cheaper than the metal of the pan",
             "correct": False,
             "why": "Cheaper, yes — and a cheap handle you cannot hold is "
                    "worth nothing."},
            {"text": "Because they carry the transfer to your hand very "
                     "slowly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e04",
        "band": "easier",
        "text": "What is a free electron?",
        "options": [
            {"text": "An electron in a metal that can move right through it",
             "correct": True},
            {"text": "An electron that has escaped from the metal into the "
                     "air",
             "correct": False,
             "why": "It stays inside the metal. Free means free to move "
                    "within it, not free to leave."},
            {"text": "An electron with no charge, so nothing holds it in "
                     "place",
             "correct": False,
             "why": "Every electron has a charge. What is different is how "
                    "tightly it is held."},
            {"text": "An extra electron a metal gains when it is heated up",
             "correct": False,
             "why": "The free electrons are there at any temperature, which "
                    "is why metals conduct electricity when cold as well."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-05-s01",
        "band": "standard",
        "text": "A metal rod and a glass rod are the same size and both are "
                "solids whose particles touch. Why does the metal win by so "
                "much?",
        "options": [
            {"text": "The metal's particles are closer together",
             "correct": False,
             "why": "Glass is dense too, and packing alone does not produce a "
                    "difference of this size."},
            {"text": "The metal is heavier, so it holds more energy",
             "correct": False,
             "why": "How much a material holds is not the same as how fast it "
                    "passes a transfer on."},
            {"text": "The metal has free electrons and the glass does not",
             "correct": True},
            {"text": "The metal's particles vibrate faster at the same "
                     "temperature",
             "correct": False,
             "why": "Temperature IS how hard the particles are moving, so at "
                    "the same temperature they are comparable."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s02",
        "band": "standard",
        "text": "A metal handrail and a wooden bench sit outside on the same "
                "cold morning. Which is true?",
        "options": [
            {"text": "The metal is colder, which is why it feels colder",
             "correct": False,
             "why": "Put a thermometer on each. Everything left in the same "
                    "place long enough reaches the same temperature."},
            {"text": "The wood is warmer because it holds yesterday's "
                     "sunlight",
             "correct": False,
             "why": "Overnight is more than long enough for both to settle at "
                    "the air temperature."},
            {"text": "The metal is at a lower temperature only at the spot "
                     "your hand is touching",
             "correct": False,
             "why": "The metal at that spot actually WARMS while you hold it, "
                    "because your hand is the hotter of the two. It never "
                    "drops below the rest of the rail."},
            {"text": "They are the same temperature and your hand is "
                     "reporting a rate, not a temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s03",
        "band": "standard",
        "text": "In a wax-blob rod test, which of these must be kept the "
                "same for the comparison to be fair?",
        "options": [
            {"text": "The material each rod is made of",
             "correct": False,
             "why": "That is the one thing you are deliberately changing. "
                    "Keeping it the same would test nothing."},
            {"text": "The number of blobs that fall off each rod",
             "correct": False,
             "why": "That is the result. Fixing a result in advance is not "
                    "an experiment."},
            {"text": "The length and thickness of the rods, and the heat "
                     "source",
             "correct": True},
            {"text": "The time each rod is heated for, and nothing else "
                     "matters",
             "correct": False,
             "why": "Time matters and it is not the only thing. A thicker rod "
                    "would beat a thin one of the same material."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s04",
        "band": "standard",
        "text": "On the bench, copper dropped all four blobs and wood dropped "
                "none in sixty seconds. What does the wood result tell you?",
        "options": [
            {"text": "That wood does not conduct at all",
             "correct": False,
             "why": "It conducts, extremely slowly. Give it long enough and "
                    "the far end does warm up."},
            {"text": "That the wood rod was not heated properly",
             "correct": False,
             "why": "The same flame for the same time was used on all five. "
                    "That is what makes the test fair."},
            {"text": "That the wax on the wood rod was a different kind",
             "correct": False,
             "why": "Same wax, same size of blob. If it were not, the whole "
                    "test would be worthless."},
            {"text": "That the vibration had not reached even the first blob "
                     "in a minute",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-05-h01",
        "band": "harder",
        "text": "Diamond conducts better than copper and has no free "
                "electrons at all. What does that show about the two routes?",
        "options": [
            {"text": "That the particle-to-particle route can be very fast if "
                     "the lattice is stiff enough",
             "correct": True},
            # ⚠️ MRB-177 — written out to the correct option's length rather
            # than the correct option being cut.
            {"text": "That diamond must secretly have free electrons after "
                     "all, like a metal",
             "correct": False,
             "why": "It has none — which is exactly why diamond is an "
                    "electrical insulator and copper is not."},
            {"text": "That free electrons are not really what makes copper "
                     "such a good conductor",
             "correct": False,
             "why": "They are. Copper without them would be far worse. "
                    "Diamond has found another way to the same place."},
            {"text": "That being very hard is what makes a material conduct "
                     "well",
             "correct": False,
             "why": "Hardness is about resisting scratches. What matters here "
                    "is how stiffly and regularly the atoms are joined."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h02",
        "band": "harder",
        "text": "Why does putting a metal spoon in a cup of hot soup make the "
                "soup cool faster?",
        "options": [
            {"text": "Because the spoon is colder than the soup and stays "
                     "that way",
             "correct": False,
             "why": "The spoon warms up in seconds. Something has to keep "
                    "carrying the transfer away after that."},
            {"text": "Because metal conducts the transfer up out of the soup "
                     "and into the room",
             "correct": True},
            {"text": "Because the spoon stirs the soup and mixes the hot and "
                     "cool parts",
             "correct": False,
             "why": "A spoon left standing still does it too, which rules "
                    "stirring out."},
            {"text": "Because metal absorbs energy and stores it permanently",
             "correct": False,
             "why": "Nothing is stored permanently. The spoon reaches the "
                    "soup's temperature and then just keeps passing energy "
                    "on to the air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h03",
        "band": "harder",
        "text": "Two blocks are at the same temperature. One is copper and "
                "one is wood. Which holds more energy?",
        "options": [
            {"text": "The copper, because metals conduct better",
             "correct": False,
             "why": "Conducting well is about passing a transfer on, not "
                    "about how much is held."},
            {"text": "The wood, because it is a better insulator",
             "correct": False,
             "why": "Insulating well is also about the rate. Neither property "
                    "answers the question asked."},
            {"text": "It cannot be told from their temperatures alone",
             "correct": True},
            {"text": "Neither — the same temperature means the same amount",
             "correct": False,
             "why": "A bath and a teaspoon at 40 °C hold very different "
                    "amounts. Temperature alone never settles it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h04",
        "band": "harder",
        "text": "A student concludes from the rod test that \"metals are hot "
                "and non-metals are cold\". What has gone wrong in the "
                "reasoning?",
        "options": [
            {"text": "The rods were all at the same temperature to start with",
             "correct": False,
             "why": "True and not the error. The error is about what the "
                    "result actually measured."},
            {"text": "The conclusion is about temperature and the test "
                     "measured a rate",
             "correct": True},
            {"text": "The test was not repeated enough times to conclude "
                     "anything",
             "correct": False,
             "why": "Repeating it would give the same result again. The "
                    "problem is what is being read into it, not how reliable "
                    "it is."},
            {"text": "Wood is not a non-metal, so the categories are wrong",
             "correct": False,
             "why": "Wood is certainly not a metal. The categories are fine; "
                    "the property attached to them is not."},
        ],
        "figure": None,
    },
]
