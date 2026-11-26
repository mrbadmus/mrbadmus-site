# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C4 `chemical-vs-physical-change` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C4'
SOURCE_SLUG = 'chemical-vs-physical-change'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'chemical-vs-physical-change',
 'title': 'Chemical change vs physical change',
 'discipline': 'chemistry',
 'unit': 'chemical-reactions',
 'family': 'CONTRAST',
 'covers': ['KS3.C.CR.01a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}, {'id': 'particles', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['proving-something-is-pure'],
 'assumes': [],
 'references': ['dissolving-and-solutions'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Two changes can look identical — the same heat, the same colour change, the same '
                 'disappearing solid — and only one of them makes something new. Which question '
                 'separates them every time?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Chocolate and egg',
           'done_when': 'committed'},
          {'anchor': 's-pairs',
           'short': 'PAIRS',
           'label': 'Three pairs',
           'done_when': 'all_six_decided'},
          {'anchor': 's-chain',
           'short': 'SENTENCE',
           'label': 'One sentence',
           'done_when': 'both_halves_chosen'},
          {'anchor': 's-think', 'short': 'THINK', 'label': 'Undo it', 'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Melt a chocolate bar and it comes back. Fry an egg and nothing brings it '
                         'back.',
                'prompt': 'Both changes were caused by heat. Melting chocolate is a physical '
                          'change. Frying an egg is a chemical change.',
                'commit': 'If you had to guess, what makes frying an egg a chemical change: the '
                          'change of colour, or that something new is made?',
                'options': ['The change of colour', 'Something new is made'],
                'reveal': 'So the test is what you end up with, not how it looks along the way. '
                          'Next: three pairs of changes that look alike.',
                'guess': True,
                'replies': ['A colour change is often a clue. But food colouring stirred into '
                            'water changes colour and makes nothing new. What decides it is that '
                            'the egg is now a different substance.',
                            'A chemical change makes at least one new substance. The fried egg is '
                            'firm and white where the raw egg white was runny and clear.'],
                'answer': 1},
 'misconceptions': [{'id': 'REACT-01',
                     'statement': 'If you can undo it, it is physical. If you cannot undo it, it '
                                  'is chemical.',
                     'elicited_by': 'think-commit-reverse',
                     'confronted_by': 'think-commit-reverse'},
                    {'id': 'REACT-02',
                     'statement': 'Something disappearing into a liquid is always the same kind of '
                                  'change.',
                     'elicited_by': 'pair-2-commit',
                     'confronted_by': 'pair-2-reveal-marble'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'In a <strong>physical change</strong>, the same substances are still there. '
                   'They have moved, changed state, or mixed — and the particles themselves are '
                   'untouched.'},
          {'type': 'explainer',
           'text': 'In a <strong>chemical change</strong> — a <strong>chemical reaction</strong> — '
                   'at least one new substance is made. The atoms are all still there, but they '
                   'have been joined up differently, and what you have now behaves differently '
                   'from what you started with.'},
          {'type': 'check', 'id': 'pairs-three', 'anchor': 's-pairs'},
          {'type': 'key-fact', 'ref': 'new-substance-or-not'},
          {'type': 'comparison',
           'eyebrow': 'Reference · the two columns',
           'statement': 'What each kind of change does and does not do',
           'ground': 'band',
           'columns': [{'caption': 'Physical change'}, {'caption': 'Chemical change'}],
           'row_tones': ['ink', 'ink'],
           'rows': [{'name': 'New substances',
                     'cells': ['No new substance.',
                               'At least one new substance, with different properties.']},
                    {'name': 'The particles',
                     'cells': ['The particles are unchanged — only their arrangement or spacing.',
                               'The atoms are the same atoms, joined up differently.']},
                    {'name': 'Reversing it',
                     'cells': ['Usually easy to reverse, and the same mass comes back.',
                               'Usually hard to reverse, and never by cooling it down.']},
                    {'name': 'Where you meet it',
                     'cells': ['Melting, boiling, dissolving, breaking, mixing.',
                               'Burning, rusting, cooking, acid on marble, respiration.']}]},
          {'type': 'check', 'id': 'chain-wax', 'anchor': 's-chain'},
          {'type': 'misconception',
           'id': 'think-commit-reverse',
           'anchor': 's-think',
           'targets': 'REACT-01'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'new-substance-or-not',
                'text': 'A chemical change makes at least one new substance. A physical change '
                        'does not — the same substances are still there, in a different state or a '
                        'different place.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-reverse',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'REACT-01',
                 'prompt': 'This rule gets the right answer most of the time, which is exactly '
                           'what makes it dangerous. Commit before you read on.',
                 'options': ['A good rule — if you cannot get the starting substances back, '
                             'something new has been made',
                             'Not the test — smashing glass is irreversible and physical, and rust '
                             'can be turned back into iron',
                             'A good rule for solids — a solid that cannot be put back together '
                             'has reacted',
                             'Wrong the other way round — chemical changes are the reversible ones '
                             'and physical changes are the permanent ones'],
                 'reveal': ['Smash a glass and you cannot undo it — and no new substance was made, '
                            'so it is a physical change. It is broken glass, which is glass. '
                            'Meanwhile a rusty nail can be turned back into iron: a steelworks '
                            'does exactly that to iron ore, which is mostly rust, and rusting is '
                            'unquestionably a chemical change.',
                            'Reversibility is about <strong>how hard</strong> the change is to '
                            'undo, and that is a fact about energy and equipment, not about what '
                            'happened to the substances. It is a useful hint and it is not the '
                            'test. <strong>Ask what you have now, not whether you can get '
                            'back.</strong>']},
                {'eyebrow': 'Your turn · three pairs, side by side',
                 'heading': 'Each pair looks alike. In each pair, one is a reaction and one is '
                            'not.',
                 'demand': 'investigate',
                 'prompt': 'Commit on both halves of a pair before you run any tests on it. Then '
                           'read the evidence and see which of your two verdicts survives.',
                 'options': ['Physical', 'Chemical'],
                 'pairs': [{'id': 'p1',
                            'label': 'Pair 1 · both involve a candle and a flame',
                            'sides': [{'id': 'wax-melt',
                                       'name': 'Wax melting',
                                       'what': 'The wax near the flame turns to a clear liquid and '
                                               'runs down the side.',
                                       'chemical': False,
                                       'evidence': [{'test': 'Does it come back?',
                                                     'result': 'It sets again as it cools, into '
                                                               'wax.'},
                                                    {'test': 'New properties?',
                                                     'result': 'Liquid wax and solid wax burn the '
                                                               'same way, smell the same and weigh '
                                                               'the same.'},
                                                    {'test': 'Mass',
                                                     'result': 'The wax that ran down weighs what '
                                                               'it weighed before.'}],
                                       'verdict': 'Physical change.',
                                       'why': 'A change of state. Same substance, different '
                                              'arrangement of the same particles.'},
                                      {'id': 'wax-burn',
                                       'name': 'Wax burning',
                                       'what': 'The wick burns with a yellow flame and the candle '
                                               'gets shorter.',
                                       'chemical': True,
                                       'evidence': [{'test': 'Does it come back?',
                                                     'result': 'Nothing you can do to the air '
                                                               'above the candle turns it back '
                                                               'into wax.'},
                                                    {'test': 'New properties?',
                                                     'result': 'Carbon dioxide and water vapour '
                                                               'come off. Neither is waxy, neither '
                                                               'burns.'},
                                                    {'test': 'Mass',
                                                     'result': 'The candle loses mass — and the '
                                                               'products, if you could weigh them '
                                                               'all, weigh more than the wax did, '
                                                               'because oxygen joined in.'}],
                                       'verdict': 'Chemical change.',
                                       'why': 'The wax has been turned into different substances. '
                                              'The atoms are all still there, joined up '
                                              'differently.'}]},
                           {'id': 'p2',
                            'label': 'Pair 2 · both make a solid vanish into a liquid',
                            'sides': [{'id': 'salt',
                                       'name': 'Salt stirred into water',
                                       'what': 'The crystals disappear and the water stays clear.',
                                       'chemical': False,
                                       'evidence': [{'test': 'Does it come back?',
                                                     'result': 'Evaporate the water and the salt '
                                                               'is back, to the gram.'},
                                                    {'test': 'New properties?',
                                                     'result': 'None that are new. The salt is '
                                                               'still salt — it just cannot be '
                                                               'seen while it is dissolved.'},
                                                    {'test': 'Mass',
                                                     'result': 'Unchanged. 100 g of water plus 10 '
                                                               'g of salt weighs 110 g.'}],
                                       'verdict': 'Physical change.',
                                       'why': 'Dissolving is mixing at the particle scale. Nothing '
                                              'new was made — which is exactly why you could get '
                                              'it back.'},
                                      {'id': 'marble',
                                       'name': 'Marble chips in acid',
                                       'what': 'The chips fizz vigorously and slowly disappear.',
                                       'chemical': True,
                                       'evidence': [{'test': 'Does it come back?',
                                                     'result': 'Evaporate the liquid and you get a '
                                                               'different white solid, not marble '
                                                               'chips.'},
                                                    {'test': 'New properties?',
                                                     'result': 'The gas given off puts out a lit '
                                                               'splint and turns limewater cloudy. '
                                                               'Marble does neither.'},
                                                    {'test': 'Mass',
                                                     'result': 'The open flask gets lighter, '
                                                               'because the gas leaves. Seal it '
                                                               'and the mass does not change at '
                                                               'all.'}],
                                       'verdict': 'Chemical change.',
                                       'why': 'Marble and acid have become a gas, a salt and '
                                              'water. "It dissolved" is the same phrase describing '
                                              'a completely different event.'}]},
                           {'id': 'p3',
                            'label': 'Pair 3 · both change colour, both take time',
                            'sides': [{'id': 'ice',
                                       'name': 'Ice left in a warm room',
                                       'what': 'The clear block goes cloudy at the edges and '
                                               'becomes a puddle.',
                                       'chemical': False,
                                       'evidence': [{'test': 'Does it come back?',
                                                     'result': 'Put the puddle in the freezer and '
                                                               'you have ice again.'},
                                                    {'test': 'New properties?',
                                                     'result': 'Ice and water are the same '
                                                               'substance. Both are water.'},
                                                    {'test': 'Mass',
                                                     'result': 'The puddle weighs what the block '
                                                               'weighed.'}],
                                       'verdict': 'Physical change.',
                                       'why': 'Melting. The particles have not changed at all — '
                                              'they have only broken out of a fixed arrangement.'},
                                      {'id': 'rust',
                                       'name': 'An iron nail left outside',
                                       'what': 'The grey nail turns orange-brown and flakes.',
                                       'chemical': True,
                                       'evidence': [{'test': 'Does it come back?',
                                                     'result': 'Not by cooling or drying. A '
                                                               'steelworks can get iron back from '
                                                               'rust, with a furnace and carbon.'},
                                                    {'test': 'New properties?',
                                                     'result': 'Rust is soft, crumbly and not '
                                                               'magnetic in the way iron is. Iron '
                                                               'is strong and grey.'},
                                                    {'test': 'Mass',
                                                     'result': 'The nail gets heavier. The extra '
                                                               'mass came out of the air.'}],
                                       'verdict': 'Chemical change.',
                                       'why': 'Iron and oxygen have become iron oxide, a new '
                                              'substance with new properties — including being '
                                              'useless as a nail.'}]}],
                 'close': 'Six changes. A solid vanished into a liquid in two of them and only one '
                          'was a reaction. Something got hot in two of them and only one was a '
                          'reaction. Colour changed in two and only one was a reaction. '
                          '<strong>Every clue you can see appears on both sides of the '
                          'line.</strong> The only question that sorted all six was whether the '
                          'substance you ended with was a different substance.',
                 'id': 'pairs-three',
                 'kind': 'change-pairs'},
                {'eyebrow': 'Say it as one sentence',
                 'heading': 'Build the comparison, not two descriptions',
                 'demand': 'construct',
                 'prompt': 'Melting wax and burning wax. Pick one clause for each half — then read '
                           'what a linked comparison has to do that two separate statements do '
                           'not.',
                 'slots': [{'id': 'a',
                            'label': 'First half',
                            'options': ['Melting wax is a physical change because the wax is still '
                                        'wax and cools back to a solid,',
                                        'Melting wax is a physical change because it can be '
                                        'undone,',
                                        'Melting wax turns a solid into a liquid,']},
                           {'id': 'b',
                            'label': 'Second half',
                            'options': ['whereas burning wax is a chemical change because the wax '
                                        'is turned into carbon dioxide and water, which cannot be '
                                        'turned back into wax by cooling.',
                                        'and burning wax is a chemical change.',
                                        'but burning wax gives off heat and light.']}],
                 'ideal': {'a': 0, 'b': 0},
                 'sentence_label': 'Your sentence',
                 'notes': {'ideal': 'That is the sentence. Both halves name the change, both give '
                                    'the reason, and the second half answers the first — the wax '
                                    'is still wax against the wax is now something else. An '
                                    'examiner is looking for the link, and "whereas" is where it '
                                    'lives.',
                           'other': 'Every clause you could pick is true. What decides the marks '
                                    'is whether the two halves are about the same thing: a '
                                    'comparison has to say what is different, not describe two '
                                    'changes and leave the reader to spot it. "It can be undone" '
                                    'and "it gives off heat and light" are both true and neither '
                                    'is the difference — one is a consequence and the other '
                                    'happens in physical changes too.'},
                 'model_label': 'A sentence that would get full marks',
                 'model': 'Melting wax is a physical change because the wax is still wax and cools '
                          'back to a solid, whereas burning wax is a chemical change because the '
                          'wax is turned into carbon dioxide and water, which cannot be turned '
                          'back into wax by cooling.',
                 'id': 'chain-wax',
                 'kind': 'chain-build'}],
 'ladder': {'recall': {'q': 'What single thing tells you that a change is a chemical change?',
                       'options': ['The change cannot be reversed by any means',
                                   'The colour of the substance has changed',
                                   'At least one new substance has been made',
                                   'Heat was needed to make it happen'],
                       'answer': 2,
                       'feedback': {0: 'Smashing a glass cannot be reversed and is physical; '
                                       'rusting can be reversed in a furnace and is chemical.',
                                    1: 'Ice going cloudy and a nail going orange both change '
                                       'colour, and only one of them is a reaction.',
                                    3: 'Melting needs heat and makes nothing new. Rusting needs no '
                                       'heat at all.'}},
            'apply': {'q': 'Salt dissolving in water and marble fizzing in acid are both described '
                           'as "it dissolved". Which pair of verdicts is right?',
                      'options': ['Both physical — in both cases the solid disappears into the '
                                  'liquid',
                                  'Both chemical — the solid is destroyed in both',
                                  'Salt: physical. Marble: chemical.',
                                  'Salt: chemical. Marble: physical.'],
                      'answer': 2,
                      'feedback': {0: 'The marble has become a gas, a salt and water, and the gas '
                                      'can be tested. Something disappearing is not evidence of '
                                      'anything.',
                                   1: 'The salt is not destroyed. Evaporate the water and every '
                                      'gram of it comes back unchanged.',
                                   3: 'Exactly the wrong way round. Test the gas from the marble: '
                                      'it turns limewater cloudy, so it is a new substance.'}},
            'explain': {'q': 'A student heats sugar in a pan. First it melts to a clear syrup; '
                             'then it turns brown, smells of caramel and sets hard. They say "the '
                             'whole thing was one change". Explain how many changes happened, '
                             'which kind each was, and what evidence separates them.',
                        'field_label': 'Your explanation',
                        'placeholder': 'There were two changes. The first…',
                        'success': ['Says there were two changes, not one.',
                                    'Says melting is a physical change — still sugar, and it would '
                                    'set back to sugar on cooling.',
                                    'Says the browning is a chemical change, because new '
                                    'substances with new properties were made.',
                                    'Uses evidence for the second: the new smell, the new colour, '
                                    'and that cooling does not bring the sugar back.',
                                    'Makes the comparison linked, not two separate descriptions — '
                                    'for example using "whereas".']},
            'produce': {'q': 'A cook says "cooking is just heating food up". Take two examples '
                             'from a kitchen — one physical change and one chemical — and use them '
                             'to explain why that sentence is wrong, and why it is easy to '
                             'believe.',
                        'field_label': 'Your answer',
                        'placeholder': 'Boiling a potato is mostly…',
                        'success': ['Names a kitchen change that is physical, and says why no new '
                                    'substance is made.',
                                    'Names a kitchen change that is chemical, and names or '
                                    'describes a new substance.',
                                    'Uses the new-substance test explicitly as the thing that '
                                    'distinguishes them.',
                                    'Explains why the sentence is tempting — heat is involved in '
                                    'both, and both look dramatic.',
                                    'Notes that one of them can be undone and the other cannot, '
                                    'and that this is a consequence rather than the definition.']}},
 'key_note': 'A chemical change makes at least one new substance, with properties the starting '
             'materials did not have. A physical change makes none — the same substances are still '
             'there, melted, dissolved, broken or moved. Bubbling, colour change, heat and '
             'irreversibility are clues that appear on both sides of the line, so none of them is '
             'the test. The test is: what have you got now?',
 'stretch': [{'type': 'explainer',
              'id': 'boundary-cases',
              'text': 'Some changes are genuinely awkward to place, and that is not a flaw in the '
                      'definition — it is what happens at a boundary. Dissolving salt in water is '
                      'physical: the salt is still there and evaporating gets it back. Dissolving '
                      'marble chips in acid is chemical: the marble is gone, replaced by a gas, a '
                      'salt and water. Both are described in everyday speech as "it dissolved", '
                      'and the word is doing two completely different jobs.'},
             {'type': 'explainer',
              'id': 'cooking',
              'text': 'Cooking is the case worth arguing about. Boiling a potato is mostly '
                      'physical — heat and water soften it. Browning a steak is chemical: hundreds '
                      'of new substances form between the amino acids and sugars on the surface, '
                      'which is why it smells of something the raw meat did not. Whipping cream is '
                      'physical, and so is whipping it too far: the fat droplets clump together '
                      'into butter, and nothing new has been made. The same pan can host both '
                      'kinds of change in the same minute.'}],
 'support': [],
 'vocabulary': [{'term': 'substance',
                 'definition': 'One material, with its own properties — water, iron, salt. Two '
                               'different substances behave differently.'},
                {'term': 'property',
                 'definition': 'Something you can find out about a substance by testing it: its '
                               'colour, whether it burns, whether a magnet pulls it.'},
                {'term': 'physical change',
                 'definition': 'A change that makes no new substance. The same stuff is still '
                               'there, melted, dissolved, broken or moved.'},
                {'term': 'chemical change',
                 'definition': 'A change that makes at least one new substance, with properties '
                               'the starting materials did not have.'},
                {'term': 'chemical reaction',
                 'definition': 'Another name for a chemical change. The atoms are all still there '
                               'and have been joined up differently.'},
                {'term': 'reversible',
                 'definition': 'Able to be turned back. It is a clue about how much energy and '
                               'equipment a change would take to undo, and it is not what decides '
                               'whether a change is chemical.'}],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why irreversible is not the same as chemical?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Reaction profiles, bond breaking and bond making, and why a chemical change '
                'involves an energy change every time.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
