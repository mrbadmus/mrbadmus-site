# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C7 `endothermic-reactions` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C7'
SOURCE_SLUG = 'endothermic-reactions'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'endothermic-reactions',
 'title': 'Endothermic reactions',
 'discipline': 'chemistry',
 'unit': 'energy-changes-in-reactions',
 'family': 'CONTRAST',
 'covers': ['KS3.C.ENER.02b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'energy', 'level': 3}, {'id': 'substances-and-reactions', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['exothermic-reactions'],
 'assumes': [],
 'references': ['the-photosynthesis-reaction',
                'aerobic-respiration',
                'thermal-decomposition',
                'changes-of-state'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Two powders, both at room temperature, stirred together in a beaker. Thirty '
                 'seconds later the thermometer has fallen from 20 °C to 12 °C, and nothing was '
                 'cooled.',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'The cold beaker',
           'done_when': 'committed'},
          {'anchor': 's-compare',
           'short': 'SORT',
           'label': 'Eight changes',
           'done_when': 'all_eight_sorted'},
          {'anchor': 's-uses',
           'short': 'USES',
           'label': 'Cold on demand',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think', 'short': 'THINK', 'label': 'Making cold', 'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Nothing was cooled. Nothing was refrigerated. The beaker got cold on its '
                         'own.',
                'prompt': 'Citric acid and sodium hydrogencarbonate, both at 20 °C, both dry, are '
                          'stirred into water. The thermometer falls to 12 °C — eight degrees '
                          'down, the same drop the fifth beaker made in the last lesson — and the '
                          'outside of the beaker mists over cold.',
                'commit': 'If you had to guess, what happened to the heat that left the water?',
                'options': ['It simply disappeared for good', 'The chemicals took it in'],
                'reveal': 'A change that takes energy in from its surroundings like this is called '
                          '<strong>endothermic</strong>: last lesson run in reverse.',
                'guess': True,
                'replies': ['It looks that way, since the thermometer only reads what is left in '
                            'the water. But energy is never destroyed, only moved.',
                            'The reaction needed energy to go ahead, and it took it from the '
                            'water, the beaker and the air. They lost energy, so they got colder.'],
                'answer': 1},
 'misconceptions': [{'id': 'ENER-05',
                     'statement': 'An endothermic reaction produces cold.',
                     'elicited_by': 'think-commit-cold',
                     'confronted_by': 'think-commit-cold'},
                    {'id': 'ENER-06',
                     'statement': 'Melting and freezing both take energy in, because both involve '
                                  'ice.',
                     'elicited_by': 'sort-eight',
                     'confronted_by': 'sort-close'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'An <strong>endothermic</strong> change takes energy in from its surroundings, '
                   'so the surroundings get colder. The thermometer falls, and nothing has been '
                   'refrigerated.'},
          {'type': 'explainer',
           'text': 'Both kinds obey the same law. Energy is never created and never destroyed — it '
                   'is transferred. Exothermic moves it out of the chemicals and into the '
                   'surroundings; endothermic moves it the other way. <strong>The only question is '
                   'which direction.</strong>'},
          {'type': 'check', 'id': 'sort-eight', 'anchor': 's-compare'},
          {'type': 'key-fact', 'ref': 'which-direction'},
          {'type': 'check', 'id': 'uses-cold', 'anchor': 's-uses'},
          {'type': 'keyword',
           'anchor': 's-words',
           'eyebrow': 'Five words',
           'lead': 'Say your answer out loud before you turn each card over. If you cannot say it, '
                   'you do not know it yet.',
           'terms': ['Endothermic',
                     'Exothermic',
                     'Conservation of energy',
                     'Photosynthesis',
                     'Dissolving']},
          {'type': 'misconception',
           'id': 'think-commit-cold',
           'anchor': 's-think',
           'targets': 'ENER-05'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'which-direction',
                'text': 'Endothermic changes take energy in from the surroundings, so the '
                        'temperature falls. Exothermic changes give it out and the temperature '
                        'rises. Reverse a change and you reverse its energy transfer.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-cold',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ENER-05',
                 'prompt': 'The beaker genuinely does get cold. Commit before you read on.',
                 'options': ['Right — it makes cold and releases it into the beaker',
                             'Wrong — there is no such thing as cold; the reaction removes energy',
                             'Right, because the temperature falls',
                             'Wrong — the beaker only feels cold, it is not really colder'],
                 'reveal': ['There is no such substance as cold. Cold is not a thing that can be '
                            'made, pumped or released — it is simply the absence of energy. The '
                            'reaction did not produce anything; it <strong>took energy '
                            'away</strong>, and what is left behind has less than it did.',
                            'The same correction applies to a fridge, which does not make cold but '
                            'moves energy out of the food and dumps it out of the grille at the '
                            'back. <strong>Every temperature change is energy going somewhere. '
                            'Naming the direction is the whole of this unit.</strong>']},
                {'eyebrow': 'Your turn · eight changes',
                 'heading': 'Exothermic or endothermic? The thermometer decides.',
                 'demand': 'classify',
                 'head_counter': {'format': '{n} of {total} sorted', 'start': 0, 'total': 8},
                 'prompt': 'Four of the eight are endothermic, and three of those four are changes '
                           'you have already met under another name.',
                 'endo_count_claim': 4,
                 'options': [{'id': 'exo', 'label': 'Exothermic'},
                             {'id': 'endo', 'label': 'Endothermic'}],
                 'verdict_exo': 'Exothermic — the surroundings warm.',
                 'verdict_endo': 'Endothermic — the surroundings cool.',
                 'pairs': [['i6', 'i7'], ['i4', 'i5']],
                 'items': [{'id': 'i1',
                            'name': 'Burning natural gas',
                            'where': 'a hob',
                            'endo': False,
                            'why': 'Combustion is exothermic, always. The whole reason for burning '
                                   'anything is the energy it gives out.'},
                           {'id': 'i2',
                            'name': 'Thermal decomposition of copper carbonate',
                            'where': 'a Bunsen',
                            'endo': True,
                            'why': 'Endothermic. The Bunsen has to keep running: take the flame '
                                   'away and the reaction stops, because it can only proceed while '
                                   'energy is being supplied. That is why the decompositions you '
                                   'did with a Bunsen all needed the flame kept on.'},
                           {'id': 'i3',
                            'name': 'Neutralising an acid with an alkali',
                            'where': 'a beaker',
                            'endo': False,
                            'why': 'Exothermic — the mixture warms by several degrees. You '
                                   'measured this in the acids unit without naming it.'},
                           {'id': 'i4',
                            'name': 'Photosynthesis',
                            'where': 'a leaf',
                            'endo': True,
                            'why': 'Endothermic, and the biggest one on the planet. The energy '
                                   'comes from sunlight, which is why a plant in the dark cannot '
                                   'do it however much carbon dioxide and water it has.'},
                           {'id': 'i5',
                            'name': 'Respiration',
                            'where': 'every living cell',
                            'endo': False,
                            'why': 'Exothermic. It is the reverse of photosynthesis, so it '
                                   'releases what photosynthesis stored — and it is why a crowded '
                                   'room warms up.'},
                           {'id': 'i6',
                            'name': 'Ice melting',
                            'where': 'a drink',
                            'endo': True,
                            'why': 'Endothermic. Melting takes energy in, taken from the drink — '
                                   'which is exactly how the ice keeps it cold, as you worked out '
                                   'last lesson.'},
                           {'id': 'i7',
                            'name': 'Water freezing',
                            'where': 'a freezer',
                            'endo': False,
                            'why': 'Exothermic. Freezing is melting run backwards, so the energy '
                                   'runs backwards too: the water gives energy out, and the '
                                   'freezer has to carry it away. That is the heat coming off the '
                                   'back of the appliance.'},
                           {'id': 'i8',
                            'name': 'Ammonium nitrate dissolving',
                            'where': 'a cold pack',
                            'endo': True,
                            'why': 'Endothermic, strongly enough to be sold as a first aid device. '
                                   'Not every dissolving is — some warm up — but this one takes in '
                                   'enough energy to bring water close to freezing.'}],
                 'close_id': 'sort-close',
                 'close_title': 'Look at how lopsided that list is.',
                 'close': ['Most changes give energy out. Endothermic ones are the exceptions, and '
                           'they tend to be the ones that need something driving them — a Bunsen '
                           'under a carbonate, sunlight falling on a leaf, or a solid pulling '
                           'itself apart as it dissolves.',
                           'Notice the pairs. Melting is endothermic and freezing is exothermic; '
                           'photosynthesis is endothermic and respiration is exothermic. '
                           '<strong>Run a change backwards and the energy runs backwards with it, '
                           'by exactly the same amount.</strong>'],
                 'id': 'sort-eight',
                 'kind': 'energy-sorter'},
                {'eyebrow': 'Three judgements',
                 'heading': 'Cold on demand',
                 'demand': 'classify',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0, 'total': 3},
                 'uses': [{'id': 'use-coldpack',
                           'correct': 'b',
                           'q': 'A sports cold pack is squeezed and goes cold in seconds. Why can '
                                'it only be used once?',
                           'options': [{'id': 'a', 'label': 'The chemicals are used up'},
                                       {'id': 'b',
                                        'label': 'The dissolving cannot be reversed inside the '
                                                 'bag'},
                                       {'id': 'c', 'label': 'The bag leaks'}],
                           'answer': 'Because the change cannot be undone in the packet. To reset '
                                     'it you would have to evaporate the water off and recover the '
                                     'solid, which needs a heat source and an open container. '
                                     'Compare the reusable hand warmer from last lesson, which '
                                     'resets by boiling — the difference is whether the reverse '
                                     'change is practical, not whether it is possible.'},
                          {'id': 'use-fuel',
                           'correct': 'b',
                           'q': 'Would an endothermic reaction be any use as a fuel?',
                           'options': [{'id': 'a', 'label': 'Yes, a very efficient one'},
                                       {'id': 'b',
                                        'label': 'No — it takes energy in rather than giving it '
                                                 'out'},
                                       {'id': 'c', 'label': 'Only in an engine'}],
                           'answer': 'No. A fuel is something you burn to get energy out, and an '
                                     'endothermic reaction does the opposite: you would have to '
                                     'keep supplying energy to make it run, and get nothing back. '
                                     'Endothermic reactions are useful for cooling, for storing '
                                     'energy and for taking things apart — not for powering '
                                     'anything.'},
                          {'id': 'use-conservation',
                           'correct': 'b',
                           'q': 'A student claims an endothermic reaction breaks the law of '
                                'conservation of energy, because energy disappears.',
                           'options': [{'id': 'a', 'label': 'They are right'},
                                       {'id': 'b',
                                        'label': 'They are wrong — the energy is stored in the '
                                                 'products'},
                                       {'id': 'c', 'label': 'The law does not apply to chemistry'}],
                           'answer': 'Wrong, and instructively so. The energy has not disappeared: '
                                     'it has been taken out of the surroundings and stored in the '
                                     'new substances, where a thermometer cannot see it. Run the '
                                     'reaction backwards and it comes out again. Nothing is lost — '
                                     'the accounting simply moved to a place the instrument does '
                                     'not read.'}],
                 'id': 'uses-cold',
                 'kind': 'energy-uses'}],
 'ladder': {'recall': {'q': 'What happens to the temperature of the surroundings during an '
                            'endothermic change?',
                       'options': ['It rises, because energy is released',
                                   'It falls, because energy is taken in by the reaction',
                                   'It stays the same',
                                   'It falls, because cold is produced by the reaction'],
                       'answer': 1,
                       'feedback': {0: 'That is exothermic — the previous lesson.',
                                    2: 'If nothing changed there would be nothing to measure. The '
                                       'thermometer falls.',
                                    3: 'The direction is right but the reason is wrong. Cold is '
                                       'not produced; energy is removed.'}},
            'apply': {'q': 'Melting is endothermic. What does that tell you about freezing?',
                      'options': ['It is exothermic — the same energy comes back out',
                                  'It is also endothermic, because both involve ice',
                                  'It involves no energy change at all',
                                  'It depends on how cold the freezer is'],
                      'answer': 0,
                      'feedback': {1: 'They are opposite changes, so the energy travels in '
                                      'opposite directions.',
                                   2: 'A freezer has to remove energy continuously. That energy is '
                                      'coming out of the water.',
                                   3: 'The direction of the transfer is fixed. The freezer '
                                      'temperature affects the rate, not the direction.'}},
            'explain': {'q': 'Two powders at room temperature are stirred into water and the '
                             'temperature falls to 12 °C. Explain what has happened in terms of '
                             'energy, and why it does not break the law of conservation of energy.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The temperature fell because…',
                        'success': ['Says the reaction is endothermic.',
                                    'Says energy has been taken in from the surroundings.',
                                    'Says the surroundings include the water, beaker and air, '
                                    'which therefore cool.',
                                    'Says the energy is now stored in the products.',
                                    'Says no energy has been destroyed — only transferred.']},
            'produce': {'q': 'A designer wants a cold pack that can be reused indefinitely. '
                             'Explain what the chemistry would have to allow, and why the ammonium '
                             'nitrate pack cannot do it.',
                        'field_label': 'Your answer',
                        'placeholder': 'For a pack to be reusable the change would have to…',
                        'success': ['Says the change would have to be reversible.',
                                    'Says reversing it would release the energy that was taken in.',
                                    'Says the reverse change would need energy supplied from '
                                    'outside, such as heating.',
                                    'Says the ammonium nitrate would have to be recovered from '
                                    'solution by evaporating the water.',
                                    'Says that cannot be done inside a sealed bag, unlike the hand '
                                    'warmer which resets by boiling.']}},
 'key_note': 'An endothermic change takes energy in from its surroundings, so the temperature '
             'falls. Thermal decomposition, photosynthesis, melting and many dissolvings are '
             'endothermic; most other changes are exothermic. Energy is never created or destroyed '
             'in either case — only transferred, and reversing a change reverses the transfer.',
 'stretch': [{'type': 'explainer',
              'id': 'cold-packs',
              'text': 'Instant cold packs in a first aid kit are a sealed bag of ammonium nitrate '
                      'with a pouch of water inside it. Squeeze the pack, the pouch bursts, the '
                      'ammonium nitrate dissolves, and the temperature drops to near 0 °C within '
                      'seconds — no freezer, no electricity, and it works on a mountainside. It is '
                      'a single-use device because the dissolving cannot be undone in the bag.'},
             {'type': 'explainer',
              'id': 'photosynthesis-banks-it',
              'text': 'The largest endothermic process on Earth is photosynthesis, and it runs on '
                      'sunlight. Every joule stored in a leaf, and therefore in every food, every '
                      'fuel and every living thing, was taken in by an endothermic reaction '
                      'powered by a star. The exothermic reactions that follow — respiration, '
                      'combustion, digestion — are all spending what photosynthesis banked. The '
                      'whole carbon cycle is one endothermic reaction feeding an enormous number '
                      'of exothermic ones.'}],
 'support': [],
 'vocabulary': [{'term': 'Endothermic',
                 'definition': 'A change that takes energy in from its surroundings, so the '
                               'surroundings get colder.',
                 'note': 'Nothing is refrigerated and no cold is made. Energy is removed.'},
                {'term': 'Exothermic',
                 'definition': 'A change that gives energy out to its surroundings, so the '
                               'surroundings get warmer.',
                 'note': 'Reverse an endothermic change and you get an exothermic one, by exactly '
                         'the same amount.'},
                {'term': 'Conservation of energy',
                 'definition': 'Energy is never created and never destroyed. It can only be moved '
                               'from one store to another.',
                 'note': 'An endothermic reaction does not lose energy — it stores it where a '
                         'thermometer cannot read it.'},
                {'term': 'Photosynthesis',
                 'definition': 'The reaction in which a plant uses light energy to build glucose '
                               'from carbon dioxide and water. It is endothermic.',
                 'note': 'This is why a plant in the dark cannot photosynthesise however much '
                         'water and carbon dioxide it has.'},
                {'term': 'Dissolving',
                 'definition': 'A solute spreading through a solvent to make a solution. Some '
                               'dissolvings take energy in and some give it out.',
                 'note': 'Ammonium nitrate takes enough in to bring water close to freezing.'},
                {'term': 'Reversible change',
                 'definition': 'A change that can be run backwards. Doing so reverses the '
                               'direction of its energy transfer as well.'}],
 'safety_note': 'An instant cold pack is a real first aid device and gets cold enough to injure '
                'skin it is held against directly. It goes on over clothing or a cloth, for short '
                'spells, and a used one is thrown away rather than opened.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why cold is not a substance?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Energy level diagrams for endothermic changes, and bond breaking as the '
                'energy-absorbing half of every reaction.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
