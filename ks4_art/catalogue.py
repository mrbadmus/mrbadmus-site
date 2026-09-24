"""ks4_art.catalogue — the declarative KS4 figure list, drawn by figlib.

⊕ MRB-352 run 2. The drawers that used to live beside this file
(`ks4_art/circuits.py`, `forces.py`, `graphs.py`, `bonding*.py`,
`oscilloscope_compare.py`) are retired: Mide's diagram library, brought in
as `figlib/`, does every one of those jobs, in the house style, and is now
the ONE source of question figures. This file stays as the declarative
layer — ids, alt text, parameters — and every `art` names a builder in
`figlib.ART`. Content lanes still add `ks4_art/catalogue_<lane>.py` beside
it; `build_figures.py` discovers them all.

Every id is prefixed `ks4-fig-` and matches `[a-z0-9-]+`. Every record
carries `title` (short — this BECOMES the alt text) and `desc` (for a
screen reader), per Mide's rule: alt text says WHAT IS SHOWN, never the
answer. Where a figure is a single AQA symbol that a question asks the
pupil to NAME, the title/desc describe its GEOMETRY only.

Symbols are exactly the AQA 8463 v1.1 §4.2.1.1 (p.24) list. Retired with
the old drawers: the motor (not on the AQA list), the a.c. supply (not on
the AQA list) and the three-cell battery (AQA draws a battery as cell,
dashed wire, cell, whatever the count).
"""

