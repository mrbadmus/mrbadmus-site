# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 P3 `distance-time-graphs` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'P3'
SOURCE_SLUG = 'distance-time-graphs'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'distance-time-graphs',
 'title': 'Distance–time graphs',
 'discipline': 'physics',
 'unit': 'Describing motion',
 'family': 'INVESTIGATION',
 'covers': ['KS3.P.MOT.02'],
 'touches': ['KS3.WS.ANA.02'],
 'beyond_statutory': False,
 'threads': [{'id': 'motion', 'level': 2}],
 'typical_year': 7,
 'typical_minutes': 60,
 'requires': ['speed'],
 'assumes': [],
 'references': [],
 'ks4_links': [],
 'meta_description': 'Someone walks down a level corridor and the graph climbs, goes flat, then '
                     'climbs more steeply. The floor never changed height. Plot seven readings '
                     'yourself and find out what the height means.',
 'big_question': 'What can you read from a graph of a journey?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'What the height means',
           'done_when': 'committed'},
          {'anchor': 's-plot',
           'short': 'PLOT',
           'label': 'Plot seven readings',
           'done_when': 'all_seven_plotted'},
          {'anchor': 's-match',
           'short': 'MATCH',
           'label': 'Walk the graph',
           'done_when': 'target_matched'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'The line climbs. The corridor is flat.',
                'prompt': 'Someone walks 6 m down a level corridor, waits at a door, then runs the '
                          'last 12 m. A motion sensor at the start draws a graph of the journey, '
                          'and as they walk the line climbs. The floor never changed height.',
                'commit': 'If you had to guess, while the walker waits at the door, does the line '
                          'go flat, or drop to the bottom?',
                'options': ['It goes flat', 'It drops to the bottom'],
                'answer': 0,
                'reveal': 'The height of the line is the distance from the start, so it only comes '
                          'down if the walker comes back. Next: plot seven readings from a motion '
                          'sensor and read the whole journey.',
                'guess': True,
                'replies': ['The walker stays 6 m from the start the whole time they wait, so the '
                            'line stays at that height.',
                            'Stopping can feel like dropping to nothing. But the walker is still 6 '
                            'm from the start, and that is what the line shows.']},
 'misconceptions': [{'id': 'FORCE-06',
                     'statement': 'A distance–time graph is a picture of the route: the line going '
                                  'up means going uphill.',
                     'elicited_by': 's-think',
                     'confronted_by': 's-think'},
                    {'id': 'FORCE-07',
                     'statement': 'A flat line on a distance–time graph means moving at a steady '
                                  'speed.',
                     'elicited_by': 'graph-plot',
                     'confronted_by': 'graph-plot'},
                    {'id': 'FORCE-08',
                     'statement': 'A curved line on a distance–time graph means the object is '
                                  'going round a bend.',
                     'elicited_by': 's-think',
                     'confronted_by': 's-think'}],
 'core': [{'type': 'hook', 'id': 'hook-commit', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Each point is one reading: at this time, that far from the start. Join the '
                   'readings and the whole journey is in one picture — <strong>including the parts '
                   'where nothing happened.</strong>'},
          {'type': 'check', 'id': 'graph-plot', 'anchor': 's-plot'},
          {'type': 'key-fact', 'ref': 'gradient-is-the-speed'},
          {'type': 'practical', 'id': 'journey-match', 'anchor': 's-match'},
          {'type': 'misconception', 'id': 'think-uphill', 'anchor': 's-think'},
          {'type': 'quiz', 'anchor': 's-ladder'},
          {'type': 'summary'}],
 'activities': [{'id': 'think-uphill',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'FORCE-06',
                 'statements': [{'quote': 'The line goes up, so she is cycling uphill — and where '
                                          'it comes back down she is freewheeling down the other '
                                          'side.',
                                 'targets': 'FORCE-06',
                                 'body': ['A cyclist rides 400 m to the postbox, posts a letter, '
                                          'and rides home. Her graph rises, goes flat, then falls '
                                          'back to zero — and the road is flat the whole way. The '
                                          'falling section is the ride <em>home</em>. Her distance '
                                          'from the start is getting smaller, which is the only '
                                          'thing that axis can mean. When the line reaches zero '
                                          'she is back where she began.',
                                          '<strong>There is no room for a hill on this '
                                          'graph.</strong> It holds two quantities and no others: '
                                          'how long, and how far from the start. The road could be '
                                          'flat, uphill, or a spiral staircase, and the graph '
                                          'would be identical.']},
                                {'quote': 'A curved line means the object is going round a bend.',
                                 'targets': 'FORCE-08',
                                 'body': ['A distance–time graph knows nothing about direction in '
                                          'space — the only thing the axes carry is how far along '
                                          'the journey and how long it has taken. A curve means '
                                          'the gradient is changing, and the gradient is the '
                                          'speed, so <strong>a curve means speeding up or slowing '
                                          'down</strong>. An object going round a perfect bend at '
                                          'a steady speed draws a straight line here.']}]},
                {'eyebrow': "Plot the sensor's readings yourself",
                 'heading': 'Seven readings, two seconds apart',
                 'prompt': 'A motion sensor at the start of the corridor recorded the distance '
                           'every two seconds. Put each reading on the grid, in order. The one you '
                           'are looking for is named under the graph.',
                 't_values': [0, 2, 4, 6, 8, 10, 12],
                 'd_values': [0, 3, 6, 9, 12, 15, 18],
                 't_label': 'Time (s)',
                 'd_label': 'Distance from the start (m)',
                 'data': [{'t': 0, 'd': 0},
                          {'t': 2, 'd': 3},
                          {'t': 4, 'd': 6},
                          {'t': 6, 'd': 6},
                          {'t': 8, 'd': 6},
                          {'t': 10, 'd': 12},
                          {'t': 12, 'd': 18}],
                 'join_label': 'Join the points',
                 'reads': [{'id': 'q1',
                            'question': 'Between 4 s and 8 s, what was the walker doing?',
                            'options': ['Walking slowly',
                                        'Standing still',
                                        'Walking back to the start'],
                            'answer': 1,
                            'why': 'The line is flat there. The distance from the start stays at 6 '
                                   'm for four seconds, so the walker is not moving at all — a '
                                   'flat line is stopped, not slow.'},
                           {'id': 'q2',
                            'question': 'Which part of the journey was fastest?',
                            'options': ['0 to 4 s', '4 to 8 s', '8 to 12 s'],
                            'answer': 2,
                            'why': 'The last part is the steepest: 12 m in 4 s. The first part '
                                   'covers 6 m in 4 s. Steeper line, bigger speed.'},
                           {'id': 'q3',
                            'question': 'What was the speed over the last four seconds?',
                            'options': ['1.5 m/s', '3 m/s', '4.5 m/s'],
                            'answer': 1,
                            'why': 'From 6 m at 8 s to 18 m at 12 s is 12 m in 4 s. 12 ÷ 4 = 3 m/s '
                                   '— the same division as the trolley on the light gates.'}],
                 'alt': 'A distance–time grid, time 0 to 12 seconds along the bottom and distance '
                        'from the start 0 to 18 metres up the side, with seven sensor readings to '
                        'plot.',
                 'close': 'Seven readings, one line, and a whole journey — including four seconds '
                          'in which nothing happened at all.',
                 'id': 'graph-plot',
                 'kind': 'graph-plot',
                 'demand': 'investigate'},
                {'eyebrow': 'Build the journey that draws this line',
                 'heading': 'Walk the graph',
                 'prompt': 'The dashed line is the target. Choose what happens in each '
                           'three-second block, then send the walker down the corridor and watch '
                           'the line draw itself.',
                 'seg_seconds': 3,
                 'modes': [{'id': 'still', 'label': 'Stand still', 'speed_ms': 0},
                           {'id': 'walk', 'label': 'Walk · 1 m/s', 'speed_ms': 1},
                           {'id': 'jog', 'label': 'Jog · 3 m/s', 'speed_ms': 3},
                           {'id': 'back', 'label': 'Walk back · 2 m/s', 'speed_ms': -2}],
                 'target': ['walk', 'still', 'jog', 'back'],
                 'send_label': 'Send the walker',
                 'clear_label': 'Clear the line',
                 'back_refused': 'The walker cannot go back past the start, so a walk-back block '
                                 'stops at 0 m rather than going below it.',
                 'alt': 'A corridor with a walker, above a distance–time graph. A dashed target '
                        "line is drawn from 0 to 12 seconds, and the walker's own line is drawn in "
                        'as it moves.',
                 'close': 'Your line and the target are compared at the end point only, as two '
                          "numbers. Whether that counts as a match is your call, not the page's.",
                 'id': 'journey-match',
                 'kind': 'journey-match',
                 'demand': 'investigate'}],
 'figures': [],
 'key_facts': [{'id': 'gradient-is-the-speed',
                'eyebrow': 'Key fact',
                'ground': 'card',
                'placement': 'top-level',
                'text': 'On a distance–time graph, the steepness of the line is the speed. A flat '
                        'line is not slow. It is stopped.'}],
 'ladder': {'recall': {'q': 'A distance–time graph is horizontal between 20 s and 35 s. What was '
                            'happening in those fifteen seconds?',
                       'options': ['It was slowing down',
                                   'It was going back to the start',
                                   'The object was stopped',
                                   'It was moving at a steady speed'],
                       'answer': 2,
                       'feedback': {0: 'Slowing down makes the line get gradually less steep. Flat '
                                       'is not slowing — it has already stopped.',
                                    1: 'Going back makes the line fall towards zero. Horizontal '
                                       'means it stayed where it was.',
                                    3: 'A steady speed gives a straight line that still climbs. '
                                       'Flat means the distance from the start is not changing at '
                                       'all.'}},
            'apply': {'q': 'Two journeys are drawn on the same axes. Line A is steeper than line '
                           'B. Which statement must be true?',
                      'options': ['A travelled further than B',
                                  'A took longer than B',
                                  'A was going uphill and B was on the flat',
                                  'A is travelling faster than B'],
                      'answer': 3,
                      'feedback': {0: 'Not necessarily. A steep line drawn for two seconds can '
                                      'cover less ground than a gentle line drawn for a minute.',
                                   1: 'Time is read along the bottom, not from the steepness. A '
                                      'steeper line usually takes less time, not more.',
                                   2: 'Nothing on this graph is a hill. Steepness on a '
                                      'distance–time graph is speed.'}},
            'explain': {'q': 'Explain why the steepness of a distance–time graph shows the speed, '
                             'and why a flat section means the object has stopped. Use a worked '
                             'example with numbers.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The steepness shows how many metres…',
                        'success': ['Says the steepness shows how many metres are covered in each '
                                    'second, which is the speed.',
                                    'Says a steeper line means more distance in each second, so a '
                                    'faster speed.',
                                    'Says a flat section means the distance from the start is not '
                                    'changing, so the object is stopped.',
                                    'Talks about distance from the start rather than height or '
                                    'hills.',
                                    'Gives a worked example, such as a line rising 30 m in 10 s '
                                    'showing a speed of 3 m/s.']},
            'produce': {'q': 'A lift rises 30 m in 20 s, waits 10 s, then returns to the ground '
                             'floor in 15 s. Calculate its speed going up and coming down, with '
                             'units, and say which is faster. What is its speed during the wait? '
                             'When it is back on the ground floor, how far has it travelled in '
                             'total, and why is that not the same as its distance from the ground '
                             'floor?',
                        'field_label': 'Your answer',
                        'placeholder': 'Going up, the speed is…',
                        'success': ['Going up: 30 ÷ 20 = 1.5 m/s.',
                                    'Coming down: 30 ÷ 15 = 2 m/s.',
                                    'Says coming down is faster, because the same 30 m takes less '
                                    'time.',
                                    'Says the speed is 0 m/s during the wait, because its distance '
                                    'from the ground floor does not change.',
                                    'Says the total distance travelled is 60 m, because distance '
                                    'travelled only ever adds up, while the distance from the '
                                    'ground floor is back to 0 m.']}},
 'key_note': 'A distance–time graph plots distance from the start against time. Steeper means '
             'faster, flat means stopped, and a line coming back down means returning towards the '
             'start. It records a journey; it never draws the route.',
 'stretch': [{'id': 'the-graph-that-never-falls',
              'type': 'explainer',
              'text': 'Change the upright axis from <em>distance from the start</em> to <em>total '
                      'distance travelled</em> and the same journey gives a different line — one '
                      'that can never come down, because a distance you have already travelled '
                      "cannot be un-travelled. The cyclist's ride home now climbs to 800 m instead "
                      'of falling to zero. <strong>Two graphs, one journey, and only one of them '
                      'can tell you that she got home.</strong>'}],
 'support': [],
 'vocabulary': [{'term': 'distance from the start',
                 'definition': 'What the upright axis carries. It gets smaller when you come back, '
                               'which is why the line can fall.'},
                {'term': 'gradient',
                 'definition': 'How steep the line is. On a distance–time graph the gradient IS '
                               'the speed, and it is the only place the speed appears.'},
                {'term': 'horizontal line',
                 'definition': 'Stopped. The distance from the start is not changing, so nothing '
                               'is moving — it is not a slow speed.'}],
 'tutor': {'anchor': 's-plot',
           'prompt': 'Ask Mr Badmus AI',
           'body': 'Not sure why a flat line means stopped?',
           'cta': 'Ask about this lesson'},
 'ks4_becomes': 'Gradients of curved graphs, motion graphs where a value can be negative, and the '
                'area underneath them.',
 'ws': ['analysis-and-evaluation', 'measurement'],
 'authored': True}
