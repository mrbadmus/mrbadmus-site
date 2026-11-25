# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C6 `acids-and-carbonates` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 860c783d26. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C6'
SOURCE_SLUG = 'acids-and-carbonates'
FROZEN_FROM = '860c783d26'

LESSON = {'slug': 'acids-and-carbonates',
 'title': 'Acids and carbonates',
 'discipline': 'chemistry',
 'unit': 'acids-and-alkalis',
 'family': 'PROCESS',
 'covers': [],
 'beyond_statutory': True,
 'ks4_links': ['chemistry/chemical-changes/reactions-of-acids'],
 'touches': [],
 'threads': [{'id': 'substances-and-reactions', 'level': 3}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['acid-plus-metal'],
 'assumes': [],
 'references': [],
 'connects_heading': 'Next in this unit',
 'big_question': 'A cathedral has stood for eight hundred years and the faces on its statues have '
                 'gone. Nobody touched them — the rain did it, one reaction at a time.',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Rock that fizzes',
           'done_when': 'committed'},
          {'anchor': 's-rig',
           'short': 'RIG',
           'label': 'The limewater test',
           'done_when': 'all_five_revealed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Four white solids',
           'done_when': 'all_four_decided'},
          {'anchor': 's-world',
           'short': 'USES',
           'label': 'Three consequences',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'What a test proves',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Drop a marble chip into acid and it fizzes like a tablet in water. '
                         'Marble is rock.',
                'prompt': 'The chip shrinks and streams bubbles from every surface. The gas is not '
                          'hydrogen: a lit splint held to it goes out instead of squeaking.',
                'commit': 'If you had to guess, does the gas come out of the rock, or out of the '
                          'acid?',
                'options': ['Out of the rock', 'Out of the acid'],
                'reveal': 'Marble, chalk and limestone are all carbonates, and all fizz in acid. '
                          'Next: the rule for what an acid and a carbonate always make, and the '
                          'test for the gas.',
                'guess': True,
                'replies': ['The gas is carbon dioxide, and its carbon and oxygen were locked '
                            'inside the rock. The acid sets them free.',
                            'With a metal the gas does come from the acid, so that makes sense. '
                            'This time it comes from the rock, which has carbon and oxygen locked '
                            'inside it.'],
                'answer': 0},
 'misconceptions': [{'id': 'ACID-08',
                     'statement': 'A gas that puts out a splint is carbon dioxide.',
                     'elicited_by': 'think-commit-splint',
                     'confronted_by': 'think-commit-splint'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'A <strong>carbonate</strong> is any compound containing a carbonate group — '
                   'calcium carbonate, sodium carbonate, copper carbonate. Every one of them '
                   'reacts with acid the same way, and there are three products, not two.'},
          {'type': 'rule',
           'id': 'salt-water-and-gas',
           'eyebrow': 'The rule',
           'statement': 'An acid and a carbonate always make the same three things.',
           'equation': {'reactants': 'acid + carbonate',
                        'arrow': 'makes',
                        'products': 'salt + water + carbon dioxide',
                        'condition': 'the carbon dioxide comes out of the carbonate, not the acid'},
           'close': 'The carbon dioxide is the giveaway. It is the fizz, and it is what limewater '
                    'detects.'},
          {'type': 'check', 'id': 'rig-limewater', 'anchor': 's-rig'},
          {'type': 'check', 'id': 'bench-four-solids', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'limewater-is-the-test'},
          {'type': 'check', 'id': 'uses-three', 'anchor': 's-world'},
          {'type': 'misconception',
           'id': 'think-commit-splint',
           'anchor': 's-think',
           'targets': 'ACID-08'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'limewater-is-the-test',
                'text': 'acid + carbonate makes salt + water + carbon dioxide. Limewater turning '
                        'milky is the test for that gas — and nothing else turns it milky.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-splint',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ACID-08',
                 'prompt': 'The splint did go out. Commit before you read on.',
                 'options': ['Right — putting a splint out is the test for carbon dioxide',
                             'Wrong — most gases put a splint out; only limewater identifies '
                             'carbon dioxide',
                             'Right, because carbon dioxide is heavier than air',
                             'Wrong — carbon dioxide makes a splint burn brighter'],
                 'reveal': ['Almost every gas puts a splint out. Nitrogen does, argon does, and so '
                            'does a tube of nothing much at all — a flame needs oxygen, and '
                            'anything that is not oxygen will smother it. “The splint went out” '
                            'narrows the answer to <em>not oxygen</em>, which is barely a clue.',
                            'Limewater is different: it goes milky for carbon dioxide and for '
                            'nothing else on your bench. <strong>A good test has one answer. A '
                            'test that dozens of substances could pass is not evidence.</strong>']},
                {'eyebrow': 'Watched first · five steps',
                 'heading': 'The limewater test',
                 'prompt': 'Each step has a reason, and each reason is a way this test can be got '
                           'wrong. Reveal them one at a time.',
                 'demand': 'explain',
                 'head_counter': {'format': '{n} of {total} revealed', 'start': 0},
                 'steps': [{'id': 'st1',
                            'what': 'Put the carbonate in a boiling tube and add the acid.',
                            'why': 'A boiling tube, not a test tube — the fizzing throws liquid up '
                                   'the sides, and a tube that is too small delivers acid spray to '
                                   'whoever is holding it.'},
                           {'id': 'st2',
                            'what': 'Fit a bung with a delivery tube straight away.',
                            'why': 'Carbon dioxide is produced from the first second. Anything '
                                   'that escapes before the bung goes in is gas you cannot test, '
                                   'and the fastest fizzing happens at the start.'},
                           {'id': 'st3',
                            'what': 'Run the delivery tube into a second tube of clear limewater.',
                            'why': 'The end of the tube must be under the surface of the '
                                   'limewater. Above it, the gas bubbles into the air and the '
                                   'limewater never meets it.'},
                           {'id': 'st4',
                            'what': 'Watch the limewater, not the reaction.',
                            'why': 'The interesting tube is the second one. Clear limewater '
                                   'turning milky white is the positive result — a fine white '
                                   'solid forming in what was a clear liquid.'},
                           {'id': 'st5',
                            'what': 'Keep bubbling and it goes clear again.',
                            'why': 'Not a mistake, and not a failed test. Excess carbon dioxide '
                                   'dissolves the white solid back into something colourless. The '
                                   'test is the change to milky, so read it when it happens rather '
                                   'than at the end.'}],
                 'labels': {'first': 'Reveal the first step',
                            'next': 'Reveal the next step',
                            'all': 'All five shown'},
                 'id': 'rig-limewater',
                 'kind': 'step-rig'},
                {'eyebrow': 'Your turn · four white solids',
                 'heading': 'Which of these are carbonates? Only the acid can tell you.',
                 'prompt': 'Three of these look almost identical in the bottle, which is the '
                           'point.',
                 'demand': 'investigate',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'options': [{'id': 'fizz', 'label': 'It will fizz', 'reacts': True},
                             {'id': 'no', 'label': 'No reaction'}],
                 'solids': [{'id': 'w1',
                             'name': 'Marble chips',
                             'looks': 'hard white lumps',
                             'answer': 'fizz',
                             'verdict': 'It fizzes — this one is a carbonate.',
                             'why': 'Calcium carbonate. Steady fizzing from every surface, and the '
                                    'limewater goes milky within seconds.',
                             'eq_left': 'hydrochloric acid + calcium carbonate',
                             'eq_right': 'calcium chloride + water + carbon dioxide'},
                            {'id': 'w2',
                             'name': 'Baking soda',
                             'looks': 'fine white powder',
                             'answer': 'fizz',
                             'verdict': 'It fizzes — this one is a carbonate.',
                             'why': 'Sodium hydrogencarbonate — a carbonate with hydrogen in it, '
                                    'and it behaves the same way. Violent fizzing because the '
                                    'powder has an enormous surface area.',
                             'eq_left': 'hydrochloric acid + sodium hydrogencarbonate',
                             'eq_right': 'sodium chloride + water + carbon dioxide'},
                            {'id': 'w3',
                             'name': 'Table salt',
                             'looks': 'white crystals',
                             'answer': 'no',
                             'verdict': 'No fizzing. Not a carbonate.',
                             'why': 'Sodium chloride. Nothing happens at all: it is already a '
                                    'salt, and there is no carbonate in it for the acid to break '
                                    'open. It just dissolves.',
                             'eq_left': '',
                             'eq_right': ''},
                            {'id': 'w4',
                             'name': 'Copper carbonate',
                             'looks': 'green powder',
                             'answer': 'fizz',
                             'verdict': 'It fizzes — this one is a carbonate.',
                             'why': 'The only one on the bench that is not white — and it fizzes '
                                    'hard, giving a blue-green solution of copper chloride. '
                                    'Carbonates are a family, not a single substance.',
                             'eq_left': 'hydrochloric acid + copper carbonate',
                             'eq_right': 'copper chloride + water + carbon dioxide'}],
                 'id': 'bench-four-solids',
                 'kind': 'solid-sorter'},
                {'eyebrow': 'Three consequences',
                 'heading': 'One reaction, three places it decides the outcome',
                 'prompt': 'Commit to each before reading. None of the three is about a '
                           'laboratory.',
                 'demand': 'explain',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'items': [{'id': 'u1',
                            'q': 'Why do old gravestones made of limestone go unreadable while '
                                 'granite ones stay sharp?',
                            'options': [{'id': 'a', 'label': 'Limestone is softer'},
                                        {'id': 'b',
                                         'label': 'Rain reacts with the carbonate in limestone'},
                                        {'id': 'c', 'label': 'Granite is polished'}],
                            'answer': 'b',
                            'reply': 'Because rain is slightly acidic and limestone is calcium '
                                     'carbonate, so the stone is slowly reacted away — letters '
                                     'first, since they are the thinnest part. Granite contains no '
                                     'carbonate, so the same rain runs off it and does nothing. '
                                     'Hardness is a side issue; this is a chemical difference, not '
                                     'a physical one.'},
                           {'id': 'u2',
                            'q': 'A fizzy indigestion tablet contains a carbonate and a solid '
                                 'acid. Why does it only fizz when dropped in water?',
                            'options': [{'id': 'a', 'label': 'Water is an acid'},
                                        {'id': 'b',
                                         'label': 'The two solids cannot react until they '
                                                  'dissolve'},
                                        {'id': 'c', 'label': 'The water heats them up'}],
                            'answer': 'b',
                            'reply': 'Both ingredients sit dry in the tablet doing nothing, '
                                     'because their particles cannot move past each other. Water '
                                     'dissolves them, the particles mix, and the reaction starts — '
                                     'giving carbon dioxide, which is the fizz. The carbonate then '
                                     'goes on to neutralise the acid in the stomach.'},
                           {'id': 'u3',
                            'q': 'A farmer wants to know whether a field of soil contains chalk. '
                                 'What is the two-minute test?',
                            'options': [{'id': 'a', 'label': 'Add acid and watch for fizzing'},
                                        {'id': 'b', 'label': 'Add water and see if it dissolves'},
                                        {'id': 'c',
                                         'label': 'Weigh a sample before and after drying'}],
                            'answer': 'a',
                            'reply': 'Drip dilute acid on it. Fizzing means a carbonate is '
                                     'present, and in soil that means chalk or limestone. '
                                     'Collecting the gas and turning limewater milky would confirm '
                                     'it. Geologists carry a small bottle of acid in the field for '
                                     'exactly this.'}],
                 'id': 'uses-three',
                 'kind': 'acid-judgements'}],
 'ladder': {'recall': {'q': 'An acid reacts with a metal carbonate. What are the products?',
                       'options': ['salt + hydrogen + carbon dioxide',
                                   'salt + water + hydrogen',
                                   'salt + water + carbon dioxide',
                                   'water + hydrogen + carbon dioxide'],
                       'answer': 2,
                       'feedback': {0: 'Hydrogen comes from a metal and an acid. A carbonate gives '
                                       'water and carbon dioxide.',
                                    1: 'No hydrogen is made. The gas from a carbonate is carbon '
                                       'dioxide.',
                                    3: 'A salt is always made. No hydrogen is made with a '
                                       'carbonate.'}},
            'apply': {'q': 'A gas is bubbled through limewater and the limewater stays clear. What '
                           'can you conclude?',
                      'options': ['The gas is oxygen, as oxygen relights a glowing wooden splint',
                                  'The gas is not carbon dioxide, as that turns limewater milky',
                                  'The gas is carbon dioxide, as that leaves limewater clear',
                                  'The gas is hydrogen, as hydrogen leaves the limewater clear'],
                      'answer': 1,
                      'feedback': {0: 'That is the test for oxygen, and no splint was used. Clear '
                                      'limewater only rules out carbon dioxide.',
                                   2: 'Carbon dioxide turns limewater milky. Clear limewater means '
                                      'the gas is not carbon dioxide.',
                                   3: 'Hydrogen does leave it clear, but so do many gases. Only '
                                      'carbon dioxide is ruled out.'}},
            'explain': {'q': 'Marble chips are dropped into dilute hydrochloric acid. Describe '
                             'what you would see, name all three products, and explain how you '
                             'would prove the gas is carbon dioxide.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The chips…',
                        'success': ['Says the chips fizz and get smaller.',
                                    'Names the products as calcium chloride, water and carbon '
                                    'dioxide.',
                                    'Says the gas is collected through a delivery tube into '
                                    'limewater.',
                                    'Says limewater turning milky shows carbon dioxide.',
                                    'Says the delivery tube must be below the surface of the '
                                    'limewater.']},
            'produce': {'q': 'Two white powders are on the bench: one is a carbonate and one is '
                             'not, and you may not taste or touch either. Design a test that would '
                             'tell them apart, and explain what result would settle it.',
                        'field_label': 'Your plan',
                        'placeholder': 'I would add dilute acid to a small sample of…',
                        'success': ['Adds dilute acid to a small sample of each powder.',
                                    'Uses the same amount of the same acid for both.',
                                    'Says the carbonate fizzes and the other does not.',
                                    'Collects the gas and tests it with limewater to confirm.',
                                    'Says limewater turning milky proves the fizzing was carbon '
                                    'dioxide.']}},
 'key_note': 'Acids react with carbonates to give a salt, water and carbon dioxide. The fizzing is '
             'the carbon dioxide leaving, and it is identified by bubbling it through limewater, '
             'which turns milky. Calcium carbonate is chalk, limestone and marble — which is why '
             'acid rain damages buildings and statues made of them.',
 'stretch': [{'type': 'explainer',
              'id': 'limestone-landscapes',
              'text': 'Whole landscapes are made by this reaction. Rain is slightly acidic before '
                      'it picks up any pollution at all, and where it falls on limestone it '
                      'dissolves it — slowly, along cracks, for thousands of years. The result is '
                      'limestone pavement above ground and cave systems below it, and every '
                      'stalactite is the same reaction running backwards as the water dries and '
                      'leaves the calcium carbonate behind.'},
             {'type': 'explainer',
              'id': 'the-same-chemistry-in-the-ocean',
              'text': 'The same chemistry sits in the ocean. Carbon dioxide dissolving into '
                      'seawater makes it very slightly more acidic, and shells and coral skeletons '
                      'are calcium carbonate. A change of a few tenths of a pH unit across an '
                      'ocean is not a laboratory abstraction — it is the difference between a '
                      'shell that thickens and one that thins.'}],
 'support': [],
 'vocabulary': [{'term': 'Carbonate',
                 'definition': 'Any compound containing a carbonate group. Every one of them '
                               'reacts with an acid to give a salt, water and carbon dioxide.'},
                {'term': 'Limewater',
                 'definition': 'A clear solution used to test for carbon dioxide. It turns milky '
                               'white when the gas is bubbled through it, and nothing else on a '
                               'school bench does that.',
                 'note': 'Keep bubbling past the milky stage and it clears again. The change to '
                         'milky is the result, not the end state.'},
                {'term': 'Calcium carbonate',
                 'definition': 'The compound that chalk, limestone and marble are all made of. It '
                               'is why acid rain damages statues and why a drop of acid on soil '
                               'tells a farmer there is chalk in it.'},
                {'term': 'Delivery tube',
                 'definition': 'The tube that carries gas from the reaction to wherever it is '
                               'being tested. Its far end goes under the surface of the liquid, or '
                               'the gas escapes into the air instead.'},
                {'term': 'Specific test',
                 'definition': 'A test only one substance can pass. A splint going out is not one '
                               '— most gases do that — and limewater going milky is.'}],
 'safety_note': 'Eye protection throughout. Dilute acid on a carbonate fizzes hard enough to throw '
                'liquid up the tube, which is why the reaction goes in a boiling tube rather than '
                'a test tube and why the bung is fitted from the side rather than over the mouth. '
                'Limewater is an alkali: wash it off skin, and off the bench.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why limewater goes cloudy?',
           'cta': 'Ask about this lesson',
           'anchor': 's-rig'},
 'ks4_becomes': 'Testing for carbonates and gases as part of qualitative analysis, and the thermal '
                'decomposition of carbonates in the lime kiln.',
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
