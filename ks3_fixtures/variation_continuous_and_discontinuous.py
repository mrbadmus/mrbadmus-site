# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B10 `variation-continuous-and-discontinuous` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B10'
SOURCE_SLUG = 'variation-continuous-and-discontinuous'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'variation-continuous-and-discontinuous',
 'title': 'Variation: continuous and discontinuous',
 'discipline': 'biology',
 'unit': 'inheritance-and-dna',
 'family': 'INVESTIGATION',
 'covers': ['KS3.B.INH.04'],
 'touches': ['KS3.B.INH.02', 'KS3.WS.EXP.06'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 2}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['sampling-an-ecosystem', 'life-processes'],
 'assumes': [],
 'references': ['chromosomes-genes-and-dna',
                {'unit': 'B11', 'lesson': 'variation-and-competitive-success'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Normal distributions, polygenic inheritance, and separating genetic from '
                'environmental causes using twin and adoption studies.',
 'big_question': 'Some differences between people run along a smooth scale and others fall into '
                 'separate groups. What decides which kind a characteristic is?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Four piles', 'done_when': 'committed'},
          {'anchor': 's-bench', 'short': 'BENCH', 'label': 'Plot it', 'done_when': 'three_plotted'},
          {'anchor': 's-two',
           'short': 'TWO',
           'label': 'Two questions',
           'mirrors': 's-bench',
           'done_when': 'three_plotted'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'One class, lined up two ways.',
                'prompt': 'Line your class up by height and the line runs smoothly from shortest '
                          'to tallest. Sort the same class by blood group and you get four '
                          'separate piles: A, B, AB and O.',
                'commit': 'If you had to guess, is the number of pets each pupil has more like '
                          'height, or more like blood group?',
                'options': ['More like height', 'More like blood group'],
                'reveal': 'Being a number is not the test. What matters is whether any value can '
                          'sit in between. Next: predict the graph for six characteristics, then '
                          'plot the data.',
                'guess': True,
                'replies': ['It is a number. But nobody has two and a half pets: the counts jump '
                            'from two to three, so they fall into separate piles.',
                            'Pets are counted, and nobody has two and a half of them. Nothing sits '
                            'between two and three, so the counts fall into separate piles.'],
                'answer': 1},
 'misconceptions': [{'id': 'GENE-01',
                     'statement': 'Continuous variation is caused by the environment; '
                                  'discontinuous variation is genetic.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'},
                    {'id': 'GENE-02',
                     'statement': 'If you can measure it with a ruler it is continuous.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'variation',
                 'definition': 'The differences between individuals of the same species.',
                 'note': 'Every characteristic you can measure or record has some.'},
                {'term': 'continuous variation',
                 'definition': 'Variation with values that grade into one another, so any value '
                               'between two others is possible.',
                 'note': 'Height, mass, hand span. Plotted as a histogram.'},
                {'term': 'discontinuous variation',
                 'definition': 'Variation that falls into separate groups with no values in '
                               'between.',
                 'note': 'Blood group, tongue rolling. Plotted as a bar chart.'},
                {'term': 'histogram',
                 'definition': 'A graph whose bars touch, because the categories are ranges that '
                               'join up.',
                 'note': 'The touching bars are the claim that the values in between exist.'},
                {'term': 'bar chart',
                 'definition': 'A graph whose bars are drawn apart, because the categories really '
                               'are separate.',
                 'note': 'The gap is the claim that nothing sits between them.'},
                {'term': 'characteristic',
                 'definition': 'A feature of an organism that can be measured or recorded.',
                 'note': 'The thing you choose before you can ask either question about it.'}],
 'figures': [{'id': 'b10-height-bars-touching',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'frequency-bars',
              'title': 'A bar chart of student heights, with every bar touching the next',
              'desc': 'A bar chart along the bottom axis showing height in centimetres, grouped '
                      'into seven ranges from 145–150 up to 175–180. The bar for every range is '
                      'drawn touching its neighbours on both sides, with no gap anywhere along the '
                      'axis. The vertical axis counts the number of students in each range, out of '
                      'sixty: 3, 7, 13, 16, 12, 6, then 3, rising to a peak in the middle range '
                      'and falling away on both sides.',
              'caption': 'Height, in centimetres, for sixty students. The bars touch — there is no '
                         'gap between one range and the next.',
              'data': {'bins': [{'label': '145–150', 'n': 3},
                                {'label': '150–155', 'n': 7},
                                {'label': '155–160', 'n': 13},
                                {'label': '160–165', 'n': 16},
                                {'label': '165–170', 'n': 12},
                                {'label': '170–175', 'n': 6},
                                {'label': '175–180', 'n': 3}],
                       'x_label': 'height',
                       'x_unit': 'cm',
                       'y_label': 'number of students',
                       'touching': True}}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'predict-the-graph-then-plot-it', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-two',
           'eyebrow': 'Two questions, asked separately',
           'statement': 'What shape is it, and what caused it.',
           'cards': [{'role': 'Question one · shape',
                      'name': 'Continuous',
                      'body': 'Any value between the extremes is possible. Plotted as a histogram '
                              'with the bars touching, because the categories are ranges that join '
                              'up.',
                      'examples': 'Height, mass, hand span, leaf length'},
                     {'role': 'Question one · shape',
                      'name': 'Discontinuous',
                      'body': 'Separate categories with no values in between. Plotted as a bar '
                              'chart with gaps, because the categories really are separate.',
                      'examples': 'Blood group, eye colour, tongue rolling, number of siblings'},
                     {'role': 'Question two · cause',
                      'name': 'Genes',
                      'body': 'Inherited from your parents and fixed at conception. Nothing you do '
                              'changes it, and you can pass it on.',
                      'examples': 'Blood group, eye colour, natural hair colour'},
                     {'role': 'Question two · cause',
                      'name': 'Environment, or both',
                      'body': 'Shaped by food, exercise, illness, sunlight or accident. Most '
                              'characteristics are both: genes set a range and the environment '
                              'decides where in it you land.',
                      'examples': 'Height, mass, scars, language spoken'}],
           'key_fact': {'ref': 'shape-and-cause-are-two-questions', 'ground': 'card'}},
          {'type': 'figure', 'ref': 'b10-height-bars-touching', 'anchor': 's-height-chart'},
          {'type': 'misconception',
           'id': 'shape-is-not-cause',
           'anchor': 's-think',
           'targets': 'GENE-01'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'shape-and-cause-are-two-questions',
                'text': 'Continuous variation has intermediate values and is plotted as a '
                        'histogram; discontinuous variation falls into separate groups and is '
                        'plotted as a bar chart. Whether variation is continuous is a question '
                        'about the data. What caused it — genes, environment or both — is a '
                        'separate question with a separate answer.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'shape-is-not-cause',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'GENE-01',
                 'statements': [{'quote': 'Continuous variation is caused by the environment; '
                                          'discontinuous variation is genetic.',
                                 'body': ['Height is the counter-example that settles it: it is '
                                          'continuous, and it is one of the most strongly '
                                          'inherited characteristics there is — tall parents have '
                                          'tall children with great reliability — while also being '
                                          'affected by childhood nutrition. Both causes, one '
                                          'smooth curve. What actually makes a characteristic '
                                          'continuous is the number of genes involved. Blood group '
                                          'is decided by a single gene with a few versions, so you '
                                          'get a few discrete groups. Height is influenced by '
                                          'hundreds of genes, each contributing a small amount, '
                                          'and hundreds of small contributions added together '
                                          'produce a smooth range with no gaps in it — then the '
                                          'environment moves everyone a little further along. So '
                                          'the honest summary is: <em>one gene tends to give '
                                          'discontinuous variation; many genes tend to give '
                                          'continuous variation</em>; and the environment can '
                                          'adjust anything that is not fixed at conception.']},
                                {'quote': 'If you can measure it with a ruler it is continuous.',
                                 'body': ['Close enough to be dangerous. Number of brothers and '
                                          'sisters is a number, you can count it precisely, and it '
                                          'is discontinuous — nobody has 2.4 siblings, and the '
                                          'average being 2.4 does not make it a possible value for '
                                          'a person. Number of leaves on a plant, number of '
                                          'petals, shoe size in the UK system: all counted, all '
                                          'discontinuous, because the values step rather than '
                                          'flow. The test is not <em>can I put a number on it</em> '
                                          'but <em>can a value exist between two neighbouring '
                                          'values</em>. Between 172 cm and 173 cm there is 172.4 '
                                          'cm and a student who is exactly that; between two and '
                                          'three siblings there is nothing at all. Get that test '
                                          'right and the graph follows automatically: bars that '
                                          'touch for continuous data because the categories are '
                                          'ranges that join up, bars with gaps for discontinuous '
                                          'data because the categories genuinely are separate.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · sixty students, six characteristics',
                 'heading': 'Predict the graph, then plot it',
                 'prompt': 'Data from one year group. The cause line underneath is a separate '
                           'question from the shape.',
                 'options_label': 'Characteristic',
                 'progress_suffix': 'plotted',
                 'characteristics': [{'id': 'height',
                                      'label': 'Height',
                                      'name': 'Height, in centimetres',
                                      'data_type': 'continuous',
                                      'axis': 'height in cm · 60 students · bars touch because the '
                                              'categories are ranges',
                                      'bins': [{'label': '145–150', 'n': 3},
                                               {'label': '150–155', 'n': 7},
                                               {'label': '155–160', 'n': 13},
                                               {'label': '160–165', 'n': 16},
                                               {'label': '165–170', 'n': 12},
                                               {'label': '170–175', 'n': 6},
                                               {'label': '175–180', 'n': 3}],
                                      'shape': 'A smooth hump with no gaps. Every value in the '
                                               'range is possible, and most people are near the '
                                               'middle — which is what the shape of nearly all '
                                               'continuous data looks like.',
                                      'cause': 'Both. Hundreds of genes each contribute a little, '
                                               'and childhood nutrition and health move the whole '
                                               'thing up or down. The clearest example there is of '
                                               'a characteristic with two causes at once.'},
                                     {'id': 'span',
                                      'label': 'Hand span',
                                      'name': 'Hand span, in centimetres',
                                      'data_type': 'continuous',
                                      'axis': 'hand span in cm · 60 students · bars touch because '
                                              'the categories are ranges',
                                      'bins': [{'label': '15–16', 'n': 4},
                                               {'label': '16–17', 'n': 9},
                                               {'label': '17–18', 'n': 15},
                                               {'label': '18–19', 'n': 17},
                                               {'label': '19–20', 'n': 10},
                                               {'label': '20–21', 'n': 5}],
                                      'shape': 'The same hump. Any span between the smallest and '
                                               'largest is possible, so the data has no gaps and '
                                               'the bars have none either.',
                                      'cause': 'Both, and mostly genetic — hand span is closely '
                                               'related to height, which is the same argument one '
                                               'step removed.'},
                                     {'id': 'mass',
                                      'label': 'Body mass',
                                      'name': 'Body mass, in kilograms',
                                      'data_type': 'continuous',
                                      'axis': 'mass in kg · 60 students · bars touch because the '
                                              'categories are ranges',
                                      'bins': [{'label': '35–40', 'n': 5},
                                               {'label': '40–45', 'n': 11},
                                               {'label': '45–50', 'n': 16},
                                               {'label': '50–55', 'n': 14},
                                               {'label': '55–60', 'n': 9},
                                               {'label': '60–65', 'n': 5}],
                                      'shape': 'Continuous, and wider than the height curve. Mass '
                                               'has more room to vary because it responds much '
                                               'more strongly to how someone lives.',
                                      'cause': 'Both, and the environmental share is larger than '
                                               'for height — diet and activity can move an '
                                               'individual a long way, which is why this curve is '
                                               'the broadest of the three.'},
                                     {'id': 'blood',
                                      'label': 'Blood group',
                                      'name': 'Blood group',
                                      'data_type': 'discontinuous',
                                      'axis': 'blood group · 60 students · bars are separated '
                                              'because the categories are',
                                      'bins': [{'label': 'O', 'n': 28},
                                               {'label': 'A', 'n': 25},
                                               {'label': 'B', 'n': 5},
                                               {'label': 'AB', 'n': 2}],
                                      'shape': 'Four separate columns and nothing between them. '
                                               'There is no such thing as being partway between '
                                               'group A and group B, so the bars are drawn apart.',
                                      'cause': 'Genes only. One gene, three versions of it, and '
                                               'nothing you eat, do or experience can change your '
                                               'blood group.'},
                                     {'id': 'tongue',
                                      'label': 'Tongue rolling',
                                      'name': 'Able to roll the tongue',
                                      'data_type': 'discontinuous',
                                      'axis': 'can or cannot · 60 students · two separate '
                                              'categories',
                                      'bins': [{'label': 'Can roll', 'n': 39},
                                               {'label': 'Cannot', 'n': 21}],
                                      'shape': 'Two columns. You either can or you cannot, with no '
                                               'halfway, which makes this the simplest '
                                               'discontinuous characteristic to survey in a '
                                               'classroom.',
                                      'cause': 'Largely genetic, and the textbook version that '
                                               'calls it a single gene is now known to be too '
                                               'simple — identical twins sometimes differ, and '
                                               'some people learn it. A good reminder that a tidy '
                                               'example is usually a simplified one.'},
                                     {'id': 'eyes',
                                      'label': 'Eye colour',
                                      'name': 'Eye colour',
                                      'data_type': 'discontinuous',
                                      'axis': 'recorded colour · 60 students · categories, so the '
                                              'bars are separated',
                                      'bins': [{'label': 'Brown', 'n': 34},
                                               {'label': 'Blue', 'n': 17},
                                               {'label': 'Green or hazel', 'n': 9}],
                                      'shape': 'Recorded as categories, so it is plotted as '
                                               'separate bars — though real eyes grade into one '
                                               'another more than three columns suggest, which is '
                                               'why the categories have to be agreed before the '
                                               'survey starts.',
                                      'cause': 'Genes only, but several genes rather than one. '
                                               'Nothing in the environment changes it, and the old '
                                               'rule that two blue-eyed parents cannot have a '
                                               'brown-eyed child is not reliable.'}],
                 'predict_label': 'Before you plot it — which shape do you expect?',
                 'predict_options': [{'id': 'continuous', 'label': 'Smooth range — continuous'},
                                     {'id': 'discontinuous',
                                      'label': 'Separate groups — discontinuous'}],
                 'kind_lines': {'continuous': 'Continuous — a histogram, bars touching',
                                'discontinuous': 'Discontinuous — a bar chart, bars separated'},
                 'run_label': 'Plot the data',
                 'run_done_label': 'Plotted',
                 'verdicts': {'right': 'Your prediction was right',
                              'wrong': 'Not what you predicted'},
                 'id': 'predict-the-graph-then-plot-it',
                 'kind': 'variation-plotter'}],
 'ladder': {'recall': {'title': 'Rung 1 · Sort them',
                       'q': 'Which of these shows discontinuous variation?',
                       'options': ['Arm length',
                                   'Body mass',
                                   'Number of petals on a flower',
                                   'Length of the leaves on a tree'],
                       'answer': 2,
                       'feedback': {0: 'Arm length can take any value in a range. It is '
                                       'continuous.',
                                    1: 'Body mass can take any value, such as 45.3 kg. It is '
                                       'continuous.',
                                    3: 'Leaf length can take any value in a range. It is '
                                       'continuous.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Height varies continuously. What causes the variation in height?',
                      'options': ['The environment alone, so tall parents never pass height to '
                                  'their children',
                                  'Genes alone, as height is passed on from parents',
                                  'Many genes and the environment together, as diet affects height '
                                  'too',
                                  'No genes at all, since genes only ever give separate groups '
                                  'like blood type'],
                      'answer': 2,
                      'feedback': {0: 'Height is continuous and strongly inherited. Continuous '
                                      'does not mean environmental.',
                                   1: 'Diet in childhood also affects height. So genes alone is '
                                      'wrong.',
                                   3: 'Many genes, each adding a little, give a smooth range like '
                                      'height.'}},
            'explain': {'title': 'Rung 3 · Explain the smooth curve',
                        'q': 'Blood group falls into four sharp categories and height forms a '
                             'smooth curve, although both are strongly influenced by genes. '
                             'Explain the difference, and say what part the environment plays in '
                             'each.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Blood group is controlled by…',
                        'success': ['Says blood group is controlled by a single gene with a small '
                                    'number of versions.',
                                    'Says a single gene therefore produces a small number of '
                                    'distinct categories with nothing in between.',
                                    'Says height is influenced by a large number of genes, each '
                                    'contributing a small amount.',
                                    'Says many small contributions added together produce a smooth '
                                    'range of values.',
                                    'Says the environment — nutrition and health — affects height '
                                    'but has no effect at all on blood group.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'Plan an investigation into variation in leaf length on a single '
                             'tree. Say how you would collect the data, how you would present it, '
                             'and how you would avoid the sampling problem you met in Sampling an '
                             'ecosystem.',
                        'field_label': 'Your plan',
                        'placeholder': 'I would collect leaves…',
                        'success': ['Collects a large enough sample — at least fifty leaves — and '
                                    'says why a small sample is not enough.',
                                    'Chooses the leaves without bias, rather than picking ones '
                                    'that look interesting or are easy to reach.',
                                    'Measures each leaf the same way, from the same points, with a '
                                    'stated precision.',
                                    'Groups the measurements into equal ranges and plots a '
                                    'histogram with touching bars, because the data is continuous.',
                                    'Predicts a hump-shaped curve, and identifies a factor that '
                                    'could shift it — shade, height on the tree, or age of the '
                                    'shoot.']}},
 'key_note': 'Continuous variation has values that grade into one another with no gaps, and is '
             'shown on a histogram with touching bars. Discontinuous variation falls into separate '
             'categories with no intermediates, and is shown on a bar chart with gaps. '
             'Characteristics controlled by one gene tend to be discontinuous; those influenced by '
             'many genes tend to be continuous, and the environment can shift anything that is not '
             'fixed at conception.',
 'stretch': [{'type': 'explainer',
              'id': 'why-the-dutch-got-taller',
              'text': 'Dutch men are now the tallest in the world, averaging around 1.84 m, and in '
                      '1860 they were among the shorter populations in Europe. Twenty centimetres '
                      'in a century and a half is far too fast for the gene pool to have changed '
                      'much — what changed was nutrition, public health and childhood disease. The '
                      'same shift has happened in South Korea and Japan within living memory, and '
                      'it has stalled or reversed in a few countries where nutrition got worse. '
                      'This is the clearest evidence there is that height is genuinely both: the '
                      'ranking within a population is largely inherited, and the level the whole '
                      'population sits at is set by the environment. It also explains a fact you '
                      "can check in any old building — Tudor doorways and the bunks in Nelson's "
                      'navy were not built for shorter people out of some quirk of taste.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to sort a characteristic the bench does not cover?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The sixty-student data set is invented for this lesson, shaped to be '
                    'realistic rather than taken from a real survey. Blood group frequencies are '
                    'approximate UK values. Eye colour is treated as three categories here, which '
                    'is a simplification: eye colour is influenced by several genes and real eyes '
                    'grade into one another more than this bench suggests.',
 'ws': ['analysis-and-evaluation', 'experimental-skills-and-investigations'],
 'review_state': 'draft',
 'authored': True}
