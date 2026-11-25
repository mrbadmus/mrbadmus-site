# -*- coding: utf-8 -*-
"""Reflection: mirrors and scattering, in the lean shape.
Spec table: docs/lessons/wave2/ks3-reflection-mirrors-and-scattering.md."""

LESSON = {
    "slug": "reflection-mirrors-and-scattering",
    "start": {
        "setup": "A mirror and a sheet of white paper are held up to a window. Both make the room "
                 "brighter. Only the mirror shows you your face.",
        "question": "If you had to guess, does the mirror send back much more light than the paper?",
        "options": [
            ("No, about the same",
             "Right. A mirror reflects a little more, but paper sends back about the same amount overall."),
            ("Yes, much more",
             "White paper sends back nearly as much light. The difference is the direction it goes."),
        ],
        "answer": 0,
    },
    "words": ["normal", "law of reflection", "specular reflection", "diffuse scattering"],
    "word_defs": {
        "normal": "A line drawn at right angles to a surface, where a ray hits it.",
        "law of reflection": "The angle of reflection equals the angle of incidence, both measured from the normal.",
        "specular reflection": "Reflection from a smooth surface. Parallel rays leave still parallel, so an image forms.",
        "diffuse scattering": "Reflection from a rough surface. The rays leave in all directions, so no image forms.",
    },
    "knowledge": [
        {"kind": "card", "title": "How we see things",
         "body": ["A light source, such as the Sun or a lamp, gives out its own light.",
                  "We see a light source when its light enters our eyes.",
                  "We see most other objects because they reflect light into our eyes.",
                  "Every surface reflects some light and absorbs some light."]},
        {"kind": "card", "title": "The law of reflection",
         "body": [{"figure": "p7-reflect-law"},
                  "The normal is a line at right angles to the surface, where the ray hits.",
                  "The angle of incidence, i, is between the incoming ray and the normal.",
                  "The angle of reflection, r, is between the reflected ray and the normal.",
                  "The law of reflection: the angle of reflection equals the angle of incidence.",
                  "Always measure both angles from the normal, never from the mirror.",
                  "Draw each ray with a ruler, and an arrow to show which way it goes."]},
        {"kind": "card", "title": "Worked example: an angle from the mirror",
         "body": [{"figure": "p7-reflect-find"},
                  "A ray hits a mirror at 20° to the mirror. Find the angle of reflection.",
                  {"points": ["Convert: nothing. Both angles are in degrees.",
                              "Formula: angle of reflection = angle of incidence",
                              "Insert: angle of incidence = 90° − 20°",
                              "Fine-tune: 90 − 20 = 70, so the angle of incidence is 70°",
                              "Answer: angle of reflection = 70°"]},
                  "The 20° is measured from the mirror. The normal is at 90° to the mirror.",
                  "So take 20° away from 90° to get the angle from the normal."]},
        {"kind": "card", "title": "Smooth and rough surfaces",
         "body": [{"figure": "p7-surfaces"},
                  "A mirror is very smooth, so its normal points the same way everywhere.",
                  "Parallel rays leave it still parallel. This keeps the picture, so you see an image.",
                  "This is specular reflection.",
                  "Paper is rough. Each tiny part faces a different way and has its own normal.",
                  "Each ray still obeys the law of reflection, but the rays leave in all directions.",
                  "This is diffuse scattering. No image forms.",
                  "At GCSE this is called diffuse reflection."]},
        {"kind": "reveal", "title": "A mirror and white paper",
         "cols": ["Mirror", "White paper"],
         "rows": [
             ("Surface", "Smooth", "Rough"),
             ("The normals", "All point the same way", "Point in many directions"),
             ("Parallel rays leave", "Still parallel", "In all directions"),
             ("Image", "Yes", "No"),
             ("Law of reflection", "Obeyed by every ray", "Obeyed by every ray"),
             ("Name", "Specular reflection", "Diffuse scattering"),
         ]},
        {"kind": "card", "title": "Light that is absorbed",
         "body": ["Every surface absorbs some of the light that hits it.",
                  "The absorbed energy warms the surface slightly.",
                  "White paper reflects most of the light, so it looks bright.",
                  "Matt black card absorbs most of the light, so it looks dark.",
                  "Crumpled foil is shiny but not smooth. It reflects a lot of light but shows no clear image."]},
        {"kind": "card", "title": "Your image in a flat mirror",
         "body": ["The image is the same size as you, and the same way up.",
                  "It looks as far behind the mirror as you are in front of it.",
                  "Rays from you reflect off the mirror into your eye.",
                  "Your brain traces them straight back, to a point behind the mirror.",
                  "No light really comes from behind the mirror. It is called a virtual image."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Rough surfaces break the law of reflection.",
              "Every ray obeys the law. On a rough surface, each part has its own normal.", "LIGHT-05"),
             ("Measure the angles from the mirror.",
              "Measure both angles from the normal.", "LIGHT-06"),
             ("A mirror sends back far more light than white paper.",
              "White paper sends back nearly as much. It scatters the light in all directions.", "LIGHT-07"),
             ("Only shiny surfaces reflect light.",
              "All surfaces reflect some light. That is how we see them.", "LIGHT-08"),
             ("The angle of reflection is double the angle of incidence.",
              "The two angles are equal."),
         ]}]},
    ],
    "key_fact": "The angle of reflection equals the angle of incidence, both measured from the normal. "
                "Smooth surfaces give specular reflection and an image, while rough surfaces scatter light.",
    "deeper": [
        {"kind": "card", "title": "Mirror writing",
         "body": ["Writing looks back to front in a flat mirror.",
                  "AMBULANCE is printed back to front on the front of an ambulance.",
                  "A driver ahead sees it the right way round in their mirror."]},
        {"kind": "card", "title": "Sound reflects too",
         "body": ["Sound obeys the same law of reflection.",
                  "A reflected sound is an echo.",
                  "Soft, rough surfaces scatter and absorb sound, so rooms with curtains have fewer echoes."]},
    ],
    "try": None,
    "ks4_becomes": "Ray diagrams for mirrors, and specular and diffuse reflection at a surface.",
    "connects": {
        "Echoes, reflection and absorption": "Sound reflects from surfaces too, as an echo.",
        "Why things look coloured": "A coloured object reflects some colours and absorbs the others.",
        "Waves on water: what a wave is": "Water waves reflect from a wall in the same way.",
    },
    "figures": [
        {"id": "p7-reflect-law", "kind": "diagram", "status": "drawn", "art": "p7-reflection",
         "title": "The law of reflection",
         "desc": "A flat mirror along the bottom. A dashed line labelled normal stands at right angles "
                 "to the mirror where a ray hits it. An incoming ray comes down from the left with an "
                 "arrow and hits the mirror at the normal. A reflected ray leaves up to the right with "
                 "an arrow. The angle between the incoming ray and the normal is marked i. The angle "
                 "between the reflected ray and the normal is marked r. The key says i = 40° and r = 40°.",
         "caption": "Both angles are measured from the normal, and they are equal.",
         "data": {"i": 40, "mirror_angle": None,
                  "key": ["angle of incidence, i = 40°", "angle of reflection, r = 40°"]}},
        {"id": "p7-reflect-find", "kind": "diagram", "status": "drawn", "art": "p7-reflection",
         "title": "A ray at 20° to a mirror",
         "desc": "A flat mirror along the bottom with a dashed normal. An incoming ray comes in low "
                 "from the left and hits the mirror where the normal meets it. The angle between the "
                 "incoming ray and the mirror is marked 20°. The angles from the normal are marked i "
                 "and r. The key says: angle to the mirror = 20°, i = ?, r = ?.",
         "caption": "Find i and r. Both are measured from the normal.",
         "data": {"i": 70, "mirror_angle": "20°",
                  "key": ["angle to the mirror = 20°", "angle of incidence, i = ?",
                          "angle of reflection, r = ?"]}},
        {"id": "p7-surfaces", "kind": "diagram", "status": "drawn", "art": "p7-surfaces",
         "title": "Specular reflection and diffuse scattering",
         "desc": "Two panels. Top, a smooth surface: three parallel rays come in from the left and "
                 "leave to the right, still parallel. Bottom, a rough surface made of tilted pieces, "
                 "each with its own dashed normal: three parallel rays come in from the left, and "
                 "each leaves in a different direction.",
         "caption": "Each ray obeys the law of reflection on both surfaces.",
         "data": {}},
    ],
    "figure_caption": {"p7-reflect-find": None},   # the card text already says it
    "ladder_feedback": {
        "recall": {
            1: "The 25° is measured from the mirror. From the normal it is 90° − 25° = 65°.",
            2: "There is no doubling. The angle of reflection equals the angle of incidence, 65°.",
            3: "Take the 25° away from 90°. The angle of incidence is 65°.",
        },
        "apply": {
            0: "Every ray obeys the law of reflection. Each part of the paper has its own normal.",
            2: "White paper reflects most of the light. That is why it looks so bright.",
            3: "All surfaces reflect some light. Crumpled foil is shiny but shows no image.",
        },
    },
}
