"""Biology · Ecology — the MRB-338 expansion of `role-of-biotechnology`.

One leaf only: AQA 8461 §4.7.5.4, Biology-only. The original twelve rows in
`ecology__b.py` take yeast as traditional biotechnology, what is inserted into
a GM plant, micropropagation by name, why mycoprotein is efficient, selective
breeding against genetic engineering, Bt maize, seed patents, the allergen
concern, Golden Rice, Bt pollen on milkweed, mycoprotein against beef, and a
proposed ban.

This file takes what they leave. The recall band finishes the named products
and the named organism: Fusarium grown in a fermenter on glucose syrup, and
mycoprotein as a FUNGUS — not an animal and not a plant, which is the
misconception the lesson flags. Around it sit insulin from modified bacteria,
herbicide tolerance, drought tolerance, and the concerns the baseline does not
reach: gene flow to wild relatives, antibiotic-resistance markers, labelling,
regulation, and who ends up owning the seed.

The weight is even at fourteen a band: this is a Triple-only spec point whose
recall is a list of named examples and whose demand is entirely about weighing
a real benefit against a real risk.

⚠️ This leaf stays on biotechnology in FOOD PRODUCTION. The mechanism of
genetic engineering — enzymes, vectors, plasmids — belongs to the inheritance
topic, and trophic efficiency to `transfer-of-biomass`.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The named organism and products, and the vocabulary the baseline
    # leaves unstated.
    {
        "id": "ks4-role-of-biotechnology-e05",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the kingdom that the organism used to make mycoprotein "
                "belongs to.",
        "options": [
            "Plants",
            "Bacteria",
            "Fungi",
            "Animals",
        ],
        "correct_index": 2,
        "why": "Mycoprotein comes from the fungus Fusarium, which is why "
               "calling it a plant protein or an animal product is wrong.",
    },
    {
        "id": "ks4-role-of-biotechnology-e06",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the vessel in which mycoprotein is grown on an "
                "industrial scale.",
        "options": [
            "A fermenter",
            "A greenhouse",
            "A centrifuge",
            "A fume cupboard",
        ],
        "correct_index": 0,
        "why": "A large fermenter supplies the glucose syrup, oxygen, warmth "
               "and stirring the fungus needs, under sterile conditions.",
    },
    {
        "id": "ks4-role-of-biotechnology-e07",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the food source supplied to the fungus that makes "
                "mycoprotein.",
        "options": [
            "Powdered meat",
            "Crushed rock",
            "Sea water",
            "Glucose syrup",
        ],
        "correct_index": 3,
        "why": "The fungus converts a carbohydrate — glucose syrup — into "
               "protein, and does so faster than a farm animal can.",
    },
    {
        "id": "ks4-role-of-biotechnology-e08",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the human hormone now produced by genetically modified "
                "bacteria.",
        "options": [
            "Thyroxine",
            "Insulin",
            "Adrenaline",
            "Testosterone",
        ],
        "correct_index": 1,
        "why": "Bacteria carrying the human insulin gene make the hormone in "
               "fermenters, which is how almost all insulin is now supplied.",
    },
    {
        "id": "ks4-role-of-biotechnology-e09",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a herbicide-resistant GM crop allows a farmer to "
                "do.",
        "options": [
            "Spray a whole field to kill the weeds without harming the "
                "crop",
            "Grow the crop without adding any mineral ions to the soil "
                "beneath",
            "Harvest the whole crop several weeks earlier than it usually "
                "ripens each year",
            "Stop insects feeding on the crop without any spraying",
        ],
        "correct_index": 0,
        "why": "The crop survives the herbicide, so weeds can be removed from "
               "the whole field in one pass rather than around each plant.",
    },
    {
        "id": "ks4-role-of-biotechnology-e10",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the characteristic a drought-tolerant GM crop has been "
                "engineered to have.",
        "options": [
            "It grows to a far greater height than usual",
            "It ripens at exactly the same time across a whole field",
            "It resists every insect pest that attacks it",
            "It survives and yields where rainfall is low",
        ],
        "correct_index": 3,
        "why": "Drought tolerance matters for food security in regions whose "
               "rainfall is falling as the climate changes.",
    },
    {
        "id": "ks4-role-of-biotechnology-e11",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the substance Golden Rice was engineered to make.",
        "options": [
            "Insulin",
            "Beta-carotene",
            "Haemoglobin",
            "Chlorophyll",
        ],
        "correct_index": 1,
        "why": "Beta-carotene is converted to vitamin A in the body, and "
               "vitamin A deficiency is a leading cause of childhood "
               "blindness.",
    },
    {
        "id": "ks4-role-of-biotechnology-e12",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by gene flow from a GM crop.",
        "options": [
            "Its genes move from one cell to another within the very same "
                "plant",
            "Its seed is carried to another farm by birds and by the wind",
            "Its pollen carries the inserted gene into a related wild "
                "plant",
            "Its genes are removed from the crop before the harvest is "
                "finally taken in",
        ],
        "correct_index": 2,
        "why": "Pollen from a GM crop can fertilise a wild relative, which is "
               "how a herbicide-tolerance gene could reach a weed.",
    },
    {
        "id": "ks4-role-of-biotechnology-e13",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name one traditional fermented food made using "
                "microorganisms.",
        "options": [
            "Boiled rice",
            "Roast potato",
            "Fresh milk",
            "Yoghurt",
        ],
        "correct_index": 3,
        "why": "Yoghurt, cheese, bread, beer and wine are all made by letting "
               "microorganisms act on a food, which is biotechnology at its "
               "oldest.",
    },
    {
        "id": "ks4-role-of-biotechnology-e14",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one advantage of growing plants by tissue culture "
                "rather than from seed.",
        "options": [
            "The plants can be grown without any water being supplied to "
                "them",
            "Every plant produced is genetically identical to the parent",
            "Each plant that is produced is genetically different from its "
                "parent plant",
            "The plants need no light while they are being grown on",
        ],
        "correct_index": 1,
        "why": "Tissue culture clones a chosen variety, so a grower gets "
               "thousands of identical, disease-free plants quickly from a "
               "small piece of tissue.",
    },
    {
        "id": "ks4-role-of-biotechnology-e15",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why the inside of a fermenter is kept sterile.",
        "options": [
            "The law requires every industrial vessel to be kept sterile",
            "Sterile conditions remove the need to supply the fungus "
                "oxygen",
            "Other microorganisms would compete with the fungus and spoil "
                "the product",
            "Sterile conditions make the fungus grow to a much larger size",
        ],
        "correct_index": 2,
        "why": "A contaminating microorganism would use the glucose, produce "
               "its own waste and make the batch unusable.",
    },
    {
        "id": "ks4-role-of-biotechnology-e16",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one social concern raised about GM seed rather than a "
                "health or environmental one.",
        "options": [
            "Large companies patent the varieties and farmers must buy new "
                "seed",
            "The crops may produce a new protein that some of the people "
                "eating it are allergic to",
            "Pollen from the crop may reach a related wild plant nearby",
            "Fields of one GM variety support very few wild species",
        ],
        "correct_index": 0,
        "why": "Patents, dependence on corporate suppliers and the cost to "
               "small-scale farmers are social and economic concerns, separate "
               "from safety.",
    },
    {
        "id": "ks4-role-of-biotechnology-e17",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why food containing GM ingredients must be labelled in "
                "the United Kingdom.",
        "options": [
            "Because the label proves the food has not been tested",
            "So that consumers can choose for themselves whether to buy it",
            "So that the crop can be traced back to the very field where "
                "it was grown",
            "Because GM food must be cooked quite differently from other "
                "food",
        ],
        "correct_index": 1,
        "why": "Labelling exists so that people can make an informed choice; "
               "it is not itself a safety warning.",
    },
    {
        "id": "ks4-role-of-biotechnology-e18",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason mycoprotein is described as a sustainable "
                "food.",
        "options": [
            "It is harvested directly from the woodland rather than being "
                "grown",
            "It contains no protein, so it needs no nitrogen to be made",
            "It uses far less land and water than the same mass of meat",
            "It grows without any energy input of any kind being needed",
        ],
        "correct_index": 2,
        "why": "Growing a fungus in a fermenter needs a fraction of the land, "
               "water and feed that rearing cattle for the same protein does.",
    },
    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # Each application and each concern in a named context.
    {
        "id": "ks4-role-of-biotechnology-s05",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why producing insulin from genetically modified "
                "bacteria is better than extracting it from animals.",
        "options": [
            "Animal insulin is poisonous, so nobody could ever safely be "
                "given it",
            "Bacterial insulin does not need to be injected into a patient",
            "The bacteria make human insulin in large amounts, and it "
                "suits every patient",
            "Bacteria make insulin without needing any food supplied to "
                "them",
        ],
        "correct_index": 2,
        "why": "The bacterial product is the human protein, made in quantity "
               "and at low cost, so supply is reliable and no patient is "
               "limited by an animal source.",
    },
    {
        "id": "ks4-role-of-biotechnology-s06",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a herbicide-tolerance gene could reach a weed "
                "growing at the edge of a GM field.",
        "options": [
            "Pollen from the crop fertilises a wild relative of the same "
                "plant family",
            "The weed absorbs the gene through its own roots out of the "
                "soil that lies beneath it",
            "The herbicide carries the gene from the crop onto the weed's "
                "leaves",
            "The weed eats part of the crop and takes the gene in with the "
                "food",
        ],
        "correct_index": 0,
        "why": "Gene flow happens by pollination, so it needs a sexually "
               "compatible wild relative growing near enough to be fertilised.",
    },
    {
        "id": "ks4-role-of-biotechnology-s07",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a grower would choose tissue culture to increase "
                "the number of a new apple variety quickly.",
        "options": [
            "Seeds from the new variety would germinate far too slowly to "
                "be useful",
            "Tissue culture changes the variety into a better one within a "
                "single season",
            "The variety would otherwise have to be bought in from a "
                "completely different country",
            "Thousands of identical plants can be produced from a small "
                "piece of tissue",
        ],
        "correct_index": 3,
        "why": "Apple seeds do not breed true, so the only way to keep the new "
               "variety's characteristics is to clone it, and tissue culture "
               "does that fastest.",
    },
    {
        "id": "ks4-role-of-biotechnology-s08",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fermenter produces 1.2 tonnes of mycoprotein per day. "
                "Calculate the mass produced in a 30 day month.",
        "options": [
            "25 tonnes",
            "36 tonnes",
            "3.6 tonnes",
            "360 tonnes",
        ],
        "correct_index": 1,
        "why": "1.2 tonnes per day × 30 days = 36 tonnes in the month.",
    },
    {
        "id": "ks4-role-of-biotechnology-s09",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fungus converts carbohydrate into protein "
                "faster than a cow does.",
        "options": [
            "It does not move or keep itself warm, so less energy is "
                "respired away",
            "It has no cells, so none of the food it takes in is broken "
                "down",
            "It photosynthesises as well as feeding, which adds a great "
                "deal of extra protein",
            "It takes its protein directly from the air inside the "
                "fermenter",
        ],
        "correct_index": 0,
        "why": "A mammal spends most of its food's energy on movement and on "
               "maintaining body temperature; a fungus in a warmed fermenter "
               "spends almost none.",
    },
    {
        "id": "ks4-role-of-biotechnology-s10",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an antibiotic-resistance marker gene in a GM "
                "plant worries some scientists.",
        "options": [
            "It makes the plant itself resistant to every antibiotic that "
                "any farmer might use",
            "It stops the crop from being able to take up any mineral ions",
            "It prevents the plant from being eaten by any insect pest",
            "It might transfer to gut bacteria and make an infection "
                "harder to treat",
        ],
        "correct_index": 3,
        "why": "The concern is transfer: a resistance gene moving from the "
               "crop into bacteria in a gut would add to the antibiotic "
               "resistance problem.",
    },
    {
        "id": "ks4-role-of-biotechnology-s11",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why growing Bt maize can help pollinating insects on "
                "a farm.",
        "options": [
            "Bt maize produces more nectar than an ordinary maize plant "
                "does",
            "Less insecticide is sprayed, so fewer non-target insects are "
                "killed",
            "The Bt toxin is a food source that the pollinating insects "
                "are able to feed on",
            "Bt maize flowers for much longer, so pollinators have more "
                "time to feed",
        ],
        "correct_index": 1,
        "why": "The toxin is made inside the plant and acts on the "
               "caterpillars eating it, so the broad-spectrum sprays that "
               "would otherwise be used are not needed.",
    },
    {
        "id": "ks4-role-of-biotechnology-s12",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a longer shelf life in a GM tomato reduces the "
                "resources used to feed people.",
        "options": [
            "Longer-lasting tomatoes are grown without any fertiliser "
                "being used",
            "The tomato ripens in the shop rather than in the field",
            "Less of the crop is thrown away, so less has to be grown",
            "The tomato contains far more energy per kilogram than usual",
        ],
        "correct_index": 2,
        "why": "Food waste is food already grown with land, water and "
               "fertiliser, so cutting waste cuts every input behind it.",
    },
    {
        "id": "ks4-role-of-biotechnology-s13",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a farmer in a poorer country may be unable to "
                "benefit from a GM variety that suits their conditions.",
        "options": [
            "GM seed is illegal to be planted anywhere outside a wealthy "
                "country",
            "The variety changes back to an ordinary one after one season",
            "GM seed needs a machine that has not yet been invented in "
                "order to sow it",
            "The seed is patented and must be bought new each year at a "
                "price",
        ],
        "correct_index": 3,
        "why": "Access is the social issue the specification names: a "
               "technology that works is of no use to a farmer who cannot "
               "afford the seed or is barred from saving it.",
    },
    {
        "id": "ks4-role-of-biotechnology-s14",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a GM crop is tested for years before it may be "
                "sold in the United Kingdom.",
        "options": [
            "Testing proves that the crop is identical to the wild variety",
            "Testing checks for effects on health and on the environment "
                "before release",
            "Testing is needed to find out what colour the crop will grow",
            "Testing allows the company to raise the price of the seed",
        ],
        "correct_index": 1,
        "why": "Regulation exists precisely because some concerns are real: "
               "safety testing and environmental assessment come before "
               "approval.",
    },
    {
        "id": "ks4-role-of-biotechnology-s15",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why replacing wild varieties with one GM variety "
                "across a region reduces biodiversity.",
        "options": [
            "One variety needs more land than several varieties would need",
            "GM crops take all the carbon dioxide from the air around them",
            "The genetic variety held in the many local varieties is lost",
            "GM plants release a chemical that kills every wild plant "
                "growing nearby",
        ],
        "correct_index": 2,
        "why": "Local varieties carry alleles bred over centuries for local "
               "conditions, and replacing them with one uniform variety throws "
               "that variation away.",
    },
    {
        "id": "ks4-role-of-biotechnology-s16",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why mycoprotein is described as a meat substitute "
                "rather than a vegetable.",
        "options": [
            "It is high in protein and low in fat, so it replaces meat in "
                "a meal",
            "It is grown in the soil in a field, in exactly the same way "
                "as a vegetable",
            "It comes from an animal, and so it has to be described as a "
                "substitute for meat",
            "It contains no protein, unlike a vegetable, which does",
        ],
        "correct_index": 0,
        "why": "Its protein content and texture let it take meat's place in a "
               "diet, which is what a substitute means, and it is neither a "
               "plant nor an animal.",
    },
    {
        "id": "ks4-role-of-biotechnology-s17",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "1 kg of beef needs 15 000 litres of water and 1 kg of "
                "mycoprotein needs 750 litres. Calculate how many times more "
                "water the beef needs.",
        "options": [
            "200 times",
            "20 times",
            "15 times",
            "2 times",
        ],
        "correct_index": 1,
        "why": "15 000 ÷ 750 = 20, so beef needs twenty times the water.",
    },
    {
        "id": "ks4-role-of-biotechnology-s18",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a buffer zone of ordinary crop is planted around "
                "a GM trial field.",
        "options": [
            "It marks out the boundary so that the inspectors are able to "
                "find the field",
            "It uses up the fertiliser the trial crop does not need",
            "It catches the pollen, so less of it reaches wild plants "
                "beyond",
            "It gives the trial crop some shelter from the wind and from "
                "the rain",
        ],
        "correct_index": 2,
        "why": "A separation distance planted with non-GM crop reduces the "
               "chance of pollen reaching wild relatives or a neighbour's "
               "field.",
    },
    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Benefit weighed against risk, with the evidence separated from the
    # speculation.
    {
        "id": "ks4-role-of-biotechnology-h05",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A weed near a GM field becomes herbicide tolerant. Explain "
                "the consequence for the farmer.",
        "options": [
            "The GM crop loses its own tolerance and is killed by the next "
                "spray",
            "The weed stops competing with the crop once it has the new "
                "gene",
            "That herbicide no longer controls the weed, so another must "
                "be found",
            "The weed becomes a crop plant and can then be harvested "
                "together with the GM crop",
        ],
        "correct_index": 2,
        "why": "The advantage the GM crop gave depended on the weeds being "
               "susceptible; once a weed shares the tolerance, that particular "
               "herbicide is useless against it.",
    },
    {
        "id": "ks4-role-of-biotechnology-h06",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the argument that GM crops must be unsafe because "
                "they are unnatural.",
        "options": [
            "It is weak, because safety depends on what the inserted gene "
                "does and not on how it arrived",
            "It is sound, because a gene moved by people behaves quite "
                "differently from a natural one",
            "It is sound, because every natural food has been shown to be "
                "perfectly safe to eat",
            "It is weak, because no GM crop has been shown to carry any "
                "risk",
        ],
        "correct_index": 0,
        "why": "The question an examiner wants separated is evidence from "
               "unease: each modification has to be assessed on what it "
               "actually produces in the plant.",
    },
    {
        "id": "ks4-role-of-biotechnology-h07",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare selective breeding and genetic engineering as ways of "
                "adding drought tolerance to a crop.",
        "options": [
            "Breeding is faster and more precise, while engineering takes "
                "many generations",
            "Breeding changes no genes, while engineering changes every "
                "gene in the plant",
            "The two are identical, because both give a plant a "
                "characteristic it lacked",
            "Breeding needs the trait to exist in a relative; engineering "
                "can take it from any species",
        ],
        "correct_index": 3,
        "why": "Selective breeding can only recombine variation that already "
               "exists in plants that will cross; engineering can move a "
               "single named gene from anywhere.",
    },
    {
        "id": "ks4-role-of-biotechnology-h08",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate Golden Rice as a way of preventing vitamin A "
                "deficiency, compared with giving out vitamin supplements.",
        "options": [
            "The two are identical, because both deliver the same mass of "
                "vitamin A to a person",
            "Rice reaches people who grow their own food; supplements need "
                "a supply chain each year",
            "Supplements are better in every case, because they contain "
                "vitamin A rather than beta-carotene",
            "Rice is better in every case, because no crop ever fails and "
                "no supplement ever works",
        ],
        "correct_index": 1,
        "why": "A staple crop keeps delivering once it is grown locally, while "
               "a supplement programme has to be funded, distributed and "
               "repeated indefinitely.",
    },
    {
        "id": "ks4-role-of-biotechnology-h09",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A GM crop raises a yield of 3.5 tonnes per hectare by 20% but "
                "its seed costs 60 pounds per hectare more. Determine the "
                "extra tonnes gained per hectare.",
        "options": [
            "0.7 tonnes",
            "0.2 tonnes",
            "4.2 tonnes",
            "7.0 tonnes",
        ],
        "correct_index": 0,
        "why": "20% of 3.5 tonnes is 0.20 × 3.5 = 0.7 tonnes more per hectare.",
    },
    {
        "id": "ks4-role-of-biotechnology-h10",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why caterpillars feeding on Bt maize may become "
                "resistant to the toxin over several seasons.",
        "options": [
            "The caterpillars learn to avoid the parts of the plant that "
                "contain the toxin",
            "The toxin weakens as the crop grows, so later caterpillars "
                "meet a smaller dose",
            "Caterpillars change into a different species once they have "
                "eaten the toxin",
            "Individuals that survive the toxin breed, so resistance "
                "spreads through the population",
        ],
        "correct_index": 3,
        "why": "A crop expressing the toxin all season is a constant selection "
               "pressure, which is why growers are required to plant a refuge "
               "of non-Bt crop alongside.",
    },
    {
        "id": "ks4-role-of-biotechnology-h11",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a field of tissue-cultured plants is at greater "
                "risk from a new disease than a field grown from seed.",
        "options": [
            "Cloned plants have no cell walls, so a pathogen enters easily",
            "The cloned plants are genetically identical, so none can "
                "resist it",
            "Cloned plants are much weaker, because they were grown in a "
                "laboratory first",
            "Plants from seed are sprayed more often than cloned plants "
                "are",
        ],
        "correct_index": 1,
        "why": "Cloning removes genetic variation, so a pathogen that "
               "overcomes one plant's defences overcomes every plant in the "
               "field.",
    },
    {
        "id": "ks4-role-of-biotechnology-h12",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that mycoprotein could replace all farmed "
                "meat.",
        "options": [
            "It could not replace any meat, because it contains no usable "
                "protein",
            "It could replace all meat, because everybody prefers its "
                "taste to meat",
            "It uses far fewer resources, but diet, culture and cost all "
                "limit how far it spreads",
            "It could replace all meat at once, because it is cheaper to "
                "make",
        ],
        "correct_index": 2,
        "why": "The resource case is strong and the barriers are real: what "
               "people will eat, what they can afford, and the industries "
               "built on livestock.",
    },
    {
        "id": "ks4-role-of-biotechnology-h13",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "1 kg of mycoprotein needs 6 square metres of land and 1 kg of "
                "beef needs 150 square metres. Determine the land saved per 50 "
                "kg of protein switched.",
        "options": [
            "144 square metres",
            "7800 square metres",
            "300 square metres",
            "7200 square metres",
        ],
        "correct_index": 3,
        "why": "The saving is 150 − 6 = 144 square metres per kilogram, and "
               "144 × 50 = 7200 square metres.",
    },
    {
        "id": "ks4-role-of-biotechnology-h14",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a company may be reluctant to develop a GM crop "
                "for a small, poor farming region.",
        "options": [
            "A small region needs a different kind of gene from a large "
                "one",
            "Development costs are high and the seed sales there would not "
                "repay them",
            "The crops that are grown in the poorer regions are unable to "
                "be genetically modified",
            "The law forbids a company from selling GM seed in a poor "
                "country",
        ],
        "correct_index": 1,
        "why": "The research is expensive and is funded by seed sales, so "
               "crops grown by people who cannot pay are the ones least likely "
               "to be developed.",
    },
    {
        "id": "ks4-role-of-biotechnology-h15",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a study finding no harm from one GM crop cannot "
                "show that all GM crops are safe.",
        "options": [
            "GM crops change after they have been studied and approved",
            "Safety is decided by public opinion rather than by a "
                "scientific study",
            "Each crop carries a different gene making a different protein",
            "One study is too small to show anything about safety",
        ],
        "correct_index": 2,
        "why": "GM is a method, not a product: the safety question is about "
               "what the particular inserted gene causes the plant to make, so "
               "it is asked afresh each time.",
    },
    {
        "id": "ks4-role-of-biotechnology-h16",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the risk of gene flow from a GM crop with no wild "
                "relatives in a country with that from one that has many.",
        "options": [
            "With no compatible wild relative there is nothing for the "
                "pollen to fertilise",
            "The risk is the same, because pollen travels the same "
                "distance in both cases",
            "The crop with many relatives is safer, because the gene is "
                "diluted among them",
            "Gene flow needs no relative, because pollen can fertilise any "
                "plant that it lands on",
        ],
        "correct_index": 0,
        "why": "Gene flow requires successful fertilisation, so the risk "
               "depends entirely on whether a sexually compatible wild "
               "relative grows within pollen range.",
    },
    {
        "id": "ks4-role-of-biotechnology-h17",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate a decision to grow mycoprotein in a country where "
                "electricity comes mainly from coal.",
        "options": [
            "The decision is wrong: mycoprotein cannot be made where coal "
                "is burned",
            "The land and water savings remain, but the fermenter's power "
                "carries its own emissions",
            "There is no benefit, because a fermenter uses more energy "
                "than a farm",
            "The benefit is unchanged, because a fermenter needs no "
                "electricity",
        ],
        "correct_index": 1,
        "why": "The comparison has to include every input: the resource case "
               "for mycoprotein is strong, and part of it is offset where the "
               "power is generated from fossil fuel.",
    },
    {
        "id": "ks4-role-of-biotechnology-h18",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a farmer may keep growing a conventional variety "
                "alongside a GM one that yields more.",
        "options": [
            "The conventional variety yields more than the GM one in a wet "
                "year",
            "A GM crop cannot be harvested unless another crop is grown "
                "beside it",
            "Some buyers will not take GM produce, so the second variety "
                "keeps that market",
            "Growing two varieties is required by law on any farm with a "
                "GM crop",
        ],
        "correct_index": 2,
        "why": "Market access is a commercial reality: a buyer, a country or a "
               "certification scheme that excludes GM produce is a reason to "
               "keep a non-GM crop in the rotation.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-role-of-biotechnology-s19",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Some vegetarian cheese is made using an enzyme (rennet) produced by "
                "genetically modified bacteria, instead of rennet extracted from a "
                "calf's stomach. Explain the benefit this brings to a vegetarian who "
                "wants to eat cheese.",
        "options": [
            "It removes the need for any starter culture when the cheese is first made",
            "It lets the cheese be produced without pasteurising the milk beforehand",
            "It lets vegetarians eat a cheese made without an enzyme extracted from a slaughtered calf",
            "It raises the amount of protein the finished cheese contains, compared with any other method",
        ],
        "correct_index": 2,
        "why": "GM bacterial rennet lets a vegetarian eat the cheese without an "
               "enzyme that came from a slaughtered calf.",
    },
    {
        "id": "ks4-role-of-biotechnology-s20",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Bt cotton has been genetically modified to produce its own "
                "insecticide against a common caterpillar pest. Explain the main "
                "benefit this brings to the farmer growing it.",
        "options": [
            "It removes the cotton plant's need for water for the rest of the growing season entirely",
            "It reduces how much chemical insecticide a farmer needs to spray to protect the crop from caterpillars",
            "It changes the colour of the cotton fibre so that it no longer ever needs to be dyed before use at any stage",
            "It removes the need for the cotton to be picked by hand or by machine once it has grown",
        ],
        "correct_index": 1,
        "why": "Bt cotton produces its own insecticide against the target pest, so "
               "the farmer needs to spray far less chemical insecticide to protect "
               "it.",
    },
    {
        "id": "ks4-role-of-biotechnology-s21",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Almost all commercially grown banana plants come from a variety that "
                "produces no viable seed. Explain why tissue culture is used to "
                "propagate this variety.",
        "options": [
            "It lets a grower collect and sow seed from this year's bananas to grow next year's identical crop easily",
            "It is used because banana seeds germinate unusually slowly compared with other tropical fruit",
            "It produces bananas that ripen more slowly than bananas grown any other way",
            "It produces large numbers of genetically identical plants from a fruit that does not produce viable seed",
        ],
        "correct_index": 3,
        "why": "Since this variety produces no viable seed, tissue culture is the "
               "only way to produce large numbers of genetically identical new "
               "plants from it.",
    },
    {
        "id": "ks4-role-of-biotechnology-s22",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain one difference in speed between introducing a chosen trait "
                "using genetic engineering and introducing the same trait using "
                "selective breeding.",
        "options": [
            "Genetic engineering can introduce a chosen trait in a single generation, while selective breeding needs many",
            "Selective breeding can introduce a chosen trait in a single generation, while genetic engineering needs many",
            "Both methods take roughly the same number of generations to introduce any new trait reliably",
            "Neither method can introduce a brand new trait; both simply strengthen a trait already present",
        ],
        "correct_index": 0,
        "why": "Genetic engineering can introduce a chosen trait directly, in a "
               "single generation, while selective breeding has to select for the "
               "trait over many generations.",
    },
    {
        "id": "ks4-role-of-biotechnology-s23",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a genetically modified crop cannot be certified as "
                "organic, whatever growing methods are used on it.",
        "options": [
            "It can be grown as organic provided no pesticide is used on it at any stage of growing",
            "It cannot be certified organic, since organic standards exclude genetically modified crops by definition",
            "It can be grown as organic provided the seed itself was not treated with any chemical whatsoever beforehand",
            "It can be grown as organic as long as the farm did not grow a GM crop in a previous year",
        ],
        "correct_index": 1,
        "why": "Organic certification standards specifically exclude genetically "
               "modified crops, regardless of what growing methods are then used on "
               "them.",
    },
    {
        "id": "ks4-role-of-biotechnology-s24",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A GM insect-resistant maize variety costs a farmer an extra 45 "
                "pounds per hectare in seed, but saves 70 pounds per hectare that "
                "would otherwise be spent on insecticide, on a 120-hectare farm. "
                "Calculate the farm's total net saving from choosing the GM variety.",
        "options": [
            "9 000 pounds, from applying the extra cost per hectare to the whole farm rather than the profit",
            "3 000 pounds, treating the seed cost alone as though it were the farm's total profit",
            "600 pounds, from comparing the two costs for a single hectare rather than the whole farm",
            "3 000 pounds, the total net saving once the extra seed cost is set against the insecticide saved",
        ],
        "correct_index": 3,
        "why": "Saving 70 pounds and spending an extra 45 pounds per hectare gives a "
               "net saving of 25 pounds per hectare, which across 120 hectares is 3 "
               "000 pounds.",
    },
    {
        "id": "ks4-role-of-biotechnology-s25",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the temperature inside a fermenter producing mycoprotein "
                "is carefully controlled at the fungus's optimum.",
        "options": [
            "Temperature is controlled mainly to change the final colour of the mycoprotein once it is harvested",
            "Temperature is controlled mainly to stop the fermenter itself from corroding over time",
            "Temperature is kept at the fungus's optimum so that it grows and reproduces as quickly as possible",
            "Temperature is controlled to stop the glucose feed from dissolving properly in the fermenter",
        ],
        "correct_index": 2,
        "why": "Keeping the fermenter at the fungus's optimum temperature lets it "
               "grow and reproduce as quickly as possible, maximising the "
               "mycoprotein produced.",
    },
    {
        "id": "ks4-role-of-biotechnology-s26",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain one way the fungus used to produce mycoprotein can be scaled "
                "up more quickly than raising cattle for beef.",
        "options": [
            "The fungus used for mycoprotein can be grown and harvested within days, far faster than raising cattle",
            "The fungus used for mycoprotein needs little glucose feed once its culture has first been established",
            "The fungus used for mycoprotein produces meat that is chemically identical to farmed beef",
            "The fungus used for mycoprotein can be grown mainly in the same regions where cattle are farmed",
        ],
        "correct_index": 0,
        "why": "The fungus used for mycoprotein can be grown and harvested within "
               "days, far faster than the months or years needed to raise cattle to "
               "slaughter weight.",
    },
    {
        "id": "ks4-role-of-biotechnology-h19",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate why some vegetarians consider cheese made using GM "
                "bacterial rennet more acceptable than cheese made using rennet "
                "extracted from a calf's stomach.",
        "options": [
            "They would not, since GM bacterial rennet and calf rennet raise exactly the same ethical objection",
            "They would not, since genetic modification itself is the objection most vegetarians raise about rennet",
            "They would, but just because GM rennet produces a cheese that tastes different from traditional cheese",
            "They would, since GM bacterial rennet avoids the objection to slaughtering a calf for its rennet",
        ],
        "correct_index": 3,
        "why": "GM bacterial rennet avoids the objection some vegetarians raise to "
               "using rennet extracted by slaughtering a calf, even though both are "
               "genetically identical to natural rennet in their effect.",
    },
    {
        "id": "ks4-role-of-biotechnology-h20",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the environmental impact of Bt cotton with the environmental "
                "impact of cotton grown using a conventional insecticide spray "
                "programme.",
        "options": [
            "Bt cotton has little meaningful environmental impact, compared with a conventional spray programme",
            "Bt cotton cuts the insecticide sprayed against its target pest, but other agrochemicals may still be needed",
            "Bt cotton needs exactly the same amount of insecticide as conventional cotton grown from ordinary seed",
            "Bt cotton removes every environmental concern a cotton farm could possibly have, once it is planted",
        ],
        "correct_index": 1,
        "why": "Bt cotton cuts the insecticide needed against its specific target "
               "pest, but a farmer may still need other agrochemicals such as "
               "herbicide, so it is not free of environmental impact.",
    },
    {
        "id": "ks4-role-of-biotechnology-h21",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Almost all commercially grown banana plants are genetically "
                "identical, produced by tissue culture, because the fruit is "
                "seedless. Evaluate the long-term risk this creates for the global "
                "banana industry.",
        "options": [
            "There is no real risk, since tissue-cultured bananas are said to be more resistant to disease than any other crop",
            "There is no real risk, since a fungal disease cannot infect a plant produced by tissue culture",
            "A single disease could threaten the entire global crop, since almost no genetic variation exists to resist it",
            "The risk applies just to a small minority of bananas, since most are grown from seed instead",
        ],
        "correct_index": 2,
        "why": "With almost no genetic variation among the plants, a single disease "
               "that this variety cannot resist could threaten the entire global "
               "crop at once.",
    },
    {
        "id": "ks4-role-of-biotechnology-h22",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A campaigner argues that genetic engineering should always be "
                "preferred over selective breeding because it introduces a trait far "
                "more quickly. Evaluate this argument.",
        "options": [
            "Speed is only one factor; genetic engineering raises separate cost, safety and public-acceptance issues that speed does not settle",
            "The argument holds completely, since speed is the main factor that should decide between the two methods",
            "The argument fails completely, since genetic engineering is not really any faster than selective breeding at all",
            "The argument cannot be assessed, since selective breeding and genetic engineering are said not to be used for the same trait",
        ],
        "correct_index": 0,
        "why": "Speed is a real advantage, but genetic engineering also raises "
               "separate cost, safety and public-acceptance questions that speed "
               "alone does not resolve.",
    },
    {
        "id": "ks4-role-of-biotechnology-h23",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region's farms are a patchwork of small organic and small GM "
                "fields side by side. Evaluate the challenge this creates for the "
                "organic farmers in particular.",
        "options": [
            "There is no real challenge, since pollen from a GM crop cannot travel as far as a neighbouring field",
            "There is no real challenge, since organic certification depends just on what the organic farmer sprays",
            "The challenge applies just when the organic farmer also grows the same crop species as the GM field",
            "Pollen drifting from the GM field could compromise the neighbouring organic farmer's crop and certification",
        ],
        "correct_index": 3,
        "why": "Pollen can drift from a GM field onto a neighbouring organic field, "
               "and organic certification specifically excludes any GM presence, "
               "however it arrived.",
    },
    {
        "id": "ks4-role-of-biotechnology-h24",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cotton farm sprays conventional cotton with insecticide 8 "
                "times a season, at a cost of 40 pounds per hectare each time. "
                "Switching to Bt cotton cuts this to 2 sprays a season, but the "
                "Bt seed costs an extra 85 pounds per hectare. Determine the "
                "farm's net saving per hectare from switching to Bt cotton.",
        "options": [
            "240 pounds, from the saved spraying alone, ignoring the extra cost of the Bt seed",
            "235 pounds, from adding the seed premium to the saved spraying instead of subtracting it",
            "320 pounds, treating the conventional spraying cost alone as the net saving",
            "155 pounds, once the 85 pound seed premium is subtracted from the 240 pounds saved on spraying",
        ],
        "correct_index": 3,
        "why": "Conventional spraying costs 8 times 40, or 320 pounds; Bt "
               "spraying costs 2 times 40, or 80 pounds, a saving of 240 "
               "pounds, minus the 85 pound seed premium, leaves 155 pounds.",
    },
    {
        "id": "ks4-role-of-biotechnology-h25",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare how quickly a fermenter of mycoprotein-producing fungus can "
                "be scaled up to meet a sudden rise in demand with how quickly a "
                "cattle herd producing beef can be scaled up to meet the same rise in "
                "demand.",
        "options": [
            "Neither can realistically be scaled up quickly, since both need years of planning before production changes",
            "A mycoprotein fermenter can be scaled up within days, while a cattle herd needs months or years to expand",
            "A cattle herd can be scaled up faster than a fermenter, since cows breed continuously throughout the year",
            "Both can be scaled up at exactly the same rate, since both ultimately depend on how much feed is available",
        ],
        "correct_index": 1,
        "why": "A fermenter can be scaled up and harvested within days, while a "
               "cattle herd takes months to reach slaughter weight and generations "
               "to expand in number.",
    },
    {
        "id": "ks4-role-of-biotechnology-h26",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A government must decide how to raise national food production: by "
                "expanding GM crop use, by expanding selective breeding programmes, "
                "or by investing in mycoprotein production facilities. Evaluate why "
                "there is no single 'best' answer to this choice.",
        "options": [
            "Each method differs in speed, cost, public acceptance and suitability, so the best choice depends on the context",
            "GM crops are usually the best answer, since they are consistently the fastest method available in every case",
            "Selective breeding is usually the best answer, since it raises no ethical objections of any kind whatsoever",
            "Mycoprotein is usually the best answer, since it alone can fully replace every crop and livestock farm in the whole country",
        ],
        "correct_index": 0,
        "why": "Each method differs in how fast it works, what it costs, how the "
               "public accepts it and which crops or animals it suits, so no single "
               "method is best in every situation.",
    },
]
