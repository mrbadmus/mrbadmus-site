"""ks4_art.catalogue_run2_bc — KS4 figures for the biology and chemistry rows
of MRB-352 run 2's 174 flagged rows (batch 2), drawn by figlib.

Every record follows the examiner's spec (figures F20–F28): exact labels,
values and what must NOT appear, shapes-only alt text. Several are the
STUDENT'S WRONG DRAWING, on purpose, for "what is wrong with it?" rows —
each is marked below so nobody "fixes" it. Kept in its own file so this lane
cannot collide with another editing `catalogue.py`.
"""

CATALOGUE = [
    # F20 · ks4-food-chains-webs-h25. ⚠️ DELIBERATELY REVERSED: the arrows
    # run from each predator back to its prey (Fox -> Rabbit -> Grass). The
    # question asks what is wrong with it. Do NOT "fix" the arrows, and do
    # not add a legend: stating the convention would point at the answer.
    {"id": "ks4-fig-food-chain-reversed-arrows",
     "art": "food-web",
     "params": {"W": 400, "H": 120, "clearance": 22,
                "nodes": [{"id": "grass", "name": "Grass", "x": 70, "y": 60},
                          {"id": "rabbit", "name": "Rabbit", "x": 200,
                           "y": 60},
                          {"id": "fox", "name": "Fox", "x": 330, "y": 60}],
                "eats": [("fox", "rabbit"), ("rabbit", "grass")]},
     "title": "A food chain: three labelled boxes in a row, Grass, Rabbit and "
              "Fox, joined by arrows.",
     "desc": "One arrow points from Fox to Rabbit, and one from Rabbit to "
             "Grass."},

    # F21 · ks4-endocrine-system-s22 — AQA 8461 §4.5.3.1 "identify the
    # position … on a diagram of the human body". No names; no adrenal
    # glands (a distractor names them).
    {"id": "ks4-fig-body-glands-abcd",
     "art": "body-glands",
     "params": {},
     "title": "An outline of a human head and body with four small shapes "
              "marked A, B, C and D.",
     "desc": "A is inside the head, low down at about eye level. B is in the "
             "front of the neck. C is a long thin shape in the upper abdomen. "
             "D is a pair of small ovals low in the abdomen."},

    # F22 · ks4-homeostasis-h22 — no set-point line, no condition named.
    {"id": "ks4-fig-graph-two-conditions-x-y",
     "art": "graph",
     "params": {"series": [
                    {"label": "X", "smooth": True,
                     "points": [(0, 50), (1, 53), (2, 50), (3, 47), (4, 50),
                                (5, 53), (6, 50), (7, 47), (8, 50), (9, 53),
                                (10, 50)]},
                    {"label": "Y", "smooth": False,
                     "points": [(0, 50), (10, 80)]}],
                "legend": True,
                "x_label": "time", "x_unit": "hours", "x_range": (0, 10),
                "x_ticks": [0, 2, 4, 6, 8, 10],
                # "level of the condition / arbitrary units" is longer than
                # the plot is tall and ran off the card; the stem names it
                "y_label": "level",
                "y_unit": "arbitrary units", "y_range": (0, 100),
                "y_ticks": [0, 20, 40, 60, 80, 100], "W": 480, "H": 380},
     "title": "A graph of two lines against time, labelled X and Y.",
     "desc": "X rises and falls in small, even waves about one level. Y "
             "starts at the same level and rises in a straight line."},

    # F23 · ks4-variation-h14 — 500 seeds, one peak; no curve overlay.
    {"id": "ks4-fig-histogram-seed-mass",
     "art": "columns",
     "params": {"bins": [{"n": n} for n in (5, 30, 90, 140, 130, 75, 25, 5)],
                "edges": [20, 25, 30, 35, 40, 45, 50, 55, 60],
                "x_label": "mass of seed", "x_unit": "mg",
                "y_label": "number of seeds", "y_step": 20, "y_max": 160,
                "touching": True, "W": 480, "H": 380},
     "title": "A histogram of the masses of 500 seeds.",
     "desc": "Eight touching bars from 20 to 60 mg, rising to a single "
             "highest bar at 35 to 40 mg and falling away on both sides."},

    # F24 · ks4-covalent-bonding-s18. ⚠️ DELIBERATELY WRONG: no pair is
    # shared — four H circles stand apart from the C. The C keeps four
    # unpaired dots (fix round 1); each H's cross sits on its own shell,
    # on the side facing the C.
    {"id": "ks4-fig-molecule-ch4-unshared",
     "art": "dot-cross",
     "params": {"formula": "CH4", "title": False, "compact": True,
                "detached": (0, 1, 2, 3), "dashed": True, "nuclei": False,
                "angles": (45, 135, 225, 315), "detached_seat": "shell",
                "detached_gap": 44},
     "title": "A dot-and-cross drawing with a C circle and four separate H "
              "circles around it, not touching it.",
     "desc": "The C circle carries four single dots. Each H circle carries "
             "one cross."},

    # F25 · ks4-covalent-bonding-h23. ⚠️ DELIBERATELY WRONG: one shared pair
    # to each O (the drawing-only table entry "CO2_single"). Counted
    # honestly: 4 dots (2 shared + 2 unpaired on C), 12 crosses (6 per O).
    {"id": "ks4-fig-molecule-co2-single-wrong",
     "art": "dot-cross",
     "params": {"formula": "CO2_single", "title": False, "compact": True,
                "dashed": True, "nuclei": False, "seat": "lens"},
     "title": "A dot-and-cross drawing of an O circle, a C circle and another "
              "O circle in a line, each O overlapping the C.",
     "desc": "Each overlap holds one dot and one cross. The C circle also has "
             "one single dot at the top and one at the bottom. Each O circle "
             "also has two pairs of crosses and one single cross."},

    # F26 · ks4-ionic-bonding-s22 — ions only: no 'before', no arrow, no key.
    # Mg2+ shows its full second shell as crosses (all magnesium's own);
    # the oxide ion's two crosses sit as a pair facing the Mg ion.
    {"id": "ks4-fig-ionic-mgo-ions",
     "art": "ionic-ions",
     "params": {"ions": [
                    {"x": 106, "symbol": "Mg", "charge": "2+",
                     "pairs": {"N": "cross", "E": "cross", "S": "cross",
                               "W": "cross"}},
                    {"x": 380, "symbol": "O", "charge": "2−",
                     "pairs": {"N": "dot", "E": "dot", "S": "dot",
                               "W": "cross"}}],
                "W": 520, "H": 230, "cy": 118, "r": 56},
     "title": "A dot-and-cross drawing of two ions in square brackets: Mg "
              "with 2+ and O with 2−.",
     "desc": "The Mg ion's circle holds eight crosses. The O ion's circle "
             "holds six dots and two crosses, the crosses as a pair on the "
             "side facing the Mg ion."},

    # F27 · ks4-reaction-profiles-h05. ⚠️ DELIBERATELY WRONG: the hump (50)
    # is BELOW the products level (70) of an endothermic profile.
    {"id": "ks4-fig-reaction-profile-endo-wrong",
     "art": "profile-sketch",
     "params": {"points": [(0, 30), (18, 30), (30, 48), (38, 50), (46, 47),
                           (58, 68), (64, 70), (100, 70)],
                "left_at": (0, 18), "right_at": (64, 100),
                "W": 480, "H": 340},
     "title": "A sketch of energy against progress of reaction: a line from "
              "a lower level labelled reactants, over a small hump, up to a "
              "higher level labelled products.",
     "desc": "The top of the hump is lower than the products level."},

    # F28 · ks4-condensation-polymerisation-s10. ⚠️ DELIBERATELY WRONG: a
    # free –OH and a free –COOH left inside the repeat unit (no ester link).
    {"id": "ks4-fig-polyester-repeat-unit-wrong",
     "art": "box-repeat-unit",
     "params": {"left": ("O", "OH"), "right": ("HOOC", "C=O"),
                "W": 480, "H": 150},
     "title": "A student's repeat unit in box notation inside square "
              "brackets marked n.",
     "desc": "Reading left to right: O, a box, OH, then HOOC, a box, and a C "
             "with a double-bonded O, with bonds passing out through both "
             "brackets."},
]
