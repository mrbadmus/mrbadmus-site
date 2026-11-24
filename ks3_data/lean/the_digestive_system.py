# -*- coding: utf-8 -*-
"""The digestive system, in the lean shape. Spec table: docs/lessons/wave2/ks3-the-digestive-system.md.

Rainford 15a asks pupils to label the organs. The old page drew the gut as one straightened
tube with numbered stops, so the organs are now drawn in their places in a body outline
(new figure b3-gut-body, phone width).
"""

LESSON = {
    "slug": "the-digestive-system",
    "start": {
        "setup": "A cheese sandwich is blended for two minutes. It becomes a smooth liquid with no lumps.",
        "question": "If you had to guess, could that smooth liquid go straight into your blood?",
        "options": [
            ("Yes, it is smooth enough",
             "Blending only makes the pieces smaller. The starch molecules in it are still too big."),
            ("No, it is not broken down enough",
             "Right. The starch is still in big molecules. Enzymes must break them into small ones."),
        ],
        "answer": 1,
    },
    "words": ["digestion", "absorption", "peristalsis", "egestion"],
    "word_defs": {
        "digestion": "Breaking large food molecules into small, soluble molecules.",
        "absorption": "Small food molecules passing from the gut into the blood.",
        "peristalsis": "Waves of muscle squeezing that push food along the gut.",
        "egestion": "Getting rid of food that was never absorbed, as faeces.",
    },
    "knowledge": [
        {"kind": "card", "title": "What digestion is",
         "body": ["Food contains large molecules, such as starch, protein and fat.",
                  "They are too big to pass into the blood.",
                  "Digestion breaks them down into small molecules that dissolve.",
                  "These small, soluble molecules can be absorbed into the blood."]},
        {"kind": "card", "title": "The organs of the digestive system",
         "body": [{"figure": "b3-gut-body"},
                  "Food travels along one long tube, from the mouth to the anus.",
                  "The liver, gall bladder and pancreas sit beside the tube.",
                  "Food never passes through them. They send juices into the small intestine."]},
        {"kind": "reveal", "title": "What each organ does",
         "cols": ["What it does"],
         "rows": [
             ("Mouth", "Teeth chew food into small pieces. Saliva wets it and starts digesting starch."),
             ("Oesophagus", "A muscular tube. It squeezes food down to the stomach."),
             ("Stomach", "Churns food with acid and enzymes. Protein digestion starts here. "
                         "The acid kills most bacteria."),
             ("Small intestine", "Enzymes finish digesting the food. Small food molecules are absorbed "
                                 "into the blood here."),
             ("Large intestine", "Water is absorbed into the blood. What is left becomes faeces."),
             ("Rectum", "Stores the faeces."),
             ("Anus", "Faeces leave the body here. This is egestion."),
             ("Liver", "Makes bile."),
             ("Gall bladder", "Stores bile and releases it into the small intestine."),
             ("Pancreas", "Makes enzymes and releases them into the small intestine."),
         ]},
        {"kind": "reveal", "title": "Two kinds of digestion",
         "cols": ["Mechanical digestion", "Chemical digestion"],
         "rows": [
             ("Done by", "Teeth chewing and the stomach churning.", "Enzymes."),
             ("What changes", "Food breaks into smaller pieces. The molecules stay the same.",
              "Large molecules are broken into small molecules."),
             ("Absorbed afterwards", "No. The molecules are still too big.",
              "Yes. Small, soluble molecules can be absorbed."),
             ("Why it helps", "Smaller pieces give enzymes more surface to work on.",
              "It makes molecules small enough to pass into the blood."),
         ]},
        {"kind": "card", "title": "Peristalsis",
         "body": ["The wall of the gut is made of muscle.",
                  "The muscle squeezes behind the food, in waves. This pushes the food along.",
                  "These waves are called peristalsis.",
                  "They work even if you swallow upside down. Gravity is not needed."]},
        {"kind": "card", "title": "Bile",
         "body": ["The liver makes bile. The gall bladder stores it.",
                  "Bile flows into the small intestine.",
                  "It breaks fat into many small droplets.",
                  "This gives the fat-digesting enzyme, lipase, more surface to work on.",
                  "Bile is not an enzyme. It does not break down any molecules itself."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Digestion is only food being squashed into smaller pieces.",
              "That is mechanical digestion. Enzymes must also break large molecules into small ones.",
              "DIET-11"),
             ("Food stays in the stomach until it is digested.",
              "Food leaves the stomach only part digested. Most digestion happens in the small intestine.",
              "DIET-12"),
             ("Food passes through the liver and the pancreas.",
              "Food never passes through them. They send juices into the small intestine."),
             ("Bile is an enzyme that digests fat.",
              "Bile breaks fat into droplets. The enzyme lipase digests the fat."),
         ]}]},
    ],
    "key_fact": "Digestion breaks large food molecules into small, soluble molecules. "
                "These are absorbed into the blood, mostly in the small intestine.",
    "deeper": [
        {"kind": "card", "title": "How long food stays in each part",
         "body": [{"points": ["Mouth: about a minute.",
                              "Stomach: about 2 to 4 hours.",
                              "Small intestine: about 4 hours.",
                              "Large intestine: about a day, or more."]},
                  "Food stays longest in the large intestine. Almost all digestion is already done.",
                  "These are typical times. They vary a lot between people and meals."]},
        {"kind": "card", "title": "Egestion and excretion",
         "body": ["Egestion gets rid of food that was never absorbed. It leaves as faeces.",
                  "Excretion gets rid of waste made by your own cells.",
                  "Carbon dioxide and urea are examples of excretion."]},
    ],
    "try": None,
    "tutor_body": "Want to check you know what each organ does?",
    "ks4_becomes": "The digestive system as an organ system, with enzymes and bile in more detail.",
    "figures": [
        {"id": "b3-gut-body", "kind": "diagram", "status": "drawn", "art": "b3-gut-body",
         "title": "The organs of the digestive system",
         "desc": "An outline of a head and body. A tube runs from the mouth down the neck as the "
                 "oesophagus to the stomach, a curved bag on the right of the picture. From the "
                 "stomach a narrow tube, the small intestine, coils in the middle of the body. The "
                 "large intestine, a wider tube, runs up the left of the picture, across the top of "
                 "the coils and down the right. It ends in the rectum, a short tube in the middle at "
                 "the bottom, which opens at the anus. The liver is a large organ on the left of the "
                 "picture, with the small gall bladder under it. The pancreas is a long thin organ "
                 "under the stomach. Every organ is labelled with a line.",
         "caption": "Food passes through the mouth, oesophagus, stomach, small intestine, large intestine, "
                    "rectum and anus.",
         "data": {"labels": {
             "mouth": ["Mouth"], "oesophagus": ["Oesophagus"], "liver": ["Liver"],
             "gall_bladder": ["Gall", "bladder"], "stomach": ["Stomach"], "pancreas": ["Pancreas"],
             "small_intestine": ["Small", "intestine"], "large_intestine": ["Large", "intestine"],
             "rectum": ["Rectum"], "anus": ["Anus"]}}},
    ],
    "ladder_stem": {
        "explain": "A student says: \"Blend a meal finely enough, and you would not need a digestive "
                   "system.\" Explain what is right and what is wrong with this. Use the difference "
                   "between mechanical and chemical digestion.",
        "produce": "A person has part of their small intestine removed after an injury. Predict how "
                   "their digestion and absorption will change. Explain why the stomach cannot take "
                   "over. Name one thing that will not change.",
    },
    "ladder_ticks": [
        ["Credits what is right: blending does the job of mechanical digestion, and does it better "
         "than teeth.",
         "Says blending does the job of mechanical digestion, and does it better than teeth."],
        ["States that absorption needs small soluble molecules, and starch, protein and lipid "
         "molecules are too large.",
         "Says only small, soluble molecules are absorbed. Starch, protein and fat molecules are too big."],
        ["Says only enzymes can cut the molecules, and names at least one product — glucose, amino "
         "acids, or fatty acids.",
         "Says only enzymes break the molecules. Names a product, such as glucose or amino acids."],
        ["Explains that the stomach cannot compensate because it barely absorbs anything even when "
         "intact.",
         "Says the stomach cannot take over, as it absorbs almost nothing."],
        ["Notes that digestion may be less complete too, since enzymes have less time and less "
         "surface to act on.",
         "Says digestion may be less complete, as enzymes have less time to work."],
        ["Names something unchanged — chewing, swallowing, stomach acid, or egestion.",
         "Names something unchanged, such as chewing, swallowing or stomach acid."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "The stomach starts protein digestion. Almost nothing is absorbed there.",
            2: "Most food is digested and absorbed before it gets there. It absorbs water.",
            3: "The mouth starts digesting starch. Food is only there for about a minute.",
        },
        "apply": {
            0: "Bile has no enzymes, so it digests nothing. Lipase digests the fat.",
            2: "Lipase comes from the pancreas. Bile has no enzymes in it.",
            3: "The liver keeps making bile. Only the store of bile is lost.",
        },
    },
}
