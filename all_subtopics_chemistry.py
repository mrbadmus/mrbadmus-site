#!/usr/bin/env python3
"""
Chemistry subtopics — Combined Foundation
AQA 8464 Chemistry spec 5.0
COMPLETE — 62 subtopics across all 10 topics

atomic-structure:  12
bonding:           12
quantitative:      5
chemical-changes:  10
energy-changes:    2
rates-equilibrium: 5
organic:           4
analysis:          4
atmosphere:        4
using-resources:   4
"""

CHEMISTRY_COLOR = "#FF6B6B"

CHEMISTRY_SUBTOPICS_ALL = {

"atomic-structure": [{'common_mistake': 'A COMPOUND is NOT a mixture. In a compound, elements are CHEMICALLY BONDED — you need a chemical '
                    'reaction to separate them (e.g. electrolysis to split water into hydrogen and oxygen). In a '
                    'MIXTURE, substances are just mixed — physical methods separate them. Water is a compound. '
                    'Saltwater is a mixture.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'atoms-elements-compounds',
  'key_note': 'Element: one type of atom. Compound: two or more elements chemically bonded — new properties, chemical '
              'separation only. Mixture: not bonded — keeps own properties, physical separation possible. Equations '
              'must be balanced — atoms conserved.',
  'matching': {'instruction': 'Sort each substance into the correct category.',
               'pairs': [('Element', 'Copper (Cu) — made of only copper atoms'),
                         ('Compound', 'Water (H₂O) — hydrogen and oxygen chemically bonded'),
                         ('Mixture', 'Air — nitrogen, oxygen and argon not chemically combined'),
                         ('Compound', 'Carbon dioxide (CO₂) — carbon and oxygen chemically bonded'),
                         ('Mixture', 'Crude oil — many different hydrocarbons mixed together'),
                         ('Element', 'Gold (Au) — one type of atom, listed on the periodic table')],
               'title': 'Element, Compound or Mixture?'},
  'quiz': [{'opts': [('In a compound, elements are chemically bonded in fixed proportions — a mixture is not bonded '
                      'and can be separated physically.',
                      True),
                     ('A compound contains only one type of atom. A mixture contains two or more types.', False),
                     ('A mixture is always a liquid. A compound is always a solid.', False),
                     ('They are the same — both describe combinations of different substances.', False)],
            'q': 'What is the key difference between a compound and a mixture?',
            'wrong_explanations': {1: 'One type of atom = ELEMENT. Compounds contain two or more elements chemically '
                                      'bonded.',
                                   2: 'Mixtures and compounds can be solids, liquids or gases — state does not define '
                                      'them.',
                                   3: 'Compounds and mixtures are fundamentally different — chemical bonding is the '
                                      'key distinction.'}},
           {'opts': [('A compound — iron sulfide — formed by chemical bonding between iron and sulfur', True),
                     ('A mixture — the iron and sulfur have blended more thoroughly', False),
                     ('An element — the sulfur has been destroyed leaving only iron', False),
                     ('A solution — the sulfur has dissolved into the iron', False)],
            'q': 'A student heats a mixture of iron filings and sulfur. A grey solid forms that cannot be separated '
                 'using a magnet. What has formed?',
            'wrong_explanations': {1: 'If it were still a mixture, the iron could be separated magnetically. Since it '
                                      'cannot, a chemical reaction has occurred.',
                                   2: 'Elements cannot be destroyed by chemical reactions — only rearranged into '
                                      'compounds.',
                                   3: 'Sulfur is a solid at these temperatures — it does not dissolve into iron.'}},
           {'opts': [('2H₂ + O₂ → 2H₂O', True),
                     ('H₂ + O₂ → H₂O', False),
                     ('H₂ + O₂ → H₂O₂', False),
                     ('2H₂ + 2O₂ → 2H₂O', False)],
            'q': 'Which equation is correctly balanced?',
            'wrong_explanations': {1: 'H₂ + O₂ → H₂O: left has 2 O atoms, right has only 1 O atom — not balanced.',
                                   2: 'H₂ + O₂ → H₂O₂: this equation is balanced (2H and 2O each side) but produces '
                                      'hydrogen peroxide (H₂O₂), not water. The question asks about water formation.',
                                   3: '2H₂ + 2O₂ → 2H₂O: left has 4 O atoms, right has only 2 O atoms — not '
                                      'balanced.'}},
           {'opts': [('Bronze — copper and tin metals mixed together, not chemically bonded', True),
                     ('Water — hydrogen and oxygen in a fixed 2:1 ratio', False),
                     ('Sodium chloride — sodium and chlorine in ionic bonds', False),
                     ('Carbon dioxide — carbon and oxygen in covalent bonds', False)],
            'q': 'Which of these is a mixture?',
            'wrong_explanations': {1: 'Water is a COMPOUND — hydrogen and oxygen are chemically bonded. Electrolysis '
                                      'is needed to separate them.',
                                   2: 'Sodium chloride is a COMPOUND — ionic bonds between Na⁺ and Cl⁻ ions.',
                                   3: 'Carbon dioxide is a COMPOUND — covalent bonds between C and O atoms.'}}],
  'rp': None,
  'spec': '5.1.1.1',
  'summary': 'Define atoms, elements and compounds and explain the differences between them.',
  'theory': [{'content': 'All substances are made of ATOMS — the smallest particles that cannot be broken down by '
                         'chemical means.\n'
                         '\n'
                         'An ELEMENT is a substance made of only ONE type of atom. Elements cannot be broken down into '
                         'simpler substances by chemical reactions.\n'
                         'There are 118 known elements — each has a unique symbol (e.g. C = carbon, O = oxygen, Fe = '
                         'iron, Na = sodium).\n'
                         'Elements are arranged in the PERIODIC TABLE in order of atomic number.\n'
                         '\n'
                         'A COMPOUND is a substance formed when two or more DIFFERENT elements are CHEMICALLY BONDED '
                         'together.\n'
                         'The properties of a compound are completely different from the properties of its elements.\n'
                         'Example: sodium (reactive metal) + chlorine (toxic green gas) → sodium chloride (table salt '
                         '— safe to eat).\n'
                         'Compounds can only be separated by chemical reactions — not physical methods.\n'
                         '\n'
                         'A MIXTURE contains two or more substances that are NOT chemically bonded — each keeps its '
                         'own properties.\n'
                         'Mixtures can be separated by physical methods (filtering, distillation, chromatography).\n'
                         'The proportions of substances in a mixture can vary.',
              'heading': 'Atoms — The Building Blocks of Matter'},
             {'content': 'Every compound has a CHEMICAL FORMULA showing which atoms are present and in what ratio.\n'
                         '\n'
                         'Examples:\n'
                         'H₂O — water: 2 hydrogen + 1 oxygen.\n'
                         'CO₂ — carbon dioxide: 1 carbon + 2 oxygen.\n'
                         'NaCl — sodium chloride: 1 sodium + 1 chlorine.\n'
                         'H₂SO₄ — sulfuric acid: 2 hydrogen + 1 sulfur + 4 oxygen.\n'
                         '\n'
                         'The small SUBSCRIPT numbers tell you how many atoms of each element are present.\n'
                         '\n'
                         'CHEMICAL EQUATIONS show what happens in a reaction:\n'
                         'Reactants → Products\n'
                         '\n'
                         'Equations must be BALANCED — the same number of each type of atom on both sides.\n'
                         'Atoms cannot be created or destroyed in a chemical reaction (law of conservation of mass).\n'
                         '\n'
                         'Balancing example:\n'
                         'Hydrogen + oxygen → water\n'
                         '2H₂ + O₂ → 2H₂O  ✓ (4 H and 2 O on each side)\n'
                         'H₂ + O₂ → H₂O  ✗ (unbalanced — 2 O on left, 1 O on right)',
              'heading': 'Chemical Formulae and Equations'},
             {'content': 'Here is a clear comparison of the three:\n'
                         '\n'
                         'ELEMENT:\n'
                         'One type of atom only.\n'
                         'Cannot be broken down chemically.\n'
                         'Has fixed properties.\n'
                         'Examples: iron (Fe), oxygen (O₂), gold (Au), sulfur (S).\n'
                         '\n'
                         'COMPOUND:\n'
                         'Two or more elements CHEMICALLY bonded in fixed proportions.\n'
                         'Has new, different properties from its elements.\n'
                         'Can only be separated by chemical reactions.\n'
                         'Examples: water (H₂O), carbon dioxide (CO₂), magnesium oxide (MgO).\n'
                         '\n'
                         'MIXTURE:\n'
                         'Two or more substances NOT chemically bonded.\n'
                         'Each component keeps its own properties.\n'
                         'Can be mixed in any proportions.\n'
                         'Separated by physical methods.\n'
                         'Examples: air, seawater, crude oil, bronze (copper + tin), ink.',
              'heading': 'Comparing Elements, Compounds and Mixtures'}],
  'title': 'Atoms, Elements and Compounds',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Filtration only removes INSOLUBLE solids. You CANNOT filter salt from water — salt is dissolved '
                    '(soluble). Use evaporation or distillation instead. Also: in distillation you collect the VAPOUR '
                    'that condenses — the liquid. Crystallisation collects the SOLID that forms as the solution cools.',
  'equations': ['Rf = distance moved by substance ÷ distance moved by solvent front'],
  'fifas': [{'label': 'Rf Value Calculation',
             'question': 'In a chromatography experiment, a dye spot moves 6.0 cm. The solvent front moves 9.0 cm. '
                         'Calculate the Rf value.',
             'steps': [('F', 'Rf = distance moved by substance ÷ distance moved by solvent'),
                       ('I', 'Rf = 6.0 ÷ 9.0'),
                       ('F', 'No unit conversion needed — Rf has no units'),
                       ('A', 'Rf = 0.67')]}],
  'higher': None,
  'id': 'mixtures',
  'key_note': 'Filtration: insoluble solid from liquid. Crystallisation: dissolved solid from solution (cool slowly). '
              'Simple distillation: liquid from solution. Fractional distillation: liquids with different boiling '
              'points. Chromatography: dissolved substances — Rf = substance distance ÷ solvent distance.',
  'matching': {'instruction': 'Match each mixture to the best separation technique.',
               'pairs': [('Filtration',
                          'Sand mixed with water — sand is insoluble and too large to pass through filter paper'),
                         ('Crystallisation',
                          'Salt dissolved in water — heat to saturate, cool slowly to form pure crystals'),
                         ('Simple distillation', 'Pure water from seawater — boil off and condense the water vapour'),
                         ('Fractional distillation', 'Crude oil — separate into fractions by different boiling points'),
                         ('Chromatography', 'Ink dyes — different dyes travel different distances in the solvent')],
               'title': 'Match the Separation Technique'},
  'quiz': [{'opts': [('Simple distillation — heat the seawater and condense the steam', True),
                     ('Filtration — filter through paper to remove the salt', False),
                     ('Chromatography — water travels faster than dissolved salts', False),
                     ('Crystallisation — cool the seawater to crystallise the water', False)],
            'q': 'A student wants to obtain pure water from seawater. Which technique should they use?',
            'wrong_explanations': {1: 'Filtration only removes INSOLUBLE solids — salt is dissolved in seawater so '
                                      'passes straight through filter paper.',
                                   2: 'Chromatography separates dissolved substances by their travel speed — it does '
                                      'not separate water from dissolved salts.',
                                   3: 'Crystallisation removes water to leave the SALT — the opposite of what is '
                                      'needed here.'}},
           {'opts': [('0.50 — Rf = 4.5 ÷ 9.0', True),
                     ('2.0 — Rf = 9.0 ÷ 4.5', False),
                     ('13.5 — adding the two distances', False),
                     ('4.5 — using just the distance the spot moved', False)],
            'q': 'In a chromatography experiment, a spot travels 4.5 cm and the solvent front travels 9.0 cm. What is '
                 'the Rf value?',
            'wrong_explanations': {1: 'Rf = 9.0 ÷ 4.5 = 2.0 — this is dividing the WRONG WAY. Rf is always substance ÷ '
                                      'solvent, and must be between 0 and 1.',
                                   2: 'Adding distances has no meaning. Rf = substance distance ÷ solvent distance = '
                                      '4.5 ÷ 9.0 = 0.50.',
                                   3: 'Just the distance alone gives no useful information — Rf is a ratio, which is '
                                      'why it has no units.'}},
           {'opts': [('Crude oil contains many liquids with different boiling points — fractional distillation '
                      'separates them into different fractions',
                      True),
                     ('Crude oil is a solid — simple distillation cannot be used on solids', False),
                     ('The fractions in crude oil are insoluble in each other — filtration would work just as well',
                      False),
                     ('Simple distillation uses too much energy for industrial use', False)],
            'q': 'Why is fractional distillation used to separate crude oil rather than simple distillation?',
            'wrong_explanations': {1: 'Crude oil is a LIQUID mixture — simple distillation collects one fraction at a '
                                      'time but cannot separate all components simultaneously.',
                                   2: 'The fractions IN crude oil mix readily — filtration only works for insoluble '
                                      'particles, not dissolved or miscible liquids.',
                                   3: 'Energy cost is relevant industrially, but the primary reason is that crude oil '
                                      'has many components with DIFFERENT boiling points that need to be separated '
                                      'simultaneously.'}}],
  'rp': 'RP1 — Investigate paper chromatography to separate and identify colours in inks or food dyes. Measure Rf '
        'values and compare to known standards.',
  'spec': '5.1.1.2',
  'summary': 'Describe physical methods for separating mixtures and the principles behind each.',
  'theory': [{'content': 'Many useful substances occur naturally as mixtures and must be separated to obtain pure '
                         'components.\n'
                         '\n'
                         'Examples:\n'
                         'Drinking water is purified from seawater or river water.\n'
                         'Crude oil (a mixture of hydrocarbons) is separated into petrol, diesel, jet fuel etc.\n'
                         'Ink contains different dyes that can be separated.\n'
                         '\n'
                         'The separation method depends on the PHYSICAL PROPERTIES of the substances:\n'
                         'Size of particles (filtration).\n'
                         'Boiling point (distillation).\n'
                         'Solubility in a solvent (chromatography).\n'
                         'Magnetic properties (magnetism).',
              'heading': 'Why Separate Mixtures?'},
             {'content': 'FILTRATION:\n'
                         'Separates an INSOLUBLE SOLID from a LIQUID.\n'
                         'Mixture is poured through filter paper in a funnel.\n'
                         'Liquid (filtrate) passes through the tiny pores.\n'
                         'Solid (residue) is too large to pass through — trapped in filter.\n'
                         'Example: separating sand from water; collecting a precipitate.\n'
                         '\n'
                         'EVAPORATION:\n'
                         'Removes a LIQUID (usually water) from a solution, leaving the dissolved solid.\n'
                         'The solution is heated — water evaporates.\n'
                         'The solid crystallises out as the solvent is removed.\n'
                         'Example: recovering salt from salt solution.\n'
                         '\n'
                         'CRYSTALLISATION:\n'
                         'More controlled than simple evaporation.\n'
                         'Heat solution to saturate it, then allow to COOL SLOWLY.\n'
                         'As temperature falls, solubility decreases — pure crystals form.\n'
                         'Better for producing large, regular, pure crystals.\n'
                         'Example: growing copper sulfate crystals from solution.',
              'heading': 'Filtration and Crystallisation'},
             {'content': 'SIMPLE DISTILLATION:\n'
                         'Separates a SOLUBLE SOLID from a LIQUID (or separates two liquids with very different '
                         'boiling points).\n'
                         'Liquid is heated → evaporates → vapour travels through condenser → cools → condenses as pure '
                         'liquid (distillate).\n'
                         'Solid or less volatile substance remains in flask.\n'
                         'Example: obtaining pure water from seawater.\n'
                         '\n'
                         'FRACTIONAL DISTILLATION:\n'
                         'Separates a MIXTURE OF LIQUIDS with different boiling points.\n'
                         'A fractionating column (tall, cooler at top) allows separation: lower boiling point '
                         'substances rise higher and condense at the top; higher boiling point substances condense '
                         'lower down.\n'
                         'Different fractions collected at different heights.\n'
                         'Example: separating crude oil; separating air into nitrogen, oxygen and argon.\n'
                         '\n'
                         'CHROMATOGRAPHY:\n'
                         'Separates DISSOLVED SUBSTANCES based on how far they travel through a medium in a solvent.\n'
                         'A spot is placed on chromatography paper and placed in a solvent (mobile phase).\n'
                         'The solvent travels up, carrying dissolved substances with it.\n'
                         'Different substances travel at different rates — they separate into distinct spots.\n'
                         'Used for: separating ink dyes, identifying food colourings, forensic analysis.\n'
                         '\n'
                         'Rf VALUE — identifies each substance:\n'
                         'Rf = distance moved by substance ÷ distance moved by solvent front\n'
                         'Each substance has a characteristic Rf value in a given solvent.',
              'heading': 'Distillation and Chromatography'}],
  'title': 'Mixtures and Separation Techniques',
  'triple_only': None,
  'variables': [('Rf', 'Retention factor (chromatography)', '', '')]},
 {'common_mistake': "In Rutherford's experiment, MOST particles passed STRAIGHT THROUGH — this is what shows atoms are "
                    'mostly empty space. Only a FEW bounced back. Students often get this backwards and say most '
                    'particles bounced back. The few that did bounce back were what proved the nucleus exists.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'model-of-the-atom',
  'key_note': 'Dalton: solid sphere. Thomson: plum pudding (electrons in positive mass). Rutherford: nuclear model — '
              'most particles pass through (empty space), a few bounce back (dense positive nucleus). Bohr: electrons '
              'in fixed shells. Each model revised due to new experimental evidence.',
  'matching': {'instruction': 'Match each atomic model to the scientist and what evidence led to it.',
               'pairs': [('Dalton', 'Solid indivisible sphere — no subatomic particles known at this time'),
                         ('Thomson', 'Plum pudding — discovery of the electron showed atoms had internal structure'),
                         ('Rutherford', 'Nuclear model — gold foil experiment showed a tiny dense positive nucleus'),
                         ('Bohr', 'Shell model — electrons orbit in fixed energy levels around the nucleus')],
               'title': 'Match the Model to its Scientist and Evidence'},
  'quiz': [{'opts': [('Atoms are mostly empty space — most particles found no matter to deflect them', True),
                     ('Gold atoms are very large — the particles passed through the gaps between atoms', False),
                     ('Alpha particles are too fast to be deflected', False),
                     ('The plum pudding model was correct — the positive charge is spread out', False)],
            'q': "In Rutherford's gold foil experiment, most alpha particles passed straight through the foil. What "
                 'does this tell us?',
            'wrong_explanations': {1: 'Atomic SIZE explains why particles might miss atoms, not why they pass THROUGH '
                                      'them. The key conclusion is that the atom is mostly empty space internally.',
                                   2: 'Alpha particles can be deflected — some WERE deflected at large angles, showing '
                                      'the nucleus exists.',
                                   3: 'The plum pudding model predicted only SMALL deflections. The large angle '
                                      'deflections and back-scattering DISPROVED the plum pudding model.'}},
           {'opts': [('The gold foil experiment produced results that could not be explained by the plum pudding model '
                      '— the new model fitted the evidence',
                      True),
                     ('Rutherford was more famous than Thomson, so his model was believed', False),
                     ('The plum pudding model was proposed before electrons were discovered', False),
                     ('Both models are still equally accepted today', False)],
            'q': "Why did the scientific community accept Rutherford's nuclear model over Thomson's plum pudding "
                 'model?',
            'wrong_explanations': {1: 'Scientific acceptance is based on EVIDENCE, not reputation — the gold foil '
                                      'results clearly contradicted the plum pudding model.',
                                   2: "Thomson's plum pudding model was specifically based on and designed to explain "
                                      'the discovery of electrons.',
                                   3: "Rutherford's nuclear model replaced the plum pudding model — it is not still "
                                      'equally accepted, though both are discussed historically.'}}],
  'rp': None,
  'spec': '5.1.1.3',
  'summary': 'Describe how the model of the atom developed as new evidence was discovered.',
  'theory': [{'content': 'Scientific models are the best current explanation of how something works — but they must '
                         'change when new experimental evidence cannot be explained by the existing model.\n'
                         '\n'
                         'The history of atomic models is a perfect example of how science works:\n'
                         'A model is proposed → experiments are done → if results conflict with the model, the model '
                         'is revised.\n'
                         '\n'
                         'The key models in chronological order:\n'
                         "1. Dalton's solid sphere (1803)\n"
                         "2. Thomson's plum pudding model (1897)\n"
                         "3. Rutherford's nuclear model (1911)\n"
                         "4. Bohr's shell model (1913)",
              'heading': 'Why Scientific Models Change'},
             {'content': "DALTON'S MODEL (1803):\n"
                         'Atoms are solid, indivisible spheres.\n'
                         'Different elements have differently sized spheres.\n'
                         'Atoms cannot be split, created or destroyed.\n'
                         'Revised when electrons were discovered.\n'
                         '\n'
                         "THOMSON'S PLUM PUDDING MODEL (1897):\n"
                         'Discovery of the ELECTRON — a tiny negatively charged particle inside atoms — proved atoms '
                         'were not solid or indivisible.\n'
                         'Thomson proposed: an atom is a ball of POSITIVE CHARGE with ELECTRONS dotted throughout — '
                         'like plums in a pudding (or currants in a bun).\n'
                         "Revised after Rutherford's gold foil experiment.\n"
                         '\n'
                         "RUTHERFORD'S NUCLEAR MODEL (1911):\n"
                         'Rutherford fired positively charged ALPHA PARTICLES at a very thin sheet of gold foil.\n'
                         'Expected (plum pudding): all particles would pass through with small deflections.\n'
                         'Observed:\n'
                         'MOST particles passed STRAIGHT THROUGH — atoms are mostly empty space.\n'
                         'SOME were deflected at large angles — something positive inside repelled them.\n'
                         'A FEW bounced STRAIGHT BACK — hit something very dense and concentrated.\n'
                         'Conclusion: atoms have a tiny, dense, positively charged NUCLEUS at the centre, surrounded '
                         'by mostly empty space with electrons.\n'
                         '\n'
                         "BOHR'S MODEL (1913):\n"
                         'Bohr proposed electrons orbit in fixed SHELLS (energy levels) at specific distances from the '
                         'nucleus.\n'
                         'Each shell has a fixed energy — electrons can jump between shells by absorbing or emitting '
                         'energy.',
              'heading': 'From Solid Sphere to Nuclear Model'},
             {'content': "After Bohr's model, further work led to the modern understanding:\n"
                         '\n'
                         'Protons and neutrons were later identified in the nucleus.\n'
                         'NEUTRON discovery (Chadwick, 1932) explained why atomic mass was not just the number of '
                         'protons.\n'
                         '\n'
                         'Why each model was better:\n'
                         'Dalton → Thomson: discovery of the electron showed atoms had internal structure.\n'
                         'Thomson → Rutherford: gold foil experiment showed positive charge was concentrated in a tiny '
                         'nucleus, not spread throughout.\n'
                         'Rutherford → Bohr: observed line spectra of hydrogen showed electrons could only occupy '
                         'specific energy levels.\n'
                         '\n'
                         'This chain of model improvements shows the power of the scientific method — each experiment '
                         'built on previous knowledge and revealed new detail about atomic structure.',
              'heading': 'The Modern Understanding'}],
  'title': 'Development of the Model of the Atom',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The number of PROTONS never changes in a chemical reaction — only electrons are gained or lost to '
                    'form ions. Also: electrons have negligible mass — almost all atomic mass is in the nucleus '
                    '(protons + neutrons both have relative mass 1). The atom is MOSTLY EMPTY SPACE — the nucleus is '
                    '10,000 times smaller than the atom.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'subatomic-particles',
  'key_note': 'Proton: +1, mass 1, nucleus. Neutron: 0, mass 1, nucleus. Electron: −1, mass ~0, shells. Neutral atom: '
              'protons = electrons. Atom loses electrons → positive ion. Atom gains electrons → negative ion. Atom '
              'mostly empty space — nucleus is tiny.',
  'matching': {'instruction': 'Match each particle to its charge, mass and location.',
               'pairs': [('Proton', 'Relative charge +1, mass 1 — in the nucleus'),
                         ('Neutron', 'Relative charge 0, mass 1 — in the nucleus'),
                         ('Electron', 'Relative charge −1, mass ~0 — in shells around the nucleus'),
                         ('Na⁺ ion', 'Sodium atom that has LOST one electron — 11 protons, 10 electrons'),
                         ('Cl⁻ ion', 'Chlorine atom that has GAINED one electron — 17 protons, 18 electrons')],
               'title': 'Match the Subatomic Particle'},
  'quiz': [{'opts': [('10 — magnesium loses 2 electrons from its original 12', True),
                     ('14 — magnesium gains 2 electrons to form a +2 ion', False),
                     ('12 — the number of electrons stays the same', False),
                     ('2 — only the outermost electrons remain', False)],
            'q': 'A magnesium atom (Mg, atomic number 12) forms a Mg²⁺ ion. How many electrons does the ion have?',
            'wrong_explanations': {1: 'Gaining electrons gives a NEGATIVE charge. Mg²⁺ is POSITIVE, so electrons were '
                                      'LOST.',
                                   2: 'Mg²⁺ is formed by losing 2 electrons. Original: 12 electrons. After loss: 12 − '
                                      '2 = 10 electrons.',
                                   3: 'Only the 2 outermost electrons are lost — but the ion still has all 10 '
                                      'remaining electrons, not just 2.'}},
           {'opts': [('The number of protons (+1 each) equals the number of electrons (−1 each) — the charges cancel',
                      True),
                     ('Protons and neutrons have equal and opposite charges that cancel', False),
                     ('Electrons are on the outside and shield the positive nucleus', False),
                     ('The atom vibrates too fast for any charge to accumulate', False)],
            'q': 'Why does an atom have no overall electrical charge?',
            'wrong_explanations': {1: 'Neutrons have ZERO charge — they cannot cancel proton charges. Charge '
                                      'neutrality comes from protons balancing electrons.',
                                   2: 'Shielding describes how inner electrons reduce the attractive force on outer '
                                      'electrons — it does not explain why atoms are electrically neutral.',
                                   3: 'Vibration does not affect electrical charge — the neutrality is a consequence '
                                      'of proton and electron numbers being equal.'}}],
  'rp': None,
  'spec': '5.1.1.4–5.1.1.5',
  'summary': 'Describe the relative charges and masses of protons, neutrons and electrons and the scale of atoms.',
  'theory': [{'content': 'Every atom contains three types of subatomic particle:\n'
                         '\n'
                         'PROTON:\n'
                         'Found in the NUCLEUS.\n'
                         'Relative charge: +1.\n'
                         'Relative mass: 1.\n'
                         '\n'
                         'NEUTRON:\n'
                         'Found in the NUCLEUS.\n'
                         'Relative charge: 0 (neutral).\n'
                         'Relative mass: 1.\n'
                         '\n'
                         'ELECTRON:\n'
                         'Found in SHELLS (energy levels) around the nucleus.\n'
                         'Relative charge: −1.\n'
                         'Relative mass: approximately 1/1836 — effectively 0 in relative terms.\n'
                         '\n'
                         'Atoms are electrically NEUTRAL because the number of protons = number of electrons (positive '
                         'and negative charges cancel).\n'
                         '\n'
                         "The NUCLEUS contains protons and neutrons — almost all of the atom's mass is concentrated "
                         'here.\n'
                         'Electrons contribute negligible mass.',
              'heading': 'The Three Subatomic Particles'},
             {'content': 'An ION is a charged particle formed when an atom gains or loses electrons.\n'
                         '\n'
                         'ATOM LOSES ELECTRONS → positive ion (cation)\n'
                         'Example: Na → Na⁺ + e⁻ (sodium loses 1 electron → +1 charge)\n'
                         'Example: Mg → Mg²⁺ + 2e⁻ (magnesium loses 2 electrons → +2 charge)\n'
                         '\n'
                         'ATOM GAINS ELECTRONS → negative ion (anion)\n'
                         'Example: Cl + e⁻ → Cl⁻ (chlorine gains 1 electron → −1 charge)\n'
                         'Example: O + 2e⁻ → O²⁻ (oxygen gains 2 electrons → −2 charge)\n'
                         '\n'
                         'The charge on an ion tells you how many electrons were gained or lost.\n'
                         'The NUMBER OF PROTONS never changes in a chemical reaction — only electron numbers change.',
              'heading': 'Ions — When Atoms Gain or Lose Electrons'},
             {'content': 'Atoms are incredibly small — they cannot be seen with a light microscope.\n'
                         '\n'
                         'A typical atomic radius ≈ 1 × 10⁻¹⁰ m (0.1 nanometres).\n'
                         'A human hair is about 1 million atoms wide.\n'
                         'A grain of sand contains approximately 10¹⁸ atoms.\n'
                         '\n'
                         'The NUCLEUS is even smaller — about 10,000 times smaller than the whole atom:\n'
                         'Nuclear radius ≈ 1 × 10⁻¹⁴ m\n'
                         '\n'
                         'This means the atom is almost entirely EMPTY SPACE — the nucleus is tiny compared to the '
                         'overall size of the atom, with electrons in the vast space around it.\n'
                         '\n'
                         'This is consistent with what Rutherford found — most alpha particles passing straight '
                         'through gold foil without hitting anything.',
              'heading': 'Size and Scale of Atoms'}],
  'title': 'Subatomic Particles',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Ar is a WEIGHTED average — not a simple average. Chlorine has Ar 35.5 because ~75% is Cl-35 and '
                    'only ~25% is Cl-37. If both were 50/50, Ar would be 36. The heavier isotope has LESS influence '
                    "because it's less abundant. Also: isotopes have SAME chemical properties (same electrons) but "
                    'DIFFERENT physical properties (different mass).',
  'equations': ['Mass number = protons + neutrons',
                'Neutrons = mass number − atomic number',
                'Ar = Σ(% abundance × mass number) ÷ 100'],
  'fifas': [{'label': 'Relative Atomic Mass Calculation',
             'question': 'Boron has two isotopes: 20% boron-10 and 80% boron-11. Calculate the relative atomic mass of '
                         'boron.',
             'steps': [('F', 'Ar = Σ(% abundance × mass number) ÷ 100'),
                       ('I', 'Ar = (20 × 10) + (80 × 11) ÷ 100'),
                       ('F', 'Ar = (200 + 880) ÷ 100 = 1080 ÷ 100'),
                       ('A', 'Ar = 10.8')]}],
  'higher': None,
  'id': 'relative-atomic-mass',
  'key_note': 'Atomic number = protons. Mass number = protons + neutrons. Neutrons = mass number − atomic number. '
              'Isotopes: same element, same protons, different neutrons — same chemical, different physical '
              'properties. Ar = weighted average of isotope masses.',
  'matching': {'instruction': 'Match each term to its correct definition.',
               'pairs': [('Atomic number', 'Number of protons — unique to each element'),
                         ('Mass number', 'Total protons + neutrons in the nucleus'),
                         ('Isotopes', 'Same element, same protons, different number of neutrons'),
                         ('Relative atomic mass', 'Weighted average of all isotope masses — often not a whole number'),
                         ('Number of neutrons', 'Mass number minus atomic number')],
               'title': 'Atomic Number, Mass Number and Isotopes'},
  'quiz': [{'opts': [('Same: atomic number (17 protons and 17 electrons). Different: mass number — Cl-35 has 18 '
                      'neutrons, Cl-37 has 20 neutrons.',
                      True),
                     ('Same: mass number. Different: atomic number and proton count.', False),
                     ('Same: everything — isotopes are identical atoms.', False),
                     ('Same: neutron number. Different: proton number.', False)],
            'q': 'Chlorine-35 and chlorine-37 are isotopes. What is the same and what differs between them?',
            'wrong_explanations': {1: 'If mass numbers were the same they would be identical — isotopes are DEFINED by '
                                      'having different mass numbers.',
                                   2: 'Isotopes DO have the same chemical properties — but they are NOT identical. '
                                      'They differ in neutron count and mass.',
                                   3: 'If neutron numbers were the same but proton numbers differed, they would be '
                                      'different ELEMENTS — not isotopes.'}},
           {'opts': [('63.8 — Ar = (60 × 63 + 40 × 65) ÷ 100 = 6380 ÷ 100', True),
                     ('64.0 — simple average of 63 and 65', False),
                     ('128 — total of both mass numbers added together', False),
                     ('63 — just the most abundant isotope mass', False)],
            'q': 'An element has two isotopes: 60% at mass 63 and 40% at mass 65. What is its Ar?',
            'wrong_explanations': {1: 'Simple average gives 64 only if BOTH isotopes are 50/50 abundant. Since there '
                                      'is more of the lighter isotope (60% at mass 63), the weighted average is pulled '
                                      'below 64.',
                                   2: 'Adding mass numbers has no physical meaning — Ar is a weighted average, not a '
                                      'sum.',
                                   3: 'Using only the most abundant isotope ignores the 40% contribution from mass 65 '
                                      '— the true Ar is pulled above 63 by the heavier isotope.'}}],
  'rp': None,
  'spec': '5.1.1.6',
  'summary': 'Define atomic number, mass number, isotopes and relative atomic mass — and calculate Ar from isotope '
             'abundances.',
  'theory': [{'content': 'Every element is defined by its ATOMIC NUMBER (proton number):\n'
                         '\n'
                         'ATOMIC NUMBER (Z) = number of PROTONS in the nucleus.\n'
                         'This is unique to each element — all carbon atoms have 6 protons, all iron atoms have 26.\n'
                         'In a neutral atom: protons = electrons.\n'
                         '\n'
                         'MASS NUMBER (A) = total number of PROTONS + NEUTRONS in the nucleus.\n'
                         '\n'
                         'From these two numbers:\n'
                         'Neutrons = mass number − atomic number\n'
                         '\n'
                         'Example — sodium-23:\n'
                         'Mass number = 23, atomic number = 11.\n'
                         'Protons = 11, electrons = 11 (neutral), neutrons = 23 − 11 = 12.\n'
                         '\n'
                         'In the periodic table, the ATOMIC NUMBER is the SMALLER number (it cannot exceed the mass '
                         'number as you cannot have negative neutrons).',
              'heading': 'Atomic Number and Mass Number'},
             {'content': 'ISOTOPES are atoms of the SAME ELEMENT with the SAME ATOMIC NUMBER but DIFFERENT MASS '
                         'NUMBERS.\n'
                         '\n'
                         'Same protons → same element → same chemical properties.\n'
                         'Different neutrons → different mass → different physical properties (e.g. density, rate of '
                         'diffusion).\n'
                         '\n'
                         'Isotopes have IDENTICAL CHEMICAL behaviour — because chemical reactions depend on electron '
                         'configuration (determined by proton number, which is the same).\n'
                         '\n'
                         'Examples:\n'
                         'CARBON ISOTOPES:\n'
                         'Carbon-12 (¹²C): 6p + 6n — the standard (98.9% of carbon)\n'
                         'Carbon-13 (¹³C): 6p + 7n — stable, ~1.1%\n'
                         'Carbon-14 (¹⁴C): 6p + 8n — radioactive, used in carbon dating\n'
                         '\n'
                         'CHLORINE ISOTOPES:\n'
                         'Chlorine-35 (³⁵Cl): 17p + 18n — ~75% of chlorine\n'
                         'Chlorine-37 (³⁷Cl): 17p + 20n — ~25% of chlorine\n'
                         'Because of this mixture, the Ar of chlorine ≈ 35.5 — between the two isotope masses.',
              'heading': 'Isotopes'},
             {'content': 'The RELATIVE ATOMIC MASS (Ar) is the WEIGHTED AVERAGE mass of all atoms of an element '
                         'compared to 1/12 of the mass of a carbon-12 atom.\n'
                         '\n'
                         'Because most elements have multiple isotopes in different abundances, Ar is NOT a whole '
                         'number.\n'
                         '\n'
                         'Formula:\n'
                         'Ar = Σ (% abundance × mass number) ÷ 100\n'
                         '\n'
                         'Example — chlorine:\n'
                         'Ar = (75 × 35 + 25 × 37) ÷ 100\n'
                         'Ar = (2625 + 925) ÷ 100\n'
                         'Ar = 3550 ÷ 100 = 35.5\n'
                         '\n'
                         'This explains why periodic table Ar values are often not whole numbers — they are weighted '
                         'averages across all naturally occurring isotopes.',
              'heading': 'Relative Atomic Mass'}],
  'title': 'Relative Atomic Mass, Atomic Number and Isotopes',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Always fill shells in ORDER — 2 in the first, then 8 in the second, then continue. The 3rd shell '
                    'fills to 8 before the 4th shell starts. Students sometimes try to put more than 8 in the 3rd '
                    'shell for early elements — for the first 20, the 3rd shell only goes up to 8.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'electronic-structure',
  'key_note': 'Shells fill innermost first: 2, 8, 8. Electronic configuration written as numbers separated by dots '
              '(e.g. 2.8.3 for Al). Same group = same outer electrons = similar chemistry. Full outer shell = stable '
              '(noble gas configuration).',
  'matching': {'instruction': 'Match each element to its correct electronic configuration.',
               'pairs': [('Sodium (Na, 11)', '2.8.1 — 11 electrons: 2 in shell 1, 8 in shell 2, 1 in shell 3'),
                         ('Chlorine (Cl, 17)', '2.8.7 — 17 electrons: 2 in shell 1, 8 in shell 2, 7 in shell 3'),
                         ('Calcium (Ca, 20)', '2.8.8.2 — 20 electrons across four shells'),
                         ('Neon (Ne, 10)', '2.8 — full outer shell, noble gas, very unreactive'),
                         ('Magnesium (Mg, 12)', '2.8.2 — 2 outer electrons, Group 2 element')],
               'title': 'Match the Element to its Electronic Configuration'},
  'quiz': [{'opts': [('Group 6 — it has 6 electrons in its outermost shell', True),
                     ('Group 2 — there are 2 complete shells below the outer shell', False),
                     ('Group 16 — add all the electrons together', False),
                     ('Period 3 — it has 3 shells', False)],
            'q': 'An element has the electronic configuration 2.8.6. Which group of the periodic table is it in?',
            'wrong_explanations': {1: 'The number of complete inner shells tells you the PERIOD — 2 inner shells means '
                                      'Period 3. Groups are determined by OUTER electrons.',
                                   2: '16 is the total number of electrons (2+8+6) — this tells you the atomic number, '
                                      'not the group.',
                                   3: 'The NUMBER OF SHELLS tells you the PERIOD (3 shells = Period 3). The GROUP is '
                                      'determined by the number of OUTER electrons (6).'}},
           {'opts': [('Both have 1 electron in their outer shell — they react in similar ways to achieve a full outer '
                      'shell',
                      True),
                     ('Both have the same total number of electrons', False),
                     ('Both are in the same period of the periodic table', False),
                     ('Both have the same mass number', False)],
            'q': 'Why do lithium (2.1) and sodium (2.8.1) have similar chemical properties?',
            'wrong_explanations': {1: 'Li has 3 electrons total, Na has 11 — very different totals, but the same outer '
                                      'shell count (1) is what matters for reactivity.',
                                   2: 'Li is Period 2, Na is Period 3 — they are in different periods. Same GROUP, '
                                      'different periods.',
                                   3: 'Li has mass number 7, Na has mass number 23 — different mass numbers. Chemical '
                                      'similarity comes from electron configuration.'}}],
  'rp': None,
  'spec': '5.1.1.7',
  'summary': 'Describe how electrons fill shells and write electronic configurations for the first 20 elements.',
  'theory': [{'content': 'Electrons occupy SHELLS (energy levels) around the nucleus. They always fill from the '
                         'INNERMOST (lowest energy) shell outward.\n'
                         '\n'
                         'SHELL CAPACITIES (for first 20 elements):\n'
                         '1st shell: maximum 2 electrons.\n'
                         '2nd shell: maximum 8 electrons.\n'
                         '3rd shell: maximum 8 electrons.\n'
                         '\n'
                         'Electrons are only added to the next shell when the current one is FULL.\n'
                         '\n'
                         'Example — Sodium (Na, atomic number 11):\n'
                         '11 electrons to distribute.\n'
                         '1st shell: 2 (full) → 2nd shell: 8 (full) → 3rd shell: 1 remaining.\n'
                         'Electronic configuration written as: 2.8.1',
              'heading': 'Electron Shells'},
             {'content': 'H  (1):  1\n'
                         'He (2):  2\n'
                         'Li (3):  2.1\n'
                         'Be (4):  2.2\n'
                         'B  (5):  2.3\n'
                         'C  (6):  2.4\n'
                         'N  (7):  2.5\n'
                         'O  (8):  2.6\n'
                         'F  (9):  2.7\n'
                         'Ne (10): 2.8\n'
                         'Na (11): 2.8.1\n'
                         'Mg (12): 2.8.2\n'
                         'Al (13): 2.8.3\n'
                         'Si (14): 2.8.4\n'
                         'P  (15): 2.8.5\n'
                         'S  (16): 2.8.6\n'
                         'Cl (17): 2.8.7\n'
                         'Ar (18): 2.8.8\n'
                         'K  (19): 2.8.8.1\n'
                         'Ca (20): 2.8.8.2\n'
                         '\n'
                         'Note: the 4th shell starts filling at potassium (K) and calcium (Ca) because the 3rd shell '
                         'fills to 8 before the 4th begins (for these lighter elements).',
              'heading': 'Electronic Configurations of the First 20 Elements'},
             {'content': "The NUMBER OF ELECTRONS IN THE OUTERMOST SHELL (valence electrons) determines an element's "
                         'chemical properties.\n'
                         '\n'
                         'Elements in the SAME GROUP of the periodic table have the SAME NUMBER of outer electrons:\n'
                         'Group 1: 1 outer electron (Li: 2.1, Na: 2.8.1, K: 2.8.8.1)\n'
                         'Group 7: 7 outer electrons (F: 2.7, Cl: 2.8.7)\n'
                         'Group 0: 8 outer electrons (full shell) — He: 2, Ne: 2.8, Ar: 2.8.8\n'
                         '\n'
                         'This is why elements in the same group have similar chemical properties — they react in '
                         'similar ways to achieve a full outer shell.\n'
                         '\n'
                         'ATOMS REACT TO ACHIEVE A FULL OUTER SHELL:\n'
                         'METALS lose electrons → form positive ions (cations).\n'
                         'NON-METALS gain electrons (or share) → form negative ions (anions) or covalent bonds.\n'
                         'NOBLE GASES already have full outer shells → very unreactive.',
              'heading': 'Electronic Structure and Chemical Properties'}],
  'title': 'Electronic Structure',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The GROUP NUMBER tells you the number of OUTER ELECTRONS — not the total electrons or the period. '
                    'The PERIOD NUMBER tells you how many shells. So an element in Period 3, Group 2 has 3 shells and '
                    "2 outer electrons — electronic configuration 2.8.2 (magnesium). Don't confuse groups and periods.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'periodic-table',
  'key_note': 'Periodic table arranged by atomic number. Period = row = number of shells. Group = column = number of '
              'outer electrons. Same group = same outer electrons = similar properties. Metals: left and centre. '
              'Non-metals: top right. Noble gases: Group 0 (right edge).',
  'matching': {'instruction': 'Match each feature to its correct description.',
               'pairs': [('Period', 'A horizontal row — each new period means another electron shell'),
                         ('Group', 'A vertical column — elements share the same number of outer electrons'),
                         ('Group 0', 'Noble gases — full outer shells, very unreactive'),
                         ('Transition metals',
                          'Hard, dense metals with high melting points — form coloured compounds, act as catalysts'),
                         ('Group 1', 'Alkali metals — 1 outer electron, very reactive, soft, low density')],
               'title': 'Match the Periodic Table Feature'},
  'quiz': [{'opts': [('2.8.2 — 3 shells (Period 3) and 2 outer electrons (Group 2)', True),
                     ('3.2 — period number first, then group number', False),
                     ('2.2 — two shells and two outer electrons', False),
                     ('2.8.3 — Period 3 means 3 electrons in the outer shell', False)],
            'q': 'An element is in Period 3 and Group 2. What is its electronic configuration?',
            'wrong_explanations': {1: "The periodic table doesn't give configurations directly — the group number is "
                                      'the outer electrons, but you must fill the inner shells first.',
                                   2: 'Period 3 means 3 SHELLS, not 3 electrons in the outer shell. The shells fill as '
                                      '2.8.2 — inner shells full, outer shell has 2.',
                                   3: 'Period 3 means 3 SHELLS — not 3 electrons in the outermost shell. The Group '
                                      'number (2) gives the outer electron count.'}},
           {'opts': [('They all have 7 electrons in their outer shell — they react similarly by gaining one electron '
                      'to achieve a full shell',
                      True),
                     ('They are all gases at room temperature', False),
                     ('They all have the same number of electrons', False),
                     ('They are all in the same period of the periodic table', False)],
            'q': 'Why do all Group 7 elements have similar chemical properties?',
            'wrong_explanations': {1: 'Fluorine is a gas but iodine is a solid at room temperature — physical state '
                                      'varies within Group 7.',
                                   2: 'Different Group 7 elements have different numbers of electrons (F:9, Cl:17, '
                                      "Br:35) — the OUTER electron count (7) is what's the same.",
                                   3: 'Elements in the same group are in DIFFERENT periods — they share the same outer '
                                      'electron count, not the same period.'}}],
  'rp': None,
  'spec': '5.1.2.1',
  'summary': 'Describe the structure of the periodic table and explain how it is organised.',
  'theory': [{'content': 'The PERIODIC TABLE arranges all known elements in order of increasing ATOMIC NUMBER.\n'
                         '\n'
                         'Key features:\n'
                         'ROWS are called PERIODS — each period represents a new electron shell being filled.\n'
                         'COLUMNS are called GROUPS — elements in the same group have the same number of OUTER '
                         'ELECTRONS and similar chemical properties.\n'
                         '\n'
                         'Period numbers tell you how many electron shells the element has:\n'
                         'Period 1: 1 shell (H and He)\n'
                         'Period 2: 2 shells (Li to Ne)\n'
                         'Period 3: 3 shells (Na to Ar)\n'
                         '\n'
                         'Group numbers (1–7 and 0) tell you how many OUTER electrons:\n'
                         'Group 1: 1 outer electron\n'
                         'Group 7: 7 outer electrons\n'
                         'Group 0: full outer shell (8 electrons, or 2 for helium)\n'
                         '\n'
                         'The periodic table is divided into:\n'
                         'METALS — left and centre (most elements are metals).\n'
                         'NON-METALS — top right.\n'
                         'METALLOIDS/SEMI-METALS — along the dividing line (e.g. silicon, germanium).',
              'heading': 'Structure of the Periodic Table'},
             {'content': 'ACROSS A PERIOD (left to right):\n'
                         'Atomic number increases.\n'
                         'Number of electrons in outer shell increases (1 to 8).\n'
                         'Metallic properties decrease — non-metallic properties increase.\n'
                         'From metal (Group 1) to non-metal (Group 7) to noble gas (Group 0).\n'
                         '\n'
                         'DOWN A GROUP:\n'
                         'Another electron shell is added.\n'
                         'Atoms get LARGER (more shells = bigger atom).\n'
                         'OUTER ELECTRONS are further from the nucleus — less strongly attracted.\n'
                         'METALS become MORE REACTIVE going down (easier to lose outer electron).\n'
                         'NON-METALS become LESS REACTIVE going down (harder to gain another electron — outer '
                         'electrons are further away).\n'
                         '\n'
                         'These trends allow chemists to PREDICT the properties of elements from their position in the '
                         'periodic table.',
              'heading': 'Trends Across Periods and Down Groups'},
             {'content': 'Between Groups 2 and 3 lies the TRANSITION METALS block (the long middle section).\n'
                         '\n'
                         'Transition metals are harder and have higher melting points than Group 1 metals.\n'
                         'They are typically dense, strong, shiny metals.\n'
                         'Examples: iron (Fe), copper (Cu), zinc (Zn), titanium (Ti), nickel (Ni), gold (Au), silver '
                         '(Ag).\n'
                         '\n'
                         'Key properties of transition metals:\n'
                         'Form COLOURED COMPOUNDS — e.g. copper sulfate is blue; iron(II) compounds are pale green; '
                         'iron(III) compounds are orange.\n'
                         'Can act as CATALYSTS — e.g. iron catalyst in the Haber process; nickel in hydrogenation.\n'
                         'Can have MULTIPLE OXIDATION STATES — e.g. iron can be Fe²⁺ or Fe³⁺.\n'
                         '\n'
                         'Compare with Group 1 metals: transition metals are less reactive, harder, have higher '
                         'melting points and form coloured compounds. Group 1 metals are soft, very reactive and their '
                         'compounds are usually white.',
              'heading': 'Transition Metals'}],
  'title': 'The Periodic Table',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Mendeleev arranged elements by RELATIVE ATOMIC MASS — the MODERN table is arranged by ATOMIC '
                    "NUMBER. Mendeleev's arrangement had a few inconsistencies because Ar and atomic number don't "
                    'always match perfectly (e.g. argon and potassium). The modern arrangement by atomic number '
                    'resolves all these problems.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'development-periodic-table',
  'key_note': "Newlands: octaves — every 8th element similar — rejected (didn't work for all elements, no gaps). "
              'Mendeleev: arranged by Ar, left gaps, predicted missing elements — accepted when predictions proved '
              'correct. Modern table: arranged by atomic number (Moseley, 1913).',
  'matching': {'instruction': 'Match each scientist to their contribution to the periodic table.',
               'pairs': [('Newlands',
                          'Law of Octaves — every 8th element similar — not accepted by scientists at the time'),
                         ('Mendeleev',
                          'Left gaps for undiscovered elements, predicted their properties — table accepted when '
                          'predictions proved correct'),
                         ('Moseley',
                          "Arranged elements by atomic number (protons) — resolved inconsistencies in Mendeleev's "
                          'Ar-based table')],
               'title': 'Match the Scientist to their Contribution'},
  'quiz': [{'opts': [('It only worked for the first 16 elements and forced elements into groups regardless of whether '
                      'properties matched',
                      True),
                     ('Newlands arranged elements by atomic number rather than relative atomic mass', False),
                     ("The law of octaves was never published so other scientists couldn't evaluate it", False),
                     ('Newlands did not leave gaps for undiscovered elements — but neither did he need to', False)],
            'q': "Why did the scientific community initially reject Newlands' Law of Octaves?",
            'wrong_explanations': {1: 'Newlands arranged by RELATIVE ATOMIC MASS — atomic numbers were not yet known.',
                                   2: 'Newlands did publish his work — it was presented to the Chemical Society in '
                                      '1866.',
                                   3: 'Not leaving gaps was a problem for Mendeleev too initially — but the bigger '
                                      'issue for Newlands was that his pattern broke down after the first 16 '
                                      'elements.'}},
           {'opts': [('He predicted properties of undiscovered elements — and when they were found, the predictions '
                      'were accurate',
                      True),
                     ('He was the first to arrange elements in order of atomic mass', False),
                     ('He discovered all the noble gases and added them to the table', False),
                     ('His table was the simplest and easiest to remember', False)],
            'q': "What was the key reason Mendeleev's periodic table was eventually accepted by scientists?",
            'wrong_explanations': {1: "Newlands had also arranged by atomic mass — Mendeleev's key advance was leaving "
                                      'gaps and making testable predictions.',
                                   2: 'Noble gases were discovered by other scientists (Ramsay and others) after '
                                      "Mendeleev's original table — they were later added as Group 0.",
                                   3: 'Science accepts models based on EVIDENCE and PREDICTIVE POWER, not simplicity '
                                      'alone.'}}],
  'rp': None,
  'spec': '5.1.2.2',
  'summary': "Describe how the periodic table developed, including Newlands and Mendeleev's contributions.",
  'theory': [{'content': 'Before atomic numbers were understood, scientists tried to classify elements based on '
                         'RELATIVE ATOMIC MASS.\n'
                         '\n'
                         'JOHN NEWLANDS — Law of Octaves (1864):\n'
                         'Arranged elements by increasing Ar.\n'
                         "Noticed that every 8th element had similar properties — called it the 'Law of Octaves' (like "
                         'musical notes).\n'
                         'Limitations:\n'
                         'Only worked for the first 16 elements.\n'
                         "Forced elements into groups even when properties didn't match.\n"
                         'Left no gaps for undiscovered elements.\n'
                         'The scientific community did not accept his work.\n'
                         '\n'
                         'DMITRI MENDELEEV — first successful periodic table (1869):\n'
                         'Also arranged elements by increasing Ar.\n'
                         'Key improvements over Newlands:\n'
                         'Left GAPS for undiscovered elements — predicted their properties.\n'
                         'Rearranged some elements to make groups match better (putting chemical properties above '
                         'strict Ar order).\n'
                         'Predicted EKA-SILICON (now known as germanium) — when it was discovered in 1886, its '
                         "properties closely matched Mendeleev's prediction.\n"
                         'This predictive power convinced the scientific community to accept the table.',
              'heading': 'Early Attempts at Classification'},
             {'content': 'The modern periodic table was only possible after the discovery of subatomic particles.\n'
                         '\n'
                         'HENRY MOSELEY (1913):\n'
                         'Used X-ray experiments to determine ATOMIC NUMBERS of elements.\n'
                         'Realised elements should be arranged by ATOMIC NUMBER (protons), not atomic mass.\n'
                         "This resolved several inconsistencies in Mendeleev's table where some elements seemed in the "
                         'wrong order when arranged by Ar.\n'
                         '\n'
                         'Key improvement: arranging by atomic number places elements in the correct groups without '
                         'exception — it is the atomic number (protons = electrons) that determines chemical '
                         'properties, not mass.\n'
                         '\n'
                         'DISCOVERY OF NOBLE GASES:\n'
                         "Argon (1894) and other noble gases were discovered AFTER Mendeleev's table — but they fit "
                         'perfectly as a new Group 0.\n'
                         'This was further evidence for the validity of the periodic table structure.',
              'heading': 'The Modern Periodic Table'},
             {'content': "Mendeleev's table was eventually accepted by the scientific community for three main "
                         'reasons:\n'
                         '\n'
                         '1. PREDICTIVE POWER: He predicted properties of undiscovered elements (eka-aluminium = '
                         'gallium, eka-silicon = germanium, eka-boron = scandium). When discovered, they matched his '
                         'predictions closely.\n'
                         '\n'
                         '2. GAPS: Leaving gaps was a bold scientific decision — it showed the table was a genuine '
                         'model of underlying patterns, not just a classification of known elements.\n'
                         '\n'
                         '3. EXPLAINING PATTERNS: The table explained why elements in the same group reacted similarly '
                         '— it made chemistry more systematic and predictable.\n'
                         '\n'
                         "Science accepts models when they successfully PREDICT new observations — Mendeleev's table "
                         'did exactly this.',
              'heading': "Why Mendeleev's Table was Accepted"}],
  'title': 'Development of the Periodic Table',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Graphite and graphene are non-metals that conduct electricity — they are exceptions. Most '
                    "non-metals do not conduct, but graphite has delocalised electrons between its layers. Don't say "
                    "'all non-metals don't conduct' — say 'non-metals generally don't conduct, except graphite and "
                    "graphene'.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'metals-non-metals',
  'key_note': 'Metals: good conductors, high melting points, malleable, ductile, form positive ions, basic oxides. '
              'Non-metals: poor conductors (except graphite), low melting points, brittle, form negative ions, acidic '
              'oxides. Metallic character decreases across a period and increases down a group.',
  'matching': {'instruction': 'Sort each property into metals or non-metals.',
               'pairs': [('Metal', 'Good conductor of electricity — delocalised electrons carry charge'),
                         ('Non-metal', 'Poor conductor of electricity — no free electrons (except graphite)'),
                         ('Metal', 'Malleable — can be hammered into sheets without shattering'),
                         ('Non-metal', 'Brittle solid — shatters when struck'),
                         ('Metal', 'Forms positive ions by losing electrons in reactions'),
                         ('Non-metal', 'Forms acidic oxides — e.g. CO₂ dissolves in water to form carbonic acid')],
               'title': 'Metal or Non-metal Property?'},
  'quiz': [{'opts': [('Metals have delocalised (free) electrons that can move through the structure and carry charge',
                      True),
                     ('Metal atoms are larger, so electrons move more easily', False),
                     ('Metals have more protons than non-metals, creating stronger positive charge', False),
                     ('Metal compounds dissolve in water to release ions that carry charge', False)],
            'q': 'Why are metals good conductors of electricity?',
            'wrong_explanations': {1: 'Atomic size does not determine conductivity — it is the presence of FREE '
                                      'electrons, not large atoms, that allows charge to flow.',
                                   2: 'Proton count determines the element, not conductivity. Non-metals also have '
                                      'many protons but are poor conductors.',
                                   3: 'Solid metals conduct electricity — not dissolved ions. Ionic conductivity in '
                                      'solution is different from metallic conductivity in a solid.'}},
           {'opts': [('Non-metal — non-metal oxides form acidic solutions when dissolved in water', True),
                     ('Metal — metal oxides are always basic', False),
                     ('Metalloid — SO₂ is both acidic and basic', False),
                     ("It could be either — the acidity of its oxide doesn't indicate the type of element", False)],
            'q': 'Sulfur dioxide (SO₂) dissolves in water to form an acidic solution. Is sulfur a metal or non-metal?',
            'wrong_explanations': {1: 'Metal oxides are BASIC — they neutralise acids. SO₂ forms an acidic solution, '
                                      'which is the behaviour of NON-METAL oxides.',
                                   2: 'SO₂ is not amphoteric (both acidic and basic) — it is distinctly acidic. Sulfur '
                                      'is clearly a non-metal.',
                                   3: 'The type of oxide (acidic or basic) is a reliable indicator of whether the '
                                      'element is a metal or non-metal.'}}],
  'rp': None,
  'spec': '5.1.2.3',
  'summary': 'Compare the properties of metals and non-metals and explain them in terms of structure and bonding.',
  'theory': [{'content': 'Most elements are METALS — they are found on the left and in the centre of the periodic '
                         'table.\n'
                         '\n'
                         'Typical physical properties of metals:\n'
                         'GOOD CONDUCTORS of electricity and heat — delocalised electrons carry charge and energy.\n'
                         'HIGH MELTING AND BOILING POINTS — strong metallic bonds.\n'
                         'SHINY (lustrous) appearance when cut or polished.\n'
                         'MALLEABLE — can be hammered into sheets without breaking.\n'
                         'DUCTILE — can be drawn into wires.\n'
                         'SOLID at room temperature — except mercury (Hg), which is a liquid.\n'
                         'HIGH DENSITY in most cases.\n'
                         '\n'
                         'Chemical properties of metals:\n'
                         'FORM POSITIVE IONS — lose outer electrons in reactions.\n'
                         'REACT with oxygen to form METAL OXIDES (these are BASIC — they neutralise acids).\n'
                         'Many react with water and acids to produce hydrogen gas.',
              'heading': 'Properties of Metals'},
             {'content': 'NON-METALS are found on the right side of the periodic table.\n'
                         '\n'
                         'Typical physical properties of non-metals:\n'
                         'POOR CONDUCTORS of electricity (except graphite and graphene).\n'
                         'LOW MELTING AND BOILING POINTS — weak forces between molecules.\n'
                         'BRITTLE when solid — cannot be bent or drawn into wires.\n'
                         'Low density generally.\n'
                         'Many are GASES at room temperature (O₂, N₂, Cl₂, H₂, etc.).\n'
                         'Some are SOLIDS (carbon, sulfur, phosphorus, iodine).\n'
                         'Bromine (Br₂) is a liquid at room temperature.\n'
                         '\n'
                         'Chemical properties of non-metals:\n'
                         'FORM NEGATIVE IONS — gain electrons (or share in covalent bonds).\n'
                         'REACT with oxygen to form NON-METAL OXIDES (these are ACIDIC — they dissolve in water to '
                         'form acids).',
              'heading': 'Properties of Non-metals'},
             {'content': 'A useful comparison table:\n'
                         '\n'
                         'Electrical conductivity:\n'
                         'METAL: Good conductor (delocalised electrons).\n'
                         'NON-METAL: Poor conductor (no free electrons) — EXCEPT graphite.\n'
                         '\n'
                         'Melting/boiling point:\n'
                         'METAL: Generally high — strong metallic bonds.\n'
                         'NON-METAL: Generally low — weak intermolecular forces.\n'
                         '\n'
                         'Malleability/ductility:\n'
                         'METAL: Malleable and ductile.\n'
                         'NON-METAL: Brittle.\n'
                         '\n'
                         'Ion formation:\n'
                         'METAL: Forms POSITIVE ions (loses electrons).\n'
                         'NON-METAL: Forms NEGATIVE ions (gains electrons).\n'
                         '\n'
                         'Oxide type:\n'
                         'METAL: Basic oxides (e.g. MgO, Fe₂O₃).\n'
                         'NON-METAL: Acidic oxides (e.g. CO₂, SO₂, NO₂).\n'
                         '\n'
                         'Some elements (like silicon) are METALLOIDS — they have properties between metals and '
                         'non-metals. Silicon conducts electricity but is brittle — it is a semiconductor, used in '
                         'electronics.',
              'heading': 'Key Differences — Metals vs Non-metals'}],
  'title': 'Metals and Non-metals',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Noble gases are MONATOMIC — they exist as single atoms (He, Ne, Ar) — NOT as molecules (not He₂ '
                    'or Ne₂). This is because they are already stable with full outer shells and have no reason to '
                    'form bonds. Other non-metals like oxygen (O₂) and nitrogen (N₂) exist as diatomic molecules '
                    'because they share electrons to achieve full outer shells.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'group-0',
  'key_note': 'Noble gases: Group 0, full outer shells, extremely unreactive, monatomic. Boiling point increases down '
              'group (bigger atoms, stronger London dispersion forces). Helium: 2 outer electrons (full 1st shell). '
              'All others: 8 outer electrons (full outer shell).',
  'matching': {'instruction': 'Match each property to noble gases and explain why.',
               'pairs': [('Very unreactive',
                          'Full outer electron shells — no tendency to gain, lose or share electrons'),
                         ('Monatomic', 'Exist as single atoms — already stable, no need to bond with other atoms'),
                         ('Boiling point increases down group',
                          'Larger atoms have stronger London dispersion forces — more electrons, larger temporary '
                          'dipoles'),
                         ('Colourless gases', 'All noble gases are transparent and gaseous at room temperature'),
                         ('Helium — lighter than air',
                          'Helium has only 2 electrons and 2 protons — very low density, used in balloons')],
               'title': 'Match the Noble Gas Property'},
  'quiz': [{'opts': [('They have full outer electron shells — no tendency to gain, lose or share electrons to become '
                      'more stable',
                      True),
                     ('They are gases — gases cannot react with solid or liquid substances', False),
                     ('They have no electrons in their outer shell — so they cannot form bonds', False),
                     ('They are too small to collide effectively with other atoms', False)],
            'q': 'Why are noble gases so unreactive?',
            'wrong_explanations': {1: 'Many gases are highly reactive — chlorine gas (Cl₂), oxygen gas (O₂) etc. Being '
                                      "a gas doesn't make something unreactive.",
                                   2: 'Noble gases have FULL outer shells, not empty ones. Helium has 2 electrons '
                                      '(full 1st shell), others have 8 outer electrons.',
                                   3: 'Atomic size affects reactivity in some cases, but noble gases are unreactive '
                                      'because of electron configuration, not size.'}},
           {'opts': [('Argon is a larger atom with more electrons — stronger London dispersion forces between atoms '
                      'need more energy to overcome',
                      True),
                     ('Argon has a higher atomic number, so its electrons are more strongly attracted to the nucleus',
                      False),
                     ('Argon forms molecules (Ar₂) while neon is monatomic — more bonds to break', False),
                     ('Argon is radioactive, releasing energy that raises its boiling point', False)],
            'q': 'Argon has a higher boiling point than neon. Why?',
            'wrong_explanations': {1: "Stronger nuclear attraction would make electrons harder to remove but doesn't "
                                      'directly raise boiling point — the intermolecular forces between atoms are what '
                                      'matter.',
                                   2: 'Noble gases are ALL monatomic — they never form Ar₂ or Ne₂ molecules under '
                                      'normal conditions.',
                                   3: 'Argon is stable and not radioactive. Radon is the radioactive noble gas.'}}],
  'rp': None,
  'spec': '5.1.2.4',
  'summary': 'Describe the properties of noble gases and explain why they are so unreactive.',
  'theory': [{'content': 'GROUP 0 (also called Group 18) contains the NOBLE GASES:\n'
                         'Helium (He) — atomic number 2.\n'
                         'Neon (Ne) — atomic number 10.\n'
                         'Argon (Ar) — atomic number 18.\n'
                         'Krypton (Kr) — atomic number 36.\n'
                         'Xenon (Xe) — atomic number 54.\n'
                         'Radon (Rn) — atomic number 86.\n'
                         '\n'
                         'All noble gases are:\n'
                         'COLOURLESS gases at room temperature.\n'
                         'MONATOMIC — they exist as single atoms, not molecules (unlike O₂, N₂, Cl₂).\n'
                         'EXTREMELY UNREACTIVE — they do not form compounds under normal conditions.\n'
                         'DENSER than air as you go down the group.\n'
                         'Have very LOW BOILING POINTS — they remain gases until very cold.',
              'heading': 'Properties of the Noble Gases'},
             {'content': 'Noble gases are unreactive because they have FULL OUTER ELECTRON SHELLS:\n'
                         'Helium: 2 electrons (full 1st shell).\n'
                         'Neon: 2.8 (full 1st and 2nd shells).\n'
                         'Argon: 2.8.8 (full 1st, 2nd and 3rd shells).\n'
                         '\n'
                         'A full outer shell is the most STABLE electron configuration — the atom has no tendency to '
                         'gain, lose or share electrons.\n'
                         '\n'
                         'This is why other elements react — they are trying to ACHIEVE the stable full outer shell '
                         'configuration of a noble gas:\n'
                         'Group 1 metals lose 1 electron → achieve noble gas configuration.\n'
                         'Group 7 non-metals gain 1 electron → achieve noble gas configuration.\n'
                         'Non-metals share electrons (covalent bonds) to achieve full outer shells.',
              'heading': 'Why Noble Gases Are Unreactive'},
             {'content': 'Going DOWN Group 0 (from He to Rn):\n'
                         '\n'
                         'ATOMIC RADIUS increases — more electron shells are added.\n'
                         '\n'
                         'BOILING POINT INCREASES:\n'
                         'He: −269°C, Ne: −246°C, Ar: −186°C, Kr: −153°C, Xe: −108°C.\n'
                         'Larger atoms have stronger LONDON DISPERSION FORCES between them (a type of intermolecular '
                         'force caused by temporary dipoles in electron clouds).\n'
                         'More electrons → greater temporary dipoles → stronger forces → higher boiling point.\n'
                         '\n'
                         'DENSITY increases down the group.\n'
                         '\n'
                         'The reactivity stays VERY LOW throughout — all noble gases are essentially inert under '
                         'normal conditions.',
              'heading': 'Trends Down Group 0'}],
  'title': 'Group 0 — Noble Gases',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Reactivity INCREASES down Group 1 (opposite to Group 7). This is because the outer electron gets '
                    'further from the nucleus and is more easily lost. Going down Group 1: more shells → outer '
                    'electron further away → weaker attraction → MORE reactive. Going down Group 7: non-metals get '
                    'LESS reactive (harder to attract an extra electron).',
  'equations': ['2M + 2H₂O → 2MOH + H₂', '2Li + 2H₂O → 2LiOH + H₂', '2Na + 2H₂O → 2NaOH + H₂', '2K + 2H₂O → 2KOH + H₂'],
  'fifas': [],
  'higher': None,
  'id': 'group-1',
  'key_note': 'Group 1: alkali metals, 1 outer electron, form +1 ions. Soft, low density, low melting point. React '
              'with water → metal hydroxide + hydrogen. Reactivity INCREASES down group (outer electron further from '
              'nucleus, less attracted, more easily lost).',
  'matching': {'instruction': 'Match each alkali metal to its reaction description with water.',
               'pairs': [('Lithium', 'Fizzes gently, moves around on water surface — less vigorous than others'),
                         ('Sodium', 'Fizzes vigorously, moves rapidly, may ignite — more reactive than lithium'),
                         ('Potassium',
                          'Reacts very vigorously, hydrogen ignites immediately with a lilac/purple flame'),
                         ('All Group 1 metals',
                          'React with water to produce a metal hydroxide (alkali) and hydrogen gas'),
                         ('Reactivity trend',
                          'Increases down Group 1 — outer electron is further from nucleus, less strongly attracted')],
               'title': 'Match the Group 1 Reaction'},
  'quiz': [{'opts': [('Sodium hydroxide (NaOH) and hydrogen gas (H₂)', True),
                     ('Sodium oxide (Na₂O) and water', False),
                     ('Sodium chloride (NaCl) and hydrogen', False),
                     ('Sodium hydroxide and oxygen gas', False)],
            'q': 'What are the products when sodium reacts with water?',
            'wrong_explanations': {1: 'Sodium reacts with oxygen to form sodium OXIDE — but when it reacts with water '
                                      'specifically, the products are hydroxide and hydrogen.',
                                   2: 'NaCl is the product of sodium reacting with CHLORINE or hydrochloric acid — not '
                                      'water.',
                                   3: 'Oxygen is not released when metals react with water. The equation is: 2Na + '
                                      '2H₂O → 2NaOH + H₂.'}},
           {'opts': [('Potassium has more electron shells — its outer electron is further from the nucleus and more '
                      'easily lost',
                      True),
                     ('Potassium has more protons — so it has a stronger positive charge making it more reactive',
                      False),
                     ('Potassium is a larger atom so it reacts with a larger surface area', False),
                     ("Potassium's outer electron has a higher charge than lithium's outer electron", False)],
            'q': 'Why is potassium more reactive than lithium?',
            'wrong_explanations': {1: 'More protons means stronger nuclear charge — this would actually make it HARDER '
                                      'to lose the electron, not easier. But the extra shells and increased distance '
                                      'outweigh the effect of more protons.',
                                   2: 'Surface area affects reaction rate but not inherent reactivity — the question '
                                      'is about why K is more reactive than Li in terms of properties.',
                                   3: "All electrons have the same charge (−1 each) — the 'ease of losing' them "
                                      'depends on how strongly they are attracted to the nucleus.'}}],
  'rp': None,
  'spec': '5.1.2.5',
  'summary': 'Describe the properties of Group 1 metals and explain trends in reactivity down the group.',
  'theory': [{'content': 'GROUP 1 contains the ALKALI METALS:\n'
                         'Lithium (Li) — atomic number 3.\n'
                         'Sodium (Na) — atomic number 11.\n'
                         'Potassium (K) — atomic number 19.\n'
                         'Rubidium (Rb), Caesium (Cs), Francium (Fr) — increasingly reactive and rare.\n'
                         '\n'
                         'All Group 1 metals share these properties:\n'
                         '1 OUTER ELECTRON — they lose this electron easily to form +1 ions.\n'
                         'SOFT — can be cut with a knife.\n'
                         'LOW DENSITY — lithium, sodium and potassium all float on water.\n'
                         'LOW MELTING AND BOILING POINTS compared to other metals.\n'
                         'Shiny when freshly cut — but quickly tarnish in air (react with oxygen).\n'
                         'Stored under OIL to prevent reaction with air and water.\n'
                         'React vigorously with WATER to produce hydrogen gas and metal hydroxide (an alkali — hence '
                         "'alkali metals').",
              'heading': 'Properties of the Alkali Metals'},
             {'content': 'All Group 1 metals react with water to produce a METAL HYDROXIDE and HYDROGEN GAS:\n'
                         '\n'
                         'General equation:\n'
                         'Metal + water → metal hydroxide + hydrogen\n'
                         '2M + 2H₂O → 2MOH + H₂\n'
                         '\n'
                         'Specific reactions:\n'
                         '2Li + 2H₂O → 2LiOH + H₂\n'
                         '(Lithium: fizzes gently, moves around on the surface)\n'
                         '\n'
                         '2Na + 2H₂O → 2NaOH + H₂\n'
                         '(Sodium: fizzes vigorously, moves rapidly, may catch fire)\n'
                         '\n'
                         '2K + 2H₂O → 2KOH + H₂\n'
                         '(Potassium: reacts very vigorously, the hydrogen gas ignites immediately with a lilac '
                         'flame)\n'
                         '\n'
                         'The resulting solution is ALKALINE — the metal hydroxide (LiOH, NaOH, KOH) is a strong '
                         'alkali. Adding universal indicator to the solution turns it PURPLE.\n'
                         '\n'
                         'As you go DOWN the group, reactions become MORE vigorous — potassium is more reactive than '
                         'sodium, which is more reactive than lithium.',
              'heading': 'Reactions with Water'},
             {'content': 'Reactivity INCREASES going DOWN Group 1 — this is explained by atomic structure.\n'
                         '\n'
                         'Going down the group:\n'
                         'ATOMS GET LARGER — more electron shells are added.\n'
                         'OUTER ELECTRON is in a higher shell — further from the nucleus.\n'
                         'Electrostatic attraction from nucleus to outer electron DECREASES (greater distance AND more '
                         'shielding from inner electrons).\n'
                         'Outer electron is MORE EASILY LOST.\n'
                         'More reactive → more easily loses the outer electron.\n'
                         '\n'
                         'Memory aid: further = weaker pull = easier to lose = more reactive.\n'
                         '\n'
                         'This is why rubidium and caesium (further down) are so reactive they must be handled with '
                         'extreme care — they can ignite explosively in water or air.',
              'heading': 'Why Reactivity Increases Down Group 1'}],
  'title': 'Group 1 — Alkali Metals',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Reactivity DECREASES down Group 7 — the OPPOSITE of Group 1. In Group 1, going down makes metals '
                    'MORE reactive (outer electron easier to LOSE). In Group 7, going down makes non-metals LESS '
                    'reactive (harder to GAIN an extra electron when the outer shell is further away).',
  'equations': ['Cl₂ + 2NaBr → 2NaCl + Br₂', 'Cl₂ + 2KI → 2KCl + I₂', 'Br₂ + 2KI → 2KBr + I₂'],
  'fifas': [],
  'higher': None,
  'id': 'group-7',
  'key_note': 'Group 7: halogens, 7 outer electrons, form −1 ions, diatomic molecules (X₂). Boiling point increases '
              'down group. Reactivity DECREASES down group (outer shell further away, weaker pull on incoming '
              'electron). More reactive halogen displaces less reactive from solution.',
  'matching': {'instruction': 'Predict whether a reaction occurs and match to the correct outcome.',
               'pairs': [('Reaction occurs',
                          'Cl₂ + NaBr solution — chlorine displaces bromine (Cl more reactive than Br)'),
                         ('Reaction occurs', 'Br₂ + KI solution — bromine displaces iodine (Br more reactive than I)'),
                         ('No reaction',
                          'Br₂ + NaCl solution — bromine cannot displace chlorine (Cl is MORE reactive)'),
                         ('Reaction occurs', 'Cl₂ + KI solution — chlorine displaces iodine (Cl more reactive than I)'),
                         ('No reaction',
                          'I₂ + NaCl solution — iodine cannot displace chlorine (Cl is much more reactive)')],
               'title': 'Match the Halogen Displacement Reaction'},
  'quiz': [{'opts': [('The solution turns orange/brown — chlorine displaces bromide ions, releasing bromine', True),
                     ('No change — chlorine cannot react with bromide ions', False),
                     ('The solution turns pale green — chlorine is absorbed by the solution', False),
                     ('A white precipitate forms — chlorine reacts with potassium ions', False)],
            'q': 'Chlorine water is added to a solution of potassium bromide. What is observed?',
            'wrong_explanations': {1: 'Chlorine IS more reactive than bromine and CAN displace bromide — so a reaction '
                                      'does occur.',
                                   2: 'Chlorine water has a yellow-green colour but when it reacts with bromide, the '
                                      'BROWN colour of bromine is what appears in the solution.',
                                   3: 'Chlorine does not react with potassium ions — it displaces bromide ions. No '
                                      'precipitate forms.'}},
           {'opts': [('Fluorine is a smaller atom — its outer shell is closer to the nucleus, so it attracts an '
                      'incoming electron more strongly',
                      True),
                     ('Fluorine has fewer electrons, making it less stable and more reactive', False),
                     ('Fluorine has more protons, making its positive charge stronger', False),
                     ('Fluorine is a gas, making it react more easily than other states of matter', False)],
            'q': 'Why is fluorine more reactive than chlorine?',
            'wrong_explanations': {1: 'Fewer electrons in an outer shell means the atom needs to GAIN electrons — but '
                                      "that doesn't directly explain why fluorine attracts electrons more strongly. "
                                      'The distance from the nucleus is the key factor.',
                                   2: 'Fluorine does have fewer protons (9) than chlorine (17) — but its outer shell '
                                      'is MUCH closer to those protons. The closeness wins over the fewer-proton '
                                      'effect.',
                                   3: 'Chlorine is also a gas — being a gas is not the reason fluorine is more '
                                      'reactive.'}},
           {'opts': [('No reaction — iodine is less reactive than chlorine and cannot displace it', True),
                     ('Chlorine gas is released — iodine displaces chloride ions', False),
                     ('A brown precipitate forms — iodine reacts with sodium ions', False),
                     ('The solution turns pale yellow — iodine bleaches the solution', False)],
            'q': 'Iodine solution is added to sodium chloride solution. What happens?',
            'wrong_explanations': {1: 'A more reactive halogen displaces a less reactive one. Iodine is LESS reactive '
                                      'than chlorine — so iodine cannot displace chloride ions.',
                                   2: 'Iodine does not react with sodium ions — and even if it tried to displace '
                                      "chloride, it couldn't because iodine is less reactive than chlorine.",
                                   3: "Iodine actually turns starch blue-black — it doesn't bleach. Chlorine is the "
                                      'halogen with bleaching properties.'}}],
  'rp': None,
  'spec': '5.1.2.6',
  'summary': 'Describe the properties of halogens and explain trends in reactivity down Group 7.',
  'theory': [{'content': 'GROUP 7 contains the HALOGENS:\n'
                         'Fluorine (F) — pale yellow gas.\n'
                         'Chlorine (Cl) — yellow-green gas.\n'
                         'Bromine (Br) — red-brown liquid.\n'
                         'Iodine (I) — grey-black solid (purple vapour).\n'
                         'Astatine (At) — radioactive, very rare.\n'
                         '\n'
                         'All Group 7 elements:\n'
                         'Have 7 OUTER ELECTRONS — they gain ONE electron to form −1 ions (halide ions: F⁻, Cl⁻, Br⁻, '
                         'I⁻).\n'
                         'Exist as DIATOMIC MOLECULES — F₂, Cl₂, Br₂, I₂ (each molecule is two atoms bonded '
                         'together).\n'
                         'Are NON-METALS — poor conductors, low melting/boiling points (except iodine which is a '
                         'solid).\n'
                         "React with metals to form SALTS (compounds containing halide ions) — hence 'halogens' means "
                         "'salt-forming'.\n"
                         'Are TOXIC — they are all poisonous in varying degrees.',
              'heading': 'Properties of the Halogens'},
             {'content': 'Going DOWN Group 7 (F → Cl → Br → I):\n'
                         '\n'
                         'PHYSICAL TRENDS:\n'
                         'MELTING AND BOILING POINT INCREASE:\n'
                         'F₂: −188°C, Cl₂: −101°C, Br₂: 59°C, I₂: 184°C.\n'
                         'Larger molecules → stronger London dispersion forces → higher boiling point.\n'
                         '\n'
                         'COLOUR BECOMES DARKER:\n'
                         'Fluorine: pale yellow, Chlorine: yellow-green, Bromine: red-brown, Iodine: grey-black.\n'
                         '\n'
                         'CHEMICAL TREND:\n'
                         'REACTIVITY DECREASES going down — OPPOSITE to Group 1.\n'
                         '\n'
                         'Fluorine is the MOST REACTIVE non-metal known.\n'
                         'Iodine is much less reactive.\n'
                         '\n'
                         'Why reactivity decreases:\n'
                         'Going down, atoms get LARGER — more electron shells.\n'
                         'The outer shell (where the incoming electron goes) is further from the nucleus.\n'
                         'Weaker attraction for an incoming electron → less easily gained → less reactive.',
              'heading': 'Physical and Chemical Trends Down Group 7'},
             {'content': 'A MORE REACTIVE halogen will DISPLACE a LESS REACTIVE halogen from its salt solution.\n'
                         '\n'
                         'This demonstrates the reactivity order: F > Cl > Br > I.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Chlorine water + sodium bromide solution:\n'
                         'Cl₂ + 2NaBr → 2NaCl + Br₂\n'
                         'Colour change: colourless → orange/brown (bromine appears).\n'
                         'Chlorine DISPLACES bromine because Cl is more reactive than Br.\n'
                         '\n'
                         'Chlorine water + potassium iodide solution:\n'
                         'Cl₂ + 2KI → 2KCl + I₂\n'
                         'Colour change: colourless → brown (iodine appears).\n'
                         '\n'
                         'Bromine water + potassium iodide solution:\n'
                         'Br₂ + 2KI → 2KBr + I₂\n'
                         'Bromine displaces iodine — bromine is more reactive than iodine.\n'
                         '\n'
                         'NO REACTION: bromine water + sodium chloride — bromine CANNOT displace chlorine as Cl is '
                         'more reactive.\n'
                         '\n'
                         'OIL LAYER TRICK: Add a non-polar solvent (e.g. cyclohexane) which forms a separate layer — '
                         'iodine in the oil layer turns VIOLET/PURPLE, bromine turns ORANGE.',
              'heading': 'Displacement Reactions of Halogens'}],
  'title': 'Group 7 — Halogens',
  'triple_only': None,
  'variables': []}],

"bonding": [{'common_mistake': 'The strong bond in a covalent MOLECULE is between atoms within the molecule. The WEAK forces '
                    'between separate molecules (intermolecular forces) are what give simple molecular substances '
                    'their LOW melting points. Students often confuse the strong covalent bond (within a molecule) '
                    'with the weak intermolecular forces (between molecules).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'chemical-bonds',
  'key_note': 'Metal + non-metal → ionic (electron transfer). Non-metal + non-metal → covalent (electron sharing). '
              'Metal → metallic (electron sea). Bond type determines properties: ionic = high MP, conducts when '
              'molten/dissolved; simple covalent = low MP; metallic = conducts, malleable.',
  'matching': {'instruction': 'Match each substance to its bond type and why it forms that way.',
               'pairs': [('Ionic', 'Sodium chloride (NaCl) — metal Na transfers electron to non-metal Cl'),
                         ('Covalent', 'Water (H₂O) — two non-metals sharing electrons'),
                         ('Metallic', 'Copper wire — metal atoms releasing electrons into a delocalised sea'),
                         ('Ionic', 'Magnesium oxide (MgO) — metal + non-metal, electron transfer'),
                         ('Covalent', 'Carbon dioxide (CO₂) — two non-metals sharing electron pairs')],
               'title': 'Match the Bond Type'},
  'quiz': [{'opts': [('Ionic bonding — the metal transfers electrons to the non-metal, forming oppositely charged ions',
                      True),
                     ('Covalent bonding — the metal shares electrons with the non-metal', False),
                     ('Metallic bonding — electrons are released into a delocalised sea', False),
                     ('Hydrogen bonding — a weak attraction between the two atoms', False)],
            'q': 'Which type of bonding occurs between a metal and a non-metal?',
            'wrong_explanations': {1: 'Covalent bonding occurs between NON-METALS only — metals do not typically share '
                                      'electrons.',
                                   2: 'Metallic bonding occurs in PURE METALS or alloys — not between a metal and a '
                                      'non-metal.',
                                   3: 'Hydrogen bonding is a type of intermolecular force, not a primary bond type '
                                      'between elements — and it is not what forms between a metal and non-metal.'}},
           {'opts': [('Ionic — magnesium transfers 2 electrons to oxygen, forming Mg²⁺ and O²⁻ ions', True),
                     ('Covalent — they share 2 electrons to fill their outer shells', False),
                     ('Metallic — magnesium releases electrons into a sea', False),
                     ("No bonding — they don't react because both are stable elements", False)],
            'q': 'Magnesium (Group 2) reacts with oxygen (Group 6) to form magnesium oxide. What type of bonding does '
                 'MgO have?',
            'wrong_explanations': {1: 'Magnesium and oxygen share electrons in covalent bonds — this only happens '
                                      'between two non-metals. Magnesium is a metal.',
                                   2: 'Metallic bonding occurs in metals only — not in compounds containing both a '
                                      'metal and non-metal.',
                                   3: 'Magnesium burns vigorously in oxygen — it is very reactive. The product MgO is '
                                      'a stable ionic compound.'}}],
  'rp': None,
  'spec': '5.2.1.1',
  'summary': 'Describe why atoms form chemical bonds and the three main types of bonding.',
  'theory': [{'content': 'Atoms form chemical bonds to achieve a MORE STABLE electron configuration — usually a FULL '
                         'OUTER SHELL, like the noble gases.\n'
                         '\n'
                         'Atoms with incomplete outer shells have a tendency to either:\n'
                         'LOSE electrons (metals — Group 1, 2, 3)\n'
                         'GAIN electrons (non-metals — Group 5, 6, 7)\n'
                         'SHARE electrons (non-metals bonding with non-metals)\n'
                         '\n'
                         'The type of bonding that forms depends on what types of atoms are combining:\n'
                         'METAL + NON-METAL → IONIC bonding (electron transfer)\n'
                         'NON-METAL + NON-METAL → COVALENT bonding (electron sharing)\n'
                         'METAL + METAL (or pure metal) → METALLIC bonding (electron sea)',
              'heading': 'Why Do Atoms Bond?'},
             {'content': 'IONIC BONDING:\n'
                         'Occurs between a METAL and a NON-METAL.\n'
                         'The metal TRANSFERS one or more electrons to the non-metal.\n'
                         'Metal becomes a POSITIVE ION (cation). Non-metal becomes a NEGATIVE ION (anion).\n'
                         'OPPOSITE CHARGES ATTRACT — strong electrostatic force holds the ions together.\n'
                         'Example: sodium chloride (NaCl) — Na transfers 1 electron to Cl.\n'
                         '\n'
                         'COVALENT BONDING:\n'
                         'Occurs between NON-METALS.\n'
                         'Atoms SHARE pairs of electrons — each shared pair counts as one covalent bond.\n'
                         'Both atoms count the shared electrons as their own — achieving full outer shells.\n'
                         'Example: water (H₂O) — oxygen shares electrons with two hydrogen atoms.\n'
                         '\n'
                         'METALLIC BONDING:\n'
                         'Occurs in PURE METALS and ALLOYS.\n'
                         "Metal atoms release their outer electrons into a 'SEA' of delocalised electrons.\n"
                         'Positive metal ions (left behind) are surrounded by and attracted to these free electrons.\n'
                         'The delocalised electrons can move freely throughout the structure.\n'
                         'Example: copper (Cu), iron (Fe), all metals.',
              'heading': 'The Three Types of Chemical Bond'},
             {'content': 'The type of bonding directly determines the properties of the substance:\n'
                         '\n'
                         'IONIC compounds:\n'
                         'High melting and boiling points (strong electrostatic forces between ions).\n'
                         'Conduct electricity when molten or dissolved (ions can move).\n'
                         'Usually soluble in water.\n'
                         '\n'
                         'COVALENT substances:\n'
                         'Simple molecules: low melting/boiling points (weak forces BETWEEN molecules).\n'
                         'Giant covalent: very high melting points (strong covalent bonds throughout).\n'
                         'Generally do not conduct electricity.\n'
                         '\n'
                         'METALLS:\n'
                         'High melting/boiling points (strong metallic bonds).\n'
                         'Excellent electrical and thermal conductors (delocalised electrons).\n'
                         'Malleable and ductile (layers of ions can slide).',
              'heading': 'Bond Type and Properties'}],
  'title': 'Chemical Bonds',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The IONIC BOND is the electrostatic attraction between OPPOSITELY charged ions — NOT the transfer '
                    'of electrons itself. The transfer creates the ions; the attraction between them IS the bond. '
                    'Also: ionic compounds always have an overall charge of ZERO — the positive and negative charges '
                    'must balance.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'ionic-bonding',
  'key_note': 'Ionic bonding: metal loses electrons → positive ion. Non-metal gains electrons → negative ion. Opposite '
              'charges attract → ionic bond. Both achieve full outer shells. Group number tells you charge: Group 1 → '
              '+1, Group 7 → −1 etc. Overall compound charge = zero.',
  'matching': {'instruction': 'Match each element to the ion it forms and why.',
               'pairs': [('Sodium (Group 1)', 'Na⁺ — loses 1 electron to achieve noble gas configuration'),
                         ('Magnesium (Group 2)', 'Mg²⁺ — loses 2 electrons to achieve noble gas configuration'),
                         ('Chlorine (Group 7)', 'Cl⁻ — gains 1 electron to achieve noble gas configuration'),
                         ('Oxygen (Group 6)', 'O²⁻ — gains 2 electrons to achieve noble gas configuration'),
                         ('Aluminium (Group 3)', 'Al³⁺ — loses 3 electrons to achieve noble gas configuration')],
               'title': 'Match the Ion to its Charge'},
  'quiz': [{'opts': [('Sodium loses 1 electron → Na⁺ (2.8). Chlorine gains 1 electron → Cl⁻ (2.8.8). Opposite charges '
                      'attract.',
                      True),
                     ('Sodium and chlorine share 1 electron pair to form a single covalent bond.', False),
                     ('Both atoms lose electrons to form a positive lattice structure.', False),
                     ('Chlorine loses 1 electron to sodium, making chlorine positive.', False)],
            'q': 'When sodium (2.8.1) reacts with chlorine (2.8.7) to form NaCl, what happens?',
            'wrong_explanations': {1: 'Covalent bonds involve sharing — NaCl is ionic (metal + non-metal = electron '
                                      'TRANSFER).',
                                   2: 'In ionic bonding only the METAL loses electrons — the non-metal GAINS them.',
                                   3: "Chlorine GAINS electrons (it needs 1 more to fill its outer shell) — it doesn't "
                                      'lose them. Non-metals gain electrons to form negative ions.'}},
           {'opts': [('CaCl₂ — Ca forms Ca²⁺, each Cl forms Cl⁻, so 2 chloride ions needed to balance the 2+ charge',
                      True),
                     ('CaCl — 1 calcium bonds with 1 chlorine', False),
                     ('Ca₂Cl — 2 calcium atoms bond with 1 chlorine', False),
                     ('CaCl₃ — calcium needs 3 chlorine atoms to be stable', False)],
            'q': 'What is the formula of calcium chloride? (Calcium is Group 2, Chlorine is Group 7)',
            'wrong_explanations': {1: 'CaCl would give a total charge of +2 + (−1) = +1 — not neutral. Ionic compounds '
                                      'must have zero overall charge.',
                                   2: 'Ca₂Cl would give 2×(+2) + (−1) = +3 — not neutral.',
                                   3: 'CaCl₃ would give +2 + 3×(−1) = −1 — not neutral. You need exactly 2 Cl⁻ to '
                                      'balance 1 Ca²⁺.'}}],
  'rp': None,
  'spec': '5.2.1.2',
  'summary': 'Describe how ionic bonds form by electron transfer between metals and non-metals.',
  'theory': [{'content': 'IONIC BONDING occurs between a METAL and a NON-METAL.\n'
                         '\n'
                         'The process:\n'
                         '1. The metal atom LOSES one or more electrons from its outer shell.\n'
                         '2. The non-metal atom GAINS those electrons into its outer shell.\n'
                         '3. Both atoms now have FULL OUTER SHELLS — stable noble gas configurations.\n'
                         '4. The metal becomes a POSITIVE ION (it lost negative electrons → net positive).\n'
                         '5. The non-metal becomes a NEGATIVE ION (it gained negative electrons → net negative).\n'
                         '6. OPPOSITE CHARGES ATTRACT — a strong electrostatic force holds the ions together.\n'
                         '\n'
                         'This electrostatic attraction between oppositely charged ions IS the ionic bond.\n'
                         '\n'
                         'The ions arrange themselves into a regular 3D lattice structure — many ions alternating '
                         'positive and negative in a giant ionic lattice.',
              'heading': 'How Ionic Bonds Form'},
             {'content': 'DOT-AND-CROSS diagrams show which atoms the electrons came from.\n'
                         'Convention: use dots (•) for electrons from one atom and crosses (×) for electrons from '
                         'another.\n'
                         '\n'
                         'SODIUM CHLORIDE (NaCl):\n'
                         'Na: 2.8.1 — loses its 1 outer electron → becomes Na⁺ (2.8)\n'
                         'Cl: 2.8.7 — gains 1 electron → becomes Cl⁻ (2.8.8)\n'
                         '\n'
                         'MAGNESIUM OXIDE (MgO):\n'
                         'Mg: 2.8.2 — loses 2 outer electrons → becomes Mg²⁺ (2.8)\n'
                         'O: 2.6 — gains 2 electrons → becomes O²⁻ (2.8)\n'
                         '\n'
                         'MAGNESIUM CHLORIDE (MgCl₂):\n'
                         'Mg: loses 2 electrons → Mg²⁺\n'
                         'Each Cl gains 1 electron → each becomes Cl⁻\n'
                         '2 chloride ions are needed per magnesium (to accept both electrons).\n'
                         'Formula: MgCl₂',
              'heading': 'Using Dot-and-Cross Diagrams'},
             {'content': 'You can predict the charge on an ion from its GROUP in the periodic table:\n'
                         '\n'
                         'GROUP 1 metals → lose 1 electron → +1 ions (Li⁺, Na⁺, K⁺)\n'
                         'GROUP 2 metals → lose 2 electrons → +2 ions (Mg²⁺, Ca²⁺)\n'
                         'GROUP 3 metals → lose 3 electrons → +3 ions (Al³⁺)\n'
                         '\n'
                         'GROUP 5 non-metals → gain 3 electrons → −3 ions (N³⁻, P³⁻)\n'
                         'GROUP 6 non-metals → gain 2 electrons → −2 ions (O²⁻, S²⁻)\n'
                         'GROUP 7 non-metals → gain 1 electron → −1 ions (F⁻, Cl⁻, Br⁻, I⁻)\n'
                         '\n'
                         'The OVERALL CHARGE of an ionic compound must be ZERO — positive and negative charges '
                         'balance.\n'
                         'For MgCl₂: Mg²⁺ needs 2 Cl⁻ to balance (2+ and 2×1− = 0). ✓\n'
                         'For Al₂O₃: 2 Al³⁺ (6+) needs 3 O²⁻ (6−) to balance. ✓',
              'heading': 'Predicting Ion Charges from Group Number'}],
  'title': 'Ionic Bonding',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Ionic compounds conduct electricity when MOLTEN or in SOLUTION — NOT when solid. The ions in '
                    'solid ionic compounds are held in fixed positions in the lattice and cannot move. Melting or '
                    'dissolving gives the ions freedom to move — and moving charged particles = electrical '
                    'conductivity.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'ionic-compounds',
  'key_note': 'Giant ionic lattice: regular 3D arrangement of alternating + and − ions held by strong electrostatic '
              'forces in all directions. High MP/BP (strong forces). Brittle (layers shift → ion repulsion). Solid: no '
              'conduction (ions fixed). Molten/dissolved: conducts (ions free to move).',
  'matching': {'instruction': 'Match each property to its structural explanation.',
               'pairs': [('High melting point',
                          'Strong electrostatic forces throughout the giant ionic lattice require a lot of energy to '
                          'break'),
                         ('Brittle',
                          'Layers shift under force → like charges align → strong repulsion → crystal shatters'),
                         ('Does not conduct when solid',
                          'Ions in fixed lattice positions — cannot move to carry charge'),
                         ('Conducts when molten or dissolved',
                          'Ions are free to move through the liquid — mobile charged particles carry the current'),
                         ('Often soluble in water',
                          'Water molecules attract and surround ions, pulling them away from the lattice')],
               'title': 'Ionic Compound Property — Explain Why'},
  'quiz': [{'opts': [('Solid: ions in fixed positions — cannot move. Molten: ions free to move and carry charge.',
                      True),
                     ('Solid NaCl has no ions — they only form when the compound melts.', False),
                     ('Solid NaCl is an insulator because it is white — colour prevents conductivity.', False),
                     ('Molten NaCl produces electrons that carry the current — not ions.', False)],
            'q': 'Why does solid sodium chloride not conduct electricity, but molten sodium chloride does?',
            'wrong_explanations': {1: 'NaCl is always ionic — the Na⁺ and Cl⁻ ions exist in the solid lattice. They '
                                      "just can't MOVE when solid.",
                                   2: 'Colour has no effect on electrical conductivity.',
                                   3: 'Ionic conduction is carried by IONS (charged atoms), not electrons. Electron '
                                      'conduction occurs in metals.'}},
           {'opts': [('Strong electrostatic forces between many oppositely charged ions throughout the giant lattice '
                      'require a lot of energy to overcome',
                      True),
                     ('The large size of ionic crystals means more energy is needed to melt the whole crystal', False),
                     ('Ionic compounds contain strong covalent bonds that must be broken', False),
                     ('The electrons in ionic compounds are tightly held and resist heating', False)],
            'q': 'Why do ionic compounds have high melting points?',
            'wrong_explanations': {1: "Physical size of a crystal doesn't determine melting point — the STRENGTH of "
                                      'bonding does.',
                                   2: 'Ionic compounds contain IONIC bonds (electrostatic attractions between ions) — '
                                      'not covalent bonds.',
                                   3: 'Electrons in ionic compounds are transferred to ions — they are not the source '
                                      'of high melting point.'}}],
  'rp': None,
  'spec': '5.2.1.3',
  'summary': 'Describe the giant ionic lattice structure of ionic compounds and link it to their properties.',
  'theory': [{'content': "When ionic compounds form, the positive and negative ions don't just stay in pairs — they "
                         'arrange themselves into a GIANT IONIC LATTICE.\n'
                         '\n'
                         'A giant ionic lattice is:\n'
                         'A regular, 3-dimensional arrangement of alternating positive and negative ions.\n'
                         'Each ion is surrounded by oppositely charged ions on all sides.\n'
                         'Held together by STRONG ELECTROSTATIC FORCES in all directions.\n'
                         '\n'
                         'The word GIANT means there are enormous numbers of ions — a typical crystal contains '
                         'billions of ions in a regular repeating pattern.\n'
                         '\n'
                         'Example: Sodium chloride (NaCl):\n'
                         'Na⁺ ions and Cl⁻ ions alternate in all three dimensions.\n'
                         'Each Na⁺ is surrounded by 6 Cl⁻ ions (and vice versa).\n'
                         'The ratio of Na⁺ : Cl⁻ = 1:1 throughout the lattice.\n'
                         '\n'
                         'This structure is very strong — requiring a lot of energy to break the many ion-ion '
                         'attractions.',
              'heading': 'The Giant Ionic Lattice'},
             {'content': 'The giant ionic lattice structure explains ALL the key properties:\n'
                         '\n'
                         'HIGH MELTING AND BOILING POINTS:\n'
                         'The electrostatic forces between ions throughout the lattice are very strong.\n'
                         'A lot of energy is needed to overcome them and separate the ions.\n'
                         'NaCl melts at 801°C; MgO melts at 2852°C.\n'
                         '\n'
                         'BRITTLE:\n'
                         'When force is applied, layers of ions shift slightly.\n'
                         'Similarly charged ions end up next to each other → repel strongly → the crystal SHATTERS '
                         'rather than bending.\n'
                         '\n'
                         'DO NOT CONDUCT ELECTRICITY WHEN SOLID:\n'
                         'Ions in the solid lattice are in fixed positions — they cannot move.\n'
                         'Electrical conductivity requires charged particles that can move freely.\n'
                         '\n'
                         'DO CONDUCT ELECTRICITY WHEN MOLTEN OR IN SOLUTION:\n'
                         'When melted or dissolved in water, ions are FREE TO MOVE.\n'
                         'The mobile ions carry charge through the liquid → conducts electricity.\n'
                         'This is why ionic compounds are electrolytes.',
              'heading': 'Properties of Ionic Compounds'},
             {'content': 'Many ionic compounds are SOLUBLE IN WATER:\n'
                         'Water molecules (which are polar — they have a partial charge) are attracted to the ions.\n'
                         'Water molecules surround the ions and pull them away from the lattice one by one.\n'
                         'The ions become surrounded by water molecules (hydrated) — this is DISSOLVING.\n'
                         '\n'
                         'When dissolved, the ions are spread throughout the solution and can move freely → the '
                         'solution conducts electricity.\n'
                         '\n'
                         'Not all ionic compounds are soluble:\n'
                         'Some lattices have very strong attractions (e.g. BaSO₄) that water cannot overcome → '
                         'insoluble.\n'
                         'Insoluble ionic compounds can form as PRECIPITATES when two solutions are mixed.\n'
                         '\n'
                         'Example: mixing silver nitrate with sodium chloride:\n'
                         "Ag⁺ ions + Cl⁻ ions → AgCl precipitate (a white solid that doesn't dissolve).",
              'heading': 'Solubility of Ionic Compounds'}],
  'title': 'Ionic Compounds',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Covalent bonds are STRONG — but simple molecular substances have LOW melting points because the '
                    'FORCES BETWEEN molecules (intermolecular forces) are WEAK. The covalent bond is within the '
                    'molecule; melting involves separating molecules from each other (overcoming intermolecular '
                    'forces), not breaking the bonds within them.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'covalent-bonding',
  'key_note': 'Covalent bonding: non-metals share electron pairs. Each shared pair = one covalent bond. Both atoms '
              'achieve full outer shells. Single bond: 1 shared pair. Double bond: 2 shared pairs. Covalent bonds '
              'within molecules are STRONG. Intermolecular forces between molecules are WEAK → low melting points.',
  'matching': {'instruction': 'Match each molecule to how many covalent bonds it contains.',
               'pairs': [('H₂', '1 single covalent bond — 1 shared pair between 2 H atoms'),
                         ('H₂O', '2 single covalent bonds — O forms 2 bonds with 2 H atoms'),
                         ('CH₄', '4 single covalent bonds — C forms 4 bonds with 4 H atoms'),
                         ('O₂', '1 double covalent bond — 2 shared pairs between 2 O atoms'),
                         ('N₂', '1 triple covalent bond — 3 shared pairs between 2 N atoms')],
               'title': 'Match the Molecule to its Bonding'},
  'quiz': [{'opts': [('4 — carbon has 4 outer electrons and needs 4 more to achieve a full shell of 8', True),
                     ('1 — carbon only forms one bond at a time', False),
                     ('2 — carbon forms 2 bonds like oxygen', False),
                     ('8 — carbon needs to reach a total of 8 electrons', False)],
            'q': 'Carbon (Group 4) bonds with hydrogen (Group 1) to form methane (CH₄). How many covalent bonds does '
                 'carbon form?',
            'wrong_explanations': {1: 'Carbon forms one bond per atom, not one bond total. Each covalent bond shares 2 '
                                      'electrons — carbon forms 4 bonds to share 4 × 2 = 8 electrons total.',
                                   2: 'Oxygen (Group 6) needs 2 more electrons — so it forms 2 bonds. Carbon (Group 4) '
                                      'needs 4 more.',
                                   3: 'Carbon needs 8 electrons in its outer shell — but each BOND provides 2 shared '
                                      'electrons. 4 bonds × 2 = 8 electrons total in the outer shell.'}},
           {'opts': [('An oxygen atom has 6 outer electrons — sharing 2 pairs with another O atom gives both atoms a '
                      'full outer shell of 8',
                      True),
                     ('Two oxygen atoms bond to make a more stable element in the periodic table', False),
                     ('Oxygen atoms repel each other and form O₂ to cancel the repulsion', False),
                     ('O₂ is formed because oxygen needs to be a gas at room temperature', False)],
            'q': 'Why does oxygen exist as O₂ rather than individual O atoms?',
            'wrong_explanations': {1: 'This confuses bonding with stability classification — O₂ forms because of '
                                      "electron configuration, not because it changes the element's position.",
                                   2: 'Atoms of the same element have the same charge and actually do repel each other '
                                      'slightly — but covalent bonding (SHARING electrons) overcomes this by creating '
                                      'a stronger attraction.',
                                   3: 'Whether a substance is a gas depends on intermolecular forces, not on why O₂ '
                                      'forms. O₂ forms because of electronic structure.'}}],
  'rp': None,
  'spec': '5.2.1.4',
  'summary': 'Describe how covalent bonds form by electron sharing between non-metal atoms.',
  'theory': [{'content': 'COVALENT BONDING occurs between NON-METAL atoms.\n'
                         '\n'
                         'Instead of transferring electrons (as in ionic bonding), non-metals SHARE pairs of '
                         'electrons.\n'
                         '\n'
                         'Each shared pair of electrons counts as ONE COVALENT BOND.\n'
                         '\n'
                         'Why sharing works:\n'
                         'Each atom counts the shared electrons as part of its OWN outer shell.\n'
                         'Both atoms achieve full outer shells — without either losing electrons entirely.\n'
                         '\n'
                         'The shared electrons are attracted to BOTH nuclei — this attraction holds the atoms '
                         'together.\n'
                         '\n'
                         'Covalent bonds are STRONG — a lot of energy is needed to break an individual covalent bond '
                         'within a molecule.',
              'heading': 'How Covalent Bonds Form'},
             {'content': 'HYDROGEN (H₂):\n'
                         'Each H has 1 electron — needs 1 more for a full shell (2 electrons).\n'
                         "Two H atoms share 1 pair of electrons → single covalent bond → each H now 'has' 2 electrons. "
                         '✓\n'
                         '\n'
                         'WATER (H₂O):\n'
                         'O has 6 outer electrons — needs 2 more. H has 1 — needs 1 more.\n'
                         'O forms 2 covalent bonds, one with each H atom.\n'
                         'O now has 8 outer electrons (full). Each H has 2 (full). ✓\n'
                         '\n'
                         'AMMONIA (NH₃):\n'
                         'N has 5 outer electrons — needs 3 more.\n'
                         'N forms 3 single covalent bonds with 3 H atoms.\n'
                         '\n'
                         'METHANE (CH₄):\n'
                         'C has 4 outer electrons — needs 4 more.\n'
                         'C forms 4 single covalent bonds with 4 H atoms.\n'
                         '\n'
                         'OXYGEN (O₂):\n'
                         'Each O has 6 outer electrons — needs 2 more.\n'
                         'Two O atoms share 2 pairs of electrons → DOUBLE covalent bond.\n'
                         '\n'
                         'NITROGEN (N₂):\n'
                         'Each N has 5 outer electrons — needs 3 more.\n'
                         'Two N atoms share 3 pairs → TRIPLE covalent bond. N₂ is very stable.',
              'heading': 'Examples of Covalent Molecules'},
             {'content': 'DOT-AND-CROSS diagrams show the shared electrons in covalent bonds.\n'
                         '\n'
                         'Convention: each pair of electrons in a bond is shown between the two atoms. Lone pairs '
                         '(non-bonding) are shown on the relevant atom.\n'
                         '\n'
                         'H₂: H × H  (one shared pair between the two H atoms — single bond)\n'
                         '\n'
                         'H₂O:\n'
                         '  H—O—H  with 2 lone pairs on O.\n'
                         'The 2 bonding pairs give O its full 8, and each H its full 2.\n'
                         '\n'
                         'CH₄ (methane):\n'
                         '  4 H atoms arranged around central C.\n'
                         '  4 single bonds — C has 8 electrons in outer shell. Each H has 2.\n'
                         '\n'
                         'CO₂:\n'
                         '  O=C=O — two double bonds.\n'
                         '  C has 8 outer electrons (two sets of 2 shared). Each O also has 8.\n'
                         '\n'
                         'The key rule: every atom in a correctly drawn dot-and-cross diagram should have a FULL OUTER '
                         'SHELL.',
              'heading': 'Dot-and-Cross Diagrams for Covalent Molecules'}],
  'title': 'Covalent Bonding',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The metallic bond is the attraction between POSITIVE METAL IONS and the SEA OF DELOCALISED '
                    'ELECTRONS — not between individual atoms directly. Malleability works because ion LAYERS slide — '
                    'the electron sea allows this without breaking bonds. If layers had to break ionic bonds (like in '
                    'ionic compounds), the metal would shatter instead of bend.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'metallic-bonding',
  'key_note': 'Metallic bonding: positive metal ions in a lattice + sea of delocalised electrons. High MP/BP (strong '
              'electrostatic forces). Conducts electricity and heat (delocalised electrons move freely). '
              'Malleable/ductile (layers slide, electron sea remains). Alloys harder — different sized atoms disrupt '
              'regular lattice.',
  'matching': {'instruction': 'Match each metal property to its structural reason.',
               'pairs': [('Good electrical conductor',
                          'Delocalised electrons move freely through the structure, carrying charge'),
                         ('High melting point',
                          'Strong electrostatic attraction between positive ions and electron sea'),
                         ('Malleable',
                          'Layers of ions can slide over each other — electron sea re-surrounds ions in new positions'),
                         ('Good thermal conductor',
                          'Delocalised electrons transfer thermal energy rapidly through the structure'),
                         ('Alloys are harder',
                          'Different-sized atoms disrupt the regular lattice — layers cannot slide as easily')],
               'title': 'Metallic Property — Structural Explanation'},
  'quiz': [{'opts': [('Delocalised electrons can move freely through the metallic lattice and carry charge', True),
                     ('Metal ions are positively charged and attract electrical current', False),
                     ('Metals have more protons than non-metals, making them better at conducting', False),
                     ('The regular lattice of metal ions allows electrical signals to travel between them', False)],
            'q': 'Why are metals good conductors of electricity?',
            'wrong_explanations': {1: 'Positive ions ATTRACT electrons but do not themselves move to carry current — '
                                      'it is the mobile delocalised electrons that carry charge.',
                                   2: "Proton count determines the element's identity, not its conductivity — "
                                      'non-metals can also have many protons but are poor conductors.',
                                   3: 'The lattice provides the structure, but conductivity comes from the FREE '
                                      'electrons, not from the ions themselves.'}},
           {'opts': [('Carbon atoms in steel have a different size to iron atoms — they disrupt the regular lattice '
                      'and prevent layers from sliding',
                      True),
                     ('Steel has stronger metallic bonds than iron because it contains more electrons', False),
                     ('Carbon atoms fill the gaps between iron atoms, increasing density and hardness', False),
                     ('Steel is harder because it has been purified — removing impurities strengthens the metal',
                      False)],
            'q': 'Why is steel harder than pure iron?',
            'wrong_explanations': {1: 'Steel has more metallic bonds in total, but the KEY reason is DISRUPTION of the '
                                      'lattice by differently-sized atoms.',
                                   2: 'Carbon atoms do fill interstitial spaces, but the hardening mechanism is '
                                      'specifically about PREVENTING LAYER SLIDING — the lattice disruption model.',
                                   3: 'Steel is iron made LESS pure (with carbon added) — it is the ADDITION of a '
                                      'different-sized element that makes it harder, not purification.'}}],
  'rp': None,
  'spec': '5.2.1.5',
  'summary': 'Describe the metallic bonding model and use it to explain the properties of metals.',
  'theory': [{'content': 'METALLIC BONDING occurs in METALS (and alloys).\n'
                         '\n'
                         'The model:\n'
                         '1. Metal atoms release their OUTER ELECTRONS — these electrons become DELOCALISED, meaning '
                         'they are free to move throughout the entire metal structure.\n'
                         "2. The metal atoms become POSITIVE IONS (they've lost electrons).\n"
                         '3. The positive metal ions are arranged in a regular LATTICE structure.\n'
                         '4. The DELOCALISED ELECTRONS move freely between and around the positive ions — forming a '
                         "'SEA OF ELECTRONS'.\n"
                         '5. STRONG ELECTROSTATIC ATTRACTION between the positive ions and the negative electron sea '
                         'holds the metal together — THIS IS THE METALLIC BOND.\n'
                         '\n'
                         "This model is sometimes called the 'electron sea model' — you can picture metal ions "
                         'floating in a sea of freely moving electrons.',
              'heading': 'The Metallic Bonding Model'},
             {'content': 'The metallic bonding model explains ALL key metal properties:\n'
                         '\n'
                         'HIGH MELTING AND BOILING POINTS:\n'
                         'Strong electrostatic forces between many positive ions and the electron sea.\n'
                         'A lot of energy needed to overcome these forces.\n'
                         'Tungsten (W): melts at 3422°C — one of the highest melting metals.\n'
                         '\n'
                         'GOOD ELECTRICAL CONDUCTORS:\n'
                         'Delocalised electrons can move freely through the structure.\n'
                         'When a voltage is applied, electrons flow — carrying charge.\n'
                         '\n'
                         'GOOD THERMAL CONDUCTORS:\n'
                         'Delocalised electrons also carry thermal (heat) energy rapidly through the structure.\n'
                         '\n'
                         'MALLEABLE (can be hammered into shapes):\n'
                         'Layers of positive ions can SLIDE past each other without breaking the metallic bond — the '
                         'electron sea re-surrounds the ions in any new position.\n'
                         '\n'
                         'DUCTILE (can be drawn into wires):\n'
                         'Same reason — ion layers slide without the structure breaking.',
              'heading': 'Properties Explained by Metallic Bonding'},
             {'content': 'ALLOYS are MIXTURES of metals (or a metal with a small amount of another element — sometimes '
                         'carbon).\n'
                         '\n'
                         'Why alloys are often harder and stronger than pure metals:\n'
                         'In a PURE METAL, all ions are the same size — layers of ions can slide over each other '
                         'easily (making the metal soft and malleable).\n'
                         'In an ALLOY, different sized atoms are introduced — they DISRUPT the regular lattice.\n'
                         'The different-sized atoms prevent layers from sliding as easily → the alloy is HARDER and '
                         'STRONGER than the pure metal.\n'
                         '\n'
                         'Examples of alloys and their uses:\n'
                         'STEEL (iron + carbon) — harder than pure iron — used in construction, tools, cars.\n'
                         'BRONZE (copper + tin) — harder than pure copper — used in sculptures, coins, bearings.\n'
                         'BRASS (copper + zinc) — harder than pure copper — used in musical instruments, door '
                         'fittings.\n'
                         'ALUMINIUM ALLOYS (aluminium + various elements) — strong and lightweight — used in aircraft.',
              'heading': 'Alloys'}],
  'title': 'Metallic Bonding',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Changes of state are PHYSICAL changes — the substance does not change chemically. H₂O is always '
                    'H₂O whether it is ice, water or steam. (aq) means dissolved in WATER specifically — not just any '
                    'liquid. A substance in ethanol or acetone would NOT be labelled (aq).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'states-of-matter',
  'key_note': 'Solid: fixed positions, vibrate. Liquid: close but can flow. Gas: widely spread, rapid random motion. '
              'Melting (s→l), boiling (l→g), condensing (g→l), freezing (l→s). State symbols: (s) solid, (l) liquid, '
              '(g) gas, (aq) aqueous solution.',
  'matching': {'instruction': 'Match each change of state to the correct term.',
               'pairs': [('Melting', 'Solid → liquid — energy added, particles break free from fixed positions'),
                         ('Boiling / evaporation', 'Liquid → gas — energy added, particles escape the liquid surface'),
                         ('Condensation', 'Gas → liquid — energy removed, particles slow and are pulled together'),
                         ('Freezing', 'Liquid → solid — energy removed, particles slow enough to form regular lattice'),
                         ('Sublimation', 'Solid → gas directly — e.g. iodine, dry ice (CO₂)')],
               'title': 'Match the State Change to its Name'},
  'quiz': [{'opts': [('(aq) — aqueous, meaning dissolved in water', True),
                     ('(l) — liquid, because a solution is a liquid', False),
                     ('(d) — dissolved', False),
                     ('(w) — water solution', False)],
            'q': 'What state symbol is used for a substance dissolved in water?',
            'wrong_explanations': {1: '(l) means PURE liquid — e.g. liquid water H₂O(l). A solution of NaCl in water '
                                      'would use NaCl(aq), not NaCl(l).',
                                   2: 'There is no (d) state symbol in chemistry equations.',
                                   3: 'The four state symbols are (s), (l), (g) and (aq) — no (w) symbol exists.'}},
           {'opts': [('Physical change — the chemical formula stays as H₂O; only the arrangement of particles changes',
                      True),
                     ('Chemical change — a new substance (water) is produced from ice', False),
                     ('Chemical change — energy is added, which must have broken chemical bonds', False),
                     ('Neither — melting is a change of state, not classified as physical or chemical', False)],
            'q': 'Ice melts to form water. Is this a physical or chemical change? Explain.',
            'wrong_explanations': {1: 'Ice and water are the same substance — H₂O. Water is NOT a new substance; it is '
                                      'just the same H₂O molecules in a different state.',
                                   2: 'Energy can be added without breaking covalent bonds — melting ice only '
                                      'overcomes the INTERMOLECULAR FORCES (hydrogen bonds between water molecules), '
                                      'not the covalent O-H bonds.',
                                   3: 'Changes of state ARE classified as physical changes — the composition of the '
                                      'substance does not change.'}}],
  'rp': None,
  'spec': '5.2.2.1–5.2.2.2',
  'summary': 'Describe the three states of matter, the changes between them and how to use state symbols.',
  'theory': [{'content': 'All matter exists in one of three states: SOLID, LIQUID or GAS.\n'
                         '\n'
                         'SOLID:\n'
                         'Particles are closely packed in a REGULAR ARRANGEMENT (often a lattice).\n'
                         'Particles VIBRATE about fixed positions — they cannot move past each other.\n'
                         'Definite shape and definite volume.\n'
                         'Incompressible.\n'
                         'Example: ice, sodium chloride, iron.\n'
                         '\n'
                         'LIQUID:\n'
                         'Particles are closely packed but in a RANDOM arrangement.\n'
                         'Particles can FLOW and move past each other (no fixed positions).\n'
                         'No definite shape — takes the shape of its container.\n'
                         'Definite volume.\n'
                         'Incompressible (like solids).\n'
                         'Example: water, mercury, liquid nitrogen.\n'
                         '\n'
                         'GAS:\n'
                         'Particles are widely SPREAD OUT — large distances between them.\n'
                         'Particles move RAPIDLY in all directions — constantly colliding with each other and '
                         'container walls.\n'
                         'No definite shape or volume — fills any container.\n'
                         'Highly compressible (particles can be pushed closer together).\n'
                         'Example: oxygen, steam, carbon dioxide.',
              'heading': 'The Three States of Matter'},
             {'content': 'CHANGES OF STATE occur when energy is added or removed:\n'
                         '\n'
                         'SOLID → LIQUID: MELTING (energy added — particles gain enough energy to break free from '
                         'fixed positions)\n'
                         'LIQUID → GAS: BOILING/EVAPORATION (energy added — particles gain enough energy to escape the '
                         'liquid)\n'
                         'GAS → LIQUID: CONDENSATION (energy removed — particles slow down, intermolecular forces pull '
                         'them back together)\n'
                         'LIQUID → SOLID: FREEZING/SOLIDIFICATION (energy removed — particles slow down enough to form '
                         'fixed lattice)\n'
                         'SOLID → GAS: SUBLIMATION (some solids go directly from solid to gas, e.g. iodine, dry '
                         'ice/CO₂)\n'
                         '\n'
                         'These are PHYSICAL CHANGES — the chemical composition does not change. Water is H₂O whether '
                         'it is ice, liquid water or steam.\n'
                         '\n'
                         'MELTING POINT — temperature at which a solid becomes a liquid.\n'
                         'BOILING POINT — temperature at which a liquid becomes a gas.\n'
                         'At these temperatures, the substance exists in BOTH states simultaneously.',
              'heading': 'Changes of State'},
             {'content': 'STATE SYMBOLS are added after formulas in chemical equations to show the physical state of '
                         'each substance:\n'
                         '\n'
                         '(s) — SOLID\n'
                         '(l) — LIQUID\n'
                         '(g) — GAS\n'
                         '(aq) — AQUEOUS SOLUTION (dissolved in water)\n'
                         '\n'
                         'Examples:\n'
                         '2H₂(g) + O₂(g) → 2H₂O(l)    — hydrogen gas + oxygen gas → liquid water\n'
                         'NaCl(s) → Na⁺(aq) + Cl⁻(aq)  — solid NaCl dissolves in water\n'
                         'CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂(g)\n'
                         '\n'
                         'State symbols give useful information:\n'
                         '(aq) shows a substance is dissolved in water — important for reactions in solution.\n'
                         '(g) shows a gas is produced — important if testing for hydrogen, CO₂ etc.\n'
                         'They make equations more informative and precise.',
              'heading': 'State Symbols in Chemical Equations'}],
  'title': 'States of Matter and State Symbols',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Ionic compounds conduct in solution because the IONS move — NOT because electrons move. This is '
                    'IONIC conduction (different from ELECTRONIC conduction in metals). Also: ionic compounds are '
                    'brittle, not ductile. They crack when struck because shifting layers brings like charges together '
                    '→ repulsion → shattering.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'properties-ionic-compounds',
  'key_note': 'Giant ionic lattice → high MP/BP (strong electrostatic forces). Brittle (layer shift → repulsion → '
              'shatters). Solid: no conduction. Molten/dissolved: conducts (mobile ions). Higher ionic charge → '
              'stronger forces → higher MP. Many dissolve in water.',
  'matching': {'instruction': 'Sort each property into ionic compound or metal.',
               'pairs': [('Ionic compound',
                          'Brittle — shatters when struck due to repulsion between like-charged ions'),
                         ('Metal', 'Malleable — layers of ions can slide without breaking the metallic bond'),
                         ('Ionic compound', 'Conducts electricity when molten but not when solid'),
                         ('Metal', 'Conducts electricity in solid state — delocalised electrons carry charge'),
                         ('Both', 'High melting points — strong electrostatic forces throughout the structure')],
               'title': 'Ionic vs Metallic Properties'},
  'quiz': [{'opts': [('Mg²⁺ and O²⁻ have higher charges (±2) than Na⁺ and Cl⁻ (±1) — stronger electrostatic forces '
                      'between ions',
                      True),
                     ('MgO has a larger crystal lattice, so more bonds must be broken', False),
                     ('MgO contains more ions per formula unit than NaCl', False),
                     ('Magnesium is a heavier element than sodium — this increases the melting point', False)],
            'q': 'Magnesium oxide (MgO) has a higher melting point than sodium chloride (NaCl). Why?',
            'wrong_explanations': {1: 'Crystal size is not the determining factor — both have giant lattices. The '
                                      'STRENGTH of individual ion-ion attractions matters.',
                                   2: 'Both NaCl and MgO have a 1:1 ratio of ions in their formula — neither has more '
                                      'ions per formula unit.',
                                   3: 'Atomic mass does not determine melting point — the CHARGE on the ions '
                                      'determines the strength of electrostatic forces.'}},
           {'opts': [('Dissolved in water and molten — ions are free to move in both cases', True),
                     ('Only in solid form — the lattice provides a pathway for electrons', False),
                     ('In all forms — NaCl always has ions present that can carry charge', False),
                     ('Only when dissolved — the water provides the conducting pathway', False)],
            'q': 'A student tests whether NaCl conducts electricity in four forms: solid, dissolved in water, molten, '
                 'and as a gas. In which forms does it conduct?',
            'wrong_explanations': {1: 'Solid NaCl has ions but they are FIXED — they cannot move to carry charge.',
                                   2: 'Ions present does NOT mean they can conduct — they must be FREE TO MOVE. In a '
                                      'solid, they are fixed in the lattice.',
                                   3: 'Molten NaCl also conducts — water is not needed. Free ions (whether from '
                                      'melting or dissolving) allow conduction.'}}],
  'rp': None,
  'spec': '5.2.2.3',
  'summary': 'Explain the properties of ionic compounds in terms of their giant lattice structure.',
  'theory': [{'content': 'Ionic compounds have a GIANT IONIC LATTICE structure:\n'
                         'Regular 3D arrangement of alternating positive and negative ions.\n'
                         'Strong electrostatic forces acting in ALL DIRECTIONS between oppositely charged ions.\n'
                         'This structure extends throughout the entire crystal — billions of ions held together.\n'
                         '\n'
                         'The FORMULA of an ionic compound shows the SIMPLEST RATIO of ions — not the actual number in '
                         'a formula unit.\n'
                         'NaCl: 1 Na⁺ for every 1 Cl⁻.\n'
                         'MgO: 1 Mg²⁺ for every 1 O²⁻.\n'
                         'CaCl₂: 1 Ca²⁺ for every 2 Cl⁻.\n'
                         '\n'
                         'The lattice structure explains ALL properties.',
              'heading': 'Reviewing the Giant Ionic Lattice'},
             {'content': 'HIGH MELTING AND BOILING POINTS:\n'
                         'Many strong electrostatic bonds throughout the lattice.\n'
                         'Very large amounts of energy needed to separate the ions.\n'
                         'Example: NaCl melts at 801°C. MgO (higher charged ions) melts at 2852°C.\n'
                         'Higher ionic charges → stronger forces → higher melting point.\n'
                         '\n'
                         'BRITTLENESS:\n'
                         'Ionic compounds are HARD but BRITTLE.\n'
                         'When a force is applied, layers of ions shift by one position.\n'
                         'Like-charged ions end up aligned → strong REPULSION → crystal cracks/shatters.\n'
                         'Cannot bend without breaking — unlike metals.\n'
                         '\n'
                         'ELECTRICAL CONDUCTIVITY:\n'
                         'SOLID: Does NOT conduct — ions are in fixed positions in the lattice, cannot move.\n'
                         'MOLTEN (liquid): DOES conduct — ions are free to move and carry charge.\n'
                         'DISSOLVED in water: DOES conduct — ions separate and can move through the solution.\n'
                         '\n'
                         'SOLUBILITY:\n'
                         'Many ionic compounds dissolve in WATER — polar water molecules attract and surround the '
                         'ions, pulling them from the lattice.\n'
                         'Not all are soluble — depends on the strength of ion-ion forces vs. ion-water forces.',
              'heading': 'Full Property Explanation'},
             {'content': 'The CHARGE on the ions affects the strength of the electrostatic forces:\n'
                         '\n'
                         'Higher charge → stronger attraction → higher melting point → higher electrical conductivity '
                         'when molten.\n'
                         '\n'
                         'Comparison:\n'
                         'NaCl (Na⁺ and Cl⁻ — charges of ±1): melting point 801°C.\n'
                         'MgO (Mg²⁺ and O²⁻ — charges of ±2): melting point 2852°C.\n'
                         '\n'
                         'MgO has MUCH stronger ionic bonds because both ions have double the charge — the '
                         'electrostatic force is proportional to the product of the charges.\n'
                         '\n'
                         'This also means more energy is released when MgO forms — MgO is a more stable compound.\n'
                         '\n'
                         'This concept helps explain why Group 2 compounds often have higher melting points than Group '
                         '1 compounds.',
              'heading': 'Comparing Ionic Compounds — Effect of Charge'}],
  'title': 'Structure and Properties of Ionic Compounds',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Simple molecular substances have LOW melting points because INTERMOLECULAR FORCES between '
                    'molecules are weak — NOT because covalent bonds are weak. The covalent bonds WITHIN molecules are '
                    'actually very strong. The confusion between these two types of force is one of the most common '
                    'errors in this topic.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'properties-small-molecules',
  'key_note': 'Simple molecules: small, discrete, strong covalent bonds within. Low MP/BP because WEAK intermolecular '
              'forces between molecules. Larger molecules → stronger intermolecular forces → higher MP/BP. No '
              'electrical conduction (no free electrons or ions). Melting/boiling separates molecules — does NOT break '
              'covalent bonds.',
  'matching': {'instruction': 'Sort each property into simple molecular substance or giant structure.',
               'pairs': [('Simple molecular',
                          'Low melting point — weak intermolecular forces between molecules overcome easily'),
                         ('Giant structure',
                          'Very high melting point — many strong bonds throughout the entire structure'),
                         ('Simple molecular', 'Often gases or liquids at room temperature'),
                         ('Simple molecular', 'Does not conduct electricity — no free ions or electrons'),
                         ('Giant structure (ionic)', 'Conducts when molten or dissolved — free ions carry charge')],
               'title': 'Simple Molecular vs Giant Structure'},
  'quiz': [{'opts': [('Water molecules form stronger intermolecular forces (hydrogen bonds) than methane — more energy '
                      'needed to separate water molecules',
                      True),
                     ('Water has more covalent bonds — it takes more energy to break them', False),
                     ('Methane is lighter and therefore evaporates faster', False),
                     ('Water contains oxygen, which makes molecules heavier and harder to separate', False)],
            'q': 'Water (H₂O) boils at 100°C, but methane (CH₄) boils at −161°C. Both are simple molecular substances. '
                 'Why is the difference so large?',
            'wrong_explanations': {1: 'Boiling does NOT break covalent bonds — water has 2 covalent bonds, methane has '
                                      '4. Bond count is not the reason.',
                                   2: 'Lighter molecules do evaporate faster at a given temperature, but boiling point '
                                      'is about the temperature at which intermolecular forces are overcome — not just '
                                      'molecular mass.',
                                   3: 'Oxygen does make water heavier, but the primary reason is STRONGER '
                                      'INTERMOLECULAR FORCES (hydrogen bonds) in water compared to the weaker London '
                                      'dispersion forces in methane.'}},
           {'opts': [('They have no free electrons or ions — there are no charged particles that can move to carry a '
                      'current',
                      True),
                     ('The covalent bonds are too strong to allow electron movement', False),
                     ('The molecules are too small to carry a useful electrical charge', False),
                     ("Simple molecules are always gases, and gases don't conduct electricity", False)],
            'q': 'Why do simple molecular substances not conduct electricity?',
            'wrong_explanations': {1: 'Electrical conduction depends on FREE MOVING charged particles — not on bond '
                                      'strength. Even if bonds were weaker, without free charges there would be no '
                                      'conductivity.',
                                   2: "Molecular size doesn't determine conductivity — metals are much larger "
                                      'structures but conduct excellently because of free electrons.',
                                   3: 'Some gases DO conduct electricity (e.g. plasma, ionised gas) — and simple '
                                      'molecular substances can be solids or liquids too.'}}],
  'rp': None,
  'spec': '5.2.2.4',
  'summary': 'Explain why simple molecular substances have low melting points and do not conduct electricity.',
  'theory': [{'content': 'SIMPLE MOLECULAR SUBSTANCES are made of small, discrete molecules — each molecule contains a '
                         'fixed number of atoms joined by STRONG COVALENT BONDS.\n'
                         '\n'
                         'Examples:\n'
                         'Water (H₂O) — 3 atoms per molecule.\n'
                         'Carbon dioxide (CO₂) — 3 atoms per molecule.\n'
                         'Methane (CH₄) — 5 atoms per molecule.\n'
                         'Hydrogen (H₂) — 2 atoms per molecule.\n'
                         'Ammonia (NH₃) — 4 atoms per molecule.\n'
                         'Oxygen (O₂), nitrogen (N₂), chlorine (Cl₂) — all diatomic.\n'
                         '\n'
                         'The COVALENT BONDS within each molecule are STRONG — but this is NOT what determines '
                         'melting/boiling point.',
              'heading': 'Simple Molecular Structures'},
             {'content': 'The KEY to understanding simple molecular properties:\n'
                         '\n'
                         'There are TWO types of forces to consider:\n'
                         '\n'
                         '1. COVALENT BONDS — within each molecule, between atoms. These are STRONG.\n'
                         '2. INTERMOLECULAR FORCES — between separate molecules. These are WEAK.\n'
                         '\n'
                         'When a simple molecular substance melts or boils:\n'
                         'The INTERMOLECULAR FORCES between molecules are overcome — molecules separate from each '
                         'other.\n'
                         'The COVALENT BONDS within molecules are NOT broken.\n'
                         '\n'
                         'Because intermolecular forces are WEAK, only a small amount of energy is needed → LOW '
                         'melting and boiling points.\n'
                         '\n'
                         'Examples:\n'
                         'H₂O boils at 100°C.\n'
                         'CH₄ boils at −161°C.\n'
                         'O₂ boils at −183°C.\n'
                         'Most simple molecular substances are GASES or LIQUIDS at room temperature.\n'
                         '\n'
                         'Larger molecules have more electrons → stronger intermolecular forces → higher '
                         'melting/boiling points.',
              'heading': 'Why Simple Molecular Substances Have Low Melting Points'},
             {'content': 'DO NOT CONDUCT ELECTRICITY:\n'
                         'Molecules have no overall charge.\n'
                         'There are no free electrons or ions to carry charge.\n'
                         'This applies whether solid, liquid or dissolved — unless the substance is ionic.\n'
                         '\n'
                         'SOLUBILITY:\n'
                         "'Like dissolves like' — non-polar molecules tend to dissolve in non-polar solvents; polar "
                         'molecules dissolve in polar solvents (like water).\n'
                         'Some simple molecules dissolve in water (e.g. sugar, HCl gas, CO₂).\n'
                         'Others are insoluble (e.g. iodine in water, but iodine dissolves well in hexane).\n'
                         '\n'
                         'Note: when HCl gas dissolves in water, it IONISES:\n'
                         'HCl(g) + water → H⁺(aq) + Cl⁻(aq)\n'
                         'The resulting solution (hydrochloric acid) DOES conduct electricity — because ions are '
                         'present.\n'
                         'This shows that dissolving can sometimes create ions, even from covalent molecules.',
              'heading': 'Other Properties of Simple Molecular Substances'}],
  'title': 'Structure and Properties of Small Molecules',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Polymers are LARGE MOLECULES — they are NOT giant covalent structures. Each polymer chain is one '
                    'large molecule held to others by intermolecular forces (which are weak). Giant covalent '
                    'structures (like diamond) have covalent bonds extending throughout the entire structure — very '
                    'different. This is why polymers have much lower melting points than diamond.',
  'equations': ['n CH₂=CH₂ → [—CH₂—CH₂—]ₙ  (poly(ethene))'],
  'fifas': [],
  'higher': None,
  'id': 'polymers',
  'key_note': 'Polymer: long chain of repeating monomer units. Addition polymerisation: monomers with C=C double bonds '
              'join together. Properties depend on chain length and intermolecular forces. Solid at room temperature, '
              'flexible, insulators. Thermoplastic: soften on heating. Thermosetting: permanently hard.',
  'matching': {'instruction': 'Match each polymer to its monomer and a use.',
               'pairs': [('Poly(ethene)', 'Monomer: ethene (CH₂=CH₂) — used in plastic bags and bottles'),
                         ('PVC', 'Monomer: chloroethene (CH₂=CHCl) — used in pipes and window frames'),
                         ('Nylon', 'Monomer: diamine + dicarboxylic acid — used in clothing and rope'),
                         ('Protein', 'Monomer: amino acids — biological polymer in all living things'),
                         ('Starch', 'Monomer: glucose — energy storage polymer in plants')],
               'title': 'Match the Polymer to its Monomer'},
  'quiz': [{'opts': [('Ethene — CH₂=CH₂ — the double bond opens up and monomers join together', True),
                     ('Ethane — C₂H₆ — a saturated hydrocarbon that joins together', False),
                     ('Ethanol — C₂H₅OH — an alcohol that polymerises', False),
                     ('Methane — CH₄ — the simplest hydrocarbon', False)],
            'q': 'What is the monomer used to make poly(ethene)?',
            'wrong_explanations': {1: 'Ethane is SATURATED (no double bond) — addition polymerisation requires a C=C '
                                      'double bond. Ethane cannot polymerise by addition.',
                                   2: 'Ethanol can undergo condensation reactions but does not form poly(ethene) — and '
                                      'poly(ethene) is produced by addition polymerisation.',
                                   3: 'Methane has no double bond and only 1 carbon — it cannot chain together to form '
                                      'poly(ethene).'}},
           {'opts': [('Polymers are separate large molecules — held together by weak intermolecular forces. Diamond '
                      'has strong covalent bonds throughout the entire structure.',
                      True),
                     ('Polymers contain fewer atoms than diamond — less matter to heat up', False),
                     ('Diamond has ionic bonds which are stronger than covalent bonds in polymers', False),
                     ('Polymers are synthetic — natural structures like diamond are always stronger', False)],
            'q': 'Why do polymers have lower melting points than giant covalent structures like diamond?',
            'wrong_explanations': {1: 'Polymers are LARGE molecules — a single polymer chain may contain millions of '
                                      'atoms. The issue is the TYPE of forces between chains, not the number of atoms.',
                                   2: 'Diamond is entirely COVALENT — it has no ionic bonds. The covalent bonds '
                                      'extending throughout the 3D diamond structure are what make it so hard and '
                                      'high-melting.',
                                   3: 'Both natural and synthetic structures can have high or low melting points — it '
                                      'depends on structure and bonding, not whether they are naturally occurring.'}}],
  'rp': None,
  'spec': '5.2.2.5',
  'summary': 'Describe the structure of polymers and explain their properties.',
  'theory': [{'content': 'POLYMERS are very large molecules made from many small repeating units called MONOMERS '
                         'joined together in long chains.\n'
                         '\n'
                         'The process of joining monomers is called POLYMERISATION.\n'
                         '\n'
                         'Key terminology:\n'
                         'MONOMER — small molecule that can join with others to form a polymer.\n'
                         'POLYMER — the long chain molecule formed from thousands of monomers.\n'
                         'The repeating unit in a polymer is typically written in brackets with an n outside: '
                         '[—CH₂—CH₂—]ₙ\n'
                         '\n'
                         'Examples:\n'
                         'Poly(ethene) — monomer: ethene (CH₂=CH₂) → polymer: long chain of —CH₂—CH₂— units.\n'
                         'Poly(propene) — monomer: propene.\n'
                         'PVC (polyvinyl chloride) — monomer: chloroethene.\n'
                         'Nylon — forms from two different monomers (a diamine and a dicarboxylic acid).\n'
                         'Protein — polymer of amino acid monomers.\n'
                         'DNA — polymer of nucleotide monomers.\n'
                         'Starch and cellulose — polymers of glucose monomers.',
              'heading': 'What Are Polymers?'},
             {'content': 'Polymers are SIMPLE MOLECULAR structures — they consist of individual polymer chains (very '
                         'large molecules) held together by INTERMOLECULAR FORCES.\n'
                         '\n'
                         'Properties depend on the CHAIN LENGTH and STRENGTH OF INTERMOLECULAR FORCES:\n'
                         '\n'
                         'LONG CHAIN LENGTH:\n'
                         'Longer chains have more surface area → stronger intermolecular forces → higher melting '
                         'point.\n'
                         'Very long polymers tend to be solid at room temperature.\n'
                         '\n'
                         'TYPE OF POLYMER (affects intermolecular force strength):\n'
                         'Poly(ethene) — weak forces → flexible, low melting point → used in plastic bags.\n'
                         'PVC — stronger intermolecular forces (polar C-Cl bonds) → stiffer, higher melting point.\n'
                         'Nylon — hydrogen bonds between chains → strong, high melting point.\n'
                         '\n'
                         'GENERAL POLYMER PROPERTIES:\n'
                         'Solid at room temperature (long chains, reasonable intermolecular forces).\n'
                         'Insulators — do not conduct electricity (no free electrons or ions).\n'
                         'Flexible (unless cross-linked or crystalline).\n'
                         'Low density compared to metals.\n'
                         'Can be moulded when heated — THERMOPLASTIC polymers soften when heated.\n'
                         'Some polymers are THERMOSETTING — they harden permanently when heated (cross-links form).',
              'heading': 'Properties of Polymers'},
             {'content': 'ADDITION POLYMERISATION occurs when monomers containing DOUBLE BONDS (C=C) join together.\n'
                         '\n'
                         'The double bond opens up — one bond breaks and the freed electrons form a new bond with the '
                         'next monomer.\n'
                         '\n'
                         'Example — poly(ethene):\n'
                         'Monomer: ethene CH₂=CH₂\n'
                         'Polymerisation: n CH₂=CH₂ → [—CH₂—CH₂—]ₙ\n'
                         '\n'
                         'The product is a SATURATED polymer (no double bonds remain in the chain).\n'
                         '\n'
                         'Other addition polymers:\n'
                         'Poly(propene): monomer propene (CH₂=CHCH₃)\n'
                         'PVC: monomer chloroethene (CH₂=CHCl)\n'
                         'Poly(styrene): monomer styrene (CH₂=CHC₆H₅)\n'
                         '\n'
                         'Notice: in addition polymerisation, ALL atoms of the monomer appear in the polymer — no '
                         'atoms are lost or expelled.',
              'heading': 'Addition Polymerisation'}],
  'title': 'Polymers',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'GRAPHITE conducts electricity — it is the exception to the rule that giant covalent structures '
                    "don't conduct. Diamond does NOT conduct. The difference: in graphite, each carbon uses only 3 of "
                    'its 4 outer electrons for bonds — the 4th electron is delocalised and free to move. In diamond, '
                    'all 4 electrons are used in bonds — none are free.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'giant-covalent-structures',
  'key_note': 'Giant covalent: many atoms all bonded by covalent bonds — very high MP, very hard. Diamond: each C '
              'bonds to 4 others, 3D lattice, does NOT conduct. Graphite: each C bonds to 3 others in layers, 4th '
              'electron delocalised — DOES conduct, layers slide (soft/lubricant). Both are carbon — different '
              'allotropes.',
  'matching': {'instruction': 'Sort each property into diamond or graphite.',
               'pairs': [('Diamond', 'Each carbon bonded to 4 others in a 3D tetrahedral lattice — very hard'),
                         ('Graphite', 'Each carbon bonded to 3 others in flat hexagonal sheets — layers can slide'),
                         ('Graphite', 'Conducts electricity — 4th outer electron is delocalised between layers'),
                         ('Diamond', 'Does NOT conduct electricity — all 4 outer electrons are used in bonds'),
                         ('Graphite', 'Used as pencil lead and as electrodes in electrolysis'),
                         ('Diamond', 'Used for cutting tools and as a gemstone — hardest natural substance')],
               'title': 'Diamond or Graphite?'},
  'quiz': [{'opts': [('Graphite has one delocalised electron per carbon atom — free to move and carry charge. Diamond '
                      'uses all 4 outer electrons in bonds — none are free.',
                      True),
                     ('Graphite contains more carbon atoms than diamond — more atoms means better conductivity', False),
                     ('Diamond is transparent — light passes through, but electricity cannot follow light', False),
                     ('Graphite has metallic bonding while diamond has ionic bonding', False)],
            'q': 'Why does graphite conduct electricity but diamond does not?',
            'wrong_explanations': {1: "The NUMBER of carbon atoms doesn't determine conductivity — it is the "
                                      'availability of FREE electrons that matters.',
                                   2: 'Transparency and electrical conductivity are completely unrelated properties.',
                                   3: 'Both diamond and graphite are entirely COVALENT — neither has metallic or ionic '
                                      'bonding.'}},
           {'opts': [('Graphite has layers of carbon atoms held by weak intermolecular forces — the layers can slide '
                      'over each other easily',
                      True),
                     ('Graphite is smooth because it has no atoms on its surface', False),
                     ('Graphite dissolves in water, creating a slippery solution', False),
                     ('Graphite is very hard like diamond, which makes surfaces it coats more slippery', False)],
            'q': 'Why is graphite used as a lubricant?',
            'wrong_explanations': {1: 'Surfaces always have atoms — graphite is slippery because of its LAYERED '
                                      'STRUCTURE where layers slide.',
                                   2: 'Graphite does not dissolve in water — it is used as a dry lubricant in '
                                      'situations where oil would be problematic.',
                                   3: 'Diamond is hard but NOT slippery — hardness and slipperiness are different '
                                      'properties. Graphite is SOFT, not hard.'}}],
  'rp': None,
  'spec': '5.2.2.6',
  'summary': 'Describe the structures of diamond and graphite and explain their contrasting properties.',
  'theory': [{'content': 'GIANT COVALENT STRUCTURES (also called macromolecular or network structures) are substances '
                         'where a VERY LARGE NUMBER of atoms are all joined together by COVALENT BONDS throughout the '
                         'entire structure.\n'
                         '\n'
                         'Unlike simple molecules (discrete, small), giant covalent structures have no individual '
                         'molecules — the covalent bonding extends in all directions throughout the solid.\n'
                         '\n'
                         'Because the structure consists entirely of strong covalent bonds:\n'
                         'VERY HIGH melting and boiling points (must break many strong covalent bonds).\n'
                         'Very HARD — rigid structure.\n'
                         'Generally do NOT conduct electricity (no free electrons or ions).\n'
                         '\n'
                         'Examples of giant covalent structures:\n'
                         'Diamond (carbon)\n'
                         'Graphite (carbon)\n'
                         'Silicon dioxide (SiO₂) — quartz/sand',
              'heading': 'What Are Giant Covalent Structures?'},
             {'content': 'DIAMOND is a form (allotrope) of CARBON.\n'
                         '\n'
                         'Structure:\n'
                         'Each carbon atom is bonded to FOUR other carbon atoms — in a TETRAHEDRAL arrangement.\n'
                         'Every carbon uses all 4 outer electrons for bonding.\n'
                         'The result is an extremely strong, rigid 3D lattice of covalent bonds.\n'
                         'No free electrons — all electrons are in bonds.\n'
                         '\n'
                         'Properties and explanations:\n'
                         'VERY HIGH MELTING POINT: must break many strong C-C covalent bonds throughout the lattice.\n'
                         'VERY HARD — hardest natural substance on Earth: rigid 3D lattice, all atoms held firmly in '
                         'all directions.\n'
                         'DOES NOT CONDUCT ELECTRICITY: all 4 outer electrons are used in covalent bonds — no free '
                         'electrons to carry charge.\n'
                         'TRANSPARENT: interacts uniquely with light due to its bonding structure.\n'
                         '\n'
                         'USES: cutting tools (drill bits, saw blades), gemstones (jewellery), abrasives.',
              'heading': 'Diamond'},
             {'content': 'GRAPHITE is another allotrope of CARBON — same element, completely different structure and '
                         'properties.\n'
                         '\n'
                         'Structure:\n'
                         'Each carbon atom is bonded to THREE other carbon atoms — forming flat HEXAGONAL RINGS.\n'
                         'These hexagons form large flat SHEETS (layers).\n'
                         'The layers are held together only by WEAK intermolecular forces — they can slide over each '
                         'other.\n'
                         'The FOURTH outer electron from each carbon is NOT used in bonding — these electrons are '
                         'DELOCALISED between the layers.\n'
                         '\n'
                         'Properties and explanations:\n'
                         'HIGH MELTING POINT: strong covalent bonds within each layer must be broken.\n'
                         'SLIPPERY / SOFT: layers can slide over each other easily (weak forces between layers).\n'
                         'CONDUCTS ELECTRICITY: delocalised electrons between layers are free to move and carry '
                         'charge.\n'
                         'GREY/BLACK and OPAQUE: absorbs light.\n'
                         '\n'
                         'USES: pencil leads (layers slide off onto paper), lubricants, electrodes in electrolysis '
                         '(conducts, unreactive), electrical contacts.',
              'heading': 'Graphite'}],
  'title': 'Giant Covalent Structures',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Metals conduct electricity in the SOLID state — unlike ionic compounds which only conduct when '
                    'molten or dissolved. This is because metallic conduction uses DELOCALISED ELECTRONS (which are '
                    'already free to move in the solid), whereas ionic conduction requires ions to move (which they '
                    "can't do when fixed in a solid lattice).",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'metals-alloys',
  'key_note': 'Metallic structure: positive ions + delocalised electrons. High MP/BP, malleable, ductile (layers '
              'slide). Conducts electricity AND heat in solid state (delocalised electrons). Alloys: different-sized '
              'atoms disrupt regular lattice → harder. Steel, bronze, brass are key examples.',
  'matching': {'instruction': 'Match each substance to its key property and use.',
               'pairs': [('Copper', 'Best common electrical conductor — used in wiring and circuits'),
                         ('Steel', 'Iron + carbon — harder than pure iron — used in construction and tools'),
                         ('Bronze', 'Copper + tin — harder than pure copper — used in bearings and statues'),
                         ('Aluminium alloys', 'Lightweight and strong — used in aircraft construction'),
                         ('Stainless steel',
                          'Iron + chromium + nickel — resists corrosion — used in cutlery and surgical instruments')],
               'title': 'Metal or Alloy — Property Match'},
  'quiz': [{'opts': [('Metals have delocalised electrons that are free to move even when solid. Ionic solids have ions '
                      'fixed in the lattice — they cannot move.',
                      True),
                     ('Metal atoms are smaller than ions, so they move more easily through the solid', False),
                     ('Metals have more protons, making them better at conducting positive charge', False),
                     ('Ionic compounds have stronger bonds that prevent any particle movement', False)],
            'q': 'Why can metals conduct electricity in the solid state, but ionic compounds cannot?',
            'wrong_explanations': {1: "Atomic size doesn't determine conductivity — it's the AVAILABILITY OF FREE "
                                      'CHARGE CARRIERS that matters.',
                                   2: "Proton count doesn't determine conductivity — non-metals can have many protons "
                                      'but are poor conductors.',
                                   3: 'Ionic bonds are strong — but ionic compounds CAN conduct when MELTED (ions '
                                      'become free). The issue in solids is that ions are FIXED, not that bonds are '
                                      'stronger.'}},
           {'opts': [('Zinc atoms are a different size to copper atoms — they disrupt the regular lattice and prevent '
                      'layers from sliding',
                      True),
                     ('Brass has more metallic bonds than copper — more bonds means harder', False),
                     ('Zinc is a harder metal than copper, so mixing them gives a harder product', False),
                     ('Brass has a different crystal structure that is always harder than face-centred cubic', False)],
            'q': 'Why is brass (copper + zinc) harder than pure copper?',
            'wrong_explanations': {1: "More bonds doesn't necessarily mean harder — the mechanism is LATTICE "
                                      'DISRUPTION preventing layer sliding.',
                                   2: 'Zinc alone is harder than pure copper, but the hardening in brass comes '
                                      'specifically from DISRUPTING the regular copper lattice with differently-sized '
                                      'zinc atoms.',
                                   3: 'Crystal structure does change in alloys — but the explanation at GCSE level '
                                      'focuses on differently-sized atoms disrupting lattice planes.'}}],
  'rp': None,
  'spec': '5.2.2.7–5.2.2.8',
  'summary': 'Explain the properties of metals and alloys in terms of metallic bonding and structure.',
  'theory': [{'content': 'METALS have GIANT METALLIC STRUCTURES — a regular lattice of positive metal ions surrounded '
                         'by a sea of delocalised electrons.\n'
                         '\n'
                         'This gives metals their characteristic properties:\n'
                         '\n'
                         'HIGH MELTING AND BOILING POINTS:\n'
                         'Strong electrostatic forces between positive ions and the electron sea throughout the '
                         'lattice.\n'
                         'Large amounts of energy needed to break these forces.\n'
                         '(Exceptions: mercury −39°C and gallium 30°C are liquids at or near room temperature.)\n'
                         '\n'
                         'MALLEABLE — can be hammered into shapes:\n'
                         'Layers of ions can slide over each other — the electron sea re-accommodates ions in new '
                         'positions.\n'
                         'No direction-specific bonds that would snap when layers move.\n'
                         '\n'
                         'DUCTILE — can be drawn into wires:\n'
                         'Same reason as malleability — ions can slide into new positions without breaking the '
                         'structure.\n'
                         '\n'
                         'HIGH DENSITY — most metals are dense:\n'
                         'Close-packed lattice of heavy atoms.',
              'heading': 'Metals as Giant Metallic Structures'},
             {'content': 'Metals are the BEST conductors of electricity and heat among common materials.\n'
                         '\n'
                         'ELECTRICAL CONDUCTIVITY:\n'
                         'Delocalised electrons can move freely through the metallic lattice.\n'
                         'When a VOLTAGE is applied, electrons drift in a specific direction → electric current.\n'
                         'This works in SOLID state — electrons can move even in a solid lattice.\n'
                         'Examples: copper (best common conductor), aluminium, iron, silver.\n'
                         '\n'
                         'THERMAL CONDUCTIVITY:\n'
                         'Delocalised electrons also transfer kinetic (heat) energy rapidly through the structure.\n'
                         'Thermal energy is passed from hot regions to cool regions by electron movement.\n'
                         'This makes metals excellent heat conductors.\n'
                         'Examples: copper for cooking pans, aluminium for heat sinks in electronics.\n'
                         '\n'
                         'This is why BOTH electrical and thermal conductivity improve together in metals — both rely '
                         'on the same delocalised electron sea.',
              'heading': 'Metals as Electrical and Thermal Conductors'},
             {'content': 'ALLOYS are MIXTURES containing a metal and one or more other elements (often another metal '
                         'or carbon).\n'
                         '\n'
                         'Why alloys form:\n'
                         'Pure metals are often too SOFT for practical use.\n'
                         'Adding a different element disrupts the regular lattice — making it HARDER.\n'
                         '\n'
                         'How alloys work:\n'
                         'In a PURE METAL, all ions are the same size — layers can slide easily → soft.\n'
                         'In an ALLOY, DIFFERENT SIZED atoms are inserted into the lattice.\n'
                         'They distort the regular pattern → layers CANNOT slide as easily → harder and stronger.\n'
                         '\n'
                         'Key alloys and their applications:\n'
                         'STEEL (iron + 0.1–2% carbon): much harder than iron → construction, tools, vehicles, '
                         'bridges.\n'
                         'STAINLESS STEEL (iron + chromium + nickel): resists corrosion → cutlery, surgical '
                         'instruments.\n'
                         'BRONZE (copper + tin): harder than copper → ship propellers, statues, bearings.\n'
                         'BRASS (copper + zinc): golden appearance, harder than copper → musical instruments, taps.\n'
                         'ALUMINIUM ALLOYS (+ copper, magnesium etc.): strong and lightweight → aircraft, spacecraft.',
              'heading': 'Alloys'}],
  'title': 'Properties of Metals and Alloys',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Nanoparticles are NOT the same as atoms or small molecules — they contain hundreds to thousands '
                    'of atoms. The key reason nanoparticles have different properties is their enormous SURFACE AREA '
                    'TO VOLUME RATIO — a much greater fraction of their atoms are on the surface, making them much '
                    'more reactive than the same material in bulk form.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'nanoparticles',
  'key_note': 'Nanoparticles: 1–100 nm. Huge surface area to volume ratio → different properties, higher reactivity. '
              'Graphene: single layer of graphite, strong, conducts. Fullerenes (C₆₀): hollow carbon spheres, drug '
              'delivery. Nanotubes: rolled graphene, strong conductors. Risks: may penetrate cells, unknown long-term '
              'effects.',
  'matching': {'instruction': 'Match each nanostructure to its description and use.',
               'pairs': [('Graphene',
                          'Single layer of graphite hexagons — extremely strong, conducts electricity, potential use '
                          'in flexible electronics'),
                         ('Buckminsterfullerene (C₆₀)',
                          '60 carbon atoms in a hollow sphere — used in drug delivery and as a lubricant'),
                         ('Carbon nanotube',
                          'Rolled graphene sheet forming a hollow tube — very strong, conducts electricity'),
                         ('Silver nanoparticles',
                          'Very high surface area → highly antibacterial — used in wound dressings'),
                         ('TiO₂ nanoparticles',
                          'Transparent at nanoscale — used in sunscreen to absorb UV without leaving white marks')],
               'title': 'Match the Carbon Nanostructure'},
  'quiz': [{'opts': [('Nanoparticles have a much larger surface area to volume ratio — a greater proportion of atoms '
                      'are on the surface and available for reactions',
                      True),
                     ('Nanoparticles are made of different atoms than bulk materials', False),
                     ('Nanoparticles have weaker chemical bonds than bulk materials', False),
                     ('Nanoparticles are always more stable than bulk materials', False)],
            'q': 'Why do nanoparticles have different properties from the same material in bulk form?',
            'wrong_explanations': {1: 'Nanoparticles ARE made of the same atoms — gold nanoparticles contain gold '
                                      'atoms, just as bulk gold does. It is the SCALE that changes properties.',
                                   2: 'The chemical bonds in nanoparticles are the same type as in bulk materials — it '
                                      'is the fraction of surface atoms that differs.',
                                   3: 'Nanoparticles are often MORE reactive than bulk materials — which can mean LESS '
                                      "stable in some contexts. Their behaviour is more complex than 'always more "
                                      "stable'."}},
           {'opts': [('Their small size allows them to penetrate cell membranes, enter cells and potentially cause '
                      'biological damage — and their long-term effects are not yet fully understood',
                      True),
                     ('Nanoparticles are more toxic because they contain more of the harmful material', False),
                     ('Nanoparticles are heavier and stay in the lungs longer than larger particles', False),
                     ('Nanoparticles react with water in the body to produce dangerous chemicals', False)],
            'q': 'Why might nanoparticles pose a greater health risk than the same material in larger particle form?',
            'wrong_explanations': {1: 'Nanoparticles contain LESS material than larger particles of the same substance '
                                      '— but their small size and high reactivity are the concern, not quantity.',
                                   2: 'Nanoparticles are actually LIGHTER than larger particles — the concern is their '
                                      'small size allowing penetration into biological systems.',
                                   3: 'Some nanoparticles may react with biological molecules — but the primary '
                                      'concern is their ability to penetrate cell membranes due to their tiny size.'}}],
  'rp': None,
  'spec': '5.2.3.3',
  'summary': 'Describe nanoparticles and fullerenes, their properties and uses, and potential risks.',
  'theory': [{'content': 'NANOPARTICLES are particles with dimensions in the range of 1 to 100 NANOMETRES (nm).\n'
                         '\n'
                         '1 nm = 1 × 10⁻⁹ m\n'
                         '\n'
                         'Nanoparticles contain a few hundred to a few thousand atoms — much smaller than bulk '
                         'materials, but larger than individual atoms or molecules.\n'
                         '\n'
                         'At this tiny scale, materials can have VERY DIFFERENT properties compared to the same '
                         'material in bulk (large) form. For example:\n'
                         'Gold in bulk: yellow, does not react with most chemicals, melts at 1064°C.\n'
                         'Gold nanoparticles: red/purple colour, much higher reactivity, much lower melting point.\n'
                         '\n'
                         'This is because nanoparticles have an enormous SURFACE AREA TO VOLUME RATIO compared to bulk '
                         'material — a much greater proportion of atoms are on the surface and available for '
                         'reactions.\n'
                         '\n'
                         'Larger surface area → higher reactivity, faster catalyst action, different optical '
                         'properties.',
              'heading': 'What Are Nanoparticles?'},
             {'content': 'GRAPHENE:\n'
                         'A SINGLE LAYER of graphite — a flat sheet of carbon atoms arranged in a hexagonal lattice, '
                         'just ONE ATOM THICK.\n'
                         'Properties:\n'
                         'Extremely strong (one of the strongest materials ever tested).\n'
                         'Very lightweight — just one atom thick.\n'
                         'Excellent electrical conductor — delocalised electrons (as in graphite).\n'
                         'Almost transparent.\n'
                         'Potential uses: flexible electronics, touchscreens, ultralight composite materials, medical '
                         'sensors.\n'
                         '\n'
                         'FULLERENES:\n'
                         'Carbon molecules where atoms form hollow SPHERES, TUBES or other shapes.\n'
                         "BUCKMINSTERFULLERENE (C₆₀) — also called 'buckyballs':\n"
                         '60 carbon atoms arranged in a sphere (like a football — hexagons and pentagons).\n'
                         'Hollow structure.\n'
                         'Fairly stable, can enclose other atoms or molecules inside the cage.\n'
                         'Uses: drug delivery (molecules placed inside for targeted medicine), lubricants, catalysis.\n'
                         '\n'
                         'CARBON NANOTUBES:\n'
                         'Rolled-up sheets of graphene forming hollow cylindrical tubes.\n'
                         'Very strong and stiff along the tube axis.\n'
                         'Excellent electrical conductors (delocalised electrons).\n'
                         'Uses: reinforcing composite materials, electronics, future nanotechnology.',
              'heading': 'Carbon Nanostructures — Graphene and Fullerenes'},
             {'content': 'USES OF NANOPARTICLES:\n'
                         'SUNSCREEN: Titanium dioxide (TiO₂) nanoparticles — transparent (unlike bulk TiO₂ which is '
                         'white) but still absorb UV radiation effectively.\n'
                         'ANTIBACTERIAL products: Silver nanoparticles — high surface area → high reactivity against '
                         'bacteria. Used in wound dressings, socks, food packaging.\n'
                         'CATALYSIS: High surface area makes nanoparticles extremely effective catalysts.\n'
                         'DRUG DELIVERY: Nanoparticles can carry drugs directly to target cells (e.g. tumour cells).\n'
                         'COATINGS: Self-cleaning glass, water-repelling fabrics.\n'
                         'ELECTRONICS: Used in transistors, sensors, LEDs.\n'
                         '\n'
                         'POTENTIAL RISKS:\n'
                         'Nanoparticles are so small they can:\n'
                         'Pass through cell membranes — may cause unknown biological effects.\n'
                         'Be inhaled into the lungs and bypass normal defence mechanisms.\n'
                         'Persist in the environment — may accumulate in food chains.\n'
                         'Interact unexpectedly with biological systems — long-term effects not fully understood.\n'
                         '\n'
                         'The same properties that make nanoparticles useful (small size, high reactivity, ability to '
                         'penetrate membranes) also make them potentially hazardous.\n'
                         '\n'
                         'More research is needed to fully understand the health and environmental impacts — this is '
                         'an area of active scientific investigation.',
              'heading': 'Uses and Risks of Nanoparticles'}],
  'title': 'Nanoparticles',
  'triple_only': None,
  'variables': []}],

"quantitative": [{'common_mistake': 'Never change the SUBSCRIPT numbers in a formula when balancing — only add or change the large '
                    'numbers (coefficients) IN FRONT of formulas. Changing H₂O to H₂O₂ would create a different '
                    'compound (hydrogen peroxide, not water). Always balance by adjusting coefficients only.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'conservation-of-mass',
  'key_note': 'Conservation of mass: atoms are rearranged, never created or destroyed → total mass reactants = total '
              'mass products. Balance equations by adjusting coefficients only — never change chemical formulae. Check '
              'all atoms balance on both sides.',
  'matching': {'instruction': 'Match each unbalanced equation to the correct balanced version.',
               'pairs': [('Na + Cl₂ → NaCl', '2Na + Cl₂ → 2NaCl (need 2 Na to balance the 2 Cl)'),
                         ('H₂ + O₂ → H₂O', '2H₂ + O₂ → 2H₂O (need 2 H₂ and 2 H₂O to balance all atoms)'),
                         ('Fe + O₂ → Fe₂O₃', '4Fe + 3O₂ → 2Fe₂O₃ (4 Fe and 6 O each side)'),
                         ('Ca + H₂O → Ca(OH)₂ + H₂', 'Ca + 2H₂O → Ca(OH)₂ + H₂ (need 2 water molecules)')],
               'title': 'Balance these Equations'},
  'quiz': [{'opts': [('Atoms cannot be created or destroyed — the same atoms must appear on both sides of the equation',
                      True),
                     ('Balanced equations are easier to read and understand', False),
                     ('Unbalanced equations produce different products', False),
                     ('Equations must be balanced to follow international chemical naming rules', False)],
            'q': 'Why must chemical equations be balanced?',
            'wrong_explanations': {1: 'Readability is a benefit but not the fundamental reason — conservation of mass '
                                      'is.',
                                   2: 'An unbalanced equation can still show the correct reactants and products — it '
                                      "just doesn't correctly represent the quantitative relationship between them.",
                                   3: 'Balancing is a scientific law requirement (conservation of mass), not a naming '
                                      'convention.'}},
           {'opts': [('16 g — conservation of mass: mass of O₂ = 40 − 24 = 16 g', True),
                     ('40 g — the oxygen has the same mass as the product', False),
                     ('64 g — double the mass of magnesium', False),
                     ('Cannot be determined without the balanced equation', False)],
            'q': '24 g of magnesium reacts completely with oxygen to form magnesium oxide. 40 g of magnesium oxide is '
                 'produced. How much oxygen reacted?',
            'wrong_explanations': {1: 'Mass in = mass out. If 40 g MgO is made from 24 g Mg, the remaining 40 − 24 = '
                                      '16 g must have come from oxygen.',
                                   2: 'The mass of oxygen is only part of the product mass — the product contains both '
                                      'magnesium AND oxygen.',
                                   3: 'Conservation of mass allows this calculation: mass O₂ = mass product − mass Mg '
                                      '= 40 − 24 = 16 g.'}},
           {'opts': [('4Fe + 3O₂ → 2Fe₂O₃', True),
                     ('Fe + O₂ → Fe₂O₃', False),
                     ('2Fe + O₂ → Fe₂O₃', False),
                     ('Fe + 3O₂ → 2Fe₂O₃', False)],
            'q': 'Which of these is a correctly balanced equation?',
            'wrong_explanations': {1: 'Fe + O₂ → Fe₂O₃: left has 1 Fe, 2 O; right has 2 Fe, 3 O — not balanced.',
                                   2: '2Fe + O₂ → Fe₂O₃: left has 2 Fe, 2 O; right has 2 Fe, 3 O — oxygen not '
                                      'balanced.',
                                   3: 'Fe + 3O₂ → 2Fe₂O₃: left has 1 Fe, 6 O; right has 4 Fe, 6 O — iron not '
                                      'balanced.'}}],
  'rp': None,
  'spec': '5.3.1.1',
  'summary': 'Explain the law of conservation of mass and balance symbol equations.',
  'theory': [{'content': 'The LAW OF CONSERVATION OF MASS states:\n'
                         'In a chemical reaction, the TOTAL MASS OF REACTANTS equals the TOTAL MASS OF PRODUCTS.\n'
                         '\n'
                         'Mass is always CONSERVED — it is neither created nor destroyed.\n'
                         '\n'
                         'Why? Because atoms are simply REARRANGED during a chemical reaction:\n'
                         'No atoms are gained or lost.\n'
                         'The same atoms that were in the reactants end up in the products, just in different '
                         'arrangements.\n'
                         "Since mass depends only on the number and type of atoms present, and these don't change, "
                         'total mass stays the same.\n'
                         '\n'
                         'Example:\n'
                         'Magnesium + oxygen → magnesium oxide\n'
                         '2Mg + O₂ → 2MgO\n'
                         'If 24 g of Mg reacts with 16 g of O₂ → 40 g of MgO is produced.\n'
                         '24 + 16 = 40 ✓ Mass is conserved.',
              'heading': 'The Law of Conservation of Mass'},
             {'content': 'A BALANCED equation has the same number of each type of atom on both sides — reflecting '
                         'conservation of mass.\n'
                         '\n'
                         'RULES:\n'
                         '1. Write the correct formulae for reactants and products (do NOT change formulae).\n'
                         '2. Count atoms on each side.\n'
                         '3. Add LARGE NUMBERS (coefficients) in front of formulae to balance — never change '
                         'subscripts within a formula.\n'
                         '4. Check all atoms balance.\n'
                         '\n'
                         'Example — balancing H₂ + O₂ → H₂O:\n'
                         'Left: 2H, 2O. Right: 2H, 1O. Oxygen unbalanced.\n'
                         'Add coefficient 2 in front of H₂O: H₂ + O₂ → 2H₂O\n'
                         'Left: 2H, 2O. Right: 4H, 2O. Hydrogen now unbalanced.\n'
                         'Add coefficient 2 in front of H₂: 2H₂ + O₂ → 2H₂O\n'
                         'Left: 4H, 2O. Right: 4H, 2O. ✓ Balanced.\n'
                         '\n'
                         'Example — iron + oxygen → iron oxide:\n'
                         'Fe + O₂ → Fe₂O₃\n'
                         '4Fe + 3O₂ → 2Fe₂O₃ ✓\n'
                         'Left: 4Fe, 6O. Right: 4Fe, 6O. ✓',
              'heading': 'Balancing Chemical Equations'},
             {'content': 'WORD EQUATIONS name the reactants and products:\n'
                         'Magnesium + hydrochloric acid → magnesium chloride + hydrogen\n'
                         '\n'
                         'SYMBOL EQUATIONS use chemical formulae — more precise, more useful:\n'
                         'Mg + 2HCl → MgCl₂ + H₂\n'
                         '\n'
                         'Symbol equations should include STATE SYMBOLS:\n'
                         'Mg(s) + 2HCl(aq) → MgCl₂(aq) + H₂(g)\n'
                         '(s) = solid, (l) = liquid, (g) = gas, (aq) = aqueous (dissolved in water)\n'
                         '\n'
                         'IMPORTANT: The coefficients in a balanced equation tell us the RATIO in which substances '
                         'react and are produced — not the number of grams, but the number of formula units (atoms, '
                         'molecules or formula units for ionic compounds).\n'
                         '\n'
                         '2H₂ + O₂ → 2H₂O means:\n'
                         '2 molecules of H₂ react with 1 molecule of O₂ to give 2 molecules of H₂O.\n'
                         'OR: 2 moles H₂ + 1 mole O₂ → 2 moles H₂O.',
              'heading': 'Word Equations and Symbol Equations'}],
  'title': 'Conservation of Mass and Balanced Equations',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'When a formula has BRACKETS with a subscript, MULTIPLY all atoms inside the bracket by the '
                    'subscript. Ca(OH)₂ has 2 oxygen atoms and 2 hydrogen atoms — not 1 of each. Write out the count '
                    'carefully: Ca(OH)₂ = Ca + 2O + 2H = 40 + 32 + 2 = 74.',
  'equations': ['Mr = sum of all Ar values in the formula'],
  'fifas': [{'label': 'Mr Calculation — H₂SO₄',
             'question': 'Calculate the relative formula mass of sulfuric acid (H₂SO₄). Ar: H=1, S=32, O=16.',
             'steps': [('F', 'Mr = sum of all Ar values × number of atoms'),
                       ('I', 'H: 1 × 2 = 2. S: 32 × 1 = 32. O: 16 × 4 = 64'),
                       ('F', 'Mr = 2 + 32 + 64'),
                       ('A', 'Mr = 98')]}],
  'higher': None,
  'id': 'relative-formula-mass',
  'key_note': 'Mr = sum of all Ar values in the formula. Use Ar from periodic table. Brackets: multiply atoms inside '
              'by the subscript outside. Mr is used to calculate mass ratios in reactions. Mr has no units.',
  'matching': {'instruction': 'Match each formula to its correct relative formula mass.',
               'pairs': [('H₂O', 'Mr = 18 — (2 × 1) + (1 × 16)'),
                         ('CO₂', 'Mr = 44 — (1 × 12) + (2 × 16)'),
                         ('NaCl', 'Mr = 58.5 — (1 × 23) + (1 × 35.5)'),
                         ('CaCO₃', 'Mr = 100 — (1 × 40) + (1 × 12) + (3 × 16)'),
                         ('Ca(OH)₂', 'Mr = 74 — (1 × 40) + (2 × 16) + (2 × 1)')],
               'title': 'Calculate the Mr'},
  'quiz': [{'opts': [('100 — (40) + (12) + (3 × 16) = 40 + 12 + 48', True),
                     ('68 — (40) + (12) + (16) — counting only one oxygen', False),
                     ('116 — (40) + (12) + (4 × 16) — counting four oxygens', False),
                     ('52 — (40) + (12) — forgetting the oxygens', False)],
            'q': 'What is the relative formula mass of calcium carbonate (CaCO₃)? Ar: Ca=40, C=12, O=16.',
            'wrong_explanations': {1: 'CaCO₃ has only ONE oxygen — but the subscript 3 after O means THREE oxygens: 3 '
                                      '× 16 = 48.',
                                   2: 'CO₃ means 3 oxygen atoms, not 4. Only CO₄ would have 4 oxygens.',
                                   3: 'The oxygen cannot be ignored — CaCO₃ has a carbon AND three oxygens.'}},
           {'opts': [('148 — Mg(24) + 2N(28) + 6O(96)', True),
                     ('86 — Mg(24) + N(14) + 3O(48)', False),
                     ('100 — Mg(24) + 2N(28) + 3O(48)', False),
                     ('116 — Mg(24) + 2N(28) + 4O(64)', False)],
            'q': 'What is the Mr of Mg(NO₃)₂? Ar: Mg=24, N=14, O=16.',
            'wrong_explanations': {1: 'The subscript 2 outside the bracket means the entire NO₃ group is repeated '
                                      'twice. So there is 1 N, NOT 2 — wait: NO₃ has 1 N and 3 O, multiplied by 2 = 2N '
                                      'and 6O.',
                                   2: 'Mg(NO₃)₂ means 2 groups of NO₃: so 2N and 6O total. Only counting 3O ignores '
                                      'the ×2 multiplier.',
                                   3: 'Each NO₃ has 3 O; multiplied by 2 = 6 O total, not 4.'}}],
  'rp': None,
  'spec': '5.3.1.2',
  'summary': 'Calculate relative formula mass (Mr) from relative atomic masses and use it in calculations.',
  'theory': [{'content': 'The RELATIVE FORMULA MASS (Mr) of a compound is the sum of the RELATIVE ATOMIC MASSES (Ar) '
                         'of all atoms in its formula.\n'
                         '\n'
                         'Mr has no units — it is a ratio (relative to carbon-12).\n'
                         '\n'
                         'You need the Ar values from the periodic table:\n'
                         'H = 1, C = 12, N = 14, O = 16, Na = 23, Mg = 24, S = 32, Cl = 35.5, Ca = 40, Fe = 56\n'
                         '\n'
                         'EXAMPLES:\n'
                         'H₂O: (2 × 1) + (1 × 16) = 2 + 16 = 18\n'
                         'CO₂: (1 × 12) + (2 × 16) = 12 + 32 = 44\n'
                         'NaCl: (1 × 23) + (1 × 35.5) = 23 + 35.5 = 58.5\n'
                         'MgO: (1 × 24) + (1 × 16) = 24 + 16 = 40\n'
                         'H₂SO₄: (2 × 1) + (1 × 32) + (4 × 16) = 2 + 32 + 64 = 98\n'
                         'CaCO₃: (1 × 40) + (1 × 12) + (3 × 16) = 40 + 12 + 48 = 100',
              'heading': 'Relative Formula Mass (Mr)'},
             {'content': 'When a formula contains BRACKETS, multiply everything inside the brackets by the number '
                         'outside.\n'
                         '\n'
                         'Examples:\n'
                         'Ca(OH)₂:\n'
                         'Ca: 40\n'
                         'O: 16 × 2 = 32 (there are 2 OH groups, each with 1 O)\n'
                         'H: 1 × 2 = 2 (each OH group has 1 H, × 2 groups)\n'
                         'Mr = 40 + 32 + 2 = 74\n'
                         '\n'
                         'Mg(NO₃)₂:\n'
                         'Mg: 24\n'
                         'N: 14 × 2 = 28\n'
                         'O: 16 × 6 = 96 (each NO₃ has 3 O, × 2 groups)\n'
                         'Mr = 24 + 28 + 96 = 148\n'
                         '\n'
                         'Al₂(SO₄)₃:\n'
                         'Al: 27 × 2 = 54\n'
                         'S: 32 × 3 = 96\n'
                         'O: 16 × 12 = 192 (each SO₄ has 4 O, × 3 groups)\n'
                         'Mr = 54 + 96 + 192 = 342',
              'heading': 'Mr for Ionic Compounds with Brackets'},
             {'content': 'Mr allows us to calculate MASSES in reactions from a balanced equation.\n'
                         '\n'
                         'FUNDAMENTAL PRINCIPLE:\n'
                         'The RATIO of masses of reactants and products in a reaction equals the RATIO of their Mr '
                         'values (multiplied by the coefficients in the balanced equation).\n'
                         '\n'
                         'Example:\n'
                         '2Mg + O₂ → 2MgO\n'
                         'Mr: Mg = 24, O₂ = 32, MgO = 40\n'
                         'Ratio of masses: 2 × 24 : 32 : 2 × 40 = 48 : 32 : 80\n'
                         '\n'
                         'So: 48 g of Mg reacts with 32 g of O₂ to produce 80 g of MgO.\n'
                         '\n'
                         'OR: to find mass of MgO from 12 g of Mg:\n'
                         'Scale factor = 12 ÷ 48 = 0.25\n'
                         'Mass of MgO = 80 × 0.25 = 20 g\n'
                         '\n'
                         'This is the foundation for all quantitative chemistry calculations.',
              'heading': 'Using Mr in Mass Calculations'}],
  'title': 'Relative Formula Mass',
  'triple_only': None,
  'variables': [('Mr', 'Relative formula mass', '', ''), ('Ar', 'Relative atomic mass', '', '')]},
 {'common_mistake': 'When a metal burns in air, the solid GAINS mass (oxygen is added from the air to form the oxide). '
                    "Students often expect the solid to lose mass because 'burning destroys things' — but mass is "
                    'always conserved. The apparent gain is real because you are adding oxygen from the atmosphere to '
                    'the solid product.',
  'equations': [],
  'fifas': [{'label': 'Mass Change Prediction',
             'question': '4.8 g of magnesium burns completely in air: 2Mg + O₂ → 2MgO. Calculate the mass of MgO '
                         'produced. Ar: Mg=24, O=16.',
             'steps': [('F', 'Use ratio from balanced equation: 2 × Mr(Mg) : 2 × Mr(MgO) = 48 : 80'),
                       ('I', 'Scale: 4.8 g of Mg. Scale factor = 4.8 ÷ 48 = 0.1'),
                       ('F', 'Mass of MgO = 80 × 0.1 = 8.0 g'),
                       ('A', '8.0 g of MgO produced (mass increases by 3.2 g — the absorbed oxygen)')]}],
  'higher': None,
  'id': 'mass-changes-reactions',
  'key_note': 'Mass is always conserved. Apparent decrease: gas escapes (e.g. CO₂ from acid + carbonate). Apparent '
              'increase: gas absorbed from air (e.g. O₂ absorbed when Mg burns). Closed container: mass always stays '
              'the same. Look for gases when mass appears to change.',
  'matching': {'instruction': 'Predict what happens to the measured mass in each scenario.',
               'pairs': [('Mass decreases', 'CaCO₃ + HCl in an open flask — CO₂ gas escapes into the atmosphere'),
                         ('Mass increases',
                          'Magnesium burning in air — oxygen from air absorbed into MgO solid product'),
                         ('Mass stays same', 'Precipitation reaction in a sealed flask — no gas escapes or enters'),
                         ('Mass decreases', 'Zinc + sulfuric acid in an open tube — H₂ gas escapes'),
                         ('Mass stays same', 'CaCO₃ heated in a sealed tube — CO₂ trapped inside')],
               'title': 'Mass Increases, Decreases or Stays Same?'},
  'quiz': [{'opts': [('The mass decreases — CO₂ gas escapes from the open crucible', True),
                     ('The mass increases — oxygen from air is absorbed', False),
                     ('The mass stays the same — conservation of mass', False),
                     ('The mass first increases, then decreases', False)],
            'q': 'A student heats calcium carbonate in an open crucible. CaCO₃ → CaO + CO₂. What happens to the '
                 'measured mass?',
            'wrong_explanations': {1: 'Oxygen is not absorbed here — CaCO₃ is decomposing, not combusting. A gas (CO₂) '
                                      'is PRODUCED and escapes.',
                                   2: 'Conservation of mass applies to the TOTAL system. In an open container, the '
                                      'mass of the CONTAINER contents decreases because CO₂ leaves. Conservation is '
                                      'still upheld if you include the escaped CO₂.',
                                   3: 'There is no initial increase phase — CO₂ is produced and escapes from the start '
                                      'of heating.'}},
           {'opts': [('Oxygen from the air combines with the iron — the oxygen adds to the mass of the solid product '
                      '(iron oxide)',
                      True),
                     ('Water from humidity condenses on the rust — adding extra mass', False),
                     ('The iron becomes denser as it rusts — same volume but more mass', False),
                     ('Iron oxide has more atoms per formula unit than iron', False)],
            'q': 'Why does the mass of iron increase when it rusts in air?',
            'wrong_explanations': {1: 'Humidity can contribute, but the primary reason is oxygen being ABSORBED from '
                                      'the air. The reaction is 4Fe + 3O₂ → 2Fe₂O₃ — the oxygen becomes part of the '
                                      'solid.',
                                   2: 'Density changes do not increase total mass — mass = density × volume. If both '
                                      'change proportionally, mass stays the same. More mass comes from more matter '
                                      '(oxygen absorbed).',
                                   3: 'Atom count per formula unit is irrelevant — it is the MASS of oxygen absorbed '
                                      'from air that increases the total mass.'}}],
  'rp': None,
  'spec': '5.3.1.3',
  'summary': 'Explain why the measured mass sometimes appears to change in a reaction and predict mass changes.',
  'theory': [{'content': 'Conservation of mass tells us total mass never changes. Yet in some experiments, the '
                         'MEASURED mass appears to increase or decrease. This is NOT a violation of conservation of '
                         'mass — it is because a GAS enters or leaves the reaction vessel.\n'
                         '\n'
                         'WHEN MASS APPEARS TO DECREASE:\n'
                         'A GAS is PRODUCED and escapes into the atmosphere.\n'
                         'The gas molecules leave the container and are no longer weighed.\n'
                         'Example: CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂(g)\n'
                         'CO₂ gas escapes → measured mass decreases.\n'
                         'Example: Mg ribbon burning — ash (MgO) seems lighter than the ribbon, but this is because '
                         'oxygen from AIR was added. Without accounting for the oxygen, mass appears lost.\n'
                         '\n'
                         'WHEN MASS APPEARS TO INCREASE:\n'
                         'A GAS is ABSORBED or ADDED from the atmosphere.\n'
                         'Example: Magnesium burning in air:\n'
                         '2Mg(s) + O₂(g) → 2MgO(s)\n'
                         'Oxygen from the air is absorbed into the solid product → measured mass of solid INCREASES.\n'
                         'The oxygen molecules join the solid — weighed mass goes up.',
              'heading': 'When Mass Appears to Change'},
             {'content': 'You can predict mass changes using the balanced equation and Mr values.\n'
                         '\n'
                         'IF A GAS IS PRODUCED and escapes an open container:\n'
                         'Mass of container decreases by mass of gas produced.\n'
                         '\n'
                         'IF A GAS IS ABSORBED from the air:\n'
                         'Mass of solid/container increases by mass of gas absorbed.\n'
                         '\n'
                         'Example calculation:\n'
                         '2Mg + O₂ → 2MgO\n'
                         'Mr values: Mg = 24, O₂ = 32, MgO = 40\n'
                         '\n'
                         'If 4.8 g of Mg burns completely in air:\n'
                         'Moles of Mg = 4.8 ÷ 24 = 0.2 mol\n'
                         'From equation: 2 mol Mg needs 1 mol O₂, so 0.2 mol Mg needs 0.1 mol O₂\n'
                         'Mass of O₂ absorbed = 0.1 × 32 = 3.2 g\n'
                         'Mass increase = 3.2 g (the oxygen from air added to the solid)\n'
                         'Expected mass of MgO = 4.8 + 3.2 = 8.0 g\n'
                         '\n'
                         'Check: 0.2 mol MgO × 40 = 8.0 g ✓',
              'heading': 'Predicting Mass Changes'},
             {'content': 'Students sometimes observe apparent non-conservation — these all have explanations:\n'
                         '\n'
                         'PRECIPITATION REACTIONS in closed containers:\n'
                         'No gas escapes or enters → mass stays exactly the same. ✓\n'
                         '\n'
                         'HEATING A METAL IN AIR (open container):\n'
                         'Mass INCREASES — oxygen from air is absorbed.\n'
                         'If weighed in a closed container with air, mass stays constant (oxygen absorbed from sealed '
                         'air pocket).\n'
                         '\n'
                         'DECOMPOSITION reactions producing gas (e.g. CaCO₃ → CaO + CO₂):\n'
                         'In open container: mass DECREASES (CO₂ escapes).\n'
                         'In closed container: mass stays constant (CO₂ trapped).\n'
                         '\n'
                         'BURNING HYDROCARBONS in open container:\n'
                         'CO₂ and H₂O vapour escape → apparent mass decreases.\n'
                         '\n'
                         'KEY INSIGHT: If you cannot account for a mass change, look for a gas being produced or '
                         'absorbed — conservation of mass is ALWAYS upheld in the universe, even if your experiment '
                         "doesn't show it.",
              'heading': 'Non-conservation Apparent Effects'}],
  'title': 'Mass Changes in Reactions',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Read the volume from the BOTTOM of the meniscus — not the top. Water curves downward in a glass '
                    'tube, creating a concave meniscus. Reading from the top overestimates the volume. Also: zeroing '
                    'the balance (taring) before each measurement is essential — failing to do so introduces a '
                    'systematic error.',
  'equations': ['% uncertainty = (uncertainty ÷ measured value) × 100'],
  'fifas': [{'label': 'Percentage Uncertainty',
             'question': 'A student measures 25.0 cm³ of solution using a measuring cylinder with an uncertainty of '
                         '±0.5 cm³. Calculate the percentage uncertainty.',
             'steps': [('F', '% uncertainty = (uncertainty ÷ measured value) × 100'),
                       ('I', '% uncertainty = (0.5 ÷ 25.0) × 100'),
                       ('F', '% uncertainty = 0.02 × 100'),
                       ('A', '% uncertainty = 2.0%')]}],
  'higher': None,
  'id': 'chemical-measurements',
  'key_note': 'Accuracy: how close to true value. Precision: how reproducible. Burette: ±0.05 cm³ — most precise for '
              'volumes. Pipette: exact fixed volume. Read from bottom of meniscus at eye level. % uncertainty = '
              '(uncertainty ÷ measured value) × 100. Larger measurement → smaller % uncertainty.',
  'matching': {'instruction': 'Match each piece of equipment to its use and precision.',
               'pairs': [('Burette',
                          'Accurately delivers variable volumes of solution — read to ±0.05 cm³ — used in titrations'),
                         ('Pipette', 'Delivers one precise fixed volume — e.g. exactly 25.00 cm³ of solution'),
                         ('Measuring cylinder', 'Less precise volume measurement — read from bottom of meniscus'),
                         ('Digital balance', 'Measures mass precisely — typically ±0.01 g — zero before each use'),
                         ('Thermometer', 'Measures temperature — typically ±0.5°C or ±1°C')],
               'title': 'Match the Measuring Equipment'},
  'quiz': [{'opts': [('The burette — % uncertainty = (0.05 ÷ 25) × 100 = 0.2%, vs the cylinder at 4%', True),
                     ('The measuring cylinder — larger equipment is always more accurate', False),
                     ('They are the same — both deliver 25 cm³', False),
                     ('The measuring cylinder — it has a smaller absolute uncertainty', False)],
            'q': 'A student measures a volume using a burette and a measuring cylinder. The burette has an uncertainty '
                 'of ±0.05 cm³ and the cylinder ±1 cm³. Both deliver 25 cm³. Which gives the lower percentage '
                 'uncertainty?',
            'wrong_explanations': {1: "Equipment size doesn't determine accuracy — precision depends on the "
                                      'uncertainty relative to the measurement.',
                                   2: 'Both deliver the same VOLUME but with different UNCERTAINTIES — the burette '
                                      '(±0.05) is far more precise than the measuring cylinder (±1).',
                                   3: 'The measuring cylinder has a LARGER absolute uncertainty (±1 cm³ vs ±0.05 cm³) '
                                      '— it is LESS precise, not more.'}},
           {'opts': [('From the bottom of the meniscus — water curves downward, creating a concave surface', True),
                     ('From the top of the meniscus — this gives the largest volume reading', False),
                     ('From the middle of the meniscus — splitting the difference', False),
                     ("It doesn't matter — the meniscus reading is always correct", False)],
            'q': 'When reading a burette or measuring cylinder containing water, where should you read the volume?',
            'wrong_explanations': {1: 'Reading from the TOP of the meniscus gives an overestimate — the markings are '
                                      'calibrated for the bottom of the meniscus.',
                                   2: 'Reading from the middle introduces error — always read from the BOTTOM '
                                      'consistently to match calibration.',
                                   3: 'Reading from the wrong part of the meniscus introduces a systematic error — it '
                                      'DOES matter and affects accuracy.'}}],
  'rp': None,
  'spec': '5.3.1.4',
  'summary': 'Describe the importance of precise measurements in chemistry and sources of uncertainty.',
  'theory': [{'content': 'Quantitative chemistry relies on PRECISE and ACCURATE measurements.\n'
                         '\n'
                         'ACCURACY — how close a measurement is to the TRUE value.\n'
                         'PRECISION — how reproducible/consistent measurements are (close to each other).\n'
                         '\n'
                         'A measurement can be precise but not accurate (consistently wrong), or accurate but not '
                         'precise (correct on average but variable).\n'
                         '\n'
                         'In chemistry, measurements include:\n'
                         'MASSES — measured using a balance (in grams, g).\n'
                         'VOLUMES of solutions — measured using a burette, pipette or measuring cylinder (in cm³ or '
                         'dm³).\n'
                         'TEMPERATURES — measured using a thermometer (in °C).\n'
                         'TIMES — measured using a stopwatch (in seconds).\n'
                         '\n'
                         'Units matter enormously:\n'
                         '1 dm³ = 1 litre = 1000 cm³\n'
                         '1 cm³ = 0.001 dm³ = 1 mL',
              'heading': 'Why Measurements Matter in Chemistry'},
             {'content': 'Every measurement has some UNCERTAINTY — a range within which the true value lies.\n'
                         '\n'
                         'Sources of uncertainty:\n'
                         'READING ERROR — difficulty in reading exact values from scales (e.g. reading a burette '
                         'between markings).\n'
                         'SYSTEMATIC ERROR — a consistent bias in one direction (e.g. a balance not zeroed correctly, '
                         'a calibration error).\n'
                         'RANDOM ERROR — unpredictable variations that scatter measurements around the true value.\n'
                         '\n'
                         'Reduce uncertainty by:\n'
                         'Using more precise equipment (e.g. a 25 cm³ pipette is more precise than a 100 cm³ measuring '
                         'cylinder).\n'
                         'Taking REPEAT measurements and calculating a MEAN.\n'
                         'Using appropriate measuring equipment for the scale of measurement.\n'
                         '\n'
                         'Percentage uncertainty = (uncertainty ÷ measured value) × 100\n'
                         '\n'
                         'The percentage uncertainty of a small measurement is higher than that of a large measurement '
                         'with the same absolute uncertainty — this is why measuring small volumes with a large '
                         'cylinder is poor practice.',
              'heading': 'Uncertainty in Measurements'},
             {'content': 'Common measuring equipment and their precision:\n'
                         '\n'
                         'BALANCE (digital): typically ±0.01 g or ±0.001 g — high precision.\n'
                         '\n'
                         'BURETTE: 50 cm³ burette with 0.1 cm³ markings. Read to ±0.05 cm³ (between markings). Used '
                         'for accurate volume delivery in titrations.\n'
                         '\n'
                         'PIPETTE: fixed volume (e.g. exactly 25.00 cm³). Very high precision for delivering one '
                         'specific volume. Used to deliver precise volumes of solutions.\n'
                         '\n'
                         'MEASURING CYLINDER: less precise than a burette or pipette. Read from the BOTTOM of the '
                         'MENISCUS (the curved water surface).\n'
                         '\n'
                         'THERMOMETER: typically ±1°C or ±0.5°C depending on type.\n'
                         '\n'
                         'KEY SKILLS:\n'
                         'Read burettes and measuring cylinders at eye level to avoid PARALLAX ERROR.\n'
                         'Read from the BOTTOM of the meniscus for water-based solutions.\n'
                         'Zero the balance before each measurement (tare).\n'
                         'Repeat and average for reliability.',
              'heading': 'Practical Measurement Techniques'}],
  'title': 'Chemical Measurements',
  'triple_only': None,
  'variables': [('% uncertainty', 'Percentage uncertainty', '%', '')]},
 {'common_mistake': 'Volume MUST be in dm³ when using the concentration formula. If given in cm³, divide by 1000 '
                    'first. 250 cm³ = 0.250 dm³. Students frequently forget this conversion and get answers 1000 times '
                    'too large or too small.',
  'equations': ['concentration (g/dm³) = mass (g) ÷ volume (dm³)',
                'mass (g) = concentration (g/dm³) × volume (dm³)',
                'volume (dm³) = mass (g) ÷ concentration (g/dm³)'],
  'fifas': [{'label': 'Concentration Calculation',
             'question': '15 g of sodium hydroxide (NaOH) is dissolved to make 500 cm³ of solution. Calculate the '
                         'concentration in g/dm³.',
             'steps': [('F', 'concentration (g/dm³) = mass (g) ÷ volume (dm³)'),
                       ('I', 'volume = 500 cm³ ÷ 1000 = 0.5 dm³. Mass = 15 g'),
                       ('F', 'concentration = 15 ÷ 0.5'),
                       ('A', 'concentration = 30 g/dm³')]}],
  'higher': None,
  'id': 'concentration-of-solutions',
  'key_note': 'Concentration (g/dm³) = mass (g) ÷ volume (dm³). Convert cm³ to dm³: ÷ 1000. Concentrated = lots of '
              'solute per volume. Dilute = little solute per volume. Dilution: same mass, larger volume, lower '
              'concentration. c₁V₁ = c₂V₂.',
  'matching': {'instruction': 'Match each calculation to the correct answer.',
               'pairs': [('5 g NaCl in 0.5 dm³', 'Concentration = 10 g/dm³'),
                         ('20 g/dm³, volume = 250 cm³ (0.25 dm³)', 'Mass = 20 × 0.25 = 5 g'),
                         ('8 g solute, concentration 40 g/dm³', 'Volume = 8 ÷ 40 = 0.2 dm³ = 200 cm³'),
                         ('100 cm³ of 60 g/dm³ diluted to 300 cm³', 'New concentration = 20 g/dm³')],
               'title': 'Concentration Calculations'},
  'quiz': [{'opts': [('50 g/dm³ — volume = 500 ÷ 1000 = 0.5 dm³, concentration = 25 ÷ 0.5 = 50', True),
                     ('0.05 g/dm³ — concentration = 25 ÷ 500', False),
                     ('12500 g/dm³ — concentration = 25 × 500', False),
                     ('2.5 g/dm³ — concentration = 25 ÷ 10', False)],
            'q': '25 g of glucose is dissolved in 500 cm³ of water. What is the concentration in g/dm³?',
            'wrong_explanations': {1: 'This uses 500 cm³ directly without converting to dm³ — gives an answer 1000× '
                                      'too small. Must convert: 500 cm³ = 0.5 dm³.',
                                   2: 'This multiplies instead of divides — and still fails to convert units.',
                                   3: 'This divides by 10 instead of 0.5 — an incorrect conversion. 500 cm³ = 0.5 dm³, '
                                      'not 10 dm³.'}},
           {'opts': [('20 g — mass = 80 × 0.25 dm³ = 20 g', True),
                     ('20000 g — mass = 80 × 250 (forgetting to convert cm³ to dm³)', False),
                     ('0.32 g — mass = 80 ÷ 250', False),
                     ('320 g — mass = 80 × (250 ÷ 10)', False)],
            'q': 'A solution has a concentration of 80 g/dm³. What mass of solute is in 250 cm³ of this solution?',
            'wrong_explanations': {1: 'Using 250 directly without converting gives 80 × 250 = 20,000 — not 20. Always '
                                      'convert: 250 cm³ = 0.25 dm³.',
                                   2: 'Dividing gives volume, not mass. mass = concentration × volume.',
                                   3: '250 ÷ 10 = 25 — but the conversion is 250 ÷ 1000 = 0.25 dm³.'}}],
  'rp': None,
  'spec': '5.3.2.5',
  'summary': 'Define concentration and calculate it from mass and volume.',
  'theory': [{'content': 'The CONCENTRATION of a solution tells us how much solute is dissolved per unit volume of '
                         'solution.\n'
                         '\n'
                         'A CONCENTRATED solution has a LOT of solute dissolved in a given volume.\n'
                         'A DILUTE solution has a LITTLE solute dissolved in the same volume.\n'
                         '\n'
                         'Concentration can be expressed in two ways at Foundation level:\n'
                         '\n'
                         '1. In g/dm³ (grams per decimetre cubed):\n'
                         'Concentration (g/dm³) = mass of solute (g) ÷ volume of solution (dm³)\n'
                         '\n'
                         '2. In g/cm³ (grams per centimetre cubed) — less common:\n'
                         'Concentration (g/cm³) = mass of solute (g) ÷ volume of solution (cm³)\n'
                         '\n'
                         'Note: 1 dm³ = 1000 cm³ = 1 litre',
              'heading': 'What is Concentration?'},
             {'content': 'FORMULA:\n'
                         'concentration (g/dm³) = mass of solute (g) ÷ volume of solution (dm³)\n'
                         '\n'
                         'Rearranging:\n'
                         'mass (g) = concentration (g/dm³) × volume (dm³)\n'
                         'volume (dm³) = mass (g) ÷ concentration (g/dm³)\n'
                         '\n'
                         'IMPORTANT: volume must be in dm³. If given in cm³, divide by 1000 first.\n'
                         '250 cm³ = 0.250 dm³\n'
                         '500 cm³ = 0.500 dm³\n'
                         '\n'
                         'EXAMPLES:\n'
                         '1. 10 g of NaCl dissolved in 0.5 dm³ (500 cm³) of water.\n'
                         'Concentration = 10 ÷ 0.5 = 20 g/dm³\n'
                         '\n'
                         '2. A solution has concentration 50 g/dm³. What mass is in 200 cm³?\n'
                         'Volume = 200 ÷ 1000 = 0.2 dm³\n'
                         'Mass = 50 × 0.2 = 10 g\n'
                         '\n'
                         '3. 8 g of glucose gives a concentration of 16 g/dm³. What volume was used?\n'
                         'Volume = 8 ÷ 16 = 0.5 dm³ = 500 cm³',
              'heading': 'Calculating Concentration'},
             {'content': 'DILUTION means adding more solvent (usually water) to reduce the concentration of a '
                         'solution.\n'
                         '\n'
                         'When you dilute a solution:\n'
                         'The AMOUNT of solute stays the SAME.\n'
                         'The VOLUME increases.\n'
                         'The CONCENTRATION decreases.\n'
                         '\n'
                         'Dilution formula:\n'
                         'concentration₁ × volume₁ = concentration₂ × volume₂\n'
                         '\n'
                         'Example:\n'
                         '100 cm³ of 40 g/dm³ solution is diluted to 400 cm³. What is the new concentration?\n'
                         'c₁V₁ = c₂V₂\n'
                         '40 × 0.1 = c₂ × 0.4\n'
                         '4 = c₂ × 0.4\n'
                         'c₂ = 4 ÷ 0.4 = 10 g/dm³\n'
                         '\n'
                         'SERIAL DILUTION:\n'
                         'A technique where a solution is diluted by a fixed factor multiple times.\n'
                         'Useful for making a range of known concentrations.\n'
                         'Example: Start with 100 g/dm³ → dilute 1:10 → 10 g/dm³ → dilute 1:10 → 1 g/dm³.',
              'heading': 'Dilution'}],
  'title': 'Concentration of Solutions',
  'triple_only': None,
  'variables': [('c', 'Concentration', 'g/dm³', 'g/dm³'),
                ('m', 'Mass of solute', 'grams', 'g'),
                ('V', 'Volume of solution', 'dm³', 'dm³')]}],

"chemical-changes": [{'common_mistake': 'A metal can only displace another metal that is BELOW it in the reactivity series. Copper cannot '
                    'displace iron from iron sulfate — copper is less reactive than iron. The more reactive metal '
                    'always displaces the less reactive one, not the other way around.',
  'equations': ['Fe + CuSO₄ → FeSO₄ + Cu  (displacement)',
                'Metal + oxygen → metal oxide',
                'Metal + water → metal hydroxide + hydrogen',
                'Metal + acid → salt + hydrogen'],
  'fifas': [],
  'higher': None,
  'id': 'reactivity-series',
  'key_note': 'Reactivity series: K, Na, Li, Ca, Mg, Al, (C), Zn, Fe, Sn, Pb, (H), Cu, Ag, Au, Pt. More reactive metal '
              'displaces less reactive from solution or oxide. Evidence from reactions with water, acid and '
              'displacement reactions.',
  'matching': {'instruction': 'Predict whether each displacement reaction occurs.',
               'pairs': [('Reaction occurs',
                          'Zinc + copper sulfate → zinc sulfate + copper (Zn more reactive than Cu)'),
                         ('No reaction', 'Copper + zinc sulfate — copper is LESS reactive than zinc'),
                         ('Reaction occurs',
                          'Magnesium + iron sulfate → magnesium sulfate + iron (Mg more reactive than Fe)'),
                         ('No reaction', 'Iron + magnesium sulfate — iron is LESS reactive than magnesium'),
                         ('Reaction occurs',
                          'Iron + copper sulfate → iron sulfate + copper (Fe more reactive than Cu)')],
               'title': 'Displacement — Reaction or No Reaction?'},
  'quiz': [{'opts': [('The blue solution fades and copper metal deposits on the zinc — zinc displaces copper', True),
                     ('No change — zinc and copper have similar reactivity', False),
                     ('The zinc dissolves and the solution turns orange', False),
                     ('Zinc sulfate crystals form in the blue solution', False)],
            'q': 'A strip of zinc is placed in copper sulfate solution. What is observed?',
            'wrong_explanations': {1: 'Zinc IS more reactive than copper — a reaction occurs. The solution changes '
                                      'from blue (Cu²⁺) to colourless/pale (Zn²⁺).',
                                   2: 'The solution turns pale/colourless as Cu²⁺ ions are replaced by Zn²⁺ — orange '
                                      'is not the colour of any of these solutions.',
                                   3: "Zinc sulfate is formed in solution (dissolved) — it doesn't crystallise out "
                                      'immediately under these conditions.'}},
           {'opts': [('Copper is BELOW hydrogen in the reactivity series — it cannot displace hydrogen from the acid',
                      True),
                     ('Copper is too dense to react with liquids', False),
                     ('Hydrochloric acid is not strong enough to react with any metals', False),
                     ('Copper reacts with acid but the product is insoluble', False)],
            'q': 'Why does copper not react with dilute hydrochloric acid?',
            'wrong_explanations': {1: "Density doesn't determine reactivity — gold is denser than magnesium but far "
                                      'less reactive.',
                                   2: 'HCl reacts with many metals — magnesium, zinc, iron all react vigorously with '
                                      "HCl. Only metals BELOW hydrogen in the series don't react.",
                                   3: "Copper doesn't react with dilute HCl at all — it doesn't produce any "
                                      'product.'}}],
  'rp': None,
  'spec': '5.4.1.1–5.4.1.2',
  'summary': 'Describe the reactivity series of metals and use it to predict reactions.',
  'theory': [{'content': 'The REACTIVITY SERIES is a list of metals in order of their reactivity — from most reactive '
                         'to least reactive.\n'
                         '\n'
                         'Most reactive (top) to least reactive (bottom):\n'
                         'Potassium (K)\n'
                         'Sodium (Na)\n'
                         'Lithium (Li)\n'
                         'Calcium (Ca)\n'
                         'Magnesium (Mg)\n'
                         'Aluminium (Al)\n'
                         'Carbon (C)* — not a metal, included as reference\n'
                         'Zinc (Zn)\n'
                         'Iron (Fe)\n'
                         'Tin (Sn)\n'
                         'Lead (Pb)\n'
                         'Hydrogen (H)* — not a metal, included as reference\n'
                         'Copper (Cu)\n'
                         'Silver (Ag)\n'
                         'Gold (Au)\n'
                         'Platinum (Pt)\n'
                         '\n'
                         'Memory aid: Potassium Sodium Lithium Calcium Magnesium Aluminium Carbon Zinc Iron Tin Lead '
                         'Hydrogen Copper Silver Gold Platinum\n'
                         "→ 'Please Stop Letting Clumsy Miners Accidentally Cut Zinc Into Tiny Little Holes — Copper "
                         "Stands Guarding Platinum'",
              'heading': 'The Reactivity Series'},
             {'content': 'The reactivity series is established by observing how vigorously metals react:\n'
                         '\n'
                         'REACTIONS WITH WATER:\n'
                         'Potassium: explosive, ignites hydrogen gas (lilac flame).\n'
                         'Sodium: vigorous fizzing, melts into a ball, may ignite.\n'
                         'Lithium: steady fizzing.\n'
                         'Calcium: steady bubbling, solution turns cloudy (Ca(OH)₂).\n'
                         'Magnesium: barely reacts with cold water; reacts well with steam.\n'
                         'Iron: reacts very slowly with steam to form iron oxide and hydrogen.\n'
                         'Copper, silver, gold: no reaction with water.\n'
                         '\n'
                         'REACTIONS WITH DILUTE ACID:\n'
                         'More reactive metals react faster and more vigorously with dilute acids.\n'
                         'Magnesium: vigorous fizzing — reacts quickly.\n'
                         'Zinc: steady bubbling.\n'
                         'Iron: slow bubbling.\n'
                         'Copper: no reaction — below hydrogen in reactivity series.\n'
                         'Gold, platinum: no reaction with dilute acid.',
              'heading': 'Metal Reactions — Evidence for Reactivity Order'},
             {'content': 'A MORE REACTIVE metal will DISPLACE a LESS REACTIVE metal from its compound (salt or '
                         'oxide).\n'
                         '\n'
                         'DISPLACEMENT FROM SALT SOLUTIONS:\n'
                         'If iron is added to copper sulfate solution:\n'
                         'Fe + CuSO₄ → FeSO₄ + Cu\n'
                         'Iron is more reactive than copper → iron displaces copper.\n'
                         'Observation: blue solution turns pale green; copper metal deposits on the iron.\n'
                         '\n'
                         'If copper is added to iron sulfate solution:\n'
                         'No reaction — copper is LESS reactive than iron.\n'
                         '\n'
                         'DISPLACEMENT FROM METAL OXIDES:\n'
                         'Hydrogen can displace metals BELOW it in the series from their oxides.\n'
                         'Carbon can reduce (displace) metals below it in the series.\n'
                         'Copper oxide + hydrogen:\n'
                         'CuO + H₂ → Cu + H₂O (copper extracted from its oxide)\n'
                         '\n'
                         'METAL OXIDES:\n'
                         'Metal oxides are BASIC — they neutralise acids.\n'
                         'The more reactive the metal, the more stable its oxide — harder to decompose or reduce.',
              'heading': 'Metal Oxides and Displacement Reactions'}],
  'title': 'Reactivity of Metals and Metal Oxides',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Aluminium is above carbon in the reactivity series — carbon CANNOT reduce aluminium oxide. '
                    'Students often try to apply carbon reduction to all metals. Only metals BELOW carbon in the '
                    'reactivity series can be extracted by carbon reduction. Metals above carbon (including aluminium) '
                    'require electrolysis.',
  'equations': ['Fe₂O₃ + 3CO → 2Fe + 3CO₂  (iron extraction)',
                'ZnO + C → Zn + CO₂',
                '2Al₂O₃ → 4Al + 3O₂  (electrolysis of aluminium oxide)'],
  'fifas': [],
  'higher': None,
  'id': 'extraction-of-metals',
  'key_note': 'Extraction method depends on reactivity. Above carbon in series → electrolysis (Al, Mg, Na etc.). Below '
              'carbon → reduction with carbon/CO (Fe, Zn etc.). Unreactive metals → found native or simple reduction. '
              'Iron: blast furnace with CO. Aluminium: electrolysis of molten Al₂O₃ in cryolite.',
  'matching': {'instruction': 'Match each metal to how it is extracted from its ore.',
               'pairs': [('Iron',
                          'Reduced with carbon monoxide in a blast furnace — below carbon in reactivity series'),
                         ('Aluminium', 'Electrolysis of molten Al₂O₃ in cryolite — above carbon in reactivity series'),
                         ('Gold', 'Found as the pure element — too unreactive to form stable compounds'),
                         ('Zinc', 'Heated with carbon/coke — ZnO + C → Zn + CO₂'),
                         ('Sodium', 'Electrolysis of molten NaCl — far too reactive for carbon reduction')],
               'title': 'Match the Metal to its Extraction Method'},
  'quiz': [{'opts': [('Aluminium is more reactive than carbon — carbon cannot displace it from aluminium oxide', True),
                     ("Aluminium oxide doesn't contain enough oxygen for the carbon to react with", False),
                     ('Carbon would contaminate the aluminium, making it too brittle to use', False),
                     ('Electrolysis is cheaper than heating with carbon for all metals', False)],
            'q': 'Why is aluminium extracted by electrolysis rather than by reduction with carbon?',
            'wrong_explanations': {1: 'Aluminium oxide has plenty of oxygen — but carbon can only REDUCE metal oxides '
                                      'when the metal is LESS reactive than carbon.',
                                   2: 'Carbon and aluminium do not form harmful alloys under these conditions — purity '
                                      'concerns are a separate issue.',
                                   3: 'Electrolysis is actually VERY EXPENSIVE — it requires huge amounts of '
                                      'electrical energy. The reason is purely reactivity-based.'}},
           {'opts': [('Reduction — the iron oxide loses oxygen; the carbon monoxide gains oxygen (and is oxidised)',
                      True),
                     ('Oxidation — the iron oxide gains electrons from the carbon monoxide', False),
                     ('Neutralisation — the acid iron oxide is neutralised by the basic carbon', False),
                     ('Electrolysis — electrical energy breaks apart the iron oxide', False)],
            'q': 'Carbon monoxide reduces iron oxide in the blast furnace. What type of reaction is this?',
            'wrong_explanations': {1: 'The IRON OXIDE loses oxygen (is REDUCED). The CO gains oxygen (is OXIDISED). '
                                      'These are simultaneous — the reaction is both a reduction AND an oxidation.',
                                   2: 'Neutralisation involves an acid and a base — iron oxide and carbon monoxide are '
                                      'not an acid-base pair.',
                                   3: 'The blast furnace uses heat (combustion), not electricity. Electrolysis is used '
                                      'for reactive metals like aluminium.'}}],
  'rp': None,
  'spec': '5.4.1.3',
  'summary': 'Explain how metals are extracted from their ores and how the method depends on reactivity.',
  'theory': [{'content': 'Most metals are found in nature as ORES — rocks containing metal compounds (usually oxides, '
                         'sulfides or carbonates) rather than pure metals.\n'
                         '\n'
                         'Only very UNREACTIVE metals (gold, platinum, silver) are found as pure elements in nature — '
                         'they are too unreactive to form compounds with oxygen or sulfur.\n'
                         '\n'
                         'All other metals must be EXTRACTED from their ores — the metal compound must be converted '
                         'back to a pure metal.\n'
                         '\n'
                         'The REACTIVITY of the metal determines the EXTRACTION METHOD:\n'
                         'VERY REACTIVE metals (K, Na, Ca, Mg, Al) — cannot be extracted by carbon reduction because '
                         'they are more reactive than carbon. Must use ELECTROLYSIS of molten compounds.\n'
                         '\n'
                         'MODERATELY REACTIVE metals BELOW carbon in the series (Zn, Fe, Sn, Pb) — can be extracted by '
                         'heating their oxide with CARBON (reduction).\n'
                         '\n'
                         'UNREACTIVE metals (Cu, Ag, Au) — found native (as pure elements) or can be extracted by '
                         'simple reduction or displacement.',
              'heading': 'Why Metals Need to be Extracted'},
             {'content': 'REDUCTION WITH CARBON (also called SMELTING) works for metals below carbon in the reactivity '
                         'series.\n'
                         '\n'
                         'Carbon displaces these metals from their oxides because carbon is MORE REACTIVE than these '
                         'metals.\n'
                         '\n'
                         'IRON FROM IRON OXIDE (Blast Furnace):\n'
                         'Iron ore (mainly haematite: Fe₂O₃) is heated with coke (carbon) and limestone in a blast '
                         'furnace.\n'
                         'Carbon reacts with oxygen to form carbon dioxide:\n'
                         'C + O₂ → CO₂\n'
                         'CO₂ then reacts with more carbon to form carbon monoxide:\n'
                         'CO₂ + C → 2CO\n'
                         'Carbon monoxide REDUCES iron oxide to iron:\n'
                         'Fe₂O₃ + 3CO → 2Fe + 3CO₂\n'
                         'Molten iron sinks to the bottom of the furnace and is tapped off.\n'
                         '\n'
                         'ZINC EXTRACTION:\n'
                         'ZnO + C → Zn + CO₂\n'
                         '\n'
                         'ALUMINIUM CANNOT be extracted this way — it is above carbon in the reactivity series and '
                         'must use electrolysis.',
              'heading': 'Reduction with Carbon — Blast Furnace'},
             {'content': 'ELECTROLYSIS is used for metals that are MORE REACTIVE than carbon (K, Na, Li, Ca, Mg, Al).\n'
                         '\n'
                         'These metals form very stable compounds — carbon cannot reduce them.\n'
                         'Instead, electrical energy is used to decompose the molten compound.\n'
                         '\n'
                         'ALUMINIUM EXTRACTION (Hall-Héroult process):\n'
                         'Aluminium oxide (Al₂O₃) — also called alumina — is dissolved in molten cryolite (to lower '
                         'the melting point from ~2000°C to ~950°C).\n'
                         'Electrolysis takes place:\n'
                         'At CATHODE (negative): Al³⁺ + 3e⁻ → Al (aluminium deposited)\n'
                         'At ANODE (positive): O²⁻ → O₂ (oxygen gas produced)\n'
                         'Molten aluminium sinks to the bottom and is tapped off.\n'
                         '\n'
                         'Why electrolysis is expensive:\n'
                         'Huge amounts of ELECTRICAL ENERGY needed.\n'
                         'The process must run continuously at high temperatures.\n'
                         'The carbon anodes react with oxygen and must be REPLACED regularly.\n'
                         '\n'
                         'This is why aluminium was once more expensive than gold — before cheap electricity, it was '
                         'extremely difficult to extract.',
              'heading': 'Electrolysis for Reactive Metals'}],
  'title': 'Extraction of Metals and Reduction',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In a redox reaction, the REDUCING AGENT is OXIDISED (it gives away electrons/oxygen). The '
                    'OXIDISING AGENT is REDUCED (it receives electrons/gains oxygen). This is counterintuitive — an '
                    "oxidising agent doesn't stay oxidised, it gets reduced. Remember: agents do the opposite of what "
                    "they're called.",
  'equations': ['Oxidation = gain of oxygen / loss of electrons',
                'Reduction = loss of oxygen / gain of electrons',
                'OIL RIG: Oxidation Is Loss, Reduction Is Gain (electrons)'],
  'fifas': [],
  'higher': None,
  'id': 'oxidation-reduction',
  'key_note': 'Oxidation: gain O / lose electrons. Reduction: lose O / gain electrons. OIL RIG. Always happen together '
              '(redox). Reducing agent: donates electrons → gets oxidised. Oxidising agent: accepts electrons → gets '
              'reduced. Carbon and hydrogen are common reducing agents.',
  'matching': {'instruction': 'Identify whether each substance is oxidised or reduced in the reaction.',
               'pairs': [('Oxidised', 'Mg in Mg + O₂ → MgO — magnesium gains oxygen'),
                         ('Reduced', 'CuO in CuO + H₂ → Cu + H₂O — copper oxide loses oxygen'),
                         ('Oxidised', 'H₂ in CuO + H₂ → Cu + H₂O — hydrogen gains oxygen'),
                         ('Reduced', 'Fe₂O₃ in Fe₂O₃ + 3CO → 2Fe + 3CO₂ — iron oxide loses oxygen'),
                         ('Oxidised', 'Na in Na → Na⁺ + e⁻ — sodium loses an electron (OIL RIG)')],
               'title': 'Oxidised or Reduced?'},
  'quiz': [{'opts': [('Hydrogen (H₂) — it reduces the copper oxide by removing its oxygen, and is itself oxidised to '
                      'water',
                      True),
                     ('Copper oxide — it causes the hydrogen to become water', False),
                     ('Copper — it is the product of reduction', False),
                     ('Water — it is formed when hydrogen is reduced', False)],
            'q': 'In the reaction CuO + H₂ → Cu + H₂O, what is the reducing agent?',
            'wrong_explanations': {1: 'Copper oxide is the OXIDISING AGENT — it provides the oxygen that oxidises '
                                      'hydrogen. It is itself reduced.',
                                   2: 'Copper is the PRODUCT of the reduction of CuO — it is not a reducing agent.',
                                   3: 'Water is a PRODUCT — reducing agents are reactants that cause reduction of '
                                      'another substance.'}},
           {'opts': [('Oxidation Is Loss (of electrons), Reduction Is Gain (of electrons)', True),
                     ('Oxidation Involves Losing Reactants, Reduction Involves Gaining', False),
                     ('Oxygen In Liquid, Reactions In Gas', False),
                     ('Only In Liquids Reactions Involve Gases', False)],
            'q': 'What does OIL RIG stand for?',
            'wrong_explanations': {1: 'OIL RIG specifically refers to ELECTRONS — Oxidation Is Loss of electrons, '
                                      "Reduction Is Gain of electrons. The words 'reactants' and 'gaining' are "
                                      'incorrect.',
                                   2: 'OIL RIG is a memory aid specifically about electron transfer in redox reactions '
                                      '— not about phases or states of matter.',
                                   3: 'OIL RIG is entirely about electrons in redox reactions — not about the physical '
                                      'state of substances.'}}],
  'rp': None,
  'spec': '5.4.1.4',
  'summary': 'Define oxidation and reduction in terms of oxygen gain/loss and use OIL RIG.',
  'theory': [{'content': 'OXIDATION and REDUCTION always occur TOGETHER in the same reaction — called a REDOX '
                         'reaction.\n'
                         '\n'
                         'In terms of OXYGEN:\n'
                         'OXIDATION = GAIN of oxygen.\n'
                         'REDUCTION = LOSS of oxygen.\n'
                         '\n'
                         'Examples:\n'
                         'Mg + O₂ → MgO\n'
                         'Magnesium is OXIDISED — it gains oxygen.\n'
                         '\n'
                         'CuO + H₂ → Cu + H₂O\n'
                         'Copper oxide is REDUCED — it loses oxygen.\n'
                         'Hydrogen is OXIDISED — it gains oxygen.\n'
                         '\n'
                         'Fe₂O₃ + 3CO → 2Fe + 3CO₂\n'
                         'Iron oxide (Fe₂O₃) is REDUCED — iron loses its oxygen.\n'
                         'Carbon monoxide (CO) is OXIDISED — it gains oxygen to become CO₂.',
              'heading': 'Oxidation and Reduction — Oxygen Definitions'},
             {'content': 'At a more advanced level, oxidation and reduction are defined in terms of ELECTRONS:\n'
                         '\n'
                         'OIL RIG:\n'
                         'Oxidation Is Loss (of electrons)\n'
                         'Reduction Is Gain (of electrons)\n'
                         '\n'
                         'Think of OIL RIG as a memory device — it only works when you remember what each letter '
                         'means.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Na → Na⁺ + e⁻ — sodium LOSES an electron → sodium is OXIDISED.\n'
                         'Cl + e⁻ → Cl⁻ — chlorine GAINS an electron → chlorine is REDUCED.\n'
                         '\n'
                         'In the reaction: Na + Cl → Na⁺ + Cl⁻\n'
                         'Sodium is OXIDISED (loses e⁻). Chlorine is REDUCED (gains e⁻).\n'
                         'This is a REDOX reaction — both happen simultaneously.\n'
                         '\n'
                         'The substance that causes oxidation is the OXIDISING AGENT.\n'
                         'The substance that causes reduction is the REDUCING AGENT.\n'
                         '\n'
                         'Note: the oxidising agent is itself REDUCED (it gains electrons). The reducing agent is '
                         'itself OXIDISED (it loses electrons).',
              'heading': 'OIL RIG — Electron Definitions (Overview)'},
             {'content': 'REDUCING AGENT — causes reduction of another substance by donating electrons (it is itself '
                         'OXIDISED):\n'
                         'Carbon in the blast furnace: reduces iron oxide — carbon is the REDUCING AGENT (it gets '
                         'oxidised to CO₂).\n'
                         'Hydrogen: reduces copper oxide — hydrogen is the REDUCING AGENT (gets oxidised to H₂O).\n'
                         '\n'
                         'OXIDISING AGENT — causes oxidation of another substance by accepting electrons (it is itself '
                         'REDUCED):\n'
                         'Oxygen: oxidises metals (is itself reduced to O²⁻).\n'
                         'Copper oxide: oxidises hydrogen (is itself reduced to Cu).\n'
                         '\n'
                         'Common reducing agents: hydrogen, carbon, carbon monoxide, more reactive metals.\n'
                         'Common oxidising agents: oxygen, chlorine, hydrogen peroxide, potassium manganate(VII).\n'
                         '\n'
                         'REDOX in everyday contexts:\n'
                         'Rusting — iron is OXIDISED by oxygen and water.\n'
                         'Combustion — fuels are OXIDISED by oxygen.\n'
                         'Metabolic respiration — glucose is OXIDISED.\n'
                         'Photosynthesis — CO₂ is REDUCED to glucose.',
              'heading': 'Oxidising and Reducing Agents'}],
  'title': 'Oxidation and Reduction',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Acid + metal carbonate produces THREE products: salt + water + carbon DIOXIDE. Students often '
                    'forget the water or forget the CO₂. Also: the SALT name comes from the METAL and the ACID — '
                    'sulfuric acid always gives sulfate salts, hydrochloric acid gives chloride salts, nitric acid '
                    'gives nitrate salts.',
  'equations': ['Acid + metal → salt + hydrogen',
                'Acid + metal oxide → salt + water',
                'Acid + metal hydroxide → salt + water',
                'Acid + metal carbonate → salt + water + carbon dioxide',
                'Mg + 2HCl → MgCl₂ + H₂',
                'CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂'],
  'fifas': [],
  'higher': None,
  'id': 'reactions-of-acids',
  'key_note': 'Acid + metal → salt + H₂ (metals above H only). Acid + metal oxide → salt + H₂O. Acid + metal hydroxide '
              '→ salt + H₂O (neutralisation). Acid + carbonate → salt + H₂O + CO₂. H₂: squeaky pop. CO₂: turns '
              'limewater milky. Salt name = metal + acid anion.',
  'matching': {'instruction': 'Match each type of reaction to the products formed.',
               'pairs': [('Acid + metal', 'Salt + hydrogen gas — test with lit splint gives squeaky pop'),
                         ('Acid + metal oxide', 'Salt + water only — no gas produced'),
                         ('Acid + metal hydroxide', 'Salt + water — neutralisation reaction'),
                         ('Acid + metal carbonate', 'Salt + water + carbon dioxide — CO₂ turns limewater milky')],
               'title': 'Match the Acid Reaction to its Products'},
  'quiz': [{'opts': [('Zinc sulfate + water + carbon dioxide', True),
                     ('Zinc sulfate + hydrogen', False),
                     ('Zinc oxide + water + carbon dioxide', False),
                     ('Zinc sulfate + water only', False)],
            'q': 'What are the products when zinc carbonate reacts with sulfuric acid?',
            'wrong_explanations': {1: 'Zinc + sulfuric acid → zinc sulfate + hydrogen. Carbonates produce CO₂, not H₂.',
                                   2: 'Zinc carbonate is a CARBONATE — the products of acid + carbonate are salt + '
                                      'water + CO₂, not zinc oxide.',
                                   3: 'Carbonates produce salt + water + CO₂ — not just salt + water. The CO₂ is '
                                      'essential.'}},
           {'opts': [('Magnesium chloride (MgCl₂) — HCl produces chloride salts', True),
                     ('Magnesium sulfate — all acids produce sulfate salts', False),
                     ('Magnesium oxide — magnesium reacts with hydrogen to form the oxide', False),
                     ('Magnesium hydroxide — the hydrogen from HCl bonds to the magnesium', False)],
            'q': 'Magnesium reacts with hydrochloric acid. What salt is produced?',
            'wrong_explanations': {1: 'Sulfuric acid (H₂SO₄) produces SULFATE salts. Hydrochloric acid (HCl) always '
                                      'produces CHLORIDE salts.',
                                   2: 'The acid does NOT supply oxygen — magnesium oxide would form from Mg reacting '
                                      'with O₂. The reaction with HCl gives a chloride salt.',
                                   3: 'The acid produces H⁺ ions which react to form H₂ gas — they do NOT combine with '
                                      'the metal to form a hydroxide.'}}],
  'rp': None,
  'spec': '5.4.2.1–5.4.2.2',
  'summary': 'Describe reactions of acids with metals, metal oxides, metal hydroxides and carbonates.',
  'theory': [{'content': 'An ACID is a substance that produces H⁺ ions (hydrogen ions) when dissolved in water.\n'
                         'Common acids: hydrochloric acid (HCl), sulfuric acid (H₂SO₄), nitric acid (HNO₃).\n'
                         '\n'
                         'A BASE is a substance that neutralises an acid. Bases are metal oxides or metal hydroxides.\n'
                         'An ALKALI is a base that dissolves in water — it produces OH⁻ ions in solution.\n'
                         'Common alkalis: sodium hydroxide (NaOH), potassium hydroxide (KOH), calcium hydroxide '
                         '(Ca(OH)₂).\n'
                         '\n'
                         'All acid reactions produce a SALT — formed from the positive metal ion and the negative ion '
                         'from the acid:\n'
                         'Hydrochloric acid → CHLORIDE salts (e.g. NaCl, MgCl₂)\n'
                         'Sulfuric acid → SULFATE salts (e.g. ZnSO₄, CuSO₄)\n'
                         'Nitric acid → NITRATE salts (e.g. Ca(NO₃)₂, KNO₃)',
              'heading': 'What Are Acids and Bases?'},
             {'content': 'ACID + METAL → SALT + HYDROGEN:\n'
                         'Mg + 2HCl → MgCl₂ + H₂\n'
                         'Zn + H₂SO₄ → ZnSO₄ + H₂\n'
                         'Fe + 2HCl → FeCl₂ + H₂\n'
                         '\n'
                         'Test for hydrogen: lit splint → squeaky pop.\n'
                         'Only metals ABOVE hydrogen in reactivity series react with dilute acids.\n'
                         'Copper, silver, gold — NO reaction.\n'
                         '\n'
                         'ACID + METAL OXIDE → SALT + WATER:\n'
                         'Metal oxides are BASES — they neutralise acids.\n'
                         'CuO + 2HCl → CuCl₂ + H₂O\n'
                         'ZnO + H₂SO₄ → ZnSO₄ + H₂O\n'
                         'Fe₂O₃ + 3H₂SO₄ → Fe₂(SO₄)₃ + 3H₂O\n'
                         '\n'
                         'Observation: the metal oxide powder DISSOLVES in the acid as the reaction proceeds. The '
                         'solution often changes colour as the metal salt forms (e.g. blue for copper sulfate).',
              'heading': 'Reactions with Metals and Metal Oxides'},
             {'content': 'ACID + METAL HYDROXIDE → SALT + WATER (neutralisation):\n'
                         'NaOH + HCl → NaCl + H₂O\n'
                         '2KOH + H₂SO₄ → K₂SO₄ + 2H₂O\n'
                         'Ca(OH)₂ + 2HCl → CaCl₂ + 2H₂O\n'
                         '\n'
                         'This is a NEUTRALISATION reaction — H⁺ from acid combines with OH⁻ from alkali to form '
                         'water.\n'
                         '\n'
                         'ACID + METAL CARBONATE → SALT + WATER + CARBON DIOXIDE:\n'
                         'CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂\n'
                         'Na₂CO₃ + H₂SO₄ → Na₂SO₄ + H₂O + CO₂\n'
                         'ZnCO₃ + 2HCl → ZnCl₂ + H₂O + CO₂\n'
                         '\n'
                         'Test for CO₂: bubble through limewater → turns milky/cloudy.\n'
                         '\n'
                         'Observation: fizzing/effervescence as CO₂ gas is produced. The solid carbonate dissolves as '
                         'the reaction proceeds.\n'
                         '\n'
                         'Summary of products:\n'
                         'Acid + metal → salt + hydrogen\n'
                         'Acid + metal oxide → salt + water\n'
                         'Acid + metal hydroxide → salt + water\n'
                         'Acid + metal carbonate → salt + water + carbon dioxide',
              'heading': 'Reactions with Hydroxides and Carbonates'}],
  'title': 'Reactions of Acids with Metals and Bases',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'When making a salt by adding excess solid to acid — you MUST use EXCESS solid to ensure ALL the '
                    "acid reacts. If you don't use excess, some acid remains and the final product will be "
                    'contaminated with acid. Then filter off the excess unreacted solid — the salt is in the filtrate.',
  'equations': ['H⁺(aq) + OH⁻(aq) → H₂O(l)  (ionic equation for neutralisation)',
                'Acid + alkali → salt + water',
                'BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq)'],
  'fifas': [],
  'higher': None,
  'id': 'salts-neutralisation',
  'key_note': 'Soluble salt from acid + solid: add excess solid, filter off excess, evaporate/crystallise. Soluble '
              'salt from two soluble reactants: titration to find volumes, then repeat without indicator. Insoluble '
              'salt: mix two solutions, precipitate forms, filter/wash/dry. Neutralisation: H⁺ + OH⁻ → H₂O.',
  'matching': {'instruction': 'Match each salt to the best method for making it.',
               'pairs': [('Copper sulfate (CuSO₄)',
                          'Add excess CuO to H₂SO₄ — filter off excess CuO — evaporate to crystallise'),
                         ('Sodium chloride (NaCl)',
                          'Titration — NaOH + HCl — find exact volume needed, then evaporate'),
                         ('Barium sulfate (BaSO₄)', 'Precipitation — mix BaCl₂(aq) + Na₂SO₄(aq) — filter and dry'),
                         ('Zinc chloride (ZnCl₂)', 'Add excess zinc carbonate to HCl — filter off excess — evaporate')],
               'title': 'Method for Making Each Salt'},
  'quiz': [{'opts': [('To ensure all the acid reacts — any remaining acid would contaminate the final salt', True),
                     ('To speed up the reaction — more solid increases the rate', False),
                     ('To increase the yield of salt — more reactant gives more product', False),
                     ('The excess solid acts as a catalyst', False)],
            'q': 'Why must excess solid be added when making a salt by reacting a metal oxide with an acid?',
            'wrong_explanations': {1: 'Excess solid does increase the surface area and reaction rate — but the MAIN '
                                      'reason is to guarantee complete neutralisation of all the acid.',
                                   2: 'You cannot add more solid than the acid can react with — excess produces the '
                                      'same yield. The reason is to ensure complete reaction.',
                                   3: "The excess solid is REMOVED by filtration — it doesn't catalyse the reaction."}},
           {'opts': [('H⁺(aq) + OH⁻(aq) → H₂O(l)', True),
                     ('Acid + alkali → salt + water', False),
                     ('Na⁺(aq) + Cl⁻(aq) → NaCl(s)', False),
                     ('H₂ + O₂ → H₂O', False)],
            'q': 'What is the ionic equation for neutralisation?',
            'wrong_explanations': {1: 'This is the WORD equation — an ionic equation uses symbols and charges. The '
                                      'ionic equation H⁺ + OH⁻ → H₂O shows the actual ions involved.',
                                   2: 'This is a precipitation ionic equation — it describes salt formation, not '
                                      'neutralisation.',
                                   3: 'This is the equation for burning hydrogen in oxygen — not neutralisation.'}}],
  'rp': 'RP3 (Chemistry) — Prepare a sample of a pure, dry hydrated copper sulfate salt starting from copper oxide and '
        'sulfuric acid using add-excess-solid method.',
  'spec': '5.4.2.2–5.4.2.3',
  'summary': 'Describe methods for making pure dry salts from acids and how neutralisation works.',
  'theory': [{'content': 'The method for making a salt depends on whether it is SOLUBLE or INSOLUBLE.\n'
                         '\n'
                         'METHOD 1 — Acid + excess metal/metal oxide/carbonate (for soluble salts):\n'
                         '1. Add excess solid (metal, metal oxide or carbonate) to the acid — ensures all acid is used '
                         'up.\n'
                         '2. FILTER off the excess unreacted solid (the salt remains in solution).\n'
                         '3. EVAPORATE the filtrate to crystallise the salt, or leave to crystallise slowly.\n'
                         '4. Filter and dry the crystals.\n'
                         '\n'
                         'Example — copper sulfate from copper oxide:\n'
                         'CuO + H₂SO₄ → CuSO₄ + H₂O\n'
                         'Add excess black CuO powder to warm sulfuric acid → blue solution forms.\n'
                         'Filter → blue CuSO₄ solution passes through.\n'
                         'Evaporate → blue CuSO₄ crystals form.\n'
                         '\n'
                         'METHOD 2 — Titration (for soluble salts from soluble starting materials):\n'
                         'Used when both reactants are soluble (e.g. NaOH + HCl → NaCl + H₂O).\n'
                         'Cannot use Method 1 — cannot filter off excess solid.\n'
                         'Instead, use a TITRATION to find the exact volume of acid needed to neutralise the alkali.\n'
                         'Then repeat without indicator → evaporate to get pure salt crystals.',
              'heading': 'Methods of Making Salts'},
             {'content': 'INSOLUBLE SALTS cannot be made from evaporation — they would never crystallise from '
                         'solution.\n'
                         '\n'
                         'They are made by MIXING two solutions that each contain one of the ions needed.\n'
                         'The insoluble salt PRECIPITATES immediately.\n'
                         '\n'
                         'Example — making barium sulfate (BaSO₄):\n'
                         'BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq)\n'
                         'Mix barium chloride solution + sodium sulfate solution.\n'
                         'BaSO₄ precipitates as a white solid immediately.\n'
                         'FILTER to collect the precipitate.\n'
                         'WASH with distilled water to remove soluble impurities.\n'
                         'DRY in an oven.\n'
                         '\n'
                         'Precipitation reactions are also used to:\n'
                         'Remove unwanted ions from solution (e.g. water treatment).\n'
                         'Test for specific ions (e.g. adding AgNO₃ to test for chloride ions — white AgCl precipitate '
                         'forms).',
              'heading': 'Making Insoluble Salts — Precipitation'},
             {'content': 'NEUTRALISATION is the reaction between an ACID and a BASE (or alkali) to form a SALT and '
                         'WATER.\n'
                         '\n'
                         'The IONIC EQUATION for neutralisation is always the same:\n'
                         'H⁺(aq) + OH⁻(aq) → H₂O(l)\n'
                         '\n'
                         'This shows the ESSENTIAL reaction — a hydrogen ion from the acid combines with a hydroxide '
                         'ion from the alkali to form water.\n'
                         '\n'
                         'TITRATION is the technique for precisely determining how much acid neutralises a given '
                         'volume of alkali:\n'
                         '1. Pipette a known volume (e.g. 25.00 cm³) of alkali into a conical flask.\n'
                         '2. Add a few drops of INDICATOR (e.g. phenolphthalein — pink in alkali, colourless in '
                         'acid).\n'
                         '3. Slowly add acid from a BURETTE until the indicator just changes colour (the END POINT).\n'
                         '4. Record the volume of acid used (the TITRE).\n'
                         '5. Repeat to get concordant (consistent) results.\n'
                         '6. Calculate mean titre from concordant results.\n'
                         '\n'
                         'To make a PURE SALT by titration:\n'
                         'Repeat without indicator — the indicator would contaminate the salt.\n'
                         'Use the known volume from the titration.',
              'heading': 'Neutralisation in Detail'}],
  'title': 'Making Salts and Neutralisation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Lower pH = MORE ACIDIC = MORE H⁺ ions. Higher pH = MORE ALKALINE = FEWER H⁺ ions (more OH⁻). '
                    'Students often confuse pH 2 and pH 12 — pH 2 is strongly acidic, pH 12 is strongly alkaline. pH 7 '
                    'is neutral — pure water. NOT all solutions at pH 7 are water.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'ph-scale',
  'key_note': 'pH 0–6: acidic. pH 7: neutral. pH 8–14: alkaline. Lower pH = more H⁺ ions. pH scale is logarithmic — '
              'each unit = 10× change in H⁺. Universal indicator: shows range of colours. Phenolphthalein: colourless '
              'in acid, pink in alkali. pH meter: most accurate.',
  'matching': {'instruction': 'Match each pH value to the correct description.',
               'pairs': [('pH 1', 'Strongly acidic — high concentration of H⁺ ions'),
                         ('pH 7', 'Neutral — equal H⁺ and OH⁻ ions — pure water at 25°C'),
                         ('pH 13', 'Strongly alkaline — high concentration of OH⁻ ions'),
                         ('pH 4', 'Weakly acidic — e.g. black coffee or tomato juice'),
                         ('pH 10', 'Weakly alkaline — e.g. baking soda solution')],
               'title': 'Match the pH to the Description'},
  'quiz': [{'opts': [('pH 2 has 100 times more H⁺ than pH 4 — each unit on the log scale is 10×', True),
                     ('pH 2 has twice as many H⁺ ions as pH 4', False),
                     ('pH 4 has more H⁺ ions — higher pH means more hydrogen', False),
                     ('They have the same H⁺ concentration — both are acidic', False)],
            'q': 'A solution has a pH of 2. Another has a pH of 4. How do their H⁺ ion concentrations compare?',
            'wrong_explanations': {1: 'The pH scale is LOGARITHMIC — each unit represents a 10× change, not a 2× '
                                      'change. pH 2 vs pH 4 = 10² = 100× difference.',
                                   2: 'LOWER pH means MORE H⁺ ions — pH 2 is more acidic than pH 4, not less.',
                                   3: 'Both are acidic (below 7) but have very different H⁺ concentrations — pH 2 is '
                                      'much more acidic.'}},
           {'opts': [('The pH increases towards 7 — dilution reduces H⁺ concentration, making it less acidic', True),
                     ('The pH decreases — water is neutral so it makes the acid stronger', False),
                     ("The pH stays the same — water doesn't affect the acid", False),
                     ('The pH jumps immediately to 7 — water always neutralises acids', False)],
            'q': 'An acid is diluted by adding water. What happens to its pH?',
            'wrong_explanations': {1: 'Water does not make acid stronger — adding water DILUTES the acid, reducing H⁺ '
                                      'concentration and raising pH.',
                                   2: 'Water does affect the acid — it reduces the concentration of H⁺ ions (dilutes '
                                      'them). The pH INCREASES.',
                                   3: 'Unless you add enormous amounts of water, the pH approaches 7 gradually but '
                                      'never quite reaches it — you are diluting, not neutralising.'}}],
  'rp': None,
  'spec': '5.4.2.4',
  'summary': 'Describe the pH scale, what it measures and how indicators are used.',
  'theory': [{'content': 'The pH SCALE measures the CONCENTRATION of hydrogen ions (H⁺) in a solution — it indicates '
                         'how acidic or alkaline a solution is.\n'
                         '\n'
                         'Scale range: 0 to 14 (though values slightly outside this range are possible).\n'
                         '\n'
                         'pH 0–6: ACIDIC (more H⁺ ions than OH⁻ ions)\n'
                         'pH 7: NEUTRAL (equal H⁺ and OH⁻ — pure water at 25°C)\n'
                         'pH 8–14: ALKALINE (more OH⁻ ions than H⁺ ions)\n'
                         '\n'
                         'The pH scale is LOGARITHMIC — each unit change represents a 10× change in H⁺ concentration:\n'
                         'pH 3 has 10× more H⁺ than pH 4.\n'
                         'pH 3 has 100× more H⁺ than pH 5.\n'
                         '\n'
                         'Typical pH values:\n'
                         'Hydrochloric acid (conc.): pH ~0–1\n'
                         'Vinegar (ethanoic acid): pH ~3\n'
                         'Coffee: pH ~5\n'
                         'Pure water: pH 7\n'
                         'Baking soda solution: pH ~9\n'
                         'Sodium hydroxide solution: pH ~13–14',
              'heading': 'The pH Scale'},
             {'content': 'An INDICATOR is a substance that changes colour depending on the pH of a solution.\n'
                         '\n'
                         'UNIVERSAL INDICATOR:\n'
                         'A mixture of indicators that shows a range of colours across the pH scale.\n'
                         'Red → orange → yellow → green → blue → purple as pH increases from 0 to 14.\n'
                         'Gives an APPROXIMATE pH — tells you the pH range.\n'
                         '\n'
                         'LITMUS:\n'
                         'Red in ACID, blue in ALKALI, purple in neutral.\n'
                         'Simple test — tells you acid or alkali, not the pH number.\n'
                         '\n'
                         'PHENOLPHTHALEIN:\n'
                         'Colourless in acid, PINK in alkali.\n'
                         'Used in titrations — clear colour change at the end point.\n'
                         '\n'
                         'pH PROBE / METER:\n'
                         'Gives a PRECISE numerical pH reading — more accurate than indicators.\n'
                         'Used in industry and for accurate laboratory measurements.\n'
                         '\n'
                         'THE RELATIONSHIP BETWEEN pH AND CONCENTRATION:\n'
                         'The MORE H⁺ ions in solution → LOWER pH (more acidic).\n'
                         'The MORE OH⁻ ions in solution → HIGHER pH (more alkaline).\n'
                         'Adding water DILUTES the solution → concentration of H⁺ decreases → pH INCREASES towards 7.',
              'heading': 'Indicators and Measuring pH'},
             {'content': 'Adding a BASE to an ACID gradually increases the pH (makes it less acidic).\n'
                         'Adding an ACID to an ALKALI gradually decreases the pH (makes it less alkaline).\n'
                         '\n'
                         'A TITRATION CURVE shows how pH changes as acid is added to alkali:\n'
                         'At the START: pH high (~13) — the solution is strongly alkaline.\n'
                         'As acid is added: pH falls slowly at first.\n'
                         'Near the END POINT: pH drops RAPIDLY — a large pH change for a small addition.\n'
                         'At the END POINT: pH = 7 (if strong acid + strong alkali).\n'
                         'After the end point: pH continues to fall as excess acid is added.\n'
                         '\n'
                         'WHY SUCH A SHARP CHANGE NEAR THE END POINT:\n'
                         'Near the equivalence point, there is very little OH⁻ left to absorb the H⁺ from the added '
                         'acid.\n'
                         'So each small addition of acid produces a large change in H⁺ concentration → large pH '
                         'change.',
              'heading': 'Effect of Neutralisation on pH'}],
  'title': 'The pH Scale and Neutralisation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'CATHODE is NEGATIVE — positive ions are attracted to it and gain electrons (reduced). ANODE is '
                    'POSITIVE — negative ions are attracted to it and lose electrons (oxidised). Students often '
                    'confuse these. Remember: AN OX (Anode Oxidation) and RED CAT (Reduction at Cathode).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'electrolysis-principles',
  'key_note': 'Electrolysis: decomposition using electrical energy. Electrolyte: ionic compound that is molten or in '
              'solution. Cathode (−): cations attracted, gain electrons, REDUCED. Anode (+): anions attracted, lose '
              'electrons, OXIDISED. AN OX, RED CAT. Inert electrodes: graphite or platinum.',
  'matching': {'instruction': 'Match each term to its correct definition.',
               'pairs': [('Cathode', 'Negative electrode — positive ions attracted here — reduction occurs'),
                         ('Anode', 'Positive electrode — negative ions attracted here — oxidation occurs'),
                         ('Electrolyte',
                          'Ionic compound that is molten or dissolved — conducts electricity and is decomposed'),
                         ('Reduction (at cathode)', 'Cations gain electrons — metal deposited or H₂ gas produced'),
                         ('Oxidation (at anode)', 'Anions lose electrons — non-metal gas produced (O₂, Cl₂)')],
               'title': 'Electrolysis Key Terms'},
  'quiz': [{'opts': [('In the solid, ions are fixed in the lattice — they cannot move to carry charge. Molten NaCl has '
                      'free-moving ions.',
                      True),
                     ("Solid NaCl doesn't contain ions — they only form when the compound melts.", False),
                     ('Solid NaCl is too hard for electricity to pass through.', False),
                     ('Electrolysis only works on liquids — all solids resist decomposition.', False)],
            'q': 'Why can solid sodium chloride not be electrolysed, but molten sodium chloride can?',
            'wrong_explanations': {1: 'NaCl is always ionic — Na⁺ and Cl⁻ ions exist in both solid and molten states. '
                                      'The issue is whether they can MOVE.',
                                   2: 'Hardness affects mechanical properties, not ionic conductivity — the issue is '
                                      'ion mobility, not physical hardness.',
                                   3: 'Some solids are electrolysed — e.g. electrolysis of a metal anode in '
                                      'electroplating. The issue specifically with NaCl solid is fixed ions.'}},
           {'opts': [('At the anode — negative ions lose electrons here (OIL: Oxidation Is Loss)', True),
                     ('At the cathode — positive ions gain electrons here', False),
                     ('In the electrolyte — ions are oxidised as they move through the solution', False),
                     ('At both electrodes simultaneously', False)],
            'q': 'During electrolysis, where does oxidation take place?',
            'wrong_explanations': {1: 'The CATHODE is where REDUCTION occurs (positive ions GAIN electrons). Remember: '
                                      'RED CAT (Reduction at Cathode).',
                                   2: 'Ions move through the solution but are not oxidised or reduced until they reach '
                                      'an electrode.',
                                   3: 'Oxidation (at anode) and reduction (at cathode) occur at DIFFERENT electrodes — '
                                      'at the same time, but not at the same place.'}}],
  'rp': None,
  'spec': '5.4.3.1',
  'summary': 'Describe what electrolysis is, how it works and the key terms used.',
  'theory': [{'content': 'ELECTROLYSIS is the decomposition of a substance using ELECTRICAL ENERGY.\n'
                         '\n'
                         'For electrolysis to occur, the substance must be an ELECTROLYTE — a substance that can '
                         'conduct electricity AND be decomposed by it.\n'
                         '\n'
                         'Electrolytes are ionic compounds that are either:\n'
                         'MOLTEN (melted) — ions are free to move through the liquid.\n'
                         'DISSOLVED in water (aqueous solution) — ions are free to move through the solution.\n'
                         '\n'
                         'Solid ionic compounds CANNOT be electrolysed — their ions are fixed in the lattice.\n'
                         '\n'
                         'Electrolysis is used to:\n'
                         'Extract reactive metals from their ores (aluminium, sodium).\n'
                         'Electroplate metals (coating objects with a metal layer).\n'
                         'Purify metals (e.g. copper refining).\n'
                         'Manufacture chemicals (e.g. chlorine and sodium hydroxide from brine).',
              'heading': 'What is Electrolysis?'},
             {'content': 'ELECTRODES: the conductors that dip into the electrolyte.\n'
                         'Connected to a DIRECT CURRENT (DC) power supply.\n'
                         '\n'
                         'CATHODE: the NEGATIVE electrode (connected to the negative terminal).\n'
                         'ANODE: the POSITIVE electrode (connected to the positive terminal).\n'
                         'Memory: CATHode = CATs are negative (they scratch!) or: An-ODE is pOsitivE.\n'
                         '\n'
                         'How it works:\n'
                         'Positive ions (CATIONS) move TOWARDS the negative cathode.\n'
                         'At the cathode: cations GAIN electrons → REDUCED → solid metal or hydrogen gas deposited.\n'
                         '\n'
                         'Negative ions (ANIONS) move TOWARDS the positive anode.\n'
                         'At the anode: anions LOSE electrons → OXIDISED → gas or element released.\n'
                         '\n'
                         'OVERALL:\n'
                         'Oxidation at the Anode (OA).\n'
                         'Reduction at the Cathode (RC).\n'
                         'Memory: AN OX, A RED CAT (ANode OXidation; REDuction at CAThode).',
              'heading': 'Key Terms and the Apparatus'},
             {'content': 'INERT ELECTRODES (e.g. graphite or platinum):\n'
                         'Do not react with the electrolyte or products.\n'
                         'Simply provide a surface for ions to discharge.\n'
                         'Graphite is most commonly used — cheap and conducts electricity.\n'
                         '\n'
                         'REACTIVE ELECTRODES (e.g. copper in electroplating):\n'
                         'The anode dissolves into the solution as copper ions.\n'
                         'The cathode grows as copper deposits onto it.\n'
                         'Used in electroplating and copper purification.\n'
                         '\n'
                         'WHY INERT ELECTRODES ARE IMPORTANT:\n'
                         'If the anode reacted with the products or electrolyte, it would change the composition of '
                         'the solution.\n'
                         'Using inert electrodes (graphite or platinum) gives consistent, predictable products.\n'
                         '\n'
                         'NB — In aluminium extraction, the CARBON ANODES slowly BURN in the oxygen produced and must '
                         'be regularly replaced. This is one reason aluminium extraction is expensive.',
              'heading': 'Electrodes — Inert vs Reactive'}],
  'title': 'The Process of Electrolysis',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In molten ionic compounds, the METAL is always produced at the CATHODE (the negative electrode). '
                    'This is reduction — metal ions GAIN electrons. The NON-METAL is always produced at the ANODE '
                    '(positive electrode). This is oxidation — non-metal ions LOSE electrons.',
  'equations': ['2NaCl(l) → 2Na(l) + Cl₂(g)  (electrolysis of molten NaCl)',
                'PbBr₂(l) → Pb(l) + Br₂(g)  (electrolysis of molten lead bromide)',
                'Cathode: Na⁺ + e⁻ → Na',
                'Anode: 2Cl⁻ → Cl₂ + 2e⁻'],
  'fifas': [],
  'higher': None,
  'id': 'electrolysis-molten',
  'key_note': 'Molten ionic compound → only those ions present. Cathode: metal ion + electrons → metal. Anode: '
              'non-metal ions lose electrons → non-metal (gas or liquid). Molten NaCl → Na metal + Cl₂ gas. Molten '
              "PbBr₂ → Pb metal + Br₂. Solid won't conduct — ions must be mobile.",
  'matching': {'instruction': 'Match each electrode product to the correct electrolysis of a molten compound.',
               'pairs': [('Cathode — molten NaCl', 'Sodium metal (liquid) — Na⁺ ions gain electrons'),
                         ('Anode — molten NaCl', 'Chlorine gas (yellow-green) — Cl⁻ ions lose electrons'),
                         ('Cathode — molten PbBr₂', 'Lead metal (liquid) — Pb²⁺ ions gain 2 electrons each'),
                         ('Anode — molten PbBr₂', 'Bromine liquid/vapour (brown) — Br⁻ ions lose electrons')],
               'title': 'Products at Each Electrode'},
  'quiz': [{'opts': [('Calcium metal — Ca²⁺ ions are reduced at the negative cathode', True),
                     ('Chlorine gas — Cl⁻ ions are discharged at the cathode', False),
                     ('Calcium chloride — no decomposition occurs at the cathode', False),
                     ('Calcium oxide — the calcium combines with oxygen from the air', False)],
            'q': 'Molten calcium chloride (CaCl₂) is electrolysed. What is produced at the cathode?',
            'wrong_explanations': {1: 'Cl⁻ is NEGATIVE — it moves to the POSITIVE ANODE, not the cathode. The cathode '
                                      'attracts positive Ca²⁺ ions.',
                                   2: 'Electrolysis DOES decompose the compound — that is its purpose.',
                                   3: "Electrolysis is done in an enclosed container — calcium doesn't react with air "
                                      'at this stage. The product is pure calcium metal.'}},
           {'opts': [('In the solid, Pb²⁺ and Br⁻ ions are fixed — they cannot move to carry charge. Melting gives the '
                      'ions freedom to move.',
                      True),
                     ('Melting changes the chemical formula of lead bromide, making electrolysis possible.', False),
                     ('The electrodes cannot penetrate a solid — they need a liquid to make contact.', False),
                     ("Solid lead bromide doesn't contain ions — they form when it melts.", False)],
            'q': 'Why must lead bromide be melted before it can be electrolysed?',
            'wrong_explanations': {1: 'Melting does NOT change the chemical formula — PbBr₂ is still PbBr₂ whether '
                                      'solid or molten.',
                                   2: "In a proper setup, electrodes can contact a solid — but the solid still won't "
                                      "conduct electricity because the ions can't move.",
                                   3: 'Lead bromide is ionic in BOTH solid and molten states — Na⁺ and Cl⁻ (or Pb²⁺ '
                                      "and Br⁻) ions exist in the solid too. They just can't move."}}],
  'rp': 'RP4 (Chemistry) — Carry out electrolysis of lead(II) bromide. Observe products at each electrode. Safety: '
        'work in fume cupboard — bromine is toxic.',
  'spec': '5.4.3.2',
  'summary': 'Predict and explain the products of electrolysing molten ionic compounds.',
  'theory': [{'content': 'When a MOLTEN ionic compound is electrolysed, the ONLY ions present are those from the '
                         'compound itself.\n'
                         '\n'
                         'This makes prediction simple:\n'
                         'At the CATHODE (negative): the POSITIVE METAL ION is discharged → metal is deposited.\n'
                         'At the ANODE (positive): the NEGATIVE NON-METAL ION is discharged → non-metal element (often '
                         'a gas) is produced.\n'
                         '\n'
                         'Example — electrolysis of molten sodium chloride (NaCl):\n'
                         'Ions present: Na⁺ and Cl⁻ only.\n'
                         'Cathode: Na⁺ + e⁻ → Na (sodium metal produced — liquid, very reactive)\n'
                         'Anode: 2Cl⁻ → Cl₂ + 2e⁻ (chlorine gas produced — yellow-green, toxic)\n'
                         '\n'
                         'Example — electrolysis of molten lead bromide (PbBr₂):\n'
                         'Ions present: Pb²⁺ and Br⁻ only.\n'
                         'Cathode: Pb²⁺ + 2e⁻ → Pb (lead metal deposited)\n'
                         'Anode: 2Br⁻ → Br₂ + 2e⁻ (bromine liquid/vapour produced — brown)',
              'heading': 'Products from Molten Ionic Compounds'},
             {'content': 'SOLID ionic compounds have ions FIXED in the lattice — they cannot move → no electrolysis '
                         'possible.\n'
                         'MOLTEN ionic compounds have ions FREE TO MOVE → electrolysis can occur.\n'
                         '\n'
                         'Practical considerations:\n'
                         'Melting ionic compounds often requires very high temperatures.\n'
                         'NaCl melts at 801°C — very high energy input needed.\n'
                         'Special equipment and safety measures required.\n'
                         'This is why electrolysis is expensive for very reactive metal production.\n'
                         '\n'
                         'For ALUMINIUM: the compound is DISSOLVED in molten cryolite (not just melted on its own) to '
                         'lower the operating temperature from ~2050°C to ~950°C — still very high, but more '
                         'practically manageable.',
              'heading': 'Why Molten Rather Than Solid?'},
             {'content': 'Lead bromide is commonly used in school demonstrations:\n'
                         '\n'
                         'Before melting: no conductivity — ions fixed in solid.\n'
                         'After melting: circuit completes — ions free to move.\n'
                         '\n'
                         'CATHODE observations:\n'
                         'Grey metallic liquid appears at the negative electrode.\n'
                         'Lead forms as liquid (above its melting point at these temperatures).\n'
                         '\n'
                         'ANODE observations:\n'
                         'Reddish-brown bromine vapour produced at positive electrode.\n'
                         'Bromine is a brown liquid/red-brown vapour.\n'
                         '\n'
                         'OVERALL: PbBr₂(l) → Pb(l) + Br₂(g)\n'
                         '\n'
                         'Note: the solid lead bromide MUST be melted before any electrolysis occurs — a clear '
                         'observation of why ions must be mobile.',
              'heading': 'Observations During Electrolysis of Lead Bromide'}],
  'title': 'Electrolysis of Molten Ionic Compounds',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In copper purification, the IMPURE copper is the ANODE (it dissolves). The PURE copper builds up '
                    'on the CATHODE. Students often get these the wrong way round. The anions in the electrolyte '
                    '(SO₄²⁻) do not move to either electrode in copper purification — only copper ions are discharged.',
  'equations': ['Al³⁺ + 3e⁻ → Al  (cathode — aluminium extraction)',
                '2O²⁻ → O₂ + 4e⁻  (anode — aluminium extraction)',
                'Cu → Cu²⁺ + 2e⁻  (anode — copper purification)',
                'Cu²⁺ + 2e⁻ → Cu  (cathode — copper purification)'],
  'fifas': [],
  'higher': None,
  'id': 'electrolysis-extraction',
  'key_note': 'Aluminium extraction: molten Al₂O₃ in cryolite (lowers MP to ~950°C), graphite electrodes, Al deposited '
              'at cathode, O₂ at anode burns graphite anodes. Copper purification: impure Cu anode dissolves, pure Cu '
              'deposits at cathode, anode sludge contains precious metals. Electroplating: coat object (cathode) with '
              'thin metal layer.',
  'matching': {'instruction': 'Match each industrial use to the correct electrode behaviour.',
               'pairs': [('Aluminium extraction — cathode',
                          'Al³⁺ ions reduced → molten aluminium deposited and tapped off'),
                         ('Aluminium extraction — anode',
                          'O²⁻ ions oxidised → O₂ gas produced — burns graphite anodes'),
                         ('Copper purification — anode', 'Impure copper dissolves — Cu → Cu²⁺ + 2e⁻'),
                         ('Copper purification — cathode', 'Pure copper deposits — Cu²⁺ + 2e⁻ → Cu'),
                         ('Electroplating — cathode', 'Object being plated — metal ions deposit onto its surface')],
               'title': 'Match the Electrolysis Application'},
  'quiz': [{'opts': [('Oxygen produced at the anode reacts with the hot graphite: C + O₂ → CO₂ — the anode burns away',
                      True),
                     ('The anode dissolves into the aluminium oxide melt', False),
                     ('The high temperature melts and destroys the graphite', False),
                     ('Aluminium deposits on the anode, blocking it', False)],
            'q': 'Why does the graphite anode in aluminium extraction need to be replaced regularly?',
            'wrong_explanations': {1: 'Graphite does not dissolve ionically — it reacts CHEMICALLY with the oxygen '
                                      'produced at the anode.',
                                   2: 'Graphite melts at ~3600°C — well above the operating temperature of ~950°C. '
                                      'Physical melting is not the issue.',
                                   3: 'Aluminium is produced at the CATHODE (the graphite lining at the bottom) — it '
                                      "doesn't deposit on the anode."}},
           {'opts': [('Pure copper deposits — Cu²⁺ ions from solution gain electrons and form solid copper', True),
                     ('Impure copper dissolves — copper atoms lose electrons and enter solution', False),
                     ('Oxygen gas is produced — water is oxidised at the cathode', False),
                     ('Gold and silver from the anode deposit at the cathode', False)],
            'q': 'In copper purification by electrolysis, what happens at the cathode?',
            'wrong_explanations': {1: 'Impure copper DISSOLVING is what happens at the ANODE — Cu → Cu²⁺ + 2e⁻. The '
                                      'cathode is where Cu DEPOSITS.',
                                   2: 'Oxygen is produced at anodes when water is oxidised — in copper purification '
                                      'the anode reaction is Cu dissolving, not water oxidation.',
                                   3: 'Less reactive metals (Au, Ag) from the anode do NOT dissolve into solution — '
                                      'they fall as anode sludge. Only copper enters solution.'}}],
  'rp': None,
  'spec': '5.4.3.3',
  'summary': 'Describe how electrolysis is used to extract aluminium and purify copper.',
  'theory': [{'content': "Aluminium is the most abundant metal in the Earth's crust — but it is very reactive, making "
                         'it difficult to extract.\n'
                         '\n'
                         'Aluminium cannot be extracted by carbon reduction (it is above carbon in the reactivity '
                         'series).\n'
                         'Instead, electrolysis of MOLTEN ALUMINIUM OXIDE (Al₂O₃) is used.\n'
                         '\n'
                         'CHALLENGE: aluminium oxide melts at about 2050°C — impractically high.\n'
                         'SOLUTION: dissolve aluminium oxide in MOLTEN CRYOLITE (Na₃AlF₆).\n'
                         'Cryolite lowers the operating temperature to about 950°C.\n'
                         'Cryolite does not react and is recovered — it just acts as a solvent.\n'
                         '\n'
                         'ELECTROLYSIS PROCESS (Hall-Héroult process):\n'
                         'Molten Al₂O₃ in cryolite is placed in a large steel tank lined with graphite (acts as the '
                         'cathode).\n'
                         'Graphite anodes dip into the melt from above.\n'
                         '\n'
                         'At CATHODE (graphite lining):\n'
                         'Al³⁺ + 3e⁻ → Al (aluminium ions reduced to molten aluminium)\n'
                         'Molten aluminium sinks to the bottom and is tapped off.\n'
                         '\n'
                         'At ANODE (graphite rods):\n'
                         '2O²⁻ → O₂ + 4e⁻ (oxide ions oxidised to oxygen gas)\n'
                         '\n'
                         'PROBLEM WITH CARBON ANODES:\n'
                         'The oxygen produced at the anode reacts with the hot graphite anodes:\n'
                         'C + O₂ → CO₂\n'
                         'Anodes burn away and must be replaced regularly — an ongoing operational cost.',
              'heading': 'Extracting Aluminium by Electrolysis'},
             {'content': 'CRUDE COPPER from smelting contains impurities (zinc, iron, silver, gold) — too impure for '
                         'electrical wiring.\n'
                         'Electrolysis purifies it to 99.99% pure copper.\n'
                         '\n'
                         'SETUP:\n'
                         'ELECTROLYTE: copper sulfate solution (CuSO₄(aq)).\n'
                         'ANODE: impure copper — REACTIVE anode (dissolves).\n'
                         'CATHODE: pure copper or stainless steel — grows as copper deposits.\n'
                         '\n'
                         'AT THE ANODE (impure copper dissolves):\n'
                         'Cu → Cu²⁺ + 2e⁻ (copper atoms from impure anode dissolve into solution)\n'
                         'Less reactive impurities (gold, silver, platinum) do NOT dissolve — they fall as ANODE '
                         'SLUDGE at the bottom.\n'
                         '\n'
                         'AT THE CATHODE (pure copper deposits):\n'
                         'Cu²⁺ + 2e⁻ → Cu (copper ions from solution deposit as pure copper)\n'
                         '\n'
                         'RESULT:\n'
                         'The impure anode gradually dissolves.\n'
                         'Pure copper builds up on the cathode.\n'
                         'The concentration of Cu²⁺ in the CuSO₄ solution stays approximately constant.\n'
                         'The anode sludge is collected — it may contain valuable metals (gold, silver) that offset '
                         'costs.',
              'heading': 'Copper Purification by Electrolysis'},
             {'content': 'ELECTROPLATING uses electrolysis to coat an object with a thin layer of metal.\n'
                         '\n'
                         'Applications:\n'
                         'Decorative: gold or silver plating of jewellery, trophies.\n'
                         'Protective: chromium plating of car parts, zinc plating of steel (galvanising).\n'
                         'Functional: nickel plating for wear resistance.\n'
                         '\n'
                         'SETUP for silver plating a copper spoon:\n'
                         'ELECTROLYTE: silver nitrate solution (AgNO₃).\n'
                         'ANODE: silver (dissolves to replenish Ag⁺ ions in solution).\n'
                         'CATHODE: the copper spoon (coated with silver).\n'
                         '\n'
                         'AT CATHODE:\n'
                         'Ag⁺ + e⁻ → Ag (silver deposits on the spoon)\n'
                         '\n'
                         'AT ANODE:\n'
                         'Ag → Ag⁺ + e⁻ (silver anode dissolves, maintaining Ag⁺ concentration)\n'
                         '\n'
                         'The anode mass decreases and the cathode mass increases by the same amount.',
              'heading': 'Electroplating'}],
  'title': 'Using Electrolysis to Extract Metals',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In aqueous solutions, WATER provides H⁺ and OH⁻ ions that compete with the ions from the '
                    'dissolved salt. At the cathode: metals above hydrogen → H₂ is produced (not the metal). At the '
                    'anode: if no halide ions present → O₂ is produced (from OH⁻). Students often predict the wrong '
                    'product for Na⁺ at the cathode — sodium is so reactive it is NEVER deposited from aqueous '
                    'solution; hydrogen is produced instead.',
  'equations': ['Cathode: 2H⁺ + 2e⁻ → H₂  (hydrogen from water/dilute acid)',
                'Anode: 4OH⁻ → O₂ + 2H₂O + 4e⁻  (oxygen from water)',
                'Anode: 2Cl⁻ → Cl₂ + 2e⁻  (chlorine from brine)',
                'Cathode: Cu²⁺ + 2e⁻ → Cu  (copper from CuSO₄)'],
  'fifas': [],
  'higher': None,
  'id': 'electrolysis-aqueous',
  'key_note': 'Aqueous solutions: ions from salt AND H⁺/OH⁻ from water compete. Cathode: metal below H → metal '
              'deposited; metal above H → H₂. Anode: Cl⁻ in high conc → Cl₂; otherwise → O₂. Brine (NaCl) → H₂ '
              '(cathode) + Cl₂ (anode) + NaOH (solution) — chlor-alkali process.',
  'matching': {'instruction': 'Match each aqueous solution to its products at cathode and anode.',
               'pairs': [('Dilute H₂SO₄', 'Cathode: H₂ gas. Anode: O₂ gas. (No metal ions below H, no halide ions)'),
                         ('CuSO₄ solution', 'Cathode: Cu metal deposited. Anode: O₂ gas. (Cu below H; no halide)'),
                         ('Concentrated NaCl (brine)', 'Cathode: H₂ gas. Anode: Cl₂ gas. (Na above H; high Cl⁻ conc)'),
                         ('Dilute NaCl', 'Cathode: H₂ gas. Anode: O₂ gas. (Na above H; low Cl⁻ conc → O₂ preferred)')],
               'title': 'Predict the Electrolysis Products'},
  'quiz': [{'opts': [('Copper metal — Cu²⁺ ions are below hydrogen in the reactivity series and are preferentially '
                      'discharged',
                      True),
                     ('Hydrogen gas — water provides H⁺ ions which are always discharged at the cathode', False),
                     ('Sulfur dioxide — SO₄²⁻ ions are discharged at the cathode', False),
                     ('Oxygen — OH⁻ ions from water are discharged at the cathode', False)],
            'q': 'Copper sulfate solution is electrolysed with inert electrodes. What is produced at the cathode?',
            'wrong_explanations': {1: 'H⁺ ions ARE present — but Cu²⁺ is LESS REACTIVE than H⁺ (copper is below '
                                      'hydrogen in the series), so Cu²⁺ is preferentially discharged.',
                                   2: 'SO₄²⁻ is a very stable ion — it is NOT discharged at the cathode or anode under '
                                      'normal conditions.',
                                   3: 'O₂ is produced at the ANODE (from OH⁻ oxidation), not the cathode.'}},
           {'opts': [('Chlorine gas — high concentration of Cl⁻ ions means they are preferentially discharged over OH⁻',
                      True),
                     ('Oxygen gas — OH⁻ ions from water are always discharged at the anode', False),
                     ('Sodium metal — Na⁺ ions are discharged at the anode', False),
                     ('Hydrogen gas — H⁺ ions from water are discharged at the anode', False)],
            'q': 'Concentrated brine (sodium chloride solution) is electrolysed. What is produced at the anode?',
            'wrong_explanations': {1: 'O₂ IS produced if the Cl⁻ concentration is LOW — but in CONCENTRATED brine, the '
                                      'high Cl⁻ concentration favours Cl₂ production.',
                                   2: 'Na⁺ is a positive ion — it moves to the CATHODE (negative electrode), not the '
                                      'anode.',
                                   3: 'H⁺ is discharged at the CATHODE (negative) — positive ions always move to the '
                                      'cathode.'}}],
  'rp': 'RP4 (Chemistry) — Investigate the electrolysis of aqueous solutions. Test products: H₂ with lit splint '
        '(squeaky pop), O₂ with glowing splint (relights), Cl₂ with damp litmus (bleaches it).',
  'spec': '5.4.3.4',
  'summary': 'Predict products of electrolysing aqueous solutions and explain why water adds complexity.',
  'theory': [{'content': 'When an ionic compound is DISSOLVED in water, the solution contains:\n'
                         'Ions from the ionic compound, AND\n'
                         'H⁺ and OH⁻ ions from water (water partially ionises: H₂O ⇌ H⁺ + OH⁻).\n'
                         '\n'
                         'At each electrode, there are COMPETING IONS — more than one type of ion that could be '
                         'discharged.\n'
                         '\n'
                         'The ion that is actually discharged depends on:\n'
                         '1. POSITION IN THE REACTIVITY SERIES — less reactive ions are discharged preferentially.\n'
                         '2. CONCENTRATION — a high concentration of an ion favours its discharge.\n'
                         '\n'
                         'At the CATHODE (reduction):\n'
                         'If the metal is BELOW hydrogen in the series → metal is deposited.\n'
                         'If the metal is ABOVE hydrogen in the series → hydrogen gas (H₂) is produced (from H⁺ '
                         'ions).\n'
                         '\n'
                         'At the ANODE (oxidation):\n'
                         'If Cl⁻ ions are present in HIGH concentration → chlorine gas (Cl₂) produced.\n'
                         'If no Cl⁻ (or low concentration) → oxygen gas (O₂) produced (from OH⁻ ions from water).',
              'heading': 'Why Aqueous Solutions Are More Complex'},
             {'content': 'DILUTE SULFURIC ACID (H₂SO₄(aq)) with inert electrodes:\n'
                         'Ions: H⁺, OH⁻, SO₄²⁻.\n'
                         'Cathode: H⁺ + e⁻ → H₂ (hydrogen produced — SO₄²⁻ not discharged, too stable)\n'
                         'Anode: 4OH⁻ → O₂ + 2H₂O (oxygen produced)\n'
                         'Ratio: 2 volumes H₂ for every 1 volume O₂ (2:1 ratio)\n'
                         '\n'
                         'CUPROUS SULFATE SOLUTION (CuSO₄(aq)) with inert electrodes:\n'
                         'Ions: Cu²⁺, SO₄²⁻, H⁺, OH⁻.\n'
                         'Cathode: Cu²⁺ preferred over H⁺ (copper is below hydrogen, less reactive) → copper '
                         'deposited.\n'
                         'Anode: OH⁻ discharged → oxygen gas.\n'
                         '\n'
                         'CONCENTRATED SODIUM CHLORIDE (brine: NaCl(aq)) with inert electrodes:\n'
                         'Ions: Na⁺, Cl⁻, H⁺, OH⁻.\n'
                         'Cathode: H⁺ preferred over Na⁺ (Na is far above hydrogen, very reactive) → hydrogen gas '
                         'produced.\n'
                         'Anode: Cl⁻ in high concentration → CHLORINE gas produced (not O₂ — Cl⁻ concentration '
                         'effect).\n'
                         'Remaining solution: Na⁺ and OH⁻ → sodium hydroxide (NaOH) — important industrial product.\n'
                         '\n'
                         'This is the CHLOR-ALKALI process — produces chlorine, hydrogen and sodium hydroxide — all '
                         'valuable chemicals.',
              'heading': 'Electrolysis of Key Aqueous Solutions'},
             {'content': "CATHODE RULE (what's produced at the negative electrode):\n"
                         'Metal ions below hydrogen in series (Cu²⁺, Ag⁺, Au³⁺) → METAL deposited.\n'
                         'Metal ions above hydrogen in series (Na⁺, K⁺, Ca²⁺, Mg²⁺, Al³⁺, Zn²⁺, Fe²⁺) → HYDROGEN gas '
                         '(H₂) produced.\n'
                         '\n'
                         "ANODE RULE (what's produced at the positive electrode):\n"
                         'If halide ions present (Cl⁻, Br⁻, I⁻) AND in high concentration → HALOGEN gas (Cl₂, Br₂, '
                         'I₂).\n'
                         'Otherwise → OXYGEN gas (O₂) from OH⁻ ions in water.\n'
                         '\n'
                         'IMPORTANT INDUSTRIAL PRODUCTS from electrolysis:\n'
                         'CHLORINE — from brine (NaCl solution). Used in PVC, disinfectants, bleach.\n'
                         'HYDROGEN — from brine. Used in Haber process, fuel cells.\n'
                         'SODIUM HYDROXIDE — from brine. Used in paper making, soap, cleaning products.\n'
                         'ALUMINIUM — from molten Al₂O₃ in cryolite.\n'
                         'OXYGEN — from water/dilute sulfuric acid.',
              'heading': 'Products Summary and Rules'}],
  'title': 'Electrolysis of Aqueous Solutions',
  'triple_only': None,
  'variables': []}],

"energy-changes": [{'common_mistake': 'EXOTHERMIC reactions make the surroundings HOTTER (temperature rises). ENDOTHERMIC reactions make '
                    'the surroundings COLDER (temperature falls). The reaction itself releases or absorbs energy — but '
                    'the SURROUNDINGS show the opposite effect to what the reaction does. Also: ΔH is NEGATIVE for '
                    "exothermic (releases energy) — students often think negative means the reaction is 'losing "
                    "energy' in a bad way — it just means energy is released.",
  'equations': ['Q = m × c × ΔT'],
  'fifas': [{'label': 'Calorimetry Calculation',
             'question': '50 g of water is heated by a reaction. The temperature rises from 20°C to 34°C. Calculate '
                         'the energy released. (c = 4.18 J/g°C)',
             'steps': [('F', 'Q = m × c × ΔT'),
                       ('I', 'm = 50 g, c = 4.18 J/g°C, ΔT = 34 − 20 = 14°C'),
                       ('F', 'Q = 50 × 4.18 × 14 = 50 × 58.52'),
                       ('A', 'Q = 2926 J ≈ 2930 J (exothermic — temperature rose)')]}],
  'higher': None,
  'id': 'exothermic-endothermic',
  'key_note': 'Exothermic: releases heat → temperature rises → examples: combustion, neutralisation, respiration. '
              'Endothermic: absorbs heat → temperature falls → examples: thermal decomposition, dissolving ammonium '
              'nitrate, photosynthesis. Q = mcΔT for calorimetry.',
  'matching': {'instruction': 'Sort each reaction into exothermic or endothermic.',
               'pairs': [('Exothermic', 'Burning methane in air — releases heat and light'),
                         ('Endothermic', 'Thermal decomposition of calcium carbonate — absorbs heat energy'),
                         ('Exothermic', 'Neutralisation of NaOH with HCl — temperature of solution rises'),
                         ('Endothermic', 'Dissolving ammonium nitrate in water — temperature of solution falls'),
                         ('Exothermic', 'Respiration — glucose + oxygen releases energy in cells'),
                         ('Endothermic', 'Photosynthesis — absorbs light energy to make glucose')],
               'title': 'Exothermic or Endothermic?'},
  'quiz': [{'opts': [('Exothermic — energy is released to the surroundings, raising the temperature', True),
                     ('Endothermic — energy is absorbed, warming the hand from within', False),
                     ('Neither — hand warmers use electrical energy, not chemical reactions', False),
                     ('Endothermic — the hand warmer absorbs heat from the hand', False)],
            'q': 'A hand warmer gets hot when activated. What type of reaction is occurring inside?',
            'wrong_explanations': {1: 'Endothermic reactions take IN heat from the surroundings — they make things '
                                      'colder, not warmer. Hand warmers get hot because they are exothermic.',
                                   2: 'Most disposable hand warmers use a chemical reaction (e.g. iron oxidation) — '
                                      'not electricity.',
                                   3: 'A hand warmer RELEASES heat to the hand — the reaction inside is exothermic '
                                      '(releases energy).'}},
           {'opts': [('3344 J — Q = 100 × 4.18 × 8', True),
                     ('836 J — Q = 100 × 4.18 × 2', False),
                     ('3340 J — temperature change forgotten, used 8.18 instead', False),
                     ('41800 J — forgot to use the temperature change', False)],
            'q': '100 g of solution is heated in a calorimetry experiment. Temperature rises from 22°C to 30°C. Using '
                 'c = 4.18 J/g°C, how much energy was released?',
            'wrong_explanations': {1: 'ΔT = 30 − 22 = 2 — not 8. The temperature change is the difference: 30 − 22 = '
                                      '8°C.',
                                   2: 'Calculation partially correct but wrong ΔT value used — not a standard error in '
                                      'the formula.',
                                   3: 'Must use Q = m × c × ΔT = 100 × 4.18 × 8 = 3344 J. Cannot use just mass × '
                                      'specific heat capacity.'}}],
  'rp': 'RP5 (Chemistry) — Investigate the variables that affect temperature changes in reactions: e.g. neutralisation '
        'of NaOH with HCl, or dissolving ammonium chloride in water.',
  'spec': '5.5.1.1',
  'summary': 'Define exothermic and endothermic reactions, give examples and describe their energy changes.',
  'theory': [{'content': 'An EXOTHERMIC reaction RELEASES energy to the surroundings — usually as HEAT, sometimes as '
                         'light or sound.\n'
                         '\n'
                         'The products have LESS energy than the reactants — energy is given out to the surroundings.\n'
                         'The TEMPERATURE of the surroundings INCREASES.\n'
                         '\n'
                         'EXAMPLES of exothermic reactions:\n'
                         'COMBUSTION — burning fuels (methane, petrol, wood): releases heat and light.\n'
                         'OXIDATION of metals — iron rusting (slow, releases heat gradually).\n'
                         'NEUTRALISATION — acid + alkali → salt + water (temperature rises).\n'
                         'RESPIRATION — glucose + oxygen → CO₂ + water (releases energy in cells).\n'
                         'HANDWARMERS — iron oxidation or sodium acetate crystallisation.\n'
                         'SELF-HEATING CANS — reaction between calcium oxide and water.\n'
                         '\n'
                         'Temperature change: ΔT is POSITIVE (temperature rises).\n'
                         'Energy change: ΔH is NEGATIVE for exothermic reactions (energy released).',
              'heading': 'Exothermic Reactions'},
             {'content': 'An ENDOTHERMIC reaction ABSORBS energy from the surroundings — usually as HEAT.\n'
                         '\n'
                         'The products have MORE energy than the reactants — energy is taken in from the '
                         'surroundings.\n'
                         'The TEMPERATURE of the surroundings DECREASES (the surroundings get cooler).\n'
                         '\n'
                         'EXAMPLES of endothermic reactions:\n'
                         'THERMAL DECOMPOSITION — heating calcium carbonate: CaCO₃ → CaO + CO₂.\n'
                         'DISSOLVING ammonium nitrate in water (temperature drops — used in instant cold packs).\n'
                         'PHOTOSYNTHESIS — CO₂ + H₂O → glucose + O₂ (absorbs light energy).\n'
                         'COOKING — baking bread, boiling eggs (energy absorbed to cook food).\n'
                         'INSTANT ICE PACKS — ammonium nitrate dissolving in water.\n'
                         'CITRIC ACID + SODIUM BICARBONATE reaction in baking powders.\n'
                         '\n'
                         'Temperature change: ΔT is NEGATIVE (temperature falls).\n'
                         'Energy change: ΔH is POSITIVE for endothermic reactions (energy absorbed).',
              'heading': 'Endothermic Reactions'},
             {'content': 'CALORIMETRY is the method for measuring heat energy changes in reactions.\n'
                         '\n'
                         'SIMPLE CALORIMETRY:\n'
                         'Reaction takes place in a polystyrene cup (good insulator).\n'
                         'Measure the temperature change (ΔT) of the water or solution.\n'
                         'Calculate energy change: Q = mcΔT\n'
                         'Where: m = mass of solution (g), c = specific heat capacity (4.18 J/g°C for water), ΔT = '
                         'temperature change (°C).\n'
                         '\n'
                         'Exothermic: temperature rises → ΔT is positive → Q is positive (heat released).\n'
                         'Endothermic: temperature falls → ΔT is negative → Q is negative (heat absorbed).\n'
                         '\n'
                         'SOURCES OF ERROR in calorimetry:\n'
                         'HEAT LOSS to the surroundings and container → underestimates energy released.\n'
                         'INCOMPLETE combustion → less heat released than expected.\n'
                         'Using polystyrene cup reduces heat loss compared to a beaker.\n'
                         '\n'
                         'Using these measurements, scientists can calculate the ENERGY PER MOLE for a reaction — the '
                         'molar enthalpy change.',
              'heading': 'Measuring Energy Changes'}],
  'title': 'Exothermic and Endothermic Reactions',
  'triple_only': None,
  'variables': [('Q', 'Heat energy transferred', 'joules', 'J'),
                ('m', 'Mass of solution', 'grams', 'g'),
                ('c', 'Specific heat capacity', 'J/g°C', 'J/g°C'),
                ('ΔT', 'Temperature change', '°C', '°C')]},
 {'common_mistake': 'The activation energy is measured from the REACTANT level to the PEAK — NOT from the reactant '
                    'level to the product level. The overall energy change (ΔH) is from reactants to PRODUCTS. These '
                    'are two different measurements on the same diagram. Students often confuse them.',
  'equations': ['ΔH = energy of products − energy of reactants',
                'Activation energy = energy of peak − energy of reactants'],
  'fifas': [],
  'higher': None,
  'id': 'reaction-profiles',
  'key_note': 'Reaction profile: x = reaction progress, y = energy. Exothermic: products LOWER than reactants (ΔH '
              'negative). Endothermic: products HIGHER than reactants (ΔH positive). Activation energy = reactant '
              'level to peak. Catalyst: lower peak, same reactant/product levels, same ΔH.',
  'matching': {'instruction': 'Match each feature of a reaction profile to its description.',
               'pairs': [('Activation energy', 'Energy gap from reactant level up to the peak of the curve'),
                         ('ΔH (exothermic)', 'Products are lower than reactants — energy released — ΔH is negative'),
                         ('ΔH (endothermic)', 'Products are higher than reactants — energy absorbed — ΔH is positive'),
                         ('Effect of catalyst',
                          'Lowers the peak — lower activation energy — same ΔH — faster reaction')],
               'title': 'Reaction Profile Features'},
  'quiz': [{'opts': [('−30 kJ — products (50) − reactants (80) = −30 kJ — exothermic reaction', True),
                     ('+30 kJ — reactants (80) − products (50) = +30 kJ', False),
                     ('+130 kJ — adding reactant and product energies', False),
                     ('−80 kJ — the reactant energy is lost', False)],
            'q': 'On a reaction profile, the reactants are at 80 kJ and the products are at 50 kJ. What is ΔH?',
            'wrong_explanations': {1: 'ΔH = products − reactants = 50 − 80 = −30. Positive 30 would mean products are '
                                      'HIGHER than reactants — but here products (50) are lower than reactants (80).',
                                   2: 'Adding energies gives a meaningless value — ΔH = products MINUS reactants.',
                                   3: "The reactant energy of 80 kJ is not 'lost' — ΔH shows the NET energy change "
                                      'from reactants to products.'}},
           {'opts': [('The activation energy peak is lower — but reactant and product energy levels and ΔH stay the '
                      'same',
                      True),
                     ('The reactant energy level increases — they become more energetic', False),
                     ('Both the activation energy and ΔH decrease', False),
                     ('The product energy level increases — products formed are higher energy', False)],
            'q': 'A catalyst is added to a reaction. What changes on the reaction profile?',
            'wrong_explanations': {1: 'Catalysts do not give reactants more energy — they provide an ALTERNATIVE '
                                      'PATHWAY with a lower energy barrier.',
                                   2: 'ΔH (the overall energy change) is NOT changed by a catalyst — only the '
                                      'activation energy peak is lowered.',
                                   3: 'Products are the same compounds regardless of whether a catalyst is used — '
                                      "their energy level doesn't change."}}],
  'rp': None,
  'spec': '5.5.1.2',
  'summary': 'Draw and interpret reaction profile diagrams for exothermic and endothermic reactions.',
  'theory': [{'content': 'A REACTION PROFILE (also called an energy profile diagram) shows how the ENERGY of the '
                         'system changes as a reaction progresses.\n'
                         '\n'
                         'The x-axis shows PROGRESS OF REACTION (from reactants to products).\n'
                         'The y-axis shows ENERGY (in kJ or kJ/mol).\n'
                         '\n'
                         'Key features on every reaction profile:\n'
                         'REACTANTS — the starting energy level (left).\n'
                         'PRODUCTS — the final energy level (right).\n'
                         'ACTIVATION ENERGY (Ea) — the energy barrier that must be overcome for the reaction to start '
                         '— shown as the PEAK of the curve above the reactant level.\n'
                         'OVERALL ENERGY CHANGE (ΔH) — the difference in energy between reactants and products.',
              'heading': 'What is a Reaction Profile?'},
             {'content': 'EXOTHERMIC REACTION PROFILE:\n'
                         'Products are at a LOWER energy level than reactants.\n'
                         'The curve rises to a peak (activation energy) then falls below the reactant level.\n'
                         'ΔH is NEGATIVE (products lower than reactants — energy released).\n'
                         'The difference between the peak and the REACTANT energy level = activation energy.\n'
                         '\n'
                         'ENDOTHERMIC REACTION PROFILE:\n'
                         'Products are at a HIGHER energy level than reactants.\n'
                         'The curve rises to a peak (activation energy) then falls — but levels off ABOVE the reactant '
                         'starting point.\n'
                         'ΔH is POSITIVE (products higher than reactants — energy absorbed).\n'
                         'The difference between the peak and the REACTANT energy level = activation energy.\n'
                         '\n'
                         'ACTIVATION ENERGY:\n'
                         'All reactions need activation energy to get started — even exothermic ones.\n'
                         'Activation energy = minimum energy needed to break existing bonds and start the reaction.\n'
                         'Low activation energy → fast reaction.\n'
                         'High activation energy → slow reaction (even if very exothermic once started).',
              'heading': 'Exothermic and Endothermic Profiles'},
             {'content': 'A CATALYST provides an ALTERNATIVE REACTION PATHWAY with a LOWER ACTIVATION ENERGY.\n'
                         '\n'
                         'On a reaction profile, adding a catalyst:\n'
                         'LOWERS the peak of the curve (lower activation energy hump).\n'
                         'Does NOT change the energy levels of reactants or products.\n'
                         'Does NOT change ΔH — the overall energy change is the same.\n'
                         '\n'
                         'This means:\n'
                         'More molecules have enough energy to react → faster reaction rate.\n'
                         'The same overall energy is released or absorbed per mole of reaction.\n'
                         '\n'
                         'Why catalysts are important:\n'
                         'Without catalysts, many industrially and biologically important reactions would be too slow '
                         'to be useful.\n'
                         'In biology, ENZYMES act as biological catalysts — lowering activation energy of specific '
                         'reactions.\n'
                         'In industry, transition metals (iron, platinum, nickel) are common catalysts.\n'
                         '\n'
                         'A lower activation energy hump on a reaction profile diagram represents a CATALYSED '
                         'reaction.',
              'heading': 'Effect of Catalysts on Reaction Profiles'}],
  'title': 'Reaction Profiles',
  'triple_only': None,
  'variables': [('Ea', 'Activation energy', 'kJ/mol', 'kJ/mol'),
                ('ΔH', 'Overall energy change (enthalpy change)', 'kJ/mol', 'kJ/mol')]}],

"rates-equilibrium": [{'common_mistake': 'The rate DECREASES over time in a closed system as REACTANTS ARE USED UP — fewer reactant '
                    'particles mean fewer collisions. The graph flattens out when the reaction is complete (all '
                    'reactants used). A steeper initial gradient = faster initial rate.',
  'equations': ['Rate = quantity of product formed (or reactant used) ÷ time',
                'Rate = gradient of graph of quantity vs time'],
  'fifas': [{'label': 'Rate Calculation',
             'question': 'A reaction between calcium carbonate and HCl produces 84 cm³ of CO₂ in 60 seconds. Calculate '
                         'the mean rate of reaction.',
             'steps': [('F', 'Rate = quantity of product ÷ time'),
                       ('I', 'Rate = 84 cm³ ÷ 60 s'),
                       ('F', 'Rate = 1.4'),
                       ('A', 'Rate = 1.4 cm³/s')]}],
  'higher': None,
  'id': 'calculating-rates',
  'key_note': 'Rate = quantity ÷ time. Units: cm³/s, g/s, mol/dm³/s. Rate = gradient of quantity-vs-time graph. '
              'Steeper = faster. Rate decreases over time (reactants used up). Mean rate = total ÷ total time. '
              'Instantaneous rate = tangent gradient at a point.',
  'matching': {'instruction': 'Match each term to its correct definition.',
               'pairs': [('Rate of reaction',
                          'How quickly reactants are used up or products are formed — quantity ÷ time'),
                         ('Steep gradient on graph', 'Fast rate — large quantity produced in short time'),
                         ('Flat gradient on graph', 'Slow rate or reaction complete — little change per unit time'),
                         ('Mean rate', 'Total quantity produced ÷ total time taken for reaction'),
                         ('Instantaneous rate', 'Gradient of tangent drawn at a specific point on the curve')],
               'title': 'Rate of Reaction Concepts'},
  'quiz': [{'opts': [('0.5 cm³/s — rate = 120 ÷ (4 × 60) = 120 ÷ 240', True),
                     ('30 cm³/s — rate = 120 ÷ 4', False),
                     ('480 cm³/s — rate = 120 × 4', False),
                     ('2 cm³/s — rate = 120 ÷ 60', False)],
            'q': 'A reaction produces 120 cm³ of gas in 4 minutes. What is the mean rate of reaction in cm³/s?',
            'wrong_explanations': {1: '4 minutes = 4 minutes — not converted to seconds. Rate in cm³/s requires time '
                                      'in seconds: 4 × 60 = 240 s.',
                                   2: 'This multiplies instead of divides.',
                                   3: 'This divides by 60 (seconds in a minute) but should divide by total seconds = 4 '
                                      '× 60 = 240.'}},
           {'opts': [('A faster rate of reaction — more product is being formed per unit time', True),
                     ('A slower rate — steeper means the reaction is taking longer', False),
                     ('The reaction is complete — no more gas is produced', False),
                     ('More reactant has been added — the amount of gas increases', False)],
            'q': 'On a graph of gas volume vs time, what does a steeper gradient indicate?',
            'wrong_explanations': {1: 'Steeper gradient = larger volume change per unit time = FASTER, not slower '
                                      'rate.',
                                   2: 'A FLAT (horizontal) gradient means the reaction is complete — no more gas being '
                                      'produced.',
                                   3: 'Adding more reactant might increase total gas produced — but gradient '
                                      '(steepness) represents RATE, not quantity.'}}],
  'rp': 'RP6 (Chemistry) — Investigate the effect of concentration on the rate of reaction between sodium thiosulfate '
        'and hydrochloric acid (cross disappears). Alternatively: rate of reaction between marble chips and HCl by '
        'mass loss or gas collection.',
  'spec': '5.6.1.1',
  'summary': 'Define rate of reaction and calculate it from experimental data.',
  'theory': [{'content': 'The RATE OF REACTION measures how quickly reactants are used up or products are formed.\n'
                         '\n'
                         'FAST reactions: explosions, burning, acid + reactive metal.\n'
                         'SLOW reactions: rusting, paint drying, decay.\n'
                         '\n'
                         'Rate can be measured by monitoring:\n'
                         'The DECREASE in mass of reactants over time.\n'
                         'The INCREASE in mass or volume of products over time.\n'
                         'The DECREASE in concentration of a reactant.\n'
                         'The INCREASE in concentration of a product.\n'
                         'The amount of GAS PRODUCED per unit time.\n'
                         'The CHANGE IN COLOUR or TURBIDITY (cloudiness) over time.',
              'heading': 'What is Rate of Reaction?'},
             {'content': 'RATE OF REACTION formula:\n'
                         'Rate = quantity of reactant used or product formed ÷ time\n'
                         '\n'
                         'Units depend on what is measured:\n'
                         'If measuring VOLUME of gas: rate = cm³/s or cm³/min.\n'
                         'If measuring MASS: rate = g/s or g/min.\n'
                         'If measuring CONCENTRATION: rate = mol/dm³/s.\n'
                         '\n'
                         'From a GRAPH:\n'
                         'The GRADIENT (slope) of a graph of quantity vs time = the rate at that point.\n'
                         'Steep gradient → fast rate.\n'
                         'Flat gradient → slow rate (or reaction finished).\n'
                         'The gradient DECREASES over time as reactants are used up.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'A reaction produces 60 cm³ of gas in 120 seconds.\n'
                         'Rate = 60 ÷ 120 = 0.5 cm³/s\n'
                         '\n'
                         'MEAN RATE vs INSTANTANEOUS RATE:\n'
                         'MEAN RATE = total quantity ÷ total time (average over the whole reaction).\n'
                         'INSTANTANEOUS RATE = gradient of a tangent to the curve at a specific point in time.',
              'heading': 'Calculating Rate of Reaction'},
             {'content': 'Common experimental methods for measuring rate:\n'
                         '\n'
                         'GAS COLLECTION:\n'
                         'Collect gas produced over water in an inverted measuring cylinder, or in a gas syringe.\n'
                         'Measure volume of gas collected at regular time intervals.\n'
                         'Plot volume vs time → gradient = rate.\n'
                         'Example: Mg + 2HCl → MgCl₂ + H₂ (measure H₂ collected).\n'
                         '\n'
                         'MASS LOSS:\n'
                         'Place reaction flask on a balance.\n'
                         'CO₂ escapes → mass decreases.\n'
                         'Record mass at regular intervals.\n'
                         'Example: CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂ (measure mass loss).\n'
                         '\n'
                         'COLOUR CHANGE / TURBIDITY:\n'
                         'For reactions involving a colour change — measure colour intensity with a colorimeter.\n'
                         'For precipitation reactions — observe when a mark under the flask becomes invisible.\n'
                         'Example: sodium thiosulfate + HCl → sulfur precipitate clouds the solution.\n'
                         'Time taken for the cross to disappear → inversely proportional to rate.',
              'heading': 'Measuring Rate Experimentally'}],
  'title': 'Rate of Reaction and Calculations',
  'triple_only': None,
  'variables': [('rate', 'Rate of reaction', 'cm³/s or g/s', '')]},
 {'common_mistake': 'All four factors (temperature, concentration, surface area, pressure for gases) increase rate by '
                    'increasing the NUMBER OF SUCCESSFUL COLLISIONS. Temperature is special — it also increases the '
                    'PROPORTION of particles with sufficient energy (≥ activation energy), making it particularly '
                    'effective. Always explain in terms of collisions.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'factors-affecting-rate',
  'key_note': 'Higher temperature → faster particles, more collisions, more above activation energy. Higher '
              'concentration → more particles per volume, more collisions. Larger surface area → more exposed '
              'particles, more collisions. Higher pressure (gases) → more particles per volume, more collisions. All '
              'increase rate by increasing successful collisions.',
  'matching': {'instruction': 'Match each factor change to its effect on reaction rate and why.',
               'pairs': [('Increase temperature',
                          'Rate increases — more particles exceed activation energy, more frequent and more energetic '
                          'collisions'),
                         ('Increase concentration',
                          'Rate increases — more particles per unit volume, more frequent collisions'),
                         ('Use powder instead of lumps',
                          'Rate increases — greater surface area exposes more particles to collisions'),
                         ('Increase pressure (gases)',
                          'Rate increases — gas particles compressed into smaller volume, more frequent collisions'),
                         ('Decrease temperature',
                          'Rate decreases — fewer particles have enough energy to react successfully')],
               'title': 'Factor → Effect on Rate'},
  'quiz': [{'opts': [('A greater proportion of particles now have energy ≥ the activation energy — so more collisions '
                      'are successful',
                      True),
                     ('Higher temperature makes particles larger — they collide more easily', False),
                     ('Higher temperature dissolves more of the solid reactants — increasing concentration', False),
                     ('Temperature has no extra effect — it only increases collision frequency', False)],
            'q': 'Why does increasing temperature increase reaction rate more than just increasing the frequency of '
                 'collisions?',
            'wrong_explanations': {1: "Particles don't change size with temperature — they move faster.",
                                   2: 'This might apply in some specific cases but is not the general reason why '
                                      'temperature increases rate — the key is the energy distribution.',
                                   3: 'Temperature does more than increase frequency — it shifts the energy '
                                      'distribution so MORE particles exceed the activation energy threshold.'}},
           {'opts': [('Rate increases — powder has much greater surface area, more particle collisions per unit time',
                      True),
                     ('Rate stays the same — same mass of marble is used', False),
                     ('Rate decreases — powder dissolves faster so there are fewer particles overall', False),
                     ('Rate increases because powder has less activation energy than chips', False)],
            'q': 'Marble chips (CaCO₃) react with HCl. The experiment is repeated with the same mass of powdered '
                 'marble. How does the rate change?',
            'wrong_explanations': {1: 'Same MASS does not mean same rate — rate depends on SURFACE AREA. Powder has '
                                      'enormously more surface area than chips.',
                                   2: 'Powder dissolving faster IS the result of faster rate — the mechanism is '
                                      'increased surface area for collisions.',
                                   3: 'Activation energy is a property of the reaction, not the physical form of the '
                                      'reactant. Powder and chips have the same activation energy.'}}],
  'rp': 'RP6 (Chemistry) — Investigate effect of concentration on rate (Na₂S₂O₃ + HCl). Can also investigate surface '
        'area (marble chips vs powder with HCl) or temperature effects.',
  'spec': '5.6.1.2',
  'summary': 'Describe and explain how temperature, concentration, surface area and pressure affect reaction rate.',
  'theory': [{'content': 'INCREASING TEMPERATURE increases reaction rate.\n'
                         '\n'
                         'Why:\n'
                         'Particles have MORE kinetic energy → move FASTER.\n'
                         'More frequent collisions (more collisions per second).\n'
                         'MORE IMPORTANTLY: a greater PROPORTION of particles have energy ≥ the activation energy.\n'
                         'More successful collisions → faster rate.\n'
                         '\n'
                         'Rule of thumb: increasing temperature by 10°C approximately DOUBLES the rate of many '
                         'reactions.\n'
                         '\n'
                         'DECREASING TEMPERATURE slows the reaction rate — used in food preservation (refrigeration '
                         'slows bacterial growth and chemical spoilage).\n'
                         '\n'
                         'Temperature has a BIGGER effect than just increasing collision frequency — it mainly '
                         'increases the proportion of successful (high-energy) collisions.',
              'heading': 'Temperature'},
             {'content': 'INCREASING CONCENTRATION of a solution increases reaction rate.\n'
                         '\n'
                         'Why:\n'
                         'More particles in the same volume.\n'
                         'Particles are closer together.\n'
                         'More frequent collisions per unit time.\n'
                         'More successful collisions → faster rate.\n'
                         '\n'
                         'Example: doubling concentration approximately doubles the number of collisions.\n'
                         '\n'
                         'INCREASING PRESSURE of GASES increases reaction rate:\n'
                         'Gas particles are compressed into a smaller volume.\n'
                         'Particles are closer together.\n'
                         'More frequent collisions → faster rate.\n'
                         'Same principle as increasing concentration — more particles per unit volume.\n'
                         '\n'
                         'Note: pressure only affects GASEOUS reactions — has no significant effect on reactions in '
                         'solution.',
              'heading': 'Concentration and Pressure'},
             {'content': 'INCREASING SURFACE AREA (by using smaller pieces/powder) increases reaction rate.\n'
                         '\n'
                         'Why:\n'
                         'More surface area exposed to reactant particles.\n'
                         'More collisions possible per unit time.\n'
                         'More of the reactant is accessible → faster rate.\n'
                         '\n'
                         'This is why POWDERS react faster than LUMPS of the same mass:\n'
                         'A 1 g marble chip: small surface area → slow reaction with acid.\n'
                         'The same 1 g crushed to powder: massive increase in surface area → much faster reaction with '
                         'acid.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Powdered coal dust is EXPLOSIVE — high surface area. Lump coal burns slowly.\n'
                         'Flour dust in mills can cause explosions.\n'
                         'Coal fires — smaller pieces of coal burn faster.\n'
                         '\n'
                         'Surface area investigation: marble chips vs powder in HCl — compare gas produced over time.',
              'heading': 'Surface Area'}],
  'title': 'Factors Affecting the Rate of Reaction',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Increasing concentration or surface area increases the FREQUENCY of collisions but does NOT '
                    'change the activation energy. Only a CATALYST changes the activation energy. Temperature '
                    'increases both frequency AND the proportion above activation energy. These are different '
                    'mechanisms.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'collision-theory',
  'key_note': 'Collision theory: reaction needs collision + sufficient energy (≥ Ea) + correct orientation. Activation '
              'energy = minimum energy for reaction. Low Ea = fast reaction. High Ea = slow reaction. Temperature '
              'raises proportion of particles above Ea — more effective collisions. Catalyst lowers Ea.',
  'matching': {'instruction': 'Match each concept to its correct description.',
               'pairs': [('Activation energy', 'Minimum energy needed for a collision to result in a reaction'),
                         ('Effective collision',
                          'A collision with sufficient energy AND correct orientation — results in products'),
                         ('Effect of temperature on Ea',
                          'Temperature does NOT change Ea — it increases the proportion of particles that have energy '
                          '≥ Ea'),
                         ('Catalyst effect on Ea',
                          'Catalyst LOWERS the activation energy — provides an alternative pathway'),
                         ('Why petrol needs a spark',
                          'Petrol is stable at room temperature — needs activation energy (spark) to initiate '
                          'combustion')],
               'title': 'Collision Theory Concepts'},
  'quiz': [{'opts': [("Most collisions don't have sufficient energy — the particles must have energy ≥ the activation "
                      'energy',
                      True),
                     ('Most collisions are too fast — particles bounce off before bonds can form', False),
                     ('Most collisions involve too many particles — only two particles can react at once', False),
                     ('Most collisions happen between the same type of particle — same reactant colliding with itself',
                      False)],
            'q': 'Why do most collisions between reactant particles NOT result in a reaction?',
            'wrong_explanations': {1: "Collision speed doesn't determine success directly — it's whether the ENERGY "
                                      'meets the activation energy threshold.',
                                   2: "Many reactions are bimolecular (two particles) but this isn't why most "
                                      'collisions fail — energy below Ea is the main reason.',
                                   3: 'Particles of the same type do collide, but in a mixture, most collisions do '
                                      'involve different reactant species — the issue is energy, not species.'}},
           {'opts': [('The reaction will be slow — only a small proportion of collisions will have enough energy to '
                      'succeed',
                      True),
                     ('The reaction will be fast — high activation energy means particles are very energetic', False),
                     ('The reaction will be exothermic — high activation energy means lots of energy released', False),
                     ('The reaction will not occur at all — nothing can overcome high activation energy', False)],
            'q': 'A reaction has a very high activation energy. What does this predict about the reaction?',
            'wrong_explanations': {1: "High activation energy doesn't mean particles are energetic — it means the "
                                      'THRESHOLD is high, so few particles exceed it.',
                                   2: 'Activation energy and ΔH are independent — a reaction can have high Ea and '
                                      'still be endothermic, or low Ea and highly exothermic.',
                                   3: 'Reactions with high Ea can still occur — just slowly. Temperature can always '
                                      'provide the energy. Explosives often have high Ea but react violently once '
                                      'started.'}}],
  'rp': None,
  'spec': '5.6.1.3',
  'summary': 'Explain collision theory and how activation energy determines whether a reaction occurs.',
  'theory': [{'content': 'COLLISION THEORY explains why reactions happen and what affects their rate.\n'
                         '\n'
                         'For a reaction to occur:\n'
                         '1. Reactant particles must COLLIDE with each other.\n'
                         '2. The collision must have sufficient ENERGY — equal to or greater than the ACTIVATION '
                         'ENERGY.\n'
                         '3. The particles must be in the CORRECT ORIENTATION (for some reactions).\n'
                         '\n'
                         'Most collisions are UNSUCCESSFUL — the particles collide but bounce off without reacting, '
                         "because they don't have enough energy.\n"
                         '\n'
                         'Only EFFECTIVE (successful) collisions lead to products.\n'
                         '\n'
                         'This explains all rate factors:\n'
                         'Higher temperature → faster particles → more collisions AND more above activation energy → '
                         'more effective collisions.\n'
                         'Higher concentration → more particles per volume → more collisions → more effective '
                         'collisions.\n'
                         'Larger surface area → more exposed particles → more collisions → more effective collisions.',
              'heading': 'Collision Theory'},
             {'content': 'ACTIVATION ENERGY (Ea) is the MINIMUM energy that colliding particles must have for a '
                         'reaction to occur.\n'
                         '\n'
                         "Even exothermic reactions need activation energy to get started — you must 'invest' some "
                         'energy to break existing bonds before the reaction can release more energy.\n'
                         '\n'
                         'Example: petrol is stable at room temperature (collisions between O₂ and petrol molecules '
                         "don't have enough energy). You need a spark (to provide the activation energy) to start the "
                         'combustion.\n'
                         '\n'
                         'EA AND REACTION RATE:\n'
                         'LOW activation energy → many particles have enough energy → FAST reaction.\n'
                         'HIGH activation energy → few particles have enough energy → SLOW reaction.\n'
                         '\n'
                         'BOLTZMANN DISTRIBUTION (energy of particles):\n'
                         'At any temperature, particles have a range of energies.\n'
                         'Most particles have intermediate energy — very few have very low or very high energy.\n'
                         'Raising temperature shifts this distribution — more particles move into the high-energy tail '
                         '(above Ea).\n'
                         'Even a 10°C rise significantly increases the proportion of particles above Ea.',
              'heading': 'Activation Energy'},
             {'content': 'Only a small fraction of collisions actually result in reaction:\n'
                         '\n'
                         'For a collision to be SUCCESSFUL (effective):\n'
                         'Energy ≥ activation energy → sufficient energy to break existing bonds.\n'
                         'Correct orientation → molecules must collide in the right way for bonds to break and reform '
                         'correctly.\n'
                         '\n'
                         'For example, in the reaction A-B + C → A + B-C:\n'
                         'The C particle must approach the B end of A-B — not the A end.\n'
                         'A collision at the wrong angle gives an unsuccessful result even if energy is sufficient.\n'
                         '\n'
                         'This is why not ALL collisions — even energetic ones — lead to products.\n'
                         '\n'
                         'INDUSTRIAL RELEVANCE:\n'
                         'Industrial chemists balance:\n'
                         'HIGH TEMPERATURE (faster rate but more energy cost).\n'
                         'CATALYST (lowers activation energy → faster rate without extra heat).\n'
                         'HIGH PRESSURE (for gas reactions — more collisions).\n'
                         'CONCENTRATION (higher concentrations mean more collisions).',
              'heading': 'Successful vs Unsuccessful Collisions'}],
  'title': 'Collision Theory and Activation Energy',
  'triple_only': None,
  'variables': [('Ea', 'Activation energy', 'kJ/mol', 'kJ/mol')]},
 {'common_mistake': 'A catalyst is NOT used up — it is the same at the END of the reaction as at the START. It does '
                    'NOT change the products or the overall energy change (ΔH). It ONLY provides an alternative '
                    'pathway with LOWER ACTIVATION ENERGY — making the reaction faster, not different.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'catalysts',
  'key_note': 'Catalyst: increases rate, not used up, lowers activation energy, does not change ΔH. Heterogeneous: '
              'different phase (solid catalyst, gas reactants). Biological: enzymes. Industrial: iron (Haber), '
              'platinum (catalytic converter), V₂O₅ (Contact process). Lower temperature possible → energy saving.',
  'matching': {'instruction': 'Match each catalyst to the industrial reaction it is used in.',
               'pairs': [('Iron', 'Haber process — N₂ + 3H₂ ⇌ 2NH₃ — making ammonia for fertilisers'),
                         ('Vanadium pentoxide (V₂O₅)',
                          'Contact process — 2SO₂ + O₂ ⇌ 2SO₃ — step in making sulfuric acid'),
                         ('Platinum / rhodium', 'Catalytic converter — converts CO and NOₓ to CO₂ and N₂'),
                         ('Nickel', 'Hydrogenation — converting unsaturated oils to solid fats (margarine)'),
                         ('Amylase (enzyme)', 'Biological catalyst — breaks down starch to sugars in digestion')],
               'title': 'Match the Catalyst to its Reaction'},
  'quiz': [{'opts': [('The rate increases because the activation energy is lowered — the products and ΔH are unchanged',
                      True),
                     ('The products change — the catalyst reacts with some reactants to form new products', False),
                     ('The overall energy change (ΔH) decreases — less energy is released or absorbed', False),
                     ('The catalyst is used up proportionally to the amount of reactant that reacts', False)],
            'q': 'A catalyst is added to a reaction. Which of the following is true?',
            'wrong_explanations': {1: 'A catalyst provides an ALTERNATIVE PATHWAY to the same products — it does not '
                                      'change what products form.',
                                   2: 'ΔH is the difference in energy between reactants and products — the catalyst '
                                      "doesn't change what the reactants or products ARE, so ΔH stays the same.",
                                   3: 'A catalyst is NOT consumed in the reaction — by definition it is regenerated. A '
                                      'substance that is used up is a REACTANT, not a catalyst.'}},
           {'opts': [('The catalyst lowers activation energy — more particles have sufficient energy at lower '
                      'temperature — fast enough rate without needing extra heat',
                      True),
                     ('Catalysts generate heat themselves — reducing the need for external heating', False),
                     ('Lower temperatures produce better quality products when catalysts are used', False),
                     ('Catalysts compress the reactant gases — raising pressure reduces the need for temperature',
                      False)],
            'q': 'Why can industrial processes use lower temperatures when a catalyst is present?',
            'wrong_explanations': {1: "Catalysts don't generate heat — they lower the energy barrier. If they released "
                                      'heat, they would be acting as reactants.',
                                   2: 'Product quality is not directly related to catalyst presence — the reason for '
                                      'lower temperature is purely kinetic (enough particles above the new lower Ea).',
                                   3: "Catalysts don't affect the pressure of reactant gases."}}],
  'rp': None,
  'spec': '5.6.1.4',
  'summary': 'Describe how catalysts work, give examples and explain their industrial importance.',
  'theory': [{'content': 'A CATALYST is a substance that INCREASES THE RATE of a reaction WITHOUT being used up or '
                         'permanently changed itself.\n'
                         '\n'
                         'Key properties:\n'
                         'Increases rate — provides a reaction pathway with LOWER ACTIVATION ENERGY.\n'
                         'Not used up — the catalyst is the same at the end of the reaction as at the start.\n'
                         'Present in small quantities — a small amount can catalyse a large quantity of reactants.\n'
                         'SPECIFIC — each catalyst only works for particular reactions (or types of reaction).\n'
                         '\n'
                         'How catalysts work:\n'
                         'They provide an ALTERNATIVE REACTION PATHWAY with a lower activation energy.\n'
                         'A greater proportion of collisions now have energy ≥ the lower activation energy → faster '
                         'rate.\n'
                         'The overall energy change (ΔH) is not affected — same reactants and products, same energy '
                         'difference.',
              'heading': 'What is a Catalyst?'},
             {'content': 'HETEROGENEOUS CATALYSTS:\n'
                         'In a DIFFERENT PHASE from the reactants.\n'
                         'Usually a solid catalyst with gaseous or liquid reactants.\n'
                         'Reaction occurs on the SURFACE of the catalyst.\n'
                         'Example: IRON catalyst in the Haber process (N₂ + 3H₂ ⇌ 2NH₃) — solid iron, gaseous '
                         'reactants.\n'
                         'Example: PLATINUM/RHODIUM in catalytic converters — converts CO, NO and hydrocarbons to CO₂, '
                         'N₂ and H₂O.\n'
                         'Example: NICKEL in margarine production — hydrogenation of vegetable oils.\n'
                         '\n'
                         'HOMOGENEOUS CATALYSTS:\n'
                         'In the SAME PHASE as the reactants (usually both dissolved in solution).\n'
                         'Example: hydrogen peroxide decomposition — Fe²⁺ ions in solution catalyse it.\n'
                         '\n'
                         'BIOLOGICAL CATALYSTS (ENZYMES):\n'
                         'Protein molecules that catalyse specific biochemical reactions.\n'
                         'Example: amylase — catalyses starch hydrolysis. Catalase — decomposes H₂O₂.\n'
                         'Highly specific — one enzyme, one reaction.\n'
                         'Sensitive to temperature and pH — denature above ~40°C.',
              'heading': 'Types of Catalyst'},
             {'content': 'Catalysts are enormously important in industry:\n'
                         '\n'
                         'HABER PROCESS (making ammonia for fertilisers):\n'
                         'N₂ + 3H₂ ⇌ 2NH₃ — iron catalyst.\n'
                         'Without catalyst: reaction too slow to be economical at practical temperatures.\n'
                         'With iron catalyst: reaction is fast enough at ~450°C.\n'
                         '\n'
                         'CONTACT PROCESS (making sulfuric acid):\n'
                         '2SO₂ + O₂ ⇌ 2SO₃ — vanadium pentoxide (V₂O₅) catalyst.\n'
                         '\n'
                         'CATALYTIC CONVERTERS in cars:\n'
                         'Platinum and rhodium catalyse conversion of toxic exhaust gases.\n'
                         '\n'
                         'ECONOMIC AND ENVIRONMENTAL BENEFITS of catalysts:\n'
                         'Reactions can be run at LOWER TEMPERATURES → less energy needed → lower cost.\n'
                         'FEWER BY-PRODUCTS in many cases → cleaner processes.\n'
                         'Smaller reactors needed → lower capital cost.\n'
                         'Catalysts can be RECOVERED and REUSED → economical.\n'
                         '\n'
                         'Disadvantage: catalysts can be POISONED — impurities in the reaction mixture bond to the '
                         'catalyst surface and block active sites.',
              'heading': 'Industrial Importance of Catalysts'}],
  'title': 'Catalysts',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'At equilibrium, the reaction has NOT stopped — it is DYNAMIC. Both forward and reverse reactions '
                    'continue at equal rates. Concentrations are CONSTANT but not necessarily EQUAL. Students often '
                    "say 'equilibrium means equal concentrations' — this is wrong. It means equal RATES.",
  'equations': ['NH₄Cl(s) ⇌ NH₃(g) + HCl(g)  (reversible reaction)',
                'CuSO₄·5H₂O(s) ⇌ CuSO₄(s) + 5H₂O(l)  (reversible reaction)'],
  'fifas': [],
  'higher': None,
  'id': 'reversible-reactions-equilibrium',
  'key_note': 'Reversible reaction: ⇌ symbol. Products can reform reactants. Closed system → dynamic equilibrium: '
              'forward and reverse rates equal, concentrations constant (not equal). If forward is exothermic → '
              'reverse is endothermic (same energy magnitude). NH₄Cl decomposition and CuSO₄ hydration are key '
              'examples.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Reversible reaction', 'Products can react to re-form original reactants — shown with ⇌'),
                         ('Dynamic equilibrium',
                          'Closed system where forward and reverse reaction rates are equal — concentrations constant'),
                         ('Closed system', 'No reactants or products enter or leave — required for equilibrium'),
                         ('Exothermic forward reaction',
                          'The reverse reaction is endothermic — same energy magnitude, opposite sign'),
                         ('Test for water',
                          'White anhydrous CuSO₄ turns blue in the presence of water — reversible hydration')],
               'title': 'Reversible Reaction Concepts'},
  'quiz': [{'opts': [('The forward and reverse reactions are still occurring at equal rates — concentrations of all '
                      'species are constant',
                      True),
                     ('The reaction has stopped — no more forward or reverse reaction takes place', False),
                     ('Concentrations of reactants and products are equal', False),
                     ('Only the forward reaction occurs — the reverse reaction has stopped', False)],
            'q': 'At dynamic equilibrium, which of the following is true?',
            'wrong_explanations': {1: "'Dynamic' means BOTH reactions are still occurring — it is NOT static. "
                                      "'Equilibrium' means rates are balanced, not that the reaction stopped.",
                                   2: 'Concentrations are CONSTANT but NOT necessarily equal. The ratio of products to '
                                      'reactants can be anything — it depends on the specific reaction and conditions.',
                                   3: 'If only the forward reaction occurred, it would be a one-way reaction — '
                                      'equilibrium requires BOTH directions continuing at equal rates.'}},
           {'opts': [('Absorbs 50 kJ/mol — the reverse reaction is endothermic with the same energy magnitude', True),
                     ('Releases 50 kJ/mol — the reverse reaction also releases the same energy', False),
                     ('Absorbs 100 kJ/mol — double the forward reaction energy', False),
                     ('Zero — the reverse reaction has no energy change', False)],
            'q': 'The forward reaction A ⇌ B releases 50 kJ/mol. How much energy does the reverse reaction B → A '
                 'involve?',
            'wrong_explanations': {1: 'If the reverse also released energy, energy would be created from nothing — '
                                      'violating conservation of energy.',
                                   2: 'The energy is the SAME magnitude (50 kJ/mol) but the direction is reversed — '
                                      'forward exothermic means reverse endothermic.',
                                   3: 'Energy changes in reversible reactions are always equal and opposite — the '
                                      'reverse cannot have zero energy change if the forward has a non-zero change.'}}],
  'rp': None,
  'spec': '5.6.2.1–5.6.2.3',
  'summary': 'Describe reversible reactions and explain what is meant by dynamic equilibrium.',
  'theory': [{'content': 'A REVERSIBLE REACTION is one where the products can react to form the original reactants '
                         'again.\n'
                         '\n'
                         'Symbol: ⇌ (double-headed arrow indicating the reaction goes in both directions).\n'
                         '\n'
                         'Examples:\n'
                         'Ammonium chloride thermal decomposition:\n'
                         'NH₄Cl(s) ⇌ NH₃(g) + HCl(g)\n'
                         'When heated: NH₄Cl decomposes to NH₃ and HCl (forward reaction).\n'
                         'When cooled: NH₃ and HCl recombine to form NH₄Cl (reverse reaction).\n'
                         '\n'
                         'Hydrated copper sulfate:\n'
                         'CuSO₄·5H₂O(s) ⇌ CuSO₄(s) + 5H₂O(l)\n'
                         'Heating blue crystals → white anhydrous powder + water (forward reaction).\n'
                         'Adding water to white powder → blue crystals reform (reverse reaction).\n'
                         'This is used as a TEST FOR WATER — white powder turns blue in the presence of water.\n'
                         '\n'
                         'The DIRECTION of a reversible reaction depends on the conditions (temperature, pressure, '
                         'concentration).',
              'heading': 'Reversible Reactions'},
             {'content': 'When a reversible reaction is carried out in a CLOSED SYSTEM (nothing enters or leaves), it '
                         'reaches EQUILIBRIUM.\n'
                         '\n'
                         'At equilibrium:\n'
                         "The FORWARD and REVERSE reactions are still occurring — the reaction doesn't stop.\n"
                         'The RATES of the forward and reverse reactions are EQUAL.\n'
                         'The CONCENTRATIONS of reactants and products remain CONSTANT (but not necessarily equal).\n'
                         '\n'
                         "This is called DYNAMIC EQUILIBRIUM — 'dynamic' because both reactions are still happening "
                         "(not static); 'equilibrium' because the concentrations are balanced (not changing).\n"
                         '\n'
                         'Important: at equilibrium the reaction is STILL HAPPENING — it just appears to have stopped '
                         'because concentrations are constant.\n'
                         '\n'
                         'CLOSED SYSTEM requirement:\n'
                         'If products are removed, the reaction shifts to produce more products (restoring '
                         'equilibrium).\n'
                         'If reactants are removed, the reaction shifts to produce more reactants.\n'
                         'Open systems (like burning fuel in open air) cannot reach equilibrium — products escape.',
              'heading': 'Dynamic Equilibrium'},
             {'content': 'In a reversible reaction:\n'
                         'If the FORWARD reaction is EXOTHERMIC → the REVERSE reaction is ENDOTHERMIC.\n'
                         'The SAME amount of energy is released in the forward direction as is absorbed in the reverse '
                         'direction.\n'
                         '\n'
                         'Example — hydrated copper sulfate:\n'
                         'CuSO₄·5H₂O → CuSO₄ + 5H₂O is ENDOTHERMIC (absorbs heat — heat applied to dehydrate).\n'
                         'CuSO₄ + 5H₂O → CuSO₄·5H₂O is EXOTHERMIC (releases heat — hand gets warm when water added).\n'
                         '\n'
                         'Example — Haber process:\n'
                         'N₂ + 3H₂ → 2NH₃ is EXOTHERMIC.\n'
                         '2NH₃ → N₂ + 3H₂ is ENDOTHERMIC.\n'
                         'Same energy value — opposite signs.\n'
                         '\n'
                         'This principle is important for understanding how changing conditions affects equilibrium '
                         'position.',
              'heading': 'Energy Changes in Reversible Reactions'}],
  'title': 'Reversible Reactions and Equilibrium',
  'triple_only': None,
  'variables': []}],

"organic": [{'common_mistake': 'Alkanes are SATURATED — they have only SINGLE bonds and do NOT decolourise bromine water. ALKENES '
                    'are UNSATURATED (have a C=C double bond) and DO decolourise bromine water. The bromine water test '
                    'distinguishes saturated (no change) from unsaturated (decolourises).',
  'equations': ['General formula for alkanes: CₙH₂ₙ₊₂',
                'CH₄ + 2O₂ → CO₂ + 2H₂O  (complete combustion of methane)',
                'C₃H₈ + 5O₂ → 3CO₂ + 4H₂O  (complete combustion of propane)'],
  'fifas': [],
  'higher': None,
  'id': 'crude-oil-hydrocarbons',
  'key_note': 'Crude oil: mixture of hydrocarbons (C and H only). Alkanes: CₙH₂ₙ₊₂, saturated (single bonds only), '
              'relatively unreactive. Complete combustion: CO₂ + H₂O. Incomplete combustion: CO (toxic) + soot. Crude '
              'oil is both fuel and feedstock.',
  'matching': {'instruction': 'Match each alkane to its molecular formula.',
               'pairs': [('Methane', 'CH₄ — 1 carbon, 4 hydrogens'),
                         ('Ethane', 'C₂H₆ — 2 carbons, 6 hydrogens'),
                         ('Propane', 'C₃H₈ — 3 carbons, 8 hydrogens'),
                         ('Butane', 'C₄H₁₀ — 4 carbons, 10 hydrogens'),
                         ('Complete combustion', 'Alkane + O₂ → CO₂ + H₂O — clean burn with plenty of oxygen')],
               'title': 'Match the Alkane'},
  'quiz': [{'opts': [('C₅H₁₂ — using CₙH₂ₙ₊₂: n=5, 2(5)+2 = 12 hydrogens', True),
                     ('C₅H₁₀ — using CₙH₂ₙ — the alkene formula', False),
                     ('C₅H₈ — fewer than expected', False),
                     ('C₅H₅ — half the expected hydrogens', False)],
            'q': 'An alkane has 5 carbon atoms. What is its molecular formula?',
            'wrong_explanations': {1: 'CₙH₂ₙ is the formula for ALKENES (unsaturated) — alkanes use CₙH₂ₙ₊₂. For n=5: '
                                      '2(5)+2=12 hydrogens.',
                                   2: "C₅H₈ doesn't fit either alkane or alkene formula — may be an alkyne or cyclic "
                                      'compound.',
                                   3: 'C₅H₅ is not a simple alkane or alkene — alkanes always have 2n+2 hydrogens.'}},
           {'opts': [('Carbon monoxide is produced — a toxic, colourless, odourless gas that prevents oxygen transport '
                      'in blood',
                      True),
                     ('Incomplete combustion releases more energy — causing overheating', False),
                     ('Water vapour produced from incomplete combustion causes corrosion', False),
                     ('Incomplete combustion only produces CO₂ which is more harmful than CO', False)],
            'q': 'Why is incomplete combustion of fuels more dangerous than complete combustion?',
            'wrong_explanations': {1: 'Incomplete combustion releases LESS energy per gram — not more. It is less '
                                      'efficient.',
                                   2: 'Water vapour is produced in BOTH complete and incomplete combustion — it is not '
                                      'specific to incomplete.',
                                   3: 'CO₂ contributes to climate change but is not immediately toxic like CO. '
                                      'Incomplete combustion produces CO (toxic) and particulates.'}}],
  'rp': None,
  'spec': '5.7.1.1',
  'summary': 'Describe crude oil as a mixture of hydrocarbons and the structure of alkanes.',
  'theory': [{'content': 'CRUDE OIL is a FINITE, NON-RENEWABLE resource found underground, formed over millions of '
                         'years from the remains of ancient marine organisms under high pressure and temperature.\n'
                         '\n'
                         'Crude oil is a MIXTURE of many different HYDROCARBONS — compounds containing only CARBON and '
                         'HYDROGEN atoms.\n'
                         '\n'
                         'Crude oil is both a FUEL and a FEEDSTOCK:\n'
                         'FUEL — burned to release energy (petrol, diesel, jet fuel, heating oil).\n'
                         'FEEDSTOCK — raw material for making other chemicals (plastics, medicines, dyes, '
                         'detergents).\n'
                         '\n'
                         'Because it is a MIXTURE, the hydrocarbons in crude oil are not chemically bonded — they can '
                         'be separated by physical methods. The most important method is FRACTIONAL DISTILLATION.',
              'heading': 'Crude Oil and Carbon Compounds'},
             {'content': 'ALKANES are the most common type of hydrocarbon in crude oil.\n'
                         '\n'
                         'Properties of alkanes:\n'
                         'Contain only SINGLE C-C bonds and C-H bonds — SATURATED hydrocarbons.\n'
                         'General formula: CₙH₂ₙ₊₂ (where n = number of carbon atoms).\n'
                         'Do not decolourise bromine water — no double bonds to react.\n'
                         '\n'
                         'Homologous series — alkanes with increasing chain length:\n'
                         'Methane: CH₄ (n=1, 1 carbon)\n'
                         'Ethane: C₂H₆ (n=2)\n'
                         'Propane: C₃H₈ (n=3)\n'
                         'Butane: C₄H₁₀ (n=4)\n'
                         'Pentane: C₅H₁₂ (n=5)\n'
                         '\n'
                         'STRUCTURAL FORMULAE:\n'
                         'Methane: H-C-H (tetrahedral, 4 H around 1 C)\n'
                         'Ethane: H₃C-CH₃ (two CH₃ groups joined)\n'
                         'Propane: H₃C-CH₂-CH₃\n'
                         '\n'
                         'The C-H and C-C bonds in alkanes are all SINGLE COVALENT bonds — this makes alkanes '
                         'relatively unreactive (the bonds are strong and non-polar).',
              'heading': 'Alkanes — Structure and Formulae'},
             {'content': 'The main reaction of alkanes is COMBUSTION — burning in oxygen to release energy.\n'
                         '\n'
                         'COMPLETE COMBUSTION (plenty of oxygen):\n'
                         'Alkane + oxygen → carbon dioxide + water\n'
                         'CH₄ + 2O₂ → CO₂ + 2H₂O (methane)\n'
                         'C₃H₈ + 5O₂ → 3CO₂ + 4H₂O (propane)\n'
                         '\n'
                         'Products: CO₂ and H₂O only — relatively clean burn.\n'
                         '\n'
                         'INCOMPLETE COMBUSTION (limited oxygen):\n'
                         'Carbon monoxide (CO) and soot (C — unburned carbon particles) are produced.\n'
                         'CO is TOXIC — colourless, odourless, binds to haemoglobin in red blood cells → prevents '
                         'oxygen transport.\n'
                         'Soot (particulates) causes respiratory problems and contributes to global dimming.\n'
                         '\n'
                         'Why complete combustion is preferred:\n'
                         'More energy released per gram of fuel.\n'
                         'No toxic CO produced.\n'
                         'Less air pollution.',
              'heading': 'Combustion of Alkanes'}],
  'title': 'Crude Oil, Hydrocarbons and Alkanes',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Fractions with SHORTER chains have LOWER boiling points and collect at the TOP of the '
                    'fractionating column (cooler). Fractions with LONGER chains have HIGHER boiling points and '
                    'collect at the BOTTOM (hotter). Students sometimes get this backwards.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'fractional-distillation',
  'key_note': 'Fractional distillation: heat crude oil → vapours rise column → cool → condense at boiling point → '
              'fractions collected. Short chains: top, low BP, more flammable, less viscous. Long chains: bottom, high '
              'BP, less flammable, more viscous. Fractions: gases, petrol, naphtha, kerosene, diesel, fuel oil, '
              'bitumen.',
  'matching': {'instruction': 'Match each fraction to its chain length, boiling point and main use.',
               'pairs': [('Refinery gases',
                          'Shortest chains (C₁–C₄), lowest boiling point — LPG for cooking and heating'),
                         ('Petrol', 'Short chains (C₅–C₁₀), low boiling point — fuel for cars'),
                         ('Kerosene', 'Medium chains (C₁₀–C₁₆) — jet aircraft fuel'),
                         ('Diesel', 'Longer chains (C₁₅–C₂₅) — fuel for lorries and trains'),
                         ('Bitumen', "Longest chains, doesn't vaporise — road surfacing")],
               'title': 'Match the Fraction to its Property and Use'},
  'quiz': [{'opts': [('Petrol collects higher up — it has shorter chains and a lower boiling point than diesel', True),
                     ('Petrol collects lower down — it is more dense than diesel', False),
                     ('Both collect at the same level — they have similar chain lengths', False),
                     ('Petrol collects at the very bottom with bitumen — it is a liquid at room temperature', False)],
            'q': 'Where in the fractionating column does petrol collect compared to diesel?',
            'wrong_explanations': {1: 'Density does affect placement somewhat, but the key factor is BOILING POINT. '
                                      'Petrol has lower BP → condenses higher up.',
                                   2: 'Petrol (C₅–C₁₀) and diesel (C₁₅–C₂₅) have very different chain lengths — they '
                                      'condense at different levels.',
                                   3: "Bitumen is at the BOTTOM because it doesn't vaporise — it has the longest "
                                      'chains and highest boiling point. Petrol is much lighter and collects high up '
                                      'the column.'}},
           {'opts': [('Bitumen molecules have much longer carbon chains — stronger intermolecular forces require more '
                      'energy to overcome',
                      True),
                     ('Bitumen contains more oxygen atoms, making it heavier', False),
                     ('Bitumen is denser so it needs more energy to change state', False),
                     ('Petrol has double bonds that make it easier to boil', False)],
            'q': 'Why does bitumen have a much higher boiling point than petrol?',
            'wrong_explanations': {1: 'Crude oil fractions are HYDROCARBONS — they contain only carbon and hydrogen. '
                                      'Oxygen is not present.',
                                   2: 'Density and boiling point are related but the cause of both is CHAIN LENGTH and '
                                      'intermolecular forces — not density itself.',
                                   3: 'Alkanes (including petrol fractions) have only SINGLE bonds — no double bonds. '
                                      'Double bonds are found in alkenes.'}}],
  'rp': None,
  'spec': '5.7.1.2',
  'summary': 'Describe how crude oil is separated into fractions and the properties of each fraction.',
  'theory': [{'content': 'FRACTIONAL DISTILLATION separates crude oil into FRACTIONS — groups of hydrocarbons with '
                         'similar boiling points and chain lengths.\n'
                         '\n'
                         'The process:\n'
                         '1. Crude oil is HEATED to ~350°C — most of it vaporises.\n'
                         '2. Vapours rise up a tall FRACTIONATING COLUMN which is HOT at the bottom and COOL at the '
                         'top.\n'
                         '3. As vapours rise, they COOL DOWN.\n'
                         '4. Each fraction CONDENSES (turns back to liquid) at its boiling point and is collected at '
                         'the appropriate level.\n'
                         '5. Fractions with HIGHER boiling points (longer chains) condense LOWER in the column.\n'
                         '6. Fractions with LOWER boiling points (shorter chains) rise higher and condense near the '
                         'TOP.\n'
                         '\n'
                         "Heavy residue (bitumen) doesn't vaporise and remains at the bottom.\n"
                         'Refinery gases (shortest chains: methane, ethane, propane, butane) rise to the very top and '
                         'leave as gases.',
              'heading': 'How Fractional Distillation Works'},
             {'content': 'From top (lowest boiling point) to bottom (highest boiling point):\n'
                         '\n'
                         'REFINERY GASES (C₁–C₄): bp below 25°C\n'
                         'Shortest chains — methane, propane, butane.\n'
                         'Uses: LPG (cooking and heating), camping gas.\n'
                         '\n'
                         'PETROL/GASOLINE (C₅–C₁₀): bp 25–75°C\n'
                         'Uses: fuel for cars.\n'
                         '\n'
                         'NAPHTHA (C₅–C₁₀): bp 75–120°C\n'
                         'Uses: feedstock for making chemicals and plastics.\n'
                         '\n'
                         'KEROSENE/JET FUEL (C₁₀–C₁₆): bp 150–250°C\n'
                         'Uses: jet aircraft fuel, heating.\n'
                         '\n'
                         'DIESEL/GAS OIL (C₁₅–C₂₅): bp 220–350°C\n'
                         'Uses: fuel for lorries, trains, some cars.\n'
                         '\n'
                         'FUEL OIL (C₂₀–C₇₀): bp >350°C\n'
                         'Uses: large ships, power stations.\n'
                         '\n'
                         "BITUMEN (C₇₀+): doesn't vaporise\n"
                         'Uses: road surfacing, roofing.',
              'heading': 'The Main Fractions and Their Uses'},
             {'content': 'As chain length INCREASES going from top to bottom of the fractionating column:\n'
                         '\n'
                         'BOILING POINT INCREASES:\n'
                         'Longer chains → stronger London dispersion forces (intermolecular) between molecules → more '
                         'energy to separate → higher boiling point.\n'
                         '\n'
                         'VISCOSITY INCREASES (gets thicker/runnier):\n'
                         'Longer chains → more tangled molecules → harder to flow.\n'
                         'Refinery gases: very low viscosity (gases). Bitumen: extremely viscous (solid/semi-solid).\n'
                         '\n'
                         'FLAMMABILITY DECREASES:\n'
                         'Shorter chain fractions ignite more easily — more volatile (evaporate easily at room '
                         'temperature).\n'
                         'Longer chains are less volatile and harder to ignite.\n'
                         '\n'
                         'COLOUR becomes darker — refinery gases are colourless, bitumen is black.\n'
                         '\n'
                         'DEMAND vs SUPPLY:\n'
                         'More petrol and diesel are demanded than naturally occur in crude oil.\n'
                         'CRACKING converts larger, less useful fractions into smaller, more useful ones (especially '
                         'petrol and ethene for plastics).',
              'heading': 'Properties and Trends in Fractions'}],
  'title': 'Fractional Distillation of Crude Oil',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Shorter chain hydrocarbons have LOWER boiling points and are MORE flammable/volatile. Longer '
                    'chains are LESS flammable and MORE viscous. Students often get flammability and chain length '
                    'confused — think of it this way: petrol (short chains) is much more flammable than diesel (longer '
                    'chains).',
  'equations': ['Hydrocarbon + O₂ → CO₂ + H₂O  (complete combustion)',
                '2C₈H₁₈ + 25O₂ → 16CO₂ + 18H₂O  (octane complete combustion)'],
  'fifas': [],
  'higher': None,
  'id': 'properties-of-hydrocarbons',
  'key_note': 'Longer chains: higher BP, more viscous, less flammable, less volatile. Shorter chains: lower BP, less '
              'viscous, more flammable, more volatile. C₁–C₄ = gases. C₅–C₁₇ = liquids. C₁₈+ = solids. Complete '
              'combustion: CO₂ + H₂O. Incomplete: CO + soot.',
  'matching': {'instruction': 'Match each property to whether it increases or decreases with chain length.',
               'pairs': [('Increases with chain length',
                          'Boiling point — stronger intermolecular forces in longer molecules'),
                         ('Increases with chain length', 'Viscosity — longer chains tangle, flow less easily'),
                         ('Decreases with chain length',
                          'Flammability — longer chains less volatile, harder to ignite'),
                         ('Decreases with chain length', 'Volatility — longer chains have lower vapour pressure')],
               'title': 'Chain Length → Property'},
  'quiz': [{'opts': [('Petrol has shorter chains — more volatile, evaporates easily at room temperature, produces '
                      'flammable vapour readily',
                      True),
                     ('Petrol contains more hydrogen — hydrogen is more flammable than carbon', False),
                     ("Diesel is more viscous — it can't flow to the flame and doesn't ignite", False),
                     ('Petrol has double bonds — alkenes are more reactive and flammable than alkanes', False)],
            'q': 'Why is petrol (C₅–C₁₀) more flammable than diesel (C₁₅–C₂₅)?',
            'wrong_explanations': {1: 'Both petrol and diesel are mainly hydrocarbons with similar C:H ratios — '
                                      'hydrogen content is not the reason for different flammability.',
                                   2: 'Viscosity affects flow but the primary reason for different flammability is '
                                      'VOLATILITY — petrol produces more vapour at room temperature.',
                                   3: 'Petrol fractions are alkanes (saturated, single bonds). Alkenes do have double '
                                      'bonds but crude oil fractions are not alkenes — they are alkanes.'}},
           {'opts': [('Hexadecane has much longer chains — stronger intermolecular forces mean its boiling point is '
                      'far above room temperature',
                      True),
                     ('Hexadecane contains more hydrogen — hydrogen atoms make it solid', False),
                     ('Propane is lighter, so it exists as a gas by buoyancy', False),
                     ('Hexadecane has ionic bonds that hold it as a solid', False)],
            'q': 'Propane (C₃H₈) is a gas at room temperature but hexadecane (C₁₆H₃₄) is a solid. Why?',
            'wrong_explanations': {1: "Hydrogen content doesn't determine physical state — chain length and the "
                                      'resulting intermolecular forces determine boiling point.',
                                   2: "Buoyancy explains why lighter gases rise but doesn't explain why propane is a "
                                      "GAS rather than a liquid or solid at room temperature — that's about "
                                      'intermolecular forces.',
                                   3: 'Both are hydrocarbons with only covalent bonds — no ionic bonds. The difference '
                                      'in state is entirely due to intermolecular force strength.'}}],
  'rp': None,
  'spec': '5.7.1.3',
  'summary': 'Explain how chain length affects the physical and chemical properties of hydrocarbons.',
  'theory': [{'content': 'The PHYSICAL PROPERTIES of hydrocarbons change systematically with chain length.\n'
                         '\n'
                         'BOILING POINT:\n'
                         'Increases with chain length.\n'
                         'Longer chains have greater LONDON DISPERSION FORCES between molecules.\n'
                         'More energy needed to separate molecules → higher boiling point.\n'
                         'Methane (CH₄): −161°C. Hexadecane (C₁₆H₃₄): 287°C.\n'
                         '\n'
                         'VISCOSITY:\n'
                         'Increases with chain length.\n'
                         'Longer chains get tangled → flow less easily → more viscous.\n'
                         'Methane: gas (not viscous at all). Bitumen: extremely viscous semi-solid.\n'
                         '\n'
                         'FLAMMABILITY (ease of ignition):\n'
                         'Decreases with chain length.\n'
                         'Shorter chains are more VOLATILE (evaporate easily at room temperature).\n'
                         'High vapour pressure → easy to ignite.\n'
                         'Longer chains: lower vapour pressure, harder to ignite.\n'
                         '\n'
                         'This explains why petrol (short chains) catches fire easily while fuel oil (long chains) is '
                         'much harder to ignite.',
              'heading': 'How Chain Length Affects Physical Properties'},
             {'content': 'VOLATILITY — the tendency to evaporate — decreases with chain length.\n'
                         '\n'
                         'At room temperature (approximately 20–25°C):\n'
                         'C₁–C₄ hydrocarbons are GASES (boiling point below room temperature).\n'
                         'C₅–C₁₇ hydrocarbons are LIQUIDS.\n'
                         'C₁₈+ hydrocarbons are SOLIDS (boiling point above room temperature).\n'
                         '\n'
                         'This explains the states of crude oil fractions:\n'
                         'Refinery gases (methane, propane): gases at room temperature.\n'
                         'Petrol, diesel: liquids.\n'
                         'Waxes, bitumen: solids or semi-solids.\n'
                         '\n'
                         'VOLATILITY AND SAFETY:\n'
                         'Highly volatile fuels (petrol) present fire hazards because vapour can ignite easily.\n'
                         'More volatile substances also have higher vapour pressures — they smell more strongly.\n'
                         'This is why petrol smells strongly and diesel smells less — petrol is more volatile.',
              'heading': 'Volatility and State at Room Temperature'},
             {'content': 'All hydrocarbons burn in oxygen — COMBUSTION is their most important chemical reaction.\n'
                         '\n'
                         'COMPLETE COMBUSTION (excess oxygen):\n'
                         'All carbon burned to CO₂. All hydrogen burned to H₂O.\n'
                         'Produces only CO₂ and water — maximum energy release.\n'
                         '\n'
                         'INCOMPLETE COMBUSTION (limited oxygen):\n'
                         'Produces CO and/or soot (carbon particulates) in addition to or instead of CO₂.\n'
                         'Less energy released.\n'
                         'CO: toxic, causes carbon monoxide poisoning.\n'
                         'Soot/particulates: cause respiratory problems, global dimming.\n'
                         '\n'
                         'BALANCING COMBUSTION EQUATIONS:\n'
                         'Octane (C₈H₁₈) + 12.5O₂ → 8CO₂ + 9H₂O (complete combustion)\n'
                         'Or: 2C₈H₁₈ + 25O₂ → 16CO₂ + 18H₂O\n'
                         '\n'
                         'The LONGER the chain, the more oxygen needed for complete combustion.',
              'heading': 'Burning Hydrocarbons — Combustion'}],
  'title': 'Properties of Hydrocarbons',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Cracking always produces at least one ALKENE — alkenes are ALWAYS one of the products. You cannot '
                    'crack a hydrocarbon to produce only alkanes. Also: alkenes DECOLOURISE bromine water (C=C reacts '
                    'with Br₂). Alkanes do NOT decolourise bromine water.',
  'equations': ['C₁₀H₂₂ → C₈H₁₈ + C₂H₄  (cracking example)',
                'General formula alkenes: CₙH₂ₙ',
                'C₂H₄ + H₂O → C₂H₅OH  (hydration)',
                'n CH₂=CH₂ → [−CH₂−CH₂−]ₙ  (polymerisation)'],
  'fifas': [],
  'higher': None,
  'id': 'cracking-alkenes',
  'key_note': 'Cracking: large alkane → smaller alkane + alkene. Needed because demand for petrol > supply from crude '
              'oil. Thermal: high T + pressure. Catalytic: ~500°C + zeolite catalyst. Alkenes: CₙH₂ₙ, C=C double bond, '
              'unsaturated, decolourise bromine water, undergo addition reactions, polymerise.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Cracking', 'Breaking long-chain alkanes into smaller alkanes + alkenes using heat/catalyst'),
                         ('Alkene test', 'Decolourises orange bromine water — C=C reacts with Br₂'),
                         ('Alkane test', 'No change with bromine water — no double bond to react'),
                         ('Addition reaction', 'Two molecules join across the C=C double bond to form one product'),
                         ('Polymerisation of ethene',
                          'Many ethene molecules join to form poly(ethene) — n CH₂=CH₂ → [−CH₂−CH₂−]ₙ')],
               'title': 'Cracking and Alkenes'},
  'quiz': [{'opts': [('It converts long-chain fractions (high supply, low demand) into short-chain fuels and alkenes '
                      '(high demand) for petrol and plastics',
                      True),
                     ('It purifies crude oil by removing impurities like sulfur compounds', False),
                     ('It increases the boiling point of fractions so they can be stored more safely', False),
                     ('It converts alkenes back into alkanes for more stable storage', False)],
            'q': 'Why is cracking important for the petrochemical industry?',
            'wrong_explanations': {1: 'Removing sulfur (desulfurisation) is a separate process — cracking is '
                                      'specifically about chain length reduction.',
                                   2: 'Cracking produces SHORTER chains with LOWER boiling points — it decreases '
                                      'boiling point, not increases it.',
                                   3: 'Cracking produces alkenes FROM alkanes — it converts alkanes to alkenes, not '
                                      'the other way round.'}},
           {'opts': [('Compound A is an alkene (unsaturated — C=C reacts with Br₂). Compound B is an alkane (saturated '
                      '— no reaction)',
                      True),
                     ('Compound A is an alkane. Compound B is an alkene.', False),
                     ('Both A and B are alkenes — both should react with bromine water', False),
                     ('The result shows compound A is more flammable than compound B', False)],
            'q': 'A student adds bromine water to two hydrocarbons. With compound A, the bromine water decolourises. '
                 'With compound B, there is no change. What does this show?',
            'wrong_explanations': {1: 'It is the ALKENE (unsaturated, C=C) that decolourises bromine water — not the '
                                      'alkane.',
                                   2: 'Alkanes do NOT decolourise bromine water — so if both reacted, that would '
                                      'suggest both are alkenes.',
                                   3: 'Bromine water test shows saturation/unsaturation — not flammability.'}}],
  'rp': None,
  'spec': '5.7.1.4',
  'summary': 'Describe cracking, explain why it is necessary and describe the structure and reactions of alkenes.',
  'theory': [{'content': 'CRACKING is the process of breaking down LARGE, LONG-CHAIN hydrocarbons into SMALLER, MORE '
                         'USEFUL ones.\n'
                         '\n'
                         'Why it is needed:\n'
                         'Crude oil contains MORE long-chain fractions (fuel oil, diesel, bitumen) than are in '
                         'demand.\n'
                         'Crude oil contains LESS short-chain fractions (petrol, gases) than are in demand.\n'
                         'Cracking converts the less useful long-chain fractions into the more useful short-chain '
                         'ones.\n'
                         '\n'
                         'Products of cracking:\n'
                         'Smaller ALKANE molecules (e.g. petrol-range hydrocarbons).\n'
                         'ALKENE molecules (e.g. ethene) — very important as feedstock for making POLYMERS and other '
                         'chemicals.\n'
                         '\n'
                         'Cracking also produces HYDROGEN GAS in some processes.\n'
                         '\n'
                         'Cracking increases the proportion of petrol available from crude oil and produces the ethene '
                         'needed for the plastics industry.',
              'heading': 'Why Cracking is Necessary'},
             {'content': 'THERMAL CRACKING:\n'
                         'High temperature (400–900°C) and high pressure.\n'
                         'Produces a high proportion of ALKENES.\n'
                         'The long-chain hydrocarbon vapour is passed through a hot tube — heat breaks the C-C bonds.\n'
                         '\n'
                         'CATALYTIC CRACKING:\n'
                         'High temperature (~500°C) but LOWER pressure.\n'
                         'Uses a ZEOLITE (aluminium silicate) catalyst.\n'
                         'More economical — lower pressure needed because catalyst lowers activation energy.\n'
                         'Produces more BRANCHED ALKANES useful for high-performance petrol.\n'
                         '\n'
                         'General equation:\n'
                         'Large alkane → smaller alkane + alkene\n'
                         'Example:\n'
                         'C₁₀H₂₂ → C₈H₁₈ + C₂H₄\n'
                         '(decane → octane + ethene)\n'
                         '\n'
                         'Condition: high temperature, catalyst (or high pressure for thermal cracking).',
              'heading': 'Methods of Cracking'},
             {'content': 'ALKENES are hydrocarbons containing at least one C=C DOUBLE BOND — they are UNSATURATED.\n'
                         '\n'
                         'General formula: CₙH₂ₙ\n'
                         'Ethene: C₂H₄\n'
                         'Propene: C₃H₆\n'
                         'Butene: C₄H₈\n'
                         '\n'
                         'The double bond makes alkenes MUCH MORE REACTIVE than alkanes.\n'
                         '\n'
                         'TEST FOR ALKENES — bromine water test:\n'
                         'Shake with BROMINE WATER (orange/brown).\n'
                         'Alkene: bromine water DECOLOURISES (turns colourless) — the C=C double bond reacts with '
                         'Br₂.\n'
                         "Alkane: NO CHANGE — single bonds don't react with bromine water at room temperature.\n"
                         '\n'
                         'ADDITION REACTIONS of alkenes:\n'
                         'UNSATURATED molecules add atoms across the C=C double bond.\n'
                         'Hydrogen: C₂H₄ + H₂ → C₂H₆ (hydrogenation — used to make margarine)\n'
                         'Bromine: C₂H₄ + Br₂ → CH₂BrCH₂Br (dibromoethane)\n'
                         'Water: C₂H₄ + H₂O → C₂H₅OH (hydration — makes ethanol)\n'
                         '\n'
                         'POLYMERISATION:\n'
                         'Ethene molecules join together to form poly(ethene): n CH₂=CH₂ → [−CH₂−CH₂−]ₙ',
              'heading': 'Alkenes — Structure and Reactions'}],
  'title': 'Cracking and Alkenes',
  'triple_only': None,
  'variables': []}],

"analysis": [{'common_mistake': "In chemistry, 'pure' does NOT mean natural or healthy — it means containing only ONE substance "
                    'with no impurities. A mixture of two pure chemicals is NOT a pure substance. Orange juice (even '
                    '100% natural) is a MIXTURE — not a pure substance in the chemical sense.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'pure-substances',
  'key_note': 'Pure substance: one element or compound only — sharp fixed melting and boiling points. Impure '
              '(mixture): melts/boils over a range of temperatures. Impurity lowers melting point and raises boiling '
              'point. Use melting/boiling point data to identify substances and test purity.',
  'matching': {'instruction': 'Match each observation to pure substance or impure mixture.',
               'pairs': [('Pure substance', 'Melts at exactly one temperature — sharp melting point'),
                         ('Impure mixture', 'Melts over a range of temperatures — starts below expected melting point'),
                         ('Pure substance', 'Boils at a constant temperature throughout'),
                         ('Impure mixture', 'Boiling point higher than expected for the pure substance'),
                         ('Pure substance', 'Has a fixed composition — contains only one type of compound')],
               'title': 'Pure or Impure?'},
  'quiz': [{'opts': [('The sample is impure — impurities lower the melting point and cause it to melt over a range',
                      True),
                     ('The sample is a different compound with a lower melting point', False),
                     ('The student heated it too quickly — this is a measurement error only', False),
                     ('The sample is pure but at a different pressure', False)],
            'q': 'A student heats a solid and records that it melts between 118°C and 125°C. Pure samples of this '
                 'compound melt at 135°C. What does this suggest?',
            'wrong_explanations': {1: 'It could be a different compound — but the wider context of the question '
                                      '(testing purity of a sample) suggests the most likely explanation is impurity.',
                                   2: 'Rapid heating can cause errors, but both a lower AND a range of melting '
                                      'temperatures strongly suggest impurity — not just measurement error.',
                                   3: 'Standard lab conditions are at atmospheric pressure — pressure effects on '
                                      'melting points are negligible without extreme pressure changes.'}},
           {'opts': [('It is a mixture of water, sugars, vitamins, acids and many other compounds — not a single '
                      'element or compound',
                      True),
                     ('Orange juice contains preservatives — these impurities make it impure', False),
                     ('It has not been distilled — only distilled liquids can be pure', False),
                     ('Orange juice changes colour — pure substances do not change colour', False)],
            'q': "Why is 'pure orange juice' not a pure substance in the chemical sense?",
            'wrong_explanations': {1: "Even 'pure' orange juice without added preservatives contains many dissolved "
                                      'compounds — it is always a mixture.',
                                   2: 'Distillation is one way to purify a liquid but is not the definition of purity '
                                      '— a single compound that has never been distilled can still be chemically pure.',
                                   3: 'Many pure substances change colour (e.g. copper sulfate changing from blue '
                                      'hydrated to white anhydrous on heating).'}}],
  'rp': None,
  'spec': '5.8.1.1',
  'summary': 'Define a pure substance in chemistry and use melting/boiling point data to assess purity.',
  'theory': [{'content': "In everyday language, 'pure' might mean clean or natural (e.g. 'pure orange juice').\n"
                         '\n'
                         'In CHEMISTRY, a PURE SUBSTANCE has a precise meaning:\n'
                         'A pure substance contains only ONE type of element or compound — nothing else mixed in.\n'
                         'A pure substance has FIXED, SHARP melting and boiling points.\n'
                         '\n'
                         'Examples:\n'
                         'Pure water: boils at exactly 100°C, melts at exactly 0°C (at standard pressure).\n'
                         'Pure iron: melts at exactly 1538°C.\n'
                         'Pure ethanol: boils at exactly 78.4°C.\n'
                         '\n'
                         'IMPURE substances (mixtures):\n'
                         'Melt and boil over a RANGE of temperatures — not at a fixed point.\n'
                         'Melting point is LOWER than that of the pure substance (melting point depression).\n'
                         'Boiling point is HIGHER than that of the pure substance (boiling point elevation).\n'
                         '\n'
                         'This gives chemists a way to test purity.',
              'heading': 'What is a Pure Substance in Chemistry?'},
             {'content': 'MELTING POINT TEST:\n'
                         'Heat a small sample slowly and record the temperature at which it starts and finishes '
                         'melting.\n'
                         '\n'
                         'PURE substance: melts at a SHARP, PRECISE temperature — starts and finishes at the same '
                         'temperature.\n'
                         'Example: pure aspirin melts at exactly 135°C.\n'
                         '\n'
                         'IMPURE substance: melts over a RANGE of temperatures — starts melting below the expected '
                         'temperature.\n'
                         'Example: aspirin with impurity might melt from 128°C to 133°C.\n'
                         '\n'
                         'BOILING POINT TEST:\n'
                         'Pure substance: boils at a fixed temperature throughout.\n'
                         'Mixture: temperature changes during boiling as components evaporate at different rates.\n'
                         '\n'
                         'IDENTIFYING SUBSTANCES:\n'
                         'Comparing measured melting/boiling point to known data tables identifies the substance.\n'
                         'A substance that melts at 135°C and matches pure aspirin data → likely aspirin.\n'
                         '\n'
                         'This method is simple, quick and requires only a small sample — very useful in organic '
                         'chemistry.',
              'heading': 'Using Melting and Boiling Points to Test Purity'},
             {'content': 'PHARMACEUTICAL PURITY:\n'
                         'Medicines must be extremely pure — even tiny impurities could be toxic or reduce '
                         'effectiveness.\n'
                         'Thalidomide showed how critically purity (and stereochemistry) matters — one form was '
                         'therapeutic, another caused birth defects.\n'
                         '\n'
                         'FOOD PURITY:\n'
                         'Food standards require ingredients at specific purities.\n'
                         'Sugar (sucrose) in food must meet purity standards — impurities affect flavour and safety.\n'
                         '\n'
                         'INDUSTRIAL PURITY:\n'
                         'Some industrial processes require specific purity levels.\n'
                         'Semiconductors (silicon chips) need extremely high purity silicon — impurities disrupt '
                         'electrical properties.\n'
                         '\n'
                         'CHEMICAL ANALYSIS:\n'
                         'Chemists use melting and boiling points alongside other techniques (chromatography, '
                         'spectroscopy) to confirm identity and purity of compounds.',
              'heading': 'Purity in Context'}],
  'title': 'Pure Substances',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A formulation is NOT just any mixture — it is a mixture that has been DELIBERATELY designed with '
                    'SPECIFIC proportions for a specific purpose. An alloy like steel is a formulation (specific '
                    'amounts of iron and carbon). A random pile of chemicals is just a mixture.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'formulations',
  'key_note': 'Formulation: deliberately designed mixture with specific proportions for a purpose. Each component has '
              'a role. Examples: medicines (active ingredient + fillers + binders), paints, fuels, fertilisers, '
              'alloys, cleaning products, cosmetics. Changing proportions changes properties.',
  'matching': {'instruction': 'Match each component in a medicine tablet to its role.',
               'pairs': [('Active ingredient',
                          'The drug itself — must be an exact dose for safe and effective treatment'),
                         ('Binder', "Holds the tablet together so it doesn't crumble"),
                         ('Filler', 'Makes the tablet the right size and weight for handling'),
                         ('Coating', 'Controls release rate, protects from stomach acid or makes swallowing easier'),
                         ('Preservative', 'Prevents microbial growth — extends shelf life')],
               'title': 'Formulation Components'},
  'quiz': [{'opts': [('Toothpaste — a deliberately designed mixture of abrasives, fluoride, detergent and flavouring '
                      'in specific proportions',
                      True),
                     ('A beaker of tap water — water with dissolved minerals', False),
                     ('A pile of sand and gravel — a random mixture of particles', False),
                     ('Pure ethanol — a single compound with no additives', False)],
            'q': 'Which of the following is a formulation?',
            'wrong_explanations': {1: 'Tap water is a mixture but NOT deliberately designed/optimised — it is not a '
                                      'formulation.',
                                   2: 'Sand and gravel is a random mixture, not deliberately formulated for specific '
                                      'properties.',
                                   3: 'Pure ethanol is a single compound — not a mixture at all, so cannot be a '
                                      'formulation.'}},
           {'opts': [('Too little is ineffective — too much can be toxic. The correct dose treats the condition '
                      'safely.',
                      True),
                     ('The active ingredient determines the colour of the tablet — exact amounts give the right colour',
                      False),
                     ('Active ingredients are very expensive — exact amounts minimise cost only', False),
                     ("The active ingredient must balance the filler — otherwise the tablet won't be the right size",
                      False)],
            'q': 'Why must the amount of active ingredient in a medicine be precise?',
            'wrong_explanations': {1: 'Colour is determined by pigments or coatings — not the active ingredient in '
                                      'most cases.',
                                   2: 'Cost is a factor but safety and efficacy are the primary reasons for precise '
                                      'dosing.',
                                   3: 'Size is controlled by fillers — the dose of active ingredient is controlled by '
                                      'safety and efficacy requirements, not tablet size.'}}],
  'rp': None,
  'spec': '5.8.1.2',
  'summary': 'Define a formulation and give examples of common formulations.',
  'theory': [{'content': 'A FORMULATION is a MIXTURE that has been carefully designed so that it has the right '
                         'properties for a specific purpose.\n'
                         '\n'
                         'Each component in a formulation is present in a SPECIFIC, MEASURED AMOUNT — because the '
                         'proportions matter for the formulation to work correctly.\n'
                         '\n'
                         'Key distinction:\n'
                         'A random mixture of chemicals is NOT a formulation.\n'
                         'A FORMULATION is a deliberately designed, optimised mixture.\n'
                         '\n'
                         'Examples of formulations:\n'
                         'MEDICINES (tablets, creams): active ingredient + binders + fillers + coatings + '
                         'preservatives.\n'
                         'PAINTS: pigment + solvent + binder + additives (anti-mould, drying accelerants).\n'
                         'FUELS: blend of hydrocarbons + additives (anti-knock agents, stabilisers).\n'
                         'ALLOYS: specific proportions of metals for required properties.\n'
                         'FERTILISERS: specific ratios of NPK (nitrogen, phosphorus, potassium).\n'
                         'FOOD: specific recipes with controlled proportions.\n'
                         'CLEANING PRODUCTS: detergents + surfactants + enzymes + fragrance.\n'
                         'COSMETICS: emollients + emulsifiers + active ingredients + fragrances.',
              'heading': 'What is a Formulation?'},
             {'content': 'Each component in a formulation has a SPECIFIC ROLE:\n'
                         '\n'
                         'MEDICINE EXAMPLE — a tablet:\n'
                         'ACTIVE INGREDIENT: the drug itself — must be exact dose (too little = ineffective, too much '
                         '= toxic).\n'
                         'BINDER: holds the tablet together — must be enough to maintain shape but not prevent '
                         'dissolution.\n'
                         'FILLER: makes tablet correct size and weight.\n'
                         'COATING: controls release rate (e.g. slow-release medication), protects from stomach acid, '
                         'makes swallowing easier.\n'
                         'PRESERVATIVE: prevents microbial growth — must not react with active ingredient.\n'
                         '\n'
                         'PAINT EXAMPLE:\n'
                         'PIGMENT: provides colour — concentration determines shade.\n'
                         'BINDER: sticks pigment to surface when dried.\n'
                         'SOLVENT: keeps paint liquid for application — evaporates when drying.\n'
                         'ADDITIVES: improve properties (anti-mould, UV resistance, faster drying).\n'
                         '\n'
                         'Changing any proportion changes the properties — often for the worse. This is why '
                         'formulation chemistry requires careful research and testing.',
              'heading': 'Why Formulations Need Precise Proportions'},
             {'content': 'Formulations appear in many everyday contexts:\n'
                         '\n'
                         'PETROL AND DIESEL:\n'
                         'Blends of hydrocarbons + additives.\n'
                         'Anti-knock agents prevent premature ignition.\n'
                         'Corrosion inhibitors protect engine components.\n'
                         '\n'
                         'SPORTS DRINKS:\n'
                         'Electrolytes (sodium, potassium) at specific concentrations.\n'
                         'Sugars for energy at specific percentages.\n'
                         'Flavourings and pH adjusters.\n'
                         '\n'
                         'SUNSCREEN:\n'
                         'UV filters at specific concentrations — too little = ineffective, too much = skin '
                         'irritation.\n'
                         'Emollients for skin feel.\n'
                         'Preservatives.\n'
                         '\n'
                         'FERTILISERS:\n'
                         'Nitrogen, phosphorus and potassium in specific NPK ratios for different crops and soils.\n'
                         'Wrong ratios can damage soil and crops.\n'
                         '\n'
                         'CHEMICAL TESTS CAN IDENTIFY INDIVIDUAL COMPONENTS:\n'
                         'Chromatography can separate and identify components of a formulation.\n'
                         'Flame tests identify metal ions.\n'
                         'pH measurement identifies acids/alkalis in the mixture.',
              'heading': 'Identifying Formulations in Context'}],
  'title': 'Formulations',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "Rf values are ALWAYS between 0 and 1. If you get a value greater than 1, you've divided the WRONG "
                    'WAY — always divide substance distance BY solvent distance. Also: the baseline and spots must be '
                    'drawn in PENCIL not pen — pen ink contains dyes that would run with the solvent and confuse '
                    'results.',
  'equations': ['Rf = distance moved by substance ÷ distance moved by solvent front'],
  'fifas': [{'label': 'Rf Calculation',
             'question': 'In a chromatography experiment, a substance moves 7.2 cm. The solvent front moves 9.6 cm. '
                         'Calculate the Rf value.',
             'steps': [('F', 'Rf = distance moved by substance ÷ distance moved by solvent front'),
                       ('I', 'Rf = 7.2 ÷ 9.6'),
                       ('F', 'No unit conversion needed — Rf has no units'),
                       ('A', 'Rf = 0.75')]}],
  'higher': None,
  'id': 'chromatography',
  'key_note': 'Chromatography: separates mixtures by how far substances travel in solvent on paper. Rf = substance '
              'distance ÷ solvent front distance (always 0–1). Same Rf in same solvent = same substance. Pure '
              'substance = 1 spot. Mixture = multiple spots. Use pencil for baseline.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Rf value',
                          'Distance moved by substance ÷ distance moved by solvent — always between 0 and 1'),
                         ('Pure substance', 'Produces only one spot on the chromatogram'),
                         ('Mixture', 'Produces multiple spots — one for each component'),
                         ('Mobile phase', 'The solvent that moves up the chromatography paper'),
                         ('Stationary phase', 'The paper — does not move')],
               'title': 'Chromatography Concepts'},
  'quiz': [{'opts': [('The food colouring is a mixture of at least three different dyes', True),
                     ('The food colouring is impure — a pure substance should give three spots', False),
                     ('Three spots means three different solvents were used', False),
                     ('The paper was too wet — excess solvent caused multiple spots', False)],
            'q': 'A student runs chromatography on a food colouring and gets three spots. What does this tell them?',
            'wrong_explanations': {1: 'A pure substance gives ONE spot — three spots means at least three components '
                                      "are present. 'Impure' is not the right term — it is simply a mixture.",
                                   2: 'One solvent gives multiple spots if the sample is a mixture — the solvent '
                                      'choice affects Rf values, not the number of spots from a given sample.',
                                   3: "Wet paper might cause spots to merge — it wouldn't create more spots from a "
                                      'simpler mixture.'}},
           {'opts': [('If the spot is below the solvent level, the substances would dissolve directly into the solvent '
                      'and be washed away rather than travelling up the paper',
                      True),
                     ('The solvent would react with the substances if they touch', False),
                     ('The spot must be above to allow gravity to pull the solvent upward', False),
                     ('Substances only move upward — placing the spot above the solvent stops them moving down',
                      False)],
            'q': 'In chromatography, why must the initial spot be placed ABOVE the solvent level?',
            'wrong_explanations': {1: "The solvent doesn't react with the substances — it dissolves and carries them. "
                                      'But if the spot is submerged, it washes off directly into the solvent pool.',
                                   2: 'Capillary action (not gravity) drives the solvent up — gravity pulls DOWN, '
                                      'which would prevent upward movement.',
                                   3: 'If the spot were below the solvent, it would dissolve into the pooled solvent — '
                                      'not because of direction of movement.'}}],
  'rp': 'RP1 (Chemistry) — Investigate paper chromatography to separate and identify colours in inks or food dyes. '
        'Measure Rf values and compare to known reference substances.',
  'spec': '5.8.1.3',
  'summary': 'Describe paper chromatography, calculate Rf values and use chromatography to identify substances.',
  'theory': [{'content': 'CHROMATOGRAPHY separates mixtures of soluble substances based on how they distribute between '
                         'a STATIONARY PHASE and a MOBILE PHASE.\n'
                         '\n'
                         "STATIONARY PHASE: doesn't move — e.g. chromatography paper.\n"
                         'MOBILE PHASE: moves — e.g. solvent (water, ethanol etc.).\n'
                         '\n'
                         'PRINCIPLE:\n'
                         'Each substance in the mixture has different SOLUBILITY in the solvent and different AFFINITY '
                         'for the paper.\n'
                         'Substances that are more soluble in the solvent and less attracted to paper TRAVEL FURTHER.\n'
                         'Substances that are less soluble or more attracted to paper TRAVEL LESS FAR.\n'
                         'This separates the mixture into distinct SPOTS.\n'
                         '\n'
                         'PAPER CHROMATOGRAPHY:\n'
                         '1. Draw a pencil baseline near the bottom of chromatography paper (pencil — ink would run).\n'
                         '2. Spot the mixture onto the baseline.\n'
                         "3. Place in a small depth of solvent — below the baseline (so the spot isn't dissolved "
                         'directly).\n'
                         '4. Solvent rises up the paper by capillary action, carrying dissolved substances.\n'
                         '5. Remove when solvent front is near the top.\n'
                         '6. Mark the solvent front immediately (it evaporates).\n'
                         '7. Measure distances moved by each spot and the solvent front.',
              'heading': 'How Chromatography Works'},
             {'content': 'The RF VALUE (retention factor) is used to identify substances — each substance has a '
                         'characteristic Rf in a given solvent.\n'
                         '\n'
                         'FORMULA:\n'
                         'Rf = distance moved by substance ÷ distance moved by solvent front\n'
                         '\n'
                         'Rf values are always between 0 and 1.\n'
                         "Rf = 0: substance doesn't move at all (stays at baseline).\n"
                         'Rf = 1: substance moves exactly as far as the solvent front.\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Substance moves 4.5 cm. Solvent front moves 9.0 cm.\n'
                         'Rf = 4.5 ÷ 9.0 = 0.50\n'
                         '\n'
                         'IDENTIFICATION:\n'
                         'Compare Rf values to known reference data or reference spots run alongside the unknown.\n'
                         'If Rf matches a known substance in the same solvent → likely the same substance.\n'
                         '\n'
                         'CHROMATOGRAM:\n'
                         'The paper with spots after development.\n'
                         'Each spot represents a different component of the mixture.\n'
                         'A pure substance produces ONE spot.\n'
                         'A mixture produces MULTIPLE spots (one per component).',
              'heading': 'Rf Values'},
             {'content': 'FOOD TESTING:\n'
                         'Identify artificial colourings in food — compare to known reference spots.\n'
                         'Check for undeclared additives.\n'
                         '\n'
                         'FORENSIC SCIENCE:\n'
                         'Analyse ink from documents to detect forgeries — different pens use different inks.\n'
                         'Drug testing — identify substances in blood or urine samples.\n'
                         '\n'
                         'SPORTS DOPING:\n'
                         'Identify banned substances in athlete samples.\n'
                         'Chromatography separates the many compounds in blood/urine.\n'
                         '\n'
                         'PHARMACEUTICAL QUALITY CONTROL:\n'
                         'Verify purity of medicines — check for impurities.\n'
                         'Confirm active ingredient is present in correct amount.\n'
                         '\n'
                         'LIMITATIONS:\n'
                         'Some substances have similar Rf values — different substances can overlap.\n'
                         'Better to use TWO different solvents — if Rf values match in both, identification is more '
                         'reliable.\n'
                         'More advanced techniques (HPLC, GC-MS) give greater precision.',
              'heading': 'Applications of Chromatography'}],
  'title': 'Chromatography',
  'triple_only': None,
  'variables': [('Rf', 'Retention factor', '', '')]},
 {'common_mistake': 'Students confuse the splint tests. LIT splint → H₂ (squeaky pop). GLOWING splint → O₂ (relights). '
                    'The litmus paper for chlorine MUST be DAMP — dry litmus paper will NOT bleach. Also: limewater '
                    'turns milky with CO₂, not just any acidic gas.',
  'equations': ['CO₂ + Ca(OH)₂ → CaCO₃ + H₂O  (CO₂ test — limewater turns milky)',
                'Cl₂ + H₂O → HCl + HClO  (chlorine dissolves to form bleaching acid)'],
  'fifas': [],
  'higher': None,
  'id': 'testing-for-gases',
  'key_note': 'H₂: lit splint → squeaky pop. O₂: glowing splint → relights. CO₂: bubble through limewater → turns '
              'milky (CaCO₃ precipitate). Cl₂: damp litmus paper → bleaches white. All are simple, reliable tests for '
              'these four common gases.',
  'matching': {'instruction': 'Match each gas to its test and expected result.',
               'pairs': [('Hydrogen (H₂)', 'Lit splint → squeaky pop as hydrogen ignites in air'),
                         ('Oxygen (O₂)', 'Glowing splint → relights as oxygen supports combustion'),
                         ('Carbon dioxide (CO₂)', 'Bubble through limewater → turns milky (white CaCO₃ precipitate)'),
                         ('Chlorine (Cl₂)', 'Damp litmus paper → bleaches white')],
               'title': 'Gas Test Match'},
  'quiz': [{'opts': [('Oxygen — oxygen supports combustion and relights a glowing splint', True),
                     ('Hydrogen — hydrogen produces a squeaky pop with a lit splint', False),
                     ('Carbon dioxide — CO₂ extinguishes flames and would put the splint out', False),
                     ('Chlorine — chlorine bleaches and might react with the splint', False)],
            'q': 'A student collects a gas and holds a glowing splint near it. The splint relights. What gas is '
                 'present?',
            'wrong_explanations': {1: 'Hydrogen uses a LIT splint (not glowing) and produces a squeaky pop — not a '
                                      'relight.',
                                   2: 'CO₂ does NOT support combustion — it would extinguish the splint, not relight '
                                      'it.',
                                   3: "Chlorine bleaches damp paper — it doesn't reliably relight a glowing splint."}},
           {'opts': [('Chlorine must dissolve in water to form hypochlorous acid (HClO) — the actual bleaching agent',
                      True),
                     ('Dry litmus paper would catch fire in chlorine gas', False),
                     ('Chlorine is heavier than air and needs moist air to rise to the paper', False),
                     ('Damp paper absorbs more chlorine — making the colour change easier to see', False)],
            'q': 'Why must the litmus paper be damp when testing for chlorine?',
            'wrong_explanations': {1: 'Chlorine is not flammable and does not ignite paper — it is a toxic gas but not '
                                      'a fire hazard in this context.',
                                   2: 'Chlorine sinking (being denser than air) is a practical concern but not why the '
                                      'paper must be damp — the chemistry requires water for the bleaching reaction.',
                                   3: 'While damp paper might absorb more gas, the specific reason for dampness is the '
                                      'CHEMISTRY — water is needed to convert Cl₂ into the bleaching agent HClO.'}}],
  'rp': None,
  'spec': '5.8.2.1–5.8.2.4',
  'summary': 'Describe the tests for hydrogen, oxygen, carbon dioxide and chlorine.',
  'theory': [{'content': 'HYDROGEN (H₂):\n'
                         'Test: hold a LIT SPLINT near the mouth of a test tube containing the gas.\n'
                         'Positive result: SQUEAKY POP sound — the hydrogen ignites and burns rapidly with the oxygen '
                         'in the air.\n'
                         'Why: H₂ + O₂ → H₂O (explosive combustion).\n'
                         'Hydrogen is the lightest gas — produces a very fast, audible pop.\n'
                         '\n'
                         'OXYGEN (O₂):\n'
                         'Test: hold a GLOWING SPLINT near the mouth of a test tube containing the gas.\n'
                         'Positive result: the glowing splint RELIGHTS — bursts back into flame.\n'
                         'Why: oxygen supports combustion — a glowing ember in oxygen reignites and burns vigorously.\n'
                         'Note: a lit splint would simply burn faster in oxygen — the glowing splint test is more '
                         'distinctive.\n'
                         '\n'
                         'Remember the difference: LIT splint for H₂ (squeaky pop). GLOWING splint for O₂ (relights).',
              'heading': 'Tests for Hydrogen and Oxygen'},
             {'content': 'CARBON DIOXIDE (CO₂):\n'
                         'Test: bubble the gas through LIMEWATER (calcium hydroxide solution, Ca(OH)₂).\n'
                         'Positive result: limewater turns MILKY (cloudy/white precipitate forms).\n'
                         'Why: CO₂ + Ca(OH)₂ → CaCO₃ + H₂O\n'
                         'Calcium carbonate (CaCO₃) is insoluble — it forms as a white precipitate, making the '
                         'solution appear milky.\n'
                         'If excess CO₂ is bubbled through: the precipitate dissolves again → solution clears:\n'
                         'CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂ (soluble calcium hydrogencarbonate).\n'
                         '\n'
                         'CHLORINE (Cl₂):\n'
                         'Test: hold DAMP LITMUS PAPER (or damp universal indicator paper) near the gas.\n'
                         'Positive result: damp litmus paper is BLEACHED — turns white (loses its colour).\n'
                         'Why: chlorine dissolves in water to form hydrochloric acid and hypochlorous acid:\n'
                         'Cl₂ + H₂O → HCl + HClO\n'
                         'Hypochlorous acid (HClO) is a powerful bleaching agent — it destroys the dye molecules in '
                         'litmus.\n'
                         'Note: the paper must be DAMP — chlorine needs water to react and bleach.',
              'heading': 'Tests for Carbon Dioxide and Chlorine'},
             {'content': 'QUICK REFERENCE TABLE:\n'
                         '\n'
                         'HYDROGEN (H₂):\n'
                         'Test: lit splint.\n'
                         'Result: squeaky pop.\n'
                         '\n'
                         'OXYGEN (O₂):\n'
                         'Test: glowing splint.\n'
                         'Result: relights.\n'
                         '\n'
                         'CARBON DIOXIDE (CO₂):\n'
                         'Test: bubble through limewater.\n'
                         'Result: turns milky (white precipitate of CaCO₃).\n'
                         '\n'
                         'CHLORINE (Cl₂):\n'
                         'Test: damp litmus paper.\n'
                         'Result: bleaches (turns white).\n'
                         '\n'
                         'COMMON CONFUSIONS:\n'
                         'H₂ uses a LIT splint — if you use a glowing splint, it might not ignite the hydrogen '
                         'reliably.\n'
                         'O₂ uses a GLOWING splint — a lit splint would just burn faster (less distinctive test).\n'
                         "CO₂ test requires LIMEWATER specifically — water doesn't turn milky with CO₂.\n"
                         'Cl₂ requires DAMP litmus — dry litmus paper does NOT bleach (chlorine needs water to form '
                         'the bleaching agent).',
              'heading': 'Summary and Common Confusions'}],
  'title': 'Testing for Gases',
  'triple_only': None,
  'variables': []}],

"atmosphere": [{'common_mistake': 'The atmosphere is approximately 78% NITROGEN and 21% OXYGEN — not the other way round. Many '
                    'students think oxygen is the main component because we need it to breathe — but nitrogen is far '
                    'more abundant. CO₂ is only about 0.04% — tiny but critically important for the greenhouse effect '
                    'and photosynthesis.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'composition-of-atmosphere',
  'key_note': 'Atmosphere: ~78% N₂, ~21% O₂, ~0.9% Ar, ~0.04% CO₂. Balance maintained by carbon cycle '
              '(photosynthesis/respiration) and nitrogen cycle. Human activities increasing CO₂ — fossil fuels, '
              'deforestation. CO₂ small but crucial for photosynthesis and greenhouse effect.',
  'matching': {'instruction': 'Match each gas to its approximate percentage and role.',
               'pairs': [('Nitrogen (N₂)', '~78% — unreactive, largest component, cycled by bacteria'),
                         ('Oxygen (O₂)', '~21% — produced by photosynthesis, consumed by respiration and combustion'),
                         ('Argon (Ar)', '~0.9% — noble gas, unreactive, present since Earth formed'),
                         ('Carbon dioxide (CO₂)',
                          '~0.04% — greenhouse gas, essential for photosynthesis, rising due to fossil fuels')],
               'title': 'Atmospheric Gas — Percentage and Role'},
  'quiz': [{'opts': [('21% — approximately one fifth of the atmosphere', True),
                     ('78% — nitrogen makes up one fifth, oxygen makes up four fifths', False),
                     ('0.04% — this is the percentage of carbon dioxide', False),
                     ('50% — oxygen and nitrogen are approximately equal', False)],
            'q': 'Approximately what percentage of the atmosphere is oxygen?',
            'wrong_explanations': {1: '78% is NITROGEN, not oxygen — the two most abundant gases are often confused. '
                                      '4/5 = nitrogen, 1/5 = oxygen.',
                                   2: '0.04% is carbon dioxide — oxygen makes up 21%, not 0.04%.',
                                   3: 'Nitrogen (78%) and oxygen (21%) are very different percentages — nitrogen is '
                                      'about 4× more abundant.'}},
           {'opts': [('Photosynthesis — plants absorb CO₂ and convert it into glucose using sunlight', True),
                     ('Respiration — all organisms absorb CO₂ to release energy', False),
                     ('Combustion — burning fuels removes CO₂ from the air', False),
                     ('Nitrogen fixation — bacteria convert CO₂ to nitrogen compounds', False)],
            'q': 'Which process removes CO₂ from the atmosphere?',
            'wrong_explanations': {1: 'Respiration RELEASES CO₂ into the atmosphere — it does not remove it. '
                                      'Respiration breaks down glucose, consuming O₂ and releasing CO₂.',
                                   2: 'Combustion RELEASES CO₂ — it burns carbon-containing fuels to produce CO₂ and '
                                      'H₂O.',
                                   3: 'Nitrogen fixation converts N₂ to ammonium compounds — it has nothing to do with '
                                      'CO₂.'}}],
  'rp': None,
  'spec': '5.9.1.1',
  'summary': 'Describe the current composition of the atmosphere and how the proportions of gases are maintained.',
  'theory': [{'content': "The Earth's atmosphere has been approximately STABLE for the last 200 million years.\n"
                         '\n'
                         'APPROXIMATE COMPOSITION BY VOLUME:\n'
                         'NITROGEN (N₂): ~78%\n'
                         'OXYGEN (O₂): ~21%\n'
                         'ARGON (Ar): ~0.9%\n'
                         'CARBON DIOXIDE (CO₂): ~0.04% (rising due to human activity)\n'
                         'Other gases: water vapour (variable), neon, helium, methane etc. — tiny amounts.\n'
                         '\n'
                         'Simplified: approximately 4/5 nitrogen and 1/5 oxygen.\n'
                         '\n'
                         'The proportions of gases are maintained by:\n'
                         'PHOTOSYNTHESIS — plants absorb CO₂ and release O₂.\n'
                         'RESPIRATION — all living organisms absorb O₂ and release CO₂.\n'
                         'COMBUSTION — burning fuels consumes O₂ and produces CO₂.\n'
                         'NITROGEN CYCLE — bacteria fix and release N₂ from/to the atmosphere.',
              'heading': 'Current Composition of the Atmosphere'},
             {'content': 'The current balance is maintained by natural CYCLES:\n'
                         '\n'
                         'CARBON CYCLE:\n'
                         'CO₂ absorbed: photosynthesis (plants), dissolving in oceans.\n'
                         'CO₂ released: respiration, combustion, decomposition, volcanic activity.\n'
                         '\n'
                         'OXYGEN BALANCE:\n'
                         'O₂ produced: photosynthesis.\n'
                         'O₂ consumed: respiration, combustion, oxidation of metals.\n'
                         '\n'
                         'NITROGEN:\n'
                         "N₂ is extremely unreactive — doesn't participate in most reactions.\n"
                         'Fixed by nitrogen-fixing bacteria in soil (convert N₂ to nitrates for plants).\n'
                         'Released back by denitrifying bacteria.\n'
                         '\n'
                         'Human activities are disrupting these balances:\n'
                         'Burning fossil fuels → increases CO₂.\n'
                         'Deforestation → reduces CO₂ absorption and O₂ production.\n'
                         'Industrial processes → release various gases.',
              'heading': 'Maintaining the Balance'},
             {'content': 'ARGON (Ar) — 0.9%:\n'
                         'A noble gas — extremely unreactive, single atoms (monatomic).\n'
                         "Present in the atmosphere since the Earth formed — doesn't participate in any reactions.\n"
                         'Uses: filling light bulbs, welding (inert atmosphere prevents oxidation).\n'
                         '\n'
                         'WATER VAPOUR:\n'
                         'Variable amount — ranges from near 0% in deserts to ~4% in humid tropical air.\n'
                         'Evaporates from oceans, lakes, rivers.\n'
                         'Condenses to form clouds and rain.\n'
                         'Plays a crucial role in weather and climate.\n'
                         '\n'
                         'CARBON DIOXIDE — ~0.04%:\n'
                         'Small but critically important:\n'
                         'ESSENTIAL for photosynthesis — all plant life depends on it.\n'
                         'GREENHOUSE GAS — absorbs infrared radiation and warms the Earth.\n'
                         'DISSERVES IN OCEANS — oceans are a major carbon sink.\n'
                         'RISING due to fossil fuel combustion.',
              'heading': 'Noble Gases and Water Vapour'}],
  'title': 'The Composition of the Atmosphere',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The early atmosphere had LOTS of CO₂ and VERY LITTLE O₂ — the opposite of today. Oxygen was '
                    'produced by PHOTOSYNTHESIS from cyanobacteria — not by volcanoes. Volcanoes released CO₂, water '
                    'vapour and other gases but NOT oxygen.',
  'equations': ['6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂  (photosynthesis — released O₂ into atmosphere)'],
  'fifas': [],
  'higher': None,
  'id': 'early-atmosphere',
  'key_note': 'Early atmosphere: mainly CO₂ + H₂O vapour + some N₂, virtually no O₂. Volcanoes released gases '
              '(outgassing). O₂ increased due to photosynthesis by cyanobacteria ~2.7 bn years ago. CO₂ decreased: '
              'photosynthesis, dissolved in oceans, formed limestone. N₂ accumulated as other gases removed. Oceans '
              'formed when Earth cooled.',
  'matching': {'instruction': 'Match each change to the process that caused it.',
               'pairs': [('CO₂ decreased — dissolved in oceans',
                          'Earth cooled below 100°C — water vapour condensed to form oceans'),
                         ('CO₂ decreased — locked in rocks',
                          'Marine organisms made CaCO₃ shells → died → shells became limestone'),
                         ('O₂ increased', 'Cyanobacteria evolved ~2.7 billion years ago — photosynthesis released O₂'),
                         ('N₂ became dominant',
                          'Nitrogen is very unreactive — accumulated as CO₂ and H₂O were removed'),
                         ('Ozone layer formed',
                          'As O₂ built up, UV converted some O₂ to O₃ — shielded Earth from UV radiation')],
               'title': 'Timeline of Atmospheric Change'},
  'quiz': [{'opts': [('Photosynthesis by cyanobacteria — they evolved around 2.7 billion years ago and released O₂',
                      True),
                     ('Volcanic eruptions — volcanoes released oxygen along with other gases', False),
                     ('Decomposition of water vapour — UV radiation split water into hydrogen and oxygen', False),
                     ('Reaction of nitrogen with carbon dioxide — produced oxygen as a by-product', False)],
            'q': "What was the main source of oxygen in Earth's early atmosphere?",
            'wrong_explanations': {1: 'Volcanoes released CO₂, H₂O vapour, SO₂ and N₂ — NOT oxygen. Early volcanic '
                                      'activity actually maintained a low-oxygen environment.',
                                   2: 'UV photolysis of water is a minor contributor — the main mechanism was '
                                      'photosynthesis by early bacteria.',
                                   3: 'N₂ and CO₂ do not react under atmospheric conditions to produce O₂ — this '
                                      "reaction doesn't occur in the atmosphere."}},
           {'opts': [('CO₂ is soluble in water — the oceans dissolved large amounts of atmospheric CO₂', True),
                     ('The oceans cooled the CO₂, making it condense and fall as acid rain', False),
                     ('Water reacted with CO₂ to produce oxygen, which replaced the CO₂', False),
                     ('CO₂ sank to the ocean floor because it is denser than air', False)],
            'q': "Why did CO₂ levels decrease as Earth's oceans formed?",
            'wrong_explanations': {1: "CO₂ doesn't condense and fall as liquid at atmospheric temperatures — it "
                                      "remains a gas but dissolves in water. Acid rain does form but that's CO₂ "
                                      'dissolved in falling water, not condensation of CO₂.',
                                   2: 'Water + CO₂ → carbonic acid (H₂CO₃) — not O₂. Oxygen came from photosynthesis, '
                                      'not this reaction.',
                                   3: "Gases don't 'sink' to ocean floors — CO₂ dissolves IN the water rather than "
                                      'sinking as a liquid.'}}],
  'rp': None,
  'spec': '5.9.1.2–5.9.1.4',
  'summary': "Describe the evidence for how Earth's early atmosphere evolved to its present composition.",
  'theory': [{'content': 'The Earth formed approximately 4.6 billion years ago. Scientists believe the EARLY '
                         "ATMOSPHERE was very different from today's.\n"
                         '\n'
                         'EVIDENCE is LIMITED — there are no direct samples. Scientists piece together evidence from:\n'
                         'Rock records and the oldest minerals.\n'
                         'Studying the atmospheres of other planets (Mars and Venus have CO₂-rich atmospheres — '
                         'possibly similar to early Earth).\n'
                         'Isotope analysis of ancient rocks.\n'
                         '\n'
                         'BELIEVED COMPOSITION of the early atmosphere (~4 billion years ago):\n'
                         'MAINLY CARBON DIOXIDE (CO₂) — similar to Mars and Venus today.\n'
                         'Some water vapour (H₂O).\n'
                         'Some nitrogen (N₂).\n'
                         'Very little oxygen (O₂) — essentially none.\n'
                         'Possibly methane (CH₄) and ammonia (NH₃).\n'
                         '\n'
                         "SOURCE: intense volcanic activity released these gases from the Earth's interior — VOLCANIC "
                         'OUTGASSING.',
              'heading': 'The Early Atmosphere'},
             {'content': "The dramatic INCREASE IN OXYGEN is one of the most significant events in Earth's history.\n"
                         '\n'
                         'STAGE 1 — PHOTOSYNTHESIS:\n'
                         'About 2.7 billion years ago, CYANOBACTERIA (blue-green bacteria) evolved — the first '
                         'photosynthetic organisms.\n'
                         'They used CO₂ and sunlight to produce glucose and OXYGEN:\n'
                         '6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂\n'
                         'Oxygen released into the atmosphere.\n'
                         '\n'
                         'STAGE 2 — OXYGEN ACCUMULATES:\n'
                         'Initially, oxygen was absorbed by reacting with dissolved iron in oceans → iron oxide '
                         '(rusting), forming BANDED IRON FORMATIONS in rocks.\n'
                         'Also absorbed by reacting with surface rocks (oxidation).\n'
                         "Once these 'sinks' were saturated, oxygen began building up in the atmosphere.\n"
                         '\n'
                         'OVER BILLIONS OF YEARS:\n'
                         'Oxygen levels gradually rose.\n'
                         'As O₂ rose, an OZONE LAYER (O₃) formed in the upper atmosphere — shielding the Earth from UV '
                         'radiation.\n'
                         'This allowed more complex life to evolve on land (previously UV would have been lethal).\n'
                         '\n'
                         'HOW CO₂ DECREASED:\n'
                         'Photosynthesis removed CO₂.\n'
                         'CO₂ dissolved in the cooling oceans.\n'
                         'Marine organisms used dissolved CO₂ to make calcium carbonate (CaCO₃) shells — when they '
                         'died, shells became LIMESTONE rocks — locking carbon away.',
              'heading': 'How Oxygen Increased'},
             {'content': 'FORMATION OF OCEANS:\n'
                         'Early Earth was very hot — water existed only as steam.\n'
                         'As Earth cooled below 100°C, water vapour CONDENSED → formed the oceans.\n'
                         'Oceans dissolved large amounts of CO₂ → dramatically reduced CO₂ in the atmosphere.\n'
                         'This was a major step in changing the atmosphere.\n'
                         '\n'
                         'NITROGEN ACCUMULATION:\n'
                         'Nitrogen was present in the early atmosphere and gradually accumulated as:\n'
                         'CO₂ was removed (by photosynthesis and ocean absorption).\n'
                         "Nitrogen is very unreactive — it doesn't get removed by most geological or biological "
                         'processes.\n'
                         'This left nitrogen as the dominant gas.\n'
                         '\n'
                         'SUMMARY OF CHANGES:\n'
                         'Early: mainly CO₂, water vapour, some N₂, no O₂.\n'
                         'Oceans form: CO₂ dissolves, water vapour removed.\n'
                         'Cyanobacteria: photosynthesis removes more CO₂, releases O₂.\n'
                         'Ozone layer forms: protects surface, allows complex life.\n'
                         'Present: N₂ 78%, O₂ 21%, CO₂ only 0.04%.',
              'heading': 'Formation of Oceans and Nitrogen'}],
  'title': "The Earth's Early Atmosphere and How It Changed",
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The greenhouse effect is NATURAL and NECESSARY — without it Earth would be frozen. The PROBLEM is '
                    'ENHANCED greenhouse effect — human activities increasing greenhouse gas concentrations beyond '
                    'natural levels, causing additional warming. Always distinguish between the natural greenhouse '
                    'effect (beneficial) and the enhanced greenhouse effect (potentially harmful).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'greenhouse-gases',
  'key_note': 'Greenhouse effect: Sun heats Earth → Earth emits infrared → greenhouse gases absorb and re-emit it → '
              'Earth stays warm. Greenhouse gases: CO₂, CH₄, H₂O vapour, N₂O. Human causes: fossil fuels (CO₂), '
              'deforestation (CO₂), livestock (CH₄), landfill (CH₄). Climate change: rising temperatures, sea level '
              'rise, extreme weather.',
  'matching': {'instruction': 'Match each human activity to the greenhouse gas it increases.',
               'pairs': [('Burning fossil fuels', 'CO₂ — carbon stored underground released into atmosphere'),
                         ('Cattle farming', 'CH₄ (methane) — produced during digestion in ruminants'),
                         ('Landfill sites', 'CH₄ — organic waste decomposes anaerobically'),
                         ('Nitrogen fertilisers', 'N₂O (nitrous oxide) — bacteria convert excess fertiliser in soil'),
                         ('Deforestation',
                          'CO₂ — trees that absorbed CO₂ are burned or decay; fewer trees to absorb future CO₂')],
               'title': 'Human Activity → Greenhouse Gas'},
  'quiz': [{'opts': [("Without greenhouse gases, the Earth's infrared radiation would escape to space and the planet "
                      'would be approximately −18°C — too cold for life',
                      True),
                     ('The greenhouse effect produces oxygen from CO₂ — without it there would be no oxygen', False),
                     ('Greenhouse gases protect Earth from UV radiation — without them we would get radiation burns',
                      False),
                     ('The greenhouse effect drives photosynthesis by concentrating CO₂ near the surface', False)],
            'q': 'Why is the greenhouse effect necessary for life on Earth?',
            'wrong_explanations': {1: 'Oxygen comes from photosynthesis — not from the greenhouse effect.',
                                   2: 'UV protection is provided by the OZONE LAYER (O₃) in the stratosphere — not by '
                                      'greenhouse gases.',
                                   3: 'CO₂ is not concentrated near the surface by the greenhouse effect — it is mixed '
                                      'throughout the atmosphere.'}},
           {'opts': [('Livestock farming — cattle and sheep produce methane during digestion', True),
                     ('Burning coal — coal combustion releases methane as a by-product', False),
                     ('Using aerosol sprays — the propellants contain methane', False),
                     ('Driving petrol cars — incomplete combustion produces methane', False)],
            'q': 'Which human activity contributes most directly to increased methane levels in the atmosphere?',
            'wrong_explanations': {1: 'Coal combustion primarily releases CO₂ — not methane. Some methane is released '
                                      'during coal mining but combustion produces CO₂.',
                                   2: 'Modern aerosol propellants are typically hydrocarbons like butane/propane or '
                                      'HFCs — not methane.',
                                   3: 'Petrol car incomplete combustion produces CO and particulates — not significant '
                                      'amounts of methane.'}}],
  'rp': None,
  'spec': '5.9.2.1–5.9.2.4',
  'summary': 'Describe the greenhouse effect, human activities that increase greenhouse gases and the impact of '
             'climate change.',
  'theory': [{'content': 'The GREENHOUSE EFFECT is the natural process that keeps the Earth warm enough to support '
                         'life.\n'
                         '\n'
                         'HOW IT WORKS:\n'
                         '1. Short-wave radiation (visible light and UV) from the Sun passes through the atmosphere '
                         "and warms the Earth's surface.\n"
                         "2. The Earth's surface emits INFRARED (heat) radiation back upward.\n"
                         '3. GREENHOUSE GASES in the atmosphere ABSORB this infrared radiation and re-emit it in all '
                         'directions — including back towards Earth.\n'
                         '4. This traps heat and warms the Earth — without it, Earth would be approximately −18°C.\n'
                         '\n'
                         'GREENHOUSE GASES include:\n'
                         'WATER VAPOUR (H₂O) — biggest natural greenhouse gas.\n'
                         'CARBON DIOXIDE (CO₂) — from combustion, respiration, deforestation.\n'
                         'METHANE (CH₄) — from livestock, landfill, natural gas leaks, wetlands.\n'
                         'NITROUS OXIDE (N₂O) — from agriculture, fertilisers.\n'
                         '\n'
                         'Without the greenhouse effect: Earth would be too cold for life.\n'
                         'With TOO MUCH greenhouse effect: global warming → climate change.',
              'heading': 'The Greenhouse Effect'},
             {'content': 'Human activities are INCREASING greenhouse gas concentrations beyond natural levels:\n'
                         '\n'
                         'CARBON DIOXIDE (CO₂):\n'
                         'BURNING FOSSIL FUELS — coal, oil, natural gas release CO₂ locked underground for millions of '
                         'years.\n'
                         'DEFORESTATION — trees absorb CO₂; removing them reduces absorption AND releases stored '
                         'carbon when burned or decomposed.\n'
                         'CEMENT PRODUCTION — CaCO₃ → CaO + CO₂ (decomposition releases CO₂).\n'
                         '\n'
                         'METHANE (CH₄):\n'
                         'LIVESTOCK (cattle and sheep) — produce methane during digestion (enteric fermentation).\n'
                         'LANDFILL SITES — decomposition of organic waste under anaerobic conditions produces '
                         'methane.\n'
                         'RICE PADDIES — anaerobic decomposition in flooded fields.\n'
                         'NATURAL GAS LEAKS from extraction and distribution.\n'
                         '\n'
                         'NITROUS OXIDE (N₂O):\n'
                         'NITROGEN FERTILISERS — bacteria convert excess fertiliser to N₂O.\n'
                         'AGRICULTURAL SOILS.',
              'heading': 'Human Activities Increasing Greenhouse Gases'},
             {'content': 'GLOBAL CLIMATE CHANGE:\n'
                         'Rising greenhouse gas levels increase the greenhouse effect → GLOBAL WARMING — rising '
                         'average global temperatures.\n'
                         '\n'
                         'EFFECTS of climate change:\n'
                         'MELTING ICE CAPS AND GLACIERS → rising sea levels → coastal flooding.\n'
                         'MORE EXTREME WEATHER — stronger storms, more intense rainfall, droughts.\n'
                         'HABITAT LOSS — ecosystems disrupted, species extinction risk.\n'
                         'OCEAN ACIDIFICATION — CO₂ dissolves in seawater to form carbonic acid → threatens coral '
                         'reefs and shellfish.\n'
                         'AGRICULTURAL DISRUPTION — changed growing seasons, droughts, flooding.\n'
                         '\n'
                         'CARBON FOOTPRINT:\n'
                         'The total amount of greenhouse gases (measured as CO₂ equivalent) produced by an individual, '
                         'organisation or product.\n'
                         '\n'
                         'REDUCING CARBON FOOTPRINT:\n'
                         'Renewable energy (wind, solar, hydroelectric) instead of fossil fuels.\n'
                         'Improve energy efficiency (insulation, LED lighting, efficient vehicles).\n'
                         'Electric vehicles.\n'
                         'Plant trees (reforestation).\n'
                         'Reduce meat consumption (livestock produce methane).\n'
                         'Carbon capture and storage (CCS).',
              'heading': 'Global Climate Change and Carbon Footprint'}],
  'title': 'Greenhouse Gases and Climate Change',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'CO (carbon monoxide) is produced by INCOMPLETE combustion. CO₂ is produced by COMPLETE '
                    'combustion. Both are colourless gases — but CO is toxic (binds to haemoglobin) while CO₂ is not '
                    'directly toxic at normal concentrations. Catalytic converters reduce CO and NOₓ but actually '
                    'INCREASE CO₂ (by converting CO to CO₂).',
  'equations': ['S + O₂ → SO₂  (sulfur impurity burning)',
                'N₂ + O₂ → 2NO  (in engines at high temperature)',
                '2CO + 2NO → 2CO₂ + N₂  (catalytic converter reaction)',
                'CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂  (acid rain dissolving limestone)'],
  'fifas': [],
  'higher': None,
  'id': 'atmospheric-pollutants',
  'key_note': 'Pollutants from fuel combustion: CO (toxic, incomplete combustion), SO₂ (acid rain, from sulfur in '
              'fuel), NOₓ (acid rain, smog, from N₂ + O₂ at high temperature), particulates (respiratory harm). Acid '
              'rain: damages limestone, kills aquatic life. Catalytic converters: convert CO + NOₓ → CO₂ + N₂.',
  'matching': {'instruction': 'Match each pollutant to its source and main effect.',
               'pairs': [('Carbon monoxide (CO)',
                          'Incomplete combustion — toxic gas that prevents oxygen transport in blood'),
                         ('Sulfur dioxide (SO₂)',
                          'Sulfur impurities in fuel burned — causes acid rain damaging buildings and ecosystems'),
                         ('Nitrogen oxides (NOₓ)', 'N₂ + O₂ at high engine temperatures — causes acid rain and smog'),
                         ('Particulates (soot)',
                          'Incomplete combustion — fine particles damage lungs and cause respiratory disease')],
               'title': 'Pollutant — Source and Effect'},
  'quiz': [{'opts': [('CO binds irreversibly to haemoglobin — preventing red blood cells from carrying oxygen, causing '
                      'suffocation even in small concentrations',
                      True),
                     ('CO is a coloured gas — it can be detected visually, making it more alarming', False),
                     ('CO is heavier than air — it sinks and accumulates at floor level where people breathe', False),
                     ('CO reacts with water in the lungs to form carbonic acid', False)],
            'q': 'Why is carbon monoxide (CO) particularly dangerous compared to carbon dioxide (CO₂)?',
            'wrong_explanations': {1: 'CO is COLOURLESS and ODOURLESS — this makes it MORE dangerous as it cannot be '
                                      'detected by sight or smell without a detector.',
                                   2: "CO has a density very similar to air — it doesn't strongly stratify, unlike "
                                      'some heavier gases.',
                                   3: 'CO does not react with water to form carbonic acid — that reaction is for CO₂. '
                                      'CO reacts with haemoglobin.'}},
           {'opts': [('They convert toxic CO and NOₓ to CO₂ and N₂ using platinum and rhodium catalysts', True),
                     ('They filter out solid particulates using a fine mesh — trapping soot before it leaves the '
                      'exhaust',
                      False),
                     ('They reduce all emissions including CO₂ — making cars more environmentally friendly overall',
                      False),
                     ('They add oxygen to the exhaust to ensure complete combustion of any remaining fuel', False)],
            'q': 'How do catalytic converters reduce air pollution from cars?',
            'wrong_explanations': {1: 'Particulate filters are separate devices — catalytic converters work by '
                                      'CHEMICAL REACTIONS, not filtration.',
                                   2: 'Catalytic converters actually INCREASE CO₂ (by converting CO to CO₂). They do '
                                      'NOT reduce CO₂ emissions.',
                                   3: "Catalysts work by providing alternative reaction pathways — they don't inject "
                                      'additional oxygen into the exhaust.'}}],
  'rp': None,
  'spec': '5.9.3.1–5.9.3.2',
  'summary': 'Describe the pollutants produced by burning fuels and their effects on health and environment.',
  'theory': [{'content': 'Burning FOSSIL FUELS releases several POLLUTANTS in addition to CO₂ and water:\n'
                         '\n'
                         'CARBON MONOXIDE (CO):\n'
                         'From INCOMPLETE COMBUSTION — insufficient oxygen.\n'
                         'COLOURLESS, ODOURLESS, TOXIC gas.\n'
                         'Binds to haemoglobin in red blood cells — prevents oxygen transport → can be fatal.\n'
                         'Measured by CO detectors in homes.\n'
                         '\n'
                         'SULFUR DIOXIDE (SO₂):\n'
                         'Fuels contain sulfur impurities → S + O₂ → SO₂ when burned.\n'
                         'Causes ACID RAIN when SO₂ reacts with water and oxygen in the atmosphere:\n'
                         'SO₂ + H₂O → H₂SO₃ (sulfurous acid) / SO₃ + H₂O → H₂SO₄ (sulfuric acid)\n'
                         'ACID RAIN effects: damages buildings/statues (limestone dissolves), kills trees, acidifies '
                         'lakes killing fish.\n'
                         'Also causes respiratory problems — irritates airways.\n'
                         '\n'
                         'NITROGEN OXIDES (NOₓ — mainly NO and NO₂):\n'
                         'Produced when N₂ and O₂ from air react at the high temperatures inside engines:\n'
                         'N₂ + O₂ → 2NO → oxidised to NO₂\n'
                         'NOₓ also causes ACID RAIN (nitric acid).\n'
                         'Contributes to SMOG and LOW-LEVEL OZONE (O₃) which irritates lungs.\n'
                         '\n'
                         'PARTICULATES (soot/carbon particles):\n'
                         'From incomplete combustion of fuels.\n'
                         'Very small particles that penetrate deep into lungs.\n'
                         'Cause respiratory disease, aggravate asthma.\n'
                         'Consciously contribute to GLOBAL DIMMING — reducing sunlight reaching Earth.',
              'heading': 'Pollutants from Combustion of Fuels'},
             {'content': 'ACID RAIN forms when sulfur dioxide (SO₂) and nitrogen oxides (NOₓ) dissolve in rainwater:\n'
                         '\n'
                         'FORMATION:\n'
                         'SO₂ + H₂O + ½O₂ → H₂SO₄ (sulfuric acid)\n'
                         '4NO₂ + O₂ + 2H₂O → 4HNO₃ (nitric acid)\n'
                         '\n'
                         'Normal rain is slightly acidic (pH ~5.6) due to dissolved CO₂.\n'
                         'Acid rain: pH typically 4–5 — 10× to 100× more acidic than normal rain.\n'
                         '\n'
                         'EFFECTS:\n'
                         'BUILDINGS AND STATUES: dissolves limestone and marble:\n'
                         'CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂\n'
                         'Irreplaceable historical buildings damaged.\n'
                         '\n'
                         'ECOSYSTEMS:\n'
                         'Lakes and rivers become too acidic for aquatic life — fish die.\n'
                         'Soil acidification → releases toxic aluminium ions → kills trees.\n'
                         'Forest die-back in areas downwind of industrial zones.\n'
                         '\n'
                         'HUMAN HEALTH:\n'
                         'SO₂ and NO₂ irritate respiratory system — worsen asthma, bronchitis.\n'
                         '\n'
                         'SOLUTIONS:\n'
                         'REMOVE SULFUR from fuels before burning (desulfurisation).\n'
                         'CATALYTIC CONVERTERS in cars — convert CO, NOₓ and unburned hydrocarbons to CO₂, N₂ and '
                         'H₂O.\n'
                         'SCRUBBERS in power station chimneys — spray calcium hydroxide to neutralise SO₂.',
              'heading': 'Acid Rain — Causes and Effects'},
             {'content': 'CATALYTIC CONVERTERS convert toxic exhaust gases to less harmful ones:\n'
                         '\n'
                         'PLATINUM AND RHODIUM catalysts:\n'
                         '2CO + 2NO → 2CO₂ + N₂\n'
                         '(toxic carbon monoxide + toxic nitrogen oxide → CO₂ + harmless nitrogen)\n'
                         '\n'
                         'Also convert unburned hydrocarbons:\n'
                         'Hydrocarbon + O₂ → CO₂ + H₂O\n'
                         '\n'
                         'Reduces: CO (toxic), NOₓ (acid rain, smog) and particulates.\n'
                         'Does NOT reduce CO₂ (a greenhouse gas) — actually increases CO₂ by converting CO to CO₂.\n'
                         '\n'
                         'OTHER SOLUTIONS:\n'
                         'LOW-SULFUR FUELS — reduce SO₂ at source.\n'
                         'PARTICULATE FILTERS in diesel vehicles.\n'
                         'ELECTRIC VEHICLES — no exhaust combustion pollutants (though power station emissions are a '
                         'separate issue).\n'
                         'IMPROVED ENGINE DESIGN — more complete combustion, less CO and particulates.\n'
                         'INTERNATIONAL AGREEMENTS — e.g. limits on SO₂ emissions from power stations.',
              'heading': 'Catalytic Converters and Reducing Pollution'}],
  'title': 'Atmospheric Pollutants from Fuels',
  'triple_only': None,
  'variables': []}],

"using-resources": [{'common_mistake': 'Sustainable development does NOT mean stopping all industrial activity — it means developing in '
                    'ways that preserve resources and environments for future generations. It balances economic, '
                    'environmental and social needs — not just environmental protection alone.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'earths-resources',
  'key_note': "Earth's resources: minerals, fossil fuels, water, biological materials. Non-renewable: finite, cannot "
              'be replaced quickly. Sustainable development: meet present needs without preventing future generations '
              'from meeting theirs. Green chemistry: minimise waste, use renewable feedstocks, reduce energy. '
              'Recycling and atom economy are key.',
  'matching': {'instruction': 'Sort each practice into sustainable or unsustainable.',
               'pairs': [('Sustainable', 'Recycling aluminium — uses 95% less energy than extracting from ore'),
                         ('Unsustainable', 'Burning fossil fuels at current rates — non-renewable, finite supply'),
                         ('Sustainable', 'Using bioplastics from plant materials — renewable feedstock'),
                         ('Unsustainable',
                          'Deforestation for agriculture — removes carbon sinks faster than they regrow'),
                         ('Sustainable', 'Designing reactions with high atom economy — less waste produced')],
               'title': 'Sustainable or Not Sustainable?'},
  'quiz': [{'opts': [('Meeting present needs without preventing future generations from meeting their own needs — '
                      'balancing economic, environmental and social factors',
                      True),
                     ('Stopping all chemical manufacturing to protect the environment', False),
                     ('Using only natural chemicals — avoiding synthetic compounds', False),
                     ('Developing countries should not industrialise — only developed nations can use resources',
                      False)],
            'q': "What does 'sustainable development' mean in chemistry?",
            'wrong_explanations': {1: 'Sustainable development explicitly does NOT mean stopping industrial activity — '
                                      'it means developing more responsibly.',
                                   2: 'Synthetic chemicals can be part of sustainable development if produced using '
                                      'renewable resources and efficient processes.',
                                   3: 'Sustainable development specifically requires EQUITY — all nations have the '
                                      'right to develop, but in sustainable ways.'}},
           {'opts': [('Recycling uses about 95% less electrical energy than electrolysis of molten aluminium oxide',
                      True),
                     ('Bauxite is not a natural resource — it is produced artificially', False),
                     ('Recycled aluminium is stronger than freshly extracted aluminium', False),
                     ('There is no bauxite left — all aluminium must now be recycled', False)],
            'q': 'Why is recycling aluminium more sustainable than extracting new aluminium from bauxite ore?',
            'wrong_explanations': {1: "Bauxite (aluminium ore) is a natural mineral found in the Earth's crust — it is "
                                      'a natural resource.',
                                   2: 'Recycled and fresh aluminium have the same properties — sustainability is about '
                                      'energy and resource use, not material strength.',
                                   3: 'Bauxite reserves still exist — but they are finite, and extraction is '
                                      'energy-intensive. The key advantage of recycling is energy saving.'}}],
  'rp': None,
  'spec': '5.10.1.1',
  'summary': "Describe how humans use the Earth's resources and the importance of sustainable development.",
  'theory': [{'content': 'Humans use NATURAL RESOURCES from the Earth — materials and energy obtained from the natural '
                         'environment.\n'
                         '\n'
                         'Types of resources:\n'
                         "MINERALS AND METALS — extracted from the Earth's crust (iron ore, aluminium ore, copper "
                         'ore).\n'
                         'FOSSIL FUELS — coal, oil, natural gas (non-renewable — takes millions of years to form).\n'
                         'AIR — nitrogen and oxygen extracted from air.\n'
                         'WATER — freshwater for drinking, industry, agriculture.\n'
                         'BIOLOGICAL RESOURCES — timber, plants, animals.\n'
                         '\n'
                         'RENEWABLE vs NON-RENEWABLE:\n'
                         'Non-renewable: fossil fuels, minerals, metals — finite, will run out. Formed over millions '
                         'of years.\n'
                         'Renewable: timber (regrows), some materials can be recycled, energy from sun/wind/water.\n'
                         '\n'
                         'Many resources are FINITE — once used, they cannot be replenished in human timescales.',
              'heading': "The Earth's Natural Resources"},
             {'content': 'SUSTAINABLE DEVELOPMENT means meeting the needs of the PRESENT without compromising the '
                         'ability of FUTURE GENERATIONS to meet their own needs.\n'
                         '\n'
                         'This requires balancing:\n'
                         'ECONOMIC GROWTH — industries and livelihoods.\n'
                         'ENVIRONMENTAL PROTECTION — not destroying ecosystems or depleting resources.\n'
                         'SOCIAL EQUITY — ensuring all people benefit fairly.\n'
                         '\n'
                         'APPLICATIONS IN CHEMISTRY:\n'
                         'GREEN CHEMISTRY — designing chemical processes that minimise waste, use renewable resources '
                         'and reduce energy consumption.\n'
                         'ATOM ECONOMY — designing reactions that convert as much of the reactants as possible into '
                         'the desired product (less waste).\n'
                         'USING RENEWABLE FEEDSTOCKS — e.g. bioplastics from plant materials rather than petroleum.\n'
                         'CARBON CAPTURE — storing CO₂ from fossil fuel burning to prevent atmospheric build-up.\n'
                         '\n'
                         'SUSTAINABLE USE OF METALS:\n'
                         'Recycle metals rather than mining new ore.\n'
                         'Develop more efficient extraction processes.\n'
                         'Find alternative materials.',
              'heading': 'Sustainable Development'},
             {'content': 'The GROWING GLOBAL POPULATION means:\n'
                         'More food needed → more agricultural land, more fertilisers.\n'
                         'More energy needed → more fossil fuels burned (rising CO₂).\n'
                         'More materials needed → more mining, more deforestation.\n'
                         'More waste produced → more landfill, more pollution.\n'
                         '\n'
                         'KEY CONFLICTS:\n'
                         'Extraction of metals: mining disrupts ecosystems, creates waste, uses energy.\n'
                         'Fossil fuels: vital energy source but non-renewable and cause climate change.\n'
                         'Agriculture: feeds billions but uses vast land, water and chemicals.\n'
                         '\n'
                         'Why chemistry is important for sustainability:\n'
                         'Chemists develop more efficient processes (less energy, less waste).\n'
                         'Create new materials to replace scarce ones.\n'
                         'Develop renewable energy technologies (solar cells, batteries, fuel cells).\n'
                         'Develop better pollution control.\n'
                         'Find ways to recycle and reuse materials.',
              'heading': 'Finite Resources and Human Impact'}],
  'title': "Using the Earth's Resources and Sustainable Development",
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Potable water is NOT the same as PURE water. Potable = safe to drink (low levels of dissolved '
                    'minerals and microbes). Pure = only H₂O. Tap water is potable but not chemically pure — it '
                    'contains dissolved calcium, chlorine, fluoride etc. Distilled water is pure but not ideal for '
                    'drinking long-term (lacks minerals).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'potable-water',
  'key_note': 'Potable water: safe to drink (not pure). UK fresh water treatment: sedimentation → filtration → '
              'chlorination. Desalination (seawater): distillation or reverse osmosis — expensive and '
              'energy-intensive. Sewage treatment: screening → sedimentation → aerobic digestion → sludge anaerobic '
              'digestion (produces biogas) → chlorination.',
  'matching': {'instruction': 'Match each water treatment step to what it removes.',
               'pairs': [('Sedimentation',
                          'Large particles and suspended solids — allowed to settle or clump and sink'),
                         ('Filtration (sand/gravel)',
                          'Finer particles and some microorganisms — physically filtered out'),
                         ('Chlorination', 'Harmful microorganisms (bacteria and viruses) — killed by chlorine'),
                         ('Screening (sewage)',
                          'Large solids — removed by physical screens at the start of sewage treatment'),
                         ('Anaerobic digestion',
                          'Organic matter in sludge — produces biogas (methane) as a useful by-product')],
               'title': 'Water Treatment Steps'},
  'quiz': [{'opts': [('Potable water contains low levels of dissolved minerals and is safe to drink — pure water '
                      'contains only H₂O molecules',
                      True),
                     ('Potable water has been boiled — pure water has not been heated', False),
                     ('Pure water is safe to drink — potable water contains pollutants', False),
                     ('Potable water is seawater that has been filtered — pure water comes from rainfall only', False)],
            'q': 'Why is potable water NOT the same as pure water?',
            'wrong_explanations': {1: 'Boiling is used in distillation to purify water — but potable water is not '
                                      'defined by whether it has been boiled.',
                                   2: "It's the other way round — PURE water is chemically pure (H₂O only). POTABLE "
                                      'water is safe to drink but contains minerals.',
                                   3: 'Potable water comes from rivers, reservoirs, boreholes — not primarily '
                                      'seawater. Pure water is the chemically pure form.'}},
           {'opts': [('Biogas (mainly methane) — can be used as a renewable fuel', True),
                     ('Pure water — the sludge is distilled', False),
                     ('Fertiliser only — no gas is produced anaerobically', False),
                     ('Chlorine — used to disinfect the remaining water', False)],
            'q': 'What useful product is obtained from anaerobic digestion of sewage sludge?',
            'wrong_explanations': {1: 'Distillation is used to purify water, not to treat sludge — the anaerobic '
                                      'digestion process produces GAS, not water.',
                                   2: 'Anaerobic digestion of sludge produces BOTH biogas AND digestate (solid '
                                      'fertiliser) — the gas is a key economic benefit.',
                                   3: 'Chlorine is added separately at the end of water treatment — it is not produced '
                                      'during anaerobic digestion.'}}],
  'rp': 'RP8 (Chemistry) — Analysis and purification of water samples from different sources, including testing for '
        'pH, dissolved ions (using flame tests or precipitation) and filtering/distillation.',
  'spec': '5.10.1.2–5.10.1.3',
  'summary': 'Describe how potable water is produced and how waste water is treated.',
  'theory': [{'content': 'POTABLE WATER is water that is SAFE TO DRINK — it has sufficiently low levels of dissolved '
                         'substances and microbes.\n'
                         '\n'
                         'Potable water is NOT the same as PURE water:\n'
                         'Pure water contains ONLY H₂O molecules — no dissolved salts, minerals, microbes.\n'
                         'Potable water contains low but acceptable levels of dissolved minerals — which are actually '
                         'needed for good health (calcium, magnesium, fluoride etc.).\n'
                         '\n'
                         'GLOBAL WATER AVAILABILITY:\n'
                         "Only ~3% of Earth's water is freshwater.\n"
                         'Of this, most is locked in ice caps — less than 1% is accessible freshwater.\n'
                         'Water scarcity affects billions of people.\n'
                         '\n'
                         'SOURCES OF WATER IN THE UK:\n'
                         'SURFACE WATER — rivers, lakes, reservoirs.\n'
                         'GROUND WATER — aquifers underground, accessed by wells and boreholes.\n'
                         'SEAWATER — can be desalinated (expensive and energy-intensive).',
              'heading': 'Potable Water'},
             {'content': 'UK fresh water treatment process:\n'
                         '\n'
                         'STEP 1 — SEDIMENTATION:\n'
                         'Water flows into large settling tanks.\n'
                         'Large particles and suspended solids SINK to the bottom (sedimentation).\n'
                         'Alternatively, a coagulant (e.g. aluminium sulfate) is added → particles clump together '
                         '(flocculation) → settle faster.\n'
                         '\n'
                         'STEP 2 — FILTRATION:\n'
                         'Water passes through sand and gravel filters.\n'
                         'Removes finer particles and some microorganisms.\n'
                         '\n'
                         'STEP 3 — CHLORINATION:\n'
                         'Small amounts of CHLORINE (or ozone/UV) added to kill harmful microorganisms (bacteria, '
                         'viruses).\n'
                         'Chlorine is very effective and maintains protection as water travels through pipes.\n'
                         '\n'
                         'RESULT: potable water — not pure, but safe to drink.\n'
                         '\n'
                         'PURIFYING SEAWATER — DESALINATION:\n'
                         'TWO METHODS:\n'
                         '1. DISTILLATION — boil seawater, condense steam → pure water. Expensive (high energy).\n'
                         '2. REVERSE OSMOSIS — force seawater through membranes that block dissolved salts. '
                         'Energy-intensive.\n'
                         'Used in water-scarce regions (Middle East, some islands).\n'
                         'Not widely used in UK — cheaper freshwater sources available.',
              'heading': 'Treating Fresh Water to Make it Potable'},
             {'content': 'WASTE WATER includes:\n'
                         'SEWAGE — water from toilets, drains, containing human waste, bacteria, organic matter.\n'
                         'AGRICULTURAL WASTE — nitrates, pesticides.\n'
                         'INDUSTRIAL WASTE — may contain heavy metals, chemicals.\n'
                         '\n'
                         'Must be treated before being released back into rivers or the sea.\n'
                         '\n'
                         'SEWAGE TREATMENT PROCESS:\n'
                         '\n'
                         'STEP 1 — SCREENING:\n'
                         'Large solids removed by screens/grilles.\n'
                         '\n'
                         'STEP 2 — SEDIMENTATION:\n'
                         'Remaining solids sink to form SLUDGE.\n'
                         'Liquid (effluent) is separated.\n'
                         '\n'
                         'STEP 3 — BIOLOGICAL TREATMENT:\n'
                         'Effluent undergoes AEROBIC DIGESTION — air is pumped through, aerobic bacteria break down '
                         'organic matter → CO₂ + H₂O.\n'
                         'Some plants also use anaerobic digestion.\n'
                         '\n'
                         'STEP 4 — SLUDGE TREATMENT:\n'
                         'SLUDGE undergoes ANAEROBIC DIGESTION — bacteria digest organic matter WITHOUT oxygen.\n'
                         'Produces BIOGAS (mainly methane) — can be used as fuel.\n'
                         'Remaining solids (digestate) can be used as fertiliser.\n'
                         '\n'
                         'FINAL STEP — CHLORINATION:\n'
                         'Effluent disinfected with chlorine before discharge to rivers/sea.',
              'heading': 'Waste Water Treatment'}],
  'title': 'Potable Water and Water Treatment',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'LCAs can be SUBJECTIVE — they depend on which factors are included and how they are weighted. A '
                    'company-funded LCA might not include all negative impacts. Always consider who has commissioned '
                    'the LCA and whether all stages and impacts are genuinely included. An LCA showing a product is '
                    "'green' in one respect might not account for harms in another.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'life-cycle-assessment',
  'key_note': 'LCA: evaluates environmental impact across all life stages — raw materials, manufacturing, use, '
              'disposal. Assesses energy, water, emissions, waste at each stage. Used to compare products — but '
              'results can be subjective. Cradle-to-grave analysis. Cotton bags need many reuses to offset high '
              'manufacturing impact.',
  'matching': {'instruction': 'Match each stage of an LCA to what it includes.',
               'pairs': [('Extracting raw materials',
                          'Mining, quarrying or farming — energy and land use to obtain starting materials'),
                         ('Manufacturing', 'Energy and resources used to make and package the product'),
                         ('Use phase', "Energy and water consumed during the product's working lifetime"),
                         ('Disposal', 'Whether the product goes to landfill, is recycled, incinerated or composted')],
               'title': 'LCA Stages'},
  'quiz': [{'opts': [('Many hundreds of uses — the large manufacturing footprint (water, energy for cotton growing) '
                      "means it needs to replace many plastic bags to 'break even'",
                      True),
                     ('Just one use — it is biodegradable so has no end-of-life impact', False),
                     ('Exactly 10 uses — most studies find this is the threshold', False),
                     ('The cotton bag always has lower impact — cotton is a natural material', False)],
            'q': 'A cotton tote bag has a higher environmental impact at the manufacturing stage than a plastic bag. '
                 'How many uses would the cotton bag need to have a lower overall LCA impact?',
            'wrong_explanations': {1: 'While a cotton bag does biodegrade, the very high energy and water use in '
                                      'cotton farming means it must be used hundreds of times to offset its '
                                      'manufacturing impact.',
                                   2: 'Studies suggest much higher numbers — some LCAs put the figure at 50–100+ uses, '
                                      'depending on methodology and region.',
                                   3: 'Natural does not always mean lower environmental impact — cotton is a '
                                      'water-intensive crop with significant agrochemical use.'}},
           {'opts': [('Different analysts may weight factors differently, include different stages, or use different '
                      'data on energy sources — making LCAs subjective',
                      True),
                     ('LCAs are always objective — differences come only from measurement errors', False),
                     ('One LCA might use a metric system and the other imperial units', False),
                     ("Products change over time — different LCAs are done at different stages of the product's design",
                      False)],
            'q': 'Why might two different LCAs of the same product reach different conclusions?',
            'wrong_explanations': {1: 'LCAs are NOT fully objective — the choice of which factors to include and how '
                                      'to weight them introduces significant subjectivity.',
                                   2: 'Unit choice could cause calculation errors but is not the fundamental reason '
                                      'for different conclusions — weighting and scope of analysis are the main '
                                      'causes.',
                                   3: 'While products do evolve, LCAs for the same version of a product can still '
                                      'differ based on methodology and scope.'}}],
  'rp': None,
  'spec': '5.10.2.1',
  'summary': 'Describe what a life cycle assessment is and how it is used to evaluate the environmental impact of '
             'products.',
  'theory': [{'content': 'A LIFE CYCLE ASSESSMENT (LCA) evaluates the TOTAL ENVIRONMENTAL IMPACT of a product through '
                         'ALL stages of its life — from raw material extraction to disposal.\n'
                         '\n'
                         "Also called a 'cradle-to-grave' assessment.\n"
                         '\n'
                         'The FOUR STAGES assessed:\n'
                         '1. EXTRACTING AND PROCESSING RAW MATERIALS — mining, farming, quarrying.\n'
                         '2. MANUFACTURING AND PACKAGING — energy and materials used in production.\n'
                         "3. USE — energy, water and other resources used during the product's lifetime.\n"
                         '4. DISPOSAL — landfill, recycling, incineration, composting.\n'
                         '\n'
                         'LCAs assess the ENVIRONMENTAL COSTS at each stage:\n'
                         'Energy consumption.\n'
                         'Water use.\n'
                         'Greenhouse gas emissions (carbon footprint).\n'
                         'Waste produced.\n'
                         'Pollution to air, water and land.\n'
                         'Resource depletion.',
              'heading': 'What is a Life Cycle Assessment?'},
             {'content': 'LCAs allow comparison of ALTERNATIVES — e.g. plastic bags vs paper bags vs cotton tote '
                         'bags.\n'
                         '\n'
                         'EXAMPLE — Carrier bags:\n'
                         'PLASTIC BAG: uses petroleum (non-renewable), manufactured quickly, lightweight (low '
                         'transport emissions), lasts for years if reused, takes ~450 years to degrade in landfill.\n'
                         'PAPER BAG: uses trees (renewable if sustainably managed), more energy to manufacture, '
                         'heavier (more transport emissions), biodegrades quickly.\n'
                         'COTTON TOTE: very high energy and water use to grow cotton and manufacture, must be reused '
                         'MANY times to offset its higher manufacturing impact — but durable.\n'
                         '\n'
                         "The LCA shows that 'eco-friendly' is complex:\n"
                         'Paper bags are NOT always better than plastic if manufacturing emissions are included.\n'
                         'Cotton bags need to be reused hundreds of times to have lower impact than plastic.\n'
                         '\n'
                         'SUBJECTIVITY IN LCAs:\n'
                         'Not all impacts are easy to quantify (e.g. harm to wildlife from plastic litter).\n'
                         'Different LCAs can reach different conclusions depending on which factors are weighted.\n'
                         'Some factors are difficult to compare (e.g. CO₂ vs water use vs land use).',
              'heading': 'Using LCA to Compare Products'},
             {'content': 'LIMITATIONS:\n'
                         'COMPLEXITY — gathering data for all stages is difficult and time-consuming.\n'
                         'SUBJECTIVITY — different analysts may weight factors differently.\n'
                         'VARIABLE DATA — energy sources differ by country (renewable vs coal), changing outcomes.\n'
                         'NOT ALL IMPACTS QUANTIFIABLE — e.g. harm to ecosystems, aesthetic impacts.\n'
                         'POSSIBLE BIAS — companies may commission LCAs that present their products favourably.\n'
                         '\n'
                         'USES:\n'
                         'HELP CONSUMERS choose more sustainable products.\n'
                         'GUIDE MANUFACTURERS to redesign products for lower environmental impact.\n'
                         'INFORM POLICY — governments use LCAs to set regulations (e.g. minimum recycled content).\n'
                         "IDENTIFY 'HOT SPOTS' — stages with the highest environmental impact → target improvements.\n"
                         '\n'
                         'GREEN CHEMISTRY uses LCA principles — designing reactions and products with:\n'
                         'Lower energy consumption.\n'
                         'Fewer toxic by-products.\n'
                         'Renewable feedstocks.\n'
                         'Higher atom economy (less waste).',
              'heading': 'Limitations and Uses of LCAs'}],
  'title': 'Life Cycle Assessment',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The Three Rs are in ORDER OF PREFERENCE: Reduce is BEST (prevent waste), then Reuse, then '
                    'Recycle. Recycling, while better than landfill, still requires energy and is the LEAST preferred '
                    'of the three. Students often treat recycling as the most important R — but reducing consumption '
                    'is actually the most effective strategy.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'reducing-use-of-resources',
  'key_note': 'Three Rs: Reduce (best — prevent waste), Reuse (second — extend life), Recycle (third — recover '
              'material). Metal recycling saves huge amounts of energy: aluminium ~95% energy saving. Glass can be '
              'recycled indefinitely. Plastic recycling complex — many types. Recycling conserves finite resources and '
              'reduces environmental impact.',
  'matching': {'instruction': 'Match each example to the correct R (in order: Reduce > Reuse > Recycle).',
               'pairs': [('Reduce', 'Buying products with minimal packaging — less waste created in the first place'),
                         ('Reuse', 'Using a refillable water bottle instead of single-use plastic bottles'),
                         ('Reuse',
                          'Buying second-hand clothes instead of new — extends product life without reprocessing'),
                         ('Recycle', 'Melting aluminium cans to make new aluminium products — recovers the material'),
                         ('Reduce',
                          'Switching off lights when leaving a room — less energy used, fewer resources consumed')],
               'title': 'Three Rs — Order of Preference'},
  'quiz': [{'opts': [('Extracting aluminium requires electrolysis of molten Al₂O₃ at ~950°C — enormous electrical '
                      'energy. Recycling just needs melting (~660°C) — saving ~95% of the energy.',
                      True),
                     ('Recycled aluminium is already in the pure metal form — no chemical reduction needed', False),
                     ('Bauxite ore is found underground — mining it uses more energy than melting aluminium', False),
                     ('The electrolysis of bauxite produces toxic by-products that recycling avoids', False)],
            'q': 'Why is recycling aluminium so much more energy-efficient than making aluminium from bauxite ore?',
            'wrong_explanations': {1: 'Recycled aluminium IS in pure metal form — but the energy saving is primarily '
                                      'about avoiding HIGH-TEMPERATURE ELECTROLYSIS, not just about the chemical form.',
                                   2: 'Mining energy is significant but the PRIMARY energy cost is the ELECTROLYSIS '
                                      'process — which recycling completely avoids.',
                                   3: 'Electrolysis of aluminium oxide does produce oxygen as a by-product (which '
                                      "reacts with anodes) — but the main reason for recycling's efficiency is energy, "
                                      'not toxicity avoidance.'}},
           {'opts': [('Reduce — preventing waste from being created is better than managing it after creation', True),
                     ('Recycle — recovering materials is the most important environmental action', False),
                     ("Reuse — extending a product's life avoids both production and disposal impacts", False),
                     ('All three are equally important — there is no hierarchy', False)],
            'q': 'In the Three Rs hierarchy, which is the MOST beneficial environmental option?',
            'wrong_explanations': {1: 'Recycling is valuable but requires energy for reprocessing — it is the LEAST '
                                      'preferred of the three. Reduction prevents the problem entirely.',
                                   2: 'Reuse is more beneficial than recycling (no reprocessing energy needed) but '
                                      'REDUCING is even better still.',
                                   3: 'The Three Rs ARE ranked in priority order: Reduce > Reuse > Recycle. Reduce is '
                                      'the most effective because it prevents resource use from occurring.'}}],
  'rp': None,
  'spec': '5.10.2.2',
  'summary': 'Describe how resources can be conserved through reduction, reuse and recycling.',
  'theory': [{'content': 'The THREE Rs provide a hierarchy for conserving resources — listed in order of environmental '
                         'benefit (most beneficial first):\n'
                         '\n'
                         '1. REDUCE — use less in the first place.\n'
                         'BEST option — prevents waste from being generated.\n'
                         'Examples: buy products with less packaging, use less energy, choose longer-lasting '
                         'products.\n'
                         '\n'
                         '2. REUSE — use the same item multiple times.\n'
                         'SECOND BEST — extends product life without reprocessing.\n'
                         'Examples: reusable bags, bottles, rechargeable batteries, second-hand goods, repairing '
                         'products.\n'
                         '\n'
                         '3. RECYCLE — recover materials from waste and remake into new products.\n'
                         'LESS PREFERRED than reduce/reuse — requires energy for reprocessing.\n'
                         'Better than disposal — conserves raw materials, uses less energy than extracting virgin '
                         'materials.\n'
                         'Examples: paper, glass, metals, some plastics.',
              'heading': 'The Three Rs — Reduce, Reuse, Recycle'},
             {'content': 'METALS are particularly important to recycle because:\n'
                         'MINING ores is energy-intensive, disruptive to landscapes and produces waste.\n'
                         'Metal ores are FINITE — they will eventually run out.\n'
                         'Recycling uses MUCH LESS ENERGY than extraction:\n'
                         'Aluminium: recycling uses ~5% of the energy needed for electrolysis of Al₂O₃.\n'
                         'Steel (iron): recycling uses ~30% of the energy of making steel from iron ore.\n'
                         '\n'
                         'ALUMINIUM RECYCLING:\n'
                         'Aluminium is extracted by electrolysis (very high energy cost).\n'
                         'Recycled aluminium: simply melt and reform — energy saving of ~95%.\n'
                         '\n'
                         'COPPER RECYCLING:\n'
                         'Copper is valuable and relatively scarce.\n'
                         'Recycling saves mining energy and preserves ore deposits.\n'
                         '\n'
                         'CHALLENGES:\n'
                         'Not all metals can be easily separated from mixtures.\n'
                         'Some products contain many different metals — sorting is difficult.\n'
                         'Quality of recycled metal may be lower than virgin metal in some applications.',
              'heading': 'Recycling Metals'},
             {'content': 'GLASS:\n'
                         'Made from sand (silicon dioxide) — a finite resource.\n'
                         'Recycled glass melts at lower temperature than making from scratch → energy saving.\n'
                         'Can be recycled indefinitely without loss of quality.\n'
                         '\n'
                         'PAPER:\n'
                         'Made from trees — if not sustainably managed, causes deforestation.\n'
                         'Recycling saves trees and energy.\n'
                         'Recycled paper quality decreases with each cycle (fibres shorten).\n'
                         '\n'
                         'PLASTICS:\n'
                         'Most plastics are made from fossil fuels — non-renewable.\n'
                         'Recycling reduces demand for new plastic production.\n'
                         'COMPLEX — many different polymer types need to be sorted (PETE, HDPE etc.).\n'
                         'Some plastics can only be recycled a limited number of times.\n'
                         'Alternatives: bioplastics from renewable resources, compostable plastics.\n'
                         '\n'
                         'BIODEGRADABLE MATERIALS:\n'
                         'Break down naturally — less landfill.\n'
                         'But may still produce greenhouse gases (methane) if they decompose anaerobically in '
                         'landfill.\n'
                         '\n'
                         'WHY RECYCLING IS IMPORTANT FOR SUSTAINABILITY:\n'
                         'Reduces demand for new raw material extraction.\n'
                         'Saves energy compared to production from raw materials.\n'
                         'Reduces landfill and pollution.\n'
                         'Extends the useful life of finite resources.',
              'heading': 'Recycling Other Materials'}],
  'title': 'Ways of Reducing the Use of Resources',
  'triple_only': None,
  'variables': []}],

}
