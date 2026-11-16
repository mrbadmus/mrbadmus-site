# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B1 `unicellular-organisms` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B1'
SOURCE_SLUG = 'unicellular-organisms'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'unicellular-organisms',
 'title': 'Unicellular organisms',
 'discipline': 'biology',
 'unit': 'cells-and-organisation',
 'family': 'CONTRAST',
 'covers': ['KS3.B.CELLS.05'],
 'touches': ['KS3.B.CELLS.02'],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 3}, {'id': 'structure-function', 'level': 2}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['levels-of-organisation'],
 'assumes': [],
 'references': [{'unit': 'B1', 'lesson': 'life-processes'},
                {'unit': 'B1', 'lesson': 'specialised-cells'}],
 'ks4_links': [],
 'big_question': 'Two single cells, one much smaller. One is a whole organism. One is a piece of '
                 'you. What tells them apart?',
 'phenomenon': {'kind': 'demo',
                'title': 'A quarter of a millimetre long, and it hunts.',
                'prompt': 'A Paramecium swims, finds food, eats it, senses obstacles, reverses, '
                          'grows and splits in two. A cheek cell is four times smaller and lines '
                          'your mouth. Neither is more alive than the other.',
                'commit': 'If you had to guess, what makes the Paramecium a whole living thing and '
                          'not just a piece of one?',
                'options': ['It does every job itself', 'It can swim about freely'],
                'reveal': 'Next: look at pond water and cheek cells under the microscope, then '
                          'work out which facts really settle it.',
                'guess': True,
                'replies': ['A Paramecium has nobody to feed it or clean up after it. It has to '
                            'feed, grow, move and reproduce all on its own.',
                            'Swimming is the eye-catching part. But what makes it a whole living '
                            'thing is that it does every job of staying alive by itself.'],
                'answer': 0},
 'misconceptions': [{'id': 'LIFE-03',
                     'statement': 'A single cell cannot be a whole living thing — it must be part '
                                  'of something bigger.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-settle'},
                    {'id': 'CELL-13',
                     'statement': 'No nucleus means no instructions — so a bacterium cannot '
                                  'divide.',
                     'elicited_by': None,
                     'confronted_by': 's-think',
                     'pairs_with': {'lesson': 'specialised-cells',
                                    'relation': 'qualifies',
                                    'claim': 'Two lessons ago: no nucleus, no instructions, no '
                                             'repair, no dividing.'}},
                    {'id': 'CELL-08',
                     'statement': 'A single-celled organism is just a simpler version of one of '
                                  'our cells — the same parts, doing less.',
                     'elicited_by': None,
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'unicellular',
                 'definition': 'Made of one single cell, which is the whole organism.',
                 'note': None},
                {'term': 'multicellular',
                 'definition': 'Made of many cells, which are usually specialised.',
                 'note': 'You are multicellular. So is every plant and animal you can see without '
                         'a microscope.'},
                {'term': 'flagellum',
                 'definition': 'A long whip that a cell beats in order to swim.',
                 'note': 'One is a flagellum, several are flagella. You have already met one: the '
                         'tail of a sperm cell.'},
                {'term': 'cilia',
                 'definition': "Short hairs covering a cell's surface, which beat together like "
                               'tiny oars.',
                 'note': 'One is a cilium. Cilia line your airways too, sweeping dust back up out '
                         'of your lungs.'}],
 'figures': [],
 'core': [{'type': 'hook', 'anchor': 's-hook'},
          {'type': 'practical', 'anchor': 's-scope', 'id': 'microscope-bench'},
          {'type': 'comparison',
           'anchor': 's-compare',
           'eyebrow': 'Side by side',
           'eyebrow_tone': 'accent-text',
           'statement': 'The same seven processes. One cell does all of them; one does one.',
           'ground': 'band',
           'columns': [{'caption': 'Paramecium', 'tone': 'alert'},
                       {'caption': 'One of your cheek cells', 'tone': 'on-dark'}],
           'rows': [{'name': 'Movement',
                     'cells': ['Beats hundreds of cilia and swims, reversing when it hits '
                               'something.',
                               'Does not move. It is held in a sheet by the cells around it.']},
                    {'name': 'Respiration',
                     'cells': ['Its own mitochondria, releasing energy for its own swimming and '
                               'feeding.',
                               'Mitochondria too — but the oxygen is delivered to it by blood.']},
                    {'name': 'Sensitivity',
                     'cells': ['Senses an obstacle and backs away from it.',
                               'Senses nothing. Nerve cells do that for the whole of you.']},
                    {'name': 'Growth',
                     'cells': ['Grows until it is big enough to divide.',
                               'Does not grow. It is replaced when it wears out.']},
                    {'name': 'Reproduction',
                     'cells': ['Splits in two, and then there are two organisms.',
                               'Divides to replace itself, and there is still only one of you.']},
                    {'name': 'Excretion',
                     'cells': ['Vacuoles collect the water that keeps seeping in and squeeze it '
                               'back out.',
                               'Waste passes into the blood, and your kidneys deal with it.']},
                    {'name': 'Nutrition',
                     'cells': ['Sweeps food into an oral groove and digests it in a vacuole inside '
                               'itself.',
                               'Is fed. Glucose arrives dissolved in blood, already digested.']}],
           'row_tones': ['ink', 'ink-body'],
           'key_fact': {'ref': 'kf-one-cell-all-seven'}},
          {'type': 'check', 'id': 's-settle', 'anchor': 's-settle'},
          {'type': 'misconception', 'anchor': 's-think', 'id': 'think-again'},
          {'type': 'quiz', 'anchor': 's-ladder', 'ref': 'ladder'},
          {'type': 'summary', 'anchor': 's-keynote', 'ref': 'key_note'}],
 'stretch': [{'type': 'explainer',
              'text': 'Euglena is the awkward one. It is green, traps light and makes its own food '
                      'like a plant; it also swims after food with a flagellum and can feed like '
                      'an animal in the dark. Biologists spent a century arguing about which '
                      'kingdom it belonged in, and the answer they settled on was that the '
                      'question was wrong — it belongs to neither, and single-celled life does not '
                      'sort neatly into plant and animal at all. Being hard to classify is not a '
                      'fault in the organism. It is information about the categories.'}],
 'support': [],
 'activities': [{'id': 'microscope-bench',
                 'kind': 'lab',
                 'demand': 'two mounts, one instrument: find, centre, then climb',
                 'eyebrow': 'At the bench · two slides',
                 'heading': 'Pond water, then your own cheek',
                 'lede': 'Same microscope, same magnifications, two mounts. Find something, centre '
                         'it, then climb — exactly as you learnt.',
                 'progress_format': '{n} of {total} mounts seen at ×400',
                 'prompt': 'Commit first. At which magnification will you first be able to tell '
                           'one pond organism from another?',
                 'options': ['×40 — the lowest power',
                             '×100',
                             '×400 — the highest',
                             'You never can with a school microscope'],
                 'sim': {'kind': 'microscope',
                         'controls': ['specimen', 'magnification', 'centre', 'motion', 'focus'],
                         'control_labels': {'specimen': 'Mount',
                                            'magnification': 'Objective',
                                            'centre': 'Move the slide to',
                                            'motion': 'Movement'},
                         'mounts': [{'id': 'pond',
                                     'label': 'Pond water',
                                     'specimen': 'pond water',
                                     'note': 'The dots scattered between them are bacteria, about '
                                             '0.002 mm long. Even at ×400 they are two pixels of '
                                             'nothing — you can see that they are there, not what '
                                             'they are. Every organism on this slide is doing all '
                                             'seven life processes for itself.',
                                     'caption': 'Real ones swim out of the field in seconds. These '
                                                'are held for you, and the slide moves when you '
                                                'ask it to.',
                                     'alt': 'A microscope field of pond water containing an '
                                            'amoeba, two paramecia, three euglena and scattered '
                                            'bacteria at various depths.',
                                     'organisms': [{'kind': 'amoeba',
                                                    'x': -0.9,
                                                    'y': 0.3,
                                                    'depth': -0.045,
                                                    'len': 0.3,
                                                    'seed': 0.4},
                                                   {'kind': 'paramecium',
                                                    'x': 0.15,
                                                    'y': -0.1,
                                                    'depth': 0,
                                                    'len': 0.25,
                                                    'seed': 1.1},
                                                   {'kind': 'euglena',
                                                    'x': 0.58,
                                                    'y': 0.46,
                                                    'depth': 0.05,
                                                    'len': 0.05,
                                                    'seed': 2.3},
                                                   {'kind': 'euglena',
                                                    'x': -0.3,
                                                    'y': -0.58,
                                                    'depth': -0.02,
                                                    'len': 0.05,
                                                    'seed': 3.7},
                                                   {'kind': 'paramecium',
                                                    'x': 1.45,
                                                    'y': 0.95,
                                                    'depth': 0.03,
                                                    'len': 0.25,
                                                    'seed': 0.8},
                                                   {'kind': 'amoeba',
                                                    'x': 1.95,
                                                    'y': -1.15,
                                                    'depth': -0.07,
                                                    'len': 0.3,
                                                    'seed': 2.9},
                                                   {'kind': 'euglena',
                                                    'x': -1.6,
                                                    'y': 1.1,
                                                    'depth': 0.015,
                                                    'len': 0.05,
                                                    'seed': 1.6}]},
                                    {'id': 'cheek',
                                     'label': 'Cheek cells',
                                     'specimen': 'cheek cells',
                                     'note': 'One layer, one shape, no movement. Racking the focus '
                                             'finds nothing behind them, because a smear is a '
                                             'sheet. Every cell here does one job, and none of '
                                             'them is an organism.',
                                     'caption': 'Stained, so the nuclei show. Unstained you would '
                                                'see almost nothing.',
                                     'alt': 'A microscope field of flat, still cheek cells in a '
                                            'single layer, each with a stained nucleus.',
                                     'organisms': []}],
                         'start_mount': 'pond',
                         'centres': [{'id': 'amoeba', 'label': 'The blob', 'x': -0.9, 'y': 0.3},
                                     {'id': 'paramecium',
                                      'label': 'The slipper',
                                      'x': 0.15,
                                      'y': -0.1},
                                     {'id': 'euglena',
                                      'label': 'The green spindle',
                                      'x': 0.58,
                                      'y': 0.46}],
                         'centre_offered_on': ['pond'],
                         'motion_toggle': True,
                         'motion_default': True,
                         'motion_labels': ['Swimming', 'Held still'],
                         'resolve_notes': {40: 'Specks, and one or two shapes. You can see that '
                                               'something in there is alive. You cannot see what '
                                               'it is, and nothing you have been told about cilia '
                                               'or eyespots is visible yet.',
                                           100: 'Outlines. You can now tell one kind from another '
                                                'by shape and by how it moves — but the insides '
                                                'are still a blur.',
                                           400: 'Structures. Cilia, the eyespot, a vacuole filling '
                                                'and emptying. The field is 0.45 mm across, so '
                                                'almost all of the slide has gone.'}}},
                {'id': 'think-again',
                 'kind': 'confrontation',
                 'demand': "resolve B1-04's rule against a bacterium, then kill 'one cell means "
                           "simple'",
                 'statements': [{'targets': 'CELL-13',
                                 'quote': 'No nucleus means no instructions — so a bacterium '
                                          'cannot divide.',
                                 'answer': 'Two lessons ago that was exactly right, about a red '
                                           'blood cell. It is wrong here, and the difference is '
                                           'worth being precise about. A red blood cell '
                                           '<em>had</em> a nucleus and destroyed it, and the DNA '
                                           'went with it. A bacterium never had one: its DNA is '
                                           'there, in a loose loop in the cytoplasm, with no '
                                           'membrane around it. Instructions present, container '
                                           'absent. That is why a bacterium can divide every '
                                           'twenty minutes and a red blood cell can never divide '
                                           'again.'},
                                {'targets': 'CELL-08',
                                 'quote': 'One cell means simple.',
                                 'answer': 'Compare what you have just looked at. Your cheek cell '
                                           'has a membrane, cytoplasm, a nucleus and mitochondria, '
                                           'and it is fed, cleaned, positioned and defended by the '
                                           'rest of you. A Paramecium has all of that plus cilia '
                                           'to swim, an oral groove to feed, food vacuoles to '
                                           'digest, and vacuoles that bail out water it cannot '
                                           'stop taking in. It has more machinery than your cell, '
                                           'not less, because there is nobody to do any of it for '
                                           'it.'}]},
                {'demand': 'discriminate: sixteen judgements, and most of the facts decide nothing',
                 'eyebrow': 'Your turn · four mystery cells',
                 'heading': 'Does that settle it?',
                 'instruction': 'Every fact below each cell is true. Most of them settle nothing, '
                                'because they are true of single-celled organisms <em>and</em> of '
                                'cells inside a body. Mark only the ones that decide it.',
                 'choice_labels': ['Settles it', 'Settles nothing'],
                 'reveal_label': 'Show what settles it',
                 'progress_format': '{n} of {total} marked',
                 'progress_opened': 'Opened',
                 'why_openers': ['Settles it.', 'Settles nothing.'],
                 'self_check': {'question': 'Now look back at your four marks. Did you have it?',
                                'options': ['Yes — I marked what settles it, and nothing else.',
                                            'Partly — I marked one of them, and something else as '
                                            'well.',
                                            'No — I went for the vivid facts and missed the quiet '
                                            'ones.'],
                                'note': 'Nobody marks this but you. The facts you marked wrongly '
                                        'are the ones to read again before the next cell.'},
                 'cases': [{'id': 'c1',
                            'label': 'Mystery cell 1',
                            'tab_label': 'Cell 1',
                            'description': 'About 0.05 mm long. It is green, and it swims using '
                                           'one long whip at the front.',
                            'features': [{'text': 'It can swim.',
                                          'settles': False,
                                          'why': 'A sperm cell swims. So does a white blood cell, '
                                                 'through tissue. Moving on your own tells you '
                                                 'nothing about whether you are an organism.'},
                                         {'text': 'It is green, and makes its own food from light.',
                                          'settles': True,
                                          'why': 'Nothing in an animal body makes its own food. A '
                                                 'cell feeding itself is not being fed by an '
                                                 'organism — so it is one.'},
                                         {'text': 'It has mitochondria.',
                                          'settles': False,
                                          'why': 'Every cell in both columns has mitochondria. A '
                                                 'fact that is true of everything discriminates '
                                                 'nothing.'},
                                         {'text': 'It is only 0.05 mm long.',
                                          'settles': False,
                                          'why': 'Size never settles it. Your cheek cell is 0.06 '
                                                 'mm and a Paramecium is 0.25 mm — the bigger one '
                                                 'is the organism here, and that is a '
                                                 'coincidence.'}],
                            'verdict_label': 'It is an organism',
                            'answer': 'Euglena — a single-celled organism.',
                            'why': 'Green, so it makes its own food; a flagellum, so it can go and '
                                   'find light. One fact out of four did the work.'},
                           {'id': 'c2',
                            'label': 'Mystery cell 2',
                            'tab_label': 'Cell 2',
                            'description': 'It has a long tail and swims fast in one direction. It '
                                           'never feeds.',
                            'features': [{'text': 'It has a tail and swims.',
                                          'settles': False,
                                          'why': 'So does Euglena. Swimming is the most misleading '
                                                 'fact on this page.'},
                                         {'text': 'It never feeds.',
                                          'settles': True,
                                          'why': 'An organism must take in nutrition. A cell that '
                                                 'never feeds is being supplied by something '
                                                 'larger — and everything it will ever spend was '
                                                 'loaded before it set out.'},
                                         {'text': 'It carries half a set of chromosomes.',
                                          'settles': True,
                                          'why': 'Half a set is only useful if it is going to be '
                                                 'added to another half. Nothing that lives on its '
                                                 'own has half its instructions.'},
                                         {'text': 'It is packed with mitochondria.',
                                          'settles': False,
                                          'why': 'True, and it tells you the cell works hard. A '
                                                 'Paramecium is packed with them too.'}],
                            'verdict_label': 'It is part of an organism',
                            'answer': 'A sperm cell — one cell of a multicellular organism.',
                            'why': 'Two facts settled it, and neither was the swimming. Some cases '
                                   'have more than one discriminator; the skill is spotting which '
                                   'facts qualify, not counting them.'},
                           {'id': 'c3',
                            'label': 'Mystery cell 3',
                            'tab_label': 'Cell 3',
                            'description': 'It has no nucleus at all. In warm conditions it '
                                           'divides about every twenty minutes.',
                            'features': [{'text': 'It has no nucleus.',
                                          'settles': False,
                                          'why': 'A red blood cell has no nucleus either, and that '
                                                 'is a part of you. Missing a nucleus settles '
                                                 'nothing on its own.'},
                                         {'text': 'It divides on its own, over and over.',
                                          'settles': True,
                                          'why': 'A red blood cell can never divide again. A cell '
                                                 'that makes more of itself unaided is reproducing '
                                                 '— the sixth life process — and so it is an '
                                                 'organism.'},
                                         {'text': 'It is very small — about 0.002 mm.',
                                          'settles': False,
                                          'why': 'Size again. It is the smallest thing on the '
                                                 'slide and it is still a complete organism.'},
                                         {'text': 'Its DNA sits in a loose loop in the cytoplasm.',
                                          'settles': True,
                                          'why': 'No cell in your body does this. Yours keep their '
                                                 'DNA inside a nucleus, always. Loose DNA is a '
                                                 'different kind of cell entirely.'}],
                            'verdict_label': 'It is an organism',
                            'answer': 'A bacterium — a single-celled organism with no nucleus.',
                            'why': 'Its instructions are present; only the container is missing. '
                                   'That is exactly why it can divide when a red blood cell '
                                   'cannot.'},
                           {'id': 'c4',
                            'label': 'Mystery cell 4',
                            'tab_label': 'Cell 4',
                            'description': 'It changes shape constantly, flows around a smaller '
                                           'cell, and takes it inside itself.',
                            'features': [{'text': 'It changes shape as it moves.',
                                          'settles': False,
                                          'why': 'A white blood cell squeezes out of a blood '
                                                 'vessel and crawls through tissue by changing '
                                                 'shape. This is not a giveaway.'},
                                         {'text': 'It flows around another cell and engulfs it.',
                                          'settles': False,
                                          'why': 'This is the hardest one. A white blood cell '
                                                 'engulfs bacteria in exactly this way — and it is '
                                                 'part of you. Behaviour is not evidence.'},
                                         {'text': 'Nothing else feeds it and nothing else '
                                                  'positions it.',
                                          'settles': True,
                                          'why': 'It is on its own. Whatever it eats, it found; '
                                                 'wherever it is, it went. That is an organism.'},
                                         {'text': 'It has a vacuole that keeps filling with water '
                                                  'and squeezing it out.',
                                          'settles': True,
                                          'why': 'Your body holds the fluid around its cells '
                                                 'steady, so no cell of yours needs to bail out. A '
                                                 'cell that must manage its own water is not '
                                                 'inside a body.'}],
                            'verdict_label': 'It is an organism',
                            'answer': 'Amoeba — a single-celled organism.',
                            'why': 'The two most vivid facts — shape-changing and engulfing — are '
                                   'the two that settle nothing, because a white blood cell does '
                                   'both. The quiet facts did the work.'}],
                 'id': 's-settle',
                 'kind': 'settles-it'}],
 'ladder': {'recall': {'title': 'Rung 1 · Discriminate',
                       'q': 'A single cell moves on its own, has mitochondria, and is about 0.05 '
                            'mm long. Which of these would settle whether it is an organism or '
                            'part of one?',
                       'options': ['How fast it moves',
                                   'Whether it feeds itself, or is fed',
                                   'How many mitochondria it has',
                                   'Whether it is bigger than one of your cells'],
                       'answer': 1,
                       'feedback': {0: 'Speed is a detail about the movement. Movement itself does '
                                       'not discriminate, so nothing about it can.',
                                    2: 'Both kinds have mitochondria, and busy cells of both kinds '
                                       'have many. A shared feature cannot separate them.',
                                    3: 'Size never settles it. A Paramecium is four times the size '
                                       'of your cheek cell, and Euglena is smaller than it.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A red blood cell has no nucleus and can never divide. A bacterium has '
                           'no nucleus and divides every twenty minutes. What explains the '
                           'difference?',
                      'options': ['The bacterium still has its DNA, loose in the cytoplasm; the '
                                  'red blood cell lost its DNA with its nucleus',
                                  'A smaller cell divides more easily, so the smallest cells are '
                                  'the ones that divide fastest',
                                  'A cell that loses its nucleus later in life can still divide, '
                                  'because it had one to begin with',
                                  'Dividing needs no instructions at all, so any cell without a '
                                  'nucleus can still copy itself freely'],
                      'answer': 0,
                      'feedback': {1: 'Size has nothing to do with it. The difference is about the '
                                      'instructions, not the effort.',
                                   2: 'Having had one does not help: the red blood cell destroyed '
                                      'its nucleus and lost the DNA with it. The bacterium never '
                                      'had a nucleus at any point.',
                                   3: 'Nothing copies itself without instructions. Every new '
                                      'bacterium gets a full copy of the loop.'}},
            'explain': {'title': 'Rung 3 · Explain both sides',
                        'q': 'A Paramecium and one of your cheek cells are both single cells. '
                             'Explain why the Paramecium needs cilia, an oral groove and a '
                             'contractile vacuole, and why your cheek cell needs none of the '
                             'three. Your answer must say something about both cells.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The Paramecium needs… whereas the cheek cell…',
                        'success': ['Says the Paramecium has to carry out all seven life processes '
                                    'by itself.',
                                    'Links each of the three structures to a process it does for '
                                    'itself — moving, feeding, and getting rid of water.',
                                    'Says the cheek cell does one job and the rest of the body '
                                    'does the others for it.',
                                    'Names at least one thing the body does for the cheek cell — '
                                    'feeds it, moves things to it, holds it in place, or keeps the '
                                    'fluid around it steady.',
                                    'Ends on the discriminator rather than on size or on how '
                                    'interesting either cell looks.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A student finds a single cell in a drop of water from a plant pot. '
                             'It has a wall, changes shape a little, has no chloroplasts, and buds '
                             'off smaller copies of itself. They say it must be part of a plant '
                             'because it has a wall. Say whether they are right, which fact you '
                             'would use instead, and what you would still want to check.',
                        'field_label': 'Your answer',
                        'placeholder': 'The wall does not settle it, because…',
                        'success': ['Says a wall does not settle it, and gives a reason — walls '
                                    'are not unique to plants.',
                                    'Picks budding off copies of itself as the fact that does the '
                                    'work, and says why: it is reproducing on its own.',
                                    'Says having no chloroplasts does not rule a plant cell out '
                                    'either, using the root cell as the reason.',
                                    'Names something they would still check — whether it feeds '
                                    'itself, or whether it is attached to anything larger.']}},
 'key_note': 'A unicellular organism is one cell that does all seven life processes for itself. '
             'Its adaptations — cilia, an oral groove, a contractile vacuole, a loose loop of DNA '
             '— are what a whole organ system does for one of your cells.',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'What settles it',
           'done_when': 'committed'},
          {'anchor': 's-scope',
           'short': 'SCOPE',
           'label': 'Two slides',
           'done_when': 'states_seen',
           'states': ['pond:400', 'cheek:400']},
          {'anchor': 's-settle',
           'short': 'SETTLE',
           'label': 'Four mystery cells',
           'done_when': 'all_cases_revealed',
           'threshold': 4},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'key_facts': [{'id': 'kf-one-cell-all-seven',
                'text': 'One cell doing all seven life processes is an organism. One cell doing '
                        'one job is part of one.',
                'eyebrow': 'Key fact',
                'placement': 'inside:s-compare',
                'ground': 'card'}],
 'tutor': {'prompt': 'Not sure which fact settles it?',
           'cta': 'Ask about this lesson',
           'anchor': 's-settle'},
 'safety_note': 'Pond water is not sterile. Keep it away from your mouth and cuts, seal slides '
                'with a coverslip, and wash your hands before you leave the lab.',
 'ks4_becomes': 'Bacterial cell structure, culturing microorganisms, and how single-celled '
                'organisms cause and fight disease.',
 'ws': ['experimental-skills-and-investigations'],
 'review_state': 'draft',
 'authored': True}
