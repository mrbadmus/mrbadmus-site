# -*- coding: utf-8 -*-
"""Anaerobic respiration in humans, in the lean shape. Spec table: docs/lessons/wave1/ks3-anaerobic-respiration-in-humans.md."""

LESSON = {
    "slug": "anaerobic-respiration-in-humans",
    "start": {
        "setup": "A 100 m sprinter takes only a few breaths during the race.",
        "question": "If you had to guess, do the muscles stop using oxygen, or keep using it?",
        "options": [
            ("They stop using oxygen", "They keep using it too. They also break down extra glucose without oxygen."),
            ("They keep using it too", "They keep using it too. They also break down extra glucose without oxygen."),
        ],
        "answer": 1,
    },
    "words": ["anaerobic respiration", "lactic acid", "oxygen debt"],
    "word_defs": {
        "anaerobic respiration": "Respiration without oxygen. It releases much less energy from each glucose.",
        "lactic acid": "The product of anaerobic respiration in human muscles.",
        "oxygen debt": "The extra oxygen needed after exercise to break down lactic acid.",
    },
    "knowledge": [
        {"kind": "card", "title": "When oxygen runs short",
         "body": ["In a sprint, your muscles need energy very fast.",
                  "Your heart and lungs cannot bring oxygen fast enough.",
                  "Aerobic respiration carries on as fast as the oxygen allows.",
                  "Anaerobic respiration makes up the rest. It does not use oxygen."]},
        {"kind": "card", "title": "The word summary",
         "body": [{"figure": "b8-word-anaerobic"},
                  "Anaerobic means without oxygen.",
                  "The glucose is only partly broken down.",
                  "So it releases much less energy than aerobic respiration.",
                  "It makes no carbon dioxide and no water."]},
        {"kind": "card", "title": "Lactic acid and tired muscles",
         "body": ["Lactic acid builds up in the muscles.",
                  "During long, hard exercise, the muscles get tired and stop contracting efficiently."]},
        {"kind": "card", "title": "The oxygen debt",
         "body": ["After hard exercise, you keep breathing hard and your heart keeps beating fast.",
                  "This brings extra oxygen to break down the lactic acid.",
                  "The oxygen needed to remove the lactic acid is called the oxygen debt."]},
        {"kind": "card", "title": "Why training helps",
         "body": ["Training makes the heart stronger. It pumps more blood with each beat.",
                  "More oxygen reaches the muscles during exercise.",
                  "So a fit person respires less anaerobically and makes less lactic acid.",
                  "Their oxygen debt is smaller, so they recover faster."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("In a sprint, muscles switch from aerobic to anaerobic respiration.",
              "Aerobic respiration carries on. Anaerobic respiration adds to it."),
             ("Anaerobic respiration in humans makes carbon dioxide.",
              "In human muscles, it makes lactic acid only."),
             ("Lactic acid makes your legs ache two days later.",
              "That ache comes from tiny damage to muscle fibres. The lactic acid is long gone."),
         ]}]},
    ],
    "key_fact": "When muscles cannot get enough oxygen, they also respire anaerobically. Glucose is broken "
                "down to lactic acid. This releases much less energy than aerobic respiration. The extra "
                "oxygen needed afterwards to break down the lactic acid is the oxygen debt.",
    "deeper": [
        {"kind": "card", "title": "Where the lactic acid goes",
         "body": ["The blood carries lactic acid away from the muscles to the liver.",
                  "The liver turns it back into glucose."]},
    ],
    "try": None,
    "figure_caption": {"b8-word-anaerobic": None},      # the card text already says it
    "ladder_stem": {
        "apply": "You finish a sprint and stand still. You go on breathing hard for two minutes. Why?",
        "explain": "A sprint starts. Two minutes after it ends, you are still breathing hard. Explain why "
                   "anaerobic respiration happens in the sprint. Explain what the oxygen debt is.",
        "produce": "Two students run the same distance at the same speed. One is back to normal breathing "
                   "in 40 seconds. The other takes three minutes. Explain what this difference shows. Then "
                   "design a fair test of one person’s recovery. Test them before and after six weeks of training.",
    },
    "ladder_ticks": [
        ["Says the heart and lungs cannot deliver oxygen fast enough to supply all of it aerobically.",
         "Says the heart and lungs cannot deliver oxygen fast enough for aerobic respiration alone."],
        ["Says aerobic respiration continues throughout at the highest rate the oxygen supply allows — the "
         "two happen together.",
         "Says aerobic respiration carries on at the same time, as fast as the oxygen allows."],
        ["Says the deep breathing afterwards supplies the oxygen needed to deal with the lactic acid, and names "
         "this the oxygen debt.",
         "Says the hard breathing afterwards brings oxygen to break down lactic acid. This is the oxygen debt."],
        ["Says the fitter student delivered more oxygen during the run, so less of the energy came from "
         "anaerobic respiration.",
         "Says the fitter student got more oxygen to their muscles, so respired less anaerobically."],
        ["Says that student therefore built up less lactic acid and has a smaller oxygen debt to repay.",
         "Says they made less lactic acid, so they had a smaller oxygen debt."],
        ["Designs a test where everyone does the same exercise for the same time or distance.",
         "Has the person do the same exercise, for the same time or distance, both times."],
        ["Says recovery time is measured the same way for everyone — for example, time for pulse rate to "
         "return to its resting value.",
         "Measures recovery the same way each time, such as time for the pulse to settle."],
        ["Identifies something that must be controlled or accounted for, such as measuring each person’s "
         "resting rate first, or the fact that people start at different fitness levels.",
         "Names another control variable, such as the time of day or what they ate before."],
    ],
    "figures": [
        {"id": "b8-word-anaerobic", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The word summary for anaerobic respiration in humans",
         "desc": "Glucose at the top, labelled reactant. A drawn arrow points down to lactic acid, "
                 "labelled product.",
         "caption": "The word summary for anaerobic respiration in humans.",
         "eq": {"left": ["glucose"], "right": ["lactic acid"]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Anaerobic means without oxygen. No oxygen is used.",
            1: "Human muscles do not make alcohol. They make lactic acid.",
            2: "Carbon dioxide and water come from aerobic respiration.",
        },
        "apply": {
            1: "Lungs do not run on by themselves. Your body needs extra oxygen.",
            2: "Your muscles have stopped working hard. The extra oxygen breaks down lactic acid.",
            3: "You lose heat mainly by sweating. The extra oxygen breaks down lactic acid.",
        },
    },
}
