# -*- coding: utf-8 -*-
"""Energy in food and what you need, in the lean shape.
Spec table: docs/lessons/wave2/ks3-energy-in-food-and-what-you-need.md.

A different lesson from the P2 record `energy-in-food` (labels, kJ and kcal, energy per gram,
calorimeter errors). This one teaches the biology side: what the body uses the energy for, how
much different people need, and comparing foods with fuels (Rainford 14b, 15c).
"""

LESSON = {
    "slug": "energy-in-food-and-what-you-need",
    "start": {
        "setup": "A 68-year-old and a 25-year-old eat the same meals. Each takes in about 11 000 kJ "
                 "a day. After a month, one has gained mass and one has lost it.",
        "question": "If you had to guess, what explains the different outcome?",
        "options": [
            ("How much energy each body needs",
             "Yes. The same food was more than one body needed, and less than the other needed."),
            ("How well each body digests food",
             "Digestion varies only a little. The difference is how much energy each body needs."),
        ],
        "answer": 0,
    },
    "words": ["kilojoule", "energy requirement", "fuel", "respiration"],
    "word_defs": {
        "kilojoule": "A unit of energy. 1 kilojoule (kJ) is 1000 joules.",
        "energy requirement": "How much energy a person needs to take in each day.",
        "fuel": "A substance that is burned to release energy, such as wood, coal or petrol.",
        "respiration": "The reaction in every cell that releases energy from food.",
    },
    "knowledge": [
        {"kind": "card", "title": "Food stores energy",
         "body": ["Food is a store of chemical energy.",
                  "Your cells release this energy by respiration.",
                  "Energy in food is measured in kilojoules, kJ. 1 kJ is 1000 joules.",
                  "Food labels give the energy in kJ."]},
        {"kind": "card", "title": "What the energy is used for",
         "body": [{"points": ["Moving: your muscles contract to move you.",
                              "Keeping warm: your body stays at about 37 °C.",
                              "Growing and repairing: making new cells.",
                              "Staying alive: your heart, breathing and brain work all the time."]},
                  "You need energy even when you are asleep.",
                  "The energy is not destroyed. It is transferred.",
                  "Most of it ends up warming you and your surroundings."]},
        {"kind": "card", "title": "Comparing foods",
         "body": ["Some foods hold much more energy than others. One portion of each:",
                  {"points": ["a glass of water: 0 kJ",
                              "an apple: about 320 kJ",
                              "a banana: about 450 kJ",
                              "a chocolate bar: about 1050 kJ",
                              "a plate of pasta and sauce: about 2400 kJ"]},
                  "To compare foods fairly, use the energy in 100 g on each label."]},
        {"kind": "reveal", "title": "Energy in foods and fuels",
         "cols": ["Energy in 1 g", "How the energy is released"],
         "rows": [
             ("Fat", "About 37 kJ", "Respiration in your cells"),
             ("Carbohydrate", "About 17 kJ", "Respiration in your cells"),
             ("Protein", "About 17 kJ", "Respiration in your cells"),
             ("Wood", "About 16 kJ", "Burning"),
             ("Coal", "About 30 kJ", "Burning"),
             ("Petrol", "About 46 kJ", "Burning"),
             ("Natural gas", "About 55 kJ", "Burning"),
         ]},
        {"kind": "card", "title": "Food and fuel",
         "body": ["Foods and fuels are both stores of chemical energy.",
                  "Fat holds more energy per gram than wood, and less than petrol.",
                  "A fuel burns fast, giving out heat and light.",
                  "Your cells release energy from food slowly, in many small steps."]},
        {"kind": "card", "title": "Burning food to compare it",
         "body": [{"figure": "b3-burning-food"},
                  {"points": ["Put 20 cm³ of water in a boiling tube. Measure its temperature.",
                              "Set a small piece of food alight on a mounted needle.",
                              "Hold it under the tube until it stops burning.",
                              "Measure the highest temperature. Work out the rise."]},
                  "The bigger the temperature rise, the more energy the food released.",
                  "For a fair test, use the same mass of each food.",
                  "Use the same volume of water each time.",
                  "The result is lower than the label. Some energy heats the air and the tube."]},
        {"kind": "card", "title": "How much energy people need",
         "body": [{"figure": "b3-energy-needs"}]},
        {"kind": "reveal", "title": "What changes how much you need",
         "cols": ["Who needs more", "Why"],
         "rows": [
             ("Age", "A 13-year-old needs more than a 4-year-old.",
              "A bigger body needs more energy to keep it warm and working."),
             ("Activity", "A bricklayer needs more than an office worker.",
              "Working muscles need energy, for hours each day."),
             ("Body size", "A large adult needs more than a small adult.",
              "There are more cells to keep warm and working."),
             ("Sex", "On average, men need more than women.",
              "On average, men are bigger and have more muscle."),
             ("Pregnancy", "A woman in the last three months of pregnancy.",
              "She needs about 800 kJ more a day to grow the baby."),
         ]},
        {"kind": "card", "title": "Worked example: one day's food against the need",
         "body": ["A 13-year-old needs 9500 kJ a day. Find out if this day's food meets that need.",
                  {"figure": "b3-day-intake"},
                  "Step 1: add up what was eaten.",
                  {"points": ["Convert: every value is already in kJ.",
                              "Formula: total = the energy of every portion added together",
                              "Insert: 4 × 780 = 3120. Then 3120 + 2400 + 450 + 1050.",
                              "Fine-tune: 3120 + 2400 + 450 + 1050 = 7020",
                              "Answer: 7020 kJ was eaten."]},
                  "Step 2: compare it with the need.",
                  {"points": ["Formula: shortfall = need − total eaten",
                              "Insert: 9500 − 7020",
                              "Fine-tune: 9500 − 7020 = 2480",
                              "Answer: 2480 kJ short of the need."]}]},
        {"kind": "card", "title": "Worked example: a share of the day",
         "body": ["A chocolate bar holds 1050 kJ. Find its share of a 13-year-old's 9500 kJ day.",
                  {"points": ["Convert: both values are in kJ.",
                              "Formula: share (%) = energy in the food ÷ daily need × 100",
                              "Insert: 1050 ÷ 9500 × 100",
                              "Fine-tune: 1050 ÷ 9500 = 0.1105. Then 0.1105 × 100 = 11.05",
                              "Answer: about 11% of the day"]},
                  "Someone who needs less energy gets a bigger share from the same bar."]},
        {"kind": "card", "title": "Too much or too little",
         "body": ["Take in more energy than you need, day after day.",
                  "The extra is stored as fat.",
                  "Your mass goes up.",
                  "Take in less than you need, and your body uses up its stores.",
                  "Your mass goes down."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The energy in food gets used up and disappears.",
              "It is transferred. Most ends up warming you and your surroundings.", "DIET-06"),
             ("Everyone needs about the same energy each day.",
              "A 4-year-old needs about 5800 kJ a day. A rower in training needs about 25 000 kJ.",
              "DIET-07"),
             ("A percentage on a food label is right for everyone.",
              "It is a share of an adult's 8400 kJ. A 4-year-old's share is bigger."),
         ]}]},
    ],
    "key_fact": "Food is a store of chemical energy, measured in kilojoules. The body uses it to move, "
                "keep warm, grow and repair, and stay alive. Each person's need depends on their age, "
                "size, sex and activity.",
    "deeper": [
        {"kind": "card", "title": "Working out the energy",
         "body": ["You can work out the energy that heated the water in the burning food test.",
                  "20 cm³ of water warms by 25 °C. 1 g of water needs 4.2 J to warm by 1 °C.",
                  {"points": ["Convert: 20 cm³ of water has a mass of 20 g.",
                              "Formula: energy (J) = mass of water (g) × 4.2 × temperature rise (°C)",
                              "Insert: 20 × 4.2 × 25",
                              "Fine-tune: 20 × 4.2 = 84. Then 84 × 25 = 2100",
                              "Answer: 2100 J, which is 2.1 kJ"]}]},
        {"kind": "card", "title": "How labels were first worked out",
         "body": ["Scientists burned food in pure oxygen, in a sealed steel container.",
                  "The container sat in water. The water's temperature rise gave the energy.",
                  "This apparatus is called a bomb calorimeter.",
                  "Label values allow for parts of food the body cannot digest, such as most fibre."]},
    ],
    "try": None,
    "tutor_body": "Want to check an energy calculation of your own?",
    "safety_note": "Burning food is a teacher demonstration or a closely supervised practical. Wear eye "
                   "protection. Never use nuts or any food someone is allergic to. The boiling tube gets "
                   "very hot. Never eat anything in the lab.",
    "ks4_becomes": "Respiration and metabolism, and how exercise changes the energy a body needs.",
    "figure_caption": {"b3-burning-food": None, "b3-day-intake": None},
    "figures": [
        {"id": "b3-burning-food", "kind": "diagram", "status": "drawn", "art": "b3-burning-food",
         "title": "Burning food under a boiling tube of water",
         "desc": "A boiling tube is held in a clamp on a clamp stand, standing on a heatproof mat. The "
                 "tube holds 20 cm³ of water, with a thermometer in it. A piece of food on the end of a "
                 "mounted needle burns under the tube, and its flame touches the bottom of the tube. "
                 "Labels: thermometer, boiling tube, 20 cm³ of water, burning food, mounted needle, "
                 "clamp stand, heatproof mat.",
         "caption": "The burning food heats the water. A bigger temperature rise means more energy.",
         "data": {"water": "20 cm³ of water"}},
        {"id": "b3-energy-needs", "kind": "diagram", "status": "drawn", "art": "b3-energy-needs",
         "title": "How much energy five people need in a day",
         "desc": "A bar chart with one bar for each person, drawn to one scale. A 4-year-old: about "
                 "5800 kJ. A 13-year-old: about 9500 kJ. An adult with a desk job: about 9000 kJ. A "
                 "bricklayer: about 13 500 kJ. A rower in training: about 25 000 kJ, the longest bar.",
         "caption": "Daily energy needs, rounded. The rower needs over four times as much as the 4-year-old.",
         "data": {"unit": "kJ",
                  "people": [{"label": "A 4-year-old", "kj": 5800},
                             {"label": "A 13-year-old", "kj": 9500},
                             {"label": "An adult with a desk job", "kj": 9000},
                             {"label": "A bricklayer", "kj": 13500},
                             {"label": "A rower in training", "kj": 25000}]}},
        {"id": "b3-day-intake", "kind": "diagram", "status": "drawn", "art": "b3-day-intake",
         "title": "One day's food against a 13-year-old's need",
         "desc": "Two bars drawn to one scale. The top bar, Eaten: 7020 kJ, is made of four blocks: "
                 "4 slices of toast and butter, 3120 kJ; a plate of pasta, 2400 kJ; a banana, 450 kJ; "
                 "a chocolate bar, 1050 kJ. A dashed outline continues the bar to the length of the "
                 "need, marked 2480 kJ short. The bottom bar, Needed: 9500 kJ. A key under the bars "
                 "lists the four foods and their energy.",
         "caption": "The day's food falls 2480 kJ short of the 9500 kJ needed.",
         "data": {"unit": "kJ", "need": 9500,
                  "foods": [{"label": "4 slices of toast and butter", "kj": 3120},
                            {"label": "A plate of pasta and sauce", "kj": 2400},
                            {"label": "A banana", "kj": 450},
                            {"label": "A chocolate bar", "kj": 1050}]}},
    ],
    "ladder_stem": {
        "explain": "An office worker and a bricklayer are the same age and size. The bricklayer needs "
                   "4500 kJ more each day. Explain what that extra energy is for, and where it ends up. "
                   "Explain why a 4-year-old needs less than either, even though they grow fast.",
        "produce": "A school plans one lunch, the same portion for every pupil aged 11 to 16. Say what "
                   "is wrong with the plan. Say what you would do instead. Name one thing you would "
                   "need to find out first.",
    },
    "ladder_ticks": [
        ["Attributes the 4500 kJ difference to activity — muscles contracting for hours require "
         "energy transfer.",
         "Says the extra 4500 kJ is for activity: muscles working for hours."],
        ["Explains the 4-year-old’s lower total by their much smaller body: less tissue to keep "
         "warm and to maintain.",
         "Says the 4-year-old's body is much smaller, with fewer cells to keep warm."],
        ["Notes that growth does claim a share of a child’s requirement, and that it is still "
         "smaller in total than an adult’s maintenance.",
         "Says growth uses some of a child's energy, but their total is still smaller."],
        ["Avoids saying anyone ‘uses up’ energy — uses transferred, or stored, instead.",
         "Says the energy is transferred, mostly warming the surroundings. Never says ‘used up’."],
        ["Names at least two things the requirement depends on — age, size, sex, growth, activity.",
         "Names two things a person's need depends on, such as age, size or activity."],
        ["Names a real thing to find out — the age spread, activity levels, or how much pupils "
         "actually eat rather than are served.",
         "Names something to find out first, such as pupils' ages or how active they are."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "That total counts only one chocolate bar. The day had two.",
            1: "The total is right. But 7670 is less than 9500, so it is a shortfall.",
            3: "Nothing makes the intake match the need. Add up the food to find out.",
        },
        "apply": {
            1: "11% is the share for a 13-year-old. A 4-year-old needs less, so the share is bigger.",
            2: "The bar holds the same energy, whoever eats it. The need is what differs.",
            3: "You do not need the mass. Divide 1050 by 5800 and multiply by 100.",
        },
    },
}
