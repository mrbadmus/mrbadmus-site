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
]
