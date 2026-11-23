# -*- coding: utf-8 -*-
"""When diet goes wrong, in the lean shape. Spec table: docs/lessons/wave2/ks3-when-diet-goes-wrong.md."""

LESSON = {
    "slug": "when-diet-goes-wrong",
    "start": {
        "setup": "A patient takes in 13 000 kJ a day. That is more energy than most adults need.",
        "question": "If you had to guess, could this patient be malnourished?",
        "options": [
            ("Yes, they could be",
             "Yes. Malnourished means the diet is out of balance. Too much energy counts."),
            ("No, not on that much",
             "They could be. Too much energy is malnutrition. A big diet can also lack iron."),
        ],
        "answer": 0,
    },
    "words": ["malnutrition", "deficiency disease", "obesity", "starvation"],
    "word_defs": {
        "malnutrition": "A diet that is not balanced: too much energy, too little, or a missing nutrient.",
        "deficiency disease": "An illness caused by too little of one nutrient in the diet.",
        "obesity": "Having so much stored body fat that it harms health.",
        "starvation": "Going without enough food for a long time, so the body breaks itself down.",
    },
    "knowledge": [
        {"kind": "card", "title": "What malnutrition means",
         "body": ["Malnutrition means a diet that is not balanced.",
                  "It can mean too much energy, too little energy, or a missing nutrient.",
                  "Someone who eats plenty can still be malnourished."]},
        {"kind": "reveal", "title": "Three kinds of imbalance",
         "cols": ["What is wrong", "What happens"],
         "rows": [
             ("Energy surplus", "More energy taken in than needed, for months or years.",
              "The extra is stored as fat. This can lead to obesity."),
             ("Energy shortfall", "Less energy taken in than needed, for weeks or months.",
              "The body breaks down its fat, then its muscle. This is starvation."),
             ("Missing nutrient", "Too little of one nutrient, such as a vitamin or iron.",
              "A deficiency disease. This can happen at any energy intake."),
         ]},
        {"kind": "card", "title": "Obesity",
         "body": ["Obesity comes from taking in more energy than you need, over a long time.",
                  "The extra energy is stored as fat under the skin and around organs.",
                  "Obesity raises the risk of type 2 diabetes, heart disease and high blood pressure.",
                  "It also puts strain on the joints, such as the knees.",
                  "A raised risk means these are more likely. They are not certain."]},
        {"kind": "card", "title": "Starvation",
         "body": ["In starvation, the body takes in far less energy than it needs.",
                  "It breaks down its fat stores first. Then it breaks down muscle.",
                  {"points": ["The person loses mass and feels weak and cold.",
                              "They catch infections more easily.",
                              "In children, growth slows or stops."]}]},
        {"kind": "reveal", "title": "Deficiency diseases",
         "cols": ["Missing nutrient", "Signs"],
         "rows": [
             ("Scurvy", "Vitamin C", "Bleeding gums. Bruises easily. Wounds heal slowly."),
             ("Rickets", "Vitamin D or calcium", "Soft, weak bones. The legs can bend."),
             ("Anaemia", "Iron", "Tiredness and pale skin. The blood carries less oxygen."),
             ("Kwashiorkor", "Mainly protein", "A swollen belly and legs. Poor growth."),
         ]},
        {"kind": "card", "title": "Curing a deficiency disease",
         "body": ["A deficiency disease is cured by the nutrient that is missing.",
                  "More of the same food does not help. It still lacks that nutrient.",
                  {"points": ["Vitamin C: oranges, other citrus fruit, peppers.",
                              "Vitamin D: oily fish, eggs, and sunlight on the skin.",
                              "Calcium: milk, cheese and yoghurt.",
                              "Iron: red meat, beans and leafy green vegetables.",
                              "Protein: meat, fish, eggs, beans and lentils."]}]},
        {"kind": "card", "title": "Reasons for malnutrition",
         "body": [{"points": ["Not enough food, because of poverty, war or crops failing.",
                              "Eating only a few kinds of food, so a nutrient is missing.",
                              "Taking in more energy than you need, with little exercise.",
                              "Some illnesses stop the gut absorbing food properly.",
                              "Some illnesses and medicines change how hungry you feel."]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Malnourished only means not having enough to eat.",
              "It means an unbalanced diet. Too much food can cause it too.", "DIET-08"),
             ("Deficiency diseases only happened in the past.",
              "Scurvy, rickets and anaemia still happen in the UK today.", "DIET-09"),
             ("You can tell what someone eats by looking at them.",
              "Body size also depends on genes, illness and activity. Blood tests can show deficiencies.",
              "DIET-10"),
             ("More of a food that lacks the nutrient cures a deficiency disease.",
              "Only the missing nutrient cures it, such as vitamin C for scurvy."),
             ("Only eating too much fat causes obesity.",
              "Extra energy from fat, carbohydrate or protein can be stored as fat."),
         ]}]},
    ],
    "key_fact": "Malnutrition means an unbalanced diet: too much energy, too little, or a missing "
                "nutrient. A deficiency disease, such as scurvy or rickets, is caused by one missing "
                "nutrient. It can happen at any energy intake.",
    "deeper": [
        {"kind": "card", "title": "James Lind and scurvy",
         "body": ["In 1747, James Lind treated twelve sailors who had scurvy.",
                  "He split them into pairs and gave each pair a different treatment.",
                  "The pair given oranges and lemons got better fastest.",
                  "It was one of the first controlled trials in medicine."]},
        {"kind": "card", "title": "Vitamin D and sunlight",
         "body": ["Your skin makes vitamin D in sunlight.",
                  "In the UK, from October to March, sunlight is too weak to make enough.",
                  "So the NHS advises a vitamin D supplement in autumn and winter."]},
    ],
    "try": None,
    "tutor_body": "Want to work through why a deficiency can happen on a full plate?",
    "safety_note": "This lesson describes these conditions as biology. It is not advice about your own "
                   "eating. If anything here worries you, talk to a trusted adult, your school nurse or "
                   "a doctor.",
    "ks4_becomes": "Risk factors for non-communicable diseases, such as diet, obesity and type 2 diabetes.",
    "ladder_stem": {
        "explain": "A region has a lot of anaemia. A charity sends large amounts of white rice. "
                   "Explain why this will reduce hunger but not the anaemia. Say what should be added.",
        "produce": "By law, UK white flour has calcium, iron and some B vitamins added. Explain what "
                   "problem this targets. Explain why adding them to flour reaches more people than "
                   "advice does. Give one limitation.",
    },
    "ladder_ticks": [
        ["Names something that would supply iron — pulses, leafy greens, meat, or fortified flour.",
         "Names a food that supplies iron, such as red meat, beans or leafy greens."],
        ["Explains that flour is eaten by almost everyone, so fortifying it reaches people who "
         "would never seek treatment.",
         "Says almost everyone eats flour, so it reaches people who would never seek help."],
        ["Notes that it requires no change in behaviour, which is why it works where advice does not.",
         "Says nobody has to change what they eat, so it works where advice fails."],
        ["Gives a real limitation — it misses people who avoid wheat, cannot be targeted to those "
         "who need it, and the dose cannot be adjusted per person.",
         "Gives a limitation, such as missing people who eat no wheat flour."],
    ],
    "ladder_feedback": {
        "recall": {
            1: "Their mass is steady on 12 000 kJ, so energy is not short.",
            2: "The missing nutrient is right. Steady mass shows there is no energy shortfall.",
            3: "Scurvy happens at any energy intake. It needs only a lack of vitamin C.",
        },
        "apply": {
            1: "No amount of food guarantees iron. Child B's diet can still lack it.",
            2: "The energy figures say nothing about how low each child's iron is.",
            3: "Anaemia here is caused by too little iron, not too little energy.",
        },
    },
}
