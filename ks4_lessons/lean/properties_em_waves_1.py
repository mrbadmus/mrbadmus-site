# -*- coding: utf-8 -*-
"""Properties of electromagnetic waves 1, in the lean shape. New record, no legacy page.
Spec table: ks4-properties-em-waves-1.md (AQA 8464 6.6.2.2 / 8463 4.6.2.2, word for word the
same).

Ray diagrams of refraction are for every route. The two (HT only) statements are on CH TH only;
the third (HT only) statement, wave front diagrams, is taught in full by wave-front-refraction
(CH TH) and only named here. The old built page taught "caused by a change in wave speed" on
Foundation: that is the HT velocity statement, now behind CH TH.

Required practical: the lead placed 8464 Required practical activity 21 (infrared and surfaces)
here, on CF CH. On TF TH the same practical (8463 Required practical activity 10) is taught by
infrared-black-bodies, so this page only points to it there. The old "RP20 refraction of light"
label was wrong twice over (RP 20 is the ripple tank; refraction of light is 8463 RP 9, physics
only, which has no page): dropped."""

LESSON = {
    "slug": "properties-em-waves-1",
    "start": {
        "setup": "A straight straw stands in a glass of water.",
        "question": "If you had to guess, why does the straw look bent where it enters the water?",
        "options": [
            ("The light from it changes direction",
             "The light changes direction as it passes from the water into the air. This is "
             "refraction. The straw is still straight."),
            ("The water bends the straw",
             "The light changes direction as it passes from the water into the air. This is "
             "refraction. The straw is still straight."),
        ],
        "answer": 0,
    },
    "words": ["refraction", "medium", "normal", "ray diagram"],
    "knowledge": [
        {"kind": "card", "title": "Refraction",
         "body": ["Refraction is when a wave changes direction as it passes from one medium into "
                  "a different medium.",
                  "A medium is a material a wave travels through, such as air, water or glass.",
                  "Light changes direction only at the boundary between the two media."]},
        {"kind": "card", "title": "Drawing a ray diagram",
         "body": [{"slot": "fig:refraction-ray-diagram"},
                  {"points": [
                      "A ray is a straight line with an arrow showing the direction the light "
                      "travels. Draw it with a ruler.",
                      "Draw the normal where the ray meets the boundary. The normal is a dashed "
                      "line at 90° to the boundary.",
                      "The angle of incidence is between the incoming ray and the normal.",
                      "The angle of refraction is between the refracted ray and the normal.",
                  ]},
                  "Always measure the angles from the normal, never from the boundary."]},
        {"kind": "reveal", "title": "Which way the light bends",
         "cols": ["What happens to the ray"],
         "rows": [
             ("Air into glass or water, at an angle", "It bends towards the normal"),
             ("Glass or water into air, at an angle", "It bends away from the normal"),
             ("Along the normal, at 90° to the boundary", "It does not change direction"),
         ]},
        {"kind": "card", "title": "Why waves refract", "routes": ["CH", "TH"],
         "body": ["Some effects, for example refraction, are due to the difference in velocity "
                  "of the waves in different substances.",
                  "Light travels more slowly in glass than in air.",
                  {"points": ["A ray that slows down bends towards the normal.",
                              "A ray that speeds up bends away from the normal."]},
                  "Wave front diagrams explain this. They are in the lesson on wave front diagrams "
                  "and refraction."]},
        {"kind": "card", "title": "It depends on the wavelength", "routes": ["CH", "TH"],
         "body": ["Different substances may absorb, transmit, refract or reflect electromagnetic "
                  "waves in ways that vary with wavelength.",
                  {"points": [
                      "<strong>Absorb</strong>: the substance takes in the wave's energy.",
                      "<strong>Transmit</strong>: the wave passes through.",
                      "<strong>Refract</strong>: the wave changes direction at a boundary.",
                      "<strong>Reflect</strong>: the wave bounces back from the surface.",
                  ]},
                  "For example, X-rays are transmitted by soft tissue but absorbed by bone. A "
                  "glass prism refracts violet light more than red light, so white light spreads "
                  "out into colours."]},
        {"kind": "card", "title": "Required practical activity 21", "routes": ["CF", "CH"],
         "body": ["Investigate how the amount of infrared radiation absorbed or radiated by a "
                  "surface depends on the nature of that surface.",
                  {"slot": "fig:leslie-cube"},
                  {"points": [
                      "Fill a Leslie cube with hot water. Each of its four faces has a different "
                      "surface: matt black, shiny black, matt white and shiny silver.",
                      "Point an infrared detector at each face in turn, from the same distance.",
                      "Record the reading for each face.",
                  ]},
                  "Matt black radiates the most infrared. Shiny silver radiates the least.",
                  "Keep the distance from the detector the same for every face, and take every "
                  "reading at the same water temperature, so the test is fair."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Measure the angle from the boundary.",
              "Measure every angle from the normal."),
             ("The light bends in the middle of the glass.",
              "It changes direction only at a boundary."),
             ("The normal is the boundary.",
              "The normal is a line at 90° to the boundary."),
         ]}]},
    ],
    "key_fact": "Refraction is a change in direction when a wave crosses the boundary between two "
                "different media. On a ray diagram, draw the normal at 90° to the boundary and "
                "measure every angle from it: light passing from air into glass bends towards the "
                "normal, and light passing from glass into air bends away from it.",
    "deeper": [
        {"kind": "card", "title": "Why the straw looks bent",
         "body": ["Light from the part of the straw under the water refracts as it leaves the "
                  "water.",
                  "Your eye traces the light back in a straight line. So that part of the straw "
                  "seems to be in a different place."]},
        {"kind": "card", "title": "Through a glass block",
         "body": ["A ray bends towards the normal as it enters a rectangular glass block, travels "
                  "in a straight line inside, and bends away from the normal as it leaves. It "
                  "comes out parallel to the direction it went in."]},
        {"kind": "card", "title": "The infrared practical", "routes": ["TF", "TH"],
         "body": ["Required practical activity 10, how the amount of infrared radiation absorbed "
                  "or radiated by a surface depends on the nature of that surface, is in the "
                  "lesson on infrared and black bodies."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Draw</strong> or <strong>complete</strong> a ray diagram: use a ruler, draw "
             "the normal, and put an arrow on every ray.",
             "<strong>Describe</strong> what happens to a ray: say which way it bends, compared "
             "with the normal, at each boundary.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what is meant by the normal on a ray diagram.",
             "why": "The normal is a line at 90° to the boundary, where the ray meets it.",
             "options": [
                 {"text": "A line at 90° to the boundary", "correct": True},
                 {"text": "The boundary between the two media", "correct": False,
                  "reply": "The normal is at 90° to the boundary."},
                 {"text": "The ray after it has refracted", "correct": False,
                  "reply": "That is the refracted ray. The normal is a construction line."},
                 {"text": "The ray before it reaches the boundary", "correct": False,
                  "reply": "That is the incident ray."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "A ray of light passes from air into a glass block at an angle. Give the "
                       "direction it bends.",
             "why": "Light passing from air into glass bends towards the normal.",
             "options": [
                 {"text": "Towards the normal", "correct": True},
                 {"text": "Away from the normal", "correct": False,
                  "reply": "That happens when light passes from glass into air."},
                 {"text": "It does not bend", "correct": False,
                  "reply": "Only a ray along the normal goes straight on."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "A ray of light travels along the normal from air into a glass block. "
                       "Identify its direction inside the glass.",
             "why": "A ray along the normal does not change direction.",
             "options": [
                 {"text": "Straight on, along the normal", "correct": True},
                 {"text": "Bent away from the normal", "correct": False,
                  "reply": "A ray along the normal does not bend."},
                 {"text": "Along the boundary", "correct": False,
                  "reply": "It carries straight on into the glass."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "A ray passes from glass into air. Its angle of incidence in the glass is "
                       "30°. Identify its angle of refraction in the air.",
             "why": "Light passing from glass into air bends away from the normal, so the angle "
                    "gets bigger.",
             "options": [
                 {"text": "Smaller than 30°: it bends towards the normal", "correct": False,
                  "reply": "Light bends towards the normal going into glass, not out of it."},
                 {"text": "Bigger than 30°: it bends away from the normal", "correct": True},
                 {"text": "Exactly 30°: it does not bend", "correct": False,
                  "reply": "Only a ray along the normal goes straight on."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how to draw a ray diagram for light entering a glass block from "
                       "air. Put the links in order.",
             "links": ["Draw the incoming ray, with an arrow, to the point where it meets the "
                       "boundary.",
                       "At that point, draw the normal at 90° to the boundary.",
                       "Draw the refracted ray inside the glass, bent towards the normal."],
             "herrings": [{"text": "Draw the normal along the boundary.",
                           "why": "The normal is at 90° to the boundary."},
                          {"text": "Draw the refracted ray bent away from the normal.",
                           "why": "Light entering glass from air bends towards the normal."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why a straw in a glass of water looks bent. Put the links in order.",
             "links": ["Light from the part of the straw under the water travels up to the "
                       "surface.",
                       "At the surface the light passes from water into air, and changes "
                       "direction: it refracts.",
                       "Your eye traces the light back in a straight line, so that part of the "
                       "straw seems to be in a different place."],
             "herrings": [{"text": "The water bends the straw.",
                           "why": "The straw stays straight. Only the light changes direction."},
                          {"text": "The light changes direction in the middle of the water.",
                           "why": "It changes direction only at the boundary."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "A ray of light enters one side of a rectangular glass block at an angle "
                       "and leaves from the opposite side. Describe what happens to the ray.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "What happens at both boundaries and inside "
                  "the block, with the direction of bending compared with the normal each time.",
                  "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One boundary described, or bending stated "
                  "without saying which way.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["At the first boundary the ray refracts, from air into glass.",
                        "It bends towards the normal.",
                        "Inside the block it travels in a straight line.",
                        "At the second boundary it refracts again, from glass into air, and bends "
                        "away from the normal.",
                        "It leaves parallel to the direction it went in."],
             "reject": ["“It bends inside the glass.”",
                        "“It bends towards the normal as it leaves the block.”"]},
        ],
    },
}
