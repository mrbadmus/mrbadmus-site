# -*- coding: utf-8 -*-
"""Population and competition, in the lean shape. Spec table: ks4-population-competition.md.

LEGACY (batch 10). The ladder and the practice set stay from the Design page. The practice set is
the page's own BANK (all routes), so its fixes are logic_edits. Practice Q2 is replaced (new id); no other stem is edited.
"""

LOGIC_EDITS = [
    # Blind HIGH + examiner SHOULD, practice Q2: "Why is intraspecific competition more intense
    # than interspecific competition?" states an off-spec generalisation (not in 8464 or 8461
    # 4.7) as fact, and no option fix can remove a premise in the stem. Whole item replaced with
    # an on-spec item (4.7.1.1 animals compete for food; 4.7.1.3 one species outcompeting
    # another). NEW ID. This replaces the two earlier edits to Q2's options.
    ('V("Why is intraspecific competition more intense than interspecific competition?", [["Individuals of the same species have identical needs — they compete for exactly the same resources", true], ["Individuals of the same species are physically stronger and dominate others", false], ["Intraspecific competition involves more individuals — so it is more intense by numbers", false], ["Different species never compete — they never need the same resources", false, { stored: "Different species never compete — they always occupy different niches" }]], { "1": "Physical strength varies within a species — the intensity of competition is about OVERLAP OF RESOURCE NEEDS, not strength.", "2": "Many species are common — but interspecific competition can also involve large numbers. The intensity difference is about the degree of resource overlap.", "3": "Different species CAN compete — grey and red squirrels are a clear UK example. Species that compete for the same resources too closely cannot coexist indefinitely." })',
     "Q('Grey squirrels moved into a wood where red squirrels live. Both eat the same nuts. Suggest why the number of red squirrels fell.', 'The grey squirrels competed with them for food', [['The red squirrels began eating the grey squirrels', 'Squirrels eat nuts, not other squirrels.'], ['The red squirrels now had more nuts to eat', 'Both species eat the nuts, so each red squirrel gets fewer.'], ['The red squirrels now had more space to live in', 'The grey squirrels take up space too, so the reds have less.']])"),
    # Practice set Q1 (predator peak after prey peak), stem kept: feedback 3 was muddled.
    ('"Migration can occur — but the time lag in predator-prey cycles is primarily a biological response time, not migration."',
     '"Predators do not need to move away. Their numbers rise later because they take time to breed."'),
    # Practice set Q4 (pondweed), stem kept, and Rung 2 Q2 (marram grass): the credited option was
    # visibly the longest. Distractors lengthened; replies kept.
    ("[['Food', 'Plants make their own food.'], ['Mates', 'That is an animal resource.'], ['Newts', 'Plants do not compete for animals.']]",
     "[['Food from the soil', 'Plants make their own food.'], ['Mates and territory', 'Those are animal resources.'], ['The newts and frogs', 'Plants do not compete for animals.']]"),
    ("['Food', 'Plants make their own food.'], ['Territory', 'Animals hold territories; plants do not.']",
     "['Food from the other plants', 'Plants make their own food.'], ['Territory and nest sites', 'Animals hold territories; plants do not.']"),
    # Examiner MUST FIX r2.1 (marram grass): the credited option was still visibly the longest.
    ("['Water and mineral ions from the sand', [",
     "['Water and mineral ions', ["),
    # Examiner SHOULD FIX practice Q1: explanations shouted and used dash asides. Options kept.
    ('"The lag is specifically about REPRODUCTION — it takes time for increased food to result in increased offspring. Predators eating prey actually reduces prey numbers."',
     '"Predators eating prey makes prey numbers fall. The predator peak comes later because predators take time to breed."'),
    ('"Prey outnumbering predators is normal — but the timing of peaks is about reproduction lag, not relative numbers."',
     '"Prey usually outnumber predators, but that does not set the timing. Predators take time to breed."'),
]

