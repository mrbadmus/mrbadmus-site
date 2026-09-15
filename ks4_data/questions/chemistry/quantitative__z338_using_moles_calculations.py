"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`using-moles-calculations`.

AQA 5.3.2.3–5.3.2.4, taken wide rather than deep: concentration in mol/dm³
rearranged all three ways with the cm³-to-dm³ conversion in the way, the
limiting reactant found by comparing moles against the equation's ratio, and
empirical and molecular formulae from masses and percentages. The harder band
chains those together — a titration answered in g/dm³, a precipitate mass from
a solution volume, a percentage yield reached through a concentration.

⚠️ HIGHER TIER, both pathways. Nothing here uses a molar gas volume: the
molar volume at room temperature and pressure is AQA 4.3.2.5, Chemistry-only,
and these rows are served to combined-science classes as well.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # easier ----------------------------------------------------------
    {
        "id": 'ks4-using-moles-calculations-e05',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 2.0 dm³ bottle holds a 0.50 mol/dm³ solution of '
                'potassium chloride. Calculate the amount of potassium '
                'chloride dissolved in it.',
        "options": [
            '1.0 mol',
            '0.25 mol',
            '4.0 mol',
            '2.5 mol',
        ],
        "correct_index": 0,
        "why": 'n = c × V = 0.50 × 2.0 = 1.0 mol.',
    },
    {
        "id": 'ks4-using-moles-calculations-e06',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the equation that gives the volume of a solution '
                'from its concentration and the amount dissolved in it.',
        "options": [
            'volume = concentration × 1000',
            'volume = moles ÷ concentration',
            'volume = moles × concentration',
            'volume = concentration ÷ moles',
        ],
        "correct_index": 1,
        "why": 'Rearranging concentration = moles ÷ volume gives volume = '
               'moles ÷ concentration.',
    },
    {
        "id": 'ks4-using-moles-calculations-e07',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the concentration, in mol/dm³, of a solution '
                'holding 0.60 mol of solute in 3.0 dm³.',
        "options": [
            '1.8 mol/dm³',
            '0.60 mol/dm³',
            '0.20 mol/dm³',
            '5.0 mol/dm³',
        ],
        "correct_index": 2,
        "why": 'c = n ÷ V = 0.60 ÷ 3.0 = 0.20 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-e08',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify what is left in the flask once a reaction that '
                'had one reactant in excess has stopped.',
        "options": [
            'Some of the limiting reactant, along with the products',
            'Only the products, because every reactant is used up',
            'Equal amounts of both reactants, along with the products',
            'Some of the reactant in excess, along with the products',
        ],
        "correct_index": 3,
        "why": 'The limiting reactant is fully used up, so what remains is '
               'the products plus the unreacted part of the reactant that '
               'was in excess.',
    },
    {
        "id": 'ks4-using-moles-calculations-e09',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify what decides the maximum mass of product a '
                'reaction can make when one of its reactants is in excess.',
        "options": [
            'The reactant with the larger relative formula mass',
            'The amount in moles of the limiting reactant',
            'The amount in moles of the reactant in excess',
            'The total mass of both reactants added together',
        ],
        "correct_index": 1,
        "why": 'The limiting reactant runs out first and stops the '
               'reaction, so it fixes how much product can form.',
    },
    {
        "id": 'ks4-using-moles-calculations-e10',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A compound is found to contain 0.10 mol of magnesium atoms '
                'and 0.20 mol of bromine atoms. Determine its empirical '
                'formula.',
        "options": [
            'Mg2Br',
            'Mg2Br4',
            'MgBr2',
            'MgBr',
        ],
        "correct_index": 2,
        "why": 'The ratio 0.10 : 0.20 simplifies to 1 : 2, giving MgBr2.',
    },
    {
        "id": 'ks4-using-moles-calculations-e11',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A flask holds 500 cm³ of solution in which 0.050 mol of '
                'acid is dissolved. Calculate the concentration in mol/dm³.',
        "options": [
            '0.0001 mol/dm³',
            '25 mol/dm³',
            '10 mol/dm³',
            '0.10 mol/dm³',
        ],
        "correct_index": 3,
        "why": 'V = 500 ÷ 1000 = 0.500 dm³, so c = 0.050 ÷ 0.500 = 0.10 '
               'mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-e12',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State the volume unit that must be used in the equation '
                'concentration = moles ÷ volume.',
        "options": [
            'dm³',
            'cm³',
            'm³',
            'mm³',
        ],
        "correct_index": 0,
        "why": 'Concentration in mol/dm³ is an amount per cubic decimetre, '
               'so the volume must be in dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-e13',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A bottle of sulfuric acid is labelled 0.20 mol/dm³. '
                'Calculate the volume, in dm³, that holds 0.050 mol of the '
                'acid.',
        "options": [
            '0.010 dm³',
            '0.050 dm³',
            '0.25 dm³',
            '4.0 dm³',
        ],
        "correct_index": 2,
        "why": 'V = n ÷ c = 0.050 ÷ 0.20 = 0.25 dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-e14',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what the empirical formula of a compound shows.',
        "options": [
            'The actual number of atoms in one molecule of it',
            'The total mass of all the atoms in one molecule',
            'The order in which its atoms are joined together',
            'The simplest whole-number ratio of the atoms in it',
        ],
        "correct_index": 3,
        "why": 'An empirical formula gives the simplest whole-number ratio '
               'of the atoms present, not the actual number in a molecule.',
    },
    {
        "id": 'ks4-using-moles-calculations-e15',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student knows the empirical formula of a compound and '
                'its relative formula mass. State the calculation that '
                'gives the number of empirical units in one of its '
                'molecules.',
        "options": [
            'The relative formula mass divided by the empirical formula mass',
            'The empirical formula mass divided by the relative formula mass',
            'The relative formula mass multiplied by the empirical formula '
            'mass',
            'The empirical formula mass taken away from the relative '
            'formula mass',
        ],
        "correct_index": 0,
        "why": 'Dividing the relative formula mass by the empirical formula '
               'mass gives the whole number that every subscript must be '
               'multiplied by.',
    },
    {
        "id": 'ks4-using-moles-calculations-e16',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify what the amounts in moles must be compared '
                'against to decide which reactant is limiting.',
        "options": [
            'The order in which the reactants were added',
            'The ratio the balanced equation asks for',
            'The relative formula mass of each reactant',
            'The mass in grams of each reactant used',
        ],
        "correct_index": 1,
        "why": 'The moles available have to be compared with the ratio in '
               'the balanced equation, because that says how much of each '
               'is needed.',
    },
    {
        "id": 'ks4-using-moles-calculations-e17',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A burette delivers 40 cm³ of acid at a concentration of '
                '0.25 mol/dm³. Determine the amount of acid delivered, in '
                'moles.',
        "options": [
            '10 mol',
            '0.0063 mol',
            '160 mol',
            '0.010 mol',
        ],
        "correct_index": 3,
        "why": 'V = 40 ÷ 1000 = 0.040 dm³, so n = 0.25 × 0.040 = 0.010 mol.',
    },
    {
        "id": 'ks4-using-moles-calculations-e18',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why the concentration in mol/dm³ is unchanged when '
                'one solution is shared equally between two identical '
                'flasks.',
        "options": [
            'The moles are halved while the volume stays the same, so it '
            'halves',
            'The volume is halved while the moles stay the same, so it '
            'doubles',
            'Both the moles and the volume are halved, so the ratio is '
            'unchanged',
            'The concentration depends on the mass of the flask, which has '
            'not changed',
        ],
        "correct_index": 2,
        "why": 'Concentration is an amount per cubic decimetre, so halving '
               'both the moles and the volume leaves the ratio between them '
               'the same.',
    },
    # standard --------------------------------------------------------
    {
        "id": 'ks4-using-moles-calculations-s05',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student weighs out 12.0 g of sodium hydroxide, NaOH, '
                'dissolves it and makes the solution up to 500 cm³ in a '
                'volumetric flask. Mr of NaOH = 40. Determine the '
                'concentration in mol/dm³.',
        "options": [
            '0.60 mol/dm³',
            '0.30 mol/dm³',
            '1.7 mol/dm³',
            '0.024 mol/dm³',
        ],
        "correct_index": 0,
        "why": 'n = 12.0 ÷ 40 = 0.300 mol and V = 0.500 dm³, so c = 0.300 ÷ '
               '0.500 = 0.60 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-s06',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the mass of potassium hydroxide, KOH (Mr = 56), '
                'needed to make 250 cm³ of a 0.20 mol/dm³ solution.',
        "options": [
            '224 g',
            '2.8 g',
            '11.2 g',
            '14.0 g',
        ],
        "correct_index": 1,
        "why": 'n = 0.20 × 0.250 = 0.050 mol, so the mass is 0.050 × 56 = '
               '2.8 g.',
    },
    {
        "id": 'ks4-using-moles-calculations-s07',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'In a titration, 25.0 cm³ of 0.120 mol/dm³ sodium hydroxide '
                'is exactly neutralised by 20.0 cm³ of hydrochloric acid. '
                'NaOH + HCl → NaCl + H2O. Calculate the concentration of '
                'the hydrochloric acid.',
        "options": [
            '0.120 mol/dm³',
            '0.300 mol/dm³',
            '0.150 mol/dm³',
            '0.0960 mol/dm³',
        ],
        "correct_index": 2,
        "why": 'n(NaOH) = 0.120 × 0.0250 = 3.00 × 10⁻³ mol, the ratio is 1 '
               ': 1, so c(HCl) = 3.00 × 10⁻³ ÷ 0.0200 = 0.150 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-s08',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": '0.30 mol of hydrogen is mixed with 0.20 mol of nitrogen '
                'and the mixture is passed over a catalyst. N2 + 3H2 → '
                '2NH3. Identify the limiting reactant.',
        "options": [
            'Nitrogen, because 0.20 mol is the smaller of the two amounts',
            'Neither, because the amounts are already in the ratio the '
            'equation asks for',
            'Nitrogen, because its relative formula mass is the larger of '
            'the two',
            'Hydrogen, because 0.20 mol of nitrogen needs 0.60 mol of it',
        ],
        "correct_index": 3,
        "why": '0.20 mol of nitrogen would need 0.60 mol of hydrogen but '
               'only 0.30 mol is present, so the hydrogen runs out first.',
    },
    {
        "id": 'ks4-using-moles-calculations-s09',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": '0.40 mol of carbon is heated with 0.30 mol of copper(II) '
                'oxide: 2CuO + C → 2Cu + CO2. Ar of Cu = 63.5. Calculate '
                'the mass of copper made.',
        "options": [
            '9.53 g',
            '19.1 g',
            '25.4 g',
            '38.1 g',
        ],
        "correct_index": 1,
        "why": '0.30 mol of copper oxide needs only 0.15 mol of carbon, so '
               'the oxide is limiting and gives 0.30 mol of copper, a mass '
               'of 0.30 × 63.5 = 19.1 g.',
    },
    {
        "id": 'ks4-using-moles-calculations-s10',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 6.2 g sample of an oxide of sodium is found to hold 4.6 '
                'g of sodium and 1.6 g of oxygen. Ar: Na = 23, O = 16. '
                'Determine its empirical formula.',
        "options": [
            'NaO2',
            'Na3O',
            'Na2O',
            'NaO',
        ],
        "correct_index": 2,
        "why": 'n(Na) = 4.6 ÷ 23 = 0.200 mol and n(O) = 1.6 ÷ 16 = 0.100 '
               'mol, a ratio of 2 : 1.',
    },
    {
        "id": 'ks4-using-moles-calculations-s11',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A bottle of potassium nitrate solution is labelled 30.3 '
                'g/dm³. Mr of KNO3 = 101. Determine its concentration in '
                'mol/dm³.',
        "options": [
            '3.33 mol/dm³',
            '3060 mol/dm³',
            '0.0300 mol/dm³',
            '0.300 mol/dm³',
        ],
        "correct_index": 3,
        "why": 'Dividing the mass held in one cubic decimetre by the Mr '
               'gives 30.3 ÷ 101 = 0.300 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-s12',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 0.250 mol/dm³ solution of copper(II) sulfate is '
                'prepared. Mr of CuSO4 = 160. Calculate its concentration '
                'in g/dm³.',
        "options": [
            '40.0 g/dm³',
            '640 g/dm³',
            '0.00156 g/dm³',
            '160 g/dm³',
        ],
        "correct_index": 0,
        "why": 'Each cubic decimetre holds 0.250 mol, and 0.250 × 160 = '
               '40.0 g, so the concentration is 40.0 g/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-s13',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the mass of sodium carbonate, Na2CO3 (Mr = 106), '
                'dissolved in 200 cm³ of a 0.500 mol/dm³ solution.',
        "options": [
            '21.2 g',
            '1.06 g',
            '10.6 g',
            '53.0 g',
        ],
        "correct_index": 2,
        "why": 'n = 0.500 × 0.200 = 0.100 mol, so the mass is 0.100 × 106 = '
               '10.6 g.',
    },
    {
        "id": 'ks4-using-moles-calculations-s14',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student works out the concentration of a solution '
                'holding 0.040 mol of solute in 80 cm³ and writes 0.040 ÷ '
                '80 = 5.0 × 10⁻⁴ mol/dm³. Identify the error.',
        "options": [
            'The volume should have been multiplied, so it is 3.2 mol/dm³',
            'The moles and volume were the wrong way round, so it is 2000 '
            'mol/dm³',
            'Nothing is wrong, because a dilute solution has a very small '
            'value',
            'The volume was left in cm³, so the answer should be 0.50 mol/dm³',
        ],
        "correct_index": 3,
        "why": 'Concentration in mol/dm³ needs the volume in dm³, so 80 cm³ '
               'is 0.080 dm³ and c = 0.040 ÷ 0.080 = 0.50 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-s15',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the amount of chloride ions, in moles, in 250 '
                'cm³ of a 0.200 mol/dm³ solution of calcium chloride, '
                'CaCl2.',
        "options": [
            '0.100 mol',
            '0.0500 mol',
            '0.0250 mol',
            '0.400 mol',
        ],
        "correct_index": 0,
        "why": 'n(CaCl2) = 0.200 × 0.250 = 0.0500 mol, and each formula '
               'unit releases two chloride ions, so there are 0.100 mol of '
               'them.',
    },
    {
        "id": 'ks4-using-moles-calculations-s16',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'In a titration, 25.0 cm³ of sodium carbonate solution is '
                'exactly neutralised by 30.0 cm³ of 0.100 mol/dm³ '
                'hydrochloric acid. Na2CO3 + 2HCl → 2NaCl + H2O + CO2. '
                'Calculate the concentration of the sodium carbonate.',
        "options": [
            '0.0300 mol/dm³',
            '0.0600 mol/dm³',
            '0.120 mol/dm³',
            '0.240 mol/dm³',
        ],
        "correct_index": 1,
        "why": 'n(HCl) = 0.100 × 0.0300 = 3.00 × 10⁻³ mol, two moles of '
               'acid react with one of carbonate, so n(Na2CO3) = 1.50 × '
               '10⁻³ mol and c = 1.50 × 10⁻³ ÷ 0.0250 = 0.0600 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-s17',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why a student must know the balanced equation '
                'before working out a concentration from a titration '
                'result.',
        "options": [
            'It gives the relative formula mass of each solution',
            'It gives the volume of each solution that must be used',
            'It gives the colour change the indicator will show',
            'It gives the ratio in which the two solutions react',
        ],
        "correct_index": 3,
        "why": 'The moles found for one solution can only be turned into '
               'moles of the other through the ratio in the balanced '
               'equation.',
    },
    {
        "id": 'ks4-using-moles-calculations-s18',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": '4.8 g of magnesium is heated in a sealed flask holding 4.8 '
                'g of oxygen gas: 2Mg + O2 → 2MgO. Ar of Mg = 24 and Mr of '
                'O2 = 32. Determine which reactant is in excess.',
        "options": [
            'Neither, because the two masses added to the flask are equal',
            'Magnesium, because it has the smaller relative atomic mass',
            'Oxygen, because 0.200 mol of magnesium needs only 0.100 mol of '
            'it',
            'Magnesium, because 0.200 mol is more than 0.150 mol of oxygen',
        ],
        "correct_index": 2,
        "why": '4.8 ÷ 24 = 0.200 mol of magnesium needs 0.100 mol of '
               'oxygen, and 4.8 ÷ 32 = 0.150 mol is present, so oxygen is '
               'left over.',
    },
    # harder ----------------------------------------------------------
    {
        "id": 'ks4-using-moles-calculations-h05',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '20.0 cm³ of 0.250 mol/dm³ potassium hydroxide is exactly '
                'neutralised by 25.0 cm³ of sulfuric acid. H2SO4 + 2KOH → '
                'K2SO4 + 2H2O. Mr of H2SO4 = 98. Determine the '
                'concentration of the acid in g/dm³.',
        "options": [
            '9.80 g/dm³',
            '19.6 g/dm³',
            '4.90 g/dm³',
            '0.100 g/dm³',
        ],
        "correct_index": 0,
        "why": 'n(KOH) = 0.250 × 0.0200 = 5.00 × 10⁻³ mol, so n(H2SO4) = '
               '2.50 × 10⁻³ mol, c = 0.100 mol/dm³ and 0.100 × 98 = 9.80 '
               'g/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-h06',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '2.7 g of aluminium is dropped into 200 cm³ of 1.00 mol/dm³ '
                'hydrochloric acid: 2Al + 6HCl → 2AlCl3 + 3H2. Ar of Al = '
                '27 and Mr of H2 = 2. Calculate the maximum mass of '
                'hydrogen that can be made.',
        "options": [
            '0.600 g',
            '0.200 g',
            '0.300 g',
            '0.100 g',
        ],
        "correct_index": 1,
        "why": '0.100 mol of aluminium would need 0.300 mol of acid but '
               'only 0.200 mol is present, so the acid is limiting and '
               'gives 0.100 mol of hydrogen, or 0.200 g.',
    },
    {
        "id": 'ks4-using-moles-calculations-h07',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '50.0 cm³ of 0.250 mol/dm³ silver nitrate is added to '
                'excess sodium chloride solution: AgNO3 + NaCl → AgCl + '
                'NaNO3. Mr of AgCl = 143.5. Calculate the mass of silver '
                'chloride precipitated.',
        "options": [
            '0.897 g',
            '17.9 g',
            '1.79 g',
            '3.59 g',
        ],
        "correct_index": 2,
        "why": 'n(AgNO3) = 0.250 × 0.0500 = 0.0125 mol, the ratio is 1 : 1, '
               'so the mass is 0.0125 × 143.5 = 1.79 g.',
    },
    {
        "id": 'ks4-using-moles-calculations-h08',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student needs 0.0250 mol of hydrochloric acid and the '
                'bottle on the shelf is labelled 0.500 mol/dm³. Determine '
                'the volume, in cm³, they must measure out.',
        "options": [
            '0.0500 cm³',
            '20.0 cm³',
            '12.5 cm³',
            '50.0 cm³',
        ],
        "correct_index": 3,
        "why": 'V = n ÷ c = 0.0250 ÷ 0.500 = 0.0500 dm³, which is 50.0 cm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-h09',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Burning 3.10 g of phosphorus in excess oxygen gives 7.10 g '
                'of an oxide and nothing else. Ar: P = 31, O = 16. '
                'Determine the empirical formula of the oxide.',
        "options": [
            'PO5',
            'P2O5',
            'PO2',
            'P2O3',
        ],
        "correct_index": 1,
        "why": '3.10 ÷ 31 = 0.100 mol of phosphorus combines with the 4.00 '
               'g of oxygen gained, which is 0.250 mol of oxygen atoms, a '
               'ratio of 2 : 5.',
    },
    {
        "id": 'ks4-using-moles-calculations-h10',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Burning 4.40 g of a compound made only of carbon and '
                'hydrogen gives 0.300 mol of carbon dioxide and 0.400 mol '
                'of water. Ar: C = 12, H = 1. Determine its empirical '
                'formula.',
        "options": [
            'CH3',
            'C3H10',
            'C3H8',
            'C3H4',
        ],
        "correct_index": 2,
        "why": 'The 0.300 mol of carbon dioxide holds 0.300 mol of carbon '
               'and the 0.400 mol of water holds 0.800 mol of hydrogen, a '
               'ratio of 3 : 8.',
    },
    {
        "id": 'ks4-using-moles-calculations-h11',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student mixes 0.20 mol of zinc with 0.20 mol of '
                'hydrochloric acid and says neither can be limiting because '
                'the amounts are equal. Zn + 2HCl → ZnCl2 + H2. Evaluate '
                'this.',
        "options": [
            'It is right: equal amounts in moles always react exactly with '
            'each other',
            'It is wrong: zinc runs out first because it is the solid in '
            'the mixture',
            'It is right, provided the acid is added to the zinc rather '
            'than the other way round',
            'It is wrong: 0.20 mol of zinc needs 0.40 mol of acid, so the '
            'acid runs out',
        ],
        "correct_index": 3,
        "why": 'The equation needs two moles of acid for each mole of zinc, '
               'so 0.20 mol of zinc would need 0.40 mol of acid and only '
               '0.20 mol is present.',
    },
    {
        "id": 'ks4-using-moles-calculations-h12',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '25.0 cm³ of 0.100 mol/dm³ sulfuric acid is mixed with 25.0 '
                'cm³ of 0.100 mol/dm³ sodium hydroxide. H2SO4 + 2NaOH → '
                'Na2SO4 + 2H2O. Determine which reactant is left over, and '
                'how much of it.',
        "options": [
            'Sulfuric acid, with 1.25 × 10⁻³ mol left over',
            'Sodium hydroxide, with 1.25 × 10⁻³ mol left over',
            'Neither, because the two amounts in moles are equal',
            'Sulfuric acid, with 2.50 × 10⁻³ mol left over',
        ],
        "correct_index": 0,
        "why": 'The 2.50 × 10⁻³ mol of sodium hydroxide uses only 1.25 × '
               '10⁻³ mol of the acid, leaving 1.25 × 10⁻³ mol of acid '
               'unreacted.',
    },
    {
        "id": 'ks4-using-moles-calculations-h13',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student dilutes 25.0 cm³ of 2.00 mol/dm³ hydrochloric '
                'acid to a total volume of 500 cm³, then takes a 20.0 cm³ '
                'sample of the diluted acid. Determine the amount of '
                'hydrochloric acid, in moles, in that sample.',
        "options": [
            '5.00 × 10⁻² mol',
            '4.00 × 10⁻³ mol',
            '2.00 × 10⁻³ mol',
            '4.00 × 10⁻² mol',
        ],
        "correct_index": 2,
        "why": 'The 25.0 cm³ holds 0.0500 mol, which spread over 0.500 dm³ '
               'gives 0.100 mol/dm³, so 0.0200 dm³ of it holds 2.00 × 10⁻³ '
               'mol.',
    },
    {
        "id": 'ks4-using-moles-calculations-h14',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine which holds more solute: 100 cm³ of 0.160 '
                'mol/dm³ sodium chloride, or 250 cm³ of 0.0500 mol/dm³ '
                'sodium chloride.',
        "options": [
            'The 250 cm³ sample, holding 0.0125 mol against 0.0160 mol',
            'The 250 cm³ sample, because the larger volume must hold more',
            'They hold the same, because concentration and volume cancel out',
            'The 100 cm³ sample, holding 0.0160 mol against 0.0125 mol',
        ],
        "correct_index": 3,
        "why": 'n = c × V gives 0.160 × 0.100 = 0.0160 mol against 0.0500 × '
               '0.250 = 0.0125 mol.',
    },
    {
        "id": 'ks4-using-moles-calculations-h15',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Excess zinc is added to 50.0 cm³ of hydrochloric acid and '
                '0.0500 g of hydrogen is collected: Zn + 2HCl → ZnCl2 + H2. '
                'Mr of H2 = 2. Determine the concentration of the acid.',
        "options": [
            '1.00 mol/dm³',
            '0.500 mol/dm³',
            '2.00 mol/dm³',
            '0.0500 mol/dm³',
        ],
        "correct_index": 0,
        "why": '0.0500 ÷ 2 = 0.0250 mol of hydrogen comes from 0.0500 mol '
               'of acid, and 0.0500 ÷ 0.0500 dm³ gives 1.00 mol/dm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-h16',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student is told a compound is 40.0% calcium, 12.0% '
                'carbon and 48.0% oxygen by mass, and claims its empirical '
                'formula is CaCO2. Ar: Ca = 40, C = 12, O = 16. Evaluate '
                'this claim.',
        "options": [
            'It is right, because the ratio 40 : 12 : 48 simplifies to 10 : '
            '3 : 12',
            'It is wrong: the oxygen comes to 3.00 mol against 1.00 mol '
            'each, so CaCO3',
            'It is right: 48.0% of oxygen divided by 16 gives 2.00 mol of '
            'oxygen atoms',
            'It is wrong: the percentages should be divided by the Mr, '
            'giving CaC3O4',
        ],
        "correct_index": 1,
        "why": '40.0 ÷ 40 = 1.00, 12.0 ÷ 12 = 1.00 and 48.0 ÷ 16 = 3.00, a '
               'ratio of 1 : 1 : 3, so the formula is CaCO3.',
    },
    {
        "id": 'ks4-using-moles-calculations-h17',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine the volume, in cm³, of 0.500 mol/dm³ '
                'hydrochloric acid needed to react completely with 2.50 g '
                'of calcium carbonate. CaCO3 + 2HCl → CaCl2 + H2O + CO2, '
                'and Mr of CaCO3 = 100.',
        "options": [
            '50.0 cm³',
            '200 cm³',
            '25.0 cm³',
            '100 cm³',
        ],
        "correct_index": 3,
        "why": 'n(CaCO3) = 2.50 ÷ 100 = 0.0250 mol needs 0.0500 mol of '
               'acid, so V = 0.0500 ÷ 0.500 = 0.100 dm³, or 100 cm³.',
    },
    {
        "id": 'ks4-using-moles-calculations-h18',
        "subtopic_slug": 'using-moles-calculations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '25.0 cm³ of 0.400 mol/dm³ copper(II) sulfate solution is '
                'reacted with excess sodium hydroxide, precipitating '
                'copper(II) hydroxide, Cu(OH)2 (Mr = 97.5), in a 1 : 1 '
                'ratio. The student collects 0.780 g. Determine the '
                'percentage yield.',
        "options": [
            '78.0%',
            '8.00%',
            '80.0%',
            '125%',
        ],
        "correct_index": 2,
        "why": 'n(CuSO4) = 0.400 × 0.0250 = 0.0100 mol, giving a '
               'theoretical 0.975 g, and 0.780 ÷ 0.975 = 80.0%.',
    },
]
