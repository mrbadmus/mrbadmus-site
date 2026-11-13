# -*- coding: utf-8 -*-
"""Ecosystems, in the lean shape. Spec table: ks4-ecosystems.md (lead moves it to docs/lessons/).

LEGACY (batch 10). The ladder and the practice set stay from the Design page, so every rung id and
every practice-set question id survives, except practice Q5, whose stem now states that dragonfly
larvae eat tadpoles (new id). The practice set is the page's own BANK (all routes), not the subtopic
quiz list, so its fixes are logic_edits below.
"""

LOGIC_EDITS = [
    # Practice set Q1 ("What is the difference between a community and an ecosystem?"), stem kept.
    # The credited option was visibly the longest; options and feedback rewritten plainly.
    ('"A community is all the living organisms in an area. An ecosystem is the community PLUS all the non-living (abiotic) factors."',
     '"An ecosystem also includes the abiotic parts"'),
    ('"A community is larger than an ecosystem — it includes several ecosystems."',
     '"A community is made of several ecosystems"'),
    ('"They are the same thing — both describe all organisms in an area."',
     '"They are two words for the same thing"'),
    ('"An ecosystem only includes animals. A community includes all living things."',
     '"An ecosystem includes only the animals"'),
    ('"An ECOSYSTEM is larger — it includes the community PLUS all abiotic factors. A community is just the living part."',
     '"It is the other way round. An ecosystem is a community plus the non-living parts."'),
    ('"They are NOT the same — a community is the living component only. An ecosystem adds the non-living environment."',
     '"A community is the living organisms only. An ecosystem adds the non-living parts."'),
    ('"An ecosystem includes ALL living organisms (animals, plants, fungi, microorganisms) plus abiotic factors — not just animals."',
     '"An ecosystem includes all the living organisms, plus the non-living parts."'),
    # Practice set Q2 ("Wolves are removed ..."), stem kept. "Other predators increase in number
    # to compensate" was arguable (its own feedback said it may happen); the credited option was
    # a four-dash chain. Options and feedback rewritten.
    ('"Deer population increases — deer overgraze vegetation — plant diversity declines — other animals that depend on those plants also decline"',
     '"Deer numbers rise and more plants are eaten"'),
    ('"The ecosystem immediately collapses — all species die without wolves"',
     '"Every species in the wood dies out"'),
    ('"Other predators increase in number to compensate for the wolves"',
     '"Deer numbers fall and plants grow more"'),
    ('"Nothing changes — deer populations regulate themselves"',
     '"Nothing in the wood changes"'),
    ('"Ecosystems rarely collapse immediately — they often shift to a new, less diverse stable state."',
     '"The other species do not all depend on the wolves. The change runs through the deer."'),
    ('"Some compensation by other predators may occur — but wolves are often the main predators, so full compensation is rare."',
     '"With no wolves to eat them, more deer survive, so deer numbers rise."'),
    ('"Without predators, prey populations often grow beyond what the habitat can support — leading to overgrazing and eventual population crash."',
     '"The species are interdependent. Removing the wolves changes the deer, and the deer change the plants."'),
    # Practice set Q5 (dragonfly larvae), stem kept: the credited option was visibly the longest.
    ("'Dragonfly larvae ate tadpoles; without them more tadpoles survived and ate more pondweed'",
     "'More tadpoles survived and ate more pondweed'"),
    # Rung 1 Q1 and Q2, Rung 2 Q1: the credited option was visibly the longest. Distractors made
    # the same length; replies unchanged except where the distractor's words changed.
    ("['All the living things in an area', 'That is a community.']",
     "['All the organisms of every species living in one area', 'That is a community.']"),
    ("['An area and everything in it', 'That is an ecosystem.']",
     "['An area with all its living and non-living parts', 'That is an ecosystem.']"),
    ("['The plants', 'Plants are living, so they are in the community.']",
     "['The plants that live in the area', 'Plants are living, so they are in the community.']"),
    ("['The microorganisms', 'Also living, so in the community.']",
     "['The fungi and bacteria living in it', 'These are living, so they are in the community.']"),
    ("['The flowers had nothing to eat', 'Plants make their own food.']",
     "['The flowers had no bees to feed on, so they starved', 'Plants make their own food. They do not feed on bees.']"),
    # Examiner MUST FIX r1.1: the credited option was still visibly the longest. The why line
    # keeps the full phrase.
    ("['The non-living (abiotic) parts of the environment', [",
     "['The non-living (abiotic) parts', ["),
    # Examiner MUST FIX r2.1: credited option longest; "fewer foxes to fertilise it" was
    # arguable (droppings add nutrients). New distractor contradicts the data.
    ("['Without foxes more rabbits survived, and more rabbits ate more grass', ['The foxes had been eating the grass', 'Foxes eat rabbits, not grass.'], ['Grass fell because there were fewer foxes to fertilise it', 'The data link runs through the rabbits: 200 to 1400.']]",
     "['More rabbits survived and ate more grass', ['The foxes had been eating the grass', 'Foxes eat rabbits, not grass.'], ['Fewer rabbits ate the grass, so it fell', 'Rabbits rose, from 200 to 1400.']]"),
    # Examiner MUST FIX r4.0: mark point 3 ("the birds nested under shrubs") was not given anywhere.
    ('Ground-nesting birds: 30 pairs, then 12 pairs.',
     'Ground-nesting birds, which nest under the shrubs: 30 pairs, then 12 pairs.'),
    # Examiner SHOULD FIX practice Q3: stem and options kept (id and answer keys survive); the
    # explanations shouted and used dash asides.
    ('{ "1": "Some farms are physically large — size is not the primary reason. MONOCULTURE (one crop species) and removal of \'weeds\' and \'pests\' dramatically reduces biodiversity.", "2": "Farmland typically receives as much sunlight as natural ecosystems — light is not the reason for lower biodiversity.", "3": "Many animals do live on farmland — but the monoculture crop structure and use of pesticides/herbicides removes habitat and food for most species." }',
     '{ "1": "Size is not the reason. One crop dominates, and most other species are removed.", "2": "Farmland gets as much light as natural land. One crop dominates, and most other species are removed.", "3": "Many animals live on farmland. One crop dominates, and weeds and pests are removed, so most species lose their food and shelter." }'),
    # Blind doubt CF-5 (MED): the stem never said the larvae eat tadpoles. Stated now (NEW ID).
    ("'Information: a pond’s dragonfly larvae were removed.",
     "'Information: dragonfly larvae eat tadpoles. A pond’s dragonfly larvae were removed."),
]

