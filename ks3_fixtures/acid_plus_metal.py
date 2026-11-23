# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C6 `acid-plus-metal` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 860c783d26. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C6'
SOURCE_SLUG = 'acid-plus-metal'
FROZEN_FROM = '860c783d26'

LESSON = {'slug': 'acid-plus-metal',
 'title': 'Acid + metal',
 'discipline': 'chemistry',
 'unit': 'acids-and-alkalis',
 'family': 'PROCESS',
 'covers': ['KS3.C.CR.06'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'substances-and-reactions', 'level': 3}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['neutralisation'],
 'assumes': [],
 'references': [{'unit': 'C5', 'lesson': 'displacement'}],
 'connects_heading': 'Next in this unit',
 'ks4_links': [],
 'big_question': 'Drop magnesium into acid and the tube fizzes hard enough to warm your hand. Drop '
                 'copper in and nothing happens at all — for a week.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The squeak', 'done_when': 'committed'},
          {'anchor': 's-bench', 'short': 'TUBES', 'label': 'Eight tubes', 'done_when': 'six_run'},
          {'anchor': 's-test',
           'short': 'TEST',
           'label': 'Testing the gas',
           'done_when': 'all_three_decided'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'What the bubbles are',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A strip of magnesium goes into dilute hydrochloric acid. The tube fills '
                         'with bubbles and the metal disappears.',
                'prompt': 'The tube gets warm. Within a minute the magnesium is gone and the '
                          'liquid is clear. Collect the gas coming off, hold a lit splint to it, '
                          'and it goes off with a squeak.',
                'commit': 'If you had to guess, did the gas come from the metal, or from the acid?',
                'options': ['From the metal', 'From the acid'],
                'reveal': 'The metal and the hydrogen swap places. Next: the rule for what always '
                          'forms, then eight tubes to try with different metals and acids.',
                'guess': True,
                'replies': ['It does look that way, because the metal vanishes as the bubbles '
                            'appear. But the metal has dissolved into the liquid. The gas came out '
                            'of the acid.',
                            'Every acid has hydrogen in it. The metal pushes the hydrogen out as a '
                            'gas and takes its place in the liquid.'],
                'answer': 1},
 'misconceptions': [{'id': 'ACID-07',
                     'statement': 'The bubbles are the metal turning into gas.',
                     'elicited_by': 'think-commit-fizz',
                     'confronted_by': 'think-commit-fizz'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'A reactive metal reacts with an acid, and there are always two products.'},
          {'type': 'rule',
           'id': 'salt-plus-hydrogen',
           'eyebrow': 'The rule',
           'statement': 'A reactive metal and an acid always make the same two things.',
           'equation': {'reactants': 'acid + metal',
                        'arrow': 'makes',
                        'products': 'salt + hydrogen',
                        'condition': 'the hydrogen comes out of the acid, not the metal'},
           'close': 'Which salt depends on the acid. Hydrochloric acid makes '
                    '<strong>chlorides</strong>, sulfuric acid makes <strong>sulfates</strong>, '
                    "nitric acid makes <strong>nitrates</strong>. The first word of the salt's "
                    'name is the metal; the second comes from the acid.'},
          {'type': 'explainer',
           'text': 'And it only happens if the metal is reactive enough. The reactivity series '
                   'decides which tubes fizz and which sit there doing nothing.'},
          {'type': 'check', 'id': 'grid-eight', 'anchor': 's-bench'},
          {'type': 'key-fact', 'ref': 'out-of-the-acid'},
          {'type': 'check', 'id': 'test-three', 'anchor': 's-test'},
          {'type': 'misconception',
           'id': 'think-commit-fizz',
           'anchor': 's-think',
           'targets': 'ACID-07'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'figures': [],
 'key_facts': [{'id': 'out-of-the-acid',
                'text': 'acid + metal makes salt + hydrogen. The hydrogen comes out of the acid, '
                        'not the metal, and a lit splint gives a squeaky pop.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'think-commit-fizz',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'ACID-07',
                 'prompt': 'The magnesium does vanish, and bubbles do come off. Commit before you '
                           'read on.',
                 'options': ['Right — the metal boils away as bubbles, which is why the strip '
                             'disappears from the tube',
                             'Wrong — the bubbles are hydrogen from the acid; the metal is '
                             'dissolved as a salt',
                             'Right, because the metal is gone at the end and the gas is the only '
                             'thing that left',
                             'Wrong — the bubbles are air that was pushed out of the liquid as the '
                             'strip sank into it'],
                 'reveal': ['Two different things are happening and they are easy to run together. '
                            'The <strong>bubbles</strong> are hydrogen, which came out of the '
                            'acid. The <strong>metal</strong> has gone into solution as a salt — '
                            'dissolved, invisible, and still every atom present.',
                            'You can prove both halves. The gas pops with a lit splint, which '
                            'magnesium vapour would not do. And evaporating the liquid leaves '
                            'white magnesium chloride crystals, which were not there when you '
                            'started. <strong>The metal did not become the gas — it swapped places '
                            'with the hydrogen in the acid.</strong>']},
                {'eyebrow': 'Your turn · eight tubes',
                 'heading': 'Four metals, two acids. Pick a tube, predict, then run it.',
                 'prompt': 'The copper row is worth running as well — a tube that does nothing is '
                           'telling you something precise.',
                 'demand': 'investigate',
                 'head_counter': {'format': '{n} of {total} run', 'start': 0},
                 'metals': [{'id': 'mg', 'name': 'Magnesium'},
                            {'id': 'zn', 'name': 'Zinc'},
                            {'id': 'fe', 'name': 'Iron'},
                            {'id': 'cu', 'name': 'Copper'}],
                 'acids': [{'id': 'hcl', 'name': 'hydrochloric acid', 'salt': 'chloride'},
                           {'id': 'h2so4', 'name': 'sulfuric acid', 'salt': 'sulfate'}],
                 'cells': [{'id': 'mg:hcl',
                            'reacts': True,
                            'mark': 'fizzes',
                            'aria': 'Magnesium in hydrochloric acid',
                            'title': 'Magnesium in hydrochloric acid',
                            'setup': 'A measured strip of magnesium dropped into 10 cm³ of dilute '
                                     'hydrochloric acid at room temperature.',
                            'result': 'Vigorous. Bubbles stream off and the tube becomes hot to '
                                      'hold. Over in under a minute.',
                            'why': 'Magnesium is high above hydrogen in the reactivity series, so '
                                   "it takes the hydrogen's place in the acid without hesitating. "
                                   'The hydrogen is pushed out as a gas and the magnesium ends up '
                                   'dissolved as magnesium chloride — which is why the strip '
                                   'disappears and the liquid stays clear.',
                            'eq_left': 'hydrochloric acid + magnesium',
                            'eq_right': 'magnesium chloride + hydrogen'},
                           {'id': 'mg:h2so4',
                            'reacts': True,
                            'mark': 'fizzes',
                            'aria': 'Magnesium in sulfuric acid',
                            'title': 'Magnesium in sulfuric acid',
                            'setup': 'A measured strip of magnesium dropped into 10 cm³ of dilute '
                                     'sulfuric acid at room temperature.',
                            'result': 'Vigorous again, and just as fast. The tube warms and the '
                                      'strip is gone within the minute.',
                            'why': 'The same metal doing the same thing, because the reactivity '
                                   'series does not care which acid the hydrogen came out of. What '
                                   'changes is the salt left behind: sulfuric acid gives a '
                                   'sulfate, so this tube ends up holding magnesium sulfate.',
                            'eq_left': 'sulfuric acid + magnesium',
                            'eq_right': 'magnesium sulfate + hydrogen'},
                           {'id': 'zn:hcl',
                            'reacts': True,
                            'mark': 'fizzes',
                            'aria': 'Zinc in hydrochloric acid',
                            'title': 'Zinc in hydrochloric acid',
                            'setup': 'Measured zinc granules dropped into 10 cm³ of dilute '
                                     'hydrochloric acid at room temperature.',
                            'result': 'Steady. A constant stream of small bubbles and a tube that '
                                      'warms gently over several minutes.',
                            'why': 'Zinc is above hydrogen too, but not as far above it as '
                                   'magnesium — so the same reaction runs at a pace you can watch '
                                   'rather than one you have to catch. The salt is zinc chloride.',
                            'eq_left': 'hydrochloric acid + zinc',
                            'eq_right': 'zinc chloride + hydrogen'},
                           {'id': 'zn:h2so4',
                            'reacts': True,
                            'mark': 'fizzes',
                            'aria': 'Zinc in sulfuric acid',
                            'title': 'Zinc in sulfuric acid',
                            'setup': 'Measured zinc granules dropped into 10 cm³ of dilute '
                                     'sulfuric acid at room temperature.',
                            'result': 'Steady, the same as with the other acid. Small bubbles, '
                                      'several minutes, a tube that warms.',
                            'why': 'This is the tube a school uses when it wants a jar of '
                                   'hydrogen: fast enough to fill one and slow enough to control. '
                                   'The salt is zinc sulfate, and it is the same zinc sulfate '
                                   'whether you make it from the metal or from zinc oxide.',
                            'eq_left': 'sulfuric acid + zinc',
                            'eq_right': 'zinc sulfate + hydrogen'},
                           {'id': 'fe:hcl',
                            'reacts': True,
                            'mark': 'fizzes',
                            'aria': 'Iron in hydrochloric acid',
                            'title': 'Iron in hydrochloric acid',
                            'setup': 'Measured iron filings dropped into 10 cm³ of dilute '
                                     'hydrochloric acid at room temperature.',
                            'result': 'Slow. A few bubbles clinging to the filings, and it takes '
                                      'most of a lesson to see much change.',
                            'why': 'Iron is only just above hydrogen, so it does displace it — but '
                                   'barely, and you need patience to see it. That narrow margin is '
                                   'the whole reason iron rusts away in wet air over years rather '
                                   'than in minutes.',
                            'eq_left': 'hydrochloric acid + iron',
                            'eq_right': 'iron chloride + hydrogen'},
                           {'id': 'fe:h2so4',
                            'reacts': True,
                            'mark': 'fizzes',
                            'aria': 'Iron in sulfuric acid',
                            'title': 'Iron in sulfuric acid',
                            'setup': 'Measured iron filings dropped into 10 cm³ of dilute sulfuric '
                                     'acid at room temperature.',
                            'result': 'Slow again, and the liquid turns a pale green as the '
                                      'filings go into solution.',
                            'why': 'Slowest of the three that work, in either acid, which places '
                                   'iron at the bottom of the reacting metals here. The pale green '
                                   'is the iron sulfate dissolving — the metal has not vanished, '
                                   'it has changed into something that dissolves.',
                            'eq_left': 'sulfuric acid + iron',
                            'eq_right': 'iron sulfate + hydrogen'},
                           {'id': 'cu:hcl',
                            'reacts': False,
                            'mark': 'none',
                            'aria': 'Copper in hydrochloric acid',
                            'title': 'Copper in hydrochloric acid',
                            'setup': 'Measured copper turnings dropped into 10 cm³ of dilute '
                                     'hydrochloric acid at room temperature.',
                            'result': 'Nothing. Not in twenty minutes, not in a week.',
                            'why': 'Copper sits BELOW hydrogen in the reactivity series, so it '
                                   'cannot push hydrogen out of an acid. There is no slow reaction '
                                   'here to wait for — there is no reaction at all, and warming '
                                   'it, stirring it or leaving it out overnight all give the same '
                                   'result.',
                            'eq_left': '',
                            'eq_right': ''},
                           {'id': 'cu:h2so4',
                            'reacts': False,
                            'mark': 'none',
                            'aria': 'Copper in sulfuric acid',
                            'title': 'Copper in sulfuric acid',
                            'setup': 'Measured copper turnings dropped into 10 cm³ of dilute '
                                     'sulfuric acid at room temperature.',
                            'result': 'Nothing again. The turnings are as bright at the end as '
                                      'they were at the start.',
                            'why': 'Changing the acid changes nothing, and that is the point of '
                                   'running the second copper tube at all. What decides this is '
                                   'where copper sits relative to hydrogen, and that is a fact '
                                   'about copper — so no acid you could reach for on this bench '
                                   'would give a different answer.',
                            'eq_left': '',
                            'eq_right': ''}],
                 'corner_label': 'Metal added to',
                 'table_label': 'Four metals crossed with two acids',
                 'unrun_mark': '?',
                 'predict_prompt': 'Predict before you run it.',
                 'predict_options': [{'id': 'fast', 'label': 'Fizzes hard'},
                                     {'id': 'slow', 'label': 'Fizzes slowly'},
                                     {'id': 'none', 'label': 'Nothing happens'}],
                 'done_at': 6,
                 'close': {'id': 'grid-pattern',
                           'title': 'Two patterns, not one.',
                           'paras': ['Read down the columns and the speed falls in the order '
                                     'magnesium, zinc, iron, copper — the reactivity series again, '
                                     'arrived at by a different route. Read across the rows and '
                                     'the metal decides the first word of the salt while the acid '
                                     'decides the second: chloride from hydrochloric, sulfate from '
                                     'sulfuric.',
                                     'Copper is the row that proves the rule. It is below hydrogen '
                                     'in the reactivity series, so it cannot push hydrogen out of '
                                     'an acid — and no amount of waiting will change that.']},
                 'id': 'grid-eight',
                 'kind': 'acid-metal-grid'},
                {'eyebrow': 'Three judgements · testing the gas',
                 'heading': 'A squeak, a lit splint and a stoppered tube',
                 'prompt': 'Commit to each before reading. The third one is a genuine hazard, not '
                           'a trick question.',
                 'demand': 'explain',
                 'head_counter': {'format': '{n} of {total} decided', 'start': 0},
                 'items': [{'id': 't1',
                            'q': 'A tube of gas from magnesium and acid is tested with a lit '
                                 'splint and squeaks. Does that prove the gas is hydrogen?',
                            'options': [{'id': 'yes', 'label': 'Yes'}, {'id': 'no', 'label': 'No'}],
                            'answer': 'yes',
                            'reply': 'Yes — the squeaky pop is the standard test for hydrogen, and '
                                     'no other gas you will meet at this level does it. The squeak '
                                     'is the sound of the hydrogen burning explosively with the '
                                     'oxygen in the tube, making water.'},
                           {'id': 't2',
                            'q': 'A student holds the splint to the mouth of the tube while it is '
                                 'still fizzing hard. Is that a good idea?',
                            'options': [{'id': 'yes', 'label': 'Yes'}, {'id': 'no', 'label': 'No'}],
                            'answer': 'no',
                            'reply': 'No. The tube needs to be collected and stoppered first, and '
                                     'tested away from the reaction. Holding a flame over a vessel '
                                     'that is actively producing hydrogen means the flame can run '
                                     'back down into it — and a tube of hydrogen mixed with air '
                                     'does not squeak, it bangs.'},
                           {'id': 't3',
                            'q': 'The same test is tried on the gas from copper and acid, and '
                                 'nothing pops. Does that mean the test failed?',
                            'options': [{'id': 'yes', 'label': 'Yes'}, {'id': 'no', 'label': 'No'}],
                            'answer': 'no',
                            'reply': 'No — it means there was no gas to test. Copper sits below '
                                     'hydrogen in the reactivity series, so it cannot displace '
                                     'hydrogen from an acid. A test that correctly reports nothing '
                                     'is not a failed test, and this one has just told you where '
                                     'copper sits.'}],
                 'id': 'test-three',
                 'kind': 'acid-judgements'}],
 'ladder': {'recall': {'q': 'Zinc is added to dilute sulfuric acid. What are the products?',
                       'options': ['Zinc chloride and hydrogen',
                                   'Zinc sulfate and water',
                                   'Zinc chloride and water',
                                   'Zinc sulfate and hydrogen'],
                       'answer': 3,
                       'feedback': {0: 'Chlorides come from hydrochloric acid. Sulfuric acid makes '
                                       'sulfates.',
                                    1: 'A metal and an acid give off hydrogen. No water is made.',
                                    2: 'Sulfuric acid makes a sulfate. A metal and an acid give '
                                       'off hydrogen.'}},
            'apply': {'q': 'Copper is left in dilute hydrochloric acid for a week and nothing '
                           'happens. What is the reason?',
                      'options': ['Copper is too unreactive, so it cannot take the place of the '
                                  'hydrogen',
                                  'The acid was too cold, so warming the acid up would make the '
                                  'copper fizz',
                                  'Copper is not a metal at all, so it cannot react with any '
                                  'dilute acids',
                                  'A week is not long enough, so the copper must be left much '
                                  'longer'],
                      'answer': 0,
                      'feedback': {1: 'Warming does not help. Copper is too unreactive to give off '
                                      'hydrogen.',
                                   2: 'Copper is a metal. It is a very unreactive one.',
                                   3: 'Waiting longer does not help. Copper is too unreactive to '
                                      'give off hydrogen.'}},
            'explain': {'q': 'Magnesium is dropped into hydrochloric acid. Describe what you would '
                             'see, name both products, and explain where the gas comes from.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The magnesium…',
                        'success': ['Says bubbles of gas are given off rapidly and the metal '
                                    'disappears.',
                                    'Says the tube gets warm.',
                                    'Names the products as magnesium chloride and hydrogen.',
                                    'Says the hydrogen comes from the acid, not from the metal.',
                                    'Says the magnesium is still present, dissolved as a salt.']},
            'produce': {'q': 'You are given four unlabelled metals and a bottle of dilute '
                             'hydrochloric acid. Explain how you would put the metals in order of '
                             'reactivity, and what you would do to make it a fair comparison.',
                        'field_label': 'Your plan',
                        'placeholder': 'I would put an equal-sized piece of each metal into…',
                        'success': ['Adds an equal-sized piece of each metal to the same volume of '
                                    'the same acid.',
                                    'Keeps the acid concentration and temperature the same for '
                                    'each.',
                                    'Compares how quickly bubbles are produced.',
                                    'Says the fastest is the most reactive and any that does '
                                    'nothing is the least.',
                                    'Says a metal that does not react at all must be below '
                                    'hydrogen in the series.']}},
 'key_note': 'A metal above hydrogen in the reactivity series reacts with an acid to give a salt '
             'and hydrogen gas. The more reactive the metal, the faster the fizzing. Hydrochloric '
             'acid gives chlorides, sulfuric acid gives sulfates. Hydrogen is tested with a lit '
             'splint: it burns with a squeaky pop.',
 'stretch': [{'type': 'explainer',
              'id': 'sacrificial-anodes',
              'text': 'This reaction is why the hulls of ships are fitted with slabs of zinc '
                      'bolted to the steel below the waterline. Seawater is full of dissolved salt '
                      'and attacks iron steadily. Bolt on something more reactive and the seawater '
                      'attacks that instead: the zinc corrodes away and the hull does not. The '
                      'slabs are called sacrificial anodes, and replacing them is routine dry-dock '
                      'work.'},
             {'type': 'explainer',
              'id': 'why-acid-is-not-stored-in-metal',
              'text': 'It is also the reason nobody stores acid in a metal can. Concentrated acids '
                      'arrive in glass or plastic, and the tanker lorries that carry sulfuric acid '
                      'are lined — because a steel tank full of acid is a hydrogen generator, and '
                      'hydrogen and air together only need a spark. The gas that gives a tidy '
                      'squeak from a test tube is the same gas that took down the Hindenburg.'}],
 'support': [],
 'vocabulary': [{'term': 'Salt',
                 'definition': 'The compound made when a metal takes the place of the hydrogen in '
                               'an acid. Its first word is the metal and its second comes from the '
                               'acid.'},
                {'term': 'Reactivity series',
                 'definition': 'The order of metals from most reactive to least. A metal above '
                               'hydrogen in it will push hydrogen out of an acid; one below it '
                               'will not.'},
                {'term': 'Displace',
                 'definition': 'To take the place of something else in a compound. A reactive '
                               'metal displaces the hydrogen in an acid and the hydrogen leaves as '
                               'a gas.'},
                {'term': 'Squeaky pop',
                 'definition': 'The test for hydrogen. A lit splint held in a tube of hydrogen '
                               'makes a sharp squeak as the gas burns.',
                 'note': 'The tube is stoppered and moved away from the reaction before it is '
                         'tested.'},
                {'term': 'Chloride',
                 'definition': 'A salt made by hydrochloric acid. Sulfuric acid makes sulfates and '
                               'nitric acid makes nitrates.'}],
 'safety_note': 'Hydrogen mixed with air explodes rather than squeaking. The gas is collected in a '
                'tube, stoppered, and carried away from the fizzing flask before a lit splint goes '
                'near it — never tested at the mouth of a tube that is still reacting.',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Still not sure why copper does nothing?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'ks4_becomes': 'Redox: the metal loses electrons and hydrogen ions gain them, plus rates of '
                'reaction measured by the volume of gas collected.',
 'ws': ['experimental-skills-and-investigations', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
