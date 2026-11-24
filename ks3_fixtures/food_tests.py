# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `food-tests` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'food-tests'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'food-tests',
 'title': 'Food tests',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'INVESTIGATION',
 'covers': ['KS3.WS.ANA.03'],
 'touches': ['KS3.B.NUT.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 1},
             {'id': 'cells-and-systems', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 55,
 'requires': ['a-balanced-diet'],
 'assumes': [],
 'references': ['enzymes-in-digestion',
                {'unit': 'C1',
                 'lesson': 'testing-the-model',
                 'label': 'Testing the model',
                 'why': 'Where the same question — what a result actually licenses you to claim — '
                        'is asked of a model rather than of a tube.'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Required practical: qualitative food tests, plus quantitative comparison against '
                'known standards.',
 'big_question': 'Four tests, four colour changes. Each one answers exactly one question — and '
                 'three questions you will want to ask, none of them can answer.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Two tubes', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Run the tests',
           'done_when': 'four_combinations_run'},
          {'anchor': 's-limits',
           'short': 'LIMITS',
           'label': 'What it is worth',
           'mirrors': 's-bench',
           'done_when': 'four_combinations_run'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two tubes of milk. One goes brick red, one stays blue.',
                'prompt': "Same bottle of milk, same Benedict's solution, same water bath. Tube 1 "
                          'was heated for five minutes and comes out brick red. Tube 2 was heated '
                          'for thirty seconds and comes out blue.',
                'commit': 'If you had to guess, what does tube 2 on its own tell you about the '
                          'milk?',
                'options': ['It has no sugar in it', 'Nothing either way'],
                'reveal': 'Next: run four tests on five foods, say what you expect each time, and '
                          'see what you may write down.',
                'guess': True,
                'replies': ['Blue does look like a clear no. But the same milk goes brick red in '
                            'tube 1, after a longer heat. A blue tube only says the test did not '
                            'find sugar this time.',
                            'On its own, a blue tube only says the test did not find sugar this '
                            'time. That is a fact about the test, not about the milk.'],
                'answer': 1},
 'misconceptions': [{'id': 'DIET-04',
                     'statement': 'The deeper the colour, the more of the nutrient there was.',
                     'elicited_by': 'twenty-combinations',
                     'confronted_by': 'think-colour'},
                    {'id': 'DIET-05',
                     'statement': 'A negative result proves the nutrient is not there.',
                     'elicited_by': 'twenty-combinations',
                     'confronted_by': 'think-colour'}],
 'vocabulary': [{'term': 'food test',
                 'definition': 'A reagent that changes colour when one particular nutrient is '
                               'present.',
                 'note': 'One test answers one question and no others.'},
                {'term': 'qualitative',
                 'definition': 'Answering ‘present or not detected’, and never ‘how much’.',
                 'note': None},
                {'term': 'reducing sugar',
                 'definition': 'A sugar that can give an electron to copper, which is what '
                               'Benedict’s solution detects.',
                 'note': 'Glucose and fructose can; ordinary table sugar cannot.'},
                {'term': 'emulsion',
                 'definition': 'A cloudy mixture of tiny droplets of one liquid suspended in '
                               'another.',
                 'note': None},
                {'term': 'false negative',
                 'definition': 'A test that shows nothing even though the substance is really '
                               'there, usually because there is too little of it to detect.',
                 'note': None}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'twenty-combinations', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-limits',
           'eyebrow': 'What a colour change is worth',
           'statement': 'Three questions these tests cannot answer.',
           'cards': [{'term': 'How much is there?',
                      'gloss': 'The test is qualitative. Colour intensity also changes with '
                               'heating time, volume and concentration, none of which you '
                               'controlled — so a deeper colour is not evidence of more nutrient.'},
                     {'term': 'Is there really none?',
                      'gloss': 'A negative means below what this test can detect, with this '
                               'sample, prepared this way. Potato does contain protein; Biuret '
                               'cannot see it at 2%.'},
                     {'term': 'Is this food healthy?',
                      'gloss': 'Nothing in a colour change is about health. Olive oil is one '
                               'positive out of four and is a required nutrient; a glucose '
                               'solution is one positive and is nothing but fuel.'}]},
          {'type': 'key-fact', 'ref': 'qualitative-never-quantity'},
          {'type': 'misconception',
           'id': 'think-colour',
           'anchor': 's-think',
           'targets': 'DIET-04'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'qualitative-never-quantity',
                'text': 'A food test is qualitative: it says present or not detected. It never '
                        'says how much, and “not detected” is a fact about your test, not about '
                        'the food.',
                'placement': 'top-level',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-colour',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'DIET-04',
                 'statements': [{'quote': "The redder the Benedict's went, the more sugar there "
                                          'was.',
                                 'body': ['Tempting, and almost useful, but not something you may '
                                          'claim from a school test. The colour does move through '
                                          'green, yellow and orange to brick red as more sugar is '
                                          'present — but it also moves that way if you heat it for '
                                          "longer, use more Benedict's, or start with a warmer "
                                          'bath. In your experiment those things were not '
                                          'controlled, so a redder tube is not evidence of more '
                                          'sugar; it is evidence that something was different, and '
                                          'you cannot say what. To make the colour mean an amount '
                                          'you would have to fix the volume, the concentration of '
                                          "Benedict's, the temperature and the time, and compare "
                                          'against tubes of known sugar concentration. That is a '
                                          'different experiment, and it is the one a laboratory '
                                          'actually runs.']},
                                {'quote': 'The iodine stayed orange, so there is no starch in it.',
                                 'body': ['Write the two sentences next to each other and the gap '
                                          'is obvious. <em>The test did not detect starch</em> is '
                                          'what you observed. <em>There is no starch</em> is a '
                                          'claim about the food. Between them sit at least four '
                                          'ways the first can be true while the second is false: '
                                          'too little starch to see, iodine too dilute, the sample '
                                          'not crushed so the iodine never reached the inside, or '
                                          'the starch already broken down to sugar — which is '
                                          'exactly what happens if you chew bread for two minutes '
                                          'before testing it. Negative results are the ones that '
                                          'need the most care, because a negative feels like '
                                          'nothing happened, and nothing happening is very easy to '
                                          'achieve by accident.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'At the bench · five foods, four tests',
                 'heading': 'Predict, then run it',
                 'head_counter': {'format': '{n} of 20 combinations run', 'total': 20, 'start': 0},
                 'prompt': 'Pick a food, pick a test, say what you expect, then run it. The tube '
                           'shows what you would actually see.',
                 'groups': {'food': 'Food', 'test': 'Test'},
                 'tests': [{'id': 'iodine',
                            'label': 'Iodine',
                            'detects': 'starch',
                            'detects_full': 'starch',
                            'method': 'A few drops of iodine solution straight onto the food. No '
                                      'heating.',
                            'neg': {'colour': '#B4762A',
                                    'name': 'orange-brown — unchanged',
                                    'headline': 'Orange-brown — unchanged — not detected.'},
                            'pos': {'colour': '#1B1B3A',
                                    'name': 'blue-black',
                                    'headline': 'Blue-black — starch detected.'}},
                           {'id': 'benedict',
                            'label': "Benedict's",
                            'detects': 'reducing sugar',
                            'detects_full': 'reducing sugar (glucose, fructose)',
                            'method': 'Equal volumes of food solution and Benedict’s, then five '
                                      'minutes in a water bath at 80 °C.',
                            'neg': {'colour': '#2E63B8',
                                    'name': 'blue — unchanged',
                                    'headline': 'Blue — unchanged — not detected.'},
                            'pos': {'colour': '#B03A16',
                                    'name': 'brick red',
                                    'headline': 'Brick red — reducing sugar detected.'}},
                           {'id': 'emulsion',
                            'label': 'Ethanol emulsion',
                            'detects': 'lipid',
                            'detects_full': 'lipid (fat and oil)',
                            'method': 'Shake the food with ethanol, let it settle, then pour the '
                                      'ethanol into water.',
                            'neg': {'colour': '#E8E2D2',
                                    'name': 'clear — unchanged',
                                    'headline': 'Clear — unchanged — not detected.'},
                            'pos': {'colour': '#FBFBF6',
                                    'name': 'cloudy white',
                                    'headline': 'Cloudy white — lipid detected.'}},
                           {'id': 'biuret',
                            'label': 'Biuret',
                            'detects': 'protein',
                            'detects_full': 'protein',
                            'method': 'Equal volumes of food solution and Biuret solution, shaken. '
                                      'No heating.',
                            'neg': {'colour': '#3E7ACB',
                                    'name': 'blue — unchanged',
                                    'headline': 'Blue — unchanged — not detected.'},
                            'pos': {'colour': '#7B4CA8',
                                    'name': 'lilac purple',
                                    'headline': 'Lilac purple — protein detected.'}}],
                 'foods': [{'id': 'potato',
                            'label': 'Potato',
                            'lower': 'potato',
                            'has': {'iodine': True,
                                    'benedict': False,
                                    'emulsion': False,
                                    'biuret': False},
                            'notes': {'iodine': 'Potato is mostly starch, and starch is what '
                                                'iodine is for. A strong blue-black comes up '
                                                'within seconds.',
                                      'benedict': 'Raw potato stores its carbohydrate as starch, '
                                                  'not as free glucose, so there is very little '
                                                  'reducing sugar to find. Leave a potato in a '
                                                  'warm cupboard for a fortnight and this test '
                                                  'starts to go positive — the starch is being '
                                                  'broken down.',
                                      'emulsion': 'Potato has almost no lipid. Under a hundredth '
                                                  'of its mass.',
                                      'biuret': 'A potato is about 2% protein — present, but too '
                                                'dilute for the school test to show. This is a '
                                                'false negative, and it is the most common one in '
                                                'the lesson.'}},
                           {'id': 'milk',
                            'label': 'Milk',
                            'lower': 'milk',
                            'has': {'iodine': False,
                                    'benedict': True,
                                    'emulsion': True,
                                    'biuret': True},
                            'notes': {'iodine': 'No starch in milk. This is a true negative — '
                                                'there really is none.',
                                      'benedict': 'Lactose, the sugar in milk, is a reducing '
                                                  'sugar. Brick red if you heat it long enough; '
                                                  'green or orange if you rush it.',
                                      'emulsion': 'Whole milk is a suspension of fat droplets in '
                                                  'water. Strong cloudiness.',
                                      'biuret': 'Milk is rich in casein and whey proteins. Clear '
                                                'lilac.'}},
                           {'id': 'eggwhite',
                            'label': 'Egg white',
                            'lower': 'egg white',
                            'has': {'iodine': False,
                                    'benedict': False,
                                    'emulsion': False,
                                    'biuret': True},
                            'notes': {'iodine': 'None. Egg white has essentially no carbohydrate.',
                                      'benedict': 'Negative, and truly so — egg white is about 90% '
                                                  'water and 10% protein, with no sugar to speak '
                                                  'of.',
                                      'emulsion': 'The lipid in an egg is all in the yolk. '
                                                  'Separate them and the white gives a clean '
                                                  'negative.',
                                      'biuret': 'The clearest positive in the lesson. Egg white is '
                                                'almost pure protein in water.'}},
                           {'id': 'applejuice',
                            'label': 'Apple juice',
                            'lower': 'apple juice',
                            'has': {'iodine': False,
                                    'benedict': True,
                                    'emulsion': False,
                                    'biuret': False},
                            'notes': {'iodine': 'No starch — in a ripe apple it has all been '
                                                'converted to sugar. An unripe apple would test '
                                                'positive, which is a nice reminder that a food is '
                                                'not a fixed thing.',
                                      'benedict': 'Fructose and glucose, both reducing sugars. '
                                                  'Rapid brick red.',
                                      'emulsion': 'Nothing. Fruit juice is sugar and water.',
                                      'biuret': 'Under 0.3% protein. Negative on the school test, '
                                                'and not quite zero in the fruit.'}},
                           {'id': 'oliveoil',
                            'label': 'Olive oil',
                            'lower': 'olive oil',
                            'has': {'iodine': False,
                                    'benedict': False,
                                    'emulsion': True,
                                    'biuret': False},
                            'notes': {'iodine': 'No starch.',
                                      'benedict': 'No sugar. Note that a negative here tells you '
                                                  'nothing about the energy in the tube — olive '
                                                  'oil carries more energy per gram than anything '
                                                  'else on the bench.',
                                      'emulsion': 'Textbook positive: a dense white cloud the '
                                                  'moment the ethanol hits the water.',
                                      'biuret': 'No protein.'}}],
                 'tube': {'caption': 'In the tube', 'label_join': ' + ', 'not_run': 'not run yet'},
                 'method_label': 'Method',
                 'detects_label': 'Detects: {detects}',
                 'predict': {'prompt': 'Before you run it — will {test} detect {detects} in '
                                       '{food_lower}?',
                             'options': ['Yes — it will change colour',
                                         'No — it will stay as it started']},
                 'verdicts': {'hit': 'You predicted this', 'miss': 'Not what you predicted'},
                 'claim_label': 'What you may write down:',
                 'claims': {'positive': '“{food} contains {detects}.” Nothing about how much.',
                            'negative': '“No {detects} was detected in {food_lower} under these '
                                        'conditions.” Not “there is none”.'},
                 'rail_after': 4,
                 'id': 'twenty-combinations',
                 'kind': 'test-bench'}],
 'ladder': {'recall': {'title': 'Rung 1 · Read the result',
                       'q': 'A student shakes a food sample with ethanol, then pours the ethanol '
                            'into water. A cloudy white layer forms. What may they write down?',
                       'options': ['The food is high in fat, as the white layer is thick',
                                   'The food contains lipid and no protein, as the layer is white',
                                   'The food contains lipid, as a cloudy white layer formed',
                                   'The food is unhealthy, as it contains a lot of fat'],
                       'answer': 2,
                       'feedback': {0: 'The test shows fat is there. It does not measure how much.',
                                    1: 'This test says nothing about protein. That needs the '
                                       'Biuret test.',
                                    3: 'A food test shows a nutrient is there. It says nothing '
                                       'about health.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Bread turns iodine blue-black and leaves Benedict’s blue. A student '
                           'chews some for a few minutes. Now iodine gives a weaker colour, and '
                           'Benedict’s turns orange. What happened?',
                      'options': ['The iodine was too dilute the second time',
                                  'Chewing crushed the starch into pieces too small for iodine to '
                                  'detect',
                                  'Saliva broke the starch down into sugar',
                                  'The starch dissolved in the saliva'],
                      'answer': 2,
                      'feedback': {0: 'The same iodine was used both times. The bread changed, not '
                                      'the reagent.',
                                   1: 'Crushing food helps a test work. It cannot make sugar '
                                      'appear.',
                                   3: 'Iodine still detects starch in solution. Some starch has '
                                      'been turned into sugar.'}},
            'explain': {'title': 'Rung 3 · Write the honest conclusion',
                        'q': 'A group tests potato with Biuret and gets no colour change. They '
                             'conclude “potato contains no protein”. Potato is in fact about 2% '
                             'protein. Explain what is wrong with their conclusion, write a '
                             'version you could defend, and say what you would change to detect '
                             'the protein.',
                        'field_label': 'Your answer',
                        'placeholder': 'Their conclusion goes further than the evidence because…',
                        'success': ['Says the observation only supports ‘protein not detected’, '
                                    'not ‘no protein present’.',
                                    'Gives the reason: the concentration is below what the test '
                                    'can detect.',
                                    'Writes a defensible conclusion using wording such as ‘no '
                                    'protein was detected under these conditions’.',
                                    'Suggests a workable change — more concentrated sample, larger '
                                    'mass of potato in less water, or a more sensitive method.',
                                    'Does not claim the test was done wrongly; the method was '
                                    'followed correctly and still gave a false negative.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A company claims its cereal bar is “protein-packed and sugar-free”. '
                             'You have iodine, Benedict’s, ethanol and Biuret. Say which tests you '
                             'would run, what result would support each claim, and which of the '
                             'two claims you could never fully check with this equipment.',
                        'field_label': 'Your answer',
                        'placeholder': 'I would run… because…',
                        'success': ['Picks Biuret for the protein claim and Benedict’s for the '
                                    'sugar claim.',
                                    'States that a lilac Biuret result supports protein being '
                                    'present but not ‘packed’, because the test gives no amount.',
                                    'Identifies ‘protein-packed’ as the claim that cannot be '
                                    'checked, since it is a quantity claim and these tests are '
                                    'qualitative.',
                                    'Notes that a blue Benedict’s does not prove sugar-free either '
                                    '— sucrose is not a reducing sugar and would not show up.']}},
 'key_note': "Iodine turns blue-black with starch. Benedict's solution turns from blue to brick "
             'red with reducing sugar, on heating. Ethanol then water turns cloudy white with '
             'lipid. Biuret solution turns from blue to lilac with protein. Each result is '
             'positive or not detected — never an amount.',
 'stretch': [{'type': 'explainer',
              'id': 'sugar-that-is-not-a-reducing-sugar',
              'text': "Benedict's test does not detect all sugars. It needs a sugar that can hand "
                      'an electron to copper — a reducing sugar — which glucose and fructose can '
                      'do and sucrose, ordinary table sugar, cannot. So a spoonful of caster sugar '
                      'in water gives a blue tube and a perfectly negative result, and a student '
                      'who concludes there is no sugar in sugar has followed the method correctly '
                      'and reasoned wrongly. Boil the same solution with a little acid first, '
                      'splitting the sucrose into glucose and fructose, and it goes brick red. The '
                      'test was never asking “is there sugar here” — it was asking a narrower '
                      'question that happens to be easy to confuse with that one.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Unsure what a negative result lets you write down?',
           'cta': 'Ask about this lesson',
           'anchor': 's-limits'},
 'safety_note': "Benedict's and Biuret solutions are irritants and Biuret contains sodium "
                'hydroxide — wear eye protection, use a water bath rather than a naked flame, and '
                'never taste anything on the bench. Ethanol is highly flammable: no Bunsen alight '
                'while it is open.',
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
