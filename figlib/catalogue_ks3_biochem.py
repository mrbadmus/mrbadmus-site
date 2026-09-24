"""figlib.catalogue_ks3_biochem — KS3 question figures for the biology and
chemistry rows of MRB-352 run 2's 174 flagged rows (batch 2).

Every record follows the examiner's spec (figures F1–F19): exact values,
labels and what must NOT appear. `title` is the alt text and names only what
is SHOWN; `desc` is the long description, shapes only. Collected by
`figlib/ks3_catalogue.py` alongside `figlib/catalogue_ks3.py`.
"""

_HEIGHTS_1CM = [0, 1, 0, 2, 0,  2, 0, 3, 0, 2,  3, 1, 4, 0, 5,
                4, 2, 5, 1, 4,  0, 5, 2, 3, 2,  2, 0, 3, 0, 1,
                0, 1, 0, 0, 2]
# 5 cm block sums 3, 7, 13, 16, 12, 6, 3 = 60 — the same sixty students as
# `b10-height-bars-touching`, split into 1 cm groups.
assert len(_HEIGHTS_1CM) == 35 and sum(_HEIGHTS_1CM) == 60
assert [sum(_HEIGHTS_1CM[i:i + 5]) for i in range(0, 35, 5)] == \
    [3, 7, 13, 16, 12, 6, 3]

