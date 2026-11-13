# -*- coding: utf-8 -*-
"""Calculating energy transferred, in the lean shape. Spec table: docs/lessons/wave1/ks3-calculating-energy-transferred.md."""

LESSON = {
    "slug": "calculating-energy-transferred",
    "start": {
        "setup": "A 9000 W shower runs for 8 minutes. A 50 W lamp is left on for 24 hours.",
        "question": "If you had to guess, how does the shower's energy compare with the lamp's?",
        "options": [
            ("The shower uses far more", "About the same. The shower has far more power, but the lamp is on far longer."),
            ("They are about the same", "About the same. The shower has far more power, but the lamp is on far longer."),
        ],
        "answer": 1,
    },
    "words": ["joule", "kilojoule", "kilowatt-hour", "convert"],
    "word_defs": {
        "joule": "The unit of energy. Its symbol is J.",
        "kilojoule": "1000 joules. Its symbol is kJ.",
        "kilowatt-hour": "The energy a 1 kW appliance transfers in 1 hour. It is 3 600 000 J.",
        "convert": "To change a quantity into different units, such as minutes into seconds.",
    },
    "knowledge": [
        {"kind": "card", "title": "The energy equation",
         "body": ["energy transferred = power × time",
                  {"figure": "p2-energy-triangle"},
                  "Use power in watts and time in seconds. This gives energy in joules.",
                  "Or use power in kilowatts and time in hours. This gives kilowatt-hours.",
                  "Never put minutes straight into the equation."]},
        {"kind": "card", "title": "Converting time",
         "body": [{"points": ["1 minute = 60 seconds",
                              "1 hour = 60 minutes = 3600 seconds",
                              "30 minutes = 0.5 hours",
                              "45 minutes = 0.75 hours"]},
                  "Convert the time before you put it into the equation."]},
        {"kind": "card", "title": "Worked example: watts and seconds",
         "body": ["A 1500 W hairdryer runs for 4 minutes. Find the energy it transfers.",
                  {"points": ["Convert: 4 minutes × 60 = 240 s",
                              "Formula: energy = power × time",
                              "Insert: energy = 1500 W × 240 s",
                              "Fine-tune: 1500 × 240 = 360 000",
                              "Answer: 360 000 J, which is 360 kJ"]}]},
        {"kind": "card", "title": "Worked example: kilowatts and hours",
         "body": ["A 3 kW heater runs for 30 minutes. Find the energy it transfers.",
                  {"points": ["Convert: 30 minutes = 0.5 h",
                              "Formula: energy = power × time",
                              "Insert: energy = 3 kW × 0.5 h",
                              "Fine-tune: 3 × 0.5 = 1.5",
                              "Answer: 1.5 kWh"]}]},
        {"kind": "reveal", "title": "Power, time and energy",
         "cols": ["Working", "Energy"],
         "rows": [
             ("Kettle: 2 kW for 6 minutes", "2 kW × 0.1 h", "0.2 kWh"),
             ("TV: 100 W for 4 hours", "0.1 kW × 4 h", "0.4 kWh"),
             ("LED lamp: 10 W for 5 hours", "0.01 kW × 5 h", "0.05 kWh"),
         ]},
        {"kind": "card", "title": "Time matters as much as power",
         "body": ["The TV has far less power than the kettle.",
                  "But it is on for much longer, so it transfers more energy.",
                  "You cannot judge energy from the power rating alone."]},
        {"kind": "card", "title": "Check the answer is a sensible size",
         "body": ["A joule is a small amount of energy.",
                  "Boiling a full kettle takes hundreds of thousands of joules.",
                  "If your answer for a kettle is only a few thousand joules, check the time."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("2000 W for 3 minutes is 2000 × 3 = 6000 J.",
              "Convert first. 3 minutes is 180 s, so it is 360 000 J."),
             ("A kilowatt-hour is a unit of power.",
              "It is a unit of energy: 1 kW for 1 hour."),
             ("A few thousand joules will boil a kettle.",
              "Boiling a kettle takes hundreds of thousands of joules."),
         ]}]},
    ],
    "key_fact": "Energy transferred = power × time. Use watts with seconds to get joules. Use kilowatts "
                "with hours to get kilowatt-hours. Always convert the time first.",
    "deeper": [
        {"kind": "card", "title": "A spacecraft lost to units",
         "body": ["In 1999, NASA lost a spacecraft called the Mars Climate Orbiter.",
                  "One team worked in US units. Another team expected metric units.",
                  "Nobody converted, so the spacecraft flew too close to Mars and was lost."]},
        {"kind": "card", "title": "Joules and kilowatt-hours",
         "body": ["1 kWh = 1000 W × 3600 s = 3 600 000 J.",
                  "Bills use kilowatt-hours. In joules, the numbers would be huge."]},
    ],
    "try": None,
    "ladder_stem": {
        "explain": "An 8500 W shower runs for 10 minutes. A 60 W lamp is on for 24 hours. Show that "
                   "they transfer almost the same energy. Explain what this tells you about judging "
                   "appliances by their power rating.",
        "produce": "A family wants to cut its electricity bill. A 2200 W oven is used for 45 minutes a "
                   "day. A 90 W fridge motor runs for about 12 hours a day. Eight 9 W LED lamps are on "
                   "for about 5 hours a day. Work out which uses the most energy per day. Then advise the "
                   "family, using numbers.",
    },
    "ladder_ticks": [
        ["Calculates the oven at about 1.65 kWh per day.",
         "Calculates the oven at about 1.65 kWh, or 5 940 000 J, per day."],
        ["Calculates the fridge at about 1.08 kWh per day.",
         "Calculates the fridge at about 1.08 kWh, or 3 888 000 J, per day."],
        ["Calculates the lamps at about 0.36 kWh per day in total.",
         "Calculates all eight lamps at about 0.36 kWh, or 1 296 000 J, per day."],
        ["Converts 24 hours to 86 400 s and calculates 5 184 000 J for the lamp.",
         "Converts 24 h to 86 400 s, giving 5 184 000 J for the lamp."],
        ["Says the rating alone cannot tell you the energy, because the times differ by a factor of 144.",
         "Says the rating alone cannot give the energy, because the times are so different."],
        ["Draws the conclusion that a low-power appliance left on for a long time can cost as much as a "
         "high-power one used briefly.",
         "Says low power for a long time can cost as much as high power briefly."],
        ["Ranks the oven first and the fridge second, and notes that the fridge comes that close on the "
         "second-lowest rating of the three — it is the hours that do it.",
         "Ranks the oven first and the fridge second. Says the fridge's long hours put it second."],
        ["Gives advice that follows from the numbers — and notes that the fridge cannot simply be switched off, "
         "so the realistic saving is elsewhere.",
         "Gives advice from the numbers. Notes the fridge cannot simply be switched off."],
    ],
    "figures": [
        {"id": "p2-energy-triangle", "kind": "diagram", "status": "drawn", "art": "formula-triangle",
         "title": "The formula triangle for energy transferred",
         "desc": "A triangle split by a horizontal line. Energy, E, in J, sits in the top part. Power, "
                 "P, in W, and time, t, in s, sit side by side in the bottom part, with a "
                 "multiplication sign between them.",
         "caption": "Cover the one you want. Side by side means multiply. One over the other means divide.",
         "data": {"top": {"s": "E", "name": "energy", "unit": "J"},
                  "bottom": [{"s": "P", "name": "power", "unit": "W"},
                             {"s": "t", "name": "time", "unit": "s"}]}},
    ],
    "ladder_feedback": {
        "recall": {
            1: "That is 1200 + 90. Multiply the power by the time.",
            2: "That is 1200 ÷ 90. Energy = power × time, so multiply.",
            3: "That uses 1.5 minutes. Watts need the time in seconds, so use 90.",
        },
        "apply": {
            0: "6000 J is far too small to boil a kettle. 3 minutes is 180 s.",
            2: "Kilowatts would need the time in hours. The real mistake is the minutes.",
            3: "Multiplying is right, as energy = power × time. The time unit is wrong.",
        },
    },
}
