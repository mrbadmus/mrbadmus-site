# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `absorption-and-the-small-intestine` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'absorption-and-the-small-intestine'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'absorption-and-the-small-intestine',
 'title': 'Absorption and the small intestine',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'MODEL',
 'covers': ['KS3.B.NUT.04c'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'structure-function', 'level': 3}, {'id': 'cells-and-systems', 'level': 2}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': [],
 'assumes': [],
 'references': ['bacteria-in-the-gut',
                {'unit': 'C1', 'lesson': 'diffusion'},
                {'unit': 'B4', 'lesson': 'alveoli-built-for-exchange'}],
 'ks4_links': [],
 'ks4_becomes': 'Exchange surfaces and the surface area to volume ratio, plus active transport of '
                'glucose against a gradient.',
 'big_question': 'How can a tube the size of a garden hose absorb a whole meal?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Hose and gut', 'done_when': 'committed'},
          {'anchor': 's-fold',
           'short': 'FOLD',
           'label': 'Build the surface',
           'done_when': 'all_three_levels_on'},
          {'anchor': 's-four',
           'short': 'FOUR',
           'label': 'Four features',
           'mirrors': 's-fold',
           'done_when': 'all_three_levels_on'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A garden hose six metres long, and your small intestine. Same length.',
                'prompt': 'Both about six metres. Both about two and a half centimetres across. '
                          'The hose has roughly half a square metre of inner surface — the area of '
                          'a tea towel. Your small intestine has about thirty square metres, '
                          'roughly a third of a badminton court.',
                'commit': 'If you had to guess, how does the intestine get sixty times the surface '
                          'of a hose?',
                'options': ['It is coiled up', 'Its wall is folded'],
                'reveal': 'Next: switch on each level of folding and watch the absorbing surface '
                          'grow.',
                'guess': True,
                'replies': ['The gut is packed in tight. But coiling a tube does not change its '
                            'inside surface. The wall itself has to be folded.',
                            'Folded, and then folded again. Folds with bumps on them, and tinier '
                            'bumps on those, give far more surface than a plain tube of the same '
                            'size.'],
                'answer': 1},
 'misconceptions': [{'id': 'DIET-15',
                     'statement': 'Villi make the intestine longer.',
                     'elicited_by': 'fold-builder',
                     'confronted_by': 'villi-and-length'},
                    {'id': 'DIET-16',
                     'statement': 'The muscles push the food through the gut wall into the blood.',
                     'elicited_by': 'villi-and-length',
                     'confronted_by': 'villi-and-length'}],
 'vocabulary': [{'term': 'absorption',
                 'definition': 'The movement of small, soluble molecules out of the gut and into '
                               'the blood.',
                 'note': None},
                {'term': 'villus',
                 'definition': 'One of the millions of finger-shaped projections that line the '
                               'small intestine.',
                 'note': 'One villus, many villi. Each one has capillaries inside it and a wall a '
                         'single cell thick.'},
                {'term': 'microvilli',
                 'definition': 'The hundreds of tiny projections on the outer surface of each cell '
                               'covering a villus.',
                 'note': None},
                {'term': 'surface area',
                 'definition': 'The total area of a surface. Folding increases it without changing '
                               'length or width.',
                 'note': None}],
 'figures': [{'id': 'b3-villus-labelled',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'villus',
              'title': 'Three scales of folding in the small intestine, and one villus cut through',
              'desc': 'Three framed drawings across the top, each a magnified callout of the one '
                      'before it. The first shows a length of the small intestine as a tube, cut '
                      'open at the near end, its inner wall thrown into ring-shaped ridges rather '
                      'than being smooth. A callout from one ridge opens into the second frame, '
                      'where the surface of that single ridge is covered in upright finger-shaped '
                      'villi. A callout from one villus opens into the third frame, where the '
                      'surface of a single villus cell is covered in far smaller projections, the '
                      'microvilli. A second callout from the same row of villi opens downward into '
                      'a wide panel beneath, showing one villus cut lengthways. Its wall is drawn '
                      'as a single row of cells, divided by cross lines so the count can be '
                      'checked, and inside the villus a capillary runs up to the tip and back. '
                      'Three arrows cross the wall from the gut into the capillary, labelled '
                      'glucose, amino acids and fatty acids.',
              'caption': 'Each frame is drawn from a callout of the frame before it, so the '
                         'folding is one thing at three sizes rather than three separate facts: '
                         'the tube is ridged, every ridge is covered in villi, and every cell of '
                         'every villus is covered in microvilli. The panel underneath shows why it '
                         'is worth doing. Count the cells across the wall of the villus — there is '
                         'one. On the far side of that single cell is a capillary, which is why a '
                         'glucose molecule in the gut is in the bloodstream a moment later.'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'fold-builder', 'anchor': 's-fold'},
          {'type': 'rule',
           'anchor': 's-four',
           'eyebrow': 'What a good exchange surface needs',
           'statement': 'Area is only one of four, and the villus has all four.',
           'cards': [{'term': 'Feature 1 · Very large surface area',
                      'gloss': 'Three levels of folding bring roughly 30 m² of absorbing surface '
                               'into a tube six metres long. <strong>Remove it and:</strong> A '
                               'plain tube of the same size absorbs about a sixtieth as fast. A '
                               'meal would pass through largely unabsorbed.'},
                     {'term': 'Feature 2 · Wall one cell thick',
                      'gloss': 'The distance from the gut contents to the blood inside a villus is '
                               'a single cell — the shortest diffusion path the body can build. '
                               '<strong>Remove it and:</strong> Diffusion slows sharply as the '
                               'distance grows. A wall ten cells thick would be a tenth as fast '
                               'for the same area.'},
                     {'term': 'Feature 3 · Dense blood supply',
                      'gloss': 'A capillary network runs through every villus, carrying absorbed '
                               'molecules away as fast as they arrive. <strong>Remove it '
                               'and:</strong> The blood side fills up, the concentration '
                               'difference disappears, and diffusion stops — with the surface and '
                               'the thin wall entirely intact.'},
                     {'term': 'Feature 4 · Moist surface',
                      'gloss': 'Everything is in solution. Molecules can only diffuse through a '
                               'membrane dissolved in water. <strong>Remove it and:</strong> A dry '
                               'surface absorbs nothing at all. This is why every exchange surface '
                               'in every organism is wet.'}]},
          {'type': 'key-fact', 'ref': 'diffusion-not-a-push'},
          {'type': 'figure', 'ref': 'b3-villus-labelled', 'anchor': 's-folds'},
          {'type': 'misconception',
           'id': 'villi-and-length',
           'anchor': 's-think',
           'targets': ['DIET-15', 'DIET-16']},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'diffusion-not-a-push',
                'text': 'Small soluble molecules cross the villus wall by diffusion, from high '
                        'concentration in the gut to low concentration in the blood. Nothing '
                        'pushes them. The blood supply keeps the concentration low on its side, '
                        'which is what keeps the diffusion going.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'villi-and-length',
                 'kind': 'confrontation',
                 'demand': 'confront both length errors in one pass: the geometric one and the '
                           'mechanical one',
                 'targets': ['DIET-15', 'DIET-16'],
                 'statements': [{'quote': 'Villi make the intestine longer.',
                                 'answer': 'They do not add a millimetre of length. Every figure '
                                           'in this lesson holds the length fixed at six metres — '
                                           'that is the point of the comparison with the hose. '
                                           'Villi are projections into the space the tube already '
                                           'has, so they add <em>surface</em> without adding '
                                           '<em>length</em>, which is a distinction worth getting '
                                           'straight because it is the same distinction that makes '
                                           'lungs, gills and leaves work. If lengthening were the '
                                           'strategy, evolution would have taken it: a sixty-metre '
                                           'intestine would need a sixty-metre animal to put it '
                                           'in, and folding gets the same area into the abdomen '
                                           'you already have.'},
                                {'quote': 'The muscles push the food through the gut wall into the '
                                          'blood.',
                                 'answer': 'Peristalsis moves food <em>along</em> the tube; it '
                                           'never moves anything <em>through</em> the wall. '
                                           'Absorption is diffusion — the same process you met in '
                                           'Diffusion, doing biological work here. Glucose '
                                           'molecules are moving randomly in all directions all '
                                           'the time, and there are more of them in the gut than '
                                           'in the blood, so more happen to cross inwards than '
                                           'outwards. Nothing pushes them, nothing wants to '
                                           'spread, and no muscle is involved. What the body does '
                                           'is keep the numbers unequal: blood flows past '
                                           'constantly, carrying absorbed glucose away, so the '
                                           'concentration on the blood side stays low and the net '
                                           'movement continues. Stop the blood flow and absorption '
                                           'stops within minutes — not because the pushing '
                                           'stopped, but because the difference did.'}]},
                {'demand': 'investigate',
                 'targets': 'DIET-15',
                 'eyebrow': 'Build the surface · three levels',
                 'heading': 'Switch each level on and watch the area',
                 'head_counter': {'format': '{n} of 3 levels on', 'total': 3, 'start': 0},
                 'prompt': 'Start with a plain tube and add the folds one level at a time. The '
                           'length never changes.',
                 'base_area': 0.5,
                 'levels': [{'id': 'folds',
                             'name': 'Level 1 · Circular folds',
                             'factor': 3,
                             'scale': 'Visible without a microscope — ridges a few millimetres '
                                      'deep',
                             'what': 'The whole wall is thrown into ridges running round the tube, '
                                     'like the inside of a concertina. Nothing is added; the same '
                                     'sheet is corrugated.'},
                            {'id': 'villi',
                             'name': 'Level 2 · Villi',
                             'factor': 5,
                             'scale': 'About 1 mm long — visible with a hand lens, like velvet',
                             'what': 'Every square millimetre of that folded wall carries '
                                     'thousands of finger-shaped projections. Each villus has a '
                                     'network of capillaries inside it and a wall one cell thick.'},
                            {'id': 'microvilli',
                             'name': 'Level 3 · Microvilli',
                             'factor': 4,
                             'scale': 'About 0.001 mm — needs an electron microscope',
                             'what': 'Each cell covering a villus has its own outer surface thrown '
                                     'into hundreds of tiny projections. Folds on folds on folds — '
                                     'the third and last level.'}],
                 'notes': ['A plain tube. Half a square metre — about a tea towel. A meal would be '
                           'through you long before much of it crossed the wall.',
                           'Corrugating the wall triples it — one and a half square metres. Still '
                           'nothing like enough, and this is the only level you could see with the '
                           'naked eye.',
                           'Villi are where most of the gain comes from. Seven and a half square '
                           'metres of absorbing surface, in a tube you could coil in your hands.',
                           'About 30 m² — roughly a third of a badminton court, and sixty times '
                           'the plain tube. The length is still six metres.'],
                 'set_notes': {'villi': 'Villi alone multiply it by five — two and a half square '
                                        'metres. This is the level that gives the most, and here '
                                        'it is doing it on a wall nobody has corrugated.',
                               'microvilli': 'Microvilli alone multiply it by four — two square '
                                             'metres. Every one of them sits on a cell surface you '
                                             'would need an electron microscope to see.',
                               'folds+microvilli': 'Twelve times the plain tube, six square metres '
                                                   '— with the middle level missing. Leaving the '
                                                   'villi out costs more than leaving out either '
                                                   'of the others.',
                               'villi+microvilli': 'Twenty times the plain tube: ten square metres '
                                                   'of velvet, on a wall that was never '
                                                   'corrugated.'},
                 'readout_label': 'Absorbing surface',
                 'area_format': '{a} m²',
                 'multiple_format': 'Compared with the plain tube: ×{x}',
                 'labels': {'off': 'Add this level', 'on': 'On · ×{factor}'},
                 'id': 'fold-builder',
                 'kind': 'fold-builder'}],
 'ladder': {'recall': {'title': 'Rung 1 · What the folding does',
                       'q': 'Villi increase the small intestine’s…',
                       'options': ['length', 'volume', 'surface area', 'muscle strength'],
                       'answer': 2,
                       'feedback': {0: 'Villi do not add any length. They add surface area.',
                                    1: 'Villi do not add volume. They give a bigger surface for '
                                       'absorbing food.',
                                    3: 'Villi do not make muscles stronger. They give a bigger '
                                       'surface for absorbing food.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A villus keeps its full surface area and its thin wall. But its blood '
                           'supply is blocked. What happens to absorption there?',
                      'options': ['It carries on as normal, as the surface and thin wall are '
                                  'intact',
                                  'It reverses, as glucose is pushed back out of the blood into '
                                  'the gut',
                                  'It speeds up, as nothing is carrying the molecules away',
                                  'It slows and stops, as the concentration difference disappears'],
                      'answer': 3,
                      'feedback': {0: 'Diffusion needs a concentration difference. Without blood '
                                      'flow, that difference disappears.',
                                   1: 'Nothing pushes glucose back. Once both sides are equal, it '
                                      'stops moving across overall.',
                                   2: 'Blood carrying glucose away keeps absorption going. Without '
                                      'it, absorption stops.'}},
            'explain': {'title': 'Rung 3 · Explain the whole design',
                        'q': 'Explain how three levels of folding, a wall one cell thick and a '
                             'dense blood supply work together to absorb a meal in a few hours. '
                             'Say what each contributes, and why no one of them would be enough '
                             'alone.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The folding contributes… the thin wall… the blood supply…',
                        'success': ['Says the folding gives a very large surface area, so many '
                                    'molecules can cross at once.',
                                    'Says the one-cell wall gives a short diffusion distance, so '
                                    'each crossing is fast.',
                                    'Says the blood supply removes absorbed molecules and so '
                                    'maintains the concentration difference.',
                                    'Names diffusion as the process, and says it happens because '
                                    'of a concentration difference rather than a push.',
                                    'Explains why one alone is not enough — e.g. a huge area with '
                                    'no blood flow still stops once the two sides equalise.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'In coeliac disease, an immune reaction to gluten flattens the villi. '
                             'Predict what a patient would experience, explain it using this '
                             'lesson, and say why they might be short of iron even while eating '
                             'plenty of it.',
                        'field_label': 'Your answer',
                        'placeholder': 'Flattened villi would mean…',
                        'success': ['Predicts poor absorption and consequences such as mass loss, '
                                    'tiredness, or poor growth.',
                                    'Explains it as a loss of surface area — the folding is gone, '
                                    'so far fewer molecules can cross.',
                                    'Says iron is eaten but not absorbed, so it never reaches the '
                                    'blood.',
                                    'Connects this to the earlier lesson: a deficiency with an '
                                    'adequate diet, caused by the gut rather than the plate.']}},
 'key_note': 'The small intestine is adapted for absorption by a very large surface area — folds, '
             'villi and microvilli — a wall one cell thick, and a dense blood supply that '
             'maintains the concentration difference. Small soluble molecules cross by diffusion. '
             'Water is absorbed here and in the large intestine.',
 'stretch': [],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to work through why blood flow keeps diffusion going?',
           'cta': 'Ask about this lesson',
           'anchor': 's-four'},
 'convention_note': 'Area figures are approximate and follow the 2014 fresh-tissue measurements.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
