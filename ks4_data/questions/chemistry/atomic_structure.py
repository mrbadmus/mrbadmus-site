"""Chemistry · Atomic structure and the periodic table (AQA 8462, 5.1).

Thirteen subtopics, twelve questions each: atoms/elements/compounds and
separating mixtures, the history of the atomic model, subatomic particles,
isotopes and relative atomic mass, electronic structure, the periodic table
and its development, metals versus non-metals, and Groups 0, 1, 7 plus the
transition metals.

The distractors are built from the mistakes the lesson pages themselves
declare: a compound treated as a mixture, filtration used on a dissolved
solid, "most alpha particles bounced back", protons changing when an ion
forms, Ar taken as a simple average rather than a weighted one, group number
confused with period number, Mendeleev's mass ordering confused with the
modern atomic-number ordering, "no non-metal conducts", noble gases written
as diatomic molecules, and — most of all — the Group 1 reactivity trend read
in the same direction as the Group 7 one.

⚠️ None of these restates a lesson page's own "Test yourself" question: that
is a different pool, printed on a page the child can open at will.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── atoms-elements-compounds ────────────────────────────────────
    {
        "id": "ks4-atoms-elements-compounds-e01",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement correctly describes an element?",
        "options": [
            "A substance made of two or more different types of atom "
            "chemically bonded together",
            "A substance made of only one type of atom",
            "A substance made of two or more different substances that "
            "are not bonded together",
            "A substance whose atoms all have the same mass number",
        ],
        "correct_index": 1,
        "why": "An element contains only one type of atom, which is why it "
               "cannot be broken down into simpler substances by a chemical "
               "reaction.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e02",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "How many atoms in total are there in one molecule of sulfuric "
                "acid, H2SO4?",
        "options": [
            "3 atoms — one for each element named in the formula",
            "4 atoms — the largest number written in the formula",
            "6 atoms — counting only the hydrogen and the oxygen atoms",
            "7 atoms — counting every atom in the whole formula",
        ],
        "correct_index": 3,
        "why": "H2SO4 contains 2 hydrogen atoms, 1 sulfur atom and 4 oxygen "
               "atoms, which is 7 atoms in total.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e03",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these substances is an element?",
        "options": [
            "Argon, Ar",
            "Ammonia, NH3",
            "Carbon monoxide, CO",
            "Sea water",
        ],
        "correct_index": 0,
        "why": "Argon is made of one type of atom only; ammonia and carbon "
               "monoxide are compounds and sea water is a mixture.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e04",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of process needed to split water into hydrogen "
                "and oxygen.",
        "options": [
            "Filtration, because the gases are trapped between the "
            "water particles",
            "Distillation, because hydrogen and oxygen have different "
            "boiling points",
            "A chemical process such as electrolysis, because the "
            "elements are chemically bonded",
            "Gentle warming, because the two gases separate on their "
            "own",
        ],
        "correct_index": 2,
        "why": "In a compound the elements are chemically bonded, so only a "
               "chemical reaction such as electrolysis can separate them.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s01",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium ribbon burns in oxygen to form a white solid, "
                "magnesium oxide. Explain why the product is a compound and not "
                "a mixture.",
        "options": [
            "The magnesium and oxygen are chemically bonded in a fixed "
            "ratio, with new properties",
            "The magnesium and oxygen have been mixed so evenly that "
            "they now look like a single substance",
            "The product is a solid, and any solid made from two "
            "elements is a compound",
            "The oxygen has been destroyed in the reaction, leaving "
            "only magnesium in a new form",
        ],
        "correct_index": 0,
        "why": "Burning bonds the two elements chemically in a fixed ratio, "
               "giving a substance whose properties are nothing like those of "
               "magnesium or of oxygen.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s02",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which set of numbers balances the equation for the combustion "
                "of methane, __CH4 + __O2 -> __CO2 + __H2O?",
        "options": [
            "1, 1, 1, 1",
            "1, 2, 1, 2",
            "1, 2, 1, 1",
            "2, 2, 2, 2",
        ],
        "correct_index": 1,
        "why": "1 CH4 + 2 O2 -> 1 CO2 + 2 H2O gives 1 carbon, 4 hydrogen and 4 "
               "oxygen atoms on each side.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s03",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed container, 24 g of magnesium reacts completely "
                "with 16 g of oxygen. Calculate the mass of magnesium oxide "
                "formed.",
        "options": [
            "8 g",
            "20 g",
            "40 g",
            "384 g",
        ],
        "correct_index": 2,
        "why": "Atoms are conserved in a reaction, so the product mass equals "
               "the total reactant mass: 24 g + 16 g = 40 g.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s04",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Air contains nitrogen, oxygen, argon and carbon dioxide. "
                "Explain why air is classed as a mixture.",
        "options": [
            "The gases react together slowly, so new compounds are "
            "constantly forming and breaking apart in it",
            "The gases are present in a fixed ratio that never changes",
            "Air can only be separated by a chemical reaction such as "
            "electrolysis",
            "The gases are not chemically bonded, each keeps its own "
            "properties, and the proportions can vary",
        ],
        "correct_index": 3,
        "why": "Nothing in air is chemically bonded to anything else, so each "
               "gas keeps its own properties and physical methods such as "
               "fractional distillation separate them.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h01",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Sodium chloride must be dangerous to eat "
                "because chlorine is a toxic green gas.' Explain the mistake in "
                "this reasoning.",
        "options": [
            "Chlorine stops being toxic once it has been cooled into a "
            "liquid",
            "Sodium chloride is a mixture, so the chlorine in it is too "
            "dilute to do any harm",
            "In a compound the elements are chemically bonded, so it "
            "has new properties of its own",
            "The chlorine atoms are destroyed when sodium chloride "
            "forms, so none of the chlorine is left",
        ],
        "correct_index": 2,
        "why": "Bonding changes the substance completely: sodium chloride's "
               "properties are its own and are nothing like those of sodium "
               "metal or chlorine gas.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h02",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A colourless liquid boils at one fixed temperature. When "
                "electricity is passed through it, two different gases are "
                "given off. Deduce what the liquid is.",
        "options": [
            "A compound, because it is pure yet can be split chemically "
            "into more than one element",
            "A mixture, because more than one gas can be obtained from "
            "it",
            "An element, because it boils at a single fixed temperature",
            "A solution, because passing electricity through it "
            "releases the dissolved gases",
        ],
        "correct_index": 0,
        "why": "A single fixed boiling point shows the liquid is pure, and "
               "splitting into two elements shows those elements were "
               "chemically bonded — so it is a compound.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h03",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 50.0 g sample of calcium carbonate is heated in an open "
                "crucible until it fully decomposes, leaving 28.0 g of calcium "
                "oxide. Calculate the mass of carbon dioxide given off.",
        "options": [
            "1.79 g",
            "28.0 g",
            "78.0 g",
            "22.0 g",
        ],
        "correct_index": 3,
        "why": "Mass is conserved overall, so the gas that escaped must "
               "account for 50.0 g - 28.0 g = 22.0 g.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h04",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that sea water is a compound because salt is "
                "dissolved in the water. Evaluate this claim.",
        "options": [
            "Correct — dissolving forms chemical bonds between the salt "
            "and the water",
            "Incorrect — nothing is chemically bonded, the proportions "
            "vary, and distillation recovers both substances",
            "Incorrect — sea water is an element, because it behaves as "
            "one single pure substance",
            "Correct — sea water has a fixed boiling point, and only "
            "compounds have fixed boiling points",
        ],
        "correct_index": 1,
        "why": "Dissolving is a physical change: the salt and water are not "
               "bonded, the concentration can vary, and simple distillation "
               "separates them again.",
    },

    # ── mixtures ────────────────────────────────────────────────────
    {
        "id": "ks4-mixtures-e01",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which technique would you use to obtain the sand from a "
                "mixture of sand and water?",
        "options": [
            "Crystallisation",
            "Paper chromatography",
            "Filtration",
            "Fractional distillation",
        ],
        "correct_index": 2,
        "why": "Sand is insoluble, so its particles are too large to pass "
               "through the filter paper while the water runs through.",
    },
    {
        "id": "ks4-mixtures-e02",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the residue in a filtration.",
        "options": [
            "The insoluble solid left behind in the filter paper",
            "The liquid that passes through the filter paper",
            "The solid that forms as a hot solution cools",
            "The vapour that condenses inside the condenser",
        ],
        "correct_index": 0,
        "why": "The residue is the insoluble solid trapped by the paper; the "
               "liquid that passes through is called the filtrate.",
    },
    {
        "id": "ks4-mixtures-e03",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the technique used to separate the different dyes in a "
                "sample of ink.",
        "options": [
            "Filtration",
            "Crystallisation",
            "Simple distillation",
            "Paper chromatography",
        ],
        "correct_index": 3,
        "why": "The dyes dissolve in the solvent and travel different "
               "distances up the paper, so they separate into distinct spots.",
    },
    {
        "id": "ks4-mixtures-e04",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a simple distillation, state which part of the mixture is "
                "collected as the distillate.",
        "options": [
            "The solid left behind in the flask",
            "The vapour that has condensed back into a liquid",
            "The undissolved solid caught in the filter paper",
            "The crystals that form as the flask cools",
        ],
        "correct_index": 1,
        "why": "The liquid evaporates and the distillate is that vapour after "
               "it has cooled and condensed in the condenser.",
    },
    {
        "id": "ks4-mixtures-s01",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants large, regular crystals of copper sulfate from "
                "copper sulfate solution. Describe the best method.",
        "options": [
            "Filter the solution and dry the residue in a warm oven",
            "Boil the solution dry as quickly as possible over a strong "
            "flame",
            "Run the solution up chromatography paper and cut out the "
            "coloured spot",
            "Heat to concentrate the solution, then leave it to cool "
            "slowly so that crystals form",
        ],
        "correct_index": 3,
        "why": "Solubility falls as a solution cools, and cooling slowly gives "
               "the particles time to build large, regular, pure crystals.",
    },
    {
        "id": "ks4-mixtures-s02",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a fractionating column separating crude oil, explain why "
                "the fractions with the lowest boiling points are collected at "
                "the top.",
        "options": [
            "They are the lightest fractions, so they simply float "
            "above the others",
            "They condense first, at the hottest part of the column "
            "near the bottom",
            "They stay as a vapour until they reach the cooler top of "
            "the column, where they condense",
            "They are pushed upwards by the fractions with higher "
            "boiling points condensing below them",
        ],
        "correct_index": 2,
        "why": "The column is coolest at the top, so a vapour condenses only "
               "where the temperature drops below its own boiling point — the "
               "lowest boiling fractions travel furthest up.",
    },
    {
        "id": "ks4-mixtures-s03",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mixture of salt, sand and water is to be separated so that "
                "both the salt and the sand are recovered. Describe the correct "
                "order of techniques.",
        "options": [
            "Crystallise first to remove the salt, then filter off the "
            "sand",
            "Filter to remove the sand, then evaporate the filtrate to "
            "recover the salt",
            "Distil the mixture first to remove the sand, then filter "
            "the salt out of the water",
            "Use chromatography, which separates all three components "
            "in one step",
        ],
        "correct_index": 1,
        "why": "Sand is insoluble, so filtration removes it first; the salt is "
               "dissolved in the filtrate and is recovered by evaporating the "
               "water away.",
    },
    {
        "id": "ks4-mixtures-s04",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why filtration cannot be used to remove dissolved salt "
                "from salt solution.",
        "options": [
            "The dissolved particles are far too small to be caught by "
            "the filter paper",
            "The salt reacts with the filter paper and is destroyed "
            "before it can be collected",
            "The salt dissolves the filter paper, so the whole mixture "
            "leaks through",
            "Filtration only works on mixtures in which the liquid is "
            "coloured",
        ],
        "correct_index": 0,
        "why": "Filter paper separates by particle size, and dissolved ions "
               "are small enough to pass straight through the pores with the "
               "solvent.",
    },
    {
        "id": "ks4-mixtures-h01",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a chromatogram the solvent front travelled 12.0 cm and one "
                "dye has an Rf value of 0.35. Calculate the distance that dye "
                "travelled.",
        "options": [
            "4.2 cm",
            "34.3 cm",
            "12.4 cm",
            "0.03 cm",
        ],
        "correct_index": 0,
        "why": "Rf = distance moved by substance / distance moved by solvent, "
               "so the distance is 0.35 x 12.0 cm = 4.2 cm.",
    },
    {
        "id": "ks4-mixtures-h02",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In paper chromatography the pencil baseline must sit above the "
                "level of the solvent in the tank. Explain why.",
        "options": [
            "Pencil dissolves in the solvent, so the baseline has to be "
            "kept dry above the liquid surface",
            "The spots would dissolve into the solvent in the tank "
            "instead of travelling up the paper",
            "The solvent would otherwise travel down the paper rather "
            "than up it",
            "The paper would tear as soon as the baseline touched the "
            "solvent",
        ],
        "correct_index": 1,
        "why": "The dyes must be carried upwards by the rising solvent; a "
               "submerged spot simply washes off into the tank and nothing "
               "separates.",
    },
    {
        "id": "ks4-mixtures-h03",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Propanone (boiling point 56 degrees C) and ethanol (boiling "
                "point 78 degrees C) are mixed. Suggest why fractional "
                "distillation separates them better than simple distillation.",
        "options": [
            "Fractional distillation reaches a higher temperature, so "
            "far more of each liquid evaporates and is caught",
            "Simple distillation can only be used on solutions of "
            "solids, never on two liquids",
            "Their boiling points are close, so repeated evaporating "
            "and condensing up the column is needed",
            "The fractionating column filters out the liquid whose "
            "particles are larger",
        ],
        "correct_index": 2,
        "why": "With boiling points only 22 degrees C apart both liquids "
               "evaporate together, and only the repeated condensing and re- "
               "evaporating in the column gives a pure fraction.",
    },
    {
        "id": "ks4-mixtures-h04",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forensic scientist finds that an unknown dye and a known dye "
                "have the same Rf value in the same solvent. Evaluate what this "
                "shows.",
        "options": [
            "It proves beyond doubt that the two dyes are the same "
            "substance",
            "It proves the dyes are different, because identical "
            "substances always give different Rf values",
            "It shows nothing at all, because Rf values change every "
            "time the experiment is repeated",
            "It suggests they may be the same substance, but other "
            "substances can share an Rf value",
        ],
        "correct_index": 3,
        "why": "An Rf value is characteristic of a substance in a given "
               "solvent but is not unique to it, so a match is strong evidence "
               "rather than proof.",
    },

    # ── model-of-the-atom ───────────────────────────────────────────
    {
        "id": "ks4-model-of-the-atom-e01",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Dalton's 1803 model said an atom was like.",
        "options": [
            "A ball of positive charge with electrons dotted through it",
            "A tiny dense nucleus surrounded by electrons in fixed "
            "shells",
            "A nucleus of protons and neutrons with electrons in a "
            "cloud",
            "A tiny solid sphere that could not be split",
        ],
        "correct_index": 3,
        "why": "Dalton pictured atoms as solid, indivisible spheres, a model "
               "that only changed once the electron was discovered.",
    },
    {
        "id": "ks4-model-of-the-atom-e02",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which discovery showed that Dalton's solid sphere model had to "
                "be revised?",
        "options": [
            "The discovery of the neutron by Chadwick",
            "The discovery of the electron by Thomson",
            "The discovery of the noble gases",
            "The measurement of atomic numbers by Moseley",
        ],
        "correct_index": 1,
        "why": "Finding a tiny negative particle inside atoms proved they are "
               "not solid and indivisible, which led to the plum pudding "
               "model.",
    },
    {
        "id": "ks4-model-of-the-atom-e03",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist who proposed that electrons orbit the "
                "nucleus in fixed shells.",
        "options": [
            "John Dalton",
            "J. J. Thomson",
            "Niels Bohr",
            "James Chadwick",
        ],
        "correct_index": 2,
        "why": "Bohr's 1913 model placed electrons in fixed energy levels, "
               "which explained the line spectra earlier models could not.",
    },
    {
        "id": "ks4-model-of-the-atom-e04",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the plum pudding model placed the positive charge "
                "in an atom.",
        "options": [
            "Spread throughout the whole atom, with the electrons "
            "dotted in it",
            "Concentrated in one tiny nucleus right at the very centre "
            "of the atom",
            "Carried by the electrons themselves",
            "Found only in the outermost shells of the atom",
        ],
        "correct_index": 0,
        "why": "Thomson's model had a ball of positive charge filling the "
               "atom, which is exactly what the scattering results later ruled "
               "out.",
    },
    {
        "id": "ks4-model-of-the-atom-s01",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the alpha scattering experiment a small number of alpha "
                "particles were deflected through large angles. Explain what "
                "this showed.",
        "options": [
            "That atoms are mostly empty space",
            "That the positive charge in an atom is concentrated in a "
            "very small central region",
            "That electrons are far lighter than alpha particles",
            "That gold atoms are packed so closely together in the foil "
            "that they blocked the particles",
        ],
        "correct_index": 1,
        "why": "A large deflection needs a strong repulsion, so the positive "
               "charge must be concentrated in one tiny place rather than "
               "spread thinly through the atom.",
    },
    {
        "id": "ks4-model-of-the-atom-s02",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Chadwick's discovery of the neutron in 1932 "
                "improved the model of the atom.",
        "options": [
            "It explained why an atom's mass is greater than the mass "
            "of its protons alone",
            "It explained why atoms have no overall electrical charge, "
            "because neutrons balance the protons",
            "It explained why electrons are held in fixed shells",
            "It explained why the nucleus is positively charged",
        ],
        "correct_index": 0,
        "why": "Neutrons add mass without adding charge, which accounts for "
               "the extra mass that the protons alone could not explain.",
    },
    {
        "id": "ks4-model-of-the-atom-s03",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the nuclear model differs from the plum pudding "
                "model.",
        "options": [
            "The nuclear model has electrons; the plum pudding model "
            "has none at all",
            "The nuclear model has no positive charge, whereas the plum "
            "pudding model does",
            "The nuclear model fixes the electrons in place, whereas "
            "the plum pudding model has them moving",
            "The nuclear model puts the positive charge and nearly all "
            "the mass in a tiny central nucleus",
        ],
        "correct_index": 3,
        "why": "Rutherford moved the positive charge and the mass from being "
               "spread through the atom into a tiny, dense central nucleus.",
    },
    {
        "id": "ks4-model-of-the-atom-s04",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the alpha scattering experiment used a very thin "
                "sheet of gold foil rather than a thick block of gold.",
        "options": [
            "Gold is the only metal that alpha particles can travel "
            "through",
            "A thick block would have been too heavy for the apparatus "
            "to hold",
            "In a thick sample each particle would be deflected many "
            "times, so the results could not be interpreted",
            "Thin foil spreads the gold atoms further apart, leaving "
            "gaps for the particles to pass through",
        ],
        "correct_index": 2,
        "why": "With foil only a few atoms thick, each deflection can be put "
               "down to a single encounter, which is what makes the pattern of "
               "results meaningful.",
    },
    {
        "id": "ks4-model-of-the-atom-h01",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what the plum pudding model said would happen when "
                "alpha particles were fired at a thin metal foil.",
        "options": [
            "All of the particles would bounce straight back off the "
            "foil, because every atom is a solid positive lump",
            "All of the particles would be absorbed by the foil",
            "All of them would pass through with only small "
            "deflections, as the positive charge is spread thinly",
            "The particles would be attracted into the centre of each "
            "atom",
        ],
        "correct_index": 2,
        "why": "A thinly spread positive charge could not push an alpha "
               "particle hard, so the model predicted small deflections only — "
               "and the large ones destroyed it.",
    },
    {
        "id": "ks4-model-of-the-atom-h02",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'The gold foil experiment proved that the plum "
                "pudding model was bad science.' Evaluate this statement.",
        "options": [
            "Correct — a model that is later replaced was never good "
            "science",
            "Correct — Thomson should have carried out the scattering "
            "experiment himself before he published his model",
            "Incorrect — the plum pudding model was never tested by any "
            "experiment at all",
            "Incorrect — the model explained the evidence available at "
            "the time and was replaced when new evidence appeared",
        ],
        "correct_index": 3,
        "why": "A model is the best explanation of the evidence available, and "
               "being revised when new evidence arrives is a strength of the "
               "scientific method rather than a failure.",
    },
    {
        "id": "ks4-model-of-the-atom-h03",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the line spectrum of hydrogen supported Bohr's "
                "model rather than Rutherford's.",
        "options": [
            "Light is emitted at only certain fixed energies, which "
            "fits electrons occupying fixed energy levels",
            "Light is emitted at every possible energy, which fits "
            "electrons sitting anywhere around the nucleus",
            "The spectrum showed that the nucleus contains neutrons as "
            "well as protons",
            "The spectrum showed that a hydrogen atom contains more "
            "than one electron",
        ],
        "correct_index": 0,
        "why": "Only fixed energy levels can give fixed energy jumps, and "
               "fixed jumps are what produce separate spectral lines rather "
               "than a continuous band of colour.",
    },
    {
        "id": "ks4-model-of-the-atom-h04",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A typical atomic radius is about 1 x 10^-10 m and a typical "
                "nuclear radius about 1 x 10^-14 m. Determine roughly how many "
                "times smaller the nucleus is.",
        "options": [
            "About 100 times smaller",
            "About 10 000 times smaller",
            "About 10 times smaller",
            "About 1 000 000 times smaller",
        ],
        "correct_index": 1,
        "why": "1 x 10^-10 m divided by 1 x 10^-14 m is 10 000, which is why "
               "the atom is almost entirely empty space.",
    },

    # ── subatomic-particles ─────────────────────────────────────────
    {
        "id": "ks4-subatomic-particles-e01",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the relative charge and relative mass of a neutron.",
        "options": [
            "Charge 0, relative mass 1",
            "Charge -1, relative mass 1",
            "Charge +1, relative mass 1",
            "Charge 0, relative mass very close to zero",
        ],
        "correct_index": 0,
        "why": "A neutron carries no charge but has the same relative mass as "
               "a proton, 1, which is why it counts towards the mass number.",
    },
    {
        "id": "ks4-subatomic-particles-e02",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where in an atom are the electrons found?",
        "options": [
            "Packed inside the nucleus alongside the protons",
            "Spread evenly through the positive charge of the atom",
            "In shells, or energy levels, around the nucleus",
            "In the nucleus, but only in atoms that have become ions",
        ],
        "correct_index": 2,
        "why": "Electrons occupy shells around the nucleus; only protons and "
               "neutrons are found inside it.",
    },
    {
        "id": "ks4-subatomic-particles-e03",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which particle has a relative mass so small that it is treated "
                "as zero?",
        "options": [
            "The proton",
            "The electron",
            "The neutron",
            "The nucleus",
        ],
        "correct_index": 1,
        "why": "An electron has about 1/1836 of a proton's mass, so "
               "essentially all of an atom's mass sits in the nucleus.",
    },
    {
        "id": "ks4-subatomic-particles-e04",
        "subtopic_slug": "subatomic-particles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom gains two electrons. State the charge on the ion that "
                "forms.",
        "options": [
            "2+",
            "1-",
            "No charge, because gaining electrons keeps the atom "
            "neutral",
            "2-",
        ],
        "correct_index": 3,
        "why": "Each electron carries a 1- charge, so two extra electrons "
               "leave the particle with an overall charge of 2-.",
    },
    {
        "id": "ks4-subatomic-particles-s01",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sodium atom forms a Na+ ion. State what has happened to the "
                "number of protons.",
        "options": [
            "It has increased by one, and that is what gives the "
            "positive charge",
            "It has decreased by one, and that is what gives the "
            "positive charge",
            "It has not changed — only an electron has been lost",
            "It has doubled, which makes the ion more stable",
        ],
        "correct_index": 2,
        "why": "Chemical reactions only move electrons; the proton number "
               "defines the element and never changes.",
    },
    {
        "id": "ks4-subatomic-particles-s02",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A particle has 17 protons, 18 neutrons and 18 electrons. "
                "Determine its overall charge.",
        "options": [
            "1+",
            "No overall charge",
            "2-",
            "1-",
        ],
        "correct_index": 3,
        "why": "There is one more electron (18 negatives) than proton (17 "
               "positives), so the overall charge is 1-.",
    },
    {
        "id": "ks4-subatomic-particles-s03",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sulfide ion, S2-, forms from a sulfur atom that has 16 "
                "protons. Determine the number of electrons in the ion.",
        "options": [
            "18",
            "16",
            "14",
            "2",
        ],
        "correct_index": 0,
        "why": "A neutral sulfur atom has 16 electrons, and gaining two more "
               "to give the 2- charge makes 18.",
    },
    {
        "id": "ks4-subatomic-particles-s04",
        "subtopic_slug": "subatomic-particles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why almost all of the mass of an atom is found in the "
                "nucleus.",
        "options": [
            "The nucleus takes up almost all of the atom's volume",
            "Protons and neutrons each have a relative mass of 1, while "
            "an electron's mass is negligible",
            "The positive charge of the nucleus attracts extra mass "
            "towards it",
            "The electrons are spread out, so their mass is shared with "
            "the space around them",
        ],
        "correct_index": 1,
        "why": "Mass comes from the protons and neutrons packed in the "
               "nucleus; the electrons around it contribute almost nothing.",
    },
    {
        "id": "ks4-subatomic-particles-h01",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the nucleus must take up most of an atom's "
                "volume because it holds most of the atom's mass. Explain the "
                "error.",
        "options": [
            "There is no error — mass and volume always go together",
            "Mass and volume are different things: the nucleus has "
            "about a ten-thousandth of the atom's radius",
            "The error is that the electrons, not the nucleus, hold "
            "most of an atom's mass and most of its volume",
            "The error is that the nucleus has no volume at all",
        ],
        "correct_index": 1,
        "why": "Almost all the mass is packed into a nucleus about 10 000 "
               "times smaller in radius than the atom, so a dense nucleus and "
               "a mostly empty atom fit together perfectly.",
    },
    {
        "id": "ks4-subatomic-particles-h02",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Particle X has 12 protons, 12 neutrons and 10 electrons. "
                "Particle Y has 12 protons, 12 neutrons and 12 electrons. "
                "Compare them.",
        "options": [
            "Both are the same element: X is a 2+ ion and Y is a "
            "neutral atom",
            "They are different elements, because they have different "
            "numbers of electrons",
            "Both are ions of the same element, with charges of 2+ and "
            "2-",
            "They are isotopes of each other, because the electron "
            "number differs",
        ],
        "correct_index": 0,
        "why": "The proton number is the same, so both are the same element; X "
               "simply has two fewer electrons than protons, giving it a 2+ "
               "charge.",
    },
    {
        "id": "ks4-subatomic-particles-h03",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beam containing separate protons, neutrons and electrons "
                "passes between a positively charged plate and a negatively "
                "charged plate. Predict how each is affected.",
        "options": [
            "All three are pulled towards the negative plate",
            "The protons and the electrons are pulled the same way; the "
            "neutrons are not affected",
            "Only the neutrons are pulled to one side, because they are "
            "the heaviest particles",
            "The protons and the electrons bend in opposite directions, "
            "and the neutrons go straight on",
        ],
        "correct_index": 3,
        "why": "Opposite charges attract, so +1 protons bend towards the "
               "negative plate and -1 electrons the other way, while an "
               "uncharged neutron is unaffected.",
    },
    {
        "id": "ks4-subatomic-particles-h04",
        "subtopic_slug": "subatomic-particles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an ion has the same mass number as the atom it was "
                "formed from.",
        "options": [
            "Because an ion gains neutrons to replace any electrons it "
            "loses",
            "Because the electrons that move are taken from inside the "
            "nucleus, where the mass is",
            "Because mass number counts only protons and neutrons, and "
            "only electrons change",
            "Because the charge on the ion cancels out the change in "
            "mass",
        ],
        "correct_index": 2,
        "why": "Mass number is protons plus neutrons, and forming an ion "
               "alters neither; electrons are far too light to count.",
    },

    # ── relative-atomic-mass ────────────────────────────────────────
    {
        "id": "ks4-relative-atomic-mass-e01",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the atomic number of an element tells you.",
        "options": [
            "The number of protons and neutrons added together",
            "The number of protons in the nucleus",
            "The number of neutrons in the nucleus",
            "The average mass of the atoms of that element",
        ],
        "correct_index": 1,
        "why": "The atomic number is the proton number, and it is what decides "
               "which element an atom is.",
    },
    {
        "id": "ks4-relative-atomic-mass-e02",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom of aluminium has mass number 27 and atomic number 13. "
                "Calculate the number of neutrons it contains.",
        "options": [
            "14",
            "13",
            "27",
            "40",
        ],
        "correct_index": 0,
        "why": "Neutrons = mass number - atomic number = 27 - 13 = 14.",
    },
    {
        "id": "ks4-relative-atomic-mass-e03",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define an isotope.",
        "options": [
            "Atoms of different elements that share the same mass "
            "number",
            "Atoms of the same element with different numbers of "
            "protons",
            "Atoms of the same element with different numbers of "
            "neutrons",
            "Atoms of the same element with different numbers of "
            "electrons",
        ],
        "correct_index": 2,
        "why": "Isotopes share the proton number, which fixes the element, and "
               "differ only in neutron number, which changes the mass.",
    },
    {
        "id": "ks4-relative-atomic-mass-e04",
        "subtopic_slug": "relative-atomic-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which particles the mass number of an atom counts.",
        "options": [
            "Protons only",
            "Neutrons only",
            "Protons and electrons",
            "Protons and neutrons",
        ],
        "correct_index": 3,
        "why": "Mass number is the total number of particles in the nucleus, "
               "so it counts the protons and the neutrons.",
    },
    {
        "id": "ks4-relative-atomic-mass-s01",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium-39 has atomic number 19. Determine the numbers of "
                "protons, neutrons and electrons in a neutral atom of it.",
        "options": [
            "39 protons, 19 neutrons, 39 electrons",
            "19 protons, 39 neutrons, 19 electrons",
            "19 protons, 19 neutrons, 20 electrons",
            "19 protons, 20 neutrons, 19 electrons",
        ],
        "correct_index": 3,
        "why": "Protons = atomic number = 19, neutrons = 39 - 19 = 20, and a "
               "neutral atom has as many electrons as protons.",
    },
    {
        "id": "ks4-relative-atomic-mass-s02",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two isotopes of the same element react in exactly "
                "the same way.",
        "options": [
            "They have the same number of neutrons, and it is the "
            "neutrons that decide how an atom reacts",
            "They have the same electron arrangement, and chemical "
            "reactions involve the electrons",
            "They have the same mass, so they collide with the same "
            "energy",
            "They have the same density, so they mix in the same "
            "proportions",
        ],
        "correct_index": 1,
        "why": "Chemical behaviour is decided by the outer electrons, and "
               "isotopes of an element have identical electron arrangements.",
    },
    {
        "id": "ks4-relative-atomic-mass-s03",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of chlorine contains chlorine-35 and chlorine-37 "
                "atoms in the ratio 3 : 1. Calculate the relative atomic "
                "mass of chlorine.",
        "options": [
            "35.5",
            "36.0",
            "36.5",
            "35.0",
        ],
        "correct_index": 0,
        "why": "Ar is a weighted average, and a 3 : 1 ratio means four atoms "
               "in every group: (3 x 35 + 1 x 37) / 4 = 142 / 4 = 35.5.",
    },
    {
        "id": "ks4-relative-atomic-mass-s04",
        "subtopic_slug": "relative-atomic-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of neon contains only neon-20 and neon-22, and its "
                "relative atomic mass is 20.2. Deduce which isotope is the more "
                "abundant.",
        "options": [
            "Neon-22, because it has the larger mass number",
            "They are present in equal amounts, because 20.2 lies "
            "between the two masses",
            "Neon-20, because the relative atomic mass is much closer "
            "to 20 than to 22",
            "It cannot be deduced without knowing the number of "
            "neutrons",
        ],
        "correct_index": 2,
        "why": "Relative atomic mass is a weighted average, so it sits nearest "
               "the mass of the most abundant isotope, and 20.2 is very close "
               "to 20.",
    },
    {
        "id": "ks4-relative-atomic-mass-h01",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Gallium has two isotopes, gallium-69 and gallium-71, and a "
                "relative atomic mass of 69.8. Calculate the percentage "
                "abundance of gallium-71.",
        "options": [
            "40%",
            "60%",
            "20%",
            "80%",
        ],
        "correct_index": 0,
        "why": "If x% is gallium-71 then (69(100 - x) + 71x) / 100 = 69.8, "
               "which gives 2x = 80 and so x = 40%.",
    },
    {
        "id": "ks4-relative-atomic-mass-h02",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An element has isotopes of mass number 24 (79%), 25 (10%) and "
                "26 (11%). A student averages the three mass numbers and gives "
                "Ar = 25.0. Explain the error.",
        "options": [
            "The three mass numbers should have been added together "
            "instead of averaged, which would give 75",
            "Mass numbers cannot be used in this calculation — only the "
            "numbers of neutrons can",
            "The abundances should have been added to the masses before "
            "averaging them",
            "Ar is a weighted average: each mass must be multiplied by "
            "its abundance, giving 24.3",
        ],
        "correct_index": 3,
        "why": "A simple average treats a rare isotope as though it were as "
               "common as an abundant one; weighting by abundance gives 24.3.",
    },
    {
        "id": "ks4-relative-atomic-mass-h03",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Atom P has 6 protons and 8 neutrons; atom Q has 7 protons and "
                "7 neutrons. Compare their mass numbers and decide whether they "
                "are isotopes.",
        "options": [
            "They have the same mass number, and they are isotopes of "
            "one element",
            "Both have mass number 14, but they are different elements, "
            "so they are not isotopes",
            "They have different mass numbers, and that is what makes "
            "them isotopes",
            "Both have mass number 14, so they must be the same element",
        ],
        "correct_index": 1,
        "why": "Both total 14 nuclear particles, but isotopes must share the "
               "proton number — 6 and 7 protons are two different elements.",
    },
    {
        "id": "ks4-relative-atomic-mass-h04",
        "subtopic_slug": "relative-atomic-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why relative atomic masses in the periodic table are "
                "often not whole numbers, even though every individual atom has "
                "a whole-number mass number.",
        "options": [
            "Because the mass of the electrons is included in the value",
            "Because the values are rounded from a very precise "
            "measurement of one single atom",
            "Because most elements are a mixture of isotopes, and Ar is "
            "a weighted average",
            "Because a proton and a neutron do not have exactly the "
            "same mass",
        ],
        "correct_index": 2,
        "why": "Any single atom has a whole-number mass number, but the "
               "tabulated Ar averages all the naturally occurring isotopes in "
               "their real proportions.",
    },

    # ── electronic-structure ────────────────────────────────────────
    {
        "id": "ks4-electronic-structure-e01",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the maximum number of electrons that the second shell of "
                "an atom can hold.",
        "options": [
            "2",
            "4",
            "6",
            "8",
        ],
        "correct_index": 3,
        "why": "For the first 20 elements the shells fill 2, then 8, then 8, "
               "so the second shell holds a maximum of 8 electrons.",
    },
    {
        "id": "ks4-electronic-structure-e02",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Write the electronic structure of a fluorine atom, atomic "
                "number 9.",
        "options": [
            "9",
            "2.8.9",
            "2.7",
            "8.1",
        ],
        "correct_index": 2,
        "why": "The first shell takes 2 electrons and the remaining 7 go into "
               "the second shell, giving 2.7.",
    },
    {
        "id": "ks4-electronic-structure-e03",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which element has the electronic structure 2.8.8.2?",
        "options": [
            "Calcium, atomic number 20",
            "Magnesium, atomic number 12",
            "Argon, atomic number 18",
            "Silicon, atomic number 14",
        ],
        "correct_index": 0,
        "why": "The digits add up to 20 electrons, and a neutral atom with 20 "
               "electrons has 20 protons, which is calcium.",
    },
    {
        "id": "ks4-electronic-structure-e04",
        "subtopic_slug": "electronic-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many electrons an atom with the structure 2.8.3 has "
                "in its outer shell.",
        "options": [
            "2",
            "3",
            "8",
            "13",
        ],
        "correct_index": 1,
        "why": "The last number in an electronic structure is the outer shell "
               "count, so 2.8.3 has 3 outer electrons.",
    },
    {
        "id": "ks4-electronic-structure-s01",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium has atomic number 19. Explain why its electronic "
                "structure is 2.8.8.1 and not 2.8.9.",
        "options": [
            "For the first 20 elements the third shell holds only 8 "
            "electrons, so the next electron starts a fourth",
            "The third shell can hold 9 electrons, but only in a metal",
            "The outer electron is pushed out of the third shell by the "
            "repulsion of the eight electrons already there",
            "Potassium is in Period 3, so it is only allowed three "
            "shells",
        ],
        "correct_index": 0,
        "why": "Shells fill in order and, for these elements, the third shell "
               "is full at 8 — so the nineteenth electron begins the fourth "
               "shell.",
    },
    {
        "id": "ks4-electronic-structure-s02",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An atom has 15 electrons. Determine its electronic structure.",
        "options": [
            "2.8.8.5",
            "2.8.5",
            "2.13",
            "8.2.5",
        ],
        "correct_index": 1,
        "why": "Fill the inner shells first: 2 in the first, 8 in the second "
               "and the remaining 5 in the third, giving 2.8.5.",
    },
    {
        "id": "ks4-electronic-structure-s03",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the charge on the ion formed by an atom with the "
                "electronic structure 2.8.2.",
        "options": [
            "2-, because it gains two electrons",
            "1+, because it loses one electron",
            "No charge, because it already has a stable structure",
            "2+, because it loses both of its outer electrons",
        ],
        "correct_index": 3,
        "why": "A metal with two outer electrons loses both, leaving a full "
               "outer shell and two more protons than electrons.",
    },
    {
        "id": "ks4-electronic-structure-s04",
        "subtopic_slug": "electronic-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium is 2.8.1 and chlorine is 2.8.7. Explain why sodium "
                "forms a positive ion while chlorine forms a negative one.",
        "options": [
            "Sodium is the heavier atom, so it holds its electrons less "
            "tightly",
            "Chlorine has more electron shells than sodium does, so it "
            "attracts any nearby electrons more strongly",
            "Sodium loses one outer electron and chlorine gains one, so "
            "both end up with a full outer shell",
            "Sodium gains seven electrons while chlorine loses seven",
        ],
        "correct_index": 2,
        "why": "Losing one electron is far easier than losing seven, and "
               "gaining one is far easier than gaining seven — both routes "
               "reach a full outer shell.",
    },
    {
        "id": "ks4-electronic-structure-h01",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the combining ratio when an element with the structure "
                "2.8.7 reacts with an element with the structure 2.8.2.",
        "options": [
            "1 atom of each",
            "2 atoms of the 2.8.7 element to 1 atom of the 2.8.2 "
            "element",
            "1 atom of the 2.8.7 element to 2 atoms of the 2.8.2 "
            "element",
            "They would not combine at all, because both need to gain "
            "electrons",
        ],
        "correct_index": 1,
        "why": "The 2.8.2 atom loses two electrons but each 2.8.7 atom can "
               "accept only one, so two of them are needed for every one metal "
               "atom.",
    },
    {
        "id": "ks4-electronic-structure-h02",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Elements with the structures 2.8.8.1 and 2.1 both react with "
                "water. Predict which reacts more vigorously and explain why.",
        "options": [
            "The 2.1 element, because it has fewer electrons to lose",
            "The 2.1 element, because its outer electron sits in a "
            "shell that is almost full, which makes it unstable",
            "The 2.8.8.1 element, because its outer electron is further "
            "from the nucleus and so is lost more easily",
            "They react equally, because both have one outer electron",
        ],
        "correct_index": 2,
        "why": "Both are Group 1, but the extra shells put the outer electron "
               "of 2.8.8.1 further from the nuclear attraction, so it is lost "
               "more readily.",
    },
    {
        "id": "ks4-electronic-structure-h03",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says an atom with the structure 2.8.8 must be in "
                "Period 8 because its outer shell holds 8 electrons. Explain "
                "the error.",
        "options": [
            "There is no error — the period number is the number of "
            "outer electrons",
            "The period number is found by adding all the electrons "
            "together, which would give Period 18",
            "The period number is the number of electrons in the first "
            "shell, so it is Period 2",
            "The period number is the number of occupied shells, so it "
            "is Period 3",
        ],
        "correct_index": 3,
        "why": "Periods count shells and groups count outer electrons, so "
               "2.8.8 is three shells — Period 3 — and a full outer shell, "
               "Group 0.",
    },
    {
        "id": "ks4-electronic-structure-h04",
        "subtopic_slug": "electronic-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the structures 2.8.1 and 2.8.7 and explain why the two "
                "elements have very different chemical properties.",
        "options": [
            "They have different numbers of outer electrons, so one "
            "loses an electron and the other gains one",
            "They have different numbers of shells, so one is a metal "
            "and the other a non-metal",
            "They have different total numbers of electrons, and it is "
            "the total that decides how an element behaves",
            "One of them already has a full outer shell and the other "
            "does not",
        ],
        "correct_index": 0,
        "why": "Chemistry is decided by the outer shell: one outer electron is "
               "easily lost, whereas seven outer electrons make an atom that "
               "gains one instead.",
    },

    # ── periodic-table ──────────────────────────────────────────────
    {
        "id": "ks4-periodic-table-e01",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the rows of the periodic table are called.",
        "options": [
            "Groups",
            "Periods",
            "Blocks",
            "Series",
        ],
        "correct_index": 1,
        "why": "Rows are periods, and the period number tells you how many "
               "electron shells the atoms of those elements have.",
    },
    {
        "id": "ks4-periodic-table-e02",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The modern periodic table places the elements in order of "
                "which quantity?",
        "options": [
            "Increasing relative atomic mass",
            "Increasing number of neutrons",
            "Decreasing reactivity",
            "Increasing atomic number",
        ],
        "correct_index": 3,
        "why": "Elements are ordered by proton number, because that is what "
               "sets the electron arrangement and therefore the chemistry.",
    },
    {
        "id": "ks4-periodic-table-e03",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where in the periodic table are the non-metals found?",
        "options": [
            "Towards the top right",
            "On the far left-hand side",
            "In the central block between Groups 2 and 3",
            "Along the bottom two rows",
        ],
        "correct_index": 0,
        "why": "Metals occupy the left and centre of the table, and the non- "
               "metals sit in the top right corner with Group 0 at the right- "
               "hand edge.",
    },
    {
        "id": "ks4-periodic-table-e04",
        "subtopic_slug": "periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "How many electrons are in the outer shell of a Group 2 "
                "element?",
        "options": [
            "8",
            "1",
            "2",
            "It depends on which period the element is in",
        ],
        "correct_index": 2,
        "why": "For Groups 1 to 7 the group number is the number of outer "
               "electrons, so a Group 2 element has two.",
    },
    {
        "id": "ks4-periodic-table-s01",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the properties of the elements change going from "
                "left to right across Period 3.",
        "options": [
            "They change from metals, through metalloids, to non-metals "
            "and finally a noble gas",
            "They change from non-metals to metals as the atomic number "
            "increases",
            "They stay metallic right across the period, because every "
            "Period 3 element has three shells",
            "They alternate between metal and non-metal from one "
            "element to the next",
        ],
        "correct_index": 0,
        "why": "Across a period the number of outer electrons rises, so the "
               "elements become steadily less metallic: sodium at the left, "
               "argon at the right.",
    },
    {
        "id": "ks4-periodic-table-s02",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict which of these elements is in the same group as "
                "sodium, 2.8.1.",
        "options": [
            "Magnesium, 2.8.2",
            "Lithium, 2.1",
            "Neon, 2.8",
            "Aluminium, 2.8.3",
        ],
        "correct_index": 1,
        "why": "Elements in a group share the number of outer electrons, and "
               "lithium's 2.1 has one outer electron just as sodium's 2.8.1 "
               "does.",
    },
    {
        "id": "ks4-periodic-table-s03",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why atoms get larger going down a group.",
        "options": [
            "The nucleus gains protons, which push the electrons "
            "outwards",
            "The outer electrons repel one another more strongly in the "
            "heavier elements",
            "Each element down the group has one more occupied electron "
            "shell",
            "The atoms gain neutrons, which take up more room in the "
            "nucleus",
        ],
        "correct_index": 2,
        "why": "Going down a group adds a whole extra shell each time, so the "
               "outer electrons sit further out and the atom is bigger.",
    },
    {
        "id": "ks4-periodic-table-s04",
        "subtopic_slug": "periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silicon conducts electricity but is brittle. Suggest what this "
                "tells you about its position in the periodic table.",
        "options": [
            "It is a Group 1 metal, because metals conduct electricity",
            "It is a noble gas, because its properties are unusual",
            "It is a transition metal, because transition metals are "
            "hard and conduct electricity",
            "It is a metalloid, on the dividing line between the metals "
            "and the non-metals",
        ],
        "correct_index": 3,
        "why": "Conducting like a metal but breaking like a non-metal is "
               "exactly the mixed behaviour of a metalloid on the metal / non- "
               "metal boundary.",
    },
    {
        "id": "ks4-periodic-table-h01",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Element X is in Group 1 and Period 5. Predict how vigorously "
                "it reacts with water compared with potassium, which is in "
                "Group 1 and Period 4.",
        "options": [
            "Less vigorously, because the extra shielding leaves the "
            "outer electron harder to remove from the atom",
            "Exactly the same, because both have one outer electron",
            "More vigorously, because its outer electron is further "
            "from the nucleus and lost even more easily",
            "It would not react, because Period 5 elements are "
            "unreactive",
        ],
        "correct_index": 2,
        "why": "One extra shell means a weaker pull on the outer electron, so "
               "a Group 1 element lower down loses it more easily and reacts "
               "more violently.",
    },
    {
        "id": "ks4-periodic-table-h02",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an element's period number is the same as its "
                "number of occupied electron shells.",
        "options": [
            "Each new period begins when electrons start filling a new "
            "shell",
            "Each period holds exactly as many elements as a shell "
            "holds electrons",
            "Each period adds one proton to the nucleus, and each "
            "proton pulls in a new shell",
            "Each period is defined by the number of outer electrons "
            "its elements have",
        ],
        "correct_index": 0,
        "why": "A period is the run of elements that fills one shell, so an "
               "element in Period 4 has electrons occupying four shells.",
    },
    {
        "id": "ks4-periodic-table-h03",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare an element in Group 1, Period 2 with an element in "
                "Group 7, Period 2. Which statement is correct?",
        "options": [
            "They have the same number of outer electrons but different "
            "numbers of shells",
            "Both form negative ions, because they are in the same "
            "period",
            "The Group 7 element is the more metallic of the two",
            "Both have two occupied shells, but one has 1 outer "
            "electron and the other 7",
        ],
        "correct_index": 3,
        "why": "The period fixes the number of shells and the group fixes the "
               "outer electrons, and it is the outer electrons that make one a "
               "reactive metal and the other a reactive non-metal.",
    },
    {
        "id": "ks4-periodic-table-h04",
        "subtopic_slug": "periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chemists can predict the properties of an element before it "
                "has been studied. Explain how the periodic table makes this "
                "possible.",
        "options": [
            "Because every element's properties are simply the average "
            "of the properties of the two elements either side of it",
            "Because an element's position fixes its outer electron "
            "count and its number of shells, and these follow regular "
            "trends",
            "Because every element in a group has exactly the same "
            "properties as the others in that group",
            "Because the relative atomic mass of an element can be used "
            "to calculate all of its properties",
        ],
        "correct_index": 1,
        "why": "Position sets electronic structure and electronic structure "
               "sets chemistry, so the trends around a gap in the table "
               "predict what belongs in it.",
    },

    # ── development-periodic-table ──────────────────────────────────
    {
        "id": "ks4-development-periodic-table-e01",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the property Mendeleev used to order the elements in his "
                "1869 table.",
        "options": [
            "Atomic number",
            "Number of neutrons",
            "Relative atomic mass",
            "Melting point",
        ],
        "correct_index": 2,
        "why": "Atomic numbers were unknown in 1869, so Mendeleev ordered the "
               "elements by their relative atomic masses.",
    },
    {
        "id": "ks4-development-periodic-table-e02",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist whose X-ray work showed that elements "
                "should be ordered by atomic number.",
        "options": [
            "Henry Moseley",
            "John Newlands",
            "Dmitri Mendeleev",
            "John Dalton",
        ],
        "correct_index": 0,
        "why": "Moseley's 1913 measurements of atomic number gave the ordering "
               "that the modern table still uses.",
    },
    {
        "id": "ks4-development-periodic-table-e03",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What name did Newlands give to his pattern in which every "
                "eighth element had similar properties?",
        "options": [
            "The law of gaps",
            "The law of periods",
            "The law of atomic numbers",
            "The law of octaves",
        ],
        "correct_index": 3,
        "why": "He named it after the eight-note musical octave, because "
               "similar elements recurred at every eighth place.",
    },
    {
        "id": "ks4-development-periodic-table-e04",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one thing Mendeleev did that Newlands did not.",
        "options": [
            "He ordered the elements by their relative atomic masses",
            "He left gaps in his table for elements that had not yet "
            "been discovered",
            "He arranged the elements in order of atomic number",
            "He grouped together the elements that happened to have "
            "similar chemical properties",
        ],
        "correct_index": 1,
        "why": "Leaving gaps let Mendeleev predict undiscovered elements "
               "instead of forcing every known element into the next slot.",
    },
    {
        "id": "ks4-development-periodic-table-s01",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mendeleev sometimes placed a heavier element before a lighter "
                "one. Explain why he did this.",
        "options": [
            "He had measured those relative atomic masses wrongly and "
            "never went back to correct the order",
            "He wanted every row of his table to contain the same "
            "number of elements",
            "He believed that relative atomic mass had nothing to do "
            "with chemistry",
            "He put chemical properties first, so an element went in "
            "the group its reactions matched",
        ],
        "correct_index": 3,
        "why": "Mendeleev trusted the pattern of properties over strict mass "
               "order, and ordering by atomic number later showed those swaps "
               "had been right.",
    },
    {
        "id": "ks4-development-periodic-table-s02",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the discovery of the noble gases in the 1890s did "
                "not damage Mendeleev's table.",
        "options": [
            "The noble gases were quietly left out of the table "
            "altogether",
            "The noble gases were placed in Group 1, which had room for "
            "them",
            "They all shared very similar properties and fitted "
            "together as a new group at the edge",
            "Their relative atomic masses were so large that they came "
            "after every other element in the table",
        ],
        "correct_index": 2,
        "why": "A whole family of unreactive elements slotted in as Group 0 "
               "without disturbing anything else, which strengthened the case "
               "for the table.",
    },
    {
        "id": "ks4-development-periodic-table-s03",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon has a relative atomic mass of 40 and potassium one of "
                "39, yet argon comes first in the modern periodic table. "
                "Explain why.",
        "options": [
            "Argon was discovered first, so it keeps the earlier "
            "position",
            "The table is ordered by atomic number, and argon has 18 "
            "protons while potassium has 19",
            "The table is ordered by relative atomic mass, and argon's "
            "mass has since been re-measured as 38",
            "Argon is a gas, and gases are always placed before solids "
            "within a period",
        ],
        "correct_index": 1,
        "why": "Ordering by proton number puts argon (18) before potassium "
               "(19), which mass order on its own would get the wrong way "
               "round.",
    },
    {
        "id": "ks4-development-periodic-table-s04",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the modern periodic table has no exceptions to its "
                "group pattern, while Mendeleev's table had a few.",
        "options": [
            "The modern table is ordered by atomic number, which sets "
            "the electron arrangement",
            "The modern table contains more elements, so all the gaps "
            "have now been filled",
            "The modern table is ordered by relative atomic mass, which "
            "is measured far more accurately now",
            "The modern table places the metals and the non-metals in "
            "separate halves",
        ],
        "correct_index": 0,
        "why": "Chemistry follows the electrons and the electron count follows "
               "the proton number, so ordering by atomic number can never "
               "conflict with the groups.",
    },
    {
        "id": "ks4-development-periodic-table-h01",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that Newlands' work was worthless because "
                "it was rejected at the time.",
        "options": [
            "Unfair — spotting a repeating pattern was an important "
            "step towards Mendeleev's table",
            "Fair — an idea that is rejected contributes nothing to "
            "science",
            "Fair — his pattern was based on musical notes rather than "
            "on any evidence",
            "Unfair — his table was widely accepted at the time and was "
            "only questioned many years later",
        ],
        "correct_index": 0,
        "why": "Newlands identified the genuine periodic repetition; what he "
               "lacked were the gaps and the flexibility that made Mendeleev's "
               "version work.",
    },
    {
        "id": "ks4-development-periodic-table-h02",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why no scientist working before 1869 could have "
                "arranged the elements in order of atomic number.",
        "options": [
            "Relative atomic masses had not yet been measured "
            "accurately enough",
            "Protons had not been discovered, so there was no way to "
            "know an element's atomic number",
            "Too few elements were known for any pattern to appear",
            "The idea of grouping elements by their properties had not "
            "yet been suggested",
        ],
        "correct_index": 1,
        "why": "Atomic number is the number of protons, and subatomic "
               "particles were not known until the work of Thomson, Rutherford "
               "and Moseley decades later.",
    },
    {
        "id": "ks4-development-periodic-table-h03",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how Newlands and Mendeleev each dealt with elements "
                "that did not fit the pattern.",
        "options": [
            "Both left gaps, but Mendeleev's gaps were in better places",
            "Both simply removed the awkward elements from their tables "
            "and never mentioned them again",
            "Newlands forced every element into the next available "
            "place; Mendeleev left a gap instead",
            "Newlands left gaps for undiscovered elements, while "
            "Mendeleev did not",
        ],
        "correct_index": 2,
        "why": "Newlands' rigid every-eighth rule put unlike elements side by "
               "side, whereas Mendeleev allowed his pattern to have holes that "
               "were later filled.",
    },
    {
        "id": "ks4-development-periodic-table-h04",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the periodic table is now finished and can "
                "never change again. Evaluate this statement.",
        "options": [
            "Correct — all 118 elements are known, so nothing can "
            "change",
            "Correct — the table has not changed at all since Mendeleev "
            "published it",
            "Incorrect — the table is reordered whenever new relative "
            "atomic masses are measured more precisely",
            "Incorrect — new elements are still being made and added, "
            "and the table is a model open to revision",
        ],
        "correct_index": 3,
        "why": "Scientific models stay provisional: this one has already been "
               "reordered once by new evidence, and synthetic elements "
               "continue to extend it.",
    },

    # ── metals-non-metals ───────────────────────────────────────────
    {
        "id": "ks4-metals-non-metals-e01",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of ion a metal atom forms in a reaction.",
        "options": [
            "A negative ion, by gaining electrons",
            "A negative ion, by losing electrons",
            "No ion at all, because metals share electrons instead",
            "A positive ion, by losing electrons",
        ],
        "correct_index": 3,
        "why": "A metal has few outer electrons and loses them, leaving more "
               "protons than electrons and therefore a positive charge.",
    },
    {
        "id": "ks4-metals-non-metals-e02",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which property is typical of a non-metal in the solid state?",
        "options": [
            "Malleable — it can be hammered into a sheet",
            "Brittle — it breaks rather than bending",
            "Ductile — it can be drawn out into a wire",
            "Shiny, with a very high melting point",
        ],
        "correct_index": 1,
        "why": "Non-metal solids have no layers of ions and delocalised "
               "electrons that can slide, so they shatter instead of changing "
               "shape.",
    },
    {
        "id": "ks4-metals-non-metals-e03",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the only metal that is a liquid at room temperature.",
        "options": [
            "Bromine",
            "Sodium",
            "Mercury",
            "Lead",
        ],
        "correct_index": 2,
        "why": "Mercury is the one metal that is liquid at room temperature; "
               "bromine is a liquid too, but it is a non-metal.",
    },
    {
        "id": "ks4-metals-non-metals-e04",
        "subtopic_slug": "metals-non-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of oxide formed when a metal reacts with "
                "oxygen.",
        "options": [
            "A basic oxide, which neutralises acids",
            "An acidic oxide, which dissolves to form an acid",
            "A neutral oxide, which has no effect on an indicator",
            "No oxide at all, because metals do not react with oxygen",
        ],
        "correct_index": 0,
        "why": "Metal oxides are bases, which is why magnesium oxide and "
               "copper oxide neutralise acids to make salts.",
    },
    {
        "id": "ks4-metals-non-metals-s01",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why copper can be drawn out into long thin wires.",
        "options": [
            "Its atoms are held by weak forces that break very easily",
            "Its layers of positive ions can slide over one another "
            "while the delocalised electrons still hold the structure "
            "together",
            "Its atoms are arranged in long chain molecules that unwind "
            "and stretch when the metal is pulled through a hole",
            "Its ions repel one another, and that repulsion pulls the "
            "metal into a thin shape",
        ],
        "correct_index": 1,
        "why": "Metallic bonding does not act in fixed directions, so the "
               "layers slip without the structure breaking — that is what "
               "makes metals ductile and malleable.",
    },
    {
        "id": "ks4-metals-non-metals-s02",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium oxide is added to water and universal indicator is then "
                "added. Predict the colour of the solution.",
        "options": [
            "Purple or blue, because a metal oxide gives an alkaline "
            "solution",
            "Red, because a metal oxide gives an acidic solution",
            "Green, because metal oxides do not change the pH of water",
            "Orange, because sodium oxide behaves as a weak acid",
        ],
        "correct_index": 0,
        "why": "Sodium is a metal, so its oxide is basic and dissolves to give "
               "an alkaline solution with a high pH.",
    },
    {
        "id": "ks4-metals-non-metals-s03",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why graphite is an exception to the rule that non- "
                "metals do not conduct electricity.",
        "options": [
            "Graphite contains metal atoms as an impurity",
            "Graphite's atoms are held together by ionic bonds, so it "
            "is the ions in it that carry the charge",
            "Graphite melts at a low temperature, so its particles are "
            "free to move",
            "Each carbon atom bonds to only three others, leaving one "
            "delocalised electron free to move",
        ],
        "correct_index": 3,
        "why": "The spare electron from every carbon atom is delocalised "
               "between the layers, giving graphite the mobile charges that "
               "most non-metals lack.",
    },
    {
        "id": "ks4-metals-non-metals-s04",
        "subtopic_slug": "metals-non-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why most non-metals have low melting points.",
        "options": [
            "The covalent bonds inside their molecules are very weak",
            "Their atoms are heavy, so less energy is needed to move "
            "them",
            "They exist as small molecules, and melting only has to "
            "overcome the weak forces between them",
            "They contain delocalised electrons that carry the heat "
            "energy away as fast as it is supplied",
        ],
        "correct_index": 2,
        "why": "Melting separates whole molecules rather than breaking bonds "
               "inside them, and the forces between small molecules are weak.",
    },
    {
        "id": "ks4-metals-non-metals-h01",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Element Z conducts electricity as a solid, forms an oxide that "
                "neutralises hydrochloric acid, and can be hammered into a "
                "sheet. Deduce whether Z is a metal or a non-metal.",
        "options": [
            "A non-metal — it must be graphite, which conducts "
            "electricity",
            "A metalloid — it has one property of a metal and two "
            "properties of a non-metal",
            "A metal — conducting, a basic oxide and malleability are "
            "all typical metal properties",
            "A non-metal — only non-metal oxides react with acids",
        ],
        "correct_index": 2,
        "why": "Three metal properties together, and especially the basic "
               "oxide, identify Z as a metal.",
    },
    {
        "id": "ks4-metals-non-metals-h02",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a metal and a non-metal each achieve a full outer "
                "shell when they react together.",
        "options": [
            "Both lose electrons to their surroundings",
            "Both gain electrons from their surroundings",
            "The metal shares its outer electrons with the non-metal "
            "until both outer shells are full",
            "The metal loses its outer electrons and the non-metal "
            "gains them, forming ions",
        ],
        "correct_index": 3,
        "why": "Electrons transfer from the metal to the non-metal, so the "
               "metal empties its outer shell while the non-metal fills its "
               "own.",
    },
    {
        "id": "ks4-metals-non-metals-h03",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict how the metallic character of the elements changes "
                "going down Group 4, from carbon to lead.",
        "options": [
            "It increases — the outer electrons are further out and "
            "lost more easily, so the lower elements are metals",
            "It decreases — the extra shells make the outer electrons "
            "harder to lose",
            "It stays the same — every element in a group behaves in "
            "the same way",
            "It increases and then decreases again, because the "
            "elements in the middle of the group are metalloids",
        ],
        "correct_index": 0,
        "why": "Metallic character is about how readily electrons are lost, "
               "and extra shells weaken the nucleus's hold — so carbon is a "
               "non-metal while lead is a metal.",
    },
    {
        "id": "ks4-metals-non-metals-h04",
        "subtopic_slug": "metals-non-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'No non-metal conducts electricity, so any "
                "element that conducts must be a metal.' Evaluate this "
                "statement.",
        "options": [
            "It is correct, and it is the standard chemical test for a "
            "metal",
            "It is unreliable — graphite and graphene are non-metals "
            "that conduct, and silicon is a metalloid",
            "It is unreliable, because most metals are actually rather "
            "poor conductors of electricity",
            "It is correct, provided the element is tested as a solid",
        ],
        "correct_index": 1,
        "why": "Conduction is a useful clue but not proof: graphite conducts "
               "because of its delocalised electrons and it is a non-metal.",
    },

    # ── group-0 ─────────────────────────────────────────────────────
    {
        "id": "ks4-group-0-e01",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by describing the noble gases as "
                "monatomic.",
        "options": [
            "They exist as single, separate atoms",
            "They exist as molecules made of two atoms joined together",
            "They contain only one type of atom in their compounds",
            "They each have only one electron shell",
        ],
        "correct_index": 0,
        "why": "With a full outer shell there is nothing to gain by bonding, "
               "so noble gas atoms stay on their own rather than pairing up.",
    },
    {
        "id": "ks4-group-0-e02",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of electrons in the outer shell of a neon "
                "atom.",
        "options": [
            "2",
            "7",
            "8",
            "10",
        ],
        "correct_index": 2,
        "why": "Neon's electronic structure is 2.8, so its outer shell holds 8 "
               "electrons, which is a full shell.",
    },
    {
        "id": "ks4-group-0-e03",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these elements is a noble gas?",
        "options": [
            "Nitrogen",
            "Krypton",
            "Chlorine",
            "Hydrogen",
        ],
        "correct_index": 1,
        "why": "Krypton is in Group 0; nitrogen, chlorine and hydrogen are "
               "reactive non-metals from other groups.",
    },
    {
        "id": "ks4-group-0-e04",
        "subtopic_slug": "group-0",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the density of the noble gases changes going down "
                "Group 0.",
        "options": [
            "It decreases, because the atoms move further apart",
            "It stays the same for every noble gas",
            "It decreases, because there is more empty space inside the "
            "larger atoms",
            "It increases, because the atoms have more mass",
        ],
        "correct_index": 3,
        "why": "Each step down the group adds protons and neutrons, so the "
               "same volume of gas weighs more.",
    },
    {
        "id": "ks4-group-0-s01",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Helium has only 2 outer electrons, yet it sits in Group 0 with "
                "elements that have 8. Explain why.",
        "options": [
            "Helium is placed there only because it is a gas",
            "Helium really has 8 outer electrons, but 6 of them are "
            "hidden inside the nucleus",
            "Helium's first shell holds only 2 electrons, so 2 is a "
            "full outer shell for helium",
            "Helium is in Group 0 by mistake, and chemists have simply "
            "kept it there out of tradition",
        ],
        "correct_index": 2,
        "why": "Group 0 is defined by having a full outer shell, and for "
               "helium's single shell full means two electrons.",
    },
    {
        "id": "ks4-group-0-s02",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why helium rather than hydrogen is used to fill "
                "weather balloons.",
        "options": [
            "Helium is heavier than air, so it holds the balloon steady "
            "as it rises through the sky",
            "Helium reacts with the balloon material and strengthens it",
            "Helium is the only gas that expands as it is cooled",
            "Helium is much less dense than air and is unreactive, so "
            "it lifts the balloon and cannot burn",
        ],
        "correct_index": 3,
        "why": "Low density gives the lift and a full outer shell gives the "
               "safety — unlike hydrogen, helium cannot burn.",
    },
    {
        "id": "ks4-group-0-s03",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon is used to fill the space inside filament light bulbs. "
                "Explain why.",
        "options": [
            "It is unreactive, so it does not react with the very hot "
            "metal filament",
            "It conducts electricity well, so it helps the current to "
            "flow",
            "It reacts with oxygen and so removes the oxygen from the "
            "bulb",
            "It has a very high boiling point, so it stays liquid "
            "inside the bulb",
        ],
        "correct_index": 0,
        "why": "An inert atmosphere stops the white-hot filament reacting with "
               "oxygen and burning away.",
    },
    {
        "id": "ks4-group-0-s04",
        "subtopic_slug": "group-0",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon boils at -186 degrees C and xenon at -108 degrees C. "
                "Predict the boiling point of krypton, which lies between them "
                "in Group 0.",
        "options": [
            "-200 degrees C",
            "-153 degrees C",
            "-95 degrees C",
            "-250 degrees C",
        ],
        "correct_index": 1,
        "why": "Boiling point rises steadily down the group, so krypton must "
               "boil somewhere between -186 degrees C and -108 degrees C.",
    },
    {
        "id": "ks4-group-0-h01",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the noble gases do not exist as diatomic molecules "
                "such as Ne2, although oxygen exists as O2.",
        "options": [
            "Neon atoms are too large to bond to one another",
            "Oxygen atoms share electrons to complete their outer "
            "shells, but a neon atom's shell is already full",
            "Neon has too few electrons to be able to form a covalent "
            "bond",
            "Neon atoms repel one another because their full outer "
            "shells of electrons are all negatively charged",
        ],
        "correct_index": 1,
        "why": "A covalent bond forms because sharing completes both outer "
               "shells, and for neon there is nothing left to complete.",
    },
    {
        "id": "ks4-group-0-h02",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radon is the noble gas below xenon. Predict its boiling point "
                "and its density compared with xenon, and explain your "
                "prediction.",
        "options": [
            "Higher boiling point and greater density — larger atoms "
            "with more electrons attract each other more strongly",
            "Lower boiling point and lower density, because the outer "
            "electrons are further from the nucleus and held loosely",
            "The same boiling point and density, because all noble "
            "gases are unreactive",
            "Higher boiling point but lower density, because larger "
            "atoms take up more space",
        ],
        "correct_index": 0,
        "why": "Both trends run the same way down Group 0: more electrons "
               "means stronger forces between atoms, and more nuclear "
               "particles means greater density.",
    },
    {
        "id": "ks4-group-0-h03",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says neon is unreactive because it has no electrons "
                "in its outer shell. Explain the error.",
        "options": [
            "There is no error — an empty outer shell is the stable "
            "arrangement",
            "The error is that neon has one electron in its outer "
            "shell, not none",
            "The error is that neon is actually quite reactive, and it "
            "forms compounds readily with other elements",
            "The error is that neon's outer shell is full, with 8 "
            "electrons — a full shell, not an empty one",
        ],
        "correct_index": 3,
        "why": "Neon is 2.8: its stability comes from a complete outer shell, "
               "so it has no tendency to gain, lose or share electrons.",
    },
    {
        "id": "ks4-group-0-h04",
        "subtopic_slug": "group-0",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the way reactivity changes down Group 0 with the way "
                "it changes down Group 1.",
        "options": [
            "Both groups become more reactive going down the group, "
            "because the atoms get larger with every extra shell",
            "Group 0 becomes more reactive down the group while Group 1 "
            "becomes less reactive",
            "Group 1 reactivity rises because its outer electron is "
            "lost more easily, while Group 0 stays unreactive",
            "Neither changes, because reactivity depends only on the "
            "period an element is in",
        ],
        "correct_index": 2,
        "why": "Group 1 reactivity depends on how easily one outer electron "
               "leaves, which changes down the group, while a Group 0 atom has "
               "no electron to give or take in the first place.",
    },

    # ── group-1 ─────────────────────────────────────────────────────
    {
        "id": "ks4-group-1-e01",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge on the ion formed by a Group 1 metal.",
        "options": [
            "1-",
            "1+",
            "2+",
            "7-",
        ],
        "correct_index": 1,
        "why": "A Group 1 atom loses its single outer electron, leaving one "
               "more proton than electron and so a 1+ charge.",
    },
    {
        "id": "ks4-group-1-e02",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the Group 1 metals are stored under oil.",
        "options": [
            "To stop them reacting with the oxygen and water vapour in "
            "the air",
            "To keep them cool, because they would otherwise melt at "
            "room temperature",
            "To stop them dissolving in the carbon dioxide in the air",
            "To keep them soft enough to be cut with a knife",
        ],
        "correct_index": 0,
        "why": "They are so reactive that they tarnish in air within seconds, "
               "and a layer of oil keeps air and moisture off the surface.",
    },
    {
        "id": "ks4-group-1-e03",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one physical property that makes the Group 1 metals "
                "unusual compared with most other metals.",
        "options": [
            "They are extremely hard",
            "They have very high melting points",
            "They are soft enough to be cut with a knife",
            "They are the densest metals known",
        ],
        "correct_index": 2,
        "why": "Group 1 metals are soft, low in density and low melting, "
               "unlike the hard, dense, high-melting metals of the central "
               "block.",
    },
    {
        "id": "ks4-group-1-e04",
        "subtopic_slug": "group-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate pH of the solution left after a Group 1 "
                "metal has reacted with water.",
        "options": [
            "About 1 — strongly acidic",
            "Exactly 7 — neutral",
            "About 5 — slightly acidic",
            "About 13 — strongly alkaline",
        ],
        "correct_index": 3,
        "why": "The product is a metal hydroxide such as NaOH, a strong "
               "alkali, which is why Group 1 are called the alkali metals.",
    },
    {
        "id": "ks4-group-1-s01",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why lithium, sodium and potassium all float when they "
                "are added to water.",
        "options": [
            "The hydrogen gas produced is what lifts them to the "
            "surface",
            "They melt instantly, and a liquid always floats on water",
            "They react so fast that the reaction pushes them upwards",
            "They have a lower density than water",
        ],
        "correct_index": 3,
        "why": "Group 1 metals are unusually low in density, and lithium, "
               "sodium and potassium are all less dense than water.",
    },
    {
        "id": "ks4-group-1-s02",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which equation correctly represents the reaction of potassium "
                "with water?",
        "options": [
            "K + H2O -> KOH + H2",
            "2K + 2H2O -> 2KOH + H2",
            "2K + H2O -> K2O + H2",
            "K + 2H2O -> KOH2 + H2",
        ],
        "correct_index": 1,
        "why": "Potassium and water give a hydroxide, KOH, and hydrogen — "
               "and 2K + 2H2O -> 2KOH + H2 is the version of that reaction "
               "whose atoms balance on both sides.",
    },
    {
        "id": "ks4-group-1-s03",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what is seen when a small piece of potassium is added "
                "to water.",
        "options": [
            "It fizzes violently, melts into a ball, moves rapidly and "
            "the hydrogen burns with a lilac flame",
            "It sinks straight down to the bottom of the beaker and "
            "dissolves slowly, with no bubbles at all",
            "It fizzes gently and gradually gets smaller over several "
            "minutes",
            "It burns with a bright white flame and leaves a white ash "
            "behind",
        ],
        "correct_index": 0,
        "why": "Potassium reacts so vigorously that the energy released "
               "ignites the hydrogen, which burns with the lilac flame "
               "characteristic of potassium.",
    },
    {
        "id": "ks4-group-1-s04",
        "subtopic_slug": "group-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen if caesium were added to water, and "
                "suggest why teachers do not demonstrate it.",
        "options": [
            "It would react gently, but caesium is far too rare to use "
            "in school",
            "It would not react at all, because caesium is at the very "
            "bottom of the group and is the most stable",
            "It would react explosively, because its outer electron is "
            "furthest from the nucleus and lost most easily",
            "It would dissolve without reacting, because it is such a "
            "soft metal",
        ],
        "correct_index": 2,
        "why": "Reactivity rises down Group 1, and by caesium the reaction "
               "with water releases so much energy so quickly that it is "
               "explosive.",
    },
    {
        "id": "ks4-group-1-h01",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A Group 1 metal M is added to water and the solution turns "
                "universal indicator purple. Which equation and explanation "
                "account for this?",
        "options": [
            "2M + 2H2O -> 2MOH + H2 — the metal hydroxide formed is a "
            "strong alkali, giving a high pH",
            "M + H2O -> MO + H2 — the metal oxide formed is an acid, "
            "giving a low pH",
            "2M + O2 -> 2MO — the oxide dissolves to give a neutral "
            "solution",
            "M + 2H2O -> M(OH)2 + H2 — the hydroxide formed contains a "
            "metal ion carrying a 2+ charge",
        ],
        "correct_index": 0,
        "why": "A Group 1 metal produces a hydroxide of formula MOH, a strong "
               "alkali, which turns universal indicator purple.",
    },
    {
        "id": "ks4-group-1-h02",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rubidium lies below potassium in Group 1. Predict its melting "
                "point and its reactivity compared with potassium.",
        "options": [
            "A higher melting point and less reactive",
            "A higher melting point and more reactive",
            "A lower melting point and less reactive",
            "A lower melting point and more reactive",
        ],
        "correct_index": 3,
        "why": "Melting point falls and reactivity rises going down Group 1, "
               "so rubidium melts more easily than potassium and reacts more "
               "violently.",
    },
    {
        "id": "ks4-group-1-h03",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of atomic structure, why Group 1 metals "
                "become more reactive down the group while Group 7 non-metals "
                "become less reactive.",
        "options": [
            "The nuclear charge falls down both groups, and that "
            "affects metals and non-metals differently",
            "In both groups the outer shell is further from the "
            "nucleus, which makes an electron easier to lose but harder "
            "to attract",
            "Group 1 atoms gain shells down the group while Group 7 "
            "atoms lose them",
            "Group 1 elements gain electrons while Group 7 elements "
            "lose them, so the two trends must run in opposite "
            "directions",
        ],
        "correct_index": 1,
        "why": "One cause — a weaker pull on the outer shell as atoms get "
               "bigger — helps a metal lose an electron and hinders a non- "
               "metal from gaining one.",
    },
    {
        "id": "ks4-group-1-h04",
        "subtopic_slug": "group-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says potassium is more reactive than sodium because "
                "a potassium atom has more protons pulling on its outer "
                "electron. Explain the error.",
        "options": [
            "There is no error — more protons always means greater "
            "reactivity",
            "The error is that potassium has fewer protons than sodium",
            "The extra protons are outweighed by the extra shell: the "
            "outer electron is shielded and lost more easily",
            "The error is that reactivity depends on the number of "
            "neutrons in the nucleus, not the number of protons",
        ],
        "correct_index": 2,
        "why": "Distance and shielding win: although potassium's nuclear "
               "charge is larger, its outer electron is held far more weakly "
               "than sodium's.",
    },

    # ── group-7 ─────────────────────────────────────────────────────
    {
        "id": "ks4-group-7-e01",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of electrons in the outer shell of a halogen "
                "atom.",
        "options": [
            "1",
            "2",
            "5",
            "7",
        ],
        "correct_index": 3,
        "why": "Group 7 elements have seven outer electrons, so each needs to "
               "gain just one more to fill the shell.",
    },
    {
        "id": "ks4-group-7-e02",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the appearance of bromine at room temperature.",
        "options": [
            "A yellow-green gas",
            "A grey-black solid",
            "A red-brown liquid",
            "A colourless gas",
        ],
        "correct_index": 2,
        "why": "Melting and boiling points rise down Group 7, and bromine "
               "falls in the range that makes it a liquid at room temperature.",
    },
    {
        "id": "ks4-group-7-e03",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the formula of a chlorine molecule.",
        "options": [
            "Cl2",
            "Cl",
            "Cl3",
            "Cl-",
        ],
        "correct_index": 0,
        "why": "The halogens are diatomic: two chlorine atoms share a pair of "
               "electrons so that both reach a full outer shell.",
    },
    {
        "id": "ks4-group-7-e04",
        "subtopic_slug": "group-7",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of ion a halogen forms.",
        "options": [
            "A halide ion with a 1+ charge",
            "A halide ion with a 1- charge",
            "A halide ion with a 7- charge",
            "A halide ion with a 2- charge",
        ],
        "correct_index": 1,
        "why": "Gaining one electron to complete the outer shell leaves one "
               "more electron than proton, giving a 1- halide ion.",
    },
    {
        "id": "ks4-group-7-s01",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why iodine has a higher boiling point than chlorine.",
        "options": [
            "Iodine molecules are larger with more electrons, so the "
            "forces between the molecules are stronger",
            "Iodine has stronger covalent bonds inside each of its "
            "molecules",
            "Iodine is the more reactive of the two, so its particles "
            "are held together much more tightly",
            "Iodine has more shells, so its atoms take longer to heat "
            "up",
        ],
        "correct_index": 0,
        "why": "Boiling separates whole molecules, and the forces between "
               "molecules grow stronger as the molecules get larger down the "
               "group.",
    },
    {
        "id": "ks4-group-7-s02",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which equation correctly represents the reaction between "
                "chlorine and potassium iodide solution?",
        "options": [
            "Cl2 + KI -> KCl + I2",
            "Cl2 + 2KI -> 2KCl + I2",
            "2Cl2 + 2KI -> 2KCl + 2I2",
            "Cl + 2KI -> KCl2 + I2",
        ],
        "correct_index": 1,
        "why": "One Cl2 molecule takes the place of one I2, so two KI units "
               "are needed: Cl2 + 2KI -> 2KCl + I2.",
    },
    {
        "id": "ks4-group-7-s03",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Astatine lies below iodine in Group 7. Predict its appearance "
                "and its reactivity.",
        "options": [
            "A pale yellow gas, more reactive than fluorine",
            "A colourless liquid, about as reactive as bromine",
            "A grey-black solid, more reactive than chlorine",
            "A dark solid, and the least reactive of the halogens "
            "listed",
        ],
        "correct_index": 3,
        "why": "Down the group the halogens get darker, more likely to be "
               "solid and less reactive, and astatine is at the far end of all "
               "three trends.",
    },
    {
        "id": "ks4-group-7-s04",
        "subtopic_slug": "group-7",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bromine water is added to potassium iodide solution. Predict "
                "what is observed and explain why.",
        "options": [
            "No reaction, because bromine is less reactive than iodine",
            "A white precipitate forms as potassium bromide "
            "crystallises out of the solution",
            "The solution darkens to brown as bromine displaces iodine "
            "from the potassium iodide",
            "The bromine loses its colour and chlorine gas is given off",
        ],
        "correct_index": 2,
        "why": "Bromine is above iodine in Group 7, so it is the more reactive "
               "and takes iodine's place, releasing brown iodine into the "
               "solution.",
    },
    {
        "id": "ks4-group-7-h01",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why displacement reactions between halogens are "
                "evidence for the reactivity order of Group 7.",
        "options": [
            "Because the halogen whose solution changes colour must "
            "always be the more reactive of the two",
            "Because a halogen can only take another's place if it "
            "attracts an electron more strongly",
            "Because the halogen with the higher boiling point always "
            "displaces the others",
            "Because the halogen that stays in solution must be the "
            "more reactive one",
        ],
        "correct_index": 1,
        "why": "Displacement is a competition for an electron, so the winner "
               "is the halogen that holds an extra electron more strongly — "
               "the more reactive one.",
    },
    {
        "id": "ks4-group-7-h02",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine water is added separately to potassium chloride, "
                "potassium bromide and potassium iodide solutions. Predict in "
                "which a reaction occurs.",
        "options": [
            "In all three of them, because chlorine is a very reactive "
            "gas and displaces any halide ion",
            "In the potassium chloride only",
            "In the potassium bromide and the potassium iodide, but not "
            "in the potassium chloride",
            "In none of them, because chlorine is already a chloride",
        ],
        "correct_index": 2,
        "why": "Chlorine is more reactive than both bromine and iodine so it "
               "displaces them, but it cannot displace itself from potassium "
               "chloride.",
    },
    {
        "id": "ks4-group-7-h03",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "After a displacement reaction, cyclohexane is added and the "
                "upper layer turns violet. Deduce which halogen has been "
                "displaced.",
        "options": [
            "Chlorine",
            "Fluorine",
            "Bromine",
            "Iodine",
        ],
        "correct_index": 3,
        "why": "Iodine dissolves in a non-polar solvent such as cyclohexane to "
               "give a violet layer, whereas bromine gives an orange one.",
    },
    {
        "id": "ks4-group-7-h04",
        "subtopic_slug": "group-7",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that fluorine must be the least reactive "
                "halogen because it is the smallest atom and small atoms hold "
                "their electrons tightly. Evaluate this reasoning.",
        "options": [
            "The conclusion is wrong — a strong pull on an incoming "
            "electron makes fluorine the most reactive",
            "The reasoning is correct — the smallest atom in a group is "
            "always the least reactive",
            "The reasoning is wrong because fluorine reacts by losing "
            "electrons, and a small atom loses them easily",
            "The reasoning is correct, because reactivity in Group 7 "
            "depends only on boiling point",
        ],
        "correct_index": 0,
        "why": "Halogens react by gaining an electron, so the strong pull of a "
               "small atom's nucleus makes fluorine the most reactive halogen "
               "rather than the least.",
    },

    # ── transition-metals (TRIPLE ONLY) ─────────────────────────────
    {
        "id": "ks4-transition-metals-e01",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State where the transition metals are found in the periodic "
                "table.",
        "options": [
            "In Group 3, on the right-hand edge of the metals",
            "In the central block, between Groups 2 and 3",
            "In the two separate rows printed below the main table",
            "In Group 1, alongside the alkali metals",
        ],
        "correct_index": 1,
        "why": "The transition metals form the wide block in the middle of the "
               "table, between Group 2 and Group 3.",
    },
    {
        "id": "ks4-transition-metals-e02",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of copper(II) sulfate solution.",
        "options": [
            "Colourless",
            "Orange",
            "Pale green",
            "Blue",
        ],
        "correct_index": 3,
        "why": "Transition metal compounds are typically coloured, and "
               "copper(II) compounds in solution are blue.",
    },
    {
        "id": "ks4-transition-metals-e03",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which property is typical of a transition metal?",
        "options": [
            "A high melting point",
            "Soft enough to be cut with a knife",
            "A density lower than that of water",
            "A violent reaction with cold water",
        ],
        "correct_index": 0,
        "why": "Transition metals are hard, dense and high melting, which is "
               "the opposite of the Group 1 metals.",
    },
    {
        "id": "ks4-transition-metals-e04",
        "subtopic_slug": "transition-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the transition metal that is a liquid at room "
                "temperature.",
        "options": [
            "Copper",
            "Titanium",
            "Mercury",
            "Chromium",
        ],
        "correct_index": 2,
        "why": "Mercury is the exception among the transition metals — every "
               "other one is a solid at room temperature.",
    },
    {
        "id": "ks4-transition-metals-s01",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron forms both Fe2+ and Fe3+ ions. State which typical "
                "property of transition metals this shows.",
        "options": [
            "They have variable oxidation states",
            "They form coloured compounds",
            "They can act as catalysts",
            "They have high melting points",
        ],
        "correct_index": 0,
        "why": "Forming ions with more than one possible charge is exactly "
               "what is meant by having variable oxidation states.",
    },
    {
        "id": "ks4-transition-metals-s02",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why nickel is used in the manufacture of margarine.",
        "options": [
            "It gives the margarine its yellow colour",
            "It catalyses the hydrogenation of vegetable oils without "
            "being used up itself",
            "It hardens the margarine by reacting with the oil to form "
            "a solid compound of nickel",
            "It neutralises the acids present in the vegetable oil",
        ],
        "correct_index": 1,
        "why": "Nickel catalyses the addition of hydrogen to the vegetable "
               "oil, so the process is faster and the nickel is recovered "
               "unchanged.",
    },
    {
        "id": "ks4-transition-metals-s03",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the reaction of iron with cold water with the reaction "
                "of sodium with cold water.",
        "options": [
            "Both react vigorously, giving off hydrogen gas",
            "Iron reacts vigorously and gives off hydrogen, while "
            "sodium reacts only very slowly",
            "Iron shows no visible reaction, while sodium fizzes "
            "vigorously and releases hydrogen",
            "Neither reacts at all, because both of them are metals",
        ],
        "correct_index": 2,
        "why": "Transition metals are far less reactive than Group 1 metals: "
               "iron barely reacts with cold water, while sodium reacts at "
               "once.",
    },
    {
        "id": "ks4-transition-metals-s04",
        "subtopic_slug": "transition-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pale green solution slowly turns orange-brown when it is "
                "left standing in air. Suggest what this indicates about the "
                "metal in the compound.",
        "options": [
            "It is a Group 1 metal, whose compounds are white",
            "It is a non-metal, because only compounds of non-metals "
            "give brightly coloured solutions",
            "It is a Group 2 metal that has continued to dissolve",
            "It is a transition metal that has changed oxidation state, "
            "iron(II) to iron(III)",
        ],
        "correct_index": 3,
        "why": "A colour change like pale green to orange-brown is "
               "characteristic of a transition metal moving between oxidation "
               "states.",
    },
    {
        "id": "ks4-transition-metals-h01",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the ability to change oxidation state makes a "
                "transition metal a good catalyst.",
        "options": [
            "Changing oxidation state makes the metal dissolve, so it "
            "mixes evenly with the reactants",
            "Changing oxidation state releases heat, and the extra heat "
            "speeds the reaction up",
            "The metal accepts electrons and gives them back, offering "
            "a pathway of lower activation energy",
            "Changing oxidation state means the metal is used up only "
            "very slowly, so far less of it is needed",
        ],
        "correct_index": 2,
        "why": "A catalyst provides an alternative route with a lower "
               "activation energy, and a metal that gains and loses electrons "
               "reversibly can take part and then be restored.",
    },
    {
        "id": "ks4-transition-metals-h02",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Titanium is chosen both for aircraft parts and for artificial "
                "hip joints. Explain why.",
        "options": [
            "It is strong, has a low density for a metal, and resists "
            "corrosion",
            "It is the cheapest of all the transition metals to extract",
            "It has a very low melting point, which makes it easy to "
            "shape",
            "It reacts steadily with water, forming a protective layer "
            "of hydroxide",
        ],
        "correct_index": 0,
        "why": "Strength without excessive weight, together with corrosion "
               "resistance, is exactly the combination that both uses demand.",
    },
    {
        "id": "ks4-transition-metals-h03",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says that any coloured solution in the laboratory "
                "must contain a transition metal compound. Evaluate this "
                "statement.",
        "options": [
            "Correct — a colour in a solution can only ever come from "
            "the ion of a transition metal compound",
            "Correct, provided that the solution is not an acid",
            "Incorrect — transition metal compounds are always "
            "colourless in solution",
            "Incorrect — coloured compounds are typical of transition "
            "metals, but dyes are coloured too",
        ],
        "correct_index": 3,
        "why": "Colour is a strong clue to a transition metal ion but it is "
               "not proof, because plenty of other substances are coloured as "
               "well.",
    },
    {
        "id": "ks4-transition-metals-h04",
        "subtopic_slug": "transition-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Vanadium(V) oxide is used in the Contact process and "
                "manganese(IV) oxide speeds up the decomposition of hydrogen "
                "peroxide. Deduce what these two examples have in common.",
        "options": [
            "Both are Group 1 compounds used up as reactants",
            "Both are transition metal compounds acting as catalysts, "
            "without being used up",
            "Both are transition metals in their pure elemental form "
            "rather than as compounds",
            "Both are coloured compounds added to dye the product",
        ],
        "correct_index": 1,
        "why": "Transition metals and their compounds are widely used as "
               "catalysts, and each of these speeds a reaction up while being "
               "recovered unchanged.",
    },
]
