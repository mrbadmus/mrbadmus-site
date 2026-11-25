# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C6 `making-a-pure-dry-salt` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 860c783d26. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C6'
SOURCE_SLUG = 'making-a-pure-dry-salt'
FROZEN_FROM = '860c783d26'

LESSON = {'slug': 'making-a-pure-dry-salt',
 'title': 'Making a pure dry salt',
 'discipline': 'chemistry',
 'unit': 'acids-and-alkalis',
 'family': 'INVESTIGATION',
 'covers': ['KS3.C.CR.07b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3},
             {'id': 'measurement-and-uncertainty', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['neutralisation'],
 'assumes': [],
 'references': [{'unit': 'C3', 'lesson': 'evaporation-and-crystallisation'}],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Blue crystals big enough to hold, grown from a beaker of clear acid and a '
                 'spoonful of black powder. Every step of getting there is a decision you can get '
                 'wrong.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Blue crystals', 'done_when': 'committed'},
          {'anchor': 's-name',
           'short': 'NAME',
           'label': 'Naming bench',
           'done_when': 'three_named'},
          {'anchor': 's-method',
           'short': 'METHOD',
           'label': 'Build the method',
           'done_when': 'all_six_placed'},
          {'anchor': 's-think', 'short': 'THINK', 'label': 'Boiling dry', 'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'You are asked for a jar of pure copper sulfate crystals. You are given '
                         'sulfuric acid and black copper oxide powder.',
                'prompt': 'The reaction itself is easy — the acid neutralises the oxide and the '
                          'solution turns blue. The hard part is what comes after: getting a pure, '
                          'dry, crystalline solid out of a beaker of blue liquid, with no leftover '
                          'acid and no black powder in it.',
                'commit': 'If you had to guess, how much black powder should you add to the acid: '
                          'only just enough, or slightly too much?',
                'options': ['Only just enough', 'Slightly too much'],
                'reveal': 'After that come more decisions, all about getting clean crystals out of '
                          'a blue liquid. Next: how salts get their names, then the six steps in '
                          'order.',
                'guess': True,
                'replies': ['Just enough sounds neat, but you cannot see when the acid has run '
                            'out. Extra powder is easy to filter off later, and leftover acid is '
                            'not.',
                            'Extra powder does not dissolve, so it sinks and you can filter it '
                            'off. That way you know every drop of acid has been used up.'],
                'answer': 1},
 'misconceptions': [{'id': 'ACID-09',
                     'statement': 'Boiling a solution dry gives the best crystals.',
                     'elicited_by': 'think-commit-boil',
                     'confronted_by': 'think-commit-boil'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': "Every neutralisation makes a salt, and the salt's name is built from the two "
                   'things that made it. The <strong>metal</strong> gives the first word. The '
                   '<strong>acid</strong> gives the second: hydrochloric makes chlorides, sulfuric '
                   'makes sulfates, nitric makes nitrates.'},
          {'type': 'explainer',
           'text': 'So the name tells you the recipe backwards. Copper sulfate had to come from '
                   'copper — as the metal, its oxide, its hydroxide or its carbonate — and '
                   'sulfuric acid. Nothing else could have made it.'},
          {'type': 'check', 'id': 'namer-twelve', 'anchor': 's-name'},
          {'type': 'check', 'id': 'method-six', 'anchor': 's-method'},
          {'type': 'key-fact', 'ref': 'excess-then-filter'},
          {'type': 'misconception',
           'id': 'think-commit-boil',
           'anchor': 's-think',
           'targets': 'ACID-09'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'excess-then-filter',
                'text': 'The metal names the salt and the acid names its ending. Use excess '
                        'insoluble base, filter it off, then crystallise — because excess solid '
                        'can be removed and excess acid cannot.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-boil',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ACID-09',
                 'prompt': 'You do get a solid, and quickly. Commit before you read on.',
                 'options': ['Right — heat gets the water off quickest, so the crystals come '
                             'sooner',
                             'Wrong — boiling dry gives a caked powder; crystals need slow cooling',
                             'Right, because the crystals cannot boil away once the water has gone',
                             'Wrong — the salt itself would be destroyed by the heat of boiling'],
                 'reveal': ['You get a solid, but not crystals. Boiling to dryness throws '
                            'thousands of tiny crystals out of solution at once and leaves a caked '
                            'powder, with whatever else was dissolved in the water trapped in it. '
                            'Crystals need time: heat the solution until it is concentrated, stop '
                            'while there is still liquid, and let it cool slowly.',
                            'This is the same rule you met when you crystallised salt from '
                            'solution — fast drying gives powder, slow cooling gives crystals. '
                            '<strong>Big clean crystals are a product of patience, not '
                            'heat.</strong>']},
                {'eyebrow': 'Your turn · the naming bench',
                 'heading': 'Pick an acid and a base. Name the salt before you check.',
                 'prompt': 'Twelve are possible — three is enough to see the rule.',
                 'demand': 'construct',
                 'acid_label': 'The acid',
                 'base_label': 'The base',
                 'ask_prompt': 'Which salt does this make?',
                 'acids': [{'id': 'hcl',
                            'label': 'Hydrochloric',
                            'name': 'hydrochloric acid',
                            'ending': 'chloride'},
                           {'id': 'h2so4',
                            'label': 'Sulfuric',
                            'name': 'sulfuric acid',
                            'ending': 'sulfate'},
                           {'id': 'hno3',
                            'label': 'Nitric',
                            'name': 'nitric acid',
                            'ending': 'nitrate'}],
                 'bases': [{'id': 'cuo',
                            'label': 'Copper oxide',
                            'name': 'copper oxide',
                            'metal': 'copper',
                            'kind': 'oxide',
                            'soluble': False},
                           {'id': 'mgo',
                            'label': 'Magnesium oxide',
                            'name': 'magnesium oxide',
                            'metal': 'magnesium',
                            'kind': 'oxide',
                            'soluble': False},
                           {'id': 'naoh',
                            'label': 'Sodium hydroxide',
                            'name': 'sodium hydroxide',
                            'metal': 'sodium',
                            'kind': 'hydroxide',
                            'soluble': True},
                           {'id': 'caco3',
                            'label': 'Calcium carbonate',
                            'name': 'calcium carbonate',
                            'metal': 'calcium',
                            'kind': 'carbonate',
                            'soluble': False}],
                 'mixes': [{'id': 'hcl:cuo',
                            'title': 'Hydrochloric acid + copper oxide',
                            'salt': 'copper chloride',
                            'options': ['Copper chloride', 'Copper sulfate', 'Sodium chloride'],
                            'answer': 0,
                            'eq_left': 'hydrochloric acid + copper oxide',
                            'eq_right': 'copper chloride + water',
                            'note': 'Copper oxide is insoluble, so you can add it in excess and '
                                    'filter off what is left.'},
                           {'id': 'hcl:mgo',
                            'title': 'Hydrochloric acid + magnesium oxide',
                            'salt': 'magnesium chloride',
                            'options': ['Magnesium sulfate',
                                        'Magnesium chloride',
                                        'Copper chloride'],
                            'answer': 1,
                            'eq_left': 'hydrochloric acid + magnesium oxide',
                            'eq_right': 'magnesium chloride + water',
                            'note': 'Magnesium oxide is insoluble, so you can add it in excess and '
                                    'filter off what is left.'},
                           {'id': 'hcl:naoh',
                            'title': 'Hydrochloric acid + sodium hydroxide',
                            'salt': 'sodium chloride',
                            'options': ['Sodium sulfate', 'Copper chloride', 'Sodium chloride'],
                            'answer': 2,
                            'eq_left': 'hydrochloric acid + sodium hydroxide',
                            'eq_right': 'sodium chloride + water',
                            'note': 'Sodium hydroxide dissolves, so excess cannot be filtered off '
                                    '— this salt has to be made by titration instead.'},
                           {'id': 'hcl:caco3',
                            'title': 'Hydrochloric acid + calcium carbonate',
                            'salt': 'calcium chloride',
                            'options': ['Calcium chloride', 'Calcium sulfate', 'Copper chloride'],
                            'answer': 0,
                            'eq_left': 'hydrochloric acid + calcium carbonate',
                            'eq_right': 'calcium chloride + water + carbon dioxide',
                            'note': 'A carbonate gives carbon dioxide as well, so this one fizzes '
                                    'while it reacts. Calcium carbonate is insoluble, so you can '
                                    'add it in excess and filter off what is left.'},
                           {'id': 'h2so4:cuo',
                            'title': 'Sulfuric acid + copper oxide',
                            'salt': 'copper sulfate',
                            'options': ['Copper chloride', 'Copper sulfate', 'Sodium sulfate'],
                            'answer': 1,
                            'eq_left': 'sulfuric acid + copper oxide',
                            'eq_right': 'copper sulfate + water',
                            'note': 'Copper oxide is insoluble, so you can add it in excess and '
                                    'filter off what is left.'},
                           {'id': 'h2so4:mgo',
                            'title': 'Sulfuric acid + magnesium oxide',
                            'salt': 'magnesium sulfate',
                            'options': ['Magnesium chloride',
                                        'Copper sulfate',
                                        'Magnesium sulfate'],
                            'answer': 2,
                            'eq_left': 'sulfuric acid + magnesium oxide',
                            'eq_right': 'magnesium sulfate + water',
                            'note': 'Magnesium oxide is insoluble, so you can add it in excess and '
                                    'filter off what is left.'},
                           {'id': 'h2so4:naoh',
                            'title': 'Sulfuric acid + sodium hydroxide',
                            'salt': 'sodium sulfate',
                            'options': ['Sodium sulfate', 'Sodium chloride', 'Copper sulfate'],
                            'answer': 0,
                            'eq_left': 'sulfuric acid + sodium hydroxide',
                            'eq_right': 'sodium sulfate + water',
                            'note': 'Sodium hydroxide dissolves, so excess cannot be filtered off '
                                    '— this salt has to be made by titration instead.'},
                           {'id': 'h2so4:caco3',
                            'title': 'Sulfuric acid + calcium carbonate',
                            'salt': 'calcium sulfate',
                            'options': ['Calcium chloride', 'Calcium sulfate', 'Copper sulfate'],
                            'answer': 1,
                            'eq_left': 'sulfuric acid + calcium carbonate',
                            'eq_right': 'calcium sulfate + water + carbon dioxide',
                            'note': 'A carbonate gives carbon dioxide as well, so this one fizzes '
                                    'while it reacts. Calcium sulfate barely dissolves either, so '
                                    'it coats the chips and the reaction stops almost at once. '
                                    'This is a salt you can name by the rule but not make by this '
                                    'method.'},
                           {'id': 'hno3:cuo',
                            'title': 'Nitric acid + copper oxide',
                            'salt': 'copper nitrate',
                            'options': ['Copper chloride', 'Sodium nitrate', 'Copper nitrate'],
                            'answer': 2,
                            'eq_left': 'nitric acid + copper oxide',
                            'eq_right': 'copper nitrate + water',
                            'note': 'Copper oxide is insoluble, so you can add it in excess and '
                                    'filter off what is left.'},
                           {'id': 'hno3:mgo',
                            'title': 'Nitric acid + magnesium oxide',
                            'salt': 'magnesium nitrate',
                            'options': ['Magnesium nitrate',
                                        'Magnesium chloride',
                                        'Copper nitrate'],
                            'answer': 0,
                            'eq_left': 'nitric acid + magnesium oxide',
                            'eq_right': 'magnesium nitrate + water',
                            'note': 'Magnesium oxide is insoluble, so you can add it in excess and '
                                    'filter off what is left.'},
                           {'id': 'hno3:naoh',
                            'title': 'Nitric acid + sodium hydroxide',
                            'salt': 'sodium nitrate',
                            'options': ['Sodium chloride', 'Sodium nitrate', 'Copper nitrate'],
                            'answer': 1,
                            'eq_left': 'nitric acid + sodium hydroxide',
                            'eq_right': 'sodium nitrate + water',
                            'note': 'Sodium hydroxide dissolves, so excess cannot be filtered off '
                                    '— this salt has to be made by titration instead.'},
                           {'id': 'hno3:caco3',
                            'title': 'Nitric acid + calcium carbonate',
                            'salt': 'calcium nitrate',
                            'options': ['Calcium chloride', 'Copper nitrate', 'Calcium nitrate'],
                            'answer': 2,
                            'eq_left': 'nitric acid + calcium carbonate',
                            'eq_right': 'calcium nitrate + water + carbon dioxide',
                            'note': 'A carbonate gives carbon dioxide as well, so this one fizzes '
                                    'while it reacts. Calcium carbonate is insoluble, so you can '
                                    'add it in excess and filter off what is left.'}],
                 'done_at': 3,
                 'id': 'namer-twelve',
                 'kind': 'salt-namer'},
                {'eyebrow': 'Your turn · build the method',
                 'heading': 'Six steps, shuffled. Put them in the order you would do them.',
                 'prompt': 'Three of the six carry a decision that could ruin the crystals, and '
                           'the order is what makes each of them possible.',
                 'demand': 'construct',
                 'steps': [{'id': 'm1',
                            'text': 'Warm the acid gently in a beaker.',
                            'why': 'Warming speeds the reaction up. It is not boiled — that would '
                                   'drive acid off before it has reacted with anything.'},
                           {'id': 'm2',
                            'text': 'Add the copper oxide a spatula at a time, stirring, until no '
                                    'more will react.',
                            'why': 'Excess is deliberate. The black powder settling out means '
                                   'every last bit of acid has been used up, which is the only way '
                                   'to be sure none is left in your product.'},
                           {'id': 'm3',
                            'text': 'Filter the mixture to remove the leftover copper oxide.',
                            'why': 'The excess base is insoluble, so it stays on the filter paper '
                                   'while the blue copper sulfate solution passes through. This is '
                                   'the step that pays for adding too much.'},
                           {'id': 'm4',
                            'text': 'Heat the filtrate to evaporate about half the water.',
                            'why': 'Concentrating the solution, not drying it. You stop while '
                                   'there is still plenty of liquid — the test is a drop on a cold '
                                   'glass rod forming crystals.'},
                           {'id': 'm5',
                            'text': 'Leave the concentrated solution to cool slowly.',
                            'why': 'Slow cooling is what grows large, regular crystals. Fast '
                                   'cooling gives a mass of tiny ones, and boiling to dryness '
                                   'gives powder.'},
                           {'id': 'm6',
                            'text': 'Pat the crystals dry between filter papers.',
                            'why': 'The last of the mother liquor is dissolved salt, and it would '
                                   'dry as a crust on the surface. Patting rather than rubbing '
                                   'keeps the crystals whole.'}],
                 'shuffled': ['m3', 'm5', 'm1', 'm6', 'm2', 'm4'],
                 'clear_label': 'Start the order again',
                 'why_join': '—',
                 'verdicts': {'right': 'That is the order, and every step earns its place.',
                              'wrong': 'Not the order that works. Here is the sequence and what '
                                       'each step is for.'},
                 'id': 'method-six',
                 'kind': 'method-order'}],
 'ladder': {'recall': {'q': 'Nitric acid is neutralised with magnesium oxide. What salt is made?',
                       'options': ['Magnesium sulfate',
                                   'Magnesium chloride',
                                   'Magnesium nitrate',
                                   'Magnesium hydroxide'],
                       'answer': 2,
                       'feedback': {0: 'Sulfates come from sulfuric acid. Nitric acid makes '
                                       'nitrates.',
                                    1: 'Chlorides come from hydrochloric acid. Nitric acid makes '
                                       'nitrates.',
                                    3: "Magnesium hydroxide is a base. The salt's ending comes "
                                       'from nitric acid.'}},
            'apply': {'q': 'Why is excess copper oxide added rather than an exactly measured '
                           'amount?',
                      'options': ['Extra copper oxide makes more salt, so the yield keeps going up',
                                  'Extra copper oxide dissolves in the water, so the crystals grow '
                                  'bigger',
                                  'Extra copper oxide is a catalyst, so it is not used up in the '
                                  'reaction',
                                  'Extra copper oxide uses up the acid, so no acid stays in the '
                                  'solution'],
                      'answer': 3,
                      'feedback': {0: 'Once the acid is used up, extra copper oxide makes no more '
                                      'salt.',
                                   1: 'Copper oxide does not dissolve. That is why the extra can '
                                      'be filtered off.',
                                   2: 'Copper oxide is a reactant, so it gets used up. The extra '
                                      'is left over.'}},
            'explain': {'q': 'Describe how you would make pure, dry crystals of magnesium sulfate '
                             'from sulfuric acid and magnesium oxide, and explain the reason '
                             'behind each of the three decisions that could ruin it.',
                        'field_label': 'Your method',
                        'placeholder': 'I would warm the acid and then…',
                        'success': ['Adds magnesium oxide in excess to warm sulfuric acid, '
                                    'stirring.',
                                    'Filters to remove the unreacted magnesium oxide.',
                                    'Evaporates some of the water rather than boiling to dryness.',
                                    'Leaves the solution to cool slowly so crystals grow.',
                                    'Explains that excess is used because the solid can be '
                                    'filtered off but excess acid could not.']},
            'produce': {'q': 'A student needs to make sodium chloride crystals from hydrochloric '
                             'acid and sodium hydroxide. Explain why the method above will not '
                             'work, and what they must do instead.',
                        'field_label': 'Your answer',
                        'placeholder': 'Sodium hydroxide is different because…',
                        'success': ['Says sodium hydroxide is soluble, so excess cannot be '
                                    'filtered off.',
                                    'Says there is no visible sign of when enough has been added.',
                                    'Says an indicator is used to find the exact volume that '
                                    'neutralises the acid.',
                                    'Says the experiment is then repeated with the same volumes '
                                    'and no indicator.',
                                    'Says the solution is then evaporated and cooled slowly to '
                                    'crystallise, as before.']}},
 'key_note': 'A salt is named after the metal and the acid that made it: sulfuric acid gives '
             'sulfates, hydrochloric gives chlorides, nitric gives nitrates. To make a pure '
             'sample, react the acid with excess insoluble base, filter off what is left over, '
             'then evaporate part of the water and let the solution cool slowly so crystals grow.',
 'stretch': [{'type': 'explainer',
              'id': 'the-soluble-case',
              'text': 'Making a salt with a soluble alkali instead of an insoluble base is a much '
                      'harder job, and it is worth knowing why. Sodium hydroxide dissolves, so '
                      'excess cannot be filtered off — there is no way to see when you have added '
                      'enough. The answer is to do the reaction twice: once with indicator to find '
                      'the exact volume that neutralises the acid, then again with the same '
                      'volumes and no indicator, so the crystals are not stained with dye.'},
             {'type': 'explainer',
              'id': 'salts-are-not-curiosities',
              'text': 'Salts are not laboratory curiosities. Ammonium nitrate and ammonium '
                      'sulfate, made by neutralising acids with ammonia, are the fertilisers that '
                      'feed a large fraction of the world; the process that makes the ammonia '
                      'consumes about one per cent of all energy generated on Earth. Copper '
                      'sulfate goes on vines as a fungicide, calcium sulfate is plasterboard, and '
                      'sodium chloride is on the table.'}],
 'support': [],
 'vocabulary': [{'term': 'Salt',
                 'definition': 'The compound made when an acid reacts with a base. The metal names '
                               'it and the acid gives it its ending.'},
                {'term': 'Excess',
                 'definition': 'More than enough. Adding an insoluble base in excess guarantees no '
                               'acid is left, and what is left over can be filtered out.'},
                {'term': 'Insoluble',
                 'definition': 'Will not dissolve. An insoluble base sits on the bottom of the '
                               'beaker once the acid is used up, which is how you know to stop.'},
                {'term': 'Filtrate',
                 'definition': 'The liquid that passes through the filter paper. Here it is the '
                               'salt solution, with the leftover solid left behind.'},
                {'term': 'Crystallise',
                 'definition': 'To grow crystals out of a solution by concentrating it and letting '
                               'it cool slowly.',
                 'note': 'Boiling to dryness is not crystallising — it gives powder.'},
                {'term': 'Soluble',
                 'definition': 'Will dissolve. A soluble base cannot be added in excess, because '
                               'there would be no way to remove what was left over.'}],
 'safety_note': 'Copper compounds are harmful if swallowed and the warm acid stage spits if it is '
                'allowed to boil. Eye protection throughout, the crystals are never tasted, and '
                'the evaporating basin is left to cool before it is handled.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why you add too much of the base on purpose?',
           'cta': 'Ask about this lesson',
           'anchor': 's-method'},
 'ks4_becomes': 'Preparing soluble salts by titration, calculating percentage yield, and '
                'predicting solubility from the rules.',
 'ws': ['experimental-skills-and-investigations', 'measurement'],
 'review_state': 'draft',
 'authored': True}
