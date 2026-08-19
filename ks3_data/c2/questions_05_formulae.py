"""C2 lesson 05 — Formulae: twelve questions (MRB-269).

These probe the one distinction the lesson is built on — a small number after a
symbol counts atoms inside one particle and changes *what* the substance is,
while a big number in front counts particles and changes *how much* you have —
and the two places the lesson lets that idea run out: the twenty-two
combinations the builder refuses, and the giant structure of salt where there
is no single particle to count. The distractors are built from both declared
misconceptions: ATOM-09 (the small number changes how much of the substance
there is) supplies the "twice as much", "more concentrated" and "the numbers
scale with the volume" options, and ATOM-10 (2H₂O and H₂O₂ hold four atoms
either way, so they must be the same) supplies the totalling trap in the
`harder` band. Three more come from the hook's own rejected answers — that one
liquid is more concentrated, that something is dissolved in it, that they are
one substance at two temperatures — and one from the model-limit card, that a
grain of salt is billions of separate NaCl particles. The `harder` band takes
the rule somewhere the lesson only gestures at (writing six particles of water
from scratch), joins the builder to the model limit (why a CO₂ particle can be
picked out and a salt particle cannot), reads the stretch layer's shared ratio
against itself, and turns the peroxide note into a compound-or-mixture
decision.
"""

