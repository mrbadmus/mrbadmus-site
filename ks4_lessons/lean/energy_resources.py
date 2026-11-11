# -*- coding: utf-8 -*-
"""Energy resources, in the lean shape. Spec table: docs/lessons/pilot/ks4-energy-resources.md."""

LESSON = {
    "slug": "energy-resources",
    "start": {
        "setup": "It is the middle of the night, dark and completely still. A phone plugged into the wall is charging.",
        "question": "If you had to guess, where is most of that electricity coming from?",
        "options": [
            ("Wind turbines and solar panels", "Power stations that can run whenever they are needed. With no wind and no daylight, wind turbines and solar panels produce nothing."),
            ("Power stations that can run whenever they are needed", "Power stations that can run whenever they are needed. With no wind and no daylight, wind turbines and solar panels produce nothing."),
        ],
        "answer": 1,
    },
    "words": ["energy resource", "renewable", "non-renewable", "reliable"],
    "knowledge": [
        {"kind": "card", "title": "Renewable and reliable",
         "body": ["A renewable energy resource is one that is being, or can be, replenished as "
                  "it is used.",
                  "A non-renewable resource will run out.",
                  "A reliable resource can be used whenever it is needed, or at times you can "
                  "predict."]},
        {"kind": "reveal", "title": "The main energy resources",
         "cols": ["Renewable", "Reliable"],
         "rows": [
             ("Fossil fuels (coal, oil, gas)", "No. They will run out.", "Yes. They can be burned whenever needed."),
             ("Nuclear fuel", "No. Uranium is finite.", "Yes. Power stations run steadily all the time."),
             ("Bio-fuel", "Yes. The plants regrow.", "Yes. It can be burned whenever needed."),
             ("Wind", "Yes.", "No. There is no output when the wind drops."),
             ("Hydro-electricity", "Yes. Rain refills the reservoir.", "Yes. Water can be released when needed."),
             ("Geothermal", "Yes.", "Yes. It is available all the time."),
             ("The tides", "Yes.", "Yes. Tide times can be predicted."),
             ("The Sun", "Yes.", "No. There is none at night and less on cloudy days."),
             ("Water waves", "Yes.", "No. Wave size depends on the weather."),
         ]},
        {"kind": "reveal", "title": "What we use them for",
         "cols": ["Main resources"],
         "rows": [
             ("Transport", "Mostly oil-based fuels, some bio-fuel and electricity"),
             ("Electricity generation", "A mix of many resources"),
             ("Heating", "Mostly gas, some electricity, some geothermal and solar"),
         ]},
        {"kind": "reveal", "title": "Environmental impact",
         "cols": ["The main impact"],
         "rows": [
             ("Fossil fuels", "Burning them releases carbon dioxide, which adds to global warming. Coal and oil also release sulfur dioxide, which causes acid rain."),
             ("Nuclear fuel", "Radioactive waste must be stored safely for a very long time."),
             ("Bio-fuel", "Growing fuel crops uses land that could grow food."),
             ("Wind", "Turbines can be noisy and change the look of the landscape."),
             ("Hydro-electricity", "Building a dam floods a valley and destroys habitats."),
             ("Geothermal", "Drilling can release gases from underground, and the power station takes up land."),
             ("The tides", "A tidal barrage changes the habitat of estuary wildlife."),
             ("The Sun", "Making solar panels uses energy and materials."),
             ("Water waves", "Wave machines can disturb marine habitats."),
         ]},
        {"kind": "card", "title": "Patterns and trends",
         "body": ["Exams give you a chart and ask you to describe the trend, then explain it.",
                  {"slot": "mix"},
                  {"points": [
                      "Coal fell from 35% to 2%. Burning coal releases carbon dioxide, and the "
                      "country chose to cut its emissions.",
                      "Wind and solar rose from 1% to 30%. They release no carbon dioxide while "
                      "running.",
                      "Gas stayed large. It can be used on demand when the wind drops or it is dark.",
                  ]}]},
        {"kind": "card", "title": "What science can and cannot do",
         "body": ["Science can identify environmental problems, such as carbon dioxide from "
                  "burning coal.",
                  "Science does not always have the power to deal with them. Political, social, "
                  "ethical and economic considerations also decide what happens."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Nuclear power is renewable because it makes no carbon dioxide.",
              "Low carbon and renewable are different. Nuclear fuel will run out."),
             ("Renewable resources have no environmental impact.",
              "Every resource has some environmental impact."),
         ]}]},
    ],
    "key_fact": "Fossil fuels and nuclear fuel are non-renewable, while bio-fuel, wind, "
                "hydro-electricity, geothermal, the tides, the Sun and water waves are renewable. "
                "Every resource has some environmental impact.",
    "deeper": [
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what the chart shows, with numbers from it.",
             "<strong>Explain</strong>: give the reason, such as renewable or not, reliable or "
             "not, and the impact.",
             "<strong>Evaluate</strong>: give points for and against each resource, then a "
             "judgement with a reason.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-5"},
}
