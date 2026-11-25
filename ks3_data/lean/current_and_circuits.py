# -*- coding: utf-8 -*-
"""Current and circuits, in the lean shape. Spec table: docs/lessons/wave2/ks3-current-and-circuits.md."""

LESSON = {
    "slug": "current-and-circuits",
    "start": {
        "setup": "A torch joins a cell and a bulb in a ring of metal strips. "
                 "Cut the ring on the way to the bulb and the bulb goes dark.",
        "question": "If you had to guess, what happens if you cut it on the way back from the bulb instead?",
        "options": [
            ("The bulb still lights",
             "It goes dark too. The current flows round the whole ring, so a gap anywhere stops it."),
            ("The bulb goes dark",
             "Right. The current flows round the whole ring, so a gap anywhere stops it."),
        ],
        "answer": 1,
    },
    "words": ["electric current", "circuit", "ammeter", "circuit symbol"],
    "word_defs": {
        "electric current": "A flow of charge. It is measured in amperes, or amps, written A.",
        "circuit": "A complete loop that charge can flow all the way round.",
        "ammeter": "The meter that measures current. It goes in the loop, in series.",
        "circuit symbol": "The agreed drawing for one part of a circuit, such as a lamp.",
    },
    "knowledge": [
        {"kind": "card", "title": "What a current is",
         "body": ["An electric current is a flow of charge.",
                  "In a metal wire, the charge is carried by tiny particles called electrons.",
                  "The electrons are already in the wire before you switch on.",
                  "A cell pushes on all of them at once, so they all move together.",
                  "The cell also gives the charge energy to carry round the circuit."]},
        {"kind": "card", "title": "A complete circuit",
         "body": [{"figure": "p8-l1-open"},
                  "A current only flows round a complete loop, called a circuit.",
                  "Here the switch is open, so there is a gap in the loop.",
                  "No current flows anywhere, and the lamp is off.",
                  "A gap after the lamp stops the current just as a gap before it does."]},
        {"kind": "reveal", "title": "Switch open and switch closed",
         "cols": ["Switch open", "Switch closed"],
         "rows": [
             ("Is the loop complete", "No, there is a gap", "Yes, there is no gap"),
             ("Current", "None, anywhere in the loop", "Flows all the way round"),
             ("The lamp", "Off", "On"),
         ]},
        {"kind": "card", "title": "Symbols for supplying and switching",
         "body": [{"figure": "p8-l1-symbols-supply"},
                  "A circuit diagram uses an agreed symbol for each part.",
                  "Then anyone can build the same circuit from the same diagram.",
                  "On a cell, the long line is the positive end.",
                  "A battery is two or more cells joined together."]},
        {"kind": "card", "title": "Symbols for using and measuring",
         "body": [{"figure": "p8-l1-symbols-use"},
                  "A lamp gives out light when a current flows through it.",
                  "A resistor makes it harder for the current to flow.",
                  "A variable resistor is one you can change, as in a dimmer switch.",
                  "An ammeter measures current. A voltmeter measures potential difference, or voltage."]},
        {"kind": "card", "title": "Drawing a circuit diagram",
         "body": [{"figure": "p8-l1-drawn"},
                  {"points": ["Draw every part with its symbol, never as a picture.",
                              "Draw the wires as straight lines with a ruler.",
                              "Turn corners at right angles.",
                              "Leave no gaps in the wires, except at an open switch.",
                              "Mark each junction, where wires join, with a dot."]},
                  "To build it, start at the cell and follow the loop round.",
                  "Join each part to the next, in the same order as the diagram."]},
        {"kind": "card", "title": "Measuring current",
         "body": ["Current is measured in amperes, or amps, written A.",
                  "You measure it with an ammeter.",
                  "The ammeter goes in the loop, in series, so the current flows through it.",
                  "A torch bulb takes a few tenths of an amp, such as 0.30 A."]},
        {"kind": "card", "title": "The same all the way round",
         "body": [{"figure": "p8-l1-two-ammeters"},
                  "One ammeter is before the lamp and one is after it.",
                  "Both read 0.30 A.",
                  "In a single loop, the current is the same everywhere.",
                  "The lamp does not use up current.",
                  "It takes energy from the charge and gives it out as light and heat."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The lamp uses up some current, so less comes back.",
              "The current is the same on both sides of the lamp.", "CIRC-01"),
             ("The current has to travel from the cell to the lamp first.",
              "The wires are already full of electrons. They all start moving at once.", "CIRC-02"),
             ("Only the wire on the way to the lamp matters.",
              "A gap anywhere in the loop stops the current everywhere.", "CIRC-03"),
             ("A cell stores current and sends it out.",
              "A cell pushes the charge already in the wires, and gives it energy.", "CIRC-04"),
             ("An ammeter goes across a lamp.",
              "An ammeter goes in the loop, so the current flows through it."),
         ]}]},
    ],
    "key_fact": "An electric current is a flow of charge, measured in amps (A) with an ammeter. "
                "It only flows round a complete circuit. "
                "In a single loop, the current is the same everywhere.",
    "deeper": [
        {"kind": "card", "title": "Why the light comes on at once",
         "body": ["Each electron drifts very slowly, under a millimetre a second.",
                  "But the wire is full of electrons from end to end.",
                  "Closing the switch pushes on all of them at the same moment.",
                  "So a lamp lights at once, even at the end of a long cable."]},
        {"kind": "card", "title": "How many electrons",
         "body": ["One amp means about six million million million electrons pass a point each second.",
                  "Numbers that big are hard to use, so we measure current in amps."]},
        {"kind": "card", "title": "Which way the current goes",
         "body": ["On diagrams, current is shown flowing from the positive end of the cell.",
                  "This is called conventional current.",
                  "The electrons in the wire really drift the other way."]},
    ],
    "try": {"label": "Circuit Lab", "href": "/simulations/physics/circuit-lab/"},
    "tutor_body": "Not sure where an ammeter goes, or what a symbol means?",
    "connects_heading": None,
    "ks4_becomes": "Charge flow = current × time, and the coulomb as the unit of charge.",
    "connects": {
        "Current at a junction": "What the current does where a wire splits in two.",
        "Building and measuring a circuit": "Building circuits from diagrams and reading the meters.",
    },
    "figures": [
        {"id": "p8-l1-open", "kind": "diagram", "status": "drawn", "art": "p8-loop",
         "title": "A circuit with the switch open",
         "desc": "A circuit diagram: one loop drawn with straight lines. A lamp symbol is on the top "
                 "wire. A cell symbol and an open switch are on the bottom wire. The switch lever is "
                 "lifted away from its contact, so there is a gap in the loop.",
         "caption": "An open switch leaves a gap, so no current flows.",
         "data": {"top": [{"k": "lamp", "name": "lamp (off)"}],
                  "bottom": [{"k": "cell", "name": "cell"}, {"k": "switch-open", "name": "switch open"}],
                  "height": 110}},
        {"id": "p8-l1-symbols-supply", "kind": "diagram", "status": "drawn", "art": "p8-symbols",
         "title": "Circuit symbols for supplying and switching",
         "desc": "A table of six circuit symbols, each drawn on a short wire and named underneath. "
                 "Cell: a long line and a short line side by side, the long line is positive. "
                 "Battery: two cells joined. Switch open: a lever lifted away from its contact. "
                 "Switch closed: the lever lying on its contact. Wire: a plain straight line. "
                 "Junction: a wire joining another at a dot.",
         "caption": "The symbols for parts that supply, join and switch.",
         "data": {"symbols": ["cell", "battery", "switch-open", "switch-closed", "wire", "junction"]}},
        {"id": "p8-l1-symbols-use", "kind": "diagram", "status": "drawn", "art": "p8-symbols",
         "title": "Circuit symbols for using and measuring",
         "desc": "A table of five circuit symbols, each drawn on a short wire and named underneath. "
                 "Lamp: a circle with a cross inside. Resistor: a rectangle. Variable resistor: a "
                 "rectangle with an arrow through it. Ammeter: a circle with the letter A. "
                 "Voltmeter: a circle with the letter V.",
         "caption": "The symbols for parts that use and measure.",
         "data": {"symbols": ["lamp", "resistor", "variable-resistor", "ammeter", "voltmeter"]}},
        {"id": "p8-l1-drawn", "kind": "diagram", "status": "drawn", "art": "p8-loop",
         "title": "A circuit diagram for a cell, a switch and a lamp",
         "desc": "A circuit diagram drawn with straight lines and square corners. A lamp symbol is "
                 "on the top wire. A cell symbol and a closed switch are on the bottom wire. Each "
                 "part is named beside it.",
         "caption": "Straight lines, square corners and the right symbols.",
         "data": {"top": [{"k": "lamp", "name": "lamp"}],
                  "bottom": [{"k": "cell", "name": "cell"}, {"k": "switch-closed", "name": "switch"}],
                  "height": 110}},
        {"id": "p8-l1-two-ammeters", "kind": "diagram", "status": "drawn", "art": "p8-loop",
         "title": "Two ammeters, one each side of a lamp",
         "desc": "A circuit diagram of one loop. On the top wire there is an ammeter, then a lamp, "
                 "then a second ammeter. A cell and a closed switch are on the bottom wire. Both "
                 "ammeters read 0.30 A.",
         "caption": "Before the lamp and after it, the current is the same.",
         "data": {"top": [{"k": "ammeter", "reading": "0.30 A"}, {"k": "lamp"},
                          {"k": "ammeter", "reading": "0.30 A"}],
                  "bottom": [{"k": "cell"}, {"k": "switch-closed"}],
                  "height": 110}},
    ],
    "figure_caption": {"p8-l1-open": None, "p8-l1-two-ammeters": None},
    "ladder_stem": {
        "explain": "A torch bulb goes out when the metal strip behind it breaks. The strip "
                   "comes after the bulb in the loop. Explain why the bulb still goes out. "
                   "Use the words current, charge and loop.",
    },
    "ladder_ticks": [
        ["Says the position of the gap makes no difference — in front of the bulb or behind it, the bulb goes out.",
         "Says a gap before or after the bulb puts it out just the same."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Nothing is used up. The bulb takes energy, and the current is the same on both sides.",
            1: "If no charge came back, the loop would stop and the bulb would go out.",
            3: "A bulb does not speed the current up. One loop has one current.",
        },
        "apply": {
            1: "Each electron drifts very slowly. The push reaches them all at once because they are already there.",
            2: "There is no delay to see. The wire is full of electrons before the switch closes.",
            3: "A cell makes no electrons. It pushes the ones already in the wire.",
        },
    },
}
