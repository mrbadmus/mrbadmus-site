# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B11 `variation-and-competitive-success` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B11'
SOURCE_SLUG = 'variation-and-competitive-success'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'variation-and-competitive-success',
 'title': 'Variation and competitive success',
 'discipline': 'biology',
 'unit': 'evolution-extinction-and-biodiversity',
 'family': 'SYSTEM',
 'covers': ['KS3.B.INH.05a'],
 'touches': ['KS3.B.INH.05b', 'KS3.B.INH.06'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 3}, {'id': 'structure-function', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['variation-continuous-and-discontinuous', 'predator-and-prey'],
 'assumes': [],
 'references': ['natural-selection',
                'leaves-built-for-the-job',
                'when-the-environment-changes-extinction'],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Selection pressures, adaptation, and the evidence for evolution from the fossil '
                'record and from living populations.',
 'big_question': 'No two individuals in a population are identical. Most of the time that is a '
                 'curiosity. When something goes wrong — a drought, a cold winter, a new predator '
                 '— it becomes the most important fact about them.',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Until it is not',
           'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Change the world',
           'done_when': 'three_conditions_seen'},
          {'anchor': 's-three',
           'short': 'COMPETE',
           'label': 'Competing for',
           'mirrors': 's-bench',
           'done_when': 'three_conditions_seen'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'A thick coat is an advantage. Until it is not.',
                'prompt': 'Two mice in the same litter, one with a noticeably thicker coat. Which '
                          'of them does better depends entirely on what happens next — and the '
                          'same is true of every difference between them: size, speed, appetite, '
                          'colour, boldness.',
                'commit': 'If you had to guess, in a long drought, which mouse is more likely to '
                          'survive: a big, strong one, or a small, quick one?',
                'options': ['The big, strong one', 'The small, quick one'],
                'reveal': 'No difference is best everywhere; it depends on the conditions. Next: '
                          'put the same five mice through five different conditions.',
                'guess': True,
                'replies': ['Strength sounds as if it should win, and in a fight it might. But a '
                            'big body needs more water and more food, and in a drought there is '
                            'neither.',
                            'A small body needs little water and cools easily, so it copes best '
                            'when the water runs out. Size has become a cost, not an asset.'],
                'answer': 1},
 'misconceptions': [{'id': 'EVOL-01',
                     'statement': 'Survival of the fittest means the strongest survive.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'},
                    {'id': 'EVOL-02',
                     'statement': 'Some individuals are just better than others.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'competition',
                 'definition': 'Two or more organisms needing the same limited resource, so that '
                               'one getting it means another does not.',
                 'note': 'Usually fiercest between members of the same species, because they need '
                         'exactly the same things.'},
                {'term': 'resource',
                 'definition': 'Something an organism needs and there is not enough of: food, '
                               'water, space, shelter, a mate.',
                 'note': 'More are born than the resources can support. That is what makes it a '
                         'competition.'},
                {'term': 'advantage',
                 'definition': 'A variation that makes an individual more likely to survive and '
                               'reproduce in the conditions it is actually in.',
                 'note': 'Always in some conditions. There is no such thing as an advantage in '
                         'general.'},
                {'term': 'adapted',
                 'definition': 'Suited to a particular environment by the variations an organism '
                               'happens to have.',
                 'note': 'Biologists say well adapted to a place, never advanced or superior.'},
                {'term': 'fitness',
                 'definition': 'How well an individual is fitted to its current conditions, '
                               'counted by how many surviving offspring it leaves.',
                 'note': 'Nothing to do with strength or with how long an organism lives.'},
                {'term': 'environment',
                 'definition': 'Everything around an organism that affects it: the weather, the '
                               'ground, the food, the predators, the other members of its own '
                               'species.',
                 'note': 'Change it and the ranking changes with it.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'change-the-world-not-the-mice', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-three',
           'eyebrow': 'What they are competing for',
           'statement': 'More are born than can possibly survive.',
           'cards': [{'role': 'Between members of one species',
                      'name': 'Food and water',
                      'body': 'The most common competition, and the one that bites first. Every '
                              'organism eating the same thing in the same place is a rival.'},
                     {'role': 'Between members of one species',
                      'name': 'Space and shelter',
                      'body': 'Territory, a burrow, a nest site, a place on the rock. Often more '
                              'limiting than food, and usually settled by size or by who arrived '
                              'first.'},
                     {'role': 'Between members of one species',
                      'name': 'Mates',
                      'body': 'Only some individuals breed. This is where fitness is finally '
                              'counted, because surviving without reproducing contributes nothing '
                              'to the next generation.'},
                     {'role': 'Against everything else',
                      'name': 'Predators and disease',
                      'body': 'Not competition exactly, but the same filter: whichever variations '
                              'happen to help you avoid being eaten or infected are the ones that '
                              'get passed on.'}],
           'key_fact': {'ref': 'no-generally-superior-individual', 'ground': 'card'}},
          {'type': 'misconception',
           'id': 'fittest-is-not-strongest',
           'anchor': 's-think',
           'targets': 'EVOL-01'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'no-generally-superior-individual',
                'text': 'Individuals of a species vary, and resources are limited, so some compete '
                        'more successfully than others. Which variation gives an advantage depends '
                        'entirely on the conditions, and the conditions change — so there is no '
                        'such thing as a generally superior individual.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'fittest-is-not-strongest',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'EVOL-01',
                 'statements': [{'quote': 'Survival of the fittest means the strongest survive.',
                                 'body': ['Fittest here means <em>best fitted to these '
                                          'conditions</em>, in the sense that a key fits a lock — '
                                          'not fittest in the sense of a gym. It is regularly the '
                                          'small, the drab and the unimpressive that come through. '
                                          'In a drought, the animal that needs least water wins; '
                                          'in a famine, the one that survives on least food; '
                                          'against a new disease, the one that happens to be '
                                          'resistant, which may be the sickliest animal in the '
                                          'group in every other respect. A stag with enormous '
                                          'antlers wins fights and starves in a hard winter '
                                          'carrying them. And the measure is not survival at all '
                                          'in the end — it is how many surviving offspring an '
                                          'individual leaves. An organism that lives fifty years '
                                          'and never breeds has a fitness of zero; a mayfly that '
                                          'lives one day and lays five hundred eggs has done '
                                          'everything that counts.']},
                                {'quote': 'Some individuals are just better than others.',
                                 'body': ['Better at what, and in what conditions? Change the '
                                          'environment on the bench above and the ranking '
                                          'reshuffles, using the same five animals with the same '
                                          'five sets of characteristics. A large mouse dominates a '
                                          'food pile and needs more of it; a bold mouse finds new '
                                          'food first and meets the owl first; a thick coat is '
                                          'life in January and a burden in July. This is why '
                                          'biologists are careful to say <em>well adapted to a '
                                          'particular environment</em> rather than '
                                          '<em>advanced</em> or <em>superior</em>, and it is not a '
                                          'politeness. A species that is superbly suited to one '
                                          'place is, by that same specialisation, badly placed if '
                                          'the place changes — which is precisely how extinctions '
                                          'happen, and it is the subject of When the environment '
                                          'changes: extinction.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · one population, five conditions',
                 'heading': 'Change the world, not the mice',
                 'prompt': 'The same five mice every time. Only the conditions change. Watch one '
                           'mouse across all five and see how often the same animal is at the top '
                           'and at the bottom.',
                 'tabs_label': 'The conditions',
                 'progress_suffix': 'conditions tried',
                 'best_suffix': ' · best here',
                 'worst_suffix': ' · worst here',
                 'subjects': [{'id': 'big', 'name': 'Large, heavy build'},
                              {'id': 'thick', 'name': 'Thick coat'},
                              {'id': 'fast', 'name': 'Small and quick'},
                              {'id': 'bold', 'name': 'Bold and exploratory'},
                              {'id': 'pale', 'name': 'Pale sandy fur'}],
                 'envs': [{'id': 'winter',
                           'label': 'A hard winter',
                           'name': 'A hard winter, snow for eight weeks',
                           'note': 'Food is scarce and buried, and the cold is relentless. Losing '
                                   'heat is now the main way to die.',
                           'chances': {'big': 70, 'thick': 90, 'fast': 45, 'bold': 55, 'pale': 75},
                           'whys': {'big': 'A large body loses heat more slowly than a small one, '
                                           'and fat reserves last. It also needs more food, which '
                                           'is scarce.',
                                    'thick': 'Insulation is exactly what this winter demands, and '
                                             'it costs almost nothing to carry.',
                                    'fast': 'A small body loses heat fast relative to its mass, '
                                            'and speed is no defence against cold.',
                                    'bold': 'Willing to search further for buried food, which '
                                            'helps — and is exposed to the cold while doing it.',
                                    'pale': 'Pale fur against snow is difficult for an owl to see, '
                                            'which is worth a great deal in a winter with no '
                                            'cover.'},
                           'verdict': 'The thick coat wins, and it is the mouse that will suffer '
                                      'most in the next environment on the list.'},
                          {'id': 'drought',
                           'label': 'A long drought',
                           'name': 'A long drought, no rain for months',
                           'note': 'Water is the limit, and heat is the danger. Every gram of body '
                                   'has to be kept cool and supplied.',
                           'chances': {'big': 40, 'thick': 25, 'fast': 85, 'bold': 60, 'pale': 70},
                           'whys': {'big': 'A big body needs more water and more food, and there '
                                           'is neither. Size is now a bill rather than an asset.',
                                    'thick': 'The insulation that saved this mouse in winter now '
                                             'traps heat it cannot lose. The worst place on the '
                                             'bench to be.',
                                    'fast': 'Small, light, needs little water and cools easily. '
                                            'The animal that struggled in January is thriving.',
                                    'bold': 'Finds the few remaining water sources, and takes '
                                            'risks doing it.',
                                    'pale': 'Pale fur reflects sunlight and matches dry ground, so '
                                            'it stays cooler and stays hidden.'},
                           'verdict': 'The thick coat has gone from best to worst, and the small '
                                      'quick mouse from worst to best. Nothing about either animal '
                                      'changed.'},
                          {'id': 'owl',
                           'label': 'An owl moves in',
                           'name': 'A barn owl takes up residence',
                           'note': 'A new predator hunting at night by sight and sound. The ground '
                                   'is dark peaty soil.',
                           'chances': {'big': 35, 'thick': 55, 'fast': 80, 'bold': 20, 'pale': 25},
                           'whys': {'big': 'Slower to reach cover and a larger target. Being '
                                           'conspicuous has suddenly become expensive.',
                                    'thick': 'Neither helped nor harmed by the coat. This mouse '
                                             'survives on average.',
                                    'fast': 'Quick to cover and a small target. Speed is worth '
                                            'more tonight than anything else.',
                                    'bold': 'Bold means out in the open more often, which is '
                                            'precisely the wrong habit to have when something is '
                                            'hunting.',
                                    'pale': 'Pale fur on dark peat is the most visible thing in '
                                            'the field. The camouflage that saved it in snow now '
                                            'advertises it.'},
                           'verdict': 'Boldness and pale fur are the liabilities here — and pale '
                                      'fur was an advantage in the snow. The variation has not '
                                      'changed; the background has.'},
                          {'id': 'crowded',
                           'label': 'Overcrowding',
                           'name': 'A mild year, and the population doubles',
                           'note': 'No shortage of weather to worry about — but too many mice, too '
                                   'little food, and constant competition for burrows.',
                           'chances': {'big': 80, 'thick': 50, 'fast': 45, 'bold': 75, 'pale': 50},
                           'whys': {'big': 'Wins direct confrontations over food and burrows. In a '
                                           'crowd, size finally pays for itself.',
                                    'thick': 'No advantage and no cost in a mild year. Average.',
                                    'fast': 'Quick, but repeatedly displaced from food by larger '
                                            'mice. Speed does not win an argument.',
                                    'bold': 'Explores beyond the crowded area and finds unoccupied '
                                            'ground and untouched food.',
                                    'pale': 'Colour is irrelevant to this problem, so this mouse '
                                            'sits in the middle.'},
                           'verdict': 'Size wins where the competition is with your own kind '
                                      'rather than with the weather. Note that the mouse that did '
                                      'badly in the drought is this environment’s winner.'},
                          {'id': 'disease',
                           'label': 'A new disease',
                           'name': 'A virus sweeps through the population',
                           'note': 'Nothing to outrun and nothing to hide from. Resistance is '
                                   'decided by which versions of certain genes an animal happens '
                                   'to carry.',
                           'chances': {'big': 45, 'thick': 45, 'fast': 45, 'bold': 30, 'pale': 45},
                           'whys': {'big': 'No protection. Size is irrelevant to a virus.',
                                    'thick': 'No protection. The coat does nothing here.',
                                    'fast': 'No protection. You cannot outrun an infection.',
                                    'bold': 'Actively worse — more contact with more mice means '
                                            'more chance of catching it.',
                                    'pale': 'No protection, and no penalty.'},
                           'verdict': 'None of the visible variations helps. Whatever decides who '
                                      'survives this is something none of these mice can be seen '
                                      'to have — which is why a population needs variation it is '
                                      'not currently using.'}],
                 'id': 'change-the-world-not-the-mice',
                 'kind': 'advantage-bench'}],
 'ladder': {'recall': {'title': 'Rung 1 · Advantage in context',
                       'q': 'Very pale fur is an advantage in snow and a disadvantage on dark '
                            'soil. What does that show?',
                       'options': ['Pale fur is generally a poor variation to have',
                                   'The mouse can change its fur colour to match the ground it is '
                                   'on',
                                   'Whether a variation is an advantage depends on the environment',
                                   'Camouflage matters more than anything else'],
                       'answer': 2,
                       'feedback': {0: 'Pale fur helps on snow. It is only poor on dark soil.',
                                    1: 'A mouse cannot change its fur. The conditions decide if '
                                       'its fur helps.',
                                    3: 'Camouflage is one advantage. Which one matters depends on '
                                       'the conditions.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'What does "fittest" mean in "survival of the fittest"?',
                      'options': ['The strongest and healthiest individuals, and the ones that win '
                                  'every direct fight',
                                  'The individuals that live the longest, and the ones that avoid '
                                  'dying young',
                                  'The ones best fitted to current conditions, and leaving the '
                                  'most offspring',
                                  'The most advanced or highly evolved, and the ones highest up '
                                  'the tree of life'],
                      'answer': 2,
                      'feedback': {0: 'Strength is one variation. In a drought, the mouse needing '
                                      'least water does best.',
                                   1: 'A long life counts for nothing if the animal never breeds.',
                                   3: 'Biology does not rank species as advanced. Fittest means '
                                      'best suited to conditions.'}},
            'explain': {'title': 'Rung 3 · Explain a reversal',
                        'q': 'On the bench, the thick-coated mouse is the most likely to survive '
                             'the winter and the least likely to survive the drought. Explain both '
                             'results, and say what this means for the idea of a "better" animal.',
                        'field_label': 'Your explanation',
                        'placeholder': 'In winter the thick coat…',
                        'success': ['Says the thick coat reduces heat loss, which is the main '
                                    'danger in a hard winter.',
                                    'Says in a drought the same coat traps heat the animal needs '
                                    'to lose.',
                                    'Makes clear the mouse itself did not change — only the '
                                    'conditions did.',
                                    'Concludes that an advantage is relative to a particular '
                                    'environment.',
                                    'States that there is therefore no generally better '
                                    'individual, only one better suited to current conditions.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'On the disease bench, none of the five visible variations protects '
                             'the mice. Explain why a population still benefits from having lots '
                             'of variation it is not currently using, and what that implies for a '
                             'population reduced to very few individuals.',
                        'field_label': 'Your answer',
                        'placeholder': 'The variation that matters against a new disease…',
                        'success': ['Says the variation that will matter against a future threat '
                                    'cannot be known in advance.',
                                    'Says a population with more variation is more likely to '
                                    'contain some individuals that happen to survive it.',
                                    'Says those survivors pass their versions on, so the '
                                    'population recovers.',
                                    'Says a population reduced to very few individuals has lost '
                                    'most of its variation.',
                                    'Concludes that such a population is much more likely to be '
                                    'wiped out by a change it happens to be unsuited to.']}},
 'key_note': 'Individuals within a species vary, and more offspring are produced than the '
             'resources can support, so they compete — for food, water, space, mates and escape '
             'from predators. Variations that suit the current conditions make an individual more '
             'likely to survive and reproduce. Which variations those are depends on the '
             'conditions, so no variation is an advantage in general.',
 'stretch': [{'type': 'explainer',
              'id': 'the-grants-and-the-finches',
              'text': 'Peter and Rosemary Grant spent forty years measuring finches on Daphne '
                      'Major, a small island in the Galápagos, catching and weighing almost every '
                      'bird on it year after year. In the drought of 1977 the small soft seeds ran '
                      'out and only the large tough ones were left, and the finches with slightly '
                      'deeper, stronger beaks survived at a much higher rate. The average beak '
                      'depth in the population measurably increased in a single generation. Then '
                      'in 1983 came exceptional rains, the small soft seeds returned in abundance, '
                      'and the average beak size went back down. That is the whole of this lesson '
                      'in one data set: the same variation, an advantage in one year and a '
                      'disadvantage six years later, with no bird ever changing its own beak. It '
                      'is also one of the few places where evolution has been watched happening '
                      'rather than reconstructed afterwards.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to test a variation against conditions of your own?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The survival percentages are teaching values chosen to show how the ranking '
                    'changes, not measurements. Real fitness depends on many characteristics at '
                    'once, on chance, and on what the rest of the population is doing; the bench '
                    'isolates one variation per mouse to make the point readable.',
 'ws': ['analysis-and-evaluation'],
 'review_state': 'draft',
 'authored': True}
