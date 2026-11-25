# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C4 `word-equations` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C4'
SOURCE_SLUG = 'word-equations'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'word-equations',
 'title': 'Word equations',
 'discipline': 'chemistry',
 'unit': 'chemical-reactions',
 'family': 'MODEL',
 'covers': ['KS3.C.CR.02a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}, {'id': 'particles', 'level': 1}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['reactions-rearrange-atoms'],
 'assumes': [],
 'references': ['chemical-vs-physical-change'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'How do chemists write down a reaction so that nothing important is left out?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Twenty-two words',
           'done_when': 'committed'},
          {'anchor': 's-builder',
           'short': 'BUILD',
           'label': 'Build it',
           'done_when': 'all_cases_checked'},
          {'anchor': 's-read',
           'short': 'READ',
           'label': 'Read it back',
           'done_when': 'all_readings_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Not an equals sign',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Magnesium in a flame.',
                'prompt': '“I held the magnesium ribbon in the flame with tongs and it burned with '
                          'a really bright white light and left a white powder behind.” Every word '
                          'is true.',
                'commit': 'If you had to guess, what would tell a chemist which reaction happened: '
                          'how long it burned, or what the powder is?',
                'options': ['How long it burned', 'What the powder is'],
                'reveal': 'A word equation names every reactant and every product in one line. '
                          'Next: build three of them from what happened.',
                'guess': True,
                'replies': ['Timings matter in lots of experiments. But how long it burned says '
                            'nothing about what reacted. A chemist needs the name of the powder, '
                            'and what the magnesium joined with.',
                            'The powder is a new substance, magnesium oxide, made when the '
                            'magnesium joins with oxygen from the air. The sentence never names '
                            'either one.'],
                'answer': 1},
 'misconceptions': [{'id': 'REACT-05',
                     'statement': 'The arrow is like an equals sign, so you could write the '
                                  'equation the other way round.',
                     'elicited_by': 's-think',
                     'confronted_by': 'think-reveal-direction'},
                    {'id': 'REACT-06',
                     'statement': 'Heat, energy or a flame can be written into an equation as a '
                                  'reactant.',
                     'elicited_by': 'builder-distractor',
                     'confronted_by': 'builder-check'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'A <strong>word equation</strong> puts the substances you start with — the '
                   '<strong>reactants</strong> — on the left, and the substances you end with — '
                   'the <strong>products</strong> — on the right. The arrow is read as '
                   '<strong>“makes”</strong> or <strong>“turns into”</strong>. It is not an equals '
                   'sign, and the two sides are not interchangeable: a reaction runs one way, and '
                   'so does the arrow.'},
          {'type': 'explainer',
           'text': 'The plus sign is read as <strong>“and”</strong>. It never means add up.'},
          {'type': 'check', 'id': 'builder-check', 'anchor': 's-builder'},
          {'type': 'key-fact', 'ref': 'only-substances'},
          {'type': 'check', 'id': 'read-back', 'anchor': 's-read'},
          {'type': 'misconception',
           'id': 'think-reveal-direction',
           'anchor': 's-think',
           'targets': 'REACT-05'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'only-substances',
                'text': 'Reactants on the left, products on the right, and the arrow means '
                        '“makes”. Only substances go in a word equation — never conditions, never '
                        'energy, and never anything that was only watching.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-reveal-direction',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'REACT-05',
                 'prompt': 'The two sides do have the same atoms in them, which is exactly why '
                           'this is tempting. Commit before you read on.',
                 'options': ['Right — both sides have the same atoms',
                             'Wrong — the arrow says which way the reaction went',
                             'Right, as long as you keep the plus signs',
                             'Wrong — the two sides do not have the same atoms'],
                 'reveal': ['The two sides balance in atoms and they are not the same thing. '
                            'Written the other way round, “magnesium oxide makes magnesium and '
                            'oxygen” claims that white powder spontaneously turns back into '
                            'burning metal and air, which it does not — it takes a furnace, and it '
                            'is a different reaction with a different equation.',
                            'So the arrow carries information an equals sign does not: '
                            '<strong>which way it went.</strong> Two other habits follow from the '
                            'same mistake. You cannot cancel a substance that appears on both '
                            'sides the way you cancel in algebra — it is doing something on each '
                            'side. And “heat”, “energy” and “a flame” are not substances, so they '
                            'never appear in the equation; if the conditions matter, they are '
                            'written above the arrow.']},
                {'eyebrow': 'Your turn · build the equation',
                 'heading': 'Read what happened. Put each substance where it belongs.',
                 'demand': 'construct',
                 'cases': [{'id': 'mg',
                            'tab': 'Burning magnesium',
                            'story': 'A ribbon of magnesium is held in a hot flame with tongs. It '
                                     'burns with a fierce white light, taking oxygen out of the '
                                     'air as it goes, and leaves a white powder called magnesium '
                                     'oxide. The tongs are unchanged. Air also contains nitrogen, '
                                     'which takes no part.',
                            'reactants': ['Magnesium', 'Oxygen'],
                            'products': ['Magnesium oxide'],
                            'distractors': [('Nitrogen',
                                             'Nitrogen was in the air and took no part in the '
                                             'reaction. A substance that is only present does not '
                                             'go in the equation — only what reacts and what is '
                                             'made.'),
                                            ('Heat',
                                             'Heat is not a substance. It is a condition, and '
                                             'conditions are written above the arrow if they are '
                                             'written at all.')]},
                           {'id': 'marble',
                            'tab': 'Marble and acid',
                            'story': 'Marble chips — calcium carbonate — are dropped into '
                                     'hydrochloric acid. The mixture fizzes hard. The gas given '
                                     'off turns limewater cloudy, so it is carbon dioxide. Left in '
                                     'the flask are water and a dissolved salt, calcium chloride. '
                                     'The limewater was in a separate test tube.',
                            'reactants': ['Calcium carbonate', 'Hydrochloric acid'],
                            'products': ['Calcium chloride', 'Water', 'Carbon dioxide'],
                            'distractors': [('Limewater',
                                             'Limewater was used to test the gas in a different '
                                             'tube. It never met the marble, so it is not part of '
                                             'this reaction.'),
                                            ('Bubbles',
                                             'Bubbles are what you saw, not a substance. The '
                                             'substance is carbon dioxide — name it.')]},
                           {'id': 'methane',
                            'tab': 'A gas hob',
                            'story': 'Methane from the gas supply burns in the oxygen of the air. '
                                     'Carbon dioxide goes up into the room and water vapour '
                                     'condenses on a cold window above the hob. The flame itself '
                                     'is the reaction happening, not an ingredient.',
                            'reactants': ['Methane', 'Oxygen'],
                            'products': ['Carbon dioxide', 'Water'],
                            'distractors': [('Energy',
                                             'Energy is given out, and it is still not a '
                                             'substance. It has no place on either side of a word '
                                             'equation.'),
                                            ('Flame',
                                             'The flame is the reaction, seen. Nothing is made of '
                                             'flame.')]}],
                 'bench_label': 'On the bench · not everything here belongs in the equation',
                 'equation_label': 'Your equation',
                 'empty_label': 'nothing yet',
                 'place_labels': {'left': 'Reactant', 'right': 'Product', 'out': 'Leave it out'},
                 'check_label': 'Check this equation',
                 'clear_label': 'Clear it',
                 'verdict': {'perfect_title': 'That is the equation.',
                             'perfect_text': 'Every reactant on the left, every product on the '
                                             'right, nothing in it that is not a substance, and '
                                             'nothing in it that was only watching.',
                             'distractor_title': 'One thing in there does not belong.',
                             'side_title': '{Name} is on the wrong side.',
                             'side_product': 'You have said {name} was there before the reaction '
                                             'started. It was made by the reaction, so it belongs '
                                             'on the right of the arrow.',
                             'side_reactant': 'You have said {name} was made by the reaction. It '
                                              'was one of the things you started with, so it '
                                              'belongs on the left.',
                             'missing_title': 'Something is missing.',
                             'missing_text': 'You have left out {names}. A word equation with a '
                                             'missing substance implies the atoms in it came from '
                                             'nowhere.',
                             'missing_join': ' and '},
                 'id': 'builder-check',
                 'kind': 'equation-builder'},
                {'eyebrow': 'Read it back',
                 'heading': 'Which sentence is the equation actually saying?',
                 'demand': 'explain',
                 'readings': [{'id': 'x1',
                               'left': 'zinc + copper sulfate',
                               'right': 'zinc sulfate + copper',
                               'options': ['Zinc and copper sulfate react to make zinc sulfate and '
                                           'copper',
                                           'Zinc plus copper sulfate equals zinc sulfate plus '
                                           'copper'],
                               'answer': 0,
                               'reply': 'The first. "Plus" and "equals" describe an arithmetic '
                                        'sum; this is a reaction, so it is read as "and" and '
                                        '"makes". Say it out loud the wrong way and you will write '
                                        'it the wrong way.'},
                              {'id': 'x2',
                               'left': 'copper carbonate',
                               'right': 'copper oxide + carbon dioxide',
                               'options': ['One substance has broken down into two',
                                           'Two substances have joined to make one'],
                               'answer': 0,
                               'reply': 'One reactant, two products: the copper carbonate has been '
                                        'broken apart. Nothing joined it and nothing needed to — '
                                        'this kind of reaction has a name of its own, thermal '
                                        'decomposition.'},
                              {'id': 'x3',
                               'left': 'iron + sulfur',
                               'right': 'iron sulfide',
                               'options': ['A mixture of iron and sulfur has been made',
                                           'A compound has been made, and the iron is no longer '
                                           'magnetic'],
                               'answer': 1,
                               'reply': 'The arrow means a reaction happened, so the product is a '
                                        'compound, not a mixture. A mixture of iron and sulfur '
                                        'would still be separable with a magnet; iron sulfide is '
                                        'not.'}],
                 'id': 'read-back',
                 'kind': 'equation-read'}],
 'ladder': {'recall': {'q': 'In a word equation, what does the arrow mean?',
                       'options': ['Equals', 'And', 'Makes, or turns into', 'Is heated to give'],
                       'answer': 2,
                       'feedback': {0: 'An equals sign works both ways. The arrow says which way '
                                       'the reaction went, and reversing it usually describes '
                                       'something that does not happen.',
                                    1: 'That is the plus sign. The arrow separates the reactants '
                                       'from the products.',
                                    3: 'Heating may or may not be involved. Many reactions need no '
                                       'heat, and the arrow means the same thing in all of them.'}},
            'apply': {'q': 'A student writes: magnesium + oxygen + heat makes magnesium oxide. '
                           'What is wrong with it?',
                      'options': ['Heat is not a substance, so it does not belong in the equation',
                                  'Nothing — heat is needed, so it should be included',
                                  'Heat should be on the right, because burning gives out heat',
                                  'The reactants and products are the wrong way round'],
                      'answer': 0,
                      'feedback': {1: 'Heat is needed, and it is a condition rather than a '
                                      'reactant. Conditions go above the arrow, not in the line of '
                                      'substances.',
                                   2: 'Energy does give out — and it still is not a substance. '
                                      'Neither side of a word equation is the place for it.',
                                   3: 'Those are in the right places. The problem is the extra '
                                      'term between them.'}},
            'explain': {'q': 'Write the word equation for marble chips reacting with hydrochloric '
                             'acid, then explain how someone reading only your equation would know '
                             'that a gas was given off and that a new substance was made.',
                        'field_label': 'Your equation and explanation',
                        'placeholder': 'calcium carbonate + hydrochloric acid makes…',
                        'success': ['Gives the correct reactants on the left: calcium carbonate '
                                    'and hydrochloric acid.',
                                    'Gives all three products: calcium chloride, water and carbon '
                                    'dioxide.',
                                    'Says the arrow means the reactants made the products, so a '
                                    'change happened.',
                                    'Identifies carbon dioxide as the gas, and says how that is '
                                    'known — it turns limewater cloudy.',
                                    'Says the products are substances that were not there before, '
                                    'which is what makes it a chemical reaction.']},
            'produce': {'q': 'A student says word equations are pointless because you could just '
                             'describe the reaction in a sentence. Give two things a word equation '
                             'forces you to say that a description can leave out, and one thing a '
                             'word equation cannot say at all.',
                        'field_label': 'Your answer',
                        'placeholder': 'A word equation forces you to name…',
                        'success': ['Says it forces you to name every reactant, including one from '
                                    'the air that is easy to forget.',
                                    'Says it forces you to name the products rather than '
                                    'describing their appearance.',
                                    'Says it makes the direction of the change explicit.',
                                    'Says it cannot show how many particles of each substance are '
                                    'involved.',
                                    'Draws the consequence — you cannot work out amounts from a '
                                    'word equation, which is why symbol equations exist.']}},
 'key_note': 'A word equation puts the reactants on the left, the products on the right, and reads '
             'the arrow as “makes”. Plus means “and”, never add. Only substances appear — not '
             'heat, not energy, not a flame, and not anything that was merely present. The arrow '
             'runs one way, because so does the reaction.',
 'stretch': [{'type': 'explainer',
              'id': 'what-words-cannot-say',
              'text': 'Word equations run out of road quickly, and it is worth knowing exactly '
                      'where. They can say which substances react and which are made. They cannot '
                      'say <em>how many</em> particles of each — and that turns out to be most of '
                      'chemistry. Two hydrogen particles react with one oxygen particle; "hydrogen '
                      '+ oxygen makes water" cannot tell you that, so it cannot tell you how much '
                      'oxygen to supply or how much water to expect.'},
             {'type': 'explainer',
              'id': 'the-name-has-to-be-agreed',
              'text': 'They also depend on the name being agreed. "Iron oxide" names three '
                      'different compounds, and rust is a hydrated one, so a word equation for '
                      'rusting is honest only if everyone reading it knows which iron oxide is '
                      'meant. Symbols fix both problems at once, and that is the next lesson but '
                      'one: formulae name the substance exactly, and the numbers in front of them '
                      'say how many.'}],
 'support': [],
 'vocabulary': [{'term': 'word equation',
                 'definition': 'A line that names the substances a reaction starts with and the '
                               'substances it ends with, separated by an arrow.'},
                {'term': 'reactant',
                 'definition': 'A substance you start with. Reactants go on the left of the '
                               'arrow.'},
                {'term': 'product',
                 'definition': 'A substance the reaction makes. Products go on the right of the '
                               'arrow.'},
                {'term': 'condition',
                 'definition': 'Something a reaction needs but is not made of — heat, light, a '
                               'catalyst. Conditions are written above the arrow, never in the '
                               'line of substances.'},
                {'term': 'limewater',
                 'definition': 'A clear liquid used to test for carbon dioxide. It turns cloudy '
                               'when the gas is bubbled through it.'}],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why heat cannot go in the equation?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Balanced symbol equations with state symbols, ionic equations, and half '
                'equations.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