LESSON = {
    "slug": "ecosystems",
    "start": {
        "setup": "One summer, every bee in a park disappears.",
        "question": "If you had to guess, would the park's flowers be fine, or would they suffer?",
        "options": [
            ("They would be fine",
             "They would suffer. Many flowers need bees to carry their pollen, so fewer seeds form."),
            ("They would suffer",
             "They would suffer. Many flowers need bees to carry their pollen, so fewer seeds form."),
        ],
        "answer": 1,
    },
    "words": ["population", "community", "ecosystem", "interdependence"],
    "knowledge": [
        {"kind": "reveal", "title": "Levels of organisation",
         "cols": ["What it is", "In a wood"],
         "rows": [
             ("Organism", "One living thing", "One robin"),
             ("Population", "All the individuals of one species living in an area",
              "All the robins in the wood"),
             ("Community", "All the populations of different species living in an area",
              "The robins, oaks, earthworms, fungi and bacteria"),
             ("Ecosystem", "A community interacting with the non-living (abiotic) parts of its "
              "environment", "The wood's living things with its soil, water, light and temperature"),
         ]},
        {"kind": "card", "title": "Ecosystem and habitat",
         "body": ["An ecosystem is the interaction of a community of living organisms (biotic) "
                  "with the non-living (abiotic) parts of their environment.",
                  "To survive and reproduce, organisms need a supply of materials from their "
                  "surroundings and from the other living organisms there.",
                  "A habitat is the place where an organism lives, such as a pond or the woodland "
                  "floor."]},
        {"kind": "card", "title": "Interdependence",
         "body": ["Within a community each species depends on other species for food, shelter, "
                  "pollination and seed dispersal.",
                  "If one species is removed it can affect the whole community. This is called "
                  "interdependence.",
                  "In this woodland web, solid arrows point from the food to the eater.",
                  {"slot": "legacy-fig:wFig"}]},
        {"kind": "reveal", "title": "Take one species out of the wood",
         "cols": ["What happens next"],
         "rows": [
             ("The wolves", "Nothing eats the deer, so deer numbers rise. More deer eat more grass, "
              "shrubs and flowering plants, so these fall. The bees that feed on the flowers fall "
              "too."),
             ("The bees", "The flowering plants are not pollinated, so they make fewer seeds and "
              "fall in number. Nothing ate the bees, but the plants depended on them."),
             ("The earthworms", "The shrews lose their food and fall in number. Leaf litter is no "
              "longer eaten, so it builds up."),
         ]},
        {"kind": "card", "title": "Competition",
         "body": ["Plants in a community often compete with each other for light and space, and "
                  "for water and mineral ions from the soil.",
                  "Animals often compete with each other for food, mates and territory.",
                  "An organism that loses the competition gets less of what it needs, so fewer of "
                  "its kind survive and breed."]},
        {"kind": "card", "title": "A stable community",
         "body": ["A stable community is one where all the species and environmental factors are "
                  "in balance so that population sizes remain fairly constant.",
                  "Individuals are born and die all the time. It is the population sizes that stay "
                  "fairly constant.",
                  "An undisturbed tropical rainforest and an ancient oak woodland are examples of stable "
                  "communities."]},
        {"kind": "card", "title": "Explain a change from data",
         "body": ["Say which number rose or fell, quote it, then link it to the next population.",
                  "Information (made up): sea otters were removed from a kelp forest. Sea urchins "
                  "rose from 20 to 80 per m². Kelp cover fell from 70% to 10%.",
                  {"points": [
                      "Otters ate sea urchins, so without otters more urchins survived: 20 rose to "
                      "80 per m².",
                      "Urchins eat kelp, so more urchins ate more kelp: cover fell from 70% to "
                      "10%.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A community and an ecosystem are the same thing.",
              "A community is the living organisms. An ecosystem is the community with the "
              "non-living parts."),
             ("Species only depend on each other for food.",
              "They also depend on each other for shelter, pollination and seed dispersal."),
             ("In a stable community nothing changes.",
              "Population sizes stay fairly constant. Individuals are still born and die."),
         ]}]},
    ],
    "key_fact": "An ecosystem is the interaction of a community of living organisms (biotic) with "
                "the non-living (abiotic) parts of their environment. Each species depends on "
                "other species for food, shelter, pollination and seed dispersal, so removing one "
                "species can affect the whole community.",
    "deeper": [
        {"kind": "card", "title": "Farmland",
         "body": ["A field growing one crop has far fewer species than a natural wood.",
                  "One crop dominates, and most other species are removed.",
                  "There is more on this in Biodiversity and Maintaining biodiversity."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Define</strong>: give the meaning of a word, such as population or "
             "ecosystem.",
             "<strong>Describe</strong>: say what something is or what happens, such as a stable "
             "community.",
             "<strong>Explain</strong>: say what happens and why. Use the numbers when you are "
             "given data.",
             "<strong>Suggest</strong>: use what you know on a habitat you have not met before.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-10", "logic_edits": LOGIC_EDITS},
}
