# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C6 `neutralisation` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 860c783d26. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C6'
SOURCE_SLUG = 'neutralisation'
FROZEN_FROM = '860c783d26'

LESSON = {'slug': 'neutralisation',
 'title': 'Neutralisation',
 'discipline': 'chemistry',
 'unit': 'acids-and-alkalis',
 'family': 'PROCESS',
 'covers': ['KS3.C.CR.07a'],
 'touches': ['KS3.C.CR.04'],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3},
             {'id': 'measurement-and-uncertainty', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['the-ph-scale-and-indicators'],
 'assumes': [],
 'references': ['acids-and-alkalis'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Mix the two most dangerous bottles in the lab in the right amounts and you can '
                 'pour the result down the sink. Where did the danger go?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Two dangerous bottles',
           'done_when': 'committed'},
          {'anchor': 's-titrate',
           'short': 'DROPS',
           'label': 'Drop by drop',
           'done_when': 'cliff_crossed'},
          {'anchor': 's-uses',
           'short': 'USES',
           'label': 'Four problems',
           'done_when': 'all_four_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Where the acid went',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Hydrochloric acid in one beaker. Sodium hydroxide in the other. Both '
                         'would burn you.',
                'prompt': 'The two are mixed carefully, in just the right amounts. The mixture '
                          'warms up, and universal indicator comes out green: pH 7, the same as '
                          'pure water. Then all the water is boiled off in a dish.',
                'commit': 'If you had to guess, what is left in the dish: nothing at all, or '
                          'something solid?',
                'options': ['Nothing at all', 'Something solid'],
                'reveal': 'A reaction between an acid and an alkali is called neutralisation. '
                          'Next: the rule for what it always makes, then add the alkali drop by '
                          'drop.',
                'guess': True,
                'replies': ['The liquid did test like pure water, so that makes sense. But the '
                            'acid and alkali did not vanish. They made water and a salt, which '
                            'stays behind as white crystals.',
                            'It is a salt, made from the acid and the alkali. It was dissolved in '
                            'the water, so it only shows once the water has boiled away.'],
                'answer': 1},
 'misconceptions': [{'id': 'ACID-05',
                     'statement': 'Neutralising an acid destroys it; only water is left.',
                     'elicited_by': 'think-commit-gone',
                     'confronted_by': 'think-commit-gone'},
                    {'id': 'ACID-06',
                     'statement': 'The pH climbs steadily as alkali is added.',
                     'elicited_by': 's-titrate',
                     'confronted_by': 'curve-reveal'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': '<strong>Neutralisation</strong> is the reaction between an acid and a base. '
                   'With an alkali the products are always the same two things, whichever acid and '
                   'whichever alkali you started with.'},
          {'type': 'rule',
           'id': 'the-two-products',
           'eyebrow': 'The rule',
           'statement': 'An acid and an alkali always make the same two things.',
           'equation': {'reactants': 'acid + alkali',
                        'arrow': 'makes',
                        'products': 'salt + water',
                        'condition': 'the salt takes its metal from the alkali and its family name '
                                     'from the acid'},
           'close': '“Salt” here does not only mean the stuff on chips. It means the whole family '
                    'of compounds made when the hydrogen in an acid is swapped for a metal — '
                    'sodium chloride is one of thousands. Which salt you get depends on which acid '
                    'and which alkali you started with, and that is a lesson of its own.'},
          {'type': 'check', 'id': 'drop-by-drop', 'anchor': 's-titrate'},
          {'type': 'key-fact', 'ref': 'salt-and-water'},
          {'type': 'check', 'id': 'uses-four', 'anchor': 's-uses'},
          {'type': 'misconception',
           'id': 'think-commit-gone',
           'anchor': 's-think',
           'targets': 'ACID-05'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'salt-and-water',
                'text': 'acid + alkali makes salt + water. Nothing is destroyed: the atoms are '
                        'rearranged into two new substances, and the pH ends at 7 only if the '
                        'amounts match exactly.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-gone',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ACID-05',
                 'prompt': 'The beaker does end up looking like water. Commit before you read on.',
                 'options': ['Right — the acid is destroyed and only water is left in the beaker '
                             'afterwards',
                             'Wrong — a salt is dissolved in the water, made from the acid and the '
                             'alkali',
                             'Right, because pH 7 means empty and the crystals came out of the '
                             'dish itself',
                             'Wrong — the acid is still there unchanged, just hidden by all the '
                             'water around it'],
                 'reveal': ['Boil the water off and the answer is sitting in the dish. A '
                            'neutralised beaker contains a <strong>salt</strong> dissolved in '
                            'water, and that salt is made of atoms that came out of the acid and '
                            'the alkali. Weigh everything before and after: the mass is unchanged, '
                            'because this is conservation of mass and no reaction escapes it.',
                            'What has gone is the <em>behaviour</em>. The thing that made the acid '
                            'corrosive has been used up in making water, and so has the thing that '
                            'made the alkali corrosive. <strong>Neutralisation does not delete the '
                            'atoms. It puts them somewhere harmless.</strong>']},
                {'eyebrow': 'Your turn · add the alkali drop by drop',
                 'heading': '25 cm³ of hydrochloric acid. Universal indicator already added.',
                 'prompt': 'Alkali goes in one drop at a time. Watch the number, not the colour — '
                           'the colour is only the number in disguise.',
                 'demand': 'investigate',
                 'curve': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 7, 11, 11, 12, 12, 12, 13, 13, 13, 13, 13],
                 'states': [{'id': 'start',
                             'at': [0],
                             'side': 'acid',
                             'label': 'Still acidic',
                             'note': 'Red, and strongly acidic. Every drop of alkali that goes in '
                                     'will be destroyed on contact by the acid already there.'},
                            {'id': 'early',
                             'at': [1, 2, 3, 4, 5, 6, 7, 8],
                             'side': 'acid',
                             'label': 'Still acidic',
                             'note': 'The reading has barely moved. There is far more acid in the '
                                     'beaker than alkali added so far, so each drop is used up as '
                                     'fast as it arrives.'},
                            {'id': 'brink',
                             'at': [9],
                             'side': 'acid',
                             'label': 'Still acidic',
                             'note': 'Orange, pH 3, and almost all the acid is gone. The next drop '
                                     'has almost nothing left to react with.'},
                            {'id': 'equal',
                             'at': [10],
                             'side': 'neutral',
                             'label': 'Neutral — exactly',
                             'note': 'Green. Every particle of acid has met a particle of alkali '
                                     'and both are gone, replaced by salt and water. One drop '
                                     'either side of this and you would miss it.'},
                            {'id': 'past',
                             'at': [11, 12, 13],
                             'side': 'alkali',
                             'label': 'Now alkaline',
                             'note': 'Past it. There is no acid left to consume the alkali, so '
                                     'alkali is now simply accumulating in the beaker.'},
                            {'id': 'flat',
                             'at': [14, 15, 16, 17, 18, 19, 20],
                             'side': 'alkali',
                             'label': 'Now alkaline',
                             'note': 'Deep purple. From here, adding more barely moves the reading '
                                     'either — the same flattening as at the start, in the other '
                                     'direction.'}],
                 'add_buttons': [{'n': 1, 'label': 'Add 1 drop'}, {'n': 5, 'label': 'Add 5 drops'}],
                 'reset_label': 'Start again',
                 'count_format': '{n} drops of alkali added',
                 'count_zero': '0 drops of alkali added',
                 'trace_label': 'The reading, drop by drop',
                 'axis_label': '0 drops · · · 20 drops',
                 'close': {'id': 'curve-reveal',
                           'title': 'Look at the shape of what you just did.',
                           'paras': ['For the first nine drops almost nothing moves. Then one '
                                     'single drop takes the reading from 3 to 11 and the colour '
                                     'goes straight through green without stopping. After that it '
                                     'flattens off again.',
                                     'That cliff is the moment the last of the acid is used up. '
                                     'Before it, every drop of alkali is consumed instantly by '
                                     'acid that is still there. After it, there is no acid left to '
                                     'consume anything, so the alkali just piles up. '
                                     '<strong>Neutral is not a region you drift into. It is a '
                                     'single point you cross.</strong>']},
                 'id': 'drop-by-drop',
                 'kind': 'titration-dial'},
                {'eyebrow': 'Four problems · one reaction',
                 'heading': 'What would you add, and why that?',
                 'prompt': 'Every one of these is neutralisation doing a job outside a laboratory. '
                           'Commit before you read.',
                 'demand': 'explain',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'items': [{'id': 'u1',
                            'q': 'A field is too acidic for wheat. What does the farmer spread on '
                                 'it?',
                            'options': [{'id': 'a', 'label': 'Lime'},
                                        {'id': 'b', 'label': 'Vinegar'},
                                        {'id': 'c', 'label': 'More fertiliser'}],
                            'answer': 'a',
                            'reply': 'Lime — calcium hydroxide or calcium carbonate, an alkali. It '
                                     'neutralises the acid in the soil and brings the pH up '
                                     'towards 7, where most crops take up nutrients best. Vinegar '
                                     'would make it worse; fertiliser feeds the plant but does '
                                     'nothing about the pH.'},
                           {'id': 'u2',
                            'q': 'Someone has indigestion: stomach acid where it should not be. '
                                 'What is in the tablet they take?',
                            'options': [{'id': 'a', 'label': 'A weak acid'},
                                        {'id': 'b', 'label': 'A base'},
                                        {'id': 'c', 'label': 'Salt'}],
                            'answer': 'b',
                            'reply': 'A base — usually magnesium hydroxide or calcium carbonate. '
                                     'It neutralises the excess acid on contact. It has to be a '
                                     'mild one: a strong alkali would do more damage than the acid '
                                     'it was sent to deal with.'},
                           {'id': 'u3',
                            'q': 'Bacteria in your mouth make acid that dissolves tooth enamel '
                                 'below about pH 5.5. What does toothpaste do about it?',
                            'options': [{'id': 'a', 'label': 'Nothing — it only scrubs'},
                                        {'id': 'b',
                                         'label': 'It is mildly alkaline and neutralises the acid'},
                                        {'id': 'c',
                                         'label': 'It coats the teeth in acid-proof plastic'}],
                            'answer': 'b',
                            'reply': 'It is mildly alkaline, so it neutralises the acid the '
                                     'bacteria produce and lifts the mouth back above the level at '
                                     'which enamel dissolves. The scrubbing matters too — it '
                                     'removes the plaque the bacteria live in — but the chemistry '
                                     'is neutralisation.'},
                           {'id': 'u4',
                            'q': 'A factory must dispose of a tank of dilute sulfuric acid. '
                                 'Pouring it into the river would kill the fish. What is done '
                                 'first?',
                            'options': [{'id': 'a', 'label': 'Dilute it with much more water'},
                                        {'id': 'b',
                                         'label': 'Neutralise it with a base, then check the pH'},
                                        {'id': 'c', 'label': 'Boil it away'}],
                            'answer': 'b',
                            'reply': 'Neutralise it, then measure the pH before anything is '
                                     'released. Dilution lowers the concentration but the water '
                                     'going into the river is still acidic, and a river has its '
                                     'own life that depends on staying near neutral. Boiling it '
                                     'concentrates the acid rather than removing it.'}],
                 'id': 'uses-four',
                 'kind': 'acid-judgements'}],
 'ladder': {'recall': {'q': 'Complete the word equation: acid + alkali makes what?',
                       'options': ['water + hydrogen',
                                   'salt + water',
                                   'hydrogen + carbon dioxide',
                                   'salt + carbon dioxide'],
                       'answer': 1,
                       'feedback': {0: 'Water is made, but no hydrogen. A salt is the other '
                                       'product.',
                                    2: 'No gas is made. An acid and an alkali make a salt and '
                                       'water.',
                                    3: 'A carbonate gives carbon dioxide. An acid and an alkali '
                                       'make a salt and water.'}},
            'apply': {'q': 'A beaker of acid has alkali added drop by drop. After nine drops the '
                           'pH is 3; after ten it is 11. What happened at the tenth drop?',
                      'options': ['The tenth drop was stronger, so it pushed the pH much further '
                                  'up',
                                  'The indicator stopped working, so the last reading cannot be '
                                  'trusted',
                                  'The last acid was used up, so extra alkali was left over',
                                  'The mixture boiled, so the water left and it turned alkaline'],
                      'answer': 2,
                      'feedback': {0: 'Every drop came from the same bottle. The acid in the '
                                      'beaker had run out.',
                                   1: 'The indicator still works. The pH really did jump from 3 to '
                                      '11.',
                                   3: 'Nothing boils here. The jump happened because the acid ran '
                                      'out.'}},
            'explain': {'q': 'A student neutralises hydrochloric acid with sodium hydroxide and '
                             'says “the acid has disappeared”. Explain what has actually happened '
                             'to the atoms, and how you could prove it.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The atoms have not disappeared. They have…',
                        'success': ['Says the acid and alkali reacted to form new substances.',
                                    'Names the products as a salt (sodium chloride) and water.',
                                    'Says the atoms are all still present, just rearranged.',
                                    'Says mass is conserved and could be checked on a balance.',
                                    'Says evaporating the water would leave the salt behind as '
                                    'crystals.']},
            'produce': {'q': 'A lake has become acidic because of pollution and the fish are '
                             'dying. Explain how you would decide how much lime to add, and why '
                             'adding a very large amount all at once would be a bad idea.',
                        'field_label': 'Your answer',
                        'placeholder': 'First I would measure…',
                        'success': ['Says to measure the pH of the lake water first.',
                                    'Says lime is a base and will neutralise the acid.',
                                    'Says to add it gradually and re-test the pH as you go.',
                                    'Says too much would push the water past 7 and make it '
                                    'alkaline.',
                                    'Says a sudden large change in pH would itself harm the '
                                    'fish.']}},
 'key_note': 'Neutralisation is the reaction of an acid with a base: acid + alkali makes salt + '
             'water. The pH moves towards 7 as the acid is used up, and the change is sudden '
             'rather than gradual. Nothing is destroyed — the salt formed is still dissolved in '
             'the beaker, and boiling the water off leaves it behind as crystals.',
 'stretch': [{'type': 'explainer',
              'id': 'titration',
              'text': 'The cliff you plotted is why a chemist measuring an unknown acid uses a '
                      'single drop of a sharp indicator rather than universal indicator. Run '
                      'alkali in from a burette, watch for the one drop that flips the colour, and '
                      'read the volume off the scale: that volume tells you exactly how much acid '
                      'was in the flask. The technique is called titration and it is how the '
                      'strength of everything from vinegar to blood plasma is checked.'},
             {'type': 'explainer',
              'id': 'chimneys-and-plasterboard',
              'text': 'Neutralisation also runs on an industrial scale where nobody would call it '
                      'chemistry. Power station chimneys are washed with a spray of calcium '
                      'hydroxide to catch the sulfur dioxide that would otherwise fall as acid '
                      'rain; the salt produced is calcium sulfate, which is plasterboard. A '
                      'reaction that started as two beakers on a bench ends up as the walls of a '
                      'house.'}],
 'support': [],
 'vocabulary': [{'term': 'Neutralisation',
                 'definition': 'The reaction between an acid and a base. With an alkali it makes a '
                               'salt and water.'},
                {'term': 'Salt',
                 'definition': 'The compound left when the hydrogen in an acid is swapped for a '
                               'metal. Sodium chloride is one of thousands.',
                 'note': 'Not only the stuff on chips.'},
                {'term': 'Base',
                 'definition': 'Any substance that neutralises an acid. The ones that dissolve in '
                               'water are alkalis.'},
                {'term': 'Equivalence point',
                 'definition': 'The moment when exactly enough alkali has been added to use up all '
                               'the acid. On this page it is the single drop where the reading '
                               'jumps.'},
                {'term': 'Titration',
                 'definition': 'Adding one solution to another a little at a time until the '
                               'reaction is exactly complete, and measuring how much it took.'}],
 'safety_note': 'The mixture warms as it reacts, and a concentrated acid mixed with a concentrated '
                'alkali warms enough to boil and spit. School titrations use dilute solutions of '
                'both, a drop at a time, with eye protection on — which is also the only way to '
                'find the one drop that matters. Teacher demonstration. Eye protection on, and '
                'watch from your seat. The acid and alkali here are dilute, but both sting in the '
                'eyes.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why the pH jumps instead of climbing?',
           'cta': 'Ask about this lesson',
           'anchor': 's-titrate'},
 'ks4_becomes': 'Titration with a burette, the ionic equation H+ + OH− makes H<sub>2</sub>O, and '
                'calculating concentrations from titration results.',
 'ws': ['experimental-skills-and-investigations', 'measurement'],
 'review_state': 'draft',
 'authored': True}
