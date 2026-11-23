# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C6 `acids-and-alkalis` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 860c783d26. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C6'
SOURCE_SLUG = 'acids-and-alkalis'
FROZEN_FROM = '860c783d26'

LESSON = {'slug': 'acids-and-alkalis',
 'title': 'Acids and alkalis',
 'discipline': 'chemistry',
 'unit': 'acids-and-alkalis',
 'family': 'CLASSIFY',
 'covers': ['KS3.C.CR.04'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['which-reaction-is-this'],
 'assumes': [],
 'references': [],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Two clear, colourless liquids. One is an acid and the other an alkali, and both '
                 'can burn your skin — and nothing you can see tells you which is which.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Two beakers', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Eight bottles',
           'done_when': 'all_eight_decided'},
          {'anchor': 's-hazard',
           'short': 'JUDGE',
           'label': 'Three judgements',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Which one burns',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two beakers, both clear, both colourless. One is hydrochloric acid. One '
                         'is sodium hydroxide.',
                'prompt': 'The labels have come off. Both are dangerous, so tasting is out and so '
                          'is touching. They are the same temperature, they pour the same, they '
                          'smell of nothing. Everything your eyes can do has already been done.',
                'commit': 'If you had to guess, which would show you which one is the acid: '
                          'weighing each, or adding a few drops of a dye?',
                'options': ['Weigh each one', 'Add a dye'],
                'reveal': 'A dye that does this is called an indicator. Next: what acid and alkali '
                          'mean, then eight everyday bottles to sort.',
                'guess': True,
                'replies': ['Weighing is how we tell many things apart. But nothing says an acid '
                            'must be heavier than an alkali. What shows the difference is what '
                            'each does to something.',
                            'Acid and alkali are not things you can see or weigh. A dye changes '
                            'colour differently in each, so it shows the difference in a second.'],
                'answer': 1},
 'misconceptions': [{'id': 'ACID-01',
                     'statement': 'Acids are the dangerous ones. Alkalis are what you use to make '
                                  'things safe.',
                     'elicited_by': 'think-commit-danger',
                     'confronted_by': 'think-commit-danger'},
                    {'id': 'ACID-02',
                     'statement': 'A dilute acid is no longer really an acid.',
                     'elicited_by': 'judgement-dilute',
                     'confronted_by': 'judgement-dilute-reveal'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'An <strong>acid</strong> is a substance that releases hydrogen into solution '
                   'when it dissolves in water. That is what makes vinegar sharp, what makes your '
                   'stomach able to break down meat, and what makes battery acid eat through '
                   'cloth. Acids have a pH below 7.'},
          {'type': 'explainer',
           'text': 'An <strong>alkali</strong> is the opposite kind of substance: it cancels acids '
                   'out. Alkalis are the ones that dissolve; the wider family they belong to is '
                   'called <strong>bases</strong>, and a base that dissolves in water is an '
                   'alkali. Alkalis have a pH above 7.'},
          {'type': 'explainer',
           'text': 'Everything else is <strong>neutral</strong> — pH exactly 7, neither one nor '
                   'the other. Pure water is the obvious example; most of what you drink sits just '
                   "on the acid side of it, which is the next lesson's scale."},
          {'type': 'check', 'id': 'bench-eight', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'either-side-of-seven'},
          {'type': 'check', 'id': 'hazard-three', 'anchor': 's-hazard'},
          {'type': 'misconception',
           'id': 'think-commit-danger',
           'anchor': 's-think',
           'targets': 'ACID-01'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'either-side-of-seven',
                'text': 'Acids have a pH below 7 and alkalis have a pH above 7. An alkali is a '
                        'base that dissolves in water, and it cancels an acid out. Neutral is '
                        'exactly 7.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-danger',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ACID-01',
                 'prompt': 'Every hazard film you have seen involves an acid. Commit before you '
                           'read on.',
                 'options': ['Right — alkalis are the safe half of the scale, and acids are the '
                             'dangerous half',
                             'Wrong — a strong alkali burns as badly as a strong acid, sometimes '
                             'worse',
                             'Right, because an alkali neutralises an acid and neutral is always '
                             'the safe state',
                             'Wrong — alkalis are the dangerous ones and acids are the half you '
                             'can safely handle'],
                 'reveal': ['Strong alkalis are, if anything, worse. Sodium hydroxide — the alkali '
                            'in oven cleaner and drain unblocker — dissolves fat and skin, and eye '
                            'damage from it can be permanent. It does not sting straight away, '
                            'which is exactly why people leave it on their hands. A strong acid '
                            'announces itself; a strong alkali feels soapy.',
                            'Meanwhile the acid in an orange is safe enough to drink a litre of. '
                            '<strong>Being an acid or an alkali says which side of 7 it sits on. '
                            'It does not say how hard it hits.</strong> That is a separate '
                            'question, and it has its own scale — coming next lesson.']},
                {'eyebrow': 'Your turn · eight bottles on the bench',
                 'heading': 'Acid, alkali or neutral? Commit on all eight.',
                 'prompt': 'Guessing is allowed — the ones you get wrong are the ones worth '
                           'reading.',
                 'demand': 'classify',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'options': [{'id': 'acid', 'label': 'Acid'},
                             {'id': 'alkali', 'label': 'Alkali'},
                             {'id': 'neutral', 'label': 'Neutral'}],
                 'bottles': [{'id': 'b1',
                              'name': 'Lemon juice',
                              'where': 'kitchen',
                              'answer': 'acid',
                              'verdict': 'Lemon juice is an acid.',
                              'why': 'Citric acid, pH about 2. Sharp enough to taste and weak '
                                     'enough to drink — which is the first sign that acid and '
                                     'danger are separate questions.'},
                             {'id': 'b2',
                              'name': 'Oven cleaner',
                              'where': 'cleaning cupboard',
                              'answer': 'alkali',
                              'verdict': 'Oven cleaner is an alkali.',
                              'why': 'Sodium hydroxide, pH about 13. It dissolves baked-on fat by '
                                     'taking it apart chemically, and it will do the same to skin. '
                                     'The most dangerous bottle on this bench is not an acid.'},
                             {'id': 'b3',
                              'name': 'Pure water',
                              'where': 'wash bottle',
                              'answer': 'neutral',
                              'verdict': 'Pure water is neutral.',
                              'why': 'pH exactly 7 — the definition of neutral. Tap water is '
                                     'usually a shade either side of it depending on what the rock '
                                     'it travelled through was made of.'},
                             {'id': 'b4',
                              'name': 'Vinegar',
                              'where': 'kitchen',
                              'answer': 'acid',
                              'verdict': 'Vinegar is an acid.',
                              'why': 'Ethanoic acid, pH about 3. The same acid that will strip '
                                     'limescale off a kettle goes on chips.'},
                             {'id': 'b5',
                              'name': 'Indigestion tablet in water',
                              'where': 'chemist',
                              'answer': 'alkali',
                              'verdict': 'An indigestion tablet in water is an alkali.',
                              'why': 'A mild alkali, pH about 9 or 10 — sold precisely because it '
                                     'cancels out stomach acid. Mild enough to swallow, which is '
                                     'the whole point of it.'},
                             {'id': 'b6',
                              'name': 'Battery acid',
                              'where': 'garage',
                              'answer': 'acid',
                              'verdict': 'Battery acid is an acid.',
                              'why': 'Sulfuric acid, pH close to 0. This is the one that matches '
                                     'the mental picture: it burns cloth, skin and metal on '
                                     'contact.'},
                             {'id': 'b7',
                              'name': 'Sodium chloride solution',
                              'where': 'salt in water',
                              'answer': 'neutral',
                              'verdict': 'Sodium chloride solution is neutral.',
                              'why': 'pH 7. It is made from an acid and an alkali reacting '
                                     'together, and what is left over sits exactly in the middle — '
                                     'which is the next lesson but one.'},
                             {'id': 'b8',
                              'name': 'Garden lime',
                              'where': 'shed',
                              'answer': 'alkali',
                              'verdict': 'Garden lime is an alkali.',
                              'why': 'Calcium hydroxide, pH about 12. It is spread on soil that '
                                     'has turned too acidic for crops — neutralisation used on a '
                                     'field-sized scale.'}],
                 'pattern': {'id': 'bench-pattern',
                             'title': 'Look at where they turn up.',
                             'text': 'The acids are in the food cupboard and in your own stomach. '
                                     'The alkalis are in the cleaning cupboard, and one of them is '
                                     'in the soil bag. Neither list is a list of poisons — you eat '
                                     'acids every day, and the alkali in indigestion tablets is '
                                     'sold in a chemist. <strong>Dangerous</strong> and '
                                     '<strong>acidic</strong> are two different questions, and the '
                                     'bench proves it: the most dangerous thing here is an '
                                     'alkali.'},
                 'id': 'bench-eight',
                 'kind': 'bottle-sorter'},
                {'eyebrow': 'Three judgements',
                 'heading': 'How dangerous, and why',
                 'prompt': 'Commit to each before you read what happens. Two of the three catch '
                           'almost everybody.',
                 'demand': 'explain',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'items': [{'id': 'j1',
                            'dom_id': 'judgement-dilute',
                            'reveal_id': 'judgement-dilute-reveal',
                            'q': 'A bottle of concentrated acid is diluted with a lot of water. Is '
                                 'it still an acid?',
                            'options': [{'id': 'yes', 'label': 'Yes'}, {'id': 'no', 'label': 'No'}],
                            'answer': 'yes',
                            'reply': 'Yes. Diluting adds water, so there is less acid in each cm³ '
                                     'and it does far less damage — but every drop of it is still '
                                     'acid and the pH is still below 7. Weaker in effect, '
                                     'unchanged in kind. That difference between how much acid and '
                                     'how fierce the acid is has caught out generations of '
                                     'students.'},
                           {'id': 'j2',
                            'q': 'Someone spills sodium hydroxide on their hand and feels nothing '
                                 'much. Should they wash it off?',
                            'options': [{'id': 'yes', 'label': 'Yes'}, {'id': 'no', 'label': 'No'}],
                            'answer': 'yes',
                            'reply': 'Immediately, under running water, for a long time. Alkalis '
                                     'do not sting on contact the way acids do — they feel soapy, '
                                     'because they are turning the fat in your skin into soap. By '
                                     'the time it hurts, the damage is done. The lack of pain is '
                                     'the hazard.'},
                           {'id': 'j3',
                            'q': 'Is the acid in your stomach stronger than the acid in vinegar?',
                            'options': [{'id': 'yes', 'label': 'Yes'}, {'id': 'no', 'label': 'No'}],
                            'answer': 'yes',
                            'reply': 'Considerably. Stomach acid is hydrochloric acid at roughly '
                                     'pH 2; vinegar is around pH 3, and the scale is not evenly '
                                     'spaced — each step is a factor of ten. Your own stomach is '
                                     'more corrosive than a bottle of malt vinegar, and it is kept '
                                     'in by a lining that replaces itself every few days.'}],
                 'id': 'hazard-three',
                 'kind': 'acid-judgements'}],
 'ladder': {'recall': {'q': 'What is an alkali?',
                       'options': ['A base that dissolves in water, with a pH above 7',
                                   'An acid that dissolves in water, with a pH below 7',
                                   'A base that does not dissolve in water, with a pH of 7',
                                   'Any substance that dissolves in water, with a pH of exactly 7'],
                       'answer': 0,
                       'feedback': {1: 'That describes an acid. An alkali has a pH above 7.',
                                    2: 'A base that does not dissolve is not an alkali. Alkalis '
                                       'are above 7.',
                                    3: 'A pH of exactly 7 is neutral. An alkali has a pH above '
                                       '7.'}},
            'apply': {'q': 'A student says: “Orange juice is an acid, so it must be dangerous.” '
                           'What is wrong with the reasoning?',
                      'options': ['Orange juice is not an acid, as it is a natural fruit juice',
                                  'Not all acids are dangerous, as orange juice is only weakly '
                                  'acidic',
                                  'All acids are dangerous, but one glass is too small to harm you',
                                  'Orange juice is neutral, as fruit juices all have a pH of '
                                  'exactly 7'],
                      'answer': 1,
                      'feedback': {0: 'Orange juice is an acid. It contains citric acid and has a '
                                      'pH below 7.',
                                   2: 'Not every acid is dangerous. Weakly acidic orange juice is '
                                      'safe to drink.',
                                   3: 'Orange juice has a pH below 7, so it is acidic, not '
                                      'neutral.'}},
            'explain': {'q': 'Two unlabelled colourless liquids are on the bench: one is an acid '
                             'and one is an alkali. Explain how you would find out which is which, '
                             'and why looking at them cannot answer it.',
                        'field_label': 'Your explanation',
                        'placeholder': 'I would add…',
                        'success': ['Says to add an indicator to a sample of each.',
                                    'Says the indicator changes to different colours in acid and '
                                    'in alkali.',
                                    'Says acid gives a pH below 7 and alkali above 7.',
                                    'Says being an acid or alkali is a chemical property, so it '
                                    'cannot be seen.',
                                    'Says to test a small sample rather than the whole bottle, and '
                                    'not to taste or touch.']},
            'produce': {'q': 'A gardener is told their soil is too acidic for the crop they want '
                             'to grow. Explain what they should add and why it works — and say '
                             'what could go wrong if they add far too much.',
                        'field_label': 'Your answer',
                        'placeholder': 'They should add…',
                        'success': ['Says to add an alkali, such as lime or calcium hydroxide.',
                                    'Says the alkali cancels out or neutralises the acid in the '
                                    'soil.',
                                    'Says this raises the pH towards 7.',
                                    'Says too much would push the soil past neutral and make it '
                                    'alkaline.',
                                    'Says the soil should be tested afterwards rather than assumed '
                                    'to be right.']}},
 'key_note': 'Acids have a pH below 7, alkalis above 7, and neutral substances exactly 7. An '
             'alkali is a base that dissolves in water, and the two cancel each other out. Whether '
             'something is acidic tells you nothing about whether it is safe: lemon juice is an '
             'acid you can drink and oven cleaner is an alkali that will burn you.',
 'stretch': [{'type': 'explainer',
              'id': 'bases-that-do-not-dissolve',
              'text': 'Not every base is an alkali. Copper oxide, magnesium oxide and calcium '
                      'carbonate all neutralise acids perfectly well, but they barely dissolve in '
                      'water — so they are bases and not alkalis. The distinction matters in the '
                      'lab: to neutralise an acid with a base that will not dissolve, you warm the '
                      'acid and stir the solid in until no more will react, then filter off what '
                      'is left. That is a method you will meet again when you make a salt on '
                      'purpose.'},
             {'type': 'explainer',
              'id': 'your-own-stomach',
              'text': 'Your stomach runs at about pH 2, which is strong enough to dissolve iron '
                      'filings and does dissolve the meat you eat. The lining survives because it '
                      'is replaced constantly and coated in mucus; where that coating fails, the '
                      'acid attacks the stomach itself and the result is an ulcer. For a long time '
                      'ulcers were treated as a stress problem. In 1984 an Australian doctor drank '
                      'a flask of bacteria to prove they were an infection, gave himself '
                      'gastritis, and eventually won a Nobel Prize for it.'}],
 'support': [],
 'vocabulary': [{'term': 'Acid',
                 'definition': 'A substance that releases hydrogen into solution when it dissolves '
                               'in water. Acids have a pH below 7.'},
                {'term': 'Alkali',
                 'definition': 'A base that dissolves in water. Alkalis have a pH above 7 and they '
                               'cancel acids out.'},
                {'term': 'Base',
                 'definition': 'Any substance that cancels an acid out. The ones that dissolve in '
                               'water are called alkalis; plenty of others do not dissolve.',
                 'note': 'Every alkali is a base. Most bases are not alkalis.'},
                {'term': 'Neutral',
                 'definition': 'Neither acidic nor alkaline — pH exactly 7. Pure water is the '
                               'standard example.'},
                {'term': 'pH',
                 'definition': 'The number that says how acidic or alkaline something is. Below 7 '
                               'is acidic, 7 is neutral, above 7 is alkaline.'},
                {'term': 'Indicator',
                 'definition': 'A dye that changes colour depending on whether it is in an acid or '
                               'an alkali. It is how the two are told apart when looking cannot.'},
                {'term': 'Corrosive',
                 'definition': 'Able to attack and destroy materials it touches, including skin. '
                               'Strong acids and strong alkalis are both corrosive.'}],
 'safety_note': 'Oven cleaner and drain unblocker are strong alkalis and battery acid is a strong '
                'acid. None of them is a thing to test at home: a strong alkali does not hurt on '
                'contact, so there is no signal telling you to wash it off, and by the time there '
                'is one the damage is done. Eye protection on before you start. Even dilute acid '
                'and alkali sting badly if they get in your eyes. If anything splashes on your '
                'skin, wash it off with plenty of cold water and tell your teacher straight away.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still unsure why a base is not always an alkali?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'ks4_becomes': 'Acids as sources of hydrogen ions (H+) in solution, alkalis as sources of '
                'hydroxide ions (OH−), and the difference between a strong acid and a concentrated '
                'one.',
 'ws': ['scientific-attitudes', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
