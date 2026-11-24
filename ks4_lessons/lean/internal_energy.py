# -*- coding: utf-8 -*-
"""Internal energy, in the lean shape. Spec table: ks4-internal-energy.md (AQA 8464 6.3.2.1 /
8463 4.3.2.1, word for word the same). No HT-only or physics-only line. Every route gets the same
lesson.

LEGACY (batch 2, Ks4Ladder). The ladder (r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank): five per route, both old stems kept word
for word. The cooling curve (`coolFig`) is drawn by the legacy logic with no state, so the card
places it through a legacy-fig slot.

LOGIC_EDITS:
  1. The Combined eyebrow read "AQA Physics (8464) 6.3.2.1": 8464 is AQA Combined Science, so it
     is written as the other lean physics pages write it.
  2. Rung 1 was practice question 1 (K.find on "Its temperature stays constant for several
     minutes"), so a pupil met it twice. It is now its own question, the definition of internal
     energy, through K.item, as metal-hydroxides did on 22 Nov 2026. Its position, and so its id
     (ks4:internal-energy:<route>#r1), is kept; its options and answer key are new."""

LOGIC_EDITS = [
    ("'AQA Physics (8464) 6.3.2.1 · Model'", "'AQA Combined Science (8464) 6.3.2.1 · Model'"),
    ("r1: Object.assign(K.find(slug, R.route, 'Its temperature stays constant for several "
     "minutes') || { options: [] }, { command: 'Identify', marks: 1, why: 'At constant power, a "
     "flat section means a change of state: the energy raises the particles’ potential energy, not "
     "their kinetic energy.' }),",
     "r1: Object.assign(K.item({ q: 'Define the internal energy of a system.', opts: [['The total "
     "kinetic energy and potential energy of all the particles in the system', true], ['The "
     "average kinetic energy of the particles that make up the system', false], ['The energy "
     "needed to raise the temperature of 1 kg of the system by 1 °C', false], ['The total kinetic "
     "energy of all the particles, not counting their potential energy', false]], "
     "wrong_explanations: { '1': 'The average kinetic energy is linked to the temperature. "
     "Internal energy is a total, of kinetic and potential energy.', '2': 'That is specific heat "
     "capacity.', '3': 'Internal energy includes the potential energy of the particles too.' } }), "
     "{ command: 'Define', marks: 1, why: 'Internal energy is the total kinetic energy and "
     "potential energy of all the particles (atoms and molecules) that make up a system.' }),"),
]

LESSON = {
    "slug": "internal-energy",
    "start": {
        "setup": "A pan of water is boiling. A thermometer in the water reads 100 °C. You turn the "
                 "heat up to full.",
        "question": "If you had to guess, does the thermometer reading go up, or stay at 100 °C?",
        "options": [
            ("It goes up",
             "It stays at 100 °C. The extra energy makes the water boil away faster. It goes "
             "into the particles' potential energy, and the temperature does not rise."),
            ("It stays at 100 °C",
             "It stays at 100 °C. The extra energy makes the water boil away faster. It goes "
             "into the particles' potential energy, and the temperature does not rise."),
        ],
        "answer": 1,
    },
    "words": ["internal energy", "kinetic energy", "potential energy", "change of state"],
    "knowledge": [
        {"kind": "card", "title": "Energy stored by particles",
         "body": ["Energy is stored inside a system by the particles (atoms and molecules) that "
                  "make up the system. This is called internal energy.",
                  {"points": [
                      "The particles move, so they have kinetic energy.",
                      "There are forces between the particles, so they also have potential "
                      "energy. It depends on how far apart they are.",
                  ]},
                  "Internal energy is the total kinetic energy and potential energy of all the "
                  "particles (atoms and molecules) that make up a system."]},
        {"kind": "card", "title": "What heating does",
         "body": ["Heating changes the energy stored within the system by increasing the energy "
                  "of the particles that make up the system. This either raises the temperature "
                  "of the system or produces a change of state.",
                  {"points": [
                      "The temperature rises: the particles move faster, so their kinetic energy "
                      "increases.",
                      "The state changes: the energy goes into the particles' potential energy. "
                      "The temperature stays the same until the change of state is complete.",
                  ]}]},
        {"kind": "reveal", "title": "Heating ice until it boils",
         "cols": ["Temperature", "Energy that increases"],
         "rows": [
             ("Ice warms from −10 °C to 0 °C", "Rises", "Kinetic"),
             ("Ice melts at 0 °C", "Stays at 0 °C", "Potential"),
             ("Water warms from 0 °C to 100 °C", "Rises", "Kinetic"),
             ("Water boils at 100 °C", "Stays at 100 °C", "Potential"),
         ]},
        {"kind": "card", "title": "Reading a cooling curve",
         "body": [{"slot": "legacy-fig:coolFig"},
                  "Energy leaves the substance all the time, so its internal energy falls along "
                  "the whole curve.",
                  {"points": [
                      "A sloping section: the temperature falls. The particles' kinetic energy "
                      "decreases.",
                      "A flat section: the substance changes state. The particles' potential "
                      "energy decreases, and the temperature stays the same.",
                      "B to C is the gas condensing at 90 °C. D to E is the liquid freezing at "
                      "40 °C.",
                  ]}]},
        {"kind": "card", "title": "Temperature and internal energy",
         "body": ["The temperature depends on the average kinetic energy of the particles. "
                  "Internal energy is the total energy of every particle, kinetic and potential.",
                  {"points": [
                      "A bath of warm water has more internal energy than a cup of hot tea. It "
                      "has far more particles.",
                      "1 kg of water at 0 °C has more internal energy than 1 kg of ice at 0 °C. "
                      "Melting raised the particles' potential energy.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Internal energy is the kinetic energy of the particles.",
              "It is the total kinetic energy and potential energy of all the particles."),
             ("Heating always makes the temperature rise.",
              "During a change of state the internal energy rises, but the temperature stays the "
              "same."),
             ("The hotter object always has more internal energy.",
              "Internal energy also depends on how many particles there are. A big, cool object "
              "can have more."),
         ]}]},
    ],
    "key_fact": "Internal energy is the total kinetic energy and potential energy of all the "
                "particles in a system. Heating increases the energy of the particles: it either "
                "raises the temperature or produces a change of state.",
    "deeper": [
        {"kind": "card", "title": "The two equations",
         "body": [{"points": [
             "Raising the temperature: ΔE = m c Δθ, in the lesson on specific heat capacity.",
             "Changing the state: E = m L, in the lesson on specific latent heat.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Determine</strong>: read it from the graph. A flat section gives a melting "
             "or boiling point.",
             "<strong>Describe</strong>: say what happens at each stage, in order, using the "
             "particles.",
             "<strong>Explain</strong>: link each step: energy in or out, which energy of the "
             "particles changes, what the temperature does.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
