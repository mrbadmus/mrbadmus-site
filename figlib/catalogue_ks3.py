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
]
