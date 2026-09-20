"""Chemistry · Atomic structure and the periodic table — electronic structure ·
the MRB-338 expansion.

Fifty-two rows on filling shells and reading what a filled set of shells tells
you. The weight falls on the two directions a pupil has to travel: atomic
number to configuration, and configuration back to a group, a period, an ion
charge or a formula. The misconception set runs through it — a third shell
holding nine, shells filled from the outside in, an ion keeping its parent
atom's arrangement, and the group number read off a period.

Particle counting and ion charge arithmetic belong to the
`subatomic-particles` leaf and the table's layout to `periodic-table`; this
leaf stays on the shells themselves and what follows from them.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-electronic-structure-e05",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "How many electrons fill the innermost shell of any atom?",
        "options": [
            "2",
            "1",
            "4",
            "8",
        ],
        "correct_index": 0,
        "why": "The first shell is full once it holds 2 electrons; only then "
               "does the next shell begin.",
    },
    {
        "id": "ks4-electronic-structure-e06",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sulfur atom has 16 electrons. State how these are arranged "
                "in shells.",
        "options": [
            "2.8.8",
            "2.8.6",
            "2.6.8",
            "8.8",
        ],
        "correct_index": 1,
        "why": "2 fill the first shell and 8 the second, leaving 6 in the "
               "third: 2.8.6.",
    },
    {
        "id": "ks4-electronic-structure-e07",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom is described as 2.8.4. State how many of its "
                "electron shells hold any electrons.",
        "options": [
            "2",
            "4",
            "3",
            "14",
        ],
        "correct_index": 2,
        "why": "Three numbers are written, so three shells are occupied.",
    },
    {
        "id": "ks4-electronic-structure-e08",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is unusual about the outer shell of a noble gas "
                "atom.",
        "options": [
            "It is empty, and an empty shell needs no filling",
            "It holds a single electron that is very hard indeed to remove "
            "from the atom",
            "It holds more electrons than the shell inside it",
            "It is full, so the atom has no need to gain or lose electrons",
        ],
        "correct_index": 3,
        "why": "A full outer shell is the stable arrangement, which is why "
               "the noble gases take part in so few reactions.",
    },
    {
        "id": "ks4-electronic-structure-e09",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has the arrangement 2.8.7. State which group of the "
                "periodic table it belongs to.",
        "options": [
            "Group 2",
            "Group 7",
            "Group 8",
            "Group 17",
        ],
        "correct_index": 1,
        "why": "The group number matches the number of outer electrons, and "
               "this atom has 7 of them.",
    },
    {
        "id": "ks4-electronic-structure-e10",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which electrons in an atom take part in its chemical "
                "reactions.",
        "options": [
            "The electrons closest to the nucleus",
            "Every electron the atom contains, equally",
            "The electrons in the outermost shell",
            "The electrons that share a shell with a neutron",
        ],
        "correct_index": 2,
        "why": "Bonding involves the outer-shell electrons; the inner shells "
               "are unchanged by a reaction.",
    },
    {
        "id": "ks4-electronic-structure-e11",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the element whose atoms have the arrangement 2.8.",
        "options": [
            "Oxygen",
            "Sodium",
            "Magnesium",
            "Neon",
        ],
        "correct_index": 3,
        "why": "2 + 8 = 10 electrons, so the atomic number is 10, which is "
               "neon.",
    },
    {
        "id": "ks4-electronic-structure-e12",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has three shells and every one of them is full. "
                "State how many electrons it holds altogether.",
        "options": [
            "18",
            "24",
            "3",
            "10",
        ],
        "correct_index": 0,
        "why": "The first three shells hold 2, 8 and 8, and 2 + 8 + 8 = 18.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-electronic-structure-s05",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon has atomic number 18. Determine how its electrons are "
                "spread between the shells.",
        "options": [
            "2.8.8",
            "2.8.8.8",
            "8.8.2",
            "2.16",
        ],
        "correct_index": 0,
        "why": "18 electrons fill the first shell with 2, the second with 8 "
               "and the third with 8.",
    },
    {
        "id": "ks4-electronic-structure-s06",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom with seven outer electrons reacts with a metal. "
                "Deduce the charge on the ion it forms.",
        "options": [
            "7-, because it gives away all seven of its outer electrons to the "
            "metal atom",
            "1-, because it gains the one electron that fills its outer shell",
            "1+, because it loses a single one of its outer electrons to the "
            "metal atom",
            "7+, because seven electrons move across to the metal",
        ],
        "correct_index": 1,
        "why": "Gaining one electron completes the outer shell and leaves one "
               "extra negative charge.",
    },
    {
        "id": "ks4-electronic-structure-s07",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lithium is 2.1 and sodium is 2.8.1. Explain why the two "
                "elements have similar chemical properties.",
        "options": [
            "They have the same total number of electrons",
            "They have the same number of occupied shells",
            "Each has one outer electron, so each reacts by losing one "
            "electron to form a 1+ ion",
            "Each has a full outer shell, so neither reacts readily",
        ],
        "correct_index": 2,
        "why": "Chemistry is set by the outer shell, and both of these have a "
               "single electron there.",
    },
    {
        "id": "ks4-electronic-structure-s08",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom contains 8 electrons. Determine how many of them lie "
                "in the outer shell.",
        "options": [
            "8",
            "2",
            "16",
            "6",
        ],
        "correct_index": 3,
        "why": "The arrangement is 2.6, so 6 electrons are in the outer shell.",
    },
    {
        "id": "ks4-electronic-structure-s09",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chlorine atom is 2.8.7. Write the arrangement of a "
                "chloride ion, Cl-.",
        "options": [
            "2.8.6",
            "2.8.8",
            "2.8.7",
            "2.8",
        ],
        "correct_index": 1,
        "why": "The ion has gained one electron, which completes the third "
               "shell at 8.",
    },
    {
        "id": "ks4-electronic-structure-s10",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A magnesium atom is 2.8.2. State the arrangement of a Mg2+ "
                "ion.",
        "options": [
            "2.8.2",
            "2.8.4",
            "2.8",
            "2.6",
        ],
        "correct_index": 2,
        "why": "The 2+ charge means both outer electrons have gone, leaving "
               "the full second shell as the outer one.",
    },
    {
        "id": "ks4-electronic-structure-s11",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom with the arrangement 2.8 takes part in "
                "very few reactions.",
        "options": [
            "Its outer shell is empty, so there is nothing for another atom "
            "to attract",
            "It has too few electrons in total for any kind of bond to be able "
            "to form",
            "Its two shells repel one another and keep other atoms away",
            "Its outer shell is full, so it has no tendency to gain or lose "
            "electrons",
        ],
        "correct_index": 3,
        "why": "A full outer shell is already the stable arrangement other "
               "atoms react in order to reach.",
    },
    {
        "id": "ks4-electronic-structure-s12",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element's atoms have 5 outer electrons and 3 occupied "
                "shells. Determine the atomic number.",
        "options": [
            "15",
            "5",
            "8",
            "13",
        ],
        "correct_index": 0,
        "why": "The arrangement is 2.8.5, and 2 + 8 + 5 = 15 electrons, so "
               "the atomic number is 15.",
    },
    {
        "id": "ks4-electronic-structure-s13",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of occupied shells in a sodium atom, "
                "2.8.1, with that in a lithium atom, 2.1.",
        "options": [
            "Sodium has two and lithium has one",
            "Sodium has three and lithium has two",
            "Both have three, since both are metals",
            "Sodium has one and lithium has two",
        ],
        "correct_index": 1,
        "why": "Each dot separates a shell, so 2.8.1 is three shells and 2.1 "
               "is two.",
    },
    {
        "id": "ks4-electronic-structure-s14",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element with the arrangement 2.1 reacts with an element "
                "with the arrangement 2.7. Predict the ratio in which their "
                "atoms combine.",
        "options": [
            "2 atoms of the 2.1 element to 1 of the 2.7 element",
            "1 atom of the 2.1 element to 2 of the 2.7 element",
            "1 atom of each",
            "3 atoms of the 2.1 element to 1 of the 2.7 element",
        ],
        "correct_index": 2,
        "why": "One element loses a single electron and the other gains a "
               "single electron, so the atoms pair up one to one.",
    },
    {
        "id": "ks4-electronic-structure-s15",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom with the arrangement 2.8.1 forms a 1+ "
                "ion rather than a 7- ion.",
        "options": [
            "Gaining seven electrons would add so much mass that the atom could "
            "no longer stay stable",
            "A charge of 7- is impossible, because no ion in a compound carries "
            "a charge larger than 3",
            "The third shell can hold no more than one electron in a metal",
            "Losing one electron is far easier than gaining seven, and both "
            "leave a full outer shell",
        ],
        "correct_index": 3,
        "why": "Either route reaches a full shell, and shedding one electron "
               "takes far less energy than collecting seven.",
    },
    {
        "id": "ks4-electronic-structure-s16",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the electron arrangement of a sodium ion with that "
                "of a neon atom.",
        "options": [
            "They are the same, 2.8, although the two particles have "
            "different numbers of protons",
            "They are the same, 2.8.1, because an ion holds on to the electron "
            "arrangement its atom had",
            "They differ, because the ion has the arrangement 2.8 while the "
            "neon atom is written as 2.8.1",
            "They differ: the ion is 2.8.2 and the neon atom is 2.8",
        ],
        "correct_index": 0,
        "why": "A sodium atom, 2.8.1, loses its outer electron to become 2.8 "
               "— neon's arrangement, but with 11 protons instead of 10.",
    },
    {
        "id": "ks4-electronic-structure-s17",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has 4 occupied shells and 2 electrons in its outer "
                "shell. Determine how many electrons it holds altogether.",
        "options": [
            "8",
            "12",
            "20",
            "26",
        ],
        "correct_index": 2,
        "why": "The arrangement is 2.8.8.2, and 2 + 8 + 8 + 2 = 20.",
    },
    {
        "id": "ks4-electronic-structure-s18",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the electron arrangement of an atom can be "
                "worked out from its atomic number alone.",
        "options": [
            "Because the atomic number counts the shells",
            "Because the atomic number is the mass number halved",
            "Because every element shares the same arrangement in its inner "
            "shells, whatever its atomic number",
            "Because the atomic number gives the proton count, which equals "
            "the electron count in a neutral atom",
        ],
        "correct_index": 3,
        "why": "Knowing how many electrons there are is enough, because they "
               "then fill 2, 8, 8 in a fixed order.",
    },
    {
        "id": "ks4-electronic-structure-s19",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silicon has atomic number 14. Determine its electron "
                "arrangement.",
        "options": [
            "2.8.4",
            "2.8.8.4",
            "2.4.8",
            "2.12",
        ],
        "correct_index": 0,
        "why": "14 electrons fill 2 then 8, leaving 4 in the third shell.",
    },
    {
        "id": "ks4-electronic-structure-s20",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes the arrangement of a phosphorus atom, "
                "atomic number 15, as 2.8.8.5. Explain the error.",
        "options": [
            "The first shell was given 2 when it should have been given 8",
            "The electrons total 23 rather than 15; the arrangement should be "
            "2.8.5",
            "The shells should be written from the outside in, as 5.8.8.2",
            "The shells should have been filled from the third one first, "
            "leaving the fourth until the very last",
        ],
        "correct_index": 1,
        "why": "2 + 8 + 8 + 5 comes to 23, not 15; phosphorus is 2.8.5.",
    },
    {
        "id": "ks4-electronic-structure-s21",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the second shell of an atom begins to fill only "
                "once the first shell is full.",
        "options": [
            "The second shell is smaller, so it can take electrons only when "
            "there is no room left",
            "The first shell is nearer the nucleus and lower in energy, so it "
            "is filled first",
            "The second shell forms only after the first one has been "
            "completed",
            "The first shell holds the neutrons, which have to be in place "
            "before any electrons arrive",
        ],
        "correct_index": 1,
        "why": "Electrons occupy the lowest energy level available, and that "
               "is the shell closest to the nucleus.",
    },
    {
        "id": "ks4-electronic-structure-s22",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element in Period 2 has 6 electrons in its outer shell. "
                "Write its electron arrangement.",
        "options": [
            "2.8.6",
            "6.2",
            "2.2.6",
            "2.6",
        ],
        "correct_index": 3,
        "why": "Period 2 means two occupied shells, so 2 in the first and 6 "
               "in the second.",
    },
    {
        "id": "ks4-electronic-structure-s23",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the total number of electrons in an atom of an "
                "element in Group 6 and Period 3.",
        "options": [
            "16",
            "18",
            "9",
            "6",
        ],
        "correct_index": 0,
        "why": "Three shells with 6 in the outer one gives 2.8.6, and 2 + 8 + "
               "6 = 16.",
    },
    {
        "id": "ks4-electronic-structure-s24",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes an atom of 12 electrons as 2.2.8, saying "
                "the shells fill from the outside in. Explain the error.",
        "options": [
            "The total should be 14 rather than 12, so the arrangement is "
            "2.4.8",
            "Shells fill from the innermost outwards, so the arrangement is "
            "2.8.2",
            "The second shell holds 2 electrons and the third holds 8, so the "
            "order is right",
            "An atom of 12 electrons has only two shells, so it should be "
            "written 4.8",
        ],
        "correct_index": 1,
        "why": "Electrons occupy the lowest energy shell first, so 2 go in, "
               "then 8, leaving 2: the arrangement is 2.8.2.",
    },
    {
        "id": "ks4-electronic-structure-s25",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of outer electrons in an atom of "
                "arrangement 2.8.8.2 with one of arrangement 2.8.2.",
        "options": [
            "The first has 8 and the second has 2",
            "The first has 20 and the second has 12",
            "Both have 2",
            "Two in the first and eight in the second",
        ],
        "correct_index": 2,
        "why": "The last number of each arrangement is the outer shell, and "
               "both end in 2 — which is why both sit in Group 2.",
    },
    {
        "id": "ks4-electronic-structure-s26",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a magnesium atom loses two electrons rather "
                "than gaining six.",
        "options": [
            "Gaining electrons is impossible for an atom with more than one "
            "shell",
            "Six electrons would not fit into the third shell of a magnesium "
            "atom",
            "Losing electrons makes the atom lighter, and a lighter atom is the "
            "more stable of the two whatever group it sits in",
            "Both routes give a full outer shell, and moving two electrons "
            "costs far less than moving six",
        ],
        "correct_index": 3,
        "why": "Magnesium is 2.8.2, so shedding two electrons leaves the full "
               "2.8 arrangement by the shorter route.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-electronic-structure-h05",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the ratio in which an element of arrangement 2.8.2 "
                "combines with an element of arrangement 2.6.",
        "options": [
            "1 atom of each",
            "1 atom of the 2.8.2 element to 2 of the 2.6 element",
            "2 atoms of the 2.8.2 element to 1 of the 2.6 element",
            "2 atoms of the 2.8.2 element to 3 of the 2.6 element",
        ],
        "correct_index": 0,
        "why": "One element loses two electrons and the other gains two, so "
               "the atoms pair one to one.",
    },
    {
        "id": "ks4-electronic-structure-h06",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element X has the arrangement 2.8.3. Predict the formula "
                "of its oxide, given that an oxygen atom gains two electrons.",
        "options": [
            "XO",
            "X2O3",
            "X3O2",
            "XO3",
        ],
        "correct_index": 1,
        "why": "X loses 3 electrons and each oxygen gains 2, so six electrons "
               "must move: two X atoms to three oxygen atoms.",
    },
    {
        "id": "ks4-electronic-structure-h07",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potassium ion and a chloride ion both have the "
                "arrangement 2.8.8, yet they carry opposite charges. Explain "
                "why.",
        "options": [
            "The two ions hold different numbers of electrons in their outer "
            "shells",
            "The chloride ion has an extra shell that does not show in the "
            "arrangement",
            "Potassium has 19 protons against the ion's 18 electrons, while "
            "chlorine has only 17",
            "Potassium is a gas and chlorine a metal, and the charge simply "
            "follows the physical state of the element",
        ],
        "correct_index": 2,
        "why": "The electron arrangements match, but the nuclei do not: 19 "
               "protons give 1+ and 17 protons give 1-.",
    },
    {
        "id": "ks4-electronic-structure-h08",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element forms 2- ions that have the arrangement 2.8. "
                "Deduce the atomic number of the element.",
        "options": [
            "10",
            "12",
            "6",
            "8",
        ],
        "correct_index": 3,
        "why": "The ion holds 10 electrons and gained two, so the atom had 8 "
               "electrons and therefore 8 protons.",
    },
    {
        "id": "ks4-electronic-structure-h09",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict which of an atom with arrangement 2.7 and an atom "
                "with arrangement 2.8.7 attracts an incoming electron more "
                "strongly, and explain why.",
        "options": [
            "The 2.7 atom, because its outer shell is closer to the nucleus "
            "and less shielded",
            "The 2.8.7 atom, because it has more electrons pulling the "
            "incoming one inwards",
            "The 2.8.7 atom, because a larger atom has a larger nuclear "
            "charge to offer",
            "Neither, because both need one electron and so attract equally",
        ],
        "correct_index": 0,
        "why": "A shorter distance and fewer inner shells in the way leave "
               "the nucleus pulling harder on an arriving electron.",
    },
    {
        "id": "ks4-electronic-structure-h10",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element's atoms hold 20 electrons. Deduce its group and "
                "its period.",
        "options": [
            "Group 4 and Period 2",
            "Group 2 and Period 4",
            "Group 20 and Period 1",
            "Group 8 and Period 2",
        ],
        "correct_index": 1,
        "why": "20 electrons give 2.8.8.2 — four occupied shells, so Period "
               "4, and 2 outer electrons, so Group 2.",
    },
    {
        "id": "ks4-electronic-structure-h11",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the arrangement of a noble gas is used as the "
                "reference point when predicting the charge on an ion.",
        "options": [
            "Because it is the heaviest element in its period",
            "Because a noble gas atom is the only one that can form an ion",
            "It is the full-shell arrangement an atom reaches by losing or "
            "gaining the fewest electrons it can",
            "Because a noble gas sits at the very end of a row, and that is "
            "the place from which charges are counted",
        ],
        "correct_index": 2,
        "why": "An atom gains or loses whatever it takes to reach the nearest "
               "full-shell arrangement, and that is a noble gas's.",
    },
    {
        "id": "ks4-electronic-structure-h12",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion has the arrangement 2.8 and carries a 3+ charge. "
                "Deduce the element it came from.",
        "options": [
            "Neon, with 10 protons",
            "Nitrogen, with 7 protons",
            "Sodium, with 11 protons",
            "Aluminium, with 13 protons",
        ],
        "correct_index": 3,
        "why": "The ion holds 10 electrons after losing three, so the atom "
               "had 13 electrons and 13 protons.",
    },
    {
        "id": "ks4-electronic-structure-h13",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that an atom whose electron count is an "
                "even number must have a full outer shell.",
        "options": [
            "Incorrect — an atom of 12 electrons is 2.8.2, with two electrons "
            "in a shell that holds eight",
            "Correct — an even number of electrons always fills the available "
            "shells exactly, leaving none left over",
            "Correct, so long as the atom lies in one of the first three "
            "periods",
            "Incorrect — an atom cannot have a full outer shell until the moment "
            "that it forms an ion",
        ],
        "correct_index": 0,
        "why": "12, 14 and 16 electrons all give part-filled outer shells, so "
               "an even count settles nothing.",
    },
    {
        "id": "ks4-electronic-structure-h14",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which of the arrangements 2.8.2, 2.8.5 and 2.8.7 "
                "belongs to the element forming the ion with the largest "
                "negative charge.",
        "options": [
            "2.8.7, which forms a 1- ion",
            "2.8.5, which forms a 3- ion",
            "2.8.2, which forms a 2- ion",
            "All three of them form 1- ions",
        ],
        "correct_index": 1,
        "why": "2.8.5 is three electrons short of a full shell, so it gains "
               "three and carries 3-; 2.8.2 loses two and is positive.",
    },
    {
        "id": "ks4-electronic-structure-h15",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three atoms have the arrangements 2.8.8, 2.8.8.1 and 2.8.7. "
                "Deduce which of them forms no ions, and explain.",
        "options": [
            "2.8.8.1, because a single outer electron is held too tightly to "
            "move",
            "2.8.7, because a shell that is already nearly full has no room for "
            "another electron",
            "2.8.8, because its outer shell is already full and it has "
            "nothing to gain by changing",
            "None of them, because every atom forms an ion of some kind",
        ],
        "correct_index": 2,
        "why": "2.8.8 is a noble gas arrangement; the other two are one "
               "electron away from it and reach it by losing or gaining one.",
    },
    {
        "id": "ks4-electronic-structure-h16",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom loses an electron from its outer shell "
                "rather than from one of its inner shells.",
        "options": [
            "An inner shell is full, and a full shell cannot lose anything",
            "An inner electron is bound to a neutron and cannot move",
            "An inner shell holds more electrons, so its hold is stronger",
            "An outer electron is furthest from the nucleus and least "
            "strongly held, so it takes the least energy to remove",
        ],
        "correct_index": 3,
        "why": "Attraction weakens with distance and with shielding by the "
               "inner shells, so the outermost electron goes first.",
    },
    {
        "id": "ks4-electronic-structure-h17",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the electron arrangement of the Period 3 element "
                "whose atoms form 3+ ions.",
        "options": [
            "2.8.3",
            "2.8.8.3",
            "2.3",
            "2.8.5",
        ],
        "correct_index": 0,
        "why": "Three occupied shells and three outer electrons to lose gives "
               "2.8.3, which is aluminium.",
    },
    {
        "id": "ks4-electronic-structure-h18",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an element of arrangement 2.8.8.2 is a metal "
                "while one of arrangement 2.8.6 is a non-metal.",
        "options": [
            "The first has more occupied shells than the second, and an element "
            "with four shells is counted as a metal",
            "The first has two outer electrons to lose, while the second is "
            "two short of a full shell and gains them",
            "The first has a heavier nucleus, and heavier elements are metals",
            "The second has an odd number of occupied shells, and that is what "
            "makes its atoms brittle rather than metallic",
        ],
        "correct_index": 1,
        "why": "Metals are the elements with few outer electrons to give "
               "away; non-metals are the ones a few short of a full shell.",
    },
    {
        "id": "ks4-electronic-structure-h19",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has the arrangement 2.8.5. Deduce the formula of "
                "its compound with hydrogen, in which each hydrogen atom "
                "forms one bond.",
        "options": [
            "XH",
            "XH2",
            "XH3",
            "XH5",
        ],
        "correct_index": 2,
        "why": "The atom is three electrons short of a full outer shell, so "
               "it shares with three hydrogen atoms.",
    },
    {
        "id": "ks4-electronic-structure-h20",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the arrangements 2.8.1 and 2.8.8.1 give ions of "
                "the same charge but elements of different reactivity.",
        "options": [
            "The second has more electrons in total, and total electrons set "
            "reactivity",
            "The second has the larger nuclear charge, which makes its outer "
            "electron much harder to remove",
            "The two are equally reactive, because charge and reactivity are "
            "the same thing",
            "Each loses one electron, but in the second that electron is "
            "further out and so goes more easily",
        ],
        "correct_index": 3,
        "why": "One outer electron in each case gives a 1+ ion; the extra "
               "shell in 2.8.8.1 weakens the pull on it.",
    },
    {
        "id": "ks4-electronic-structure-h21",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce why an atom of 11 electrons and an atom of 19 "
                "electrons form ions carrying the same charge.",
        "options": [
            "Both are 2.8.1 or 2.8.8.1, so each has one outer electron to lose",
            "Both have the same number of occupied shells",
            "The difference of 8 electrons cancels itself out when an ion is "
            "formed",
            "Both have a full outer shell before they react",
        ],
        "correct_index": 0,
        "why": "11 electrons give 2.8.1 and 19 give 2.8.8.1, and a single "
               "outer electron in each case means a 1+ ion.",
    },
    {
        "id": "ks4-electronic-structure-h22",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compound has the formula X3N2, where nitrogen forms a 3- "
                "ion. Deduce the number of outer electrons in an atom of X.",
        "options": [
            "3",
            "2",
            "6",
            "1",
        ],
        "correct_index": 1,
        "why": "Two nitride ions carry 6- in total, so three X ions must "
               "carry 6+, which is 2+ each — two outer electrons lost.",
    },
    {
        "id": "ks4-electronic-structure-h23",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the shells of an atom are also described as "
                "energy levels.",
        "options": [
            "Because an electron gives out energy whenever it moves within a "
            "shell",
            "Because the energy of a shell is set by how many electrons it "
            "already holds",
            "Because an electron in a shell further from the nucleus has more "
            "energy, and shells fill from the lowest energy upwards",
            "Because the energy of an atom is shared out equally between all "
            "of its shells",
        ],
        "correct_index": 2,
        "why": "Shells are a ladder of energies, and electrons take the "
               "lowest rung available first.",
    },
    {
        "id": "ks4-electronic-structure-h24",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes the arrangement of a calcium ion as "
                "2.8.8.2. Explain the error.",
        "options": [
            "The ion has gained an extra shell, so it should be written as "
            "2.8.8.8.2",
            "The arrangement should be written the other way round, as 2.8.8.2 "
            "reversed",
            "The total of 20 is wrong; a calcium atom holds 18 electrons",
            "The ion has lost its two outer electrons, so it should be 2.8.8",
        ],
        "correct_index": 3,
        "why": "2.8.8.2 is the calcium ATOM; the 2+ ion has shed both outer "
               "electrons and is 2.8.8.",
    },
    {
        "id": "ks4-electronic-structure-h25",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the arrangement of the atom that has three occupied "
                "shells and twice as many outer electrons as it has shells.",
        "options": [
            "2.8.6",
            "2.8.3",
            "2.8.8",
            "2.6.6",
        ],
        "correct_index": 0,
        "why": "Three shells and 2 × 3 = 6 outer electrons gives 2.8.6, which "
               "is sulfur.",
    },
    {
        "id": "ks4-electronic-structure-h26",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the number of outer electrons in an "
                "atom equals its group number for every element in the "
                "periodic table.",
        "options": [
            "Correct — the group number is defined as the count of outer "
            "electrons, and the rule holds without exception",
            "Incorrect — Group 0 atoms hold 8 outer electrons, not 0, and the "
            "transition metals do not follow the rule either",
            "Incorrect — the rule holds only for the non-metals on the right "
            "of the table",
            "Correct, provided the element lies in one of the first two "
            "periods",
        ],
        "correct_index": 1,
        "why": "The rule works for Groups 1 to 7 of the main block; Group 0 "
               "and the central block are the exceptions.",
    },
]
