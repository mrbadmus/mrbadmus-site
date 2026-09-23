"""ks4_art.oscilloscope_compare — two oscilloscope traces on one screen.

Added for the MRB-352 frozen-window repair of `ks4-direct-alternating-pd-h02`,
whose stem says "Trace X shows 5 complete cycles... Trace Y shows 10 complete
cycles... at the same time base setting" without ever showing either trace —
exactly the pattern Mide's standing rule forbids (a diagram described in
words instead of drawn). `ks4_art.graphs.draw_oscilloscope` draws only ONE
trace, so it cannot serve a question that is fundamentally a comparison
between two.

A new module rather than an addition to `ks4_art/graphs.py`: this is a
shared worktree and another lane may be editing that file concurrently, so
adding a new module (discovered automatically by `ks4_art.load()`) is the
safe way to add one drawer without touching a file someone else owns this
run.

Reuses `ks3_art.kit._plot` verbatim for the actual plotting — traces are
told apart by dash pattern plus an end label ("X", "Y"), exactly as `_plot`
already requires for any multi-series graph. No new plotting logic; only
the analytic sine-point generation `ks4_art.graphs.draw_oscilloscope`
already uses, repeated here for two series instead of one.
"""

import math

from ks3_art.kit import _plot


def _sine_points(cycles, n, divisions_x, amplitude):
    return [(divisions_x * i / float(n),
            amplitude * math.sin(2 * math.pi * cycles * i / float(n)))
           for i in range(n + 1)]


def draw_oscilloscope_compare(fig):
    """`fig["traces"]` — 2+ dicts of `{"cycles": int, "label": str}`, each
    drawn as that many complete sine cycles across the SAME screen width and
    time-base — the comparison the stem asks the pupil to make is the thing
    actually drawn, not a number they have to hold in their head."""
    traces = fig.get("traces")
    if not traces or len(traces) < 2:
        raise ValueError(
            "oscilloscope-compare figure %r needs 2 or more `traces`."
            % fig.get("id"))
    for t in traces:
        if not t.get("cycles") or not t.get("label"):
            raise ValueError(
                "oscilloscope-compare figure %r has a trace with no "
                "`cycles` or no `label`." % fig.get("id"))
    dx = fig.get("divisions_x", 10)
    dy = fig.get("divisions_y", 8)
    amplitude = fig.get("amplitude", dy / 2.0 - 1)
    n = max(240, int(max(t["cycles"] for t in traces)) * 48)
    series = [{"points": _sine_points(t["cycles"], n, dx, amplitude),
              "label": t["label"]}
             for t in traces]
    return _plot(fig, fig.get("w", 380), fig.get("h", 260), series,
                "time", "div", "voltage", "div",
                x_range=(0, dx), y_range=(-dy / 2.0, dy / 2.0),
                x_ticks=list(range(0, dx + 1)),
                y_ticks=list(range(int(-dy / 2), int(dy / 2) + 1)),
                origin_marker=False)


ART = {
    "graph-oscilloscope-compare": draw_oscilloscope_compare,
}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    svg = draw_oscilloscope_compare({
        "id": "sc-osc-compare", "title": "t", "desc": "d",
        "traces": [{"cycles": 5, "label": "X"}, {"cycles": 10, "label": "Y"}],
    })
    ET.fromstring(svg)
    print("ok: oscilloscope-compare %6d bytes" % len(svg))
    print("oscilloscope_compare.py self-check: renders well-formed SVG")
