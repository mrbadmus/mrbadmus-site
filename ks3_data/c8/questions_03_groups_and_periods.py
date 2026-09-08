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
]
