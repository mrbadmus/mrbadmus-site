# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C4 `reactions-rearrange-atoms` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C4'
SOURCE_SLUG = 'reactions-rearrange-atoms'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'reactions-rearrange-atoms',
 'title': 'Reactions rearrange atoms',
 'discipline': 'chemistry',
 'unit': 'chemical-reactions',
 'family': 'MODEL',
 'covers': ['KS3.C.CR.01b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}, {'id': 'particles', 'level': 3}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['chemical-vs-physical-change'],
 'assumes': [],
 'references': [],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'A new substance appears where two old ones were. Nothing was added and nothing '
                 'left — so what actually happened?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Two balloons', 'done_when': 'committed'},
          {'anchor': 's-rearr',
           'short': 'ATOMS',
           'label': 'Take it apart',
           'done_when': 'all_three_reactions_rebuilt'},
          {'anchor': 's-impossible',
           'short': 'RULE',
           'label': 'Break the rule',
           'done_when': 'one_product_asked'},
          {'anchor': 's-think', 'short': 'THINK', 'label': 'New atoms?', 'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two invisible gases. Set fire to them and you get something you can '
                         'drink.',
                'prompt': 'Hydrogen in one balloon, oxygen in another. Both colourless, neither of '
                          'them heavy in the hand, neither of them wet. Light them and what '
                          'condenses on the cold glass afterwards is water.',
                'commit': 'If you had to guess, would the two gases, mixed in one balloon and left '
                          'alone, turn into water on their own?',
                'options': ['Yes, on their own', 'No, they need starting'],
                'reveal': 'Once started, the atoms that were in the balloons join up in a new way, '
                          'as water. Next: take three reactions apart and count the atoms.',
                'guess': True,
                'replies': ['Mixing sounds like enough for a reaction. But the atoms in each gas '
                            'are joined in pairs, and those joins must be broken first. Without a '
                            'flame or spark, the mixture just sits there.',
                            'A mix of hydrogen and oxygen can sit in a balloon for a very long '
                            'time. A flame or spark is needed to break the first joins between its '
                            'atoms.'],
                'answer': 1},
 'misconceptions': [{'id': 'REACT-03',
                     'statement': 'When magnesium burns, the magnesium atoms turn into magnesium '
                                  'oxide atoms.',
                     'elicited_by': 'think-commit-mgo-atom',
                     'confronted_by': 'think-commit-mgo-atom'},
                    {'id': 'REACT-04',
                     'statement': 'New atoms can be made if the conditions are right.',
                     'elicited_by': 'ask-gold',
                     'confronted_by': 'ask-gold-refusal'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Atoms are joined together in the substances you start with. A chemical '
                   'reaction <strong>breaks those joins and makes different ones</strong>. The '
                   'atoms are not changed, created or destroyed — they are the same atoms '
                   'throughout, and only their partners are new.'},
          {'type': 'explainer',
           'text': 'That is why a new substance can appear out of two old ones, and why the atom '
                   'count on each side is always identical. It has to be. There is nowhere else '
                   'for an atom to come from.'},
          {'type': 'check', 'id': 'atom-rearranger', 'anchor': 's-rearr'},
          {'type': 'check', 'id': 'impossible-product-ask', 'anchor': 's-impossible'},
          {'type': 'key-fact', 'ref': 'atoms-rearranged'},
          {'type': 'misconception',
           'id': 'think-commit-mgo-atom',
           'anchor': 's-think',
           'targets': 'REACT-03'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'atoms-rearranged',
                'text': 'A chemical reaction breaks the joins between atoms and makes new ones. '
                        'The atoms themselves are unchanged, and there are exactly as many of each '
                        'kind afterwards as there were before.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-mgo-atom',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'REACT-03',
                 'prompt': 'It sounds right, and it uses the right words in the right order. '
                           'Commit before you read on.',
                 'options': ['Right — that is what burning does',
                             'Wrong — there is no such thing as a magnesium oxide atom',
                             'Right, because the powder is a new substance',
                             'Wrong — the magnesium atoms are destroyed in the flame'],
                 'reveal': ['There is no such thing as a magnesium oxide atom. Magnesium oxide is '
                            'a <strong>compound</strong>, built from magnesium atoms and oxygen '
                            'atoms held together — and both kinds of atom are still exactly what '
                            'they were. Nothing in the flame changed one element into another; the '
                            'periodic table has not been edited.',
                            'This is the same idea as thinking a copper atom is orange and '
                            'conducts. <strong>An atom does not carry the properties of the '
                            'substance it ends up in.</strong> Turning one element into another is '
                            'possible, but not with a Bunsen burner and not in chemistry — it '
                            'takes a nuclear reaction, and that is a different subject.']},
                {'eyebrow': 'Your turn · take a reaction apart',
                 'heading': 'Break the joins, count the atoms, make the new joins',
                 'demand': 'investigate',
                 'elements': {'H': {'colour': '#F3EDE1', 'ink': '#1A1714', 'name': 'Hydrogen'},
                              'O': {'colour': '#E4572E', 'ink': '#FFFDF8', 'name': 'Oxygen'},
                              'Mg': {'colour': '#2F5D8A', 'ink': '#FFFDF8', 'name': 'Magnesium'},
                              'C': {'colour': '#1A1714', 'ink': '#FFFDF8', 'name': 'Carbon'}},
                 'reactions': [{'id': 'water',
                                'tab': 'Hydrogen + oxygen',
                                'words': 'hydrogen + oxygen makes water',
                                'reactants': [{'formula': [('H', 2)], 'atoms': ['H', 'H']},
                                              {'formula': [('H', 2)], 'atoms': ['H', 'H']},
                                              {'formula': [('O', 2)], 'atoms': ['O', 'O']}],
                                'products': [{'formula': [('H', 2), ('O', 1)],
                                              'atoms': ['H', 'H', 'O']},
                                             {'formula': [('H', 2), ('O', 1)],
                                              'atoms': ['H', 'H', 'O']}],
                                'counts': [{'el': 'Hydrogen', 'n': 4}, {'el': 'Oxygen', 'n': 2}],
                                'gate': {'q': 'The loose atoms are on the table. How many oxygen '
                                              'atoms will be in the water you make?',
                                         'options': ['One — water only needs one',
                                                     'Two — the same two that were there',
                                                     'Four — one for each hydrogen']},
                                'product_text': 'Two water particles, each one oxygen atom joined '
                                                'to two hydrogen atoms. Four hydrogens and two '
                                                'oxygens, exactly as before — and a liquid, from '
                                                'two gases.'},
                               {'id': 'mgo',
                                'tab': 'Magnesium + oxygen',
                                'words': 'magnesium + oxygen makes magnesium oxide',
                                'reactants': [{'formula': [('Mg', 1)], 'atoms': ['Mg']},
                                              {'formula': [('Mg', 1)], 'atoms': ['Mg']},
                                              {'formula': [('O', 2)], 'atoms': ['O', 'O']}],
                                'products': [{'formula': [('Mg', 1), ('O', 1)],
                                              'atoms': ['Mg', 'O']},
                                             {'formula': [('Mg', 1), ('O', 1)],
                                              'atoms': ['Mg', 'O']}],
                                'counts': [{'el': 'Magnesium', 'n': 2}, {'el': 'Oxygen', 'n': 2}],
                                'gate': {'q': 'Two magnesium atoms and two oxygen atoms are loose. '
                                              'How many magnesium oxide units can you build?',
                                         'options': ['One', 'Two', 'Four']},
                                'product_text': 'Two magnesium oxide units, each one magnesium '
                                                'joined to one oxygen. The white powder weighs '
                                                'more than the ribbon did — because the oxygen '
                                                'atoms came from the air and are now part of it.'},
                               {'id': 'methane',
                                'tab': 'Methane + oxygen',
                                'words': 'methane + oxygen makes carbon dioxide + water',
                                'reactants': [{'formula': [('C', 1), ('H', 4)],
                                               'atoms': ['C', 'H', 'H', 'H', 'H']},
                                              {'formula': [('O', 2)], 'atoms': ['O', 'O']},
                                              {'formula': [('O', 2)], 'atoms': ['O', 'O']}],
                                'products': [{'formula': [('C', 1), ('O', 2)],
                                              'atoms': ['C', 'O', 'O']},
                                             {'formula': [('H', 2), ('O', 1)],
                                              'atoms': ['H', 'H', 'O']},
                                             {'formula': [('H', 2), ('O', 1)],
                                              'atoms': ['H', 'H', 'O']}],
                                'counts': [{'el': 'Carbon', 'n': 1},
                                           {'el': 'Hydrogen', 'n': 4},
                                           {'el': 'Oxygen', 'n': 4}],
                                'gate': {'q': 'One carbon, four hydrogens and four oxygens are '
                                              'loose. Which set of products uses all of them '
                                              'exactly?',
                                         'options': ['One carbon dioxide and one water',
                                                     'One carbon dioxide and two waters',
                                                     'Two carbon dioxides and two waters']},
                                'product_text': 'One carbon dioxide and two waters — and every one '
                                                'of the nine atoms is used, with none left over '
                                                'and none invented. This is what a gas hob does, '
                                                'several times a second.'}],
                 'stage': 0,
                 'tabs_label': 'The reaction',
                 'count_label': 'Atom count',
                 'count_headings': {'atom': 'Atom', 'before': 'Before', 'after': 'After'},
                 'count_pending': '—',
                 'stage_names': ['Before · the substances you start with',
                                 'The joins are broken · loose atoms on the table',
                                 'After · the new substances'],
                 'stage_texts': ['Each box is one particle of a starting substance, and the atoms '
                                 'inside it are joined together. Nothing has happened yet.',
                                 'Every join has been broken and nothing else has been done. This '
                                 'stage is not real — no chemist ever sees it — but it is the '
                                 'honest way to see what a reaction has to work with. Count what '
                                 'is on the table: that is your entire budget.'],
                 'stage_labels': ['A particle diagram of the reactants: {n} separate particles, '
                                  'each drawn as its atoms joined inside one outline.',
                                  'The same atoms, all separate, with no joins between any of '
                                  'them.',
                                  'A particle diagram of the products: {n} new particles, built '
                                  'from exactly the same atoms.'],
                 'advance_labels': ['Break the joins', 'Make the new joins'],
                 'reset_label': 'Put it back',
                 'summary': 'All three reactions taken apart, and the atom count came out '
                            'identical every time — because at the loose-atom stage there was '
                            'nothing to add and nothing to take away. Whatever the products turn '
                            'out to be, they can only be built from the atoms on the table.',
                 'id': 'atom-rearranger',
                 'kind': 'atom-rearranger'},
                {'eyebrow': 'The rule has teeth · try to break it',
                 'heading': 'Ask the bench for a product it cannot build',
                 'prompt': 'You have hydrogen and oxygen on the table and nothing else. Pick '
                           'something for the bench to make.',
                 'demand': 'investigate',
                 'table': ['H', 'O'],
                 'asks': [{'id': 'water',
                           'label': 'Water',
                           'needs': ['H', 'O'],
                           'title': 'Built. Two hydrogens and one oxygen, and you had both.',
                           'text': 'Everything water needs was on the table. That is the only '
                                   'condition a reaction has to meet.'},
                          {'id': 'peroxide',
                           'label': 'Hydrogen peroxide',
                           'needs': ['H', 'O'],
                           'title': 'Built — and it is a different substance from water.',
                           'text': 'Two hydrogens and two oxygens. Same two elements as water, one '
                                   'extra oxygen atom, and a substance that bleaches hair rather '
                                   'than quenching thirst. The atoms decide, and so does how many '
                                   'of them.'},
                          {'id': 'ammonia',
                           'label': 'Ammonia',
                           'needs': ['N', 'H'],
                           'title': 'Refused. There is no nitrogen on this table.',
                           'text': 'Ammonia is nitrogen joined to three hydrogens, and nothing in '
                                   'either balloon contains a nitrogen atom. No reaction can make '
                                   'one — atoms are not created. If you want nitrogen in your '
                                   'product, you have to put nitrogen in your reactants.'},
                          {'id': 'gold',
                           'label': 'Gold',
                           'needs': ['Au'],
                           'title': 'Refused, and not because the bench is not trying hard enough.',
                           'text': 'Gold is an element. The only way to have gold atoms at the end '
                                   'is to have had gold atoms at the start. Fifteen hundred years '
                                   'of alchemy is the evidence, and this rule is why it never '
                                   'worked.'}],
                 'id': 'impossible-product-ask',
                 'kind': 'impossible-ask'}],
 'ladder': {'recall': {'q': 'What happens to the atoms during a chemical reaction?',
                       'options': ['Some atoms are destroyed and new ones are made',
                                   'The atoms themselves change into different kinds of atom',
                                   'The atoms stay exactly as they were, joined to the same '
                                   'partners',
                                   'The joins between them are broken and new joins are made'],
                       'answer': 3,
                       'feedback': {0: 'Atoms are not created or destroyed in a chemical reaction. '
                                       'Count them on each side and the numbers match.',
                                    1: 'That takes a nuclear reaction, not chemistry. A magnesium '
                                       'atom is still a magnesium atom after it burns.',
                                    2: 'Then nothing would have happened. New partners are '
                                       'precisely what makes it a reaction.'}},
            'apply': {'q': 'Methane burns in oxygen. There are four hydrogen atoms in the methane. '
                           'How many hydrogen atoms are in the products?',
                      'options': ['Two, because water only has two hydrogens',
                                  'Four — the same four, now in two water particles',
                                  'None — they are burnt up',
                                  'It depends on how much oxygen there is'],
                      'answer': 1,
                      'feedback': {0: 'Water has two hydrogens each, and two waters are made. Four '
                                      'atoms in, four atoms out.',
                                   2: 'Burning is not disappearing. The hydrogen atoms end up in '
                                      'the water that condenses on a cold window above a hob.',
                                   3: 'The oxygen decides whether the reaction can finish, not how '
                                      'many hydrogen atoms exist. Those were fixed by the '
                                      'methane.'}},
            'explain': {'q': 'A ribbon of magnesium is weighed, burned in air, and the white '
                             'powder left behind is weighed. It is heavier. Explain how the powder '
                             'can be heavier than the ribbon if atoms are never created.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The magnesium atoms have joined with…',
                        'success': ['Says the magnesium has joined with oxygen from the air.',
                                    'Says the oxygen atoms are now part of the powder, so their '
                                    'mass is included in the reading.',
                                    'Says no atoms were created — the oxygen atoms already '
                                    'existed, in the air.',
                                    'Says the mass of the ribbon plus the mass of the oxygen used '
                                    'equals the mass of the powder.',
                                    'Notes that weighing the air is what makes the sum come out '
                                    'right, and that this is why an open dish seems to gain '
                                    'mass.']},
            'produce': {'q': 'A student proposes making gold by reacting two cheap substances '
                             'together, and says the reason nobody has done it is that no-one has '
                             'found the right conditions. Use what you know about reactions and '
                             'atoms to explain why the plan cannot work, and what would be needed '
                             'instead.',
                        'field_label': 'Your answer',
                        'placeholder': 'Gold is an element, which means…',
                        'success': ['Says gold is an element, so it is made of gold atoms only.',
                                    'Says a reaction can only rearrange the atoms it is given.',
                                    'Says there is no gold atom in the starting materials, so '
                                    'there can be none in the products.',
                                    'Says conditions — heat, pressure, catalyst — change how a '
                                    'reaction goes, not which atoms exist.',
                                    'Says making gold from another element means changing the '
                                    'atoms themselves, which is a nuclear change, not '
                                    'chemistry.']}},
 'key_note': 'A chemical reaction breaks the joins between atoms and makes new ones. The atoms are '
             'the same atoms all the way through: not created, not destroyed, and never changed '
             'into other kinds of atom. So the count of each kind of atom is identical before and '
             'after, and a reaction can only build products from the atoms it was given.',
 'stretch': [{'type': 'explainer',
              'id': 'bond-energy',
              'text': 'The reason a reaction takes or gives out energy sits exactly here. Breaking '
                      'the joins between atoms always costs energy, and making new joins always '
                      'gives energy back. If the new joins give back more than the old ones cost, '
                      'the surplus leaves as heat and the reaction warms its surroundings; if they '
                      'give back less, the reaction takes the difference from its surroundings and '
                      'everything gets cold. Nothing else needs to be added to that story — it is '
                      'bookkeeping on joins.'},
             {'type': 'explainer',
              'id': 'why-it-needs-a-match',
              'text': 'It also explains why some reactions need a match. A mixture of hydrogen and '
                      'oxygen will sit in a balloon indefinitely, even though the reaction gives '
                      'out an enormous amount of energy, because the first joins still have to be '
                      'broken and nothing has paid for them. A flame pays for the first few, those '
                      'release enough energy to pay for the next few, and the balloon goes off. '
                      'Chemistry is full of things that are worth doing and still need starting.'}],
 'support': [],
 'vocabulary': [{'term': 'chemical reaction',
                 'definition': 'A change in which the joins between atoms are broken and new joins '
                               'are made, so one or more new substances appear.',
                 'note': None},
                {'term': 'reactant',
                 'definition': 'A substance you start with, before the reaction happens.',
                 'note': None},
                {'term': 'product',
                 'definition': 'A substance made by the reaction.',
                 'note': 'The atoms in a product were all in the reactants first. There is nowhere '
                         'else for them to come from.'},
                {'term': 'rearrange',
                 'definition': 'To keep the same things and put them together differently.',
                 'note': 'It is the whole of what a reaction does to atoms.'},
                {'term': 'compound',
                 'definition': 'A substance made of two or more kinds of atom joined together.',
                 'note': 'Magnesium oxide is a compound. There is no such thing as a magnesium '
                         'oxide atom.'}],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why no reaction can make gold?',
           'cta': 'Ask about this lesson',
           'anchor': 's-impossible'},
 'ks4_becomes': 'Bond breaking and bond making as the energy story of a reaction, and balanced '
                'symbol equations with state symbols.',
 'ws': ['scientific-attitudes', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
