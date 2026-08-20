"""C4 lesson 05 — Symbol equations and balancing: twelve questions (MRB-246).

The lesson has one rule and one trap. The rule is that a symbol equation says
which substances react and how many particles of each, and that only the
numbers in FRONT of a formula may be changed. The trap is that the arithmetic
can be made to agree around the wrong substance, which is what the forbidden
move on the page lets a student do on purpose. These twelve probe the angles
the mastery ladder leaves alone: what a number in front actually MEANS when it
multiplies a whole formula, what "balanced" does and does not prove, and the
rule carried into places the lesson does not visit.

The distractors are built from the lesson's two declared misconceptions.
`REACT-08` (an equation can be balanced by changing the small numbers in a
formula) drives the wrong options in e01, e03, s01, s04 and h02 — each of them
treats a subscript as if it were a count of particles, which is the move
`#s-forbidden` offers as a button. `REACT-09` (a balanced equation is a
correct equation) drives e04, s02, s03 and h01, where matching counts are
taken to settle a question they cannot reach.

A third strand runs through e02, s03 and h03 and is in neither register entry:
that a number in front multiplies EVERY atom in the formula it sits in front
of. It is the arithmetic error a student actually makes at the bench — reading
3H2O as three hydrogen atoms, or 2CH4 as six — and it is invisible to both of
the named misconceptions because a student who makes it is trying to obey the
rule rather than to break it. Those three carry a distractor that does exactly
that, and their four options are numerals of one shape with the numbers
changed, which is the numeric form §13 requires.

⚠️ EVERY FORMULA HERE IS FLAT — `H2O2`, `2CH4`, `2Mg + O2`. The lesson body
writes real `<sub>` elements, because the unit standardises on them and
`rich()` admits the tag; a question bank does not go through `rich()` and its
text is set as text by whatever surface serves the assignment, so a `<sub>`
here would ship as visible angle brackets. Design's own ladder is flat for the
same reason, and the split is documented at both ends.

Every question here is new prose — a question bank is the one place in these
two files where that is true — and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, and each is a mistake a real
student in a real lesson actually makes.
"""

