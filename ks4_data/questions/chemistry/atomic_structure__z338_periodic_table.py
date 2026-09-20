"""Chemistry · Atomic structure and the periodic table — the periodic table ·
the MRB-338 expansion.

Fifty-two rows on the table as a map: what a column is, what a row is, and
what a pupil can read off a position once they know which is which. The weight
falls on moving between position and electronic structure in both directions —
group to outer electrons, period to occupied shells, position to ion charge
and to the formula of a chloride or an oxide — and on the misconception the
lesson names, which is reading the group number off a period or the period
number off a count of outer electrons.

Group-by-group chemistry belongs to the `group-0`, `group-1`, `group-7` and
`transition-metals` leaves, and the history of the ordering to
`development-periodic-table`; this leaf stays on the map itself.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-periodic-table-e05",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the vertical columns of the periodic table.",
        "options": [
            "Groups",
            "Periods",
            "Shells",
            "Blocks",
        ],
        "correct_index": 0,
        "why": "The columns are groups; elements in one group share the same "
               "number of outer electrons.",
    },
    {
        "id": "ks4-periodic-table-e06",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element sits in Group 6. Deduce how many electrons occupy "
                "its outer shell.",
        "options": [
            "2",
            "6",
            "12",
            "8",
        ],
        "correct_index": 1,
        "why": "For the main groups the group number gives the number of "
               "outer electrons, so Group 6 means 6.",
    },
    {
        "id": "ks4-periodic-table-e07",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which group sits at the right-hand edge of the "
                "periodic table.",
        "options": [
            "Group 1",
            "Group 7",
            "Group 0",
            "Group 2",
        ],
        "correct_index": 2,
        "why": "Group 0, the noble gases, closes each row at the right-hand "
               "edge of the table.",
    },
    {
        "id": "ks4-periodic-table-e08",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element lies in Period 4. Deduce what that tells you "
                "about its atoms.",
        "options": [
            "They hold four electrons in the outer shell",
            "They hold four protons in the nucleus",
            "They share their properties with four other elements",
            "They have four electron shells that hold electrons",
        ],
        "correct_index": 3,
        "why": "Each new period begins as electrons start to fill a new "
               "shell, so the period number counts the occupied shells.",
    },
    {
        "id": "ks4-periodic-table-e09",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Elements in one group of the periodic table share which "
                "feature?",
        "options": [
            "The same number of electron shells in their atoms",
            "The same number of outer electrons in their atoms",
            "The same relative atomic mass",
            "The same number of neutrons in their atoms",
        ],
        "correct_index": 1,
        "why": "A group is a column of elements with matching outer-shell "
               "counts, which is why their chemistry is alike.",
    },
    {
        "id": "ks4-periodic-table-e10",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many elements lie in Period 2 of the periodic "
                "table.",
        "options": [
            "2",
            "18",
            "8",
            "20",
        ],
        "correct_index": 2,
        "why": "Period 2 runs from lithium to neon, which is eight elements, "
               "matching the eight electrons the second shell holds.",
    },
    {
        "id": "ks4-periodic-table-e11",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the group whose elements are known as the alkali "
                "metals.",
        "options": [
            "Group 0",
            "Group 2",
            "Group 6",
            "Group 1",
        ],
        "correct_index": 3,
        "why": "Group 1 elements are the alkali metals, so called because "
               "their hydroxides dissolve to give alkaline solutions.",
    },
    {
        "id": "ks4-periodic-table-e12",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether most of the known elements are metals or "
                "non-metals.",
        "options": [
            "Most are metals",
            "Most are non-metals",
            "The two are present in equal numbers",
            "Most are metalloids",
        ],
        "correct_index": 0,
        "why": "The metals fill the left-hand side and the whole central "
               "block, leaving the non-metals a small area at the top right.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-periodic-table-s05",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has 3 occupied electron shells and 7 electrons in "
                "its outer shell. Determine its group and its period.",
        "options": [
            "Group 7 and Period 3",
            "Group 3 and Period 7",
            "Group 7 and Period 7",
            "Group 10 and Period 3",
        ],
        "correct_index": 0,
        "why": "Outer electrons give the group and occupied shells give the "
               "period, so it is Group 7, Period 3 — chlorine.",
    },
    {
        "id": "ks4-periodic-table-s06",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the elements at the two ends of Period 3 "
                "behave so differently from one another.",
        "options": [
            "Their atoms hold quite different numbers of occupied shells, "
            "and that is what sets the chemistry",
            "Sodium has a single outer electron to shed, while argon's outer "
            "shell is already full",
            "Sodium is far heavier than argon, and a heavy atom reacts much "
            "more readily than a light one",
            "Argon has a single outer electron to shed, while sodium's outer "
            "shell is already full",
        ],
        "correct_index": 1,
        "why": "A row runs from one outer electron to eight, so its two ends "
               "are the extremes of reactive metal and inert gas.",
    },
    {
        "id": "ks4-periodic-table-s07",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the group of an element whose atoms form ions "
                "carrying a 3- charge.",
        "options": [
            "Group 3",
            "Group 7",
            "Group 5",
            "Group 6",
        ],
        "correct_index": 2,
        "why": "An atom that gains three electrons is three short of a full "
               "shell, so it has 5 outer electrons and sits in Group 5.",
    },
    {
        "id": "ks4-periodic-table-s08",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why every element in Period 3 has three occupied "
                "electron shells.",
        "options": [
            "Because each of them has three electrons in the outer shell of "
            "its atoms",
            "Because a period holds exactly the same number of elements as a "
            "shell holds electrons, and the third shell holds eight",
            "Because the third shell of each of them is completely full of "
            "electrons",
            "Because a new period starts as electrons begin filling a new "
            "shell, so Period 3 is the third shell filling",
        ],
        "correct_index": 3,
        "why": "Period number counts occupied shells, so every Period 3 atom "
               "has electrons in shells one, two and three.",
    },
    {
        "id": "ks4-periodic-table-s09",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element has the arrangement 2.8.8.7. Deduce which known "
                "element it resembles most closely in its chemistry.",
        "options": [
            "Chlorine, 2.8.7",
            "Argon, 2.8.8",
            "Potassium, 2.8.8.1",
            "Silicon, 2.8.4",
        ],
        "correct_index": 0,
        "why": "Seven outer electrons puts it in Group 7 with chlorine, and "
               "the group sets the chemistry.",
    },
    {
        "id": "ks4-periodic-table-s10",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict whether an element near the left of Period 3 or one "
                "near the right is the more likely to conduct electricity.",
        "options": [
            "The one near the right, because a nearly full outer shell holds "
            "its electrons where a current can reach them",
            "The one near the left, because it is a metal and its outer "
            "electrons are free to move through the structure",
            "Both equally, because every element in a period has the same "
            "number of occupied shells",
            "Neither, because conduction depends on the period rather than "
            "on the place within it",
        ],
        "correct_index": 1,
        "why": "The left of a period is metallic, and a metal conducts "
               "because its delocalised electrons can move.",
    },
    {
        "id": "ks4-periodic-table-s11",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the elements are set out by structure rather "
                "than listed in alphabetical order.",
        "options": [
            "Because an alphabetical list would place the metals and the "
            "non-metals side by side",
            "Because the names of the elements differ from language to "
            "language",
            "Because a position in the table fixes the electron arrangement, "
            "and that is what sets an element's chemistry",
            "Because the elements happen to have been discovered in the very "
            "order in which they now appear across the table",
        ],
        "correct_index": 2,
        "why": "The arrangement makes the pattern in the properties visible; "
               "an alphabetical list would hide it completely.",
    },
    {
        "id": "ks4-periodic-table-s12",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two elements in the same period do not have "
                "similar chemical properties.",
        "options": [
            "They hold different numbers of neutrons, and neutrons decide how "
            "an atom reacts with others",
            "They have different numbers of occupied shells, which is what "
            "decides the chemistry",
            "They have different relative atomic masses, and mass governs the "
            "way an element behaves",
            "They have different numbers of outer electrons, and it is the "
            "outer shell that sets the chemistry",
        ],
        "correct_index": 3,
        "why": "A period shares a shell count but runs through every outer "
               "electron count from 1 to 8.",
    },
    {
        "id": "ks4-periodic-table-s13",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict which of lithium, sodium and potassium has the "
                "largest atoms.",
        "options": [
            "Potassium, because it has the most occupied shells of the three",
            "Lithium, because its outer electron is held most tightly of the "
            "three and is therefore drawn in closest",
            "Sodium, because it sits in the middle of the three and takes an "
            "average of their two sizes",
            "All three are the same size, because all three are in Group 1",
        ],
        "correct_index": 0,
        "why": "Each step down a group adds a shell, so potassium's four "
               "shells make it the largest of the three.",
    },
    {
        "id": "ks4-periodic-table-s14",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the atomic number of the elements "
                "going from left to right along a period.",
        "options": [
            "It falls by one at each step, which is why the elements get "
            "lighter towards the right",
            "It rises by one at each step",
            "It stays the same across a period and changes only down a group",
            "It rises by eight at each step",
        ],
        "correct_index": 1,
        "why": "The table is ordered by atomic number, so each element along "
               "a row has one more proton than the one before it.",
    },
    {
        "id": "ks4-periodic-table-s15",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a Group 0 element is numbered 0 even though its "
                "atoms hold 8 outer electrons.",
        "options": [
            "Because 0 records the number of shells its atoms have to spare",
            "Because the group was numbered before anyone had counted the "
            "electrons in its atoms",
            "Because the outer shell is full, so no electrons at all are "
            "available to be lost or gained",
            "Because these elements have no outer shell at all until they have "
            "been cooled right down to a liquid",
        ],
        "correct_index": 2,
        "why": "The 0 records what the group does in a reaction — nothing — "
               "because the full shell leaves no electrons in play.",
    },
    {
        "id": "ks4-periodic-table-s16",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of occupied electron shells in an atom "
                "from Period 2 with one from Period 5.",
        "options": [
            "Two and five, but counted from the outside in rather than from "
            "the nucleus outwards",
            "Five and two, because the shells are numbered from the outermost "
            "shell inwards",
            "Both have two",
            "Two and five",
        ],
        "correct_index": 3,
        "why": "The period number is the count of occupied shells, so Period "
               "2 gives two and Period 5 gives five.",
    },
    {
        "id": "ks4-periodic-table-s17",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newly made element is placed in Group 1, Period 7. Predict "
                "two of its chemical properties.",
        "options": [
            "A very reactive metal that forms a 1+ ion",
            "An unreactive gas that forms no ions of any kind",
            "A brittle non-metal that forms a 1- ion",
            "A hard, dense metal that forms coloured compounds",
        ],
        "correct_index": 0,
        "why": "Group 1 means one outer electron, lost to give a 1+ ion, and "
               "Period 7 means it lies far down the most reactive group.",
    },
    {
        "id": "ks4-periodic-table-s18",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to the elements of the long central "
                "block lying between Groups 2 and 3.",
        "options": [
            "The alkaline earth metals",
            "The transition metals",
            "The metalloids",
            "The noble metals",
        ],
        "correct_index": 1,
        "why": "The block between Groups 2 and 3 is the transition metals — "
               "iron, copper, nickel and the rest.",
    },
    {
        "id": "ks4-periodic-table-s19",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says magnesium is in Period 2 because its atoms "
                "have 2 outer electrons. Explain the error.",
        "options": [
            "Magnesium has 2 outer electrons but they lie in the second "
            "shell, so the period is still 2",
            "Magnesium has 3 outer electrons rather than 2, which puts it in "
            "Period 3 of the table",
            "Outer electrons give the group; magnesium is 2.8.2, so three "
            "shells put it in Period 3",
            "Magnesium is placed by its relative atomic mass of 24, which is "
            "what fixes its period",
        ],
        "correct_index": 2,
        "why": "Two outer electrons make it Group 2; the three occupied "
               "shells of 2.8.2 make it Period 3.",
    },
    {
        "id": "ks4-periodic-table-s20",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compound has the formula XCl2, and chlorine forms 1- ions "
                "in it. Deduce the group X belongs to.",
        "options": [
            "Group 1",
            "Group 7",
            "Group 4",
            "Group 2",
        ],
        "correct_index": 3,
        "why": "Two chloride ions carry 2- between them, so one X ion must "
               "carry 2+ and X has two outer electrons to lose.",
    },
    {
        "id": "ks4-periodic-table-s21",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the ions formed by an element in Group 1 with those "
                "formed by an element in Group 7.",
        "options": [
            "Group 1 gives 1+ ions and Group 7 gives 1- ions",
            "Group 1 gives 1- ions and Group 7 gives 1+ ions, since a metal "
            "picks up the electrons a non-metal sheds",
            "Both give 1+ ions, because both sit at the outside edges of the "
            "table where electrons are lost",
            "Group 1 gives 1+ ions and Group 7 gives 7- ions",
        ],
        "correct_index": 0,
        "why": "One outer electron is lost to give 1+; seven outer electrons "
               "means one is gained, giving 1-.",
    },
    {
        "id": "ks4-periodic-table-s22",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which of the arrangements 2.3, 2.8.3 and 2.8.8.3 "
                "belongs to an element of Period 3.",
        "options": [
            "2.3",
            "2.8.3",
            "2.8.8.3",
            "None of the three, because a Period 3 atom has 3 outer electrons",
        ],
        "correct_index": 1,
        "why": "Period 3 means three occupied shells, and only 2.8.3 is "
               "written with three numbers.",
    },
    {
        "id": "ks4-periodic-table-s23",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to elements such as silicon and "
                "germanium, which show some properties of metals and some of "
                "non-metals.",
        "options": [
            "Transition metals",
            "Noble gases",
            "Metalloids",
            "Halogens",
        ],
        "correct_index": 2,
        "why": "Metalloids lie along the staircase that divides the metals "
               "from the non-metals and behave partly like each.",
    },
    {
        "id": "ks4-periodic-table-s24",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an element's position in the periodic table "
                "says more about its chemistry than its relative atomic mass "
                "does.",
        "options": [
            "Because relative atomic mass is measured far less accurately "
            "than a position can be read",
            "Because relative atomic mass changes from one sample of an "
            "element to the next",
            "Because the mass of an atom has no connection to any of its "
            "physical properties",
            "Because a position fixes the number of outer electrons and the "
            "number of shells, and reactions are decided by the electrons",
        ],
        "correct_index": 3,
        "why": "Two elements of very similar mass can behave completely "
               "differently; two in one group behave alike.",
    },
    {
        "id": "ks4-periodic-table-s25",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the number of outer electrons in an atom of a "
                "Group 0 element other than helium.",
        "options": [
            "8",
            "0",
            "2",
            "18",
        ],
        "correct_index": 0,
        "why": "Neon, argon and the rest have full outer shells of 8; helium "
               "is the exception, with a full first shell of 2.",
    },
    {
        "id": "ks4-periodic-table-s26",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the metallic character of the "
                "elements going down a group.",
        "options": [
            "It weakens",
            "It grows stronger",
            "It stays the same",
            "It grows stronger then weakens again",
        ],
        "correct_index": 1,
        "why": "The outer electrons sit further from the nucleus with each "
               "extra shell and are lost more readily, which is metallic "
               "behaviour.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-periodic-table-h05",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Element Q lies in Group 2 and Period 3. Predict the formula "
                "of the compound it forms with chlorine.",
        "options": [
            "QCl",
            "Q2Cl",
            "QCl2",
            "QCl3",
        ],
        "correct_index": 2,
        "why": "Q loses its two outer electrons to form Q2+, and each "
               "chlorine takes one, so two chlorines are needed.",
    },
    {
        "id": "ks4-periodic-table-h06",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare an element in Group 6, Period 2 with an element in "
                "Group 6, Period 3.",
        "options": [
            "Both have two occupied shells, but the second has more outer "
            "electrons than the first",
            "The two have different numbers of outer electrons but the same "
            "number of occupied shells",
            "Both have six occupied shells and six outer electrons, since "
            "group and period match in Group 6",
            "Both have six outer electrons, but the second has three occupied "
            "shells against the first's two",
        ],
        "correct_index": 3,
        "why": "The shared group fixes the outer electrons at six; the "
               "different periods fix the shell counts at two and three.",
    },
    {
        "id": "ks4-periodic-table-h07",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element X forms an oxide with the formula X2O3, and an "
                "oxide ion carries a 2- charge. Deduce the group of X.",
        "options": [
            "Group 3",
            "Group 2",
            "Group 6",
            "Group 5",
        ],
        "correct_index": 0,
        "why": "Three oxide ions carry 6- in total, so two X ions carry 6+, "
               "which is 3+ each and three outer electrons lost.",
    },
    {
        "id": "ks4-periodic-table-h08",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict which is the more reactive non-metal, an element in "
                "Group 7 Period 2 or one in Group 7 Period 4, and explain.",
        "options": [
            "The Period 4 element, because its extra shells give it more "
            "electrons with which to attract another atom",
            "The Period 2 element, because its outer shell is nearer the "
            "nucleus and pulls an incoming electron in more strongly",
            "The Period 4 element, because a larger atom offers a larger "
            "target for an incoming electron to reach",
            "Neither, because both need a single electron and so both are "
            "equally reactive",
        ],
        "correct_index": 1,
        "why": "Reactivity falls down Group 7: the further the outer shell, "
               "the weaker the attraction for an extra electron.",
    },
    {
        "id": "ks4-periodic-table-h09",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that every element in one group has "
                "identical properties.",
        "options": [
            "Sound — elements in a group have the same outer electron count "
            "and therefore behave identically",
            "Sound, so long as the comparison is limited to the metals within "
            "a group and leaves out the non-metals altogether",
            "Unsound — the chemistry is similar but never identical, since "
            "reactivity and physical properties shift down a group",
            "Unsound — elements in a group have nothing chemically in common "
            "with one another at all",
        ],
        "correct_index": 2,
        "why": "Lithium and potassium both react with water to give a 1+ ion, "
               "but potassium does it far more vigorously.",
    },
    {
        "id": "ks4-periodic-table-h10",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element forms 2- ions and its atoms have three occupied "
                "shells. Determine its atomic number.",
        "options": [
            "8",
            "18",
            "14",
            "16",
        ],
        "correct_index": 3,
        "why": "Gaining two electrons means six outer electrons, so the "
               "arrangement is 2.8.6 and the atomic number is 16.",
    },
    {
        "id": "ks4-periodic-table-h11",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the group number gives the size of the ion "
                "charge for Groups 1, 2 and 3 but not for Groups 5, 6 and 7.",
        "options": [
            "Groups 1 to 3 lose their outer electrons, while Groups 5 to 7 "
            "gain enough to fill the shell, which is 8 minus the group number",
            "Groups 1 to 3 are metals, and a metal is the one sort of element "
            "that forms ions",
            "Groups 5 to 7 form no ions, so no charge can be worked out for "
            "any of them",
            "Groups 5 to 7 lose electrons too, but they lose more of them "
            "than the group number suggests",
        ],
        "correct_index": 0,
        "why": "A Group 6 atom needs two electrons, not six, so it forms a 2- "
               "ion rather than a 6- one.",
    },
    {
        "id": "ks4-periodic-table-h12",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an element whose atoms hold eight outer "
                "electrons is placed at the end of a row rather than at the "
                "start of one.",
        "options": [
            "Because the heaviest element of a row is put last, and a full "
            "shell makes for a heavy atom",
            "Because a full shell means the next electron starts a new shell, "
            "and a new shell is a new row",
            "Because the elements at the end of a row were the last to be "
            "discovered, and these were found late",
            "Because a row is ordered by reactivity, and an element with a "
            "full shell is the least reactive of its row",
        ],
        "correct_index": 1,
        "why": "A period ends when a shell is complete; the next element "
               "begins filling the shell beyond it and opens a new period.",
    },
    {
        "id": "ks4-periodic-table-h13",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a metal and a non-metal taken from the same period, "
                "and explain the difference in the ions they form.",
        "options": [
            "The metal sits further right with more outer electrons, so it "
            "gains them and turns negative",
            "Both form positive ions, because both have the same number of "
            "occupied shells to work from",
            "The metal has few outer electrons and loses them to give a "
            "positive ion; the non-metal is short of a few and gains them",
            "The non-metal forms no ion of any sort, because a non-metal "
            "shares its electrons in each compound that it goes on to make",
        ],
        "correct_index": 2,
        "why": "Position across a period sets the outer electron count, and "
               "that decides whether losing or gaining is the shorter route.",
    },
    {
        "id": "ks4-periodic-table-h14",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a chemist can predict the formula of an "
                "element's chloride from its position in the periodic table "
                "alone.",
        "options": [
            "The period number gives the number of chlorine atoms that will "
            "join to each atom of the element",
            "The relative atomic mass printed above the symbol gives the "
            "combining ratio directly",
            "The element's row in the table gives the charge, and the charge "
            "is the number of chlorines",
            "The group gives the charge on the element's ion, and enough "
            "1- chloride ions are added to balance it",
        ],
        "correct_index": 3,
        "why": "A Group 2 element forms a 2+ ion, so two 1- chloride ions "
               "balance it and the formula is XCl2.",
    },
    {
        "id": "ks4-periodic-table-h15",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how the outer electron count and the shell count "
                "both change on moving from Group 1 Period 2 to Group 2 "
                "Period 3.",
        "options": [
            "One more outer electron and one more occupied shell",
            "One fewer outer electron and one more occupied shell",
            "One more outer electron and the same number of shells",
            "The same outer electron count and one more occupied shell",
        ],
        "correct_index": 0,
        "why": "Group 1 to Group 2 adds an outer electron; Period 2 to Period "
               "3 adds a shell — 2.1 becomes 2.8.2.",
    },
    {
        "id": "ks4-periodic-table-h16",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the transition metals are set in a block of "
                "their own rather than inside the numbered groups.",
        "options": [
            "Because they were all discovered later than the elements of the "
            "numbered groups around them",
            "Because their outer electron counts do not step up neatly across "
            "the block as the main groups do",
            "Because they are the one part of the table that is metallic right "
            "through, so they are kept apart",
            "Because they have no outer electrons at all, so no group number "
            "could be given to them",
        ],
        "correct_index": 1,
        "why": "Across the block the outer shell stays much the same, so the "
               "steady group pattern of the main table does not apply.",
    },
    {
        "id": "ks4-periodic-table-h17",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the formula of the compound formed between a Group 1 "
                "element X and a Group 6 element Y.",
        "options": [
            "XY",
            "XY2",
            "X2Y",
            "X6Y",
        ],
        "correct_index": 2,
        "why": "X forms X+ and Y forms Y2-, so two X ions are needed to "
               "balance one Y ion.",
    },
    {
        "id": "ks4-periodic-table-h18",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of electrons a Group 6 atom must gain "
                "with the number a Group 2 atom must lose.",
        "options": [
            "The Group 6 atom gains six and the Group 2 atom loses two, "
            "matching their group numbers exactly",
            "The Group 6 atom gains four and the Group 2 atom loses six, "
            "since the two figures add up to eight",
            "Both have to move six electrons",
            "Each moves two — the Group 6 atom gains two and the Group 2 atom "
            "loses two",
        ],
        "correct_index": 3,
        "why": "Group 6 is two short of a full shell of 8, and Group 2 has "
               "two to spare, so both move two electrons.",
    },
    {
        "id": "ks4-periodic-table-h19",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An unknown element is a soft metal that reacts violently "
                "with cold water and gives an alkaline solution. Deduce its "
                "likely group.",
        "options": [
            "Group 1",
            "Group 2",
            "Group 7",
            "The transition metal block",
        ],
        "correct_index": 0,
        "why": "Softness, a violent reaction with cold water and an alkaline "
               "product together point to the alkali metals.",
    },
    {
        "id": "ks4-periodic-table-h20",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the period of the element whose atoms have the "
                "arrangement 2.8.1.",
        "options": [
            "Period 1",
            "Period 3",
            "Period 2",
            "Period 8",
        ],
        "correct_index": 1,
        "why": "Three numbers means three occupied shells, so the element is "
               "in Period 3 — it is sodium.",
    },
    {
        "id": "ks4-periodic-table-h21",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'The periodic table sorts the "
                "elements by how they look.'",
        "options": [
            "Sound — every element in one group has the same colour and the "
            "same shine as the rest of that group",
            "Sound, provided the elements are all compared as solids at the "
            "same temperature",
            "Unsound — the sorting is by atomic number, which sets the "
            "electron arrangement and so the properties",
            "Unsound — the sorting is by relative atomic mass, which has no "
            "connection with appearance at all",
        ],
        "correct_index": 2,
        "why": "Appearance is a consequence, not the criterion: bromine is a "
               "liquid and iodine a solid, yet both are Group 7.",
    },
    {
        "id": "ks4-periodic-table-h22",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why one element cannot appear in two different "
                "groups of the periodic table.",
        "options": [
            "Because each group was filled up completely before the next one "
            "was started by the chemists who drew the table",
            "Because an element would then need two relative atomic masses",
            "Because the table has exactly one space left for each element "
            "once all the others have been placed in it",
            "Because its atoms have only one outer electron count, and that "
            "count is what a group is",
        ],
        "correct_index": 3,
        "why": "The group is read directly off the electron arrangement, and "
               "an element has only one arrangement.",
    },
    {
        "id": "ks4-periodic-table-h23",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element's atoms have four outer electrons and form four "
                "covalent bonds. Determine its group.",
        "options": [
            "Group 4",
            "Group 8",
            "Group 2",
            "Group 0",
        ],
        "correct_index": 0,
        "why": "Four outer electrons puts it in Group 4, and sharing all four "
               "gives it a full outer shell.",
    },
    {
        "id": "ks4-periodic-table-h24",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says argon must be in Group 8 because its atoms "
                "have eight outer electrons. Evaluate this reasoning.",
        "options": [
            "Correct — argon is in Group 8, and the group number is read off "
            "the outer electron count in the usual way",
            "The count is right but the label is not: the full-shell group is "
            "numbered 0, not 8",
            "The count is wrong: an argon atom has no outer electrons, which "
            "is why the group is numbered 0",
            "Correct, although some tables write the group as 18",
        ],
        "correct_index": 1,
        "why": "Argon is 2.8.8 and so does have eight outer electrons, but "
               "the convention numbers the noble gases as Group 0.",
    },
    {
        "id": "ks4-periodic-table-h25",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two elements have atoms containing 9 and 17 electrons. "
                "Deduce what their positions in the periodic table have in "
                "common.",
        "options": [
            "They lie in the same period, since both of them are non-metals",
            "They lie in neighbouring groups",
            "They lie in the same group, Group 7",
            "They have nothing in common, since 9 and 17 are unrelated",
        ],
        "correct_index": 2,
        "why": "The arrangements are 2.7 and 2.8.7, so both have seven outer "
               "electrons and both sit in Group 7.",
    },
    {
        "id": "ks4-periodic-table-h26",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two elements in the same group can have very "
                "different melting points while behaving alike in reactions.",
        "options": [
            "Because melting point is set by the number of neutrons, which "
            "differs down a group",
            "Because the heavier element in a group is the one that melts at "
            "the lower temperature",
            "Because melting point depends on the group number and reactions "
            "depend on the period number",
            "Because reactions turn on the outer electrons, while melting "
            "point turns on the structure and the forces between particles",
        ],
        "correct_index": 3,
        "why": "Chlorine and iodine share a group and a chemistry, but "
               "iodine's larger molecules attract one another far more "
               "strongly.",
    },
]
