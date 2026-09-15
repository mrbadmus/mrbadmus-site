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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-05-e05",
        "band": "easier",
        "text": "What does it mean to say an equation is balanced?",
        "options": [
            {"text": "There are the same number of substances written on each "
                     "side of the arrow, so that neither side of the equation "
                     "is longer than the other",
             "correct": False,
             "why": "The number of SUBSTANCES often differs. It is the atoms "
                    "that have to match"},
            {"text": "Every kind of atom appears the same number of times on "
                     "both sides",
             "correct": True},
            {"text": "The same big numbers appear on both sides",
             "correct": False,
             "why": "The big numbers are usually different. What has to match "
                    "is the atom count"},
            {"text": "The equation describes a reaction that really happens",
             "correct": False,
             "why": "Balanced is not the same as true. An equation can "
                    "balance and describe a reaction nobody has ever seen"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e06",
        "band": "easier",
        "text": "What can a symbol equation tell you that a word equation "
                "cannot?",
        "options": [
            {"text": "Whether the reaction gives out heat or takes it in, "
                     "which is the thing an engineer most needs to know "
                     "before building a plant around it",
             "correct": False,
             "why": "Neither kind of equation carries energy. It is the "
                    "numbers of particles that symbols add"},
            {"text": "Which substances react",
             "correct": False,
             "why": "A word equation does that perfectly well. The symbols "
                    "add the counting"},
            {"text": "How many particles of each substance take part",
             "correct": True},
            {"text": "How fast the reaction goes",
             "correct": False,
             "why": "No equation of either kind says anything about rate"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e07",
        "band": "easier",
        "text": "In 4H2O, what does the 4 tell you?",
        "options": [
            {"text": "That there are four hydrogen atoms in each water "
                     "particle, so the formula describes a substance with "
                     "twice as much hydrogen in it as ordinary water",
             "correct": False,
             "why": "A number in FRONT counts particles. A number changing "
                    "the hydrogen would have to be small and after the H"},
            {"text": "That there are four oxygen atoms in one particle",
             "correct": False,
             "why": "Small numbers count atoms inside a particle. This one is "
                    "in front"},
            {"text": "That the water is four times as concentrated",
             "correct": False,
             "why": "Concentration is not what a formula records. The number "
                    "counts particles"},
            {"text": "That there are four water particles",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e08",
        "band": "easier",
        "text": "What is H2O2?",
        "options": [
            {"text": "Hydrogen peroxide, which bleaches hair",
             "correct": True},
            {"text": "Water, written out more fully so that both of the "
                     "atoms it is built from are shown in the formula rather "
                     "than only one of them",
             "correct": False,
             "why": "Water is H2O. Adding the second oxygen makes a different "
                    "substance altogether"},
            {"text": "Two water particles",
             "correct": False,
             "why": "Two waters would be 2H2O, with the number in front"},
            {"text": "A mixture of hydrogen and oxygen",
             "correct": False,
             "why": "It is a compound with its atoms joined, not a mixture of "
                    "two gases"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e09",
        "band": "easier",
        "text": "In 3CO2, how many oxygen atoms are there altogether?",
        "options": [
            {"text": "Two",
             "correct": False,
             "why": "That is the number in ONE particle. There are three "
                    "particles here"},
            {"text": "Six",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is how many particles there are. Each one carries "
                    "two oxygens"},
            {"text": "Five, adding the big 3 in front to the small 2 that "
                     "follows the oxygen symbol",
             "correct": False,
             "why": "The two numbers multiply rather than adding. Three lots "
                    "of two is six"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e10",
        "band": "easier",
        "text": "Why must the big numbers in a balanced equation be whole "
                "numbers?",
        "options": [
            {"text": "Because a fraction would make the equation harder to "
                     "read, and chemists agreed a long time ago to keep the "
                     "notation as simple as it can be made",
             "correct": False,
             "why": "Tidiness is why the SMALLEST whole numbers are used. "
                    "Whole numbers are required for a stronger reason"},
            {"text": "Because a fraction would unbalance the equation",
             "correct": False,
             "why": "A half would balance the counts perfectly well. It would "
                    "describe something that cannot exist"},
            {"text": "Because you cannot have half a particle",
             "correct": True},
            {"text": "Because small numbers are already whole",
             "correct": False,
             "why": "True and unrelated. The rule is about what a particle "
                    "count can mean"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c4-05-s05",
        "band": "standard",
        "text": "Balance: C + O2 makes CO2. What numbers have to go in?",
        "options": [
            {"text": "2 in front of the C and 2 in front of the CO2, matching "
                     "the two oxygen atoms that the O2 brings with it",
             "correct": False,
             "why": "That would give two carbons on the left and two on the "
                    "right — balanced, but not the smallest numbers, and "
                    "unnecessary"},
            {"text": "None — it is already balanced",
             "correct": True},
            {"text": "2 in front of the CO2",
             "correct": False,
             "why": "That would need two carbons and four oxygens on the "
                    "left, and there is one of each"},
            {"text": "2 in front of the O2",
             "correct": False,
             "why": "That gives four oxygen atoms on the left and two on the "
                    "right. It was balanced before you touched it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s06",
        "band": "standard",
        "text": "N2 + 3H2 makes 2NH3. How many hydrogen atoms are on each "
                "side?",
        "options": [
            {"text": "Three on the left and three on the right, which is what "
                     "makes the equation balance in the first place",
             "correct": False,
             "why": "Three is the number of hydrogen PARTICLES on the left. "
                    "Each carries two atoms"},
            {"text": "Six on the left and three on the right",
             "correct": False,
             "why": "Then it would not balance. Two NH3 particles carry three "
                    "hydrogens each"},
            {"text": "Six on each side",
             "correct": True},
            {"text": "Two on each side",
             "correct": False,
             "why": "Two is the number of ammonia particles. Count the atoms "
                    "inside them"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s07",
        "band": "standard",
        "text": "A student balances H2 + Cl2 makes HCl by writing HCl2. What "
                "have they actually done?",
        "options": [
            {"text": "Balanced it correctly, since both sides now carry the "
                     "same number of each kind of atom and that is the whole "
                     "requirement",
             "correct": False,
             "why": "The counts do not even match, and changing a small "
                    "number changes the substance in any case"},
            {"text": "Written the equation backwards",
             "correct": False,
             "why": "The direction is fine. The fault is inside a formula"},
            {"text": "Nothing wrong — HCl2 is another way of writing HCl",
             "correct": False,
             "why": "A small number is part of the substance's name. HCl and "
                    "HCl2 are not the same thing"},
            {"text": "Written a formula for a substance that is not hydrogen "
                     "chloride",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s08",
        "band": "standard",
        "text": "Which line is balanced?",
        "options": [
            {"text": "2H2 + O2 makes 2H2O",
             "correct": True},
            {"text": "H2 + O2 makes H2O",
             "correct": False,
             "why": "Two oxygen atoms on the left and one on the right. An "
                    "oxygen atom has gone missing"},
            {"text": "H2 + O2 makes H2O2, which balances because there are "
                     "two hydrogens and two oxygens on each side of the arrow",
             "correct": False,
             "why": "The counts do match, and the product is hydrogen "
                    "peroxide. Balanced is not the same as true"},
            {"text": "2H2 + 2O2 makes 2H2O",
             "correct": False,
             "why": "Four oxygen atoms on the left and two on the right. Two "
                    "have vanished"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s09",
        "band": "standard",
        "text": "In CH4 + 2O2 makes CO2 + 2H2O, how many atoms are there "
                "altogether on the right-hand side?",
        "options": [
            {"text": "Six, counting one carbon, two oxygens and then the "
                     "three atoms that make up a single particle of water",
             "correct": False,
             "why": "There are TWO water particles, so their atoms count "
                    "twice: three carbon-and-oxygen plus six from the water"},
            {"text": "Nine",
             "correct": True},
            {"text": "Five",
             "correct": False,
             "why": "That is the number on the left-hand side. Count the "
                    "products instead"},
            {"text": "Four",
             "correct": False,
             "why": "Four is the number of oxygen atoms on the left. The "
                    "question asks for every atom on the right"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s10",
        "band": "standard",
        "text": "How many atoms are there altogether in 3NH3?",
        "options": [
            {"text": "Four, which is the number of atoms in one particle of "
                     "ammonia and therefore the number the formula is "
                     "describing",
             "correct": False,
             "why": "Four is right for ONE particle. The 3 in front says "
                    "there are three of them"},
            {"text": "Seven, adding the 3 in front to the 3 after the H and "
                     "the nitrogen atom",
             "correct": False,
             "why": "The numbers multiply rather than adding. Three lots of "
                    "four is twelve"},
            {"text": "Twelve",
             "correct": True},
            {"text": "Nine",
             "correct": False,
             "why": "That is three lots of the three hydrogens. The nitrogen "
                    "in each particle has to be counted too"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-05-h05",
        "band": "harder",
        "text": "A plant runs 2H2 + O2 makes 2H2O and is fed 100 particles of "
                "hydrogen and 60 of oxygen. What happens?",
        "options": [
            {"text": "All of both are used, because the plant supplies "
                     "whatever is needed and any imbalance is corrected as the "
                     "reaction goes on",
             "correct": False,
             "why": "Nothing corrects an imbalance. The reaction stops when "
                    "one reactant runs out"},
            {"text": "All 100 hydrogens react with 50 oxygens, leaving 10 "
                     "oxygens unused",
             "correct": True},
            {"text": "60 hydrogens react with 60 oxygens, leaving 40 "
                     "hydrogens",
             "correct": False,
             "why": "The ratio is two hydrogen particles to one oxygen, not "
                    "one to one"},
            {"text": "Nothing reacts, because the amounts are not in the "
                     "right ratio",
             "correct": False,
             "why": "A reaction runs until one reactant is exhausted. It does "
                    "not refuse to start"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h06",
        "band": "harder",
        "text": "Balance: Fe + O2 makes Fe2O3. Which set of big numbers "
                "works?",
        "options": [
            {"text": "2Fe + O2 makes Fe2O3, which balances the iron and "
                     "leaves the oxygen to look after itself",
             "correct": False,
             "why": "The iron balances and the oxygen does not: two on the "
                    "left, three on the right"},
            {"text": "2Fe + 3O2 makes 2Fe2O3",
             "correct": False,
             "why": "The oxygen balances at six each side and the iron does "
                    "not: two on the left, four on the right"},
            {"text": "4Fe + 3O2 makes 2Fe2O3",
             "correct": True},
            {"text": "Fe + 3O2 makes Fe2O3",
             "correct": False,
             "why": "Neither element balances. One iron cannot make a product "
                    "containing two"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h07",
        "band": "harder",
        "text": "4H2 + 2O2 makes 4H2O balances perfectly and would still be "
                "marked down. Why?",
        "options": [
            {"text": "Because it describes four reactions at once rather than "
                     "one, and an equation is only allowed to describe a "
                     "single reaction happening",
             "correct": False,
             "why": "It describes the same reaction. The convention is about "
                    "the smallest whole numbers, not about how many "
                    "reactions"},
            {"text": "Because 4H2O is not a real formula",
             "correct": False,
             "why": "It is perfectly real — four water particles"},
            {"text": "Because oxygen cannot have a number in front of it",
             "correct": False,
             "why": "Any formula may carry a big number. There is no "
                    "exception for oxygen"},
            {"text": "Because the numbers are not the smallest whole ones "
                     "that work",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h08",
        "band": "harder",
        "text": "A hydrogen car is fed exactly equal numbers of hydrogen and "
                "oxygen particles. What does the engineer need to change, and "
                "why?",
        "options": [
            {"text": "Double the hydrogen, because the equation needs two "
                     "hydrogen particles per oxygen",
             "correct": True},
            {"text": "Nothing, because the two gases react one particle to "
                     "one particle",
             "correct": False,
             "why": "The balanced equation gives two hydrogens to one oxygen, "
                    "not one to one"},
            {"text": "Double the oxygen, so that there is plenty of it",
             "correct": False,
             "why": "There is already too much oxygen. Doubling it wastes "
                    "more"},
            {"text": "Halve both, so that the numbers stay equal",
             "correct": False,
             "why": "Halving both keeps the same wrong ratio, with less of "
                    "everything"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h09",
        "band": "harder",
        "text": "Adding a small 2 to the water balances the hydrogen "
                "equation in one move. What exactly does that move cost?",
        "options": [
            {"text": "Nothing at the time, and it will cost marks later on "
                     "because examiners insist on the big numbers being used "
                     "even where a small one would do the same job",
             "correct": False,
             "why": "It is not a marking convention. The equation now "
                    "describes a different reaction"},
            {"text": "The equation now says that burning hydrogen makes "
                     "hydrogen peroxide, which it does not",
             "correct": True},
            {"text": "The atom counts no longer match",
             "correct": False,
             "why": "They match exactly, which is what makes the move so "
                    "tempting. The problem is what has been written"},
            {"text": "The equation now needs a big number as well",
             "correct": False,
             "why": "No further number is needed. What is wrong is the "
                    "substance"},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h10",
        "band": "harder",
        "text": "Why does a balanced equation HAVE to have equal atom counts "
                "on both sides?",
        "options": [
            {"text": "Because chemists agreed on the rule so that equations "
                     "from different laboratories could be compared with each "
                     "other reliably",
             "correct": False,
             "why": "It is not a convention that could have been agreed "
                    "otherwise. It follows from what a reaction does"},
            {"text": "Because the two sides have to weigh the same",
             "correct": False,
             "why": "They do weigh the same, and that is a CONSEQUENCE of the "
                    "atoms being the same atoms"},
            {"text": "Because atoms are never created or destroyed in a "
                     "chemical reaction",
             "correct": True},
            {"text": "Because otherwise the equation would be hard to read",
             "correct": False,
             "why": "Readability is not the reason. An unbalanced equation "
                    "claims an atom appeared from nowhere"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 night 3 ────────────────────────────────────────
    {
        "id": "c4-05-e11",
        "band": "easier",
        "text": "In the formula O2, what does the small 2 tell you?",
        "options": [
            {"text": "That two oxygen particles are taking part",
             "correct": False,
             "why": "A count of separate particles is written as a big number "
                    "in front, not as a small number inside."},
            {"text": "That the oxygen is twice as concentrated",
             "correct": False,
             "why": "A formula records what one particle is built from. "
                    "Concentration is not something a formula can carry."},
            {"text": "That one particle of oxygen gas is built from two oxygen "
                     "atoms joined together",
             "correct": True},
            {"text": "That oxygen is the second substance written down",
             "correct": False,
             "why": "Small numbers have nothing to do with the order the "
                    "substances are written in."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e12",
        "band": "easier",
        "text": "One particle of methane is CH4. How many atoms does it "
                "contain?",
        "options": [
            {"text": "Five",
             "correct": True},
            {"text": 'Four',
             "correct": False,
             "why": "The carbon atom is in the formula too, written as the C "
                    "at the front."},
            {"text": 'One',
             "correct": False,
             "why": "It does describe one particle, and that particle is built "
                    "from more than one atom."},
            {"text": 'Fourteen',
             "correct": False,
             "why": "The letters are symbols for elements, not numbers waiting "
                    "to be added up."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e13",
        "band": "easier",
        "text": "A formula in an equation has no big number written in front "
                "of it. How many particles does it stand for?",
        "options": [
            {"text": "None, because a formula needs a number before it counts",
             "correct": False,
             "why": "Every formula written into an equation stands for "
                    "something. A blank space is not a missing substance."},
            {"text": "One particle, because a 1 is never written",
             "correct": True},
            {"text": 'As many as the balancing needs',
             "correct": False,
             "why": "A number chosen for balancing gets written down. A "
                    "formula with nothing in front of it means one."},
            {"text": "It cannot be worked out until the equation is balanced",
             "correct": False,
             "why": "A formula on its own already stands for one particle, "
                    "whether the equation balances or not."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e14",
        "band": "easier",
        "text": "Magnesium oxide is MgO. How many oxygen atoms are there "
                "in 2MgO?",
        "options": [
            {"text": "One, the number written after the O",
             "correct": False,
             "why": "There is no number after the O, so each particle carries "
                    "one oxygen atom — and there are two particles."},
            {"text": "Four, two in each particle",
             "correct": False,
             "why": "Magnesium oxide is MgO, with a single oxygen atom in it. "
                    "Four would need MgO2."},
            {"text": "Three, adding the 2 in front to the single O",
             "correct": False,
             "why": "A big number multiplies the atoms in the formula; it is "
                    "never added to them."},
            {"text": "Two, one oxygen atom from each of the two particles",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e15",
        "band": "easier",
        "text": "Hydrogen gas and chlorine gas both travel as pairs of atoms. "
                "How are the two gases written as formulae?",
        "options": [
            {"text": "2H and 2Cl",
             "correct": False,
             "why": "A big number in front counts separate particles. A pair "
                    "joined into one particle takes a small number."},
            {"text": "H2 and Cl2",
             "correct": True},
            {"text": "H and Cl, with the pairing understood",
             "correct": False,
             "why": "H and Cl are single atoms. Nothing there says the atoms "
                    "travel joined in twos."},
            {"text": "H2Cl2, because the two gases pair up together",
             "correct": False,
             "why": "That is one formula for one compound. The question is "
                    "about two separate gases."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e16",
        "band": "easier",
        "text": "Which of these lines is written as a symbol equation?",
        "options": [
            {"text": "sodium + chlorine makes sodium chloride",
             "correct": False,
             "why": "That is a word equation. It names the substances and uses "
                    "no formulae at all."},
            {"text": '2Na + Cl2, with nothing after it',
             "correct": False,
             "why": 'That names what you start with and then stops. An '
                    'equation has to say what you end with as well.'},
            {"text": "2Na + Cl2 makes 2NaCl",
             "correct": True},
            {"text": "sodium and chlorine react together to make salt",
             "correct": False,
             "why": "That is a sentence about the reaction. An equation is a "
                    "line of formulae with an arrow through it."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e17",
        "band": "easier",
        "text": "What does the word formula mean in chemistry?",
        "options": [
            {"text": "How a substance is written in symbols",
             "correct": True},
            {"text": "A rule for working out how many particles react",
             "correct": False,
             "why": "That is what a balanced equation gives you. A formula "
                    "describes one substance."},
            {"text": "The list of substances a reaction starts with",
             "correct": False,
             "why": "Those are the reactants. A formula belongs to a single "
                    "substance, not to a list of them."},
            {"text": "A sum that has to come out the same on both sides",
             "correct": False,
             "why": "Counting atoms on both sides is balancing. A formula is "
                    "what the atoms are counted in."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e18",
        "band": "easier",
        "text": "Magnesium burns in air. Which formula stands for magnesium "
                "oxide?",
        "options": [
            {"text": "Mg2O, with two magnesium atoms to each oxygen",
             "correct": False,
             "why": "That is a different substance. Magnesium oxide holds one "
                    "atom of each kind."},
            {"text": "MgO2, with two oxygen atoms in each particle",
             "correct": False,
             "why": "MgO2 is not magnesium oxide. The small numbers are part "
                    "of the substance's name."},
            {"text": "2MgO, because two particles are made each time",
             "correct": False,
             "why": "A big number counts particles inside an equation. It is "
                    "not part of the formula itself."},
            {"text": "MgO, one magnesium atom to one oxygen atom",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e19",
        "band": "easier",
        "text": "Where in a formula do you find the small numbers?",
        "options": [
            {"text": "At the very end, after the last symbol",
             "correct": False,
             "why": "A small number sits directly after the one symbol it "
                    "counts, wherever in the formula that symbol is."},
            {"text": "Just after the symbol they count, written smaller and "
                     "lower down",
             "correct": True},
            {"text": "At the front, before the first symbol",
             "correct": False,
             "why": "A number at the front is a big number, and it counts "
                    "whole particles instead."},
            {"text": "Above the symbol they belong to",
             "correct": False,
             "why": "Small numbers are written below the line of the symbols, "
                    "not above it."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e20",
        "band": "easier",
        "text": "Why is 2H2O not the same as H2O2?",
        "options": [
            {"text": "Because 2H2O comes earlier in the equation",
             "correct": False,
             "why": "Where a formula sits in an equation has nothing to do "
                    "with what the formula means."},
            {"text": 'Because a big 2 and a small 2 both mean the number two, '
                     'just written in two different places on the line',
             "correct": False,
             "why": "They mean different things. One counts whole particles "
                    "and the other counts atoms inside a particle."},
            {"text": "The first is two particles of water and the second is "
                     "one particle of a different substance",
             "correct": True},
            {"text": "Because only one of them can be balanced",
             "correct": False,
             "why": "Balancing is something a whole equation does, not "
                    "something a single formula does."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e21",
        "band": "easier",
        "text": "Balancing an equation changes how many particles react. What "
                "does it never change?",
        "options": [
            {"text": "What the substances are",
             "correct": True},
            {"text": "How many atoms take part in the reaction",
             "correct": False,
             "why": "Putting a bigger number in front is exactly what changes "
                    "how many atoms take part."},
            {"text": "Whether the equation balances",
             "correct": False,
             "why": "That is the one thing balancing is for: an unbalanced "
                    "equation is turned into a balanced one."},
            {"text": "The number of atoms written on each side",
             "correct": False,
             "why": "Those counts are what the big numbers move. Balancing "
                    "shifts them until they agree."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e22",
        "band": "easier",
        "text": "Iron oxide is Fe2O3. How many oxygen atoms are in one "
                "particle of it?",
        "options": [
            {"text": 'Two',
             "correct": False,
             "why": "That 2 counts the iron atoms. A small number counts only "
                    "the symbol it follows."},
            {"text": "Three",
             "correct": True},
            {"text": 'Five',
             "correct": False,
             "why": "Five is the total of all the atoms. The question asks for "
                    "the oxygen on its own."},
            {"text": 'Six, the two small numbers multiplied',
             "correct": False,
             "why": "Small numbers are not multiplied together. Each one "
                    "counts its own symbol and nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e23",
        "band": "easier",
        "text": "Sodium chloride is NaCl. How many sodium atoms are there in "
                "4NaCl?",
        "options": [
            {"text": "One, since the formula names a single sodium atom",
             "correct": False,
             "why": "Each particle holds one, and the 4 in front says there "
                    "are four of those particles."},
            {"text": 'Five',
             "correct": False,
             "why": "The big number multiplies the atoms in the formula and is "
                    "never added to them."},
            {"text": "Four, one from each particle",
             "correct": True},
            {"text": "Eight, four particles of two sodium atoms each",
             "correct": False,
             "why": "NaCl holds one sodium atom, not two. Two would have to be "
                    "written Na2Cl, which is a different substance."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e24",
        "band": "easier",
        "text": "Two hydrogen particles react with one oxygen particle. How is "
                "that written in front of the formulae?",
        "options": [
            {"text": 'H2 and H2 and O2',
             "correct": False,
             "why": "Writing the same particle twice is what a big number "
                    "replaces. An equation uses the number instead."},
            {"text": 'H4 + O2 instead',
             "correct": False,
             "why": "Changing a small number changes the substance. H4 is not "
                    "hydrogen gas."},
            {"text": '2H2 + 2O2 together',
             "correct": False,
             "why": "Only the hydrogen is doubled here. The oxygen stays as "
                    "one particle."},
            {"text": "2H2 + O2",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e25",
        "band": "easier",
        "text": "Which of these changes would alter what a formula means?",
        "options": [
            {"text": "Changing a small number that follows a symbol",
             "correct": True},
            {"text": "Writing a bigger number in front of it",
             "correct": False,
             "why": "A big number counts how many of that particle take part. "
                    "The particle itself is untouched."},
            {"text": "Moving it to the other end of its own side",
             "correct": False,
             "why": "The order of the substances on one side carries no "
                    "meaning at all."},
            {"text": "Writing it further along the same line",
             "correct": False,
             "why": "Where a formula is written on the line makes no "
                    "difference to the substance it names."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e26",
        "band": "easier",
        "text": "In 2Mg + O2 makes 2MgO, how many magnesium atoms are on the "
                "left?",
        "options": [
            {"text": 'One',
             "correct": False,
             "why": "Mg does name one atom, and the 2 in front says two of "
                    "those atoms take part."},
            {"text": "Two",
             "correct": True},
            {"text": 'Three',
             "correct": False,
             "why": "The symbol is not counted as an extra atom on top of the "
                    "number. The number says how many there are."},
            {"text": 'Four, two magnesium atoms in each particle',
             "correct": False,
             "why": "Mg is a single atom, so each particle is one atom. Four "
                    "would need 4Mg."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e27",
        "band": "easier",
        "text": "Water is H2O and hydrogen peroxide is H2O2. What single "
                "change turns the first formula into the second?",
        "options": [
            {"text": "A big 2 is put in front of the formula",
             "correct": False,
             "why": "A big number counts particles. It cannot reach inside a "
                    "formula and change the substance."},
            {"text": "The H is swapped for an O",
             "correct": False,
             "why": "Both hydrogen atoms are still there in H2O2. Nothing has "
                    "been swapped, only added."},
            {"text": "A small 2 is added after the O",
             "correct": True},
            {"text": "The small 2 after the H is moved along the formula",
             "correct": False,
             "why": "The hydrogen keeps its 2 in H2O2. A second small number "
                    "has been written, not moved."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e28",
        "band": "easier",
        "text": "Chlorine gas is written Cl2. How many chlorine atoms are "
                "there in 3Cl2?",
        "options": [
            {"text": 'Three',
             "correct": False,
             "why": "Three is how many particles there are. Each of them "
                    "carries two chlorine atoms."},
            {"text": 'Two',
             "correct": False,
             "why": "Two is right for one particle. The 3 in front says there "
                    "are three of them."},
            {"text": 'Five, the 3 added to the small 2',
             "correct": False,
             "why": "The two numbers multiply rather than adding. Three lots "
                    "of two is six."},
            {"text": "Six",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e29",
        "band": "easier",
        "text": "A big number is written in front of a formula. Which atoms "
                "does it multiply?",
        "options": [
            {"text": "Every atom in the formula it stands in front of",
             "correct": True},
            {"text": "Only the first symbol in that formula",
             "correct": False,
             "why": "It multiplies the whole particle, so every symbol in the "
                    "formula is multiplied."},
            {"text": "Only the atoms that already carry a small number",
             "correct": False,
             "why": "A symbol with no small number stands for one atom, and "
                    "that one is multiplied as well."},
            {"text": 'Every atom written anywhere on that side of the arrow',
             "correct": False,
             "why": "It reaches no further than its own formula. The next "
                    "formula along has its own number."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-e30",
        "band": "easier",
        "text": "In the formula 2CO2, how many carbon atoms are there?",
        "options": [
            {"text": 'Four',
             "correct": False,
             "why": "There are four oxygen atoms, and the carbon has its own "
                    "count: one in each of the two particles."},
            {"text": 'One',
             "correct": False,
             "why": "One is right for a single particle. The 2 in front says "
                    "two particles take part."},
            {"text": "Six, every atom the two particles hold",
             "correct": False,
             "why": "Six is all the atoms together. The question asks for the "
                    "carbon alone."},
            {"text": "Two",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night 3 ──────────────────────────────────────
    {
        "id": "c4-05-s11",
        "band": "standard",
        "text": "Hydrogen reacts with chlorine: H2 + Cl2 makes HCl. What has "
                "to be added to balance it?",
        "options": [
            {"text": "A 2 in front of the HCl",
             "correct": True},
            {"text": "A 2 in front of the H2 and one in front of the Cl2",
             "correct": False,
             "why": "That gives four hydrogen atoms and two chlorine atoms on "
                    "the left against one of each on the right, which is "
                    "further from balance than the line began."},
            {"text": 'A small 2 in HCl',
             "correct": False,
             "why": "H2Cl is a different substance. The small numbers belong "
                    "to the formula and are not yours to move."},
            {"text": "Nothing, because each side already holds two atoms",
             "correct": False,
             "why": "The left holds two hydrogens and two chlorines; the right "
                    "holds one of each. The totals are not the test."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s12",
        "band": "standard",
        "text": "Hydrogen peroxide breaks down into water and oxygen: H2O2 "
                "makes H2O + O2. What balances it?",
        "options": [
            {"text": "A 2 in front of the O2 on the right",
             "correct": False,
             "why": "That widens the gap. The right-hand side already carries "
                    "more oxygen than the left."},
            {"text": "A 2 in front of the H2O2 and a 2 in front of the H2O",
             "correct": True},
            {"text": "A small 2 after the O in the water",
             "correct": False,
             "why": "That turns the water back into hydrogen peroxide, so the "
                    "equation stops describing a breakdown at all."},
            {"text": "A 2 in front of the H2O only",
             "correct": False,
             "why": "That gives four hydrogens on the right against two on the "
                    "left. The hydrogen was balanced before."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s13",
        "band": "standard",
        "text": "Copper is heated in air: Cu + O2 makes CuO. Which set of big "
                "numbers balances it?",
        "options": [
            {"text": "Cu + 2O2 makes 2CuO",
             "correct": False,
             "why": "That gives four oxygen atoms on the left and two on the "
                    "right, and one copper against two."},
            {"text": "2Cu + 2O2 makes 2CuO",
             "correct": False,
             "why": "The copper balances and the oxygen does not: four atoms "
                    "on the left against two on the right."},
            {"text": "2Cu + O2 makes 2CuO",
             "correct": True},
            {"text": "Cu + O2 makes CuO2",
             "correct": False,
             "why": "CuO2 is not copper oxide. Changing a small number swaps "
                    "the product for a substance the reaction does not make."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s14",
        "band": "standard",
        "text": "A current is passed through water and it splits into two "
                "gases: H2O makes H2 + O2. Which big numbers are needed?",
        "options": [
            {"text": "A small 2 after the O in the water",
             "correct": False,
             "why": "That makes the starting substance hydrogen peroxide, "
                    "which is not what is being split."},
            {"text": "A 2 in front of the O2",
             "correct": False,
             "why": "The right-hand side already has too much oxygen. Doubling "
                    "it makes the shortfall worse."},
            {"text": "A 2 in front of the H2 only",
             "correct": False,
             "why": "That leaves four hydrogens on the right against two on "
                    "the left, and the oxygen still short."},
            {"text": "A 2 in front of the H2O and a 2 in front of the H2",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s15",
        "band": "standard",
        "text": "When balancing the burning of methane, why is it easier to "
                "leave the oxygen until last?",
        "options": [
            {"text": "Oxygen appears in both products, so its total is settled "
                     "once the others are done",
             "correct": True},
            {"text": 'Oxygen is a gas, and a gas is always balanced after '
                     'every solid in the same equation',
             "correct": False,
             "why": "Nothing in balancing depends on whether a substance is a "
                    "gas, a liquid or a solid."},
            {"text": 'Oxygen travels in pairs, so it can only be balanced '
                     'once every other element has been settled',
             "correct": False,
             "why": "It does travel in pairs, and that is no reason it must "
                    "come last. Chlorine travels in pairs and is balanced "
                    "first in other equations."},
            {"text": "Oxygen is the only atom allowed a big number",
             "correct": False,
             "why": "Every formula in an equation may carry a big number. No "
                    "element is treated specially."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s16",
        "band": "standard",
        "text": "Aluminium oxide is Al2O3. In the balanced line 4Al + 3O2 "
                "makes 2Al2O3, how many oxygen atoms are on the right?",
        "options": [
            {"text": 'Three',
             "correct": False,
             "why": "Three is right for one particle. The 2 in front says "
                    "there are two of them."},
            {"text": "Six",
             "correct": True},
            {"text": 'Five',
             "correct": False,
             "why": "That counts the aluminium in as well. The question asks "
                    "for the oxygen alone."},
            {"text": "Ten, all the atoms in both product particles",
             "correct": False,
             "why": "Ten is every atom on the right. Six of them are oxygen "
                    "and four are aluminium."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s17",
        "band": "standard",
        "text": "Putting a 2 in front of H2O changes the oxygen count. Why "
                "does it change the hydrogen count as well?",
        "options": [
            {"text": "Because water always has to keep two hydrogens for every "
                     "oxygen",
             "correct": False,
             "why": "That ratio is true of water, and it is not what the big "
                    "number does. The number multiplies the whole particle."},
            {"text": "Because the hydrogen already has a small 2, which the "
                     "big 2 doubles",
             "correct": False,
             "why": "The big number multiplies every atom in the formula, "
                    "whether it carries a small number or not."},
            {"text": "Because the big number multiplies every atom in the "
                     "formula, not just the last one",
             "correct": True},
            {"text": "Because the hydrogen and the oxygen are joined, so they "
                     "cannot be counted apart",
             "correct": False,
             "why": "They are joined, and they are counted separately every "
                    "time an equation is balanced."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s18",
        "band": "standard",
        "text": "A student balances Mg + O2 makes MgO by rewriting it as Mg + "
                "O makes MgO. What is wrong?",
        "options": [
            {"text": "The equation now has too few atoms on the right",
             "correct": False,
             "why": "It has one of each on both sides. The fault is that the "
                    "left-hand substance is no longer oxygen gas."},
            {"text": "A big number should have been used instead of an arrow",
             "correct": False,
             "why": "The arrow is exactly where it should be. What has changed "
                    "is a formula."},
            {"text": "The product should have been written MgO2",
             "correct": False,
             "why": "MgO2 is a different substance. Magnesium oxide is MgO and "
                    "stays MgO."},
            {"text": "Oxygen gas is O2, so writing O changes the substance the "
                     "magnesium is burning in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s19",
        "band": "standard",
        "text": "Ammonia is NH3. In 2NH3, how many nitrogen atoms and how many "
                "hydrogen atoms are there?",
        "options": [
            {"text": "Two nitrogen and six hydrogen",
             "correct": True},
            {"text": "One nitrogen and three hydrogen",
             "correct": False,
             "why": "That is one particle. The 2 in front says there are two "
                    "of them."},
            {"text": "Two nitrogen and three hydrogen",
             "correct": False,
             "why": "The big number multiplies every atom in the formula, so "
                    "the hydrogen doubles along with the nitrogen."},
            {"text": "Two nitrogen and five hydrogen",
             "correct": False,
             "why": "The 2 in front is multiplied by the 3, not added to it. "
                    "Two lots of three is six."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s20",
        "band": "standard",
        "text": "Zinc reacts with hydrochloric acid: Zn + HCl makes ZnCl2 + "
                "H2. What balances it?",
        "options": [
            {"text": "A 2 in front of the ZnCl2",
             "correct": False,
             "why": "That asks for four chlorine atoms on the right against "
                    "one on the left, and two zincs against one."},
            {"text": "A 2 in front of the HCl",
             "correct": True},
            {"text": "A small 2 after the H in the HCl",
             "correct": False,
             "why": "H2Cl is not hydrochloric acid. The small numbers belong "
                    "to the substance."},
            {"text": "A 2 in front of the Zn and a 2 in front of the H2",
             "correct": False,
             "why": "The zinc was balanced already, and doubling the hydrogen "
                    "gas makes the hydrogen shortfall worse."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s21",
        "band": "standard",
        "text": "A reactor runs N2 + 3H2 makes 2NH3 and is fed 300 nitrogen "
                "particles. How many hydrogen particles are needed?",
        "options": [
            {"text": '300',
             "correct": False,
             "why": "The equation asks for three hydrogen particles to every "
                    "one of nitrogen, not one to one."},
            {"text": '100',
             "correct": False,
             "why": "The 3 says hydrogen is the substance there is more of. "
                    "Dividing turns the ratio upside down."},
            {"text": "900",
             "correct": True},
            {"text": "600, matching the 2 in front of the ammonia",
             "correct": False,
             "why": "The 2 belongs to the ammonia made. The hydrogen needed is "
                    "set by the 3 in front of the H2."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s22",
        "band": "standard",
        "text": "A student writes 2MgO on the right and says the 2 also counts "
                "the O2 on the left. Why is that wrong?",
        "options": [
            {"text": 'Because a big number may only ever be written on the '
                     'left-hand side of an arrow',
             "correct": False,
             "why": "Big numbers are written on both sides. That is how the "
                    "two sides are brought into agreement."},
            {"text": "Because the O2 already carries a small 2, which does the "
                     "counting for it",
             "correct": False,
             "why": "The small 2 counts atoms inside one particle. It says "
                    "nothing about how many particles there are."},
            {"text": "Because the left-hand side is counted before the right",
             "correct": False,
             "why": "The two sides are counted in whichever order suits you. "
                    "Order is not what limits a big number."},
            {"text": "Because a big number counts only the formula it stands "
                     "in front of",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s23",
        "band": "standard",
        "text": "A student makes the atom counts agree by swapping the "
                "products for different substances. Why is that not balancing?",
        "options": [
            {"text": "The products are fixed by what the reaction makes, and "
                     "balancing may only change how many particles react",
             "correct": True},
            {"text": "Swapping a product is allowed once the counts agree",
             "correct": False,
             "why": "It is not allowed at any point. The equation would then "
                    "report a reaction nobody ran."},
            {"text": "Only the reactants may be swapped for other substances",
             "correct": False,
             "why": "Neither side may be swapped. Both are decided by the "
                    "chemistry before any balancing starts."},
            {"text": 'It is balancing, only done the long way round, and it '
                     'reaches exactly the same answer as changing the numbers '
                     'would',
             "correct": False,
             "why": "It is not a slower method. It produces an equation about "
                    "a different reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s24",
        "band": "standard",
        "text": "A line of an equation reads 2CO2 + 3H2O. How many oxygen "
                "atoms is that?",
        "options": [
            {"text": 'Five',
             "correct": False,
             "why": "The big numbers multiply what is inside each formula. CO2 "
                    "brings two oxygens of its own."},
            {"text": "Seven",
             "correct": True},
            {"text": 'Three',
             "correct": False,
             "why": "A big number counts particles of one substance. It is not "
                    "an answer on its own."},
            {"text": "Four, the oxygen in the carbon dioxide only",
             "correct": False,
             "why": "Four is the carbon dioxide's share. The water carries "
                    "three more oxygen atoms."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s25",
        "band": "standard",
        "text": "A student offers 2CH4 + 2O2 makes 2CO2 + 4H2O. Does it "
                "balance?",
        "options": [
            {"text": "Yes, every kind of atom matches",
             "correct": False,
             "why": "The carbon and the hydrogen match. The oxygen does not: "
                    "four on the left against eight on the right."},
            {"text": "No, the hydrogen is short on the left",
             "correct": False,
             "why": "The hydrogen is fine at eight atoms on each side. It is "
                    "the oxygen that fails."},
            {"text": "No, there are four oxygen atoms on the left and eight on "
                     "the right",
             "correct": True},
            {"text": "No, the carbon is doubled on one side only",
             "correct": False,
             "why": "There are two carbon atoms on each side. The carbon "
                    "balances perfectly."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s26",
        "band": "standard",
        "text": "Magnesium nitride is Mg3N2. Is 3Mg + N2 makes Mg3N2 balanced?",
        "options": [
            {"text": "No, the nitrogen is short on the right",
             "correct": False,
             "why": "There are two nitrogen atoms on each side. The small 2 in "
                    "Mg3N2 supplies them."},
            {"text": "No, a big number is needed in front of the product",
             "correct": False,
             "why": "A second particle of the product would need six magnesium "
                    "atoms, and only three are supplied."},
            {"text": "No, the magnesium needs a small number instead",
             "correct": False,
             "why": "The magnesium in the product already carries its small 3. "
                    "Small numbers are not added while balancing."},
            {"text": "Yes, three magnesium and two nitrogen atoms on each side",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s27",
        "band": "standard",
        "text": "Iron and sulfur are heated and make iron sulfide: Fe + S "
                "makes FeS. Why does this equation need no big numbers?",
        "options": [
            {"text": "Each formula already supplies one atom of each kind, so "
                     "the counts agree as written",
             "correct": True},
            {"text": 'Because neither element travels as a pair of atoms, so '
                     'there is nothing that has to be doubled on either side',
             "correct": False,
             "why": 'Neither element does travel in pairs, and that is not '
                    'what decides it. An equation is tested by counting its '
                    'atoms, not by the shape of the substances in it.'},
            {"text": "Because there is only one product to balance against",
             "correct": False,
             "why": "A single product is no guarantee. Mg + O2 makes MgO has "
                    "one product and needs balancing."},
            {"text": 'Because solids are counted by their mass rather than by '
                     'the number of particles in them',
             "correct": False,
             "why": "A symbol equation counts particles for every substance, "
                    "solid or not."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s28",
        "band": "standard",
        "text": "Magnesium reacts with hydrochloric acid to make MgCl2 and H2. "
                "How many HCl particles does one magnesium atom need?",
        "options": [
            {"text": 'One',
             "correct": False,
             "why": "The magnesium needs two chlorine atoms for MgCl2, and "
                    "each HCl carries only one."},
            {"text": "Two",
             "correct": True},
            {"text": 'Four',
             "correct": False,
             "why": "MgCl2 holds three atoms, two of them chlorine. Two HCl "
                    "particles supply those two chlorines."},
            {"text": "Three, one for the magnesium and two for the chlorine",
             "correct": False,
             "why": "The magnesium is already there. Only the two chlorine "
                    "atoms have to be supplied."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s29",
        "band": "standard",
        "text": "Why must the same KINDS of atom appear on both sides of an "
                "equation, and not simply the same number of atoms?",
        "options": [
            {"text": 'Because a reaction is allowed to turn one kind of atom '
                     'into another whenever the totals on the two sides still '
                     'come out equal',
             "correct": False,
             "why": "No chemical reaction changes one element into another. "
                    "The atoms are only joined up differently."},
            {"text": 'Because an atom of one kind weighs the same as an atom '
                     'of any other, so only the totals matter',
             "correct": False,
             "why": 'Atoms of different elements have different masses, which '
                    'is exactly why matching totals is not enough.'},
            {"text": "A reaction rearranges the atoms it started with, so an "
                     "atom of a kind that was never there cannot appear",
             "correct": True},
            {"text": "Because each kind of atom has a different symbol to "
                     "write down",
             "correct": False,
             "why": "Symbols are how the atoms are recorded. They are not why "
                    "the kinds have to match."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-s30",
        "band": "standard",
        "text": "A balanced equation is changed by doubling the big numbers on "
                "the left only. What happens?",
        "options": [
            {"text": "It stays balanced, because both sides were doubled "
                     "together",
             "correct": False,
             "why": "Only one side was doubled. The other side was left as it "
                    "was."},
            {"text": "It stays balanced, but is no longer in its smallest "
                     "numbers",
             "correct": False,
             "why": "That is what happens when BOTH sides are doubled. "
                    "Doubling one side breaks the counts."},
            {"text": "It stops balancing, because the left now holds twice as "
                     "many atoms as the right",
             "correct": True},
            {"text": "It stops balancing, because the substances have been "
                     "changed",
             "correct": False,
             "why": "No substance has changed. Every formula is exactly as it "
                    "was, and only the counts have moved."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night 3 ────────────────────────────────────────
    {
        "id": "c4-05-h11",
        "band": "harder",
        "text": "Aluminium burns in chlorine to make aluminium chloride: Al + "
                "Cl2 makes AlCl3. Which set of big numbers balances it?",
        "options": [
            {"text": "2Al + 3Cl2 makes 2AlCl3",
             "correct": True},
            {"text": "Al + 3Cl2 makes AlCl3",
             "correct": False,
             "why": "The aluminium balances at one each side and the chlorine "
                    "does not: six on the left against three on the right."},
            {"text": "3Al + 2Cl2 makes 3AlCl3",
             "correct": False,
             "why": "The numbers are the right pair the wrong way round: four "
                    "chlorine atoms on the left against nine on the right."},
            {"text": "2Al + 3Cl2 makes 3AlCl3",
             "correct": False,
             "why": "The chlorine is then nine on the right against six on the "
                    "left, and the aluminium three against two."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h12",
        "band": "harder",
        "text": "Marble reacts with acid: CaCO3 + HCl makes CaCl2 + H2O + CO2. "
                "What single change balances it?",
        "options": [
            {"text": "A 2 in front of the CaCO3",
             "correct": False,
             "why": "That doubles the calcium and the carbon on the left, "
                    "neither of which was short."},
            {"text": "A 2 in front of the HCl",
             "correct": True},
            {"text": "A 2 in front of the H2O",
             "correct": False,
             "why": "That asks for four hydrogen atoms on the right against "
                    "the one on the left, which is further from balance."},
            {"text": "A small 2 after the Cl in the HCl",
             "correct": False,
             "why": "HCl2 is not hydrochloric acid. Balancing may not reach "
                    "inside a formula."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h13",
        "band": "harder",
        "text": "C + O2 makes CO2 and 2C + O2 makes 2CO both balance. What is "
                "the difference between the two claims?",
        "options": [
            {"text": "One is in smaller numbers than the other",
             "correct": False,
             "why": "Neither can be reduced. The difference is not in the "
                    "numbers at all."},
            {"text": "The second describes twice as much burning",
             "correct": False,
             "why": "Big numbers give a ratio, not an amount. What differs is "
                    "the substance written on the right."},
            {"text": "They say the reaction makes different substances, and "
                     "only the chemistry can decide which one it is",
             "correct": True},
            {"text": 'The second cannot be right, because doubling the carbon '
                     'on both sides is a move that balancing does not allow',
             "correct": False,
             "why": "Doubling a formula is an ordinary move. It is the product "
                    "that differs, and CO is a real substance."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h14",
        "band": "harder",
        "text": "Butane burns as 2C4H10 + 13O2 makes 8CO2 + 10H2O. How many "
                "oxygen atoms are on the right?",
        "options": [
            {"text": 'Eighteen',
             "correct": False,
             "why": "Those are particle counts. Each CO2 carries two oxygen "
                    "atoms, so the carbon dioxide alone supplies sixteen."},
            {"text": 'Sixteen',
             "correct": False,
             "why": "Sixteen is the carbon dioxide alone. The ten water "
                    "particles carry an oxygen atom each."},
            {"text": "Thirteen, the big number the oxygen carries on the left",
             "correct": False,
             "why": "Thirteen counts oxygen particles on the left. The "
                    "question asks for oxygen atoms on the right."},
            {"text": "Twenty-six",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h15",
        "band": "harder",
        "text": "Two elements react as 2X + 3Y2 makes 2XY3. How many atoms of "
                "Y are there in the product altogether?",
        "options": [
            {"text": "Six",
             "correct": True},
            {"text": 'Three',
             "correct": False,
             "why": "Three is the count in one particle of XY3, and the 2 in "
                    "front says there are two of them."},
            {"text": "Five, the 2 in front added to the small 3",
             "correct": False,
             "why": "A big number multiplies the atoms of the formula and is "
                    "never added to a small one."},
            {"text": 'Eight',
             "correct": False,
             "why": "Eight is every atom in the product. The question asks for "
                    "the Y atoms alone."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h16",
        "band": "harder",
        "text": "A student says that doubling every big number in N2 + 3H2 "
                "makes 2NH3 would make the reactor produce twice as much "
                "ammonia. Evaluate that claim.",
        "options": [
            {"text": 'Correct, since the equation would then name four ammonia '
                     'particles where it named two, and four particles is '
                     'twice as much ammonia',
             "correct": False,
             "why": "The written numbers are a ratio. How much is produced "
                    "depends on how much is fed in, not on how the ratio is "
                    "written down."},
            {"text": "Wrong — the numbers give the ratio the substances react "
                     "in, and how much is made depends on how much is supplied",
             "correct": True},
            {"text": "Correct, because bigger numbers mean a bigger reaction",
             "correct": False,
             "why": "An equation carries no size. The same equation describes "
                    "a test tube and a chemical works."},
            {"text": "Wrong, because a balanced equation cannot be doubled",
             "correct": False,
             "why": "It can be doubled and it stays balanced. What is wrong is "
                    "the claim about the amount produced."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h17",
        "band": "harder",
        "text": "Ammonia burns in oxygen: NH3 + O2 makes N2 + H2O. Which set "
                "of big numbers balances it?",
        "options": [
            {"text": "2NH3 + 2O2 makes N2 + 3H2O",
             "correct": False,
             "why": "The nitrogen and hydrogen balance, and the oxygen does "
                    "not: four on the left against three on the right."},
            {"text": "4NH3 + 3O2 makes 4N2 + 6H2O",
             "correct": False,
             "why": "The hydrogen and oxygen balance, and the nitrogen does "
                    "not: four on the left against eight on the right."},
            {"text": "4NH3 + 3O2 makes 2N2 + 6H2O",
             "correct": True},
            {"text": "4NH3 + 6O2 makes 2N2 + 6H2O",
             "correct": False,
             "why": "Twelve oxygen atoms on the left against six on the right. "
                    "Only the oxygen has been over-supplied."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h18",
        "band": "harder",
        "text": "A student checks an equation by counting the total number of "
                "atoms on each side, finds they match, and calls it balanced. "
                "Why is that check not enough?",
        "options": [
            {"text": "Totals can only match when the kinds match, so the check "
                     "is sound",
             "correct": False,
             "why": "They can match while the kinds do not — four hydrogens "
                    "and two oxygens on one side, two and four on the other."},
            {"text": "The check misses any atom that carries no small number",
             "correct": False,
             "why": "A symbol with no small number counts as one atom, and a "
                    "total sweeps it up along with the rest."},
            {"text": "The totals must be counted on the left before the right",
             "correct": False,
             "why": "The order the sides are counted in makes no difference to "
                    "either total."},
            {"text": "Each kind of atom has to match on its own, and two "
                     "different shortfalls can cancel out in a total",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h19",
        "band": "harder",
        "text": "An equation balances with the big numbers 2, 2 and 4 in front "
                "of its three formulae. What should be written instead?",
        "options": [
            {"text": "1, 1 and 2",
             "correct": True},
            {"text": "2, 2 and 4, which is already correct",
             "correct": False,
             "why": "It balances, and all three numbers share a factor of two, "
                    "so it is not in its smallest whole numbers."},
            {"text": "1, 1 and 4, dividing only the first two",
             "correct": False,
             "why": "Dividing some numbers and not others breaks the balance. "
                    "Every big number has to be divided together."},
            {"text": "4, 4 and 8, doubling them to be safe",
             "correct": False,
             "why": "That goes the wrong way. The convention asks for the "
                    "smallest whole numbers that work."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h20",
        "band": "harder",
        "text": "Iron oxide is Fe2O3. In 3Fe2O3, how many atoms are there "
                "in total?",
        "options": [
            {"text": 'Eight',
             "correct": False,
             "why": "The big number multiplies the formula and is never added "
                    "to it."},
            {"text": "Fifteen",
             "correct": True},
            {"text": "Nine, three oxygen atoms for each of the three particles",
             "correct": False,
             "why": "Nine is the oxygen alone. The six iron atoms have to be "
                    "counted as well."},
            {"text": 'Five',
             "correct": False,
             "why": "Five is one particle. The 3 in front says there are three "
                    "of them."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h21",
        "band": "harder",
        "text": "Iron oxide is heated with carbon: Fe2O3 + C makes Fe + CO2. "
                "Which set of big numbers balances it?",
        "options": [
            {"text": "Fe2O3 + 3C makes 2Fe + 3CO2",
             "correct": False,
             "why": "The iron balances at two each side and the oxygen does "
                    "not: three on the left against six on the right."},
            {"text": "2Fe2O3 + C makes 4Fe + CO2",
             "correct": False,
             "why": "The iron balances at four each side and the oxygen does "
                    "not: six on the left against two on the right."},
            {"text": "2Fe2O3 + 3C makes 4Fe + 3CO2",
             "correct": True},
            {"text": "2Fe2O3 + 6C makes 4Fe + 6CO2",
             "correct": False,
             "why": "The carbon has been doubled on both sides, so the oxygen "
                    "runs six on the left against twelve on the right."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h22",
        "band": "harder",
        "text": "Sodium reacts with water: Na + H2O makes NaOH + H2. Which set "
                "of big numbers balances it?",
        "options": [
            {"text": "Na + 2H2O makes NaOH + H2",
             "correct": False,
             "why": "The hydrogen then runs four on the left against three on "
                    "the right, and the oxygen two against one."},
            {"text": "2Na + H2O makes 2NaOH + H2",
             "correct": False,
             "why": "The sodium balances and the oxygen does not: one on the "
                    "left against two on the right."},
            {"text": "2Na + 2H2O makes 2NaOH + H2",
             "correct": True},
            {"text": "2Na + 2H2O makes 2NaOH + 2H2",
             "correct": False,
             "why": "That puts six hydrogen atoms on the right against four on "
                    "the left. Only one hydrogen particle is released."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h23",
        "band": "harder",
        "text": "Ethane burns as 2C2H6 + 7O2 makes 4CO2 + 6H2O. How many "
                "hydrogen atoms are on the left?",
        "options": [
            {"text": "Twelve",
             "correct": True},
            {"text": "Six, the small number in the formula for ethane",
             "correct": False,
             "why": "Six is right for one particle, and the 2 in front says "
                    "there are two of them."},
            {"text": "Eight, adding the 2 in front to the small 6",
             "correct": False,
             "why": "The two numbers multiply rather than adding. Two lots of "
                    "six is twelve."},
            {"text": "Sixteen, counting the carbon atoms in as well",
             "correct": False,
             "why": "Sixteen is every atom in the ethane. The question asks "
                    "for the hydrogen alone."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h24",
        "band": "harder",
        "text": "Propane is C3H8. Which of these is the balanced equation for "
                "burning it in oxygen?",
        "options": [
            {"text": "C3H8 + 3O2 makes 3CO2 + 4H2O",
             "correct": False,
             "why": "The carbon and hydrogen balance and the oxygen does not: "
                    "six on the left against ten on the right."},
            {"text": "C3H8 + 5O2 makes 3CO2 + 4H2O",
             "correct": True},
            {"text": "C3H8 + 5O2 makes 3CO2 + 8H2O",
             "correct": False,
             "why": "Eight waters carry sixteen hydrogen atoms against the "
                    "eight the propane supplies."},
            {"text": "C3H8 + 4O2 makes 3CO2 + 4H2O",
             "correct": False,
             "why": "Eight oxygen atoms on the left against ten on the right. "
                    "One more O2 particle is needed."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h25",
        "band": "harder",
        "text": "An equation cannot be made to balance whatever big numbers "
                "are tried. What does that tell you?",
        "options": [
            {"text": "Some reactions simply cannot be written as equations",
             "correct": False,
             "why": "Every reaction can be written down. If the correct "
                    "formulae are used, the numbers can always be found."},
            {"text": 'A small number somewhere will have to be changed '
                     'instead',
             "correct": False,
             "why": "Changing a small number would give a different substance. "
                    "The formula has to be looked up, not invented."},
            {"text": "At least one of the formulae in it must be wrong",
             "correct": True},
            {"text": "The arrow must be pointing the wrong way",
             "correct": False,
             "why": "Turning an equation round balances exactly as well or as "
                    "badly as it did before."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h26",
        "band": "harder",
        "text": "Two elements react and make a single compound. Explain why "
                "the compound's formula, rather than the big numbers, decides "
                "how the equation must balance.",
        "options": [
            {"text": 'Because the big numbers are chosen first, and the '
                     'formula for the product is then written to fit whatever '
                     'numbers happened to be picked',
             "correct": False,
             "why": "The formula is found out before any balancing begins. The "
                    "numbers are the only thing left to choose."},
            {"text": 'Because the big numbers must be whole numbers and a '
                     "formula's small numbers need not be",
             "correct": False,
             "why": 'Both kinds are whole numbers. A small number counts '
                    'atoms inside a particle, and there is no such thing as '
                    'part of an atom either.'},
            {"text": "Because the smallest whole numbers have to be used in "
                     "the end",
             "correct": False,
             "why": "That convention tidies an answer once it is found. It "
                    "does not decide what the answer is."},
            {"text": "Because the formula fixes the ratio of atoms in the "
                     "product, and the big numbers then have to supply exactly "
                     "that ratio",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h27",
        "band": "harder",
        "text": "A furnace runs 2Mg + O2 makes 2MgO. How many magnesium atoms "
                "react with 30 oxygen particles?",
        "options": [
            {"text": "60",
             "correct": True},
            {"text": '30',
             "correct": False,
             "why": "Each oxygen particle carries two atoms, and it takes two "
                    "magnesium atoms to use both of them."},
            {"text": "15, halving the oxygen to match the 2 in the equation",
             "correct": False,
             "why": "The 2 says magnesium is the substance there is more of. "
                    "Halving turns the ratio upside down."},
            {"text": '120',
             "correct": False,
             "why": "The pairing in O2 is what the 2 in front of the Mg "
                    "already answers. It is not counted twice."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h28",
        "band": "harder",
        "text": "Sulfur dioxide reacts with more oxygen: SO2 + O2 makes SO3. "
                "Which set of big numbers balances it?",
        "options": [
            {"text": "SO2 + 2O2 makes SO3",
             "correct": False,
             "why": "Six oxygen atoms on the left against three on the right, "
                    "which is further from balance than the line began."},
            {"text": "2SO2 + O2 makes 2SO3",
             "correct": True},
            {"text": "2SO2 + 2O2 makes 2SO3",
             "correct": False,
             "why": "The sulfur balances and the oxygen does not: eight on the "
                    "left against six on the right."},
            {"text": "SO2 + O2 makes SO4",
             "correct": False,
             "why": "SO4 is a different substance. A small number may not be "
                    "changed to make the counts agree."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h29",
        "band": "harder",
        "text": "A student balances an equation, then notices that one of the "
                "formulae was copied down wrongly. What must they do?",
        "options": [
            {"text": "Keep the numbers and correct the formula afterwards",
             "correct": False,
             "why": "The numbers were chosen to suit the wrong formula, so "
                    "they will not fit the right one."},
            {"text": "Leave it, since the counts already agree on both sides",
             "correct": False,
             "why": "They agree around a substance that takes no part. A "
                    "balanced equation about the wrong reaction is worthless."},
            {"text": "Correct the formula and balance the equation again, "
                     "because the big numbers depend on the formulae",
             "correct": True},
            {"text": "Change a small number elsewhere to make up for it",
             "correct": False,
             "why": "That would put a second wrong substance into the equation "
                    "alongside the first."},
        ],
        "figure": None,
    },
    {
        "id": "c4-05-h30",
        "band": "harder",
        "text": "Aluminium takes oxygen from copper oxide: 2Al + 3CuO makes "
                "Al2O3 + 3Cu. How many atoms are there on the left?",
        "options": [
            {"text": "Five, the atoms in the Al2O3 the reaction makes",
             "correct": False,
             "why": "Five is the aluminium oxide on the right. The question "
                    "asks about the left-hand side."},
            {"text": "Six, three copper atoms and three oxygen atoms",
             "correct": False,
             "why": "That is the copper oxide alone. The two aluminium atoms "
                    "have to be counted as well."},
            {"text": "Eight",
             "correct": True},
            {"text": "Nine, counting the copper released as well",
             "correct": False,
             "why": "The copper on its own is a product. It appears on the "
                    "right of the arrow, not the left."},
        ],
        "figure": None,
    },
]
