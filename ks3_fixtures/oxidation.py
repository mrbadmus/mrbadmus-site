# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C5 `oxidation` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C5'
SOURCE_SLUG = 'oxidation'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'oxidation',
 'title': 'Oxidation',
 'discipline': 'chemistry',
 'unit': 'types-of-reaction',
 'family': 'PROCESS',
 'covers': ['KS3.C.CR.03c'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3},
             {'id': 'structure-function', 'level': 1}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['combustion'],
 'assumes': [],
 'references': [{'unit': 'B8',
                 'lesson': 'aerobic-respiration',
                 'why': 'The reaction that keeps you alive is an oxidation, run slowly enough to '
                        'be useful.'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'big_question': 'A flash of burning magnesium and twenty years of a rusting gate are the same '
                 'reaction. What is it, and what does it need?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Fast and slow', 'done_when': 'committed'},
          {'anchor': 's-rust',
           'short': 'TUBES',
           'label': 'Four tubes',
           'done_when': 'all_tubes_predicted'},
          {'anchor': 's-stop',
           'short': 'STOP',
           'label': 'Stopping it',
           'done_when': 'all_methods_decided'},
          {'anchor': 's-think', 'short': 'THINK', 'label': 'Aluminium', 'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Magnesium burns in two seconds. A gate rusts over twenty years.',
                'prompt': 'One is a flash of white light and a puff of white powder. The other is '
                          'so slow that nobody has ever watched it happen. Both start as shiny '
                          'metal and end as a crumbly powder or crust.',
                'commit': 'If you had to guess, would all the powder left from burning magnesium '
                          'weigh more than the metal did, or less?',
                'options': ['More', 'Less'],
                'reveal': 'Rusting does the same thing slowly. Next: what oxidation is, then four '
                          'tubes that show what rusting needs.',
                'guess': True,
                'replies': ['The magnesium joins with oxygen from the air, so the powder is the '
                            'metal plus the oxygen it picked up.',
                            'Burning wood does leave less, because gases escape. But magnesium '
                            'takes oxygen in and keeps it, so the powder weighs more than the '
                            'metal did.'],
                'answer': 0},
 'misconceptions': [{'id': 'REACT-14',
                     'statement': 'Aluminium does not corrode — that is why drinks cans and window '
                                  'frames are made of it.',
                     'elicited_by': 's-think',
                     'confronted_by': 'think-reveal-oxide-layer'},
                    {'id': 'REACT-15',
                     'statement': 'Rusting needs water only, or air only.',
                     'elicited_by': 'tube-predictions',
                     'confronted_by': 'four-tube-summary'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': '<strong>Oxidation</strong> is a reaction in which a substance gains oxygen. '
                   'Metal plus oxygen makes a metal oxide, and the product always weighs more than '
                   'the metal did, because the oxygen atoms are now part of it.'},
          {'type': 'explainer',
           'text': 'That makes oxidation the widest of the four reaction types in this unit. Every '
                   'combustion is an oxidation. So is rusting, so is the browning of a cut apple, '
                   'and so — inside every cell in your body, at a temperature you can survive — is '
                   'respiration.'},
          {'type': 'check', 'id': 'tube-predictions', 'anchor': 's-rust'},
          {'type': 'key-fact', 'ref': 'gaining-oxygen'},
          {'type': 'check', 'id': 'rust-methods', 'anchor': 's-stop'},
          {'type': 'misconception',
           'id': 'think-reveal-oxide-layer',
           'anchor': 's-think',
           'targets': 'REACT-14'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'gaining-oxygen',
                'text': 'Oxidation is a substance gaining oxygen, and the product is always '
                        'heavier than what you started with. Rusting needs oxygen and water '
                        'together; salt only makes it faster.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-reveal-oxide-layer',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'REACT-14',
                 'prompt': 'Aluminium really does last outdoors for decades without going orange '
                           'and flaking. Commit before you read on.',
                 'options': ['Right — aluminium does not react with oxygen',
                             'Wrong — it oxidises immediately, and the oxide layer protects it',
                             'Right, because aluminium is a very unreactive metal',
                             'Wrong — aluminium corrodes faster than iron and cans are lined to '
                             'stop it'],
                 'reveal': ['Aluminium oxidises the moment it meets air, and faster than iron does '
                            '— it is one of the more reactive metals you will meet. Every piece of '
                            'aluminium you have ever touched was already covered in a layer of '
                            'aluminium oxide before you got to it.',
                            'The difference is what the oxide does next. Aluminium oxide is tough, '
                            'invisible and <strong>sticks tightly to the metal '
                            'underneath</strong>, so it seals the surface and the reaction stops. '
                            'Rust is crumbly and flakes off, exposing fresh iron, so the reaction '
                            'never stops — a nail left long enough rusts all the way through. '
                            '<strong>Both metals corrode; only one of them is protected by the '
                            'result.</strong>']},
                {'eyebrow': 'Your turn · four tubes, four weeks',
                 'heading': 'An identical nail in each. Only what surrounds it is different.',
                 'demand': 'investigate',
                 'prompt': 'Predict every tube before you open any of them. The tubes are designed '
                           'so that the four results together answer the question no single tube '
                           'could.',
                 'tubes': [{'id': 't1',
                            'name': 'Air and water',
                            'setup': 'An iron nail half in tap water, tube open to the air.',
                            'chips': [{'label': 'Oxygen', 'on': True},
                                      {'label': 'Water', 'on': True}],
                            'rust': True,
                            'result': 'Rusted — orange and flaking at the water line.',
                            'why': 'Both requirements present. The worst of it is at the surface, '
                                   'where the nail meets air and water at once.'},
                           {'id': 't2',
                            'name': 'Dry air, no water',
                            'setup': 'A nail in a bunged tube with a drying agent to take all '
                                     'moisture out of the air.',
                            'chips': [{'label': 'Oxygen', 'on': True},
                                      {'label': 'Water', 'on': False}],
                            'rust': False,
                            'result': 'No rust. The nail is as shiny as the day it went in.',
                            'why': 'Oxygen on its own is not enough. This tube is the control that '
                                   'rules out air being the whole story.'},
                           {'id': 't3',
                            'name': 'Water, no air',
                            'setup': 'A nail in water that was boiled to drive out dissolved air, '
                                     'with a layer of oil on top to keep more out.',
                            'chips': [{'label': 'Oxygen', 'on': False},
                                      {'label': 'Water', 'on': True}],
                            'rust': False,
                            'result': 'No rust, or the faintest trace where the oil did not quite '
                                      'seal.',
                            'why': 'Water on its own is not enough either. Together with tube 2, '
                                   'this proves both are needed — and the faint trace is honest '
                                   'data, not a failure.'},
                           {'id': 't4',
                            'name': 'Salt water and air',
                            'setup': 'A nail half in salt water, tube open to the air.',
                            'chips': [{'label': 'Oxygen', 'on': True},
                                      {'label': 'Water', 'on': True},
                                      {'label': 'Salt', 'on': True}],
                            'rust': True,
                            'result': 'Rusted heavily — much worse than tube 1 in the same four '
                                      'weeks.',
                            'why': 'Salt is not a requirement; it is an accelerator. It is why '
                                   'cars rust faster near the coast and after a gritted winter.'}],
                 'num_format': 'Tube {n}',
                 'chip_labels': {'on': 'present', 'off': 'removed'},
                 'predict_options': [{'id': 'rust', 'label': 'Will rust'},
                                     {'id': 'no', 'label': 'Will not rust'}],
                 'summary': {'id': 'four-tube-summary',
                             'title': 'Read the four together.',
                             'text': 'Tube 1 had air and water and rusted. Tube 2 had air and no '
                                     'water: no rust. Tube 3 had water and no air: no rust. So '
                                     '<strong>both</strong> are needed, and neither on its own '
                                     'will do it — which is a conclusion no single tube could have '
                                     'supported. Tube 4 had both plus salt and rusted fastest, so '
                                     'salt is not needed but it speeds the reaction up. Tubes 2 '
                                     'and 3 are the controls, and they are doing the actual work.',
                             'equation': {'left': 'iron + oxygen + water',
                                          'right': 'hydrated iron oxide (rust)'}},
                 'id': 'tube-predictions',
                 'kind': 'control-tubes'},
                {'eyebrow': 'Five ways to stop it',
                 'heading': 'Four keep the oxygen and water out. One does something cleverer.',
                 'demand': 'classify',
                 'prompt': 'Decide which kind each method is before you read it. If you know the '
                           'rule, one of the five should feel wrong under it — that is the one '
                           'worth understanding.',
                 'methods': [{'id': 'm1',
                              'name': 'Painting a bridge',
                              'what': 'A continuous film of paint over every exposed surface.',
                              'barrier': True,
                              'answer': 'A barrier. It works only while it is unbroken — a chip in '
                                        'the paint is where the rust starts, and it then spreads '
                                        'underneath.'},
                             {'id': 'm2',
                              'name': 'Oiling a bicycle chain',
                              'what': 'A thin film of oil, renewed regularly.',
                              'barrier': True,
                              'answer': 'A barrier, and a deliberately temporary one. It has to be '
                                        'renewed because it wears off, which is why chains need '
                                        'oiling rather than painting.'},
                             {'id': 'm3',
                              'name': 'Stainless steel cutlery',
                              'what': 'Iron mixed with chromium and nickel.',
                              'barrier': True,
                              'answer': 'A barrier, made by the alloy itself: the chromium '
                                        'oxidises into a tough invisible layer that seals the '
                                        'surface. Not paint, and the same trick aluminium '
                                        'performs.'},
                             {'id': 'm4',
                              'name': 'Zinc blocks bolted to a ship',
                              'what': 'Lumps of zinc attached below the waterline and replaced '
                                      'every few years.',
                              'barrier': False,
                              'answer': 'Not a barrier — the blocks do not cover anything. Zinc is '
                                        'more reactive than iron, so it corrodes instead of the '
                                        'hull. It is called sacrificial protection, and the blocks '
                                        'being eaten away is the method working.'},
                             {'id': 'm5',
                              'name': 'A galvanised gate',
                              'what': 'Steel dipped in molten zinc, leaving a zinc coat.',
                              'barrier': False,
                              'answer': 'Both, and the second one is why it is worth the money. '
                                        'The zinc is a barrier — and when the barrier is scratched '
                                        'the exposed zinc still corrodes in preference to the '
                                        'iron, so a scratch in galvanising does not start '
                                        'rusting.'}],
                 'verdict_options': [{'id': 'barrier', 'label': 'Keeps oxygen and water out'},
                                     {'id': 'other', 'label': 'Works some other way'}],
                 'id': 'rust-methods',
                 'kind': 'rust-stop'}],
 'ladder': {'recall': {'q': 'What happens to a substance during oxidation?',
                       'options': ['It gains oxygen',
                                   'It loses oxygen',
                                   'It is broken down by heat',
                                   'It reacts with water'],
                       'answer': 0,
                       'feedback': {1: 'That is reduction, which you will meet at GCSE. Oxidation '
                                       'is the gain.',
                                    2: 'That is thermal decomposition, and it needs no oxygen at '
                                       'all.',
                                    3: 'Rusting does need water as well — but the reaction is '
                                       'named for the oxygen the iron gains.'}},
            'apply': {'q': 'A nail in boiled water under a layer of oil does not rust. What does '
                           'that tube on its own prove?',
                      'options': ['Only that water alone is not enough — you need the other tubes '
                                  'to conclude anything more',
                                  'That water is not involved in rusting, so the other tubes are '
                                  'not needed',
                                  'That oil is what prevents rusting — you can conclude that from '
                                  'this tube alone',
                                  'That rusting needs salt as well, because this tube had none in '
                                  'it'],
                      'answer': 0,
                      'feedback': {1: 'Tube 1 rusted and had water in it. This tube shows water is '
                                      'not sufficient, not that it is unnecessary — and that is '
                                      'exactly why the other tubes are needed.',
                                   2: 'The oil is there to keep air out. Concluding that oil is '
                                      'the active ingredient confuses the method with the '
                                      'variable.',
                                   3: 'Tube 1 had no salt and rusted anyway. Salt changes the '
                                      'speed, not the requirements.'}},
            'explain': {'q': 'Explain why the four-tube experiment needs tubes 2 and 3, when tube '
                             '1 already shows that a nail rusts. Then state the conclusion the '
                             'whole set supports, and what tube 4 adds.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Tube 1 on its own shows that…',
                        'success': ['Says tube 1 alone shows rusting happens but not what is '
                                    'needed for it.',
                                    'Says tube 2 removes water while keeping air, and tube 3 '
                                    'removes air while keeping water.',
                                    'Says each of those tubes rules out one factor being '
                                    'sufficient on its own.',
                                    'States the conclusion: both oxygen and water are needed for '
                                    'rusting.',
                                    'Says tube 4 shows salt speeds it up without being a '
                                    'requirement.']},
            'produce': {'q': 'A boat owner is told that bolting blocks of a more reactive metal to '
                             'the hull will protect it, and replies that adding more reactive '
                             'metal to a corroding boat sounds like the worst possible idea. '
                             'Explain why the method works, what happens to the blocks, and why '
                             'they have to be checked.',
                        'field_label': 'Your answer',
                        'placeholder': 'The blocks are more reactive than iron, so…',
                        'success': ['Says the blocks are made of a metal more reactive than iron, '
                                    'such as zinc.',
                                    'Says the more reactive metal corrodes in preference to the '
                                    'iron.',
                                    'Says the hull is therefore protected while the blocks last.',
                                    'Says the blocks are gradually eaten away, which is the method '
                                    'working rather than failing.',
                                    'Says they must be inspected and replaced, or the protection '
                                    'ends and the hull starts to corrode.']}},
 'key_note': 'Oxidation is a substance gaining oxygen, and the product weighs more than the '
             'starting material. Combustion is oxidation fast enough to burn; rusting is oxidation '
             'slow enough to take years, and it needs oxygen and water together — salt only speeds '
             'it up. Rust flakes off and exposes fresh iron, which is why iron keeps rusting while '
             'aluminium, whose oxide clings, does not.',
 'stretch': [{'type': 'explainer',
              'id': 'oxidation-without-a-flame',
              'text': 'Oxidation does not need a flame, a bench or a metal. Cut an apple and the '
                      'surface browns within minutes as substances in the flesh oxidise in air; '
                      'lemon juice slows it because vitamin C is oxidised first, which is what '
                      '"antioxidant" means on a label. And the reaction that keeps you alive is an '
                      'oxidation: glucose plus oxygen makes carbon dioxide and water, exactly the '
                      'products of burning it, released slowly enough at 37 °C that your cells can '
                      'use the energy instead of catching fire.'},
             {'type': 'explainer',
              'id': 'the-sacrificial-block',
              'text': 'The cleverest anti-rusting trick is worth knowing in full. Bolt blocks of '
                      "zinc to a steel ship's hull and the zinc corrodes instead of the steel — "
                      'not by covering it, but because zinc is the more reactive of the two, and '
                      'the more reactive metal corrodes in preference to the other. The blocks are '
                      'inspected and replaced every few years, which is why they are called '
                      'sacrificial. Galvanising is the same idea in a thin layer: a scratch in a '
                      'galvanised gate does not start rusting, because the zinc around the scratch '
                      'is still doing the corroding for it.'}],
 'support': [],
 'vocabulary': [{'term': 'oxidation',
                 'definition': 'A reaction in which a substance gains oxygen. The product always '
                               'weighs more than the substance you started with.'},
                {'term': 'metal oxide',
                 'definition': 'What a metal becomes when it gains oxygen — magnesium oxide, iron '
                               'oxide, aluminium oxide.'},
                {'term': 'rust',
                 'definition': 'Hydrated iron oxide: what iron becomes when it has oxygen and '
                               'water together. It is crumbly and flakes off, which is why the '
                               'iron underneath keeps rusting.',
                 'note': 'Only iron and steel rust. Other metals corrode, which is the general '
                         'word.'},
                {'term': 'corrosion',
                 'definition': 'A metal being eaten away by reacting with its surroundings. '
                               'Rusting is corrosion; so is the oxidising of aluminium and of '
                               'zinc.'},
                {'term': 'control',
                 'definition': 'A tube set up to remove exactly one thing, so that what happens in '
                               'it tells you whether that one thing was needed.'},
                {'term': 'sacrificial protection',
                 'definition': 'Attaching a more reactive metal so that it corrodes in preference '
                               'to the iron you want to keep. The blocks are eaten away on purpose '
                               'and are replaced.'}],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why tubes 2 and 3 are the important ones?',
           'cta': 'Ask about this lesson',
           'anchor': 's-rust'},
 'ks4_becomes': 'Oxidation and reduction as electron transfer, corrosion and its prevention, and '
                'the reactivity series explained.',
 'ws': ['experimental-skills', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
