# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `energy-in-food-and-what-you-need` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'energy-in-food-and-what-you-need'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'energy-in-food-and-what-you-need',
 'title': 'Energy in food and what you need',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'QUANTITATIVE',
 'covers': ['KS3.B.NUT.02a'],
 'touches': ['KS3.B.NUT.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'energy', 'level': 1}, {'id': 'cells-and-systems', 'level': 2}],
 'typical_year': 7,
 'typical_minutes': 50,
 'requires': ['a-balanced-diet'],
 'assumes': [],
 'references': [{'unit': 'P2',
                 'lesson': 'energy-in-food',
                 'label': 'Energy in food (Physics)',
                 'why': 'Where comparing energy values from labels in kJ is taught as physics — '
                        'the arithmetic and the units.'},
                {'unit': 'P2',
                 'lesson': 'calculating-energy-transferred',
                 'why': 'Where a joule is derived from power and time rather than counted off a '
                        'packet.'}],
 'connects_heading': 'Continues in Physics',
 'ks4_links': [],
 'ks4_becomes': 'Energy budgets, metabolic rate, and the effect of exercise and body composition '
                'on requirement.',
 'big_question': 'How much food does a body need in a day, and what decides it?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Same food', 'done_when': 'committed'},
          {'anchor': 's-ledger',
           'short': 'LEDGER',
           'label': 'Feed a day',
           'done_when': 'food_on_the_plate'},
          {'anchor': 's-maths',
           'short': 'MATHS',
           'label': 'On paper',
           'mirrors': 's-ledger',
           'done_when': 'food_on_the_plate'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two people eat exactly the same food for a month.',
                'prompt': 'A 68-year-old and a 25-year-old eat the same meals, in the same '
                          'portions, at the same times: about 11 000 kJ a day each. After a month, '
                          'one has gained mass and one has lost it.',
                'commit': 'If you had to guess, what explains the different outcome?',
                'options': ['How much energy each body needs', 'How well each body digests food'],
                'reveal': 'Next: feed five different people for a day and watch the same plate fit '
                          'one and not another.',
                'guess': True,
                'replies': ['Bodies need very different amounts of energy in a day. The same food '
                            'is more than enough for one and not enough for the other.',
                            'Digestion does vary a little, but not enough to turn the same meals '
                            'into a gain for one and a loss for the other. What differs is how '
                            'much energy each body needs.'],
                'answer': 0},
 'misconceptions': [{'id': 'DIET-06',
                     'statement': 'The energy in food gets used up and disappears.',
                     'elicited_by': 'feed-a-day',
                     'confronted_by': 'think-requirement'},
                    {'id': 'DIET-07',
                     'statement': 'Everyone needs about the same amount of food in a day.',
                     'elicited_by': 'feed-a-day',
                     'confronted_by': 'think-requirement'}],
 'vocabulary': [{'term': 'kilojoule',
                 'definition': 'The unit energy in food is measured in. One kilojoule is a '
                               'thousand joules.',
                 'note': 'Written kJ. A packet may also print kilocalories, an older unit for the '
                         'same thing — one kilocalorie is about 4.2 kJ.'},
                {'term': 'energy requirement',
                 'definition': 'The amount of energy a particular person needs to take in over a '
                               'day.',
                 'note': 'It belongs to the person, never to the food.'},
                {'term': 'intake',
                 'definition': 'The total energy in everything a person eats and drinks over a '
                               'day.',
                 'note': None},
                {'term': 'surplus',
                 'definition': 'Taking in more energy than you transfer, so the extra is stored.',
                 'note': None},
                {'term': 'shortfall',
                 'definition': 'Taking in less energy than you transfer, so stores are broken down '
                               'to make up the difference.',
                 'note': None}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'feed-a-day', 'anchor': 's-ledger'},
          {'type': 'rule',
           'anchor': 's-maths',
           'eyebrow': 'Doing it on paper',
           'statement': 'Three sums, and the units that make them behave.'},
          {'type': 'worked-example', 'id': 'sum-total'},
          {'type': 'worked-example', 'id': 'sum-compare'},
          {'type': 'worked-example', 'id': 'sum-share'},
          {'type': 'key-fact', 'ref': 'requirement-belongs-to-the-person'},
          {'type': 'rule',
           'id': 'forward-pointer',
           'eyebrow': 'Forward pointer · Physics',
           'statement': '',
           'close': 'You have used kJ here as a bookkeeping unit — energy in versus energy needed. '
                    'The full treatment belongs to Physics: what a joule actually is, how energy '
                    'is transferred rather than used up, and how to calculate it from power and '
                    'time.  Nothing here contradicts it; it is the same joule, counted less '
                    'formally.'},
          {'type': 'misconception',
           'id': 'think-requirement',
           'anchor': 's-think',
           'targets': 'DIET-07'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'requirement-belongs-to-the-person',
                'text': 'Energy requirement is not a property of food. It is a property of the '
                        'person eating it — set by their size, their age, their growth and how '
                        'much they move.',
                'placement': 'top-level',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'sum-total',
                 'kind': 'worked-example',
                 'demand': 'calculate',
                 'ground': 'inset',
                 'eyebrow': 'Sum 1',
                 'heading': 'Total the day up',
                 'prompt': 'Nothing clever — multiply each portion by how many, then add. Marks '
                           'are lost far more often on arithmetic and on forgetting a portion than '
                           'on method.',
                 'fifa': [{'name': '4 slices toast and butter', 'line': '4 × 780 = 3120 kJ'},
                          {'name': '1 plate of pasta', 'line': '= 2400 kJ'},
                          {'name': '1 banana', 'line': '= 450 kJ'},
                          {'name': '1 chocolate bar', 'line': '= 1050 kJ'},
                          {'name': 'total', 'line': '= 7020 kJ'}]},
                {'id': 'sum-compare',
                 'kind': 'worked-example',
                 'demand': 'calculate',
                 'ground': 'inset',
                 'eyebrow': 'Sum 2',
                 'heading': 'Compare with the requirement',
                 'prompt': 'A shortfall is not automatically a fault in the day — it is a '
                           'statement that stores will be drawn on. Over one day that is normal. '
                           'Over a month it becomes mass loss.',
                 'fifa': [{'name': 'requirement (13-year-old)', 'line': '= 9500 kJ'},
                          {'name': 'intake', 'line': '= 7020 kJ'},
                          {'name': 'shortfall', 'line': '9500 − 7020 = 2480 kJ'}]},
                {'id': 'sum-share',
                 'kind': 'worked-example',
                 'demand': 'calculate',
                 'ground': 'inset',
                 'eyebrow': 'Sum 3',
                 'heading': 'Turn a label into a share',
                 'prompt': 'The same bar is 18% of a 4-year-old’s day and 4% of a rower’s. A '
                           'percentage on a packet is only meaningful once you say whose '
                           'requirement it is a percentage of — which is exactly what packets do '
                           'not say.',
                 'fifa': [{'name': 'bar', 'line': '= 1050 kJ'},
                          {'name': 'requirement', 'line': '= 9500 kJ'},
                          {'name': 'share', 'line': '1050 ÷ 9500 × 100 = 11%'}]},
                {'id': 'think-requirement',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'DIET-07',
                 'statements': [{'quote': 'Everyone needs about 2000 calories a day.',
                                 'body': ['That figure is a labelling convention, not a fact about '
                                          'a person. It exists so packets can print a percentage, '
                                          'and it is the rounded average for an adult woman doing '
                                          'moderate activity. Run the bench above through all five '
                                          'people and the honest range is roughly 6000 to 25 000 '
                                          'kJ a day — more than a fourfold spread, and the top of '
                                          'it is a professional athlete rather than an extreme '
                                          "case. A 4-year-old fed an adult's day would be badly "
                                          "overfed; a rower fed a 4-year-old's day would collapse "
                                          'in a week. When a question gives you a number for a '
                                          'requirement, that number belongs to somebody, and part '
                                          'of the answer is saying who.']},
                                {'quote': 'The energy in food gets used up and disappears.',
                                 'body': ['You met this in Energy stores and it comes back wearing '
                                          "a chef's hat. Nothing about eating destroys energy. The "
                                          'chemical store in your food is transferred: some to '
                                          'movement when you walk, some to the chemical store of '
                                          'new tissue while you grow, and — this is the part '
                                          'people miss — most of it to the thermal store of your '
                                          'surroundings. You are a 70-watt heater. Sit in a small '
                                          'room with the door shut and the temperature rises '
                                          'measurably, and that rise is the energy from your '
                                          'breakfast, still entirely present, just no longer '
                                          'anywhere useful. “Where did the energy go” always has '
                                          'an answer.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'At the bench · feed a person for a day',
                 'heading': 'Pick who you are feeding, then add food',
                 'head_counter': {'format': '{n} portions on the plate',
                                  'format_one': '{n} portion on the plate',
                                  'total': 72,
                                  'start': 0},
                 'group_label': 'Who is eating',
                 'people': [{'id': 'child',
                             'label': '4-year-old',
                             'name': 'A 4-year-old',
                             'lower': 'a 4-year-old',
                             'need': 5800,
                             'why': 'Small body, so little tissue to keep warm and fuel — but '
                                    'growing fast, and a surprising share of the total goes into '
                                    'building new tissue rather than moving about.'},
                            {'id': 'teen',
                             'label': '13-year-old',
                             'name': 'A 13-year-old',
                             'lower': 'a 13-year-old',
                             'need': 9500,
                             'why': 'Almost an adult’s requirement, in a body that is still '
                                    'smaller than one. Adolescent growth is the most '
                                    'energy-expensive period of a human life after infancy.'},
                            {'id': 'adult',
                             'label': 'Office worker',
                             'name': 'An adult with a desk job',
                             'lower': 'an adult with a desk job',
                             'need': 9000,
                             'why': 'Full adult size, no growth to pay for, and very little '
                                    'movement. Roughly three quarters of this goes on simply '
                                    'staying alive and at 37 °C.'},
                            {'id': 'builder',
                             'label': 'Bricklayer',
                             'name': 'An adult doing heavy manual work',
                             'lower': 'an adult doing heavy manual work',
                             'need': 13500,
                             'why': 'The same body as the office worker, doing eight hours of '
                                    'lifting. The difference between these two rows is activity '
                                    'and nothing else.'},
                            {'id': 'rower',
                             'label': 'Olympic rower',
                             'name': 'An Olympic rower in training',
                             'lower': 'an Olympic rower in training',
                             'need': 25000,
                             'why': 'Large muscular body plus six hours of hard training. Athletes '
                                    'at this level struggle to eat enough, which is a problem most '
                                    'people never have.'}],
                 'start_person': 'teen',
                 'need_format': 'Needs {need} kJ / day',
                 'total_format': '{total} kJ of {need} kJ',
                 'balance': {'empty': 'empty plate',
                             'matched': 'balanced for this person',
                             'surplus': '{n} kJ surplus — stored',
                             'short': '{n} kJ short — stores drawn on'},
                 'food_label': 'Tap to add a portion · tap again to remove one',
                 'foods': [{'id': 'toast',
                            'name': 'Toast and butter',
                            'kj': 780,
                            'kj_label': '780 kJ each'},
                           {'id': 'cereal',
                            'name': 'Bowl of cereal with milk',
                            'kj': 1100,
                            'kj_label': '1100 kJ each'},
                           {'id': 'banana', 'name': 'Banana', 'kj': 450, 'kj_label': '450 kJ each'},
                           {'id': 'apple', 'name': 'Apple', 'kj': 320, 'kj_label': '320 kJ each'},
                           {'id': 'sandwich',
                            'name': 'Two chapatis with dal',
                            'kj': 1750,
                            'kj_label': '1750 kJ each'},
                           {'id': 'pasta',
                            'name': 'Plate of pasta and sauce',
                            'kj': 2400,
                            'kj_label': '2400 kJ each'},
                           {'id': 'chicken',
                            'name': 'Plate of jollof rice and chicken',
                            'kj': 2100,
                            'kj_label': '2100 kJ each'},
                           {'id': 'yoghurt',
                            'name': 'Pot of yoghurt',
                            'kj': 520,
                            'kj_label': '520 kJ each'},
                           {'id': 'nuts',
                            'name': 'Handful of nuts',
                            'kj': 1250,
                            'kj_label': '1250 kJ each'},
                           {'id': 'juice',
                            'name': 'Glass of orange juice',
                            'kj': 380,
                            'kj_label': '380 kJ each'},
                           {'id': 'chocolate',
                            'name': 'Chocolate bar',
                            'kj': 1050,
                            'kj_label': '1050 kJ each'},
                           {'id': 'water', 'name': 'Glass of water', 'kj': 0, 'kj_label': '0 kJ'}],
                 'count_format': '×{n}',
                 'max_per_food': 6,
                 'clear_label': 'Empty the day',
                 'portions': {'empty': 'nothing added yet',
                              'some': '{n} portions, {total} kJ',
                              'one': '{n} portion, {total} kJ'},
                 'tolerance': 5,
                 'match': {'eyebrow': 'Within 5% of the target',
                           'head': 'That day matches {person}.',
                           'why': 'Now switch person without changing the food. The same plate is '
                                  'a surplus for one body and a shortfall for another, and nothing '
                                  'about the food has changed — which is the whole idea.'},
                 'id': 'feed-a-day',
                 'kind': 'person-ledger'}],
 'ladder': {'recall': {'title': 'Rung 1 · Do the sum',
                       'q': 'A 13-year-old needing 9500 kJ eats: cereal (1100 kJ), two chapatis '
                            'with dal (1750 kJ), an apple (320 kJ), pasta (2400 kJ) and two '
                            'chocolate bars (1050 kJ each). What is their intake, and how does it '
                            'compare?',
                       'options': ['6620 kJ, which is about 2900 kJ short of the requirement',
                                   '7670 kJ, which is about 1800 kJ more than the requirement',
                                   '7670 kJ, which is about 1800 kJ short of the requirement',
                                   '9500 kJ, which is exactly the same as the requirement'],
                       'answer': 2,
                       'feedback': {0: 'That total counts only one chocolate bar. The day had two.',
                                    1: 'The total is right. But 7670 is less than 9500, so it is a '
                                       'shortfall.',
                                    3: 'Nothing makes the intake match the need. Add up the food '
                                       'to find out.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A chocolate bar holds 1050 kJ. That is 11% of a 13-year-old’s daily '
                           'need of 9500 kJ. A 4-year-old needs about 5800 kJ a day. What share of '
                           'the 4-year-old’s day is one bar?',
                      'options': ['About 18%, because their daily need is much lower',
                                  'About 11%, because the bar holds the same energy for everyone',
                                  'About 6%, because a smaller body takes less energy from the bar',
                                  'You cannot say, because the 4-year-old’s mass is not given'],
                      'answer': 0,
                      'feedback': {1: '11% is the share for a 13-year-old. A 4-year-old needs '
                                      'less, so the share is bigger.',
                                   2: 'The bar holds the same energy, whoever eats it. The need is '
                                      'what differs.',
                                   3: 'You do not need the mass. Divide 1050 by 5800 and multiply '
                                      'by 100.'}},
            'explain': {'title': 'Rung 3 · Explain the pair',
                        'q': 'The office worker and the bricklayer in the bench above are the same '
                             'age and size, but their requirements differ by 4500 kJ a day. '
                             'Explain where that difference goes, and why the 4-year-old needs '
                             'less than either despite growing fastest.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The bricklayer needs more because…',
                        'success': ['Attributes the 4500 kJ difference to activity — muscles '
                                    'contracting for hours require energy transfer.',
                                    'Says the two bodies are otherwise identical, so activity is '
                                    'the only variable.',
                                    'Explains the 4-year-old’s lower total by their much smaller '
                                    'body: less tissue to keep warm and to maintain.',
                                    'Notes that growth does claim a share of a child’s '
                                    'requirement, and that it is still smaller in total than an '
                                    'adult’s maintenance.',
                                    'Avoids saying anyone ‘uses up’ energy — uses transferred, or '
                                    'stored, instead.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A school wants one standard lunch, the same portion for every pupil '
                             'aged 11 to 16. Using what you now know about requirements, say what '
                             'is wrong with the plan, what you would do instead, and one thing you '
                             'would need to find out first.',
                        'field_label': 'Your answer',
                        'placeholder': 'One portion cannot work because…',
                        'success': ['Says requirements vary substantially across this age range, '
                                    'so one portion cannot match all of them.',
                                    'Names at least two things the requirement depends on — age, '
                                    'size, sex, growth, activity.',
                                    'Proposes something workable: variable portions, second '
                                    'helpings, or a base meal plus add-ons.',
                                    'Names a real thing to find out — the age spread, activity '
                                    'levels, or how much pupils actually eat rather than are '
                                    'served.']}},
 'key_note': "Energy in food is measured in kilojoules. A person's daily requirement depends on "
             'their age, size, sex, rate of growth and level of activity, so there is no single '
             'correct figure. Take in more than you transfer and the surplus is stored; take in '
             'less and stores are broken down.',
 'stretch': [{'type': 'explainer',
              'id': 'the-bomb-calorimeter',
              'text': 'The numbers on a food packet were originally obtained by burning the food. '
                      'A weighed sample goes into a sealed steel vessel packed with oxygen, the '
                      'vessel sits in a known mass of water, and the sample is ignited '
                      'electrically; the rise in water temperature gives the energy released. The '
                      'device is called a bomb calorimeter, and the name is literal enough that '
                      'early ones occasionally lived up to it. It measures the total chemical '
                      'energy in the sample, which is why the figure for dietary fibre had to be '
                      'corrected downwards later — a calorimeter happily burns cellulose, and your '
                      'gut cannot digest a gram of it. The instrument was answering a chemistry '
                      'question when what was wanted was a biology one.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to check a requirement calculation of your own?',
           'cta': 'Ask about this lesson',
           'anchor': 's-maths'},
 'convention_note': 'Requirement figures are rounded typical values used to teach the principle. '
                    "They are not a guide for anyone's own eating, and this lesson does not set "
                    'targets for any individual. Questions about your own diet belong with a '
                    'doctor or a registered dietitian.',
 'ws': ['measurement', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
