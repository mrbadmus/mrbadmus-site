# -*- coding: utf-8 -*-
"""Electric fields, in the lean shape. Spec table: docs/lessons/wave2/ks3-electric-fields.md."""

LESSON = {
    "slug": "electric-fields",
    "start": {
        "setup": "A comb pulled through dry hair is held near a thin stream of tap water. "
                 "The stream bends towards the comb without touching it.",
        "question": "If you had to guess, does the comb need the air between it and the water to bend the stream?",
        "options": [
            ("Yes, it needs air",
             "No. The comb's field acts across the gap. It does not need air."),
            ("No, it does not",
             "Right. The comb's electric field fills the space, with or without air."),
        ],
        "answer": 1,
    },
    "words": ["electric field", "non-contact force", "field arrow"],
    "word_defs": {
        "electric field": "The space around a charged object, where another charge feels a force.",
        "non-contact force": "A force that acts between objects that are not touching.",
        "field arrow": "An arrow showing which way a small positive charge would be pushed at that point.",
    },
    "knowledge": [
        {"kind": "card", "title": "What an electric field is",
         "body": ["A charged object has an electric field around it.",
                  "The field is the space where another charged object feels a force.",
                  "The field is there even when nothing is in it.",
                  "Put a charged object in the field, and it is pushed or pulled straight away."]},
        {"kind": "card", "title": "Forces across a gap",
         "body": ["The field is how a force acts across the space between objects.",
                  "So charged objects push and pull without touching.",
                  "Nothing has to travel across the gap, and no air is needed.",
                  "It works just the same in a vacuum."]},
        {"kind": "card", "title": "Drawing the field",
         "body": [{"figure": "p9-field-arrows-two"},
                  "Arrows show the field. Each one shows the push on a small positive charge.",
                  "Around a positive charge, the arrows point away from it.",
                  "Around a negative charge, the arrows point towards it.",
                  "The field is strongest close to the charge.",
                  "A negative charge is pushed the opposite way to the arrows."]},
        {"kind": "card", "title": "Between two like charges",
         "body": [{"figure": "p9-field-cancel-mid"},
                  "Half way between two equal positive charges, a test charge is pushed both ways.",
                  "The two pushes are equal and opposite, so they cancel.",
                  "So the field at that one point is zero.",
                  "Move a little closer to one charge, and that charge's push wins."]},
        {"kind": "reveal", "title": "Three forces that act at a distance",
         "cols": ["Made by", "Acts on"],
         "rows": [
             ("Gravity", "Anything with mass", "Anything with mass"),
             ("Magnetism", "A magnet or a current", "Magnets and magnetic materials"),
             ("Static electricity", "A charged object", "Charged objects, and neutral ones by induction"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A field only exists when something is in it.",
              "The field is there all the time, even with nothing in it.", "CHRG-09"),
             ("The air in the gap carries the force.",
              "The field carries the force. It works the same in a vacuum.", "CHRG-10"),
             ("The field is strongest half way between two like charges.",
              "Half way between two equal like charges, the field is zero.", "CHRG-11"),
             ("A negative charge is pushed along the field arrows.",
              "A negative charge is pushed the opposite way to the arrows.", "CHRG-12"),
             ("A field arrow shows the push on a negative charge.",
              "A field arrow shows the push on a small positive charge."),
         ]}]},
    ],
    "key_fact": "A charged object has an electric field around it. "
                "Any other charged object in that field feels a force. "
                "So the force acts across the gap, without the objects touching.",
    "deeper": [
        {"kind": "card", "title": "Bending water",
         "body": ["A charged comb bends a thin stream of tap water.",
                  "The comb's field acts on the water from a few centimetres away.",
                  "Nothing touches the water, and no air is needed."]},
        {"kind": "card", "title": "Safe inside a car",
         "body": ["A car's metal body is a conductor.",
                  "If lightning strikes, the charge flows round the outside of the metal.",
                  "The field inside the car is almost zero, so the people inside are safe.",
                  "The metal body protects you. The rubber tyres do not."]},
    ],
    "try": None,
    "tutor_body": "Got two charges and want to know which way the field points?",
    "ks4_becomes": "Field lines round charged objects, and field strength.",
    "safety_note": "Only a car with a metal roof and metal sides protects you. "
                   "Never shelter under a tree in a storm. Get indoors or into a car.",
    "figures": [
        {"id": "p9-field-arrows-two", "kind": "diagram", "status": "drawn", "art": "p9-field-arrows",
         "title": "Field arrows round a positive charge and a negative charge",
         "desc": "Two charged balls side by side. Eight arrows round the positive ball all point away "
                 "from it, labelled arrows point away. Eight arrows round the negative ball all point "
                 "towards it, labelled arrows point in.",
         "caption": "Each arrow shows the push on a small positive charge at that point.",
         "data": {}},
        {"id": "p9-field-cancel-mid", "kind": "diagram", "status": "drawn", "art": "p9-field-cancel",
         "title": "A test charge half way between two equal positive charges",
         "desc": "Two positive balls far apart, with a small positive test charge exactly half way "
                 "between them. One arrow of the same length points from the test charge towards "
                 "each side, away from each big charge. Labels say the two equal pushes cancel, so "
                 "the field there is zero.",
         "caption": "Each big charge pushes the test charge away from itself.",
         "data": {}},
    ],
    "ladder_stem": {
        "explain": "A comb is charged by rubbing it on a jumper. It is held 1 cm above small pieces of paper. "
                   "They jump up to it without being touched. Explain what is happening, using the word field. "
                   "Say what would change if this were done in a vacuum.",
        "produce": "People are safe from lightning inside a car, and the rubber tyres are not the reason. "
                   "Explain why, using the idea of a field and what you know about conductors.",
    },
    "ladder_ticks": [
        ["Says the tyres are irrelevant — the protection is the metal shell surrounding you, not an insulating layer underneath.",
         "Says the tyres do not protect you. The metal shell around you does."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Arrows point away from a positive charge. So the object is positive.",
            1: "The object is positive. But a negative charge is pushed against the arrows.",
            3: "The direction tells you the sign. Away means positive, towards means negative.",
        },
        "apply": {
            0: "Closeness matters, but so does direction. The two pushes cancel there.",
            2: "It is zero only at the middle point. Move a little and the nearer charge wins.",
            3: "The pushes add as arrows. Two equal pushes the opposite way add to zero.",
        },
    },
}
