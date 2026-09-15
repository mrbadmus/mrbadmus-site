"""Chemistry · Quantitative chemistry — the MRB-338 expansion for `moles`.

AQA 5.3.2.1, taken wide rather than deep: the mole as a fixed count of
particles, molar mass as the Mr in grams, and n = m ÷ Mr worked in all three
directions, across elements, simple molecules, ionic compounds, bracketed
formulae and hydrated salts. The standard band adds the unit conversions
(mg and kg) and the step from moles of a substance to moles of the atoms or
ions inside it; the harder band chains those together and works backwards to
an unknown Ar or an unknown number of waters of crystallisation.

⚠️ HIGHER TIER, both pathways. Every row here is reachable from n = m ÷ Mr and
the Avogadro constant alone — no gas volumes, no concentrations.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # easier ----------------------------------------------------------
    {
        "id": 'ks4-moles-e05',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A lump of charcoal is almost pure carbon and has a mass of '
                '24 g. Ar of C = 12. Calculate the amount of carbon '
                'present, in moles.',
        "options": [
            '2.0 mol',
            '0.50 mol',
            '36 mol',
            '288 mol',
        ],
        "correct_index": 0,
        "why": 'n = mass ÷ Ar = 24 ÷ 12 = 2.0 mol of carbon atoms.',
    },
    {
        "id": 'ks4-moles-e06',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Neon is used in advertising signs. Calculate the mass of '
                '3.00 mol of neon. Ar of Ne = 20.',
        "options": [
            '23 g',
            '60 g',
            '6.67 g',
            '0.15 g',
        ],
        "correct_index": 1,
        "why": 'mass = moles × Ar = 3.00 × 20 = 60 g.',
    },
    {
        "id": 'ks4-moles-e07',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what one mole of a substance always contains.',
        "options": [
            'One gram of the substance for each proton in one of its atoms',
            'Exactly one million million particles of the substance',
            'The same number of particles as there are in 12 g of carbon-12',
            'The same mass of particles as there is in 12 g of carbon-12',
        ],
        "correct_index": 2,
        "why": 'A mole is the amount holding 6.02 × 10²³ particles, which '
               'is the number of atoms in exactly 12 g of carbon-12.',
    },
    {
        "id": 'ks4-moles-e08',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": '8.5 g of ammonia gas, NH3, is collected in a flask. Mr of '
                'NH3 = 17. Determine the amount of ammonia, in moles.',
        "options": [
            '2.0 mol',
            '0.61 mol',
            '144.5 mol',
            '0.50 mol',
        ],
        "correct_index": 3,
        "why": 'n = 8.5 ÷ 17 = 0.50 mol of ammonia molecules.',
    },
    {
        "id": 'ks4-moles-e09',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the mass of one mole of carbon-12 atoms.',
        "options": [
            '1 g',
            '12 g',
            '6 g',
            '24 g',
        ],
        "correct_index": 1,
        "why": 'The mole is defined so that one mole of carbon-12 atoms has '
               'a mass of exactly 12 g.',
    },
    {
        "id": 'ks4-moles-e10',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A sample of iron is found to hold 1.204 × 10²⁴ atoms. The '
                'Avogadro constant is 6.02 × 10²³ mol⁻¹. Determine the '
                'amount of iron, in moles.',
        "options": [
            '0.500 mol',
            '7.25 × 10⁴⁷ mol',
            '2.00 mol',
            '1.20 × 10²⁴ mol',
        ],
        "correct_index": 2,
        "why": 'n = particles ÷ Avogadro constant = 1.204 × 10²⁴ ÷ 6.02 × '
               '10²³ = 2.00 mol.',
    },
    {
        "id": 'ks4-moles-e11',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the quantity that is the same for one mole of '
                'every substance.',
        "options": [
            'The mass of the sample in grams',
            'The volume the sample takes up',
            'The number of protons in each particle',
            'The number of particles it contains',
        ],
        "correct_index": 3,
        "why": 'One mole of anything holds 6.02 × 10²³ particles, although '
               'its mass and volume depend on what the substance is.',
    },
    {
        "id": 'ks4-moles-e12',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A balloon holds 0.20 g of hydrogen gas, H2, and the Mr of '
                'H2 is 2. Calculate the number of moles of hydrogen '
                'molecules inside it.',
        "options": [
            '0.10 mol',
            '10 mol',
            '0.20 mol',
            '0.40 mol',
        ],
        "correct_index": 0,
        "why": 'n = 0.20 ÷ 2 = 0.10 mol, because hydrogen gas exists as H2 '
               'molecules with an Mr of 2.',
    },
    {
        "id": 'ks4-moles-e13',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Sulfur dioxide, SO2, is given off when fossil fuels that '
                'contain sulfur are burned. Ar: S = 32, O = 16. Identify '
                'the mass of one mole of sulfur dioxide.',
        "options": [
            '32 g',
            '128 g',
            '64 g',
            '48 g',
        ],
        "correct_index": 2,
        "why": 'Mr = 32 + (2 × 16) = 64, so one mole of it has a mass of 64 '
               'g.',
    },
    {
        "id": 'ks4-moles-e14',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State the unit in which molar mass is measured.',
        "options": [
            'mol/g',
            'g',
            'mol',
            'g/mol',
        ],
        "correct_index": 3,
        "why": 'Molar mass is a mass for every one mole, so it is measured '
               'in grams per mole.',
    },
    {
        "id": 'ks4-moles-e15',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the mass of 0.40 mol of copper. Ar of Cu = 63.5.',
        "options": [
            '25.4 g',
            '158.75 g',
            '63.9 g',
            '0.0063 g',
        ],
        "correct_index": 0,
        "why": 'mass = moles × Ar = 0.40 × 63.5 = 25.4 g.',
    },
    {
        "id": 'ks4-moles-e16',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the percentage by mass of carbon in ethane, '
                'C2H6. Ar: C = 12, H = 1.',
        "options": [
            '125%',
            '80.0%',
            '20.0%',
            '40.0%',
        ],
        "correct_index": 1,
        "why": 'Mr = (2 × 12) + (6 × 1) = 30, so % C = (24 ÷ 30) × 100 = '
               '80.0%.',
    },
    {
        "id": 'ks4-moles-e17',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what the Avogadro constant is used for.',
        "options": [
            'Turning a mass in grams into a relative formula mass',
            'Turning a volume in cm³ into a volume in dm³',
            'Turning a percentage yield into a mass of product',
            'Turning a number of moles into a number of particles',
        ],
        "correct_index": 3,
        "why": 'Multiplying an amount in moles by 6.02 × 10²³ gives the '
               'number of particles present.',
    },
    {
        "id": 'ks4-moles-e18',
        "subtopic_slug": 'moles',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A coin of pure silver has a mass of 54 g. Ar of Ag = 108. '
                'Calculate the amount of silver in it, in moles.',
        "options": [
            '162 mol',
            '5832 mol',
            '0.50 mol',
            '2.00 mol',
        ],
        "correct_index": 2,
        "why": 'n = 54 ÷ 108 = 0.50 mol of silver atoms.',
    },
    # standard --------------------------------------------------------
    {
        "id": 'ks4-moles-s05',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'An indigestion tablet contains 250 mg of calcium '
                'carbonate, CaCO3. Mr of CaCO3 = 100. Calculate the amount '
                'of calcium carbonate in the tablet, in moles.',
        "options": [
            '2.50 × 10⁻³ mol',
            '2.50 mol',
            '2.50 × 10⁻⁶ mol',
            '400 mol',
        ],
        "correct_index": 0,
        "why": '250 mg is 0.250 g, so n = 0.250 ÷ 100 = 2.50 × 10⁻³ mol.',
    },
    {
        "id": 'ks4-moles-s06',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A gas cylinder holds 66 g of carbon dioxide, CO2. Mr = 44 '
                'and the Avogadro constant is 6.02 × 10²³ mol⁻¹. Calculate '
                'the number of carbon dioxide molecules it holds.',
        "options": [
            '6.02 × 10²³',
            '9.03 × 10²³',
            '4.01 × 10²³',
            '1.50 × 10²³',
        ],
        "correct_index": 1,
        "why": 'n = 66 ÷ 44 = 1.50 mol, so molecules = 1.50 × 6.02 × 10²³ = '
               '9.03 × 10²³.',
    },
    {
        "id": 'ks4-moles-s07',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the number of hydrogen atoms in 0.75 mol of '
                'methane, CH4. The Avogadro constant is 6.02 × 10²³ mol⁻¹.',
        "options": [
            '1.13 × 10²³',
            '1.81 × 10²³',
            '1.81 × 10²⁴',
            '4.52 × 10²³',
        ],
        "correct_index": 2,
        "why": 'Each molecule holds four hydrogen atoms, so there are 0.75 '
               '× 4 = 3.0 mol of hydrogen atoms, and 3.0 × 6.02 × 10²³ = '
               '1.81 × 10²⁴.',
    },
    {
        "id": 'ks4-moles-s08',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calcium nitrate, Ca(NO3)2, is used as a fertiliser. Ar: Ca '
                '= 40, N = 14, O = 16. Calculate the percentage by mass of '
                'nitrogen in it.',
        "options": [
            '8.5%',
            '13.7%',
            '27.5%',
            '17.1%',
        ],
        "correct_index": 3,
        "why": 'Mr = 40 + 2 × (14 + 48) = 164 and the nitrogen in it has a '
               'mass of 2 × 14 = 28, so % N = (28 ÷ 164) × 100 = 17.1%.',
    },
    {
        "id": 'ks4-moles-s09',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine which holds the greater amount in moles: 20 g of '
                'calcium (Ar = 40) or 20 g of sulfur (Ar = 32).',
        "options": [
            'Calcium, because a heavier atom must give more moles per gram',
            'Sulfur, because 20 ÷ 32 = 0.63 mol against 20 ÷ 40 = 0.50 mol',
            'Calcium, because its relative atomic mass is the larger of the '
            'two',
            'They hold the same amount, because the two masses are equal',
        ],
        "correct_index": 1,
        "why": 'The lighter atom gives more moles for a fixed mass: 20 ÷ 32 '
               '= 0.63 mol of sulfur against 20 ÷ 40 = 0.50 mol of calcium.',
    },
    {
        "id": 'ks4-moles-s10',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the mass of 0.20 mol of hydrated magnesium '
                'sulfate, MgSO4.7H2O. Mr = 246.',
        "options": [
            '1230 g',
            '0.00081 g',
            '49.2 g',
            '24.0 g',
        ],
        "correct_index": 2,
        "why": 'mass = 0.20 × 246 = 49.2 g, and the water of '
               'crystallisation is part of the formula so it counts towards '
               'the mass.',
    },
    {
        "id": 'ks4-moles-s11',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A pure metal sample has a mass of 8.1 g and is found to '
                'contain 0.30 mol of atoms. Determine the relative atomic '
                'mass of the metal.',
        "options": [
            '0.037',
            '2.43',
            '8.4',
            '27',
        ],
        "correct_index": 3,
        "why": 'Ar = mass ÷ moles = 8.1 ÷ 0.30 = 27, which is the relative '
               'atomic mass of aluminium.',
    },
    {
        "id": 'ks4-moles-s12',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the number of moles of chloride ions in 0.25 mol '
                'of magnesium chloride, MgCl2.',
        "options": [
            '0.50 mol',
            '0.25 mol',
            '0.125 mol',
            '2.0 mol',
        ],
        "correct_index": 0,
        "why": 'Each formula unit holds two chloride ions, so there are '
               '0.25 × 2 = 0.50 mol of them.',
    },
    {
        "id": 'ks4-moles-s13',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student works out the amount of oxygen gas in a 64 g '
                'sample as 64 ÷ 16 = 4.0 mol of molecules. Ar of O = 16. '
                'Identify the error.',
        "options": [
            'They used grams when they should have used kilograms, so it is '
            '0.0040 mol',
            'Nothing is wrong, because oxygen gas is made of single atoms',
            'They used the Ar of an oxygen atom, not the Mr of O2, so it is '
            '2.0 mol',
            'They divided when they should have multiplied, so it is 1024 mol',
        ],
        "correct_index": 2,
        "why": 'Oxygen gas exists as O2 molecules with an Mr of 32, so n = '
               '64 ÷ 32 = 2.0 mol.',
    },
    {
        "id": 'ks4-moles-s14',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Washing soda is hydrated sodium carbonate, Na2CO3.10H2O, '
                'with an Mr of 286. Mr of H2O = 18. Calculate the '
                'percentage by mass of water in it.',
        "options": [
            '6.3%',
            '37.1%',
            '159%',
            '62.9%',
        ],
        "correct_index": 3,
        "why": 'The ten water molecules have a combined mass of 10 × 18 = '
               '180 out of 286, so (180 ÷ 286) × 100 = 62.9%.',
    },
    {
        "id": 'ks4-moles-s15',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the mass of 2.50 mol of sodium carbonate, '
                'Na2CO3. Ar: Na = 23, C = 12, O = 16.',
        "options": [
            '265 g',
            '207.5 g',
            '42.4 g',
            '83 g',
        ],
        "correct_index": 0,
        "why": 'Mr = (2 × 23) + 12 + (3 × 16) = 106, so mass = 2.50 × 106 = '
               '265 g.',
    },
    {
        "id": 'ks4-moles-s16',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why one mole of carbon dioxide, CO2, has a greater '
                'mass than one mole of carbon monoxide, CO.',
        "options": [
            'Carbon dioxide is a gas at room temperature while carbon '
            'monoxide is a liquid',
            'It holds one more oxygen atom per molecule, so its Mr is 44 '
            'against 28',
            'It holds more molecules per mole, because its formula is the '
            'larger one',
            'Its molecules pack together more tightly, so more fit into the '
            'same space',
        ],
        "correct_index": 1,
        "why": 'One mole of each holds the same number of molecules, but a '
               'CO2 molecule carries an extra oxygen atom, giving an Mr of '
               '44 against 28.',
    },
    {
        "id": 'ks4-moles-s17',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine which holds the greater number of atoms: 0.20 '
                'mol of argon or 0.10 mol of carbon dioxide, CO2.',
        "options": [
            'Argon, because 0.20 mol is the larger amount of substance',
            'They hold equal numbers, because a mole is the same count each '
            'time',
            'Argon, because its atoms are heavier than carbon or oxygen atoms',
            'Carbon dioxide, because 0.10 mol of it holds 0.30 mol of atoms',
        ],
        "correct_index": 3,
        "why": 'Each CO2 molecule holds three atoms, so 0.10 mol of it '
               "gives 0.30 mol of atoms against argon's 0.20 mol.",
    },
    {
        "id": 'ks4-moles-s18',
        "subtopic_slug": 'moles',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A sealed flask holds 1.4 g of nitrogen gas, N2, and 1.6 g '
                'of oxygen gas, O2. Ar: N = 14, O = 16. Determine which gas '
                'is present in the greater amount in moles.',
        "options": [
            'Nitrogen, because its molecules are the lighter of the two',
            'Oxygen, because 1.6 g is the larger of the two masses',
            'Neither, because 1.4 ÷ 28 and 1.6 ÷ 32 both come to 0.050 mol',
            'Oxygen, because its relative formula mass is the larger one',
        ],
        "correct_index": 2,
        "why": 'n(N2) = 1.4 ÷ 28 = 0.050 mol and n(O2) = 1.6 ÷ 32 = 0.050 '
               'mol, so the two amounts are equal.',
    },
    # harder ----------------------------------------------------------
    {
        "id": 'ks4-moles-h05',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '9.5 g of magnesium chloride, MgCl2, is dissolved in water '
                'so that it splits completely into ions. Mr = 95 and the '
                'Avogadro constant is 6.02 × 10²³ mol⁻¹. Calculate the '
                'number of chloride ions released.',
        "options": [
            '1.20 × 10²³',
            '6.02 × 10²²',
            '2.41 × 10²³',
            '1.20 × 10²⁴',
        ],
        "correct_index": 0,
        "why": 'n = 9.5 ÷ 95 = 0.100 mol, each formula unit releases two '
               'chloride ions, so ions = 0.200 × 6.02 × 10²³ = 1.20 × 10²³.',
    },
    {
        "id": 'ks4-moles-h06',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '0.25 mol of a metal carbonate with the formula MCO3 has a '
                'mass of 25 g. Ar: C = 12, O = 16. Determine the relative '
                'atomic mass of the metal M.',
        "options": [
            '24',
            '40',
            '100',
            '60',
        ],
        "correct_index": 1,
        "why": 'Mr = 25 ÷ 0.25 = 100, and the CO3 part accounts for 12 + 48 '
               '= 60, leaving 40 for the metal.',
    },
    {
        "id": 'ks4-moles-h07',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine which iron ore holds the greater percentage of '
                'iron by mass: haematite, Fe2O3 (Mr = 160), or magnetite, '
                'Fe3O4 (Mr = 232). Ar of Fe = 56.',
        "options": [
            'Haematite, because its relative formula mass is the smaller of '
            'the two',
            'They are equal, because both are oxides of the same metal',
            "Magnetite, at 72.4% against haematite's 70.0%",
            "Haematite, at 70.0% against magnetite's 24.1%",
        ],
        "correct_index": 2,
        "why": 'Magnetite holds 3 × 56 = 168 of every 232, or 72.4%, '
               'against 112 of every 160, or 70.0%, in haematite.',
    },
    {
        "id": 'ks4-moles-h08',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Four samples are weighed out: 4.0 g of helium (Ar = 4), '
                '2.0 g of hydrogen gas H2 (Mr = 2), 6.0 g of magnesium (Ar '
                '= 24) and 8.0 g of oxygen gas O2 (Mr = 32). Identify the '
                'one that holds one mole of atoms.',
        "options": [
            '4.0 g of helium',
            '2.0 g of hydrogen gas, H2',
            '6.0 g of magnesium',
            '8.0 g of oxygen gas, O2',
        ],
        "correct_index": 0,
        "why": '4.0 ÷ 4 = 1.00 mol of helium atoms, while the hydrogen '
               'gives 2.00 mol of atoms, the magnesium 0.25 mol and the '
               'oxygen 0.50 mol.',
    },
    {
        "id": 'ks4-moles-h09',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student finds the mass of 3.01 × 10²² molecules of '
                'methane, CH4 (Mr = 16). They write: 3.01 × 10²² ÷ 6.02 × '
                '10²³ = 0.050 mol, then mass = 0.050 ÷ 16 = 0.0031 g. '
                'Identify the error.',
        "options": [
            'Nothing is wrong, because a mass in grams is always smaller '
            'than the Mr',
            'Mass = moles × Mr, so the answer should be 0.050 × 16 = 0.80 g',
            'Moles = particles × the constant, so the answer is 1.8 × 10⁴⁶ '
            'mol',
            'The Mr of methane is 12, not 16, so the answer should be 0.60 g',
        ],
        "correct_index": 1,
        "why": 'Moles are turned into a mass by multiplying by the molar '
               'mass, so 0.050 × 16 = 0.80 g.',
    },
    {
        "id": 'ks4-moles-h10',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 10.0 g sample of rock is 60% calcium carbonate, CaCO3 '
                '(Mr = 100), by mass, the rest being sand. Calculate the '
                'amount of calcium carbonate in the sample.',
        "options": [
            '0.60 mol',
            '6.0 mol',
            '0.060 mol',
            '0.100 mol',
        ],
        "correct_index": 2,
        "why": '60% of 10.0 g is 6.0 g of calcium carbonate, so n = 6.0 ÷ '
               '100 = 0.060 mol.',
    },
    {
        "id": 'ks4-moles-h11',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A sample of aluminium oxide, Al2O3 (Mr = 102), holds 1.204 '
                '× 10²³ aluminium ions. The Avogadro constant is 6.02 × '
                '10²³ mol⁻¹. Calculate the mass of the sample.',
        "options": [
            '20.4 g',
            '5.10 g',
            '102 g',
            '10.2 g',
        ],
        "correct_index": 3,
        "why": '1.204 × 10²³ ÷ 6.02 × 10²³ = 0.200 mol of aluminium ions, '
               'and each formula unit holds two, so n(Al2O3) = 0.100 mol '
               'and mass = 0.100 × 102 = 10.2 g.',
    },
    {
        "id": 'ks4-moles-h12',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Heating 6.25 g of a hydrated salt to constant mass leaves '
                '4.00 g of the anhydrous salt, whose Mr is 160. Mr of water '
                '= 18. Determine the number of water molecules in one '
                'formula unit of the hydrate.',
        "options": [
            '5',
            '1',
            '10',
            '3',
        ],
        "correct_index": 0,
        "why": '4.00 ÷ 160 = 0.0250 mol of anhydrous salt and 2.25 ÷ 18 = '
               '0.125 mol of water, a ratio of 1 : 5.',
    },
    {
        "id": 'ks4-moles-h13',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": "Evaluate this statement: 'One mole of iron atoms and one "
                "mole of sulfur atoms have the same mass.' Ar: Fe = 56, S = "
                '32.',
        "options": [
            'It is wrong: iron has fewer atoms per mole because each of its '
            'atoms is larger',
            'It is right, provided both samples are weighed at the same '
            'temperature',
            'It is wrong: both hold 6.02 × 10²³ atoms but iron atoms are '
            'heavier, so 56 g against 32 g',
            'It is right: one mole is the same amount, so the two masses '
            'must match as well',
        ],
        "correct_index": 2,
        "why": 'A mole of each holds the same number of atoms, but the mass '
               'of a mole is the Ar in grams, so 56 g of iron against 32 g '
               'of sulfur.',
    },
    {
        "id": 'ks4-moles-h14',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A fertiliser is 80% ammonium nitrate, NH4NO3 (Mr = 80), by '
                'mass. Ar of N = 14. Calculate the mass of nitrogen in a '
                '500 g bag of the fertiliser.',
        "options": [
            '175 g',
            '70 g',
            '280 g',
            '140 g',
        ],
        "correct_index": 3,
        "why": 'The bag holds 400 g of ammonium nitrate, which is 5.00 mol, '
               'and each formula unit holds two nitrogen atoms, so 10.0 mol '
               'of nitrogen has a mass of 140 g.',
    },
    {
        "id": 'ks4-moles-h15',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine the mass of magnesium that holds the same number '
                'of atoms as 6.4 g of sulfur. Ar: Mg = 24, S = 32.',
        "options": [
            '4.8 g',
            '8.5 g',
            '6.4 g',
            '0.20 g',
        ],
        "correct_index": 0,
        "why": '6.4 ÷ 32 = 0.20 mol of sulfur atoms, and 0.20 mol of '
               'magnesium has a mass of 0.20 × 24 = 4.8 g.',
    },
    {
        "id": 'ks4-moles-h16',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why 1 g of hydrogen gas, H2, holds far more '
                'molecules than 1 g of oxygen gas, O2. Ar: H = 1, O = 16.',
        "options": [
            'Both hold the same number, because one gram is one gram '
            'whatever the gas',
            'Its Mr is 2 against 32, so 1 g is 0.5 mol of it against 0.031 '
            'mol',
            'Hydrogen is a gas at room temperature while oxygen has to be '
            'compressed',
            'Its molecules hold two atoms each while oxygen molecules hold '
            'only one',
        ],
        "correct_index": 1,
        "why": '1 g is 1 ÷ 2 = 0.5 mol of H2 but only 1 ÷ 32 = 0.031 mol of '
               'O2, and it is the amount in moles that counts the '
               'molecules.',
    },
    {
        "id": 'ks4-moles-h17',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the mass of one atom of carbon, in grams. Ar of '
                'C = 12 and the Avogadro constant is 6.02 × 10²³ mol⁻¹.',
        "options": [
            '7.22 × 10²⁴ g',
            '5.02 × 10²² g',
            '1.20 × 10⁻²³ g',
            '1.99 × 10⁻²³ g',
        ],
        "correct_index": 3,
        "why": 'One mole has a mass of 12 g and holds 6.02 × 10²³ atoms, so '
               'one atom has a mass of 12 ÷ 6.02 × 10²³ = 1.99 × 10⁻²³ g.',
    },
    {
        "id": 'ks4-moles-h18',
        "subtopic_slug": 'moles',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student needs 0.15 mol of copper(II) sulfate but the '
                'only bottle on the shelf is the hydrated salt, CuSO4.5H2O, '
                'with an Mr of 250. Determine the mass of the hydrated salt '
                'they must weigh out.',
        "options": [
            '1667 g',
            '0.15 g',
            '37.5 g',
            '24.0 g',
        ],
        "correct_index": 2,
        "why": 'One mole of the hydrate supplies one mole of copper(II) '
               'sulfate, so 0.15 × 250 = 37.5 g is needed.',
    },
]
