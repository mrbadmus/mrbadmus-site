# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `a-balanced-diet` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'a-balanced-diet'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'a-balanced-diet',
 'title': 'A balanced diet',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'CLASSIFY',
 'covers': ['KS3.B.NUT.01'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 1},
             {'id': 'substances-and-reactions', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': [],
 'assumes': [],
 'references': ['food-tests',
                'when-diet-goes-wrong',
                {'unit': 'P1',
                 'lesson': 'energy-stores',
                 'label': 'Energy stores',
                 'why': 'Where the chemical store in food is developed as energy rather than as '
                        'nutrition.'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Nutrient requirements, malnutrition, and the biochemistry of carbohydrates, '
                'lipids and proteins as polymers.',
 'big_question': 'What does “balanced” actually mean for a diet?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'One orange', 'done_when': 'committed'},
          {'anchor': 's-plate',
           'short': 'BENCH',
           'label': 'Build a day',
           'done_when': 'all_seven_committed_and_opened'},
          {'anchor': 's-nutrients',
           'short': 'SEVEN',
           'label': 'The seven',
           'mirrors': 's-plate',
           'done_when': 'all_seven_committed_and_opened'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two plates. One of them will kill you in about four months.',
                'prompt': 'Plate A is white rice, chicken, oil, water and salt, every day, nothing '
                          'else. Plate B is the same food plus one orange. The person eating Plate '
                          'A dies. The person eating Plate B is fine.',
                'commit': 'If you had to guess, what in the orange saves the person on Plate B?',
                'options': ['A tiny vital substance', 'A bit more energy'],
                'reveal': 'So balance is not about equal amounts. Next: set seven nutrients to the '
                          'amounts you think a day needs, then see the real ones.',
                'guess': True,
                'replies': ['Just 50 mg of vitamin C, a tiny fraction of the meal. Without it the '
                            'body cannot build the protein that holds your body together.',
                            'The rice and oil on Plate A are already full of energy. What the '
                            'plate lacks is a tiny amount of vitamin C.'],
                'answer': 0},
 'misconceptions': [{'id': 'DIET-01',
                     'statement': 'A balanced diet means equal amounts of each food group.',
                     'elicited_by': 'seven-bands',
                     'confronted_by': 'think-balanced'},
                    {'id': 'DIET-02',
                     'statement': 'Vitamins give you energy.',
                     'elicited_by': 'think-balanced',
                     'confronted_by': 'think-balanced'},
                    {'id': 'DIET-03',
                     'statement': 'Fat is bad for you, so a healthy diet has none in it.',
                     'elicited_by': 'think-balanced',
                     'confronted_by': 'think-balanced'}],
 'vocabulary': [{'term': 'nutrient',
                 'definition': 'A substance in food that the body needs in order to work, grow or '
                               'repair itself.',
                 'note': 'There are seven, and none of them is optional.'},
                {'term': 'carbohydrate',
                 'definition': 'The nutrient the body breaks down to glucose and respires first '
                               'for energy.',
                 'note': None},
                {'term': 'lipid',
                 'definition': 'Fats and oils: an energy store, an insulator, and the material '
                               'every cell membrane is built from.',
                 'note': '‘Lipid’ is the scientific word for fats and oils together.'},
                {'term': 'protein',
                 'definition': 'The nutrient broken into amino acids and rebuilt into muscle, '
                               'enzymes and antibodies. Growth and repair.',
                 'note': None},
                {'term': 'vitamin',
                 'definition': 'A small molecule needed in tiny amounts that makes particular '
                               'reactions in the body possible.',
                 'note': 'A vitamin carries no energy of its own.'},
                {'term': 'mineral',
                 'definition': 'An element the body builds into a structure or a carrier — calcium '
                               'into bone, iron into haemoglobin.',
                 'note': None},
                {'term': 'dietary fibre',
                 'definition': 'Plant material the body cannot digest, which gives the gut muscles '
                               'something to push against.',
                 'note': None},
                {'term': 'deficiency',
                 'definition': 'Going short of one particular nutrient, and the specific illness '
                               'that follows from it.',
                 'note': None}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'seven-bands', 'anchor': 's-plate'},
          {'type': 'comparison',
           'anchor': 's-nutrients',
           'eyebrow': 'The seven',
           'eyebrow_tone': 'accent-text',
           'statement': 'What each one is for, and what goes wrong without it.',
           'ground': 'band',
           'columns': [{'caption': 'What your body does with it', 'tone': 'on-dark'},
                       {'caption': 'Without enough', 'tone': 'alert'}],
           'row_tones': ['ink', 'ink-body'],
           'rows': [{'name': 'Carbohydrate',
                     'cells': ['Broken down to glucose and respired for energy. The store the body '
                               'reaches for first.',
                               'Tiredness, and the body starts breaking down its own fat and then '
                               'its own protein for fuel.']},
                    {'name': 'Lipid',
                     'cells': ['Energy store, insulation, and the raw material of every cell '
                               'membrane. Carries vitamins A, D, E and K.',
                               'Those four vitamins cannot be absorbed. Skin and nerves are '
                               'affected before anything else shows.']},
                    {'name': 'Protein',
                     'cells': ['Broken into amino acids and rebuilt into muscle, enzymes, '
                               'antibodies and haemoglobin. Growth and repair.',
                               'Growth stops, wounds heal slowly, and fluid collects in the '
                               'tissues. Kwashiorkor in severe cases.']},
                    {'name': 'Vitamins',
                     'cells': ['Small molecules that make specific reactions possible. Thirteen of '
                               'them, each with its own job.',
                               'A specific deficiency disease per vitamin — scurvy without C, '
                               'rickets without D, beriberi without B1.']},
                    {'name': 'Minerals',
                     'cells': ['Elements built into structures and carriers: calcium into bone, '
                               'iron into haemoglobin, iodine into thyroid hormone.',
                               'Anaemia without iron, weak bones without calcium, goitre without '
                               'iodine.']},
                    {'name': 'Dietary fibre',
                     'cells': ['Not digested and not absorbed. Adds bulk so gut muscles have '
                               'something to grip and push.',
                               'Constipation, and a raised long-term risk of bowel disease.']},
                    {'name': 'Water',
                     'cells': ['The solvent every reaction in the body happens in, and the '
                               'transport medium for blood, urine and digestion.',
                               'Concentration and temperature control fail within hours. Death in '
                               'days — faster than for any other nutrient.']}],
           'key_fact': {'ref': 'balanced-means-targets', 'ground': 'card'}},
          {'type': 'misconception',
           'id': 'think-balanced',
           'anchor': 's-think',
           'targets': 'DIET-01'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'balanced-means-targets',
                'text': 'Balanced means each nutrient in the amount that nutrient needs — not the '
                        'same amount of each. Two of the seven are measured in hundreds of grams. '
                        'One is measured in milligrams. None of them is optional.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-balanced',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'DIET-01',
                 'statements': [{'quote': 'A balanced diet means equal amounts of each food group.',
                                 'body': ['Look at the two ends of the table you have just filled '
                                          'in. A 13-year-old needs roughly 300 g of carbohydrate '
                                          'and about 0.0000015 g of vitamin B12 in a day — a '
                                          'difference of two hundred million times. Eating them in '
                                          'equal amounts would mean 300 g of vitamin B12, which '
                                          'would be a year’s supply for about half a million '
                                          'people and would poison you long before you finished '
                                          'the plate. The word balanced describes a set of seven '
                                          'different targets being met at once, like seven dials '
                                          'each reading correctly. It has never meant seven equal '
                                          'piles.']},
                                {'quote': 'Vitamins give you energy.',
                                 'body': ['They do not, and this is worth being exact about. Only '
                                          'three of the seven nutrients release energy when they '
                                          'are respired: carbohydrate, lipid and protein. A '
                                          'vitamin tablet has an energy content of zero — you '
                                          'could eat the whole bottle and be no better fuelled '
                                          'than before. What vitamins do is let the reactions that '
                                          'release energy actually happen: vitamin B1 is part of '
                                          'the machinery that gets glucose into respiration, so '
                                          'someone short of it is exhausted despite eating plenty. '
                                          'Feeling tired because you lack a vitamin is not the '
                                          'same as feeling tired because you lack fuel, and the '
                                          'fix is different.']},
                                {'quote': 'Fat is bad for you, so a healthy diet has none in it.',
                                 'body': ['Lipids are a required nutrient, not a permitted vice. '
                                          'Every cell membrane in you — and there are about thirty '
                                          'trillion of them — is built from lipid, and vitamins A, '
                                          'D, E and K only dissolve in fat, so a diet with no '
                                          'lipid in it cannot deliver them however much you eat. '
                                          'What is true is that lipid carries more than twice the '
                                          'energy per gram of carbohydrate, so it is easy to take '
                                          'in far more energy than you need without noticing. That '
                                          'is a statement about quantity, not about the nutrient '
                                          'being harmful.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'At the bench · build a day',
                 'heading': 'Set the amounts yourself, then see the real ones',
                 'head_counter': {'format': '{n} of 7 set', 'total': 7, 'start': 0},
                 'prompt': 'For each of the seven, choose how much a 13-year-old needs in one day. '
                           'Commit to all seven before you open the answers.',
                 'bands': [{'id': 'lots',
                            'label': 'Hundreds of grams',
                            'miss_label': 'Actually hundreds of grams'},
                           {'id': 'some',
                            'label': 'Tens of grams',
                            'miss_label': 'Actually tens of grams'},
                           {'id': 'grams',
                            'label': 'A few grams',
                            'miss_label': 'Actually a few grams'},
                           {'id': 'trace',
                            'label': 'Milligrams or less',
                            'miss_label': 'Actually milligrams or less'}],
                 'hit_label': 'You had it',
                 'rows': [{'name': 'Carbohydrate',
                           'hint': 'bread, rice, pasta, potato',
                           'band': 'lots',
                           'mass': 'about 300 g',
                           'why': 'The bulk of the plate, and the body’s first choice of fuel. '
                                  'Almost every cell can respire glucose, and your brain can use '
                                  'very little else.'},
                          {'name': 'Lipid (fat and oil)',
                           'hint': 'oils, butter, nuts, oily fish',
                           'band': 'some',
                           'mass': 'about 70 g',
                           'why': 'Tens of grams, not hundreds — but not zero. It carries more '
                                  'than twice the energy per gram of carbohydrate, builds every '
                                  'cell membrane, and is the only way vitamins A, D, E and K can '
                                  'be absorbed.'},
                          {'name': 'Protein',
                           'hint': 'meat, fish, eggs, beans, lentils',
                           'band': 'some',
                           'mass': 'about 45 g',
                           'why': 'Tens of grams. Protein is the only nutrient that supplies the '
                                  'nitrogen needed to build and repair tissue, so a growing '
                                  '13-year-old needs a steady supply rather than a large one.'},
                          {'name': 'Vitamins',
                           'hint': 'fruit, vegetables, dairy, liver',
                           'band': 'trace',
                           'mass': 'about 0.2 g in total',
                           'why': 'A fifth of a gram covers all thirteen of them together. They '
                                  'release no energy at all — they let the reactions that do '
                                  'release energy actually run.'},
                          {'name': 'Minerals',
                           'hint': 'dairy, red meat, leafy greens, salt',
                           'band': 'grams',
                           'mass': 'about 5 g in total',
                           'why': 'A few grams, mostly calcium, and then iron, iodine and the rest '
                                  'in milligrams. Iron is 14 mg a day; miss it and your blood '
                                  'cannot carry oxygen properly.'},
                          {'name': 'Dietary fibre',
                           'hint': 'wholegrains, skins, pulses, vegetables',
                           'band': 'some',
                           'mass': 'about 25 g',
                           'why': 'Tens of grams of something you never absorb. It is not digested '
                                  'and not respired — it gives the gut muscles something to push '
                                  'against, which is what keeps everything moving.'},
                          {'name': 'Water',
                           'hint': 'drinks, and most of your food',
                           'band': 'lots',
                           'mass': 'about 2000 g',
                           'why': 'Two kilograms — by far the largest requirement on the list, and '
                                  'the one you die from fastest without. Every reaction in you '
                                  'happens in solution.'}],
                 'open_label': 'Show the real amounts',
                 'commit_format': '{n} of {total} committed',
                 'commit_done': 'Opened',
                 'verdict_eyebrow': 'Your day, scored',
                 'verdict_format': '{n} of {total} in the right band.',
                 'verdicts': {'all_same': 'You put all seven in the same band — which is exactly '
                                          'the wrong idea this lesson exists to kill. Read the '
                                          'amounts again: 2000 g of water and 0.2 g of vitamins '
                                          'are both correct, and they are ten thousand times '
                                          'apart.',
                              'close': 'Notice what the spread looks like: two nutrients in '
                                       'hundreds of grams, three in tens, one in single grams and '
                                       'one in milligrams. Balanced describes seven separate '
                                       'targets, not seven similar piles.',
                              'spread': 'The usual misses are lipid and fibre. Lipid feels like it '
                                        'should be near zero and is not; fibre feels like a trace '
                                        'and is 25 g — more than half a day’s protein, of '
                                        'something you never absorb at all.'},
                 'id': 'seven-bands',
                 'kind': 'band-commit'}],
 'ladder': {'recall': {'title': 'Rung 1 · Which three',
                       'q': 'Which nutrients release energy when the body respires them?',
                       'options': ['Carbohydrate, lipid and vitamins',
                                   'Carbohydrate, lipid and protein',
                                   'Carbohydrate and lipid only',
                                   'All seven, in different amounts'],
                       'answer': 1,
                       'feedback': {0: 'Vitamins release no energy. Protein does, so it belongs in '
                                       'the list.',
                                    2: 'Protein can be respired for energy too, as well as for '
                                       'growth.',
                                    3: 'Vitamins, minerals and water release no energy. Fibre '
                                       'gives almost none.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A student is tired all the time. They eat plenty of bread, pasta and '
                           'rice but almost no meat, fish or leafy vegetables. A doctor finds '
                           'their blood cannot carry oxygen properly. What is missing?',
                      'options': ['Iron, because it is needed to make haemoglobin',
                                  'Carbohydrate, because they need more fuel for energy',
                                  'Water, because they are dehydrated from drinking too little',
                                  'Vitamin C, because they are getting no fruit at all'],
                      'answer': 0,
                      'feedback': {1: 'They eat plenty of bread, pasta and rice. Fuel is not what '
                                      'is missing.',
                                   2: 'Water does not help blood carry oxygen. Iron makes '
                                      'haemoglobin, which does.',
                                   3: 'Too little vitamin C causes scurvy. Iron is needed to carry '
                                      'oxygen.'}},
            'explain': {'title': 'Rung 3 · Explain the two ends',
                        'q': 'A 13-year-old needs about 300 g of carbohydrate and about 14 mg of '
                             'iron each day — twenty thousand times less iron. Explain why both '
                             'are described as essential, and why the amounts are so different.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Both are essential because… but the amounts differ '
                                       'because…',
                        'success': ['Says carbohydrate is used as fuel and is respired '
                                    'continuously, so it is used up and must be replaced in bulk.',
                                    'Says iron is built into a structure — haemoglobin — rather '
                                    'than burnt, so it is not consumed in the same way.',
                                    'States that essential means the body cannot make it and fails '
                                    'without it, which is true of both regardless of amount.',
                                    'Names a consequence of going short of iron specifically, not '
                                    'just ‘being unhealthy’.',
                                    'Explicitly rejects the idea that a bigger requirement means a '
                                    'more important nutrient.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A sports drink advertises itself as ‘packed with energy-giving '
                             'vitamins’. The bottle lists sugars 32 g and eight vitamins. Say what '
                             'is wrong with the claim, what is actually supplying the energy, and '
                             'why the vitamins might still be worth having in it.',
                        'field_label': 'Your answer',
                        'placeholder': 'The claim is wrong because…',
                        'success': ['Says vitamins supply no energy, so ‘energy-giving vitamins’ '
                                    'is false as written.',
                                    'Identifies the 32 g of sugar as the actual source of the '
                                    'energy.',
                                    'Explains that some vitamins are part of the machinery that '
                                    'releases energy from glucose, which is probably what the '
                                    'claim is distorting.',
                                    'Says the vitamins are not useless — gives one honest reason '
                                    'they might belong in the drink.']}},
 'key_note': 'A healthy diet contains carbohydrate, lipid, protein, vitamins, minerals, dietary '
             'fibre and water. Carbohydrate, lipid and protein are the only three that release '
             'energy; protein also builds and repairs. The other four are needed in far smaller '
             'amounts and are needed just as absolutely — fibre and water are not even absorbed as '
             'fuel, and you cannot live without either.',
 'stretch': [{'type': 'explainer',
              'id': 'takaki-and-the-barley-ships',
              'text': 'In the 1880s the Japanese Navy was losing sailors to beriberi — weakness, '
                      'swelling, heart failure — while the Army was not. Takaki Kanehiro noticed '
                      'the two forces ate differently and ran what amounted to a fleet-sized '
                      'experiment: one ship on the usual polished white rice, another with barley '
                      'and vegetables added. The barley ship came home almost untouched. He had no '
                      'idea why, because vitamin B1 would not be identified for another forty '
                      'years, and he was ridiculed for suggesting food could be the cause of a '
                      'disease everyone assumed was an infection. The interesting part is that he '
                      'was right about the fix while being wrong about the mechanism, which '
                      'happens in science far more often than the tidy version admits.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why a milligram can matter as much as a gram?',
           'cta': 'Ask about this lesson',
           'anchor': 's-plate'},
 'convention_note': 'Figures are typical daily requirements for a 13-year-old and are for learning '
                    "the principle, not for planning anyone's meals. Individual needs differ; "
                    'dietary advice comes from a doctor or a registered dietitian.',
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
