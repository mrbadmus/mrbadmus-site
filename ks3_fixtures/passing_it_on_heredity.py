# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B10 `passing-it-on-heredity` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B10'
SOURCE_SLUG = 'passing-it-on-heredity'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'passing-it-on-heredity',
 'title': 'Passing it on: heredity',
 'discipline': 'biology',
 'unit': 'inheritance-and-dna',
 'family': 'PROCESS',
 'covers': ['KS3.B.INH.01'],
 'touches': ['KS3.B.INH.02', 'KS3.B.INH.04'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 3}, {'id': 'cells-and-systems', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['chromosomes-genes-and-dna', 'gametes-and-fertilisation'],
 'assumes': [],
 'references': ['what-makes-a-species', {'unit': 'B11', 'lesson': 'natural-selection'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Alleles, dominant and recessive, homozygous and heterozygous, Punnett squares and '
                'probability, and inherited disorders.',
 'big_question': 'A characteristic can vanish for a whole generation and then come back. What does '
                 'that tell us about how it is passed on?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'It came back', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Grow seeds',
           'done_when': 'twenty_seeds_grown'},
          {'anchor': 's-steps',
           'short': 'STEPS',
           'label': 'The journey',
           'mirrors': 's-bench',
           'done_when': 'twenty_seeds_grown'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Cross a tall pea plant with a short one and you get tall plants.',
                'prompt': 'Then breed those tall plants together, and short plants come back in '
                          'about a quarter of the offspring.',
                'commit': 'If you had to guess, what happened to the shortness while every plant '
                          'grew tall?',
                'options': ['Hidden, but still there', 'Mixed in and watered down'],
                'reveal': 'Inherited information comes in separate units that keep their identity '
                          'from one generation to the next. Next: grow pea seeds from two parent '
                          'plants and count the flower colours.',
                'guess': True,
                'replies': ['The instruction for short was carried, complete and unchanged, by '
                            'plants that looked tall. Nothing was lost along the way.',
                            'Mixing paint works like that. But the shortness came back at full '
                            'strength, so it was never watered down.'],
                'answer': 0},
 'misconceptions': [{'id': 'GENE-07',
                     'statement': 'Characteristics blend — a tall parent and a short parent give a '
                                  'medium child.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'},
                    {'id': 'GENE-08',
                     'statement': 'It skipped a generation, so the gene must have disappeared and '
                                  'come back.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'heredity',
                 'definition': 'The passing of genetic information from parents to their '
                               'offspring.',
                 'note': 'The process, not the information. What is passed on is genes.'},
                {'term': 'gamete',
                 'definition': 'A sex cell — a sperm, an egg or a pollen grain — carrying one '
                               'chromosome from every pair instead of two.',
                 'note': 'Half a set, so that two of them make a full one.'},
                {'term': 'fertilisation',
                 'definition': 'Two gametes fusing, so the offspring has a full set of chromosomes '
                               'again, half from each parent.',
                 'note': 'The moment the new combination is fixed.'},
                {'term': 'version of a gene',
                 'definition': 'One of the alternative forms a gene comes in, such as the one for '
                               'purple flowers and the one for white.',
                 'note': 'An organism carries two and may show only one of them.'},
                {'term': 'offspring',
                 'definition': 'The new organisms produced by a cross or by a pair of parents.',
                 'note': 'A proportion of them, not any single one, is what a prediction is '
                         'about.'},
                {'term': 'pure-breeding',
                 'definition': 'Carrying two identical versions of a gene, so every offspring '
                               'receives the same one.',
                 'note': 'Mendel started every experiment with lines like these.'}],
 'figures': [{'id': 'b10-punnett-pp',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'punnett',
              'title': 'Every way two Pp parents can pass their gene versions on',
              'desc': 'A two-by-two grid with a parent plant drawn above it and another to the '
                      'left of it, both labelled Pp. Two arrows lead down from the parent above '
                      'the grid, one to each column heading, and two more lead across from the '
                      'parent beside it, one to each row heading. Each heading is a single letter '
                      'in a circle — P and p on the columns, P and p on the rows — because each '
                      'parent carries two versions and passes one of them, chosen at random. Every '
                      'square of the grid holds the pair of letters made by its own column and '
                      'row, numbered one to four: PP, then Pp, then Pp, then pp. Under each pair '
                      'is a flower drawn with five petals and the word for its colour. The first '
                      'three flowers are drawn with solid petals and labelled purple; the fourth '
                      'is drawn as an outline only and labelled white. A dashed line runs from the '
                      'fourth square to a note reading that neither parent is white and this one '
                      'is. Beneath the grid the same four are listed again in a row, in the same '
                      'numbered order, and a drawn bracket gathers the first three under the words '
                      'three of the four, purple, with a second bracket under the fourth reading '
                      'one of the four, white. The ratio three purple to one white is printed '
                      'below them.',
              'caption': 'Each parent has two versions and passes one, so there are four ways the '
                         'pair can land — and the grid is all four. Three of them contain at least '
                         'one P, and P beats p, so three of the four flower purple. The fourth got '
                         'p from both parents. That is where three to one comes from, and it is '
                         'why a white plant can appear from two purple ones.',
              'data': {'parent1': 'Pp',
                       'parent2': 'Pp',
                       'dominant': 'purple',
                       'recessive': 'white'}}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'grow-seeds-and-count-them', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-steps',
           'eyebrow': 'How the information travels',
           'statement': 'Halved, combined, then copied into everything.',
           'cards': [{'num': '1',
                      'name': 'Every body cell has two of each',
                      'body': 'Chromosomes come in pairs — 23 pairs in a human — so every gene is '
                              'present twice, once on each chromosome of the pair. The two copies '
                              'may be the same version or different ones.'},
                     {'num': '2',
                      'name': 'Gametes get one of each',
                      'body': 'When sex cells are made, each gamete receives one chromosome from '
                              'every pair, so it carries a single version of each gene. Which one '
                              'it gets is decided by chance, which is why siblings differ.'},
                     {'num': '3',
                      'name': 'Fertilisation restores the pair',
                      'body': 'One gamete from each parent fuses and the full number is back — 46 '
                              'in humans, half from each parent. This is the moment the new '
                              'combination is fixed.'},
                     {'num': '4',
                      'name': 'Every cell is a copy',
                      'body': 'The fertilised egg divides again and again, copying its DNA exactly '
                              'each time, so every cell of the new organism carries the same '
                              'instructions it started with.'}],
           'key_fact': {'ref': 'heredity-halved-combined-copied', 'ground': 'card'}},
          {'type': 'figure', 'ref': 'b10-punnett-pp', 'anchor': 's-grid'},
          {'type': 'misconception',
           'id': 'blending-and-the-skipped-generation',
           'anchor': 's-think',
           'targets': 'GENE-07'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'heredity-halved-combined-copied',
                'text': 'Heredity is the transfer of genetic information from parents to '
                        'offspring. Each parent passes half their chromosomes in a gamete, so '
                        'offspring carry two versions of every gene, one from each parent. '
                        'Versions are not blended: one may be hidden for generations and still be '
                        'passed on unchanged.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'blending-and-the-skipped-generation',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'GENE-07',
                 'statements': [{'quote': 'Characteristics blend — a tall parent and a short '
                                          'parent give a medium child.',
                                 'body': ['This was the accepted view for most of the nineteenth '
                                          'century, and it has a fatal problem that Darwin himself '
                                          'worried about: if characteristics blended, then '
                                          'variation would halve with every generation and after a '
                                          'few dozen generations every individual in a species '
                                          'would be identical. Look around a classroom; that has '
                                          "not happened. Mendel's peas showed why. Cross a tall "
                                          'variety with a short one and the offspring are all '
                                          'tall, not medium — and the shortness reappears, '
                                          'undiluted, in the generation after. Information is '
                                          'carried in discrete units that keep their identity, and '
                                          'what you see is the result of which versions a plant '
                                          'happens to be carrying. Height in people looks like '
                                          'blending because hundreds of genes are involved, which '
                                          'is the smooth curve in Variation: continuous and '
                                          'discontinuous; underneath, each of those hundreds of '
                                          'genes is being passed on whole.']},
                                {'quote': 'It skipped a generation, so the gene must have '
                                          'disappeared and come back.',
                                 'body': ['Nothing disappeared. A characteristic that is hidden in '
                                          'one generation was being carried the whole time by '
                                          'parents who did not show it, because they also carried '
                                          'a version that overrides it. Set both parents on the '
                                          'bench to <em>Pp</em> — both purple — and roughly a '
                                          'quarter of the seeds come out white. The white version '
                                          'was in both parents, in every one of their cells, doing '
                                          'nothing visible. This matters far beyond peas: it is '
                                          'why two people with no family history of a condition '
                                          'can have a child who inherits it, and why breeders and '
                                          'doctors distinguish between what an organism shows and '
                                          'what it carries. The two questions <em>what does it '
                                          'look like</em> and <em>what is it carrying</em> have '
                                          'different answers, and only the second one predicts the '
                                          'next generation.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · two parents, one gene',
                 'heading': 'Grow seeds and count them',
                 'prompt': 'Flower colour in pea plants. Each parent carries two copies of the '
                           'gene and passes one of them, chosen at random, into each seed. '
                           '<strong>P</strong> gives purple and beats <strong>p</strong>; a plant '
                           'is white only if it has p from both parents.',
                 'progress': {'none': 'no seeds grown',
                              'suffix_one': 'seed grown',
                              'suffix_many': 'seeds grown'},
                 'genotypes': [{'id': 'PP', 'label': 'PP · purple', 'alleles': ['P', 'P']},
                               {'id': 'Pp', 'label': 'Pp · purple', 'alleles': ['P', 'p']},
                               {'id': 'pp', 'label': 'pp · white', 'alleles': ['p', 'p']}],
                 'parents': [{'id': 'parent1', 'name': 'Parent plant 1'},
                             {'id': 'parent2', 'name': 'Parent plant 2'}],
                 'start': {'parent1': 'Pp', 'parent2': 'Pp'},
                 'phenotypes': {'dominant': 'purple', 'recessive': 'white'},
                 'one_label': 'Grow one seed',
                 'many_label': 'Grow a hundred',
                 'many_n': 100,
                 'reset_label': 'Clear the plot',
                 'cross_join': 'crossed with',
                 'last_label': 'Most recent seed',
                 'last_template': 'This seed received {g1} from parent 1 and {g2} from parent 2, '
                                  'so it is {genotype} — a {phenotype}-flowered plant.',
                 'tally_rows': [{'id': 'dominant', 'name': 'Purple flowers'},
                                {'id': 'recessive', 'name': 'White flowers'}],
                 'ratio_template': 'Ratio purple to white — {ratio} : 1',
                 'no_recessive_template': 'No white plants at all in {total} seeds',
                 'no_recessive_template_one': 'No white plant — {total} seed grown',
                 'no_dominant_template': 'No purple plants at all in {total} seeds',
                 'no_dominant_template_one': 'No purple plant — {total} seed grown',
                 'notes': {'both_pure_dominant': 'Both parents carry two P versions, so there is '
                                                 'no p anywhere in this cross to pass on. Every '
                                                 'seed is purple, and none of them is carrying '
                                                 'anything hidden — grow a thousand and the '
                                                 'generation after will be purple too.',
                           'pure_dominant_x_pure_recessive': 'One parent has only P and the other '
                                                             'only p, so every seed receives one '
                                                             'of each and every seed is Pp. All '
                                                             'purple — and every single one of '
                                                             'them is carrying p. Cross two of '
                                                             'these and the white flowers come '
                                                             'back.',
                           'one_pure_dominant': 'One parent carries two P versions, so every seed '
                                                'receives at least one P. Every offspring is '
                                                'purple however many you grow — and some of them '
                                                'are quietly carrying p, which will show up in the '
                                                'generation after.',
                           'both_pure_recessive': 'Both parents carry only p, so every seed gets p '
                                                  'from both sides. All white, every time. A '
                                                  'hidden version stops being hidden when there is '
                                                  'nothing left to override it.',
                           'both_carriers': 'Both parents are purple and both carry p. Each seed '
                                            'has a one-in-four chance of receiving p from both — '
                                            'so about a quarter come out white, from two purple '
                                            'parents. This is Mendel’s 3:1, and it is the result '
                                            'that made him think in particles.',
                           'mixed': 'One parent carries two of the same version and the other '
                                    'carries one of each. Watch the proportion rather than any '
                                    'individual seed — chance decides each one, and only the '
                                    'totals show the pattern.'},
                 'id': 'grow-seeds-and-count-them',
                 'kind': 'pea-cross'}],
 'ladder': {'recall': {'title': 'Rung 1 · The numbers',
                       'q': 'A human body cell has 46 chromosomes. How many are in a sperm cell, '
                            'and why?',
                       'options': ['46, as every cell in the body has the same number',
                                   '23, as each chromosome is cut in half to make the sperm',
                                   '92, as the chromosomes double before fertilisation',
                                   '23, one from each pair, so the fertilised egg has 46'],
                       'answer': 3,
                       'feedback': {0: 'Then a fertilised egg would have 92. Gametes carry half '
                                       'the chromosomes.',
                                    1: 'Chromosomes are passed on whole. The sperm gets one from '
                                       'each pair.',
                                    2: 'The number is halved in a gamete, not doubled.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Two purple-flowered pea plants are crossed and about a quarter of the '
                           'offspring are white. What does that show?',
                      'options': ['A new white version of the gene appeared by mutation in the '
                                  'offspring',
                                  "The parents' colours blended together, then separated again in "
                                  'the offspring',
                                  'Something in the soil turned a quarter of the flowers white',
                                  'Both parents were carrying the white version without showing '
                                  'it'],
                      'answer': 3,
                      'feedback': {0: 'A new change is far too rare to explain a quarter. Both '
                                      'parents carried white.',
                                   1: 'Nothing blended. The white version was passed on unchanged.',
                                   2: 'One in four is the pattern of two parents carrying a hidden '
                                      'version.'}},
            'explain': {'title': 'Rung 3 · Explain the skipped generation',
                        'q': 'A characteristic appears in a grandparent, is absent in the parents, '
                             'and appears again in a grandchild. Explain how, using what you know '
                             'about versions of genes and how gametes are made.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The grandparent had two copies of…',
                        'success': ['Says each individual carries two versions of the gene, one '
                                    'from each parent.',
                                    'Says one version can override the other, so an individual can '
                                    'carry a version without showing it.',
                                    'Says the parents each carried the hidden version and passed '
                                    'it on unchanged.',
                                    'Says the grandchild received that version from both parents, '
                                    'so there was nothing to override it.',
                                    'Makes clear the version was never lost or recreated — it was '
                                    'carried the whole time.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A dog breeder wants white-coated puppies, and white is the hidden '
                             'version of the coat-colour gene. She has two coloured-coated dogs '
                             'that have each produced a white puppy in an earlier litter. Explain '
                             'what she can predict, what she cannot, and why breeding for a hidden '
                             'characteristic is easier than breeding one out.',
                        'field_label': 'Your answer',
                        'placeholder': 'Both dogs must be carrying…',
                        'success': ['Says both dogs must be carrying the white version, because '
                                    'they have produced white puppies.',
                                    'Says roughly a quarter of the puppies in a litter would be '
                                    'expected to be white.',
                                    'Says she cannot predict any individual puppy — which version '
                                    'each gamete carries is chance.',
                                    'Says a small litter may not show the ratio at all, so the '
                                    'prediction is about large numbers.',
                                    'Explains that a white dog must carry two white versions and '
                                    'so breeds true, while a coloured dog may or may not be '
                                    'carrying white and cannot be identified by looking.']}},
 'key_note': 'Heredity is the passing of genetic information from one generation to the next. '
             'Gametes carry half the chromosomes — 23 in humans — so a fertilised egg has a full '
             'set of 46, half from each parent, and every cell of the new organism is a copy of '
             'that. Genes come in versions; an organism carries two of each and shows one, so a '
             'version can be carried without being shown and can reappear generations later.',
 'stretch': [{'type': 'explainer',
              'id': 'the-man-who-counted-the-peas',
              'text': 'Gregor Mendel was a monk running a garden in what is now the Czech '
                      'Republic, and between 1856 and 1863 he grew something like 28,000 pea '
                      'plants, counting the offspring of every cross. Peas were an inspired '
                      'choice: they self-pollinate, so he could establish pure-breeding lines; '
                      'they have several characteristics that come in two clean forms; and they '
                      'grow fast. Counting was the real innovation. Other people had crossed '
                      'plants before and described the results; Mendel counted them, found ratios '
                      'close to 3:1, and realised the ratio implied particles rather than fluids. '
                      'He published in 1866 and was almost entirely ignored — his paper was cited '
                      'a handful of times in thirty-four years — and he died in 1884 without '
                      'knowing. Three separate botanists rediscovered the same rules in 1900 and '
                      'found his paper already there. It is the clearest case in science of a '
                      'correct answer arriving before anyone had a use for it.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to work out what a cross would produce before you run it?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The bench uses one gene with two versions and a clean dominance rule, which '
                    'is the simplest case and the one Mendel chose deliberately. Most '
                    'characteristics involve several genes, several versions and no clean '
                    'dominance, and a real 3:1 ratio only emerges over large numbers — which is '
                    'why the hundred-seed button exists.',
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
