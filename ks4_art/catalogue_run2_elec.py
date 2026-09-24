"""ks4_art.catalogue_run2_elec — KS4 electricity figures for the 174 flagged
rows (MRB-352 run 2, batch 3), drawn by figlib.

⊕ Every record here is the examiner's figure specification N1–N21
(spec174_ks4_electricity.md): exact components, labels and parameters, what
must NOT appear, and shapes-only alt text. Kept in its own file so another
lane editing `catalogue.py` cannot collide with it; `ks4_art` discovers it.

Every circuit uses AQA 8463 v1.1 §4.2.1.1 (p.24) symbols only — no motor, no
a.c. supply, no buzzer. Where a diode or LED is drawn, the cell sits on the
loop's left side with its "+" (long plate) at the TOP, so conventional
current runs clockwise: left to right along the top wire.
"""

_PANEL = {"cell_w": 200, "cols": 2, "H": 175, "fs": 25}
_SCOPE_TITLE = ("An oscilloscope screen with a square grid and a darker "
                "centre line, showing a wave trace.")

CATALOGUE = [
    # N1 — ks4-circuit-symbols-s08: pick the battery
    {"id": "ks4-fig-symbol-panel-cell-fuse-battery-resistor",
     "art": "symbol-panel",
     "params": dict(_PANEL, items=[("P", "cell"), ("Q", "fuse"),
                                   ("R", "battery"), ("S", "resistor")]),
     "title": "Four circuit symbols, labelled P, Q, R and S.",
     "desc": "P: one long line and one short line across the wire, with a "
             "plus sign by the long line. Q: a rectangle with the wire "
             "running through it along its length. R: two pairs of long and "
             "short lines joined by a dashed line, with a plus sign by the "
             "first long line. S: a plain rectangle."},

    # N2 — ks4-circuit-symbols-s13: a voltmeter wired into the loop
    {"id": "ks4-fig-circuit-voltmeter-in-loop-lamp",
     "art": "circuit",
     "params": {"netlist": [["voltmeter", None, None, {"inline": True}],
                            ["lamp"]],
                "left": [["cell"]]},
     "title": "A single loop with a cell, a circle with the letter V, and a "
              "circle with a cross, one after another around the loop.",
     "desc": "One rectangular wire loop: a cell on the left side, then along "
             "the top wire a circle marked V and a circle with a cross inside "
             "it. Nothing is joined across any component."},

    # N3 — ks4-circuit-symbols-s15
    {"id": "ks4-fig-symbol-panel-resistor-fuse",
     "art": "symbol-panel",
     "params": dict(_PANEL, items=[("P", "resistor"), ("Q", "fuse")]),
     "title": "Two circuit symbols, labelled P and Q.",
     "desc": "P: a plain rectangle in a wire. Q: a rectangle with the wire "
             "running straight through it along its length."},

    # N4 — ks4-circuit-symbols-s16: the diode reversed against the current
    {"id": "ks4-fig-circuit-cell-diode-reversed-lamp",
     "art": "circuit",
     "params": {"netlist": [["diode", None, None, {"reverse": True}]],
                "left": [["cell"]], "right": [["lamp"]]},
     "title": "A single loop with a cell, a circle containing a triangle and "
              "bar, and a circle with a cross.",
     "desc": "One rectangular wire loop: a cell on the left side with its "
             "plus sign at the top, a diode symbol on the top wire whose "
             "triangle points to the left, back towards the cell, and a lamp "
             "symbol on the right side."},

    # N5 — ks4-circuit-symbols-s17, h06
    {"id": "ks4-fig-circuit-cell-resistor-lamp",
     "art": "circuit",
     "params": {"netlist": [["resistor"], ["lamp"]], "left": [["cell"]]},
     "title": "A single loop with a cell, a plain rectangle and a circle "
              "with a cross.",
     "desc": "One rectangular wire loop: a cell on the left side, then along "
             "the top a plain rectangle and a circle with a cross inside it."},

    # N6 — ks4-circuit-symbols-s18: a lit LED, forward-biased
    {"id": "ks4-fig-circuit-cell-led-resistor",
     "art": "circuit",
     "params": {"netlist": [["led"], ["resistor"]], "left": [["cell"]]},
     "title": "A single loop with a cell, a circle containing a triangle and "
              "bar with two small arrows pointing away from it, and a plain "
              "rectangle.",
     "desc": "One rectangular wire loop: a cell on the left side with its "
             "plus sign at the top, then along the top wire an LED symbol "
             "whose triangle points to the right, away from the cell's plus "
             "end, then a plain rectangle."},

    # N7 — ks4-circuit-symbols-s22: pick the temperature sensor
    {"id": "ks4-fig-symbol-panel-ldr-resistor-varres-thermistor",
     "art": "symbol-panel",
     "params": dict(_PANEL, items=[("W", "ldr"), ("X", "resistor"),
                                   ("Y", "variable_resistor"),
                                   ("Z", "thermistor")]),
     "title": "Four circuit symbols, labelled W, X, Y and Z.",
     "desc": "W: a small rectangle inside a circle, with two arrows outside "
             "it pointing in. X: a plain rectangle. Y: a rectangle with a "
             "diagonal arrow drawn across it. Z: a rectangle with a diagonal "
             "line through it whose lower end turns into a short horizontal "
             "tail."},

    # N8 — ks4-circuit-symbols-s24, h09 (the mirror of the frozen
    # ks4-fig-circuit-cell-open-switch-lamp)
    {"id": "ks4-fig-circuit-cell-closed-switch-lamp",
     "art": "circuit",
     "params": {"netlist": [["switch_closed"]], "left": [["cell"]],
                "right": [["lamp"]]},
     "title": "A single loop with a pair of long and short lines, a switch "
              "whose lever joins both of its contacts, and a circle with a "
              "cross inside it.",
     "desc": "One rectangular wire loop: a cell on the left side, a switch "
             "on the top wire whose lever runs from one hollow contact to the "
             "other, and a circle with a cross inside it on the right side."},

    # N9 — ks4-circuit-symbols-h07: the two meters swapped
    {"id": "ks4-fig-circuit-meters-swapped-lamp",
     "art": "circuit",
     "params": {"netlist": [["voltmeter", None, None, {"inline": True}],
                            ["lamp", None, None, {"ammeter": True}]],
                "left": [["cell"]]},
     "title": "A single loop with a cell, a circle with the letter V, and a "
              "circle with a cross, with a circle carrying the letter A "
              "connected across the circle with a cross on a short pair of "
              "wires.",
     "desc": "One rectangular wire loop: a cell on the left side, then along "
             "the top a circle marked V, which sits in the loop itself, and a "
             "lamp symbol. A circle marked A is joined to the top wire by two "
             "short wires, one either side of the lamp, so it bridges the "
             "lamp only."},

    # N10 — ks4-circuit-symbols-h11
    {"id": "ks4-fig-circuit-two-lamp-branches-open-switch-x",
     "art": "circuit",
     "params": {"netlist": [["cell"],
                            {"parallel": [[["switch"], ["lamp", "X"]],
                                          [["lamp", "Y"]]]}]},
     "title": "A cell feeding two parallel branches: one holds a switch and "
              "a circle with a cross labelled X; the other holds a circle "
              "with a cross labelled Y.",
     "desc": "A cell on the top wire of the loop. The wire then reaches a "
             "junction dot and splits into two branches that rejoin at a "
             "second dot. The upper branch holds a switch whose lever is "
             "angled away from its second contact, leaving a gap, then a "
             "lamp symbol labelled X. The lower branch holds one lamp "
             "symbol, labelled Y."},

    # N11 — ks4-circuit-symbols-h12
    {"id": "ks4-fig-symbol-panel-resistor-varres",
     "art": "symbol-panel",
     "params": dict(_PANEL, items=[("P", "resistor"),
                                   ("Q", "variable_resistor")]),
     "title": "Two circuit symbols, labelled P and Q.",
     "desc": "P: a plain rectangle in a wire. Q: a rectangle with a straight "
             "diagonal line from below-left to above-right, passing through "
             "it and ending in a solid arrowhead."},

    # N12 — ks4-circuit-symbols-h17
    {"id": "ks4-fig-circuit-lamp-x-branch-varres-lamp-y",
     "art": "circuit",
     "params": {"netlist": [["cell"],
                            {"parallel": [[["lamp", "X"]],
                                          [["variable_resistor"],
                                           ["lamp", "Y"]]]}]},
     "title": "A cell feeding two parallel branches: one holds a circle with "
              "a cross labelled X; the other holds a rectangle with a "
              "diagonal arrow and a circle with a cross labelled Y.",
     "desc": "A cell on the top wire of the loop. The wire then reaches a "
             "junction dot and splits into two branches that rejoin at a "
             "second dot. The upper branch holds one lamp symbol, labelled "
             "X. The lower branch holds a variable-resistor symbol, then a "
             "lamp symbol labelled Y."},

    # N13 — ks4-circuit-symbols-h18, h26
    {"id": "ks4-fig-circuit-cell-lamp",
     "art": "circuit",
     "params": {"netlist": [["lamp"]], "left": [["cell"]]},
     "title": "A single loop with a pair of long and short lines and a "
              "circle with a cross inside it.",
     "desc": "One rectangular wire loop: a cell on the left side and a lamp "
             "symbol on the top wire. Nothing else is drawn."},

    # N14 — ks4-circuit-symbols-h19
    {"id": "ks4-fig-circuit-cell-ammeter-thermistor",
     "art": "circuit",
     "params": {"netlist": [["ammeter"], ["thermistor"]], "left": [["cell"]]},
     "title": "A single loop with a cell, a circle with the letter A, and a "
              "rectangle with a diagonal line through it whose lower end "
              "turns into a short horizontal tail.",
     "desc": "One rectangular wire loop: a cell on the left side, then along "
             "the top a circle marked A and a rectangle crossed by a diagonal "
             "line that ends in a short horizontal tail, with no "
             "arrowhead."},

    # N15 — ks4-circuit-symbols-h20
    {"id": "ks4-fig-circuit-cell-two-switches-one-open-lamp",
     "art": "circuit",
     "params": {"netlist": [["switch_closed"], ["switch"]],
                "left": [["cell"]], "right": [["lamp"]]},
     "title": "A single loop with a cell, two switches and a circle with a "
              "cross: the first switch's lever joins both contacts, and the "
              "second switch's lever is angled away from its second "
              "contact.",
     "desc": "One rectangular wire loop: a cell on the left side, two "
             "switches one after the other on the top wire (the first "
             "closed, the second open with a gap), and a lamp symbol on the "
             "right side."},

    # N16 — ks4-circuit-symbols-h22
    {"id": "ks4-fig-circuit-main-switch-two-lamp-branches",
     "art": "circuit",
     "params": {"netlist": [["cell"], ["switch_closed"],
                            {"parallel": [[["lamp", "X"]],
                                          [["lamp", "Y"]]]}]},
     "title": "A cell and a switch on the main wire, which then splits into "
              "two parallel branches, each holding one circle with a cross: "
              "one labelled X, one labelled Y.",
     "desc": "A cell and then a switch whose lever joins both contacts, on "
             "the top wire of the loop. The wire then reaches a junction dot "
             "and splits into two branches that rejoin at a second dot. The "
             "upper branch holds a lamp symbol labelled X; the lower branch "
             "holds a lamp symbol labelled Y."},

    # N17 — ks4-electric-fields-h18
    {"id": "ks4-fig-radial-field-points-a-b",
     "art": "radial-field",
     "params": {"W": 420, "n_lines": 12, "sign": "+",
                "points": [{"label": "A", "r": 0.17, "angle": 45},
                           {"label": "B", "r": 0.40, "angle": 45}]},
     "title": "A small circle marked with a plus sign, with straight lines "
              "spreading out from it in all directions, each with an "
              "arrowhead pointing away from the circle. Two dots, A and B, "
              "lie in the same gap between two neighbouring lines: A close "
              "to the circle and B further out.",
     "desc": "Twelve evenly spaced straight lines radiate from a circle at "
             "the centre. Every arrowhead points outward. Dot A is near the "
             "circle, where the two lines either side of it are close "
             "together. Dot B lies further out in the same direction from "
             "the centre, where the same two lines are further apart."},

    # N18 — ks4-resistors-h10
    {"id": "ks4-fig-graph-iv-resistor-bends",
     "art": "graph",
     "params": {"series": [{"points": [(0, 0), (1, 0.10), (2, 0.20),
                                       (3, 0.30), (4, 0.38), (5, 0.44),
                                       (6, 0.48)],
                            "smooth": True}],
                "x_label": "potential difference", "x_unit": "V",
                "y_label": "current", "y_unit": "A",
                "x_range": (0, 6), "y_range": (0, 0.5),
                "x_ticks": [0, 1, 2, 3, 4, 5, 6],
                "y_ticks": [0, 0.1, 0.2, 0.3, 0.4, 0.5]},
     "title": "A graph of current against potential difference: a line that "
              "is straight from the origin at first, then curves so that it "
              "rises less steeply at the highest potential differences.",
     "desc": "A graph of current in amperes against potential difference in "
             "volts. The line starts at the origin and rises in a straight "
             "line up to 3 V. Above that it curves over, rising less and "
             "less steeply up to 6 V."},

    # N19 — ks4-direct-alternating-pd-s08
    {"id": "ks4-fig-oscilloscope-peak-2-5-div",
     "art": "oscilloscope",
     "params": {"traces": [{"cycles": 2, "caption": None}],
                "divisions": (10, 6), "amplitude": 2.5},
     "title": _SCOPE_TITLE,
     "desc": "One gridded screen, 10 squares wide and 6 squares high, with a "
             "darker horizontal centre line. A smooth wave starts on the "
             "centre line at the left edge and makes two complete up-and-down "
             "cycles across the screen. Each crest is two and a half squares "
             "above the centre line, and each trough is the same distance "
             "below it. No numbers are shown."},

    # N20 — ks4-direct-alternating-pd-s26
    {"id": "ks4-fig-oscilloscope-2-5-cycles",
     "art": "oscilloscope",
     "params": {"traces": [{"cycles": 2.5, "caption": None}],
                "divisions": (10, 6), "amplitude": 2},
     "title": _SCOPE_TITLE,
     "desc": "One gridded screen, 10 squares wide and 6 high, with a darker "
             "centre line. A smooth wave starts on the centre line at the "
             "left edge and makes two and a half up-and-down cycles, ending "
             "on the centre line at the right edge. No numbers are shown."},

    # N21 — ks4-direct-alternating-pd-h18
    {"id": "ks4-fig-oscilloscope-4-cycles",
     "art": "oscilloscope",
     "params": {"traces": [{"cycles": 4, "caption": None}],
                "divisions": (10, 6), "amplitude": 2},
     "title": _SCOPE_TITLE,
     "desc": "One gridded screen, 10 squares wide and 6 high, with a darker "
             "centre line. A smooth wave starts on the centre line at the "
             "left edge and makes four complete up-and-down cycles across "
             "the screen. No numbers are shown."},
]
