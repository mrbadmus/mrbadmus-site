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
            {"text": "That the two metals share a route through the rod "
                     "that the glass does not have",
             "correct": False,
             "why": "True, and it is why both metals beat glass — but the "
                    "ORDER also separates the two metals."},
            {"text": "That the glass rod must have been thinner or longer "
                     "than the metal ones were",
             "correct": False,
             "why": "All three rods are identical. Only the material "
                    "changed, which is what makes it a fair test."},
            {"text": "That both metals beat glass, and copper's electrons "
                     "move more freely than iron's",
             "correct": True},
            {"text": "That copper must have started off at a higher "
                     "temperature than the other two",
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
             "why": "That is the temperature-is-energy error again. Amount "
                    "depends on how many "
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-05-e05",
        "band": "easier",
        "text": "Which of these is the best INSULATOR?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper is one of the best conductors there is, which is "
                    "the opposite of an insulator."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a metal with free electrons, so it passes "
                    "energy on quickly."},
            {"text": "Wool", "correct": True},
            {"text": "Steel", "correct": False,
             "why": "Steel is a metal too. It conducts more slowly than "
                    "copper, but far faster than any non-metal."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e06",
        "band": "easier",
        "text": "During conduction, do the particles themselves travel along "
                "the material?",
        "options": [
            {"text": "Yes — the hot particles move to the cold end",
             "correct": False,
             "why": "The particles stay where they are. What travels along "
                    "the material is the energy."},
            {"text": "No — they stay in place and pass energy on by "
                     "colliding",
             "correct": True},
            {"text": "Yes — but only in metals, because of free electrons",
             "correct": False,
             "why": "Free electrons do move, but the metal's atoms stay put, "
                    "which is why the spoon keeps its shape."},
            {"text": "No — nothing at all moves during conduction",
             "correct": False,
             "why": "The particles vibrate harder and harder along the "
                    "material; that is how the energy is passed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-05-s05",
        "band": "standard",
        "text": "A metal ruler and a wooden ruler are left in a warm oven for "
                "the same time. Which is uncomfortable to pick up, and why?",
        "options": [
            {"text": "The wooden one, because wood holds more energy",
             "correct": False,
             "why": "Both reach the oven's temperature; the wood simply "
                    "delivers its energy to your hand very slowly."},
            {"text": "The metal one, because metal reaches a higher "
                     "temperature in an oven",
             "correct": False,
             "why": "Both end up at the oven's temperature. The difference is "
                    "how fast each delivers energy."},
            {"text": "Neither, because they are at the same temperature",
             "correct": False,
             "why": "Same temperature, very different feel: what your hand "
                    "senses is the RATE energy arrives at."},
            {"text": "The metal one, because it conducts energy into your "
                     "hand far faster",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s06",
        "band": "standard",
        "text": "Why does a metal teaspoon left standing in hot tea become "
                "too hot to hold, while a plastic one does not?",
        "options": [
            {"text": "Metal conducts energy up the handle quickly; plastic "
                     "hardly does",
             "correct": True},
            {"text": "Metal attracts energy towards itself much more strongly "
                     "than plastic does",
             "correct": False,
             "why": "Nothing attracts energy. It flows from hotter to colder, "
                    "and metal simply passes it on faster."},
            {"text": "Metal is hotter than plastic to start with",
             "correct": False,
             "why": "Both start at room temperature; it is the transfer speed "
                    "that differs."},
            {"text": "Plastic reflects the energy back into the tea",
             "correct": False,
             "why": "Conduction is not reflected. Plastic simply passes "
                    "energy along very slowly."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-05-h05",
        "band": "harder",
        "text": "A fire-walker crosses a bed of glowing wood embers at "
                "several hundred degrees without being burnt. Why?",
        "options": [
            {"text": "The embers are not really hot, only glowing",
             "correct": False,
             "why": "They genuinely are at several hundred degrees; glowing "
                    "is what that temperature looks like."},
            {"text": "Embers conduct very slowly, so each step delivers "
                     "little energy",
             "correct": True},
            {"text": "The feet are cold enough to cool the embers down as "
                     "soon as they touch them",
             "correct": False,
             "why": "A foot cannot cool a bed of embers. What protects it is "
                    "how slowly they deliver energy."},
            {"text": "Walking quickly stops any energy transferring at all",
             "correct": False,
             "why": "Some does transfer every step; the point is that a poor "
                    "conductor delivers very little of it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h06",
        "band": "harder",
        "text": "Why do free electrons make a metal conduct faster than "
                "vibration on its own?",
        "options": [
            {"text": "Because they are far hotter than the atoms they move "
                     "between in the metal",
             "correct": False,
             "why": "An electron does not have its own temperature. It is a "
                    "carrier, not a hot object."},
            {"text": "Because they push the atoms out of the way as they go",
             "correct": False,
             "why": "The atoms stay in place. The electrons travel between "
                    "them without moving them along."},
            {"text": "Because they carry energy right through the metal, not "
                     "atom to atom",
             "correct": True},
            {"text": "Because there are more electrons than atoms in a metal",
             "correct": False,
             "why": "How many there are is not the point; being free to move "
                    "the whole length is."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "p1-05-e07",
        "band": "easier",
        "text": "What is conduction?",
        "options": [
            {"text": "Energy passed through a material by particles colliding "
                     "with their neighbours",
             "correct": True},
            {"text": "Warm material rising through a liquid or gas, carrying "
                     "energy with it",
             "correct": False,
             "why": "That is convection, and it needs a fluid that can move. "
                    "Conduction happens in solids."},
            {"text": "Energy travelling as a wave that needs no material at "
                     "all",
             "correct": False,
             "why": "That is radiation. Conduction cannot cross a gap with no "
                    "particles in it."},
            {"text": "A material giving out its own warmth",
             "correct": False,
             "why": "No material makes warmth of its own. Conduction only "
                    "passes on what arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e08",
        "band": "easier",
        "text": "Which state of matter usually conducts energy best?",
        "options": [
            {"text": "Gases, because their particles travel right across the "
                     "container",
             "correct": False,
             "why": "Gas particles are far apart and rarely collide, so a gas "
                    "is one of the worst conductors."},
            {"text": "Solids, because their particles are packed close "
                     "together and always in contact",
             "correct": True},
            {"text": "Liquids, because their particles can touch and slide "
                     "past",
             "correct": False,
             "why": "Liquid particles are further apart than a solid's, so "
                    "liquids conduct more slowly."},
            {"text": "All three conduct at the same rate",
             "correct": False,
             "why": "They differ enormously. How closely the particles are "
                    "packed makes a large difference."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e09",
        "band": "easier",
        "text": "Why is air such a poor conductor?",
        "options": [
            {"text": "Because air is colder than the objects that are usually "
                     "standing in it",
             "correct": False,
             "why": "Air in a room is at the same temperature as everything "
                    "else in it. Temperature is not the reason."},
            {"text": "Because air weighs almost nothing",
             "correct": False,
             "why": "Air does have weight, and weight is not what decides how "
                    "well something conducts."},
            {"text": "Because its particles are far apart and seldom collide",
             "correct": True},
            {"text": "Because air is a mixture, not a pure substance",
             "correct": False,
             "why": "Pure nitrogen conducts just as badly. Spacing is what "
                    "matters, not purity."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e10",
        "band": "easier",
        "text": "What is a conductor?",
        "options": [
            {"text": "A material that stays warm for a long time once it has "
                     "been heated up",
             "correct": False,
             "why": "Staying warm is what a poor conductor does. A conductor "
                    "passes energy on quickly."},
            {"text": "A material that produces warmth whenever energy passes "
                     "through it",
             "correct": False,
             "why": "No material produces warmth. A conductor only passes on "
                    "what it is given."},
            {"text": "A material that is always hotter than everything around "
                     "it",
             "correct": False,
             "why": "Everything in a room ends up at the room's temperature, "
                    "conductors included."},
            {"text": "A material that lets energy pass through it quickly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e11",
        "band": "easier",
        "text": "Which of these conducts energy the most slowly?",
        "options": [
            {"text": "Wood", "correct": True},
            {"text": "Glass", "correct": False,
             "why": "Glass is slow, but the wax on a glass rod does eventually "
                    "melt. On a wooden rod it never does."},
            {"text": "Iron", "correct": False,
             "why": "Iron is a metal with free electrons, so it conducts "
                    "hundreds of times faster than wood."},
            {"text": "Copper", "correct": False,
             "why": "Copper is the fastest conductor in the whole set, not "
                    "the slowest."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e12",
        "band": "easier",
        "text": "Copper and iron are both metals. Which drops its wax first "
                "on the conduction bench?",
        "options": [
            {"text": "Iron, because it is the heavier and denser of the two "
                     "metals being raced",
             "correct": False,
             "why": "Density is not the mechanism. Copper's electrons move "
                    "more freely, and copper wins by a wide margin."},
            {"text": "Copper, in roughly a third of the time the iron rod "
                     "needs",
             "correct": True},
            {"text": "Whichever rod is nearer the flame when it is lit",
             "correct": False,
             "why": "Both rods are the same distance from the flame. That is "
                    "what makes the race fair."},
            {"text": "Neither — two metals always match",
             "correct": False,
             "why": "Metals differ a great deal. Copper is about three times "
                    "faster than iron here."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e13",
        "band": "easier",
        "text": "On the bench the wax on the wooden rod never melts at all. "
                "What does that show?",
        "options": [
            {"text": "That wood conducts so slowly that the flame end scorches "
                     "first",
             "correct": True},
            {"text": "That wood blocks energy completely, so none of it gets "
                     "inside",
             "correct": False,
             "why": "Energy does enter — the flame end gets very hot. It "
                    "simply travels along extremely slowly."},
            {"text": "That the wooden rod was too far from the flame",
             "correct": False,
             "why": "All four rods sit the same distance from the flame, "
                    "which is what makes the comparison fair."},
            {"text": "That wax will not melt while resting on wood",
             "correct": False,
             "why": "Wax melts at the same temperature whatever it sits on. "
                    "The far end simply never gets there."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e14",
        "band": "easier",
        "text": "Do non-metals such as glass and wood contain free electrons?",
        "options": [
            {"text": "Yes, but far fewer of them than any metal contains",
             "correct": False,
             "why": "They have none at all. Every electron in them is held "
                    "inside a bond."},
            {"text": "Yes, and that is why they conduct energy at all",
             "correct": False,
             "why": "They conduct by particle-to-particle vibration only, "
                    "which is the slow route."},
            {"text": "No — that missing second route is the whole difference",
             "correct": True},
            {"text": "No, but they gain some as soon as they are warmed up",
             "correct": False,
             "why": "Heating adds energy, never electrons. A hot glass rod "
                    "has exactly as many as a cold one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e15",
        "band": "easier",
        "text": "What happens to the particles at the hot end of a metal bar?",
        "options": [
            {"text": "They break away from the bar and travel down towards "
                     "the cooler end of it",
             "correct": False,
             "why": "Nothing breaks away. Each particle stays on its own spot "
                    "and vibrates there."},
            {"text": "They vibrate more strongly about their fixed positions",
             "correct": True},
            {"text": "They stop moving altogether once they have been heated "
                     "enough",
             "correct": False,
             "why": "Heating makes particles move more, not less. Stopping "
                    "would be cooling to absolute zero."},
            {"text": "They swap places with the cold particles",
             "correct": False,
             "why": "Particles in a solid do not swap places. That is why a "
                    "bar keeps its shape as it heats."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e16",
        "band": "easier",
        "text": "Does a steel bar become shorter at the hot end as energy "
                "travels along it?",
        "options": [
            {"text": "Yes, because the particles there have moved off down "
                     "the bar towards the cold end",
             "correct": False,
             "why": "The particles do not travel. Only the energy moves along "
                    "the bar."},
            {"text": "Yes, because heating always makes a metal contract at "
                     "the end that is hottest",
             "correct": False,
             "why": "Heating makes metals expand very slightly, and in any "
                    "case no particles leave."},
            {"text": "No, because particles leave both ends of the bar equally "
                     "fast",
             "correct": False,
             "why": "No particles are removed from either end. Nothing leaves "
                    "the bar at all."},
            {"text": "No — the matter stays put and only the energy travels",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e17",
        "band": "easier",
        "text": "Why is the base of a saucepan made of metal?",
        "options": [
            {"text": "So that energy passes quickly from the hob into the "
                     "food",
             "correct": True},
            {"text": "So that the pan holds a great deal of warmth of its own "
                     "before cooking begins",
             "correct": False,
             "why": "The pan stores very little. Its job is to pass energy "
                    "through, not to hold it."},
            {"text": "So that the pan stays at a safe temperature",
             "correct": False,
             "why": "The base gets extremely hot. That is exactly what makes "
                    "it useful."},
            {"text": "So that the flame cannot get in",
             "correct": False,
             "why": "Any solid base would block a flame. Metal is chosen for "
                    "the speed it passes energy on."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e18",
        "band": "easier",
        "text": "Why is a central-heating radiator made of metal rather than "
                "of plastic?",
        "options": [
            {"text": "Because plastic would melt at the temperature of the hot "
                     "water",
             "correct": False,
             "why": "Plenty of plastics survive hot water easily. The problem "
                    "is that they would not pass energy out."},
            {"text": "Because metal makes its own warmth once hot water "
                     "arrives",
             "correct": False,
             "why": "It makes none. Everything it gives out arrives in the "
                    "water from the boiler."},
            {"text": "Because a metal wall passes the water's energy out into "
                     "the room quickly",
             "correct": True},
            {"text": "Because metal is strong enough to hang on a wall",
             "correct": False,
             "why": "Strength is convenient but it is not the reason. A "
                    "strong plastic radiator would still heat nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e19",
        "band": "easier",
        "text": "A ceramic tile is not a metal, yet it still feels cold to "
                "touch. Why?",
        "options": [
            {"text": "Because ceramic is at a lower temperature than the wood "
                     "beside it",
             "correct": False,
             "why": "Everything in the room is at the same temperature. Only "
                    "the rate of transfer differs."},
            {"text": "Because ceramic contains a few free electrons of its own",
             "correct": False,
             "why": "It has none. It conducts by vibration alone, just faster "
                    "than wood does."},
            {"text": "Because ceramic conducts far better than wood, even "
                     "without free electrons",
             "correct": True},
            {"text": "Because ceramic is a much harder material than wood is",
             "correct": False,
             "why": "Hardness is not the mechanism. How readily the lattice "
                    "passes vibration on is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e20",
        "band": "easier",
        "text": "What does your skin actually detect when you touch "
                "something?",
        "options": [
            {"text": "The temperature of whatever your fingers happen to be "
                     "touching",
             "correct": False,
             "why": "If skin read temperature, a metal and a wooden object in "
                    "one room would feel identical."},
            {"text": "How fast energy is leaving or entering your fingers",
             "correct": True},
            {"text": "How much energy is stored inside the object",
             "correct": False,
             "why": "A huge cold object and a small one can feel the same. "
                    "The amount stored is not detected."},
            {"text": "How hard the surface feels",
             "correct": False,
             "why": "Hardness is felt by pressure sensors. The warm-or-cold "
                    "judgement is about the rate of transfer."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e21",
        "band": "easier",
        "text": "Which of these would make the best handle for a hot frying "
                "pan?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper is the best conductor on the bench, so it would "
                    "deliver the hob's energy straight to your hand."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a metal with free electrons and conducts "
                    "far too well for a handle."},
            {"text": "Steel", "correct": False,
             "why": "Steel conducts more slowly than copper but still far too "
                    "fast for anything you have to hold."},
            {"text": "Wood", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e22",
        "band": "easier",
        "text": "In which direction does energy travel along a bar that has "
                "one hot end and one cold end?",
        "options": [
            {"text": "From the hot end towards the cold end",
             "correct": True},
            {"text": "From the cold end towards the hot end",
             "correct": False,
             "why": "Energy never travels that way on its own. The flow is "
                    "always from hotter to cooler."},
            {"text": "In both directions equally, so that nothing changes",
             "correct": False,
             "why": "If nothing changed, the cold end would never warm up — "
                    "and it does."},
            {"text": "Cold travels from the cold end to the hot end",
             "correct": False,
             "why": "Cold is not a thing that travels. There is one flow, and "
                    "it is energy."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e23",
        "band": "easier",
        "text": "Two objects of different materials have been in the same room "
                "all night. What are their temperatures?",
        "options": [
            {"text": "The metal one is lower, because metals settle at a "
                     "colder point",
             "correct": False,
             "why": "No material has a temperature of its own. Both settle at "
                    "the room's."},
            {"text": "Whichever has the greater mass will be lower by morning",
             "correct": False,
             "why": "Mass changes how long settling takes, not where it "
                    "settles. Overnight is ample for both."},
            {"text": "They are the same, and equal to the room's",
             "correct": True},
            {"text": "It depends which one went in first",
             "correct": False,
             "why": "Both have had all night. The order they arrived in makes "
                    "no difference at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e24",
        "band": "easier",
        "text": "Is heat a substance that flows out of hot objects?",
        "options": [
            {"text": "Yes, and it can be weighed on a sensitive enough balance",
             "correct": False,
             "why": "Nobody has ever weighed any. That test was tried, and "
                    "the substance was not there."},
            {"text": "Yes, which is why hot objects become lighter as they "
                     "cool",
             "correct": False,
             "why": "A cooling object does not lose mass. Only energy leaves "
                    "it."},
            {"text": "No — there is no such substance, only energy moving",
             "correct": True},
            {"text": "No, because heat only flows inwards",
             "correct": False,
             "why": "There is no such substance in either direction. Energy "
                    "flows both ways depending on temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e25",
        "band": "easier",
        "text": "What is an insulator?",
        "options": [
            {"text": "A material that lets energy through only slowly",
             "correct": True},
            {"text": "A material with no energy of its own at any temperature",
             "correct": False,
             "why": "Every material above absolute zero holds energy. "
                    "Insulating is about the rate it passes it on."},
            {"text": "A material that destroys the energy reaching it",
             "correct": False,
             "why": "Nothing destroys energy. It passes through an insulator "
                    "very slowly and comes out the other side."},
            {"text": "A material that reflects energy straight back",
             "correct": False,
             "why": "An insulator takes energy in and passes it on slowly. "
                    "Reflecting is what a shiny surface does instead."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e26",
        "band": "easier",
        "text": "A metal skewer is left in a barbecue. Why does the end you "
                "hold become hot?",
        "options": [
            {"text": "Because the flames reach along the whole length of the "
                     "skewer as it lies there",
             "correct": False,
             "why": "Only one end is in the fire. The other end heats even "
                    "when it is well clear of the flames."},
            {"text": "Because the hot particles from the fire travel along "
                     "the inside of the skewer",
             "correct": False,
             "why": "No particles travel along it. Each one vibrates where it "
                    "is and passes energy on."},
            {"text": "Because the skewer makes extra warmth of its own over a "
                     "fire",
             "correct": False,
             "why": "It makes none. Everything it delivers to your hand came "
                    "out of the barbecue."},
            {"text": "Because metal conducts energy quickly from end to end",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e27",
        "band": "easier",
        "text": "Can cold be conducted from a cold object into a warm one?",
        "options": [
            {"text": "Yes, and that is exactly why a metal spoon feels cold "
                     "when you pick it up",
             "correct": False,
             "why": "Nothing enters your hand. Energy leaves it, which is a "
                    "different statement."},
            {"text": "No — cold is not a thing, so there is nothing to "
                     "conduct",
             "correct": True},
            {"text": "Yes, but only when the cold object is a metal and the "
                     "warm one is not",
             "correct": False,
             "why": "Material makes no difference. There is no cold to move "
                    "in either case."},
            {"text": "No, because cold moves only through a gas",
             "correct": False,
             "why": "Cold is not conducted through anything, because it is "
                    "not a substance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e28",
        "band": "easier",
        "text": "Which conducts energy better, a metal or water?",
        "options": [
            {"text": "Water, because it can flow around the object it is "
                     "touching and reach all of it",
             "correct": False,
             "why": "Flowing is convection, which is a different route. By "
                    "conduction alone metal wins easily."},
            {"text": "Water, because its particles are packed closer together "
                     "than the particles of a metal",
             "correct": False,
             "why": "A liquid's particles are further apart than a solid's, "
                    "and water has no free electrons."},
            {"text": "They conduct at much the same rate as one another",
             "correct": False,
             "why": "Metals conduct hundreds of times faster. Their free "
                    "electrons make the difference."},
            {"text": "The metal, by a very wide margin",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e29",
        "band": "easier",
        "text": "On the conduction bench each particle sits inside a grey "
                "ring. What are the rings there to show?",
        "options": [
            {"text": "That every particle stays on the spot it started from",
             "correct": True},
            {"text": "That the particles are joined by bonds",
             "correct": False,
             "why": "The rings mark position, not bonding. They are there to "
                    "show that nothing travels."},
            {"text": "That all the particles are the same size",
             "correct": False,
             "why": "Size is not what the rings record. They record where "
                    "each particle began."},
            {"text": "That the energy has to move in a circle before it passes "
                     "on",
             "correct": False,
             "why": "Energy passes straight along the rod. The circles mark "
                    "home positions, not a path."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-e30",
        "band": "easier",
        "text": "Which route does a metal have that a non-metal does not?",
        "options": [
            {"text": "Radiation, straight out through the surface of the "
                     "metal and away from it",
             "correct": False,
             "why": "Every material radiates. That is not what separates a "
                    "metal from a non-metal."},
            {"text": "Convection, because the particles inside a metal are "
                     "free to circulate within it",
             "correct": False,
             "why": "Nothing circulates inside a solid. Convection needs a "
                    "liquid or a gas."},
            {"text": "Free electrons moving through the whole structure",
             "correct": True},
            {"text": "Vibration passed from one particle to the next along it",
             "correct": False,
             "why": "Every solid has that route. The metal's advantage is the "
                    "second one on top of it."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · standard ───────────────────────────────
    {
        "id": "p1-05-s07",
        "band": "standard",
        "text": "Copper, iron, glass and wood are raced on the bench. Put "
                "them in order, fastest conductor first.",
        "options": [
            {"text": "Copper, iron, glass, wood", "correct": True},
            {"text": "Iron, copper, wood, glass", "correct": False,
             "why": "Copper beats iron by about three times, and glass beats "
                    "wood by more than that again."},
            {"text": "Glass, wood, copper, iron", "correct": False,
             "why": "That is close to the reverse. Both metals conduct far "
                    "faster than either non-metal."},
            {"text": "Wood, glass, iron, copper", "correct": False,
             "why": "Exactly backwards. Wood is the slowest of the four and "
                    "copper the fastest."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s08",
        "band": "standard",
        "text": "A cook leaves a wooden spoon standing in a pan of boiling "
                "sauce for ten minutes. Why is it still safe to pick up?",
        "options": [
            {"text": "Because the sauce cannot reach a temperature that would "
                     "make a wooden handle hot to hold",
             "correct": False,
             "why": "Boiling sauce would scald you instantly. The handle is "
                    "safe because of the wood, not the sauce."},
            {"text": "Because wood conducts so slowly that very little energy "
                     "reaches the handle",
             "correct": True},
            {"text": "Because wood reflects the energy in the sauce back down "
                     "into the pan instead of taking it",
             "correct": False,
             "why": "Wood does take energy in. It simply passes it along "
                    "extremely slowly."},
            {"text": "Because wood is at a lower temperature than metal is "
                     "when both stand in one room",
             "correct": False,
             "why": "Both would be at the sauce's temperature at the bottom. "
                    "Materials have no temperature of their own."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s09",
        "band": "standard",
        "text": "On a frosty morning a metal gate is painful to touch and the "
                "wooden fence beside it is not. Which is the colder?",
        "options": [
            {"text": "The metal gate, because metal reaches a lower "
                     "temperature outdoors than wood ever does",
             "correct": False,
             "why": "Both settle at the air's temperature overnight. A "
                    "thermometer reads the same on each."},
            {"text": "The wooden fence, because it takes in less of the "
                     "morning sunshine than the gate does",
             "correct": False,
             "why": "In the shade before dawn neither has had any sun, and "
                    "the gate still hurts to touch."},
            {"text": "Neither — they are both at the temperature of the air, "
                     "and only the transfer rate differs",
             "correct": True},
            {"text": "It depends which one you touch first",
             "correct": False,
             "why": "The order makes no difference. The gate feels colder "
                    "every time, in any order."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s10",
        "band": "standard",
        "text": "A computer chip is fitted with a block of aluminium called a "
                "heat sink. What is it for?",
        "options": [
            {"text": "To absorb the chip's energy and destroy it before it "
                     "can build up inside the case",
             "correct": False,
             "why": "Nothing destroys energy. The block moves it out to the "
                    "air, where it spreads."},
            {"text": "To keep the chip at a lower temperature than the air "
                     "around it inside the computer",
             "correct": False,
             "why": "Nothing can hold the chip below the air's temperature. "
                    "The block only slows the rise."},
            {"text": "To make the chip produce less energy while it is doing "
                     "difficult calculations",
             "correct": False,
             "why": "The block cannot change what the chip transfers. It "
                    "changes where that energy goes."},
            {"text": "To conduct energy away from the chip quickly and spread "
                     "it over a large surface",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s11",
        "band": "standard",
        "text": "A good saucepan has a copper base and a wooden handle. What "
                "does that tell you about how it was designed?",
        "options": [
            {"text": "That one end was chosen to pass energy on fast and the "
                     "other to pass it on slowly",
             "correct": True},
            {"text": "That the copper was chosen for its appearance and the "
                     "wood because it costs less to buy",
             "correct": False,
             "why": "Both choices are about conduction. A cheap steel handle "
                    "would still be unusable."},
            {"text": "That copper adds warmth to the food while the wooden "
                     "handle takes warmth away from it",
             "correct": False,
             "why": "Neither adds or removes warmth. Both simply pass energy "
                    "on at very different rates."},
            {"text": "That the handle is the part that gets hottest",
             "correct": False,
             "why": "The handle is the part that stays coolest, which is why "
                    "it is made of wood."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s12",
        "band": "standard",
        "text": "Why must the four rods in a conduction race all be the same "
                "thickness?",
        "options": [
            {"text": "Because a thicker rod looks different, and the results "
                     "would be harder to write up neatly",
             "correct": False,
             "why": "Appearance is not the issue. A thicker rod genuinely "
                    "carries energy at a different rate."},
            {"text": "Because a thicker rod would carry energy at a different "
                     "rate, hiding the effect of the material",
             "correct": True},
            {"text": "Because the wax blobs have to be exactly the same size "
                     "as one another on every single rod",
             "correct": False,
             "why": "Blob size is a separate control, and it is not what rod "
                    "thickness is about."},
            {"text": "Because a thin rod would melt in the flame",
             "correct": False,
             "why": "None of these rods melts. Thickness matters because it "
                    "changes the rate, not the safety."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s13",
        "band": "standard",
        "text": "Glass and iron are both solids with their particles in "
                "contact. Why does the glass take so much longer?",
        "options": [
            {"text": "Because glass is transparent, so energy passes straight "
                     "through it instead of along it",
             "correct": False,
             "why": "Transparency is about light. It has nothing to do with "
                    "how a solid conducts."},
            {"text": "Because glass particles are much further apart than the "
                     "particles in a piece of iron",
             "correct": False,
             "why": "Glass is a dense solid with its particles in contact. "
                    "The missing thing is a second route."},
            {"text": "Because glass has only the particle-to-particle route, "
                     "and iron has free electrons as well",
             "correct": True},
            {"text": "Because glass starts at a lower temperature",
             "correct": False,
             "why": "Both rods start at room temperature. That is what makes "
                    "the race a fair one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s14",
        "band": "standard",
        "text": "The flame end of a glass rod is glowing while the far end is "
                "barely warm. What does that show?",
        "options": [
            {"text": "That glass passes energy along so slowly that a large "
                     "difference can be held across one rod",
             "correct": True},
            {"text": "That the far end of a glass rod is a different material "
                     "from the end that is in the flame",
             "correct": False,
             "why": "It is one rod of one material. Only the energy arriving "
                    "at each end differs."},
            {"text": "That energy stops travelling once a rod reaches a "
                     "certain temperature at the hot end",
             "correct": False,
             "why": "It keeps travelling. Leave the rod long enough and the "
                    "far end does warm up."},
            {"text": "That glass takes in no energy from the flame",
             "correct": False,
             "why": "It takes in plenty — the glowing end proves it. Getting "
                    "it along the rod is the slow part."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s15",
        "band": "standard",
        "text": "Many good pans have a copper or aluminium layer in the base "
                "rather than plain steel. Why is that worth the cost?",
        "options": [
            {"text": "Because those metals hold more warmth in the base once "
                     "the hob has been switched off",
             "correct": False,
             "why": "Holding warmth is a different property. The layer is "
                    "there to spread energy while cooking."},
            {"text": "Because those metals reach a higher temperature than "
                     "steel does when they sit on a hob",
             "correct": False,
             "why": "All three reach the hob's temperature. What differs is "
                    "how quickly energy spreads sideways."},
            {"text": "Because those metals conduct faster, so the base heats "
                     "evenly instead of in a hot ring",
             "correct": True},
            {"text": "Because those metals let the flame through to the food",
             "correct": False,
             "why": "No solid base lets a flame through. The layer works by "
                    "spreading energy, not by letting it past."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s16",
        "band": "standard",
        "text": "The bench says its times are illustrative rather than "
                "measured. What may still fairly be concluded from them?",
        "options": [
            {"text": "Nothing at all, because a model that is not measured "
                     "can never teach anybody anything",
             "correct": False,
             "why": "A model can teach an order and a rough ratio honestly. "
                    "It simply must not be quoted as data."},
            {"text": "The order of the four materials, and roughly how big "
                     "the gaps between them are",
             "correct": True},
            {"text": "The exact number of seconds each material would take in "
                     "a real classroom experiment",
             "correct": False,
             "why": "Those are the one thing the note rules out. The seconds "
                    "were chosen to be watchable."},
            {"text": "The temperature of the flame used on each rod",
             "correct": False,
             "why": "The bench never claims a flame temperature, so nothing "
                    "about it can be read off."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s17",
        "band": "standard",
        "text": "Why must all four rods start at the same temperature before "
                "the flame is lit?",
        "options": [
            {"text": "Because a rod that started warmer would need less "
                     "energy to reach the melting point of the wax",
             "correct": True},
            {"text": "Because a rod that started warmer would have fewer "
                     "particles left inside it to pass energy on",
             "correct": False,
             "why": "Warming a rod removes no particles. Every one of them is "
                    "still there, vibrating harder."},
            {"text": "Because a warm rod cannot conduct energy at all until "
                     "it has been allowed to cool right down",
             "correct": False,
             "why": "A warm rod conducts perfectly well. The problem is that "
                    "the comparison stops being fair."},
            {"text": "Because the wax would already have melted",
             "correct": False,
             "why": "Room temperature is far below the wax's melting point, "
                    "so no wax has melted before the flame is lit."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s18",
        "band": "standard",
        "text": "A park has a metal bench and a wooden bench side by side in "
                "full summer sun. Which is more painful to sit on?",
        "options": [
            {"text": "The wooden one, because wood holds far more energy than "
                     "metal does at the same temperature",
             "correct": False,
             "why": "The amount held is not what your skin detects. The rate "
                    "of delivery is."},
            {"text": "Neither, because both benches have been standing in "
                     "exactly the same sunshine all afternoon",
             "correct": False,
             "why": "Both are hot, but only one delivers that energy to you "
                    "fast enough to hurt."},
            {"text": "The metal one, because it delivers its energy into you "
                     "far faster than the wood can",
             "correct": True},
            {"text": "The metal one, because metal reaches a much higher "
                     "temperature in sunshine than wood does",
             "correct": False,
             "why": "Both reach a similar temperature in the same sun. The "
                    "difference is the rate of transfer into you."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s19",
        "band": "standard",
        "text": "Two bars at 200 °C, one copper and one iron, are touched "
                "briefly. Which is more likely to burn, and why?",
        "options": [
            {"text": "The copper, because it delivers energy into the skin "
                     "about three times faster",
             "correct": True},
            {"text": "The iron, because iron stores much more energy in it at "
                     "200 °C than copper does",
             "correct": False,
             "why": "How much is stored is not what burns you. How fast it "
                    "arrives at your skin is."},
            {"text": "Neither, because both bars are at exactly the same "
                     "temperature as one another",
             "correct": False,
             "why": "Same temperature, very different delivery rate — which "
                    "is the whole point of this lesson."},
            {"text": "The iron, because iron is the harder of the two metals",
             "correct": False,
             "why": "Hardness is not the mechanism. Copper's electrons move "
                    "energy faster, which is what matters."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s20",
        "band": "standard",
        "text": "A ceramic mug full of tea is too hot to hold by the body but "
                "comfortable by the handle. Why?",
        "options": [
            {"text": "Because the handle is made of a different material from "
                     "the rest of the mug it is joined to",
             "correct": False,
             "why": "It is the same ceramic throughout. The difference is the "
                    "path the energy has to take."},
            {"text": "Because the tea cannot touch the handle, and ceramic "
                     "conducts too slowly to warm it quickly",
             "correct": True},
            {"text": "Because the handle is shaped to reflect the tea's "
                     "energy back into the body of the mug",
             "correct": False,
             "why": "Shape does not reflect conducted energy. The handle is "
                    "simply a long, slow route."},
            {"text": "Because ceramic is a far better conductor than metal",
             "correct": False,
             "why": "Ceramic conducts far more slowly than metal, which is "
                    "exactly why the handle stays cool."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s21",
        "band": "standard",
        "text": "Baking trays are made of metal rather than of ceramic. What "
                "is the advantage in the oven?",
        "options": [
            {"text": "The metal reaches a far higher temperature in an oven "
                     "than any ceramic dish could reach",
             "correct": False,
             "why": "Everything in the oven reaches the oven's temperature. "
                    "The difference is how fast it gets there."},
            {"text": "The metal conducts the oven's energy into the food "
                     "quickly, so the base browns properly",
             "correct": True},
            {"text": "The metal holds far more energy than ceramic does, so "
                     "the food keeps cooking out of the oven",
             "correct": False,
             "why": "A thin metal tray holds very little. Ceramic holds more, "
                    "which is why it is used for slow dishes."},
            {"text": "The metal stops the oven's energy reaching the food",
             "correct": False,
             "why": "That would be the opposite of useful. The tray is chosen "
                    "to pass energy on quickly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s22",
        "band": "standard",
        "text": "A metal pan lid becomes too hot to lift bare-handed while a "
                "glass one stays easier. Explain the difference.",
        "options": [
            {"text": "Metal conducts the steam's energy up to the knob much "
                     "faster than glass does",
             "correct": True},
            {"text": "Metal is a colder material, so more energy flows into "
                     "it before it becomes hot to hold",
             "correct": False,
             "why": "No material is colder in itself. Both lids reach the "
                    "same temperature over a boiling pan."},
            {"text": "Glass reflects the steam's energy straight back down "
                     "into the pan instead of taking it",
             "correct": False,
             "why": "Glass takes energy in. It simply passes it along the lid "
                    "very much more slowly."},
            {"text": "Steam cannot reach the underside of a glass lid in the "
                     "way that it reaches a metal one",
             "correct": False,
             "why": "Steam touches both lids equally. The difference is "
                    "entirely in the material of the lid."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s23",
        "band": "standard",
        "text": "A student says a metal rail “took the cold out of my "
                "hand”. What is the correct description?",
        "options": [
            {"text": "The rail took warmth out of the hand, and cold moved "
                     "the other way to balance it",
             "correct": False,
             "why": "Only one thing moves, and it is energy. There is no "
                    "second flow going the other way."},
            {"text": "Nothing moved at all — the hand simply noticed that the "
                     "rail was a cold material",
             "correct": False,
             "why": "Something certainly moved: the hand lost energy, which "
                    "is why it felt cold."},
            {"text": "The rail put cold into the hand, which is why the hand "
                     "felt colder after touching it",
             "correct": False,
             "why": "Cold is not a substance, so nothing can be put in. "
                    "Energy left the hand instead."},
            {"text": "Energy moved quickly out of the hand into the rail",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s24",
        "band": "standard",
        "text": "A metal spoon standing in a hot drink ends up warm along its "
                "whole length, not just the part in the liquid. Why?",
        "options": [
            {"text": "Because the drink creeps up the spoon and warms every "
                     "part of it that the liquid reaches",
             "correct": False,
             "why": "The liquid stays in the mug. Energy travels up the dry "
                    "metal without anything moving with it."},
            {"text": "Because each particle passes energy to its neighbour "
                     "all the way to the top of the spoon",
             "correct": True},
            {"text": "Because the warm particles from the drink travel up "
                     "through the spoon towards the handle",
             "correct": False,
             "why": "No particles travel up the spoon. They vibrate on the "
                    "spot and hand energy on."},
            {"text": "Because a metal spoon makes warmth of its own",
             "correct": False,
             "why": "It makes none. Every joule in the handle arrived from "
                    "the drink through the metal."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s25",
        "band": "standard",
        "text": "A copper rod drops its wax in about nine seconds. Roughly "
                "how long would you predict for an identical iron rod?",
        "options": [
            {"text": "About three seconds, because iron is denser",
             "correct": False,
             "why": "Iron is slower than copper, not faster, and density is "
                    "not what decides the rate."},
            {"text": "About nine seconds as well, since both rods are metals "
                     "and metals all behave alike",
             "correct": False,
             "why": "Metals differ a great deal. Copper's electrons move far "
                    "more freely than iron's do."},
            {"text": "About twenty seconds, because iron conducts roughly a "
                     "third as well as copper",
             "correct": True},
            {"text": "About two and a half minutes, which is the figure the "
                     "glass rod takes on the same bench",
             "correct": False,
             "why": "That is the glass figure. Iron sits between copper and "
                    "glass, much closer to copper."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s26",
        "band": "standard",
        "text": "A heat sink is made of aluminium and cut into many thin "
                "fins. Why the fins as well as the metal?",
        "options": [
            {"text": "The fins make the block lighter, so the chip underneath "
                     "does not have to carry as much weight",
             "correct": False,
             "why": "Weight is a convenience. The fins are there to put more "
                    "metal in contact with the air."},
            {"text": "The fins stop energy escaping from the sides of the "
                     "block once it has been conducted there",
             "correct": False,
             "why": "Escaping is exactly what is wanted. The fins help energy "
                    "leave, not stay."},
            {"text": "The fins give a much larger area of metal in contact "
                     "with the air around it",
             "correct": True},
            {"text": "The fins make the aluminium itself into a much better "
                     "conductor of energy than before",
             "correct": False,
             "why": "Cutting metal does not change how well it conducts. It "
                    "changes how much surface touches the air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s27",
        "band": "standard",
        "text": "The cooling pipes at the back of a fridge are made of metal. "
                "Why does that matter?",
        "options": [
            {"text": "Because metal passes the energy taken from inside the "
                     "fridge out into the kitchen air quickly",
             "correct": True},
            {"text": "Because metal makes the pipes cold, which is what "
                     "keeps the inside of the fridge chilled",
             "correct": False,
             "why": "The pipes at the back are warm, not cold. They are "
                    "where energy leaves the fridge."},
            {"text": "Because metal is strong enough to hold the pressure "
                     "inside the pipes without bursting open",
             "correct": False,
             "why": "Strength matters for the engineering, but the pipes are "
                    "on the outside to get rid of energy."},
            {"text": "Because metal stops energy getting back into the fridge",
             "correct": False,
             "why": "Metal is the worst possible choice for stopping energy. "
                    "The insulation in the walls does that job."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s28",
        "band": "standard",
        "text": "A student is told to hold a metal rod in a Bunsen flame with "
                "tongs rather than by hand. Why?",
        "options": [
            {"text": "Because a bare hand would leave grease on the rod and "
                     "change how quickly it conducted energy",
             "correct": False,
             "why": "Grease makes no measurable difference. The reason is "
                    "that the free end becomes dangerously hot."},
            {"text": "Because metal conducts fast enough to make the far end "
                     "too hot to hold within seconds",
             "correct": True},
            {"text": "Because the flame would reach along the rod to the hand "
                     "holding the far end of it",
             "correct": False,
             "why": "A flame does not travel along a rod. The energy does, by "
                    "conduction."},
            {"text": "Because a hand would cool the rod and spoil the test",
             "correct": False,
             "why": "A hand takes a tiny share. The real reason is that the "
                    "hand would be burnt."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s29",
        "band": "standard",
        "text": "An iron poker is left with one end in a fire. Describe the "
                "temperature along it after a few minutes.",
        "options": [
            {"text": "Coldest in the fire and hottest at the far end, since "
                     "energy always collects at the far end",
             "correct": False,
             "why": "Energy does not collect at one end. It flows from hot to "
                    "cold, so the fire end is hottest."},
            {"text": "The same all the way along, because iron conducts "
                     "energy so quickly from one end to the other",
             "correct": False,
             "why": "Iron is fast but not instant. There is a clear "
                    "difference between the two ends."},
            {"text": "Hottest in the fire, falling steadily along the poker "
                     "to the coolest point at the handle",
             "correct": True},
            {"text": "Hot at both ends and cool in the middle of the poker",
             "correct": False,
             "why": "Nothing heats the far end directly, so it cannot be "
                    "hotter than the metal next to it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-s30",
        "band": "standard",
        "text": "Two identical ice cubes are put on a metal tray and a wooden "
                "board, both at room temperature. Which melts first?",
        "options": [
            {"text": "The one on the wooden board, because wood is the warmer "
                     "of the two materials to begin with",
             "correct": False,
             "why": "Both start at room temperature. Neither is warmer than "
                    "the other at the start."},
            {"text": "Both at the same rate, since the tray and the board are "
                     "at the same temperature as each other",
             "correct": False,
             "why": "Same temperature, very different rate: the metal "
                    "delivers its energy to the ice far faster."},
            {"text": "The one on the wooden board, because ice always melts "
                     "faster on a surface that feels warm",
             "correct": False,
             "why": "Wood only feels warmer. It actually delivers energy to "
                    "the ice more slowly than metal does."},
            {"text": "The one on the metal tray, because metal conducts "
                     "energy into the ice much faster",
             "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · harder ─────────────────────────────────
    {
        "id": "p1-05-h07",
        "band": "harder",
        "text": "Why does the particle-to-particle route work faster in a "
                "stiff solid than in a soft one?",
        "options": [
            {"text": "Because a stiff solid contains more free electrons than "
                     "a soft one does at the same temperature",
             "correct": False,
             "why": "Stiffness has nothing to do with free electrons. Diamond "
                    "is extremely stiff and has none at all."},
            {"text": "Because the particles are bound tightly, so a vibration "
                     "is passed on almost at once",
             "correct": True},
            {"text": "Because a stiff solid holds far more energy than a soft "
                     "one does",
             "correct": False,
             "why": "How much is held is a separate property. The question is "
                    "how quickly a wobble is handed on."},
            {"text": "Because the particles in a stiff solid travel along it",
             "correct": False,
             "why": "Particles in any solid stay on their own spots. Nothing "
                    "travels along, however stiff the material."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h08",
        "band": "harder",
        "text": "A steel block and a cork block have both been at 20 °C all "
                "night. Predict what a thermal camera shows and what a hand "
                "reports.",
        "options": [
            {"text": "The camera shows both the same; the hand reports the "
                     "steel as colder",
             "correct": True},
            {"text": "The camera shows the steel colder, and the hand agrees "
                     "with the camera about which is colder",
             "correct": False,
             "why": "A camera reads temperature and both are at 20 °C, so it "
                    "cannot show one as colder."},
            {"text": "The camera shows the cork colder, while the hand "
                     "reports the steel as the colder of the two",
             "correct": False,
             "why": "Neither is colder. A camera reading either as colder "
                    "would be a fault in the camera."},
            {"text": "Both the camera and the hand report the two blocks as "
                     "being at exactly the same temperature",
             "correct": False,
             "why": "The hand is not a thermometer. It reports the steel as "
                    "colder because energy leaves it faster."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h09",
        "band": "harder",
        "text": "A class wants real conduction times rather than the bench's "
                "illustrative ones. What is the best plan?",
        "options": [
            {"text": "Use the bench's figures but round them, since rounding "
                     "removes the illustrative part of them",
             "correct": False,
             "why": "Rounding an invented number gives another invented "
                    "number. Only measuring produces data."},
            {"text": "Time real rods of one thickness with one flame, and "
                     "repeat each material several times",
             "correct": True},
            {"text": "Time one rod of each material once, since the four "
                     "differ so much",
             "correct": False,
             "why": "A single run cannot show how much a result scatters, so "
                    "there is nothing to compare against."},
            {"text": "Ask a teacher which times are correct",
             "correct": False,
             "why": "A figure taken on authority is still not a measurement "
                    "this class has made."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h10",
        "band": "harder",
        "text": "A metal spoon left in a hot drink gets hotter for a while "
                "and then stops. Why does it stop?",
        "options": [
            {"text": "Because the spoon runs out of room to hold any more "
                     "energy inside the metal it is made of",
             "correct": False,
             "why": "There is no limit of that kind. The spoon would keep "
                    "warming if the drink stayed hotter than it."},
            {"text": "Because the metal stops conducting once it has reached "
                     "a certain temperature of its own",
             "correct": False,
             "why": "Metal conducts at any temperature. What changes is the "
                    "difference driving the flow."},
            {"text": "Because the spoon and the drink have reached the same "
                     "temperature, so the flow evens out",
             "correct": True},
            {"text": "Because the drink has by then run out of energy",
             "correct": False,
             "why": "The drink still holds a great deal. It has simply "
                    "stopped being hotter than the spoon."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h11",
        "band": "harder",
        "text": "A firefighter's axe has a steel head and a thickly wrapped "
                "handle. Explain the two choices.",
        "options": [
            {"text": "Steel is chosen because it stays cold in a fire, and "
                     "the wrapping keeps the cold in the handle",
             "correct": False,
             "why": "Steel does not stay cold, and there is no cold to keep "
                    "anywhere. Both halves are wrong."},
            {"text": "Steel is chosen for strength, and the wrapping slows "
                     "the energy travelling to the hand",
             "correct": True},
            {"text": "Steel is chosen because it conducts badly, and the "
                     "wrapping improves grip",
             "correct": False,
             "why": "Steel conducts well, which is exactly the problem the "
                    "wrapping is there to solve."},
            {"text": "Both parts are chosen to conduct as fast as possible",
             "correct": False,
             "why": "A fast-conducting handle would be the last thing you "
                    "want on an axe used near a fire."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h12",
        "band": "harder",
        "text": "You are designing a soldering iron. Which pair of materials "
                "should the tip and the grip be made from, and why?",
        "options": [
            {"text": "A wooden tip and a copper grip, so that the heat is "
                     "kept at the end you are holding",
             "correct": False,
             "why": "That is the design exactly reversed. The tip has to "
                    "deliver energy and the grip must not."},
            {"text": "A copper tip and a copper grip, so the whole tool "
                     "warms up evenly along its length",
             "correct": False,
             "why": "An evenly hot tool cannot be held. The two ends need "
                    "opposite properties."},
            {"text": "A wooden tip and a wooden grip, so nothing about the "
                     "tool ever becomes dangerously hot",
             "correct": False,
             "why": "A wooden tip would never deliver enough energy to melt "
                    "solder, so the tool would not work."},
            {"text": "A copper tip and a plastic grip",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h13",
        "band": "harder",
        "text": "A student says wood is a good insulator because it is light. "
                "What is wrong with that reasoning?",
        "options": [
            {"text": "Nothing is wrong — lighter materials really do conduct "
                     "more slowly than heavier ones do",
             "correct": False,
             "why": "Aluminium is light and conducts well; lead is heavy and "
                    "conducts badly. Weight does not decide it."},
            {"text": "Wood is not actually light, so the reason given cannot "
                     "be the explanation for anything",
             "correct": False,
             "why": "Wood is light. The trouble is that being light is not "
                    "what makes it insulate."},
            {"text": "Weight is not the mechanism — having no free electrons "
                     "and trapping air is",
             "correct": True},
            {"text": "Wood is a conductor rather than an insulator",
             "correct": False,
             "why": "Wood is one of the best insulators on the bench. The "
                    "reasoning is wrong, not the conclusion."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h14",
        "band": "harder",
        "text": "On a copper rod the wax melts at 20 cm in nine seconds. What "
                "would you expect at 40 cm along the same rod?",
        "options": [
            {"text": "Under nine seconds, because the energy has built up "
                     "along the rod by the time it gets there",
             "correct": False,
             "why": "Energy does not build up ahead of itself. A more distant "
                    "blob always melts later, not sooner."},
            {"text": "Exactly nine seconds again, because the material of the "
                     "rod has not been changed at all",
             "correct": False,
             "why": "The material is the same but the distance is not, and "
                    "distance is what the extra time is for."},
            {"text": "Nothing can be predicted, because the bench gives no "
                     "figure for a rod of that length",
             "correct": False,
             "why": "A sensible prediction can be made: further along means "
                    "longer, whatever the exact figure."},
            {"text": "Noticeably longer than nine seconds",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h15",
        "band": "harder",
        "text": "Why does energy never travel by conduction from the cold end "
                "of a bar to the hot end on its own?",
        "options": [
            {"text": "Because the particles at the hot end vibrate more, so "
                     "the net flow is always away from them",
             "correct": True},
            {"text": "Because the particles at the cold end are locked in "
                     "place and cannot pass anything on at all",
             "correct": False,
             "why": "Cold particles still vibrate and still pass energy on. "
                    "They simply pass on less than they receive."},
            {"text": "Because cold flows the other way and blocks the energy "
                     "from travelling in that direction",
             "correct": False,
             "why": "There is no such thing as a flow of cold. Only energy "
                    "moves, and it moves one way."},
            {"text": "Because a bar has a built-in direction of flow",
             "correct": False,
             "why": "Turn the bar round and the flow reverses at once. The "
                    "direction comes from the temperatures."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h16",
        "band": "harder",
        "text": "A cook can lift a hot oven shelf with a dry cloth but is "
                "scalded through a damp one. Explain.",
        "options": [
            {"text": "The damp cloth is colder, so the shelf's energy is "
                     "pulled into it much more strongly",
             "correct": False,
             "why": "Both cloths start at room temperature. What differs is "
                    "how fast each passes energy through."},
            {"text": "The damp cloth is heavier, and a heavier material "
                     "always conducts energy faster than a light one",
             "correct": False,
             "why": "Weight does not decide conduction. Water replacing "
                    "trapped air is what changes the rate."},
            {"text": "Water has filled the air spaces, and water conducts "
                     "far better than trapped air",
             "correct": True},
            {"text": "The water boils and the steam carries energy by "
                     "radiation straight through to the hand",
             "correct": False,
             "why": "Steam is involved in the pain but the route is not "
                    "radiation, and the wet cloth conducts before it boils."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h17",
        "band": "harder",
        "text": "Two identical copper rods are put in flames, one much hotter "
                "than the other. Which drops its wax sooner, and why?",
        "options": [
            {"text": "Neither — the wax on identical copper rods always melts "
                     "at the same moment whatever the flame",
             "correct": False,
             "why": "The flame sets how much energy arrives each second, so "
                    "it certainly changes the timing."},
            {"text": "The one in the cooler flame, because a gentler heating "
                     "lets the energy spread more evenly",
             "correct": False,
             "why": "Spreading evenly does not make it arrive sooner. The "
                    "hotter flame wins every time."},
            {"text": "The one in the cooler flame, because copper conducts "
                     "better when it is not overheated",
             "correct": False,
             "why": "Copper does not conduct better when cooler. Nothing "
                    "about the metal improves in a weaker flame."},
            {"text": "The one in the hotter flame, because a bigger "
                     "temperature difference drives a faster flow",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h18",
        "band": "harder",
        "text": "Metals are the best conductors of electricity and also the "
                "best conductors of energy. Why do the two go together?",
        "options": [
            {"text": "Because a material that carries a current always heats "
                     "up, and heating makes it conduct better",
             "correct": False,
             "why": "Heating is a consequence, not the link. A cold copper "
                    "wire conducts both extremely well."},
            {"text": "Because free electrons carry both the charge and the "
                     "energy through the structure",
             "correct": True},
            {"text": "Because metals are denser than non-metals, and density "
                     "is what decides both kinds of conduction",
             "correct": False,
             "why": "Lead is very dense and a poor conductor for a metal. "
                    "Density is not the link."},
            {"text": "It is a coincidence with no shared cause",
             "correct": False,
             "why": "It is not a coincidence. One property, the free "
                    "electrons, is doing both jobs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h19",
        "band": "harder",
        "text": "Why can conduction not carry energy across a gap between two "
                "objects, however small the gap is?",
        "options": [
            {"text": "Because a gap is always colder than the objects on "
                     "either side of it, so nothing can cross",
             "correct": False,
             "why": "A gap has no temperature of its own. The reason is that "
                    "there is nothing in it to collide."},
            {"text": "Because conduction needs particles in contact, and "
                     "across a gap there are none to collide",
             "correct": True},
            {"text": "Because energy travels only in straight lines, and a "
                     "gap always bends the path it has to take",
             "correct": False,
             "why": "Straight lines are radiation's habit. Conduction is "
                    "stopped by the absence of particles."},
            {"text": "Because the two objects repel one another across it",
             "correct": False,
             "why": "There is no repulsion between ordinary objects. The gap "
                    "simply contains nothing to pass energy on."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h20",
        "band": "harder",
        "text": "A thin steel sheet and a thick cork block have been in one "
                "room all day. Which feels colder, and what does that say "
                "about each?",
        "options": [
            {"text": "The cork, because a thicker object always holds more "
                     "cold than a thin one of any material",
             "correct": False,
             "why": "There is no cold to hold, and thickness does not decide "
                    "how something feels."},
            {"text": "The steel, because a thin sheet cools down faster "
                     "overnight than a thick block ever could",
             "correct": False,
             "why": "Both reached room temperature long ago. Cooling speed "
                    "is not what the hand is reporting now."},
            {"text": "The steel, because it removes energy from the hand far "
                     "faster than the cork can",
             "correct": True},
            {"text": "Neither, because both are at the room's temperature",
             "correct": False,
             "why": "Both are at the room's temperature and they still feel "
                    "completely different, which is the point."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h21",
        "band": "harder",
        "text": "A student says a longer rod conducts faster because there is "
                "more material in it to carry the energy. Evaluate.",
        "options": [
            {"text": "Correct — more material genuinely does mean a faster "
                     "journey from one end to the other",
             "correct": False,
             "why": "More material means a longer relay. The far end of a "
                    "long rod warms later, not sooner."},
            {"text": "Wrong — a longer rod means more particles to pass the "
                     "energy along, so the far end warms later",
             "correct": True},
            {"text": "Wrong, because the length of a rod makes no difference "
                     "at all to how quickly the far end warms",
             "correct": False,
             "why": "Length makes a large difference. A blob further along "
                    "always melts later."},
            {"text": "Correct, but only for metals and not for non-metals",
             "correct": False,
             "why": "It is wrong for every material. Length slows the journey "
                    "in metals and non-metals alike."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h22",
        "band": "harder",
        "text": "Why is conduction in a solid so different from convection in "
                "a liquid, even though both move energy?",
        "options": [
            {"text": "In conduction the material itself travels, and in "
                     "convection it is only the energy that moves",
             "correct": False,
             "why": "That is the two the wrong way round. Convection is the "
                    "one where material travels."},
            {"text": "In conduction the particles stay put and pass energy "
                     "on; in convection the material itself moves",
             "correct": True},
            {"text": "In conduction no particles are involved at all, and in "
                     "convection the particles carry everything",
             "correct": False,
             "why": "Conduction is entirely about particles colliding. It "
                    "cannot happen without them."},
            {"text": "In conduction the energy travels as a wave through the "
                     "solid, and in convection it does not",
             "correct": False,
             "why": "A wave crossing empty space is radiation. Conduction "
                    "needs particles in contact."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h23",
        "band": "harder",
        "text": "On the bench the free-electron control shows nothing at all "
                "for the glass and wooden rods. Why is that the right "
                "behaviour rather than a fault?",
        "options": [
            {"text": "Because the electrons in those rods are too small for "
                     "the bench to be able to draw them",
             "correct": False,
             "why": "Size is not the issue. There are no free electrons in "
                    "either rod to draw."},
            {"text": "Because non-metals have no free electrons at all, and "
                     "that absence is the whole difference",
             "correct": True},
            {"text": "Because the electrons in a non-metal only appear once "
                     "the rod has been heated in the flame",
             "correct": False,
             "why": "Heating adds energy, never electrons. A hot glass rod "
                    "has no more than a cold one."},
            {"text": "Because the control was designed only for metals and "
                     "has no meaning for any other material",
             "correct": False,
             "why": "It is meaningful for every rod, and what it means for a "
                    "non-metal is that there is nothing to show."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h24",
        "band": "harder",
        "text": "One student says a metal spoon warms the tea and another "
                "says it cools it. Who is right, and when?",
        "options": [
            {"text": "The first, because a spoon at room temperature is "
                     "warmer than any tea that has been standing",
             "correct": False,
             "why": "Hot tea is far warmer than a room-temperature spoon, so "
                    "the flow runs out of the tea."},
            {"text": "The second, because a metal spoon is always colder than "
                     "anything it is put into",
             "correct": False,
             "why": "A spoon has no temperature of its own. Put it in "
                    "iced water and it warms that instead."},
            {"text": "Neither — a spoon cannot change a drink's temperature "
                     "in either direction at all",
             "correct": False,
             "why": "It certainly can. A metal spoon is a fast route out of "
                    "the mug, and a drink cools faster with one in it."},
            {"text": "The second, because the spoon is cooler than the tea "
                     "and gives the energy a fast route to the air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h25",
        "band": "harder",
        "text": "Copper and iron are both metals with free electrons. Why "
                "does copper still conduct about three times better?",
        "options": [
            {"text": "Because iron has no free electrons at all, so it "
                     "conducts only by particle vibration",
             "correct": False,
             "why": "Iron is a metal and has plenty. That is why it still "
                    "beats glass by a wide margin."},
            {"text": "Because copper is the softer of the two metals, and "
                     "softness is what carries energy quickly",
             "correct": False,
             "why": "Softness is not the mechanism. A stiff lattice passes "
                    "vibration on better, not worse."},
            {"text": "Because copper's electrons move more freely through its "
                     "structure than iron's do",
             "correct": True},
            {"text": "Because copper is at a higher temperature than iron",
             "correct": False,
             "why": "Both rods start at room temperature. The difference is "
                    "in the metal, not in the starting point."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h26",
        "band": "harder",
        "text": "Is “a good conductor is always a bad insulator” "
                "a fair statement?",
        "options": [
            {"text": "No, because conducting and insulating are two "
                     "completely unrelated properties of a material",
             "correct": False,
             "why": "They are the same property described from the two ends. "
                    "They cannot be unrelated."},
            {"text": "No, because a material can be good at both if it is "
                     "thick enough to slow the flow down",
             "correct": False,
             "why": "Thickness slows any material, good conductor or not. It "
                    "does not change what the material is."},
            {"text": "Yes, but only for metals, since non-metals can be good "
                     "at conducting and at insulating together",
             "correct": False,
             "why": "No material is good at both. Glass conducts better than "
                    "wood and insulates worse, exactly as expected."},
            {"text": "Yes — the two words describe one property from "
                     "opposite ends",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h27",
        "band": "harder",
        "text": "An aluminium can and a glass bottle of the same drink are "
                "put in a freezer together. Which chills first, and why?",
        "options": [
            {"text": "The can, because aluminium conducts energy out of the "
                     "drink far faster than glass does",
             "correct": True},
            {"text": "The bottle, because glass is a colder material than "
                     "aluminium once both are in a freezer",
             "correct": False,
             "why": "Neither material is colder in itself. Both end at the "
                    "freezer's temperature."},
            {"text": "The can, because aluminium holds much less energy in it "
                     "than glass does at the start",
             "correct": False,
             "why": "Most of the energy is in the drink, not the container. "
                    "The rate of transfer is what differs."},
            {"text": "Neither, because both are in the same freezer",
             "correct": False,
             "why": "Both end up equally cold, but one gets there much "
                    "sooner, which is what was asked."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h28",
        "band": "harder",
        "text": "Why would a saucepan made entirely of copper, handle "
                "included, cook beautifully and still be unusable?",
        "options": [
            {"text": "Because copper spreads the hob's energy evenly and "
                     "would also deliver it straight into your hand",
             "correct": True},
            {"text": "Because copper conducts so well that the food would "
                     "burn before the pan itself became warm",
             "correct": False,
             "why": "The pan warms with the food. The problem is at the "
                    "handle, not in the cooking."},
            {"text": "Because copper is too soft a metal to be made into a "
                     "handle that anybody could hold",
             "correct": False,
             "why": "Copper is easily strong enough for a handle. The "
                    "difficulty is the temperature it reaches."},
            {"text": "Because copper would react with the food in the pan",
             "correct": False,
             "why": "That is a separate issue solved by lining. The "
                    "conduction problem is the one this lesson is about."},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h29",
        "band": "harder",
        "text": "A metal bar has one end in melting ice and the other in "
                "boiling water. After a while nothing changes. Describe the "
                "bar.",
        "options": [
            {"text": "Every part of it is at the same temperature, since the "
                     "bar has had time to settle down",
             "correct": False,
             "why": "It cannot settle at one temperature while one end is in "
                    "ice and the other in boiling water."},
            {"text": "It is coldest in the middle, because energy leaves from "
                     "both of its ends at the same time",
             "correct": False,
             "why": "Energy enters at the hot end and leaves at the cold one. "
                    "The middle is between the two."},
            {"text": "Nothing is happening in it at all, because the "
                     "temperature readings have stopped changing",
             "correct": False,
             "why": "Energy is flowing steadily through it the whole time. "
                    "Steady is not the same as stopped."},
            {"text": "It holds a steady slope of temperature, hot end to "
                     "cold, with energy flowing along it all the while",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-05-h30",
        "band": "harder",
        "text": "Design a fair way to rank four materials as conductors. "
                "Which plan would give the most trustworthy ranking?",
        "options": [
            {"text": "Hold a sample of each in your hand and put them in "
                     "order of how cold each one feels to you",
             "correct": False,
             "why": "A hand judges the rate but cannot be read off as a "
                    "number, and different hands disagree."},
            {"text": "Identical rods, one flame, one blob distance, timed "
                     "three times each and averaged",
             "correct": True},
            {"text": "Heat one end of each rod for one minute and then "
                     "measure how heavy each rod has become",
             "correct": False,
             "why": "Mass does not change when something is heated, so the "
                    "measurement would say nothing at all."},
            {"text": "Use rods of different lengths so that every material "
                     "gets a fair chance to show what it can do",
             "correct": False,
             "why": "Different lengths would change the result on their own, "
                    "which is the opposite of a fair test."},
        ],
        "figure": None,
    },
]
