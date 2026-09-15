"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`amounts-in-equations`.

AQA 5.3.2.2, taken wide rather than deep: coefficients read as a ratio of
moles, in both directions, across combination, decomposition, combustion,
displacement and neutralisation, and with ratios that are 1 : 1, 1 : 2, 2 : 3,
4 : 2 and 2 : 1. The standard band runs the full mass-to-mass method; the
harder band layers purity, percentage yield and a second reaction step on top
of it, and works backwards from a product mass to an unknown Ar or a mass of
reactant.

⚠️ HIGHER TIER, both pathways. Every row turns on a molar ratio taken from a
balanced equation printed in the stem — there is no limiting-reactant work
here, which belongs to `using-moles-calculations`.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # easier ----------------------------------------------------------
    {
        "id": 'ks4-amounts-in-equations-e05',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'In the equation N2 + 3H2 → 2NH3, state the ratio of moles '
                'of nitrogen to moles of ammonia.',
        "options": [
            '1 : 2',
            '1 : 3',
            '2 : 1',
            '3 : 2',
        ],
        "correct_index": 0,
        "why": 'The coefficients are 1 for nitrogen and 2 for ammonia, so '
               'the ratio is 1 : 2.',
    },
    {
        "id": 'ks4-amounts-in-equations-e06',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For CaCO3 + 2HCl → CaCl2 + H2O + CO2, calculate the amount '
                'of hydrochloric acid needed to react completely with 0.30 '
                'mol of calcium carbonate.',
        "options": [
            '2.0 mol',
            '0.60 mol',
            '0.30 mol',
            '0.15 mol',
        ],
        "correct_index": 1,
        "why": 'The equation needs two moles of acid for each mole of '
               'carbonate, so 0.30 × 2 = 0.60 mol.',
    },
    {
        "id": 'ks4-amounts-in-equations-e07',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what the coefficients in a balanced equation tell a '
                'chemist about the substances in it.',
        "options": [
            'The ratio of the volumes in cm³ in which they react',
            'The number of atoms in one particle of each of them',
            'The ratio of the amounts in moles in which they react',
            'The ratio of the masses in grams in which they react',
        ],
        "correct_index": 2,
        "why": 'A coefficient counts moles, so the coefficients together '
               'give the molar ratio in which the substances react.',
    },
    {
        "id": 'ks4-amounts-in-equations-e08',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For 2Mg + O2 → 2MgO, calculate the amount of magnesium '
                'oxide made from 0.50 mol of magnesium.',
        "options": [
            '1.00 mol',
            '0.25 mol',
            '2.00 mol',
            '0.50 mol',
        ],
        "correct_index": 3,
        "why": 'Magnesium and magnesium oxide are in a 2 : 2, or 1 : 1, '
               'ratio, so 0.50 mol of magnesium gives 0.50 mol of oxide.',
    },
    {
        "id": 'ks4-amounts-in-equations-e09',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For Cl2 + 2KI → 2KCl + I2, calculate the amount of iodine '
                'made when 0.40 mol of potassium iodide reacts completely.',
        "options": [
            '0.10 mol',
            '0.20 mol',
            '0.40 mol',
            '0.80 mol',
        ],
        "correct_index": 1,
        "why": 'Two moles of potassium iodide give one mole of iodine, so '
               '0.40 ÷ 2 = 0.20 mol.',
    },
    {
        "id": 'ks4-amounts-in-equations-e10',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State why the mass of a reactant cannot be put straight '
                'into the molar ratio taken from an equation.',
        "options": [
            'The ratio changes whenever the mass of reactant used is changed',
            'Masses must first be turned into percentages before a ratio '
            'can be used',
            'The ratio counts particles, and equal masses hold different '
            'numbers of them',
            'The ratio counts particles, and a mass in grams is always too '
            'large a number',
        ],
        "correct_index": 2,
        "why": 'Coefficients give a ratio of moles, so a mass has to be '
               'divided by the Mr to become a number of particles first.',
    },
    {
        "id": 'ks4-amounts-in-equations-e11',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For 2Fe2O3 + 3C → 4Fe + 3CO2, calculate the amount of '
                'carbon dioxide made when 0.20 mol of iron(III) oxide '
                'reacts completely.',
        "options": [
            '0.20 mol',
            '0.13 mol',
            '0.60 mol',
            '0.30 mol',
        ],
        "correct_index": 3,
        "why": 'Two moles of iron(III) oxide give three moles of carbon '
               'dioxide, so 0.20 × 3 ÷ 2 = 0.30 mol.',
    },
    {
        "id": 'ks4-amounts-in-equations-e12',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For Zn + 2HCl → ZnCl2 + H2, state the amount of hydrogen '
                'made when one mole of zinc reacts completely.',
        "options": [
            '1 mol',
            '2 mol',
            '0.5 mol',
            '4 mol',
        ],
        "correct_index": 0,
        "why": 'Zinc and hydrogen each carry a coefficient of 1, so one '
               'mole of zinc gives one mole of hydrogen.',
    },
    {
        "id": 'ks4-amounts-in-equations-e13',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For C + O2 → CO2, calculate the mass of carbon dioxide '
                'made when 1.00 mol of carbon burns completely. Mr of CO2 = '
                '44.',
        "options": [
            '32.0 g',
            '88.0 g',
            '44.0 g',
            '12.0 g',
        ],
        "correct_index": 2,
        "why": 'One mole of carbon gives one mole of CO2, and one mole of '
               'CO2 has a mass of 44.0 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-e14',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what happens to the molar ratio in an equation when '
                'twice as much of each reactant is used.',
        "options": [
            'It doubles, because twice as many moles of each are reacting',
            'It halves, because the coefficients are shared out over more '
            'moles',
            'It cannot be worked out until the masses used are known',
            'It never changes, because it is fixed by the balanced equation',
        ],
        "correct_index": 3,
        "why": 'The coefficients are set by the balanced equation, so the '
               'ratio stays the same whatever quantities are used.',
    },
    {
        "id": 'ks4-amounts-in-equations-e15',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For 2C2H6 + 7O2 → 4CO2 + 6H2O, state the amount of carbon '
                'dioxide made when 2 mol of ethane burns completely.',
        "options": [
            '4 mol',
            '2 mol',
            '6 mol',
            '7 mol',
        ],
        "correct_index": 0,
        "why": 'The coefficients are 2 for ethane and 4 for carbon dioxide, '
               'so 2 mol of ethane gives 4 mol of CO2.',
    },
    {
        "id": 'ks4-amounts-in-equations-e16',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the amount of water made when 0.10 mol of '
                'ethanol burns completely in C2H5OH + 3O2 → 2CO2 + 3H2O.',
        "options": [
            '0.10 mol',
            '0.30 mol',
            '0.20 mol',
            '0.60 mol',
        ],
        "correct_index": 1,
        "why": 'Each mole of ethanol gives three moles of water, so 0.10 × '
               '3 = 0.30 mol.',
    },
    {
        "id": 'ks4-amounts-in-equations-e17',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what must be true of an equation before its '
                'coefficients can be used as a molar ratio.',
        "options": [
            'It must have state symbols written after every formula',
            'It must have the same number of formulae on each side',
            'It must show the reactants in the order they were added',
            'It must be balanced, with the same atoms on each side',
        ],
        "correct_index": 3,
        "why": 'Only a balanced equation gives the true ratio of moles, '
               'because balancing is what makes the atoms on each side '
               'match.',
    },
    {
        "id": 'ks4-amounts-in-equations-e18',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'For 2Al + 6HCl → 2AlCl3 + 3H2, calculate the amount of '
                'hydrogen gas made when 0.60 mol of aluminium reacts '
                'completely.',
        "options": [
            '1.80 mol',
            '0.40 mol',
            '0.90 mol',
            '0.60 mol',
        ],
        "correct_index": 2,
        "why": 'Two moles of aluminium give three moles of hydrogen, so '
               '0.60 × 3 ÷ 2 = 0.90 mol.',
    },
    # standard --------------------------------------------------------
    {
        "id": 'ks4-amounts-in-equations-s05',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Hydrogen peroxide decomposes: 2H2O2 → 2H2O + O2. Mr of '
                'H2O2 = 34 and Mr of O2 = 32. Calculate the mass of oxygen '
                'gas made when 6.8 g of hydrogen peroxide decomposes '
                'completely.',
        "options": [
            '3.2 g',
            '6.4 g',
            '1.6 g',
            '0.10 g',
        ],
        "correct_index": 0,
        "why": 'n(H2O2) = 6.8 ÷ 34 = 0.20 mol, the 2 : 1 ratio gives 0.10 '
               'mol of O2, and 0.10 × 32 = 3.2 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s06',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Lithium reacts with water: 2Li + 2H2O → 2LiOH + H2. Ar of '
                'Li = 7 and Mr of H2 = 2. Calculate the mass of hydrogen '
                'made when 2.8 g of lithium reacts completely.',
        "options": [
            '2.8 g',
            '0.40 g',
            '0.80 g',
            '0.20 g',
        ],
        "correct_index": 1,
        "why": 'n(Li) = 2.8 ÷ 7 = 0.40 mol, two moles of lithium give one '
               'of hydrogen, so 0.20 × 2 = 0.40 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s07',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Copper(II) oxide is reduced by hydrogen: CuO + H2 → Cu + '
                'H2O. Mr of CuO = 79.5 and Ar of Cu = 63.5. Calculate the '
                'mass of copper(II) oxide needed to make 12.7 g of copper.',
        "options": [
            '31.8 g',
            '7.95 g',
            '15.9 g',
            '12.7 g',
        ],
        "correct_index": 2,
        "why": 'n(Cu) = 12.7 ÷ 63.5 = 0.200 mol, the ratio is 1 : 1, so the '
               'mass of CuO is 0.200 × 79.5 = 15.9 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s08',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Ammonia burns in oxygen: 4NH3 + 3O2 → 2N2 + 6H2O. Mr of '
                'NH3 = 17 and Mr of N2 = 28. Calculate the mass of nitrogen '
                'made when 13.6 g of ammonia burns completely.',
        "options": [
            '22.4 g',
            '5.6 g',
            '13.6 g',
            '11.2 g',
        ],
        "correct_index": 3,
        "why": 'n(NH3) = 13.6 ÷ 17 = 0.80 mol, four moles of ammonia give '
               'two of nitrogen, so 0.40 × 28 = 11.2 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s09',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student burns 2.4 g of magnesium in 2Mg + O2 → 2MgO. '
                'They apply the 2 : 2 ratio to the mass and write 2.4 g of '
                'magnesium oxide. Ar of Mg = 24 and Mr of MgO = 40. '
                'Identify the error.',
        "options": [
            'Nothing is wrong, because a 2 : 2 ratio means the masses are '
            'equal too',
            'A ratio applies to moles, not masses: 0.10 mol gives 4.0 g of '
            'oxide',
            'The 2 : 2 ratio should have been halved, so the answer is 1.2 g',
            'Magnesium and oxygen react in a 1 : 1 mass ratio, so it is 4.8 g',
        ],
        "correct_index": 1,
        "why": 'The ratio counts moles: n(Mg) = 2.4 ÷ 24 = 0.10 mol, so '
               '0.10 mol of MgO forms, with a mass of 0.10 × 40 = 4.0 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s10',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Sulfur dioxide is oxidised in the Contact process: 2SO2 + '
                'O2 → 2SO3. Mr of SO2 = 64 and Mr of SO3 = 80. Calculate '
                'the mass of sulfur trioxide made from 12.8 g of sulfur '
                'dioxide.',
        "options": [
            '8.0 g',
            '32.0 g',
            '16.0 g',
            '12.8 g',
        ],
        "correct_index": 2,
        "why": 'n(SO2) = 12.8 ÷ 64 = 0.200 mol, the SO2 : SO3 ratio is 1 : '
               '1, so the mass is 0.200 × 80 = 16.0 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s11',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'In 2H2 + O2 → 2H2O, 4.0 g of hydrogen reacts with 32 g of '
                'oxygen to give 36 g of water. Determine the mass of water '
                'made when 1.0 g of hydrogen reacts with excess oxygen.',
        "options": [
            '36 g',
            '18 g',
            '4.5 g',
            '9.0 g',
        ],
        "correct_index": 3,
        "why": '1.0 g of hydrogen is a quarter of 4.0 g, so a quarter of '
               'the water forms: 36 ÷ 4 = 9.0 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s12',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calcium reacts with water: Ca + 2H2O → Ca(OH)2 + H2. Ar of '
                'Ca = 40 and Mr of Ca(OH)2 = 74. Calculate the mass of '
                'calcium hydroxide made when 4.0 g of calcium reacts '
                'completely.',
        "options": [
            '7.4 g',
            '3.7 g',
            '14.8 g',
            '4.0 g',
        ],
        "correct_index": 0,
        "why": 'n(Ca) = 4.0 ÷ 40 = 0.10 mol, the ratio is 1 : 1, so the '
               'mass is 0.10 × 74 = 7.4 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s13',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Excess dilute hydrochloric acid is added to 5.0 g of '
                'calcium carbonate: CaCO3 + 2HCl → CaCl2 + H2O + CO2. '
                'Explain why the mass of carbon dioxide made can be '
                'calculated without knowing how much acid was used.',
        "options": [
            'Carbon dioxide comes only from the acid, whose amount is '
            'unlimited here',
            'The two reactants are in a 1 : 1 ratio, so their masses must '
            'be equal',
            'The carbonate runs out first, so it alone fixes the amount of '
            'product',
            'The acid takes no part in the reaction and is only there as a '
            'solvent',
        ],
        "correct_index": 2,
        "why": 'With the acid in excess the carbonate is used up first, so '
               'the amount of carbonate decides how much carbon dioxide '
               'forms.',
    },
    {
        "id": 'ks4-amounts-in-equations-s14',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'The thermite reaction is Fe2O3 + 2Al → 2Fe + Al2O3. Ar of '
                'Al = 27 and Ar of Fe = 56. Calculate the mass of iron made '
                'when 10.8 g of aluminium reacts completely.',
        "options": [
            '11.2 g',
            '44.8 g',
            '10.8 g',
            '22.4 g',
        ],
        "correct_index": 3,
        "why": 'n(Al) = 10.8 ÷ 27 = 0.400 mol, aluminium and iron are in a '
               '2 : 2 ratio, so 0.400 × 56 = 22.4 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s15',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'When 0.20 mol of a metal M reacts completely with dilute '
                'hydrochloric acid it makes 0.30 mol of hydrogen gas. '
                'Determine the balanced equation for the reaction.',
        "options": [
            '2M + 6HCl → 2MCl3 + 3H2',
            'M + 2HCl → MCl2 + H2',
            '2M + 2HCl → 2MCl + H2',
            'M + 3HCl → MCl3 + 3H2',
        ],
        "correct_index": 0,
        "why": 'The 0.20 : 0.30 ratio of metal to hydrogen simplifies to 2 '
               ': 3, which only 2M + 6HCl → 2MCl3 + 3H2 matches.',
    },
    {
        "id": 'ks4-amounts-in-equations-s16',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Compare the mass of carbon dioxide made when 0.10 mol of '
                'calcium carbonate is heated with the mass made when 0.10 '
                'mol of magnesium carbonate is heated. Both decompose in a '
                '1 : 1 ratio and Mr of CO2 = 44.',
        "options": [
            'Neither can be worked out without the mass of each carbonate '
            'in grams',
            'Both make 4.4 g, because each gives 0.10 mol of carbon dioxide',
            'Calcium carbonate makes more, because its formula mass is larger',
            'Magnesium carbonate makes more, because its formula mass is '
            'smaller',
        ],
        "correct_index": 1,
        "why": 'Both decompose in a 1 : 1 ratio, so each gives 0.10 mol of '
               'carbon dioxide, with a mass of 0.10 × 44 = 4.4 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s17',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Nitrogen monoxide forms inside a hot car engine: N2 + O2 → '
                '2NO. Mr of N2 = 28 and Mr of NO = 30. Calculate the mass '
                'of nitrogen monoxide made from 2.8 g of nitrogen.',
        "options": [
            '3.0 g',
            '12.0 g',
            '2.8 g',
            '6.0 g',
        ],
        "correct_index": 3,
        "why": 'n(N2) = 2.8 ÷ 28 = 0.100 mol, each mole of N2 gives two of '
               'NO, so 0.200 × 30 = 6.0 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-s18',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Aluminium is extracted by electrolysis: 2Al2O3 → 4Al + '
                '3O2. Mr of Al2O3 = 102 and Ar of Al = 27. Calculate the '
                'mass of aluminium oxide needed to make 108 g of aluminium.',
        "options": [
            '408 g',
            '108 g',
            '204 g',
            '102 g',
        ],
        "correct_index": 2,
        "why": 'n(Al) = 108 ÷ 27 = 4.00 mol, four moles of aluminium come '
               'from two of the oxide, so 2.00 × 102 = 204 g.',
    },
    # harder ----------------------------------------------------------
    {
        "id": 'ks4-amounts-in-equations-h05',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A limestone sample is 90% calcium carbonate, CaCO3 (Mr = '
                '100), by mass. CaCO3 → CaO + CO2 and Mr of CaO = 56. '
                'Calculate the mass of calcium oxide made when 50 g of the '
                'limestone is heated until it fully decomposes.',
        "options": [
            '25.2 g',
            '28.0 g',
            '31.1 g',
            '45.0 g',
        ],
        "correct_index": 0,
        "why": 'The sample holds 45 g of calcium carbonate, which is 0.45 '
               'mol, so 0.45 × 56 = 25.2 g of calcium oxide forms.',
    },
    {
        "id": 'ks4-amounts-in-equations-h06',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Ethanol is made industrially by C2H4 + H2O → C2H5OH. Mr: '
                'C2H4 = 28, C2H5OH = 46. The plant runs at a percentage '
                'yield of 75%. Calculate the mass of ethanol made from 112 '
                'kg of ethene.',
        "options": [
            '92 kg',
            '138 kg',
            '184 kg',
            '245 kg',
        ],
        "correct_index": 1,
        "why": '112 ÷ 28 = 4.00 units of ethene give a theoretical 4.00 × '
               '46 = 184 kg of ethanol, and 75% of that is 138 kg.',
    },
    {
        "id": 'ks4-amounts-in-equations-h07',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Chromium is extracted by Cr2O3 + 2Al → 2Cr + Al2O3. Ar of '
                'Cr = 52 and Mr of Cr2O3 = 152. The process gives a '
                'percentage yield of 80%. Calculate the mass of chromium '
                'oxide needed to make 208 g of chromium.',
        "options": [
            '304 g',
            '475 g',
            '380 g',
            '152 g',
        ],
        "correct_index": 2,
        "why": '208 ÷ 52 = 4.00 mol of chromium is 80% of the theoretical, '
               'so 5.00 mol must be planned for, which needs 2.50 mol of '
               'Cr2O3, a mass of 2.50 × 152 = 380 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h08',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Sodium hydrogencarbonate decomposes on heating: 2NaHCO3 → '
                'Na2CO3 + H2O + CO2. Mr: NaHCO3 = 84, Na2CO3 = 106. '
                'Calculate the mass of sodium carbonate left when 33.6 g of '
                'sodium hydrogencarbonate is heated to constant mass.',
        "options": [
            '42.4 g',
            '10.6 g',
            '33.6 g',
            '21.2 g',
        ],
        "correct_index": 3,
        "why": 'n(NaHCO3) = 33.6 ÷ 84 = 0.400 mol, two moles of it give one '
               'of sodium carbonate, so 0.200 × 106 = 21.2 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h09',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '8.0 g of a metal oxide with the formula MO is reduced '
                'completely by hydrogen: MO + H2 → M + H2O. The metal left '
                'has a mass of 6.4 g. Ar of O = 16. Determine the relative '
                'atomic mass of M.',
        "options": [
            '16',
            '64',
            '80',
            '32',
        ],
        "correct_index": 1,
        "why": 'The 1.6 g of oxygen lost is 0.100 mol, so the sample was '
               '0.100 mol of MO and the 6.4 g of metal is 0.100 mol, giving '
               'Ar = 6.4 ÷ 0.100 = 64.',
    },
    {
        "id": 'ks4-amounts-in-equations-h10',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student works out the mass of oxygen needed to burn 0.50 '
                'mol of propane in C3H8 + 5O2 → 3CO2 + 4H2O. They write: '
                'ratio 1 : 5, so 0.50 × 5 = 2.5 mol, then mass = 2.5 × 16 = '
                '40 g. Identify the error.',
        "options": [
            'The ratio is 1 : 3 because there are three carbon dioxides, '
            'giving 48 g',
            'Nothing is wrong, because oxygen has a relative atomic mass of '
            '16',
            'They used the Ar of oxygen instead of the Mr of O2, so it is '
            '80 g',
            'They used the ratio upside down, so only 0.10 mol is needed, '
            'or 3.2 g',
        ],
        "correct_index": 2,
        "why": 'Oxygen reacts as O2 with an Mr of 32, so the mass needed is '
               '2.5 × 32 = 80 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h11',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Sulfur trioxide is made in two steps: S + O2 → SO2, then '
                '2SO2 + O2 → 2SO3. Ar of S = 32 and Mr of SO3 = 80. '
                'Calculate the mass of sulfur trioxide made from 9.6 g of '
                'sulfur, assuming both steps go to completion.',
        "options": [
            '16.0 g',
            '48.0 g',
            '9.6 g',
            '24.0 g',
        ],
        "correct_index": 3,
        "why": 'n(S) = 9.6 ÷ 32 = 0.300 mol, and both steps keep a 1 : 1 '
               'ratio of sulfur to sulfur trioxide, so 0.300 × 80 = 24.0 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h12',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Iron can be made from Fe2O3 + 3CO → 2Fe + 3CO2 or from '
                'Fe3O4 + 4CO → 3Fe + 4CO2. Mr: Fe2O3 = 160, Fe3O4 = 232. '
                'Determine which ore needs the smaller mass to make 1.00 '
                'mol of iron.',
        "options": [
            'Fe3O4, needing 77.3 g against 80.0 g for Fe2O3',
            'Fe2O3, needing 80.0 g against 116 g for Fe3O4',
            'Fe2O3, because its relative formula mass is the smaller of the '
            'two',
            'They need the same mass, because both are oxides of iron',
        ],
        "correct_index": 0,
        "why": '1.00 mol of iron needs 0.500 mol of Fe2O3, which is 80.0 g, '
               'but only 0.333 mol of Fe3O4, which is 77.3 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h13',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student needs 4.4 g of carbon dioxide and will make it '
                'by CaCO3 + 2HCl → CaCl2 + H2O + CO2. Mr: CaCO3 = 100, CO2 '
                '= 44, HCl = 36.5. Determine the mass of calcium carbonate '
                'and the minimum mass of hydrogen chloride needed.',
        "options": [
            '4.40 g of calcium carbonate and 7.30 g of hydrogen chloride',
            '20.0 g of calcium carbonate and 7.30 g of hydrogen chloride',
            '10.0 g of calcium carbonate and 7.30 g of hydrogen chloride',
            '10.0 g of calcium carbonate and 3.65 g of hydrogen chloride',
        ],
        "correct_index": 2,
        "why": '4.4 ÷ 44 = 0.100 mol of CO2 needs 0.100 mol of carbonate, '
               'or 10.0 g, and 0.200 mol of HCl, or 7.30 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h14',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Zinc carbonate decomposes: ZnCO3 → ZnO + CO2. Mr: ZnCO3 = '
                '125, CO2 = 44. A 25.0 g sample is heated and the solid '
                'left has a mass of 18.4 g. Determine the percentage of the '
                'zinc carbonate that decomposed.',
        "options": [
            '73.6%',
            '26.4%',
            '25.0%',
            '75.0%',
        ],
        "correct_index": 3,
        "why": 'Full decomposition of 0.200 mol would lose 8.8 g of carbon '
               'dioxide, but only 6.6 g was lost, so 6.6 ÷ 8.8 = 75.0% '
               'decomposed.',
    },
    {
        "id": 'ks4-amounts-in-equations-h15',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Two students each burn 1.20 g of carbon. One forms only '
                'carbon dioxide, CO2 (Mr = 44); the other, in a poor supply '
                'of air, forms only carbon monoxide, CO (Mr = 28). Ar of C '
                '= 12. Determine the difference between the masses of gas '
                'made.',
        "options": [
            '1.60 g',
            '7.20 g',
            '0.160 g',
            '16.0 g',
        ],
        "correct_index": 0,
        "why": 'Each burns 1.20 ÷ 12 = 0.100 mol of carbon, giving 4.40 g '
               'of carbon dioxide against 2.80 g of carbon monoxide, a '
               'difference of 1.60 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h16',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student says that because 2Mg + O2 → 2MgO has three '
                'moles on the left and only two on the right, mass must be '
                'lost in the reaction. Evaluate this.',
        "options": [
            'It is right, but only when the reaction is carried out in an '
            'open crucible',
            'It is wrong: the number of moles falls but every atom is still '
            'there',
            'It is right: three moles become two, so a third of the mass is '
            'lost as gas',
            'It is wrong: the equation should be balanced so the moles '
            'match on each side',
        ],
        "correct_index": 1,
        "why": 'A balanced equation has the same atoms on both sides, so '
               'mass is conserved even though the number of moles changes.',
    },
    {
        "id": 'ks4-amounts-in-equations-h17',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Ammonia is neutralised by sulfuric acid to make a '
                'fertiliser: 2NH3 + H2SO4 → (NH4)2SO4. Mr: NH3 = 17, '
                '(NH4)2SO4 = 132. Calculate the mass of ammonium sulfate '
                'made when 3.4 g of ammonia reacts with excess acid.',
        "options": [
            '26.4 g',
            '6.60 g',
            '3.40 g',
            '13.2 g',
        ],
        "correct_index": 3,
        "why": 'n(NH3) = 3.4 ÷ 17 = 0.200 mol, two moles of ammonia give '
               'one of the salt, so 0.100 × 132 = 13.2 g.',
    },
    {
        "id": 'ks4-amounts-in-equations-h18',
        "subtopic_slug": 'amounts-in-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 2.00 g sample of impure zinc is added to excess dilute '
                'sulfuric acid: Zn + H2SO4 → ZnSO4 + H2. Ar of Zn = 65 and '
                'Mr of H2 = 2. The reaction gives 0.052 g of hydrogen. '
                'Determine the percentage purity of the zinc.',
        "options": [
            '118%',
            '65.0%',
            '84.5%',
            '2.60%',
        ],
        "correct_index": 2,
        "why": '0.052 ÷ 2 = 0.026 mol of hydrogen means 0.026 mol of zinc '
               'reacted, a mass of 1.69 g, which is 84.5% of 2.00 g.',
    },
]
