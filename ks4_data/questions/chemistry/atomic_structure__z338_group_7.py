"""Chemistry · Atomic structure and the periodic table — Group 7 · the MRB-338
expansion.

Fifty-two rows on the halogens. The weight falls on displacement — which pairs
react, which do not, what is seen, and why the order F > Cl > Br > I follows
from how strongly a nucleus can pull in one extra electron — and on the fact
that the physical trend and the chemical trend run in opposite directions down
the group. Several rows carry real melting and boiling point data and two carry
mass calculations, so the group is worked with as well as recalled.

Redox language belongs to `chemical-changes` and the use of chlorine in water
treatment to `resources`; this leaf stays on the group's own chemistry.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-group-7-e05",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the state of matter of iodine at room temperature.",
        "options": [
            "Solid",
            "Liquid",
            "Gas",
            "It has no fixed state at room temperature",
        ],
        "correct_index": 0,
        "why": "Iodine is a grey-black solid at room temperature and melts at "
               "184 degrees C.",
    },
    {
        "id": "ks4-group-7-e06",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the colour of the halogens changes going down "
                "Group 7.",
        "options": [
            "It grows paler, so that the lowest of them is colourless",
            "It grows darker",
            "It stays the same",
            "It changes from dark to pale and then back to dark again",
        ],
        "correct_index": 1,
        "why": "Fluorine is pale yellow, chlorine yellow-green, bromine "
               "red-brown and iodine almost black.",
    },
    {
        "id": "ks4-group-7-e07",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of atoms in one molecule of a halogen "
                "element.",
        "options": [
            "One",
            "Three",
            "Two",
            "Seven",
        ],
        "correct_index": 2,
        "why": "The halogens are diatomic: each molecule is two atoms sharing "
               "a pair of electrons.",
    },
    {
        "id": "ks4-group-7-e08",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A halogen and a metal react together. Name the class of "
                "compound produced.",
        "options": [
            "An acid",
            "An oxide",
            "A carbonate",
            "A salt",
        ],
        "correct_index": 3,
        "why": "Halogen means salt-forming: the metal gives up electrons and "
               "the halogen takes them, giving a metal halide.",
    },
    {
        "id": "ks4-group-7-e09",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the halogen at the top of Group 7.",
        "options": [
            "Chlorine",
            "Fluorine",
            "Astatine",
            "Iodine",
        ],
        "correct_index": 1,
        "why": "Fluorine has the smallest atoms of the group and so the "
               "strongest pull on an incoming electron.",
    },
    {
        "id": "ks4-group-7-e10",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the halogen added to drinking water to kill bacteria.",
        "options": [
            "Iodine",
            "Bromine",
            "Chlorine",
            "Astatine",
        ],
        "correct_index": 2,
        "why": "Chlorine is reactive enough to kill microorganisms and can be "
               "dosed safely at very low concentration.",
    },
    {
        "id": "ks4-group-7-e11",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iodine melts far above chlorine. State the trend in melting "
                "point that this shows for Group 7.",
        "options": [
            "They fall",
            "They stay the same",
            "They fall then rise",
            "They rise",
        ],
        "correct_index": 3,
        "why": "Larger molecules attract one another more strongly, so more "
               "energy is needed to separate them.",
    },
    {
        "id": "ks4-group-7-e12",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the appearance of fluorine at room temperature.",
        "options": [
            "A pale yellow gas",
            "A grey-black solid",
            "A red-brown liquid",
            "A colourless liquid",
        ],
        "correct_index": 0,
        "why": "Fluorine is the palest and the lightest of the halogens, and "
               "it is a gas at room temperature.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-group-7-s05",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Select the balanced equation for chlorine reacting with "
                "sodium bromide solution.",
        "options": [
            "Cl2 + 2NaBr -> 2NaCl + Br2",
            "Cl2 + NaBr -> NaCl + Br2",
            "2Cl2 + 2NaBr -> 2NaCl + 2Br2",
            "Cl + 2NaBr -> NaCl2 + Br2",
        ],
        "correct_index": 0,
        "why": "One Cl2 molecule takes the place of one Br2, and two sodium "
               "ions are needed to balance either.",
    },
    {
        "id": "ks4-group-7-s06",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the name halogen means salt-forming.",
        "options": [
            "Because a halogen dissolves in water to give a solution that "
            "tastes of salt when it is tested",
            "Because a halogen reacts with a metal to give a metal halide, "
            "which is a salt",
            "Because a halogen is extracted from rock salt and takes its name "
            "from the material it comes from",
            "Because a halogen turns into common salt when left in the open air",
        ],
        "correct_index": 1,
        "why": "Sodium chloride, potassium bromide and the rest are all "
               "salts, and a halogen is the non-metal half of each.",
    },
    {
        "id": "ks4-group-7-s07",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A few drops of bromine water are shaken with sodium chloride "
                "solution. State what happens.",
        "options": [
            "The mixture turns dark brown as chlorine is set free from the "
            "salt",
            "A white precipitate settles out of the mixture within a few "
            "seconds",
            "Nothing happens, because chlorine is the more reactive of the "
            "two halogens",
            "The bromine loses its colour as it is taken into the sodium "
            "chloride",
        ],
        "correct_index": 2,
        "why": "A halogen can only push out one below it in the group, and "
               "chlorine is above bromine.",
    },
    {
        "id": "ks4-group-7-s08",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why reactivity falls going down Group 7.",
        "options": [
            "The atoms hold more electrons down the group, and the extra "
            "electrons get in the way of a reaction",
            "The atoms lose their outer electrons more readily down the "
            "group, which leaves less for them to gain",
            "The atoms become heavier down the group, and a heavy atom moves "
            "too slowly to collide usefully",
            "The outer shell lies further from the nucleus down the group, so "
            "an incoming electron is attracted less strongly",
        ],
        "correct_index": 3,
        "why": "A halogen reacts by capturing one electron, and distance plus "
               "shielding weaken the pull that captures it.",
    },
    {
        "id": "ks4-group-7-s09",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the compound formed when chlorine reacts with hydrogen "
                "and give its formula.",
        "options": [
            "Hydrogen chloride, HCl",
            "Chloric acid, HClO3",
            "Hydrogen chloride, H2Cl",
            "Chlorine hydride, ClH2",
        ],
        "correct_index": 0,
        "why": "Each atom shares one electron, so the molecule is one "
               "hydrogen joined to one chlorine.",
    },
    {
        "id": "ks4-group-7-s10",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a halogen element exists as molecules of two "
                "atoms rather than as single atoms.",
        "options": [
            "Two atoms are attracted to one another by their charges, since "
            "each halogen atom carries a 1- charge already",
            "Two atoms each share one electron, and the shared pair gives "
            "both of them a full outer shell",
            "Only two will fit into the space available inside a halogen "
            "molecule",
            "Two atoms are needed so that one can take an electron from the "
            "other and both end up stable",
        ],
        "correct_index": 1,
        "why": "Seven outer electrons each, plus one shared pair, gives each "
               "atom the eight it needs.",
    },
    {
        "id": "ks4-group-7-s11",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine boils at -101 degrees C and iodine at 184 degrees "
                "C. Deduce which has the stronger forces between its "
                "molecules.",
        "options": [
            "Chlorine, because it boils at the lower of the two temperatures "
            "and so leaves the liquid faster",
            "Neither, since both are halogens and every halogen behaves in "
            "the same way as the rest",
            "Iodine, because more energy has to be supplied before its "
            "molecules will separate",
            "Chlorine, because a gas holds its particles together more "
            "tightly than a solid does",
        ],
        "correct_index": 2,
        "why": "Boiling point measures how much energy separating the "
               "particles takes, and iodine needs far more of it.",
    },
    {
        "id": "ks4-group-7-s12",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens when chlorine water is added to "
                "potassium bromide solution, and state the colour change.",
        "options": [
            "No reaction, so the solution stays exactly as colourless as it "
            "was before the chlorine was added",
            "The solution turns milky white as potassium chloride settles out "
            "of it as a fine solid",
            "The solution turns deep violet as iodine is set free",
            "Bromine is displaced, and the solution turns orange-brown",
        ],
        "correct_index": 3,
        "why": "Chlorine is above bromine in the group, so it takes the place "
               "of bromine and the free bromine colours the solution.",
    },
    {
        "id": "ks4-group-7-s13",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the formula of the compound formed between potassium "
                "and bromine.",
        "options": [
            "KBr",
            "KBr2",
            "K2Br",
            "K2Br3",
        ],
        "correct_index": 0,
        "why": "Potassium forms K+ and bromine forms Br-, so the two combine "
               "in a one to one ratio.",
    },
    {
        "id": "ks4-group-7-s14",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why fluorine is the most reactive element in Group 7.",
        "options": [
            "Its molecules are the smallest, so they travel fastest and "
            "collide with other particles more often than any other halogen",
            "Its atoms are the smallest, so the incoming electron comes "
            "closest to the nucleus and is held most strongly",
            "Its atoms hold the fewest electrons, so there is the most room "
            "available in its outer shell for another one",
            "Its atoms have eight outer electrons rather than seven, which "
            "leaves them closest to a full shell",
        ],
        "correct_index": 1,
        "why": "Reactivity in Group 7 is about capturing an electron, and a "
               "small atom with little shielding captures one best.",
    },
    {
        "id": "ks4-group-7-s15",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State two physical properties that change going down Group 7 "
                "and one chemical property that changes.",
        "options": [
            "Physical: colour and boiling point. Chemical: reactivity",
            "Physical: colour and reactivity. Chemical: outer electrons",
            "Physical: the charge on the ion and the number of outer "
            "electrons. Chemical: the colour",
            "Physical: boiling point and the number of atoms in a molecule. "
            "Chemical: the charge on the ion",
        ],
        "correct_index": 0,
        "why": "Outer electrons, molecule size and ion charge stay fixed down "
               "the group; colour, boiling point and reactivity do not.",
    },
    {
        "id": "ks4-group-7-s16",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which of chlorine and iodine can push the other out "
                "of a solution of its salt.",
        "options": [
            "Iodine can push out chlorine",
            "Neither of them can, because a halogen cannot displace another "
            "halogen from a solution",
            "Chlorine can push out iodine",
            "Either can push out the other, depending on which of the two "
            "solutions is the more concentrated",
        ],
        "correct_index": 2,
        "why": "Chlorine is above iodine in Group 7 and so is the more "
               "reactive, which is what displacement requires.",
    },
    {
        "id": "ks4-group-7-s17",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why bromine cannot push chlorine out of sodium "
                "chloride solution.",
        "options": [
            "Because sodium chloride is a salt, and a salt cannot take part "
            "in a displacement reaction of any kind",
            "Because bromine is a liquid and chlorine a gas, and a liquid "
            "cannot displace a gas from a solution",
            "Because chlorine is above bromine in the group and holds the "
            "extra electron more strongly",
            "Because the two molecules are the same size, so neither has any "
            "advantage over the other",
        ],
        "correct_index": 2,
        "why": "Displacement runs one way only: the halogen that attracts an "
               "electron more strongly keeps it.",
    },
    {
        "id": "ks4-group-7-s18",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fluorine boils at -188 degrees C and chlorine at -101 "
                "degrees C. Predict which of these is the boiling point of "
                "bromine.",
        "options": [
            "-250 degrees C",
            "59 degrees C",
            "-140 degrees C",
            "-101 degrees C",
        ],
        "correct_index": 1,
        "why": "Boiling point climbs steadily down the group, so bromine's "
               "must lie above chlorine's — it is 59 degrees C.",
    },
    {
        "id": "ks4-group-7-s19",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a halogen atom forms an ion carrying a single "
                "negative charge.",
        "options": [
            "It loses seven electrons, and losing an electron leaves a "
            "negative charge behind",
            "It gains seven electrons, one for each of the electrons already "
            "in its outer shell",
            "It gains one electron to complete its outer shell, which leaves "
            "one extra negative charge",
            "It shares one electron with a metal, and sharing gives an ion a "
            "single negative charge",
        ],
        "correct_index": 2,
        "why": "Seven outer electrons plus one gained makes eight, and the "
               "extra electron is the extra negative charge.",
    },
    {
        "id": "ks4-group-7-s20",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why chlorine gas is handled only in a fume "
                "cupboard.",
        "options": [
            "Because it is heavier than air and would sink to the floor of "
            "the laboratory and be hard to sweep up afterwards",
            "Because it would react with the wooden bench and burn a hole "
            "straight through it",
            "Because it would dampen the walls of the room",
            "Because it is toxic, and breathing it in damages the lungs",
        ],
        "correct_index": 3,
        "why": "Every halogen is poisonous to some degree, and chlorine is "
               "the one a school is most likely to make.",
    },
    {
        "id": "ks4-group-7-s21",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour of the cyclohexane layer when bromine has "
                "been displaced into it.",
        "options": [
            "Orange",
            "Violet",
            "Colourless",
            "Pale green",
        ],
        "correct_index": 0,
        "why": "Bromine colours the non-polar layer orange; iodine colours it "
               "violet, which is how the two are told apart.",
    },
    {
        "id": "ks4-group-7-s22",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict whether astatine would push iodine out of potassium "
                "iodide solution.",
        "options": [
            "Yes, because astatine has the largest atoms and the largest "
            "atoms always win a displacement",
            "No, because astatine lies below iodine and is the less reactive "
            "of the two",
            "Yes, because astatine and iodine are both solids",
            "It cannot be predicted, since astatine is too rare for anyone to "
            "have written a rule about it",
        ],
        "correct_index": 1,
        "why": "Displacement follows the group order, and astatine is at the "
               "bottom of it.",
    },
    {
        "id": "ks4-group-7-s23",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Select the balanced equation for bromine reacting with "
                "potassium iodide solution.",
        "options": [
            "Br2 + KI -> KBr + I2",
            "2Br2 + 2KI -> 2KBr + 2I2",
            "Br2 + 2KI -> 2KBr + I2",
            "Br + 2KI -> KBr2 + I2",
        ],
        "correct_index": 2,
        "why": "Two iodide ions give up their places to the two bromine "
               "atoms, so two KI are needed for each Br2.",
    },
    {
        "id": "ks4-group-7-s24",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a more reactive halogen takes the place of a "
                "less reactive one in its salt.",
        "options": [
            "The more reactive halogen is the larger molecule, so it pushes "
            "the smaller one out of the way",
            "The more reactive halogen dissolves better, so it forces the "
            "other one out of the solution",
            "The more reactive halogen has the higher boiling point, so it "
            "stays in solution while the other leaves",
            "The more reactive halogen holds the extra electron more "
            "strongly, so it takes it from the halide ion",
        ],
        "correct_index": 3,
        "why": "The electron ends up wherever it is held most firmly, and "
               "that is the smaller, higher halogen.",
    },
    {
        "id": "ks4-group-7-s25",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the formula of the compound formed between calcium "
                "and chlorine, given calcium forms a 2+ ion.",
        "options": [
            "CaCl2",
            "CaCl",
            "Ca2Cl",
            "Ca2Cl3",
        ],
        "correct_index": 0,
        "why": "Two chloride ions at 1- each are needed to balance the 2+ "
               "charge on one calcium ion.",
    },
    {
        "id": "ks4-group-7-s26",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the appearance of chlorine and state one hazard of "
                "working with it.",
        "options": [
            "A grey-black solid that stains the skin brown",
            "A yellow-green gas that is poisonous to breathe in",
            "A red-brown liquid that boils at room temperature and gives off "
            "a flammable vapour",
            "A colourless gas that displaces the air and leaves a person "
            "short of oxygen",
        ],
        "correct_index": 1,
        "why": "Chlorine's colour is the middle of the group's range, and "
               "like every halogen it is toxic.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-group-7-h05",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of atomic structure, why a chlorine atom "
                "attracts an incoming electron more strongly than a bromine "
                "atom does.",
        "options": [
            "Chlorine has fewer occupied shells, so its outer shell lies "
            "closer to the nucleus and is less shielded",
            "Chlorine has more protons in its nucleus, which gives it the "
            "greater pull of the two on any nearby electron",
            "Chlorine is a gas and bromine a liquid, and a gas draws in a "
            "passing electron more readily than a liquid",
            "Chlorine has one more outer electron than bromine, so its shell "
            "is nearer to being complete",
        ],
        "correct_index": 0,
        "why": "Distance and shielding decide it; chlorine's third shell is "
               "nearer the nucleus than bromine's fourth.",
    },
    {
        "id": "ks4-group-7-h06",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Halogen W displaces X from its salt, and X displaces Y from "
                "its salt. Deduce the order of reactivity.",
        "options": [
            "Y, then X, then W, with Y the most reactive",
            "X, then W, then Y, with X the most reactive of the three",
            "W, then X, then Y, with W the most reactive",
            "The three are equally reactive, since each of them displaced "
            "something from a salt",
        ],
        "correct_index": 2,
        "why": "Only a more reactive halogen displaces a less reactive one, "
               "so each displacement fixes one step of the order.",
    },
    {
        "id": "ks4-group-7-h07",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A colourless solution turns brown when chlorine water is "
                "added, and a cyclohexane layer shaken with it turns violet. "
                "Deduce the salt that was in the solution.",
        "options": [
            "Potassium chloride",
            "Potassium fluoride",
            "Potassium bromide",
            "Potassium iodide",
        ],
        "correct_index": 3,
        "why": "The violet layer is free iodine, so an iodide must have been "
               "present for chlorine to displace.",
    },
    {
        "id": "ks4-group-7-h08",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a halogen atom reacts by gaining one "
                "electron.",
        "options": [
            "Sound — a halogen has seven outer electrons and gaining one is "
            "the only route to a full shell open to it",
            "Only partly — it gains one from a metal, but with a non-metal it "
            "shares a pair instead",
            "Unsound — a halogen reacts by losing its seven outer electrons "
            "to whichever atom it meets",
            "Unsound — a halogen has a full outer shell already and takes no "
            "part in a reaction",
        ],
        "correct_index": 1,
        "why": "Hydrogen chloride and a chlorine molecule are both covalent; "
               "the ion only forms when a metal is the partner.",
    },
    {
        "id": "ks4-group-7-h09",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the relative formula mass of a chlorine molecule, "
                "Cl2. (Cl = 35.5)",
        "options": [
            "35.5",
            "71",
            "17.75",
            "70",
        ],
        "correct_index": 1,
        "why": "Two chlorine atoms give 2 × 35.5 = 71.",
    },
    {
        "id": "ks4-group-7-h10",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why boiling point rises down Group 7 while "
                "reactivity falls.",
        "options": [
            "The two trends are measured at different temperatures, which is "
            "why they appear to run opposite ways",
            "Boiling point depends on the forces between whole molecules, "
            "while reactivity depends on the pull on one electron",
            "Boiling point depends on the number of outer electrons, while "
            "reactivity depends on the size of the molecule",
            "Boiling point depends on colour, and the halogens grow darker "
            "down the group as they grow less reactive",
        ],
        "correct_index": 1,
        "why": "A bigger molecule attracts its neighbours better and captures "
               "a stray electron worse; both follow from size.",
    },
    {
        "id": "ks4-group-7-h11",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce what is seen when chlorine water is added to sodium "
                "fluoride solution.",
        "options": [
            "The solution turns pale yellow as fluorine is displaced from the "
            "salt by the chlorine",
            "A white solid appears at once and settles to the bottom of the "
            "tube within a minute or so",
            "No change, because fluorine is above chlorine and holds its "
            "electron more strongly",
            "The chlorine loses its colour as it is taken up into the sodium "
            "fluoride solution",
        ],
        "correct_index": 2,
        "why": "Displacement only runs downwards in the group, and there is "
               "nothing above fluorine.",
    },
    {
        "id": "ks4-group-7-h12",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the state and the reactivity of a halogen placed "
                "below astatine in Group 7.",
        "options": [
            "A gas, and the most reactive halogen of them all",
            "A solid, and less reactive than astatine",
            "A liquid, and about as reactive as bromine is",
            "A gas, and completely unreactive in every circumstance",
        ],
        "correct_index": 1,
        "why": "Both trends continue: melting point climbs, so it is solid, "
               "and reactivity keeps falling down the group.",
    },
    {
        "id": "ks4-group-7-h13",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of electrons a halogen atom gains with "
                "the number a Group 1 atom loses.",
        "options": [
            "The halogen gains seven and the Group 1 atom loses one, which "
            "matches each of their group numbers",
            "The halogen gains one and the Group 1 atom loses seven, so seven "
            "metal atoms are needed for each halogen",
            "Each moves one electron: the halogen takes one in and the Group "
            "1 atom gives one away",
            "Each moves seven electrons, which is why a halide contains seven "
            "atoms of the metal",
        ],
        "correct_index": 2,
        "why": "One electron passes from metal to non-metal, which is why "
               "sodium chloride is NaCl and not Na7Cl.",
    },
    {
        "id": "ks4-group-7-h14",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the formula of aluminium chloride, given that "
                "aluminium forms a 3+ ion.",
        "options": [
            "AlCl",
            "Al3Cl",
            "Al2Cl3",
            "AlCl3",
        ],
        "correct_index": 3,
        "why": "Three chloride ions at 1- each balance the 3+ charge on one "
               "aluminium ion.",
    },
    {
        "id": "ks4-group-7-h15",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why chlorine is added to drinking water even though "
                "it is poisonous.",
        "options": [
            "Because the amount used is far too small to harm a person but "
            "large enough to kill microorganisms",
            "Because chlorine stops being poisonous once it has dissolved in "
            "any quantity of water",
            "Because the chlorine settles to the bottom of the reservoir and "
            "never reaches the taps at all",
            "Because chlorine is the only substance that will dissolve in "
            "water, so there is no alternative",
        ],
        "correct_index": 0,
        "why": "Dose is what decides a hazard; a few parts per million "
               "sterilises the supply without risk to the drinker.",
    },
    {
        "id": "ks4-group-7-h16",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the mass of sodium chloride formed when 7.1 g of "
                "chlorine reacts completely with sodium. (Cl = 35.5, Na = 23)",
        "options": [
            "5.85 g",
            "58.5 g",
            "11.7 g",
            "7.1 g",
        ],
        "correct_index": 2,
        "why": "7.1 ÷ 71 = 0.1 mol of Cl2 gives 0.2 mol of NaCl, and NaCl has "
               "a relative formula mass of 58.5, so 0.2 × 58.5 = 11.7 g.",
    },
    {
        "id": "ks4-group-7-h17",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why no halogen can push fluorine out of a solution "
                "of a fluoride.",
        "options": [
            "Because fluorine is a gas, and a gas cannot be displaced from a "
            "solution by anything",
            "Because a fluoride is insoluble, so there is nothing dissolved "
            "for another halogen to react with",
            "Because fluorine sits at the top of the group and holds an "
            "electron more strongly than any other halogen",
            "Because fluorine's molecules are so small that another halogen "
            "cannot reach them in solution",
        ],
        "correct_index": 2,
        "why": "Displacement needs a halogen that attracts the electron more "
               "strongly, and none does.",
    },
    {
        "id": "ks4-group-7-h18",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a chlorine atom with a chloride ion in terms of "
                "electrons and charge.",
        "options": [
            "The ion has one electron fewer and carries a 1+ charge as a "
            "result of losing it",
            "The two have the same number of electrons, and the charge comes "
            "from a change in the nucleus",
            "The ion has seven electrons fewer and carries a 7- charge, one "
            "for each outer electron",
            "The ion has one electron more and carries a 1- charge as a "
            "result of gaining it",
        ],
        "correct_index": 3,
        "why": "The nucleus is untouched; one extra electron is the whole "
               "difference, and it is the source of the charge.",
    },
    {
        "id": "ks4-group-7-h19",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which of chlorine, bromine and iodine has the "
                "highest melting point.",
        "options": [
            "Iodine",
            "Chlorine",
            "Bromine",
            "All three melt at the same temperature",
        ],
        "correct_index": 0,
        "why": "Melting point climbs down Group 7, and iodine is the lowest "
               "of the three in the group.",
    },
    {
        "id": "ks4-group-7-h20",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says bromine will displace chlorine because "
                "bromine is a liquid and chlorine a gas. Evaluate this "
                "reasoning.",
        "options": [
            "Correct — a liquid is the more concentrated of the two and "
            "therefore wins the exchange",
            "Wrong — the state of a halogen has nothing to do with it, and "
            "chlorine is the more reactive of the two",
            "Correct, provided the chlorine has first been dissolved in water "
            "to make chlorine water",
            "Wrong — bromine would displace chlorine, but the reason given "
            "for it is the wrong one",
        ],
        "correct_index": 1,
        "why": "Displacement depends on the pull on an electron, which is set "
               "by position in the group, not by state.",
    },
    {
        "id": "ks4-group-7-h21",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrogen chloride dissolves in water to give a solution of "
                "pH 1. Deduce what this shows about the compound.",
        "options": [
            "That it is an acid in solution",
            "That it is an alkali in solution",
            "That it is neutral in solution, since a gas cannot change a pH",
            "That it has broken down into hydrogen and chlorine again",
        ],
        "correct_index": 0,
        "why": "A pH well below 7 is the mark of an acid; the solution is "
               "hydrochloric acid.",
    },
    {
        "id": "ks4-group-7-h22",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'A halogen is more reactive the "
                "larger its atoms are.'",
        "options": [
            "Sound — a larger atom offers a bigger target for an incoming "
            "electron to strike",
            "Sound, because reactivity and boiling point rise together down "
            "the group as the atoms get larger",
            "Unsound — the larger atoms hold an incoming electron less "
            "strongly, so reactivity falls as size rises",
            "Unsound — every halogen is equally reactive, whatever the size "
            "of its atoms may be",
        ],
        "correct_index": 2,
        "why": "This is the Group 1 rule applied to the wrong group: gaining "
               "an electron and losing one respond to size oppositely.",
    },
    {
        "id": "ks4-group-7-h23",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the relative formula mass of potassium bromide, "
                "KBr. (K = 39, Br = 80)",
        "options": [
            "41",
            "119",
            "158",
            "80",
        ],
        "correct_index": 1,
        "why": "39 + 80 = 119.",
    },
    {
        "id": "ks4-group-7-h24",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a school uses iodine rather than fluorine in a "
                "displacement experiment.",
        "options": [
            "Because iodine is the more reactive and so gives a clearer "
            "colour change to observe",
            "Because fluorine is a solid and would be difficult to measure "
            "out accurately in a classroom",
            "Because fluorine is extremely reactive and dangerous, while "
            "iodine can be handled safely",
            "Because fluorine gives no colour change of any kind, so there "
            "would be nothing for a pupil to see",
        ],
        "correct_index": 2,
        "why": "Fluorine attacks glass and skin; iodine is a manageable solid "
               "with a striking colour.",
    },
    {
        "id": "ks4-group-7-h25",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium burns in bromine vapour. Deduce the product and "
                "its formula.",
        "options": [
            "Potassium bromate, KBrO3",
            "Potassium bromide, K2Br",
            "Potassium bromide, KBr",
            "Potassium bromide, KBr2",
        ],
        "correct_index": 2,
        "why": "K+ and Br- carry equal and opposite charges, so they combine "
               "one to one.",
    },
    {
        "id": "ks4-group-7-h26",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a halogen atom reaches a full outer shell with a "
                "metal and with another non-metal.",
        "options": [
            "With a metal it gives away an electron; with a non-metal it "
            "takes one in",
            "With both it shares a pair of electrons, and the difference "
            "between the two lies only in how many pairs",
            "With a metal it takes an electron and becomes a 1- ion; with a "
            "non-metal it shares a pair instead",
            "With both it takes an electron and becomes an ion, whichever "
            "kind of element it is reacting with",
        ],
        "correct_index": 2,
        "why": "Ionic with a metal, covalent with a non-metal — sodium "
               "chloride against hydrogen chloride.",
    },
]
