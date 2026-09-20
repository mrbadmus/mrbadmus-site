"""Physics · Atomic structure — the MRB-338 expansion of `structure-of-atom`.

One leaf only: AQA 8463 §6.4.1.1 — the three subatomic particles with their
charges, masses and locations, the shell model (2, 8, 8), the size of the atom
against the size of its nucleus, and what changes and what does not when an ion
forms. The original twelve rows in `atomic_structure__a.py` take the shell
transition, the group rule, the nuclear-radius order of magnitude, the first
shell's capacity, carbon's arrangement and the scale-model arithmetic; this
file takes everything those twelve leave — proton and neutron charge and mass
side by side, the electron's negligible 1/1836, the second and third shells,
the arrangements of chlorine, potassium, calcium and the ions of fluorine,
sodium and aluminium, the period-from-shells rule, the nm-to-m conversion, the
volume ratio that follows from the radius ratio, and why removing an electron
leaves both the nucleus and the mass alone.

The weight follows the CONTENT. `easier` stays at eight because recall here is
three particles, three shell capacities and two sizes, and asking it a ninth
way is the same question wearing different words. The demand lives in
`standard` and `harder`, where an arrangement has to be built from a count and
then read back as a group or a period, or where a ratio has to be carried
through two steps — so that is where the twenty-two-row bands sit.

Orders of magnitude are written the way the original twelve write them, with
Unicode superscripts (1 × 10⁻¹⁰ m). No question needs a figure: every
arrangement is given as a count or as the shell list itself.

⚠️ Every wrong option carries its own reason at the key's level of detail
(brief §9.2), so that in three sets out of four the longest option is a
DISTRACTOR. The added clauses are false ones — padding a wrong option with a
true clause strengthens it (§9.9).
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The three particles with charge, mass and location; the shell
    # capacities the first twelve never ask; the atom's own size in nm.
    {
        "id": "ks4-structure-of-atom-e05",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge on a proton and where in the atom it is "
                "found.",
        "options": [
            "A charge of −1, and it is found in the nucleus",
            "A charge of +1, and it is found in the outer shell",
            "No charge at all, and it is found in the nucleus",
            "A charge of +1, and it is found in the nucleus",
        ],
        "correct_index": 3,
        "why": "A proton carries a charge of +1 and sits in the nucleus "
               "alongside the neutrons.",
    },
    {
        "id": "ks4-structure-of-atom-e06",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the mass of an electron compared with the mass of a "
                "proton.",
        "options": [
            "About 1/1836 of it, which is small enough to be ignored",
            "About 1836 times larger, which is why it moves so quickly",
            "Roughly the same, since both are subatomic particles",
            "Exactly half of it, because its charge is also smaller",
        ],
        "correct_index": 0,
        "why": "An electron has about 1/1836 of a proton's mass, so its mass "
               "is taken as negligible.",
    },
    {
        "id": "ks4-structure-of-atom-e07",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the subatomic particle that carries no electric charge.",
        "options": [
            "The proton",
            "The neutron",
            "The electron",
            "The nucleus",
        ],
        "correct_index": 1,
        "why": "The neutron is electrically neutral; the proton is +1 and the "
               "electron is −1.",
    },
    {
        "id": "ks4-structure-of-atom-e08",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom's shells fill from the inside outwards. State how "
                "many electrons fit in the second shell once it is full.",
        "options": [
            "2",
            "18",
            "8",
            "10",
        ],
        "correct_index": 2,
        "why": "The second shell holds up to 8 electrons, as does the third "
               "for the first twenty elements.",
    },
    {
        "id": "ks4-structure-of-atom-e09",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate radius of an atom in nanometres.",
        "options": [
            "10 nm",
            "100 nm",
            "0.000 1 nm",
            "0.1 nm",
        ],
        "correct_index": 3,
        "why": "An atomic radius of about 1 × 10⁻¹⁰ m is 0.1 nm, since one "
               "nanometre is 1 × 10⁻⁹ m.",
    },
    {
        "id": "ks4-structure-of-atom-e10",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a neutral atom, state which other count is always equal "
                "to the number of protons.",
        "options": [
            "The number of neutrons, since the two share the nucleus",
            "The number of occupied electron shells in the atom",
            "The number of electrons in the shells",
            "The number of outer-shell electrons, which is what fixes the "
                "group the element is in",
        ],
        "correct_index": 2,
        "why": "A neutral atom has one electron for every proton, so the two "
               "counts are equal and the charges cancel.",
    },
    {
        "id": "ks4-structure-of-atom-e11",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where almost all of the mass of an atom is found.",
        "options": [
            "Spread evenly through the whole volume of the atom, because "
                "mass always follows volume",
            "In the electron shells, because an atom holds more electrons "
                "than anything else",
            "In the empty space between the nucleus and the shells",
            "In the nucleus, in the protons and the neutrons",
        ],
        "correct_index": 3,
        "why": "Protons and neutrons each have a mass of about 1 atomic mass "
               "unit while an electron's is negligible, so the nucleus holds "
               "nearly all of it.",
    },
    {
        "id": "ks4-structure-of-atom-e12",
        "subtopic_slug": "structure-of-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sodium atom has 11 electrons. State how those electrons "
                "are arranged in shells.",
        "options": [
            "2, 8, 1",
            "8, 2, 1",
            "2, 2, 7",
            "1, 8, 2",
        ],
        "correct_index": 0,
        "why": "Shells fill from the innermost outwards — 2 in the first, 8 "
               "in the second, leaving 1 in the third.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Arrangements built from a count and read back as a group or a period;
    # the size conversions; what an ion changes and what it leaves alone.
    {
        "id": "ks4-structure-of-atom-s05",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom of chlorine has 17 electrons. Determine how many "
                "electron shells of the atom are occupied.",
        "options": [
            "3, because the first two shells hold 10 between them and 7 "
                "electrons are still left over",
            "2, because 17 electrons will fit inside the first two shells",
            "4, because no shell beyond the first is able to hold as many "
                "as 8",
            "17, because each electron takes up an occupied shell of its own",
        ],
        "correct_index": 0,
        "why": "2 + 8 = 10 electrons fill the first two shells, and the "
               "remaining 7 occupy a third shell.",
    },
    {
        "id": "ks4-structure-of-atom-s06",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the electron arrangement of a neutral chlorine "
                "atom, which has 17 electrons.",
        "options": [
            "2, 8, 8, 1",
            "2, 8, 7",
            "2, 7, 8",
            "8, 8, 1",
        ],
        "correct_index": 1,
        "why": "The first shell takes 2 and the second takes 8, leaving 7 "
               "electrons in the third shell.",
    },
    {
        "id": "ks4-structure-of-atom-s07",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has the electron arrangement 2, 8, 2. Determine "
                "which group of the periodic table it belongs to.",
        "options": [
            "Group 3, counting one group for each occupied shell",
            "Group 12, adding all of its electrons",
            "Group 2, matching the electrons in its outer shell",
            "Group 8, matching the eight electrons in its full second shell",
        ],
        "correct_index": 2,
        "why": "The group number matches the number of outer-shell "
               "electrons, and this atom has 2 of them.",
    },
    {
        "id": "ks4-structure-of-atom-s08",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The electrons in an atom are arranged 2, 8, 5. State the "
                "period of the periodic table this atom occupies.",
        "options": [
            "The fifth period, matching the 5 electrons in its outer shell",
            "The second period, because its second shell has been filled",
            "The fifteenth period, matching the 15 electrons it holds "
                "altogether across its shells",
            "The third period, because it occupies three shells",
        ],
        "correct_index": 3,
        "why": "The period number is the number of occupied electron shells, "
               "and this atom occupies three.",
    },
    {
        "id": "ks4-structure-of-atom-s09",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has a radius of 0.15 nm. Calculate its radius in "
                "metres.",
        "options": [
            "1.5 × 10⁻⁸ m",
            "1.5 × 10⁻¹⁰ m",
            "1.5 × 10⁻¹² m",
            "0.15 × 10⁻⁹ m, which cannot be written any more simply",
        ],
        "correct_index": 1,
        "why": "One nanometre is 1 × 10⁻⁹ m, so 0.15 nm is 0.15 × 10⁻⁹ m, "
               "which is 1.5 × 10⁻¹⁰ m.",
    },
    {
        "id": "ks4-structure-of-atom-s10",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass of an atom is taken as the number of "
                "protons plus the number of neutrons.",
        "options": [
            "Because electrons have no mass whatsoever, so nothing at all "
                "is being left out of the total",
            "Because the electrons of an atom are shared with its "
                "neighbours and so belong to no single atom to be counted",
            "Because protons and neutrons each have a mass of about 1 unit "
                "while an electron's is negligible",
            "Because only a particle inside the nucleus is heavy enough to "
                "register on a laboratory balance",
        ],
        "correct_index": 2,
        "why": "A proton and a neutron each have a mass of about 1 atomic "
               "mass unit, and an electron has roughly 1/1836 of that, so "
               "the electrons contribute almost nothing.",
    },
    {
        "id": "ks4-structure-of-atom-s11",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom loses two electrons. Describe the effect on "
                "its overall charge and on its mass.",
        "options": [
            "Charge becomes +2; mass is almost unchanged",
            "Charge becomes −2; mass is almost unchanged",
            "Charge becomes +2; mass falls by two units",
            "Charge stays at zero; mass falls by two units",
        ],
        "correct_index": 0,
        "why": "Losing two negative electrons leaves two unbalanced protons, "
               "so the charge is +2, and the electrons taken away carry "
               "almost no mass.",
    },
    {
        "id": "ks4-structure-of-atom-s12",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an atom is described as being mostly empty "
                "space.",
        "options": [
            "Its electrons move so quickly that they are somewhere else "
                "most of the time, leaving the rest of it empty",
            "Its electrons are so light that the space they occupy counts "
                "as empty",
            "It contains gaps between its shells that other atoms can slide "
                "into",
            "Its nucleus takes up only a tiny fraction of the atom's volume "
                "and its electrons are spread far outside it",
        ],
        "correct_index": 3,
        "why": "The nuclear radius is about 1/10 000 of the atomic radius, so "
               "the nucleus occupies an almost vanishing part of the atom's "
               "volume.",
    },
    {
        "id": "ks4-structure-of-atom-s13",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus is 10 000 times smaller than the atom containing "
                "it. Determine the radius of the nucleus in an atom whose own "
                "radius is 2 × 10⁻¹⁰ m.",
        "options": [
            "2 × 10⁻⁶ m",
            "2 × 10⁻¹² m",
            "2 × 10⁻¹⁴ m",
            "2 × 10⁻²⁰ m",
        ],
        "correct_index": 2,
        "why": "Dividing 2 × 10⁻¹⁰ m by 10 000, which is 10⁴, gives "
               "2 × 10⁻¹⁴ m.",
    },
    {
        "id": "ks4-structure-of-atom-s14",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fluorine atom has 9 electrons and gains one more to "
                "become a fluoride ion. Determine the electron arrangement "
                "of that ion.",
        "options": [
            "2, 7",
            "2, 8",
            "2, 8, 1",
            "1, 8, 1",
        ],
        "correct_index": 1,
        "why": "Gaining one electron takes the count from 9 to 10, which "
               "fills the first shell with 2 and the second with 8.",
    },
    {
        "id": "ks4-structure-of-atom-s15",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sodium ion and a neon atom have the same electron "
                "arrangement. Explain how that is possible.",
        "options": [
            "The sodium atom has lost one electron, leaving 10 in the same "
                "arrangement as neon's 10",
            "Sodium and neon stand next to one another in the periodic "
                "table, so the shells of the two elements always fill in "
                "step",
            "The sodium ion has taken one of neon's electrons, so the two "
                "particles now match",
            "The two elements sit in the same group of the periodic table, "
                "so both have the same outer shell",
        ],
        "correct_index": 0,
        "why": "Sodium's 11 electrons become 10 when the ion forms, and 10 "
               "electrons arrange as 2, 8 — exactly neon's arrangement.",
    },
    {
        "id": "ks4-structure-of-atom-s16",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potassium atom has 19 electrons. Determine how they are "
                "arranged in shells.",
        "options": [
            "2, 8, 9",
            "8, 8, 2, 1",
            "2, 9, 8",
            "2, 8, 8, 1",
        ],
        "correct_index": 3,
        "why": "The first three shells take 2, 8 and 8, which is 18, leaving "
               "one electron in a fourth shell.",
    },
    {
        "id": "ks4-structure-of-atom-s17",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why every element in the same period of the "
                "periodic table has the same number of occupied electron "
                "shells.",
        "options": [
            "Because the elements along a period all hold the same number "
                "of electrons in their outer shell, which is what a period "
                "counts",
            "Because a period is defined by how many shells the atoms of "
                "its elements have in use",
            "Because every period holds exactly eight elements, one for "
                "each place available in a filled shell",
            "Because the elements along a period all have nuclei carrying "
                "the same total positive charge",
        ],
        "correct_index": 1,
        "why": "The rows of the periodic table are built so that a new "
               "period begins each time a new shell starts to fill.",
    },
    {
        "id": "ks4-structure-of-atom-s18",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why energy must be supplied before an electron can "
                "move to a shell further from the nucleus.",
        "options": [
            "The outer shells of the atom are already full, so room has to "
                "be made inside one of them first",
            "The electron must be given extra mass to reach a larger shell",
            "The electron is attracted to the positive nucleus, so work "
                "must be done against that attraction to move it away",
            "The electron has to be turned positive before it will move out",
        ],
        "correct_index": 2,
        "why": "A negative electron is attracted to the positive nucleus, so "
               "moving it further out means working against that "
               "attraction.",
    },
    {
        "id": "ks4-structure-of-atom-s19",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom contains 12 protons. Determine how many "
                "electrons it has and how they are arranged.",
        "options": [
            "12 electrons, arranged 2, 8, 2",
            "12 electrons, arranged 2, 2, 8",
            "6 electrons, arranged 2, 4, because the protons pair up",
            "24 electrons, arranged 2, 8, 8, 6, a pair for every proton",
        ],
        "correct_index": 0,
        "why": "A neutral atom has as many electrons as protons, and 12 "
               "electrons fill the shells as 2, 8, 2.",
    },
    {
        "id": "ks4-structure-of-atom-s20",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the mass and the charge of a proton with those of a "
                "neutron.",
        "options": [
            "The proton is the heavier of the two, and both of them carry a "
                "charge of +1",
            "The neutron is the heavier of the two, and it is the only one "
                "of them carrying any charge at all",
            "Both have a mass of about 1 unit; the proton is +1 and the "
                "neutron is −1",
            "Both have a mass of about 1 unit; the proton is +1 and the "
                "neutron is neutral",
        ],
        "correct_index": 3,
        "why": "Both have a mass of about 1 atomic mass unit, but only the "
               "proton is charged, at +1.",
    },
    {
        "id": "ks4-structure-of-atom-s21",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beam of electrons is deflected as it crosses an electric "
                "field, but a beam of neutrons passing through the same "
                "field is not. Explain why.",
        "options": [
            "Neutrons are so much heavier than electrons that an electric "
                "field of this strength cannot deflect them by any "
                "measurable amount",
            "Electrons carry a charge of −1 and neutrons carry none, and "
                "only a charged particle feels a force in an electric field",
            "Neutrons cross the field too quickly for it to have time to "
                "act on them",
            "Neutrons are shielded by the protons that sat beside them in "
                "the nucleus",
        ],
        "correct_index": 1,
        "why": "An electric field exerts a force only on charged particles, "
               "and the neutron is electrically neutral.",
    },
    {
        "id": "ks4-structure-of-atom-s22",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why only the outer-shell electrons of an atom take "
                "part in chemical bonding.",
        "options": [
            "Only the outer electrons are loosely enough held and close "
                "enough to another atom to be shared or transferred",
            "Only the outer electrons are able to move at all, because "
                "every shell inside them has already been filled completely",
            "Only the outer electrons carry a negative charge, the inner "
                "ones having been neutralised by the nucleus",
            "Only the outer electrons are heavy enough to be pulled across "
                "to a second atom",
        ],
        "correct_index": 0,
        "why": "The outer electrons are furthest from the nucleus and "
               "nearest a neighbouring atom, so they are the ones shared or "
               "transferred when bonds form.",
    },
    {
        "id": "ks4-structure-of-atom-s23",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Atom J has 7 electrons and atom K has 13 electrons. "
                "Determine which of them occupies more electron shells.",
        "options": [
            "J, because the fewer the electrons the further out they spread",
            "K, because 13 electrons need a third shell while 7 need two",
            "Both the same, since both of them are neutral atoms",
            "K, because each extra electron opens a new shell of its own",
        ],
        "correct_index": 1,
        "why": "7 electrons arrange as 2, 5 in two shells; 13 arrange as "
               "2, 8, 3 and so need three.",
    },
    {
        "id": "ks4-structure-of-atom-s24",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the nucleus of an atom compares with the whole "
                "atom in terms of size and of mass.",
        "options": [
            "About a tenth of the radius of the atom, and holding about a "
                "tenth of the atom's mass as well",
            "Tiny in size — about 1/10 000 of the radius — yet holding "
                "nearly all of the mass",
            "Almost the whole size of the atom, and holding almost all of "
                "its mass into the bargain",
            "Tiny in size — about 1/10 000 of the radius — and holding "
                "about 1/10 000 of the mass",
        ],
        "correct_index": 1,
        "why": "The nucleus has about 1/10 000 of the atomic radius but "
               "contains all the protons and neutrons, and so nearly all "
               "the mass.",
    },
    {
        "id": "ks4-structure-of-atom-s25",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has a radius of 1 × 10⁻¹⁰ m and its nucleus has a "
                "radius of 1 × 10⁻¹⁴ m. Calculate how many times larger the "
                "atomic radius is.",
        "options": [
            "100 times",
            "1 000 000 times",
            "4 times, from the difference between the two powers of ten",
            "10 000 times",
        ],
        "correct_index": 3,
        "why": "Dividing 10⁻¹⁰ by 10⁻¹⁴ gives 10⁴, which is 10 000.",
    },
    {
        "id": "ks4-structure-of-atom-s26",
        "subtopic_slug": "structure-of-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has three occupied shells holding 2, 8 and 8 "
                "electrons. State its total number of electrons and whether "
                "its outer shell is full.",
        "options": [
            "18 electrons, and the outer shell is full",
            "18 electrons, and the outer shell has room for 10 more",
            "16 electrons, and the outer shell is therefore full",
            "18 electrons, and the outer shell is only half filled",
        ],
        "correct_index": 0,
        "why": "2 + 8 + 8 = 18, and 8 is the capacity of the third shell for "
               "the first twenty elements, so it is full.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Ratios carried through two steps, ion counts worked backwards from a
    # charge, and the misconception set met from the wrong side.
    {
        "id": "ks4-structure-of-atom-h05",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The radius of an atom is about 10 000 times the radius of "
                "its nucleus. Determine roughly how many times greater the "
                "volume of the atom is than the volume of its nucleus.",
        "options": [
            "30 000 times, because a volume has three dimensions to fill "
                "and each one takes the ratio again",
            "1 × 10⁸ times, since the ratio of the radii is squared",
            "1 × 10¹² times, since the ratio of the radii is cubed",
            "10 000 times, since a volume rises in step with its radius",
        ],
        "correct_index": 2,
        "why": "Volume goes as the cube of the radius, so a radius ratio of "
               "10⁴ gives a volume ratio of (10⁴)³ = 10¹².",
    },
    {
        "id": "ks4-structure-of-atom-h06",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nearly all of an atom's mass sits inside a nucleus that "
                "occupies a minute fraction of the atom's volume. Explain "
                "what this shows about the density of nuclear material.",
        "options": [
            "It is the same as the average density of the atom, because the "
                "mass and the volume being divided both belong to that one "
                "atom",
            "It is far lower than the average density of the atom, because "
                "a nucleus contains only a handful of particles",
            "It cannot be compared at all, because a nucleus is far too "
                "small for a density to be defined for it",
            "It is far greater than the average density of the atom, "
                "because a large mass is packed into a very small volume",
        ],
        "correct_index": 3,
        "why": "Density is mass divided by volume, so almost all the mass in "
               "almost none of the volume makes nuclear material "
               "extraordinarily dense.",
    },
    {
        "id": "ks4-structure-of-atom-h07",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ion carries a charge of 3+ and contains 10 electrons. "
                "Determine the number of protons in its nucleus.",
        "options": [
            "7, because the charge is taken away from the electrons",
            "13, because three electrons have been lost from the atom",
            "10, because the two counts must match in any particle",
            "30, because the charge multiplies the number of shells",
        ],
        "correct_index": 1,
        "why": "A 3+ charge means three more protons than electrons, so "
               "10 + 3 = 13 protons.",
    },
    {
        "id": "ks4-structure-of-atom-h08",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A negative ion holds 18 electrons and has an overall charge "
                "of 2−. Calculate how many protons its nucleus must contain.",
        "options": [
            "20, because the charge is added to the electron count",
            "18, because forming an ion changes neither count",
            "16, because two electrons have been gained",
            "9, because a 2− charge means the electrons doubled",
        ],
        "correct_index": 2,
        "why": "A 2− charge means two more electrons than protons, so "
               "18 − 2 = 16 protons.",
    },
    {
        "id": "ks4-structure-of-atom-h09",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that an atom arranged 2, 8, 1 and an ion "
                "arranged 2, 8 must be different elements, because their "
                "electron arrangements differ. Explain the error.",
        "options": [
            "The two arrangements are in fact identical to one another once "
                "the shells have been counted properly",
            "An ion is not an element, so no comparison can be made",
            "Which element a particle is depends on its proton number, and "
                "losing an electron leaves that number untouched",
            "The arrangement does fix the element, so the shells have "
                "simply been miscounted",
        ],
        "correct_index": 2,
        "why": "The element is set by the number of protons in the nucleus, "
               "and forming an ion changes only the electron count.",
    },
    {
        "id": "ks4-structure-of-atom-h10",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass of an atom barely changes when it "
                "becomes an ion, even though a particle has been removed "
                "from it.",
        "options": [
            "Because the nucleus swells very slightly to make up for "
                "whatever the atom has just lost from its outer shell",
            "Because an electron carries only about 1/1836 of the mass of a "
                "proton or a neutron",
            "Because the departing electron is replaced straight away by a "
                "neutron taken from the nucleus",
            "Because the mass of an atom depends on its volume, and the ion "
                "keeps the volume it had",
        ],
        "correct_index": 1,
        "why": "The mass removed is that of a single electron, roughly "
               "1/1836 of a nucleon's mass, so the total is almost "
               "unaffected.",
    },
    {
        "id": "ks4-structure-of-atom-h11",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Element X has the arrangement 2, 8, 2 and element Y has the "
                "arrangement 2, 2. Predict whether the two will react in "
                "similar ways and justify your prediction.",
        "options": [
            "Yes — each has 2 electrons in its outer shell, and the outer "
                "shell decides chemical behaviour",
            "No — X occupies three shells against Y's two, and it is the "
                "number of occupied shells that settles how an element "
                "reacts",
            "Yes — each holds an even number of electrons in total, and "
                "that is what governs the reactions an element takes part in",
            "No — X holds 12 electrons in all and Y holds 4, so their "
                "reactions must differ",
        ],
        "correct_index": 0,
        "why": "Both are group 2 elements with two outer-shell electrons, "
               "and it is the outer shell that takes part in bonding.",
    },
    {
        "id": "ks4-structure-of-atom-h12",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutral atom has 20 electrons. Determine its electron "
                "arrangement and the group of the periodic table it is in.",
        "options": [
            "2, 8, 10 and group 10",
            "2, 8, 8, 2 and group 4, one group for each occupied shell",
            "2, 10, 8 and group 8",
            "2, 8, 8, 2 and group 2",
        ],
        "correct_index": 3,
        "why": "The first three shells hold 2, 8 and 8, leaving 2 in a "
               "fourth shell, and two outer electrons put the element in "
               "group 2.",
    },
    {
        "id": "ks4-structure-of-atom-h13",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that taking an electron away from an atom "
                "makes its nucleus smaller. Explain the error.",
        "options": [
            "The nucleus does shrink a little, but by far too little for "
                "school apparatus to measure",
            "The electron comes from a shell outside the nucleus, so the "
                "protons and neutrons are left exactly as they were",
            "The nucleus grows a little instead, no longer being held "
                "together by that electron",
            "The nucleus loses one of its protons at the same moment, and "
                "that is what makes it smaller",
        ],
        "correct_index": 1,
        "why": "Electrons occupy shells around the nucleus, so removing one "
               "changes the electron count and leaves the nucleus "
               "unchanged.",
    },
    {
        "id": "ks4-structure-of-atom-h14",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has 15 electrons. Determine how many are in its "
                "outer shell and how many more it would need to fill that "
                "shell.",
        "options": [
            "5 in the outer shell, needing 3 more",
            "5 in the outer shell, needing 5 more",
            "3 in the outer shell, needing 5 more",
            "7 in the outer shell, needing 1 more",
        ],
        "correct_index": 0,
        "why": "15 electrons arrange as 2, 8, 5, and a third shell holding "
               "8 needs 3 further electrons.",
    },
    {
        "id": "ks4-structure-of-atom-h15",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why more energy is needed to remove an electron "
                "from the first shell of an atom than from its outer shell.",
        "options": [
            "The first shell holds a greater number of electrons, so each "
                "one of them is correspondingly harder to pull out of it",
            "The first-shell electron carries a larger negative charge than "
                "one in the outer shell",
            "The first-shell electron is closer to the positive nucleus and "
                "so is held by a stronger attraction",
            "The outer shell is full, so its own electrons leave of their "
                "own accord",
        ],
        "correct_index": 2,
        "why": "Electrostatic attraction is stronger at shorter range, so an "
               "inner electron is more tightly bound to the nucleus than an "
               "outer one.",
    },
    {
        "id": "ks4-structure-of-atom-h16",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element in group 6 of the periodic table is in the third "
                "period. Determine its electron arrangement and the number "
                "of protons in its nucleus.",
        "options": [
            "2, 8, 6 and 16 protons",
            "2, 6, 8 and 16 protons",
            "2, 8, 8, 6 and 24 protons",
            "2, 8, 6 and 6 protons, one proton for each outer electron",
        ],
        "correct_index": 0,
        "why": "Three occupied shells with 6 outer electrons gives 2, 8, 6, "
               "a total of 16 electrons, and a neutral atom has 16 protons "
               "to match.",
    },
    {
        "id": "ks4-structure-of-atom-h17",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how many electrons an oxygen atom with 8 electrons "
                "must gain to fill its outer shell with how many a "
                "magnesium atom with 12 electrons must lose to empty its "
                "own.",
        "options": [
            "Oxygen gains 6 and magnesium loses 2",
            "Oxygen gains 2 and magnesium loses 8",
            "Oxygen gains 6 and magnesium loses 10",
            "Oxygen gains 2 and magnesium loses 2",
        ],
        "correct_index": 3,
        "why": "Oxygen is 2, 6 so it needs 2 more to reach 8, and magnesium "
               "is 2, 8, 2 so losing 2 empties its outer shell.",
    },
    {
        "id": "ks4-structure-of-atom-h18",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has a radius of 1.0 × 10⁻¹⁰ m. Determine roughly "
                "how many of these atoms placed side by side would stretch "
                "across 1.0 mm.",
        "options": [
            "1.0 × 10⁷, taking each atom as one radius wide",
            "5.0 × 10⁶, taking each atom as two radii wide",
            "5.0 × 10⁹, working in metres rather than millimetres",
            "2.0 × 10⁻¹³, dividing the atom by the millimetre",
        ],
        "correct_index": 1,
        "why": "Each atom is 2.0 × 10⁻¹⁰ m across, and 1.0 × 10⁻³ m divided "
               "by 2.0 × 10⁻¹⁰ m is 5.0 × 10⁶.",
    },
    {
        "id": "ks4-structure-of-atom-h19",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number of protons, rather than the total "
                "number of particles in the nucleus, is used to order the "
                "elements in the periodic table.",
        "options": [
            "Because the proton is the only nuclear particle that can be "
                "counted accurately",
            "Because protons are heavier than neutrons and so dominate any "
                "total taken over the nucleus",
            "Because the proton number is fixed for an element while the "
                "number of neutrons can differ between its atoms",
            "Because the total number of nuclear particles comes out the "
                "same for every element",
        ],
        "correct_index": 2,
        "why": "Every atom of an element has the same proton number, whereas "
               "its atoms can hold different numbers of neutrons, so only "
               "the proton number identifies the element uniquely.",
    },
    {
        "id": "ks4-structure-of-atom-h20",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an atom whose outer shell is already full takes "
                "part in very few chemical reactions.",
        "options": [
            "Its electrons are held so tightly by the nucleus that not one "
                "of them is able to move anywhere at all",
            "It has no tendency to gain, lose or share outer electrons, and "
                "that is what bonding requires",
            "Its nucleus is screened by the complete shell, so no other "
                "nucleus is able to come near it",
            "It has no outer shell left for another atom's electrons to "
                "reach into",
        ],
        "correct_index": 1,
        "why": "Bonding happens when outer electrons are transferred or "
               "shared, and an atom with a full outer shell has no reason "
               "to do either.",
    },
    {
        "id": "ks4-structure-of-atom-h21",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A particle contains 8 protons, 8 neutrons and 10 electrons. "
                "Determine its overall charge.",
        "options": [
            "2+",
            "2−",
            "Neutral",
            "10−",
        ],
        "correct_index": 1,
        "why": "Ten charges of −1 against eight of +1 leaves a net charge of "
               "2−, since neutrons are uncharged.",
    },
    {
        "id": "ks4-structure-of-atom-h22",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the charge on the nucleus of an atom is always "
                "positive, whichever element it belongs to.",
        "options": [
            "Every element has more protons in its nucleus than neutrons, "
                "so the positive charges outweigh the rest",
            "The only charged particles it contains are protons, and every "
                "proton is +1",
            "The electrons outside it leave a positive charge behind them "
                "as they travel around the nucleus",
            "Neutrons carry a small positive charge of their own that adds "
                "to the charge carried by the protons",
        ],
        "correct_index": 1,
        "why": "A nucleus holds only protons at +1 and neutrons at 0, so its "
               "total charge can never be anything but positive.",
    },
    {
        "id": "ks4-structure-of-atom-h23",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A textbook diagram draws an atom with its nucleus filling a "
                "fifth of the width of the page. Evaluate how well that "
                "diagram represents a real atom.",
        "options": [
            "It is accurate, because a nucleus really does fill a large part "
                "of the space inside an atom",
            "It is misleading on scale — a true nucleus would be about "
                "1/10 000 of the width and far too small to see",
            "It is misleading because the nucleus belongs outside the "
                "electron shells",
            "It is accurate for the heavy elements and misleading only for "
                "the lightest",
        ],
        "correct_index": 1,
        "why": "A nuclear radius of about 1/10 000 of the atomic radius "
               "could not be drawn to scale on a page at all, so such "
               "diagrams exaggerate it enormously.",
    },
    {
        "id": "ks4-structure-of-atom-h24",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the overall charge of an atom stays the same "
                "when one of its electrons moves from one shell to another.",
        "options": [
            "The electron gives up its charge for as long as it is in "
                "flight between the two shells it is moving between",
            "No electron has been gained or lost, so the counts of positive "
                "and negative charge are unaltered",
            "The nucleus adjusts its own charge to match the new position "
                "the electron has taken up",
            "The charge does change briefly, returning once the electron "
                "has settled again",
        ],
        "correct_index": 1,
        "why": "Overall charge depends on how many protons and electrons "
               "there are, not on which shell an electron happens to "
               "occupy.",
    },
    {
        "id": "ks4-structure-of-atom-h25",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two neutral atoms occupy the same number of electron "
                "shells but hold different numbers of outer-shell "
                "electrons. Predict where each sits in the periodic table.",
        "options": [
            "In the same group but different periods, because the group is "
                "set by the shell count",
            "In the same group and the same period, since the shell count "
                "fixes both of those",
            "In neither the same group nor the same period, since no two "
                "elements share either",
            "In the same period but different groups, because the period is "
                "set by the shell count",
        ],
        "correct_index": 3,
        "why": "The number of occupied shells gives the period and the "
               "number of outer electrons gives the group, so equal shells "
               "with unequal outer electrons means one period and two "
               "groups.",
    },
    {
        "id": "ks4-structure-of-atom-h26",
        "subtopic_slug": "structure-of-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Electron mass is negligible, so "
                "the electrons of an atom make no difference to it.'",
        "options": [
            "Unsound — electrons contribute almost no mass but they set the "
                "atom's charge and decide its chemical behaviour",
            "Sound — an atom behaves the same with or without them",
            "Unsound for mass but sound for charge, since an electron is "
                "too light to carry a full charge",
            "Sound — electrons matter only once a bond has formed",
        ],
        "correct_index": 0,
        "why": "Electron mass really is negligible, but each electron still "
               "carries a full −1 charge and the outer ones govern every "
               "reaction the atom takes part in.",
    },
]
