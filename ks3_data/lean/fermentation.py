# -*- coding: utf-8 -*-
"""Fermentation, in the lean shape. Spec table: docs/lessons/wave1/ks3-fermentation.md."""

LESSON = {
    "slug": "fermentation",
    "start": {
        "setup": "Bread dough is flour, water and a little yeast. Left somewhere warm, it rises and fills with holes.",
        "question": "If you had to guess, what made the holes?",
        "options": [
            ("The yeast cells swelling up", "A gas the yeast gave off. The holes are bubbles of carbon dioxide."),
            ("A gas the yeast gave off", "A gas the yeast gave off. The holes are bubbles of carbon dioxide."),
        ],
        "answer": 1,
    },
    "words": ["fermentation", "yeast", "ethanol", "limewater"],
    "word_defs": {
        "fermentation": "Anaerobic respiration in yeast. It makes ethanol and carbon dioxide.",
        "yeast": "A single-celled fungus. Bakers and brewers use it.",
        "ethanol": "A type of alcohol. Yeast makes it in fermentation.",
        "limewater": "A liquid that turns cloudy when carbon dioxide bubbles through it.",
    },
    "knowledge": [
        {"kind": "card", "title": "Fermentation",
         "body": ["Yeast is a single-celled fungus.",
                  "When it is short of oxygen, yeast respires anaerobically.",
                  "Anaerobic respiration in yeast is called fermentation."]},
        {"kind": "card", "title": "The word summary",
         "body": [{"figure": "b8-word-fermentation"},
                  "Plant cells respire anaerobically in the same way when they are short of oxygen.",
                  "Fermentation releases much less energy than aerobic respiration."]},
        {"kind": "reveal", "title": "Anaerobic respiration in muscles and in yeast",
         "cols": ["Human muscle cells", "Yeast and plant cells"],
         "rows": [
             ("Reactant", "Glucose", "Glucose"),
             ("Products", "Lactic acid", "Ethanol and carbon dioxide"),
             ("Gas given off", "None", "Carbon dioxide"),
         ]},
        {"kind": "card", "title": "Showing that yeast respires anaerobically",
         "body": [{"figure": "b8-yeast-limewater"},
                  {"points": ["Boil water to remove its oxygen, then let it cool.",
                              "Mix yeast and sugar into the water.",
                              "Pour a thin layer of oil on top to keep air out.",
                              "Run a delivery tube from the yeast into limewater.",
                              "Keep the yeast warm in a water bath."]},
                  "Bubbles of gas pass into the limewater. The limewater turns cloudy.",
                  "A control tube with boiled yeast gives no bubbles.",
                  "So living yeast made carbon dioxide without oxygen."]},
        {"kind": "card", "title": "Bread and beer",
         "body": ["Bakers use the carbon dioxide. Its bubbles make bread dough rise.",
                  "Ethanol boils at 78 °C, far below oven temperature. So it evaporates as the bread bakes.",
                  "Ethanol is the alcohol in beer and wine."]},
        {"kind": "card", "title": "Yoghurt",
         "body": ["Yoghurt bacteria also respire anaerobically.",
                  "They turn the sugar in milk into lactic acid. This is also fermentation.",
                  "The acid thickens the milk into yoghurt.",
                  "The acid also slows the growth of microbes that spoil food. So yoghurt keeps longer."]},
        {"kind": "card", "title": "Temperature matters",
         "body": ["Yeast is alive, so temperature changes how fast it respires.",
                  "Warm yeast respires faster than cold yeast.",
                  "The temperature at which it works fastest is called the optimum.",
                  "Too hot, and the yeast's enzymes are denatured. They change shape and stop working.",
                  "This cannot be undone, so very hot water kills yeast."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Yeast makes lactic acid.",
              "Yeast makes ethanol and carbon dioxide. Human muscles make lactic acid."),
             ("Bread rises because the yeast cells swell.",
              "Bubbles of carbon dioxide make the dough rise."),
             ("Fermentation needs oxygen.",
              "Fermentation is anaerobic. It happens without oxygen."),
         ]}]},
    ],
    "key_fact": "Fermentation is anaerobic respiration in yeast. Yeast turns glucose into ethanol and "
                "carbon dioxide. Plant cells respire anaerobically in the same way.",
    "deeper": [
        {"kind": "card", "title": "Why brewers keep air out",
         "body": ["With oxygen, yeast respires aerobically instead.",
                  "Then it makes carbon dioxide and water, not ethanol.",
                  "So brewers seal their tanks to get alcohol."]},
        {"kind": "card", "title": "Roots in waterlogged soil",
         "body": ["Roots in waterlogged soil get very little oxygen.",
                  "They respire anaerobically and make ethanol.",
                  "Ethanol builds up and harms the roots."]},
    ],
    "try": None,
    "figure_caption": {"b8-word-fermentation": None,      # the card text already says it
                       "b8-yeast-limewater": None},
    "ladder_stem": {
        "explain": "Bacteria are added to warm milk to make yoghurt. Explain how the milk becomes yoghurt. "
                   "Explain why yoghurt keeps longer than milk.",
        "produce": "Design an investigation to find the temperature at which yeast ferments fastest. Say "
                   "what you would measure and what you would keep the same. Describe the result you "
                   "expect. Explain what happens above the optimum temperature.",
    },
    "ladder_ticks": [
        ["Says the acid lowers the pH, which curdles the milk protein and thickens it.",
         "Says the acid thickens the milk into yoghurt."],
        ["Says particular bacteria are added to warm milk deliberately.",
         "Names the process as fermentation, or anaerobic respiration."],
        ["Says the low pH stops spoilage micro-organisms from growing.",
         "Says the acid slows the growth of microbes that spoil food."],
        ["Concludes that the yoghurt therefore keeps longer — the chosen organism has made the milk "
         "uninhabitable for the others.",
         "Concludes that the yoghurt therefore keeps longer than the milk."],
        ["Sets up several identical flasks of yeast and sugar solution, each at a different temperature in a "
         "water bath.",
         "Sets up identical yeast and sugar flasks in water baths at different temperatures."],
        ["Measures the rate as bubbles of carbon dioxide per minute, or gas volume collected in a fixed time.",
         "Measures the rate as bubbles per minute, or gas collected in a fixed time."],
        ["Keeps the same the mass of yeast, the sugar concentration, the volume of solution and the time allowed.",
         "Keeps the yeast mass, sugar concentration, volume and time the same."],
        ["Explains the fall above the optimum as the yeast’s enzymes being denatured — and notes this "
         "is permanent, so cooling the flask does not restore it.",
         "Says above the optimum the enzymes are denatured. Cooling the flask does not undo this."],
    ],
    "figures": [
        {"id": "b8-word-fermentation", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The word summary for fermentation",
         "desc": "Glucose at the top, labelled reactant. A drawn arrow points down to ethanol plus "
                 "carbon dioxide, labelled products.",
         "caption": "The word summary for fermentation.",
         "eq": {"left": ["glucose"], "right": ["ethanol", "carbon dioxide"]}},
        {"id": "b8-yeast-limewater", "kind": "diagram", "status": "drawn", "art": "yeast-limewater",
         "title": "Showing that yeast respires anaerobically",
         "desc": "A tube of yeast and sugar solution with a layer of oil on top, stood in a warm water "
                 "bath. A delivery tube runs from its bung into a second tube of limewater, where "
                 "bubbles of gas rise.",
         "caption": "Yeast and sugar solution, with a delivery tube into limewater."},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Human muscles make lactic acid. Yeast makes ethanol and carbon dioxide.",
            2: "Carbon dioxide and water come from aerobic respiration.",
            3: "Oxygen and glucose are made by photosynthesis, not respiration.",
        },
        "apply": {
            1: "Yeast does not take the ethanol back. It evaporates in the hot oven.",
            2: "Bread yeast does make ethanol. It evaporates in the hot oven.",
            3: "Flour does not cancel out ethanol. It evaporates in the hot oven.",
        },
    },
}
