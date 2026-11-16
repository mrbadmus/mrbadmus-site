# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B1 `life-processes` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B1'
SOURCE_SLUG = 'life-processes'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'life-processes',
 'title': 'Life processes and what living things are made of',
 'discipline': 'biology',
 'unit': 'cells-and-organisation',
 'family': 'CLASSIFY',
 'covers': ['KS3.B.CELLS.01a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': [],
 'assumes': [],
 'references': [{'unit': 'B1', 'lesson': 'using-a-microscope'},
                {'unit': 'B1', 'lesson': 'animal-and-plant-cells'}],
 'ks4_links': [],
 'big_question': 'A candle flame moves, grows, feeds and makes waste. What decides whether '
                 'something is alive?',
 'phenomenon': {'kind': 'demo',
                'title': 'Watch a candle for a minute',
                'prompt': 'It moves. Feed the wick and it grows. It takes in oxygen and gives out '
                          'carbon dioxide, water and soot. Open a door and it leans away. Touch a '
                          'second wick to it and there are two flames.',
                'commit': 'If you had to guess, is a candle flame alive?',
                'art': 'b1-candle-flame',
                'options': ['Yes, it is alive', 'No, it is not alive'],
                'reveal': 'Doing the life processes is not enough on its own. What settles it is '
                          'what a thing is <em>made of</em>.',
                'guess': True,
                'replies': ['It does almost everything on the list of life processes. But a flame '
                            'is not made of cells, and every living thing is.',
                            'A flame moves, grows, feeds and makes waste, and it is still not '
                            'alive. What it is missing is cells.'],
                'answer': 1},
 'misconceptions': [{'id': 'LIFE-01',
                     'statement': 'If something moves on its own it must be alive, and if it never '
                                  'moves it must not be.',
                     'elicited_by': 'seven-tests',
                     'confronted_by': 'score-does-not-settle-it'},
                    {'id': 'LIFE-02',
                     'statement': 'Doing one of the life processes is enough to count as alive — '
                                  'if it grows on its own, it is alive.',
                     'elicited_by': 'seven-tests',
                     'confronted_by': 'score-does-not-settle-it'}],
 'vocabulary': [{'term': 'organism',
                 'definition': 'A single living thing.',
                 'note': 'One organism can be one cell, or trillions of them working together. You '
                         'will meet both in this unit.'},
                {'term': 'cell',
                 'definition': 'The smallest living unit, and the thing every living thing is '
                               'built from.',
                 'note': None},
                {'term': 'life process',
                 'definition': 'One of the seven jobs that every living thing does.',
                 'note': 'The seven are movement, respiration, sensitivity, growth, reproduction, '
                         'excretion and nutrition. Many people remember them by the first letters: '
                         'MRS GREN.'}],
 'figures': [{'id': 'b1-candle-flame',
              'kind': 'css-art',
              'art': 'candle-flame',
              'caption': 'A burning candle: a flickering flame above the wick, with soot rising '
                         'from it.',
              'status': 'final'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'id': 'the-seven',
           'anchor': 's-seven',
           'text': 'Biologists describe living things by seven life processes. Their initials '
                   'spell <strong>MRS GREN</strong>.',
           'pills': [{'initial': 'M', 'label': 'Movement'},
                     {'initial': 'R', 'label': 'Respiration'},
                     {'initial': 'S', 'label': 'Sensitivity'},
                     {'initial': 'G', 'label': 'Growth'},
                     {'initial': 'R', 'label': 'Reproduction'},
                     {'initial': 'E', 'label': 'Excretion'},
                     {'initial': 'N', 'label': 'Nutrition'}]},
          {'type': 'check', 'id': 'seven-tests', 'anchor': 's-board'},
          {'type': 'key-fact', 'ref': 'what-the-seven-do'},
          {'type': 'misconception',
           'id': 'score-does-not-settle-it',
           'anchor': 's-think',
           'targets': 'LIFE-01'},
          {'type': 'rule',
           'anchor': 's-rule',
           'eyebrow': 'What settles it',
           'statement': 'Every living thing is made of cells.',
           'cards': [{'term': 'A candle flame',
                      'gloss': 'Hot glowing gas. No cells, so not alive — whatever it does.'},
                     {'term': 'An acorn',
                      'gloss': 'Cells, packed with a food store and ticking over slowly.'},
                     {'term': 'You',
                      'gloss': 'Around thirty trillion cells, all working at once.'}],
           'close': 'One cell is enough — yeast manages on one. You are somewhere near thirty '
                    'trillion. A flame has none, so however it behaves, it never joins the club.'},
          {'type': 'check', 'id': 'living-once-never', 'anchor': 's-sort'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'stretch': [{'type': 'explainer',
              'id': 'viruses',
              'text': 'A virus is not made of cells, and on its own it does none of the seven — it '
                      'cannot even copy itself without getting inside a cell. So most biologists '
                      'do not count viruses as living. A few argue the line is in the wrong place, '
                      'and that argument is still open.'}],
 'support': [],
 'activities': [{'id': 'seven-tests',
                 'kind': 'test-board',
                 'demand': 'classify',
                 'eyebrow': 'Your turn · test four things',
                 'heading': 'Run the seven tests',
                 'prompt': 'Pick a specimen. Say what you think first. Then work through the seven '
                           'tests and see how far they get you.',
                 'predict': {'prompt': 'Before you test it — alive, or not alive?',
                             'options': ['Alive', 'Not alive']},
                 'tests': [{'key': 'M', 'initial': 'M', 'name': 'Movement'},
                           {'key': 'R', 'initial': 'R', 'name': 'Respiration'},
                           {'key': 'S', 'initial': 'S', 'name': 'Sensitivity'},
                           {'key': 'G', 'initial': 'G', 'name': 'Growth'},
                           {'key': 'Rp', 'initial': 'R', 'name': 'Reproduction'},
                           {'key': 'E', 'initial': 'E', 'name': 'Excretion'},
                           {'key': 'N', 'initial': 'N', 'name': 'Nutrition'}],
                 'specimens': [{'id': 'flame',
                                'name': 'Candle flame',
                                'blurb': 'A wick, some wax and a supply of air.',
                                'results': {'M': [True,
                                                  'It climbs and leans. Nothing is carrying it — '
                                                  'the hot gas rises.'],
                                            'R': [False,
                                                  'Burning is not respiration. Respiration is a '
                                                  'controlled set of reactions inside cells.'],
                                            'S': [True,
                                                  'Open a door and it bends away from the '
                                                  'draught.'],
                                            'G': [True, 'Longer wick, bigger flame.'],
                                            'Rp': [True,
                                                   'Touch a second wick to it and there are two '
                                                   'flames.'],
                                            'E': [True,
                                                  'Carbon dioxide, water vapour and soot leave '
                                                  'it.'],
                                            'N': [True, 'Wax and oxygen go in and are used up.']},
                                'verdict_head': 'Six of seven — and still not alive.',
                                'verdict_body': 'Only respiration fails, and even that one is a '
                                                'near miss: a flame really does take in oxygen and '
                                                'give out carbon dioxide. Counting behaviours '
                                                'cannot settle this.',
                                'extra_label': 'The eighth test',
                                'extra_answer': 'No cells.',
                                'extra_note': 'A flame is hot glowing gas. There is nothing to '
                                              'look at under a microscope.'},
                               {'id': 'seed',
                                'name': 'Oak seed',
                                'blurb': 'An acorn in a drawer. It has been there four years.',
                                'results': {'M': [False, 'Nothing about it moves.'],
                                            'R': [True,
                                                  'Even dry and still, it respires — slowly enough '
                                                  'to last for years.'],
                                            'S': [True,
                                                  'Give it water and warmth and it responds by '
                                                  'starting to grow.'],
                                            'G': [False, 'Not while it sits in the drawer.'],
                                            'Rp': [False,
                                                   'Not yet. That is an oak tree’s job, decades '
                                                   'from now.'],
                                            'E': [True,
                                                  'The carbon dioxide from that slow respiration '
                                                  'leaves it.'],
                                            'N': [False,
                                                  'It is not taking food in. It is living off the '
                                                  'store packed inside it.']},
                                'verdict_head': 'Three of seven — and it is alive.',
                                'verdict_body': 'The seven are things an organism can do across '
                                                'its life, not a checklist for this second. A '
                                                'sleeping seed scores badly and is still alive.',
                                'extra_label': 'The eighth test',
                                'extra_answer': 'Made of cells.',
                                'extra_note': 'Cut it open, look down a microscope, and there they '
                                              'are — packed with a food store.'},
                               {'id': 'robot',
                                'name': 'Robot vacuum',
                                'blurb': 'Bumps around the kitchen, finds its charger, empties '
                                         'into a bin.',
                                'results': {'M': [True, 'It crosses the room on its own.'],
                                            'R': [False,
                                                  'It runs on a battery. Nothing is broken down '
                                                  'inside it to release energy.'],
                                            'S': [True,
                                                  'Sensors find the wall, the stairs and the dog.'],
                                            'G': [False,
                                                  'It leaves the factory the size it will always '
                                                  'be.'],
                                            'Rp': [False,
                                                   'A factory makes the next one. It cannot.'],
                                            'E': [False,
                                                  'It empties dust it collected. Excretion means '
                                                  'waste from your own chemistry.'],
                                            'N': [False,
                                                  'Charging is not feeding — no food goes in and '
                                                  'nothing is digested.']},
                                'verdict_head': 'Two of seven — not alive.',
                                'verdict_body': 'It is better than a flame at looking alive and '
                                                'worse at scoring. Behaviour is a poor test in '
                                                'both directions.',
                                'extra_label': 'The eighth test',
                                'extra_answer': 'No cells.',
                                'extra_note': 'Plastic, metal and a battery. Take it apart and you '
                                              'find parts, not cells.'},
                               {'id': 'yeast',
                                'name': 'Yeast in dough',
                                'blurb': 'A spoonful of dried yeast, warm water, flour and sugar.',
                                'results': {'M': [True,
                                                  'Its parts move, and it moves through the dough '
                                                  'as it grows.'],
                                            'R': [True,
                                                  'It respires the sugar — that is where the '
                                                  'bubbles of gas come from.'],
                                            'S': [True, 'It responds to warmth and to sugar.'],
                                            'G': [True, 'Each cell grows.'],
                                            'Rp': [True, 'One cell buds into two, over and over.'],
                                            'E': [True,
                                                  'Carbon dioxide and alcohol leave it as waste.'],
                                            'N': [True, 'It takes in sugar.']},
                                'verdict_head': 'Seven of seven — alive.',
                                'verdict_body': 'And every one of those jobs is done by a single '
                                                'cell. One cell is a whole organism here.',
                                'extra_label': 'The eighth test',
                                'extra_answer': 'Made of cells.',
                                'extra_note': 'One cell each. A teaspoon of dried yeast holds '
                                              'thousands of millions of them.'}],
                 'targets': 'LIFE-02'},
                {'id': 'score-does-not-settle-it',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'statements': ['If it moves and grows, it must be alive.'],
                 'prompt': 'The flame lit six lamps. The seed lit three. One of them is alive and '
                           'it is not the one with the higher score.',
                 'scorecards': [{'figure': '6 of 7',
                                 'title': 'Candle flame — not alive',
                                 'note': 'Doing the behaviours is not the same as being alive.'},
                                {'figure': '3 of 7',
                                 'title': 'Oak seed — alive',
                                 'note': 'The seven are things it <em>can</em> do across its life, '
                                         'not a checklist for this second.'}],
                 'targets': 'LIFE-01'},
                {'id': 'living-once-never',
                 'kind': 'sort-rows',
                 'demand': 'classify',
                 'eyebrow': 'Your turn · sort all eight',
                 'heading': 'Living, once living, never living',
                 'prompt': 'Three boxes, not two. Something can be made of cells that stopped '
                           'working a long time ago.',
                 'categories': ['Living', 'Once living', 'Never living'],
                 'items': [{'id': 'moss',
                            'name': 'Moss on a wall',
                            'answer': 'Living',
                            'evidence': 'Green, growing, made of cells that are working right '
                                        'now.'},
                           {'id': 'yeast',
                            'name': 'Yeast in bread dough',
                            'answer': 'Living',
                            'evidence': 'Single cells, feeding on sugar and budding into new '
                                        'ones.'},
                           {'id': 'woodlouse',
                            'name': 'A woodlouse under a stone',
                            'answer': 'Living',
                            'evidence': 'Moves, feeds, breeds — and it is built from cells.'},
                           {'id': 'spoon',
                            'name': 'A wooden spoon',
                            'answer': 'Once living',
                            'evidence': 'Wood is the leftover walls of tree cells. The cells '
                                        'themselves died when the tree was cut.'},
                           {'id': 'leather',
                            'name': 'A leather boot',
                            'answer': 'Once living',
                            'evidence': 'Skin is a tissue. Tanning preserves it long after the '
                                        'animal has gone.'},
                           {'id': 'coal',
                            'name': 'A lump of coal',
                            'answer': 'Once living',
                            'evidence': 'Squashed plants from around three hundred million years '
                                        'ago. No cells left, but it was part of living things.'},
                           {'id': 'granite',
                            'name': 'A granite pebble',
                            'answer': 'Never living',
                            'evidence': 'Crystals that grew from cooling molten rock. No cells '
                                        'were ever involved.'},
                           {'id': 'flame',
                            'name': 'A candle flame',
                            'answer': 'Never living',
                            'evidence': 'Hot glowing gas doing six of the seven processes and made '
                                        'of no cells at all.'}],
                 'reveal_label': 'Show what settles each one',
                 'self_check': {'question': 'Now the answers are showing — how many of your eight '
                                            'matched?',
                                'options': ['All eight', 'Six or seven', 'Five or fewer'],
                                'note': 'Nobody marks this but you. The ones that did not match '
                                        'are the ones worth reading again.'}}],
 'ladder': {'recall': {'q': 'Which one of these is true of every living thing, with no exceptions?',
                       'options': ['It moves from place to place',
                                   'It is made of one or more cells',
                                   'It grows bigger every day',
                                   'It takes in oxygen'],
                       'answer': 1,
                       'feedback': {0: 'A tree stays put for two hundred years. Movement inside an '
                                       'organism counts, and plenty of living things never travel.',
                                    2: 'An acorn in a drawer grows on no day at all, and a '
                                       'full-grown adult has stopped. Growth happens somewhere in '
                                       'a life, not every day of it.',
                                    3: 'Some organisms respire without oxygen — the yeast in dough '
                                       'switches to doing exactly that. Every one of them is still '
                                       'made of cells.'}},
            'apply': {'q': 'A robot vacuum crosses the floor on its own, senses the stairs and '
                           'drives to its charger when the battery is low. Which statement is '
                           'right?',
                      'options': ['It is alive — it does three of the seven',
                                  'It is not alive — nothing built by people is alive',
                                  'You would have to watch it for longer to say',
                                  'It is not alive — it is not made of cells'],
                      'answer': 3,
                      'feedback': {0: 'A flame does six and is not alive. Counting processes never '
                                      'settles it.',
                                   1: 'True of this one, but not for that reason. Bread dough is '
                                      'put together by people and the yeast in it is alive.',
                                   2: 'You would not. Open it up: parts, wiring and a battery. No '
                                      'cells, so no.'}},
            'explain': {'q': 'A candle flame moves, grows, gives out waste gases, and can start a '
                             'second flame. Explain why a scientist still says it is not alive.',
                        'field_label': 'Your answer',
                        'placeholder': 'Write two or three sentences.',
                        'success': ['I said the flame does several of the seven life processes.',
                                    'I said the seven processes describe living things — they do '
                                    'not decide the case on their own.',
                                    'I said living things are made of one or more cells.',
                                    'I said the flame is made of hot glowing gas, with no cells.']},
            'produce': {'q': 'A probe on Mars finds orange crust that spreads across rock, takes '
                             'in one gas and gives out another. Write the one test you would run '
                             'to settle whether it is alive, and say what result would mean '
                             '“alive”.',
                        'field_label': 'Your answer',
                        'placeholder': 'Name the test, then say what you would need to see.',
                        'success': ['I named looking at a sample under a microscope.',
                                    'I said what I am looking for: cells.',
                                    'I described what alive would look like — separate units, each '
                                    'with a boundary around it, repeating.',
                                    'I said spreading and swapping gases are not enough on their '
                                    'own, because a chemical reaction can do both.']}},
 'key_note': 'The seven life processes — <strong>MRS GREN</strong> — describe what living things '
             '<em>do</em>. Being made of one or more cells is what makes a thing <em>living</em>.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The flame', 'done_when': 'committed'},
          {'anchor': 's-board',
           'short': 'TESTS',
           'label': 'Run the tests',
           'done_when': 'all_tests_run'},
          {'anchor': 's-sort',
           'short': 'SORT',
           'label': 'Sort all eight',
           'done_when': 'all_sorted'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'key_facts': [{'id': 'what-the-seven-do',
                'text': 'The seven processes describe what living things <em>do</em>. They do not '
                        'decide whether something is alive.',
                'placement': 'top-level',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'tutor': {'prompt': 'Stuck on why a flame isn’t alive?',
           'cta': 'Ask about this lesson',
           'anchor': 's-board'},
 'before_this': 'Nothing — this is where the unit starts.',
 'ks4_becomes': 'Cell theory, and the argument over where the line around “living” belongs.',
 'safety_note': 'Never light a candle to test this at home without an adult with you.',
 'ws': ['scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
