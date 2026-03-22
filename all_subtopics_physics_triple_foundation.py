#!/usr/bin/env python3
"""Physics subtopics — Triple Foundation (AQA 8463) — 64 subtopics"""

PHYSICS_COLOR = "#4ECDC4"

PHYSICS_SUBTOPICS_ALL = {

"energy": [{'common_mistake': 'STORES are where energy is held (kinetic, chemical, thermal etc.). PATHWAYS are how it moves '
                    "(heating, mechanical work, electrical work, radiation). 'Heat' is a transfer pathway — not a "
                    "store. You store THERMAL energy, not 'heat'.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'energy-stores-systems',
  'key_note': '8 energy stores: kinetic, thermal, chemical, gravitational PE, elastic PE, magnetic, electrostatic, '
              'nuclear. 4 pathways: mechanical work, electrical work, heating, radiation. Law of conservation of '
              'energy: energy cannot be created or destroyed.',
  'matching': {'instruction': 'Sort each into an energy store or a transfer pathway.',
               'pairs': [('Energy store',
                          "Gravitational potential — energy held due to an object's height above ground"),
                         ('Energy store', 'Chemical — energy held in the bonds of fuels, food and batteries'),
                         ('Energy store', 'Elastic potential — energy held in a stretched spring or compressed gas'),
                         ('Transfer pathway', 'Heating — thermal energy transferred from hot to cold objects'),
                         ('Transfer pathway', 'Electrical work — charge moving through a potential difference'),
                         ('Transfer pathway', 'Radiation — energy transferred by light, infrared or sound waves')],
               'title': 'Store or Pathway?'},
  'quiz': [{'opts': [('Kinetic store → gravitational potential store — the ball slows as it gains height', True),
                     ('Gravitational potential store → kinetic store — the ball is losing height', False),
                     ('Chemical store → kinetic store — energy from muscles is still being converted', False),
                     ('Thermal store → kinetic store — air warms the ball and pushes it up', False)],
            'q': 'A ball is thrown upwards and slows down. Which energy transfer is occurring?',
            'wrong_explanations': {1: 'Gravitational PE → kinetic occurs when the ball FALLS. While RISING, the ball '
                                      'slows (losing KE) and gains height (gaining GPE): kinetic → GPE.',
                                   2: 'Once released from the hand, the chemical energy of muscles is no longer '
                                      'involved — the transfer is purely kinetic → gravitational PE while rising.',
                                   3: 'Air resistance transfers some KE to thermal, but the dominant transfer while '
                                      'rising is kinetic → gravitational PE.'}},
           {'opts': [('Heating — the process of thermal energy flowing from a hot to a cold object', True),
                     ('Thermal energy — energy stored in the random motion of particles', False),
                     ('Chemical energy — energy stored in chemical bonds of fuel', False),
                     ('Nuclear energy — energy stored in atomic nuclei', False)],
            'q': 'Which of the following is an energy TRANSFER PATHWAY, not an energy store?',
            'wrong_explanations': {1: 'Thermal energy IS an energy store — energy held in the random kinetic and '
                                      'potential energy of particles. Heating is the PATHWAY by which thermal energy '
                                      'moves.',
                                   2: 'Chemical energy is a store — energy held in molecular bonds, released when '
                                      'bonds break in reactions.',
                                   3: 'Nuclear energy is a store — energy held in atomic nuclei, released in fission '
                                      'or fusion.'}}],
  'rp': None,
  'spec': '6.1.1.1',
  'summary': 'Describe energy stores and identify how energy is transferred between stores in different systems.',
  'theory': [{'content': 'A SYSTEM is an object or group of objects being studied.\n'
                         '\n'
                         'When a system changes, energy is TRANSFERRED between different energy stores — but the TOTAL '
                         'energy always stays the same.\n'
                         '\n'
                         'Examples of systems changing:\n'
                         'A ball thrown upwards: kinetic store → gravitational potential store.\n'
                         'A falling object: gravitational potential store → kinetic store.\n'
                         'A battery powering a bulb: chemical store → thermal store + light radiation.\n'
                         'A stretched spring released: elastic potential store → kinetic store.',
              'heading': 'What Is a System?'},
             {'content': 'Energy can be held in eight different STORES:\n'
                         '\n'
                         '1. KINETIC — energy stored in any moving object. Cars, wind, flowing water.\n'
                         '2. THERMAL (INTERNAL) — energy stored in the random movement of particles. Hot water, warm '
                         'air.\n'
                         '3. CHEMICAL — energy stored in chemical bonds. Food, fuel, batteries.\n'
                         '4. GRAVITATIONAL POTENTIAL — energy stored in an object due to its height. A book on a '
                         'shelf, a raised hammer.\n'
                         '5. ELASTIC POTENTIAL — energy stored in a stretched or compressed object. A stretched '
                         'spring, a drawn bow.\n'
                         '6. MAGNETIC — energy stored in magnetic fields.\n'
                         '7. ELECTROSTATIC — energy stored between charged objects.\n'
                         '8. NUCLEAR — energy stored in atomic nuclei. Released in nuclear reactions.\n'
                         '\n'
                         'Think of energy stores like BANK ACCOUNTS — energy moves between accounts but you can never '
                         'create money from nowhere. The total always stays the same.',
              'heading': 'The Eight Energy Stores'},
             {'content': 'Energy is transferred between stores via PATHWAYS:\n'
                         '\n'
                         'MECHANICAL WORK — a force acting through a distance. Pushing, lifting, stretching.\n'
                         'ELECTRICAL WORK — charge moving through a potential difference. Current in a circuit.\n'
                         'HEATING — thermal energy transferred by conduction, convection or radiation.\n'
                         'RADIATION — energy transferred by waves (light, infrared, sound etc.).\n'
                         '\n'
                         'EXAMPLES of complete energy transfers:\n'
                         'Kettle: chemical store → thermal store (water + surroundings) via heating and electrical '
                         'work.\n'
                         'Dropped ball: gravitational PE store → kinetic store → thermal store (on impact) via '
                         'mechanical work.\n'
                         'Car: chemical store → kinetic store + thermal store (engine heat, friction, air '
                         'resistance).\n'
                         '\n'
                         'The LAW OF CONSERVATION OF ENERGY: energy cannot be created or destroyed — only transferred '
                         'between stores or dissipated.',
              'heading': 'Energy Pathways'}],
  'title': 'Energy Stores and Systems',
  'triple_only': None,
  'variables': [('E', 'Energy', 'joules', 'J')]},
 {'common_mistake': 'In Ek = ½mv², SQUARE THE SPEED FIRST before multiplying. Write out v² before doing anything else. '
                    'Also: mass in kg, speed in m/s. Convert 500 g → 0.5 kg and 72 km/h → 20 m/s before substituting.',
  'equations': ['Ek = ½ × m × v²', 'Ep = m × g × h', 'Ee = ½ × k × e²'],
  'fifas': [{'label': 'Kinetic Energy',
             'question': 'A 70 kg cyclist travels at 6 m/s. Calculate the kinetic energy.',
             'steps': [('F', 'Ek = ½ × m × v²'),
                       ('I', 'm = 70 kg, v = 6 m/s'),
                       ('F', 'v² = 6² = 36; Ek = ½ × 70 × 36 = ½ × 2520'),
                       ('A', 'Ek = 1260 J')]},
            {'label': 'Gravitational PE',
             'question': 'A 5 kg box is lifted 3 m. Calculate the GPE gained. (g = 9.8 N/kg)',
             'steps': [('F', 'Ep = m × g × h'),
                       ('I', 'm = 5 kg, g = 9.8 N/kg, h = 3 m'),
                       ('F', 'Ep = 5 × 9.8 × 3 = 5 × 29.4'),
                       ('A', 'Ep = 147 J')]}],
  'higher': None,
  'id': 'changes-in-energy',
  'key_note': 'Ek = ½mv² (kinetic). Ep = mgh (gravitational PE, g = 9.8 N/kg Earth). Ee = ½ke² (elastic PE). Doubling '
              'speed → ×4 kinetic energy. Doubling extension → ×4 elastic PE. All three equations need mass in kg and '
              'distance in m.',
  'matching': {'instruction': 'Match each energy type to its equation.',
               'pairs': [('Kinetic energy', 'Ek = ½mv² — depends on mass and speed squared'),
                         ('Gravitational PE', 'Ep = mgh — depends on mass, gravitational field strength, and height'),
                         ('Elastic PE', 'Ee = ½ke² — depends on spring constant and extension squared'),
                         ('g on Earth', '9.8 N/kg — or 10 N/kg used for estimates')],
               'title': 'Energy Equation Match'},
  'quiz': [{'opts': [('160,000 J — Ek = ½ × 800 × 20² = ½ × 800 × 400 = 160,000 J', True),
                     ('8000 J — forgot to square the speed: ½ × 800 × 20 = 8000', False),
                     ('320,000 J — forgot the ½: 800 × 400 = 320,000', False),
                     ('16,000 J — used speed not speed squared: ½ × 800 × 40', False)],
            'q': 'An 800 kg car travels at 20 m/s. What is its kinetic energy?',
            'wrong_explanations': {1: 'Must square the speed first: 20² = 400. Then ½ × 800 × 20 = 8000 — missing the '
                                      'squared step.',
                                   2: 'The ½ is essential in the kinetic energy formula — without it the answer '
                                      'doubles.',
                                   3: '16,000 comes from ½ × 800 × 40 — this would be the answer if v = √40, not v = '
                                      '20.'}},
           {'opts': [('2 J — Ee = ½ × 400 × 0.1² = ½ × 400 × 0.01 = 2 J', True),
                     ('4 J — forgot the ½: 400 × 0.01 = 4 J', False),
                     ('20 J — forgot to square the extension: ½ × 400 × 0.1 = 20', False),
                     ('40 J — forgot both ½ and to square: 400 × 0.1 = 40', False)],
            'q': 'A spring with k = 400 N/m is compressed 0.1 m. What elastic PE is stored?',
            'wrong_explanations': {1: 'The ½ is part of the formula: Ee = ½ke². Without ½: 400 × 0.01 = 4 J.',
                                   2: 'Extension must be squared first: 0.1² = 0.01. ½ × 400 × 0.1 = 20 is missing the '
                                      'squaring.',
                                   3: 'Both the ½ AND the squaring are missing: must be Ee = ½ × k × e².'}}],
  'rp': None,
  'spec': '6.1.1.2',
  'summary': 'Calculate kinetic energy, gravitational potential energy and elastic potential energy.',
  'theory': [{'content': 'KINETIC ENERGY (Ek) is the energy stored in any moving object.\n'
                         '\n'
                         'EQUATION:\n'
                         'Ek = ½ × m × v²\n'
                         '\n'
                         'Ek = kinetic energy (J)\n'
                         'm = mass (kg)\n'
                         'v = speed (m/s)\n'
                         '\n'
                         'Key points:\n'
                         'Kinetic energy depends on the SQUARE of speed — doubling speed QUADRUPLES kinetic energy.\n'
                         'Any moving object has kinetic energy: cars, wind, flowing water, planets.\n'
                         '\n'
                         'EXAMPLE:\n'
                         '1000 kg car at 20 m/s:\n'
                         'Ek = ½ × 1000 × 20² = ½ × 1000 × 400 = 200,000 J = 200 kJ',
              'heading': 'Kinetic Energy'},
             {'content': 'GRAVITATIONAL POTENTIAL ENERGY (Ep) is the energy stored in an object due to its HEIGHT '
                         'above the ground.\n'
                         '\n'
                         'EQUATION:\n'
                         'Ep = m × g × h\n'
                         '\n'
                         'Ep = gravitational potential energy (J)\n'
                         'm = mass (kg)\n'
                         'g = gravitational field strength (N/kg) — on Earth: g = 9.8 N/kg\n'
                         'h = height above ground (m)\n'
                         '\n'
                         'Key points:\n'
                         'GPE increases as height increases.\n'
                         'GPE depends on mass — heavier objects store more GPE at the same height.\n'
                         'g = 9.8 N/kg on Earth; use g = 10 N/kg for estimates.\n'
                         '\n'
                         'EXAMPLE:\n'
                         '2 kg book on a shelf 1.5 m above the floor:\n'
                         'Ep = 2 × 9.8 × 1.5 = 29.4 J',
              'heading': 'Gravitational Potential Energy'},
             {'content': 'ELASTIC POTENTIAL ENERGY (Ee) is the energy stored in a stretched or compressed elastic '
                         'object.\n'
                         '\n'
                         'EQUATION:\n'
                         'Ee = ½ × k × e²\n'
                         '\n'
                         'Ee = elastic potential energy (J)\n'
                         'k = spring constant (N/m) — stiffness of the spring\n'
                         'e = extension or compression (m)\n'
                         '\n'
                         'Key points:\n'
                         "Only valid within the ELASTIC LIMIT (Hooke's Law region).\n"
                         'A stiffer spring (larger k) stores more energy for the same extension.\n'
                         'Elastic PE depends on extension SQUARED — doubling extension quadruples stored energy.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Spring with k = 200 N/m stretched 0.05 m:\n'
                         'Ee = ½ × 200 × 0.05² = ½ × 200 × 0.0025 = 0.25 J',
              'heading': 'Elastic Potential Energy'}],
  'title': 'Changes in Energy',
  'triple_only': None,
  'variables': [('Ek', 'Kinetic energy', 'joules', 'J'),
                ('Ep', 'Gravitational potential energy', 'joules', 'J'),
                ('Ee', 'Elastic potential energy', 'joules', 'J'),
                ('m', 'Mass', 'kilograms', 'kg'),
                ('v', 'Speed', 'm/s', 'm/s'),
                ('g', 'Gravitational field strength', 'N/kg', 'N/kg'),
                ('h', 'Height', 'metres', 'm'),
                ('k', 'Spring constant', 'N/m', 'N/m'),
                ('e', 'Extension', 'metres', 'm')]},
 {'common_mistake': 'Temperature change (Δθ) is final temperature MINUS initial temperature — not the final '
                    'temperature alone. If water heats from 20°C to 60°C, Δθ = 40°C, not 60°C. Also: mass must be in '
                    'kg — convert grams first (÷1000).',
  'equations': ['ΔE = m × c × Δθ'],
  'fifas': [{'label': 'SHC Calculation',
             'question': 'How much energy is needed to heat 0.5 kg of water from 25°C to 85°C? (c = 4200 J/kg°C)',
             'steps': [('F', 'ΔE = m × c × Δθ'),
                       ('I', 'm = 0.5 kg, c = 4200, Δθ = 85 − 25 = 60°C'),
                       ('F', 'ΔE = 0.5 × 4200 × 60 = 0.5 × 252,000'),
                       ('A', 'ΔE = 126,000 J (126 kJ)')]}],
  'higher': None,
  'id': 'energy-changes-in-systems',
  'key_note': 'SHC (c): energy to raise 1 kg by 1°C. ΔE = mcΔθ. Water c = 4200 J/kg°C (very high). Δθ = final − '
              'initial. Rearrange for any unknown. RP14: electric heater method. High SHC of water → used in heating '
              'systems and car cooling.',
  'matching': {'instruction': 'Match each substance and application to the correct SHC fact.',
               'pairs': [('Water (c = 4200 J/kg°C)',
                          'Highest common SHC — used in central heating, car cooling, moderates ocean climate'),
                         ('Aluminium (c = 900 J/kg°C)',
                          'Higher SHC than iron — heats more slowly for same energy input'),
                         ('Δθ = final − initial temp', 'Temperature CHANGE — not the final temperature alone'),
                         ('ΔE = mcΔθ', 'Calculates thermal energy change for any heating or cooling process')],
               'title': 'SHC Application Match'},
  'quiz': [{'opts': [('108,000 J — ΔE = 2 × 450 × 120 = 108,000 J (Δθ = 150 − 30 = 120°C)', True),
                     ('27,000 J — used final temperature (30°C) not temperature change (120°C)', False),
                     ('135,000 J — used initial temperature (150°C) not temperature change', False),
                     ('1350 J — divided instead of multiplied', False)],
            'q': 'A 2 kg iron block (c = 450 J/kg°C) cools from 150°C to 30°C. How much energy is released?',
            'wrong_explanations': {1: 'Δθ = 150 − 30 = 120°C is the temperature CHANGE. Using 30°C gives ΔE = 2 × 450 '
                                      '× 30 = 27,000 J — using the final temperature, not the change.',
                                   2: 'Δθ is not the initial temperature — it is the CHANGE (150 − 30 = 120). 2 × 450 '
                                      '× 150 = 135,000 J is too large.',
                                   3: 'ΔE = m × c × Δθ requires multiplication — 2 × 450 × 120 = 108,000 J.'}},
           {'opts': [('Water has a very high SHC (4200 J/kg°C) — it carries large amounts of thermal energy per kg per '
                      '°C rise, so less water is needed',
                      True),
                     ('Water has a low SHC — it heats up quickly so the system responds faster', False),
                     ('Water is denser than most liquids — it carries more energy due to its mass', False),
                     ('Water has zero SHC at 100°C — it conducts heat perfectly at boiling point', False)],
            'q': 'Why is water used in central heating systems rather than a cheaper liquid?',
            'wrong_explanations': {1: "The opposite is true — water's HIGH SHC is the key property. A low SHC would "
                                      'mean it heats quickly but also loses heat quickly and carries less energy.',
                                   2: "Water is less dense than many metals — density is not the primary reason it's "
                                      'used in heating systems.',
                                   3: "SHC doesn't become zero at any temperature — SHC is a property of the material, "
                                      'roughly constant over normal temperature ranges.'}}],
  'rp': 'RP14 (Physics) — Determine the specific heat capacity of a material using an electric heater, thermometer and '
        'balance. E = Pt gives energy input; rearrange ΔE = mcΔθ to find c.',
  'spec': '6.1.1.3',
  'summary': 'Use specific heat capacity to calculate energy changes when substances are heated or cooled.',
  'theory': [{'content': 'Different materials need DIFFERENT amounts of energy to raise their temperature by the same '
                         'amount. This is described by SPECIFIC HEAT CAPACITY (c).\n'
                         '\n'
                         'DEFINITION:\n'
                         'The specific heat capacity of a substance is the amount of energy needed to raise the '
                         'temperature of 1 kg of the substance by 1°C.\n'
                         '\n'
                         'EQUATION:\n'
                         'ΔE = m × c × Δθ\n'
                         '\n'
                         'ΔE = change in thermal energy (J)\n'
                         'm = mass (kg)\n'
                         'c = specific heat capacity (J/kg°C)\n'
                         'Δθ = temperature change (°C)\n'
                         '\n'
                         'Common SHC values:\n'
                         'Water: 4200 J/kg°C\n'
                         'Aluminium: 900 J/kg°C\n'
                         'Iron/steel: 450 J/kg°C\n'
                         'Copper: 385 J/kg°C\n'
                         '\n'
                         'Water has a very HIGH SHC — it takes a lot of energy to heat it. This makes it ideal for '
                         'carrying and storing thermal energy.',
              'heading': 'Specific Heat Capacity'},
             {'content': 'The equation ΔE = mcΔθ can be rearranged:\n'
                         'Δθ = ΔE ÷ (m × c)\n'
                         'm = ΔE ÷ (c × Δθ)\n'
                         'c = ΔE ÷ (m × Δθ)\n'
                         '\n'
                         'EXAMPLE 1 — Energy needed:\n'
                         'Heat 2 kg of water from 20°C to 100°C:\n'
                         'Δθ = 100 − 20 = 80°C\n'
                         'ΔE = 2 × 4200 × 80 = 672,000 J = 672 kJ\n'
                         '\n'
                         'EXAMPLE 2 — Temperature change:\n'
                         '27,000 J heats a 3 kg aluminium block (c = 900 J/kg°C):\n'
                         'Δθ = 27,000 ÷ (3 × 900) = 27,000 ÷ 2700 = 10°C\n'
                         '\n'
                         'The same equation applies when objects COOL — ΔE is the energy released.',
              'heading': 'Using the SHC Equation'},
             {'content': 'WHY WATER IS USED IN RADIATORS AND COOLING SYSTEMS:\n'
                         'High SHC = carries large amounts of thermal energy per kg per °C → less water needed to heat '
                         'a room.\n'
                         'Car cooling systems: water absorbs heat from the engine efficiently.\n'
                         'Oceans: high SHC means they absorb huge amounts of solar energy → moderate coastal '
                         'climates.\n'
                         '\n'
                         'REQUIRED PRACTICAL:\n'
                         'RP14 — Determine the SHC of a material:\n'
                         'Heat a known mass with an electric heater of known power.\n'
                         'Record temperature change over time.\n'
                         'Energy input: E = P × t\n'
                         'Compare to ΔE = mcΔθ → rearrange for c.\n'
                         '\n'
                         'SOURCES OF ERROR in RP14:\n'
                         'Heat loss to surroundings → measured c higher than true value.\n'
                         'Heat not fully transferred to material → same direction of error.\n'
                         'Minimise by lagging (insulating) the material being heated.',
              'heading': 'Applications of Specific Heat Capacity'}],
  'title': 'Energy Changes in Systems',
  'triple_only': None,
  'variables': [('ΔE', 'Change in thermal energy', 'joules', 'J'),
                ('m', 'Mass', 'kilograms', 'kg'),
                ('c', 'Specific heat capacity', 'J/kg°C', 'J/kg°C'),
                ('Δθ', 'Temperature change', 'degrees Celsius', '°C')]},
 {'common_mistake': "Time MUST be in SECONDS when using P = E/t with energy in joules. '5 minutes' = 300 s, NOT 5. "
                    'Forgetting to convert is the most common mistake in power calculations.',
  'equations': ['P = E ÷ t', 'P = W ÷ t', 'E = P × t'],
  'fifas': [{'label': 'Power — Stair Climb',
             'question': 'A 50 kg student climbs 4 m of stairs in 5 seconds. Calculate her power output. (g = 9.8 '
                         'N/kg)',
             'steps': [('F', 'P = W ÷ t, where W = m × g × h'),
                       ('I', 'W = 50 × 9.8 × 4 = 1960 J; t = 5 s'),
                       ('F', 'P = 1960 ÷ 5'),
                       ('A', 'P = 392 W')]}],
  'higher': None,
  'id': 'power',
  'key_note': 'Power = rate of energy transfer. P = E/t = W/t. Unit: watt (W) = J/s. E = Pt. Always convert time to '
              'seconds. Higher power = same work done faster. P = mgh/t for climbing problems.',
  'matching': {'instruction': 'Match each scenario to the correct power value.',
               'pairs': [('100 W', 'Device transfers 1000 J in 10 s — P = 1000 ÷ 10'),
                         ('500 W', 'Motor does 30,000 J of work in 1 minute — P = 30,000 ÷ 60'),
                         ('200 W', 'Engine transfers 24,000 J in 2 minutes — P = 24,000 ÷ 120'),
                         ('1 W', '1 joule transferred every second — the definition of 1 watt')],
               'title': 'Power Values'},
  'quiz': [{'opts': [('360,000 J — E = 2000 × (3 × 60) = 2000 × 180 = 360,000 J', True),
                     ('6000 J — used minutes not seconds: E = 2000 × 3', False),
                     ('11.1 J — divided instead of multiplied: 2000 ÷ 180', False),
                     ('6,000,000 J — multiplied by 3000 instead of 180', False)],
            'q': 'A 2000 W heater is on for 3 minutes. How much energy does it transfer?',
            'wrong_explanations': {1: '3 minutes must be converted to seconds: 3 × 60 = 180 s. E = 2000 × 3 = 6000 J '
                                      'uses minutes, not seconds.',
                                   2: 'P = E/t → E = P × t, not P ÷ t.',
                                   3: '3 minutes = 180 s, not 3000 s. E = 2000 × 180 = 360,000 J.'}},
           {'opts': [("A has twice B's power — same work (mgh), but A does it in half the time", True),
                     ('Both have the same power — they do the same total work', False),
                     ('B has more power — taking longer means working harder overall', False),
                     ('Cannot compare — they take different times so cannot use the same equation', False)],
            'q': 'Two students both lift a 10 kg bag 5 m. Student A takes 10 s, B takes 20 s. How do their power '
                 'outputs compare?',
            'wrong_explanations': {1: 'Same work ÷ same time = same power — but the TIMES ARE DIFFERENT. P = W/t; A: P '
                                      "= mgh/10; B: P = mgh/20. A's power is twice B's.",
                                   2: 'More time for the same work = LESS power. B takes longer so B has lower power.',
                                   3: 'The same equation P = W/t applies to both — using different times is exactly '
                                      'how power differs between them.'}}],
  'rp': None,
  'spec': '6.1.1.4',
  'summary': 'Define power as rate of energy transfer and calculate power from energy and time.',
  'theory': [{'content': 'POWER is the RATE at which energy is transferred or work is done.\n'
                         '\n'
                         'Power tells us how QUICKLY energy is being used — not how much total energy.\n'
                         '\n'
                         'EQUATIONS:\n'
                         'P = E ÷ t\n'
                         'P = W ÷ t\n'
                         '\n'
                         'P = power (W)\n'
                         'E = energy transferred (J)\n'
                         'W = work done (J)\n'
                         't = time (s)\n'
                         '\n'
                         'UNIT: watt (W) = 1 joule per second\n'
                         '1 kilowatt (kW) = 1000 W\n'
                         '1 megawatt (MW) = 1,000,000 W\n'
                         '\n'
                         'Rearrangements:\n'
                         'E = P × t\n'
                         't = E ÷ P',
              'heading': 'What Is Power?'},
             {'content': 'Two machines can do the SAME total work — but the more powerful one does it FASTER.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Machine A: 1000 J in 10 s → P = 100 W\n'
                         'Machine B: 1000 J in 5 s → P = 200 W\n'
                         'Machine B is twice as powerful — same work, half the time.\n'
                         '\n'
                         'Typical power values:\n'
                         '100 W lightbulb → 100 J/s transferred\n'
                         '2000 W kettle → 2000 J/s transferred\n'
                         '1000 W (≈1 kW) — elite sprinter sustained output\n'
                         '50–150 kW — typical car engine\n'
                         '\n'
                         'POWER AND WORK DONE IN CLIMBING:\n'
                         'P = mgh ÷ t\n'
                         'This combines Ep = mgh with P = W/t — useful for stair/ramp problems.',
              'heading': 'Comparing Power'},
             {'content': 'ALWAYS convert time to SECONDS before calculating:\n'
                         '1 minute = 60 s\n'
                         '1 hour = 3600 s\n'
                         '\n'
                         'EXAMPLE 1 — finding energy:\n'
                         'A 60 W bulb on for 5 minutes:\n'
                         't = 5 × 60 = 300 s\n'
                         'E = 60 × 300 = 18,000 J\n'
                         '\n'
                         'EXAMPLE 2 — finding power:\n'
                         'A motor transfers 36,000 J in 2 minutes:\n'
                         't = 2 × 60 = 120 s\n'
                         'P = 36,000 ÷ 120 = 300 W\n'
                         '\n'
                         'EXAMPLE 3 — stair climb:\n'
                         '60 kg person climbs 3 m in 4 seconds (g = 9.8):\n'
                         'W = mgh = 60 × 9.8 × 3 = 1764 J\n'
                         'P = 1764 ÷ 4 = 441 W',
              'heading': 'Energy, Power and Time Calculations'}],
  'title': 'Power',
  'triple_only': None,
  'variables': [('P', 'Power', 'watts', 'W'),
                ('E', 'Energy transferred', 'joules', 'J'),
                ('W', 'Work done', 'joules', 'J'),
                ('t', 'Time', 'seconds', 's')]},
 {'common_mistake': "Energy is NEVER destroyed — it is dissipated to less useful stores. 'Lost' energy has been "
                    'transferred to the thermal energy of the surroundings — it is still there, just spread out and '
                    "difficult to use again. Never say energy is 'used up' or 'gone'.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'energy-transfers-in-a-system',
  'key_note': 'Conservation of energy: never created or destroyed. Dissipation: energy spreads to surroundings as '
              'thermal — less useful. Reduce by: lubrication (friction), streamlining (air resistance), insulation '
              '(thermal loss), better conductors (electrical resistance). Wasted = total input − useful output.',
  'matching': {'instruction': 'Match each energy dissipation cause to its solution.',
               'pairs': [('Friction between moving parts',
                          'Lubrication with oil — reduces surface contact, less thermal energy wasted'),
                         ('Air resistance on moving objects',
                          'Streamlining — aerodynamic shape lets air flow smoothly, less energy transferred to air'),
                         ('Thermal loss from buildings',
                          'Insulation — thick walls, double glazing, loft insulation reduce conduction rate'),
                         ('Electrical resistance in wires',
                          'Thicker wires or lower-resistance materials — less heat generated by current')],
               'title': 'Reducing Dissipation'},
  'quiz': [{'opts': [('Dissipated to thermal stores of the surrounding air and pivot through air resistance and '
                      'friction',
                      True),
                     ('The energy is destroyed — the pendulum stopping proves this', False),
                     ("Stored in the pendulum's elastic potential energy store ready to restart", False),
                     ('Converted to sound only, which then disappears', False)],
            'q': 'A pendulum swings and eventually stops. Where has the energy gone?',
            'wrong_explanations': {1: 'Energy is NEVER destroyed — this violates the law of conservation of energy. '
                                      'The pendulum slows because energy is dissipated, not destroyed.',
                                   2: 'Once stopped, the pendulum has no stored elastic PE — it is hanging at rest and '
                                      'any elastic PE would have been released.',
                                   3: 'Some sound is produced, but sound also eventually dissipates to thermal energy '
                                      'in the air. No energy disappears — all ends up as thermal energy of the '
                                      'surroundings.'}},
           {'opts': [('It slows the rate of thermal energy transfer from the warm house to the cold surroundings — '
                      'less energy needed to maintain temperature',
                      True),
                     ('It generates heat from the solar radiation it absorbs', False),
                     ('It stores thermal energy during the day and releases it at night', False),
                     ('It prevents cold draughts entering through the roof — stopping convection', False)],
            'q': 'Why does adding loft insulation reduce heating bills?',
            'wrong_explanations': {1: 'Loft insulation works by reducing CONDUCTION through the ceiling — the fibres '
                                      'trap air (poor thermal conductor) and slow heat loss.',
                                   2: 'While insulation has thermal mass, this is not its primary mechanism — reducing '
                                      'the RATE of heat loss is.',
                                   3: 'Loft insulation does reduce some convection at the ceiling, but its primary '
                                      'mechanism is reducing thermal CONDUCTION.'}}],
  'rp': None,
  'spec': '6.1.2.1',
  'summary': 'Describe how energy is conserved, dissipated and how unwanted transfers can be reduced.',
  'theory': [{'content': 'The LAW OF CONSERVATION OF ENERGY:\n'
                         'Energy cannot be CREATED or DESTROYED — it can only be TRANSFERRED between stores or '
                         'DISSIPATED.\n'
                         '\n'
                         'In a CLOSED SYSTEM:\n'
                         'Total energy before = Total energy after — always.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Swinging pendulum: KE ⇌ GPE, cycling continuously (ignoring air resistance).\n'
                         'Bouncing ball: GPE → KE → elastic PE → KE → GPE → lower each time (energy dissipated).\n'
                         'Battery-powered torch: chemical → electrical → light + thermal.\n'
                         '\n'
                         'Energy is never destroyed — but it can become less USEFUL when it spreads out into the '
                         'thermal stores of the surroundings.',
              'heading': 'Conservation of Energy'},
             {'content': 'DISSIPATION: energy transferred to less useful stores — typically the thermal stores of the '
                         'surroundings.\n'
                         '\n'
                         'Dissipated energy is described as WASTED — not used for the intended purpose.\n'
                         '\n'
                         'Causes of dissipation:\n'
                         'FRICTION — between moving parts → thermal energy.\n'
                         'AIR RESISTANCE — object transfers energy to air.\n'
                         'ELECTRICAL RESISTANCE — current in wires → heat.\n'
                         'SOUND — vibrations dissipate energy to the air.\n'
                         '\n'
                         'Once energy is dissipated into the surroundings, it spreads out and becomes very difficult '
                         'to use again.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Car: chemical PE → useful KE + wasted thermal (engine, brakes, air resistance).\n'
                         'Filament bulb: electrical → useful light (10%) + wasted thermal (90%).\n'
                         'Phone charging: electrical → chemical store + thermal (phone gets warm).',
              'heading': 'Dissipation of Energy'},
             {'content': 'LUBRICATION — oil between moving parts reduces friction → less thermal wasted.\n'
                         'STREAMLINING — aerodynamic shapes reduce air resistance → less energy to air.\n'
                         'INSULATION — reduces thermal transfer to/from surroundings:\n'
                         'Thick walls, double glazing, loft insulation, cavity wall insulation.\n'
                         'BETTER CONDUCTORS — lower resistance in wires → less electrical energy wasted as heat.\n'
                         'SUPERCONDUCTORS — zero resistance at very low temperatures → zero electrical energy wasted.\n'
                         '\n'
                         'There is always a practical limit — beyond a certain point, the cost of further improvements '
                         'outweighs the energy saved.',
              'heading': 'Reducing Unwanted Energy Transfers'}],
  'title': 'Energy Transfers in a System',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Efficiency = useful output ÷ TOTAL INPUT — not useful ÷ wasted. Result must be ≤ 1 (≤ 100%). If '
                    'your answer exceeds 1, you have divided the wrong way. Wasted energy = total input − useful '
                    'output (not the denominator).',
  'equations': ['efficiency = useful output energy ÷ total input energy',
                'efficiency = useful power output ÷ total power input',
                'efficiency (%) = (useful output ÷ total input) × 100'],
  'fifas': [{'label': 'Efficiency Calculation',
             'question': 'A car engine uses 20,000 J of chemical energy and produces 7,000 J of useful kinetic energy. '
                         'Calculate its efficiency.',
             'steps': [('F', 'efficiency = useful output energy ÷ total input energy'),
                       ('I', 'efficiency = 7000 ÷ 20,000'),
                       ('F', 'efficiency = 0.35'),
                       ('A', 'efficiency = 0.35 (35%)')]}],
  'higher': 'Describe specific ways to increase efficiency for a given device or system and justify each: lubrication '
            'reduces friction losses, streamlining reduces air resistance, thermal insulation reduces heat loss to '
            'surroundings, regenerative braking captures KE. Evaluate cost vs benefit of efficiency improvements.',
  'id': 'efficiency',
  'key_note': 'Efficiency = useful output ÷ total input (decimal, 0–1) or × 100 for %. Wasted = total − useful. Sankey '
              'diagrams: arrow width ∝ energy amount. Improve: reduce friction (lube), reduce air resistance '
              '(streamline), reduce heat loss (insulation), use LEDs. Max efficiency = 100% (never exceeded).',
  'matching': {'instruction': 'Match each device to its efficiency.',
               'pairs': [('0.75 (75%)', 'Motor: 300 J input, 225 J useful mechanical output — 225÷300'),
                         ('0.10 (10%)', 'Incandescent bulb: 100 J electrical, 10 J light — 10÷100'),
                         ('0.40 (40%)', 'Engine: 500 J chemical, 200 J kinetic — 200÷500'),
                         ('0.90 (90%)', 'LED lamp: 100 J electrical, 90 J light — 90÷100')],
               'title': 'Efficiency Values'},
  'quiz': [{'opts': [('200 J — useful = 0.6 × 500 = 300 J; wasted = 500 − 300 = 200 J', True),
                     ('300 J — this is the useful output, not the wasted amount', False),
                     ('500 J — all energy is wasted at efficiency 0.6', False),
                     ('833 J — dividing 500 ÷ 0.6', False)],
            'q': 'A device has efficiency 0.6 and is supplied with 500 J. How much energy is wasted?',
            'wrong_explanations': {1: '300 J is the USEFUL output (60% of 500). WASTED = total − useful = 500 − 300 = '
                                      '200 J.',
                                   2: 'At efficiency 0.6, only 40% (200 J) is wasted — not all 500 J.',
                                   3: '500 ÷ 0.6 = 833 J: this would be the input needed to get 500 J useful output, '
                                      'not the wasted energy.'}},
           {'opts': [('89 J/s — LED wastes 1 J/s, bulb wastes 90 J/s; difference = 89 J/s', True),
                     ('0 J/s — both produce the same useful light so waste must be equal', False),
                     ('10 J/s — the useful output is 10 J/s so waste is also 10 J/s', False),
                     ('100 J/s — the bulb uses 100 J/s so wastes all of it', False)],
            'q': 'An LED uses 11 J/s total and produces 10 J/s of light. A filament bulb produces the same 10 J/s of '
                 'light but uses 100 J/s. How much more energy per second does the bulb waste?',
            'wrong_explanations': {1: 'Same USEFUL output does NOT mean same waste. LED: wastes 11 − 10 = 1 J/s. Bulb: '
                                      'wastes 100 − 10 = 90 J/s. Difference = 89 J/s.',
                                   2: 'Wasted = total − useful. The TOTAL inputs are very different (11 vs 100 J/s).',
                                   3: 'Bulb uses 100 J/s but 10 J/s is useful light — it wastes 90 J/s, not 100 '
                                      'J/s.'}}],
  'rp': None,
  'spec': '6.1.2.2',
  'summary': 'Calculate efficiency as a decimal or percentage and interpret Sankey diagrams.',
  'theory': [{'content': 'EFFICIENCY measures what fraction of total input energy becomes USEFUL output.\n'
                         '\n'
                         'No device is 100% efficient — some energy is always dissipated as thermal energy or sound.\n'
                         '\n'
                         'EQUATIONS:\n'
                         'efficiency = useful output energy ÷ total input energy\n'
                         'efficiency = useful power output ÷ total power input\n'
                         '\n'
                         'Express as:\n'
                         'DECIMAL: 0 to 1 (e.g. 0.75)\n'
                         'PERCENTAGE: multiply decimal by 100 (e.g. 75%)\n'
                         '\n'
                         'Max efficiency = 1 (100%) — impossible in practice.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Motor: 200 J electrical input, 150 J useful mechanical output, 50 J wasted as heat.\n'
                         'Efficiency = 150 ÷ 200 = 0.75 = 75%\n'
                         'Wasted = 200 − 150 = 50 J',
              'heading': 'Efficiency — Definition and Equations'},
             {'content': 'A SANKEY DIAGRAM shows energy transfers visually:\n'
                         'Arrow WIDTH is proportional to the amount of energy.\n'
                         'Input arrow on the left. Useful output arrow goes right. Wasted outputs go downward.\n'
                         '\n'
                         'Reading a Sankey diagram:\n'
                         'Efficiency = width of useful output ÷ width of input arrow.\n'
                         'The input arrow = sum of ALL output arrows.\n'
                         '\n'
                         'EXAMPLE — incandescent bulb (very inefficient):\n'
                         'Input: 100 J electrical\n'
                         'Useful light output: 10 J (thin right arrow)\n'
                         'Wasted heat: 90 J (wide downward arrow)\n'
                         'Efficiency = 10 ÷ 100 = 0.10 = 10%\n'
                         '\n'
                         'EXAMPLE — LED bulb (efficient):\n'
                         'Input: 100 J\n'
                         'Useful light: 90 J\n'
                         'Wasted heat: 10 J\n'
                         'Efficiency = 90 ÷ 100 = 0.90 = 90%',
              'heading': 'Sankey Diagrams'},
             {'content': 'REDUCE FRICTION: lubricate moving parts → less thermal wasted.\n'
                         'REDUCE AIR RESISTANCE: streamlined shapes → less energy to air.\n'
                         'BETTER INSULATION: less thermal energy escapes hot devices.\n'
                         'BETTER COMPONENTS: LED lights instead of filament bulbs → more light, less heat.\n'
                         'REGENERATIVE BRAKING: hybrid/electric cars capture braking KE → stored in battery rather '
                         'than wasted as thermal.\n'
                         '\n'
                         'WHY EFFICIENCY MATTERS:\n'
                         'Higher efficiency → less fuel for same useful output → lower costs.\n'
                         'Less fuel → less CO₂ → lower environmental impact.\n'
                         'But: no device can exceed 100% efficiency.',
              'heading': 'Improving Efficiency'}],
  'title': 'Efficiency',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Bio-fuels ARE renewable — the plants regrow. Nuclear is NOT renewable — uranium is finite. '
                    "Hydroelectric, wind, tidal and wave are all renewable. Also: 'renewable' does NOT mean 'zero "
                    "environmental impact' — every resource has some impact.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'energy-resources',
  'key_note': 'Non-renewable: fossil fuels + nuclear. Renewable: wind, solar, hydro, bio-fuel, geothermal, tidal, '
              'wave. Most generation: turbine + generator (except solar PV). Fossil fuels: reliable, high energy '
              'density, but CO₂ + pollution. Renewables: lower impact but often intermittent. Nuclear: no CO₂ but '
              'radioactive waste.',
  'matching': {'instruction': 'Match each resource to its type and main concern.',
               'pairs': [('Non-renewable', 'Coal — CO₂ and SO₂ when burned; finite supply'),
                         ('Non-renewable', 'Nuclear — radioactive waste; uranium is finite'),
                         ('Renewable', 'Wind — no CO₂ during operation; intermittent; noise and visual impact'),
                         ('Renewable', 'Hydroelectric — no CO₂; reliable; dam flooding destroys habitats'),
                         ('Renewable', 'Bio-fuel — roughly carbon neutral; land use competes with food crops')],
               'title': 'Energy Resource — Type and Impact'},
  'quiz': [{'opts': [('Geothermal — heat from inside the Earth is continuously produced and will not run out on human '
                      'timescales',
                      True),
                     ('Nuclear — uranium can be recycled so supplies will not run out', False),
                     ('Coal — new coal forms continuously from organic material', False),
                     ('Natural gas — underground reserves are replenished by geological processes', False)],
            'q': 'Which of the following energy resources is renewable?',
            'wrong_explanations': {1: 'Nuclear fuel is FINITE — while some can be reprocessed, uranium supplies will '
                                      'eventually run out. It is non-renewable.',
                                   2: 'Coal takes MILLIONS of years to form — it is not replenished on any '
                                      'human-relevant timescale. Non-renewable.',
                                   3: 'Natural gas reserves are being used far faster than they form — a finite, '
                                      'non-renewable resource.'}},
           {'opts': [('They only generate electricity when the sun shines or wind blows — output is variable and '
                      'cannot be guaranteed on demand',
                      True),
                     ('They are expensive to maintain and break down frequently', False),
                     ('They produce too much electricity at peak times, requiring regular shutdown', False),
                     ('They can only be used in specific countries, not globally', False)],
            'q': "Why are solar and wind described as 'intermittent' energy sources?",
            'wrong_explanations': {1: "'Intermittent' refers specifically to VARIABLE, WEATHER-DEPENDENT output — not "
                                      'maintenance reliability.',
                                   2: "Overproduction is a grid-management challenge but 'intermittent' specifically "
                                      'means UNPREDICTABLE output dependent on weather, not overproduction.',
                                   3: "Wind and solar are used globally — 'intermittent' describes the "
                                      'time-variability of output, not geographic limitation.'}}],
  'rp': None,
  'spec': '6.1.3',
  'summary': 'Compare renewable and non-renewable energy resources, their uses and environmental impacts.',
  'theory': [{'content': 'NON-RENEWABLE energy resources WILL RUN OUT — cannot be replenished on human timescales.\n'
                         'FOSSIL FUELS: coal, oil, natural gas — formed from ancient organic material over millions of '
                         'years.\n'
                         'NUCLEAR FUEL: uranium and plutonium — finite supply.\n'
                         '\n'
                         'RENEWABLE energy resources are REPLENISHED naturally and will not run out.\n'
                         'WIND — kinetic energy of moving air drives turbines.\n'
                         'SOLAR (SUN) — photovoltaic cells convert light → electricity; solar thermal heats water.\n'
                         'HYDROELECTRICITY — falling/flowing water drives turbines.\n'
                         'BIO-FUEL — fuels grown from plants (wood, ethanol, biodiesel) — regrow so renewable.\n'
                         'GEOTHERMAL — heat from inside the Earth → steam → turbines.\n'
                         'TIDES — tidal flow drives turbines.\n'
                         'WATER WAVES — wave energy converters.\n'
                         '\n'
                         'All renewables (except geothermal, tidal and nuclear) ultimately trace back to the Sun.',
              'heading': 'Renewable and Non-Renewable Resources'},
             {'content': 'ELECTRICITY GENERATION — most methods use TURBINES + GENERATORS:\n'
                         'Fuel (or wind/water) → turbine spins → generator produces electricity.\n'
                         'Exceptions: solar PV converts light directly to electricity (no turbine).\n'
                         '\n'
                         'HEATING:\n'
                         'Gas central heating, geothermal hot springs, solar thermal panels.\n'
                         '\n'
                         'TRANSPORT:\n'
                         'Petrol/diesel (from crude oil) currently dominant.\n'
                         'Electric vehicles (charged from grid), hydrogen fuel cells, bio-fuels.\n'
                         '\n'
                         'WHY FOSSIL FUELS STILL DOMINATE:\n'
                         'Reliable on demand — not weather-dependent.\n'
                         'High energy density — large amount of energy per kg.\n'
                         'Existing infrastructure in place.\n'
                         'But: finite supply and significant environmental impact are driving a transition.',
              'heading': 'Uses of Energy Resources'},
             {'content': 'FOSSIL FUELS:\n'
                         'CO₂ released → greenhouse effect → climate change. Major concern.\n'
                         'SO₂ (from coal/oil) → acid rain.\n'
                         'Nitrogen oxides → smog, air pollution.\n'
                         'Oil spills → marine ecosystem damage.\n'
                         '\n'
                         'NUCLEAR:\n'
                         'No CO₂ during operation — low carbon.\n'
                         'RADIOACTIVE WASTE: hazardous, must be stored safely for thousands of years.\n'
                         'Risk of major accidents (rare but severe: Chernobyl, Fukushima).\n'
                         '\n'
                         'WIND: No CO₂. Noise, visual impact, risk to birds. Intermittent.\n'
                         'SOLAR: No CO₂. Panel manufacture uses energy and materials. Intermittent.\n'
                         'HYDROELECTRIC: No CO₂. Reliable. Dam flooding destroys habitats.\n'
                         'GEOTHERMAL: Low CO₂. Limited to active volcanic regions.\n'
                         'BIO-FUEL: Roughly carbon neutral (CO₂ released = CO₂ absorbed while growing). Land use '
                         'competes with food production.\n'
                         'TIDES/WAVES: No CO₂. Disrupts marine ecosystems. Expensive to build.\n'
                         '\n'
                         'KEY TRADE-OFFS:\n'
                         'Renewables: lower environmental impact but INTERMITTENT (wind/solar) — need storage or '
                         'backup.\n'
                         'Fossil fuels: RELIABLE and on-demand but CO₂ and pollution.\n'
                         'The energy mix must balance reliability, cost and environmental impact.',
              'heading': 'Environmental Impact of Energy Resources'}],
  'title': 'Energy Resources',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "INSULATORS do not stop heat transfer — they slow it down. A perfect insulator doesn't exist. "
                    'Trapped air is one of the best insulators because air is a poor conductor and convection is '
                    'reduced when it is trapped in small spaces.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'thermal-conductivity',
  'key_note': 'Thermal conductivity: rate of energy transfer by conduction. Metals = good conductors (free electrons). '
              'Air/fibreglass = good insulators. Reducing losses: insulation, lubrication, streamlining. Thicker '
              'insulation = less energy lost. RP2: compare materials by rate of cooling.',
  'matching': {'instruction': 'Match each material to its thermal conductivity property.',
               'pairs': [('Copper', 'Very high thermal conductivity — free electrons transfer energy rapidly'),
                         ('Air (trapped)', 'Very low thermal conductivity — excellent insulator when trapped'),
                         ('Cavity wall insulation', 'Fibreglass with trapped air — reduces energy loss through walls'),
                         ('Lubrication', 'Reduces friction between surfaces — less energy wasted as heat')],
               'title': 'Thermal Conductivity'},
  'quiz': [{'opts': [('Air has much lower thermal conductivity than glass — it transfers energy by conduction very '
                      'slowly',
                      True),
                     ('Air is lighter than glass — lower density means less thermal energy stored', False),
                     ('Glass transmits light which carries thermal energy — air does not', False),
                     ('Air molecules move randomly, transferring energy away from hot objects faster', False)],
            'q': 'Why is trapped air a better insulator than glass?',
            'wrong_explanations': {1: "Density affects heat capacity but not thermal conductivity directly — air's "
                                      'insulating property comes from its very low thermal conductivity.',
                                   2: 'Light transmission (transparency) is unrelated to thermal conductivity.',
                                   3: 'Moving air molecules would increase CONVECTION — trapped air cannot convect, so '
                                      'only slow conduction occurs.'}},
           {'opts': [('Rate of temperature decrease — steeper temperature-time graph = less effective insulator', True),
                     ('Final temperature after 10 minutes — higher temperature = better conductor', False),
                     ('Mass of insulating material used — more mass = more insulation', False),
                     ('Colour of the insulating material — darker colours absorb more radiation', False)],
            'q': 'A student investigates thermal insulators by wrapping identical beakers in different materials. '
                 'Which measurement gives the best comparison?',
            'wrong_explanations': {1: "Final temperature alone doesn't account for starting conditions or time — rate "
                                      'of cooling (gradient) is a fairer comparison.',
                                   2: 'Mass is not controlled in this way — thickness and type of material matter, not '
                                      'total mass.',
                                   3: 'Colour affects radiation absorption — relevant for infrared studies but not '
                                      'primary factor in conduction-based insulation tests.'}}],
  'rp': 'RP2 (physics only) — Investigate effectiveness of different thermal insulators. Measure rate of cooling of '
        'hot water wrapped in different materials.',
  'spec': '6.1.3 (physics only)',
  'summary': 'Explain thermal conductivity and describe how insulation reduces unwanted energy transfers.',
  'theory': [{'content': 'THERMAL CONDUCTIVITY measures how well a material transfers thermal energy by conduction.\n'
                         '\n'
                         'Good THERMAL CONDUCTORS: metals (copper, aluminium, iron). Transfer energy quickly. Free '
                         'electrons carry thermal energy through the material.\n'
                         '\n'
                         'Good THERMAL INSULATORS: air, wood, fibreglass, polystyrene, wool. Transfer energy slowly. '
                         'No free electrons; energy transferred only by vibration between tightly packed or sparse '
                         'particles.\n'
                         '\n'
                         'Unit of thermal conductivity: W/m·K (watts per metre per kelvin).\n'
                         '\n'
                         'Higher thermal conductivity → energy transferred faster for the same temperature difference '
                         'and thickness.\n'
                         '\n'
                         'Examples:\n'
                         'Copper: ~400 W/m·K — excellent conductor.\n'
                         'Glass: ~1 W/m·K — poor conductor.\n'
                         'Air: ~0.025 W/m·K — excellent insulator.',
              'heading': 'Thermal Conductivity'},
             {'content': 'All energy transfers involve some unwanted dissipation — energy transferred to the thermal '
                         'store of the surroundings.\n'
                         '\n'
                         'METHODS TO REDUCE THERMAL ENERGY LOSS:\n'
                         '\n'
                         '1. INSULATION:\n'
                         'Surround objects with poor conductors.\n'
                         'Cavity wall insulation (fibreglass or foam) — reduces conduction through walls.\n'
                         'Loft insulation — reduces conduction through roof.\n'
                         'Double-glazing — air gap between panes of glass reduces conduction.\n'
                         'Foam lagging on hot water pipes — reduces heat loss to surroundings.\n'
                         '\n'
                         '2. LUBRICATION:\n'
                         'Reduces friction between moving surfaces.\n'
                         'Less friction → less thermal energy dissipated.\n'
                         'Machine oil, grease used in engines, bearings, chains.\n'
                         '\n'
                         '3. STREAMLINING:\n'
                         'Reduces air resistance on moving vehicles.\n'
                         'Less drag → less energy wasted overcoming resistance.\n'
                         '\n'
                         '4. ELECTROMAGNETIC SHIELDING:\n'
                         'Reduces energy loss from electrical components.\n'
                         '\n'
                         'THICKNESS AND THERMAL CONDUCTIVITY:\n'
                         'Thicker insulation → less energy transferred per second (for same temperature difference).\n'
                         'More insulating material (lower conductivity) → less energy transferred.\n'
                         'Energy lost per second ∝ thermal conductivity × area × (temperature difference) ÷ thickness.',
              'heading': 'Reducing Unwanted Energy Transfers'},
             {'content': 'REQUIRED PRACTICAL (RP2 — physics only):\n'
                         'Investigate the effectiveness of different materials as thermal insulators.\n'
                         '\n'
                         'METHOD:\n'
                         'Wrap beakers of hot water in different materials (wool, bubble wrap, newspaper, foil).\n'
                         'Measure temperature of water at regular time intervals.\n'
                         'Plot temperature-time graphs for each material.\n'
                         'Compare rate of cooling — steeper gradient = less effective insulator.\n'
                         '\n'
                         'VARIABLES:\n'
                         'Independent: type of insulating material.\n'
                         'Dependent: rate of cooling (temperature change per unit time).\n'
                         'Controlled: initial temperature, volume of water, thickness of insulation, surface area.\n'
                         '\n'
                         'CONCLUSION:\n'
                         'Material with lowest thermal conductivity → slowest cooling → best insulator.\n'
                         'Air is often the best insulator — sealed air pockets in fibreglass work well.\n'
                         '\n'
                         'APPLICATIONS:\n'
                         'Building insulation — reduces heating bills and carbon footprint.\n'
                         'Refrigeration — insulated walls slow thermal energy entering the cold space.\n'
                         'Cryogenics — extreme insulation to maintain very low temperatures.',
              'heading': 'Required Practical — Thermal Insulation'}],
  'title': 'Thermal Conductivity and Reducing Unwanted Energy Transfers',
  'triple_only': 'Thermal conductivity and insulation (physics only) — not in Combined Science.',
  'variables': []}],

"electricity": [{'common_mistake': 'Ammeters are connected IN SERIES — they must be in the same loop as the component. Voltmeters are '
                    'connected IN PARALLEL — they bridge across the component. Swapping these will give wrong readings '
                    '(and could damage the meter). Always draw with a ruler — freehand diagrams lose marks.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'circuit-symbols',
  'key_note': 'Standard symbols allow universal reading of circuits. Key symbols: cell, battery, bulb, motor, switch, '
              'ammeter (series), voltmeter (parallel), fixed/variable resistor, thermistor, LDR, diode, LED, fuse. '
              'Ammeter in series. Voltmeter in parallel.',
  'matching': {'instruction': 'Match each circuit symbol description to the component it represents.',
               'pairs': [('Cell', 'One long line (positive) and one shorter line (negative)'),
                         ('Ammeter', 'Circle with A inside — connected in series to measure current'),
                         ('Voltmeter', 'Circle with V inside — connected in parallel to measure potential difference'),
                         ('LDR', 'Resistor symbol with two arrows pointing inward — resistance decreases in light'),
                         ('Diode', 'Triangle pointing to a vertical line — allows current in one direction only')],
               'title': 'Symbol to Component'},
  'quiz': [{'opts': [('In series with the bulb — in the same loop so the same current flows through both', True),
                     ('In parallel with the bulb — bridging across it so it measures the voltage', False),
                     ('Anywhere in the circuit — ammeters measure the total current of the whole circuit', False),
                     ('Between the two terminals of the battery — to measure the source current', False)],
            'q': 'How should an ammeter be connected to measure the current through a bulb?',
            'wrong_explanations': {1: 'In parallel is how you connect a VOLTMETER, not an ammeter. An ammeter in '
                                      'parallel would short-circuit the component.',
                                   2: 'An ammeter must be in series specifically with the component being measured — '
                                      'position matters in branched circuits.',
                                   3: 'Placing an ammeter directly across the battery terminals would short-circuit '
                                      'the battery — dangerous and incorrect.'}},
           {'opts': [('A lamp (bulb) — the cross represents the filament inside the glass envelope', True),
                     ('A motor — the cross indicates rotation', False),
                     ('A fuse — the cross means it can break the circuit', False),
                     ('An LED — the cross represents light emission', False)],
            'q': 'What does the symbol of a circle with a cross inside represent?',
            'wrong_explanations': {1: 'A motor symbol is a circle with M inside — not a cross.',
                                   2: 'A fuse symbol is a rectangle with a line through it — not a circle with a '
                                      'cross.',
                                   3: 'An LED symbol is a diode (triangle + line) with two outward arrows — not a '
                                      'circle with a cross.'}}],
  'rp': 'RP15 (Physics) — Use circuit diagrams to set up and investigate circuits. RP16 — Construct circuits to '
        'investigate I–V characteristics.',
  'spec': '6.2.1.1',
  'summary': 'Draw and interpret circuit diagrams using standard symbols.',
  'theory': [{'content': 'Circuit diagrams use STANDARD SYMBOLS so that any engineer or scientist worldwide can read '
                         'and build the same circuit — regardless of language.\n'
                         '\n'
                         'A circuit diagram shows how components are connected using straight lines (wires) and '
                         'standardised symbols. It is a schematic, not a picture of the physical layout.\n'
                         '\n'
                         'Rules for drawing circuit diagrams:\n'
                         'Use a RULER — all lines must be straight.\n'
                         'Components are placed on the lines, not at corners.\n'
                         'Circuit should be drawn as a CLOSED LOOP.\n'
                         'Wires are shown as straight horizontal and vertical lines.',
              'heading': 'Why Standard Symbols?'},
             {'content': 'You must be able to draw and recognise all of these:\n'
                         '\n'
                         'POWER SUPPLIES:\n'
                         'Cell — one long line (positive) + one short line (negative)\n'
                         'Battery — two or more cells in series\n'
                         'AC supply — circle with a sine wave\n'
                         '\n'
                         'CONTROL:\n'
                         'Switch (open) — a line with a gap and a lever\n'
                         'Switch (closed) — lever touches the contact\n'
                         '\n'
                         'OUTPUT COMPONENTS:\n'
                         'Bulb/lamp — circle with a cross inside\n'
                         'Motor — circle with M inside\n'
                         'Buzzer — circle with rectangle inside\n'
                         '\n'
                         'MEASUREMENT:\n'
                         'Ammeter — circle with A (connected in SERIES)\n'
                         'Voltmeter — circle with V (connected in PARALLEL)\n'
                         '\n'
                         'RESISTANCE:\n'
                         'Fixed resistor — rectangle\n'
                         'Variable resistor (rheostat) — rectangle with an arrow through it\n'
                         'Thermistor — resistor symbol with a diagonal line through\n'
                         'LDR (light-dependent resistor) — resistor symbol with arrows pointing in\n'
                         '\n'
                         'OTHER:\n'
                         'Diode — triangle pointing to a line (current flows in direction of triangle)\n'
                         'LED — diode symbol with two arrows pointing out\n'
                         'Fuse — rectangle with a line through it',
              'heading': 'Essential Component Symbols'},
             {'content': 'To INTERPRET a circuit diagram:\n'
                         '1. Trace the path from the positive terminal of the battery.\n'
                         '2. Identify all components along each branch.\n'
                         '3. Note which components are in series (same path) and which are in parallel (different '
                         'branches).\n'
                         '\n'
                         'To DRAW a circuit diagram:\n'
                         '1. Sketch the battery and switch first.\n'
                         '2. Add components in the correct positions.\n'
                         '3. Connect everything with straight ruled lines.\n'
                         '4. Add meters: ammeter in series with the component; voltmeter in parallel across it.\n'
                         '\n'
                         'COMMON EXAM TASK:\n'
                         'Given a description of a circuit, draw it accurately with all components in the correct '
                         'positions and symbols drawn correctly.',
              'heading': 'Reading and Drawing Circuit Diagrams'}],
  'title': 'Standard Circuit Diagram Symbols',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Time must be in SECONDS when using Q = It. If given minutes, multiply by 60 first. In a series '
                    "circuit, current is the SAME at every point — it does not get 'used up' passing through "
                    'components.',
  'equations': ['Q = I × t'],
  'fifas': [{'label': 'Charge Calculation',
             'question': 'A current of 0.4 A flows through a lamp for 5 minutes. Calculate the charge that flows.',
             'steps': [('F', 'Q = I × t'),
                       ('I', 'I = 0.4 A, t = 5 × 60 = 300 s'),
                       ('F', 'Q = 0.4 × 300'),
                       ('A', 'Q = 120 C')]}],
  'higher': None,
  'id': 'electrical-charge-current',
  'key_note': 'Current = rate of flow of charge. Q = It. Unit: ampere (A). Series: same current everywhere. Parallel: '
              'current splits — I_total = sum of branches. Charge carriers in metals = electrons. Conventional '
              'current: + to −. Electron flow: − to +.',
  'matching': {'instruction': 'Match each scenario to the correct value.',
               'pairs': [('60 C', 'Current = 3 A, time = 20 s — Q = 3 × 20'),
                         ('0.5 A', 'Charge = 90 C, time = 3 minutes — I = 90 ÷ 180'),
                         ('Same everywhere', 'Current at each point in a series circuit'),
                         ('Splits at junctions', 'Current behaviour in a parallel circuit')],
               'title': 'Charge and Current'},
  'quiz': [{'opts': [('1.5 A — I = Q ÷ t = 180 ÷ 120 = 1.5 A (t = 2 × 60 = 120 s)', True),
                     ('90 A — I = 180 ÷ 2 (used minutes not seconds)', False),
                     ('360 A — I = 180 × 2 (multiplied instead of divided)', False),
                     ('0.013 A — I = 180 ÷ 14400 (used hours)', False)],
            'q': 'A charge of 180 C flows through a resistor in 2 minutes. What is the current?',
            'wrong_explanations': {1: '2 minutes = 120 seconds. I = 180 ÷ 2 = 90 A — used minutes, not seconds.',
                                   2: 'I = Q ÷ t, not Q × t. Must divide.',
                                   3: '2 minutes = 120 s (not 14400). I = 180 ÷ 120 = 1.5 A.'}},
           {'opts': [('0.3 A — current is identical at every point in a series circuit', True),
                     ('Less than 0.3 A — the first lamp has used some of the current', False),
                     ('More than 0.3 A — the second lamp draws extra current', False),
                     ('Depends on the resistance of each lamp', False)],
            'q': 'In a series circuit, an ammeter before the first lamp reads 0.3 A. What does an ammeter between the '
                 'two lamps read?',
            'wrong_explanations': {1: "Current is NOT 'used up' — energy is transferred but the charges continue "
                                      'flowing. Current is identical throughout a series circuit.',
                                   2: 'Current cannot increase through a series circuit without a junction.',
                                   3: 'In a series circuit, current is always the same at all points regardless of '
                                      'individual resistances.'}}],
  'rp': 'RP15 (Physics) — Set up series and parallel circuits; measure current with ammeters at different positions to '
        'verify series current is constant and parallel currents sum to total.',
  'spec': '6.2.1.2',
  'summary': 'Describe electric current as flow of charge and calculate charge, current and time.',
  'theory': [{'content': 'ELECTRIC CURRENT is a flow of electrical charge.\n'
                         '\n'
                         'For current to flow, two conditions must be met:\n'
                         '1. There must be a CLOSED CIRCUIT — a complete, unbroken conducting path.\n'
                         '2. There must be a SOURCE OF POTENTIAL DIFFERENCE (a battery or power supply) to drive the '
                         'charge.\n'
                         '\n'
                         'Current is measured in AMPERES (A).\n'
                         '1 ampere = 1 coulomb of charge passing a point per second.\n'
                         '\n'
                         'In metal conductors, the charge carriers are FREE ELECTRONS.\n'
                         'In solutions (electrolytes), the charge carriers are IONS.\n'
                         '\n'
                         'CONVENTIONAL CURRENT flows from + to − around the external circuit.\n'
                         'ELECTRON FLOW is actually from − to + (electrons repelled from the negative terminal).\n'
                         'Conventional current direction was defined before electrons were discovered.',
              'heading': 'Electric Current — Flow of Charge'},
             {'content': 'Q = I × t\n'
                         '\n'
                         'Q = charge flow (coulombs, C)\n'
                         'I = current (amperes, A)\n'
                         't = time (seconds, s)\n'
                         '\n'
                         'Rearranging:\n'
                         'I = Q ÷ t\n'
                         't = Q ÷ I\n'
                         '\n'
                         'EXAMPLE 1:\n'
                         'A current of 2 A flows for 30 s:\n'
                         'Q = 2 × 30 = 60 C\n'
                         '\n'
                         'EXAMPLE 2:\n'
                         '120 C flows in 4 minutes:\n'
                         't = 4 × 60 = 240 s\n'
                         'I = 120 ÷ 240 = 0.5 A\n'
                         '\n'
                         'One coulomb ≈ 6.24 × 10¹⁸ electrons.',
              'heading': 'Charge, Current and Time'},
             {'content': 'SERIES circuit:\n'
                         'Current is the SAME everywhere — only one path for charge.\n'
                         'I₁ = I₂ = I₃\n'
                         '\n'
                         'PARALLEL circuit:\n'
                         'Current SPLITS at junctions — more paths available.\n'
                         'I_total = I₁ + I₂ + I₃\n'
                         'Branches with lower resistance carry more current.\n'
                         '\n'
                         'MEASURING CURRENT:\n'
                         'Use an AMMETER connected in SERIES.\n'
                         'Ammeters have very LOW resistance — do not significantly affect the circuit.',
              'heading': 'Current in Series and Parallel Circuits'}],
  'title': 'Electrical Charge and Current',
  'triple_only': None,
  'variables': [('Q', 'Charge', 'coulombs', 'C'), ('I', 'Current', 'amperes', 'A'), ('t', 'Time', 'seconds', 's')]},
 {'common_mistake': 'R = V ÷ I, NOT V × I. Use the triangle: cover the unknown — the remaining two show the operation. '
                    "'Voltage' is acceptable in everyday speech but the precise term is POTENTIAL DIFFERENCE.",
  'equations': ['V = I × R'],
  'fifas': [{'label': 'Resistance Calculation',
             'question': 'A component has 12 V across it and 0.4 A through it. Calculate its resistance.',
             'steps': [('F', 'R = V ÷ I'), ('I', 'V = 12 V, I = 0.4 A'), ('F', 'R = 12 ÷ 0.4'), ('A', 'R = 30 Ω')]}],
  'higher': None,
  'id': 'current-resistance-pd',
  'key_note': 'V = IR. I = V/R. R = V/I. Ohmic: I ∝ V, straight I–V line. Series: pd splits (sum = total). Parallel: '
              'same pd across each branch. Ammeter in series; voltmeter in parallel.',
  'matching': {'instruction': 'Match each circuit scenario to the correct calculated value.',
               'pairs': [('R = 6 Ω', 'V = 12 V, I = 2 A — R = 12 ÷ 2'),
                         ('I = 0.5 A', 'V = 3 V, R = 6 Ω — I = 3 ÷ 6'),
                         ('V = 9 V', 'I = 3 A, R = 3 Ω — V = 3 × 3'),
                         ('I doubles', 'Pd doubles for an ohmic conductor — current proportional to pd')],
               'title': 'V = IR Calculations'},
  'quiz': [{'opts': [('18 V — V = I × R = 3 × 6 = 18 V', True),
                     ('2 V — V = R ÷ I = 6 ÷ 3 = 2 V', False),
                     ('0.5 V — V = I ÷ R = 3 ÷ 6', False),
                     ('9 V — V = (I + R) / 2', False)],
            'q': 'A 6 Ω resistor has 3 A through it. What is the potential difference?',
            'wrong_explanations': {1: 'R ÷ I gives Ω/A — not volts. V = I × R = 3 × 6 = 18 V.',
                                   2: 'I ÷ R gives A/Ω — not volts. The equation is V = I × R.',
                                   3: "There is no averaging formula in Ohm's Law."}},
           {'opts': [('Lower resistance — more current per volt (I = V/R, larger I means smaller R)', True),
                     ('Higher resistance — steeper means more opposition', False),
                     ('Higher pd — the axes are swapped', False),
                     ('Non-ohmic behaviour — only curved graphs are ohmic', False)],
            'q': 'On an I–V graph for an ohmic conductor, what does a steeper gradient indicate?',
            'wrong_explanations': {1: 'Steeper I–V gradient means MORE current for same pd → LOWER resistance. High '
                                      'resistance = shallower gradient.',
                                   2: 'On a standard I–V graph (I on y-axis, V on x-axis), steeper = more current per '
                                      'volt = lower R.',
                                   3: 'Ohmic conductors produce straight-line I–V graphs — steepness indicates the R '
                                      'value.'}}],
  'rp': 'RP15 (Physics) — Measure V and I for different components; calculate resistance using R = V/I.',
  'spec': '6.2.1.3',
  'summary': "Apply Ohm's Law (V = IR) to calculate current, resistance and potential difference.",
  'theory': [{'content': 'POTENTIAL DIFFERENCE (pd) — also called voltage — is the energy transferred per unit '
                         'charge.\n'
                         'Unit: VOLT (V). 1 V = 1 joule per coulomb.\n'
                         '\n'
                         'RESISTANCE is the opposition to the flow of current.\n'
                         'Unit: OHM (Ω).\n'
                         '\n'
                         "OHM'S LAW:\n"
                         'V = I × R\n'
                         '\n'
                         'V = potential difference (V)\n'
                         'I = current (A)\n'
                         'R = resistance (Ω)\n'
                         '\n'
                         'Rearranging:\n'
                         'I = V ÷ R\n'
                         'R = V ÷ I\n'
                         '\n'
                         'Higher resistance → lower current for a given pd.\n'
                         'Higher pd → higher current for a given resistance.',
              'heading': 'Potential Difference and Resistance'},
             {'content': 'An OHMIC CONDUCTOR (e.g. a resistor at constant temperature):\n'
                         'Current is DIRECTLY PROPORTIONAL to pd.\n'
                         'Resistance stays CONSTANT as current changes.\n'
                         '\n'
                         'On an I–V graph:\n'
                         'Straight line through the origin.\n'
                         'Steeper gradient = lower resistance (more current per volt).\n'
                         '\n'
                         'MEASURING RESISTANCE:\n'
                         'Ammeter in series + voltmeter in parallel.\n'
                         'R = V ÷ I\n'
                         '\n'
                         'EXAMPLE:\n'
                         '6 V across a resistor, 2 A through it:\n'
                         'R = 6 ÷ 2 = 3 Ω',
              'heading': 'Ohmic Conductors and I–V Graphs'},
             {'content': 'SERIES — pd SPLITS between components:\n'
                         'V_total = V₁ + V₂ + V₃\n'
                         'Higher resistance → larger share of pd.\n'
                         '\n'
                         'PARALLEL — pd is the SAME across all branches:\n'
                         'V₁ = V₂ = V₃ = V_supply\n'
                         '\n'
                         'EXAMPLE — series circuit:\n'
                         'Battery = 12 V. R₁ = 4 Ω, R₂ = 8 Ω.\n'
                         'Total R = 12 Ω. I = 12 ÷ 12 = 1 A.\n'
                         'V₁ = 1 × 4 = 4 V. V₂ = 1 × 8 = 8 V. Check: 4 + 8 = 12 V ✓',
              'heading': 'Potential Difference in Circuits'}],
  'title': 'Current, Resistance and Potential Difference',
  'triple_only': None,
  'variables': [('V', 'Potential difference', 'volts', 'V'),
                ('I', 'Current', 'amperes', 'A'),
                ('R', 'Resistance', 'ohms', 'Ω')]},
 {'common_mistake': 'Thermistor resistance DECREASES with higher temperature (NTC). LDR resistance DECREASES with more '
                    'light. Both are the OPPOSITE of what students often assume. A filament lamp is NOT ohmic — its '
                    'resistance increases as it heats up.',
  'equations': ['R = V ÷ I'],
  'fifas': [],
  'higher': None,
  'id': 'resistors',
  'key_note': 'Ohmic resistor: constant R, straight I–V. Filament lamp: R increases with temperature, curved I–V. '
              'Diode: one direction only. Thermistor (NTC): R decreases with temperature. LDR: R decreases with light. '
              'RP16: investigate I–V graphs for resistor, lamp, diode.',
  'matching': {'instruction': 'Match each component to how its resistance changes.',
               'pairs': [('Ohmic resistor', 'Resistance stays constant — straight I–V line through origin'),
                         ('Filament lamp', 'Resistance increases as it heats up — curved I–V graph'),
                         ('Diode', 'Very low resistance in forward direction only — blocks reverse current'),
                         ('Thermistor (NTC)', 'Resistance decreases as temperature increases'),
                         ('LDR', 'Resistance decreases as light intensity increases')],
               'title': 'Component Behaviour'},
  'quiz': [{'opts': [('Resistance decreases, current increases — NTC thermistors have lower resistance at higher '
                      'temperatures',
                      True),
                     ('Resistance increases, current decreases — hotter means more resistance like a metal wire',
                      False),
                     ('Resistance stays the same — thermistors are ohmic', False),
                     ('Current stays constant — current is set by the battery', False)],
            'q': "When temperature rises, what happens to a thermistor's resistance and the current through it?",
            'wrong_explanations': {1: 'Metal wires do increase resistance with temperature, but thermistors are NTC — '
                                      'opposite behaviour.',
                                   2: 'Thermistors are NOT ohmic — resistance changes significantly with temperature.',
                                   3: 'I = V/R — if R changes, I changes too (assuming constant pd).'}},
           {'opts': [('Current increases — LDR resistance falls in light, total circuit resistance falls, current '
                      'rises',
                      True),
                     ('Current decreases — more light makes the LDR resist more', False),
                     ('Current stays the same — the fixed resistor controls the current', False),
                     ('Current becomes zero — LDR blocks current in light', False)],
            'q': 'An LDR is in series with a fixed resistor and battery. A light is switched on. What happens to the '
                 'current?',
            'wrong_explanations': {1: 'LDR resistance DECREASES in light. Lower total resistance → I = V/R gives '
                                      'higher current.',
                                   2: 'Fixed resistor limits the minimum resistance but total R still falls when LDR R '
                                      'falls.',
                                   3: 'LDRs are not diodes — they conduct in both directions, just with different '
                                      'resistance values.'}}],
  'rp': 'RP16 (Physics) — Construct circuits to investigate I–V characteristics of a filament lamp, diode and '
        'resistor. Plot graphs and interpret each.',
  'spec': '6.2.1.4',
  'summary': 'Describe I–V characteristics of resistors, lamps, diodes, thermistors and LDRs.',
  'theory': [{'content': 'OHMIC CONDUCTOR — constant resistance; I–V graph is a straight line through the origin.\n'
                         '\n'
                         'FILAMENT LAMP:\n'
                         'As current increases → lamp heats up → resistance INCREASES.\n'
                         'I–V graph: curve that gets shallower at higher pd.\n'
                         'Not ohmic — resistance changes with temperature.\n'
                         '\n'
                         'DIODE:\n'
                         'Allows current in ONE DIRECTION only.\n'
                         'Very high resistance in reverse.\n'
                         'I–V graph: flat near zero in reverse; steep rise forward (above ~0.6 V threshold).\n'
                         'Used in rectifiers to convert AC to DC.\n'
                         '\n'
                         'LED (LIGHT-EMITTING DIODE):\n'
                         'Works like a diode but emits light when forward biased.\n'
                         'Very efficient — widely used for lighting and indicators.',
              'heading': 'Ohmic and Non-Ohmic Components'},
             {'content': 'THERMISTOR (NTC — negative temperature coefficient):\n'
                         'Resistance DECREASES as temperature INCREASES.\n'
                         'Hotter → more charge carriers → lower resistance → more current.\n'
                         '\n'
                         'Applications: thermostats, temperature sensors, fire alarms, ovens.\n'
                         '\n'
                         'LDR (LIGHT-DEPENDENT RESISTOR):\n'
                         'Resistance DECREASES as light intensity INCREASES.\n'
                         'Bright light → more charge carriers available → lower resistance.\n'
                         'In darkness → very high resistance.\n'
                         '\n'
                         'Applications: automatic street lights (switch on when dark), security lights, camera '
                         'exposure meters.\n'
                         '\n'
                         'EXAMPLE: Street light circuit — dark → LDR resistance high → voltage across LDR high → '
                         'triggers switch → light activates.',
              'heading': 'Thermistors and LDRs'},
             {'content': 'REQUIRED PRACTICAL (RP16) — Investigate I–V characteristics of:\n'
                         '1. A resistor at constant temperature (ohmic — straight line)\n'
                         '2. A filament lamp (non-ohmic — curve, resistance rises)\n'
                         '3. A diode (allows one direction — flat then steep)\n'
                         '\n'
                         'METHOD:\n'
                         'Variable resistor changes pd across component.\n'
                         'Ammeter (series) and voltmeter (parallel) measure I and V.\n'
                         'Reverse connections to obtain negative values.\n'
                         'Plot I–V graph for each.\n'
                         '\n'
                         'SAFETY: Keep current low to avoid overheating. Use a protective resistor in series with the '
                         'diode.',
              'heading': 'I–V Characteristics and Required Practical'}],
  'title': 'Resistors',
  'triple_only': None,
  'variables': [('R', 'Resistance', 'ohms', 'Ω'),
                ('I', 'Current', 'amperes', 'A'),
                ('V', 'Potential difference', 'volts', 'V')]},
 {'common_mistake': 'In PARALLEL, total resistance is LESS than any individual resistance — more branches = more paths '
                    '= lower resistance. Adding resistors in SERIES always increases total resistance. Students often '
                    'mix these up.',
  'equations': ['Series: R_total = R₁ + R₂ + R₃', 'Series: V_total = V₁ + V₂ + V₃', 'Parallel: I_total = I₁ + I₂ + I₃'],
  'fifas': [{'label': 'Series Circuit',
             'question': 'R₁ = 3 Ω and R₂ = 7 Ω in series with a 20 V battery. Find the current and pd across each '
                         'resistor.',
             'steps': [('F', 'R_total = R₁ + R₂; I = V ÷ R_total; V₁ = I × R₁; V₂ = I × R₂'),
                       ('I', 'R_total = 3 + 7 = 10 Ω; V = 20 V'),
                       ('F', 'I = 20 ÷ 10 = 2 A; V₁ = 2 × 3 = 6 V; V₂ = 2 × 7 = 14 V'),
                       ('A', 'I = 2 A throughout; V₁ = 6 V; V₂ = 14 V (check: 6 + 14 = 20 V ✓)')]}],
  'higher': None,
  'id': 'series-parallel-circuits',
  'key_note': 'Series: same I, pd splits, R adds. Parallel: same pd, I splits, total R less than smallest. Household = '
              'parallel — full voltage, independent. Series break = all stop. Parallel break = others continue.',
  'matching': {'instruction': 'Match each property to the correct circuit type.',
               'pairs': [('Series', 'Current is identical at every point in the loop'),
                         ('Parallel', 'Potential difference is the same across every branch'),
                         ('Series', 'Total resistance equals the sum of individual resistances'),
                         ('Parallel', 'If one component breaks, the others continue working'),
                         ('Both', 'The battery provides the total pd for the whole circuit')],
               'title': 'Series vs Parallel'},
  'quiz': [{'opts': [('6 V each — every branch in a parallel circuit has the same pd as the supply', True),
                     ('3 V each — the pd splits equally between the two parallel lamps', False),
                     ('12 V each — parallel doubles the voltage per branch', False),
                     ('Depends on lamp resistance — cannot determine without values', False)],
            'q': 'Two lamps are connected in parallel across a 6 V battery. What is the pd across each lamp?',
            'wrong_explanations': {1: 'Pd splitting happens in SERIES. In PARALLEL, all branches have the SAME pd as '
                                      'the supply.',
                                   2: 'Parallel circuits never increase voltage beyond the supply.',
                                   3: 'In parallel, all branches have the supply pd regardless of resistance — only '
                                      'the branch CURRENT changes with resistance.'}},
           {'opts': [("Each appliance gets full mains voltage and works independently — switching one off doesn't "
                      'affect others',
                      True),
                     ('Parallel uses less total current so it is safer', False),
                     ('Series cannot carry enough current for multiple appliances', False),
                     ('Parallel wiring is cheaper to install', False)],
            'q': 'Why is household wiring parallel rather than series?',
            'wrong_explanations': {1: 'Parallel draws MORE total current (I_total = sum of branches) — safety comes '
                                      'from fuses, not lower current.',
                                   2: 'Series wiring would mean each appliance gets a reduced share of 230 V and all '
                                      'would stop if one broke.',
                                   3: 'Cost is a secondary concern — the electrical reasons (full voltage, independent '
                                      'operation) are the key ones.'}}],
  'rp': 'RP15 (Physics) — Construct series and parallel circuits; measure I and V at different points to verify rules.',
  'spec': '6.2.2',
  'summary': 'Calculate current, potential difference and resistance in series and parallel circuits.',
  'theory': [{'content': 'In a SERIES circuit, all components are in a SINGLE LOOP — one path for current.\n'
                         '\n'
                         'Rules:\n'
                         'CURRENT: same through every component — I₁ = I₂ = I₃\n'
                         'PD: splits between components — V_total = V₁ + V₂ + V₃\n'
                         'RESISTANCE: adds up — R_total = R₁ + R₂ + R₃\n'
                         '\n'
                         'EXAMPLE:\n'
                         'R₁ = 4 Ω, R₂ = 6 Ω, battery = 10 V.\n'
                         'R_total = 10 Ω. I = 10 ÷ 10 = 1 A.\n'
                         'V₁ = 1 × 4 = 4 V; V₂ = 1 × 6 = 6 V. Check: 4 + 6 = 10 V ✓\n'
                         '\n'
                         'If one component breaks — ALL components stop working.',
              'heading': 'Series Circuits'},
             {'content': 'In a PARALLEL circuit, components are in SEPARATE BRANCHES — multiple paths for current.\n'
                         '\n'
                         'Rules:\n'
                         'PD: same across every branch — V₁ = V₂ = V₃ = V_supply\n'
                         'CURRENT: splits — I_total = I₁ + I₂ + I₃\n'
                         'RESISTANCE: total is LESS than the smallest individual resistance.\n'
                         '\n'
                         'EXAMPLE:\n'
                         '12 V supply. R₁ = 6 Ω, R₂ = 4 Ω.\n'
                         'I₁ = 12 ÷ 6 = 2 A; I₂ = 12 ÷ 4 = 3 A.\n'
                         'I_total = 2 + 3 = 5 A.\n'
                         '\n'
                         'If one branch breaks — OTHER branches continue working.',
              'heading': 'Parallel Circuits'},
             {'content': 'Domestic wiring is PARALLEL because:\n'
                         '1. Each appliance gets the FULL mains pd (230 V).\n'
                         "2. Appliances work INDEPENDENTLY — switching one off doesn't affect others.\n"
                         '3. Easy to add appliances without affecting existing ones.\n'
                         '4. Each appliance can have its own fuse.\n'
                         '\n'
                         'SECOMPARISON:\n'
                         'Series: same current, pd splits, R adds, all-or-nothing.\n'
                         'Parallel: same pd, current splits, R decreases, independent operation.',
              'heading': 'Why Household Circuits Are Parallel'}],
  'title': 'Series and Parallel Circuits',
  'triple_only': None,
  'variables': [('I', 'Current', 'amperes', 'A'),
                ('V', 'Potential difference', 'volts', 'V'),
                ('R', 'Resistance', 'ohms', 'Ω')]},
 {'common_mistake': 'UK mains is 50 Hz — not 60 Hz (USA). The quoted 230 V is an rms value — the peak voltage is '
                    'higher (~325 V). A DC trace is a flat line; an AC trace is a wave.',
  'equations': ['f = 1 ÷ T'],
  'fifas': [{'label': 'Frequency from Period',
             'question': 'An oscilloscope trace shows one complete cycle takes 0.02 s. Calculate the frequency.',
             'steps': [('F', 'f = 1 ÷ T'),
                       ('I', 'T = 0.02 s'),
                       ('F', 'f = 1 ÷ 0.02'),
                       ('A', 'f = 50 Hz — UK mains frequency ✓')]}],
  'higher': None,
  'id': 'direct-alternating-pd',
  'key_note': 'DC: constant direction, flat oscilloscope line. AC: reversing, sinusoidal trace. UK mains: 50 Hz, ~230 '
              'V rms. f = 1/T. Mains AC because generators produce AC and it can be transformed easily.',
  'matching': {'instruction': 'Match each description to DC or AC.',
               'pairs': [('DC', 'Flows in one direction only — flat horizontal oscilloscope trace'),
                         ('AC', 'Reverses direction repeatedly — sinusoidal oscilloscope trace'),
                         ('DC', 'Produced by batteries and solar cells'),
                         ('AC', 'UK mains — 230 V, 50 Hz'),
                         ('AC', 'Produced by generators in power stations')],
               'title': 'DC vs AC'},
  'quiz': [{'opts': [('A DC supply — constant pd in one direction', True),
                     ('An AC supply — the line shows the average value of the alternating current', False),
                     ('No current — horizontal means the circuit is off', False),
                     ('Very high frequency AC — oscillations too fast to see', False)],
            'q': 'An oscilloscope shows a horizontal line above the zero axis. What does this represent?',
            'wrong_explanations': {1: 'An AC trace is sinusoidal. A flat line means CONSTANT pd — that is DC. A line '
                                      'at zero means no pd; above zero means a positive DC voltage.',
                                   2: 'A horizontal line above zero means a CONSTANT positive pd — DC, not AC.',
                                   3: 'Very fast AC would appear blurred or as a thick band — a sharp flat line '
                                      'specifically indicates DC.'}},
           {'opts': [('50 Hz and 230 V', True),
                     ('60 Hz and 230 V — 60 Hz is the UK standard', False),
                     ('50 Hz and 110 V — 110 V is the UK mains voltage', False),
                     ('50 Hz and 325 V — 325 V is the correct value', False)],
            'q': 'What are the frequency and voltage of the UK mains supply?',
            'wrong_explanations': {1: '60 Hz is used in the USA — UK is 50 Hz.',
                                   2: '110 V is used in the USA — UK mains is ~230 V.',
                                   3: '325 V is the PEAK voltage — 230 V is the quoted rms (effective) value.'}}],
  'rp': None,
  'spec': '6.2.3.1',
  'summary': 'Distinguish dc and ac, state UK mains values and read oscilloscope traces.',
  'theory': [{'content': 'DIRECT CURRENT (DC) — flows in ONE direction only; pd is constant.\n'
                         '\n'
                         'Sources: batteries, solar cells, dc power supplies.\n'
                         '\n'
                         'On an oscilloscope:\n'
                         'DC appears as a HORIZONTAL LINE — constant pd, no oscillation.\n'
                         'Higher line = higher pd. Line at zero = no pd.',
              'heading': 'Direct Current (DC)'},
             {'content': 'ALTERNATING CURRENT (AC) — current and pd REVERSE DIRECTION repeatedly.\n'
                         '\n'
                         'Sources: mains electricity, generators.\n'
                         '\n'
                         'On an oscilloscope:\n'
                         'AC appears as a WAVE (sinusoidal) — rises above and below zero.\n'
                         'FREQUENCY = complete cycles per second (Hz).\n'
                         'PEAK VOLTAGE = maximum pd from zero.\n'
                         '\n'
                         'UK MAINS:\n'
                         'Frequency: 50 Hz\n'
                         'Voltage: ~230 V (rms value)\n'
                         '\n'
                         'Mains is AC because generators naturally produce AC, and AC is easily transformed to '
                         'different voltages for efficient transmission.',
              'heading': 'Alternating Current (AC)'},
             {'content': 'Y-axis: voltage. X-axis: time.\n'
                         '\n'
                         'FREQUENCY:\n'
                         'Measure the time for ONE complete cycle (period T).\n'
                         'f = 1 ÷ T\n'
                         '\n'
                         'PEAK VOLTAGE:\n'
                         'Measure from zero line to peak.\n'
                         'Peak pd = divisions × volts per division setting.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Period T = 0.02 s:\n'
                         'f = 1 ÷ 0.02 = 50 Hz — UK mains ✓\n'
                         '\n'
                         'DC trace: flat horizontal line.\n'
                         'AC trace: regular sinusoidal wave.',
              'heading': 'Reading Oscilloscope Traces'}],
  'title': 'Direct and Alternating Potential Difference',
  'triple_only': None,
  'variables': [('f', 'Frequency', 'hertz', 'Hz'),
                ('T', 'Period', 'seconds', 's'),
                ('V', 'Potential difference', 'volts', 'V')]},
 {'common_mistake': 'Earth wire normally carries NO current — only activates in a fault. Neutral wire (blue) IS at ~0 '
                    'V but CAN carry current. Fuses and switches must be in the LIVE wire so the appliance is fully '
                    'isolated when switched off.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'mains-electricity',
  'key_note': 'Live = brown (~230 V). Neutral = blue (0 V). Earth = green/yellow (safety, no normal current). Fuse in '
              'live wire — just above operating current. Earth wire diverts fault current → blows fuse → safe. Double '
              'insulation = no earth needed. Switches in live wire only.',
  'matching': {'instruction': 'Match each wire to its colour, voltage and role.',
               'pairs': [('Live wire', 'Brown — carries ~230 V alternating pd from the supply'),
                         ('Neutral wire', 'Blue — at 0 V, completes the circuit back to the supply'),
                         ('Earth wire', 'Green and yellow — safety wire, normally carries no current'),
                         ('Fuse', 'In the live wire — melts if current exceeds safe value')],
               'title': 'Three-Core Cable Wires'},
  'quiz': [{'opts': [('If in the neutral wire, the appliance remains at 230 V even when the fuse blows — still '
                      'dangerous',
                      True),
                     ('The neutral wire has too much resistance for a fuse to work', False),
                     ('Fuses only work with DC — neutral carries AC', False),
                     ('The neutral wire is at 230 V — it would blow constantly', False)],
            'q': 'Why must a fuse be in the live wire, not the neutral wire?',
            'wrong_explanations': {1: 'Neutral wire resistance is very low — fuses work electrically in either wire. '
                                      'The reason is SAFETY ISOLATION.',
                                   2: 'Both wires carry AC — fuses work with AC. The reason is about isolating the '
                                      'appliance from the dangerous 230 V.',
                                   3: 'Neutral is at ~0 V, not 230 V. Live is the dangerous wire at high pd.'}},
           {'opts': [('Large current flows through earth wire, fuse blows, circuit breaks — case is made safe', True),
                     ('Current stays in the case — metal is a poor conductor', False),
                     ('Earth wire permanently absorbs the fault current', False),
                     ('Nothing — earth wire only activates in thunderstorms', False)],
            'q': 'A metal-cased appliance develops a fault — live touches the case. What happens if it is properly '
                 'earthed?',
            'wrong_explanations': {1: 'Metal is an excellent conductor — current flows easily through it.',
                                   2: 'Earth wire provides a low-resistance path. The resulting surge blows the fuse. '
                                      'Earth does not permanently carry current.',
                                   3: 'Earth wire activates whenever live connects to earth (e.g. through the metal '
                                      'case) — not only in storms.'}}],
  'rp': None,
  'spec': '6.2.3.2',
  'summary': 'Describe three-core cable colour coding, the earth wire, fuses and electrical safety.',
  'theory': [{'content': 'Domestic appliances use THREE-CORE CABLE with three wires:\n'
                         '\n'
                         '1. LIVE WIRE — brown insulation\n'
                         'Carries the alternating pd (~230 V relative to earth).\n'
                         'DANGEROUS — carries current at high pd.\n'
                         '\n'
                         '2. NEUTRAL WIRE — blue insulation\n'
                         'Completes the circuit. Normally at 0 V.\n'
                         'Can still carry current — still potentially dangerous.\n'
                         '\n'
                         '3. EARTH WIRE — green and yellow striped insulation\n'
                         'Safety wire — carries NO CURRENT during normal operation.\n'
                         'Connected to the metal case of appliances.\n'
                         'If fault connects live to metal case → current flows through earth → fuse blows → circuit '
                         'breaks → safe.\n'
                         '\n'
                         'MEMORY: Live = Brown; Neutral = Blue; Earth = Green + Yellow.',
              'heading': 'Three-Core Cable'},
             {'content': 'FUSE: thin wire in series with live wire — MELTS if current exceeds safe level → circuit '
                         'breaks.\n'
                         'Rated in amps. Choose just ABOVE normal operating current.\n'
                         'Common ratings: 1 A, 3 A, 5 A, 13 A.\n'
                         '\n'
                         'CIRCUIT BREAKER: trips instead of melting — can be reset.\n'
                         'RCD (Residual Current Device): detects current imbalances — very fast response. Essential '
                         'for bathrooms and outdoor use.\n'
                         '\n'
                         'DOUBLE INSULATION:\n'
                         'Two layers of insulation between live parts and outer case.\n'
                         'No earth wire needed. Symbol: square within a square.\n'
                         '\n'
                         'EXAMPLE — selecting fuse:\n'
                         '1 kW kettle at 230 V: I = 1000 ÷ 230 ≈ 4.3 A → use 5 A fuse.',
              'heading': 'Fuses, Circuit Breakers and Safety'},
             {'content': 'WHY LIVE IS DANGEROUS:\n'
                         'Live is at ~230 V. Touching it while connected to earth → current through body → electric '
                         'shock.\n'
                         '\n'
                         'WHY FUSES AND SWITCHES GO IN THE LIVE WIRE:\n'
                         "If in the neutral wire → appliance still at 230 V when 'off' → dangerous.\n"
                         'In live wire → appliance fully isolated when switched off.\n'
                         '\n'
                         'COMMON HAZARDS:\n'
                         'Frayed cables — exposed live wire.\n'
                         'Overloaded sockets — too many appliances → excess current → heat → fire.\n'
                         'Water near appliances — water conducts electricity.\n'
                         'Damaged plugs — loose connections.',
              'heading': 'Electrical Safety'}],
  'title': 'Mains Electricity',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In P = I²R, CURRENT is squared, not resistance. Students often write P = I × R² by mistake. To '
                    'find I from power: use I = P ÷ V (not P = I²R unless R is known and V is not).',
  'equations': ['P = V × I', 'P = I² × R', 'E = P × t', 'E = V × Q'],
  'fifas': [{'label': 'Electrical Power',
             'question': 'A lamp operates at 240 V and draws 0.25 A. Calculate its power.',
             'steps': [('F', 'P = V × I'),
                       ('I', 'V = 240 V, I = 0.25 A'),
                       ('F', 'P = 240 × 0.25'),
                       ('A', 'P = 60 W')]}],
  'higher': None,
  'id': 'power-electricity',
  'key_note': 'P = VI. P = I²R. E = Pt. E = VQ. I = P/V for fuse selection — choose just above. UK mains = 230 V.',
  'matching': {'instruction': 'Match each scenario to the correct answer.',
               'pairs': [('24 W', 'V = 12 V, I = 2 A — P = 12 × 2'),
                         ('100 W', 'I = 10 A, R = 1 Ω — P = 10² × 1'),
                         ('3 A fuse', '690 W appliance on 230 V — I = 3 A'),
                         ('13 A fuse', '2300 W kettle on 230 V — I = 10 A')],
               'title': 'Power Calculations'},
  'quiz': [{'opts': [('72 W — P = I² × R = 9 × 8 = 72 W', True),
                     ('24 W — P = I × R = 3 × 8 (forgot to square I)', False),
                     ('576 W — P = I² × R² = 9 × 64 (squared both)', False),
                     ('2.67 W — P = R ÷ I', False)],
            'q': 'A resistor (R = 8 Ω) carries 3 A. What is the power dissipated?',
            'wrong_explanations': {1: 'P = I × R gives volts (A × Ω = V) — not watts. Must square the current.',
                                   2: 'Only CURRENT is squared: P = I²R = 9 × 8 = 72 W.',
                                   3: 'R ÷ I gives Ω/A — not watts. P = I²R.'}},
           {'opts': [('13 A — I = 1380 ÷ 230 = 6 A; next rating above 6 A is 13 A', True),
                     ('3 A — safest choice for any appliance', False),
                     ('5 A — just below 6 A so it will work', False),
                     ('1 A — smallest fuse is always safest', False)],
            'q': 'A 1380 W iron on 230 V mains. Which fuse?',
            'wrong_explanations': {1: 'A 3 A fuse would blow immediately — the iron draws ~6 A.',
                                   2: '5 A is BELOW the 6 A operating current — it would blow under normal use.',
                                   3: '1 A is far below operating current — would blow immediately.'}}],
  'rp': None,
  'spec': '6.2.4.1',
  'summary': 'Calculate electrical power using P = VI and P = I²R, and select appropriate fuse ratings.',
  'theory': [{'content': 'ELECTRICAL POWER is the rate of energy transfer by an electrical component.\n'
                         '\n'
                         'P = V × I\n'
                         'P = I² × R\n'
                         '\n'
                         'P = power (W)\n'
                         'V = potential difference (V)\n'
                         'I = current (A)\n'
                         'R = resistance (Ω)\n'
                         '\n'
                         'Use P = VI when you know V and I.\n'
                         'Use P = I²R when you know I and R.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Lamp: 12 V, 2 A.\n'
                         'P = 12 × 2 = 24 W\n'
                         'Check: R = 12/2 = 6 Ω; P = 2² × 6 = 4 × 6 = 24 W ✓',
              'heading': 'Electrical Power Equations'},
             {'content': 'E = P × t (energy in J, time in seconds)\n'
                         'E = V × Q (energy = pd × charge)\n'
                         '\n'
                         'EXAMPLE:\n'
                         '60 W lamp for 5 minutes:\n'
                         'E = 60 × 300 = 18,000 J\n'
                         '\n'
                         'Charge link:\n'
                         '150 C through 12 V component:\n'
                         'E = 12 × 150 = 1800 J',
              'heading': 'Energy and Charge'},
             {'content': 'Step 1: I = P ÷ V\n'
                         'Step 2: Choose fuse rated JUST ABOVE operating current.\n'
                         '\n'
                         'Common ratings: 1 A, 3 A, 5 A, 13 A.\n'
                         '\n'
                         'EXAMPLE 1 — 500 W TV at 230 V:\n'
                         'I = 500 ÷ 230 ≈ 2.2 A → 3 A fuse.\n'
                         '\n'
                         'EXAMPLE 2 — 2300 W kettle at 230 V:\n'
                         'I = 2300 ÷ 230 = 10 A → 13 A fuse.\n'
                         '\n'
                         'Fuse too low → blows in normal use.\n'
                         "Fuse too high → won't blow in a fault → dangerous.",
              'heading': 'Choosing the Correct Fuse'}],
  'title': 'Power',
  'triple_only': None,
  'variables': [('P', 'Power', 'watts', 'W'),
                ('V', 'Potential difference', 'volts', 'V'),
                ('I', 'Current', 'amperes', 'A'),
                ('R', 'Resistance', 'ohms', 'Ω'),
                ('E', 'Energy', 'joules', 'J'),
                ('Q', 'Charge', 'coulombs', 'C')]},
 {'common_mistake': 'For E = Pt in joules, time must be in SECONDS. For kWh, use kW and hours. Mixing units is the '
                    'most common error. High-power appliance used briefly can use LESS energy than a low-power one '
                    'running for hours.',
  'equations': ['E = P × t', 'Energy (kWh) = Power (kW) × time (hours)'],
  'fifas': [{'label': 'Energy Calculation',
             'question': 'A 1.5 kW toaster is used for 4 minutes. Calculate the energy transferred in joules.',
             'steps': [('F', 'E = P × t'),
                       ('I', 'P = 1500 W, t = 4 × 60 = 240 s'),
                       ('F', 'E = 1500 × 240'),
                       ('A', 'E = 360,000 J (360 kJ)')]}],
  'higher': None,
  'id': 'energy-transfers-appliances',
  'key_note': 'E = Pt (J, t in seconds). kWh = kW × hours. 1 kWh = 3.6 MJ. Cost = kWh × price/unit. Motor → kinetic; '
              'heater → thermal; lamp → light; speaker → sound; charger → chemical.',
  'matching': {'instruction': 'Match each appliance to its primary useful energy output.',
               'pairs': [('Electric motor', 'Kinetic energy — spinning drum, fan or drill'),
                         ('Electric heater', 'Thermal energy — heating room or food'),
                         ('Lamp/LED', 'Light — plus thermal as waste'),
                         ('Speaker', 'Sound — kinetic energy of vibrating air'),
                         ('Phone charger', 'Chemical energy — stored in rechargeable battery')],
               'title': 'Appliance Energy Transfers'},
  'quiz': [{'opts': [('6 kWh and £1.50 — 2 × 3 = 6 kWh; 6 × 25p = 150p', True),
                     ('6000 kWh — used watts not kilowatts: 2000 × 3 = 6000', False),
                     ('0.67 kWh — divided instead of multiplied', False),
                     ('6 kWh and 25p — cost = 1 unit regardless of amount', False)],
            'q': 'A 2 kW heater runs for 3 hours. How much energy does it use and what does it cost at 25p/kWh?',
            'wrong_explanations': {1: 'Must use KILOWATTS: 2 kW × 3 h = 6 kWh. Using 2000 W gives 6000 — wrong unit.',
                                   2: 'Energy = P × t = 2 kW × 3 h = 6 kWh. Must multiply.',
                                   3: 'Cost = energy × price per unit = 6 × 25p = 150p = £1.50.'}},
           {'opts': [('The fridge — 200 W × 24 h = 4.8 kWh vs kettle: 2 kW × (5/60) h ≈ 0.17 kWh', True),
                     ('The kettle — much higher power', False),
                     ('They use the same', False),
                     ('Cannot compare without knowing brands', False)],
            'q': 'A 200 W fridge runs continuously. A 2000 W kettle runs 5 min/day. Which uses more energy in 24 '
                 'hours?',
            'wrong_explanations': {1: 'Higher power ≠ higher energy use — energy = power × TIME. Fridge runs 24 h; '
                                      'kettle runs only 5 min.',
                                   2: 'Energy = power × time. Fridge: 0.2 × 24 = 4.8 kWh. Kettle: 2 × (5/60) ≈ 0.17 '
                                      'kWh.',
                                   3: "Power and time are all that's needed — brand is irrelevant."}}],
  'rp': None,
  'spec': '6.2.4.2',
  'summary': 'Calculate energy transferred using E = Pt, use kWh and describe appliance energy transfers.',
  'theory': [{'content': 'Every electrical appliance transfers energy from the electrical store:\n'
                         '\n'
                         'ELECTRIC MOTOR (washing machine, fan, drill): electrical → kinetic + thermal\n'
                         'ELECTRIC HEATER (oven, toaster): electrical → thermal\n'
                         'LAMP/LED: electrical → light + thermal\n'
                         'SPEAKER: electrical → sound\n'
                         'CHARGER: electrical → chemical (battery)\n'
                         '\n'
                         'All appliances dissipate some energy as thermal — no appliance is 100% efficient.',
              'heading': 'Energy Transfers in Appliances'},
             {'content': 'E = P × t (joules; time in SECONDS)\n'
                         '\n'
                         'EXAMPLE 1:\n'
                         '2 kW kettle for 3 minutes:\n'
                         'P = 2000 W, t = 180 s\n'
                         'E = 2000 × 180 = 360,000 J\n'
                         '\n'
                         'KILOWATT-HOUR (kWh) — energy company unit:\n'
                         'Energy (kWh) = Power (kW) × time (hours)\n'
                         '1 kWh = 3,600,000 J\n'
                         '\n'
                         'EXAMPLE 2:\n'
                         '3 kW shower for 0.5 hours:\n'
                         'Energy = 3 × 0.5 = 1.5 kWh',
              'heading': 'Calculating Energy Transferred'},
             {'content': 'Cost = energy (kWh) × price per kWh\n'
                         '\n'
                         'EXAMPLE:\n'
                         '1.5 kWh at 30p per kWh = 45p\n'
                         '\n'
                         'COMPARING APPLIANCES:\n'
                         'High power × short time vs low power × long time:\n'
                         'Fridge: 200 W × 24 h = 4.8 kWh/day\n'
                         'Kettle: 2 kW × 5 min/day ≈ 0.17 kWh/day\n'
                         'Fridge uses far more despite lower power — it runs continuously.\n'
                         '\n'
                         'REDUCING ENERGY USE:\n'
                         'LED bulbs instead of filament.\n'
                         'Shorter usage times.\n'
                         'Better insulation → less heating demand.',
              'heading': 'Energy Cost and Comparison'}],
  'title': 'Energy Transfers in Everyday Appliances',
  'triple_only': None,
  'variables': [('E', 'Energy transferred', 'joules', 'J'),
                ('P', 'Power', 'watts', 'W'),
                ('t', 'Time', 'seconds', 's')]},
 {'common_mistake': 'Transformers only work with AC — DC produces no output. High voltage reduces CURRENT (not power) '
                    '— cable losses are proportional to I² so even a small current reduction gives large savings.',
  'equations': ['Vp ÷ Vs = np ÷ ns', 'P_lost in cables = I² × R'],
  'fifas': [{'label': 'Transformer Calculation',
             'question': 'A step-down transformer: 2000 primary turns, 100 secondary turns, primary voltage 230,000 V. '
                         'Find secondary voltage.',
             'steps': [('F', 'Vs = Vp × (ns ÷ np)'),
                       ('I', 'Vp = 230,000 V; np = 2000; ns = 100'),
                       ('F', 'Vs = 230,000 × (100 ÷ 2000) = 230,000 × 0.05'),
                       ('A', 'Vs = 11,500 V')]}],
  'higher': None,
  'id': 'national-grid',
  'key_note': 'Power stations → step-up → high-voltage cables → step-down → homes (230 V). High V = low I = low I²R '
              'losses. Step-up: more secondary turns. Step-down: fewer secondary turns. Transformers: AC only. Vp/Vs = '
              'np/ns.',
  'matching': {'instruction': 'Match each component to its role.',
               'pairs': [('Step-up transformer',
                          'At power stations — increases voltage to ~400 kV for efficient transmission'),
                         ('Transmission cables', 'Carry high-voltage AC across the country on pylons or underground'),
                         ('Step-down transformer', 'At substations — reduces voltage to 230 V for homes'),
                         ('High-voltage transmission', 'Reduces current → reduces I²R losses — more efficient')],
               'title': 'National Grid Components'},
  'quiz': [{'opts': [('High voltage means lower current for the same power — lower current means far less I²R heating '
                      'in cables',
                      True),
                     ('High voltage means higher current — more charge carriers reduce resistance', False),
                     ('Cables are designed only for high voltage — they cannot carry low voltage', False),
                     ('High voltage prevents cable corrosion in rain', False)],
            'q': 'Why is electricity transmitted at high voltage across the National Grid?',
            'wrong_explanations': {1: 'P = IV — for same power, high V means LOW current. Lower current → I²R losses '
                                      'much smaller.',
                                   2: 'Cable design is for mechanical and safety reasons — efficiency is determined by '
                                      'current levels.',
                                   3: 'Voltage has no effect on corrosion — cables are protected by materials '
                                      'regardless of voltage.'}},
           {'opts': [('1000 V — Vs = 20,000 × (200 ÷ 4000) = 20,000 × 0.05 = 1000 V', True),
                     ('400,000 V — Vs = 20,000 × (4000 ÷ 200) (inverted ratio)', False),
                     ('100 V — incorrect ratio calculation', False),
                     ('20,000 V — voltage unchanged through transformer', False)],
            'q': 'A transformer has 4000 primary turns, 200 secondary turns, primary voltage 20,000 V. What is the '
                 'secondary voltage?',
            'wrong_explanations': {1: 'Using np/ns inverts the ratio: Vs = Vp × (ns/np) = 20,000 × (200/4000) = 1000 V '
                                      '— not ×20.',
                                   2: 'Check: ns/np = 200/4000 = 0.05. Vs = 20,000 × 0.05 = 1000 V, not 100 V.',
                                   3: 'Transformers CHANGE the voltage — that is their purpose. Vs = Vp × (ns/np).'}}],
  'rp': None,
  'spec': '6.2.4.3',
  'summary': 'Explain how the National Grid transmits electricity efficiently and the role of transformers.',
  'theory': [{'content': 'The NATIONAL GRID is the network of cables and transformers transmitting electrical energy '
                         'from power stations to consumers.\n'
                         '\n'
                         'Path:\n'
                         'POWER STATIONS → STEP-UP TRANSFORMERS → HIGH-VOLTAGE CABLES → STEP-DOWN TRANSFORMERS → HOMES '
                         '(230 V)\n'
                         '\n'
                         'Transmission uses very high voltages (132 kV to 400 kV).\n'
                         'Before homes receive it, voltage is stepped down to 230 V by local substations.',
              'heading': 'What Is the National Grid?'},
             {'content': 'P = IV. For a given power:\n'
                         'High voltage → LOW current (for the same power)\n'
                         'Low current → less I²R heating in cables → less energy wasted.\n'
                         '\n'
                         'Current is SQUARED in power loss (P = I²R) — halving current reduces cable losses by ¾.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Transmit 1 MW through cables (R = 10 Ω):\n'
                         'At 1000 V: I = 1000 A → P_lost = 1000² × 10 = 10 MW (more than transmitted!)\n'
                         'At 100,000 V: I = 10 A → P_lost = 10² × 10 = 1000 W (tiny fraction)\n'
                         '\n'
                         'High voltage = far more efficient.',
              'heading': 'Why Transmit at High Voltage?'},
             {'content': 'TRANSFORMERS change voltage of AC only (not DC).\n'
                         '\n'
                         'STEP-UP: increases voltage (decreases current) — at power stations.\n'
                         'STEP-DOWN: decreases voltage (increases current) — at local substations.\n'
                         '\n'
                         'Transformer equation:\n'
                         'Vp ÷ Vs = np ÷ ns\n'
                         '\n'
                         'Vp = primary voltage; Vs = secondary voltage\n'
                         'np = primary turns; ns = secondary turns\n'
                         '\n'
                         'EXAMPLE:\n'
                         '500 primary turns, 50 secondary turns, Vp = 10,000 V:\n'
                         'Vs = 10,000 × (50 ÷ 500) = 1000 V (step-down)',
              'heading': 'Transformers'}],
  'title': 'The National Grid',
  'triple_only': None,
  'variables': [('Vp', 'Primary voltage', 'volts', 'V'),
                ('Vs', 'Secondary voltage', 'volts', 'V'),
                ('np', 'Primary turns', '', ''),
                ('ns', 'Secondary turns', '', ''),
                ('I', 'Current', 'amperes', 'A'),
                ('P', 'Power', 'watts', 'W')]},
 {'common_mistake': 'Only ELECTRONS move when static charge builds up — positive charges do not move. Rubbing makes '
                    'one object negative (gains electrons) and one positive (loses electrons). Like charges repel, '
                    'opposite charges attract — the same rule as for magnets but remember that electrical charges and '
                    'magnetic poles are completely different things.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'static-charge',
  'key_note': 'Static: electrons transfer when insulators rubbed → one negative, one positive. Like charges repel; '
              "opposite attract. Conductors can't hold static (charge flows). Applications: inkjet printers, "
              'photocopiers, precipitators, spray painting. Hazards: fuel tankers, ESD. Induction: charged object '
              'causes charge separation in neutral conductor.',
  'matching': {'instruction': 'Match each scenario to the correct electrostatic explanation.',
               'pairs': [('Negative charge on rod',
                          'Gains electrons when rubbed with cloth — electrons transferred to rod'),
                         ('Positive charge on cloth', 'Loses electrons to the rod — left with net positive charge'),
                         ('Balloon sticks to wall',
                          'Balloon induces opposite charge on wall surface — opposite charges attract'),
                         ('Hair standing up after rubbing',
                          'All hairs gain same charge — like charges repel, hairs push apart')],
               'title': 'Static Charge'},
  'quiz': [{'opts': [('Electrons transferred from the cloth to the rod — rod gains electrons (negative), cloth loses '
                      'electrons (positive)',
                      True),
                     ('Protons transferred from the cloth to the rod — rod gains positive charge', False),
                     ('Electrons were created in the rod by rubbing — friction generates new electrons', False),
                     ('Both positive and negative charges transferred — more negative arrived in the rod', False)],
            'q': 'A plastic rod is rubbed with a woollen cloth and becomes negatively charged. What has happened?',
            'wrong_explanations': {1: 'Protons are fixed in the nucleus — they cannot be transferred by rubbing. Only '
                                      'electrons move.',
                                   2: 'Charge is conserved — rubbing transfers existing charges, it does not create '
                                      'new ones.',
                                   3: 'Both types of charge do not transfer simultaneously in this way — only '
                                      'electrons (negative) move.'}},
           {'opts': [('They give soot particles an electric charge so they are attracted to oppositely charged '
                      'collection plates — removing particulates from the exhaust gas',
                      True),
                     ('They heat the smoke so soot burns completely before leaving the chimney', False),
                     ('They use magnetic fields to filter out metal particles from the smoke', False),
                     ('They dissolve soot in water sprayed into the chimney', False)],
            'q': 'Why are electrostatic precipitators used in power station chimneys?',
            'wrong_explanations': {1: "Precipitators use electrostatics — not heat. They don't burn the soot.",
                                   2: 'Precipitators are electrical devices — they use electric fields, not magnetic '
                                      'fields.',
                                   3: 'Scrubbers (wet systems) dissolve gases like SO₂ — precipitators work by '
                                      'electrostatic attraction to plates.'}}],
  'rp': None,
  'spec': '6.2.5 (physics only)',
  'summary': 'Describe static electricity, explain how charges build up and describe electric fields.',
  'theory': [{'content': 'STATIC ELECTRICITY arises when electric charge builds up on an insulating material.\n'
                         '\n'
                         'HOW STATIC CHARGE BUILDS UP:\n'
                         'When two insulating materials are RUBBED together, electrons transfer from one to the '
                         'other.\n'
                         'Material gaining electrons → becomes NEGATIVELY charged.\n'
                         'Material losing electrons → becomes POSITIVELY charged.\n'
                         '\n'
                         'CHARGE IS CONSERVED: total charge before = total charge after. The charges are equal and '
                         'opposite.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Rubbing a plastic rod with a cloth: rod becomes negatively charged, cloth becomes positively '
                         'charged.\n'
                         'Walking on carpet: body builds up charge (electrons transfer to feet or from carpet).\n'
                         'Nylon clothing rubbed against skin.\n'
                         '\n'
                         'ONLY ELECTRONS MOVE — protons are fixed in the nucleus. Positive charge is created by '
                         'REMOVING electrons, not by adding protons.\n'
                         '\n'
                         'INSULATORS vs CONDUCTORS:\n'
                         'Insulators: charge stays where it is built up — cannot flow away.\n'
                         'Conductors: charge spreads across the surface immediately — cannot build up static.',
              'heading': 'Building Up Static Charge'},
             {'content': 'LIKE CHARGES REPEL — two positive charges or two negative charges push each other apart.\n'
                         'OPPOSITE CHARGES ATTRACT — positive and negative charges pull each other together.\n'
                         '\n'
                         'This is a NON-CONTACT FORCE — charges exert forces across empty space.\n'
                         '\n'
                         'DEMONSTRATIONS:\n'
                         'Charged balloon sticks to a wall — the charged balloon induces an opposite charge on the '
                         'wall surface.\n'
                         'Two charged rods of same material repel each other.\n'
                         'Hair standing up after rubbing — all hairs gain the same charge and repel each other.\n'
                         '\n'
                         'INDUCTION:\n'
                         'A charged object brought near a neutral conductor causes charge SEPARATION (induction).\n'
                         'Free electrons in conductor move towards or away from the charged object.\n'
                         'Nearest end becomes opposite charge to the object → attraction.\n'
                         '\n'
                         'ELECTROSTATIC HAZARDS:\n'
                         'Fuel tankers: static builds up from fuel flowing through pipes → spark → fire/explosion '
                         'risk.\n'
                         'Electronic components: sensitive to electrostatic discharge (ESD) — wear antistatic '
                         'wristbands.\n'
                         'Lightning: massive electrostatic discharge between cloud and earth.',
              'heading': 'Forces Between Charges'},
             {'content': 'INKJET PRINTERS:\n'
                         'Tiny ink droplets given different charges → deflected by charged plates → precise '
                         'positioning.\n'
                         'Computer controls charge on each droplet → forms text and images.\n'
                         '\n'
                         'LASER PRINTERS / PHOTOCOPIERS:\n'
                         'Drum given static charge.\n'
                         'Laser removes charge from non-printing areas.\n'
                         'Toner (charged powder) sticks to charged areas → transferred to paper → heated to fuse.\n'
                         '\n'
                         'ELECTROSTATIC PRECIPITATORS (smoke filters):\n'
                         'Electrodes create strong electric field in chimney.\n'
                         'Soot particles gain charge → attracted to oppositely charged plates → fall into collection '
                         'bin.\n'
                         'Reduces particulate pollution from power stations and factories.\n'
                         '\n'
                         'SPRAY PAINTING:\n'
                         'Spray gun charges paint droplets.\n'
                         'Object to be painted is given opposite charge.\n'
                         'Paint attracted to surface evenly — even coverage, less waste.\n'
                         'Used in car manufacturing.\n'
                         '\n'
                         'DEFIBRILLATORS:\n'
                         'Deliver controlled electric shock to restart heart.\n'
                         "Capacitors store charge then discharge through patient's chest.",
              'heading': 'Applications of Static Electricity'}],
  'title': 'Static Charge',
  'triple_only': 'Static charge (physics only) — not in Combined Science.',
  'variables': []},
 {'common_mistake': 'Electric field lines go from POSITIVE to NEGATIVE — the direction a positive charge would move. '
                    "Don't confuse with magnetic field lines which go from N to S. A uniform field (between parallel "
                    'plates) has equal spacing — field strength is the same at all points.',
  'equations': ['E = F ÷ q'],
  'fifas': [],
  'higher': None,
  'id': 'electric-fields',
  'key_note': 'Electric field: force per unit charge. Field lines: + to −, closer = stronger. Patterns: single charges '
              'radiate; opposite charges arc between them; uniform field between parallel plates. E = F/q. Sparks: air '
              'ionised in strong fields. Lightning conductor: provides safe discharge path.',
  'matching': {'instruction': 'Match each charge configuration to its field pattern.',
               'pairs': [('Single positive charge', 'Field lines radiate OUTWARD in all directions from the charge'),
                         ('Single negative charge', 'Field lines point INWARD toward the charge from all directions'),
                         ('Two opposite charges',
                          'Field lines arc from positive to negative — strong attractive field between them'),
                         ('Two parallel plates (+ and −)',
                          'Uniform field — parallel equally-spaced lines between the plates')],
               'title': 'Electric Field Patterns'},
  'quiz': [{'opts': [('From positive to negative — the direction a positive test charge would experience a force',
                      True),
                     ('From negative to positive — field lines follow electron flow direction', False),
                     ('In random directions depending on the shape of the charged object', False),
                     ('Always horizontally — electric fields are always horizontal', False)],
            'q': 'In which direction do electric field lines point?',
            'wrong_explanations': {1: 'Field lines go from + to − (the direction of conventional current/positive '
                                      'charge flow) — not from − to +.',
                                   2: 'Field directions are fixed by convention and the geometry of the charges — not '
                                      'random.',
                                   3: 'Electric fields can point in any direction depending on the charge '
                                      'configuration.'}},
           {'opts': [('The pointed conductor creates a strong local electric field that safely channels the discharge '
                      'to earth via a low-resistance conducting path',
                      True),
                     ('The conductor blocks the electric field between the cloud and building — the charge disperses '
                      'harmlessly',
                      False),
                     ("The conductor absorbs the charge into the building's structure — distributing it safely", False),
                     ('The conductor reflects the lightning bolt away from the building', False)],
            'q': 'Why does a lightning conductor protect a building?',
            'wrong_explanations': {1: "Conductors don't block or absorb electric fields — they provide a preferred "
                                      'discharge PATH to earth.',
                                   2: 'Lightning conductors deliberately attract lightning (via strong local field at '
                                      "the point) and channel it safely to earth — they don't reflect it.",
                                   3: 'Charge goes through the conductor to earth — not into the building '
                                      'structure.'}}],
  'rp': None,
  'spec': '6.2.6 (physics only)',
  'summary': 'Describe electric fields around charges, represent them with field lines, and apply to sparks.',
  'theory': [{'content': 'An ELECTRIC FIELD is a region around a charged object where any other charged object '
                         'experiences a force.\n'
                         '\n'
                         'FIELD LINES show the direction and strength of the field:\n'
                         'Arrows point from POSITIVE to NEGATIVE (direction a positive charge would move).\n'
                         'Closer field lines → STRONGER field.\n'
                         'Field lines never cross.\n'
                         '\n'
                         'FIELD PATTERNS:\n'
                         'SINGLE POSITIVE CHARGE: field lines radiate outward in all directions.\n'
                         'SINGLE NEGATIVE CHARGE: field lines point inward from all directions.\n'
                         'TWO OPPOSITE CHARGES: field lines arc from positive to negative — strong between them.\n'
                         'TWO LIKE CHARGES: field lines curve away from each other — neutral point between them.\n'
                         'UNIFORM FIELD (between parallel plates): parallel, equally spaced horizontal lines — '
                         'constant strength.\n'
                         '\n'
                         'The electric field is a vector — it has both magnitude and direction at every point.',
              'heading': 'Electric Fields'},
             {'content': 'A charge placed in an electric field experiences a FORCE:\n'
                         'Positive charge: force in the direction of the field (along field lines).\n'
                         'Negative charge: force opposite to the direction of the field.\n'
                         '\n'
                         'The POTENTIAL DIFFERENCE (voltage) drives the movement of charge through an electric field.\n'
                         '\n'
                         'NON-CONTACT FORCE:\n'
                         'Electric fields allow charges to exert forces on each other WITHOUT TOUCHING.\n'
                         'This is the same principle as magnetic fields and gravitational fields.\n'
                         '\n'
                         'ELECTRIC FIELD STRENGTH:\n'
                         'Defined as the force per unit charge: E = F/q\n'
                         'Stronger field → larger force on a given charge.\n'
                         '\n'
                         'BETWEEN PARALLEL PLATES:\n'
                         'Uniform field — force on a charge is constant everywhere between the plates.\n'
                         'Basis of many electronic devices (capacitors, CRT screens, particle accelerators).',
              'heading': 'Electric Force and Potential Difference'},
             {'content': 'When an ELECTRIC FIELD becomes strong enough, air itself becomes conducting.\n'
                         '\n'
                         'SPARKS:\n'
                         'Very strong electric field near a sharp point or charged conductor.\n'
                         'Air molecules ionised — electrons stripped from air atoms.\n'
                         'Ionised air conducts → sudden discharge → spark.\n'
                         '\n'
                         'LIGHTNING:\n'
                         'Massive charge builds up in storm clouds.\n'
                         'Electric field between cloud and earth becomes extremely strong.\n'
                         'Air breaks down → conducting channel forms → lightning strikes.\n'
                         'Lightning conductors: pointed metal rods on buildings → provide low-resistance path to '
                         'earth.\n'
                         'Reduces risk of building being struck or damaged.\n'
                         '\n'
                         'STATIC ELECTRICITY LINK:\n'
                         'When a charged object is brought near an earthed conductor:\n'
                         'Electric field between them becomes strong.\n'
                         'A spark (discharge) may occur, transferring charge rapidly.\n'
                         'This is why fuel tankers earth themselves before refuelling — prevents spark igniting fuel.',
              'heading': 'Sparks and Electric Discharge'}],
  'title': 'Electric Fields',
  'triple_only': 'Electric fields (physics only) — not in Combined Science.',
  'variables': [('E', 'Electric field strength', 'N/C', 'N/C'),
                ('F', 'Force', 'newtons', 'N'),
                ('q', 'Charge', 'coulombs', 'C')]}],

"particle-model": [{'common_mistake': 'Units for density are kg/m³ (SI) or g/cm³ (also common). Do NOT mix — if mass is in grams and '
                    'volume in cm³, density comes out in g/cm³. Convert to kg/m³ by multiplying by 1000. Also: 1 cm³ = '
                    '1 × 10⁻⁶ m³.',
  'equations': ['ρ = m ÷ V'],
  'fifas': [{'label': 'Density Calculation',
             'question': 'A block has mass 540 g and volume 200 cm³. Calculate its density in g/cm³.',
             'steps': [('F', 'ρ = m ÷ V'),
                       ('I', 'm = 540 g, V = 200 cm³'),
                       ('F', 'ρ = 540 ÷ 200'),
                       ('A', 'ρ = 2.7 g/cm³ (aluminium)')]}],
  'higher': None,
  'id': 'density-of-materials',
  'key_note': 'ρ = m/V. Units: kg/m³. Denser = more mass per volume. Solids > liquids > gases (usually). Ice less '
              'dense than water (exception). Float if ρ_object < ρ_fluid. RP17: regular solids — measure dimensions; '
              'irregular solids — displacement method.',
  'matching': {'instruction': 'Match each scenario to the correct density or mass value.',
               'pairs': [('2700 kg/m³',
                          'Aluminium block: mass = 270 g, volume = 100 cm³ (in consistent units: 0.27 kg ÷ 1×10⁻⁴ m³)'),
                         ('Floats', 'Object with density 800 kg/m³ placed in water (density 1000 kg/m³)'),
                         ('Sinks', 'Object with density 8000 kg/m³ placed in water (density 1000 kg/m³)'),
                         ('Displacement method', 'Used to find the volume of an irregularly shaped solid')],
               'title': 'Density Calculations'},
  'quiz': [{'opts': [('0.8 g/cm³ — ρ = m ÷ V = 800 ÷ 1000 = 0.8 g/cm³', True),
                     ('1.25 g/cm³ — ρ = V ÷ m = 1000 ÷ 800', False),
                     ('800,000 g/cm³ — multiplied instead of divided', False),
                     ('1.0 g/cm³ — density of all liquids is always 1 g/cm³', False)],
            'q': 'A liquid has mass 800 g and volume 1000 cm³. What is its density in g/cm³?',
            'wrong_explanations': {1: 'ρ = V ÷ m inverts the formula — it gives cm³/g, not g/cm³. Always divide MASS '
                                      'by VOLUME.',
                                   2: 'Multiplying mass × volume gives g·cm³ — not a density unit.',
                                   3: 'Only WATER has density 1 g/cm³ — other liquids vary. This liquid (0.8 g/cm³) '
                                      'would float on water.'}},
           {'opts': [('Ice is less dense than liquid water — its particles are arranged in a more open lattice '
                      'structure, giving lower density (917 kg/m³ vs 1000 kg/m³)',
                      True),
                     ('Ice is lighter than water because it is frozen — freezing reduces mass', False),
                     ('Ice floats because it is a solid — all solids float on their liquid form', False),
                     ('Ice has more volume than the same mass of water — it sinks if enough weight is added', False)],
            'q': 'Why does ice float on water?',
            'wrong_explanations': {1: "Freezing doesn't change mass — the same molecules are present. Ice floats "
                                      'because of LOWER DENSITY, not lower mass.',
                                   2: 'Most solids are DENSER than their liquid form (e.g. solid iron sinks in liquid '
                                      'iron). Water/ice is a special exception.',
                                   3: 'Ice is less dense because its crystal structure spreads particles further apart '
                                      "— and because it's less dense, it floats. The last part of the option is "
                                      'correct (adding weight to ice can sink it) but irrelevant to why ice naturally '
                                      'floats.'}}],
  'rp': 'RP17 (Physics) — Determine densities of regular solids (measure dimensions), irregular solids (displacement), '
        'and liquids (measure cylinder with balance). ρ = m/V.',
  'spec': '6.3.1.1',
  'summary': 'Define density and calculate it from mass and volume for solids and liquids.',
  'theory': [{'content': "DENSITY is a measure of how much mass is packed into a given volume — how 'compact' a "
                         'material is.\n'
                         '\n'
                         'EQUATION:\n'
                         'ρ = m ÷ V\n'
                         '\n'
                         'ρ = density (kg/m³)\n'
                         'm = mass (kg)\n'
                         'V = volume (m³)\n'
                         '\n'
                         'Rearranging:\n'
                         'm = ρ × V\n'
                         'V = m ÷ ρ\n'
                         '\n'
                         'Common density values:\n'
                         'Water: 1000 kg/m³\n'
                         'Aluminium: 2700 kg/m³\n'
                         'Iron/steel: 7800 kg/m³\n'
                         'Air: ~1.2 kg/m³\n'
                         'Gold: 19,300 kg/m³\n'
                         'Ice: 917 kg/m³ (less dense than liquid water — why ice floats)\n'
                         '\n'
                         'DENSITY AND FLOATING:\n'
                         'Objects FLOAT in a fluid if their density is LESS than the fluid.\n'
                         'Objects SINK if their density is GREATER than the fluid.',
              'heading': 'What Is Density?'},
             {'content': 'The particle model explains density differences between states and materials:\n'
                         '\n'
                         'SOLIDS:\n'
                         'Particles tightly packed in a regular lattice.\n'
                         'High density — many particles in a small volume.\n'
                         '\n'
                         'LIQUIDS:\n'
                         'Particles close together but able to flow.\n'
                         'Slightly lower density than solids (usually) — particles slightly further apart.\n'
                         'Exceptions: water is denser than ice (ice has a more open lattice structure).\n'
                         '\n'
                         'GASES:\n'
                         'Particles far apart — mostly empty space.\n'
                         'Very low density — much lower than solids or liquids.\n'
                         'Example: air is ~800× less dense than water.\n'
                         '\n'
                         'DIFFERENT MATERIALS:\n'
                         'Denser materials have either heavier atoms (higher atomic mass) or more tightly packed '
                         'atomic structures.\n'
                         'Gold (dense): heavy atoms + tightly packed.\n'
                         'Aluminium (less dense): lighter atoms.\n'
                         'Polystyrene (very low density): mostly air — open foam structure.',
              'heading': 'Particle Model Explanation of Density'},
             {'content': 'REQUIRED PRACTICAL (RP17) — Determine densities of regular and irregular solids and '
                         'liquids.\n'
                         '\n'
                         'REGULAR SOLID (e.g. a cuboid or cylinder):\n'
                         'Measure dimensions with a RULER, MICROMETER or VERNIER CALLIPERS.\n'
                         'Calculate volume: V = l × w × h (cuboid) or V = πr²h (cylinder).\n'
                         'Measure mass with a BALANCE.\n'
                         'Calculate: ρ = m ÷ V\n'
                         '\n'
                         'IRREGULAR SOLID (e.g. a stone):\n'
                         'Measure mass with a BALANCE.\n'
                         'Fill a measuring cylinder with water, note initial volume.\n'
                         'LOWER the solid into the water using a thread.\n'
                         'Note the new volume — the rise = volume of the solid (DISPLACEMENT METHOD).\n'
                         'Calculate: ρ = m ÷ ΔV\n'
                         '\n'
                         'LIQUID:\n'
                         'Place an empty measuring cylinder on a balance and zero it (tare).\n'
                         'Pour a known volume of liquid in.\n'
                         'Read the mass.\n'
                         'Calculate: ρ = m ÷ V\n'
                         '\n'
                         'SOURCES OF ERROR:\n'
                         'Air bubbles trapped under the object in displacement.\n'
                         'Parallax error reading the meniscus in a measuring cylinder.\n'
                         'Not drying the solid before measuring mass after displacement.',
              'heading': 'Measuring Density — Required Practical'}],
  'title': 'Density of Materials',
  'triple_only': None,
  'variables': [('ρ', 'Density', 'kg/m³', 'kg/m³'), ('m', 'Mass', 'kilograms', 'kg'), ('V', 'Volume', 'm³', 'm³')]},
 {'common_mistake': 'Changes of state are PHYSICAL changes — not chemical. The substance remains the same chemical '
                    'compound throughout. Mass is ALWAYS conserved in a change of state — the number of particles '
                    "doesn't change, only their arrangement.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'changes-of-state',
  'key_note': 'Solid → liquid: melting. Liquid → gas: boiling/evaporation. Reverse: freezing, condensation. '
              'Sublimation: solid → gas directly. All are physical changes — reversible, mass conserved. Particles '
              'rearrange but are not created or destroyed.',
  'matching': {'instruction': 'Match each change of state to its name and direction.',
               'pairs': [('Melting',
                          'Solid → liquid — energy supplied, particles gain enough energy to break from lattice'),
                         ('Freezing', 'Liquid → solid — energy removed, particles slow down and form fixed lattice'),
                         ('Evaporation/Boiling',
                          'Liquid → gas — energy supplied, particles escape intermolecular forces'),
                         ('Condensation',
                          'Gas → liquid — energy removed, particles slow and intermolecular forces pull them together'),
                         ('Sublimation', 'Solid → gas directly — e.g. dry ice (solid CO₂) at room temperature')],
               'title': 'Change of State Match'},
  'quiz': [{'opts': [('200 g — mass is conserved during changes of state; no particles are created or destroyed', True),
                     ('Less than 200 g — some water evaporates as it cools', False),
                     ('More than 200 g — ice is larger in volume so it must be heavier', False),
                     ('Depends on temperature — colder freezers produce heavier ice', False)],
            'q': '200 g of water is placed in a freezer and completely freezes. What is the mass of the ice formed?',
            'wrong_explanations': {1: 'In a sealed container with no evaporation, mass is perfectly conserved — but '
                                      'even with some evaporation, the PRINCIPLE is conservation of mass in a change '
                                      'of state.',
                                   2: 'Ice IS larger in volume than liquid water — but volume and mass are different. '
                                      'The MASS is the same; ice is simply less dense.',
                                   3: 'Temperature affects rate of freezing and final temperature, not the mass of ice '
                                      'formed.'}},
           {'opts': [("No new substances are formed — the material's chemical identity is preserved and the change is "
                      'reversible',
                      True),
                     ('Melting only affects the surface of the solid — the inside remains chemically unchanged', False),
                     ('Physical changes always involve energy, while chemical changes do not', False),
                     ('Melting is chemical because the structure of the material is permanently altered', False)],
            'q': 'Why is melting a physical change rather than a chemical change?',
            'wrong_explanations': {1: 'Melting is a bulk process — the entire solid changes state, not just the '
                                      'surface.',
                                   2: 'Both chemical and physical changes can involve energy. The distinction is '
                                      'whether new chemical substances are formed.',
                                   3: 'The ARRANGEMENT of particles changes (structure), but the CHEMICAL IDENTITY '
                                      "doesn't — it's still the same compound. Chemical changes produce new "
                                      'substances.'}}],
  'rp': None,
  'spec': '6.3.1.2',
  'summary': 'Describe changes of state in terms of particles and explain why mass is conserved.',
  'theory': [{'content': 'Matter exists in three main states: SOLID, LIQUID and GAS.\n'
                         '\n'
                         'Changes of state occur when enough energy is supplied or removed:\n'
                         '\n'
                         'SOLID → LIQUID: MELTING (energy supplied)\n'
                         'LIQUID → SOLID: FREEZING (energy removed)\n'
                         'LIQUID → GAS: EVAPORATION/BOILING (energy supplied)\n'
                         'GAS → LIQUID: CONDENSATION (energy removed)\n'
                         'SOLID → GAS (directly): SUBLIMATION (energy supplied)\n'
                         'GAS → SOLID (directly): DEPOSITION (energy removed)\n'
                         '\n'
                         'MASS IS CONSERVED:\n'
                         'When a substance changes state, no particles are created or destroyed — they simply '
                         'rearrange.\n'
                         'The total mass before = total mass after.\n'
                         'Example: 100 g of ice melts to give exactly 100 g of liquid water.',
              'heading': 'The States of Matter and Changes of State'},
             {'content': 'Changes of state are PHYSICAL CHANGES — NOT chemical changes.\n'
                         '\n'
                         'Key difference:\n'
                         'PHYSICAL change: the substance keeps its chemical identity — REVERSIBLE.\n'
                         'CHEMICAL change: new substances are formed — usually irreversible.\n'
                         '\n'
                         'Why changes of state are physical:\n'
                         'No new chemical bonds are formed or broken between different types of molecule.\n'
                         'Water freezing: H₂O molecules are still H₂O — just rearranged in a lattice.\n'
                         'Water evaporating: H₂O molecules still exist as individual molecules in the gas.\n'
                         '\n'
                         'The change can be REVERSED:\n'
                         'Ice melts → water → refreezes → ice again. Same substance throughout.\n'
                         '\n'
                         'Contrast with chemical change:\n'
                         'Burning wood: wood + oxygen → CO₂ + water. Original material cannot be recovered.',
              'heading': 'Physical vs Chemical Changes'},
             {'content': 'SOLID:\n'
                         'Particles in fixed positions in a regular lattice.\n'
                         'Vibrate in place — cannot flow.\n'
                         'Strong intermolecular forces hold them together.\n'
                         '\n'
                         'LIQUID:\n'
                         'Particles close together but able to move past each other.\n'
                         'No fixed arrangement — can flow and take the shape of the container.\n'
                         'Weaker intermolecular forces than solid.\n'
                         '\n'
                         'GAS:\n'
                         'Particles far apart — mostly empty space.\n'
                         'Move rapidly in all directions — random motion.\n'
                         'Very weak intermolecular forces (effectively none).\n'
                         'Fill any container.\n'
                         '\n'
                         'DURING MELTING:\n'
                         'Energy supplied → particles vibrate more → forces between particles overcome → lattice '
                         'breaks down → particles begin to flow.\n'
                         '\n'
                         'DURING BOILING:\n'
                         'Energy supplied → particles gain enough energy to completely overcome intermolecular forces '
                         '→ escape from liquid surface into gas phase.',
              'heading': 'Particle Explanation of Changes of State'}],
  'title': 'Changes of State',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'During a CHANGE OF STATE, temperature stays CONSTANT — energy goes into potential energy '
                    '(breaking bonds), not kinetic energy. Students often think heating always raises temperature — '
                    'but at melting/boiling point, temperature is flat on the heating curve until the change is '
                    'complete.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'internal-energy',
  'key_note': 'Internal energy = KE + PE of all particles. Heating → increases internal energy → either raises '
              'temperature (KE) or causes change of state (PE). Temperature = average KE per particle. During change '
              'of state: temperature constant, PE increasing. Heating curve: slopes = temperature rise; flat sections '
              '= changes of state.',
  'matching': {'instruction': 'Match each statement to the correct concept.',
               'pairs': [('Internal energy', 'Total kinetic + potential energy of ALL particles in the system'),
                         ('Temperature', 'Measure of AVERAGE kinetic energy per particle'),
                         ('Flat section on heating curve',
                          'Change of state — temperature constant, energy increasing PE (breaking bonds)'),
                         ('Sloping section on heating curve',
                          'Temperature rising — energy increasing KE of particles')],
               'title': 'Internal Energy Concepts'},
  'quiz': [{'opts': [('A change of state — energy is increasing potential energy to break intermolecular bonds, not '
                      'raising temperature',
                      True),
                     ('The heater has broken — no energy is being supplied', False),
                     ('The substance has reached its maximum possible temperature', False),
                     ('The substance is losing heat to the surroundings at exactly the same rate as energy is supplied',
                      False)],
            'q': 'A substance is heated at constant power. Its temperature stays constant for several minutes. What is '
                 'happening?',
            'wrong_explanations': {1: 'If no energy were being supplied, temperature would fall (cool to room '
                                      'temperature) — a constant temperature at the melting/boiling point specifically '
                                      'indicates a change of state.',
                                   2: 'There is no maximum temperature concept for most substances in normal '
                                      'conditions — temperature can always rise further if energy is supplied.',
                                   3: 'While heat loss to surroundings can cause apparent temperature plateaus, in '
                                      'exam context a flat section on a heating curve always indicates a change of '
                                      'state — the temperature is pinned at the melting or boiling point.'}},
           {'opts': [('The swimming pool — despite lower temperature, it has vastly more particles so its total KE + '
                      'PE is much greater',
                      True),
                     ('The cup of tea — higher temperature means more internal energy', False),
                     ('They have the same — internal energy depends only on temperature', False),
                     ('Cannot compare — internal energy requires knowing density as well', False)],
            'q': 'A large cool swimming pool and a small hot cup of tea — which has greater internal energy?',
            'wrong_explanations': {1: 'Higher temperature means higher AVERAGE KE per particle — but internal energy '
                                      'is the TOTAL for all particles. The pool has far more particles, so total '
                                      'internal energy is greater.',
                                   2: 'Internal energy depends on temperature, mass AND specific heat capacity — not '
                                      'temperature alone.',
                                   3: 'Density is relevant to calculating particle numbers but the main point is that '
                                      'internal energy is an EXTENSIVE property — it scales with the amount of '
                                      'matter.'}}],
  'rp': None,
  'spec': '6.3.2.1',
  'summary': 'Define internal energy and explain how heating affects a system.',
  'theory': [{'content': 'INTERNAL ENERGY is the total kinetic energy and potential energy of all the particles in a '
                         'system.\n'
                         '\n'
                         'INTERNAL ENERGY = sum of:\n'
                         'KINETIC ENERGY of particles — from their random motion (vibration, translation, rotation).\n'
                         'POTENTIAL ENERGY of particles — stored in the bonds and intermolecular forces between them.\n'
                         '\n'
                         'When a substance is heated, the energy supplied goes into the internal energy of the '
                         'system.\n'
                         '\n'
                         'This increased internal energy can produce TWO EFFECTS:\n'
                         '1. TEMPERATURE RISE — particles move faster (higher average KE).\n'
                         '2. CHANGE OF STATE — particles gain enough PE to overcome intermolecular forces (bonds '
                         'break/form).\n'
                         '\n'
                         'NOTE: Both effects cannot happen simultaneously for a pure substance at its melting or '
                         'boiling point — during a change of state, temperature stays constant even as energy is '
                         'supplied.',
              'heading': 'What Is Internal Energy?'},
             {'content': 'TEMPERATURE is a measure of the AVERAGE KINETIC ENERGY of the particles.\n'
                         '\n'
                         'Higher temperature = faster-moving particles = higher average KE.\n'
                         'Lower temperature = slower-moving particles = lower average KE.\n'
                         '\n'
                         'At the same temperature:\n'
                         'Different materials have different internal energies because they have different numbers of '
                         'particles and different potential energy arrangements.\n'
                         '\n'
                         'IMPORTANT DISTINCTION:\n'
                         'TEMPERATURE (°C or K) — measures average KE per particle.\n'
                         'THERMAL ENERGY (J) — total energy transferred — depends on temperature difference AND mass '
                         'AND specific heat capacity.\n'
                         '\n'
                         'Example:\n'
                         'A large cool lake and a small hot cup of tea:\n'
                         'The tea is hotter (higher temperature = higher average KE per particle).\n'
                         'But the lake has far greater total internal energy (more particles, more total KE + PE).',
              'heading': 'Temperature and Kinetic Energy'},
             {'content': 'When energy is SUPPLIED to a substance:\n'
                         'EFFECT 1 — TEMPERATURE RISES:\n'
                         'Particles move faster (KE increases).\n'
                         'This happens when no change of state is occurring.\n'
                         'Calculated using ΔE = mcΔθ.\n'
                         '\n'
                         'EFFECT 2 — CHANGE OF STATE:\n'
                         'Temperature stays CONSTANT while state changes.\n'
                         'Energy goes into increasing POTENTIAL ENERGY — breaking intermolecular bonds.\n'
                         'Calculated using E = mL (latent heat equation).\n'
                         '\n'
                         'On a HEATING CURVE (temperature vs time for constant energy input):\n'
                         'Sloping sections: temperature rising (KE increasing).\n'
                         'FLAT sections: change of state occurring (temperature constant, PE increasing).\n'
                         'Flat section during melting = melting point.\n'
                         'Flat section during boiling = boiling point.\n'
                         '\n'
                         'On a COOLING CURVE: the reverse — flat sections at condensation and freezing points.',
              'heading': 'Heating and Cooling — Two Effects'}],
  'title': 'Internal Energy',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Δθ is FINAL minus INITIAL temperature — not the final temperature alone. Heating from 20°C to '
                    '60°C gives Δθ = 40°C, not 60°C. Also convert mass to kg (not grams) before substituting.',
  'equations': ['ΔE = m × c × Δθ'],
  'fifas': [{'label': 'SHC Calculation',
             'question': 'How much energy heats 0.5 kg of water from 20°C to 100°C? (c = 4200 J/kg°C)',
             'steps': [('F', 'ΔE = m × c × Δθ'),
                       ('I', 'm = 0.5 kg, c = 4200, Δθ = 100 − 20 = 80°C'),
                       ('F', 'ΔE = 0.5 × 4200 × 80 = 0.5 × 336,000'),
                       ('A', 'ΔE = 168,000 J (168 kJ)')]}],
  'higher': None,
  'id': 'temperature-changes-shc',
  'key_note': 'SHC (c): J per kg per °C. ΔE = mcΔθ. Water c = 4200 J/kg°C (highest common). Δθ = final − initial. '
              'Rearrange for any unknown. RP14: electric heater method. High SHC of water → radiators, cooling '
              'systems, climate moderation.',
  'matching': {'instruction': 'Match each scenario to the correct energy or temperature change.',
               'pairs': [('504,000 J', '2 kg water, Δθ = 60°C, c = 4200 — ΔE = 2 × 4200 × 60'),
                         ('20°C rise', '54,000 J into 3 kg aluminium (c = 900) — Δθ = 54,000 ÷ 2700'),
                         ('High SHC benefit',
                          'Water used in central heating — carries more thermal energy per kg per °C'),
                         ('Δθ = final − initial', 'Temperature CHANGE — not the final temperature alone')],
               'title': 'SHC Calculations'},
  'quiz': [{'opts': [('135,000 J — ΔE = 2 × 450 × 150 = 135,000 J (Δθ = 200 − 50 = 150°C)', True),
                     ('45,000 J — used final temperature (50°C) not temperature change (150°C)', False),
                     ('180,000 J — used initial temperature (200°C) not temperature change', False),
                     ('900 J — ΔE = c × Δθ (forgot mass)', False)],
            'q': 'A 2 kg iron block (c = 450 J/kg°C) cools from 200°C to 50°C. How much energy is released?',
            'wrong_explanations': {1: 'Δθ = 200 − 50 = 150°C (change, not final). Using 50°C: 2 × 450 × 50 = 45,000 J '
                                      '— wrong Δθ.',
                                   2: 'Using 200°C: 2 × 450 × 200 = 180,000 J — using initial temp, not the change.',
                                   3: 'Must include mass: ΔE = m × c × Δθ = 2 × 450 × 150 = 135,000 J.'}},
           {'opts': [("Water's high SHC (4200 J/kg°C) means it absorbs large amounts of thermal energy per kg per °C — "
                      'effective at cooling without a large temperature rise',
                      True),
                     ('Water has a low SHC — it heats up quickly so it removes heat from the engine faster', False),
                     ('Water is electrically insulating — it prevents short circuits in the engine', False),
                     ('Water has the highest density of any liquid — it flows faster through the cooling system',
                      False)],
            'q': 'Why is water used as the coolant in car engines rather than a cheaper fluid?',
            'wrong_explanations': {1: 'A LOW SHC would mean water heats up quickly and saturates with heat — '
                                      'counterproductive for cooling. HIGH SHC means it can absorb lots of heat before '
                                      'its temperature rises much.',
                                   2: 'Water is a conductor (especially tap water with dissolved ions) — electrical '
                                      'insulation is not the reason.',
                                   3: 'Water is not the densest liquid — mercury is far denser. Flow rate is '
                                      'determined by pump design, not density alone.'}}],
  'rp': 'RP14 (Physics) — Determine SHC of a material: electric heater (E = Pt), thermometer, balance. Rearrange ΔE = '
        'mcΔθ for c. Insulate to reduce heat loss errors.',
  'spec': '6.3.2.2',
  'summary': 'Use ΔE = mcΔθ to calculate energy changes when substances are heated or cooled.',
  'theory': [{'content': 'SPECIFIC HEAT CAPACITY (c) is the amount of energy needed to raise the temperature of 1 kg '
                         'of a substance by 1°C.\n'
                         '\n'
                         'EQUATION:\n'
                         'ΔE = m × c × Δθ\n'
                         '\n'
                         'ΔE = change in thermal energy (J)\n'
                         'm = mass (kg)\n'
                         'c = specific heat capacity (J/kg°C)\n'
                         'Δθ = temperature change (°C)\n'
                         '\n'
                         'Common values:\n'
                         'Water: 4200 J/kg°C — very high\n'
                         'Aluminium: 900 J/kg°C\n'
                         'Iron/steel: 450 J/kg°C\n'
                         'Copper: 385 J/kg°C\n'
                         'Air: ~1000 J/kg°C\n'
                         '\n'
                         'Higher SHC = more energy needed per kg per °C = heats up and cools down more slowly.',
              'heading': 'Specific Heat Capacity'},
             {'content': 'Rearrangements:\n'
                         'Δθ = ΔE ÷ (m × c)\n'
                         'm = ΔE ÷ (c × Δθ)\n'
                         'c = ΔE ÷ (m × Δθ)\n'
                         '\n'
                         'EXAMPLE 1:\n'
                         'Heat 2 kg of water from 20°C to 80°C (c = 4200 J/kg°C):\n'
                         'Δθ = 80 − 20 = 60°C\n'
                         'ΔE = 2 × 4200 × 60 = 504,000 J\n'
                         '\n'
                         'EXAMPLE 2:\n'
                         '54,000 J heats a 3 kg aluminium block (c = 900):\n'
                         'Δθ = 54,000 ÷ (3 × 900) = 54,000 ÷ 2700 = 20°C\n'
                         '\n'
                         'REQUIRED PRACTICAL (RP14):\n'
                         'Heat a known mass using an electric heater.\n'
                         'E = P × t (energy in from heater).\n'
                         'Measure Δθ with a thermometer.\n'
                         'Rearrange ΔE = mcΔθ to find c.\n'
                         'Insulate to reduce heat loss.',
              'heading': 'Using the SHC Equation'},
             {'content': 'WHY WATER IS USED IN HEATING SYSTEMS:\n'
                         'Water has one of the highest SHC values of any common liquid.\n'
                         'Can carry large amounts of thermal energy per kg per °C — efficient heat transfer.\n'
                         'Used in: central heating radiators, car cooling systems, industrial heat exchangers.\n'
                         '\n'
                         'OCEANIC CLIMATE REGULATION:\n'
                         'Oceans have enormous mass of water with high SHC.\n'
                         'Absorb and store huge amounts of solar energy → release slowly.\n'
                         'Coastal areas have milder, more stable temperatures than inland areas.\n'
                         '\n'
                         'COOKING:\n'
                         'Cast iron pans (low SHC ≈ 450 J/kg°C): heat up quickly — responsive.\n'
                         'Ceramic dishes (higher SHC): heat up more slowly but retain heat longer.\n'
                         '\n'
                         'CONSERVATION OF ENERGY IN MIXING:\n'
                         'm₁c₁Δθ₁ = m₂c₂Δθ₂ (energy lost by hot = energy gained by cold, in an insulated system)',
              'heading': 'Applications of Specific Heat Capacity'}],
  'title': 'Temperature Changes and Specific Heat Capacity',
  'triple_only': None,
  'variables': [('ΔE', 'Change in thermal energy', 'joules', 'J'),
                ('m', 'Mass', 'kilograms', 'kg'),
                ('c', 'Specific heat capacity', 'J/kg°C', 'J/kg°C'),
                ('Δθ', 'Temperature change', '°C', '°C')]},
 {'common_mistake': 'During a change of state, temperature does NOT change — the flat sections on a heating curve. E = '
                    'mL has NO temperature change term — unlike ΔE = mcΔθ. Students often confuse the two equations. '
                    'If temperature is changing, use ΔE = mcΔθ. If state is changing (temperature constant), use E = '
                    'mL.',
  'equations': ['E = m × L'],
  'fifas': [{'label': 'Latent Heat — Melting',
             'question': 'Calculate the energy needed to melt 2 kg of ice. (Lf = 334,000 J/kg)',
             'steps': [('F', 'E = m × L'),
                       ('I', 'm = 2 kg, L = 334,000 J/kg'),
                       ('F', 'E = 2 × 334,000'),
                       ('A', 'E = 668,000 J (668 kJ)')]}],
  'higher': None,
  'id': 'specific-latent-heat',
  'key_note': 'E = mL. No temperature change during state change — energy goes into PE (breaking bonds). Fusion: solid '
              '↔ liquid. Vaporisation: liquid ↔ gas. Lv > Lf (more energy to boil than melt). Water Lf = 334 kJ/kg; Lv '
              '= 2260 kJ/kg. Steam burns worse than boiling water — releases latent heat on condensing.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Latent heat of fusion', 'Energy to change 1 kg solid ↔ liquid with NO temperature change'),
                         ('Latent heat of vaporisation',
                          'Energy to change 1 kg liquid ↔ gas with NO temperature change — larger than fusion'),
                         ('E = mL', 'Equation for energy in a change of state — no Δθ term'),
                         ('Why steam burns worse',
                          'Steam releases latent heat of vaporisation on condensing — extra energy on top of cooling'),
                         ('Flat section on heating curve',
                          'Temperature constant during change of state — energy increasing PE, not KE')],
               'title': 'Latent Heat Concepts'},
  'quiz': [{'opts': [('1,130,000 J — E = 0.5 × 2,260,000 = 1,130,000 J', True),
                     ('4,520,000 J — E = 2 × 2,260,000 (used L as mass)', False),
                     ('0 J — no energy change because temperature stays at 100°C', False),
                     ('168,000 J — used SHC equation instead of latent heat', False)],
            'q': 'How much energy is released when 0.5 kg of steam at 100°C condenses to water at 100°C? (Lv = '
                 '2,260,000 J/kg)',
            'wrong_explanations': {1: "E = m × L = 0.5 × 2,260,000. Using 2 for mass gives E = 4,520,000 J — that's "
                                      'for 2 kg, not 0.5 kg.',
                                   2: 'Temperature staying constant does NOT mean no energy change. Energy is released '
                                      'as bonds FORM during condensation — latent heat is released, not absorbed.',
                                   3: 'For a change of state, use E = mL. The SHC equation (ΔE = mcΔθ) applies when '
                                      'TEMPERATURE CHANGES — here temperature is constant.'}},
           {'opts': [('Sweat evaporating absorbs latent heat of vaporisation from the skin — the energy taken from the '
                      'skin during evaporation lowers its temperature',
                      True),
                     ('Sweat is cold — it cools the skin by conduction when applied', False),
                     ('Sweat reflects sunlight — reducing energy absorbed by the skin', False),
                     ('Sweat increases skin density — denser skin conducts heat away faster', False)],
            'q': 'Why does sweating cool the body?',
            'wrong_explanations': {1: 'Sweat is at body temperature (37°C) — it is not cold. The cooling comes from '
                                      'EVAPORATION absorbing latent heat.',
                                   2: "Sweat is transparent — it doesn't reflect significant sunlight.",
                                   3: "Skin density doesn't change meaningfully due to sweat — cooling is entirely an "
                                      'evaporative latent heat effect.'}}],
  'rp': None,
  'spec': '6.3.2.3',
  'summary': 'Define specific latent heat and calculate energy for changes of state using E = mL.',
  'theory': [{'content': 'LATENT HEAT is the energy required to change the state of a substance WITHOUT changing its '
                         'temperature.\n'
                         '\n'
                         'When a substance changes state:\n'
                         'Energy is supplied BUT temperature stays constant.\n'
                         'The energy goes into POTENTIAL ENERGY — breaking or forming intermolecular bonds.\n'
                         'Kinetic energy of particles stays the same → temperature stays the same.\n'
                         '\n'
                         "'Latent' means 'hidden' — the energy is 'hidden' because it doesn't show up as a temperature "
                         'change.\n'
                         '\n'
                         'There are TWO types:\n'
                         'SPECIFIC LATENT HEAT OF FUSION (Lf): energy to change 1 kg of solid → liquid (melting) or '
                         'liquid → solid (freezing).\n'
                         'SPECIFIC LATENT HEAT OF VAPORISATION (Lv): energy to change 1 kg of liquid → gas (boiling) '
                         'or gas → liquid (condensing).\n'
                         '\n'
                         'Lv > Lf for most substances — it takes more energy to fully separate particles (boiling) '
                         'than to just disrupt the lattice (melting).',
              'heading': 'What Is Latent Heat?'},
             {'content': 'EQUATION:\n'
                         'E = m × L\n'
                         '\n'
                         'E = energy for the change of state (J)\n'
                         'm = mass (kg)\n'
                         'L = specific latent heat (J/kg)\n'
                         '\n'
                         'Rearranging:\n'
                         'm = E ÷ L\n'
                         'L = E ÷ m\n'
                         '\n'
                         'Some values:\n'
                         'Water — latent heat of fusion: 334,000 J/kg (334 kJ/kg)\n'
                         'Water — latent heat of vaporisation: 2,260,000 J/kg (2260 kJ/kg)\n'
                         '\n'
                         'Note: vaporisation needs ~7× more energy than fusion for water.\n'
                         '\n'
                         'EXAMPLE 1 — melting:\n'
                         'Energy to melt 0.5 kg of ice (Lf = 334,000 J/kg):\n'
                         'E = 0.5 × 334,000 = 167,000 J\n'
                         '\n'
                         'EXAMPLE 2 — boiling:\n'
                         'Energy to boil away 2 kg of water at 100°C (Lv = 2,260,000 J/kg):\n'
                         'E = 2 × 2,260,000 = 4,520,000 J = 4.52 MJ',
              'heading': 'The Specific Latent Heat Equation'},
             {'content': 'WHY STEAM CAUSES WORSE BURNS THAN BOILING WATER:\n'
                         'Boiling water (100°C) and steam (100°C) are at the same temperature.\n'
                         'But when steam CONDENSES on skin, it releases the latent heat of vaporisation (2,260,000 '
                         'J/kg) IN ADDITION to the heat from cooling.\n'
                         'Steam releases much more energy per kg than liquid water at the same temperature.\n'
                         '\n'
                         'SWEATING AND EVAPORATIVE COOLING:\n'
                         'When sweat evaporates, it absorbs latent heat of vaporisation from the skin.\n'
                         'This cools the body — the energy taken from the skin during evaporation lowers skin '
                         'temperature.\n'
                         'High latent heat of vaporisation of water makes this very effective.\n'
                         '\n'
                         'FREEZING PONDS:\n'
                         'Water releases latent heat of fusion when it freezes → water surrounding fish slowly '
                         'releases energy → pond cools slowly.\n'
                         'This is why ponds freeze from the surface DOWN — the surface loses heat to the cold air '
                         'above.\n'
                         '\n'
                         'HEATING CURVE — FLAT SECTIONS:\n'
                         'Flat at 0°C during melting (fusion). Flat at 100°C during boiling (vaporisation).\n'
                         'Slopes in between = temperature rising using ΔE = mcΔθ.',
              'heading': 'Latent Heat in Context'}],
  'title': 'Changes of State and Specific Latent Heat',
  'triple_only': None,
  'variables': [('E', 'Energy for change of state', 'joules', 'J'),
                ('m', 'Mass', 'kilograms', 'kg'),
                ('L', 'Specific latent heat', 'J/kg', 'J/kg')]},
 {'common_mistake': 'Temperature in gas law calculations MUST be in KELVIN — not Celsius. Add 273 to convert. 0°C = '
                    '273 K, NOT 0 K. Pressure is caused by COLLISIONS of molecules with the walls — not by the weight '
                    'or speed alone, but by the RATE and FORCE of collisions.',
  'equations': ["p × V = constant  (Boyle's Law, constant temperature)",
                'p ÷ T = constant  (constant volume, T in kelvin)',
                'T (K) = T (°C) + 273'],
  'fifas': [{'label': "Boyle's Law",
             'question': 'A gas at 200 kPa occupies 3 m³. The gas is compressed to 1 m³ at constant temperature. '
                         'Calculate the new pressure.',
             'steps': [('F', "p₁V₁ = p₂V₂ (Boyle's Law — constant temperature)"),
                       ('I', 'p₁ = 200 kPa, V₁ = 3 m³, V₂ = 1 m³'),
                       ('F', 'p₂ = p₁V₁ ÷ V₂ = 200 × 3 ÷ 1 = 600'),
                       ('A', 'p₂ = 600 kPa')]}],
  'higher': None,
  'id': 'particle-motion-pressure',
  'key_note': 'Gas pressure: caused by molecular collisions with container walls. Higher T → faster molecules → more '
              'frequent, harder collisions → higher pressure. Smaller V → more frequent collisions → higher pressure. '
              "Boyle's Law: pV = constant. T in kelvin: K = °C + 273. Absolute zero = 0 K = −273°C.",
  'matching': {'instruction': 'Match each change to its effect on gas pressure (assuming everything else stays '
                              'constant).',
               'pairs': [('Pressure increases',
                          'Temperature of gas increases at constant volume — faster molecules, more forceful '
                          'collisions'),
                         ('Pressure increases',
                          'Volume of container decreases at constant temperature — more frequent collisions with '
                          'walls'),
                         ('Pressure decreases',
                          'Temperature of gas decreases at constant volume — slower molecules, less frequent '
                          'collisions'),
                         ('Pressure decreases',
                          'Volume of container increases at constant temperature — molecules travel further between '
                          'collisions')],
               'title': 'Pressure and Particle Motion'},
  'quiz': [{'opts': [('The tyre gets hotter — higher temperature means faster-moving air molecules, more frequent and '
                      'harder collisions with the tyre walls',
                      True),
                     ('Air leaks into the tyre from outside — more molecules means higher pressure', False),
                     ('The tyre volume decreases as the car is driven — smaller volume means higher pressure', False),
                     ('The tyre heats up and the air molecules get larger — more molecules hit the walls', False)],
            'q': 'Why does the pressure inside a tyre increase when a car has been driven for a while?',
            'wrong_explanations': {1: "Air doesn't leak IN to a sealed tyre — if anything, slow leaks go OUT. The "
                                      'pressure rises due to TEMPERATURE increase.',
                                   2: "Tyre volume stays approximately constant while driving (unless there's a "
                                      'puncture). The pressure rises due to TEMPERATURE increase at constant volume.',
                                   3: "Gas molecules don't change size with temperature — they just move FASTER, "
                                      'increasing collision frequency and force.'}},
           {'opts': [('200 kPa — T₁ = 300 K, T₂ = 600 K; pressure doubles as temperature doubles', True),
                     ('1200 kPa — used Celsius values: 327 ÷ 27 × 100', False),
                     ('50 kPa — temperature increased so pressure decreases', False),
                     ("100 kPa — pressure doesn't change with temperature", False)],
            'q': 'A gas is at 27°C and 100 kPa. It is heated to 327°C at constant volume. What is the new pressure?',
            'wrong_explanations': {1: 'Must convert to KELVIN: 27°C = 300 K, 327°C = 600 K. Ratio = 600/300 = 2. Using '
                                      'Celsius: 327/27 ≈ 12 — completely wrong ratio.',
                                   2: 'Pressure INCREASES when temperature increases at constant volume — more '
                                      'energetic collisions, higher pressure.',
                                   3: 'Pressure and temperature (in kelvin) are directly proportional at constant '
                                      'volume — higher temperature = higher pressure.'}}],
  'rp': None,
  'spec': '6.3.3.1',
  'summary': 'Explain gas pressure in terms of particle motion and describe how temperature and volume affect '
             'pressure.',
  'theory': [{'content': 'Gas molecules are in CONSTANT, RANDOM MOTION — moving in all directions at high speeds.\n'
                         '\n'
                         'TEMPERATURE AND KINETIC ENERGY:\n'
                         'The TEMPERATURE of a gas is related to the AVERAGE KINETIC ENERGY of its molecules.\n'
                         'Higher temperature → molecules move FASTER → higher average KE.\n'
                         'Lower temperature → molecules move SLOWER → lower average KE.\n'
                         '\n'
                         'At ABSOLUTE ZERO (0 K = −273°C):\n'
                         'Particles have minimum possible energy — minimum motion.\n'
                         'Kelvin (K) scale: K = °C + 273\n'
                         '\n'
                         'Examples:\n'
                         '0°C = 273 K (freezing point of water)\n'
                         '100°C = 373 K (boiling point of water)\n'
                         '−273°C = 0 K (absolute zero — theoretical minimum)\n'
                         '\n'
                         'The Kelvin scale is the absolute temperature scale — used in gas law calculations.',
              'heading': 'Particle Motion in Gases'},
             {'content': 'GAS PRESSURE is caused by the COLLISIONS of gas molecules with the WALLS of the container.\n'
                         '\n'
                         'Each collision exerts a tiny force on the wall — the total of billions of collisions per '
                         'second creates the measurable pressure.\n'
                         '\n'
                         'Pressure is measured in PASCALS (Pa) or N/m².\n'
                         '1 Pa = 1 N/m².\n'
                         '\n'
                         'FACTORS AFFECTING PRESSURE:\n'
                         '\n'
                         'TEMPERATURE (constant volume):\n'
                         'Higher temperature → molecules move FASTER → MORE FREQUENT collisions with walls → HIGHER '
                         'PRESSURE → MORE FORCEFUL collisions.\n'
                         'At constant volume: pressure is proportional to absolute temperature (Kelvin).\n'
                         '\n'
                         'VOLUME (constant temperature):\n'
                         'Smaller volume → molecules travel LESS DISTANCE between collisions → MORE FREQUENT '
                         'collisions with walls → HIGHER PRESSURE.\n'
                         "At constant temperature: pressure increases when volume decreases (Boyle's Law).",
              'heading': 'Gas Pressure'},
             {'content': "BOYLE'S LAW (constant temperature):\n"
                         'Pressure × Volume = constant\n'
                         'pV = constant\n'
                         'Doubling volume → halves pressure. Halving volume → doubles pressure.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Gas at 100 kPa occupies 2 m³. What pressure when compressed to 0.5 m³?\n'
                         'p₁V₁ = p₂V₂\n'
                         '100 × 2 = p₂ × 0.5\n'
                         'p₂ = 200 ÷ 0.5 = 400 kPa\n'
                         '\n'
                         'PRESSURE–TEMPERATURE LAW (constant volume):\n'
                         'p ÷ T = constant (T in kelvin)\n'
                         'Double absolute temperature → double pressure.\n'
                         '\n'
                         'APPLICATIONS:\n'
                         'TYRES: pressurised air — less volume of air compressed inside → high pressure.\n'
                         'SYRINGES: pushing plunger → smaller volume → higher pressure → liquid/gas pushed out.\n'
                         'AEROSOLS: gas under high pressure pushes liquid out when valve opened.\n'
                         'BIKE PUMP: compressing air into small volume → high pressure → inflates tyre.',
              'heading': 'Pressure, Volume and Temperature Relationships'}],
  'title': 'Particle Motion in Gases',
  'triple_only': None,
  'variables': [('p', 'Pressure', 'pascals', 'Pa'),
                ('V', 'Volume', 'm³', 'm³'),
                ('T', 'Temperature', 'kelvin', 'K'),
                ('Ek', 'Average kinetic energy', 'joules', 'J')]}],

"atomic-structure": [{'common_mistake': 'The nucleus contains protons AND neutrons — NOT electrons. Electrons orbit the nucleus in shells. '
                    'The mass of an atom comes almost entirely from the nucleus (protons + neutrons) — electron mass '
                    'is negligible.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'structure-of-atom',
  'key_note': 'Atom: nucleus (protons + neutrons) + electrons in shells. Proton: +1, mass 1. Neutron: 0, mass 1. '
              'Electron: −1, negligible mass. Protons = electrons in neutral atom. Nuclear radius ≈ 1/10,000 atomic '
              'radius — mostly empty space. Shells: 2, 8, 8...',
  'matching': {'instruction': 'Match each particle to its charge, mass and location.',
               'pairs': [('Proton', 'Charge +1, mass 1 amu, found in the nucleus'),
                         ('Neutron', 'Charge 0, mass 1 amu, found in the nucleus'),
                         ('Electron', 'Charge −1, negligible mass, found in shells around the nucleus'),
                         ('Nucleus',
                          "Contains protons and neutrons — radius ~1/10,000 of the atom — most of atom's mass")],
               'title': 'Subatomic Particles'},
  'quiz': [{'opts': [('In the nucleus — protons and neutrons make up almost all the atomic mass; electrons are '
                      'negligible',
                      True),
                     ('In the electron shells — electrons are the most numerous particles', False),
                     ('Evenly spread throughout the atom — mass is uniformly distributed', False),
                     ('On the outer electron shell — outermost electrons carry most of the mass', False)],
            'q': 'Where is most of the mass of an atom concentrated?',
            'wrong_explanations': {1: 'There are often as many electrons as protons, but each electron weighs ~1/1836 '
                                      'of a proton — their combined mass is negligible.',
                                   2: 'Mass is concentrated in the tiny nucleus — the rest of the atom is mostly empty '
                                      'space.',
                                   3: 'Outer electrons have even less mass than inner ones — all electron mass is '
                                      'negligible.'}},
           {'opts': [('8 — neutral atoms always have equal numbers of protons and electrons', True),
                     ('16 — electrons come in pairs so there are twice as many', False),
                     ('4 — only half the protons are balanced by electrons', False),
                     ('0 — electrons are not part of the neutral atom', False)],
            'q': 'A neutral atom has 8 protons. How many electrons does it have?',
            'wrong_explanations': {1: "Electrons don't automatically pair — the number equals the number of protons "
                                      'for charge balance.',
                                   2: 'Only half the protons balanced would give the atom a net positive charge — '
                                      'neutral means equal numbers.',
                                   3: 'Electrons are an essential part of every atom — removing them creates a '
                                      'positive ion, not a neutral atom.'}}],
  'rp': None,
  'spec': '6.4.1.1',
  'summary': 'Describe the structure of an atom including the nucleus, protons, neutrons and electrons.',
  'theory': [{'content': 'Atoms are extremely small — radius approximately 1 × 10⁻¹⁰ m (0.1 nanometres).\n'
                         '\n'
                         'Structure:\n'
                         'NUCLEUS at the centre — contains PROTONS and NEUTRONS.\n'
                         'ELECTRONS orbit the nucleus at different distances (energy levels/shells).\n'
                         '\n'
                         'The nucleus is tiny compared to the whole atom:\n'
                         'Nuclear radius ≈ 1/10,000 of the atomic radius.\n'
                         'Most of the atom is empty space.\n'
                         '\n'
                         'SIZE COMPARISON:\n'
                         'Atomic radius: ~1 × 10⁻¹⁰ m\n'
                         'Nuclear radius: ~1 × 10⁻¹⁴ m\n'
                         'If the nucleus were the size of a football (30 cm), the atom would be ~3 km across.',
              'heading': 'Inside the Atom'},
             {'content': 'Three subatomic particles:\n'
                         '\n'
                         'PROTON:\n'
                         'Mass: 1 atomic mass unit (amu)\n'
                         'Charge: +1\n'
                         'Location: nucleus\n'
                         '\n'
                         'NEUTRON:\n'
                         'Mass: 1 amu\n'
                         'Charge: 0 (neutral)\n'
                         'Location: nucleus\n'
                         '\n'
                         'ELECTRON:\n'
                         'Mass: approximately 1/1836 amu (negligible)\n'
                         'Charge: −1\n'
                         'Location: shells (energy levels) around the nucleus\n'
                         '\n'
                         'OVERALL CHARGE:\n'
                         'Number of protons = number of electrons in a neutral atom.\n'
                         'Positive protons balanced by negative electrons → atom has no overall charge.\n'
                         '\n'
                         'MASS:\n'
                         'Almost all the mass is in the nucleus (protons + neutrons).\n'
                         'Electron mass is negligible.',
              'heading': 'Properties of Subatomic Particles'},
             {'content': 'Electrons occupy SHELLS (energy levels) at different distances from the nucleus.\n'
                         '\n'
                         'Shells fill from the innermost outwards:\n'
                         'Shell 1 (closest to nucleus): maximum 2 electrons\n'
                         'Shell 2: maximum 8 electrons\n'
                         'Shell 3: maximum 8 electrons (for elements 1–20)\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Hydrogen (1 proton, 1 electron): 1 shell — 1 electron in shell 1\n'
                         'Carbon (6 protons, 6 electrons): 2 shells — 2 in shell 1, 4 in shell 2\n'
                         'Sodium (11 protons, 11 electrons): 3 shells — 2, 8, 1\n'
                         '\n'
                         'ELECTRONS AND CHEMISTRY:\n'
                         "The arrangement of electrons determines an element's chemical properties.\n"
                         'Outer shell electrons are involved in chemical bonding.\n'
                         'Elements in the same group of the periodic table have the same number of outer shell '
                         'electrons.\n'
                         '\n'
                         'When an electron ABSORBS energy it moves to a higher shell (further from nucleus).\n'
                         'When it releases energy it moves to a lower shell — emitting radiation (light or other EM '
                         'waves).',
              'heading': 'Electron Shells and Energy Levels'}],
  'title': 'The Structure of an Atom',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Mass number is protons + NEUTRONS — not protons alone. To find neutrons: subtract atomic number '
                    'FROM mass number. Isotopes have the same atomic number (same element) but different mass numbers '
                    '(different neutron counts).',
  'equations': ['Number of neutrons = mass number − atomic number'],
  'fifas': [{'label': 'Particle Counts',
             'question': 'An atom has nuclear notation ³⁵₁₇Cl. How many protons, neutrons and electrons does it have?',
             'steps': [('F', 'Protons = atomic number (Z); Neutrons = A − Z; Electrons = protons (neutral atom)'),
                       ('I', 'A = 35, Z = 17'),
                       ('F', 'Protons = 17; Neutrons = 35 − 17 = 18; Electrons = 17'),
                       ('A', '17 protons, 18 neutrons, 17 electrons')]}],
  'higher': None,
  'id': 'mass-number-isotopes',
  'key_note': 'Atomic number (Z) = protons. Mass number (A) = protons + neutrons. Neutrons = A − Z. Isotopes: same Z, '
              'different A (different neutron count). Same chemical properties, different physical. Some isotopes '
              'radioactive. Ions: gain/lose electrons — mass number unchanged.',
  'matching': {'instruction': 'Match each nucleus to its correct particle count.',
               'pairs': [('¹²₆C', '6 protons, 6 neutrons, 6 electrons (neutral atom)'),
                         ('²³₁₁Na', '11 protons, 12 neutrons, 11 electrons (neutral atom)'),
                         ('¹⁴C (isotope of ¹²C)', '6 protons, 8 neutrons — same element, different neutron count'),
                         ('Na⁺ ion', '11 protons, 10 electrons — lost 1 electron, charge +1')],
               'title': 'Nuclear Notation'},
  'quiz': [{'opts': [('18 — neutrons = mass number − atomic number = 35 − 17 = 18', True),
                     ('35 — the mass number equals the neutron number', False),
                     ('17 — same as the proton number', False),
                     ('52 — neutrons = mass number + atomic number = 35 + 17', False)],
            'q': 'An atom has 17 protons and mass number 35. How many neutrons does it have?',
            'wrong_explanations': {1: 'Mass number = protons + neutrons. So neutrons = 35 − 17 = 18. The mass number '
                                      'is NOT just neutrons.',
                                   2: 'Neutrons = proton number only when A = 2Z, which is not always the case.',
                                   3: 'Neutrons = A − Z = 35 − 17 = 18, not 35 + 17.'}},
           {'opts': [('Isotopes — same element (same protons), different neutron count (different mass numbers)', True),
                     ('Different elements — different mass numbers mean different elements', False),
                     ('Ions — they have gained or lost electrons', False),
                     ('Allotropes — different structural forms of the same element', False)],
            'q': 'Two atoms have the same atomic number but different mass numbers. What are they?',
            'wrong_explanations': {1: 'ATOMIC NUMBER defines the element — not mass number. Same atomic number = same '
                                      'element = isotopes.',
                                   2: 'Ions differ in electron count — mass number and atomic number are unchanged '
                                      'when ions form.',
                                   3: 'Allotropes (like diamond and graphite) are different structural arrangements of '
                                      'atoms — not related to atomic/mass numbers.'}}],
  'rp': None,
  'spec': '6.4.1.2',
  'summary': 'Define atomic number, mass number and isotopes and interpret nuclear notation.',
  'theory': [{'content': 'ATOMIC NUMBER (Z) = number of PROTONS in the nucleus.\n'
                         'Defines the element — all atoms of the same element have the same atomic number.\n'
                         'In a neutral atom: atomic number = number of electrons.\n'
                         '\n'
                         'MASS NUMBER (A) = total number of PROTONS + NEUTRONS.\n'
                         'Also called nucleon number.\n'
                         'Number of neutrons = mass number − atomic number = A − Z\n'
                         '\n'
                         'NUCLEAR NOTATION:\n'
                         '₍Z₎A X\n'
                         'Where X = element symbol, A = mass number (top), Z = atomic number (bottom).\n'
                         '\n'
                         'EXAMPLES:\n'
                         '¹²₆C — carbon: 6 protons, 6 neutrons, 6 electrons\n'
                         '²³₁₁Na — sodium: 11 protons, 12 neutrons, 11 electrons\n'
                         '²³⁵₉₂U — uranium: 92 protons, 143 neutrons, 92 electrons',
              'heading': 'Atomic Number and Mass Number'},
             {'content': 'ISOTOPES are atoms of the same element with the SAME atomic number but DIFFERENT mass '
                         'numbers.\n'
                         '\n'
                         'Same element → same number of protons.\n'
                         'Different mass numbers → different numbers of NEUTRONS.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Carbon isotopes:\n'
                         '¹²C — 6 protons, 6 neutrons (most common, stable)\n'
                         '¹³C — 6 protons, 7 neutrons (stable, rare)\n'
                         '¹⁴C — 6 protons, 8 neutrons (radioactive — used in carbon dating)\n'
                         '\n'
                         'Hydrogen isotopes:\n'
                         '¹H — 1 proton, 0 neutrons (protium — most common)\n'
                         '²H — 1 proton, 1 neutron (deuterium)\n'
                         '³H — 1 proton, 2 neutrons (tritium — radioactive)\n'
                         '\n'
                         'CHEMICAL PROPERTIES:\n'
                         'Isotopes of the same element have the SAME chemical properties — same electron arrangement.\n'
                         'Physical properties differ slightly (different mass → different density, melting point '
                         'etc.).\n'
                         '\n'
                         'SOME ISOTOPES ARE RADIOACTIVE (unstable nucleus) — they undergo radioactive decay.',
              'heading': 'Isotopes'},
             {'content': 'When atoms GAIN or LOSE electrons they become IONS.\n'
                         '\n'
                         'POSITIVE ION (CATION): loses electrons → more protons than electrons → positive charge.\n'
                         'NEGATIVE ION (ANION): gains electrons → more electrons than protons → negative charge.\n'
                         '\n'
                         'Example:\n'
                         'Sodium atom ²³₁₁Na: 11 protons, 11 electrons — neutral.\n'
                         'Sodium ion Na⁺: 11 protons, 10 electrons — lost 1 electron → charge +1.\n'
                         '\n'
                         'Fluorine atom ¹⁹₉F: 9 protons, 9 electrons — neutral.\n'
                         'Fluoride ion F⁻: 9 protons, 10 electrons — gained 1 electron → charge −1.\n'
                         '\n'
                         'Note: NUCLEAR NOTATION and mass number / atomic number are NOT changed by ion formation — '
                         'only the electron count changes.',
              'heading': 'Ions'}],
  'title': 'Mass Number, Atomic Number and Isotopes',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The alpha scattering experiment DISPROVED the plum pudding model — it did NOT confirm it. The '
                    'fact that MOST particles passed straight through shows atoms are mostly empty space. The FEW that '
                    'bounced back showed the nucleus is small and dense.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'development-atomic-model',
  'key_note': 'Solid sphere → plum pudding (Thomson, electrons discovered) → nuclear model (Rutherford, alpha '
              'scattering). Alpha scattering: most pass through (empty space), few bounce back (small dense positive '
              'nucleus). Bohr: electrons in fixed shells. Chadwick: neutron discovered 1932.',
  'matching': {'instruction': 'Match each model or discovery to the evidence that led to it.',
               'pairs': [('Solid sphere model abandoned',
                          'Discovery of the electron — atoms have internal structure, can be divided'),
                         ('Plum pudding model proposed',
                          'Electrons discovered — atom must be positive sphere with embedded electrons'),
                         ('Plum pudding model disproved',
                          'Alpha particle scattering — few particles bounced back, showing small dense nucleus'),
                         ('Nuclear model accepted',
                          'Most particles pass through (empty space) + few bounce back (small dense positive nucleus)'),
                         ('Electrons in fixed shells',
                          'Bohr model — explains discrete emission spectra and stable electron orbits')],
               'title': 'Atomic Model Timeline'},
  'quiz': [{'opts': [('The atom is mostly empty space — alpha particles encounter nothing to deflect them', True),
                     ('Alpha particles are too fast to be deflected — their speed carries them through', False),
                     ('Gold atoms have no charge — nothing to repel the positive alpha particles', False),
                     ('The gold foil was too thin — a thicker foil would have deflected all particles', False)],
            'q': "In Rutherford's alpha scattering experiment, most alpha particles passed straight through the gold "
                 'foil. What does this tell us?',
            'wrong_explanations': {1: 'Speed could be reduced by using slower particles — the KEY conclusion is about '
                                      'structure, not speed.',
                                   2: 'The FEW particles that DID deflect show gold nuclei ARE positively charged — '
                                      'most pass through the empty space.',
                                   3: 'Thicker foil would increase the probability of deflection, but the fundamental '
                                      'conclusion — mostly empty space — remains.'}},
           {'opts': [('The plum pudding model predicted only small deflections — the large deflections and '
                      'back-scattering showed the positive charge must be concentrated in a tiny nucleus',
                      True),
                     ('The plum pudding model predicted all particles would bounce back — but most passed through',
                      False),
                     ('The plum pudding model had no electrons — but the experiment detected electrons', False),
                     ('The plum pudding model was proposed after the scattering experiment', False)],
            'q': 'Why did the results of alpha scattering disprove the plum pudding model?',
            'wrong_explanations': {1: 'The plum pudding model predicted most particles would PASS THROUGH or have '
                                      'SMALL deflections (spread-out positive charge) — NOT that all would bounce '
                                      'back.',
                                   2: 'The plum pudding model DID include electrons — Thomson discovered them and '
                                      'built them into the model.',
                                   3: "Thomson proposed the plum pudding model in 1904 — BEFORE Rutherford's 1909 "
                                      'scattering experiment.'}}],
  'rp': None,
  'spec': '6.4.1.3',
  'summary': 'Describe how the model of the atom developed from solid sphere to nuclear model.',
  'theory': [{'content': 'Before the late 1800s, atoms were thought to be TINY SOLID SPHERES that could not be divided '
                         '— the smallest possible particles of matter.\n'
                         '\n'
                         "This model had no internal structure — atoms were indivisible 'billiard balls'.\n"
                         '\n'
                         'This model was replaced when ELECTRONS were discovered.\n'
                         '\n'
                         'DISCOVERY OF THE ELECTRON (J.J. Thomson, 1897):\n'
                         'Thomson used cathode rays — beams of particles deflected by electric and magnetic fields.\n'
                         'The particles (electrons) were the same regardless of the cathode material → electrons are '
                         'part of all atoms.\n'
                         'Electrons have negative charge and very small mass.\n'
                         '\n'
                         'This proved atoms CAN be divided — they have internal structure.\n'
                         'The solid sphere model was abandoned.',
              'heading': 'The Solid Sphere Model'},
             {'content': "After Thomson's discovery, he proposed the PLUM PUDDING MODEL:\n"
                         "The atom is a BALL OF POSITIVE CHARGE (the 'pudding').\n"
                         "NEGATIVE ELECTRONS are embedded within it (the 'plums').\n"
                         'The overall charge is neutral.\n'
                         '\n'
                         'This seemed reasonable — it explained that atoms have electrons but are overall neutral.\n'
                         '\n'
                         'However, this model was soon disproved by an important experiment.\n'
                         '\n'
                         "RUTHERFORD'S ALPHA PARTICLE SCATTERING EXPERIMENT (1909, Geiger and Marsden):\n"
                         'Alpha particles fired at a very thin gold foil.\n'
                         'Expected result (plum pudding): all alpha particles would pass straight through or deflect '
                         'only slightly (spread-out positive charge).\n'
                         'Actual result: MOST passed straight through; a SMALL NUMBER deflected through large angles; '
                         'a VERY FEW bounced back almost 180°.\n'
                         '\n'
                         "Rutherford's famous quote: 'It was as if you fired a 15-inch shell at tissue paper and it "
                         "came back and hit you.'",
              'heading': 'The Plum Pudding Model'},
             {'content': 'The scattering results led to the NUCLEAR MODEL (Rutherford, 1911):\n'
                         '\n'
                         'Conclusions from the experiment:\n'
                         'MOST particles passed straight through → atom is MOSTLY EMPTY SPACE.\n'
                         'SOME deflected through large angles → there is a concentrated region of POSITIVE CHARGE.\n'
                         'VERY FEW bounced back → the positive charge is very SMALL and very DENSE.\n'
                         '\n'
                         'The NUCLEAR MODEL:\n'
                         'Small, dense, positively charged NUCLEUS at the centre.\n'
                         'Electrons orbit the nucleus at relatively large distances.\n'
                         'Most of the atom is empty space.\n'
                         '\n'
                         'FURTHER DEVELOPMENTS:\n'
                         "Bohr (1913): electrons orbit in fixed shells (energy levels) — explains why atoms don't "
                         'collapse and why emission spectra have discrete lines.\n'
                         'Chadwick (1932): discovered the NEUTRON — explained why nuclei are heavier than just protons '
                         'alone.\n'
                         '\n'
                         'SCIENCE PRINCIPLE:\n'
                         'New experimental evidence leads to models being changed or replaced.\n'
                         'The atomic model changed as new evidence emerged — showing how science is self-correcting.',
              'heading': 'The Nuclear Model'}],
  'title': 'Development of the Model of the Atom',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Alpha is the MOST ionising but LEAST penetrating. Gamma is the LEAST ionising per path length but '
                    'MOST penetrating. These are often confused. Alpha is most dangerous INSIDE the body; gamma is '
                    'most dangerous OUTSIDE the body.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'radioactive-decay',
  'key_note': 'α: helium nucleus (+2), stopped by paper, most ionising. β: fast electron (−1), stopped by aluminium, '
              'moderate. γ: EM wave (0 charge), needs lead/concrete, least ionising per path. Activity in Bq. Decay is '
              'random. Uses: smoke detectors (α), thickness gauges (β), cancer treatment/sterilisation (γ).',
  'matching': {'instruction': 'Match each radiation type to its composition, penetration and use.',
               'pairs': [('Alpha (α)', 'Helium nucleus — stopped by paper — used in smoke detectors'),
                         ('Beta (β)', 'Fast electron — stopped by aluminium — used in paper thickness monitoring'),
                         ('Gamma (γ)', 'EM wave — needs lead/concrete — used in cancer radiotherapy and sterilisation'),
                         ('Most ionising', 'Alpha radiation — causes most ion pairs per cm of path'),
                         ('Most penetrating',
                          'Gamma radiation — passes through most materials, needs lead/concrete shielding')],
               'title': 'Radiation Properties'},
  'quiz': [{'opts': [('Alpha is highly ionising — it causes dense ionisation damage to nearby cells and cannot escape '
                      'the body to be detected',
                      True),
                     ('Alpha has the highest energy of all three types — more energy means more damage', False),
                     ('Alpha moves fastest — it collides more often with cells', False),
                     ('Alpha is most penetrating — it reaches all organs from a single source', False)],
            'q': 'Why is alpha radiation the most dangerous type when a source is inside the body?',
            'wrong_explanations': {1: 'Alpha does not have the highest energy — gamma photons have very high energies '
                                      'too. The danger is from DENSE IONISATION in a small area.',
                                   2: 'Alpha is actually the SLOWEST of the three — and its high mass means it '
                                      'interacts strongly with matter.',
                                   3: "Alpha is the LEAST penetrating — stopped by a few cm of air. That's exactly why "
                                      "it's so dangerous inside the body — all ionisation is deposited nearby."}},
           {'opts': [('340 nuclei in the source are decaying every second, each emitting radiation', True),
                     ('The source has 340 radioactive atoms remaining in total', False),
                     ('The source emits 340 joules of energy every second', False),
                     ('The source has been decaying for 340 seconds', False)],
            'q': 'A Geiger counter measures 340 Bq from a radioactive source. What does this mean?',
            'wrong_explanations': {1: 'Activity = total number of radioactive atoms remaining, not the rate. Bq '
                                      'measures the RATE of decay (per second).',
                                   2: 'Bq measures rate in decays per second — not joules. Energy per decay is '
                                      'measured in eV or joules, not Bq.',
                                   3: 'Bq is a rate (per second) — not a duration.'}}],
  'rp': None,
  'spec': '6.4.2.1',
  'summary': 'Describe alpha, beta and gamma radiation, their properties and uses and dangers.',
  'theory': [{'content': 'Some atomic nuclei are UNSTABLE — they spontaneously emit radiation to become more stable.\n'
                         'This is RADIOACTIVE DECAY — a RANDOM process (cannot predict exactly when any nucleus will '
                         'decay).\n'
                         '\n'
                         'ACTIVITY: the rate at which a source decays — measured in BECQUEREL (Bq).\n'
                         '1 Bq = 1 decay per second.\n'
                         '\n'
                         'COUNT RATE: decays recorded per second by a detector (e.g. Geiger-Müller tube).\n'
                         '\n'
                         'Three main types of nuclear radiation:\n'
                         'ALPHA (α) — helium nucleus (2 protons + 2 neutrons)\n'
                         'BETA (β) — fast electron from the nucleus\n'
                         'GAMMA (γ) — high-energy electromagnetic wave',
              'heading': 'Radioactive Decay'},
             {'content': 'ALPHA (α):\n'
                         'Composition: 2 protons + 2 neutrons (helium-4 nucleus, ⁴₂He)\n'
                         'Charge: +2\n'
                         'Mass: 4 amu\n'
                         'Range in air: a few centimetres\n'
                         'Penetration: stopped by a few cm of air, or paper, or skin\n'
                         'Ionisation: STRONGLY ionising — causes most damage to nearby cells\n'
                         '\n'
                         'BETA (β):\n'
                         'Composition: fast-moving electron (⁰₋₁e)\n'
                         'Charge: −1\n'
                         'Mass: negligible\n'
                         'Range in air: a few metres\n'
                         'Penetration: stopped by a few mm of aluminium\n'
                         'Ionisation: moderately ionising\n'
                         '\n'
                         'GAMMA (γ):\n'
                         'Composition: high-energy electromagnetic wave (photon)\n'
                         'Charge: 0\n'
                         'Mass: 0\n'
                         'Range in air: effectively unlimited\n'
                         'Penetration: reduced by several cm of lead or metres of concrete\n'
                         'Ionisation: weakly ionising per unit path\n'
                         '\n'
                         'DETECTION: Geiger-Müller tube connected to a counter.',
              'heading': 'Properties of Alpha, Beta and Gamma'},
             {'content': 'USES:\n'
                         'ALPHA — smoke detectors: alpha source ionises air → current flows → alarm triggers when '
                         'smoke absorbs alpha and current drops.\n'
                         'BETA — paper thickness monitoring: beta passes through paper; more absorbed = thicker paper '
                         '→ adjust rollers.\n'
                         'GAMMA — medical imaging (gamma cameras), cancer treatment (radiotherapy), sterilising '
                         'medical equipment, food irradiation.\n'
                         'GAMMA/BETA — industrial thickness gauges, pipeline fault detection.\n'
                         '\n'
                         'DANGERS:\n'
                         'All ionising radiation damages living cells by ionising molecules in DNA → mutations → '
                         'cancer.\n'
                         'HIGH DOSE → cell death → radiation sickness.\n'
                         "ALPHA: most dangerous INSIDE the body (highly ionising, can't escape). Safe outside the body "
                         '(stopped by skin).\n'
                         'GAMMA: most dangerous OUTSIDE the body (penetrates to internal organs). Less ionising per '
                         'path length.\n'
                         'BETA: intermediate — penetrates skin, absorbed by soft tissue.\n'
                         '\n'
                         'PROTECTION:\n'
                         'Distance — inverse square law applies (intensity decreases with distance).\n'
                         'Shielding — appropriate materials (paper for alpha, aluminium for beta, lead for gamma).\n'
                         'Time — minimise exposure duration.\n'
                         'Monitoring — dosimeters worn by radiation workers.',
              'heading': 'Uses and Dangers of Nuclear Radiation'}],
  'title': 'Radioactive Decay and Nuclear Radiation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In beta decay, the MASS NUMBER stays the same — a neutron turns into a proton plus an electron. '
                    'The atomic number INCREASES by 1 (one more proton). Students often think beta decay is like alpha '
                    'and reduces mass number.',
  'equations': ['Alpha decay: A decreases by 4, Z decreases by 2',
                'Beta decay: A unchanged, Z increases by 1',
                'Gamma: no change to A or Z'],
  'fifas': [{'label': 'Alpha Decay Equation',
             'question': 'Write the nuclear equation for alpha decay of ²²⁶₈₈Ra (radium).',
             'steps': [('F', 'Alpha decay: A decreases by 4, Z decreases by 2. Product + ⁴₂He'),
                       ('I', 'A = 226 − 4 = 222; Z = 88 − 2 = 86. Z=86 is radon (Rn)'),
                       ('F', '²²⁶₈₈Ra → ²²²₈₆Rn + ⁴₂He'),
                       ('A', '²²⁶₈₈Ra → ²²²₈₆Rn + ⁴₂He  (check: 226 = 222+4 ✓; 88 = 86+2 ✓)')]}],
  'higher': None,
  'id': 'nuclear-equations',
  'key_note': 'Nuclear equations: mass numbers and atomic numbers must balance on both sides. Alpha (⁴₂He): A−4, Z−2. '
              'Beta (⁰₋₁e): A same, Z+1. Gamma (γ): no change. New element formed in alpha and beta (different Z). '
              'Always verify balance.',
  'matching': {'instruction': 'Match each decay type to the change in mass number and atomic number.',
               'pairs': [('Alpha decay', 'Mass number −4, atomic number −2 — new element two places lower'),
                         ('Beta decay', 'Mass number unchanged, atomic number +1 — new element one place higher'),
                         ('Gamma emission',
                          'No change to mass number or atomic number — same element, energy released'),
                         ('Beta particle', '⁰₋₁e — electron emitted from nucleus when neutron converts to proton')],
               'title': 'Nuclear Equation Changes'},
  'quiz': [{'opts': [('²³⁴₉₁Pa (protactinium) — mass number unchanged, atomic number increases by 1', True),
                     ('²³⁰₈₈Ra (radium) — mass number decreases by 4, atomic number decreases by 2', False),
                     ('²³⁴₈₉Ac (actinium) — atomic number decreases by 1', False),
                     ('²³⁸₉₂U (uranium) — mass number increases', False)],
            'q': 'Thorium-234 (²³⁴₉₀Th) undergoes beta decay. What is the daughter nucleus?',
            'wrong_explanations': {1: 'That describes ALPHA decay (A−4, Z−2) — not beta decay.',
                                   2: 'Beta decay INCREASES atomic number by 1 — not decreases it.',
                                   3: "Beta decay doesn't increase mass number — it is always unchanged. Z goes from "
                                      '90 to 91.'}},
           {'opts': [('234 — 238 − 4 = 234 (alpha carries away mass number 4)', True),
                     ('236 — 238 − 2 = 236 (subtracting atomic number instead of mass number)', False),
                     ('242 — 238 + 4 = 242 (added instead of subtracted)', False),
                     ("238 — mass number doesn't change in alpha decay", False)],
            'q': 'In a nuclear equation, the mass numbers on both sides must balance. A nucleus of ²³⁸₉₂U emits an '
                 'alpha particle. What is the mass number of the daughter nucleus?',
            'wrong_explanations': {1: 'The 2 from the atomic number change is subtracted from the bottom number — '
                                      'alpha takes away mass number 4 and atomic number 2.',
                                   2: 'Mass number cannot increase in alpha decay — the alpha particle carries 4 units '
                                      'of mass number away.',
                                   3: 'Mass number DOES change in alpha decay — it decreases by 4.'}}],
  'rp': None,
  'spec': '6.4.2.2',
  'summary': 'Write and balance nuclear equations for alpha and beta decay.',
  'theory': [{'content': 'Nuclear equations show radioactive decay using nuclear notation.\n'
                         '\n'
                         'Rules for BALANCING nuclear equations:\n'
                         'MASS NUMBERS must balance — top numbers sum the same on both sides.\n'
                         'ATOMIC NUMBERS must balance — bottom numbers sum the same on both sides.\n'
                         '\n'
                         'ALPHA PARTICLE symbol: ⁴₂He (or ⁴₂α)\n'
                         'BETA PARTICLE symbol: ⁰₋₁e (or ⁰₋₁β)\n'
                         'GAMMA RAY: represented by γ — no change to mass or atomic number\n'
                         '\n'
                         'Alpha decay:\n'
                         'Parent nucleus → daughter nucleus + alpha particle\n'
                         'Mass number decreases by 4. Atomic number decreases by 2.\n'
                         '\n'
                         'Beta decay:\n'
                         'Parent nucleus → daughter nucleus + beta particle\n'
                         'A neutron becomes a proton + electron: ¹₀n → ¹₁p + ⁰₋₁e\n'
                         'Mass number unchanged. Atomic number increases by 1.',
              'heading': 'Writing Nuclear Equations'},
             {'content': 'ALPHA DECAY EXAMPLE:\n'
                         'Radium-226 decays by alpha emission:\n'
                         '²²⁶₈₈Ra → ²²²₈₆Rn + ⁴₂He\n'
                         'Check: mass numbers: 226 = 222 + 4 ✓\n'
                         'Atomic numbers: 88 = 86 + 2 ✓\n'
                         'Radium (88) → Radon (86) — atomic number decreases by 2, so element changes.\n'
                         '\n'
                         'BETA DECAY EXAMPLE:\n'
                         'Carbon-14 decays by beta emission:\n'
                         '¹⁴₆C → ¹⁴₇N + ⁰₋₁e\n'
                         'Check: mass numbers: 14 = 14 + 0 ✓\n'
                         'Atomic numbers: 6 = 7 + (−1) ✓\n'
                         'Carbon (6) → Nitrogen (7) — atomic number increases by 1.\n'
                         '\n'
                         'GAMMA EMISSION:\n'
                         'Often follows alpha or beta decay — nucleus releases excess energy as gamma ray.\n'
                         'No change to mass number or atomic number.\n'
                         'No separate nuclear equation needed — just add + γ.',
              'heading': 'Alpha and Beta Decay Examples'},
             {'content': 'ALPHA DECAY:\n'
                         'Mass number: decreases by 4\n'
                         'Atomic number: decreases by 2\n'
                         'Result: new element (two places lower in periodic table)\n'
                         '\n'
                         'BETA DECAY:\n'
                         'Mass number: unchanged (a neutron converts to a proton + electron)\n'
                         'Atomic number: increases by 1\n'
                         'Result: new element (one place higher in periodic table)\n'
                         '\n'
                         'GAMMA EMISSION:\n'
                         'Mass number: unchanged\n'
                         'Atomic number: unchanged\n'
                         'Result: same element, just releases energy\n'
                         '\n'
                         'PATTERN TO REMEMBER:\n'
                         'Alpha → lose 4 mass, lose 2 charge\n'
                         'Beta → same mass, gain 1 charge\n'
                         'Gamma → no change to nucleus\n'
                         '\n'
                         'EXAM STRATEGY:\n'
                         'Always check both mass AND atomic numbers balance.\n'
                         'Use the periodic table to identify the daughter element from its new atomic number.',
              'heading': 'Effect on the Nucleus'}],
  'title': 'Nuclear Equations',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'After each half-life, the activity halves AGAIN from its current value — not from the original. '
                    'After 3 half-lives starting at 1000 Bq: 500 → 250 → 125 Bq. Also: background radiation must be '
                    'subtracted before half-life calculations.',
  'equations': ['After n half-lives: fraction remaining = (½)ⁿ'],
  'fifas': [{'label': 'Half-Life Calculation',
             'question': 'A source has initial activity 960 Bq. Its half-life is 3 hours. What is the activity after '
                         '12 hours?',
             'steps': [('F', 'Number of half-lives = total time ÷ half-life; remaining = initial × (½)ⁿ'),
                       ('I', 'n = 12 ÷ 3 = 4 half-lives'),
                       ('F', '960 × (½)⁴ = 960 × 1/16 = 960 ÷ 16'),
                       ('A', 'Activity = 60 Bq')]}],
  'higher': None,
  'id': 'half-lives',
  'key_note': 'Half-life: time for activity (or nuclei count) to halve. Constant for a given isotope. Random decay — '
              "can't predict individual nucleus. After n half-lives: (½)ⁿ remains. Decay curve: exponential fall. "
              'Background radiation must be subtracted. Medical tracers need short half-lives; carbon dating uses '
              '5730-year ¹⁴C half-life.',
  'matching': {'instruction': 'Match each scenario to the correct remaining activity.',
               'pairs': [('400 Bq', 'Initial activity 1600 Bq, after 2 half-lives: 1600 → 800 → 400'),
                         ('125 Bq', 'Initial activity 1000 Bq, after 3 half-lives: 1000 → 500 → 250 → 125'),
                         ('Longer half-life needed',
                          'Carbon dating — need isotope with half-life comparable to age of sample (thousands of '
                          'years)'),
                         ('Shorter half-life needed',
                          'Medical tracer — activity must fall quickly to reduce patient radiation dose')],
               'title': 'Half-Life Calculations'},
  'quiz': [{'opts': [('80 Bq — 12 ÷ 4 = 3 half-lives; 640 → 320 → 160 → 80 Bq', True),
                     ('160 Bq — only 2 half-lives calculated (8 hours, not 12)', False),
                     ('320 Bq — only 1 half-life applied', False),
                     ('0 Bq — the source has fully decayed after 12 hours', False)],
            'q': 'A radioactive source has a half-life of 4 hours and initial activity 640 Bq. What is the activity '
                 'after 12 hours?',
            'wrong_explanations': {1: '12 ÷ 4 = 3 half-lives. After 2: 640 → 320 → 160 (only 8 hours). After 3: → 80 '
                                      'Bq.',
                                   2: 'After 1 half-life (4 h): 640 → 320. After 2 (8 h): → 160. After 3 (12 h): → 80.',
                                   3: 'Radioactive sources never fully reach zero — activity halves each half-life but '
                                      'never reaches exactly zero (exponential decay).'}},
           {'opts': [('It always takes the same time for the activity to halve, regardless of temperature, pressure or '
                      'how much has already decayed',
                      True),
                     ("It stays constant because the number of atoms in the sample doesn't change", False),
                     ('It is constant because decay rate increases to compensate as fewer atoms remain', False),
                     ('It is constant only at room temperature — at high temperatures the half-life changes', False)],
            'q': "Why is the half-life of a radioactive isotope described as a 'constant'?",
            'wrong_explanations': {1: 'The number of undecayed atoms DOES decrease — but the proportion that decay per '
                                      'unit time stays fixed, so the time to halve is always the same.',
                                   2: 'If rate increased to compensate, activity would stay constant — but it falls '
                                      'exponentially, halving each half-life.',
                                   3: 'Half-life is independent of temperature, pressure, or chemical state — this is '
                                      'one of the key properties of radioactive decay.'}}],
  'rp': None,
  'spec': '6.4.2.3',
  'summary': 'Define half-life, calculate remaining activity and explain the random nature of decay.',
  'theory': [{'content': 'Radioactive decay is a RANDOM PROCESS:\n'
                         'It is impossible to predict exactly WHEN any individual nucleus will decay.\n'
                         'It is impossible to predict WHICH nucleus in a sample will decay next.\n'
                         'Decay is spontaneous — NOT triggered by temperature, pressure or chemical state.\n'
                         '\n'
                         'However, for a LARGE SAMPLE:\n'
                         'We can predict the PROPORTION that will decay in a given time.\n'
                         'Statistical behaviour becomes predictable even though individual decays are random.\n'
                         '\n'
                         'This is similar to flipping a large number of coins — we cannot predict any individual flip, '
                         'but we can confidently predict about 50% will be heads.\n'
                         '\n'
                         'ACTIVITY decreases over time as the number of unstable nuclei falls.',
              'heading': 'Radioactive Decay Is Random'},
             {'content': 'The HALF-LIFE of a radioactive isotope is the time for:\n'
                         'The number of UNDECAYED NUCLEI to halve, OR\n'
                         'The ACTIVITY (or count rate) of the source to halve.\n'
                         '\n'
                         "Half-life is CONSTANT for a given isotope — it doesn't change.\n"
                         '\n'
                         'EXAMPLES:\n'
                         'Carbon-14: half-life ~5730 years (used in carbon dating)\n'
                         'Iodine-131: half-life ~8 days (medical uses — short enough to leave the body)\n'
                         'Uranium-238: half-life ~4.5 billion years\n'
                         'Radon-222: half-life ~3.8 days\n'
                         '\n'
                         'CALCULATING REMAINING ACTIVITY/NUCLEI:\n'
                         'After 1 half-life: ½ remains\n'
                         'After 2 half-lives: ¼ remains\n'
                         'After 3 half-lives: ⅛ remains\n'
                         'After n half-lives: (½)ⁿ remains\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Source starts at 800 Bq. Half-life = 2 hours. What is the activity after 6 hours?\n'
                         '6 hours ÷ 2 hours = 3 half-lives\n'
                         '800 → 400 → 200 → 100 Bq',
              'heading': 'Half-Life'},
             {'content': 'DECAY CURVE:\n'
                         'Graph of activity (or count rate) against time.\n'
                         'Curve starts high and decreases exponentially.\n'
                         'To find half-life from graph: find initial activity, halve it, read off time → then verify '
                         'the next halving takes the same time.\n'
                         '\n'
                         'PRACTICAL SELECTION of isotopes:\n'
                         'MEDICAL TRACERS: short half-life needed — activity falls quickly so patient receives minimal '
                         'long-term dose. Technetium-99m: 6 hours.\n'
                         'CANCER TREATMENT: short enough to deliver dose in treatment window, then decay away.\n'
                         'CARBON DATING: 14C half-life ~5730 years — compares ¹⁴C/¹²C ratio of living things vs '
                         'sample.\n'
                         'NUCLEAR WASTE: long half-life isotopes are the biggest storage problem — some remain '
                         'dangerous for thousands of years.\n'
                         '\n'
                         'BACKGROUND RADIATION:\n'
                         'All measurements of radioactive sources include BACKGROUND RADIATION — radiation from '
                         'natural sources (rocks, cosmic rays, radon gas, food).\n'
                         'Background must be measured and SUBTRACTED from readings.',
              'heading': 'Uses of Half-Life and Decay Curves'}],
  'title': 'Half-Lives and Radioactive Decay',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Contamination and irradiation are NOT the same. Contamination: radioactive material on/in you — '
                    'source travels with you. Irradiation: external source — exposure stops when you move away. Alpha '
                    'is most dangerous as INTERNAL contaminant (highly ionising, short range → all energy deposits '
                    'locally).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'radioactive-contamination',
  'key_note': 'Contamination: source deposits on/in person — ongoing. Irradiation: external exposure — stops when away '
              'from source. Alpha most dangerous internally. Gamma most dangerous externally. Precautions: tongs, '
              'shielding, distance, dosimeters, sealed containers, ventilation. Benefits vs risks must be balanced.',
  'matching': {'instruction': 'Sort each scenario into contamination or irradiation.',
               'pairs': [('Contamination', 'Breathing in radioactive dust — source is now inside the body'),
                         ('Contamination', 'Radioactive material spilled on skin — source remains in contact'),
                         ('Irradiation', 'Standing near a gamma source — move away and exposure stops'),
                         ('Irradiation', 'Medical X-ray — brief external exposure, no source deposited'),
                         ('Most dangerous internally',
                          'Alpha radiation — highly ionising, short range, deposits all energy nearby')],
               'title': 'Contamination vs Irradiation'},
  'quiz': [{'opts': [('Alpha is highly ionising — inside the body all the ionising energy is deposited in nearby lung '
                      'tissue, causing severe local damage',
                      True),
                     ('Alpha travels far inside the body reaching all organs — more widespread damage', False),
                     ('Alpha is easily exhaled — it escapes before causing harm', False),
                     ('Alpha inside the body becomes beta radiation — which is more penetrating', False)],
            'q': 'A worker accidentally inhales radioactive dust containing an alpha emitter. Why is this particularly '
                 'dangerous?',
            'wrong_explanations': {1: "Alpha has very SHORT range — it doesn't travel far. That's exactly the problem: "
                                      'all its energy is deposited locally in lung tissue.',
                                   2: 'Radioactive dust lodges in lung tissue and continues to emit radiation there — '
                                      "it doesn't simply get exhaled.",
                                   3: "Radiation types don't change — alpha always remains alpha. Different isotopes "
                                      "emit different types, but the type doesn't transform."}},
           {'opts': [('Leaving the room while the X-ray is taken — distance and a lead-lined wall reduces irradiation '
                      'when not needed',
                      True),
                     ('Wearing a lead apron while staying in the room — lead blocks all radiation types', False),
                     ('Taking fewer breaths during the X-ray — radiation enters through breathing', False),
                     ('Washing hands after each X-ray — removes radiation from skin', False)],
            'q': 'A radiographer takes X-rays of patients all day. Which precaution best reduces their radiation dose?',
            'wrong_explanations': {1: 'A lead apron is useful protection but does not cover all body parts — leaving '
                                      'the room is more effective for reducing total dose.',
                                   2: 'X-rays are electromagnetic radiation — they are not inhaled. The concern is '
                                      'external irradiation, not contamination.',
                                   3: "X-rays from the machine don't contaminate surfaces — the radiographer's dose "
                                      'comes from irradiation (external source), not contamination.'}}],
  'rp': None,
  'spec': '6.4.2.4',
  'summary': 'Distinguish contamination from irradiation and explain the hazards and precautions for each.',
  'theory': [{'content': 'These two terms are often confused but describe very different situations:\n'
                         '\n'
                         'RADIOACTIVE CONTAMINATION:\n'
                         'Unwanted radioactive material is DEPOSITED ON or INSIDE a person or object.\n'
                         'The contaminating material continues to emit radiation over time.\n'
                         'The source stays with the person/object — ongoing exposure.\n'
                         'Example: breathing in radon gas; swallowing radioactive dust; radioactive material on skin.\n'
                         '\n'
                         'IRRADIATION:\n'
                         'The person or object is EXPOSED TO RADIATION from a source that is NOT attached to them.\n'
                         'When the person moves away from the source, exposure stops.\n'
                         'Example: standing near a radioactive source; medical X-ray; radiotherapy.\n'
                         '\n'
                         'KEY DIFFERENCE:\n'
                         'Contamination = source stays with you.\n'
                         'Irradiation = source is external, exposure ends when you move away.',
              'heading': 'Contamination vs Irradiation'},
             {'content': 'CONTAMINATION HAZARDS:\n'
                         'Alpha sources are especially dangerous as INTERNAL CONTAMINANTS:\n'
                         'Alpha particles are highly ionising but very short range.\n'
                         'Inside the body they deposit all their energy in nearby cells → severe local tissue damage.\n'
                         'External alpha contamination (on skin) is less dangerous — alpha cannot penetrate skin.\n'
                         'Beta and gamma internal contamination is also serious — penetrate to internal organs.\n'
                         '\n'
                         'IRRADIATION HAZARDS:\n'
                         'Depends on radiation type, dose and duration.\n'
                         'Gamma is most dangerous external source — penetrates deeply into tissue.\n'
                         'Alpha from external source: stopped by skin, relatively safe.\n'
                         'Beta: penetrates skin, can damage underlying tissue.\n'
                         '\n'
                         'LONG-TERM EFFECTS:\n'
                         'Ionising radiation damages DNA → mutations → increased cancer risk.\n'
                         'High acute doses → radiation sickness, cell death.\n'
                         'Eyes, bone marrow and gonads particularly sensitive.',
              'heading': 'Hazards of Each Type'},
             {'content': 'PRECAUTIONS TO PREVENT CONTAMINATION:\n'
                         'Never touch radioactive materials directly — use TONGS or remote handling.\n'
                         'Wear PROTECTIVE CLOTHING (gloves, lab coat) to prevent skin contact.\n'
                         'WORK IN WELL-VENTILATED areas to prevent inhaling radioactive dust or gases.\n'
                         'No eating, drinking or applying make-up in radioactive areas — prevents ingestion.\n'
                         'Seal radioactive materials in appropriate containers.\n'
                         '\n'
                         'PRECAUTIONS TO REDUCE IRRADIATION:\n'
                         'DISTANCE — intensity follows inverse square law; doubling distance reduces dose by ¾.\n'
                         'SHIELDING — appropriate material (paper for alpha, aluminium for beta, lead/concrete for '
                         'gamma).\n'
                         'TIME — minimise exposure duration.\n'
                         'DOSIMETERS — worn by radiation workers to monitor cumulative dose.\n'
                         '\n'
                         'PROFESSIONAL GUIDELINES:\n'
                         'Radiation workers have annual dose limits.\n'
                         'Regular monitoring of workplace radiation levels.\n'
                         'Storage of radioactive sources in lead-lined containers when not in use.\n'
                         '\n'
                         'BENEFITS vs RISKS:\n'
                         'Medical uses (X-rays, radiotherapy, tracers) involve balancing dose risk vs '
                         'diagnostic/treatment benefit.\n'
                         'Risk is managed, not eliminated.',
              'heading': 'Precautions and Safe Use'}],
  'title': 'Radioactive Contamination',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Background radiation must be SUBTRACTED before any half-life calculations. Using the uncorrected '
                    'count rate gives a half-life that appears longer than the true value because the count rate never '
                    'falls to zero. Background should be measured BEFORE introducing any source.',
  'equations': ['Corrected count rate = measured count rate − background count rate'],
  'fifas': [],
  'higher': None,
  'id': 'background-radiation',
  'key_note': 'Background radiation: always present from natural (radon ~50%, cosmic, food, ground) and artificial '
              '(medical, nuclear) sources. Must subtract from measurements. Corrected count rate = measured − '
              'background. Dose in sieverts. UK average ~2.7 mSv/year. Radon main natural source — highest in granite '
              'areas.',
  'matching': {'instruction': 'Match each source to its approximate contribution to UK background radiation.',
               'pairs': [('Radon gas', '~50% of UK background — seeps from uranium in rocks into buildings'),
                         ('Cosmic rays', '~10% — high-energy particles from space, more at altitude'),
                         ('Medical sources', '~15% of total — X-rays, CT scans, nuclear medicine'),
                         ('Correcting for background',
                          'Subtract background count rate from measured rate before calculating activity')],
               'title': 'Sources of Background Radiation'},
  'quiz': [{'opts': [('300 counts/min — corrected = 320 − 20 = 300 counts/min', True),
                     ('340 counts/min — 320 + 20 = 340 (added instead of subtracted)', False),
                     ('320 counts/min — background is too small to affect the measurement', False),
                     ('16 counts/min — 320 ÷ 20 = 16', False)],
            'q': 'Background count rate is 20 counts/min. With a source present, the detector reads 320 counts/min. '
                 'What is the corrected activity of the source?',
            'wrong_explanations': {1: 'Background must be SUBTRACTED, not added — adding would overestimate the source '
                                      'activity.',
                                   2: 'Background should always be corrected for, however small — accurate '
                                      'measurements require it.',
                                   3: 'Dividing has no physical meaning here — background is subtracted: 320 − 20 = '
                                      '300.'}},
           {'opts': [('To establish the baseline radiation level so it can be subtracted from measurements — giving '
                      'the true activity of the source alone',
                      True),
                     ('To check the Geiger counter is working correctly before the experiment begins', False),
                     ('To calibrate the counter to zero — resetting it before use', False),
                     ('To measure the half-life of the background radiation', False)],
            'q': 'Why is the background count rate measured before a radioactive source is introduced in an '
                 'experiment?',
            'wrong_explanations': {1: 'Checking equipment is good practice but not the specific reason for measuring '
                                      'background — the purpose is subtraction for accurate source measurement.',
                                   2: "Geiger counters don't need resetting to zero — they count ionisation events "
                                      'regardless.',
                                   3: 'Background radiation has no measurable half-life — it comes from many '
                                      'continuously replenished sources.'}}],
  'rp': None,
  'spec': '6.4.3 (physics only)',
  'summary': 'Describe sources of background radiation and explain why it must be considered in measurements.',
  'theory': [{'content': 'BACKGROUND RADIATION is low-level ionising radiation that is present everywhere in the '
                         'environment at all times — from natural and artificial sources.\n'
                         '\n'
                         'It is always present — even when no radioactive source is in the lab.\n'
                         '\n'
                         'SOURCES OF BACKGROUND RADIATION:\n'
                         '\n'
                         'NATURAL SOURCES (~85% of total in UK):\n'
                         'RADON GAS (~50%): naturally occurring radioactive gas from uranium in rocks. Seeps into '
                         'buildings. Major health risk in granite areas (e.g. Cornwall).\n'
                         'GAMMA RAYS FROM GROUND AND BUILDINGS (~15%): radioactive isotopes in rocks (granite) and '
                         'building materials.\n'
                         'COSMIC RAYS (~10%): high-energy particles from space. More at high altitude (pilots receive '
                         'more).\n'
                         'FOOD AND DRINK (~10%): small amounts of naturally occurring radioactive isotopes (e.g. ¹⁴C, '
                         '⁴⁰K).\n'
                         '\n'
                         'ARTIFICIAL SOURCES (~15% of total):\n'
                         'MEDICAL: X-rays, CT scans, nuclear medicine.\n'
                         'NUCLEAR INDUSTRY: small amounts from nuclear power stations and waste.\n'
                         'NUCLEAR WEAPONS TESTING: historical fallout still present.',
              'heading': 'What Is Background Radiation?'},
             {'content': 'WHY IT MATTERS FOR EXPERIMENTS:\n'
                         'All measurements of radioactive sources include background radiation.\n'
                         'If not corrected, measured activity appears higher than the true source activity.\n'
                         '\n'
                         'CORRECTING FOR BACKGROUND:\n'
                         '1. Measure the count rate without any source present (background count rate).\n'
                         '2. Measure the count rate with the source present.\n'
                         '3. Subtract background: corrected count rate = measured count rate − background count rate.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Background count rate: 25 counts per minute.\n'
                         'Measured count rate with source: 175 counts per minute.\n'
                         'Corrected count rate from source: 175 − 25 = 150 counts per minute.\n'
                         '\n'
                         'This correction is important for accurate half-life calculations and activity measurements.\n'
                         '\n'
                         'VARIATION IN BACKGROUND:\n'
                         'Background radiation varies from place to place (geology, altitude).\n'
                         'Background radiation varies slightly over time (cosmic ray intensity fluctuates).\n'
                         'The count rate of the background should be measured over a long time period and averaged.',
              'heading': 'Measuring and Correcting for Background'},
             {'content': 'RADIATION DOSE is measured in SIEVERTS (Sv) or millisieverts (mSv).\n'
                         'The dose accounts for both the amount of radiation and its biological effect.\n'
                         '\n'
                         'UK AVERAGE ANNUAL DOSE: approximately 2.7 mSv.\n'
                         'Majority from radon gas and medical procedures.\n'
                         '\n'
                         'FACTORS AFFECTING PERSONAL DOSE:\n'
                         'Location: granite areas → more radon → higher dose.\n'
                         'Occupation: pilots, astronauts, nuclear workers → higher doses.\n'
                         'Medical procedures: X-rays, CT scans add to dose.\n'
                         'Altitude: more cosmic radiation at high altitude.\n'
                         '\n'
                         'RADON GAS RISK:\n'
                         'Radon decays in lungs → alpha particles emitted → highly ionising → increases lung cancer '
                         'risk.\n'
                         'Ventilating buildings in high-radon areas reduces exposure.\n'
                         'Radon test kits available for homes in affected areas.\n'
                         '\n'
                         'BENEFIT vs RISK:\n'
                         'Medical uses (imaging, treatment) involve weighing the benefit of diagnosis/treatment '
                         'against radiation dose risk.\n'
                         'Regulated exposure limits protect workers.',
              'heading': 'Health Risks and Radiation Dose'}],
  'title': 'Background Radiation',
  'triple_only': 'Background radiation (physics only) — not in Combined Science as a separate topic.',
  'variables': []},
 {'common_mistake': 'Beta is used for THICKNESS monitoring — not alpha or gamma. Alpha is used for SMOKE detectors — '
                    'not beta or gamma. Gamma is used for DEEP medical imaging and radiotherapy — because it '
                    'penetrates to internal organs. Medical tracers need SHORT half-lives to minimise patient dose.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'uses-of-nuclear-radiation',
  'key_note': 'Alpha: smoke detectors (ionises air, short range). Beta: thickness gauges (absorbed proportional to '
              'thickness). Gamma: radiotherapy, medical tracers, sterilisation, pipeline testing (most penetrating). '
              'Medical tracers: gamma + short half-life (Tc-99m, 6 hours). Selection based on penetration, ionisation '
              'and half-life.',
  'matching': {'instruction': 'Match each use to the radiation type and reason it is chosen.',
               'pairs': [('Smoke detector',
                          'Alpha — ionises air between electrodes; smoke absorbs alpha → current drops → alarm'),
                         ('Paper thickness gauge',
                          'Beta — absorbed proportional to thickness; gamma too penetrating; alpha too weak'),
                         ('Medical tracer (organ imaging)',
                          'Gamma — penetrates body to reach detector outside; short half-life minimises dose'),
                         ('Radiotherapy',
                          'Gamma — penetrates to deep tumour; multiple beams cross at tumour to concentrate dose')],
               'title': 'Radiation Uses'},
  'quiz': [{'opts': [('Alpha ionises air very effectively between the electrodes AND has short range — it stays safely '
                      'inside the casing without penetrating the housing',
                      True),
                     ('Alpha is less dangerous than gamma — so it is safer for household use in general', False),
                     ('Gamma cannot ionise air — only alpha radiation can ionise gases', False),
                     ('Alpha has a longer half-life than gamma emitters — so the detector lasts longer', False)],
            'q': 'Why is americium-241 (an alpha emitter) used in smoke detectors rather than a gamma emitter?',
            'wrong_explanations': {1: 'Safety is part of it — but the specific reasons are HIGH IONISATION (needed to '
                                      "create the ion current) and SHORT RANGE (safe containment). Simply being 'less "
                                      "dangerous' isn't precise enough.",
                                   2: 'Gamma CAN ionise air — all types of ionising radiation can ionise air, but '
                                      'alpha is much MORE efficient per unit path.',
                                   3: 'Half-life of Am-241 is ~432 years — it does last well in detectors, but the '
                                      'primary reason for alpha selection is ionisation efficiency and range, not '
                                      'half-life.'}},
           {'opts': [('Gamma penetrates the body to reach an external detector, and short half-life means patient dose '
                      'is minimal — activity falls quickly after the procedure',
                      True),
                     ('Gamma is most ionising — causes maximum contrast in the image, and short half-life means it '
                      'works faster',
                      False),
                     ('Gamma is the safest radiation type, so combining with any half-life gives safe imaging', False),
                     ('Short half-life means the tracer stays in the body longer before decaying', False)],
            'q': 'A medical tracer needs to emit gamma radiation and have a short half-life. Why?',
            'wrong_explanations': {1: 'Gamma is LEAST ionising per path — less immediate local tissue damage. High '
                                      'ionisation would cause cell damage, not contrast.',
                                   2: "Gamma penetrates body safely — but 'safest' oversimplifies. The combination of "
                                      'penetration (for imaging) AND short half-life (for low dose) is the key.',
                                   3: 'Short half-life means the tracer DECAYS QUICKLY — activity falls rapidly, '
                                      "reducing the patient's radiation dose."}}],
  'rp': None,
  'spec': '6.4.4 (physics only)',
  'summary': 'Describe the uses of alpha, beta and gamma radiation in medicine and industry.',
  'theory': [{'content': 'CANCER TREATMENT (RADIOTHERAPY):\n'
                         'Gamma rays from cobalt-60 focused on tumour from multiple directions.\n'
                         'Crossing beams concentrate dose at tumour — minimise dose to surrounding healthy tissue.\n'
                         'Kills cancer cells by damaging DNA.\n'
                         'Gamma used because it penetrates deeply enough to reach internal tumours.\n'
                         '\n'
                         'MEDICAL TRACERS:\n'
                         'A gamma-emitting radioisotope injected into patient.\n'
                         'Gamma camera detects distribution of the tracer in the body.\n'
                         'Reveals function of organs (not just structure like X-rays).\n'
                         'Technetium-99m: short half-life (~6 hours) — activity falls rapidly → low patient dose.\n'
                         'Iodine-123: accumulates in thyroid → used to diagnose thyroid disorders.\n'
                         "Gamma used: penetrates body to reach detector outside; shorter range alpha/beta wouldn't "
                         'exit.\n'
                         '\n'
                         'STERILISATION OF MEDICAL EQUIPMENT:\n'
                         'Gamma radiation from cobalt-60 kills bacteria and viruses on medical instruments.\n'
                         'Equipment sealed in packaging — gamma penetrates to sterilise contents.\n'
                         'No heat needed — suitable for heat-sensitive equipment.\n'
                         'Also used to sterilise food (extending shelf life).',
              'heading': 'Medical Uses'},
             {'content': 'PAPER/SHEET THICKNESS MONITORING:\n'
                         'Beta source placed above a moving sheet (paper, metal foil).\n'
                         'Beta detector below measures transmitted intensity.\n'
                         'More beta absorbed → thicker sheet.\n'
                         'Signal fed back to rollers → adjusts pressure to maintain correct thickness.\n'
                         'Beta chosen: absorbed by the sheet but not by surrounding air; alpha too weak to penetrate '
                         "any sheet; gamma too penetrating (wouldn't distinguish thicknesses).\n"
                         '\n'
                         'SMOKE DETECTORS:\n'
                         'Alpha source (americium-241) ionises air between two electrodes.\n'
                         'Ion current flows — circuit active.\n'
                         'Smoke particles absorb alpha radiation → less ionisation → current drops → alarm triggers.\n'
                         "Alpha chosen: short range — doesn't escape detector casing, safe for household use; ionises "
                         'air well.\n'
                         '\n'
                         'PIPELINE FAULT DETECTION:\n'
                         'Gamma source moved through underground pipe.\n'
                         'Gamma detector on surface detects escaping radiation.\n'
                         'Crack or fault → more gamma escapes → indicates location of leak.\n'
                         '\n'
                         'CARBON DATING:\n'
                         'Radioactive ¹⁴C decays with 5730-year half-life.\n'
                         'Compare ¹⁴C/¹²C ratio in sample vs living material.\n'
                         'Calculate age from ratio.',
              'heading': 'Industrial Uses'},
             {'content': 'SELECTION CRITERIA — match the type to the application:\n'
                         '\n'
                         'ALPHA:\n'
                         'High ionisation — useful for ionising air (smoke detectors).\n'
                         'Short range — safe for household devices.\n'
                         'NOT useful where penetration is needed.\n'
                         '\n'
                         'BETA:\n'
                         'Moderate penetration — can pass through a few mm of material.\n'
                         'Absorbed by aluminium — useful for thickness monitoring of thin sheets.\n'
                         'NOT useful for deep tissue medical imaging.\n'
                         '\n'
                         'GAMMA:\n'
                         'High penetration — can pass through the body and through thick materials.\n'
                         'Least ionising per path — causes less immediate local damage.\n'
                         'Useful for: medical imaging, radiotherapy, sterilisation, pipeline testing.\n'
                         'Must be shielded with lead/concrete.\n'
                         '\n'
                         'HALF-LIFE SELECTION:\n'
                         'Medical tracers: SHORT half-life (hours–days) — patient exposure minimal.\n'
                         "Industrial sources: LONGER half-life (years) — source doesn't need replacing frequently.\n"
                         'Carbon dating: half-life comparable to age of sample (thousands of years).',
              'heading': 'Choosing the Right Type'}],
  'title': 'Uses of Nuclear Radiation',
  'triple_only': 'Uses of nuclear radiation (physics only) — not in Combined Science as a separate detailed topic.',
  'variables': []},
 {'common_mistake': 'In nuclear fission, the NEUTRON is ABSORBED first, making the nucleus unstable — then it splits. '
                    'Fission is NOT the same as radioactive decay. The energy comes from the conversion of a tiny '
                    'amount of MASS into energy (mass defect). Control rods ABSORB neutrons — inserting them SLOWS or '
                    'stops the reaction.',
  'equations': ['E = mc²  (mass-energy equivalence)'],
  'fifas': [],
  'higher': None,
  'id': 'nuclear-fission',
  'key_note': 'Fission: large nucleus absorbs neutron → splits → two smaller nuclei + 2–3 neutrons + energy. Chain '
              'reaction: neutrons trigger further fissions. Critical mass: minimum for sustained chain reaction. '
              'Reactor: fuel rods + moderator (slows neutrons) + control rods (absorb neutrons) + coolant. Energy from '
              'mass defect (E = mc²).',
  'matching': {'instruction': 'Match each reactor component to its function.',
               'pairs': [('Fuel rods', 'Contain enriched uranium-235 — fission occurs here releasing thermal energy'),
                         ('Moderator', 'Slows fast neutrons to thermal speed — water or graphite'),
                         ('Control rods',
                          'Absorb neutrons — inserted deeper to slow reaction, withdrawn to increase power'),
                         ('Coolant', 'Transfers thermal energy from core to steam generator — water or CO₂')],
               'title': 'Nuclear Reactor Components'},
  'quiz': [{'opts': [('They absorb neutrons — inserting them deeper reduces neutron availability and slows the chain '
                      'reaction',
                      True),
                     ('They slow down neutrons — making them more likely to cause fission of U-235', False),
                     ('They cool the reactor core — preventing overheating by absorbing thermal energy', False),
                     ('They contain the radioactive fuel — preventing radiation from escaping the reactor', False)],
            'q': 'What is the purpose of control rods in a nuclear reactor?',
            'wrong_explanations': {1: 'MODERATORS (water/graphite) slow neutrons — control rods ABSORB them. These are '
                                      'different functions.',
                                   2: 'Coolant removes thermal energy from the core — control rods are neutron '
                                      'absorbers.',
                                   3: 'Fuel is contained in the fuel rods and pressure vessel — control rods '
                                      'specifically absorb neutrons.'}},
           {'opts': [("The total mass of products is slightly less than the total mass of reactants — this 'mass "
                      "defect' is converted to energy via E = mc²",
                      True),
                     ('The nucleus breaks apart releasing chemical bonds — chemical potential energy becomes kinetic '
                      'energy',
                      False),
                     ('The gamma radiation produced carries energy from the nucleus to the surroundings', False),
                     ('Electrons are released from the nucleus — their kinetic energy is the source of fission energy',
                      False)],
            'q': 'Why is energy released in a nuclear fission reaction?',
            'wrong_explanations': {1: 'Fission involves NUCLEAR forces — much stronger than chemical bonds. Chemical '
                                      'bond energies are millions of times smaller.',
                                   2: 'Gamma radiation does carry some energy away — but the primary energy source is '
                                      'the mass-energy conversion (mass defect), not the gamma radiation itself.',
                                   3: "Electrons are not the primary energy carriers in fission — it's the kinetic "
                                      'energy of the fission fragments and the mass-energy conversion.'}}],
  'rp': None,
  'spec': '6.4.5.1 (physics only)',
  'summary': 'Describe nuclear fission, chain reactions and the basic operation of a nuclear reactor.',
  'theory': [{'content': 'NUCLEAR FISSION is the splitting of a large, unstable nucleus into two smaller nuclei when '
                         'it absorbs a NEUTRON.\n'
                         '\n'
                         'FISSILABLE MATERIALS:\n'
                         'Uranium-235 (²³⁵U): most commonly used.\n'
                         'Plutonium-239 (²³⁹Pu): used in some reactors and weapons.\n'
                         '\n'
                         'WHAT HAPPENS:\n'
                         '1. A slow (thermal) NEUTRON is absorbed by a ²³⁵U nucleus.\n'
                         '2. The nucleus becomes highly unstable (²³⁶U) and splits.\n'
                         '3. Produces TWO SMALLER NUCLEI (fission fragments) + 2–3 NEUTRONS + ENERGY.\n'
                         '\n'
                         'EXAMPLE:\n'
                         '²³⁵U + n → ²³⁶U → ¹⁴¹Ba + ⁹²Kr + 3n + energy\n'
                         '\n'
                         'ENERGY RELEASED:\n'
                         'The total mass of products is LESS than the total mass of reactants.\n'
                         "The 'missing mass' is converted to energy: E = mc².\n"
                         'This tiny mass difference produces an enormous amount of energy.\n'
                         'One fission reaction releases ~200 MeV — vastly more than any chemical reaction (few eV).',
              'heading': 'What Is Nuclear Fission?'},
             {'content': 'CHAIN REACTION:\n'
                         'The 2–3 neutrons released by each fission can trigger further fission events.\n'
                         'Those produce more neutrons → trigger more fissions → chain reaction.\n'
                         '\n'
                         'CONTROLLED chain reaction (nuclear reactor): carefully managed — produces steady thermal '
                         'energy.\n'
                         'UNCONTROLLED chain reaction (nuclear weapon): exponential growth — massive energy release '
                         'almost instantaneously.\n'
                         '\n'
                         'CRITICAL MASS:\n'
                         'Minimum mass of fissile material needed to sustain a chain reaction.\n'
                         'Below critical mass: too many neutrons escape — chain reaction dies out.\n'
                         'Above critical mass: chain reaction sustained or grows.\n'
                         '\n'
                         'MODERATOR:\n'
                         'Neutrons from fission are FAST — must be SLOWED DOWN to be captured by U-235 nuclei.\n'
                         'Moderator (water or graphite) slows neutrons by elastic collisions.\n'
                         'Slow (thermal) neutrons are much more likely to cause fission.',
              'heading': 'Chain Reactions'},
             {'content': 'A NUCLEAR REACTOR generates thermal energy from controlled fission, which is used to produce '
                         'electricity.\n'
                         '\n'
                         'KEY COMPONENTS:\n'
                         'FUEL RODS: contain enriched uranium (mostly U-238 with ~3–5% U-235).\n'
                         'MODERATOR (water or graphite): slows neutrons to useful speed.\n'
                         'CONTROL RODS (boron or cadmium): absorb neutrons. Inserted deeper → fewer neutrons → less '
                         'fission. Withdrawn → more fission. Used to control power output.\n'
                         'COOLANT (water or CO₂): transfers thermal energy from reactor core to steam generator.\n'
                         'STEAM GENERATOR: hot coolant boils water → steam → drives turbine → generator → '
                         'electricity.\n'
                         'PRESSURE VESSEL AND SHIELDING: contains radiation, maintains pressure.\n'
                         '\n'
                         'ADVANTAGES of nuclear power:\n'
                         'Low CO₂ emissions during operation.\n'
                         'Very energy-dense fuel — small amount produces huge energy.\n'
                         'Reliable base-load power.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'High cost of building and decommissioning.\n'
                         'Nuclear waste: some isotopes remain radioactive for thousands of years — difficult storage.\n'
                         'Small risk of catastrophic accident (Chernobyl, Fukushima).',
              'heading': 'Nuclear Reactors'}],
  'title': 'Nuclear Fission',
  'triple_only': 'Nuclear fission (physics only) — not in Combined Science.',
  'variables': []},
 {'common_mistake': 'Fusion releases energy because the product nucleus has LESS MASS than the sum of the reactants — '
                    'the mass defect converts to energy (E=mc²). Same principle as fission but with different nuclei. '
                    'Fusion requires EXTREMELY HIGH TEMPERATURE (not just high pressure) because nuclei must have '
                    'enough kinetic energy to overcome electrostatic repulsion.',
  'equations': ['²H + ³H → ⁴He + n + 17.6 MeV  (deuterium-tritium fusion)'],
  'fifas': [],
  'higher': None,
  'id': 'nuclear-fusion',
  'key_note': 'Fusion: two small nuclei join → larger nucleus + energy. Powers the Sun. D-T fusion: ²H + ³H → ⁴He + n. '
              'Requires ~100 million °C plasma. Confinement: magnetic (tokamak/ITER) or laser. Advantages: abundant '
              'fuel, clean waste, inherently safe. Challenge: net energy gain not yet achieved. Compare with fission: '
              'fusion cleaner but not yet practical.',
  'matching': {'instruction': 'Match each property to fusion, fission, or both.',
               'pairs': [('Fusion only', 'Small nuclei join together — releases energy from mass defect'),
                         ('Fission only', 'Large nucleus absorbs neutron and splits — used in nuclear reactors today'),
                         ('Both', 'Energy released comes from a mass defect — E = mc²'),
                         ('Fusion only', 'Requires ~100 million °C plasma — not yet achieved at practical scale'),
                         ('Fission only', 'Produces long-lived radioactive waste — difficult disposal')],
               'title': 'Fusion vs Fission'},
  'quiz': [{'opts': [('Nuclei need enough kinetic energy to overcome the electrostatic repulsion between their '
                      'positive charges and get close enough for the strong nuclear force to cause fusion',
                      True),
                     ('Fusion produces so much energy that the reaction must start at high temperature to release it',
                      False),
                     ('Radioactive materials only become fusible at extreme temperatures — below this they are too '
                      'stable',
                      False),
                     ('High temperature converts hydrogen to plasma, which is the only state in which fusion can occur '
                      'in a magnetic field',
                      False)],
            'q': 'Why does nuclear fusion require temperatures of around 100 million degrees Celsius?',
            'wrong_explanations': {1: 'The energy comes FROM the fusion — high temperature is the REQUIREMENT to START '
                                      'fusion, not a result of it.',
                                   2: "The materials don't need to be radioactive for fusion — deuterium and tritium "
                                      'are simply isotopes of hydrogen.',
                                   3: 'Plasma formation IS needed for magnetic confinement — but the fundamental '
                                      'reason for high temperature is overcoming electrostatic repulsion, not simply '
                                      'creating plasma.'}},
           {'opts': [('Fusion uses virtually unlimited fuel from seawater, produces no long-lived radioactive waste '
                      'and is inherently safe — the reaction cannot run away',
                      True),
                     ('Fusion is already used commercially — it is cheaper and more reliable than fission', False),
                     ('Fusion produces more energy per reaction than fission — so fewer reactions are needed', False),
                     ('Fusion does not require any confinement — it operates safely at room temperature', False)],
            'q': 'What is the main advantage of nuclear fusion over nuclear fission as an energy source?',
            'wrong_explanations': {1: 'Fusion is NOT yet used commercially — it is still under development. ITER and '
                                      'other projects are research reactors.',
                                   2: 'Individual fusion reactions do release large amounts of energy, but individual '
                                      "fission reactions also release large amounts — the comparison isn't "
                                      'straightforward per reaction.',
                                   3: 'Fusion requires extreme temperature and pressure confinement — one of the '
                                      'biggest engineering challenges.'}}],
  'rp': None,
  'spec': '6.4.5.2 (physics only)',
  'summary': 'Describe nuclear fusion, why it requires extreme conditions and its potential as an energy source.',
  'theory': [{'content': 'NUCLEAR FUSION is the joining together of two small nuclei to form a larger nucleus, '
                         'releasing energy.\n'
                         '\n'
                         'Fusion is the OPPOSITE of fission:\n'
                         'Fission: large nucleus splits into smaller ones.\n'
                         'Fusion: small nuclei join to make a larger one.\n'
                         '\n'
                         'FUSION IN THE SUN:\n'
                         'The Sun and all stars are powered by nuclear fusion.\n'
                         "In the Sun's core: hydrogen nuclei (protons) fuse under enormous pressure and temperature.\n"
                         'Four protons → helium-4 nucleus (two protons + two neutrons) + energy.\n'
                         '\n'
                         'PRACTICAL FUSION REACTIONS (for energy):\n'
                         'Deuterium (²H) + Tritium (³H) → Helium-4 + neutron + energy\n'
                         '²H + ³H → ⁴He + n + 17.6 MeV\n'
                         '\n'
                         'Deuterium: from seawater (abundant). Tritium: from lithium (moderately abundant).\n'
                         'Fuel is far more abundant than uranium — potential to power civilisation for millions of '
                         'years.',
              'heading': 'What Is Nuclear Fusion?'},
             {'content': 'THE COULOMB BARRIER:\n'
                         'Both nuclei are positively charged → they REPEL each other.\n'
                         'To fuse, nuclei must get close enough for the STRONG NUCLEAR FORCE to take over.\n'
                         'This requires overcoming the electrostatic repulsion — needs extremely high kinetic energy.\n'
                         '\n'
                         'REQUIRED CONDITIONS:\n'
                         "TEMPERATURE: ~100 million °C (ten times hotter than the Sun's core for practical fusion "
                         'reactors).\n'
                         'At this temperature, matter exists as PLASMA — fully ionised gas of electrons and nuclei.\n'
                         'High temperature → high kinetic energy → nuclei approach close enough to fuse.\n'
                         '\n'
                         'CONFINEMENT:\n'
                         'No material can contain plasma at 100 million °C.\n'
                         'SOLUTIONS:\n'
                         'MAGNETIC CONFINEMENT: powerful magnetic fields (tokamak design) hold plasma away from walls '
                         '— JET, ITER.\n'
                         'INERTIAL CONFINEMENT: powerful lasers compress a small pellet of fuel — NIF (USA).\n'
                         '\n'
                         'PRESSURE:\n'
                         'In stars: enormous gravitational pressure provides confinement.\n'
                         'On Earth: must use magnetic or laser confinement instead.',
              'heading': 'Why Fusion Requires Extreme Conditions'},
             {'content': 'ADVANTAGES OF FUSION:\n'
                         'VIRTUALLY UNLIMITED FUEL: deuterium from seawater; tritium from lithium.\n'
                         'NO CO₂ EMISSIONS during operation.\n'
                         'NO LONG-LIVED RADIOACTIVE WASTE: products (helium + neutrons) — neutron activation of '
                         'reactor walls is manageable, much shorter half-lives than fission waste.\n'
                         "INHERENTLY SAFE: reaction stops immediately if conditions not maintained — cannot 'run away' "
                         'like fission.\n'
                         'High energy density: small amount of fuel → huge energy.\n'
                         '\n'
                         'CHALLENGES:\n'
                         'Extreme temperatures require plasma confinement — technically very difficult.\n'
                         'More energy currently required to initiate and maintain fusion than is produced — net energy '
                         'gain not yet achieved consistently.\n'
                         'Materials: reactor walls damaged by high-energy neutrons over time.\n'
                         'Cost: massive engineering projects (ITER costs ~€20 billion).\n'
                         '\n'
                         'CURRENT STATUS:\n'
                         'JET (Joint European Torus): record fusion energy output 2022.\n'
                         'ITER: international reactor under construction in France — target: Q > 10 (10× more energy '
                         'out than in).\n'
                         'First commercial fusion power: optimistically predicted 2040s–2050s.\n'
                         '\n'
                         'FUSION vs FISSION:\n'
                         'Fusion: cleaner waste, more fuel, inherently safer, not yet achieved at scale.\n'
                         'Fission: already used commercially, radioactive waste problem, limited uranium.',
              'heading': 'Fusion as an Energy Source'}],
  'title': 'Nuclear Fusion',
  'triple_only': 'Nuclear fusion (physics only) — not in Combined Science.',
  'variables': []}],

"forces": [{'common_mistake': 'SPEED is scalar, VELOCITY is vector. DISTANCE is scalar, DISPLACEMENT is vector. The most common '
                    'error is treating velocity and speed as the same thing. A car travelling in a circle at constant '
                    'SPEED has changing VELOCITY (direction changes).',
  'equations': ['Resultant² = F₁² + F₂²  (for perpendicular vectors)'],
  'fifas': [],
  'higher': None,
  'id': 'scalar-vector-quantities',
  'key_note': 'Scalar: magnitude only (distance, speed, mass, energy). Vector: magnitude + direction (displacement, '
              'velocity, force, acceleration, weight). Arrow length = magnitude; direction = vector direction. Adding '
              'vectors: same direction = add; opposite = subtract; right angles = Pythagoras.',
  'matching': {'instruction': 'Sort each quantity into scalar or vector.',
               'pairs': [('Scalar', 'Speed — magnitude of motion with no direction'),
                         ('Vector', 'Velocity — speed in a specified direction'),
                         ('Scalar', 'Distance — total path length, no direction'),
                         ('Vector', 'Displacement — straight-line distance from start, with direction'),
                         ('Vector', 'Force — magnitude and direction (e.g. 10 N downward)')],
               'title': 'Scalar or Vector?'},
  'quiz': [{'opts': [('Distance = 400 m, displacement = 0 m — the runner returns to the starting point', True),
                     ('Distance = 0 m, displacement = 400 m — same as the lap distance', False),
                     ('Distance = 400 m, displacement = 400 m — both equal the lap length', False),
                     ('Both are zero — one full lap cancels everything out', False)],
            'q': "A runner completes one full lap of a 400 m circular track. What is the runner's distance and "
                 'displacement?',
            'wrong_explanations': {1: 'Displacement is the NET change in position. After a full lap the runner is back '
                                      'at start → displacement = 0. Distance is the total path = 400 m.',
                                   2: 'Distance = displacement only for straight-line motion in one direction — a full '
                                      'lap gives zero displacement.',
                                   3: 'Distance is never zero if the runner moved — it counts total path length '
                                      'regardless of direction.'}},
           {'opts': [('5 N to the right — 8 − 3 = 5 N; direction is that of the larger force', True),
                     ('11 N to the right — 8 + 3 = 11 N (added without considering direction)', False),
                     ('5 N to the left — 3 − 8 = −5 N so leftward', False),
                     ('Zero — two forces always cancel out', False)],
            'q': 'Two forces act on a box: 8 N to the right and 3 N to the left. What is the resultant force?',
            'wrong_explanations': {1: 'Vectors in OPPOSITE directions SUBTRACT. Adding gives 11 N which ignores '
                                      'direction.',
                                   2: 'The net force is in the direction of the LARGER force — 8 N is larger than 3 N '
                                      'so resultant is rightward.',
                                   3: 'Forces only cancel when equal in magnitude AND opposite in direction. 8 N ≠ 3 N '
                                      "so they don't cancel."}}],
  'rp': None,
  'spec': '6.5.1.1',
  'summary': 'Distinguish scalar and vector quantities and represent vectors with arrows.',
  'theory': [{'content': 'SCALAR quantities have MAGNITUDE (size) only.\n'
                         'VECTOR quantities have both MAGNITUDE and DIRECTION.\n'
                         '\n'
                         'SCALARS:\n'
                         'Distance, speed, mass, time, temperature, energy, power, pressure.\n'
                         '\n'
                         'VECTORS:\n'
                         'Displacement, velocity, force, acceleration, momentum, weight.\n'
                         '\n'
                         'Why direction matters:\n'
                         'A force of 10 N to the right and 10 N to the left cancel out — net force is zero.\n'
                         "If force were scalar (no direction), you couldn't distinguish these.\n"
                         '\n'
                         'VECTOR REPRESENTATION:\n'
                         'An arrow represents a vector.\n'
                         'Length of arrow ∝ magnitude.\n'
                         'Direction of arrow = direction of the quantity.',
              'heading': 'Scalars and Vectors'},
             {'content': 'Several pairs are commonly confused:\n'
                         '\n'
                         'DISTANCE vs DISPLACEMENT:\n'
                         'Distance: total path length travelled — scalar.\n'
                         'Displacement: straight-line distance from start to finish, with direction — vector.\n'
                         'Example: walking 3 m east then 3 m west → distance = 6 m; displacement = 0 m.\n'
                         '\n'
                         'SPEED vs VELOCITY:\n'
                         'Speed: how fast — scalar (magnitude only).\n'
                         'Velocity: speed in a specified direction — vector.\n'
                         'Example: car at 30 m/s — speed = 30 m/s. Velocity = 30 m/s north.\n'
                         '\n'
                         'MASS vs WEIGHT:\n'
                         'Mass: amount of matter — scalar (kg).\n'
                         'Weight: gravitational force — vector (N, acts downward).',
              'heading': 'Distinguishing Common Pairs'},
             {'content': 'When adding SCALAR quantities: simple arithmetic.\n'
                         '3 kg + 5 kg = 8 kg (always).\n'
                         '\n'
                         'When adding VECTOR quantities: direction matters.\n'
                         'Two forces in the SAME direction: add magnitudes.\n'
                         '10 N + 5 N (both right) = 15 N right.\n'
                         '\n'
                         'Two forces in OPPOSITE directions: subtract smaller from larger.\n'
                         '10 N right + 5 N left = 5 N right (resultant).\n'
                         '\n'
                         'Two forces at RIGHT ANGLES: use Pythagoras.\n'
                         'Resultant² = F₁² + F₂²\n'
                         '3 N up + 4 N right → resultant = √(9 + 16) = 5 N (at an angle).\n'
                         '\n'
                         'Scale drawings can also be used to find the resultant of vectors at any angle.',
              'heading': 'Adding Vectors'}],
  'title': 'Scalar and Vector Quantities',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Gravity is a NON-CONTACT force — it acts at a distance without objects touching. Weight is the '
                    'gravitational force on an object. Normal contact force is NOT the same as weight — normal force '
                    'is a REACTION from the surface, perpendicular to it.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'contact-noncontact-forces',
  'key_note': 'Contact: friction, air resistance, tension, normal contact, compression, upthrust. Non-contact: gravity '
              '(always attractive), electrostatic (attract/repel), magnetic (attract/repel). Force = vector (N). '
              'Forces cause changes in speed, direction or shape.',
  'matching': {'instruction': 'Sort each force into contact or non-contact.',
               'pairs': [('Contact force', 'Friction — acts between surfaces in direct physical contact'),
                         ('Contact force', 'Tension — pull through a rope or string physically attached to objects'),
                         ('Contact force', 'Normal contact force — surface pushes perpendicularly on resting object'),
                         ('Non-contact force', 'Gravity — attractive force between masses, acts without touching'),
                         ('Non-contact force', 'Magnetic force — acts between magnets across empty space')],
               'title': 'Contact or Non-Contact?'},
  'quiz': [{'opts': [('Weight (gravity, non-contact, downward) and normal contact force (contact, upward) — these '
                      'balance so the book is stationary',
                      True),
                     ('Weight (downward) and friction (upward) — friction stops the book from falling', False),
                     ('Weight and tension — the table pulls the book down with tension', False),
                     ('Only weight acts — no force is needed to keep a stationary object still', False)],
            'q': 'A book rests on a table. Which two forces act on the book and what type are they?',
            'wrong_explanations': {1: "Friction acts parallel to surfaces (opposing sliding) — it doesn't act "
                                      'vertically on a stationary book sitting on a flat table.',
                                   2: 'Tension acts through strings/ropes — not through a solid table supporting a '
                                      'book.',
                                   3: "Newton's First Law: a stationary object has balanced forces — weight down is "
                                      'balanced by normal contact force up.'}},
           {'opts': [('The gravitational pull of the Sun on the Earth — acts across empty space without touching',
                      True),
                     ('Air resistance on a falling skydiver — acts through contact with air molecules', False),
                     ('Tension in a rope supporting a hanging mass — acts through physical contact along the rope',
                      False),
                     ('Upthrust on a submarine — acts through the water directly in contact with the hull', False)],
            'q': 'Which of the following is a non-contact force?',
            'wrong_explanations': {1: 'Air resistance is a CONTACT force — it acts through collisions between air '
                                      "molecules and the skydiver's body.",
                                   2: 'Tension is a CONTACT force — transmitted through the physical rope.',
                                   3: 'Upthrust is a CONTACT force — it acts through direct fluid pressure on the '
                                      'submerged surface.'}}],
  'rp': None,
  'spec': '6.5.1.2',
  'summary': 'Classify forces as contact or non-contact and give examples of each.',
  'theory': [{'content': 'A FORCE is a push or pull that acts on an object due to an interaction with another object.\n'
                         '\n'
                         'Forces are VECTOR quantities — they have magnitude and direction.\n'
                         'Measured in NEWTONS (N).\n'
                         'Forces can: change speed, change direction, change shape of an object.\n'
                         '\n'
                         'All forces arise from interactions between two objects:\n'
                         'Object A exerts a force on object B.\n'
                         "Object B exerts an equal and opposite force on object A (Newton's Third Law).",
              'heading': 'What Is a Force?'},
             {'content': 'CONTACT FORCES require the two objects to be PHYSICALLY TOUCHING.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'FRICTION — opposes relative motion between surfaces in contact. A book sliding along a '
                         'table.\n'
                         'AIR RESISTANCE (drag) — friction between an object and air/fluid. A car moving through air.\n'
                         'TENSION — pulling force through a string, rope or cable. A hanging weight.\n'
                         'NORMAL CONTACT FORCE — perpendicular force from a surface on an object resting on it. Book '
                         'on a table.\n'
                         'COMPRESSION — a pushing force through a solid. A compressed spring.\n'
                         'UPTHRUST — upward force from a fluid on a submerged object. A boat floating.\n'
                         '\n'
                         'Contact forces act through direct physical interaction between surfaces.',
              'heading': 'Contact Forces'},
             {'content': 'NON-CONTACT FORCES act between objects that are PHYSICALLY SEPARATED — no touching '
                         'required.\n'
                         '\n'
                         'Three fundamental non-contact forces at GCSE:\n'
                         '\n'
                         'GRAVITATION (gravity):\n'
                         'Attractive force between any two objects with mass.\n'
                         'The Earth attracts all objects towards its centre.\n'
                         "Acts over very large distances — the Sun's gravity holds planets in orbit.\n"
                         '\n'
                         'ELECTROSTATIC FORCE:\n'
                         'Force between charged objects.\n'
                         'Opposite charges attract; like charges repel.\n'
                         'Example: charged balloon sticks to a wall (different charges attract).\n'
                         '\n'
                         'MAGNETIC FORCE:\n'
                         'Force between magnets or between a magnet and a magnetic material.\n'
                         'Opposite poles attract; like poles repel.\n'
                         'Acts through space without physical contact — a magnet picks up iron filings from a '
                         'distance.\n'
                         '\n'
                         'All three non-contact forces can attract or repel (except gravity — gravity is always '
                         'attractive).',
              'heading': 'Non-Contact Forces'}],
  'title': 'Contact and Non-Contact Forces',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Mass and weight are DIFFERENT things. Mass (kg) is constant everywhere. Weight (N) changes with '
                    'gravitational field strength. On the Moon, your MASS stays the same but your WEIGHT is less. '
                    'Weight is measured in NEWTONS — not kilograms.',
  'equations': ['W = m × g'],
  'fifas': [{'label': 'Weight Calculation',
             'question': 'Calculate the weight of a 12 kg object on Earth. (g = 9.8 N/kg)',
             'steps': [('F', 'W = m × g'),
                       ('I', 'm = 12 kg, g = 9.8 N/kg'),
                       ('F', 'W = 12 × 9.8'),
                       ('A', 'W = 117.6 N')]}],
  'higher': None,
  'id': 'gravity',
  'key_note': 'W = mg. Weight = gravitational force (N, vector, downward). Mass = amount of matter (kg, scalar, '
              'constant). g = 9.8 N/kg on Earth, 1.6 N/kg on Moon. Weight changes with location; mass does not. '
              'Gravitational field: region where masses experience force.',
  'matching': {'instruction': 'Match each statement to mass or weight.',
               'pairs': [('Mass', 'Measured in kilograms — stays the same on the Moon and on Earth'),
                         ('Weight', 'Measured in newtons — changes with gravitational field strength'),
                         ('W = 686 N', '70 kg person on Earth — W = 70 × 9.8 = 686 N'),
                         ('W = 112 N', '70 kg person on the Moon — W = 70 × 1.6 = 112 N')],
               'title': 'Mass vs Weight'},
  'quiz': [{'opts': [('128 N — W = 80 × 1.6 = 128 N', True),
                     ("784 N — W = 80 × 9.8 (used Earth's g)", False),
                     ('50 kg — mass on the Moon is 1/6 of Earth mass', False),
                     ('0 N — astronauts are weightless on the Moon', False)],
            'q': 'An astronaut has mass 80 kg. What is her weight on the Moon? (g_Moon = 1.6 N/kg)',
            'wrong_explanations': {1: "Use the Moon's gravitational field strength (1.6 N/kg), not Earth's (9.8 N/kg).",
                                   2: 'Mass NEVER changes — it is 80 kg on the Moon, on Earth, anywhere. Only weight '
                                      'changes.',
                                   3: 'The Moon has significant gravity (1.6 N/kg) — astronauts are not weightless on '
                                      'the surface. Weightlessness occurs in orbit (free fall).'}},
           {'opts': [('Weight is measured in NEWTONS — kilograms measure MASS. Their weight is approximately 588 N (60 '
                      '× 9.8)',
                      True),
                     ('Nothing is wrong — weight and mass are the same thing and can be measured in the same units',
                      False),
                     ('Weight should be in grams — 60,000 g', False),
                     ('The statement is correct on the Moon but wrong on Earth', False)],
            'q': "A student says 'my weight is 60 kg'. What is wrong with this statement?",
            'wrong_explanations': {1: 'Weight and mass are different physical quantities — they cannot use the same '
                                      'units.',
                                   2: 'Grams are a unit of mass — not weight. Weight is always in newtons.',
                                   3: 'Weight is always in newtons everywhere — the statement would still be wrong on '
                                      'the Moon (just a different wrong value).'}}],
  'rp': None,
  'spec': '6.5.1.3',
  'summary': 'Explain weight as gravitational force, distinguish mass from weight, and calculate using W = mg.',
  'theory': [{'content': 'WEIGHT is the FORCE acting on an object due to GRAVITY — it is a vector quantity acting '
                         'downward.\n'
                         '\n'
                         'WEIGHT EQUATION:\n'
                         'W = m × g\n'
                         '\n'
                         'W = weight (newtons, N)\n'
                         'm = mass (kilograms, kg)\n'
                         'g = gravitational field strength (N/kg)\n'
                         '\n'
                         'On Earth: g = 9.8 N/kg (use 10 N/kg for estimates).\n'
                         "On the Moon: g ≈ 1.6 N/kg (about 1/6 of Earth's).\n"
                         '\n'
                         'MEANING OF g:\n'
                         'The gravitational field strength g tells us the weight per unit mass.\n'
                         'On Earth: every 1 kg of mass experiences 9.8 N of gravitational force downward.',
              'heading': 'Weight and Gravitational Field Strength'},
             {'content': 'MASS:\n'
                         'Amount of matter in an object.\n'
                         'Scalar quantity — measured in kilograms (kg).\n'
                         "Constant everywhere in the universe — doesn't change with location.\n"
                         '\n'
                         'WEIGHT:\n'
                         'Gravitational force on an object.\n'
                         'Vector quantity — measured in newtons (N).\n'
                         'Changes with location — depends on gravitational field strength.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'A 70 kg astronaut:\n'
                         'On Earth: W = 70 × 9.8 = 686 N\n'
                         'On the Moon: W = 70 × 1.6 = 112 N\n'
                         'In deep space (no gravity): W = 0 N\n'
                         'Mass is 70 kg everywhere.\n'
                         '\n'
                         'MEASURING:\n'
                         'Mass: measured with a balance (compares gravitational force on both sides — same anywhere).\n'
                         'Weight: measured with a calibrated spring balance/newton meter (reads force directly).',
              'heading': 'Mass vs Weight'},
             {'content': 'A GRAVITATIONAL FIELD is a region around a mass where any other mass experiences a force.\n'
                         '\n'
                         'Field lines point TOWARDS the centre of mass (gravity is always attractive).\n'
                         "On Earth's surface, field lines point vertically downward (towards Earth's centre).\n"
                         '\n'
                         'Gravitational field strength DECREASES with distance from the mass:\n'
                         "At Earth's surface: g = 9.8 N/kg\n"
                         'At altitude of 400 km (ISS orbit): g ≈ 8.7 N/kg (astronauts are still falling — not '
                         'weightless!)\n'
                         '\n'
                         "WHY 'WEIGHTLESSNESS' IN SPACE:\n"
                         'Astronauts in orbit are NOT weightless in terms of gravitational force.\n'
                         'They are in FREE FALL — constantly falling towards Earth but moving sideways fast enough to '
                         'miss it.\n'
                         'The sensation of weightlessness occurs because everything around them is falling at the same '
                         'rate.',
              'heading': 'Gravitational Fields'}],
  'title': 'Gravity',
  'triple_only': None,
  'variables': [('W', 'Weight', 'newtons', 'N'),
                ('m', 'Mass', 'kilograms', 'kg'),
                ('g', 'Gravitational field strength', 'N/kg', 'N/kg')]},
 {'common_mistake': 'A resultant force of ZERO does NOT mean the object is stationary — it means CONSTANT VELOCITY '
                    '(which includes stationary). An object moving at constant speed in a straight line also has zero '
                    'resultant force.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'resultant-forces',
  'key_note': 'Resultant = single force with same effect as all forces combined. Balanced (zero resultant): stationary '
              'or constant velocity. Unbalanced: acceleration. Free body diagrams: arrows from object, length = '
              'magnitude. Terminal velocity: air resistance = weight → zero resultant → constant speed.',
  'matching': {'instruction': 'Match each situation to the correct description of the resultant force and motion.',
               'pairs': [('Resultant = 0, stationary', 'Book on table — weight balanced by normal contact force'),
                         ('Resultant = 0, moving',
                          'Car at constant speed on motorway — driving force equals resistance'),
                         ('Resultant forward',
                          'Car accelerating — driving force greater than air resistance + friction'),
                         ('Terminal velocity', 'Skydiver at constant speed — weight = air resistance, zero resultant')],
               'title': 'Resultant Force and Motion'},
  'quiz': [{'opts': [('The resultant force is zero — driving force equals resistive forces (friction + air resistance)',
                      True),
                     ('No forces act on the car — it moves freely', False),
                     ('The driving force is greater than resistive forces — the car is accelerating', False),
                     ('The car must be slowing down — constant speed requires deceleration', False)],
            'q': 'A car travels at constant speed along a straight road. What does this tell us about the forces on '
                 'the car?',
            'wrong_explanations': {1: 'Forces always act on a moving car — gravity, normal, driving force, air '
                                      'resistance. Constant speed means they BALANCE.',
                                   2: 'Constant speed means balanced forces (resultant = 0) — not acceleration. '
                                      'Acceleration requires UNBALANCED forces.',
                                   3: 'Constant speed is neither speeding up nor slowing down — it requires balanced '
                                      'forces.'}},
           {'opts': [('Air resistance increases with speed until it equals weight — resultant becomes zero, so '
                      'acceleration stops',
                      True),
                     ('The skydiver runs out of energy from the jump — no more acceleration', False),
                     ('Gravity decreases with altitude — weight reduces to zero at terminal velocity', False),
                     ('Terminal velocity means constant acceleration, not constant speed', False)],
            'q': 'A skydiver jumps from a plane. Initially they accelerate. Later they reach terminal velocity. Why do '
                 'they stop accelerating?',
            'wrong_explanations': {1: "Skydivers don't 'run out of energy' — gravity continuously acts on them. "
                                      'Acceleration stops when forces BALANCE.',
                                   2: 'Gravity changes very little over the heights of a typical skydive — weight '
                                      'stays approximately constant.',
                                   3: 'Terminal velocity means CONSTANT SPEED (zero acceleration) — not constant '
                                      'acceleration.'}}],
  'rp': None,
  'spec': '6.5.1.4',
  'summary': 'Find the resultant of forces and relate it to the motion of an object.',
  'theory': [{'content': 'When MULTIPLE FORCES act on an object, they can be replaced by a SINGLE RESULTANT FORCE that '
                         'has the same effect.\n'
                         '\n'
                         'Finding the resultant:\n'
                         'FORCES IN THE SAME DIRECTION: add magnitudes.\n'
                         'FORCES IN OPPOSITE DIRECTIONS: subtract smaller from larger; direction = that of larger '
                         'force.\n'
                         'FORCES AT RIGHT ANGLES: use Pythagoras; direction from trigonometry or scale drawing.\n'
                         '\n'
                         'BALANCED FORCES (resultant = 0):\n'
                         'If resultant force = 0, the object is either:\n'
                         'Stationary (at rest), OR\n'
                         'Moving at CONSTANT VELOCITY (constant speed in a straight line).\n'
                         "This is Newton's First Law.\n"
                         '\n'
                         'UNBALANCED FORCES (resultant ≠ 0):\n'
                         'If resultant force ≠ 0, the object ACCELERATES (changes speed or direction).',
              'heading': 'What Is a Resultant Force?'},
             {'content': 'A FREE BODY DIAGRAM shows all forces acting ON a single object as arrows:\n'
                         'Length ∝ magnitude of force.\n'
                         'Arrow points in direction of force.\n'
                         'Object represented as a box or dot at the centre.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Stationary book on table:\n'
                         '↑ Normal contact force (upward)\n'
                         '↓ Weight (downward)\n'
                         'Resultant = 0 → balanced → stationary ✓\n'
                         '\n'
                         'Car accelerating forward:\n'
                         '→ Driving force (forward, larger)\n'
                         '← Friction + air resistance (backward, smaller)\n'
                         'Resultant = driving force − resistance → forwards → accelerates ✓\n'
                         '\n'
                         'Skydiver in free fall (before terminal velocity):\n'
                         '↓ Weight (downward)\n'
                         '↑ Air resistance (upward, smaller)\n'
                         'Resultant = weight − air resistance → downward → accelerates downward',
              'heading': 'Free Body Diagrams'},
             {'content': 'An object is in EQUILIBRIUM when the resultant force is zero:\n'
                         'All forces balance — no net force.\n'
                         'Object stays still or moves at constant velocity.\n'
                         '\n'
                         'When forces are UNBALANCED:\n'
                         'Resultant force in the direction of motion → object SPEEDS UP.\n'
                         'Resultant force opposite to direction of motion → object SLOWS DOWN.\n'
                         'Resultant force perpendicular to motion → object CHANGES DIRECTION.\n'
                         '\n'
                         'SCALE DRAWING METHOD:\n'
                         'Draw vectors head-to-tail to scale.\n'
                         'Resultant = vector from tail of first to head of last.\n'
                         'Measure magnitude with ruler (× scale factor).\n'
                         'Measure direction with protractor.\n'
                         '\n'
                         'TERMINAL VELOCITY:\n'
                         'As a falling object speeds up → air resistance increases.\n'
                         'Eventually air resistance = weight → resultant = 0 → constant velocity = terminal velocity.\n'
                         'For skydivers: terminal velocity ≈ 55 m/s (120 mph) before parachute.',
              'heading': 'Equilibrium and Resultant'}],
  'title': 'Resultant Forces',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Work is only done when the object moves IN THE DIRECTION of the force. Holding a heavy weight '
                    'stationary does NO work (no displacement) — even though it feels tiring. Also: W in this equation '
                    'is work done (joules), NOT weight.',
  'equations': ['W = F × s'],
  'fifas': [{'label': 'Work Done',
             'question': 'A 300 N force moves a crate 6 m along a floor. Calculate the work done.',
             'steps': [('F', 'W = F × s'), ('I', 'F = 300 N, s = 6 m'), ('F', 'W = 300 × 6'), ('A', 'W = 1800 J')]}],
  'higher': None,
  'id': 'work-done-energy-transfer',
  'key_note': 'W = Fs. Work done = energy transferred (J). 1 J = 1 N × 1 m. Work only done if object moves in force '
              'direction. Lifting = GPE gained = mgh = Fs. Friction does work → thermal energy. P = Fv (force × speed '
              'for constant motion).',
  'matching': {'instruction': 'Match each scenario to the correct work done value.',
               'pairs': [('2000 J', '500 N force moves object 4 m — W = 500 × 4'),
                         ('98 J', 'Lifting 5 kg by 2 m — W = mgh = 5 × 9.8 × 2'),
                         ('0 J', 'Holding a 100 N weight stationary — no displacement, no work done'),
                         ('5 m', '1000 J work done by a 200 N force — s = W ÷ F = 1000 ÷ 200')],
               'title': 'Work Done Calculations'},
  'quiz': [{'opts': [('0 J — gravity acts downward but the box moves horizontally; no displacement in the direction of '
                      'the gravitational force',
                      True),
                     ('1960 J — W = mgs = 20 × 9.8 × 10', False),
                     ('2000 J — W = 20 × 10 × 10 (using g = 10)', False),
                     ('196 J — W = mg = 20 × 9.8 (forgot to include distance)', False)],
            'q': 'A person carries a 20 kg box horizontally for 10 m at constant height. How much work does gravity do '
                 'on the box?',
            'wrong_explanations': {1: 'W = F × s requires the displacement to be in the DIRECTION of the force. '
                                      'Gravity acts downward; box moves horizontally → no work done by gravity.',
                                   2: 'Same error — using horizontal distance for a vertical force.',
                                   3: 'mg gives weight (force) not work — must multiply by distance IN THE DIRECTION '
                                      'of the force, which is zero here.'}},
           {'opts': [('8 m — s = W ÷ F = 3200 ÷ 400 = 8 m', True),
                     ('1,280,000 m — s = W × F = 3200 × 400', False),
                     ('0.125 m — s = F ÷ W = 400 ÷ 3200', False),
                     ('3600 m — s = W + F = 3200 + 400', False)],
            'q': 'A 400 N force does 3200 J of work. How far does the object move?',
            'wrong_explanations': {1: 's = W × F multiplies — but W = Fs means s = W ÷ F.',
                                   2: 's = F ÷ W inverts the rearrangement: s = W ÷ F = 3200 ÷ 400 = 8 m.',
                                   3: 'Adding work and force gives meaningless units (J + N). Use W = Fs rearranged: s '
                                      '= W ÷ F.'}}],
  'rp': None,
  'spec': '6.5.2',
  'summary': 'Calculate work done by a force and understand it as energy transferred.',
  'theory': [{'content': 'When a FORCE causes an object to move through a DISTANCE, WORK IS DONE.\n'
                         '\n'
                         'Work is an energy transfer — doing work transfers energy from one store to another.\n'
                         '\n'
                         'EQUATION:\n'
                         'W = F × s\n'
                         '\n'
                         'W = work done (joules, J)\n'
                         'F = force (newtons, N)\n'
                         's = distance moved along the line of action of the force (metres, m)\n'
                         '\n'
                         '1 joule = 1 newton-metre (1 J = 1 N·m).\n'
                         '\n'
                         'KEY CONDITION:\n'
                         'Work is only done when the object moves IN THE DIRECTION the force acts.\n'
                         'If the force and motion are at right angles → no work done by that force.\n'
                         'Example: carrying a heavy bag horizontally — the vertical weight does no work (no vertical '
                         'movement).',
              'heading': 'Work Done'},
             {'content': 'Work done = energy transferred.\n'
                         '\n'
                         'ENERGY TRANSFERS THROUGH WORK:\n'
                         'Pushing a box along the floor: work done against friction → kinetic energy of box + thermal '
                         'energy (friction).\n'
                         'Lifting an object: work done against gravity → gravitational PE gained.\n'
                         'Compressing a spring: work done by force → elastic PE stored.\n'
                         'Braking a car: friction does work → kinetic energy → thermal energy.\n'
                         '\n'
                         'EXAMPLE 1:\n'
                         'A 500 N force pushes a box 4 m along the floor.\n'
                         'W = 500 × 4 = 2000 J of energy transferred.\n'
                         '\n'
                         'EXAMPLE 2:\n'
                         'How far does a 200 N force push an object if 1000 J of work is done?\n'
                         's = W ÷ F = 1000 ÷ 200 = 5 m\n'
                         '\n'
                         'LINK TO POWER:\n'
                         'P = W ÷ t = F × s ÷ t = F × v\n'
                         'Power also equals force × speed (for constant force and velocity).',
              'heading': 'Work and Energy'},
             {'content': 'UNIT CHECK — understanding dimensions:\n'
                         '1 J = 1 N × 1 m = 1 N·m\n'
                         '\n'
                         'This is why energy and work have the same units (joules).\n'
                         '\n'
                         'COMMON CONTEXTS:\n'
                         'Lifting: W = F × h (where F = weight = mg and h = height)\n'
                         'Combined with W = mg: W = mgh — same as GPE equation.\n'
                         '\n'
                         'EXAMPLE — lifting:\n'
                         'Lift 5 kg by 2 m:\n'
                         'Force needed = weight = 5 × 9.8 = 49 N\n'
                         'Work done = 49 × 2 = 98 J\n'
                         'This equals the GPE gained (Ep = mgh = 5 × 9.8 × 2 = 98 J) ✓\n'
                         '\n'
                         'FRICTION AND WORK:\n'
                         'Friction always acts OPPOSITE to motion — it always does NEGATIVE work on moving objects '
                         '(takes energy from kinetic store → thermal store).\n'
                         'This is why machines that involve friction always need a continuous energy input to keep '
                         'moving.',
              'heading': 'Joules and Newtons'}],
  'title': 'Work Done and Energy Transfer',
  'triple_only': None,
  'variables': [('W', 'Work done', 'joules', 'J'),
                ('F', 'Force', 'newtons', 'N'),
                ('s', 'Distance moved in direction of force', 'metres', 'm')]},
 {'common_mistake': 'Extension (e) is NOT the total length of the spring — it is the INCREASE in length from the '
                    'natural (unstretched) length. If a 10 cm spring stretches to 14 cm, e = 4 cm = 0.04 m.',
  'equations': ['F = k × e'],
  'fifas': [{'label': "Hooke's Law",
             'question': 'A spring with k = 80 N/m is stretched by 0.15 m. Calculate the force applied.',
             'steps': [('F', 'F = k × e'),
                       ('I', 'k = 80 N/m, e = 0.15 m'),
                       ('F', 'F = 80 × 0.15'),
                       ('A', 'F = 12 N')]}],
  'higher': None,
  'id': 'forces-elasticity',
  'key_note': "Hooke's Law: F = ke. k = spring constant (N/m), stiffness. Extension = increase in length (not total "
              "length). Elastic limit: beyond this, Hooke's Law breaks down — graph curves. Elastic deformation: "
              'returns to shape. Inelastic: permanent. RP18: force–extension graph, gradient = k.',
  'matching': {'instruction': 'Match each scenario to the correct force or extension.',
               'pairs': [('F = 10 N', 'Spring k = 50 N/m, extension = 0.2 m — F = ke = 50 × 0.2'),
                         ('e = 0.05 m', 'Spring k = 200 N/m, force = 10 N — e = F/k = 10/200'),
                         ('Elastic limit exceeded',
                          "Graph of F vs e curves away from straight line — Hooke's Law no longer obeyed"),
                         ('Inelastic deformation',
                          'Spring stretched beyond elastic limit — does not return to original length')],
               'title': "Hooke's Law"},
  'quiz': [{'opts': [('50 N/m — extension = 16 − 10 = 6 cm = 0.06 m; k = F/e = 3/0.06 = 50 N/m', True),
                     ('18.75 N/m — k = F/total length = 3/0.16', False),
                     ('0.02 N/m — k = e/F = 0.06/3', False),
                     ('300 N/m — k = F/e = 3/0.01 (used 1 cm extension)', False)],
            'q': 'A spring of natural length 10 cm is stretched to 16 cm by a 3 N force. What is the spring constant?',
            'wrong_explanations': {1: 'Extension is NOT the total length — it is the INCREASE: 16 − 10 = 6 cm. k = '
                                      '3/0.16 uses total length incorrectly.',
                                   2: 'k = F/e, not e/F. 0.06/3 gives m/N — not N/m.',
                                   3: 'Extension = 6 cm = 0.06 m, not 0.01 m (1 cm). k = 3/0.06 = 50 N/m.'}},
           {'opts': [('Applying only one force would make the rubber band accelerate — two equal opposite forces are '
                      'needed to deform it without moving it',
                      True),
                     ('One force is not strong enough — two forces together provide double the stretching force',
                      False),
                     ('Rubber bands only deform with two forces — a single force has no effect on elastic materials',
                      False),
                     ('The rubber band needs forces from both sides to stay in equilibrium while stretching', False)],
            'q': 'Why do you need to pull both ends of a rubber band to stretch it?',
            'wrong_explanations': {1: "Two forces DON'T double the stretching — you still only apply one extension. "
                                      "The reason is Newton's First Law — a single force would cause acceleration, not "
                                      'deformation.',
                                   2: 'A single force CAN stretch an elastic material if one end is fixed — but then '
                                      "the fixed end provides the second force via Newton's Third Law.",
                                   3: 'Equilibrium (resultant = 0) IS the right idea here — for deformation without '
                                      'acceleration, net force on the object must be zero.'}}],
  'rp': 'RP18 (Physics) — Investigate force–extension relationship for a spring. Add masses, measure extension. Plot F '
        'vs e graph. Find k from gradient. Identify elastic limit.',
  'spec': '6.5.3',
  'summary': "Apply Hooke's Law to springs and distinguish elastic from inelastic deformation.",
  'theory': [{'content': 'When a force is applied to a spring (or elastic material), it STRETCHES or COMPRESSES.\n'
                         '\n'
                         "HOOKE'S LAW:\n"
                         'Within the ELASTIC LIMIT, extension is DIRECTLY PROPORTIONAL to the applied force.\n'
                         '\n'
                         'EQUATION:\n'
                         'F = k × e\n'
                         '\n'
                         'F = force applied (newtons, N)\n'
                         'k = spring constant (N/m) — stiffness of the spring\n'
                         'e = extension (metres, m) — increase in length from natural length\n'
                         '\n'
                         'A STIFFER spring has a LARGER k value — more force needed per metre of extension.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'A spring with k = 50 N/m is stretched by 0.2 m:\n'
                         'F = 50 × 0.2 = 10 N\n'
                         '\n'
                         'Rearranging:\n'
                         'e = F ÷ k\n'
                         'k = F ÷ e',
              'heading': "Hooke's Law"},
             {'content': 'FORCE-EXTENSION GRAPH for a spring:\n'
                         'X-axis: extension (m). Y-axis: force (N).\n'
                         '\n'
                         'LINEAR (STRAIGHT) SECTION:\n'
                         "Obeys Hooke's Law — force proportional to extension.\n"
                         'Gradient = spring constant k = F ÷ e.\n'
                         '\n'
                         'BEYOND THE ELASTIC LIMIT:\n'
                         'Graph curves — no longer proportional.\n'
                         'Larger extension per unit force.\n'
                         '\n'
                         'RETURN BEHAVIOUR:\n'
                         'ELASTIC deformation: spring returns to original length when force removed.\n'
                         'INELASTIC deformation: spring does NOT return to original length — permanently stretched.\n'
                         'The elastic limit is the point beyond which deformation becomes inelastic.\n'
                         '\n'
                         'REQUIRED PRACTICAL (RP18):\n'
                         'Add masses to a spring. Measure extension at each mass.\n'
                         'Plot force vs extension. Find spring constant from gradient.\n'
                         "Identify where Hooke's Law is obeyed and where it breaks down.",
              'heading': 'Force–Extension Graphs'},
             {'content': 'To change the SHAPE of an object, MORE THAN ONE FORCE must be applied.\n'
                         '\n'
                         'Reason: if only one force is applied, the object would accelerate in that direction instead '
                         'of deforming.\n'
                         'Two equal and opposite forces are needed to stretch, compress or bend an object.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Stretching a rubber band: you pull both ends — two forces in opposite directions.\n'
                         'Compressing a spring: push both ends together — two forces towards each other.\n'
                         '\n'
                         'STORAGE OF ELASTIC PE:\n'
                         'A stretched spring stores elastic potential energy:\n'
                         'Ee = ½ × k × e²\n'
                         '\n'
                         'All the work done stretching the spring (within elastic limit) is stored as Ee.\n'
                         'When released, this converts to kinetic energy.\n'
                         '\n'
                         'APPLICATIONS:\n'
                         'Springs in mattresses, car suspensions, watches, catapults, archery bows.\n'
                         'Elastic bands, bungee cords, rubber in tyres.',
              'heading': 'More Than One Force Needed'}],
  'title': 'Forces and Elasticity',
  'triple_only': None,
  'variables': [('F', 'Force', 'newtons', 'N'),
                ('k', 'Spring constant', 'N/m', 'N/m'),
                ('e', 'Extension', 'metres', 'm')]},
 {'common_mistake': 'Distance in moments must be the PERPENDICULAR distance from the line of action of the force to '
                    'the pivot — not the distance along the lever. For the principle of moments, the object must be in '
                    'equilibrium (balanced and not rotating).',
  'equations': ['M = F × d', 'Principle of moments: Σ clockwise moments = Σ anticlockwise moments'],
  'fifas': [{'label': 'Moment Calculation',
             'question': 'A 300 N person sits 2 m to the right of a seesaw pivot. How far to the left must an 400 N '
                         'person sit to balance?',
             'steps': [('F', 'Principle of moments: clockwise moments = anticlockwise moments → F₁ × d₁ = F₂ × d₂'),
                       ('I', '300 × 2 = 400 × d₂'),
                       ('F', '600 = 400 × d₂ → d₂ = 600 ÷ 400'),
                       ('A', 'd₂ = 1.5 m')]}],
  'higher': None,
  'id': 'moments-levers-gears',
  'key_note': 'Moment = F × d (N·m). Principle of moments: clockwise = anticlockwise for equilibrium. Levers: force '
              'multipliers — small force × long distance = large force × short distance. Gears: large driven by small '
              '= more force, less speed; small driven by large = more speed, less force. Gear ratio = teeth_driven ÷ '
              'teeth_driving.',
  'matching': {'instruction': 'Match each scenario to the correct moment or principle.',
               'pairs': [('20 N·m', '50 N force applied 0.4 m from pivot — M = 50 × 0.4'),
                         ('Principle of moments (equilibrium)',
                          'Total clockwise moments = total anticlockwise moments'),
                         ('Force multiplier (lever)',
                          'Small input force × long distance = large output force × short distance'),
                         ('Large gear driven by small gear',
                          'Output rotates slower but with more turning force (torque)')],
               'title': 'Moments and Levers'},
  'quiz': [{'opts': [('20 N·m — M = F × d = 40 × 0.5 = 20 N·m', True),
                     ('80 N·m — M = F ÷ d = 40 ÷ 0.5 = 80', False),
                     ('40.5 N·m — M = F + d = 40 + 0.5', False),
                     ('0.0125 N·m — M = d ÷ F = 0.5 ÷ 40', False)],
            'q': 'A force of 40 N is applied 0.5 m from a pivot. What is the moment?',
            'wrong_explanations': {1: 'M = F ÷ d gives the force needed to produce a given moment at that distance — '
                                      'not the moment itself.',
                                   2: 'Adding force and distance gives meaningless units — M = F × d = 40 × 0.5 = 20 '
                                      'N·m.',
                                   3: 'M = d ÷ F inverts the relationship — M = F × d = 40 × 0.5 = 20 N·m.'}},
           {'opts': [('The back wheel turns slowly but with more turning force — useful for climbing hills', True),
                     ('The back wheel turns faster than the pedals — useful for high speeds', False),
                     ('The wheel and pedals turn at the same speed — no mechanical advantage', False),
                     ('The force decreases and speed increases — gears always trade force for speed', False)],
            'q': 'A bicycle is in a low gear — a small driving gear meshes with a large driven gear. What is the '
                 'effect?',
            'wrong_explanations': {1: 'Small driving → large driven gear gives MORE SPEED not more force. Low gear = '
                                      'large driving sprocket (at pedals) → small sprocket (at wheel) in cycling, OR '
                                      'equivalently small driving → large driven output.',
                                   2: 'Equal speeds = gear ratio of 1 — this is only when gears are identical.',
                                   3: 'Gears CAN either trade force for speed OR speed for force — it depends on which '
                                      'gear is driving which.'}}],
  'rp': None,
  'spec': '6.5.3 (physics only)',
  'summary': 'Calculate moments, apply the principle of moments and describe levers and gears as force multipliers.',
  'theory': [{'content': 'A MOMENT is the turning effect of a force about a pivot.\n'
                         '\n'
                         'EQUATION:\n'
                         'Moment = Force × perpendicular distance from the pivot\n'
                         'M = F × d\n'
                         '\n'
                         'M = moment (newton-metres, N·m)\n'
                         'F = force (newtons, N)\n'
                         'd = perpendicular distance from line of action of force to pivot (metres, m)\n'
                         '\n'
                         'Direction:\n'
                         'CLOCKWISE moment: force tends to turn the object clockwise.\n'
                         'ANTICLOCKWISE moment: force tends to turn the object anticlockwise.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'A 50 N force applied 0.4 m from a pivot:\n'
                         'M = 50 × 0.4 = 20 N·m\n'
                         '\n'
                         'LARGER MOMENT can be achieved by:\n'
                         'Increasing the FORCE, OR\n'
                         'Increasing the DISTANCE from the pivot.\n'
                         'This is why door handles are at the edge, not the hinge side.',
              'heading': 'Moments'},
             {'content': 'PRINCIPLE OF MOMENTS (equilibrium condition):\n'
                         'For an object in equilibrium, total clockwise moments = total anticlockwise moments about '
                         'any pivot.\n'
                         '\n'
                         'Σ(F × d) clockwise = Σ(F × d) anticlockwise\n'
                         '\n'
                         'EXAMPLE — balanced seesaw:\n'
                         'Child A (600 N) sits 1.5 m from pivot.\n'
                         'Clockwise moment = 600 × 1.5 = 900 N·m\n'
                         'Child B must produce 900 N·m anticlockwise.\n'
                         'If Child B weighs 450 N: distance = 900 ÷ 450 = 2 m from pivot.\n'
                         '\n'
                         'LEVERS as FORCE MULTIPLIERS:\n'
                         'A lever is a rigid rod that pivots about a fulcrum (pivot).\n'
                         'Small input force × long distance = large output force × short distance.\n'
                         'EXAMPLES: wheelbarrow, crowbar, scissors, tweezers, nutcracker, fishing rod.\n'
                         '\n'
                         'Different CLASSES of levers have pivot, effort and load in different positions:\n'
                         'Class 1: pivot between effort and load (seesaw, crowbar).\n'
                         'Class 2: load between pivot and effort (wheelbarrow, nutcracker).\n'
                         'Class 3: effort between pivot and load (tweezers, fishing rod).',
              'heading': 'Principle of Moments and Levers'},
             {'content': 'GEARS are toothed wheels that transmit force and rotation.\n'
                         '\n'
                         'How gears work:\n'
                         'Meshed gears rotate in OPPOSITE DIRECTIONS.\n'
                         'The teeth interlock — no slipping.\n'
                         '\n'
                         'GEAR RATIO:\n'
                         'Gear ratio = number of teeth on driven gear ÷ number of teeth on driving gear\n'
                         '\n'
                         'LARGE GEAR driven by SMALL GEAR:\n'
                         'Output gear rotates SLOWER but with MORE FORCE (torque).\n'
                         'Used to increase turning force — e.g. low gear in a car for acceleration.\n'
                         '\n'
                         'SMALL GEAR driven by LARGE GEAR:\n'
                         'Output gear rotates FASTER but with LESS FORCE.\n'
                         'Used to increase speed — e.g. high gear in a car at speed.\n'
                         '\n'
                         'GEARS AS FORCE MULTIPLIERS:\n'
                         'Like levers, gears convert a small force over a large rotation into a large force over a '
                         'small rotation (or vice versa).\n'
                         'Energy is conserved — work done is the same (ignoring friction).\n'
                         '\n'
                         'APPLICATIONS:\n'
                         'Bicycle gears — change between speed and force.\n'
                         'Car gearbox — match engine output to driving conditions.\n'
                         'Clocks — precise speed reduction from mainspring to hour hand.\n'
                         'Wind turbines — gearbox speeds up slow blade rotation for the generator.',
              'heading': 'Gears'}],
  'title': 'Moments, Levers and Gears',
  'triple_only': 'Moments, levers and gears (physics only) — not in Combined Science.',
  'variables': [('M', 'Moment', 'newton-metres', 'N·m'),
                ('F', 'Force', 'newtons', 'N'),
                ('d', 'Perpendicular distance from pivot', 'metres', 'm')]},
 {'common_mistake': 'Pressure in a fluid acts in ALL DIRECTIONS — not just downwards. P = hρg gives the ADDITIONAL '
                    'pressure due to the fluid depth — total pressure at depth includes atmospheric pressure too. '
                    'Upthrust equals the weight of DISPLACED fluid — not the weight of the whole object.',
  'equations': ['P = F ÷ A', 'P = h × ρ × g  (pressure at depth in a fluid)'],
  'fifas': [{'label': 'Fluid Pressure',
             'question': 'Calculate the pressure at 5 m depth in fresh water (ρ = 1000 kg/m³, g = 9.8 N/kg).',
             'steps': [('F', 'P = h × ρ × g'),
                       ('I', 'h = 5 m, ρ = 1000 kg/m³, g = 9.8 N/kg'),
                       ('F', 'P = 5 × 1000 × 9.8 = 49,000'),
                       ('A', 'P = 49,000 Pa = 49 kPa')]}],
  'higher': None,
  'id': 'pressure-in-a-fluid',
  'key_note': 'P = F/A. P = hρg — pressure increases with depth, density and g. Atmospheric pressure ~100 kPa at sea '
              'level, decreases with altitude. Upthrust = weight of displaced fluid (Archimedes). Float when upthrust '
              '≥ weight. Float if density < fluid density.',
  'matching': {'instruction': 'Match each scenario to the correct pressure concept.',
               'pairs': [('P = hρg', 'Pressure at depth h in a fluid of density ρ under gravity g'),
                         ('Atmospheric pressure', '~100 kPa at sea level — weight of air column above unit area'),
                         ('Upthrust', "Upward force = weight of fluid displaced (Archimedes' principle)"),
                         ('Object floats', 'Density of object < density of fluid — upthrust equals weight')],
               'title': 'Pressure in Fluids'},
  'quiz': [{'opts': [('More fluid above means a greater weight pressing down — the pressure equals the weight of fluid '
                      'per unit area above that point',
                      True),
                     ('Deeper water molecules move faster — increased kinetic energy creates higher pressure', False),
                     ('Fluid becomes denser at greater depth — denser fluid has higher pressure', False),
                     ('Gravity is stronger deeper underground — this increases pressure at depth', False)],
            'q': 'Why does pressure in a fluid increase with depth?',
            'wrong_explanations': {1: "Water molecules don't move significantly faster at greater depths — the "
                                      'pressure is due to the column of fluid weight above.',
                                   2: "Water is nearly incompressible — its density doesn't change significantly with "
                                      'depth in normal conditions.',
                                   3: 'Gravity is effectively constant for the depths relevant in GCSE — the '
                                      'increasing pressure comes from more fluid weight above.'}},
           {'opts': [('The hollow ship displaces a large volume of water — the upthrust (weight of displaced water) '
                      "equals the ship's weight",
                      True),
                     ('Salt water is denser than the steel in the hull — the extra density provides more upthrust',
                      False),
                     ("The ship's engine produces a downward thrust that reduces the net weight", False),
                     ('The shape of the hull creates lift, like an aeroplane wing in reverse', False)],
            'q': 'A steel ship floats in water even though steel is denser than water. Why?',
            'wrong_explanations': {1: "Steel is denser than salt water — the hull doesn't float because the water is "
                                      'denser than the hull material.',
                                   2: 'Engines produce forward thrust, not downward thrust — the ship floats due to '
                                      'displacement, not engine force.',
                                   3: "Hull shape does affect stability but ships primarily float due to Archimedes' "
                                      "principle — the hollow volume displaces water equal to the ship's weight."}}],
  'rp': None,
  'spec': '6.5.5 (physics only)',
  'summary': 'Calculate pressure in fluids, explain atmospheric pressure and describe pressure-depth relationships.',
  'theory': [{'content': 'PRESSURE in a fluid acts in ALL DIRECTIONS at any given point — not just downward.\n'
                         '\n'
                         'PRESSURE EQUATION:\n'
                         'P = F ÷ A\n'
                         '\n'
                         'P = pressure (pascals, Pa)\n'
                         'F = force (newtons, N)\n'
                         'A = area (m²)\n'
                         '\n'
                         '1 Pa = 1 N/m²\n'
                         '\n'
                         'PRESSURE INCREASES WITH DEPTH:\n'
                         'As depth increases → more fluid above → greater weight → greater pressure.\n'
                         '\n'
                         'EQUATION FOR FLUID PRESSURE:\n'
                         'P = h × ρ × g\n'
                         '\n'
                         'P = pressure (Pa)\n'
                         'h = depth (m)\n'
                         'ρ = density of fluid (kg/m³)\n'
                         'g = gravitational field strength (N/kg)\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Pressure at 10 m depth in seawater (ρ = 1025 kg/m³, g = 9.8 N/kg):\n'
                         'P = 10 × 1025 × 9.8 = 100,450 Pa ≈ 100 kPa',
              'heading': 'Pressure in Fluids'},
             {'content': 'ATMOSPHERIC PRESSURE is caused by the weight of the air column above any point.\n'
                         '\n'
                         'At sea level: approximately 101,325 Pa (about 100 kPa or 1 atm).\n'
                         'Atmospheric pressure DECREASES with altitude — less air above.\n'
                         '\n'
                         'WHY ATMOSPHERIC PRESSURE EXISTS:\n'
                         "The Earth's atmosphere has mass → gravity pulls it down.\n"
                         'At any point, the pressure equals the weight of the air column above per unit area.\n'
                         '\n'
                         'EFFECTS OF ATMOSPHERIC PRESSURE:\n'
                         'Suction cups: press cup against smooth surface, remove air → atmospheric pressure holds it '
                         'on.\n'
                         'Drinking through a straw: lungs create lower pressure → atmospheric pressure pushes drink '
                         'up.\n'
                         'Barometer: mercury column supported by atmospheric pressure.\n'
                         'Weather: high pressure = fair weather; low pressure = storms.\n'
                         '\n'
                         'VARIATION WITH ALTITUDE:\n'
                         'At 5500 m: pressure is approximately half sea-level.\n'
                         'At 10,000 m (cruising altitude): ~26 kPa → aircraft cabins pressurised.',
              'heading': 'Atmospheric Pressure'},
             {'content': 'UPTHRUST (buoyancy force): upward force on an object submerged in a fluid.\n'
                         '\n'
                         "ARCHIMEDES' PRINCIPLE:\n"
                         'Upthrust = weight of fluid displaced.\n'
                         '\n'
                         'FLOATING CONDITION:\n'
                         'Object floats when: upthrust = weight.\n'
                         'Object sinks when: weight > upthrust.\n'
                         '\n'
                         'PHYSICAL EXPLANATION:\n'
                         'Pressure at the bottom of a submerged object > pressure at the top.\n'
                         'Net upward force = pressure difference × area = weight of displaced fluid.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Ship: large volume of water displaced → large upthrust, even though ship is made of steel.\n'
                         'Hot air balloon: buoyancy in air — hot (less dense) air displaces cooler air → upthrust > '
                         'weight → rises.\n'
                         'Diver with wetsuit: carefully balanced to achieve neutral buoyancy.\n'
                         '\n'
                         'DENSITY AND FLOATING:\n'
                         'Object floats if density < fluid density.\n'
                         'Object sinks if density > fluid density.\n'
                         'Example: ice (917 kg/m³) floats on water (1000 kg/m³).',
              'heading': 'Upthrust and Floating'}],
  'title': 'Pressure in a Fluid',
  'triple_only': 'Pressure in a fluid (physics only) — not in Combined Science.',
  'variables': [('P', 'Pressure', 'pascals', 'Pa'),
                ('F', 'Force', 'newtons', 'N'),
                ('A', 'Area', 'm²', 'm²'),
                ('h', 'Depth', 'metres', 'm'),
                ('ρ', 'Density', 'kg/m³', 'kg/m³')]},
 {'common_mistake': 'Speed is scalar (magnitude only). Velocity is vector (magnitude AND direction). A car travelling '
                    'in a circle at constant SPEED has changing VELOCITY — direction is always changing. Average speed '
                    '= total distance ÷ total time (not displacement).',
  'equations': ['v = d ÷ t  (average speed)'],
  'fifas': [{'label': 'Speed Calculation',
             'question': 'A car travels 450 m in 30 s. Calculate its average speed.',
             'steps': [('F', 'v = d ÷ t'), ('I', 'd = 450 m, t = 30 s'), ('F', 'v = 450 ÷ 30'), ('A', 'v = 15 m/s')]}],
  'higher': None,
  'id': 'distance-speed-velocity',
  'key_note': 'Distance: scalar, total path. Displacement: vector, start to finish with direction. Speed = d/t '
              '(scalar). Velocity = displacement/t (vector). Speed = |velocity| for straight-line motion. Constant '
              'speed in a circle = changing velocity. Average speed: total distance ÷ total time.',
  'matching': {'instruction': 'Match each calculation or concept to the correct value or description.',
               'pairs': [('Speed = 5 m/s', 'Travels 100 m in 20 s — v = 100 ÷ 20 = 5 m/s'),
                         ('Velocity = 0 m/s', 'Walks 400 m around a circular track and returns to start in 200 s'),
                         ('Distance = 7 m', 'Walks 3 m north and 4 m east — total path length = 3 + 4'),
                         ('Changing velocity',
                          'Car driving in a circle at constant speed — direction (and therefore velocity) changes')],
               'title': 'Distance, Speed, Velocity'},
  'quiz': [{'opts': [('Speed = 10 m/s, velocity = 0 m/s — total distance = 1200 m, total time = 120 s; displacement = '
                      '0',
                      True),
                     ('Speed = 0 m/s, velocity = 10 m/s — velocity and speed are the same thing', False),
                     ('Both 10 m/s — displacement equals total distance', False),
                     ('Speed = 5 m/s, velocity = 5 m/s — average of 600 m in 60 s both ways', False)],
            'q': 'A cyclist rides 600 m east in 60 s, then 600 m west in 60 s. What is the average speed and average '
                 'velocity for the whole journey?',
            'wrong_explanations': {1: 'Speed and velocity are NOT the same — speed is scalar (total distance/time), '
                                      'velocity is vector (displacement/time).',
                                   2: 'Displacement = net change in position = 0 (back at start). Speed uses total '
                                      'distance (1200 m), velocity uses displacement (0 m).',
                                   3: 'Speed = total distance / total time = 1200/120 = 10 m/s, not 5 m/s.'}},
           {'opts': [('No — direction changes continuously around the roundabout, so velocity (which includes '
                      'direction) is always changing',
                      True),
                     ('Yes — speed is constant at 10 m/s, so velocity must also be constant', False),
                     ('Yes — velocity is always 10 m/s regardless of direction', False),
                     ('No — the car is accelerating because it is going around a circle', False)],
            'q': 'A car drives around a roundabout at constant speed of 10 m/s. Is its velocity constant?',
            'wrong_explanations': {1: 'Speed is scalar and CAN be constant — velocity is vector and changes when '
                                      'direction changes.',
                                   2: '10 m/s is speed — velocity = 10 m/s north, then 10 m/s northeast, etc. The '
                                      'direction changes.',
                                   3: 'Option D is actually CORRECT (circular motion does involve acceleration) — but '
                                      "the reason given (acceleration) is a consequence, not the answer to 'is "
                                      "velocity constant?'. The primary answer is that direction changes."}}],
  'rp': None,
  'spec': '6.5.4.1.1–6.5.4.1.3',
  'summary': 'Define and calculate distance, displacement, speed and velocity.',
  'theory': [{'content': 'DISTANCE: total length of path travelled — scalar (no direction).\n'
                         'DISPLACEMENT: straight-line distance from start to finish with direction — vector.\n'
                         '\n'
                         'Example:\n'
                         ' Walk 3 m north then 4 m east:\n'
                         'Distance = 3 + 4 = 7 m\n'
                         'Displacement = √(3² + 4²) = 5 m (north-east) — Pythagoras\n'
                         '\n'
                         'For motion in a straight line in ONE direction:\n'
                         'Distance = displacement (they are numerically equal).\n'
                         'For motion that changes direction: distance > |displacement|.',
              'heading': 'Distance and Displacement'},
             {'content': 'SPEED is the rate of change of distance — scalar quantity.\n'
                         '\n'
                         'EQUATION:\n'
                         'v = d ÷ t (for uniform/average speed)\n'
                         '\n'
                         'v = speed (m/s)\n'
                         'd = distance (m)\n'
                         't = time (s)\n'
                         '\n'
                         'Typical speeds:\n'
                         'Walking: ~1.5 m/s\n'
                         'Running: ~3 m/s\n'
                         'Cycling: ~6 m/s\n'
                         'Car on motorway: ~30 m/s\n'
                         'Speed of sound in air: ~340 m/s\n'
                         'Speed of light in vacuum: 3 × 10⁸ m/s\n'
                         '\n'
                         'SPEED IS NOT CONSTANT in most real motion — the equation gives AVERAGE speed.\n'
                         '\n'
                         'UNIT CONVERSIONS:\n'
                         '1 m/s = 3.6 km/h\n'
                         '30 m/s ≈ 108 km/h',
              'heading': 'Speed'},
             {'content': 'VELOCITY is the rate of change of displacement — vector quantity.\n'
                         '\n'
                         'velocity = displacement ÷ time\n'
                         '\n'
                         'Velocity has the SAME MAGNITUDE as speed when moving in a straight line.\n'
                         'Velocity DIFFERS from speed when direction changes.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'A car drives 100 m north in 10 s → velocity = 10 m/s north, speed = 10 m/s.\n'
                         'A car drives 100 m north then 100 m south in 20 s total:\n'
                         'Speed = 200/20 = 10 m/s\n'
                         'Velocity = 0/20 = 0 m/s (back at start → displacement = 0)\n'
                         '\n'
                         'CHANGING VELOCITY:\n'
                         'Velocity changes when speed changes OR when direction changes.\n'
                         'A car going around a bend at constant speed has CHANGING VELOCITY (direction changes).\n'
                         'Changing velocity = acceleration.',
              'heading': 'Velocity'}],
  'title': 'Distance, Speed and Velocity',
  'triple_only': None,
  'variables': [('v', 'Speed or velocity', 'm/s', 'm/s'),
                ('d', 'Distance', 'metres', 'm'),
                ('s', 'Displacement', 'metres', 'm'),
                ('t', 'Time', 'seconds', 's')]},
 {'common_mistake': 'A FLAT (horizontal) section means the object is STATIONARY — not moving at constant speed. '
                    'Constant speed gives a diagonal straight line. A steeper line means FASTER speed.',
  'equations': ['Speed = gradient of distance–time graph = Δd ÷ Δt'],
  'fifas': [{'label': 'Speed from d–t Graph',
             'question': 'A d–t graph shows an object moving from 0 m to 60 m in the first 12 seconds. Calculate the '
                         'speed.',
             'steps': [('F', 'Speed = gradient = Δd ÷ Δt'),
                       ('I', 'Δd = 60 − 0 = 60 m, Δt = 12 − 0 = 12 s'),
                       ('F', 'Speed = 60 ÷ 12'),
                       ('A', 'Speed = 5 m/s')]}],
  'higher': None,
  'id': 'distance-time-graphs',
  'key_note': 'Gradient of d–t graph = speed. Steep straight line = fast constant speed. Flat line = stationary. Curve '
              '= changing speed (accelerating or decelerating). Negative gradient = returning to start. Calculate '
              'speed: pick two points, speed = Δd/Δt.',
  'matching': {'instruction': 'Match each section of a d–t graph to the motion it represents.',
               'pairs': [('Steep straight line upward', 'Fast constant speed away from start'),
                         ('Horizontal flat line', 'Stationary — object has stopped'),
                         ('Gentle straight line upward', 'Slow constant speed away from start'),
                         ('Straight line downward', 'Constant speed returning towards starting point'),
                         ('Upward curve (increasing steepness)', 'Accelerating — speed increasing over time')],
               'title': 'Distance–Time Graph Sections'},
  'quiz': [{'opts': [('The object is stationary — no change in distance means zero speed', True),
                     ('The object is moving at constant speed — horizontal means steady motion', False),
                     ('The object is accelerating — the line is preparing to slope upward', False),
                     ('The object has reached maximum speed and is maintaining it', False)],
            'q': 'A d–t graph shows a horizontal (flat) line for 5 seconds. What is the object doing?',
            'wrong_explanations': {1: 'A horizontal line on a VELOCITY–time graph means constant velocity — but on a '
                                      'DISTANCE–time graph it means zero speed (stationary).',
                                   2: 'Flat line = zero gradient = zero speed. Constant speed on a d–t graph is a '
                                      'SLOPED straight line.',
                                   3: 'Acceleration on a d–t graph shows as a CURVE (increasing gradient) — not a flat '
                                      'section.'}},
           {'opts': [('Section A — steeper gradient on a d–t graph means higher speed', True),
                     ('Section B — less steep means the object is working harder to maintain motion', False),
                     ('They are the same speed — both are straight lines', False),
                     ('Section B — a gentler slope indicates faster, more efficient motion', False)],
            'q': 'On a distance–time graph, two straight sections are drawn. Section A has gradient 8 m/s and section '
                 'B has gradient 2 m/s. Which section shows faster motion?',
            'wrong_explanations': {1: 'Gentler slope does not imply harder work — gradient directly equals speed on a '
                                      'd–t graph.',
                                   2: 'Both are straight lines (constant speed) but at DIFFERENT speeds — the gradient '
                                      'value gives the speed.',
                                   3: 'Gentle slope = smaller gradient = slower speed. Fast motion = steeper slope = '
                                      'larger gradient.'}}],
  'rp': None,
  'spec': '6.5.4.1.4',
  'summary': 'Interpret distance–time graphs and calculate speed from the gradient.',
  'theory': [{'content': 'A DISTANCE–TIME GRAPH shows distance from a reference point (y-axis) against time (x-axis).\n'
                         '\n'
                         'GRADIENT = SPEED:\n'
                         'Steeper gradient → faster speed.\n'
                         'Flat (horizontal) line → stationary (speed = 0).\n'
                         'Downward slope → returning towards start.\n'
                         '\n'
                         'UNIFORM MOTION (constant speed): straight line with constant gradient.\n'
                         'NON-UNIFORM MOTION (changing speed): curved line — gradient changes.\n'
                         '\n'
                         'CALCULATING SPEED FROM GRADIENT:\n'
                         'speed = Δd ÷ Δt = (change in distance) ÷ (change in time)\n'
                         'Pick two clear points on the line and divide the vertical change by the horizontal change.',
              'heading': 'Reading Distance–Time Graphs'},
             {'content': "STATIONARY: horizontal straight line (distance doesn't change).\n"
                         'CONSTANT SPEED: straight line with positive gradient.\n'
                         'ACCELERATING: curve with increasing gradient (getting steeper).\n'
                         'DECELERATING: curve with decreasing gradient (getting shallower).\n'
                         'RETURNING: line going back down — distance from starting point decreasing.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Graph shows: 0–4 s: straight line to 20 m (constant speed).\n'
                         '4–6 s: horizontal (stationary).\n'
                         '6–10 s: straight line back to 0 m.\n'
                         '\n'
                         'Speed in first section: 20 m ÷ 4 s = 5 m/s\n'
                         'Speed stationary: 0 m/s\n'
                         'Return speed: 20 m ÷ 4 s = 5 m/s',
              'heading': 'Different Motion Shapes'},
             {'content': 'EXAM TECHNIQUE:\n'
                         'Always use a large triangle when calculating gradient — minimises reading errors.\n'
                         'Read coordinates from the axis, not from the line itself if possible.\n'
                         'Check units — distance in metres, time in seconds → speed in m/s.\n'
                         '\n'
                         'TANGENT TRICK (Higher Tier):\n'
                         'For a curved distance–time graph, draw a tangent at the point of interest.\n'
                         'Gradient of tangent = instantaneous speed at that point.\n'
                         '\n'
                         'FOUNDATION LEVEL:\n'
                         'Only need to find average speed from a straight-line section.\n'
                         'Describe the motion from different sections of the graph.',
              'heading': 'Using the Graph'}],
  'title': 'Distance–Time Graphs',
  'triple_only': None,
  'variables': [('v', 'Speed', 'm/s', 'm/s'), ('d', 'Distance', 'metres', 'm'), ('t', 'Time', 'seconds', 's')]},
 {'common_mistake': 'Gradient of a v–t graph = ACCELERATION (not distance or speed). Area under a v–t graph = '
                    "DISTANCE. This is the opposite of the d–t graph where gradient = speed. Don't confuse the two "
                    'graphs.',
  'equations': ['a = (v − u) ÷ t', 'v² = u² + 2as'],
  'fifas': [{'label': 'Acceleration',
             'question': 'A train accelerates from rest to 50 m/s in 25 s. Calculate the acceleration.',
             'steps': [('F', 'a = (v − u) ÷ t'),
                       ('I', 'v = 50 m/s, u = 0 m/s, t = 25 s'),
                       ('F', 'a = (50 − 0) ÷ 25 = 50 ÷ 25'),
                       ('A', 'a = 2 m/s²')]}],
  'higher': None,
  'id': 'acceleration',
  'key_note': 'a = (v−u)/t. v² = u² + 2as. Units: m/s². Positive a = speeding up; negative a = decelerating. v–t '
              'graph: gradient = acceleration; area = distance. Horizontal v–t = constant velocity. Steep v–t = large '
              'acceleration.',
  'matching': {'instruction': 'Match each scenario to the correct acceleration or distance.',
               'pairs': [('4 m/s²', 'Velocity increases from 10 m/s to 30 m/s in 5 s — a = 20÷5'),
                         ('−2 m/s²', 'Car decelerates from 20 m/s to 0 in 10 s — a = −20÷10'),
                         ('Area = distance', 'The area under a velocity–time graph gives distance travelled'),
                         ('Gradient = acceleration', 'The gradient of a velocity–time graph gives acceleration')],
               'title': 'Acceleration Calculations'},
  'quiz': [{'opts': [('−2 m/s² — a = (6−24)÷9 = −18÷9 = −2 m/s² (negative = deceleration)', True),
                     ('2 m/s² — ignoring the sign of deceleration', False),
                     ('−3.3 m/s² — a = (6−24)÷(6+3) using wrong time', False),
                     ('−18 m/s² — a = v − u without dividing by t', False)],
            'q': 'A car decelerates from 24 m/s to 6 m/s in 9 s. What is the acceleration?',
            'wrong_explanations': {1: 'The magnitude is correct (2 m/s²) but the SIGN matters: deceleration is '
                                      'negative acceleration. a = (v−u)/t = (6−24)/9 = −2 m/s².',
                                   2: 'This is not a standard calculation — t = 9 s must be used.',
                                   3: 'a = (v−u)/t = (6−24)/9 = −18/9 = −2. Must divide by time.'}},
           {'opts': [('72 m — area = base × height = 6 × 12 = 72 m', True),
                     ('2 m — gradient = 12/6 = 2 m/s² (used gradient formula)', False),
                     ('0 m — horizontal line means stationary on a v–t graph', False),
                     ('12 m — only reading the speed value, not calculating area', False)],
            'q': 'A v–t graph shows a straight horizontal line at 12 m/s for 6 seconds. What is the distance covered?',
            'wrong_explanations': {1: 'Gradient of a v–t graph gives ACCELERATION — 12/6 = 2 m/s². Distance comes from '
                                      'the AREA.',
                                   2: 'A horizontal line on a v–t graph means CONSTANT VELOCITY (not zero) — '
                                      'stationary would be v = 0.',
                                   3: '12 m/s is the velocity — to get distance, multiply by time: 12 × 6 = 72 m (or '
                                      'calculate area).'}}],
  'rp': None,
  'spec': '6.5.4.1.5',
  'summary': 'Calculate acceleration and use velocity–time graphs to describe and analyse motion.',
  'theory': [{'content': 'ACCELERATION is the rate of change of velocity.\n'
                         '\n'
                         'EQUATIONS:\n'
                         'a = Δv ÷ t = (v − u) ÷ t\n'
                         '\n'
                         'a = acceleration (m/s²)\n'
                         'v = final velocity (m/s)\n'
                         'u = initial velocity (m/s)\n'
                         't = time (s)\n'
                         '\n'
                         'Also: v² = u² + 2as (links velocity, acceleration and distance)\n'
                         '\n'
                         'a is positive → SPEEDING UP (in direction of motion).\n'
                         'a is negative → SLOWING DOWN (deceleration).\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Car accelerates from 10 m/s to 30 m/s in 5 s:\n'
                         'a = (30 − 10) ÷ 5 = 20 ÷ 5 = 4 m/s²\n'
                         '\n'
                         'NOTE: acceleration can occur even at constant speed if DIRECTION changes (circular motion).',
              'heading': 'Acceleration'},
             {'content': 'A VELOCITY–TIME GRAPH shows velocity (y-axis) against time (x-axis).\n'
                         '\n'
                         'GRADIENT = ACCELERATION:\n'
                         'Steep positive gradient → large acceleration.\n'
                         'Flat (horizontal) → constant velocity (zero acceleration).\n'
                         'Negative gradient → deceleration.\n'
                         '\n'
                         'AREA UNDER THE GRAPH = DISTANCE TRAVELLED:\n'
                         'For constant acceleration (straight line): area = ½ × base × height (triangle) + rectangle.\n'
                         'For horizontal section: area = base × height (rectangle).\n'
                         '\n'
                         'SHAPES:\n'
                         'Horizontal line → constant velocity.\n'
                         'Straight line up → constant acceleration.\n'
                         'Straight line down → constant deceleration.\n'
                         'Curved → changing acceleration.',
              'heading': 'Velocity–Time Graphs'},
             {'content': 'The equation v² = u² + 2as is useful when TIME is not given.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'A car starts from rest (u = 0) and accelerates at 3 m/s² over 75 m. Find the final speed.\n'
                         'v² = 0² + 2 × 3 × 75 = 450\n'
                         'v = √450 ≈ 21.2 m/s\n'
                         '\n'
                         'EXAMPLE 2:\n'
                         'Car moving at 20 m/s decelerates at 4 m/s² to a stop. Find the braking distance.\n'
                         'v = 0, u = 20 m/s, a = −4 m/s²\n'
                         '0 = 400 + 2 × (−4) × s\n'
                         '8s = 400\n'
                         's = 50 m\n'
                         '\n'
                         'CALCULATING DISTANCE FROM v–t GRAPH:\n'
                         'Distance = area under the v–t graph.\n'
                         'Use triangle area (½bh) for constant acceleration from rest.\n'
                         'Use trapezium area for constant acceleration with initial velocity.',
              'heading': 'Using v² = u² + 2as'}],
  'title': 'Acceleration',
  'triple_only': None,
  'variables': [('a', 'Acceleration', 'm/s²', 'm/s²'),
                ('v', 'Final velocity', 'm/s', 'm/s'),
                ('u', 'Initial velocity', 'm/s', 'm/s'),
                ('t', 'Time', 'seconds', 's'),
                ('s', 'Distance', 'metres', 'm')]},
 {'common_mistake': "Newton's Third Law pairs act on DIFFERENT objects — they cannot cancel. When a horse pulls a cart "
                    "(action), the cart pulls back on the horse (reaction). These don't cancel because they act on "
                    "different things. Newton's First Law is about ONE object — don't confuse the two.",
  'equations': ['F = m × a'],
  'fifas': [{'label': "Newton's Second Law",
             'question': 'A 900 kg car has a resultant forward force of 2700 N. Calculate its acceleration.',
             'steps': [('F', 'F = m × a, so a = F ÷ m'),
                       ('I', 'F = 2700 N, m = 900 kg'),
                       ('F', 'a = 2700 ÷ 900'),
                       ('A', 'a = 3 m/s²')]}],
  'higher': None,
  'id': 'newtons-laws',
  'key_note': 'N1: constant velocity (or stationary) if resultant = 0. N2: F = ma. N3: equal and opposite pairs on '
              'different objects. N2: bigger F → bigger a; bigger m → smaller a. N3 pairs: same type, same magnitude, '
              'opposite direction, different objects.',
  'matching': {'instruction': "Match each scenario to the Newton's Law it illustrates.",
               'pairs': [("Newton's First Law", 'Car at constant speed — resultant force is zero, velocity unchanged'),
                         ("Newton's Second Law",
                          'Pushing a heavier trolley requires more force for the same acceleration'),
                         ("Newton's Third Law", 'A swimmer pushes water backward — water pushes swimmer forward'),
                         ("Newton's Second Law", 'F = 1200 N, m = 600 kg → a = 1200/600 = 2 m/s²')],
               'title': "Newton's Laws"},
  'quiz': [{'opts': [('3000 N — F = m × a = 1500 × 2 = 3000 N', True),
                     ('750 N — F = m ÷ a = 1500 ÷ 2 = 750', False),
                     ('1502 N — F = m + a = 1500 + 2', False),
                     ('300 N — F = m × a ÷ 10 = 3000/10', False)],
            'q': 'A 1500 kg car accelerates at 2 m/s². What is the resultant force?',
            'wrong_explanations': {1: 'F = m ÷ a inverts the formula — F = m × a = 1500 × 2 = 3000 N.',
                                   2: 'Adding mass and acceleration gives meaningless units (kg + m/s²).',
                                   3: "There's no factor of 10 in F = ma — this confuses g with acceleration."}},
           {'opts': [('The table pushes UP on the book with 10 N — equal, opposite, on the table (reacting on the '
                      'book)',
                      True),
                     ('The normal contact force from the table pushing up on the book — this balances the weight',
                      False),
                     ("The Earth's gravity pulling the book down — the reaction to the normal force", False),
                     ('The book pushes down on the Earth through the table with 10 N', False)],
            'q': 'A book sits on a table. The book pushes down on the table with force 10 N (its weight). What is the '
                 "Newton's Third Law reaction to this?",
            'wrong_explanations': {1: "The normal force IS the Newton's Third Law reaction — but the question asks "
                                      'what force it is, and the key is it acts ON THE BOOK FROM THE TABLE. Option B '
                                      "describes it correctly but incorrectly labels it as 'balancing' — N3 pairs "
                                      "don't balance (they're on different objects).",
                                   2: "Earth's gravity on the book is a different force pair entirely (book pulls "
                                      "Earth up / Earth pulls book down). It's not the reaction to the normal contact "
                                      'force.',
                                   3: 'The book presses on the table (not directly on Earth) — and the N3 pair to '
                                      "'book pushes on table' is 'table pushes on book'. The chain to Earth involves "
                                      'more steps.'}}],
  'rp': None,
  'spec': '6.5.4.2.1–6.5.4.2.3',
  'summary': "State and apply Newton's three laws of motion.",
  'theory': [{'content': "NEWTON'S FIRST LAW:\n"
                         'An object will remain at rest or continue moving at CONSTANT VELOCITY unless acted upon by a '
                         'RESULTANT FORCE.\n'
                         '\n'
                         'In other words:\n'
                         'No resultant force → no change in motion.\n'
                         'A resultant force is needed to START, STOP or CHANGE THE DIRECTION of motion.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'A book on a table: weight balanced by normal force → resultant = 0 → stays still.\n'
                         'A puck on frictionless ice: no horizontal forces → moves in straight line forever.\n'
                         'A car at constant speed: driving force = friction + air resistance → resultant = 0 → '
                         'constant velocity.\n'
                         '\n'
                         'INERTIA:\n'
                         'The tendency of an object to resist changes in its motion.\n'
                         'Heavier (more massive) objects have more inertia — harder to accelerate or stop.',
              'heading': "Newton's First Law"},
             {'content': "NEWTON'S SECOND LAW:\n"
                         'The acceleration of an object is proportional to the resultant force and inversely '
                         'proportional to the mass.\n'
                         '\n'
                         'EQUATION:\n'
                         'F = m × a\n'
                         '\n'
                         'F = resultant force (newtons, N)\n'
                         'm = mass (kilograms, kg)\n'
                         'a = acceleration (m/s²)\n'
                         '\n'
                         'Rearranging:\n'
                         'a = F ÷ m\n'
                         'm = F ÷ a\n'
                         '\n'
                         'EXAMPLES:\n'
                         '1000 kg car, resultant force 3000 N:\n'
                         'a = 3000 ÷ 1000 = 3 m/s²\n'
                         '\n'
                         'Greater force → greater acceleration (for same mass).\n'
                         'Greater mass → smaller acceleration (for same force).',
              'heading': "Newton's Second Law"},
             {'content': "NEWTON'S THIRD LAW:\n"
                         'Whenever object A exerts a force on object B, object B exerts an equal and opposite force on '
                         'object A.\n'
                         '\n'
                         "Also called: 'action and reaction are equal and opposite'.\n"
                         '\n'
                         'Key features of Third Law pairs:\n'
                         'EQUAL in magnitude.\n'
                         'OPPOSITE in direction.\n'
                         'ACT ON DIFFERENT OBJECTS — they cannot cancel each other.\n'
                         'SAME TYPE of force.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Book on table: book pushes down on table (gravity transfers) → table pushes up on book '
                         '(normal force). Equal magnitude, opposite direction.\n'
                         'Rocket: rocket pushes exhaust gas backward → exhaust pushes rocket forward.\n'
                         'Swimmer pushes water backward → water pushes swimmer forward.\n'
                         'Earth pulls you down (gravity) → you pull Earth up (equally) but Earth barely moves '
                         '(enormous mass).\n'
                         '\n'
                         "IMPORTANT: Newton's Third Law pairs must be the same TYPE of force between the same two "
                         'objects.',
              'heading': "Newton's Third Law"}],
  'title': "Newton's Laws of Motion",
  'triple_only': None,
  'variables': [('F', 'Resultant force', 'newtons', 'N'),
                ('m', 'Mass', 'kilograms', 'kg'),
                ('a', 'Acceleration', 'm/s²', 'm/s²')]},
 {'common_mistake': 'Braking distance ∝ v² — doubling speed QUADRUPLES braking distance (not doubles). Thinking '
                    'distance is proportional to v (doubles when speed doubles). Students often mix up which factor '
                    'affects which component.',
  'equations': ['Stopping distance = thinking distance + braking distance',
                'Thinking distance = speed × reaction time',
                'Braking distance ∝ v²'],
  'fifas': [{'label': 'Stopping Distance',
             'question': 'A driver has reaction time 0.6 s and is driving at 20 m/s. The braking distance is 40 m. '
                         'Calculate the total stopping distance.',
             'steps': [('F',
                        'Stopping distance = thinking distance + braking distance; thinking distance = speed × '
                        'reaction time'),
                       ('I', 'Speed = 20 m/s, reaction time = 0.6 s, braking distance = 40 m'),
                       ('F', 'Thinking distance = 20 × 0.6 = 12 m'),
                       ('A', 'Stopping distance = 12 + 40 = 52 m')]}],
  'higher': None,
  'id': 'stopping-distance-braking',
  'key_note': 'Stopping distance = thinking + braking. Thinking distance affected by speed and reaction time (alcohol, '
              'drugs, tiredness, distraction). Braking distance affected by speed (∝v²), road conditions (wet/ice), '
              'tyre condition, brake condition, vehicle mass. Double speed → 4× braking distance.',
  'matching': {'instruction': 'Match each factor to thinking distance or braking distance.',
               'pairs': [('Thinking distance',
                          'Driver is tired — reaction time increases → more distance covered before braking'),
                         ('Thinking distance', 'Driving faster — same reaction time but higher speed → more distance'),
                         ('Braking distance', 'Wet road — reduced friction between tyres and surface'),
                         ('Braking distance', 'Bald tyres — less tread → reduced grip → longer distance to stop'),
                         ('Both increase', 'Higher speed — thinking distance ∝ v AND braking distance ∝ v²')],
               'title': 'Stopping Distance Factors'},
  'quiz': [{'opts': [('It quadruples — braking distance is proportional to v², so (20/10)² = 4 times longer', True),
                     ('It doubles — speed doubles so distance doubles', False),
                     ('It increases by 10 m — simple addition', False),
                     ('It stays the same — braking distance depends only on road conditions', False)],
            'q': "A car's speed doubles from 10 m/s to 20 m/s. How does the braking distance change?",
            'wrong_explanations': {1: "Braking distance ∝ v (not v²) would give doubling — but it's ∝ v², so doubling "
                                      'speed multiplies braking distance by 4.',
                                   2: 'Braking distance is not fixed — it depends on speed squared, road conditions '
                                      'and braking force.',
                                   3: 'Braking distance depends strongly on speed (∝v²) — doubling speed quadruples '
                                      'it, not keeps it constant.'}},
           {'opts': [('Alcohol increases reaction time — the driver takes longer to respond, so thinking distance '
                      'increases',
                      True),
                     ('Alcohol weakens muscles — the driver cannot press the brakes as hard, increasing braking '
                      'distance',
                      False),
                     ('Alcohol blurs vision — the driver takes longer to see the hazard and applies brakes later',
                      False),
                     ('Alcohol reduces vehicle mass — lighter car has less braking force available', False)],
            'q': 'Why does alcohol increase stopping distance?',
            'wrong_explanations': {1: 'While impaired vision and muscle weakness may play minor roles, the PRIMARY '
                                      'effect of alcohol on stopping distance is through REACTION TIME (thinking '
                                      'distance component).',
                                   2: 'Vision is relevant but the primary mechanism tested at GCSE is the effect on '
                                      'REACTION TIME specifically.',
                                   3: "Alcohol doesn't change vehicle mass — the driver's mass is a tiny fraction of "
                                      'the vehicle.'}}],
  'rp': None,
  'spec': '6.5.4.3',
  'summary': 'Define stopping distance and explain factors affecting thinking distance and braking distance.',
  'theory': [{'content': 'STOPPING DISTANCE = THINKING DISTANCE + BRAKING DISTANCE\n'
                         '\n'
                         'THINKING DISTANCE: distance travelled during the REACTION TIME of the driver (before brakes '
                         'are applied).\n'
                         'Thinking distance = speed × reaction time\n'
                         '\n'
                         'BRAKING DISTANCE: distance travelled from when brakes are APPLIED until the vehicle stops.\n'
                         '\n'
                         'EXAMPLE (typical values at 30 mph = 13.3 m/s):\n'
                         'Thinking distance ≈ 9 m\n'
                         'Braking distance ≈ 14 m\n'
                         'Stopping distance ≈ 23 m\n'
                         'At 60 mph: stopping distance ≈ 73 m (much more than double — braking distance increases with '
                         'v²)',
              'heading': 'Stopping Distance'},
             {'content': 'Thinking distance = reaction time × speed\n'
                         '\n'
                         'Thinking distance INCREASES with:\n'
                         'HIGHER SPEED — same reaction time but more distance covered.\n'
                         'IMPAIRED REACTION TIME due to:\n'
                         'ALCOHOL — slows nerve impulse transmission.\n'
                         'DRUGS (including some prescription medicines) — affect concentration and reaction.\n'
                         'TIREDNESS/FATIGUE — reduced alertness.\n'
                         'DISTRACTION — mobile phones, eating, passengers.\n'
                         '\n'
                         'TYPICAL REACTION TIME: 0.2–0.9 seconds (average ~0.7 s).\n'
                         '\n'
                         'MEASURING REACTION TIME:\n'
                         "Ruler drop test: drop a ruler through a person's fingers — measure how far it falls before "
                         'they catch it.\n'
                         'Electronic reaction time testers.\n'
                         'Computer-based tests.',
              'heading': 'Factors Affecting Thinking Distance'},
             {'content': 'Braking distance INCREASES with:\n'
                         'HIGHER SPEED — braking distance ∝ v² (doubling speed quadruples braking distance).\n'
                         'POOR ROAD CONDITIONS:\n'
                         'Wet road: less friction between tyres and road.\n'
                         'Icy road: dramatically less friction.\n'
                         'Loose gravel: tyres lose grip.\n'
                         'DEFECTIVE TYRES:\n'
                         'Bald tyres: little tread → reduced water dispersal → aquaplaning risk.\n'
                         'Under-inflated tyres: reduce contact area.\n'
                         'POOR BRAKES: worn brake pads, overheated brakes (brake fade).\n'
                         'HEAVY VEHICLE: more mass → more kinetic energy to remove → longer braking distance (for same '
                         'braking force).\n'
                         '\n'
                         'PHYSICS LINK:\n'
                         'Braking force does WORK to remove kinetic energy:\n'
                         'Work = F × d and Ek = ½mv²\n'
                         'F × d = ½mv²\n'
                         'So d = mv² ÷ (2F)\n'
                         'Braking distance ∝ v² — doubling speed quadruples braking distance.\n'
                         '\n'
                         'LARGE DECELERATIONS:\n'
                         'Hard braking → large deceleration → large forces on passengers.\n'
                         'Could cause injuries — seat belts and crumple zones reduce risk.',
              'heading': 'Factors Affecting Braking Distance'}],
  'title': 'Stopping Distance and Braking',
  'triple_only': None,
  'variables': []}],

"waves": [{'common_mistake': 'In a TRANSVERSE wave, the oscillation is PERPENDICULAR to the direction of travel — not parallel. '
                    'In a LONGITUDINAL wave (like sound), the oscillation is PARALLEL to the direction of travel. '
                    "Don't confuse the two.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'transverse-longitudinal-waves',
  'key_note': 'Waves transfer energy, not matter. Transverse: oscillation ⊥ direction (light, water ripples, EM '
              'waves). Longitudinal: oscillation ∥ direction (sound, ultrasound). Longitudinal shows compressions and '
              'rarefactions. Sound needs a medium; light does not.',
  'matching': {'instruction': 'Sort each wave into transverse or longitudinal.',
               'pairs': [('Transverse', 'Light — electric field oscillates perpendicular to direction of travel'),
                         ('Transverse', 'Water ripples — water surface moves up and down, wave moves horizontally'),
                         ('Longitudinal',
                          'Sound in air — air molecules compressed and rarefied in direction of travel'),
                         ('Longitudinal', 'Ultrasound — pressure waves with compressions and rarefactions'),
                         ('Transverse', 'All electromagnetic waves — can travel through a vacuum')],
               'title': 'Wave Types'},
  'quiz': [{'opts': [('Parallel — particles oscillate back and forth along the same direction as the wave travels',
                      True),
                     ('Perpendicular — particles oscillate at right angles to the wave direction', False),
                     ('They move with the wave — carried forward as the wave progresses', False),
                     ('They remain completely stationary — only energy travels', False)],
            'q': 'How do particles move in a longitudinal wave compared to the direction of wave travel?',
            'wrong_explanations': {1: 'PERPENDICULAR oscillation describes TRANSVERSE waves — in longitudinal waves, '
                                      'oscillation is parallel.',
                                   2: "Particles in a wave oscillate about their equilibrium position — they don't "
                                      'travel with the wave. This is the key distinction between wave motion and '
                                      'particle transport.',
                                   3: "Particles do move — they oscillate back and forth. They just don't travel with "
                                      'the wave as a whole.'}},
           {'opts': [('Light is a transverse electromagnetic wave — needs no medium. Sound is longitudinal and needs '
                      'particles to compress and rarefy.',
                      True),
                     ("Sound travels faster than light and 'uses up' the medium, leaving nothing for light", False),
                     ('Light is brighter than sound waves — intensity allows it to travel without a medium', False),
                     ('Sound is a transverse wave and cannot travel without a medium; light is longitudinal and can',
                      False)],
            'q': 'Why can light travel through a vacuum but sound cannot?',
            'wrong_explanations': {1: 'Light travels much FASTER than sound (3×10⁸ m/s vs ~340 m/s) — speed is '
                                      'irrelevant to whether a medium is needed.',
                                   2: 'Wave intensity is unrelated to whether a medium is required.',
                                   3: "It's the OPPOSITE: sound is LONGITUDINAL (needs medium); light is TRANSVERSE EM "
                                      'wave (no medium needed).'}}],
  'rp': 'RP19 (Physics) — Investigate the slinky spring to demonstrate transverse and longitudinal wave motion. RP20 — '
        'Ripple tank to observe wave properties.',
  'spec': '6.6.1.1',
  'summary': 'Describe transverse and longitudinal waves and give examples of each.',
  'theory': [{'content': 'A WAVE is a transfer of ENERGY from one place to another WITHOUT transferring matter.\n'
                         '\n'
                         "The particles (or fields) oscillate — they don't travel with the wave.\n"
                         'The WAVE PATTERN travels; the MEDIUM stays in place.\n'
                         '\n'
                         'Evidence:\n'
                         "Ripples on water: a floating cork bobs up and down but doesn't travel forward.\n"
                         "Sound wave: air molecules vibrate back and forth but don't travel with the sound.\n"
                         '\n'
                         'Waves transfer energy — this is why sound can move a speaker cone, light can heat objects, '
                         'and water waves erode cliffs.',
              'heading': 'What Is a Wave?'},
             {'content': 'TRANSVERSE WAVES: the oscillation (vibration) is PERPENDICULAR (at right angles) to the '
                         'direction of wave travel.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Light and all electromagnetic waves — electric and magnetic fields oscillate perpendicular '
                         'to travel direction.\n'
                         'Ripples on water surface — water moves up and down; wave travels horizontally.\n'
                         'Waves on a string or rope — string moves up and down; wave travels along the string.\n'
                         'Seismic S-waves.\n'
                         '\n'
                         'DRAWING: shows a sinusoidal wave — peaks and troughs.\n'
                         'The DISPLACEMENT of the medium is perpendicular to the direction of energy transfer.\n'
                         '\n'
                         'CAN travel through vacuum — light reaches us from the Sun through empty space.',
              'heading': 'Transverse Waves'},
             {'content': 'LONGITUDINAL WAVES: the oscillation is PARALLEL to (along the same direction as) the '
                         'direction of wave travel.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'SOUND waves in air (or any medium) — most important example.\n'
                         'Ultrasound — longitudinal pressure waves above 20,000 Hz.\n'
                         'Seismic P-waves.\n'
                         'Compression waves in a spring.\n'
                         '\n'
                         'MECHANISM:\n'
                         'Particles are pushed closer together (COMPRESSION) and pulled further apart (RAREFACTION) '
                         'alternately.\n'
                         'Compressions = high pressure regions. Rarefactions = low pressure regions.\n'
                         'The pattern of compressions and rarefactions travels forward — the particles only vibrate '
                         'back and forth.\n'
                         '\n'
                         'CANNOT travel through vacuum — sound needs a medium (particles to compress).\n'
                         'In space, no one can hear you scream.',
              'heading': 'Longitudinal Waves'}],
  'title': 'Transverse and Longitudinal Waves',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Amplitude is the distance from the equilibrium (centre) to the crest — NOT from crest to trough '
                    "(that's double the amplitude). Frequency and period are reciprocals: f = 1/T. Don't confuse "
                    'wavelength (one full cycle length) with amplitude (height from centre).',
  'equations': ['v = f × λ', 'T = 1 ÷ f'],
  'fifas': [{'label': 'Wave Equation',
             'question': 'A sound wave has frequency 500 Hz and travels at 340 m/s. Calculate its wavelength.',
             'steps': [('F', 'v = f × λ, so λ = v ÷ f'),
                       ('I', 'v = 340 m/s, f = 500 Hz'),
                       ('F', 'λ = 340 ÷ 500'),
                       ('A', 'λ = 0.68 m')]}],
  'higher': None,
  'id': 'properties-of-waves',
  'key_note': 'Amplitude: equilibrium to crest (m). Wavelength (λ): crest to crest (m). Frequency (f): waves per '
              'second (Hz). Period (T): seconds per wave. T = 1/f. v = fλ. EM waves in vacuum: 3×10⁸ m/s. Sound in '
              'air: ~340 m/s. RP19: measure wave speed in ripple tank.',
  'matching': {'instruction': 'Match each wave property to its definition and unit.',
               'pairs': [('Amplitude', 'Maximum displacement from equilibrium — measured in metres'),
                         ('Wavelength (λ)', 'Distance from one crest to the next — metres'),
                         ('Frequency (f)', 'Number of complete waves per second — hertz (Hz)'),
                         ('Period (T)', 'Time for one complete wave — seconds; T = 1/f'),
                         ('Wave speed (v)', 'v = f × λ — distance travelled per second in m/s')],
               'title': 'Wave Property Definitions'},
  'quiz': [{'opts': [('0.005 s — T = 1 ÷ f = 1 ÷ 200 = 0.005 s', True),
                     ('200 s — T = f = 200 s', False),
                     ('20 s — T = f ÷ 10', False),
                     ('0.1 s — T = 1/10 of the frequency', False)],
            'q': 'A wave has frequency 200 Hz. What is its period?',
            'wrong_explanations': {1: 'T is not equal to f — they are reciprocals: T = 1/f = 1/200 = 0.005 s.',
                                   2: 'T = 1/f not f/10.',
                                   3: 'T = 1/f only — T = 1/200 = 0.005 s.'}},
           {'opts': [('1 × 10⁸ Hz — f = v ÷ λ = 3×10⁸ ÷ 3 = 1×10⁸ Hz', True),
                     ('9 × 10⁸ Hz — f = v × λ = 3×10⁸ × 3', False),
                     ('1 × 10⁻⁸ Hz — f = λ ÷ v = 3 ÷ 3×10⁸', False),
                     ('3 × 10⁸ Hz — frequency equals wave speed for EM waves', False)],
            'q': 'A radio wave has wavelength 3 m. What is its frequency? (speed of EM waves = 3 × 10⁸ m/s)',
            'wrong_explanations': {1: 'f = v × λ multiplies rather than divides — must use f = v ÷ λ.',
                                   2: 'f = λ ÷ v inverts the rearrangement. f = v ÷ λ = 3×10⁸ ÷ 3 = 1×10⁸ Hz.',
                                   3: 'Wave speed and frequency are not the same — they are related by v = fλ.'}}],
  'rp': 'RP19 (Physics) — Measure the speed of waves in a ripple tank using v = fλ. Measure frequency and wavelength '
        'of waves. Also: measure speed of sound using microphones and oscilloscope.',
  'spec': '6.6.1.2',
  'summary': 'Define amplitude, wavelength, frequency, period and wave speed, and use v = fλ.',
  'theory': [{'content': 'KEY WAVE PROPERTIES:\n'
                         '\n'
                         'AMPLITUDE (A): maximum displacement of a particle from its equilibrium (undisturbed) '
                         'position.\n'
                         'Measured in metres (m). Relates to energy — larger amplitude = more energy.\n'
                         '\n'
                         'WAVELENGTH (λ, lambda): distance from one point on a wave to the equivalent point on the '
                         'next wave.\n'
                         'For example: crest to crest, or trough to trough, or compression to compression.\n'
                         'Measured in metres (m).\n'
                         '\n'
                         'FREQUENCY (f): number of complete waves passing a point per second.\n'
                         'Measured in HERTZ (Hz). 1 Hz = 1 complete wave per second.\n'
                         '\n'
                         'PERIOD (T): time for one complete wave to pass a point.\n'
                         'Measured in seconds (s).\n'
                         'Relationship: T = 1 ÷ f  (or f = 1 ÷ T)',
              'heading': 'Wave Properties'},
             {'content': 'WAVE SPEED EQUATION:\n'
                         'v = f × λ\n'
                         '\n'
                         'v = wave speed (m/s)\n'
                         'f = frequency (Hz)\n'
                         'λ = wavelength (m)\n'
                         '\n'
                         'Rearranging:\n'
                         'f = v ÷ λ\n'
                         'λ = v ÷ f\n'
                         '\n'
                         'EXAMPLE 1:\n'
                         'Sound wave: frequency 440 Hz, speed 340 m/s:\n'
                         'λ = 340 ÷ 440 = 0.77 m\n'
                         '\n'
                         'EXAMPLE 2:\n'
                         'EM wave: wavelength 0.1 m, speed 3 × 10⁸ m/s:\n'
                         'f = 3 × 10⁸ ÷ 0.1 = 3 × 10⁹ Hz = 3 GHz (microwave range)\n'
                         '\n'
                         'All EM waves travel at the SAME speed in vacuum: c = 3 × 10⁸ m/s.\n'
                         'Sound in air: ~340 m/s at room temperature.',
              'heading': 'The Wave Equation'},
             {'content': 'REQUIRED PRACTICAL (RP19) — Measure wave speed:\n'
                         '\n'
                         'METHOD 1 — Water waves (ripple tank):\n'
                         "Use a stroboscope to 'freeze' waves.\n"
                         'Measure wavelength from the still image.\n'
                         'Count frequency from the vibrating bar setting.\n'
                         'Calculate: v = fλ.\n'
                         '\n'
                         'METHOD 2 — Sound waves:\n'
                         'Connect a microphone to an oscilloscope.\n'
                         'Display the waveform — measure period T from the trace.\n'
                         'f = 1/T.\n'
                         'Using two microphones and measuring time delay to find speed.\n'
                         '\n'
                         'EXAM SKILL — reading oscilloscope traces:\n'
                         'Time per division (x-axis) → period T → frequency f = 1/T.\n'
                         'Volts per division (y-axis) → amplitude.',
              'heading': 'Measuring Wave Speed — Required Practical'}],
  'title': 'Properties of Waves',
  'triple_only': None,
  'variables': [('v', 'Wave speed', 'm/s', 'm/s'),
                ('f', 'Frequency', 'hertz', 'Hz'),
                ('λ', 'Wavelength', 'metres', 'm'),
                ('T', 'Period', 'seconds', 's'),
                ('A', 'Amplitude', 'metres', 'm')]},
 {'common_mistake': 'All EM waves travel at the SAME speed in vacuum (3 × 10⁸ m/s) — they differ only in wavelength '
                    'and frequency. Higher frequency = shorter wavelength = more energy per photon. Gamma rays are NOT '
                    'the same as X-rays — they come from different sources (nucleus vs electron deceleration).',
  'equations': ['c = f × λ  (for EM waves in vacuum, c = 3 × 10⁸ m/s)'],
  'fifas': [],
  'higher': None,
  'id': 'types-of-em-waves',
  'key_note': 'EM spectrum (long→short λ): radio, microwave, infrared, visible, UV, X-ray, gamma. All travel at 3×10⁸ '
              'm/s in vacuum. All transverse. Higher frequency = shorter λ = more energy. Visible: red (longest) to '
              'violet (shortest). Gamma from nucleus; X-rays from electron deceleration.',
  'matching': {'instruction': 'Match each EM wave type to its wavelength range or key property.',
               'pairs': [('Radio waves', 'Longest wavelength — used for communication, TV and radio broadcasts'),
                         ('Microwaves',
                          'Wavelength ~1 mm to 0.1 m — used in mobile phones, cooking, satellite communication'),
                         ('Infrared',
                          'Emitted by all warm objects — detected as heat; used in night vision and remote controls'),
                         ('Visible light',
                          '400 nm (violet) to 700 nm (red) — only part of EM spectrum detected by human eyes'),
                         ('Gamma rays', 'Shortest wavelength, highest energy — emitted by unstable atomic nuclei')],
               'title': 'EM Spectrum Order'},
  'quiz': [{'opts': [('Gamma rays — at the short-wavelength end of the spectrum; highest frequency and energy', True),
                     ('Radio waves — longest wavelength means highest frequency', False),
                     ('Visible light — humans evolved to see the most frequent EM radiation', False),
                     ('Microwaves — used in microwave ovens, must have highest energy', False)],
            'q': 'Which EM wave has the highest frequency?',
            'wrong_explanations': {1: 'Longest wavelength = LOWEST frequency (v = fλ — for constant v, f and λ are '
                                      'inversely proportional).',
                                   2: 'Visible light is a narrow band in the middle of the spectrum — far from the '
                                      'highest frequency.',
                                   3: "Microwave ovens work by matching the frequency to water molecules' resonant "
                                      'frequency, not because microwaves have the highest energy.'}},
           {'opts': [('Speed — all travel at 3 × 10⁸ m/s regardless of wavelength or frequency', True),
                     ('Wavelength — all EM waves have the same wavelength in vacuum', False),
                     ('Frequency — the frequency is constant for all EM waves', False),
                     ('Energy — all EM waves carry the same amount of energy', False)],
            'q': 'All electromagnetic waves in a vacuum have the same what?',
            'wrong_explanations': {1: 'EM waves vary enormously in wavelength — from >100 m (radio) to <0.01 nm '
                                      '(gamma).',
                                   2: 'Frequency varies inversely with wavelength for a given speed — radio (low f) to '
                                      'gamma (high f).',
                                   3: 'Energy per photon = hf — higher frequency EM waves carry more energy per '
                                      'photon.'}}],
  'rp': None,
  'spec': '6.6.2.1',
  'summary': 'Describe the electromagnetic spectrum and the properties all EM waves share.',
  'theory': [{'content': 'ELECTROMAGNETIC (EM) WAVES are transverse waves that transfer energy from source to '
                         'absorber.\n'
                         '\n'
                         'All EM waves:\n'
                         'Travel at the SAME SPEED in vacuum: c = 3 × 10⁸ m/s.\n'
                         'Are TRANSVERSE waves.\n'
                         'Can travel through a VACUUM (no medium needed).\n'
                         'Transfer ENERGY.\n'
                         '\n'
                         'EM waves form a CONTINUOUS SPECTRUM grouped by wavelength and frequency:\n'
                         '(longest wavelength / lowest frequency → shortest wavelength / highest frequency)\n'
                         '\n'
                         'RADIO WAVES → MICROWAVES → INFRARED → VISIBLE LIGHT → ULTRAVIOLET → X-RAYS → GAMMA RAYS\n'
                         '\n'
                         "Memory: 'Raging Martians Invaded Venus Using X-ray Guns'\n"
                         '\n'
                         'As you go from radio → gamma:\n'
                         'Wavelength DECREASES\n'
                         'Frequency INCREASES\n'
                         'Energy INCREASES (∝ frequency)',
              'heading': 'The Electromagnetic Spectrum'},
             {'content': 'Approximate ranges:\n'
                         '\n'
                         'RADIO WAVES: λ = 0.1 m to 10⁴ m; f = 30 MHz to 3 kHz\n'
                         'MICROWAVES: λ = 1 mm to 0.1 m; f = 300 MHz to 300 GHz\n'
                         'INFRARED: λ = 700 nm to 1 mm\n'
                         'VISIBLE LIGHT: λ = 400 nm (violet) to 700 nm (red)\n'
                         'ULTRAVIOLET: λ = 10 nm to 400 nm\n'
                         'X-RAYS: λ = 0.01 nm to 10 nm\n'
                         'GAMMA RAYS: λ < 0.01 nm; highest frequency and energy\n'
                         '\n'
                         'VISIBLE SPECTRUM (Roy G Biv):\n'
                         'Red → Orange → Yellow → Green → Blue → Indigo → Violet\n'
                         'Red has longest wavelength / lowest frequency in visible range.\n'
                         'Violet has shortest wavelength / highest frequency in visible range.',
              'heading': 'Wavelengths and Frequencies'},
             {'content': 'RADIO WAVES: produced by oscillating electrical circuits in transmitters.\n'
                         'MICROWAVES: produced by electronic devices; also by oscillating electrons.\n'
                         'INFRARED: emitted by all objects with temperature above absolute zero — thermal radiation.\n'
                         'VISIBLE LIGHT: produced by hot objects (incandescent), LEDs, fluorescent lamps.\n'
                         'ULTRAVIOLET: produced by very hot objects (the Sun), UV lamps.\n'
                         'X-RAYS: produced by decelerating high-energy electrons hitting a metal target.\n'
                         'GAMMA RAYS: emitted from unstable atomic nuclei during radioactive decay.\n'
                         '\n'
                         'All are produced by changes in energy levels of electrons OR by oscillating charges.\n'
                         'All travel at 3 × 10⁸ m/s in vacuum — but SLOWER in other materials.\n'
                         'Light slows down in glass → this causes refraction.',
              'heading': 'Sources and Properties'}],
  'title': 'Types of Electromagnetic Waves',
  'triple_only': None,
  'variables': [('c', 'Speed of EM waves in vacuum', 'm/s', '3 × 10⁸ m/s'),
                ('λ', 'Wavelength', 'metres', 'm'),
                ('f', 'Frequency', 'hertz', 'Hz')]},
 {'common_mistake': 'When light enters glass from air, it SLOWS DOWN and bends TOWARDS the normal (angle of refraction '
                    '< angle of incidence). When it leaves glass into air, it SPEEDS UP and bends AWAY from the '
                    'normal. Always identify which medium is faster/slower.',
  'equations': [],
  'fifas': [],
  'higher': 'Explain refraction in terms of velocity change: when wave enters denser medium, wavefronts slow and '
            'compress, causing a change in direction. Explain total internal reflection (TIR): when angle exceeds '
            'critical angle in a denser medium, all light reflects internally. Applications: optical fibres, diamond '
            'cut. Calculate critical angle: sin(c) = 1/n.',
  'id': 'properties-em-waves-1',
  'key_note': 'Refraction: change in direction due to change in speed at boundary. Air → glass (slower): bends towards '
              'normal. Glass → air (faster): bends away. Frequency constant; wavelength changes. Ray diagrams: '
              'incident ray, normal, refracted ray, angles of incidence and refraction.',
  'matching': {'instruction': 'Match each refraction scenario to the correct description.',
               'pairs': [('Air → glass', 'Wave slows down — bends towards the normal — angle of refraction smaller'),
                         ('Glass → air', 'Wave speeds up — bends away from the normal — angle of refraction larger'),
                         ('Along the normal (0°)', 'No refraction — wave passes straight through boundary unchanged'),
                         ('Frequency during refraction', 'Stays constant — wavelength changes as speed changes')],
               'title': 'Refraction Concepts'},
  'quiz': [{'opts': [('It bends towards the normal — angle of refraction is less than 40°, because light slows down in '
                      'glass',
                      True),
                     ('It bends away from the normal — angle of refraction is greater than 40°', False),
                     ('It travels straight through without bending — glass has no effect on direction', False),
                     ('It reflects back — light cannot pass from air into glass', False)],
            'q': 'A ray of light passes from air into a glass block. The angle of incidence is 40°. What happens to '
                 'the ray?',
            'wrong_explanations': {1: 'Bending AWAY happens when light goes from glass to air (speeds up). Air → glass '
                                      'means slowing down → bends TOWARDS normal.',
                                   2: "Light is transmitted through glass — it doesn't fully reflect at normal "
                                      'incidence.',
                                   3: 'Total internal reflection only occurs when light travels from a denser medium '
                                      '(glass) at an angle exceeding the critical angle — not when going from air into '
                                      'glass.'}},
           {'opts': [('Wavelength and speed both decrease — frequency stays constant', True),
                     ('Frequency increases — higher frequency in a denser medium', False),
                     ('Speed increases — denser medium speeds waves up', False),
                     ('All properties change — wavelength, frequency and speed all change', False)],
            'q': 'When light is refracted into a slower medium, which property changes?',
            'wrong_explanations': {1: "Frequency is determined by the SOURCE — it doesn't change at a boundary. Speed "
                                      'and wavelength both change (λ = v/f).',
                                   2: 'Speed DECREASES in a denser/slower medium — waves slow down, not speed up.',
                                   3: "Frequency is the one property that DOESN'T change during refraction — only "
                                      'speed and wavelength change.'}}],
  'rp': 'RP20 (Physics) — Investigate refraction of light through glass or perspex blocks. Measure angles of incidence '
        'and refraction. Plot i vs r to find relationship.',
  'spec': '6.6.2.2',
  'summary': 'Describe refraction of EM waves and construct ray diagrams at boundaries.',
  'theory': [{'content': 'REFRACTION: the change in direction of a wave when it passes from one medium to another.\n'
                         '\n'
                         'Caused by a CHANGE IN WAVE SPEED at the boundary.\n'
                         'When waves move from a FAST medium to a SLOW medium → bend TOWARDS the normal.\n'
                         'When waves move from a SLOW medium to a FAST medium → bend AWAY from the normal.\n'
                         '\n'
                         'FOR LIGHT:\n'
                         'Light slows down when entering glass or water from air.\n'
                         'Bends TOWARDS the normal when entering glass (air → glass).\n'
                         'Bends AWAY from the normal when leaving glass (glass → air).\n'
                         '\n'
                         'WAVELENGTH changes during refraction — frequency stays constant.\n'
                         'λ = v/f — if v decreases and f stays constant, λ must decrease too.',
              'heading': 'Refraction of Waves'},
             {'content': 'Drawing refraction ray diagrams:\n'
                         '\n'
                         '1. Draw the boundary between two media (horizontal line).\n'
                         '2. Draw the NORMAL — a dashed line perpendicular to the boundary at the point of incidence.\n'
                         '3. Draw the INCIDENT RAY approaching the boundary.\n'
                         '4. Measure the ANGLE OF INCIDENCE (i) — between incident ray and normal.\n'
                         '5. Draw the REFRACTED RAY on the other side of the boundary.\n'
                         '6. Measure the ANGLE OF REFRACTION (r) — between refracted ray and normal.\n'
                         '\n'
                         'RULE: when going from air into glass (slower medium):\n'
                         'Angle of refraction < angle of incidence (bends towards normal).\n'
                         'If incident ray is along the normal (0°): no bending occurs.\n'
                         '\n'
                         'At 0° (along the normal): no refraction — wave passes straight through.',
              'heading': 'Ray Diagrams for Refraction'},
             {'content': 'When EM waves reach a boundary, several things can happen:\n'
                         '\n'
                         'TRANSMISSION: wave passes through the medium.\n'
                         'ABSORPTION: wave energy transferred to the medium (heats it up or causes other effects).\n'
                         'REFLECTION: wave bounces back from the boundary.\n'
                         'REFRACTION: wave passes through but changes direction due to speed change.\n'
                         '\n'
                         'Different materials affect different wavelengths differently:\n'
                         'Glass: transparent to visible light, opaque to ultraviolet and infrared.\n'
                         'Sunscreen: absorbs UV, transmits visible.\n'
                         'X-ray: transmitted by soft tissue, absorbed by bone.\n'
                         'Microwaves: absorbed by water molecules in food (hence microwave cooking).\n'
                         '\n'
                         'This wavelength-dependent behaviour is why we have different detectors and uses for '
                         'different parts of the EM spectrum.',
              'heading': 'Absorption, Transmission and Reflection'}],
  'title': 'Properties of Electromagnetic Waves 1',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'UV, X-rays and gamma rays are all IONISING — they can damage DNA. Infrared and visible light can '
                    'cause burns/eye damage but are NOT ionising. The hazard from ionising radiation is cancer and '
                    'cell damage — not just burns.',
  'equations': [],
  'fifas': [],
  'higher': 'Radio waves produced by electrical oscillations — when absorbed they induce AC at the same frequency. '
            'Explain how this is used in radio reception. Describe greenhouse effect of atmosphere in terms of IR '
            'absorption and re-emission by greenhouse gases. Discuss how changes in climate models affect predictions.',
  'id': 'properties-em-waves-2',
  'key_note': 'Hazards increase with frequency. Infrared: burns. UV: sunburn, skin cancer, eye damage. X-rays: '
              'ionising, cancer risk, medical imaging. Gamma: most ionising, cancer/radiotherapy. Radio waves: '
              'produced by oscillating circuits, absorbed to induce same-frequency AC. Ionising radiation damages DNA '
              '→ mutations.',
  'matching': {'instruction': 'Match each EM wave type to its main hazard and protection.',
               'pairs': [('Infrared', 'Thermal burns at high intensity — avoid prolonged exposure to intense sources'),
                         ('Ultraviolet',
                          'Sunburn and skin cancer — DNA damage in skin cells — use sunscreen and cover up'),
                         ('X-rays', 'Ionising — DNA damage and cancer risk — minimise dose, use lead shielding'),
                         ('Gamma rays',
                          'Most ionising and penetrating — used in radiotherapy — needs lead/concrete shielding')],
               'title': 'EM Wave Hazards'},
  'quiz': [{'opts': [('X-rays are ionising — they have enough energy to remove electrons from atoms, damaging DNA. '
                      'Infrared only heats tissue.',
                      True),
                     ('X-rays travel faster than infrared — more collisions with cells per second', False),
                     ('Infrared is absorbed at the surface — X-rays penetrate deeper', False),
                     ('X-rays have longer wavelength — this allows them to interact with more DNA molecules', False)],
            'q': 'Why are X-rays more harmful to living tissue than infrared radiation of the same intensity?',
            'wrong_explanations': {1: "All EM waves travel at the same speed (3×10⁸ m/s) in vacuum — speed doesn't "
                                      'determine hazard.',
                                   2: 'While penetration IS a factor in X-ray safety, the fundamental reason X-rays '
                                      'are more harmful is IONISATION — they can break chemical bonds and damage DNA.',
                                   3: 'X-rays have SHORTER wavelength than infrared. Shorter wavelength = higher '
                                      'frequency = more energy per photon = more likely to ionise.'}},
           {'opts': [('Ultraviolet — UV has enough energy to penetrate skin cells and damage DNA, causing mutations',
                      True),
                     ('Infrared — warmth from the sun causes DNA to denature', False),
                     ('Visible light — the bright light damages cell membranes', False),
                     ('All parts equally — sunlight causes damage through all wavelengths together', False)],
            'q': 'A person sunbathes without sunscreen. Which part of sunlight causes the most DNA damage?',
            'wrong_explanations': {1: 'Infrared causes thermal effects (sunburn/heat) — but DNA damage specifically '
                                      'comes from UV ionising radiation.',
                                   2: "Visible light at solar intensities can damage the eyes (retina) but doesn't "
                                      'significantly damage skin DNA.',
                                   3: 'UV is specifically responsible for DNA damage and skin cancer — this is why SPF '
                                      'sunscreens block UV, not the whole spectrum.'}}],
  'rp': None,
  'spec': '6.6.2.3',
  'summary': 'Describe hazards of EM radiation and how different waves interact with matter.',
  'theory': [{'content': 'Not all EM radiation is harmful — hazard depends on frequency (and therefore energy per '
                         'photon).\n'
                         '\n'
                         'HIGHER FREQUENCY = MORE ENERGY = MORE POTENTIALLY HARMFUL.\n'
                         '\n'
                         'RADIO WAVES AND MICROWAVES:\n'
                         'Generally low risk at normal exposures.\n'
                         'Microwaves CAN heat tissue (same mechanism as microwave oven — absorbed by water).\n'
                         'Concerns about mobile phones (microwaves) have been studied — no confirmed harmful effects '
                         'at normal levels.\n'
                         '\n'
                         'INFRARED:\n'
                         'Absorbed by skin — can cause BURNS at high intensity.\n'
                         'Thermal cameras detect infrared emitted by people and objects.\n'
                         '\n'
                         'VISIBLE LIGHT:\n'
                         'Normally safe. Very intense visible light can damage retina (e.g. looking at solar eclipse '
                         'or high-power laser).',
              'heading': 'Hazards of EM Radiation'},
             {'content': 'ULTRAVIOLET (UV):\n'
                         'Can cause SUNBURN — damages skin cells.\n'
                         'Increases risk of SKIN CANCER — damages DNA in skin cells.\n'
                         "Can cause damage to EYES — cataracts, photokeratitis ('snow blindness').\n"
                         'Protection: sunscreen (absorbs UV), sunglasses (filter UV), protective clothing.\n'
                         '\n'
                         'X-RAYS:\n'
                         'Penetrate soft tissue, absorbed by denser materials (bone, metal).\n'
                         'Used in medical imaging (X-rays, CT scans).\n'
                         'Can IONISE cells — damage DNA → cancer risk.\n'
                         'Dose kept minimal; radiographers leave the room; lead aprons used.\n'
                         '\n'
                         'GAMMA RAYS:\n'
                         'Highest energy — most penetrating, most ionising.\n'
                         'Emitted by radioactive materials.\n'
                         'Can cause radiation sickness at high doses, cancer at lower doses.\n'
                         'Used in cancer TREATMENT (radiotherapy) — beams focused on tumour.\n'
                         '\n'
                         'Ionising radiation (UV, X-ray, gamma): damages DNA → mutations → cancer.',
              'heading': 'Ultraviolet, X-rays and Gamma Rays'},
             {'content': 'RADIO WAVES are produced by OSCILLATING ELECTRICAL CIRCUITS:\n'
                         'An alternating current at radio frequency in a transmitter aerial causes oscillating charges '
                         '→ emit radio waves.\n'
                         'Frequency of radio waves = frequency of electrical oscillation in the circuit.\n'
                         '\n'
                         'ABSORPTION OF RADIO WAVES:\n'
                         'When radio waves are absorbed by a conducting aerial → induces an alternating current at the '
                         'SAME FREQUENCY as the radio wave → this is how radio receivers work.\n'
                         '\n'
                         'DIFFERENT EM WAVES — INTERACTION WITH MATTER SUMMARY:\n'
                         'Absorbed: energy transferred to medium (heating or other effects).\n'
                         'Transmitted: passes through without significant interaction.\n'
                         'Reflected: bounces off boundary.\n'
                         'Refracted: changes direction at boundary due to speed change.\n'
                         "The interaction depends on the wavelength and the material's properties.",
              'heading': 'Radio Waves — Production and Uses'}],
  'title': 'Properties of Electromagnetic Waves 2 and Hazards',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'MRI scanners use RADIO WAVES (not X-rays) — they are safe for soft tissue imaging with no '
                    'ionising radiation. X-rays are used for imaging BONE and dense structures. Also: microwaves for '
                    'SATELLITE communication (pass through ionosphere); radio waves for BROADCAST (reflect off '
                    'ionosphere).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'uses-em-waves',
  'key_note': 'Radio: broadcast, MRI. Microwave: satellites, phones, radar, cooking. IR: heating, remote controls, '
              'night vision, fibre optics. Visible: photography, fibre optics, photosynthesis. UV: sterilisation, '
              'fluorescence, vitamin D. X-ray: medical imaging, airport security, CT. Gamma: radiotherapy, '
              'sterilisation, tracers.',
  'matching': {'instruction': 'Match each application to the EM wave type used.',
               'pairs': [('Radio waves', 'MRI scanner — safe for soft tissue, no ionising radiation'),
                         ('Microwaves', 'Satellite communication — passes through ionosphere to reach satellites'),
                         ('Infrared', 'TV remote control — pulses of IR carry the signal to the TV'),
                         ('X-rays', 'Medical imaging of bones — absorbed by dense bone, transmitted by soft tissue'),
                         ('Gamma rays', 'Radiotherapy — focused beams kill cancer cells')],
               'title': 'EM Wave Applications'},
  'quiz': [{'opts': [('Microwaves pass through the ionosphere — radio waves reflect off it, preventing them from '
                      'reaching satellites in orbit',
                      True),
                     ('Microwaves are more powerful — they reach greater distances than radio waves', False),
                     ('Radio waves are dangerous at high altitude — microwaves are safer for satellite use', False),
                     ('Satellites can only detect microwaves — their receivers are not compatible with radio waves',
                      False)],
            'q': 'Why are microwaves used for satellite communications rather than radio waves?',
            'wrong_explanations': {1: 'Power determines signal strength at a given distance — but all EM waves travel '
                                      'at the same speed. The key distinction is IONOSPHERE INTERACTION.',
                                   2: 'Safety is not the relevant factor — the ionosphere physically reflects (most) '
                                      'radio waves back to Earth.',
                                   3: "This is backwards — it's the PHYSICS of ionosphere reflection, not receiver "
                                      'incompatibility, that determines which EM type is used.'}},
           {'opts': [('UV has enough energy to damage DNA in microorganisms — killing or inactivating bacteria and '
                      'viruses',
                      True),
                     ('UV heats the equipment to high temperatures, killing microorganisms by heat', False),
                     ('UV is absorbed by metal — heating the equipment surface to kill bacteria', False),
                     ('UV converts oxygen to ozone, which then kills bacteria chemically', False)],
            'q': 'UV light is used to sterilise medical equipment. Why is UV effective for this?',
            'wrong_explanations': {1: "UV can cause some warming but it's not the primary mechanism — UV sterilisation "
                                      'works through DNA damage (photochemical action), not significant heating.',
                                   2: 'UV sterilisation is used for transparent surfaces, water, and air — metal '
                                      'surfaces are typically sterilised by heat or chemicals.',
                                   3: 'UV can produce some ozone, but the primary sterilisation mechanism is direct '
                                      'DNA damage from UV photons — not ozone.'}}],
  'rp': None,
  'spec': '6.6.2.4',
  'summary': 'Describe the uses of each type of electromagnetic wave and explain why each type is suitable.',
  'theory': [{'content': 'RADIO WAVES:\n'
                         'BROADCASTING: AM and FM radio, TV broadcasts — travel long distances, reflect off '
                         'ionosphere.\n'
                         'COMMUNICATION: aircraft, ships, emergency services.\n'
                         'ASTRONOMY: radio telescopes detect radio waves from distant stars and galaxies.\n'
                         'MRI SCANNERS: radio waves + magnetic field → detailed images of soft tissue (no ionising '
                         'radiation).\n'
                         '\n'
                         'MICROWAVES:\n'
                         'MOBILE PHONES AND WIFI: short-range communication.\n'
                         'SATELLITE COMMUNICATION: microwaves pass through the atmosphere and ionosphere (radio waves '
                         'reflect off ionosphere — limited for satellite use).\n'
                         "MICROWAVE OVENS: microwave frequency matches water molecules' resonance → absorbed → food "
                         'heats from inside.\n'
                         'RADAR: detect aircraft, ships, weather systems — measure distance by timing reflection.',
              'heading': 'Uses of Radio Waves and Microwaves'},
             {'content': 'INFRARED (IR):\n'
                         'HEATING: electric heaters, grills — absorbed by surfaces, converted to heat.\n'
                         'REMOTE CONTROLS: TV, DVD players — IR pulses carry coded signals.\n'
                         'FIBRE OPTICS: IR carried along optical fibres for high-speed internet.\n'
                         'NIGHT VISION CAMERAS: detect IR emitted by warm bodies — useful in darkness.\n'
                         'THERMAL IMAGING: medical, security, wildlife observation.\n'
                         '\n'
                         'VISIBLE LIGHT:\n'
                         'PHOTOGRAPHY: cameras capture visible light.\n'
                         'FIBRE OPTICS: carries data as light pulses — basis of broadband internet.\n'
                         'PHOTOSYNTHESIS: plants absorb red and blue light.\n'
                         'LASERS: surgery, barcode scanners, DVD reading.\n'
                         '\n'
                         'ULTRAVIOLET (UV):\n'
                         'STERILISATION: UV kills bacteria and viruses — used in hospitals and water treatment.\n'
                         'FLUORESCENCE: some materials emit visible light when absorbing UV — security markings, '
                         'fluorescent lamps.\n'
                         'BLACK LIGHTS: detect forged bank notes (UV-reactive ink).\n'
                         'VITAMIN D PRODUCTION: skin produces vitamin D when exposed to UV.',
              'heading': 'Uses of Infrared, Visible and Ultraviolet'},
             {'content': 'X-RAYS:\n'
                         'MEDICAL IMAGING: pass through soft tissue, absorbed by bone → shadow on film/detector.\n'
                         'CT SCANS: multiple X-ray beams → 3D image of internal structures.\n'
                         'AIRPORT SECURITY: luggage scanning — detect metal, explosives.\n'
                         'MATERIAL TESTING: checking for cracks in metal castings and welds.\n'
                         '\n'
                         'GAMMA RAYS:\n'
                         'CANCER TREATMENT (radiotherapy): focused beams kill tumour cells.\n'
                         'ST ERILISATION of medical equipment: kills all microorganisms without heat.\n'
                         'FOOD IRRADIATION: kills bacteria in food → longer shelf life.\n'
                         'MEDICAL TRACERS: gamma-emitting radioisotopes injected → gamma camera detects distribution '
                         'in body → reveals organ function.\n'
                         'THICKNESS MONITORING: detect gamma penetration through materials in manufacturing.\n'
                         '\n'
                         'MATCHING APPLICATION TO WAVE TYPE:\n'
                         'The wave chosen matches its properties to the application:\n'
                         'Must penetrate enough → not be absorbed too quickly.\n'
                         'Must interact appropriately with the target material.\n'
                         'Hazard must be managed — ionising types minimised.',
              'heading': 'Uses of X-rays and Gamma Rays'}],
  'title': 'Uses and Applications of Electromagnetic Waves',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A converging lens does NOT always form a real image. If the object is inside the focal length, it '
                    'forms a VIRTUAL image (like a magnifying glass). Diverging lenses ALWAYS form virtual images. '
                    'Real images can be projected; virtual images cannot.',
  'equations': ['Magnification = image height ÷ object height = image distance ÷ object distance'],
  'fifas': [],
  'higher': None,
  'id': 'lenses',
  'key_note': 'Converging (convex) lens: focuses parallel rays at focal point. Forms real images (object beyond f) or '
              'virtual (object inside f). Three rays: parallel→focal point, through centre undeviated, through focal '
              'point→parallel. Magnification = image/object height. Myopia: diverging lens. Hyperopia: converging '
              'lens.',
  'matching': {'instruction': 'Match each lens/object position to the type of image formed.',
               'pairs': [('Converging, object beyond 2f',
                          'Real, inverted, diminished image — between f and 2f on other side'),
                         ('Converging, object inside f',
                          'Virtual, upright, magnified image — same side as object (magnifying glass)'),
                         ('Diverging lens',
                          'Virtual, upright, diminished image — always, regardless of object position'),
                         ('Myopia correction', 'Diverging lens — diverges light before it reaches the eye')],
               'title': 'Lenses and Images'},
  'quiz': [{'opts': [('Less than 10 cm from the lens — the object must be inside the focal length to produce a '
                      'virtual, magnified image',
                      True),
                     ('More than 20 cm away — large objects need to be far from the lens', False),
                     ('Exactly at 10 cm — the focal point gives maximum magnification', False),
                     ('Between 10 cm and 20 cm — real magnified images are produced here', False)],
            'q': 'A converging lens has focal length 10 cm. Where should an object be placed to use it as a magnifying '
                 'glass?',
            'wrong_explanations': {1: 'More than 20 cm gives a real, DIMINISHED image — not useful as a magnifying '
                                      'glass.',
                                   2: 'At exactly the focal point, rays emerge parallel — no image is formed.',
                                   3: "Between f and 2f gives a real, MAGNIFIED image — but it's inverted and appears "
                                      'on the other side, not a magnifying glass use.'}},
           {'opts': [('A diverging (concave) lens — it spreads the light before it enters the eye, so the image forms '
                      'further back on the retina rather than in front of it',
                      True),
                     ('A converging (convex) lens — it focuses the light more, moving the image onto the retina',
                      False),
                     ('Either type works — the brain adjusts to either correction', False),
                     ('No lens needed — short-sightedness corrects itself over time', False)],
            'q': 'A person is short-sighted (myopic). What type of lens corrects this and why?',
            'wrong_explanations': {1: 'A converging lens would make the eye MORE powerful, causing the image to form '
                                      'even FURTHER in front of the retina — making myopia worse.',
                                   2: 'Vision correction is specific — the wrong type of lens makes things worse.',
                                   3: "Myopia is a structural issue that doesn't self-correct — it typically worsens "
                                      'over time.'}}],
  'rp': None,
  'spec': '6.6.3 (physics only)',
  'summary': 'Describe how converging and diverging lenses refract light and construct ray diagrams.',
  'theory': [{'content': 'A LENS is a shaped piece of transparent material that refracts light to form images.\n'
                         '\n'
                         'CONVERGING (CONVEX) LENS:\n'
                         'Thicker in the middle, thinner at the edges.\n'
                         'Bends parallel rays INWARD to meet at the FOCAL POINT.\n'
                         'Focal length (f): distance from lens to focal point.\n'
                         'Can form REAL images (on the other side of the lens) — can be projected on a screen.\n'
                         'Can also form VIRTUAL images (if object inside focal length) — appear on same side as '
                         'object.\n'
                         '\n'
                         'DIVERGING (CONCAVE) LENS:\n'
                         'Thinner in the middle, thicker at the edges.\n'
                         'Bends parallel rays OUTWARD — they appear to diverge from a VIRTUAL focal point.\n'
                         'Focal length: the virtual focal point is on the SAME side as the incoming light.\n'
                         'Always forms VIRTUAL, upright, diminished images — cannot be projected.',
              'heading': 'Types of Lenses'},
             {'content': 'THREE STANDARD RAYS for constructing images:\n'
                         '\n'
                         '1. RAY PARALLEL to the principal axis → refracts THROUGH the focal point on the other side.\n'
                         '2. RAY THROUGH the CENTRE of the lens → passes straight through UNDEVIATED.\n'
                         '3. RAY THROUGH the FOCAL POINT on the near side → refracts PARALLEL to the principal axis.\n'
                         '\n'
                         'Where two (or more) rays meet → location of the IMAGE.\n'
                         '\n'
                         'IMAGES FORMED BY CONVERGING LENS:\n'
                         'Object beyond 2f: real, inverted, diminished image between f and 2f.\n'
                         'Object at 2f: real, inverted, same size as object, image at 2f on other side.\n'
                         'Object between f and 2f: real, inverted, magnified image beyond 2f.\n'
                         'Object at f: no image — rays parallel, never meet.\n'
                         'Object inside f: virtual, upright, magnified image on same side as object (magnifying '
                         'glass).\n'
                         '\n'
                         'MAGNIFICATION:\n'
                         'Magnification = image height ÷ object height = image distance ÷ object distance',
              'heading': 'Ray Diagrams for Converging Lenses'},
             {'content': 'MAGNIFYING GLASS:\n'
                         'Converging lens used with object inside focal length.\n'
                         'Virtual, upright, magnified image.\n'
                         'Used by jewellers, stamp collectors, to read small print.\n'
                         '\n'
                         'CAMERA:\n'
                         'Converging lens focuses real, inverted image onto sensor/film.\n'
                         'Object far from lens → image close to lens (just beyond f).\n'
                         'Zoom lens: variable focal length.\n'
                         '\n'
                         'EYE:\n'
                         'Cornea and eye lens (both converging) focus light onto retina.\n'
                         'CILIARY MUSCLES change lens shape → adjust focal length (accommodation).\n'
                         'NORMAL VISION: image forms on retina.\n'
                         '\n'
                         'CORRECTING VISION DEFECTS:\n'
                         'MYOPIA (short-sightedness): eye lens too powerful → image forms in FRONT of retina.\n'
                         'Corrected with DIVERGING lens — spreads light before it reaches the eye.\n'
                         'HYPEROPIA (long-sightedness): eye lens too weak → image would form BEHIND retina.\n'
                         'Corrected with CONVERGING lens — helps converge light before it reaches the eye.\n'
                         '\n'
                         'TELESCOPES: two converging lenses — objective (large, long focal length) + eyepiece (small, '
                         'short focal length).\n'
                         'MICROSCOPES: two converging lenses in series — objective very close to specimen.',
              'heading': 'Applications of Lenses'}],
  'title': 'Lenses',
  'triple_only': 'Lenses (physics only) — not in Combined Science.',
  'variables': [('f', 'Focal length', 'metres', 'm'), ('M', 'Magnification', '', '')]},
 {'common_mistake': 'A PERFECT BLACK BODY is black because it absorbs ALL radiation — it also emits MAXIMUM radiation '
                    "for its temperature. Being a 'perfect emitter' and 'perfect absorber' go together. Hotter objects "
                    'emit at SHORTER wavelengths — this seems counterintuitive but is why glowing objects change '
                    'colour from red to white-hot as they get hotter.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'infrared-black-bodies',
  'key_note': 'All objects emit and absorb IR. Dark matt = best emitter and absorber. Shiny = best reflector. Black '
              'body: absorbs all radiation, emits maximum for its temperature. Hotter → more emission at shorter '
              'wavelength. Stars: colour indicates temperature (red=cool, blue=hot). Earth absorbs solar, re-emits IR '
              '— greenhouse effect.',
  'matching': {'instruction': 'Match each statement to the correct concept.',
               'pairs': [('Dark matt surface', 'Best emitter and absorber of infrared radiation'),
                         ('Perfect black body',
                          'Absorbs all incident radiation — emits maximum radiation for its temperature'),
                         ('Hotter object',
                          'Emits more radiation AND at shorter wavelengths — peak shifts towards visible/UV'),
                         ('Blue-white star', 'Very hot (~30,000 K) — peak emission in UV/blue visible range')],
               'title': 'Infrared and Black Bodies'},
  'quiz': [{'opts': [('As temperature increases, the peak emission shifts to shorter wavelengths — from infrared '
                      'through red to shorter visible wavelengths approaching white',
                      True),
                     ('The metal changes chemical composition as it gets hotter, producing different coloured oxides',
                      False),
                     ('Different wavelengths of light are produced by different electrons in the metal', False),
                     ('White light contains all colours — the metal must be emitting all wavelengths at low '
                      'temperature but only red at high temperature',
                      False)],
            'q': 'A metal rod is heated in a furnace. First it glows red, then orange, then white. What does this tell '
                 'us?',
            'wrong_explanations': {1: 'The colour change is due to temperature-dependent emission spectra — not '
                                      'chemical changes. A pure metal rod would show the same progression.',
                                   2: 'Different electrons in the metal contribute to emission, but the pattern '
                                      'follows the temperature-dependent black body spectrum — the overall colour '
                                      'shift is about temperature.',
                                   3: 'White hot means the peak has moved to visible wavelengths with broad-spectrum '
                                      'emission — cool objects emit IR (invisible) then progress through red, orange, '
                                      'yellow to white as temperature rises.'}},
           {'opts': [('Silvered walls are poor emitters and poor absorbers of infrared — they reflect radiation back, '
                      'reducing thermal energy transfer by radiation',
                      True),
                     ('Silver is a good conductor — it rapidly distributes heat evenly around the flask walls', False),
                     ('Silver reacts with oxygen in the air — the oxide layer acts as an insulator', False),
                     ('The bright colour of silver reflects external light, keeping the flask cool', False)],
            'q': 'Why are the walls of a thermos flask silvered?',
            'wrong_explanations': {1: 'Silver is an excellent conductor — but the silvered wall is there to REDUCE '
                                      'radiation transfer, not to conduct heat.',
                                   2: "Silver doesn't form a significant protective oxide layer at room temperature — "
                                      'the silvering works by reflection of radiation.',
                                   3: "Visible light reflection is not the primary reason — it's the IR radiation "
                                      'reflection that reduces thermal energy transfer.'}}],
  'rp': None,
  'spec': '6.6.5 (physics only)',
  'summary': 'Describe infrared emission and absorption by surfaces and explain perfect black body radiation.',
  'theory': [{'content': 'All objects emit and absorb THERMAL RADIATION (infrared radiation) continuously.\n'
                         '\n'
                         'EMISSION:\n'
                         'All objects above absolute zero emit infrared radiation.\n'
                         'Hotter objects emit MORE radiation and at SHORTER wavelengths (higher frequency, more '
                         'energetic).\n'
                         '\n'
                         'ABSORPTION:\n'
                         'Objects absorb radiation from their surroundings.\n'
                         'Dark, matt surfaces are better ABSORBERS than light, shiny surfaces.\n'
                         '\n'
                         'Dark matt surfaces are also better EMITTERS.\n'
                         'Shiny, light surfaces are better REFLECTORS and poorer emitters/absorbers.\n'
                         '\n'
                         'EMISSION vs ABSORPTION RATES:\n'
                         'If emission rate > absorption rate → object cools.\n'
                         'If absorption rate > emission rate → object heats up.\n'
                         'If rates are equal → temperature is constant (thermal equilibrium).',
              'heading': 'Emission and Absorption of Radiation'},
             {'content': 'A PERFECT BLACK BODY is a theoretical object that:\n'
                         'ABSORBS all radiation that falls on it (reflects none).\n'
                         'EMITS the maximum amount of radiation for its temperature.\n'
                         '\n'
                         'Perfect black bodies emit the most radiation of any object at the same temperature.\n'
                         'The emission spectrum of a black body depends ONLY on temperature — not on the material.\n'
                         '\n'
                         'BLACK BODY RADIATION CURVES:\n'
                         'As temperature increases:\n'
                         'Peak of emission shifts to SHORTER wavelengths (higher frequency).\n'
                         'Total energy emitted per second INCREASES dramatically.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'A cool object: emits mainly low-frequency infrared — invisible to the eye.\n'
                         'Hot iron (600°C): glows dull red — emitting visible red light.\n'
                         'Very hot iron (1000°C): orange-white — peak moves into visible range.\n'
                         'The Sun (~5500°C surface): peak emission in visible light (yellow-green).\n'
                         '\n'
                         'A cavity with a small hole acts as an approximate black body.',
              'heading': 'Perfect Black Bodies'},
             {'content': 'STARS AS BLACK BODIES:\n'
                         'Stars approximately behave as black bodies.\n'
                         'The colour of a star indicates its surface temperature:\n'
                         'Red stars (~3000 K) → cool → peak in infrared/red.\n'
                         'Yellow stars (like the Sun, ~5500 K) → medium → peak in visible.\n'
                         'Blue-white stars (~30,000 K) → very hot → peak in UV/blue.\n'
                         '\n'
                         "EARTH'S TEMPERATURE:\n"
                         'The Earth absorbs solar radiation and re-emits as infrared (longer wavelength — Earth is '
                         'cooler than Sun).\n'
                         "Greenhouse gases absorb Earth's infrared emission → trap energy → warming effect.\n"
                         '\n'
                         'THERMAL CAMERAS:\n'
                         'Detect infrared emitted by warm objects — used in: night vision, firefighting, medical '
                         'diagnosis (detecting hot spots), building inspection (heat loss).\n'
                         '\n'
                         'SPACE TELESCOPES:\n'
                         'Infrared telescopes detect emission from cool objects like dust clouds in space.\n'
                         'Hubble detects visible light; James Webb Space Telescope detects infrared.\n'
                         '\n'
                         'SELECTIVE EMISSION AND ABSORPTION:\n'
                         'Solar panels: dark, matt surfaces to maximise solar absorption.\n'
                         'Solar water heaters: black tubes to maximise absorption.\n'
                         'Thermos flasks: silvered walls to minimise emission and absorption (reflect radiation back).',
              'heading': 'Applications'}],
  'title': 'Infrared Emission, Absorption and Black Bodies',
  'triple_only': 'Infrared emission/absorption and black bodies (physics only) — not in Combined Science.',
  'variables': []}],

"magnetism": [{'common_mistake': 'Only IRON, STEEL, NICKEL and COBALT are magnetic materials. Aluminium and copper are NOT '
                    'attracted to magnets. Permanent magnets (steel) retain magnetism. Induced magnets (iron) lose it '
                    'when the field is removed.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'poles-of-a-magnet',
  'key_note': 'Like poles repel; opposite poles attract. Permanent magnets: retain magnetism (steel — hard). Induced '
              'magnets: temporary, lose magnetism when external field removed (iron — soft). Magnetic materials: iron, '
              'steel, nickel, cobalt. Domains: aligned = magnetised, random = unmagnetised.',
  'matching': {'instruction': 'Match each statement to permanent magnet or induced magnet.',
               'pairs': [('Permanent magnet', 'Made from steel — retains magnetism without an external field'),
                         ('Induced magnet', 'Made from iron — temporary, loses magnetism when external field removed'),
                         ('Both attract',
                          'The near end always becomes the opposite pole — both are attracted to the magnet'),
                         ('Demagnetising',
                          'Heating above Curie temperature or using AC solenoid — randomises domain alignment')],
               'title': 'Magnetic Properties'},
  'quiz': [{'opts': [('The steel becomes an induced magnet — the end nearest the magnet becomes opposite in polarity, '
                      'so they attract',
                      True),
                     ('Steel is made from iron which is naturally magnetic — it has its own permanent field that '
                      'attracts',
                      False),
                     ('The paper clip gains an electric charge from the magnetic field — opposite charges attract',
                      False),
                     ('The magnetic field passes through the paper clip, pulling it forward', False)],
            'q': 'A steel paper clip is brought near a bar magnet. Why is the paper clip attracted?',
            'wrong_explanations': {1: 'Steel is a MAGNETIC MATERIAL (ferromagnetic) but not permanently magnetised '
                                      'until it is magnetised. The attraction is due to INDUCED MAGNETISM from the bar '
                                      'magnet.',
                                   2: "Magnetism and electric charge are separate — magnetic fields don't charge "
                                      'objects with static electricity.',
                                   3: "Magnetic forces act on magnetic materials — they don't 'push' the clip forward. "
                                      'The attraction is between the magnetic poles of the induced magnet and the bar '
                                      'magnet.'}},
           {'opts': [('Fridge magnet: permanent — retains field indefinitely. Compass: also permanent — compass needle '
                      'must always point north reliably',
                      True),
                     ('Fridge magnet: temporary — it loses magnetism each day. Compass: permanent', False),
                     ('Fridge magnet: stronger field — household magnets are more powerful than compass needles',
                      False),
                     ('Fridge magnet: induced. Compass: permanent — all small magnets are induced magnets', False)],
            'q': 'A fridge magnet and a compass are both magnets. What is the key difference between them regarding '
                 'their magnetism?',
            'wrong_explanations': {1: 'Both ARE permanent magnets — but the question is testing understanding that '
                                      'both fridge magnets and compass needles are permanent (made from hard magnetic '
                                      'materials).',
                                   2: 'Strength varies between magnets but strength is not the distinguishing feature '
                                      'the question asks about.',
                                   3: 'Both the fridge magnet and compass needle are PERMANENT magnets — they must '
                                      'retain their magnetism to function.'}}],
  'rp': None,
  'spec': '6.7.1.1',
  'summary': 'Describe the properties of magnets, distinguish permanent from induced magnetism, and describe magnetic '
             'forces.',
  'theory': [{'content': 'Every magnet has a NORTH POLE and a SOUTH POLE.\n'
                         '\n'
                         'RULES FOR MAGNETIC FORCES:\n'
                         'LIKE POLES REPEL — N and N repel; S and S repel.\n'
                         'OPPOSITE POLES ATTRACT — N and S attract.\n'
                         '\n'
                         'Magnetic force is a NON-CONTACT FORCE — acts at a distance without touching.\n'
                         '\n'
                         'MAGNETIC MATERIALS:\n'
                         'Ferromagnetic materials are attracted to magnets.\n'
                         'Main ferromagnetic materials at GCSE: IRON, STEEL, NICKEL, COBALT.\n'
                         'Aluminium, copper, plastic, wood — NOT magnetic.\n'
                         '\n'
                         'Only iron, steel, nickel and cobalt can become magnetised or be attracted to magnets.',
              'heading': 'Poles and Magnetic Forces'},
             {'content': 'PERMANENT MAGNETS:\n'
                         "Produce their own persistent magnetic field — they don't need an external field to be "
                         'magnetic.\n'
                         'Retain magnetism when the external field is removed.\n'
                         'Made from HARD magnetic materials — steel, alnico alloys.\n'
                         'Hard materials are harder to magnetise but retain magnetism better.\n'
                         'Examples: bar magnets, horseshoe magnets, fridge magnets, compass needles.\n'
                         '\n'
                         'INDUCED MAGNETS:\n'
                         'Temporarily magnetised by placing them in a magnetic field.\n'
                         'When the external field is removed, they LOSE their magnetism quickly.\n'
                         'Made from SOFT magnetic materials — IRON.\n'
                         'Soft materials are easier to magnetise and demagnetise.\n'
                         'Examples: iron nail picked up by a magnet; iron core in an electromagnet.\n'
                         '\n'
                         'INDUCED MAGNETISM DIRECTION:\n'
                         "The induced pole nearest to the magnet's pole is ALWAYS OPPOSITE to that pole.\n"
                         'This is why magnets ATTRACT ferromagnetic materials — the near end becomes the opposite '
                         'pole.',
              'heading': 'Permanent and Induced Magnetism'},
             {'content': 'MAGNETISING a material:\n'
                         'Rub with a permanent magnet always in the same direction (stroking method).\n'
                         'Place in a SOLENOID carrying DC — the field aligns the magnetic domains.\n'
                         "Hammer while held in the Earth's magnetic field (unreliable).\n"
                         '\n'
                         'DEMAGNETISING:\n'
                         'HEAT — heating above the CURIE TEMPERATURE destroys magnetic domain alignment.\n'
                         'HAMMERING/VIBRATION — disrupts domain alignment.\n'
                         'ALTERNATING CURRENT (AC) in a solenoid — reverses field repeatedly, randomising domains.\n'
                         '\n'
                         'MAGNETIC DOMAINS:\n'
                         'A magnet is made of tiny regions called DOMAINS — each domain acts like a mini-magnet.\n'
                         'In an UNMAGNETISED material: domains point in random directions → overall effect cancels.\n'
                         'In a MAGNETISED material: domains are aligned in the same direction → net magnetic field.\n'
                         'Magnetising aligns the domains; demagnetising randomises them.',
              'heading': 'Magnetising and Demagnetising'}],
  'title': 'Poles of a Magnet and Permanent Magnetism',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Field lines go from NORTH to SOUTH outside the magnet — this shows the direction a north pole '
                    'would move. Field lines NEVER cross. Closer field lines = STRONGER field — not weaker. The '
                    "Earth's geographic north pole is actually a magnetic SOUTH pole (that's why compass north is "
                    'attracted to it).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'magnetic-fields',
  'key_note': 'Magnetic field: region where magnetic material experiences force. Field lines: N to S outside magnet, '
              'never cross, closer = stronger. Plot with compass (shows direction) or iron filings (shows pattern, no '
              "direction). Strongest field at poles. Earth's field: like a giant bar magnet.",
  'matching': {'instruction': 'Match each field line property to its meaning.',
               'pairs': [('Arrow direction', 'Points from north pole to south pole outside the magnet'),
                         ('Closely spaced lines', 'Strong magnetic field — near the poles of a bar magnet'),
                         ('Widely spaced lines', 'Weak magnetic field — far from the magnet'),
                         ('Lines that never cross',
                          'Field lines represent unique directions — two directions at one point is impossible')],
               'title': 'Magnetic Field Lines'},
  'quiz': [{'opts': [('The field is strongest near the poles — closely spaced field lines indicate greater magnetic '
                      'force in that region',
                      True),
                     ('The poles have more mass — iron filings are attracted to mass, not field strength', False),
                     ('The poles are the least magnetised parts — filings avoid the strong field regions', False),
                     ('Iron filings cluster near poles due to gravity — the poles are at the ends', False)],
            'q': 'A student plots a magnetic field using iron filings around a bar magnet. The filings cluster densely '
                 'near the poles. What does this show?',
            'wrong_explanations': {1: 'Iron filings are attracted to magnetic fields — they cluster where the field is '
                                      'STRONGEST (at poles), not due to mass.',
                                   2: 'Dense filings = strong field = more attraction. Less magnetised areas would '
                                      'have fewer filings.',
                                   3: "The magnet is horizontal in typical demonstrations — gravity doesn't explain "
                                      'end-clustering.'}},
           {'opts': [('From the north pole to the south pole — field lines exit the north pole and enter the south '
                      'pole',
                      True),
                     ("From south to north — the south pole is the 'positive' terminal", False),
                     ("In random directions — field lines don't have a set direction", False),
                     ('From both poles outward — field lines never enter the magnet', False)],
            'q': 'Which direction do magnetic field lines point outside a bar magnet?',
            'wrong_explanations': {1: 'Convention states field lines go from N to S — the direction a free north pole '
                                      'would move.',
                                   2: 'Field lines have a specific direction defined by convention — from N to S.',
                                   3: 'Field lines form closed loops — they exit the north pole, curve around, and '
                                      're-enter at the south pole.'}}],
  'rp': 'RP21 (Physics) — Plot the magnetic field pattern around a bar magnet using a plotting compass. Mark direction '
        'of field lines from N to S.',
  'spec': '6.7.1.2',
  'summary': 'Describe magnetic fields, draw field line patterns and explain how they show force and direction.',
  'theory': [{'content': 'A MAGNETIC FIELD is a region around a magnet (or current-carrying conductor) where a '
                         'magnetic material experiences a force.\n'
                         '\n'
                         'MAGNETIC FIELD LINES:\n'
                         'Shown as lines with arrows pointing from NORTH to SOUTH outside the magnet.\n'
                         'Inside the magnet, arrows point from south to north (completing the loop).\n'
                         'Closer field lines → STRONGER field.\n'
                         'Field lines NEVER CROSS each other.\n'
                         '\n'
                         'The STRENGTH of a magnetic field is shown by the SPACING of field lines:\n'
                         'Close together → strong field (near the poles).\n'
                         'Far apart → weak field (far from the magnet).\n'
                         '\n'
                         'A COMPASS placed in a magnetic field aligns with the field — the north pole of the compass '
                         'points in the direction of the field line at that point.',
              'heading': 'Magnetic Fields and Field Lines'},
             {'content': 'BAR MAGNET:\n'
                         'Field lines emerge from the NORTH pole, curve around, and enter the SOUTH pole.\n'
                         'Strongest field at the POLES (field lines closest together).\n'
                         'Field extends in 3D around the magnet.\n'
                         '\n'
                         'ATTRACTING MAGNETS (opposite poles facing):\n'
                         'Field lines go from the N pole of one magnet to the S pole of the other.\n'
                         'In the space between — field lines go directly across → strong, attractive force.\n'
                         '\n'
                         'REPELLING MAGNETS (like poles facing):\n'
                         'Field lines curve AWAY from each other.\n'
                         'A NEUTRAL POINT exists between them — where fields cancel (no net field).\n'
                         '\n'
                         'HORSESHOE MAGNET:\n'
                         'Field lines go directly between the two poles (N and S facing each other).\n'
                         'Strong, concentrated uniform field in the gap.\n'
                         'Useful in motors and generators.',
              'heading': 'Field Patterns for Different Magnets'},
             {'content': 'PLOTTING WITH A COMPASS:\n'
                         '1. Place bar magnet on paper.\n'
                         '2. Place a compass at a point near the magnet.\n'
                         '3. Mark the position of the NORTH END of the compass needle with a dot.\n'
                         '4. Move the compass so its SOUTH end is where the previous dot was.\n'
                         '5. Mark the new position of the north end.\n'
                         '6. Repeat to trace the field line.\n'
                         '7. Draw a smooth curve through the dots with an arrow pointing from the original position '
                         'towards the current one (north to south direction outside the magnet).\n'
                         '\n'
                         'PLOTTING WITH IRON FILINGS:\n'
                         'Scatter iron filings around the magnet on a sheet of paper.\n'
                         'Filing align with field lines → reveals field pattern.\n'
                         "Faster than compass method but doesn't show direction.\n"
                         '\n'
                         "Earth's magnetic field:\n"
                         'Earth has a magnetic field that acts like a giant bar magnet.\n'
                         'Geographic north pole corresponds to a magnetic SOUTH pole (compass north points there).\n'
                         "Compass needles align with Earth's field — used for navigation.",
              'heading': 'Plotting Magnetic Fields'}],
  'title': 'Magnetic Fields',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'An electromagnet uses IRON (soft) — not steel (hard). Iron demagnetises when the current is '
                    'switched off. Steel would retain magnetism. Increasing CURRENT or NUMBER OF TURNS both increase '
                    "the strength of an electromagnet's field.",
  'equations': [],
  'fifas': [],
  'higher': 'The motor effect: a current-carrying conductor in a magnetic field experiences a force. F = BIl (force = '
            "flux density × current × length). Fleming's Left-Hand Rule: thumb = force direction, index = field, "
            'middle finger = current. Applications: electric motors (rotating coil in field). Induced EMF (generator '
            'effect).',
  'id': 'electromagnetism',
  'key_note': 'Current-carrying wire: circular field lines, stronger with more current, weaker further away. Solenoid: '
              'uniform field inside, acts like bar magnet. Electromagnet: solenoid + iron core. Iron (soft): loses '
              'magnetism when off. Stronger with more current, more turns, iron core. Applications: cranes, bells, '
              'MRI, relays.',
  'matching': {'instruction': 'Match each feature to the correct description.',
               'pairs': [('Magnetic field around a wire',
                          'Concentric circles — stronger near the wire, strengthens with more current'),
                         ('Solenoid field', 'Uniform inside the coil, acts like a bar magnet with N and S poles'),
                         ('Why iron core is used',
                          'Iron is soft — easily demagnetised when current stops, so electromagnet switches off '
                          'cleanly'),
                         ('Increasing field strength', 'Increase current OR increase number of turns OR add iron core'),
                         ('Scrapyard crane',
                          'Electromagnet picks up ferromagnetic scrap when on, releases when current switched off')],
               'title': 'Electromagnetism Concepts'},
  'quiz': [{'opts': [('Iron is a soft magnetic material — it quickly loses magnetism when the current is switched off, '
                      'so the electromagnet can be turned off easily',
                      True),
                     ('Iron is harder than steel — it is more durable and resists damage', False),
                     ('Iron has higher electrical conductivity than steel — more current flows through it', False),
                     ('Steel would make the magnet too strong — iron limits the field to a safe level', False)],
            'q': 'Why is an iron core used in an electromagnet instead of a steel core?',
            'wrong_explanations': {1: "Steel is harder mechanically, but in magnetism 'hard' means it RETAINS "
                                      'magnetism — which is not wanted for a switchable electromagnet.',
                                   2: 'The iron core is not in the electrical circuit — it is inside the coil. Current '
                                      'flows through the wire coil, not the core.',
                                   3: 'The goal is NOT to limit strength — electromagnets are made as strong as '
                                      'possible. The issue is being able to switch off.'}},
           {'opts': [('The field doubles in strength — magnetic field strength is directly proportional to current',
                      True),
                     ('The field halves — more current creates resistance which reduces the field', False),
                     ('The field stays the same — only the number of turns affects field strength', False),
                     ('The field quadruples — field strength increases with current squared', False)],
            'q': "What happens to the strength of an electromagnet's field when the current is doubled?",
            'wrong_explanations': {1: 'The magnetic field of an electromagnet is proportional to current (and to '
                                      "number of turns) — it doesn't reduce when current increases.",
                                   2: 'BOTH current and number of turns affect field strength. Doubling current '
                                      'doubles the field.',
                                   3: 'Field strength is directly proportional to current (not current squared). '
                                      'Doubling current → double field.'}}],
  'rp': 'RP21 (Physics) — Investigate the factors affecting the strength of an electromagnet (number of turns, '
        'current). Plot field strength vs current or turns.',
  'spec': '6.7.2.1',
  'summary': 'Describe the magnetic field around a current-carrying wire, solenoid and electromagnet.',
  'theory': [{'content': 'A current-carrying conductor produces a MAGNETIC FIELD around it.\n'
                         '\n'
                         'For a STRAIGHT WIRE:\n'
                         'Field lines form CONCENTRIC CIRCLES around the wire.\n'
                         'The field is in a PLANE PERPENDICULAR to the wire.\n'
                         'DIRECTION: given by the RIGHT-HAND RULE — point thumb in direction of conventional current '
                         '(+ to −), fingers curl in direction of field lines.\n'
                         '\n'
                         'STRENGTH depends on:\n'
                         'SIZE OF CURRENT — larger current → stronger field.\n'
                         'DISTANCE FROM WIRE — further away → weaker field.\n'
                         '\n'
                         'This was discovered by Oersted (1820) — a compass placed near a current-carrying wire '
                         'deflected. First evidence that electric current and magnetism are related.',
              'heading': 'Magnetic Field Around a Current-Carrying Wire'},
             {'content': 'A SOLENOID is a coil of wire. When current flows, it produces a uniform magnetic field '
                         'INSIDE the coil.\n'
                         '\n'
                         'FIELD PATTERN:\n'
                         'Outside the solenoid: similar to a bar magnet — lines from N to S.\n'
                         'Inside the solenoid: uniform, parallel field lines along the axis.\n'
                         'The solenoid acts like a BAR MAGNET — has a definite north and south end.\n'
                         '\n'
                         'IDENTIFYING POLES:\n'
                         'Right-hand rule for solenoid: curl fingers in direction of conventional current flow around '
                         'the coil → thumb points towards NORTH pole.\n'
                         'Alternatively: view each end — if current flows ANTICLOCKWISE = NORTH; CLOCKWISE = SOUTH.\n'
                         '\n'
                         "STRENGTH of solenoid's field:\n"
                         'Increase CURRENT → stronger field.\n'
                         'Increase NUMBER OF TURNS → stronger field.\n'
                         'Add IRON CORE → much stronger field (core becomes an induced magnet).',
              'heading': 'The Solenoid'},
             {'content': 'An ELECTROMAGNET is a solenoid with an IRON CORE.\n'
                         '\n'
                         'Why iron (not steel)?\n'
                         'IRON is a SOFT magnetic material — easily magnetised and demagnetised.\n'
                         'When current is OFF → iron loses its magnetism quickly → electromagnet switches OFF.\n'
                         'STEEL would retain magnetism even when current is off — less useful as a switch.\n'
                         '\n'
                         'ADVANTAGES over permanent magnets:\n'
                         'Can be switched on and off.\n'
                         'Strength can be controlled by changing current.\n'
                         'Polarity can be reversed by reversing current direction.\n'
                         '\n'
                         'APPLICATIONS:\n'
                         'ELECTRIC BELL: electromagnet attracts striker → bell rings → circuit broken → striker '
                         'returns → repeat.\n'
                         'ELECTRIC CRANE (scrapyard): picks up ferromagnetic scrap when on → releases when off.\n'
                         'CIRCUIT BREAKER (relay): electromagnet pulls a switch to break a circuit.\n'
                         'MAGLEV TRAINS: electromagnets in track repel magnets in train → train levitates.\n'
                         'MRI SCANNER: powerful electromagnets (superconducting) create strong, uniform field.\n'
                         'SPEAKERS: varying current → changing force on cone → sound.',
              'heading': 'Electromagnets'}],
  'title': 'Electromagnetism',
  'triple_only': None,
  'variables': []}],

"space": [{'common_mistake': 'Geostationary orbits are above the EQUATOR and have a period of exactly 24 hours — they appear '
                    'stationary from Earth. LEO satellites have much shorter periods (90 minutes). The Sun is NOT at '
                    'the exact centre of planetary orbits — orbits are slightly elliptical, with the Sun at one focus.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'solar-system-gravity',
  'key_note': 'Solar System: Sun + 8 planets + moons, asteroids, comets. Gravity provides centripetal force for '
              'orbits. Closer orbit = faster speed. Geostationary: 36,000 km, 24-hour period, stationary above '
              'equator. LEO: 200–2000 km, 90-min period. 1 light-year = 9.46 × 10¹⁵ m.',
  'matching': {'instruction': 'Match each body to its description.',
               'pairs': [('Geostationary satellite',
                          '36,000 km altitude, 24-hour period, appears stationary — used for communications'),
                         ('Low Earth orbit (LEO)',
                          '200–2000 km altitude, ~90 min period — used for ISS, Earth observation'),
                         ('Asteroid belt',
                          'Rocky bodies between Mars and Jupiter — remnants from Solar System formation'),
                         ('Light-year',
                          'Distance light travels in one year — 9.46 × 10¹⁵ m — used for interstellar distances')],
               'title': 'Solar System'},
  'quiz': [{'opts': [('The gravitational force is stronger closer to the Sun — planets need higher orbital speed to '
                      'prevent being pulled into the Sun (centripetal force = gravitational force)',
                      True),
                     ('Closer planets are smaller — lighter objects move faster', False),
                     ('Solar radiation pressure pushes planets outward — closer planets need to move faster to '
                      'counteract this',
                      False),
                     ('The Sun rotates and drags nearby planets along — faster rotation nearer the surface', False)],
            'q': 'Why do planets closer to the Sun orbit faster than those further away?',
            'wrong_explanations': {1: "Planetary size doesn't determine orbital speed — all objects at the same "
                                      'orbital radius orbit at the same speed regardless of mass.',
                                   2: 'Solar radiation pressure is negligible compared to gravity for planetary '
                                      'motion.',
                                   3: "The Sun's rotation doesn't drag planets — planetary orbits are determined by "
                                      'gravity and initial velocities.'}},
           {'opts': [("Geostationary satellites remain over a fixed point on Earth's surface — dishes can point "
                      'permanently at them without tracking',
                      True),
                     ('Geostationary satellites are closer to Earth — signals have shorter distances to travel and '
                      'less delay',
                      False),
                     ('Geostationary satellites orbit faster — more data can be transmitted per second', False),
                     ('There are more geostationary satellites than LEO satellites — better coverage', False)],
            'q': 'What is the advantage of geostationary satellites over low Earth orbit satellites for '
                 'communications?',
            'wrong_explanations': {1: 'Geostationary satellites are actually 36,000 km away — much FURTHER than LEO '
                                      '(~400 km for ISS). Signal delay is greater for geostationary.',
                                   2: 'Geostationary satellites orbit SLOWER (24-hour period) than LEO satellites (90 '
                                      'minutes).',
                                   3: 'There are actually more LEO satellites than geostationary — but their movement '
                                      'means complex tracking is required.'}}],
  'rp': None,
  'spec': '6.8.1 (physics only)',
  'summary': 'Describe the scale and structure of the Solar System and explain orbital motion using gravity.',
  'theory': [{'content': 'Our SOLAR SYSTEM consists of:\n'
                         'The SUN — a star at the centre; contains ~99.8% of the total mass of the Solar System.\n'
                         'EIGHT PLANETS — orbit the Sun in approximately circular or elliptical orbits.\n'
                         'DWARF PLANETS — e.g. Pluto, Ceres — smaller bodies.\n'
                         'MOONS — natural satellites orbiting planets.\n'
                         'ASTEROID BELT — rocky bodies between Mars and Jupiter.\n'
                         'COMETS — icy bodies with highly elliptical orbits.\n'
                         '\n'
                         'PLANETS (in order from the Sun):\n'
                         'Mercury, Venus, Earth, Mars | Jupiter, Saturn, Uranus, Neptune.\n'
                         "Memory: 'My Very Excellent Mother Just Served Us Noodles'\n"
                         '\n'
                         'SCALE:\n'
                         'Earth–Sun distance: 1 AU = 1.5 × 10¹¹ m.\n'
                         'Nearest star (Proxima Centauri): ~4.25 light-years.\n'
                         'Our galaxy (Milky Way): ~100,000 light-years across.\n'
                         '1 light-year = 9.46 × 10¹⁵ m.',
              'heading': 'The Solar System'},
             {'content': 'Planets, moons and satellites stay in orbit due to GRAVITY.\n'
                         '\n'
                         'GRAVITATIONAL FORCE:\n'
                         'All masses attract each other via gravity (a non-contact force).\n'
                         "The Sun's gravity keeps planets in orbit.\n"
                         "Earth's gravity keeps the Moon in orbit.\n"
                         'Gravity acts as the CENTRIPETAL FORCE for circular orbits — always directed towards the '
                         'centre.\n'
                         '\n'
                         'ORBITAL SPEED AND DISTANCE:\n'
                         'Planets closer to the Sun move FASTER — they need more speed to balance the stronger '
                         'gravitational pull.\n'
                         'Planets further from the Sun move SLOWER — in larger orbits.\n'
                         '\n'
                         'NATURAL SATELLITES:\n'
                         'Moon: natural satellite of Earth. Orbital period: ~27 days.\n'
                         'Moons of other planets: hundreds known.\n'
                         '\n'
                         'ARTIFICIAL SATELLITES:\n'
                         'High Earth orbit (geostationary): 35,786 km, 24-hour period. Appears stationary. Used for: '
                         'communications, weather.\n'
                         'Low Earth orbit (LEO): 200–2000 km, ~90 min period. Used for: ISS, Earth observation, GPS.\n'
                         'Higher orbit = slower speed, longer period.',
              'heading': 'Orbital Motion and Gravity'},
             {'content': 'STARS:\n'
                         'The Sun is a star — a large ball of plasma undergoing nuclear fusion.\n'
                         'Stars are grouped into GALAXIES.\n'
                         'Milky Way: our galaxy, ~200–400 billion stars.\n'
                         'Nearest galaxy to us: Andromeda (~2.5 million light-years).\n'
                         '\n'
                         'UNIVERSE:\n'
                         'Contains ~2 trillion galaxies — observable universe ~93 billion light-years in diameter.\n'
                         'Age of universe: ~13.8 billion years.\n'
                         '\n'
                         'DISTANCE MEASUREMENT:\n'
                         'Astronomical Unit (AU): average Earth-Sun distance — used within solar system.\n'
                         'Light-year: distance light travels in one year — used for interstellar distances.\n'
                         'Parsec: 3.26 light-years — used by professional astronomers.\n'
                         '\n'
                         'SPACE EXPLORATION:\n'
                         'Probes: Voyager 1 and 2, New Horizons, Mars rovers.\n'
                         'Telescopes: Hubble (visible), James Webb (infrared), Chandra (X-ray).\n'
                         'Human spaceflight: ISS — continuous human presence since 2000.',
              'heading': 'Beyond the Solar System'}],
  'title': 'Our Solar System and Gravity',
  'triple_only': 'Space physics (physics only) — entire topic not in Combined Science.',
  'variables': []},
 {'common_mistake': "PLANETARY NEBULA has nothing to do with planets — it's a cloud of gas ejected by a dying medium "
                    'star (named because early observers thought they resembled planets through telescopes). A WHITE '
                    "DWARF is not a main sequence star — it's a remnant with no active fusion. The SUN will become a "
                    'red giant then WHITE DWARF — not a supernova.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'stellar-evolution',
  'key_note': 'Star life cycle: nebula → protostar → main sequence (fusion of H→He, pressure balances gravity) → red '
              'giant/supergiant → white dwarf/supernova → neutron star/black hole. Mass determines fate. Heavy '
              'elements made in supernovae. Sun: main sequence for ~10 billion years total, then red giant → planetary '
              'nebula → white dwarf.',
  'matching': {'instruction': 'Match each star stage to its description.',
               'pairs': [('Protostar',
                          'Collapsing nebula — gravitational PE converts to thermal; before fusion begins'),
                         ('Main sequence', 'Stable stage — fusion of H to He; radiation pressure balances gravity'),
                         ('Red giant', "H exhausted in core — outer layers expand and cool; Sun's eventual fate"),
                         ('Supernova',
                          'Massive star collapse — creates heavy elements; leaves neutron star or black hole'),
                         ('White dwarf',
                          'Core remnant of medium star — no fusion; slowly cools over billions of years')],
               'title': 'Stellar Life Cycle'},
  'quiz': [{'opts': [('The outward radiation pressure from nuclear fusion in the core exactly balances the inward '
                      'gravitational pull — maintaining equilibrium',
                      True),
                     ('The star constantly gains mass from surrounding gas clouds — replenishing the fuel', False),
                     ('Gravity and fusion both decrease together — the star slowly shrinks at the same rate it cools',
                      False),
                     ('Main sequence stars do not actually use up their fuel — fusion is completely efficient', False)],
            'q': 'Why does a star on the main sequence remain stable for billions of years?',
            'wrong_explanations': {1: 'Stars do gain some mass from surrounding material, but the key stability '
                                      'mechanism is the pressure-gravity balance.',
                                   2: 'Both gravity and fusion change as the star evolves — but during the stable main '
                                      'sequence phase they are in equilibrium, not both decreasing.',
                                   3: 'Stars do use up their fuel — they have a finite lifetime. The Sun will exhaust '
                                      'its H in ~5 billion years.'}},
           {'opts': [('Elements heavier than iron can only be created in supernova explosions — relatively rare events '
                      'that scatter these elements across space',
                      True),
                     ('Heavy elements are unstable — they decay quickly and cannot accumulate in large amounts', False),
                     ('Heavy elements sink to the centre of planets and stars — not observable from the surface',
                      False),
                     ('The Big Bang only produced hydrogen and helium — all heavier elements are rare primordial '
                      'leftovers',
                      False)],
            'q': 'Why are elements heavier than iron (like gold and uranium) only found in tiny amounts in the '
                 'universe?',
            'wrong_explanations': {1: 'While some heavy elements are unstable (radioactive), many like gold are stable '
                                      '— the rarity is due to the limited production mechanism (supernovae), not '
                                      'instability.',
                                   2: 'Heavy elements do accumulate in planetary cores (iron, nickel) — but the rarity '
                                      'is about production quantity, not settling.',
                                   3: 'The Big Bang produced only H and He. Heavier elements are made in stars and '
                                      'supernovae — but elements heavier than Fe specifically require supernova '
                                      'conditions.'}}],
  'rp': None,
  'spec': '6.8.2 (physics only)',
  'summary': 'Describe the life cycle of stars of different masses from nebula to final remnant.',
  'theory': [{'content': 'All stars form from clouds of gas and dust called NEBULAE (singular: nebula).\n'
                         '\n'
                         'FORMATION PROCESS:\n'
                         '1. NEBULA: cloud of hydrogen (and other gases) and dust — remnants of previous stars.\n'
                         '2. PROTOSTAR: gravity pulls gas and dust together → cloud collapses → heats up as '
                         'gravitational PE converts to thermal energy.\n'
                         '3. MAIN SEQUENCE: when temperature is high enough (~10 million °C at core) → NUCLEAR FUSION '
                         'begins.\n'
                         '   H → He fusion in the core. Outward radiation pressure from fusion BALANCES inward '
                         'gravitational force → stable star.\n'
                         '\n'
                         'Our Sun is currently a MAIN SEQUENCE star — has been for ~4.6 billion years.\n'
                         'Expected to remain on the main sequence for another ~5 billion years.\n'
                         '\n'
                         'SIZE DETERMINES FATE:\n'
                         "Star's mass determines its entire life cycle and ultimate fate.",
              'heading': 'Formation of Stars'},
             {'content': 'MAIN SEQUENCE (billions of years):\n'
                         'Fuses hydrogen to helium in the core.\n'
                         'Stable — radiation pressure balances gravity.\n'
                         '\n'
                         'RED GIANT (when H runs out in core):\n'
                         'Core contracts and heats up → H fusion in a shell around the core → helium fusion in core.\n'
                         'Outer layers EXPAND enormously → star becomes cooler and REDDER.\n'
                         'Sun will expand to ~200× current size — will engulf Mercury, Venus, possibly Earth.\n'
                         '\n'
                         'PLANETARY NEBULA:\n'
                         'Outer layers ejected — forms a beautiful expanding shell of glowing gas.\n'
                         'BRIEFLY illuminated by the central remnant.\n'
                         '\n'
                         'WHITE DWARF:\n'
                         "Core remnant left behind — hot, dense, about Earth's size.\n"
                         'No fusion occurring — slowly cools over billions of years.\n'
                         'Eventually becomes a cold BLACK DWARF (takes longer than current age of universe).',
              'heading': 'Life Cycle — Small to Medium Stars (like our Sun)'},
             {'content': "Massive stars (>8× Sun's mass) live shorter, more dramatic lives.\n"
                         '\n'
                         'MAIN SEQUENCE (millions of years — much shorter than Sun):\n'
                         'More massive → more gravitational compression → hotter core → faster fusion → shorter '
                         'lifetime.\n'
                         '\n'
                         'RED SUPERGIANT:\n'
                         'Expands to enormous size after H exhausted.\n'
                         'Fuses progressively heavier elements: He → C → O → ... → iron.\n'
                         'Iron cannot be fused to release energy — fusion of iron requires energy input.\n'
                         '\n'
                         'SUPERNOVA:\n'
                         'Core suddenly collapses when iron builds up → massive shockwave → SUPERNOVA explosion.\n'
                         'Briefest moment can outshine entire galaxy.\n'
                         'CREATES all elements heavier than iron (gold, uranium, lead) — scattered into space.\n'
                         'This is the origin of heavy elements on Earth.\n'
                         '\n'
                         'FINAL REMNANT depends on remaining core mass:\n'
                         'Moderate mass: NEUTRON STAR — incredibly dense; a teaspoon weighs ~1 billion tonnes.\n'
                         'Very high mass: BLACK HOLE — gravity so strong that even light cannot escape.\n'
                         '\n'
                         'COMPLETE CYCLE:\n'
                         'Nebula → protostar → main sequence → red supergiant → supernova → neutron star or black '
                         'hole\n'
                         'Ejected material forms new nebulae → new star systems (including planetary systems with '
                         'heavy elements).',
              'heading': 'Life Cycle — Massive Stars'}],
  'title': 'The Life Cycle of a Star',
  'triple_only': 'Stellar evolution (physics only) — not in Combined Science.',
  'variables': []},
 {'common_mistake': 'Red-shift does NOT mean galaxies are moving THROUGH space away from us — it means SPACE ITSELF is '
                    'expanding between galaxies. The Earth is not at the centre of the universe — all observers in any '
                    'galaxy would see other galaxies receding. The Big Bang was not an explosion in an existing space '
                    '— it was the beginning of space and time itself.',
  'equations': ["v = H₀ × d  (Hubble's Law)"],
  'fifas': [],
  'higher': None,
  'id': 'red-shift-big-bang',
  'key_note': "Red-shift: distant galaxies' light stretched to longer wavelengths → moving away → universe expanding. "
              "Hubble's Law: v = H₀d (faster recession = further away). Big Bang: ~13.8 billion years ago, hot dense "
              'singularity. Evidence: red-shift, CMBR (2.7 K microwave background), H/He abundance. CMBR = strongest '
              'evidence.',
  'matching': {'instruction': 'Match each piece of evidence to the Big Bang theory.',
               'pairs': [('Red-shift of galaxies',
                          'Nearly all galaxies moving away — greater red-shift for more distant galaxies — universe '
                          'expanding'),
                         ('Cosmic Microwave Background Radiation',
                          'Faint microwave radiation from all directions — afterglow of the hot early universe at 2.7 '
                          'K'),
                         ('H/He abundance',
                          '~75% hydrogen, ~25% helium — matches Big Bang nucleosynthesis predictions'),
                         ("Hubble's Law",
                          'Recession speed ∝ distance (v = H₀d) — first observational evidence for expansion')],
               'title': 'Evidence for the Big Bang'},
  'quiz': [{'opts': [('The universe is expanding — all distant galaxies are moving away, with more distant galaxies '
                      "receding faster (Hubble's Law)",
                      True),
                     ('Distant galaxies are very hot — the red colour indicates high temperature', False),
                     ('The universe is rotating — galaxies on the far side are moving away as it spins', False),
                     ('Distant galaxies are all moving towards a common point — the universe is contracting', False)],
            'q': 'What does the red-shift of distant galaxies tell us about the universe?',
            'wrong_explanations': {1: "Red-shift is not about colour of the galaxy — it's a Doppler shift in ALL "
                                      'wavelengths of light from the galaxy, indicating recession velocity.',
                                   2: "If the universe were rotating, we'd expect some galaxies to show red-shift and "
                                      'others blue-shift depending on direction. Nearly ALL show red-shift.',
                                   3: 'Red-shift means AWAY from us — if galaxies were all moving toward a common '
                                      "point, we'd see blue-shift from most directions."}},
           {'opts': [('It is a faint, uniform microwave glow from all directions — exactly matching the predicted '
                      'afterglow of the hot early universe cooled to ~2.7 K by 13.8 billion years of expansion',
                      True),
                     ('It shows that microwaves existed before the Big Bang — proving the universe had a beginning',
                      False),
                     ("It provides a current map of where all galaxies are moving — confirming Hubble's Law", False),
                     ('It was predicted after the Big Bang theory was developed — making it a confirmatory test rather '
                      'than a coincidence',
                      False)],
            'q': 'Why is the Cosmic Microwave Background Radiation (CMBR) considered the strongest evidence for the '
                 'Big Bang?',
            'wrong_explanations': {1: 'The CMBR is evidence OF the Big Bang, not evidence for events BEFORE it — there '
                                      'is no observable evidence from before the Big Bang.',
                                   2: 'The CMBR shows the distribution of early universe temperature fluctuations — it '
                                      'maps the early universe, not galaxy motion today.',
                                   3: 'The strength of the CMBR as evidence is that it was PREDICTED by the Big Bang '
                                      'theory and then discovered independently — the prediction of its temperature '
                                      'and uniformity is confirmed by observation.'}}],
  'rp': None,
  'spec': '6.8.3–6.8.4 (physics only)',
  'summary': 'Explain red-shift as evidence for an expanding universe and describe the Big Bang theory.',
  'theory': [{'content': 'RED-SHIFT: light from distant galaxies is shifted towards LONGER WAVELENGTHS (red end of the '
                         'spectrum).\n'
                         '\n'
                         'This is a DOPPLER EFFECT — similar to how a siren sounds lower-pitched as an ambulance '
                         'drives away.\n'
                         'When a light source moves AWAY from an observer, wavelengths are STRETCHED → shifted to '
                         'red.\n'
                         'When a light source moves TOWARDS an observer, wavelengths are COMPRESSED → blue-shift.\n'
                         '\n'
                         'OBSERVATIONS:\n'
                         'Nearly all galaxies show red-shift → nearly all galaxies are moving AWAY from us.\n'
                         'More distant galaxies show GREATER red-shift → moving away FASTER.\n'
                         'This relationship (velocity proportional to distance) was discovered by Edwin Hubble (1929) '
                         "— HUBBLE'S LAW.\n"
                         '\n'
                         "HUBBLE'S LAW:\n"
                         'Recession speed = Hubble constant × distance\n'
                         'v = H₀ × d\n'
                         '\n'
                         'H₀ ≈ 70 km/s/Mpc (current best estimate).\n'
                         '\n'
                         'KEY CONCLUSION:\n'
                         'The universe is EXPANDING — all galaxies moving away from all others.',
              'heading': 'Red-shift'},
             {'content': 'The expanding universe implies that in the past, all matter was closer together.\n'
                         'Extrapolating backwards → there was a point in time when all matter and energy was '
                         'concentrated in an incredibly hot, dense state — THE BIG BANG.\n'
                         '\n'
                         'BIG BANG TIMELINE:\n'
                         '~13.8 billion years ago: Big Bang — universe begins from an extremely hot, dense '
                         'singularity.\n'
                         'First 380,000 years: universe too hot for neutral atoms — opaque plasma.\n'
                         '380,000 years: universe cools enough for hydrogen atoms to form → universe becomes '
                         'transparent.\n'
                         'First light (CMBR emitted).\n'
                         'Hundreds of millions of years: first stars and galaxies form.\n'
                         '~4.6 billion years ago: Solar System forms.\n'
                         '~3.8 billion years ago: life on Earth begins.\n'
                         'Now: observable universe ~93 billion light-years in diameter.\n'
                         '\n'
                         'IMPORTANT: The Big Bang was not an explosion IN space — it was an expansion OF space itself. '
                         'There is no centre of the universe — all points are moving away from all others.',
              'heading': 'The Big Bang Theory'},
             {'content': 'EVIDENCE FOR THE BIG BANG:\n'
                         '\n'
                         '1. RED-SHIFT OF GALAXIES:\n'
                         'All distant galaxies show red-shift — moving away.\n'
                         "More distant → greater red-shift → faster recession (Hubble's Law).\n"
                         'First and most direct evidence for expansion.\n'
                         '\n'
                         '2. COSMIC MICROWAVE BACKGROUND RADIATION (CMBR):\n'
                         'Faint microwave radiation detected uniformly from all directions.\n'
                         'Predicted by Big Bang theory — the afterglow of the hot early universe, now cooled to ~2.7 '
                         'K.\n'
                         'Discovered accidentally by Penzias and Wilson (1964) — confirmed the Big Bang.\n'
                         'The most compelling evidence for the Big Bang theory.\n'
                         '\n'
                         '3. ABUNDANCE OF HYDROGEN AND HELIUM:\n'
                         'Big Bang nucleosynthesis predicted ~75% hydrogen, ~25% helium (by mass).\n'
                         'Observations of the oldest stars match this prediction remarkably well.\n'
                         '\n'
                         '4. LARGE-SCALE STRUCTURE:\n'
                         'The distribution of galaxies in the universe matches the predicted evolution from the Big '
                         'Bang.\n'
                         '\n'
                         'UNANSWERED QUESTIONS:\n'
                         "Dark matter: ~27% of universe's mass-energy is 'dark matter' — does not interact with "
                         'light.\n'
                         'Dark energy: ~68% — mysterious energy causing accelerating expansion.\n'
                         'Original cause of the Big Bang remains unknown.',
              'heading': 'Evidence for an Expanding Universe'}],
  'title': 'Red-shift and the Big Bang',
  'triple_only': 'Red-shift and Big Bang (physics only) — not in Combined Science.',
  'variables': [('v', 'Recession speed', 'km/s', 'km/s'),
                ('H₀', 'Hubble constant', 'km/s/Mpc', 'km/s/Mpc'),
                ('d', 'Distance to galaxy', 'Mpc', 'Mpc')]}],

}
