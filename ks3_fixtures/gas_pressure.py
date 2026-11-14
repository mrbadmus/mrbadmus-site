# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C1 `gas-pressure` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C1'
SOURCE_SLUG = 'gas-pressure'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'gas-pressure',
 'title': 'Gas pressure',
 'discipline': 'chemistry',
 'unit': 'particles-and-their-behaviour',
 'family': 'MODEL',
 'covers': ['KS3.C.PNM.01c'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'particles', 'level': 2}, {'id': 'forces-and-fields', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': ['changes-of-state'],
 'assumes': [],
 'references': ['diffusion'],
 'connects_heading': 'Next in this unit',
 'ks4_links': ['chemistry/bonding/states-of-matter'],
 'ks4_becomes': 'The gas laws — pressure, volume and temperature as quantities you can calculate '
                'with, and the kelvin scale that makes them work.',
 'big_question': 'A used-up aerosol can carries a warning: do not put it on a fire, it may '
                 'explode. What would make it burst?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The empty can', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'COUNT',
           'label': 'Collision counter',
           'done_when': 'three_controls_tried',
           'threshold': 3},
          {'anchor': 's-predict',
           'short': 'PREDICT',
           'label': 'Three predictions',
           'done_when': 'all_predictions_answered'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Swelling particles',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'eyebrow': 'Start here',
                'title': 'The can that sounds empty.',
                'prompt': 'Shake the can and it sounds empty. Press the nozzle and nothing comes '
                          'out. Put it in a bonfire and within a minute it will burst hard enough '
                          'to be dangerous at ten metres.',
                'commit': 'If you had to guess, is that can really empty inside?',
                'options': ['No, there is gas inside', 'Yes, it is really empty'],
                'reveal': 'Heat that gas and within a minute the steel gives way. Next: what a gas '
                          'is actually doing inside a sealed container.',
                'guess': True,
                'replies': ['The can is full of gas. There is no such thing as a sealed can with '
                            'nothing in it, even when it has stopped spraying.',
                            'Nothing sprays out, so it certainly seems empty. But the space inside '
                            'is full of gas that has simply stopped pushing its way out.'],
                'answer': 0},
 'misconceptions': [{'id': 'PART-08',
                     'statement': 'Gas pressure is the particles pushing against each other.',
                     'elicited_by': 'count-the-hits',
                     'confronted_by': 'count-the-hits'},
                    {'id': 'PART-09',
                     'statement': 'Heating a gas makes the particles swell up, so they fill more '
                                  'of the can, so the pressure goes up.',
                     'elicited_by': 'three-predictions',
                     'confronted_by': 'think-swelling-particles'}],
 'vocabulary': [{'term': 'pressure',
                 'definition': 'How hard a force pushes on each bit of a surface.',
                 'note': 'You will meet pressure = force ÷ area as a calculation in Physics P5.'},
                {'term': 'collision',
                 'definition': 'When a moving particle hits something and bounces off.',
                 'note': None},
                {'term': 'temperature',
                 'definition': 'How hot or cold something is. The hotter something is, the faster '
                               'its particles are moving.',
                 'note': 'Heating changes how fast the particles move and nothing else — never '
                         'their size.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Pressure is the one idea in this unit that people think they already '
                   'understand, which is what makes it dangerous. It feels like a squeezing, or a '
                   'crowdedness, or a force held inside the container. It is none of those. It is '
                   'particles hitting a wall, and the whole of this lesson is a machine for '
                   'counting them.'},
          {'type': 'check', 'id': 'count-the-hits', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'pressure-is-collisions'},
          {'type': 'practical', 'id': 'three-predictions', 'anchor': 's-predict'},
          {'type': 'misconception',
           'id': 'think-swelling-particles',
           'anchor': 's-think',
           'targets': 'PART-09'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'pressure-is-collisions',
                'text': 'Gas pressure is caused by particles colliding with the walls of the '
                        'container. More collisions, or harder ones, means more pressure.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-swelling-particles',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'PART-09',
                 'prompt': 'This explanation gets the right answer for the wrong reason, which is '
                           'the hardest kind of wrong idea to shift. Commit.',
                 'options': ['True — hotter particles are bigger particles',
                             'The particles move faster; their size never changes',
                             'The particles multiply, so there are more of them',
                             'The particles get heavier, so they hit harder'],
                 'reveal': ['Heating changes the <em>speed</em> of the particles and nothing else. '
                            'The reference particle at the bottom of the bench is drawn at the '
                            'same size at every temperature setting, and that is not a '
                            'simplification — it is the fact.',
                            'Here is the test that separates the two explanations. If heating made '
                            'particles swell, a hot gas would be harder to squash than a cold one, '
                            'because the particles would be taking up more of the room. It is not. '
                            'A hot gas squashes just as easily. And if the particles swelled, the '
                            'gas would eventually become a solid block of touching particles — the '
                            'opposite of what heating does.',
                            'Faster particles reach the wall more often, and hit it harder when '
                            'they get there. Two effects, one cause, no swelling.']},
                {'demand': 'investigate',
                 'targets': 'PART-08',
                 'eyebrow': 'The collision counter · change one thing at a time',
                 'heading': 'Count the hits on the wall.',
                 'head_counter': {'format': '{n} of 3 controls tried',
                                  'total': 3,
                                  'full': 'all controls tried'},
                 'gate': {'prompt': 'Commit first. What actually causes the pressure inside a '
                                    'sealed container of gas?',
                          'options': ['Particles pushing against each other',
                                      'Particles hitting the walls of the container',
                                      'The gas trying to escape to a bigger space',
                                      'The weight of the gas pressing down']},
                 'temps': [{'label': 'Cold', 'speed_multiplier': 0.55},
                           {'label': 'Warm', 'speed_multiplier': 1},
                           {'label': 'Hot', 'speed_multiplier': 1.75}],
                 'vols': [{'label': 'Large', 'volume': 1},
                          {'label': 'Half size', 'volume': 0.5},
                          {'label': 'Quarter size', 'volume': 0.25}],
                 'counts': [{'label': '12', 'n': 12},
                            {'label': '24', 'n': 24},
                            {'label': '48', 'n': 48}],
                 'start': {'temp': 1, 'vol': 0, 'count': 1},
                 'labels': {'temperature': 'Temperature',
                            'volume': 'Size of the container',
                            'particles': 'How many particles'},
                 'bumps': {'on_label': 'Show particle-to-particle bumps',
                           'off_label': 'Hide particle-to-particle bumps',
                           'caption': 'Particle-to-particle bumps are marked in grey. They never '
                                      'touch the wall, so they never add to the pressure.',
                           'threshold': 0.0022},
                 'canvas_labels': {'reference': 'ONE PARTICLE — SAME SIZE AT EVERY SETTING',
                                   'hits': 'WALL HITS PER SECOND',
                                   'pressure': 'PRESSURE',
                                   'pressure_unit': 'kPa',
                                   'temperature': 'TEMPERATURE',
                                   'container': 'CONTAINER',
                                   'particles': 'PARTICLES'},
                 'pressure_full': 170,
                 'kpa_per_hit': 7,
                 'smooth_ms': 900,
                 'readout_ms': 500,
                 'window_ms': 1000,
                 'flash_ms': 420,
                 'reduced_motion_scale': 0.35,
                 'notes': {'bumps': 'The grey rings are particles bumping into each other in the '
                                    'middle of the box. There are plenty of them, and not one '
                                    'contributes to the pressure — the wall never feels them. '
                                    'Pressure is only ever what arrives at the wall.',
                           'smaller_box': 'Smaller box, same particles, same speed — and the count '
                                          'is up. Nothing about the gas changed; the wall simply '
                                          'moved closer, so each particle gets back to it sooner.',
                           'hot': 'Hot. The count jumps, and notice the reference particle at the '
                                  'bottom left has not changed size by a single pixel. Speed is '
                                  'doing all the work.',
                           'cold': 'Cold. Fewer arrivals per second and each one softer. Cool a '
                                   'sealed can enough and the outside air will crush it, which is '
                                   'the same idea from the other side.',
                           'more_particles': 'More particles, so more of them arriving. This is '
                                             'what you are doing to a tyre when you pump it up — '
                                             'not squashing the air, just putting more of it in.',
                           'resting': 'Twenty-four particles at room temperature. Every orange '
                                      'flash is one collision with a wall, and the number above is '
                                      'how many happened in the last second.'},
                 'alt': {'template': 'A sealed box of gas particles at {temp} temperature, '
                                     'container {vol}, with {n} particles, and a live count of '
                                     'collisions with the walls each second. Wall hits in the last '
                                     'second: {hits}. Pressure: {kpa}.'},
                 'id': 'count-the-hits',
                 'kind': 'collision-counter'},
                {'demand': 'predict',
                 'targets': 'PART-09',
                 'eyebrow': 'Three predictions · then check them on the bench',
                 'heading': 'Say what will happen before you do it',
                 'prompt': 'Each of these changes exactly one thing. Predict the effect on the '
                           'wall-hit count, then go back up and try it.',
                 'shared_options': ['Goes up', 'Stays the same', 'Goes down'],
                 'predictions': [{'id': 'p1',
                                  'question': 'The container is made smaller, and nothing else '
                                              'changes. What happens to the wall hits each second?',
                                  'answer': 0,
                                  'note': 'Up. The particles are travelling no faster, but the '
                                          'walls are closer, so each particle completes the '
                                          'journey between walls more often. Same speed, shorter '
                                          'trip, more arrivals.'},
                                 {'id': 'p2',
                                  'question': 'The gas is heated, and the container stays exactly '
                                              'the same size. What happens to the wall hits each '
                                              'second?',
                                  'answer': 0,
                                  'note': 'Up — and for two reasons at once. Faster particles '
                                          'cross the box more often, and each collision carries '
                                          'more punch. Both push the pressure up.'},
                                 {'id': 'p3',
                                  'question': 'Half the particles are removed, and the temperature '
                                              'and container stay the same. What happens to the '
                                              'wall hits each second?',
                                  'answer': 2,
                                  'note': 'Down, by about half. Each remaining particle behaves '
                                          'exactly as it did — there are simply fewer of them '
                                          'arriving. This is what happens when a tyre leaks.'}],
                 'wrong_note': 'Not quite — go back to the bench and try it before reading on. '
                               'Change only the one thing the question changes.',
                 'id': 'three-predictions',
                 'kind': 'prediction-stack'}],
 'ladder': {'recall': {'title': 'Rung 1 · Recall',
                       'q': 'What causes the pressure of a gas on the walls of its container?',
                       'options': ['Particles pushing against each other',
                                   'Particles colliding with the walls',
                                   'The weight of the gas pressing down',
                                   'The gas trying to escape'],
                       'answer': 1,
                       'feedback': {0: 'Particles do bump into each other, but those bumps are '
                                       'nowhere near the wall and do nothing to it.',
                                    2: 'Pressure acts on the top and sides of a container as much '
                                       'as the bottom. Weight cannot explain that.',
                                    3: 'Particles have no aim. They travel in straight lines until '
                                       'something is in the way.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A sealed metal can of gas is heated. The can does not change size. '
                           'Which of these has NOT changed?',
                      'options': ['The average speed of the particles',
                                  'The size of the particles',
                                  'The number of wall collisions each second',
                                  'The pressure inside the can'],
                      'answer': 1,
                      'feedback': {0: 'Speed is exactly what heating changes.',
                                   2: 'Faster particles reach the wall more often, so this rises.',
                                   3: 'This is what rises, and it is why the warning is on the '
                                      'can.'}},
            'explain': {'title': 'Rung 3 · Explain',
                        'q': 'A bicycle pump is sealed at the end and the handle is pushed halfway '
                             'in. Explain, in terms of particles, why it gets harder and harder to '
                             'push.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The same number of particles…',
                        'success': ['Says the number of particles inside is unchanged.',
                                    'Says the space they are in has been made smaller.',
                                    'Says each particle now reaches a wall more often, because it '
                                    'has less distance to travel.',
                                    'Says more collisions per second on the walls means higher '
                                    'pressure.',
                                    'Says the higher pressure pushes back harder on the handle — '
                                    'the particles are not being squashed themselves.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A car tyre is correctly inflated on a cold morning. After an hour of '
                             'motorway driving, the pressure gauge reads noticeably higher, and no '
                             'air has been added. Explain, and say what a driver should NOT '
                             'conclude from it.',
                        'field_label': 'Your answer',
                        'placeholder': 'Driving heats the tyre because…',
                        'success': ['Says friction with the road and flexing of the rubber heat '
                                    'the air in the tyre.',
                                    'Says the particles move faster when heated.',
                                    'Says faster particles hit the tyre wall more often and '
                                    'harder.',
                                    'Says the number of particles has not changed — no air has '
                                    'been added.',
                                    'Says the driver should not let air out to correct it, because '
                                    'the pressure will fall again as the tyre cools.']}},
 'key_note': 'Pressure = collisions with the wall. Heat it and they come faster and harder. Shrink '
             'it and they come more often. Add particles and there are more of them arriving. '
             'Nothing swells, and particle-to-particle bumps do not count.',
 'stretch': [{'type': 'explainer',
              'id': 'atmospheric-pressure',
              'text': 'You are under pressure right now — about 100,000 pascals of it: the weight '
                      'of the whole depth of the atmosphere above you, which pushes about as hard '
                      'as ten metres of water would, and works out at something like a tonne '
                      'pressing on your shoulders. You cannot feel it because the same pressure is '
                      'pushing out from inside you, and the two balance exactly. Remove one side '
                      'of that balance and it becomes obvious immediately: a sealed plastic bottle '
                      'brought down a mountain crumples on its own, and a suction cup holds a '
                      'shelf up using nothing but the air that is not inside it. Nothing sucks, '
                      'ever. Things get pushed, by particles, from the side where there are more '
                      'of them.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still picturing pressure as particles pushing each other?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
