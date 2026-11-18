# -*- coding: utf-8 -*-
"""Wave front diagrams and refraction, in the lean shape. New record, no legacy page.
Spec table: ks4-wave-front-refraction.md (AQA 8464 6.6.2.2 (HT only) / 8463 4.6.2.2 (HT only)).
CH TH only. The old TH data called this lesson "physics only": it is Higher tier on both specs,
and not Triple only. The old spec field "6.6.2 (HT only)" is not a real point.

The lead's split: ray diagrams live on properties-em-waves-1; this page teaches wave front
diagrams in full. "The frequency does not change" is used once, as the reason the wavelength
gets shorter; it is not a spec sentence and is listed in UNSURE.md for the examiner."""

LESSON = {
    "slug": "wave-front-refraction",
    "start": {
        "setup": "Water waves reach the edge of a shallow region at an angle. Waves travel more "
                 "slowly in shallow water.",
        "question": "If you had to guess, do the waves change direction as they cross into the "
                    "shallow water?",
        "options": [
            ("Yes, they turn",
             "Yes. The end of each wave that reaches the shallow water first slows down first, "
             "so the wave turns. This is refraction."),
            ("No, they go straight on",
             "Yes. The end of each wave that reaches the shallow water first slows down first, "
             "so the wave turns. This is refraction."),
        ],
        "answer": 0,
    },
    "words": ["wave front", "refraction", "wave speed", "wavelength"],
    "knowledge": [
        {"kind": "card", "title": "Wave fronts",
         "body": ["A wave front is a line joining the same point on each part of a wave, for "
                  "example along the top of each ripple.",
                  {"slot": "fig:wave-fronts"},
                  {"points": [
                      "The distance between one wave front and the next is the wavelength.",
                      "The wave travels at 90° to its wave fronts.",
                  ]}]},
        {"kind": "card", "title": "Why waves refract",
         "body": ["Some effects, for example refraction, are due to the difference in velocity "
                  "of the waves in different substances.",
                  "Light travels more slowly in glass than in air. Water waves travel more slowly "
                  "in shallow water than in deep water."]},
        {"kind": "card", "title": "The wave front diagram",
         "body": [{"slot": "fig:wavefront-refraction"},
                  {"points": [
                      "The wave fronts reach the boundary at an angle.",
                      "One end of each wave front crosses the boundary first, and slows down "
                      "first.",
                      "The rest of that wave front is still moving at the faster speed, so the "
                      "wave front swings round.",
                      "The wave changes direction: it bends towards the normal.",
                      "In the slower medium the wave fronts are closer together. The wavelength "
                      "is shorter.",
                  ]}]},
        {"kind": "reveal", "title": "Slowing down and speeding up",
         "cols": ["Slows down", "Speeds up"],
         "rows": [
             ("Example", "Air into glass", "Glass into air"),
             ("Direction", "Bends towards the normal", "Bends away from the normal"),
             ("Wavelength", "Gets shorter", "Gets longer"),
             ("Frequency", "Stays the same", "Stays the same"),
         ]},
        {"kind": "card", "title": "Linking it to v = f λ",
         "body": ["The waves arrive at the boundary at the same rate as they leave it, so the "
                  "frequency does not change.",
                  "v = f λ. With the same frequency, a lower speed means a shorter wavelength.",
                  "For example, light that slows to two thirds of its speed has two thirds of its "
                  "wavelength."]},
        {"kind": "card", "title": "Along the normal",
         "body": ["A wave that meets the boundary along the normal still slows down, and its "
                  "wavelength still gets shorter.",
                  "The whole wave front slows down at the same moment, so the wave does not change "
                  "direction."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The frequency changes when a wave refracts.",
              "The speed and the wavelength change. The frequency stays the same."),
             ("A wave that slows down bends away from the normal.",
              "A wave that slows down bends towards the normal."),
             ("The wave travels along its wave fronts.",
              "The wave travels at 90° to its wave fronts."),
         ]}]},
    ],
    "key_fact": "Refraction happens because waves travel at different speeds in different "
                "substances. When wave fronts cross a boundary at an angle, the end that enters "
                "the slower medium first slows down first, so the wave changes direction towards "
                "the normal and its wavelength gets shorter.",
    "deeper": [
        {"kind": "card", "title": "Seeing it in a ripple tank",
         "body": ["Put a flat sheet of glass or plastic in part of a ripple tank to make the water "
                  "shallow there.",
                  "Waves that cross into the shallow water at an angle change direction, and their "
                  "wave fronts get closer together."]},
        {"kind": "card", "title": "It depends on the wavelength",
         "body": ["Different substances may absorb, transmit, refract or reflect electromagnetic "
                  "waves in ways that vary with wavelength.",
                  "A glass prism refracts violet light more than red light, so white light "
                  "spreads out into colours."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Use a wave front diagram to explain</strong>: say which end of the wave "
             "front changes speed first, and what that does to the direction.",
             "<strong>Explain</strong> the change in wavelength: speed changes, frequency stays "
             "the same, so v = f λ gives the new wavelength.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the reason waves refract at the boundary between two substances.",
             "why": "Refraction is due to the difference in velocity of the waves in the two "
                    "substances.",
             "options": [
                 {"text": "The wave speed changes at the boundary", "correct": True},
                 {"text": "The frequency changes at the boundary", "correct": False,
                  "reply": "The frequency stays the same. The speed changes."},
                 {"text": "The amplitude changes at the boundary", "correct": False,
                  "reply": "Refraction is caused by the change in speed."},
                 {"text": "The wave is reflected by the boundary", "correct": False,
                  "reply": "Reflection sends a wave back. Refraction is caused by the change in "
                           "speed."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "A wave slows down as it crosses a boundary at an angle. Give the direction "
                       "it bends.",
             "why": "A wave that slows down bends towards the normal.",
             "options": [
                 {"text": "Towards the normal", "correct": True},
                 {"text": "Away from the normal", "correct": False,
                  "reply": "That happens when the wave speeds up."},
                 {"text": "It does not change direction", "correct": False,
                  "reply": "At an angle, one end slows down first, so the wave turns."},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "A water wave has a frequency of 2.0 Hz. In shallow water it travels at "
                       "0.30 m/s. Calculate its wavelength in the shallow water.",
             "convOptions": ["Nothing to convert", "Convert Hz to kHz: divide by 1000",
                             "Convert m/s to cm/s: multiply by 100"],
             "convAnswer": 0, "answer": 0.15, "tol": 0.005, "unit": "m",
             "units": ["m", "Hz", "m/s", "s"],
             "right": "λ = 0.30 ÷ 2.0 = 0.15 m.",
             "wrong": "v = f λ, so λ = v ÷ f = 0.30 ÷ 2.0 = 0.15 m.",
             "model": ["C · Nothing to convert", "F · v = f λ", "I · 0.30 = 2.0 × λ",
                       "F · λ = 0.30 ÷ 2.0 = 0.15", "A · λ = 0.15 m"]},
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "Light passes from air into glass and slows down. Identify what happens to "
                       "the light in the glass.",
             "why": "The speed is lower and the wavelength is shorter. The frequency stays the "
                    "same.",
             "options": [
                 {"text": "Speed lower, wavelength shorter, frequency the same", "correct": True},
                 {"text": "Speed lower, wavelength shorter, frequency lower", "correct": False,
                  "reply": "The frequency stays the same at the boundary."},
                 {"text": "Speed lower, wavelength longer, frequency the same", "correct": False,
                  "reply": "v = f λ: with the same frequency, a lower speed means a shorter "
                           "wavelength."},
                 {"text": "Speed the same, wavelength shorter, frequency higher", "correct": False,
                  "reply": "The light slows down in glass. That is why it refracts."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Use the idea of wave fronts to explain why light bends towards the normal "
                       "as it enters glass at an angle. Put the links in order.",
             "links": ["One end of each wave front reaches the glass first.",
                       "That end slows down, while the rest of the wave front is still in the air, "
                       "moving faster.",
                       "So the wave front swings round, and the light changes direction towards "
                       "the normal."],
             "herrings": [{"text": "The glass pulls the light towards it.",
                           "why": "Nothing pulls the light. One end of the wave front slows down "
                                  "first."},
                          {"text": "The frequency of the light drops in the glass.",
                           "why": "The frequency stays the same. The speed drops."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why the wave fronts get closer together when a wave slows down at "
                       "a boundary. Put the links in order.",
             "links": ["The wave crosses into a medium where it travels more slowly.",
                       "Each wave front moves a shorter distance before the next wave front "
                       "arrives.",
                       "So the wave fronts are closer together: the wavelength is shorter."],
             "herrings": [{"text": "The wave fronts spread further apart in the slower medium.",
                           "why": "Slower waves travel less far between wave fronts, so the fronts "
                                  "bunch up."},
                          {"text": "The frequency doubles in the slower medium.",
                           "why": "The frequency stays the same."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 6,
             "prompt": "Water waves pass at an angle from deep water into shallow water, where they "
                       "travel more slowly. Use the idea of wave fronts to explain what happens to "
                       "the direction and the wavelength of the waves.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "A clear, linked explanation of the change in "
                  "direction from one end of the wave front slowing first, and of the shorter "
                  "wavelength.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "The change in direction or the change in "
                  "wavelength explained, with some linking to the change in speed.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "A change described with no reason given.",
                  "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["The wave fronts reach the boundary at an angle.",
                        "One end of each wave front enters the shallow water first.",
                        "That end slows down first, while the rest is still moving faster.",
                        "So the wave front swings round: the waves change direction, towards the "
                        "normal.",
                        "In the shallow water the wave fronts are closer together, so the "
                        "wavelength is shorter.",
                        "The frequency stays the same, so v = f λ gives a shorter wavelength at "
                        "the lower speed."],
             "reject": ["“The waves speed up in the shallow water.”",
                        "“The waves bend because the water is shallower.” (no link to the change "
                        "in speed)"]},
        ],
    },
}
