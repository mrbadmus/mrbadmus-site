# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C1 `changes-of-state` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C1'
SOURCE_SLUG = 'changes-of-state'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'changes-of-state',
 'title': 'Changes of state',
 'discipline': 'chemistry',
 'unit': 'particles-and-their-behaviour',
 'family': 'PROCESS',
 'covers': ['KS3.C.PNM.02', 'KS3.P.PHYC.01'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'particles', 'level': 2}, {'id': 'energy', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['solids-liquids-and-gases'],
 'assumes': [],
 'references': ['gas-pressure'],
 'connects_heading': 'Next in this unit',
 'ks4_links': ['chemistry/bonding/states-of-matter'],
 'big_question': 'Put a beaker of ice on a hot ring and the temperature climbs. Then, for six full '
                 'minutes, it stops climbing — while the flame is still on. Where is that energy '
                 'going?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Sealed bag', 'done_when': 'committed'},
          {'anchor': 's-curve',
           'short': 'CURVE',
           'label': 'Heating bench',
           'done_when': 'both_plateaus_visited'},
          {'anchor': 's-bubble',
           'short': 'BUBBLE',
           'label': 'In the bubble',
           'done_when': 'committed'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Melt or dissolve',
           'done_when': 'all_cards_sorted'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'demo',
                'title': 'An ice cube in a bag.',
                'prompt': 'An ice cube, 50 g, sealed inside a bag. Weigh it. Leave it on the bench '
                          'until it is a puddle of water, then weigh the bag again.',
                'commit': 'If you had to guess, once the ice has melted, will the balance read '
                          'less than 50 g, or exactly 50 g?',
                'options': ['A bit less', 'Exactly 50 g'],
                'reveal': 'The same is true of boiling, freezing and condensing: the mass never '
                          'changes. Next: heat 50 g of ice steadily and watch the temperature.',
                'guess': True,
                'replies': ['It can feel as if some of the ice has gone, because a solid has '
                            'turned into a puddle. But the bag is sealed, so nothing has left it. '
                            'Every particle is still inside.',
                            'Melting moves the particles around but never removes any, and nothing '
                            'can leave a sealed bag. The balance has nothing to report.'],
                'answer': 1},
 'misconceptions': [{'id': 'PART-05',
                     'statement': 'When a substance melts or evaporates, some of it is lost or '
                                  'destroyed.',
                     'elicited_by': 'the-heating-bench',
                     'confronted_by': 'the-heating-bench'},
                    {'id': 'PART-06',
                     'statement': 'Melting and dissolving are the same thing.',
                     'elicited_by': 'melt-or-dissolve',
                     'confronted_by': 'melt-or-dissolve'},
                    {'id': 'PART-07',
                     'statement': 'Bubbles in boiling water are made of air, or of nothing.',
                     'elicited_by': 'the-bubble',
                     'confronted_by': 'the-bubble'}],
 'vocabulary': [{'term': 'melting',
                 'definition': 'Changing from a solid to a liquid.',
                 'note': None},
                {'term': 'freezing',
                 'definition': 'Changing from a liquid to a solid.',
                 'note': 'Freezing and melting happen at the same temperature for a given '
                         'substance — they are the same doorway, used in opposite directions.'},
                {'term': 'evaporating',
                 'definition': 'Changing from a liquid to a gas.',
                 'note': None},
                {'term': 'condensing',
                 'definition': 'Changing from a gas to a liquid.',
                 'note': None},
                {'term': 'sublimation',
                 'definition': 'Changing straight from a solid to a gas, with no liquid in '
                               'between.',
                 'note': 'Solid carbon dioxide does this — which is why it is called dry ice.'},
                {'term': 'conserved',
                 'definition': 'Stays the same in total. Nothing is gained or lost.',
                 'note': None}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Melting, freezing, boiling, condensing, evaporating. Five words for the same '
                   'short list of events: particles gaining enough energy to break away from their '
                   'neighbours, or losing enough to be captured again. Nothing else happens. '
                   'Nothing is made and nothing is lost.'},
          {'type': 'check', 'id': 'the-heating-bench', 'anchor': 's-curve'},
          {'type': 'key-fact', 'ref': 'temperature-holds'},
          {'type': 'practical', 'id': 'the-bubble', 'anchor': 's-bubble'},
          {'type': 'misconception', 'id': 'melt-or-dissolve', 'anchor': 's-think'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'temperature-holds',
                'text': 'During a change of state the temperature does not change: the energy goes '
                        'into breaking the particles apart from each other, not into speeding them '
                        'up. Mass stays the same throughout.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'demand': 'investigate',
                 'targets': 'PART-05',
                 'eyebrow': 'The heating bench · scrub through it',
                 'heading': 'Heat it steadily and watch the temperature refuse to rise.',
                 'head_counter': {'format': '{n} of {total} plateaus visited', 'total': 2},
                 'prompt': '50 g of ice at −20 °C in a sealed flask, on a ring that delivers the '
                           'same energy every second from start to finish. Drag through the run.',
                 'gate': {'prompt': 'Commit first. The energy goes in at a steady rate. What will '
                                    'the temperature do?',
                          'options': ['Rise steadily the whole way, in a straight line',
                                      'Rise, then stop twice while the state changes, then rise '
                                      'again',
                                      'Rise faster and faster as it gets hotter',
                                      'Rise to 100 °C and stay there forever']},
                 'keys': [[0, -20], [6, 0], [15, 0], [34, 100], [95, 100], [100, 120]],
                 'phases': [{'id': 'ice',
                             'label': 'Ice',
                             'tone': 'ink',
                             'note': 'Solid ice, warming. The energy is going straight into making '
                                     'the particles vibrate harder, and the thermometer reports it '
                                     'faithfully.'},
                            {'id': 'melting',
                             'label': 'Melting',
                             'tone': 'accent',
                             'band': 'MELTING',
                             'banner': 'ORDER BREAKING DOWN',
                             'note': 'The thermometer has stopped at 0 °C and it will not move '
                                     'until the last of the ice has gone — but the heater has not '
                                     'stopped. Every joule going in now is being spent breaking '
                                     'particles out of the rigid arrangement. Watch the flask: '
                                     'order is being destroyed, and the mass has not shifted by a '
                                     'milligram.'},
                            {'id': 'water',
                             'label': 'Water',
                             'tone': 'ink',
                             'note': 'All liquid now, and the temperature climbs again. Notice '
                                     'this stretch is much longer than the ice stretch — water '
                                     'takes more energy per degree than almost anything else, '
                                     'which is why the sea moderates the climate.'},
                            {'id': 'boiling',
                             'label': 'Boiling',
                             'tone': 'accent',
                             'band': 'BOILING',
                             'banner': 'BREAKING AWAY COMPLETELY',
                             'note': 'The second plateau, at 100 °C, and it is far longer than the '
                                     'melting one. Melting only loosens the particles; boiling has '
                                     'to separate them completely, and that costs about seven '
                                     'times as much energy.'},
                            {'id': 'steam',
                             'label': 'Steam',
                             'tone': 'ink',
                             'note': 'Steam, above 100 °C, warming quickly — there is almost '
                                     'nothing to slow it down now. Same 50 g of water that started '
                                     'as ice. Not one particle has been created or destroyed in '
                                     'the whole run.'}],
                 'mass': '50.0 g',
                 'labels': {'scrub': 'Energy put in · drag to move through the run',
                            'temperature': 'Temperature',
                            'phase': 'What is in the flask',
                            'mass': 'Mass in the flask',
                            'unit': '°C'},
                 'jumps': [{'label': 'Jump to melting', 'value': 10},
                           {'label': 'Jump to boiling', 'value': 64},
                           {'label': 'Back to the start', 'value': 0}],
                 'graph': {'t_min': -30,
                           't_max': 130,
                           'grid': [-20, 0, 50, 100, 120],
                           'ticks': [-20, 0, 100, 120],
                           'y_label': 'TEMPERATURE / °C',
                           'x_label': 'ENERGY IN, INCREASING'},
                 'flask': {'caption': 'SEALED FLASK — 50.0 g THROUGHOUT'},
                 'alt': {'template': 'A heating curve for 50 g of water with the marker at {t} '
                                     'degrees Celsius, and a flask showing the particles as '
                                     '{phase}.'},
                 'valuetext': '{t} degrees, {phase}',
                 'id': 'the-heating-bench',
                 'kind': 'heating-bench'},
                {'demand': 'predict',
                 'targets': 'PART-07',
                 'eyebrow': 'The bubble · a small question with a large answer',
                 'heading': 'What is inside a bubble in boiling water?',
                 'prompt': 'A pan of water at a rolling boil. Bubbles form at the bottom, rise, '
                           'and burst at the surface. Commit to what is in one.',
                 'options': [{'text': 'Air that was dissolved in the water',
                              'reply': 'Not this one. Follow the consequence of your answer '
                                       'through.'},
                             {'text': 'Nothing — it is an empty space',
                              'reply': 'Not this one. Follow the consequence of your answer '
                                       'through.'},
                             {'text': 'Water that has turned into a gas',
                              'reply': 'Correct — and it is worth knowing why the other three '
                                       'fail.'},
                             {'text': 'Hydrogen and oxygen, split apart by the heat',
                              'reply': 'No. Splitting water into hydrogen and oxygen is a chemical '
                                       'change and takes far more energy than a kettle has; '
                                       'boiling is a change of state and the water is still '
                                       'water.'}],
                 'answer_index': 2,
                 'reveal': ['Steam. Water that has boiled into a gas, right there at the bottom of '
                            'the pan where it is hottest. If a bubble were air, the pan would run '
                            'out of air after a minute and stop bubbling — and boiling water does '
                            'not stop bubbling. If a bubble were empty, the water pressure would '
                            'crush it instantly.',
                            'And the steam you can <em>see</em> above the pan is not steam. Steam '
                            'is invisible. What you see is the steam having already condensed back '
                            'into tiny drops of liquid water in the cold air — a change of state '
                            'happening in front of you, twice, in the space of a few centimetres.'],
                 'id': 'the-bubble',
                 'kind': 'keyed-commit'},
                {'demand': 'classify',
                 'targets': 'PART-06',
                 'statements': ['Sugar melts in tea.'],
                 'prompt': 'Everyone says it and it is the wrong word. Sort each of these into the '
                           'right column before you read on — the sorting is the point, not the '
                           'score.',
                 'buttons': [{'label': 'Melting', 'value': 'melt'},
                             {'label': 'Dissolving', 'value': 'dissolve'}],
                 'items': [{'id': 's1',
                            'text': 'A sugar cube stirred into hot tea',
                            'answer': 'dissolve',
                            'right': 'Dissolving. Two substances, and the sugar particles spread '
                                     'out among the water particles.',
                            'wrong': 'Not melting — tea is nowhere near sugar’s melting point of '
                                     'about 186 °C. Two substances are involved, so this is '
                                     'dissolving.'},
                           {'id': 's2',
                            'text': 'Butter left in a pan over a low flame',
                            'answer': 'melt',
                            'right': 'Melting. One substance, heated until its particles break out '
                                     'of their fixed positions.',
                            'wrong': 'Nothing is being spread through a liquid here. One '
                                     'substance, heated — that is melting.'},
                           {'id': 's3',
                            'text': 'Salt stirred into cold water',
                            'answer': 'dissolve',
                            'right': 'Dissolving. Cold water, so no heating is involved at all — '
                                     'and it still happens.',
                            'wrong': 'The water is cold, so nothing has been heated past a melting '
                                     'point. Salt melts at 801 °C.'},
                           {'id': 's4',
                            'text': 'A chocolate bar left on a sunny windowsill',
                            'answer': 'melt',
                            'right': 'Melting. One substance, warmed above its melting point, and '
                                     'it sets again when it cools.',
                            'wrong': 'There is no second substance for it to spread into. Warmed '
                                     'above its melting point, it melts — and re-solidifies on '
                                     'cooling.'}],
                 'summary': ['Melting needs one substance and heat: the particles of that '
                             'substance break out of their fixed positions, and if you cool it the '
                             'solid comes straight back. Dissolving needs two substances and no '
                             'heat at all: the particles of the solid separate and slot in among '
                             'the particles of the liquid, and to get the solid back you have to '
                             'remove the liquid.',
                             'Sugar in tea is dissolving. Sugar in a dry pan over a flame really '
                             'does melt, at about 186 °C. It is an awkward example, because sugar '
                             'starts browning and breaking down at around its melting point — and '
                             'that browning is a chemical change, not a melt. Same substance, two '
                             'entirely different events, and the word you choose says which one '
                             'you mean.'],
                 'id': 'melt-or-dissolve',
                 'kind': 'sort-cards'}],
 'ladder': {'recall': {'title': 'Rung 1 · Recall',
                       'q': 'What is the name of the change from a gas to a liquid?',
                       'options': ['Evaporating', 'Freezing', 'Condensing', 'Sublimating'],
                       'answer': 2,
                       'feedback': {0: 'That is the other direction — liquid to gas.',
                                    1: 'Freezing is liquid to solid.',
                                    3: 'Sublimation is solid straight to gas, skipping the liquid '
                                       '— what dry ice does.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A beaker of ice and water is heated steadily. For six minutes the '
                           'thermometer stays at 0 °C. What is the energy doing during those six '
                           'minutes?',
                      'options': ['Breaking the particles free from their fixed positions',
                                  'Nothing — it is being lost to the room',
                                  'Warming the beaker instead of the water',
                                  'Making the water particles bigger'],
                      'answer': 0,
                      'feedback': {1: 'Heat is being lost to the room the whole time, before and '
                                      'after the plateau too — yet the climb only stops while ice '
                                      'remains. The ice is what is absorbing it.',
                                   2: 'Use a different beaker and the plateau still lasts the same '
                                      'time. It is the ice that is absorbing it.',
                                   3: 'Particles never change size. This is the misconception from '
                                      'the last lesson wearing a new hat.'}},
            'explain': {'title': 'Rung 3 · Explain',
                        'q': 'Explain why the temperature stops rising while ice is melting, even '
                             'though the heater is still supplying energy at the same rate.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Temperature is a measure of…',
                        'success': ['Says temperature is a measure of the average kinetic energy '
                                    'of the particles — the energy they have because they are '
                                    'moving.',
                                    'Says the energy going in during melting is used to break the '
                                    'particles apart from each other.',
                                    'Says that energy is not going into making the particles move '
                                    'faster.',
                                    'Says the temperature therefore stays constant until all the '
                                    'ice has melted.',
                                    'Says the energy is not lost — it is stored, and released '
                                    'again when the water freezes.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A wet towel dries on a washing line on a cold day, at 8 °C. Water '
                             'boils at 100 °C. Explain how the water can become a gas at a '
                             'temperature far below its boiling point.',
                        'field_label': 'Your answer',
                        'placeholder': 'Not all the particles in the water…',
                        'success': ['Says the particles in the water do not all move at the same '
                                    'speed.',
                                    'Says the fastest particles at the surface can escape even '
                                    'when the average is low.',
                                    'Says this is evaporation, and it happens from the surface '
                                    'only.',
                                    'Says boiling is different: it happens throughout the liquid, '
                                    'at one fixed temperature.',
                                    'Says the water left behind is cooler, because the fastest '
                                    'particles are the ones that left.']}},
 'key_note': 'Changes of state are reversible, cost or release energy, and never change the mass. '
             'Temperature holds still at the melting and boiling points because the energy is '
             'buying separation, not speed.',
 'stretch': [{'type': 'explainer',
              'id': 'steam-burns',
              'text': 'The plateau has a practical consequence you have felt. Water at 100 °C will '
                      'scald you; steam at 100 °C — the same temperature — will do far worse, '
                      "because every gram of it has to give back the whole boiling plateau's worth "
                      'of energy as it condenses on your skin, and that is about seven times the '
                      'energy released by the same water cooling from 100 °C to room temperature. '
                      'Nothing about the temperature reading warns you. This is also how a '
                      'sweating body cools itself, how a fridge works, and why a puddle can '
                      'evaporate on a cold day without ever reaching 100 °C.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure where the energy goes during the plateau?',
           'cta': 'Ask about this lesson',
           'anchor': 's-curve'},
 'ks4_becomes': 'Specific heat capacity and specific latent heat — the plateau, turned into a '
                'number you can calculate with.',
 'ws': ['measurement', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
