# -*- coding: utf-8 -*-
"""Food chains and food webs, in the lean shape. Spec table: ks4-food-chains-webs.md.

LEGACY (batch 10). The ladder and the practice set stay from the Design page. The practice set is
the page's own BANK: Triple routes get Q1 (trophic levels) + the four shared items, Combined routes
get the four shared items + Q5 (secondary consumer). Its fixes are logic_edits. No practice-set stem is edited; the Rung 2 Q1 prompt is reworded in place (id kept).
"""

LOGIC_EDITS = [
    # Practice set, Triple Q1 ("Why do food chains rarely have more than 4–5 trophic levels?"),
    # stem kept. The Triple spec talks of biomass passed between trophic levels; "Producers cannot
    # support more than 4 levels" was arguable; feedback said "thermodynamic" and "cognitive".
    ('[["Energy is lost at each level — so little remains by the top level that it cannot support many organisms", true], ["Top predators are too large to find enough food in most ecosystems", false], ["Longer food chains would be too complex for organisms to navigate", false], ["Producers cannot support more than 4 levels of consumers", false]], { "1": "Size can increase up a food chain, but the limiting factor is ENERGY, not size. Even small top predators need large amounts of food.", "2": "Food chains are not \'navigated\' by organisms — the limit is thermodynamic (energy loss), not cognitive.", "3": "Producers can support more levels in principle — the limit is the progressive loss of energy at each transfer, not some fixed rule about producers." }',
     '[["Only about 10% of the biomass passes to each next level", true], ["Top predators are too large to find enough food", false], ["Longer food chains would have too many predators", false], ["Producers can only be eaten by four kinds of animal", false]], { "1": "The limit is how much biomass is passed up the chain, not the size of the predator.", "2": "Each level has less biomass than the one below, so there is too little left to support another level.", "3": "Many kinds of animal eat producers. The limit is the biomass passed up at each level." }'),
    # Practice set shared Q1 (foxes killed, what happens to the grass), stem kept: feedback 1 was
    # muddled ("reduced decomposition adds some nutrients").
    ('"Fox death → reduced decomposition adds some nutrients, but the dominant effect is that MORE RABBITS eat MORE GRASS → grass DECREASES."',
     '"Fewer foxes means more rabbits survive, and more rabbits eat more grass, so the grass decreases."'),
    # Practice set shared Q2 (chain written fox, rabbit, grass), stem kept: the credited option was
    # visibly the longest, and two distractors described what the pupil had already done.
    ("'The arrows point the wrong way: they should point from grass to rabbit to fox'",
     "'The arrows point the wrong way'"),
    ("['The grass should be at the end', 'A chain begins with the producer, and the arrows run from it.']",
     "['The grass should be in the middle', 'Grass is the producer, so it starts the chain.']"),
    ("['The fox should be first', 'The producer comes first.']",
     "['The rabbit should be first', 'The producer comes first, so the chain starts with grass.']"),
    # Rung 2 Q2 (oak leaves chain): the credited option was visibly the longest.
    ("['Put the sparrowhawk first', 'The producer comes first.'], ['Remove the oak leaves', 'A chain begins with a producer.']",
     "['Put the sparrowhawk first and the oak leaves last', 'The producer comes first.'], ['Remove the oak leaves and start with the caterpillar', 'A chain begins with a producer.']"),
    # Examiner MUST FIX practice Q3 (CF/CH) / Q4 (TF/TH), producer item: the credited option
    # was twice as long as the distractors. Distractors lengthened; credited text kept.
    ("[['A rabbit', 'A rabbit is a primary consumer.'], ['A fungus', 'Fungi do not photosynthesise.'], ['An owl', 'An owl is a consumer.']]",
     "[['A rabbit in a field', 'A rabbit is a primary consumer.'], ['A fungus on a log', 'Fungi do not photosynthesise.'], ['An owl in a barn', 'An owl is a consumer.']]"),
    # Examiner SHOULD FIX r2.0: it described the food web in words and pointed at a figure the
    # ladder does not show. One feeding fact is enough. Blind doubt r2-1 (LOW): foxes can switch
    # to shrews, so the prompt asks for the most likely effect, and "unaffected" is made
    # explicit. Position kept (id kept).
    ("'In the field web, grass feeds rabbits and grasshoppers; foxes eat rabbits and shrews; shrews eat grasshoppers; owls eat shrews. A disease kills most of the rabbits. Explain the effect on the foxes.'",
     "'Foxes eat rabbits and shrews. A disease kills most of the rabbits. Explain the most likely effect on the foxes.'"),
    ("['Foxes are unaffected', 'Rabbits were their food.']",
     "['Foxes are unaffected by the rabbits dying', 'The foxes have lost part of their food.']"),
    # Examiner SHOULD FIX practice Q1 (CF/CH) / Q2 (TF/TH): explanations 2 and 3 shouted and
    # brought in mutualism, which is not on the spec. Options unchanged.
    ('"Plants ARE part of food webs — as producers. They are directly affected by herbivore (rabbit) population changes."',
     '"Grass is the producer in the web. More rabbits eat more of it."'),
    ('"Rabbits eat grass — this is a consumer-producer relationship (predation/herbivory), not mutualism. Rabbits benefit; grass is harmed."',
     '"Rabbits eat grass, so more rabbits means less grass."'),
    # Figure brief (lead, item 6) + examiner NOTE 5: chFig adds "level N" labels when its flag is
    # true, and trophic levels are Triple only (4.7.4, biology only). The lean builder may call
    # chFig with no flag or with a state number, so chFig now reads the route itself unless it is
    # given a true boolean: labels on TF/TH only, never on CF/CH.
    ("  chFig(T) {\n",
     "  chFig(T) {\n    if (typeof T !== 'boolean') T = this.flags().T;\n"),
]

