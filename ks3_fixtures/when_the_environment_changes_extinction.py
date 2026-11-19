# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B11 `when-the-environment-changes-extinction` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B11'
SOURCE_SLUG = 'when-the-environment-changes-extinction'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'when-the-environment-changes-extinction',
 'title': 'When the environment changes: extinction',
 'discipline': 'biology',
 'unit': 'evolution-extinction-and-biodiversity',
 'family': 'SYSTEM',
 'covers': ['KS3.B.INH.06'],
 'touches': ['KS3.B.INH.05b', 'KS3.B.ECO.03'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 3}, {'id': 'interdependence', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['natural-selection', 'disturbing-a-food-web'],
 'assumes': [],
 'references': ['biodiversity-and-gene-banks',
                {'unit': 'B9', 'lesson': 'pollinators-and-food-security'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Causes of extinction, the fossil record as evidence, and the biological and '
                'economic arguments for maintaining biodiversity.',
 'big_question': 'More than nine in ten of all the species that have ever lived are gone. '
                 'Extinction is not a failure of the system — it is the system, and the question '
                 'worth asking is what makes a species vulnerable to it.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Same wood', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Who survives',
           'done_when': 'four_combinations_seen'},
          {'anchor': 's-risk',
           'short': 'RISK',
           'label': 'Four risks',
           'mirrors': 's-bench',
           'done_when': 'four_combinations_seen'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two species meet the same change. One survives it.',
                'prompt': 'A woodland is cleared to half its size. The wood mice are fine within a '
                          'few years. The dormice, living in the same wood, eating from the same '
                          'trees, do not come back. Both faced exactly the same event.',
                'commit': 'If you had to guess, what helps an animal most when its home changes?',
                'options': ['Breeding fast, eating anything', 'Being big, strong and fierce'],
                'reveal': 'A dormouse has one small litter a year and eats only a few foods, which '
                          'is why it did not come back. Next: try four species against five kinds '
                          'of change.',
                'guess': True,
                'replies': ['A fast breeder gets many chances to produce young that suit the new '
                            'home, and an unfussy eater can use whatever food is left.',
                            'Big and strong helps in a fight, but a change to the home is not a '
                            'fight. Slow breeders with fussy diets can run out of options.'],
                'answer': 0},
 'misconceptions': [{'id': 'EVOL-05',
                     'statement': 'Extinction is unnatural — it only happens because of us.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'},
                    {'id': 'EVOL-06',
                     'statement': 'If a species goes extinct, another one just takes its place.',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'extinction',
                 'definition': 'The permanent loss of a species, when the last individual of it '
                               'dies.',
                 'note': 'There is no coming back from it, which is what makes it different from a '
                         'population crash.'},
                {'term': 'specialist',
                 'definition': 'A species that depends on one food, one habitat or one narrow set '
                               'of conditions.',
                 'note': 'Very good at the thing it does, and with nothing to fall back on when '
                         'that thing changes.'},
                {'term': 'generalist',
                 'definition': 'A species that can use many foods and live in many places.',
                 'note': 'Rarely the best at anything, and very hard to get rid of.'},
                {'term': 'genetic variation',
                 'definition': 'The differences in genes between individuals in the same '
                               'population.',
                 'note': 'Selection can only work with variation that is already there.'},
                {'term': 'mass extinction',
                 'definition': "An episode in which a very large share of the world's species dies "
                               'out in a short stretch of geological time.',
                 'note': 'Five are recorded in the fossil record; the largest was at the end of '
                         'the Permian.'},
                {'term': 'background rate',
                 'definition': 'The slow, steady rate at which species go extinct in ordinary '
                               'times.',
                 'note': 'The number current rates are compared against, which is what makes the '
                         'comparison checkable.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'who-survives-what', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-risk',
           'eyebrow': 'What makes a species vulnerable',
           'statement': 'Four properties, and the same four every time.',
           'cards': [{'role': 'Risk factor one',
                      'name': 'Specialist diet or habitat',
                      'body': 'A species that needs one food or one habitat has nothing to fall '
                              'back on when that thing changes. Generalists survive changes that '
                              'wipe out specialists in the same place.'},
                     {'role': 'Risk factor two',
                      'name': 'Slow reproduction',
                      'body': 'Natural selection works through generations. A species producing '
                              'one offspring every two years gets very few attempts before '
                              'conditions change again.'},
                     {'role': 'Risk factor three',
                      'name': 'Small or fragmented range',
                      'body': 'A species in one valley can be wiped out by one event. Fragmenting '
                              'a range also stops populations mixing, so each fragment loses '
                              'variation separately.'},
                     {'role': 'Risk factor four',
                      'name': 'Low genetic variation',
                      'body': 'The most important and the least visible. Selection can only work '
                              'with variation that already exists — a population that has lost it '
                              'has nothing to select from.'}],
           'key_fact': {'ref': 'extinction-is-a-question-of-rate-and-variation', 'ground': 'card'}},
          {'type': 'misconception',
           'id': 'extinction-is-natural-and-permanent',
           'anchor': 's-think',
           'targets': 'EVOL-05'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'extinction-is-a-question-of-rate-and-variation',
                'text': 'A species becomes extinct when the environment changes faster than it can '
                        'adapt, or in ways its existing variation cannot cope with. Specialists, '
                        'slow breeders, species with small ranges and populations with little '
                        'genetic variation are the most vulnerable. Extinction is permanent.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'extinction-is-natural-and-permanent',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'EVOL-05',
                 'statements': [{'quote': 'Extinction is unnatural — it only happens because of '
                                          'us.',
                                 'body': ['Over ninety-nine per cent of all species that have ever '
                                          'existed are extinct, and almost all died out long '
                                          'before there were any humans. There have been five mass '
                                          'extinctions in the fossil record; the largest, at the '
                                          'end of the Permian, removed something like nine tenths '
                                          'of marine species, and the most famous ended the '
                                          'non-bird dinosaurs sixty-six million years ago after an '
                                          'asteroid impact. Species go extinct in ordinary times '
                                          'too, at a slow background rate, simply because '
                                          'environments change. None of that lets anybody off. '
                                          'What is different now is the <em>rate</em>: current '
                                          'extinction rates are estimated at tens to hundreds of '
                                          'times the background rate, driven by habitat loss, '
                                          'introduced species, hunting and a changing climate. The '
                                          'argument for acting is not that extinction is unnatural '
                                          '— it is that we have made it happen far faster than it '
                                          'otherwise would, which is a claim you can check with '
                                          'numbers.']},
                                {'quote': 'If a species goes extinct, another one just takes its '
                                          'place.',
                                 'body': ['Something usually does move into the space, eventually, '
                                          'and eventually is doing a great deal of work in that '
                                          'sentence. After each mass extinction the recovery of '
                                          'diversity took millions of years — not centuries. In '
                                          'the meantime the ecosystem runs without whatever the '
                                          'missing species was doing, and as Disturbing a food web '
                                          'showed, the effects reach species that had no obvious '
                                          'connection to it. There is also the matter of what is '
                                          'lost: an extinct species takes with it a genetic '
                                          'combination that took millions of years to assemble and '
                                          'that nothing else has. A great many of our medicines '
                                          'began as compounds found in living things — aspirin '
                                          'from willow bark, penicillin from a mould, the '
                                          'anticancer drug vincristine from the Madagascar '
                                          'periwinkle — and the ones in a species that dies out '
                                          'unstudied are not recoverable. De-extinction projects '
                                          'exist and are technically interesting; none has '
                                          'restored a functioning population of a lost species, '
                                          'and none is a reason to be relaxed about losing '
                                          'one.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · four species, five pressures',
                 'title': 'Who survives what',
                 'intro': 'A species can be tough against one pressure and helpless against '
                          'another.',
                 'species_label': 'The species',
                 'pressure_label': 'What happens',
                 'progress_suffix': 'combination(s) tried',
                 'trait_labels': ['Diet', 'Breeding rate', 'Range', 'Genetic variation'],
                 'species': [{'id': 'rat',
                              'name': 'Brown rat',
                              'diet': 'Anything at all',
                              'breeding': 'Up to five litters a year',
                              'range': 'Every continent except Antarctica',
                              'variation': 'Very high',
                              'scores': {'habitat': 85,
                                         'climate': 80,
                                         'predator': 70,
                                         'disease': 65,
                                         'hunting': 75}},
                             {'id': 'dormouse',
                              'name': 'Hazel dormouse',
                              'diet': 'Hazelnuts, flowers and insects, in a strict seasonal order',
                              'breeding': 'One small litter a year',
                              'range': 'Fragments of southern English woodland',
                              'variation': 'Low, and falling as populations are cut off',
                              'scores': {'habitat': 15,
                                         'climate': 30,
                                         'predator': 45,
                                         'disease': 35,
                                         'hunting': 80}},
                             {'id': 'panda',
                              'name': 'Giant panda',
                              'diet': 'Bamboo, almost exclusively',
                              'breeding': 'One cub every two years at best',
                              'range': 'Mountain forest in central China',
                              'variation': 'Low',
                              'scores': {'habitat': 20,
                                         'climate': 25,
                                         'predator': 70,
                                         'disease': 40,
                                         'hunting': 35}},
                             {'id': 'gull',
                              'name': 'Herring gull',
                              'diet': 'Fish, waste, chips, almost anything',
                              'breeding': 'A clutch a year, long-lived',
                              'range': 'Coasts and increasingly towns across the northern '
                                       'hemisphere',
                              'variation': 'High',
                              'scores': {'habitat': 80,
                                         'climate': 70,
                                         'predator': 75,
                                         'disease': 60,
                                         'hunting': 65}}],
                 'pressures': [{'id': 'habitat',
                                'label': 'Habitat loss',
                                'name': 'Half the habitat is cleared',
                                'note': 'The commonest cause of extinction today. What remains is '
                                        'also broken into fragments that populations cannot move '
                                        'between.'},
                               {'id': 'climate',
                                'label': 'Climate shift',
                                'name': 'The climate warms by two degrees',
                                'note': 'Seasons shift, so food appears earlier or later than the '
                                        'species expects, and the suitable zone moves — usually '
                                        'polewards or uphill.'},
                               {'id': 'predator',
                                'label': 'A new predator',
                                'name': 'A predator arrives that was never here before',
                                'note': 'Introduced by people, usually. The local species has no '
                                        'evolved defence against it, because nothing like it has '
                                        'ever hunted them.'},
                               {'id': 'disease',
                                'label': 'A new disease',
                                'name': 'A disease sweeps through',
                                'note': 'Survival depends on whether anyone in the population '
                                        'happens to carry resistance — which is a question about '
                                        'genetic variation, not about strength.'},
                               {'id': 'hunting',
                                'label': 'Hunting',
                                'name': 'The species is hunted or collected',
                                'note': 'Direct removal by people, for food, for trade or as a '
                                        'pest. The only pressure on this bench that can be '
                                        'switched off by a decision.'}],
                 'outcomes': {'rat': {'habitat': 'Rats eat anything and live anywhere, including '
                                                 'places people build. Half the woodland gone is '
                                                 'barely an inconvenience — they move into the '
                                                 'other half and into the town beside it.',
                                      'climate': 'A generalist with a huge range simply shifts. '
                                                 'There is nowhere it currently lives that it '
                                                 'could not leave.',
                                      'predator': 'High numbers, fast breeding and no fussiness. A '
                                                  'new predator takes a lot of rats and the '
                                                  'population replaces them within a season.',
                                      'disease': 'A large, varied population almost certainly '
                                                 'contains resistant individuals. Numbers crash '
                                                 'and then recover from the survivors — which is '
                                                 'natural selection doing exactly what the Natural '
                                                 'selection lesson described.',
                                      'hunting': 'People have been trying to eliminate rats for '
                                                 'centuries with poison, traps and dogs, and have '
                                                 'never managed it anywhere they have not first '
                                                 'eliminated the food and shelter.'},
                              'dormouse': {'habitat': 'The worst case on the bench. Dormice will '
                                                      'not cross open ground, so clearing half the '
                                                      'wood does not halve the population — it '
                                                      'strands the remainder in fragments too '
                                                      'small to be viable, each one slowly losing '
                                                      'variation.',
                                           'climate': 'A warmer winter interrupts hibernation, '
                                                      'which burns fat reserves the animal cannot '
                                                      'replace, and shifting seasons break the '
                                                      'strict order of foods it depends on.',
                                           'predator': 'Nocturnal and arboreal, so it avoids some '
                                                       'new predators — but with one litter a year '
                                                       'it replaces losses very slowly.',
                                           'disease': 'Small, isolated populations with low '
                                                      'variation are unlikely to contain resistant '
                                                      'individuals, and there is no route for '
                                                      'survivors to recolonise from elsewhere.',
                                           'hunting': 'Not hunted, and legally protected. This is '
                                                      'the one pressure it is safe from — which is '
                                                      'why the population is still falling for the '
                                                      'other four reasons.'},
                              'panda': {'habitat': 'Bamboo forest cleared for farmland and roads, '
                                                   'and pandas will not cross the gaps. The '
                                                   'remaining populations are isolated from each '
                                                   'other, which is a genetic problem as well as a '
                                                   'spatial one.',
                                        'climate': 'Bamboo is slow to move and much of the '
                                                   'suitable zone would shift uphill beyond where '
                                                   'the mountains stop. A specialist can only '
                                                   'follow its food if the food can move.',
                                        'predator': 'A large adult panda has essentially no '
                                                    'natural predators. This is the one pressure '
                                                    'it handles well, and it explains nothing '
                                                    'about why the species is in trouble.',
                                        'disease': 'Low genetic variation across a small isolated '
                                                   'population is the textbook setup for a disease '
                                                   'outbreak with no resistant survivors.',
                                        'hunting': 'Hunting was a serious historical cause and is '
                                                   'now heavily suppressed by protection — an '
                                                   'example of the one pressure a decision can '
                                                   'actually remove.'},
                              'gull': {'habitat': 'Gulls have responded to habitat loss by moving '
                                                  'into towns, where the food is abundant and the '
                                                  'roofs make excellent cliffs. Generalists '
                                                  'convert a problem into an opportunity.',
                                       'climate': 'A wide range and a varied diet mean a warming '
                                                  'climate shifts where they are rather than '
                                                  'whether they are.',
                                       'predator': 'Large, aggressive, colonial and quite capable '
                                                   'of driving off most things. Not a species that '
                                                   'struggles with predators.',
                                       'disease': 'Dense colonies spread disease efficiently, '
                                                  'which pulls the score down — but the population '
                                                  'is large and varied enough to contain '
                                                  'resistance.',
                                       'hunting': 'Legally protected in the UK and widely '
                                                  'disliked; culls are local and the population is '
                                                  'not limited by them.'}},
                 'outcome_label': 'Population after fifty years',
                 'outcome_suffix': '% of the original population',
                 'bands': {'ok': 65, 'mid': 40},
                 'id': 'who-survives-what',
                 'kind': 'pressure-bench'}],
 'ladder': {'recall': {'title': 'Rung 1 · Read the risk',
                       'q': 'Which of these makes a species most likely to become extinct when its '
                            'environment changes?',
                       'options': ['It eats only one kind of food and breeds slowly',
                                   'It is small and not very strong',
                                   'It has a large population spread over several countries',
                                   'It has many predators'],
                       'answer': 0,
                       'feedback': {1: 'Small size does not decide it. Rats are small and very '
                                       'hard to wipe out.',
                                    2: 'A large, widespread population is one of the safest things '
                                       'to have.',
                                    3: 'Species live alongside their usual predators. A new '
                                       'predator is the danger.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'Is extinction a natural process?',
                      'options': ['No. Species only die out when people hunt them or clear their '
                                  'habitat',
                                  'Yes. Most species that have ever lived died out long before '
                                  'humans existed',
                                  'Yes, so today’s extinctions are nothing to worry about, as they '
                                  'would happen anyway',
                                  'Only for badly adapted species, because a well adapted species '
                                  'always survives'],
                      'answer': 1,
                      'feedback': {0: 'Species died out long before humans. Five mass extinctions '
                                      'happened without us.',
                                   2: 'Extinction is natural, but humans have made it much faster. '
                                      'That is a worry.',
                                   3: 'Well adapted species die out too, when their conditions '
                                      'change.'}},
            'explain': {'title': 'Rung 3 · Explain the difference',
                        'q': 'A brown rat and a hazel dormouse live in the same wood, and half of '
                             'it is cleared. Explain why the rat population recovers and the '
                             'dormouse population may not, referring to at least three of the four '
                             'risk factors.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The rat eats almost anything, so…',
                        'success': ['Says the rat is a generalist and the dormouse a specialist, '
                                    'and explains why that matters when habitat changes.',
                                    'Says the rat breeds several times a year and the dormouse '
                                    'once, so the rat replaces losses far faster.',
                                    'Says the dormouse will not cross open ground, so the '
                                    'remaining wood is fragmented into isolated populations.',
                                    'Says isolated populations lose genetic variation, leaving '
                                    'less for selection to act on.',
                                    'Concludes that the rat population recovers while the dormouse '
                                    'population may decline to nothing even though the event was '
                                    'identical.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A conservation team can do one of three things for an endangered '
                             'woodland species: increase the size of the reserve, plant hedgerows '
                             'linking the reserve to another population twenty miles away, or '
                             'start a captive breeding programme. Argue for one, using what you '
                             'know about the risk factors, and say what the other two would and '
                             'would not fix.',
                        'field_label': 'Your answer',
                        'placeholder': 'The problem I would prioritise is…',
                        'success': ['Identifies which risk factor each option addresses — range, '
                                    'fragmentation and genetic variation, or numbers.',
                                    'Makes a clear choice and gives a reason grounded in the risk '
                                    'factors rather than in preference.',
                                    'Recognises that linking populations addresses genetic '
                                    'variation as well as space, which the other two do not.',
                                    'Notes a limitation of captive breeding — that it does not fix '
                                    'the habitat the animals would return to, or that captive '
                                    'populations lose variation too.',
                                    'Acknowledges that the options are not equally cheap or '
                                    'equally quick, and that a real decision involves a '
                                    'trade-off.']}},
 'key_note': 'Environments change, and a species survives only if its existing variation allows '
             'some individuals to cope and it can produce new generations fast enough. '
             'Specialists, slow breeders, small ranges and low genetic variation all raise the '
             "risk. Extinction has happened throughout Earth's history, including five mass "
             'extinctions; what is different now is how fast it is happening and why.',
 'stretch': [{'type': 'explainer',
              'id': 'the-kakapo-and-what-recovery-costs',
              'text': 'Kakapo are large flightless parrots from New Zealand, and every one of '
                      'their vulnerabilities is a feature that used to be an advantage. New '
                      'Zealand had no land mammals, so there was nothing to run from: flight was '
                      'an unnecessary expense and the kakapo gave it up, freezing when threatened '
                      'instead — a superb defence against a hunting eagle that looks for movement, '
                      'and a fatal one against a stoat that hunts by smell. They breed only in '
                      'years when a particular tree fruits heavily, which can be two to four years '
                      'apart, and lay very few eggs. Every one of those traits was well fitted to '
                      'New Zealand before humans arrived with rats, cats and stoats. The '
                      'population fell to 51 birds. Every living kakapo is now individually named, '
                      'radio-tagged and monitored, and the population is slowly climbing — which '
                      'tells you both that recovery is possible and roughly what it costs.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to work out which pressures a species you know would survive?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The four species are real and their traits are accurately described; the '
                    'fifty-year population figures are illustrative outcomes for a single pressure '
                    'applied in isolation, not projections. Real extinctions almost always involve '
                    'several pressures at once, which is one reason they are hard to predict.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
