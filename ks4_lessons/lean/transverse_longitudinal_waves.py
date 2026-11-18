# -*- coding: utf-8 -*-
"""Transverse and longitudinal waves, in the lean shape. New record, no legacy page.
Spec table: ks4-transverse-longitudinal-waves.md (AQA 8464 6.6.1.1 / 8463 4.6.1.1, word for word
the same). The old data's "RP19 slinky" label is not an AQA required practical: dropped. The
waves required practical (8464 RP 20 / 8463 RP 8) belongs to properties-of-waves."""

LESSON = {
    "slug": "transverse-longitudinal-waves",
    "start": {
        "setup": "A rubber duck floats on a pond. Ripples pass under it.",
        "question": "If you had to guess, is the duck carried along by the ripples?",
        "options": [
            ("Yes, it moves along with them",
             "No. The duck bobs up and down in the same place. The wave travels, but the water "
             "does not."),
            ("No, it bobs up and down",
             "No. The duck bobs up and down in the same place. The wave travels, but the water "
             "does not."),
        ],
        "answer": 1,
    },
    "words": ["transverse", "longitudinal", "compression", "rarefaction"],
    "knowledge": [
        {"kind": "card", "title": "Waves transfer energy",
         "body": ["Waves transfer energy from one place to another.",
                  "The wave travels. The water or air it travels through does not travel with it.",
                  "Waves may be either transverse or longitudinal."]},
        {"kind": "card", "title": "Transverse waves",
         "body": ["In a transverse wave the oscillations (vibrations) are at right angles to the "
                  "direction the wave travels.",
                  {"slot": "fig:transverse-wave"},
                  "The ripples on a water surface are an example of a transverse wave.",
                  "Electromagnetic waves, such as light, are transverse too."]},
        {"kind": "card", "title": "Longitudinal waves",
         "body": ["In a longitudinal wave the oscillations are parallel to the direction the wave "
                  "travels.",
                  {"slot": "fig:longitudinal-wave"},
                  "Longitudinal waves show areas of compression and rarefaction.",
                  {"points": ["<strong>Compression</strong>: a region where the particles are "
                              "closer together.",
                              "<strong>Rarefaction</strong>: a region where the particles are "
                              "further apart."]},
                  "Sound waves travelling through air are longitudinal."]},
        {"kind": "card", "title": "Evidence: ripples on water",
         "body": [{"points": [
             "Float a cork on the water in a ripple tank, then make ripples.",
             "As the ripples pass, the cork bobs up and down.",
             "The cork stays in the same place. It is not carried along with the ripples.",
         ]},
             "So it is the wave that travels, and not the water itself."]},
        {"kind": "card", "title": "Evidence: sound in air",
         "body": [{"points": [
             "Hold a candle flame in front of a loudspeaker playing a loud, low note.",
             "The flame moves back and forth, along the direction the sound travels.",
             "The flame is not blown away from the loudspeaker.",
         ]},
             "So the air vibrates back and forth about the same place. It is the wave that "
             "travels, and not the air itself."]},
        {"kind": "card", "title": "Sound needs a material",
         "body": ["A sound wave is passed on by particles pushing on the particles next to them. "
                  "So sound needs a material, such as air, to travel through.",
                  "Sound cannot travel through a vacuum. Electromagnetic waves, such as light, "
                  "can."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Water travels along with a ripple.",
              "The water moves up and down. Only the wave travels along."),
             ("Sound waves are transverse.",
              "Sound waves travelling through air are longitudinal."),
             ("In a longitudinal wave the particles travel along with the wave.",
              "They vibrate back and forth about one place, parallel to the direction of travel."),
         ]}]},
    ],
    "key_fact": "In a transverse wave the oscillations are at right angles to the direction the "
                "wave travels. In a longitudinal wave they are parallel to it, and the wave shows "
                "areas of compression and rarefaction. For ripples on water and sound in air, it "
                "is the wave that travels, and not the water or the air.",
    "deeper": [
        {"kind": "card", "title": "Both types on a slinky",
         "body": ["Stretch a slinky spring along a bench.",
                  {"points": [
                      "Move one end from side to side: a transverse wave travels along it.",
                      "Push and pull one end along the spring: a longitudinal wave travels along "
                      "it, with compressions and rarefactions.",
                  ]}]},
        {"kind": "card", "title": "Seismic waves", "routes": ["TH"],
         "body": ["Earthquakes make two kinds of seismic wave.",
                  {"points": ["P-waves are longitudinal.", "S-waves are transverse."]},
                  "You use them in the lesson on waves for detection and exploration."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe the difference</strong>: say the direction of the oscillations "
             "compared with the direction of travel, for both types of wave.",
             "<strong>Describe evidence</strong>: say what you would see, and what it shows.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the direction of the oscillations in a transverse wave, compared with "
                       "the direction the wave travels.",
             "why": "In a transverse wave the oscillations are at right angles to the direction of "
                    "travel.",
             "options": [
                 {"text": "At right angles to it", "correct": True},
                 {"text": "Parallel to it", "correct": False,
                  "reply": "That is a longitudinal wave."},
                 {"text": "In the opposite direction", "correct": False,
                  "reply": "The oscillations go back and forth across the direction of travel, at "
                           "right angles to it."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Identify the longitudinal wave.",
             "why": "Sound waves travelling through air are longitudinal.",
             "options": [
                 {"text": "Ripples on water", "correct": False,
                  "reply": "Ripples on a water surface are transverse."},
                 {"text": "Sound waves in air", "correct": True},
                 {"text": "Light waves in air", "correct": False,
                  "reply": "Light is an electromagnetic wave. Electromagnetic waves are "
                           "transverse."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the region of a longitudinal wave where the particles are closest "
                       "together.",
             "why": "A compression is a region where the particles are closer together.",
             "options": [
                 {"text": "Rarefaction", "correct": False,
                  "reply": "In a rarefaction the particles are further apart."},
                 {"text": "Compression", "correct": True},
                 {"text": "Oscillation", "correct": False,
                  "reply": "An oscillation is the back and forth movement itself."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "A wave travelling along a slinky shows compressions and rarefactions. "
                       "Identify the type of wave.",
             "why": "Longitudinal waves show areas of compression and rarefaction.",
             "options": [
                 {"text": "Transverse", "correct": False,
                  "reply": "A transverse wave has no compressions or rarefactions."},
                 {"text": "Longitudinal", "correct": True},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how a sound wave travels from a loudspeaker to your ear. Put the "
                       "links in order.",
             "links": ["The loudspeaker cone vibrates back and forth.",
                       "It pushes and pulls on the air next to it, making compressions and "
                       "rarefactions.",
                       "Each layer of air pushes on the next, so the compressions and rarefactions "
                       "travel to your ear."],
             "herrings": [{"text": "The air travels from the loudspeaker to your ear.",
                           "why": "The air vibrates about the same place. Only the wave travels."},
                          {"text": "The air particles vibrate at right angles to the direction "
                                   "the sound travels.",
                           "why": "That would be a transverse wave. Sound in air is longitudinal."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain what a floating cork shows about ripples on water. Put the links "
                       "in order.",
             "links": ["Ripples pass under a cork floating on the water.",
                       "The cork bobs up and down but stays in the same place.",
                       "So the water is not carried along: it is the wave that travels."],
             "herrings": [{"text": "The cork is carried along to the edge of the tank.",
                           "why": "It stays in the same place. The ripples pass under it."},
                          {"text": "The cork moves back and forth along the direction of the "
                                   "ripples, so ripples are longitudinal.",
                           "why": "It moves up and down, at right angles to the direction of "
                                  "travel. Ripples are transverse."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe the differences between transverse and longitudinal waves. Give "
                       "an example of each.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Both directions of oscillation described "
                  "against the direction of travel, compressions and rarefactions named, and a "
                  "correct example of each.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One type described, or examples with no "
                  "description.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Transverse: the oscillations are at right angles to the direction of travel.",
                        "Longitudinal: the oscillations are parallel to the direction of travel.",
                        "Longitudinal waves show areas of compression and rarefaction.",
                        "Example of a transverse wave: ripples on a water surface (or light).",
                        "Example of a longitudinal wave: sound waves travelling through air."],
             "reject": ["“In a transverse wave the particles move along with the wave.”",
                        "“Sound is a transverse wave.”"]},
        ],
    },
}
