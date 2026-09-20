"""Chemistry · Atomic structure and the periodic table — transition metals ·
the MRB-338 expansion.

Forty-two rows on the central block, chemistry-only content (AQA 4.1.3). The
weight falls on the four characteristic properties and on doing something with
each of them rather than listing them: variable charge worked out from a
formula, coloured compounds named with their colours, catalysts identified with
the process they serve, and the Group 1 comparison made with real melting-point
and density figures. Three rows carry formula-mass and percentage-composition
calculations.

Every row is tier `foundation` and `triple_only` True, exactly as the
curriculum classifies the subtopic.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-transition-metals-e05",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether a transition metal is harder or softer than a "
                "Group 1 metal.",
        "options": [
            "Harder",
            "Softer",
            "The two are equally hard as one another",
            "It depends on the temperature of the room they are in",
        ],
        "correct_index": 0,
        "why": "The alkali metals can be cut with a knife; iron, copper and "
               "chromium cannot.",
    },
    {
        "id": "ks4-transition-metals-e06",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the transition metal used for the wiring inside a "
                "house.",
        "options": [
            "Titanium",
            "Copper",
            "Chromium",
            "Manganese",
        ],
        "correct_index": 1,
        "why": "Copper conducts electricity extremely well and is ductile "
               "enough to be drawn into long thin wires.",
    },
    {
        "id": "ks4-transition-metals-e07",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of a solution of iron(II) sulfate.",
        "options": [
            "Deep blue",
            "Colourless",
            "Pale green",
            "Bright purple",
        ],
        "correct_index": 2,
        "why": "Iron(II) compounds in solution are pale green; iron(III) "
               "compounds are orange-brown.",
    },
    {
        "id": "ks4-transition-metals-e08",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the transition metal used as the catalyst in the Haber "
                "process.",
        "options": [
            "Copper",
            "Zinc",
            "Silver",
            "Iron",
        ],
        "correct_index": 3,
        "why": "An iron catalyst speeds up the combination of nitrogen and "
               "hydrogen to make ammonia.",
    },
    {
        "id": "ks4-transition-metals-e09",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a catalyst does.",
        "options": [
            "It speeds up a reaction without being used up itself",
            "It increases the mass of product a reaction can give",
            "It is used up steadily as the reaction it speeds up goes on",
            "It turns a reaction that gives out heat into one that takes it in",
        ],
        "correct_index": 0,
        "why": "A catalyst offers a route of lower activation energy and is "
               "recovered unchanged at the end.",
    },
    {
        "id": "ks4-transition-metals-e10",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the metal alloyed with copper to make brass.",
        "options": [
            "Tin",
            "Zinc",
            "Nickel",
            "Lead",
        ],
        "correct_index": 1,
        "why": "Brass is copper with zinc; bronze is copper with tin.",
    },
    {
        "id": "ks4-transition-metals-e11",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the density of a transition metal with that of a "
                "Group 1 metal.",
        "options": [
            "The transition metal is the less dense of the two",
            "The two have much the same density as one another",
            "The transition metal is the denser of the two",
            "The transition metal is denser only when it is warmed first",
        ],
        "correct_index": 2,
        "why": "Iron is 7.8 g/cm3 against lithium's 0.5 g/cm3 — dense enough "
               "to sink where the alkali metals float.",
    },
    {
        "id": "ks4-transition-metals-e12",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether the compounds of the transition metals are "
                "usually coloured or usually white.",
        "options": [
            "Usually white",
            "Usually colourless when dissolved",
            "Usually white when dry",
            "Usually coloured",
        ],
        "correct_index": 3,
        "why": "Blue copper sulfate, green iron(II) sulfate and purple "
               "potassium manganate(VII) are the standard examples.",
    },
    {
        "id": "ks4-transition-metals-e13",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the transition metal used in jewellery because it "
                "resists corrosion.",
        "options": [
            "Gold",
            "Iron",
            "Manganese",
            "Cobalt",
        ],
        "correct_index": 0,
        "why": "Gold is so unreactive that it keeps its shine indefinitely, "
               "which is why it is found as the free element.",
    },
    {
        "id": "ks4-transition-metals-e14",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the charge carried by the iron ion in iron(III) "
                "chloride.",
        "options": [
            "2+",
            "3+",
            "3-",
            "1+",
        ],
        "correct_index": 1,
        "why": "The roman numeral in the name gives the charge on the metal "
               "ion, so iron(III) is Fe3+.",
    },
    {
        "id": "ks4-transition-metals-e15",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the transition metal added to iron to make stainless "
                "steel resist rusting.",
        "options": [
            "Titanium",
            "Silver",
            "Chromium",
            "Mercury",
        ],
        "correct_index": 2,
        "why": "Chromium, with some nickel, gives stainless steel its "
               "corrosion resistance.",
    },
    {
        "id": "ks4-transition-metals-e16",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the melting point a typical transition metal has.",
        "options": [
            "Below 0 degrees C",
            "Between 50 and 100 degrees C",
            "Between 100 and 300 degrees C",
            "Above 1000 degrees C",
        ],
        "correct_index": 3,
        "why": "Iron melts at 1538 degrees C; mercury, a liquid at room "
               "temperature, is the exception to the pattern.",
    },
    {
        "id": "ks4-transition-metals-e17",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of a solution of potassium manganate(VII).",
        "options": [
            "Purple",
            "Pale green",
            "Colourless",
            "Bright yellow",
        ],
        "correct_index": 0,
        "why": "The deep purple comes from the manganate(VII) ion, and it is "
               "one of the most striking transition metal colours.",
    },
    {
        "id": "ks4-transition-metals-e18",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one property of a transition metal that makes it "
                "useful as a building material.",
        "options": [
            "It is soft enough to be shaped by hand on a building site",
            "It is strong",
            "It melts easily",
            "It has a very low density, so a beam of it weighs nothing",
        ],
        "correct_index": 1,
        "why": "High tensile strength, together with a high melting point, is "
               "why steel frames and reinforcing bars are used.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-transition-metals-s05",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a transition metal does not have to be kept "
                "under oil.",
        "options": [
            "Because it is too dense to be covered by oil, which would float "
            "away on the top of it",
            "Because oil would react with its surface and spoil the metal "
            "underneath before long",
            "Because it reacts only slowly with air and water, so it is not "
            "spoilt by being left out",
            "Because it has already reacted with the air completely, so "
            "nothing further can happen to it",
        ],
        "correct_index": 2,
        "why": "Low reactivity is the whole point of the contrast with Group "
               "1, where air alone destroys the metal.",
    },
    {
        "id": "ks4-transition-metals-s06",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Copper is heated strongly in air. Name the compound formed "
                "and state its colour.",
        "options": [
            "Copper hydroxide, a pale blue solid",
            "Copper carbonate, a bright green solid",
            "Copper sulfate, a blue solid",
            "Copper oxide, a black solid",
        ],
        "correct_index": 3,
        "why": "A metal heated in air combines with oxygen, and copper oxide "
               "is black even though copper sulfate is blue.",
    },
    {
        "id": "ks4-transition-metals-s07",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a bridge is built from a transition metal rather "
                "than from a Group 1 metal.",
        "options": [
            "The transition metal is strong, hard and unreactive enough to "
            "stand in the weather for decades",
            "The transition metal is lighter, so the bridge puts less weight "
            "on the ground beneath it",
            "The transition metal melts at a lower temperature, which makes "
            "the parts easier to cast on site",
            "The transition metal is cheaper to obtain than any of the Group "
            "1 metals would be",
        ],
        "correct_index": 0,
        "why": "A Group 1 metal is soft, low-melting and would react with "
               "rain within minutes.",
    },
    {
        "id": "ks4-transition-metals-s08",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron melts at 1538 degrees C and sodium at 98 degrees C. "
                "State what this difference shows.",
        "options": [
            "That sodium's atoms are the heavier of the two, so they take "
            "longer to be warmed through",
            "That the bonding in a transition metal is far stronger than that "
            "in a Group 1 metal",
            "That iron is a compound while sodium is an element, and a "
            "compound melts higher than an element",
            "That iron contains more heat energy to begin with, so it has "
            "further to go before it melts",
        ],
        "correct_index": 1,
        "why": "Melting point measures how hard the structure is to break "
               "apart, and iron's is very much harder.",
    },
    {
        "id": "ks4-transition-metals-s09",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the two metals that are alloyed together to make bronze.",
        "options": [
            "Copper and zinc",
            "Iron and carbon",
            "Copper and tin",
            "Iron and chromium",
        ],
        "correct_index": 2,
        "why": "Bronze is copper with tin; copper with zinc gives brass "
               "instead.",
    },
    {
        "id": "ks4-transition-metals-s10",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce the formula of iron(II) chloride, given that a "
                "chloride ion is Cl-.",
        "options": [
            "FeCl",
            "Fe2Cl",
            "FeCl3",
            "FeCl2",
        ],
        "correct_index": 3,
        "why": "Iron(II) is Fe2+, so two chloride ions are needed to balance "
               "the charge.",
    },
    {
        "id": "ks4-transition-metals-s11",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why copper rather than iron is used for water pipes "
                "in a house.",
        "options": [
            "Copper resists corrosion by water and can be bent into shape "
            "without cracking",
            "Copper is the stronger of the two, so a copper pipe can be made "
            "with much thinner walls",
            "Copper melts at a lower temperature, which lets a plumber shape "
            "a pipe with a household kettle",
            "Copper reacts with water to form a hard lining that keeps the "
            "pipe from leaking",
        ],
        "correct_index": 0,
        "why": "An iron pipe would rust through; copper does not, and it is "
               "malleable enough to bend around corners.",
    },
    {
        "id": "ks4-transition-metals-s12",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe two ways in which a transition metal differs from a "
                "Group 1 metal.",
        "options": [
            "It is softer and melts lower, but it is far more reactive with "
            "water than a Group 1 metal is",
            "It is harder and melts higher, and it is far less reactive with "
            "water",
            "It forms white compounds and reacts violently with air, which a "
            "Group 1 metal does not do",
            "It has one fixed ion charge and forms colourless compounds",
        ],
        "correct_index": 1,
        "why": "Hardness, melting point, density and low reactivity are the "
               "four contrasts with Group 1.",
    },
    {
        "id": "ks4-transition-metals-s13",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce the charge on the manganese ion in MnO2, given that "
                "an oxide ion carries a 2- charge.",
        "options": [
            "2+",
            "7+",
            "4+",
            "2-",
        ],
        "correct_index": 2,
        "why": "Two oxide ions carry 4- between them, so the single manganese "
               "ion must carry 4+.",
    },
    {
        "id": "ks4-transition-metals-s14",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a catalyst is left out of the overall equation "
                "for a reaction.",
        "options": [
            "Because it is destroyed during the reaction and so has nothing "
            "left to write on either side",
            "Because it appears on the left of the equation only, which makes "
            "it easier to leave out entirely",
            "Because it changes from one reaction to the next and cannot be "
            "given a single fixed formula",
            "Because it is present unchanged at the end, so it would appear "
            "on both sides and cancel",
        ],
        "correct_index": 3,
        "why": "A catalyst is recovered, so writing it in twice would add "
               "nothing to the equation.",
    },
    {
        "id": "ks4-transition-metals-s15",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nichrome heating wire is an alloy of chromium with one other "
                "transition metal. Name it.",
        "options": [
            "Nickel",
            "Copper",
            "Zinc",
            "Silver",
        ],
        "correct_index": 0,
        "why": "Nichrome is nickel and chromium, chosen because it survives "
               "being heated red-hot again and again.",
    },
    {
        "id": "ks4-transition-metals-s16",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why stainless steel is chosen for surgical "
                "instruments.",
        "options": [
            "It is soft enough to be reshaped by the surgeon during an "
            "operation if that becomes necessary",
            "It resists corrosion, so it survives repeated washing and "
            "sterilising without rusting",
            "It melts at a low temperature, which makes each instrument "
            "cheap to cast in quantity",
            "It reacts with the skin to form a protective layer over the "
            "cut it has just made",
        ],
        "correct_index": 1,
        "why": "The chromium in the alloy keeps the surface from rusting "
               "however often the instrument is boiled or autoclaved.",
    },
    {
        "id": "ks4-transition-metals-s17",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce the formula of copper(II) sulfate, given that a "
                "sulfate ion is SO4 2-.",
        "options": [
            "Cu2SO4",
            "Cu(SO4)2",
            "CuSO4",
            "Cu2(SO4)3",
        ],
        "correct_index": 2,
        "why": "Cu2+ and SO4 2- carry equal and opposite charges, so they "
               "combine one to one.",
    },
    {
        "id": "ks4-transition-metals-s18",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why platinum is used in the catalytic converter of a "
                "car.",
        "options": [
            "Because it is the cheapest metal available and a converter has "
            "to be replaced several times in the life of a car",
            "Because it burns away slowly and the heat this releases is what "
            "drives the reaction on",
            "Because it dissolves in the exhaust gases and is carried through "
            "the converter with them",
            "Because it catalyses the reactions in the exhaust and survives "
            "the high temperature without corroding",
        ],
        "correct_index": 3,
        "why": "A converter runs hot and wet with acidic gases, so the "
               "catalyst has to be both effective and extremely unreactive.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-transition-metals-h05",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A vanadium compound is written V2O5. Work out the charge "
                "carried by each vanadium ion in it.",
        "options": [
            "5+",
            "2+",
            "10+",
            "5-",
        ],
        "correct_index": 0,
        "why": "Five oxide ions carry 10- between them, so two vanadium ions "
               "share 10+, which is 5+ each.",
    },
    {
        "id": "ks4-transition-metals-h06",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a transition metal can form ions of more than "
                "one charge while a Group 1 metal forms only one.",
        "options": [
            "A transition metal's ions differ in size rather than in charge, "
            "which is what gives the impression of a second ion",
            "A transition metal can lose different numbers of electrons, "
            "while a Group 1 atom has just one it can lose",
            "A transition metal gains electrons in some reactions and loses "
            "them in others, which changes the sign of the charge",
            "A transition metal is an alloy of several elements, and each of "
            "them contributes an ion of its own",
        ],
        "correct_index": 1,
        "why": "Iron gives up two electrons to form Fe2+ or three to form "
               "Fe3+; sodium has only the one outer electron to give.",
    },
    {
        "id": "ks4-transition-metals-h07",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare how a transition metal and a Group 1 metal each "
                "behave when left in air.",
        "options": [
            "Both tarnish within seconds, since every metal reacts with the "
            "oxygen in the air at the same rate",
            "The transition metal tarnishes at once while the Group 1 metal "
            "stays bright for months on end",
            "The transition metal changes slowly, if at all, while the Group "
            "1 metal dulls within seconds",
            "Neither changes at all, which is why both can be stored on an "
            "open shelf in a laboratory",
        ],
        "correct_index": 2,
        "why": "Iron takes days to show rust and gold never tarnishes; "
               "sodium is dull before the knife is put down.",
    },
    {
        "id": "ks4-transition-metals-h08",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that every metal in the central block "
                "behaves in exactly the same way.",
        "options": [
            "Sound — they share four characteristic properties, and sharing "
            "those properties is what defines the block",
            "Sound, provided the comparison is limited to the metals in the "
            "first row of the block",
            "Unsound — they share no properties at all, and the block is "
            "simply where the leftover elements were put",
            "Unsound — they share characteristic properties, but gold is "
            "unreactive where iron rusts, and mercury is a liquid",
        ],
        "correct_index": 3,
        "why": "The shared properties are a family likeness, not an identity; "
               "the exceptions are worth knowing by name.",
    },
    {
        "id": "ks4-transition-metals-h09",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the relative formula mass of copper(II) sulfate, "
                "CuSO4. (Cu = 64, S = 32, O = 16)",
        "options": [
            "160",
            "112",
            "96",
            "176",
        ],
        "correct_index": 0,
        "why": "64 + 32 + (4 × 16) = 64 + 32 + 64 = 160.",
    },
    {
        "id": "ks4-transition-metals-h10",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a very small mass of a transition metal catalyst "
                "can convert a very large mass of reactant.",
        "options": [
            "The catalyst is slowly used up, but so slowly that the mass lost "
            "cannot be measured on a school balance",
            "The catalyst splits into smaller and smaller pieces, so the "
            "amount of it available keeps on growing",
            "Each piece of catalyst is recovered unchanged and goes on to "
            "serve the next set of particles",
            "The catalyst joins the product, so the product outweighs the "
            "reactant",
        ],
        "correct_index": 2,
        "why": "Because it is not consumed, the same surface can be reused "
               "indefinitely, which is why so little is needed.",
    },
    {
        "id": "ks4-transition-metals-h11",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce the formula of iron(III) oxide, given that an oxide "
                "ion carries a 2- charge.",
        "options": [
            "FeO",
            "Fe3O2",
            "Fe2O3",
            "Fe3O",
        ],
        "correct_index": 2,
        "why": "Two Fe3+ ions carry 6+ and three O2- ions carry 6-, so the "
               "formula is Fe2O3.",
    },
    {
        "id": "ks4-transition-metals-h12",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron has a density of 7.8 g/cm3 and lithium 0.5 g/cm3. "
                "Deduce what would happen to a block of each if it were "
                "dropped into water.",
        "options": [
            "Both blocks would float, because a metal is less dense than "
            "water whichever part of the table it comes from",
            "The iron would sink and the lithium would float",
            "Both blocks would sink, because a metal is denser than water "
            "whichever part of the table it comes from",
            "The iron would float and the lithium would sink",
        ],
        "correct_index": 1,
        "why": "Water is 1.0 g/cm3, so 7.8 sinks and 0.5 floats — the "
               "alkali metals float and react at the surface.",
    },
    {
        "id": "ks4-transition-metals-h13",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a transition metal is the best "
                "choice for any job that needs a metal.",
        "options": [
            "Unsound — density and cost matter too, which is why aluminium "
            "is chosen for aircraft skins and drink cans",
            "Sound — a transition metal is harder, stronger and less reactive "
            "than every other metal in the table",
            "Sound, provided the job does not involve the metal being placed "
            "into water at any stage",
            "Unsound — a transition metal corrodes faster than any other kind "
            "of metal and so is rarely used",
        ],
        "correct_index": 0,
        "why": "Choosing a material weighs several properties at once, and "
               "strength is only one of them.",
    },
    {
        "id": "ks4-transition-metals-h14",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why adding a catalyst does not change the mass of "
                "product a reaction finally gives.",
        "options": [
            "Because the catalyst is used up in forming the product, so the "
            "two effects cancel one another out exactly",
            "Because it changes only how quickly the product forms, not how "
            "much reactant there was to start with",
            "Because the catalyst adds its own mass to the product, and that "
            "makes up for the reactant it consumes",
            "Because a catalyst works only at the start of a reaction and "
            "stops taking any part once it is under way",
        ],
        "correct_index": 1,
        "why": "Yield is set by the amounts of reactant; a catalyst changes "
               "the rate and nothing else.",
    },
    {
        "id": "ks4-transition-metals-h15",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce which of FeCl2 and FeCl3 contains iron carrying the "
                "larger positive charge.",
        "options": [
            "FeCl2, because it contains the smaller number of chloride ions",
            "Neither, because the iron carries the same charge in both of "
            "them",
            "FeCl3, because three chloride ions at 1- each need 3+ to balance "
            "them",
            "FeCl2, because a lower formula number always means a higher "
            "charge on the metal",
        ],
        "correct_index": 2,
        "why": "The number of chlorides counts the positive charges the metal "
               "ion has to supply.",
    },
    {
        "id": "ks4-transition-metals-h16",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the percentage by mass of copper in copper oxide, "
                "CuO. (Cu = 64, O = 16)",
        "options": [
            "20%",
            "64%",
            "25%",
            "80%",
        ],
        "correct_index": 3,
        "why": "CuO has a relative formula mass of 80, and 64 ÷ 80 × 100 = "
               "80%.",
    },
    {
        "id": "ks4-transition-metals-h17",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An iron catalyst is supplied as small lumps rather than as "
                "one solid block. Suggest why.",
        "options": [
            "Small lumps give a far larger surface area, so more reactant "
            "particles can meet the catalyst at once",
            "Small lumps are considerably cheaper to produce than a single "
            "large block of the same metal",
            "Small lumps melt more readily, and a molten catalyst speeds a "
            "reaction up far better than a solid one",
            "Small lumps are used up more slowly than one large block of the "
            "same total mass would be",
        ],
        "correct_index": 0,
        "why": "A catalyst works at its surface, so breaking the same mass "
               "into smaller pieces exposes far more of it.",
    },
    {
        "id": "ks4-transition-metals-h18",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what happens when iron and when potassium are each "
                "added to dilute hydrochloric acid.",
        "options": [
            "Neither reacts, because an acid attacks a metal oxide and never "
            "the metal itself",
            "Iron fizzes steadily while potassium reacts explosively; both "
            "give off hydrogen",
            "Potassium fizzes steadily while iron reacts explosively; both "
            "give off oxygen",
            "Both react at the same rate, since both of them are metals and "
            "the acid is the same",
        ],
        "correct_index": 1,
        "why": "Same reaction, very different rate: the metal that gives up "
               "its outer electrons more readily reacts faster.",
    },

    # ── standard (top-up) ──────────────────────────────────────────────
    {
        "id": "ks4-transition-metals-s19",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why titanium is chosen for an artificial hip joint "
                "rather than steel.",
        "options": [
            "It is stronger than steel and takes an unlimited load safely",
            "It is low in density and resists corrosion inside the body",
            "It is cheaper than steel, which matters for a mass-produced part",
            "It conducts electricity, which lets a surgeon check the joint "
            "later",
        ],
        "correct_index": 1,
        "why": "Titanium combines a low density with a corrosion resistance "
               "steel cannot match, which matters for a part left in the "
               "body for years.",
    },
    {
        "id": "ks4-transition-metals-s20",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the transition metal used as a catalyst when vegetable "
                "oil is hardened into margarine.",
        "options": [
            "Nickel",
            "Silver",
            "Gold",
            "Chromium",
        ],
        "correct_index": 0,
        "why": "Nickel catalyses the addition of hydrogen to the oil, which "
               "is the reaction that hardens it into margarine.",
    },
    {
        "id": "ks4-transition-metals-s21",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Manganese(IV) oxide speeds up the breakdown of hydrogen "
                "peroxide into water and oxygen. State the role it plays in "
                "this reaction.",
        "options": [
            "It is oxidised as the hydrogen peroxide breaks down",
            "It is the catalyst, and it is recovered unchanged at the end",
            "It is one of the two products the hydrogen peroxide breaks into",
            "It reacts to form water, which speeds the breakdown up",
        ],
        "correct_index": 1,
        "why": "Manganese(IV) oxide is a classic catalyst for this "
               "decomposition and is left chemically unchanged once the gas "
               "has stopped bubbling off.",
    },
    {
        "id": "ks4-transition-metals-s22",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mercury is a transition metal that is liquid at room "
                "temperature. State what this shows about the general rule "
                "that transition metals have high melting points.",
        "options": [
            "The rule is wrong, because most transition metals are in fact "
            "liquids",
            "The rule holds without any exception among the transition metals",
            "The rule is a pattern with an exception, and mercury is that "
            "exception",
            "The rule applies only to metals discovered before the twentieth "
            "century",
        ],
        "correct_index": 2,
        "why": "Iron, copper and the rest melt well above 1000 degrees C, but "
               "mercury is the one transition metal that breaks the pattern.",
    },
    {
        "id": "ks4-transition-metals-s23",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why pure iron is alloyed with carbon before it is "
                "used for construction.",
        "options": [
            "Carbon lowers the melting point, so the iron is easier to pour "
            "into a mould",
            "Carbon disrupts the layers of iron atoms, so the resulting steel "
            "is harder",
            "Carbon reacts with the iron to give a compound that resists rust "
            "completely",
            "Carbon makes the iron lighter, which is useful in tall buildings",
        ],
        "correct_index": 1,
        "why": "Pure iron is too soft on its own; carbon atoms of a different "
               "size break up the regular layers and give steel its extra "
               "hardness.",
    },
    {
        "id": "ks4-transition-metals-s24",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one property of silver that makes it useful in an "
                "electrical contact.",
        "options": [
            "It is magnetic, so it holds the contact closed under vibration",
            "It is an excellent conductor and resists corrosion at the "
            "contact surface",
            "It is the cheapest metal that will conduct electricity at all",
            "It melts at a very low temperature, so it solders easily in "
            "place",
        ],
        "correct_index": 1,
        "why": "A corroded contact conducts poorly, so silver's combination "
               "of high conductivity and resistance to tarnishing keeps the "
               "connection reliable.",
    },
    {
        "id": "ks4-transition-metals-s25",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why copper is used for the pipes inside a heat "
                "exchanger rather than a Group 1 metal.",
        "options": [
            "Copper is low in density, so the exchanger weighs very little",
            "Copper conducts heat well and does not react with the water "
            "flowing through it",
            "Copper is soft, so the pipes can be bent tightly around corners",
            "Copper is magnetic, so it can be gripped and positioned by a "
            "machine",
        ],
        "correct_index": 1,
        "why": "A heat exchanger has to pass heat through its walls without "
               "the metal itself reacting with what is flowing past it.",
    },
    {
        "id": "ks4-transition-metals-s26",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Vanadium(V) oxide is the catalyst used to make sulfuric acid "
                "in the Contact process. State the transition metal property "
                "this is an example of.",
        "options": [
            "Coloured compounds",
            "Catalytic activity",
            "High density",
            "Variable oxidation states",
        ],
        "correct_index": 1,
        "why": "Speeding up a reaction without being used up in it is what "
               "catalytic activity means, and vanadium(V) oxide does exactly "
               "that in the Contact process.",
    },

    # ── harder (top-up) ─────────────────────────────────────────────────
    {
        "id": "ks4-transition-metals-h19",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the relative formula mass of iron(III) oxide, "
                "Fe2O3. (Fe = 56, O = 16)",
        "options": [
            "72",
            "160",
            "104",
            "88",
        ],
        "correct_index": 1,
        "why": "(2 × 56) + (3 × 16) = 112 + 48 = 160.",
    },
    {
        "id": "ks4-transition-metals-h20",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the percentage by mass of iron in iron(III) oxide, "
                "Fe2O3, given that its relative formula mass is 160 and iron "
                "has a relative atomic mass of 56.",
        "options": [
            "35.0%",
            "56.0%",
            "70.0%",
            "48.0%",
        ],
        "correct_index": 2,
        "why": "Two iron atoms give 112 out of a total of 160, and "
               "(112 ÷ 160) × 100 = 70.0%.",
    },
    {
        "id": "ks4-transition-metals-h21",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the job done by the iron catalyst in the Haber "
                "process with the job done by vanadium(V) oxide in the "
                "Contact process.",
        "options": [
            "Both speed up a different reaction, without being consumed by "
            "either one",
            "Iron is consumed as ammonia forms, while vanadium(V) oxide is "
            "not consumed",
            "Both react completely to form part of the final product they "
            "help to make",
            "Iron raises the equilibrium yield, while vanadium(V) oxide only "
            "raises the rate",
        ],
        "correct_index": 0,
        "why": "Each is a catalyst for a different industrial reaction, "
               "recovered unchanged, and neither one changes the equilibrium "
               "position of the reaction it serves.",
    },
    {
        "id": "ks4-transition-metals-h22",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Titanium costs far more per kilogram than stainless steel, "
                "yet it is chosen for a hip joint over stainless steel. "
                "Evaluate this choice.",
        "options": [
            "A poor choice: cost should always outweigh a small gain in "
            "corrosion resistance inside the body",
            "A poor choice, because stainless steel is in fact lighter than "
            "titanium of the same strength",
            "A good choice, because the joint must not corrode over decades "
            "and must not add unnecessary weight",
            "A good choice, because titanium is magnetic and can be found "
            "again easily by a scanner",
        ],
        "correct_index": 2,
        "why": "A joint fitted once has to last for the rest of a patient's "
               "life, so long-term corrosion resistance and a low mass "
               "outweigh the higher price of the metal.",
    },
    {
        "id": "ks4-transition-metals-h23",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nickel forms an oxide in which the metal ion carries a 2+ "
                "charge. Deduce the formula of nickel oxide and calculate its "
                "relative formula mass. (Ni = 59, O = 16)",
        "options": [
            "Ni2O, relative formula mass 134",
            "NiO2, relative formula mass 91",
            "NiO, relative formula mass 75",
            "Ni2O3, relative formula mass 166",
        ],
        "correct_index": 2,
        "why": "A 2+ nickel ion balances a single 2- oxide ion, giving NiO, "
               "and 59 + 16 = 75.",
    },
    {
        "id": "ks4-transition-metals-h24",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why titanium survives for decades in damp soil while "
                "an unprotected iron pipe rusts through within a few years.",
        "options": [
            "Titanium is denser than iron, so water cannot reach far enough "
            "into it to cause damage",
            "Titanium forms a thin oxide layer that seals its surface, "
            "whereas iron's oxide flakes away",
            "Titanium does not react with oxygen at all, unlike iron, which "
            "reacts readily",
            "Titanium is a transition metal and iron is not, and only a "
            "transition metal can resist corrosion",
        ],
        "correct_index": 1,
        "why": "Titanium reacts to form a dense, adherent oxide that blocks "
               "further attack, while iron's oxide is porous and keeps "
               "exposing fresh metal.",
    },
    {
        "id": "ks4-transition-metals-h25",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that because iron catalyses the Haber "
                "process, it will also speed up any other reaction it is "
                "added to. Evaluate this claim.",
        "options": [
            "Sound, because every transition metal catalyses every reaction "
            "it is placed in",
            "Sound, because a catalyst works by supplying a metal surface, "
            "and any surface will do",
            "Unsound: a catalyst suits a particular reaction, which is why "
            "different processes use different metals",
            "Unsound, because iron stops being a catalyst once it has been "
            "used in one reaction",
        ],
        "correct_index": 2,
        "why": "Iron catalyses the Haber process, nickel catalyses "
               "hydrogenation and vanadium(V) oxide the Contact process — "
               "each is specific to the reaction it is chosen for.",
    },
    {
        "id": "ks4-transition-metals-h26",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the percentage by mass of iron in iron(III) "
                "chloride, FeCl3. (Fe = 56, Cl = 35.5)",
        "options": [
            "26.7%",
            "34.5%",
            "56.0%",
            "61.2%",
        ],
        "correct_index": 1,
        "why": "The relative formula mass is 56 + (3 × 35.5) = 162.5, and "
               "(56 ÷ 162.5) × 100 = 34.5%.",
    },
]
