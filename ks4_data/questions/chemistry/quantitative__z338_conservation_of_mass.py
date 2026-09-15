"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`conservation-of-mass`.

The weight falls where AQA 4.3.1.1 puts it: the law itself and the reason for
it (atoms rearranged, none made or lost), then the mechanics of a balanced
symbol equation — what a coefficient may and may not touch, what it means,
state symbols, and balancing a wide spread of named reactions from combustion
and neutralisation to thermal decomposition, displacement and roasting. The
harder rows deduce a missing formula from the atoms that must be there, and do
mass arithmetic in closed vessels where a reactant is left over.

⚠️ FOUNDATION TIER. No mole appears in any stem, option or `why` — every mass
calculation here runs on a stated mass ratio or on conservation arithmetic,
which is how AQA asks this at Foundation.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-conservation-of-mass-e05",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the total mass of the products equals the total "
                "mass of the reactants in a chemical reaction.",
        "options": [
            "The atoms are rearranged, so the same atoms are there at the end",
            "The reactants and products contain the same number of molecules",
            "Any atoms destroyed in the reaction are replaced by atoms drawn "
            "from the air",
            "The products have the same chemical formulae as the reactants",
        ],
        "correct_index": 0,
        "why": "A chemical reaction only rearranges atoms into new "
               "combinations, so the number and type of atoms — and therefore "
               "the total mass — cannot change.",
    },
    {
        "id": "ks4-conservation-of-mass-e06",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the large number 3 in front of O2 tells you in the "
                "equation 2KClO3 → 2KCl + 3O2.",
        "options": [
            "Three oxygen atoms in total are formed each time this reaction "
            "happens",
            "Three oxygen molecules form for every two units of KClO3",
            "Each oxygen molecule formed contains three oxygen atoms",
            "Oxygen is the third substance written in the equation",
        ],
        "correct_index": 1,
        "why": "A large number in front of a formula counts units of that "
               "substance, so 3O2 means three oxygen molecules for the two "
               "units of KClO3 shown.",
    },
    {
        "id": "ks4-conservation-of-mass-e07",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the total number of oxygen atoms on the left-hand side "
                "of the equation Ca(OH)2 + H2SO4 → CaSO4 + 2H2O.",
        "options": [
            "2",
            "4",
            "6",
            "8",
        ],
        "correct_index": 2,
        "why": "Ca(OH)2 contributes two oxygen atoms and H2SO4 contributes "
               "four, giving six on the left — the same six that appear in "
               "CaSO4 and 2H2O.",
    },
    {
        "id": "ks4-conservation-of-mass-e08",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the balanced symbol equation for the reaction of "
                "sodium with water.",
        "options": [
            "Na + H2O → NaOH + H2",
            "2Na + H2O → 2NaOH + H2",
            "Na + 2H2O → NaOH + 2H2",
            "2Na + 2H2O → 2NaOH + H2",
        ],
        "correct_index": 3,
        "why": "2Na + 2H2O → 2NaOH + H2 has two sodium, four hydrogen and two "
               "oxygen atoms on each side, so every element balances.",
    },
    {
        "id": "ks4-conservation-of-mass-e09",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the word equation for the reaction between zinc and "
                "dilute hydrochloric acid.",
        "options": [
            "zinc + hydrochloric acid → zinc chloride + hydrogen",
            "zinc + hydrochloric acid → zinc oxide + hydrogen chloride gas",
            "zinc + hydrochloric acid → zinc hydroxide + chlorine",
            "zinc + hydrochloric acid → zinc chloride + water",
        ],
        "correct_index": 0,
        "why": "A metal and an acid give a salt and hydrogen, so zinc with "
               "hydrochloric acid gives zinc chloride and hydrogen gas.",
    },
    {
        "id": "ks4-conservation-of-mass-e10",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the substance missing from this equation for the "
                "thermal decomposition of calcium carbonate: "
                "CaCO3 → CaO + ______",
        "options": [
            "CO",
            "CO2",
            "O2",
            "C",
        ],
        "correct_index": 1,
        "why": "CaCO3 holds one carbon and three oxygen atoms; CaO takes one "
               "oxygen, leaving one carbon and two oxygen atoms, which is CO2.",
    },
    {
        "id": "ks4-conservation-of-mass-e11",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A closed container holds 2.4 g of magnesium and 1.6 g of "
                "oxygen. The magnesium is ignited and both substances are "
                "used up entirely. Calculate the mass of magnesium oxide "
                "that remains in the container.",
        "options": [
            "0.8 g",
            "1.6 g",
            "4.0 g",
            "4.8 g",
        ],
        "correct_index": 2,
        "why": "The container is closed and nothing else is present, so the "
               "mass of the product is 2.4 + 1.6 = 4.0 g.",
    },
    {
        "id": "ks4-conservation-of-mass-e12",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the state symbol that should be written after a "
                "substance that has been melted.",
        "options": [
            "(s)",
            "(g)",
            "(aq)",
            "(l)",
        ],
        "correct_index": 3,
        "why": "A melted substance is a pure liquid, which takes the state "
               "symbol (l); (aq) is reserved for a substance dissolved in "
               "water.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-conservation-of-mass-s05",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethane burns completely in oxygen: C2H6 + O2 → CO2 + H2O. "
                "Determine the simplest whole-number coefficients that "
                "balance this equation, written in the order C2H6, O2, CO2, "
                "H2O.",
        "options": [
            "2, 7, 4, 6",
            "1, 3, 2, 3",
            "2, 5, 4, 6",
            "1, 7, 2, 3",
        ],
        "correct_index": 0,
        "why": "2C2H6 + 7O2 → 4CO2 + 6H2O gives 4 carbon, 12 hydrogen and 14 "
               "oxygen atoms on each side.",
    },
    {
        "id": "ks4-conservation-of-mass-s06",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium burns in oxygen: xAl + 3O2 → 2Al2O3. Determine the "
                "value of x.",
        "options": [
            "6",
            "4",
            "3",
            "2",
        ],
        "correct_index": 1,
        "why": "2Al2O3 contains four aluminium atoms, so four aluminium atoms "
               "must react and x = 4.",
    },
    {
        "id": "ks4-conservation-of-mass-s07",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the balanced symbol equation for iron reacting with "
                "chlorine to form iron(III) chloride.",
        "options": [
            "Fe + Cl2 → FeCl3",
            "Fe + 3Cl2 → FeCl3",
            "2Fe + 3Cl2 → 2FeCl3",
            "2Fe + 6Cl2 → 2FeCl3",
        ],
        "correct_index": 2,
        "why": "Two FeCl3 units need six chlorine atoms, which is three Cl2 "
               "molecules, so 2Fe + 3Cl2 → 2FeCl3 balances.",
    },
    {
        "id": "ks4-conservation-of-mass-s08",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Phosphoric acid is neutralised by sodium hydroxide: "
                "NaOH + H3PO4 → Na3PO4 + H2O. Determine the simplest "
                "whole-number coefficients, written in the order shown.",
        "options": [
            "1, 1, 1, 1",
            "1, 3, 1, 3",
            "3, 1, 3, 1",
            "3, 1, 1, 3",
        ],
        "correct_index": 3,
        "why": "Na3PO4 needs three sodium atoms, so 3NaOH react with one "
               "H3PO4 and the six hydrogen atoms left over form 3H2O.",
    },
    {
        "id": "ks4-conservation-of-mass-s09",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethanol burns completely: C2H5OH + xO2 → 2CO2 + 3H2O. "
                "Determine the value of x.",
        "options": [
            "2",
            "3",
            "4",
            "7",
        ],
        "correct_index": 1,
        "why": "The products hold 4 + 3 = 7 oxygen atoms and the ethanol "
               "supplies one, so 6 must come from O2, giving x = 3.",
    },
    {
        "id": "ks4-conservation-of-mass-s10",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the balanced equation 2Al + 3CuCl2 → 2AlCl3 + 3Cu, state "
                "the ratio in which aluminium and copper(II) chloride react.",
        "options": [
            "1 : 1",
            "3 : 2",
            "2 : 6",
            "2 : 3",
        ],
        "correct_index": 3,
        "why": "The coefficients give the ratio directly: two units of "
               "aluminium react with three of copper(II) chloride, so 2 : 3.",
    },
    {
        "id": "ks4-conservation-of-mass-s11",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 2Mg(NO3)2 → 2MgO + 4NO2 + O2, determine the total number "
                "of oxygen atoms shown among the products.",
        "options": [
            "6",
            "8",
            "12",
            "14",
        ],
        "correct_index": 2,
        "why": "2MgO gives 2, 4NO2 gives 8 and O2 gives 2, so the products "
               "hold 12 oxygen atoms — the same 12 as in 2Mg(NO3)2.",
    },
    {
        "id": "ks4-conservation-of-mass-s12",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the balanced symbol equation for the neutralisation "
                "of nitric acid by calcium hydroxide.",
        "options": [
            "Ca(OH)2 + 2HNO3 → Ca(NO3)2 + 2H2O",
            "Ca(OH)2 + HNO3 → Ca(NO3)2 + H2O",
            "Ca(OH)2 + 2HNO3 → CaNO3 + 2H2O",
            "2Ca(OH)2 + HNO3 → Ca(NO3)2 + H2O",
        ],
        "correct_index": 0,
        "why": "Calcium nitrate is Ca(NO3)2, so two HNO3 are needed, and the "
               "two hydroxide groups with the two acid hydrogens give 2H2O.",
    },
    {
        "id": "ks4-conservation-of-mass-s13",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes the reaction of sodium with chlorine as "
                "Na + Cl → NaCl and says the atoms balance. Explain what is "
                "wrong.",
        "options": [
            "Chlorine gas exists as Cl2 molecules, so Cl is the wrong formula",
            "Sodium chloride is an ionic compound, so no formula can be "
            "written for it",
            "The sodium chloride needs a coefficient of 2 to make it balance",
            "Sodium reacts as Na2, so the sodium must be written as Na2 here",
        ],
        "correct_index": 0,
        "why": "Chlorine is a diatomic molecule, so the correct starting "
               "equation is 2Na + Cl2 → 2NaCl.",
    },
    {
        "id": "ks4-conservation-of-mass-s14",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "When 100 g of calcium carbonate decomposes it gives 56 g of "
                "calcium oxide and 44 g of carbon dioxide. Calculate the mass "
                "of carbon dioxide made from 50 g of calcium carbonate.",
        "options": [
            "44 g",
            "28 g",
            "11 g",
            "22 g",
        ],
        "correct_index": 3,
        "why": "Half the mass of carbonate gives half of every product, so the "
               "carbon dioxide is 44 ÷ 2 = 22 g.",
    },
    {
        "id": "ks4-conservation-of-mass-s15",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed flask, 12.8 g of sulfur dioxide reacts "
                "completely with oxygen and 16.0 g of sulfur trioxide is the "
                "only product. Calculate the mass of oxygen that reacted.",
        "options": [
            "28.8 g",
            "4.8 g",
            "3.2 g",
            "2.4 g",
        ],
        "correct_index": 2,
        "why": "The product mass equals the total reactant mass, so the oxygen "
               "was 16.0 − 12.8 = 3.2 g.",
    },
    {
        "id": "ks4-conservation-of-mass-s16",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what must be true of a symbol equation before it can be "
                "used to work out the masses of reactants and products.",
        "options": [
            "It must include a state symbol for every substance",
            "It must show the reactants written in alphabetical order",
            "It must contain as many substances on each side",
            "It must have the same number of each type of atom on both sides",
        ],
        "correct_index": 3,
        "why": "Only a balanced equation gives the true ratio in which the "
               "substances react, and that ratio is what any mass "
               "calculation rests on.",
    },
    {
        "id": "ks4-conservation-of-mass-s17",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lead(II) nitrate solution is mixed with potassium iodide "
                "solution: Pb(NO3)2 + KI → PbI2 + KNO3. Determine the "
                "simplest whole-number coefficients, written in the order "
                "shown.",
        "options": [
            "1, 1, 1, 1",
            "2, 1, 2, 1",
            "1, 2, 1, 2",
            "1, 2, 1, 1",
        ],
        "correct_index": 2,
        "why": "PbI2 needs two iodide units, so 2KI react, and the two "
               "potassium atoms released form 2KNO3.",
    },
    {
        "id": "ks4-conservation-of-mass-s18",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 4NH3 + 5O2 → 4NO + 6H2O, state the ratio in which ammonia "
                "and oxygen react.",
        "options": [
            "1 : 1",
            "4 : 6",
            "4 : 5",
            "5 : 4",
        ],
        "correct_index": 2,
        "why": "The coefficients of the two reactants are 4 and 5, so ammonia "
               "and oxygen react in the ratio 4 : 5.",
    },
    {
        "id": "ks4-conservation-of-mass-s19",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction N2 + 3H2 → 2NH3, 28 g of nitrogen reacts "
                "exactly with 6 g of hydrogen to give 34 g of ammonia. "
                "Calculate the mass of ammonia formed from 14 g of nitrogen.",
        "options": [
            "3 g",
            "17 g",
            "20 g",
            "34 g",
        ],
        "correct_index": 1,
        "why": "14 g of nitrogen is half of 28 g, so half as much ammonia "
               "forms: 34 ÷ 2 = 17 g.",
    },
    {
        "id": "ks4-conservation-of-mass-s20",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Propan-1-ol burns completely: 2C3H7OH + xO2 → 6CO2 + 8H2O. "
                "Determine the value of x.",
        "options": [
            "6",
            "7",
            "9",
            "10",
        ],
        "correct_index": 2,
        "why": "The products hold 12 + 8 = 20 oxygen atoms and the two "
               "alcohol molecules supply two, so 18 come from O2 and x = 9.",
    },
    {
        "id": "ks4-conservation-of-mass-s21",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the balanced symbol equation for the thermal "
                "decomposition of potassium chlorate into potassium chloride "
                "and oxygen.",
        "options": [
            "KClO3 → KCl + O2",
            "2KClO3 → 2KCl + 3O2",
            "2KClO3 → 2KCl + 2O2",
            "2KClO3 → 2KCl + O2",
        ],
        "correct_index": 1,
        "why": "Two KClO3 units hold six oxygen atoms, which leave as three "
               "O2 molecules, so 2KClO3 → 2KCl + 3O2 balances.",
    },
    {
        "id": "ks4-conservation-of-mass-s22",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the equation that correctly shows zinc reacting "
                "with dilute sulfuric acid, including state symbols.",
        "options": [
            "Zn(aq) + H2SO4(aq) → ZnSO4(s) + H2(l)",
            "Zn(s) + H2SO4(l) → ZnSO4(aq) + H2(g)",
            "Zn(g) + H2SO4(aq) → ZnSO4(aq) + H2(s)",
            "Zn(s) + H2SO4(aq) → ZnSO4(aq) + H2(g)",
        ],
        "correct_index": 3,
        "why": "Zinc is a solid, the dilute acid and the salt formed are both "
               "in solution, and the hydrogen leaves as a gas.",
    },
    {
        "id": "ks4-conservation-of-mass-s23",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron reacts with steam: Fe + H2O → Fe3O4 + H2. Determine the "
                "simplest whole-number coefficients, written in the order "
                "shown.",
        "options": [
            "1, 1, 1, 1",
            "3, 2, 1, 2",
            "3, 4, 1, 4",
            "1, 4, 3, 4",
        ],
        "correct_index": 2,
        "why": "Fe3O4 needs three iron and four oxygen atoms, so 3Fe react "
               "with 4H2O and the eight hydrogen atoms leave as 4H2.",
    },
    {
        "id": "ks4-conservation-of-mass-s24",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed container, 13.7 g of a solid decomposes into "
                "8.0 g of one solid product, 2.9 g of a second solid product "
                "and a gas. Calculate the mass of gas produced.",
        "options": [
            "1.9 g",
            "2.8 g",
            "5.7 g",
            "10.9 g",
        ],
        "correct_index": 1,
        "why": "The three products together must weigh 13.7 g, so the gas is "
               "13.7 − 8.0 − 2.9 = 2.8 g.",
    },
    {
        "id": "ks4-conservation-of-mass-s25",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium burns in a sealed tube: 2Mg + O2 → 2MgO. 48 g of "
                "magnesium reacts exactly with 32 g of oxygen. Calculate the "
                "mass of oxygen needed to react with 12 g of magnesium.",
        "options": [
            "20 g",
            "16 g",
            "8 g",
            "4 g",
        ],
        "correct_index": 2,
        "why": "12 g is a quarter of 48 g, so a quarter of the oxygen is "
               "needed: 32 ÷ 4 = 8 g.",
    },
    {
        "id": "ks4-conservation-of-mass-s26",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says an equation must be balanced because it has "
                "three substances on the left and three on the right. Explain "
                "why this is not a valid check.",
        "options": [
            "Balancing compares the atoms of each element, not the number of "
            "substances",
            "Balancing compares the total mass of the formulae written on "
            "each side",
            "Balancing compares the number of molecules written on each side "
            "of the arrow shown",
            "Balancing compares the state symbols given for each of the "
            "substances shown",
        ],
        "correct_index": 0,
        "why": "An equation balances when each element has the same number of "
               "atoms on both sides; how many formulae appear is irrelevant.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-conservation-of-mass-h05",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hexane burns completely: 2C6H14 + xO2 → 12CO2 + 14H2O. "
                "Determine the value of x.",
        "options": [
            "13",
            "17",
            "19",
            "21",
        ],
        "correct_index": 2,
        "why": "The products hold 24 + 14 = 38 oxygen atoms, all from O2, so "
               "x = 38 ÷ 2 = 19.",
    },
    {
        "id": "ks4-conservation-of-mass-h06",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation 2NaHCO3 → Na2CO3 + H2O + X, determine the "
                "formula of X.",
        "options": [
            "CO",
            "H2",
            "O2",
            "CO2",
        ],
        "correct_index": 3,
        "why": "The left side holds 2 Na, 2 H, 2 C and 6 O; Na2CO3 and H2O "
               "account for all but one carbon and two oxygen atoms, so X is "
               "CO2.",
    },
    {
        "id": "ks4-conservation-of-mass-h07",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation 3Fe + 4H2O → X + 4H2, determine the formula "
                "of X.",
        "options": [
            "FeO",
            "Fe2O3",
            "Fe3O4",
            "Fe(OH)3",
        ],
        "correct_index": 2,
        "why": "Three iron atoms react and the four water molecules leave "
               "four oxygen atoms behind once the hydrogen has gone, so X is "
               "Fe3O4.",
    },
    {
        "id": "ks4-conservation-of-mass-h08",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethanol burns completely: C2H5OH + O2 → CO2 + H2O. Determine "
                "the simplest whole-number coefficients, written in the order "
                "shown.",
        "options": [
            "1, 2, 2, 3",
            "1, 3, 2, 3",
            "1, 3, 2, 2",
            "2, 3, 4, 6",
        ],
        "correct_index": 1,
        "why": "C2H5OH + 3O2 → 2CO2 + 3H2O gives 2 carbon, 6 hydrogen and 7 "
               "oxygen atoms on each side.",
    },
    {
        "id": "ks4-conservation-of-mass-h09",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student mixes two solutions in a stoppered flask on a "
                "balance and the reading rises by 0.1 g. Evaluate the "
                "student's conclusion that mass has been created.",
        "options": [
            "Wrong: no matter can enter a stoppered flask, so the rise must "
            "be a measurement error",
            "Right: a precipitation reaction adds mass because a new solid "
            "has formed",
            "Right: gases from the air are drawn in as the reaction uses "
            "reactants up",
            "Wrong: mass is conserved, so the products must weigh less than "
            "the reactants",
        ],
        "correct_index": 0,
        "why": "A stoppered flask is a closed system, so its total mass "
               "cannot change; a 0.1 g rise is a fault in the measurement, "
               "not in the chemistry.",
    },
    {
        "id": "ks4-conservation-of-mass-h10",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed flask, 6.0 g of magnesium is heated with 3.2 g of "
                "oxygen. 8.0 g of magnesium oxide forms and some magnesium is "
                "left. Calculate the mass of magnesium that did not react.",
        "options": [
            "6.0 g",
            "4.8 g",
            "2.8 g",
            "1.2 g",
        ],
        "correct_index": 3,
        "why": "The flask holds 6.0 + 3.2 = 9.2 g throughout, and 8.0 g of "
               "that is magnesium oxide, so 1.2 g of magnesium is left over.",
    },
    {
        "id": "ks4-conservation-of-mass-h11",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 2Al + 3Cl2 → 2AlCl3, 54 g of aluminium reacts exactly with "
                "213 g of chlorine to give 267 g of aluminium chloride. "
                "Calculate the mass of aluminium chloride formed from 18 g of "
                "aluminium.",
        "options": [
            "267 g",
            "134 g",
            "89 g",
            "71 g",
        ],
        "correct_index": 2,
        "why": "18 g is one third of 54 g, so one third of the product forms: "
               "267 ÷ 3 = 89 g.",
    },
    {
        "id": "ks4-conservation-of-mass-h12",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "When copper is warmed with concentrated nitric acid the "
                "products are copper(II) nitrate, nitrogen dioxide and water. "
                "Determine how many molecules of nitric acid react with each "
                "copper atom.",
        "options": [
            "2",
            "3",
            "4",
            "8",
        ],
        "correct_index": 2,
        "why": "Cu + 4HNO3 → Cu(NO3)2 + 2NO2 + 2H2O gives 4 hydrogen, 4 "
               "nitrogen and 12 oxygen atoms on each side.",
    },
    {
        "id": "ks4-conservation-of-mass-h13",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes Mg + O → MgO for magnesium burning in air "
                "and says every atom balances. Explain what is wrong with "
                "this equation.",
        "options": [
            "Oxygen in air is O2, so the equation must be 2Mg + O2 → 2MgO",
            "Magnesium oxide is ionic, so the equation needs its charges "
            "shown",
            "Magnesium exists as Mg2 molecules, so it must be written as Mg2 "
            "here",
            "Burning needs a coefficient of 2 written in front of every "
            "substance involved",
        ],
        "correct_index": 0,
        "why": "Oxygen is a diatomic molecule, so the equation must start "
               "from O2, which then needs two magnesium atoms to balance.",
    },
    {
        "id": "ks4-conservation-of-mass-h14",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper oxide is reduced by hydrogen: CuO + H2 → Cu + H2O. In "
                "one run, 80 g of copper oxide gave 64 g of copper and 18 g "
                "of water. Calculate the mass of hydrogen used.",
        "options": [
            "34 g",
            "18 g",
            "16 g",
            "2 g",
        ],
        "correct_index": 3,
        "why": "The two reactant masses must total the two product masses, so "
               "the hydrogen was (64 + 18) − 80 = 2 g.",
    },
    {
        "id": "ks4-conservation-of-mass-h15",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "20.0 g of a metal M reacts completely with chlorine in a "
                "sealed vessel and 38.2 g of the chloride MCl2 is the only "
                "product. Calculate the mass of chlorine that reacted.",
        "options": [
            "58.2 g",
            "38.2 g",
            "19.1 g",
            "18.2 g",
        ],
        "correct_index": 3,
        "why": "Nothing leaves a sealed vessel, so the chlorine is "
               "38.2 − 20.0 = 18.2 g.",
    },
    {
        "id": "ks4-conservation-of-mass-h16",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats 4.00 g of a metal with 1.00 g of sulfur in a "
                "sealed tube. All the sulfur reacts, 3.30 g of metal sulfide "
                "forms, and metal is left over. Calculate the mass of metal "
                "left over.",
        "options": [
            "0.70 g",
            "1.70 g",
            "2.30 g",
            "3.00 g",
        ],
        "correct_index": 1,
        "why": "The sealed tube holds 5.00 g throughout, and 3.30 g of that "
               "is the sulfide, so 1.70 g of metal is unreacted.",
    },
    {
        "id": "ks4-conservation-of-mass-h17",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium reacts with dilute sulfuric acid: "
                "Al + H2SO4 → Al2(SO4)3 + H2. Determine the simplest "
                "whole-number coefficients, written in the order shown.",
        "options": [
            "1, 3, 1, 3",
            "2, 3, 1, 3",
            "2, 1, 1, 1",
            "2, 6, 1, 6",
        ],
        "correct_index": 1,
        "why": "Al2(SO4)3 needs two aluminium atoms and three sulfate groups, "
               "so 2Al react with 3H2SO4 and the six hydrogen atoms give "
               "3H2.",
    },
    {
        "id": "ks4-conservation-of-mass-h18",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ammonium nitrate decomposes: 2NH4NO3 → 2N2 + O2 + 4H2O. "
                "Determine the total number of atoms shown on the right-hand "
                "side.",
        "options": [
            "12",
            "14",
            "18",
            "20",
        ],
        "correct_index": 2,
        "why": "2N2 is 4 atoms, O2 is 2 and 4H2O is 12, giving 18 atoms in "
               "the products — the same 18 as in 2NH4NO3.",
    },
    {
        "id": "ks4-conservation-of-mass-h19",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "10.0 g of substance A reacts with 15.0 g of substance B to "
                "make a single product C. A student collects 22.0 g of C and "
                "concludes that 3.0 g of mass was destroyed. Evaluate this "
                "conclusion.",
        "options": [
            "Wrong: 25.0 g of C must have formed, so 3.0 g of it was lost in "
            "the apparatus",
            "Right: some mass is always lost as heat energy escapes from the "
            "reaction mixture",
            "Wrong: the missing 3.0 g escaped as an invisible gas, so C cannot "
            "have been the only product",
            "Right: the product is denser than the reactants were, so it "
            "weighs less overall",
        ],
        "correct_index": 0,
        "why": "Mass is conserved, so all 25.0 g of C formed; collecting only "
               "22.0 g means 3.0 g stayed on the glassware or in the filter.",
    },
    {
        "id": "ks4-conservation-of-mass-h20",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The thermite reaction is Fe2O3 + 2Al → Al2O3 + 2Fe. In one "
                "run, 160 g of iron(III) oxide reacted with 54 g of aluminium "
                "and 102 g of aluminium oxide was collected. Calculate the "
                "mass of iron formed.",
        "options": [
            "56 g",
            "102 g",
            "112 g",
            "214 g",
        ],
        "correct_index": 2,
        "why": "The reactants total 214 g, so the products must too, and the "
               "iron is 214 − 102 = 112 g.",
    },
    {
        "id": "ks4-conservation-of-mass-h21",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron pyrite is roasted in oxygen: FeS2 + O2 → Fe2O3 + SO2. "
                "Determine the simplest whole-number coefficients, written in "
                "the order shown.",
        "options": [
            "2, 5, 1, 4",
            "4, 11, 2, 8",
            "1, 3, 1, 2",
            "4, 7, 2, 8",
        ],
        "correct_index": 1,
        "why": "4FeS2 + 11O2 → 2Fe2O3 + 8SO2 gives 4 iron, 8 sulfur and 22 "
               "oxygen atoms on each side.",
    },
    {
        "id": "ks4-conservation-of-mass-h22",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes the combustion of butane as "
                "C4H10 + 6O2 → 4CO2 + 5H2O and says it is balanced. Determine "
                "what is wrong with it.",
        "options": [
            "The carbon atoms do not balance, so the CO2 needs a coefficient "
            "of 8",
            "Thirteen oxygen atoms are needed on the left, so the equation "
            "must be doubled",
            "The hydrogen atoms do not balance, so the water needs 10 in front",
            "Nothing is wrong: the atoms of every element balance on both sides",
        ],
        "correct_index": 1,
        "why": "The products hold 8 + 5 = 13 oxygen atoms but 6O2 supplies "
               "only 12, so the whole equation is doubled to "
               "2C4H10 + 13O2 → 8CO2 + 10H2O.",
    },
    {
        "id": "ks4-conservation-of-mass-h23",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 4Fe + 3O2 → 2Fe2O3, 224 g of iron reacts exactly with 96 g "
                "of oxygen to give 320 g of iron(III) oxide. Calculate the "
                "mass of oxygen needed to react with 56 g of iron.",
        "options": [
            "12 g",
            "24 g",
            "48 g",
            "80 g",
        ],
        "correct_index": 1,
        "why": "56 g is a quarter of 224 g, so a quarter of the oxygen is "
               "needed: 96 ÷ 4 = 24 g.",
    },
    {
        "id": "ks4-conservation-of-mass-h24",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the balanced equation 2X + 15O2 → 12CO2 + 6H2O, determine "
                "the formula of X.",
        "options": [
            "C6H12",
            "C12H12",
            "C6H14",
            "C6H6",
        ],
        "correct_index": 3,
        "why": "The 12 carbon and 12 hydrogen atoms in the products are "
               "shared between two units of X, so each holds 6 carbon and 6 "
               "hydrogen atoms.",
    },
    {
        "id": "ks4-conservation-of-mass-h25",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed glass tube of mass 20.00 g holds 12.50 g of zinc "
                "carbonate. The tube is heated until the carbonate has fully "
                "decomposed to zinc oxide and carbon dioxide, then reweighed "
                "while still sealed. Determine the reading.",
        "options": [
            "20.00 g",
            "27.10 g",
            "32.50 g",
            "37.90 g",
        ],
        "correct_index": 2,
        "why": "The carbon dioxide is trapped inside, so the sealed tube "
               "still holds everything it started with: 20.00 + 12.50 = "
               "32.50 g.",
    },
    {
        "id": "ks4-conservation-of-mass-h26",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium carbonate reacts with dilute nitric acid: "
                "CaCO3 + HNO3 → Ca(NO3)2 + H2O + CO2. Determine the simplest "
                "whole-number coefficients, written in the order shown.",
        "options": [
            "1, 1, 1, 1, 1",
            "1, 2, 1, 1, 1",
            "1, 2, 1, 2, 1",
            "2, 2, 1, 1, 2",
        ],
        "correct_index": 1,
        "why": "Ca(NO3)2 needs two nitrate groups, so 2HNO3 react, and their "
               "two hydrogen atoms give one H2O alongside one CO2.",
    },
]
