#!/usr/bin/env python3
"""make_test_plate.py — a stand-in plate for the flat renderer (MRB-190).

The heart's 2D diagram has not been drawn: ``assets.fallback`` in
``content/heart.json`` is a Stage-8 TODO, exactly as ``assets.mesh`` is. The
mesh renderer answered that with a generated test specimen; this is the same
move for the flat one, and under the same discipline:

  * it is a GEOMETRY FIXTURE, never content;
  * it is underscore-prefixed and gitignored, like ``_test-specimen.glb``;
  * it evaporates the moment a real ``.svg`` lands in ``public/assets/``,
    with no change in ``src/``;
  * and it is drawn so that NOBODY could mistake it for an authored diagram.

That last point is the one that matters and the one that shaped every line
below. A plausible-looking heart diagram with numbered parts is precisely the
thing that could pass review and reach a student, so this plate carries no
anatomy at all: neutral grey discs on a grid, numbered, with the words TEST
PLATE and GENERATED GEOMETRY FIXTURE printed across it. There is no anatomical
label anywhere in this file, and there must never be one — the hotspot labels
come from the content record, and those are Mide's to write at Stage 8.

The marker positions are the same deterministic spread the flat renderer
derives for an unauthored ``position2d`` (see ``renderer/flat/points.ts``). If
the two ever drift the dots simply sit off their discs on a fixture, which is
cosmetic; the formula is duplicated rather than shared because a Python build
script and a TypeScript module have no honest way to share one, and both cite
each other.

Usage:  python3 tools/make_test_plate.py
"""

from __future__ import annotations

import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
OUT = os.path.join(STUDIO, "public", "assets", "_test-plate.svg")
HEART = os.path.join(STUDIO, "content", "heart.json")

# The plate's coordinate space. `position2d` is authored in these units, so the
# renderer scales the plate to its stage and places dots in the same space.
WIDTH = 720
HEIGHT = 560

# Kept deliberately away from the palette's warm range: this is a fixture, and
# it should not read as part of the designed surface.
PLATE = "#F4F1EC"
GRID = "#E3DFD8"
FORM = "#C9C3B9"
FORM_EDGE = "#AFA79B"
MARK = "#8A8279"

GOLDEN_ANGLE = math.pi * (3 - math.sqrt(5))


def stand_in_point(index: int, count: int) -> tuple[float, float]:
    """Mirror of standInPoint() in src/renderer/flat/points.ts."""
    radius = 0.30 * math.sqrt((index + 0.5) / max(count, 1))
    angle = index * GOLDEN_ANGLE
    return (
        WIDTH * (0.5 + radius * math.cos(angle)),
        HEIGHT * (0.48 + radius * math.sin(angle)),
    )


def hotspot_count() -> int:
    with open(HEART, encoding="utf-8") as fh:
        return len(json.load(fh)["hotspots"])


def build(count: int) -> str:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
        'width="%d" height="%d" role="img" '
        'aria-label="Generated test plate, not an anatomical diagram">'
        % (WIDTH, HEIGHT, WIDTH, HEIGHT),
        "<defs><pattern id='g' width='36' height='36' patternUnits='userSpaceOnUse'>"
        "<path d='M36 0H0V36' fill='none' stroke='%s' stroke-width='1'/>"
        "</pattern></defs>" % GRID,
        "<rect width='%d' height='%d' fill='%s'/>" % (WIDTH, HEIGHT, PLATE),
        "<rect width='%d' height='%d' fill='url(#g)'/>" % (WIDTH, HEIGHT),
    ]

    # Neutral discs, one per hotspot, at the renderer's stand-in points. Circles
    # on a grid: a shape with no anatomy in it.
    for i in range(count):
        cx, cy = stand_in_point(i, count)
        parts.append(
            "<circle cx='%.1f' cy='%.1f' r='54' fill='%s' stroke='%s' "
            "stroke-width='2'/>" % (cx, cy, FORM, FORM_EDGE))
        parts.append(
            "<text x='%.1f' y='%.1f' font-family='monospace' font-size='19' "
            "fill='%s' text-anchor='middle'>%02d</text>"
            % (cx, cy + 7, MARK, i + 1))

    parts.append(
        "<text x='%d' y='42' font-family='monospace' font-size='17' "
        "letter-spacing='3' fill='%s' text-anchor='middle'>TEST PLATE</text>"
        % (WIDTH // 2, MARK))
    parts.append(
        "<text x='%d' y='%d' font-family='monospace' font-size='13' "
        "letter-spacing='2' fill='%s' text-anchor='middle'>"
        "GENERATED GEOMETRY FIXTURE &#183; NOT AN ANATOMICAL DIAGRAM</text>"
        % (WIDTH // 2, HEIGHT - 26, MARK))
    parts.append(
        "<rect x='6' y='6' width='%d' height='%d' fill='none' stroke='%s' "
        "stroke-width='2' stroke-dasharray='9 7'/>"
        % (WIDTH - 12, HEIGHT - 12, FORM_EDGE))
    parts.append("</svg>")
    return "".join(parts)


def main() -> int:
    count = hotspot_count()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    svg = build(count)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("wrote %s" % os.path.relpath(OUT, STUDIO))
    print("  %d marker(s), %d bytes, viewBox %d x %d"
          % (count, len(svg.encode("utf-8")), WIDTH, HEIGHT))
    print("  a geometry fixture: no anatomy, no authored label, gitignored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
