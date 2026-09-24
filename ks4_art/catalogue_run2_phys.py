"""ks4_art.catalogue_run2_phys — MRB-352 run 2, batch 4: KS4 physics except
electricity (forces, magnetism, waves, space, atomic structure, energy).

Declarative records only, discovered by `ks4_art.catalogue_modules()`. Every
figure here is specified in full by the examiner in
`spec174_ks4_physics_other.md`; the `title` is the alt text and says what is
SHOWN, never the answer. Where a desc gives numbers, they are the numbers
printed on the figure, which a sighted pupil also has.
"""


def _graph(x_label, x_unit, y_label, y_unit, x_range, y_range, x_ticks,
           y_ticks, series, **kw):
    p = {"x_label": x_label, "x_unit": x_unit, "y_label": y_label,
         "y_unit": y_unit, "x_range": list(x_range), "y_range": list(y_range),
         "x_ticks": list(x_ticks), "y_ticks": list(y_ticks),
         "series": series}
    p.update(kw)
    return p


def _steps(a, b, step):
    out, v = [], a
    while v <= b + 1e-9:
        out.append(round(v, 6))
        v += step
    return out


def _dt(x_max, x_step, y_max, y_step, series, **kw):
    return _graph("time", "s", "distance", "m", (0, x_max), (0, y_max),
                  _steps(0, x_max, x_step), _steps(0, y_max, y_step),
                  series, **kw)


def _fe(x_unit, x_max, x_ticks, y_max, y_ticks, series, **kw):
    return _graph("extension", x_unit, "force", "N", (0, x_max), (0, y_max),
                  x_ticks, y_ticks, series, **kw)


def _grid(cols, rows, side, dot, to, label, side_, key, **kw):
    p = {"arrows": [{"to": list(to), "label": label, "label_side": side_}],
         "dot": list(dot), "cols": cols, "rows": rows, "side": side,
         "caption": key}
    p.update(kw)
    return p


