"""C8 lesson 03 — Groups and periods: twelve questions (MRB-281).

The lesson's argument is one shape: similarity runs DOWN the columns and not
along the rows, because a column shares a number of outer electrons and a row
shares nothing that matters. The page teaches it with a tappable table of the
first twenty elements and four addresses to read off it.

These twelve probe the angles the mastery ladder leaves alone: reading an
address both ways, using a group to predict a formula, and telling the group
number apart from the atomic number.

The distractors are built from the lesson's two declared misconceptions.

`PTAB-05` (elements next to each other are similar) drives the wrong options
in e02, s01, s03 and h02. Each treats adjacency as kinship. s03 is the one
that matters: sodium and chlorine are six squares apart in one row and react
together to make table salt, so the belief has to explain a pair that could
hardly be less alike.

`PTAB-06` (the group number tells you how many electrons the atom has) drives
e04, s02 and h01, where the two numbers printed on every square are conflated.

A third strand, on the page and in neither register entry, is that a group
fixes a FORMULA and not just a behaviour — e03 and h04 are built on it, because
that is the part Mendeleev actually used and the part students forget.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "groups-and-periods"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-03-e01",
        "band": "easier",
        # ⚑ Deliberately asks about the PERIOD, not the group. The recall
        # rung already asks "what is a group", and check 6 is right that a
        # bank restating a rung adds no depth.
        "text": "What is a period in the periodic table?",
        "options": [
            {"text": "A horizontal row, running from metals on the left to "
                     "non-metals on the right",
             "correct": True},
            {"text": "A vertical column of elements that all behave in "
                     "similar ways",
             "correct": False,
             "why": "That describes a group. Elements in a period are not "
                    "alike at all."},
            {"text": "The length of time an element takes to react with "
                     "water",
             "correct": False,
             "why": "The word has an everyday meaning that does not apply "
                    "here. A period is a row."},
            {"text": "A set of elements that all have the same number of "
                     "outer electrons",
             "correct": False,
             "why": "That is a group again. Along a period the outer-electron "
                    "count rises by one each square."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e02",
        "band": "easier",
        "text": "Sodium is in group 1 and magnesium is the square next to it "
                "in group 2. What does being neighbours tell you?",
        "options": [
            {"text": "That they will react in almost exactly the same way",
             "correct": False,
             "why": "Sodium explodes on water; magnesium barely fizzes. "
                    "Neighbours along a row are not a family."},
            {"text": "Very little — they are in different groups and behave "
                     "differently",
             "correct": True},
            {"text": "That magnesium must be more reactive, being further "
                     "along",
             "correct": False,
             "why": "It is less reactive, and in any case reactivity does not "
                    "simply rise along a period."},
            {"text": "That they will form compounds with identical formulae",
             "correct": False,
             "why": "Same formulae come from the same GROUP. Sodium gives "
                    "NaCl and magnesium MgCl₂."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e03",
        "band": "easier",
        "text": "Lithium reacts with water to give lithium hydroxide and "
                "hydrogen. What would you expect sodium to do?",
        "options": [
            {"text": "Nothing, because each element in a group behaves "
                     "differently",
             "correct": False,
             "why": "A group is a family precisely because its members do "
                    "behave alike."},
            {"text": "Give a completely different set of products from "
                     "lithium",
             "correct": False,
             "why": "Same group, same kind of reaction, same kind of "
                    "products. Only the vigour changes."},
            {"text": "The same reaction, giving sodium hydroxide and hydrogen",
             "correct": True},
            {"text": "React only if the water is heated first",
             "correct": False,
             "why": "Sodium reacts violently with cold water straight from "
                    "the tap."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e04",
        "band": "easier",
        "text": "Chlorine is in group 7 and has 17 electrons in total. How "
                "many are in its outer shell?",
        "options": [
            {"text": "17, because the group number counts every electron",
             "correct": False,
             "why": "17 is the atomic number. The group number counts only "
                    "the outer shell."},
            {"text": "3, because 17 is three more than a full shell of "
                     "fourteen",
             "correct": False,
             "why": "Shells do not hold fourteen, and the group number is "
                    "read straight off the table."},
            {"text": "10, because the inner shells hold seven between them",
             "correct": False,
             "why": "This reverses the two numbers. The outer shell is the "
                    "smaller count here, not the larger."},
            {"text": "7, because the group number is the number of outer "
                     "electrons",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-03-s01",
        "band": "standard",
        "text": "Which pair would you expect to behave most alike: chlorine "
                "and argon, or chlorine and fluorine?",
        "options": [
            {"text": "Chlorine and fluorine, because both are in group 7",
             "correct": True},
            {"text": "Chlorine and argon, because they are next to each other",
             "correct": False,
             "why": "They are adjacent and opposite: one attacks almost every "
                    "metal, the other reacts with nothing."},
            {"text": "Both pairs equally, because all three are non-metals",
             "correct": False,
             "why": "Being a non-metal is far too coarse. It puts carbon and "
                    "helium in the same box."},
            {"text": "Chlorine and argon, because their atomic masses are "
                     "close",
             "correct": False,
             "why": "Similar mass does not mean similar chemistry — the "
                    "lesson Mendeleev's swaps taught."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s02",
        "band": "standard",
        "text": "Two squares on the table print the numbers 12 and 2 for "
                "magnesium. What does each number mean?",
        "options": [
            {"text": "12 is the group and 2 is the period it sits in",
             "correct": False,
             "why": "There is no group 12 on a KS3 table. The columns run 1 "
                    "to 7 and then 0."},
            {"text": "12 is the atomic number and 2 is the number of outer "
                     "electrons",
             "correct": True},
            {"text": "12 is the mass and 2 is the number of shells it has",
             "correct": False,
             "why": "Magnesium has three shells, and 12 is the count of "
                    "protons rather than the mass."},
            {"text": "12 is the number of shells and 2 is the atomic number",
             "correct": False,
             "why": "No atom has twelve shells, and magnesium's atomic number "
                    "is 12."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s03",
        "band": "standard",
        "text": "Sodium and chlorine sit six squares apart in period 3 and "
                "react together to make table salt. What does that show about "
                "sharing a period?",
        "options": [
            {"text": "That elements in a period get steadily more similar "
                     "along the row",
             "correct": False,
             "why": "They get steadily LESS alike — the row runs from a "
                    "violent metal to an unreactive gas."},
            {"text": "That a period groups elements which react with each "
                     "other",
             "correct": False,
             "why": "Sodium reacts with chlorine because they are opposites, "
                    "not because they share a row."},
            {"text": "That sharing a period says almost nothing about "
                     "behaviour",
             "correct": True},
            {"text": "That the period number decides which compounds an "
                     "element forms",
             "correct": False,
             "why": "The GROUP decides the formula. The period only says how "
                    "many shells there are."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s04",
        "band": "standard",
        "text": "Which element is in group 2 of period 4?",
        "options": [
            {"text": "Magnesium, because it is the second element in group 2",
             "correct": False,
             "why": "Magnesium is group 2 but period 3 — one row too far up."},
            {"text": "Potassium, because it is the first element in period 4",
             "correct": False,
             "why": "Potassium is period 4 but group 1 — one column too far "
                    "left."},
            {"text": "Beryllium, because it is at the top of group 2",
             "correct": False,
             "why": "Beryllium is group 2 but period 2 — two rows too far "
                    "up."},
            {"text": "Calcium, counting two columns across on the fourth row",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-03-h01",
        "band": "harder",
        "text": "Why does the group number predict how an element reacts, "
                "when the atomic number does not?",
        "options": [
            {"text": "Because only the outer electrons take part in reactions",
             "correct": True},
            {"text": "Because the atomic number is too large a figure to be "
                     "useful",
             "correct": False,
             "why": "Size is not the problem. Atomic number fixes the "
                    "element's identity exactly — it just does not predict "
                    "behaviour directly."},
            {"text": "Because the group number is measured and the atomic "
                     "number is estimated",
             "correct": False,
             "why": "Both are exact counts. Neither is an estimate."},
            {"text": "Because the atomic number changes when an element "
                     "reacts",
             "correct": False,
             "why": "The atomic number never changes in a chemical reaction. "
                    "It is what makes the element that element."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h02",
        "band": "harder",
        "text": "An unfamiliar element is in group 1, period 5. Which "
                "prediction is best supported?",
        "options": [
            {"text": "It is a gas, because period 5 is a long way down the "
                     "table",
             "correct": False,
             "why": "Group decides the family, and group 1 is metals all the "
                    "way down."},
            {"text": "It is a soft metal that reacts violently with water",
             "correct": True},
            {"text": "It behaves like the element to its right in period 5",
             "correct": False,
             "why": "That is the neighbours-are-similar error. Its family is "
                    "the column, not the row."},
            {"text": "It is unreactive, because larger atoms hold their "
                     "electrons more tightly",
             "correct": False,
             "why": "Larger atoms hold the outer electron LESS tightly, which "
                    "is why group 1 gets more reactive downwards."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h03",
        "band": "harder",
        "text": "The transition metals sit between groups 2 and 3 from "
                "period 4 onwards. Why are they treated as a block rather "
                "than as ordinary groups?",
        "options": [
            {"text": "Because they were discovered later than the elements "
                     "either side",
             "correct": False,
             "why": "Iron and copper are among the oldest known elements of "
                    "all."},
            {"text": "Because they are the only metals in the whole table",
             "correct": False,
             "why": "Groups 1 and 2 are metals too, and far more reactive "
                    "ones."},
            {"text": "Because they behave alike across the block, not just "
                     "down it",
             "correct": True},
            {"text": "Because they have no outer electrons to react with",
             "correct": False,
             "why": "They have outer electrons and react readily — just less "
                    "violently than group 1."},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h04",
        "band": "harder",
        "text": "Carbon forms CO₂. Silicon is directly below it. "
                "What is the strongest reason to expect SiO₂?",
        "options": [
            {"text": "Because silicon is heavier, so it takes more oxygen "
                     "atoms",
             "correct": False,
             "why": "Mass does not set the ratio. Tin is much heavier than "
                    "silicon and still gives SnO₂."},
            {"text": "Because every element forms an oxide with two oxygen "
                     "atoms",
             "correct": False,
             "why": "Sodium gives Na₂O and magnesium gives MgO. "
                    "The ratio is a fact about the group."},
            {"text": "Because carbon and silicon were discovered close "
                     "together",
             "correct": False,
             "why": "Discovery has no bearing on combining ratios."},
            {"text": "Because elements in one group combine in the same "
                     "ratios",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-03-e05",
        "band": "easier",
        "text": "What is the outer shell of an atom?",
        "options": [
            {"text": "The outermost layer of electrons, and the one that "
                     "takes part in reactions",
             "correct": True},
            {"text": "The surface of the atom, where it touches the atoms "
                     "next to it and is held in place by them in the "
                     "structure",
             "correct": False,
             "why": "An atom has no surface in that sense. The shell is a "
                    "layer of electrons"},
            {"text": "The nucleus right at the middle of the atom, where all "
                     "of the protons and neutrons sit",
             "correct": False,
             "why": "The nucleus is the centre. The outer shell is as far "
                    "from it as the electrons go"},
            {"text": "The whole set of electrons that the atom has, counted "
                     "right across every one of its shells",
             "correct": False,
             "why": "That is all of them across every shell. Only the "
                    "outermost layer is the outer shell"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e06",
        "band": "easier",
        "text": "Potassium is in group 1. How many electrons are in its outer "
                "shell?",
        "options": [
            {"text": "19, which is the number of electrons a potassium atom "
                     "has altogether and therefore the number available in "
                     "its outermost layer",
             "correct": False,
             "why": "19 is the total across every shell. The group number "
                    "gives the outer ones, and it is 1"},
            {"text": "One",
             "correct": True},
            {"text": "Four, counting the period it is in",
             "correct": False,
             "why": "The period number counts SHELLS, not the electrons in "
                    "the outer one"},
            {"text": "Eight",
             "correct": False,
             "why": "Eight is a full outer shell, which is group 0. Group 1 "
                    "has one"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e07",
        "band": "easier",
        "text": "Iron, copper and zinc sit in the block between groups 2 and "
                "3. What are they called?",
        "options": [
            {"text": "Alkali metals",
             "correct": False,
             "why": "Those are group 1 — soft, light and stored under oil. "
                    "These three are none of those things"},
            {"text": "Halogens",
             "correct": False,
             "why": "The halogens are group 7 and are non-metals"},
            {"text": "Transition metals",
             "correct": True},
            {"text": "Noble gases, since they are the metals that are least "
                     "willing to react and so share the property that gives "
                     "group 0 its name",
             "correct": False,
             "why": "Noble gases are gases in group 0. Being unreactive does "
                    "not put a metal there"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-03-s05",
        "band": "standard",
        "text": "Which element is in group 7 of period 2?",
        "options": [
            {"text": "Fluorine",
             "correct": True},
            {"text": "Chlorine, which is the halogen everybody meets first "
                     "and is therefore the one at the top of the group",
             "correct": False,
             "why": "Chlorine is group 7 and period 3. Fluorine is the one "
                    "above it"},
            {"text": "Oxygen",
             "correct": False,
             "why": "Oxygen is in period 2 and in group 6. One column short"},
            {"text": "Neon",
             "correct": False,
             "why": "Neon is in period 2 and in group 0, one column further "
                    "on"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s06",
        "band": "standard",
        "text": "An element is described as being in period 4. What does that "
                "tell you?",
        "options": [
            {"text": "That it has four electrons in its outer shell, since "
                     "the row number counts them in the same way the column "
                     "number does",
             "correct": False,
             "why": "Outer electrons are counted by the GROUP number. A "
                    "period tells you how many shells there are"},
            {"text": "Which row it is in, and so how many shells its atoms "
                     "have",
             "correct": True},
            {"text": "That it is a metal",
             "correct": False,
             "why": "A period runs from metals on the left to non-metals on "
                    "the right, so it covers both"},
            {"text": "That it behaves like the other elements in period 4",
             "correct": False,
             "why": "Sharing a period says almost nothing about behaviour. "
                    "Sharing a group does"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s07",
        "band": "standard",
        "text": "Lithium hydroxide, sodium hydroxide and potassium hydroxide "
                "all have one metal atom to one oxygen and one hydrogen. What "
                "does that pattern show?",
        "options": [
            {"text": "That the three metals are all in period 2, so their "
                     "atoms are close enough in size to build the same "
                     "compound between them",
             "correct": False,
             "why": "They are in three different periods. What they share is "
                    "the column"},
            {"text": "That all hydroxides have that formula",
             "correct": False,
             "why": "Calcium hydroxide is group 2 and takes two hydroxides "
                    "per metal atom. The formula follows the group"},
            {"text": "That elements in one group form compounds with the same "
                     "formulae",
             "correct": True},
            {"text": "That the three metals all have very nearly the same "
                     "atomic mass as each other",
             "correct": False,
             "why": "Their masses differ a great deal. It is the outer "
                    "electron count they share"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-03-h05",
        "band": "harder",
        "text": "The group number is not a label somebody chose. What is it?",
        "options": [
            {"text": "The number of electrons in an atom's outer shell",
             "correct": True},
            {"text": "The number of the column, counted from the left-hand "
                     "edge of the table, which is why group 1 is the first "
                     "column and group 7 the seventh",
             "correct": False,
             "why": "That is how it is READ off, and the number would be "
                    "arbitrary if that were all it was. It counts outer "
                    "electrons"},
            {"text": "The number of shells in the atom",
             "correct": False,
             "why": "That is the period number, read down the side"},
            {"text": "The number of compounds the element can form",
             "correct": False,
             "why": "No element is limited like that. Carbon forms millions"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h06",
        "band": "harder",
        "text": "Suppose the group number did NOT match the number of outer "
                "electrons. What would follow?",
        "options": [
            {"text": "Nothing much — the table would still work, because the "
                     "families were noticed from how the elements behave long "
                     "before anyone knew about electrons",
             "correct": False,
             "why": "The families were noticed first, and the electron count "
                    "is why they exist. Without it there is no reason for "
                    "them"},
            {"text": "There would be no reason for a column to behave as a "
                     "family, and the table would have to be redrawn",
             "correct": True},
            {"text": "Only group 0 would be affected",
             "correct": False,
             "why": "Every group's chemistry follows from its outer electron "
                    "count, not just the full one"},
            {"text": "The periods would have to be renumbered instead, and the "
                     "columns could then be left exactly as they already are",
             "correct": False,
             "why": "The periods count shells and are a separate matter. It "
                    "is the columns that would lose their meaning"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h07",
        "band": "harder",
        "text": "The transition metals are the ones almost everything has "
                "ever been built out of. Which set of their properties "
                "explains that?",
        "options": [
            {"text": "That they are soft, light and easy to cut, so they can "
                     "be worked into shape without heavy machinery",
             "correct": False,
             "why": "That describes group 1, which is far too reactive to "
                    "build with. Transition metals are hard and dense"},
            {"text": "That their compounds are coloured",
             "correct": False,
             "why": "A real property of theirs, and it is why they are used "
                    "as pigments rather than why bridges are made of them"},
            {"text": "That they are hard, dense and much less reactive than "
                     "the metals on the far left",
             "correct": True},
            {"text": "That they are found as the pure metal in the ground, so "
                     "no smelting of them is needed at all",
             "correct": False,
             "why": "Almost all of them have to be smelted out of an ore. "
                    "Gold is the famous exception"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e08",
        "band": "easier",
        "text": "An atom has six electrons in its outer shell. Which group is "
                "the element in?",
        "options": [
            {"text": "Group 6", "correct": True},
            {"text": "Group 2", "correct": False,
             "why": "A group 2 atom carries two outer electrons, not six"},
            {"text": "Group 8", "correct": False,
             "why": "The main columns run 1 to 7 and then 0, so nothing is "
                    "headed 8"},
            {"text": "Period 6", "correct": False,
             "why": "A period is a row and counts shells, not outer electrons"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e09",
        "band": "easier",
        "text": "What does an element's period number tell you?",
        "options": [
            {"text": "How many electrons sit in its outer shell",
             "correct": False,
             "why": "That is the group number, which is the column rather "
                    "than the row"},
            {"text": "How many shells its electrons occupy", "correct": True},
            {"text": "How many protons are packed into its nucleus",
             "correct": False,
             "why": "That is the atomic number, printed on every square"},
            {"text": "How heavy one of its atoms is", "correct": False,
             "why": "That is the mass number, and it climbs along a row as "
                    "well as down one"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e10",
        "band": "easier",
        "text": "Beryllium is in group 2 of period 2. How many electrons "
                "does a beryllium atom have altogether?",
        "options": [
            {"text": "2", "correct": False,
             "why": "Two is its outer-shell count, and the full shell "
                    "underneath has to be added"},
            {"text": "8", "correct": False,
             "why": "Eight is what fills a second shell, and beryllium's is "
                    "nowhere near full"},
            {"text": "4", "correct": True},
            {"text": "22", "correct": False,
             "why": "Writing the group and the period side by side makes a "
                    "number that counts nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e11",
        "band": "easier",
        "text": "An atom's electrons are arranged 2,8,1. Which group is the "
                "element in?",
        "options": [
            {"text": "Group 2", "correct": False,
             "why": "The 2 is the innermost shell, which is full, and not "
                    "the outer one"},
            {"text": "Group 8", "correct": False,
             "why": "The 8 is the middle shell, and no column is headed 8 in "
                    "any case"},
            {"text": "Group 11", "correct": False,
             "why": "Eleven is the total number of electrons, which is the "
                    "atomic number"},
            {"text": "Group 1", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e12",
        "band": "easier",
        "text": "A sodium atom has an atomic number of 11. How many "
                "electrons does one sodium atom have?",
        "options": [
            {"text": "11", "correct": True},
            {"text": "1", "correct": False,
             "why": "One is its outer-shell count, which is its group number"},
            {"text": "3", "correct": False,
             "why": "Three is how many shells its electrons occupy, which is "
                    "its period"},
            {"text": "23", "correct": False,
             "why": "Twenty-three is sodium's mass number, which counts "
                    "particles in the nucleus"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e13",
        "band": "easier",
        "text": "Whereabouts in the periodic table are the metals found?",
        "options": [
            {"text": "Spread evenly through every group", "correct": False,
             "why": "They are not spread evenly; there is a clear divide "
                    "across the table"},
            {"text": "On the left-hand side and in the middle block",
             "correct": True},
            {"text": "Only in groups 1 and 2", "correct": False,
             "why": "Groups 1 and 2 are metals, but so is the whole block "
                    "between groups 2 and 3"},
            {"text": "On the right-hand side, past the staircase",
             "correct": False,
             "why": "The right-hand side past the staircase is where the "
                    "non-metals sit"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e14",
        "band": "easier",
        "text": "The main columns of the periodic table are numbered in "
                "order from the left. Which number heads the last column?",
        "options": [
            {"text": "8", "correct": False,
             "why": "Counting straight on to 8 is the natural guess, but the "
                    "last column is not numbered that way"},
            {"text": "7", "correct": False,
             "why": "Seven heads the second-from-last column, which holds "
                    "fluorine and chlorine"},
            {"text": "0", "correct": True},
            {"text": "20", "correct": False,
             "why": "Twenty is how many elements a KS3 table usually draws, "
                    "not a column heading"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e15",
        "band": "easier",
        "text": "Neon is the last element in period 2. Which group is neon "
                "in?",
        "options": [
            {"text": "Group 2", "correct": False,
             "why": "Two is neon's period, which is the row it sits in"},
            {"text": "Group 7", "correct": False,
             "why": "Group 7 is the second-from-last column, and fluorine is "
                    "its period 2 member"},
            {"text": "Group 10", "correct": False,
             "why": "Ten is neon's atomic number, the total count of its "
                    "electrons"},
            {"text": "Group 0", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e16",
        "band": "easier",
        "text": "Which electrons in an atom take part in chemical reactions?",
        "options": [
            {"text": "The ones in the outer shell", "correct": True},
            {"text": "The ones in the innermost shell", "correct": False,
             "why": "The inner shells are full and stay out of the chemistry"},
            {"text": "All of them equally", "correct": False,
             "why": "Only the outermost take part, which is why the group "
                    "number matters"},
            {"text": "The ones in the nucleus", "correct": False,
             "why": "The nucleus holds protons and neutrons; the electrons "
                    "are outside it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e17",
        "band": "easier",
        "text": "An argon atom's electrons are arranged 2,8,8. How many are "
                "in its outer shell?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Two is the innermost shell, which filled first"},
            {"text": "Eight", "correct": True},
            {"text": "Three", "correct": False,
             "why": "Three is how many shells hold electrons, which gives "
                    "the period"},
            {"text": "Eighteen", "correct": False,
             "why": "Eighteen is the total across all three shells, which is "
                    "the atomic number"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e18",
        "band": "easier",
        "text": "A metal is described as sitting in the block between groups "
                "2 and 3. What does that tell you about its group number?",
        "options": [
            {"text": "It is group 2, since that is the column on its left",
             "correct": False,
             "why": "Group 2 is the column itself; the block sits beyond it "
                    "and takes neither heading"},
            {"text": "It is group 3, since that is the column on its right",
             "correct": False,
             "why": "Group 3 is that column's own heading, and the block is "
                    "not part of it"},
            {"text": "It has none of the numbered group headings",
             "correct": True},
            {"text": "It is whichever group matches its period number",
             "correct": False,
             "why": "The period counts shells and never doubles as a group "
                    "heading"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e19",
        "band": "easier",
        "text": "A chlorine atom's electrons are arranged 2,8,7. How many "
                "shells hold electrons?",
        "options": [
            {"text": "Seven", "correct": False,
             "why": "Seven is the outer-shell count, which gives the group"},
            {"text": "Seventeen", "correct": False,
             "why": "Seventeen is the total number of electrons, which is "
                    "the atomic number"},
            {"text": "Two", "correct": False,
             "why": "Two is only the innermost shell; there are two more "
                    "beyond it"},
            {"text": "Three", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e20",
        "band": "easier",
        "text": "Which of these is an address in the periodic table?",
        "options": [
            {"text": "Group 5, period 2", "correct": True},
            {"text": "Atomic number 12", "correct": False,
             "why": "That counts the electrons in one atom; it does not say "
                    "which row or column"},
            {"text": "Mass number 24", "correct": False,
             "why": "That says how heavy an atom is, which no column or row "
                    "is set by"},
            {"text": "The symbol Mg", "correct": False,
             "why": "A symbol names the element without saying where its "
                    "square sits"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e21",
        "band": "easier",
        "text": "What does the word family mean when it is used about the "
                "periodic table?",
        "options": [
            {"text": "A set of elements found together in the same rock",
             "correct": False,
             "why": "Where an element is dug up has nothing to do with which "
                    "column it sits in"},
            {"text": "A set of elements that react in the same way",
             "correct": True},
            {"text": "A run of elements with masses close together",
             "correct": False,
             "why": "Elements with close masses sit side by side in a row, "
                    "and those are the least alike"},
            {"text": "All the elements discovered by one chemist",
             "correct": False,
             "why": "Who found an element does not decide where its square "
                    "goes"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e22",
        "band": "easier",
        "text": "Which two elements make up the whole of period 1?",
        "options": [
            {"text": "Lithium and beryllium", "correct": False,
             "why": "Those two open period 2, the row below"},
            {"text": "Hydrogen and lithium", "correct": False,
             "why": "Lithium is in period 2, directly under hydrogen"},
            {"text": "Hydrogen and helium", "correct": True},
            {"text": "Helium and neon", "correct": False,
             "why": "Both close a row in group 0, but neon closes period 2"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e23",
        "band": "easier",
        "text": "Period 2 runs from lithium to neon. How many elements is "
                "that?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Two is how many period 1 holds, in the row above"},
            {"text": "Seven", "correct": False,
             "why": "Seven is the highest numbered group, but one more "
                    "square closes the row"},
            {"text": "Twenty", "correct": False,
             "why": "Twenty is how many elements are drawn altogether, "
                    "across four rows"},
            {"text": "Eight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e24",
        "band": "easier",
        "text": "Magnesium sits in group 2. How many outer electrons does a "
                "magnesium atom have?",
        "options": [
            {"text": "Two", "correct": True},
            {"text": "Twelve", "correct": False,
             "why": "Twelve is its atomic number, the electron total for the "
                    "whole atom"},
            {"text": "Three", "correct": False,
             "why": "Three is its period, the number of shells its electrons "
                    "occupy"},
            {"text": "Eight", "correct": False,
             "why": "Eight is what fills an outer shell, not what magnesium "
                    "carries in one"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e25",
        "band": "easier",
        "text": "A square for chlorine prints 35.5 and 17. Which of the two "
                "is the atomic number?",
        "options": [
            {"text": "35.5", "correct": False,
             "why": "35.5 is the relative atomic mass, which says how heavy an "
                    "atom is"},
            {"text": "17", "correct": True},
            {"text": "Neither of them", "correct": False,
             "why": "Every square prints an atomic number, so it is one of "
                    "the two"},
            {"text": "Both, written two ways", "correct": False,
             "why": "They measure different things and are never the same "
                    "number"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e26",
        "band": "easier",
        "text": "A zig-zag staircase is printed across the periodic table. "
                "What does it separate?",
        "options": [
            {"text": "The metals from the transition metals", "correct": False,
             "why": "The transition metals are metals and sit well to the "
                    "left of the staircase"},
            {"text": "One period from the next", "correct": False,
             "why": "Rows are separated by being drawn one under another, "
                    "not by a staircase"},
            {"text": "The metals from the non-metals", "correct": True},
            {"text": "The solids from the gases", "correct": False,
             "why": "State is not what the staircase marks; most non-metals "
                    "beside it are solid"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e27",
        "band": "easier",
        "text": "Electrons fill the shells around a nucleus in order. Which "
                "shell fills first?",
        "options": [
            {"text": "The outermost one", "correct": False,
             "why": "The outer shell is the last to fill and the one left "
                    "part-filled"},
            {"text": "Whichever holds the most", "correct": False,
             "why": "Shells fill from the inside out, whatever they hold"},
            {"text": "They all fill together", "correct": False,
             "why": "Each shell fills completely before the next one starts"},
            {"text": "The one nearest the nucleus", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e28",
        "band": "easier",
        "text": "Going down a group from one element to the next, what "
                "happens to the number of electrons in the outer shell?",
        "options": [
            {"text": "It stays the same", "correct": True},
            {"text": "It rises by one each time", "correct": False,
             "why": "That is what happens going across a row, not down a "
                    "column"},
            {"text": "It falls by one each time", "correct": False,
             "why": "Nothing about the outer count falls down a column; it "
                    "is fixed"},
            {"text": "It doubles each time", "correct": False,
             "why": "The outer count does not grow at all, let alone double"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e29",
        "band": "easier",
        "text": "Which of these pairs of elements is in the same group?",
        "options": [
            {"text": "Sodium and magnesium", "correct": False,
             "why": "They are next-door squares in period 3 and in different "
                    "columns"},
            {"text": "Nitrogen and phosphorus", "correct": True},
            {"text": "Carbon and nitrogen", "correct": False,
             "why": "They are neighbours along period 2, one column apart"},
            {"text": "Neon and sodium", "correct": False,
             "why": "Neon closes period 2 and sodium opens period 3, at "
                    "opposite ends"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e30",
        "band": "easier",
        "text": "Which of these elements is in period 3?",
        "options": [
            {"text": "Lithium", "correct": False,
             "why": "Lithium opens period 2, the row above"},
            {"text": "Calcium", "correct": False,
             "why": "Calcium is in period 4, the row below"},
            {"text": "Aluminium", "correct": True},
            {"text": "Fluorine", "correct": False,
             "why": "Fluorine is in period 2, directly above chlorine"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e31",
        "band": "easier",
        "text": "Silicon is drawn directly below carbon. Which group are "
                "both of them in?",
        "options": [
            {"text": "Group 2", "correct": False,
             "why": "Group 2 is the second column, and carbon sits further "
                    "across"},
            {"text": "Group 6", "correct": False,
             "why": "Group 6 holds oxygen and sulfur, two columns to the "
                    "right"},
            {"text": "Group 14", "correct": False,
             "why": "Fourteen is silicon's atomic number, not a heading on a "
                    "KS3 table"},
            {"text": "Group 4", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-e32",
        "band": "easier",
        "text": "Calcium is in group 2. Which element sits directly above it "
                "and shares its chemistry?",
        "options": [
            {"text": "Magnesium", "correct": True},
            {"text": "Potassium", "correct": False,
             "why": "Potassium is the square to calcium's left, in group 1"},
            {"text": "Argon", "correct": False,
             "why": "Argon is in the row above but in group 0, not calcium's "
                    "column"},
            {"text": "Sodium", "correct": False,
             "why": "Sodium is in group 1 of period 3, so it is neither "
                    "above nor alongside"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s08",
        "band": "standard",
        "text": "An element's atoms have three electrons in the outermost "
                "shell, with two full shells beneath it. Which group and "
                "which period is the element in?",
        "options": [
            {"text": "Group 2, period 3", "correct": False,
             "why": "Two is how many full shells lie underneath, and it is "
                    "not the outer electron count"},
            {"text": "Group 3, period 3", "correct": True},
            {"text": "Group 3, period 13", "correct": False,
             "why": "Thirteen is the electron total for such an atom, which "
                    "is its atomic number and not a row"},
            {"text": "Group 3, period 2", "correct": False,
             "why": "Two full shells plus the outer one makes three occupied "
                    "shells, so the row is period 3"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s09",
        "band": "standard",
        "text": "An element is in group 6 of period 3. How many electrons "
                "does one of its atoms have altogether?",
        "options": [
            {"text": "6", "correct": False,
             "why": "Six is only the outer shell; the two full shells "
                    "underneath have to be counted as well"},
            {"text": "9", "correct": False,
             "why": "Adding the group to the period counts neither shell "
                    "properly and has no meaning"},
            {"text": "16", "correct": True},
            {"text": "18", "correct": False,
             "why": "Eighteen would need a full outer shell of eight, and "
                    "this element has only six in it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s10",
        "band": "standard",
        "text": "Fluorine and chlorine are in the same group but sit in "
                "different periods. What is the same about their atoms, and "
                "what is different?",
        "options": [
            {"text": "Same number of shells, different outer electrons",
             "correct": False,
             "why": "That is the wrong way round: the column fixes the outer "
                    "count and the row fixes the shells"},
            {"text": "Same number of electrons, different arrangement",
             "correct": False,
             "why": "Their electron totals differ, because each element has "
                    "its own atomic number"},
            {"text": "Everything is the same except the name",
             "correct": False,
             "why": "They are different elements with different atoms; only "
                    "the outer count matches"},
            {"text": "Same outer electrons, different number of shells",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s11",
        "band": "standard",
        "text": "Beryllium is in group 2 of period 2 and magnesium is in "
                "group 2 of period 3. Which of the two has more occupied "
                "electron shells?",
        "options": [
            {"text": "Magnesium", "correct": True},
            {"text": "Beryllium", "correct": False,
             "why": "Beryllium is in the row above, so it uses one shell "
                    "fewer"},
            {"text": "Neither; both are in group 2", "correct": False,
             "why": "The group fixes the outer electrons, and it is the "
                    "period that counts shells"},
            {"text": "It cannot be worked out from their addresses",
             "correct": False,
             "why": "The period number is exactly the number of occupied "
                    "shells, so it can"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s12",
        "band": "standard",
        "text": "Magnesium's oxide has the formula MgO. Calcium is drawn "
                "directly below magnesium. What formula would you expect for "
                "calcium's oxide?",
        "options": [
            {"text": "Ca₂O", "correct": False,
             "why": "Two calcium atoms to one oxygen breaks the ratio the "
                    "column shares"},
            {"text": "CaO", "correct": True},
            {"text": "CaO₂", "correct": False,
             "why": "Two oxygen atoms to one calcium breaks the same ratio "
                    "the other way"},
            {"text": "Ca₂O₃", "correct": False,
             "why": "That is the pattern for group 3, one column further "
                    "across"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s13",
        "band": "standard",
        "text": "Sodium chloride has the formula NaCl. Potassium sits "
                "directly below sodium. What is the formula of potassium "
                "chloride?",
        "options": [
            {"text": "K₂Cl", "correct": False,
             "why": "Doubling the metal changes a ratio the column is "
                    "supposed to keep"},
            {"text": "KCl₂", "correct": False,
             "why": "Doubling the chlorine changes the same ratio the other "
                    "way"},
            {"text": "KCl", "correct": True},
            {"text": "PCl", "correct": False,
             "why": "P is the symbol for phosphorus; potassium's symbol is K"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s14",
        "band": "standard",
        "text": "An atom of an element has 15 electrons. How are they "
                "arranged in shells?",
        "options": [
            {"text": "8,2,5", "correct": False,
             "why": "Shells fill from the inside out, and the innermost one "
                    "holds only two"},
            {"text": "2,2,2,2,2,2,2,1", "correct": False,
             "why": "Only the first shell stops at two; the next ones hold "
                    "eight each"},
            {"text": "2,13", "correct": False,
             "why": "No shell holds thirteen, so a third shell has to be "
                    "started"},
            {"text": "2,8,5", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s15",
        "band": "standard",
        "text": "Boron sits on the staircase in group 3 of period 2. What "
                "does each of those two numbers tell you about a boron atom?",
        "options": [
            {"text": "Three outer electrons, in two occupied shells",
             "correct": True},
            {"text": "Three occupied shells, with two outer electrons",
             "correct": False,
             "why": "The two numbers have been swapped: the group is the "
                    "outer count and the period is the shells"},
            {"text": "Three electrons altogether, in the second shell",
             "correct": False,
             "why": "Three is only the outer shell; boron has five "
                    "electrons altogether"},
            {"text": "Three protons, and two electrons around them",
             "correct": False,
             "why": "Neither number counts protons; that is what the atomic "
                    "number does"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s16",
        "band": "standard",
        "text": "A neon atom has 10 electrons and an argon atom has 18, and "
                "the two elements close their rows in the same column. What "
                "does that difference in total tell you?",
        "options": [
            {"text": "That argon must sit lower in the column than it does",
             "correct": False,
             "why": "A bigger electron total does not move a square across "
                    "or down; the extra electrons fill a new shell"},
            {"text": "That argon has one more occupied shell than neon",
             "correct": True},
            {"text": "That argon has more outer electrons than neon",
             "correct": False,
             "why": "Sharing a column means sharing the outer count; the "
                    "extra electrons fill a new shell"},
            {"text": "That they cannot really be in the same group",
             "correct": False,
             "why": "Elements in one column always have different totals, "
                    "because each has its own atomic number"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s17",
        "band": "standard",
        "text": "Lithium, sodium and potassium all sit in the same column of "
                "the table. What is true of all three of their atoms?",
        "options": [
            {"text": "Each has the same number of electrons altogether",
             "correct": False,
             "why": "Their totals are 3, 11 and 19; it is only the outer "
                    "shell that matches"},
            {"text": "Each has the same number of occupied shells",
             "correct": False,
             "why": "They are in three different rows, so they use two, "
                    "three and four shells"},
            {"text": "Each has one electron in its outer shell",
             "correct": True},
            {"text": "Each has one shell of electrons in total",
             "correct": False,
             "why": "One shell would put all three in period 1, where only "
                    "two elements sit"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s18",
        "band": "standard",
        "text": "Gallium is drawn directly below aluminium in group 3, and "
                "aluminium's oxide is Al₂O₃. What is the most likely formula "
                "for gallium's oxide?",
        "options": [
            {"text": "GaO", "correct": False,
             "why": "A one-to-one ratio is the group 2 pattern, one column "
                    "to the left"},
            {"text": "Ga₃O₂", "correct": False,
             "why": "The numbers have been swapped, which reverses the ratio "
                    "the column shares"},
            {"text": "GaO₃", "correct": False,
             "why": "Dropping the 2 from the metal breaks the ratio "
                    "aluminium sets"},
            {"text": "Ga₂O₃", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s19",
        "band": "standard",
        "text": "An atom has three occupied electron shells and seven "
                "electrons in the outer one. What is its address in the "
                "table?",
        "options": [
            {"text": "Group 7, period 3", "correct": True},
            {"text": "Group 3, period 7", "correct": False,
             "why": "The numbers have been swapped: shells give the period "
                    "and outer electrons give the group"},
            {"text": "Group 7, period 17", "correct": False,
             "why": "Seventeen is the electron total for such an atom, which "
                    "is its atomic number"},
            {"text": "Group 10, period 3", "correct": False,
             "why": "Adding the shells to the outer electrons gives a number "
                    "that names no column"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s20",
        "band": "standard",
        "text": "Why is hydrogen drawn at the top of group 1 when it is not "
                "a metal at all?",
        "options": [
            {"text": "Because it was the first element ever discovered, "
                     "and the squares were filled in from the left in the "
                     "order the elements were found", "correct": False,
             "why": "The squares were not filled in discovery order; "
                    "hydrogen's place follows from its single outer "
                    "electron"},
            {"text": "Because it has one electron in its outer shell, which "
                     "is what the column counts", "correct": True},
            {"text": "Because it is the lightest element and light elements "
                     "go on the left", "correct": False,
             "why": "Mass does not decide the column; helium is light and "
                    "closes the row on the right"},
            {"text": "Because it reacts with water in the way the metals "
                     "below it do", "correct": False,
             "why": "Hydrogen does not react with water like the metals "
                    "below; its square carries a note saying so"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s21",
        "band": "standard",
        "text": "Period 1 holds only two elements while period 2 holds "
                "eight. What explains the difference in length?",
        "options": [
            {"text": "The first two elements were discovered long before the "
                     "others", "correct": False,
             "why": "Discovery dates have no effect on how long a row is"},
            {"text": "Hydrogen and helium are gases, and gases take up less "
                     "of a row", "correct": False,
             "why": "State has nothing to do with it; the row below holds "
                    "gases too"},
            {"text": "The innermost shell is full at two, while the next one "
                     "holds eight", "correct": True},
            {"text": "Six squares of period 1 are simply missing and should "
                     "be filled in", "correct": False,
             "why": "Nothing is missing: no element has two electrons in a "
                    "shell that is already full"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s22",
        "band": "standard",
        "text": "Iron, cobalt and nickel sit side by side along one row of "
                "the block between groups 2 and 3, and they are strikingly "
                "alike. Why does that not break the rule about rows?",
        "options": [
            {"text": "Because those three are really one element under three "
                     "names", "correct": False,
             "why": "They are three separate elements with three different "
                    "atomic numbers"},
            {"text": "Because the rule about rows applies only to metals, "
                     "and there is not a single metal anywhere in the block "
                     "between groups 2 and 3", "correct": False,
             "why": "Every element of that block is a metal, iron and copper "
                    "among them, so the escape does not exist"},
            {"text": "Because the block is set apart from the numbered "
                     "columns for exactly this reason", "correct": True},
            {"text": "Because they are in three different periods despite "
                     "looking adjacent", "correct": False,
             "why": "Side by side along one row means one period, which is "
                    "what makes them interesting"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s23",
        "band": "standard",
        "text": "A student says an element in period 2 cannot have more than "
                "eight electrons altogether. Is the student right?",
        "options": [
            {"text": "No — two shells hold up to ten between them",
             "correct": True},
            {"text": "Yes — eight is the most any atom can hold",
             "correct": False,
             "why": "Eight is one shell's capacity, and atoms further down "
                    "use several shells"},
            {"text": "Yes — the period number sets the electron total",
             "correct": False,
             "why": "The period counts shells; the atomic number is the "
                    "electron total"},
            {"text": "No — a period 2 atom can hold any number at all",
             "correct": False,
             "why": "Two shells set a firm ceiling of ten, so the number is "
                    "not unlimited"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s24",
        "band": "standard",
        "text": "Arsenic is in group 5 of period 4. Which element in period "
                "2 belongs to the same family?",
        "options": [
            {"text": "Carbon", "correct": False,
             "why": "Carbon is in group 4, one column to the left of "
                    "arsenic's"},
            {"text": "Nitrogen", "correct": True},
            {"text": "Neon", "correct": False,
             "why": "Neon closes period 2 in group 0, at the far end of the "
                    "row"},
            {"text": "Potassium", "correct": False,
             "why": "Potassium is in group 1, and it is in period 4 rather "
                    "than period 2"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s25",
        "band": "standard",
        "text": "The main columns are numbered 1 to 7 and then 0, rather "
                "than 1 to 8. What does the 0 mark?",
        "options": [
            {"text": "That its atoms have no electrons in their outer shell "
                     "at all", "correct": False,
             "why": "Those atoms have a full outer shell; an atom with no "
                    "outer electrons is not a thing"},
            {"text": "That the column was added to the table last of all",
             "correct": False,
             "why": "When a column was added does not decide its heading"},
            {"text": "That its atoms already have a complete outer shell",
             "correct": True},
            {"text": "That the column holds no elements of its own",
             "correct": False,
             "why": "It holds helium, neon and argon among others, one in "
                    "every row"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s26",
        "band": "standard",
        "text": "An unfamiliar element has 32 electrons, arranged "
                "2,8,18,4. Which group is it in?",
        "options": [
            {"text": "Group 18", "correct": False,
             "why": "Eighteen is the third shell in this atom, not the outer "
                    "one"},
            {"text": "Group 32", "correct": False,
             "why": "Thirty-two is the electron total, which is the atomic "
                    "number"},
            {"text": "Group 2", "correct": False,
             "why": "Two is the innermost shell, which filled before any of "
                    "the others"},
            {"text": "Group 4", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s27",
        "band": "standard",
        "text": "A student is told only that two elements form compounds "
                "with identical formulae. What can the student conclude "
                "about where the two sit?",
        "options": [
            {"text": "They are in the same group", "correct": True},
            {"text": "They are in the same period", "correct": False,
             "why": "Elements along one row combine in different ratios, "
                    "which is why a period is not a family"},
            {"text": "They are next to each other in the table",
             "correct": False,
             "why": "Neighbouring squares in a row are the pair least likely "
                    "to share a formula"},
            {"text": "They have the same number of electrons",
             "correct": False,
             "why": "Two elements never have the same electron total; each "
                    "has its own atomic number"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s28",
        "band": "standard",
        "text": "Oxygen is in group 6 and sulfur is drawn directly below it. "
                "Water is H₂O. What formula would you expect for the "
                "compound of hydrogen and sulfur?",
        "options": [
            {"text": "HS", "correct": False,
             "why": "One hydrogen to one sulfur is the group 7 pattern, one "
                    "column further across"},
            {"text": "H₂S", "correct": True},
            {"text": "H₂S₂", "correct": False,
             "why": "Doubling both atoms is not the ratio water sets for the "
                    "column"},
            {"text": "HS₆", "correct": False,
             "why": "The group number is the outer electron count, not the "
                    "number of atoms in a formula"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s29",
        "band": "standard",
        "text": "A student writes that fluorine must have seven electrons "
                "altogether because it is in group 7. Fluorine's atomic "
                "number is 9. What has the student confused?",
        "options": [
            {"text": "The mass number with the atomic number",
             "correct": False,
             "why": "Neither of those is 7; the mass number of fluorine is "
                    "about 19"},
            {"text": "The period with the group", "correct": False,
             "why": "Fluorine's period is 2, so swapping the two would give "
                    "an answer of 2 and not 7"},
            {"text": "The outer-shell count with the whole electron count",
             "correct": True},
            {"text": "The number of protons with the number of neutrons",
             "correct": False,
             "why": "Neither count is what the group heading gives, so "
                    "neither is the slip here"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s30",
        "band": "standard",
        "text": "Why does walking across a period take you from a metal on "
                "the left to a non-metal on the right?",
        "options": [
            {"text": "Because the atoms get heavier and heavy elements are "
                     "non-metals", "correct": False,
             "why": "Mass does not decide it; the heaviest elements of all "
                    "are metals"},
            {"text": "Because a new shell is started at every step along "
                     "the row, and the more shells an atom has the less like "
                     "a metal it is", "correct": False,
             "why": "The shell count is fixed along a row, and atoms far "
                    "down the table with many shells are metals"},
            {"text": "Because the squares were arranged that way to keep the "
                     "table tidy", "correct": False,
             "why": "The order follows from the atoms themselves, not from a "
                    "tidying choice"},
            {"text": "Because the number of outer electrons rises by one at "
                     "each step", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s31",
        "band": "standard",
        "text": "Two elements are in the same period. Which statement about "
                "them is definitely true?",
        "options": [
            {"text": "Their electrons occupy the same number of shells",
             "correct": True},
            {"text": "They react in similar ways", "correct": False,
             "why": "Similar reactions come from sharing a column; a row "
                    "runs from metal to non-metal"},
            {"text": "They have the same number of outer electrons",
             "correct": False,
             "why": "The outer count changes at every step along a row, "
                    "which is what makes them differ"},
            {"text": "Their compounds have the same formulae",
             "correct": False,
             "why": "Matching formulae come from a shared column, not from a "
                    "shared row"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-s32",
        "band": "standard",
        "text": "Potassium is in group 1 of period 4 and lithium is in "
                "group 1 of period 2. Which has its outer electron further "
                "from the nucleus?",
        "options": [
            {"text": "Lithium", "correct": False,
             "why": "Lithium uses only two shells, so its outer electron is "
                    "the closer in"},
            {"text": "Potassium", "correct": True},
            {"text": "Neither; both are in group 1", "correct": False,
             "why": "The group fixes how many outer electrons there are, not "
                    "how far out they sit"},
            {"text": "It depends which compound the atom is in",
             "correct": False,
             "why": "The number of shells is a fact about the atom itself, "
                    "whatever it has joined to"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h08",
        "band": "harder",
        "text": "Two students give reasons why one column of the table "
                "shares its chemistry. One says the atoms have similar "
                "masses; the other says they have the same number of outer "
                "electrons. Which reason holds up?",
        "options": [
            {"text": "The first, because mass is what a square's biggest "
                     "number records", "correct": False,
             "why": "Mass climbs steadily down a column while the chemistry "
                    "stays put, so mass cannot be what fixes it"},
            {"text": "Neither, because a column is only a filing decision "
                     "made long ago", "correct": False,
             "why": "The columns record a real fact about the atoms, which "
                    "is why they predict formulae"},
            {"text": "The second, because the outer electrons are the ones "
                     "that react", "correct": True},
            {"text": "Both, because similar masses and similar outer shells "
                     "go together", "correct": False,
             "why": "They do not go together: two elements side by side in a "
                    "row have close masses and different outer counts"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h09",
        "band": "harder",
        "text": "A newly made element is placed in group 2 of period 7 "
                "before anyone has managed to react it with anything. Which "
                "prediction is the table entitled to make about it?",
        "options": [
            {"text": "That its exact melting point follows from the row it is "
                     "in", "correct": False,
             "why": "No row fixes a melting point; the table records "
                    "structure, not a temperature"},
            {"text": "That it is a gas like the other elements low in the "
                     "table", "correct": False,
             "why": "There is no such rule; the elements low in the table "
                    "are overwhelmingly metals"},
            {"text": "Nothing at all until it has been reacted",
             "correct": False,
             "why": "Predicting before reacting is the whole use of the "
                    "table, and it is how missing elements were described"},
            {"text": "That its compounds take the same formulae as "
                     "calcium's", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h10",
        "band": "harder",
        "text": "A periodic table is printed with the column headings "
                "missing, so a student counts squares from the left-hand end "
                "of each row instead. When does that method stop working?",
        "options": [
            {"text": "As soon as the block between groups 2 and 3 appears in "
                     "the row", "correct": True},
            {"text": "Never — the group is just how far along the row a square "
                     "sits", "correct": False,
             "why": "The group is defined by the outer electron count, and "
                    "the inserted block breaks the match with the count of "
                    "squares"},
            {"text": "At the staircase, where the count restarts on the "
                     "non-metal side", "correct": False,
             "why": "The count does not restart anywhere along a row; the "
                    "staircase is drawn over the squares, not between two "
                    "countings"},
            {"text": "In period 1, where that row has gaps drawn in the middle", "correct": False,
             "why": "The gaps are drawn in, so counting the squares as "
                    "printed still lands helium in the last column"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h11",
        "band": "harder",
        "text": "Two elements have atomic numbers 14 and 15, so they are "
                "side-by-side squares in one row. Which single quantity "
                "differs between their atoms, and why does it change their "
                "chemistry so much?",
        "options": [
            {"text": "The number of shells, and the outer shell is the one "
                     "that reacts", "correct": False,
             "why": "Side-by-side squares share a row, so their atoms use "
                    "the same number of shells"},
            {"text": "The number of outer electrons, and those are the ones "
                     "that react", "correct": True},
            {"text": "The number of protons, and protons are what join one "
                     "atom to another", "correct": False,
             "why": "Protons sit in the nucleus and take no part in a "
                    "reaction"},
            {"text": "The mass, and a heavier atom always reacts more "
                     "slowly", "correct": False,
             "why": "Mass does not set how an atom reacts; the outer "
                    "electrons do"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h12",
        "band": "harder",
        "text": "A student suggests writing the elements as one long list in "
                "order of atomic number rather than as a grid. What would "
                "that lose?",
        "options": [
            {"text": "The order of the elements, which only a grid can "
                     "record", "correct": False,
             "why": "A list keeps the order perfectly; the order is the one "
                    "thing it does well"},
            {"text": "The atomic numbers themselves, which are printed on "
                     "the squares", "correct": False,
             "why": "Each entry would still carry its number; nothing about "
                    "a list hides it"},
            {"text": "The columns, which stack elements with matching outer "
                     "shells", "correct": True},
            {"text": "The symbols, which stop meaning anything at all once "
                     "they leave a square", "correct": False,
             "why": "A symbol means the same wherever it is written; it does "
                    "not depend on a grid"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h13",
        "band": "harder",
        "text": "An atom has an atomic number of 14. Using only the filling "
                "rule 2, 8, 8, how many electrons are in its outer shell and "
                "how many shells are occupied?",
        "options": [
            {"text": "Fourteen outer electrons in one shell", "correct": False,
             "why": "No shell holds fourteen; the filling rule stops the "
                    "first at two and the second at eight"},
            {"text": "Eight outer electrons in two shells", "correct": False,
             "why": "Filling two and then eight uses only ten of the "
                    "fourteen, so a third shell has to be started"},
            {"text": "Two outer electrons in eight shells", "correct": False,
             "why": "The numbers of the rule have been read as a count of "
                    "shells rather than as capacities"},
            {"text": "Four outer electrons in three shells", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h14",
        "band": "harder",
        "text": "Helium has only two electrons in its outer shell, yet the "
                "table starts a whole new row after it. Why?",
        "options": [
            {"text": "Because its first shell is full at two, so the next "
                     "electron must start a new one", "correct": True},
            {"text": "Because helium is a gas and a row cannot end on a "
                     "solid", "correct": False,
             "why": "Every row ends on a gas of group 0, so state is not "
                    "what breaks the row"},
            {"text": "Because only two elements were known when the first "
                     "row was drawn", "correct": False,
             "why": "The length of a row follows from the shells, not from "
                    "how much anyone knew"},
            {"text": "Because the six missing squares of that row hold "
                     "elements nobody has found", "correct": False,
             "why": "Those squares can never be filled: no element has a "
                    "third or fourth electron in a shell that is full at two"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h15",
        "band": "harder",
        "text": "An element in period 3 forms a chloride with the formula "
                "XCl₄. Which group is it in, and which element is it?",
        "options": [
            {"text": "Group 3, and the element is aluminium", "correct": False,
             "why": "A group 3 element pairs with three chlorines, not four, "
                    "so the formula would be XCl₃"},
            {"text": "Group 4, and the element is silicon", "correct": True},
            {"text": "Group 4, and the element is carbon", "correct": False,
             "why": "Carbon is in group 4 but in period 2, one row above the "
                    "one described"},
            {"text": "Group 7, and the element is chlorine", "correct": False,
             "why": "Chlorine is the other half of the compound, so it "
                    "cannot also be the element joining to it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h16",
        "band": "harder",
        "text": "A student predicts that an element in group 7 of period 6 "
                "will be a metal, because the elements low down in the table "
                "are metals. What is wrong with the reasoning?",
        "options": [
            {"text": "Nothing is wrong; every element below period 4 is a "
                     "metal", "correct": False,
             "why": "Iodine and radon both sit below period 4 and neither "
                    "of them is a metal"},
            {"text": "The period was misread; group 7 of period 6 is not a "
                     "real square", "correct": False,
             "why": "It is a real square: period 6 runs the full width of "
                    "the table"},
            {"text": "The column decides the family, and group 7 sits on the "
                     "non-metal side", "correct": True},
            {"text": "The prediction should have used the mass instead, "
                     "which is the reliable guide", "correct": False,
             "why": "Mass is no guide to metal or non-metal; some of the "
                    "heaviest non-metals outweigh light metals"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h17",
        "band": "harder",
        "text": "Two elements each have four electrons in the outer shell, "
                "but one uses two occupied shells and the other uses three. "
                "Which of their properties should match, and which should "
                "not?",
        "options": [
            {"text": "Their atomic numbers should match, but not their "
                     "formulae", "correct": False,
             "why": "No two elements share an atomic number; it is what "
                    "tells them apart"},
            {"text": "Their number of shells should match, but not their "
                     "outer counts", "correct": False,
             "why": "That is the opposite of what they were given as: the "
                    "outer counts match and the shell counts differ"},
            {"text": "Nothing should match, because they are different "
                     "elements", "correct": False,
             "why": "A shared outer count is exactly the thing that makes a "
                    "column a family"},
            {"text": "The formulae of their compounds should match, but not "
                     "the size of their atoms", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h18",
        "band": "harder",
        "text": "A student learns by heart where twenty elements sit but "
                "cannot say what a group means. Where will that first let "
                "them down?",
        "options": [
            {"text": "The moment they are asked about an element outside the "
                     "twenty", "correct": True},
            {"text": "Never, because knowing where the squares are is all a "
                     "group is", "correct": False,
             "why": "A group is a shared count of outer electrons; the "
                    "positions are only where that shows up"},
            {"text": "As soon as they are asked to name any of the twenty",
             "correct": False,
             "why": "Naming the twenty is precisely what the memorising does "
                    "deliver"},
            {"text": "Only if the table in front of them is drawn a "
                     "different way round", "correct": False,
             "why": "The memorised positions would survive a redrawing; it "
                    "is unfamiliar elements that break the method"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h19",
        "band": "harder",
        "text": "One atom's electrons are arranged 2,8,7 and another's are "
                "arranged 2,8,18,7. Explain how they can be in the same "
                "group when one has far more electrons.",
        "options": [
            {"text": "They cannot be; the electron totals settle which "
                     "column an atom goes in", "correct": False,
             "why": "The total is the atomic number, and every element in a "
                    "column has a different one"},
            {"text": "Only the outer shell is counted, and both end in seven",
             "correct": True},
            {"text": "The extra ten electrons are ignored because they lie "
                     "outside the outer shell", "correct": False,
             "why": "They are counted in the total and sit inside the outer "
                    "shell, not beyond it"},
            {"text": "Both have four shells once the empty ones are included",
             "correct": False,
             "why": "One uses three shells and the other four; a shell with "
                    "nothing in it is not occupied"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h20",
        "band": "harder",
        "text": "Aluminium and silicon are next-door squares in period 3. "
                "Aluminium's oxide is Al₂O₃ and silicon's is SiO₂. What does "
                "that pair of formulae show?",
        "options": [
            {"text": "That one of the two formulae must have been written "
                     "down wrongly", "correct": False,
             "why": "Both are correct; different groups genuinely combine in "
                    "different ratios"},
            {"text": "That oxygen joins different elements at random",
             "correct": False,
             "why": "There is nothing random about it: the ratio follows the "
                    "outer electron count of the element oxygen joins"},
            {"text": "That neighbours in a row combine in different ratios, "
                     "so a period is no family", "correct": True},
            {"text": "That aluminium and silicon must sit in the same group "
                     "after all", "correct": False,
             "why": "Sharing a group would mean sharing a ratio, and these "
                    "two do not share one"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h21",
        "band": "harder",
        "text": "One element is in group 4 of period 2 and another is in "
                "group 2 of period 4. A student calls them the same thing "
                "the other way round. Why is that wrong?",
        "options": [
            {"text": "Because the two addresses name the same square read "
                     "from two ends", "correct": False,
             "why": "They name two different squares; one is high on the "
                    "table and the other is low and to the left"},
            {"text": "Because group numbers and period numbers cannot be "
                     "compared at all", "correct": False,
             "why": "They can be compared perfectly well; they simply count "
                    "different things"},
            {"text": "Because the numbers match only by chance, and no two "
                     "elements in the table are ever allowed to carry the "
                     "same pair of numbers in either order", "correct": False,
             "why": "Plenty of squares share a pair of numbers in the other "
                    "order; nothing forbids it, and the two addresses simply "
                    "mean different things"},
            {"text": "Because one counts outer electrons and the other "
                     "counts shells, so swapping them names a different "
                     "element", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h22",
        "band": "harder",
        "text": "The formula of an element's oxide can usually be predicted "
                "from the element directly above it, but not from the one "
                "directly to its left. Why the difference?",
        "options": [
            {"text": "The one above shares its outer electron count and the "
                     "one beside it does not", "correct": True},
            {"text": "The one above has a similar mass and the one beside it "
                     "does not", "correct": False,
             "why": "The element beside it is the closer in mass; the one "
                    "above is markedly lighter"},
            {"text": "The one above was discovered first and is the better "
                     "understood", "correct": False,
             "why": "How long an element has been known does not change what "
                    "its atoms do"},
            {"text": "The one above is in the same period and the one beside "
                     "it is not", "correct": False,
             "why": "That is backwards: the element beside it shares its "
                    "period and the one above does not"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h23",
        "band": "harder",
        "text": "Helium carries two outer electrons, the same number as the "
                "group 2 metals, yet it is placed in the last column "
                "instead. What does that show about how the table is built?",
        "options": [
            {"text": "That some squares were placed by guesswork and never "
                     "corrected", "correct": False,
             "why": "Helium's placement is deliberate and is the one that "
                    "makes its column consistent"},
            {"text": "That a complete outer shell, not a bare count, decides "
                     "the last column", "correct": True},
            {"text": "That helium has no outer electrons once the shell is "
                     "counted properly", "correct": False,
             "why": "It has two, and they sit in a shell that is full at two"},
            {"text": "That the group 2 metals should have been placed in the "
                     "last column too", "correct": False,
             "why": "Their outer shells are far from full, so they belong "
                    "where the count puts them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h24",
        "band": "harder",
        "text": "Sodium chloride is NaCl and potassium bromide is KBr. Both "
                "join a group 1 element to a group 7 one. What formula would "
                "you expect for lithium fluoride?",
        "options": [
            {"text": "Li₂F", "correct": False,
             "why": "Doubling the group 1 element breaks the one-to-one "
                    "ratio both examples set"},
            {"text": "LiF₇", "correct": False,
             "why": "The 7 is the group heading, which counts outer "
                    "electrons and not atoms in a formula"},
            {"text": "LiF", "correct": True},
            {"text": "LiF₂", "correct": False,
             "why": "Two of the group 7 element is the pattern for a group 2 "
                    "metal, one column across"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h25",
        "band": "harder",
        "text": "Two students are each given one fact about an unknown "
                "element. One is told its atomic number and the other is "
                "told its mass number. Which of them can work out its group?",
        "options": [
            {"text": "The one with the mass number, because mass decides "
                     "where a square sits", "correct": False,
             "why": "Mass does not fix a column; two pairs of elements even "
                    "run out of mass order in the table"},
            {"text": "Both of them, because either number can be turned into "
                     "the other", "correct": False,
             "why": "Neither number can be worked out from the other; they "
                    "count different particles"},
            {"text": "Neither of them, because the group has to be read off "
                     "a printed table", "correct": False,
             "why": "The group follows from filling the shells, so it can be "
                    "worked out without a table"},
            {"text": "The one with the atomic number, because it fixes how "
                     "the shells fill", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h26",
        "band": "harder",
        "text": "A student reasons that because the table has eight main "
                "columns, every atom must carry eight outer electrons. What "
                "is the fault?",
        "options": [
            {"text": "Eight is the most an outer shell holds, not what every "
                     "atom carries", "correct": True},
            {"text": "The table has seven main columns, so the number itself "
                     "is wrong", "correct": False,
             "why": "There are eight main columns; the fault is in what the "
                    "student does with the number"},
            {"text": "Outer electrons are not counted in whole numbers at "
                     "all", "correct": False,
             "why": "They are counted in whole numbers, and that count is "
                    "the group heading"},
            {"text": "The columns count shells rather than electrons, so "
                     "neither number applies", "correct": False,
             "why": "It is the rows that count shells; the columns do count "
                    "outer electrons"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h27",
        "band": "harder",
        "text": "Carbon is the element living things are built around and "
                "silicon is what microchips are cut from, and the two share "
                "a column. What does the shared column let you predict, and "
                "what does it not?",
        "options": [
            {"text": "It predicts what each is used for, but not their "
                     "formulae", "correct": False,
             "why": "That is the wrong way round; uses depend on far more "
                    "than the outer electron count"},
            {"text": "It predicts the formulae of their compounds, but not "
                     "what they are used for", "correct": True},
            {"text": "It predicts both, because a column fixes everything "
                     "about a member", "correct": False,
             "why": "A column fixes the outer electron count and what "
                    "follows from it, which is not everything"},
            {"text": "It predicts neither, because the two are used in "
                     "completely different ways", "correct": False,
             "why": "Different uses do not cancel the shared ratio; both "
                    "form an oxide of the same shape"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h28",
        "band": "harder",
        "text": "Why is an element's address in the table a better guide to "
                "its chemistry than a single measured property such as its "
                "melting point?",
        "options": [
            {"text": "Because a melting point is too hard to measure "
                     "accurately", "correct": False,
             "why": "Melting points are measured very accurately; the "
                    "trouble is what they fail to predict"},
            {"text": "Because an address is a number and a melting point is "
                     "not", "correct": False,
             "why": "A melting point is a number too; being numerical is not "
                    "what makes the address useful"},
            {"text": "Because the address carries the outer electron count, "
                     "which is what reacts", "correct": True},
            {"text": "Because melting points are identical for every "
                     "element in one group, so the figure can never tell two "
                     "members of a column apart", "correct": False,
             "why": "They differ widely within a column, which is part of "
                    "why a melting point predicts so little"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h29",
        "band": "harder",
        "text": "A poster prints the table turned on its side, so the "
                "families run across the page and the periods run down it. "
                "Does that change any of the chemistry it records?",
        "options": [
            {"text": "Yes, because a group heading can only ever be "
                     "written above a column, so turning the page leaves "
                     "every number with nothing left to label", "correct": False,
             "why": "A heading can be written at the end of a row just as "
                    "well; the numbering labels the families themselves"},
            {"text": "Yes, because turning it swaps every element's group "
                     "with its period", "correct": False,
             "why": "Nothing is swapped: each element keeps the family and "
                    "the shell count it had"},
            {"text": "No, because how a table is arranged never carries any "
                     "information", "correct": False,
             "why": "The arrangement is the whole content of the table; a "
                    "plain alphabetical list would carry none of it"},
            {"text": "No, because the same families are kept together and "
                     "that is what the table records", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h30",
        "band": "harder",
        "text": "A student writes that a period is just a group lying on its "
                "side. Which correction is the sharpest?",
        "options": [
            {"text": "A period holds elements with the same shell count and "
                     "quite different chemistry", "correct": True},
            {"text": "A period is a group with its elements listed in the "
                     "opposite order", "correct": False,
             "why": "Reversing an order does not turn a family into a row; "
                    "the two hold different sets of elements"},
            {"text": "A period is simply a longer group, since rows hold "
                     "more squares", "correct": False,
             "why": "Length is not the difference; a row and a column record "
                    "two different facts about an atom"},
            {"text": "A period is a group drawn for the elements left over "
                     "once every family in the table has already been filled "
                     "in", "correct": False,
             "why": "Nothing is left over: every element sits in a row and "
                    "in a column, so none is without a family"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h31",
        "band": "harder",
        "text": "Magnesium chloride is MgCl₂ and calcium chloride is CaCl₂. "
                "Strontium is the next element down that column. How strong "
                "is the prediction that strontium chloride is SrCl₂?",
        "options": [
            {"text": "Weak, because two examples can never support a third",
             "correct": False,
             "why": "Two members of one column agreeing is exactly the "
                    "evidence a family claim rests on"},
            {"text": "Strong, because two members of the column already "
                     "share the ratio", "correct": True},
            {"text": "Weak, because strontium is heavier and heavier atoms "
                     "take more chlorine", "correct": False,
             "why": "Mass does not change a combining ratio; the outer "
                    "electron count does, and it is unchanged"},
            {"text": "Strong, because every chloride in the table has two "
                     "chlorine atoms", "correct": False,
             "why": "Sodium chloride has one, so that is plainly not a rule "
                    "of the whole table"},
        ],
        "figure": None,
    },
    {
        "id": "c8-03-h32",
        "band": "harder",
        "text": "Somebody proposes a new table with the elements arranged "
                "in order of melting point instead. What would such a table "
                "fail to do?",
        "options": [
            {"text": "Record each element's melting point", "correct": False,
             "why": "Melting point is the one thing that arrangement would "
                    "record perfectly"},
            {"text": "Give every element a place of its own", "correct": False,
             "why": "Every element has a melting point, so every element "
                    "would still get a place"},
            {"text": "Put elements that react alike into the same column",
             "correct": True},
            {"text": "Keep the elements in a definite and repeatable order",
             "correct": False,
             "why": "Melting points give a perfectly definite order; the "
                    "trouble is what that order groups together"},
        ],
        "figure": None,
    },
]