LESSON = {
    "slug": "population-competition",
    "start": {
        "setup": "Two seedlings share one small pot. A third seedling has a pot the same size to "
                 "itself.",
        "question": "If you had to guess, which grows bigger?",
        "options": [
            ("One of the pair",
             "The one on its own. It has all the pot's light, water, mineral ions and space. The "
             "pair compete for them."),
            ("The one on its own",
             "The one on its own. It has all the pot's light, water, mineral ions and space. The "
             "pair compete for them."),
        ],
        "answer": 1,
    },
    "words": ["competition", "territory", "predator", "prey"],
    "knowledge": [
        {"kind": "card", "title": "What plants compete for",
         "body": ["Plants in a community or habitat often compete with each other for light and "
                  "space, and for water and mineral ions from the soil.",
                  {"points": [
                      "<strong>Light</strong>: taller plants shade shorter ones, so the shorter "
                      "ones photosynthesise less.",
                      "<strong>Space</strong>: room for roots and leaves to spread.",
                      "<strong>Water and mineral ions</strong>: taken up from the soil by the "
                      "roots.",
                  ]},
                  {"slot": "fig:competition-resources"}]},
        {"kind": "card", "title": "What animals compete for",
         "body": ["Animals often compete with each other for food, mates and territory.",
                  {"points": [
                      "<strong>Food</strong>: prey, plants or nectar that is in short supply.",
                      "<strong>Mates</strong>: the chance to breed. Stags fight for it.",
                      "<strong>Territory</strong>: an area with food and nest sites. A robin sings "
                      "to hold its territory.",
                  ]},
                  "Animals compete for mates only with their own species."]},
        {"kind": "card", "title": "Suggest what they compete for",
         "body": ["First decide whether each organism is a plant or an animal. Then choose from "
                  "that list.",
                  "A hedgerow holds hawthorn bushes, blackbirds and robins.",
                  {"points": [
                      "The hawthorn bushes compete for light, space, water and mineral ions.",
                      "The blackbirds and robins compete for food and territory.",
                  ]}]},
        {"kind": "card", "title": "Within and between species",
         "body": ["Competition within one species is called intraspecific competition. "
                  "Competition between different species is called interspecific competition.",
                  "Competition within a species is usually the strongest, because the individuals "
                  "need the same resources.",
                  "Grey squirrels outcompete red squirrels for food and nesting sites. In many "
                  "areas there are now too few red squirrels left to breed."]},
        {"kind": "card", "title": "What limits a population",
         "body": ["A population cannot grow for ever. Its size is limited by:",
                  {"points": [
                      "<strong>food</strong>: when it runs short, fewer survive and breed",
                      "<strong>water</strong>: a dry season limits plants and the animals that "
                      "eat them",
                      "<strong>space</strong>: territory and nest sites run out",
                      "<strong>predators</strong>: more predators, fewer prey survive",
                      "<strong>disease</strong>: pathogens spread quickly through a crowded "
                      "population",
                  ]}]},
        {"kind": "card", "title": "Predators and prey",
         "body": ["Consumers that kill and eat other animals are predators, and those eaten are "
                  "prey.",
                  "In a stable community the numbers of predators and prey rise and fall in "
                  "cycles.",
                  {"points": [
                      "Lots of prey means lots of food, so more predators survive and breed.",
                      "More predators eat more prey, so prey numbers fall.",
                      "With less food, fewer predators survive, so predator numbers fall.",
                      "With fewer predators, more prey survive, so prey numbers rise again.",
                  ]}]},
        {"kind": "card", "title": "Reading a predator-prey graph",
         "body": ["Predators take time to breed, so the predator peak comes after the prey peak. "
                  "This delay is the lag.",
                  {"slot": "fig:predator-prey-graph"},
                  "To find the lag, read the year of each peak and subtract.",
                  "On this graph the hares peak at year 2 and the lynx at about year 3.5. The lag "
                  "is about 1.5 years."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Predators and prey peak at the same time.",
              "The predator peak comes after the prey peak."),
             ("Plants compete for food.",
              "Plants make their own food. They compete for light, space, water and mineral ions."),
             ("Different species compete for mates.",
              "Animals compete for mates with their own species."),
         ]}]},
    ],
    "key_fact": "Plants compete for light and space, and for water and mineral ions from the "
                "soil; animals compete for food, mates and territory. In a stable community "
                "predator and prey numbers rise and fall in cycles, and the predator peak comes "
                "after the prey peak because predators take time to breed.",
    "deeper": [
        {"kind": "card", "title": "Native and American crayfish",
         "body": ["American signal crayfish were brought to British rivers.",
                  "They outcompete the native white-clawed crayfish for food and shelter.",
                  "They also carry crayfish plague, a disease that kills the native crayfish."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Suggest</strong>: say what organisms in a habitat you have not met before "
             "compete for.",
             "<strong>Interpret</strong>: read values from a predator-prey graph and find the "
             "lag.",
             "<strong>Explain</strong>: say why the predator peak comes after the prey peak.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-10", "logic_edits": LOGIC_EDITS},
}
