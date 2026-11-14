# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C1 `particle-model` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C1'
SOURCE_SLUG = 'particle-model'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'particle-model',
 'title': 'The particle model',
 'discipline': 'chemistry',
 'unit': 'particles-and-their-behaviour',
 'family': 'MODEL',
 'covers': ['KS3.C.PNM.01a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'particles', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 35,
 'requires': [],
 'assumes': [],
 'references': ['solids-liquids-and-gases'],
 'connects_heading': 'Next in this unit',
 'ks4_links': ['chemistry/bonding/states-of-matter'],
 'big_question': '50 ml of water and 50 ml of alcohol make 97 ml, every time. What does that tell '
                 'us about liquids?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': '50 + 50 = 97', 'done_when': 'committed'},
          {'anchor': 's-cut',
           'short': 'CUT',
           'label': 'Keep cutting',
           'done_when': 'floor_reached'},
          {'anchor': 's-gap',
           'short': 'GAP',
           'label': 'What is in the gap',
           'done_when': 'one_test_run'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'A sharper knife',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'demo',
                'title': 'Fifty and fifty makes ninety-seven.',
                'prompt': 'Two measuring cylinders, both read to the millilitre. 50 ml of water, '
                          '50 ml of pure alcohol. Tip one into the other, wait for the froth to '
                          'settle and read the level: 97 ml. Do it again tomorrow and you get 97 '
                          'ml again.',
                'commit': 'If you had to guess, where did the missing 3 ml go?',
                'options': ['It evaporated away', 'It squeezed into gaps'],
                'reveal': 'That idea, that matter is made of separate particles with gaps, is the '
                          'whole model. Next: try to break it by cutting a sugar cube in half, '
                          'again and again.',
                'guess': True,
                'replies': ['Some alcohol does evaporate, but nowhere near 3 ml, and you get 97 '
                            'every time. The liquid is all still there, tucked into gaps.',
                            'Nothing is lost. Every drop is still in the cylinder. Liquids are not '
                            'solid all the way through, so the small bits of one settle into gaps '
                            'between the big bits of the other.'],
                'answer': 1},
 'misconceptions': [{'id': 'PART-01',
                     'statement': 'You stopped cutting because the knife was not sharp enough. A '
                                  'better knife would keep going.',
                     'elicited_by': 'cut-bench',
                     'confronted_by': 'think-commit-knife'},
                    {'id': 'PART-02',
                     'statement': 'There is air (or dust, or something) in the gaps between '
                                  'particles.',
                     'elicited_by': 'gap-rig',
                     'confronted_by': 'gap-rig'}],
 'vocabulary': [{'term': 'particle',
                 'definition': 'One of the tiny pieces that all matter is made from, far too small '
                               'to see.',
                 'note': "In this unit 'particle' means atoms or molecules. You will meet those "
                         'names properly in C2.'},
                {'term': 'matter',
                 'definition': 'Anything that has mass and takes up space.',
                 'note': None},
                {'term': 'model',
                 'definition': 'A simple picture or idea that helps explain something we cannot '
                               'see directly.',
                 'note': 'A model does not have to be a perfect copy to be useful. L6 asks how far '
                         'this one can be pushed.'},
                {'term': 'continuous',
                 'definition': 'All one piece, with no gaps and no separate bits, however closely '
                               'you look.',
                 'note': 'This is the idea the particle model replaces. Matter looks continuous; '
                         'it is not.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Everything in this unit rests on one claim: matter is not continuous. It is '
                   'made of separate particles, far too small to see, with nothing at all in '
                   'between them, and they never stop moving. That claim is worth nothing to you '
                   'until you have tried to break it — so the rest of this lesson is two attempts '
                   'to break it.'},
          {'type': 'check', 'id': 'cut-bench', 'anchor': 's-cut'},
          {'type': 'key-fact', 'ref': 'nothing-between'},
          {'type': 'practical', 'id': 'gap-rig', 'anchor': 's-gap'},
          {'type': 'misconception',
           'id': 'think-commit-knife',
           'anchor': 's-think',
           'targets': 'PART-01'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'nothing-between',
                'text': 'All matter is made of particles, far too small to see, with nothing '
                        'between them, and they are always moving.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-knife',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'PART-01',
                 'prompt': 'This is the sensible objection, and it is worth taking seriously '
                           'before you answer it. Commit.',
                 'options': ['True — a sharper knife would just keep going',
                             'The knife could cut it, but what comes out is not sugar any more',
                             'False — particles cannot be cut by anything',
                             'The piece would be too small for the knife to touch'],
                 'reveal': ['A sharper knife does not help, because past this point you are not '
                            'cutting any more. Splitting a sugar particle takes it apart into '
                            'different substances altogether — that is a chemical change, not a '
                            'smaller slice. Cutting has a floor, and this is it: what is '
                            'impossible is a smaller piece <em>that is still sugar</em>.',
                            'That is what the model claims, and it is a much stronger claim than '
                            '"things are small". It says matter comes in units with a floor, and '
                            'below that floor the substance stops existing. Everything you meet in '
                            'this unit — melting, pressure, diffusion — is that floor doing '
                            'work.']},
                {'eyebrow': 'The cutting bench · attempt one',
                 'heading': 'Keep cutting it in half.',
                 'head_counter': {'format': '{n} of {total} possible cuts', 'total': 24},
                 'progress_full': 'floor reached',
                 'prompt': 'A sugar cube, one centimetre on each side. A knife with a perfect '
                           'edge, and no limit on your patience. Halve it across, throw the rest '
                           'away, then halve what is left again — every cut leaves a piece half as '
                           'wide as the one before.',
                 'floor': 24,
                 'start_cm': 1,
                 'grain_at': 4,
                 'gate': {'prompt': 'Commit before you start. With a perfect knife and forever to '
                                    'work, how many times could you cut?',
                          'options': ['Forever — there is always a smaller half',
                                      'Millions of times, then the piece is too small to see',
                                      'A few dozen times, then no smaller piece of sugar exists',
                                      'Until it turns into a liquid']},
                 'readouts': [{'label': 'Cuts made', 'source': 'count'},
                              {'label': 'Edge of the piece', 'source': 'size'},
                              {'label': 'Still sugar?', 'source': 'verdict'}],
                 'verdict': {'open': 'Yes', 'floor': 'Floor'},
                 'buttons': [{'label': 'Cut it in half',
                              'action': 'cut',
                              'step': 1,
                              'disabled_when': 'at_floor'},
                             {'label': 'Undo a cut',
                              'action': 'undo',
                              'step': 1,
                              'disabled_when': 'at_start'},
                             {'label': 'Cut ten more times',
                              'action': 'cut',
                              'step': 10,
                              'disabled_when': 'at_floor'}],
                 'notes': {'at_floor': 'Twenty-four cuts. Not twenty-four thousand, not forever — '
                                       'twenty-four. The knife has not gone blunt and your hand '
                                       'has not got tired. There is simply no piece of sugar '
                                       'smaller than this one, because this one is a single '
                                       'particle, and halving matter runs out. 0.6 nm is about a '
                                       'millionth of a millimetre: a human hair is a hundred '
                                       'thousand times wider.',
                           'near_floor': 'The edge has stopped being smooth. What looked like a '
                                         'solid block four cuts ago is a countable number of '
                                         'particles, and you can see the end coming.',
                           'at_start': 'A centimetre of sugar. Cut it and watch it go — the size '
                                       'on the ruler and the piece on the bench are the same '
                                       'claim.',
                           'mid': 'Still sugar, still sweet, still white, still behaving exactly '
                                  'like sugar. Halving does not seem to be getting you anywhere. '
                                  'Keep going.'},
                 'alt': {'template': 'A piece of sugar after {n} halvings, {size} across{tail}',
                         'smooth': ', still a smooth solid block.',
                         'grainy': ', now visibly made of separate round particles.'},
                 'canvas_labels': {'ghost': 'the piece before this cut',
                                   'one': 'ONE PARTICLE',
                                   'many': '{n} PARTICLES LEFT',
                                   'start': 'CUT 0',
                                   'end': 'CUT {floor}',
                                   'zoom': 'ZOOMED IN ×{n}'},
                 'id': 'cut-bench',
                 'kind': 'halving-bench',
                 'demand': 'investigate'},
                {'eyebrow': 'Attempt two · the gap',
                 'heading': 'What is between the particles?',
                 'prompt': 'Zoom into the sugar until you can see individual particles with spaces '
                           'between them. Pick what is in the space, then run the test that would '
                           'tell them apart.',
                 'choices': ['Air',
                             'A gas we have not discovered yet',
                             'Dust and moisture, too small to see',
                             'Nothing at all'],
                 'empty_choice': 3,
                 'caption': 'Take the gap away and see what happens',
                 'tests': [{'id': 'squash',
                            'label': 'Squash the gas',
                            'on': 'With gaps: the particles are pushed closer and the gas takes up '
                                  'a fifth of the space. That is why a bike pump works.',
                            'off': 'Fill the gaps with air and there is nothing left to squash — '
                                   'the air would need gaps of its own, and so would that air, '
                                   'forever.'},
                           {'id': 'mix',
                            'label': 'Pour the water in',
                            'on': 'With gaps: small particles drop into the spaces between large '
                                  'ones, and 50 + 50 comes out at 97.',
                            'off': 'Fill the gaps with something and the volumes must simply add. '
                                   '50 and 50 would make 100, and it does not.'},
                           {'id': 'smell',
                            'label': 'Let the smell spread',
                            'on': 'With gaps: a moving particle has somewhere to go, and it works '
                                  'its way across the room without any draught.',
                            'off': 'Pack the space solid and nothing can move anywhere. A smell '
                                   'would never cross a still room, and it does.'}],
                 'notes': {'empty': 'Nothing is the hard answer to accept and the only one that '
                                    'survives. Run a test and see why the alternatives do not.',
                           'filled': 'You have put something in the gap. Now run a test and watch '
                                     'it fail.'},
                 'canvas_labels': {'empty': 'GAPS EMPTY',
                                   'filled': 'GAPS FILLED IN',
                                   'foot_filled': 'your answer, on the right',
                                   'foot_empty': 'your answer says nothing is there — both boxes '
                                                 'agree'},
                 'alt': {'template': 'Two particle boxes side by side. Left: particles with empty '
                                     'space between them. Right: {right}',
                         'filled': 'the same particles with the space packed solid.',
                         'empty': 'the same picture, because the answer was that nothing is '
                                  'there.'},
                 'id': 'gap-rig',
                 'kind': 'gap-test-rig',
                 'demand': 'investigate'}],
 'ladder': {'recall': {'q': 'What does the particle model say is between the particles of a gas?',
                       'options': ['Nothing at all',
                                   'Air',
                                   'A very thin gas',
                                   'Dust too small to see'],
                       'answer': 0,
                       'feedback': {1: 'Air is itself a gas made of particles. Saying the gaps are '
                                       'full of air just asks the same question one layer down.',
                                    2: 'Same problem: that gas would have gaps too, and you would '
                                       'never finish.',
                                    3: 'Dust is matter, made of particles, with gaps of its own. '
                                       'Nothing is nothing.'}},
            'apply': {'q': 'A student halves a sugar cube twenty-four times, each cut leaving a '
                           'piece half as wide, and reaches one particle. Why can they not make '
                           'the twenty-fifth cut?',
                      'options': ['No knife is thin enough to fit',
                                  'Particles are too hard to cut',
                                  'They can cut it, but what comes out is no longer sugar',
                                  'The piece is too small to see, so the cut cannot be aimed'],
                      'answer': 2,
                      'feedback': {0: 'A sharp enough tool can split a particle. The limit is not '
                                      'mechanical.',
                                   1: 'Hardness is a property of a large lump of a substance, not '
                                      'of one particle.',
                                   3: 'Difficulty in aiming is a practical problem. The model '
                                      'makes a stronger claim than that.'}},
            'explain': {'q': 'Explain, using the particle model, why 50 ml of water added to 50 ml '
                             'of alcohol gives 97 ml and not 100 ml.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Both liquids are made of…',
                        'success': ['Says both liquids are made of particles with gaps between '
                                    'them.',
                                    'Says the particles of the two liquids are different sizes.',
                                    'Says the smaller particles fit into the gaps between the '
                                    'larger ones.',
                                    'Says no particles are lost or destroyed — the total amount of '
                                    'matter is unchanged.',
                                    'Says the volume drops because the particles pack more '
                                    'closely, not because anything disappears.']},
            'produce': {'q': 'A student says the gaps between particles in a gas must contain air, '
                             '"because otherwise it would be a vacuum in there, and you cannot '
                             'have a vacuum in the middle of a room." Reply to them.',
                        'field_label': 'Your reply',
                        'placeholder': 'If the gaps were full of air…',
                        'success': ['Points out that air is itself made of particles.',
                                    'Says that filling the gaps with air only pushes the same '
                                    'question down a level, and never ends.',
                                    'Says the gaps genuinely contain nothing.',
                                    'Uses evidence: a gas can be squashed, which would be '
                                    'impossible if the space were already full.',
                                    'Notes that this is not a vacuum you could stand in — each '
                                    "empty space is far too small for anything to be 'in', "
                                    'millions of times thinner than a hair.']}},
 'key_note': 'Matter is made of particles with a floor you cannot cut past, nothing at all between '
             'them, and constant motion. Three claims. You have tested two of them in this lesson '
             'and the third is the next five lessons.',
 'stretch': [{'type': 'explainer',
              'id': 'democritus',
              'text': 'The Greeks got here by argument alone, around 400 BC — Democritus reasoned '
                      'that cutting must stop somewhere and called the last piece <em>atomos</em>, '
                      'uncuttable. He had no evidence, and for two thousand years his idea sat '
                      'next to the equally reasonable one that matter is continuous, with nothing '
                      'to choose between them. What broke the tie was not a better argument but a '
                      'measurement: gases combining in fixed whole-number ratios, mass balancing '
                      'exactly through a reaction, and eventually the water-and-alcohol arithmetic '
                      'you did at the top of this page. An idea does not become science when '
                      'someone thinks of it. It becomes science when a number forces it.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still think something must be in the gap?',
           'cta': 'Ask about this lesson',
           'anchor': 's-gap'},
 'before_this': 'Nothing — this is where the unit starts',
 'ks4_becomes': 'The kinetic theory of matter, ionic and covalent structure, and the limits of the '
                'simple particle picture.',
 'ws': ['scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
