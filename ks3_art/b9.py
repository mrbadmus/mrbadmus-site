"""ks3_art.b9 — B9's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import re
from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_CARD,
    _SVG_GROUND,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_MONO,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _b7_need,
    _b8_group,
    _b8_plain,
    _b8_round,
    _b9_json,
    _b9_placeholders,
    _circle,
    _label,
    _line,
    _mono,
    _path,
    _pctnum,
    _rect,
    _svg_open,
    _svg_text,
    e,
    rich,
    t,
)


def _food_web(fig):
    """A food web: trophic rows bottom-up, arrows pointing the way energy goes.

    ⚖️ ARROW DIRECTION IS THE SCIENCE, not a drawing convention. `ECO-01` — the
    first misconception in the family — is *"the arrow points at what the animal
    eats"*, and b9-01's own confrontation says examiners mark arrow direction
    and it is the most commonly lost mark in the topic. So every arrowhead here
    sits at the EATER, the marker is named `eats-arrow` so a misuse is legible
    in the markup, and the legend states the rule in words on the drawing
    itself. A food-web figure that got this backwards would teach the
    misconception the lesson beside it exists to remove.

    Rows are authored top-down (top predator first) because that is the
    document order a screen reader traversing the SVG would meet, and reading
    "tertiary consumers … producers" down the web is the sense-making order.
    They are DRAWN bottom-up from the same list, which is the sense-making
    order for the eye — energy climbing.

    `thread` optionally names one chain through the web. It is drawn in accent
    with a 3px stroke AND a numbered badge on each node AND a legend entry:
    three channels, because the never-colour-alone rule means a student who
    cannot separate the orange from the ink still sees which nodes are on the
    thread and in what order.
    """
    d = fig.get("data") or {}
    rows = d.get("rows") or []
    if not rows:
        raise ValueError("food-web figure %r has no rows." % fig.get("id"))

    GUTTER, PAD_X, PAD_TOP = 132, 22, 30
    W, ROW_H, NODE_H = 760, 84, 42
    thread = list(d.get("thread") or [])
    tpos = {nid: i + 1 for i, nid in enumerate(thread)}

    # Geometry first, markup second — the links need every node's box before
    # any of them can be routed, so nothing is emitted until all of it is known.
    box, order = {}, []
    for r, row in enumerate(rows):
        nodes = row.get("nodes") or []
        # ⚠️ NO INVERSION HERE, and the first version had one. The rows are
        # already authored in the order they are drawn — tertiary consumers
        # first, producers and then decomposers last — so `r` IS the visual row
        # and `(len(rows) - 1 - r)` flipped the whole web upside down: the
        # decomposers came out along the top and the sparrowhawk along the
        # bottom, with every arrow pointing the wrong way up the page. The
        # arrowheads were still on the eaters, so nothing about the data was
        # wrong; the drawing simply taught the opposite of it. Only visible by
        # looking at it.
        y = PAD_TOP + r * ROW_H
        span = W - GUTTER - PAD_X
        for i, n in enumerate(nodes):
            # Even spacing per row. A label's width is estimated from its
            # length at 15px/600 — 8.6px per character against the shipped Plus
            # Jakarta Sans — and the box is padded either side, so a long name
            # widens its box rather than overflowing it. A node on the thread
            # gets 26px more, because the numbered badge is inside the box and
            # `Sparrowhawk` at the old width printed its label straight through
            # its own badge.
            w = max(96, int(8.6 * len(n["name"])) + 34
                    + (26 if n["id"] in tpos else 0))
            # ⚠️ CLAMPED, so a wide first node cannot reach back into the
            # gutter. Even spacing puts the leftmost box's centre at
            # GUTTER + span/2n, which is fine until the box is 26px wider for a
            # thread badge: `Caterpillars` then printed its left edge over the
            # row label "eats a producer". The label owns the gutter.
            cx = max(GUTTER + w / 2.0 + 6, GUTTER + span * (i + 0.5) / len(nodes))
            box[n["id"]] = {"cx": cx, "cy": y + NODE_H / 2.0, "w": w,
                            "h": NODE_H, "name": n["name"], "row": r}
            order.append(n["id"])

    # Height follows the legend's OWN row count. A fixed reserve was what let
    # two keys overlap without the box growing to notice.
    n_keys = 1 + (1 if thread else 0) + (1 if d.get("other") else 0)
    H = PAD_TOP + len(rows) * ROW_H + 22 + n_keys * 24

    out = [_svg_open(fig, W, H)]

    # One marker per link treatment. Both point at the eater; the open one is
    # for a link that is NOT a feeding link, so the head shape differs as well
    # as the dash.
    out.append(
        '<defs>'
        '<marker id="%s-eats" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" style="fill:%s"/></marker>'
        '<marker id="%s-eats-thread" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" style="fill:%s"/></marker>'
        '<marker id="%s-other" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0.5,0.5 L9.5,5 L0.5,9.5" style="fill:none;stroke:%s" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        '</marker></defs>'
        % (e(fig["id"]), _SVG_INK, e(fig["id"]), _SVG_ACCENT,
           e(fig["id"]), _SVG_INK_MUTED))

    # Row bands, then row labels. The band is a tint and the label is words:
    # the trophic level is never carried by the tint alone.
    # ⚠️ THE SAME `y`, and it has to be derived the same way. The row order
    # defect was fixed in the geometry loop above and NOT here, so the nodes
    # moved and the bands and their labels did not: the sparrowhawk sat on a
    # band captioned DECOMPOSERS and the oak on one captioned SECONDARY. Two
    # loops sharing one coordinate is the hazard; the fix is that both read
    # `r` directly, and a future third loop must too.
    for r, row in enumerate(rows):
        y = PAD_TOP + r * ROW_H
        tint = row.get("tint") or _SVG_INSET
        out.append('<rect x="0" y="%s" width="%d" height="%s" rx="14" '
                   'style="fill:%s"/>' % (y - 13, W, ROW_H - 16, tint))
        out.append(_svg_text(18, y + NODE_H / 2.0 - 3, row["label"], size=13,
                             fill=_SVG_INK_BODY, weight="700", anchor="start",
                             family=_SVG_MONO, spacing="0.06em"))
        if row.get("note"):
            out.append(_svg_text(18, y + NODE_H / 2.0 + 15, row["note"],
                                 size=13, fill=_SVG_INK_MUTED, weight="500",
                                 anchor="start", family=_SVG_MONO))

    # Links before nodes, so a line never draws over a name.
    def edge(a, b):
        """Route from the top or bottom edge of each box, not from its centre."""
        pa, pb = box[a], box[b]
        ay = pa["cy"] - pa["h"] / 2.0 if pb["cy"] < pa["cy"] else pa["cy"] + pa["h"] / 2.0
        by = pb["cy"] + pb["h"] / 2.0 if pb["cy"] < pa["cy"] else pb["cy"] - pb["h"] / 2.0
        return pa["cx"], ay, pb["cx"], by

    def _blocked(pts, skip):
        """The first node any of `pts` lands inside, ignoring the endpoints."""
        for nid, q in box.items():
            if nid in skip:
                continue
            for x, y in pts:
                if (abs(x - q["cx"]) <= q["w"] / 2.0 + 5
                        and abs(y - q["cy"]) <= q["h"] / 2.0 + 5):
                    return q
        return None

    def _samples(x1, y1, x2, y2, cx=None, cy=None):
        """Points along the link — a straight segment, or a quadratic if bowed."""
        out_pts = []
        for k in range(1, 48):
            t = k / 48.0
            if cx is None:
                out_pts.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
            else:
                u = 1.0 - t
                out_pts.append((u * u * x1 + 2 * u * t * cx + t * t * x2,
                                u * u * y1 + 2 * u * t * cy + t * t * y2))
        return out_pts

    def path(a, b, shift=0.0):
        """The link's `d`, bowed aside when a straight line would cross a node.

        ⚖️ THIS IS A SCIENCE PROBLEM WEARING A LAYOUT PROBLEM'S CLOTHES. A link
        drawn through a third organism's box does not look untidy — it reads as
        two different feeding relationships that the web does not contain. Two
        of them were in the first draft of this drawing: `sparrowhawk → fungi`
        ran straight down through the ladybirds, and `mice → sparrowhawk` clipped
        the ladybirds' right-hand end. Both appeared to say the sparrowhawk eats
        ladybirds. Neither is in Design's eight sentences.

        So the route is CHECKED rather than trusted. A straight segment is
        sampled against every other node's box; if it lands in one, the link is
        bowed away from that node and re-sampled; if both bows still cross
        something, this RAISES rather than drawing a line that lies. A build
        failure names the pair and can be fixed in the data; a quietly wrong
        arrow cannot be seen by any gate that is not a pair of eyes.
        """
        x1, y1, x2, y2 = edge(a, b)
        x1 += shift
        x2 += shift
        skip = {a, b}
        hit = _blocked(_samples(x1, y1, x2, y2), skip)
        if hit is None:
            return "M%.1f,%.1f L%.1f,%.1f" % (x1, y1, x2, y2)
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        # Bow AWAY from the node in the way, and if that side is also occupied,
        # try the other. Magnitudes are the two that clear a 42px-tall box at
        # this row pitch; a third guess would be a search, and a search that
        # can fail should fail loudly at the second try instead.
        for bow in (58.0, -58.0, 104.0, -104.0):
            away = bow if hit["cx"] <= mx else -bow
            cx, cy = mx + away, my
            if _blocked(_samples(x1, y1, x2, y2, cx, cy), skip) is None:
                return ("M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f"
                        % (x1, y1, cx, cy, x2, y2))
        raise ValueError(
            "food-web figure %r cannot route the link %s \u2192 %s without "
            "crossing %r, on either side. An arrow through a third organism's "
            "box reads as a feeding relationship the web does not claim, so "
            "this fails the build. Reorder that row's nodes, or split the "
            "figure." % (fig.get("id"), a, b, hit["name"]))

    for prey, eater in d.get("eats") or []:
        for nid in (prey, eater):
            if nid not in box:
                raise ValueError(
                    "food-web figure %r has a feeding link naming %r, which "
                    "is not a node in any row." % (fig.get("id"), nid))
        on = prey in tpos and eater in tpos and abs(tpos[prey] - tpos[eater]) == 1
        out.append('<path d="%s" style="fill:none;stroke:%s" stroke-width="%s" '
                   'stroke-linecap="round" marker-end="url(#%s-%s)"/>'
                   % (path(prey, eater), _SVG_ACCENT if on else _SVG_INK,
                      "3" if on else "2", e(fig["id"]),
                      "eats-thread" if on else "eats"))

    for a, b, label in d.get("other") or []:
        for nid in (a, b):
            if nid not in box:
                raise ValueError(
                    "food-web figure %r has a non-feeding link naming %r, "
                    "which is not a node in any row." % (fig.get("id"), nid))
        # ⚠️ SHIFTED 18px, because a non-feeding link between two organisms
        # that also feed each other lands on exactly the same geometry. The
        # wildflowers feed the bees and the bees pollinate the wildflowers, so
        # the solid arrow and the dashed one were drawn one on top of the other
        # and read as a single line — which erased the distinction the dash
        # exists to make. Parallel, not coincident.
        x1, y1, x2, y2 = edge(a, b)
        x1 += 18
        x2 += 18
        out.append('<path d="%s" style="fill:none;stroke:%s" stroke-width="2" '
                   'stroke-dasharray="7 5" stroke-linecap="round" '
                   'marker-end="url(#%s-other)"/>'
                   % (path(a, b, shift=18), _SVG_INK_MUTED, e(fig["id"])))
        # A backing plate under the word. `pollinates` printed across the
        # bottom edge of the bees' box and was unreadable against the outline;
        # a label with no ground of its own is at the mercy of whatever the
        # link happens to pass. Width from the same per-character estimate the
        # boxes use, at the mono 12px this text is set in.
        lx, ly = (x1 + x2) / 2.0 + 10, (y1 + y2) / 2.0 + 5
        out.append('<rect x="%.1f" y="%.1f" width="%d" height="18" rx="6" '
                   'style="fill:%s"/>'
                   % (lx - 5, ly - 13, int(7.4 * len(label)) + 10, _SVG_GROUND))
        out.append(_svg_text(lx, ly, label, size=13, fill=_SVG_INK_MUTED,
                             weight="600", anchor="start", family=_SVG_MONO))

    # Nodes, in the authored top-down order.
    for nid in order:
        p = box[nid]
        x, y = p["cx"] - p["w"] / 2.0, p["cy"] - p["h"] / 2.0
        on = nid in tpos
        out.append('<rect x="%.1f" y="%.1f" width="%s" height="%s" rx="13" '
                   'style="fill:%s;stroke:%s" stroke-width="%s"/>'
                   % (x, y, p["w"], p["h"],
                      _SVG_ACCENT_TINT if on else _SVG_CARD,
                      _SVG_ACCENT if on else _SVG_INK, "3" if on else "2"))
        # ⚠️ THE CLASS IS A GATE HOOK, not styling. `thread label is
        # accent-TEXT, never accent` selected `text[style*='accent-text']` at
        # first, and the mutation test showed why that is not an assertion:
        # repainting every thread label to ink left the LEGEND's accent-text
        # key matching the same selector, so the row still resolved and the
        # gate stayed green over a drawing that had lost the distinction it
        # measures. A named hook is the difference between a row that pins the
        # thread label and a row that pins "some orange text, somewhere".
        out.append(_svg_text(p["cx"] + (13 if on else 0), p["cy"] + 5, p["name"],
                             fill=_SVG_ACCENT_TEXT if on else _SVG_INK,
                             cls="ks3-web-thread-label" if on else None))
        if on:
            # The third channel. A number is not a colour, and it also carries
            # the ORDER of the chain, which the tint could not.
            out.append('<circle cx="%.1f" cy="%.1f" r="10" '
                       'style="fill:%s;stroke:%s" stroke-width="2"/>'
                       % (x + 15, p["cy"], _SVG_CARD, _SVG_ACCENT))
            out.append(_svg_text(x + 15, p["cy"] + 4, str(tpos[nid]), size=13,
                                 fill=_SVG_ACCENT_TEXT, weight="700",
                                 family=_SVG_MONO))

    # The legend states in words every distinction the drawing makes in ink —
    # which is the never-colour-alone rule discharged for the whole figure.
    #
    # ⚠️ ONE ROW PER ENTRY, and it is a fix rather than a preference. The first
    # version drew the thread key and the not-feeding key at the same `y`, so on
    # b9-01 — the only figure that has both — two sentences printed on top of
    # each other and neither was readable. Seen in a browser, not reasoned
    # about; the arithmetic looked fine.
    keys = [("eats", "2", None, _SVG_INK, _SVG_INK_BODY,
             d.get("legend_eats")
             or "points from the eaten to the eater — the way the energy goes")]
    if thread:
        keys.append(("eats-thread", "3", None, _SVG_ACCENT, _SVG_ACCENT_TEXT,
                     d.get("legend_thread")
                     or "one numbered chain, pulled out of the web"))
    if d.get("other"):
        keys.append(("other", "2", "7 5", _SVG_INK_MUTED, _SVG_INK_MUTED,
                     d.get("legend_other")
                     or "dashed: a link that is not feeding"))

    top = PAD_TOP + len(rows) * ROW_H
    out.append('<line x1="0" y1="%s" x2="%d" y2="%s" style="stroke:%s" '
               'stroke-width="2"/>' % (top, W, top, _SVG_RULE_STRONG))
    for i, (marker, wid, dash, ink, textink, label) in enumerate(keys):
        ly = top + 26 + i * 24
        out.append('<line x1="18" y1="%s" x2="52" y2="%s" style="stroke:%s" '
                   'stroke-width="%s"%s marker-end="url(#%s-%s)"/>'
                   % (ly, ly, ink, wid,
                      ' stroke-dasharray="%s"' % dash if dash else "",
                      e(fig["id"]), marker))
        out.append(_svg_text(62, ly + 4, label, size=13, fill=textink,
                             weight="600", anchor="start"))
    out.append('</svg>')
    return "".join(out)
# ── one turn of the predator–prey cycle, with the lag dimensioned (b9-02) ──


def _cycle_lag_run(m, years):
    """The bench's model, one step at a time, in Python.

    ⚠️ THIS IS `wireCycleRunner`'s RECURRENCE, TRANSCRIBED, and it must stay
    that way. Build contract §5A.1: any count or figure quoted in prose must
    match the instrument, and the instrument is the measurement. A figure that
    drew its own idealised sine waves beside a bench running a discrete
    logistic model would be a second source for the one number this lesson
    states six times — and the two would drift the first time anybody touched
    either. So the curve is the model's own output and the lag is counted off
    it, not authored.
    """
    prey, pred = float(m["start_prey"]), float(m["start_pred"])
    hist = [(prey, pred)]
    for _ in range(years):
        nxt_prey = (prey + m["r"] * prey * (1 - prey / m["k"])
                    - m["a"] * prey * pred)
        nxt_pred = pred + m["b"] * m["a"] * prey * pred - m["m"] * pred
        prey = max(0.0, min(m["k"] * m["prey_cap_mult"], nxt_prey))
        pred = max(0.0, min(m["k"], nxt_pred))
        if pred < m["pred_floor"]:
            pred = 0.0
        hist.append((prey, pred))
    return hist
def _cycle_lag_peaks(hist, idx, lo, hi):
    """Every interior local maximum of one series inside [lo, hi]."""
    return [y for y in range(max(lo, 1), min(hi, len(hist) - 2) + 1)
            if hist[y][idx] > hist[y - 1][idx] and hist[y][idx] > hist[y + 1][idx]]
def _cycle_lag(fig):
    """Two populations over one turn of the cycle, and the gap between the
    peaks measured on the drawing.

    ⚖️ WHY THIS LESSON GETS A DIAGRAM (WS1 audit #12). This is the one page
    where the bench ATTEMPTS the sequential idea and measurably fails at the
    width most of these students are on. At 390px the chart is 274px holding
    fifty-two bars at two pixels each, with no year axis and no year labels at
    all, and the two series scaled separately. The lesson's own instruction is
    *"Look at when each peak happens — not how high, when"*, and at that width
    there is nothing on screen a student could answer it from: a two-pixel bar
    has no when. The instrument is not replaced — it is where a student changes
    the field and watches it respond, which no drawing can do — but the claim
    it exists to demonstrate needs one picture that holds still and carries an
    axis.

    ⚖️ ONE TURN, NOT THE WHOLE RUN. The bench draws twenty-six years, which is
    one and a half cycles of a DAMPED model, so the second prey peak is lower
    than the first. Drawn as a figure that reads as "and then it dies away",
    which is true of the model and is not this lesson's claim — the damping is
    `#s-think`'s second belief and rung 4's business. So the window is one
    complete period, and the caption says it is one turn.

    ⚖️ THE LAG IS COUNTED, NEVER AUTHORED. `_cycle_lag_peaks` finds both peaks
    in the drawn window and the dimension label prints the difference. The
    lesson states "about five years" in seven places; if the model's parameters
    were ever touched, this figure would print the new number and disagree with
    those seven sentences loudly, instead of agreeing with them silently while
    drawing something else. That is the §5A.1 rule — the instrument is the
    measurement — turned into a property of the drawing.

    ⛔ NO CATEGORY HUE, AND THE BENCH'S AMBER AND GREEN DO NOT COME WITH IT.
    The chart beside this figure keys rabbits to `--ks3-alert` and foxes to
    `--ks3-ok`, which is the usage MRB-252 ruled against and which the
    biology figure set carries none of. Here the two series are told apart by
    STROKE (solid against dashed), by a filled peak marker against an open one,
    and by a direct label on each curve — three channels, none of them colour,
    and the direct labels mean nothing has to be carried back to a key.

    ⚠️ TWO SCALES, SAID OUT LOUD. The bench scales the two series
    independently and its caption says so, because on one scale the fox line
    flattens into the axis and the lag becomes unreadable. This figure does the
    same and therefore inherits the same obligation: two axes, each labelled
    with its own numbers, and a line on the face of the drawing telling the
    reader to compare WHEN and not HOW HIGH. Without that a reader compares two
    heights that were never comparable.

    ⚠️ THE YEARLY SAMPLES ARE DRAWN AS DOTS. The model is discrete — one step
    is one year — and a smooth curve through it would quietly claim a
    continuous population that was measured between the years. The dots are
    where the numbers actually are; the curve is the eye's line through them.
    """
    d = fig.get("data") or {}
    m = d.get("model")
    if not m:
        raise ValueError(
            "cycle-lag figure %r carries no `model`. The curve IS the bench's "
            "model — a figure that drew its own would be a second source for "
            "the one number this lesson states seven times."
            % fig.get("id"))

    span = int(d.get("span") or 60)
    hist = _cycle_lag_run(m, span)

    # The drawn window: one full period, taken from the SECOND turn, because
    # the first is still leaving the starting values behind and its shape is
    # the model settling rather than the cycle.
    prey_pk = _cycle_lag_peaks(hist, 0, 1, span - 2)
    pred_pk = _cycle_lag_peaks(hist, 1, 1, span - 2)
    if len(prey_pk) < 2 or len(pred_pk) < 2:
        raise ValueError(
            "cycle-lag figure %r finds %d prey peak(s) and %d predator peak(s) "
            "in %d years. The figure is one turn of a cycle and needs two of "
            "each to know where a turn begins and ends."
            % (fig.get("id"), len(prey_pk), len(pred_pk), span))
    y_prey, y_pred = prey_pk[1], pred_pk[1]
    if y_pred <= y_prey:
        raise ValueError(
            "cycle-lag figure %r puts the predator peak at year %d and the "
            "prey peak at year %d. The predator peak FOLLOWS the prey peak — "
            "that is the lesson, stated seven times on this page — and a "
            "figure that drew it the other way round would teach the "
            "misconception the page exists to break."
            % (fig.get("id"), y_pred, y_prey))
    lag = y_pred - y_prey

    period = prey_pk[1] - prey_pk[0]
    y0 = y_prey - int(round(period * 0.42))
    y1 = y0 + period
    y0 = max(0, y0)
    y1 = min(span, y1)

    W, H = 900, 626
    PX0, PX1, PY0, PY1 = 104.0, 812.0, 96.0, 430.0
    out = [_svg_open(fig, W, H)]

    prey_max = float(d.get("prey_axis") or 1000)
    pred_max = float(d.get("pred_axis") or 400)
    prey_name = d.get("prey_name") or "Rabbits"
    pred_name = d.get("pred_name") or "Foxes"

    def x_of(year):
        return PX0 + (PX1 - PX0) * (year - y0) / float(y1 - y0)

    def y_of(v, top):
        return PY1 - (PY1 - PY0) * (v / top)

    out.append(_mono(24, 40, "ONE TURN OF THE CYCLE, FROM THE FIELD ON THIS "
                             "PAGE", size=14, fill=_SVG_INK_MUTED,
                     spacing="1.4"))

    # ── the frame: two axes, because there are two scales ──
    out.append(_line(PX0, PY0 - 10, PX0, PY1, stroke=_SVG_INK, w=2.5))
    out.append(_line(PX1, PY0 - 10, PX1, PY1, stroke=_SVG_INK, w=2.5))
    out.append(_line(PX0, PY1, PX1, PY1, stroke=_SVG_INK, w=2.5))

    for v in range(0, int(prey_max) + 1, int(prey_max // 4)):
        yy = y_of(v, prey_max)
        out.append(_line(PX0 - 7, yy, PX0, yy, stroke=_SVG_INK, w=2))
        if v:
            out.append(_line(PX0, yy, PX1, yy, stroke=_SVG_RULE, w=1.4,
                             dash="3 6"))
        out.append(_mono(PX0 - 12, yy + 5, str(v), size=13, anchor="end",
                         fill=_SVG_INK_MUTED))
    for v in range(0, int(pred_max) + 1, int(pred_max // 4)):
        yy = y_of(v, pred_max)
        out.append(_line(PX1, yy, PX1 + 7, yy, stroke=_SVG_INK, w=2))
        out.append(_mono(PX1 + 12, yy + 5, str(v), size=13, fill=_SVG_INK_MUTED))

    # ⚠️ INSIDE THE AXES, NOT OUTSIDE THEM. These sat at `PX0 - 12` anchored
    # end and `PX1 + 12` anchored start, which put "Rabbits counted" starting
    # at x = -8 and "Foxes counted" ending past x = 900. SVG does not warn when
    # text leaves the viewBox; it simply draws outside it and is clipped, so
    # the figure rendered with "bits counted" on the left and "Foxes cou" on
    # the right — each axis labelled with a fragment, on a figure whose one
    # instruction is that the two scales are separate.
    out.append(_mono(PX0, PY0 - 24, "%s counted" % prey_name, size=13,
                     fill=_SVG_INK_BODY))
    out.append(_mono(PX1, PY0 - 24, "%s counted" % pred_name, size=13,
                     anchor="end", fill=_SVG_INK_BODY))

    # ── the year axis, which the bench's chart has none of ──
    for year in range(y0, y1 + 1):
        xx = x_of(year)
        major = (year - y0) % 2 == 0
        out.append(_line(xx, PY1, xx, PY1 + (9 if major else 5),
                         stroke=_SVG_INK, w=2 if major else 1.5))
        if major:
            out.append(_mono(xx, PY1 + 30, str(year), size=13,
                             anchor="middle", fill=_SVG_INK_MUTED))
    out.append(_mono(PX0, PY1 + 56, "year", size=13, fill=_SVG_INK_BODY))

    # ── the two series ──
    #
    # ⚠️ THE DIRECT LABELS GO WHERE THE CURVES ARE FURTHEST APART, DERIVED.
    # They were first placed at the right-hand end of each curve, which is
    # where a line chart usually labels itself — and on this chart the two
    # lines converge as the oscillation damps, so at the last year they were
    # 14px apart and the words "Rabbits" and "Foxes" printed on top of each
    # other. Both series then had no usable label, on a figure that carries no
    # colour and relies on the direct label as one of its three channels.
    #
    # So the anchor is the year at which the drawn vertical gap between the two
    # curves is greatest. That is a property of whatever the model does, not of
    # this particular set of parameters, so it cannot come back if the numbers
    # move.
    gap_best, gap_year = -1.0, y0
    for year in range(y0, y1 + 1):
        g = abs(y_of(hist[year][0], prey_max) - y_of(hist[year][1], pred_max))
        if g > gap_best:
            gap_best, gap_year = g, year
    prey_above = (y_of(hist[gap_year][0], prey_max)
                  < y_of(hist[gap_year][1], pred_max))

    for key, idx, top, name, dash, wt in (
            ("prey", 0, prey_max, prey_name, None, 3.6),
            ("pred", 1, pred_max, pred_name, "9 6", 3.0)):
        pts = [(x_of(y), y_of(hist[y][idx], top)) for y in range(y0, y1 + 1)]
        out.append(_path(
            "".join("%s%.1f,%.1f" % ("M " if i == 0 else " L ", p[0], p[1])
                    for i, p in enumerate(pts)),
            stroke=_SVG_INK if key == "prey" else _SVG_INK_BODY,
            w=wt, dash=dash, data_series=key))
        # The samples. One dot is one year, which is one step of the model.
        for i, y in enumerate(range(y0, y1 + 1)):
            out.append(_circle(pts[i][0], pts[i][1], 3.4,
                               fill=_SVG_INK if key == "prey" else _SVG_GROUND,
                               stroke=_SVG_INK_BODY, w=1.6,
                               data_series=key, data_year=y,
                               data_count=int(round(hist[y][idx]))))
        # Direct label on the curve, so neither series has to be carried back
        # to a key to be identified.
        lx = x_of(gap_year)
        ly_ = y_of(hist[gap_year][idx], top)
        up = prey_above if key == "prey" else not prey_above
        out.append(_label(lx, ly_ - 16 if up else ly_ + 28, name,
                          size=16, weight="800", fill=_SVG_INK,
                          data_series_label=key))

    # ── the two peaks, and the gap between them ──
    marks = ((y_prey, 0, prey_max, True, "%s peak" % prey_name),
             (y_pred, 1, pred_max, False, "%s peak" % pred_name))
    for year, idx, top, filled, name in marks:
        xx, yy = x_of(year), y_of(hist[year][idx], top)
        out.append(_line(xx, yy + 8, xx, PY1, stroke=_SVG_ACCENT, w=2,
                         dash="5 5"))
        out.append(_circle(xx, yy, 8.5,
                           fill=_SVG_INK if filled else _SVG_GROUND,
                           stroke=_SVG_INK, w=2.6,
                           data_peak=("prey" if idx == 0 else "pred"),
                           data_peak_year=year))
        out.append(_label(xx, yy - 20, name, size=14, weight="800",
                          fill=_SVG_ACCENT_TEXT))
        out.append(_mono(xx, yy - 38, "year %d" % year, size=13,
                         anchor="middle", fill=_SVG_ACCENT_TEXT))

    dy = PY1 + 78
    xa, xb = x_of(y_prey), x_of(y_pred)
    # ⊕ MRB-254 · THEY START BELOW THE YEAR, NOT AT THE AXIS. These two ran
    # from `PY1 + 12` and the year-axis numerals sit at `PY1 + 30` — so the
    # extension line for the fox peak came down through the numeral naming the
    # year it was extending from, and "25" is the number the whole dimension
    # exists to subtract. `PY1 + 44` starts them ten units under the numeral's
    # descender. Nothing is lost by the shortening: each peak already has a
    # dashed drop-line from its own marker to the axis, so the eye is carried
    # down to the year before these ever begin.
    for xx in (xa, xb):
        out.append(_line(xx, PY1 + 44, xx, dy + 9, stroke=_SVG_ACCENT, w=1.6,
                         dash="4 4"))
    out.append(_line(xa, dy, xb, dy, stroke=_SVG_ACCENT, w=2.6,
                     data_lag_dimension=lag))
    for xx in (xa, xb):
        out.append(_line(xx, dy - 8, xx, dy + 8, stroke=_SVG_ACCENT, w=2.6))
    out.append(_rect((xa + xb) / 2 - 62, dy - 17, 124, 34, rx=12,
                     fill=_SVG_GROUND, stroke="none"))
    out.append(_label((xa + xb) / 2, dy + 6,
                      "%d years" % lag, size=21, weight="800",
                      fill=_SVG_ACCENT_TEXT, data_lag=lag))

    ky = dy + 52
    out.append(_line(24, ky - 22, W - 24, ky - 22, stroke=_SVG_RULE_STRONG,
                     w=2))
    out.append(_line(30, ky + 2, 76, ky + 2, stroke=_SVG_INK, w=3.6))
    out.append(_circle(53, ky + 2, 3.4, fill=_SVG_INK, stroke=_SVG_INK_BODY,
                       w=1.6))
    out.append(_label(88, ky + 7, "%s — solid, filled peak" % prey_name,
                      size=13, weight="600", anchor="start",
                      fill=_SVG_INK_BODY))
    out.append(_line(330, ky + 2, 376, ky + 2, stroke=_SVG_INK_BODY, w=3.0,
                     dash="9 6"))
    out.append(_circle(353, ky + 2, 3.4, fill=_SVG_GROUND,
                       stroke=_SVG_INK_BODY, w=1.6))
    out.append(_label(388, ky + 7, "%s — dashed, open peak" % pred_name,
                      size=13, weight="600", anchor="start",
                      fill=_SVG_INK_BODY))
    out.append(_label(24, ky + 38,
                      "The two are counted on their own scales. Look at WHEN "
                      "each peak happens — not how high, when.",
                      size=15, weight="600", anchor="start",
                      fill=_SVG_INK))
    out.append('</svg>')
    return "".join(out)
# renderers: ═══ END B8 ═══


# renderers: ═══ BEGIN B9 ═══
#
# ── B9 · Ecosystems and interdependence (⊕ MRB-250) ──
#
# Six instruments, one per lesson — the largest single-unit instrument count in
# the biology build. All six are DOM-only: `canvas`, `requestAnimationFrame`,
# `setTimeout` and `setInterval` appear ZERO times across all six of Design's
# delivered pages, and `shared/ks3.js` keeps it that way. So this unit creates
# no reduced-motion obligation (MRB-220 R4) and adds no timer for a gate to
# have to chase.
#
# ⚠️ ALL SIX SHIP ON `ks3-block ks3-dark ks3-practical`, measured off Design's
# own `#s-bench` markup on all six pages character for character (b9-01 L105,
# b9-02 L105, b9-03 L104, b9-04 L105, b9-05 L105, b9-06 L104). `.ks3-dark p` is
# (0,1,1) and a bare component class is (0,1,0), so every colour rule in the B9
# stylesheet is written under `.ks3-dark …` at (0,2,0) and every one of them is
# resolved by `ks3_parity.check_dark_text_specificity()` on the real cascade.
#
# ⚠️ AND NONE OF THE SIX MARKS ANYTHING (MRB-196 R10). A chosen tab shows that
# it was CHOSEN — the alert ground Design's own `seg()` paints — and takes no
# verdict class, no green, no red, ever. What these benches show is a
# CONSEQUENCE: what arrives at the top of a chain, what a field does over
# twenty-six years, what a removal reaches, what is left on a shelf, what a
# chemical does on the way up, and how wrong an estimate was. Only the mastery
# ladder marks correctness. Amber is a wrong IDEA being confronted.
#
# ⚠️ THE STAGE PREDICATE IS MONOTONIC ON ALL SIX and on three of them that is a
# DEPARTURE FROM DESIGN, made under MRB-208 rather than against it. Design's
# `isDone()` for b9-01, b9-03 and b9-05 reads a sticky `everTopped`/`everDone`,
# but b9-04's reads `s.level !== 'all'` and b9-06's reads `s.truthShown` — both
# of which a student can turn back OFF by tidying up after themselves (bringing
# the pollinators back, re-sampling the field). MRB-208 ruled the rail records
# PARTICIPATION, and B5's compare rows and B7's tuner already resolved the same
# clash the same way. What ticks is unchanged; what unticks is nothing.
#
# ⚖️ AND B9 OWNS THE TROPHIC 10:1 FOR THE WHOLE KEY STAGE (schema §0.7). b9-01
# states it, computes with it and legals it; b9-05 runs the same arithmetic in
# the opposite direction. `r_chain_ledger` refuses any other factor rather than
# letting a later edit re-teach the ratio by accident.


def _b9_num(x):
    """A number printed the way JavaScript's `String(n)` prints it.

    ⚠️ THE STATIC RENDER AND THE RUNTIME MUST AGREE AT EVERY PRINTED VALUE, and
    the two are written in different languages. Design's pages compose their
    figures with plain JS concatenation — `(100 / Math.pow(10, i)) + '% of the
    original'` — which prints `0.1` and `0.01` with no trailing noise. Python's
    `str(float)` agrees on those; what it does not agree on is the integers,
    where it says `100.0` and JavaScript says `100`. So the integer case is
    handled explicitly and everything else falls through to `repr`, which is
    Python's shortest round-tripping form and is the same algorithm V8 uses.
    """
    x = float(x)
    if x == int(x) and abs(x) < 1e16:
        return str(int(x))
    return repr(x)
def _b9_strip2(x):
    """`x.toFixed(2).replace(/\\.?0+$/, '')` — Design's own percentage rule.

    ⚠️ `0.10 → 0.1` AND `0.01` SURVIVES UNTOUCHED, and the difference between
    those two is the difference between a four-level chain and a five-level
    one. Reproduced rather than tidied: the verdict line quotes this number as
    the fraction of the original energy that arrived, and it is the number the
    lesson's whole argument rests on.
    """
    return re.sub(r"\.?0+$", "", "%.2f" % float(x)) or "0"
def _b9_progress(pg, act_id, kind, keys):
    """The block-head readout, validated where the instrument derives it.

    ⊕ MRB-250. Five of the six B9 benches put a live count in Design's head-row
    paragraph — "level 3 of 4", "year 26", "round 2 of 3", "8 quadrats counted"
    — and `_KIND_HEAD_FROM` converts the authored `progress` into the head
    counter that draws it. Reading the key here is what puts the kind into
    `_KIND_FN_OWNS_PROGRESS`, which is what stops the shell ALSO printing the
    raw map through `_progress_readout` and shipping `level {n} of {total}`
    with the placeholders still in it.

    So this is a read site in the strict R5 sense and not a formality: without
    it the page ships a brace on screen, which is exactly what B7's own drive
    fails a build for.
    """
    if not isinstance(pg, dict) or not pg:
        raise ValueError(
            "%s %r declares no `progress`. Design draws a live readout in this "
            "block's head row on all six B9 pages, right-aligned and mono, and "
            "without it the row is the eyebrow and the heading with a hole in "
            "it." % (kind or "?", act_id))
    for k in keys:
        if not pg.get(k):
            raise ValueError(
                "%s %r progress declares no %r. Every state the instrument can "
                "reach needs a sentence, or the readout goes blank while the "
                "student is holding the control." % (kind or "?", act_id, k))
    return pg
def _b9_head(a, kind, keys, build):
    """The block-head readout, validated and then converted, in that order.

    ⊕ MRB-250. `r_activity` emits the head row BEFORE it dispatches to the
    instrument, so a `progress` map that is missing a state is met by
    `_progress_readout`'s generic complaint about a `data-state-…` name rather
    than by the renderer's own message about what the readout is FOR. Found by
    mutation: dropping `progress` from a chain-ledger reported "progress state
    'format' has no label", which is true, unactionable, and about a key the
    author never wrote.

    So the derivation validates first and builds second, and there is exactly
    one message per mistake, raised at the first point that can see it.
    """
    pg = _b9_progress(a.get("progress"), a.get("id") or "?", kind, keys)
    return build(pg)
# ── b9-01 `#s-bench` · chain-ledger ──────────────────────────────────────

def r_chain_ledger(a, act_id):
    """⊕ b9-01 `#s-bench` — ten thousand kilojoules, and what is left at the top.

    ⚖️ THE PRODUCER IS DRAWN AT THE BOTTOM, and that is not styling. The level
    list is `flex-direction: column-reverse`, so a student reads the chain the
    way the energy travels: in at the bottom, up one step at a time, a tenth
    of it surviving each step. Flipping the list to ordinary document order
    would draw the same numbers making the opposite claim, and the arrows in
    `#s-think` — the unit's most-marked misconception — are about exactly this
    direction. The rule is in the stylesheet and there is a parity row on it.

    ⚖️ THE VERDICT LINE IS COMPUTED, NEVER AUTHORED PER CHAIN. Three fragments
    — `lead`, `mid`, `tail` — with the two figures derived from the chain's own
    length, which is why a fourth chain needs no new prose and cannot disagree
    with the bench beside it. Four-level chains land on "10 arrived here —
    0.1% of it"; the five-level sea chain lands on "1 … 0.01%". Both come out
    of one expression.

    ⚖️ THE FACTOR IS TEN AND THE RENDERER REFUSES ANYTHING ELSE. Schema §0.7:
    B9 owns the trophic 10:1 for the whole key stage — b9-01 states it, the
    bench computes with it, the legal line qualifies it as a teaching average,
    and b9-05 runs the same arithmetic in the other direction. A later edit
    that "tuned" this to 8 or 12 would silently re-teach the ratio in every
    lesson that cites b9-01, and nothing else in the build would notice.

    ⚠️ EVERY CHAIN'S PANEL IS IN THE DOCUMENT and only one is shown, so a
    reader with JS off gets a whole chain rather than an empty shell. Design
    resets `shown` to 1 on every tab press, so the panels do NOT each keep
    their own progress — one count is held by the runtime and the panels are
    redrawn from it, which is what makes switching chains restart the climb.
    """
    # ⚠️ `start_kj` AND `factor` ARE NOT IN THIS LIST. `_b7_need` tests
    # truthiness, so a numeric key whose wrong value is ZERO is reported as
    # ABSENT and the explicit check below — the one with the teaching message —
    # never runs. Found by mutation: `harm: 0` on b9-05 said "declares no
    # `harm`", which is false and sends the author looking for a missing line.
    _b7_need(a, act_id, ("tabs_label", "chains", "step_label",
                         "step_spent_label", "reset_label", "verdict"))
    for f in ("start_kj", "factor"):
        if a.get(f) is None:
            raise ValueError("chain-ledger %r declares no %r." % (act_id, f))
    _b9_progress(a.get("progress"), act_id, "chain-ledger",
                 ("before", "after"))

    factor = float(a["factor"])
    if abs(factor - 10.0) > 1e-9:
        raise ValueError(
            "chain-ledger %r sets factor %r. B9 OWNS THE TROPHIC 10:1 for the "
            "whole key stage (schema §0.7): this bench states the ratio, "
            "computes with it, and b9-05 runs the same arithmetic in the "
            "opposite direction. Changing it here re-teaches the figure in "
            "every later lesson that cites b9-01, and the page's own legal "
            "line — a tenth, a teaching average — would then be describing a "
            "bench that says something else." % (act_id, a["factor"]))
    start_kj = float(a["start_kj"])
    if start_kj <= 0:
        raise ValueError(
            "chain-ledger %r starts at %r kJ. The producers are where energy "
            "ENTERS the living world; a chain that starts at nothing prints a "
            "ladder of zeroes." % (act_id, a["start_kj"]))

    verdict = a["verdict"]
    for f in ("lead", "mid", "tail"):
        if not verdict.get(f):
            raise ValueError(
                "chain-ledger %r verdict declares no %r. The line is three "
                "authored fragments with two computed figures between them; a "
                "missing fragment is a sentence that reads '10 0.1%%'."
                % (act_id, f))

    chains = a["chains"]
    if len(chains) < 2:
        raise ValueError(
            "chain-ledger %r declares %d chain(s). The bench's argument is "
            "that chains of DIFFERENT lengths stop for the same reason, which "
            "needs more than one." % (act_id, len(chains)))

    seen, tabs, panels = set(), [], []
    for i, c in enumerate(chains):
        for f in ("id", "label", "levels"):
            if not c.get(f):
                raise ValueError("chain-ledger %r chain %r declares no %r."
                                 % (act_id, c.get("id"), f))
        if c["id"] in seen:
            raise ValueError("chain-ledger %r declares chain id %r twice."
                             % (act_id, c["id"]))
        seen.add(c["id"])
        levels = c["levels"]
        if len(levels) < 3:
            raise ValueError(
                "chain-ledger %r chain %r has %d level(s). A chain that "
                "reaches its top predator in two steps is a caption, not a "
                "climb." % (act_id, c["id"], len(levels)))
        top = start_kj / (factor ** (len(levels) - 1))
        if top < 1.0:
            raise ValueError(
                "chain-ledger %r chain %r runs %d levels and arrives at %s kJ. "
                "Design's own formatting has no branch below one kilojoule, "
                "and the lesson's point is that a chain STOPS before it gets "
                "there — a level that prints a fraction of a kilojoule is the "
                "bench contradicting the sentence under it."
                % (act_id, c["id"], len(levels), _b9_num(top)))
        for L in levels:
            for f in ("name", "role", "note"):
                if not L.get(f):
                    raise ValueError(
                        "chain-ledger %r chain %r has a level missing %r. The "
                        "`role` is the job title `#s-roles` names and the "
                        "`note` is what arrives on a press — a level that "
                        "unhides nothing is a press that does nothing."
                        % (act_id, c["id"], f))

        first = i == 0
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-cl-tab" '
            'data-cl-chain="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(c["id"]), "true" if first else "false", t(c["label"])))

        rows = []
        for j, L in enumerate(levels):
            kj = start_kj / (factor ** j)
            pct = 100.0 / (factor ** j)
            rows.append(
                '<li class="ks3-cl-level" data-i="%d"%s%s>'
                '<div class="ks3-cl-levelhead">'
                '<p class="ks3-cl-levelname">%s</p>'
                '<p class="ks3-cl-levelrole">%s</p></div>'
                '<div class="ks3-cl-readout" data-cl-readout%s>'
                '<div class="ks3-cl-figs">'
                '<p class="ks3-cl-energy" data-cl-energy>%s</p>'
                '<p class="ks3-cl-pct" data-cl-pct>%s</p></div>'
                '<span class="ks3-cl-track">'
                '<span class="ks3-cl-bar" data-cl-bar style="width:%s%%">'
                '</span></span>'
                '<p class="ks3-cl-note">%s</p></div></li>'
                % (j, ' data-shown=""' if j == 0 else "",
                   ' data-top=""' if j == 0 else "",
                   t(L["name"]), t(L["role"]), "" if j == 0 else " hidden",
                   t(_b9_energy(kj, a)), t(_b9_pct(pct, a)),
                   e(_pctnum(max(0.6, pct))), t(L["note"])))

        panels.append(
            '<ol class="ks3-cl-levels" role="list" data-cl-chainpanel="%s" '
            'data-total="%d"%s>%s</ol>'
            % (e(c["id"]), len(levels), "" if first else " hidden",
               "".join(rows)))

    return ('<div class="ks3-cl" data-cl data-start-kj="%s" data-factor="%s" '
            'data-energy-unit="%s" data-pct-suffix="%s" data-step-label="%s" '
            'data-step-spent-label="%s" data-verdict-lead="%s" '
            'data-verdict-mid="%s" data-verdict-tail="%s">'
            '<div class="ks3-cl-tabsgroup">'
            '<p class="ks3-cl-tabslabel" id="%s-chains">%s</p>'
            '<ul class="ks3-options ks3-cl-tabs" role="list" '
            'aria-labelledby="%s-chains">%s</ul></div>'
            '<div class="ks3-cl-panel">%s'
            '<div class="ks3-cl-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-cl-up" '
            'data-cl-up>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-cl-reset" '
            'data-cl-reset>%s</button></div>'
            '<p class="ks3-cl-verdict" data-cl-verdict hidden>%s</p>'
            '</div></div>'
            % (e(_pctnum(start_kj)), e(_pctnum(factor)),
               e(_b8_plain(a.get("energy_unit") or " kJ", act_id,
                           "`energy_unit`")),
               e(_b8_plain(a.get("pct_suffix") or "% of the original", act_id,
                           "`pct_suffix`")),
               e(_b8_plain(a["step_label"], act_id, "`step_label`")),
               e(_b8_plain(a["step_spent_label"], act_id,
                           "`step_spent_label`")),
               e(_b8_plain(verdict["lead"], act_id, "verdict `lead`")),
               e(_b8_plain(verdict["mid"], act_id, "verdict `mid`")),
               e(_b8_plain(verdict["tail"], act_id, "verdict `tail`")),
               e(act_id), t(a["tabs_label"]), e(act_id), "".join(tabs),
               "".join(panels), t(a["step_label"]), t(a["reset_label"]),
               t(_b9_chain_verdict(a, chains[0], factor, start_kj))))
def _b9_energy(kj, a):
    """`10,000 kJ` — grouped by hand, never by `toLocaleString()`.

    ⚠️ `toLocaleString()` IS THE BROWSER'S LOCALE AND NOT OURS. A student whose
    machine is set to a European locale reads `10.000 kJ` for ten thousand —
    ten, printed as if it were ten. Design writes the locale call; the port
    groups explicitly at both ends so the page cannot say a different number in
    a different country.
    """
    unit = a.get("energy_unit") or " kJ"
    if kj >= 1 and float(kj) == int(kj):
        return _b8_group(int(kj), True) + unit
    return _b9_num(kj) + unit
def _b9_pct(pct, a):
    return _b9_num(pct) + (a.get("pct_suffix") or "% of the original")
def _b9_chain_verdict(a, chain, factor, start_kj):
    """The computed line, built once here and once in `wireChainLedger`."""
    n = len(chain["levels"])
    top = start_kj / (factor ** (n - 1))
    v = a["verdict"]
    return ("%s%s%s%s%s"
            % (v["lead"],
               _b8_group(int(top), True) if (top >= 1 and top == int(top))
               else _b9_num(top),
               v["mid"], _b9_strip2(100.0 / (factor ** (n - 1))), v["tail"]))
# ── b9-02 `#s-bench` · cycle-runner ──────────────────────────────────────

# ⚖️ THE SIX NOTE BRANCHES, IN DESIGN'S EVALUATION ORDER. First match wins, and
# the ORDER IS THE MEANING: `no_pred_at_ceiling` must be tested before
# `no_pred` or the ceiling note never fires and *Remove every fox* stops
# teaching carrying capacity. The predicates are implemented once, in
# `wireCycleRunner`, keyed by these ids — which is why the id set is closed and
# ordered rather than free.
#
# ⊖ Design's `notes` carry a `when` string in the schema. It is NOT authored
# here: a predicate expressed as a string needs an evaluator, we are not
# shipping one, and a key whose only reader is a comment is precisely the dead
# key R5 forbids. The `id` IS the predicate's name and the runtime branches on
# it. Reported as a schema deviation.
# ⊕ MRB-257 (5.11) / MRB-255 S5 — `settled` IS THE SEVENTH, and it sits
# fourth because that is where `noteId()` tests it: after the two no-fox
# branches (which are about a field the student emptied) and before the three
# that describe a swing (which are false once there is no swing left). The
# shipped parameters are a DAMPED oscillator with a stable equilibrium — 667
# rabbits / 267 foxes by year 260 — and four presses of "Ten years" reaches a
# spread of 99.9–100.0%. MRB-255 rules that the MATHS STAYS: a neutral model
# would cycle forever at its starting amplitude, which looks like perpetual
# motion, is structurally unstable, and loses the carrying capacity `#s-think`
# and rung 4 both depend on. So the arrival needs a note of its own rather
# than `steady` describing a cycle that has stopped.
_B9_CYCLE_NOTES = ("year_zero", "no_pred_at_ceiling", "no_pred", "settled",
                   "prey_high_pred_low", "prey_low", "steady")
_B9_CYCLE_MODEL = ("r", "k", "a", "b", "m", "start_prey", "start_pred",
                   "history", "prey_cap_mult", "pred_floor")
def r_cycle_runner(a, act_id):
    """⊕ b9-02 `#s-bench` — two rules, twenty-six years, and a lag.

    ⚖️ K IS THE GRASS SUPPLY AND IT IS NOT A TUNING CONSTANT. It is the only
    reason *Remove every fox* teaches a carrying-capacity result — the rabbits
    climb, then stop, crowded and hungry — instead of drawing the exponential
    curve that would teach the misconception `#s-think` exists to break. Design
    says so in a comment on her own page. A revision that drops it, raises it
    out of reach, or replaces the logistic term with plain growth deletes the
    lesson, so the renderer refuses a model whose prey cannot reach the
    ceiling and refuses one that starts at or above it.

    ⚖️ THE TWO SERIES ARE SCALED INDEPENDENTLY and the caption says so in
    words. On one scale the fox line flattens into the axis and the LAG — which
    is the entire lesson, and the thing rung 1 and rung 2 both test — becomes
    unreadable. `wireCycleRunner` computes `maxPrey` and `maxPred` separately,
    each with its own floor, exactly as Design does. Do not "fix" it.

    ⚠️ *REMOVE EVERY FOX* IS NOT A RESET. It toggles the predator count between
    zero and its starting value, pushes ONE history point and advances the year
    by one — so the chart records the intervention as a year like any other and
    the student can see the rabbits respond to it over the years that follow.

    ⚑ `culled` is dead in DESIGN'S OWN CODE: `onCull` sets it, `onReset`
    clears it, and `renderVals()` never reads it. Not carried across.
    """
    _b7_need(a, act_id, ("model", "series", "chart_caption", "year_label",
                         "ten_label", "cull_label", "restore_label",
                         "reset_label", "notes"))
    _b9_progress(a.get("progress"), act_id, "cycle-runner", ("prefix",))

    model = a["model"]
    for f in _B9_CYCLE_MODEL:
        if model.get(f) is None:
            raise ValueError(
                "cycle-runner %r model declares no %r. Every one of the ten is "
                "in the recurrence or in a clamp on it, and a missing one "
                "makes the whole field NaN on the first press."
                % (act_id, f))
    k = float(model["k"])
    if k <= 0:
        raise ValueError(
            "cycle-runner %r sets K = %r. K IS THE GRASS SUPPLY. Without a "
            "positive carrying capacity the logistic term is gone and "
            "'Remove every fox' draws an exponential curve — which is the "
            "misconception `#s-think` exists to break, taught by the bench "
            "that is supposed to break it." % (act_id, model["k"]))
    if float(model["start_prey"]) >= k:
        raise ValueError(
            "cycle-runner %r starts the prey at %r against a ceiling of %r. "
            "The field opens with room to grow into, or the first ten years "
            "show a population that only ever falls."
            % (act_id, model["start_prey"], model["k"]))
    if float(model["start_pred"]) <= 0:
        raise ValueError(
            "cycle-runner %r starts with %r predators. With none there is no "
            "cycle to run and the bench opens on the cull's answer."
            % (act_id, model["start_pred"]))
    if int(model["history"]) < 10:
        raise ValueError(
            "cycle-runner %r keeps %r years of history. The cycle's period is "
            "several years and the lag is read ACROSS the chart, so a window "
            "shorter than one full turn cannot show it."
            % (act_id, model["history"]))
    if float(model["prey_cap_mult"]) < 1:
        raise ValueError(
            "cycle-runner %r caps the prey below K itself (×%r). The ceiling "
            "clamp exists to stop a discrete model overshooting, not to hold "
            "the population under its own carrying capacity."
            % (act_id, model["prey_cap_mult"]))

    series = a["series"]
    for f in ("prey", "pred"):
        s = series.get(f) or {}
        if not (s.get("name") and s.get("colour_token")):
            raise ValueError(
                "cycle-runner %r series %r needs `name` and `colour_token`. "
                "The name is the live readout's label and the token is the "
                "bar's fill — the caption reads the two colours out by name, "
                "so neither is decoration." % (act_id, f))
        if not str(s["colour_token"]).startswith("--ks3-"):
            raise ValueError(
                "cycle-runner %r series %r names colour token %r. Only the "
                "shipped KS3 palette is reachable from a page; an arbitrary "
                "value here is a styling backdoor around the parity gate."
                % (act_id, f, s["colour_token"]))

    notes = a["notes"]
    got = [n.get("id") for n in notes]
    if got != list(_B9_CYCLE_NOTES):
        raise ValueError(
            "cycle-runner %r declares note branches %s. The seven are fixed "
            "and "
            "ORDERED — %s — because first match wins and %r must be tested "
            "before %r or the ceiling note never fires and 'Remove every fox' "
            "stops teaching carrying capacity."
            % (act_id, got, list(_B9_CYCLE_NOTES),
               "no_pred_at_ceiling", "no_pred"))
    for n in notes:
        if not n.get("text"):
            raise ValueError(
                "cycle-runner %r note %r has no text. Every branch is a state "
                "the field can be left in, and a blank one reads as the bench "
                "having stopped responding." % (act_id, n["id"]))

    prey_name = _b8_plain(series["prey"]["name"], act_id, "series prey `name`")
    pred_name = _b8_plain(series["pred"]["name"], act_id, "series pred `name`")
    note_map = dict((n["id"], _b8_plain(n["text"], act_id,
                                        "note %r" % n["id"])) for n in notes)
    mdl = dict((f, float(model[f])) for f in _B9_CYCLE_MODEL)

    # The resting chart is Design's opening history: exactly one year, the
    # starting pair. `maxPrey`/`maxPred` carry their own floors, so the two
    # bars are already on two scales in the shipped bytes.
    p0, q0 = mdl["start_prey"], mdl["start_pred"]
    max_prey = max(600.0, p0)
    max_pred = max(150.0, q0)

    return ('<div class="ks3-cy" data-cy data-model="%s" data-notes="%s" '
            'data-prey-name="%s" data-pred-name="%s" data-prey-fill="%s" '
            'data-pred-fill="%s" data-cull-label="%s" '
            'data-restore-label="%s">'
            '<div class="ks3-cy-panel">'
            '<div class="ks3-cy-now">'
            '<p class="ks3-cy-live" data-series="prey">'
            '<span class="ks3-cy-livename">%s</span> '
            '<span class="ks3-cy-liveval" data-cy-prey>%d</span></p>'
            '<p class="ks3-cy-live" data-series="pred">'
            '<span class="ks3-cy-livename">%s</span> '
            '<span class="ks3-cy-liveval" data-cy-pred>%d</span></p></div>'
            '<div class="ks3-cy-chart" data-cy-chart role="img" '
            'aria-label="%s">%s</div>'
            '<p class="ks3-cy-caption">%s</p>'
            '<p class="ks3-cy-note" data-cy-note>%s</p>'
            '<div class="ks3-cy-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-cy-btn" '
            'data-cy-year>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-cy-btn" '
            'data-cy-ten>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-cy-btn" '
            'data-cy-cull>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-cy-btn" '
            'data-cy-reset>%s</button></div></div></div>'
            % (_b9_json(mdl), _b9_json(note_map), e(prey_name), e(pred_name),
               e(series["prey"]["colour_token"]),
               e(series["pred"]["colour_token"]),
               e(_b8_plain(a["cull_label"], act_id, "`cull_label`")),
               e(_b8_plain(a["restore_label"], act_id, "`restore_label`")),
               t(series["prey"]["name"]), _b8_round(p0),
               t(series["pred"]["name"]), _b8_round(q0),
               e(_b8_plain(a["chart_caption"], act_id, "`chart_caption`")),
               _b9_cycle_bars(series, p0, q0, max_prey, max_pred),
               t(a["chart_caption"]), t(note_map["year_zero"]),
               t(a["year_label"]), t(a["ten_label"]), t(a["cull_label"]),
               t(a["reset_label"])))
def _b9_cycle_bars(series, prey, pred, max_prey, max_pred):
    """One year of the chart: a paired amber and green bar on two scales."""
    return ('<span class="ks3-cy-year">'
            '<span class="ks3-cy-bar" data-series="prey" '
            'style="--cy-fill: var(%s); height: %s%%"></span>'
            '<span class="ks3-cy-bar" data-series="pred" '
            'style="--cy-fill: var(%s); height: %s%%"></span></span>'
            % (e(series["prey"]["colour_token"]),
               e(_pctnum(max(2.0, (prey / max_prey) * 100.0))),
               e(series["pred"]["colour_token"]),
               e(_pctnum(max(2.0, (pred / max_pred) * 100.0)))))
# ── b9-03 `#s-bench` · remove-a-species ──────────────────────────────────

def r_remove_a_species(a, act_id):
    """⊕ b9-03 `#s-bench` — take one out of an oak wood and follow it.

    ⚖️ THE BEES ARE IN THE WEB WITH NO FEEDING LINE, DELIBERATELY. `web_lines`
    gives them a SERVICE — they pollinate the wildflowers — and nothing in the
    wood eats them. Removing them still empties the web three rounds later, and
    the verdict says so: feeding is not the only kind of dependence. That is
    the setup for b9-04 and it is the strongest link in the unit. A revision
    that "tidies" the web by giving the bees a feeding line, or drops them
    because they have none, destroys it.

    ⚖️ THE OAK IS THE ONE REMOVAL WHERE THE WEB DOES NOT REORGANISE. Every
    other verdict describes a redistribution; the producer's describes a loss
    the web cannot absorb. It is the contrast case, and it is why there are six
    removals rather than five.

    ⚠️ EXACTLY THREE ROUNDS PER SPECIES, AND AN EMPTY ONE IS REFUSED. Design's
    `caterpillars` carries a fourth round object — `{ title: '', body: '' }` —
    which her renderer filters out at draw time (`sp.rounds.filter(r => r.title)`)
    so the page never shows it and the counter still reads "of 3". It is an
    editing artefact. This renderer has no filter and does not want one: an
    empty round is a dead payload entry under R5 and a blank row on the page,
    and refusing it at build time is how the authoring pass finds out.

    ⚠️ EVERY SPECIES' PANEL IS IN THE DOCUMENT and only one is shown. Design
    resets `shown` to 0 on every tab press, so the panels do not each keep
    their own progress — the runtime holds one count and redraws.
    """
    _b7_need(a, act_id, ("web_label", "web_lines", "tabs_label", "species",
                         "step_first_label", "step_label",
                         "step_spent_label", "reset_label",
                         "still_here_label", "removed_label"))
    _b9_progress(a.get("progress"), act_id, "remove-a-species",
                 ("none", "mid", "all"))

    for key in ("still_here_label", "removed_label"):
        if "{name}" not in str(a[key]):
            raise ValueError(
                "remove-a-species %r's %s names no {name}. Design composes the "
                "panel's headline from the species' own label — 'Ladybirds — "
                "still in the wood', 'Ladybirds removed' — so the line has to "
                "carry the slot the label goes into." % (act_id, key))

    web_lines = a["web_lines"]
    if len(web_lines) < 6:
        raise ValueError(
            "remove-a-species %r draws %d web line(s). The bench's whole claim "
            "is that a removal reaches species it never touched, which needs a "
            "web with enough in it to reach ACROSS."
            % (act_id, len(web_lines)))

    species = a["species"]
    if len(species) < 4:
        raise ValueError(
            "remove-a-species %r offers %d removal(s). The contrast between a "
            "web that reorganises and a producer whose loss it cannot absorb "
            "is what the set is for." % (act_id, len(species)))

    seen, tabs, panels = set(), [], []
    for i, sp in enumerate(species):
        for f in ("id", "label", "why", "rounds", "verdict"):
            if not sp.get(f):
                raise ValueError(
                    "remove-a-species %r species %r declares no %r."
                    % (act_id, sp.get("id"), f))
        if sp["id"] in seen:
            raise ValueError("remove-a-species %r declares species id %r twice."
                             % (act_id, sp["id"]))
        seen.add(sp["id"])
        rounds = sp["rounds"]
        if len(rounds) != 3:
            raise ValueError(
                "remove-a-species %r species %r declares %d round(s). Three, "
                "on every species, because the counter says 'of 3' and because "
                "the third round is where the consequence has travelled far "
                "enough to be surprising. Design's `caterpillars` carries a "
                "FOURTH, empty, and filters it out at draw time — that is an "
                "editing artefact and it is not carried across."
                % (act_id, sp["id"], len(rounds)))
        for j, r in enumerate(rounds, 1):
            if not (r.get("title") and r.get("body")):
                raise ValueError(
                    "remove-a-species %r species %r round %d is missing "
                    "`title` or `body`. An empty round draws a numbered row "
                    "with nothing in it and counts towards 'all three rounds'."
                    % (act_id, sp["id"], j))

        first = i == 0
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-rs-tab" '
            'data-rs-species="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(sp["id"]), "true" if first else "false", t(sp["label"])))

        rows = "".join(
            '<li class="ks3-rs-round" data-i="%d">'
            '<span class="ks3-rs-num" aria-hidden="true">%d</span>'
            '<span class="ks3-rs-roundmain">'
            '<span class="ks3-rs-roundtitle">%s</span>'
            '<span class="ks3-rs-roundbody" hidden>%s</span></span></li>'
            % (j, j + 1, t(r["title"]), t(r["body"]))
            for j, r in enumerate(rounds))

        panels.append(
            '<div class="ks3-rs-panel" data-rs-panel="%s" data-total="%d" '
            'data-label="%s"%s>'
            '<p class="ks3-rs-headline" data-rs-headline>%s</p>'
            '<p class="ks3-rs-why">%s</p>'
            '<ol class="ks3-rs-rounds" role="list">%s</ol>'
            '<p class="ks3-rs-verdict" data-rs-verdict hidden>%s</p></div>'
            % (e(sp["id"]), len(rounds),
               e(_b8_plain(sp["label"], act_id, "species %r `label`" % sp["id"])),
               "" if first else " hidden",
               t(str(a["still_here_label"]).replace("{name}", sp["label"])),
               t(sp["why"]), rows, rich(sp["verdict"])))

    return ('<div class="ks3-rs" data-rs data-still-label="%s" '
            'data-removed-label="%s" data-first-label="%s" '
            'data-step-label="%s" data-spent-label="%s">'
            '<div class="ks3-rs-web">'
            '<p class="ks3-rs-weblabel">%s</p>'
            '<ul class="ks3-rs-weblines" role="list">%s</ul></div>'
            '<div class="ks3-rs-tabsgroup">'
            '<p class="ks3-rs-tabslabel" id="%s-remove">%s</p>'
            '<ul class="ks3-options ks3-rs-tabs" role="list" '
            'aria-labelledby="%s-remove">%s</ul></div>'
            '<div class="ks3-rs-body">%s'
            '<div class="ks3-rs-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-rs-next" '
            'data-rs-next>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-rs-reset" '
            'data-rs-reset>%s</button></div></div></div>'
            % (e(_b8_plain(a["still_here_label"], act_id,
                           "`still_here_label`")),
               e(_b8_plain(a["removed_label"], act_id, "`removed_label`")),
               e(_b8_plain(a["step_first_label"], act_id,
                           "`step_first_label`")),
               e(_b8_plain(a["step_label"], act_id, "`step_label`")),
               e(_b8_plain(a["step_spent_label"], act_id,
                           "`step_spent_label`")),
               t(a["web_label"]),
               "".join('<li class="ks3-rs-webline">%s</li>' % t(w)
                       for w in web_lines),
               e(act_id), t(a["tabs_label"]), e(act_id), "".join(tabs),
               "".join(panels), t(a["step_first_label"]),
               t(a["reset_label"])))
# ── b9-04 `#s-bench` · supermarket-shelf ─────────────────────────────────

def r_supermarket_shelf(a, act_id):
    """⊕ b9-04 `#s-bench` — twelve foods, and two numbers that fall differently.

    ⚖️ THE GAP BETWEEN THE TWO BARS IS THE ENTIRE LESSON. Two bars, two
    colours, two labels, two percentages, side by side and never combined. The
    `none` note reads the gap aloud — nobody starves on what is left, and
    nobody stays healthy on it either — and rung 2 marks a student for knowing
    which of the two falls further. A revision that merges them into one 'food'
    bar, renders them stacked, or drops one for space at a narrow breakpoint
    deletes the lesson, so: the grid is `repeat(auto-fit, minmax(220px, 1fr))`
    and wraps to two ROWS rather than merging, there is a parity row on the
    container at a narrow viewport, and this renderer REFUSES a payload whose
    two bars land on the same percentage when the pollinators are gone.

    ⚖️ AND THE DIAL DOUBLES AS THE TEACHING LABEL. At full pollination each
    tile shows the food's `how` — wind-pollinated, grown from tubers,
    pollinated by midges — rather than a status, so a student reads WHY a food
    is about to survive before finding out that it does.

    ⚠️ THREE STATES, TWO BUTTONS, AND NO PATH FROM `half` BACK TO `all`. That
    is Design's, measured, and it is left alone: *Remove every insect
    pollinator* toggles `none ↔ all`, *Lose half of them* sets `half`
    unconditionally. Inventing a third button would be inventing a control.
    """
    _b7_need(a, act_id, ("foods", "bars", "remove_label", "restore_label",
                         "half_label", "notes"))
    # ⚠️ THREE NAMED STATES WITH NO NUMBER IN ANY OF THEM, so this one alone
    # among the six needs no derivation — `_progress_readout` draws it as
    # authored. It still goes through `_KIND_HEAD_FROM` like its five siblings,
    # because reading `progress` here is what puts the kind into
    # `_KIND_FN_OWNS_PROGRESS`, and a kind in that set gets no head row at all
    # unless something hands one back.
    pg = _b9_progress(a.get("progress"), act_id, "supermarket-shelf",
                      ("all", "half", "none"))
    if list(pg)[0] != "all":
        raise ValueError(
            "supermarket-shelf %r opens its progress on %r. `_progress_readout` "
            "prints the FIRST authored state at rest and the shelf opens "
            "intact, so a page with the pollinators still on it would ship "
            "bytes saying they were gone." % (act_id, list(pg)[0]))

    foods = a["foods"]
    if len(foods) < 8:
        raise ValueError(
            "supermarket-shelf %r stocks %d food(s). The argument is a WEEKLY "
            "SHOP — that most of the calories survive and most of the variety "
            "does not — and it cannot be made from a handful."
            % (act_id, len(foods)))

    bars = a["bars"]
    if [b.get("id") for b in bars] != ["cal", "vit"]:
        raise ValueError(
            "supermarket-shelf %r declares bars %s. Exactly two, `cal` then "
            "`vit`, because the GAP between them is the lesson and the order "
            "is the order the note reads them out in."
            % (act_id, [b.get("id") for b in bars]))
    for b in bars:
        if not (b.get("label") and b.get("colour_token")):
            raise ValueError(
                "supermarket-shelf %r bar %r needs `label` and `colour_token`. "
                "Two labels and two colours is what stops them reading as one "
                "quantity." % (act_id, b.get("id")))
        if not str(b["colour_token"]).startswith("--ks3-"):
            raise ValueError(
                "supermarket-shelf %r bar %r names colour token %r. Only the "
                "shipped KS3 palette is reachable from a page."
                % (act_id, b["id"], b["colour_token"]))

    cal_max = vit_max = 0.0
    cal_gone = vit_gone = 0.0
    deps = set()
    for f in foods:
        for key in ("name", "how"):
            if not f.get(key):
                raise ValueError(
                    "supermarket-shelf %r food %r declares no %r. `how` is "
                    "what the tile reads at full pollination — the dial "
                    "doubles as the teaching label." % (act_id, f.get("name"), key))
        for key in ("cal", "vit"):
            if f.get(key) is None:
                raise ValueError(
                    "supermarket-shelf %r food %r declares no %r share. A food "
                    "with no share contributes nothing to either bar and is a "
                    "tile that cannot move." % (act_id, f["name"], key))
        dep = float(f.get("dep") or 0)
        if not 0 <= dep <= 1:
            raise ValueError(
                "supermarket-shelf %r food %r has dep %r. It is the FRACTION "
                "of the crop lost with no insect pollinators, so it lives "
                "between 0 and 1." % (act_id, f["name"], f["dep"]))
        deps.add(dep)
        cal_max += float(f["cal"])
        vit_max += float(f["vit"])
        cal_gone += float(f["cal"]) * (1 - dep)
        vit_gone += float(f["vit"]) * (1 - dep)
    if cal_max <= 0 or vit_max <= 0:
        raise ValueError(
            "supermarket-shelf %r's shelf carries no calories or no vitamins. "
            "Both bars are percentages of a total and neither total can be "
            "zero." % act_id)
    if 0.0 not in deps:
        raise ValueError(
            "supermarket-shelf %r stocks nothing with dep 0. The four "
            "wind-pollinated staples are the reason the calorie bar survives, "
            "and without one the bench teaches 'no bees, no food' — which is "
            "the belief `#s-think` exists to break." % act_id)
    if max(deps) < 1.0:
        raise ValueError(
            "supermarket-shelf %r stocks nothing that is entirely "
            "insect-pollinated. A shelf where every tile only dims never shows "
            "a food GO, and 'gone' is the tile state the lesson turns on."
            % act_id)

    cal_pct = _b8_round(cal_gone / cal_max * 100.0)
    vit_pct = _b8_round(vit_gone / vit_max * 100.0)
    if cal_pct == vit_pct:
        raise ValueError(
            "supermarket-shelf %r lands both bars on %d%% with the pollinators "
            "gone. THE GAP BETWEEN THE TWO BARS IS THE ENTIRE LESSON — the "
            "`none` note reads it aloud and rung 2 marks a student for knowing "
            "which falls further. Two bars that agree are one bar drawn twice."
            % (act_id, cal_pct))
    if vit_pct >= cal_pct:
        raise ValueError(
            "supermarket-shelf %r loses %d%% of its calories and %d%% of its "
            "vitamins. The claim the unit makes — cereals carry the calories, "
            "insect-pollinated crops carry the variety — is that the VITAMIN "
            "bar falls further. This shelf says the opposite."
            % (act_id, 100 - cal_pct, 100 - vit_pct))

    notes = a["notes"]
    for f in ("all", "none", "half"):
        if not notes.get(f):
            raise ValueError("supermarket-shelf %r notes declares no %r."
                             % (act_id, f))
    _b9_placeholders(notes["none"], act_id, "note `none`", ("{cal}", "{vit}"))

    tiles = "".join(
        '<li class="ks3-ss-food" data-ss-food="%d" data-dep="%s" '
        'data-how="%s">'
        '<p class="ks3-ss-foodname">%s</p>'
        '<p class="ks3-ss-foodstatus" data-ss-status>%s</p></li>'
        % (i, e(_pctnum(f.get("dep") or 0)),
           e(_b8_plain(f["how"], act_id, "food %r `how`" % f["name"])),
           t(f["name"]), t(f["how"]))
        for i, f in enumerate(foods))

    barhtml = "".join(
        '<div class="ks3-ss-bar" data-ss-bar="%s">'
        '<div class="ks3-ss-barhead">'
        '<p class="ks3-ss-barlabel">%s</p>'
        '<p class="ks3-ss-barvalue" data-ss-value>100%%</p></div>'
        '<span class="ks3-ss-track"><span class="ks3-ss-fill" '
        'style="--ss-fill: var(%s); width: 100%%"></span></span></div>'
        % (e(b["id"]), t(b["label"]), e(b["colour_token"]))
        for b in bars)

    return ('<div class="ks3-ss" data-ss data-shares="%s" data-notes="%s" '
            'data-remove-label="%s" data-restore-label="%s" '
            'data-gone-label="%s" data-unaffected-label="%s" '
            'data-part-label="%s">'
            '<ul class="ks3-ss-shelf" role="list">%s</ul>'
            '<div class="ks3-ss-bars">%s</div>'
            '<p class="ks3-ss-note" data-ss-note>%s</p>'
            '<div class="ks3-ss-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ss-toggle" '
            'data-ss-toggle>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-ss-half" '
            'data-ss-half>%s</button></div></div>'
            % (_b9_json([[float(f["cal"]), float(f["vit"]),
                          float(f.get("dep") or 0)] for f in foods]),
               _b9_json(dict((k, _b8_plain(notes[k], act_id, "note %r" % k))
                             for k in ("all", "none", "half"))),
               e(_b8_plain(a["remove_label"], act_id, "`remove_label`")),
               e(_b8_plain(a["restore_label"], act_id, "`restore_label`")),
               e(_b8_plain(a.get("gone_label") or "gone", act_id,
                           "`gone_label`")),
               e(_b8_plain(a.get("unaffected_label") or "unaffected", act_id,
                           "`unaffected_label`")),
               e(_b8_plain(a.get("part_label") or "{n}% of the crop", act_id,
                           "`part_label`")),
               tiles, barhtml, t(notes["all"]),
               t(a["remove_label"]), t(a["half_label"])))
# ── b9-05 `#s-bench` · bioaccumulation ───────────────────────────────────

def r_bioaccumulation(a, act_id):
    """⊕ b9-05 `#s-bench` — one lake, six levels, and a persistence dial.

    ⚖️ THE ×1 SETTING IS THE CONTROL AND IT PRODUCES A FLAT LINE. Its verdict
    is the only one that computes no number: the chemical is excreted as fast
    as it arrives, so no organism holds more than any other. It is what proves
    the mechanism is PERSISTENCE, NOT TOXICITY — the claim rung 1 marks and
    `#s-think` confronts — and removing it as 'the boring one' would remove the
    control from a lesson about controls. The renderer refuses a payload
    without one.

    ⚖️ THE DIAL IS A PERSISTENCE DIAL AND NEVER A TOXICITY DIAL. Nothing on the
    bench varies how poisonous the chemical is; what varies is whether the body
    can get rid of it. Bioaccumulation is driven by FAT-SOLUBILITY, and the
    water-soluble setting is the one that does nothing — that pairing is
    already live as a written distractor and every label here keeps it.

    ⚖️ SIX ROWS, AND THE BENCH WINS OVER THE PROSE. Measured, `persistent` runs
    0.0030 → 0.030 → 0.300 → 3.0 → 30 → 300 ppm and the harmful verdict
    computes 100,000×. The hook, rung 3 and NOTES-B9 all describe five rows and
    ~10,000×. Ruled: the bench is right and the prose is what changes. The
    renderer asserts the persistent setting actually REACHES harm, which is the
    property the lesson depends on, rather than asserting a row count.

    ⚠️ FOUR-BRANCH NUMBER FORMATTING, REPRODUCED EXACTLY: ≥10 → 0 dp, ≥1 → 1
    dp, ≥0.01 → 3 dp, else 4 dp. It is what puts `0.0030` and `300` in the same
    column without either reading as noise, and the runtime and the static
    render share one implementation of it in each language.
    """
    # ⚠️ `harm` IS NOT IN THIS LIST — see the same note on `r_chain_ledger`.
    _b7_need(a, act_id, ("tabs_label", "chemicals", "levels",
                         "harm_verdict", "safe_verdict", "step_label",
                         "step_spent_label", "reset_label", "verdicts"))
    if a.get("harm") is None:
        raise ValueError(
            "bioaccumulation %r declares no `harm` threshold. Every row is "
            "measured against it, so without one no level is ever flagged and "
            "the ospreys' verdict can never fire." % act_id)
    _b9_progress(a.get("progress"), act_id, "bioaccumulation",
                 ("before", "after"))

    harm = float(a["harm"])
    if harm <= 0:
        raise ValueError(
            "bioaccumulation %r puts the harm threshold at %r ppm. Every row "
            "would then read 'above the level that causes harm', including the "
            "lake water, and the bench would be saying the water was the "
            "problem all along." % (act_id, a["harm"]))

    levels = a["levels"]
    if len(levels) < 4:
        raise ValueError(
            "bioaccumulation %r draws %d level(s). The build-up is only "
            "visible over a chain long enough for the multiplication to run "
            "away, and this one is trimmed to where it does not."
            % (act_id, len(levels)))
    for L in levels:
        if not (L.get("name") and L.get("eats")):
            raise ValueError(
                "bioaccumulation %r has a level missing `name` or `eats`. The "
                "`eats` line — eat thousands of algae, eat hundreds of perch a "
                "year — is the MECHANISM: it is why the concentration "
                "multiplies rather than merely persisting."
                % act_id)

    chems = a["chemicals"]
    if len(chems) < 3:
        raise ValueError(
            "bioaccumulation %r offers %d setting(s). Three: it persists, it "
            "is slowly broken down, it is excreted. The middle one is what "
            "stops the lesson reading as a binary, and the third is the "
            "CONTROL — the flat line that proves the mechanism is persistence "
            "and not toxicity." % (act_id, len(chems)))
    seen, factors, ctrl = set(), [], []
    for c in chems:
        for f in ("id", "label", "factor", "start", "tab_note"):
            if c.get(f) is None or c.get(f) == "":
                raise ValueError(
                    "bioaccumulation %r chemical %r declares no %r. The "
                    "`tab_note` is the sentence under the dial that says what "
                    "the setting MEANS, and without it the dial is three "
                    "numbers." % (act_id, c.get("id"), f))
        if c["id"] in seen:
            raise ValueError("bioaccumulation %r declares chemical id %r twice."
                             % (act_id, c["id"]))
        seen.add(c["id"])
        if float(c["factor"]) < 1:
            raise ValueError(
                "bioaccumulation %r chemical %r has factor %r. A factor below "
                "one is a chemical that gets WEAKER up the chain, which is not "
                "a persistence setting and is not a thing that happens."
                % (act_id, c["id"], c["factor"]))
        if float(c["start"]) <= 0:
            raise ValueError(
                "bioaccumulation %r chemical %r starts at %r ppm. The lake is "
                "the source; a source of nothing has nothing to accumulate."
                % (act_id, c["id"], c["start"]))
        factors.append(float(c["factor"]))
        if abs(float(c["factor"]) - 1.0) < 1e-9:
            ctrl.append(c["id"])
    if len(ctrl) != 1:
        raise ValueError(
            "bioaccumulation %r declares %d setting(s) at ×1 (%s). EXACTLY ONE "
            "IS THE CONTROL. The flat line is what proves the mechanism is "
            "persistence and not toxicity — it is the claim rung 1 marks and "
            "`#s-think` confronts, and a bench without it is a bench with no "
            "comparison in it." % (act_id, len(ctrl), ", ".join(ctrl) or "none"))

    top_chem = max(chems, key=lambda c: float(c["factor"]))
    top_conc = float(top_chem["start"]) * (float(top_chem["factor"])
                                           ** (len(levels) - 1))
    if top_conc < harm:
        raise ValueError(
            "bioaccumulation %r's most persistent setting reaches %s ppm "
            "against a harm threshold of %s. Nothing on the bench is ever "
            "flagged as harmful, so the ospreys' verdict never fires and the "
            "lesson's whole consequence is unreachable."
            % (act_id, _b9_ppm(top_conc), _b9_ppm(harm)))

    verdicts = a["verdicts"]
    for f in ("flat", "harmful", "below"):
        if not verdicts.get(f):
            raise ValueError("bioaccumulation %r verdicts declares no %r."
                             % (act_id, f))
    _b9_placeholders(verdicts["flat"], act_id, "verdict `flat`", (),
                     ("{ppm}", "{times}"))
    _b9_placeholders(verdicts["harmful"], act_id, "verdict `harmful`",
                     ("{ppm}", "{times}"))
    _b9_placeholders(verdicts["below"], act_id, "verdict `below`", ("{ppm}",))

    tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-ba-tab" '
        'data-ba-chem="%s" data-factor="%s" data-start="%s" data-note="%s" '
        'aria-pressed="%s"><span class="ks3-opt-label">%s</span>'
        '</button></li>'
        % (e(c["id"]), e(_pctnum(c["factor"])), e(_pctnum(c["start"])),
           e(_b8_plain(c["tab_note"], act_id,
                       "chemical %r `tab_note`" % c["id"])),
           "true" if c is chems[0] else "false", t(c["label"]))
        for c in chems)

    opener = chems[0]
    rows = []
    for i, L in enumerate(levels):
        conc = float(opener["start"]) * (float(opener["factor"]) ** i)
        harmful = conc >= harm
        rows.append(
            '<li class="ks3-ba-level" data-i="%d"%s%s%s>'
            '<div class="ks3-ba-levelhead">'
            '<p class="ks3-ba-name">%s</p>'
            '<p class="ks3-ba-eats">%s</p></div>'
            '<div class="ks3-ba-readout"%s>'
            '<div class="ks3-ba-figs">'
            '<p class="ks3-ba-ppm" data-ba-ppm>%s</p>'
            '<p class="ks3-ba-lvlverdict" data-ba-lvlverdict>%s</p></div>'
            '<span class="ks3-ba-track"><span class="ks3-ba-bar" '
            'data-ba-bar style="width: %s%%"></span></span></div></li>'
            % (i, ' data-shown=""' if i == 0 else "",
               ' data-cur=""' if i == 0 else "",
               ' data-harmful="1"' if harmful else "",
               t(L["name"]), t(L["eats"]), "" if i == 0 else " hidden",
               t(_b9_ppm(conc) + (a.get("ppm_suffix") or " ppm")),
               t(a["harm_verdict"] if harmful else a["safe_verdict"]),
               e(_pctnum(_b9_ba_width(conc, top_conc, harm)))))

    return ('<div class="ks3-ba" data-ba data-harm="%s" data-total="%d" '
            'data-ppm-suffix="%s" data-harm-verdict="%s" '
            'data-safe-verdict="%s" data-step-label="%s" '
            'data-step-spent-label="%s" data-verdict-flat="%s" '
            'data-verdict-harmful="%s" data-verdict-below="%s">'
            '<div class="ks3-ba-tabsgroup">'
            '<p class="ks3-ba-tabslabel" id="%s-chems">%s</p>'
            '<ul class="ks3-options ks3-ba-tabs" role="list" '
            'aria-labelledby="%s-chems">%s</ul></div>'
            '<div class="ks3-ba-panel">'
            '<p class="ks3-ba-chemnote" data-ba-chemnote>%s</p>'
            '<ol class="ks3-ba-levels" role="list">%s</ol>'
            '<div class="ks3-ba-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ba-up" '
            'data-ba-up>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-ba-reset" '
            'data-ba-reset>%s</button></div>'
            '<p class="ks3-ba-verdict" data-ba-verdict hidden>%s</p>'
            '</div></div>'
            % (e(_pctnum(harm)), len(levels),
               e(_b8_plain(a.get("ppm_suffix") or " ppm", act_id,
                           "`ppm_suffix`")),
               e(_b8_plain(a["harm_verdict"], act_id, "`harm_verdict`")),
               e(_b8_plain(a["safe_verdict"], act_id, "`safe_verdict`")),
               e(_b8_plain(a["step_label"], act_id, "`step_label`")),
               e(_b8_plain(a["step_spent_label"], act_id,
                           "`step_spent_label`")),
               e(_b8_plain(verdicts["flat"], act_id, "verdict `flat`")),
               e(_b8_plain(verdicts["harmful"], act_id, "verdict `harmful`")),
               e(_b8_plain(verdicts["below"], act_id, "verdict `below`")),
               e(act_id), t(a["tabs_label"]), e(act_id), tabs,
               t(opener["tab_note"]), "".join(rows),
               t(a["step_label"]), t(a["reset_label"]),
               t(_b9_ba_verdict(a, opener, levels, harm))))
def _b9_ppm(x):
    """Design's four-branch rule: ≥10 → 0 dp · ≥1 → 1 dp · ≥0.01 → 3 dp · 4 dp.

    ⚠️ THE THRESHOLD IS PER VALUE, NOT PER SETTING. On the persistent chemical
    the same column prints `0.0030` and `300`, and that is the rule applied
    honestly: three significant places where the number is small enough to need
    them and none where it is not. Tidying it to one form would either bury the
    lake water in zeroes or print the ospreys to four decimals.
    """
    x = float(x)
    if x >= 10:
        return "%.0f" % x
    if x >= 1:
        return "%.1f" % x
    if x >= 0.01:
        return "%.3f" % x
    return "%.4f" % x
def _b9_ba_width(conc, top_conc, harm):
    """Design's bar: the concentration against the taller of the top and harm."""
    return max(1.0, min(100.0, (conc / max(top_conc, harm)) * 100.0))
def _b9_ba_verdict(a, chem, levels, harm):
    """Which of the three closing lines this setting earns, with its figures."""
    v = a["verdicts"]
    factor, start = float(chem["factor"]), float(chem["start"])
    top = start * (factor ** (len(levels) - 1))
    if abs(factor - 1.0) < 1e-9:
        return v["flat"]
    if top >= harm:
        return (v["harmful"].replace("{ppm}", _b9_ppm(top))
                .replace("{times}", _b8_group(_b8_round(top / start), True)))
    return v["below"].replace("{ppm}", _b9_ppm(top))
# ── b9-06 `#s-bench` · quadrat-bench ─────────────────────────────────────

_B9_QUADRAT_METHODS = ("random", "corner", "path")
def r_quadrat_bench(a, act_id):
    """⊕ b9-06 `#s-bench` — a field you can check your answer against.

    ⚖️ INCREASING THE SAMPLE SIZE FIXES THE RANDOM CASE AND DOES NOTHING FOR
    THE TWO BIASED ONES. That separation is the whole instrument and it falls
    out of the POOLS rather than out of any special-casing: 3 → 8 → 25 random
    squares converge on the true mean, while 25 corner squares are drawn from a
    25-cell pool entirely inside the cluster — so the largest sample on the
    biased setting is the most stably wrong, and is in fact DETERMINISTIC,
    because it exhausts its pool. The verdicts say it in words. A revision that
    "balances" the pools, or lets sample size shrink the bias, deletes
    `NOS-04`'s confrontation, so the renderer measures the pools against the
    field's own model and refuses a set that is not biased in both directions.

    ⚠️ THE FIELD IS REGENERATED, UNSEEDED, ON EVERY PAGE LOAD. This is the only
    `Math.random()` in B9 — 100 calls, once, at mount — and it is deliberate:
    two students never see the same field and no student sees the same one
    twice, so the estimate cannot be memorised and the reveal cannot be
    spoiled. Design's legal line states it. It also means the counts CANNOT be
    rendered at build time, which is why the shipped grid is a hundred empty
    cells: that is exactly what an unsurveyed field looks like, so the static
    page is not a placeholder for the live one — it IS the resting state.

    ⚠️ TWO-STAGE COMPLETION, AND THE RAIL TICKS ON THE REVEAL. *Take the
    sample*, then *Show the real total* — the second disabled until the first
    has run, re-sampling clearing the reveal. Design's threshold is
    `s.truthShown` and it is kept; what is not kept is her un-ticking, because
    MRB-208 ruled the rail records participation.
    """
    # ⚠️ `side` IS NOT IN THIS LIST — see the note on `r_chain_ledger`.
    if a.get("side") is None:
        raise ValueError("quadrat-bench %r declares no `side`." % act_id)
    _b7_need(a, act_id, ("field", "methods_label", "methods",
                         "counts_label", "counts", "figures", "sample_label",
                         "resample_label", "truth_label", "captions",
                         "verdicts", "direction"))
    _b9_progress(a.get("progress"), act_id, "quadrat-bench",
                 ("before", "after"))

    side = int(a["side"])
    if side < 5:
        raise ValueError(
            "quadrat-bench %r lays out a %d×%d field. The estimate is a mean "
            "scaled by the number of quadrat-sized areas in the site, and a "
            "site small enough to count by eye is a site nobody would sample."
            % (act_id, side, side))

    fld = a["field"]
    for f in ("centre_row", "centre_col", "reach", "base", "peak", "noise",
              "shade_max"):
        if fld.get(f) is None:
            raise ValueError(
                "quadrat-bench %r field declares no %r. The clustering model "
                "is what makes the two biased methods biased; a missing term "
                "flattens the field and every method then agrees."
                % (act_id, f))
    if float(fld["peak"]) <= 0:
        raise ValueError(
            "quadrat-bench %r's field peaks at %r above base. With no peak the "
            "daisies are spread evenly, the flowery corner is not flowery, and "
            "the bench teaches that placement does not matter."
            % (act_id, fld["peak"]))

    counts = [int(c) for c in a["counts"]]
    if len(counts) < 3 or counts != sorted(counts) or len(set(counts)) != len(counts):
        raise ValueError(
            "quadrat-bench %r offers counts %s. Three or more, strictly "
            "increasing: the dial's argument is what MORE work does, and it "
            "cannot be read off a list that doubles back."
            % (act_id, counts))
    default = int(a.get("default_count") or counts[1 if len(counts) > 1 else 0])
    if default not in counts:
        raise ValueError(
            "quadrat-bench %r opens on %d quadrats, which it does not offer."
            % (act_id, default))

    methods = a["methods"]
    if [m.get("id") for m in methods] != list(_B9_QUADRAT_METHODS):
        raise ValueError(
            "quadrat-bench %r declares methods %s. The three are fixed — %s — "
            "because the POOL each one draws from is the pedagogy and is "
            "implemented against these names in `wireQuadratBench`."
            % (act_id, [m.get("id") for m in methods],
               list(_B9_QUADRAT_METHODS)))
    for m in methods:
        if not m.get("label"):
            raise ValueError("quadrat-bench %r method %r has no label."
                             % (act_id, m["id"]))

    # ⚖️ THE POOLS, MEASURED AGAINST THE FIELD'S OWN MODEL. The noise term is
    # left out on purpose: what is asserted is that the two biased pools sit on
    # systematically richer and poorer ground than the field as a whole, which
    # is a property of WHERE they look and not of the roll of the dice.
    def richness(r, c):
        return max(0.0, 1 - (abs(c - float(fld["centre_col"]))
                             + abs(r - float(fld["centre_row"])))
                   / float(fld["reach"]))

    def density(r, c):
        return float(fld["base"]) + richness(r, c) ** 2 * float(fld["peak"])

    pools = _b9_quadrat_pools(side)
    whole = sum(density(i // side, i % side)
                for i in range(side * side)) / float(side * side)
    for mid, direction in (("corner", 1), ("path", -1)):
        pool = pools[mid]
        if not pool:
            raise ValueError(
                "quadrat-bench %r's %r pool is empty on a %d×%d field."
                % (act_id, mid, side, side))
        mean = sum(density(i // side, i % side) for i in pool) / float(len(pool))
        if direction * (mean - whole) <= 0:
            raise ValueError(
                "quadrat-bench %r's %r pool averages %.2f daisies a square "
                "against the field's %.2f, so it is not biased %s. THE TWO "
                "BIASED POOLS ARE THE INSTRUMENT: bias has no favourite "
                "direction, and one that overstates and one that understates "
                "is what proves it. A field whose cluster has moved leaves both "
                "of them sampling the same ground as everybody else."
                % (act_id, mid, mean, whole,
                   "high" if direction > 0 else "low"))
    if max(counts) < len(pools["corner"]):
        raise ValueError(
            "quadrat-bench %r's largest sample is %d against a corner pool of "
            "%d. The point of the largest setting is that it EXHAUSTS the "
            "biased pool — twenty-five quadrats out of twenty-five squares is "
            "deterministic, so the answer stops wobbling and stays exactly as "
            "wrong. That is what makes bias visibly different from chance."
            % (act_id, max(counts), len(pools["corner"])))

    figures = a["figures"]
    if [f.get("id") for f in figures] != ["mean", "estimate", "real"]:
        raise ValueError(
            "quadrat-bench %r declares figures %s. Three, in this order: the "
            "mean, what it scales up to, and the answer — which stays hidden "
            "until the student has committed to the other two."
            % (act_id, [f.get("id") for f in figures]))
    if not figures[2].get("hidden_value"):
        raise ValueError(
            "quadrat-bench %r's `real` figure declares no `hidden_value`. The "
            "slot is on screen from the start and says so; a blank one looks "
            "like the bench failing to compute it." % act_id)
    for f in figures:
        if not f.get("label"):
            raise ValueError("quadrat-bench %r figure %r has no label."
                             % (act_id, f["id"]))

    caps = a["captions"]
    for f in ("unsampled", "sampled", "revealed"):
        if not caps.get(f):
            raise ValueError("quadrat-bench %r captions declares no %r."
                             % (act_id, f))

    verdicts = a["verdicts"]
    for f in ("corner", "path", "chance", "good"):
        if not verdicts.get(f):
            raise ValueError("quadrat-bench %r verdicts declares no %r."
                             % (act_id, f))
    _b9_placeholders(verdicts["corner"], act_id, "verdict `corner`",
                     ("{err}", "{dir}"))
    _b9_placeholders(verdicts["path"], act_id, "verdict `path`", ("{err}",))
    _b9_placeholders(verdicts["chance"], act_id, "verdict `chance`", ("{err}",))
    _b9_placeholders(verdicts["good"], act_id, "verdict `good`",
                     ("{err}", "{n}"))
    direction = a["direction"]
    for f in ("over", "under"):
        if not direction.get(f):
            raise ValueError(
                "quadrat-bench %r direction declares no %r. The corner verdict "
                "reads 'and far too high' or 'and wrong' depending on which "
                "way the error fell, and the two are not interchangeable."
                % (act_id, f))

    method_tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-qb-tab" '
        'data-qb-method="%s" aria-pressed="%s">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(m["id"]), "true" if m["id"] == methods[0]["id"] else "false",
           t(m["label"]))
        for m in methods)
    count_tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-qb-tab '
        'ks3-qb-counttab" data-qb-count="%d" aria-pressed="%s">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (c, "true" if c == default else "false",
           t((a.get("count_label") or "{n} quadrats").replace("{n}", str(c))))
        for c in counts)

    cells = "".join('<span class="ks3-qb-cell" data-i="%d"></span>' % i
                    for i in range(side * side))
    figs = "".join(
        '<li class="ks3-qb-figure" data-qb-figure="%s">'
        '<p class="ks3-qb-figlabel">%s</p>'
        '<p class="ks3-qb-figvalue" data-qb-fig="%s">%s</p></li>'
        % (e(f["id"]), t(f["label"]), e(f["id"]),
           t(f.get("hidden_value") or "0"))
        for f in figures)

    return ('<div class="ks3-qb" data-qb data-side="%d" data-field="%s" '
            'data-count="%d" data-sample-label="%s" data-resample-label="%s" '
            'data-caption-unsampled="%s" data-caption-sampled="%s" '
            'data-caption-revealed="%s" data-hidden-value="%s" '
            'data-verdicts="%s" data-direction="%s">'
            '<div class="ks3-qb-dials">'
            '<div class="ks3-qb-dial">'
            '<p class="ks3-qb-diallabel" id="%s-where">%s</p>'
            '<ul class="ks3-options ks3-qb-tabs" role="list" '
            'aria-labelledby="%s-where">%s</ul></div>'
            '<div class="ks3-qb-dial">'
            '<p class="ks3-qb-diallabel" id="%s-many">%s</p>'
            '<ul class="ks3-options ks3-qb-tabs" role="list" '
            'aria-labelledby="%s-many">%s</ul></div></div>'
            '<div class="ks3-qb-panel">'
            '<div class="ks3-qb-grid" data-qb-grid role="img" '
            'aria-label="%s" style="--qb-cols: %d">%s</div>'
            '<p class="ks3-qb-caption" data-qb-caption>%s</p>'
            '<ul class="ks3-qb-figures" data-qb-figures role="list" hidden>'
            '%s</ul>'
            '<div class="ks3-qb-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-qb-sample" '
            'data-qb-sample>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-qb-truth" '
            'data-qb-truth disabled>%s</button></div>'
            '<p class="ks3-qb-verdict" data-qb-verdict hidden></p>'
            '</div></div>'
            % (side,
               _b9_json(dict((k, float(fld[k]))
                             for k in ("centre_row", "centre_col", "reach",
                                       "base", "peak", "noise", "shade_max"))),
               default,
               e(_b8_plain(a["sample_label"], act_id, "`sample_label`")),
               e(_b8_plain(a["resample_label"], act_id, "`resample_label`")),
               e(_b8_plain(caps["unsampled"], act_id, "caption `unsampled`")),
               e(_b8_plain(caps["sampled"], act_id, "caption `sampled`")),
               e(_b8_plain(caps["revealed"], act_id, "caption `revealed`")),
               e(_b8_plain(figures[2]["hidden_value"], act_id,
                           "`hidden_value`")),
               _b9_json(dict((k, _b8_plain(verdicts[k], act_id,
                                           "verdict %r" % k))
                             for k in ("corner", "path", "chance", "good"))),
               _b9_json(dict((k, _b8_plain(direction[k], act_id,
                                           "direction %r" % k))
                             for k in ("over", "under"))),
               e(act_id), t(a["methods_label"]), e(act_id), method_tabs,
               e(act_id), t(a["counts_label"]), e(act_id), count_tabs,
               e(caps["unsampled"]), side, cells, t(caps["unsampled"]), figs,
               t(a["sample_label"]), t(a["truth_label"])))