UNIT = "C2"
LESSON = "formulae"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c2-05-e01",
        "band": "easier",
        "text": "In the formula CO₂, what is the small 2 written after the O "
                "telling you?",
        "options": [
            {"text": "That there are two particles of carbon dioxide "
                     "present.",
             "correct": False,
             "why": "Particles are counted by a big number written in front, "
                    "like 2CO₂. A small number sits inside one particle and "
                    "counts atoms."},
            {"text": "That one particle of carbon dioxide contains two "
                     "oxygen atoms.",
             "correct": True},
            {"text": "That there is twice as much carbon dioxide as there "
                     "would otherwise be.",
             "correct": False,
             "why": "A small number never tells you how much you have. It "
                    "counts atoms inside one particle, so changing it changes "
                    "the substance, not the amount."},
            {"text": "That each oxygen atom is twice the size of the carbon "
                     "atom.",
             "correct": False,
             "why": "A formula counts atoms and names elements. It says "
                    "nothing at all about how big any of them are."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e02",
        "band": "easier",
        "text": "In the builder you pick carbon and oxygen, set the carbon "
                "count to 1 and the oxygen count to 2. What appears?",
        "options": [
            {"text": "Carbon dioxide, CO₂ — the gas living things breathe "
                     "out.",
             "correct": True},
            {"text": "Carbon monoxide, CO — the colourless gas with no smell "
                     "that kills.",
             "correct": False,
             "why": "Carbon monoxide is one carbon and one oxygen. You set "
                    "the oxygen to 2, and that second oxygen atom makes a "
                    "different substance."},
            {"text": "Nothing at all — no substance anywhere has that "
                     "formula.",
             "correct": False,
             "why": "Most combinations do come back as not a substance, but "
                    "CO₂ is one of the five real ones the builder can make."},
            {"text": "Two particles of carbon monoxide, written 2CO.",
             "correct": False,
             "why": "A count in the builder changes the atoms inside one "
                    "particle. It never changes how many particles there "
                    "are — that is what a big number in front does."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e03",
        "band": "easier",
        "text": "What is actually inside a single grain of table salt?",
        "options": [
            {"text": "Billions of separate particles, each holding one sodium "
                     "and one chlorine.",
             "correct": False,
             "why": "That is the molecule picture, and salt is the substance "
                    "this lesson uses to break it. There are no separate NaCl "
                    "particles anywhere in the grain."},
            {"text": "A mixture of tiny sodium grains and trapped chlorine "
                     "gas.",
             "correct": False,
             "why": "Nothing loose is in there. Every sodium and every "
                    "chlorine atom is locked into one structure, which is why "
                    "salt behaves as neither of them."},
            {"text": "Billions of sodium and chlorine atoms locked in one "
                     "repeating stack.",
             "correct": True},
            {"text": "One large sodium particle with chlorine spread evenly "
                     "through it.",
             "correct": False,
             "why": "Neither element is spread through the other. Sodium and "
                    "chlorine alternate through the stack, one for one, which "
                    "is what NaCl records."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e04",
        "band": "easier",
        "text": "A page of working has 2H₂O written on it. What is the 2 at "
                "the front telling you?",
        "options": [
            {"text": "That each particle has two extra hydrogen atoms in it.",
             "correct": False,
             "why": "The hydrogens are already counted by the small 2 after "
                    "the H. A number in front sits outside the particle "
                    "altogether."},
            {"text": "That this water is twice as concentrated as ordinary "
                     "water.",
             "correct": False,
             "why": "Concentration is about something dissolved, and nothing "
                    "is dissolved here. The 2 counts whole particles of water."},
            {"text": "That this is a different substance from H₂O.",
             "correct": False,
             "why": "It is the same substance — water — just two particles of "
                    "it. Only a change inside the particle changes what the "
                    "substance is."},
            {"text": "That there are two particles of water.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c2-05-s01",
        "band": "standard",
        "text": "Twenty-two of the twenty-seven combinations the builder can "
                "make come back as not a substance. Why so many?",
        "options": [
            {"text": "Chemists have not yet worked out how to make those "
                     "ones.",
             "correct": False,
             "why": "It is not a gap in what has been discovered. Those "
                    "substances do not exist, because the atoms cannot join "
                    "in those numbers."},
            {"text": "They exist only at very high temperatures, so they "
                     "cannot be shown.",
             "correct": False,
             "why": "Heating does not let atoms bond in combinations they "
                    "cannot form. How many of each can join is fixed by the "
                    "elements themselves."},
            {"text": "The elements fix how many of each atom can bond, so "
                     "most invented formulae do not exist.",
             "correct": True},
            {"text": "The builder only stores the five real ones, so every "
                     "other combination is simply missing from it.",
             "correct": False,
             "why": "The refusal is the point of the tool, not a limit of it. "
                    "Atoms genuinely do not join in any combination you like."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s02",
        "band": "standard",
        "text": "Carbon monoxide (CO) and carbon dioxide (CO₂) are both made "
                "of nothing but carbon and oxygen. Which statement about them "
                "is correct?",
        "options": [
            {"text": "They are different substances: one holds an extra "
                     "oxygen in every particle.",
             "correct": True},
            {"text": "They are the same substance, one of them simply more "
                     "concentrated than the other.",
             "correct": False,
             "why": "Concentration would mean more of the same particles in "
                    "the same space. These are two different particles, so "
                    "they are two different substances."},
            {"text": "They are the same substance, shown at two different "
                     "temperatures.",
             "correct": False,
             "why": "Temperature changes how particles move, never what is "
                    "inside them. One carbon with one oxygen and one carbon "
                    "with two are not the same particle."},
            {"text": "CO₂ is carbon monoxide with some extra oxygen dissolved "
                     "in it.",
             "correct": False,
             "why": "Nothing is dissolved in anything. That second oxygen is "
                    "joined inside every single particle, which is what makes "
                    "it a different substance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s03",
        "band": "standard",
        "text": "One of these is true of the formula CO₂ but not of the "
                "formula NaCl. Which one?",
        "options": [
            {"text": "It gives the proportion of one element to the other in "
                     "the substance.",
             "correct": False,
             "why": "True of both. Giving the proportion is the thing a "
                    "formula always does — for salt it is the only thing it "
                    "does."},
            {"text": "It names which elements the substance is made of.",
             "correct": False,
             "why": "True of both. Every formula names its elements; that is "
                    "not where the molecule and the giant structure part "
                    "company."},
            {"text": "It tells you how much of the substance is present.",
             "correct": False,
             "why": "True of neither. No formula carries an amount — that is "
                    "the job of a big number written in front."},
            {"text": "It counts the atoms in one particle of the substance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s04",
        "band": "standard",
        "text": "One beaker holds 20 cm³ of water and another holds 500 cm³. "
                "What is the formula of the water in the bigger beaker?",
        "options": [
            {"text": "H₄O₂, because twice as much water needs twice as many "
                     "atoms written into the formula.",
             "correct": False,
             "why": "Doubling the small numbers would change what the "
                    "substance is, not how much of it there is — and H₄O₂ is "
                    "not a substance at all."},
            {"text": "H₂O, the same as the small beaker — a formula says "
                     "what, not how much.",
             "correct": True},
            {"text": "25H₂O, because there is twenty-five times as much in "
                     "it.",
             "correct": False,
             "why": "A big number counts individual particles, and even a "
                    "drop holds billions of them. An amount you can measure "
                    "in cm³ never goes into a formula."},
            {"text": "It has no formula until you say how much water there "
                     "is.",
             "correct": False,
             "why": "The formula belongs to the substance, not to the sample. "
                    "Every drop of water anywhere is H₂O."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c2-05-h01",
        "band": "harder",
        "text": "In principle you could pick one particle of carbon dioxide "
                "out of the air, but you could not pick one particle of salt "
                "out of a grain. Why not?",
        "options": [
            {"text": "A salt particle is far too small to be picked out one "
                     "at a time.",
             "correct": False,
             "why": "Size is not the problem — a carbon dioxide particle is "
                    "smaller still. The problem is that there is no single "
                    "salt particle there to pick."},
            {"text": "A grain of salt is one repeating stack of atoms, with "
                     "no separate particles.",
             "correct": True},
            {"text": "Salt particles are stuck to one another and only come "
                     "apart in water.",
             "correct": False,
             "why": "Water does break the stack up, but not into NaCl "
                    "particles — the grain was never built out of them in the "
                    "first place."},
            {"text": "A salt particle holds one sodium and one chlorine that "
                     "cannot be separated at all.",
             "correct": False,
             "why": "That is the molecule picture again. NaCl is a ratio "
                    "running through a stack, not a count of what is inside "
                    "one particle."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h02",
        "band": "harder",
        "text": "Asked to write six particles of water, a student writes "
                "H₁₂O₆. What has gone wrong?",
        "options": [
            {"text": "Nothing — twelve hydrogens and six oxygens is what six "
                     "particles of water come to altogether.",
             "correct": False,
             "why": "The atoms do total the same, and that is exactly the "
                    "trap. Totalling them cannot tell six ordinary particles "
                    "apart from one particle six times the size."},
            {"text": "The two numbers are the wrong way round; it should read "
                     "H₆O₁₂.",
             "correct": False,
             "why": "Swapping them just counts different numbers of each "
                    "element, and it still describes one particle rather than "
                    "six."},
            {"text": "Each element needs its own six, so it should read "
                     "6H₂6O.",
             "correct": False,
             "why": "One number at the front already multiplies the whole "
                    "particle and everything inside it. Repeating it is not "
                    "needed and is not how formulae are written."},
            {"text": "Six particles is 6H₂O; H₁₂O₆ would be one particle six "
                     "times the size.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h03",
        "band": "harder",
        "text": "Glucose is C₆H₁₂O₆ and ethanoic acid is C₂H₄O₂. Divide each "
                "down and both reach one carbon to two hydrogens to one "
                "oxygen. What does that tell you?",
        "options": [
            {"text": "Proportions alone do not fix a substance — the atoms "
                     "in each particle matter too.",
             "correct": True},
            {"text": "They are really the same substance, written two "
                     "different ways.",
             "correct": False,
             "why": "One is sugar and the other is vinegar. Sharing a "
                    "proportion is not the same as being the same substance."},
            {"text": "One of the two formulae must have been copied down "
                     "wrongly, since both cannot be right.",
             "correct": False,
             "why": "Both are correct as written. Two different substances "
                    "are perfectly free to share the same ratio of elements."},
            {"text": "Glucose is six times as concentrated as ethanoic acid.",
             "correct": False,
             "why": "The numbers count atoms inside one particle, never how "
                    "much of the substance you have. Concentration is not in "
                    "a formula at all."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h04",
        "band": "harder",
        "text": "Hydrogen peroxide breaks down into water and oxygen. A "
                "student says that proves it was a mixture of the two all "
                "along. Why are they wrong?",
        "options": [
            {"text": "A mixture would have broken down far faster than "
                     "hydrogen peroxide does.",
             "correct": False,
             "why": "How fast something breaks down is not the test. The test "
                    "is whether the atoms are joined inside each particle, "
                    "and in peroxide they are."},
            {"text": "Water and oxygen cannot be mixed together in the first "
                     "place.",
             "correct": False,
             "why": "They can be mixed — but that mixture is not hydrogen "
                    "peroxide, because in peroxide the second oxygen is "
                    "joined into every particle."},
            {"text": "Its particles are two hydrogens joined to two oxygens: "
                     "a reaction, not a separation.",
             "correct": True},
            {"text": "It was a mixture all right, but of hydrogen and oxygen "
                     "rather than water and oxygen.",
             "correct": False,
             "why": "Nothing loose is in there. Each particle is H₂O₂, with "
                    "all four atoms joined, and the hydrogen and oxygen only "
                    "appear once a reaction has happened."},
        ],
        "figure": None,
    },
]
