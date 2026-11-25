# -*- coding: utf-8 -*-
"""Magnetic fields, in the lean shape. Spec table: docs/lessons/wave2/ks3-magnetic-fields.md."""

LESSON = {
    "slug": "magnetic-fields",
    "start": {
        "setup": "Iron filings are sprinkled on paper over a bar magnet. They form curved lines.",
        "question": "If you had to guess, is the magnet's pull there before the filings arrive, "
                    "or do the filings make it?",
        "options": [
            ("It is already there",
             "Yes. The field was there first. Each filing lines up with it."),
            ("The filings make it",
             "Sweep the filings away and the pull is still there. They only show it up."),
        ],
        "answer": 0,
    },
    "words": ["magnetic field", "field line", "plotting compass"],
    "word_defs": {
        "magnetic field": "The space around a magnet where a magnetic material or another magnet feels a force.",
        "field line": "A line showing which way a compass's N end points. Outside a magnet, it runs from N to S.",
        "plotting compass": "A small compass used to find the direction of a magnetic field at one point.",
    },
    "knowledge": [
        {"kind": "card", "title": "What a magnetic field is",
         "body": ["A magnet has a magnetic field around it.",
                  "The field is the space where a magnetic material or another magnet feels a force.",
                  "The field is there even when nothing is in it.",
                  "It is strongest at the poles.",
                  "Iron filings line up with the field, so they show its shape."]},
        {"kind": "card", "title": "Field lines round a bar magnet",
         "body": [{"figure": "p10-bar-field-lines"},
                  "Field lines show the shape and direction of a magnetic field.",
                  "Outside the magnet, the lines go from the north pole to the south pole.",
                  "Each line has an arrow pointing from N to S.",
                  "The lines are closest together at the poles, where the field is strongest.",
                  "Field lines never cross."]},
        {"kind": "reveal", "title": "Reading a field diagram",
         "cols": ["Rule", "Why"],
         "rows": [
             ("Direction", "N to S outside the magnet", "That is the way a compass's N end points"),
             ("Spacing", "Close lines mean a strong field", "The lines crowd together at the poles"),
             ("Crossing", "Lines never cross", "A compass can only point one way"),
             ("Gaps", "The field is still there", "The lines are only a drawing of it"),
         ]},
        {"kind": "card", "title": "Plotting a field with a compass",
         "body": [{"points": ["Put the magnet on paper and draw round it.",
                              "Put a plotting compass near the N pole.",
                              "Mark a dot where the needle's N end points.",
                              "Move the compass so its S end is over that dot. Mark again.",
                              "Keep going until you reach the S pole.",
                              "Join the dots into a smooth line, with an arrow from N to S.",
                              "Start again from other points near the N pole."]},
                  "Each dot records the direction of the field at that point."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("There is no field between the lines.",
              "The field fills all the space. The lines are only a drawing of it.", "MAG-05"),
             ("The iron filings make the field.",
              "The field is there first. The filings only show its shape.", "MAG-06"),
             ("Field lines can cross where the field is strong.",
              "Field lines never cross. A compass can only point one way.", "MAG-07"),
             ("The magnet makes extra lines at its ends.",
              "The same lines crowd closer together at the poles, where the field is strong.", "MAG-08"),
             ("Field lines go from S to N.",
              "Outside the magnet, field lines go from N to S."),
         ]}]},
    ],
    "key_fact": "A magnetic field is the space around a magnet where magnetic materials feel a force. "
                "Field lines go from the north pole to the south pole. "
                "They are closest together where the field is strongest, and they never cross.",
    "deeper": [
        {"kind": "card", "title": "Two magnets, N facing N",
         "body": [{"figure": "p10-two-magnets-nn"},
                  "The lines from each N pole turn away from the gap.",
                  "Half way between the magnets, the two fields are equal and opposite.",
                  "They cancel, so the field there is zero. This is a neutral point.",
                  "A compass there feels no pull from either magnet.",
                  "Iron filings leave a bare patch there."]},
        {"kind": "card", "title": "A field in three dimensions",
         "body": ["The field goes all the way round the magnet.",
                  "It is above and below the paper too.",
                  "Filings on paper only show one flat slice of it."]},
    ],
    "try": None,
    "tutor_body": "Stuck on which way the arrows go on a field line?",
    "ks4_becomes": "The field round a wire and a coil, and field strength.",
    "figures": [
        {"id": "p10-bar-field-lines", "kind": "diagram", "status": "drawn", "art": "p10-bar-field",
         "title": "Field lines round a bar magnet",
         "desc": "A bar magnet with N on the left and S on the right. Curved field lines leave the N "
                 "pole and loop round into the S pole, with arrows pointing from N to S. Straight lines "
                 "run out along the axis at each end, the arrows again pointing away from N and into S. "
                 "The lines are packed close at the poles and spread out at the sides. Three small "
                 "compasses sit near the lines, each needle's N end pointing along the line.",
         "caption": "Each small circle is a plotting compass. Its needle points along the field line.",
         "data": {}},
        {"id": "p10-two-magnets-nn", "kind": "diagram", "status": "drawn", "art": "p10-two-magnets",
         "title": "Two bar magnets with their N poles facing",
         "desc": "Two bar magnets end to end, their N poles facing across a gap. Field lines leave each N "
                 "pole and bend away from the gap, looping round to each magnet's own S pole or running "
                 "off the edge. A cross half way between the magnets is labelled neutral point: the two "
                 "fields cancel.",
         "caption": "No field lines pass through the neutral point.",
         "data": {}},
    ],
    "ladder_stem": {
        "explain": "Explain how you would plot the field around a bar magnet with a plotting compass "
                   "and a pencil. Say what each pencil mark records.",
        "produce": "Two bar magnets lie end to end with their N poles facing. Iron filings are scattered "
                   "over them. A small bare patch is left half way between the magnets. "
                   "Explain what is happening there. Say what a compass on that patch would do.",
    },
    "ladder_ticks": [
        ["Says a compass there would not settle to any particular direction and would stay wherever it is left.",
         "Says a compass there feels no force from either magnet."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Crowded lines mean a strong field. The field is strongest near the ends.",
            1: "The field fills all the space, between the lines too. Spacing shows strength.",
            2: "Spread out lines mean a weaker field. The sides are weaker than the ends.",
        },
        "apply": {
            1: "Strength is not the problem. A compass at a point can only point one way.",
            2: "Lines never cross anywhere, inside or outside the magnet.",
            3: "Two lines through one point would mean two directions there. That cannot happen.",
        },
    },
}
