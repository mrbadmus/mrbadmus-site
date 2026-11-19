# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B10 `chromosomes-genes-and-dna` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B10'
SOURCE_SLUG = 'chromosomes-genes-and-dna'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'chromosomes-genes-and-dna',
 'title': 'Chromosomes, genes and DNA',
 'discipline': 'biology',
 'unit': 'inheritance-and-dna',
 'family': 'MODEL',
 'covers': ['KS3.B.INH.02a'],
 'touches': ['KS3.B.CELLS.02', 'KS3.B.CELLS.06'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 2}, {'id': 'cells-and-systems', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['animal-and-plant-cells', 'levels-of-organisation'],
 'assumes': [],
 'references': [{'unit': 'B10',
                 'lesson': 'how-we-worked-out-dna',
                 'label': "How we worked out DNA's structure"},
                {'unit': 'B1', 'lesson': 'specialised-cells'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Alleles, genotype and phenotype, protein synthesis, and the genome as a whole.',
 'big_question': 'Nucleus, chromosome, gene, DNA: people often use these four words as if they '
                 'meant the same thing. How do they actually fit together?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Two metres', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'ZOOM',
           'label': 'Zoom in',
           'done_when': 'all_levels_shown'},
          {'anchor': 's-model',
           'short': 'MODEL',
           'label': 'The model',
           'mirrors': 's-bench',
           'done_when': 'all_levels_shown'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two metres of DNA, in a nucleus you cannot see.',
                'prompt': 'Unwind the DNA from a single one of your cells and lay it end to end '
                          'and it measures about two metres. The nucleus holding it is around six '
                          'thousandths of a millimetre across. Almost every cell in your body is '
                          'doing this, right now.',
                'commit': 'If you had to guess, how does two metres of DNA fit inside one tiny '
                          'nucleus?',
                'options': ['It is coiled up tightly', 'Most of it is kept elsewhere'],
                'reveal': 'The coiled packages are called chromosomes, and the pieces inside them '
                          'have names too. Next: zoom in from a whole person down to the letters '
                          'that spell out an instruction.',
                'guess': True,
                'replies': ['DNA is incredibly thin, and it is wound round proteins, then coiled '
                            'again and again. All two metres really are inside the nucleus.',
                            'It is a very small space. But the whole two metres is inside the '
                            'nucleus. It fits because it is very thin and coiled up tightly.'],
                'answer': 0},
 'misconceptions': [{'id': 'GENE-03',
                     'statement': 'Chromosomes, genes and DNA are three different things in the '
                                  'nucleus.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'},
                    {'id': 'GENE-04',
                     'statement': 'Only the cells that need a gene contain it.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'DNA',
                 'definition': 'The long molecule that carries the instructions for building and '
                               'running an organism.',
                 'note': 'One molecule, seen at four magnifications in this lesson.'},
                {'term': 'chromosome',
                 'definition': 'One DNA molecule coiled tightly with proteins so it can be stored '
                               'and moved without tangling.',
                 'note': 'Not a different substance from DNA. It is DNA, packed.'},
                {'term': 'gene',
                 'definition': 'A section of the DNA in a chromosome, carrying the instruction for '
                               'one characteristic.',
                 'note': 'A part of the chromosome, not an object attached to it.'},
                {'term': 'base',
                 'definition': 'One of the four units — A, T, C and G — whose order along a gene '
                               'is the instruction.',
                 'note': 'The alphabet. Nothing to do with the bases in acid chemistry.'},
                {'term': 'nucleus',
                 'definition': 'The part of a cell that holds the chromosomes.',
                 'note': 'Met in Animal and plant cells; this lesson looks inside it.'}],
 'figures': [{'id': 'b10-nested-scale',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'nested-scale',
              'title': 'Chromosomes, genes and DNA: one strand at five magnifications',
              'desc': 'Five framed drawings in a column, each a magnified callout of the one above '
                      'it, joined by tapering wedges. Panel 01, a cell 0.02 mm across, with a '
                      'nucleus at its centre; a single orange fleck inside the nucleus is the '
                      'strand the figure follows. Panel 02, that nucleus enlarged to 0.006 mm, '
                      'holding 46 chromosomes in 23 pairs drawn in grey, with one of them picked '
                      'out in orange. Panel 03, that one chromosome, 0.002 mm long, drawn as an '
                      'orange strand coiled around grey proteins and unwinding at its lower end. '
                      'Panel 04, the unwound strand as two orange backbones with rungs between '
                      'them, running the width of the frame; a bracket marks one length of it as a '
                      'gene. Panel 05, four rungs of that same length, each a pair of lettered '
                      'boxes: A with T, C with G, T with A, G with C, the letters 0.0000003 mm '
                      'apart. Orange is DNA in every panel. Grey and dark ink are everything that '
                      'is not DNA.',
              'caption': 'One molecule, five magnifications. Each frame is a callout of the frame '
                         'above it, and the orange strand you can trace from the top of the column '
                         'to the bottom never stops being the same strand. Orange is DNA wherever '
                         'it appears; ink and grey are everything that is not DNA. The gene in '
                         'panel 04 is a marked length of the strand that was coiled in panel 03 — '
                         'a section of it, not a separate object sitting on it. Nothing is swapped '
                         'for anything else on the way down: a chromosome, a gene and DNA are not '
                         'three things sitting side by side in the nucleus, they are one thing at '
                         'three magnifications. Count the marks in panel 02 — there are 46, in 23 '
                         'pairs — and the orange one is the member of one pair that the rest of '
                         'the column follows.'}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'from-a-whole-person-to-four-letters', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-model',
           'eyebrow': 'The model in four sentences',
           'statement': 'A gene is an instruction for one job.',
           'cards': [{'role': 'The molecule',
                      'name': 'DNA',
                      'body': 'A long, thin molecule made of two strands twisted round each other. '
                              'It carries information in the order of its four bases, and it can '
                              'be copied exactly.'},
                     {'role': 'The package',
                      'name': 'Chromosome',
                      'body': 'One DNA molecule, coiled with proteins so it can be stored and '
                              'moved without tangling. 46 in a human body cell, in 23 matched '
                              'pairs.'},
                     {'role': 'The instruction',
                      'name': 'Gene',
                      'body': 'A section of DNA that codes for one characteristic. Different '
                              'versions of the same gene are why people differ — the gene for eye '
                              'colour is in everybody.'},
                     {'role': 'The alphabet',
                      'name': 'Bases',
                      'body': 'Four of them, A, T, C and G, in a sequence. Everything a cell can '
                              'be told is written with those four letters and nothing else.'}],
           'key_fact': {'ref': 'the-four-levels', 'ground': 'card'}},
          {'type': 'figure', 'ref': 'b10-nested-scale', 'anchor': 's-nested'},
          {'type': 'misconception',
           'id': 'three-things-and-the-cells-that-need-them',
           'anchor': 's-think',
           'targets': 'GENE-03'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'the-four-levels',
                'text': 'DNA is a long molecule found in the nucleus. It is coiled into '
                        'chromosomes — 46 in a human body cell, in 23 pairs. A gene is a section '
                        'of DNA carrying the instruction for one characteristic, and the '
                        'instruction is written in a sequence of four bases.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'three-things-and-the-cells-that-need-them',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'GENE-03',
                 'statements': [{'quote': 'Chromosomes, genes and DNA are three different things '
                                          'in the nucleus.',
                                 'body': ['They are one thing described at three magnifications, '
                                          'and the levels-of-organisation ladder is the right way '
                                          'to hold it: cell, tissue, organ, organ system was one '
                                          'nesting, and DNA, gene, chromosome, nucleus is another. '
                                          'DNA is the molecule. A gene is a length of that '
                                          'molecule — a section, not a separate object sitting on '
                                          'it. A chromosome is the whole molecule coiled up '
                                          'tightly with proteins so that it can be moved around '
                                          'without tangling. Asking whether a nucleus contains '
                                          'chromosomes <em>or</em> DNA is like asking whether a '
                                          'library contains books or paper. The one place the '
                                          'analogy is worth pushing further: a chromosome is a '
                                          'single, extremely long DNA molecule, so a gene is not '
                                          'attached to a chromosome — it is part of it, the way a '
                                          'chapter is part of a book rather than a bookmark in '
                                          'one.']},
                                {'quote': 'Only the cells that need a gene contain it.',
                                 'body': ['Every cell with a nucleus carries the whole set: all 46 '
                                          'chromosomes, all of your genes, the complete '
                                          'instructions. A cell in your eye contains the genes for '
                                          'making liver enzymes and for growing hair, and a cell '
                                          'in your liver contains the genes for eye colour. What '
                                          'differs between cells is which genes are <em>switched '
                                          'on</em>, and that is what makes a nerve cell different '
                                          'from a skin cell despite the two carrying identical '
                                          'information — which is the mechanism behind the '
                                          'specialised cells. It is also the reason a single cell '
                                          'left at a crime scene identifies a person, and the '
                                          'reason a whole sheep could be built from one udder '
                                          'cell. If cells only carried the genes they were using, '
                                          'none of that would be possible.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · zoom in five times',
                 'heading': 'From a whole person to four letters',
                 'prompt': 'Each step down is inside the one above it, and nothing new is added — '
                           'you are looking at the same material, closer.',
                 'progress': {'all': 'all six levels',
                              'step_prefix': 'level ',
                              'step_join': ' of '},
                 'levels': [{'name': 'A person',
                             'scale': '1.6 m',
                             'body': 'Around thirty trillion cells, almost every one of them '
                                     'carrying an identical copy of the same instructions.'},
                            {'name': 'A cell',
                             'scale': '0.02 mm',
                             'body': 'Any body cell will do — a cheek cell, a liver cell, a root '
                                     'hair cell in a plant. All of them keep their instructions in '
                                     'the same place.'},
                            {'name': 'The nucleus',
                             'scale': '0.006 mm',
                             'body': 'The control centre of the cell, and where the DNA is kept. '
                                     'Red blood cells are the famous exception: they throw theirs '
                                     'away to make room for haemoglobin.'},
                            {'name': 'A chromosome',
                             'scale': '0.002 mm long',
                             'body': 'DNA wound around proteins and coiled tightly. A human body '
                                     'cell has 46 of them, in 23 pairs — one of each pair from '
                                     'each parent. They are only visible under a microscope when a '
                                     'cell is about to divide.'},
                            {'name': 'A gene',
                             'scale': 'a section of the strand',
                             'body': 'A length of the DNA in that chromosome, carrying the '
                                     'instruction for one characteristic. Not a separate object '
                                     'attached to the chromosome — a part of it, like a chapter in '
                                     'a book.'},
                            {'name': 'The bases',
                             'scale': '0.0000003 mm apart',
                             'body': 'The instruction is written in a sequence of four bases, '
                                     'known by their initials A, T, C and G. The order of those '
                                     'letters along the gene is the information.'}],
                 'in_label': 'Zoom in',
                 'in_done_label': 'As far in as it goes',
                 'reset_label': 'Back out',
                 'close': 'Six levels, and the last three are all the same molecule seen at '
                          'different magnifications. A chromosome is coiled DNA; a gene is a '
                          'section of that DNA; the bases are the units the section is written in. '
                          'Nothing was swapped for anything else on the way down.',
                 'say_it_back': {'options_label': 'Say it back — which one is which?',
                                 'opens_on': 'contains',
                                 'questions': [{'id': 'longest',
                                                'label': 'Which is the longest?',
                                                'answer': 'All the DNA in one cell — about two '
                                                          'metres if you uncoiled it all. It is '
                                                          'divided between 46 chromosomes, each '
                                                          'packed down to a few thousandths of a '
                                                          'millimetre.'},
                                               {'id': 'contains',
                                                'label': 'What contains what?',
                                                'answer': 'The nucleus contains the chromosomes; '
                                                          'each chromosome is one coiled DNA '
                                                          'molecule; each gene is a section of '
                                                          'that DNA; the bases are the units the '
                                                          'section is written in. Five levels, '
                                                          'each inside the last.'},
                                               {'id': 'howmany',
                                                'label': 'How many, in a human?',
                                                'answer': '46 chromosomes in 23 pairs in a body '
                                                          'cell, 23 single chromosomes in a sperm '
                                                          'or egg cell, and around twenty thousand '
                                                          'genes altogether.'},
                                               {'id': 'same',
                                                'label': 'Do all your cells match?',
                                                'answer': 'Yes — every cell with a nucleus carries '
                                                          'the same complete set. What differs is '
                                                          'which genes are switched on, and that '
                                                          'is what makes a nerve cell different '
                                                          'from a skin cell.'}]},
                 'id': 'from-a-whole-person-to-four-letters',
                 'kind': 'zoom-bench'}],
 'ladder': {'recall': {'title': 'Rung 1 · Put them in order',
                       'q': 'Order these from largest to smallest: gene, nucleus, chromosome, '
                            'base.',
                       'options': ['Chromosome, nucleus, gene, base',
                                   'Nucleus, chromosome, gene, base',
                                   'Nucleus, gene, chromosome, base',
                                   'Gene, chromosome, nucleus, base'],
                       'answer': 1,
                       'feedback': {0: 'The nucleus holds the chromosomes, so it is the largest.',
                                    2: 'A gene is a section of a chromosome, so it is smaller.',
                                    3: 'The nucleus holds everything else, so it comes first.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Does a cell in your foot contain the genes for eye colour?',
                      'options': ['Yes, as every body cell with a nucleus has all your genes',
                                  'No, as those genes are only found in the cells of the eye',
                                  'Only if you have brown eyes, as only they carry those genes',
                                  'No, as genes move to the organs that need to use them'],
                      'answer': 0,
                      'feedback': {1: 'Every body cell with a nucleus has every gene. Genes are '
                                      'not sorted by organ.',
                                   2: 'Everyone has the eye colour genes. People differ in which '
                                      'versions they carry.',
                                   3: 'Genes cannot move. They are sections of the chromosomes in '
                                      'each nucleus.'}},
            'explain': {'title': 'Rung 3 · Explain the nesting',
                        'q': 'A student says "the nucleus contains chromosomes and DNA and genes". '
                             'Rewrite the sentence so it is correct, and explain how the four '
                             'things are related.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The nucleus contains chromosomes, which are…',
                        'success': ['Says the nucleus contains chromosomes.',
                                    'Says each chromosome is a long DNA molecule, coiled up — not '
                                    'a separate thing from DNA.',
                                    'Says a gene is a section of the DNA in a chromosome.',
                                    'Makes clear the three are not three separate contents of the '
                                    'nucleus but one structure at three levels.',
                                    'Uses a comparison or an ordering that shows the nesting '
                                    'clearly — for example largest to smallest, or a book, chapter '
                                    'and letters.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A single cheek cell left on a glass at a crime scene is enough to '
                             'identify a person. Explain what makes that possible, using what you '
                             'know about where genetic information is stored and which cells carry '
                             'it.',
                        'field_label': 'Your answer',
                        'placeholder': 'Every cell with a nucleus…',
                        'success': ['Says every cell with a nucleus carries the person’s complete '
                                    'set of chromosomes.',
                                    'Says the DNA in any one cell is therefore the same as in any '
                                    'other cell of that person.',
                                    'Says the sequence of bases differs between people, so it can '
                                    'be used to tell them apart.',
                                    'Says a single cell is enough because the whole instruction '
                                    'set is present in it, not just part of it.',
                                    'Identifies a limitation — identical twins share their DNA, or '
                                    'the sample may be contaminated or degraded, or a red blood '
                                    'cell would not work because it has no nucleus.']}},
 'key_note': 'DNA is a long molecule, coiled with proteins into chromosomes and stored in the '
             'nucleus. A human body cell has 46 chromosomes in 23 pairs, one of each pair from '
             'each parent. A gene is a section of DNA that carries the instruction for a '
             'characteristic, and the instruction is written as a sequence of four bases. Every '
             'cell with a nucleus carries the whole set; cells differ in which genes are switched '
             'on.',
 'stretch': [{'type': 'explainer',
              'id': 'what-the-counts-do-not-tell-you',
              'text': 'The number of chromosomes tells you almost nothing about an organism. A '
                      'human has 46, a chimpanzee 48, a potato 48, a dog 78 and a particular fern '
                      'over a thousand. Complexity does not track the count, and neither does the '
                      'number of genes: humans have around twenty thousand, which came as an '
                      'unwelcome surprise in 2003 when the Human Genome Project finished and the '
                      'pre-project bets had run to a hundred thousand. A water flea has more genes '
                      'than you do. What the count misses is that a gene can be read in several '
                      'ways, that most of the genome is regulatory rather than instructional, and '
                      'that the interesting differences between species are as much about when and '
                      'where genes are switched on as about which genes exist. Chimpanzee and '
                      'human DNA differ by something like one per cent of the letters, and that '
                      'one per cent includes a great deal of switching.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to get the four words straight in your own wording?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The scale figures are rounded to the nearest order of magnitude to make the '
                    'nesting readable. "One gene, one characteristic" is a deliberate '
                    'simplification kept for KS3: most characteristics involve many genes and many '
                    'genes affect more than one characteristic, as the height curve in Variation: '
                    'continuous and discontinuous already implied.',
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
