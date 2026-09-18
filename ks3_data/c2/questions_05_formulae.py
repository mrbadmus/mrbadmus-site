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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-05-e05",
        "band": "easier",
        "text": "What is a molecule?",
        "options": [
            {"text": "A small group of atoms joined together, existing as a "
                     "separate particle",
             "correct": True},
            {"text": "Any group of billions of atoms locked into one "
                     "repeating stack that carries on in every direction",
             "correct": False,
             "why": "That is a giant structure, like salt. A molecule is "
                    "small and separate"},
            {"text": "The smallest particle of an element",
             "correct": False,
             "why": "That is an atom. A molecule is usually several atoms "
                    "joined"},
            {"text": "Any particle too small to be seen with a microscope",
             "correct": False,
             "why": "Atoms are too small to see and are not molecules. Size "
                    "is not the definition"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e06",
        "band": "easier",
        "text": "What is a giant structure?",
        "options": [
            {"text": "A substance whose particles are unusually large and "
                     "heavy",
             "correct": False,
             "why": "Nothing here is about a particle being large. There are "
                    "no separate particles in it at all"},
            {"text": "Billions of atoms locked into one repeating stack, with "
                     "no separate particles in it",
             "correct": True},
            {"text": "A single very big molecule floating on its own",
             "correct": False,
             "why": "A giant structure is not one molecule. It is a stack "
                    "with no separate pieces in it"},
            {"text": "A pile of grains of a solid, each grain made of many "
                     "particles",
             "correct": False,
             "why": "A pile of grains is a pile. The word describes what is "
                    "inside ONE grain"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e07",
        "band": "easier",
        "text": "Which of these is made of separate molecules rather than a "
                "giant structure?",
        "options": [
            {"text": "Table salt, NaCl, where every sodium is surrounded by "
                     "chlorines and every chlorine by sodiums",
             "correct": False,
             "why": "That description is a giant structure. There is no "
                    "particle in it holding one of each"},
            {"text": "A grain of sand",
             "correct": False,
             "why": "Sand is a giant structure too — a repeating stack, not "
                    "separate particles"},
            {"text": "Carbon dioxide, CO₂",
             "correct": True},
            {"text": "A copper wire",
             "correct": False,
             "why": "Copper is a stack of atoms all the way through. Nothing "
                    "in it is a separate particle"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e08",
        "band": "easier",
        "text": "What does the word ratio mean?",
        "options": [
            {"text": "The total number of atoms that a formula names when all "
                     "its small numbers have been added up together",
             "correct": False,
             "why": "That is a total, not a ratio. A ratio compares two "
                    "counts rather than adding them"},
            {"text": "How much of a substance you have in grams",
             "correct": False,
             "why": "That is a mass. A ratio has no units and does not depend "
                    "on how much you have"},
            {"text": "The order in which the symbols are written",
             "correct": False,
             "why": "Order is a convention. A ratio is about numbers of "
                    "atoms"},
            {"text": "How many of one thing there are for every one of "
                     "another",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c2-05-s05",
        "band": "standard",
        "text": "Ammonia has the formula NH₃. How many atoms are in one "
                "particle, and how many different elements?",
        "options": [
            {"text": "Four atoms and two elements",
             "correct": True},
            {"text": "Three atoms and two elements, since the small 3 gives "
                     "the total number of atoms in the whole particle",
             "correct": False,
             "why": "The 3 counts hydrogen atoms only. Add the nitrogen and "
                    "the total is four"},
            {"text": "Four atoms and four elements",
             "correct": False,
             "why": "Count the capitals for elements: N and H, so two. The "
                    "hydrogens are three atoms of one element"},
            {"text": "Two atoms and two elements",
             "correct": False,
             "why": "That ignores the small 3 altogether. It is a count of "
                    "hydrogen atoms and has to be used"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s06",
        "band": "standard",
        "text": "Methane, the gas burnt in a cooker, is CH₄. Which statement "
                "about the small 4 is right?",
        "options": [
            {"text": "It says there is four times as much methane as there "
                     "would otherwise be",
             "correct": False,
             "why": "A small number never counts how much you have. It counts "
                    "atoms inside one particle"},
            {"text": "It counts the hydrogen atoms in one particle, and "
                     "changing it would give a different substance",
             "correct": True},
            {"text": "It counts the atoms of both elements added together",
             "correct": False,
             "why": "A small number belongs to the symbol it follows. Only "
                    "the hydrogens are counted by it"},
            {"text": "It says the methane must be handled in fours",
             "correct": False,
             "why": "Nothing in a formula is an instruction. It is a "
                    "description of one particle"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s07",
        "band": "standard",
        "text": "Sulfuric acid is H₂SO₄. A student says the S must really "
                "have an invisible 1 after it. Are they right?",
        "options": [
            {"text": "No — a symbol with nothing after it can mean any number "
                     "of atoms, and only the reaction settles which",
             "correct": False,
             "why": "It always means exactly one. Nothing about a reaction "
                    "changes what a formula says"},
            {"text": "Yes, and it should be written in, because leaving it "
                     "out makes the formula ambiguous",
             "correct": False,
             "why": "The meaning is not ambiguous at all. Chemists agree that "
                    "no number means one"},
            {"text": "Yes about the meaning — it is one sulfur atom — but a 1 "
                     "is never written",
             "correct": True},
            {"text": "No — a symbol with no number after it means the element "
                     "is present in traces",
             "correct": False,
             "why": "There is no such thing as a trace in a formula. It means "
                    "exactly one atom"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s08",
        "band": "standard",
        "text": "A grain of salt is ground into a fine powder. What happens "
                "to its formula?",
        "options": [
            {"text": "It becomes Na₂Cl₂, because the grinding has broken the "
                     "stack into pieces that hold two of each",
             "correct": False,
             "why": "Grinding breaks a grain into smaller grains, each still "
                    "a stack. Nothing about the ratio changes"},
            {"text": "It stops having one, because a powder is a mixture",
             "correct": False,
             "why": "Grinding does not mix anything. Every speck is still "
                    "sodium chloride"},
            {"text": "It gains a big number in front to show how many grains "
                     "there are",
             "correct": False,
             "why": "A big number counts particles in an equation, not grains "
                    "in a dish"},
            {"text": "Nothing — it is still NaCl",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-05-h05",
        "band": "harder",
        "text": "Rust is Fe₂O₃. What is the ratio of iron atoms to oxygen "
                "atoms, and does a bigger lump change it?",
        "options": [
            {"text": "Two iron to three oxygen, and a bigger lump does not "
                     "change it",
             "correct": True},
            {"text": "Two iron to three oxygen in a small lump, and more "
                     "oxygen in a large one because the outside has been "
                     "exposed to the air for longer",
             "correct": False,
             "why": "The ratio is a property of the substance. Anything with "
                    "a different ratio would be a different substance"},
            {"text": "Three iron to two oxygen, unchanged by the size",
             "correct": False,
             "why": "The right idea about size, but the numbers are the wrong "
                    "way round. The small number follows the symbol it "
                    "counts"},
            {"text": "Five to one, since there are five atoms in the formula",
             "correct": False,
             "why": "Five is the total number of atoms, not a ratio. A ratio "
                    "compares the two counts"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h06",
        "band": "harder",
        "text": "A student says 2CO and CO₂ must be the same thing, because "
                "each of them has a 2 and the letters C and O. What is "
                "actually in each?",
        "options": [
            {"text": "2CO is one carbon and two oxygens; CO₂ is two carbons "
                     "and one oxygen, so the two are the same atoms written "
                     "in the opposite order",
             "correct": False,
             "why": "A big number in front multiplies the WHOLE formula, and "
                    "a small number counts only the symbol before it"},
            {"text": "2CO is two carbons and two oxygens in two particles; "
                     "CO₂ is one carbon and two oxygens in one",
             "correct": True},
            {"text": "Both are two carbons and two oxygens, so the student is "
                     "right",
             "correct": False,
             "why": "CO₂ has only one carbon. Doubling CO gives two of "
                    "each"},
            {"text": "2CO is a mixture of carbon and oxygen; CO₂ is a "
                     "compound",
             "correct": False,
             "why": "Both are compounds. The big number counts particles of a "
                    "compound, not a mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h07",
        "band": "harder",
        "text": "Copper sulfate is CuSO₄. A student reads it as four "
                "elements: copper, sulfur, oxygen and “four”. Correct them.",
        "options": [
            {"text": "Three elements and six atoms, since the 4 also counts "
                     "the sulfur that is written immediately in front of it",
             "correct": False,
             "why": "A small number counts only the symbol directly before "
                    "it, which is the O. There is one sulfur"},
            {"text": "Four elements and six atoms, because the 4 is a count "
                     "and a count is a fourth thing in the formula",
             "correct": False,
             "why": "A count is not an element. Only capital letters start "
                    "elements, and there are three"},
            {"text": "Three elements and six atoms — the 4 counts oxygen "
                     "atoms",
             "correct": True},
            {"text": "Three elements and three atoms, because a formula names "
                     "each element once",
             "correct": False,
             "why": "The small numbers have to be used. Three elements here "
                    "come to six atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h08",
        "band": "harder",
        "text": "Ethanol and dimethyl ether are both C₂H₆O, and they are "
                "completely different substances — one is in beer and the "
                "other is a gas. What does that show?",
        "options": [
            {"text": "That one of the two formulae must have been written "
                     "down wrongly",
             "correct": False,
             "why": "Both are right. Sharing a formula is exactly what makes "
                    "the pair worth knowing about"},
            {"text": "That one of them must be a mixture rather than a "
                     "compound",
             "correct": False,
             "why": "Both are compounds with a fixed formula. Neither is a "
                    "mixture"},
            {"text": "That the atoms must be different sizes in the two "
                     "substances",
             "correct": False,
             "why": "A carbon atom is a carbon atom in both. What differs is "
                    "which atom is joined to which"},
            {"text": "That a formula does not fix a substance on its own — "
                     "how the atoms are joined matters too",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    # ⚠️ FORMULAE ARE WRITTEN FLAT IN THE ROWS BELOW — CO2, not CO₂ — per the
    # MRB-338 authoring contract and CLAUDE.md's MRB-302 store-flat ruling.
    # The rows above (MRB-269 and the MRB-335 top-up) use Unicode subscripts,
    # so this leaf now carries both conventions. Reported to the commander
    # rather than resolved here: the shipped rows are frozen and may not be
    # edited, and a mixed file is the only append-only outcome available.
    {
        "id": "c2-05-e09",
        "band": "easier",
        "text": "Sulfur dioxide has the formula SO2. What is the small 2 "
                "counting?",
        "options": [
            {"text": "The oxygen atoms inside one particle of it.",
             "correct": True},
            {"text": "The particles of sulfur dioxide that are there.",
             "correct": False,
             "why": "Particles are counted by a big number written in front, "
                    "as in 2SO2. A small number sits inside one particle."},
            {"text": "The sulfur atoms in it.",
             "correct": False,
             "why": "A small number belongs to the symbol it follows, and that "
                    "symbol is O. The S has no number, so there is one sulfur."},
            {"text": "The elements in it, since two are named by a 2.",
             "correct": False,
             "why": "Two elements here is a coincidence. SO3 also holds two "
                    "elements, and its small number is a 3."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e10",
        "band": "easier",
        "text": "Magnesium oxide is MgO, and neither symbol has a number "
                "written after it. How many atoms of each does one particle "
                "hold?",
        "options": [
            {"text": "Two of each: a bare symbol stands for a pair",
             "correct": False,
             "why": "A symbol on its own stands for one atom. Two of each "
                    "would have to be written Mg2O2."},
            {"text": "None of either, since an unnumbered symbol counts nothing",
             "correct": False,
             "why": "The formula is complete as it stands. Chemists leave the "
                    "1 out because a bare symbol already means one."},
            {"text": "One magnesium atom and one oxygen atom",
             "correct": True},
            {"text": "It cannot be worked out from this formula",
             "correct": False,
             "why": "It can, and this is how every formula is read. No number "
                    "after a symbol means exactly one atom of it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e11",
        "band": "easier",
        "text": "A student writes 5CO2 at the top of a page of working. What "
                "is the 5 counting?",
        "options": [
            {"text": "The carbon atoms, which a front number always counts",
             "correct": False,
             "why": "The carbon has no small number, so there is one of it. "
                    "The 5 is not inside the particle at all."},
            {"text": "Particles of carbon dioxide",
             "correct": True},
            {"text": "The oxygen atoms in each particle",
             "correct": False,
             "why": "The oxygen atoms are counted by the small 2 after the O. "
                    "A big number in front counts whole particles."},
            {"text": "The elements it is built from",
             "correct": False,
             "why": "Carbon dioxide is built from two elements, whatever "
                    "number stands in front of it. The 5 counts particles."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e12",
        "band": "easier",
        "text": "A student changes a formula from SO2 to SO3. Both are real "
                "substances. Has the amount changed, or what the substance is?",
        "options": [
            {"text": "The amount: SO3 is more of the gas",
             "correct": False,
             "why": "No small number reports an amount. Changing one changes "
                    "what is inside every particle."},
            {"text": "Neither: both name one substance",
             "correct": False,
             "why": "They name two substances. A particle holding three "
                    "oxygens is not a particle holding two."},
            {"text": "Both at once",
             "correct": False,
             "why": "Half of this is right — the substance has changed. The "
                    "amount is not in a formula to be changed."},
            {"text": "What the substance is: SO3 is not sulfur dioxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e13",
        "band": "easier",
        "text": "What does the word particle mean?",
        "options": [
            {"text": "The smallest separate piece of a substance",
             "correct": True},
            {"text": "Any piece of a substance small enough to be a speck of "
                     "dust",
             "correct": False,
             "why": "A speck of dust is enormous next to a particle, and it "
                    "holds billions of them."},
            {"text": "The smallest piece an element can possibly be cut into",
             "correct": False,
             "why": "That is an atom. A particle of water is three atoms "
                    "joined."},
            {"text": "A group of atoms taken from two or more elements",
             "correct": False,
             "why": "A particle can be built from one element, and being made "
                    "of two is no part of what the word means."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e14",
        "band": "easier",
        "text": "Calcium chloride is CaCl2. How many chlorine atoms does the "
                "formula show for every one calcium?",
        "options": [
            {"text": "One",
             "correct": False,
             "why": "The Cl carries a small 2, and that 2 counts chlorine "
                    "atoms."},
            {"text": "Two",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is every atom in the formula added up. The "
                    "question asks for chlorine on its own."},
            {"text": "Four",
             "correct": False,
             "why": "Four would need the formula CaCl4. The number written "
                    "is 2."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e15",
        "band": "easier",
        "text": "Count the atoms in a single particle of hydrogen peroxide, "
                "H2O2. What is the total?",
        "options": [
            {"text": "Two",
             "correct": False,
             "why": "Two is the hydrogen count on its own. The oxygens are "
                    "still to be added."},
            {"text": "Three",
             "correct": False,
             "why": "Three atoms is a particle of water. Peroxide carries one "
                    "oxygen more than that."},
            {"text": "Four",
             "correct": True},
            {"text": "Six",
             "correct": False,
             "why": "Six would need H3O3. Both of the small numbers written "
                    "here are 2."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e16",
        "band": "easier",
        "text": "Nitrogen monoxide is NO and nitrogen dioxide is NO2. Which "
                "holds more oxygen in each particle, and by how much?",
        "options": [
            {"text": "Nitrogen dioxide, by one oxygen atom in every particle",
             "correct": True},
            {"text": "Nitrogen monoxide",
             "correct": False,
             "why": "Monoxide is the one with the single oxygen, and its "
                    "formula shows no small number at all."},
            {"text": "Nitrogen dioxide, by twice as much gas",
             "correct": False,
             "why": "A small number changes what sits inside each particle, "
                    "never how much of the gas you have."},
            {"text": "Neither, since both formulae name the same gas",
             "correct": False,
             "why": "One oxygen atom per particle is the whole difference "
                    "between two substances that behave nothing alike."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e17",
        "band": "easier",
        "text": "In the formula Na2S, which symbol does the small 2 belong "
                "to?",
        "options": [
            {"text": "To the S",
             "correct": False,
             "why": "A small number is written after the symbol it counts, "
                    "and this one comes before the S."},
            {"text": "To both, because one number covers a whole formula",
             "correct": False,
             "why": "One small number counts one element. Two of each would "
                    "be written Na2S2."},
            {"text": "To neither, since it counts particles",
             "correct": False,
             "why": "A number that counts particles is written in front of "
                    "the whole formula, never tucked inside it."},
            {"text": "To the Na, giving two sodium atoms",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e18",
        "band": "easier",
        "text": "Propane, the gas burnt in a camping stove, is C3H8. State "
                "the number of hydrogen atoms in one particle.",
        "options": [
            {"text": "Three",
             "correct": False,
             "why": "Three is the carbon count. The hydrogen's number is the "
                    "one written after the H."},
            {"text": "Eight",
             "correct": True},
            {"text": "Eleven",
             "correct": False,
             "why": "Eleven is every atom in the particle added up, and the "
                    "question asks for hydrogen alone."},
            {"text": "Twenty-four",
             "correct": False,
             "why": "Multiplying the two small numbers means nothing. Each "
                    "one counts its own element and no other."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e19",
        "band": "easier",
        "text": "Is every formula that somebody can write down a real "
                "substance?",
        "options": [
            {"text": "Yes, since real atoms will join in any numbers you ask for",
             "correct": False,
             "why": "Real elements are not enough. Hydrogen and oxygen are "
                    "both real and H3O2 is still nothing."},
            {"text": "Yes, though a few of them have yet to be discovered",
             "correct": False,
             "why": "Those substances are not waiting to be found. Atoms "
                    "cannot join in those numbers, so they do not exist."},
            {"text": "No — most combinations of atoms are not substances",
             "correct": True},
            {"text": "No, because a formula of two elements is the limit",
             "correct": False,
             "why": "Formulae naming three and four elements are ordinary. "
                    "What limits them is which numbers can bond."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e20",
        "band": "easier",
        "text": "Which of these changes would alter what a substance IS, "
                "rather than how much of it you have?",
        "options": [
            {"text": "Changing a small number written after a symbol",
             "correct": True},
            {"text": "Writing a number in front",
             "correct": False,
             "why": "A number in front counts particles, so it changes the "
                    "amount and leaves the substance alone."},
            {"text": "Pouring it into a larger container",
             "correct": False,
             "why": "A container holds a substance; it does not reach inside "
                    "the particles to change one."},
            {"text": "Drawing its particles further apart",
             "correct": False,
             "why": "How a drawing is spaced out is a drawing decision. The "
                    "particles themselves are unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e21",
        "band": "easier",
        "text": "A formula names the elements in a substance and counts the "
                "atoms of each. Which of these can it NOT tell you?",
        "options": [
            {"text": "Which elements the substance is built from",
             "correct": False,
             "why": "That is the first thing a formula does. Every capital "
                    "letter in it starts an element."},
            {"text": "How many atoms of each element are in one particle",
             "correct": False,
             "why": "That is the job of the small numbers, and it is the "
                    "other half of what a formula is for."},
            {"text": "The proportion of one element to the next",
             "correct": False,
             "why": "A formula always gives the proportion — for a giant "
                    "structure that is the only thing it gives."},
            {"text": "How much of the substance you have",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e22",
        "band": "easier",
        "text": "Potassium oxide is K2O. How many potassium atoms are there "
                "for every oxygen atom?",
        "options": [
            {"text": "One",
             "correct": False,
             "why": "The O having no number fixes the oxygen at one. The "
                    "potassium is the element with the 2."},
            {"text": "Two",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is the total number of atoms. A ratio compares the "
                    "two counts instead of adding them up."},
            {"text": "It depends on the amount",
             "correct": False,
             "why": "A ratio belongs to the substance. A lorry-load of it is "
                    "two potassium for every oxygen as well."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e23",
        "band": "easier",
        "text": "Each particle of a substance holds two lithium atoms joined "
                "to one oxygen atom. How is its formula written?",
        "options": [
            {"text": "LiO2",
             "correct": False,
             "why": "This puts the 2 on the oxygen, so it says one lithium "
                    "and two oxygens — the wrong way round."},
            {"text": "Li2O2",
             "correct": False,
             "why": "This doubles the oxygen as well. Only the lithium was "
                    "described as coming in twos."},
            {"text": "Li2O",
             "correct": True},
            {"text": "2LiO",
             "correct": False,
             "why": "A number in front counts particles, so this says two "
                    "particles holding one of each."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e24",
        "band": "easier",
        "text": "Aluminium chloride is AlCl3. Which element has three atoms "
                "in each particle?",
        "options": [
            {"text": "Chlorine",
             "correct": True},
            {"text": "Aluminium",
             "correct": False,
             "why": "The Al has no number written after it, which fixes it "
                    "at one atom."},
            {"text": "Both of them",
             "correct": False,
             "why": "Three of each would read Al3Cl3. The 3 counts only the "
                    "symbol it follows."},
            {"text": "Neither: the 3 counts particles",
             "correct": False,
             "why": "It is written small and low, after a symbol, so it "
                    "counts atoms. Particle counts go in front."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e25",
        "band": "easier",
        "text": "A diamond is one repeating stack of carbon atoms, with "
                "nothing separate anywhere in it. Which word describes it?",
        "options": [
            {"text": "A mixture",
             "correct": False,
             "why": "A mixture holds more than one substance, loosely. This "
                    "is carbon bonded to carbon throughout."},
            {"text": "A molecule",
             "correct": False,
             "why": "A molecule is a small group of atoms you could pick out "
                    "on its own. Nothing here comes apart like that."},
            {"text": "A compound",
             "correct": False,
             "why": "A compound holds at least two elements joined. Diamond "
                    "is carbon and carbon only."},
            {"text": "A giant structure",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e26",
        "band": "easier",
        "text": "The formula Fe3O4 has two small numbers in it. What do both "
                "of them count?",
        "options": [
            {"text": "Particles: three of one kind and four of the other",
             "correct": False,
             "why": "Both numbers sit inside one formula, after a symbol. A "
                    "particle count is a single number out in front."},
            {"text": "Atoms, each of the element whose symbol it follows",
             "correct": True},
            {"text": "Elements: three of them before the O and four after it",
             "correct": False,
             "why": "The formula names two elements, iron and oxygen. What "
                    "the numbers count is atoms."},
            {"text": "Grams of iron and of oxygen",
             "correct": False,
             "why": "Nothing in a formula is a mass. The numbers count atoms, "
                    "whatever the sample weighs."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e27",
        "band": "easier",
        "text": "Hydrogen and oxygen can be written down in many "
                "combinations, and just two of them are substances. Which "
                "pair is real?",
        "options": [
            {"text": "HO and HO2",
             "correct": False,
             "why": "Neither is a substance. Hydrogen comes in twos in both "
                    "of the real ones."},
            {"text": "H3O and H3O2",
             "correct": False,
             "why": "Three hydrogens is one too many, and no bottle of either "
                    "of these exists anywhere."},
            {"text": "H2O and H2O2",
             "correct": True},
            {"text": "H2O and H3O",
             "correct": False,
             "why": "Water is right, and the second one is not. The other "
                    "real substance carries a second oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e28",
        "band": "easier",
        "text": "Asked what NaCl tells them, a student answers: one sodium "
                "atom for every chlorine atom. Is that right?",
        "options": [
            {"text": "Yes — a one-to-one ratio is exactly what it says",
             "correct": True},
            {"text": "No, one particle holds one of each",
             "correct": False,
             "why": "Salt has no separate particles to hold anything. The "
                    "ratio runs through a stack instead."},
            {"text": "No, it tells you how many grains are in a spoonful",
             "correct": False,
             "why": "A formula carries no amount of any kind, in grains or "
                    "in anything else."},
            {"text": "No, because a formula gives the element names and stops there",
             "correct": False,
             "why": "Naming the elements is half of the job. Counting them "
                    "against each other is the other half."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e29",
        "band": "easier",
        "text": "A substance has the formula CuCl2. Which element is there "
                "more of in each particle?",
        "options": [
            {"text": "Copper",
             "correct": False,
             "why": "Being written first counts nothing. The numbers decide "
                    "it, and the Cu has none."},
            {"text": "There is the same amount of each",
             "correct": False,
             "why": "Equal numbers would read CuCl. The small 2 puts the "
                    "chlorine ahead by one atom."},
            {"text": "It cannot be told from a formula",
             "correct": False,
             "why": "It is precisely what a formula is for. Read the small "
                    "numbers and compare them."},
            {"text": "Chlorine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-e30",
        "band": "easier",
        "text": "One sample of a pure substance is a lorry-load and another "
                "is a pinch. What must be true of the two formulae?",
        "options": [
            {"text": "The lorry-load's formula carries a big number in front",
             "correct": False,
             "why": "A number in front counts particles one at a time, and a "
                    "pinch already holds billions of them."},
            {"text": "They are the same formula",
             "correct": True},
            {"text": "The lorry-load's small numbers are larger",
             "correct": False,
             "why": "Larger small numbers would name a different substance "
                    "rather than a bigger heap of this one."},
            {"text": "The two formulae are not the same one",
             "correct": False,
             "why": "A formula belongs to the substance, not to the sample. "
                    "The pinch has the same one."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c2-05-s09",
        "band": "standard",
        "text": "A line of working reads 3H2O. How many atoms is that "
                "altogether?",
        "options": [
            {"text": "Nine",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is the number of particles. Each of them holds "
                    "three atoms of its own."},
            {"text": "Five",
             "correct": False,
             "why": "Five adds the 3 and the 2 together. The front number "
                    "multiplies the particle rather than joining it."},
            {"text": "Six",
             "correct": False,
             "why": "Six is the hydrogen atoms only. Each particle brings an "
                    "oxygen with it as well."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s10",
        "band": "standard",
        "text": "Two students describe what the formula MgCl2 shows. One says "
                "it shows one magnesium for every two chlorines; the other "
                "says it shows two magnesiums for every one chlorine. Who is "
                "right?",
        "options": [
            {"text": "The second, and what the first has described is MgCl",
             "correct": False,
             "why": "The second student has the ratio backwards — MgCl2 "
                    "gives one magnesium to two chlorines, not the reverse."},
            {"text": "The first, and the second has the ratio backwards",
             "correct": True},
            {"text": "Both, since the same atoms are named either way",
             "correct": False,
             "why": "The two descriptions give different ratios, and only "
                    "one of them matches what the small 2 says."},
            {"text": "Neither, since the small 2 counts magnesium atoms, not "
                     "chlorine atoms",
             "correct": False,
             "why": "The 2 sits after the Cl, so it counts chlorine atoms, "
                    "not magnesium ones."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s11",
        "band": "standard",
        "text": "Sodium and chlorine join one atom to one atom. Predict what "
                "you would get if you asked for Na2Cl3.",
        "options": [
            {"text": "Twice the sodium in an ordinary grain of salt",
             "correct": False,
             "why": "Small numbers are not a recipe you can dial up. Asking "
                    "for more sodium in the formula asks for a substance that "
                    "is not there."},
            {"text": "Salt, since those are the two elements salt is made of",
             "correct": False,
             "why": "The elements alone do not make the substance. Their "
                    "numbers have to be right as well, and salt is one to one."},
            {"text": "Nothing: no substance has that formula",
             "correct": True},
            {"text": "A stronger-tasting kind of salt than the usual one",
             "correct": False,
             "why": "Taste is a property of a real substance. There is no "
                    "substance here to taste."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s12",
        "band": "standard",
        "text": "Copper oxide is CuO. Explain why writing CuO2 instead would "
                "not simply mean more copper oxide.",
        "options": [
            {"text": "Because a small number reports an amount only when it "
                     "is larger than one",
             "correct": False,
             "why": "A small number never reports an amount, whatever its "
                    "size. It counts atoms inside a particle."},
            {"text": "Because the 2 would have to be written in front to "
                     "count anything",
             "correct": False,
             "why": "Written in front it would count particles. Written after "
                    "the O it changes the particle itself."},
            {"text": "Because it changes what is in each particle, so it "
                     "names another substance",
             "correct": True},
            {"text": "Because copper oxide is a giant structure and takes no "
                     "numbers",
             "correct": False,
             "why": "Giant structures take numbers too — their formulae give "
                    "a ratio, and a changed ratio is a changed substance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s13",
        "band": "standard",
        "text": "Sand is SiO2 and is one repeating stack; carbon dioxide is "
                "CO2 and is separate particles. Both formulae are one to two. "
                "What is different about what they mean?",
        "options": [
            {"text": "Nothing: one to two means the same in both",
             "correct": False,
             "why": "The proportion is shared, and what it describes is not. "
                    "Only one of the two has a particle to describe."},
            {"text": "For sand it is a ratio through the stack; for the gas "
                     "it is also the contents of one particle",
             "correct": True},
            {"text": "For sand the numbers count grains of it, and for the gas they "
                     "count particles, which is why only one of them is a "
                     "true formula",
             "correct": False,
             "why": "No formula counts grains. A grain holds billions of "
                    "atoms and the formula knows nothing of it."},
            {"text": "For sand the formula is a guess, since nobody can see "
                     "inside a grain",
             "correct": False,
             "why": "It is measured, not guessed. The ratio of silicon to "
                    "oxygen in sand is known exactly."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s14",
        "band": "standard",
        "text": "A bottle is labelled 4H2O2. State what the 4 is doing and "
                "what the two 2s are doing.",
        "options": [
            {"text": "All three numbers count atoms, so this is eight atoms "
                     "in one large particle",
             "correct": False,
             "why": "A number in front sits outside the particle. Totalling "
                    "all three treats it as though it were inside."},
            {"text": "The 4 makes the substance four times as concentrated as it "
                     "would be without it",
             "correct": False,
             "why": "Concentration needs something dissolved in something "
                    "else. The 4 is a count of whole particles."},
            {"text": "The 4 counts the elements, and each 2 counts particles of "
                     "the element it follows",
             "correct": False,
             "why": "Only two elements are named here, and particles are "
                    "never counted from inside a formula."},
            {"text": "The 4 counts particles; each 2 counts atoms of the "
                     "element it follows",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s15",
        "band": "standard",
        "text": "A student totals the atoms in 2CH4 and writes down ten. "
                "Determine whether they are right.",
        "options": [
            {"text": "No: it is five atoms",
             "correct": False,
             "why": "Five is one particle. The 2 in front says there are two "
                    "of them."},
            {"text": "No: it is seven atoms, the five in the particle plus the two "
                     "the front number adds on",
             "correct": False,
             "why": "Seven adds the 2 to the five atoms. A front number "
                    "multiplies the particle instead."},
            {"text": "Yes: two particles of five atoms each",
             "correct": True},
            {"text": "No: it is eight atoms",
             "correct": False,
             "why": "Eight doubles the hydrogens and forgets the carbons. "
                    "Everything inside the particle is doubled."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s16",
        "band": "standard",
        "text": "A student invents the formula CO3 for a new gas made of "
                "carbon and oxygen. Suggest why no bottle of it exists.",
        "options": [
            {"text": "Because carbon and oxygen have already been used up in "
                     "making CO and CO2, and an element can only be spent "
                     "once on one compound",
             "correct": False,
             "why": "Elements are not used up by the compounds they make. "
                    "There is plenty of both."},
            {"text": "Because the elements themselves fix how many atoms can "
                     "join, and three oxygens is not one of them",
             "correct": True},
            {"text": "Because a gas is never made of three of anything",
             "correct": False,
             "why": "Ammonia is a gas with three hydrogens in every particle. "
                    "Three is no barrier on its own."},
            {"text": "Because nobody has tried to make it yet",
             "correct": False,
             "why": "It is not an unexplored gap. Those atoms do not bond in "
                    "those numbers, so there is nothing to try for."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s17",
        "band": "standard",
        "text": "There is no single particle of salt anywhere in a grain. "
                "Explain how salt can have a formula at all.",
        "options": [
            {"text": "It is borrowed from salt water, where separate "
                     "particles do float about",
             "correct": False,
             "why": "Dissolved salt is not separate NaCl particles either, "
                    "and the formula was never taken from a solution."},
            {"text": "Chemists agree to pretend there is a particle, because "
                     "the formula is useful",
             "correct": False,
             "why": "Nothing is being pretended. The proportion the formula "
                    "gives is real and can be measured."},
            {"text": "The grain is small enough to count as one particle by "
                     "itself",
             "correct": False,
             "why": "A grain is billions of atoms. Its size is not what "
                    "decides whether a particle is there."},
            {"text": "Because a formula gives a proportion, and the stack has "
                     "one sodium for every chlorine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s18",
        "band": "standard",
        "text": "Copper forms two oxides, CuO and Cu2O. State the ratio of "
                "copper atoms to oxygen atoms in each.",
        "options": [
            {"text": "One to one, and two to one",
             "correct": True},
            {"text": "One to one, and one to two",
             "correct": False,
             "why": "The 2 in Cu2O follows the copper, so it is the copper "
                    "that comes in twos."},
            {"text": "Two to one, and one to one",
             "correct": False,
             "why": "The formulae are the right way round in your answer but "
                    "swapped between them. CuO is the one to one."},
            {"text": "One to one in both, since the formulae name the same "
                     "two elements",
             "correct": False,
             "why": "Naming the same elements is not having the same ratio. "
                    "That is why two different oxides exist."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s19",
        "band": "standard",
        "text": "A chemist needs to write down four particles of sulfur "
                "dioxide. Which is correct?",
        "options": [
            {"text": "S4O8",
             "correct": False,
             "why": "This is one particle with four sulfurs and eight "
                    "oxygens, which is not a substance at all."},
            {"text": "SO8",
             "correct": False,
             "why": "This multiplies the oxygen only and leaves the sulfur "
                    "alone. A count of particles covers everything."},
            {"text": "4SO2",
             "correct": True},
            {"text": "4S4O2",
             "correct": False,
             "why": "The 4 in front already covers the whole formula. "
                    "Repeating it inside multiplies the sulfur twice over."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s20",
        "band": "standard",
        "text": "A student says NaCl and Na2Cl2 must mean the same thing, "
                "since both are one to one. Explain which a chemist writes.",
        "options": [
            {"text": "Na2Cl2, because a formula must always show at least two "
                     "atoms of something in it",
             "correct": False,
             "why": "No such rule exists. Plenty of formulae, NaCl among "
                    "them, carry no small numbers at all."},
            {"text": "NaCl, because a giant structure's formula is written as "
                     "the simplest form of the ratio",
             "correct": True},
            {"text": "Na2Cl2, because a grain holds far more than one of each",
             "correct": False,
             "why": "A grain holds billions of each, so no small number could "
                    "ever report the true count anyway."},
            {"text": "Either one, depending on the size of the grain",
             "correct": False,
             "why": "The ratio does not shift with the size of a grain, and "
                    "only one form of it is written."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s21",
        "band": "standard",
        "text": "Methane is CH4 and ethane is C2H6. Determine which holds "
                "more atoms in one particle, and by how many.",
        "options": [
            {"text": "Ethane, by two, counting the extra carbon and the "
                     "hydrogens as one",
             "correct": False,
             "why": "Every atom is counted separately. Five against eight "
                    "leaves a difference of three."},
            {"text": "Methane, by one, since 4 is the larger small number "
                     "written in either formula",
             "correct": False,
             "why": "One number cannot be compared on its own. Both of a "
                    "formula's counts have to be added up."},
            {"text": "Neither: both hold the same, as both are made of carbon "
                     "and hydrogen only",
             "correct": False,
             "why": "Sharing two elements is not holding the same atoms. The "
                    "numbers differ, so the totals differ."},
            {"text": "Ethane, by three",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s22",
        "band": "standard",
        "text": "A syringe of carbon dioxide is sealed and squeezed into half "
                "the space. State what happens to the formula of the gas, and "
                "why.",
        "options": [
            {"text": "It doubles to C2O4, because the particles are twice as "
                     "close together and a formula reports how tightly packed "
                     "a gas is",
             "correct": False,
             "why": "Squeezing moves particles closer; it does not join them. "
                    "Each one is still one carbon and two oxygens."},
            {"text": "It gains a 2 in front, since the gas is twice as "
                     "concentrated as it was",
             "correct": False,
             "why": "A number in front counts particles, and squeezing makes "
                    "no new ones."},
            {"text": "Nothing happens to it: the formula says what the gas "
                     "is, and squeezing has not changed that",
             "correct": True},
            {"text": "It can no longer be written, because the gas is under "
                     "pressure",
             "correct": False,
             "why": "Pressure changes nothing about a formula. Carbon dioxide "
                    "is CO2 in a syringe as much as in the open air."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s23",
        "band": "standard",
        "text": "Sulfur trioxide is SO3 and sulfuric acid is H2SO4. State "
                "what the H2 adds, and whether the two are the same "
                "substance.",
        "options": [
            {"text": "Two hydrogen atoms; they are different substances",
             "correct": True},
            {"text": "Two hydrogen particles; they are the same substance "
                     "dissolved in water",
             "correct": False,
             "why": "The hydrogens are atoms joined inside the particle, not "
                    "separate particles mixed in."},
            {"text": "Two extra elements on top of the sulfur and the oxygen",
             "correct": False,
             "why": "H2 names one element twice over, not two. It is hydrogen "
                    "and hydrogen only."},
            {"text": "Two hydrogen atoms; they remain the same substance, "
                     "since the sulfur and oxygen are unchanged",
             "correct": False,
             "why": "The hydrogens and the extra oxygen are both inside every "
                    "particle, which makes it a different substance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s24",
        "band": "standard",
        "text": "Ethene is C2H4 and ethane is C2H6. Explain why they are not "
                "the same gas in two different amounts.",
        "options": [
            {"text": "Because a gas in a different amount would need a "
                     "different number in front of it",
             "correct": False,
             "why": "True about front numbers, and it is not the reason. The "
                    "difference here is inside the particle."},
            {"text": "Because two gases can never share a pair of elements "
                     "between them",
             "correct": False,
             "why": "They can, and often do. Carbon and hydrogen build a "
                    "great many different gases."},
            {"text": "Because ethene holds fewer atoms, so there is less of "
                     "it in the cylinder",
             "correct": False,
             "why": "How many atoms a particle holds says nothing about how "
                    "many particles a cylinder holds."},
            {"text": "Because the extra hydrogens are inside every particle, "
                     "so the substance itself is different",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s25",
        "band": "standard",
        "text": "Fool's gold is FeS2 and iron sulfide is FeS. State the ratio "
                "of iron to sulfur in each.",
        "options": [
            {"text": "One to two, and one to one",
             "correct": True},
            {"text": "Two to one, and one to one",
             "correct": False,
             "why": "The 2 follows the S in FeS2, so the sulfur is the "
                    "element that comes in twos."},
            {"text": "One to two in both, because both formulae hold the same "
                     "two elements as each other",
             "correct": False,
             "why": "Holding the same elements does not fix the ratio. FeS "
                    "carries no small number at all."},
            {"text": "Three to two, adding the atoms up",
             "correct": False,
             "why": "Adding the atoms gives a total. A ratio compares the two "
                    "counts against each other."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s26",
        "band": "standard",
        "text": "Nitrogen and oxygen form NO, NO2 and N2O, and all three are "
                "real. State what that shows.",
        "options": [
            {"text": "That any two elements at all can be combined in any numbers "
                     "you like",
             "correct": False,
             "why": "Three real formulae out of the many that could be "
                    "written is not any numbers at all."},
            {"text": "That nitrogen and oxygen are unusual, since a pair of "
                     "elements normally makes one substance",
             "correct": False,
             "why": "Several pairs behave this way. Carbon and oxygen give "
                    "both CO and CO2."},
            {"text": "That all three of them are really one substance written out "
                     "in three ways",
             "correct": False,
             "why": "Three formulae with different numbers describe three "
                    "different particles, so three substances."},
            {"text": "That two elements can join in more than one way, though "
                     "not in every way",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s27",
        "band": "standard",
        "text": "A student says 7CO2 must be a different substance from CO2, "
                "because the formula looks different. Explain the mistake.",
        "options": [
            {"text": "The 7 counts particles, so it is seven lots of the same "
                     "substance",
             "correct": True},
            {"text": "The 7 is not allowed there",
             "correct": False,
             "why": "It is perfectly allowed. A number in front is how "
                    "chemists write an amount of particles."},
            {"text": "The 7 makes it a mixture of seven gases",
             "correct": False,
             "why": "Every one of those particles is carbon dioxide, so "
                    "nothing is mixed with anything."},
            {"text": "The 7 makes each particle seven times the size, which is what "
                     "a number outside a formula does to it",
             "correct": False,
             "why": "A number in front multiplies how many particles there "
                    "are, and leaves each one as it was."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s28",
        "band": "standard",
        "text": "One particle of calcium oxide is CaO and one of calcium "
                "carbonate is CaCO3. How many more atoms does the second "
                "hold?",
        "options": [
            {"text": "Two",
             "correct": False,
             "why": "Two is the extra oxygens alone. The extra carbon has to "
                    "be counted as well."},
            {"text": "Three",
             "correct": True},
            {"text": "Four",
             "correct": False,
             "why": "Four is the second particle's atoms after the calcium is "
                    "removed, not the difference between the two."},
            {"text": "Five",
             "correct": False,
             "why": "Five is every atom in the second particle. The first "
                    "particle's two have still to be taken off."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s29",
        "band": "standard",
        "text": "A worksheet asks for the chlorine atoms in 3CaCl2. What is "
                "the answer?",
        "options": [
            {"text": "Six",
             "correct": True},
            {"text": "Two",
             "correct": False,
             "why": "Two is the chlorine in one particle. The 3 says there "
                    "are three of those particles."},
            {"text": "Three",
             "correct": False,
             "why": "Three is the number of particles, not the chlorine "
                    "atoms in them."},
            {"text": "Nine",
             "correct": False,
             "why": "Nine is every atom in the three particles. The question "
                    "asks for chlorine on its own."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-s30",
        "band": "standard",
        "text": "Ice, liquid water and steam are all water. Explain why one "
                "formula covers all three.",
        "options": [
            {"text": "Because a formula is written for the liquid, and the "
                     "other two borrow it",
             "correct": False,
             "why": "No state owns the formula. All three are built from the "
                    "same particles."},
            {"text": "Because steam and ice are too hard to analyse, so the "
                     "liquid's formula is used",
             "correct": False,
             "why": "Both can be analysed perfectly well, and both come back "
                    "as two hydrogens to one oxygen."},
            {"text": "Because the formula changes with temperature and "
                     "happens to land on H2O three times",
             "correct": False,
             "why": "A formula does not move with temperature at all. It "
                    "belongs to the substance."},
            {"text": "Because melting and boiling rearrange the particles "
                     "without changing what is inside one",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c2-05-h09",
        "band": "harder",
        "text": "Sodium chloride is NaCl and calcium chloride is CaCl2, and "
                "both are repeating stacks. Explain why only one of the two "
                "formulae carries a small number.",
        "options": [
            {"text": "Because calcium chloride's stack is the larger of the "
                     "two, so its formula needs the bigger numbers in it",
             "correct": False,
             "why": "Both stacks run on for billions of atoms. No formula "
                    "reports how big a stack is."},
            {"text": "Because the ratios differ: one sodium for every "
                     "chlorine, but one calcium for every two chlorines",
             "correct": True},
            {"text": "Because calcium chloride is a compound and sodium "
                     "chloride is an element",
             "correct": False,
             "why": "Both are compounds. Each of them names two different "
                    "elements in its formula."},
            {"text": "Because only calcium chloride has separate particles "
                     "to count",
             "correct": False,
             "why": "Neither has separate particles. Both formulae are "
                    "reporting a proportion through a stack."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h10",
        "band": "harder",
        "text": "A gas is analysed. Each of its particles holds three atoms, "
                "and there are twice as many oxygen atoms as carbon atoms. "
                "Determine its formula.",
        "options": [
            {"text": "C2O",
             "correct": False,
             "why": "This puts the 2 on the carbon, so it says twice as much "
                    "carbon as oxygen — the ratio the wrong way round."},
            {"text": "CO3",
             "correct": False,
             "why": "Three oxygens to one carbon is a ratio of three, and it "
                    "makes four atoms in the particle rather than three."},
            {"text": "C2O4",
             "correct": False,
             "why": "The ratio is right and the count is not. Six atoms is "
                    "twice the particle the question describes."},
            {"text": "CO2",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h11",
        "band": "harder",
        "text": "A student concludes that two substances with different "
                "formulae must contain different elements. Evaluate that "
                "conclusion.",
        "options": [
            {"text": "It is sound, since the elements are the only thing a "
                     "formula reports about a substance",
             "correct": False,
             "why": "A formula reports the counts as well, and the counts "
                    "alone are enough to make a second substance."},
            {"text": "It is wrong, but only where one of the two substances "
                     "is a giant structure",
             "correct": False,
             "why": "It fails for two ordinary gases. Giant structures have "
                    "nothing to do with why."},
            {"text": "It is sound for compounds and fails for elements",
             "correct": False,
             "why": "Carbon monoxide and carbon dioxide are both compounds, "
                    "and they break it between them."},
            {"text": "It is wrong: CO and CO2 name the same two elements in "
                     "different numbers",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h12",
        "band": "harder",
        "text": "A grain of salt is stirred into water until it vanishes, and "
                "the water is then dried off. Predict what the formula of the "
                "solid left behind will be.",
        "options": [
            {"text": "NaCl, because it is the same substance it was before it "
                     "was stirred in",
             "correct": True},
            {"text": "Na and Cl separately, since dissolving splits the two "
                     "elements apart from one another",
             "correct": False,
             "why": "Dissolving parts a stack; it does not part sodium from "
                    "chlorine. Neither element is left on its own."},
            {"text": "NaClH2O, since the water joins the stack while the salt "
                     "is dissolved in it",
             "correct": False,
             "why": "The water is driven off again and nothing of it stays. "
                    "Dissolving joins no atoms to anything."},
            {"text": "Na2Cl2, because the stack rebuilds itself in bigger "
                     "pieces as the water dries",
             "correct": False,
             "why": "However the stack rebuilds, its ratio is one to one, and "
                    "that is what the formula records."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h13",
        "band": "harder",
        "text": "A student argues that salt's formula is less useful than "
                "carbon dioxide's, because it gives only a ratio. Evaluate "
                "that argument.",
        "options": [
            {"text": "It is fair: a ratio is a rough description, and an "
                     "exact count would be better",
             "correct": False,
             "why": "The ratio is exact. One sodium for every chlorine is not "
                    "an approximation of anything."},
            {"text": "It is fair, since salt would have a proper formula if "
                     "anyone could see inside a grain",
             "correct": False,
             "why": "Seeing inside would show the stack, which is what the "
                    "formula already reports."},
            {"text": "It is unfair: a ratio is what there is to report, and "
                     "the formula reports it exactly",
             "correct": True},
            {"text": "It is unfair, because salt's formula counts the atoms "
                     "in one particle after all",
             "correct": False,
             "why": "There is no particle of salt for it to count. The "
                    "argument fails for a different reason than this."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h14",
        "band": "harder",
        "text": "A line of working reads 6CH4. Determine the number of "
                "hydrogen atoms and the number of atoms altogether.",
        "options": [
            {"text": "24 hydrogen atoms and 30 atoms altogether",
             "correct": True},
            {"text": "24 hydrogen atoms and 24 atoms altogether",
             "correct": False,
             "why": "The hydrogens are right. Six carbons still have to be "
                    "added to reach the total."},
            {"text": "4 hydrogen atoms and 10 atoms altogether",
             "correct": False,
             "why": "This multiplies nothing by the 6. A number in front "
                    "multiplies every atom in the particle."},
            {"text": "10 hydrogen atoms and 11 atoms altogether",
             "correct": False,
             "why": "Adding the 6 to the 4 treats the front number as one "
                    "more atom instead of a count of particles."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h15",
        "band": "harder",
        "text": "A new substance is one atom of X to three of Y. Two chemists "
                "propose XY3 and X2Y6. Determine what would settle which to "
                "write.",
        "options": [
            {"text": "Weighing a sample, since the heavier formula belongs to "
                     "the heavier substance",
             "correct": False,
             "why": "One substance cannot have two weights. Both formulae are "
                    "describing the same material."},
            {"text": "Whether its particles are separate, since a giant "
                     "structure is written as the simplest ratio",
             "correct": True},
            {"text": "Nothing: the two formulae say the same thing, so either "
                     "may be written",
             "correct": False,
             "why": "They share a ratio, and a molecule's formula must also "
                    "count what is in one particle."},
            {"text": "How much of it there is, since a larger sample takes "
                     "the larger numbers",
             "correct": False,
             "why": "No amount of a substance changes the numbers in its "
                    "formula."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h16",
        "band": "harder",
        "text": "Ammonia is NH3 and hydrazine is N2H4. A student says "
                "hydrazine must be two particles of ammonia with a hydrogen "
                "removed. Evaluate.",
        "options": [
            {"text": "Wrong: two particles of ammonia would be written 2NH3, "
                     "and hydrazine is one particle of its own",
             "correct": True},
            {"text": "Right: the atoms work out, since two ammonias minus one "
                     "hydrogen leave two nitrogens and five hydrogens",
             "correct": False,
             "why": "Two ammonias minus a hydrogen is five hydrogens, and "
                    "hydrazine has four. The arithmetic does not even land."},
            {"text": "Right, and 2NH3 and N2H4 are two ways of writing one "
                     "substance",
             "correct": False,
             "why": "One is two particles of ammonia and the other is a "
                    "single particle of a different substance."},
            {"text": "Wrong, because nitrogen and hydrogen make only one "
                     "compound between them",
             "correct": False,
             "why": "They make several, and both of these are real. The "
                    "mistake is about particles, not about which exist."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h17",
        "band": "harder",
        "text": "Carbon monoxide kills and carbon dioxide puts out fires, "
                "though both are built from carbon and oxygen only. State "
                "what a formula does not tell you.",
        "options": [
            {"text": "Which elements have been joined together",
             "correct": False,
             "why": "Naming the elements is the first thing a formula does, "
                    "and both of these name the same two."},
            {"text": "How the substance behaves",
             "correct": True},
            {"text": "How many atoms of each element are in a particle",
             "correct": False,
             "why": "Counting them is exactly what the small numbers are "
                    "for, and it is how these two are told apart."},
            {"text": "The proportion of one element to the other in it",
             "correct": False,
             "why": "A formula always gives the proportion. One to one and "
                    "one to two is the whole difference here."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h18",
        "band": "harder",
        "text": "A student asks how many particles there are in a 1 g sample "
                "of a substance, and is told to read the formula. Explain why "
                "that will not work.",
        "options": [
            {"text": "Because 1 g is too small a sample for a formula to "
                     "describe, and a larger one would answer it",
             "correct": False,
             "why": "Sample size is no part of it. A tonne could not be read "
                    "off a formula either."},
            {"text": "Because the formula would have to be weighed first, and "
                     "a formula cannot be put on a balance",
             "correct": False,
             "why": "Weighing the substance is a reasonable thing to do. What "
                    "cannot be done is reading a count out of the formula."},
            {"text": "Because a formula carries no amount at all — it says "
                     "what the substance is, not how much there is",
             "correct": True},
            {"text": "Because only a formula with a number in front of it "
                     "reports a count",
             "correct": False,
             "why": "A number in front counts particles one by one, and a "
                    "gram holds far more than anyone would write down."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h19",
        "band": "harder",
        "text": "Rust, Fe2O3, is a repeating stack of atoms. A student says "
                "the formula proves that each particle of rust holds five "
                "atoms. Evaluate.",
        "options": [
            {"text": "Wrong, and the total is three rather than five",
             "correct": False,
             "why": "Five is the right total for the formula. The mistake is "
                    "assuming there is a particle to total."},
            {"text": "Right about the five, and wrong to call rust a stack",
             "correct": False,
             "why": "Rust is a stack, and that is what makes the particle "
                    "claim fail."},
            {"text": "Right: any formula counts the atoms in one particle, and rust "
                     "is no different from a gas in that",
             "correct": False,
             "why": "For a giant structure there is no separate particle, so "
                    "the formula reports a ratio instead."},
            {"text": "Wrong: a stack has no separate particle, so the "
                     "formula gives two iron atoms for every three oxygens",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h20",
        "band": "harder",
        "text": "Determine the total number of atoms written down in 5Na2S.",
        "options": [
            {"text": "Eight",
             "correct": False,
             "why": "Eight adds the 5, the 2 and the sulfur together. The 5 "
                    "multiplies rather than adds."},
            {"text": "Ten",
             "correct": False,
             "why": "Ten is the sodium atoms alone. Each of the five "
                    "particles carries a sulfur as well."},
            {"text": "Fifteen",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is one particle. The 5 in front says there are "
                    "five of them."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h21",
        "band": "harder",
        "text": "An equation carries the term 12CO. Determine the atoms of "
                "each element that names, and state what CO12 would have been "
                "instead.",
        "options": [
            {"text": "12 carbon and 12 oxygen; CO12 would be one particle "
                     "holding a carbon and twelve oxygens",
             "correct": True},
            {"text": "12 carbon and 1 oxygen; CO12 would be the same thing "
                     "written the other way round",
             "correct": False,
             "why": "A front number multiplies everything after it, so both "
                    "elements are multiplied by twelve."},
            {"text": "1 carbon and 12 oxygen; CO12 would be twelve particles "
                     "of carbon monoxide",
             "correct": False,
             "why": "This is the two numbers swapped. In front the 12 counts "
                    "particles; after the O it counts oxygen atoms."},
            {"text": "24 atoms in one large particle; CO12 would name a "
                     "mixture of carbon and oxygen",
             "correct": False,
             "why": "12CO is twelve ordinary particles, not one large one, "
                    "and CO12 would be a compound rather than a mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h22",
        "band": "harder",
        "text": "Evaluate this claim: a formula tells you everything there is "
                "to know about a substance.",
        "options": [
            {"text": "True, provided the substance is a molecule rather than "
                     "a giant structure",
             "correct": False,
             "why": "Ethanol and dimethyl ether are both molecules and share "
                    "a formula, so it fails there too."},
            {"text": "True, since the elements named in it and the numbers beside "
                     "them are all there is to any substance",
             "correct": False,
             "why": "Two substances can share both and still differ, which "
                    "means there is something else."},
            {"text": "False: it never says how much there is, and it does not "
                     "say how the atoms are joined",
             "correct": True},
            {"text": "False, because a formula leaves out the elements that "
                     "are present in small amounts",
             "correct": False,
             "why": "A formula names every element in the substance. Nothing "
                    "is left out for being scarce."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h23",
        "band": "harder",
        "text": "Sand is SiO2 and carbon dioxide is CO2. A student says a "
                "spoonful of sand and a flask of the gas must hold the same "
                "number of atoms. Evaluate.",
        "options": [
            {"text": "Right, since the two formulae carry the same numbers as each "
                     "other and a number is a number wherever it is written",
             "correct": False,
             "why": "The numbers give a proportion within the substance. They "
                    "say nothing about how much of it is in the room."},
            {"text": "Wrong: a shared ratio says nothing at all about how "
                     "much of either substance there is",
             "correct": True},
            {"text": "Right, as long as the spoonful and the flask are the "
                     "same size",
             "correct": False,
             "why": "Equal volumes of a solid and a gas hold nothing like "
                    "equal numbers of atoms."},
            {"text": "Wrong, because the two formulae have different ratios "
                     "in them",
             "correct": False,
             "why": "Both are one to two. The conclusion fails for a "
                    "different reason than that."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h24",
        "band": "harder",
        "text": "Two labels read 2H2O2 and 4H2O. Determine which names more "
                "hydrogen atoms.",
        "options": [
            {"text": "2H2O2, by four hydrogen atoms",
             "correct": False,
             "why": "2H2O2 is four hydrogens and 4H2O is eight, so the "
                    "comparison runs the other way."},
            {"text": "They name the same number of hydrogen atoms",
             "correct": False,
             "why": "Four against eight. The front numbers have to be "
                    "multiplied through before anything is compared."},
            {"text": "4H2O, by four hydrogen atoms",
             "correct": True},
            {"text": "2H2O2, because each of its particles holds more atoms "
                     "in total than a particle of water does",
             "correct": False,
             "why": "Its particles are bigger and there are half as many of "
                    "them, which leaves fewer hydrogens altogether."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h25",
        "band": "harder",
        "text": "A student says a small number would not be written unless it "
                "were bigger than one. Evaluate that, using carbon monoxide, "
                "CO.",
        "options": [
            {"text": "Right: CO is the exception that chemists allow, and "
                     "every other formula carries its numbers",
             "correct": False,
             "why": "CO is no exception. Any symbol standing on its own, in "
                    "any formula, means one atom."},
            {"text": "Wrong: a 1 is never written, so CO is one carbon and "
                     "one oxygen",
             "correct": True},
            {"text": "Wrong, because CO really does carry two small 1s that "
                     "are printed too faintly to see",
             "correct": False,
             "why": "There is nothing there to see. The convention is that "
                    "the 1 is left out altogether."},
            {"text": "Right, and CO therefore holds an unknown number of "
                     "atoms of each element",
             "correct": False,
             "why": "Nothing about CO is unknown. It is exactly one atom of "
                    "each, and that is why no number is needed."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h26",
        "band": "harder",
        "text": "A compound's particles each hold five atoms, and there are "
                "four times as many chlorine atoms as carbon atoms. Determine "
                "its formula.",
        "options": [
            {"text": "C4Cl",
             "correct": False,
             "why": "This has four carbons to one chlorine, which is the "
                    "ratio the wrong way round."},
            {"text": "CCl5",
             "correct": False,
             "why": "Five chlorines to one carbon makes six atoms, and the "
                    "ratio is five rather than four."},
            {"text": "C2Cl8",
             "correct": False,
             "why": "The ratio is right and the particle is twice the size "
                    "the question describes."},
            {"text": "CCl4",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h27",
        "band": "harder",
        "text": "A student says any substance whose formula carries a small "
                "number must be made of molecules. Evaluate, using calcium "
                "chloride, CaCl2.",
        "options": [
            {"text": "Right, since a number that counts atoms in a particle "
                     "shows there is a particle there to count",
             "correct": False,
             "why": "In a stack the same number is reporting a ratio, and no "
                    "particle is implied by it."},
            {"text": "Right, and calcium chloride is therefore made of "
                     "separate particles holding three atoms",
             "correct": False,
             "why": "Calcium chloride is a stack. There is no three-atom "
                    "particle anywhere in it."},
            {"text": "Wrong, because CaCl2 carries no small number in it",
             "correct": False,
             "why": "It carries a 2 after the chlorine. The claim fails on "
                    "what that 2 means, not on whether it is there."},
            {"text": "Wrong: CaCl2 is a repeating stack, and its 2 reports a "
                     "ratio rather than a particle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h28",
        "band": "harder",
        "text": "Most of the formulae anyone could write down are not "
                "substances. A student says that makes chemistry mostly "
                "guesswork. Evaluate.",
        "options": [
            {"text": "Fair, since a chemist can do no better than try "
                     "combinations and see which of them work",
             "correct": False,
             "why": "Which combinations bond is understood and predictable, "
                    "not a matter of trying every one in turn."},
            {"text": "Unfair: which combinations exist is fixed by the "
                     "elements, so it is a rule rather than a guess",
             "correct": True},
            {"text": "Fair, because the substances that do exist were all "
                     "found by accident",
             "correct": False,
             "why": "Many were made on purpose, from what was already known "
                    "about how the elements join."},
            {"text": "Unfair, because every formula that can be written turns "
                     "out to be a substance somewhere",
             "correct": False,
             "why": "Most of them are not substances anywhere. That is the "
                    "fact the student started from, and it is true."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h29",
        "band": "harder",
        "text": "Suggest why chemists count atoms with a number written small "
                "and low, rather than with a full-sized number.",
        "options": [
            {"text": "So that it cannot be confused with the number in front, "
                     "which counts whole particles",
             "correct": True},
            {"text": "So that a formula takes up less room on the page",
             "correct": False,
             "why": "A small number saves almost nothing. What it saves is "
                    "the confusion with a particle count."},
            {"text": "Because a small number stands for a small quantity of "
                     "the substance",
             "correct": False,
             "why": "It stands for a count of atoms, and there is no small "
                    "quantity of anything in a formula."},
            {"text": "Because the atoms it counts are smaller than the "
                     "particles the other number counts",
             "correct": False,
             "why": "How a number is printed has nothing to do with the size "
                    "of what it counts."},
        ],
        "figure": None,
    },
    {
        "id": "c2-05-h30",
        "band": "harder",
        "text": "H2O and H2O2 are both real. A student says HO must exist "
                "too, halfway between them. Evaluate.",
        "options": [
            {"text": "Right, and HO is simply too unstable to keep in a "
                     "bottle for long",
             "correct": False,
             "why": "It is not a matter of a substance that spoils. Those "
                    "atoms do not bond in those numbers."},
            {"text": "Right, since anything written between two real formulae must "
                     "itself be a real substance somewhere",
             "correct": False,
             "why": "There is no halfway rule of that kind. Formulae are not "
                    "spaced out along a line."},
            {"text": "Wrong: two real formulae do not make everything "
                     "between them real, and no substance is HO",
             "correct": True},
            {"text": "Wrong, because HO holds fewer atoms than any real "
                     "substance does",
             "correct": False,
             "why": "Two-atom substances are ordinary — carbon monoxide is "
                    "one. HO fails on which atoms, not how many."},
        ],
        "figure": None,
    },
]
