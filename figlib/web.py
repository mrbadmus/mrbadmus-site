"""figlib.web — the ONE place a library SVG becomes a manifest SVG.

The library's `Canvas` draws for export: a fixed `width`/`height`, a cream
`<rect>` for paper, and `<g>` groups that carry paint for their children.
A question figure travels further than that — into a phone's assignment
page, Set work, a PDFKit worksheet and a resvg raster — and every one of
those surfaces has to draw it the same way with nothing but the SVG itself.
So every manifest figure passes through `to_manifest_svg()` exactly once,
and the drawers never have to know:

  * SCALABLE. `width`/`height` are removed; only `viewBox` remains, so the
    container decides the size and nothing fights it.
  * NAMED. `role="img"` + `aria-labelledby` pointing at a `<title>` and a
    `<desc>` — the same accessibility contract `ks3_art.kit._svg_open`
    enforces for lesson figures, so a screen reader gets the same thing on
    every surface.
  * FLAT. `<g>` is dissolved: its paint attributes are pushed down onto each
    child that does not set its own, then the group is removed. Every shape
    then carries its own paint, which is what makes the figure
    SELF-PAINTING — the rule `figlib.checks` enforces and figure-contract §8
    was written about.
  * COLLISION-FREE. Any `id` a drawer used is prefixed with the figure id
    (and every `url(#…)`/`href="#…"` reference with it), so two figures on
    one page cannot share an id.
  * PAPER. The canvas's cream background rect becomes a rounded card with a
    hairline edge, so the figure reads as a sheet of paper in light AND dark
    mode — the card is never transparent to the page behind it.
  * SMALL. Coordinates are rounded to 2 decimal places.
"""

import re
import xml.etree.ElementTree as ET

from .style import STYLE, q_stroke

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

_Q = "{%s}" % SVG_NS

# Paint a <g> may carry for its children. Pushed down only where the child
# does not already say otherwise — the SVG inheritance rule, made explicit.
_INHERITED = ("fill", "stroke", "stroke-width", "stroke-linecap",
              "stroke-linejoin", "stroke-dasharray", "font-family",
              "font-size", "font-weight", "text-anchor")

_NUM = re.compile(r"-?\d+\.\d{3,}")
_WEIGHTS = {"bold": "700", "normal": "400", "bolder": "700", "lighter": "300"}
CARD_EDGE = "#D9D1BD"


def _round(value):
    return _NUM.sub(lambda m: ("%.2f" % float(m.group(0))).rstrip("0")
                    .rstrip("."), value)


def _flatten(parent):
    """Replace every <g> under `parent` by its children, in place, with the
    group's paint pushed down. A group with a `transform` is refused: the
    manifest's element subset has no group transforms, and silently
    dropping one would move shapes."""
    i = 0
    while i < len(parent):
        el = parent[i]
        if el.tag == _Q + "g":
            if el.get("transform"):
                raise ValueError(
                    "figlib.web: a <g transform=%r> cannot be flattened — "
                    "draw the shapes in place instead." % el.get("transform"))
            _flatten(el)
            kids = list(el)
            for k in kids:
                for attr in _INHERITED:
                    if el.get(attr) is not None and k.get(attr) is None:
                        k.set(attr, el.get(attr))
            parent.remove(el)
            for j, k in enumerate(kids):
                parent.insert(i + j, k)
            i += len(kids)
        else:
            _flatten(el)
            i += 1


def to_manifest_svg(svg, fid, title, desc):
    """A library SVG string -> the manifest's SVG string for figure `fid`."""
    root = ET.fromstring(svg)
    if root.tag != _Q + "svg":
        raise ValueError("figlib.web: %r did not render an <svg> root" % fid)
    vb = root.get("viewBox")
    if not vb:
        w, h = root.get("width"), root.get("height")
        if not (w and h):
            raise ValueError("figlib.web: %r has no viewBox and no size" % fid)
        vb = "0 0 %s %s" % (w, h)
    _, _, W, H = (float(v) for v in vb.split())

    _flatten(root)

    # ── ids: prefix every one, and every reference to one ────────────────
    renames = {}
    for el in root.iter():
        old = el.get("id")
        if old:
            new = "%s-%s" % (fid, old)
            renames[old] = new
            el.set("id", new)
    if renames:
        for el in root.iter():
            for k, v in list(el.attrib.items()):
                for old, new in renames.items():
                    v = v.replace("url(#%s)" % old, "url(#%s)" % new)
                    if v == "#" + old:
                        v = "#" + new
                el.set(k, v)

    # ── the paper card: the canvas's own background rect ─────────────────
    first = next((el for el in root if el.tag == _Q + "rect"), None)
    if (first is not None and first.get("fill", "").upper()
            == STYLE["cream"].upper() and first.get("x") in (None, "0")
            and first.get("y") in (None, "0")):
        edge = q_stroke(W, 1.5)
        first.set("x", "%g" % (edge / 2))
        first.set("y", "%g" % (edge / 2))
        first.set("width", "%g" % (W - edge))
        first.set("height", "%g" % (H - edge))
        first.set("rx", "12")
        first.set("stroke", CARD_EDGE)
        first.set("stroke-width", "%g" % edge)
        # a print renderer drops this one rect on white paper; a screen
        # keeps it, so the figure is a cream card in light AND dark mode
        first.set("data-role", "paper")
    else:
        raise ValueError(
            "figlib.web: %r does not open with the library's cream paper "
            "rect — every figlib figure is drawn on a Canvas, whose first "
            "shape is the paper. Without it the figure would be transparent "
            "to whatever page is behind it, which is exactly how text ends "
            "up on a dark background in dark mode." % fid)

    # ── the accessible name ──────────────────────────────────────────────
    for attr in ("width", "height"):
        if attr in root.attrib:
            del root.attrib[attr]
    attrs = dict(root.attrib)
    root.attrib.clear()
    root.set("viewBox", "0 0 %g %g" % (W, H))
    root.set("role", "img")
    root.set("aria-labelledby", "%s-t %s-d" % (fid, fid))
    root.set("preserveAspectRatio", "xMidYMid meet")
    for k, v in attrs.items():
        if k not in ("viewBox",):
            root.set(k, v)
    t = ET.Element(_Q + "title", {"id": "%s-t" % fid})
    t.text = title
    d = ET.Element(_Q + "desc", {"id": "%s-d" % fid})
    d.text = desc
    root.insert(0, d)
    root.insert(0, t)

    for el in root.iter():
        tag = el.tag[len(_Q):]
        for k, v in list(el.attrib.items()):
            if k not in ("id", "aria-labelledby", "role"):
                el.set(k, _round(v))
        # the worksheet translator reads weights as numbers, never names
        fw = el.get("font-weight")
        if fw is not None:
            el.set("font-weight", _WEIGHTS.get(fw, fw))
        # an open shape says so, rather than leaving a renderer to guess
        # (PDFKit's default for an unstated fill is black)
        if tag in ("line", "polyline") and el.get("fill") is None:
            el.set("fill", "none")
        if el.tail is not None and not el.tail.strip():
            el.tail = None
        if (el.text is not None and not el.text.strip()
                and el.tag != _Q + "text"):
            el.text = None
    return ET.tostring(root, encoding="unicode")
