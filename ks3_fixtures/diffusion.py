# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C1 `diffusion` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C1'
SOURCE_SLUG = 'diffusion'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'diffusion',
 'title': 'Diffusion',
 'discipline': 'chemistry',
 'unit': 'particles-and-their-behaviour',
 'family': 'MODEL',
 'covers': ['KS3.C.PIS.03', 'KS3.P.PHYC.04'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'particles', 'level': 3}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': ['gas-pressure'],
 'assumes': [],
 'references': ['testing-the-model'],
 'connects_heading': 'Next in this unit',
 'ks4_links': ['chemistry/bonding/states-of-matter'],
 'big_question': 'Someone opens a bottle of perfume at the far end of a room. Before long you can '
                 'smell it. How does it get to you?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'The still room',
           'done_when': 'committed'},
          {'anchor': 's-walk',
           'short': 'WALK',
           'label': 'Random walk',
           'done_when': 'tank_has_evened_out'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Wanting to spread',
           'done_when': 'committed'},
          {'anchor': 's-scale',
           'short': 'SCALE',
           'label': 'Distance and time',
           'mirrors': 's-think',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'demo',
                'title': 'A bottle of perfume in a still room.',
                'prompt': 'A bottle of perfume is opened at the far end of a room. The windows are '
                          'shut, the air is dead still, and a candle flame at the centre of the '
                          'room stands perfectly upright, so there is no draught at all.',
                'commit': 'If you had to guess, with no draught to carry it, will the smell of the '
                          'perfume ever reach you?',
                'options': ['Yes, in the end', 'No, it needs a draught'],
                'reveal': 'Spreading out with nothing pushing has a name: diffusion. Next: a drop '
                          'of dye in still water, followed one particle at a time.',
                'guess': True,
                'replies': ['The perfume particles spread out by themselves, bouncing off the air '
                            'particles on the way. It is slow, but no draught is needed.',
                            'In a real room draughts do carry a smell most of the way. But even '
                            'with the air perfectly still, the perfume gets there on its own.'],
                'answer': 0},
 'misconceptions': [{'id': 'PART-10',
                     'statement': 'Diffusion needs a draught, a current, or someone to waft it — '
                                  'something has to push the particles along.',
                     'elicited_by': 'hook',
                     'confronted_by': 'walk-bench'},
                    {'id': 'PART-11',
                     'statement': "Particles move in order to spread out — they 'want' to fill the "
                                  'space, or they move from crowded to empty on purpose.',
                     'elicited_by': 'think-spread',
                     'confronted_by': 'walk-bench'}],
 'vocabulary': [{'term': 'diffusion',
                 'definition': 'The spreading out of particles from where there are many to where '
                               'there are few, caused by their own random movement.',
                 'note': None},
                {'term': 'concentration',
                 'definition': 'How many particles of a substance there are in a given space.',
                 'note': None},
                {'term': 'random',
                 'definition': 'With no pattern and no set direction.',
                 'note': "In science 'random' does not mean 'strange'. It means genuinely "
                         'unpredictable, direction by direction.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Diffusion is the one piece of the particle model that people find hardest to '
                   'accept, because it looks purposeful. Something spreads out and fills a space, '
                   'evenly, every time — and evenly-and-every-time is what deliberate things do. '
                   'This lesson takes the purpose out of it and leaves nothing but random '
                   'movement, which turns out to be enough.'},
          {'type': 'check', 'id': 'walk-bench', 'anchor': 's-walk'},
          {'type': 'key-fact', 'ref': 'spreading'},
          {'type': 'misconception',
           'id': 'think-spread',
           'anchor': 's-think',
           'targets': 'PART-11'},
          {'type': 'practical', 'id': 'scale-panel', 'anchor': 's-scale'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'spreading',
                'text': 'Diffusion is the spreading out of particles from where they are crowded '
                        'to where they are not, caused by their own random movement. Nothing '
                        'pushes them and nothing stops when it is finished.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-spread',
                 'kind': 'predict',
                 'targets': 'PART-11',
                 'statements': ['The particles spread out because they want to fill the space '
                                'evenly.'],
                 'prompt': 'Every word of that sentence is doing damage, and it is the sentence '
                           'almost everyone writes. Commit to what is wrong with it.',
                 'options': ['Nothing — that is a fair description of what happens',
                             'Particles cannot want anything; the evenness is what random movement '
                             'produces',
                             'They repel each other, so they push apart until evenly spread',
                             'Only gases spread like this; liquid particles are too packed to '
                             'move'],
                 'reveal': ['A particle has no goal, no information about the rest of the tank, '
                            'and no way to prefer one direction over another. It cannot want '
                            'anything. The evenness is not aimed at — it is what randomness '
                            'produces when you start with a crowd on one side.',
                            'The counters on the bench are the proof. At the start, far more '
                            'particles cross left-to-right than right-to-left — not because they '
                            'are heading that way, but because there are more of them on the left '
                            'to make the crossing. Once the two sides are even, the two counts '
                            'climb at the same rate and keep climbing. The spreading has finished; '
                            'the moving has not. If the particles were trying to fill the space, '
                            'they would stop when the job was done.']},
                {'targets': 'PART-10',
                 'eyebrow': 'The random-walk bench · watch one particle, then all of them',
                 'heading': 'No one is steering.',
                 'head_counter': {'format': '{phase}',
                                  'total': 0,
                                  'start_extra': {'phase': 'not started'}},
                 'prompt': 'A drop of dye released on the left of a sealed tank of still water. '
                           'Every particle takes a step in a random direction, over and over. '
                           'Nothing else is happening.',
                 'gate': {'prompt': 'Commit first. Once the dye has spread out completely and the '
                                    'tank looks even, what are the particles doing?',
                          'options': ['Nothing — they have stopped where they are',
                                      'Still moving randomly, equal numbers crossing each way',
                                      'Slowly sinking to the bottom',
                                      'Moving, but only away from where they started']},
                 'particles': 130,
                 'seed': {'x': [0.04, 0.17], 'y': [0.18, 0.82]},
                 'step': {'cool': 0.0055, 'warm': 0.011, 'y_scale': 1.5},
                 'bounds': {'x': [0.015, 0.985], 'y': [0.03, 0.97]},
                 'even': {'tolerance': 0.09, 'hz': 3},
                 'trail_max': 900,
                 'bins': 18,
                 'reduced_scale': 0.4,
                 'labels': {'cross_right': 'Crossings left to right',
                            'cross_left': 'Crossings right to left',
                            'even': 'Spread out?',
                            'even_yes': 'Yes',
                            'even_no': 'Not yet',
                            'run_start': 'Start the run',
                            'run_pause': 'Pause',
                            'run_continue': 'Continue',
                            'reset': 'Put the drop back',
                            'trace_on': 'Follow one particle',
                            'trace_off': 'Stop following one particle',
                            'warm_on': 'Warm the water',
                            'warm_off': 'Cool the water'},
                 'canvas_labels': {'left_half': 'LEFT HALF: ',
                                   'right_half': 'RIGHT HALF: ',
                                   'profile': 'HOW CROWDED, ALONG THE TANK'},
                 'notes': {'idle': 'The drop is sitting on the left. Nothing is pushing it, '
                                   'nothing is stirring, and there is no current in the tank. '
                                   'Press start and watch what randomness alone does — and warm '
                                   'the water if you want it sooner, because hotter particles move '
                                   'faster and the evening out comes on much more quickly.',
                           'spreading': 'Early on, more particles cross left-to-right than '
                                        'right-to-left — not because they know where to go, but '
                                        'because there are more of them on the left available to '
                                        'make the crossing. Watch the GAP between the two counters '
                                        'rather than their size: a single particle near the middle '
                                        'crosses the line again and again, so both totals run '
                                        'away. The gap is the net movement, and it is the whole of '
                                        'diffusion.',
                           'even': 'Evened out — and look at the two crossing counters. They are '
                                   'still climbing, at the same rate as each other. Particles are '
                                   'pouring across the middle in both directions, in equal '
                                   'numbers, forever. Nothing has stopped; the two flows have '
                                   'simply balanced.',
                           'tracing': 'The single traced particle is not going anywhere in '
                                      'particular. Its path doubles back on itself constantly — '
                                      'and the tangle is exactly why crossing a few centimetres '
                                      'takes so long when the particle itself is fast.'},
                 'progress': {'idle': 'not started',
                              'spreading': 'spreading',
                              'even': 'evened out'},
                 'alt': {'template': 'A tank of water with dye particles {state}, and a bar chart '
                                     'underneath showing how crowded each part of the tank is. '
                                     '{left} particles in the left half, {right} in the right.',
                         'even': 'spread evenly throughout',
                         'uneven': 'concentrated towards the left'},
                 'id': 'walk-bench',
                 'kind': 'random-walk-bench',
                 'demand': 'investigate'},
                {'eyebrow': 'Where this does real work',
                 'heading': 'Hopeless across a room, unbeatable across a cell',
                 'prompt': 'Diffusion is hopeless over long distances and unbeatable over short '
                           'ones, and that single fact shapes a great deal of biology.',
                 'scale_cards': [{'distance': 'Across a cell · 0.01 mm',
                                  'time': 'About a hundredth of a second',
                                  'text': 'Fast enough that a cell needs no delivery system at '
                                          'all. Oxygen simply arrives.'},
                                 {'distance': 'Across a fingertip · 10 mm',
                                  'time': 'About three hours',
                                  'text': 'Already hopeless. This is why you have a bloodstream, '
                                          'and why the blood is never more than a fraction of a '
                                          'millimetre from any cell.'},
                                 {'distance': 'Across a room · 4 m',
                                  'time': 'Far too slow on its own',
                                  'text': 'Gas particles move far faster and travel further '
                                          'between collisions than they do in a liquid — but '
                                          'across a whole room diffusion alone would take days. '
                                          'Draughts and convection carry a smell most of the way; '
                                          'diffusion covers the last stretch.'}],
                 'close': 'Double the distance and diffusion takes four times as long, not twice. '
                          'That is why every cell in your body is microscopic, why lungs are '
                          'folded into millions of tiny sacs instead of two smooth bags, and why '
                          'anything larger than an insect needs a heart.',
                 'id': 'scale-panel',
                 'kind': 'scale-cards',
                 'demand': 'investigate'}],
 'ladder': {'recall': {'q': 'Diffusion is the movement of particles from where they are…',
                       'options': ['Colder to where they are warmer',
                                   'Lower to where they are higher',
                                   'Heavier to where they are lighter',
                                   'More crowded to where they are less crowded'],
                       'answer': 3,
                       'feedback': {0: 'Temperature changes how fast diffusion happens, but the '
                                       'direction is set by crowding.',
                                    1: 'Diffusion works in every direction, including downwards.',
                                    2: 'Mass affects speed, not the direction of the spread.'}},
            'apply': {'q': 'A tank of dye has completely evened out. What is happening to the '
                           'particles now?',
                      'options': ['They are still moving randomly, with equal numbers crossing '
                                  'each way',
                                  'They have stopped, because the job is done',
                                  'They slow down and settle to the bottom',
                                  'They keep moving but only sideways now'],
                      'answer': 0,
                      'feedback': {1: 'Nothing tells a particle the job is done. Movement does not '
                                      'switch off.',
                                   2: 'Settling is what happens to particles too big to be jostled '
                                      '— sand, not dye.',
                                   3: 'There is no mechanism that could restrict them to one '
                                      'direction.'}},
            'explain': {'q': 'Explain how perfume particles move through the air on their own, and '
                             'why diffusion alone is so slow across a room even though the '
                             'particles travel at hundreds of metres per second.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The perfume particles are already moving…',
                        'success': ['Says the perfume particles are moving randomly on their own.',
                                    'Says no draught, push or carrier is needed.',
                                    'Says they collide constantly with air particles.',
                                    'Says each collision sends them off in a new direction, so the '
                                    'path is not straight.',
                                    'Says the actual distance travelled is enormous compared with '
                                    'the straight-line distance across the room.']},
            'produce': {'q': 'A drop of food colouring is put into a glass of cold water and an '
                             'identical drop into a glass of hot water. The hot one spreads much '
                             'faster. Explain why — and explain why the cold one still spreads '
                             'completely if you wait.',
                        'field_label': 'Your answer',
                        'placeholder': 'In the hot water the particles…',
                        'success': ['Says particles in hot water have more energy and move faster.',
                                    'Says faster movement means the colouring is jostled further '
                                    'in a given time.',
                                    'Says the direction of movement is random in both glasses.',
                                    'Says the cold glass spreads by exactly the same mechanism, '
                                    'only more slowly.',
                                    'Says neither needs stirring — stirring is a different process '
                                    'that moves whole regions of liquid at once.']}},
 'key_note': 'Random movement, no pushing, no purpose. Particles go from crowded to less crowded '
             'because there are more of them to leave the crowded side. Warmer means faster. The '
             'movement never stops, even when the spreading looks finished.',
 'stretch': [{'type': 'explainer',
              'id': 'brown-einstein-perrin',
              'text': 'In 1827 the botanist Robert Brown watched pollen grains in water through a '
                      'microscope and found them jittering about, endlessly, with nothing touching '
                      'them. He could not explain it and nor could anyone else for nearly eighty '
                      'years. Then in 1905 Einstein worked out that the jitter was exactly what '
                      'you would see if the water were made of invisible particles battering the '
                      'grain from every side, slightly unevenly, millions of times a second — and '
                      'he predicted precisely how far a grain should wander in a given time. When '
                      'Jean Perrin measured it and the numbers matched, the last serious '
                      'scientific doubt that atoms exist was gone. A dancing speck of pollen '
                      'settled it.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still feels like something must be pushing them?',
           'cta': 'Ask about this lesson',
           'anchor': 's-walk'},
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
