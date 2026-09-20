"""Chemistry · Atomic structure and the periodic table — subatomic particles ·
the MRB-338 expansion.

Fifty-two rows on the three particles and the counting that follows from them:
relative charge and relative mass, where each particle sits, atomic number and
mass number used as a pair, why a neutral atom has equal protons and electrons,
and what changes and what does not when an ion forms. The weight falls on
counting — protons, neutrons and electrons for a named atom and for a named ion,
and the charge deduced back from a count — and on the two misreadings that cost
most marks: mass number taken for atomic number, and protons thought to change
when an ion forms.

Isotopes and relative atomic mass belong to the `relative-atomic-mass` leaf and
the history of the model to `model-of-the-atom`; neither is asked here.
Radioactivity is the physics half of this topic id and is absent entirely.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-subatomic-particles-e05",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the relative charge and relative mass of a proton.",
        "options": [
            "Charge +1, relative mass 1",
            "Charge -1, relative mass 1",
            "Charge 0, relative mass 1",
            "Charge +1, relative mass 0",
        ],
        "correct_index": 0,
        "why": "A proton carries a single positive charge and has a relative "
               "mass of 1, the same as a neutron.",
    },
    {
        "id": "ks4-subatomic-particles-e06",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the relative charge on an electron.",
        "options": [
            "+1",
            "-1",
            "0",
            "-2",
        ],
        "correct_index": 1,
        "why": "An electron carries one negative charge, which exactly "
               "balances the positive charge of one proton.",
    },
    {
        "id": "ks4-subatomic-particles-e07",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two particles found in the nucleus of an atom.",
        "options": [
            "Protons and electrons",
            "Neutrons and electrons",
            "Protons and neutrons",
            "Electrons only",
        ],
        "correct_index": 2,
        "why": "The nucleus holds the protons and the neutrons, while the "
               "electrons occupy shells around it.",
    },
    {
        "id": "ks4-subatomic-particles-e08",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom of fluorine has 9 protons. State the number of "
                "electrons in the neutral atom.",
        "options": [
            "7",
            "8",
            "10",
            "9",
        ],
        "correct_index": 3,
        "why": "A neutral atom has as many electrons as protons, so the "
               "charges cancel exactly.",
    },
    {
        "id": "ks4-subatomic-particles-e09",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the overall charge on the nucleus of an atom.",
        "options": [
            "Positive, because of the protons in it",
            "Negative, because of the electrons around it",
            "Neutral, because of the neutrons in it",
            "It depends on the element",
        ],
        "correct_index": 0,
        "why": "Only protons carry charge inside the nucleus, so a nucleus is "
               "always positively charged.",
    },
    {
        "id": "ks4-subatomic-particles-e10",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to an atom's charge when it loses one "
                "electron.",
        "options": [
            "It becomes 1-",
            "It becomes 1+",
            "It stays neutral",
            "It becomes 2+",
        ],
        "correct_index": 1,
        "why": "Removing one negative charge leaves one unbalanced positive "
               "charge behind on the particle.",
    },
    {
        "id": "ks4-subatomic-particles-e11",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which number in a nuclear symbol is written as the "
                "larger of the two.",
        "options": [
            "The atomic number",
            "The neutron count",
            "The mass number",
            "The electron count",
        ],
        "correct_index": 2,
        "why": "The mass number counts protons and neutrons together, so it "
               "cannot be smaller than the proton count on its own.",
    },
    {
        "id": "ks4-subatomic-particles-e12",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the relative mass of an electron compares with "
                "that of a proton.",
        "options": [
            "It is about the same",
            "It is about twice as large",
            "It is about half as large",
            "It is so small it is treated as negligible, at roughly 1/1836 of "
            "a proton's mass",
        ],
        "correct_index": 3,
        "why": "An electron's mass is a tiny fraction of a proton's, which is "
               "why it is neglected rather than counted as exactly zero.",
    },
    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-subatomic-particles-s05",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom of oxygen has mass number 16 and atomic number 8. "
                "Determine the numbers of protons, neutrons and electrons.",
        "options": [
            "8 protons, 8 neutrons, 8 electrons",
            "8 protons, 16 neutrons, 8 electrons",
            "16 protons, 8 neutrons, 16 electrons",
            "8 protons, 24 neutrons, 8 electrons",
        ],
        "correct_index": 0,
        "why": "Neutrons are 16 - 8 = 8, and a neutral atom has as many "
               "electrons as its 8 protons.",
    },
    {
        "id": "ks4-subatomic-particles-s06",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom of iron has mass number 56 and atomic number 26. "
                "Calculate the number of neutrons.",
        "options": [
            "26",
            "30",
            "56",
            "82",
        ],
        "correct_index": 1,
        "why": "Neutrons are found by subtracting the atomic number from the "
               "mass number.",
    },
    {
        "id": "ks4-subatomic-particles-s07",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A magnesium atom has 12 protons. Determine the number of "
                "electrons in a Mg2+ ion.",
        "options": [
            "14",
            "12",
            "10",
            "2",
        ],
        "correct_index": 2,
        "why": "A 2+ charge means two electrons have been lost from the "
               "neutral atom's twelve.",
    },
    {
        "id": "ks4-subatomic-particles-s08",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a metal atom forms a positive ion rather than a "
                "negative one.",
        "options": [
            "It gains electrons, and every electron gained adds a positive "
            "charge to the atom",
            "It gains protons from the non-metal it reacts with",
            "It loses protons from its nucleus during the reaction",
            "It loses electrons, leaving more protons than electrons",
        ],
        "correct_index": 3,
        "why": "Losing negative charge leaves the positive charge of the "
               "nucleus no longer fully balanced.",
    },
    {
        "id": "ks4-subatomic-particles-s09",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion is made from an atom with 20 protons and 20 neutrons "
                "that has lost some electrons, leaving it with 18. Work out "
                "the ion's overall charge.",
        "options": [
            "2+",
            "2-",
            "Neutral",
            "18+",
        ],
        "correct_index": 0,
        "why": "There are two more protons than electrons, so two positive "
               "charges are left unbalanced.",
    },
    {
        "id": "ks4-subatomic-particles-s10",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A copper atom's nucleus contains 29 protons and has a mass "
                "number of 63. Work out how many neutrons it contains.",
        "options": [
            "29",
            "34",
            "32",
            "63",
        ],
        "correct_index": 1,
        "why": "Subtracting 29 from 63 gives the number of neutrons in the "
               "nucleus.",
    },
    {
        "id": "ks4-subatomic-particles-s11",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the atomic number identifies which element an "
                "atom belongs to.",
        "options": [
            "Because the electron count can be changed without altering "
            "which element an atom is",
            "Because the neutron count is the same in every atom of one "
            "element and differs between elements",
            "Because the proton count is fixed for an element and different "
            "for every other one",
            "Because the mass of an atom is what decides the element it "
            "belongs to",
        ],
        "correct_index": 2,
        "why": "Every carbon atom has 6 protons and nothing else has 6, so "
               "the proton count names the element.",
    },
    {
        "id": "ks4-subatomic-particles-s12",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oxide ion is written O2-. An oxygen atom has 8 protons. "
                "Determine the number of electrons in the ion.",
        "options": [
            "6",
            "8",
            "16",
            "10",
        ],
        "correct_index": 3,
        "why": "A 2- charge means two electrons have been gained on top of "
               "the atom's original eight.",
    },
    {
        "id": "ks4-subatomic-particles-s13",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom has no overall charge.",
        "options": [
            "The number of protons equals the number of electrons, so the "
            "charges cancel",
            "The neutrons in the nucleus cancel out the charge of the protons "
            "beside them",
            "The electrons move so quickly that their charge averages out to "
            "nothing over time",
            "The charge of a proton is smaller than the charge of an electron "
            "by a small amount",
        ],
        "correct_index": 0,
        "why": "Equal numbers of single positive and single negative charges "
               "sum to zero.",
    },
    {
        "id": "ks4-subatomic-particles-s14",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A phosphorus atom has 15 protons and a mass number of 31. "
                "State how many protons, neutrons and electrons it contains.",
        "options": [
            "15 protons, 31 neutrons, 15 electrons",
            "15 protons, 16 neutrons, 15 electrons",
            "31 protons, 15 neutrons, 31 electrons",
            "16 protons, 15 neutrons, 16 electrons",
        ],
        "correct_index": 1,
        "why": "Neutrons are 31 - 15 = 16, and the neutral atom has 15 "
               "electrons to match its 15 protons.",
    },
    {
        "id": "ks4-subatomic-particles-s15",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An aluminium atom has 13 protons. Determine the number of "
                "electrons in an Al3+ ion.",
        "options": [
            "3",
            "13",
            "10",
            "16",
        ],
        "correct_index": 2,
        "why": "A 3+ charge means three of the thirteen electrons have been "
               "lost.",
    },
    {
        "id": "ks4-subatomic-particles-s16",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a neutron adds to an atom's mass but not to its "
                "charge.",
        "options": [
            "It sits outside the nucleus, where charge has no effect on the "
            "atom as a whole",
            "It has a relative mass of 0 and a relative charge of 1",
            "It carries a charge that the protons beside it immediately "
            "cancel out inside the nucleus",
            "It has a relative mass of 1 and a relative charge of 0",
        ],
        "correct_index": 3,
        "why": "The neutron is the one nuclear particle that is massive and "
               "electrically neutral at the same time.",
    },
    {
        "id": "ks4-subatomic-particles-s17",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon has an atomic number of 18 and a mass number of 40. "
                "How many neutrons does one of its atoms contain?",
        "options": [
            "22",
            "20",
            "18",
            "40",
        ],
        "correct_index": 0,
        "why": "The neutron count is the mass number less the atomic number.",
    },
    {
        "id": "ks4-subatomic-particles-s18",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral calcium atom has 20 electrons. When it forms a "
                "Ca2+ ion, state how many electrons remain.",
        "options": [
            "16",
            "18",
            "20",
            "22",
        ],
        "correct_index": 1,
        "why": "Two electrons have been removed from the neutral atom's "
               "twenty.",
    },
    {
        "id": "ks4-subatomic-particles-s19",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a chloride ion has 18 protons because it has "
                "18 electrons. Explain the error.",
        "options": [
            "The electron count is actually 17, because an ion keeps equal "
            "numbers of the two particles",
            "The proton count rises to 18, which is what gives the ion its "
            "negative charge in the first place",
            "The proton count stays at 17; only the electron count has changed",
            "The proton count falls to 16, so the extra electron restores the "
            "balance of charge again",
        ],
        "correct_index": 2,
        "why": "Forming an ion moves electrons only, so the nucleus and its "
               "17 protons are untouched.",
    },
    {
        "id": "ks4-subatomic-particles-s20",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc has 30 protons in every atom and a mass number of 65. "
                "Work out how many protons, neutrons and electrons one atom "
                "of zinc contains.",
        "options": [
            "30 protons, 65 neutrons, 30 electrons",
            "65 protons, 30 neutrons, 65 electrons",
            "35 protons, 30 neutrons, 35 electrons",
            "30 protons, 35 neutrons, 30 electrons",
        ],
        "correct_index": 3,
        "why": "Neutrons are 65 - 30 = 35, and the neutral atom carries 30 "
               "electrons.",
    },
    {
        "id": "ks4-subatomic-particles-s21",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many electrons a nitride ion, N3-, contains, given "
                "that nitrogen has 7 protons.",
        "options": [
            "10",
            "7",
            "4",
            "21",
        ],
        "correct_index": 0,
        "why": "Three electrons have been gained on top of the atom's "
               "original seven.",
    },
    {
        "id": "ks4-subatomic-particles-s22",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why removing an electron changes an atom's charge "
                "but hardly changes its mass.",
        "options": [
            "An electron carries no charge but a large share of the atom's "
            "mass, which stays behind in the ion",
            "An electron carries a full unit of charge but almost no mass",
            "An electron is replaced by a neutron as soon as it leaves, so "
            "the mass is kept the same",
            "An electron takes a proton with it as it leaves the atom, and "
            "the two masses cancel out",
        ],
        "correct_index": 1,
        "why": "Charge and mass are separate properties, and the electron is "
               "large in one and negligible in the other.",
    },
    {
        "id": "ks4-subatomic-particles-s23",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bromine atom's mass number is 80, and it has 35 protons. "
                "Find the number of neutrons in its nucleus.",
        "options": [
            "35",
            "40",
            "45",
            "80",
        ],
        "correct_index": 2,
        "why": "Taking 35 away from 80 leaves the number of neutrons in the "
               "nucleus.",
    },
    {
        "id": "ks4-subatomic-particles-s24",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a non-metal atom tends to form a negatively "
                "charged ion.",
        "options": [
            "It loses protons to the metal it is reacting with, leaving fewer "
            "positive charges",
            "It loses electrons, and each electron lost leaves a negative "
            "charge behind in the atom",
            "It gains neutrons, which carry the negative charge into the "
            "nucleus of the atom",
            "It gains electrons, so the negative charges outnumber the "
            "protons",
        ],
        "correct_index": 3,
        "why": "Extra electrons give more negative charge than the nucleus "
               "can balance.",
    },
    {
        "id": "ks4-subatomic-particles-s25",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass number of an atom that contains 14 "
                "protons and 14 neutrons.",
        "options": [
            "28",
            "14",
            "42",
            "196",
        ],
        "correct_index": 0,
        "why": "The mass number is the protons and neutrons added together.",
    },
    {
        "id": "ks4-subatomic-particles-s26",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the electrons contribute almost nothing to the "
                "mass of an atom even when there are many of them.",
        "options": [
            "Each electron is held outside the nucleus, and only what is "
            "inside the nucleus is counted as mass",
            "Each electron has a relative mass close to zero, so even many "
            "together add very little",
            "Each electron loses its mass as it moves, so a fast-moving "
            "electron weighs nothing at all",
            "Each electron cancels the mass of one proton, leaving only the "
            "neutrons to be counted up",
        ],
        "correct_index": 1,
        "why": "A proton is about 1836 times more massive, so even twenty "
               "electrons barely register.",
    },
    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-subatomic-particles-h05",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A particle has 26 protons, 30 neutrons and 23 electrons. "
                "Determine its mass number and its charge.",
        "options": [
            "Mass number 79, charge 3+",
            "Mass number 56, charge 3-",
            "Mass number 56, charge 3+",
            "Mass number 53, charge neutral",
        ],
        "correct_index": 2,
        "why": "Mass number counts 26 + 30 protons and neutrons, and three "
               "more protons than electrons gives a 3+ charge.",
    },
    {
        "id": "ks4-subatomic-particles-h06",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a K+ ion with an Ar atom, given that potassium has "
                "19 protons and argon 18.",
        "options": [
            "Both carry a positive charge, because each has more protons than "
            "it has electrons",
            "Both have 18 protons, but they differ in how many electrons each "
            "one is carrying",
            "Both are the same element, since a particle's identity is set by "
            "its electron count",
            "Both have 18 electrons, but they have different numbers of "
            "protons",
        ],
        "correct_index": 3,
        "why": "Matching electron counts do not make two particles the same "
               "element, because the proton count differs.",
    },
    {
        "id": "ks4-subatomic-particles-h07",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bromide ion is Br-. Bromine has atomic number 35 and the "
                "ion has mass number 80. Determine its protons, neutrons and "
                "electrons.",
        "options": [
            "35 protons, 45 neutrons, 36 electrons",
            "35 protons, 45 neutrons, 34 electrons",
            "36 protons, 44 neutrons, 36 electrons",
            "35 protons, 46 neutrons, 35 electrons",
        ],
        "correct_index": 0,
        "why": "Neutrons are 80 - 35 = 45, and the 1- charge means one "
               "electron more than the 35 protons.",
    },
    {
        "id": "ks4-subatomic-particles-h08",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why it is wrong to say that an electron has no mass.",
        "options": [
            "An electron has no mass at rest but gains some as it begins to "
            "move around the nucleus",
            "An electron has a small but real mass, which is neglected only "
            "because it is tiny beside a proton's",
            "An electron has the same mass as a proton, and the two are only "
            "distinguished by their charge",
            "An electron has a negative mass, which is why it reduces the "
            "total mass of the atom",
        ],
        "correct_index": 1,
        "why": "Its relative mass is about 1/1836, which is negligible in a "
               "mass-number calculation but is not zero.",
    },
    {
        "id": "ks4-subatomic-particles-h09",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the charge on a particle containing 16 protons, 16 "
                "neutrons and 18 electrons.",
        "options": [
            "Neutral",
            "2+",
            "2-",
            "18-",
        ],
        "correct_index": 2,
        "why": "Two more electrons than protons leaves two negative charges "
               "unbalanced.",
    },
    {
        "id": "ks4-subatomic-particles-h10",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two particles both contain 10 electrons. One has 8 protons "
                "and the other has 12. Compare them.",
        "options": [
            "They are isotopes of one element, because the electron counts "
            "match one another exactly",
            "They are the same element, since the electron counts are equal "
            "and electrons decide identity",
            "They are different elements, but both must be neutral because "
            "each holds ten electrons",
            "They are different elements, one carrying a 2- charge and the "
            "other a 2+ charge",
        ],
        "correct_index": 3,
        "why": "Eight protons against ten electrons gives 2-, and twelve "
               "against ten gives 2+, and the elements differ.",
    },
    {
        "id": "ks4-subatomic-particles-h11",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the number of electrons in a Fe3+ ion, given that "
                "iron has atomic number 26.",
        "options": [
            "23",
            "26",
            "29",
            "3",
        ],
        "correct_index": 0,
        "why": "Three electrons have been removed from the neutral atom's "
               "twenty-six.",
    },
    {
        "id": "ks4-subatomic-particles-h12",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass number of an atom is always a whole "
                "number.",
        "options": [
            "It is rounded to the nearest whole number for convenience when "
            "it is written into a symbol",
            "It counts whole particles, and a nucleus cannot hold part of a "
            "proton or part of a neutron",
            "It is a measured mass, and every measurement of mass comes out "
            "as a whole number of units",
            "It excludes the electrons, whose masses are the only fractions "
            "involved anywhere in an atom",
        ],
        "correct_index": 1,
        "why": "Mass number is a count of nuclear particles, so it can only "
               "take whole-number values.",
    },
    {
        "id": "ks4-subatomic-particles-h13",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom has 4 more neutrons than protons and a mass "
                "number of 24. Determine its atomic number.",
        "options": [
            "14",
            "12",
            "10",
            "20",
        ],
        "correct_index": 2,
        "why": "If protons are p then neutrons are p + 4 and 2p + 4 = 24, so "
               "p = 10.",
    },
    {
        "id": "ks4-subatomic-particles-h14",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the number of neutrons in an atom "
                "can be read straight off the periodic table.",
        "options": [
            "Unsound, because no information about the nucleus appears "
            "anywhere on the periodic table",
            "Sound, because the larger of the two numbers printed for an "
            "element is its neutron count",
            "Sound, because subtracting the group number from the period "
            "number gives the neutron count",
            "Unsound, because the table gives the proton number and a mass "
            "that is an average over isotopes",
        ],
        "correct_index": 3,
        "why": "The table gives a relative atomic mass rather than one "
               "atom's mass number, so a neutron count needs a named isotope.",
    },
    {
        "id": "ks4-subatomic-particles-h15",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the radius of a sodium atom when it "
                "loses its outer electron.",
        "options": [
            "It becomes smaller, because the outermost occupied shell has "
            "been emptied",
            "It becomes larger, because the remaining electrons spread out to "
            "fill the space that is left",
            "It stays the same, because the nucleus is what sets the size of "
            "a particle in the first place",
            "It becomes larger, because losing a charge weakens the pull of "
            "the nucleus on the electrons",
        ],
        "correct_index": 0,
        "why": "Losing the only electron in the outer shell leaves a smaller "
               "particle with one fewer occupied shell.",
    },
    {
        "id": "ks4-subatomic-particles-h16",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which particle count must be known to identify an "
                "unknown element with certainty.",
        "options": [
            "The number of neutrons",
            "The number of protons",
            "The number of electrons",
            "The total number of particles",
        ],
        "correct_index": 1,
        "why": "Neutron and electron counts both vary for one element, but "
               "the proton count never does.",
    },
    {
        "id": "ks4-subatomic-particles-h17",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lithium atom has 3 protons and 4 neutrons. Determine the "
                "numbers of each particle in a Li+ ion.",
        "options": [
            "2 protons, 4 neutrons, 2 electrons",
            "3 protons, 4 neutrons, 4 electrons",
            "3 protons, 4 neutrons, 2 electrons",
            "4 protons, 3 neutrons, 3 electrons",
        ],
        "correct_index": 2,
        "why": "The nucleus is unchanged and one of the three electrons has "
               "been lost.",
    },
    {
        "id": "ks4-subatomic-particles-h18",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the charge on an ion tells you how many "
                "electrons moved, but not which way the mass changed.",
        "options": [
            "The charge comes from neutrons, whose mass and charge are both "
            "altered when an ion is formed",
            "Electrons carry mass but no charge, so the charge on an ion must "
            "have come from somewhere else",
            "The charge comes from protons leaving the nucleus, and protons "
            "are what carry the mass as well",
            "Electrons carry charge but almost no mass, so their number can "
            "change without the mass doing so",
        ],
        "correct_index": 3,
        "why": "Moving electrons changes the charge by whole units while "
               "leaving the mass number exactly where it was.",
    },
    {
        "id": "ks4-subatomic-particles-h19",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the atomic number of an atom whose mass number is "
                "31 and which contains 16 neutrons.",
        "options": [
            "15",
            "16",
            "31",
            "47",
        ],
        "correct_index": 0,
        "why": "Protons are the mass number less the neutrons, so 31 - 16 "
               "gives the atomic number.",
    },
    {
        "id": "ks4-subatomic-particles-h20",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a table of relative charges uses +1 and -1 "
                "rather than the charges measured in coulombs.",
        "options": [
            "Because the charge on a proton has never been measured in "
            "coulombs by any experiment so far",
            "Because the comparison is what matters, and whole numbers make "
            "it easy to see that charges cancel",
            "Because a proton and an electron have charges that differ "
            "slightly, which relative values hide",
            "Because coulombs measure current rather than charge, so they "
            "cannot describe a particle at all",
        ],
        "correct_index": 1,
        "why": "Relative values strip out a common factor and leave the "
               "balance between protons and electrons plain to see.",
    },
    {
        "id": "ks4-subatomic-particles-h21",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom has twice as many neutrons as protons and a "
                "mass number of 39. Explain why this cannot be correct.",
        "options": [
            "No atom is able to hold more neutrons than protons in its "
            "nucleus under any circumstances",
            "A mass number has to be an even number whenever neutrons "
            "outnumber protons in a nucleus",
            "Three times the proton number would have to be 39, giving 13 "
            "protons and 26 neutrons, which is not a real element's isotope",
            "A neutral atom must contain equal numbers of neutrons and "
            "protons, so the ratio given is impossible",
        ],
        "correct_index": 2,
        "why": "The arithmetic does give 13 protons and 26 neutrons, but "
               "aluminium-39 does not exist, so the description is faulty.",
    },
    {
        "id": "ks4-subatomic-particles-h22",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the change in an atom's mass number and its atomic "
                "number when it forms an ion.",
        "options": [
            "The atomic number changes but the mass number does not, since "
            "electrons carry the charge",
            "Both change, because the ion is a different element from the "
            "atom it was formed from",
            "The mass number changes but the atomic number does not, since "
            "electrons contribute to mass",
            "Neither changes, because only the electron count is altered",
        ],
        "correct_index": 3,
        "why": "Mass number counts protons and neutrons and atomic number "
               "counts protons, and neither is touched by moving electrons.",
    },
    {
        "id": "ks4-subatomic-particles-h23",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the number of neutrons in an atom of silver whose "
                "mass number is 108 and whose atomic number is 47.",
        "options": [
            "61",
            "55",
            "47",
            "108",
        ],
        "correct_index": 0,
        "why": "Subtracting 47 from 108 leaves the neutron count.",
    },
    {
        "id": "ks4-subatomic-particles-h24",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a beam of protons is deflected less sharply than "
                "a beam of electrons in the same electric field.",
        "options": [
            "A proton carries a smaller charge, so the field exerts a much "
            "weaker force on it",
            "A proton is far more massive, so the same force changes its path "
            "much less",
            "A proton is positive, and a positive particle is unaffected by "
            "an electric field of any strength",
            "A proton travels more slowly, so it spends longer in the field "
            "and is straightened out again",
        ],
        "correct_index": 1,
        "why": "The two charges are equal in size, so the difference in "
               "deflection comes entirely from the difference in mass.",
    },
    {
        "id": "ks4-subatomic-particles-h25",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a 2+ ion contains two protons.",
        "options": [
            "Sound, because a 2+ charge can only arise in an atom that has "
            "exactly two protons to start with",
            "Sound, because the number written in the charge is always the "
            "count of protons in the nucleus",
            "Unsound, because the 2 records a shortfall of two electrons, not "
            "a total number of protons",
            "Unsound, because a 2+ ion contains two neutrons rather than the "
            "two protons that are claimed",
        ],
        "correct_index": 2,
        "why": "The charge number reports the imbalance between protons and "
               "electrons and says nothing about the proton total.",
    },
    {
        "id": "ks4-subatomic-particles-h26",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce why a particle with 11 protons and 10 electrons "
                "cannot be a neutral atom of neon.",
        "options": [
            "Its charge is 1- rather than neutral, because it holds one more "
            "proton than it does electrons",
            "Its 10 electrons make it neon, so it must be a neutral atom of "
            "that element after all",
            "Its proton and electron counts are both wrong for any element "
            "that appears on the periodic table",
            "Its 11 protons make it sodium, and it carries a 1+ charge as "
            "well",
        ],
        "correct_index": 3,
        "why": "The proton count names the element and the mismatch with the "
               "electron count gives the charge.",
    },
]
