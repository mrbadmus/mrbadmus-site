"""Chemistry · Atomic structure and the periodic table — metals and non-metals ·
the MRB-338 expansion.

Fifty-two rows on the two families and the structures behind them. The weight
falls on the properties a pupil is asked to explain rather than merely list —
conduction and malleability from delocalised electrons and sliding layers, low
melting points from small molecules, and above all the oxides, which is where
the classification does real chemical work: a metal oxide is a base, a
non-metal oxide dissolves to an acid, and either can be used to identify an
unknown element.

The exception set is here on purpose: graphite conducts, mercury is liquid,
bromine is liquid, silicon sits on the line. The reactivity series belongs to
`chemical-changes` and the transition metals to their own leaf.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-metals-non-metals-e05",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sulfur burns in air. State whether the oxide produced is "
                "acidic, basic or neutral.",
        "options": [
            "An acidic oxide",
            "A basic oxide",
            "A neutral oxide",
            "An alkaline oxide",
        ],
        "correct_index": 0,
        "why": "Non-metal oxides such as CO2 and SO2 dissolve in water to give "
               "acidic solutions.",
    },
    {
        "id": "ks4-metals-non-metals-e06",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a metal conducts heat well.",
        "options": [
            "Its ions vibrate so slowly that energy passes between them "
            "without being held up on the way",
            "Its delocalised electrons move through the structure and carry "
            "energy with them",
            "Its atoms are packed loosely, leaving gaps through which the "
            "energy can travel unhindered",
            "Its surface is shiny, and a shiny surface takes in heat faster",
        ],
        "correct_index": 1,
        "why": "The same free electrons that carry an electric current also "
               "transfer energy quickly through the metal.",
    },
    {
        "id": "ks4-metals-non-metals-e07",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by describing a metal as malleable.",
        "options": [
            "It melts at a low temperature",
            "It dissolves readily in water",
            "It can be hammered into a sheet without shattering",
            "It reacts quickly with the oxygen and water vapour in the air",
        ],
        "correct_index": 2,
        "why": "Malleable means it can be beaten or rolled into a new shape "
               "rather than breaking apart.",
    },
    {
        "id": "ks4-metals-non-metals-e08",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name an element that is a non-metal and a gas at room "
                "temperature.",
        "options": [
            "Calcium",
            "Zinc",
            "Lead",
            "Nitrogen",
        ],
        "correct_index": 3,
        "why": "Nitrogen is a non-metal and exists as N2 gas; the other three "
               "are metals and are solid at room temperature.",
    },
    {
        "id": "ks4-metals-non-metals-e09",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A non-metal oxide dissolves in water. State the pH range of "
                "the solution formed.",
        "options": [
            "Above 7",
            "Below 7",
            "Exactly 7",
            "Above 14",
        ],
        "correct_index": 1,
        "why": "A non-metal oxide gives an acidic solution, so the pH falls "
               "below 7.",
    },
    {
        "id": "ks4-metals-non-metals-e10",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether metals or non-metals generally have the higher "
                "melting points.",
        "options": [
            "Non-metals",
            "The two are much the same",
            "Metals",
            "It depends on the sample",
        ],
        "correct_index": 2,
        "why": "Strong metallic bonding throughout a metal's structure has to "
               "be overcome, which takes a great deal of energy.",
    },
    {
        "id": "ks4-metals-non-metals-e11",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two products formed when a metal reacts with a "
                "dilute acid.",
        "options": [
            "A salt and water",
            "A salt and hydrogen",
            "An oxide and water",
            "A salt and oxygen",
        ],
        "correct_index": 1,
        "why": "Metal + acid gives a salt and hydrogen, which is why the "
               "mixture fizzes.",
    },
    {
        "id": "ks4-metals-non-metals-e12",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the metalloid used to make the chips inside a computer.",
        "options": [
            "Silicon",
            "Sodium",
            "Sulfur",
            "Silver",
        ],
        "correct_index": 0,
        "why": "Silicon is a semiconductor: it conducts, but not as freely as "
               "a metal, which is what a chip needs.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-metals-non-metals-s05",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why copper conducts electricity but solid sulfur "
                "does not.",
        "options": [
            "Copper has delocalised electrons free to move through it; "
            "sulfur's electrons are all held within its molecules",
            "Copper is the denser of the two, and a dense material carries a "
            "current more readily than a light one does",
            "Copper melts at the higher temperature, and a high melting point "
            "is what allows a current to pass",
            "Copper is a compound and sulfur is an element, and a compound "
            "conducts electricity where an element does not",
        ],
        "correct_index": 0,
        "why": "Conduction needs charged particles free to move, and only the "
               "metal has them.",
    },
    {
        "id": "ks4-metals-non-metals-s06",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon dioxide dissolves in rain water. Deduce the effect "
                "this has on the pH of the water.",
        "options": [
            "The pH rises above 7",
            "The pH falls below 7",
            "The pH stays at exactly 7",
            "The pH falls to 0",
        ],
        "correct_index": 1,
        "why": "Carbon dioxide is a non-metal oxide, so the solution it forms "
               "is acidic — this is why rain is slightly acidic naturally.",
    },
    {
        "id": "ks4-metals-non-metals-s07",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a strip of aluminium bends when it is struck "
                "while a lump of sulfur shatters.",
        "options": [
            "Aluminium is held together by weak forces that give way easily "
            "under a blow and then re-form afterwards",
            "Aluminium contains water between its particles, and the water "
            "lets the shape change without any damage",
            "Aluminium's layers of ions slide over one another while the "
            "electrons hold the structure together",
            "Aluminium melts for an instant where the hammer lands, and the "
            "liquid then sets in the new shape",
        ],
        "correct_index": 2,
        "why": "Sulfur is separate molecules with nothing to hold a new shape "
               "together, so the solid simply breaks apart.",
    },
    {
        "id": "ks4-metals-non-metals-s08",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium ribbon is dropped into dilute hydrochloric acid. "
                "Describe what is seen and name the gas produced.",
        "options": [
            "A white precipitate forms slowly, and the gas is oxygen",
            "The metal turns black without fizzing, and the gas is chlorine",
            "The acid turns blue and no gas is given off at any point",
            "The ribbon fizzes and disappears, and the gas is hydrogen",
        ],
        "correct_index": 3,
        "why": "Metal + acid gives a salt and hydrogen, so the fizzing is "
               "hydrogen leaving the solution.",
    },
    {
        "id": "ks4-metals-non-metals-s09",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why most metals have to be heated to a very high "
                "temperature before they melt.",
        "options": [
            "Strong attraction between the positive ions and the delocalised "
            "electrons runs right through the structure",
            "Metal atoms are heavier than other atoms, and a heavy atom takes "
            "longer to warm through to its centre",
            "Metals conduct heat away so quickly that the temperature at the "
            "surface cannot build up to the melting point",
            "Metal atoms are packed so tightly that there is no room left for "
            "any of them to move",
        ],
        "correct_index": 0,
        "why": "Melting means breaking that attraction throughout the giant "
               "structure, which takes a great deal of energy.",
    },
    {
        "id": "ks4-metals-non-metals-s10",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element burns in oxygen and its oxide dissolves in water "
                "to give a solution of pH 3. Deduce the type of element.",
        "options": [
            "A metal",
            "A non-metal",
            "A metalloid",
            "It cannot be decided from this",
        ],
        "correct_index": 1,
        "why": "An acidic oxide is the mark of a non-metal; a metal oxide "
               "would have given a pH above 7.",
    },
    {
        "id": "ks4-metals-non-metals-s11",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper oxide is warmed with dilute sulfuric acid until the "
                "acid has been used up. Name the two products formed.",
        "options": [
            "A salt and hydrogen",
            "An alkali and hydrogen",
            "A salt and water",
            "A salt and carbon dioxide",
        ],
        "correct_index": 2,
        "why": "A metal oxide is a base, and base + acid gives a salt and "
               "water with no gas at all.",
    },
    {
        "id": "ks4-metals-non-metals-s12",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sulfur melts at about 115 degrees C even though each of its "
                "molecules contains eight atoms. Explain why.",
        "options": [
            "The bonds inside each molecule are extremely weak and give way "
            "as soon as the solid is warmed",
            "Sulfur is a yellow solid, and a coloured solid takes in energy "
            "from a flame more readily than a white one",
            "Eight atoms is too few for a molecule to hold together at any "
            "temperature much above room temperature",
            "Melting only separates the molecules from one another, and the "
            "forces between molecules are weak",
        ],
        "correct_index": 3,
        "why": "Melting never breaks the covalent bonds inside a molecule, "
               "only the weak attractions holding molecules together.",
    },
    {
        "id": "ks4-metals-non-metals-s13",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a non-metal element would be a poor choice for "
                "the core of an electrical cable.",
        "options": [
            "It has no free charged particles, so almost no current passes "
            "through it",
            "It would react with the plastic used to insulate the cable and "
            "destroy the covering",
            "It is denser than a metal, so a cable made of it would be far "
            "too heavy to hang",
            "It conducts so well that the cable would overheat and would have "
            "to be cooled",
        ],
        "correct_index": 0,
        "why": "Conduction needs delocalised electrons, and a non-metal's "
               "electrons stay within its molecules.",
    },
    {
        "id": "ks4-metals-non-metals-s14",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the ions formed by metals differ from those "
                "formed by non-metals.",
        "options": [
            "Metal ions are negative and formed by gaining electrons; "
            "non-metal ions are positive and formed by losing them",
            "Metal ions are positive and formed by losing electrons; "
            "non-metal ions are negative and formed by gaining them",
            "Both are positive, but a metal ion carries the larger charge of "
            "the two in any compound they form together",
            "Both are negative, although a non-metal ion is formed rather "
            "more readily than a metal ion is",
        ],
        "correct_index": 1,
        "why": "A metal has few outer electrons to shed; a non-metal is a few "
               "short of a full shell and takes them in.",
    },
    {
        "id": "ks4-metals-non-metals-s15",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why many non-metals are gases at room temperature "
                "while nearly every metal is a solid.",
        "options": [
            "Non-metal atoms are lighter, and a light atom is found as a gas "
            "at ordinary temperatures",
            "Non-metals have no bonds between their atoms, so nothing holds "
            "a non-metal together in any state",
            "Non-metals exist as small molecules with weak forces between "
            "them; a metal is one giant bonded structure",
            "Non-metals are found on the right of the table, and the elements "
            "on that side are warmed more easily",
        ],
        "correct_index": 2,
        "why": "Weak attractions between separate molecules are overcome at "
               "room temperature; metallic bonding is not.",
    },
    {
        "id": "ks4-metals-non-metals-s16",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of bonding found in a metal and state what "
                "holds the structure together.",
        "options": [
            "Covalent bonding, held together by pairs of electrons shared "
            "between neighbouring atoms",
            "Ionic bonding, held together by the attraction between positive "
            "ions and negative ions",
            "Hydrogen bonding, held together by the attraction between one "
            "molecule and the next along",
            "Metallic bonding, held together by attraction between positive "
            "ions and delocalised electrons",
        ],
        "correct_index": 3,
        "why": "The lattice of positive ions sits in a sea of electrons that "
               "belong to no single atom.",
    },
    {
        "id": "ks4-metals-non-metals-s17",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas produced when a metal reacts with a dilute acid "
                "and describe the test for it.",
        "options": [
            "Hydrogen, which gives a squeaky pop with a lighted splint",
            "Oxygen, which relights a splint that has been blown out",
            "Carbon dioxide, which turns limewater milky when bubbled in",
            "Chlorine, which bleaches damp litmus paper placed in the mouth "
            "of the tube",
        ],
        "correct_index": 0,
        "why": "Metal + acid always gives hydrogen, and the squeaky pop is "
               "the standard school test for it.",
    },
    {
        "id": "ks4-metals-non-metals-s18",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the densities of a typical metal and a typical "
                "non-metal, and suggest why this matters when choosing a "
                "building material.",
        "options": [
            "The non-metal is denser, so it is the better choice wherever a "
            "structure has to carry a heavy load above it",
            "The metal is denser, so a beam made of it is heavy but strong "
            "enough to carry a load",
            "The two are much alike in density, so cost decides the choice",
            "The metal is less dense, which is what makes it the better "
            "choice for the frame of a tall building",
        ],
        "correct_index": 1,
        "why": "Metals are generally dense and strong, and the weight is "
               "accepted for the strength it brings.",
    },
    {
        "id": "ks4-metals-non-metals-s19",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One end of a copper bar is heated. State what the "
                "delocalised electrons do.",
        "options": [
            "They stop moving, and the energy is passed along by the ions "
            "instead",
            "They leave the metal at the hot end, which is why the bar loses "
            "mass as it is heated",
            "They gain energy and carry it through the bar to the cooler end",
            "They collect at the cold end and stay there until the bar has "
            "cooled down again",
        ],
        "correct_index": 2,
        "why": "Free electrons move quickly and take energy with them, which "
               "is why a metal conducts heat so well.",
    },
    {
        "id": "ks4-metals-non-metals-s20",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a metal oxide is described as a base.",
        "options": [
            "Because it dissolves in water to give a solution of pH 7",
            "Because it releases hydrogen gas when it is added to water",
            "Because it is formed at the base of a flame when a metal burns",
            "Because it neutralises an acid, giving a salt and water",
        ],
        "correct_index": 3,
        "why": "A base is a substance that neutralises an acid, and that is "
               "exactly what a metal oxide does.",
    },
    {
        "id": "ks4-metals-non-metals-s21",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Phosphorus is a non-metal. Predict how a solid lump of it "
                "behaves when it is struck with a hammer and when a current "
                "is passed through it.",
        "options": [
            "It shatters, and almost no current passes through it",
            "It flattens into a sheet, and a current passes through it easily",
            "It shatters, and a current passes through it easily",
            "It flattens into a sheet, and almost no current passes through "
            "it",
        ],
        "correct_index": 0,
        "why": "A non-metal solid is brittle and has no delocalised electrons "
               "to carry a current.",
    },
    {
        "id": "ks4-metals-non-metals-s22",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why aluminium rather than lead is chosen for "
                "overhead power cables.",
        "options": [
            "Lead melts at the higher temperature of the two, so a lead cable "
            "could not be joined once it had been hung in place",
            "Aluminium conducts well and has a low density, so the cable is "
            "light enough to hang between pylons",
            "Aluminium is a non-metal, and a non-metal carries a current with "
            "far less waste than a metal does",
            "Lead is the better conductor but is far scarcer, so aluminium is "
            "used in its place as a substitute",
        ],
        "correct_index": 1,
        "why": "A cable has to carry its own weight over a long span, so a "
               "light good conductor wins over a heavy one.",
    },
    {
        "id": "ks4-metals-non-metals-s23",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium oxide melts at about 2850 degrees C and carbon "
                "dioxide is a gas at room temperature. Explain the "
                "difference.",
        "options": [
            "Magnesium oxide contains more atoms in each of its particles, "
            "and a larger particle is harder to separate from its neighbours",
            "Carbon dioxide has no bonds of any kind inside it, so there is "
            "nothing for the heating to overcome",
            "Magnesium oxide is a giant structure of strongly attracted ions; "
            "carbon dioxide is separate molecules with weak forces between "
            "them",
            "Carbon dioxide was made in a laboratory while magnesium oxide "
            "occurs naturally, and natural materials melt higher",
        ],
        "correct_index": 2,
        "why": "The metal oxide's lattice must be broken apart; the non-metal "
               "oxide's molecules only have to drift away from one another.",
    },
    {
        "id": "ks4-metals-non-metals-s24",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element is a dull solid that shatters when struck and "
                "does not conduct electricity. Deduce what it is.",
        "options": [
            "A metal",
            "A metalloid",
            "A tarnished metal",
            "A non-metal",
        ],
        "correct_index": 3,
        "why": "Dullness, brittleness and no conduction are the three "
               "standard non-metal properties together.",
    },
    {
        "id": "ks4-metals-non-metals-s25",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a non-metal element would make a poor knife "
                "blade.",
        "options": [
            "It is brittle, so the edge would chip or the blade snap in use",
            "It would conduct heat away and cool the food as it was cut",
            "It would dissolve in the water used to wash the blade after it "
            "had been used",
            "It is far too dense, so the finished knife would be much too "
            "heavy to hold",
        ],
        "correct_index": 0,
        "why": "A blade has to take a shock without breaking, and a brittle "
               "solid cannot.",
    },
    {
        "id": "ks4-metals-non-metals-s26",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sorting the elements into metals and non-metals "
                "is useful even though a few elements fit neither group.",
        "options": [
            "Because the elements that fit neither group are so rare that no "
            "chemist ever has to work with any of them in practice",
            "Because the sorting predicts the behaviour of the great majority, "
            "and the few in between are named as metalloids",
            "Because every element can be forced into one of the two groups "
            "once its melting point has been measured",
            "Because chemists use the sorting for the metals and simply "
            "ignore it whenever a non-metal is involved",
        ],
        "correct_index": 1,
        "why": "A classification earns its place by how much it predicts, and "
               "this one predicts oxide behaviour, conduction and ion charge.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-metals-non-metals-h05",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Element J is a dull solid that does not conduct, and its "
                "oxide dissolves to give pH 2. Deduce where in the periodic "
                "table J is found.",
        "options": [
            "On the far left, among the Group 1 metals",
            "In the central block, among the transition metals",
            "Towards the top right, among the non-metals",
            "At the foot of the table, below the main body of it",
        ],
        "correct_index": 2,
        "why": "No conduction and an acidic oxide are both non-metal "
               "properties, and the non-metals occupy the top right.",
    },
    {
        "id": "ks4-metals-non-metals-h06",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium and sulfur are each burned in oxygen and the "
                "product shaken with water. Compare the two solutions.",
        "options": [
            "Both solutions come out alkaline, because burning in oxygen "
            "produces a base",
            "The magnesium product gives an acid and the sulfur product gives "
            "an alkali",
            "Both solutions come out acidic, because an oxide of any element "
            "dissolves to give an acid",
            "The magnesium product gives an alkaline solution and the sulfur "
            "product an acidic one",
        ],
        "correct_index": 3,
        "why": "Magnesium oxide is basic and sulfur dioxide acidic, which is "
               "the standard metal / non-metal contrast.",
    },
    {
        "id": "ks4-metals-non-metals-h07",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the pH of the solution formed when each of magnesium "
                "oxide and carbon dioxide is shaken with water.",
        "options": [
            "Magnesium oxide above 7, carbon dioxide below 7",
            "Magnesium oxide below 7, carbon dioxide above 7",
            "Both above 7, since an oxide is a base whichever element it "
            "comes from",
            "Both below 7, since an oxide contains oxygen and oxygen is "
            "acidic",
        ],
        "correct_index": 0,
        "why": "A metal oxide gives an alkaline solution and a non-metal "
               "oxide an acidic one.",
    },
    {
        "id": "ks4-metals-non-metals-h08",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that an element which conducts "
                "electricity and is brittle has to be a metal.",
        "options": [
            "Sound — conduction is the property that settles it, and "
            "brittleness has no bearing on the classification",
            "Unsound — silicon conducts to a degree and is brittle, and it is "
            "a metalloid rather than a metal",
            "Sound — every brittle element turns out to be a metal once it "
            "has been tested properly",
            "Unsound — a metal cannot conduct and be brittle at the same "
            "time, so no such element exists",
        ],
        "correct_index": 1,
        "why": "The two properties pull in opposite directions, which is "
               "exactly what marks out an element on the dividing line.",
    },
    {
        "id": "ks4-metals-non-metals-h09",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a metal oxide is basic while a non-metal oxide "
                "is acidic.",
        "options": [
            "The metal oxide contains more oxygen per atom than the non-metal "
            "oxide does, and oxygen is what makes a base",
            "A metal oxide is the heavier of the two, and a heavy compound "
            "settles out before it can turn acidic",
            "A metal oxide gives hydroxide ions in water, while a non-metal "
            "oxide gives hydrogen ions",
            "A metal oxide dissolves and a non-metal oxide does not",
        ],
        "correct_index": 2,
        "why": "pH is set by which ion the oxide releases: OH- makes the "
               "solution alkaline, H+ makes it acidic.",
    },
    {
        "id": "ks4-metals-non-metals-h10",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium is added to dilute sulfuric acid. Write the word "
                "equation for the reaction.",
        "options": [
            "magnesium + sulfuric acid -> magnesium oxide + water",
            "magnesium + sulfuric acid -> magnesium sulfide + water",
            "magnesium + sulfuric acid -> magnesium hydroxide + oxygen",
            "magnesium + sulfuric acid -> magnesium sulfate + hydrogen",
        ],
        "correct_index": 3,
        "why": "Metal + acid gives a salt and hydrogen, and sulfuric acid's "
               "salt is a sulfate.",
    },
    {
        "id": "ks4-metals-non-metals-h11",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how energy travels through a copper rod with how it "
                "travels through a block of sulfur.",
        "options": [
            "Copper carries it quickly by moving electrons; sulfur relies on "
            "slow vibration passed from particle to particle",
            "Both carry it by moving electrons, but copper's electrons move "
            "considerably faster than sulfur's do",
            "Copper carries it by vibration alone, while sulfur's molecules "
            "move bodily through the block and take it with them",
            "Neither carries it, because energy travels through a liquid or a "
            "gas but not through a solid",
        ],
        "correct_index": 0,
        "why": "Delocalised electrons are free to travel the length of the "
               "metal; sulfur has no such mechanism.",
    },
    {
        "id": "ks4-metals-non-metals-h12",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which of sodium, sulfur and silicon would be the best "
                "material for a semiconductor, and explain.",
        "options": [
            "Sodium, because a metal conducts better than anything else and a "
            "semiconductor needs the best conductor there is",
            "Silicon, because a metalloid conducts a little without "
            "conducting freely, which is what a semiconductor must do",
            "Sulfur, because a non-metal blocks a current and a semiconductor "
            "is a material that blocks one",
            "Any of the three, because the word semiconductor describes how a "
            "material is used and not what it is made from",
        ],
        "correct_index": 1,
        "why": "A semiconductor sits between a conductor and an insulator, "
               "which is what puts silicon on the dividing line.",
    },
    {
        "id": "ks4-metals-non-metals-h13",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that every metal oxide dissolves in water "
                "to give an alkaline solution.",
        "options": [
            "Sound — a metal oxide is a base, and a base dissolves to give an "
            "alkaline solution",
            "Sound, provided the water is warmed first so that the oxide has "
            "a chance to dissolve properly",
            "Unsound — many metal oxides, such as copper oxide, hardly "
            "dissolve, though they still neutralise an acid",
            "Unsound — a metal oxide dissolves to give an acidic solution "
            "rather than an alkaline one",
        ],
        "correct_index": 2,
        "why": "Being a base and being soluble are different things; an "
               "alkali is the special case of a base that dissolves.",
    },
    {
        "id": "ks4-metals-non-metals-h14",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An unknown element melts at 1538 degrees C, conducts "
                "electricity and can be drawn into a wire. Deduce whether it "
                "is a metal, a non-metal or a metalloid.",
        "options": [
            "A non-metal",
            "A metalloid",
            "It cannot be decided until the oxide has been tested",
            "A metal",
        ],
        "correct_index": 3,
        "why": "A high melting point, conduction and ductility are three "
               "metal properties together, with no conflict between them.",
    },
    {
        "id": "ks4-metals-non-metals-h15",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens when sulfur dioxide is bubbled into "
                "sodium hydroxide solution, and explain.",
        "options": [
            "A reaction occurs, because an acidic oxide is neutralised by an "
            "alkali",
            "Nothing happens, because two non-metal compounds cannot react "
            "with one another",
            "Hydrogen is given off, because the gas displaces it from the "
            "solution as it passes through",
            "The solution turns more strongly alkaline, as an oxide is a base",
        ],
        "correct_index": 0,
        "why": "Sulfur dioxide is a non-metal oxide and so behaves as an "
               "acid, which sodium hydroxide neutralises.",
    },
    {
        "id": "ks4-metals-non-metals-h16",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why graphite is chosen for the electrodes used in "
                "electrolysis even though it is a non-metal.",
        "options": [
            "Because a non-metal takes no part in a reaction, and an "
            "electrode must be completely unreactive in every cell",
            "It conducts and has a very high melting point, so it survives a "
            "hot molten mixture",
            "Because it is the cheapest material available",
            "Because it dissolves slowly in the molten mixture and so keeps "
            "the electrolyte topped up as the cell runs",
        ],
        "correct_index": 1,
        "why": "Graphite's delocalised electrons carry the current and its "
               "giant covalent structure withstands the temperature.",
    },
    {
        "id": "ks4-metals-non-metals-h17",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a copper wire's ability to "
                "carry a current if its delocalised electrons were fixed in "
                "place.",
        "options": [
            "It would carry a current more efficiently, because fixed "
            "electrons cannot be scattered on the way through",
            "The current would be unchanged, because the positive ions would "
            "take over the job of moving the charge",
            "It would stop conducting, because a current is those electrons "
            "moving",
            "It would carry a current only while it was heated",
        ],
        "correct_index": 2,
        "why": "An electric current in a metal IS the flow of the "
               "delocalised electrons; stop them and nothing flows.",
    },
    {
        "id": "ks4-metals-non-metals-h18",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'A brittle material can never be "
                "used in a building.'",
        "options": [
            "Sound — a brittle material shatters under load, so it has no "
            "place in a structure of any kind",
            "Sound, unless the material is also a good conductor, in which "
            "case the brittleness stops mattering",
            "Unsound — a brittle material such as glass or brick is used "
            "where it is pressed rather than bent",
            "Unsound — brittleness and strength are the same property, so a "
            "brittle material is the strongest available",
        ],
        "correct_index": 2,
        "why": "Brittle materials fail under a bending or shock load, but "
               "stand up well to being squashed.",
    },
    {
        "id": "ks4-metals-non-metals-h19",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of the oxides MgO, CO2, SO2 and Na2O would "
                "neutralise hydrochloric acid.",
        "options": [
            "MgO and Na2O",
            "CO2 and SO2",
            "All four of them",
            "MgO and CO2",
        ],
        "correct_index": 0,
        "why": "MgO and Na2O are metal oxides and therefore bases; CO2 and "
               "SO2 are non-metal oxides and are acidic themselves.",
    },
    {
        "id": "ks4-metals-non-metals-h20",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why testing whether an element conducts electricity "
                "is a more reliable check for a metal than looking at how "
                "shiny it is.",
        "options": [
            "Because judging shininess needs an instrument that most school "
            "laboratories do not have available to them",
            "Because a metal tarnishes and looks dull, while conduction "
            "depends on the structure and does not change",
            "Because a non-metal element cannot be polished, so the shine "
            "test gives no reading for one",
            "Because conduction is the quicker of the two tests to set up, "
            "and a quick test is the more reliable one",
        ],
        "correct_index": 1,
        "why": "A freshly cut metal is shiny but a tarnished one is not, so "
               "appearance can mislead where conduction does not.",
    },
    {
        "id": "ks4-metals-non-metals-h21",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a metal, a metalloid and a non-metal in terms of how "
                "well each carries an electric current.",
        "options": [
            "The metalloid carries it best, then the metal, then the "
            "non-metal, which carries almost none of it",
            "All three carry it equally, because every element contains "
            "electrons of one kind or another",
            "The metal carries it best, the metalloid carries some, and the "
            "non-metal carries almost none",
            "The non-metal carries it best, because its electrons are held "
            "within molecules where a current can reach them",
        ],
        "correct_index": 2,
        "why": "The metalloids sit between the two families in conductivity, "
               "which is what makes them semiconductors.",
    },
    {
        "id": "ks4-metals-non-metals-h22",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why metallic and non-metallic behaviour is better "
                "described as a gradual change than as a sharp dividing line.",
        "options": [
            "Because chemists have not agreed on where the dividing line "
            "between the two families ought to be drawn",
            "Because an element's behaviour changes from one day to the next "
            "depending on how it has been stored",
            "Because the dividing line moves whenever a new element is added "
            "to the bottom of the periodic table",
            "Because elements near the divide share properties with both "
            "families, conducting a little and being brittle",
        ],
        "correct_index": 3,
        "why": "Silicon and germanium have one foot in each camp, which is "
               "why the metalloid category exists at all.",
    },
    {
        "id": "ks4-metals-non-metals-h23",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc is added to dilute sulfuric acid. Name the salt formed "
                "and state the change in mass of the zinc.",
        "options": [
            "Zinc sulfate, and the zinc loses mass as it dissolves",
            "Zinc sulfide, and the zinc gains mass as the acid coats it",
            "Zinc oxide, and the mass of the zinc does not change",
            "Zinc chloride, and the zinc loses mass as it dissolves",
        ],
        "correct_index": 0,
        "why": "Sulfuric acid gives sulfates, and the metal passes into "
               "solution as zinc ions, so the solid shrinks.",
    },
    {
        "id": "ks4-metals-non-metals-h24",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate which single property — conduction, appearance or "
                "brittleness — is the best test of whether an element is a "
                "metal.",
        "options": [
            "Appearance, because a metal is shiny and a non-metal is dull "
            "whenever the two are compared side by side",
            "Conduction, because it follows directly from the delocalised "
            "electrons that define a metal's structure",
            "Brittleness, because a metal bends and a non-metal shatters, "
            "which is the clearest difference to see",
            "None of the three, because a single property cannot be used to "
            "place an element in a family",
        ],
        "correct_index": 1,
        "why": "The other two have exceptions a pupil meets at GCSE — a "
               "tarnished metal, a brittle metalloid — while conduction "
               "tracks the structure itself.",
    },
    {
        "id": "ks4-metals-non-metals-h25",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compound contains oxygen and its solution turns red "
                "litmus blue. Deduce the type of element bonded to the "
                "oxygen.",
        "options": [
            "A non-metal",
            "A noble gas",
            "A metal",
            "It cannot be decided from this",
        ],
        "correct_index": 2,
        "why": "Red litmus turning blue means alkaline, and only a metal "
               "oxide gives an alkaline solution.",
    },
    {
        "id": "ks4-metals-non-metals-h26",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the structure of a metal with that of a typical "
                "non-metal element, and link each structure to one property.",
        "options": [
            "Both are giant structures, but the metal's is held by shared "
            "pairs of electrons and so melts at the higher temperature",
            "Both are made of separate molecules, and the metal's are the "
            "larger, which is what makes it the better conductor",
            "The metal is separate molecules, so it conducts; the non-metal "
            "is a giant structure, so it is brittle",
            "The metal is a giant lattice with free electrons, so it "
            "conducts; the non-metal is small molecules, so it melts low",
        ],
        "correct_index": 3,
        "why": "Each property traces back to the structure: free electrons "
               "give conduction, weak forces between molecules give a low "
               "melting point.",
    },
]
