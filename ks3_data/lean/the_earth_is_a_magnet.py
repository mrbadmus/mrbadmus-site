# -*- coding: utf-8 -*-
"""The Earth is a magnet, in the lean shape. Spec table: docs/lessons/wave2/ks3-the-earth-is-a-magnet.md."""

LESSON = {
    "slug": "the-earth-is-a-magnet",
    "start": {
        "setup": "A compass sits on a table, far from any magnet or metal. "
                 "Spin it, and it always settles pointing the same way.",
        "question": "If you had to guess, is whatever turns the needle near the surface, "
                    "or deep inside the Earth?",
        "options": [
            ("Near the surface",
             "It is deep inside. The Earth's field is made in its core, far below you."),
            ("Deep inside the Earth",
             "Yes. Moving liquid iron in the core makes a field that covers the whole Earth."),
        ],
        "answer": 1,
    },
    "words": ["compass", "true north", "magnetic north"],
    "word_defs": {
        "compass": "A small magnet that can turn freely. Its N end points north.",
        "true north": "The direction of the geographic North Pole, at the top of the Earth's spin axis.",
        "magnetic north": "The direction a compass points. It is close to true north, and it moves slowly.",
    },
    "knowledge": [
        {"kind": "card", "title": "How a compass works",
         "body": ["A compass needle is a small magnet that can turn freely.",
                  "A magnet turns until it lines up with the magnetic field around it.",
                  "Far from any other magnet, a compass still points the same way.",
                  "So the Earth must have a magnetic field.",
                  "The needle lines up with the Earth's field, so its N end points north."]},
        {"kind": "card", "title": "The Earth's magnetic field",
         "body": [{"figure": "p10-earth-field-model"},
                  "The Earth's field has the same shape as the field of a bar magnet.",
                  "It is as if a giant bar magnet were inside the Earth.",
                  "There is no real bar magnet. The core is too hot to stay magnetised.",
                  "The field is made by moving liquid iron in the Earth's core."]},
        {"kind": "card", "title": "Why the north is a south pole",
         "body": ["The N end of a compass needle points towards the Arctic.",
                  "Unlike poles attract.",
                  "So the magnetic pole near the geographic North Pole is a magnetic south pole.",
                  "That is why the magnet in the diagram has its S end at the top.",
                  "The ends of a needle were named for where they point."]},
        {"kind": "reveal", "title": "Two norths",
         "cols": ["True north", "Magnetic north"],
         "rows": [
             ("What it is", "The top of the Earth's spin axis", "Where a compass N end points"),
             ("What is there", "The geographic North Pole", "A magnetic south pole"),
             ("Moves over time", "No", "Yes, a little each year"),
         ]},
        {"kind": "card", "title": "Finding your way with a compass",
         "body": ["A map is drawn with north at the top.",
                  "A compass shows magnetic north, which is a little different.",
                  "The angle between magnetic north and true north is called the declination.",
                  "It is different in different places.",
                  "It changes as the magnetic pole moves.",
                  "So a map prints the declination and the year it was measured.",
                  "Walkers use it to correct their compass bearings."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The Earth's North Pole is a magnetic north pole.",
              "There is a magnetic south pole near it. That is why a compass N end points there.", "MAG-09"),
             ("A compass points exactly at the North Pole.",
              "It points to magnetic north, which is some way from the North Pole.", "MAG-10"),
             ("There is a bar of iron inside the Earth.",
              "Moving liquid iron in the core makes the field. There is no bar magnet.", "MAG-11"),
             ("A compass works best at the magnetic pole.",
              "It works badly there, because the field points almost straight down.", "MAG-12"),
             ("A compass needle is pulled north by gravity.",
              "The needle is a magnet. It lines up with the Earth's magnetic field."),
         ]}]},
    ],
    "key_fact": "A compass needle is a small magnet that lines up with the Earth's magnetic field. "
                "Its N end points north. "
                "So the magnetic pole near the geographic North Pole is a magnetic south pole.",
    "deeper": [
        {"kind": "card", "title": "Compasses near the poles",
         "body": ["Near a magnetic pole, the Earth's field points steeply into the ground.",
                  "A compass needle can only turn flat, so it hardly settles.",
                  "Polar pilots and explorers use satellite navigation instead."]},
        {"kind": "card", "title": "A pole on the move",
         "body": ["Magnetic north has moved more than 1000 km since 1900.",
                  "Over very long times, the Earth's field has flipped many times.",
                  "Rocks on the sea floor keep a record of these flips."]},
        {"kind": "card", "title": "Grid north",
         "body": ["A map has a third north, called grid north.",
                  "It is the way the grid lines on the map run.",
                  "It is fixed by how the map is drawn, so it does not move."]},
    ],
    "try": None,
    "tutor_body": "Confused about why magnetic north is a south pole?",
    "connects_heading": None,
    "ks4_becomes": "The Earth's field as evidence about the core, and magnetic stripes on the sea floor.",
    "figures": [
        {"id": "p10-earth-field-model", "kind": "diagram", "status": "drawn", "art": "p10-earth-field",
         "title": "The Earth's magnetic field, drawn as if a bar magnet were inside",
         "desc": "A circle for the Earth with a dashed spin axis from the North Pole at the top to the "
                 "South Pole at the bottom. A bar magnet is drawn inside, tilted a little from the axis, "
                 "with its S end at the top and its N end at the bottom. Field lines leave the ground near "
                 "the South Pole, loop round both sides and go back in near the North Pole. Arrows on "
                 "the lines point north. A compass sits on one line, its N end pointing along it to the north.",
         "caption": "The magnet's S end is under the Arctic, so the compass N end points north.",
         "data": {}},
    ],
    "ladder_stem": {
        "explain": "Explain why a compass works. Start with what the needle is. "
                   "End with what it lines up with.",
        "produce": "Pilots on polar routes are trained not to trust a magnetic compass near the magnetic pole. "
                   "Explain what goes wrong with a compass there. Suggest what they could use instead.",
    },
    "ladder_ticks": [
        ["Says the needle therefore settles slowly, or not to any useful direction at all, and directly over the pole there is no horizontal direction to find.",
         "Says the needle settles slowly or not at all. Over the pole there is no sideways direction."],
        ["Suggests something not magnetic — satellite positioning, a gyroscopic compass, or fixes from the Sun or stars.",
         "Suggests something not magnetic, such as satellite navigation, a gyrocompass, or the Sun or stars."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Its place on the map does not decide its type. Two N poles would repel.",
            1: "Like poles repel at every distance. The needle is attracted, so that pole is S.",
            3: "Gravity pulls things down, and it pulls on any object. This is a magnet lining up.",
        },
        "apply": {
            0: "A weaker field still points the same way. The direction is what has changed.",
            2: "A compass is a magnet on a pivot. Every compass points the same way.",
            3: "Grid north is fixed by how the map is drawn. It is magnetic north that moves.",
        },
    },
}
