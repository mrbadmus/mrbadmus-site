# -*- coding: utf-8 -*-
"""Forces between charges, in the lean shape. Spec table: docs/lessons/wave2/ks3-forces-between-charges.md."""

LESSON = {
    "slug": "forces-between-charges",
    "start": {
        "setup": "A balloon rubbed on a jumper sticks to a wall. Nobody has charged the wall.",
        "question": "If you had to guess, does the wall have a charge of its own?",
        "options": [
            ("Yes, it has a charge",
             "No. The wall is neutral. The balloon shifts the wall's own electrons."),
            ("No, it has none",
             "Right. The wall has no overall charge. Its electrons shift a little, leaving the surface slightly positive."),
        ],
        "answer": 1,
    },
    "words": ["repel", "attract", "induction", "non-contact force"],
    "word_defs": {
        "repel": "To push apart. Two like charges repel each other.",
        "attract": "To pull together. Two unlike charges attract each other.",
        "induction": "A charged object shifting a neutral object's electrons, so the near side is oppositely charged.",
        "non-contact force": "A force that acts between objects that are not touching.",
    },
    "knowledge": [
        {"kind": "card", "title": "Like and unlike charges",
         "body": [{"figure": "p9-pairs-three"},
                  "Charged objects push or pull on each other.",
                  "Like charges repel. Two positives push apart. Two negatives push apart.",
                  "Unlike charges attract. A positive and a negative pull together.",
                  "The two forces are always equal in size and opposite in direction."]},
        {"kind": "card", "title": "A force without touching",
         "body": ["Charged objects do not need to touch to push or pull.",
                  "The force acts across the gap between them.",
                  "So the force between charges is a non-contact force.",
                  "Gravity and the force between magnets are non-contact forces too.",
                  "It works just the same with all the air pumped out."]},
        {"kind": "card", "title": "Closer means stronger",
         "body": ["The force gets weaker quickly as the objects move apart.",
                  "Double the distance, and the force falls to about a quarter.",
                  "That is why static only has an effect when things are close."]},
        {"kind": "card", "title": "Attracting a neutral object",
         "body": [{"figure": "p9-induction-wall"},
                  "A charged object also attracts a neutral object.",
                  "A negative balloon pushes the wall's electrons a little way back.",
                  "The wall's surface is left slightly positive, so it attracts the balloon.",
                  "The wall is still neutral overall. Nothing has been added or taken away.",
                  "This is called induction.",
                  "It is why a rubbed comb picks up small bits of paper."]},
        {"kind": "reveal", "title": "What two objects do",
         "cols": ["What happens", "Why"],
         "rows": [
             ("Positive and positive", "Repel", "Like charges"),
             ("Negative and negative", "Repel", "Like charges"),
             ("Positive and negative", "Attract", "Unlike charges"),
             ("Charged and neutral", "Attract", "Induction"),
             ("Neutral and neutral", "Nothing", "No charge to act"),
         ]},
        {"kind": "card", "title": "The test for charge",
         "body": ["Attraction does not prove an object is charged.",
                  "A charged rod attracts an opposite charge and a neutral object.",
                  "Repulsion is the only proof. Only a charged object can be repelled.",
                  "If it is repelled, it has the same charge as your rod."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The rod picks up the paper, so the paper must be charged.",
              "The paper is neutral. The rod attracts it by induction.", "CHRG-05"),
             ("Charges must touch, or the air must carry the force.",
              "The force acts across the gap, even with no air there.", "CHRG-06"),
             ("Double the distance and the force halves.",
              "Double the distance and the force falls to about a quarter.", "CHRG-07"),
             ("A charged object does nothing to a neutral one.",
              "It attracts it, by shifting the neutral object's electrons.", "CHRG-08"),
             ("The smaller object feels the bigger force.",
              "Both objects feel forces of the same size."),
         ]}]},
    ],
    "key_fact": "Like charges repel and unlike charges attract. "
                "A charged object also attracts a neutral object, by induction. "
                "The force acts without touching, and it gets weaker quickly with distance.",
    "deeper": [
        {"kind": "card", "title": "Hair standing on end",
         "body": ["Rub your hair with a balloon and each hair loses electrons.",
                  "Every hair is now positive.",
                  "Like charges repel, so the hairs push away from each other."]},
        {"kind": "card", "title": "Spray painting",
         "body": ["A paint sprayer gives the paint drops a charge.",
                  "The car being painted is given the opposite charge.",
                  "Unlike charges attract, so the paint is pulled on evenly.",
                  "Like charges repel, so the drops spread out into a fine mist."]},
    ],
    "try": None,
    "tutor_body": "Got two objects and want to know whether they attract, repel or do nothing?",
    "ks4_becomes": "Electric fields, and how the force between charges depends on distance.",
    "figures": [
        {"id": "p9-pairs-three", "kind": "diagram", "status": "drawn", "art": "p9-pairs",
         "title": "Three pairs of charges and the forces on them",
         "desc": "Three rows, each with two charged balls. Two positive balls each have an arrow "
                 "pointing away from the other, labelled like charges repel. Two negative balls do "
                 "the same. A positive ball and a negative ball each have an arrow pointing towards "
                 "the other, labelled unlike charges attract. The arrows in each row are equal.",
         "caption": "The arrows show the force on each ball.",
         "data": {"rows": [["+", "+"], ["-", "-"], ["+", "-"]]}},
        {"id": "p9-induction-wall", "kind": "diagram", "status": "drawn", "art": "p9-induction",
         "title": "A charged balloon held near a wall",
         "desc": "A balloon covered in minus signs hangs on a string near a wall. In the wall, a "
                 "column of plus signs sits at the surface facing the balloon, and a column of minus "
                 "signs sits a little further in. Labels say the electrons are pushed a little way "
                 "back. An arrow from the balloon towards the wall is labelled pulled in.",
         "caption": "The wall's electrons move a little way back. The surface is left slightly positive.",
         "data": {}},
    ],
    "figure_caption": {"p9-pairs-three": None},
    "ladder_stem": {
        "explain": "A balloon rubbed on a jumper sticks to a wall. Nobody has charged the wall. "
                   "Explain how a charged object can be attracted to an uncharged one.",
        "produce": "You have two hanging balls. You know that one of them is charged. "
                   "Describe how you would find out whether the other is charged too. "
                   "Explain why one possible result would tell you nothing.",
    },
    "ladder_feedback": {
        "recall": {
            0: "A neutral ball is attracted too, by induction. So it could be either.",
            2: "An oppositely charged ball is pulled in too. So it could be either.",
            3: "Two negatives repel. A negative ball is the one thing this rules out.",
        },
        "apply": {
            0: "The force falls faster than that. Double the distance gives about a quarter.",
            1: "The charges are the same, but the force also depends on the distance.",
            2: "The forces on the two spheres are always equal. Both fall to about a quarter.",
        },
    },
}
