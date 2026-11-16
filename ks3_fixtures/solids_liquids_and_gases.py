# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C1 `solids-liquids-and-gases` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C1'
SOURCE_SLUG = 'solids-liquids-and-gases'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'solids-liquids-and-gases',
 'title': 'Solids, liquids and gases',
 'discipline': 'chemistry',
 'unit': 'particles-and-their-behaviour',
 'family': 'CONTRAST',
 'covers': ['KS3.C.PNM.01b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'particles', 'level': 1}, {'id': 'structure-function', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': ['particle-model'],
 'assumes': [],
 'references': ['changes-of-state'],
 'connects_heading': 'Next in this unit',
 'ks4_links': ['chemistry/bonding/states-of-matter'],
 'big_question': 'Ice, water and steam are the same substance. So what exactly is different about '
                 'them?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'The long bridge',
           'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'State bench',
           'done_when': 'all_three_states_seen'},
          {'anchor': 's-matrix',
           'short': 'TABLE',
           'label': 'The contrast',
           'mirrors': 's-bench',
           'done_when': 'all_three_states_seen'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Softening particles',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A steel girder on a hot day.',
                'prompt': 'A bridge is longer in August than in January — by centimetres, enough '
                          'that bridges are built with gaps to swallow it. The steel gains nothing '
                          'and loses nothing. The same iron particles are there in both months, '
                          'and there are exactly as many of them.',
                'commit': 'If you had to guess, when steel expands in the heat, what gets bigger?',
                'options': ['Each particle swells up', 'The gaps between them'],
                'reveal': 'Same particles, different spacing and movement: that is the idea behind '
                          'every state. Next: watch one substance as a solid, a liquid and a gas.',
                'guess': True,
                'replies': ['Swelling is the natural thing to picture, but the particles stay '
                            'exactly the same size. It is the gaps between them that grow.',
                            'Heat makes the particles jiggle harder, so each needs more room and '
                            'the gaps grow. The particles themselves stay exactly the same size.'],
                'answer': 1},
 'misconceptions': [{'id': 'PART-03',
                     'statement': 'The particles themselves change — they melt, or get softer, or '
                                  'expand — when a substance changes state.',
                     'elicited_by': 'same-particles-reveal',
                     'confronted_by': 'same-particles-reveal'},
                    {'id': 'PART-04',
                     'statement': 'Particles in a solid are completely still.',
                     'elicited_by': 'state-bench',
                     'confronted_by': 'state-bench'}],
 'vocabulary': [{'term': 'solid',
                 'definition': 'A state of matter that keeps its own shape and cannot be squashed '
                               'much.',
                 'note': None},
                {'term': 'liquid',
                 'definition': 'A state of matter that takes the shape of its container but keeps '
                               'the same volume.',
                 'note': None},
                {'term': 'gas',
                 'definition': 'A state of matter that spreads out to fill its whole container.',
                 'note': "'Gas' is a state. 'Air' is a particular mixture of gases — they are not "
                         'the same word.'},
                {'term': 'vibrate',
                 'definition': 'To move quickly back and forth about a fixed position.',
                 'note': None},
                {'term': 'state',
                 'definition': 'One of the forms a substance can take. Solid, liquid and gas are '
                               'the three you meet in this unit.',
                 'note': 'Ice, water and steam are one substance in three states — the particles '
                         'are identical in all three.'}],
 'figures': [{'id': 'c1-particle-states',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'particle-states',
              'title': 'Solid, liquid and gas, each drawn as a box of particles, with a reference '
                       'particle beside every box',
              'desc': "Three boxes side by side, labelled Solid, Liquid and Gas. The solid's box "
                      'holds sixteen particles in a tight, regular grid, each one touching its '
                      "neighbours. The liquid's box holds fifteen particles, still close together "
                      "but arranged unevenly rather than in a grid. The gas's box holds eight "
                      'particles, scattered with wide gaps between them and none touching. Beneath '
                      "each box sits one more particle on its own, captioned 'one particle, actual "
                      "size'.",
              'caption': 'One substance, three states. Compare the particles inside each box with '
                         'the reference particle underneath it.',
              'data': {'states': [{'id': 'solid', 'kind': 'solid', 'label': 'Solid'},
                                  {'id': 'liquid', 'kind': 'liquid', 'label': 'Liquid'},
                                  {'id': 'gas', 'kind': 'gas', 'label': 'Gas'}]}}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Three states, one substance. The particles do not change — not their size, not '
                   'their mass, not what they are. What changes is how close together they sit and '
                   'how much they move. Every difference you can see and feel between ice, water '
                   'and steam comes out of those two things.'},
          {'type': 'check', 'id': 'state-bench', 'anchor': 's-bench'},
          {'type': 'check', 'id': 'contrast-matrix', 'anchor': 's-matrix'},
          {'type': 'key-fact', 'ref': 'state-is-arrangement'},
          {'type': 'figure', 'ref': 'c1-particle-states', 'anchor': 's-particle-states'},
          {'type': 'misconception',
           'id': 'same-particles-reveal',
           'anchor': 's-think',
           'targets': 'PART-03'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'state-is-arrangement',
                'text': 'The state of a substance is set by how its particles are arranged and how '
                        'fast they move — never by any change in the particles themselves.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'same-particles-reveal',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'PART-03',
                 'statements': ['When ice melts, the particles go soft and squash into the new '
                                'shape.'],
                 'prompt': 'This is the most common wrong idea in the whole of KS3 physical '
                           'science, and it is worth catching now, because it will follow you into '
                           'pressure, expansion and density. Commit before you read on.',
                 'options': ['True — that is what melting is',
                             'The particles stay identical; only their spacing and movement change',
                             'The particles get smaller so they can fit the new shape',
                             'Some particles break apart to make room'],
                 'reveal': ['A water particle in ice and a water particle in steam are identical. '
                            'Same size, same mass, same three atoms joined the same way. Melting '
                            'does not soften anything and boiling does not stretch anything.',
                            'Test it against the bridge: the girder gets longer, and no one thinks '
                            'the iron atoms inflate. What changes is always the spacing and the '
                            'speed. <em>Soft</em>, <em>runny</em> and <em>squashy</em> are words '
                            'about a crowd of particles, never about one.']},
                {'demand': 'investigate',
                 'eyebrow': 'The state bench · watch one substance',
                 'heading': 'Same particles. Three arrangements.',
                 'head_counter': {'format': '{n} of 3 states seen', 'total': 3, 'start': 0},
                 'progress_full': 'all three seen',
                 'gate': {'prompt': 'Commit first. In a block of ice sitting in a freezer, what '
                                    'are the particles doing?',
                          'options': ['Nothing — they are completely still',
                                      'Vibrating on the spot without moving anywhere',
                                      'Sliding slowly past each other',
                                      'Moving freely, just very slowly']},
                 'states': [{'key': 'solid',
                             'label': 'Solid',
                             'alt': 'A particle box showing the solid state: particles in regular '
                                    'rows, vibrating in place.'},
                            {'key': 'liquid',
                             'label': 'Liquid',
                             'alt': 'A particle box showing the liquid state: particles touching '
                                    'but jumbled, sliding past each other below a surface line.'},
                            {'key': 'gas',
                             'label': 'Gas',
                             'alt': 'A particle box showing the gas state: widely separated '
                                    'particles moving fast in all directions.'}],
                 'groups': {'states': 'State', 'instruments': 'Instruments'},
                 'controls': {'motion': {'running': 'Freeze the motion',
                                         'frozen': 'Start the motion'},
                              'trails': {'shown': 'Hide the paths', 'hidden': 'Show the paths'},
                              'squash': {'label': 'Try to squash it'}},
                 'squash_banner': {'gas': 'PISTON PUSHED IN — IT GAVE WAY',
                                   'other': 'PISTON PUSHED HARD — IT BARELY MOVED'},
                 'reference_particle': 'ONE PARTICLE, ACTUAL SIZE — THE SAME IN ALL THREE STATES',
                 'notes': {'squash': {'gas': 'The gas gave way immediately, because most of a gas '
                                             'is empty space and squashing it just removes some of '
                                             'that space. The particles did not get smaller — they '
                                             'got closer.',
                                      'other': 'Barely a millimetre. The particles are already '
                                               'touching, so there is no space left to remove, and '
                                               'pushing harder only pushes particle against '
                                               'particle. This is why you can compress air in a '
                                               'syringe and not water.'},
                           'trails': {'solid': 'Every particle has a home position and never '
                                               'leaves it. The trails are tiny circles — that is '
                                               'vibration, not travel, and it is why a solid keeps '
                                               'its shape.',
                                      'liquid': 'The trails wander. Particles change neighbours '
                                                'constantly but stay in contact, which is exactly '
                                                'what pouring looks like from the inside.',
                                      'gas': 'Long straight runs between collisions. Nothing '
                                             'steers a gas particle; it goes until it hits '
                                             'something.'},
                           'rest': {'solid': 'A solid is not still. Every particle is vibrating '
                                             'about a fixed point — switch the motion off and on '
                                             'and watch the difference between vibrating and '
                                             'travelling.',
                                    'liquid': 'The particles are still touching, exactly as in the '
                                              'solid, but the neat rows have gone. Same crowding, '
                                              'no order: that is the entire difference between a '
                                              'solid and a liquid.',
                                    'gas': 'Almost all of this box is empty. That emptiness is '
                                           'what lets you squash a gas, and nothing else about it '
                                           'has changed.'}},
                 'id': 'state-bench',
                 'kind': 'state-bench'},
                {'demand': 'compare',
                 'eyebrow': 'The contrast, in one table',
                 'heading': 'What each arrangement forces to be true',
                 'prompt': 'Nothing in this table is a fact to memorise separately. Every row is a '
                           'consequence of the two rows above it.',
                 'columns': ['Property', 'Solid', 'Liquid', 'Gas'],
                 'rows': [{'key': 'arrangement',
                           'label': 'Arrangement',
                           'solid': 'Regular rows, all touching',
                           'liquid': 'Touching, but jumbled',
                           'gas': 'Far apart, random'},
                          {'key': 'movement',
                           'label': 'Movement',
                           'solid': 'Vibrating on the spot',
                           'liquid': 'Sliding over each other',
                           'gas': 'Fast, in all directions'},
                          {'key': 'shape',
                           'label': 'Shape',
                           'solid': 'Keeps its own',
                           'liquid': 'Takes the container’s',
                           'gas': 'Fills the container'},
                          {'key': 'volume',
                           'label': 'Volume',
                           'solid': 'Fixed',
                           'liquid': 'Fixed',
                           'gas': 'Fills whatever it is given'},
                          {'key': 'squash',
                           'label': 'Can it be squashed?',
                           'solid': 'Almost not at all',
                           'liquid': 'Almost not at all',
                           'gas': 'Easily'},
                          {'key': 'pour',
                           'label': 'Can it be poured?',
                           'solid': 'No',
                           'liquid': 'Yes',
                           'gas': 'It escapes instead'}],
                 'highlight_from': 's-bench',
                 'highlight': {'squash': 'squash', 'trails': 'movement', 'rest': 'arrangement'},
                 'footnote': 'The highlighted row is the one your current bench setting is '
                             'showing.',
                 'id': 'contrast-matrix',
                 'kind': 'state-matrix'}],
 'ladder': {'recall': {'title': 'Rung 1 · Recall',
                       'q': 'Which state has particles that are close together but not in a '
                            'regular pattern?',
                       'options': ['Solid', 'Gas', 'All three are equally spaced', 'Liquid'],
                       'answer': 3,
                       'feedback': {0: 'A solid is close together and regular. It is the pattern '
                                       'that makes it a solid.',
                                    1: 'A gas is not close together at all — the particles are '
                                       'mostly far apart.',
                                    2: 'The whole point of the three states is that spacing '
                                       'differs.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A gas can be squashed into a fifth of its volume. A liquid hardly '
                           'squashes at all. Why not?',
                      'options': ['Liquid particles are much harder than gas particles, so they '
                                  'resist being pressed together',
                                  'Liquid particles are bigger, so they take up all the room in '
                                  'the container',
                                  'Liquids are heavier than gases, so they push back harder '
                                  'against the squash',
                                  'A liquid’s particles are already touching, so there is no space '
                                  'to squash out'],
                      'answer': 3,
                      'feedback': {0: 'They are the same particles. Water vapour and water are '
                                      'made of identical things.',
                                   1: 'Size does not change with state — that is the misconception '
                                      'this lesson exists to kill.',
                                   2: 'Weight is not what resists the squash. Space is.'}},
            'explain': {'title': 'Rung 3 · Explain',
                        'q': 'A gas fills any container it is put in; a liquid of the same amount '
                             'sits in a puddle at the bottom. Explain both, using the arrangement '
                             'and movement of the particles.',
                        'field_label': 'Your explanation',
                        'placeholder': 'In a gas the particles…',
                        'success': ['Says gas particles are far apart with large spaces between '
                                    'them.',
                                    'Says gas particles move fast in random directions.',
                                    'Says nothing holds gas particles together, so they spread '
                                    'until the walls stop them.',
                                    'Says liquid particles are touching and attracted to each '
                                    'other, so they stay as one body.',
                                    'Says liquid particles can still slide past each other, which '
                                    'is why the puddle takes the shape of the floor.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A steel railway rail is 30 m long in winter and about 1 cm longer on '
                             'a hot summer day. Explain what has happened to the particles, and '
                             'say clearly what has NOT happened.',
                        'field_label': 'Your answer',
                        'placeholder': 'Heating the rail gives the particles…',
                        'success': ['Says heating gives the particles more energy so they vibrate '
                                    'faster or further.',
                                    'Says the average spacing between the particles increases.',
                                    'Says the number of particles is unchanged.',
                                    'States explicitly that the particles themselves have NOT got '
                                    'bigger.',
                                    'Says the steel is still a solid — the particles are still in '
                                    'fixed positions, just further apart.']}},
 'key_note': 'Solid: touching, ordered, vibrating in place. Liquid: touching, disordered, sliding '
             'past each other. Gas: far apart, disordered, moving fast and freely. The particles '
             'are identical in all three.',
 'stretch': [{'type': 'explainer',
              'id': 'edges-of-three-states',
              'text': 'Three states is a school simplification, and a good one — it covers almost '
                      'everything you will meet. But glass is a genuine embarrassment to it: it '
                      'holds its shape like a solid while its particles sit in the jumbled '
                      'arrangement of a liquid, so it is neither, and arguments about which box it '
                      'belongs in have been running for a century. Liquid crystals, the material '
                      'in the screen you may be reading this on, flow like a liquid while staying '
                      'lined up like a solid. And most of the matter in the universe is in a '
                      'fourth state, plasma, which is what stars are made of. None of this makes '
                      'the three-state model wrong. It makes it a model, with edges, exactly like '
                      "Dalton's will turn out to be."}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Not sure why a solid vibrates but does not move?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'ws': ['experimental-skills-and-investigations'],
 'review_state': 'draft',
 'authored': True}
