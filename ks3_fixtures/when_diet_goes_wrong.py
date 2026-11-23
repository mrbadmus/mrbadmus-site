# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `when-diet-goes-wrong` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'when-diet-goes-wrong'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'when-diet-goes-wrong',
 'title': 'When diet goes wrong',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'CONTRAST',
 'covers': ['KS3.B.NUT.03'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 2}, {'id': 'energy', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': ['energy-in-food-and-what-you-need'],
 'assumes': [],
 'references': ['a-balanced-diet', 'bacteria-in-the-gut'],
 'ks4_links': [],
 'ks4_becomes': 'Risk factors for non-communicable disease, and the evidence linking diet to '
                'cardiovascular disease and type 2 diabetes.',
 'big_question': 'What can go wrong with a diet, and what does each problem do to the body?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Full plate', 'done_when': 'committed'},
          {'anchor': 's-three',
           'short': 'THREE',
           'label': 'Three failures',
           'mirrors': 's-hook',
           'done_when': 'committed'},
          {'anchor': 's-cases',
           'short': 'CLINIC',
           'label': 'Five clinics',
           'done_when': 'all_five_diagnosed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A patient on 13 000 kJ a day.',
                'prompt': 'Not going short of food. Not skipping meals. Taking in more energy than '
                          'an adult needs, every day.',
                'commit': 'If you had to guess, could this patient be malnourished?',
                'options': ['Yes, they could be', 'No, not on that much'],
                'reveal': 'Malnutrition is not one problem but three separate ones. Next: the '
                          'three side by side, then five clinics to diagnose.',
                'guess': True,
                'replies': ['Malnourished means badly nourished, not underfed. A big diet can '
                            'still be missing something the body needs, such as iron or a vitamin.',
                            'Most people think malnourished means underfed. But it means badly '
                            'nourished, and a diet can be huge in energy and still be missing iron '
                            'or a vitamin.'],
                'answer': 0},
 'misconceptions': [{'id': 'DIET-08',
                     'statement': 'Malnourished means not having enough to eat.',
                     'elicited_by': 'three-wrong-ideas',
                     'confronted_by': 'three-wrong-ideas'},
                    {'id': 'DIET-09',
                     'statement': 'Deficiency diseases are all in the past.',
                     'elicited_by': 'three-wrong-ideas',
                     'confronted_by': 'three-wrong-ideas'},
                    {'id': 'DIET-10',
                     'statement': 'You can tell what someone eats by looking at them.',
                     'elicited_by': 'three-wrong-ideas',
                     'confronted_by': 'three-wrong-ideas'}],
 'vocabulary': [{'term': 'malnutrition',
                 'definition': 'A diet whose balance is wrong — too much energy, too little '
                               'energy, or a nutrient missing.',
                 'note': 'It does not mean going short of food. That is one of the three things it '
                         'can mean.'},
                {'term': 'obesity',
                 'definition': 'A long-term energy surplus stored as so much lipid that health '
                               'risks rise.',
                 'note': None},
                {'term': 'deficiency disease',
                 'definition': 'An illness caused by one nutrient being absent or too low in the '
                               'diet.',
                 'note': 'Scurvy, rickets and anaemia are three. Each has one missing nutrient '
                         'behind it.'},
                {'term': 'adipose tissue',
                 'definition': 'The body tissue that stores lipid.',
                 'note': None}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'rule',
           'anchor': 's-three',
           'eyebrow': 'Three separate failures',
           'statement': 'Not one problem with a dial on it.',
           'cards': [{'term': 'Imbalance 1 · Long-term energy surplus',
                      'gloss': '<strong>What is wrong</strong> Energy taken in is greater than '
                               'energy transferred, day after day, for months or years. '
                               '<strong>What the body does</strong> The surplus is stored as lipid '
                               'in adipose tissue. Storage is a normal, healthy mechanism; the '
                               'problem is only the size of the store when it keeps growing. '
                               '<strong>What follows</strong> Obesity raises the risk of type 2 '
                               'diabetes, high blood pressure, heart disease and joint damage. '
                               'Risk raised, not certainty — these are probabilities, not '
                               'verdicts. <strong>What changes it</strong> Any lasting change to '
                               'the balance between intake and activity. Slow, because the store '
                               'took a long time to build.'},
                     {'term': 'Imbalance 2 · Long-term energy shortfall',
                      'gloss': '<strong>What is wrong</strong> Energy taken in is less than energy '
                               'transferred, for weeks or months. Causes range from food being '
                               'unavailable to illness that prevents eating or absorbing. '
                               '<strong>What the body does</strong> Lipid stores are broken down '
                               'first. When those are gone it breaks down its own protein — '
                               'muscle, including heart muscle. <strong>What follows</strong> '
                               'Growth stops, the immune system weakens, and body temperature is '
                               'hard to maintain. In children the effect on growth may not be '
                               'recoverable. <strong>What changes it</strong> Refeeding, done '
                               'carefully and medically — restarting food too fast after prolonged '
                               'starvation is itself dangerous.'},
                     {'term': 'Imbalance 3 · A specific nutrient missing',
                      'gloss': '<strong>What is wrong</strong> One nutrient is absent or too low. '
                               'Energy intake can be high, normal or low — it is a separate '
                               'question. <strong>What the body does</strong> Whatever that '
                               'nutrient was needed for stops working properly. Nothing else can '
                               'substitute: no amount of carbohydrate replaces 14 mg of iron. '
                               '<strong>What follows</strong> A named deficiency disease. No '
                               'vitamin C, scurvy. No vitamin D, rickets. No iron, anaemia. Each '
                               'has its own signs. <strong>What changes it</strong> Supplying that '
                               'one nutrient. Often a fast and complete recovery, which is what '
                               'makes deficiency diseases so striking to treat.'}],
           'close': 'Each of the three has a different cause, a different mechanism inside the '
                    'body, and a different remedy. Compare them line by line.'},
          {'type': 'key-fact', 'ref': 'three-imbalances'},
          {'type': 'practical', 'id': 'five-clinics', 'anchor': 's-cases'},
          {'type': 'misconception',
           'id': 'three-wrong-ideas',
           'anchor': 's-think',
           'targets': 'DIET-08'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'three-imbalances',
                'text': 'Too much energy, too little energy and a missing nutrient are three '
                        'different imbalances. A deficiency can occur at any level of energy '
                        'intake, because a specific nutrient cannot be substituted by more of the '
                        'others.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'three-wrong-ideas',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'DIET-08',
                 'statements': [{'quote': 'Malnourished means not having enough to eat.',
                                 'body': ['The word means badly nourished, not under-nourished, '
                                          'and the difference is not nit-picking — it changes what '
                                          'you look for and what you do. Rickets was widespread in '
                                          'industrial British cities among children who were fed '
                                          'enough, because vitamin D needs either oily fish or '
                                          'sunlight and a smoke-filled street supplies neither. '
                                          'Iron deficiency is the most common nutritional disorder '
                                          'in the world and it is not concentrated in places where '
                                          'food is scarce. If you diagnose every dietary problem '
                                          'as a shortage of food, you will treat these by handing '
                                          'over more of the same food, and nothing will improve, '
                                          'because the missing nutrient is still missing.']},
                                {'quote': 'Deficiency diseases are all in the past.',
                                 'body': ['Scurvy still appears in hospitals. So does rickets, so '
                                          'does severe iron deficiency, and vitamin B12 deficiency '
                                          'is common enough that it is a routine blood test. The '
                                          'reason is not that food is unavailable; it is that a '
                                          'nutrient needed in milligrams can be absent from a diet '
                                          'that looks entirely ordinary, and the early signs — '
                                          'tiredness, aching, slow healing, low mood — are the '
                                          'least specific symptoms in medicine. A deficiency is '
                                          'easy to miss precisely because it does not announce '
                                          'itself as a food problem.']},
                                {'quote': 'You can tell what someone eats by looking at them.',
                                 'body': ['You cannot, and this is the most important sentence in '
                                          'the lesson. Body mass is affected by genetics, by '
                                          'illness, by medication, by how much someone can move, '
                                          'by sleep, by stress and by whether they can afford or '
                                          'reach particular foods — as well as by what they eat. '
                                          'Two people on the same diet can differ a lot, which is '
                                          'exactly what the hook in the energy lesson showed. The '
                                          'three imbalances in this lesson are described by '
                                          'measurements and by clinical signs, not by appearance, '
                                          'and a biologist reasons from the measurements.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'Your turn · five clinics',
                 'heading': 'Which imbalance is this?',
                 'head_counter': {'format': '{n} of 5 diagnosed', 'total': 5, 'start': 0},
                 'prompt': 'Each description gives you a diet and a set of signs. Say which of the '
                           'three imbalances fits. Two of the five have more than one answer, and '
                           'being unwilling to pick two is itself a mistake.',
                 'kinds': [{'id': 'surplus', 'label': 'Energy surplus'},
                           {'id': 'shortfall', 'label': 'Energy shortfall'},
                           {'id': 'missing', 'label': 'A nutrient missing'}],
                 'pick_label': 'Tick every imbalance that applies',
                 'reveal_label': 'Show the diagnosis',
                 'count_labels': {'none': 'nothing ticked yet',
                                  'some': '{n} ticked',
                                  'done': 'Diagnosed'},
                 'cases': [{'id': 'k1',
                            'label': 'Clinic 1',
                            'tab_label': 'Clinic 1',
                            'description': 'An adult reports tiredness, breathlessness on stairs '
                                           'and pale skin. Blood tests show low haemoglobin. Their '
                                           'diet is bread, pasta, cheese and fruit, with no meat, '
                                           'fish or leafy vegetables. They are not losing mass.',
                            'intake': 'Intake about 10 000 kJ / day — close to requirement',
                            'kinds': ['missing'],
                            'verdict_label': 'One imbalance applies here',
                            'answer': 'Iron-deficiency anaemia. A nutrient missing, and nothing '
                                      'else.',
                            'why': 'Energy intake is fine, mass is stable, and the signs all point '
                                   'at haemoglobin. Iron is needed in milligrams and this diet '
                                   'supplies almost none. Adding more of the same food would '
                                   'change nothing.'},
                           {'id': 'k2',
                            'label': 'Clinic 2',
                            'tab_label': 'Clinic 2',
                            'description': 'A 14-year-old has stopped growing in height over '
                                           'eighteen months, feels cold constantly, and bruises '
                                           'easily. Their family has been unable to afford regular '
                                           'meals.',
                            'intake': 'Intake about 4500 kJ / day — far below requirement',
                            'kinds': ['shortfall', 'missing'],
                            'verdict_label': 'Two imbalances apply here',
                            'answer': 'Energy shortfall, and almost certainly deficiencies '
                                      'alongside it.',
                            'why': 'Both apply, and this is the pair most students refuse to tick '
                                   'together. Too little food means too little of everything in it '
                                   '— so a prolonged shortfall drags specific deficiencies along '
                                   'behind it. The growth arrest is the shortfall; the bruising '
                                   'suggests vitamin C or K as well.'},
                           {'id': 'k3',
                            'label': 'Clinic 3',
                            'tab_label': 'Clinic 3',
                            'description': 'An adult has gained mass steadily over ten years. '
                                           'Blood glucose is raised and a doctor has diagnosed '
                                           'type 2 diabetes. They eat large portions, mostly '
                                           'processed food, and have a desk job and a car commute.',
                            'intake': 'Intake about 14 000 kJ / day — well above requirement',
                            'kinds': ['surplus'],
                            'verdict_label': 'One imbalance applies here',
                            'answer': 'Long-term energy surplus.',
                            'why': 'Ten years of intake above requirement, stored as lipid, and '
                                   'one of the risks that follow has now appeared. Note what this '
                                   'case is not: it is not a moral failure, and the fix is a '
                                   'change in the long-term balance, not a punishment.'},
                           {'id': 'k4',
                            'label': 'Clinic 4',
                            'tab_label': 'Clinic 4',
                            'description': 'A toddler in a smoky northern city in 1900 has soft, '
                                           'bowed leg bones and a delayed walk. They are fed '
                                           'bread, potatoes, tea and a little meat. They are not '
                                           'thin.',
                            'intake': 'Intake roughly at requirement',
                            'kinds': ['missing'],
                            'verdict_label': 'One imbalance applies here',
                            'answer': 'Rickets — vitamin D missing.',
                            'why': 'Enough food, enough energy, no vitamin D. It comes from oily '
                                   'fish or from sunlight on skin, and a smoke-darkened street '
                                   'supplies neither. Calcium cannot be absorbed properly without '
                                   'it, so the bones stay soft. This is the classic case of a '
                                   'deficiency in a fed child.'},
                           {'id': 'k5',
                            'label': 'Clinic 5',
                            'tab_label': 'Clinic 5',
                            'description': 'An adult recovering from major surgery cannot absorb '
                                           'nutrients properly from their shortened intestine. '
                                           'They eat willingly and in normal quantities but are '
                                           'losing mass and have low levels of several vitamins.',
                            'intake': 'Intake about 9500 kJ / day — at requirement',
                            'kinds': ['shortfall', 'missing'],
                            'verdict_label': 'Two imbalances apply here',
                            'answer': 'Both — and the cause is not the diet at all.',
                            'why': 'The plate is fine. What has failed is absorption, so what '
                                   'reaches the blood is a shortfall even though what reaches the '
                                   'mouth is not. This is the case that shows why ‘diet’ and '
                                   '‘nutrition’ are not the same word: the next three lessons are '
                                   'about the part of the system that has broken here.'}],
                 'self_check': {'question': 'Now every diagnosis is showing — how many of your '
                                            'five did you have?',
                                'options': ['All five', 'Three or four', 'Two or fewer'],
                                'note': 'Nobody marks this but you. Clinics 2 and 5 each have two '
                                        'answers, and those are the two worth reading again.'},
                 'id': 'five-clinics',
                 'kind': 'clinic-cases'}],
 'ladder': {'recall': {'title': 'Rung 1 · Name the imbalance',
                       'q': 'A patient eats 12 000 kJ a day, and their mass is not changing. They '
                            'have been diagnosed with scurvy. Which imbalance or imbalances apply?',
                       'options': ['A missing nutrient only',
                                   'An energy shortfall only',
                                   'A missing nutrient and an energy shortfall',
                                   'No imbalance at all on that much food'],
                       'answer': 0,
                       'feedback': {1: 'Their mass is steady on 12 000 kJ, so energy is not short.',
                                    2: 'The missing nutrient is right. Steady mass shows there is '
                                       'no energy shortfall.',
                                    3: 'Scurvy happens at any energy intake. It needs only a lack '
                                       'of vitamin C.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Two children are the same age and height. Child A eats 6000 kJ a day; '
                           'child B eats 11 000 kJ. Both have been diagnosed with iron-deficiency '
                           'anaemia. What does this tell you?',
                      'options': ['Energy intake does not decide iron intake, as iron is a '
                                  'separate nutrient',
                                  'Child B must have been misdiagnosed, as 11 000 kJ always holds '
                                  'enough iron',
                                  'Child A’s anaemia must be worse, as they eat less food each day',
                                  'Both children need more food, as anaemia comes from too little '
                                  'energy'],
                      'answer': 0,
                      'feedback': {1: "No amount of food guarantees iron. Child B's diet can still "
                                      'lack it.',
                                   2: "The energy figures say nothing about how low each child's "
                                      'iron is.',
                                   3: 'Anaemia here is caused by too little iron, not too little '
                                      'energy.'}},
            'explain': {'title': 'Rung 3 · Explain why more food does not fix it',
                        'q': 'A charity responds to a region with widespread anaemia by shipping '
                             'large quantities of white rice. Explain why this will reduce hunger '
                             'but not reduce the anaemia, and what would need to be added.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Rice will help with… but not with…',
                        'success': ['Says rice supplies carbohydrate and so addresses an energy '
                                    'shortfall.',
                                    'Says rice supplies very little iron, so the specific '
                                    'deficiency is untouched.',
                                    'States the general principle: a missing nutrient cannot be '
                                    'substituted by more of the others.',
                                    'Names something that would supply iron — pulses, leafy '
                                    'greens, meat, or fortified flour.',
                                    'Recognises that both problems can be present at once and both '
                                    'need addressing.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'The UK adds calcium, iron and B vitamins to white flour by law. '
                             'Using the three imbalances, explain what problem this policy '
                             'targets, why it works at the flour rather than at the person, and '
                             'one limitation you would expect it to have.',
                        'field_label': 'Your answer',
                        'placeholder': 'Fortification targets…',
                        'success': ['Identifies the target as specific nutrient deficiencies, not '
                                    'energy imbalance.',
                                    'Explains that flour is eaten by almost everyone, so '
                                    'fortifying it reaches people who would never seek treatment.',
                                    'Notes that it requires no change in behaviour, which is why '
                                    'it works where advice does not.',
                                    'Gives a real limitation — it misses people who avoid wheat, '
                                    'cannot be targeted to those who need it, and the dose cannot '
                                    'be adjusted per person.']}},
 'key_note': 'An imbalanced diet can mean a long-term energy surplus, a long-term energy '
             'shortfall, or a specific nutrient missing. Obesity raises the risk of type 2 '
             'diabetes, heart disease and joint damage. Prolonged energy shortfall breaks down '
             'first fat and then muscle, and stops growth. Deficiency diseases — scurvy, rickets, '
             'anaemia — are caused by one missing nutrient and can occur at any level of energy '
             'intake.',
 'stretch': [{'type': 'explainer',
              'id': 'lind-and-the-gap',
              'text': 'In 1747 the naval surgeon James Lind ran what is often called the first '
                      'controlled clinical trial, on twelve scurvy patients divided into six '
                      'pairs, each pair given a different treatment: cider, sulfuric acid, '
                      'vinegar, seawater, a paste of herbs, or two oranges and a lemon. The citrus '
                      'pair recovered. The trial was tiny, it was not blinded, and Lind himself '
                      'did not fully accept the result — he thought the fruit worked by helping '
                      'digestion and later recommended a boiled-down concentrate that destroyed '
                      'the vitamin C entirely. The Navy took another forty years to adopt lemon '
                      'juice, and it saved more sailors than any battle of the period. Good '
                      'evidence and correct interpretation are different achievements, and the gap '
                      'between them is measured in lives.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to work through why a deficiency can happen on a full plate?',
           'cta': 'Ask about this lesson',
           'anchor': 's-three'},
 'ws': ['analysis-and-evaluation'],
 'safeguarding_note': 'If any of this is about you or someone you know, talk to someone you trust '
                      '— a parent or carer, a teacher, your school nurse, a pharmacist or your GP. '
                      'Out of school hours: Childline — 0800 1111, free and confidential.',
 'safety_note': 'This lesson describes conditions clinically, as biology. It is not advice about '
                "anybody's own body or eating, and it sets no targets. If any of it worries you "
                'about yourself or someone you know, speak to a trusted adult, your school nurse '
                'or a doctor — that is the right next step, not a change to what you eat.',
 'review_state': 'draft',
 'authored': True}
