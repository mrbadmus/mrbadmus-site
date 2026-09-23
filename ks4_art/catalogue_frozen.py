"""ks4_art.catalogue_frozen — KS4 figures for the MRB-352 frozen-window rows
(Mide's 23 Sep 2026 ruling, `frozen_window_allowlist.py`), drawn by figlib.

⊕ MRB-352 run 2: every record here was rebuilt against the examiner's
figure specification for the 28 frozen rows — exact components, labels and
values, what must NOT appear, and shapes-only alt text. Kept in its own
file so a content lane editing `catalogue.py` cannot collide with it.
"""

_H04 = {"netlist": [["battery"], ["switch_closed"],
                    {"parallel": [[["lamp"]], [["resistor"]]]}]}
_H04_TITLE = ("A battery and a closed switch on the main wire, which then "
              "splits into two parallel branches: one holding a circle with "
              "a cross inside it, the other a plain rectangle.")
_H04_DESC = "No meter is drawn anywhere in the circuit."

CATALOGUE = [
    # ks4-circuit-symbols-h04 — ammeter placement, so NO meter is drawn.
    # The second branch was a motor; the motor is not an AQA symbol.
    {"id": "ks4-fig-circuit-battery-switch-lamp-resistor-branches",
     "art": "circuit", "params": _H04,
     "title": _H04_TITLE, "desc": _H04_DESC},
    # ⚠ The row still names this OLD id until the content lane re-points it.
    # Same motor-free drawing. Delete this record once nothing references
    # it (build_figures reports every id no question uses).
    {"id": "ks4-fig-circuit-battery-switch-lamp-motor-branches",
     "art": "circuit", "params": _H04,
     "title": _H04_TITLE, "desc": _H04_DESC},

    # ks4-circuit-symbols-s03 — cell on the left side; closed switch, lamp,
    # lamp along the top; no labels.
    {"id": "ks4-fig-circuit-cell-switch-two-lamps-loop",
     "art": "circuit",
     "params": {"netlist": [["switch_closed"], ["lamp"], ["lamp"]],
                "left": [["cell"]]},
     "title": "A single loop with a cell, a closed switch, and two lamp "
              "symbols, one after another around the loop.",
     "desc": "One rectangular wire loop: a cell on the left side, then along "
             "the top a switch whose lever joins its two contacts, and two "
             "lamp symbols (each a circle with a cross inside it)."},

    # ks4-circuit-symbols-e02 — the open switch, in a circuit.
    {"id": "ks4-fig-circuit-cell-open-switch-lamp",
     "art": "circuit",
     "params": {"netlist": [["switch"]], "left": [["cell"]],
                "right": [["lamp"]]},
     "title": "A single loop with a pair of long and short lines, a switch "
              "symbol whose lever is lifted away from its second contact, "
              "and a circle with a cross inside it.",
     "desc": "One rectangular wire loop: a cell on the left side, a switch "
             "on the top wire whose lever starts at one contact and angles "
             "away, ending short of the other, and a circle with a cross "
             "inside it on the right side."},

    # ks4-circuit-symbols-h02 — the two students' drawings (E1 closed).
    {"id": "ks4-fig-sensor-symbols-student-a-b",
     "art": "symbol-panel",
     "params": {"items": [("Student A", "thermistor"), ("Student B", "ldr")]},
     "title": "Two circuit symbols, labelled Student A and Student B.",
     "desc": "Student A: a rectangle in a wire with a diagonal line through "
             "it; the lower end of the line turns into a short horizontal "
             "tail, and there is no arrowhead. Student B: a small rectangle "
             "inside a circle in a wire, with two arrows outside the circle "
             "pointing in towards it."},

    # ks4-acceleration-h03 — first gradient 9 m/s², never above g; a
    # monotone curve that never exceeds 55; gridlines every 5 so 55 sits on
    # one; no marker, tangent or dashed line.
    {"id": "ks4-fig-graph-velocity-time-skydiver",
     "art": "graph",
     "params": {"series": [{"points": [(0, 0), (2, 18), (4, 32), (6, 42),
                                       (8, 48.5), (10, 52.5), (12, 54.5),
                                       (14, 55), (16, 55), (18, 55), (20, 55)],
                            "smooth": True}],
                "x_label": "time", "x_unit": "s",
                "y_label": "velocity", "y_unit": "m/s",
                "x_range": (0, 20), "y_range": (0, 60),
                "x_ticks": list(range(0, 21, 2)),
                "y_ticks": list(range(0, 61, 10)),
                "y_grid": list(range(0, 61, 5)),
                "W": 480, "H": 380},
     "title": "A graph of velocity in m/s against time in s: a curved line "
              "starting at the origin, rising and then levelling off.",
     "desc": "The time axis runs from 0 to 20 s and the velocity axis from "
             "0 to 60 m/s."},

    # ks4-distance-time-graphs-h02 — a plausible 400 m run, ending at 80 s.
    {"id": "ks4-fig-graph-distance-time-runner-400m",
     "art": "graph",
     "params": {"series": [{"points": [(0, 0), (10, 80), (20, 155), (30, 225),
                                       (40, 285), (50, 335), (60, 372),
                                       (70, 393), (80, 400)],
                            "smooth": True}],
                "x_label": "time", "x_unit": "s",
                "y_label": "distance", "y_unit": "m",
                "x_range": (0, 80), "y_range": (0, 400),
                "x_ticks": list(range(0, 81, 10)),
                "y_ticks": list(range(0, 401, 100)),
                "y_grid": list(range(0, 401, 50)),
                "end_dot": True, "W": 480, "H": 380},
     "title": "A graph of distance in m against time in s: a curved line "
              "from the origin that becomes less steep, ending at 400 m at "
              "80 s.",
     "desc": "The time axis runs from 0 to 80 s and the distance axis from "
             "0 to 400 m. A dot marks the end of the line."},

    # ks4-covalent-bonding-s04 — the student's WRONG ammonia: the third H
    # drawn apart, so N's shell unambiguously holds 6.
    {"id": "ks4-fig-molecule-nh3-missing-bond",
     "art": "dot-cross",
     "params": {"formula": "NH3", "title": False, "compact": True,
                "angles": (180, 90, 0), "detached": (2,), "dashed": True,
                "nuclei": False, "seat": "lens"},
     "title": "A dot-and-cross diagram with an N circle overlapping two H "
              "circles, and a third H circle drawn apart from it.",
     "desc": "Each overlap holds one dot and one cross. The N circle also "
             "has a pair of dots on its own. The separate H circle holds one "
             "cross."},

    # ks4-direct-alternating-pd-h02 — two separate, captioned screens.
    {"id": "ks4-fig-oscilloscope-compare-5-10",
     "art": "oscilloscope",
     "params": {"traces": [{"cycles": 5, "caption": "Supply X"},
                           {"cycles": 10, "caption": "Supply Y"}]},
     "title": "Two oscilloscope screens, labelled X and Y, each showing a "
              "wave trace of the same height; the trace on Y has more "
              "up-and-down cycles across the same width.",
     "desc": "Two gridded screens stacked one above the other, captioned "
             "Supply X and Supply Y, with no numbers on either."},

    # ks4-food-chains-webs-s02 — the moorland web, four boxes, four arrows.
    {"id": "ks4-fig-food-web-moorland",
     "art": "food-web",
     "params": {"W": 400, "H": 300,
                "nodes": [{"id": "fox", "name": "Fox", "x": 200, "y": 50},
                          {"id": "hare", "name": "Mountain hare", "x": 96, "y": 150},
                          {"id": "grouse", "name": "Red grouse", "x": 304, "y": 150},
                          {"id": "heather", "name": "Heather", "x": 200, "y": 250}],
                "eats": [("heather", "hare"), ("heather", "grouse"),
                         ("hare", "fox"), ("grouse", "fox")]},
     "title": "A food web: four labelled boxes joined by arrows.",
     "desc": "Heather at the bottom, mountain hare and red grouse in the "
             "middle, fox at the top."},

    # ks4-condensation-polymerisation-h02 — AQA box notation, monomers only.
    {"id": "ks4-fig-polyester-monomers",
     "art": "box-monomers",
     "params": {"parts": [("n", "HO", "OH"), ("n", "HOOC", "COOH")],
                "product": "polyester"},
     "title": "Two chemical formulas with a box standing for the carbon "
              "chain: HO–box–OH and HOOC–box–COOH, each with n in front, "
              "joined by a plus sign and an arrow to the word polyester.",
     "desc": "One line of formulas: n HO, a bond, an empty box, a bond, OH; "
             "a plus sign; n HOOC, a bond, an empty box, a bond, COOH. "
             "Below, an arrow points to the word polyester."},
]
