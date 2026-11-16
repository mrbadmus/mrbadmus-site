# -*- coding: utf-8 -*-
"""Magnetic fields, in the lean shape. New record, no legacy page.
Spec table: ks4-magnetic-fields.md (AQA 8464 6.7.1.2 / 8463 4.7.1.2)."""

LESSON = {
    "slug": "magnetic-fields",
    "start": {
        "setup": "You stand outside, far from any magnet, holding a compass.",
        "question": "If you had to guess, what does the compass needle do?",
        "options": [
            ("It points in one direction",
             "It points in one direction. The Earth has a magnetic field, and the needle lines up "
             "with it."),
            ("It stops anywhere it likes",
             "It points in one direction. The Earth has a magnetic field, and the needle lines up "
             "with it."),
        ],
        "answer": 0,
    },
    "words": ["magnetic field", "magnetic material", "field line", "compass"],
    "knowledge": [
        {"kind": "card", "title": "What a magnetic field is",
         "body": ["The magnetic field is the region around a magnet where a force acts on another "
                  "magnet or on a magnetic material.",
                  "The magnetic materials are iron, steel, cobalt and nickel.",
                  "The force between a magnet and a magnetic material is always one of attraction.",
                  "In the field, the magnetic material becomes an induced magnet. When it is "
                  "removed from the field, it loses most or all of its magnetism quickly."]},
        {"kind": "card", "title": "How strong the field is",
         "body": ["The strength of the magnetic field depends on the distance from the magnet.",
                  "The further you are from the magnet, the weaker the field.",
                  "The field is strongest at the poles of the magnet."]},
        {"kind": "card", "title": "Which way the field points",
         "body": ["The direction of the magnetic field at any point is given by the direction of "
                  "the force that would act on another north pole placed at that point.",
                  "So the direction of a magnetic field line is from the north (seeking) pole of "
                  "a magnet to the south (seeking) pole of the magnet."]},
        {"kind": "card", "title": "Drawing the field of a bar magnet",
         "body": ["Look at where the lines are closest together.",
                  {"slot": "fig:bar-magnet-field"},
                  {"points": [
                      "Draw the lines going from the north pole to the south pole, with an arrow "
                      "on each line.",
                      "Draw the lines closest together at the poles, where the field is strongest.",
                      "Draw the lines further apart further from the magnet, where the field is "
                      "weaker.",
                      "Field lines never cross.",
                  ]}]},
        {"kind": "card", "title": "Plotting the field with a compass",
         "body": ["A plotting compass needle points in the direction of the field where it sits.",
                  {"points": [
                      "1. Put the bar magnet on a sheet of paper and draw round it.",
                      "2. Put a plotting compass next to the north pole of the magnet.",
                      "3. Mark a dot just beyond the north end of the compass needle.",
                      "4. Move the compass so the tail of the needle is on the dot. Mark a new dot "
                      "beyond the north end of the needle.",
                      "5. Repeat until you reach the south pole. Join the dots with a smooth line "
                      "and add an arrow from N to S.",
                      "6. Start again from a different point next to the magnet to plot more lines.",
                  ]},
                  {"slot": "fig:compass-plotting"}]},
        {"kind": "card", "title": "The compass and the Earth",
         "body": ["A magnetic compass contains a small bar magnet.",
                  "The Earth has a magnetic field. The compass needle points in the direction of "
                  "the Earth's magnetic field.",
                  "Look at the compass on the Earth's surface.",
                  {"slot": "fig:earth-field"}]},
        {"kind": "card", "title": "Evidence that the Earth's core is magnetic",
         "body": [{"points": [
             "Far from any magnet, a compass needle still turns to point in one direction.",
             "The needle is a small magnet, so a magnetic field must be acting on it.",
             "So the Earth must have a magnetic field.",
             "Something inside the Earth must be magnetic to produce this field. This is evidence "
             "that the core of the Earth must be magnetic.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Field lines go from south to north outside a magnet.",
              "A magnetic field line goes from the north pole to the south pole."),
             ("The field is strongest in the middle of the magnet.",
              "The field is strongest at the poles."),
             ("A magnet can attract or repel a magnetic material.",
              "The force between a magnet and a magnetic material is always one of attraction."),
             ("All metals are magnetic.",
              "The magnetic materials are iron, steel, cobalt and nickel. Copper and aluminium "
              "are not."),
         ]}]},
    ],
    "key_fact": "A magnetic field is the region around a magnet where a force acts on another "
                "magnet or on a magnetic material (iron, steel, cobalt and nickel). Field lines go "
                "from the north pole to the south pole and are closest together at the poles, "
                "where the field is strongest.",
    "deeper": [
        {"kind": "card", "title": "Why the north pole is called north seeking",
         "body": ["The north pole of a compass needle points roughly towards the Earth's "
                  "geographic North Pole. It seeks the north.",
                  "Unlike poles attract. So the Earth's magnetic pole near the geographic North "
                  "Pole is a south pole."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe how to</strong>: give the steps in order, so someone else could "
             "follow them.",
             "<strong>Draw</strong>: field lines with arrows from N to S, closest together at "
             "the poles.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Which of these is a magnetic material?",
             "why": "The magnetic materials are iron, steel, cobalt and nickel.",
             "options": [
                 {"text": "Copper", "correct": False, "reply": "Copper is not a magnetic material."},
                 {"text": "Nickel", "correct": True},
                 {"text": "Aluminium", "correct": False,
                  "reply": "Aluminium is not a magnetic material."},
                 {"text": "Glass", "correct": False, "reply": "Glass is not a magnetic material."},
             ]},
            {"kind": "mcq", "command": "Complete", "marks": 1,
             "prompt": "The direction of the magnetic field at any point is the direction of the "
                       "force that would act on…",
             "why": "AQA's wording: the force that would act on another north pole placed at "
                    "that point.",
             "options": [
                 {"text": "another south pole placed at that point", "correct": False,
                  "reply": "The direction is defined using a north pole."},
                 {"text": "another north pole placed at that point", "correct": True},
                 {"text": "a piece of iron placed at that point", "correct": False,
                  "reply": "Iron is always attracted, towards either pole, so it cannot show the "
                           "direction."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "Describe how the strength and direction of the magnetic field change from "
                       "point to point around a bar magnet.",
             "why": "The field is strongest at the poles and weaker further away. Its direction is "
                    "from the north pole to the south pole.",
             "options": [
                 {"text": "Strongest at the poles and weaker further away. It points from north to "
                          "south.", "correct": True},
                 {"text": "Strongest in the middle and weaker at the poles. It points from south to "
                          "north.", "correct": False,
                  "reply": "The field is strongest at the poles. It points from north to south."},
                 {"text": "The same strength everywhere. It points from north to south.",
                  "correct": False,
                  "reply": "The strength depends on the distance from the magnet."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A steel paper clip is held near the north pole of a bar magnet, then near "
                       "the south pole. Explain what happens each time.",
             "why": "Steel is a magnetic material, so it becomes an induced magnet. The force "
                    "between a magnet and a magnetic material is always one of attraction.",
             "options": [
                 {"text": "Attracted to the north pole, repelled by the south pole",
                  "correct": False,
                  "reply": "A magnetic material is never repelled by a magnet."},
                 {"text": "Repelled both times, because it becomes an induced magnet",
                  "correct": False,
                  "reply": "The force on a magnetic material is always attraction."},
                 {"text": "Attracted both times, because it becomes an induced magnet",
                  "correct": True},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how the behaviour of a compass is evidence that the core of the "
                       "Earth must be magnetic. Put the links in order.",
             "links": ["The compass needle is a small magnet, and far from any other magnet it "
                       "still points in one direction.",
                       "So a magnetic field must be acting on the needle. This is the Earth's "
                       "magnetic field.",
                       "Something inside the Earth must be magnetic to produce this field, so the "
                       "core of the Earth must be magnetic."],
             "herrings": [{"text": "The needle has an electric charge, so the Earth attracts it.",
                           "why": "The needle is a magnet. Only a magnetic field turns it."},
                          {"text": "Gravity pulls the north end of the needle towards the North "
                                   "Pole.",
                           "why": "Gravity pulls down, towards the centre of the Earth. It does "
                                  "not turn the needle."}]},
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how to plot one field line of a bar magnet using a plotting "
                       "compass. Put the links in order.",
             "links": ["Put a plotting compass next to the north pole of the magnet and mark a dot "
                       "beyond the north end of the needle.",
                       "Move the compass so the tail of the needle is on the dot, then mark a new "
                       "dot beyond the north end of the needle.",
                       "Repeat until you reach the south pole, then join the dots with a smooth "
                       "line and add an arrow from N to S."],
             "herrings": [{"text": "Keep the compass still and move the magnet each time.",
                           "why": "The magnet stays still. You move the compass along the line."},
                          {"text": "Draw the arrow on the line from the south pole to the north "
                                   "pole.",
                           "why": "A magnetic field line goes from the north pole to the south "
                                  "pole."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 6,
             "prompt": "Describe how to plot the magnetic field pattern of a bar magnet using a "
                       "plotting compass. Say how your finished pattern shows the strength and "
                       "the direction of the field.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "A clear method in a logical order that "
                  "would plot several field lines, and says how the pattern shows both the "
                  "direction and the strength of the field.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "A method that would plot at least one field "
                  "line, with some steps missing or out of order, or with no link to strength or "
                  "direction.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant steps, or one correct "
                  "statement about the pattern.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Put the magnet on a sheet of paper and draw round it.",
                        "Put a plotting compass next to the north pole of the magnet.",
                        "Mark a dot beyond the north end of the compass needle.",
                        "Move the compass so the tail of the needle is on the dot, and mark the "
                        "next dot.",
                        "Repeat until you reach the south pole, then join the dots with a smooth "
                        "line.",
                        "Start from other points next to the magnet to plot more lines.",
                        "Arrows on the lines from N to S show the direction of the field.",
                        "The lines are closest together at the poles, where the field is "
                        "strongest, and further apart where it is weaker."],
             "reject": ["“Draw the arrows from the south pole to the north pole.”",
                        "“The lines are furthest apart at the poles because the field is "
                        "strongest there.”"]},
        ],
    },
}
