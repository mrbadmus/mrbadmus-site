"""ks4_art.graphs — every KS4 line/curve graph, built on `ks3_art.kit._plot`.

Distance-time, velocity-time, a heating/cooling curve with its plateau, and
an oscilloscope trace are all the SAME primitive with different labels and
(for the oscilloscope) a generated sine series — never four hand-tuned axis
mappings that could quietly disagree with each other.
"""

import math

from ks3_art.kit import _plot


def draw_distance_time(fig):
    """`fig["series"]` — a bare list of `(t, s)` points, or a list of
    series dicts (see `_plot`). `fig["x_unit"]`/`fig["y_unit"]` default to
    's' and 'm'; override for a different scale."""
    series = fig.get("series")
    if not series:
        raise ValueError("distance-time figure %r has no series." % fig.get("id"))
    return _plot(fig, fig.get("w", 380), fig.get("h", 260), series,
                "time", fig.get("x_unit", "s"), "distance", fig.get("y_unit", "m"),
                x_range=fig.get("x_range"), y_range=fig.get("y_range"),
                x_ticks=fig.get("x_ticks"), y_ticks=fig.get("y_ticks"),
                origin_marker=fig.get("origin_marker", True))


def draw_velocity_time(fig):
    series = fig.get("series")
    if not series:
        raise ValueError("velocity-time figure %r has no series." % fig.get("id"))
    return _plot(fig, fig.get("w", 380), fig.get("h", 260), series,
                "time", fig.get("x_unit", "s"), "velocity", fig.get("y_unit", "m/s"),
                x_range=fig.get("x_range"), y_range=fig.get("y_range"),
                x_ticks=fig.get("x_ticks"), y_ticks=fig.get("y_ticks"),
                origin_marker=fig.get("origin_marker", True))


def draw_heating_cooling(fig):
    """`fig["series"]` carries the plateau explicitly — e.g.
    `[(0,20),(2,20),(2,100),(6,100),(8,140)]` — the flat run IS the phase
    change, and it is authored as real points, never smoothed away."""
    series = fig.get("series")
    if not series:
        raise ValueError("heating/cooling figure %r has no series." % fig.get("id"))
    return _plot(fig, fig.get("w", 380), fig.get("h", 260), series,
                "time", fig.get("x_unit", "min"), "temperature",
                fig.get("y_unit", "°C"),
                x_range=fig.get("x_range"), y_range=fig.get("y_range"),
                x_ticks=fig.get("x_ticks"), y_ticks=fig.get("y_ticks"),
                origin_marker=fig.get("origin_marker", False))


def draw_oscilloscope(fig):
    """`fig["cycles"]` complete cycles drawn across a `divisions_x` x
    `divisions_y` division grid — exactly the trace-reading questions ask
    a pupil to count. Generated analytically (200+ sample points), never
    hand-placed, so the number of cycles ACTUALLY shown always matches
    what the figure claims."""
    cycles = fig.get("cycles")
    if not cycles or cycles <= 0:
        raise ValueError(
            "oscilloscope figure %r needs a positive `cycles`." % fig.get("id"))
    dx = fig.get("divisions_x", 10)
    dy = fig.get("divisions_y", 8)
    amplitude = fig.get("amplitude", dy / 2.0 - 1)
    n = max(240, int(cycles) * 48)
    pts = [(dx * i / float(n),
           amplitude * math.sin(2 * math.pi * cycles * i / float(n)))
          for i in range(n + 1)]
    return _plot(fig, fig.get("w", 360), fig.get("h", 260), pts,
                "time", "div", "voltage", "div",
                x_range=(0, dx), y_range=(-dy / 2.0, dy / 2.0),
                x_ticks=list(range(0, dx + 1)),
                y_ticks=list(range(int(-dy / 2), int(dy / 2) + 1)),
                origin_marker=False)


ART = {
    "graph-distance-time": draw_distance_time,
    "graph-velocity-time": draw_velocity_time,
    "graph-heating-cooling": draw_heating_cooling,
    "graph-oscilloscope": draw_oscilloscope,
}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    def _check(name, svg):
        ET.fromstring(svg)
        print("ok: %-24s %6d bytes" % (name, len(svg)))

    _check("distance-time", draw_distance_time(
        {"id": "sc-dt", "title": "t", "desc": "d",
         "series": [(0, 0), (2, 4), (4, 4), (6, 10)]}))
    _check("velocity-time", draw_velocity_time(
        {"id": "sc-vt", "title": "t", "desc": "d",
         "series": [(0, 0), (14, 55)]}))
    _check("heating-cooling", draw_heating_cooling(
        {"id": "sc-heat", "title": "t", "desc": "d",
         "series": [(0, 20), (2, 20), (2, 100), (6, 100), (8, 140)]}))
    _check("oscilloscope · 5 cycles", draw_oscilloscope(
        {"id": "sc-osc", "title": "t", "desc": "d", "cycles": 5}))
    print("graphs.py self-check: every drawer renders well-formed SVG")
