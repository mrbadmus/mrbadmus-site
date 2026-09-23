"""ks4_art.catalogue_frozen — new KS4 figures for the MRB-352 frozen-window
diagram repair (Mide's 23 Sep 2026 ruling, `frozen_window_allowlist.py`).

Kept in its own file, separate from `ks4_art/catalogue.py`, because this is
a shared worktree and another content lane may be editing that file at the
same time — records here never collide with anything of theirs.

⚠️ KNOWN GAP, not something this file can fix (out of this lane's permitted
touch scope): `build_figures.py` currently does
`from ks4_art.catalogue import CATALOGUE` and only ever reads THAT one list —
it does not discover every `ks4_art/catalogue_*.py` module the way
`ks4_art.load()` discovers every drawer module for the `ART` table. So none
of the ids below are visible to `build_figures.py` yet, and the six rows
that reference a new id here will fail its `unresolved_ks4` check until
something merges every `ks4_art/catalogue_*.py` module's `CATALOGUE` list
(mirroring the discover-not-list pattern `ks4_art/__init__.py` already uses
for drawers). That fix touches `build_figures.py`, which sits outside this
worktree's permitted scope (`ks4_data/questions/**` and
`ks4_art/catalogue*.py` only) — flagged in the run report rather than
patched here.

Every id, title and desc below follows `ks4_art/catalogue.py`'s own rules
verbatim: id prefixed `ks4-fig-`, alt text (`title`/`desc`) describing
GEOMETRY only, never the identification or the answer.
"""

CATALOGUE = [
    # ── ks4-circuit-symbols-h04 — an ammeter-placement question, so the
    # figure must NOT already show an ammeter (that would hand over the
    # answer). Battery + closed switch feeding two branches only. ─────────
    {
        "id": "ks4-fig-circuit-battery-switch-lamp-motor-branches",
        "art": "circuit",
        "title": "A battery and a closed switch on the top wire, splitting "
                 "into two parallel branches — one holding a circle with a "
                 "cross drawn inside it, the other a circle with the "
                 "letter M.",
        "desc": "A battery symbol (repeated long-and-short line pairs) and "
                "a closed switch (a straight line joining two small "
                "circles) sit on the top wire, before it splits into two "
                "parallel branches: one branch carries a lamp symbol (a "
                "circle with a cross drawn inside it), the other a circle "
                "with the letter M. No meter is drawn anywhere in this "
                "circuit.",
        "w": 460, "h": 300,
        "circuit": {
            "topology": "parallel",
            "supply": [{"symbol": "battery", "id": "bat"},
                      {"symbol": "switch", "id": "sw", "state": "closed"}],
            "branches": [
                ("lamp-branch", [{"symbol": "lamp", "id": "lamp1"}]),
                ("motor-branch", [{"symbol": "motor", "id": "motor1"}]),
            ],
        },
    },

    # ── ks4-circuit-symbols-s03 — a single loop with a cell, a closed
    # switch and two lamps, exactly as the stem's setup describes. ────────
    {
        "id": "ks4-fig-circuit-cell-switch-two-lamps-loop",
        "art": "circuit",
        "title": "A single loop with a cell, a closed switch, and two lamp "
                 "symbols, one after another around the loop.",
        "desc": "One rectangular wire loop carrying, in order, a cell, a "
                "closed switch (a straight line joining two small "
                "circles), and two lamp symbols (each a circle with a "
                "cross drawn inside it), all connected one after another "
                "around the same loop.",
        "w": 420, "h": 260,
        "circuit": {
            "topology": "series",
            "loop": [{"symbol": "cell", "id": "cell"},
                    {"symbol": "switch", "id": "sw", "state": "closed"},
                    {"symbol": "lamp", "id": "lamp1"},
                    {"symbol": "lamp", "id": "lamp2"}],
        },
    },

    # ── ks4-acceleration-h03 — the skydiver's velocity–time graph. ────────
    {
        "id": "ks4-fig-graph-velocity-time-skydiver",
        "art": "graph-velocity-time",
        "title": "A velocity–time graph: a line rising steeply from the "
                 "origin, curving so its gradient falls to zero, then "
                 "running flat.",
        "desc": "A velocity-against-time graph. The line starts at the "
                "origin and rises steeply at first, then curves so it "
                "becomes gradually less steep, meeting a horizontal "
                "section at around 14 seconds and staying flat afterward "
                "at a velocity of 55 metres per second.",
        "series": [{"points": [(0, 0), (2, 26), (4, 40), (6, 48), (8, 52),
                              (10, 54), (12, 54.7), (14, 55), (16, 55),
                              (18, 55)],
                   "smooth": True}],
        "x_range": (0, 18), "y_range": (0, 60),
        "x_ticks": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
        "y_ticks": [0, 10, 20, 30, 40, 50, 55],
    },

    # ── ks4-distance-time-graphs-h02 — the runner's distance–time graph. ──
    {
        "id": "ks4-fig-graph-distance-time-runner-400m",
        "art": "graph-distance-time",
        "title": "A distance–time graph: a line rising steeply from the "
                 "origin, then curving to become gradually less steep, "
                 "ending nearly flat at 400 m after 80 s.",
        "desc": "A distance-against-time graph. The line starts at the "
                "origin and rises steeply at first, then curves so it "
                "becomes gradually less steep as time goes on, ending "
                "nearly horizontal at a distance of 400 metres after 80 "
                "seconds.",
        "series": [{"points": [(0, 0), (10, 120), (20, 210), (30, 280),
                              (40, 330), (50, 365), (60, 385), (70, 395),
                              (80, 400)],
                   "smooth": True}],
        "x_range": (0, 85), "y_range": (0, 420),
        "x_ticks": [0, 10, 20, 30, 40, 50, 60, 70, 80],
        "y_ticks": [0, 100, 200, 300, 400],
    },

    # ── ks4-covalent-bonding-s04 — the student's WRONG ammonia diagram,
    # one bonding pair short. ──────────────────────────────────────────────
    {
        "id": "ks4-fig-molecule-nh3-missing-bond",
        "art": "molecule-nh3-missing-bond",
        "title": "A dot-and-cross diagram of ammonia in which one hydrogen "
                 "atom's shell carries no shared pair with the nitrogen "
                 "atom.",
        "desc": "A dot-and-cross diagram showing a nitrogen atom with "
                "three hydrogen atoms arranged around it. Two of the "
                "three nitrogen–hydrogen connections show a complete "
                "shared pair (one dot and one cross together). The third "
                "hydrogen's shell contains only its own single cross, "
                "with no dot from the nitrogen atom alongside it. The "
                "nitrogen atom also carries one further pair of dots, not "
                "shared with any hydrogen atom.",
    },

    # ── ks4-direct-alternating-pd-h02 — the two oscilloscope traces the
    # stem asks the pupil to compare. ──────────────────────────────────────
    {
        "id": "ks4-fig-oscilloscope-compare-5-10",
        "art": "graph-oscilloscope-compare",
        "title": "Two oscilloscope traces on the same screen: trace X "
                 "completes 5 cycles, trace Y completes 10 cycles across "
                 "the same width.",
        "desc": "An oscilloscope screen showing two wave traces plotted "
                "against the same time axis, each drawn as a smooth "
                "up-and-down curve. Trace X completes 5 full cycles "
                "across the screen. Trace Y completes 10 full cycles "
                "across the same width of screen.",
        "traces": [{"cycles": 5, "label": "X"}, {"cycles": 10, "label": "Y"}],
    },
]
