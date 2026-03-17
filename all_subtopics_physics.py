#!/usr/bin/env python3
"""
Physics subtopics — Combined Foundation
AQA 8464 Physics spec 6.0
IN PROGRESS

  6.1 Energy            7  ✅
  6.2 Electricity      10  ✅
  6.3 Particle Model    6  ✅
  6.4 Atomic Structure  (pending)
  6.5 Forces            (pending)
  6.6 Waves             (pending)
  6.7 Magnetism         (pending)
"""

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
                ('P', 'Power', 'watts', 'W')]}],

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

}
