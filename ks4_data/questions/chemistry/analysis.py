"""Chemistry · Chemical analysis — purity, formulations, chromatography and ion tests.

Eight subtopics: the four BASE ones (purity, formulations, chromatography, gas
tests) and the four Triple-only identification ones (flame tests, hydroxide
precipitates, anion tests, instrumental methods).

The distractors come from the declared misconceptions in the brief: 'pure' in
the everyday sense against the chemical sense; a formulation confused with any
old mixture; Rf inverted so it exceeds 1; the lit/glowing splint swap; sodium
called red and lithium called yellow; iron(II) green and iron(III) brown
swapped; the halide precipitate colours shuffled; and flame emission
spectroscopy treated as merely qualitative.

⚠️ `chromatography` is a slug KS3 also uses. Everything here is KS4: Rf
arithmetic and rearrangement, mobile and stationary phase, spot count as a
purity test. Nothing describes a chromatogram that has to be looked at — every
distance is given in the words.
"""

TOPIC = "analysis"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── pure-substances ─────────────────────────────────────────────────
    {
        "id": "ks4-pure-substances-e01",
        "subtopic_slug": "pure-substances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement describes a pure substance in chemistry?",
        "options": [
            "A substance that has been filtered to remove solid particles",
            "A substance containing only one element or one compound",
            "A substance that is natural and has no artificial additives",
            "A substance that is safe for people to eat or to drink",
        ],
        "correct_index": 1,
        "why": "In chemistry a pure substance is a single element or compound "
               "with nothing else mixed in — nothing to do with being natural.",
    },
    {
        "id": "ks4-pure-substances-e02",
        "subtopic_slug": "pure-substances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the temperature while a mixture melts.",
        "options": [
            "It rises steadily, because the mixture melts over a range",
            "It stays fixed at one sharp temperature until melting finishes",
            "It falls, because melting takes energy out of the mixture",
            "It stays fixed at the melting point of the largest component",
        ],
        "correct_index": 0,
        "why": "A mixture has no single fixed melting point — the components "
               "disrupt one another, so melting is spread over a range.",
    },
    {
        "id": "ks4-pure-substances-e03",
        "subtopic_slug": "pure-substances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pure water melts at 0 °C. Predict what happens when a sample "
                "of water containing dissolved salt is cooled and then melted.",
        "options": [
            "It melts at exactly 0 °C, because water always melts at 0 °C",
            "It melts above 0 °C, at a single sharp temperature",
            "It melts below 0 °C, over a range of temperatures",
            "It does not melt at all until the salt has been removed",
        ],
        "correct_index": 2,
        "why": "An impurity lowers the melting point and spreads melting over a "
               "range, which is why salt is spread on icy roads.",
    },
    {
        "id": "ks4-pure-substances-e04",
        "subtopic_slug": "pure-substances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a pure substance in the chemical sense?",
        "options": [
            "Filtered sea water that is completely clear and colourless",
            "Stainless steel, made to a carefully controlled recipe",
            "Fresh milk from a single cow with nothing added to it",
            "Distilled water collected from a condenser",
        ],
        "correct_index": 3,
        "why": "Distilled water is only H2O molecules — one compound; the other "
               "three are mixtures however clean or natural they look.",
    },
    {
        "id": "ks4-pure-substances-s01",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liquid starts to boil at 102 °C and the temperature drifts "
                "upwards as boiling continues. Pure water boils at 100 °C. "
                "Suggest what this shows about the liquid.",
        "options": [
            "It is pure water, and the thermometer must be reading about 2 °C "
            "too high",
            "It is a different pure compound that happens to boil at exactly "
            "102 °C",
            "It is water with a solute dissolved in it, which raises the "
            "boiling point",
            "It was heated too quickly, so it boiled before it had reached "
            "100 °C",
        ],
        "correct_index": 2,
        "why": "A dissolved impurity raises the boiling point and stops it "
               "staying fixed, so the temperature climbs as boiling goes on.",
    },
    {
        "id": "ks4-pure-substances-s02",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chemist has two white solids. Sample A melts sharply at "
                "133 °C. Sample B melts from 121 °C to 130 °C. Explain what "
                "this tells the chemist about the two samples.",
        "options": [
            "Both are pure, but they are different compounds with different "
            "melting points",
            "Sample A is pure; sample B contains impurities that lower and "
            "broaden its melting",
            "Sample B is pure; a range shows the melting has finished, while "
            "one value is a rushed reading",
            "Sample A must be an element and sample B must be a compound",
        ],
        "correct_index": 1,
        "why": "A sharp fixed melting point means pure; a range that begins "
               "below the expected value means impurities are present.",
    },
    {
        "id": "ks4-pure-substances-s03",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pure aspirin melts at 135 °C. A student makes aspirin, "
                "measures a sharp melting point of 135 °C, and says this "
                "proves the sample is aspirin. Evaluate their claim.",
        "options": [
            "They are right — a sharp melting point can only be produced by "
            "aspirin itself",
            "They are wrong — melting point tells you about purity but never "
            "about identity at all",
            "They are wrong — a sharp melting point at any temperature shows "
            "that a sample is impure",
            "They are probably right, but other compounds melt at 135 °C, so "
            "a further test is needed",
        ],
        "correct_index": 3,
        "why": "A sharp melting point matching the data book is strong "
               "evidence, but it cannot on its own rule out another compound.",
    },
    {
        "id": "ks4-pure-substances-s04",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a melting point test is useful for checking the "
                "purity of a newly made medicine.",
        "options": [
            "A pure medicine melts sharply at a known temperature, so a range "
            "reveals impurity",
            "Melting the medicine destroys any impurities present, leaving "
            "only the active ingredient",
            "Impurities have higher melting points, so they stay solid and "
            "can be filtered off afterwards",
            "The mass lost on melting is equal to the mass of impurity in the "
            "sample being tested",
        ],
        "correct_index": 0,
        "why": "Impurity lowers the melting point and spreads it over a range, "
               "so a sharp melt at the data-book value is evidence of purity.",
    },
    {
        "id": "ks4-pure-substances-h01",
        "subtopic_slug": "pure-substances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compound X melts at 80 °C when pure. Four samples are tested. "
                "Determine which sample is most likely to be the purest.",
        "options": [
            "Sample A, which melts from 71 °C to 79 °C",
            "Sample B, which melts from 74 °C to 80 °C",
            "Sample C, which melts from 68 °C to 76 °C",
            "Sample D, which melts from 79 °C to 80 °C",
        ],
        "correct_index": 3,
        "why": "The purest sample melts closest to 80 °C over the narrowest "
               "range — impurity both lowers the melting point and widens it.",
    },
    {
        "id": "ks4-pure-substances-h02",
        "subtopic_slug": "pure-substances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three liquids are tested. P boils steadily at 78 °C, Q boils "
                "from 82 °C to 96 °C, and R boils steadily at 100 °C. Ethanol "
                "boils at 78 °C and water at 100 °C. Deduce which liquid is a "
                "mixture of ethanol and water.",
        "options": [
            "P, because ethanol is the more volatile component and boils first",
            "R, because water would be the major component of such a mixture",
            "Q, because a mixture boils over a range as its components leave",
            "Both P and R, since each boils at the temperature of one "
            "component",
        ],
        "correct_index": 2,
        "why": "A mixture has no fixed boiling point — the temperature climbs "
               "as the more volatile component leaves first.",
    },
    {
        "id": "ks4-pure-substances-h03",
        "subtopic_slug": "pure-substances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of purity, why spreading salt on a road "
                "stops ice forming when the air temperature is −3 °C.",
        "options": [
            "Dissolved salt makes the water impure, lowering its freezing "
            "point below 0 °C",
            "Salt reacts with the ice, and the energy released by the reaction "
            "melts it",
            "Salt raises the freezing point of water, so ice forms higher up "
            "and is easier to clear",
            "Salt is a pure substance, so it freezes sharply and stops the "
            "water freezing at all",
        ],
        "correct_index": 0,
        "why": "An impurity lowers a substance's melting and freezing point, so "
               "salty water stays liquid below 0 °C.",
    },
    {
        "id": "ks4-pure-substances-h04",
        "subtopic_slug": "pure-substances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug company rejects a batch whose melting range is "
                "129–134 °C when the pure drug melts at 136 °C. Suggest why "
                "the batch is rejected even though it is almost pure.",
        "options": [
            "A melting range always proves the wrong compound was made in the "
            "reaction",
            "The range shows impurity, and an impurity in a medicine may be "
            "toxic or weaken the dose",
            "Melting the batch at 129 °C would destroy the active ingredient "
            "before it could be used",
            "A drug that melts below its data-book value contains too much "
            "active ingredient",
        ],
        "correct_index": 1,
        "why": "Melting over a range starting below the true value shows "
               "impurity, and even traces in a medicine can be harmful.",
    },

    # ── formulations ────────────────────────────────────────────────────
    {
        "id": "ks4-formulations-e01",
        "subtopic_slug": "formulations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define a formulation.",
        "options": [
            "Any mixture of two or more substances, however it was made",
            "A pure compound that has been made in an industrial process",
            "A mixture designed with each component in a measured amount",
            "A substance whose formula has been found by experiment",
        ],
        "correct_index": 2,
        "why": "A formulation is a deliberately designed mixture in which every "
               "component is present in a chosen quantity for a reason.",
    },
    {
        "id": "ks4-formulations-e02",
        "subtopic_slug": "formulations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which component of a paint formulation provides its "
                "colour.",
        "options": [
            "The solvent, which keeps the paint liquid while it is applied",
            "The binder, which sticks the paint to the surface as it dries",
            "The additive, which stops mould growing on the dried paint",
            "The pigment, whose concentration decides the shade",
        ],
        "correct_index": 3,
        "why": "The pigment is the coloured component; binder, solvent and "
               "additives each do a different job.",
    },
    {
        "id": "ks4-formulations-e03",
        "subtopic_slug": "formulations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the role of the filler in a tablet.",
        "options": [
            "It makes the tablet the right size and mass to handle",
            "It is the drug itself, and treats the patient's condition",
            "It holds the powder together so the tablet keeps its shape",
            "It controls how quickly the tablet dissolves in the stomach",
        ],
        "correct_index": 0,
        "why": "The filler is the bulking agent; the binder holds the tablet "
               "together and the active ingredient does the treating.",
    },
    {
        "id": "ks4-formulations-e04",
        "subtopic_slug": "formulations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fertilisers are sold with an NPK ratio. State which three "
                "elements this ratio gives the proportions of.",
        "options": [
            "Nitrogen, phosphorus and krypton",
            "Nitrogen, phosphorus and potassium",
            "Nickel, phosphorus and potassium",
            "Nitrogen, potassium and calcium",
        ],
        "correct_index": 1,
        "why": "N, P and K are nitrogen, phosphorus and potassium — the three "
               "nutrients a fertiliser formulation is balanced for.",
    },
    {
        "id": "ks4-formulations-s01",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Engine coolant contains water, ethylene glycol and a "
                "corrosion inhibitor in fixed proportions. Explain why it is "
                "a formulation and not simply a mixture.",
        "options": [
            "Each component is present in a measured amount chosen to give "
            "the properties needed",
            "It contains more than one substance, and any mixture of several "
            "substances is a formulation",
            "It was made in a factory, and anything made industrially counts "
            "as a formulation",
            "The components react together, so the product is a compound "
            "rather than a mixture",
        ],
        "correct_index": 0,
        "why": "What makes a mixture a formulation is design — measured "
               "proportions chosen for a purpose, not simply having parts.",
    },
    {
        "id": "ks4-formulations-s02",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sunscreen formulation contains 6% of a UV filter. Suggest "
                "what could happen if a manufacturer doubled this to 12% "
                "without further testing.",
        "options": [
            "The sunscreen would stop working, because too much filter blocks "
            "absorption into the skin",
            "Nothing would change, because the UV filter is the only "
            "component that matters at all",
            "Protection may rise, but the higher concentration could irritate "
            "the skin",
            "The sunscreen would become a pure substance, since one component "
            "now dominates the mixture",
        ],
        "correct_index": 2,
        "why": "Every component of a formulation has an optimum proportion — "
               "more active ingredient is not automatically better.",
    },
    {
        "id": "ks4-formulations-s03",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two paints use the same pigment, but paint A contains far "
                "more solvent than paint B. Predict how the two differ in use.",
        "options": [
            "Paint A dries faster, because evaporating solvent is what dries "
            "a paint",
            "Paint A is thinner and easier to spread, but leaves a thinner "
            "coat of colour",
            "Paint A is a formulation and paint B only a mixture, because it "
            "has more components",
            "Paint A gives a deeper colour, because the solvent carries more "
            "pigment to the surface",
        ],
        "correct_index": 1,
        "why": "Solvent keeps the paint liquid and then evaporates, so more "
               "solvent means a runnier paint and less pigment left behind.",
    },
    {
        "id": "ks4-formulations-s04",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cleaning product contains a surfactant, an enzyme, water "
                "and several coloured dyes. Describe how a chemist could find "
                "out which dyes it contains.",
        "options": [
            "Measure its melting point and compare it with a data book of dye "
            "melting points",
            "Carry out a flame test on the product and match the flame colour "
            "to a known dye",
            "Boil the product and collect the first fraction, which will be "
            "the mixture of dyes",
            "Run paper chromatography and compare the spots with reference "
            "dyes",
        ],
        "correct_index": 3,
        "why": "Chromatography separates the components of a formulation so "
               "each can be matched against known reference substances.",
    },
    {
        "id": "ks4-formulations-h01",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A slow-release painkiller and an ordinary painkiller contain "
                "identical masses of the same active ingredient. Explain what "
                "must differ between the two formulations.",
        "options": [
            "The slow-release tablet contains extra active ingredient hidden "
            "inside its filler",
            "The coating differs, so the slow-release tablet dissolves "
            "gradually rather than at once",
            "The slow-release tablet uses a weaker form of the drug that acts "
            "over a longer period",
            "The binder differs, so the slow-release tablet is heavier and "
            "takes longer to swallow",
        ],
        "correct_index": 1,
        "why": "With the same dose, the difference has to be in how fast it is "
               "released, and the coating controls the release rate.",
    },
    {
        "id": "ks4-formulations-h02",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states: 'Bronze is an alloy, so it cannot be a "
                "formulation.' Evaluate this statement.",
        "options": [
            "Incorrect — bronze uses measured proportions of copper and tin "
            "chosen for its properties",
            "Correct — alloys are mixtures of metals only, and every "
            "formulation must include a solvent",
            "Correct — a formulation must be a liquid, and bronze is a solid "
            "at room temperature",
            "Incorrect — bronze is a compound of copper and tin, and all "
            "compounds count as formulations",
        ],
        "correct_index": 0,
        "why": "An alloy made to a set recipe is a designed mixture, which is "
               "exactly what a formulation is.",
    },
    {
        "id": "ks4-formulations-h03",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A petrol formulation contains hydrocarbons, an anti-knock "
                "additive and a corrosion inhibitor. A company removes the "
                "corrosion inhibitor to cut costs. Evaluate this decision.",
        "options": [
            "Sensible — the inhibitor does not burn, so it contributes "
            "nothing to the fuel at all",
            "Sensible — the anti-knock additive already protects the engine "
            "from corrosion as well",
            "Unwise — without the inhibitor the fuel would no longer ignite "
            "inside the engine",
            "Unwise — each component has a role, and engine parts would "
            "corrode more quickly",
        ],
        "correct_index": 3,
        "why": "In a formulation every component is there for a reason; "
               "removing one loses the property it was added to provide.",
    },
    {
        "id": "ks4-formulations-h04",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sports drink A contains 6 g of sugar and 0.20 g of sodium "
                "per 100 cm3. Drink B contains 12 g of sugar and 0.02 g of "
                "sodium per 100 cm3. Suggest which is better formulated for "
                "rehydrating an athlete.",
        "options": [
            "Drink B, because more sugar always means energy is delivered to "
            "the muscles faster",
            "Drink B, because a lower sodium content makes it less salty and "
            "much easier to drink",
            "Drink A, because it replaces the sodium lost in sweat at a "
            "useful concentration",
            "Neither, because a rehydration drink should contain water and "
            "nothing else added",
        ],
        "correct_index": 2,
        "why": "Sweat loses sodium as well as water, so a rehydration "
               "formulation is designed around electrolytes, not just sugar.",
    },

    # ── chromatography ──────────────────────────────────────────────────
    {
        "id": "ks4-chromatography-e01",
        "subtopic_slug": "chromatography",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In paper chromatography, which part is the stationary phase?",
        "options": [
            "The solvent, which rises up the paper by capillary action",
            "The mixture spotted onto the baseline at the start",
            "The air in the closed container above the solvent",
            "The chromatography paper, which does not move",
        ],
        "correct_index": 3,
        "why": "The stationary phase stays still — it is the paper; the solvent "
               "moving through it is the mobile phase.",
    },
    {
        "id": "ks4-chromatography-e02",
        "subtopic_slug": "chromatography",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation used to calculate an Rf value.",
        "options": [
            "Rf = distance moved by solvent front ÷ distance moved by "
            "substance",
            "Rf = distance moved by substance ÷ distance moved by solvent "
            "front",
            "Rf = distance moved by substance × distance moved by solvent "
            "front",
            "Rf = distance moved by solvent front − distance moved by "
            "substance",
        ],
        "correct_index": 1,
        "why": "Rf is the substance's distance divided by the solvent front's "
               "distance, which is why it always lies between 0 and 1.",
    },
    {
        "id": "ks4-chromatography-e03",
        "subtopic_slug": "chromatography",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spot travels 3.0 cm while the solvent front travels 6.0 cm. "
                "Calculate the Rf value of the spot.",
        "options": [
            "2.00",
            "3.00",
            "0.50",
            "0.05",
        ],
        "correct_index": 2,
        "why": "Rf = 3.0 ÷ 6.0 = 0.50 — the substance moved half as far as the "
               "solvent that carried it.",
    },
    {
        "id": "ks4-chromatography-e04",
        "subtopic_slug": "chromatography",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the baseline on a chromatogram is drawn in pencil.",
        "options": [
            "Pencil does not dissolve, but pen ink would run and give extra "
            "spots",
            "Pencil lines are thinner, so the spots can be positioned more "
            "accurately",
            "Pencil carries the solvent up the paper faster than ink is able "
            "to",
            "Ink would react with the paper and stop the solvent rising up it",
        ],
        "correct_index": 0,
        "why": "Pencil is insoluble graphite; pen ink is itself a mixture of "
               "dyes that would separate and confuse the chromatogram.",
    },
    {
        "id": "ks4-chromatography-s01",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pure substance is spotted onto chromatography paper and run "
                "in a solvent. Predict what is seen on the paper afterwards.",
        "options": [
            "No spots at all, because a pure substance will not dissolve in "
            "the solvent",
            "One spot, because there is only one substance to be carried up "
            "the paper",
            "Two spots, one for the element and one for the compound in the "
            "sample",
            "A continuous streak, because a pure substance travels the whole "
            "length of the paper",
        ],
        "correct_index": 1,
        "why": "Each component gives one spot, so a single spot means a single "
               "substance and multiple spots mean a mixture.",
    },
    {
        "id": "ks4-chromatography-s02",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A red dye travels 7.2 cm while the solvent front travels "
                "9.0 cm. Calculate the Rf value of the red dye.",
        "options": [
            "1.25",
            "0.72",
            "1.80",
            "0.80",
        ],
        "correct_index": 3,
        "why": "Rf = 7.2 ÷ 9.0 = 0.80; a value above 1 would mean the spot "
               "outran the solvent carrying it, which cannot happen.",
    },
    {
        "id": "ks4-chromatography-s03",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two substances are run in the same solvent. Substance A has "
                "an Rf of 0.85 and substance B an Rf of 0.20. Explain the "
                "difference between them.",
        "options": [
            "A is more soluble in the solvent and less held by the paper, so "
            "travels further",
            "A has a greater mass, so it is carried further up the paper than "
            "B is carried",
            "A is a pure substance and B is a mixture, so B is held back at "
            "the baseline instead",
            "A was spotted closer to the solvent, so it had a shorter "
            "distance to travel upwards",
        ],
        "correct_index": 0,
        "why": "How far a substance travels depends on the balance between its "
               "solubility in the mobile phase and its attraction to the paper.",
    },
    {
        "id": "ks4-chromatography-s04",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forensic scientist runs ink from a document alongside ink "
                "from four pens in the same solvent. Describe how they decide "
                "which pen wrote the document.",
        "options": [
            "The pen giving the fewest spots wrote it, because its ink is the "
            "purest of the four",
            "The pen whose spots travel furthest wrote it, because its dyes "
            "are the most soluble",
            "The pen giving spots at the same Rf values as the document ink "
            "wrote it",
            "The pen giving the darkest spots wrote it, because more ink was "
            "applied to the paper",
        ],
        "correct_index": 2,
        "why": "In the same solvent a substance always has the same Rf, so a "
               "matching set of Rf values identifies the ink.",
    },
    {
        "id": "ks4-chromatography-h01",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dye has an Rf value of 0.62 and moved 5.1 cm up the paper. "
                "Determine how far the solvent front travelled. Give your "
                "answer to 2 significant figures.",
        "options": [
            "8.2 cm",
            "3.2 cm",
            "5.7 cm",
            "0.12 cm",
        ],
        "correct_index": 0,
        "why": "Rearranging Rf = substance ÷ solvent gives solvent = 5.1 ÷ 0.62 "
               "= 8.2 cm.",
    },
    {
        "id": "ks4-chromatography-h02",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates an Rf value of 1.4. Explain what has "
                "gone wrong.",
        "options": [
            "Nothing — an Rf can exceed 1 if the substance is very soluble in "
            "the solvent used",
            "The solvent front was marked too late, after the paper had dried "
            "out completely",
            "The two distances have been divided the wrong way round — Rf "
            "cannot exceed 1",
            "The spot was placed below the solvent level, which doubles every "
            "measured distance",
        ],
        "correct_index": 2,
        "why": "A spot can never travel further than the solvent that carries "
               "it, so Rf always lies between 0 and 1.",
    },
    {
        "id": "ks4-chromatography-h03",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two different dyes both have an Rf value of 0.55 in ethanol. "
                "Suggest how a chemist could still tell them apart.",
        "options": [
            "Repeat the run in ethanol but leave the paper in the solvent for "
            "much longer",
            "Run the chromatography again in a different solvent and compare "
            "the new Rf values",
            "Use a much larger spot of each dye so any difference in Rf "
            "becomes measurable",
            "Measure to the top of each spot rather than to its centre, which "
            "separates them",
        ],
        "correct_index": 1,
        "why": "Rf depends on the solvent, so two substances that happen to "
               "match in one solvent will usually differ in another.",
    },
    {
        "id": "ks4-chromatography-h04",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In one run the solvent front travelled 8.0 cm and a spot "
                "travelled 2.4 cm. The run is repeated with the same solvent "
                "but stopped when the solvent front reaches 5.0 cm. Predict "
                "how far the same spot travels.",
        "options": [
            "2.4 cm, because a substance always travels the same distance in "
            "a given solvent",
            "0.30 cm, because the Rf value is itself the distance the spot "
            "moves up the paper",
            "3.3 cm, because the spot travels proportionally further when "
            "there is less solvent",
            "1.5 cm, because the Rf value of 0.30 is unchanged",
        ],
        "correct_index": 3,
        "why": "Rf = 2.4 ÷ 8.0 = 0.30, and Rf is fixed for a substance in a "
               "given solvent, so 0.30 × 5.0 = 1.5 cm.",
    },

    # ── testing-for-gases ───────────────────────────────────────────────
    {
        "id": "ks4-testing-for-gases-e01",
        "subtopic_slug": "testing-for-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the test for hydrogen gas and its positive result.",
        "options": [
            "A lit splint at the mouth of the tube gives a pop",
            "A glowing splint at the mouth of the tube relights",
            "Damp litmus paper held in the gas is bleached white",
            "The gas turns limewater milky when bubbled through it",
        ],
        "correct_index": 0,
        "why": "Hydrogen burns explosively with the oxygen in the air, and that "
               "rapid combustion makes the squeaky pop.",
    },
    {
        "id": "ks4-testing-for-gases-e02",
        "subtopic_slug": "testing-for-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which gas turns limewater milky?",
        "options": [
            "Hydrogen",
            "Sulfur dioxide",
            "Carbon dioxide",
            "Chlorine",
        ],
        "correct_index": 2,
        "why": "CO2 reacts with the calcium hydroxide in limewater to make "
               "insoluble calcium carbonate, which clouds the solution.",
    },
    {
        "id": "ks4-testing-for-gases-e03",
        "subtopic_slug": "testing-for-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the white solid that makes limewater turn milky.",
        "options": [
            "Calcium oxide, CaO",
            "Calcium carbonate, CaCO3",
            "Calcium hydroxide, Ca(OH)2",
            "Calcium hydrogencarbonate, Ca(HCO3)2",
        ],
        "correct_index": 1,
        "why": "CO2 + Ca(OH)2 gives CaCO3, which is insoluble and appears as a "
               "white cloudiness.",
    },
    {
        "id": "ks4-testing-for-gases-e04",
        "subtopic_slug": "testing-for-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to damp litmus paper held in chlorine gas.",
        "options": [
            "It turns blue, because chlorine is alkaline in solution",
            "It turns black, because chlorine chars the paper",
            "It stays unchanged, because chlorine is a neutral gas",
            "It is bleached white, losing its colour",
        ],
        "correct_index": 3,
        "why": "Chlorine dissolves in the water on the paper to form "
               "hypochlorous acid, which destroys the dye and bleaches it.",
    },
    {
        "id": "ks4-testing-for-gases-s01",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student holds a lit splint at the mouth of a tube of "
                "oxygen. Predict what they will observe.",
        "options": [
            "A squeaky pop, because the splint ignites the gas in the tube",
            "The splint goes out at once, because oxygen smothers a flame",
            "The splint is bleached, because oxygen removes colour from wood",
            "The splint burns more brightly, but there is no squeaky pop",
        ],
        "correct_index": 3,
        "why": "Oxygen supports combustion, so a flame burns more fiercely in "
               "it — the distinctive test uses a glowing splint, which relights.",
    },
    {
        "id": "ks4-testing-for-gases-s02",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon dioxide is bubbled through limewater until it turns "
                "milky, and bubbling then continues for several minutes. "
                "Describe what happens next.",
        "options": [
            "The cloudiness clears, as excess CO2 forms soluble "
            "hydrogencarbonate",
            "The cloudiness deepens until the tube is completely blocked with "
            "solid",
            "The limewater turns from milky to deep blue as it becomes acidic",
            "Nothing further happens, because the reaction has already "
            "finished",
        ],
        "correct_index": 0,
        "why": "Excess CO2 turns insoluble CaCO3 into soluble calcium "
               "hydrogencarbonate, so the milkiness disappears again.",
    },
    {
        "id": "ks4-testing-for-gases-s03",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A colourless gas puts out a lit splint. Explain why this "
                "result alone does not prove the gas is carbon dioxide.",
        "options": [
            "Carbon dioxide would relight the splint rather than putting it "
            "straight out",
            "A lit splint is never used in gas testing, so this result means "
            "nothing at all",
            "Other gases such as nitrogen also put out a flame — limewater "
            "must confirm it",
            "Carbon dioxide is a coloured gas, so this colourless gas cannot "
            "be carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Putting out a flame only shows the gas does not support "
               "combustion; limewater is what identifies CO2 specifically.",
    },
    {
        "id": "ks4-testing-for-gases-s04",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc reacts with dilute hydrochloric acid and the gas given "
                "off is collected. Describe the test that identifies this gas "
                "and the result expected.",
        "options": [
            "Bubble it through limewater; the limewater turns milky white",
            "Hold a lit splint at the tube; a squeaky pop is heard",
            "Hold a glowing splint in the gas; the splint relights at once",
            "Hold damp litmus paper in the gas; the paper is bleached white",
        ],
        "correct_index": 1,
        "why": "A metal reacting with an acid gives hydrogen, and hydrogen is "
               "identified by a lit splint and a squeaky pop.",
    },
    {
        "id": "ks4-testing-for-gases-h01",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student tests a gas with dry litmus paper, sees no change, "
                "and concludes the gas is not chlorine. Evaluate this "
                "conclusion.",
        "options": [
            "Sound — dry litmus is the standard test, and chlorine would "
            "bleach it immediately",
            "Sound — chlorine bleaches only when the paper is dry, so the gas "
            "must be another one",
            "Unsafe — chlorine needs water to form the bleaching acid, so "
            "damp paper must be used",
            "Unsafe — chlorine turns dry litmus blue rather than bleaching "
            "it, so they misread it",
        ],
        "correct_index": 2,
        "why": "Chlorine must dissolve in water to make hypochlorous acid, so "
               "dry paper can give a false negative.",
    },
    {
        "id": "ks4-testing-for-gases-h02",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrogen peroxide decomposes to water and one other product. "
                "A glowing splint held in that product relights. Determine the "
                "balanced equation for the decomposition.",
        "options": [
            "H2O2 → H2O + H2",
            "2H2O2 → 2H2O + O2",
            "H2O2 → H2 + O2",
            "2H2O2 → H2O + 2O2",
        ],
        "correct_index": 1,
        "why": "The relighting splint identifies oxygen, and 2H2O2 → 2H2O + O2 "
               "is the balanced decomposition.",
    },
    {
        "id": "ks4-testing-for-gases-h03",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tube contains a mixture of hydrogen and carbon dioxide. "
                "Suggest why bubbling the mixture through limewater and then "
                "testing the remaining gas with a lit splint identifies both.",
        "options": [
            "The limewater removes hydrogen first, leaving carbon dioxide to "
            "give a squeaky pop",
            "The limewater converts the hydrogen into carbon dioxide, which "
            "can then be tested",
            "A lit splint burns both gases at once, so the limewater is only "
            "a safety measure",
            "Limewater turns milky with CO2 and absorbs it, so a later pop "
            "must be hydrogen",
        ],
        "correct_index": 3,
        "why": "Limewater both detects and removes the CO2, so whatever gas is "
               "left can be tested independently.",
    },
    {
        "id": "ks4-testing-for-gases-h04",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Marble chips react with dilute hydrochloric acid. Predict "
                "what happens when a lit splint is held at the mouth of the "
                "reaction tube, and explain why.",
        "options": [
            "The splint goes out, because carbon dioxide does not support "
            "combustion",
            "A squeaky pop is heard, because an acid and a solid always give "
            "hydrogen",
            "The splint burns more brightly, because oxygen is released from "
            "the carbonate",
            "The splint is bleached white, because chloride ions release "
            "chlorine gas",
        ],
        "correct_index": 0,
        "why": "An acid on a carbonate gives CO2, which extinguishes a flame; "
               "limewater would then confirm it.",
    },

    # ── flame-tests ─────────────────────────────────────────────────────
    {
        "id": "ks4-flame-tests-e01",
        "subtopic_slug": "flame-tests",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the flame colour produced by lithium ions.",
        "options": [
            "Pale lilac",
            "Crimson red",
            "Apple green",
            "Bright yellow",
        ],
        "correct_index": 1,
        "why": "Lithium gives a crimson-red flame; potassium is lilac, copper "
               "green and sodium yellow.",
    },
    {
        "id": "ks4-flame-tests-e02",
        "subtopic_slug": "flame-tests",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which metal ion produces a green flame colour?",
        "options": [
            "Calcium, Ca2+",
            "Potassium, K+",
            "Lithium, Li+",
            "Copper(II), Cu2+",
        ],
        "correct_index": 3,
        "why": "Copper(II) ions burn with a green or blue-green flame.",
    },
    {
        "id": "ks4-flame-tests-e03",
        "subtopic_slug": "flame-tests",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the flame colour produced by potassium ions.",
        "options": [
            "Lilac",
            "Orange-red",
            "Crimson",
            "Blue-green",
        ],
        "correct_index": 0,
        "why": "Potassium gives a lilac flame — easily lost if any sodium is "
               "present in the sample.",
    },
    {
        "id": "ks4-flame-tests-e04",
        "subtopic_slug": "flame-tests",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how the nichrome wire is prepared before a flame "
                "test is carried out.",
        "options": [
            "It is heated in a yellow Bunsen flame until it glows red hot",
            "It is rinsed in distilled water and then dried on a paper towel",
            "It is dipped in hydrochloric acid and heated until colourless",
            "It is coated in the sample and heated at once, with no cleaning",
        ],
        "correct_index": 2,
        "why": "Cleaning with acid and burning off until the flame is "
               "colourless removes ions left from a previous test.",
    },
    {
        "id": "ks4-flame-tests-s01",
        "subtopic_slug": "flame-tests",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a blue Bunsen flame is used for a flame test "
                "rather than a yellow one.",
        "options": [
            "A blue flame is cooler, so the sample is not destroyed before "
            "the colour appears",
            "A blue flame contains more oxygen, which reacts with the metal "
            "to make the colour",
            "A blue flame produces less soot, which would otherwise stick to "
            "the nichrome wire",
            "A yellow flame has a colour of its own that would hide the "
            "sample's colour",
        ],
        "correct_index": 3,
        "why": "The luminous yellow flame is itself coloured, so it would mask "
               "the colour the metal ion produces.",
    },
    {
        "id": "ks4-flame-tests-s02",
        "subtopic_slug": "flame-tests",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solid gives an orange-red flame. One student says lithium "
                "and another says calcium. Explain why this disagreement can "
                "arise.",
        "options": [
            "Lithium and calcium always occur together in the same compound",
            "Lithium is crimson and calcium orange-red — the colours are "
            "close and easily confused",
            "Both metals give exactly the same flame colour, so a flame test "
            "cannot separate them",
            "Calcium gives a yellow flame that looks orange when the Bunsen "
            "flame is very hot",
        ],
        "correct_index": 1,
        "why": "Crimson and orange-red are close enough for the eye to "
               "confuse, which is one limitation of a visual flame test.",
    },
    {
        "id": "ks4-flame-tests-s03",
        "subtopic_slug": "flame-tests",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of electrons, why different metal ions give "
                "different flame colours.",
        "options": [
            "Different metals melt at different temperatures, and the colour "
            "depends on the melting point",
            "Different metals have different masses, and heavier atoms glow "
            "with redder light",
            "Electrons excited to higher levels emit light of a particular "
            "colour as they fall back",
            "Different metals burn to form oxides, and it is the oxide powder "
            "that is coloured",
        ],
        "correct_index": 2,
        "why": "Heat excites electrons to higher levels, and the light emitted "
               "as they drop back has an energy, and so a colour, unique to "
               "that metal.",
    },
    {
        "id": "ks4-flame-tests-s04",
        "subtopic_slug": "flame-tests",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student tests a solution of potassium chloride but sees a "
                "strong yellow flame. Suggest the most likely reason.",
        "options": [
            "The wire was not cleaned properly and sodium ions were left on it",
            "Potassium chloride gives a yellow flame once it is dissolved in "
            "water",
            "The chloride ion produces a yellow flame that masks the "
            "potassium colour",
            "The flame was too hot, which shifts potassium's colour from "
            "lilac to yellow",
        ],
        "correct_index": 0,
        "why": "Sodium is a very common contaminant, and even a trace gives an "
               "intense yellow that hides lilac.",
    },
    {
        "id": "ks4-flame-tests-h01",
        "subtopic_slug": "flame-tests",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A mixture is known to contain two different metal ions, but "
                "a flame test gives only a yellow colour. Evaluate what can "
                "be concluded from this result.",
        "options": [
            "Only sodium is present, because a flame test detects every ion "
            "in a mixture",
            "The two ions have reacted together, so neither of them can now "
            "be detected",
            "Sodium is present, but a second ion could be hidden by the "
            "intense yellow",
            "Neither ion is a metal, since a mixture of metals would give two "
            "separate colours",
        ],
        "correct_index": 2,
        "why": "A flame test shows only the dominant colour, so a strong "
               "sodium yellow can conceal another ion entirely.",
    },
    {
        "id": "ks4-flame-tests-h02",
        "subtopic_slug": "flame-tests",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why flame emission spectroscopy could identify both "
                "ions in that mixture when the visual flame test could not.",
        "options": [
            "It separates the emitted light by wavelength, so each element's "
            "lines show",
            "It uses a much hotter flame, which forces the weaker ion to emit "
            "a brighter colour",
            "It removes all the sodium from the sample before the measurement "
            "is taken at all",
            "It measures the mass of each ion present rather than the light "
            "that it emits",
        ],
        "correct_index": 0,
        "why": "A spectrometer resolves emitted light into separate "
               "wavelengths, so one element's lines cannot hide another's.",
    },
    {
        "id": "ks4-flame-tests-h03",
        "subtopic_slug": "flame-tests",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student concludes that a compound contains no metal ion "
                "because its flame test gave no colour. Evaluate this "
                "conclusion.",
        "options": [
            "Sound — every metal ion produces a visible colour in a hot "
            "Bunsen flame",
            "Sound — a colourless flame proves that the compound must be "
            "covalent",
            "Unsound — the flame colour appears only when the sample is "
            "completely dry",
            "Unsound — flame tests detect only a few metal ions; others give "
            "no colour",
        ],
        "correct_index": 3,
        "why": "Only certain cations give a flame colour, so a negative result "
               "cannot rule out every metal ion.",
    },
    {
        "id": "ks4-flame-tests-h04",
        "subtopic_slug": "flame-tests",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A sample gives a lilac flame. Predict what would be seen if "
                "a small amount of sodium chloride were added to the sample "
                "and the flame test repeated.",
        "options": [
            "A brighter lilac, because two ionic compounds together emit far "
            "more light",
            "A yellow flame, because sodium's emission masks the lilac",
            "A green flame, because the two colours mix together to give a "
            "third colour",
            "No colour at all, because sodium and potassium cancel each other "
            "out entirely",
        ],
        "correct_index": 1,
        "why": "Sodium emits so strongly at its yellow wavelength that even a "
               "trace overwhelms potassium's lilac.",
    },

    # ── metal-hydroxides ────────────────────────────────────────────────
    {
        "id": "ks4-metal-hydroxides-e01",
        "subtopic_slug": "metal-hydroxides",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of the precipitate formed when sodium "
                "hydroxide solution is added to copper(II) sulfate solution.",
        "options": [
            "Green",
            "Brown",
            "Blue",
            "White",
        ],
        "correct_index": 2,
        "why": "Copper(II) ions form copper(II) hydroxide, Cu(OH)2, which is a "
               "blue precipitate.",
    },
    {
        "id": "ks4-metal-hydroxides-e02",
        "subtopic_slug": "metal-hydroxides",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of the precipitate formed by iron(II) ions "
                "with sodium hydroxide solution.",
        "options": [
            "Green",
            "Brown",
            "Blue",
            "White",
        ],
        "correct_index": 0,
        "why": "Fe2+ gives green Fe(OH)2; it is Fe3+ that gives the brown "
               "precipitate.",
    },
    {
        "id": "ks4-metal-hydroxides-e03",
        "subtopic_slug": "metal-hydroxides",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which ion gives no precipitate with sodium hydroxide "
                "solution, but releases a gas when the mixture is warmed?",
        "options": [
            "Magnesium, Mg2+",
            "Aluminium, Al3+",
            "Iron(III), Fe3+",
            "Ammonium, NH4+",
        ],
        "correct_index": 3,
        "why": "NH4+ is not a metal ion and forms no hydroxide — warming with "
               "NaOH drives off ammonia gas instead.",
    },
    {
        "id": "ks4-metal-hydroxides-e04",
        "subtopic_slug": "metal-hydroxides",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the gas given off when an ammonium salt is warmed with "
                "sodium hydroxide solution.",
        "options": [
            "Hydrogen",
            "Ammonia",
            "Carbon dioxide",
            "Chlorine",
        ],
        "correct_index": 1,
        "why": "Sodium hydroxide displaces ammonia from the ammonium ion, and "
               "the ammonia turns damp red litmus blue.",
    },
    {
        "id": "ks4-metal-hydroxides-s01",
        "subtopic_slug": "metal-hydroxides",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the test that confirms the gas given off when an "
                "ammonium compound is warmed with sodium hydroxide.",
        "options": [
            "Hold a lit splint in the gas; a squeaky pop is heard",
            "Hold damp red litmus paper in the gas; it turns blue",
            "Bubble the gas through limewater; the limewater turns milky",
            "Hold damp blue litmus paper in the gas; it is bleached white",
        ],
        "correct_index": 1,
        "why": "Ammonia is alkaline in solution, so it turns damp red litmus "
               "paper blue.",
    },
    {
        "id": "ks4-metal-hydroxides-s02",
        "subtopic_slug": "metal-hydroxides",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solution gives a white precipitate with a few drops of "
                "sodium hydroxide. Describe how to find out whether the ion "
                "present is aluminium or magnesium.",
        "options": [
            "Warm the mixture and test the gas released with damp red litmus "
            "paper held above it",
            "Add dilute hydrochloric acid and see whether the precipitate "
            "fizzes as it dissolves",
            "Add excess sodium hydroxide; the aluminium precipitate "
            "dissolves and magnesium does not",
            "Carry out a flame test; aluminium gives a white flame and "
            "magnesium a bright red one",
        ],
        "correct_index": 2,
        "why": "Al(OH)3 is amphoteric and redissolves in excess alkali, while "
               "Mg(OH)2 stays as a solid.",
    },
    {
        "id": "ks4-metal-hydroxides-s03",
        "subtopic_slug": "metal-hydroxides",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Write the ionic equation for the precipitate formed when "
                "sodium hydroxide is added to a solution containing Fe3+ ions.",
        "options": [
            "Fe3+ + 3OH- → Fe(OH)3",
            "Fe3+ + 2OH- → Fe(OH)2",
            "Fe2+ + 3OH- → Fe(OH)3",
            "Fe3+ + OH- → FeOH",
        ],
        "correct_index": 0,
        "why": "The 3+ charge on iron(III) needs three hydroxide ions to "
               "balance it, giving Fe(OH)3.",
    },
    {
        "id": "ks4-metal-hydroxides-s04",
        "subtopic_slug": "metal-hydroxides",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solution gives a green precipitate with sodium hydroxide. "
                "Identify the metal ion and the formula of the precipitate.",
        "options": [
            "Copper(II), Cu(OH)2",
            "Iron(III), Fe(OH)3",
            "Calcium, Ca(OH)2",
            "Iron(II), Fe(OH)2",
        ],
        "correct_index": 3,
        "why": "Green is the colour of iron(II) hydroxide, Fe(OH)2.",
    },
    {
        "id": "ks4-metal-hydroxides-h01",
        "subtopic_slug": "metal-hydroxides",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solution gives a white precipitate with sodium hydroxide "
                "that does not dissolve in excess. A flame test on the same "
                "solution gives an orange-red colour. Deduce the metal ion.",
        "options": [
            "Aluminium, Al3+",
            "Magnesium, Mg2+",
            "Sodium, Na+",
            "Calcium, Ca2+",
        ],
        "correct_index": 3,
        "why": "A white precipitate that survives excess alkali rules out "
               "aluminium, and the orange-red flame identifies calcium.",
    },
    {
        "id": "ks4-metal-hydroxides-h02",
        "subtopic_slug": "metal-hydroxides",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why aluminium hydroxide dissolves in excess sodium "
                "hydroxide but calcium hydroxide does not.",
        "options": [
            "Aluminium hydroxide is soluble in water, so any extra solvent "
            "will dissolve it",
            "Aluminium hydroxide is amphoteric, reacting with excess "
            "hydroxide to form aluminate",
            "Aluminium has a 3+ charge, and every hydroxide of a 3+ ion "
            "dissolves in excess alkali",
            "Calcium hydroxide is a stronger alkali, so it cannot react with "
            "any more alkali",
        ],
        "correct_index": 1,
        "why": "Al(OH)3 is amphoteric — it reacts with alkali as well as acid, "
               "forming the soluble aluminate ion Al(OH)4-.",
    },
    {
        "id": "ks4-metal-hydroxides-h03",
        "subtopic_slug": "metal-hydroxides",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solution gives a green precipitate with sodium hydroxide. "
                "Left standing in air, the surface of the precipitate turns "
                "brown. Explain this observation.",
        "options": [
            "Iron(II) hydroxide is oxidised by the air to iron(III) "
            "hydroxide, which is brown",
            "The green precipitate dries out, and a dried precipitate is "
            "always brown",
            "Excess sodium hydroxide slowly converts the precipitate into a "
            "brown aluminate",
            "The precipitate reacts with carbon dioxide in the air to form "
            "brown iron carbonate",
        ],
        "correct_index": 0,
        "why": "Oxygen in the air oxidises Fe2+ to Fe3+, and iron(III) "
               "hydroxide is the brown precipitate.",
    },
    {
        "id": "ks4-metal-hydroxides-h04",
        "subtopic_slug": "metal-hydroxides",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student records 'white precipitate, dissolves in excess "
                "NaOH' and concludes the solution contained magnesium ions. "
                "Identify the error and state the correct conclusion.",
        "options": [
            "No error — magnesium hydroxide does dissolve in excess alkali",
            "The error is the excess: magnesium hydroxide dissolves only in "
            "excess acid, so it is calcium",
            "Magnesium hydroxide does not dissolve in excess — dissolving "
            "shows the ion is aluminium",
            "The white precipitate shows sodium, since sodium hydroxide is "
            "itself a white solid",
        ],
        "correct_index": 2,
        "why": "Only Al(OH)3 redissolves in excess NaOH; Mg(OH)2 and Ca(OH)2 "
               "stay put.",
    },

    # ── carbonates-halides-sulfates ─────────────────────────────────────
    {
        "id": "ks4-carbonates-halides-sulfates-e01",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of the precipitate formed when silver "
                "nitrate is added to an acidified solution of a bromide.",
        "options": [
            "White",
            "Yellow",
            "Green",
            "Cream",
        ],
        "correct_index": 3,
        "why": "Silver bromide is cream — chloride gives white and iodide "
               "gives yellow.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-e02",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which reagent is added, after acidifying with dilute "
                "hydrochloric acid, to test for sulfate ions?",
        "options": [
            "Silver nitrate solution",
            "Sodium hydroxide solution",
            "Barium chloride solution",
            "Limewater",
        ],
        "correct_index": 2,
        "why": "Barium ions and sulfate ions form insoluble barium sulfate, "
               "seen as a white precipitate.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-e03",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the gas given off when dilute acid is added to a "
                "carbonate.",
        "options": [
            "Hydrogen",
            "Carbon dioxide",
            "Sulfur dioxide",
            "Chlorine",
        ],
        "correct_index": 1,
        "why": "Acid on a carbonate releases CO2, which is then confirmed by "
               "turning limewater milky.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-e04",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of the precipitate formed by iodide ions "
                "with acidified silver nitrate solution.",
        "options": [
            "Yellow",
            "Cream",
            "White",
            "Blue",
        ],
        "correct_index": 0,
        "why": "Silver iodide is yellow; the colours deepen from white "
               "(chloride) through cream (bromide) to yellow (iodide).",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-s01",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe fully how to show that an unknown white solid is a "
                "carbonate.",
        "options": [
            "Add barium chloride solution; a white precipitate confirms "
            "carbonate",
            "Add silver nitrate solution; a white precipitate confirms "
            "carbonate",
            "Add dilute acid and bubble the gas through limewater, which "
            "turns milky",
            "Add sodium hydroxide and warm; a gas turns damp red litmus paper "
            "blue",
        ],
        "correct_index": 2,
        "why": "Fizzing alone is not enough — the gas must be shown to be CO2 "
               "by turning limewater milky.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-s02",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why dilute hydrochloric acid, and not dilute sulfuric "
                "acid, is used to acidify a solution before testing for "
                "sulfate ions.",
        "options": [
            "Sulfuric acid adds sulfate ions, giving a white precipitate "
            "whatever the sample held",
            "Sulfuric acid is too concentrated and would dissolve the barium "
            "sulfate as it formed",
            "Hydrochloric acid reacts with barium chloride and makes the "
            "reagent work much faster",
            "Sulfuric acid would react with the barium chloride and release "
            "chlorine gas",
        ],
        "correct_index": 0,
        "why": "Adding sulfate ions in the acid would guarantee a positive "
               "result, so the test would prove nothing.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-s03",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solution gives a white precipitate with acidified silver "
                "nitrate, and a separate sample gives a white precipitate "
                "with acidified barium chloride. Deduce which ions are "
                "present.",
        "options": [
            "Chloride only, since silver chloride and barium chloride are "
            "both white solids",
            "Sulfate only, since both of the white precipitates must be "
            "barium sulfate",
            "Carbonate only, since carbonates give a white precipitate with "
            "every reagent",
            "Chloride and sulfate, since each test has given its own positive "
            "result",
        ],
        "correct_index": 3,
        "why": "The two tests are independent: acidified AgNO3 white means "
               "chloride, acidified BaCl2 white means sulfate.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-s04",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student adds barium chloride to a solution without "
                "acidifying it first, sees a white precipitate, and concludes "
                "sulfate is present. Suggest why this conclusion may be wrong.",
        "options": [
            "Barium chloride is itself white and may simply have precipitated "
            "out of the solution",
            "Carbonate ions also form a white precipitate with barium, so the "
            "result is not specific",
            "Without acid the barium sulfate stays dissolved, so the "
            "precipitate must be something else",
            "Chloride ions from the barium chloride form white silver "
            "chloride within the solution",
        ],
        "correct_index": 1,
        "why": "Barium carbonate is white too, so unless carbonate has first "
               "been removed by acid a white precipitate does not prove "
               "sulfate.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-h01",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solid gives a lilac flame, fizzes with dilute acid, and "
                "the gas produced turns limewater milky. Deduce the compound.",
        "options": [
            "Potassium carbonate",
            "Potassium sulfate",
            "Sodium carbonate",
            "Calcium carbonate",
        ],
        "correct_index": 0,
        "why": "The lilac flame identifies potassium and the CO2 released by "
               "acid identifies the carbonate ion.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-h02",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student acidifies a sample with dilute hydrochloric acid "
                "instead of dilute nitric acid before adding silver nitrate. "
                "Predict the result and explain it.",
        "options": [
            "No precipitate forms at all, because hydrochloric acid destroys "
            "the silver nitrate",
            "A white precipitate forms even with no halide present, because "
            "the acid supplies chloride",
            "A cream precipitate forms, because hydrochloric acid converts "
            "chloride ions into bromide",
            "The test works as normal, because the acid chosen makes no "
            "difference to the result",
        ],
        "correct_index": 1,
        "why": "HCl adds chloride ions of its own, so silver chloride would "
               "precipitate whatever the sample contained.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-h03",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pale green solution gives a white precipitate with "
                "acidified silver nitrate, and a green precipitate with "
                "sodium hydroxide. Deduce the compound and give its formula.",
        "options": [
            "Iron(III) chloride, FeCl3",
            "Iron(II) sulfate, FeSO4",
            "Iron(II) chloride, FeCl2",
            "Copper(II) chloride, CuCl2",
        ],
        "correct_index": 2,
        "why": "The green hydroxide precipitate shows Fe2+ and the white "
               "silver precipitate shows Cl-, so the salt is FeCl2.",
    },
    {
        "id": "ks4-carbonates-halides-sulfates-h04",
        "subtopic_slug": "carbonates-halides-sulfates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two students test the same solution. Student A adds silver "
                "nitrate straight away and gets a white precipitate. Student "
                "B acidifies with nitric acid first and gets none. Explain "
                "the difference.",
        "options": [
            "Student B used too much acid, which dissolved the silver nitrate "
            "before it could react",
            "Student A's sample was more concentrated, so only that sample "
            "gave enough precipitate",
            "Student B destroyed the chloride ions with the acid, so no "
            "halide could then be detected",
            "The solution held carbonate, not chloride — the acid removed it, "
            "so no precipitate formed",
        ],
        "correct_index": 3,
        "why": "Silver carbonate is also a white precipitate, which is exactly "
               "why the acidification step comes first.",
    },

    # ── instrumental-methods ────────────────────────────────────────────
    {
        "id": "ks4-instrumental-methods-e01",
        "subtopic_slug": "instrumental-methods",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one advantage of instrumental analysis over a chemical "
                "test carried out by hand.",
        "options": [
            "It costs less to buy and needs no training at all to operate",
            "It is more sensitive and detects very small amounts of a "
            "substance",
            "It works without any sample, so nothing at all is used up",
            "It gives a result that never has to be compared with reference "
            "data",
        ],
        "correct_index": 1,
        "why": "Instruments detect far smaller quantities than a colour change "
               "the human eye can see.",
    },
    {
        "id": "ks4-instrumental-methods-e02",
        "subtopic_slug": "instrumental-methods",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one disadvantage of instrumental methods of analysis.",
        "options": [
            "They can only ever detect metals, and never non-metal ions",
            "They give results that depend on the operator's colour vision",
            "The equipment is expensive and needs trained operators",
            "They destroy the whole sample, so no repeat can be made",
        ],
        "correct_index": 2,
        "why": "The main costs of instrumental analysis are the equipment "
               "itself and the expertise needed to run and calibrate it.",
    },
    {
        "id": "ks4-instrumental-methods-e03",
        "subtopic_slug": "instrumental-methods",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In flame emission spectroscopy, what is passed through a "
                "prism or diffraction grating?",
        "options": [
            "The sample solution, just before it enters the flame",
            "The flame gases, once the sample has burned away",
            "An electric current, to excite the electrons in the sample",
            "The light emitted by the sample in the flame",
        ],
        "correct_index": 3,
        "why": "Splitting the emitted light by wavelength is what turns a "
               "colour into a spectrum of identifiable lines.",
    },
    {
        "id": "ks4-instrumental-methods-e04",
        "subtopic_slug": "instrumental-methods",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the position of a line in an emission spectrum "
                "tells a chemist.",
        "options": [
            "Which element is present, since each emits at characteristic "
            "wavelengths",
            "How much of the element is present, since position rises with "
            "concentration",
            "The temperature of the flame that was used to produce the "
            "spectrum",
            "Whether the compound in the sample is ionic or covalent",
        ],
        "correct_index": 0,
        "why": "Wavelength identifies the element; it is the intensity of the "
               "line that says how much is there.",
    },
    {
        "id": "ks4-instrumental-methods-s01",
        "subtopic_slug": "instrumental-methods",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why flame emission spectroscopy is described as an "
                "objective method while a visual flame test is not.",
        "options": [
            "A detector measures the wavelength as a number, rather than a "
            "person judging a colour",
            "The instrument uses a hotter flame, so the colours produced are "
            "always exactly the same",
            "The instrument tests many samples at once, so any errors average "
            "themselves out",
            "The instrument works in the dark, where a colour cannot be "
            "misread by the eye",
        ],
        "correct_index": 0,
        "why": "Replacing the human eye with a measured wavelength takes the "
               "judgement, and the disagreement, out of the result.",
    },
    {
        "id": "ks4-instrumental-methods-s02",
        "subtopic_slug": "instrumental-methods",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A water sample is analysed by flame emission spectroscopy "
                "and a line is recorded at 766 nm. Identify the element "
                "present.",
        "options": [
            "Sodium",
            "Lithium",
            "Calcium",
            "Potassium",
        ],
        "correct_index": 3,
        "why": "766 nm is potassium's characteristic emission wavelength; "
               "sodium's strong line is at 589 nm.",
    },
    {
        "id": "ks4-instrumental-methods-s03",
        "subtopic_slug": "instrumental-methods",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two water samples are analysed. Sample A gives a sodium line "
                "twice as intense as sample B's. Deduce what this shows.",
        "options": [
            "Sample A was heated to twice the temperature that sample B "
            "reached",
            "Sample A contains about twice the concentration of sodium that "
            "B contains",
            "Sample A contains sodium while sample B contains a different "
            "element",
            "Sample A contains sodium atoms with twice the mass of those in "
            "sample B",
        ],
        "correct_index": 1,
        "why": "Emission intensity is proportional to concentration, so double "
               "the intensity means roughly double the amount.",
    },
    {
        "id": "ks4-instrumental-methods-s04",
        "subtopic_slug": "instrumental-methods",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hospital measures the sodium and potassium concentrations "
                "in a patient's blood. Explain why flame emission "
                "spectroscopy is used rather than flame tests.",
        "options": [
            "Flame tests would burn away the whole blood sample before any "
            "colour appeared",
            "Flame tests cannot detect either sodium or potassium in any "
            "sample at all",
            "Flame tests show only whether an ion is present; the hospital "
            "needs an amount",
            "Flame tests take several days, while the instrument takes only a "
            "few minutes",
        ],
        "correct_index": 2,
        "why": "Clinical work needs a number, and only the instrumental method "
               "gives a quantitative concentration.",
    },
    {
        "id": "ks4-instrumental-methods-h01",
        "subtopic_slug": "instrumental-methods",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A sample contains both sodium and potassium. Explain why "
                "flame emission spectroscopy can measure both while a visual "
                "flame test cannot.",
        "options": [
            "The instrument removes the sodium first, so the potassium can "
            "then be seen clearly",
            "The instrument uses a cooler flame, in which sodium does not "
            "emit any light at all",
            "The instrument records each wavelength separately, so one "
            "element cannot hide another",
            "The instrument measures the mass of each ion instead of the "
            "light that it emits",
        ],
        "correct_index": 2,
        "why": "A spectrum separates the light by wavelength, so the sodium "
               "line and the potassium line are recorded independently.",
    },
    {
        "id": "ks4-instrumental-methods-h02",
        "subtopic_slug": "instrumental-methods",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that instrumental methods have made "
                "chemical tests such as the silver nitrate halide test "
                "completely obsolete. Evaluate this claim.",
        "options": [
            "Too strong — chemical tests are cheap, quick and portable, which "
            "instruments often are not",
            "Correct — instrumental methods do everything a chemical test "
            "does, faster and more cheaply",
            "Too strong — instrumental methods cannot detect any negative "
            "ions in a sample at all",
            "Correct — chemical tests have been banned in laboratories on "
            "safety grounds",
        ],
        "correct_index": 0,
        "why": "Instruments are more sensitive and quantitative, but a test "
               "needing no calibration and no capital cost still has its place.",
    },
    {
        "id": "ks4-instrumental-methods-h03",
        "subtopic_slug": "instrumental-methods",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A laboratory measures sodium solutions of known "
                "concentration before analysing an unknown sample. Explain "
                "why this calibration step is necessary.",
        "options": [
            "It cleans the burner of any sodium left behind by an earlier "
            "sample run",
            "It links line intensity to concentration, so an unknown reading "
            "converts",
            "It heats the instrument until the flame reaches the temperature "
            "sodium needs",
            "It proves sodium emits at 589 nm, which must be checked for each "
            "new sample",
        ],
        "correct_index": 1,
        "why": "Intensity is only proportional to concentration — the known "
               "solutions supply the scale that turns intensity into a value.",
    },
    {
        "id": "ks4-instrumental-methods-h04",
        "subtopic_slug": "instrumental-methods",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A river is suspected of metal pollution at a level of a few "
                "parts per million. Suggest why a visual flame test would be "
                "unsuitable for measuring this.",
        "options": [
            "A flame test would react with the water and destroy the "
            "pollutant before testing",
            "A flame test works only on solids, and the river sample is a "
            "solution",
            "A flame test gives a reading in parts per billion, which is far "
            "too precise",
            "A flame test is not sensitive enough to give a colour at such a "
            "low concentration",
        ],
        "correct_index": 3,
        "why": "Trace levels produce no visible colour, which is exactly where "
               "instrumental sensitivity is needed.",
    },
]
