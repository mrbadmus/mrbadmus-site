# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C7 `exothermic-reactions` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C7'
SOURCE_SLUG = 'exothermic-reactions'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'exothermic-reactions',
 'title': 'Exothermic reactions',
 'discipline': 'chemistry',
 'unit': 'energy-changes-in-reactions',
 'family': 'PROCESS',
 'covers': ['KS3.C.ENER.02a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'energy', 'level': 3}, {'id': 'substances-and-reactions', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['energy-and-changes-of-state'],
 'assumes': [],
 'references': ['neutralisation', 'acid-plus-metal', 'oxidation'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Some changes make their surroundings hot, from a campfire to a hand warmer. '
                 'Where does that heat come from?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'The hand warmer',
           'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Five beakers',
           'done_when': 'all_five_run'},
          {'anchor': 's-uses',
           'short': 'USES',
           'label': 'Three judgements',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Starting versus running',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A hand warmer is a sealed plastic pouch. Snap the metal disc inside and '
                         'it reaches 50 °C, in a pocket, on a cold day.',
                'prompt': 'No battery, no flame, nothing plugged in. The pouch was at the same '
                          'temperature as the room a moment before. It stays hot for about an '
                          'hour, then goes cold, and it can be reset by boiling it.',
                'commit': 'If you had to guess, does the warmth come from your body heat in the '
                          'pocket, or from inside the pouch?',
                'options': ['Your body heat', 'Inside the pouch'],
                'reveal': 'A change that gives energy out to its surroundings like this is called '
                          '<strong>exothermic</strong>.',
                'guess': True,
                'replies': ['A pocket is warm. But the pouch started at room temperature, cooler '
                            'than you, and it still got hotter than your body.',
                            'The pouch heats itself. Snapping the disc starts a change inside, and '
                            'energy that was stored in the chemicals comes out as heat.'],
                'answer': 1},
 'misconceptions': [{'id': 'ENER-03',
                     'statement': 'A reaction that needs heating to start cannot be exothermic.',
                     'elicited_by': 'think-commit-spark',
                     'confronted_by': 'think-commit-spark'},
                    {'id': 'ENER-04',
                     'statement': 'Chemical reactions create energy.',
                     'elicited_by': 'use-fireworks',
                     'confronted_by': 'use-fireworks-reveal'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'An <strong>exothermic</strong> change transfers energy to its surroundings. '
                   'The surroundings get warmer — which is why the test for one is a thermometer '
                   'in the beaker, not in the flame.'},
          {'type': 'explainer',
           'text': 'Most reactions you have met are exothermic. Combustion, neutralisation, '
                   'respiration, a metal reacting with acid, and every reaction in the '
                   'displacement grid gave out energy. It is common enough that people forget it '
                   'needs explaining at all.'},
          {'type': 'check', 'id': 'bench-five', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'energy-out'},
          {'type': 'check', 'id': 'uses-exo', 'anchor': 's-uses'},
          {'type': 'keyword',
           'anchor': 's-words',
           'eyebrow': 'Five words',
           'lead': 'Say your answer out loud before you turn each card over. If you cannot say it, '
                   'you do not know it yet.',
           'terms': ['Exothermic',
                     'Surroundings',
                     'Chemical store',
                     'Combustion',
                     'Neutralisation']},
          {'type': 'misconception',
           'id': 'think-commit-spark',
           'anchor': 's-think',
           'targets': 'ENER-03'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'energy-out',
                'text': 'An exothermic change gives energy out to its surroundings, so the '
                        'temperature of the mixture rises. The energy was stored in the chemicals '
                        'before the reaction started.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-spark',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ENER-03',
                 'prompt': 'A Bunsen really is needed to light the magnesium. Commit before you '
                           'read on.',
                 'options': ['Right — a reaction that needs energy put in cannot be giving energy '
                             'out',
                             'Wrong — the spark only starts it; far more energy comes out than '
                             'went in',
                             'Right, because the Bunsen is the real source of the heat you feel',
                             'Wrong — a truly exothermic reaction would never need starting in the '
                             'first place'],
                 'reveal': ['Starting a reaction and running it are two different accounts. Petrol '
                            'needs a spark; a match needs striking; magnesium needs a flame. That '
                            'initial energy gets the reaction going — and once it is going, it '
                            'gives out far more than the spark ever supplied, which is why the '
                            'flame keeps burning after you take the match away.',
                            'The test is the balance, not the beginning. <strong>Exothermic means '
                            'more energy comes out than went in.</strong> If the spark were the '
                            'whole story, a car would need to be lit continuously — and a forest '
                            'fire would go out the moment the lightning stopped.']},
                {'eyebrow': 'Your turn · five beakers, one thermometer',
                 'heading': 'Predict the temperature change, then run it.',
                 'demand': 'investigate',
                 'head_counter': {'format': '{n} of {total} run', 'start': 0, 'total': 5},
                 'prompt': 'Four of these five do the same thing. Run all five — the odd one out '
                           'is the point. The temperatures are typical classroom values chosen to '
                           'show the pattern, not readings from one particular afternoon.',
                 'reactions': [{'id': 'x1',
                                'label': 'Burning magnesium',
                                'start': 21,
                                'end': 60,
                                'exo': True,
                                'setup': 'A coil of magnesium ribbon lowered into a beaker of '
                                         'water, lit at the top with a Bunsen. Thermometer in the '
                                         'water.',
                                'why': 'Combustion, and one of the fiercest exothermic reactions '
                                       'in a school lab. It needed a flame to start — and then '
                                       'gave out enough energy to be dangerous to look at '
                                       'directly.'},
                               {'id': 'x2',
                                'label': 'Acid + alkali',
                                'start': 20,
                                'end': 27,
                                'exo': True,
                                'setup': '25 cm³ of hydrochloric acid with 25 cm³ of sodium '
                                         'hydroxide stirred in. Thermometer in the mixture.',
                                'why': 'Neutralisation is exothermic, and you noticed this without '
                                       'being told: the beaker warmed while you were titrating in '
                                       'the acids unit. A rise of seven degrees from two clear '
                                       'liquids that look unchanged afterwards.'},
                               {'id': 'x3',
                                'label': 'Magnesium + acid',
                                'start': 20,
                                'end': 34,
                                'exo': True,
                                'setup': 'A strip of magnesium dropped into 25 cm³ of dilute '
                                         'hydrochloric acid. Thermometer in the acid.',
                                'why': 'A metal reacting with an acid is strongly exothermic. This '
                                       'is the reaction that produced the squeaky pop, and the '
                                       'warm tube was evidence you had already collected without '
                                       'naming it.'},
                               {'id': 'x4',
                                'label': 'Hand warmer',
                                'start': 21,
                                'end': 50,
                                'exo': True,
                                'setup': 'A commercial reusable hand warmer, snapped and placed '
                                         'against the thermometer bulb.',
                                'why': 'Sodium ethanoate crystallising out of a supersaturated '
                                       'solution. Not strictly a chemical reaction — it is a '
                                       'change of state — but the energy accounting is identical: '
                                       'the particles fall together and release what was stored.'},
                               {'id': 'x5',
                                'label': 'Citric acid + baking soda',
                                'start': 20,
                                'end': 12,
                                'exo': False,
                                'setup': 'Citric acid solution with sodium hydrogencarbonate '
                                         'stirred in. Thermometer in the mixture.',
                                'why': 'The temperature fell by eight degrees. Energy went from '
                                       'the surroundings into the reaction rather than out of it — '
                                       'the opposite of every other beaker on this bench, and the '
                                       'subject of the next lesson.'}],
                 'setup_label': 'The set-up',
                 'predict': {'prompt': 'Predict before you run it.',
                             'options': [{'id': 'up', 'label': 'Temperature rises'},
                                         {'id': 'same', 'label': 'No change'},
                                         {'id': 'down', 'label': 'Temperature falls'}]},
                 'start_label': 'Start',
                 'peak_label': 'Highest reading',
                 'arrow_word': 'rises to',
                 'label_exo': 'exothermic',
                 'label_not_exo': 'not exothermic',
                 'close_id': 'bench-close',
                 'close_title': 'Four went up. One went down.',
                 'close': ['Combustion, neutralisation, metal with acid and the hand warmer all '
                           'warmed their surroundings — they are exothermic, and between them they '
                           'cover most of the chemistry you have done so far. The fifth got '
                           'colder, which means energy went the other way. That one has its own '
                           'name and its own lesson.',
                           'Note what the thermometer is actually in. <strong>It is in the '
                           'mixture, and it is reading the surroundings getting warmer.</strong> '
                           'Exothermic is defined by what happens outside the reaction, not inside '
                           'it.'],
                 'id': 'bench-five',
                 'kind': 'temp-bench'},
                {'eyebrow': 'Three judgements',
                 'heading': 'Exothermic on purpose, and exothermic by accident',
                 'demand': 'classify',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0, 'total': 3},
                 'uses': [{'id': 'use-rust',
                           'correct': 'a',
                           'q': 'A disposable hand warmer contains iron powder, salt and sawdust, '
                                'and gets warm when the packet is opened to the air. What is the '
                                'reaction?',
                           'options': [{'id': 'a', 'label': 'The iron rusting'},
                                       {'id': 'b', 'label': 'The salt dissolving'},
                                       {'id': 'c', 'label': 'The sawdust burning'}],
                           'answer': 'The iron oxidising — rusting, deliberately made fast. Salt '
                                     'speeds it up and the sawdust holds everything in contact '
                                     'with air. Rusting is exothermic like any oxidation; normally '
                                     'it is so slow that the energy escapes unnoticed, and the '
                                     'trick here is simply making it fast enough to feel.'},
                          {'id': 'use-engines',
                           'correct': 'b',
                           'q': 'Why do power stations, cars and your own body all rely on '
                                'exothermic reactions?',
                           'options': [{'id': 'a',
                                        'label': 'They are the only reactions that work'},
                                       {'id': 'b',
                                        'label': 'Because energy given out can be used to do '
                                                 'something'},
                                       {'id': 'c', 'label': 'Because they are cheaper'}],
                           'answer': 'Because getting energy out is the entire point. A power '
                                     'station burns fuel, a car burns petrol, and your cells '
                                     'respire glucose — three very different settings running the '
                                     'same accounting. An endothermic reaction would take energy '
                                     'in, which is useful for cooling but no use for driving '
                                     'anything.'},
                          {'id': 'use-fireworks',
                           'correct': 'b',
                           'q': 'A student says fireworks prove chemical reactions create energy. '
                                'Are they right?',
                           'options': [{'id': 'a', 'label': 'Yes'},
                                       {'id': 'b',
                                        'label': 'No — the energy was already stored in the '
                                                 'chemicals'},
                                       {'id': 'c', 'label': 'Only for large fireworks'}],
                           'answer': 'No, and this is the important sentence in the lesson. Energy '
                                     'cannot be created. It was stored in the chemicals before the '
                                     'firework was lit, and the reaction released it as light, '
                                     'heat and sound. The firework is a container for energy that '
                                     'was put there when it was manufactured — the same accounting '
                                     'as a battery.'}],
                 'id': 'uses-exo',
                 'kind': 'energy-uses'}],
 'ladder': {'recall': {'q': 'What happens to the temperature of the surroundings during an '
                            'exothermic change?',
                       'options': ['It falls, because the reaction takes energy in',
                                   'It stays the same, because energy is conserved',
                                   'It rises, because energy is transferred out of the reaction',
                                   'It rises only if the reaction is lit with a flame'],
                       'answer': 2,
                       'feedback': {0: 'That describes an endothermic change — the next lesson.',
                                    1: 'Energy is conserved, but it moves. Conservation does not '
                                       'mean nothing happens.',
                                    3: 'A hand warmer needs no flame and still warms its '
                                       'surroundings.'}},
            'apply': {'q': 'Burning methane needs a spark to start. Does that make it endothermic?',
                      'options': ['Yes, because energy has to be supplied before it will start',
                                  'It is endothermic at first and exothermic once the flame '
                                  'catches',
                                  'It depends how big the spark is compared with the fuel',
                                  'No — far more energy comes out than the spark put in'],
                      'answer': 3,
                      'feedback': {0: 'Supplying a start is not the same as the reaction taking '
                                      'energy in overall. The flame keeps burning after the spark '
                                      'is gone.',
                                   1: 'The reaction is exothermic throughout. The spark only gets '
                                      'the first molecules going.',
                                   2: 'The size of the spark changes nothing about the energy the '
                                      'reaction releases.'}},
            'explain': {'q': 'A student mixes an acid and an alkali and the thermometer rises by 7 '
                             '°C. Explain what this shows, where the energy came from, and why the '
                             'beaker cools down again after a few minutes.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The temperature rise shows…',
                        'success': ['Says the temperature rise shows the reaction is exothermic.',
                                    'Says energy has been transferred from the reaction to the '
                                    'surroundings.',
                                    'Says the energy was stored in the chemicals beforehand, not '
                                    'created.',
                                    'Says the reaction finishes, so no more energy is released.',
                                    'Says the warm beaker then loses heat to the room until it '
                                    'reaches room temperature.']},
            'produce': {'q': 'A company wants to sell a self-heating food can. Explain what they '
                             'need from the chemistry, and give two safety problems they would '
                             'have to solve.',
                        'field_label': 'Your answer',
                        'placeholder': 'They need a reaction that…',
                        'success': ['Says they need an exothermic reaction.',
                                    'Says it must release enough energy to warm the food to a '
                                    'useful temperature.',
                                    'Says it must not get so hot that it burns the user or bursts '
                                    'the can.',
                                    'Says the reactants must be kept separate until the user '
                                    'starts it.',
                                    'Says the chemicals must not contaminate the food, or must be '
                                    'sealed away from it.']}},
 'key_note': 'An exothermic change transfers energy to the surroundings, so the temperature of the '
             'mixture rises. Combustion, neutralisation, respiration and metals reacting with '
             'acids are all exothermic. Needing energy to get started does not stop a reaction '
             'being exothermic — what matters is that more energy comes out than went in.',
 'stretch': [{'type': 'explainer',
              'id': 'self-heating-cans',
              'text': 'Self-heating cans of coffee use the reaction between calcium oxide and '
                      'water, which is exothermic enough to bring a drink to serving temperature '
                      'in three minutes from a chemical reaction in a sealed compartment. The same '
                      'reaction is a genuine hazard on building sites: quicklime dust in a wet eye '
                      'releases its energy exactly where you would least want it.'},
             {'type': 'explainer',
              'id': 'compost-and-hay',
              'text': 'Compost heaps are exothermic on a scale that surprises people. Bacteria '
                      'respiring their way through grass cuttings release enough energy to hold '
                      'the middle of a heap at 60 °C through a frost, and a large enough '
                      'badly-managed pile of hay can reach the point of catching fire on its own. '
                      'Farmers have lost barns to it. The energy is coming out of the chemical '
                      'store in the plant material, and it makes no difference to the arithmetic '
                      'that the reaction is being run by bacteria rather than a Bunsen.'}],
 'support': [],
 'vocabulary': [{'term': 'Exothermic',
                 'definition': 'A change that transfers energy out to its surroundings, so the '
                               'surroundings get warmer.',
                 'note': 'The test is a thermometer in the mixture, not in the flame.'},
                {'term': 'Surroundings',
                 'definition': 'Everything that is not the reaction itself — the water, the '
                               'beaker, the bench and the air. It is the surroundings whose '
                               'temperature you measure.',
                 'note': 'Exothermic and endothermic are defined by what happens to these, not by '
                         'what happens inside the reaction.'},
                {'term': 'Chemical store',
                 'definition': "Energy held in the way a substance's particles are arranged. A "
                               'reaction can release it or take more in, but nothing creates it.',
                 'note': 'A firework is a container for energy that was put there when it was '
                         'made.'},
                {'term': 'Combustion',
                 'definition': 'A substance reacting with oxygen and releasing energy. Every '
                               'combustion is exothermic.',
                 'note': 'Needing a flame to start is not the same as taking energy in overall.'},
                {'term': 'Neutralisation',
                 'definition': 'An acid reacting with an alkali to make a salt and water. It is '
                               'exothermic, which is why the beaker warms.'},
                {'term': 'Energy transfer',
                 'definition': 'Energy moving from one place to another. It is never created and '
                               'never destroyed, so every temperature change is energy going '
                               'somewhere.'}],
 'safety_note': 'These are demonstrations. Burning magnesium is blinding to look at directly and '
                'is watched through the eye protection everyone in the room is already wearing. A '
                'reusable hand warmer is reset by boiling it in a pan of water on a hob, never in '
                'a microwave and never by an unsupervised student.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why a match does not disprove this?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Energy level diagrams, activation energy, and bond breaking and making as the '
                'reason a reaction gives energy out.',
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
