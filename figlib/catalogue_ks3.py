"""figlib.catalogue_ks3 — the KS3 QUESTION figures, declared.

⊕ MRB-352 run 2. A KS3 question used to borrow its figure from the lesson
page (`build_ks3.SVG_ART`, painted by `ks3.css` classes), which is how the
same drawing came out as a black disc, black bands and black-on-black
letters everywhere a lesson stylesheet was not loaded. Question figures now
come from figlib, in the exam-paper house style, self-painted.

KS3 LESSON pages are untouched: they still draw their own figures with
`ks3_art`, from `LESSON["figures"]` (architecture law). So one id can have
two drawings — the lesson's, and the question's — and that is deliberate.
The question's is declared here, SAME id, SAME meaning.

Every record: `id`, `art` (a key of `figlib.ART`), `title` (becomes the alt
text — it names what is SHOWN, never the answer), `desc` (the longer
screen-reader description, shapes only), `params` (the builder's keyword
arguments). Where one drawing serves several ids, the params are shared,
not copied.
"""

# ── the oak wood (ks3_data/b9: the lesson's own feeding links, minus the
# two decomposer links no question needs). Positions are box centres on a
# 640-wide canvas. Mice -> Sparrowhawk must pass in the gap between
# Ladybirds and Owls; `food_web` refuses the layout if any arrow comes
# within 22 units of a box that is not one of its ends, or two boxes
# closer than that. (Positions: the examiner's layout, widened to fit.) ─────────────────
_OAK_WOOD = {
    "W": 640, "H": 410, "clearance": 22,
    "nodes": [
        {"id": "hawk", "name": "Sparrowhawk", "x": 290, "y": 50},
        {"id": "bluetits", "name": "Blue tits", "x": 80, "y": 150},
        {"id": "ladybirds", "name": "Ladybirds", "x": 250, "y": 150},
        {"id": "owls", "name": "Owls", "x": 560, "y": 150},
        {"id": "caterpillars", "name": "Caterpillars", "x": 100, "y": 255},
        {"id": "aphids", "name": "Aphids", "x": 265, "y": 255},
        {"id": "mice", "name": "Mice", "x": 450, "y": 255},
        {"id": "bees", "name": "Bees", "x": 578, "y": 255},
        {"id": "oak", "name": "Oak tree", "x": 200, "y": 360},
        {"id": "flowers", "name": "Wildflowers", "x": 500, "y": 360},
    ],
    "eats": [("oak", "caterpillars"), ("oak", "aphids"), ("oak", "mice"),
             ("flowers", "mice"), ("flowers", "bees"),
             ("caterpillars", "bluetits"), ("aphids", "bluetits"),
             ("aphids", "ladybirds"), ("mice", "owls"),
             ("bluetits", "hawk"), ("mice", "hawk")],
    "legend": "arrows point from the organism that is eaten to the "
              "organism that eats it",
}
_OAK_TITLE = "A food web: ten labelled boxes joined by arrows."
_OAK_DESC = ("Boxes arranged in four rows, joined by one-way arrows. Bottom "
             "row: Oak tree, Wildflowers. Second row: Caterpillars, Aphids, "
             "Mice, Bees. Third row: Blue tits, Ladybirds, Owls. Top: "
             "Sparrowhawk.")

# ── solid / liquid / gas: one substance, three boxes, ONE particle size ──
_STATES = dict(W=598, H=252, box_w=170, box_h=170, pr=11, title=None,
               label_size=21, top=50, gap=24, descs=False, solid_grid=(5, 5),
               liquid_n=20, gas_n=5, gas_min=5.2)

_CHARGES = ["Positive", "Neutral", "Negative"]

