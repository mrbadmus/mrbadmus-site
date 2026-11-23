# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B10 `what-makes-a-species` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B10'
SOURCE_SLUG = 'what-makes-a-species'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'what-makes-a-species',
 'title': 'What makes a species',
 'discipline': 'biology',
 'unit': 'inheritance-and-dna',
 'family': 'CLASSIFY',
 'covers': ['KS3.B.INH.03'],
 'touches': ['KS3.B.INH.04', 'KS3.B.INH.05'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['passing-it-on-heredity', 'variation-continuous-and-discontinuous'],
 'assumes': [],
 'references': [{'unit': 'B11', 'lesson': 'natural-selection'},
                {'unit': 'B1', 'lesson': 'unicellular-organisms'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Speciation, isolation mechanisms, classification systems and the use of DNA '
                'sequencing to work out relationships.',
 'big_question': 'A great dane and a chihuahua look nothing alike, but they are one species. What '
                 'is the test for being the same species?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The mule', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'CASES',
           'label': 'Hard cases',
           'done_when': 'five_cases_opened'},
          {'anchor': 's-test',
           'short': 'TEST',
           'label': 'The test',
           'mirrors': 's-bench',
           'done_when': 'five_cases_opened'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A mule has a horse for a mother and a donkey for a father.',
                'prompt': 'Mules are strong, healthy and long-lived, and they have been bred '
                          'deliberately for four thousand years.',
                'commit': 'If you had to guess, are a horse and a donkey the same species?',
                'options': ['No, two different species', 'Yes, the same species'],
                'reveal': 'Even this test will not settle every pair. Next: seven tricky cases to '
                          'judge, and the last few are ones that biologists still argue about.',
                'guess': True,
                'replies': ['Their mule is healthy, but it almost never has young of its own. To '
                            'be one species, the offspring must be able to have young too.',
                            'They can have a foal together, so it is easy to think so. But a mule '
                            'almost never has young of its own, and that makes a horse and a '
                            'donkey two species.'],
                'answer': 0},
 'misconceptions': [{'id': 'GENE-09',
                     'statement': 'Organisms that look alike are the same species.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'},
                    {'id': 'GENE-10',
                     'statement': 'If two animals can have a baby together, they are the same '
                                  'species.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'species',
                 'definition': 'A group of organisms that can breed together to produce fertile '
                               'offspring.',
                 'note': 'The test is breeding, not appearance.'},
                {'term': 'fertile',
                 'definition': 'Able to reproduce — to produce offspring of its own.',
                 'note': 'The word the definition turns on. A mule is alive and healthy and is not '
                         'fertile.'},
                {'term': 'hybrid',
                 'definition': 'The offspring of two different species, such as a mule or a liger.',
                 'note': 'Usually infertile, which is the evidence that its parents are two '
                         'species.'},
                {'term': 'cryptic species',
                 'definition': 'Two species that look effectively identical and were filed under '
                               'one name until closer study separated them.',
                 'note': "Britain's pipistrelle bats, split on their echolocation frequency."},
                {'term': 'ring species',
                 'definition': 'A chain of populations where each interbreeds with its neighbours, '
                               'but the two ends of the chain do not.',
                 'note': 'The case where the definition gives different answers depending on where '
                         'you apply it.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'same-species-or-not', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-test',
           'eyebrow': 'The test, and where it runs out',
           'statement': 'A good definition that does not cover everything.',
           'cards': [{'role': 'The definition',
                      'name': 'Fertile offspring',
                      'body': 'Two organisms are the same species if they can breed to produce '
                              'offspring that can themselves reproduce. Both words matter: '
                              'offspring, and fertile.'},
                     {'role': 'Where it works',
                      'name': 'Animals that breed sexually',
                      'body': 'Clean and decisive for most animals and many plants, and it '
                              'explains hybrids like the mule without needing an extra rule.'},
                     {'role': 'Where it strains',
                      'name': 'Organisms that do not breed',
                      'body': 'Bacteria divide, many dandelions clone themselves, and fossils '
                              'cannot be bred at all. For these, biologists compare DNA or '
                              'inherited features instead.'},
                     {'role': 'What it is not',
                      'name': 'Looking alike',
                      'body': 'One species can look wildly different individual to individual, and '
                              'two species can be indistinguishable. Appearance is where you '
                              'start, not where you finish.'}],
           'key_fact': {'ref': 'fertile-offspring-is-the-test', 'ground': 'card'}},
          {'type': 'misconception',
           'id': 'looks-alike-and-can-have-a-baby',
           'anchor': 's-think',
           'targets': 'GENE-09'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'fertile-offspring-is-the-test',
                'text': 'Two organisms belong to the same species if they can breed together to '
                        'produce fertile offspring. Members of a species vary enormously in '
                        'appearance; organisms of different species may look almost identical. '
                        'Appearance is a clue, not the test.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'looks-alike-and-can-have-a-baby',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'GENE-09',
                 'statements': [{'quote': 'Organisms that look alike are the same species.',
                                 'body': ['Appearance fails in both directions at once, which is '
                                          'why it cannot be the test. In one direction, a great '
                                          'dane and a chihuahua differ in mass by a factor of '
                                          'forty and are unquestionably one species — every breed '
                                          'of dog is <em>Canis familiaris</em>, and a great dane '
                                          'and a chihuahua are more different in appearance than a '
                                          'wolf and a coyote, which are two species. In the other '
                                          'direction, biologists regularly find <em>cryptic '
                                          'species</em>: populations that are visually identical, '
                                          'that entomologists happily filed under one name for a '
                                          'century, and that turn out on closer study not to '
                                          'interbreed at all. There are pipistrelle bats in '
                                          'Britain that were recognised as two species only when '
                                          'someone noticed they echolocated at different '
                                          'frequencies and never bred with each other. Looking at '
                                          'an organism tells you what to guess. Only breeding '
                                          'tells you the answer.']},
                                {'quote': 'If two animals can have a baby together, they are the '
                                          'same species.',
                                 'body': ['The definition has a second word in it, and it is the '
                                          'one people drop. A lion and a tiger can produce a '
                                          'liger; a horse and a donkey produce a mule; a false '
                                          'killer whale and a bottlenose dolphin have produced '
                                          'offspring in captivity. In each case the hybrid is a '
                                          'real, living, often healthy animal, and in almost every '
                                          'case it cannot reproduce. The reason is usually '
                                          'chromosome number: a horse has 64 chromosomes and a '
                                          'donkey 62, so a mule has 63 — an odd number that cannot '
                                          'be sorted into matching pairs when gametes are made, '
                                          'and the process stalls. So the test is <em>fertile</em> '
                                          'offspring, and hybrids are precisely the evidence that '
                                          'two populations have separated far enough to count as '
                                          'two species. They are not a loophole in the definition; '
                                          'they are how it is applied.']}]},
                {'segment': 'practical',
                 'demand': 'classify',
                 'eyebrow': 'At the bench · seven hard cases',
                 'heading': 'Same species or not?',
                 'prompt': 'Every one of these is chosen because the obvious answer is wrong, or '
                           'because the test itself struggles. Commit before you check — and read '
                           'the last two carefully, because they are the ones biologists still '
                           'argue about.',
                 'progress_suffix': 'settled',
                 'options_label': 'The pair',
                 'cases': [{'id': 'dogs',
                            'label': 'Dane and chihuahua',
                            'answer': 'same',
                            'title': 'A great dane and a chihuahua',
                            'facts': 'A mass difference of about forty times, and skulls so '
                                     'different that a vet can tell the breeds apart from a single '
                                     'bone. Mating them naturally is impractical; with veterinary '
                                     'help the puppies are healthy and can themselves have '
                                     'puppies.',
                            'why': 'One species. Every dog breed is a variety of the same species, '
                                   'and the offspring are fertile — which is the only thing that '
                                   'counts. The pair also demonstrates how far appearance can '
                                   'differ within one species: these two look less alike than a '
                                   'wolf and a coyote, which are two.'},
                           {'id': 'mule',
                            'label': 'Horse and donkey',
                            'answer': 'different',
                            'title': 'A horse and a donkey',
                            'facts': 'They mate readily and produce mules, which are healthy, '
                                     'strong and long-lived. A horse has 64 chromosomes, a donkey '
                                     '62, and a mule 63. Mules are almost always unable to '
                                     'reproduce.',
                            'why': 'Two species. The offspring exists but is infertile, and the '
                                   'reason is visible in the numbers: 63 chromosomes cannot be '
                                   'sorted into pairs when gametes are made. This is the case the '
                                   'definition was written around.'},
                           {'id': 'liger',
                            'label': 'Lion and tiger',
                            'answer': 'different',
                            'title': 'A lion and a tiger',
                            'facts': 'They do not meet in the wild, but in captivity they have '
                                     'produced ligers and tigons. The hybrids are large, and the '
                                     'males are infertile; a few females have had offspring.',
                            'why': 'Two species. The male hybrids are infertile and the animals '
                                   'never breed together in nature. The occasional fertile female '
                                   'is a genuine complication and is the kind of exception that '
                                   'makes biologists talk about how strongly two populations are '
                                   'separated rather than whether they are.'},
                           {'id': 'pipistrelle',
                            'label': 'Two pipistrelles',
                            'answer': 'different',
                            'title': 'Two bats that nobody could tell apart',
                            'facts': 'Common pipistrelles in Britain were treated as one species '
                                     'for a century. In the 1990s researchers noticed two groups '
                                     'echolocating at clearly different frequencies, roosting '
                                     'separately and not interbreeding.',
                            'why': 'Two species, and they look effectively identical — the reverse '
                                   'of the dog case. These are called cryptic species, and DNA '
                                   'work has since found a great many of them. Appearance failed '
                                   'completely here, and the breeding test settled it.'},
                           {'id': 'bacteria',
                            'label': 'Two bacteria',
                            'answer': 'unclear',
                            'title': 'Two bacteria in a petri dish',
                            'facts': 'Bacteria reproduce by dividing in two, not by breeding. They '
                                     'also swap sections of DNA with unrelated bacteria, including '
                                     'ones that would never be called the same species.',
                            'why': 'The test does not settle it, because it asks about breeding '
                                   'and these organisms do not breed. Biologists classify bacteria '
                                   'by comparing DNA sequences and drawing a line at a chosen '
                                   'level of similarity — a line that is useful, agreed, and '
                                   'openly somewhat arbitrary.'},
                           {'id': 'dandelion',
                            'label': 'Two dandelions',
                            'answer': 'unclear',
                            'title': 'Two dandelions on a school field',
                            'facts': 'Most British dandelions produce seed without fertilisation, '
                                     'so each plant produces clones of itself. Botanists have '
                                     'named over two hundred British microspecies.',
                            'why': 'The test does not settle it. With no interbreeding there is '
                                   'nothing for the definition to test, so botanists fall back on '
                                   'consistent inherited differences — and end up with a number of '
                                   'species that depends on how finely they choose to divide.'},
                           {'id': 'gulls',
                            'label': 'A ring of gulls',
                            'answer': 'unclear',
                            'title': 'Herring gulls and lesser black-backed gulls',
                            'facts': 'A chain of gull populations circles the Arctic. Each '
                                     'interbreeds with its neighbours all the way round, but where '
                                     'the two ends meet in Britain, the birds behave as two '
                                     'separate species.',
                            'why': 'The test gives different answers depending on where you apply '
                                   'it, which is not a fault in the gulls. It is what you should '
                                   'expect if species form gradually as populations drift apart — '
                                   'catch the process halfway and there is no sharp line to find. '
                                   'The gull example is also messier than the textbook version, '
                                   'and honest sources say so.'}],
                 'commit_label': 'Same species?',
                 'verdicts': [{'id': 'same', 'text': 'Same species'},
                              {'id': 'different', 'text': 'Different species'},
                              {'id': 'unclear', 'text': 'The test does not settle it'}],
                 'run_label': 'Check it',
                 'run_done_label': 'Settled',
                 'verdict_tags': {'right': 'That is the answer', 'wrong': 'Not quite'},
                 'tally': {'all': 'all seven settled', 'remaining_suffix': 'still to settle'},
                 'id': 'same-species-or-not',
                 'kind': 'species-cases'}],
 'ladder': {'recall': {'title': 'Rung 1 · Apply the definition',
                       'q': 'Two birds mate and produce healthy chicks. The chicks grow up and are '
                            'unable to have young of their own. Are the two parent birds the same '
                            'species?',
                       'options': ['Yes, they had offspring, so the parents count as one species',
                                   'No, the offspring must be fertile for the parents to be one '
                                   'species',
                                   'Yes, if the chicks look like both parents, as looks decide the '
                                   'species',
                                   'It cannot be decided, as one infertile brood proves nothing '
                                   'either way'],
                       'answer': 1,
                       'feedback': {0: 'Having offspring is only half the test. The offspring must '
                                       'be fertile.',
                                    2: 'Looks do not decide a species. A mule looks like both its '
                                       'parents.',
                                    3: 'Healthy but infertile offspring is the sign of two '
                                       'species.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A great dane and a chihuahua look nothing alike. Why are they the same '
                           'species?',
                      'options': ['Because they are both called dogs',
                                  'Because their puppies can grow up and have puppies',
                                  'Because they have exactly the same DNA',
                                  'Because they live in the same homes and eat the same food'],
                      'answer': 1,
                      'feedback': {0: 'A name is something people chose. The test is fertile '
                                      'offspring.',
                                   2: 'Dogs do not have identical DNA. That is why breeds look so '
                                      'different.',
                                   3: 'Food has nothing to do with the species test.'}},
            'explain': {'title': 'Rung 3 · Explain the mule',
                        'q': 'Explain why horses and donkeys are classed as two species even '
                             'though they readily produce mules, and use the chromosome numbers in '
                             'your answer.',
                        'field_label': 'Your explanation',
                        'placeholder': 'A horse has 64 chromosomes…',
                        'success': ['States the definition: same species means fertile offspring.',
                                    'Says a horse has 64 chromosomes and a donkey 62, so a mule '
                                    'has 63.',
                                    'Says an odd number cannot be sorted into matching pairs when '
                                    'gametes are made.',
                                    'Concludes the mule cannot produce working gametes and so is '
                                    'almost always infertile.',
                                    'Concludes that horses and donkeys are therefore two species, '
                                    'and notes that producing offspring alone is not enough.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A biologist finds two populations of beetle on either side of a '
                             'mountain range. They look identical. Describe what she would need to '
                             'find out to decide whether they are one species or two, what she '
                             'should do if they cannot be brought together, and why the answer '
                             'might reasonably be "not yet decided".',
                        'field_label': 'Your answer',
                        'placeholder': 'The test is whether they can produce fertile offspring, '
                                       'so…',
                        'success': ['Says the test is whether they can breed together and produce '
                                    'fertile offspring.',
                                    'Proposes bringing them together and observing whether they '
                                    'mate and whether the offspring can then reproduce.',
                                    'Notes that looking identical proves nothing, referring to '
                                    'cryptic species or giving an equivalent reason.',
                                    'Says that if they cannot be bred, comparing DNA is the '
                                    'alternative approach.',
                                    'Explains that populations separated recently may be partway '
                                    'to becoming separate species, so a clear answer may not exist '
                                    'yet.']}},
 'key_note': 'A species is a group of organisms that can breed together to produce fertile '
             'offspring. Appearance is not the test: one species can contain wildly '
             'different-looking individuals, and two species can look identical. Hybrids such as '
             'the mule show two populations have separated far enough to count as different '
             'species. The definition does not work for organisms that never breed sexually, and '
             'for those biologists compare DNA instead.',
 'stretch': [{'type': 'explainer',
              'id': 'ring-species-and-the-line-you-cannot-draw',
              'text': 'Ring species are the case that shows the definition bending in real time. '
                      'Around the Arctic, herring gulls and lesser black-backed gulls form a chain '
                      'of populations that circles the pole. Each population interbreeds happily '
                      'with its neighbours all the way round — but where the two ends of the chain '
                      'meet again, in Britain, they behave as two clearly separate species and do '
                      'not interbreed. There is no point along the ring where you could draw a '
                      'line and say a species ends here. The example has been picked over by '
                      'biologists and the gull case in particular turns out to be messier than the '
                      'textbook version, which is worth knowing too. What it demonstrates is that '
                      'species boundaries are real without being sharp: they are the product of '
                      'populations drifting apart over time, and if you catch one in the middle of '
                      'that process you should expect the definition to strain — which is exactly '
                      'what natural selection predicts.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to test the definition on a pair the bench does not cover?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The seven cases are chosen to stress the definition rather than to illustrate '
                    'it comfortably, and several are genuinely contested among biologists. '
                    'Chromosome numbers are as usually given; hybrid fertility is described as '
                    '"almost always infertile" rather than "always" because rare exceptions are '
                    'recorded, including a small number of fertile female mules.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
