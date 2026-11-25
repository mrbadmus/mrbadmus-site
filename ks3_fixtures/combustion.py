# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C5 `combustion` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C5'
SOURCE_SLUG = 'combustion'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'combustion',
 'title': 'Combustion',
 'discipline': 'chemistry',
 'unit': 'types-of-reaction',
 'family': 'PROCESS',
 'covers': ['KS3.C.CR.03a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 4}, {'id': 'energy', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['word-equations'],
 'assumes': ['chemical-vs-physical-change'],
 'references': ['symbol-equations-and-balancing',
                {'unit': 'B4',
                 'lesson': 'the-gas-exchange-system',
                 'why': 'Where carbon monoxide does its harm.'}],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'A collar of metal at the bottom of a burner decides whether the flame is clean '
                 'and hot or dirty, cool and poisonous. Why should a hole in the side matter that '
                 'much?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Two flames', 'done_when': 'committed'},
          {'anchor': 's-burner',
           'short': 'BENCH',
           'label': 'The burner bench',
           'done_when': 'both_air_settings_read'},
          {'anchor': 's-fuels',
           'short': 'FUELS',
           'label': 'Three fuels',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Which is hotter?',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two flames on the same burner. One is clean and roaring. One is lazy, '
                         'yellow and quietly making a poison.',
                'prompt': 'Same burner, same room. The only thing that changed was a metal collar '
                          'at the bottom of the burner. Hold a beaker over the yellow flame and it '
                          'comes away black; hold it over the blue one and it stays clean.',
                'commit': 'If you had to guess, what does the hole in the collar let into the '
                          'burner: more gas, or more air?',
                'options': ['More gas', 'More air'],
                'reveal': 'Burning needs oxygen, and how much arrives changes what the flame '
                          'makes. Next: what combustion is, then a burner where you open and shut '
                          'the hole yourself.',
                'guess': True,
                'replies': ['Gas is what burns, so that makes sense. But the gas comes in at the '
                            'bottom through the tap, and that stayed the same. The collar opens a '
                            'hole for air.',
                            'The hole lets air into the burner. Air carries the oxygen the gas '
                            'needs to burn properly, and with the hole shut there is too little of '
                            'it.'],
                'answer': 1},
 'misconceptions': [{'id': 'REACT-10',
                     'statement': 'The big yellow flame is hotter — you can see more fire.',
                     'elicited_by': 'think-commit-yellow',
                     'confronted_by': 'think-commit-yellow'},
                    {'id': 'REACT-11',
                     'statement': 'Shutting the air off makes a flame burn hotter or more '
                                  'fiercely.',
                     'elicited_by': 'gate-air-shut',
                     'confronted_by': 'shut-hole-run'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': '<strong>Combustion</strong> is a fuel reacting with oxygen and giving out '
                   'energy. Nothing burns without oxygen, which is why a jar over a candle puts it '
                   'out — and why a rocket leaving the atmosphere has to carry its own oxygen with '
                   'it.'},
          {'type': 'explainer',
           'text': 'When there is enough oxygen for the reaction to finish, it is <strong>complete '
                   'combustion</strong>. When there is not, it is <strong>incomplete '
                   'combustion</strong>, and the products are different — worse in every way.'},
          {'type': 'check', 'id': 'shut-hole-run', 'anchor': 's-burner'},
          {'type': 'key-fact', 'ref': 'what-the-air-hole-decides'},
          {'type': 'check', 'id': 'three-fuels', 'anchor': 's-fuels'},
          {'type': 'misconception',
           'id': 'think-commit-yellow',
           'anchor': 's-think',
           'targets': 'REACT-10'},
          {'type': 'rule',
           'id': 'three-things-a-fire-needs',
           'eyebrow': 'Reference · three things a fire needs',
           'statement': 'Take away any one of them and it stops',
           'cards': [{'term': 'Fuel',
                      'gloss': 'A firebreak clears the fuel out of the way so a wildfire has '
                               'nothing to reach.'},
                     {'term': 'Oxygen',
                      'gloss': 'A fire blanket, a pan lid or a carbon dioxide extinguisher cuts '
                               'the air off.'},
                     {'term': 'Heat',
                      'gloss': 'Water cools the fuel below the temperature at which it can keep '
                               'going.'}],
           'close': 'Never water on a chip-pan fire or on an electrical fire: hot oil throws '
                    'burning droplets everywhere, and water conducts. Cutting off the oxygen is '
                    'the move in both cases.'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'what-the-air-hole-decides',
                'text': 'Combustion is a fuel reacting with oxygen and giving out energy. With '
                        'enough oxygen the carbon in the fuel ends up as carbon dioxide and the '
                        'hydrogen ends up as water. With too little, some carbon comes out as soot '
                        'and some as carbon monoxide, and less energy is released.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-yellow',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'REACT-10',
                 'prompt': 'It is taller, brighter and looks far more like a fire. Commit before '
                           'you read on.',
                 'options': ['Right — the yellow flame is hotter; the brightness is heat you can '
                             'see',
                             'Wrong — the blue flame is hotter; the yellow glow is glowing soot',
                             'Right — yellow light carries more energy; the colour is the '
                             'temperature',
                             'Wrong — both flames are the same temperature; only the size has '
                             'changed'],
                 'reveal': ['The blue flame is the hot one — around 1500 °C at its tip, against '
                            'roughly 1000 °C for the yellow. What you can see in the yellow flame '
                            'is <strong>glowing soot</strong>: unburnt carbon, hot enough to give '
                            'off light but not burning. The brightness is the fuel being wasted, '
                            'and the soot lands on whatever you were trying to heat.',
                            'Which is why the blue flame is almost invisible. There is nothing '
                            'solid left in it to glow — every carbon atom has already made it to '
                            'carbon dioxide. <strong>In a flame, visible is not the same as '
                            'hot.</strong> The safety flame is yellow so you can see the burner is '
                            'lit; the working flame is blue because it is finishing the job.']},
                {'eyebrow': 'Your turn · the burner bench',
                 'heading': 'Pick a fuel, set the air supply, and see what comes out',
                 'demand': 'investigate',
                 'dials': [{'id': 'fuel',
                            'label': 'The fuel',
                            'options': [{'id': 'methane', 'label': 'Methane'},
                                        {'id': 'wax', 'label': 'Candle wax'},
                                        {'id': 'charcoal', 'label': 'Charcoal'},
                                        {'id': 'hydrogen', 'label': 'Hydrogen'}]},
                           {'id': 'air',
                            'label': 'The air supply',
                            'tracks_done': True,
                            'options': [{'id': 'open', 'label': 'Air hole open'},
                                        {'id': 'shut', 'label': 'Air hole shut'}]}],
                 'predict': {'gate_id': 'gate-air-shut',
                             'prompt': 'Before you light it: with the air hole shut, what will be '
                                       'in the products that was not there before?',
                             'options': ['Nothing new, and a flame that gives less heat',
                                         'Soot, and a gas that is colourless and poisonous',
                                         'More carbon dioxide, and a flame that burns hotter']},
                 'tiles': [{'id': 'flame', 'label': 'The flame'},
                           {'id': 'energy', 'label': 'Energy released'},
                           {'id': 'soot', 'label': 'Beaker held over the flame'},
                           {'id': 'air', 'label': 'In the air around it'}],
                 'eq_label': 'The word equation for this run',
                 'runs': [{'id': 'methane:open',
                           'eq_left': 'methane + oxygen',
                           'eq_right': 'carbon dioxide + water',
                           'cells': [{'value': 'Blue, roaring, around 1500 °C',
                                      'note': 'Nothing solid in it to glow.'},
                                     {'value': 'All of it', 'note': 'The reaction finished.'},
                                     {'value': 'None — the beaker stays clean',
                                      'note': 'Carbon that never made it to carbon dioxide.'},
                                     {'value': 'Nothing harmful from this reaction',
                                      'note': 'No carbon monoxide. Every carbon atom reached '
                                              'carbon dioxide.'}],
                           'verdict': 'Complete combustion. Enough oxygen arrived for every atom '
                                      'in the fuel to finish reacting, so all of the available '
                                      'energy came out and nothing was left over.'},
                          {'id': 'methane:shut',
                           'eq_left': 'methane + oxygen',
                           'eq_right': 'carbon monoxide + carbon + water',
                           'cells': [{'value': 'Yellow, lazy, around 1000 °C',
                                      'note': 'The brightness is glowing soot.'},
                                     {'value': 'Less than the fuel could give',
                                      'note': 'Unfinished reactions release less.'},
                                     {'value': 'Black deposit on the beaker within seconds',
                                      'note': 'Carbon that never made it to carbon dioxide.'},
                                     {'value': 'Carbon monoxide',
                                      'alert': True,
                                      'note': 'Carbon monoxide: colourless, odourless, and it '
                                              'stops your blood carrying oxygen.'}],
                           'verdict': 'Incomplete combustion. The fuel still reacted and it did '
                                      'not finish: some carbon stopped at carbon monoxide, some '
                                      'never reacted at all and came out as soot, and the energy '
                                      'you wanted stayed locked in both of them.'},
                          {'id': 'wax:open',
                           'eq_left': 'candle wax + oxygen',
                           'eq_right': 'carbon dioxide + water',
                           'cells': [{'value': 'Blue, roaring, around 1500 °C',
                                      'note': 'Nothing solid in it to glow.'},
                                     {'value': 'All of it', 'note': 'The reaction finished.'},
                                     {'value': 'None — the beaker stays clean',
                                      'note': 'Carbon that never made it to carbon dioxide.'},
                                     {'value': 'Nothing harmful from this reaction',
                                      'note': 'No carbon monoxide. Every carbon atom reached '
                                              'carbon dioxide.'}],
                           'verdict': 'Complete combustion. Enough oxygen arrived for every atom '
                                      'in the fuel to finish reacting, so all of the available '
                                      'energy came out and nothing was left over.'},
                          {'id': 'wax:shut',
                           'eq_left': 'candle wax + oxygen',
                           'eq_right': 'carbon monoxide + carbon + water',
                           'cells': [{'value': 'Yellow, lazy, around 1000 °C',
                                      'note': 'The brightness is glowing soot.'},
                                     {'value': 'Less than the fuel could give',
                                      'note': 'Unfinished reactions release less.'},
                                     {'value': 'Black deposit on the beaker within seconds',
                                      'note': 'Carbon that never made it to carbon dioxide.'},
                                     {'value': 'Carbon monoxide',
                                      'alert': True,
                                      'note': 'Carbon monoxide: colourless, odourless, and it '
                                              'stops your blood carrying oxygen.'}],
                           'verdict': 'Incomplete combustion. The fuel still reacted and it did '
                                      'not finish: some carbon stopped at carbon monoxide, some '
                                      'never reacted at all and came out as soot, and the energy '
                                      'you wanted stayed locked in both of them.'},
                          {'id': 'charcoal:open',
                           'eq_left': 'carbon + oxygen',
                           'eq_right': 'carbon dioxide',
                           'eq_note': 'Charcoal is mostly carbon, with a little ash and other '
                                      'substances in it, so the equation is written for the '
                                      'carbon.',
                           'cells': [{'value': 'Orange glow, hardly any flame',
                                      'note': 'The solid itself is glowing, not a gas above it.'},
                                     {'value': 'All of it', 'note': 'The reaction finished.'},
                                     {'value': 'None — the beaker stays clean',
                                      'note': 'Carbon that never made it to carbon dioxide.'},
                                     {'value': 'Nothing harmful from this reaction',
                                      'note': 'No carbon monoxide. Every carbon atom reached '
                                              'carbon dioxide.'}],
                           'verdict': 'Complete combustion. Enough oxygen arrived for every atom '
                                      'in the fuel to finish reacting, so all of the available '
                                      'energy came out and nothing was left over.'},
                          {'id': 'charcoal:shut',
                           'eq_left': 'carbon + oxygen',
                           'eq_right': 'carbon monoxide + carbon',
                           'eq_note': 'Charcoal is mostly carbon, with a little ash and other '
                                      'substances in it, so the equation is written for the '
                                      'carbon.',
                           'cells': [{'value': 'A dull, dark glow',
                                      'note': 'Less oxygen reaching it means less of it burning.'},
                                     {'value': 'Less than the fuel could give',
                                      'note': 'Unfinished reactions release less.'},
                                     {'value': 'Black deposit on the beaker within seconds',
                                      'note': 'Carbon that never made it to carbon dioxide.'},
                                     {'value': 'Carbon monoxide',
                                      'alert': True,
                                      'note': 'Carbon monoxide: colourless, odourless, and it '
                                              'stops your blood carrying oxygen.'}],
                           'verdict': 'Incomplete combustion. The fuel still reacted and it did '
                                      'not finish: some carbon stopped at carbon monoxide, some '
                                      'never reacted at all and came out as soot, and the energy '
                                      'you wanted stayed locked in both of them.'},
                          {'id': 'hydrogen:open',
                           'eq_left': 'hydrogen + oxygen',
                           'eq_right': 'water',
                           'cells': [{'value': 'Almost invisible, very hot',
                                      'note': 'Nothing solid in it to glow.'},
                                     {'value': 'All of it', 'note': 'The reaction finished.'},
                                     {'value': 'None — there is no carbon in the fuel',
                                      'note': 'There is no carbon in this fuel to leave behind.'},
                                     {'value': 'Nothing harmful from this reaction',
                                      'note': 'No carbon monoxide is possible, whatever the air '
                                              'supply.'}],
                           'verdict': 'Complete combustion. Enough oxygen arrived for every atom '
                                      'in the fuel to finish reacting, so all of the available '
                                      'energy came out and nothing was left over.'},
                          {'id': 'hydrogen:shut',
                           'eq_left': 'hydrogen + oxygen',
                           'eq_right': 'water',
                           'cells': [{'value': 'Pale and quiet',
                                      'note': 'Nothing solid in it to glow.'},
                                     {'value': 'Nearly all of it',
                                      'note': 'Unfinished reactions release less.'},
                                     {'value': 'None — there is no carbon in the fuel',
                                      'note': 'There is no carbon in this fuel to leave behind.'},
                                     {'value': 'Nothing harmful from this reaction',
                                      'note': 'No carbon monoxide is possible, whatever the air '
                                              'supply.'}],
                           'verdict': 'Incomplete combustion, and without carbon in the fuel it '
                                      'looks quite different. Less oxygen still means less of the '
                                      'hydrogen finishes reacting, so less energy comes out — but '
                                      'there is no carbon to stop half way, so there is no soot '
                                      'and no carbon monoxide. The only product is still water.'}],
                 'close': 'Same fuel, both air settings. Shutting the air off did not stop the '
                          'reaction and did not make it hotter — it made it '
                          '<strong>unfinished</strong>. Less energy out, soot on the glass, and '
                          'carbon monoxide in the room. A yellow flame is never the flame you heat '
                          'something with.',
                 'id': 'shut-hole-run',
                 'kind': 'burner-bench'},
                {'eyebrow': 'Three fuels · predict the products',
                 'heading': 'Complete combustion, plenty of oxygen. What comes out?',
                 'demand': 'construct',
                 'prompt': 'One rule does all three: every carbon atom in the fuel ends up in '
                           'carbon dioxide, and every hydrogen atom ends up in water. Read the '
                           'fuel, commit, then check.',
                 'options': [{'id': 'both', 'label': 'Carbon dioxide + water'},
                             {'id': 'co2', 'label': 'Carbon dioxide only'},
                             {'id': 'water', 'label': 'Water only'}],
                 'fuels': [{'id': 'f1',
                            'name': 'Propane, in a camping stove',
                            'made': 'Made of carbon and hydrogen only. Burned with plenty of air.',
                            'answer': 'both',
                            'eq_left': 'propane + oxygen',
                            'eq_right': 'carbon dioxide + water',
                            'why': 'Carbon and hydrogen in the fuel, so carbon dioxide and water '
                                   'out. Every hydrocarbon burned completely gives these two '
                                   'products and no others.'},
                           {'id': 'f2',
                            'name': 'Charcoal, on a barbecue',
                            'made': 'Almost pure carbon. No hydrogen in it at all.',
                            'answer': 'co2',
                            'eq_left': 'carbon + oxygen',
                            'eq_right': 'carbon dioxide',
                            'why': 'No hydrogen means no water. One product only — which is why a '
                                   'charcoal barbecue in an enclosed space is so dangerous when '
                                   'the air runs short and that product becomes carbon monoxide '
                                   'instead.'},
                           {'id': 'f3',
                            'name': 'Hydrogen, in a hydrogen-powered bus',
                            'made': 'No carbon anywhere in the fuel.',
                            'answer': 'water',
                            'eq_left': 'hydrogen + oxygen',
                            'eq_right': 'water',
                            'why': 'No carbon means no carbon dioxide and no soot. The exhaust is '
                                   'water. This is the reason hydrogen is interesting, and the '
                                   'reason the argument about it happens elsewhere — in how the '
                                   'hydrogen was made.'}],
                 'id': 'three-fuels',
                 'kind': 'fuel-cards'}],
 'ladder': {'recall': {'q': 'What are the products of the complete combustion of a fuel containing '
                            'carbon and hydrogen?',
                       'options': ['Carbon monoxide and water',
                                   'Carbon dioxide only',
                                   'Soot and water vapour',
                                   'Carbon dioxide and water'],
                       'answer': 3,
                       'feedback': {0: 'Carbon monoxide is a product of incomplete combustion, '
                                       'when the oxygen supply is short.',
                                    1: 'The hydrogen in the fuel has to go somewhere, and it goes '
                                       'into water.',
                                    2: 'Soot means carbon that never finished reacting. With '
                                       'enough oxygen there is none.'}},
            'apply': {'q': 'A Bunsen burner is giving a tall yellow flame. What does that tell '
                           'you?',
                      'options': ['Turning the gas up makes the flame taller, so the colour '
                                  'follows the amount of fuel',
                                  'A bigger, brighter flame is a hotter flame, so the yellow one '
                                  'is burning more fiercely',
                                  'Not enough air is getting in, so combustion is incomplete',
                                  'Yellow means the gas supply is contaminated, so the colour '
                                  'comes from the impurity'],
                      'answer': 2,
                      'feedback': {0: 'The gas tap changes the size of the flame. The colour is '
                                      'about air, and yellow means too little of it.',
                                   1: 'The blue flame is hotter, at around 1500 °C. The yellow '
                                      'glow is soot, and soot is wasted fuel.',
                                   3: 'Same gas, both flames. Open the air hole and the yellow '
                                      'flame becomes blue immediately.'}},
            'explain': {'q': 'A gas fire is burning with a yellow flame and there is black marking '
                             'on the wall above it. Explain what is going wrong chemically, why it '
                             'is dangerous, and why the danger cannot be detected by smell.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The yellow flame shows that…',
                        'success': ['Says the yellow flame and soot show incomplete combustion.',
                                    'Says there is not enough oxygen for all the carbon to become '
                                    'carbon dioxide.',
                                    'Names carbon monoxide as a product of incomplete combustion.',
                                    'Says carbon monoxide is colourless and has no smell, so it '
                                    'gives no warning.',
                                    'Says less energy is released as well, so the fire is also '
                                    'wasting fuel.']},
            'produce': {'q': 'A rocket has to burn its fuel hundreds of kilometres above the '
                             'Earth, where there is effectively no air. A candle in a sealed jar '
                             'goes out within seconds. Use the same idea to explain both, and say '
                             'what a rocket must therefore carry.',
                        'field_label': 'Your answer',
                        'placeholder': 'Combustion needs…',
                        'success': ['Says combustion needs oxygen as a reactant, not just fuel.',
                                    'Explains the candle: the oxygen in the sealed jar is used up, '
                                    'so the reaction stops.',
                                    'Says there is no oxygen in space for a rocket to react with.',
                                    'Says the rocket must carry its own supply of oxygen, or '
                                    'another oxidiser.',
                                    'Notes that this is why the fuel alone is not enough, however '
                                    'much of it there is.']}},
 'key_note': 'Combustion is a fuel reacting with oxygen, giving out energy. Complete combustion — '
             'plenty of oxygen — turns the carbon in the fuel into carbon dioxide and the hydrogen '
             'into water, and releases all the available energy. Incomplete combustion, with too '
             'little oxygen, leaves soot and produces carbon monoxide, and releases less. A yellow '
             'flame is the visible warning; the poison is not visible at all.',
 'stretch': [{'type': 'explainer',
              'id': 'carbon-monoxide-and-blood',
              'text': 'Carbon monoxide is dangerous for a reason that belongs to biology, and you '
                      'meet it properly in <em>The gas exchange system</em>. It sticks to the '
                      'haemoglobin in your red blood cells far more strongly than oxygen does, and '
                      'it does not let go — so the blood keeps circulating while carrying less and '
                      'less oxygen. There is no smell and no taste, and the early symptoms are a '
                      'headache and tiredness, which is exactly what you would ignore. A boiler '
                      'burning with a yellow flame instead of a blue one is producing it, which is '
                      'why the servicing is a legal requirement rather than a suggestion.'},
             {'type': 'explainer',
              'id': 'a-clean-flame-is-not-a-clean-fuel',
              'text': 'Hydrogen is the fuel that breaks the pattern: it contains no carbon at all, '
                      'so complete combustion gives water and nothing else — no carbon dioxide, no '
                      'soot, no carbon monoxide. That is the whole appeal of a hydrogen car. The '
                      'catch is not in the burning; it is that hydrogen has to be made first, and '
                      'most of it today is made from natural gas, which releases carbon dioxide '
                      'somewhere else. A clean flame is not the same as a clean fuel, and knowing '
                      'where to look is the difference.'}],
 'support': [],
 'vocabulary': [{'term': 'Combustion',
                 'definition': 'A reaction in which a fuel reacts with oxygen and gives out '
                               'energy.',
                 'note': 'Burning is the everyday word for it. Nothing burns without oxygen.'},
                {'term': 'Fuel',
                 'definition': 'A substance burned to release energy.',
                 'note': None},
                {'term': 'Complete combustion',
                 'definition': 'Combustion with enough oxygen for the reaction to finish, so all '
                               'the available energy is released.',
                 'note': 'The carbon in the fuel ends up as carbon dioxide and the hydrogen ends '
                         'up as water.'},
                {'term': 'Incomplete combustion',
                 'definition': 'Combustion with too little oxygen, so the reaction does not '
                               'finish.',
                 'note': 'It makes soot and carbon monoxide and releases less energy. A yellow '
                         'flame from a burner is the warning sign.'},
                {'term': 'Carbon monoxide',
                 'definition': 'A colourless, odourless, poisonous gas made when a fuel containing '
                               'carbon burns without enough oxygen.',
                 'note': 'It stops the blood carrying oxygen, and there is nothing to smell.'},
                {'term': 'Soot',
                 'definition': 'Carbon from a fuel that never finished reacting, left behind as a '
                               'black solid.',
                 'note': 'It is what makes a yellow flame bright, and it is wasted fuel.'},
                {'term': 'Hydrocarbon',
                 'definition': 'A compound made of carbon and hydrogen only.',
                 'note': 'Methane, propane and candle wax are all hydrocarbons, which is why all '
                         'three burn to the same two products.'}],
 'safety_note': 'Anything held in a flame stays hot long after it stops looking it, and glass '
                'shows nothing at all — the sooted beaker is moved with tongs and left to cool. '
                'Open the collar only while you are actually heating something, and turn the '
                'burner back to the yellow flame as soon as you stop, so that everyone can see it '
                'is lit.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why the blue flame is the hot one?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Fuels, the atmosphere and pollutants, and combustion as an exothermic reaction '
                'with a reaction profile.',
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
