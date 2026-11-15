# -*- coding: utf-8 -*-
"""Decomposition, in the lean shape. New record, no legacy page.
Spec table: ks4-decomposition.md.

Routes: the page exists on CF, CH, TF and TH, but 8461 4.7.2.3 Decomposition is "(biology only)"
and 8464 has no decomposition section. So:
  every route   8464/8461 4.7.2.2, the role of microorganisms in cycling materials (cards 1-4,
                Easy mistakes, Key fact, every rung);
  TF and TH     8461 4.7.2.3 (rate of decay, compost, biogas, Required practical activity 10,
                rate calculations) and 8461 4.7.4.1 (how decomposers feed), behind
                "routes": ["TF", "TH"].
The rungs are the same on every route, so they test 4.7.2.2 only."""

TRIPLE = ["TF", "TH"]

LESSON = {
    "slug": "decomposition",
    "start": {
        "setup": "A wood drops a thick layer of dead leaves every autumn, year after year.",
        "question": "If you had to guess, why is the wood not buried under hundreds of years of "
                    "old leaves?",
        "options": [
            ("Microorganisms break the leaves down",
             "Microorganisms break them down. Bacteria and fungi decay the dead leaves and return "
             "what was in them to the air and the soil."),
            ("The wind blows the leaves away",
             "Microorganisms break them down. Bacteria and fungi decay the dead leaves and return "
             "what was in them to the air and the soil."),
        ],
        "answer": 0,
    },
    "words": ["decay", "decomposer", "microorganism", "mineral ions"],
    "knowledge": [
        {"kind": "card", "title": "What decay is",
         "body": ["Decay is the breakdown of dead plants, dead animals and animal waste by "
                  "microorganisms.",
                  "The main microorganisms that cause decay are bacteria and fungi. They are "
                  "called decomposers."]},
        {"kind": "card", "title": "Returning carbon",
         "body": ["As the microorganisms feed on dead material, they respire.",
                  "Their respiration returns the carbon to the atmosphere as carbon dioxide.",
                  "Plants then take in the carbon dioxide for photosynthesis."]},
        {"kind": "card", "title": "Returning mineral ions",
         "body": ["Dead plants and animals contain mineral ions.",
                  "Decay returns these mineral ions to the soil.",
                  "Plants take up the mineral ions through their roots and use them to grow."]},
        {"kind": "card", "title": "Why decay matters",
         "body": ["All materials in the living world are recycled to provide the building blocks "
                  "for future organisms.",
                  "Without microorganisms, the carbon and mineral ions would stay locked in dead "
                  "organisms. Plants would run short of them."]},
        {"kind": "card", "title": "How decomposers feed", "routes": TRIPLE,
         "body": ["Decomposers break down dead plant and animal matter by secreting enzymes into "
                  "the environment.",
                  "Small soluble food molecules then diffuse into the microorganism.",
                  {"slot": "fig:decomposer-feeding"}]},
        {"kind": "reveal", "title": "What affects the rate of decay", "routes": TRIPLE,
         "cols": ["Effect on the rate of decay"],
         "rows": [("Temperature", "Warmer conditions speed up decay, up to an optimum. The "
                                  "enzymes in the microorganisms work faster. If it gets too "
                                  "hot, the enzymes denature and decay slows. Cold slows "
                                  "decay."),
                  ("Water", "Moist conditions speed up decay. Microorganisms need water to "
                            "grow. Dry conditions slow decay."),
                  ("Availability of oxygen", "More oxygen speeds up decay. Most decomposers "
                                             "need oxygen for aerobic respiration.")]},
        {"kind": "card", "title": "Compost", "routes": TRIPLE,
         "body": ["Gardeners and farmers try to provide optimum conditions for rapid decay of "
                  "waste biological material.",
                  "A compost heap is kept warm and moist, and is turned to let oxygen in.",
                  "The compost produced is used as a natural fertiliser for growing garden "
                  "plants or crops."]},
        {"kind": "card", "title": "Anaerobic decay and biogas", "routes": TRIPLE,
         "body": ["Decay without oxygen is anaerobic decay. Anaerobic decay produces methane "
                  "gas.",
                  "Biogas generators can be used to produce methane gas as a fuel. Waste such as "
                  "animal manure or food waste decays inside, without oxygen. The methane is "
                  "collected and burned."]},
        {"kind": "card", "title": "Required practical activity 10", "routes": TRIPLE,
         "body": ["Investigate the effect of temperature on the rate of decay of fresh milk by "
                  "measuring pH change.",
                  {"points": [
                      "1. Mix milk with sodium carbonate solution and a few drops of "
                      "phenolphthalein indicator. The mixture is pink, because it is alkaline.",
                      "2. Put this tube and a tube of lipase solution in a water bath at the "
                      "first temperature. Wait until both reach that temperature.",
                      "3. Add the lipase to the milk and start a timer.",
                      "4. Lipase breaks down the fat in the milk into fatty acids and glycerol. "
                      "The fatty acids lower the pH.",
                      "5. Stop the timer when the pink colour disappears.",
                      "6. Repeat at other temperatures. Keep the volumes the same each time.",
                  ]},
                  "The shorter the time, the faster the rate. rate = 1 ÷ time."]},
        {"kind": "card", "title": "Calculating a rate of decay", "routes": TRIPLE,
         "body": ["rate of decay = change ÷ time",
                  "A leaf's mass falls from 12.0 g to 9.0 g in 6 days.",
                  {"points": [
                      "Change in mass = 12.0 − 9.0 = 3.0 g",
                      "rate = 3.0 ÷ 6",
                      "rate = 0.5 g per day",
                  ]},
                  "In the milk practical, the pink colour disappears after 200 s. "
                  "rate = 1 ÷ 200 = 0.005 per second."]},
        {"kind": "card", "title": "Graphs of decay", "routes": TRIPLE,
         "body": [{"points": [
             "Put the variable you changed, such as temperature, on the x-axis. Put the rate on "
             "the y-axis.",
             "Choose scales so the points fill most of the grid.",
             "Plot each point and draw a line of best fit: a straight line or a smooth curve.",
             "On a graph of mass against time, the rate between two times = change in mass ÷ "
             "change in time.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Decay destroys the carbon in dead organisms.",
              "Decay returns the carbon to the atmosphere as carbon dioxide."),
             ("The microorganisms that cause decay photosynthesise.",
              "They respire, which releases carbon dioxide."),
             ("Decay is bad for plants.",
              "Decay returns mineral ions to the soil for plants to use."),
         ]}]},
        {"kind": "card", "title": "Easy mistakes: the rate of decay", "routes": TRIPLE,
         "body": [{"mistakes": [
             ("The hotter it is, the faster the decay, always.",
              "Above the optimum, the enzymes denature and decay slows."),
             ("A fridge kills the microorganisms in food.",
              "Cold slows their enzymes and their growth. It does not kill them."),
             ("Anaerobic decay produces oxygen.",
              "Anaerobic decay produces methane."),
         ]}]},
    ],
    "key_fact": "Microorganisms such as bacteria and fungi decay dead material. As they respire "
                "they return carbon to the atmosphere as carbon dioxide, and they return mineral "
                "ions to the soil, so plants can use both again.",
    "deeper": [
        {"kind": "card", "title": "Biogas and the weather", "routes": TRIPLE,
         "body": ["A biogas generator makes gas faster in warm weather. The enzymes in the "
                  "microorganisms work faster when it is warm.",
                  "In cold weather it makes less gas, unless it is kept warm."]},
        {"kind": "card", "title": "Link to the carbon cycle",
         "body": ["Decay is the arrow in the carbon cycle that takes carbon from dead material "
                  "back to the air. The Carbon cycle lesson shows the whole cycle."]},
        {"kind": "card", "title": "Command words", "routes": ["CF", "CH"],
         "body": [{"points": [
             "<strong>Explain</strong>: say what the microorganisms do and why it matters, for "
             "example that they respire and so release carbon dioxide.",
             "<strong>Describe</strong>: say what happens, in order.",
         ]}]},
        {"kind": "card", "title": "Command words", "routes": ["TF", "TH"],
         "body": [{"points": [
             "<strong>Explain</strong>: say what the microorganisms do and why it matters, for "
             "example that they respire and so release carbon dioxide.",
             "<strong>Calculate</strong>: work out a number and show each line.",
             "<strong>Describe</strong>: say what happens, in order.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the type of organism that decays dead plants and animals.",
             "why": "Microorganisms, such as bacteria and fungi, cause decay.",
             "options": [
                 {"text": "Producers", "correct": False,
                  "reply": "Producers make their own food by photosynthesis."},
                 {"text": "Herbivores", "correct": False,
                  "reply": "Herbivores eat living plants."},
                 {"text": "Microorganisms", "correct": True},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "Decay returns mineral ions to which part of the ecosystem?",
             "why": "Microorganisms return mineral ions to the soil and carbon to the atmosphere.",
             "options": [
                 {"text": "The soil", "correct": True},
                 {"text": "The atmosphere", "correct": False,
                  "reply": "Carbon goes to the atmosphere, as carbon dioxide. Mineral ions go to "
                           "the soil."},
                 {"text": "The leaves of plants", "correct": False,
                  "reply": "Mineral ions go to the soil first. Roots then take them up."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain how microorganisms return the carbon in a dead leaf to the "
                       "atmosphere.",
             "why": "The microorganisms feed on the leaf and respire. Respiration releases "
                    "carbon dioxide.",
             "options": [
                 {"text": "They photosynthesise, releasing the carbon as oxygen",
                  "correct": False,
                  "reply": "Microorganisms that cause decay respire. Oxygen contains no carbon."},
                 {"text": "They feed on the leaf and respire, releasing carbon dioxide",
                  "correct": True},
                 {"text": "They burn the leaf, releasing carbon dioxide as smoke",
                  "correct": False,
                  "reply": "Nothing burns. The microorganisms respire."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A farmer ploughs the dead roots of last year's crop into the soil. "
                       "Explain how this helps next year's crop.",
             "why": "Microorganisms decay the roots and return mineral ions to the soil. The new "
                    "crop takes them up.",
             "options": [
                 {"text": "The dead roots photosynthesise and make glucose for the crop",
                  "correct": False,
                  "reply": "Dead roots do nothing. Microorganisms decay them."},
                 {"text": "Microorganisms decay the roots and return mineral ions to the soil",
                  "correct": True},
                 {"text": "The dead roots take carbon dioxide out of the soil",
                  "correct": False,
                  "reply": "Decay releases carbon dioxide. It returns mineral ions to the soil."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how the mineral ions in a dead animal can end up in a living "
                       "plant. Put the links in order.",
             "links": ["Microorganisms feed on the dead animal and break it down.",
                       "The mineral ions from the animal are returned to the soil.",
                       "A plant's roots take up the mineral ions from the soil."],
             "herrings": [{"text": "The plant's leaves take in the mineral ions from the air.",
                           "why": "Mineral ions are returned to the soil and taken up by "
                                  "roots."},
                          {"text": "The microorganisms make new mineral ions by photosynthesis.",
                           "why": "Mineral ions are not made. They are recycled from the dead "
                                  "animal."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain what would happen to a wood if every microorganism in its soil "
                       "were killed. Put the links in order.",
             "links": ["Dead leaves and wood would no longer decay.",
                       "Carbon and mineral ions would stay locked in the dead material.",
                       "The soil would run short of mineral ions, so the trees would grow less "
                       "well."],
             "herrings": [{"text": "More carbon dioxide would be returned to the air.",
                           "why": "Without decay, less carbon dioxide is returned to the air."},
                          {"text": "The trees would grow faster, with nothing to compete with.",
                           "why": "Microorganisms return mineral ions. Without them the soil "
                                  "runs short."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Explain the role of microorganisms in cycling materials through an "
                       "ecosystem.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Says that microorganisms decay dead "
                  "material, and explains how both carbon and mineral ions are returned and "
                  "used again.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Says microorganisms break down dead "
                  "material, or names one material returned.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Microorganisms (bacteria and fungi) decay dead plants, dead animals "
                        "and animal waste.",
                        "As they feed, they respire, returning carbon to the atmosphere as "
                        "carbon dioxide.",
                        "Plants take in the carbon dioxide for photosynthesis.",
                        "Decay returns mineral ions to the soil, which plants take up through "
                        "their roots.",
                        "So materials are recycled to provide the building blocks for future "
                        "organisms."],
             "reject": ["“Microorganisms destroy the carbon.”",
                        "“Decay takes carbon dioxide out of the air.”"]},
        ],
    },
}