CATALOGUE = [
    # ── the AQA symbol palette, standalone — the "name this component"
    # family ───────────────────────────────────────────────────────────────
    {
        "id": "ks4-fig-circuit-symbol-resistor",
        "art": "symbol", "params": {"key": "resistor"},
        "title": "Circuit symbol: a plain rectangle in the wire, with no other mark on it.",
        "desc": "A rectangle drawn in a wire. Nothing else is drawn on or "
                "near the rectangle.",
    },
    {
        "id": "ks4-fig-circuit-symbol-fuse",
        "art": "symbol", "params": {"key": "fuse"},
        "title": "Circuit symbol: a rectangle with the wire running straight "
                 "through it along its length.",
        "desc": "A rectangle drawn in a wire, with a thin straight line "
                "running horizontally through its middle from one end to "
                "the other, joining the wire on both sides.",
    },
    {
        "id": "ks4-fig-circuit-symbol-variable-resistor",
        "art": "symbol", "params": {"key": "variable_resistor"},
        "title": "Circuit symbol: a rectangle with a diagonal arrow drawn across it.",
        "desc": "A rectangle drawn in a wire, with a straight diagonal line "
                "that starts below and to the left of the rectangle, passes "
                "through it, and ends above and to the right of it in a "
                "solid arrowhead.",
    },
    {
        "id": "ks4-fig-circuit-symbol-thermistor",
        "art": "symbol", "params": {"key": "thermistor"},
        "title": "Circuit symbol: a rectangle with a diagonal line through "
                 "it, whose lower end turns into a short horizontal tail.",
        "desc": "A rectangle drawn in a wire. A straight diagonal line "
                "passes through it from below-left to above-right. At its "
                "lower-left end the line turns into a short horizontal tail "
                "pointing left. There is no arrowhead.",
    },
    {
        "id": "ks4-fig-circuit-symbol-ldr",
        "art": "symbol", "params": {"key": "ldr"},
        "title": "Circuit symbol: a small rectangle inside a circle, with two "
                 "arrows pointing in towards it.",
        "desc": "A circle sitting in a wire, the wire running into it to a "
                "small rectangle at its centre. Outside the circle, at its "
                "upper left, two short parallel arrows point down and to the "
                "right, in towards the circle.",
    },
    {
        "id": "ks4-fig-circuit-symbol-lamp",
        "art": "symbol", "params": {"key": "lamp"},
        "title": "Circuit symbol: a circle with a cross drawn inside it.",
        "desc": "A circle drawn in a wire, with an X shape — two crossing "
                "diagonal lines — drawn inside it.",
    },
    {
        "id": "ks4-fig-circuit-symbol-diode",
        "art": "symbol", "params": {"key": "diode"},
        "title": "Circuit symbol: a circle containing a triangle pointing "
                 "along the wire, with a short bar across its tip.",
        "desc": "A circle drawn in a wire. Inside it, the wire runs through "
                "an outlined triangle that points along the wire, and a "
                "short straight bar is drawn across the triangle's tip.",
    },
    {
        "id": "ks4-fig-circuit-symbol-led",
        "art": "symbol", "params": {"key": "led"},
        "title": "Circuit symbol: a circle containing a triangle and bar, "
                 "with two small arrows pointing away from it.",
        "desc": "The same circle, triangle and bar shape as the diode, with "
                "two short parallel arrows at its upper right pointing up "
                "and away from the circle.",
    },
    {
        "id": "ks4-fig-circuit-symbol-ammeter",
        "art": "symbol", "params": {"key": "ammeter"},
        "title": "Circuit symbol: a circle with the letter A inside it.",
        "desc": "A circle drawn in the wire with the capital letter A "
                "printed in its centre.",
    },
    {
        "id": "ks4-fig-circuit-symbol-voltmeter",
        "art": "symbol", "params": {"key": "voltmeter"},
        "title": "Circuit symbol: a circle with the letter V inside it.",
        "desc": "A circle drawn in the wire with the capital letter V "
                "printed in its centre.",
    },
    {
        "id": "ks4-fig-circuit-symbol-cell",
        "art": "symbol", "params": {"key": "cell"},
        "title": "Circuit symbol: one long line and one short line, side by "
                 "side across the wire, with a plus sign by the long line.",
        "desc": "Two short vertical lines drawn close together across the "
                "wire: one longer, one shorter. A small plus sign sits above "
                "and to the left of the longer line.",
    },
    {
        "id": "ks4-fig-circuit-symbol-battery-2",
        "art": "symbol", "params": {"key": "battery"},
        "title": "Circuit symbol: two pairs of lines — each a long line "
                 "beside a short line — joined by a dashed line, with a plus "
                 "sign by the first long line.",
        "desc": "Across the wire, a long line and a short line, then a short "
                "dashed length of wire, then another long line and short "
                "line. A small plus sign sits above and to the left of the "
                "first long line.",
    },
    {
        "id": "ks4-fig-circuit-symbol-switch-open",
        "art": "symbol", "params": {"key": "switch"},
        "title": "Circuit symbol: two small hollow circles in the wire, with "
                 "a straight line from one that is angled away from the other.",
        "desc": "Two small hollow circles in the wire, a short distance "
                "apart. A straight line starts at the left circle and angles "
                "away from the wire, ending short of the right circle, so "
                "there is a gap.",
    },
    {
        "id": "ks4-fig-circuit-symbol-switch-closed",
        "art": "symbol", "params": {"key": "switch_closed"},
        "title": "Circuit symbol: two small hollow circles in the wire joined "
                 "by a straight line touching both.",
        "desc": "Two small hollow circles in the wire, a short distance "
                "apart, with a straight line running from one to the other.",
    },

    # ── whole circuits ─────────────────────────────────────────────────────
    {
        "id": "ks4-fig-circuit-fuse-in-supply-wire",
        "art": "circuit",
        "params": {"netlist": [["fuse"], ["lamp"]], "left": [["cell"]]},
        "title": "A single loop with a cell, a rectangle with the wire "
                 "running through it, and a lamp.",
        "desc": "One rectangular wire loop. A cell sits on the left side. "
                "Along the top wire, first a rectangle with the wire running "
                "straight through its length, then a lamp symbol (a circle "
                "with a cross inside it).",
    },
    {
        "id": "ks4-fig-circuit-wire-short-of-cell",
        "art": "circuit",
        "params": {"netlist": [["cell"], ["fuse"], ["lamp"]], "gap": "start"},
        "title": "A single loop with a cell, a rectangle with the wire "
                 "running through it, and a lamp — but one wire does not "
                 "quite reach the cell.",
        "desc": "A cell, then a rectangle with the wire running through it, "
                "then a lamp, along the top of a loop. The wire coming back "
                "up the left side stops just short of the corner where the "
                "cell is, leaving a small gap.",
    },
    {
        "id": "ks4-fig-circuit-ammeter-voltmeter-resistor",
        "art": "circuit",
        "params": {"netlist": [["ammeter"], ["resistor", None, None,
                                              {"voltmeter": True}]],
                   "left": [["cell"]]},
        "title": "A single loop with a cell, a circle with the letter A, and "
                 "a rectangle — with a second circle, carrying the letter V, "
                 "connected across the rectangle on a short pair of wires.",
        "desc": "One rectangular wire loop with a cell on the left side, then "
                "a circle marked A and a plain rectangle along the top. A "
                "second circle, marked V, is joined to the top wire by two "
                "short wires, one either side of the rectangle, so it "
                "bridges the rectangle only.",
    },
    {
        "id": "ks4-fig-circuit-single-loop-four-components",
        "art": "circuit",
        "params": {"netlist": [["ammeter"], ["variable_resistor"], ["lamp"]],
                   "left": [["cell"]]},
        "title": "A single loop with a cell, a circle with the letter A, a "
                 "rectangle with a diagonal arrow, and a circle with a cross.",
        "desc": "One rectangular wire loop: a cell on the left side, then "
                "along the top a circle marked A, a rectangle with a "
                "diagonal arrow drawn across it, and a circle with a cross "
                "drawn inside it.",
    },

    # ── MRB-352 run 2 motor sweep (Mide: no circuit question may use a
    # motor symbol; no question may ask a pupil to describe a symbol or a
    # diagram in words). Each replaces a motor row's words with a drawing.
    {
        # ks4-circuit-symbols-s05 — a student's torch, the bulb drawn wrong
        "id": "ks4-fig-circuit-torch-ldr-for-bulb",
        "art": "circuit",
        "params": {"netlist": [["switch_closed"], ["ldr"]],
                   "left": [["battery"]]},
        "title": "A single loop with two pairs of long and short lines "
                 "joined by a dashed line, a switch whose lever joins both "
                 "contacts, and a small rectangle inside a circle with two "
                 "arrows pointing in towards it.",
        "desc": "One rectangular wire loop. On the left side, two pairs of "
                "long and short lines joined by a dashed line, with a plus "
                "sign by the first long line. Along the top, a switch whose "
                "lever runs from one hollow contact to the other, then a "
                "circle with a small rectangle inside it and two short "
                "arrows outside it pointing in.",
    },
    {
        # ks4-circuit-symbols-s19 — pick the three symbols a circuit needs
        "id": "ks4-fig-symbol-panel-battery-ldr-switch-lamp",
        "art": "symbol-panel",
        "params": {"items": [("P", "battery"), ("Q", "ldr"),
                             ("R", "switch_closed"), ("S", "lamp")],
                   # ⊕ fix round 1 (visual M1): 2 × 2, not a 700-wide strip
                   "cell_w": 200, "cols": 2, "H": 175, "fs": 25},
        "title": "Four circuit symbols, labelled P, Q, R and S.",
        "desc": "P: two pairs of long and short lines joined by a dashed "
                "line, with a plus sign. Q: a small rectangle inside a "
                "circle, with two arrows outside it pointing in. R: two "
                "hollow circles joined by a straight lever. S: a circle "
                "with a cross inside it.",
    },
    {
        # ks4-circuit-symbols-s26 — which symbol is the light-emitting diode
        "id": "ks4-fig-symbol-panel-diode-ldr-led-lamp",
        "art": "symbol-panel",
        "params": {"items": [("P", "diode"), ("Q", "ldr"), ("R", "led"),
                             ("S", "lamp")],
                   # ⊕ fix round 1 (visual M1): 2 × 2, not a 700-wide strip
                   "cell_w": 200, "cols": 2, "H": 175, "fs": 25},
        "title": "Four circuit symbols, labelled P, Q, R and S.",
        "desc": "P: a circle containing a triangle pointing along the wire "
                "with a bar across its tip. Q: a small rectangle inside a "
                "circle, with two arrows outside it pointing in. R: the same "
                "circle, triangle and bar as P, with two arrows outside it "
                "pointing out. S: a circle with a cross inside it.",
    },
    {
        # ks4-circuit-symbols-h08 — a switch in one branch only
        "id": "ks4-fig-circuit-two-lamp-branches-switch-y",
        "art": "circuit",
        "params": {"netlist": [["cell"],
                               {"parallel": [[["lamp", "X"]],
                                             [["switch_closed"],
                                              ["lamp", "Y"]]]}]},
        "title": "A cell feeding two parallel branches: one holds a circle "
                 "with a cross labelled X; the other holds a switch and a "
                 "circle with a cross labelled Y.",
        "desc": "A cell on the top wire of the loop. The wire then reaches a "
                "junction dot and splits into two branches that rejoin at a "
                "second dot. The upper branch holds one lamp symbol, "
                "labelled X. The lower branch holds a switch whose lever "
                "joins both contacts, then a lamp symbol labelled Y.",
    },
    {
        # ks4-circuit-symbols-h24 — the ammeter as the diagram places it
        "id": "ks4-fig-circuit-ammeter-in-lamp-branch",
        "art": "circuit",
        "params": {"netlist": [["cell"],
                               {"parallel": [[["ammeter"], ["lamp"]],
                                             [["resistor"]]]}]},
        "title": "A cell feeding two parallel branches: one holds a circle "
                 "with the letter A and a circle with a cross; the other "
                 "holds a plain rectangle.",
        "desc": "A cell on the top wire of the loop. The wire then reaches a "
                "junction dot and splits into two branches that rejoin at a "
                "second dot. The upper branch holds a circle marked A and "
                "then a circle with a cross inside it. The lower branch "
                "holds a plain rectangle.",
    },

    # ── graphs, forces, molecules ─────────────────────────────────────────
    {
        "id": "ks4-fig-graph-distance-time-runner",
        "art": "graph",
        "params": {"series": [{"points": [(0, 0), (2, 8), (4, 13), (6, 16),
                                          (8, 17.5), (10, 18.2)],
                               "smooth": True}],
                   "x_label": "time", "x_unit": "s",
                   "y_label": "distance", "y_unit": "m",
                   "x_range": (0, 10), "y_range": (0, 20),
                   "x_ticks": [0, 2, 4, 6, 8, 10],
                   "y_ticks": [0, 5, 10, 15, 20]},
        "title": "A distance–time graph: a line rising steeply from the "
                 "origin, then curving to become gradually less steep.",
        "desc": "A graph of distance in metres against time in seconds. The "
                "line starts at the origin and rises steeply at first, then "
                "curves so that it becomes gradually less steep as time goes "
                "on, without going flat.",
    },
    {
        "id": "ks4-fig-resolution-triangle-generic",
        "art": "resolution-triangle",
        "params": {},
        "title": "A right-angled triangle with a labelled diagonal side and "
                 "two labelled shorter sides, with a small square marking "
                 "the right angle.",
        "desc": "A right-angled triangle. The longest side (the hypotenuse) "
                "is labelled F. The horizontal side is labelled F cos θ and "
                "the vertical side F sin θ. A small square marks the right "
                "angle, and θ is marked where the hypotenuse meets the "
                "horizontal side.",
    },
    {
        "id": "ks4-fig-molecule-h2o-dot-cross",
        "art": "dot-cross",
        # ⊕ fix round 1 (examiner B3): "lens" seats BOTH electrons of each
        # bonding pair inside the overlap of the two shells. The default
        # seat put O's electron outside the H shell — a shared pair drawn
        # as not shared, and H counting one electron.
        "params": {"formula": "H2O", "title": False, "compact": True,
                   "seat": "lens"},
        "title": "A dot-and-cross diagram of a water molecule.",
        "desc": "One oxygen atom's circle overlapping two hydrogen atoms' "
                "circles. Each overlap holds one dot and one cross. The "
                "oxygen circle also carries two further pairs of dots, not "
                "shared with a hydrogen atom.",
    },
]
