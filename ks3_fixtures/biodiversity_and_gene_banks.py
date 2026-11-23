# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B11 `biodiversity-and-gene-banks` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from dd8f3d33ae. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B11'
SOURCE_SLUG = 'biodiversity-and-gene-banks'
FROZEN_FROM = 'dd8f3d33ae'

LESSON = {'slug': 'biodiversity-and-gene-banks',
 'title': 'Biodiversity and gene banks',
 'discipline': 'biology',
 'unit': 'evolution-extinction-and-biodiversity',
 'family': 'SYSTEM',
 'covers': ['KS3.B.INH.07'],
 'touches': ['KS3.B.INH.05', 'KS3.B.INH.06'],
 'beyond_statutory': False,
 'threads': [{'id': 'genes-and-evolution', 'level': 3}, {'id': 'interdependence', 'level': 3}],
 'typical_year': 9,
 'typical_minutes': 55,
 'requires': ['when-the-environment-changes-extinction', 'natural-selection'],
 'assumes': [],
 'references': [{'unit': 'B9', 'lesson': 'pollinators-and-food-security'},
                {'unit': 'B9', 'lesson': 'disturbing-a-food-web'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Maintaining biodiversity, the trade-offs in conservation programmes, and the '
                'biological arguments behind agricultural policy.',
 'big_question': 'Variation is what a population has instead of a plan. Keeping it — in the wild '
                 'where possible, in a freezer where necessary — is the closest thing biology has '
                 'to an insurance policy.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'One banana', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'The blight',
           'done_when': 'two_blighted'},
          {'anchor': 's-banks',
           'short': 'BANKS',
           'label': 'Gene banks',
           'mirrors': 's-bench',
           'done_when': 'two_blighted'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Every Cavendish banana in every shop is a clone of every other one.',
                'prompt': 'A clone is an exact genetic copy. Cavendish bananas are grown from '
                          'cuttings, never from seed, so a plantation is a huge field of identical '
                          'plants.',
                'commit': 'If you had to guess, why could one disease wipe out a whole field of '
                          'these bananas?',
                'options': ['Each clone is a weak plant', 'They all share one weak spot'],
                'reveal': 'The Gros Michel, the banana before the Cavendish, was lost this way, '
                          'and a fungus is now attacking the Cavendish. Next: plant four fields, '
                          'from identical to mixed, and release a blight.',
                'guess': True,
                'replies': ['A Cavendish plant is as healthy as any other banana. The danger is '
                            'that every plant is the same, so whatever kills one can kill them '
                            'all.',
                            'Every plant is the same plant, so whatever can kill one can kill all '
                            'of them. There is no different plant left that happens to resist.'],
                'answer': 1},
 'misconceptions': [{'id': 'EVOL-07',
                     'statement': 'Biodiversity means how many different species there are.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'},
                    {'id': 'EVOL-08',
                     'statement': 'We have gene banks, so it does not matter if species are lost '
                                  'in the wild.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'biodiversity',
                 'definition': 'The variety of living things: the number of different species, and '
                               'the genetic variation within each one.',
                 'note': 'Two measures, and the second is the one this lesson turns on.'},
                {'term': 'gene bank',
                 'definition': 'A store of hereditary material — seeds, sperm, eggs or tissue — '
                               'kept so that variation can be recovered later.',
                 'note': 'Insurance against a loss, not a way of preventing one.'},
                {'term': 'monoculture',
                 'definition': 'A crop grown as a single variety across a whole field or region.',
                 'note': 'The highest yield in a good year, and nothing to fall back on in a bad '
                         'one.'},
                {'term': 'variety',
                 'definition': 'A named type of a crop species, bred to be consistent, so all its '
                               'plants are closely related.',
                 'note': 'Four varieties is four kinds of plant, not four thousand.'},
                {'term': 'landrace',
                 'definition': 'A crop population grown from seed in one place over many '
                               'generations, so no two plants are genetically identical.',
                 'note': 'Less per plant in a good year, and something left in a bad one.'},
                {'term': 'clone',
                 'definition': 'An organism genetically identical to the one it was grown or '
                               'copied from.',
                 'note': 'A thousand cloned plants is one plant repeated a thousand times.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'plant-it-then-release-the-blight', 'anchor': 's-bench'},
          {'type': 'rule',
           'anchor': 's-banks',
           'eyebrow': 'Keeping the variation',
           'statement': 'Two places to store it, and only one of them is alive.',
           'cards': [{'role': 'In the wild',
                      'name': 'Protected habitat',
                      'body': 'Populations left where they are, still breeding, still varying, '
                              'still evolving in response to whatever happens. The only method '
                              'that preserves the ecosystem along with the species.',
                      'limit': 'Needs land, and land has other uses. Vulnerable to exactly the '
                               'pressures that made protection necessary.'},
                     {'role': 'In storage',
                      'name': 'Seed banks',
                      'body': 'Dried seeds at around minus eighteen degrees, catalogued and '
                              'duplicated between countries. Cheap per sample and enormous numbers '
                              'can be held in one building.',
                      'limit': 'Only works for seeds that survive drying and freezing, and they '
                               'must be tested and regrown on a cycle or they die quietly in the '
                               'dark.'},
                     {'role': 'In storage',
                      'name': 'Frozen sperm, eggs and tissue',
                      'body': 'For animals, where you cannot store a seed. Frozen zoos hold '
                              'material from thousands of species, including some already extinct '
                              'in the wild.',
                      'limit': 'Bringing an animal back from frozen cells needs a surrogate mother '
                               'of a close species, and a stored population cannot be a '
                               'functioning one.'},
                     {'role': 'Living collections',
                      'name': 'Botanic gardens and zoos',
                      'body': 'Living organisms maintained and bred deliberately, with studbooks '
                              'tracking relatedness to keep as much variation as possible.',
                      'limit': 'Expensive per individual, holds small numbers, and captive '
                               'populations lose variation and adapt to captivity over '
                               'generations.'}],
           'key_fact': {'ref': 'biodiversity-is-two-things', 'ground': 'card'}},
          {'type': 'misconception',
           'id': 'biodiversity-and-what-a-bank-holds',
           'anchor': 's-think',
           'targets': 'EVOL-07'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'biodiversity-is-two-things',
                'text': 'Biodiversity is the variety of living things — between species, and '
                        'between individuals within a species. It matters because variation is '
                        'what allows populations to survive change. Gene banks store seeds, sperm, '
                        'eggs and tissue so that variation is not lost for ever if a population '
                        'is.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'biodiversity-and-what-a-bank-holds',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'EVOL-07',
                 'statements': [{'quote': 'Biodiversity means how many different species there '
                                          'are.',
                                 'body': ['That is one of the two things it means, and the other '
                                          'one is doing more work in this unit. Biodiversity '
                                          'includes the variation <em>within</em> each species — '
                                          'how genetically different the individuals of one '
                                          'population are from each other. A wood with forty '
                                          'species in it, each reduced to a handful of closely '
                                          'related survivors, is in far more trouble than the '
                                          'species count suggests, and this is exactly the '
                                          'vulnerability that appeared as risk factor four in When '
                                          'the environment changes: extinction. It is also the '
                                          'sense in which a field of one thousand identical potato '
                                          'plants has a biodiversity of almost nothing, despite '
                                          'being a thousand living organisms. Count species when '
                                          'you want to describe a habitat; ask about variation '
                                          'within a species when you want to know whether it can '
                                          'survive what happens next.']},
                                {'quote': 'We have gene banks, so it does not matter if species '
                                          'are lost in the wild.',
                                 'body': ['A seed bank stores a species; it does not store the '
                                          'thing the species was part of. Put a seed back into a '
                                          'landscape and it needs the soil fungi it partners with, '
                                          'the insect that pollinates it, the animal that '
                                          'disperses it, and a climate resembling the one it left '
                                          '— none of which is in the freezer. Seeds also do not '
                                          'last for ever: they need testing, regrowing and '
                                          'replacing on a cycle, which is expensive and only as '
                                          'reliable as the funding. And a stored population cannot '
                                          'go on evolving; it is frozen in the state it was '
                                          'collected in, while the world outside carries on '
                                          'changing. Gene banks are worth every penny as an '
                                          'insurance policy, and the honest description of them is '
                                          'exactly that — insurance, taken out against a loss you '
                                          'are still trying to prevent, not a substitute for '
                                          'preventing it.']}]},
                {'segment': 'practical',
                 'demand': 'investigate',
                 'eyebrow': 'At the bench · four fields, one disease',
                 'title': 'Plant it, then release the blight',
                 'intro': 'A thousand potato plants, and a blight that a few varieties happen to '
                          'resist. Watch what is left to plant next year.',
                 'tabs_label': 'What you planted',
                 'progress_suffix': 'field(s) tested',
                 'progress_zero': 'no blight released yet',
                 'total': 1000,
                 'fields': [{'id': 'clone',
                             'label': 'One variety',
                             'name': 'One variety, a thousand identical plants',
                             'note': 'Every plant grown from cuttings of the same original, '
                                     'easiest to harvest by machine, and every plant has exactly '
                                     'the same weaknesses.',
                             'varieties': 1,
                             'resistant': 0,
                             'variation_word': 'none',
                             'variation_bar': 9,
                             'yield_word': 'highest',
                             'yield_bar': 100},
                            {'id': 'four',
                             'label': 'Four varieties',
                             'name': 'Four varieties, 250 plants of each',
                             'note': 'A little less convenient — four harvest dates, four sets of '
                                     'instructions — and one of the four happens to carry '
                                     'resistance to this particular blight.',
                             'varieties': 4,
                             'resistant': 1,
                             'variation_word': '4 varieties',
                             'variation_bar': 36,
                             'yield_word': 'good',
                             'yield_bar': 85},
                            {'id': 'ten',
                             'label': 'Ten varieties',
                             'name': 'Ten varieties, 100 plants of each',
                             'note': 'The way small farms grew potatoes for centuries, and still '
                                     'do in the Andes where the crop originated. Awkward to '
                                     'manage, and four of the ten resist this blight.',
                             'varieties': 10,
                             'resistant': 4,
                             'variation_word': '10 varieties',
                             'variation_bar': 90,
                             'yield_word': 'good',
                             'yield_bar': 85},
                            {'id': 'landrace',
                             'label': 'A mixed landrace',
                             'name': 'A mixed landrace, every plant slightly different',
                             'note': 'Not varieties at all — a population grown from seed, so no '
                                     'two plants are genetically identical. Yields less per plant '
                                     'and is nearly impossible to harvest mechanically.',
                             'varieties': 1000,
                             'resistant': 620,
                             'variation_word': 'very high',
                             'variation_bar': 100,
                             'yield_word': 'lowest',
                             'yield_bar': 55}],
                 'bar_labels': ['Plants surviving the blight',
                                'Genetic variation in the field',
                                'Yield per plant in a good year'],
                 'bar_label_before': 'Plants standing in the field',
                 'run_label': 'Release the blight',
                 'ran_label': 'Blight has passed through',
                 'reset_label': 'Clear the field',
                 'verdicts': {'clone': 'Nothing survives. Not one plant in a thousand, because '
                                       'there was only ever one plant repeated a thousand times — '
                                       'and this blight kills it. This is what happened to '
                                       "Ireland's potato crop in the 1840s, in miniature, and it "
                                       'is the shape of the Gros Michel banana as well.',
                              'four': 'About {pct}% survives — not a good year, and not a '
                                      'catastrophe. There is a crop to eat and, more importantly, '
                                      'seed to plant that is known to resist. Variation is what '
                                      'turns a total loss into a bad harvest.',
                              'ten': 'About {pct}% survives — not a good year, and not a '
                                     'catastrophe. There is a crop to eat and, more importantly, '
                                     'seed to plant that is known to resist. Variation is what '
                                     'turns a total loss into a bad harvest.',
                              'landrace': 'Around {pct}% of the crop comes through, and next year '
                                          'every one of those survivors is a plant that resisted. '
                                          'The yield per plant was never the highest here; the '
                                          'yield in the year of a blight is the only one that '
                                          'decides whether anyone eats.'},
                 'id': 'plant-it-then-release-the-blight',
                 'kind': 'blight-bench'}],
 'ladder': {'recall': {'title': 'Rung 1 · What biodiversity includes',
                       'q': 'Which field has the lowest biodiversity?',
                       'options': ['A field with a thousand clones of one potato variety',
                                   'A field with fifty different plant species growing in it '
                                   'together',
                                   'A field with ten potato varieties, a hundred plants of each',
                                   'A field with two species of wild grass'],
                       'answer': 0,
                       'feedback': {1: 'Fifty species is a lot of variety. Look for the least '
                                       'variation.',
                                    2: 'Ten varieties have far more variation than one clone '
                                       'variety.',
                                    3: 'Each grass plant differs a little. Clones have no '
                                       'variation at all.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A charity says a seed bank means a plant species can never truly be '
                           'lost. What is the strongest objection?',
                      'options': ['Seeds do not survive freezing, so every stored sample is dead '
                                  'before it is needed',
                                  'Gene banks cost too much, so the money is always better spent '
                                  'somewhere else',
                                  'Nobody knows how to grow a stored seed, so it can never come '
                                  'back',
                                  'Its pollinators and soil fungi are not stored, so it may not '
                                  'survive'],
                      'answer': 3,
                      'feedback': {0: 'Many seeds survive drying and freezing. That is why seed '
                                      'banks work.',
                                   1: 'Seed banks are cheap for what they protect. Cost is not the '
                                      'main objection.',
                                   2: 'Stored seeds can be grown. The problem is the habitat they '
                                      'return to.'}},
            'explain': {'title': 'Rung 3 · Explain the monoculture risk',
                        'q': 'Explain why a field of genetically identical crop plants can be '
                             'completely destroyed by a disease, while a field of many varieties '
                             'usually is not — and link your answer to natural selection.',
                        'field_label': 'Your explanation',
                        'placeholder': 'If every plant is genetically identical…',
                        'success': ['Says genetically identical plants all have the same '
                                    'susceptibility, so if one can be infected they all can.',
                                    'Says a mixed field contains plants with different versions of '
                                    'genes, some of which may resist the disease.',
                                    'Says the resistant plants survive and can be harvested and '
                                    'replanted.',
                                    'Links this to natural selection: selection can only act on '
                                    'variation that already exists in the population.',
                                    'Concludes that a clone population has no variation for '
                                    'selection to act on, so there is no possibility of a '
                                    'resistant survivor.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'A government has a fixed conservation budget and must divide it '
                             'between protecting habitat and expanding a national seed bank. Set '
                             'out the argument for each, say which you would fund more heavily and '
                             'why, and identify one thing your choice would fail to protect.',
                        'field_label': 'Your answer',
                        'placeholder': 'Protecting habitat keeps…',
                        'success': ['States what habitat protection achieves: living populations '
                                    'that keep varying and evolving, with their ecosystem intact.',
                                    'States what a seed bank achieves: many species stored cheaply '
                                    'and safely, including some already lost from the wild.',
                                    'Makes a clear choice with a reason grounded in biology rather '
                                    'than preference.',
                                    'Identifies a real limitation of the chosen option — land use '
                                    'conflict, or the fact that stored material stops evolving.',
                                    'Recognises the two are complementary rather than '
                                    'alternatives, or explains why a split would still involve a '
                                    'trade-off.']}},
 'key_note': 'Biodiversity is the variety of life: the number of species, and the genetic '
             'variation within each one. Variation is what allows a population to survive a '
             'change, so losing it raises the risk of extinction and, in crops, of total crop '
             'failure. Gene banks preserve hereditary material — seeds, sperm, eggs, tissue — as '
             'insurance, but they cannot store an ecosystem and a stored population stops '
             'evolving.',
 'stretch': [{'type': 'explainer',
              'id': 'the-svalbard-global-seed-vault',
              'text': 'The Svalbard Global Seed Vault sits inside a mountain on an Arctic island, '
                      'about 1,300 km from the North Pole. It holds well over a million seed '
                      'samples sent by seed banks all over the world, in sealed foil packets at '
                      'minus eighteen degrees, and it is designed to keep them cold even if the '
                      'power fails, because the surrounding rock is permanently frozen. It is a '
                      'backup of backups: countries deposit duplicates of what their own national '
                      "banks already hold. It has been used for real. Syria's seed bank at Aleppo, "
                      'which held varieties of wheat and barley from across the Middle East, '
                      'became inaccessible during the civil war, and researchers withdrew their '
                      'duplicate samples from Svalbard, grew them on in Lebanon and Morocco, and '
                      'sent fresh seed back to the vault. That is the whole argument for gene '
                      'banks in one story — and also for why the seeds have to be regrown '
                      'periodically rather than simply left in a freezer.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to argue the case for or against a conservation decision?',
           'cta': 'Ask about this lesson',
           'anchor': 's-bench'},
 'convention_note': 'The blight bench is a teaching model: the disease affects whole varieties '
                    'rather than individual plants, resistance is all-or-nothing, and yield is '
                    'treated as directly proportional to surviving plants. Real blight resistance '
                    'is partial and varies with weather, and real fields lose some of every '
                    'variety. The Gros Michel, Cavendish and Svalbard accounts are real.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
