"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`atom-economy`.

AQA 4.3.3.2, Chemistry only. The calculation is taken across a wide spread of
real industrial equations — the blast furnace, aluminium electrolysis,
fermentation and dehydration of ethanol, the chlor-alkali process, cracking,
roasting a sulfide ore, carbonate decompositions — so that the coefficients
matter every time. Around it sit the ideas the number depends on: that atom
economy is a property of the EQUATION, that a single-product reaction is 100%,
that the waste share is whatever is left, and that a by-product counted as
wanted changes the answer. Harder rows combine an atom economy with a
percentage yield and test the two errors that the estate sees: a coefficient
dropped, and a reactant's mass used in place of the products' total.

⚠️ FOUNDATION TIER, triple only. No mole appears in any stem, option or `why` —
every Mr value a row needs is written into its stem.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-atom-economy-e05",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether the atom economy of a reaction is decided by the "
                "balanced equation or by how the experiment is carried out.",
        "options": [
            "By the balanced equation, whatever happens in the laboratory",
            "By how carefully the product is filtered, dried and transferred "
            "afterwards",
            "By how much of the product a chemist manages to collect",
            "By the temperature and pressure the reaction is run at",
        ],
        "correct_index": 0,
        "why": "Atom economy compares the Mr values written in the equation, so "
               "it is fixed as soon as the equation is known.",
    },
    {
        "id": "ks4-atom-economy-e06",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Quicklime is made by CaCO3 → CaO + CO2. Mr: CaO = 56, "
                "CO2 = 44. Calculate the atom economy for calcium oxide.",
        "options": [
            "56.0%",
            "78.6%",
            "44.0%",
            "127%",
        ],
        "correct_index": 0,
        "why": "(56 ÷ (56 + 44)) × 100 = 56.0%.",
    },
    {
        "id": "ks4-atom-economy-e07",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the atom economy of a reaction that forms only one "
                "product.",
        "options": [
            "50%",
            "75%",
            "100%",
            "It cannot be worked out",
        ],
        "correct_index": 2,
        "why": "With one product, the Mr of the desired product and the total Mr "
               "of all products are the same number.",
    },
    {
        "id": "ks4-atom-economy-e08",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the reason an addition reaction has an atom economy "
                "of 100%.",
        "options": [
            "The reactants are used up completely",
            "No catalyst is needed for the change",
            "The reaction cannot be reversed again",
            "Every reactant atom ends up in the single product formed",
        ],
        "correct_index": 3,
        "why": "An addition reaction joins the reactants into one product, so "
               "no atoms are left over as waste.",
    },
    {
        "id": "ks4-atom-economy-e09",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Zinc carbonate decomposes: ZnCO3 → ZnO + CO2. Mr: ZnO = 81, "
                "CO2 = 44. Calculate the atom economy for zinc oxide.",
        "options": [
            "35.2%",
            "54.3%",
            "84.4%",
            "64.8%",
        ],
        "correct_index": 3,
        "why": "(81 ÷ (81 + 44)) × 100 = 64.8%.",
    },
    {
        "id": "ks4-atom-economy-e10",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify what goes on the bottom of the atom economy fraction.",
        "options": [
            "The total Mr of all the products in the equation",
            "The total Mr of the reactants that were used up",
            "The Mr of the waste product on its own",
            "The mass of product the chemist collected",
        ],
        "correct_index": 0,
        "why": "The denominator is the sum of the Mr values of every product, "
               "including the ones that are waste.",
    },
    {
        "id": "ks4-atom-economy-e11",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethene reacts with steam to make ethanol, and ethanol is the "
                "only product. State the atom economy of this reaction for "
                "ethanol.",
        "options": [
            "46%",
            "61%",
            "92%",
            "100%",
        ],
        "correct_index": 3,
        "why": "Nothing else is formed, so all of the product mass is the "
               "ethanol wanted.",
    },
    {
        "id": "ks4-atom-economy-e12",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one benefit to a company of using a reaction with a high "
                "atom economy.",
        "options": [
            "The reaction will run more quickly than a low-economy one would",
            "There is less waste to treat or dispose of, which costs less",
            "The product comes out of the reactor already pure and dry",
            "A smaller reactor can be used, whatever the scale of production",
        ],
        "correct_index": 1,
        "why": "A high atom economy means most of the product mass is the "
               "useful one, so less by-product has to be handled.",
    },
    {
        "id": "ks4-atom-economy-e13",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen peroxide decomposes: 2H2O2 → 2H2O + O2. Mr: "
                "H2O = 18, O2 = 32. Calculate the atom economy for oxygen.",
        "options": [
            "47.1%",
            "52.9%",
            "64.0%",
            "88.9%",
        ],
        "correct_index": 0,
        "why": "The products are 2H2O = 36 and O2 = 32, so "
               "(32 ÷ 68) × 100 = 47.1%.",
    },
    {
        "id": "ks4-atom-economy-e14",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what an atom economy of 40% tells you about the waste "
                "from a reaction.",
        "options": [
            "Waste makes up 60% of the mass of the products formed",
            "Waste makes up 40% of the mass of the products formed",
            "Waste makes up 60% of the mass of the reactants supplied to start "
            "with",
            "Waste cannot be worked out without the percentage yield as well",
        ],
        "correct_index": 0,
        "why": "The rest of the product mass is by-product, so 100 − 40 = 60% "
               "of it is waste.",
    },
    {
        "id": "ks4-atom-economy-e15",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the quantity that an atom economy does not depend on.",
        "options": [
            "The Mr of the product that is wanted",
            "The mass of product a chemist collects",
            "The balancing numbers in front of the products in the equation",
            "The formulae of the products that are made",
        ],
        "correct_index": 1,
        "why": "What is actually collected belongs to percentage yield; atom "
               "economy is read off the equation alone.",
    },
    {
        "id": "ks4-atom-economy-e16",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Lead oxide is reduced by carbon: PbO + C → Pb + CO. Mr: "
                "Pb = 207, CO = 28. Calculate the atom economy for lead.",
        "options": [
            "11.9%",
            "92.8%",
            "88.1%",
            "13.5%",
        ],
        "correct_index": 2,
        "why": "(207 ÷ (207 + 28)) × 100 = 88.1%.",
    },
    {
        "id": "ks4-atom-economy-e17",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the two things an atom economy calculation needs from a "
                "balanced equation.",
        "options": [
            "The state symbols and the reaction conditions that are used",
            "The formula of each product and its balancing number",
            "The Mr of each reactant and the temperature",
            "The mass of each reactant and each product",
        ],
        "correct_index": 1,
        "why": "The Mr of every product is worked out from its formula, and "
               "each is multiplied by the number in front of it.",
    },
    {
        "id": "ks4-atom-economy-e18",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether the atom economy of a reaction changes when the "
                "reaction is scaled up from a test tube to a factory.",
        "options": [
            "It rises, because a factory wastes less than a student does",
            "It falls, because more by-product is made on a large scale",
            "It cannot be compared between the two different scales",
            "It stays the same, because the equation has not changed",
        ],
        "correct_index": 3,
        "why": "Atom economy is a ratio of Mr values in the equation, and the "
               "equation is the same however much material is used.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-atom-economy-s05",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron is made in the blast furnace: Fe2O3 + 3CO → 2Fe + 3CO2. "
                "Ar of Fe = 56 and Mr of CO2 = 44. Calculate the atom economy "
                "for iron.",
        "options": [
            "56.0%",
            "70.0%",
            "45.9%",
            "22.9%",
        ],
        "correct_index": 2,
        "why": "The products are 2Fe = 112 and 3CO2 = 132, so "
               "(112 ÷ 244) × 100 = 45.9%.",
    },
    {
        "id": "ks4-atom-economy-s06",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethanol is made by fermentation: C6H12O6 → 2C2H5OH + 2CO2. "
                "Mr: C2H5OH = 46, CO2 = 44. Calculate the atom economy for "
                "ethanol.",
        "options": [
            "25.6%",
            "48.9%",
            "51.1%",
            "100%",
        ],
        "correct_index": 2,
        "why": "The products are 2C2H5OH = 92 and 2CO2 = 88, so "
               "(92 ÷ 180) × 100 = 51.1%.",
    },
    {
        "id": "ks4-atom-economy-s07",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Aluminium is extracted by 2Al2O3 → 4Al + 3O2. Ar of Al = 27 "
                "and Mr of O2 = 32. Calculate the atom economy for aluminium.",
        "options": [
            "26.5%",
            "45.8%",
            "52.9%",
            "84.4%",
        ],
        "correct_index": 2,
        "why": "The products are 4Al = 108 and 3O2 = 96, so "
               "(108 ÷ 204) × 100 = 52.9%.",
    },
    {
        "id": "ks4-atom-economy-s08",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how the same reaction can have a high atom economy "
                "and a low percentage yield.",
        "options": [
            "The equation makes little waste, but little product is collected",
            "The equation makes a lot of waste, but the product is pure enough",
            "The reaction is reversible, so both figures must always disagree",
            "The atom economy was worked out from the reactants by mistake, so "
            "it is too high",
        ],
        "correct_index": 0,
        "why": "Atom economy judges the equation while percentage yield judges "
               "the experiment, so an efficient equation can still be handled "
               "badly.",
    },
    {
        "id": "ks4-atom-economy-s09",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethanol is dehydrated to ethene: C2H5OH → C2H4 + H2O. Mr: "
                "C2H4 = 28, H2O = 18. Calculate the atom economy for ethene.",
        "options": [
            "60.9%",
            "39.1%",
            "64.3%",
            "100%",
        ],
        "correct_index": 0,
        "why": "(28 ÷ (28 + 18)) × 100 = 60.9%.",
    },
    {
        "id": "ks4-atom-economy-s10",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Oxygen is made by heating potassium chlorate: "
                "2KClO3 → 2KCl + 3O2. Mr: KCl = 74.5, O2 = 32. Calculate the "
                "atom economy for oxygen.",
        "options": [
            "13.1%",
            "30.1%",
            "60.8%",
            "39.2%",
        ],
        "correct_index": 3,
        "why": "The products are 2KCl = 149 and 3O2 = 96, so "
               "(96 ÷ 245) × 100 = 39.2%.",
    },
    {
        "id": "ks4-atom-economy-s11",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction has an atom economy of 85%. Determine the "
                "percentage of the product mass that is waste.",
        "options": [
            "85%",
            "1.18%",
            "15%",
            "It depends on the percentage yield of the reaction as well",
        ],
        "correct_index": 2,
        "why": "The desired product is 85% of the product mass, so the "
               "remaining 15% is by-product.",
    },
    {
        "id": "ks4-atom-economy-s12",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sodium hydroxide is made by "
                "2NaCl + 2H2O → 2NaOH + H2 + Cl2. Mr: NaOH = 40, H2 = 2, "
                "Cl2 = 71. Calculate the atom economy for sodium hydroxide.",
        "options": [
            "26.1%",
            "46.4%",
            "35.4%",
            "52.3%",
        ],
        "correct_index": 3,
        "why": "The products are 2NaOH = 80, H2 = 2 and Cl2 = 71, so "
               "(80 ÷ 153) × 100 = 52.3%.",
    },
    {
        "id": "ks4-atom-economy-s13",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a route that makes two products tends to have a "
                "higher atom economy than one that makes three.",
        "options": [
            "Fewer products means a bigger share of the mass is the one wanted",
            "Fewer products means the reaction is faster and so wastes less",
            "Fewer products means the reaction is easier to balance correctly",
            "Fewer products means the reactants are cheaper to buy in the "
            "first place",
        ],
        "correct_index": 0,
        "why": "The denominator is the total product mass, so every extra "
               "by-product takes a further slice of it away from the desired "
               "product.",
    },
    {
        "id": "ks4-atom-economy-s14",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Magnesium reacts with hydrochloric acid: "
                "Mg + 2HCl → MgCl2 + H2. Mr: MgCl2 = 95, H2 = 2. Calculate "
                "the atom economy for magnesium chloride.",
        "options": [
            "2.1%",
            "47.5%",
            "97.9%",
            "50.0%",
        ],
        "correct_index": 2,
        "why": "(95 ÷ (95 + 2)) × 100 = 97.9%.",
    },
    {
        "id": "ks4-atom-economy-s15",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Decane is cracked: C10H22 → C8H18 + C2H4. Mr: C8H18 = 114, "
                "C2H4 = 28. Determine the atom economy for octane.",
        "options": [
            "80.3%",
            "19.7%",
            "80.0%",
            "100%",
        ],
        "correct_index": 0,
        "why": "(114 ÷ (114 + 28)) × 100 = 80.3%.",
    },
    {
        "id": "ks4-atom-economy-s16",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction's desired product has an Mr of 60 and the reaction "
                "has an atom economy of 40%. Determine the total Mr of all "
                "the products.",
        "options": [
            "24",
            "100",
            "24 000",
            "150",
        ],
        "correct_index": 3,
        "why": "60 is 40% of the total, so the total is "
               "60 × 100 ÷ 40 = 150.",
    },
    {
        "id": "ks4-atom-economy-s17",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why atom economy is worked out from the products "
                "rather than from the reactants.",
        "options": [
            "The reactants have no Mr values",
            "The reactants are never all used up",
            "Reactant formulae are harder to find",
            "The products are what the mass is divided into, useful and waste",
        ],
        "correct_index": 3,
        "why": "Every atom supplied ends up in some product, so the split "
               "between the products is exactly the split between useful "
               "material and waste.",
    },
    {
        "id": "ks4-atom-economy-s18",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Zinc sulfide is roasted: 2ZnS + 3O2 → 2ZnO + 2SO2. Mr: "
                "ZnO = 81, SO2 = 64. Calculate the atom economy for zinc "
                "oxide.",
        "options": [
            "44.1%",
            "55.9%",
            "27.9%",
            "35.4%",
        ],
        "correct_index": 1,
        "why": "The products are 2ZnO = 162 and 2SO2 = 128, so "
               "(162 ÷ 290) × 100 = 55.9%.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-atom-economy-h05",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron is reduced from magnetite: Fe3O4 + 4CO → 3Fe + 4CO2. Ar "
                "of Fe = 56 and Mr of CO2 = 44. Calculate the atom economy "
                "for iron.",
        "options": [
            "24.4%",
            "48.8%",
            "56.0%",
            "72.4%",
        ],
        "correct_index": 1,
        "why": "The products are 3Fe = 168 and 4CO2 = 176, so "
               "(168 ÷ 344) × 100 = 48.8%.",
    },
    {
        "id": "ks4-atom-economy-h06",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student works out the atom economy for iron in "
                "Fe2O3 + 3CO → 2Fe + 3CO2 as (56 ÷ (56 + 44)) × 100 = 56%. "
                "Identify the error and give the correct value.",
        "options": [
            "The Mr of Fe2O3 should have been used; it is 54.8%",
            "The reactants were used instead of the products; it is 65.6%",
            "The coefficients were left out; it is 112 ÷ 244, or 45.9%",
            "Carbon monoxide should be counted as a product; it is 38.7%",
        ],
        "correct_index": 2,
        "why": "The equation makes two iron atoms and three CO2 molecules, so "
               "both products must be multiplied by their coefficients.",
    },
    {
        "id": "ks4-atom-economy-h07",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Chlorine can be made by 2NaCl + 2H2O → 2NaOH + H2 + Cl2 "
                "(Mr: NaOH = 40, H2 = 2, Cl2 = 71) or by "
                "4HCl + O2 → 2Cl2 + 2H2O (Mr: Cl2 = 71, H2O = 18). Determine "
                "which route has the higher atom economy for chlorine.",
        "options": [
            "The first route, at 46.4% against 20.2%",
            "The second route, at 79.8% against 46.4%",
            "The first route, at 52.3% against 39.9%",
            "They are equal, because both routes make one Cl2 per NaCl",
        ],
        "correct_index": 1,
        "why": "The first gives 71 ÷ 153 = 46.4% while the second gives "
               "142 ÷ 178 = 79.8%.",
    },
    {
        "id": "ks4-atom-economy-h08",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why adding a catalyst leaves the atom economy of a "
                "reaction unchanged.",
        "options": [
            "A catalyst is used up, so it cancels out of the calculation",
            "A catalyst raises the yield rather than the atom economy",
            "A catalyst is not one of the products, so the fraction is the same",
            "A catalyst lowers the energy needed rather than the mass of waste",
        ],
        "correct_index": 2,
        "why": "Atom economy is the ratio of Mr values among the products, and "
               "a catalyst appears on neither side of the balanced equation.",
    },
    {
        "id": "ks4-atom-economy-h09",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction has an atom economy of 45% and a percentage yield "
                "of 90%. Determine the mass of desired product obtained from "
                "200 g of reactants.",
        "options": [
            "90 g",
            "180 g",
            "81 g",
            "50 g",
        ],
        "correct_index": 2,
        "why": "200 g of reactants gives 200 g of products, of which 45% is "
               "the desired product (90 g), and 90% of that is collected: "
               "81 g.",
    },
    {
        "id": "ks4-atom-economy-h10",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sodium hydrogencarbonate decomposes: "
                "2NaHCO3 → Na2CO3 + H2O + CO2. Mr: Na2CO3 = 106, H2O = 18, "
                "CO2 = 44. Calculate the atom economy for sodium carbonate.",
        "options": [
            "36.9%",
            "63.1%",
            "70.7%",
            "82.8%",
        ],
        "correct_index": 1,
        "why": "The products total 106 + 18 + 44 = 168, so "
               "(106 ÷ 168) × 100 = 63.1%.",
    },
    {
        "id": "ks4-atom-economy-h11",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says a reaction with an atom economy of 100% must "
                "also have a percentage yield of 100%. Evaluate this claim.",
        "options": [
            "Wrong: the equation can be perfect while product is still lost",
            "Right: with one product, none of the reactant can be wasted",
            "Right: a 100% atom economy means nothing is left in the reactor "
            "at the end of the run",
            "Wrong: a 100% atom economy is impossible for any real reaction",
        ],
        "correct_index": 0,
        "why": "Atom economy says nothing about how much product survives "
               "filtering, transfer and drying, or whether the reaction went "
               "to completion.",
    },
    {
        "id": "ks4-atom-economy-h12",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Poly(ethene) is made from ethene by addition "
                "polymerisation. Determine the atom economy of this process "
                "for the polymer.",
        "options": [
            "50%, because half the ethene remains unreacted",
            "28%, because the Mr of ethene is 28",
            "It cannot be found, because the polymer has no fixed Mr",
            "100%, because the polymer is the only product formed",
        ],
        "correct_index": 3,
        "why": "Every ethene molecule joins the chain and nothing else is made, "
               "so all of the product mass is polymer.",
    },
    {
        "id": "ks4-atom-economy-h13",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calcium chloride is made by "
                "CaCO3 + 2HCl → CaCl2 + H2O + CO2. Mr: CaCl2 = 111, "
                "H2O = 18, CO2 = 44. Determine the atom economy for calcium "
                "chloride.",
        "options": [
            "35.8%",
            "71.6%",
            "83.5%",
            "64.2%",
        ],
        "correct_index": 3,
        "why": "The products total 111 + 18 + 44 = 173, so "
               "(111 ÷ 173) × 100 = 64.2%.",
    },
    {
        "id": "ks4-atom-economy-h14",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A process has an atom economy of 25%. Determine the mass of "
                "by-product formed alongside every 50 g of desired product.",
        "options": [
            "12.5 g",
            "200 g",
            "150 g",
            "50 g",
        ],
        "correct_index": 2,
        "why": "50 g is a quarter of the product mass, so the products total "
               "200 g and 200 − 50 = 150 g is by-product.",
    },
    {
        "id": "ks4-atom-economy-h15",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Of two routes to hydrogen, the one with the higher atom "
                "economy has the lower percentage yield. Determine what a "
                "company needs in order to choose between them.",
        "options": [
            "The atom economies alone, since they measure the real waste",
            "The percentage yields alone, since they measure what is collected",
            "Both figures, because together they fix the product per tonne of "
            "raw material",
            "Neither figure, because the cost of the reactants is what settles "
            "the matter by itself",
        ],
        "correct_index": 2,
        "why": "Atom economy fixes the maximum share of the mass that can be "
               "product and the yield fixes how much of that is obtained, so "
               "only the two together give the output per tonne.",
    },
    {
        "id": "ks4-atom-economy-h16",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student divides the Mr of the desired product by the total "
                "Mr of the reactants instead of the products. Determine the "
                "effect on the answer for a balanced equation.",
        "options": [
            "The answer is doubled",
            "The answer is halved",
            "The answer becomes a yield",
            "There is no effect, because the two totals are equal for a "
            "balanced equation",
        ],
        "correct_index": 3,
        "why": "Mass is conserved, so the Mr values of the reactants and of "
               "the products add up to the same total, and the fraction is "
               "unchanged.",
    },
    {
        "id": "ks4-atom-economy-h17",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In 2NaCl + 2H2O → 2NaOH + H2 + Cl2, a works sells both the "
                "sodium hydroxide and the chlorine. Mr: NaOH = 40, H2 = 2, "
                "Cl2 = 71. Determine the atom economy when both are counted "
                "as wanted.",
        "options": [
            "52.3%",
            "46.4%",
            "98.7%",
            "100%",
        ],
        "correct_index": 2,
        "why": "The wanted products total 80 + 71 = 151 out of 153, so "
               "(151 ÷ 153) × 100 = 98.7% — only the hydrogen is waste.",
    },
    {
        "id": "ks4-atom-economy-h18",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate this claim: 'A reaction with a low atom economy "
                "should not be used in industry.'",
        "options": [
            "Correct, because a low atom economy means the reaction wastes most "
            "of the material it is given",
            "Correct, because a low atom economy always makes a process "
            "unprofitable",
            "Wrong, because the by-product may be saleable or no better route "
            "may exist",
            "Wrong, because atom economy applies only to reactions run in a "
            "laboratory",
        ],
        "correct_index": 2,
        "why": "A by-product that can be sold is not waste, and a low-economy "
               "route can still be the only one available for that product.",
    },
]
