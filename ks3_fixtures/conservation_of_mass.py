# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C2 `conservation-of-mass` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 256741b1d0. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C2'
SOURCE_SLUG = 'conservation-of-mass'
FROZEN_FROM = '256741b1d0'

LESSON = {'slug': 'conservation-of-mass',
 'title': 'Conservation of mass',
 'discipline': 'chemistry',
 'unit': 'atoms-elements-and-compounds',
 'family': 'QUANTITATIVE',
 'covers': ['KS3.C.AEC.04a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}, {'id': 'particles', 'level': 3}],
 'typical_year': 7,
 'typical_minutes': 60,
 'requires': ['formulae'],
 'assumes': [],
 'references': [{'unit': 'C1', 'lesson': 'changes-of-state'}],
 'ks4_links': [],
 'big_question': 'A candle burns down to nothing. A nail rusts and gets heavier. What is happening '
                 'to the mass in each?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Where the wax went',
           'done_when': 'committed'},
          {'anchor': 's-balance',
           'short': 'BALANCE',
           'label': 'Open and sealed',
           'done_when': 'three_runs_done'},
          {'anchor': 's-build',
           'short': 'STEPS',
           'label': 'Your own four steps',
           'done_when': 'steps_opened'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Burning and mass',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Sixty grams of candle, and by morning there is nothing on the plate.',
                'prompt': 'Light a candle in the evening and leave it. In the morning the wax is '
                          'gone, the plate is clean, and the balance reads what an empty plate '
                          'reads. Nothing was taken away and nobody touched it.',
                'commit': 'If you had to guess, where did the wax go?',
                'options': ['Into gas in the air', 'Into heat and light'],
                'reveal': 'Those gases have mass, but in an open room nobody weighs them. Next: a '
                          'balance, with the flask open and then sealed.',
                'guess': True,
                'replies': ['The wax joined with oxygen from the air and drifted off as invisible '
                            'gases. It is still somewhere in the room.',
                            'A candle does give off heat and light. But heat and light are not '
                            'made of anything you can weigh. The wax itself leaves as gas.'],
                'answer': 0},
 'misconceptions': [{'id': 'ATOM-11',
                     'statement': 'When something burns, the mass is destroyed — it turns into '
                                  'heat and light.',
                     'elicited_by': 'think-commit-burning',
                     'confronted_by': 'think-commit-burning'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'A reaction rearranges atoms. It does not make any and it does not destroy any. '
                   'So the mass of everything you started with must equal the mass of everything '
                   'you end with — as long as you can weigh all of it.'},
          {'type': 'practical', 'id': 'open-and-sealed', 'anchor': 's-balance'},
          {'type': 'formula',
           'id': 'the-rule',
           'eyebrow': 'The rule',
           'statement': 'total mass of everything before = total mass of everything after',
           'support': ['everything means the gases too', 'mass is measured in grams (g)'],
           'figure': {'shape': 'balance',
                      'aria_label': 'A balance beam, level. On the left pan: the total mass of '
                                    'everything you started with. On the right pan: the total mass '
                                    'of everything you ended with. The two are equal.',
                      'pans': {'left': 'before', 'right': 'after'},
                      'caption': 'always level'},
           'cover': {'shape': 'bar',
                     'eyebrow': 'The bar',
                     'heading': 'Cover the one you want',
                     'aria_label': 'A bar model. One long bar is everything before the reaction. '
                                   'Underneath, the same length is split into two: what is left in '
                                   'the flask, and the gas. Covering one part leaves the way to '
                                   'work it out.',
                     'whole': {'id': 'whole',
                               'label': 'everything before',
                               'button': 'Cover the whole'},
                     'parts': [{'id': 'left',
                                'label': 'left in the flask',
                                'button': 'Cover what is left',
                                'weight': 296},
                               {'id': 'gas',
                                'label': 'the gas',
                                'button': 'Cover the gas',
                                'weight': 146}],
                     'covered': 'gas',
                     'results': {'whole': {'result': 'before = left in the flask + the gas',
                                           'sentence': 'Cover the whole bar and you are left with '
                                                       'the two parts side by side — add them.'},
                                 'left': {'result': 'left in the flask = before − the gas',
                                          'sentence': 'Cover the left part and you are left with '
                                                      'the whole bar and the gas — take the gas '
                                                      'away from the whole.'},
                                 'gas': {'result': 'the gas = before − left in the flask',
                                         'sentence': 'Cover the gas and you are left with the '
                                                     'whole bar and what stayed behind — take one '
                                                     'away from the other. This is the one an open '
                                                     'flask asks you for.'}},
                     'close': 'Two parts side by side make the whole. Cover the part you want and '
                              'take the other one away from the whole.'}},
          {'type': 'worked-example', 'id': 'magnesium-worked'},
          {'type': 'check', 'id': 'your-four-steps', 'anchor': 's-build'},
          {'type': 'key-fact', 'ref': 'rearranged-never-made'},
          {'type': 'keyword',
           'anchor': 's-words',
           'eyebrow': 'Five words',
           'lead': 'Say your answer out loud before you turn each card over. If you cannot say it, '
                   'you do not know it yet.',
           'terms': ['Conservation of mass',
                     'Chemical reaction',
                     'Product',
                     'Closed system',
                     'Mass']},
          {'type': 'misconception',
           'id': 'think-commit-burning',
           'anchor': 's-think',
           'targets': 'ATOM-11'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'rearranged-never-made',
                'text': 'Atoms are rearranged in a reaction, never created or destroyed. If the '
                        'mass appears to change, a gas has come in from the air or escaped into '
                        'it.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'vocabulary': [{'term': 'Conservation of mass',
                 'definition': 'The total mass of everything before a reaction is equal to the '
                               'total mass of everything after it.',
                 'note': 'It holds because atoms are only rearranged. Everything means the gases '
                         'too.'},
                {'term': 'Chemical reaction',
                 'definition': 'A change in which atoms are rearranged into different substances.',
                 'note': 'No atom is created, destroyed or turned into another kind.'},
                {'term': 'Product',
                 'definition': 'A substance a reaction makes.',
                 'note': 'Burning wax makes carbon dioxide and water vapour. Both are products, '
                         'and both have mass.'},
                {'term': 'Closed system',
                 'definition': 'A container nothing can get into or out of, so everything that '
                               'takes part is on the balance.',
                 'note': 'A sealed flask is one. An open flask is not, and that is the whole '
                         'difference between the two readings.'},
                {'term': 'Mass',
                 'definition': 'How much substance there is, measured on a balance in grams.',
                 'note': 'Gases have mass. Heat and light do not — they are not made of atoms.'}],
 'activities': [{'id': 'magnesium-worked',
                 'kind': 'worked-example',
                 'demand': 'explain',
                 'eyebrow': 'Worked example · one step at a time',
                 'heading': '2.40 g of magnesium burns and leaves 4.00 g of white powder.',
                 'head_counter': {'format': 'Step {n} of 4', 'total': 4},
                 'staged': True,
                 'buttons': {'first': 'Show the first step',
                             'next': 'Show the next step',
                             'done': 'All four shown',
                             'done_note': 'Now the same four steps on the other reaction.'},
                 'fifa': [{'letter': 'F',
                           'label': 'Formula',
                           'line': 'total mass before = total mass after',
                           'note': 'Nothing is created and nothing is destroyed. Everything has to '
                                   'be counted, including the gas.'},
                          {'letter': 'I',
                           'label': 'Insert',
                           'line': '2.40 g + mass of oxygen = 4.00 g',
                           'note': 'The magnesium was weighed; the oxygen came from the air and '
                                   'was not.'},
                          {'letter': 'F',
                           'label': 'Fine-tune',
                           'line': 'mass of oxygen = 4.00 − 2.40',
                           'note': 'Cover the part you want on the bar. Rearranged so the unknown '
                                   'is on its own, with both masses in grams.'},
                          {'letter': 'A',
                           'label': 'Answer',
                           'line': '1.60 g of oxygen joined from the air',
                           'note': 'The powder is heavier than the metal because it contains '
                                   'something that was not on the balance to start with.'}]},
                {'id': 'think-commit-burning',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ATOM-11',
                 'prompt': 'This is the same wrong idea you met when a puddle dried up, wearing '
                           'different clothes. Commit before you read on.',
                 'options': ['Burning uses a fuel up, so the mass really is destroyed and gone',
                             'The mass leaves as gases, and the products weigh more than the fuel '
                             'did',
                             'Heat has weight of its own, so the mass turns into heat and escapes',
                             'Gases weigh nothing, so all of the mass stays behind in the ash'],
                 'reveal': ['Heat and light are not made of atoms, so nothing that leaves as heat '
                            'or light can account for a gram of anything. Burn 60 g of candle wax '
                            'in a sealed box and weigh the box afterwards: it reads exactly what '
                            'it read before, warm or not.',
                            'What actually happens is that the wax joins with oxygen from the air '
                            'and leaves as carbon dioxide and water vapour — which together weigh '
                            '<strong>more</strong> than the wax did. The reason it looks like '
                            'destruction is that the products are invisible and they float away. '
                            'Put a lid on and the illusion goes with them.']},
                {'eyebrow': 'At the bench · two reactions, two vessels',
                 'heading': 'The balance reports. It does not explain.',
                 'head_counter': {'format': '{n} of 3 runs done', 'total': 3},
                 'done_at': 3,
                 'demand': 'investigate',
                 'targets': 'ATOM-11',
                 'prompt': 'One reaction gives off a gas and one takes a gas in. Run each of them '
                           'open to the air and then sealed, and read what the balance says.',
                 'gate': {'prompt': 'Commit first. Marble chips react with acid in an open flask, '
                                    'fizzing hard. What does the balance do?',
                          'options': ['The reading goes down',
                                      'The reading goes up',
                                      'The reading does not change',
                                      'It goes up while it fizzes, then back down']},
                 'reactions': [{'id': 'marble', 'label': 'Marble chips and acid'},
                               {'id': 'magnesium', 'label': 'Burning magnesium'}],
                 'vessels': [{'id': 'open', 'label': 'Open flask'},
                             {'id': 'sealed', 'label': 'Sealed flask'}],
                 'start_vessel': 'open',
                 'labels': {'reaction': 'Reaction',
                            'vessel': 'Vessel',
                            'unit': 'g',
                            'unmeasured': '—',
                            'before_tag': 'BEFORE',
                            'after_tag': 'AFTER',
                            'open': 'open flask',
                            'sealed': 'sealed flask',
                            'status_idle': 'The balance is zeroed with everything on it, flask '
                                           'included.',
                            'status_done': 'Read the two numbers, then change something and run it '
                                           'again.',
                            'idle_note': 'Nothing has happened yet. The display shows the mass of '
                                         'the whole apparatus before the reaction starts.'},
                 'run_labels': {'idle': 'Start the reaction', 'done': 'Reaction finished'},
                 'liquid_colours': {'marble': 'rgba(143,183,255,0.35)',
                                    'magnesium': 'rgba(255,197,61,0.28)'},
                 'gas_labels': {'out': 'gas leaving the flask',
                                'in': 'oxygen joining from the air'},
                 'alt': {'template': 'A flask on a top-pan balance, {vessel}. The display reads '
                                     '{mass} grams {when} the reaction.',
                         'open': 'open to the air',
                         'sealed': 'sealed with a bung',
                         'before': 'before',
                         'after': 'after'},
                 'decimals': 2,
                 'tiles': [{'id': 'before', 'label': 'Mass before'},
                           {'id': 'after', 'label': 'Mass after'},
                           {'id': 'gone',
                            'label': 'Where it went',
                            'body': 'not measured — you work it out'}],
                 'runs': {'marble:open': {'before': 152.0,
                                          'after': 149.8,
                                          'gas': 'out',
                                          'note': 'The balance falls by 2.20 g. Carbon dioxide is '
                                                  'bubbling out of the flask and into the room, '
                                                  'and it has mass — the reading is not wrong, the '
                                                  'weighing is incomplete.'},
                          'marble:sealed': {'before': 152.0,
                                            'after': 152.0,
                                            'gas': 'none',
                                            'note': 'Exactly the same reading. The gas is still '
                                                    'made, and it is still in the flask, so it is '
                                                    'still on the balance. Nothing about the '
                                                    'reaction changed; what changed is how much of '
                                                    'it you weighed.'},
                          'magnesium:open': {'before': 84.6,
                                             'after': 86.2,
                                             'gas': 'in',
                                             'note': 'The balance rises by 1.60 g. Nothing was '
                                                     'added by hand — oxygen from the air has '
                                                     'joined the magnesium, and it weighs '
                                                     'something.'},
                          'magnesium:sealed': {'before': 250.0,
                                               'after': 250.0,
                                               'gas': 'none',
                                               'note': 'No change. The oxygen that joins the '
                                                       'magnesium was already inside the sealed '
                                                       'flask and already on the balance, so '
                                                       'moving it from the air into the powder '
                                                       'changes nothing.'}},
                 'id': 'open-and-sealed',
                 'kind': 'balance-bench'},
                {'ground': 'inset',
                 'eyebrow': 'Your turn · the same four steps',
                 'heading': 'Marble and acid, open flask: 152.00 g before, 149.80 g after.',
                 'demand': 'construct',
                 'prompt': 'Work out the mass of gas that left the flask. Commit to each line, '
                           'then open the worked version.',
                 'picks': [{'label': 'Step 1 · The rule',
                            'options': ['total mass before = total mass after',
                                        'mass of solid before = mass of solid after',
                                        'mass after = mass before + mass of gas']},
                           {'label': 'Step 2 · Insert',
                            'options': ['152.00 = 149.80 + mass of gas',
                                        '149.80 = 152.00 + mass of gas',
                                        'mass of gas = 152.00 + 149.80']}],
                 'field': {'label': 'Steps 3 and 4 · Work it out, then answer',
                           'hint': 'Your answer as a number',
                           'placeholder': '0.00',
                           'unit_hint': 'Unit',
                           'unit_placeholder': 'choose a unit',
                           'units': ['g', 'kg', 'cm³', 'N']},
                 'button': 'Show the four steps',
                 'progress': {'format': '{n} of 3 lines committed', 'done': 'Opened'},
                 'reveal_head': 'The open flask, done four ways',
                 'steps': [{'letter': 'F',
                            'label': 'Formula',
                            'line': 'total mass before = total mass after',
                            'note': 'The gas counts, even though it has left the flask.'},
                           {'letter': 'I',
                            'label': 'Insert',
                            'line': '152.00 = 149.80 + mass of gas',
                            'note': 'Everything that started on the balance is on the left; '
                                    'everything that ended up anywhere is on the right.'},
                           {'letter': 'F',
                            'label': 'Fine-tune',
                            'line': 'mass of gas = 152.00 − 149.80',
                            'note': 'Cover the gas on the bar. Rearranged so the unknown is alone, '
                                    'and both masses are already in grams.'},
                           {'letter': 'A',
                            'label': 'Answer',
                            'line': 'mass of gas = 2.20 g',
                            'note': 'That is carbon dioxide, now in the room. Seal the flask and '
                                    'those 2.20 g stay on the balance.'}],
                 'close': {'template': 'You wrote {answer} {unit}. The worked answer is 2.20 g.',
                           'blank': '—'},
                 'id': 'your-four-steps',
                 'kind': 'fifa-pick'}],
 'ladder': {'recall': {'q': '18 g of a metal reacts completely with 32 g of sulfur in a sealed '
                            'tube. What mass of metal sulfide is made?',
                       'options': ['14 g',
                                   '32 g',
                                   '50 g',
                                   'It cannot be worked out without knowing the metal'],
                       'answer': 2,
                       'feedback': {0: 'That is 32 − 18. Nothing has been taken away here; the two '
                                       'substances joined.',
                                    1: 'That is the sulfur alone. The metal is still in the tube '
                                       'and still has mass.',
                                    3: 'Conservation of mass does not care which metal it is. '
                                       'Everything that went in is still in the sealed tube.'}},
            'apply': {'q': 'An iron nail is weighed, left to rust for a month, and weighed again. '
                           'It is heavier. Why?',
                      'options': ['Rust is denser than iron',
                                  'Oxygen from the air has joined the iron, and it has mass',
                                  'Water has been absorbed into the metal',
                                  'Mass is not conserved when something is left for a long time'],
                      'answer': 1,
                      'feedback': {0: 'Density is mass in a given space. The balance measures '
                                      'mass, and mass does not increase by rearranging what is '
                                      'already there.',
                                   2: 'Water speeds rusting up, but the extra mass is oxygen that '
                                      'has chemically joined the iron.',
                                   3: 'Time changes nothing. The nail was simply never a closed '
                                      'system — the air was part of the reaction all along.'}},
            'explain': {'q': 'A candle is weighed, burnt for an hour, and weighed again. It has '
                             'lost 12 g. Explain where the 12 g went, and describe an experiment '
                             'that would prove you right.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The wax has reacted with…',
                        'success': ['Says the wax reacted with oxygen from the air.',
                                    'Says the products are gases — carbon dioxide and water vapour '
                                    '— which floated away.',
                                    'Says the gases have mass, and that they were not weighed.',
                                    'Says the total mass of the products is more than 12 g, '
                                    'because the oxygen is in them too.',
                                    'Describes burning the candle in a sealed container and '
                                    'weighing the whole thing before and after.']},
            'produce': {'q': 'A sealed bag of steel wool is weighed, shaken and left until the '
                             'wool has rusted, then weighed again. Predict the reading, then say '
                             'what would be different if the bag had a small hole in it, and '
                             'explain both.',
                        'field_label': 'Your answer',
                        'placeholder': 'In the sealed bag the reading would…',
                        'success': ['Predicts no change in the sealed bag.',
                                    'Says the oxygen that joins the iron was already inside the '
                                    'bag and already on the balance.',
                                    'Says with a hole the reading would go up.',
                                    'Explains that more oxygen can be drawn in from outside '
                                    'through the hole.',
                                    'States conservation of mass as the reason both readings make '
                                    'sense.']}},
 'key_note': 'Total mass before a reaction equals total mass after it, because atoms are only '
             'rearranged. In an open vessel a gas can leave or join, so the balance changes; seal '
             'the vessel and it never does.',
 'stretch': [{'type': 'explainer',
              'id': 'phlogiston',
              'text': 'For two hundred years chemists explained burning by saying that a substance '
                      'called phlogiston escaped from things as they burnt. It fitted: burning '
                      'wood loses mass, and a candle goes out in a sealed jar because the air is '
                      'full of phlogiston and cannot take any more. Then someone weighed a burning '
                      'metal carefully, found it got <em>heavier</em>, and the theory needed '
                      'phlogiston to have negative mass. That is the point at which a model stops '
                      'being repairable — and the weighing had been possible the whole time.'}],
 'support': [],
 'safety_note': 'Burning magnesium is dangerously bright. Never look straight at it, and never '
                'seal a flask that is being heated.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Not sure why a sealed flask behaves differently?',
           'cta': 'Ask about this lesson',
           'anchor': 's-balance'},
 'ks4_becomes': 'Balancing equations by mass, reacting masses, and calculating what a reaction can '
                'produce.',
 'ws': ['measurement', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