UNIT = "C4"
LESSON = "symbol-equations-and-balancing"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c4-05-e01",
        "band": "easier",
        "text": "In the equation 2H2 + O2 makes 2H2O, which number tells you "
                "how many water particles are made?",
        "options": [
            {"text": "The 2 written in front of the H2O", "correct": True},
            {"text": "The small 2 inside the H2O", "correct": False,
             "why": "That 2 says a water particle is built from two hydrogen "
                    "atoms. It is part of the formula for water and it counts "
                    "atoms inside one particle, not particles."},
            {"text": "The 2 written in front of the H2", "correct": False,
             "why": "That one counts the hydrogen particles taking part. Each "
                    "formula's own front number counts that substance and no "
                    "other."},
            {"text": "The small 2 inside the O2", "correct": False,
             "why": "That 2 says an oxygen particle is made of two oxygen "
                    "atoms. It is part of the formula for oxygen gas and "
                    "says nothing about the water."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e02",
        "band": "easier",
        "text": "A student writes 3H2O. How many hydrogen atoms is that "
                "altogether?",
        "options": [
            {"text": "Three hydrogen atoms", "correct": False,
             "why": "Three is how many water particles there are. Each one "
                    "carries two hydrogen atoms, so the 3 has to multiply "
                    "what is inside the formula."},
            {"text": "Six hydrogen atoms", "correct": True},
            {"text": "Two hydrogen atoms", "correct": False,
             "why": "Two is how many hydrogen atoms are in ONE water "
                    "particle. The 3 in front says there are three of those "
                    "particles."},
            {"text": "Five hydrogen atoms", "correct": False,
             "why": "The number in front multiplies the atoms in the formula; "
                    "it is never added to them. Three particles of two atoms "
                    "each is six, not five."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-05-e03",
        "band": "easier",
        "text": "Which of these changes are you allowed to make while you are "
                "balancing an equation?",
        "options": [
            {"text": "Changing a small number inside a formula",
             "correct": False,
             "why": "The small numbers are part of the substance's name. "
                    "Changing H2O to H2O2 does balance the oxygen, and it "
                    "does it by turning the water into bleach."},
            {"text": "Swapping one substance in the equation for another",
             "correct": False,
             "why": "What the reaction makes is decided by the chemistry, and "
                    "the equation is the report of it. Swapping a substance "
                    "changes the claim rather than balancing it."},
            {"text": "Putting a bigger number in front of a formula",
             "correct": True},
            {"text": "Crossing out an atom that refuses to balance",
             "correct": False,
             "why": "Atoms are never created or destroyed, which is the whole "
                    "reason the equation has to balance. An atom you cross "
                    "out has to have gone somewhere."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-05-e04",
        "band": "easier",
        "text": "Both sides of an equation have the same number of every kind "
                "of atom. What does that tell you?",
        "options": [
            {"text": "That it is correct, because a balanced equation is a "
                     "correct equation", "correct": False,
             "why": "Balanced and true are two different things. H2 + O2 "
                    "makes H2O2 balances perfectly and describes a reaction "
                    "that does not happen."},
            {"text": "That the substances in it must be the right ones",
             "correct": False,
             "why": "The counts can be made to agree around any substances at "
                    "all. What the reaction really makes has to be found out "
                    "first, and the arithmetic comes afterwards."},
            {"text": "That it will stay balanced whatever you change next",
             "correct": False,
             "why": "It stays balanced only while nothing moves. Changing any "
                    "number in front changes the counts on that side "
                    "straight away."},
            {"text": "That it is balanced, which on its own does not make it "
                     "true", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c4-05-s01",
        "band": "standard",
        "text": "Magnesium burns in oxygen. Written as Mg + O2 makes MgO the "
                "equation does not balance. Which change fixes it?",
        "options": [
            {"text": "Put a 2 in front of the Mg and a 2 in front of the MgO",
             "correct": True},
            {"text": "Put a 2 in front of the O2 and a 2 in front of the MgO",
             "correct": False,
             "why": "That puts four oxygen atoms on the left against two on "
                    "the right. Oxygen was already the side with too many, "
                    "and doubling it widens the gap."},
            {"text": "Put a small 2 in the MgO so that it becomes MgO2",
             "correct": False,
             "why": "A small 2 there makes MgO2, which is a different "
                    "substance. Magnesium oxide is MgO, and the small numbers "
                    "in a formula belong to the substance."},
            {"text": "Put a 2 in front of the Mg and a small 2 in the MgO",
             "correct": False,
             "why": "The 2 in front of the Mg is right and the small 2 is "
                    "not. It balances the atoms by changing what is being "
                    "made, which is the one move balancing may not use."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-05-s02",
        "band": "standard",
        "text": "Why can a word equation never tell an engineer how much "
                "oxygen to supply for a fuel?",
        "options": [
            {"text": "It leaves out the products, so there is nothing to work "
                     "back from", "correct": False,
             "why": "A word equation does name its products. What it leaves "
                    "out is how many particles of each take part, and that is "
                    "the number the engineer needs."},
            {"text": "It names the substances but says nothing about how many "
                     "particles react", "correct": True},
            {"text": "It uses names, and a name is always less exact than a "
                     "symbol is", "correct": False,
             "why": "A name is exactly as precise as a formula about WHICH "
                    "substance it is. The difference is the numbers, which "
                    "only the symbol equation carries."},
            {"text": "It gives the ratio in words, which is too vague to "
                     "measure out", "correct": False,
             "why": "It gives no ratio at all, in words or otherwise. "
                    "'Hydrogen plus oxygen makes water' is true whether one "
                    "particle reacts or a million."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s03",
        "band": "standard",
        "text": "Methane is CH4. How many atoms altogether are there in 2CH4?",
        "options": [
            {"text": "Eight atoms altogether", "correct": False,
             "why": "Eight is the hydrogen alone, doubled. The 2 in front "
                    "multiplies everything inside the formula, and there is a "
                    "carbon atom in there too."},
            {"text": "Five atoms altogether", "correct": False,
             "why": "Five is what is in ONE methane particle — one carbon and "
                    "four hydrogens. The 2 in front says there are two of "
                    "those particles."},
            {"text": "Ten atoms altogether", "correct": True},
            {"text": "Seven atoms altogether", "correct": False,
             "why": "The number in front multiplies the atoms in the formula "
                    "and is never added to them. Two particles of five atoms "
                    "each is ten."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s04",
        "band": "standard",
        "text": "Two students balance the same reaction. One writes 2H2 + O2 "
                "makes 2H2O and the other writes 4H2 + 2O2 makes 4H2O. Who is "
                "right?",
        "options": [
            {"text": "The second, because bigger numbers describe more of the "
                     "reaction happening", "correct": False,
             "why": "The numbers give a RATIO, not an amount. Two to one is "
                    "the same ratio as four to two, and the equation is "
                    "written in the smallest whole numbers that work."},
            {"text": "The first, because the second one does not actually "
                     "balance at all", "correct": False,
             "why": "Count them: eight hydrogens and four oxygens on each "
                    "side. The second one balances perfectly — it is simply "
                    "not written the way it should be."},
            {"text": "Neither, because a balanced equation cannot have two "
                     "answers", "correct": False,
             "why": "Any balanced equation can be doubled and will still "
                    "balance. That is why the convention exists: the smallest "
                    "whole numbers that work are the ones written down."},
            {"text": "Both balance, but only the first is in the smallest "
                     "whole numbers", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c4-05-h01",
        "band": "harder",
        "text": "A student says that because balancing only changes the "
                "numbers in front, any equation you are handed can be made "
                "right. What is wrong with that?",
        "options": [
            {"text": "You have to know the real products first, and balancing "
                     "cannot tell you those", "correct": True},
            {"text": "Nothing — every equation can be put right by the "
                     "numbers in front", "correct": False,
             "why": "Balancing makes the arithmetic honest and does nothing "
                    "else. An equation naming a product the reaction does not "
                    "make will balance and still be false."},
            {"text": "Some equations do need their small numbers changed as "
                     "well", "correct": False,
             "why": "None of them do. A small number is part of the "
                    "substance, so changing one changes what the equation is "
                    "about rather than fixing it."},
            {"text": "Only an equation with one product on the right can be "
                     "balanced", "correct": False,
             "why": "Methane burning has two products and balances readily. "
                    "How many products there are is not what decides whether "
                    "an equation can balance."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-05-h02",
        "band": "harder",
        "text": "Sodium burns in chlorine. Chlorine gas is Cl2 and sodium "
                "chloride is NaCl. Why does the balanced equation need a 2 in "
                "front of the Na?",
        "options": [
            {"text": "Because NaCl already holds two atoms, so two of "
                     "everything else is needed", "correct": False,
             "why": "NaCl holds one sodium and one chlorine. What forces the "
                    "2 is on the other side: chlorine arrives in pairs, so "
                    "two sodium atoms are used at once."},
            {"text": "Because one chlorine particle carries two atoms, which "
                     "need two sodium atoms", "correct": True},
            {"text": "Because sodium always reacts two atoms at a time, "
                     "whatever it is reacting with", "correct": False,
             "why": "Sodium has no such habit. The 2 comes from the chlorine "
                    "travelling in pairs, and with a different reactant the "
                    "number would be different."},
            {"text": "Because the 2 in the Cl2 has to be copied in front of "
                     "the Na", "correct": False,
             "why": "A small number is never copied into a front number. The "
                    "two chlorine ATOMS have to be used up, and it takes two "
                    "sodium atoms to do it."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h03",
        "band": "harder",
        "text": "In the balanced equation CH4 + 2O2 makes CO2 + 2H2O, how "
                "many oxygen atoms are on the left?",
        "options": [
            {"text": "Two oxygen atoms", "correct": False,
             "why": "Two is one O2 particle. The 2 in front says there are "
                    "two of those particles, so the atoms double."},
            {"text": "Six oxygen atoms", "correct": False,
             "why": "Six counts the right-hand side as well. The question "
                    "asks about the left, where the only oxygen is the 2O2."},
            {"text": "Four oxygen atoms", "correct": True},
            {"text": "Three oxygen atoms", "correct": False,
             "why": "Three adds the 2 in front to the one particle it "
                    "describes. A number in front multiplies the atoms in the "
                    "formula; it never adds to them."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h04",
        "band": "harder",
        "text": "A plant runs 2H2 + O2 makes 2H2O and is fed hydrogen and "
                "oxygen in equal amounts. What happens?",
        "options": [
            {"text": "Nothing changes, because the reaction takes whatever it "
                     "is given", "correct": False,
             "why": "The ratio is fixed by the equation and cannot adjust. "
                    "Each water particle needs two hydrogens and one oxygen, "
                    "and there is nowhere else for atoms to come from."},
            {"text": "Twice as much water forms, because there is more oxygen "
                     "available", "correct": False,
             "why": "Extra oxygen makes no extra water. The hydrogen runs out "
                    "first, and once it has, the leftover oxygen has nothing "
                    "to react with."},
            {"text": "The equation rebalances itself to 2H2 + 2O2 makes "
                     "2H2O2", "correct": False,
             "why": "An equation does not rearrange itself to suit the "
                    "supply. H2O2 is hydrogen peroxide, and writing it would "
                    "be claiming the plant makes bleach."},
            {"text": "Half the oxygen is left over, because twice as much "
                     "hydrogen is needed", "correct": True},
                   ],
        "figure": None,
    },
]
