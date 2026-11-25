# -*- coding: utf-8 -*-
"""Refraction, in the lean shape. Spec table: docs/lessons/wave2/ks3-refraction.md."""

LESSON = {
    "slug": "refraction",
    "start": {
        "setup": "A straw stands in a glass of water. Seen from above at a slant, it looks bent at "
                 "the water surface.",
        "question": "If you had to guess, what really bends: the straw, or the light coming from it?",
        "options": [
            ("The straw itself",
             "Lift the straw out and it is straight. The light from it bends at the water surface."),
            ("The light from it",
             "Right. Light from the straw changes direction as it leaves the water."),
        ],
        "answer": 1,
    },
    "words": ["refraction", "normal", "boundary"],
    "word_defs": {
        "refraction": "The change in direction of light as it crosses from one material into another.",
        "normal": "A line drawn at right angles to a surface, where a ray meets it.",
        "boundary": "The surface where two materials meet, such as air and glass.",
    },
    "knowledge": [
        {"kind": "card", "title": "Light changes speed",
         "body": ["Light travels fastest in a vacuum, and almost as fast in air.",
                  "It slows down when it goes into water, perspex or glass.",
                  "In glass, light travels at about two thirds of its speed in air.",
                  "It speeds up again when it comes back out into the air."]},
        {"kind": "card", "title": "Refraction",
         "body": [{"figure": "p7-block-angle"},
                  "Crossing a boundary at an angle, light changes speed and so changes direction.",
                  "This is refraction.",
                  "Going into glass, light slows down and bends towards the normal.",
                  "Coming out into air, light speeds up and bends away from the normal.",
                  "A block with parallel sides sends the ray out in its starting direction, shifted sideways."]},
        {"kind": "card", "title": "Along the normal",
         "body": [{"figure": "p7-block-straight"},
                  "A ray that meets the boundary along the normal does not bend.",
                  "It still slows down inside the glass.",
                  "So light can change speed without changing direction."]},
        {"kind": "reveal", "title": "Reflection and refraction",
         "cols": ["Reflection", "Refraction"],
         "rows": [
             ("What the light does", "Bounces off the surface", "Passes into the new material"),
             ("Its speed", "Stays the same", "Changes"),
             ("Its direction", "Leaves at the same angle it arrived", "Bends towards or away from the normal"),
             ("Where it ends up", "Back in the first material", "In the second material"),
             ("An example", "Seeing yourself in a mirror", "A straw looking bent in water"),
         ]},
        {"kind": "card", "title": "Why the straw looks bent",
         "body": [{"figure": "p7-straw"},
                  "Light from the bottom of the straw travels up through the water.",
                  "At the surface, it speeds up and bends away from the normal.",
                  "Your brain assumes that light has come in a straight line.",
                  "So it traces the ray straight back, to a point higher than the real end.",
                  "The straw is straight. The light from it is what bent."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The straw really bends in water.",
              "The straw stays straight. The light from it bends at the surface.", "LIGHT-09"),
             ("Water is thicker, so it pushes light sideways.",
              "Nothing pushes the light. It bends because its speed changes.", "LIGHT-10"),
             ("Light speeds up when it goes into glass.",
              "Light slows down in glass. It is fastest in a vacuum.", "LIGHT-11"),
             ("A ray that goes straight through has not changed speed.",
              "Along the normal, light slows down but does not bend.", "LIGHT-12"),
             ("Going into glass, light bends away from the normal.",
              "Going into glass, light bends towards the normal."),
         ]}]},
    ],
    "key_fact": "Refraction is light changing direction as it crosses into a new material at an angle. "
                "It bends towards the normal when it slows down, and away when it speeds up.",
    "deeper": [
        {"kind": "card", "title": "Different materials, different bends",
         "body": ["Light travels at about 226 000 000 m/s in water.",
                  "It travels at about 200 000 000 m/s in glass.",
                  "Glass slows light more than water does.",
                  "So at the same angle, glass bends a ray more than water does."]},
        {"kind": "card", "title": "Optical fibres",
         "body": ["Light inside glass can meet the surface at a very large angle to the normal.",
                  "Then none of it escapes. It all reflects back inside the glass.",
                  "This is total internal reflection.",
                  "Optical fibres use it to carry light along thin glass threads, even round bends."]},
        {"kind": "card", "title": "Colours bend by different amounts",
         "body": ["Each colour in white light is refracted by a slightly different amount.",
                  "A prism uses this to split white light into a spectrum."]},
    ],
    "try": {"label": "Refraction Lab", "href": "/simulations/physics/refraction-lab/"},
    "connects_heading": None,
    "ks4_becomes": "Ray diagrams for refraction at a boundary, and why a change of speed makes light bend.",
    "connects": {
        "Light travels": "Light is fastest in a vacuum and slows down in materials.",
        "Colour and the spectrum": "A prism refracts each colour by a different amount.",
        "Waves on water: what a wave is": "Water waves also change direction when their speed changes.",
    },
    "figures": [
        {"id": "p7-block-angle", "kind": "diagram", "status": "drawn", "art": "p7-glass-block",
         "title": "A ray into and out of a glass block",
         "desc": "A rectangular glass block with air above and below it. A ray comes down from the "
                 "upper left and hits the top face, where a dashed normal is drawn. Inside the glass "
                 "the ray is closer to the normal: it bends towards the normal. At the bottom face, "
                 "with another dashed normal, the ray bends away from the normal and leaves parallel "
                 "to the way it came in, shifted to one side.",
         "caption": "Towards the normal going in. Away from the normal coming out.",
         "data": {"i": 40, "n": 1.5}},
        {"id": "p7-block-straight", "kind": "diagram", "status": "drawn", "art": "p7-glass-block",
         "title": "A ray along the normal",
         "desc": "The same glass block. A ray comes straight down along the dashed normal, passes "
                 "through the glass and comes out of the bottom, all in one straight line. Labels say "
                 "it slows down in the glass but does not bend, and speeds up again in the air.",
         "caption": "Along the normal: a change of speed, but no change of direction.",
         "data": {"i": 0, "n": 1.5}},
        {"id": "p7-straw", "kind": "diagram", "status": "drawn", "art": "p7-straw",
         "title": "Why a straw looks bent in water",
         "desc": "A glass of water seen from the side, with a straight straw standing in it. A ray "
                 "leaves the bottom of the straw, travels up through the water, and bends away from a "
                 "dashed normal at the water surface on its way to an eye at the top right. A dashed "
                 "line traces that ray straight back into the water, to a point above the real end. "
                 "The real end is labelled really here, and the higher point is labelled looks here.",
         "caption": "The eye traces the light back in a straight line.",
         "data": {"n": 1.33}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Bending away happens on the way out, when light speeds up. Going in, it bends towards the normal.",
            1: "Light slows down in glass. Being clear does not make light faster.",
            2: "It bends at each face. Parallel sides only mean it leaves in its starting direction.",
        },
        "apply": {
            0: "Along the normal there is no angle, so the ray does not bend. It does slow down.",
            1: "Light always slows down in glass. Here it slows down without bending.",
            3: "A little light is reflected, but most goes into the glass and carries straight on.",
        },
    },
}
