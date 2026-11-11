# -*- coding: utf-8 -*-
"""Exercise, asthma and smoking, in the lean shape. Spec table: docs/lessons/pilot/ks3-exercise-asthma-and-smoking.md.

Tone rule carried over from the old page: factual. No advice, no doses, no warnings added."""

LESSON = {
    "slug": "exercise-asthma-and-smoking",
    "start": {
        "setup": None,
        "question": "If you had to guess, what does a reliever inhaler do?",
        "options": [
            ("It opens up the airways",
             "It opens up the airways. In an asthma attack the bronchioles narrow, and the "
             "inhaler relaxes their muscle."),
            ("It adds oxygen to the air",
             "It opens up the airways. In an asthma attack the bronchioles narrow, and the "
             "inhaler relaxes their muscle."),
        ],
        "answer": 0,
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
             ("Cilia", "Damaged by tar", "Yes, over weeks to months after stopping smoking"),
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
    "key_fact": "Exercise raises breathing rate and asthma narrows the airways, and both can be "
                "reversed. Smoking destroys the walls of the alveoli, which permanently reduces "
                "gas exchange.",
    "deeper": [
        {"kind": "card", "title": "Why you keep panting after you stop",
         "body": ["Your blood still holds extra carbon dioxide when you stop.",
                  "You keep breathing hard until it has been removed."]},
        {"kind": "card", "title": "Why oxygen does not fix an asthma attack",
         "body": ["The air already holds plenty of oxygen.",
                  "The problem is the narrow airways, so air cannot get through.",
                  "A reliever inhaler treats that by opening the airways."]},
        {"kind": "card", "title": "Emphysema and lung volume",
         "body": ["In emphysema, the walls between alveoli break down.",
                  "The lungs still hold nearly as much air.",
                  "But the surface area is much smaller, so gas exchange is poor."]},
    ],
    "try": None,
    "ladder_feedback": {
        "recall": {
            0: "Blood oxygen hardly changes in ordinary exercise. Your body detects carbon dioxide.",
            2: "Your body does not measure how full the lungs are.",
            3: "Breathing speeds up before you feel tired. It follows carbon dioxide in the blood.",
        },
        "apply": {
            0: "This clears about a day after the last cigarette.",
            1: "Cilia recover over weeks to months after stopping.",
            3: "This reduces once the irritation stops.",
        },
    },
}
