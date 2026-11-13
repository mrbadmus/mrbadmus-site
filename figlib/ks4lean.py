# -*- coding: utf-8 -*-
"""figlib.ks4lean: the figures a KS4 lean lesson record may place in a card.

A record writes `{"slot": "fig:bar-magnet-field"}` as a card part (docs/lessons/LEAN-RECORD.md).
lean_ks4.py asks `svg(name)` for the inline markup and wraps it in lean_blocks.fig_wrap.

The drawings live in figlib/ks4lean_mag.py (the lean Magnetism lesson; REGISTRY name -> drawer).
Each carries its own #FFFDF8 background and an aria-label. Here each one goes through:
    figlib.web.to_manifest_svg   viewBox only, role="img", <title>/<desc>, flat paint, ids prefixed
                                 (it insists on the library's cream paper rect, so the drawing's own
                                 #FFFDF8 background is swapped to cream for the conversion and put
                                 back after it; the checks then run on the final #FFFDF8 figure)
    figlib.checks.check_figure   element set, 4.5:1 label contrast on the fill underneath, 11px
                                 text at 320px, no label collisions
    figlib.checks.check_paper    one data-role="paper" rect first
and lean's own check: the smallest label must still draw at 11px in a 300px card.
An unknown name, or any failed check, stops the build. The output is width="100%" with a viewBox,
role="img" and the aria-label.
"""
import re

from . import checks, web
from .style import STYLE

MIN_PX = 11.0
CARD_PX = 300.0                 # the narrowest card text column the lean page gives a figure
BG = "#FFFDF8"


def _registry():
    from . import ks4lean_mag
    return ks4lean_mag.REGISTRY


_CACHE = {}


def names():
    return sorted(_registry())


def svg(name):
    """The checked inline SVG for `fig:<name>`. Raises ValueError for an unknown name or a
    figure that fails a check, so the build stops."""
    reg = _registry()
    if name not in reg:
        raise ValueError("lean record: {'slot': 'fig:%s'} names no lean figure. Known: %s"
                         % (name, ", ".join("fig:" + n for n in names())))
    if name in _CACHE:
        return _CACHE[name]
    raw = reg[name]()
    label = re.search(r'aria-label="([^"]*)"', raw).group(1)
    fid = "lean-fig-" + name
    src = raw.replace('fill="%s"' % BG, 'fill="%s"' % STYLE["cream"], 1)
    src = src.replace(' aria-label="%s"' % label, '', 1)
    out = web.to_manifest_svg(src, fid, label, label)
    out = out.replace('fill="%s"' % STYLE["cream"], 'fill="%s"' % BG, 1)
    probs = checks.check_figure(fid, out) + checks.check_paper(fid, out)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', out).group(1).split()]
    small = min(float(f) for f in re.findall(r'font-size="([\d.]+)"', out))
    if small * CARD_PX / vb[2] < MIN_PX:
        probs.append("%s: its smallest label (%g) draws at %.1fpx in a %gpx card (viewBox %g wide); "
                     "the card fit needs %gpx" % (fid, small, small * CARD_PX / vb[2], CARD_PX, vb[2], MIN_PX))
    if probs:
        raise ValueError("lean figure %r fails its checks:\n  %s" % (name, "\n  ".join(probs)))
    out = out.replace("<svg ", '<svg width="100%%" aria-label="%s" ' % label.replace('"', "&quot;"), 1)
    _CACHE[name] = out
    return out
