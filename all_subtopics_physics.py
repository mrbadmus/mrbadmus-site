#!/usr/bin/env python3
"""
Physics subtopics — Combined Foundation
AQA 8464 Physics spec 6.0
IN PROGRESS — Energy complete (7 subtopics)

Topics:
  6.1 Energy                        7  ✅
  6.2 Electricity                   (pending)
  6.3 Particle Model of Matter      (pending)
  6.4 Atomic Structure              (pending)
  6.5 Forces                        (pending)
  6.6 Waves                         (pending)
  6.7 Magnetism & Electromagnetism  (pending)
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

}
