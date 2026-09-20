"""Physics · Atomic structure — the MRB-338 expansion of `mass-number-isotopes`.

One leaf only: AQA 8463 §6.4.1.2 — atomic number, mass number, the subtraction
that gives the neutron count, nuclear notation, what makes two nuclides
isotopes of one element, and what an ion changes and what it leaves alone. The
original twelve rows in `atomic_structure__a.py` define the two numbers, add
26 protons to 30 neutrons, hold the mass number still through ion formation,
count a magnesium ion, compare the two bromines, compare tritium with
hydrogen-1 and evaluate neon-22; this file takes what they leave — nucleon
number as the other name, the subtraction run in both directions, the named
nuclides of uranium, lead, potassium, chlorine, argon, copper, oxygen, lithium
and nitrogen, deuterium, the ions of fluorine and aluminium, why the physical
properties differ while the chemical ones do not, and the several ways a
neutron count can be reached from a charge and a mass number together.

The weight follows the CONTENT. `easier` stays at eight because recall here is
two definitions, one subtraction and the isotope rule, and asking those a ninth
way is the same question in different words. The demand lives in `standard` and
`harder`, where a count has to be recovered from a charge and a mass number at
once, or two nuclides compared to decide whether they are isotopes at all — so
that is where the twenty-two-row bands sit.

⚠️ Two numbers are deliberately not reused: the original `e03` adds 26 protons
to 30 neutrons and `h02` states a mass number of 31 in its stem, so no row here
asks a pupil for 56 or for 31. A stem that states another row's keyed answer is
brief §9.6, and a leaf that asks the same arithmetic twice is §3.

Every wrong option carries its own FALSE reason at the key's level of detail
(brief §9.2/§9.9), so that in three sets out of four the longest option is a
distractor.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Nucleon number, the subtraction, the isotope rule, deuterium, and the
    # one thing an electron cannot change.
    {
        "id": "ks4-mass-number-isotopes-e05",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the other name given to the mass number of a nucleus.",
        "options": [
            "The nucleon number",
            "The proton number",
            "The electron number",
            "The neutron number",
        ],
        "correct_index": 0,
        "why": "Protons and neutrons are together called nucleons, so the "
               "count of both is the nucleon number.",
    },
    {
        "id": "ks4-mass-number-isotopes-e06",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the number of neutrons in a nucleus is worked out.",
        "options": [
            "Add the atomic number to the mass number",
            "Halve the mass number, since the nucleons of a nucleus come in "
                "pairs",
            "Subtract the atomic number from the mass number",
            "Subtract the mass number from the atomic number",
        ],
        "correct_index": 2,
        "why": "The mass number counts protons and neutrons together, so "
               "taking away the protons leaves the neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-e07",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus has a mass number of 23 and contains 12 neutrons. "
                "State the number of protons.",
        "options": [
            "35",
            "12",
            "23",
            "11",
        ],
        "correct_index": 3,
        "why": "Protons are the mass number minus the neutrons, so "
               "23 − 12 = 11.",
    },
    {
        "id": "ks4-mass-number-isotopes-e08",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what every isotope of one element has in common.",
        "options": [
            "The same number of neutrons in the nucleus",
            "The same number of protons in the nucleus",
            "The same mass number, since they are one element",
            "The same total number of nucleons held inside the nucleus",
        ],
        "correct_index": 1,
        "why": "The proton number fixes the element, so all its isotopes "
               "share it.",
    },
    {
        "id": "ks4-mass-number-isotopes-e09",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what differs between two isotopes of the same element.",
        "options": [
            "Their number of neutrons",
            "Their number of protons, which is what makes them separate "
                "isotopes of one element",
            "Their number of outer-shell electrons, which is what gives each "
                "isotope its own chemistry",
            "Their number of occupied electron shells",
        ],
        "correct_index": 0,
        "why": "Isotopes share a proton number and differ only in how many "
               "neutrons sit alongside those protons.",
    },
    {
        "id": "ks4-mass-number-isotopes-e10",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the isotope of hydrogen whose nucleus holds one proton "
                "and one neutron.",
        "options": [
            "Deuterium",
            "Tritium",
            "Helium",
            "Protium",
        ],
        "correct_index": 0,
        "why": "Deuterium is hydrogen-2 — one proton and one neutron; "
               "tritium has two neutrons and protium has none.",
    },
    {
        "id": "ks4-mass-number-isotopes-e11",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon has atomic number 6. State the number of neutrons in "
                "a carbon-14 nucleus.",
        "options": [
            "14",
            "20",
            "8",
            "6",
        ],
        "correct_index": 2,
        "why": "14 − 6 = 8 neutrons alongside the six protons.",
    },
    {
        "id": "ks4-mass-number-isotopes-e12",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the number of protons in an atom when "
                "that atom gains an electron.",
        "options": [
            "It rises by one, so that the extra negative charge is balanced "
                "again",
            "It falls by one, because the new electron takes the place of a "
                "proton in the nucleus",
            "It does not change",
            "It doubles, because charges are always added in pairs",
        ],
        "correct_index": 2,
        "why": "Electrons are gained and lost outside the nucleus, so the "
               "proton count is untouched.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Named nuclides, ion counts, and the physical-versus-chemical split.
    {
        "id": "ks4-mass-number-isotopes-s05",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Uranium has atomic number 92. Determine the number of "
                "neutrons in a uranium-235 nucleus.",
        "options": [
            "327",
            "143",
            "92",
            "235",
        ],
        "correct_index": 1,
        "why": "235 − 92 = 143 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s06",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine has atomic number 17. Compare the number of "
                "neutrons in a chlorine-35 nucleus with the number in a "
                "chlorine-37 nucleus.",
        "options": [
            "17 in each, because the two nuclei belong to the same element",
            "35 and 37, because the name of a nuclide gives its neutron "
                "count directly",
            "18 and 20",
            "52 and 54, adding the atomic number on to the mass number of "
                "each nuclide in turn",
        ],
        "correct_index": 2,
        "why": "35 − 17 = 18 and 37 − 17 = 20, so the heavier nuclide holds "
               "two extra neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s07",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nuclide is written in nuclear notation with 23 above the "
                "element symbol and 11 below it. Determine the number of "
                "neutrons in its nucleus.",
        "options": [
            "23, which is the figure written above the symbol",
            "34, from adding the two figures together",
            "11, which is the figure written below the symbol",
            "12",
        ],
        "correct_index": 3,
        "why": "The upper figure is the mass number and the lower one the "
               "atomic number, so 23 − 11 = 12 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s08",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fluorine has atomic number 9. Determine the number of "
                "protons and electrons in a fluoride ion with a charge of "
                "1−.",
        "options": [
            "9 protons and 10 electrons",
            "10 protons and 9 electrons",
            "8 protons and 9 electrons",
            "9 protons and 8 electrons",
        ],
        "correct_index": 0,
        "why": "The proton count stays at 9 and a 1− charge means one extra "
               "electron, so there are 10.",
    },
    {
        "id": "ks4-mass-number-isotopes-s09",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium has atomic number 13. Determine the number of "
                "electrons in an aluminium ion with a charge of 3+.",
        "options": [
            "16, because the charge is added to the proton count",
            "13, because the electron count of an ion matches its protons",
            "10",
            "39, because a 3+ charge triples the number of electrons",
        ],
        "correct_index": 2,
        "why": "A 3+ charge means three electrons fewer than the 13 protons, "
               "so 13 − 3 = 10 electrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s10",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass number of an atom stays the same when "
                "that atom becomes an ion.",
        "options": [
            "Because a nucleon is taken out of the nucleus for every "
                "electron gained, so the two changes cancel each other out "
                "exactly",
            "Because the mass number counts only protons and neutrons, and "
                "an ion forms by gaining or losing electrons",
            "Because the electrons of an atom are far too light to be "
                "counted by any balance a school could own",
            "Because the mass number is a property of the element and can "
                "never be altered by anything",
        ],
        "correct_index": 1,
        "why": "Mass number is the count of nucleons, and ion formation "
               "changes only the number of electrons outside the nucleus.",
    },
    {
        "id": "ks4-mass-number-isotopes-s11",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One nucleus has 20 protons and 20 neutrons; another has 20 "
                "protons and 22 neutrons. Determine the relationship between "
                "them.",
        "options": [
            "Different elements, because the neutron counts of the two are "
                "not equal",
            "The same nuclide, since the proton counts agree",
            "Ions of one element, the second having gained two particles",
            "Isotopes of one element, with mass numbers of 40 and 42",
        ],
        "correct_index": 3,
        "why": "Equal proton numbers make them the same element, and 40 "
               "against 42 nucleons makes them isotopes of it.",
    },
    {
        "id": "ks4-mass-number-isotopes-s12",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Oxygen has atomic number 8. Determine the mass number of "
                "the oxygen isotope whose nucleus contains 10 neutrons.",
        "options": [
            "10, which is the neutron count itself",
            "2, from the difference between the two figures",
            "18",
            "80, from multiplying the neutrons by the protons",
        ],
        "correct_index": 2,
        "why": "8 protons plus 10 neutrons gives a mass number of 18.",
    },
    {
        "id": "ks4-mass-number-isotopes-s13",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Isotopes of one element have slightly different densities "
                "and melting points. Explain why.",
        "options": [
            "Their outer-shell electrons sit at slightly different distances "
                "from the nucleus in each one",
            "Their nuclei carry different charges, so each one attracts its "
                "neighbouring atoms with a different strength",
            "One of the two is radioactive, and a decaying atom takes up "
                "more room than a stable one",
            "Their nuclei hold different numbers of neutrons, so their atoms "
                "have different masses",
        ],
        "correct_index": 3,
        "why": "A different neutron count gives a different atomic mass, and "
               "mass is what density and melting point depend on.",
    },
    {
        "id": "ks4-mass-number-isotopes-s14",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lead-208 nucleus contains 82 protons. Calculate how many "
                "neutrons it holds.",
        "options": [
            "290",
            "82",
            "208",
            "126",
        ],
        "correct_index": 3,
        "why": "208 − 82 = 126 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s15",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium-40 has 19 protons and a mass number of 40. "
                "Determine its neutron count.",
        "options": [
            "21",
            "19",
            "40",
            "59",
        ],
        "correct_index": 0,
        "why": "40 − 19 = 21 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s16",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample contains nuclei of mass number 35 and nuclei of "
                "mass number 37, and every nucleus in it holds 17 protons. "
                "State how many different elements are present.",
        "options": [
            "Two, because the two mass numbers are not the same",
            "One",
            "Three, counting each mass number and the sample as a whole",
            "None, because a sample of mixed nuclei is a mixture rather "
                "than an element",
        ],
        "correct_index": 1,
        "why": "Every nucleus has 17 protons, so every atom is chlorine — one "
               "element present as two isotopes.",
    },
    {
        "id": "ks4-mass-number-isotopes-s17",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a neutral chlorine-35 atom and a neutral "
                "chlorine-37 atom both contain 17 electrons.",
        "options": [
            "Because the two atoms share their electrons between them, and "
                "that sharing is what makes them isotopes of one element",
            "Because 17 electrons is the largest number that the shells of a "
                "chlorine atom are able to hold at once",
            "Because the extra neutrons of chlorine-37 each cancel out one "
                "of that atom's electrons",
            "Because each of them holds 17 protons and a neutral atom has "
                "one electron for every proton",
        ],
        "correct_index": 3,
        "why": "Both are chlorine, so both have 17 protons, and a neutral "
               "atom matches its electron count to its proton count.",
    },
    {
        "id": "ks4-mass-number-isotopes-s18",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion contains 12 protons, 12 neutrons and 10 electrons. "
                "Determine its mass number and its charge.",
        "options": [
            "Mass number 34, charge 2+",
            "Mass number 24, charge 2−",
            "Mass number 22, charge 2+",
            "Mass number 24, charge 2+",
        ],
        "correct_index": 3,
        "why": "12 + 12 = 24 nucleons, and two protons more than electrons "
               "gives a charge of 2+.",
    },
    {
        "id": "ks4-mass-number-isotopes-s19",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon-12 and carbon-14 are both present in a piece of "
                "wood. Compare the nuclei of the two.",
        "options": [
            "6 protons in each; 6 neutrons in one and 8 in the other",
            "6 protons in each; 12 neutrons in one and 14 in the other",
            "6 neutrons in each; 6 protons in one and 8 in the other",
            "12 protons in one and 14 in the other, with 6 neutrons in each "
                "of them",
        ],
        "correct_index": 0,
        "why": "Both are carbon, so both have 6 protons, and 12 − 6 = 6 "
               "neutrons against 14 − 6 = 8.",
    },
    {
        "id": "ks4-mass-number-isotopes-s20",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why it is the atomic number, and not the mass "
                "number, that tells you which element an atom belongs to.",
        "options": [
            "Because the atomic number is the larger of the two figures "
                "printed",
            "Because the mass number is only ever an estimate, while the "
                "atomic number has been measured exactly",
            "Because every atom of an element has the same proton count, "
                "while its atoms can hold different numbers of neutrons",
            "Because the mass number changes each time an atom forms an ion "
                "and so cannot be relied upon",
        ],
        "correct_index": 2,
        "why": "Proton number is the same for every atom of an element, "
               "whereas its isotopes have different mass numbers.",
    },
    {
        "id": "ks4-mass-number-isotopes-s21",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass number of a nucleus that contains 15 "
                "protons and 17 neutrons.",
        "options": [
            "15",
            "2",
            "32",
            "17",
        ],
        "correct_index": 2,
        "why": "The mass number counts both, so 15 + 17 = 32.",
    },
    {
        "id": "ks4-mass-number-isotopes-s22",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the figure 14 stands for in the name "
                "carbon-14.",
        "options": [
            "The number of neutrons the nucleus holds alongside its protons",
            "The mass number — the protons and neutrons of the nucleus "
                "counted together",
            "The number of protons, which is what gives the element its "
                "position in the periodic table",
            "The number of electrons that a neutral atom of it carries in "
                "its shells",
        ],
        "correct_index": 1,
        "why": "The figure after an element's name is its mass number, the "
               "total count of protons and neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s23",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has 8 protons and a mass number of 18. Determine "
                "its neutron count and whether it is an isotope of "
                "oxygen-16.",
        "options": [
            "10 neutrons, and it is an isotope of oxygen-16",
            "10 neutrons, but it is a different element altogether from "
                "oxygen-16",
            "18 neutrons, and it is an isotope of oxygen-16",
            "2 neutrons, but it is a different element from oxygen-16",
        ],
        "correct_index": 0,
        "why": "18 − 8 = 10 neutrons, and sharing oxygen's 8 protons with a "
               "different nucleon total makes it an isotope of it.",
    },
    {
        "id": "ks4-mass-number-isotopes-s24",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lithium has atomic number 3. Determine the numbers of "
                "protons, neutrons and electrons in a neutral lithium-7 "
                "atom.",
        "options": [
            "7 protons, 3 neutrons, 7 electrons",
            "3 protons, 7 neutrons, 3 electrons",
            "3 protons, 4 neutrons, 3 electrons",
            "3 protons, 4 neutrons, 7 electrons",
        ],
        "correct_index": 2,
        "why": "3 protons from the atomic number, 7 − 3 = 4 neutrons, and a "
               "neutral atom has 3 electrons to match its protons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s25",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom that has lost two electrons still has "
                "the mass number it started with.",
        "options": [
            "Because the two electrons that have gone are replaced by two "
                "neutrons drawn into the nucleus from outside the atom",
            "Because the mass that has gone is restored as soon as the ion "
                "meets another particle and settles",
            "Because the nucleus expands slightly to make up for whatever "
                "the shells have lost",
            "Because mass number counts nucleons, and no proton or neutron "
                "has been removed",
        ],
        "correct_index": 3,
        "why": "The mass number is the total of protons and neutrons, and "
               "removing electrons changes neither of those.",
    },
    {
        "id": "ks4-mass-number-isotopes-s26",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Helium has atomic number 2. Compare a helium-4 nucleus with "
                "a helium-3 nucleus.",
        "options": [
            "4 protons in one and 3 in the other",
            "2 protons in each; 2 neutrons in one and 1 in the other",
            "2 protons in each; 4 neutrons in one and 3 in the other",
            "2 neutrons in each; 4 protons in one and 3 in the other",
        ],
        "correct_index": 1,
        "why": "Both are helium with 2 protons, and 4 − 2 = 2 neutrons "
               "against 3 − 2 = 1.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Counts recovered from a charge and a mass number at once, the
    # same-mass-number trap, and the isotope-versus-ion distinction.
    {
        "id": "ks4-mass-number-isotopes-h05",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion has a charge of 3+, a mass number of 27 and contains "
                "14 neutrons. Determine the number of electrons it has.",
        "options": [
            "16, by adding the charge to the proton count",
            "13, because the electron count of any particle matches its "
                "proton count",
            "10",
            "24, by taking the charge away from the mass number",
        ],
        "correct_index": 2,
        "why": "27 − 14 = 13 protons, and a 3+ charge leaves three fewer "
               "electrons than that, so 10.",
    },
    {
        "id": "ks4-mass-number-isotopes-h06",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus holds three more neutrons than protons and has a "
                "mass number of 39. Determine its atomic number.",
        "options": [
            "21, which is the number of neutrons rather than of protons",
            "18",
            "36, from subtracting the three extra neutrons from 39",
            "13, from dividing 39 by the three extra neutrons",
        ],
        "correct_index": 1,
        "why": "If there are p protons then p + (p + 3) = 39, so 2p = 36 and "
               "p = 18.",
    },
    {
        "id": "ks4-mass-number-isotopes-h07",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two neutral atoms have the same mass number but different "
                "atomic numbers. Explain whether the two can be isotopes of "
                "one another.",
        "options": [
            "Yes — sharing a mass number is what makes two atoms isotopes "
                "of one element",
            "No — isotopes must share an atomic number, and these two are "
                "different elements",
            "Yes — provided one of the two is radioactive and the other is "
                "a stable nuclide",
            "No — two neutral atoms can never share a mass number",
        ],
        "correct_index": 1,
        "why": "Isotopes are atoms of the SAME element, so they must have "
               "equal proton numbers and unequal mass numbers.",
    },
    {
        "id": "ks4-mass-number-isotopes-h08",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Atom X has 17 protons and 18 neutrons. Atom Y has 18 "
                "protons and 17 neutrons. Compare the two.",
        "options": [
            "Isotopes of one element, since the nucleons of the two come to "
                "the same total",
            "The same nuclide written two ways, because both nuclei contain "
                "35 particles altogether",
            "Different elements with the same mass number of 35, so they "
                "are not isotopes",
            "Different elements with different mass numbers, of 35 and 36 "
                "respectively",
        ],
        "correct_index": 2,
        "why": "Both have 35 nucleons, but 17 protons and 18 protons are two "
               "different elements, and isotopes must share a proton count.",
    },
    {
        "id": "ks4-mass-number-isotopes-h09",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Uranium has atomic number 92. Determine how many more "
                "neutrons a uranium-238 nucleus holds than a uranium-235 "
                "nucleus.",
        "options": [
            "3",
            "92",
            "473",
            "146",
        ],
        "correct_index": 0,
        "why": "238 − 92 = 146 and 235 − 92 = 143, a difference of 3 — the "
               "same as the difference between the mass numbers.",
    },
    {
        "id": "ks4-mass-number-isotopes-h10",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus has 92 protons and a mass number of 238. "
                "Calculate the percentage of its nucleons that are neutrons.",
        "options": [
            "38.7%",
            "61.3%",
            "92.0%",
            "63.0%",
        ],
        "correct_index": 1,
        "why": "238 − 92 = 146 neutrons, and 146 ÷ 238 × 100 = 61.3%.",
    },
    {
        "id": "ks4-mass-number-isotopes-h11",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a carbon-14 nucleus must contain 14 protons. "
                "Explain the error.",
        "options": [
            "The figure 14 counts the electrons of the atom, and a nucleus "
                "holds none of those at all",
            "The figure 14 is the mass number, so it counts protons and "
                "neutrons together; carbon has 6 protons",
            "The figure 14 is right for the protons but counts the neutrons "
                "too",
            "The figure 14 is the neutron count, so the nucleus in fact "
                "holds 20 protons in total",
        ],
        "correct_index": 1,
        "why": "14 is the nucleon total; carbon's atomic number of 6 fixes "
               "the protons, leaving 8 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-h12",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1+ ion of mass number 23 holds 10 electrons. Calculate how "
                "many neutrons are in its nucleus.",
        "options": [
            "13, from taking the electron count away from the mass number",
            "12",
            "10, because the neutron count of an ion matches its electrons",
            "11, which is the proton count rather than the neutron count",
        ],
        "correct_index": 1,
        "why": "A 1+ charge on 10 electrons means 11 protons, and "
               "23 − 11 = 12 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-h13",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Tritium is radioactive and "
                "hydrogen-1 is not, so the two cannot be isotopes of the "
                "same element.'",
        "options": [
            "Sound — both isotopes of an element must be stable, or both of "
                "them radioactive",
            "Sound — a radioactive nuclide belongs to a separate element of "
                "its own, listed elsewhere in the table",
            "Unsound — tritium is in fact an ion of hydrogen rather than an "
                "isotope of it, since it carries a charge",
            "Unsound — isotopes need only share a proton number, and whether "
                "a nuclide is radioactive does not enter into it",
        ],
        "correct_index": 3,
        "why": "Both nuclides have one proton, which makes them hydrogen "
               "isotopes; stability depends on the neutron count and is a "
               "separate matter.",
    },
    {
        "id": "ks4-mass-number-isotopes-h14",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral sodium-23 atom has 11 protons. Calculate how many "
                "subatomic particles it contains altogether.",
        "options": [
            "34",
            "23",
            "46",
            "45",
        ],
        "correct_index": 0,
        "why": "11 protons, 23 − 11 = 12 neutrons and 11 electrons come to "
               "34 particles in all.",
    },
    {
        "id": "ks4-mass-number-isotopes-h15",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two isotopes of one element can be separated by "
                "a physical process but not by a chemical one.",
        "options": [
            "Because one of the two nuclides is radioactive, and chemistry "
                "cannot act on a decaying nucleus",
            "Because a chemical reaction destroys the lighter isotope of the "
                "two before any separation can be made",
            "Because their nuclei carry different charges, and only a "
                "physical process is able to tell two charges apart",
            "Because their electron arrangements are identical, so they "
                "react alike, while their different masses can be used",
        ],
        "correct_index": 3,
        "why": "Chemistry depends on electron arrangement, which the two "
               "share, while physical methods can exploit the difference in "
               "mass.",
    },
    {
        "id": "ks4-mass-number-isotopes-h16",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two nuclei each contain 30 neutrons. One has a mass number "
                "of 56 and the other a mass number of 54. Determine whether "
                "they are isotopes of one element.",
        "options": [
            "Yes, because the two share an identical neutron count",
            "No — 26 protons against 24 makes them different elements",
            "Yes, because the difference between their two mass numbers is "
                "no more than two",
            "No — they are the same element but one of them is an ion of it",
        ],
        "correct_index": 1,
        "why": "56 − 30 = 26 protons and 54 − 30 = 24, so the two are "
               "different elements and cannot be isotopes.",
    },
    {
        "id": "ks4-mass-number-isotopes-h17",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine has atomic number 17. Compare the neutron count of "
                "a chlorine-35 atom with that of a chlorine-37 ion that has "
                "gained one electron.",
        "options": [
            "18 and 20 — gaining an electron changes neither count",
            "18 and 21 — the electron gained joins the neutrons",
            "18 and 19 — the extra electron cancels one neutron",
            "17 and 17 — both are chlorine, so both counts are equal",
        ],
        "correct_index": 0,
        "why": "35 − 17 = 18 and 37 − 17 = 20, and an electron gained sits "
               "outside the nucleus so alters no nucleon count.",
    },
    {
        "id": "ks4-mass-number-isotopes-h18",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus holds equal numbers of protons and neutrons and "
                "has a mass number of 40. Determine its atomic number and "
                "the electron count of a neutral atom of it.",
        "options": [
            "Atomic number 40, and 40 electrons",
            "Atomic number 20, and 40 electrons",
            "Atomic number 20, and 20 electrons",
            "Atomic number 10, and 10 electrons",
        ],
        "correct_index": 2,
        "why": "Equal counts summing to 40 gives 20 protons and 20 neutrons, "
               "and a neutral atom has 20 electrons to match its protons.",
    },
    {
        "id": "ks4-mass-number-isotopes-h19",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number of neutrons in a particular nucleus "
                "cannot be found from the periodic table on its own.",
        "options": [
            "Because the periodic table is arranged by mass number, not by "
                "neutrons",
            "Because the neutron count of a nucleus changes constantly and "
                "so could not be printed in any table",
            "Because neutrons carry no charge, which means their number can "
                "never be worked out by calculation",
            "Because the table gives the atomic number, and the mass number "
                "of the particular isotope is needed as well",
        ],
        "correct_index": 3,
        "why": "The table fixes the proton number for an element, but its "
               "isotopes have different neutron counts, so the mass number "
               "of the nuclide in question is also required.",
    },
    {
        "id": "ks4-mass-number-isotopes-h20",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a neutral atom of any isotope of an element "
                "carries the same number of electrons as a neutral atom of "
                "every other isotope of it.",
        "options": [
            "Because all the isotopes of one element share a proton count, "
                "and a neutral atom matches its electrons to its protons",
            "Because each extra neutron of the heavier isotope is balanced "
                "by one more electron in its shells",
            "Because the electron count of an atom is decided by its mass "
                "number, which is the same for all of its isotopes",
            "Because the shells of an element are able to hold only one "
                "fixed number of electrons, whatever the nucleus does",
        ],
        "correct_index": 0,
        "why": "Isotopes share the atomic number, and a neutral atom has one "
               "electron per proton, so the electron count is the same.",
    },
    {
        "id": "ks4-mass-number-isotopes-h21",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nitrogen has atomic number 7. Determine the ratio of "
                "neutrons to protons in a nitrogen-15 nucleus.",
        "options": [
            "15 : 7",
            "7 : 8",
            "8 : 7",
            "1 : 1",
        ],
        "correct_index": 2,
        "why": "15 − 7 = 8 neutrons to 7 protons, so the ratio is 8 : 7.",
    },
    {
        "id": "ks4-mass-number-isotopes-h22",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass number of an ion that contains 24 "
                "protons, 28 neutrons and 21 electrons.",
        "options": [
            "73",
            "45",
            "52",
            "49",
        ],
        "correct_index": 2,
        "why": "Mass number counts nucleons only, so 24 + 28 = 52 and the "
               "electrons are not included.",
    },
    {
        "id": "ks4-mass-number-isotopes-h23",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why adding a neutron to a nucleus changes its mass "
                "number but leaves the element it belongs to unaltered.",
        "options": [
            "Because a neutron has no mass of its own, so only the printed "
                "count alters",
            "Because the extra neutron is pushed straight back out of the "
                "nucleus before the element has time to change",
            "Because the new neutron turns into a proton, and that keeps the "
                "element exactly as it was before",
            "Because the mass number counts nucleons, which the new neutron "
                "joins, while the element is fixed by the proton count",
        ],
        "correct_index": 3,
        "why": "One more nucleon raises the mass number by 1, and the "
               "element depends only on how many protons there are.",
    },
    {
        "id": "ks4-mass-number-isotopes-h24",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on an atom of gaining one neutron with "
                "the effect of gaining one electron.",
        "options": [
            "The neutron raises the mass number by 1 and leaves the charge "
                "alone; the electron makes the charge 1− and leaves the mass "
                "number alone",
            "The neutron makes the charge 1+ as well as raising the mass "
                "number by 1; the electron makes the charge 1− and lowers that "
                "number by 1",
            "Both raise the mass number by 1, and only the electron has any "
                "effect at all on the overall charge",
            "The neutron changes the element the atom belongs to; the "
                "electron changes its mass number instead",
        ],
        "correct_index": 0,
        "why": "A neutron is a nucleon with no charge, so it moves the mass "
               "number only; an electron carries −1 and no appreciable mass, "
               "so it moves the charge only.",
    },
    {
        "id": "ks4-mass-number-isotopes-h25",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper has atomic number 29 and has isotopes of mass "
                "numbers 63 and 65. Determine the difference between their "
                "neutron counts.",
        "options": [
            "29",
            "58",
            "2",
            "34",
        ],
        "correct_index": 2,
        "why": "63 − 29 = 34 and 65 − 29 = 36 neutrons, a difference of 2.",
    },
    {
        "id": "ks4-mass-number-isotopes-h26",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'An ion of an element is simply "
                "another isotope of that element.'",
        "options": [
            "Sound — an ion and an isotope both differ from the ordinary "
                "atom",
            "Unsound — isotopes differ in their neutron count, while an ion "
                "differs from its atom in its electron count",
            "Sound — provided the ion carries a positive charge rather than "
                "a negative one",
            "Unsound — an ion is a different element altogether, because "
                "its charge is not the same",
        ],
        "correct_index": 1,
        "why": "An isotope is defined by a different number of neutrons in "
               "the nucleus; an ion is an atom that has gained or lost "
               "electrons, and its nucleus is unchanged.",
    },
]
