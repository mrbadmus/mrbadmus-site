# -*- coding: utf-8 -*-
"""Maintaining biodiversity, in the lean shape. Legacy Design page (batch 10): the ladder and the
practice set stay from it, with the fixes in logic_edits below.
Spec table: ks4-maintaining-biodiversity.md (AQA 8464 4.7.3.6 / 8461 4.7.3.6, the same words)."""

LESSON = {
    "slug": "maintaining-biodiversity",
    "start": {
        "setup": "Farmers pulled out many hedgerows to make bigger wheat fields.",
        "question": "If you had to guess, did the farms then have more or fewer bird species?",
        "options": [
            ("More",
             "Fewer. Hedgerows give birds food, nest sites and shelter that a wheat field cannot."),
            ("Fewer",
             "Fewer. Hedgerows give birds food, nest sites and shelter that a wheat field cannot."),
        ],
        "answer": 1,
    },
    "words": ["endangered", "extinct", "breeding programme", "field margin"],
    "knowledge": [
        {"kind": "reveal", "title": "Human interactions that harm or help",
         "cols": ["Effect on biodiversity"],
         "rows": [
             ("Clearing forest for cattle",
              "Harms it. The habitat is destroyed, so species are lost."),
             ("Dumping waste in landfill",
              "Harms it. Land is lost and pollution is caused."),
             ("Burning fossil fuels",
              "Harms it. Carbon dioxide rises, and global warming changes where species can live."),
             ("Replanting a hedgerow on a wheat farm",
              "Helps it. Wildlife gets food and shelter that the crop cannot give."),
             ("Recycling paper, glass and metal",
              "Helps it. Less waste goes to landfill."),
             ("Fencing off and replanting a rare wetland",
              "Helps it. A rare habitat and its species are protected."),
         ]},
        {"kind": "card", "title": "The programmes",
         "body": ["Scientists and concerned citizens have put in place programmes to reduce the "
                  "negative effects of humans on ecosystems and biodiversity. These include:",
                  {"points": [
                      "<strong>Breeding programmes for endangered species</strong>: zoos and "
                      "reserves breed rare animals to raise their numbers, and may release them into "
                      "the wild.",
                      "<strong>Protection and regeneration of rare habitats</strong>: for example "
                      "nature reserves, and restoring wetlands.",
                      "<strong>Reintroduction of field margins and hedgerows</strong> in "
                      "agricultural areas where farmers grow only one type of crop.",
                      "<strong>Reduction of deforestation and carbon dioxide emissions</strong> by "
                      "some governments.",
                      "<strong>Recycling resources</strong> rather than dumping waste in landfill.",
                  ]}]},
        {"kind": "card", "title": "Hedgerows and field margins",
         "body": ["A field margin is a strip at the edge of a field left for wild flowers and grasses.",
                  "A field of one crop gives food and shelter to very few species.",
                  "Hedgerows and field margins give insects, birds and mammals food and shelter, so "
                  "more species can live on the farm.",
                  {"slot": "legacy-fig:hFig"}]},
        {"kind": "card", "title": "Conflicting pressures",
         "body": ["Maintaining biodiversity competes with other needs:",
                  {"points": [
                      "<strong>Cost</strong>: programmes cost money that could be spent on other "
                      "things.",
                      "<strong>Land</strong>: land is needed for food and housing.",
                      "<strong>Jobs</strong>: some people earn a living from activities such as "
                      "logging.",
                  ]},
                  "To evaluate a programme, give the gain, give the cost, then make a judgement "
                  "using the information you are given."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Maintaining biodiversity just means stopping pollution.",
              "There are several programmes, from breeding programmes to hedgerows."),
             ("Conservation costs nothing.",
              "It costs money, land and sometimes jobs."),
             ("A breeding programme protects a habitat.",
              "It raises the numbers of an endangered species. Protecting habitats is a separate "
              "programme."),
         ]}]},
    ],
    "key_fact": "Programmes to maintain biodiversity include breeding programmes for endangered "
                "species, protection and regeneration of rare habitats, reintroduction of field "
                "margins and hedgerows, reduction of deforestation and carbon dioxide emissions, and "
                "recycling rather than landfill. Each has to be weighed against conflicting "
                "pressures such as cost, land for food and housing, and jobs.",
    "deeper": [
        {"kind": "card", "title": "Examples of rare habitats",
         "body": ["Coral reefs, mangroves and heathland are rare habitats that are protected and "
                  "regenerated."]},
        {"kind": "card", "title": "Using data to evaluate",
         "body": ["Quote the numbers on both sides.",
                  "For example: bird species rose from 9 to 17, but the wheat harvest fell from 400 "
                  "to 372 tonnes.",
                  "28 ÷ 400 × 100 = 7%, so the harvest fell by 7%."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: positive and negative human interactions, and the "
             "programmes.",
             "<strong>Explain</strong>: how an action changes biodiversity.",
             "<strong>Evaluate</strong>: a programme against the conflicting pressures, from the "
             "information given.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # The kept Design figure has no switch any more: draw the farm with hedgerows and
            # margins, which shows what a hedgerow and a field margin are. Its "17 bird species"
            # label was a made-up count shown as fact; it now names the crop.
            ("hFig: fig(() => this.hFig(s.h))", "hFig: fig(() => this.hFig(1))"),
            ("TX(340, 185, '17 bird species', 18, { fill: INK })",
             "TX(340, 185, 'one crop: wheat', 18, { fill: INK })"),
            # Three unlabelled black marks in the wheat read as nothing in particular: removed.
            ("[[120, 140], [500, 200], [300, 110]].map((p) => '<ellipse cx=\"' + p[0] + '\" cy=\"' "
             "+ p[1] + '\" rx=\"9\" ry=\"6\" fill=\"' + INK + '\"/>').join('')",
             "''"),
            # Rung 1, Q2: "Clean water" was arguable (reservoirs flood habitats).
            ("['Clean water', 'Protecting habitats tends to help clean water.']",
             "['Recycling more waste', 'Recycling helps biodiversity. It does not conflict with it.']"),
            # Rung 2, Q1: the right option was visibly the longest, and "They increase the crop
            # yield" was arguable (margins hold pollinators and pest predators).
            ("['They give insects, birds and mammals food and shelter', ['They increase the crop "
             "yield', 'The benefit is to wildlife.'], ['They stop all pests', 'They do not; they "
             "add habitat.']]",
             "['They give wildlife food and shelter', ['They let the farmer grow more of the crop', "
             "'The margins take land out of the crop. The benefit is to wildlife.'], ['They remove "
             "all the pests from the farm', 'They do not remove pests. They add habitat.']]"),
            # Rung 2, Q2: the right option was visibly the longest.
            ("['Forest habitats and the species in them survive', ['More land is freed for cattle', "
             "'That is the opposite.'], ['Carbon dioxide rises', 'Keeping forests lowers it.']]",
             "['Forest habitats and their species survive', ['More land is cleared for cattle "
             "ranches', 'That is the opposite of reducing deforestation.'], ['Carbon dioxide in the "
             "atmosphere rises', 'Fewer trees are burned, so less carbon dioxide is released.']]"),
            # Rung 3, chain 2: an evaluation's gain and cost can come in either order, so the chain
            # had two right orders and the "But" link forced one. Rewritten as a forced sequence.
            # Same position, same id. Evaluation stays in Rung 4.
            ("CHAIN('Evaluate', 'A village wants a nature reserve on land a farmer uses for wheat. "
             "Build a fair evaluation. Put the links in order.',\n            ['The reserve would "
             "protect a habitat and raise the number of species.', 'But the farmer loses land, "
             "income and perhaps jobs, and the reserve costs money to run.', 'A judgement weighs "
             "the gain in biodiversity against the cost in land, money and livelihoods.'],\n"
             "            [['Conservation is always right, so the farmer must give up the land.', "
             "'A judgement weighs both sides.'], ['Nature reserves cost nothing.', 'They need "
             "funding.']])",
             "CHAIN('Explain', 'A zoo breeds an endangered bird and releases the young into the "
             "wild. Explain how this helps maintain biodiversity. Put the links in order.',\n"
             "            ['The zoo breeds the birds in captivity, so their numbers rise.', 'Young "
             "birds are released into a suitable habitat in the wild.', 'The wild population "
             "grows, so the species is less likely to become extinct.'],\n            [['The "
             "breeding programme makes the species extinct.', 'It raises the numbers of an "
             "endangered species.'], ['The released birds become a new species.', 'They are the "
             "same species.']])"),
            # Practice set 1 (stem kept, id kept): "They increase the yield of the single crop" was
            # arguable. Feedback dashes removed.
            ('["They increase the yield of the single crop", false]',
             '["They let the farmer plant more of the single crop", false]'),
            ('"Their main benefit is biodiversity, not crop yield — they give wildlife food and '
             'shelter."',
             '"The margins take land out of the crop. Their benefit is food and shelter for '
             'wildlife."'),
            ('"Competition between species does not disappear — more species living there means '
             'more, not less, interaction; the gain is food and shelter for more species."',
             '"Competition between species does not disappear. The gain is food and shelter for '
             'more species."'),
            # Practice set 2 (stem and options kept, id kept): feedback dashes removed.
            ('"Conservation programmes need funding — that cost is one source of the conflict."',
             '"Conservation programmes need funding. That cost is one source of the conflict."'),
            ('"Breeding programmes exist because some endangered species cannot recover on their '
             'own — and this is not a conflict with human needs anyway."',
             '"Breeding programmes exist because some endangered species cannot recover on their '
             'own. This is not a conflict with human needs."'),
            # Practice set 3 (stem kept): the right option was visibly the longest.
            ("'Biodiversity rose a lot, but 300 homes were not built, so the town traded housing "
             "for wildlife'",
             "'Species rose by 90, but 300 homes were not built'"),
            ("[['There was no cost', 'The 300 houses are the cost.'], ['The reserve failed', "
             "'Species rose from 120 to 210.'], ['Houses are always more important', 'A judgement "
             "weighs both; it does not dismiss one side.']]",
             "[['There was no cost, because species rose', 'The 300 homes that were not built are "
             "the cost.'], ['The reserve failed, because no homes were built', 'Species rose from "
             "120 to 210.'], ['Houses always matter more than wildlife', 'A judgement weighs both "
             "sides. It does not dismiss one.']]"),
            # Practice set 4 (stem kept): the right option was visibly the longest, and "It
            # increases carbon dioxide" was arguable (recycling uses energy).
            ("'Less waste goes to landfill, so less land is lost and there is less pollution'",
             "'Less land is used for landfill sites'"),
            ("[['It feeds endangered species', 'Recycling is about resources and waste.'], ['It "
             "increases carbon dioxide', 'It reduces the need for new raw materials.'], ['It makes "
             "hedgerows grow', 'Hedgerows are a separate programme.']]",
             "[['It provides food for endangered species', 'Recycling is about resources and "
             "waste.'], ['It removes all pollution from rivers', 'Recycling reduces some "
             "pollution, but not all of it.'], ['It makes hedgerows grow back on farms', "
             "'Hedgerows are a separate programme.']]"),
            # Examiner MUST FIX r1.0: "Breeding programmes for endangered species" was far the longest.
            # Distractors lengthened; replies still hold.
            ("['Clearing forest for farmland'",
             "['Clearing tropical forest to make new farmland'"),
            ("['Dumping waste in landfill'",
             "['Dumping more household waste in landfill'"),
            # Examiner SHOULD FIX r1.1: the credited option was clearly the longest.
            ("['More wildlife'",
             "['More wild species living there'"),
            # Examiner MUST FIX practice Q1 (hedgerows): the credited option was the longest by 9.
            ('"They provide food and shelter for a wider range of species"',
             '"They give food and shelter to more species"'),
            # Examiner MUST FIX practice Q2 (conflict): the credited option was the longest by 12.
            ('"Protecting a habitat reduces land available for farming or building"',
             '"Protecting a habitat leaves less land for farms"'),
            # Examiner SHOULD FIX r4.0: the data give a 7% fall in the harvest, not in income.
            ("a 7% loss of income",
             "a 7% fall in the harvest"),
            # Examiner NOTE r4.0: credit any supported judgement, not only one verdict.
            ("'Judgement: a large gain in biodiversity for a modest loss of crop and a shared cost, so the scheme is worthwhile, though the farmer bears a real loss.'",
             "'Judgement: any reasoned judgement that weighs the gain in bird species against the fall in the harvest and the cost; for example, a large gain in biodiversity for a modest loss of crop and a shared cost.'"),
            # Examiner NOTE hFig: two unlabelled red dots on the hedges meant nothing.
            ("+ D.circ(560, 45, 5, RED) + D.circ(200, 318, 5, RED)",
             ""),
        ],
    },
}