CATALOGUE = [
    # F1 · b10-03-e13 — no text at all: naming the shape would answer it.
    {"id": "b10-dna-xray-pattern",
     "art": "xray-pattern",
     "params": {},
     "title": "A drawing of an X-ray photograph: dark marks on a pale oval.",
     "desc": "Short dark dashes lie along two diagonal lines that cross at "
             "the centre. A thick dark arc sits at the top of the oval and "
             "another at the bottom. The centre is blank."},

    # F2 · b10-01-s07 — twelve students, seven 5 cm groups.
    {"id": "b10-height-hist-12",
     "art": "columns",
     "params": {"bins": [{"n": n} for n in (1, 3, 1, 1, 4, 1, 1)],
                "edges": [145, 150, 155, 160, 165, 170, 175, 180],
                "x_label": "height", "x_unit": "cm",
                "y_label": "number of students", "y_step": 1, "y_max": 5,
                "touching": True, "W": 480, "H": 380},
     "title": "A histogram of twelve students' heights.",
     "desc": "Seven touching bars from 145 to 180 cm in 5 cm groups, with "
             "heights 1, 3, 1, 1, 4, 1 and 1 students."},

    # F3 · b10-01-s24 — 35 one-centimetre groups; every 5th boundary numbered.
    {"id": "b10-height-hist-1cm",
     "art": "columns",
     "params": {"bins": [{"n": n} for n in _HEIGHTS_1CM],
                "edges": list(range(145, 181)),
                "edge_label_every": 5,
                "x_label": "height", "x_unit": "cm",
                "y_label": "number of students", "y_step": 1, "y_max": 5,
                "touching": True, "W": 480, "H": 380},
     "title": "A histogram of sixty students' heights in 1 cm groups.",
     "desc": "Thirty-five narrow touching bars from 145 to 180 cm. Their "
             "heights jump up and down between 0 and 5, and many bars have "
             "zero height."},

    # F4 · b10-01-h25
    {"id": "b10-height-curves-boys-girls",
     "art": "graph",
     "params": {"series": [
                    {"label": "girls", "smooth": True,
                     "points": [(140, 0), (145, 2), (150, 6), (155, 12),
                                (160, 16), (165, 12), (170, 6), (175, 2),
                                (180, 0), (185, 0), (190, 0)]},
                    {"label": "boys", "smooth": True,
                     "points": [(140, 0), (145, 0), (150, 1), (155, 4),
                                (160, 9), (165, 14), (170, 16), (175, 11),
                                (180, 5), (185, 1), (190, 0)]}],
                "legend": True,
                "x_label": "height", "x_unit": "cm", "x_range": (140, 190),
                "x_ticks": [140, 150, 160, 170, 180, 190],
                "y_label": "number of students", "y_unit": None,
                "y_range": (0, 20), "y_ticks": [0, 5, 10, 15, 20],
                "W": 480, "H": 400},
     "title": "A graph of number of students against height, with two "
              "curved lines labelled boys and girls.",
     "desc": "Both lines are single humps. The girls' line peaks at 160 cm "
             "and the boys' at 170 cm. The two humps cover much of the same "
             "range of heights."},

    # F5 · b4-05-h17 — NO net line: why it would curve is the question.
    {"id": "b4-light-rates-graph",
     "art": "graph",
     "params": {"series": [
                    {"label": "photosynthesis", "smooth": True,
                     "points": [(0, 0), (1, 3.2), (2, 5.6), (3, 7.2),
                                (4, 8.1), (5, 8.5), (6, 8.6), (7, 8.6),
                                (8, 8.6)]},
                    {"label": "respiration", "smooth": False,
                     "points": [(0, 2), (8, 2)]}],
                "legend": True,
                "x_label": "light intensity", "x_unit": "arbitrary units",
                "x_range": (0, 8), "x_ticks": list(range(0, 9)),
                # the spec's "rate of carbon dioxide exchange / arbitrary
                # units" is 424 units of bold text, longer than any phone-
                # width plot is tall; the formula keeps it on the axis
                "y_label": "rate of CO₂ exchange",
                "y_unit": "arbitrary units", "y_range": (0, 10),
                "y_ticks": [0, 2, 4, 6, 8, 10], "W": 480, "H": 470},
     "title": "A graph with two lines against light intensity: a curved line "
              "labelled photosynthesis and a flat line labelled respiration.",
     "desc": "The photosynthesis line starts at zero, rises steeply and then "
             "levels off at about 8.6. The respiration line is flat at 2 all "
             "the way across."},

    # F6 · b5-03-h26 — the student's poster: release drawn opposite Day 1.
    {"id": "b5-cycle-clock-poster",
     "art": "cycle-clock",
     "params": {"days": 35, "marker_at": 0.5},
     "title": "A student's poster: a circle marked with 35 ticks, Day 1 at "
              "the top and a dot labelled 'egg released' at the bottom.",
     "desc": "The ticks run clockwise from the top, shown by a small arrow. "
             "The dot sits directly opposite Day 1."},

    # F7 · b9-01-s11 — the sparrowhawk keeps distractor [2] false. NO legend
    # (batch-2 fix round, examiner MINOR-1, commander's ruling): stating the
    # arrow convention would answer distractor A, exactly as on F20.
    {"id": "b9-garden-web-blackbird",
     "art": "food-web",
     "params": {"W": 400, "H": 350, "clearance": 22,
                "nodes": [
                    {"id": "hawk", "name": "Sparrowhawk", "x": 200, "y": 45},
                    {"id": "blackbird", "name": "Blackbird", "x": 200,
                     "y": 140},
                    {"id": "caterpillars", "name": "Caterpillars", "x": 95,
                     "y": 235},
                    {"id": "nettles", "name": "Nettles", "x": 95, "y": 310},
                    {"id": "bush", "name": "Berry bush", "x": 305,
                     "y": 310}],
                "eats": [("nettles", "caterpillars"),
                         ("caterpillars", "blackbird"),
                         ("bush", "blackbird"), ("blackbird", "hawk")]},
     "title": "A food web: five labelled boxes joined by arrows.",
     "desc": "Nettles and Berry bush at the bottom, Caterpillars above "
             "Nettles, Blackbird above them, Sparrowhawk at the top."},

    # F8 · b9-01-h15
    {"id": "b9-oak-pyramid-numbers",
     "art": "pyramid",
     "params": {"levels": [{"width": 36, "label": "1 oak tree"},
                           {"width": 290, "label": "5 000 caterpillars"},
                           {"width": 90, "label": "20 blue tits"}],
                "note": "Bar widths are not to scale.",
                "W": 500, "H": 212, "cx": 170, "bar_h": 44, "label_x": 330},
     "title": "A pyramid of numbers with three bars: 1 oak tree at the "
              "bottom, 5 000 caterpillars in the middle, 20 blue tits at "
              "the top.",
     "desc": "The bottom bar is very narrow, the middle bar is very wide and "
             "the top bar is narrow."},

    # F9 · b9-02-s13 — the student's WRONG graph: owls above voles.
    {"id": "b9-owl-vole-graph-wrong",
     "art": "graph",
     "params": {"series": [
                    {"label": "voles", "smooth": True,
                     "points": [(0, 40), (1, 55), (2, 70), (3, 60), (4, 40),
                                (5, 30), (6, 40), (7, 55), (8, 70), (9, 60),
                                (10, 40)]},
                    {"label": "owls", "smooth": True,
                     "points": [(0, 110), (1, 100), (2, 110), (3, 125),
                                (4, 135), (5, 120), (6, 105), (7, 100),
                                (8, 110), (9, 125), (10, 135)]}],
                "legend": True,
                "x_label": "time", "x_unit": "years", "x_range": (0, 10),
                "x_ticks": [0, 2, 4, 6, 8, 10],
                "y_label": "number of animals", "y_unit": None,
                "y_range": (0, 150), "y_ticks": [0, 50, 100, 150],
                "W": 480, "H": 380},
     "title": "A student's graph of owl and vole numbers against time, two "
              "wavy lines.",
     "desc": "Both lines rise and fall in cycles. The owls line stays above "
             "the voles line at every point."},

    # F10 · b9-02-h25 — one point per year, joined in order, anticlockwise.
    {"id": "b9-predator-prey-loop",
     "art": "graph",
     "params": {"series": [
                    {"label": "", "smooth": False, "dots": True,
                     "arrows": [0, 3, 5, 8],
                     "points": [(20, 10), (35, 11), (52, 14), (62, 20),
                                (58, 28), (45, 33), (30, 31), (20, 25),
                                (15, 18), (16, 13), (23, 11.5)]}],
                "x_label": "number of prey", "x_unit": None,
                "x_range": (0, 70), "x_ticks": list(range(0, 71, 10)),
                "y_label": "number of predators", "y_unit": None,
                "y_range": (0, 40), "y_ticks": [0, 10, 20, 30, 40],
                "W": 480, "H": 400},
     "title": "A graph of number of predators against number of prey: "
              "points joined in order form a closed loop.",
     "desc": "Eleven dots joined by straight lines go round once "
             "anticlockwise and end near where they began. Small arrowheads "
             "on the line show the direction."},

    # F11 · c10-05-s30 — two bars only; the remainder is the question.
    {"id": "c10-air-two-gases",
     "art": "hbar",
     "params": {"rows": [{"label": "Nitrogen", "value": 78,
                          "display": "78%"},
                         {"label": "Oxygen", "value": 21, "display": "21%"}],
                "axis": {"label": "percentage", "unit": "%",
                         "ticks": [0, 20, 40, 60, 80, 100],
                         "min": 0, "max": 100},
                "heading": "Percentage of dry air", "W": 480},
     "title": "A bar chart with two horizontal bars: nitrogen 78% and "
              "oxygen 21%.",
     "desc": "The axis runs from 0 to 100 percent of dry air."},

    # F12 · c2-03-e07 — a 1:1 lattice, NOT Fe–S pairs (FeS is not molecular).
    {"id": "c2-iron-sulfide-particles",
     "art": "particle-grid",
     "params": {"kinds": [{"fill": "#8d939c", "label": "iron atom"},
                          {"fill": "#f2d04b", "label": "sulfur atom"}],
                "n": 6, "r": 18, "pitch": 36, "origin": (40, 40),
                "frame": (20, 20, 224, 224), "W": 380, "H": 264,
                "key_x": 252, "key_y": (110, 150)},
     "title": "A box of touching circles of two kinds, grey and yellow, "
              "alternating in rows.",
     "desc": "Each grey circle touches yellow circles on every side and "
             "there are equal numbers of each. A key says grey is an iron "
             "atom and yellow is a sulfur atom."},

    # F13 · c3-05-s28 — the bulb deliberately ABOVE the side arm.
    {"id": "c3-thermometer-high",
     "art": "distillation-flask",
     "params": {"bulb_y": 115, "arm_y": 160, "W": 380, "H": 420},
     "title": "A flask of liquid being heated, with a thermometer in the "
              "neck and a side arm leading to a condenser.",
     "desc": "The thermometer bulb sits high in the neck, above the point "
             "where the side arm leaves."},

    # F14 · c3-05-h13 — no fraction names on the column.
    {"id": "c3-column-temperatures",
     "art": "column-temps",
     "params": {"outlets": [(405, "350 °C"), (290, "200 °C"),
                            (160, "100 °C"), (45, "25 °C")],
                "W": 360, "H": 460, "col": (130, 30, 80, 390)},
     "title": "A tall column with four outlet pipes and a temperature marked "
              "beside each.",
     "desc": "From bottom to top the outlets are marked 350 °C, 200 °C, "
             "100 °C and 25 °C. The outlets are at the bottom, a third of "
             "the way up, two thirds of the way up and at the top. Heated "
             "crude oil enters near the bottom."},

    # F15 · c4-04-s10 — 2.4 g + ? g = 4.0 g, with no operators drawn.
    {"id": "c4-bar-model-mg-oxide",
     "art": "bar-model",
     "params": {"whole": "magnesium oxide: 4.0 g",
                "parts": [("magnesium: 2.4 g", 0.6), ("oxygen: ? g", 0.4)],
                "W": 480, "H": 175},
     "title": "A bar model: a whole bar labelled magnesium oxide, 4.0 g, "
              "above two parts labelled magnesium, 2.4 g, and oxygen, "
              "question mark.",
     "desc": "The two parts together are exactly as long as the whole bar. "
             "The magnesium part is the longer."},

    # F16 · c6-03-h10 — strong acid + strong alkali, step at 10 cm³.
    {"id": "c6-ph-curve",
     "art": "graph",
     "params": {"series": [
                    {"label": "", "smooth": True,
                     "points": [(0, 1.0), (3, 1.2), (6, 1.5), (8, 2.0),
                                (9, 2.5), (9.6, 3.2), (9.9, 4.0), (10, 7.0),
                                (10.1, 10.0), (10.4, 11.0), (11, 11.5),
                                (14, 12.2), (20, 12.6)]}],
                "x_label": "volume of alkali added", "x_unit": "cm³",
                "x_range": (0, 20), "x_ticks": [0, 5, 10, 15, 20],
                "y_label": "pH", "y_unit": None, "y_range": (0, 14),
                "y_ticks": [0, 2, 4, 6, 8, 10, 12, 14], "W": 480, "H": 400},
     "title": "A graph of pH against volume of alkali added.",
     "desc": "The line stays low and nearly flat, rises very steeply near "
             "10 cm³, then stays high and nearly flat to 20 cm³."},

    # F17 · c6-02-e32 — the arrow at 12; no acid/alkali words.
    {"id": "c6-ph-scale-arrow",
     "art": "ph-strip",
     "params": {"pointer": 12, "pointer_label": "solution X",
                "W": 480, "H": 148},
     "title": "A pH scale drawn as fifteen cells numbered 0 to 14, with an "
              "arrow labelled solution X pointing at one cell.",
     "desc": "The arrow points at the cell numbered 12."},

    # F18 · c7-01-s22 — one flat step, then a climb to the end of the run.
    {"id": "c7-heating-one-step",
     "art": "graph",
     "params": {"series": [
                    {"label": "", "smooth": False,
                     "points": [(0, 20), (6, 80), (12, 80), (16, 120),
                                (20, 160)]}],
                "x_label": "time", "x_unit": "min", "x_range": (0, 20),
                "x_ticks": [0, 4, 8, 12, 16, 20],
                "y_label": "temperature", "y_unit": "°C",
                "y_range": (0, 200), "y_ticks": [0, 40, 80, 120, 160, 200],
                "W": 480, "H": 380},
     "title": "A graph of temperature against time: a rising line, a flat "
              "section, then a rising line again.",
     "desc": "The temperature rises to 80 °C, stays at 80 °C from 6 to 12 "
             "minutes, then rises steadily until the line ends at 160 °C at "
             "20 minutes."},

    # F19 · c9-04-s23 — the lesson's own meets/fails; NO tints (they'd answer).
    {"id": "c9-materials-table",
     "art": "table",
     "params": {"col_heads": ["Stiff under load?",
                              "Cheap by the square metre?"],
                "rows": [{"head": "PET", "cells": [["No"], ["Yes"]]},
                         {"head": "Polythene", "cells": [["No"], ["Yes"]]},
                         {"head": "Firebrick", "cells": [["Yes"], ["Yes"]]},
                         {"head": "Reinforced concrete",
                          "cells": [["Yes"], ["Yes"]]},
                         {"head": "Carbon-fibre composite",
                          "cells": [["Yes"], ["No"]]},
                         {"head": "Heat-proof glass-ceramic",
                          "cells": [["Yes"], ["No"]]}],
                # fix round 2 (visual o2): the row names wrap, so the
                # "Cheap by the square metre?" header — the stem's own words
                # — fits in two lines instead of four
                "head_max": 130, "W": 480},
     "title": "A table of six materials with two columns: stiff under load, "
              "and cheap by the square metre, each answered yes or no.",
     "desc": "Rows: PET, polythene, firebrick, reinforced concrete, "
             "carbon-fibre composite, heat-proof glass-ceramic."},
]
