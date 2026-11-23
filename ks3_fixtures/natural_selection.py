# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B11 `natural-selection` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B11'
SOURCE_SLUG = 'natural-selection'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'natural-selection',
 'title': 'Natural selection',
 'discipline': 'biology',
 'unit': 'evolution-extinction-and-biodiversity',
 'family': 'PROCESS',
 'covers': ['KS3.B.INH.05b'],
 'touches': ['KS3.B.INH.01', 'KS3.B.INH.02a', 'KS3.B.INH.04'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 3},
             {'id': 'evidence-and-explanation', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['variation-and-competitive-success', 'passing-it-on-heredity'],
 'assumes': [],
 'references': ['when-the-environment-changes-extinction',
                {'unit': 'B10', 'lesson': 'what-makes-a-species'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Darwin and Wallace, the evidence for evolution, speciation, mutation as the '
                'source of new variation, and selective breeding as the contrast case.',
 'big_question': 'Over many generations, a whole species can change its shape. What actually makes '
                 'that happen?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'The giraffe', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Run generations',
           'done_when': 'ten_generations_run'},
          {'anchor': 's-steps',
           'short': 'STEPS',
           'label': 'Five steps',
           'mirrors': 's-bench',
           'done_when': 'ten_generations_run'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Giraffes have long necks. How did that happen?',
                'prompt': "A giraffe's neck is about two metres long, which lets it reach leaves "
                          'that most other animals cannot. Its ancestors had much shorter necks.',
                'commit': 'If you had to guess, how did giraffes end up with such long necks?',
                'options': ['Long-necked giraffes had more babies',
                            'Stretching, then passing it on'],
                'reveal': 'It is the group that changes, one generation at a time. Next: watch it '
                          'happen with pale and dark moths on a tree trunk.',
                'guess': True,
                'replies': ['Some giraffes were born with longer necks than others. In hard times '
                            'they reached more food, so more of them survived to have babies with '
                            'long necks too.',
                            'That was once a leading scientific idea, and it sounds sensible. But '
                            "stretching changes only that one giraffe's body, and its babies are "
                            'not born with the extra length.'],
                'answer': 0},
 'misconceptions': [{'id': 'EVOL-03',
                     'statement': 'Animals change themselves to suit their environment, and pass '
                                  'the change on.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'},
                    {'id': 'EVOL-04',
                     'statement': 'The population needed to change, so it did.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'natural selection',
                 'definition': 'The process by which individuals whose variations suit the '
                               'conditions survive and reproduce more, so those variations become '
                               'more common over generations.',
                 'note': 'It acts on a population. It cannot act on an individual.'},
                {'term': 'adaptation',
                 'definition': 'A feature that makes an organism well suited to where it lives.',
                 'note': 'A feature, not an action — no individual adapts during its own life.'},
                {'term': 'selection pressure',
                 'definition': 'Anything in the environment that makes some variations survive '
                               'better than others.',
                 'note': 'A bird that eats what it can see. Nothing is choosing.'},
                {'term': 'variation',
                 'definition': 'The differences between individuals of the same species.',
                 'note': 'It has to be there before the conditions change, or there is nothing to '
                         'select from.'},
                {'term': 'generation',
                 'definition': 'One complete round of a population being born, surviving and '
                               'reproducing.',
                 'note': 'Almost nothing happens in one. Everything happens in fifty.'},
                {'term': 'inherited',
                 'definition': 'Passed from parents to offspring through their genes.',
                 'note': 'What an organism does during its life is not inherited.'}],
 'figures': [{'id': 'b11-moth-pair',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'moth-pair',
              'title': 'The same two moths on two kinds of bark',
              'desc': 'Two panels side by side, each showing the same pair of moths on a different '
                      'bark. On the left, clean bark mottled with lichen: the pale moth is almost '
                      'invisible against it and the dark moth stands out sharply. On the right, '
                      'bark blackened by soot and marked with vertical streaks: the same pale moth '
                      'now stands out sharply and the same dark moth is almost invisible. Neither '
                      'moth has changed. Only the bark has.',
              'caption': 'Neither moth changed. The bark did. Being found is the whole of the '
                         'disadvantage.',
              'data': {'key': 'Being hard to see is not a property of the moth. It is a property '
                              'of the moth and the background together.',
                       'panels': [{'bark': 'lichen',
                                   'label': 'Clean, lichen-covered bark',
                                   'moths': [{'tone': 'pale',
                                              'label': 'Pale moth',
                                              'note': 'hard to see'},
                                             {'tone': 'dark',
                                              'label': 'Dark moth',
                                              'note': 'easy to see'}]},
                                  {'bark': 'soot',
                                   'label': 'Bark blackened by soot',
                                   'moths': [{'tone': 'pale',
                                              'label': 'Pale moth',
                                              'note': 'easy to see'},
                                             {'tone': 'dark',
                                              'label': 'Dark moth',
                                              'note': 'hard to see'}]}]}}],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'run-the-generations', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-steps',
           'eyebrow': 'The process, in five steps',
           'statement': 'Every step is something you have already met.',
           'cards': [{'num': '1',
                      'name': 'Variation already exists',
                      'body': 'Individuals in the population differ, and the differences are there '
                              'before anything changes. In the moths, pale and dark forms both '
                              'existed long before the factories were built — dark ones were '
                              'simply rare.'},
                     {'num': '2',
                      'name': 'More are born than survive',
                      'body': 'Every population produces far more offspring than the food, space '
                              'and shelter can support, so most of them will not live to breed. '
                              'This is where the competition you met in Variation and competitive '
                              'success comes in.'},
                     {'num': '3',
                      'name': 'Some survive better than others',
                      'body': 'Whichever variations happen to suit the current conditions make '
                              'survival more likely. Nothing is choosing; the environment simply '
                              'kills a higher proportion of one kind.'},
                     {'num': '4',
                      'name': 'Survivors reproduce and pass it on',
                      'body': 'The survivors are the ones that breed, and they pass on the '
                              'versions of the genes they carry — which are, on average, the ones '
                              'that helped them survive. This is heredity doing the work, and you '
                              'met it in Passing it on: heredity.'},
                     {'num': '5',
                      'name': 'Repeat, and the population shifts',
                      'body': 'A small change each generation, accumulated over many generations. '
                              'Nothing dramatic happens in any single generation, and after fifty '
                              'the population looks different.'}],
           'key_fact': {'ref': 'natural-selection-in-four-moves', 'ground': 'card'}},
          {'type': 'figure', 'ref': 'b11-moth-pair', 'anchor': 's-moths'},
          {'type': 'misconception',
           'id': 'nothing-is-trying',
           'anchor': 's-think',
           'targets': 'EVOL-03'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'natural-selection-in-four-moves',
                'text': 'Natural selection: individuals vary; those whose variations suit the '
                        'conditions survive and reproduce more; they pass those variations to '
                        'their offspring; over many generations the population changes. '
                        'Individuals do not change — populations do.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'nothing-is-trying',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'EVOL-03',
                 'statements': [{'quote': 'Animals change themselves to suit their environment, '
                                          'and pass the change on.',
                                 'body': ["This is Lamarck's idea, and it deserves respect rather "
                                          'than mockery: it was a serious scientific theory, it '
                                          'explained the observations available in 1809, and '
                                          'Lamarck was right about the big thing — that species '
                                          'change over time — when most people still thought they '
                                          "did not. It fails on the mechanism. A blacksmith's "
                                          'children are not born with thick arms; a mouse that '
                                          'loses its tail has ordinary tailed offspring; and '
                                          'generations of people cutting their hair has produced '
                                          'nobody born bald. What an organism does during its life '
                                          'does not rewrite the DNA in its gametes, so it cannot '
                                          'be inherited. What natural selection needs instead is '
                                          'variation that is <em>already there</em>, arriving '
                                          'before the environment changes rather than in response '
                                          'to it. The moths on the bench above were not turned '
                                          'dark by soot; some were already dark and the soot '
                                          'changed which ones got eaten.']},
                                {'quote': 'The population needed to change, so it did.',
                                 'body': ['Nothing in this process is aiming at anything. There is '
                                          'no need, no goal, no trying — natural selection is the '
                                          'accumulated arithmetic of who happened to leave more '
                                          'offspring, and it cannot look ahead. The language makes '
                                          'this hard: it is almost impossible to describe '
                                          'evolution without saying a species <em>developed</em> a '
                                          'feature <em>in order to</em> do something, and every '
                                          'one of those phrases smuggles in a purpose that is not '
                                          'there. Watch the wording in the mastery ladder and in '
                                          'your own answers. The consequences of getting it right '
                                          'are real: a population facing a change it has no '
                                          'existing variation for does not conjure one up, it '
                                          'dies, and that is why extinction is common rather than '
                                          'rare. And it is why antibiotic resistance appears '
                                          'within years of a new drug — the resistant bacteria '
                                          'were already in the population before the drug '
                                          'arrived.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · a hundred moths on a tree trunk',
                 'title': 'Run the generations',
                 'intro': 'Pale and dark moths resting on tree bark, hunted by birds that find '
                          'whatever they can see. The population changes while no individual moth '
                          'changes at all.',
                 'tabs_label': 'The tree bark',
                 'barks': [{'id': 'clean',
                            'label': 'Clean, lichen-covered',
                            'pale_surv': 0.85,
                            'dark_surv': 0.45,
                            'note': 'Pale, mottled lichen on the trunks — the state of most '
                                    'woodland before industry, and again in many places today.'},
                           {'id': 'sooty',
                            'label': 'Blackened by soot',
                            'pale_surv': 0.45,
                            'dark_surv': 0.85,
                            'note': 'Soot from coal-burning factories has killed the lichen and '
                                    'darkened the bark, as it did across industrial Britain in the '
                                    'nineteenth century.'},
                           {'id': 'mixed',
                            'label': 'Patchy, partly recovered',
                            'pale_surv': 0.7,
                            'dark_surv': 0.7,
                            'note': 'Some lichen returning, some bark still dark. Neither colour '
                                    'has an advantage, which makes this the control.'}],
                 'gen_label': 'generation ',
                 'gen_zero_label': 'generation 0',
                 'start_pale': 0.9,
                 'reset_pale': 0.5,
                 'history_len': 24,
                 'pale_label': 'Pale',
                 'dark_label': 'Dark',
                 'axis_note': 'pale on top, dark below · one column per generation · oldest on the '
                              'left',
                 'axis_format': 'pale on top, dark below · one column per generation · generations '
                                '{from} to {to}',
                 'one_label': 'One generation',
                 'ten_label': 'Ten generations',
                 'reset_label': 'Start again at fifty-fifty',
                 'notes': {'start': 'Nine moths in ten are pale, which is where the British '
                                    'population started.',
                           'reset': 'Half the moths are pale and half are dark — not where the '
                                    'British population started, but the clearest place to watch a '
                                    'change from.',
                           'control': 'Neither colour has an advantage on patchy bark, so the '
                                      'proportions barely move however long you run it. This is '
                                      'the control: without a difference in survival there is no '
                                      'selection, only a population sitting where it already was.',
                           'dark_high': 'The population is now overwhelmingly dark, and not one '
                                        'moth ever changed colour. Every moth that has ever lived '
                                        'in this simulation was born its colour and died its '
                                        'colour. What moved was the proportion, generation by '
                                        'generation, decided entirely by who was eaten.',
                           'pale_high': 'On clean lichen the pale form is nearly invisible and the '
                                        'dark form stands out, so the population stays pale — or '
                                        'returns to pale, if you have switched back after running '
                                        'it sooty. Selection has no memory and no direction.',
                           'moving': 'The proportions are shifting. Notice how little changes in '
                                     'any single generation and how much has changed after ten — '
                                     'that is the whole reason evolution is hard to see '
                                     'happening.'},
                 'id': 'run-the-generations',
                 'kind': 'selection-runner'}],
 'ladder': {'recall': {'title': 'Rung 1 · What changes',
                       'q': 'After fifty generations on sooty bark, most of the moths are dark. '
                            'What changed?',
                       'options': ['Each moth darkened, because a moth living on sooty bark '
                                   'changes colour to match',
                                   'The proportion of dark moths rose, because dark parents '
                                   'survived to breed',
                                   'The soot stained the moths, because anything resting on a '
                                   'black trunk turns dark',
                                   'The pale moths learned to hide, and passed what they learned '
                                   'to their young'],
                       'answer': 1,
                       'feedback': {0: 'No moth changed colour. Each moth keeps the colour it was '
                                       'born with.',
                                    2: 'Soot does not change the colour a moth is born with. '
                                       'Colour is inherited.',
                                    3: 'Learning is not inherited. Fewer pale moths survived to '
                                       'breed.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Why is "giraffes stretched their necks and passed the extra length to '
                           'their calves" wrong?',
                      'options': ['Because giraffes cannot stretch their necks at all, so there is '
                                  'nothing to pass on',
                                  'Because giraffes do not eat from tall trees, so no stretching '
                                  'ever happened',
                                  'Because necks got shorter, not longer, so the direction in the '
                                  'story is wrong',
                                  "Because stretching does not change the giraffe's genes, so "
                                  'calves cannot inherit it'],
                      'answer': 3,
                      'feedback': {0: 'Giraffes can stretch. Stretching does not change the genes '
                                      'they pass on.',
                                   1: 'Giraffes do feed from tall trees. The idea about '
                                      'inheritance is what is wrong.',
                                   2: 'Giraffe necks did get longer. The question is how that '
                                      'happened.'}},
            'explain': {'title': 'Rung 3 · Explain it properly',
                        'q': 'Explain how a population of mainly pale moths became a population of '
                             'mainly dark moths after the bark was blackened by soot. Use all five '
                             'steps, and be careful not to say the moths changed.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Both pale and dark moths already existed…',
                        'success': ['Says both pale and dark moths already existed before the bark '
                                    'darkened.',
                                    'Says birds could see the pale moths more easily against the '
                                    'dark bark, so more of them were eaten.',
                                    'Says more dark moths therefore survived to reproduce.',
                                    'Says the surviving dark moths passed on the genes for dark '
                                    'colour to their offspring.',
                                    'Says the proportion of dark moths increased over many '
                                    'generations — and does not say that any moth changed '
                                    'colour.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A farmer sprays a pesticide that kills 99% of the insect pests. '
                             'Within three years it barely works at all. Explain what has '
                             'happened, why spraying more of it makes the problem worse, and what '
                             'this shares with the moth bench.',
                        'field_label': 'Your answer',
                        'placeholder': 'A few insects in the original population…',
                        'success': ['Says a few insects in the original population happened to be '
                                    'resistant, before the pesticide was used.',
                                    'Says the pesticide killed the others, leaving the resistant '
                                    'ones with little competition.',
                                    'Says those survivors bred and passed resistance on, so the '
                                    'proportion of resistant insects rose each generation.',
                                    'Says spraying more applies the same selection pressure harder '
                                    'and speeds the process up.',
                                    'Identifies the shared mechanism: existing variation plus a '
                                    'change in what survives, with no individual insect becoming '
                                    'resistant during its life.']}},
 'key_note': 'Natural selection needs four things: variation that already exists in the '
             'population, competition because more are born than can survive, a difference in who '
             'survives and reproduces, and inheritance so the surviving variations are passed on. '
             'Repeat over many generations and the population changes. No individual adapts during '
             'its own life, and the process has no goal.',
 'stretch': [{'type': 'explainer',
              'id': 'how-do-we-know-about-the-moths',
              'text': 'Ask <em>how do we know?</em> about the moths and you get the best answer in '
                      'this book. Bernard Kettlewell tested the idea directly in the 1950s: he '
                      'released marked pale and dark moths into a polluted wood near Birmingham '
                      'and an unpolluted one in Dorset, recaptured what he could, and in each wood '
                      'the better-hidden form came back in greater numbers. It was in every '
                      'textbook within a decade — and then the method was taken apart. He had '
                      'released moths by day, at densities no real wood would hold, and often onto '
                      'exposed trunks, when peppered moths mostly rest higher up beneath branches. '
                      'Those criticisms were fair, and for a while they were reported as though '
                      'the conclusion had fallen with the method. It had not. Michael Majerus '
                      'spent the 2000s running the experiment the way the critics said it should '
                      'be run — moths in natural resting positions, at natural densities, with '
                      'birds watched taking them — and got the same result, more strongly; the '
                      'findings were published in 2012, after his death. That sequence is not an '
                      'embarrassment for science, it is the whole of science in one example. A '
                      'conclusion is only ever as good as the method behind it, so someone attacks '
                      'the method, and a conclusion that survives a better test than the one that '
                      'first produced it is standing on firmer ground than before.'},
             {'type': 'explainer',
              'id': 'antibiotic-resistance-is-this-happening-now',
              'text': 'Antibiotic resistance is natural selection happening fast enough to be a '
                      'public health emergency. In any large population of bacteria a few '
                      'individuals happen to carry a version of a gene that lets them survive a '
                      'particular antibiotic — they were there before the drug was ever used, '
                      'produced by ordinary random mutation. Give the antibiotic and it kills the '
                      'rest, which leaves the resistant few with no competition and an empty '
                      'patient to reproduce into. Bacteria divide every twenty minutes, so a '
                      'population that is almost entirely susceptible in the morning can be almost '
                      'entirely resistant within days. This is exactly the moth bench with the '
                      'generation time reduced from a year to twenty minutes, and it is why '
                      'finishing a course as prescribed, and not demanding antibiotics for a '
                      'virus, are not fussiness. Every use of an antibiotic is a selection '
                      'pressure applied to every bacterium in the person taking it.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to check whether your explanation smuggles in a purpose?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The moth bench is a teaching model: survival differences are fixed '
                    'percentages, the population size is held constant, and there is no mutation, '
                    'migration or chance beyond the survival rates themselves.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
