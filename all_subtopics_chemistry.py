#!/usr/bin/env python3
"""
Chemistry subtopics — Combined Foundation
AQA 8464 Chemistry spec 5.0

Atomic Structure and Periodic Table: 12 subtopics (complete)
All other topics: stubs (to be built topic by topic)
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

"bonding": [],
"quantitative": [],
"chemical-changes": [],
"energy-changes": [],
"rates-equilibrium": [],
"organic": [],
"analysis": [],
"atmosphere": [],
"using-resources": [],

}
