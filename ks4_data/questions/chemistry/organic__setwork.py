"""Chemistry · Organic chemistry — the MRB-335 extension.

`organic.py` holds the frozen twelve per subtopic that the AUTOMATIC weekly
assignment composes from. This file adds the rows Set work v2 needed: the
7 Sep 2026 table showed Combined Foundation at 48 and Combined HIGHER at 32,
because only four of this topic's twelve subtopics are on the Combined
pathway at all — the alkene chemistry, the alcohols, the acids and both
polymer subtopics are Triple.

So the additions land entirely on those four — `crude-oil-hydrocarbons`,
`fractional-distillation`, `properties-of-hydrocarbons`, `cracking-alkenes` —
and lean towards `standard` and `harder`, because the Higher cell of a base
topic is fed only by those two bands. Foundation gains from every row here;
Higher gains from seven of the eight in each subtopic.

⚠️ NOT USED HERE, deliberately: the hydration of ethene to ethanol and
addition polymerisation. Both appear in the base page's equations block, and
both belong to Triple-only subtopics under `ks4_data.classify()`. A base row
that examined them would put Chemistry-only content in front of a Foundation
Combined class, which is the exact failure the content rule exists to stop.
"""

TOPIC = "organic"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── crude-oil-hydrocarbons ────────────────── BASE (5.7.1.1) ── +8 ──
    {
        "id": "ks4-crude-oil-hydrocarbons-e05",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the elements present in a hydrocarbon.",
        "options": [
            "Carbon and oxygen only",
            "Carbon, hydrogen and oxygen",
            "Carbon and hydrogen only",
            "Hydrogen and oxygen only",
        ],
        "correct_index": 2,
        "why": "A hydrocarbon is a compound of carbon and hydrogen and "
               "nothing else — one oxygen atom and it is no longer a "
               "hydrocarbon.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s05",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why crude oil is described as a finite resource.",
        "options": [
            "It took millions of years to form and is being used far faster "
            "than it is replaced",
            "It is found in only a small number of countries",
            "It is a mixture rather than a single compound, so it cannot be "
            "replaced",
            "It has to be separated before any of it can be used",
        ],
        "correct_index": 0,
        "why": "Finite means the supply is limited: crude oil forms over "
               "millions of years and we are removing it very much faster "
               "than that.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s06",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alkane molecule contains 20 hydrogen atoms. Determine "
                "the number of carbon atoms in the molecule.",
        "options": [
            "10",
            "11",
            "18",
            "9",
        ],
        "correct_index": 3,
        "why": "Alkanes fit CnH2n+2, so 2n + 2 = 20 gives n = 9 and the "
               "molecule is C9H20.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s07",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of carbon dioxide molecules formed when "
                "one molecule of methane, CH4, burns completely with the "
                "number formed when one molecule of butane, C4H10, burns "
                "completely.",
        "options": [
            "Both give 1, because both are alkanes",
            "Methane gives 1 and butane gives 4, because each carbon atom "
            "becomes one CO2",
            "Methane gives 1 and butane gives 10, one for each hydrogen atom",
            "Methane gives 4 and butane gives 1",
        ],
        "correct_index": 1,
        "why": "Every carbon atom in the fuel ends up in one molecule of "
               "carbon dioxide, so the count follows the number of carbons.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s08",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alkanes do not decolourise bromine water.",
        "options": [
            "They are too unreactive to dissolve in water",
            "The bromine reacts with their hydrogen atoms instead of the "
            "carbon ones",
            "They already contain bromine atoms",
            "They are saturated — every carbon-carbon bond is single, so "
            "nothing can add across one",
        ],
        "correct_index": 3,
        "why": "Bromine water is decolourised when bromine adds across a C=C "
               "double bond, and an alkane has no double bond to add across.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h05",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One molecule of a hydrocarbon burns completely to give 3 "
                "molecules of carbon dioxide and 4 molecules of water. "
                "Deduce its molecular formula.",
        "options": [
            "C3H8",
            "C3H4",
            "C3H6",
            "C4H3",
        ],
        "correct_index": 0,
        "why": "3 CO2 accounts for 3 carbon atoms and 4 H2O for 8 hydrogen "
               "atoms, so the fuel was C3H8.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h06",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the mass of carbon dioxide produced when 1 mol of "
                "methane, CH4, burns completely with the mass produced when "
                "1 mol of ethane, C2H6, burns completely. Relative atomic "
                "masses: C 12, O 16.",
        "options": [
            "44 g and 44 g",
            "16 g and 30 g",
            "88 g and 44 g",
            "44 g and 88 g",
        ],
        "correct_index": 3,
        "why": "Methane gives 1 mol of CO2 (44 g) and ethane gives 2 mol "
               "(88 g), because ethane has twice as many carbon atoms.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h07",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas heater in a poorly ventilated room burns with a "
                "yellow flame and releases less energy per gram of fuel than "
                "the manufacturer states. Explain both observations.",
        "options": [
            "The flame is cooled by the nitrogen in the room, which absorbs "
            "a large part of the energy released",
            "A restricted air supply gives incomplete combustion: glowing "
            "carbon colours the flame and less energy is released",
            "The fuel burns too fast for all its energy to escape, which "
            "colours the flame",
            "Water vapour from the flame puts out part of the burner, "
            "wasting fuel",
        ],
        "correct_index": 1,
        "why": "Both come from the same cause: too little oxygen, so carbon "
               "is left unburned as soot rather than being oxidised fully to "
               "carbon dioxide.",
    },

    # ── fractional-distillation ───────────────── BASE (5.7.1.2) ── +8 ──
    {
        "id": "ks4-fractional-distillation-e05",
        "subtopic_slug": "fractional-distillation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate temperature to which crude oil is "
                "heated before it enters the fractionating column.",
        "options": [
            "About 25 °C",
            "About 100 °C",
            "About 350 °C",
            "About 1500 °C",
        ],
        "correct_index": 2,
        "why": "Around 350 °C vaporises almost all of the crude oil, leaving "
               "only the bitumen residue behind.",
    },
    {
        "id": "ks4-fractional-distillation-s05",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to a hydrocarbon vapour as it rises "
                "through the fractionating column.",
        "options": [
            "It heats up, and boils at the level where the temperature "
            "equals its boiling point",
            "It cools, and freezes to a solid near the top of the column",
            "It stays at the same temperature the whole way up",
            "It cools, and condenses to a liquid at the level where the "
            "temperature equals its boiling point",
        ],
        "correct_index": 3,
        "why": "The column is hot at the bottom and cool at the top, so each "
               "vapour turns back to a liquid at the height that matches its "
               "own boiling point.",
    },
    {
        "id": "ks4-fractional-distillation-s06",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Naphtha contains hydrocarbons with 5 to 10 carbon atoms; "
                "fuel oil contains 20 to 70. Predict which is collected "
                "higher in the column and which is more flammable.",
        "options": [
            "Naphtha is collected higher and naphtha is more flammable",
            "Fuel oil is collected higher and fuel oil is more flammable",
            "Naphtha is collected higher but fuel oil is more flammable",
            "Fuel oil is collected higher but naphtha is more flammable",
        ],
        "correct_index": 0,
        "why": "Shorter chains have lower boiling points, so they rise "
               "further before condensing, and they are more volatile and so "
               "easier to ignite.",
    },
    {
        "id": "ks4-fractional-distillation-s07",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why fractional distillation gives fractions rather "
                "than pure single compounds.",
        "options": [
            "Each fraction holds several hydrocarbons with boiling points "
            "close enough to condense together",
            "The column is never tall enough to separate any of the "
            "hydrocarbons",
            "The hydrocarbons react with one another as they rise, forming "
            "new mixtures",
            "A pure compound can never be obtained from a mixture by any "
            "method",
        ],
        "correct_index": 0,
        "why": "Crude oil contains hundreds of hydrocarbons with boiling "
               "points only degrees apart, so a level of the column collects "
               "a group of them rather than one.",
    },
    {
        "id": "ks4-fractional-distillation-s08",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Diesel is collected where the column is at about 300 °C. "
                "Predict where a hydrocarbon that boils at 150 °C is "
                "collected, and explain why.",
        "options": [
            "Lower down, where it is hotter, because it condenses more "
            "easily than diesel",
            "Higher up, where it is cooler, because it stays a vapour until "
            "the temperature falls to 150 °C",
            "At the same level, because both are liquids at room temperature",
            "At the base as residue, because it does not vaporise at all",
        ],
        "correct_index": 1,
        "why": "A vapour only condenses once the column has cooled to its own "
               "boiling point, so a lower boiling point means a higher "
               "collection level.",
    },
    {
        "id": "ks4-fractional-distillation-h05",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two refineries distil the same crude oil, one using a "
                "column 20 m tall and one using a column 5 m tall, with the "
                "same base temperature. Predict which separates the "
                "fractions better and explain why.",
        "options": [
            "The 5 m column, because the vapours reach the top before they "
            "can mix again",
            "Both separate equally well, because the boiling points do not "
            "change with the height of the column",
            "The 5 m column, because a shorter path means less energy is "
            "lost",
            "The 20 m column, because the temperature falls more gradually "
            "and vapours condense and re-evaporate many more times",
        ],
        "correct_index": 3,
        "why": "A taller column gives a gentler temperature gradient, so "
               "hydrocarbons with similar boiling points get many more "
               "chances to separate from one another.",
    },
    {
        "id": "ks4-fractional-distillation-h06",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fraction G is a thick liquid that is hard to set alight; "
                "fraction H is runny and catches fire easily. Deduce which "
                "was collected nearer the base of the column, justifying "
                "your answer with both properties.",
        "options": [
            "G, because high viscosity and low flammability both point to "
            "long chains and a high boiling point",
            "H, because runny liquids sink to the base of the column",
            "G, because viscous liquids vaporise first and condense last",
            "H, because a fraction that ignites easily must condense where "
            "the column is hottest",
        ],
        "correct_index": 0,
        "why": "Viscosity rises and flammability falls as chains get longer, "
               "and long chains have the highest boiling points, so they "
               "condense lowest.",
    },
    {
        "id": "ks4-fractional-distillation-h07",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crude oil sample contains a hydrocarbon with 18 carbon "
                "atoms and one with 4. Compare their collection points, "
                "their states at room temperature and their viscosities.",
        "options": [
            "The C18 condenses higher, is a gas at room temperature and is "
            "less viscous",
            "The C4 condenses lower, is a liquid at room temperature and is "
            "the more viscous of the two",
            "The C18 condenses lower, is a solid or thick liquid at room "
            "temperature and is far more viscous",
            "Both condense at the same level and both are liquids of "
            "similar viscosity",
        ],
        "correct_index": 2,
        "why": "Chains of 18 carbons boil well above room temperature, so "
               "they condense low in the column and are viscous solids or "
               "near-solids; C4 is a gas.",
    },

    # ── properties-of-hydrocarbons ────────────── BASE (5.7.1.3) ── +8 ──
    {
        "id": "ks4-properties-of-hydrocarbons-e05",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "As the carbon chains in a hydrocarbon get longer, state "
                "what happens to how easily it ignites.",
        "options": [
            "It increases steadily",
            "It decreases steadily",
            "It stays the same",
            "It increases and then decreases",
        ],
        "correct_index": 1,
        "why": "Longer chains are less volatile, so less vapour forms above "
               "the liquid and the fuel is harder to ignite.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s05",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hexane has 6 carbon atoms per molecule and eicosane has 20. "
                "Predict which pours more easily at room temperature and "
                "explain why.",
        "options": [
            "Eicosane, because longer molecules slide past one another more "
            "easily",
            "Hexane, because it has the higher boiling point of the two",
            "Hexane, because shorter chains are less viscous and flow more "
            "easily",
            "Eicosane, because heavier molecules flow faster under gravity",
        ],
        "correct_index": 2,
        "why": "Long chains tangle around one another, so viscosity rises "
               "with chain length and the shorter hexane is much runnier.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s06",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why petrol must be kept in a sealed container away "
                "from any flame.",
        "options": [
            "It is volatile, so it evaporates readily and its vapour forms "
            "a flammable mixture with air",
            "It is viscous, so it spreads quickly across a surface once it "
            "has been spilled",
            "It has a high boiling point, so it stores a great deal of "
            "energy",
            "It reacts with oxygen in the air even when there is no flame",
        ],
        "correct_index": 0,
        "why": "It is the vapour above the liquid that ignites, and petrol's "
               "short chains make it evaporate readily at room temperature.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s07",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydrocarbon has 22 carbon atoms per molecule. Predict its "
                "state at room temperature and whether it would work as a "
                "petrol engine fuel, explaining your answer.",
        "options": [
            "A gas, and unsuitable, because it would leak out of the fuel "
            "tank",
            "A runny liquid, and suitable, because long chains burn most "
            "easily",
            "A solid, and suitable, because solids store the most energy "
            "for each gram burned",
            "A solid or thick liquid, and unsuitable, because it is not "
            "volatile enough to vaporise and ignite",
        ],
        "correct_index": 3,
        "why": "Chains of 18 carbons and above are solids at room "
               "temperature, and a petrol engine needs a fuel that "
               "vaporises before the spark reaches it.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s08",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One molecule of fuel J contains 8 carbon atoms and one "
                "molecule of fuel K contains 12. Both burn completely. "
                "Predict which produces more carbon dioxide per molecule "
                "burned, and explain.",
        "options": [
            "J, because shorter molecules burn more completely",
            "K, because each of its 12 carbon atoms forms one molecule of "
            "carbon dioxide",
            "They produce the same amount, because both burn completely",
            "J, because it is more volatile so more of it burns",
        ],
        "correct_index": 1,
        "why": "Complete combustion turns every carbon atom into one carbon "
               "dioxide molecule, so the count follows the chain length.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h05",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrocarbon T boils at 36 °C and hydrocarbon U boils at "
                "216 °C. Deduce which is more suitable for an aircraft fuel "
                "that must not evaporate from the tank at altitude, and "
                "explain.",
        "options": [
            "T, because a low boiling point means it ignites more reliably",
            "T, because volatile fuels are safer in a very cold tank",
            "U, because its longer chains make it far less volatile, so "
            "little of it evaporates away",
            "U, because a high boiling point means it stores more energy per "
            "gram",
        ],
        "correct_index": 2,
        "why": "A boiling point of 216 °C means very little vapour forms at "
               "the temperatures a fuel tank reaches, so the fuel stays in "
               "the tank.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h06",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Bitumen must be the best fuel, "
                "because its molecules are the biggest and so store the most "
                "energy.'",
        "options": [
            "It is right — the largest molecules always release the most "
            "energy for each gram burned",
            "It is wrong — a fuel must also vaporise and ignite, and "
            "bitumen is far too involatile to burn in a burner",
            "It is wrong — larger molecules store less energy per gram than "
            "smaller ones do",
            "It is right, but bitumen is simply too expensive to use as a "
            "fuel",
        ],
        "correct_index": 1,
        "why": "Being a good fuel is about ease of ignition as well as "
               "energy content, and bitumen barely vaporises at all.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h07",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alkane with n carbon atoms burns completely to give n "
                "molecules of carbon dioxide and (n + 1) molecules of water. "
                "Deduce the number of oxygen molecules needed per molecule "
                "of the alkane.",
        "options": [
            "(3n + 1)",
            "(n + 1) ÷ 2",
            "(2n + 1) ÷ 2",
            "(3n + 1) ÷ 2",
        ],
        "correct_index": 3,
        "why": "The products hold 2n + (n + 1) = 3n + 1 oxygen ATOMS, and "
               "each O2 molecule supplies two of them.",
    },

    # ── cracking-alkenes ──────────────────────── BASE (5.7.1.4) ── +8 ──
    {
        "id": "ks4-cracking-alkenes-e05",
        "subtopic_slug": "cracking-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the bond that makes an alkene unsaturated.",
        "options": [
            "A carbon-carbon double bond",
            "A carbon-hydrogen single bond",
            "A carbon-carbon single bond",
            "A carbon-oxygen double bond",
        ],
        "correct_index": 0,
        "why": "Unsaturated means the molecule contains a C=C double bond "
               "that other atoms can add across.",
    },
    {
        "id": "ks4-cracking-alkenes-s05",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cracking C14H30 gives one molecule of C8H18 and two "
                "molecules of the same alkene. Determine the formula of the "
                "alkene.",
        "options": [
            "C2H4",
            "C6H12",
            "C3H6",
            "C3H8",
        ],
        "correct_index": 2,
        "why": "C14H30 minus C8H18 leaves C6H12, and splitting that between "
               "two identical molecules gives C3H6.",
    },
    {
        "id": "ks4-cracking-alkenes-s06",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas made by cracking turns bromine water from orange to "
                "colourless. Deduce what this shows about the gas and give "
                "its general formula.",
        "options": [
            "It is saturated, with only single bonds, and fits CnH2n+2",
            "It is unsaturated, containing a C=C bond, and fits CnH2n",
            "It is an alkane, and fits CnH2n",
            "It is unsaturated, and fits CnH2n+2",
        ],
        "correct_index": 1,
        "why": "Only a C=C double bond decolourises bromine water, and the "
               "alkenes that contain one fit the general formula CnH2n.",
    },
    {
        "id": "ks4-cracking-alkenes-s07",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a catalyst is used in catalytic cracking.",
        "options": [
            "It raises the temperature needed, so more alkenes are produced",
            "It is used up as the reaction proceeds, so it must be topped up "
            "constantly",
            "It joins the alkane molecules together before they break apart",
            "It lowers the activation energy, so cracking works at a lower "
            "pressure and costs less to run",
        ],
        "correct_index": 3,
        "why": "The zeolite catalyst lowers the energy barrier, which is why "
               "catalytic cracking needs neither the very high pressure nor "
               "the extreme temperature of thermal cracking.",
    },
    {
        "id": "ks4-cracking-alkenes-s08",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A refinery cracks 100 tonnes of a long-chain fraction and "
                "collects shorter alkanes together with alkenes. Explain why "
                "the total mass of the products is also 100 tonnes.",
        "options": [
            "Cracking only rearranges the atoms that are already there, and "
            "mass is conserved in a chemical reaction",
            "Some mass is lost as heat, but the catalyst replaces it",
            "The alkenes weigh less than the alkanes, so extra alkane is "
            "made to make up the difference",
            "Mass is conserved only when a catalyst is used",
        ],
        "correct_index": 0,
        "why": "No atoms are created or destroyed when the chains break, so "
               "the products together have the same mass as the fraction "
               "that went in.",
    },
    {
        "id": "ks4-cracking-alkenes-h05",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "C16H34 is cracked into one alkane and two molecules of "
                "ethene, C2H4. Deduce the formula of the alkane.",
        "options": [
            "C12H24",
            "C12H26",
            "C14H30",
            "C12H22",
        ],
        "correct_index": 1,
        "why": "Two ethene molecules account for C4H8, and C16H34 minus C4H8 "
               "leaves C12H26.",
    },
    {
        "id": "ks4-cracking-alkenes-h06",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Liquid paraffin is cracked over hot broken pot in a test "
                "tube and the gas is collected over water. Explain why the "
                "delivery tube must be lifted out of the water before the "
                "heating is stopped.",
        "options": [
            "The gas would react with the water and be lost from the "
            "collecting tube entirely",
            "The water would put out the Bunsen flame",
            "The gas inside cools and contracts, so water is drawn back "
            "onto the hot glass and could crack it",
            "The broken pot would dissolve in the water and stop working",
        ],
        "correct_index": 2,
        "why": "Cooling gas takes up less space, so cold water is sucked "
               "back up the tube onto glass that is still very hot.",
    },
    {
        "id": "ks4-cracking-alkenes-h07",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Catalytic cracking is always the "
                "better choice, so thermal cracking should never be used.'",
        "options": [
            "Always true — a catalyst makes every reaction cheaper and "
            "faster, and it has no drawbacks at all",
            "Never true — thermal cracking is cheaper because it needs no "
            "catalyst at all",
            "Always true — catalytic cracking is the only method that "
            "produces alkenes",
            "Not always — catalytic cracking is cheaper to run, but thermal "
            "cracking gives more of the alkenes industry needs",
        ],
        "correct_index": 3,
        "why": "The two methods are chosen for different products: "
               "catalytic for branched alkanes for petrol, thermal when a "
               "high yield of alkenes is wanted.",
    },
]
