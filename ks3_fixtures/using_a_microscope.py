# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B1 `using-a-microscope` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B1'
SOURCE_SLUG = 'using-a-microscope'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'using-a-microscope',
 'title': 'Using a microscope',
 'discipline': 'biology',
 'unit': 'cells-and-organisation',
 'family': 'INVESTIGATION',
 'covers': ['KS3.WS.EXP.05', 'KS3.B.CELLS.01b'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 50,
 'requires': ['life-processes'],
 'assumes': [],
 'references': [],
 'ks4_links': ['biology/cell-biology/microscopy'],
 'big_question': 'Changing only the lens turned a clear picture into a smear. How do you use a '
                 'microscope so that does not happen?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Two photographs',
           'done_when': 'committed'},
          {'anchor': 's-method',
           'short': 'METHOD',
           'label': 'Sam’s method',
           'done_when': 'steps_opened'},
          {'anchor': 's-worked',
           'short': 'WATCH',
           'label': 'Watch it done',
           'done_when': 'all_steps_shown'},
          {'anchor': 's-yours', 'short': 'YOU', 'label': 'Now you', 'done_when': 'attempt_checked'},
          {'anchor': 's-lab',
           'short': 'BENCH',
           'label': 'The bench',
           'done_when': 'all_rows_recorded'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'data',
                'title': 'Same slide. Same microscope. Same person.',
                'prompt': 'Two photographs, taken one minute apart, of one piece of onion skin. In '
                          'the first you can count the cells. In the second there is a grey smear '
                          'with one dark curve in it. Nothing was changed except the objective '
                          'lens.',
                'figures': ['b1-onion-epidermis-x100', 'b1-onion-epidermis-x400'],
                'commit': 'If you had to guess, which lens should you start with to find the '
                          'cells?',
                'options': ['The weakest lens', 'The strongest lens'],
                'reveal': "Next: look at Sam's method for viewing onion skin and decide which "
                          'steps would cost him.',
                'guess': True,
                'replies': ['That is the right start. Find the cells on the weakest lens first, '
                            'then move up to a stronger one.',
                            'The strongest lens does give the most detail. But it makes cells very '
                            'hard to find in the first place.'],
                'answer': 0},
 'figures': [{'id': 'b1-onion-epidermis-x100',
              'kind': 'micrograph',
              'caption': 'Onion epidermis, ×100. Cells countable, edges sharp.',
              'slot_label': 'Photo coming soon',
              'status': 'needed'},
             {'id': 'b1-onion-epidermis-x400',
              'kind': 'micrograph',
              'caption': 'The same spot, ×400. One cell wall crossing an empty grey field.',
              'slot_label': 'Photo coming soon',
              'status': 'needed'}],
 'misconceptions': [{'id': 'CELL-01',
                     'statement': 'Those neat round circles in the field of view are the cells.',
                     'elicited_by': 'sams-method',
                     'confronted_by': 'sams-method'},
                    {'id': 'CELL-02',
                     'statement': 'The highest magnification always shows you the most.',
                     'elicited_by': 'microscope-lab',
                     'confronted_by': 'microscope-lab'}],
 'vocabulary': [{'term': 'specimen',
                 'definition': 'The thing you are looking at under the microscope.',
                 'note': 'It has to be thin enough for light to get through it. That is why onion '
                         'skin works and a whole onion does not.'},
                {'term': 'coverslip',
                 'definition': 'The thin square of glass laid over a specimen.',
                 'note': 'Lower it slowly, at an angle. Dropping it flat is what traps the air '
                         'bubbles Sam’s method starts with.'},
                {'term': 'magnification',
                 'definition': 'How many times bigger than real life something looks.',
                 'note': 'Total magnification = eyepiece × objective. A ×10 eyepiece with a ×40 '
                         'objective gives ×400.'},
                {'term': 'field of view',
                 'definition': 'The circle of the specimen you can see down the microscope at one '
                               'time.',
                 'note': 'Turn to a higher magnification and the field of view gets smaller. You '
                         'see more detail of less.'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'check', 'id': 'sams-method', 'anchor': 's-method'},
          {'type': 'formula',
           'anchor': 's-formula',
           'statement': 'total magnification = eyepiece × objective',
           'triangle': {'eyebrow': 'The triangle',
                        'heading': 'Cover the one you want',
                        'aria_label': 'Formula triangle: total magnification on top, eyepiece and '
                                      'objective below',
                        'top': {'label': 'total',
                                'button': 'Cover total',
                                'text': 'Total is on its own at the top, with the other two side '
                                        'by side underneath. Cover it and you are left with '
                                        'eyepiece × objective — multiply.'},
                        'left': {'label': 'eye',
                                 'button': 'Cover eyepiece',
                                 'text': 'Cover the eyepiece and you are left with total over '
                                         'objective. Divide the total by the objective.'},
                        'right': {'label': 'obj',
                                  'button': 'Cover objective',
                                  'text': 'Cover the objective and you are left with total over '
                                          'eyepiece. Divide the total by the eyepiece.'},
                        'close': 'Two things side by side means multiply. One thing over another '
                                 'means divide.'}},
          {'type': 'key-fact', 'ref': 'multiply-never-add'},
          {'type': 'worked-example', 'id': 'magnification-fifa', 'anchor': 's-worked'},
          {'type': 'check', 'id': 'magnification-fifa-do', 'anchor': 's-yours'},
          {'type': 'practical', 'id': 'microscope-lab', 'anchor': 's-lab'},
          {'type': 'misconception',
           'id': 'highest-is-best',
           'anchor': 's-think',
           'targets': 'CELL-02'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'multiply-never-add',
                'text': 'Multiply the two, never add them. ×10 and ×40 give ×400, not ×50.',
                'placement': 'top-level',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'sams-method',
                 'kind': 'critique-steps',
                 'demand': 'explain',
                 'eyebrow': 'Your turn · judge it first',
                 'heading': 'Sam’s method',
                 'prompt': 'Sam wrote this up for a slide of onion skin. Three of the six steps '
                           'will cost him. Tap the ones you would change, then open them up.',
                 'steps': [{'text': 'Put a drop of water on the slide, then drop the coverslip '
                                    'straight down onto it.',
                            'fault': True,
                            'word': 'Costs him',
                            'verdict': 'Dropped flat, it traps air. Bubbles are round, thick and '
                                       'black-edged, and they get drawn as cells every year. Lower '
                                       'it slowly on one edge instead.'},
                           {'text': 'Clip the slide onto the stage, over the hole in the middle.',
                            'fault': False,
                            'word': 'Sound',
                            'verdict': 'Light has to come up through the specimen, so it must sit '
                                       'over the hole.'},
                           {'text': 'Start on the ×40 objective, so there is as much detail as '
                                    'possible from the beginning.',
                            'fault': True,
                            'word': 'Costs him',
                            'verdict': 'That is 0.45 mm of slide in view. He is hunting for '
                                       'something the width of a hair in the dark. Start on ×4, '
                                       'where he can see 4.5 mm at once.'},
                           {'text': 'Look down the eyepiece and turn the coarse focus so the '
                                    'objective comes down towards the slide.',
                            'fault': True,
                            'word': 'Costs him',
                            'verdict': 'From the eyepiece he cannot see the gap closing. Watch '
                                       'from the side, bring it down until it nearly touches, then '
                                       'focus by moving it away.'},
                           {'text': 'Draw what he sees in pencil, in clear single lines, with no '
                                    'shading.',
                            'fault': False,
                            'word': 'Sound',
                            'verdict': 'A biological drawing is a record, not a picture. Single '
                                       'lines, no shading, no colouring in.'},
                           {'text': 'Write the magnification he used next to the drawing.',
                            'fault': False,
                            'word': 'Sound',
                            'verdict': 'Without it the drawing says nothing about size, and no one '
                                       'can repeat what he did.'}],
                 'reveal_label': 'Open the steps I picked',
                 'progress_zero': 'Pick at least one',
                 'targets': 'CELL-01'},
                {'id': 'magnification-fifa',
                 'kind': 'worked-example',
                 'demand': 'apply',
                 'eyebrow': 'Watch it done · one step at a time',
                 'heading': 'Riya’s eyepiece says ×10. The objective clicked into place says ×40. '
                            'Calculate the total magnification.',
                 'staged': True,
                 'fifa': [{'letter': 'F',
                           'name': 'Formula',
                           'line': 'total magnification = eyepiece × objective',
                           'note': 'Written down before any numbers. That is what stops the next '
                                   'step going wrong.'},
                          {'letter': 'I',
                           'name': 'Insert',
                           'line': 'total magnification = 10 × 40',
                           'note': 'Eyepiece where eyepiece goes, objective where objective goes.'},
                          {'letter': 'F',
                           'name': 'Fine-tune',
                           'line': 'nothing to convert — both are already “times”',
                           'note': 'Multiply, never add. 10 + 40 = 50 is the commonest wrong '
                                   'answer on this calculation.'},
                          {'letter': 'A',
                           'name': 'Answer',
                           'line': '×400',
                           'note': 'Magnification has no unit — ×400 means four hundred times '
                                   'bigger, never 400 mm.'}],
                 'buttons': {'first': 'Show the first step',
                             'next': 'Show the next step',
                             'done': 'All four steps shown'}},
                {'id': 'magnification-fifa-do',
                 'kind': 'fifa-construct',
                 'demand': 'apply',
                 'eyebrow': 'Now you · same four steps',
                 'heading': 'Your eyepiece says ×10. You click the ×4 objective into place. '
                            'Calculate the total magnification.',
                 'prompt': 'Write each step out. Then check your working against Riya’s and tick '
                           'what you did.',
                 'fields': [{'id': 'my-f',
                             'letter': 'F',
                             'label': 'Formula',
                             'placeholder': 'total magnification = …'},
                            {'id': 'my-i',
                             'letter': 'I',
                             'label': 'Insert',
                             'placeholder': 'total magnification = … × …'},
                            {'id': 'my-t',
                             'letter': 'F',
                             'label': 'Fine-tune',
                             'placeholder': 'anything to convert?'},
                            {'id': 'my-a', 'letter': 'A', 'label': 'Answer', 'placeholder': '×…'}],
                 'check_label': 'Check my working',
                 'model_lead': 'Riya’s working, with your numbers',
                 'model': ['F   total magnification = eyepiece × objective',
                           'I   total magnification = 10 × 4',
                           'F   nothing to convert — multiply, do not add',
                           'A   ×40'],
                 'success': ['I wrote the formula out before I put any numbers in.',
                             'I put 10 in for the eyepiece and 4 in for the objective.',
                             'I multiplied. I did not add.',
                             'My answer is written ×40 — a number of times, with no unit after '
                             'it.'],
                 'tally_met': 'All 4 ticked — you can do this one on your own.'},
                {'id': 'microscope-lab',
                 'kind': 'lab',
                 'demand': 'investigate',
                 'heading': 'The bench microscope',
                 'aside': 'Eyepiece fixed at ×10. Turret, focus and a slide of onion skin.',
                 'prompt': 'Turn from the ×4 objective to the ×40. What happens to the amount of '
                           'slide you can see?',
                 'options': ['You see more of the slide',
                             'You see less of the slide',
                             'You see the same amount, bigger'],
                 'sim': {'kind': 'microscope',
                         'controls': ['magnification', 'focus'],
                         'specimens': ['onion skin'],
                         'eyepiece': 10,
                         'objective_control': 'segment',
                         'focus_label': 'Focus — rack through the layers',
                         'veil': 'Answer the question underneath first. The lens will not tell you '
                                 'anything you have not already guessed at.',
                         'readouts': [{'id': 'total-magnification', 'label': 'Total magnification'},
                                      {'id': 'field-of-view', 'label': 'Field of view'},
                                      {'id': 'cells-across', 'label': 'Cells across it'}],
                         'resolve_notes': {'40': 'At ×40 the whole thickness of the skin is in '
                                                 'focus at once. Easy to find things; not much '
                                                 'detail in them.',
                                           '100': 'At ×100 only one layer is sharp at a time. Rack '
                                                  'the focus and you swap one layer for another — '
                                                  'the depth you had at ×40 has already gone.',
                                           '400': 'At ×400 the slice in focus is thinner than one '
                                                  'cell. Rack the focus and the layers arrive one '
                                                  'at a time — that thin slice is the depth of '
                                                  'field.'},
                         'record': {'button': 'Record this row',
                                    'columns': [{'id': 'objective', 'label': 'Objective'},
                                                {'id': 'total', 'label': 'Total'},
                                                {'id': 'field-of-view', 'label': 'Field of view'},
                                                {'id': 'cells-across', 'label': 'Cells across'}],
                                    'complete': 'Ten times the magnification. A tenth of the field '
                                                'of view. A tenth of the cells in front of you — '
                                                'and a slice of depth so thin that most of the '
                                                'cell is out of focus at once.'}},
                 'targets': 'CELL-02'},
                {'id': 'highest-is-best',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'CELL-02',
                 'paragraphs': ['Magnification makes things bigger. It does not make them easier '
                                'to find, and it takes away depth as fast as it adds size. Your '
                                'own readout says it: at ×400 the field of view is 0.45 mm — fewer '
                                'than two onion cells across — and the slice in focus is thinner '
                                'than one cell.',
                                'So the method is: find it on the lowest power, get it in the '
                                'middle, then climb.']}],
 'ladder': {'recall': {'q': 'You have just clipped a new slide onto the stage. Which objective do '
                            'you turn in first?',
                       'options': ['The ×4 — the lowest power',
                                   'The ×40 — the highest power',
                                   'The ×10 — somewhere in the middle',
                                   'Whichever one is already in place'],
                       'answer': 0,
                       'feedback': {1: 'That is 0.45 mm of slide in view and almost no depth in '
                                       'focus. Finding anything is luck.',
                                    2: 'Better than starting at the top, but you still have less '
                                       'to search. Start at the bottom every time, then climb.',
                                    3: 'If the last person left the ×40 in, you start blind and '
                                       'risk driving the lens into the glass. Turn to the lowest '
                                       'first.'}},
            'apply': {'q': 'A microscope has a ×15 eyepiece. You click the ×40 objective into '
                           'place. What is the total magnification?',
                      'scaffold': [{'letter': 'F',
                                    'text': 'write the formula down before anything else.'},
                                   {'letter': 'I', 'text': 'insert the two numbers.'},
                                   {'letter': 'F',
                                    'text': 'fine-tune: convert any units, and rearrange the '
                                            'equation if what you want is not on the left.'},
                                   {'letter': 'A', 'text': 'answer, written as “times”.'}],
                      'options': ['×55', '×40', '×600', '×6000'],
                      'answer': 2,
                      'feedback': {0: 'That is 15 + 40. The two magnifications multiply — the '
                                      'objective makes an image and the eyepiece magnifies that '
                                      'image again.',
                                   1: 'That is the objective on its own. The eyepiece magnifies '
                                      'again on top of it, so it must go into the sum.',
                                   3: 'One zero too many: 15 × 40 = 600. Worth checking the size '
                                      'of the answer against the ×400 you already know.'}},
            'explain': {'q': 'Ade finds his cells on ×4, then turns straight to ×40 and says they '
                             'have vanished. Explain what has happened and what he should do.',
                        'field_label': 'Your answer',
                        'placeholder': 'Write two or three sentences.',
                        'success': ['I said the field of view gets smaller as magnification goes '
                                    'up.',
                                    'I said that means less of the slide is in front of him — so '
                                    'what he wants can end up outside the view.',
                                    'I said the depth in focus shrinks too, so it can be there and '
                                    'still look blurred.',
                                    'I said he should go back to ×4, move what he wants into the '
                                    'middle, then climb through ×10 and refocus at each step.']},
            'produce': {'q': 'Two students disagree about whether onion cells from the outer layer '
                             'are longer than cells from an inner layer. Write the method you '
                             'would give them.',
                        'field_label': 'Your answer',
                        'placeholder': 'Say what you would change, what you would keep the same, '
                                       'and what you would measure.',
                        'success': ['I said which layer the onion strip comes from — that is the '
                                    'thing being changed.',
                                    'I said the magnification stays the same for every slide, or '
                                    'the comparison is worthless.',
                                    'I said what gets measured and how — cells counted across a '
                                    'known field of view, or measured against the field.',
                                    'I said measure several cells and repeat, rather than trusting '
                                    'one.']}},
 'key_note': 'Total magnification = eyepiece × objective. Every step up in magnification hands '
             'back field of view and depth, so find it low and climb.',
 'stretch': [{'type': 'explainer',
              'id': 'where-180-comes-from',
              'text': 'Where does 180 come from? Printed on the eyepiece is a field number — on '
                      'these ones, 18. Divide it by the objective and you get the field of view in '
                      'millimetres. Because this eyepiece is ×10, dividing 180 by the total '
                      'magnification gives the same answer. Change the eyepiece and the 180 '
                      'changes with it.'}],
 'support': [],
 'tutor': {'prompt': 'Stuck on the calculation?',
           'cta': 'Ask about this lesson',
           'anchor': 's-worked'},
 'ks4_becomes': 'Magnification = image size ÷ actual size, and the electron microscope.',
 'safety_note': 'Microscope lamps get hot and slides are glass. Follow your teacher’s instructions '
                'at the bench.',
 'ws': ['experimental-skills-and-investigations', 'measurement', 'analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
