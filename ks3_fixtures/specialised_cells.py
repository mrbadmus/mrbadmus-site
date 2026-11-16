# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B1 `specialised-cells` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B1'
SOURCE_SLUG = 'specialised-cells'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'specialised-cells',
 'title': 'Specialised cells',
 'discipline': 'biology',
 'unit': 'cells-and-organisation',
 'family': 'SYSTEM',
 'covers': ['KS3.B.CELLS.04'],
 'touches': ['KS3.B.CELLS.02'],
 'beyond_statutory': False,
 'threads': [{'id': 'structure-function', 'level': 2}, {'id': 'cells-and-systems', 'level': 2}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['animal-and-plant-cells'],
 'assumes': [],
 'references': [{'unit': 'B1', 'lesson': 'levels-of-organisation'},
                {'unit': 'B1', 'lesson': 'unicellular-organisms'}],
 'ks4_links': [],
 'ks4_becomes': 'Cell differentiation, exchange surfaces and surface area to volume ratio, and '
                'active transport at the root hair.',
 'big_question': 'One cell in your body throws its nucleus away. Why would anything do that?',
 'phenomenon': {'kind': 'narrative',
                'eyebrow': 'Start here',
                'title': 'Last lesson: no nucleus, no instructions, no repair, no dividing.',
                'prompt': 'All still true. And yet: a red blood cell starts out with a nucleus, in '
                          'the marrow inside your bones, and as it matures it pushes that nucleus '
                          'out and destroys it. It can then never repair itself and never divide, '
                          'and it lasts about a hundred and twenty days. Your body does this '
                          'deliberately, two million times a second.',
                'commit': 'If you had to guess, what does the red blood cell gain by throwing its '
                          'nucleus away?',
                'options': ['More room inside', 'A faster trip'],
                'reveal': 'Every specialised cell makes a trade like this. Next: four cells on one '
                          'bench, to see what each has given up and gained.',
                'pairs_with': {'lesson': 'unicellular-organisms',
                               'relation': 'qualified-by',
                               'qualifier': 'CELL-13'},
                'guess': True,
                'replies': ['Room is the gain. The space the nucleus leaves is packed with '
                            'haemoglobin, the red stuff that carries oxygen.',
                            'Less baggage does sound faster, but blood cells are carried along by '
                            'the flow. What the cell gains is room for its cargo.'],
                'answer': 0},
 'misconceptions': [{'id': 'CELL-14',
                     'statement': 'Specialised cells are made of different parts from ordinary '
                                  'cells.',
                     'elicited_by': 's-tuned',
                     'confronted_by': 'same-seven-tuned'},
                    {'id': 'CELL-15',
                     'statement': 'A red blood cell is not really a cell, then.',
                     'elicited_by': 's-hook',
                     'confronted_by': 'same-seven-tuned'},
                    {'id': 'CELL-05',
                     'statement': 'Every cell in your body has a nucleus.',
                     'elicited_by': 's-hook',
                     'confronted_by': 'same-seven-tuned'}],
 'vocabulary': [{'term': 'specialised',
                 'definition': 'Built to do one particular job very well.',
                 'note': 'The price is that a specialised cell is usually no good at anything '
                         'else.'},
                {'term': 'adaptation',
                 'definition': 'A feature that helps something do its job.',
                 'note': 'Here the adaptation is a feature of one single cell. Later you will meet '
                         'adaptations of whole organisms.'},
                {'term': 'surface area',
                 'definition': 'The total amount of outside surface something has.',
                 'note': 'Squash a cell flat, or grow it a long thin hair, and its surface area '
                         'goes up without much more inside to supply.'},
                {'term': 'haemoglobin',
                 'definition': 'The red protein that fills a red blood cell and that oxygen sticks '
                               'to.',
                 'note': 'It is what the nucleus made room for.'},
                {'term': 'biconcave',
                 'definition': 'Dished in on both sides — a disc squashed at the middle.',
                 'note': 'Same volume as a ball, much more surface, and floppy enough to fold.'}],
 'figures': [],
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The trade', 'done_when': 'committed'},
          {'anchor': 's-tuned',
           'short': 'TUNED',
           'label': 'Same seven parts',
           'done_when': 'all_specimens_seen'},
          {'anchor': 's-break',
           'short': 'BREAK',
           'label': 'Break it on purpose',
           'done_when': 'predictions_made',
           'threshold': 4},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'key_facts': [{'text': 'A specialised cell has no new parts. The same seven are turned up, turned '
                        'down, or reshaped.',
                'placement': 'top-level',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'tutor': {'prompt': 'Not sure which problem a cell is solving?',
           'cta': 'Ask about this lesson',
           'anchor': 's-rule'},
 'named_conditions': False,
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'check', 'id': 's-tuned', 'anchor': 's-tuned'},
          {'type': 'practical', 'id': 's-break', 'anchor': 's-break'},
          {'type': 'rule',
           'anchor': 's-rule',
           'eyebrow': 'What settles it',
           'statement': 'Every adaptation is an answer to a physical problem.',
           'sub': 'There are only a few problems a single cell can be up against. Once you can '
                  'name the problem, the shape stops being a fact to memorise and becomes the '
                  'obvious solution.',
           'cards': [{'label': 'Problem 1',
                      'title': 'Not enough surface',
                      'body': 'Everything enters a cell through its surface. Need more in? Get '
                              'more surface: a long thin hair, a folded edge, a flattened disc.',
                      'examples': 'Root hair cell · red blood cell'},
                     {'label': 'Problem 2',
                      'title': 'Too far to travel',
                      'body': 'A message from your toe to your spine has a metre to cross. Passing '
                              'it from cell to cell costs time at every handover, so one cell is '
                              'stretched the whole way.',
                      'examples': 'Nerve cell'},
                     {'label': 'Problem 3',
                      'title': 'Work that never stops',
                      'body': 'Movement costs energy, and energy comes from mitochondria. A cell '
                              'that swims, contracts or sweeps all day is crammed with them.',
                      'examples': 'Sperm cell · muscle cell · ciliated cell'},
                     {'label': 'Problem 4',
                      'title': 'Nowhere to put the cargo',
                      'body': 'A cell that carries something needs room for it, and room has to '
                              'come from somewhere. This is the only problem on the list solved by '
                              'throwing a part away.',
                      'examples': 'Red blood cell'}]},
          {'type': 'misconception', 'id': 'same-seven-tuned', 'anchor': 's-think'},
          {'type': 'key-fact', 'ref': 0},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'stretch': [{'type': 'explainer',
              'id': 'the-maintenance-bill',
              'text': 'Something has to keep replacing them, and it does: about two million new '
                      'cells a second, from marrow in your ribs, spine, hips and the ends of your '
                      'long bones. That is the hidden cost of the trade — cargo space bought with '
                      'a maintenance bill handed to the rest of the body. Why keep paying it? '
                      'Because roughly five in every six of your cells are red blood cells, and '
                      'the space the nucleus would have taken is haemoglobin in every single '
                      'one.'}],
 'support': [],
 'activities': [{'id': 'same-seven-tuned',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': ['CELL-14', 'CELL-15'],
                 'statements': [{'targets': 'CELL-14',
                                 'quote': 'Specialised cells are made of different parts from '
                                          'ordinary cells.',
                                 'answer': 'There is no such thing as an ordinary cell. Every cell '
                                           'in the four you just looked at is built from the same '
                                           'seven parts as the cheek cell — the tuning is what '
                                           'differs. A nerve cell has a nucleus, cytoplasm, a '
                                           'membrane and mitochondria; so does a sperm cell; so '
                                           'does a root hair cell, plus its wall and its vacuole. '
                                           'Nothing on the parts list is new. What changes is how '
                                           'much of each, and what shape the whole thing is pulled '
                                           'into.'},
                                {'targets': 'CELL-15',
                                 'quote': 'A red blood cell is not really a cell, then.',
                                 'answer': 'It is. It was made in the marrow with a full nucleus '
                                           'and everything else, and it gave the nucleus up on the '
                                           'way to the job — the way you might take the back seats '
                                           'out of a van. It still has a membrane, still has '
                                           'cytoplasm, still carries oxygen for about a hundred '
                                           'and twenty days. What it cannot do is repair itself or '
                                           'divide, and that is the price of the room it '
                                           'gained.'}]},
                {'eyebrow': 'The bench · same seven parts',
                 'heading': 'Nothing new was added. Something was turned up, and something was '
                            'turned down.',
                 'prompt': 'These are the same seven parts you numbered last lesson. Pick a cell '
                           'and read what has been tuned — and what the tuning is for.',
                 'start': 'red',
                 'specimens': [{'id': 'red',
                                'name': 'Red blood cell',
                                'tag': 'In your blood',
                                'job': 'Carry oxygen from your lungs to every working cell.',
                                'where': 'Made in bone marrow, then pushed round your body about '
                                         'once a minute for four months. Twenty-five trillion are '
                                         'in you right now.',
                                'problem': 'Nowhere to put the cargo — and not enough surface to '
                                           'load it through.',
                                'caption': 'A capillary, with red blood cells folding through it '
                                           'single file.',
                                'alt': 'A narrow blood capillary in cross-section with three '
                                       'biconcave red blood cells passing through it in single '
                                       'file.',
                                'drawing': 'red',
                                'tuning': [{'dial': 'GONE',
                                            'part': 'Nucleus (3)',
                                            'why': 'Pushed out and destroyed as the cell matures. '
                                                   'The space it freed is filled with haemoglobin, '
                                                   'the red protein that oxygen sticks to.'},
                                           {'dial': 'SHAPE',
                                            'part': 'Whole cell',
                                            'why': 'A disc squashed in at the middle — biconcave. '
                                                   'Same volume, much more surface, so oxygen '
                                                   'loads and unloads faster. It also folds to '
                                                   'squeeze through vessels narrower than itself.'},
                                           {'dial': 'NONE',
                                            'part': 'Mitochondria (4)',
                                            'why': 'It has none either — which means it cannot use '
                                                   'any of the oxygen it is carrying. A courier '
                                                   'that ate the parcel would be no use.'}]},
                               {'id': 'root',
                                'name': 'Root hair cell',
                                'tag': 'In a plant root',
                                'job': 'Pull water and dissolved minerals out of the soil.',
                                'where': 'Just behind the growing tip of every root, in a fuzz of '
                                         'millions. They last days, then are replaced further '
                                         'along as the root pushes on.',
                                'problem': 'Not enough surface. Water is spread thinly over soil '
                                           'particles, and it has to be collected.',
                                'caption': 'A root hair cell, with its hair pushed out between '
                                           'soil particles.',
                                'alt': 'A root hair cell in root tissue with a long thin hair '
                                       'extending into soil between soil particles, and arrows '
                                       'showing water entering.',
                                'drawing': 'root',
                                'tuning': [{'dial': 'SHAPE',
                                            'part': 'Whole cell',
                                            'why': 'Drawn out into a long thin finger that pushes '
                                                   'between soil particles. The hair alone can be '
                                                   'more than ten times the length of the cell '
                                                   'body, and almost all of the surface is on it.'},
                                           {'dial': 'NONE',
                                            'part': 'Chloroplasts (7)',
                                            'why': 'No light reaches a root, so none are built. '
                                                   'This cell is a plant cell and it is not '
                                                   'green.'},
                                           {'dial': 'MORE',
                                            'part': 'Mitochondria (4)',
                                            'why': 'Water arrives on its own, but minerals have to '
                                                   'be dragged in against the flow, and dragging '
                                                   'costs energy. So this cell keeps a large '
                                                   'supply of mitochondria.'}]},
                               {'id': 'sperm',
                                'name': 'Sperm cell',
                                'tag': 'A sex cell',
                                'job': 'Travel a long way, and deliver half a set of instructions.',
                                'where': 'Made in the testes, and built for one journey it will '
                                         'make once. Most never arrive.',
                                'problem': 'Work that never stops, over a distance that is '
                                           'enormous for one cell.',
                                'caption': 'A sperm cell: head, mitochondria-packed midpiece, and '
                                           'tail.',
                                'alt': 'A sperm cell with a rounded head containing a nucleus, a '
                                       'midpiece full of mitochondria, and a long wavy tail.',
                                'drawing': 'sperm',
                                'tuning': [{'dial': 'SHAPE',
                                            'part': 'Whole cell',
                                            'why': 'A streamlined head and a long tail that whips '
                                                   'from side to side. Nothing about this cell is '
                                                   'built to sit still.'},
                                           {'dial': 'MORE',
                                            'part': 'Mitochondria (4)',
                                            'why': 'Packed into the middle section, right behind '
                                                   'the head, feeding the tail. Swimming for hours '
                                                   'is expensive and there is nowhere to refuel.'},
                                           {'dial': 'HALF',
                                            'part': 'Nucleus (3)',
                                            'why': 'It carries half a set of chromosomes, not a '
                                                   'full set, so that it can be added to the half '
                                                   'in the egg. This is the one cell on the page '
                                                   'whose nucleus is deliberately incomplete.'}]},
                               {'id': 'nerve',
                                'name': 'Nerve cell',
                                'tag': 'In your nervous system',
                                'job': 'Carry a signal a long way, fast.',
                                'where': 'From your spine to your toe can be a single cell over a '
                                         'metre long — the longest cells in your body by a wide '
                                         'margin.',
                                'problem': 'Too far to travel, and every handover between cells '
                                           'costs time.',
                                'caption': 'A nerve cell: branched ends, and a long sheathed cable '
                                           'between them.',
                                'alt': 'A nerve cell with branching dendrites, a long axon covered '
                                       'in segments of fatty sheath with gaps between them, and '
                                       'branched terminals.',
                                'drawing': 'nerve',
                                'tuning': [{'dial': 'SHAPE',
                                            'part': 'Whole cell',
                                            'why': 'Drawn out into one enormous thread. Branches '
                                                   'at both ends collect signals in and pass them '
                                                   'on; the middle is pure cable.'},
                                           {'dial': 'EXTRA',
                                            'part': 'Fatty sheath',
                                            'why': 'A fatty covering wrapped round the cable in '
                                                   'segments with tiny gaps between them. The '
                                                   'signal jumps from gap to gap instead of '
                                                   'creeping along, which makes it many times '
                                                   'faster. The sheath is not one of the nerve '
                                                   "cell's own parts — it is made of other cells "
                                                   'wrapped tightly around it, which is why it is '
                                                   'not on the list of seven.'},
                                           {'dial': 'MORE',
                                            'part': 'Mitochondria (4)',
                                            'why': 'Concentrated at the branched ends, where the '
                                                   'signal is passed to the next cell. That '
                                                   'handover is the expensive part.'}]}],
                 'id': 's-tuned',
                 'kind': 'system-bench',
                 'demand': 'investigate'},
                {'bench': 's-tuned',
                 'eyebrow': 'Break it on purpose',
                 'heading': 'Take the adaptation away',
                 'lede': 'Knowing the parts is not knowing the system. Sabotage one thing about '
                         '{specimen}, say what you think breaks first, and then follow it out from '
                         'the cell to the whole organism.',
                 'commit': 'Commit first. What breaks first?',
                 'specimens': [{'specimen': 'red',
                                'options': [{'id': 'sphere',
                                             'label': 'Make it a sphere',
                                             'what': 'Round it out. Same volume of cell, no dimple '
                                                     'in the middle, and stiff instead of floppy.',
                                             'predict': ['It cannot carry haemoglobin any more',
                                                         'It has less surface, and it can no '
                                                         'longer fold through narrow vessels',
                                                         'It runs out of energy'],
                                             'caption': 'The same cells, rounded out and stiff, '
                                                        'jamming at a narrowing.',
                                             'alt': 'Spherical red blood cells too large and rigid '
                                                    'to pass through a narrowing in the capillary.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'Rounding it up gives the same '
                                                                'volume the smallest possible '
                                                                'surface. Oxygen now has less '
                                                                'membrane to cross, so loading and '
                                                                'unloading both slow down.'},
                                                       {'scale': 'The vessel',
                                                        'text': 'The narrowest capillaries are '
                                                                'thinner than a red blood cell. A '
                                                                'floppy disc folds and slips '
                                                                'through; a stiff ball wedges, and '
                                                                'everything behind it stops too.'},
                                                       {'scale': 'The whole body',
                                                        'text': 'Tissues past the blockage get '
                                                                'less oxygen than they need, and '
                                                                'the spleen destroys the misshapen '
                                                                'cells early, so there are fewer '
                                                                'of them as well.'}],
                                             'close': 'This is not hypothetical. In hereditary '
                                                      'spherocytosis the red cells really are '
                                                      'round and stiff, and the result is exactly '
                                                      'this: tiredness, and a spleen working '
                                                      'overtime.',
                                             'close_safe': 'Shape is not decoration here. There '
                                                           'are real inherited conditions in which '
                                                           'red cells come out round and stiff '
                                                           'instead of flexible discs, and '
                                                           'tiredness is the first thing people '
                                                           'notice.'},
                                            {'id': 'nucleus',
                                             'label': 'Give the nucleus back',
                                             'what': 'Let it keep the nucleus it would normally '
                                                     'destroy. Everything else stays the same.',
                                             'predict': ['It carries less oxygen',
                                                         'It cannot fit through capillaries at all',
                                                         'It stops being able to divide'],
                                             'caption': 'The same cells, each with the nucleus it '
                                                        'should have given up.',
                                             'alt': 'Red blood cells each containing a nucleus, '
                                                    'with visibly less haemoglobin packed around '
                                                    'it.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'The nucleus occupies space that '
                                                                'haemoglobin was using. Less '
                                                                'haemoglobin means less oxygen '
                                                                'carried per cell — and the '
                                                                'nucleus is in the way of the '
                                                                'dimple, so the shape suffers '
                                                                'too.'},
                                                       {'scale': 'The blood',
                                                        'text': 'The same volume of blood now '
                                                                'delivers noticeably less oxygen '
                                                                'per beat, because every courier '
                                                                'in it is carrying a smaller '
                                                                'load.'},
                                                       {'scale': 'The whole body',
                                                        'text': 'Climbing stairs becomes hard '
                                                                'work. Your muscles ask for oxygen '
                                                                'at a rate the blood can no longer '
                                                                'supply, so they respire without '
                                                                'it and ache.'}],
                                             'close': 'It would gain something: with a nucleus it '
                                                      'could repair itself and live far longer '
                                                      'than a hundred and twenty days. The body '
                                                      'has judged that trade and chosen cargo over '
                                                      'lifespan.',
                                             'close_safe': 'It would gain something: with a '
                                                           'nucleus it could repair itself and '
                                                           'live far longer than a hundred and '
                                                           'twenty days. The body has judged that '
                                                           'trade and chosen cargo over '
                                                           'lifespan.'}]},
                               {'specimen': 'root',
                                'options': [{'id': 'short',
                                             'label': 'Shorten the hair',
                                             'what': 'Cut the hair back to a stub, so the cell is '
                                                     'a neat block like its neighbours. Nothing '
                                                     'inside it changes.',
                                             'predict': ['It cannot make food any more',
                                                         'Far less surface is touching soil water',
                                                         'The cell bursts'],
                                             'caption': 'The same cell with the hair cut back to a '
                                                        'stub.',
                                             'alt': 'A root hair cell with only a short stub '
                                                    'instead of a long hair, touching far fewer '
                                                    'soil particles.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'Almost all of this cell’s surface '
                                                                'was on the hair. Cut it off and '
                                                                'the area in contact with soil '
                                                                'water collapses, so far less can '
                                                                'cross the membrane per second.'},
                                                       {'scale': 'The root',
                                                        'text': 'Multiply that by millions of '
                                                                'cells. The root can still absorb, '
                                                                'but at a fraction of the rate — '
                                                                'and it is competing with the soil '
                                                                'itself, which holds water '
                                                                'tightly.'},
                                                       {'scale': 'The whole plant',
                                                        'text': 'The leaves lose water faster than '
                                                                'the root can replace it, so the '
                                                                'vacuoles empty and the plant '
                                                                'wilts. Minerals like nitrate '
                                                                'arrive too slowly to build new '
                                                                'leaves, so growth stops.'}],
                                             'close': 'Surface area is the whole point of this '
                                                      'cell. It is the same idea your lungs and '
                                                      'your small intestine are built on, at a '
                                                      'scale you can see.',
                                             'close_safe': 'Surface area is the whole point of '
                                                           'this cell. It is the same idea your '
                                                           'lungs and your small intestine are '
                                                           'built on, at a scale you can see.'},
                                            {'id': 'mito',
                                             'label': 'Remove the mitochondria',
                                             'what': 'Take out every mitochondrion. The hair, the '
                                                     'wall, the vacuole and the nucleus all stay '
                                                     'exactly as they were.',
                                             'predict': ['Water stops entering',
                                                         'Minerals stop entering, but water keeps '
                                                         'coming',
                                                         'The hair shrivels immediately'],
                                             'caption': 'The same cell with no mitochondria — '
                                                        'minerals no longer crossing in.',
                                             'alt': 'A root hair cell with no mitochondria; water '
                                                    'arrows still enter but mineral arrows have '
                                                    'stopped.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'Water still soaks in on its own, '
                                                                'because it moves from where there '
                                                                'is more to where there is less. '
                                                                'Minerals do not: there is more '
                                                                'nitrate inside the cell than in '
                                                                'the soil, so pulling more in has '
                                                                'to be paid for — and the payment '
                                                                'came from the mitochondria.'},
                                                       {'scale': 'The root',
                                                        'text': 'The plant keeps drinking and '
                                                                'stops feeding. Water goes up the '
                                                                'stem as usual; the dissolved '
                                                                'minerals it should be carrying '
                                                                'are missing.'},
                                                       {'scale': 'The whole plant',
                                                        'text': 'The leaves turn yellow. '
                                                                'Chlorophyll needs nitrogen and '
                                                                'magnesium to build, and neither '
                                                                'is arriving — so the plant is '
                                                                'standing in wet soil, in full '
                                                                'sun, slowly starving.'}],
                                             'close': 'This is the sabotage that separates two '
                                                      'things students often merge: water gets in '
                                                      'for free, minerals have to be bought. '
                                                      'Yellow leaves on a well-watered plant is '
                                                      'the classic sign.',
                                             'close_safe': 'This is the sabotage that separates '
                                                           'two things students often merge: water '
                                                           'gets in for free, minerals have to be '
                                                           'bought. Yellow leaves on a '
                                                           'well-watered plant is the classic '
                                                           'sign.'}]},
                               {'specimen': 'sperm',
                                'options': [{'id': 'notail',
                                             'label': 'Remove the tail',
                                             'what': 'Take the tail off. The head, the nucleus and '
                                                     'every mitochondrion stay untouched.',
                                             'predict': ['It can no longer move',
                                                         'It can no longer carry chromosomes',
                                                         'It runs out of energy faster'],
                                             'caption': 'The same cell with no tail. Everything '
                                                        'else is intact.',
                                             'alt': 'A sperm cell head and midpiece with no tail '
                                                    'attached.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'It has the instructions, the '
                                                                'energy and the enzymes — and no '
                                                                'way to move. A cell this small '
                                                                'cannot drift anywhere useful on '
                                                                'its own.'},
                                                       {'scale': 'The journey',
                                                        'text': 'It never gets near the egg. '
                                                                'Distance, for something this '
                                                                'size, is the hardest part of the '
                                                                'whole job.'},
                                                       {'scale': 'The outcome',
                                                        'text': 'No fertilisation. Every other '
                                                                'adaptation in the cell was in '
                                                                'perfect order and none of them '
                                                                'mattered.'}],
                                             'close': 'This is what a system means. Six things '
                                                      'right and one thing missing is not '
                                                      'five-sixths of a working cell — it is a '
                                                      'cell that fails.',
                                             'close_safe': 'This is what a system means. Six '
                                                           'things right and one thing missing is '
                                                           'not five-sixths of a working cell — it '
                                                           'is a cell that fails.'},
                                            {'id': 'mito',
                                             'label': 'Empty the midpiece',
                                             'what': 'Take out the mitochondria. The tail is still '
                                                     'perfectly formed and attached.',
                                             'predict': ['The tail falls off',
                                                         'The tail can beat, but not for long',
                                                         'The nucleus stops working'],
                                             'caption': 'The same cell with an empty midpiece — '
                                                        'the tail hangs limp.',
                                             'alt': 'A sperm cell with an empty midpiece and a '
                                                    'limp, nearly straight tail.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'A tail is a motor and a motor '
                                                                'needs fuel released. With no '
                                                                'mitochondria there is nothing '
                                                                'turning food into usable energy, '
                                                                'so the tail beats weakly and then '
                                                                'stops.'},
                                                       {'scale': 'The journey',
                                                        'text': 'It covers a fraction of the '
                                                                'distance and stalls. There is no '
                                                                'refuelling on the way — '
                                                                'everything it will ever spend was '
                                                                'loaded before it set off.'},
                                                       {'scale': 'The outcome',
                                                        'text': 'No fertilisation, for the same '
                                                                'reason as before but from the '
                                                                'other end: the machine is intact '
                                                                'and unpowered.'}],
                                             'close': 'Notice the pattern. The tail and the '
                                                      'mitochondria are not two adaptations, they '
                                                      'are one — a structure and its power supply, '
                                                      'useless apart.',
                                             'close_safe': 'Notice the pattern. The tail and the '
                                                           'mitochondria are not two adaptations, '
                                                           'they are one — a structure and its '
                                                           'power supply, useless apart.'}]},
                               {'specimen': 'nerve',
                                'options': [{'id': 'sheath',
                                             'label': 'Strip the fatty sheath',
                                             'what': 'Remove the fatty covering. The cell is the '
                                                     'same length, and every other part is intact.',
                                             'predict': ['The signal cannot start at all',
                                                         'The signal still travels, but much more '
                                                         'slowly',
                                                         'The cell dies'],
                                             'caption': 'The same cell with the sheath stripped '
                                                        'away — bare cable.',
                                             'alt': 'A nerve cell with a bare, unsheathed axon and '
                                                    'no segments.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'With the sheath on, the signal '
                                                                'jumps between the gaps. Bare, it '
                                                                'has to travel the whole length of '
                                                                'the membrane step by step, and it '
                                                                'leaks as it goes.'},
                                                       {'scale': 'The nerve',
                                                        'text': 'The message arrives many times '
                                                                'later, and weaker. Timing between '
                                                                'different nerves goes out of '
                                                                'step, which matters as much as '
                                                                'the delay itself.'},
                                                       {'scale': 'The whole body',
                                                        'text': 'Movement becomes clumsy and slow '
                                                                'to correct, and vision and '
                                                                'balance are affected too, because '
                                                                'those signals depend on arriving '
                                                                'on time.'}],
                                             'close': 'The sheath is what makes a metre-long cell '
                                                      'practical. In multiple sclerosis the body’s '
                                                      'own immune system damages it, and these are '
                                                      'the effects people describe.',
                                             'close_safe': 'The sheath is what makes a metre-long '
                                                           'cell practical. Speed here is not a '
                                                           'bonus; it is the difference between '
                                                           'catching yourself as you trip and '
                                                           'hitting the floor.'},
                                            {'id': 'short',
                                             'label': 'Make it short',
                                             'what': 'Replace the one long cell with a relay of '
                                                     'short ones covering the same distance. Every '
                                                     'cell keeps its sheath and its mitochondria.',
                                             'predict': ['The signal cannot cross the gaps between '
                                                         'cells',
                                                         'Every handover adds a delay, so the '
                                                         'total time goes up',
                                                         'The signal gets stronger with each cell'],
                                             'caption': 'The same distance covered by a relay of '
                                                        'short cells, with junctions between them.',
                                             'alt': 'Three short nerve cells in a row spanning the '
                                                    'same distance, with junction gaps drawn '
                                                    'between them.',
                                             'chain': [{'scale': 'The cell',
                                                        'text': 'Each short cell works perfectly. '
                                                                'But at the end of every one, the '
                                                                'signal has to be handed to the '
                                                                'next across a junction, and that '
                                                                'handover takes chemistry, not '
                                                                'electricity.'},
                                                       {'scale': 'The nerve',
                                                        'text': 'Chemistry across a junction is '
                                                                'slower than a signal running down '
                                                                'a cable. Two extra junctions is '
                                                                'two extra delays; a hundred would '
                                                                'be a hundred.'},
                                                       {'scale': 'The whole body',
                                                        'text': 'A reflex that should take a '
                                                                'fraction of a second takes long '
                                                                'enough to matter. You would still '
                                                                'be deciding to let go of the hot '
                                                                'pan after you had already been '
                                                                'burned.'}],
                                             'close': 'This is why the nerve cell is shaped the '
                                                      'way it is. Length is not a curiosity — it '
                                                      'is the adaptation, and it exists to avoid '
                                                      'handovers.',
                                             'close_safe': 'This is why the nerve cell is shaped '
                                                           'the way it is. Length is not a '
                                                           'curiosity — it is the adaptation, and '
                                                           'it exists to avoid handovers.'}]}],
                 'id': 's-break',
                 'kind': 'sabotage',
                 'demand': 'investigate'}],
 'ladder': {'recall': {'title': 'Rung 1 · Name the job',
                       'q': 'A cell is long and thin, has a wall and a vacuole, no chloroplasts, '
                            'and an unusually large number of mitochondria. What is it built for?',
                       'options': ['Carrying oxygen round the body',
                                   'Trapping light to make food',
                                   'Absorbing water and minerals from soil',
                                   'Carrying a signal from your spine to your toe'],
                       'answer': 2,
                       'feedback': {0: 'That cell has no wall and no vacuole — and no mitochondria '
                                       'at all, so that it does not use the oxygen it carries.',
                                    1: 'Then it would be full of chloroplasts. This one has none, '
                                       'which is the clue that no light reaches it.',
                                    3: 'A nerve cell is an animal cell. No animal cell has a wall '
                                       'or a permanent vacuole.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A student says a red blood cell is not really a cell, because it has '
                           'no nucleus. What is the best reply?',
                      'options': ['Every cell in your body keeps its nucleus, so anything without '
                                  'one is a fragment rather than a cell',
                                  'A red blood cell keeps its nucleus all its life, and it is only '
                                  'too small to see under a school microscope',
                                  'It started with a nucleus and destroyed it as it matured, which '
                                  'is why it cannot repair itself and lasts about 120 days',
                                  'A cell can switch its nucleus off when it is not needed, and '
                                  'switch it back on when it is'],
                      'answer': 2,
                      'feedback': {0: 'It has a membrane and cytoplasm and it does a job for four '
                                      'months. Having no nucleus is a cost it paid, not proof it '
                                      'was never a cell.',
                                   1: 'It genuinely has none. This is not a limit of the '
                                      'microscope — the nucleus is pushed out and destroyed while '
                                      'the cell matures.',
                                   3: 'A switched-off nucleus would still take up the space. The '
                                      'whole point of losing it is the room that the haemoglobin '
                                      'then fills.'}},
            'explain': {'title': 'Rung 3 · Explain it',
                        'q': 'A root hair cell is drawn out into a long thin hair. Explain how '
                             'that shape helps the whole plant, and why a rounder cell of the same '
                             'volume would be worse.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The long thin shape means…',
                        'success': ['Says the long thin shape gives a much larger surface area '
                                    'than a round cell of the same volume.',
                                    'Says water and dissolved minerals can only enter through the '
                                    'surface, so more surface means a faster rate of absorption.',
                                    'Says the hair reaches in between soil particles, where the '
                                    'water actually is.',
                                    'Connects it to the whole plant: enough water to stay firm and '
                                    'enough minerals to keep growing.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'Design a cell whose job is to line the inside of your windpipe and '
                             'stop dust reaching your lungs. Say which of the seven parts you '
                             'would turn up, what shape you would give the cell, and what would go '
                             'wrong in the whole body if that shape stopped working. You may '
                             'invent a structure — but say which problem it solves.',
                        'field_label': 'Your design',
                        'placeholder': 'Shape: … Turned up: … If it failed: …',
                        'success': ['Gives the cell something on its exposed surface that can move '
                                    'dust along — a fringe of hair-like structures, or your own '
                                    'equivalent, with a reason.',
                                    'Turns up mitochondria, because constant sweeping is constant '
                                    'work.',
                                    'Says the surface facing the airway is the one that matters, '
                                    'and the cells sit in a sheet so they can sweep together in '
                                    'one direction.',
                                    'Follows a failure out to the whole body: dust and mucus stay '
                                    'in the airway instead of being cleared, so infections take '
                                    'hold.']},
            'retry_note': 'Clears the ticks on rungs 3 and 4 and keeps what you wrote.',
            'sub': 'Four rungs. Two the page marks, two you mark.'},
 'key_note': 'A specialised cell is not built from different parts. It is the same seven, tuned — '
             'more of one, none of another, and a shape that answers one physical problem.',
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
