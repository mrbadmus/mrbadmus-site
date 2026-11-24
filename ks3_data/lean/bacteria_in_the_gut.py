# -*- coding: utf-8 -*-
"""Bacteria in the gut, in the lean shape. Spec table: docs/lessons/wave2/ks3-bacteria-in-the-gut.md.

Rainford 15b's fourth outcome ("explain the importance of bacteria in the digestive system") is
taught here, on its own page, not in the absorption lesson.
"""

LESSON = {
    "slug": "bacteria-in-the-gut",
    "start": {
        "setup": "A mouse is raised in a sealed bubble. It never has any bacteria in or on it.",
        "question": "If you had to guess, does a mouse with no bacteria need more food than a normal "
                    "mouse, or less?",
        "options": [
            ("More food",
             "Yes, about 30% more. Gut bacteria release energy from fibre the mouse cannot digest."),
            ("Less food",
             "It needs about 30% more. Without gut bacteria, the energy in fibre is lost."),
        ],
        "answer": 0,
    },
    "words": ["gut bacteria", "fibre", "vitamin K", "antibiotic"],
    "word_defs": {
        "gut bacteria": "The trillions of bacteria that live in your gut, mostly in the large intestine.",
        "fibre": "Plant material, such as cellulose, that your own enzymes cannot digest.",
        "vitamin K": "A vitamin your blood needs to clot. Gut bacteria make some of it.",
        "antibiotic": "A medicine that kills bacteria, helpful ones as well as harmful ones.",
    },
    "knowledge": [
        {"kind": "card", "title": "Bacteria in your gut",
         "body": ["Trillions of bacteria live in your gut. Most live in the large intestine.",
                  "Few live in the stomach. Its acid kills most bacteria that you swallow.",
                  "Most gut bacteria are harmless or helpful. A few kinds can cause disease."]},
        {"kind": "reveal", "title": "What gut bacteria do for you",
         "cols": ["What they do", "Without them"],
         "rows": [
             ("Fibre", "Break down fibre that your own enzymes cannot. This releases substances your "
                       "body uses for energy.",
              "The energy in fibre is lost in the faeces."),
             ("Vitamins", "Make vitamin K and some B vitamins, which you absorb.",
              "Less vitamin K, so blood may not clot properly."),
             ("Space", "Take up the space and food in the gut.",
              "Harmful bacteria can settle and grow more easily."),
             ("Immune system", "Help the immune system learn what to attack and what to leave alone.",
              "The body fights infections less well."),
         ]},
        {"kind": "card", "title": "Good for both sides",
         "body": ["The bacteria get a warm place to live, at about 37 °C.",
                  "They get a steady supply of food from what you eat.",
                  "You get the jobs they do. Both sides gain."]},
        {"kind": "card", "title": "Small, but not simple",
         "body": ["A bacterium is a single cell.",
                  "But bacteria can make enzymes that your own cells cannot make.",
                  "That is how gut bacteria can break down fibre that you cannot digest."]},
        {"kind": "card", "title": "Antibiotics and gut bacteria",
         "body": ["Antibiotics are medicines that kill bacteria.",
                  "They kill helpful gut bacteria as well as harmful ones.",
                  "This leaves space and food in the gut.",
                  "A harmful bacterium, such as C. difficile, can then grow fast.",
                  "It can cause severe diarrhoea."]},
        {"kind": "card", "title": "Same bacterium, different place",
         "body": ["Most kinds of E. coli live harmlessly in the large intestine.",
                  "If E. coli gets into the bladder or the blood, it can make you ill.",
                  "So whether a bacterium harms you can depend on where it is."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Bacteria are germs. Having bacteria inside you means you are ill.",
              "Everyone has trillions of gut bacteria. Most of them are helpful.", "DIET-17"),
             ("A bacterium is just a simpler version of one of our cells.",
              "Bacteria can do things our cells cannot, such as break down fibre.", "CELL-08"),
             ("Antibiotics only kill harmful bacteria.",
              "Antibiotics kill helpful gut bacteria too."),
             ("Most gut bacteria live in the stomach.",
              "Most live in the large intestine. Stomach acid kills most bacteria."),
         ]}]},
    ],
    "key_fact": "Most gut bacteria are harmless or helpful. Some break down fibre we cannot digest. "
                "Some make vitamins, and they crowd out harmful bacteria.",
    "deeper": [
        {"kind": "card", "title": "The germ-free mouse",
         "body": ["Scientists can raise mice with no bacteria at all.",
                  "These mice need about 30% more food than normal mice.",
                  "Their gut wall is thinner, and they catch infections more easily."]},
        {"kind": "card", "title": "Vitamin K for newborn babies",
         "body": ["Newborn babies have very little vitamin K.",
                  "Little of it crosses from the mother before birth.",
                  "Their gut has almost no bacteria yet to make it.",
                  "In the UK, babies are offered vitamin K soon after birth."]},
    ],
    "try": None,
    "tutor_body": "Want to talk through why the same bacterium can be helpful or harmful?",
    "ks4_becomes": "Communicable disease, and how bacteria become resistant to antibiotics.",
    "ladder_stem": {
        "explain": "A germ-free mouse needs about 30% more food than a normal mouse. It also catches "
                   "infections more easily. Explain both, using at least three things gut bacteria do.",
        "produce": "Cows digest grass, which is mostly cellulose. Cows make no enzyme that breaks down "
                   "cellulose. Explain how a cow can digest grass. Suggest how a cow's gut compares "
                   "in size with ours.",
    },
    "ladder_ticks": [
        ["Says fibre is not fermented, so the energy in it is lost rather than absorbed.",
         "Says no bacteria break down the fibre, so the energy in it is lost."],
        ["Says vitamins normally made by bacteria are absent and must come from food or be missing.",
         "Says vitamins made by bacteria are missing, so they must come from food."],
        ["Says nothing is occupying the gut, so an arriving harmful species meets no competition.",
         "Says harmful bacteria meet no competition, as nothing else lives in the gut."],
        ["Ends on the general point: the bacteria were doing jobs, not being tolerated.",
         "Concludes that gut bacteria do useful jobs for the body."],
        ["Says the cow relies on bacteria — and other microorganisms — to break down cellulose, not "
         "on its own enzymes.",
         "Says microorganisms in the cow's gut break down the cellulose for it."],
        ["Says the products of that fermentation are then absorbed by the cow.",
         "Says the cow then absorbs the products."],
        ["Concludes the cow needs a much larger fermentation chamber than a human has — hence the "
         "multi-chambered stomach.",
         "Concludes the cow needs a much bigger gut, like its four-part stomach."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Your own villus cells absorb glucose. Bacteria are not needed for that.",
            1: "Your stomach lining makes the acid. The acid kills most bacteria that arrive.",
            2: "Your own protease enzymes digest protein. Bacteria are not needed for that.",
        },
        "apply": {
            0: "The antibiotic did not change C. difficile. It removed its competitors.",
            2: "This diarrhoea was caused by C. difficile, a bacterium that grew in the gut.",
            3: "Chest bacteria did not cause it. C. difficile grew because its competitors were gone.",
        },
    },
}