def _b9_quadrat_pools(side):
    """Design's three sampling pools, by the rules on her own page.

    ⚖️ `random` IS EVERY SQUARE, `corner` IS THE BOTTOM-LEFT QUADRANT AND
    `path` IS THE TOP THREE ROWS, and the sizes that fall out — 100, 25, 30 —
    are not balanced and must not be. The corner pool is small enough for the
    largest sample setting to exhaust it, which is what makes the biased answer
    stop wobbling without getting any better.
    """
    return {
        "random": list(range(side * side)),
        "corner": [i for i in range(side * side)
                   if i // side >= side // 2 and i % side <= (side // 2) - 1],
        "path": [i for i in range(side * side) if i // side <= 2],
    }


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'cycle-lag': _cycle_lag,
    'food-web': _food_web,
}

KIND_SHELL = {
    'chain-ledger': ("ks3-cl-block",
                         ' data-instrument data-clblock data-stage-done="0"'),
    'cycle-runner': ("ks3-cy-block",
                         ' data-instrument data-cyblock data-stage-done="0"'),
    'remove-a-species': ("ks3-rs-block",
                         ' data-instrument data-rsblock data-stage-done="0"'),
    'supermarket-shelf': ("ks3-ss-block",
                          ' data-instrument data-ssblock data-stage-done="0"'),
    'bioaccumulation': ("ks3-ba-block",
                         ' data-instrument data-bablock data-stage-done="0"'),
    'quadrat-bench': ("ks3-qb-block",
                         ' data-instrument data-qbblock data-stage-done="0"'),
}

KIND_FN = {
    'chain-ledger': r_chain_ledger,
    'cycle-runner': r_cycle_runner,
    'remove-a-species': r_remove_a_species,
    'supermarket-shelf': r_supermarket_shelf,
    'bioaccumulation': r_bioaccumulation,
    'quadrat-bench': r_quadrat_bench,
}

KIND_HEAD_TOTAL = {
    'chain-ledger': lambda a: len(((a.get("chains") or [{}])[0]).get("levels") or []),
    'remove-a-species': lambda a: len(((a.get("species") or [{}])[0]).get("rounds") or []),
    'bioaccumulation': lambda a: len(a.get("levels") or []),
    'quadrat-bench': lambda a: int(a.get("side") or 0) ** 2,
}

KIND_HEAD_FROM = {
    'chain-ledger': lambda a: _b9_head(
        a, "chain-ledger", ("before", "after"),
        lambda pg: {"format": pg["before"], "full": pg["after"], "start": 1}),
    'cycle-runner': lambda a: _b9_head(
        a, "cycle-runner", ("prefix",),
        lambda pg: {"format": "%s{n}" % pg["prefix"], "start": 0}),
    'remove-a-species': lambda a: _b9_head(
        a, "remove-a-species", ("none", "mid", "all"),
        lambda pg: {"format": pg["mid"], "zero": pg["none"],
                    "full": pg["all"], "start": 0}),
    'supermarket-shelf': lambda a: _b9_head(
        a, "supermarket-shelf", ("all", "half", "none"), lambda pg: pg),
    'bioaccumulation': lambda a: _b9_head(
        a, "bioaccumulation", ("before", "after"),
        lambda pg: {"format": pg["before"], "full": pg["after"], "start": 1}),
    'quadrat-bench': lambda a: _b9_head(
        a, "quadrat-bench", ("before", "after"),
        lambda pg: {"format": pg["after"], "zero": pg["before"], "start": 0}),
}
