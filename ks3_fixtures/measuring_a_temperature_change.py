# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C7 `measuring-a-temperature-change` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C7'
SOURCE_SLUG = 'measuring-a-temperature-change'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'measuring-a-temperature-change',
 'title': 'Measuring a temperature change',
 'discipline': 'chemistry',
 'unit': 'energy-changes-in-reactions',
 'family': 'INVESTIGATION',
 'covers': ['KS3.C.ENER.02c'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'energy', 'level': 3}, {'id': 'measurement-and-evidence', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['endothermic-reactions'],
 'assumes': [],
 'references': ['neutralisation', 'exothermic-reactions'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Four groups run the same reaction and get four different answers. One of them is '
                 'closest to right — and it is not the one with the neatest handwriting.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Four answers', 'done_when': 'committed'},
          {'anchor': 's-plan',
           'short': 'PLAN',
           'label': 'Judge the plan',
           'done_when': 'all_five_ruled_on'},
          {'anchor': 's-bench',
           'short': 'RIG',
           'label': 'Build the rig',
           'done_when': 'three_rigs_run'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'What averaging fixes',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Same acid, same alkali, same volumes, same room. Four groups report +5, '
                         '+7, +2 and +7 °C.',
                'prompt': 'Nobody made anything up. All four wrote down what their thermometer '
                          'said. The reaction cannot have released a different amount of energy in '
                          'four beakers on the same bench.',
                'commit': 'If you had to guess, what mainly caused the different answers?',
                'options': ['Heat escaping to the room', 'The thermometers being unreliable'],
                'reveal': 'So the skill is in the set-up as well as in the reading.',
                'guess': True,
                'replies': ['A beaker is always leaking heat to the bench and the air, so the '
                            'later and slower the reading, the more has already escaped.',
                            'Thermometers can be a little off, but not by five degrees. What '
                            'really differed was how long each beaker was losing heat before it '
                            'was read.'],
                'answer': 0},
 'misconceptions': [{'id': 'ENER-07',
                     'statement': 'Repeating an experiment and averaging makes the result '
                                  'accurate.',
                     'elicited_by': 'think-commit-average',
                     'confronted_by': 'think-commit-average'},
                    {'id': 'ENER-08',
                     'statement': 'Results that agree closely with each other must be correct.',
                     'elicited_by': 'rig-build',
                     'confronted_by': 'rig-close'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Energy change is measured by measuring temperature — and a temperature reading '
                   'is only as good as the arrangement around it. Heat leaks out of an open '
                   'beaker, into the bench, and into the thermometer itself.'},
          {'type': 'explainer',
           'text': 'This lesson is about the decisions that decide whether your number means '
                   'anything: what to measure, what to keep the same, and what to insulate '
                   'against.'},
          {'type': 'check', 'id': 'plan-judge', 'anchor': 's-plan'},
          {'type': 'check', 'id': 'rig-build', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'start-peak-difference'},
          {'type': 'keyword',
           'anchor': 's-words',
           'eyebrow': 'Five words',
           'lead': 'Say your answer out loud before you turn each card over. If you cannot say it, '
                   'you do not know it yet.',
           'terms': ['Temperature change',
                     'Insulation',
                     'Peak temperature',
                     'Systematic error',
                     'Random error']},
          {'type': 'misconception',
           'id': 'think-commit-average',
           'anchor': 's-think',
           'targets': 'ENER-07'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'start-peak-difference',
                'text': 'Measure the start temperature, the highest or lowest reading, and take '
                        'the difference. Insulate, use a lid, and read quickly — every escape of '
                        'heat makes the measured change too small.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-average',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ENER-07',
                 'prompt': 'Repeating and averaging is genuinely good practice. Commit before you '
                           'read on.',
                 'options': ['Right — averaging three results is what makes a measurement accurate '
                             'rather than lucky',
                             'Wrong — averaging fixes random scatter, not an error that always '
                             'runs one way',
                             'Right, because more data is always better and three runs beat one '
                             'every time',
                             'Wrong — repeating an experiment tells you nothing you did not '
                             'already know'],
                 'reveal': ['Averaging fixes <strong>random</strong> error — the scatter from '
                            'reading a scale slightly differently each time, or stirring a bit '
                            'harder. Those errors fall on both sides of the truth, so they cancel '
                            'out.',
                            'Heat loss is not like that. It makes every single reading too low, so '
                            'the average of three low readings is a low average. <strong>An error '
                            'that always points the same way survives any number of '
                            'repeats.</strong> The only cure is to change the apparatus — which is '
                            'why the lid matters more than the third run.']},
                {'eyebrow': "Before you run it · judge someone else's plan",
                 'heading': 'A student has written a method. Five decisions. Rule on each.',
                 'demand': 'evaluate',
                 'head_counter': {'format': '{n} of {total} ruled on', 'start': 0, 'total': 5},
                 'prompt': 'Two of the five are sound, two are flawed, and one would wreck the '
                           'result on its own.',
                 'sound_claim': 2,
                 'flawed_claim': 2,
                 'fatal_claim': 1,
                 'options': [{'id': 'ok', 'label': 'Sound'}, {'id': 'bad', 'label': 'Flawed'}],
                 'steps': [{'id': 'p1',
                            'tag': 'Step 1',
                            'sound': False,
                            'fatal': False,
                            'step': 'Measure 25 cm³ of acid into a glass beaker.',
                            'verdict': 'Flawed — sound as far as it goes, but the glass beaker is '
                                       'the weak point.',
                            'why': 'Glass conducts heat away into the bench and the air, and it '
                                   'absorbs a share of the energy warming itself up. A polystyrene '
                                   'cup does neither, and costs less.'},
                           {'id': 'p2',
                            'tag': 'Step 2',
                            'sound': True,
                            'fatal': False,
                            'step': 'Take the temperature of the acid before adding anything.',
                            'verdict': 'Sound — essential, in fact, and easy to skip.',
                            'why': 'Without a starting value there is no change to calculate — '
                                   'only a final number that means nothing on its own. It should '
                                   'be recorded, not remembered.'},
                           {'id': 'p3',
                            'tag': 'Step 3',
                            'sound': False,
                            'fatal': True,
                            'step': 'Add the alkali, then go and write up the method while it '
                                    'reacts.',
                            'verdict': 'Flawed, and this is the one that ruins the experiment.',
                            'why': 'The peak temperature arrives within seconds and then falls as '
                                   'heat escapes to the room. Come back two minutes later and you '
                                   'record a number that is mostly a measure of how long you were '
                                   'away.'},
                           {'id': 'p4',
                            'tag': 'Step 4',
                            'sound': False,
                            'fatal': False,
                            'step': 'Stir with the thermometer.',
                            'verdict': 'Flawed — stirring is right, stirring with the thermometer '
                                       'is not.',
                            'why': 'Without stirring the thermometer reads one warm pocket rather '
                                   'than the mixture. But it is a fragile instrument, and a broken '
                                   'one in a beaker of acid is a genuine incident. Use a stirring '
                                   'rod.'},
                           {'id': 'p5',
                            'tag': 'Step 5',
                            'sound': True,
                            'fatal': False,
                            'step': 'Record the highest temperature reached, and subtract the '
                                    'starting temperature.',
                            'verdict': 'Sound, and the right quantity to record.',
                            'why': 'The peak is the closest the apparatus gets to the true value, '
                                   'because from that moment on heat loss is winning. Subtracting '
                                   'gives the temperature change, which is what the energy '
                                   'transfer is judged by.'}],
                 'id': 'plan-judge',
                 'kind': 'rig-plan-critique'},
                {'eyebrow': 'Your turn · build the apparatus',
                 'heading': 'Three choices, then run it and see what your setup was worth.',
                 'demand': 'investigate',
                 'prompt': 'The true temperature rise for this reaction is 7.0 °C. Your reading '
                           'will be lower than that by however much heat your apparatus lets '
                           'escape. Both that value and the eight readings are illustrative '
                           'figures chosen to show what heat loss does, not measurements from one '
                           'afternoon.',
                 'dials': [{'id': 'vessel',
                            'label': 'The container',
                            'options': [{'id': 'beaker',
                                         'label': 'Glass beaker',
                                         'phrase': 'Glass beaker'},
                                        {'id': 'cup',
                                         'label': 'Polystyrene cup',
                                         'phrase': 'Polystyrene cup'}]},
                           {'id': 'cover',
                            'label': 'The top',
                            'options': [{'id': 'open',
                                         'label': 'Open',
                                         'phrase': 'open to the room'},
                                        {'id': 'lid',
                                         'label': 'Lid with a hole',
                                         'phrase': 'lid fitted'}]},
                           {'id': 'speed',
                            'label': 'When you read it',
                            'options': [{'id': 'slow',
                                         'label': 'After two minutes',
                                         'phrase': 'read after two minutes'},
                                        {'id': 'fast',
                                         'label': 'At the peak',
                                         'phrase': 'read at the peak'}]}],
                 'rigs': [{'id': 'beaker|open|slow',
                           'v': 2.1,
                           'why': 'A glass beaker, open to the room, read two minutes late. Almost '
                                  'two-thirds of the rise has leaked away before anyone looked at '
                                  'the thermometer. This is the group that reported +2 °C.'},
                          {'id': 'beaker|open|fast',
                           'v': 4.9,
                           'why': 'Reading promptly saved a great deal — but an open glass beaker '
                                  'still loses heat upwards and into the bench the whole time.'},
                          {'id': 'beaker|lid|slow',
                           'v': 3.4,
                           'why': 'The lid helps, and then two minutes of waiting throws the '
                                  'benefit away. Good apparatus does not rescue slow measurement.'},
                          {'id': 'beaker|lid|fast',
                           'v': 5.6,
                           'why': 'Better. What is still missing is the insulation: glass '
                                  'conducts, and some of the energy is warming the beaker itself '
                                  'rather than the mixture.'},
                          {'id': 'cup|open|slow',
                           'v': 4.2,
                           'why': 'The cup insulates well, but an open top loses heat by '
                                  'evaporation and convection — and two minutes is long enough for '
                                  'that to matter.'},
                          {'id': 'cup|open|fast',
                           'v': 6.3,
                           'why': 'Close. The polystyrene is doing its job; what is escaping now '
                                  'is going straight up out of the open top.'},
                          {'id': 'cup|lid|slow',
                           'v': 5.1,
                           'why': 'Good apparatus, poor timing. The rig would have given you 6.8 '
                                  'if you had read it when the reaction finished.'},
                          {'id': 'cup|lid|fast',
                           'v': 6.8,
                           'why': 'The best a school bench will do: insulated, covered, read at '
                                  'the peak. The missing 0.2 °C went into warming the cup, the lid '
                                  'and the thermometer, and no arrangement of this apparatus '
                                  'recovers it.'}],
                 'true_value': 7.0,
                 'true_label': 'True value',
                 'reading_label': 'Your reading',
                 'lost_suffix': ' °C lost',
                 'run_label': 'Run it',
                 'best': 'cup|lid|fast',
                 'done_after': 3,
                 'close_id': 'rig-close',
                 'close_title': 'You found the best rig — and it still reads low.',
                 'close': ['A polystyrene cup with a lid and a fast reading gets you to 6.8 of the '
                           '7.0 degrees. The last two tenths went into warming the cup, the '
                           'thermometer and the lid, and no school apparatus recovers them.',
                           'That is worth saying plainly: <strong>every reading here is an '
                           'underestimate, and the error runs one way.</strong> An error that '
                           'always points the same direction is not random scatter — it is a '
                           'systematic error, and repeating the experiment will not remove it.'],
                 'id': 'rig-build',
                 'kind': 'rig-builder'}],
 'ladder': {'recall': {'q': 'What two readings do you need to find the temperature change of a '
                            'reaction?',
                       'options': ['The room temperature and the final temperature',
                                   'The temperature at the start and the temperature ten minutes '
                                   'later',
                                   'Only the highest temperature reached',
                                   'The starting temperature and the highest (or lowest) '
                                   'temperature reached'],
                       'answer': 3,
                       'feedback': {0: 'The room may not be at the same temperature as your '
                                       'solution. Measure the solution before you start.',
                                    1: 'Ten minutes later the mixture has cooled back towards room '
                                       'temperature. You need the peak.',
                                    2: 'Without a starting value there is nothing to subtract '
                                       'from, and the number on its own says nothing.'}},
            'apply': {'q': 'A group insulates the cup, fits a lid, and repeats the experiment five '
                           'times. Their answers are all close together but all lower than the '
                           'true value. What kind of error is this?',
                      'options': ['A random error, which more repeats and a better average would '
                                  'fix',
                                  'No error — close agreement between five readings means the '
                                  'results are correct',
                                  'A systematic error — heat loss makes every reading low in the '
                                  'same direction',
                                  'A mistake in the calculation, repeated the same way in all five '
                                  'runs'],
                      'answer': 2,
                      'feedback': {0: 'Random errors scatter both sides of the truth. These are '
                                      'all low, which is the signature of a systematic error.',
                                   1: 'Precise and accurate are different. Five readings can agree '
                                      'closely and all be wrong in the same way.',
                                   3: 'A calculation error would not produce consistently low '
                                      'readings from a rig that is known to leak heat.'}},
            'explain': {'q': 'Write a method for measuring the temperature change when an acid is '
                             'neutralised by an alkali. Include what you would keep the same, and '
                             'explain the reason behind two of your choices.',
                        'field_label': 'Your method',
                        'placeholder': 'I would measure 25 cm³ of acid into…',
                        'success': ['Measures a fixed volume of acid into an insulated container '
                                    'such as a polystyrene cup.',
                                    'Records the starting temperature before adding anything.',
                                    'Adds the alkali, stirs, and records the highest temperature '
                                    'reached.',
                                    'Keeps volumes, concentrations and starting temperature the '
                                    'same between runs.',
                                    'Explains that a lid and insulation reduce heat loss, so the '
                                    'measured change is closer to the true value.']},
            'produce': {'q': 'A group wants to compare which of three fuels releases the most '
                             'energy, by heating a beaker of water with each in turn. Identify the '
                             'main sources of error in that plan and say what they should keep the '
                             'same.',
                        'field_label': 'Your answer',
                        'placeholder': 'The main problem is that most of the heat…',
                        'success': ['Says much of the heat from the flame escapes into the air '
                                    'instead of reaching the water.',
                                    'Says the same volume or mass of water must be used each time.',
                                    'Says the distance from flame to beaker must be kept the same.',
                                    'Says the same mass of fuel should be burned, or the mass '
                                    'burned should be measured.',
                                    'Says the readings will all be underestimates, so the '
                                    'comparison between fuels is more trustworthy than the '
                                    'absolute values.']}},
 'key_note': 'To measure an energy change, record the starting temperature and the highest or '
             'lowest temperature reached, and subtract. Insulating the container, fitting a lid '
             'and reading promptly all reduce heat loss to the surroundings. Heat loss makes every '
             'reading too small, and because the error always runs the same way, repeating the '
             'experiment will not correct it.',
 'stretch': [{'type': 'explainer',
              'id': 'bomb-calorimeter',
              'text': 'Professional versions of this experiment are done in a bomb calorimeter: a '
                      'sealed steel vessel sitting in a measured mass of water inside an insulated '
                      'jacket, with the whole assembly weighed and its own heat capacity measured '
                      'beforehand. The reaction is ignited electrically and the water temperature '
                      'is tracked to a hundredth of a degree. The calorie figures on the back of a '
                      'food packet come from a machine like that, burning a sample of the food and '
                      'measuring the water.'},
             {'type': 'explainer',
              'id': 'the-cup-is-real-apparatus',
              'text': 'The polystyrene cup you chose is a genuine piece of scientific apparatus, '
                      'not a school compromise. It works because polystyrene foam is mostly '
                      'trapped air, and air is a poor conductor; the same principle is in a '
                      'wetsuit, a duvet and the walls of a house. What makes it good enough for a '
                      'classroom is that its own heat capacity is small — a glass beaker absorbs a '
                      'noticeable share of the energy just warming itself up, and a plastic cup '
                      'barely does.'}],
 'support': [],
 'vocabulary': [{'term': 'Temperature change',
                 'definition': 'The highest or lowest temperature reached, minus the starting '
                               'temperature. It is the quantity an energy change is judged by.',
                 'note': 'One reading on its own says nothing. You need both.'},
                {'term': 'Insulation',
                 'definition': 'Material that slows heat escaping. Polystyrene foam works because '
                               'it is mostly trapped air, and air is a poor conductor.'},
                {'term': 'Peak temperature',
                 'definition': 'The highest reading the thermometer reaches. From that moment on, '
                               'heat loss to the room is winning and the number falls.',
                 'note': 'Read it when the reaction finishes, not when you get round to it.'},
                {'term': 'Systematic error',
                 'definition': 'An error that pushes every reading the same way. Heat loss is one: '
                               'it makes every measured change too small.',
                 'note': 'Repeating and averaging will not remove it. Only changing the apparatus '
                         'will.'},
                {'term': 'Random error',
                 'definition': 'An error that scatters readings on both sides of the true value — '
                               'reading a scale slightly differently each time, for instance.',
                 'note': 'This is the kind that repeating and averaging really does reduce.'},
                {'term': 'True value',
                 'definition': 'The value a perfect measurement would give. Real apparatus gets '
                               'close to it and this apparatus never quite reaches it.'}],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why averaging does not fix heat loss?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Calorimetry with real calculations, energy per gram of fuel, and evaluating '
                'systematic error in a required practical.',
 'ws': ['experimental-skills-and-investigations',
        'analysis-and-evaluation',
        'measurement-and-units'],
 'review_state': 'draft',
 'authored': True}
