# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B10 `how-we-worked-out-dna` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B10'
SOURCE_SLUG = 'how-we-worked-out-dna'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'how-we-worked-out-dna',
 'title': "How we worked out DNA's structure",
 'discipline': 'biology',
 'unit': 'inheritance-and-dna',
 'family': 'INVESTIGATION',
 'covers': ['KS3.B.INH.02b'],
 'touches': ['KS3.B.INH.02a', 'KS3.B.INH.04'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 2},
             {'id': 'evidence-and-explanation', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['chromosomes-genes-and-dna', 'testing-the-model'],
 'assumes': [],
 'references': ['passing-it-on-heredity',
                {'unit': 'B6', 'lesson': 'substance-misuse-and-decisions'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'The structure of DNA in detail, the history of the model as an example of how '
                'science works, and DNA replication.',
 'big_question': 'Nobody has ever seen a DNA molecule directly. So how did anyone work out its '
                 'shape?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Too small to see',
           'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Build the model',
           'done_when': 'solved'},
          {'anchor': 's-who',
           'short': 'WHO',
           'label': 'Who did what',
           'mirrors': 's-bench',
           'done_when': 'solved'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A molecule far too small to see, worked out in 1953.',
                'prompt': 'DNA is a hundred thousand times thinner than a hair. No microscope of '
                          'the 1950s could resolve it, and no microscope today can show you the '
                          'shape of a single molecule directly. Yet by April 1953 the structure '
                          'was published, and it was right.',
                'commit': 'If you had to guess, was the shape of DNA worked out by one brilliant '
                          'person, or by several teams?',
                'options': ['One brilliant person', 'Several teams together'],
                'reveal': 'Nobody ever saw the molecule: each piece of evidence ruled some shapes '
                          'out. Next: use the evidence of 1952 to build a model of DNA, one '
                          'decision at a time.',
                'guess': True,
                'replies': ['That is how the story is often told. But it took X-ray pictures from '
                            'one lab, chemical measurements from another and model building in a '
                            'third.',
                            'X-ray pictures taken in London, chemical measurements made in New '
                            'York and models built in Cambridge all had to fit together.'],
                'answer': 1},
 'misconceptions': [{'id': 'GENE-05',
                     'statement': 'Watson and Crick discovered DNA.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'},
                    {'id': 'NOS-03',
                     'statement': "A great discovery is one person's flash of insight.",
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'double helix',
                 'definition': 'Two strands wound round each other in a spiral, which is the shape '
                               'of a DNA molecule.',
                 'note': 'Two strands, not one and not three. The width in the X-ray pattern is '
                         'what settled it.'},
                {'term': 'base',
                 'definition': 'One of the four chemical units — A, T, C and G — whose order along '
                               'a DNA strand carries the information.',
                 'note': 'They sit on the inside of the helix, facing each other.'},
                {'term': 'base pairing',
                 'definition': 'The rule that A always pairs with T and C always pairs with G '
                               'across the two strands.',
                 'note': 'Chargaff measured the equal amounts; the pairing rule is what explains '
                         'them.'},
                {'term': 'X-ray diffraction',
                 'definition': 'Firing X-rays at a substance and reading the pattern they scatter '
                               'into, which can be worked backwards to the arrangement of atoms '
                               'that produced it.',
                 'note': 'Not a photograph of the molecule. Photo 51 is a pattern of spots, not a '
                         'picture.'},
                {'term': 'crystallography',
                 'definition': 'The science of working out how atoms are arranged in a solid from '
                               'the way it scatters X-rays.',
                 'note': "Franklin's field, and one of the hardest kinds of measurement there is."},
                {'term': 'model',
                 'definition': 'A representation of something built so it can be tested against '
                               'evidence and thrown away if it fails.',
                 'note': "Watson and Crick built theirs out of metal. Pauling's was wrong, and "
                         'that was still useful.'}],
 'figures': [{'id': 'b10-base-pairs',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'base-pairs',
              'title': 'How the bases pair across the two strands of DNA, and the same ladder '
                       'twisted',
              'desc': 'On the left, two backbones running down the sides with five rungs between '
                      'them. Each rung is one base from the left strand meeting one from the '
                      'right: A with T, T with A, C with G, G with C, and A with T again. A and G '
                      'are drawn wide and C and T narrow, because A and G are the big bases and C '
                      'and T the small ones. Every rung pairs a big base with a small one, so '
                      'every rung comes to the same width. That width is measured twice, by a '
                      'dimension line drawn straight across the first rung and another drawn '
                      'straight across the last — both the same length, both starting and '
                      'finishing at the same two points. On the right the same ladder is drawn '
                      'again with the twist put back into it: the two backbones wind round each '
                      'other as a double helix with rungs running between them all the way down, '
                      'and two dashed lines mark the widest points of the spiral with a third '
                      'dimension line measured across them. That third measurement is the same '
                      'length as the two on the ladder, because the width of the twisted molecule '
                      'is its diameter and the ladder is what sets it. It is the constant width '
                      'measured from the diffraction images on this page.',
              'caption': 'The reason is width. Every rung is one big and one small and every rung '
                         'comes out the same length. Two big bases would bulge; two small ones '
                         'would pinch — and twisting the ladder up into the shape you already know '
                         'does not change it, because that width has become the width of the '
                         'spiral.',
              'data': {'rungs': [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C'), ('A', 'T')],
                       'guide_label': 'every rung the same width'}}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'build-a-model-that-fits-all-of-it', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-who',
           'eyebrow': 'Who did what',
           'statement': 'Four names, two laboratories, one structure.',
           'cards': [{'initials': 'RF',
                      'name': 'Rosalind Franklin',
                      'role': 'King’s College London · X-ray crystallography',
                      'body': 'Produced the diffraction images, including Photo 51 with her '
                              'student Raymond Gosling, and calculated from them that the molecule '
                              'was a helix of a particular width with the phosphates on the '
                              'outside. Hers is the evidence the model had to fit.'},
                     {'initials': 'MW',
                      'name': 'Maurice Wilkins',
                      'role': 'King’s College London · X-ray crystallography',
                      'body': 'Began the X-ray work on DNA and continued it alongside Franklin, in '
                              'a working relationship that was difficult from the start. He showed '
                              'Photo 51 to Watson.'},
                     {'initials': 'EC',
                      'name': 'Erwin Chargaff',
                      'role': 'Columbia University · biochemistry',
                      'body': 'Measured the amounts of the four bases in DNA from many species and '
                              'found the equalities that carry his name — without proposing what '
                              'they meant. The pairing rule was sitting in his tables for three '
                              'years.'},
                     {'initials': 'WC',
                      'name': 'Watson and Crick',
                      'role': 'Cambridge · model building',
                      'body': 'Built physical models and tested them against everyone else’s '
                              'measurements until one fitted all of them. They did no experiments '
                              'on DNA themselves, which is not a criticism — model building is a '
                              'legitimate method, and it was the right one here.'}],
           'key_fact': {'ref': 'dna-is-a-double-helix', 'ground': 'card'}},
          {'type': 'figure', 'ref': 'b10-base-pairs', 'anchor': 's-pairs'},
          {'type': 'misconception',
           'id': 'who-discovered-what',
           'anchor': 's-think',
           'targets': 'GENE-05'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'dna-is-a-double-helix',
                'text': 'DNA is a double helix: two strands twisted round each other, with the '
                        'bases paired on the inside — A always with T, C always with G. The '
                        'structure was deduced in 1953 from X-ray diffraction images taken by '
                        "Rosalind Franklin and Maurice Wilkins, and from Erwin Chargaff's base "
                        'ratios, by James Watson and Francis Crick.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'who-discovered-what',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'GENE-05',
                 'statements': [{'quote': 'Watson and Crick discovered DNA.',
                                 'body': ['DNA was discovered in 1869 by Friedrich Miescher, who '
                                          'isolated it from the pus on used surgical bandages and '
                                          'called it nuclein — eighty-four years before 1953. By '
                                          'the 1940s Avery, MacLeod and McCarty had shown it was '
                                          'the material carrying inherited information, which was '
                                          'the genuinely surprising result, since most biochemists '
                                          'had assumed the genetic material must be protein. What '
                                          'Watson and Crick worked out was the <em>structure</em>, '
                                          "and even that was model-building from other people's "
                                          'measurements: they did no experiments on DNA '
                                          'themselves. Getting this right is not pedantry about '
                                          'credit. It is the difference between imagining science '
                                          'as a series of individual discoveries and understanding '
                                          'it as what it is — a slow accumulation where the person '
                                          'who assembles the final piece is standing on twenty '
                                          "years of other people's work."]},
                                {'quote': "A great discovery is one person's flash of insight.",
                                 'body': ['Look at what 1953 actually required. Franklin and '
                                          "Wilkins produced the diffraction images at King's "
                                          'College London and Franklin calculated the measurements '
                                          'from them. Chargaff, in New York, had published the '
                                          'base ratios years earlier without seeing what they '
                                          'meant. Linus Pauling in California published a '
                                          'triple-helix model that was wrong, which mattered, '
                                          'because ruling out a serious rival narrows the field. '
                                          'Watson and Crick built physical models in Cambridge and '
                                          "tested them against everyone else's numbers until one "
                                          'fitted. Five laboratories, three countries, two '
                                          'decades. The flash-of-insight story survives because it '
                                          'is easier to tell, and it gives students a false '
                                          'picture of what doing science looks like: mostly it '
                                          'looks like checking whether your idea is consistent '
                                          "with someone else's data."]}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · the evidence available in 1952',
                 'heading': 'Build a model that fits all of it',
                 'prompt': 'Three decisions to make, and four pieces of evidence that each rule '
                           'something out. Exactly one combination survives all four — which is '
                           'what Watson and Crick were doing with pieces of cardboard and bent '
                           'metal.',
                 'dials': [{'id': 'strands',
                            'name': 'How many strands',
                            'options': [{'id': '1', 'label': 'One', 'phrase': 'A single strand'},
                                        {'id': '2', 'label': 'Two', 'phrase': 'Two strands'},
                                        {'id': '3', 'label': 'Three', 'phrase': 'Three strands'}]},
                           {'id': 'bases',
                            'name': 'Where the bases sit',
                            'options': [{'id': 'in',
                                         'label': 'Inside, facing each other',
                                         'phrase': 'bases on the inside'},
                                        {'id': 'out',
                                         'label': 'Outside, facing the water',
                                         'phrase': 'bases on the outside'}]},
                           {'id': 'pairing',
                            'name': 'How the bases pair',
                            'options': [{'id': 'specific',
                                         'label': 'A with T, C with G',
                                         'phrase': 'A with T and C with G'},
                                        {'id': 'any',
                                         'label': 'Any base with any base',
                                         'phrase': 'any base with any base'}]}],
                 'start': {'strands': '3', 'bases': 'out', 'pairing': 'any'},
                 'correct': {'strands': '2', 'bases': 'in', 'pairing': 'specific'},
                 'evidence': [{'id': 'photo',
                               'name': 'Photo 51 · Franklin and Gosling, 1952',
                               'what': 'An X-ray diffraction image of DNA fibres. The cross-shaped '
                                       'pattern of spots is the signature of a helix, and the '
                                       'spacing of the spots gives its width and the distance per '
                                       'turn.',
                               'why': 'The measured width does not fit this. A single strand is '
                                      'too narrow and three strands are too wide — the pattern '
                                      'says two.',
                               'requires': {'strands': '2'}},
                              {'id': 'water',
                               'name': 'Franklin’s water measurements',
                               'what': 'DNA takes up a great deal of water, which means its '
                                       'water-attracting parts — the phosphate groups — must be on '
                                       'the outside of the molecule, in contact with it.',
                               'why': 'If the bases are on the outside then the phosphates are on '
                                      'the inside, which contradicts the water measurements — and '
                                      'the negative phosphates would repel each other.',
                               'requires': {'bases': 'in'}},
                              {'id': 'chargaff',
                               'name': 'Chargaff’s ratios, 1950',
                               'what': 'In DNA from any organism, the amount of A always equals '
                                       'the amount of T, and the amount of C always equals the '
                                       'amount of G — while the ratio of A to C varies from '
                                       'species to species.',
                               'why': 'If any base could pair with any other there would be no '
                                      'reason for A and T to come in equal amounts in every '
                                      'organism ever measured.',
                               'requires': {'pairing': 'specific'}},
                              {'id': 'pauling',
                               'name': 'Pauling’s triple helix, early 1953',
                               'what': 'The most respected chemist alive published a model with '
                                       'three strands and the bases facing outwards. It was wrong, '
                                       'and seeing why it was wrong narrowed the field for '
                                       'everyone else.',
                               'why': 'This is Pauling’s model, and it has already been ruled out. '
                                      'Its phosphates were crowded into the centre where their '
                                      'negative charges would push the molecule apart.',
                               'forbids': {'strands': '3', 'bases': 'out'}}],
                 'verdict_tags': {'pass': 'Every test passed',
                                  'fail_one': '{n} test still failing',
                                  'fail_many': '{n} tests still failing'},
                 'verdicts': {'pass': 'Two strands, bases paired on the inside, A with T and C '
                                      'with G. This is the only combination on the bench that '
                                      'survives all four pieces of evidence, and it is the '
                                      'structure published in April 1953. Notice what just '
                                      'happened: the evidence did not show you the answer — it '
                                      'eliminated everything else.',
                              'fail': 'Each failing test is telling you which decision to change, '
                                      'and none of them requires you to know the answer in advance '
                                      '— which is exactly the position everyone was in during '
                                      '1952.'},
                 'progress_suffix': 'tests passed',
                 'id': 'build-a-model-that-fits-all-of-it',
                 'kind': 'model-builder'}],
 'ladder': {'recall': {'title': 'Rung 1 · What the evidence showed',
                       'q': 'What did Chargaff’s ratios contribute to the model?',
                       'options': ['That DNA is a helix, because its base amounts repeat regularly',
                                   'That there are two strands, because there are two pairs of '
                                   'bases',
                                   'That the phosphates are on the outside, because he measured '
                                   'whole molecules',
                                   'That A pairs with T and C with G, because the amounts match'],
                       'answer': 3,
                       'feedback': {0: "The helix came from Franklin's X-ray pattern. Chargaff "
                                       'measured amounts of bases.',
                                    1: 'The number of strands came from the X-ray measurements of '
                                       'width.',
                                    2: "The backbones being outside came from Franklin's "
                                       'measurements.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'What did Watson and Crick do in 1953 to help us understand DNA?',
                      'options': ["They worked out its shape by building models to fit others' "
                                  'data',
                                  'They discovered DNA by finding it inside cells for the first '
                                  'time',
                                  'They proved DNA carries genetic information, using experiments '
                                  'on bacteria',
                                  'They took the X-ray photographs that showed DNA is a double '
                                  'helix'],
                      'answer': 0,
                      'feedback': {1: 'DNA was found in 1869, by Friedrich Miescher.',
                                   2: "Avery's team showed that in 1944, before the model was "
                                      'built.',
                                   3: "Franklin and Gosling took the X-ray images at King's "
                                      'College London.'}},
            'explain': {'title': 'Rung 3 · Match evidence to conclusion',
                        'q': 'For each of the three features of the DNA model — two strands, bases '
                             'on the inside, and A pairing with T — say which piece of evidence '
                             'established it and how.',
                        'field_label': 'Your answer',
                        'placeholder': 'The two strands came from…',
                        'success': ['Links the two strands to the X-ray diffraction pattern, and '
                                    'says the spacing gave the width.',
                                    'Says the cross-shaped pattern in the image showed the '
                                    'molecule was a helix.',
                                    'Links the bases being on the inside to Franklin’s water '
                                    'measurements and the phosphates being outside.',
                                    'Links the A-with-T and C-with-G pairing to Chargaff’s ratios.',
                                    'Explains why equal amounts of A and T in every species '
                                    'implies they must pair with each other.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'The 1953 paper acknowledged only that the authors had been '
                             '"stimulated by" unpublished results from King’s College. Using what '
                             'you know about how the structure was worked out, write what you '
                             'think a fair acknowledgement would have said — and explain what rule '
                             'about using other people’s data you would draw from this episode.',
                        'field_label': 'Your answer',
                        'placeholder': 'A fair acknowledgement would have named…',
                        'success': ['Names Franklin specifically, and what her contribution was — '
                                    'the diffraction images and the measurements taken from them.',
                                    'Notes that the data was seen without her knowledge or '
                                    'permission.',
                                    'Recognises that Watson and Crick’s own contribution — '
                                    'assembling a model that fitted everything — was real and '
                                    'worth credit too.',
                                    'States a general rule, such as: data should be credited to '
                                    'whoever produced it, and used only with their knowledge.',
                                    'Avoids treating the episode as a simple story of heroes and '
                                    'villains — acknowledges that the history is contested or that '
                                    'several factors were involved.']}},
 'key_note': "DNA's structure — a double helix with paired bases inside — was deduced in 1953 from "
             'evidence nobody could see directly. Franklin and Wilkins produced the X-ray '
             "diffraction images; Franklin's measurements showed the helix's dimensions and that "
             "the phosphates lie outside; Chargaff's ratios showed A pairs with T and C with G; "
             'Watson and Crick built the model that fitted all of it. The structure immediately '
             'suggested how DNA could be copied.',
 'stretch': [{'type': 'explainer',
              'id': 'why-the-structure-mattered-so-much',
              'text': 'The paper announcing the structure ran to about a page, and it closed with '
                      'a single sentence, phrased with deliberate understatement, noting that the '
                      'pairing they had proposed immediately suggested a way the material could '
                      'copy itself. That sentence is the reason the structure mattered so much. If '
                      'A always pairs with T and C always with G, then each strand carries the '
                      'full information: unzip the double helix and each half specifies exactly '
                      'what must be built alongside it. A structure that explains, in its own '
                      'geometry, how inheritance can work is a rare thing in science — most '
                      'structures have to have their function worked out afterwards. Five years '
                      'later Meselson and Stahl showed experimentally that copying does happen '
                      'that way, and the model stopped being a proposal.'}],
 'support': [{'type': 'explainer',
              'id': 'a-note-on-the-credit',
              'text': "Photo 51 was taken in Franklin's laboratory by her research student Raymond "
                      'Gosling. It was shown to Watson by Wilkins without her knowledge, and a '
                      'report containing her unpublished measurements reached Crick through a '
                      'research council committee, also without her being asked. Watson and '
                      'Crick\'s 1953 paper acknowledged only that they had been "stimulated by" '
                      "unpublished results from King's. Franklin died of ovarian cancer in 1958, "
                      'aged 37, probably from her exposure to X-rays; the Nobel Prize was awarded '
                      'to Watson, Crick and Wilkins in 1962, and the rules do not allow it to be '
                      'given posthumously. Historians still argue about how much of this was '
                      'ordinary scientific rivalry, how much was the treatment of a woman in a '
                      "hostile department, and how much was the Nobel's own rules. What is not in "
                      'dispute is that the data were used without permission and that the '
                      'acknowledgement understated what was owed.'}],
 'support_heading': 'A note on the credit',
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to talk through what Photo 51 actually shows?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The bench is a simplification of a two-year argument into three decisions and '
                    'four tests. The real work involved crystallography mathematics well beyond '
                    'this level, several intermediate wrong models by everyone concerned, and '
                    'evidence not listed here. The historical account in the credit note follows '
                    'the mainstream of what historians of science have established; several '
                    'details remain contested.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
