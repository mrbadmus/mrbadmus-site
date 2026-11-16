# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B1 `animal-and-plant-cells` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B1'
SOURCE_SLUG = 'animal-and-plant-cells'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'animal-and-plant-cells',
 'title': 'Animal and plant cells',
 'discipline': 'biology',
 'unit': 'cells-and-organisation',
 'family': 'MODEL',
 'covers': ['KS3.B.CELLS.02', 'KS3.B.CELLS.03'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 2}, {'id': 'structure-function', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['using-a-microscope'],
 'assumes': [],
 'references': [{'unit': 'B1', 'lesson': 'specialised-cells'},
                {'unit': 'B1', 'lesson': 'unicellular-organisms'}],
 'ks4_links': [],
 'big_question': 'What do plant cells and animal cells have in common, and what is different?',
 'phenomenon': {'kind': 'compare',
                'title': 'A cheek cell and an oak leaf cell.',
                'prompt': 'Seven parts in all. Some are found in a cell scraped from your cheek. '
                          'Some are found in a cell cut from an oak leaf.',
                'tiles': [{'n': 1, 'label': 'Cell membrane'},
                          {'n': 2, 'label': 'Cytoplasm'},
                          {'n': 3, 'label': 'Nucleus'},
                          {'n': 4, 'label': 'Mitochondria'},
                          {'n': 5, 'label': 'Cell wall'},
                          {'n': 6, 'label': 'Vacuole'},
                          {'n': 7, 'label': 'Chloroplasts'}],
                'commit': 'If you had to guess, does the cheek cell have any of these seven parts '
                          'that the oak leaf cell lacks?',
                'options': ['Yes, at least one', 'No, not one'],
                'reveal': 'Next: a bench with both cells on it, so you can check part by part.',
                'guess': True,
                'replies': ['Animals and plants do live very differently. But every part in your '
                            'cheek cell is in the oak leaf cell too.',
                            'Every part in your cheek cell is in the leaf cell too. The leaf cell '
                            'just has some extra parts of its own.'],
                'answer': 1},
 'misconceptions': [{'id': 'CELL-04',
                     'statement': 'The cell membrane and the cell wall are the same thing — animal '
                                  'cells have a wall, it is just called a membrane.',
                     'elicited_by': 'wall-or-membrane',
                     'confronted_by': 'wall-and-chloroplasts'},
                    {'id': 'CELL-03',
                     'statement': 'Every plant cell is green, because plants are green.',
                     'elicited_by': 'fit-the-cell',
                     'confronted_by': 'wall-and-chloroplasts'}],
 'vocabulary': [{'term': 'cell membrane',
                 'definition': 'A thin skin around every cell that controls what gets in and out.',
                 'note': 'Every cell has one — plant, animal and every other kind.'},
                {'term': 'cytoplasm',
                 'definition': 'The jelly that fills the cell, where most of its chemical '
                               'reactions happen.',
                 'note': None},
                {'term': 'nucleus',
                 'definition': 'The control centre. It holds the instructions for everything the '
                               'cell does.',
                 'note': 'Usually one per cell. You will meet a cell with none at all in the next '
                         'lesson.'},
                {'term': 'mitochondria',
                 'definition': 'Tiny structures where energy is released from food.',
                 'note': 'One is a mitochondrion; several are mitochondria. A muscle cell is '
                         'packed with them.'},
                {'term': 'cell wall',
                 'definition': 'A stiff layer outside the membrane of a plant cell, which gives '
                               'the cell its shape.',
                 'note': 'A wall is stiff and on the outside; a membrane is thin and underneath '
                         'it. An animal cell has the membrane only.'},
                {'term': 'vacuole',
                 'definition': 'A large space in a plant cell, filled with cell sap, which pushes '
                               'outwards and keeps the cell firm.',
                 'note': 'When a plant is short of water the vacuoles stop pushing, and the whole '
                         'plant wilts.'},
                {'term': 'chloroplast',
                 'definition': 'The green part of a plant cell, where light is used to make food.',
                 'note': 'Only the cells that get light have them. Roots are not green.'}],
 'figures': [{'id': 'b1-cell-bench',
              'kind': 'css-art',
              'art': 'cell-bench',
              'caption': 'The cell bench drawing: a leaf cell and a cheek cell, each as a textbook '
                         'drawing and as a ×400 field of view.',
              'slot_label': 'Diagram coming soon',
              'status': 'drafted'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'check', 'id': 'seven-parts-two-cells', 'anchor': 's-bench'},
          {'type': 'rule',
           'id': 'what-settles-it',
           'anchor': 's-rule',
           'eyebrow': 'What settles it',
           'statement': 'Everything in an animal cell is on the plant’s list too. The plant has '
                        'three more.',
           'sub': 'Of the seven parts you meet at Key Stage 3. The difference runs one way only.',
           'cards': [{'label': 'In both · 4',
                      'label_tone': 'muted',
                      'chips': ['1 · Cell membrane',
                                '2 · Cytoplasm',
                                '3 · Nucleus',
                                '4 · Mitochondria'],
                      'chip_tone': 'inset',
                      'close': 'A door, a jelly, a set of instructions and a way of releasing '
                               'energy. Nothing alive on this page does without them.'},
                     {'label': 'Plant only · 3',
                      'label_tone': 'accent',
                      'chips': ['5 · Cell wall', '6 · Vacuole', '7 · Chloroplasts'],
                      'chip_tone': 'accent-tint',
                      'close': 'A plant cannot move, cannot hunt and cannot hold itself up with a '
                               'skeleton. All three extras answer one of those problems. The third '
                               'one only turns up where light does.'}]},
          {'type': 'check', 'id': 'wall-or-membrane', 'anchor': 's-wall'},
          {'type': 'practical', 'id': 'fit-the-cell', 'anchor': 's-fit'},
          {'type': 'misconception', 'id': 'wall-and-chloroplasts', 'anchor': 's-think'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'stretch': [{'type': 'explainer',
              'id': 'why-celery-is-stiff',
              'text': 'Why is a stick of celery stiff? Not the wall by itself — a box is only as '
                      'firm as what is inside it. Each cell’s vacuole is full of watery sap '
                      'pressing outwards against the wall, and thousands of cells pressing on '
                      'their neighbours is what holds the stalk up. Take the water away and the '
                      'vacuoles shrink, the pressure drops, and the whole thing flops. That is '
                      'wilting, and it reverses the moment water comes back — until the cells are '
                      'actually damaged.'}],
 'support': [],
 'activities': [{'id': 'seven-parts-two-cells',
                 'kind': 'cell-bench',
                 'anchor': 's-bench',
                 'demand': "compare two real specimens part by part, and tell 'not there' apart "
                           "from 'there but not visible'",
                 'eyebrow': 'The bench · seven parts, one job each',
                 'heading': 'One cell, two organisms, two ways of looking',
                 'prompt': 'Switch the specimen and watch which parts stay put. Then switch from '
                           'the textbook drawing to what a school microscope actually shows you, '
                           'and watch which parts disappear.',
                 'figure': 'b1-cell-bench',
                 'start': 'leaf',
                 'mark_space': {'w': 900, 'h': 560},
                 'control_labels': {'specimen': 'Specimen', 'view': 'Looking at it'},
                 'where_labels': {'both': {'tag': 'In both', 'pill': 'In both cells'},
                                  'plant': {'tag': 'Plant only', 'pill': 'Plant cells only'},
                                  'absent': {'pill': 'Not in this cell at all'}},
                 'scope_words': {'visible': 'You can see this one.',
                                 'hidden': 'You cannot see this one.'},
                 'views': [{'id': 'diagram', 'label': 'The textbook drawing'},
                           {'id': 'scope',
                            'label': 'Down a school microscope',
                            'locked_until_gate': True,
                            'shows_scope_note': True}],
                 'gate': {'q': 'Before you switch — of the seven parts, how many can a school '
                               'microscope actually show you in a leaf cell?',
                          'options': ['All seven',
                                      'Five of them',
                                      'Three of them',
                                      'Only the wall'],
                          'unlocks': 'scope'},
                 'extras': [{'id': 'stain',
                             'group_label': 'Stain',
                             'label_off': 'Add methylene blue',
                             'label_on': 'Methylene blue — on',
                             'when': {'specimen': 'cheek', 'view': 'scope'}}],
                 'specimens': [{'id': 'cheek',
                                'label': 'Cheek cell',
                                'absent_tag': 'Not in an animal cell',
                                'absent_detail': 'Switch the specimen to a leaf cell to find this '
                                                 'one. An animal cell does not have it, and that '
                                                 'is not a fault — nothing a cheek cell does needs '
                                                 'it.',
                                'alt': {'diagram': 'A labelled drawing of a cheek cell: an '
                                                   'irregular membrane, cytoplasm, a central '
                                                   'nucleus and scattered mitochondria.',
                                        'scope': 'A field of cheek cells as seen through a school '
                                                 'microscope: pale grey outlines with a faint '
                                                 'nucleus in each.'},
                                'caption': {'diagram': 'Cheek cell, drawn flattened. In your mouth '
                                                       'it is a soft, irregular bag.',
                                            'scope': 'Cheek cells, ×400. Unstained: almost nothing '
                                                     'to see.',
                                            'scope+stain': 'Cheek cells, ×400. Stained with '
                                                           'methylene blue.'},
                                'tally': {'diagram': '4 parts in this cell · every one of them is '
                                                     'in a leaf cell too',
                                          'scope': '4 parts in this cell · 2 of them visible at '
                                                   '×400 — and only once it is stained',
                                          'scope+stain': '4 parts in this cell · 2 of them visible '
                                                         'at ×400'},
                                'art': {'mitochondria': [[250, 214, 0.5],
                                                         [302, 368, -0.4],
                                                         [600, 196, 0.3],
                                                         [650, 352, -0.5],
                                                         [392, 196, 0.9],
                                                         [420, 392, 0.1],
                                                         [694, 272, 1.3],
                                                         [224, 300, 1.4]]}},
                               {'id': 'leaf',
                                'label': 'Leaf cell',
                                'alt': {'diagram': 'A labelled drawing of a leaf cell: cell wall, '
                                                   'membrane, cytoplasm, a large central vacuole, '
                                                   'a nucleus at one side, chloroplasts and '
                                                   'mitochondria.',
                                        'scope': 'A field of leaf cells as seen through a school '
                                                 'microscope: a honeycomb of walls, pale vacuoles '
                                                 'and small green chloroplasts.'},
                                'caption': {'diagram': 'Leaf cell, drawn as a slice through the '
                                                       'middle. A real cell is a box, not a '
                                                       'rectangle.',
                                            'scope': 'Leaf tissue, ×400. Real slides are crowded — '
                                                     'you never get one cell on its own.'},
                                'tally': {'diagram': '7 parts in this cell · 4 shared with you · 3 '
                                                     'the plant’s own',
                                          'scope': '7 parts in this cell · 5 of them visible at '
                                                   '×400'},
                                'art': {'chloroplasts': [[300, 126, -0.2],
                                                         [392, 112, 0.1],
                                                         [486, 124, -0.15],
                                                         [578, 114, 0.2],
                                                         [664, 132, -0.1],
                                                         [706, 222, 1.5],
                                                         [700, 330, 1.4],
                                                         [620, 438, 0.15],
                                                         [520, 452, -0.1],
                                                         [420, 440, 0.2],
                                                         [316, 450, -0.15],
                                                         [176, 404, 1.3],
                                                         [180, 196, 1.45]],
                                        'mitochondria': [[258, 140, 0.6],
                                                         [742, 182, 1.2],
                                                         [700, 392, -0.5],
                                                         [268, 438, 0.3]]}}],
                 'parts': [{'id': 'membrane',
                            'num': '1',
                            'name': 'Cell membrane',
                            'where': 'both',
                            'job': 'It chooses what gets into the cell and what stays out.',
                            'detail': 'A skin two molecules thick, wrapped right round the '
                                      'cytoplasm. Water and oxygen cross it easily; most other '
                                      'things only cross where the cell lets them. In a plant cell '
                                      'it sits just inside the wall, pressed against it.',
                            'visible': False,
                            'scope_note': 'Far too thin to resolve — a few molecules across. The '
                                          'single line you see at the edge of a cheek cell is not '
                                          'the membrane; it is just where the cell stops.',
                            'mark': {'cheek': [{'x': 152, 'y': 286, 'r': 17}],
                                     'leaf': [{'x': 620, 'y': 78, 'r': 15}]}},
                           {'id': 'cytoplasm',
                            'num': '2',
                            'name': 'Cytoplasm',
                            'where': 'both',
                            'job': 'The jelly where almost all of the cell’s reactions happen.',
                            'detail': 'Not empty and not still. It is crowded with dissolved '
                                      'substances and with the parts below, and it holds them in '
                                      'place. Textbook drawings leave it looking spacious; it is '
                                      'not.',
                            'visible': True,
                            'scope_note': 'You see it, but only as a faintly grainy region — the '
                                          'grain is the parts you cannot separate.',
                            'mark': {'cheek': [{'x': 560, 'y': 372, 'r': 36}],
                                     'leaf': [{'x': 450, 'y': 128, 'r': 34}]}},
                           {'id': 'nucleus',
                            'num': '3',
                            'name': 'Nucleus',
                            'where': 'both',
                            'job': 'It holds the DNA — the instructions for running and building '
                                   'the cell.',
                            'detail': 'One per cell, and the cell cannot make a new part or divide '
                                      'without it. In a plant cell it is usually pushed out to one '
                                      'side, because the vacuole has taken the middle.',
                            'visible': True,
                            'scope_note': 'Visible, and much clearer once stained. Methylene blue '
                                          'on a cheek cell turns it from almost nothing into the '
                                          'darkest thing in the field.',
                            'mark': {'cheek': [{'x': 466, 'y': 272, 'r': 76}],
                                     'leaf': [{'x': 188, 'y': 300, 'r': 58}]}},
                           {'id': 'mitochondria',
                            'num': '4',
                            'name': 'Mitochondria',
                            'where': 'both',
                            'job': 'They release energy from food, by respiration.',
                            'detail': 'Every cell has them and busy cells have thousands. A cell '
                                      'that never stops working — a muscle cell, a sperm cell — is '
                                      'packed with them. That is the whole difference between it '
                                      'and a cheek cell on this list.',
                            'visible': False,
                            'scope_note': 'Around fifty times smaller across than the cell itself, '
                                          'and below what a school microscope can separate. '
                                          'Turning the magnification up gives you a bigger blur, '
                                          'not a mitochondrion.',
                            'mark': {'cheek': [{'x': 250, 'y': 214, 'r': 24},
                                               {'x': 302, 'y': 368, 'r': 24},
                                               {'x': 600, 'y': 196, 'r': 24},
                                               {'x': 650, 'y': 352, 'r': 24},
                                               {'x': 392, 'y': 196, 'r': 24},
                                               {'x': 420, 'y': 392, 'r': 24},
                                               {'x': 694, 'y': 272, 'r': 24},
                                               {'x': 224, 'y': 300, 'r': 24}],
                                     'leaf': [{'x': 258, 'y': 140, 'r': 24},
                                              {'x': 742, 'y': 182, 'r': 24},
                                              {'x': 700, 'y': 392, 'r': 24},
                                              {'x': 268, 'y': 438, 'r': 24}]}},
                           {'id': 'wall',
                            'num': '5',
                            'name': 'Cell wall',
                            'where': 'plant',
                            'job': 'It holds the cell’s shape and stops it bursting.',
                            'detail': 'Made of cellulose, and stiff. Water floods into a plant '
                                      'cell and the wall is what pushes back — without it the cell '
                                      'would swell until it split. It chooses nothing: things pass '
                                      'straight through it to the membrane.',
                            'visible': True,
                            'scope_note': 'The clearest thing on the slide. In onion or leaf '
                                          'tissue the walls are what draw the honeycomb you '
                                          'actually see.',
                            'mark': {'leaf': [{'x': 300, 'y': 68, 'r': 15}]}},
                           {'id': 'vacuole',
                            'num': '6',
                            'name': 'Vacuole',
                            'where': 'plant',
                            'job': 'A bag of sap that presses outwards and keeps the cell firm.',
                            'detail': 'One big permanent one, often taking up most of the cell. It '
                                      'stores water and dissolved sugars and salts, and the '
                                      'pressure it puts on the wall is what holds a leaf out flat. '
                                      'Lose the water and the cell goes limp.',
                            'visible': True,
                            'scope_note': 'Visible as a large pale region in the middle, with the '
                                          'cytoplasm squeezed into a rim around it.',
                            'mark': {'leaf': [{'x': 450, 'y': 280, 'r': 78}]}},
                           {'id': 'chloroplasts',
                            'num': '7',
                            'name': 'Chloroplasts',
                            'where': 'plant',
                            'job': 'They trap light, so the cell can make its own food.',
                            'detail': 'Green because of the chlorophyll inside them. A cell at the '
                                      'top of a leaf can hold a hundred; a cell in a root holds '
                                      'none at all, because no light gets there. This is the part '
                                      'that makes a plant a plant.',
                            'visible': True,
                            'scope_note': 'Big enough to see, and they give themselves away by '
                                          'colour — small green ovals, no stain needed.',
                            'mark': {'leaf': [{'x': 300, 'y': 126, 'r': 22},
                                              {'x': 392, 'y': 112, 'r': 22},
                                              {'x': 486, 'y': 124, 'r': 22},
                                              {'x': 578, 'y': 114, 'r': 22},
                                              {'x': 664, 'y': 132, 'r': 22},
                                              {'x': 706, 'y': 222, 'r': 22},
                                              {'x': 700, 'y': 330, 'r': 22},
                                              {'x': 620, 'y': 438, 'r': 22},
                                              {'x': 520, 'y': 452, 'r': 22},
                                              {'x': 420, 'y': 440, 'r': 22},
                                              {'x': 316, 'y': 450, 'r': 22},
                                              {'x': 176, 'y': 404, 'r': 22},
                                              {'x': 180, 'y': 196, 'r': 22}]}}]},
                {'id': 'wall-or-membrane',
                 'kind': 'sort-pairs',
                 'anchor': 's-wall',
                 'demand': 'elicit CELL-04 by forcing five commitments that only separate if the '
                           'wall and the membrane are two different things',
                 'eyebrow': 'Your turn · tell two apart',
                 'heading': 'Wall or membrane?',
                 'prompt': 'These two get swapped for each other more than any other pair on the '
                           'list. Send each statement to the one it belongs to. Change your mind '
                           'as often as you like — nothing is marked here.',
                 'categories': [{'id': 'wall', 'label': 'Cell wall'},
                                {'id': 'membrane', 'label': 'Cell membrane'}],
                 'rows': [{'id': 'q1',
                           'text': 'Stops the cell bursting when water moves in.',
                           'answer': 'wall',
                           'note': 'The wall pushes back. Put an animal cell in pure water and '
                                   'there is nothing to push back — it swells and splits.'},
                          {'id': 'q2',
                           'text': 'Decides what gets in and what stays out.',
                           'answer': 'membrane',
                           'note': 'Every choice about what enters is made here, in a plant cell '
                                   'exactly as in yours.'},
                          {'id': 'q3',
                           'text': 'Made of cellulose.',
                           'answer': 'wall',
                           'note': 'Cellulose is a plant material. It is also what makes celery '
                                   'stringy and paper possible.'},
                          {'id': 'q4',
                           'text': 'Every cell on this list has one — plant or animal.',
                           'answer': 'membrane',
                           'note': 'This is the one people get wrong. The wall is an extra; the '
                                   'membrane was never replaced.'},
                          {'id': 'q5',
                           'text': 'Sits on the outside of the other one.',
                           'answer': 'wall',
                           'note': 'Wall outside, membrane just inside it. That order matters when '
                                   'you draw one.'}],
                 'reveal_label': 'Open the answers',
                 'progress_unit': 'sent',
                 'reveal_panel': {'headline': 'The wall is the box. The membrane is the door.',
                                  'body': 'A plant cell has both, and in that order: wall on the '
                                          'outside, membrane just inside it, pressed against it. '
                                          'The wall never chooses anything — water and dissolved '
                                          'substances pass straight through it. Every choice about '
                                          'what enters the cell is made at the membrane, in a '
                                          'plant exactly as in you.'},
                 'mark_rows': False,
                 'targets': 'CELL-04'},
                {'id': 'fit-the-cell',
                 'kind': 'fit-parts',
                 'anchor': 's-fit',
                 'demand': "build four real cells from one parts list, so that 'which parts' "
                           "becomes a consequence of 'what job'",
                 'eyebrow': 'Build it',
                 'heading': 'Fit the cell to the job',
                 'head_counter': {'format': '{n} of 4 cells run', 'total': 4},
                 'prompt': 'Four real cells, four different jobs. Install the parts each one needs '
                           '— no more than that — then run it. The cell will tell you what you got '
                           'away with.',
                 'parts_from': 'seven-parts-two-cells',
                 'job_label': 'The job',
                 'install_label': 'Install the parts',
                 'run_label': 'Run this cell',
                 'rerun_label': 'Run it again',
                 'clear_label': 'Strip it back out',
                 'install_unit': 'installed',
                 'install_empty_hint': 'Install something first',
                 'specimens': [{'id': 'palisade',
                                'label': 'Palisade cell',
                                'kind': 'plant',
                                'job': 'Make food out of light.',
                                'where': 'Packed in a row just under the upper surface of a leaf — '
                                         'the first cells the light reaches.',
                                'needs': ['membrane',
                                          'cytoplasm',
                                          'nucleus',
                                          'mitochondria',
                                          'wall',
                                          'vacuole',
                                          'chloroplasts'],
                                'waste': {},
                                'note': 'All seven. A palisade cell is a plant cell with nothing '
                                        'left out, and it can hold a hundred chloroplasts — which '
                                        'is why the top of a leaf is the darkest green part of '
                                        'it.'},
                               {'id': 'root',
                                'label': 'Root hair cell',
                                'kind': 'plant',
                                'job': 'Take water and minerals out of the soil.',
                                'where': 'A long thin finger pushing between soil particles, well '
                                         'below the surface. No light has ever reached it.',
                                'needs': ['membrane',
                                          'cytoplasm',
                                          'nucleus',
                                          'mitochondria',
                                          'wall',
                                          'vacuole'],
                                'waste': {'chloroplasts': 'No light ever arrives down here, so '
                                                          'chloroplasts would be machinery that '
                                                          'never switches on. Real root cells do '
                                                          'not build them — and that is why roots '
                                                          'are not green.'},
                                'note': 'Six of the seven. Wall, vacuole, membrane, cytoplasm, '
                                        'nucleus, mitochondria — and no chloroplasts. A root hair '
                                        'cell is completely a plant cell and completely not '
                                        'green.'},
                               {'id': 'cheek',
                                'label': 'Cheek cell',
                                'kind': 'animal',
                                'job': 'Line a wet, moving surface.',
                                'where': 'The inside of your mouth, in a flat sheet that gets '
                                         'scraped and replaced constantly.',
                                'needs': ['membrane', 'cytoplasm', 'nucleus', 'mitochondria'],
                                'waste': {'wall': 'An animal cell has no wall. A cheek cell has to '
                                                  'bend as your jaw moves — a cellulose box would '
                                                  'crack.',
                                          'vacuole': 'Animal cells have small temporary vacuoles '
                                                     'at most, never one big permanent sap-filled '
                                                     'one. Nothing here needs that push.',
                                          'chloroplasts': 'You cannot photosynthesise. Nothing in '
                                                          'your body traps light to make food.'},
                                'note': 'Four. And here is the thing worth keeping: every one of '
                                        'those four is also in a leaf cell. There is nothing on '
                                        'this list that an animal cell has and a plant cell does '
                                        'not.'},
                               {'id': 'muscle',
                                'label': 'Muscle cell',
                                'kind': 'animal',
                                'job': 'Contract, over and over, without stopping.',
                                'where': 'In your leg, working every time you take a step.',
                                'needs': ['membrane', 'cytoplasm', 'nucleus', 'mitochondria'],
                                'waste': {'wall': 'A wall would stop it contracting. A muscle cell '
                                                  'has to change shape — that is its entire job.',
                                          'vacuole': 'A big sap-filled bag in the middle would be '
                                                     'dead weight in something that has to move.',
                                          'chloroplasts': 'Buried inside your leg. There is no '
                                                          'light in there.'},
                                'note': 'The same four as a cheek cell. What makes a muscle cell a '
                                        'muscle cell is not a different parts list — it is the '
                                        'amount: it is crammed with mitochondria, because it never '
                                        'stops needing energy. That is the next lesson.'}],
                 'consequence': {'membrane': 'Nothing is choosing what comes in or goes out. '
                                             'Everything leaks both ways and the cell is finished '
                                             'within minutes.',
                                 'cytoplasm': 'No jelly means no reactions and nothing holding the '
                                              'parts in place. This is not a cell; it is a bag.',
                                 'nucleus': 'No instructions. It cannot build a single new part '
                                            'and it cannot divide.',
                                 'mitochondria': 'No respiration, so no usable energy. Everything '
                                                 'else you installed sits there doing nothing.',
                                 'wall': 'Water moves in, the cell swells, and with nothing '
                                         'pushing back it bursts.',
                                 'vacuole': 'Nothing presses out against the wall, so the cell '
                                            'goes limp and so does the tissue around it. This is '
                                            'wilting.',
                                 'chloroplasts': 'No chloroplasts in a leaf cell means no '
                                                 'photosynthesis. The plant starves in full '
                                                 'sunlight.'},
                 'verdicts': {'fails': {'badge': 'Fails',
                                        'headline_one': 'It does not survive. One part short.',
                                        'headline_many': 'It does not survive. {n} parts short.'},
                              'waste': {'badge': 'Alive, but wasteful',
                                        'headline': 'It lives — but you built something it will '
                                                    'never switch on.'},
                              'works': {'badge': 'Alive',
                                        'headline': 'It works. Exactly the parts the job needs, '
                                                    'and nothing spare.'}},
                 'finding_words': {'missing': 'Missing — ', 'extra': 'Installed, never used — '},
                 'waste_fallback': 'This cell has no job that needs it.',
                 'note_when': 'any',
                 'targets': 'CELL-03'},
                {'id': 'wall-and-chloroplasts',
                 'kind': 'confrontation',
                 'anchor': 's-think',
                 'demand': 'make the wrongness of CELL-04 and CELL-03 visible, each against '
                           'something the student has just built or looked at',
                 'statements': [{'targets': 'CELL-04',
                                 'quote': '“Plant cells have a cell wall instead of a cell '
                                          'membrane.”',
                                 'body': ['The wall did not replace anything. Go back to the leaf '
                                          'cell on the bench and look at the edge: there are two '
                                          'lines, one just inside the other. The outer one is the '
                                          'wall — cellulose, rigid, built to stop the cell '
                                          'bursting when water floods in. The inner one is the '
                                          'membrane, doing in a plant exactly what it does in you: '
                                          'deciding what crosses.',
                                          'A plant cell has both. An animal cell has the door and '
                                          'no box — which is why a cheek cell is a floppy bag and '
                                          'a leaf cell is a brick.'],
                                 'key_fact': 'kf-wall-outside'},
                                {'targets': 'CELL-03',
                                 'quote': '“If it is a plant cell, it has chloroplasts.”',
                                 'body': ['You built a root hair cell a moment ago: wall, vacuole, '
                                          'membrane, cytoplasm, nucleus, mitochondria — and no '
                                          'chloroplasts, because no light has ever reached it. '
                                          'Chloroplasts get built where there is light to trap, so '
                                          'a plant cell without them is still completely a plant '
                                          'cell. Most of a plant’s cells are exactly that.'],
                                 'key_fact': 'kf-chloroplasts-where-light'}]}],
 'ladder': {'recall': {'title': 'Rung 1 · Read the list',
                       'q': 'A cell has a membrane, cytoplasm, a nucleus and mitochondria — and '
                            'nothing else from the seven. What is it?',
                       'options': ['A cell from an oak leaf',
                                   'A cheek cell',
                                   'A root hair cell',
                                   'There is not enough information'],
                       'answer': 1,
                       'feedback': {0: 'A leaf cell has a wall and a vacuole as well, and near the '
                                       'top of the leaf, chloroplasts. None of those are here.',
                                    2: 'A root hair cell has no chloroplasts — but it still has a '
                                       'wall and a vacuole, and both are missing here.',
                                    3: 'There is enough. No wall and no vacuole rules out every '
                                       'plant cell on this page.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A student says a root hair cell cannot be a plant cell, because it is '
                           'not green. What is wrong with the reasoning?',
                      'options': ['Root cells build chloroplasts like every other plant cell, but '
                                  'leave the green pigment out of them',
                                  'Roots are green under the soil, so a root cell is green '
                                  'wherever you dig it up',
                                  'The green is stored in the vacuole, so a cell with a clear '
                                  'vacuole is not a plant cell',
                                  'Chloroplasts are only built where light reaches, so a plant '
                                  'cell without them is still a plant cell'],
                      'answer': 3,
                      'feedback': {0: 'Close to something true about other structures in a root, '
                                      'but not this. A root hair cell does not build chloroplasts '
                                      'at all.',
                                   1: 'They are not. Dig one up and look.',
                                   2: 'The vacuole is mostly water with sugars and salts dissolved '
                                      'in it. The green is chlorophyll, and it is inside the '
                                      'chloroplasts.'}},
            'explain': {'title': 'Rung 3 · Explain it',
                        'q': 'Down a school microscope you can see a leaf cell’s wall, its '
                             'nucleus, its vacuole and its chloroplasts — but not its mitochondria '
                             'and not its membrane. Explain why not.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Both of them are still there, but…',
                        'success': ['Says both are still there — the microscope cannot show them, '
                                    'they are not absent.',
                                    'Says a chloroplast is several times wider than a '
                                    'mitochondrion, which is why one shows and the other does not.',
                                    'Says the membrane is thinner again — only a few molecules '
                                    'across.',
                                    'Says turning the magnification up would not fix it, because '
                                    'the limit is what the microscope can separate, not how big it '
                                    'makes things.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A single cell is found in pond water. It has a cell wall, a large '
                             'vacuole, cytoplasm, a nucleus and mitochondria — and no '
                             'chloroplasts. Can you say it came from a plant? Say what you can '
                             'conclude and what you cannot.',
                        'field_label': 'Your answer',
                        'placeholder': 'The wall and the vacuole suggest…',
                        'success': ['Notes that the wall and the large vacuole are both on the '
                                    'plant side of the list.',
                                    'Notes that having no chloroplasts does not rule a plant out — '
                                    'a root cell has none either.',
                                    'Notes that a wall on its own is not proof, because things '
                                    'that are not plants have walls too.',
                                    'Ends with a decision that fits the evidence: plant-like but '
                                    'not proved, and says what would settle it.']}},
 'key_note': 'Membrane, cytoplasm, nucleus and mitochondria are in every cell here. Wall, vacuole '
             'and chloroplasts are the plant’s three extras — and chloroplasts only appear where '
             'light does.',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'The parts list',
           'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'The bench',
           'done_when': 'gate_answered'},
          {'anchor': 's-wall',
           'short': 'WALL',
           'label': 'Wall or membrane',
           'done_when': 'answers_opened'},
          {'anchor': 's-fit',
           'short': 'BUILD',
           'label': 'Fit the cell',
           'done_when': 'all_specimens_run'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'key_facts': [{'id': 'kf-wall-outside',
                'text': 'Wall on the outside, membrane just inside it. A plant cell has both.',
                'placement': 'inside:s-think',
                'ground': 'band',
                'eyebrow': 'Key fact'},
               {'id': 'kf-chloroplasts-where-light',
                'text': 'Chloroplasts are only built where light reaches. A plant cell without '
                        'them is still a plant cell.',
                'placement': 'inside:s-think',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'tutor': {'prompt': 'Still not sure which parts are the plant’s?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'ks4_becomes': 'Eukaryotic and prokaryotic cells, ribosomes and cell membranes in detail, and '
                'magnification calculations on real micrographs.',
 'safety_note': 'A cheek cell sample is your own only, taken with a clean swab that goes straight '
                'into disinfectant afterwards. Methylene blue stains skin, clothes and benches — '
                'and it does not wash out.',
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