CATALOGUE = [
    {
        "id": "b1-cell-bench",
        "art": "plant-cell",
        "title": "A labelled drawing of a leaf cell",
        "desc": "A rectangular cell with a thick outer wall and a thin "
                "membrane just inside it. A large rounded space fills most "
                "of the middle. The nucleus sits at one side, between that "
                "space and the membrane. Small oval chloroplasts lie in the "
                "thin layer of cytoplasm around the edge. Labels, each with "
                "a line to the part: cell wall, cell membrane, chloroplast, "
                "vacuole, cytoplasm, nucleus.",
        "params": {},
    },
    {
        "id": "b10-base-pairs",
        "art": "dna-ladder",
        "title": "How the bases pair across the two strands of DNA",
        "desc": "Two upright backbones with five rungs between them. Each "
                "rung is one base from the left meeting one from the right: "
                "A with T, T with A, C with G, G with C, A with T. A and G "
                "are drawn wide, C and T narrow, in two different fills. "
                "The same measurement line is drawn across the top and the "
                "bottom of the ladder, labelled 'every rung the same width'. "
                "A key says which fill marks the large bases and which the "
                "small.",
        "params": {"rungs": [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C"),
                             ("A", "T")]},
    },
    {
        "id": "b10-height-bars-touching",
        "art": "columns",
        "title": "A bar chart of student heights, with every bar touching "
                 "the next",
        "desc": "Seven bars along an axis of height in centimetres, grouped "
                "145 to 150 up to 175 to 180, every bar touching its "
                "neighbours with no gap. The vertical axis is the number of "
                "students: 3, 7, 13, 16, 12, 6, 3.",
        "params": {"bins": [{"label": "145–150", "n": 3},
                            {"label": "150–155", "n": 7},
                            {"label": "155–160", "n": 13},
                            {"label": "160–165", "n": 16},
                            {"label": "165–170", "n": 12},
                            {"label": "170–175", "n": 6},
                            {"label": "175–180", "n": 3}],
                   "edges": [145, 150, 155, 160, 165, 170, 175, 180],
                   "x_label": "height", "x_unit": "cm",
                   "y_label": "number of students", "y_step": 4,
                   "touching": True, "W": 480, "H": 380},
    },
    {
        "id": "b11-moth-pair",
        "art": "moth-pair",
        "title": "The same two moths on two kinds of bark",
        "desc": "Two panels side by side, each showing the same pale moth "
                "and the same dark moth. Left, clean bark mottled with "
                "lichen: the pale moth almost disappears against it and the "
                "dark moth stands out. Right, bark blackened by soot: the "
                "pale moth stands out and the dark moth almost disappears.",
        "params": {"panels": [{"title": "Lichen-covered bark", "bark": "lichen"},
                              {"title": "Soot-blackened bark", "bark": "soot"}]},
    },
    {
        "id": "b3-gut-transit-times",
        "art": "columns",
        "title": "A bar chart of the typical time food spends in the mouth, "
                 "stomach, small intestine and large intestine.",
        "desc": "Four bars: mouth, about 1 minute; stomach, 3 hours; small "
                "intestine, 4 hours; large intestine, 30 hours. The time "
                "axis runs from 0 to 35 hours.",
        "params": {"bins": [{"label": "Mouth", "n": 0.0,
                             # ⊕ fix round 1 (visual m1): one line, under
                             # the 5-hour gridline, not struck through by it
                             "display": "about 1 min"},
                            {"label": "Stomach", "n": 3, "display": "3 h"},
                            {"label": "Small intestine", "n": 4, "display": "4 h"},
                            {"label": "Large intestine", "n": 30, "display": "30 h"}],
                   "x_label": None, "x_unit": None,
                   "y_label": "time", "y_unit": "hours", "y_max": 35,
                   "y_step": 5, "touching": False, "values": True,
                   "min_bar": 2,
                   "caption": "Typical times. They vary a lot from person "
                              "to person and meal to meal.",
                   "W": 480, "H": 470},
    },
    {
        "id": "b4-gas-exchange-bars",
        "art": "columns",
        "title": "A bar chart with three bars: respiration, photosynthesis, "
                 "and a third bar labelled 'what a sensor outside the leaf "
                 "measures'.",
        "desc": "Three bars side by side on one baseline, each with its "
                "value above it: respiration 2, photosynthesis 8.6, and a "
                "third bar labelled 'What a sensor outside the leaf "
                "measures', 6.6. The vertical axis is the rate of carbon "
                "dioxide exchange in arbitrary units, from 0 to 10.",
        "params": {"bins": [{"label": "Respiration", "n": 2, "display": "2"},
                            {"label": "Photosynthesis", "n": 8.6, "display": "8.6"},
                            {"label": "What a sensor outside the leaf measures",
                             "n": 6.6, "display": "6.6"}],
                   "x_label": None, "x_unit": None,
                   "y_label": "rate of carbon dioxide exchange "
                              "(arbitrary units)",
                   "y_max": 10, "y_step": 2, "touching": False,
                   "values": True, "y_title": "top", "W": 480, "H": 470},
    },
    {
        "id": "b5-egg-sperm-scale",
        "art": "hbar",
        "title": "Two horizontal bars comparing an egg cell's diameter with a "
                 "sperm cell head's diameter, drawn to scale",
        "desc": "Two horizontal bars, one above the other, drawn to the same "
                "scale. The upper bar, egg cell, 0.1 mm across, runs the "
                "full width. The lower bar, sperm cell head, 0.005 mm "
                "across, is a twentieth of that length.",
        "params": {"rows": [{"label": "Egg cell", "value": 0.1,
                             "display": "0.1 mm across"},
                            {"label": "Sperm cell head", "value": 0.005,
                             "display": "0.005 mm across"}],
                   "heading": "Diameter, drawn to scale"},
    },
    dict(id="b9-oak-wood-web-plain", art="food-web", title=_OAK_TITLE,
         desc=_OAK_DESC, params=_OAK_WOOD),
    # an id a question referenced before the plain web existed — the SAME
    # drawing, so a question still pointing at it gets the legible web, not
    # the lesson's banded one
    dict(id="b9-oak-wood-web", art="food-web", title=_OAK_TITLE,
         desc=_OAK_DESC, params=_OAK_WOOD),
    {
        "id": "c1-three-states-particles",
        "art": "particle-states",
        "title": "Three boxes of circles, headed solid, liquid and gas.",
        "desc": "Each box contains circles of one size. In the first box the "
                "circles are packed tightly together in neat rows. In the "
                "second they are touching, heaped at the bottom in no "
                "pattern. In the third a few circles are spread far apart.",
        "params": _STATES,
    },
    {
        "id": "p10-horseshoe-field-gap",
        "art": "horseshoe-gap",
        "title": "A horseshoe magnet with five parallel lines crossing the "
                 "gap between its poles.",
        "desc": "A U-shaped magnet opening upwards. The top of the left arm "
                "is marked N and the top of the right arm S, their inner "
                "faces facing each other. Five straight, parallel, evenly "
                "spaced lines cross the gap from the N face to the S face, "
                "each with an arrowhead at its middle pointing from N to S.",
        "params": {"lines": 5},
    },
    {
        "id": "p10-motor-arrows-marked",
        "art": "motor-coil",
        "title": "A coil seen end-on between two magnetic poles, with an "
                 "arrow drawn from each side of the coil.",
        "desc": "An N pole on the left and an S pole on the right, with four "
                "straight lines between them, each with an arrowhead "
                "pointing from N to S. Between the poles, two small circles "
                "joined by a straight line through a dot: the left circle "
                "holds a cross, the right one a dot. An arrow points "
                "straight down from the left circle and an arrow of the same "
                "length points straight up from the right one.",
        "params": {},
    },
    {
        "id": "p4-crate-two-forces",
        "art": "crate-forces",
        "title": "A box on the ground with two horizontal arrows: one "
                 "pointing right labelled 50 N, one pointing left labelled "
                 "30 N.",
        "desc": "A square crate resting on a ground line. From the middle of "
                "its right side an arrow points right, labelled 50 N; from "
                "the middle of its left side a shorter arrow points left, "
                "labelled 30 N. Both arrows are drawn to one scale on the "
                "same horizontal line.",
        "params": {"forces": [{"newtons": 50, "dir": "right"},
                              {"newtons": 30, "dir": "left"}],
                   "label": "crate"},
    },
    {
        "id": "p8-lamp-symbol",
        "art": "symbol",
        "title": "Circuit symbol: a circle with two lines crossing inside it",
        "desc": "A single circuit symbol: a short wire enters a circle from "
                "the left and another leaves it on the right. Inside the "
                "circle two straight lines cross from edge to edge, making "
                "an X.",
        "params": {"key": "lamp"},
    },
    {
        "id": "p8-resistance-chart-recap",
        "art": "hbar",
        "title": "A bar chart of seven resistances on a logarithmic axis",
        "desc": "Seven horizontal bars, one per specimen: copper wire 0.05 "
                "ohms, nichrome wire 1.1 ohms, pencil lead 30 ohms, salt "
                "water 400 ohms, tap water 40 kilohms, dry wood 5 megohms, "
                "plastic ruler 2 teraohms. The axis marks are equally spaced "
                "and labelled 1 milliohm, 1 ohm, 1 kilohm, 1 megohm, 1 "
                "gigaohm, 1 teraohm. A dashed vertical line crosses the "
                "chart at 100 kilohms, labelled 'no sharp line — roughly "
                "where useful conduction gives out'.",
        "params": {"rows": [{"label": "Copper wire", "value": 0.05, "display": "0.05 Ω"},
                            {"label": "Nichrome wire", "value": 1.1, "display": "1.1 Ω"},
                            {"label": "Pencil lead", "value": 30, "display": "30 Ω"},
                            {"label": "Salt water", "value": 400, "display": "400 Ω"},
                            {"label": "Tap water", "value": 4e4, "display": "40 kΩ"},
                            {"label": "Dry wood", "value": 5e6, "display": "5 MΩ"},
                            {"label": "Plastic ruler", "value": 2e12, "display": "2 TΩ"}],
                   "log": True,
                   "axis": {"label": "resistance", "unit": None,
                            "note": "each mark is a thousand times the one "
                                    "before it",
                            "min": 1e-3, "max": 1e13,
                            "ticks": [1e-3, 1, 1e3, 1e6, 1e9, 1e12],
                            "tick_labels": ["1 mΩ", "1 Ω", "1 kΩ", "1 MΩ",
                                            "1 GΩ", "1 TΩ"]},
                   "boundary": {"value": 1e5,
                                "lines": ["no sharp line — roughly where",
                                          "useful conduction gives out"]}},
    },
    {
        "id": "p9-charge-matrix-blank",
        "art": "table",
        "title": "A 3 by 3 grid with rows and columns headed positive, "
                 "neutral and negative, and every inner cell empty.",
        "desc": "A grid. Across the top, under the heading Object 2: "
                "Positive, Neutral, Negative. Down the side, beside the "
                "heading Object 1: Positive, Neutral, Negative. All nine "
                "inner cells are empty.",
        "params": {"col_heads": _CHARGES, "col_title": "Object 2",
                   "row_title": "Object 1",
                   "rows": [{"head": h, "cells": [[], [], []]}
                            for h in _CHARGES]},
    },
    {
        "id": "p9-field-point-marked",
        "art": "field-point",
        "title": "An electric field map of arrows pointing right, with one "
                 "point marked P.",
        "desc": "A dashed frame holding rows of equal arrows, all pointing "
                "right. In the middle, one arrow is drawn bold, starting from "
                "a filled dot; the dot is lettered P.",
        "params": {},
    },
    # ── MRB-352 run 2, batch 1: KS3 physics (spec174_ks3_physics.md, plus
    # five P10-02 siblings drawn by the executor for the adjacent rows) ──
    {
        "id": 'p1-cooling-curve',
        "art": 'graph',
        "title": 'A graph of temperature in °C against time in minutes: a '
                 'curved line falling from 80 °C.',
        "desc": 'The time axis runs from 0 to 30 minutes and the '
                'temperature axis from 0 to 80 °C. The line starts at 80 '
                '°C, falls steeply at first, then more and more gently, '
                'ending just above 20 °C at 30 minutes.',
        "params": {'series': [{'points': [[0, 80],
                                          [2, 66.7],
                                          [4, 56.4],
                                          [6, 48.3],
                                          [8, 42.1],
                                          [10, 37.2],
                                          [15, 29.2],
                                          [20, 24.9],
                                          [25, 22.6],
                                          [30, 21.4]],
                               'smooth': True}],
                   'x_label': 'time',
                   'x_unit': 'minutes',
                   'y_label': 'temperature',
                   'y_unit': '°C',
                   'x_range': [0, 30],
                   'y_range': [0, 80],
                   'x_ticks': [0, 5, 10, 15, 20, 25, 30],
                   'y_ticks': [0, 20, 40, 60, 80],
                   'W': 480,
                   'H': 380,
                   'y_grid': [0, 10, 20, 30, 40, 50, 60, 70, 80]},
    },
    {
        "id": 'p3-dt-crossing',
        "art": 'graph',
        "title": 'A distance–time graph with two straight lines, A and B, '
                 'that cross.',
        "desc": 'Time from 0 to 40 s, distance from start from 0 to 80 m. '
                'Line A rises from 0 m at 0 s to 80 m at 40 s. Line B, '
                'dashed, rises gently from 30 m at 0 s to 50 m at 40 s. '
                'They cross at 20 s and 40 m.',
        "params": {'series': [{'points': [[0, 0], [40, 80]], 'label': 'A'},
                              {'points': [[0, 30], [40, 50]], 'label': 'B'}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 40],
                   'y_range': [0, 80],
                   'x_ticks': [0, 10, 20, 30, 40],
                   'y_ticks': [0, 20, 40, 60, 80],
                   'W': 480,
                   'H': 380,
                   'legend': True},
    },
    {
        "id": 'p3-dt-stop-start',
        "art": 'graph',
        "title": 'A distance–time graph made of three straight sections.',
        "desc": 'Time from 0 to 40 s, distance from start from 0 to 80 m. '
                'The line rises from 0 m to 40 m between 0 and 20 s, stays '
                'level at 40 m from 20 to 30 s, then rises to 70 m at 40 s.',
        "params": {'series': [{'points': [[0, 0], [20, 40], [30, 40], [40, 70]]}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 40],
                   'y_range': [0, 80],
                   'x_ticks': [0, 10, 20, 30, 40],
                   'y_ticks': [0, 20, 40, 60, 80],
                   'W': 480,
                   'H': 380,
                   'y_grid': [0, 10, 20, 30, 40, 50, 60, 70, 80]},
    },
    {
        "id": 'p3-dt-same-distance',
        "art": 'graph',
        "title": 'A distance–time graph with two straight lines, A and B, '
                 'from the origin.',
        "desc": 'Time from 0 to 30 s, distance from start from 0 to 60 m. '
                'Line A rises from the origin to 50 m at 10 s and ends '
                'there. Line B, dashed, rises from the origin to 50 m at 25'
                ' s and ends there. A dot marks the end of each line.',
        "params": {'series': [{'points': [[0, 0], [10, 50]], 'label': 'A'},
                              {'points': [[0, 0], [25, 50]], 'label': 'B'}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 30],
                   'y_range': [0, 60],
                   'x_ticks': [0, 5, 10, 15, 20, 25, 30],
                   'y_ticks': [0, 10, 20, 30, 40, 50, 60],
                   'W': 480,
                   'H': 380,
                   'legend': True,
                   'end_dot': True},
    },
    {
        "id": 'p3-dt-there-and-back',
        "art": 'graph',
        "title": 'A distance–time graph that rises, stays level, then falls'
                 ' back to zero.',
        "desc": 'Time from 0 to 50 s, distance from start from 0 to 100 m. '
                'The line rises from 0 m to 100 m between 0 and 10 s, stays'
                ' at 100 m until 30 s, then falls back to 0 m at 50 s.',
        "params": {'series': [{'points': [[0, 0], [10, 100], [30, 100], [50, 0]]}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 50],
                   'y_range': [0, 100],
                   'x_ticks': [0, 10, 20, 30, 40, 50],
                   'y_ticks': [0, 20, 40, 60, 80, 100],
                   'W': 480,
                   'H': 380},
    },
    {
        "id": 'p3-dt-three-sections',
        "art": 'graph',
        "title": 'A distance–time graph made of three straight sections.',
        "desc": 'Time from 0 to 40 s, distance from start from 0 to 60 m. '
                'The line rises from 0 m to 30 m between 0 and 10 s, stays '
                'at 30 m until 30 s, then rises to 60 m at 35 s.',
        "params": {'series': [{'points': [[0, 0], [10, 30], [30, 30], [35, 60]]}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 40],
                   'y_range': [0, 60],
                   'x_ticks': [0, 5, 10, 15, 20, 25, 30, 35, 40],
                   'y_ticks': [0, 10, 20, 30, 40, 50, 60],
                   'W': 480,
                   'H': 380},
    },
    {
        "id": 'p3-dt-late-start',
        "art": 'graph',
        "title": 'A distance–time graph with two parallel straight lines, A'
                 ' and B.',
        "desc": 'Time from 0 to 60 s, distance from start from 0 to 100 m. '
                'Line A rises from the origin to 90 m at 60 s. Line B, '
                'dashed and parallel to A, starts on the time axis at 20 s '
                'and rises to 60 m at 60 s.',
        "params": {'series': [{'points': [[0, 0], [60, 90]], 'label': 'A'},
                              {'points': [[20, 0], [60, 60]], 'label': 'B'}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 60],
                   'y_range': [0, 100],
                   'x_ticks': [0, 10, 20, 30, 40, 50, 60],
                   'y_ticks': [0, 20, 40, 60, 80, 100],
                   'W': 480,
                   'H': 380,
                   'legend': True},
    },
    {
        "id": 'p3-dt-steady-45m',
        "art": 'graph',
        "title": 'A distance–time graph with one straight line from the '
                 'origin, ending in a dot.',
        "desc": 'Time from 0 to 25 s, distance from start from 0 to 50 m, '
                'with gridlines every 5 m. The line rises from the origin '
                'and ends at a dot at 20 s and 45 m.',
        "params": {'series': [{'points': [[0, 0], [20, 45]]}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 25],
                   'y_range': [0, 50],
                   'x_ticks': [0, 5, 10, 15, 20, 25],
                   'y_ticks': [0, 10, 20, 30, 40, 50],
                   'W': 480,
                   'H': 380,
                   'y_grid': [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                   'end_dot': True},
    },
    {
        "id": 'p3-dt-parallel',
        "art": 'graph',
        "title": 'A distance–time graph with two parallel straight lines, A'
                 ' and B.',
        "desc": 'Time from 0 to 40 s, distance from start from 0 to 100 m. '
                'Line A rises from 20 m at 0 s to 100 m at 40 s. Line B, '
                'dashed, rises from 0 m at 0 s to 80 m at 40 s.',
        "params": {'series': [{'points': [[0, 20], [40, 100]], 'label': 'A'},
                              {'points': [[0, 0], [40, 80]], 'label': 'B'}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 40],
                   'y_range': [0, 100],
                   'x_ticks': [0, 10, 20, 30, 40],
                   'y_ticks': [0, 20, 40, 60, 80, 100],
                   'W': 480,
                   'H': 380,
                   'legend': True},
    },
    {
        "id": 'p3-dt-steep-short',
        "art": 'graph',
        "title": 'A distance–time graph with two straight lines, A and B, '
                 'from the origin.',
        "desc": 'Time from 0 to 40 s, distance from start from 0 to 60 m. '
                'Line A rises steeply from the origin and ends at a dot at '
                '10 s and 40 m. Line B, dashed, rises gently from the '
                'origin and ends at a dot at 40 s and 60 m.',
        "params": {'series': [{'points': [[0, 0], [10, 40]], 'label': 'A'},
                              {'points': [[0, 0], [40, 60]], 'label': 'B'}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'distance from start',
                   'y_unit': 'm',
                   'x_range': [0, 40],
                   'y_range': [0, 60],
                   'x_ticks': [0, 10, 20, 30, 40],
                   'y_ticks': [0, 10, 20, 30, 40, 50, 60],
                   'W': 480,
                   'H': 380,
                   'legend': True,
                   'end_dot': True},
    },
    {
        "id": 'p3-dt-two-scales',
        "art": 'graph-panels',
        "title": 'Two distance–time graphs, one above the other, each with '
                 'one straight line from the origin.',
        "desc": 'Graph 1: distance axis from 0 to 100 m, time from 0 to 50 '
                's; the line rises from the origin to 80 m at 50 s. Graph '
                '2: distance axis from 0 to 1000 m, time from 0 to 50 s; '
                'the line rises from the origin to 80 m at 50 s, close to '
                'the time axis.',
        "params": {'W': 480,
                   'panels': [{'caption': 'Graph 1',
                               'series': [{'points': [[0, 0], [50, 80]]}],
                               'x_label': 'time',
                               'x_unit': 's',
                               'y_label': 'distance from start',
                               'y_unit': 'm',
                               'x_range': [0, 50],
                               'y_range': [0, 100],
                               'x_ticks': [0, 10, 20, 30, 40, 50],
                               'y_ticks': [0, 20, 40, 60, 80, 100],
                               'W': 480,
                               'H': 300},
                              {'caption': 'Graph 2',
                               'series': [{'points': [[0, 0], [50, 80]]}],
                               'x_label': 'time',
                               'x_unit': 's',
                               'y_label': 'distance from start',
                               'y_unit': 'm',
                               'x_range': [0, 50],
                               'y_range': [0, 1000],
                               'x_ticks': [0, 10, 20, 30, 40, 50],
                               'y_ticks': [0, 200, 400, 600, 800, 1000],
                               'W': 480,
                               'H': 300}]},
    },
    {
        "id": 'p3-dt-train-km-min',
        "art": 'graph',
        "title": 'A graph of distance in km against time in minutes, made '
                 'of three straight sections.',
        "desc": 'Time from 0 to 10 minutes, distance from 0 to 12 km. The '
                'line rises from the origin to 6 km at 4 minutes, stays at '
                '6 km until 6 minutes, then rises to 12 km at 10 minutes.',
        "params": {'series': [{'points': [[0, 0], [4, 6], [6, 6], [10, 12]]}],
                   'x_label': 'time',
                   'x_unit': 'minutes',
                   'y_label': 'distance',
                   'y_unit': 'km',
                   'x_range': [0, 10],
                   'y_range': [0, 12],
                   'x_ticks': [0, 2, 4, 6, 8, 10],
                   'y_ticks': [0, 2, 4, 6, 8, 10, 12],
                   'W': 480,
                   'H': 380,
                   'x_grid': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
    },
    {
        "id": 'p4-grid-arrows-a-b',
        "art": 'force-grid',
        "title": 'A box drawn on squared paper with two arrows, A and B, '
                 'pointing away from it.',
        "desc": 'A square box in the middle of a grid of squares. Arrow A '
                'points left from the box and is 3 squares long. Arrow B '
                'points right from the box and is 6 squares long.',
        "params": {'arrows': [{'dir': 'left', 'squares': 3, 'label': 'A'},
                              {'dir': 'right', 'squares': 6, 'label': 'B'}],
                   'caption': None},
    },
    {
        "id": 'p4-grid-arrows-30-45-equal',
        "art": 'force-grid',
        "title": 'A box drawn on squared paper with two arrows labelled 30 '
                 'N and 45 N.',
        "desc": 'A square box in the middle of a grid of squares. An arrow '
                'labelled 30 N points left from the box and is 4 squares '
                'long. An arrow labelled 45 N points right from the box and'
                ' is 4 squares long.',
        "params": {'arrows': [{'dir': 'left', 'squares': 4, 'label': '30 N'},
                              {'dir': 'right', 'squares': 4, 'label': '45 N'}],
                   'caption': None},
    },
    {
        "id": 'p4-grid-arrows-12-20',
        "art": 'force-grid',
        "title": 'A box drawn on squared paper with two arrows labelled 12 '
                 'N and 20 N.',
        "desc": 'A square box in the middle of a grid of squares. An arrow '
                'labelled 12 N points left from the box and is 3 squares '
                'long. An arrow labelled 20 N points right from the box and'
                ' is 4 squares long.',
        "params": {'arrows': [{'dir': 'left', 'squares': 3, 'label': '12 N'},
                              {'dir': 'right', 'squares': 4, 'label': '20 N'}],
                   'caption': None},
    },
    {
        "id": 'p4-grid-arrows-scale-10n',
        "art": 'force-grid',
        "title": 'A box drawn on squared paper with two unlabelled arrows, '
                 'and a scale under the grid.',
        "desc": 'A square box in the middle of a grid of squares. One arrow'
                ' points left from the box and is 3 squares long; the other'
                ' points right and is 7 squares long. Under the grid: '
                "'Scale: 1 square = 10 N'.",
        "params": {'arrows': [{'dir': 'left', 'squares': 3, 'label': None},
                              {'dir': 'right', 'squares': 7, 'label': None}],
                   'caption': 'Scale: 1 square = 10 N'},
    },
    {
        "id": 'p4-grid-arrows-50-10-equal',
        "art": 'force-grid',
        "title": 'A box drawn on squared paper with two arrows labelled 50 '
                 'N and 10 N.',
        "desc": 'A square box in the middle of a grid of squares. An arrow '
                'labelled 50 N points left from the box and is 5 squares '
                'long. An arrow labelled 10 N points right from the box and'
                ' is 5 squares long.',
        "params": {'arrows': [{'dir': 'left', 'squares': 5, 'label': '50 N'},
                              {'dir': 'right', 'squares': 5, 'label': '10 N'}],
                   'caption': None},
    },
    {
        "id": 'p6-wave-dots-two-waves',
        "art": 'wave-line',
        "title": 'A wave with two dots on it and a measured distance '
                 'between the dots.',
        "desc": 'A smooth wave of two and a half cycles along a straight '
                'centre line. One dot sits half-way down the right-hand '
                'side of the first crest, the other at the same place on '
                'the third crest. A '
                'double-headed arrow below the wave, between two thin '
                'dashed lines dropped from the dots, is labelled 0.90 m.',
        "params": {'cycles': 2.5,
                   'start_phase': 0.0,
                   'dots': [0.416667, 2.416667],
                   'dimension': {'from': 0.416667, 'to': 2.416667, 'label': '0.90 m'}},
    },
    {
        "id": 'p6-wave-six-crests',
        "art": 'wave-line',
        "title": 'A wave with six crests and a measured distance from the '
                 'first crest to the last.',
        "desc": 'A smooth wave with six crests along a straight centre '
                'line, starting and ending a quarter-cycle beyond the first'
                ' and last crests. Thin dashed lines drop from the first '
                'and sixth crests to a double-headed arrow below the wave '
                'labelled 1.5 m.',
        "params": {'cycles': 5.5,
                   'start_phase': 0.0,
                   'dots': [],
                   'dimension': {'from': 0.25, 'to': 5.25, 'label': '1.5 m'}},
    },
    {
        "id": 'p6-sound-six-compressions',
        "art": 'longitudinal',
        "title": 'A row of vertical lines bunched together in six places, '
                 'with a measured distance between the first two bunches.',
        "desc": 'A long row of thin vertical lines. In six evenly spaced '
                'places the lines are squeezed close together; between '
                'those places they are spread apart. The row starts a '
                'little before the first squeezed place and ends a little '
                'after the sixth. A '
                'double-headed arrow below the row, from the centre of the '
                'first squeezed place to the centre of the second, is '
                'labelled 30 cm.',
        "params": {'compressions': 6, 'dimension': {'label': '30 cm'},
                   'per_wave': 7},
    },
    {
        "id": 'p6-sound-four-compressions',
        "art": 'longitudinal',
        "title": 'A row of vertical lines bunched together in four places, '
                 'with a measured distance between the first two bunches.',
        "desc": 'As six-compressions, with four evenly spaced squeezed '
                'places; the arrow between the first two is labelled 22 cm.',
        "params": {'compressions': 4, 'dimension': {'label': '22 cm'}},
    },
    {
        "id": 'p6-sound-three-compressions',
        "art": 'longitudinal',
        "title": 'A row of vertical lines bunched together in three places.',
        "desc": 'A row of thin vertical lines, squeezed close together in '
                'three evenly spaced places and spread apart between them. '
                'The row starts a little before the first squeezed place '
                'and ends a little after the third.',
        "params": {'compressions': 3, 'dimension': None},
    },
    {
        "id": 'p8-battery-symbol',
        "art": 'symbol',
        "title": 'A circuit symbol in a short length of wire.',
        "desc": 'Two pairs of upright lines, each pair a long line and a '
                'shorter line, with a dashed line joining the pairs, in a '
                'horizontal wire. A plus sign beside the first long line.',
        "params": {'key': 'battery'},
    },
    {
        "id": 'p8-cell-symbol',
        "art": 'symbol',
        "title": 'A circuit symbol in a short length of wire.',
        "desc": 'One long upright line and one shorter upright line side by'
                ' side in a horizontal wire, with a plus sign beside the '
                'long line.',
        "params": {'key': 'cell'},
    },
    {
        "id": 'p8-resistor-symbol',
        "art": 'symbol',
        "title": 'A circuit symbol in a short length of wire.',
        "desc": 'An empty rectangle in a horizontal wire.',
        "params": {'key': 'resistor'},
    },
    {
        "id": 'p8-variable-resistor-symbol',
        "art": 'symbol',
        "title": 'A circuit symbol: a rectangle in a wire with an arrow '
                 'drawn diagonally through it.',
        "desc": 'An empty rectangle in a horizontal wire, with a straight '
                'arrow crossing it diagonally from lower left to upper '
                'right, the arrowhead clear of the rectangle.',
        "params": {'key': 'variable_resistor'},
    },
    {
        "id": 'p8-voltmeter-symbol',
        "art": 'symbol',
        "title": 'A circuit symbol in a short length of wire.',
        "desc": 'A circle with the capital letter V inside it, in a '
                'horizontal wire.',
        "params": {'key': 'voltmeter'},
    },
    {
        "id": 'p8-symbols-find-switch',
        "art": 'symbol-panel',
        "title": 'Four circuit symbols labelled A, B, C and D.',
        "desc": 'A grid of two rows. A: a circle with a cross inside it. B:'
                ' an empty rectangle. C: a circle with the letter A inside '
                'it. D: two small hollow circles with a lever from one that'
                ' is lifted clear of the other.',
        "params": {'items': [['A', 'lamp'],
                             ['B', 'resistor'],
                             ['C', 'ammeter'],
                             ['D', 'switch']],
                   'cols': 2},
    },
    {
        "id": 'p8-symbols-find-varres',
        "art": 'symbol-panel',
        "title": 'Four circuit symbols labelled A, B, C and D.',
        "desc": 'A grid of two rows. A: an empty rectangle. B: a rectangle '
                'with an arrow drawn diagonally through it. C: a long and a'
                ' short upright line side by side. D: a circle with the '
                'letter V inside it.',
        "params": {'items': [['A', 'resistor'],
                             ['B', 'variable_resistor'],
                             ['C', 'cell'],
                             ['D', 'voltmeter']],
                   'cols': 2},
    },
    {
        "id": 'p8-three-cells-lamp',
        "art": 'circuit',
        "title": 'A circuit with three cells in a row and a lamp in one '
                 'loop.',
        "desc": 'A rectangular loop of wire. Along the top, three cell '
                'symbols one after another, each a long and a short upright'
                ' line with a plus sign by the long line, all facing the '
                'same way, then a circle with a cross inside it.',
        "params": {'netlist': [['cell'], ['cell'], ['cell'], ['lamp']]},
    },
    {
        "id": 'p8-junction-current-lines',
        "art": 'graph',
        "title": 'A graph of current in A against time in s with three '
                 'lines, P, Q and R.',
        "desc": 'Time from 0 to 60 s, current from 0 to 0.6 A. Line P, '
                'solid, starts at 0.5 A and curves gently down to 0.35 A. '
                'Line Q, dashed, stays level at 0.2 A. Line R, dotted, '
                'rises in a straight line from 0.2 A to 0.3 A.',
        "params": {'series': [{'points': [[0, 0.5],
                                          [10, 0.457],
                                          [20, 0.425],
                                          [30, 0.4],
                                          [40, 0.38],
                                          [50, 0.364],
                                          [60, 0.35]],
                               'smooth': True,
                               'label': 'P'},
                              {'points': [[0, 0.2], [60, 0.2]], 'label': 'Q'},
                              {'points': [[0, 0.2], [60, 0.3]], 'label': 'R'}],
                   'x_label': 'time',
                   'x_unit': 's',
                   'y_label': 'current',
                   'y_unit': 'A',
                   'x_range': [0, 60],
                   'y_range': [0, 0.6],
                   'x_ticks': [0, 10, 20, 30, 40, 50, 60],
                   'y_ticks': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
                   'W': 480,
                   'H': 380,
                   'legend': True},
    },
    {
        "id": 'p8-series-meters-lamp-resistor',
        "art": 'circuit',
        "title": 'A series circuit with a cell, two ammeters, a lamp, a '
                 'resistor and two voltmeters.',
        "desc": 'A single loop. A cell on the left side. Along the top, in '
                'order: an ammeter labelled A1, a lamp, an ammeter labelled'
                ' A2, and a resistor. A voltmeter labelled V1 is connected '
                'across the lamp and a voltmeter labelled V2 across the '
                'resistor.',
        "params": {'netlist': [['ammeter', None, 'A1'],
                               ['lamp'],
                               ['voltmeter', None, 'V1'],
                               ['ammeter', None, 'A2'],
                               ['resistor'],
                               ['voltmeter', None, 'V2']],
                   'left': [['cell']]},
    },
    {
        "id": 'p10-bar-field-line-reversed',
        "art": 'bar-field',
        "title": 'A bar magnet with curved field lines around it, one of '
                 'them labelled X.',
        "desc": 'A bar magnet, N on the left and S on the right. Curved '
                'lines leave the N end and loop round to the S end, four '
                'above the magnet and four below, each with an arrowhead. '
                'The outermost line below, labelled X, also runs from the '
                'N end to the S end, but its arrowhead points back towards '
                'N; every other arrowhead points towards S.',
        "params": {'panels': [{'caption': None,
                               'upper': [38, 52, 66, 80],
                               'lower': [-38, -54, -70],
                               'reversed': {'angle': -86, 'label': 'X',
                                            'label_xy': [175, 290]},
                               'points': []}],
                   'panel_h': 320,
                   'clip': False},
    },
    {
        "id": 'p10-bar-field-two-drawings',
        "art": 'bar-field',
        "title": 'Two drawings, A and B, of the field around the same bar '
                 'magnet, one above the other.',
        "desc": 'Each drawing shows a bar magnet, N on the left and S on '
                'the right, with curved field lines looping from N to S, '
                'crowded near the ends. Drawing A has three lines above and'
                ' three below the magnet. Drawing B has six above and six '
                'below.',
        "params": {'panels': [{'caption': 'Drawing A',
                               'upper': [45, 65, 85],
                               'lower': [-45, -65, -85]},
                              {'caption': 'Drawing B',
                               'upper': [38, 48, 58, 68, 78, 87],
                               'lower': [-38, -48, -58, -68, -78, -87]}],
                   'panel_h': 320,
                   'clip': False},
    },
    {
        "id": 'p10-bar-field-points-xy',
        "art": 'bar-field',
        "title": 'A bar magnet with field lines and two marked points, X '
                 'and Y.',
        "desc": 'A bar magnet, N on the left and S on the right, with '
                'curved field lines looping from N to S. Point X is a dot '
                'beyond the N end, on the line through the middle of the '
                'magnet. Point Y is a dot above the middle of the magnet.',
        "params": {'panels': [{'caption': None,
                               'upper': [35, 50, 65, 80, 100, 120, 140, 160, 180],
                               'lower': [-35, -50, -65, -80, -100, -120, -140, -160],
                               'points': [{'label': 'X', 'at': 'axis_left', 'r': 1.5},
                                          {'label': 'Y',
                                           'at': 'above_centre',
                                           'r': 1.5}]}],
                   'panel_h': 380,
                   'clip': True},
    },
    {
        "id": 'p10-bar-field-line-upper',
        "art": 'bar-field',
        "title": 'A bar magnet with curved field lines around it, one of '
                 'them labelled X.',
        "desc": 'A bar magnet, N on the left and S on the right. Curved '
                'lines with arrowheads leave the N end and loop round to '
                'the S end, three above the magnet and four below. One more'
                ' line above, labelled X, leaves the N end and stops '
                'partway round, in empty space.',
        "params": {'panels': [{'caption': None,
                               'upper': [40, 58, 86],
                               'lower': [-40, -56, -72, -86],
                               'faulty': {'angle': 72,
                                          'fraction': 0.45,
                                          'label': 'X'},
                               'points': []}],
                   'panel_h': 320,
                   'clip': False},
    },
    {
        "id": 'p10-bar-field-two-drawings-b',
        "art": 'bar-field',
        "title": 'Two drawings, A and B, of the field around the same bar '
                 'magnet, one above the other.',
        "desc": 'Each drawing shows a bar magnet, N on the left and S on '
                'the right, with curved field lines looping from N to S. '
                'Drawing A has two lines above and two below the magnet. '
                'Drawing B has seven above and seven below.',
        "params": {'panels': [{'caption': 'Drawing A',
                               'upper': [50, 80],
                               'lower': [-50, -80]},
                              {'caption': 'Drawing B',
                               'upper': [36, 45, 54, 63, 72, 80, 87],
                               'lower': [-36, -45, -54, -63, -72, -80, -87]}],
                   'panel_h': 320,
                   'clip': False},
    },
    {
        "id": 'p10-bar-field-points-abcd',
        "art": 'bar-field',
        "title": 'A bar magnet with field lines and four marked points, A, '
                 'B, C and D.',
        "desc": 'A bar magnet, N on the left and S on the right, with '
                'curved field lines looping from N to S. Point A is a dot '
                'well above the magnet, a little right of its middle. Point'
                ' B is a dot up and to the left, beyond the N end. Point C '
                'is a dot down and to the right, beyond the S end. Point D '
                'is a dot just beyond the N end, on the line through the '
                'middle of the magnet.',
        "params": {'panels': [{'caption': None,
                               'points': [{'label': 'A', 'x': 0.45, 'y': 1.6},
                                          {'label': 'B', 'x': -1.9, 'y': 0.9},
                                          {'label': 'C', 'x': 1.6, 'y': -1.3},
                                          {'label': 'D', 'x': -1.15, 'y': 0}],
                               'upper': [35, 50, 65, 80, 100, 120, 140, 180],
                               'lower': [-35,
                                         -50,
                                         -65,
                                         -80,
                                         -100,
                                         -120,
                                         -140]}],
                   'panel_h': 380,
                   'clip': True},
    },
    {
        "id": 'p10-bar-field-wavy',
        "art": 'bar-field',
        "title": 'A bar magnet with wavy field lines around it.',
        "desc": 'A bar magnet, N on the left and S on the right. Lines with'
                ' arrowheads leave the N end and loop round to the S end, '
                'three above the magnet and three below, crowded near the '
                'ends. Every line wiggles from side to side along its '
                'length.',
        "params": {'panels': [{'caption': None,
                               'upper': [42, 64, 86],
                               'lower': [-42, -64, -86],
                               'wavy': {'amp': 3.2, 'period': 34}}],
                   'panel_h': 330,
                   'clip': False},
    },
    {
        "id": 'p10-bar-field-inside',
        "art": 'bar-field',
        "title": 'A bar magnet with field lines around it and two lines '
                 'drawn inside it.',
        "desc": 'A bar magnet, N on the left and S on the right. Curved '
                'lines with arrowheads leave the N end and loop round to '
                'the S end, three above the magnet and three below. Two '
                'straight lines are drawn inside the magnet from the N end '
                'to the S end, each with an arrowhead pointing towards S.',
        "params": {'panels': [{'caption': None,
                               'upper': [42, 64, 86],
                               'lower': [-42, -64, -86],
                               'inside': 2}],
                   'panel_h': 320,
                   'clip': False},
    },
    {
        "id": 'p10-bar-field-even',
        "art": 'bar-field',
        "title": "A student's drawing of field lines around a bar magnet: "
                 'evenly spaced curved lines.',
        "desc": 'A bar magnet, N on the left and S on the right. Above it, '
                'five curved lines with arrowheads, each an arch from the N'
                ' half over to the S half, one inside another with equal '
                'gaps between them. Five more arches, the same, below the '
                'magnet.',
        "params": {'panels': [{'caption': None,
                               'upper': [],
                               'lower': [],
                               'even': {'n': 5, 'step': 13}}],
                   'panel_h': 300,
                   'clip': False},
    },
]
