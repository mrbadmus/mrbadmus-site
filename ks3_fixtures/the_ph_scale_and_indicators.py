# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C6 `the-ph-scale-and-indicators` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 860c783d26. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C6'
SOURCE_SLUG = 'the-ph-scale-and-indicators'
FROZEN_FROM = '860c783d26'

LESSON = {'slug': 'the-ph-scale-and-indicators',
 'title': 'The pH scale and indicators',
 'discipline': 'chemistry',
 'unit': 'acids-and-alkalis',
 'family': 'MODEL',
 'covers': ['KS3.C.CR.05'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3},
             {'id': 'measurement-and-uncertainty', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['acids-and-alkalis'],
 'assumes': [],
 'references': [],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'A dye squeezed out of a boiled cabbage can tell you something about a liquid '
                 'that no amount of looking at it will. What is it actually reading?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Cabbage water', 'done_when': 'committed'},
          {'anchor': 's-scale',
           'short': 'SCALE',
           'label': 'The pH scale',
           'done_when': 'committed',
           'mirrors': 's-hook'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Testing bench',
           'done_when': 'four_tested'},
          {'anchor': 's-choose',
           'short': 'JOBS',
           'label': 'Pick the indicator',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Ten times, not twice',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Boil a red cabbage, keep the purple water, and throw away the cabbage. '
                         'You have made a scientific instrument.',
                'prompt': 'A few drops of that purple liquid go into six beakers of different '
                          'clear liquids. It comes out red in one, pink in another, purple in the '
                          'third, then blue, then green, then yellow. The cabbage water was the '
                          'same in every beaker.',
                'commit': 'If you had to guess, would juice squeezed from blackberries change '
                          'colour like this too, or only the cabbage water?',
                'options': ['Blackberry juice would too', 'Only the cabbage water'],
                'reveal': 'So the colour is a reading of how acidic or alkaline each liquid is, '
                          'and a dye that gives one is called an indicator. Next: the two main '
                          'indicators, and a number scale built from their colours.',
                'guess': True,
                'replies': ['The colour in blackberries, beetroot and red cabbage is the same kind '
                            'of dye. It changes shape in acids and alkalis, and each shape shows a '
                            'different colour.',
                            'It does feel as if red cabbage must be special. But blackberries and '
                            'beetroot hold the same kind of dye, and it changes colour in acids '
                            'and alkalis in the same way.'],
                'answer': 0},
 'misconceptions': [{'id': 'ACID-03',
                     'statement': 'pH 2 is twice as acidic as pH 4 — it is half the number, so it '
                                  'is double the strength.',
                     'elicited_by': 'think-commit-scale',
                     'confronted_by': 'think-commit-scale'},
                    {'id': 'ACID-04',
                     'statement': 'More indicator gives a different pH reading.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-ladder'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'An <strong>indicator</strong> is a dye that changes colour depending on '
                   'whether it is in an acid or an alkali. <strong>Litmus</strong> is the simple '
                   'one: red in acid, blue in alkali, and nothing in between. It answers one '
                   'question — which side of neutral is this? — and answers it instantly.'},
          {'type': 'explainer',
           'text': '<strong>Universal indicator</strong> is a mixture of several dyes, and its '
                   'colour changes gradually all the way along. Match that colour to a printed '
                   'chart and you get a number: the <strong>pH</strong>. Below 7 is acidic, above '
                   '7 is alkaline, and 7 exactly is neutral.'},
          {'type': 'figure', 'ref': 'ph-scale', 'anchor': 's-scale'},
          {'type': 'check', 'id': 'bench-six', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'a-number-not-a-side'},
          {'type': 'check', 'id': 'jobs-three', 'anchor': 's-choose'},
          {'type': 'misconception',
           'id': 'think-commit-scale',
           'anchor': 's-think',
           'targets': 'ACID-03'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [{'id': 'ph-scale',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'ph-strip',
              'title': 'The pH scale',
              'desc': 'Fifteen coloured cells in a row, numbered 0 to 14. Cells 0 to 6 run from '
                      'red through orange to yellow-green and are the acids; cell 7 is green and '
                      'is labelled neutral; cells 8 to 14 run from green-blue through blue to '
                      'purple and are the alkalis. Each cell carries its own number.',
              'caption': 'Fifteen whole numbers, one colour each. The reds and oranges are acid, '
                         'green is neutral, and the blues and purples are alkali. The numbers '
                         'matter more than the colours: colour-blind chemists use a pH meter and '
                         'get the same answer.',
              'data': {'colours': ['#C1272D',
                                   '#D2382B',
                                   '#E04A22',
                                   '#EA6A1E',
                                   '#EE8C1B',
                                   '#EFB120',
                                   '#D7CA2A',
                                   '#4FA352',
                                   '#3E9C86',
                                   '#2F8DA8',
                                   '#2A6FA8',
                                   '#2E4E96',
                                   '#453C8E',
                                   '#553191',
                                   '#5E2483'],
                       'neutral_at': 7,
                       'acid_end': 'Strongly acidic',
                       'neutral_label': 'Neutral · 7',
                       'alkali_end': 'Strongly alkaline',
                       'note': 'Every step of one is a factor of ten.'}}],
 'key_facts': [{'id': 'a-number-not-a-side',
                'text': 'Litmus tells you which side of neutral you are on. Universal indicator '
                        'gives you a number on the pH scale — and every step down that scale is '
                        'ten times more acidic.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-scale',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ACID-03',
                 'prompt': 'It looks like an ordinary number line. Commit before you read on.',
                 'options': ['Right — half the number means double the acidity, so pH 2 is twice '
                             'as strong as pH 4',
                             'Wrong — each step is ten times, so pH 2 is a hundred times more '
                             'acidic than pH 4',
                             'Wrong — the numbers are only labels for the colours and say nothing '
                             'at all about strength',
                             'Right, because the scale runs from 0 to 14 and 2 is half of 4 on it'],
                 'reveal': ['Each step of one on the pH scale is a factor of <strong>ten</strong>. '
                            'pH 3 is ten times more acidic than pH 4; pH 2 is a hundred times more '
                            'acidic than pH 4; pH 1 is a thousand times. The numbers are close '
                            'together because the scale squashes an enormous range into fifteen '
                            'steps — that is the entire reason it exists.',
                            'Which is why the gap between lemon juice at pH 2 and rainwater at pH '
                            '6 is not four small steps. It is ten thousand times. <strong>Two pH '
                            'numbers that look near each other can describe liquids that behave '
                            'nothing alike.</strong>']},
                {'eyebrow': 'Your turn · the testing bench',
                 'heading': 'Pick a sample, guess its pH, then drop the indicator in.',
                 'prompt': 'A guess you commit to is worth ten you keep to yourself.',
                 'demand': 'investigate',
                 'guess_prompt': 'Which band is it in?',
                 'litmus_label': 'Litmus:',
                 'samples': [{'id': 's1',
                              'label': 'Battery acid',
                              'ph': 0,
                              'band': 'strong-acid',
                              'litmus': 'red',
                              'setup': 'A few drops from a car battery, handled with gloves and a '
                                       'face shield.',
                              'why': 'Sulfuric acid, and about as far down the scale as anything '
                                     'you will ever meet. It is about a thousand times more acidic '
                                     'than the vinegar on a chip shop counter.'},
                             {'id': 's2',
                              'label': 'Lemon juice',
                              'ph': 2,
                              'band': 'strong-acid',
                              'litmus': 'red',
                              'setup': 'Squeezed straight from the fruit, no water added.',
                              'why': 'Citric acid. The same pH as the acid in your own stomach, '
                                     'and safe to drink because your mouth and stomach are built '
                                     'for it — your tooth enamel less so.'},
                             {'id': 's3',
                              'label': 'Rainwater',
                              'ph': 6,
                              'band': 'weak-acid',
                              'litmus': 'red',
                              'setup': 'Collected clean, in the open, well away from a road.',
                              'why': 'Slightly acidic even when perfectly clean, because carbon '
                                     'dioxide from the air dissolves into it. Genuinely pure water '
                                     'at pH 7 is a laboratory object, not a weather event.'},
                             {'id': 's4',
                              'label': 'Pure water',
                              'ph': 7,
                              'band': 'neutral',
                              'litmus': 'no change',
                              'setup': 'Distilled, straight from the still, kept sealed.',
                              'why': 'The definition of neutral. Leave the bottle open for an hour '
                                     'and it will drift towards 6 as air dissolves in.'},
                             {'id': 's5',
                              'label': 'Baking soda solution',
                              'ph': 9,
                              'band': 'weak-alkali',
                              'litmus': 'blue',
                              'setup': 'A spatula of sodium hydrogencarbonate stirred into water.',
                              'why': 'A mild alkali — mild enough to eat, which is why it is in '
                                     'cakes and in some toothpastes, where it works against the '
                                     'acid that attacks enamel.'},
                             {'id': 's6',
                              'label': 'Oven cleaner',
                              'ph': 13,
                              'band': 'strong-alkali',
                              'litmus': 'blue',
                              'setup': 'Sprayed into a beaker, in a fume cupboard, gloves on.',
                              'why': 'Sodium hydroxide. It is as far from neutral as the battery '
                                     'acid was, in the other direction, and it does comparable '
                                     'damage — but it feels soapy instead of stinging.'}],
                 'bands': [{'id': 'strong-acid',
                            'label': 'pH 0–2',
                            'lo': 0,
                            'hi': 2,
                            'verdict': 'Strongly acidic.'},
                           {'id': 'weak-acid',
                            'label': 'pH 3–6',
                            'lo': 3,
                            'hi': 6,
                            'verdict': 'Weakly acidic.'},
                           {'id': 'neutral',
                            'label': 'pH 7',
                            'lo': 7,
                            'hi': 7,
                            'verdict': 'Neutral.'},
                           {'id': 'weak-alkali',
                            'label': 'pH 8–10',
                            'lo': 8,
                            'hi': 10,
                            'verdict': 'Weakly alkaline.'},
                           {'id': 'strong-alkali',
                            'label': 'pH 11–14',
                            'lo': 11,
                            'hi': 14,
                            'verdict': 'Strongly alkaline.'}],
                 'done_at': 4,
                 'id': 'bench-six',
                 'kind': 'ph-bench'},
                {'eyebrow': 'Three jobs · pick the right indicator',
                 'heading': 'Litmus, universal indicator, or neither',
                 'prompt': 'Commit to each. The right tool is the one that answers the question '
                           'being asked — no more than that.',
                 'demand': 'classify',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'items': [{'id': 'j1',
                            'q': 'A technician needs to know whether a spilled solution is acid or '
                                 'alkali, immediately, before deciding what to clean it up with.',
                            'options': [{'id': 'lit', 'label': 'Litmus'},
                                        {'id': 'uni', 'label': 'Universal indicator'},
                                        {'id': 'none', 'label': 'Neither'}],
                            'answer': 'lit',
                            'reply': 'Litmus. One question, one answer, no chart to consult: red '
                                     'means acid, blue means alkali. A pH number would be more '
                                     'information than the decision needs, and it would take '
                                     'longer to read.'},
                           {'id': 'j2',
                            'q': 'A fish farmer must keep pond water between pH 6.5 and 8, and '
                                 'needs to know when it drifts out of range.',
                            'options': [{'id': 'lit', 'label': 'Litmus'},
                                        {'id': 'uni', 'label': 'Universal indicator'},
                                        {'id': 'none', 'label': 'Neither'}],
                            'answer': 'uni',
                            'reply': 'Universal indicator — or better, a pH meter. Litmus cannot '
                                     'help here at all: both ends of the acceptable range are '
                                     'close to neutral, and litmus only tells you which side of it '
                                     'you are on. This job needs a number.'},
                           {'id': 'j3',
                            'q': 'A student wants to know how much acid is in a bottle of vinegar '
                                 'compared with a bottle of lemon juice.',
                            'options': [{'id': 'lit', 'label': 'Litmus'},
                                        {'id': 'uni', 'label': 'Universal indicator'},
                                        {'id': 'none', 'label': 'Neither'}],
                            'answer': 'none',
                            'reply': 'Neither, on its own. pH tells you how acidic the solution '
                                     'is, not how much acid is dissolved in it — a weak acid at '
                                     'high concentration and a strong acid at low concentration '
                                     'can read the same. Answering this properly means '
                                     'neutralising each with a measured alkali and comparing how '
                                     'much it took.'}],
                 'id': 'jobs-three',
                 'kind': 'acid-judgements'}],
 'ladder': {'recall': {'q': 'What does universal indicator do that litmus does not?',
                       'options': ['It works on dry solids, so it gives the pH of a powder',
                                   'It measures danger, so it shows how harmful a substance is to '
                                   'skin',
                                   'It changes colour across the whole scale, so it shows the pH',
                                   'It changes colour for good, so the result can be kept'],
                       'answer': 2,
                       'feedback': {0: 'Both indicators need a solution. Dissolve a solid in water '
                                       'before you test it.',
                                    1: 'Neither indicator measures danger. Universal indicator '
                                       'shows the pH.',
                                    3: 'Both indicators change back if the solution changes. '
                                       'Neither colour is permanent.'}},
            'apply': {'q': 'A solution turns universal indicator green. A student adds more '
                           'indicator and the green gets deeper. What does this show about the '
                           'solution?',
                      'options': ['It is more neutral, because a deeper green means nearer to pH 7',
                                  'It is now alkaline, because the extra indicator has raised its '
                                  'pH',
                                  'It has become more concentrated, because its colour is darker',
                                  'It is still pH 7, because the indicator does not change its pH'],
                      'answer': 3,
                      'feedback': {0: 'Neutral is one point, pH 7. A solution cannot be more '
                                      'neutral than that.',
                                   1: 'The colour stayed green, so the pH is still 7. It has not '
                                      'become alkaline.',
                                   2: 'Adding indicator does not concentrate the solution. Only '
                                      'the colour changes.'}},
            'explain': {'q': 'Explain how you would find the pH of a soil sample from a garden, '
                             'and why the answer would be useful to the gardener.',
                        'field_label': 'Your method',
                        'placeholder': 'I would shake the soil with…',
                        'success': ['Says to shake the soil with distilled water and let it settle '
                                    'or filter it.',
                                    'Says to add universal indicator to the liquid.',
                                    'Says to match the colour against the pH chart to read a '
                                    'number.',
                                    'Says different plants need different pH ranges.',
                                    'Says an out-of-range result tells the gardener what to add — '
                                    'lime for acid soil.']},
            'produce': {'q': 'A drinks company claims its new drink is “gentle on teeth”. Enamel '
                             'starts to dissolve below about pH 5.5. Design a fair test that would '
                             'check the claim against an ordinary cola, and say what result would '
                             'support it.',
                        'field_label': 'Your plan',
                        'placeholder': 'I would measure the pH of…',
                        'success': ['Measures the pH of both drinks with universal indicator or a '
                                    'pH meter.',
                                    'Keeps the volume, temperature and method the same for both.',
                                    'Repeats the measurement to check it is reliable.',
                                    'Says the claim is supported only if the new drink reads above '
                                    'about 5.5.',
                                    'Notes that pH alone does not settle it — how long the drink '
                                    'stays on the teeth matters too.']}},
 'key_note': 'An indicator is a dye whose colour depends on how acidic or alkaline a solution is. '
             'Litmus is red in acid and blue in alkali. Universal indicator changes gradually and '
             'is matched against a chart to give a pH number: below 7 acidic, 7 neutral, above 7 '
             'alkaline. Each step on the scale is a factor of ten.',
 'stretch': [{'type': 'explainer',
              'id': 'dyes-out-of-plants',
              'text': 'Litmus is not a manufactured chemical. It is squeezed out of lichens — the '
                      'crusty growths on gravestones and stone walls — and has been used as a dye '
                      'since long before anyone knew what pH was. Red cabbage, beetroot, '
                      'blackberries and the petals of hydrangeas all work for the same reason: the '
                      'pigment that makes them coloured is a molecule that changes shape in acid. '
                      'Hydrangeas go further and read the soil, coming up blue in acid ground and '
                      'pink in alkaline.'},
             {'type': 'explainer',
              'id': 'nobody-judges-by-eye',
              'text': 'Nobody in a working laboratory judges pH by eye any more. A pH meter puts a '
                      'thin glass bulb into the solution and measures a voltage across it, giving '
                      'two decimal places in a second and no argument about whether the colour is '
                      'more yellow-green than green. Colour charts survive because they are cheap, '
                      'need no power and cannot go out of calibration halfway through a lesson.'}],
 'support': [],
 'vocabulary': [{'term': 'Indicator',
                 'definition': 'A dye that changes colour depending on whether it is in an acid or '
                               'an alkali.'},
                {'term': 'Litmus',
                 'definition': 'The simplest indicator: red in acid, blue in alkali, and nothing '
                               'in between. It tells you which side of neutral you are on and no '
                               'more.'},
                {'term': 'Universal indicator',
                 'definition': 'A mixture of dyes whose colour changes gradually all the way along '
                               'the scale, so it gives a pH number rather than a side.',
                 'note': 'Matched against a printed chart to read the number off.'},
                {'term': 'pH scale',
                 'definition': 'The numbered scale, 0 to 14, for how acidic or alkaline a solution '
                               'is. Each step of one is a factor of ten.'},
                {'term': 'Neutral',
                 'definition': 'pH exactly 7 — neither acidic nor alkaline. It is a single point '
                               'on the scale, not a region.'},
                {'term': 'pH meter',
                 'definition': 'An instrument that measures pH electrically and reads out a '
                               'number, with no colour to judge by eye.'}],
 'safety_note': 'Two of the six samples on that bench are corrosive. They are tested a few drops '
                'at a time, in a beaker, with gloves and eye protection — never by dipping a strip '
                'into the bottle, which contaminates what is left in it.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why the scale jumps by ten?',
           'cta': 'Ask about this lesson',
           'anchor': 's-scale'},
 'ks4_becomes': 'pH as a measure of hydrogen ion concentration, the logarithmic scale, and '
                'choosing indicators by the range over which they change.',
 'ws': ['measurement', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