LESSON = {
    "slug": "food-chains-webs",
    "start": {
        "setup": "Every fox in a field disappears.",
        "question": "If you had to guess, would there be more rabbits or fewer?",
        "options": [
            ("Fewer rabbits",
             "More rabbits. Foxes eat rabbits, so without foxes more rabbits survive and breed."),
            ("More rabbits",
             "More rabbits. Foxes eat rabbits, so without foxes more rabbits survive and breed."),
        ],
        "answer": 1,
    },
    "words": ["producer", "consumer", "food web", "predator"],
    "knowledge": [
        {"kind": "card", "title": "Producers",
         "body": ["Photosynthetic organisms are the producers of biomass for life on Earth.",
                  "All food chains begin with a producer which synthesises molecules. This is "
                  "usually a green plant or alga which makes glucose by photosynthesis."]},
        {"kind": "card", "title": "Food chains",
         "body": ["Feeding relationships within a community can be represented by food chains.",
                  "Producers are eaten by primary consumers, which in turn may be eaten by "
                  "secondary consumers and then tertiary consumers.",
                  "Each arrow points from the food to the eater. It shows the direction biomass "
                  "is transferred.",
                  {"slot": "legacy-fig:chFig"}]},
        {"kind": "reveal", "title": "A pond food chain: algae, pond snail, small fish, heron",
         "cols": ["Role", "Eats"],
         "rows": [
             ("Algae", "Producer", "Nothing. Algae make glucose by photosynthesis."),
             ("Pond snail", "Primary consumer", "Algae"),
             ("Small fish", "Secondary consumer", "Pond snails"),
             ("Heron", "Tertiary consumer", "Small fish"),
         ]},
        {"kind": "card", "title": "Predators and prey",
         "body": ["Consumers that kill and eat other animals are predators, and those eaten are "
                  "prey.",
                  "In the pond chain the heron is a predator and the small fish are its prey."]},
        {"kind": "card", "title": "Food webs",
         "body": ["Most animals eat more than one kind of food, so food chains join up into a food "
                  "web.",
                  "The organisms in a web depend on each other. Change one population and the "
                  "populations linked to it change too."]},
        {"kind": "card", "title": "Follow the arrows",
         "body": [{"slot": "legacy-fig:wFig"},
                  "In this web, the foxes die out. Follow the arrows one step at a time.",
                  {"points": [
                      "Foxes ate rabbits, so more rabbits survive. More rabbits eat more grass, so "
                      "the grass falls.",
                      "Foxes also ate shrews, so more shrews survive. Owls eat shrews, so the owls "
                      "have more food.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The arrow means 'eats'.",
              "The arrow points from the food to the eater. It shows where the biomass goes."),
             ("A food chain can start with an animal.",
              "Every food chain starts with a producer, usually a green plant or alga."),
             ("Only the animals that eat a species are affected when it dies out.",
              "Follow the web. Animals further along are affected too."),
         ]}]},
    ],
    "key_fact": "All food chains begin with a producer, usually a green plant or alga that makes "
                "glucose by photosynthesis. The arrows point from the food to the eater, and in a "
                "food web a change in one population changes the populations linked to it.",
    "deeper": [
        {"kind": "card", "title": "Trophic levels", "routes": ["TF", "TH"],
         "body": ["Each feeding level in a food chain is a trophic level. Level 1 is the "
                  "producers, level 2 the primary consumers, and so on.",
                  "Only approximately 10% of the biomass from each trophic level is transferred "
                  "to the level above it.",
                  "So little biomass is left after four or five levels that food chains are rarely "
                  "longer than that.",
                  "This is taught in full in Trophic levels and Transfer of biomass."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Draw</strong>: a food chain with the producer first and arrows from the "
             "food to the eater.",
             "<strong>Name</strong>: the producer and the primary, secondary and tertiary "
             "consumers.",
             "<strong>Explain</strong>: say what happens to one population when another changes, "
             "and why.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-10", "logic_edits": LOGIC_EDITS},
}
