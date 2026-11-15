# -*- coding: utf-8 -*-
"""Biodiversity, in the lean shape. New record, no legacy page.
Spec table: ks4-biodiversity.md (AQA 8464 4.7.3.1 / 8461 4.7.3.1, the same words in both)."""

LESSON = {
    "slug": "biodiversity",
    "start": {
        "setup": "One kind of insect dies out in two ponds. One pond has many different species. "
                 "The other has very few.",
        "question": "If you had to guess, which pond's community copes better?",
        "options": [
            ("The pond with many species",
             "The pond with many species. The animals that ate the insect have other foods, so they "
             "depend less on that one species."),
            ("The pond with few species",
             "The pond with many species. The animals that ate the insect have other foods, so they "
             "depend less on that one species."),
        ],
        "answer": 0,
    },
    "words": ["biodiversity", "species", "ecosystem", "stability"],
    "knowledge": [
        {"kind": "card", "title": "What biodiversity means",
         "body": ["Biodiversity is the variety of all the different species of organisms on Earth, "
                  "or within an ecosystem.",
                  "It counts every kind of living thing: plants, animals and microorganisms."]},
        {"kind": "card", "title": "Why a great biodiversity keeps an ecosystem stable",
         "body": ["A great biodiversity ensures the stability of ecosystems.",
                  "It reduces the dependence of one species on another for food, shelter and the "
                  "maintenance of the physical environment.",
                  {"points": [
                      "<strong>Food</strong>: an animal with several foods can switch if one is lost.",
                      "<strong>Shelter</strong>: there are many places to live, so losing one is not "
                      "the end.",
                      "<strong>The physical environment</strong>: many species help to keep it in "
                      "good condition. For example, plant roots hold the soil in place. If one "
                      "species is lost, others still do the job.",
                  ]},
                  "Arrows point from the food to the eater.",
                  {"slot": "fig:biodiversity-webs"}]},
        {"kind": "card", "title": "Why biodiversity matters to us",
         "body": ["The future of the human species on Earth relies on us maintaining a good level of "
                  "biodiversity.",
                  "We rely on other species for food, and many medicines first came from living things."]},
        {"kind": "card", "title": "Human activities that reduce biodiversity",
         "body": ["Many human activities are reducing biodiversity.",
                  {"points": [
                      "<strong>Waste</strong>: pollution kills plants and animals.",
                      "<strong>Deforestation</strong>: forest habitats are destroyed.",
                      "<strong>Global warming</strong>: some species can no longer live where they "
                      "used to.",
                  ]},
                  "Only recently have measures been taken to try to stop this reduction."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Biodiversity is the number of animals in an area.",
              "It is the variety of all the different species, plants and microorganisms too."),
             ("With more species, each one depends more on the others.",
              "A great biodiversity reduces the dependence of one species on another."),
             ("People have always protected biodiversity.",
              "Only recently have measures been taken to stop it falling."),
         ]}]},
    ],
    "key_fact": "Biodiversity is the variety of all the different species of organisms on Earth, or "
                "within an ecosystem. A great biodiversity makes an ecosystem stable, because it "
                "reduces the dependence of one species on another for food, shelter and the "
                "maintenance of the physical environment.",
    "deeper": [
        {"kind": "card", "title": "Medicines from living things",
         "body": ["The heart drug digitalis originates from foxgloves.",
                  "The painkiller aspirin originates from willow.",
                  "Species we lose could hold medicines we have not found yet."]},
        {"kind": "card", "title": "Where this goes next",
         "body": ["Waste management, Land use, Deforestation and Global warming each show one way "
                  "humans reduce biodiversity.",
                  "Maintaining biodiversity shows the programmes that try to stop it."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Define</strong>: give the meaning, in AQA's words.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Define", "marks": 1, "prompt": "Define biodiversity.",
             "why": "Biodiversity is the variety of all the different species of organisms on Earth, "
                    "or within an ecosystem.",
             "options": [
                 {"text": "The number of individual animals in an ecosystem", "correct": False,
                  "reply": "Biodiversity is about how many different species there are, of every kind."},
                 {"text": "The variety of all the different species in an ecosystem", "correct": True},
                 {"text": "The total mass of all the living things in an ecosystem", "correct": False,
                  "reply": "That is biomass. Biodiversity is the variety of species."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State how a great biodiversity affects the stability of an ecosystem.",
             "why": "A great biodiversity ensures the stability of ecosystems.",
             "options": [
                 {"text": "It makes the ecosystem less stable", "correct": False,
                  "reply": "More species means each one depends less on any other, so it is more stable."},
                 {"text": "It has no effect on stability", "correct": False,
                  "reply": "A great biodiversity ensures the stability of ecosystems."},
                 {"text": "It makes the ecosystem more stable", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why an ecosystem with a great biodiversity is more stable.",
             "why": "It reduces the dependence of one species on another for food and shelter, so losing "
                    "one species does less harm.",
             "options": [
                 {"text": "Species depend more on one other species for food and shelter",
                  "correct": False, "reply": "This is the wrong way round."},
                 {"text": "Species depend less on any one other species for food and shelter",
                  "correct": True},
                 {"text": "Species stop competing with each other for food and shelter",
                  "correct": False,
                  "reply": "Species still compete. The point is that each one has other foods and shelter."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 2,
             "prompt": "Give two human activities that reduce biodiversity.",
             "why": "Pollution kills plants and animals, and deforestation destroys habitats.",
             "options": [
                 {"text": "Polluting rivers and cutting down forests", "correct": True},
                 {"text": "Recycling waste and planting hedgerows", "correct": False,
                  "reply": "Both of these help to maintain biodiversity."},
                 {"text": "Breeding rare species and protecting habitats", "correct": False,
                  "reply": "Both of these are programmes that protect biodiversity."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A wood has many species. A field has very few. Explain why the wood is the more "
                       "stable ecosystem. Put the links in order.",
             "links": ["In the wood, most animals have several different foods.",
                       "If one food species dies out, the animals that ate it can eat something else.",
                       "So their populations do not fall sharply, and the wood stays stable."],
             "herrings": [{"text": "In the wood, every animal depends on just one food species.",
                           "why": "A great biodiversity reduces the dependence of one species on another."},
                          {"text": "More species means the wood has less food in it.",
                           "why": "More species means more different foods to choose from."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how cutting down a forest reduces biodiversity. Put the links in order.",
             "links": ["The trees are cut down.",
                       "The habitat of many species is destroyed, so they lose their food and shelter.",
                       "Fewer different species can live there, so biodiversity falls."],
             "herrings": [{"text": "The trees grow back straight away.",
                           "why": "Clearing removes the habitat; it does not return quickly."},
                          {"text": "Biodiversity is not affected because the soil is still there.",
                           "why": "Biodiversity is the variety of species, and many species have lost their habitat."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Explain why a great biodiversity is important for ecosystems and for humans.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Explains how a great biodiversity keeps an "
                  "ecosystem stable, and gives a reason it matters to humans.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Defines biodiversity or gives one relevant point.",
                  "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Biodiversity is the variety of all the different species of organisms in an "
                        "ecosystem.",
                        "A great biodiversity ensures the stability of the ecosystem.",
                        "It reduces the dependence of one species on another for food, shelter and the "
                        "maintenance of the physical environment.",
                        "If one species is lost, others have other food and shelter to use.",
                        "The future of the human species relies on maintaining a good level of "
                        "biodiversity, for example for food."],
             "reject": ["“Biodiversity is the number of animals in an area.”",
                        "“More species means each species depends more on the others.”"]},
        ],
    },
}
