# -*- coding: utf-8 -*-
"""Exercise, asthma and smoking, in the lean shape. Spec table: docs/lessons/pilot/ks3-exercise-asthma-and-smoking.md.

Tone rule carried over from the old page: factual. No advice, no doses, no warnings added."""

LESSON = {
    "slug": "exercise-asthma-and-smoking",
    "start": {
        "setup": "A reliever inhaler helps someone having an asthma attack.",
        "question": "If you had to guess, does the puff from the inhaler contain extra oxygen?",
        "options": [
            ("Yes, extra oxygen", "No oxygen at all. The inhaler relaxes the muscle in the bronchioles, so the airways open."),
            ("No oxygen at all", "No oxygen at all. The inhaler relaxes the muscle in the bronchioles, so the airways open."),
        ],
        "answer": 1,
    },
    "words": ["asthma", "bronchioles", "cilia", "carbon monoxide"],
    "knowledge": [
        {"kind": "card", "title": "What exercise does",
         "body": ["When you exercise, your muscles respire faster.",
                  "They need more oxygen and make more carbon dioxide.",
                  "Your brain detects the rising carbon dioxide in your blood.",
                  "Your breathing gets faster and deeper. Your heart rate rises too.",
                  "This delivers more oxygen and removes more carbon dioxide.",
                  "These changes reverse after you stop."]},
        {"kind": "card", "title": "What asthma does",
         "body": ["In an asthma attack, the bronchioles get narrower.",
                  "The muscle in their walls contracts.",
                  "The lining swells and makes more mucus.",
                  "Less air can get through to the alveoli.",
                  "A reliever inhaler relaxes the muscle, so the airways open again."]},
        {"kind": "reveal", "title": "What is in cigarette smoke",
         "cols": ["What it does", "The result"],
         "rows": [
             ("Tar", "Coats the airways and damages cilia", "Mucus builds up. Tar contains substances that cause cancer."),
             ("Carbon monoxide", "Joins to haemoglobin in red blood cells", "Blood carries less oxygen"),
             ("Nicotine", "Narrows blood vessels and raises heart rate", "It is addictive, so stopping is hard"),
             ("Particulates and heat", "Irritate the lining of the airways", "More mucus is made"),
         ]},
        {"kind": "card", "title": "What smoking does to the alveoli",
         "body": ["Smoking damages the walls of the alveoli. This disease is called emphysema.",
                  "The surface area for gas exchange falls.",
                  "This damage is permanent."]},
        {"kind": "reveal", "title": "What recovers",
         "cols": ["What changes", "Recovers"],
         "rows": [
             ("Exercise", "Faster, deeper breathing", "Yes, soon after you stop"),
             ("Asthma attack", "Narrowed bronchioles", "Yes, with treatment"),
             ("Carbon monoxide", "Less oxygen carried", "Yes, within about a day of stopping smoking"),
             ("Cilia", "Damaged by tar", "Mostly, over weeks to months after stopping smoking"),
             ("Alveoli walls", "Destroyed by smoking", "No, this is permanent"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Being out of breath means your lungs cannot hold enough air.",
              "Your body is responding to rising carbon dioxide."),
             ("In an asthma attack there is not enough oxygen in the air.",
              "The air is the same. The airways have narrowed."),
         ]}]},
    ],
    "key_fact": "Exercise raises breathing rate, and this reverses after you stop. In an asthma "
                "attack the airways narrow, and treatment can open them again. Smoking destroys "
                "the walls of the alveoli, which permanently reduces gas exchange.",
    "deeper": [
        {"kind": "card", "title": "Why you keep panting after you stop",
         "body": ["Your blood still holds extra carbon dioxide when you stop.",
                  "After hard exercise, your body also needs oxygen to break down lactic acid.",
                  "You keep breathing hard until this is done."]},
        {"kind": "card", "title": "Why the air is not the problem in an asthma attack",
         "body": ["The air already holds plenty of oxygen.",
                  "The problem is the narrow airways, so less air can get through.",
                  "A reliever inhaler treats that by opening the airways."]},
        {"kind": "card", "title": "Emphysema and lung volume",
         "body": ["In emphysema, the walls between alveoli break down.",
                  "The lungs still hold about as much air.",
                  "But the surface area is much smaller, so gas exchange is poor."]},
    ],
    "try": None,
    # render-only overlays (ks3_data/lean/__init__.py, build_ks3.py): nothing here reaches the question mirror
    "connects": {
        "Antagonistic muscle pairs": "Muscles can only pull, so they work in pairs.",
    },
    "word_defs": {
        "asthma": "A condition in which the bronchioles narrow. The muscle contracts, the lining swells and extra mucus is made.",
    },
    "ladder_stem": {
        "produce": "A patient with emphysema has almost normal lung volume but greatly reduced gas transfer. "
                   "Explain how both can be true, using what you learnt about alveoli. Say which feature of "
                   "a good exchange surface has been lost.",
    },
    "ladder_ticks": [
        ["Identifies the problem as narrowed bronchioles \u2014 muscle contraction, swelling and mucus.",
         "Identifies the problem as narrowed bronchioles: muscle contraction, swelling and mucus."],
        ["Identifies large surface area as the requirement that has been lost.",
         "Identifies large surface area as the feature that has been lost."],
        ["Connects this back to the hook of the alveoli lesson \u2014 the patient has moved partway towards the smooth bag.",
         "Says the alveoli have joined into fewer, larger spaces, more like one smooth bag."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Blood oxygen hardly changes in ordinary exercise. Your body detects carbon dioxide.",
            2: "Your lungs do not empty during exercise. Your body detects carbon dioxide.",
            3: "Breathing speeds up before you feel tired. It follows carbon dioxide in the blood.",
        },
        "apply": {
            0: "This clears about a day after the last cigarette.",
            1: "Cilia recover over weeks to months after stopping.",
            3: "This reduces once the irritation stops.",
        },
    },
}
