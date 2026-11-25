# -*- coding: utf-8 -*-
"""Electromagnets, in the lean shape. Spec table: docs/lessons/wave2/ks3-electromagnets.md."""

LESSON = {
    "slug": "electromagnets",
    "start": {
        "setup": "A scrapyard crane lifts a car with a big flat disc. Then it drops the car into a skip.",
        "question": "If you had to guess, does the disc need electricity the whole time it holds the car, "
                    "or just a burst at the start?",
        "options": [
            ("The whole time",
             "Yes. The disc is an electromagnet. It is only a magnet while a current flows."),
            ("Just a burst at the start",
             "It needs a current the whole time. Switch the current off and the car drops."),
        ],
        "answer": 0,
    },
    "words": ["electromagnet", "coil", "iron core", "current"],
    "word_defs": {
        "electromagnet": "A magnet made by passing a current through a coil of wire. It can be switched off.",
        "coil": "Wire wound round and round in loops. Each loop is called a turn.",
        "iron core": "A piece of iron inside the coil. It makes the electromagnet much stronger.",
        "current": "The flow of charge round a circuit, measured in amps.",
    },
    "knowledge": [
        {"kind": "card", "title": "A current makes a magnetic field",
         "body": ["A wire with a current in it has a magnetic field around it.",
                  "This is called the magnetic effect of a current.",
                  "Around a single straight wire, the field is weak.",
                  "Wind the wire into a coil, and the fields of the turns add together.",
                  "The coil's field has the same shape as a bar magnet's field.",
                  "It has a north pole at one end and a south pole at the other."]},
        {"kind": "card", "title": "Making an electromagnet",
         "body": [{"figure": "p10-electromagnet-nail"},
                  {"points": ["Wind insulated wire many times round an iron nail.",
                              "Connect the ends of the wire to a cell and a switch.",
                              "Close the switch. A current flows and the nail becomes a strong magnet.",
                              "Dip the end of the nail in paper clips.",
                              "Count the clips it picks up, to see how strong it is."]}]},
        {"kind": "card", "title": "Features of an electromagnet",
         "body": ["An electromagnet is a coil of wire with a current in it.",
                  "It usually has an iron core inside the coil.",
                  "It is only magnetic while the current flows.",
                  "Switch the current off, and the magnetism goes.",
                  "Reverse the current, and the north and south poles swap ends."]},
        {"kind": "reveal", "title": "Changing an electromagnet",
         "cols": ["What happens", "Why"],
         "rows": [
             ("More turns on the coil", "Stronger", "Each turn adds its own field"),
             ("More current", "Stronger", "More current makes a stronger field"),
             ("Iron core added", "Much stronger", "The coil magnetises the iron"),
             ("Plastic core instead of iron", "Weaker", "Plastic is not magnetic"),
             ("Current switched off", "No magnetism", "No current means no field"),
             ("Current reversed", "Poles swap ends", "The field points the other way"),
         ]},
        {"kind": "card", "title": "Why the core is soft iron",
         "body": ["Soft iron becomes a strong magnet easily.",
                  "It loses almost all its magnetism as soon as the current stops.",
                  "A steel core would stay magnetised.",
                  "Then the electromagnet would not switch off properly."]},
        {"kind": "card", "title": "Using electromagnets",
         "body": ["Electromagnets are useful because they can be switched on and off.",
                  "A scrapyard crane lifts a car, then drops it when the current is switched off.",
                  "Electric bells, relays and loudspeakers also use electromagnets."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The iron core makes the magnetism. The coil just holds it.",
              "The current in the coil makes the field. The iron makes it stronger.", "MAG-13"),
             ("More turns make it stronger because more current flows.",
              "Each turn adds its own field. More turns do not make more current flow.", "MAG-14"),
             ("Switching off leaves a weak field that slowly drains away.",
              "The field goes as soon as the current stops.", "MAG-15"),
             ("Once the iron core is magnetised, it stays a magnet.",
              "Soft iron loses almost all its magnetism when the current stops.", "MAG-16"),
             ("Any metal core makes an electromagnet stronger.",
              "Only a magnetic material, such as iron, makes it stronger."),
         ]}]},
    ],
    "key_fact": "An electromagnet is a coil of wire with a current in it. "
                "It usually has an iron core. "
                "It is only magnetic while the current flows. "
                "More turns, more current and an iron core make it stronger.",
    "deeper": [
        {"kind": "card", "title": "Fire doors",
         "body": ["Some fire doors are held open by an electromagnet on the wall.",
                  "A current flows through it while the building is safe.",
                  "The fire alarm cuts the current, so the field goes and the door closes.",
                  "A power cut also lets the door close, so it fails safe."]},
        {"kind": "card", "title": "Relays",
         "body": ["A relay uses a small current to switch on a much bigger one.",
                  "The small current makes an electromagnet pull an iron switch closed.",
                  "A car's starter motor is switched on this way."]},
    ],
    "try": None,
    "tutor_body": "Want to check what makes an electromagnet stronger?",
    "ks4_becomes": "The field pattern round a coil, and how motors and transformers use it.",
    "safety_note": "The coil can get hot. Switch off between tries and let it cool. "
                   "Use only the low-voltage supply your teacher gives you.",
    "figures": [
        {"id": "p10-electromagnet-nail", "kind": "diagram", "status": "drawn", "art": "p10-electromagnet",
         "title": "A simple electromagnet picking up paper clips",
         "desc": "An iron core lies across the top with a coil of wire wound round its middle. Wires "
                 "from the two ends of the coil run down to a circuit with a cell and a closed switch. "
                 "A chain of three paper clips hangs from the right-hand end of the core.",
         "caption": "Close the switch, and the iron core picks up the clips.",
         "data": {"turns": 9}},
    ],
    "ladder_stem": {
        "explain": "A scrapyard crane uses an electromagnet instead of a strong permanent magnet. "
                   "Explain why. Say what the iron core is for.",
        "produce": "A school fire door is held open by an electromagnet on the wall. It closes by itself "
                   "when the fire alarm sounds. Explain how the alarm makes the door close. "
                   "Explain why this is safer than a catch that someone has to release.",
    },
    "ladder_feedback": {
        "recall": {
            1: "That does help. With the same current, more turns give a stronger field.",
            2: "That does help. More current through the coil makes a stronger field.",
            3: "That helps a lot. An iron core is the biggest change you can make.",
        },
        "apply": {
            0: "Soft iron is chosen because it does not stay magnetised.",
            1: "Nothing is stored to drain away. The field goes when the current stops.",
            2: "There are no poles once the current stops. And a south pole attracts clips too.",
        },
    },
}
