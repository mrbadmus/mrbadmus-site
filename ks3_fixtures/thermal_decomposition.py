# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C5 `thermal-decomposition` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 9a7b28d0fb. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C5'
SOURCE_SLUG = 'thermal-decomposition'
FROZEN_FROM = '9a7b28d0fb'

LESSON = {'slug': 'thermal-decomposition',
 'title': 'Thermal decomposition',
 'discipline': 'chemistry',
 'unit': 'types-of-reaction',
 'family': 'PROCESS',
 'covers': ['KS3.C.CR.03b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}, {'id': 'energy', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['combustion'],
 'assumes': [],
 'references': ['chemical-vs-physical-change'],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'A green powder is heated and turns black. What kind of reaction is this, and how '
                 'is it different from burning?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'One in, two out',
           'done_when': 'committed'},
          {'anchor': 's-tube',
           'short': 'TUBE',
           'label': 'The test tube',
           'done_when': 'all_three_run'},
          {'anchor': 's-sort',
           'short': 'SORT',
           'label': 'Five changes',
           'done_when': 'all_five_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Did it burn?',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A green powder in a hot tube.',
                'prompt': 'A green powder is heated in a test tube. It turns black, and a gas '
                          'comes off that turns limewater cloudy.',
                'commit': 'If you had to guess, once the heating is over, does what is left in the '
                          'tube weigh more than before, or less?',
                'options': ['More than before', 'Less than before'],
                'reveal': 'The green powder has split into two new substances, and one of them '
                          'escaped. Next: what this kind of reaction is called, then three powders '
                          'to heat.',
                'guess': True,
                'replies': ['When a metal burns it does get heavier, because oxygen from the air '
                            'joins it. Here nothing joins in: part of the powder leaves as a gas, '
                            'so the tube gets lighter.',
                            'Part of the powder left the tube as that gas. The black solid that '
                            'stays behind weighs less than the green powder did.'],
                'answer': 1},
 'misconceptions': [{'id': 'REACT-12',
                     'statement': 'It went black, so the copper carbonate burnt.',
                     'elicited_by': 'think-commit-black',
                     'confronted_by': 'think-commit-black'},
                    {'id': 'REACT-13',
                     'statement': 'A decomposition reverses when it cools.',
                     'elicited_by': 'cool-gate',
                     'confronted_by': 'stage-4-reveal'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': '<strong>Thermal decomposition</strong> is one compound being broken down into '
                   'two or more substances using heat. It is the only reaction type you will meet '
                   'that runs <em>backwards</em> compared with the others: instead of substances '
                   'joining, one comes apart.'},
          {'type': 'explainer',
           'text': 'It also needs the heat continuously. Take the flame away and the reaction '
                   'stops — which is the opposite of burning, where the reaction supplies its own '
                   'heat once it has started.'},
          {'type': 'check', 'id': 'tube-heat', 'anchor': 's-tube'},
          {'type': 'key-fact', 'ref': 'one-in-more-out'},
          {'type': 'check', 'id': 'sort-five', 'anchor': 's-sort'},
          {'type': 'misconception',
           'id': 'think-commit-black',
           'anchor': 's-think',
           'targets': 'REACT-12'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'one-in-more-out',
                'text': 'Thermal decomposition breaks one compound into two or more substances '
                        'using heat. One reactant, several products, nothing added — and it does '
                        'not reverse when it cools.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-black',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'REACT-12',
                 'prompt': 'Things that go black in a flame usually have burnt. Commit before you '
                           'read on.',
                 'options': ['Right — heating something until it goes black is burning',
                             'Wrong — nothing burnt; the black solid is copper oxide',
                             'Right, because oxygen from the air joined in',
                             'Wrong — the powder only looks black while it is hot'],
                 'reveal': ['Burning needs oxygen as a reactant. Do this reaction in a tube with '
                            'no air in it and it works exactly the same — so nothing was burnt. '
                            'The black is not soot and it is not charring: it is <strong>copper '
                            'oxide</strong>, which is black because that is what copper oxide '
                            'looks like.',
                            'The two reaction types point in opposite directions. In combustion, a '
                            'substance <strong>joins with</strong> oxygen and the reaction '
                            'releases energy. In thermal decomposition, a compound <strong>comes '
                            'apart</strong> and the reaction absorbs energy for as long as you '
                            'supply it. Both involve heat and a Bunsen burner, and that is the '
                            'whole of their resemblance.']},
                {'eyebrow': 'Your turn · the test tube',
                 'heading': 'Heat it, test the gas, then let it cool',
                 'demand': 'investigate',
                 'dial_label': 'In the tube',
                 'substances': [{'id': 'copper',
                                 'tab': 'Copper carbonate',
                                 'mass0': '4.00 g',
                                 'mass1': '2.58 g',
                                 'intro': 'A green powder. It decomposes at a temperature an '
                                          'ordinary Bunsen burner reaches easily, which is why it '
                                          'is the school version of this reaction.',
                                 'stages': ['The flame goes under the tube. Nothing happens for a '
                                            'few seconds while the powder heats through.',
                                            'The green darkens from the bottom upwards and becomes '
                                            'black. The colour change spreads as the heat does — '
                                            'the part not yet hot enough is still green.',
                                            'The gas is bubbled through limewater, which turns '
                                            'milky. That is the test for carbon dioxide, and only '
                                            'carbon dioxide passes it.',
                                            'The flame comes off. The powder stays black as it '
                                            'cools, and it stays black tomorrow.'],
                                 'eq_left': 'copper carbonate',
                                 'eq_right': 'copper oxide + carbon dioxide',
                                 'finish': 'Black copper oxide left in the tube, carbon dioxide '
                                           'gone into the limewater. The tube is lighter by '
                                           'exactly the mass of the gas that left.'},
                                {'id': 'calcium',
                                 'tab': 'Limestone',
                                 'mass0': '4.00 g',
                                 'mass1': '2.24 g',
                                 'intro': 'Calcium carbonate — limestone, chalk and marble are all '
                                          'the same compound. It needs a much higher temperature '
                                          'than the copper one: a roaring blue flame and patience, '
                                          'or an industrial kiln.',
                                 'stages': ['The flame goes under the lump. Nothing visible '
                                            'happens for a long time — this reaction needs far '
                                            'more heat than the copper carbonate did.',
                                            'The lump glows and crumbles slightly, and it stays '
                                            'white. There is no colour change to watch, which '
                                            'makes this a good reminder that a colour change is a '
                                            'clue and not a requirement.',
                                            'The gas turns limewater milky: carbon dioxide again. '
                                            'This is the only evidence that anything has happened '
                                            'at all.',
                                            'It cools as a white solid — calcium oxide, quicklime '
                                            '— and it is not the same substance that went in. Drop '
                                            'water on it and it hisses and gets hot.'],
                                 'eq_left': 'calcium carbonate',
                                 'eq_right': 'calcium oxide + carbon dioxide',
                                 'finish': 'Quicklime in the tube and carbon dioxide gone. This is '
                                           'the reaction that makes cement possible, run in kilns '
                                           'the size of buildings.'},
                                {'id': 'bicarb',
                                 'tab': 'Baking soda',
                                 'mass0': '4.00 g',
                                 'mass1': '2.52 g',
                                 'intro': 'Sodium hydrogencarbonate — the raising agent in a cake. '
                                          'It decomposes at oven temperatures, which is the entire '
                                          'reason it is in the recipe.',
                                 'stages': ['Gentle heating. The white powder starts to fizz and '
                                            'shift as gas works its way out of it.',
                                            'It stays white and loses volume. Water vapour '
                                            'condenses in the cool upper part of the tube — this '
                                            'decomposition gives two gases, not one.',
                                            'The gas turns limewater milky, so carbon dioxide is '
                                            'among the products. In a cake, this gas is what makes '
                                            'it rise.',
                                            'It cools to a white powder — sodium carbonate — and '
                                            'does not turn back. A cake does not become batter '
                                            'again as it cools either.'],
                                 'eq_left': 'sodium hydrogencarbonate',
                                 'eq_right': 'sodium carbonate + carbon dioxide + water',
                                 'finish': 'Three products from one reactant. The carbon dioxide '
                                           'is the point in baking, and the water vapour is why a '
                                           'cake steams as it comes out of the oven.'}],
                 'stage_titles': ['Heat it',
                                  'Watch the solid',
                                  'Test the gas',
                                  'Take the flame away'],
                 'gate': {'id': 'cool-gate',
                          'reveal_id': 'stage-4-reveal',
                          'q': 'Before you take the flame away: what happens as it cools?',
                          'options': ['It changes back as it cools',
                                      'It stays as it is — the change does not reverse',
                                      'It changes back only if you add the gas again']},
                 'tiles': [{'kind': 'mass', 'label': 'Mass in the tube'},
                           {'kind': 'lime', 'label': 'Limewater', 'values': ['clear', 'milky']},
                           {'kind': 'heat',
                            'label': 'Heat needed',
                            'values': ['not yet', 'continuously', 'flame removed']}],
                 'advance_labels': ['Light the Bunsen',
                                    'Keep heating',
                                    'Test the gas',
                                    'Let it cool'],
                 'reset_label': 'Fresh tube',
                 'summary': 'Three different substances, three word equations, and the same shape '
                            'every time: <strong>one on the left, more than one on the '
                            'right.</strong> None of them needed anything added, all of them '
                            'needed the flame kept on, and not one of them came back on cooling.',
                 'id': 'tube-heat',
                 'kind': 'tube-run'},
                {'eyebrow': 'Five changes · which are decomposition?',
                 'heading': 'Heat is involved in all five. Only some are this reaction',
                 'demand': 'classify',
                 'options': ['Thermal decomposition', 'Something else'],
                 'items': [{'id': 's1',
                            'yes': True,
                            'text': 'Green copper carbonate is heated and turns black, giving off '
                                    'carbon dioxide.',
                            'answer': 'Thermal decomposition. One compound in, two substances out, '
                                      'using heat and nothing else.'},
                           {'id': 's2',
                            'yes': False,
                            'text': 'A candle is lit and the wax burns away.',
                            'answer': 'Combustion, not decomposition. Two reactants — wax and '
                                      'oxygen — and the reaction releases heat rather than needing '
                                      'it.'},
                           {'id': 's3',
                            'yes': False,
                            'text': 'Ice in a beaker is heated and melts to water.',
                            'answer': 'A physical change. One substance in and the same substance '
                                      'out, and it reverses on cooling. No new substance was made '
                                      'at all.'},
                           {'id': 's4',
                            'yes': True,
                            'text': 'Baking soda in a cake mixture is heated and the cake rises.',
                            'answer': 'Thermal decomposition. The sodium hydrogencarbonate breaks '
                                      'down and the carbon dioxide it releases is trapped in the '
                                      'mixture.'},
                           {'id': 's5',
                            'yes': False,
                            'text': 'Magnesium ribbon is heated in air and leaves a white powder.',
                            'answer': 'Oxidation — two reactants joining, not one coming apart. '
                                      'The mass goes up here; in a decomposition it goes down.'}],
                 'id': 'sort-five',
                 'kind': 'decomp-sort'}],
 'ladder': {'recall': {'q': 'What is thermal decomposition?',
                       'options': ['Two or more substances joined together into one compound by '
                                   'heat',
                                   'One substance turned from a solid into a liquid by heat',
                                   'One substance joined with the oxygen in the air by heat',
                                   'One compound broken down into two or more substances by heat'],
                       'answer': 3,
                       'feedback': {0: 'That is the shape of combustion and oxidation. '
                                       'Decomposition goes the other way: one reactant, several '
                                       'products.',
                                    1: 'Melting is a physical change — same substance, different '
                                       'state, and it reverses on cooling.',
                                    2: 'That is oxidation. Decomposition needs no other reactant '
                                       'at all, and works in a tube with no air in it.'}},
            'apply': {'q': 'A tube of copper carbonate is weighed, heated until the colour change '
                           'is complete, and weighed again. What has happened to the mass, and '
                           'why?',
                      'options': ['It has risen, because oxygen joined the copper',
                                  'It has fallen, because the carbon dioxide left the tube',
                                  'It is unchanged, because mass is always conserved',
                                  'It has fallen, because some of the solid was destroyed'],
                      'answer': 1,
                      'feedback': {0: 'Nothing joined. No oxygen was needed — the reaction works '
                                      'in a tube with no air, and the oxygen in the copper oxide '
                                      'came from the carbonate itself.',
                                   2: 'Mass is conserved, and one of the products left the tube. '
                                      'The balance can only weigh what stayed.',
                                   3: 'Nothing is destroyed. Collect the gas and weigh it and the '
                                      'total comes out exactly the same.'}},
            'explain': {'q': 'A student heats copper carbonate and says "it burnt, that is why it '
                             'went black". Give two pieces of evidence from this lesson that show '
                             'they are wrong, and say what the black solid actually is.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Burning needs oxygen, and…',
                        'success': ['Says burning needs oxygen as a reactant.',
                                    'Gives the evidence that the reaction works with no air in the '
                                    'tube.',
                                    'Says the mass went down, whereas things that react with '
                                    'oxygen gain mass.',
                                    'Identifies the black solid as copper oxide, a product of the '
                                    'decomposition.',
                                    'Says the gas given off was carbon dioxide, shown by the '
                                    'limewater turning milky.']},
            'produce': {'q': 'Cement is made by decomposing limestone in kilns. Explain why this '
                             'process releases carbon dioxide even if the kiln were heated with '
                             'electricity from wind turbines, and why that makes the emissions '
                             'hard to remove.',
                        'field_label': 'Your answer',
                        'placeholder': 'The decomposition itself produces…',
                        'success': ['Says the decomposition of calcium carbonate itself produces '
                                    'carbon dioxide.',
                                    'Says that gas comes from the limestone, not from the fuel.',
                                    'Says changing the heat source removes the fuel emissions '
                                    'only.',
                                    'Says the reaction is required to make the product, so it '
                                    'cannot simply be left out.',
                                    'Suggests what would be needed instead — capturing the gas, or '
                                    'a different material altogether.']}},
 'key_note': 'Thermal decomposition breaks one compound down into two or more substances using '
             'heat. One reactant, several products, and nothing added — so it works even where '
             'there is no air. It absorbs energy for as long as you supply it, the mass left '
             'behind falls because a gas escapes, and it does not reverse on cooling.',
 'stretch': [{'type': 'explainer',
              'id': 'cement',
              'text': 'One thermal decomposition is carried out on an industrial scale that dwarfs '
                      'everything else in this unit. Limestone is heated in kilns to around 900 °C '
                      'to make calcium oxide — quicklime — which is the basis of cement. The '
                      'reaction is unavoidable and it releases carbon dioxide from the rock '
                      'itself, before you count the fuel used to heat the kiln. Cement production '
                      "is responsible for something like 8% of the world's carbon dioxide "
                      'emissions, and the chemistry means you cannot fix it by changing the fuel '
                      'alone.'},
             {'type': 'explainer',
              'id': 'cakes-and-airbags',
              'text': 'The same reaction type is why cakes rise, and why an airbag can inflate in '
                      'thirty milliseconds. Sodium hydrogencarbonate in baking powder decomposes '
                      'in the oven and the carbon dioxide it releases is trapped as bubbles in the '
                      'batter. An airbag holds a solid, sodium azide, which decomposes to nitrogen '
                      'gas fast enough to fill a bag before your head arrives — a reaction chosen '
                      'precisely because one solid becomes an enormous volume of gas, on '
                      'command.'}],
 'support': [],
 'vocabulary': [{'term': 'thermal decomposition',
                 'definition': 'Breaking one compound down into two or more substances using heat. '
                               'Nothing else is added, and it does not go back when it cools.'},
                {'term': 'compound',
                 'definition': 'A substance made of two or more different kinds of atom joined '
                               'together. Copper carbonate is copper, carbon and oxygen joined.'},
                {'term': 'reactant',
                 'definition': 'A substance you start with. A decomposition has only one, which is '
                               'what makes it unusual.'},
                {'term': 'product',
                 'definition': 'A substance you end up with. A decomposition makes two or more of '
                               'them from a single reactant.'},
                {'term': 'limewater',
                 'definition': 'A clear liquid used to test a gas. It turns milky when carbon '
                               'dioxide is bubbled through it, and for nothing else.',
                 'note': 'Milky and cloudy mean the same thing here.'},
                {'term': 'quicklime',
                 'definition': 'The everyday name for calcium oxide, the white solid left when '
                               'limestone is decomposed. It is the basis of cement.'},
                {'term': 'absorbs energy',
                 'definition': 'Takes energy in rather than giving it out. A decomposition absorbs '
                               'energy for as long as you keep heating it, which is why it stops '
                               'when the flame comes off.'}],
 'safety_note': 'These are demonstrations, not things to try at home. Take the tube carrying the '
                'gas out of the limewater before the flame comes off, or cold liquid is drawn back '
                'into the hot test tube and cracks it.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why nothing burnt in the tube?',
           'cta': 'Ask about this lesson',
           'anchor': 's-think'},
 'ks4_becomes': 'Endothermic reactions and reaction profiles, and thermal decomposition in the '
                'extraction of metals and the making of cement.',
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
