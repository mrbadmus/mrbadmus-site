"""Chemistry · Atomic structure and the periodic table — Group 1 · the MRB-338
expansion.

Fifty-two rows on the alkali metals. The weight falls on the reaction with
water — the products, the balanced equations for lithium and sodium, the
observations that separate one metal from the next, and the alkaline solution
that gives the group its name — and on the structural explanation for the
trend, which is distance and shielding rather than nuclear charge. Two rows
carry mass calculations so that the reaction is quantitative as well as
descriptive.

⚠️ No row claims a density trend down Group 1: lithium, sodium and potassium
do not run in order, so the honest statement is that the first three float and
the lower two do not.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-group-1-e05",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the group of the periodic table that holds sodium and "
                "potassium.",
        "options": [
            "Group 1",
            "Group 3",
            "Group 6",
            "Group 0",
        ],
        "correct_index": 0,
        "why": "Both have a single outer electron, which places them in the "
               "first column of the table.",
    },
    {
        "id": "ks4-group-1-e06",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom of a Group 1 element is examined. State how many "
                "electrons its outer shell holds.",
        "options": [
            "2",
            "1",
            "7",
            "8",
        ],
        "correct_index": 1,
        "why": "Group 1 elements have one outer electron, which is the "
               "electron they lose in every reaction.",
    },
    {
        "id": "ks4-group-1-e07",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what is seen when a small piece of lithium is "
                "dropped into a trough of water.",
        "options": [
            "It sinks straight to the bottom and lies there without changing "
            "in any way",
            "It burns with a bright white flame and leaves a white ash on the "
            "surface of the water",
            "It floats and fizzes gently, moving about on the surface",
            "It dissolves at once, with no bubbles and no movement of any "
            "kind",
        ],
        "correct_index": 2,
        "why": "Lithium is the least vigorous of the three commonly used "
               "alkali metals, so the fizzing is steady rather than violent.",
    },
    {
        "id": "ks4-group-1-e08",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas given off when a Group 1 metal reacts with "
                "water.",
        "options": [
            "Oxygen",
            "Carbon dioxide",
            "Chlorine",
            "Hydrogen",
        ],
        "correct_index": 3,
        "why": "The water is split, the metal takes the hydroxide part and "
               "hydrogen is released as a gas.",
    },
    {
        "id": "ks4-group-1-e09",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A piece of sodium is cut open and left on a tile. State what "
                "happens to the fresh surface.",
        "options": [
            "It stays bright and shiny for several hours together",
            "It quickly goes dull as it reacts with the air",
            "It turns black and then crumbles into a fine powder",
            "It slowly turns bright blue over a period of minutes",
        ],
        "correct_index": 1,
        "why": "The fresh metal reacts with oxygen and water vapour in the "
               "air, coating itself in a dull layer of compound.",
    },
    {
        "id": "ks4-group-1-e10",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of compound formed alongside hydrogen when a "
                "Group 1 metal reacts with water.",
        "options": [
            "A metal oxide",
            "A metal chloride",
            "A metal hydroxide",
            "A metal carbonate",
        ],
        "correct_index": 2,
        "why": "Metal + water gives a metal hydroxide and hydrogen; the "
               "hydroxide dissolves to give an alkali.",
    },
    {
        "id": "ks4-group-1-e11",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of lithium, sodium and potassium reacts most "
                "vigorously with water.",
        "options": [
            "Lithium",
            "Sodium",
            "All three react equally vigorously as each other",
            "Potassium",
        ],
        "correct_index": 3,
        "why": "Reactivity climbs down Group 1, and potassium is the lowest "
               "of the three in the group.",
    },
    {
        "id": "ks4-group-1-e12",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to the elements of Group 1.",
        "options": [
            "The alkali metals",
            "The alkaline earth metals",
            "The halogens",
            "The transition metals",
        ],
        "correct_index": 0,
        "why": "Their hydroxides dissolve in water to give alkaline "
               "solutions, which is where the name comes from.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-group-1-s05",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Select the balanced equation for lithium reacting with "
                "water.",
        "options": [
            "2Li + 2H2O -> 2LiOH + H2",
            "Li + H2O -> LiOH + H2",
            "2Li + H2O -> Li2O + H2",
            "Li + 2H2O -> Li(OH)2 + H2",
        ],
        "correct_index": 0,
        "why": "Two lithium atoms release two electrons between them, which "
               "is what one H2 molecule needs.",
    },
    {
        "id": "ks4-group-1-s06",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lithium hydroxide, sodium hydroxide and potassium hydroxide "
                "all dissolve to give solutions of high pH. Explain what this "
                "has to do with the name given to Group 1.",
        "options": [
            "Because they are extracted from alkaline rocks found near the "
            "surface of the ground",
            "Because their reaction with water leaves a hydroxide that "
            "dissolves to give an alkaline solution",
            "Because they neutralise any alkali they are placed into, "
            "leaving a completely neutral solution behind them",
            "Because their oxides dissolve in acid to give a solution with a "
            "pH above 7",
        ],
        "correct_index": 1,
        "why": "Lithium, sodium and potassium hydroxides are all strong "
               "alkalis, which is what the group name records.",
    },
    {
        "id": "ks4-group-1-s07",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a piece of sodium darts about on the surface of "
                "water.",
        "options": [
            "The water heats up and the currents it sets up carry the metal "
            "around with them",
            "The metal is attracted to the walls of the trough and moves "
            "towards whichever side is nearest",
            "The hydrogen given off streams away from one side and pushes the "
            "metal in the opposite direction",
            "The metal is lighter than water, and a floating solid drifts "
            "about on any surface it is placed on",
        ],
        "correct_index": 2,
        "why": "Gas leaving unevenly acts like a tiny jet and drives the "
               "molten ball across the surface.",
    },
    {
        "id": "ks4-group-1-s08",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a freshly cut Group 1 metal loses its shine "
                "within seconds.",
        "options": [
            "The cut surface cools quickly, and a cold metal surface looks "
            "duller than a warm one does",
            "The cut surface dries out, and the loss of moisture from it is "
            "what takes away the shine",
            "The cut surface absorbs light from the room, which is what makes "
            "it appear dull to the eye",
            "The cut surface reacts with oxygen in the air, covering itself "
            "with a layer of oxide",
        ],
        "correct_index": 3,
        "why": "The metal is reactive enough to combine with the air, and the "
               "oxide layer that forms is dull.",
    },
    {
        "id": "ks4-group-1-s09",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Select the balanced equation for sodium burning in chlorine.",
        "options": [
            "2Na + Cl2 -> 2NaCl",
            "Na + Cl2 -> NaCl2",
            "Na + Cl -> NaCl",
            "2Na + 2Cl2 -> 2NaCl2",
        ],
        "correct_index": 0,
        "why": "Chlorine is diatomic and each atom takes one electron, so two "
               "sodium atoms are needed for each Cl2 molecule.",
    },
    {
        "id": "ks4-group-1-s10",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sodium reacts more vigorously with water than "
                "lithium does.",
        "options": [
            "Sodium has more outer electrons to give away, so more of them "
            "can move at once",
            "Sodium's outer electron is further from the nucleus and more "
            "shielded, so it is lost more easily",
            "Sodium has a greater nuclear charge, and a greater charge pulls "
            "the water molecules in faster",
            "Sodium has a lower melting point, and a metal with a low melting "
            "point reacts faster than one that has not",
        ],
        "correct_index": 1,
        "why": "One more occupied shell puts the outer electron further out "
               "and behind more inner electrons.",
    },
    {
        "id": "ks4-group-1-s11",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the melting points of the Group 1 "
                "metals going down the group.",
        "options": [
            "They climb, because the atoms grow heavier as the group is "
            "descended",
            "They stay much the same, since every Group 1 metal is soft",
            "They fall",
            "They fall and then climb again below potassium",
        ],
        "correct_index": 2,
        "why": "Caesium melts at only 28 degrees C, low enough to melt in a "
               "warm hand, while lithium melts at 180 degrees C.",
    },
    {
        "id": "ks4-group-1-s12",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the compound formed when lithium is burned in oxygen.",
        "options": [
            "Lithium hydroxide",
            "Lithium chloride",
            "Lithium carbonate",
            "Lithium oxide",
        ],
        "correct_index": 3,
        "why": "A metal burning in oxygen gives its oxide; the hydroxide only "
               "appears when water is involved.",
    },
    {
        "id": "ks4-group-1-s13",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the hardness of sodium with the hardness of iron.",
        "options": [
            "Sodium is far softer and can be cut with a knife; iron cannot",
            "Sodium is far harder, which is why it has to be cut with a "
            "special blade rather than an ordinary knife",
            "The two are much alike, since both of them are metals and every "
            "metal is about as hard as the next",
            "Sodium is harder when it is cold and softer when warm, while "
            "iron stays the same at any temperature",
        ],
        "correct_index": 0,
        "why": "The alkali metals are unusually soft for metals, which is one "
               "of the ways they stand out from the rest.",
    },
    {
        "id": "ks4-group-1-s14",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why only a very small piece of a Group 1 metal is "
                "used in a classroom demonstration.",
        "options": [
            "Because a larger piece would take far too long to react for a "
            "single lesson",
            "Because the reaction is vigorous and exothermic, and a larger "
            "piece would be dangerous",
            "Because the metal is so expensive that a larger piece could not "
            "be afforded by a school",
            "Because a larger piece would sink, and the reaction happens right "
            "at the surface of the water",
        ],
        "correct_index": 1,
        "why": "The heat released can ignite the hydrogen, so the quantity is "
               "kept to a rice-grain size.",
    },
    {
        "id": "ks4-group-1-s15",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the formula of the oxide formed when sodium burns "
                "in oxygen, given that an oxide ion is O2-.",
        "options": [
            "NaO",
            "NaO2",
            "Na2O",
            "Na2O2",
        ],
        "correct_index": 2,
        "why": "Each sodium gives one electron and each oxide ion needs two, "
               "so two sodium ions balance one oxide ion.",
    },
    {
        "id": "ks4-group-1-s16",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the ion formed by a Group 1 metal has the "
                "electron arrangement of a noble gas.",
        "options": [
            "The ion gains an electron from the water it is dissolved in, "
            "which completes the outer shell",
            "The ion keeps the arrangement its atom had, and that arrangement "
            "was already a noble gas one",
            "The ion picks up a whole extra shell as it forms, and the new "
            "shell is full from the start",
            "Losing the single outer electron leaves the full shell beneath "
            "it as the new outer shell",
        ],
        "correct_index": 3,
        "why": "Sodium's 2.8.1 becomes 2.8 — neon's arrangement — once the "
               "outer electron has gone.",
    },
    {
        "id": "ks4-group-1-s17",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a piece of potassium left "
                "uncovered on a bench overnight.",
        "options": [
            "It would react with the oxygen and water vapour in the air and "
            "end up as a crust of compound",
            "It would stay exactly as it was, since air is far too dry for "
            "any reaction to take place in it",
            "It would evaporate away completely, leaving nothing behind on "
            "the surface of the bench",
            "It would set hard and become as difficult to cut as a piece of "
            "iron of the same size",
        ],
        "correct_index": 0,
        "why": "This is precisely why the metal is kept under oil: air alone "
               "is enough to destroy it.",
    },
    {
        "id": "ks4-group-1-s18",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a Group 1 metal is never dug out of the ground "
                "as the pure element.",
        "options": [
            "Because it is far too soft to survive being dug out of rock "
            "without crumbling into pieces",
            "Because it is so reactive that it has long since combined with "
            "other elements into compounds",
            "Because it is lighter than the rock around it and has floated to "
            "the surface, where it is lost",
            "Because it dissolves in the ground water and is carried away "
            "long before it can be found",
        ],
        "correct_index": 1,
        "why": "Only unreactive elements such as gold are found native; a "
               "Group 1 metal is always locked in a compound.",
    },
    {
        "id": "ks4-group-1-s19",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the vigour of the reaction with water changes "
                "from lithium through sodium to potassium.",
        "options": [
            "It weakens steadily, so that potassium barely reacts",
            "It stays exactly the same, because all three of these metals have "
            "just the one outer electron between them to lose",
            "It strengthens: gentle fizzing, then rapid movement and melting, "
            "then a reaction fast enough to ignite the gas",
            "It strengthens and then weakens, with sodium the most vigorous "
            "of the three",
        ],
        "correct_index": 2,
        "why": "The trend is a straightforward climb down the group as the "
               "outer electron becomes easier to lose.",
    },
    {
        "id": "ks4-group-1-s20",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the water left after a Group 1 metal has reacted "
                "turns red litmus blue.",
        "options": [
            "Because the hydrogen given off dissolves back into the water and "
            "makes it alkaline",
            "Because the metal itself dissolves, and a dissolved metal gives "
            "an alkaline solution",
            "Because the water has been heated, and warm water turns red "
            "litmus blue by itself",
            "Because a metal hydroxide has formed and dissolved, giving an "
            "alkaline solution",
        ],
        "correct_index": 3,
        "why": "Red litmus turning blue is the test for an alkali, and the "
               "hydroxide is a strong one.",
    },
    {
        "id": "ks4-group-1-s21",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why francium is almost never used in an experiment.",
        "options": [
            "It is extremely rare and extremely reactive, so it is difficult "
            "and dangerous to obtain and handle",
            "It is unreactive, so there would be nothing to observe if it "
            "were used in one",
            "It is a gas at room temperature, which makes it awkward to "
            "collect and awkward to weigh out accurately",
            "It is a non-metal, so it does not belong in a Group 1 experiment "
            "in the first place",
        ],
        "correct_index": 0,
        "why": "Francium sits at the foot of the group, so it is the most "
               "reactive alkali metal, and only tiny amounts exist.",
    },
    {
        "id": "ks4-group-1-s22",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three alkali metals are tested with water. A fizzes gently, "
                "B melts and darts about, and C sets its hydrogen alight. "
                "Deduce which sits highest in the group.",
        "options": [
            "C",
            "A",
            "B",
            "They must all be at the same height in the group",
        ],
        "correct_index": 1,
        "why": "The gentlest reaction belongs to the metal whose outer "
               "electron is hardest to lose, and that is the one nearest the "
               "top of the group.",
    },
    {
        "id": "ks4-group-1-s23",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrogen rather than oxygen is released when a "
                "Group 1 metal reacts with water.",
        "options": [
            "Because oxygen is the heavier of the two gases and stays "
            "dissolved in the water instead",
            "Because the metal takes the oxygen for itself, which leaves only "
            "hydrogen to escape as a gas",
            "Because the metal joins the hydroxide part of the water, leaving "
            "the hydrogen with nothing to bond to",
            "Because oxygen is given off when a metal reacts with an acid "
            "rather than with water",
        ],
        "correct_index": 2,
        "why": "The metal ion pairs with OH-, and the remaining hydrogen "
               "atoms pair up and leave as H2.",
    },
    {
        "id": "ks4-group-1-s24",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A piece of sodium forms a shiny ball as it reacts with "
                "water. Suggest why.",
        "options": [
            "The water polishes the surface of the metal as it moves across "
            "it, and that is what makes the little ball shine",
            "The sodium absorbs water and swells until it takes up a rounded "
            "shape on the surface",
            "The reaction strips the dull coating away and leaves the "
            "original shape of the piece behind",
            "The reaction gives out enough heat to melt the sodium, and a "
            "molten drop pulls itself into a ball",
        ],
        "correct_index": 3,
        "why": "Sodium melts at only 98 degrees C, and the reaction is "
               "exothermic enough to reach it.",
    },
    {
        "id": "ks4-group-1-s25",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce the formula of the chloride formed by a Group 1 metal "
                "M, given that a chloride ion is Cl-.",
        "options": [
            "MCl",
            "MCl2",
            "M2Cl",
            "MCl3",
        ],
        "correct_index": 0,
        "why": "M+ and Cl- carry equal and opposite charges, so they combine "
               "one to one.",
    },
    {
        "id": "ks4-group-1-s26",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the alkali metals are grouped together even "
                "though they react with water at very different rates.",
        "options": [
            "Because their rates are much closer together than they appear to "
            "be when the reactions are watched side by side",
            "Because each has one outer electron and so reacts in the same "
            "way, giving a hydroxide and hydrogen",
            "Because they were all discovered by the same chemist and have "
            "been listed together ever since",
            "Because their relative atomic masses rise in equal steps down "
            "the column of the table",
        ],
        "correct_index": 1,
        "why": "A group shares the kind of reaction; the rate changes down it "
               "because the outer electron sits further out.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-group-1-h05",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A Group 1 metal M burns in oxygen. Deduce the formula of the "
                "oxide, given that an oxide ion carries a 2- charge.",
        "options": [
            "MO",
            "MO2",
            "M2O",
            "M2O3",
        ],
        "correct_index": 2,
        "why": "M+ carries one positive charge, so two are needed to balance "
               "one O2- ion.",
    },
    {
        "id": "ks4-group-1-h06",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rubidium is dropped into water. Predict the products and "
                "describe what would be seen.",
        "options": [
            "Rubidium oxide and oxygen, with the metal slowly dissolving away "
            "at the surface without any fizzing",
            "Rubidium chloride and hydrogen, with a steady stream of bubbles "
            "rising for several minutes",
            "No products at all, since rubidium lies too far down the group "
            "to react with cold water",
            "Rubidium hydroxide and hydrogen, with a violent reaction and the "
            "hydrogen igniting",
        ],
        "correct_index": 3,
        "why": "Rubidium sits below potassium, so the same products appear "
               "but the reaction is fiercer still.",
    },
    {
        "id": "ks4-group-1-h07",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A Group 1 metal X reacts with water to give XOH, which has a "
                "relative formula mass of 40. Identify X. (O = 16, H = 1)",
        "options": [
            "Sodium",
            "Lithium",
            "Potassium",
            "Rubidium",
        ],
        "correct_index": 0,
        "why": "OH accounts for 17, so X has a relative atomic mass of 40 − "
               "17 = 23, which is sodium.",
    },
    {
        "id": "ks4-group-1-h08",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what happens to the outer electron of a lithium atom "
                "and of a caesium atom when each reacts.",
        "options": [
            "The lithium electron is lost more easily, because a small atom "
            "has less to hold on to",
            "Both are lost, but the caesium electron goes more easily because "
            "it lies further out and behind more shells",
            "The lithium electron is shared rather than lost, while the "
            "caesium electron is lost outright",
            "Both are gained rather than lost, since a Group 1 atom needs "
            "seven more to fill its shell",
        ],
        "correct_index": 1,
        "why": "Same event, different ease: distance and shielding weaken the "
               "hold the nucleus has on caesium's outer electron.",
    },
    {
        "id": "ks4-group-1-h09",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a Group 1 element is a typical metal.",
        "options": [
            "Sound — it conducts electricity, it is shiny when freshly cut and "
            "it forms positive ions, which is all that a metal has to do",
            "Sound, because every element on the left of the periodic table "
            "behaves in the same way as the rest",
            "Only partly — it conducts and forms positive ions, but it is far "
            "softer, lighter and more reactive than most metals",
            "Unsound — it forms negative ions, which no metal does, so it "
            "cannot be counted as a metal at all",
        ],
        "correct_index": 2,
        "why": "The chemistry is metallic but the physical properties are "
               "extreme, which is what makes the group worth studying.",
    },
    {
        "id": "ks4-group-1-h10",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a Group 1 metal would be a hopeless choice for a "
                "cooking pan.",
        "options": [
            "It conducts heat too poorly for the food inside the pan to be "
            "warmed through evenly",
            "It is too dense to be lifted safely once a quantity of food has "
            "been put into it",
            "It would shatter the first time it was placed on a hot ring, "
            "because it is so brittle",
            "It is soft, melts at a low temperature and reacts violently with "
            "water",
        ],
        "correct_index": 3,
        "why": "Any one of the three would rule it out; together they make "
               "the idea impossible.",
    },
    {
        "id": "ks4-group-1-h11",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that reactivity rises down Group 1 "
                "because the atoms get heavier.",
        "options": [
            "Unsound — mass is not what is tested; the outer electron is "
            "lost more easily because it is further out and shielded",
            "Sound — a heavier atom carries more momentum and so collides a "
            "good deal harder with each water molecule that it happens to "
            "meet",
            "Sound, because relative atomic mass and reactivity climb "
            "together down every group in the table",
            "Unsound — the atoms actually get lighter down the group, which "
            "is the real reason for the trend",
        ],
        "correct_index": 0,
        "why": "Mass rises down the group too, but it is a coincidence of the "
               "trend rather than its cause.",
    },
    {
        "id": "ks4-group-1-h12",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen if a piece of potassium were added "
                "to dilute hydrochloric acid.",
        "options": [
            "Nothing, because a metal that reacts with water cannot also "
            "react with an acid",
            "It would react even more violently than with water, giving "
            "potassium chloride and hydrogen",
            "It would react gently, giving potassium hydroxide and chlorine "
            "gas",
            "It would dissolve without any reaction, leaving a solution of "
            "the metal in the acid",
        ],
        "correct_index": 1,
        "why": "An acid is a more concentrated source of H+ than water is, so "
               "the same reaction runs faster and more dangerously.",
    },
    {
        "id": "ks4-group-1-h13",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the reaction of sodium with cold water with that of "
                "magnesium with cold water.",
        "options": [
            "Magnesium reacts vigorously while sodium shows no reaction at "
            "all with cold water",
            "Both react vigorously, and both give off hydrogen at about the "
            "same rate as one another",
            "Sodium reacts vigorously; magnesium reacts only very slowly with "
            "cold water",
            "Neither reacts, because a metal needs steam rather than cold "
            "water before anything happens",
        ],
        "correct_index": 2,
        "why": "Sodium's single outer electron goes far more readily than "
               "magnesium's two, which is why magnesium needs steam.",
    },
    {
        "id": "ks4-group-1-h14",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the mass of lithium hydroxide formed when 0.7 g of "
                "lithium reacts completely with water. (Li = 7, O = 16, H = 1)",
        "options": [
            "0.7 g",
            "7.0 g",
            "24 g",
            "2.4 g",
        ],
        "correct_index": 3,
        "why": "0.7 ÷ 7 = 0.1 mol of lithium gives 0.1 mol of LiOH, and LiOH "
               "has a relative formula mass of 24, so 0.1 × 24 = 2.4 g.",
    },
    {
        "id": "ks4-group-1-h15",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a Group 1 metal is kept under oil rather than "
                "under water.",
        "options": [
            "Oil keeps air away without reacting, while water would react "
            "with the metal at once",
            "Oil is denser than the metal and holds it down, while water "
            "would let it float up into the air",
            "Oil conducts heat away from the metal, while water would let it "
            "warm up and catch fire",
            "Oil dissolves the layer of oxide from the surface, while water "
            "would leave the layer in place",
        ],
        "correct_index": 0,
        "why": "The whole point is to exclude both air and water, and oil "
               "does the first without being the second.",
    },
    {
        "id": "ks4-group-1-h16",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'Every Group 1 metal floats on "
                "water.'",
        "options": [
            "Sound — a low density is one of the properties that defines the "
            "whole of Group 1",
            "Too strong — lithium, sodium and potassium float, but rubidium "
            "and caesium are denser than water",
            "Unsound — none of them floats, and each sinks to the bottom "
            "before the reaction begins",
            "Sound, provided the water is cold, since a floating metal sinks "
            "as soon as the water is warmed",
        ],
        "correct_index": 1,
        "why": "The three metals a pupil sees do float, but the statement "
               "does not hold for the whole group.",
    },
    {
        "id": "ks4-group-1-h17",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium sulfate has the formula Na2SO4. Deduce the charge "
                "carried by the sulfate ion in it.",
        "options": [
            "1-",
            "1+",
            "2-",
            "2+",
        ],
        "correct_index": 2,
        "why": "Two sodium ions carry 2+ between them, so the sulfate ion "
               "must carry 2- for the compound to be neutral.",
    },
    {
        "id": "ks4-group-1-h18",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of sodium oxide and sodium hydroxide is "
                "formed when sodium reacts with water.",
        "options": [
            "Sodium oxide, because the water supplies the oxygen the metal "
            "needs to form it",
            "Both are formed together, in equal amounts, whenever sodium "
            "meets water",
            "Neither, because sodium reacts with water to give sodium metal "
            "back along with oxygen",
            "Sodium hydroxide, because the metal takes the whole hydroxide "
            "group from the water",
        ],
        "correct_index": 3,
        "why": "The oxide comes from burning in oxygen; water gives the "
               "hydroxide and hydrogen.",
    },
    {
        "id": "ks4-group-1-h19",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the hydrogen from potassium reacting with water "
                "often catches fire but the hydrogen from lithium does not.",
        "options": [
            "The potassium reaction is faster and releases heat more quickly, "
            "so the gas reaches its ignition temperature",
            "The potassium reaction gives a different gas, which is far "
            "easier to set alight than hydrogen is",
            "The lithium reaction gives off no hydrogen, so there is nothing "
            "present that could catch fire",
            "The potassium floats higher in the water, so its gas meets the "
            "air sooner and lights on contact",
        ],
        "correct_index": 0,
        "why": "Same gas, same air — the difference is how much energy is "
               "released in how short a time.",
    },
    {
        "id": "ks4-group-1-h20",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the energy needed to remove the outer electron from "
                "a lithium atom with that needed for a potassium atom.",
        "options": [
            "More is needed for potassium, because it has more electrons to "
            "be pulled past on the way out",
            "Less is needed for potassium, because its outer electron is "
            "further from the nucleus and shielded",
            "The same is needed for both, because each has a single outer "
            "electron to remove",
            "More is needed for potassium, because it has the greater nuclear "
            "charge of the two",
        ],
        "correct_index": 1,
        "why": "Easier removal is precisely what greater reactivity means in "
               "Group 1.",
    },
    {
        "id": "ks4-group-1-h21",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A very small piece of lithium is dropped into a large trough "
                "of water. Deduce the effect on the pH.",
        "options": [
            "The pH falls sharply, because hydrogen gas dissolves back into "
            "the water",
            "The pH stays at 7 exactly, because so little lithium was used",
            "The pH rises, though only a little, because the hydroxide formed "
            "is spread through a large volume",
            "The pH rises to 14, because lithium hydroxide is a strong alkali "
            "whatever quantity is present",
        ],
        "correct_index": 2,
        "why": "The product is alkaline, but concentration matters: a tiny "
               "amount of alkali in a lot of water moves the pH only a little.",
    },
    {
        "id": "ks4-group-1-h22",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a more reactive metal is a more "
                "useful metal.",
        "options": [
            "Sound — a metal that reacts readily can be turned into a far "
            "greater number of useful compounds than one that does not",
            "Sound, because the reactivity series is arranged with the most "
            "useful metals placed at the top of it",
            "Unsound — a reactive metal is harder to extract, and that is its "
            "one drawback",
            "Unsound — reactivity makes a metal useless as a structural "
            "material, which is why iron and aluminium are used instead",
        ],
        "correct_index": 3,
        "why": "Usefulness depends on the job: sodium is reactive and "
               "valuable in chemistry, but nobody builds a bridge from it.",
    },
    {
        "id": "ks4-group-1-h23",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a Group 1 metal reacts with chlorine as readily "
                "as it reacts with water.",
        "options": [
            "In both reactions the metal gives away the same single outer "
            "electron to a substance that wants it",
            "In both reactions the metal takes an electron in, which is the "
            "one thing a Group 1 atom is able to do",
            "In both reactions the metal is broken down into its separate "
            "atoms before anything else happens",
            "In both reactions the metal is heated, and a heated metal reacts "
            "with whatever it happens to meet",
        ],
        "correct_index": 0,
        "why": "The metal's half of the reaction is the same either way; only "
               "the electron's destination changes.",
    },
    {
        "id": "ks4-group-1-h24",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "0.2 mol of sodium is dropped into excess water. Determine "
                "the mass of sodium hydroxide produced. (NaOH = 40)",
        "options": [
            "4.0 g of sodium hydroxide",
            "8.0 g of sodium hydroxide",
            "40 g of sodium hydroxide",
            "0.2 g of sodium hydroxide",
        ],
        "correct_index": 1,
        "why": "Each sodium atom gives one NaOH, so 0.2 mol of NaOH forms, "
               "and 0.2 × 40 = 8.0 g.",
    },
    {
        "id": "ks4-group-1-h25",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why sodium hydroxide is used in oven cleaners.",
        "options": [
            "Because it is a neutral compound and so cannot damage the metal "
            "surface of the oven",
            "Because it releases hydrogen, and the bubbles lift the burnt "
            "food away from the surface",
            "Because it is a strong alkali, which attacks the burnt-on fat "
            "and breaks it down",
            "Because it evaporates quickly, carrying the grease away with it "
            "as it goes",
        ],
        "correct_index": 2,
        "why": "Strong alkalis break fats down, which is why oven cleaner is "
               "corrosive and has to be handled with gloves.",
    },
    {
        "id": "ks4-group-1-h26",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium sits in Group 2. Deduce how the charge on a "
                "magnesium ion differs from the charge on a sodium ion, and "
                "say why.",
        "options": [
            "Group 1 forms 2+ ions and Group 2 forms 1+ ions, which is why "
            "the two groups are numbered the way they are",
            "Both form 1+ ions, and the difference between the groups lies in "
            "how quickly each of them reacts",
            "Group 1 forms 1- ions and Group 2 forms 2- ions, since both "
            "groups gain electrons in a reaction",
            "Group 1 forms 1+ ions by losing one electron; Group 2 forms 2+ "
            "ions by losing two",
        ],
        "correct_index": 3,
        "why": "The charge on the ion matches the number of outer electrons "
               "the atom has to shed.",
    },
]
