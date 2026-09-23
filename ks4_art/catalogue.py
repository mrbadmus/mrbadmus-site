"""ks4_art.catalogue — the declarative KS4 figure list.

Not a module `build_figures.py` merges through the registry (see
`ks4_art/__init__.py::discover`, which excludes this file by name): a
catalogue record names an `art` key, it does not implement one, so it lives
outside the `ART`-table discovery it feeds.

Every id is prefixed `ks4-fig-` and matches `[a-z0-9-]+`, per the figure
contract. Every record carries `title` (short — this BECOMES the alt text)
and `desc` (a longer description for a screen reader), per Mide's rule:
alt text says WHAT IS SHOWN, never the answer. Where a figure is a single
AQA symbol that a question asks the pupil to NAME, the title/desc describe
its GEOMETRY only — "a rectangle with a diagonal arrow drawn across it" —
never the component's name.

Started with the biggest confirmed cluster from the diagrams audit: KS4
physics electricity/circuit-symbols (43 of the 110 confirmed rows). This is
a STARTER set proving every drawer end to end, not a byte-for-byte mapping
of all 43 rows — wiring a specific question id to a figure id is content
work for the authoring pass, not this ticket.
"""

CATALOGUE = [
    # ── the AQA symbol palette, standalone — the "name this component"
    # family (e.g. ks4-circuit-symbols-e01, -e07, -e09 … -h02) ────────────
    {
        "id": "ks4-fig-circuit-symbol-resistor",
        "art": "circuit-symbol-resistor",
        "title": "Circuit symbol: a plain rectangle in the wire, with no other mark on it.",
        "desc": "A rectangle drawn in a wire. Nothing else is drawn on or "
                "near the rectangle.",
    },
    {
        "id": "ks4-fig-circuit-symbol-fuse",
        "art": "circuit-symbol-fuse",
        "title": "Circuit symbol: a rectangle with a straight line running "
                 "along its length, the line sticking out a little beyond "
                 "each end.",
        "desc": "A rectangle drawn in a wire, with a thin straight line "
                "passing horizontally through its middle and continuing a "
                "short distance beyond the rectangle on both sides.",
    },
    {
        "id": "ks4-fig-circuit-symbol-variable-resistor",
        "art": "circuit-symbol-variable-resistor",
        "title": "Circuit symbol: a rectangle with a diagonal arrow drawn across it.",
        "desc": "A rectangle drawn in a wire, with a straight diagonal line "
                "running from the lower-left corner area to the upper-right "
                "corner area, ending in an arrowhead.",
    },
    {
        "id": "ks4-fig-circuit-symbol-thermistor",
        "art": "circuit-symbol-thermistor",
        "title": "Circuit symbol: a rectangle with a line that runs along "
                 "near the bottom and turns upward at the right-hand end.",
        "desc": "A rectangle drawn in a wire. A line enters at the lower "
                "left, runs roughly horizontally through the rectangle, "
                "then bends and runs upward at the right-hand end, with no "
                "arrowhead anywhere on it.",
    },
    {
        "id": "ks4-fig-circuit-symbol-ldr",
        "art": "circuit-symbol-ldr",
        "title": "Circuit symbol: a rectangle with two separate arrows "
                 "pointing in towards it from outside.",
        "desc": "A rectangle drawn in a wire, with two short diagonal "
                "arrows above it, both pointing down and in towards the "
                "rectangle, side by side.",
    },
    {
        "id": "ks4-fig-circuit-symbol-lamp",
        "art": "circuit-symbol-lamp",
        "title": "Circuit symbol: a circle with a cross drawn inside it.",
        "desc": "A circle drawn in a wire, with an X shape — two crossing "
                "diagonal lines — drawn inside it.",
    },
    {
        "id": "ks4-fig-circuit-symbol-diode",
        "art": "circuit-symbol-diode",
        "title": "Circuit symbol: a triangle pointing along the wire, with "
                 "a short bar drawn across its tip.",
        "desc": "A filled or outlined triangle sitting in the wire, "
                "pointing in the direction of the wire, with a short "
                "straight bar drawn across the triangle's tip.",
    },
    {
        "id": "ks4-fig-circuit-symbol-led",
        "art": "circuit-symbol-led",
        "title": "Circuit symbol: a triangle-and-bar shape with two small "
                 "arrows pointing away from it.",
        "desc": "The same triangle-and-bar shape as a diode, with two "
                "short arrows drawn near it pointing away and outward, "
                "on the side away from the wire.",
    },
    {
        "id": "ks4-fig-circuit-symbol-ammeter",
        "art": "circuit-symbol-ammeter",
        "title": "Circuit symbol: a circle with the letter A inside it.",
        "desc": "A circle drawn in the wire with the capital letter A "
                "printed in its centre.",
    },
    {
        "id": "ks4-fig-circuit-symbol-voltmeter",
        "art": "circuit-symbol-voltmeter",
        "title": "Circuit symbol: a circle with the letter V inside it.",
        "desc": "A circle drawn in the wire with the capital letter V "
                "printed in its centre.",
    },
    {
        "id": "ks4-fig-circuit-symbol-motor",
        "art": "circuit-symbol-motor",
        "title": "Circuit symbol: a circle with the letter M inside it.",
        "desc": "A circle drawn in the wire with the capital letter M "
                "printed in its centre.",
    },
    {
        "id": "ks4-fig-circuit-symbol-ac-supply",
        "art": "circuit-symbol-ac-supply",
        "title": "Circuit symbol: a circle with a wavy (sine-shaped) line drawn inside it.",
        "desc": "A circle drawn in the wire with one smooth up-and-down "
                "wave drawn across its middle.",
    },
    {
        "id": "ks4-fig-circuit-symbol-cell",
        "art": "circuit-symbol-cell",
        "title": "Circuit symbol: one long thin line and one short thick "
                 "line, side by side, in the wire.",
        "desc": "Two short vertical lines drawn close together across the "
                "wire: one longer and thin, the other shorter and thicker.",
    },
    {
        "id": "ks4-fig-circuit-symbol-battery-2",
        "art": "circuit-symbol-battery",
        "title": "Circuit symbol: two long-and-short line pairs joined end to end.",
        "desc": "Two long-thin-line-and-short-thick-line pairs, drawn one "
                "after the other across the wire.",
        "cells": 2,
    },
    {
        "id": "ks4-fig-circuit-symbol-battery-3",
        "art": "circuit-symbol-battery",
        "title": "Circuit symbol: three long-and-short line pairs joined end to end.",
        "desc": "Three long-thin-line-and-short-thick-line pairs, drawn one "
                "after the other across the wire.",
        "cells": 3,
    },
    {
        "id": "ks4-fig-circuit-symbol-switch-open",
        "art": "circuit-symbol-switch-open",
        "title": "Circuit symbol: two small circles in the wire with a "
                 "straight line resting near one of them, not touching the other.",
        "desc": "Two small filled circles in the wire, a short distance "
                "apart, with a straight line running from one circle up "
                "and away, not reaching the other circle — the wire is "
                "broken here.",
    },
    {
        "id": "ks4-fig-circuit-symbol-switch-closed",
        "art": "circuit-symbol-switch-closed",
        "title": "Circuit symbol: two small circles in the wire joined by "
                 "a straight line touching both.",
        "desc": "Two small filled circles in the wire, a short distance "
                "apart, with a straight line joining them so the wire is "
                "unbroken.",
    },

    # ── whole circuits — the majority of the confirmed rows ───────────────
    {
        "id": "ks4-fig-circuit-fuse-in-supply-wire",
        "art": "circuit",
        "title": "A single loop with a cell, a rectangle with a line "
                 "through it in the wire leaving the cell, and a lamp.",
        "desc": "One rectangular wire loop. A cell sits on the left side. "
                "Along the top wire, first a rectangle with a straight "
                "line through its length, then a lamp symbol (a circle "
                "with a cross inside it).",
        "w": 380, "h": 240,
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "fuse", "id": "fuse"},
                    {"symbol": "lamp", "id": "lamp"}],
        },
    },
    {
        "id": "ks4-fig-circuit-wire-short-of-cell",
        "art": "circuit",
        "title": "A single loop with a cell, a rectangle with a line "
                 "through it, and a lamp — but one wire does not quite "
                 "reach the cell.",
        "desc": "The same loop as the fuse circuit above, except the wire "
                "returning to the cell stops just short of it, leaving a "
                "small gap — the circuit is not actually complete.",
        "w": 380, "h": 240,
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "fuse", "id": "fuse"},
                    {"symbol": "lamp", "id": "lamp"}],
            "gap": {"after": "return"},
        },
    },
    {
        "id": "ks4-fig-circuit-ammeter-voltmeter-resistor",
        "art": "circuit",
        "title": "A single loop with a cell, a circle with the letter A, "
                 "and a rectangle — with a second circle, carrying the "
                 "letter V, connected across the rectangle on a short pair "
                 "of wires.",
        "desc": "One rectangular wire loop with a cell, then a circle "
                "marked A, then a plain rectangle, all in series around "
                "the loop. A second circle, marked V, is joined to the "
                "loop by two short wires that bridge across the rectangle "
                "only, rather than sitting in the main loop itself.",
        "w": 420, "h": 260,
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "ammeter", "id": "amm"},
                    {"symbol": "resistor", "id": "r1"}],
            "meters_across": [{"symbol": "voltmeter", "target": "r1"}],
        },
    },
    {
        "id": "ks4-fig-circuit-two-branches-lamp-motor",
        "art": "circuit",
        "title": "A battery and a switch feeding two branches — one with a "
                 "circle with a cross, one with a circle with the letter "
                 "M — with a circle marked A before the branches split.",
        "desc": "A battery symbol (three long-and-short line pairs) and a "
                "closed switch sit on the top wire, followed by a circle "
                "marked A, before the wire splits into two parallel "
                "branches: one branch holds a lamp symbol, the other a "
                "circle with the letter M.",
        "w": 460, "h": 300,
        "circuit": {
            "topology": "parallel",
            "supply": [{"symbol": "battery", "id": "bat", "cells": 3},
                      {"symbol": "switch", "id": "sw", "state": "closed"},
                      {"symbol": "ammeter", "id": "amm-total"}],
            "branches": [
                ("lamp-branch", [{"symbol": "lamp", "id": "lamp1"}]),
                ("motor-branch", [{"symbol": "motor", "id": "motor1"}]),
            ],
        },
    },
    {
        "id": "ks4-fig-circuit-single-loop-four-components",
        "art": "circuit",
        "title": "A single loop with a cell, a circle with the letter A, "
                 "a rectangle with a diagonal arrow, and a circle with a cross.",
        "desc": "One rectangular wire loop carrying, in order, a cell, a "
                "circle marked A, a rectangle with a diagonal arrow drawn "
                "across it, and a circle with a cross drawn inside it.",
        "w": 420, "h": 260,
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "ammeter", "id": "amm"},
                    {"symbol": "variable-resistor", "id": "vr"},
                    {"symbol": "lamp", "id": "lamp"}],
        },
    },

    # ── one worked example from each other module, proving the merged
    # registry end to end ─────────────────────────────────────────────────
    {
        "id": "ks4-fig-graph-distance-time-runner",
        "art": "graph-distance-time",
        "title": "A distance–time graph: a line rising steeply from the "
                 "origin, then curving to become gradually less steep.",
        "desc": "A distance-against-time graph. The line starts at the "
                "origin and rises steeply and straight at first, then "
                "curves so that it becomes gradually less steep as time "
                "goes on, without ever going flat.",
        "series": [(0, 0), (2, 8), (4, 13), (6, 16), (8, 17.5), (10, 18.2)],
        "x_range": (0, 10), "y_range": (0, 20),
    },
    {
        "id": "ks4-fig-resolution-triangle-generic",
        "art": "resolution-triangle",
        "title": "A right-angled triangle with a labelled diagonal side and "
                 "two labelled shorter sides, with a small square marking "
                 "the right angle.",
        "desc": "A right-angled triangle. The longest side (the "
                "hypotenuse) is labelled F. The horizontal side is "
                "labelled F cos θ and the vertical side is labelled F sin "
                "θ. A small square is drawn in the corner where the "
                "horizontal and vertical sides meet, marking the right "
                "angle. The angle θ is marked where the hypotenuse meets "
                "the horizontal side.",
        "angle": 35, "hyp_label": "F", "horiz_label": "F cos θ",
        "vert_label": "F sin θ", "angle_label": "θ",
    },
    {
        "id": "ks4-fig-molecule-h2o-dot-cross",
        "art": "molecule-h2o",
        "title": "A dot-and-cross diagram of a water molecule.",
        "desc": "A dot-and-cross diagram showing one oxygen atom bonded to "
                "two hydrogen atoms. Each O–H bond is shown as one dot and "
                "one cross together between the two atoms' outer shells. "
                "The oxygen atom carries two further pairs of dots, each "
                "pair not shared with a hydrogen atom.",
    },
]
