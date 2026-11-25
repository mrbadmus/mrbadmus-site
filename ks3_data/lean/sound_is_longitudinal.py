# -*- coding: utf-8 -*-
"""Sound is longitudinal, in the lean shape. Spec table: docs/lessons/wave2/ks3-sound-is-longitudinal.md."""

LESSON = {
    "slug": "sound-is-longitudinal",
    "start": {
        "setup": "A slinky lies stretched out on the floor. You push one end forward and pull it back. "
                 "A squashed-up patch of coils runs along it.",
        "question": "If you had to guess, as the squashed-up patch passes, does "
                    "each coil shuffle along and back, or stay where it is?",
        "options": [
            ("Shuffle along and back",
             "Yes. Each coil moves a little way along and back, then stops where it began."),
            ("Stay where it is",
             "A coil has to move to get squashed. It shuffles along and back, then stops."),
        ],
        "answer": 0,
    },
    "words": ["longitudinal", "compression", "rarefaction", "transverse"],
    "word_defs": {
        "longitudinal": "A wave where the material moves back and forth along the direction of travel.",
        "compression": "A place where the particles are squashed closer together.",
        "rarefaction": "A place where the particles are spread further apart.",
        "transverse": "A wave where the material moves at right angles to the direction of travel.",
    },
    "knowledge": [
        {"kind": "card", "title": "Two kinds of wave",
         "body": [{"figure": "p6-04-transverse"},
                  "In a transverse wave, the material moves at right angles to the direction of travel.",
                  "Shake a slinky up and down and a transverse wave runs along it.",
                  "In a longitudinal wave, the material moves back and forth along the direction of travel.",
                  "Push and pull the end of the slinky and a longitudinal wave runs along it.",
                  "In both kinds, the wave carries energy and the material stays where it was."]},
        {"kind": "card", "title": "Sound is longitudinal",
         "body": [{"figure": "p6-04-sound"},
                  "A loudspeaker cone moves forward and squashes the air in front of it.",
                  "This squashed region is a compression.",
                  "The cone moves back and leaves a region where the air is spread out.",
                  "This spread-out region is a rarefaction.",
                  "Compressions and rarefactions travel away from the loudspeaker. That is the sound wave.",
                  "Each layer of air moves back and forth, then ends where it started."]},
        {"kind": "reveal", "title": "Transverse and longitudinal",
         "cols": ["Transverse", "Longitudinal"],
         "rows": [
             ("Which way it vibrates", "Across the direction of travel",
              "Along the direction of travel"),
             ("What you see", "Crests and troughs", "Compressions and rarefactions"),
             ("Examples", "Water waves, light, a shaken rope", "Sound, a pushed slinky"),
         ]},
        {"kind": "card", "title": "Wavelength and amplitude of sound",
         "body": ["A sound wave has a wavelength.",
                  "It is the distance from one compression to the next compression.",
                  "A sound wave also has an amplitude.",
                  "It is how far each layer of air moves from its rest position."]},
        {"kind": "card", "title": "Why sound is drawn as a wavy line",
         "body": ["Sound is often drawn as a wavy line.",
                  "The line is a graph. It shows how squashed the air is at each place.",
                  "The peaks are compressions. The dips are rarefactions.",
                  "The air itself moves back and forth, along the direction of travel."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Sound is transverse, because it is drawn as a wavy line.",
              "Sound is longitudinal. The wavy line is only a graph.", "WAVE-13"),
             ("In a compression, the air travels to your ear.",
              "Only the compression travels. Each layer of air moves back and forth.", "WAVE-14"),
             ("A longitudinal wave has no amplitude, because it has no crests.",
              "It has an amplitude: how far each layer of air moves from its rest position.", "WAVE-15"),
             ("A compression is made by heating the air.",
              "A compression is made by squashing the air. The particles are pushed closer together.",
              "WAVE-16"),
             ("The wavelength of sound runs from a compression to a rarefaction.",
              "The wavelength runs from one compression to the next compression."),
         ]}]},
    ],
    "key_fact": "Sound is longitudinal: the air moves back and forth along the direction of travel. "
                "This makes compressions, where the air is squashed, and rarefactions, where it is spread out.",
    "deeper": [
        {"kind": "card", "title": "Earthquake waves",
         "body": ["An earthquake sends both kinds of wave through the Earth.",
                  "P waves are longitudinal. S waves are transverse.",
                  "S waves cannot travel through liquids.",
                  "This helped scientists work out that the Earth's outer core is liquid."]},
        {"kind": "card", "title": "Water waves are a mix",
         "body": ["Water waves are not purely transverse.",
                  "Each patch of water moves round a small circle.",
                  "So it moves a little along, as well as up and down."]},
    ],
    "try": {"label": "Wave Motion Lab", "href": "/simulations/physics/wave-motion-lab/"},
    "ks4_becomes": "Comparing transverse and longitudinal waves, wave speed in different materials, "
                   "and earthquake waves.",
    "figures": [
        {"id": "p6-04-transverse", "kind": "diagram", "status": "drawn", "art": "p6-transverse-wave",
         "title": "A transverse wave on a slinky",
         "desc": "A wave drawn on a dashed rest line, with an arrow along the top showing the direction "
                 "of travel, to the right. One coil is marked with a dot. A double arrow through the dot "
                 "points up and down, across the direction of travel. Words under the wave say each coil "
                 "moves up and down, and the wave travels along, at right angles.",
         "caption": "Transverse: each coil moves across the direction of travel.",
         "data": {"show": "motion", "motion_label": "Each coil moves up and down.",
                  "travel_note": "The wave travels along, at right angles."}},
        {"id": "p6-04-sound", "kind": "diagram", "status": "drawn", "art": "p6-longitudinal",
         "title": "A sound wave in front of a loudspeaker",
         "desc": "A loudspeaker on the left. In front of it, the air is drawn as a row of upright lines. "
                 "In some places the lines are squashed close together: these are labelled compression. In "
                 "between, the lines are spread apart: one is labelled rarefaction. A double arrow from one "
                 "compression to the next is labelled wavelength. An arrow along the top shows the sound "
                 "travelling to the right. One layer of air is marked, with a double arrow pointing left "
                 "and right: it moves back and forth.",
         "caption": "Longitudinal: each layer of air moves back and forth along the direction of travel.",
         "data": {}},
    ],
    "figure_caption": {"p6-04-transverse": None, "p6-04-sound": None},   # the card text already says it
    "ladder_ticks": [
        ["Gives one real limitation — for example: the queue is one line rather than air spreading in every direction, people move a long way compared with air, or a person choosing to step forward is not the same as being pushed.",
         "Gives one real limitation, such as: the queue is one line, or people choose when to step."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Longitudinal is about how the material moves. It is not about the wave's shape.",
            1: "Moving at right angles is transverse. Transverse waves have crests and troughs.",
            2: "No wave carries its material along. Each layer moves back and forth.",
        },
        "apply": {
            1: "Drawing sound as a wavy line is fine. The line is a graph.",
            2: "The air moves back and forth along the direction of travel, never up and down.",
            3: "The air moves along the direction of travel everywhere, even near the loudspeaker.",
        },
    },
}
