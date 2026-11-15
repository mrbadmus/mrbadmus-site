# -*- coding: utf-8 -*-
"""Factors affecting food security, in the lean shape. Spec table:
ks4-factors-affecting-food-security.md. Old-format lesson (no Design page): full record with
rungs; the practice set is quiz-factors-affecting-food-security.json.
"""

LESSON = {
    "slug": "factors-affecting-food-security",
    "start": {
        "setup": "One year the rains fail in a farming region.",
        "question": "If you had to guess, who goes short of food: only the farmers, or the "
                    "whole population?",
        "options": [
            ("Only the farmers",
             "The whole population. The crops fail, so there is less food for everyone, and "
             "there can be widespread famine."),
            ("The whole population",
             "The whole population. The crops fail, so there is less food for everyone, and "
             "there can be widespread famine."),
        ],
        "answer": 1,
    },
    "words": ["food security", "birth rate", "pathogen", "sustainable"],
    "knowledge": [
        {"kind": "card", "title": "What food security means",
         "body": ["Food security is having enough food to feed a population.",
                  "Sustainable methods must be found to feed all people on Earth."]},
        {"kind": "card", "title": "Biological factors that threaten food security",
         "body": [{"points": [
             "The increasing birth rate has threatened food security in some countries.",
             "Changing diets in developed countries mean scarce food resources are transported "
             "around the world.",
             "New pests and pathogens affect farming.",
             "Environmental changes affect food production. For example, there can be "
             "widespread famine in some countries if the rains fail.",
             "The cost of agricultural inputs, such as seed, fertiliser and animal feed.",
             "Conflicts in some parts of the world affect the availability of water or food.",
         ]}]},
        {"kind": "reveal", "title": "How each one cuts the food people have",
         "cols": ["What happens"],
         "rows": [("Increasing birth rate",
                   "More people share the same food."),
                  ("Changing diets in developed countries",
                   "Scarce food resources are transported around the world to meet these diets, "
                   "so less is left for the people where it was grown."),
                  ("New pests and pathogens",
                   "Crops and farm animals are damaged or die, so less food is produced."),
                  ("Rains fail",
                   "Crops fail, so there can be widespread famine."),
                  ("Cost of agricultural inputs",
                   "Farmers cannot afford what they need, so they grow less food."),
                  ("Conflict",
                   "People cannot get the water or food they need.")]},
        {"kind": "card", "title": "Reading food data",
         "body": [{"points": [
             "Compare how fast the population grows with how fast food production grows.",
             "If the population grows faster than food production, each person has less food, "
             "so food security falls.",
             "Quote the numbers from the data in your answer.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Food security means food that is safe to eat.",
              "Food security is having enough food to feed a population."),
             ("A falling birth rate threatens food security.",
              "It is the increasing birth rate that threatens food security."),
             ("Changing diets in developed countries only affect those countries.",
              "Scarce food resources are transported around the world to meet them."),
         ]}]},
    ],
    "key_fact": "Food security is having enough food to feed a population. It is threatened by "
                "an increasing birth rate, changing diets in developed countries, new pests and "
                "pathogens, environmental changes such as failed rains, the cost of agricultural "
                "inputs, and conflict.",
    "deeper": [
        {"kind": "card", "title": "Where the solutions are",
         "body": ["The next lessons show some sustainable ways to produce more food:",
                  {"points": ["Farming techniques",
                              "Sustainable fisheries",
                              "The role of biotechnology"]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: name each factor and say what it does to the food "
             "supply.",
             "<strong>Explain</strong>: say how a factor leads to less food for each person.",
             "<strong>Evaluate</strong>: use the population and food data to judge how secure "
             "the food supply is.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Complete", "marks": 1,
             "prompt": "Food security is having…",
             "why": "Food security is having enough food to feed a population.",
             "options": [
                 {"text": "enough food to feed a population", "correct": True},
                 {"text": "food that is safe and clean to eat", "correct": False,
                  "reply": "Food security is about having enough food."},
                 {"text": "food grown without any pesticides", "correct": False,
                  "reply": "Food security is about having enough food, however it is grown."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Which of these threatens food security?",
             "why": "The increasing birth rate has threatened food security in some countries.",
             "options": [
                 {"text": "A falling birth rate", "correct": False,
                  "reply": "A falling birth rate means fewer people to feed."},
                 {"text": "An increasing birth rate", "correct": True},
                 {"text": "Rains that arrive as usual", "correct": False,
                  "reply": "Food production suffers when the rains fail."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Information (made up): a country's population rose from 20 million to 30 "
                       "million in 20 years. Its food production stayed the same. Explain what "
                       "happened to its food security.",
             "why": "The same amount of food had to feed 10 million more people, so each person "
                    "had less.",
             "options": [
                 {"text": "It fell, because the same food had to feed more people",
                  "correct": True},
                 {"text": "It rose, because more people could farm the land", "correct": False,
                  "reply": "Food production stayed the same, so each person had less."},
                 {"text": "It stayed the same, because food production did not change",
                  "correct": False,
                  "reply": "The same food now has to feed 10 million more people."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain how a conflict can threaten food security.",
             "why": "Conflicts affect the availability of water or food.",
             "options": [
                 {"text": "It makes crops grow more slowly in the soil", "correct": False,
                  "reply": "A conflict affects whether people can get food and water."},
                 {"text": "It raises the birth rate in that country", "correct": False,
                  "reply": "A conflict affects whether people can get food and water."},
                 {"text": "It stops people getting water or food",
                  "correct": True},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how a new pathogen can threaten food security. Put the links in "
                       "order.",
             "links": ["A new pathogen infects a crop that many people rely on.",
                       "Many of the plants are damaged or die, so the harvest is smaller.",
                       "Less food is produced, so there may not be enough to feed the "
                       "population."],
             "herrings": [{"text": "The pathogen makes the crop grow faster.",
                           "why": "A pathogen causes disease, so the crop grows less well."},
                          {"text": "Pathogens only affect animals, never crops.",
                           "why": "Pathogens infect plants as well as animals."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how the cost of agricultural inputs can threaten food security. "
                       "Put the links in order.",
             "links": ["The price of seed, fertiliser and animal feed rises.",
                       "Some farmers cannot afford to buy as much of them.",
                       "They grow less food, so there may not be enough to feed the "
                       "population."],
             "herrings": [{"text": "Farmers buy more fertiliser when it costs more.",
                           "why": "A higher price means farmers can afford less, not more."},
                          {"text": "Seed costs nothing, so its price cannot matter.",
                           "why": "Seed is an agricultural input that farmers have to buy."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 6,
             "prompt": "Describe some of the biological factors that threaten food security. "
                       "For each one, say how it reduces the food people have.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "Four or more factors, each linked "
                  "clearly to less food for people.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Two or three factors, with some links to "
                  "less food for people.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One factor, or a list of factors with no "
                  "links.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Food security is having enough food to feed a population.",
                        "An increasing birth rate means more people need feeding from the same "
                        "food.",
                        "Changing diets in developed countries mean scarce food resources are "
                        "transported around the world.",
                        "New pests and pathogens damage crops and farm animals, so less food is "
                        "produced.",
                        "Environmental changes affect food production: if the rains fail, crops "
                        "fail and there can be widespread famine.",
                        "The cost of agricultural inputs means some farmers cannot afford what "
                        "they need, so they grow less.",
                        "Conflicts affect the availability of water or food."],
             "reject": ["“Food security means food that is safe to eat.”",
                        "“A falling birth rate threatens food security.”"]},
        ],
    },
}
