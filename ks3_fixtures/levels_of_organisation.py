# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B1 `levels-of-organisation` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B1'
SOURCE_SLUG = 'levels-of-organisation'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'levels-of-organisation',
 'title': 'Levels of organisation',
 'discipline': 'biology',
 'unit': 'cells-and-organisation',
 'family': 'SYSTEM',
 'covers': ['KS3.B.CELLS.06'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 3}, {'id': 'structure-function', 'level': 2}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['specialised-cells'],
 'assumes': [],
 'references': ['unicellular-organisms', 'life-processes'],
 'ks4_links': [],
 'ks4_becomes': 'Organ systems in detail — digestion, circulation, gas exchange — and tissue '
                'engineering.',
 'big_question': 'A dish of living stomach cells cannot digest a sandwich. Your stomach can. What '
                 'is the difference?',
 'phenomenon': {'kind': 'demo',
                'eyebrow': 'Start here',
                'title': 'Stomach cells in a dish, and a stomach.',
                'prompt': 'Scientists can grow real stomach cells in a dish. They live for weeks, '
                          'making acid and enzymes. Put a sandwich in the dish and it sits there. '
                          'Put it in a stomach and twenty minutes later it is gone.',
                'commit': 'If you had to guess, what lets a real stomach do what the dish of cells '
                          'cannot?',
                'options': ['Many more cells', 'Cells arranged in layers'],
                'reveal': 'That gives a ladder of levels, from one cell up to a whole living '
                          'thing. Next: zoom from a whole plant down to one cell, one level at a '
                          'time.',
                'guess': True,
                'replies': ['More cells sounds sensible, but a dish with a thousand times more '
                            'would still leave the sandwich untouched. It is how they are arranged '
                            'that counts.',
                            'Layers, each with its own job: muscle to churn the food, a lining to '
                            'make acid and enzymes. They only work as a team.'],
                'answer': 1},
 'misconceptions': [{'id': 'CELL-06',
                     'statement': 'An organ is just a bigger tissue.',
                     'elicited_by': 's-hard',
                     'confronted_by': 'organ-is-not-a-bigger-tissue'},
                    {'id': 'CELL-07',
                     'statement': 'Blood can’t be a tissue — it’s a liquid.',
                     'elicited_by': 's-hard',
                     'confronted_by': 'organ-is-not-a-bigger-tissue'}],
 'vocabulary': [{'term': 'tissue',
                 'definition': 'A group of similar cells working together to do one job.',
                 'note': None},
                {'term': 'organ',
                 'definition': 'A group of different tissues working together to do one job.',
                 'note': 'A stomach is an organ. So is a leaf — plants have them too.'},
                {'term': 'organ system',
                 'definition': 'A group of organs working together to do one big job.',
                 'note': 'Your digestive system is a chain of organs, from your mouth to your '
                         'intestines.'}],
 'figures': [],
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Cells in a dish',
           'done_when': 'committed'},
          {'anchor': 's-zoom',
           'short': 'ZOOM',
           'label': 'Five stops',
           'done_when': 'all_stops_seen',
           'threshold': 5},
          {'anchor': 's-hard',
           'short': 'SORT',
           'label': 'The awkward ones',
           'done_when': 'answers_opened'},
          {'anchor': 's-break',
           'short': 'BREAK',
           'label': 'Take a level out',
           'done_when': 'all_cases_explored',
           'threshold': 4},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'key_facts': [{'id': 'kf-a-rung-up-is-a-different-kind',
                'text': 'A rung up is a different kind of thing, not a bigger one. The only thing '
                        'added between rungs is organisation.',
                'eyebrow': 'Key fact',
                'ground': 'band',
                'placement': 'top-level'}],
 'tutor': {'prompt': 'Stuck on which rung something belongs to?',
           'cta': 'Ask about this lesson',
           'anchor': 's-hard'},
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'check', 'id': 's-zoom', 'anchor': 's-zoom'},
          {'type': 'check', 'id': 's-hard', 'anchor': 's-hard'},
          {'type': 'practical', 'id': 's-break', 'anchor': 's-break'},
          {'type': 'misconception',
           'id': 'organ-is-not-a-bigger-tissue',
           'anchor': 's-think',
           'eyebrow': 'Think again'},
          {'type': 'key-fact', 'ref': 0},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote', 'eyebrow': 'Key note'}],
 'stretch': [{'type': 'explainer',
              'text': 'The ladder does not stop at the organism. Above it sit populations, '
                      'communities and ecosystems, and the same rule holds: each level does '
                      'something the one below cannot. A single rabbit cannot go extinct and '
                      'cannot evolve — only a population can. It runs downwards too, past the cell '
                      'to organelles, molecules and atoms. Biologists put the bottom rung at the '
                      'cell because it is the smallest thing on the ladder that is '
                      '<em>alive</em>.'}],
 'support': [],
 'activities': [{'id': 'organ-is-not-a-bigger-tissue',
                 'kind': 'confrontation',
                 'demand': 'confront both level misconceptions in one pass: the size error and the '
                           'solidity error',
                 'targets': ['CELL-06', 'CELL-07'],
                 'statements': [{'quote': 'An organ is just a bigger tissue.',
                                 'answer': 'Size is not what the ladder measures. A rung up is not '
                                           'more of the same thing — it is a different '
                                           '<em>kind</em> of thing, made by putting unlike parts '
                                           'together. A tissue is many cells of one kind doing one '
                                           'job. An organ is several <em>different</em> tissues '
                                           'that between them do a job none of them could do '
                                           'alone. Your stomach has a muscle layer to churn, a '
                                           'lining to make acid and enzymes, connective tissue to '
                                           'hold it in shape and nerves to time it. Grow the '
                                           'muscle layer to the size of a stomach and it still '
                                           'cannot digest anything.'},
                                {'quote': 'Blood can’t be a tissue — it’s a liquid.',
                                 'answer': 'A tissue is defined by what it is made of and what it '
                                           'does, not by whether it holds its shape. Blood is a '
                                           'huge population of cells of a few kinds, suspended in '
                                           'liquid, all working on one job: transport. That makes '
                                           'it a tissue, and it is the reason the ladder is about '
                                           'organisation rather than about solidity.'}]},
                {'eyebrow': 'Zoom in · five stops',
                 'heading': 'From a whole plant to one cell, without leaving the leaf',
                 'prompt': 'Drag the slider. Each stop is hiding inside the one before it.',
                 'slider': True,
                 'slider_label': 'Zoom level',
                 'start': 'organism',
                 'step_format': 'Stop {n} of {total}',
                 'human_prefix': 'In you:',
                 'next_box_label': 'NEXT STOP IS HERE',
                 'canvas': {'buffer': [1800, 1000], 'design_space': [900, 500], 'device_scale': 2},
                 'levels': [{'tick': 'Organism',
                             'name': 'Organism — the whole plant',
                             'size': 'about 30 cm tall',
                             'what': 'Everything from the root tips to the newest leaf, working as '
                                     'one thing. It grows, it responds, it reproduces, it makes '
                                     'its own food.',
                             'gain_label': 'What it can do that an organ system cannot',
                             'gain': 'Live. No single system in a plant survives on its own — the '
                                     'shoot would starve of water in a day and the root would '
                                     'starve of sugar.',
                             'human': 'You. Roughly thirty trillion cells, and one thing.',
                             'alt': 'A whole plant with a stem, three leaves and a root system, '
                                    'with an orange box round the shoot.',
                             'drawing': 'plant',
                             'next_box': [180, 56, 540, 306]},
                            {'tick': 'Organ system',
                             'name': 'Organ system — the shoot',
                             'size': 'about 20 cm',
                             'what': 'The stem and all the leaves together. Several organs that '
                                     'share one overall job: catch light, make food, and move it '
                                     'to wherever it is needed.',
                             'gain_label': 'What it can do that a single organ cannot',
                             'gain': 'Run a whole function end to end. One leaf can '
                                     'photosynthesise but cannot deliver the sugar anywhere; the '
                                     'stem can move sugar but cannot make any.',
                             'human': 'Your digestive system: mouth, oesophagus, stomach, '
                                      'intestines, liver and pancreas, all on one job.',
                             'alt': 'The same plant with the stem and leaves drawn solid and the '
                                    'roots faded, and an orange box round one leaf.',
                             'drawing': 'plant',
                             'drawing_variant': 'shoot',
                             'next_box': [548, 150, 232, 124]},
                            {'tick': 'Organ',
                             'name': 'Organ — one leaf',
                             'size': 'about 5 cm long',
                             'what': 'A structure made of several different tissues, arranged so '
                                     'that together they do one job: photosynthesis.',
                             'gain_label': 'What it can do that a single tissue cannot',
                             'gain': 'Photosynthesise. The palisade layer traps the light, but it '
                                     'needs veins to bring water and carry sugar away, an '
                                     'epidermis to stop it drying out, and pores to let carbon '
                                     'dioxide in. Take any one of those away and the job fails.',
                             'human': 'Your stomach: muscle to churn, lining to make acid and '
                                      'enzymes, connective tissue to hold its shape, nerves to '
                                      'time it.',
                             'alt': 'A single leaf with a midrib and branching veins, with an '
                                    'orange box marking a slice through it.',
                             'drawing': 'one-leaf',
                             'next_box': [406, 122, 88, 256]},
                            {'tick': 'Tissue',
                             'name': 'Tissue — the palisade layer',
                             'size': 'about 0.2 mm thick',
                             'what': 'A group of similar cells, all doing the same job, packed '
                                     'together so their effect adds up. Here: one dense layer of '
                                     'tall cells right under the upper surface.',
                             'gain_label': 'What it can do that a single cell cannot',
                             'gain': 'Catch nearly all of the light landing on the leaf. One '
                                     'palisade cell intercepts a speck; a whole layer of them, '
                                     'shoulder to shoulder with no gaps, leaves almost nothing to '
                                     'get past.',
                             'human': 'Blood is a tissue. So is muscle, and so is the lining of '
                                      'your gut.',
                             'alt': 'A cross-section through a leaf showing the upper epidermis, a '
                                    'dense palisade layer, a spongy layer with air spaces, and the '
                                    'lower epidermis.',
                             'drawing': 'leaf-section',
                             'next_box': [100, 156, 76, 146]},
                            {'tick': 'Cell',
                             'name': 'Cell — one palisade cell',
                             'size': 'about 50 micrometres — 0.05 mm',
                             'what': 'The one you built two lessons ago: wall, membrane, '
                                     'cytoplasm, nucleus, mitochondria, vacuole, and chloroplasts '
                                     'crowded against the light.',
                             'gain_label': 'What it can do that its own parts cannot',
                             'gain': 'Be alive. A chloroplast on its own is machinery; a nucleus '
                                     'on its own is a library nobody reads. The cell is the '
                                     'smallest thing on this ladder that does all seven life '
                                     'processes.',
                             'human': 'Your cells too. Same rung, different tuning.',
                             'alt': 'A single palisade cell with a cell wall, a large vacuole, a '
                                    'nucleus at one side and chloroplasts packed near the top.',
                             'drawing': 'one-cell',
                             'next_box': None}],
                 'id': 's-zoom',
                 'kind': 'zoom-ladder',
                 'demand': 'investigate'},
                {'eyebrow': 'Your turn · the awkward ones',
                 'heading': 'Eight things that get put on the wrong rung',
                 'prompt': 'The easy examples teach you nothing. These are the ones people argue '
                           'about. Put each on a rung — change your mind as often as you like, '
                           'nothing is marked — then open the answers.',
                 'choices': ['Cell',
                             'Tissue',
                             'Organ',
                             'Organ system',
                             'Organism',
                             'Not on the ladder'],
                 'gate_label': 'Open the answers',
                 'counter': '{n} of {total} placed',
                 'marks_on_reveal': True,
                 'items': [{'id': 'blood',
                            'item': 'Blood',
                            'answer': 'Tissue',
                            'note': 'A few kinds of cell, in enormous numbers, suspended in liquid '
                                    'and all working on transport. Being a liquid does not '
                                    'disqualify it.'},
                           {'id': 'skin',
                            'item': 'Skin',
                            'answer': 'Organ',
                            'note': 'Your largest organ, and clearly several tissues: layers of '
                                    'epidermis, connective tissue underneath, glands, nerve '
                                    'endings and blood vessels running through it.'},
                           {'id': 'xylem',
                            'item': 'Xylem',
                            'answer': 'Tissue',
                            'note': 'Similar cells, one job — carrying water up the plant. It sits '
                                    'inside an organ (the stem, the root, the leaf) the way muscle '
                                    'sits inside your stomach.'},
                           {'id': 'brain',
                            'item': 'The brain',
                            'answer': 'Organ',
                            'note': 'Several tissues — nerve tissue of more than one kind, blood '
                                    'vessels, connective tissue and membranes. It is the main '
                                    'organ of the nervous system, not the system itself.'},
                           {'id': 'chloroplast',
                            'item': 'A chloroplast',
                            'answer': 'Not on the ladder',
                            'note': 'It is a part of a cell, below the bottom rung. That is '
                                    'exactly why the ladder starts at the cell: a chloroplast is '
                                    'machinery, not a living thing.'},
                           {'id': 'stomach',
                            'item': 'The stomach',
                            'answer': 'Organ',
                            'note': 'An organ of the digestive system. On its own it can churn and '
                                    'make acid; it cannot digest a meal and deliver it, which is '
                                    'what the system does.'},
                           {'id': 'bone',
                            'item': 'A bone, such as your femur',
                            'answer': 'Organ',
                            'note': 'This is the one worth arguing about, and both sides are right '
                                    'about different things. A named bone is an organ — it '
                                    'contains bone tissue, marrow, blood vessels and nerves. The '
                                    'hard material inside it, "bone", is a tissue. The wording '
                                    'decides which you mean.'},
                           {'id': 'rootsys',
                            'item': 'The root system of a tree',
                            'answer': 'Organ system',
                            'note': 'Many roots — each an organ — working together on one overall '
                                    'job: anchoring the tree and taking up water and minerals.'}],
                 'id': 's-hard',
                 'kind': 'sort-task',
                 'demand': 'investigate'},
                {'eyebrow': 'Take a level out',
                 'heading': 'Keep every cell alive. Remove the organisation.',
                 'lede': 'Nothing here is killed and nothing is taken away. In each case the parts '
                         'are all present and all healthy — only the arrangement is gone. Pick '
                         'one, say what stops, then read what actually happens.',
                 'counter': '{n} of {total} explored',
                 'what_label': 'What we did',
                 'commit': 'Commit first. What stops working?',
                 'lost_prefix': 'Level lost: ',
                 'principle_prefix': 'The principle:',
                 'cases': [{'id': 'dish',
                            'label': 'Stomach cells in a dish',
                            'what': 'We take a healthy stomach and separate every cell from every '
                                    'other cell. Nothing is killed.',
                            'intact': 'All the cells are alive. All of them are the right kinds. '
                                      'There are exactly as many as there were.',
                            'lost': 'Tissue and above',
                            'predict': ['Nothing — the cells still do their jobs',
                                        'Nothing can be churned or held together, so no meal is '
                                        'ever digested',
                                        'The cells die within minutes'],
                            'headline': 'They keep working. Nothing gets digested.',
                            'body': 'The acid-making cells make acid, into the dish. The muscle '
                                    'cells contract, on their own, in no particular direction. '
                                    'There is no cavity to hold food, no wall to squeeze it '
                                    'against, no sequence and no timing. Everything a stomach is '
                                    'for depended on the cells being arranged, and the arrangement '
                                    'is what we took.',
                            'principle': 'Between the cell and the tissue, the only thing added is '
                                         'organisation — and it is doing most of the work.'},
                           {'id': 'nomuscle',
                            'label': 'A stomach with no muscle layer',
                            'what': 'We leave the stomach whole and remove only its muscle tissue. '
                                    'Every other tissue stays where it is.',
                            'intact': 'The lining still makes acid and enzymes. The shape is still '
                                      'there. The nerves are still there.',
                            'lost': None,
                            'predict': ['Acid production stops',
                                        'The chemistry works but nothing mixes, so digestion is '
                                        'slow and patchy',
                                        'The stomach bursts'],
                            'headline': 'The chemistry is fine. The mixing is gone.',
                            'body': 'Enzymes only work where they meet the food, and a sandwich is '
                                    'not a liquid. Without the muscle layer squeezing and folding '
                                    'the contents, acid and enzymes reach the outside of the lump '
                                    'and never the middle. What should take twenty minutes does '
                                    'not finish at all.',
                            'principle': 'An organ is several unlike tissues. Remove one and the '
                                         'organ does not do a bit less of its job — it stops doing '
                                         'the job properly at all.'},
                           {'id': 'leafcells',
                            'label': 'Leaf cells, unarranged',
                            'what': 'We take a leaf and shuffle its cells, so palisade, spongy and '
                                    'epidermis cells are mixed evenly through a blob of the same '
                                    'total size.',
                            'intact': 'Every cell is alive, with all its chloroplasts. The blob '
                                      'has the same volume and mass as the leaf did.',
                            'lost': None,
                            'predict': ['It photosynthesises just as well',
                                        'Far less light is caught, and it dries out or suffocates',
                                        'It turns yellow immediately'],
                            'headline': 'It photosynthesises, badly, and not for long.',
                            'body': 'The chloroplasts are no longer in a dense layer at the top, '
                                    'so most of them sit in shade behind other cells. There is no '
                                    'epidermis on the outside, so water escapes freely; there are '
                                    'no air spaces, so carbon dioxide cannot reach the middle; and '
                                    'no veins, so nothing arrives or leaves. A leaf is flat and '
                                    'layered for reasons, and every one of them is now gone.',
                            'principle': 'Arrangement is not decoration. In an organ, where each '
                                         'tissue sits is part of how it works.'},
                           {'id': 'detached',
                            'label': 'A leaf cut off the plant',
                            'what': 'We cut a healthy leaf off and leave it in the light, with '
                                    'every cell and every tissue perfectly intact.',
                            'intact': 'The whole organ is undamaged. It keeps photosynthesising '
                                      'for a while.',
                            'lost': None,
                            'predict': ['It carries on indefinitely, since it makes its own food',
                                        'It runs out of water and has nowhere to send the sugar, '
                                        'so it fails within days',
                                        'It stops photosynthesising immediately'],
                            'headline': 'A perfect organ, for about two days.',
                            'body': 'It goes on making sugar until the water runs out — and there '
                                    'is no root system to replace what evaporates. The sugar it '
                                    'makes has nowhere to go, so it accumulates and photosynthesis '
                                    'slows. Nothing is wrong with the leaf. What is missing is '
                                    'everything it was connected to.',
                            'principle': 'An organ is not self-sufficient. That is exactly what an '
                                         'organ system, and then the organism, adds.'}],
                 'id': 's-break',
                 'kind': 'removal-cases',
                 'demand': 'investigate'}],
 'ladder': {'retry_note': 'Clears the ticks on rungs 3 and 4 and keeps what you wrote.',
            'recall': {'title': 'Rung 1 · Put it on a rung',
                       'q': 'Blood is a liquid that flows. Which level of organisation is it?',
                       'options': ['A cell', 'An organ', 'Not on the ladder at all', 'A tissue'],
                       'answer': 3,
                       'feedback': {0: 'It contains cells — several kinds of them — so it must be '
                                       'at least one rung above a cell.',
                                    1: 'An organ is several different tissues arranged together. '
                                       'Blood is one tissue, which travels through organs rather '
                                       'than being one.',
                                    2: 'It is on the ladder. Being a liquid is not the '
                                       'disqualifier — the ladder measures organisation, not '
                                       'solidity.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A dish of living stomach cells cannot digest a sandwich, even though '
                           'every cell is healthy and doing its job. Why not?',
                      'options': ['They are not organised into tissues and layers that work on the '
                                  'food together',
                                  'Digestion needs a big enough mass of cells, so a small dish can '
                                  'never manage it',
                                  'Stomach cells only line the stomach, so digesting food is a job '
                                  'for a different kind of cell',
                                  'Enzymes only work inside a living body, so cells in a dish '
                                  'cannot digest anything at all'],
                      'answer': 0,
                      'feedback': {1: 'Add a thousand times more and it still will not digest '
                                      'anything. The problem is not quantity.',
                                   2: 'They are exactly the right cells — the same ones that are '
                                      'doing it in you right now.',
                                   3: 'They do work outside one. These enzymes are being made and '
                                      'released — just into a dish rather than into a stomach.'}},
            'explain': {'title': 'Rung 3 · Explain it',
                        'q': 'Explain why a leaf is called an organ but the palisade layer inside '
                             'it is called a tissue. Use the word “tissues” in your answer.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The palisade layer is…',
                        'success': ['Says the palisade layer is many similar cells all doing the '
                                    'same job.',
                                    'Says a leaf contains several different tissues, and names at '
                                    'least two of them.',
                                    'Says the leaf does a job that no one of those tissues could '
                                    'do on its own.',
                                    'Makes clear the difference is organisation, not size.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A laboratory grows a sheet of living heart muscle cells in a dish. '
                             'It beats, steadily, on its own. A newspaper reports that they have '
                             'grown a heart. Say what they have actually made, which rung it is '
                             'on, and what would still be missing.',
                        'field_label': 'Your answer',
                        'placeholder': 'What they have made is…',
                        'success': ['Says they have made a tissue, not an organ, and says why: one '
                                    'kind of cell, one job.',
                                    'Names tissues a real heart has that the sheet does not — '
                                    'valves, blood vessels, nerve tissue, connective tissue.',
                                    'Says the arrangement matters too: four chambers in a '
                                    'particular order, so blood is pushed the right way.',
                                    'Says that even a complete heart would need to be connected '
                                    'into the circulatory system to be any use.']}},
 'key_note': 'Cells, tissues, organs, organ systems, organism. Each rung can do something the rung '
             'below it cannot — and the only thing added between rungs is organisation.',
 'illustration_palette': {'soil': '#EFE3C9',
                          'root': '#8A6A3C',
                          'stem': '#5E7A3A',
                          'leaf-fill': '#5E9440',
                          'leaf-stroke': '#2F5326',
                          'midrib': '#3E6B2C',
                          'epidermis': '#EFE6D2',
                          'cell-fill': '#EFF3E4',
                          'chloroplast': '#4F7C3B',
                          'cell-wall': '#D9C48D',
                          'cytoplasm': '#F5ECD8',
                          'membrane': '#A2603A',
                          'vacuole-fill': '#E4EDE9',
                          'vacuole-stroke': '#9AB0A6',
                          'nucleus-fill': '#7C6AA6',
                          'nucleus-stroke': '#453A69'},
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
