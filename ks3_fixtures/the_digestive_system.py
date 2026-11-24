# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `the-digestive-system` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'the-digestive-system'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'the-digestive-system',
 'title': 'The digestive system',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'SYSTEM',
 'covers': ['KS3.B.NUT.04a'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 2}, {'id': 'structure-function', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 40,
 'requires': [],
 'assumes': [],
 'references': ['enzymes-in-digestion',
                {'unit': 'B1', 'lesson': 'levels-of-organisation'},
                'absorption-and-the-small-intestine'],
 'ks4_links': [],
 'ks4_becomes': 'The digestive system as an organ system, with named enzymes, bile, and the role '
                'of the liver in metabolism.',
 'big_question': 'A nine-metre tube with seven jobs along it. Food spends a few hours in the organ '
                 'everybody names, a few more in the one that actually does the work — and longest '
                 'of all in the one that only takes back water.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The blender', 'done_when': 'committed'},
          {'anchor': 's-journey',
           'short': 'JOURNEY',
           'label': 'Seven stops',
           'done_when': 'all_seven_stops_visited'},
          {'anchor': 's-two',
           'short': 'BREAK',
           'label': 'Two kinds',
           'mirrors': 's-journey',
           'done_when': 'all_seven_stops_visited'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Blend a meal to a smooth liquid. Is it digested?',
                'prompt': 'A cheese sandwich goes into a blender for two minutes on high. What '
                          'comes out is a smooth grey liquid with no lumps in it at all — smoother '
                          'than anything your teeth or stomach could manage.',
                'commit': 'If you had to guess, could that smooth liquid go straight into your '
                          'blood?',
                'options': ['Yes, it is smooth enough', 'No, it is not broken down enough'],
                'reveal': 'Digestion has to cut the molecules themselves, and enzymes do that. '
                          'Next: follow a sandwich through seven stops of the gut.',
                'guess': True,
                'replies': ['Smooth does feel finished. But blades only make the pieces smaller. '
                            'The starch inside is still in long chains, far too big to cross into '
                            'your blood.',
                            'Smooth is not the same as small enough. The starch in the liquid is '
                            'still in long chains, far too big to cross into your blood.'],
                'answer': 1},
 'misconceptions': [{'id': 'DIET-11',
                     'statement': 'Digestion is food being squashed into smaller and smaller '
                                  'pieces.',
                     'elicited_by': 'two-wrong-ideas',
                     'confronted_by': 'two-wrong-ideas'},
                    {'id': 'DIET-12',
                     'statement': 'Food sits in your stomach until it is digested, then goes to '
                                  'the intestine.',
                     'elicited_by': 'two-wrong-ideas',
                     'confronted_by': 'two-wrong-ideas'}],
 'vocabulary': [{'term': 'digestion',
                 'definition': 'Breaking large insoluble food molecules into small soluble ones '
                               'that can be absorbed.',
                 'note': None},
                {'term': 'mechanical digestion',
                 'definition': 'Breaking food into smaller pieces without changing the molecules.',
                 'note': 'Its whole purpose is to expose more surface for the chemical kind.'},
                {'term': 'chemical digestion',
                 'definition': 'Cutting the long food molecules into short ones, which only '
                               'enzymes can do.',
                 'note': None},
                {'term': 'peristalsis',
                 'definition': 'The wave of muscle contraction that squeezes food along the gut.',
                 'note': 'It does not need gravity — you can swallow upside down.'},
                {'term': 'egestion',
                 'definition': 'Removing material that passed through the gut and was never '
                               'absorbed.',
                 'note': 'Not the same as excretion, which is getting rid of waste your own cells '
                         'produced.'}],
 'figures': [{'id': 'b3-gut-labelled',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'gut-tube',
              'title': 'The digestive system: one continuous coiled tube with seven stops',
              'desc': 'A wide framed drawing above a key of seven stops. In the drawing, one tube '
                      'runs from the top of the frame to the bottom with an orange line down the '
                      'middle of it that is a single unbroken path from beginning to end. From the '
                      'top: 01, the mouth, at the top of a straight narrow run. 02, the '
                      'oesophagus, that run. 03, the stomach, drawn as a bag whose muscular wall '
                      'bulges out to the right, open at the top where the oesophagus enters and '
                      'open at the lower left where the tube leaves; the orange line curves '
                      'through the inside of the bag. 04, the small intestine, a narrow tube in '
                      'six tight coils across the middle of the frame, noted as six to seven '
                      'metres of narrow tube, coiled. 06, the large intestine, below it, drawn '
                      'distinctly wider and shorter. 07, the rectum and anus, at the bottom. On '
                      'the left of the frame, well clear of the tube, a dashed boundary encloses '
                      'stop 05: the liver as a large wedge, the gall bladder as a small pear below '
                      'it, and the pancreas as a tapering shape below that. Ducts leave those '
                      'three, join into one, and run right to meet the tube just after the '
                      'stomach. The orange line does not enter the dashed boundary at any point. '
                      'The key reads: 01 mouth, chewed and mixed with saliva. 02 oesophagus, '
                      'squeezed down by muscle, nothing is broken here. 03 stomach, churned in '
                      'acid, protein begins. 04 small intestine, every nutrient finished, and '
                      'almost all absorption. 05 pancreas, liver and gall bladder, juices in and '
                      'no food passes through, its badge dashed because it is off the tube. 06 '
                      'large intestine, water absorbed, the nutrients have already gone. 07 rectum '
                      'and anus, stored then out, material that was never absorbed.',
              'caption': 'One tube, from 01 at the top to 07 at the bottom, with the orange line '
                         'running down the middle of it the whole way. The small intestine is the '
                         'long narrow coiled run; the large intestine below it is visibly wider '
                         'and shorter. Stop 05 — pancreas, liver and gall bladder — sits inside '
                         'the dashed boundary, with ducts leading out of it into the tube. That is '
                         'the distinction the bench’s own stop 05 rests on: those three send '
                         'juices in, and food never passes through them. Put a finger on 01 and '
                         'follow the orange line down: it does not stop, branch or start again '
                         'anywhere between there and 07, and it never once goes into the dashed '
                         'boundary.'},
             {'id': 'b3-digestion-timing',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'digestion-timing-bars',
              'title': 'A bar chart of how long a meal spends in each part of the digestive system',
              'desc': 'A bar chart with six bars, one per organ in the order food travels: mouth, '
                      'oesophagus, stomach, small intestine, large intestine, rectum and anus. The '
                      'mouth and oesophagus bars are both drawn as thin slivers, labelled under 1 '
                      "hour. The stomach's bar reaches 3 hours and the small intestine's 4 hours. "
                      "The large intestine's bar is by far the tallest, reaching 30 hours, and the "
                      "rectum's bar reaches 6 hours.",
              'caption': 'Hours spent in each organ, to scale.',
              'data': {'organs': [{'id': 'mouth',
                                   'label': 'Mouth',
                                   'hours': 0.02,
                                   'display': '<1 h'},
                                  {'id': 'oesophagus',
                                   'label': 'Oesophagus',
                                   'hours': 0.003,
                                   'display': '<1 h'},
                                  {'id': 'stomach',
                                   'label': 'Stomach',
                                   'hours': 3,
                                   'display': '3 h'},
                                  {'id': 'smallint',
                                   'label': 'Small intestine',
                                   'hours': 4,
                                   'display': '4 h'},
                                  {'id': 'largeint',
                                   'label': 'Large intestine',
                                   'hours': 30,
                                   'display': '30 h'},
                                  {'id': 'rectum',
                                   'label': 'Rectum and anus',
                                   'hours': 6,
                                   'display': '6 h'}],
                       'y_unit': 'hours'}}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'seven-stops', 'anchor': 's-journey'},
          {'type': 'rule',
           'anchor': 's-two',
           'eyebrow': 'Two kinds of breaking',
           'statement': 'Smaller pieces is not smaller molecules.',
           'cards': [{'term': 'Mechanical digestion · Making pieces smaller',
                      'gloss': 'Teeth cutting and grinding, the stomach churning, bile splitting '
                               'fat droplets. The chemical nature of the food does not change at '
                               'all — starch is still starch afterwards. <strong>Does it let food '
                               'into the blood?</strong> No. A crumb of bread a thousand times '
                               'smaller is still made of the same molecules, and they are still '
                               'too large to cross a membrane.'},
                     {'term': 'Chemical digestion · Making molecules smaller',
                      'gloss': 'Enzymes cut the long chains at each link: starch to glucose, '
                               'protein to amino acids, lipid to fatty acids and glycerol. This is '
                               'a chemical change and the products are different substances from '
                               'what went in. <strong>Does it let food into the blood?</strong> '
                               'Yes. This is the only process that produces molecules small enough '
                               'and soluble enough to be absorbed — which is why enzymes, not '
                               'teeth, are the point of the system.'}]},
          {'type': 'key-fact', 'ref': 'digestion-is-chemical'},
          {'type': 'figure', 'ref': 'b3-gut-labelled', 'anchor': 's-tube'},
          {'type': 'figure', 'ref': 'b3-digestion-timing', 'anchor': 's-digestion-timing'},
          {'type': 'misconception',
           'id': 'two-wrong-ideas',
           'anchor': 's-think',
           'targets': 'DIET-11'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'digestion-is-chemical',
                'text': 'Digestion is the breaking of large insoluble molecules into small soluble '
                        'ones. Chewing and churning only increase surface area so the enzymes can '
                        'work faster — they digest nothing on their own.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'two-wrong-ideas',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'DIET-11',
                 'statements': [{'quote': 'Digestion is food being squashed into smaller and '
                                          'smaller pieces.',
                                 'body': ['If that were true, the blender in the hook would have '
                                          'done the whole job. Follow the sizes instead. A starch '
                                          'molecule in bread is a chain of a few thousand glucose '
                                          'units; a glucose unit is about 0.0000009 mm across, and '
                                          'that is about the size limit for a molecule crossing a '
                                          'cell membrane. Cutting the bread into a million crumbs '
                                          'leaves every starch molecule exactly as long as it was '
                                          '— you have made more, smaller pieces of the same '
                                          'molecule. What has to happen is that the chain is cut '
                                          'chemically at each link, and only an enzyme does that. '
                                          'The word for what your teeth do is <em>mechanical '
                                          'digestion</em>, and its entire purpose is to expose '
                                          'more surface for the chemical kind.']},
                                {'quote': 'Food sits in your stomach until it is digested, then '
                                          'goes to the intestine.',
                                 'body': ['The stomach is not the destination — it is a holding '
                                          'tank with an acid bath and a strong set of muscles. It '
                                          'holds a meal for two to four hours, kills most of the '
                                          'bacteria that came in with it, starts protein '
                                          'digestion, and releases the result into the small '
                                          'intestine a little at a time. Almost nothing is '
                                          'absorbed through the stomach wall: no glucose, no amino '
                                          'acids, no fatty acids. If your stomach were removed — '
                                          'and people do live without one — you could still digest '
                                          'and absorb a meal, because the organ that does the real '
                                          'work is the next one along.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'Follow the meal · seven stops',
                 'heading': 'Where the sandwich actually goes',
                 'head_counter': {'format': '{n} of 7 stops visited', 'total': 7, 'start': 1},
                 'tile_labels': {'time': 'Time spent here',
                                 'breaks': 'Molecules broken here',
                                 'absorbs': 'Absorbed here'},
                 'note_label': 'Worth knowing:',
                 'stops': [{'id': 'mouth',
                            'label': 'Mouth',
                            'name': 'Mouth',
                            'kind': 'Mechanical and chemical',
                            'hours': 0.02,
                            'time': 'about 1 minute',
                            'chart_name': 'Mouth',
                            'chart_hours': '<1 h',
                            'breaks': 'Starch, a little',
                            'absorbs': 'Nothing',
                            'what': 'Teeth cut and grind the food into a soft mass, and the tongue '
                                    'mixes it with saliva. Saliva does two jobs: it lubricates the '
                                    'mass so it can be swallowed, and it contains amylase, which '
                                    'starts cutting starch chains into shorter ones.',
                            'note': 'Hold a plain cracker on your tongue without chewing and it '
                                    'turns faintly sweet in about ninety seconds. That is amylase '
                                    'producing sugar from starch, and it is the only digestion you '
                                    'can taste happening.'},
                           {'id': 'oesophagus',
                            'label': 'Oesophagus',
                            'name': 'Oesophagus',
                            'kind': 'Transport only',
                            'hours': 0.003,
                            'time': 'about 8 seconds',
                            'chart_name': 'Oesophagus',
                            'chart_hours': '<1 h',
                            'breaks': 'Nothing',
                            'absorbs': 'Nothing',
                            'what': 'A muscular tube from throat to stomach. Rings of muscle '
                                    'contract behind the food and relax in front of it, squeezing '
                                    'it along. This wave is called peristalsis and it happens the '
                                    'whole length of the gut.',
                            'note': 'Peristalsis does not need gravity. An astronaut can swallow '
                                    'upside down in orbit, and so can you — the muscle wave, not '
                                    'the fall, moves the food.'},
                           {'id': 'stomach',
                            'label': 'Stomach',
                            'name': 'Stomach',
                            'kind': 'Mechanical and chemical',
                            'hours': 3,
                            'time': '2 to 4 hours',
                            'chart_name': 'Stomach',
                            'chart_hours': '3 h',
                            'breaks': 'Protein',
                            'absorbs': 'Almost nothing',
                            'what': 'A muscular bag that churns the food, adds hydrochloric acid '
                                    'at about pH 2, and adds the enzyme protease to begin breaking '
                                    'protein into shorter chains. The acid also kills most '
                                    'bacteria swallowed with the meal.',
                            'note': 'The acid is strong enough to dissolve the stomach itself, '
                                    'which is why the lining secretes a layer of mucus and '
                                    'replaces its own cells every few days. Ulcers are what '
                                    'happens when that defence fails — usually because of a '
                                    'bacterium, not because of stress or spicy food.'},
                           {'id': 'smallint',
                            'label': 'Small intestine',
                            'name': 'Small intestine',
                            'kind': 'Chemical, then absorption',
                            'hours': 4,
                            'time': 'about 4 hours (2 to 6)',
                            'chart_name': 'Small intestine',
                            'chart_hours': '4 h',
                            'breaks': 'Starch, protein and lipid — all of them, to completion',
                            'absorbs': 'Almost everything',
                            'what': 'Six or seven metres of narrow tube, and the organ that does '
                                    'most of the work. Enzymes from the pancreas and from the '
                                    'intestine wall finish breaking every nutrient down to '
                                    'molecules small enough to cross a membrane, and those '
                                    'molecules are then absorbed into the blood through the '
                                    'intestine wall.',
                            'note': 'Its surface is folded, then covered in villi, then each '
                                    'villus cell is covered in microvilli — three levels of '
                                    'folding that bring the absorbing surface to around 30 m². '
                                    'That is the next lesson’s subject and it is the single best '
                                    'piece of engineering in the body.'},
                           {'id': 'pancreas',
                            'label': 'Pancreas, liver, gall bladder',
                            'name': 'Pancreas, liver and gall bladder',
                            'kind': 'Secretion — no food passes through',
                            'hours': 0,
                            'time': 'no food enters these',
                            'chart_name': 'Pancreas',
                            'chart_hours': '—',
                            'breaks': 'They supply what does the breaking',
                            'absorbs': 'Nothing',
                            'what': 'These three feed into the small intestine without ever '
                                    'holding food. The pancreas supplies amylase, protease and '
                                    'lipase together with an alkali that neutralises the stomach '
                                    'acid. The liver makes bile; the gall bladder stores it and '
                                    'releases it onto fatty food.',
                            'note': 'Bile is not an enzyme and digests nothing. It breaks large '
                                    'fat droplets into many small ones — emulsification — which is '
                                    'mechanical digestion happening chemically, and it multiplies '
                                    'the surface available to lipase enormously.'},
                           {'id': 'largeint',
                            'label': 'Large intestine',
                            'name': 'Large intestine',
                            'kind': 'Absorption of water',
                            'hours': 30,
                            'time': 'a day or more — about 30 hours',
                            'chart_name': 'Large intestine',
                            'chart_hours': '30 h',
                            'breaks': 'Nothing your enzymes can break',
                            'absorbs': 'Water, some minerals and some vitamins',
                            'what': 'Wider and shorter than the small intestine. By the time '
                                    'material arrives, the nutrients have gone; what is left is '
                                    'water, fibre and bacteria. The wall absorbs most of the water '
                                    'back, leaving a solid mass.',
                            'note': 'This is where the trillions of gut bacteria live, and they '
                                    'digest some of the fibre your own enzymes cannot touch — '
                                    'releasing fatty acids and making vitamin K and some B '
                                    'vitamins as by-products. That is lesson eight.'},
                           {'id': 'rectum',
                            'label': 'Rectum and anus',
                            'name': 'Rectum and anus',
                            'kind': 'Storage and egestion',
                            'hours': 6,
                            'time': 'a few hours',
                            'chart_name': 'Rectum and anus',
                            'chart_hours': '6 h',
                            'breaks': 'Nothing',
                            'absorbs': 'Nothing',
                            'what': 'The remaining solid material is stored in the rectum and '
                                    'leaves through the anus. This is egestion — the removal of '
                                    'material that was never absorbed.',
                            'note': 'Egestion is not excretion, and examiners care about the '
                                    'difference. Excretion is getting rid of waste your own cells '
                                    'produced, such as urea and carbon dioxide. Egestion is '
                                    'getting rid of what you never took in.'}],
                 'chart': {'label': 'Hours spent in each organ, to scale',
                           'close': 'The stomach is the organ everyone names first, and it holds '
                                    'the meal for two to four hours. The small intestine holds it '
                                    'for only about four more, yet that is where nearly all '
                                    'digestion is completed and nearly all absorption happens. The '
                                    'longest stay, a day or more, is in the large intestine, which '
                                    'only takes back water. Time spent is not work done.'},
                 'id': 'seven-stops',
                 'kind': 'gut-journey'}],
 'ladder': {'recall': {'title': 'Rung 1 · Where does the work happen',
                       'q': 'In which organ is most food digested and most food absorbed?',
                       'options': ['The stomach',
                                   'The small intestine',
                                   'The large intestine',
                                   'The mouth'],
                       'answer': 1,
                       'feedback': {0: 'The stomach starts protein digestion. Almost nothing is '
                                       'absorbed there.',
                                    2: 'Most food is digested and absorbed before it gets there. '
                                       'It absorbs water.',
                                    3: 'The mouth starts digesting starch. Food is only there for '
                                       'about a minute.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A patient has their gall bladder removed and is advised to avoid very '
                           'fatty meals. Bile contains no enzymes. Why does losing bile storage '
                           'make fat harder to digest?',
                      'options': ['Bile digests the fat itself, so without bile no fat is broken '
                                  'down',
                                  'Bile breaks fat into small droplets, so lipase has more surface',
                                  'Bile adds lipase to the gut, so without it no lipase arrives',
                                  'Without a gall bladder the liver stops making bile, so no fat '
                                  'is digested'],
                      'answer': 1,
                      'feedback': {0: 'Bile has no enzymes, so it digests nothing. Lipase digests '
                                      'the fat.',
                                   2: 'Lipase comes from the pancreas. Bile has no enzymes in it.',
                                   3: 'The liver keeps making bile. Only the store of bile is '
                                      'lost.'}},
            'explain': {'title': 'Rung 3 · Explain the blender',
                        'q': 'A student argues that if you blended a meal finely enough, you would '
                             'not need a digestive system. Explain what is right and what is wrong '
                             'in their reasoning, using the difference between mechanical and '
                             'chemical digestion.',
                        'field_label': 'Your explanation',
                        'placeholder': 'They are right that… but wrong that…',
                        'success': ['Credits what is right: blending does the job of mechanical '
                                    'digestion, and does it better than teeth.',
                                    'Says mechanical breakdown makes pieces smaller without '
                                    'changing the molecules.',
                                    'States that absorption needs small soluble molecules, and '
                                    'starch, protein and lipid molecules are too large.',
                                    'Says only enzymes can cut the molecules, and names at least '
                                    'one product — glucose, amino acids, or fatty acids.',
                                    'Concludes that blending removes the need for chewing, not for '
                                    'the digestive system.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A person has a section of small intestine removed after an injury. '
                             'Predict what will change about their digestion and absorption, say '
                             'why the stomach cannot compensate, and name one thing that would not '
                             'change at all.',
                        'field_label': 'Your answer',
                        'placeholder': 'Losing small intestine would mean…',
                        'success': ['Predicts reduced absorption, because absorbing surface has '
                                    'been lost.',
                                    'Explains that the stomach cannot compensate because it barely '
                                    'absorbs anything even when intact.',
                                    'Notes that digestion may be less complete too, since enzymes '
                                    'have less time and less surface to act on.',
                                    'Names something unchanged — chewing, swallowing, stomach '
                                    'acid, or egestion.']}},
 'key_note': 'Food passes through the mouth, oesophagus, stomach, small intestine and large '
             'intestine. The pancreas, liver and gall bladder add secretions without food passing '
             'through them. Mechanical breakdown increases surface area; chemical breakdown by '
             'enzymes turns large insoluble molecules into small soluble ones. Almost all '
             'absorption happens in the small intestine.',
 'stretch': [{'type': 'explainer',
              'id': 'outside-you',
              'text': 'There is a real sense in which the inside of your gut is outside your body. '
                      'The tube runs from mouth to anus without interruption, so its contents are '
                      'topologically outside you in the same way that the hole in a doughnut is '
                      'outside the doughnut — nothing has entered you until it has crossed the gut '
                      'wall into the blood. This is not a word game; it is why the gut can hold '
                      'trillions of bacteria without your immune system treating it as an '
                      'infection, and why swallowing a small coin is usually harmless while the '
                      'same coin in your bloodstream would not be. Absorption, not swallowing, is '
                      'the moment food enters you.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Unclear why chewing is not digestion on its own?',
           'cta': 'Ask about this lesson',
           'anchor': 's-two'},
 'ws': ['analysis-and-evaluation'],
 'convention_note': 'Transit times are typical figures for a mixed meal in a healthy adult and '
                    'vary widely between people and between meals.',
 'review_state': 'draft',
 'authored': True}
