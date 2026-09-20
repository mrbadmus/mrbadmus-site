"""Chemistry · Atomic structure and the periodic table — Group 0 · the MRB-338
expansion.

Fifty-two rows on the noble gases. The weight falls on the one explanation the
group exists to teach — a full outer shell leaves nothing to lose, gain or
share — and on the trends that follow from atom size rather than from
chemistry: boiling point and density both climb down the group while
reactivity stays where it is. Several rows work with real boiling-point and
composition data so that a pupil interpolates, extrapolates and calculates
rather than only recalling.

⚠️ Reactivity is framed as "under normal conditions" throughout, which is the
honest GCSE statement: the heavier noble gases do form a few compounds under
extreme laboratory conditions, so no option here claims total inertness in all
circumstances.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-group-0-e05",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour of the noble gases at room temperature.",
        "options": [
            "They are colourless",
            "They are pale yellow",
            "They are yellow-green",
            "They are red-brown",
        ],
        "correct_index": 0,
        "why": "All of the noble gases are colourless gases at room "
               "temperature; the colours in a neon sign come from the "
               "electric discharge.",
    },
    {
        "id": "ks4-group-0-e06",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the noble gas with the lowest boiling point of all.",
        "options": [
            "Radon",
            "Helium",
            "Argon",
            "Xenon",
        ],
        "correct_index": 1,
        "why": "Boiling point climbs down Group 0, so the gas at the top of "
               "the group boils lowest.",
    },
    {
        "id": "ks4-group-0-e07",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the feature of a noble gas atom that puts it in Group "
                "0.",
        "options": [
            "It has no outer shell",
            "It has one electron more than the element before it",
            "Its outer shell is full",
            "Its nucleus holds more neutrons than protons",
        ],
        "correct_index": 2,
        "why": "Group 0 is the full-outer-shell group, which is the source of "
               "every property the group has.",
    },
    {
        "id": "ks4-group-0-e08",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the noble gas used in bright red advertising signs.",
        "options": [
            "Helium",
            "Argon",
            "Radon",
            "Neon",
        ],
        "correct_index": 3,
        "why": "Neon glows red-orange when a current is passed through it, "
               "which is why the signs carry its name.",
    },
    {
        "id": "ks4-group-0-e09",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The noble gases are listed from helium at the top to radon "
                "at the bottom. State what happens to their boiling points.",
        "options": [
            "They fall steadily from helium to radon",
            "They rise steadily from helium to radon",
            "They rise and then fall again halfway down",
            "They stay the same all the way down",
        ],
        "correct_index": 1,
        "why": "Bigger atoms with more electrons attract one another more "
               "strongly, so more energy is needed to separate them.",
    },
    {
        "id": "ks4-group-0-e10",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the noble gas that makes up about 1% of the air.",
        "options": [
            "Helium",
            "Neon",
            "Argon",
            "Xenon",
        ],
        "correct_index": 2,
        "why": "Argon is the third most common gas in dry air, after "
               "nitrogen and oxygen.",
    },
    {
        "id": "ks4-group-0-e11",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a noble gas atom does not form an ion.",
        "options": [
            "It is too large for an electron to be pulled away from it",
            "It has no electrons at all in its outermost shell, so it has "
            "nothing it could give away",
            "It is a gas, and a gas cannot carry an electrical charge",
            "It already has a full outer shell, so it has no reason to lose "
            "or gain an electron",
        ],
        "correct_index": 3,
        "why": "Ions form when an atom moves electrons to reach a full shell; "
               "a noble gas is there already.",
    },
    {
        "id": "ks4-group-0-e12",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the noble gas that is radioactive and can collect in "
                "the basements of buildings.",
        "options": [
            "Radon",
            "Krypton",
            "Neon",
            "Helium",
        ],
        "correct_index": 0,
        "why": "Radon seeps from certain rocks and is the heaviest of the "
               "noble gases a pupil meets.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-group-0-s05",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Helium sits above neon in Group 0, and neon boils at -246 "
                "degrees C. Deduce whether helium's boiling point is higher "
                "or lower than that.",
        "options": [
            "Higher, because a smaller atom attracts its neighbours more "
            "strongly than a larger one does",
            "Lower, because helium's atoms are smaller and hold fewer "
            "electrons, so they attract one another weakly",
            "The same, because every noble gas boils at the same temperature "
            "as the others",
            "Higher, because helium is the lightest gas and a light gas is "
            "the hardest of all to condense",
        ],
        "correct_index": 1,
        "why": "The trend runs the other way up the group: helium boils "
               "lowest of all, at about -269 degrees C.",
    },
    {
        "id": "ks4-group-0-s06",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why every noble gas is a gas at room temperature.",
        "options": [
            "The forces between separate noble gas atoms are very weak, so "
            "little energy is needed to keep them apart",
            "Noble gas atoms repel one another strongly, which drives them "
            "apart and keeps the substance a gas",
            "Noble gas atoms are so light that gravity cannot hold them "
            "together into a liquid at any temperature",
            "Noble gases have no bonds inside them, so there is nothing "
            "holding any part of the substance together",
        ],
        "correct_index": 0,
        "why": "There are no bonds between the atoms at all, only weak "
               "attractions, and room temperature is enough to overcome them.",
    },
    {
        "id": "ks4-group-0-s07",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During welding a stream of argon is played over the hot "
                "joint. Suggest the reason.",
        "options": [
            "It cools the joint quickly so that the weld sets before it can "
            "run out of shape",
            "It reacts with the metal and forms a hard protective coating "
            "over the finished weld",
            "It is unreactive and keeps oxygen away from the hot metal",
            "It carries the current from the rod to the metal",
        ],
        "correct_index": 2,
        "why": "Hot metal would otherwise oxidise rapidly in air; a blanket "
               "of an unreactive gas prevents it.",
    },
    {
        "id": "ks4-group-0-s08",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the noble gases form no compounds under normal "
                "conditions.",
        "options": [
            "Their atoms are far too small for another atom to reach and bond "
            "to them",
            "Their atoms carry a charge that pushes every other atom away "
            "before it can get close",
            "Their atoms are far too heavy to move quickly enough for any "
            "collision between them to lead on to a reaction",
            "Their outer shells are full, so there is nothing to be gained by "
            "losing, gaining or sharing an electron",
        ],
        "correct_index": 3,
        "why": "Bonding is a route to a full outer shell, and these atoms "
               "have no route left to take.",
    },
    {
        "id": "ks4-group-0-s09",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Xenon boils at -108 degrees C and radon at -62 degrees C. "
                "Deduce which has the stronger forces between its atoms.",
        "options": [
            "Radon, because a higher boiling point means more energy is "
            "needed to separate the atoms",
            "Xenon, because it boils at the lower of the two temperatures",
            "Neither, since both are noble gases and every noble gas is alike "
            "in this respect",
            "Xenon, because a lower boiling point shows that its atoms are "
            "held together more tightly",
        ],
        "correct_index": 0,
        "why": "Boiling point is a direct measure of how much energy it takes "
               "to pull the particles apart.",
    },
    {
        "id": "ks4-group-0-s10",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a neon atom with a fluorine atom in terms of outer "
                "electrons and reactivity.",
        "options": [
            "Neon has 7 outer electrons and fluorine 8, so fluorine is the "
            "less reactive of the two",
            "Both have 8 outer electrons, so both of them are unreactive",
            "Neon has 8 outer electrons and is unreactive; fluorine has 7 and "
            "is very reactive",
            "Both have 7 outer electrons, and each is as reactive as the "
            "other",
        ],
        "correct_index": 2,
        "why": "One electron is the whole difference: fluorine is one short "
               "of a full shell and neon has reached it.",
    },
    {
        "id": "ks4-group-0-s11",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a full outer shell is described as a stable "
                "electron arrangement.",
        "options": [
            "The electrons in a full shell stop moving, and a particle that "
            "is not moving cannot take part in anything",
            "The atom has no tendency to change it, so it takes no part in a "
            "reaction",
            "A full shell locks the nucleus in place",
            "A full shell weighs more than a part-filled one, and the extra "
            "weight holds the atom steady",
        ],
        "correct_index": 1,
        "why": "Stable here means unchanging in a chemical sense: there is "
               "nothing the atom can gain by rearranging.",
    },
    {
        "id": "ks4-group-0-s12",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Air is about 1% argon by volume. Calculate the volume of "
                "argon in 500 cm3 of air.",
        "options": [
            "5 cm3",
            "50 cm3",
            "1 cm3",
            "0.5 cm3",
        ],
        "correct_index": 0,
        "why": "1% of 500 cm3 is 500 ÷ 100 = 5 cm3.",
    },
    {
        "id": "ks4-group-0-s13",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a noble gas rather than nitrogen is used to "
                "protect some very hot metals.",
        "options": [
            "Nitrogen is denser than any noble gas, so it sinks away from the "
            "hot surface instead of covering it",
            "Nitrogen dissolves in hot metal and makes the finished piece "
            "brittle once it has cooled again",
            "Nitrogen will react with certain hot metals, forming a nitride, "
            "while a noble gas will not",
            "Nitrogen burns in air, so a stream of it near a hot metal would "
            "catch light straight away",
        ],
        "correct_index": 2,
        "why": "Magnesium, for instance, burns in nitrogen to give magnesium "
               "nitride, so nitrogen is not inert enough for every job.",
    },
    {
        "id": "ks4-group-0-s14",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the size of the atoms going down "
                "Group 0.",
        "options": [
            "They get smaller, because the growing nuclear charge pulls the "
            "shells inwards as you go down",
            "They stay the same, because every noble gas has a full outer "
            "shell whatever its position",
            "They get smaller and then larger again below argon",
            "They get larger, because each element down the group has another "
            "occupied shell",
        ],
        "correct_index": 3,
        "why": "One more shell each step down means a larger atom, which is "
               "the same trend as in every other group.",
    },
    {
        "id": "ks4-group-0-s15",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the boiling point of a noble gas rises going "
                "down the group.",
        "options": [
            "The atoms become more reactive down the group, and a reactive "
            "substance is harder to boil away",
            "The atoms become heavier down the group, and a heavy particle "
            "cannot be lifted out of a liquid",
            "The atoms hold more electrons down the group, so the attraction "
            "between neighbouring atoms is stronger",
            "The atoms begin to bond to one another down the group, and those "
            "bonds must be broken before boiling",
        ],
        "correct_index": 2,
        "why": "More electrons make a larger temporary attraction between "
               "atoms, so more energy is needed to separate them.",
    },
    {
        "id": "ks4-group-0-s16",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which noble gas has atoms containing 18 electrons.",
        "options": [
            "Neon",
            "Argon",
            "Krypton",
            "Helium",
        ],
        "correct_index": 1,
        "why": "Argon's atomic number is 18, so a neutral argon atom has 18 "
               "electrons, arranged 2.8.8.",
    },
    {
        "id": "ks4-group-0-s17",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical balloons are filled to the same volume, one "
                "with helium and one with argon. Predict which is the heavier.",
        "options": [
            "The argon balloon, because argon is the denser of the two gases",
            "The helium balloon, because helium is the denser of the two",
            "They weigh the same, because both balloons hold the same volume "
            "of gas as one another",
            "It cannot be said, because the density of a gas depends on how "
            "reactive the gas is",
        ],
        "correct_index": 0,
        "why": "Density climbs down Group 0 and argon sits well below helium, "
               "so the same volume weighs a good deal more.",
    },
    {
        "id": "ks4-group-0-s18",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why argon is sealed into the gap in a double-glazed "
                "window.",
        "options": [
            "It reacts slowly with the glass and seals up any small cracks "
            "that appear in it over the passing years",
            "It is unreactive and transfers heat poorly, so it insulates "
            "without attacking the frame or the glass",
            "It is denser than air and presses the two panes apart, which "
            "keeps the window rigid",
            "It absorbs the light that passes through the window and stops "
            "the room overheating in summer",
        ],
        "correct_index": 1,
        "why": "An unreactive gas can be sealed in for the life of the unit, "
               "and it conducts heat less well than air does.",
    },
    {
        "id": "ks4-group-0-s19",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a mixture of helium and argon does not react "
                "even when it is heated strongly.",
        "options": [
            "Heating a mixture of gases can never bring about a reaction "
            "between them",
            "The two are both gases, and two gases cannot react with one "
            "another",
            "Both have full outer shells, so neither has electrons to trade "
            "with the other",
            "Helium is too light to collide hard enough with an argon atom "
            "for a reaction to begin",
        ],
        "correct_index": 2,
        "why": "A reaction needs electrons to move or be shared, and neither "
               "atom has any reason to do either.",
    },
    {
        "id": "ks4-group-0-s20",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State two properties shared by every noble gas and one "
                "property that changes down the group.",
        "options": [
            "Shared: coloured and reactive. Changes: the outer electrons",
            "Shared: solid and dense. Changes: the reactivity of the element "
            "as the group is descended",
            "Shared: monatomic and unreactive. Changes: the reactivity of the "
            "element down the group",
            "Shared: colourless and unreactive. Changes: the boiling point",
        ],
        "correct_index": 3,
        "why": "Chemistry stays constant down Group 0; only the physical "
               "properties that depend on atom size shift.",
    },
    {
        "id": "ks4-group-0-s21",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict which of krypton and xenon is the denser gas at room "
                "temperature.",
        "options": [
            "Krypton, because its atoms are smaller",
            "Xenon, because its atoms have the greater mass of the two",
            "They have the same density, because both are noble gases and "
            "every noble gas behaves alike",
            "Krypton, because a lighter atom moves faster and so fills a "
            "container more completely",
        ],
        "correct_index": 1,
        "why": "Density climbs down Group 0, and xenon lies below krypton.",
    },
    {
        "id": "ks4-group-0-s22",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine reacts with almost every metal. Explain why it does "
                "not react with neon.",
        "options": [
            "Neon is a gas, and a gas cannot react with another gas",
            "Neon atoms are heavier than chlorine atoms and cannot be moved "
            "by them",
            "Neon has a full outer shell, so it has no electron to give and "
            "no space to receive one",
            "Neon is found only in tiny amounts, so there is never enough of "
            "it present to react",
        ],
        "correct_index": 2,
        "why": "Chlorine reacts by taking an electron, and neon has none "
               "loose enough to take.",
    },
    {
        "id": "ks4-group-0-s23",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Krypton has atomic number 36 and xenon 54. Determine how "
                "many more electrons a xenon atom holds.",
        "options": [
            "90",
            "36",
            "8",
            "18",
        ],
        "correct_index": 3,
        "why": "54 − 36 = 18, since a neutral atom has as many electrons as "
               "protons.",
    },
    {
        "id": "ks4-group-0-s24",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the noble gases were once known as the inert "
                "gases.",
        "options": [
            "Because they were thought to take no part in chemical reactions",
            "Because they were thought to be present in every mineral that "
            "had been analysed at the time",
            "Because they were the last group to be named",
            "Because they were thought to be mixtures rather than elements "
            "when they were first collected",
        ],
        "correct_index": 0,
        "why": "Inert means taking no part; the name was softened once a few "
               "compounds of the heavier members were made.",
    },
    {
        "id": "ks4-group-0-s25",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Neon boils at -246 degrees C and oxygen at -183 degrees C. "
                "Suggest why neon's is the lower of the two.",
        "options": [
            "Neon exists as single atoms with very few electrons, so the "
            "attraction between its particles is weaker",
            "Neon is the more reactive of the two, and a reactive substance "
            "boils at a lower temperature",
            "Neon is a compound while oxygen is an element, and compounds "
            "boil below the elements they contain",
            "Neon is the heavier of the two, and a heavy particle leaves a "
            "liquid more readily than a light one",
        ],
        "correct_index": 0,
        "why": "An oxygen molecule is two atoms with more electrons between "
               "them, so the forces holding the liquid together are stronger.",
    },
    {
        "id": "ks4-group-0-s26",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the noble gases are set out in a group of their "
                "own rather than spread through the table.",
        "options": [
            "Because they were discovered together and are kept together for "
            "that historical reason",
            "Because they share a full outer shell and therefore share their "
            "chemical behaviour",
            "Because they are the only gases in the table and the gases are "
            "gathered in one place",
            "Because their relative atomic masses fall close together and a "
            "group collects elements of similar mass",
        ],
        "correct_index": 1,
        "why": "A group is defined by outer electrons, and every noble gas "
               "has a complete set.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-group-0-h05",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Helium boils at -269 degrees C and argon at -186 degrees C. "
                "Estimate the boiling point of neon, which lies between them.",
        "options": [
            "-300 degrees C",
            "-120 degrees C",
            "-246 degrees C",
            "-186 degrees C",
        ],
        "correct_index": 2,
        "why": "Neon must lie between the two, and its measured value is "
               "-246 degrees C.",
    },
    {
        "id": "ks4-group-0-h06",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of electrons, why the attraction between "
                "noble gas atoms strengthens down the group.",
        "options": [
            "Each atom gains an outer electron down the group, and the extra "
            "electron forms a weak bond to the atom alongside it",
            "Each atom holds more electrons down the group, so the temporary "
            "uneven spread of charge across it is larger",
            "Each atom loses an outer electron down the group, leaving a "
            "positive charge that attracts its neighbours",
            "Each atom has more protons down the group, and a proton in one "
            "atom attracts a proton in the next",
        ],
        "correct_index": 1,
        "why": "A bigger electron cloud produces a bigger momentary dipole, "
               "and so a stronger attraction between neighbouring atoms.",
    },
    {
        "id": "ks4-group-0-h07",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon and calcium have almost the same relative atomic mass, "
                "yet argon is a gas and calcium a solid. Explain why.",
        "options": [
            "Calcium's atoms are bonded to one another throughout a giant "
            "structure; argon's separate atoms barely attract at all",
            "Calcium's atoms are much heavier than argon's, although the two "
            "relative atomic masses happen to be printed the same",
            "Argon's atoms repel one another while calcium's attract, and "
            "repulsion is what keeps a substance gaseous",
            "Calcium is a compound and argon an element, and a compound is "
            "the more likely of the two to be a solid",
        ],
        "correct_index": 0,
        "why": "State of matter follows from bonding, not from mass: "
               "metallic bonding holds calcium together and argon has none.",
    },
    {
        "id": "ks4-group-0-h08",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a noble gas takes no part in "
                "chemistry whatsoever.",
        "options": [
            "Sound — no compound of a noble gas has been made by any chemist "
            "working anywhere",
            "Sound, because a full outer shell rules out the formation of a "
            "compound by any route",
            "Too strong — under extreme laboratory conditions a few compounds "
            "of the heavier members have been made",
            "Unsound — the noble gases react as readily as the halogens once "
            "they are warmed a little",
        ],
        "correct_index": 2,
        "why": "At GCSE they are treated as unreactive under normal "
               "conditions, which is a claim about ordinary conditions rather "
               "than about every possible one.",
    },
    {
        "id": "ks4-group-0-h09",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Air is 0.93% argon by volume. Calculate the volume of argon "
                "in 2000 litres of air.",
        "options": [
            "9.3 litres",
            "186 litres",
            "0.93 litres",
            "18.6 litres",
        ],
        "correct_index": 3,
        "why": "0.93 ÷ 100 × 2000 = 18.6 litres.",
    },
    {
        "id": "ks4-group-0-h10",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Beryllium and helium both have two outer electrons, yet only "
                "one of them is a noble gas. Explain why.",
        "options": [
            "Helium's two electrons fill its only shell, while beryllium's "
            "second shell has room for six more",
            "Beryllium has two outer electrons in a shell that holds two, so "
            "it is the one that ought to be in Group 0",
            "Helium is a gas and beryllium a solid, and Group 0 contains only "
            "the elements that are gases",
            "Beryllium's two electrons are in the first shell and helium's "
            "are in the second, which is the full one",
        ],
        "correct_index": 0,
        "why": "A full shell, not a count of two, is what matters — and the "
               "first shell is full at two while the second is not.",
    },
    {
        "id": "ks4-group-0-h11",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A colourless gas will not burn, will not support burning, "
                "and gives no reaction with anything it is tested against. "
                "Deduce its group.",
        "options": [
            "Group 1",
            "Group 7",
            "Group 0",
            "Group 6",
        ],
        "correct_index": 2,
        "why": "Colourless and showing no reaction at all is the signature of "
               "a noble gas.",
    },
    {
        "id": "ks4-group-0-h12",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radon has a relative atomic mass of 222 and helium of 4. "
                "Calculate how many times denser radon gas is than helium at "
                "the same temperature and pressure.",
        "options": [
            "55.5",
            "218",
            "226",
            "5.55",
        ],
        "correct_index": 0,
        "why": "Equal volumes hold equal numbers of atoms, so the density "
               "ratio is the mass ratio: 222 ÷ 4 = 55.5.",
    },
    {
        "id": "ks4-group-0-h13",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why argon is pumped into the space above a molten "
                "reactive metal during its production.",
        "options": [
            "To cool the surface of the metal so that it sets before it can "
            "be poured out of the vessel",
            "To dissolve into the metal and improve the strength of the "
            "finished product once it has set",
            "To keep air away, since the metal would otherwise react with the "
            "oxygen and the nitrogen in it",
            "To raise the pressure above the metal so that it boils at a "
            "lower temperature than it would",
        ],
        "correct_index": 2,
        "why": "A blanket of an unreactive gas excludes both reactive "
               "components of air at once.",
    },
    {
        "id": "ks4-group-0-h14",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a balloon filled with a noble gas "
                "lifts better the further down Group 0 the gas comes from.",
        "options": [
            "Sound — the atoms get larger down the group, and a larger atom "
            "takes up more room and so lifts a good deal more",
            "Unsound — density climbs down the group, so the lower gases lift "
            "less and the heaviest would not lift at all",
            "Sound — every noble gas is lighter than air, and the effect "
            "grows stronger down the group",
            "Unsound — lift depends on how unreactive a gas is rather than on "
            "its density at all",
        ],
        "correct_index": 1,
        "why": "Only helium is much less dense than air; argon and below are "
               "denser than air and would sink.",
    },
    {
        "id": "ks4-group-0-h15",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why helium is the one noble gas whose full outer "
                "shell holds two electrons rather than eight.",
        "options": [
            "Because helium is the lightest element and a light element needs "
            "fewer electrons to be stable",
            "Because helium's two electrons are shared with a neighbouring "
            "atom, which completes the shell between them",
            "Because helium lost six of its electrons long ago and has never "
            "regained any of them since",
            "Because its only occupied shell is the first, and the first "
            "shell is full once it holds two",
        ],
        "correct_index": 3,
        "why": "Full means full for that particular shell, and the first "
               "shell's capacity is two.",
    },
    {
        "id": "ks4-group-0-h16",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon boils at -186 degrees C and xenon at -108 degrees C. "
                "Calculate the difference between the two boiling points.",
        "options": [
            "294 degrees C",
            "78 degrees C",
            "88 degrees C",
            "108 degrees C",
        ],
        "correct_index": 1,
        "why": "-108 − (-186) = 78, so xenon boils 78 degrees C higher than "
               "argon.",
    },
    {
        "id": "ks4-group-0-h17",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what holds an oxygen molecule together with what "
                "holds two neon atoms near one another in liquid neon.",
        "options": [
            "Oxygen is held by a strong covalent bond; neon atoms are held "
            "only by a weak attraction between separate atoms",
            "Both are held by covalent bonds, but the oxygen bond is the "
            "stronger of the two by a small margin",
            "Oxygen is held together by an ionic bond, while two neon atoms "
            "are held to one another by a covalent bond of the usual kind",
            "Neon is held by a strong covalent bond while oxygen molecules "
            "merely drift close to one another",
        ],
        "correct_index": 0,
        "why": "Neon forms no bonds at all; the liquid holds together on "
               "weak attractions that vanish at -246 degrees C.",
    },
    {
        "id": "ks4-group-0-h18",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict whether a sealed tube of argon conducts electricity "
                "in the way a copper wire does, and explain.",
        "options": [
            "Yes, because an argon atom's eight outer electrons are free to "
            "move through the gas",
            "Yes, because a gas offers less resistance to a current than a "
            "solid metal does",
            "No, because argon has no delocalised electrons and no ions to "
            "carry a charge through it",
            "No, because argon is the denser of the two and a dense material "
            "blocks a current",
        ],
        "correct_index": 2,
        "why": "Every electron in an argon atom is held in a full shell, so "
               "nothing charged is free to move.",
    },
    {
        "id": "ks4-group-0-h19",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element's atoms hold one electron more than a neon atom. "
                "Deduce its electron arrangement and predict its reactivity.",
        "options": [
            "2.8.1, and very reactive",
            "2.9, and unreactive",
            "2.8.1, and unreactive",
            "2.7, and very reactive",
        ],
        "correct_index": 0,
        "why": "Eleven electrons give 2.8.1 — sodium — and a single outer "
               "electron is lost easily, making it very reactive.",
    },
    {
        "id": "ks4-group-0-h20",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon has 18 electrons and potassium 19, yet argon is "
                "unreactive and potassium violently reactive. Explain why one "
                "electron makes so much difference.",
        "options": [
            "The extra electron adds mass, and a heavier atom collides harder "
            "and so reacts more readily than a lighter one",
            "Argon's 18 electrons complete its third shell, while "
            "potassium's nineteenth sits alone in a new shell and is lost "
            "easily",
            "The extra electron gives potassium an electrical charge, and a "
            "charged particle reacts far faster than a neutral one",
            "Argon's electrons are held in the nucleus while potassium's are "
            "outside it, which is what allows a reaction",
        ],
        "correct_index": 1,
        "why": "2.8.8 is a full set; 2.8.8.1 is a full set plus one loosely "
               "held electron, and that one electron is the chemistry.",
    },
    {
        "id": "ks4-group-0-h21",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of neon, argon and krypton has the largest "
                "atoms.",
        "options": [
            "Neon, because the atoms at the top of a group have the most "
            "room to spread out into",
            "Argon, because it sits in the middle of the three and takes an "
            "average of the other two sizes",
            "Krypton, because it has the most occupied electron shells of the "
            "three",
            "All three are the same size, because each of them has a full "
            "outer shell",
        ],
        "correct_index": 2,
        "why": "Neon has two shells, argon three and krypton four, and each "
               "extra shell makes the atom bigger.",
    },
    {
        "id": "ks4-group-0-h22",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the noble gases are found in the air as free "
                "elements rather than locked up in compounds.",
        "options": [
            "Because any compound they once formed has since been broken "
            "down by sunlight in the upper atmosphere",
            "Because they are lighter than the other gases and float clear "
            "of the compounds forming below them",
            "Because their compounds are all gases too, and a gaseous "
            "compound cannot be told apart from an element",
            "Because they have full outer shells and so have never combined "
            "with anything under ordinary conditions",
        ],
        "correct_index": 3,
        "why": "An element that does not react is left as itself, which is "
               "why argon can simply be separated from liquid air.",
    },
    {
        "id": "ks4-group-0-h23",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Helium has two electrons and lithium three, yet helium is "
                "unreactive and lithium very reactive. Explain the "
                "difference.",
        "options": [
            "Helium's two electrons fill its first shell; lithium's third "
            "electron starts a new shell and is lost easily",
            "Helium's two electrons are shared with another helium atom, "
            "which is what leaves the element unreactive",
            "Lithium is a metal and helium a gas, and the state of an element "
            "is what decides how reactive it is",
            "Lithium's three electrons are all in the first shell, which "
            "makes that shell unstable and the element reactive",
        ],
        "correct_index": 0,
        "why": "One electron past a full shell is a loose electron, and a "
               "loose electron is what a reaction uses.",
    },
    {
        "id": "ks4-group-0-h24",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the boiling point and the reactivity of a new noble "
                "gas made below radon in Group 0.",
        "options": [
            "A lower boiling point than radon, and a good deal more reactive "
            "than radon itself is",
            "A higher boiling point than radon, and still unreactive under "
            "ordinary conditions",
            "The same boiling point as radon, and the same reactivity too",
            "A higher boiling point than radon, and reactive enough to burn "
            "in air",
        ],
        "correct_index": 1,
        "why": "The physical trend continues down the group while the full "
               "outer shell, and so the chemistry, does not change.",
    },
    {
        "id": "ks4-group-0-h25",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate which property of argon matters more for its use as "
                "a welding shield: its density or its lack of reactivity.",
        "options": [
            "Its density, because a dense gas cools the weld faster than a "
            "light one would manage to",
            "Its lack of reactivity, because the point is to keep the hot "
            "metal from reacting, though being denser than air helps it stay "
            "put",
            "Its density, because the whole purpose of the shield is to press "
            "down on the molten metal",
            "Neither, because the argon is there to carry the current from "
            "the rod to the workpiece",
        ],
        "correct_index": 1,
        "why": "Unreactivity is the reason a shield works at all; the density "
               "is a useful second property, not the main one.",
    },
    {
        "id": "ks4-group-0-h26",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the reason helium is used in a party balloon with "
                "the reason argon is used in a light bulb.",
        "options": [
            "Both uses depend on the gas being denser than air and staying "
            "where it is put",
            "Both uses depend on the gas glowing when a current is passed "
            "through it",
            "The helium use depends on its reactivity and the argon use on "
            "its density",
            "The helium use depends chiefly on its low density and the argon "
            "use on its unreactivity, though both gases are unreactive",
        ],
        "correct_index": 3,
        "why": "One use needs lift, the other needs a gas that will not "
               "attack a white-hot filament.",
    },
]
