"""P1 lesson 05 — Conduction: twelve questions.

⊕ THE HIGHEST SURVIVAL RATE OF ANY SET IN THE UNIT (MRB-223).

Run 1's twelve were written for a lesson it had invented, but its invented
`p1-05` happened to teach what Design's actually teaches — conduction as
particle-to-particle transfer, the second route through free electrons, and
the touch test. So eleven of the twelve are aimed at the right lesson, which
is not true of `p1-02`, `p1-03` or `p1-04`.

Run 1's own provenance audit flags exactly one: `s04`, which quotes
*"copper dropped all four blobs and wood dropped none in sixty seconds"* off
a bench with four wax blobs and a sixty-second run. Design's bench has ONE
blob per rod and her times are 9 s, 22 s, 150 s and never. The stem is
replaced rather than renumbered.

    CHANGED — eleven stems kept, option ORDER varied for MRB-278 (11):
        e01 e02 e03 e04 · s01 s02 s03 · h01 h02 h03 h04
        Wording is run 1's where it was already right. What moved is which
        button the answer sits behind, and a handful of `why` lines that
        named the invented bench.

    NEW — replaces the one with invented data (1):
        s04  the wax-blob times, on Design's OWN numbers (9 s / 22 s /
             150 s / never) rather than on a four-blob bench

    ⚠️ `h01` IS KEPT AND IT IS THE BEST QUESTION IN THE UNIT. Diamond
    conducts better than copper and has no free electrons, so the
    particle-to-particle route can beat the electron route when the lattice
    is stiff enough. That is correct physics, it is well beyond KS3, and it
    is exactly the right shape for a `harder` band item — it rewards a
    student who understood the MECHANISM rather than the ranking.

⚠️ Answer positions are 2,3,0,1 · 2,3,0,2 · 3,1,0,1 — three of each index.
They do not run in a clean cycle: run 1's option ORDER was kept wherever it
read naturally, and the positions were then balanced across the set rather
than imposed question by question. MRB-278 measures the COUNT, and it is
3/3/3/3.
⚠️ Every distractor is written to the correct answer's own length (MRB-177).

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "conduction"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-05-e01",
        "band": "easier",
        "text": "Which of these is the best conductor of energy?",
        "options": [
            {"text": "Wood", "correct": False,
             "why": "Wood barely conducts at all — it is why a wooden spoon "
                    "can be left in a hot pan."},
            {"text": "Glass", "correct": False,
             "why": "Glass conducts, but slowly. It has no free electrons, "
                    "so only the particle route is available."},
            {"text": "Copper", "correct": True},
            {"text": "Air", "correct": False,
             "why": "Air is one of the worst there is, which is exactly why "
                    "insulators work by trapping it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e02",
        "band": "easier",
        "text": "In conduction through a solid, what actually travels along "
                "the material?",
        "options": [
            {"text": "The particles themselves, moving from the hot end to "
                     "the cold end",
             "correct": False,
             "why": "That is convection, and it needs a fluid. In a solid "
                    "each particle stays where it is."},
            {"text": "Heat, which is a substance that flows between the "
                     "two ends",
             "correct": False,
             "why": "There is no substance called heat. That was caloric "
                    "theory, and a cannon disproved it in 1798."},
            {"text": "Cold, travelling in the opposite direction to the "
                     "warmth",
             "correct": False,
             "why": "Cold is not a thing that moves. There is one flow and "
                    "it is energy."},
            {"text": "Energy, passed on by particles colliding with their "
                     "neighbours",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e03",
        "band": "easier",
        "text": "Why is a saucepan handle usually made of wood or plastic?",
        "options": [
            {"text": "Because those materials conduct very badly, so your "
                     "hand stays cool",
             "correct": True},
            {"text": "Because those materials are lighter than metal and "
                     "easier to lift",
             "correct": False,
             "why": "Weight is a side benefit. The reason is that they do "
                    "not carry energy to your hand."},
            {"text": "Because those materials reflect the radiation coming "
                     "off the hob",
             "correct": False,
             "why": "Radiation is not the problem here. The energy would "
                    "arrive by conduction along the handle."},
            {"text": "Because those materials stay cold whatever is "
                     "happening around them",
             "correct": False,
             "why": "Nothing stays cold on its own. Left long enough the "
                    "handle warms up too — just slowly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e04",
        "band": "easier",
        "text": "What is a free electron?",
        "options": [
            {"text": "An electron that has escaped from the metal out into "
                     "the surrounding air",
             "correct": False,
             "why": "It stays inside the metal. Free means free to move "
                    "WITHIN the structure."},
            {"text": "An electron in a metal that can move right through "
                     "the whole structure",
             "correct": True},
            {"text": "An electron with no charge at all, so that nothing "
                     "holds it in place",
             "correct": False,
             "why": "Every electron has a charge. That is not what makes it "
                    "free to move."},
            {"text": "An extra electron that a metal gains whenever it is "
                     "heated up",
             "correct": False,
             "why": "Heating adds energy, not electrons. They were there "
                    "before the metal was heated."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-05-s01",
        "band": "standard",
        "text": "A metal rod and a glass rod are the same size and both are "
                "solids. Why does the metal conduct so much better?",
        "options": [
            {"text": "Because the metal's particles are packed much more "
                     "closely together",
             "correct": False,
             "why": "Packing helps a little, but glass is dense too. The "
                    "difference is a whole second mechanism."},
            {"text": "Because the metal starts at a higher temperature than "
                     "the glass does",
             "correct": False,
             "why": "They start the same. The difference is in how they "
                    "carry energy, not where they begin."},
            {"text": "Because the metal has free electrons as well as the "
                     "particle-to-particle route",
             "correct": True},
            {"text": "Because the glass reflects the energy back instead of "
                     "letting it through",
             "correct": False,
             "why": "Glass does not reflect it. It passes it on, just far "
                    "more slowly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s02",
        "band": "standard",
        "text": "A metal handrail and a wooden bench sit outside on the same "
                "cold morning. Which is at the lower temperature?",
        "options": [
            {"text": "The metal handrail, because metal is a colder "
                     "material than wood",
             "correct": False,
             "why": "Materials do not have temperatures of their own. Both "
                    "reached the air's temperature overnight."},
            {"text": "The wooden bench, because it holds less energy in "
                     "total than the rail",
             "correct": False,
             "why": "Holding less total energy is not the same as being "
                    "colder. Their temperatures match."},
            {"text": "It depends which one the sun has been shining on "
                     "since dawn",
             "correct": False,
             "why": "A fair thought, but in the shade both still read the "
                    "same. The rail still feels colder."},
            {"text": "Neither — both have reached the temperature of the "
                     "air around them",
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
            {"text": "The distance from the flame to the wax blob on every "
                     "rod being tested",
             "correct": True},
            {"text": "The material each rod is made from, so they can be "
                     "compared properly",
             "correct": False,
             "why": "That is the one thing you must CHANGE — it is what the "
                    "test is about."},
            {"text": "The number of wax blobs put on each of the different "
                     "rods being tested",
             "correct": False,
             "why": "One blob is enough. What matters is that it sits the "
                    "same distance along each rod."},
            {"text": "The colour of the wax used for the blob at the end of "
                     "each rod",
             "correct": False,
             "why": "Colour has nothing to do with conduction. It would "
                    "matter for radiation, next lesson."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s04",
        "band": "standard",
        "text": "On the bench, copper drops its wax in about 9 s, iron in "
                "about 22 s and glass in about 150 s. What does the ORDER "
                "tell you?",
        "options": [
            {"text": "That the two metals share a route the glass does not "
                     "have at all",
             "correct": False,
             "why": "True, and it is why both metals beat glass — but the "
                    "ORDER also separates the two metals."},
            {"text": "That the glass rod must have been thinner than the "
                     "two metal rods were",
             "correct": False,
             "why": "All three rods are identical. Only the material "
                    "changed, which is what makes it a fair test."},
            {"text": "That both metals beat glass, and copper's electrons "
                     "move more freely than iron's",
             "correct": True},
            {"text": "That copper must have started at a higher temperature "
                     "than the other two",
             "correct": False,
             "why": "All three start at room temperature. The difference is "
                    "entirely in how they carry energy."},
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
            {"text": "That diamond must secretly contain free electrons "
                     "after all, just like a metal",
             "correct": False,
             "why": "It genuinely has none. Its electrons are all locked "
                    "into bonds, which is why it does not conduct "
                    "electricity."},
            {"text": "That free electrons are not really what makes copper "
                     "such a good conductor",
             "correct": False,
             "why": "They are — copper's electron route is real. Diamond "
                    "simply beats it by the other one."},
            {"text": "That being extremely hard is the property which makes "
                     "a material conduct well",
             "correct": False,
             "why": "Close, but hardness is not the mechanism. Stiffness of "
                    "the lattice is what passes vibration on fast."},
            {"text": "That the particle-to-particle route can be very fast "
                     "if the lattice is stiff enough",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h02",
        "band": "harder",
        "text": "Why does putting a metal spoon in a cup of hot soup make "
                "the soup cool faster?",
        "options": [
            {"text": "The spoon absorbs the soup's heat and destroys some of "
                     "it in the process",
             "correct": False,
             "why": "Nothing is destroyed. The spoon passes energy on to "
                    "the air, which is a different claim."},
            {"text": "The spoon conducts energy out of the soup and gives "
                     "it a bigger route to the air",
             "correct": True},
            {"text": "The spoon is colder than the soup, so it makes the "
                     "whole cup colder than it was",
             "correct": False,
             "why": "It warms to the soup's temperature within seconds. The "
                    "effect continues after that."},
            {"text": "The metal reflects the radiation that would otherwise "
                     "keep the soup warm",
             "correct": False,
             "why": "Radiation is a small part of it. The spoon works by "
                    "conducting, which is this lesson's route."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h03",
        "band": "harder",
        "text": "Two blocks are at the same temperature, one copper and one "
                "wood. Which holds more energy in its thermal store?",
        "options": [
            {"text": "It cannot be told from their temperatures alone",
             "correct": True},
            {"text": "The copper, because metals conduct energy so much "
                     "better than wood does",
             "correct": False,
             "why": "Conducting well is about the RATE energy moves, not "
                    "about how much is held."},
            {"text": "The wood, because being a better insulator lets it "
                     "hold on to more of it",
             "correct": False,
             "why": "Insulating well is also about rate. It says nothing "
                    "about the amount stored."},
            {"text": "Neither — being at the same temperature means holding "
                     "the same amount of energy",
             "correct": False,
             "why": "That is the `p1-04` error. Amount depends on how many "
                    "particles there are as well."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h04",
        "band": "harder",
        "text": "A student concludes from the rod test that “metals "
                "are hot and non-metals are cold”. What has gone "
                "wrong in the reasoning?",
        "options": [
            {"text": "The rods were not all at the same temperature before "
                     "the test began",
             "correct": False,
             "why": "They were. That is what makes the test fair, and it is "
                    "not where the reasoning failed."},
            {"text": "The conclusion is about temperature and the test "
                     "measured a rate",
             "correct": True},
            {"text": "The test was not repeated enough times for anyone to "
                     "conclude anything",
             "correct": False,
             "why": "Repeating would tighten the numbers but would not fix "
                    "a conclusion about the wrong quantity."},
            {"text": "Wood is not really a non-metal, so the two categories "
                     "are the wrong ones",
             "correct": False,
             "why": "Wood is a non-metal. The categories are fine; the "
                    "quantity being concluded about is not."},
        ],
        "figure": None,
    },
]
