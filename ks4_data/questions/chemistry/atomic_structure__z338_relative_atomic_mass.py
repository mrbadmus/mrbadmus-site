"""Chemistry · Atomic structure and the periodic table — relative atomic mass,
atomic number and isotopes · the MRB-338 expansion.

Fifty-two rows on the three numbers that describe a nucleus and the one number
that describes an element. The weight falls on the arithmetic a pupil actually
has to do — neutrons from mass number minus atomic number, electrons in an ion,
and above all the weighted average, run forwards from abundances and backwards
from a published Ar. The rest of the leaf is the misconception set: that Ar is a
simple mean, that a heavier isotope must be the commoner one, that a different
mass means a different element, and that isotopes have to be radioactive.

The electron-shell arithmetic belongs to the `electronic-structure` leaf and the
history of the ordering to `development-periodic-table`; this leaf stays on the
nucleus and the average.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-relative-atomic-mass-e05",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom of magnesium contains 12 protons. State the "
                "number of electrons it contains.",
        "options": [
            "12, because the positive and negative charges must balance",
            "24, because every proton in the nucleus is paired with two "
            "electrons outside it",
            "0, because the electrons are held inside the nucleus with the "
            "protons",
            "2, because magnesium sits in Group 2 and only the outer "
            "electrons are counted",
        ],
        "correct_index": 0,
        "why": "A neutral atom has equal numbers of protons and electrons, so "
               "12 protons means 12 electrons.",
    },
    {
        "id": "ks4-relative-atomic-mass-e06",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine-35 and chlorine-37 both occur naturally. State the "
                "term used for two atoms like these.",
        "options": [
            "Allotropes, because they are two forms of the same element",
            "Isotopes, because they have the same protons but different "
            "neutrons",
            "Ions, because one of the two carries an electrical charge",
            "Molecules, because two chlorine atoms are joined together",
        ],
        "correct_index": 1,
        "why": "Isotopes are atoms of one element with the same proton number "
               "and different neutron numbers.",
    },
    {
        "id": "ks4-relative-atomic-mass-e07",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which two numbers are needed to work out how many "
                "neutrons an atom contains.",
        "options": [
            "The atomic number and the electron count",
            "The relative atomic mass and the group number of the element",
            "The mass number and the atomic number",
            "The mass number and the number of electrons in the outer shell",
        ],
        "correct_index": 2,
        "why": "Neutrons = mass number − atomic number, so both of those "
               "numbers are needed.",
    },
    {
        "id": "ks4-relative-atomic-mass-e08",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sulfur-34 has atomic number 16. State the number of neutrons "
                "in one atom of it.",
        "options": [
            "16",
            "34",
            "50",
            "18",
        ],
        "correct_index": 3,
        "why": "Neutrons = 34 − 16 = 18.",
    },
    {
        "id": "ks4-relative-atomic-mass-e09",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why relative atomic mass is quoted without any units.",
        "options": [
            "Because it compares one atomic mass with another, so the units "
            "cancel out",
            "Because its units would be far too small to be written down "
            "conveniently",
            "Because it is a whole number for every element, and whole "
            "numbers need no units",
            "Because the unit is understood to be grams and is left off the "
            "table to save space",
        ],
        "correct_index": 0,
        "why": "Ar compares the mass of an atom with one twelfth of a "
               "carbon-12 atom, so it is a ratio and carries no unit.",
    },
    {
        "id": "ks4-relative-atomic-mass-e10",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which particle count differs between two isotopes of "
                "the same element.",
        "options": [
            "The number of protons in the nucleus",
            "The number of neutrons in the nucleus",
            "The number of electrons in the outer shell",
            "The number of protons and electrons added together",
        ],
        "correct_index": 1,
        "why": "Isotopes of one element share a proton number and differ only "
               "in how many neutrons they hold.",
    },
    {
        "id": "ks4-relative-atomic-mass-e11",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon-12 and carbon-14 are both isotopes of carbon. State "
                "how many protons each of them contains.",
        "options": [
            "Six protons in carbon-12 and eight protons in carbon-14",
            "Twelve protons in carbon-12 and fourteen protons in carbon-14",
            "Six protons in each of them",
            "Twelve protons in each of them",
        ],
        "correct_index": 2,
        "why": "Every carbon atom has 6 protons; the two isotopes differ only "
               "in their neutron numbers.",
    },
    {
        "id": "ks4-relative-atomic-mass-e12",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the relative atomic mass of an element means.",
        "options": [
            "The mass of its most common atom, measured in grams",
            "The total mass of all the protons and all the neutrons in one of "
            "its atoms, added together",
            "The mass of one of its atoms compared with the mass of one "
            "hydrogen atom",
            "The weighted average mass of its atoms compared with one twelfth "
            "of a carbon-12 atom",
        ],
        "correct_index": 3,
        "why": "Ar is a weighted average across the element's isotopes, "
               "measured against one twelfth of a carbon-12 atom.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-relative-atomic-mass-s05",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of copper is 69% copper-63 and 31% copper-65. "
                "Calculate its relative atomic mass.",
        "options": [
            "63.6",
            "64.0",
            "63.0",
            "65.0",
        ],
        "correct_index": 0,
        "why": "Ar = (69 × 63 + 31 × 65) ÷ 100 = 6362 ÷ 100 = 63.6.",
    },
    {
        "id": "ks4-relative-atomic-mass-s06",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of an element is 25% of the isotope with mass number "
                "14 and 75% of the isotope with mass number 12. Calculate the "
                "relative atomic mass.",
        "options": [
            "13.0",
            "12.5",
            "12.0",
            "13.5",
        ],
        "correct_index": 1,
        "why": "Ar = (25 × 14 + 75 × 12) ÷ 100 = 1250 ÷ 100 = 12.5.",
    },
    {
        "id": "ks4-relative-atomic-mass-s07",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two isotopes of one element have mass numbers 63 and 65. "
                "Determine the difference between them in the number of "
                "neutrons one atom holds.",
        "options": [
            "1",
            "4",
            "2",
            "128",
        ],
        "correct_index": 2,
        "why": "Both isotopes have the same proton count, so the whole "
               "difference of 65 − 63 = 2 must be in the neutrons.",
    },
    {
        "id": "ks4-relative-atomic-mass-s08",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Neon-20 and neon-22 have different densities but take part in "
                "exactly the same reactions. Suggest why.",
        "options": [
            "The extra neutrons change the mass and also leave the atom "
            "slightly more reactive",
            "The extra protons change the mass, and protons play no part in "
            "the making of bonds",
            "The extra electrons change the mass, while the reactions depend "
            "on the nucleus",
            "The extra neutrons change the mass of the atom but not its "
            "electron arrangement",
        ],
        "correct_index": 3,
        "why": "Reactions depend on the electrons, which are unchanged; the "
               "extra neutrons add mass and so change the density.",
    },
    {
        "id": "ks4-relative-atomic-mass-s09",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of an element contains equal numbers of atoms of "
                "mass number 151 and mass number 153. Calculate its relative "
                "atomic mass.",
        "options": [
            "152.0",
            "151.0",
            "153.0",
            "304.0",
        ],
        "correct_index": 0,
        "why": "With equal abundances the weighted average is the midpoint, "
               "(151 + 153) ÷ 2 = 152.0.",
    },
    {
        "id": "ks4-relative-atomic-mass-s10",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the relative atomic mass of most elements lies "
                "close to a whole number, even though it is an average.",
        "options": [
            "Because relative atomic masses are rounded to the nearest whole "
            "number before they are published",
            "Because one isotope is usually far more abundant than the others",
            "Because the neutrons in an atom have almost no mass of their own",
            "Because most elements have a single isotope, so there is nothing "
            "to average",
        ],
        "correct_index": 1,
        "why": "One isotope usually dominates the mixture, so the weighted "
               "average sits very near that isotope's mass number.",
    },
    {
        "id": "ks4-relative-atomic-mass-s11",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the relative atomic mass of an element does not "
                "change when that element takes part in a reaction.",
        "options": [
            "The atoms share electrons, and a shared electron is counted only "
            "once",
            "The mass of the compound is shared between its elements in fixed "
            "proportions",
            "The atoms themselves are unchanged, and Ar describes the atoms "
            "rather than the bonding",
            "Ar is worked out again for each compound, but the change is too "
            "small to notice",
        ],
        "correct_index": 2,
        "why": "A reaction rearranges electrons between atoms; the nuclei, "
               "and so the isotope mixture the average is taken over, are "
               "untouched.",
    },
    {
        "id": "ks4-relative-atomic-mass-s12",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom contains 14 protons and 15 neutrons. State its mass "
                "number and name the element.",
        "options": [
            "Mass number 14, and the element is silicon",
            "Mass number 29, and the element is phosphorus",
            "Mass number 15, and the element is nitrogen",
            "Mass number 29, and the element is silicon",
        ],
        "correct_index": 3,
        "why": "Mass number = 14 + 15 = 29, and 14 protons identifies the "
               "element as silicon.",
    },
    {
        "id": "ks4-relative-atomic-mass-s13",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says magnesium-25 must be a different element from "
                "magnesium-24 because its atoms have a different mass. "
                "Explain the error.",
        "options": [
            "Both have 12 protons, and it is the proton number that fixes the "
            "element",
            "Both have 12 neutrons, and it is the neutron number that fixes "
            "the element",
            "The two masses are in fact identical, so no difference arises in "
            "the first place",
            "Magnesium-25 does not occur in nature, so the comparison cannot "
            "be made at all",
        ],
        "correct_index": 0,
        "why": "Both isotopes have 12 protons; the extra neutron changes the "
               "mass but not the element.",
    },
    {
        "id": "ks4-relative-atomic-mass-s14",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silver occurs as silver-107 and silver-109 in almost equal "
                "amounts. Predict its relative atomic mass.",
        "options": [
            "About 107",
            "About 108",
            "About 109",
            "About 216",
        ],
        "correct_index": 1,
        "why": "Roughly equal abundances put the weighted average close to "
               "the midpoint of 107 and 109.",
    },
    {
        "id": "ks4-relative-atomic-mass-s15",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the relationship between the numbers of protons and "
                "electrons in a neutral atom, and explain why it holds.",
        "options": [
            "Electrons outnumber protons, because an electron weighs very "
            "much less than a proton does",
            "Protons outnumber electrons, because some electrons are lost as "
            "the atom forms",
            "They are equal, because a proton's charge of 1+ is cancelled by "
            "an electron's charge of 1-",
            "They are equal, because a proton and an electron have exactly "
            "the same mass",
        ],
        "correct_index": 2,
        "why": "An atom carries no overall charge, so the 1+ of each proton "
               "must be matched by the 1- of an electron.",
    },
    {
        "id": "ks4-relative-atomic-mass-s16",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium-24, magnesium-25 and magnesium-26 all form 2+ "
                "ions. Explain why.",
        "options": [
            "All three hold 12 neutrons, and the neutron count sets the "
            "charge on the ion",
            "All three sit in Period 3, and every Period 3 element forms an "
            "ion with a 2+ charge",
            "All three have different masses, and a heavier atom gives up "
            "more of its electrons",
            "All three have the electron arrangement 2.8.2 and lose the same "
            "two outer electrons",
        ],
        "correct_index": 3,
        "why": "Isotopes share an electron arrangement, so each one loses the "
               "same two outer electrons.",
    },
    {
        "id": "ks4-relative-atomic-mass-s17",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of silicon is 92% silicon-28, 5% silicon-29 and 3% "
                "silicon-30. Calculate its relative atomic mass.",
        "options": [
            "28.1",
            "28.5",
            "29.0",
            "28.0",
        ],
        "correct_index": 0,
        "why": "Ar = (92 × 28 + 5 × 29 + 3 × 30) ÷ 100 = 2811 ÷ 100 = 28.1.",
    },
    {
        "id": "ks4-relative-atomic-mass-s18",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the number of neutrons in an atom of uranium-238, "
                "which has atomic number 92.",
        "options": [
            "92",
            "146",
            "238",
            "330",
        ],
        "correct_index": 1,
        "why": "Neutrons = 238 − 92 = 146.",
    },
    {
        "id": "ks4-relative-atomic-mass-s19",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom contains 34 electrons and 45 neutrons. "
                "Determine its mass number.",
        "options": [
            "45",
            "34",
            "79",
            "113",
        ],
        "correct_index": 2,
        "why": "A neutral atom has 34 protons to match its 34 electrons, so "
               "the mass number is 34 + 45 = 79.",
    },
    {
        "id": "ks4-relative-atomic-mass-s20",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An isotope is written as chromium-52, and chromium has "
                "atomic number 24. Determine what the 52 counts and how many "
                "neutrons follow from it.",
        "options": [
            "The neutrons alone, giving 52 neutrons",
            "The protons alone, giving 24 neutrons",
            "The electrons and protons together, giving 26 neutrons",
            "The protons and neutrons together, giving 28 neutrons",
        ],
        "correct_index": 3,
        "why": "The number after the name is the mass number, protons plus "
               "neutrons, so neutrons = 52 − 24 = 28.",
    },
    {
        "id": "ks4-relative-atomic-mass-s21",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample holds equal numbers of atoms of mass number 10 and "
                "mass number 11. A student adds the two and gives Ar = 21. "
                "Explain the error.",
        "options": [
            "The two masses should be averaged rather than added, giving 10.5",
            "The two masses should be multiplied rather than added, giving 110",
            "The two masses should be subtracted rather than added, giving 1",
            "The value of 21 is right, but it should be written to one decimal "
            "place as 21.0",
        ],
        "correct_index": 0,
        "why": "Ar is an average; with equal abundances it is (10 + 11) ÷ 2 = "
               "10.5.",
    },
    {
        "id": "ks4-relative-atomic-mass-s22",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the relative atomic mass of an element "
                "if the proportion of its heavier isotope rises.",
        "options": [
            "It falls, because the lighter isotope's share has gone down",
            "It rises, because the heavier isotope now carries more weight in "
            "the average",
            "It stays fixed, because relative atomic mass is a set property",
            "It doubles, because the heavier isotope contributes twice as "
            "much",
        ],
        "correct_index": 1,
        "why": "A weighted average moves towards whichever isotope takes the "
               "larger share of the sample.",
    },
    {
        "id": "ks4-relative-atomic-mass-s23",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three atoms are described. A has 8 protons and 8 neutrons, B "
                "has 8 protons and 10 neutrons, and C has 10 protons and 8 "
                "neutrons. Determine which two are isotopes of one element.",
        "options": [
            "A and C",
            "B and C",
            "A and B",
            "All three of them",
        ],
        "correct_index": 2,
        "why": "A and B share a proton count of 8 and differ only in "
               "neutrons; C has 10 protons and so is a different element.",
    },
    {
        "id": "ks4-relative-atomic-mass-s24",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the atomic number of an element can never be "
                "larger than the mass number of one of its atoms.",
        "options": [
            "The atomic number counts only the electrons, and an atom holds "
            "fewer electrons than protons",
            "The mass number counts the neutrons alone, and every atom holds "
            "more neutrons than protons",
            "The two numbers are printed the other way round in the periodic "
            "table, so their order is fixed by convention",
            "The mass number counts the protons as well as the neutrons, so "
            "it is at least as large",
        ],
        "correct_index": 3,
        "why": "Mass number = protons + neutrons, and a neutron count cannot "
               "be negative, so it is never below the proton count.",
    },
    {
        "id": "ks4-relative-atomic-mass-s25",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of antimony is 57% antimony-121 and 43% "
                "antimony-123. Calculate its relative atomic mass.",
        "options": [
            "121.9",
            "122.0",
            "121.0",
            "123.0",
        ],
        "correct_index": 0,
        "why": "Ar = (57 × 121 + 43 × 123) ÷ 100 = 12186 ÷ 100 = 121.9.",
    },
    {
        "id": "ks4-relative-atomic-mass-s26",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why all the isotopes of one element occupy the same "
                "place in the periodic table.",
        "options": [
            "They share a mass number, and the table is ordered by mass number",
            "They share an atomic number, and the table is ordered by atomic "
            "number",
            "They share a neutron count, and it is the neutron count that "
            "fixes an element's position",
            "They are grouped together for convenience, although their true "
            "positions are some way apart",
        ],
        "correct_index": 1,
        "why": "Position in the modern table is set by proton number, and "
               "isotopes of one element all share it.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-relative-atomic-mass-h05",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lithium occurs as lithium-6 and lithium-7 and has a relative "
                "atomic mass of 6.9. Calculate the percentage of lithium-7 in "
                "the sample.",
        "options": [
            "10%",
            "69%",
            "90%",
            "50%",
        ],
        "correct_index": 2,
        "why": "If x% is lithium-7, (6(100 − x) + 7x) ÷ 100 = 6.9, so 600 + x "
               "= 690 and x = 90.",
    },
    {
        "id": "ks4-relative-atomic-mass-h06",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rubidium occurs as rubidium-85 and rubidium-87, and its "
                "relative atomic mass is 85.5. Calculate the percentage of "
                "rubidium-87.",
        "options": [
            "75%",
            "50%",
            "15%",
            "25%",
        ],
        "correct_index": 3,
        "why": "If x% is rubidium-87, (85(100 − x) + 87x) ÷ 100 = 85.5, so "
               "8500 + 2x = 8550 and x = 25.",
    },
    {
        "id": "ks4-relative-atomic-mass-h07",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element has two isotopes. 75% of its atoms have mass "
                "number 63 and its relative atomic mass is 63.5. Determine "
                "the mass number of the other isotope.",
        "options": [
            "65",
            "64",
            "66",
            "67",
        ],
        "correct_index": 0,
        "why": "(75 × 63 + 25x) ÷ 100 = 63.5 gives 4725 + 25x = 6350, so 25x "
               "= 1625 and x = 65.",
    },
    {
        "id": "ks4-relative-atomic-mass-h08",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element has isotopes of mass number 90 (52%), 92 (17%) "
                "and 94 (31%). Calculate its relative atomic mass to one "
                "decimal place.",
        "options": [
            "92.0",
            "91.6",
            "91.0",
            "92.7",
        ],
        "correct_index": 1,
        "why": "(52 × 90 + 17 × 92 + 31 × 94) ÷ 100 = 9158 ÷ 100 = 91.58, "
               "which is 91.6 to one decimal place.",
    },
    {
        "id": "ks4-relative-atomic-mass-h09",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why atomic masses are quoted on a relative scale "
                "rather than in grams.",
        "options": [
            "The mass of an atom shifts with temperature, so a fixed value in "
            "grams could not be given",
            "Grams measure the mass of a substance, and a single atom is not "
            "a substance",
            "The real mass of an atom is far too small to be a convenient "
            "number in grams",
            "The gram was defined long after the periodic table was drawn up, "
            "so the older scale has simply been kept on",
        ],
        "correct_index": 2,
        "why": "One carbon atom weighs about 2 × 10^-23 g; comparing atoms "
               "with one another gives numbers a pupil can work with.",
    },
    {
        "id": "ks4-relative-atomic-mass-h10",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two samples of one element are taken from different rocks "
                "and their relative atomic masses differ in the third decimal "
                "place. Suggest why.",
        "options": [
            "The atoms in one rock have picked up a few extra protons over "
            "geological time",
            "The element behaves differently in different rocks, so its atoms "
            "are not identical",
            "One sample must be contaminated, since a relative atomic mass "
            "cannot differ between samples",
            "The two rocks hold the element's isotopes in slightly different "
            "proportions",
        ],
        "correct_index": 3,
        "why": "Ar is a weighted average, so a small shift in the isotope "
               "proportions shifts the value slightly.",
    },
    {
        "id": "ks4-relative-atomic-mass-h11",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a hydrogen-1 atom with a hydrogen-2 atom in terms of "
                "the particles they contain and their chemical behaviour.",
        "options": [
            "Hydrogen-2 has one extra neutron; the two behave the same way in "
            "chemical reactions",
            "Hydrogen-2 has one extra proton; the two behave the same way in "
            "chemical reactions",
            "Hydrogen-2 has one extra neutron, which leaves it reacting about "
            "twice as fast as hydrogen-1",
            "Hydrogen-2 has one extra electron, so it forms a 2- ion where "
            "hydrogen-1 forms a 1+ ion",
        ],
        "correct_index": 0,
        "why": "One extra neutron doubles the mass but leaves the single "
               "electron, and so the chemistry, unchanged.",
    },
    {
        "id": "ks4-relative-atomic-mass-h12",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion with the formula X2- contains 18 electrons and has a "
                "mass number of 34. Determine the atomic number of X.",
        "options": [
            "18",
            "16",
            "20",
            "34",
        ],
        "correct_index": 1,
        "why": "The 2- charge means two electrons were gained, so the atom "
               "had 16 electrons and therefore 16 protons.",
    },
    {
        "id": "ks4-relative-atomic-mass-h13",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion with the formula M3+ contains 10 electrons and 14 "
                "neutrons. Determine the mass number of M.",
        "options": [
            "24",
            "23",
            "27",
            "13",
        ],
        "correct_index": 2,
        "why": "A 3+ charge means three electrons were lost, so there are 13 "
               "protons, and 13 + 14 = 27.",
    },
    {
        "id": "ks4-relative-atomic-mass-h14",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect on an element's relative atomic mass if a "
                "previously unknown heavier isotope were found to make up 2% "
                "of natural samples.",
        "options": [
            "It would drop slightly, because the mixture now holds more "
            "different isotopes than before",
            "It would not move, because a 2% share is too small to have any "
            "effect on an average",
            "It would climb to the mass number of the new isotope, which now "
            "sets the value for the element",
            "It would climb slightly, because a small share of heavier atoms "
            "enters the average",
        ],
        "correct_index": 3,
        "why": "Adding a heavier isotope at low abundance raises the weighted "
               "average by a small amount.",
    },
    {
        "id": "ks4-relative-atomic-mass-h15",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'If an element has isotopes, at "
                "least one of them must be radioactive.'",
        "options": [
            "Incorrect — many elements have two or more stable isotopes, such "
            "as carbon-12 and carbon-13",
            "Correct — any difference in the neutron number leaves the "
            "nucleus unstable and it decays",
            "Correct — an unusual neutron number is a sign of a radioactive "
            "atom",
            "Incorrect — none of the isotopes that occur in nature is "
            "radioactive",
        ],
        "correct_index": 0,
        "why": "Most elements have several stable isotopes; radioactivity is "
               "a separate property of particular nuclei.",
    },
    {
        "id": "ks4-relative-atomic-mass-h16",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 200-atom sample contains 150 atoms of mass number 79 and "
                "50 atoms of mass number 81. Calculate the relative atomic "
                "mass.",
        "options": [
            "80.0",
            "79.5",
            "80.5",
            "79.0",
        ],
        "correct_index": 1,
        "why": "(150 × 79 + 50 × 81) ÷ 200 = 15900 ÷ 200 = 79.5.",
    },
    {
        "id": "ks4-relative-atomic-mass-h17",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the relative atomic mass of an element is a "
                "property of the element rather than of any one of its atoms.",
        "options": [
            "Every atom of the element has exactly that mass, so the value "
            "belongs to all of them equally",
            "It is a property of the periodic table rather than of the matter "
            "the element is made from",
            "No single atom has that mass; the value is an average taken "
            "across the mixture of isotopes",
            "It describes how the mass of a sample grows as the sample gets "
            "larger, which is a bulk property",
        ],
        "correct_index": 2,
        "why": "Ar averages over the isotopes present, so it describes the "
               "element's natural mixture and not any individual atom.",
    },
    {
        "id": "ks4-relative-atomic-mass-h18",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium-40 has atomic number 20, argon-40 has atomic number "
                "18 and potassium-40 has atomic number 19. Determine which of "
                "the three contains the most neutrons.",
        "options": [
            "Calcium-40, with 20 neutrons",
            "Potassium-40, with 21 neutrons",
            "All three contain 40 neutrons",
            "Argon-40, with 22 neutrons",
        ],
        "correct_index": 3,
        "why": "Neutrons = 40 − atomic number, so argon has 22, potassium 21 "
               "and calcium 20.",
    },
    {
        "id": "ks4-relative-atomic-mass-h19",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Boron occurs as boron-10 and boron-11 and has a relative "
                "atomic mass of 10.8. Determine the ratio of boron-10 to "
                "boron-11 in the sample.",
        "options": [
            "1 : 4",
            "4 : 1",
            "1 : 1",
            "3 : 1",
        ],
        "correct_index": 0,
        "why": "If x% is boron-11, 1000 + x = 1080 so x = 80; the sample is "
               "20% boron-10 to 80% boron-11, which is 1 : 4.",
    },
    {
        "id": "ks4-relative-atomic-mass-h20",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student finds a relative atomic mass by adding the two "
                "isotope mass numbers and halving, and gets the right value. "
                "Suggest the condition under which this works.",
        "options": [
            "The two isotopes differ by exactly two neutrons",
            "The two isotopes are present in equal amounts",
            "The element has no more than two isotopes in total",
            "The heavier of the two isotopes is the more abundant",
        ],
        "correct_index": 1,
        "why": "A weighted average only reduces to the plain midpoint when "
               "the two abundances are the same.",
    },
    {
        "id": "ks4-relative-atomic-mass-h21",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Uranium-235 and uranium-238 behave the same way in chemical "
                "reactions, yet only uranium-235 is used as a nuclear fuel. "
                "Explain why.",
        "options": [
            "Chemistry depends on the neutrons, and uranium-238 alone holds "
            "enough of them to react",
            "Uranium-235 has more electrons, so it gives out more energy in a "
            "chemical reaction",
            "Chemistry depends on the electrons, which match; the difference "
            "between them is a nuclear one",
            "The two are really different elements, so the similarity in "
            "their chemistry is only apparent",
        ],
        "correct_index": 2,
        "why": "Both isotopes have 92 electrons and so identical chemistry; "
               "what differs is the behaviour of the nucleus itself.",
    },
    {
        "id": "ks4-relative-atomic-mass-h22",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims the relative atomic mass of an element must "
                "lie between the mass numbers of its lightest and its "
                "heaviest isotope. Evaluate this claim.",
        "options": [
            "Unsound — the average drops below the lightest mass number when "
            "that isotope is rare",
            "Unsound — the value is fixed by the commonest isotope and the "
            "rest are ignored",
            "Sound, though only because every element has exactly two "
            "isotopes",
            "Sound — a weighted average cannot fall outside the range of the "
            "values it averages",
        ],
        "correct_index": 3,
        "why": "Every isotope mass is multiplied by a share between 0 and 1, "
               "so the total must sit somewhere between the smallest and the "
               "largest mass number.",
    },
    {
        "id": "ks4-relative-atomic-mass-h23",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a chemist identifying an unknown element "
                "measures its atomic number rather than its mass number.",
        "options": [
            "Atomic number fixes the element, whereas two different elements "
            "can share a mass number",
            "Atomic number is the easier measurement, though either number "
            "would identify the element",
            "Mass number fixes the element, but it is a good deal harder to "
            "measure than atomic number",
            "Mass number shifts with temperature, so a measurement of it "
            "would not be reliable",
        ],
        "correct_index": 0,
        "why": "Argon-40 and calcium-40 share a mass number but are different "
               "elements; only the proton count settles it.",
    },
    {
        "id": "ks4-relative-atomic-mass-h24",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element has isotopes of mass number 204, 206, 207 and 208 "
                "in the proportions 1%, 24%, 22% and 53%. Calculate its "
                "relative atomic mass to one decimal place.",
        "options": [
            "206.3",
            "207.3",
            "207.0",
            "208.0",
        ],
        "correct_index": 1,
        "why": "(204 + 4944 + 4554 + 11024) ÷ 100 = 20726 ÷ 100 = 207.26, "
               "which is 207.3 to one decimal place.",
    },
    {
        "id": "ks4-relative-atomic-mass-h25",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that an element with a relative atomic "
                "mass of exactly 16.0 must contain atoms of mass number 16 "
                "and nothing else.",
        "options": [
            "Safe — a whole-number value can come from a single isotope and "
            "from no other arrangement",
            "Unsafe — the value would have had to be 16.5 for a single "
            "isotope",
            "Unsafe — a mixture of isotopes could average out to exactly 16.0",
            "Safe — an average taken over several isotopes cannot land on a "
            "whole number",
        ],
        "correct_index": 2,
        "why": "A sample of, say, mass numbers 15 and 17 in equal proportions "
               "also averages to 16.0, so the conclusion does not follow.",
    },
    {
        "id": "ks4-relative-atomic-mass-h26",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the relative atomic mass of an element lies "
                "closer to the mass number of its most abundant isotope than "
                "to any other.",
        "options": [
            "That isotope has the largest mass, so it pulls the average",
            "The less abundant isotopes are left out of the sum",
            "The average is taken over abundances rather than masses",
            "That isotope contributes the largest share of the weighted "
            "average",
        ],
        "correct_index": 3,
        "why": "Each isotope's mass is multiplied by its abundance, so the "
               "commonest isotope dominates the total.",
    },
]
