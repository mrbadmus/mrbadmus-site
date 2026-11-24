# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `enzymes-in-digestion` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'enzymes-in-digestion'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'enzymes-in-digestion',
 'title': 'Enzymes in digestion',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'PROCESS',
 'covers': ['KS3.B.NUT.04b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 2},
             {'id': 'substances-and-reactions', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': ['the-digestive-system'],
 'assumes': [],
 'references': ['food-tests', {'unit': 'P1', 'lesson': 'heating-and-thermal-equilibrium'}],
 'ks4_links': [],
 'ks4_becomes': 'The lock-and-key model, active sites, and rate-against-temperature and '
                'rate-against-pH curves.',
 'big_question': 'What is an enzyme, and what can stop it from working?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'A teaspoon', 'done_when': 'committed'},
          {'anchor': 's-bench', 'short': 'BENCH', 'label': 'Run it', 'done_when': 'reaction_run'},
          {'anchor': 's-three',
           'short': 'THREE',
           'label': 'The three',
           'mirrors': 's-bench',
           'done_when': 'reaction_run'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A teaspoon of amylase and a kilogram of starch.',
                'prompt': 'Mix a teaspoon of amylase, an enzyme from your spit, with a kilogram of '
                          'starch and wait. By the end, the starch is gone.',
                'commit': 'If you had to guess, is the amylase still there once the starch has '
                          'gone?',
                'options': ['Yes, all of it', 'No, it gets used up'],
                'reveal': 'Next: run the reaction on a bench and watch three counters, including '
                          'one that counts the enzyme.',
                'guess': True,
                'replies': ['All of it is still there. An enzyme is a catalyst: it speeds a '
                            'reaction up without being used up, so a teaspoon goes a very long '
                            'way.',
                            'The starch certainly is used up. But an enzyme ends each job exactly '
                            'as it started, ready for the next.'],
                'answer': 0},
 'misconceptions': [{'id': 'DIET-13',
                     'statement': 'Enzymes are killed by heat.',
                     'elicited_by': 'the-bench',
                     'confronted_by': 'two-wrong-ideas'},
                    {'id': 'DIET-14',
                     'statement': 'The enzyme gets used up as the food is digested.',
                     'elicited_by': 'the-bench',
                     'confronted_by': 'two-wrong-ideas'}],
 'vocabulary': [{'term': 'enzyme',
                 'definition': 'A protein that speeds up one particular reaction in a living '
                               'thing.',
                 'note': None},
                {'term': 'catalyst',
                 'definition': 'Something that makes a reaction go faster without being used up by '
                               'it.',
                 'note': 'That is why a teaspoon of enzyme can handle a kilogram of food.'},
                {'term': 'substrate',
                 'definition': 'The substance an enzyme works on.',
                 'note': None},
                {'term': 'denatured',
                 'definition': 'An enzyme whose shape has been destroyed, so it no longer fits its '
                               'substrate.',
                 'note': 'Not the same as dead. An enzyme is a molecule and was never alive.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'the-bench', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-three',
           'eyebrow': 'The three you must know',
           'statement': 'One enzyme, one substrate, one place it works best.',
           'cards': [{'term': 'Carbohydrase (amylase)',
                      'gloss': '<strong>Made in the salivary glands and pancreas</strong> starch → '
                               'glucose · Starts in the mouth, stops in the acid of the stomach, '
                               'and starts again in the small intestine when pancreatic alkali has '
                               'neutralised the acid. <strong>Best at pH 7 (neutral)</strong>'},
                     {'term': 'Protease',
                      'gloss': '<strong>Made in the stomach and pancreas</strong> protein → amino '
                               'acids · The stomach version is built to work in acid, which is '
                               'unusual for a protein — most would denature at pH 2. It is a '
                               'genuinely specialised molecule. <strong>Best at pH 2 in the '
                               'stomach, 8 in the small intestine</strong>'},
                     {'term': 'Lipase',
                      'gloss': '<strong>Made in the pancreas</strong> lipid → fatty acids + '
                               'glycerol · Works on the surface of fat droplets, so bile’s '
                               'emulsifying job multiplies its rate rather than helping it '
                               'chemically. <strong>Best at pH 8 (slightly alkaline)</strong>'}]},
          {'type': 'key-fact', 'ref': 'enzymes-are-catalysts'},
          {'type': 'misconception',
           'id': 'two-wrong-ideas',
           'anchor': 's-think',
           'targets': 'DIET-13'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'enzymes-are-catalysts',
                'text': 'An enzyme is a biological catalyst: it speeds a reaction up and is not '
                        'used up doing it. Each one has a shape that fits one substrate, and above '
                        'about 50 °C that shape is destroyed permanently.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'two-wrong-ideas',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'DIET-13',
                 'statements': [{'quote': 'Enzymes are killed by heat.',
                                 'body': ['An enzyme cannot be killed, because it was never alive. '
                                          'It is a single protein molecule — no cell, no membrane, '
                                          'no respiration, nothing that could die. What heat does '
                                          'is shake the molecule until the folds holding its shape '
                                          'come apart, and since the shape is the whole point, a '
                                          'molecule with the wrong shape no longer fits its '
                                          'substrate. The word is <em>denatured</em>, and '
                                          'examiners take the difference seriously. It matters '
                                          'practically too: “killed” suggests something that could '
                                          'be replaced by growing more, whereas a denatured enzyme '
                                          'is a permanently ruined tool. Cool it back to 37 °C and '
                                          'nothing recovers — which is exactly what you saw on the '
                                          'bench above, and it is why the change is not simply the '
                                          'reverse of warming up.']},
                                {'quote': 'The enzyme gets used up as the food is digested.',
                                 'body': ['Watch the third counter on the bench. Substrate falls, '
                                          'product rises, enzyme does not move. A single amylase '
                                          'molecule binds a starch chain, cuts it, releases the '
                                          'pieces and is immediately free to bind the next one — '
                                          'thousands of times a second in some cases. This is what '
                                          'the word catalyst means, and it explains a fact that is '
                                          'otherwise baffling: your pancreas makes a few grams of '
                                          'enzyme a day and it handles a kilogram of food. If '
                                          'enzymes were consumed by the reactions they catalyse, '
                                          'digestion would be limited by how fast you could '
                                          'manufacture them, and no animal could eat a large '
                                          'meal.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'At the bench · one tube, two dials',
                 'heading': 'Run the reaction, watch the counts',
                 'head_counter': {'off': 'not run yet', 'on': 'reaction run'},
                 'prompt': 'Watch all three counters, and watch what happens to the third one.',
                 'group_labels': {'enzyme': 'Enzyme',
                                  'ph': 'pH of the tube',
                                  'temp': 'Temperature'},
                 'enzymes': [{'id': 'amylase',
                              'label': 'Carbohydrase',
                              'equation': 'starch → glucose',
                              'opt_ph': 7,
                              'counter_substrate': 'Starch left',
                              'counter_product': 'Glucose made'},
                             {'id': 'protease',
                              'label': 'Protease',
                              'equation': 'protein → amino acids',
                              'opt_ph': [2, 8],
                              'counter_substrate': 'Protein left',
                              'counter_product': 'Amino acids made'},
                             {'id': 'lipase',
                              'label': 'Lipase',
                              'equation': 'lipid → fatty acids + glycerol',
                              'opt_ph': 8,
                              'counter_substrate': 'Lipid left',
                              'counter_product': 'Fatty acids and glycerol made'}],
                 'phs': [{'value': 2, 'label': 'pH 2 — stomach'},
                         {'value': 7, 'label': 'pH 7 — mouth'},
                         {'value': 8, 'label': 'pH 8 — small intestine'}],
                 'start_ph': 7,
                 'temp': {'min': 0,
                          'max': 80,
                          'step': 1,
                          'start': 37,
                          'format': '{t} °C',
                          'field_label': 'Temperature of the tube'},
                 'model': {'denature_c': 50,
                           'optimum_c': 37,
                           'rise_exponent': 1.6,
                           'fall_divisor': 13,
                           'ph_span': 4.5},
                 'temp_bands': {'past_optimum': 45, 'optimum': 33, 'cold': 12},
                 'temp_notes': {'denatured_hot': 'Above about 50 °C the folds holding this '
                                                 'enzyme’s shape have come apart, and the damage '
                                                 'is already done. Cooling the tube will not bring '
                                                 'it back — cool it first, then take a fresh tube.',
                                'denatured_cool': 'This enzyme was taken above 50 °C and is '
                                                  'denatured. It is back at a temperature it would '
                                                  'work perfectly well at, and it will not work at '
                                                  'all. Only a fresh tube starts again.',
                                'past_optimum': 'Past the optimum and falling fast. The molecule '
                                                'is beginning to lose its shape, and above 50 °C '
                                                'it will not get it back.',
                                'optimum': 'Around body temperature — close to the fastest this '
                                           'enzyme goes.',
                                'cold': 'Cold but unharmed. Molecules collide less often, so the '
                                        'rate is low; warm it up and it recovers completely.',
                                'freezing': 'Near freezing. Almost nothing happens, and nothing is '
                                            'damaged — this is how a fridge slows food spoiling.'},
                 'run': {'ticks': 20,
                         'tick_ms': 160,
                         'units_per_tick': 90,
                         'start_substrate': 1000,
                         'reduced_motion_scale': 0.35,
                         'slow_below_pct': 25,
                         'labels': {'start': 'Run the reaction',
                                    'more': 'Run more',
                                    'running': 'Running…',
                                    'reset': 'Fresh tube',
                                    'clock': '{n} of {total} ticks',
                                    'clock_fresh': 'fresh tube',
                                    'rate': 'Rate {pct}% of maximum'}},
                 'units_format': '{n} units',
                 'enzyme_counter_label': 'Enzyme molecules present',
                 'enzyme_counter_value': '40 — unchanged',
                 'verdicts': {'denatured': 'Nothing was digested and nothing will be. All forty '
                                           'enzyme molecules are still in the tube — they have not '
                                           'been used up, they have been ruined. Turn the '
                                           'temperature back down and run it again: still nothing. '
                                           'That is the difference between denatured and merely '
                                           'cold.',
                              'nothing': 'Nothing was digested at all. The enzyme is intact — it '
                                         'has not been ruined, and the counter still reads forty — '
                                         'but in these conditions it is not working. Move the pH '
                                         'towards one this enzyme works at, or the temperature '
                                         'back towards 37 °C, and run it again.',
                              'slow': 'A little product, slowly. The enzyme is intact and these '
                                      'are not the conditions it works best in — move the pH '
                                      'towards one this enzyme works at, or the temperature '
                                      'towards 37 °C, and run it again to see the difference.',
                              'worked': 'Substrate down, product up, enzyme unchanged. Forty '
                                        'molecules converted hundreds of units and are all still '
                                        'there, ready to do it again.'},
                 'id': 'the-bench',
                 'kind': 'enzyme-run'}],
 'ladder': {'recall': {'title': 'Rung 1 · What a catalyst is',
                       'q': 'After digesting a large amount of starch, how much of the original '
                            'amylase is left?',
                       'options': ['None, as it is used up when the starch is broken down',
                                   'About half, as some enzyme is lost each time it does its job',
                                   'It depends, as more starch uses up more of the enzyme',
                                   'All of it, as an enzyme is not used up by the reaction'],
                       'answer': 3,
                       'feedback': {0: 'Enzymes are catalysts, so they are not used up. All of it '
                                       'is left.',
                                    1: 'None is lost. Each enzyme molecule is ready to work again '
                                       'after each job.',
                                    2: 'The amount of enzyme stays the same, however much starch '
                                       'it breaks down.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Amylase at 70 °C digests no starch. It is cooled back to 37 °C and '
                           'still digests no starch. Why not?',
                      'options': ['It is now too cold, so it must be warmed up again before it '
                                  'works',
                                  'The heat killed it, so the dead enzyme can never work again',
                                  'The starch was denatured instead, so amylase has nothing to '
                                  'work on',
                                  'Its shape changed for good, so it no longer fits starch'],
                      'answer': 3,
                      'feedback': {0: '37 °C is body temperature, so it is warm enough. The enzyme '
                                      'itself has changed.',
                                   1: 'Enzymes were never alive, so they cannot be killed. Heat '
                                      'denatures them.',
                                   2: 'Starch is not denatured. The heat changed the shape of the '
                                      'enzyme.'}},
            'explain': {'title': 'Rung 3 · Explain the pH switch',
                        'q': 'Amylase from saliva works well in the mouth, stops working in the '
                             'stomach, and then starch digestion resumes in the small intestine. '
                             'Explain all three stages, and say what the pancreas contributes '
                             'besides enzymes.',
                        'field_label': 'Your explanation',
                        'placeholder': 'In the mouth… in the stomach… in the small intestine…',
                        'success': ['Says salivary amylase works at about pH 7, which is the pH of '
                                    'the mouth.',
                                    'Says the stomach is about pH 2 and that this stops amylase '
                                    'working.',
                                    'Says the pancreas supplies fresh amylase into the small '
                                    'intestine.',
                                    'Says the pancreas also supplies an alkali that neutralises '
                                    'the stomach acid, raising the pH to around 8.',
                                    'Makes clear that the amylase which entered the stomach does '
                                    'not recover — the resumed digestion uses new enzyme.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A washing powder claims to work at any temperature. Using what you '
                             'know about enzymes, say what you would expect to happen at 20 °C, at '
                             '40 °C and at 90 °C, and design a fair test of the claim.',
                        'field_label': 'Your answer',
                        'placeholder': 'At 20 °C I would expect…',
                        'success': ['Predicts slow action at 20 °C — enzymes work, but the rate is '
                                    'low.',
                                    'Predicts the best result near 40 °C, close to the optimum.',
                                    'Predicts little or no enzyme action at 90 °C because the '
                                    'enzymes are denatured, while noting hot water alone still '
                                    'removes some dirt.',
                                    'Describes a fair test: identical stains, identical fabric, '
                                    'same mass of powder, same time, only the temperature '
                                    'changed.']}},
 'key_note': 'Enzymes are biological catalysts. Carbohydrase breaks starch to glucose; protease '
             'breaks protein to amino acids; lipase breaks lipid to fatty acids and glycerol. Each '
             'works fastest at about 37 °C and at the pH of the organ that makes it. Above about '
             '50 °C the enzyme is denatured and the change is permanent.',
 'stretch': [{'type': 'explainer',
              'id': 'washing-and-pineapple',
              'text': 'Biological washing powder contains protease and lipase, which is why it '
                      'removes blood and grease and why the box tells you to wash at 40 °C rather '
                      'than 60 °C — a hot wash denatures the enzymes you paid for. The awkward '
                      'consequence is that a wash cool enough to keep the enzymes working is also '
                      'cool enough to leave some bacteria alive, so the choice between a 40 °C '
                      'enzyme wash and a 60 °C sterilising wash is a genuine trade-off rather than '
                      'a mistake. Enzymes are also why you cannot make jelly with fresh pineapple: '
                      'it contains a protease that cuts the gelatin protein apart faster than it '
                      'can set. Tinned pineapple works perfectly, because canning heats it and '
                      'denatures the enzyme.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to talk through why denaturing cannot be undone?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'convention_note': 'The bench is a simplified model: rate is shown against temperature and pH '
                    'only, and one substrate at a time. Real digestion runs several enzymes at '
                    'once on a mixture, and the curves are smoother than the numbers here suggest.',
 'review_state': 'draft',
 'authored': True}
