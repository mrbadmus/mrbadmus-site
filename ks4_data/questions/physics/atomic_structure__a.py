"""Physics · Atomic structure — part A: the atom, isotopes, the model's
development, radiation, nuclear equations and half-life.

Six subtopics (spec 6.4.1.1–6.4.2.3), twelve questions each. Every one is a
BASE question — `tier='foundation'`, `triple_only=False` — so nothing here
reaches for Higher-only content.

The distractors are built from the briefs' declared mistakes: electrons put
in the nucleus, mass number read as protons alone, alpha scattering read as
CONFIRMING the plum pudding model, penetrating power confused with ionising
power, beta decay treated as though it dropped the mass number, and
half-life read as "half the time to decay completely" or applied to the
ORIGINAL activity each time rather than to what is left. Two half-life
questions also make the student subtract background before they count the
halvings — one of them is built so that forgetting to subtract lands exactly
on a stated wrong option (12 minutes rather than 8).

No question needs a figure: nuclear changes are written in words
("polonium-210, which has atomic number 84, decays by alpha emission") and
every half-life is stated numerically in the stem.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ── structure-of-atom ───────────────────────────────────────────────
    {
        "id": "ks4-structure-of-atom-e01",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what an electron does when it moves from a shell "
                "further from the nucleus to a shell closer to it.",
        "options": [
            "It absorbs electromagnetic radiation and gains energy",
            "It emits electromagnetic radiation and loses energy",
            "It gains a unit of positive charge from the nucleus",
            "It joins with a proton in the nucleus to make a neutron",
        ],
        "correct_index": 1,
        "why": "A shell closer to the nucleus is a lower energy level, so "
               "the electron must give up energy — and it does so by "
               "emitting electromagnetic radiation.",
    },
    {
        "id": "ks4-structure-of-atom-e02",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the elements in the same group of the periodic "
                "table have in common.",
        "options": [
            "The same total number of electrons in the atom",
            "The same number of neutrons in the nucleus",
            "The same number of occupied electron shells",
            "The same number of electrons in the outer shell",
        ],
        "correct_index": 3,
        "why": "The group number matches the number of outer-shell "
               "electrons, and it is the outer electrons that decide how an "
               "element reacts.",
    },
    {
        "id": "ks4-structure-of-atom-e03",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The radius of an atom is about 1 × 10⁻¹⁰ m. State the "
                "approximate radius of its nucleus.",
        "options": [
            "1 × 10⁻¹⁴ m",
            "1 × 10⁻¹² m",
            "1 × 10⁻¹⁰ m",
            "1 × 10⁻⁸ m",
        ],
        "correct_index": 0,
        "why": "The nuclear radius is about 1/10 000 of the atomic radius, "
               "and 1 × 10⁻¹⁰ m ÷ 10 000 = 1 × 10⁻¹⁴ m.",
    },
    {
        "id": "ks4-structure-of-atom-e04",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the maximum number of electrons that can occupy the "
                "first (innermost) shell of an atom.",
        "options": [
            "8",
            "1",
            "2",
            "18",
        ],
        "correct_index": 2,
        "why": "The first shell is full with 2 electrons; the second and "
               "third shells then hold up to 8 each.",
    },
    {
        "id": "ks4-structure-of-atom-s01",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A carbon atom has 6 protons and 6 neutrons. Describe how "
                "its electrons are arranged in shells.",
        "options": [
            "2 in the first shell and 6 in the second shell",
            "6 in the first shell and none in the second shell",
            "2 in the first shell and 4 in the second shell",
            "4 in the first shell and 2 in the second shell",
        ],
        "correct_index": 2,
        "why": "A neutral carbon atom has 6 electrons; the first shell fills "
               "with 2, leaving 4 for the second shell.",
    },
    {
        "id": "ks4-structure-of-atom-s02",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom has no overall electric charge.",
        "options": [
            "It has equal numbers of protons and electrons, so the +1 and "
            "−1 charges cancel out",
            "The neutrons in the nucleus cancel out the charge carried by "
            "the protons",
            "The electrons are far too light for their charge to have any "
            "effect on the atom",
            "The protons and the neutrons are bound together, so their "
            "charges cancel out",
        ],
        "correct_index": 0,
        "why": "Each proton is +1 and each electron is −1, and a neutral "
               "atom has one electron for every proton, so the total charge "
               "is zero.",
    },
    {
        "id": "ks4-structure-of-atom-s03",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electron in an atom absorbs energy from electromagnetic "
                "radiation. Describe what happens to that electron.",
        "options": [
            "It stays in the same shell but orbits the nucleus more quickly",
            "It moves to a shell that is closer to the nucleus",
            "It moves into the nucleus and becomes a neutron",
            "It moves to a shell that is further from the nucleus",
        ],
        "correct_index": 3,
        "why": "Absorbing energy lifts an electron to a higher energy level, "
               "which is a shell further out from the nucleus.",
    },
    {
        "id": "ks4-structure-of-atom-s04",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sodium atom has 11 electrons and a lithium atom has 3 "
                "electrons. Suggest why the two elements react in similar "
                "ways.",
        "options": [
            "Both atoms have the same number of occupied electron shells",
            "Both atoms have a single electron in their outer shell",
            "Both atoms have the same mass number",
            "Both atoms have the same number of neutrons",
        ],
        "correct_index": 1,
        "why": "Chemical behaviour is decided by the outer-shell electrons: "
               "lithium is 2,1 and sodium is 2,8,1, so each has one outer "
               "electron.",
    },
    {
        "id": "ks4-structure-of-atom-h01",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scale model of an atom is built with the nucleus 2 cm "
                "across. Determine roughly how wide the whole atom should "
                "be in the same model.",
        "options": [
            "20 cm",
            "2 m",
            "20 m",
            "200 m",
        ],
        "correct_index": 3,
        "why": "The atom is about 10 000 times wider than the nucleus, and "
               "2 cm × 10 000 = 20 000 cm = 200 m.",
    },
    {
        "id": "ks4-structure-of-atom-h02",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'An atom is mostly empty space, so most "
                "of its mass must be spread thinly through that space.' "
                "Explain the error in this reasoning.",
        "options": [
            "The reasoning is correct — the mass of an atom is spread evenly "
            "through its whole volume",
            "Volume and mass are not linked in that way — nearly all the "
            "mass is in the tiny nucleus",
            "The atom is not mostly empty space at all — the electron shells "
            "are solid layers of matter",
            "The electrons fill the space between the shells, and they carry "
            "most of the atom's mass",
        ],
        "correct_index": 1,
        "why": "Almost the whole mass sits in the nucleus even though the "
               "nucleus takes up a minute fraction of the atom's volume.",
    },
    {
        "id": "ks4-structure-of-atom-h03",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why it is the electrons, rather than the nucleus, "
                "that decide how an element behaves chemically.",
        "options": [
            "The nucleus is far too small to take part in a reaction, so "
            "only electrons can be involved",
            "Electrons are much lighter than the nucleus, so they move and "
            "react more easily than it does",
            "Only the outer electrons are close enough to be shared or "
            "transferred between atoms when they bond",
            "The nucleus is shielded by its neutrons, which stop it from "
            "reacting with other atoms",
        ],
        "correct_index": 2,
        "why": "Bonding happens when outer-shell electrons are shared or "
               "transferred; the nucleus is buried at the centre and is "
               "unchanged in a chemical reaction.",
    },
    {
        "id": "ks4-structure-of-atom-h04",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom has 2 electrons in its first shell, 8 in its "
                "second and 3 in its third. Predict the number of protons in "
                "its nucleus and explain your answer.",
        "options": [
            "13, because a neutral atom has one proton for every electron "
            "and there are 13 electrons",
            "3, because only the electrons in the outer shell are balanced "
            "by protons in the nucleus",
            "10, because the two full inner shells account for all of the "
            "protons in the nucleus",
            "26, because every electron is balanced by both a proton and a "
            "neutron in the nucleus",
        ],
        "correct_index": 0,
        "why": "The electrons total 2 + 8 + 3 = 13, and a neutral atom has "
               "an equal number of protons.",
    },

    # ── mass-number-isotopes ────────────────────────────────────────────
    {
        "id": "ks4-mass-number-isotopes-e01",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the atomic number of an element.",
        "options": [
            "The total number of protons and neutrons in the nucleus",
            "The number of neutrons in the nucleus",
            "The number of protons in the nucleus",
            "The number of occupied electron shells in the atom",
        ],
        "correct_index": 2,
        "why": "Atomic number counts the protons, and the proton number is "
               "what decides which element an atom is.",
    },
    {
        "id": "ks4-mass-number-isotopes-e02",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which particles are counted by the mass number of an "
                "atom.",
        "options": [
            "The protons and the neutrons together",
            "The protons only",
            "The neutrons only",
            "The protons, neutrons and electrons together",
        ],
        "correct_index": 0,
        "why": "Mass number is the nucleon number, protons + neutrons; "
               "electrons have negligible mass and are not counted.",
    },
    {
        "id": "ks4-mass-number-isotopes-e03",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has 26 protons and 30 neutrons. State its mass "
                "number.",
        "options": [
            "26",
            "56",
            "30",
            "4",
        ],
        "correct_index": 1,
        "why": "Mass number = protons + neutrons = 26 + 30 = 56.",
    },
    {
        "id": "ks4-mass-number-isotopes-e04",
        "subtopic_slug": "mass-number-isotopes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the mass number of an atom when it "
                "loses an electron and becomes a positive ion.",
        "options": [
            "It decreases by 1",
            "It increases by 1",
            "It halves",
            "It does not change",
        ],
        "correct_index": 3,
        "why": "Mass number counts only the particles in the nucleus, and "
               "forming an ion changes nothing but the electrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s01",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A magnesium atom has 12 protons and 12 neutrons. Determine "
                "the numbers of protons, neutrons and electrons in a "
                "magnesium ion, Mg²⁺.",
        "options": [
            "12 protons, 12 neutrons, 12 electrons",
            "10 protons, 12 neutrons, 10 electrons",
            "12 protons, 10 neutrons, 12 electrons",
            "12 protons, 12 neutrons, 10 electrons",
        ],
        "correct_index": 3,
        "why": "Forming a 2+ ion removes two electrons; the nucleus is "
               "untouched, so the proton and neutron counts are unchanged.",
    },
    {
        "id": "ks4-mass-number-isotopes-s02",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bromine-79 and bromine-81 are isotopes, and bromine has "
                "atomic number 35. Compare the numbers of protons, neutrons "
                "and electrons in a neutral atom of each.",
        "options": [
            "Different protons — 35 and 37 — but the same number of neutrons "
            "in each atom",
            "Same protons and electrons, 35 of each, but different neutrons "
            "— 44 and 46",
            "Different protons and different neutrons, because the two are "
            "in fact different elements",
            "Same protons and neutrons, 35 of each, but different numbers "
            "of electrons",
        ],
        "correct_index": 1,
        "why": "Isotopes share the atomic number 35, so 35 protons and 35 "
               "electrons each; the neutron counts are 79 − 35 = 44 and "
               "81 − 35 = 46.",
    },
    {
        "id": "ks4-mass-number-isotopes-s03",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two isotopes of the same element take part in "
                "exactly the same chemical reactions.",
        "options": [
            "They have the same arrangement of outer-shell electrons, and "
            "those electrons do the bonding",
            "They have the same mass number, so their atoms collide with one "
            "another at the same energy",
            "They have the same number of neutrons, and neutrons hold the "
            "atom together during a reaction",
            "They have the same density, so the same number of atoms fits "
            "into a given volume of each",
        ],
        "correct_index": 0,
        "why": "Isotopes have identical proton numbers and therefore "
               "identical electron arrangements, and chemistry is decided by "
               "the outer electrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-s04",
        "subtopic_slug": "mass-number-isotopes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has a mass number of 39 and contains 20 neutrons. "
                "Potassium has atomic number 19 and calcium has atomic "
                "number 20. Determine which element the atom is.",
        "options": [
            "Calcium, because the atom contains 20 neutrons",
            "Calcium, because 39 − 19 gives 20",
            "Potassium, because its atomic number is 39 − 20 = 19",
            "Neither, because no element has a mass number of 39",
        ],
        "correct_index": 2,
        "why": "Atomic number = mass number − neutrons = 39 − 20 = 19, which "
               "is potassium.",
    },
    {
        "id": "ks4-mass-number-isotopes-h01",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample contains atoms with 8 protons and 8 neutrons, "
                "atoms with 8 protons and 10 neutrons, and atoms with 9 "
                "protons and 9 neutrons. Determine how many different "
                "elements and how many different isotopes are present.",
        "options": [
            "Two elements and three isotopes",
            "Three elements and three isotopes",
            "One element and three isotopes",
            "Two elements and two isotopes",
        ],
        "correct_index": 0,
        "why": "The element is set by the proton number, so 8 and 9 give two "
               "elements, while each different proton–neutron combination is "
               "a separate isotope, giving three.",
    },
    {
        "id": "ks4-mass-number-isotopes-h02",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom X has 15 electrons and a mass number of 31. "
                "A neutral atom Y has 15 protons and 16 neutrons. Determine "
                "the relationship between X and Y.",
        "options": [
            "They are isotopes of one element, because their neutron numbers "
            "are different",
            "They are different elements, because X is described by its "
            "electrons and Y by its protons",
            "They are atoms of the same element with the same mass number, "
            "so they are identical",
            "X is an ion of Y, because X has been described by its electron "
            "count rather than its protons",
        ],
        "correct_index": 2,
        "why": "X is neutral, so it has 15 protons and 31 − 15 = 16 "
               "neutrons — exactly the same nucleus as Y.",
    },
    {
        "id": "ks4-mass-number-isotopes-h03",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Tritium is an isotope of hydrogen with mass number 3. "
                "Hydrogen has atomic number 1. Compare a tritium atom with "
                "an ordinary hydrogen-1 atom.",
        "options": [
            "Tritium has three times as many protons and the same number of "
            "neutrons as hydrogen-1",
            "Tritium has two extra electrons in its shell, and that is why "
            "its atom is heavier",
            "Tritium has one proton and three neutrons, so there are four "
            "particles in its nucleus",
            "Tritium has the same single proton plus two neutrons, so its "
            "nucleus is about three times as massive",
        ],
        "correct_index": 3,
        "why": "Both are hydrogen, so both have one proton; tritium's mass "
               "number of 3 means 3 − 1 = 2 neutrons.",
    },
    {
        "id": "ks4-mass-number-isotopes-h04",
        "subtopic_slug": "mass-number-isotopes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Neon-22 must be a different element from "
                "neon-20, because it has a different mass.' Evaluate this "
                "statement.",
        "options": [
            "Correct — a change in the mass number always produces a new "
            "element",
            "Incorrect — the element is fixed by the 10 protons both atoms "
            "have; only the neutron count differs",
            "Incorrect — neon-22 is an ion of neon, rather than a separate "
            "isotope of it",
            "Correct — neon-22 has 12 protons and neon-20 has 10, so they "
            "are different elements",
        ],
        "correct_index": 1,
        "why": "Both nuclei hold 10 protons, so both are neon; neon-22 "
               "simply has 12 neutrons where neon-20 has 10.",
    },

    # ── development-atomic-model ────────────────────────────────────────
    {
        "id": "ks4-development-atomic-model-e01",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the model of the atom that scientists used before the "
                "electron was discovered.",
        "options": [
            "The nuclear model, with a dense centre and electrons orbiting "
            "far outside it",
            "The plum pudding model, with electrons set into a ball of "
            "positive charge",
            "The Bohr model, with electrons held in fixed energy levels "
            "around a nucleus",
            "The solid sphere model, with atoms as tiny balls that cannot be "
            "divided",
        ],
        "correct_index": 3,
        "why": "Until Thomson found the electron in 1897, an atom was "
               "thought to be a tiny indivisible solid sphere.",
    },
    {
        "id": "ks4-development-atomic-model-e02",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist who discovered the electron.",
        "options": [
            "Ernest Rutherford",
            "Niels Bohr",
            "J. J. Thomson",
            "James Chadwick",
        ],
        "correct_index": 2,
        "why": "Thomson's cathode ray experiments of 1897 identified the "
               "electron and showed that atoms have internal structure.",
    },
    {
        "id": "ks4-development-atomic-model-e03",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Place these models of the atom in the order in which "
                "scientists accepted them, earliest first.",
        "options": [
            "Plum pudding, solid sphere, nuclear, Bohr",
            "Solid sphere, plum pudding, nuclear, Bohr",
            "Solid sphere, nuclear, plum pudding, Bohr",
            "Nuclear, Bohr, solid sphere, plum pudding",
        ],
        "correct_index": 1,
        "why": "The indivisible solid sphere came first, the electron gave "
               "the plum pudding model, alpha scattering gave the nuclear "
               "model, and Bohr then added fixed energy levels.",
    },
    {
        "id": "ks4-development-atomic-model-e04",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which particle James Chadwick discovered in 1932.",
        "options": [
            "The neutron",
            "The proton",
            "The electron",
            "The alpha particle",
        ],
        "correct_index": 0,
        "why": "Chadwick's neutron explained why nuclei are heavier than "
               "their protons alone can account for.",
    },
    {
        "id": "ks4-development-atomic-model-s01",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe one feature of the atom that the plum pudding "
                "model and the nuclear model agree on.",
        "options": [
            "Both have the atom containing negative electrons and carrying "
            "no overall charge",
            "Both have the positive charge concentrated in a tiny central "
            "nucleus",
            "Both have the electrons held at fixed distances in separate "
            "energy levels",
            "Both have the atom as mostly empty space with a dense centre",
        ],
        "correct_index": 0,
        "why": "Thomson's model already had electrons and overall "
               "neutrality; what Rutherford changed was where the positive "
               "charge sits.",
    },
    {
        "id": "ks4-development-atomic-model-s02",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to the fraction of alpha "
                "particles deflected through large angles if a foil of the "
                "same thickness were made from a metal with a much smaller "
                "atomic number than gold.",
        "options": [
            "It would be unchanged, because every nucleus deflects an alpha "
            "particle by the same amount",
            "It would be smaller, because a nucleus with less positive "
            "charge repels an alpha particle less strongly",
            "It would be larger, because a lighter nucleus is knocked aside "
            "more easily by the alpha particle",
            "It would fall to zero, because only gold has a nucleus small "
            "enough to deflect alpha particles",
        ],
        "correct_index": 1,
        "why": "The deflection comes from the repulsion between the alpha "
               "particle's +2 charge and the charge on the nucleus, so a "
               "nucleus with fewer protons pushes it aside less.",
    },
    {
        "id": "ks4-development-atomic-model-s03",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alpha particle carries a charge of +2. Explain why this "
                "matters when interpreting the large deflections seen in the "
                "scattering experiment.",
        "options": [
            "The positive alpha particles were attracted by the positive "
            "nucleus, pulling them off course",
            "The positive alpha particles were attracted by the electrons, "
            "which pulled them sideways",
            "The positive alpha particles were repelled by the positive "
            "nucleus, so a close approach turned them sharply",
            "The charge does not matter — the deflections were caused by "
            "collisions with neutrons",
        ],
        "correct_index": 2,
        "why": "Like charges repel, so an alpha particle passing close to "
               "the concentrated positive nucleus is pushed hard away from "
               "its path.",
    },
    {
        "id": "ks4-development-atomic-model-s04",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rutherford's team counted alpha particles for many months "
                "rather than for a single afternoon. Explain why so many "
                "observations were needed.",
        "options": [
            "Because the alpha source grew weaker each time it was used, so "
            "readings had to be averaged",
            "Because a different scientist counted on each day, and their "
            "results had to be compared",
            "Because the gold foil had to be replaced after every alpha "
            "particle struck it",
            "Because only a tiny fraction of alpha particles are deflected "
            "through a large angle, so the pattern shows up only in very "
            "large numbers",
        ],
        "correct_index": 3,
        "why": "Large-angle deflections are rare events, so a reliable "
               "measurement of how often they happen needs an enormous "
               "number of particles counted.",
    },
    {
        "id": "ks4-development-atomic-model-h01",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The gold foil used in the alpha scattering experiment was "
                "only a few atoms thick. Suggest why such a thin foil was "
                "used.",
        "options": [
            "So that each alpha particle would lose all of its energy inside "
            "a single sheet of gold",
            "So that the gold atoms would be forced closer together and "
            "become easier to hit",
            "So that most alpha particles pass through after at most one "
            "close encounter, making the deflections readable",
            "So that the foil would be light enough not to be pushed aside "
            "by the beam of alpha particles",
        ],
        "correct_index": 2,
        "why": "In a foil this thin an alpha particle interacts with "
               "essentially one nucleus, so the pattern of deflections "
               "reflects single scattering events.",
    },
    {
        "id": "ks4-development-atomic-model-h02",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Rutherford's experiment showed "
                "the plum pudding model was wrong, so Thomson was a poor "
                "scientist.'",
        "options": [
            "Correct — a model that is later disproved should never have "
            "been published in the first place",
            "Correct — Thomson ignored scattering evidence that was already "
            "available to him at the time",
            "Incorrect — the plum pudding model was never disproved, it was "
            "only extended by Rutherford",
            "Incorrect — Thomson's model fitted the evidence of its day, and "
            "models change as new evidence appears",
        ],
        "correct_index": 3,
        "why": "A scientific model is judged against the evidence available "
               "when it is made, and replacing it with a better-supported "
               "one is how science is meant to work.",
    },
    {
        "id": "ks4-development-atomic-model-h03",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what the alpha scattering results revealed about "
                "the size of the nucleus with what they revealed about its "
                "charge.",
        "options": [
            "How rarely large deflections happened showed the nucleus is "
            "tiny; that alphas were repelled showed it is positive",
            "How rarely large deflections happened showed the nucleus is "
            "positive; their size showed that it is tiny",
            "The number of particles passing through showed it is positive; "
            "its charge showed that it is dense",
            "Neither size nor charge could be found from this experiment — "
            "only the total mass of the atom",
        ],
        "correct_index": 0,
        "why": "How often a large deflection happens measures how small a "
               "target the nucleus is, while the deflections being "
               "repulsions of a +2 charge shows the nucleus is positive.",
    },
    {
        "id": "ks4-development-atomic-model-h04",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the nuclear model replaced the plum pudding "
                "model because Rutherford was more famous than Thomson. "
                "Explain why this is not how the change happened.",
        "options": [
            "The nuclear model was accepted because it was a simpler picture "
            "than the plum pudding model",
            "The nuclear model was accepted because it explained "
            "experimental results the plum pudding model could not",
            "The nuclear model was accepted because Bohr later supported it "
            "with the idea of fixed electron orbits",
            "The nuclear model was accepted because Chadwick's neutron had "
            "already been discovered by then",
        ],
        "correct_index": 1,
        "why": "A model replaces another when it accounts for observations "
               "the old one fails to explain — here, the large-angle "
               "scattering of alpha particles.",
    },

    # ── radioactive-decay ───────────────────────────────────────────────
    {
        "id": "ks4-radioactive-decay-e01",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what an alpha particle is made of.",
        "options": [
            "Two protons and two neutrons",
            "Two protons and two electrons",
            "A single fast-moving electron",
            "A high-energy electromagnetic wave",
        ],
        "correct_index": 0,
        "why": "An alpha particle is a helium nucleus — two protons and two "
               "neutrons, with a charge of +2.",
    },
    {
        "id": "ks4-radioactive-decay-e02",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate range of alpha radiation in air.",
        "options": [
            "A few metres",
            "A few millimetres",
            "A few centimetres",
            "Several kilometres",
        ],
        "correct_index": 2,
        "why": "Alpha ionises the air so strongly that it gives up all of "
               "its energy within a few centimetres of leaving the source.",
    },
    {
        "id": "ks4-radioactive-decay-e03",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge carried by gamma radiation.",
        "options": [
            "+2",
            "−1",
            "+1",
            "0",
        ],
        "correct_index": 3,
        "why": "Gamma radiation is an electromagnetic wave, so it carries no "
               "charge and no mass.",
    },
    {
        "id": "ks4-radioactive-decay-e04",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the unit in which the activity of a radioactive source "
                "is measured.",
        "options": [
            "The joule (J)",
            "The becquerel (Bq)",
            "The watt (W)",
            "The hertz (Hz)",
        ],
        "correct_index": 1,
        "why": "Activity is the number of nuclei decaying each second, and "
               "1 becquerel is 1 decay per second.",
    },
    {
        "id": "ks4-radioactive-decay-s01",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The count rate measured from a source varies from one "
                "minute to the next, even though the source's half-life is "
                "many years. Explain why.",
        "options": [
            "The detector's efficiency changes as it warms up during the "
            "measurement",
            "Radioactive decay is random, so the number of nuclei decaying "
            "in any one minute varies by chance",
            "The source's activity genuinely rises and falls in a regular "
            "cycle",
            "The tube subtracts the background automatically, and that "
            "correction varies",
        ],
        "correct_index": 1,
        "why": "Decay is a random process: each nucleus has a fixed chance "
               "of decaying, so the count in a given minute scatters about "
               "an average even when the activity is effectively constant.",
    },
    {
        "id": "ks4-radioactive-decay-s02",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source is placed in front of a detector. The count rate "
                "is unchanged when a sheet of paper is put between them, but "
                "falls almost to the background level when a 5 mm aluminium "
                "sheet is added. Determine which radiation the source emits.",
        "options": [
            "Alpha only, because the paper made no difference to the reading",
            "Gamma only, because the count rate fell when aluminium was used",
            "Alpha and gamma, because two different absorbers were needed",
            "Beta only, because it passes through paper but is stopped by a "
            "few millimetres of aluminium",
        ],
        "correct_index": 3,
        "why": "Paper stops alpha and aluminium stops beta, so radiation "
               "that ignores paper but is absorbed by 5 mm of aluminium must "
               "be beta.",
    },
    {
        "id": "ks4-radioactive-decay-s03",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gamma radiation penetrates much further into a "
                "material than alpha radiation does.",
        "options": [
            "Gamma travels faster than alpha, so it passes through before it "
            "can be absorbed",
            "Gamma is a wave rather than a particle, so it is too large to "
            "be stopped by an atom",
            "Gamma has no charge and no mass, so it ionises only rarely and "
            "gives up its energy slowly",
            "Gamma is attracted by the nuclei of the material, which pull it "
            "deeper inside",
        ],
        "correct_index": 2,
        "why": "Ionising is what costs a radiation its energy, and an "
               "uncharged, massless gamma ray ionises far less often than a "
               "charged, massive alpha particle.",
    },
    {
        "id": "ks4-radioactive-decay-s04",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gamma radiation, rather than alpha radiation, "
                "is used to sterilise surgical instruments inside sealed "
                "packets.",
        "options": [
            "Gamma penetrates the packaging and kills bacteria inside "
            "without the packet being opened",
            "Gamma is the most ionising of the radiations, so it destroys "
            "the bacteria fastest",
            "Gamma makes the instruments themselves radioactive, which keeps "
            "them sterile in storage",
            "Gamma is absorbed by the packet, so the radiation cannot escape "
            "and harm the workers",
        ],
        "correct_index": 0,
        "why": "Only gamma is penetrating enough to pass through the sealed "
               "packaging and still ionise the bacteria inside it.",
    },
    {
        "id": "ks4-radioactive-decay-h01",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source is kept in a lead-lined box. A detector outside "
                "the box records a count rate equal to the background count "
                "rate. Suggest what this tells you about the type of "
                "radiation the source emits.",
        "options": [
            "The source has stopped decaying for as long as it is inside the "
            "box",
            "The source must be emitting gamma radiation and nothing else",
            "The source is emitting no radiation of any kind at all",
            "Nothing — lead absorbs all three types, so any of them would "
            "give this reading",
        ],
        "correct_index": 3,
        "why": "Lead absorbs alpha, beta and gamma, so a background-level "
               "reading outside the box is consistent with any of the three.",
    },
    {
        "id": "ks4-radioactive-decay-h02",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student holds a sealed alpha source in their hand for "
                "one minute. Another stands two metres from a sealed gamma "
                "source for one minute. Evaluate which student is at the "
                "greater risk.",
        "options": [
            "The gamma student, because gamma penetrates skin and reaches "
            "organs, while alpha is stopped by skin",
            "The alpha student, because alpha is the most ionising radiation "
            "in every situation",
            "The alpha student, because holding a source is always more "
            "dangerous than standing near one",
            "Neither, because a sealed source cannot emit any radiation "
            "through its container",
        ],
        "correct_index": 0,
        "why": "Outside the body alpha cannot get past the outer layer of "
               "skin, so the penetrating gamma is the greater hazard even "
               "from two metres away.",
    },
    {
        "id": "ks4-radioactive-decay-h03",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the count rate recorded by a Geiger–Müller tube "
                "near a source is not the same number as the activity of "
                "that source.",
        "options": [
            "The counter always reads exactly half the activity, because "
            "half the decays go the wrong way",
            "The tube detects only the radiation that enters it, and it "
            "records background radiation as well",
            "Activity is measured in becquerels and count rate in hertz, so "
            "the two numbers cannot match",
            "The activity of a source cannot be measured at all, because "
            "radioactive decay is random",
        ],
        "correct_index": 1,
        "why": "Radiation is emitted in every direction, so only a fraction "
               "of it enters the tube, and whatever background is present is "
               "counted too.",
    },
    {
        "id": "ks4-radioactive-decay-h04",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector near a source records 1080 counts in 3.0 "
                "minutes. With the source removed it records 45 counts in "
                "3.0 minutes. Determine the corrected count rate of the "
                "source, in counts per minute, and explain why the "
                "correction is needed.",
        "options": [
            "375 counts per minute — the background has to be added to what "
            "the source itself emits",
            "360 counts per minute — background radiation is far too weak to "
            "make any difference",
            "345 counts per minute — background from rocks, cosmic rays and "
            "the air is recorded even with no source present",
            "24 counts per minute — the measured reading is divided by the "
            "background count rate",
        ],
        "correct_index": 2,
        "why": "The two rates are 1080 ÷ 3.0 = 360 and 45 ÷ 3.0 = 15 counts "
               "per minute, and the tube counts everything that reaches it, "
               "so 360 − 15 = 345 counts per minute.",
    },

    # ── nuclear-equations ───────────────────────────────────────────────
    {
        "id": "ks4-nuclear-equations-e01",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of caesium-137 emits a beta particle. State the "
                "mass number of the nucleus that is left.",
        "options": [
            "133",
            "137",
            "138",
            "136",
        ],
        "correct_index": 1,
        "why": "In beta decay a neutron turns into a proton, so the total "
               "number of nucleons — and therefore the mass number — is "
               "unchanged at 137.",
    },
    {
        "id": "ks4-nuclear-equations-e02",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus with atomic number 66 emits an alpha particle. "
                "State the atomic number of the nucleus that is left.",
        "options": [
            "64",
            "62",
            "68",
            "66",
        ],
        "correct_index": 0,
        "why": "An alpha particle carries away two protons, so the atomic "
               "number falls by 2, from 66 to 64.",
    },
    {
        "id": "ks4-nuclear-equations-e03",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a nuclear equation an alpha particle is written with a "
                "mass number and an atomic number. State what these two "
                "numbers are.",
        "options": [
            "Mass number 2 and atomic number 4",
            "Mass number 1 and atomic number 0",
            "Mass number 0 and atomic number −1",
            "Mass number 4 and atomic number 2",
        ],
        "correct_index": 3,
        "why": "An alpha particle is a helium nucleus — two protons and two "
               "neutrons — so its mass number is 4 and its atomic number 2.",
    },
    {
        "id": "ks4-nuclear-equations-e04",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 60 and atomic number 27 emits a "
                "gamma ray. State the mass number and the atomic number of "
                "the nucleus afterwards.",
        "options": [
            "Mass number 56, atomic number 25",
            "Mass number 60, atomic number 28",
            "Mass number 60, atomic number 27",
            "Mass number 59, atomic number 27",
        ],
        "correct_index": 2,
        "why": "Gamma emission carries away energy but no protons and no "
               "neutrons, so both numbers are left exactly as they were.",
    },
    {
        "id": "ks4-nuclear-equations-s01",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Polonium-210, which has atomic number 84, decays by alpha "
                "emission. Determine the mass number and the atomic number "
                "of the daughter nucleus.",
        "options": [
            "Mass number 206, atomic number 84",
            "Mass number 210, atomic number 82",
            "Mass number 206, atomic number 82",
            "Mass number 208, atomic number 82",
        ],
        "correct_index": 2,
        "why": "An alpha particle takes away 4 nucleons and 2 protons: "
               "210 − 4 = 206 and 84 − 2 = 82.",
    },
    {
        "id": "ks4-nuclear-equations-s02",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Strontium-90, which has atomic number 38, decays by beta "
                "emission. Determine the mass number and the atomic number "
                "of the daughter nucleus.",
        "options": [
            "Mass number 89, atomic number 39",
            "Mass number 86, atomic number 36",
            "Mass number 90, atomic number 37",
            "Mass number 90, atomic number 39",
        ],
        "correct_index": 3,
        "why": "Beta decay leaves the mass number at 90 and raises the "
               "atomic number by one, from 38 to 39.",
    },
    {
        "id": "ks4-nuclear-equations-s03",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of nitrogen-16, atomic number 7, changes into a "
                "nucleus of oxygen-16, atomic number 8. Determine which type "
                "of decay has taken place.",
        "options": [
            "Alpha decay, because a different element has been formed",
            "Beta decay, because the mass number is unchanged and the atomic "
            "number has risen by 1",
            "Gamma emission, because the mass number of the nucleus is "
            "unchanged",
            "Alpha decay followed by gamma emission, because both numbers "
            "have changed",
        ],
        "correct_index": 1,
        "why": "Only beta decay leaves the nucleon count alone while turning "
               "a neutron into a proton, which raises the atomic number "
               "by 1.",
    },
    {
        "id": "ks4-nuclear-equations-s04",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of the particles in the nucleus, why beta "
                "decay increases the atomic number by one.",
        "options": [
            "A neutron in the nucleus changes into a proton and an electron, "
            "and the electron is emitted",
            "A proton in the nucleus changes into a neutron, and an electron "
            "is emitted from a shell",
            "An electron from the innermost shell falls into the nucleus and "
            "becomes a proton there",
            "Two neutrons in the nucleus join together to make one proton, "
            "which is then emitted",
        ],
        "correct_index": 0,
        "why": "Beta decay converts a neutron into a proton plus a fast "
               "electron; the new proton stays behind, so the proton count "
               "rises by one.",
    },
    {
        "id": "ks4-nuclear-equations-h01",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radon-220, atomic number 86, decays by alpha emission. The "
                "daughter nucleus then decays by beta emission twice in "
                "succession. Determine the mass number and atomic number of "
                "the final nucleus.",
        "options": [
            "Mass number 216, atomic number 86",
            "Mass number 216, atomic number 82",
            "Mass number 212, atomic number 86",
            "Mass number 220, atomic number 84",
        ],
        "correct_index": 0,
        "why": "The alpha decay gives mass number 216 and atomic number 84, "
               "and each beta decay then adds 1 to the atomic number, "
               "giving 86.",
    },
    {
        "id": "ks4-nuclear-equations-h02",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 214 and atomic number 83 decays in "
                "two steps into a nucleus of mass number 210 and atomic "
                "number 82. Determine the two decays involved.",
        "options": [
            "Two beta decays, one after the other",
            "Two alpha decays, one after the other",
            "One alpha decay and one beta decay",
            "One alpha decay and one gamma emission",
        ],
        "correct_index": 2,
        "why": "Losing 4 from the mass number needs one alpha, which drops "
               "the atomic number to 81, and a beta decay then raises it "
               "back to 82.",
    },
    {
        "id": "ks4-nuclear-equations-h03",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes an equation in which a nucleus of mass "
                "number 230 and atomic number 90 emits an alpha particle to "
                "give a nucleus of mass number 226 and atomic number 88, "
                "plus an electron. Explain the error.",
        "options": [
            "There is no error — both the mass numbers and the atomic "
            "numbers already balance",
            "The mass number of the daughter should fall by 2, not by 4, "
            "when an alpha particle is emitted",
            "The atomic number of the daughter should be 92, because "
            "emitting an alpha particle raises it by 2",
            "The extra electron should not be there: the atomic numbers give "
            "88 + 2 − 1 = 89, which is not 90",
        ],
        "correct_index": 3,
        "why": "An alpha decay emits only the alpha particle, and the mass "
               "numbers and the atomic numbers must each balance across the "
               "two sides.",
    },
    {
        "id": "ks4-nuclear-equations-h04",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect of one alpha decay on an element's "
                "position in the periodic table with the effect of two beta "
                "decays of the same nucleus.",
        "options": [
            "Both of them move the element two places to the left in the "
            "periodic table",
            "Alpha moves it two places left; two beta decays move it two "
            "places right",
            "Alpha moves it two places right; two beta decays move it two "
            "places left",
            "Alpha moves it four places left; two beta decays leave its "
            "position unchanged",
        ],
        "correct_index": 1,
        "why": "Alpha lowers the atomic number by 2 while each beta raises "
               "it by 1, so two betas move the element the opposite way by "
               "the same amount.",
    },

    # ── half-lives ──────────────────────────────────────────────────────
    {
        "id": "ks4-half-lives-e01",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the half-life of a radioactive isotope.",
        "options": [
            "The time taken for the source to decay away completely",
            "The time taken for half of the atoms in the source to be "
            "emitted as radiation",
            "The time taken for the number of undecayed nuclei, or the "
            "activity, to fall to half its value",
            "Half of the time taken for the source to become safe enough to "
            "handle",
        ],
        "correct_index": 2,
        "why": "In one half-life the number of undecayed nuclei — and so the "
               "activity — falls to one half of whatever it was at the start "
               "of that interval.",
    },
    {
        "id": "ks4-half-lives-e02",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the fraction of the original undecayed nuclei that "
                "remains after two half-lives.",
        "options": [
            "One half",
            "One quarter",
            "One eighth",
            "None — the sample has fully decayed",
        ],
        "correct_index": 1,
        "why": "Each half-life halves what is left, so after two half-lives "
               "½ × ½ = ¼ of the nuclei remain.",
    },
    {
        "id": "ks4-half-lives-e03",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why it is impossible to say when one particular "
                "unstable nucleus will decay.",
        "options": [
            "Radioactive decay is a random process",
            "The nucleus decays only once it has been heated enough",
            "The nucleus decays exactly one half-life after it is formed",
            "Measuring instruments are not yet accurate enough to tell",
        ],
        "correct_index": 0,
        "why": "Decay is spontaneous and random, so only the behaviour of a "
               "large number of nuclei together is predictable.",
    },
    {
        "id": "ks4-half-lives-e04",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iodine-131 has a half-life of 8 days. A sample has an "
                "activity of 600 Bq today. State its activity 8 days from "
                "now.",
        "options": [
            "0 Bq",
            "150 Bq",
            "600 Bq",
            "300 Bq",
        ],
        "correct_index": 3,
        "why": "Exactly one half-life passes, so the activity halves: "
               "600 Bq ÷ 2 = 300 Bq.",
    },
    {
        "id": "ks4-half-lives-s01",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source has an activity of 2400 Bq and a half-life of 15 "
                "minutes. Calculate its activity one hour later.",
        "options": [
            "150 Bq",
            "300 Bq",
            "600 Bq",
            "1200 Bq",
        ],
        "correct_index": 0,
        "why": "One hour is 60 ÷ 15 = 4 half-lives, so the activity halves "
               "four times: 2400 → 1200 → 600 → 300 → 150 Bq.",
    },
    {
        "id": "ks4-half-lives-s02",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample contains 8.0 × 10⁸ undecayed nuclei of an isotope "
                "whose half-life is 3 years. Calculate the number of "
                "undecayed nuclei left after 9 years.",
        "options": [
            "4.0 × 10⁸",
            "2.7 × 10⁸",
            "2.0 × 10⁸",
            "1.0 × 10⁸",
        ],
        "correct_index": 3,
        "why": "Nine years is three half-lives, so the number left is "
               "8.0 × 10⁸ ÷ 2 ÷ 2 ÷ 2 = 1.0 × 10⁸.",
    },
    {
        "id": "ks4-half-lives-s03",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The activity of a source falls from 480 Bq to 60 Bq over 24 "
                "hours. Determine the half-life of the source.",
        "options": [
            "24 hours",
            "12 hours",
            "8 hours",
            "3 hours",
        ],
        "correct_index": 2,
        "why": "The activity halves three times (480 → 240 → 120 → 60 Bq), "
               "so three half-lives take 24 hours and one takes 8 hours.",
    },
    {
        "id": "ks4-half-lives-s04",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An isotope has a half-life of 6 hours. Determine how long "
                "it takes for its activity to fall to one sixteenth of its "
                "starting value.",
        "options": [
            "16 hours",
            "24 hours",
            "48 hours",
            "96 hours",
        ],
        "correct_index": 1,
        "why": "One sixteenth is (½)⁴, so four half-lives are needed: "
               "4 × 6 hours = 24 hours.",
    },
    {
        "id": "ks4-half-lives-h01",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source has an activity of 3200 Bq. Twenty hours later "
                "its activity is 200 Bq. Determine what its activity was 10 "
                "hours after the first measurement.",
        "options": [
            "1600 Bq",
            "800 Bq",
            "400 Bq",
            "1000 Bq",
        ],
        "correct_index": 1,
        "why": "The activity fell to one sixteenth in 20 hours, which is "
               "four half-lives, so the half-life is 5 hours and 10 hours is "
               "two halvings: 3200 → 1600 → 800 Bq.",
    },
    {
        "id": "ks4-half-lives-h02",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Source A has an activity of 800 Bq and a half-life of 2 "
                "days. Source B has an activity of 200 Bq and a half-life of "
                "8 days. Determine which has the greater activity 8 days "
                "later.",
        "options": [
            "B, at 100 Bq against A's 50 Bq",
            "A, because it started with four times B's activity",
            "They are equal, at 100 Bq each",
            "A, at 200 Bq against B's 100 Bq",
        ],
        "correct_index": 0,
        "why": "In 8 days A goes through four half-lives (800 → 400 → 200 → "
               "100 → 50 Bq) while B goes through only one (200 → 100 Bq), "
               "so the weaker but longer-lived source ends up ahead.",
    },
    {
        "id": "ks4-half-lives-h03",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector records 140 counts per second near a source, "
                "falling to 35 counts per second 24 minutes later. The "
                "background count rate in the room is 20 counts per second. "
                "Determine the half-life of the source.",
        "options": [
            "24 minutes",
            "6 minutes",
            "12 minutes",
            "8 minutes",
        ],
        "correct_index": 3,
        "why": "Subtracting the background first gives 120 → 60 → 30 → 15 "
               "counts per second, three half-lives in 24 minutes, so the "
               "half-life is 8 minutes.",
    },
    {
        "id": "ks4-half-lives-h04",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'This source has a half-life of 2 days, so "
                "after 4 days it will have decayed completely.' Evaluate "
                "this statement.",
        "options": [
            "Correct — two half-lives always take the activity of a source "
            "down to zero",
            "Correct — the whole sample decays within two half-lives, though "
            "the activity falls to zero later",
            "Incorrect — after 4 days a quarter of the original activity is "
            "left, because each half-life halves what remains",
            "Incorrect — after 4 days half of the original activity is left, "
            "because two half-lives make one whole life",
        ],
        "correct_index": 2,
        "why": "Each half-life halves what is left rather than the original, "
               "so 4 days is two half-lives and one quarter of the activity "
               "remains.",
    },
]
