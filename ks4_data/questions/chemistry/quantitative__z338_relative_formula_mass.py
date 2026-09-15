"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`relative-formula-mass`.

AQA 4.3.1.2, taken wide rather than deep: Mr as a sum of Ar values with no
unit, across simple molecules, ionic compounds, bracketed formulae, hydrated
salts and the diatomic elements; then the two things Mr is FOR — working
backwards to an unknown Ar or to an unknown formula, and turning a balanced
equation into a mass ratio. The harder rows sit on the two errors the estate
sees most: a bracket subscript ignored, and atomic numbers used in place of
relative atomic masses.

⚠️ FOUNDATION TIER. Nothing here uses a mole. Every mass calculation runs on a
ratio of Mr values stated in the stem, which is how AQA asks this at
Foundation.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-relative-formula-mass-e05",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon dioxide, CO2, is the gas given off when a carbonate is "
                "heated. Calculate its relative formula mass. "
                "Ar: C = 12, O = 16.",
        "options": [
            "44",
            "28",
            "56",
            "22",
        ],
        "correct_index": 0,
        "why": "One carbon atom and two oxygen atoms give 12 + (2 × 16) = 44.",
    },
    {
        "id": "ks4-relative-formula-mass-e06",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium chloride, CaCl2, is spread on icy roads. Calculate "
                "its relative formula mass. Ar: Ca = 40, Cl = 35.5.",
        "options": [
            "75.5",
            "111",
            "146.5",
            "80",
        ],
        "correct_index": 1,
        "why": "Two chlorine atoms are needed, so the Mr is "
               "40 + (2 × 35.5) = 111.",
    },
    {
        "id": "ks4-relative-formula-mass-e07",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit in which a relative formula mass is quoted.",
        "options": [
            "It is quoted in grams for every one of the compound's formula "
            "units",
            "It is quoted in grams per centimetre cubed of the substance",
            "It has no unit, because it compares one mass with another",
            "It is quoted in grams, taken from the periodic table directly",
        ],
        "correct_index": 2,
        "why": "Relative masses are ratios measured against the carbon-12 "
               "atom, so an Mr is just a number with no unit attached.",
    },
    {
        "id": "ks4-relative-formula-mass-e08",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Natural gas is mostly methane, CH4. Calculate the relative "
                "formula mass of methane. Ar: C = 12, H = 1.",
        "options": [
            "13",
            "17",
            "48",
            "16",
        ],
        "correct_index": 3,
        "why": "One carbon atom and four hydrogen atoms give "
               "12 + (4 × 1) = 16.",
    },
    {
        "id": "ks4-relative-formula-mass-e09",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car battery contains sulfuric acid, H2SO4. Calculate the "
                "relative formula mass of sulfuric acid. "
                "Ar: H = 1, S = 32, O = 16.",
        "options": [
            "98",
            "49",
            "50",
            "82",
        ],
        "correct_index": 0,
        "why": "Two hydrogen, one sulfur and four oxygen atoms give "
               "2 + 32 + 64 = 98.",
    },
    {
        "id": "ks4-relative-formula-mass-e10",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine gas exists as Cl2 molecules. Calculate the relative "
                "formula mass of one chlorine molecule. Ar: Cl = 35.5.",
        "options": [
            "35.5",
            "71",
            "106.5",
            "17.75",
        ],
        "correct_index": 1,
        "why": "A chlorine molecule holds two chlorine atoms, so its Mr is "
               "2 × 35.5 = 71.",
    },
    {
        "id": "ks4-relative-formula-mass-e11",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Washing soda contains sodium carbonate, Na2CO3. Calculate "
                "its relative formula mass. Ar: Na = 23, C = 12, O = 16.",
        "options": [
            "83",
            "51",
            "106",
            "144",
        ],
        "correct_index": 2,
        "why": "Two sodium, one carbon and three oxygen atoms give "
               "46 + 12 + 48 = 106.",
    },
    {
        "id": "ks4-relative-formula-mass-e12",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what must be done with the atoms inside the brackets of "
                "Ca(NO3)2 when its relative formula mass is worked out.",
        "options": [
            "They are added together once and the 2 outside the bracket is "
            "ignored",
            "They are added to the calcium and the total is then halved",
            "They are added once and the calcium is counted twice instead",
            "They are all counted twice, since the 2 applies to every one",
        ],
        "correct_index": 3,
        "why": "The 2 outside the bracket multiplies everything inside it, so "
               "Ca(NO3)2 holds two nitrogen and six oxygen atoms.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-relative-formula-mass-s05",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bauxite is purified to aluminium oxide, Al2O3, before "
                "electrolysis. Calculate the relative formula mass of "
                "aluminium oxide. Ar: Al = 27, O = 16.",
        "options": [
            "102",
            "43",
            "86",
            "75",
        ],
        "correct_index": 0,
        "why": "Two aluminium and three oxygen atoms give "
               "(2 × 27) + (3 × 16) = 102.",
    },
    {
        "id": "ks4-relative-formula-mass-s06",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium nitrate, Ca(NO3)2, is sold as a fertiliser. "
                "Calculate its relative formula mass. "
                "Ar: Ca = 40, N = 14, O = 16.",
        "options": [
            "102",
            "164",
            "140",
            "118",
        ],
        "correct_index": 1,
        "why": "The bracket is doubled, so the Mr is "
               "40 + (2 × 14) + (6 × 16) = 164.",
    },
    {
        "id": "ks4-relative-formula-mass-s07",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Anhydrous magnesium sulfate, MgSO4, is added to plant feeds. "
                "Determine its relative formula mass. "
                "Ar: Mg = 24, S = 32, O = 16.",
        "options": [
            "72",
            "104",
            "120",
            "246",
        ],
        "correct_index": 2,
        "why": "One magnesium, one sulfur and four oxygen atoms give "
               "24 + 32 + 64 = 120.",
    },
    {
        "id": "ks4-relative-formula-mass-s08",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Glucose, C6H12O6, is the sugar respired by living cells. "
                "Determine its relative formula mass. "
                "Ar: C = 12, H = 1, O = 16.",
        "options": [
            "29",
            "96",
            "168",
            "180",
        ],
        "correct_index": 3,
        "why": "Six carbon, twelve hydrogen and six oxygen atoms give "
               "72 + 12 + 96 = 180.",
    },
    {
        "id": "ks4-relative-formula-mass-s09",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ammonium chloride, NH4Cl, is the electrolyte in a dry cell. "
                "Determine its relative formula mass. "
                "Ar: N = 14, H = 1, Cl = 35.5.",
        "options": [
            "53.5",
            "50.5",
            "49.5",
            "88",
        ],
        "correct_index": 0,
        "why": "One nitrogen, four hydrogen and one chlorine atom give "
               "14 + 4 + 35.5 = 53.5.",
    },
    {
        "id": "ks4-relative-formula-mass-s10",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Plaster is made from hydrated calcium sulfate, CaSO4.2H2O. "
                "Determine its relative formula mass. "
                "Ar: Ca = 40, S = 32, O = 16, H = 1.",
        "options": [
            "154",
            "172",
            "136",
            "208",
        ],
        "correct_index": 1,
        "why": "CaSO4 is 136 and two water molecules add 36, giving "
               "136 + 36 = 172.",
    },
    {
        "id": "ks4-relative-formula-mass-s11",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chloride of a metal M has the formula MCl2 and a relative "
                "formula mass of 95. Ar of Cl = 35.5. Determine the relative "
                "atomic mass of M.",
        "options": [
            "59.5",
            "48",
            "24",
            "12",
        ],
        "correct_index": 2,
        "why": "The two chlorine atoms account for 71, so M must be "
               "95 − 71 = 24.",
    },
    {
        "id": "ks4-relative-formula-mass-s12",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "For 2Mg + O2 → 2MgO, the Mr of magnesium oxide is 40. "
                "Determine the total relative formula mass of the products of "
                "this equation.",
        "options": [
            "40",
            "56",
            "72",
            "80",
        ],
        "correct_index": 3,
        "why": "There are two units of MgO in the products, so the total is "
               "2 × 40 = 80 — the same total as the reactants.",
    },
    {
        "id": "ks4-relative-formula-mass-s13",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium manganate(VII), KMnO4, is a purple oxidising "
                "agent. Determine its relative formula mass. "
                "Ar: K = 39, Mn = 55, O = 16.",
        "options": [
            "158",
            "110",
            "174",
            "94",
        ],
        "correct_index": 0,
        "why": "One potassium, one manganese and four oxygen atoms give "
               "39 + 55 + 64 = 158.",
    },
    {
        "id": "ks4-relative-formula-mass-s14",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ar: C = 12, S = 32, O = 16. Compare the relative formula "
                "masses of carbon dioxide, CO2, and sulfur dioxide, SO2.",
        "options": [
            "They are the same, because each formula holds two oxygen atoms "
            "in total",
            "Sulfur dioxide is larger, at 64 against 44 for carbon dioxide",
            "Carbon dioxide is larger, at 44 against 32 for sulfur dioxide",
            "Sulfur dioxide is larger, at 96 against 44 for carbon dioxide",
        ],
        "correct_index": 1,
        "why": "CO2 is 12 + 32 = 44 and SO2 is 32 + 32 = 64, so the sulfur "
               "compound has the larger Mr by 20.",
    },
    {
        "id": "ks4-relative-formula-mass-s15",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper oxide is reduced by hydrogen: CuO + H2 → Cu + H2O. "
                "The Mr of CuO is 80 and the Ar of Cu is 64, so 80 g of "
                "copper oxide gives 64 g of copper. Calculate the mass of "
                "copper obtained from 20 g of copper oxide.",
        "options": [
            "4 g",
            "10 g",
            "16 g",
            "25 g",
        ],
        "correct_index": 2,
        "why": "20 g is a quarter of 80 g, so a quarter of the copper forms: "
               "64 ÷ 4 = 16 g.",
    },
    {
        "id": "ks4-relative-formula-mass-s16",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ammonium phosphate, (NH4)3PO4, is used as a fertiliser. "
                "Determine its relative formula mass. "
                "Ar: N = 14, H = 1, P = 31, O = 16.",
        "options": [
            "113",
            "131",
            "203",
            "149",
        ],
        "correct_index": 3,
        "why": "Three NH4 groups give 54, and PO4 gives 31 + 64 = 95, so the "
               "Mr is 149.",
    },
    {
        "id": "ks4-relative-formula-mass-s17",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethanol, C2H5OH, is the alcohol made by fermentation. "
                "Determine its relative formula mass. "
                "Ar: C = 12, H = 1, O = 16.",
        "options": [
            "46",
            "45",
            "44",
            "62",
        ],
        "correct_index": 0,
        "why": "Two carbon, six hydrogen and one oxygen atom give "
               "24 + 6 + 16 = 46.",
    },
    {
        "id": "ks4-relative-formula-mass-s18",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrated sodium carbonate crystals have the formula "
                "Na2CO3.10H2O. Determine their relative formula mass. "
                "Ar: Na = 23, C = 12, O = 16, H = 1.",
        "options": [
            "126",
            "286",
            "268",
            "196",
        ],
        "correct_index": 1,
        "why": "Na2CO3 is 106 and ten water molecules add 180, giving "
               "106 + 180 = 286.",
    },
    {
        "id": "ks4-relative-formula-mass-s19",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium sulfate has the formula Na2SO4 and a relative formula "
                "mass of 142. Ar: Na = 23, O = 16. Determine the relative "
                "atomic mass of sulfur.",
        "options": [
            "16",
            "28",
            "32",
            "64",
        ],
        "correct_index": 2,
        "why": "Two sodium atoms give 46 and four oxygen atoms give 64, so "
               "sulfur must be 142 − 110 = 32.",
    },
    {
        "id": "ks4-relative-formula-mass-s20",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lead(II) nitrate, Pb(NO3)2, gives a yellow precipitate with "
                "iodide ions. Determine its relative formula mass. "
                "Ar: Pb = 207, N = 14, O = 16.",
        "options": [
            "269",
            "283",
            "331",
            "455",
        ],
        "correct_index": 2,
        "why": "The bracket is doubled, so the Mr is "
               "207 + (2 × 14) + (6 × 16) = 331.",
    },
    {
        "id": "ks4-relative-formula-mass-s21",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the blast furnace, Fe2O3 + 3CO → 2Fe + 3CO2. The Mr of "
                "Fe2O3 is 160 and 160 g of it yields 112 g of iron. Calculate "
                "the mass of iron obtained from 40 g of iron(III) oxide.",
        "options": [
            "28 g",
            "56 g",
            "14 g",
            "112 g",
        ],
        "correct_index": 0,
        "why": "40 g is a quarter of 160 g, so a quarter of the iron forms: "
               "112 ÷ 4 = 28 g.",
    },
    {
        "id": "ks4-relative-formula-mass-s22",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two compounds with the same relative formula "
                "mass are not necessarily the same substance.",
        "options": [
            "Because a relative formula mass is only ever an estimate of the "
            "true value",
            "Because different combinations of atoms can add up to the same "
            "total",
            "Because a relative formula mass changes with the temperature of "
            "the sample",
            "Because the relative formula mass of a compound depends on how "
            "much there is",
        ],
        "correct_index": 1,
        "why": "Mr is just a sum, and unrelated formulae can reach the same "
               "sum — CO2 and C3H8 both come to 44.",
    },
    {
        "id": "ks4-relative-formula-mass-s23",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium dichromate(VI), K2Cr2O7, is an orange crystalline "
                "solid. Determine its relative formula mass. "
                "Ar: K = 39, Cr = 52, O = 16.",
        "options": [
            "203",
            "214",
            "294",
            "406",
        ],
        "correct_index": 2,
        "why": "Two potassium give 78, two chromium give 104 and seven oxygen "
               "give 112, so the Mr is 294.",
    },
    {
        "id": "ks4-relative-formula-mass-s24",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Temporary hard water contains calcium hydrogencarbonate, "
                "Ca(HCO3)2. Determine its relative formula mass. "
                "Ar: Ca = 40, H = 1, C = 12, O = 16.",
        "options": [
            "101",
            "117",
            "146",
            "162",
        ],
        "correct_index": 3,
        "why": "Each HCO3 group is 61 and there are two of them, so the Mr is "
               "40 + 122 = 162.",
    },
    {
        "id": "ks4-relative-formula-mass-s25",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oxide of nitrogen has a relative formula mass of 46 and "
                "one nitrogen atom in its formula. Ar: N = 14, O = 16. "
                "Determine the formula of this oxide.",
        "options": [
            "NO2",
            "NO",
            "N2O",
            "N2O4",
        ],
        "correct_index": 0,
        "why": "46 − 14 = 32, which is two oxygen atoms, so the formula is "
               "NO2.",
    },
    {
        "id": "ks4-relative-formula-mass-s26",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "For CaCO3 → CaO + CO2 the Mr values are 100, 56 and 44. "
                "Explain what the relationship between these three numbers "
                "shows.",
        "options": [
            "That the calcium oxide is the heavier of the two products formed",
            "That the total Mr is unchanged, because the atoms have only been "
            "rearranged",
            "That carbon dioxide must escape for the equation to work",
            "That a reactant's Mr is larger than that of any product",
        ],
        "correct_index": 1,
        "why": "56 + 44 = 100, so the products carry exactly the same atoms, "
               "and therefore the same total Mr, as the reactant.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-relative-formula-mass-h05",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium sulfate, Al2(SO4)3, is used to clarify drinking "
                "water. Determine its relative formula mass. "
                "Ar: Al = 27, S = 32, O = 16.",
        "options": [
            "150",
            "182",
            "342",
            "438",
        ],
        "correct_index": 2,
        "why": "Two aluminium give 54, three sulfur give 96 and twelve oxygen "
               "give 192, so the Mr is 342.",
    },
    {
        "id": "ks4-relative-formula-mass-h06",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Green crystals of hydrated iron(II) sulfate have the formula "
                "FeSO4.7H2O. Determine their relative formula mass. "
                "Ar: Fe = 56, S = 32, O = 16, H = 1.",
        "options": [
            "152",
            "170",
            "260",
            "278",
        ],
        "correct_index": 3,
        "why": "FeSO4 is 152 and seven water molecules add 126, giving "
               "152 + 126 = 278.",
    },
    {
        "id": "ks4-relative-formula-mass-h07",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ar: Mg = 24, N = 14, O = 16, S = 32. Determine how much "
                "larger the relative formula mass of magnesium nitrate, "
                "Mg(NO3)2, is than that of magnesium sulfate, MgSO4.",
        "options": [
            "28",
            "20",
            "36",
            "12",
        ],
        "correct_index": 0,
        "why": "Mg(NO3)2 is 148 and MgSO4 is 120, so the nitrate is larger by "
               "28.",
    },
    {
        "id": "ks4-relative-formula-mass-h08",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrated magnesium sulfate has the formula MgSO4.nH2O and a "
                "relative formula mass of 246. The Mr of MgSO4 is 120 and of "
                "water is 18. Determine the value of n.",
        "options": [
            "5",
            "7",
            "10",
            "14",
        ],
        "correct_index": 1,
        "why": "The water accounts for 246 − 120 = 126, and 126 ÷ 18 = 7 water "
               "molecules.",
    },
    {
        "id": "ks4-relative-formula-mass-h09",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The compound M2O3 has an Mr of 160. Taking Ar(O) as 16, "
                "determine the relative atomic mass of the element M.",
        "options": [
            "27",
            "48",
            "56",
            "112",
        ],
        "correct_index": 2,
        "why": "The three oxygen atoms account for 48, leaving 112 shared "
               "between two M atoms, so each is 56.",
    },
    {
        "id": "ks4-relative-formula-mass-h10",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "For 2H2 + O2 → 2H2O the Ar values are H = 1 and O = 16. "
                "Determine the total relative formula mass on each side of "
                "this equation.",
        "options": [
            "18 on the left and 18 on the right",
            "36 on the left and 18 on the right",
            "18 on the left and 36 on the right",
            "36 on the left and 36 on the right",
        ],
        "correct_index": 3,
        "why": "Two H2 and one O2 give 4 + 32 = 36, and two H2O give "
               "2 × 18 = 36, so the two sides match.",
    },
    {
        "id": "ks4-relative-formula-mass-h11",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium carbonate decomposes: MgCO3 → MgO + CO2. The Mr of "
                "MgCO3 is 84 and of MgO is 40, so 84 g of the carbonate gives "
                "40 g of the oxide. Calculate the mass of magnesium oxide "
                "made from 21 g of magnesium carbonate.",
        "options": [
            "10 g",
            "20 g",
            "8 g",
            "44 g",
        ],
        "correct_index": 0,
        "why": "21 g is a quarter of 84 g, so a quarter of the oxide forms: "
               "40 ÷ 4 = 10 g.",
    },
    {
        "id": "ks4-relative-formula-mass-h12",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydroxide of aluminium has a relative formula mass of 78. "
                "Ar: Al = 27, O = 16, H = 1. Determine its formula.",
        "options": [
            "AlOH",
            "Al(OH)3",
            "Al(OH)2",
            "Al2(OH)3",
        ],
        "correct_index": 1,
        "why": "78 − 27 = 51, and each OH group is 17, so three hydroxide "
               "groups are present.",
    },
    {
        "id": "ks4-relative-formula-mass-h13",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alkane has the general formula CnH2n+2 and a relative "
                "formula mass of 58. Ar: C = 12, H = 1. Determine the number "
                "of carbon atoms in one of its molecules.",
        "options": [
            "3",
            "5",
            "4",
            "6",
        ],
        "correct_index": 2,
        "why": "12n + 2n + 2 = 58 gives 14n = 56, so n = 4 and the alkane is "
               "C4H10.",
    },
    {
        "id": "ks4-relative-formula-mass-h14",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 2Al + Fe2O3 → Al2O3 + 2Fe, 54 g of aluminium reacts with "
                "iron(III) oxide to give 112 g of iron. Calculate the mass of "
                "aluminium needed to make 28 g of iron.",
        "options": [
            "6.75 g",
            "27 g",
            "54 g",
            "13.5 g",
        ],
        "correct_index": 3,
        "why": "28 g is a quarter of 112 g, so a quarter of the aluminium is "
               "needed: 54 ÷ 4 = 13.5 g.",
    },
    {
        "id": "ks4-relative-formula-mass-h15",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ar: Ca = 40, C = 12, O = 16, S = 32, H = 1, Cl = 35.5. "
                "Determine which of these calcium compounds has the largest "
                "relative formula mass.",
        "options": [
            "CaSO4",
            "CaCl2",
            "CaCO3",
            "Ca(OH)2",
        ],
        "correct_index": 0,
        "why": "CaSO4 is 136, ahead of CaCl2 at 111, CaCO3 at 100 and "
               "Ca(OH)2 at 74.",
    },
    {
        "id": "ks4-relative-formula-mass-h16",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student works out the relative formula mass of Ca(OH)2 as "
                "40 + 16 + 1 = 57. Ar: Ca = 40, O = 16, H = 1. Identify the "
                "error and give the correct value.",
        "options": [
            "The calcium was counted twice; the correct value is 97 instead",
            "The bracket subscript was ignored; the correct value is 74",
            "The hydrogen was left out of the sum entirely; the correct value "
            "is 58",
            "The oxygen was counted three times over; the correct value is 89 "
            "instead",
        ],
        "correct_index": 1,
        "why": "The 2 outside the bracket doubles both the O and the H, giving "
               "40 + 32 + 2 = 74.",
    },
    {
        "id": "ks4-relative-formula-mass-h17",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student works out the relative formula mass of CO2 as "
                "6 + 8 + 8 = 22. Identify the error in this method.",
        "options": [
            "Only one oxygen atom was counted rather than the two in CO2",
            "The atomic numbers were used in place of relative atomic masses",
            "The answer was halved at the end instead of being left alone",
            "The relative atomic masses of both elements were taken from the "
            "wrong group",
        ],
        "correct_index": 1,
        "why": "6 and 8 are the atomic numbers of carbon and oxygen; the "
               "relative atomic masses are 12 and 16, giving an Mr of 44.",
    },
    {
        "id": "ks4-relative-formula-mass-h18",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Photographic fixer contains Na2S2O3.5H2O. Determine its "
                "relative formula mass. Ar: Na = 23, S = 32, O = 16, H = 1.",
        "options": [
            "158",
            "203",
            "338",
            "248",
        ],
        "correct_index": 3,
        "why": "Na2S2O3 is 46 + 64 + 48 = 158 and five water molecules add "
               "90, giving 248.",
    },
    {
        "id": "ks4-relative-formula-mass-h19",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two fertilisers are compared. Ar: N = 14, H = 1, O = 16, "
                "K = 39. Determine which has the larger relative formula "
                "mass: ammonium nitrate, NH4NO3, or potassium nitrate, KNO3.",
        "options": [
            "Potassium nitrate, at 101 against 80 for ammonium nitrate",
            "Ammonium nitrate, at 80 against 67 for potassium nitrate",
            "They are equal, because each formula holds one nitrate group and "
            "nothing else",
            "Ammonium nitrate, at 98 against 101 for potassium nitrate",
        ],
        "correct_index": 0,
        "why": "KNO3 is 39 + 14 + 48 = 101 and NH4NO3 is 18 + 62 = 80, so the "
               "potassium salt has the larger Mr.",
    },
    {
        "id": "ks4-relative-formula-mass-h20",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Titanium is extracted by TiCl4 + 4Na → Ti + 4NaCl. The Mr of "
                "TiCl4 is 190 and the Ar of Ti is 48, so 190 g of TiCl4 "
                "yields 48 g of titanium. Calculate the mass of TiCl4 needed "
                "to make 12 g of titanium.",
        "options": [
            "760 g",
            "47.5 g",
            "3.0 g",
            "142.5 g",
        ],
        "correct_index": 1,
        "why": "12 g is a quarter of 48 g, so a quarter of the chloride is "
               "needed: 190 ÷ 4 = 47.5 g.",
    },
    {
        "id": "ks4-relative-formula-mass-h21",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "For CuCO3 → CuO + CO2 the Mr values are 123.5, 79.5 and 44. A "
                "student says these numbers prove that mass is lost on "
                "heating. Evaluate this claim.",
        "options": [
            "Correct, because the oxide left is lighter than the carbonate",
            "Correct, because the 44 is lost from the solid in the tube",
            "Wrong, because 79.5 + 44 = 123.5, so nothing has been lost at "
            "all",
            "Wrong, because the Mr values would have to be equal",
        ],
        "correct_index": 2,
        "why": "The two products add up to the reactant exactly, so all the "
               "mass is still present — the carbon dioxide has simply left "
               "the tube.",
    },
    {
        "id": "ks4-relative-formula-mass-h22",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium burns in nitrogen to form magnesium nitride, "
                "Mg3N2. Determine the relative formula mass of magnesium "
                "nitride. Ar: Mg = 24, N = 14.",
        "options": [
            "38",
            "86",
            "52",
            "100",
        ],
        "correct_index": 3,
        "why": "Three magnesium atoms give 72 and two nitrogen atoms give 28, "
               "so the Mr is 100.",
    },
    {
        "id": "ks4-relative-formula-mass-h23",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium carbonate has a relative formula mass of 100, of "
                "which the three oxygen atoms account for 48. Calculate the "
                "mass of oxygen contained in 250 g of calcium carbonate.",
        "options": [
            "120 g",
            "48 g",
            "202 g",
            "52 g",
        ],
        "correct_index": 0,
        "why": "48 out of every 100 units of mass is oxygen, so 250 g holds "
               "250 × 0.48 = 120 g of oxygen.",
    },
    {
        "id": "ks4-relative-formula-mass-h24",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium hydroxide, NaOH, and sodium hydride, NaH, are both "
                "white solids. Ar: Na = 23, O = 16, H = 1. Determine the "
                "difference between their relative formula masses.",
        "options": [
            "15",
            "16",
            "17",
            "24",
        ],
        "correct_index": 1,
        "why": "NaOH is 40 and NaH is 24, so the difference is the oxygen "
               "atom: 16.",
    },
    {
        "id": "ks4-relative-formula-mass-h25",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the Haber process N2 + 3H2 → 2NH3, 28 g of nitrogen gives "
                "34 g of ammonia. Calculate the mass of nitrogen needed to "
                "make 170 g of ammonia.",
        "options": [
            "34 g",
            "85 g",
            "140 g",
            "206 g",
        ],
        "correct_index": 2,
        "why": "170 g is five times 34 g, so five times the nitrogen is "
               "needed: 28 × 5 = 140 g.",
    },
    {
        "id": "ks4-relative-formula-mass-h26",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In sodium chloride, 35.5 of every 58.5 units of relative "
                "formula mass is chlorine; in calcium chloride it is 71 of "
                "every 111. Determine which 100 g sample holds more "
                "chlorine.",
        "options": [
            "Sodium chloride, because its formula mass is smaller",
            "Sodium chloride, because each formula unit holds one chlorine",
            "They hold the same mass, because both samples weigh exactly "
            "100 g",
            "Calcium chloride, because 64% of its formula mass is chlorine "
            "against 61%",
        ],
        "correct_index": 3,
        "why": "71 ÷ 111 is 64% while 35.5 ÷ 58.5 is 61%, so 100 g of calcium "
               "chloride holds about 3 g more chlorine.",
    },
]