CATALOGUE = [
    # ── atomic structure ──────────────────────────────────────────────────
    {
        "id": "ks4-fig-nuclide-sodium-23",
        "art": "nuclide",
        "params": {"symbol": "Na", "mass": 23, "atomic": 11, "W": 320,
                   "H": 190, "size": 92, "num": 36},
        "title": "A chemical symbol with one number at its upper left and "
                 "another at its lower left.",
        "desc": "The symbol Na, with 23 written at the top left and 11 at "
                "the bottom left.",
    },
    # ── energy ────────────────────────────────────────────────────────────
    {
        "id": "ks4-fig-sankey-100-65-useful-unlabelled",
        "art": "sankey-simple",
        "params": {"labels": {"in": ["energy in", "100 J"],
                              "useful": ["useful energy"],
                              "wasted": ["wasted", "energy", "65 J"]}},
        "title": "A Sankey diagram: one wide band on the left splits into a "
                 "band that carries straight on to the right and a band "
                 "that turns downward.",
        "desc": "The left band is labelled energy in, 100 J. The band going "
                "right is labelled useful energy, with no value. The band "
                "turning down is labelled wasted energy, 65 J.",
    },
    # ── forces: distance–time graphs ──────────────────────────────────────
    {
        "id": "ks4-fig-graph-dt-school-bus",
        "art": "graph",
        "params": _dt(500, 100, 4000, 1000,
                      [{"points": [[0, 0], [200, 2000], [260, 2000],
                                   [460, 4000]]}],
                      y_grid=_steps(0, 4000, 500)),
        "title": "A distance–time graph made of three straight sections: a "
                 "sloping line, a flat line, then another sloping line.",
        "desc": "Time runs from 0 to 500 s and distance from 0 to 4000 m. "
                "The line rises from the origin to 2000 m at 200 s, stays "
                "at 2000 m until 260 s, then rises to 4000 m at 460 s.",
    },
    {
        "id": "ks4-fig-graph-dt-train-speeding-up",
        "art": "graph",
        "params": _dt(60, 10, 800, 200,
                      [{"points": [[0, 0], [10, 20], [20, 80], [30, 180],
                                   [40, 320], [50, 500], [60, 720]],
                        "smooth": True}],
                      y_grid=_steps(0, 800, 100)),
        "title": "A distance–time graph: a curved line from the origin that "
                 "gets steeper and steeper.",
        "desc": "Time runs from 0 to 60 s and distance from 0 to 800 m.",
    },
    {
        "id": "ks4-fig-graph-dt-cars-j-k",
        "art": "graph",
        "params": _dt(50, 10, 1000, 200,
                      [{"points": [[0, 0], [50, 750]], "label": "car J"},
                       {"points": [[0, 0], [10, 37.5], [20, 150],
                                   [30, 337.5], [40, 600], [50, 937.5]],
                        "smooth": True, "label": "car K"}],
                      y_grid=_steps(0, 1000, 100), legend=True),
        "title": "A distance–time graph with two lines from the origin: a "
                 "straight line, and a curve that gets steeper and crosses "
                 "it.",
        "desc": "Time runs from 0 to 50 s and distance from 0 to 1000 m. "
                "The key shows a solid line for car J and a dashed line for "
                "car K.",
    },
    {
        "id": "ks4-fig-graph-dt-car-waits-then-drives",
        "art": "graph",
        "params": _dt(70, 10, 1000, 200,
                      [{"points": [[0, 200], [25, 200], [65, 1000]]}],
                      y_grid=_steps(0, 1000, 100)),
        "title": "A distance–time graph: a flat line, then a steep straight "
                 "line upwards.",
        "desc": "Time runs from 0 to 70 s and distance from 0 to 1000 m. "
                "The line is flat at 200 m until 25 s, then rises to 1000 m "
                "at 65 s.",
    },
    {
        "id": "ks4-fig-graph-dt-straight-and-flattening",
        "art": "graph",
        "params": _dt(60, 10, 600, 100,
                      [{"points": [[0, 0], [60, 600]], "label": "A"},
                       {"points": [[0, 0], [10, 75], [20, 130], [30, 170],
                                   [40, 192], [50, 200], [60, 200]],
                        "smooth": True, "label": "B"}],
                      y_grid=_steps(0, 600, 50), legend=True),
        "title": "A distance–time graph with two lines from the origin: a "
                 "straight line, and a curve that becomes flat.",
        "desc": "Time runs from 0 to 60 s and distance from 0 to 600 m. "
                "The key shows a solid line for A and a dashed line for B.",
    },
    {
        "id": "ks4-fig-graph-dt-runner-2400m",
        "art": "graph",
        "params": _dt(700, 100, 2500, 500,
                      [{"points": [[0, 0], [100, 620], [200, 1160],
                                   [300, 1620], [400, 2000], [500, 2280],
                                   [600, 2400], [700, 2400]],
                        "smooth": True}],
                      y_grid=_steps(0, 2500, 100)),
        "title": "A distance–time graph: a curved line from the origin that "
                 "becomes less steep and then flat.",
        "desc": "Time runs from 0 to 700 s and distance from 0 to 2500 m.",
    },
    {
        "id": "ks4-fig-graph-dt-lift-steps",
        "art": "graph",
        "params": _dt(25, 5, 25, 5,
                      [{"points": [[0, 0], [4, 8], [10, 8], [14, 16],
                                   [20, 16], [24, 24]]}]),
        "title": "A distance–time graph shaped like a staircase: sloping "
                 "straight sections separated by flat sections.",
        "desc": "Time runs from 0 to 25 s and distance from 0 to 25 m.",
    },
    {
        "id": "ks4-fig-graph-dt-cyclist-slows",
        "art": "graph",
        "params": _dt(40, 10, 250, 50,
                      [{"points": [[0, 0], [10, 90], [20, 180], [22, 196.5],
                                   [24, 210], [26, 220.5], [28, 228],
                                   [30, 232.5], [32, 234], [36, 234],
                                   [40, 234]],
                        "smooth": True}],
                      x_grid=_steps(0, 40, 5), y_grid=_steps(0, 250, 10)),
        "title": "A distance–time graph: a straight line from the origin "
                 "that then curves over and becomes flat.",
        "desc": "Time runs from 0 to 40 s and distance from 0 to 250 m.",
    },
    {
        "id": "ks4-fig-graph-dt-parallel-journeys",
        "art": "graph",
        "params": _dt(50, 10, 200, 50,
                      [{"points": [[0, 0], [20, 100]], "label": "A"},
                       {"points": [[10, 0], [50, 200]], "label": "B"}],
                      y_grid=_steps(0, 200, 25), legend=True),
        "title": "A distance–time graph with two parallel straight lines, "
                 "one longer than the other.",
        "desc": "Time runs from 0 to 50 s and distance from 0 to 200 m. "
                "The key shows a solid line for A and a dashed line for B.",
    },
    # ── forces: elasticity ────────────────────────────────────────────────
    {
        "id": "ks4-fig-graph-force-extension-two-springs",
        "art": "graph",
        "params": _fe("m", 0.10, [0, 0.02, 0.04, 0.06, 0.08, 0.10], 10,
                      _steps(0, 10, 2),
                      [{"points": [[0, 0], [0.10, 8]], "label": "spring X"},
                       {"points": [[0, 0], [0.10, 4]], "label": "spring Y"}],
                      legend=True),
        "title": "A force–extension graph with two straight lines from the "
                 "origin, one steeper than the other.",
        "desc": "Extension runs from 0 to 0.10 m and force from 0 to 10 N. "
                "The key shows a solid line for spring X and a dashed line "
                "for spring Y.",
    },
    {
        "id": "ks4-fig-graph-force-extension-past-limit",
        "art": "graph",
        "params": _fe("cm", 12, _steps(0, 12, 2), 6, _steps(0, 6, 1),
                      [{"points": [[0, 0], [2, 1], [4, 2], [6, 3], [8, 4],
                                   [9, 4.35], [10, 4.6], [11, 4.8],
                                   [12, 4.95]],
                        "smooth": True}]),
        "title": "A force–extension graph: a straight line from the origin "
                 "that then curves over, becoming less steep.",
        "desc": "Extension runs from 0 to 12 cm and force from 0 to 6 N.",
    },
    {
        "id": "ks4-fig-graph-force-extension-offset",
        "art": "graph",
        "params": _fe("cm", 12, _steps(0, 12, 2), 6, _steps(0, 6, 1),
                      [{"points": [[3.1, 1], [4.9, 2], [7.0, 3], [9.1, 4],
                                   [10.9, 5]],
                        "line": False, "markers": "x"},
                       {"points": [[1.0, 0], [12, 5.5]], "colour": "ink"}],
                      x_grid=_steps(0, 12, 1)),
        "title": "A force–extension graph: five plotted crosses and a "
                 "straight line of best fit that meets the extension axis "
                 "to the right of the origin.",
        "desc": "Extension runs from 0 to 12 cm and force from 0 to 6 N. "
                "The line meets the extension axis at 1 cm.",
    },
    # ── forces: free body diagrams ────────────────────────────────────────
    {
        "id": "ks4-fig-free-body-sign-40n",
        "art": "free-body",
        "params": {"obj": {"kind": "dot", "at": [90, 150], "r": 7},
                   "arrows": [{"from": [90, 150], "dy": -110,
                               "label": "tension 40 N"},
                              {"from": [90, 150], "dy": 110,
                               "label": "weight 40 N"}],
                   "W": 260, "H": 300},
        "title": "A free body diagram: a dot with one arrow pointing up and "
                 "one pointing down, the same length.",
        "desc": "The upward arrow is labelled tension 40 N and the downward "
                "arrow weight 40 N.",
    },
    {
        "id": "ks4-fig-free-body-parachutist-three-arrows",
        "art": "free-body",
        "params": {"obj": {"kind": "square", "at": [190, 190], "size": 40},
                   "arrows": [{"from": [190, 210], "dy": 120,
                               "label": "weight"},
                              {"from": [172, 170], "dy": -75,
                               "label": "drag", "label_side": "left"},
                              {"from": [208, 170], "dy": -50,
                               "label": "pull of the parachute"}],
                   "W": 380, "H": 380},
        "title": "A free body diagram: a small square with one arrow "
                 "pointing down and two arrows pointing up.",
        "desc": "The downward arrow is labelled weight. The two upward "
                "arrows are labelled drag and pull of the parachute.",
    },
    # ── forces: scale drawings on a grid (AQA 8463 §4.5.1.4, HT) ─────────
    {
        "id": "ks4-fig-force-grid-ring-8n-6n",
        "art": "force-grid",
        "params": {"arrows": [{"to": [2, 9], "label": "8 N",
                               "label_side": "left"},
                              {"to": [8, 1], "label": "6 N",
                               "label_side": "below"}],
                   "dot": [2, 1], "cols": 10, "rows": 10, "side": 30,
                   "caption": "1 square = 1 N"},
        "title": "Two force arrows drawn to scale on a square grid from one "
                 "dot: one pointing up and one pointing right.",
        "desc": "The upward arrow is 8 squares long and labelled 8 N; the "
                "arrow to the right is 6 squares long and labelled 6 N. The "
                "key reads 1 square = 1 N.",
    },
    {
        "id": "ks4-fig-force-grid-50n-4r-3u",
        "art": "force-grid",
        "params": _grid(7, 5, 40, (1, 1), (5, 4), "50 N", "upper-left",
                        "1 square = 10 N"),
        "title": "A force arrow drawn to scale on a square grid, pointing "
                 "up and to the right, with a scale key.",
        "desc": "The arrow is labelled 50 N. It runs 4 squares to the right "
                "and 3 squares up. The key reads 1 square = 10 N.",
    },
    {
        "id": "ks4-fig-force-grid-100n-8r-6u",
        "art": "force-grid",
        "params": _grid(10, 8, 30, (1, 1), (9, 7), "100 N", "upper-left",
                        "1 square = 10 N", ground_row=1),
        "title": "A force arrow drawn to scale on a square grid, rising "
                 "from a dot on a ground line, with a scale key.",
        "desc": "The arrow is labelled 100 N. It runs 8 squares to the "
                "right and 6 squares up. The key reads 1 square = 10 N.",
    },
    {
        "id": "ks4-fig-force-grid-250n-4r-3d",
        "art": "force-grid",
        "params": _grid(7, 5, 40, (1, 4), (5, 1), "250 N", "upper-right",
                        "1 square = 50 N"),
        "title": "A force arrow drawn to scale on a square grid, pointing "
                 "down and to the right, with a scale key.",
        "desc": "The arrow is labelled 250 N. It runs 4 squares to the "
                "right and 3 squares down. The key reads 1 square = 50 N.",
    },
    {
        "id": "ks4-fig-force-grid-260n-12r-5u",
        "art": "force-grid",
        "params": _grid(14, 7, 32, (1, 1), (13, 6), "260 N", "upper-left",
                        "1 square = 20 N"),
        "title": "A force arrow drawn to scale on a square grid, rising "
                 "gently to the right, with a scale key.",
        "desc": "The arrow is labelled 260 N. It runs 12 squares to the "
                "right and 5 squares up. The key reads 1 square = 20 N.",
    },
    {
        "id": "ks4-fig-force-grid-500n-4r-3u",
        "art": "force-grid",
        "params": _grid(7, 5, 40, (1, 1), (5, 4), "500 N", "upper-left",
                        "1 square = 100 N"),
        "title": "A force arrow drawn to scale on a square grid, pointing "
                 "up and to the right, with a scale key.",
        "desc": "The arrow is labelled 500 N. It runs 4 squares to the "
                "right and 3 squares up. The key reads 1 square = 100 N.",
    },
    # ── forces: gravity ───────────────────────────────────────────────────
    {
        "id": "ks4-fig-graph-weight-mass-planet",
        "art": "graph",
        "params": _graph("mass", "kg", "weight", "N", (0, 10), (0, 40),
                         _steps(0, 10, 2), _steps(0, 40, 10),
                         [{"points": [[0, 0], [10, 38]]}],
                         x_grid=_steps(0, 10, 1), y_grid=_steps(0, 40, 2),
                         end_dot=True),
        "title": "A graph of weight against mass: a straight line from the "
                 "origin, ending with a dot.",
        "desc": "Mass runs from 0 to 10 kg and weight from 0 to 40 N. The "
                "line ends at 10 kg and 38 N.",
    },
    {
        "id": "ks4-fig-graph-weight-mass-two-worlds",
        "art": "graph",
        "params": _graph("mass", "kg", "weight", "N", (0, 10), (0, 100),
                         _steps(0, 10, 2), _steps(0, 100, 20),
                         [{"points": [[0, 0], [10, 98]]},
                          {"points": [[0, 0], [10, 16]]}]),
        "title": "A graph of weight against mass with two straight lines "
                 "from the origin, one much steeper than the other.",
        "desc": "Mass runs from 0 to 10 kg and weight from 0 to 100 N. One "
                "line is solid and the other dashed.",
    },
    # ── magnetism ─────────────────────────────────────────────────────────
    {
        "id": "ks4-fig-solenoid-current-front-back",
        "art": "solenoid",
        "params": {"current": "down-front"},
        "title": "A coil of wire with six turns and a horizontal axis, with "
                 "arrows on the wire and a lead at each end.",
        "desc": "The front of each turn is a solid line slanting down to "
                "the right, with an arrow pointing down along it; the back "
                "of each turn is a dashed line. The lead at each end has an "
                "arrow pointing to the right. A key explains solid and "
                "dashed.",
    },
    {
        "id": "ks4-fig-graph-electromagnet-strength-current",
        "art": "graph",
        "params": _graph("current", "A", "magnetic field strength", None,
                         (0, 5), (0, 100), _steps(0, 5, 1), [],
                         [{"points": [[0, 0], [0.5, 20], [1, 40], [1.5, 58],
                                      [2, 72], [2.5, 82], [3, 88],
                                      [3.5, 91], [4, 93], [5, 95]],
                           "smooth": True}],
                         y_grid=_steps(0, 100, 20)),
        "title": "A graph of magnetic field strength against current: a "
                 "line from the origin that rises almost straight, then "
                 "bends over and becomes nearly flat.",
        "desc": "Current runs from 0 to 5 A. The field-strength axis has "
                "no numbers.",
    },
    {
        "id": "ks4-fig-magnet-compasses-near-north",
        "art": "magnet-compasses",
        "params": {"magnet": {"x0": 80, "x1": 320, "y0": 95, "y1": 145,
                              "left": "S"},
                   "compasses": [{"at": [360, 60], "label": "A",
                                  "label_pos": "upper-right"},
                                 {"at": [360, 180], "label": "B",
                                  "label_pos": "lower-right"}],
                   "W": 460, "H": 240},
        "title": "A bar magnet with two empty compass circles, one above "
                 "and one below its right-hand end.",
        "desc": "The magnet's left end is marked S and its right end N. "
                "Compass A is just above and beyond the N end; compass B is "
                "just below and beyond it.",
    },
    {
        "id": "ks4-fig-magnet-compass-beside-middle",
        "art": "magnet-compasses",
        "params": {"magnet": {"x0": 80, "x1": 320, "y0": 95, "y1": 145,
                              "left": "S"},
                   "compasses": [{"at": [200, 62]}],
                   "key": {"at": [372, 212], "len": 30},
                   "W": 460, "H": 240},
        "title": "A bar magnet with an empty compass circle above its "
                 "middle, and a small direction key.",
        "desc": "The magnet's left end is marked S and its right end N. The "
                "key shows north up the page and east to the right.",
    },
    {
        "id": "ks4-fig-magnet-compasses-on-axis",
        "art": "magnet-compasses",
        "params": {"magnet": {"x0": 110, "x1": 350, "y0": 75, "y1": 125,
                              "left": "S"},
                   "compasses": [{"at": [60, 100], "label": "A",
                                  "label_pos": "above"},
                                 {"at": [400, 100], "label": "B",
                                  "label_pos": "above"}],
                   "W": 460, "H": 200},
        "title": "A bar magnet with an empty compass circle beyond each "
                 "end, in line with the magnet.",
        "desc": "The magnet's left end is marked S and its right end N. "
                "Compass A is beyond the S end and compass B beyond the N "
                "end.",
    },
    # ── space ─────────────────────────────────────────────────────────────
    {
        "id": "ks4-fig-graph-hubble-two-galaxies",
        "art": "graph",
        "params": _graph("distance", "Mpc", "recession speed", "km/s",
                         (0, 200), (0, 14000), _steps(0, 200, 50),
                         _steps(0, 14000, 2000),
                         [{"points": [[0, 0], [200, 14000]]},
                          {"points": [[50, 3500], [150, 10500]],
                           "line": False, "markers": "dot",
                           "colour": "ink"}],
                         x_grid=_steps(0, 200, 10),
                         y_grid=_steps(0, 14000, 500)),
        "title": "A graph of recession speed against distance: a straight "
                 "line from the origin with two dots on it.",
        "desc": "Distance runs from 0 to 200 Mpc and speed from 0 to "
                "14 000 km/s.",
    },
    {
        "id": "ks4-fig-graph-hubble-forty-galaxies",
        "art": "graph",
        "params": _graph("distance", "Mpc", "recession speed", "km/s",
                         (0, 200), (0, 14000), _steps(0, 200, 50),
                         _steps(0, 14000, 2000),
                         [{"points": [[9, 450], [11, 1600], [16, 2000],
                                      [22, 1000], [26, 2250], [30, 1500],
                                      [35, 2100], [40, 2900], [44, 2750],
                                      [48, 3400], [55, 3750], [58, 4400],
                                      [65, 4700], [68, 5400], [73, 5800],
                                      [76, 4950], [81, 6100], [86, 6150],
                                      [92, 7300], [94, 6150], [99, 7500],
                                      [104, 7800], [111, 8150],
                                      [113, 8350], [120, 8950],
                                      [122, 9150], [129, 8150],
                                      [133, 9650], [138, 9500],
                                      [140, 8950], [147, 10650],
                                      [151, 10000], [156, 11500],
                                      [160, 11000], [165, 11050],
                                      [170, 11200], [173, 11550],
                                      [177, 11750], [183, 12700],
                                      [188, 13900]],
                           "line": False, "markers": "dot"},
                          {"points": [[0, 0], [200, 14000]],
                           "colour": "ink"}]),
        "title": "A scatter graph of recession speed against distance: "
                 "forty dots rising from left to right, scattered either "
                 "side of a straight line through the origin.",
        "desc": "Distance runs from 0 to 200 Mpc and speed from 0 to "
                "14 000 km/s.",
    },
    # ── waves ─────────────────────────────────────────────────────────────
    {
        "id": "ks4-fig-echo-sounder-display",
        "art": "echo-sounder",
        "params": {"seabed": [42, 41, 43, 44, 42, 40, 41, 43],
                   "patch": {"dashes": [[0.40, 19, 24], [0.43, 22, 20],
                                        [0.45, 18, 28], [0.48, 24, 22],
                                        [0.50, 20, 26], [0.52, 23, 18],
                                        [0.54, 19, 24], [0.56, 21, 20],
                                        [0.57, 24, 18]],
                             "label_depth": 21}},
        "title": "An echo-sounder screen: depth down the side, a thick wavy "
                 "line near the bottom, and a small patch of faint marks "
                 "labelled X higher up.",
        "desc": "Depth runs from 0 m at the top to 50 m at the bottom. The "
                "thick line labelled seabed runs across the whole screen at "
                "about 40 to 44 m. The faint patch X is at about 18 to 24 m "
                "and covers only the middle part of the screen.",
    },
    {
        "id": "ks4-fig-graph-pressure-distance-sound",
        "art": "wave-graph",
        "params": {"x_label": "distance", "y_label": "air pressure"},
        "title": "A graph of air pressure against distance: a smooth wavy "
                 "line above the distance axis.",
        "desc": "The curve rises and falls evenly, two and a half times, "
                "about a dashed middle line. The axes have no numbers.",
    },
    {
        "id": "ks4-fig-wavefronts-student-refraction",
        "art": "wavefront-diagram",
        "params": {"i_deg": 40, "r_deg": 60, "refracted_head_at": 133},
        "title": "A wave front diagram: a ray with evenly spaced wave fronts "
                 "meets a horizontal boundary at a dashed normal and "
                 "continues below it with more closely spaced fronts.",
        "desc": "Above the boundary, material 1; below it, material 2. The "
                "ray below the boundary makes a larger angle with the "
                "normal than the ray above it.",
    },
]
