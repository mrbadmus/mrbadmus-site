# -*- coding: utf-8 -*-
"""Reflection of waves, in the lean shape. New record, created from nothing (no legacy page, no
old subtopic data). Spec table: ks4-reflection-of-waves.md (AQA 8463 4.6.1.3 (physics only), all
tiers). Not on 8464. Routes TF TH.

4.6.1.3 has no (HT only) line, so every card is on both Triple routes. The one card that leans on
an (HT only) statement from 4.6.2.2 ("in ways that vary with wavelength") is Dive deeper and TH
only. Required practical activity 9 sits under 4.6.1.3 in the spec; it has its own lesson
(required-practical-light), and this page only points to it.

"Angle of incidence = angle of reflection" is not spec wording, but 4.6.1.3 asks pupils to
construct ray diagrams of reflection, which needs it (UNSURE item in NEW-LESSONS.md)."""

LESSON = {
    "slug": "reflection-of-waves",
    "start": {
        "setup": "You stand in a lit room at night and look at a window.",
        "question": "If you had to guess, what happens to the light when it reaches the glass?",
        "options": [
            ("All of it passes through",
             "Most passes through, but some is reflected. That is why you see a faint reflection "
             "of the room in the window."),
            ("Some of it bounces back",
             "Most passes through, but some is reflected. That is why you see a faint reflection "
             "of the room in the window."),
        ],
        "answer": 1,
    },
    "words": ["reflect", "absorb", "transmit", "normal"],
    "knowledge": [
        {"kind": "card", "title": "At a boundary",
         "body": ["Waves can be reflected at the boundary between two different materials.",
                  "Waves can be absorbed or transmitted at the boundary between two different "
                  "materials.",
                  {"points": [
                      "<strong>Reflected</strong>: the wave bounces back into the first material.",
                      "<strong>Absorbed</strong>: the material takes in the wave's energy.",
                      "<strong>Transmitted</strong>: the wave passes on into the second material.",
                  ]},
                  "Often more than one happens at the same boundary. Part of the wave is reflected, "
                  "part is absorbed and the rest is transmitted."]},
        {"kind": "reveal", "title": "What happens at the boundary",
         "cols": ["What happens to most of the wave"],
         "rows": [
             ("Light meets a mirror", "It is reflected"),
             ("Light meets a clear window", "It is transmitted, and a little is reflected"),
             ("Light meets matt black card", "It is absorbed"),
             ("Sound meets a thick curtain", "It is absorbed"),
             ("Sound meets a hard, flat wall", "It is reflected, so you can hear an echo"),
         ]},
        {"kind": "card", "title": "The effects",
         "body": [{"points": [
             "<strong>Reflection</strong> sends the wave back. An echo is reflected sound. You see "
             "yourself in a mirror by reflected light.",
             "<strong>Absorption</strong> transfers the wave's energy to the material. A dark "
             "road warms up in sunshine because it absorbs the Sun's radiation.",
             "<strong>Transmission</strong> lets the wave carry on into the next material. The "
             "transmitted wave can change direction: that is refraction, in the lesson on "
             "properties of electromagnetic waves.",
         ]}]},
        {"kind": "card", "title": "Drawing a ray diagram for reflection",
         "body": [{"slot": "fig:reflection-ray-diagram"},
                  {"points": [
                      "Draw the mirror or surface as a straight line.",
                      "Draw the incoming ray with a ruler, with an arrow, to the point where it "
                      "meets the surface.",
                      "At that point, draw the normal: a dashed line at 90° to the surface.",
                      "Measure the angle of incidence, between the incoming ray and the normal.",
                      "Draw the reflected ray on the other side of the normal, at the same angle, "
                      "with an arrow.",
                  ]},
                  "The angle of incidence equals the angle of reflection. Measure both from the "
                  "normal, never from the surface."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Measure the angles from the mirror.",
              "Measure both angles from the normal."),
             ("At a boundary a wave is reflected, absorbed or transmitted, never more than one.",
              "Often more than one happens. Sound meeting a wall is partly reflected and partly "
              "absorbed."),
             ("An absorbed wave just disappears.",
              "Its energy is transferred to the material, which can warm up."),
         ]}]},
    ],
    "key_fact": "At the boundary between two different materials a wave can be reflected, absorbed "
                "or transmitted, and often part of it does each. On a ray diagram for reflection, "
                "draw the normal at 90° to the surface: the angle of reflection equals the angle of "
                "incidence, both measured from the normal.",
    "deeper": [
        {"kind": "card", "title": "It depends on the wavelength", "routes": ["TH"],
         "body": ["Different substances may absorb, transmit, refract or reflect electromagnetic "
                  "waves in ways that vary with wavelength.",
                  "A brick wall absorbs or reflects visible light, so you cannot see through it. "
                  "Radio waves are mostly transmitted through the wall, with some absorbed, so a "
                  "radio still works indoors."]},
        {"kind": "card", "title": "Echoes in a room",
         "body": ["Hard, flat walls and floors reflect most of the sound that reaches them.",
                  "Soft materials such as curtains and carpets absorb more of it. So an empty room "
                  "echoes more than the same room with curtains and carpets."]},
        {"kind": "card", "title": "Smooth and rough surfaces",
         "body": ["A smooth surface reflects light in a single direction. A rough surface scatters "
                  "it. This is in the lesson on visible light."]},
        {"kind": "card", "title": "The practical",
         "body": ["Required practical activity 9, the reflection of light by different types of "
                  "surface and the refraction of light by different substances, has its own "
                  "lesson."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Construct</strong> or <strong>draw</strong> a ray diagram: use a ruler, "
             "draw the normal, put an arrow on every ray, and make the two angles equal.",
             "<strong>Describe</strong> what happens at a boundary: say whether the wave is "
             "reflected, absorbed or transmitted, and the effect of each.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what is meant by a wave being transmitted at a boundary.",
             "why": "A transmitted wave passes on into the second material.",
             "options": [
                 {"text": "It bounces back into the first material", "correct": False,
                  "reply": "That is reflection."},
                 {"text": "It passes on into the second material", "correct": True},
                 {"text": "Its energy is taken in by the material", "correct": False,
                  "reply": "That is absorption."},
                 {"text": "It stops moving at the boundary", "correct": False,
                  "reply": "A transmitted wave carries on into the next material."},
             ]},
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the line drawn at 90° to a mirror, at the point where a ray meets it.",
             "why": "The normal is at 90° to the surface. Both angles are measured from it.",
             "options": [
                 {"text": "The incident ray", "correct": False,
                  "reply": "The incident ray is the ray travelling towards the mirror."},
                 {"text": "The reflected ray", "correct": False,
                  "reply": "The reflected ray leaves the mirror."},
                 {"text": "The normal", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Determine", "marks": 2,
             "prompt": "A ray of light hits a plane mirror. The angle between the ray and the "
                       "surface of the mirror is 30°. Determine the angle of reflection.",
             "why": "The angle of incidence is measured from the normal: 90° − 30° = 60°. The "
                    "angle of reflection equals it: 60°.",
             "options": [
                 {"text": "30°", "correct": False,
                  "reply": "30° is measured from the mirror. From the normal it is 90° − 30° = 60°."},
                 {"text": "60°", "correct": True},
                 {"text": "120°", "correct": False,
                  "reply": "120° is the angle between the two rays: 60° + 60°."},
                 {"text": "150°", "correct": False,
                  "reply": "That is 180° − 30°. Measure from the normal: 90° − 30° = 60°."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "Light shines on a clear glass window. Identify what happens to the "
                       "light at the glass.",
             "why": "You can see through clear glass, so most of the light is transmitted. A little "
                    "is reflected, which is why you see a faint reflection in a window.",
             "options": [
                 {"text": "Most is reflected and a little is transmitted", "correct": False,
                  "reply": "Then the window would act like a mirror. You can see through it, so "
                           "most is transmitted."},
                 {"text": "Most is absorbed and a little is transmitted", "correct": False,
                  "reply": "Clear glass absorbs very little. You can see through it, so most is "
                           "transmitted."},
                 {"text": "All of it is transmitted through the clear glass", "correct": False,
                  "reply": "Then you would never see a reflection in a window."},
                 {"text": "Most is transmitted and a little is reflected", "correct": True},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 4,
             "prompt": "Describe how to draw a ray diagram for light reflected by a plane mirror. "
                       "Put the links in order.",
             "links": ["Draw the incoming ray, with an arrow, to the point where it meets the "
                       "mirror.",
                       "At that point, draw the normal at 90° to the mirror.",
                       "Measure the angle of incidence, between the incoming ray and the normal.",
                       "Draw the reflected ray on the other side of the normal, at the same "
                       "angle."],
             "herrings": [{"text": "Measure the angle between the incoming ray and the mirror.",
                           "why": "Both angles are measured from the normal."},
                          {"text": "Draw the reflected ray on the same side of the normal as the "
                                   "incoming ray.",
                           "why": "The reflected ray is on the other side of the normal."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why you hear an echo when you shout towards a cliff. Put the "
                       "links in order.",
             "links": ["The sound wave travels through the air to the cliff.",
                       "At the boundary between the air and the rock, some of the sound is "
                       "reflected.",
                       "The reflected sound travels back through the air to your ears, a short "
                       "time later."],
             "herrings": [{"text": "All of the sound is absorbed by the cliff.",
                           "why": "Absorbed sound does not come back. The echo is the reflected "
                                  "part."},
                          {"text": "The cliff makes a new sound of its own.",
                           "why": "The cliff makes no sound. It reflects the sound that reaches "
                                  "it."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Light shines onto three surfaces: a plane mirror, a sheet of clear glass "
                       "and a piece of matt black card. Describe what happens to the light at "
                       "each surface.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "All three surfaces described, using "
                  "reflected, transmitted and absorbed correctly, with a detail such as equal "
                  "angles at the mirror or a little reflection from the glass.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two surfaces described correctly.",
                  "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["The mirror reflects most of the light.",
                        "At the mirror the angle of reflection equals the angle of incidence.",
                        "The clear glass transmits most of the light, and reflects a little.",
                        "The matt black card absorbs most of the light.",
                        "The energy absorbed warms the card."],
             "reject": ["“The black card reflects black light.”",
                        "“The glass absorbs all of the light.”"]},
        ],
    },
}
