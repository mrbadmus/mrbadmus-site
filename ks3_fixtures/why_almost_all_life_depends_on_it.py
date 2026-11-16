# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B7 `why-almost-all-life-depends-on-it` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B7'
SOURCE_SLUG = 'why-almost-all-life-depends-on-it'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'why-almost-all-life-depends-on-it',
 'title': 'Why almost all life depends on it',
 'discipline': 'biology',
 'unit': 'photosynthesis',
 'family': 'SYSTEM',
 'covers': ['KS3.B.PHOT.02'],
 'touches': ['KS3.B.PHOT.01', 'KS3.B.RESP.01', 'KS3.B.ECO.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'energy', 'level': 2}, {'id': 'cells-and-systems', 'level': 1}],
 'typical_year': 8,
 'typical_minutes': 55,
 'requires': ['the-photosynthesis-reaction'],
 'assumes': [],
 'references': [{'unit': 'P1', 'lesson': 'energy-stores'},
                {'unit': 'P2', 'lesson': 'fuels-and-energy-resources'},
                {'unit': 'B4', 'lesson': 'stomata-and-gas-exchange-in-plants'}],
 'connects_heading': 'Connects to',
 'ks4_links': [],
 'ks4_becomes': 'Trophic levels and biomass transfer, the carbon cycle, and the evidence behind '
                'human effects on atmospheric carbon dioxide.',
 'big_question': 'One reaction, running in leaves and in water you cannot see into, is the doorway '
                 'through which almost all the energy in the living world arrives — and the source '
                 'of every breath you have ever taken.',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Every meal', 'done_when': 'committed'},
          {'anchor': 's-trace',
           'short': 'TRACE',
           'label': 'Trace it back',
           'done_when': 'chain_traced'},
          {'anchor': 's-jobs',
           'short': 'JOBS',
           'label': 'Three jobs',
           'mirrors': 's-trace',
           'done_when': 'chain_traced'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Every meal you eat started somewhere.',
                'prompt': 'A steak is a cow, and the cow ate grass. Bread is made from wheat. A '
                          'mushroom is harder: it is not green, has no leaves, and grows on '
                          'compost or rotting wood, often where no sunlight reaches.',
                'commit': 'If you had to guess, does a mushroom live on food that a plant made, or '
                          'on food it makes itself?',
                'options': ['Food a plant made', 'Food it makes itself'],
                'reveal': 'Follow almost any food back far enough and you reach something that '
                          'makes food from light. Next: pick a food and trace it back, step by '
                          'step.',
                'guess': True,
                'replies': ["A mushroom's threads feed on dead plant material, so its food was "
                            'built by a plant, maybe years ago.',
                            'It grows without anyone feeding it, so it can look self-made. But a '
                            'mushroom has no chlorophyll and cannot make food from light. It '
                            'digests what a plant built earlier.'],
                'answer': 0},
 'misconceptions': [{'id': 'PLANT-07',
                     'statement': 'Plants do the photosynthesising — trees are the lungs of the '
                                  'planet.',
                     'elicited_by': 's-think',
                     'confronted_by': 's-think'},
                    {'id': 'PLANT-08',
                     'statement': 'Plants make oxygen for us to breathe.',
                     'elicited_by': 's-jobs',
                     'confronted_by': 's-think'}],
 'vocabulary': [{'term': 'producer',
                 'definition': 'An organism that builds its own organic molecules from simple raw '
                               "materials, instead of eating something else's.",
                 'note': 'It is at the bottom of a food chain, not the top.'},
                {'term': 'photosynthetic organism',
                 'definition': 'Any organism that carries out photosynthesis: plants, algae, and '
                               'some bacteria.',
                 'note': "Not only plants. Roughly half of the world's photosynthesis happens in "
                         'the sea.'},
                {'term': 'phytoplankton',
                 'definition': 'Microscopic algae drifting in the sunlit surface water of seas and '
                               'lakes.',
                 'note': 'Each one photosynthesises with chlorophyll, exactly as a leaf does.'},
                {'term': 'organic molecule',
                 'definition': 'A molecule built around carbon by a living thing — a sugar, a '
                               'starch, a protein, a fat.',
                 'note': None},
                {'term': 'decomposer',
                 'definition': 'An organism that feeds on dead material, digesting it from the '
                               'outside and absorbing what is released.',
                 'note': 'It sits at the end of a food chain, not outside one.'},
                {'term': 'chemosynthesis',
                 'definition': 'Building sugars using energy released by chemical reactions, '
                               'instead of energy from light.',
                 'note': 'Found at deep-sea vents where no light has ever reached.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'trace-a-meal', 'anchor': 's-trace'},
          {'type': 'rule',
           'anchor': 's-jobs',
           'eyebrow': 'Three things it does for everything else',
           'statement': 'Food, air, and the balance between them.',
           'cards': [{'term': 'Job one · The way in for energy',
                      'gloss': 'Energy enters almost every food chain on Earth at one point: a '
                               'photosynthetic organism capturing sunlight. Everything above that '
                               'is spending what a producer captured. Without it: nothing above '
                               'the producers has any source of energy at all, and the chains '
                               'empty from the bottom up.'},
                     {'term': 'Job two · The oxygen in the air',
                      'gloss': 'The atmosphere is about a fifth oxygen and all of it is biological '
                               'in origin — released over billions of years as a waste product of '
                               'splitting water. Without it: no new oxygen is added, while every '
                               'respiring organism keeps consuming what is there.'},
                     {'term': 'Job three · Taking carbon back out',
                      'gloss': 'Respiration, decay and burning all put carbon dioxide into the '
                               'air. Photosynthesis is the only large-scale biological process '
                               'that removes it, locking carbon into wood, roots and ocean '
                               'sediment. Without it: carbon dioxide only ever rises, because the '
                               "living world's one route out of the atmosphere has been closed."}]},
          {'type': 'key-fact', 'ref': 'photosynthetic-organisms-are-producers'},
          {'type': 'misconception',
           'id': 'two-wrong-ideas',
           'anchor': 's-think',
           'targets': 'PLANT-07'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'photosynthetic-organisms-are-producers',
                'text': 'Photosynthetic organisms — plants on land, algae and plankton in the sea '
                        '— are the producers. They build the organic molecules that almost every '
                        'other living thing eats, they released the oxygen in the atmosphere, and '
                        'they take carbon dioxide back out of it.',
                'placement': 'top-level',
                'ground': 'band',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'two-wrong-ideas',
                 'kind': 'confrontation',
                 'demand': 'explain',
                 'targets': 'PLANT-07',
                 'statements': [{'quote': 'Plants do the photosynthesising — trees are the lungs '
                                          'of the planet.',
                                 'body': ['Roughly half of all photosynthesis on Earth happens in '
                                          'the sea, carried out by algae and phytoplankton, most '
                                          'of them single cells too small to see without a '
                                          'microscope. A drifting organism a hundredth of a '
                                          'millimetre across, in numbers no one can count, matches '
                                          'every forest and grassland on land put together. '
                                          'Rainforests are irreplaceable for a long list of '
                                          "reasons, and being the planet's only oxygen supply is "
                                          'not one of them — a mature forest also consumes much of '
                                          'what it produces, since every one of its cells respires '
                                          'day and night. Keep the vocabulary honest and this '
                                          'stays clear: the group that matters is '
                                          '<em>photosynthetic organisms</em>, which includes '
                                          'plants, algae and some bacteria. Restricting the idea '
                                          "to green things with roots leaves out half the planet's "
                                          'production and most of its producers.']},
                                {'quote': 'Plants make oxygen for us to breathe.',
                                 'body': ['Not for us, and not for anything. Oxygen is a waste '
                                          'product: the plant is building glucose, and oxygen is '
                                          'what is left over from splitting water to do it. There '
                                          'was no oxygen worth mentioning in the atmosphere for '
                                          "the first two billion years of Earth's history, and the "
                                          'organisms that eventually filled it with the stuff were '
                                          'bacteria releasing a gas that was, at the time, '
                                          'poisonous to almost everything alive. Breathing animals '
                                          'appeared afterwards, in an atmosphere that was already '
                                          'there — the sequence runs the other way round from the '
                                          'way the sentence implies. Nothing in biology is done '
                                          "<em>for</em> another organism's benefit, and a plant "
                                          'that gave away useful material on purpose would be '
                                          'out-competed by one that did not. Plants also respire '
                                          'continuously, which is the subject of Stomata and gas '
                                          'exchange in plants and worth having straight before '
                                          'this claim is repeated.']}]},
                {'demand': 'investigate',
                 'eyebrow': 'At the bench · follow it back',
                 'heading': 'Trace a meal to a leaf',
                 'head_counter': {'format': 'step {n} of {total}', 'done': 'chain traced'},
                 'prompt': 'Pick something off the plate and step backwards through the chain that '
                           'supplied it. Count the steps — and notice that the number changes '
                           'while the destination never does.',
                 'options_label': 'On the plate',
                 'foods': [{'id': 'steak',
                            'label': 'Steak',
                            'name': 'Steak',
                            'chain': [{'name': 'Steak on the plate',
                                       'note': 'Muscle tissue, built from protein the animal '
                                               'assembled.'},
                                      {'name': 'The cow',
                                       'note': 'Everything in it was built from what it ate. A cow '
                                               'eats no meat at all.'},
                                      {'name': 'Grass',
                                       'note': 'Around ten kilograms of grass for every kilogram '
                                               'of cow — most of what the cow eats is respired '
                                               'away to keep the cow alive.'},
                                      {'name': 'Photosynthesis in the grass leaf',
                                       'note': 'Carbon dioxide from the air, water from the soil, '
                                               'energy from sunlight falling on a field.'}],
                            'verdict': 'Three steps from a field to a plate, and every gram of it '
                                       'was carbon dioxide before the grass got hold of it.'},
                           {'id': 'bread',
                            'label': 'Bread',
                            'name': 'Bread',
                            'chain': [{'name': 'A slice of bread',
                                       'note': 'Mostly starch, plus the protein that makes the '
                                               'dough stretch.'},
                                      {'name': 'Wheat grain',
                                       'note': 'A seed — a store of starch the plant packed for '
                                               'its own seedling, which we intercept.'},
                                      {'name': 'Photosynthesis in the wheat leaf',
                                       'note': 'Glucose made in the leaves, moved to the '
                                               'developing grain and stored as starch.'}],
                            'verdict': 'Two steps, the shortest chain on the plate. Eating a '
                                       'producer directly is the most efficient thing you can do '
                                       'with a field.'},
                           {'id': 'salmon',
                            'label': 'Salmon',
                            'name': 'Salmon',
                            'chain': [{'name': 'A salmon fillet',
                                       'note': 'From the sea, and nothing green anywhere near it.'},
                                      {'name': 'Small fish and shrimp-like animals',
                                       'note': 'What a salmon hunts.'},
                                      {'name': 'Zooplankton',
                                       'note': 'Tiny drifting animals, each a fraction of a '
                                               'millimetre across, eaten in enormous numbers.'},
                                      {'name': 'Phytoplankton',
                                       'note': 'Microscopic algae drifting in the sunlit surface '
                                               'water. They photosynthesise exactly as a leaf '
                                               'does, with chlorophyll and the same reaction.'},
                                      {'name': 'Sunlight on the top hundred metres of ocean',
                                       'note': 'Below that depth there is not enough light, which '
                                               'is why almost all sea life lives in a thin layer '
                                               'at the top.'}],
                            'verdict': 'Four steps, and the producer at the end is invisible. '
                                       'Roughly half the world’s photosynthesis is done by '
                                       'organisms like these.'},
                           {'id': 'cheese',
                            'label': 'Cheese',
                            'name': 'Cheese',
                            'chain': [{'name': 'Cheese',
                                       'note': 'Milk protein and fat, curdled and matured — '
                                               'bacteria do the maturing.'},
                                      {'name': 'Milk from a cow',
                                       'note': 'Produced from what the cow ate, by an animal that '
                                               'eats only plants.'},
                                      {'name': 'Grass and silage',
                                       'note': 'Silage is preserved grass, which is how a dairy '
                                               'herd is fed in winter.'},
                                      {'name': 'Photosynthesis in the grass leaf',
                                       'note': 'The same field as the steak, and the same '
                                               'reaction.'}],
                            'verdict': 'Three steps. The bacteria that ripen the cheese are living '
                                       'on the same sugars and proteins, one further down the '
                                       'chain again.'},
                           {'id': 'mushroom',
                            'label': 'Mushroom',
                            'name': 'Mushroom',
                            'chain': [{'name': 'A mushroom',
                                       'note': 'Not a plant. Fungi have no chlorophyll and cannot '
                                               'photosynthesise at all.'},
                                      {'name': 'Threads through compost or dead wood',
                                       'note': 'The mushroom is the fruiting body; the organism is '
                                               'a network of threads digesting dead material from '
                                               'the outside in.'},
                                      {'name': 'Dead plant material',
                                       'note': 'Straw, wood, leaf litter — built by a plant that '
                                               'is no longer alive.'},
                                      {'name': 'Photosynthesis, some time ago',
                                       'note': 'The molecules the fungus is living on were '
                                               'assembled in a leaf, possibly years earlier.'}],
                            'verdict': 'Three steps, and it is the case that looks like an '
                                       'exception and is not. A decomposer is not outside the '
                                       'chain — it is at the end of it.'},
                           {'id': 'honey',
                            'label': 'Honey',
                            'name': 'Honey',
                            'chain': [{'name': 'Honey',
                                       'note': 'Concentrated sugar, and almost nothing else.'},
                                      {'name': 'Bees',
                                       'note': 'They collect nectar and evaporate the water off '
                                               'it. They add enzymes; they do not add sugar.'},
                                      {'name': 'Nectar in a flower',
                                       'note': 'A sugar solution the plant manufactures '
                                               'deliberately, to pay pollinators for a delivery '
                                               'service.'},
                                      {'name': 'Photosynthesis in the plant',
                                       'note': 'The sugar in nectar is glucose the plant made from '
                                               'carbon dioxide.'}],
                            'verdict': 'Three steps, and the shortest chemical journey of the six: '
                                       'the sugar you taste is close to the sugar the leaf '
                                       'built.'}],
                 'steps_label': {'idle': 'follow it back', 'done': '{n} steps back to a producer'},
                 'step_label': 'Where did that come from?',
                 'done_label': 'You have reached a producer',
                 'reset_label': 'Start again',
                 'id': 'trace-a-meal',
                 'kind': 'trace-it-back'}],
 'ladder': {'recall': {'title': 'Rung 1 · Producers',
                       'q': 'What does it mean to call a plant a producer?',
                       'options': ['It builds its own organic molecules from simple raw materials, '
                                   'instead of eating something else’s',
                                   'It makes the oxygen other organisms breathe, so its role in a '
                                   'chain is supplying air',
                                   'It produces more offspring than it needs, so the word is about '
                                   'quantity rather than food',
                                   'It sits at the top of a food chain, because everything else '
                                   'depends on it'],
                       'answer': 0,
                       'feedback': {1: 'Oxygen is a waste product, and it is not made for anyone. '
                                       'Producer is about food, not about air.',
                                    2: 'That is true of most organisms and has nothing to do with '
                                       'the term.',
                                    3: 'It is at the bottom — the base that everything else is '
                                       'standing on.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A mushroom is not green and cannot photosynthesise. Does it depend on '
                           'photosynthesis?',
                      'options': ['No — an organism that takes its food straight from the compost '
                                  'it grows in is making its own, so it needs no producer',
                                  'No — a fungus takes its energy from the minerals in the soil, '
                                  'so sunlight never enters its chain',
                                  'Yes — it feeds on dead material that a photosynthetic organism '
                                  'built, so it sits at the end of the same chain',
                                  'Only if it is growing on a living plant — what is dead has '
                                  'stopped being part of any chain'],
                      'answer': 2,
                      'feedback': {0: 'Feeding on something is not making your own food. The '
                                      'compost is dead plant material, and a fungus is digesting '
                                      'what a plant built.',
                                   1: 'Minerals supply no energy, to a fungus or to anything else. '
                                      'That is the same mistake as thinking plants feed on soil.',
                                   3: 'Dead or alive makes no difference to where the molecules '
                                      'came from. Either way they were assembled by '
                                      'photosynthesis.'}},
            'explain': {'title': 'Rung 3 · Follow the energy',
                        'q': 'Explain how the energy in a beef burger got there, starting from the '
                             'Sun. Use the words producer, photosynthesis, glucose and '
                             'respiration.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Light from the Sun fell on…',
                        'success': ['Says light energy from the Sun was absorbed by chlorophyll in '
                                    'grass leaves.',
                                    'Says photosynthesis used that energy to build glucose from '
                                    'carbon dioxide and water — so the grass is the producer.',
                                    'Says the energy is now stored chemically in molecules the '
                                    'plant built.',
                                    'Says the cow ate the grass and used some of that energy, '
                                    'storing the rest in its own tissues.',
                                    'Says most of what the cow ate was released again by '
                                    'respiration rather than passed on, which is why a field feeds '
                                    'far more people as wheat than as beef.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'Coal is often described as "ancient sunlight". Explain what that '
                             'means, where the carbon in a lump of coal came from, and what '
                             'burning it does to the atmosphere.',
                        'field_label': 'Your answer',
                        'placeholder': 'The coal formed from…',
                        'success': ['Says coal formed from plants that lived and photosynthesised '
                                    'hundreds of millions of years ago.',
                                    'Says the carbon in those plants came from carbon dioxide in '
                                    'the atmosphere of the time.',
                                    'Says the energy stored chemically in the coal is energy those '
                                    'plants captured from sunlight.',
                                    'Says the plant material was buried before it could fully '
                                    'decay, so the carbon was locked away instead of returning to '
                                    'the air.',
                                    'Says burning it returns that carbon dioxide to the atmosphere '
                                    '— releasing in a moment what was removed over millions of '
                                    'years, faster than photosynthesis can take it back out.']}},
 'key_note': 'Photosynthetic organisms are producers: they build organic molecules from carbon '
             'dioxide and water using light, and everything that cannot do this depends on them, '
             'directly or through a chain. They also released the oxygen in the atmosphere and '
             "continue to take carbon dioxide out of it. Roughly half of the world's "
             'photosynthesis happens in the sea.',
 'stretch': [{'type': 'explainer',
              'id': 'the-almost-in-the-title',
              'text': "The word <em>almost</em> in this lesson's title is doing real work. Two and "
                      'a half kilometres down, where no light has ever reached, hot water loaded '
                      'with dissolved chemicals pours out of cracks in the sea floor and whole '
                      'communities live around it — tube worms two metres long, crabs, clams. At '
                      'the base of those food chains are bacteria that build sugars using energy '
                      'released from chemical reactions instead of energy from light, a process '
                      'called chemosynthesis. They were found in 1977, and they mattered '
                      'immediately: until then, sunlight was assumed to be the only way energy '
                      'could enter a living system. It is a useful thing to know when people '
                      'speculate about life on a moon with a frozen ocean and no daylight at '
                      'all.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to trace something that is not on the plate above?',
           'cta': 'Ask about this lesson',
           'anchor': 's-trace'},
 'convention_note': 'The chains are simplified to one line each: real diets are webs, a farmed '
                    "salmon eats feed made from several sources, and a cow's rumen bacteria sit "
                    'between the grass and the cow. The land-and-sea split of global '
                    'photosynthesis is an approximate figure that varies between estimates and '
                    'with the season.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
