# -*- coding: utf-8 -*-
"""Power, in the lean shape. Spec table: docs/lessons/pilot/ks4-power.md."""

LESSON = {
    "slug": "power",
    "start": {
        "setup": "Two motors lift the same load to the same height. One takes twice as long.",
        "question": "If you had to guess, which motor has more power?",
        "options": [
            ("The faster motor",
             "The faster motor. It transfers the same energy in less time."),
            ("They have equal power",
             "The faster motor. It transfers the same energy in less time."),
        ],
        "answer": 0,
    },
    "words": ["power", "watt", "energy transferred", "work done"],
    "knowledge": [
        {"kind": "card", "title": "What power means",
         "body": ["Power is the rate at which energy is transferred or the rate at which work "
                  "is done.",
                  "An energy transfer of 1 joule per second is equal to a power of 1 watt."]},
        {"kind": "card", "title": "The equations",
         "body": ["power = energy transferred ÷ time",
                  "P = E ÷ t",
                  "power = work done ÷ time",
                  "P = W ÷ t",
                  {"points": ["power, P, in watts (W)",
                              "energy transferred, E, in joules (J)",
                              "work done, W, in joules (J)",
                              "time, t, in seconds (s)"]},
                  "You need to remember both equations.",
                  {"slot": "triangle:EQ_PE"},
                  {"slot": "triangle:EQ_PW"}]},
        {"kind": "card", "title": "Comparing two motors",
         "body": ["Two motors lift the same weight through the same height.",
                  "They do the same amount of work.",
                  "The motor that does it in less time has the greater power."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Units first",
         "body": ["Joules and seconds go in. Watts come out. Convert anything else first.",
                  {"points": ["1 kW = 1000 W", "1 MW = 1 000 000 W", "1 kJ = 1000 J",
                              "1 minute = 60 s", "1 hour = 3600 s"]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("It took 2 minutes, so divide by 2.",
              "Time must be in seconds. 2 minutes is 120 s."),
             ("The more powerful motor can lift the heavier load.",
              "Power is how quickly energy is transferred. It is not a force."),
         ]}]},
    ],
    "key_fact": "Power is the rate at which energy is transferred or the rate at which work is "
                "done. One watt is an energy transfer of one joule per second.",
    "deeper": [
        {"kind": "card", "title": "Two kettles",
         "body": ["A 3000 W kettle transfers 3000 J each second.",
                  "A 1500 W kettle transfers 1500 J each second.",
                  "To transfer the same energy, the 1500 W kettle takes twice as long."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Define</strong>: give the exact meaning in one sentence.",
             "<strong>Calculate</strong>: convert, write the equation, substitute, rearrange, "
             "then give the answer with its unit.",
             "<strong>Explain</strong>: link the work done and the time taken to the rate of "
             "energy transfer.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3"},
    "equations": {
        "EQ_PE": {"name": "Power from energy", "written": "power = energy transferred ÷ time",
                  "source": "none",
                  "top": {"s": "E", "name": "energy transferred", "unit": "J"},
                  "bottom": [{"s": "P", "name": "power", "unit": "W"},
                             {"s": "t", "name": "time", "unit": "s"}]},
        "EQ_PW": {"name": "Power from work", "written": "power = work done ÷ time",
                  "source": "none",
                  "top": {"s": "W", "name": "work done", "unit": "J"},
                  "bottom": [{"s": "P", "name": "power", "unit": "W"},
                             {"s": "t", "name": "time", "unit": "s"}]},
    },
}
