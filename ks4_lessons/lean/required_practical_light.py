# -*- coding: utf-8 -*-
"""Required practical activity 9 (physics only), in the lean shape. New record, created from
nothing (no legacy page, no old subtopic data). Spec table: ks4-required-practical-light.md.
AQA 8463 4.6.1.3 (Required practical activity 9) and 8463 section 8.2.9 (AT 4, AT 8). Not on
8464. Routes TF TH. No (HT only) content: why light refracts (a change of speed) is the (HT only)
4.6.2.2 statement, so it is a TH-only Dive deeper link, never on TF.

The spec names the practical and its AT skills only. The method (ray box and slit, plane mirror,
rectangular glass block, a clear box of water as the second substance, crosses, protractor) is
the standard one; see NEW-LESSONS.md. The example results are made up for practice from
n(glass) = 1.5 and n(water) = 1.33, rounded to the nearest degree."""

LESSON = {
    "slug": "required-practical-light",
    "start": {
        "setup": "A narrow ray of light from a ray box enters a glass block at an angle.",
        "question": "If you had to guess, which way does the ray bend inside the glass?",
        "options": [
            ("Away from the normal",
             "Towards the normal. You will measure this: the angle of refraction comes out "
             "smaller than the angle of incidence."),
            ("Towards the normal",
             "Towards the normal. You will measure this: the angle of refraction comes out "
             "smaller than the angle of incidence."),
        ],
        "answer": 1,
    },
    "words": ["ray box", "angle of incidence", "angle of reflection", "angle of refraction"],
    "knowledge": [
        {"kind": "card", "title": "The aim",
         "body": ["Investigate the reflection of light by different types of surface and the "
                  "refraction of light by different substances.",
                  "You trace rays of light on paper and measure their angles with a protractor."]},
        {"kind": "card", "title": "Apparatus",
         "body": [{"points": [
             "A ray box with a single narrow slit, to make one narrow ray of light.",
             "A plane mirror, and other surfaces to compare, such as white paper.",
             "A rectangular glass block, and a second substance: a clear rectangular plastic "
             "box of water.",
             "A protractor, a ruler, a sharp pencil and sheets of plain paper.",
         ]},
                  "Work in a dimmed room, so the ray is easy to see."]},
        {"kind": "card", "title": "Method: reflection",
         "body": [{"slot": "fig:reflection-ray-diagram"},
                  {"points": [
                      "Stand the plane mirror on a sheet of paper and draw a line along its "
                      "reflecting surface.",
                      "Draw a normal at 90° to the line. Aim the ray at the point where the "
                      "normal meets the mirror.",
                      "Mark the incoming ray and the reflected ray with two crosses each, far "
                      "apart.",
                      "Take the mirror away. Join the crosses with a ruler to draw both rays.",
                      "Measure the angle of incidence and the angle of reflection from the "
                      "normal.",
                      "Repeat for several angles of incidence.",
                      "Repeat with other surfaces, and look at how clearly the reflected ray "
                      "shows.",
                  ]}]},
        {"kind": "card", "title": "Method: refraction",
         "body": [{"slot": "fig:rp-glass-block"},
                  {"points": [
                      "Put the glass block on a sheet of paper and draw around it.",
                      "Draw a normal at 90° to one side. Aim the ray at the point where the "
                      "normal meets the side.",
                      "Mark the ray going in and the ray coming out with two crosses each, far "
                      "apart.",
                      "Take the block away. Join each pair of crosses with a ruler, up to the "
                      "outline.",
                      "Join the point where the ray went in to the point where it came out. "
                      "This is the ray inside the block.",
                      "Measure the angle of incidence and the angle of refraction from the "
                      "normal.",
                      "Repeat for several angles of incidence, then with the second substance.",
                  ]}]},
        {"kind": "card", "title": "Variables",
         "body": [{"points": [
             "<strong>Independent</strong>: the angle of incidence, and the type of surface or "
             "the substance.",
             "<strong>Dependent</strong>: the angle of reflection, or the angle of refraction.",
             "<strong>Control</strong>: the same ray box and the same narrow ray, and every "
             "angle measured from the normal.",
         ]}]},
        {"kind": "card", "title": "Getting good results",
         "body": [{"points": [
             "Use a narrow ray, and put each cross in the middle of it.",
             "Put the two crosses on each ray far apart. A small error in one cross then makes "
             "only a small error in the direction of the line.",
             "Use a sharp pencil, and read the protractor from the normal.",
             "Repeat each angle and take a mean.",
         ]}]},
        {"kind": "card", "title": "Safety",
         "body": [{"points": [
             "The ray box gets hot. Do not touch the lamp housing, and let it cool before you "
             "move it.",
             "The room is dimmed. Keep bags and stools out of the way.",
             "Handle the glass block with care. A chipped edge can cut.",
             "Keep the water away from the ray box and its power supply.",
         ]}]},
        {"kind": "card", "title": "What you find",
         "body": [{"points": [
             "<strong>Mirror</strong>: the angle of reflection equals the angle of incidence.",
             "<strong>Smooth, shiny surfaces</strong> give one clear reflected ray.",
             "<strong>Rough surfaces</strong>, such as white paper, scatter the light. There is "
             "no single reflected ray.",
             "<strong>Glass and water</strong>: the ray bends towards the normal as it goes in, "
             "so the angle of refraction is smaller than the angle of incidence.",
             "<strong>Along the normal</strong>, at 0°, the ray goes straight on.",
             "<strong>Different substances</strong> refract light by different amounts.",
         ]}]},
        {"kind": "reveal", "title": "Made-up example results: angle of refraction",
         "cols": ["Glass", "Water"],
         "rows": [
             ("Angle of incidence 0°", "0°", "0°"),
             ("Angle of incidence 20°", "13°", "15°"),
             ("Angle of incidence 40°", "25°", "29°"),
             ("Angle of incidence 60°", "35°", "41°"),
         ]},
        {"kind": "card", "title": "Reading the example results",
         "body": ["These results are made up for practice.",
                  "For each angle of incidence, the angle of refraction is smaller in glass than "
                  "in water. So glass bends the light more than water does."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Measure the angles from the side of the block or the mirror.",
              "Measure every angle from the normal."),
             ("Draw the ray inside the block while the block is in place.",
              "You cannot draw through the block. Take it away first."),
             ("The ray bends away from the normal as it goes into the glass.",
              "It bends towards the normal going in, and away from the normal coming out."),
         ]}]},
    ],
    "key_fact": "Trace narrow rays from a ray box on paper, mark each ray with two crosses far "
                "apart, and measure every angle from the normal with a protractor. For a plane "
                "mirror the angle of reflection equals the angle of incidence; rough surfaces "
                "scatter the light. Light entering glass or water bends towards the normal, and "
                "different substances refract light by different amounts.",
    "deeper": [
        {"kind": "card", "title": "Why the light bends", "routes": ["TH"],
         "body": ["Refraction is due to the difference in the velocity of light in different "
                  "substances. This is in the lesson on wave front diagrams and refraction."]},
        {"kind": "card", "title": "Plotting a graph",
         "body": ["Plot the angle of refraction against the angle of incidence for each "
                  "substance, and draw a smooth curve through each set of points.",
                  "The substance whose curve is lower bends the light more."]},
        {"kind": "card", "title": "Specular and diffuse",
         "body": ["The one clear ray from a smooth surface is specular reflection. The scattering "
                  "from a rough surface is diffuse reflection. Both are in the lesson on visible "
                  "light."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe a method</strong>: apparatus, the steps in order, what you "
             "measure, and how you make it accurate and safe.",
             "<strong>Identify a variable</strong>: say which one you change, which you measure, "
             "and which you keep the same.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the piece of apparatus that makes a single narrow ray of light.",
             "why": "A ray box with a single slit makes one narrow ray.",
             "options": [
                 {"text": "A protractor", "correct": False,
                  "reply": "A protractor measures the angles."},
                 {"text": "A ray box", "correct": True},
                 {"text": "A glass block", "correct": False,
                  "reply": "The glass block refracts the ray. It does not make it."},
                 {"text": "A plane mirror", "correct": False,
                  "reply": "The mirror reflects the ray. It does not make it."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "In the refraction part of the practical, identify the dependent variable.",
             "why": "The dependent variable is the one you measure: the angle of refraction.",
             "options": [
                 {"text": "The angle of incidence", "correct": False,
                  "reply": "You choose the angle of incidence: it is the independent variable."},
                 {"text": "The size of the glass block", "correct": False,
                  "reply": "That is not measured. Keep the same block."},
                 {"text": "The brightness of the ray", "correct": False,
                  "reply": "That is not measured. Keep the same ray box."},
                 {"text": "The angle of refraction", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "A ray of light enters a glass block from air. The angle of incidence is "
                       "40°. Identify the most likely angle of refraction.",
             "why": "Light entering glass bends towards the normal, so the angle of refraction is "
                    "smaller than 40°, but bigger than 0°.",
             "options": [
                 {"text": "0°", "correct": False,
                  "reply": "Only a ray along the normal has an angle of refraction of 0°. This "
                           "ray bends, but not that far."},
                 {"text": "25°", "correct": True},
                 {"text": "40°", "correct": False,
                  "reply": "Then the ray would not bend at all."},
                 {"text": "55°", "correct": False,
                  "reply": "A bigger angle means bending away from the normal. Light entering "
                           "glass bends towards it."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why you put the two crosses on each ray far apart.",
             "why": "With the crosses far apart, a small error in placing one cross makes only a "
                    "small error in the direction of the ray.",
             "options": [
                 {"text": "So the ray box does not get too hot", "correct": False,
                  "reply": "The crosses do not affect the ray box."},
                 {"text": "So the ray is brighter where it is marked on the paper", "correct": False,
                  "reply": "Crosses do not change how bright the ray is."},
                 {"text": "So the line through them has an accurate direction", "correct": True},
                 {"text": "So the angle of refraction becomes bigger than before", "correct": False,
                  "reply": "Marking the ray does not change how it bends."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 4,
             "prompt": "Describe how to measure the angle of refraction for light entering a glass "
                       "block. Put the links in order.",
             "links": ["Put the glass block on a sheet of paper and draw around it.",
                       "Draw a normal at 90° to one side, and aim the ray at the point where the "
                       "normal meets that side.",
                       "Mark the point where the ray enters the block and the point where it comes "
                       "out, then take the block away.",
                       "Join the point where the ray went in to the point where it came out, and "
                       "measure the angle between this line and the normal."],
             "herrings": [{"text": "Measure the angle between the ray inside the block and the "
                                   "side of the block.",
                           "why": "Measure from the normal, not from the side."},
                          {"text": "Draw the normal along the side of the block, where the ray "
                                   "goes in.",
                           "why": "The normal is at 90° to the side, not along it."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A ray of light hits a sheet of white paper. No single reflected ray can be "
                       "seen. Explain why. Put the links in order.",
             "links": ["The surface of the paper is rough, with tiny bumps facing different ways.",
                       "So the normal points in a different direction at each part of the surface.",
                       "Each part of the light reflects at the same angle to its own normal as it "
                       "arrived, so the light goes off in many directions: it is scattered."],
             "herrings": [{"text": "The paper absorbs all of the light.",
                           "why": "White paper reflects most of the light. It looks bright."},
                          {"text": "The paper transmits all of the light.",
                           "why": "Very little light passes through paper. Most is reflected."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 6,
             "prompt": "Describe a method to investigate how the angle of refraction depends on "
                       "the angle of incidence for light entering a glass block.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "A clear, logical method that could be "
                  "followed: tracing the ray, measuring both angles from the normal, a range of "
                  "angles, and a way to make the results accurate or a safety point.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Most of the steps, with some detail missing "
                  "or out of order.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant steps.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Put the block on paper and draw around it.",
                        "Draw a normal at 90° to one side.",
                        "Shine a narrow ray from a ray box at the point where the normal meets "
                        "the side, and measure the angle of incidence with a protractor.",
                        "Mark the rays going in and coming out with crosses, take the block away "
                        "and join the points where the ray went in and came out.",
                        "Measure the angle of refraction from the normal.",
                        "Repeat for a range of angles of incidence, for example 10° to 70°.",
                        "Repeat each angle and take a mean, or put the crosses far apart.",
                        "Do not touch the hot ray box."],
             "reject": ["“Measure the angles from the side of the block.”",
                        "“Use a wide beam of light.”"]},
        ],
    },
}
