# -*- coding: utf-8 -*-
"""How we worked out DNA's structure, in the lean shape. Spec table: docs/lessons/wave2/ks3-how-we-worked-out-dna.md."""

LESSON = {
    "slug": "how-we-worked-out-dna",
    "start": {
        "setup": None,
        "question": "If you had to guess, was the shape of DNA worked out by one brilliant person, "
                    "or by several teams?",
        "options": [
            ("One brilliant person",
             "Several teams. X-ray images, chemical measurements and model building all had to fit."),
            ("Several teams together",
             "Yes. X-ray images from London, chemical data from New York and models from Cambridge."),
        ],
        "answer": 1,
    },
    "words": ["double helix", "X-ray diffraction", "base pairing", "model"],
    "word_defs": {
        "double helix": "Two strands twisted round each other in a spiral. It is the shape of DNA.",
        "X-ray diffraction": "Firing X-rays at a substance and studying the pattern they scatter into.",
        "base pairing": "In DNA, A always pairs with T, and C always pairs with G.",
        "model": "A way of showing how something works, tested against evidence.",
    },
    "knowledge": [
        {"kind": "card", "title": "Too small to see",
         "body": ["A DNA molecule is far too thin to see with a light microscope.",
                  "In the early 1950s, scientists used other evidence to work out its shape.",
                  "In 1953, the double helix model was published.",
                  "It needed work from four scientists in two labs, plus a chemist in New York."]},
        {"kind": "reveal", "title": "Who did what",
         "cols": ["Where", "What they did"],
         "rows": [
             ("Rosalind Franklin", "King's College London",
              "Took X-ray images of DNA, including Photo 51. Her measurements showed DNA is a helix."),
             ("Maurice Wilkins", "King's College London",
              "Began the X-ray work on DNA at King's. He showed Photo 51 to Watson."),
             ("James Watson and Francis Crick", "Cambridge University",
              "Built models to fit all the evidence. They published the double helix in 1953."),
             ("Erwin Chargaff", "Columbia University, New York",
              "Measured the amounts of the four bases in DNA. A equals T, and C equals G."),
         ]},
        {"kind": "card", "title": "Franklin's X-ray evidence",
         "body": ["X-rays scatter off the atoms in DNA and make a pattern of spots.",
                  "Franklin and her student Raymond Gosling took the clearest image, Photo 51.",
                  "Its pattern of spots is the sign of a helix.",
                  "The spacing of the spots gave the width of the molecule.",
                  "Her measurements helped show there were two strands.",
                  "Her measurements also showed the backbones are on the outside. The bases are inside."]},
        {"kind": "card", "title": "Chargaff's ratios",
         "body": ["Chargaff measured the amounts of the four bases in DNA.",
                  "In every species, the amount of A equals the amount of T.",
                  "The amount of C equals the amount of G.",
                  "This fits if A always pairs with T, and C always pairs with G.",
                  {"figure": "b10-base-ladder"},
                  "Each pair is one big base and one small base. So every rung is the same width."]},
        {"kind": "card", "title": "Building the model",
         "body": ["Watson and Crick did no experiments on DNA themselves.",
                  "They built models out of metal and card.",
                  "They tested each model against the evidence from London and New York.",
                  "One model fitted it all: two strands, bases inside, A with T, C with G.",
                  "Other models did not fit. Linus Pauling's model had three strands."]},
        {"kind": "card", "title": "Giving credit",
         "body": ["In January 1953, Wilkins showed Photo 51 to Watson.",
                  "Franklin had not yet published it.",
                  "Crick also saw a report that included Franklin's measurements.",
                  "Their 1953 paper only said they were \"stimulated by\" the King's results.",
                  "Franklin's own paper was printed in the same issue of the journal.",
                  "In 1962, Watson, Crick and Wilkins won the Nobel Prize.",
                  "Franklin had died in 1958. The prize is not given after death.",
                  "Today, scientists must credit the people whose data they use."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Watson and Crick discovered DNA.",
              "DNA was found in 1869. Watson and Crick worked out its shape in 1953.", "GENE-05"),
             ("A great discovery is one person's flash of insight.",
              "The double helix needed evidence from several scientists in different labs.", "NOS-03"),
             ("Photo 51 is a photograph of a DNA molecule.",
              "It is a pattern of scattered X-rays. The shape was worked out from it."),
             ("Watson and Crick took the X-ray images.",
              "Franklin and Gosling took Photo 51 at King's College London."),
         ]}]},
    ],
    "key_fact": "DNA is a double helix of two twisted strands. A pairs with T, and C pairs with G. "
                "Franklin and Wilkins provided the X-ray evidence. "
                "Watson and Crick used it to build the model in 1953.",
    "deeper": [
        {"kind": "card", "title": "Why the shape mattered",
         "body": ["A always pairs with T, and C always pairs with G.",
                  "So each strand holds all the information.",
                  "Unzip the two strands, and each one can be used to build a new partner.",
                  "The shape showed how DNA could be copied."]},
        {"kind": "card", "title": "DNA was known long before",
         "body": ["Friedrich Miescher found DNA in 1869.",
                  "In 1944, Oswald Avery's team showed that DNA carries genetic information.",
                  "Its shape was the part still unknown in 1953."]},
    ],
    "try": None,
    "tutor_body": "Want to talk through what each scientist added to the DNA model?",
    "ks4_becomes": "The structure of DNA in more detail, and how scientific ideas are tested and shared.",
    "figures": [
        {"id": "b10-base-ladder", "kind": "diagram", "status": "drawn", "art": "b10-base-ladder",
         "title": "How the bases pair across the two strands of DNA, and the same ladder twisted",
         "desc": "Two backbones run down the sides, labelled backbone, with five rungs between them. "
                 "Each rung is one base from the left and one from the right. From the top, the rungs are "
                 "A with T, T with A and C with G. Then come G with C, and A with T. A and G are drawn wide. C and T are drawn "
                 "narrow. A line measures across the first rung and another across the last. They are the "
                 "same length, labelled every rung the same width. Below, the same ladder is twisted into "
                 "a double helix. Two dashed lines mark its widest points. A third line measures across "
                 "them, labelled still the same width. A key says A and G are the big bases. "
                 "C and T are the small bases.",
         "caption": "A big base always pairs with a small one.",
         "data": {"rungs": [["A", "T"], ["T", "A"], ["C", "G"], ["G", "C"], ["A", "T"]],
                  "guide_label": "every rung the same width"}},
    ],
    # The lesson's own "A note on the credit" (the lesson file's `support` layer) is cut on the
    # lean page: the Giving credit card already says every settled fact in it, and the note's
    # claim about the cause of Franklin's cancer is contested. lean.apply() reads this key.
    "support": [],
    "figure_caption": {"b10-base-ladder": None},
    "ladder_stem": {
        "explain": "The DNA model has two strands, bases on the inside, and A paired with T. "
                   "For each feature, say which evidence showed it, and how.",
        "produce": "The 1953 paper only said the authors were \"stimulated by\" unpublished results from "
                   "King's College. Write what a fair acknowledgement would have said. Then give a rule "
                   "about using other people's data.",
    },
    "ladder_ticks": [
        ["Links the two strands to the X-ray diffraction pattern, and says the spacing gave the width.",
         "Links two strands to Franklin's X-ray measurements."],
        ["Links the bases being on the inside to Franklin’s water measurements and the phosphates being outside.",
         "Links bases inside to Franklin's measurements showing the backbones are outside."],
        ["Explains why equal amounts of A and T in every species implies they must pair with each other.",
         "Explains that equal amounts of A and T suggest they pair together."],
        ["Names Franklin specifically, and what her contribution was — the diffraction images and the measurements taken from them.",
         "Names Franklin and her contribution: the X-ray images and her measurements."],
        ["Recognises that Watson and Crick’s own contribution — assembling a model that fitted everything — was real and worth credit too.",
         "Says Watson and Crick's model building was real work that also deserves credit."],
        ["States a general rule, such as: data should be credited to whoever produced it, and used only with their knowledge.",
         "States a rule: credit data to whoever produced it, and use it only with permission."],
        ["Avoids treating the episode as a simple story of heroes and villains — acknowledges that the history is contested or that several factors were involved.",
         "Treats it fairly, with no heroes or villains, as several people played a part."],
        ["Says the cross-shaped pattern in the image showed the molecule was a helix.",
         "Says the pattern of spots in Photo 51 showed DNA is a helix."],
        ["Notes that the data was seen without her knowledge or permission.",
         "Notes that her results were used before she had published them."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "The helix came from Franklin's X-ray pattern. Chargaff measured amounts of bases.",
            1: "The number of strands came from the X-ray measurements of width.",
            2: "The backbones being outside came from Franklin's measurements.",
        },
        "apply": {
            1: "DNA was found in 1869, by Friedrich Miescher.",
            2: "Avery's team showed that in 1944, before the model was built.",
            3: "Franklin and Gosling took the X-ray images at King's College London.",
        },
    },
}
